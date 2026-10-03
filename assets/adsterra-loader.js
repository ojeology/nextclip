/* Adsterra Native Banner - consent-aware loader.
 *
 * WHY THIS FILE EXISTS
 * The banner used to be loaded by a bare <script async src="//host/key/invoke.js">
 * in the page. That tag executes for every visitor, in every region, before any
 * consent is given. Google's Consent Mode v2 defaults (see /assets/gtag-init.js)
 * gate GOOGLE tags only - they cannot stop a third-party network's script, and
 * Google's EU user consent policy requires consent to cover the publisher's
 * partners too, not just Google's own ad tech. So an EEA/UK/Swiss visitor was
 * being served an ad-network script before choosing anything.
 *
 * WHAT IT DOES
 *   - Outside the EEA, UK and Switzerland: loads the units immediately, exactly
 *     as before. Lagos, New York, Delhi, Toronto traffic is untouched.
 *   - Inside them: waits for a granted ad-consent signal from Google's CMP and
 *     only then loads the units. If consent is refused, or never given, nothing
 *     loads and no third-party request is made.
 *
 * Three unit kinds ride this gate (see data-ad-kind on each slot):
 *   - native  : Adsterra Native Banner - the script is appended to the page.
 *   - social  : Adsterra Social Bar - same; the script mounts its own widget.
 *   - display : classic atOptions banner - invoke.js needs a global atOptions
 *     config, and the CSP bans inline scripts, so the loader sets that object
 *     on a dedicated iframe and loads invoke.js inside it.
 *
 * HOW THE REGION IS DECIDED
 * By IANA timezone, not by IP. There is no geo-IP service on the site and adding
 * one to decide ad loading would be its own privacy problem. Europe/* timezones
 * cover the EEA, UK and Switzerland and also a few non-EEA European countries
 * (Serbia, Turkey, Ukraine, and others). That error is in the safe direction: it
 * can only withhold an ad from someone who was not legally required to consent,
 * never serve one to someone who was.
 *
 * Adsterra install verification: the loader URL is still visible in page source,
 * on the container itself, as data-ad-src="https://host/key/invoke.js". To go
 * back to the plain inline tag, set adsterra.gateConsent to false in
 * site.config.json and rebuild - but read the paragraph above first.
 *
 * No cookies, no storage, no identifiers are set by this file. It reads one data
 * attribute and adds one script tag.
 */
(function () {
  "use strict";

  // Multi-placement: every rendered native slot carries its own data-ad-src
  // (one Adsterra unit key per placement - see scripts/inject-ads.py).
  var slots = [].slice.call(document.querySelectorAll(
    '.adband-slot[data-ad-src], [data-adband="adsterra-social"][data-ad-src]'));
  if (!slots.length) return;

  var loadedSrcs = {};
  var done = false;
  function load() {
    if (done) return;
    done = true;
    slots.forEach(function (slot) {
      var src = slot.getAttribute("data-ad-src");
      if (!src || loadedSrcs[src]) return;
      loadedSrcs[src] = true;
      var kind = slot.getAttribute("data-ad-kind") || "native";
      if (kind === "display") { loadDisplay(slot, src); return; }
      // native banner and social bar: both are plain external scripts; the
      // social bar script mounts its own floating widget once it runs.
      var s = document.createElement("script");
      s.async = true;
      s.setAttribute("data-cfasync", "false");
      s.src = src;
      (document.head || document.documentElement).appendChild(s);
    });
  }

  // Classic atOptions display banner. The network's invoke.js expects a global
  // `atOptions` config object and then renders the creative. The dashboard
  // snippet ships that config as an inline script, which the site CSP bans -
  // so this loader, which is first-party ('self'), sets the object itself on a
  // fresh same-origin iframe's window and loads invoke.js inside that iframe.
  // Whatever the network's script does next (document.write or DOM insertion)
  // stays contained in the iframe and can never touch the page.
  function loadDisplay(slot, src) {
    try {
      var f = document.createElement("iframe");
      f.width = slot.getAttribute("data-ad-width") || "300";
      f.height = slot.getAttribute("data-ad-height") || "250";
      f.setAttribute("frameborder", "0");
      f.setAttribute("scrolling", "no");
      f.setAttribute("aria-label", "advertisement");
      f.style.border = "0";
      f.style.display = "block";
      f.style.margin = "0 auto";
      slot.appendChild(f);
      var win = f.contentWindow;
      var d = f.contentDocument || (win && win.document);
      if (!win || !d) { throw new Error("no iframe document"); }
      win.atOptions = {
        key: slot.getAttribute("data-ad-key") || "",
        format: slot.getAttribute("data-ad-format") || "iframe",
        height: parseInt(f.height, 10) || 250,
        width: parseInt(f.width, 10) || 300,
        params: {}
      };
      var s = d.createElement("script");
      s.async = true;
      s.setAttribute("data-cfasync", "false");
      s.src = src;
      (d.body || d.documentElement).appendChild(s);
    } catch (e) {
      var s2 = document.createElement("script");
      s2.async = true;
      s2.setAttribute("data-cfasync", "false");
      s2.src = src;
      (document.head || document.documentElement).appendChild(s2);
    }
  }

  function looksEuropean() {
    try {
      var tz = (Intl.DateTimeFormat().resolvedOptions().timeZone || "");
      return /^Europe\//.test(tz);
    } catch (e) {
      return false;
    }
  }

  if (!looksEuropean()) {
    load();
    return;
  }

  // --- EEA / UK / CH: nothing loads until ad consent is granted --------------
  function granted(state) {
    return !!state && (state.ad_storage === "granted" ||
                       state.ad_personalization === "granted" ||
                       state.ad_user_data === "granted");
  }

  // Google's CMP sends gtag('consent', 'update', {...}), and gtag() is
  // `function gtag(){dataLayer.push(arguments)}` - so the signal arrives as ONE
  // array-like argument, not as three arguments. Reading arguments[0] as the
  // string "consent" therefore never matched and the gate never opened. Both
  // shapes are accepted here: the arguments object gtag sends, and a plain array
  // pushed by anything else.
  function consentState(args) {
    var v = args;
    if (args.length === 1 && args[0] && typeof args[0] === "object" &&
        typeof args[0] !== "string") {
      v = args[0];
    }
    if (v && v[0] === "consent" && v[1] === "update") return v[2];
    return null;
  }

  var dl = (window.dataLayer = window.dataLayer || []);
  var nativePush = dl.push;
  dl.push = function () {
    try {
      if (granted(consentState(arguments))) load();
    } catch (e) { /* never let this break the page */ }
    return nativePush.apply(dl, arguments);
  };

  // Fallback for the case where consent was granted before this script ran (it
  // is deferred, so the CMP can beat it): read the resolved state directly, and
  // keep checking for two minutes in case the visitor takes a while.
  function state() {
    try {
      var e = window.google_tag_data && window.google_tag_data.ics &&
              window.google_tag_data.ics.entries;
      if (!e) return null;
      var pick = e.ad_storage || e.ad_personalization || e.ad_user_data;
      return pick ? { ad_storage: pick[1] } : null;
    } catch (err) {
      return null;
    }
  }
  if (granted(state())) { load(); return; }
  var ticks = 0;
  var iv = setInterval(function () {
    ticks += 1;
    if (granted(state())) load();
    if (done || ticks > 120) clearInterval(iv);
  }, 1000);
})();
