/* Monetag (In-Page Push + Vignette) - first-party, consent-aware loader.
 *
 * WHY THIS FILE EXISTS
 * Monetag's dashboard snippet is an inline <script>. The site's Content-Security-
 * Policy is script-src 'self' https: with no unsafe-inline, so an inline snippet
 * would be blocked and never run. This external, first-party file ('self') does
 * exactly what that snippet does - append <script data-zone="ZONE" src="..."> to
 * the page - so the policy is not weakened.
 *
 * WHERE THE ZONES COME FROM
 * Nothing is hard-coded here. site.config.json -> monetag lists the zones, and
 * scripts/inject-ads.py renders one hidden marker per enabled zone into the page,
 * before </body>, followed by the tag for this file:
 *
 *   <div data-adband="monetag" data-ad-unit="vignette" data-ad-zone="ZONE"
 *        data-ad-src="https://host/script.js" hidden></div>
 *
 * The zones are therefore visible in "View page source", and switching a zone on,
 * off or to a new id is a config edit plus a rebuild - never a JavaScript edit.
 * No markers on the page (a noindex stub, or monetag.enabled false) -> this file
 * does nothing at all.
 *
 * EVERY PAGE LOAD, NO LOCAL CAP
 * Both zones are requested on every page view that carries the markers. There is
 * no frequency cap, no counter and no timer in this file, and it reads and writes
 * no cookie, localStorage or sessionStorage. This is deliberate: Vignette is
 * shown at page transitions, and this site is a multi-page site, so each
 * navigation is a fresh page load - the only way Vignette can ever run between
 * pages is for its script to be present on every one. How often an ad actually
 * appears is Monetag's own decision. (An earlier version capped Vignette to 4
 * loads per 4 hours and Push to 12 per 12 hours in localStorage; both caps are
 * gone, and scripts/test-ad-consent.js fails if either returns.)
 *
 * CONSENT - the same gate as /assets/adsterra-loader.js
 *   - Outside the EEA, UK and Switzerland: loads both zones immediately.
 *   - Inside them: waits for a granted ad-consent signal from Google's CMP and
 *     only then loads the zones. If consent is refused, or never given, nothing
 *     loads and no request is made to Monetag at all.
 * The region is decided by IANA timezone, not by IP: there is no geo-IP service
 * on the site, and adding one to decide ad loading would be its own privacy
 * problem. Europe/* timezones cover the EEA, UK and Switzerland and a few non-EEA
 * European countries as well, which errs on the side of withholding an ad. Keep
 * the gate below behaviourally identical to the Adsterra loader's; the consent
 * test exercises both loaders through the same cases.
 *
 * WHAT THIS FILE DOES NOT CONTROL
 * This file sets no cookies, stores nothing and creates no identifiers. The two
 * Monetag scripts it loads are third-party code: once running they make their own
 * requests and may use their own cookies or browser storage and device
 * identifiers (the privacy page says so). That is why they sit behind the
 * consent gate in Europe rather than loading with the page.
 */
(function () {
  "use strict";

  // Guard against the tag being present twice: a second copy would otherwise
  // wrap dataLayer.push again and load every zone a second time.
  if (window.__brymeMonetagLoader) return;
  window.__brymeMonetagLoader = true;

  var units = [].slice.call(document.querySelectorAll(
    '[data-adband="monetag"][data-ad-src][data-ad-zone]'));
  if (!units.length) return;

  var done = false;
  var seen = {};
  function load() {
    if (done) return;
    done = true;
    // Same target as Monetag's own snippet: <body>, else <html> if the body
    // does not exist yet.
    var target = document.body || document.documentElement;
    units.forEach(function (unit) {
      var src = unit.getAttribute("data-ad-src") || "";
      var zone = unit.getAttribute("data-ad-zone") || "";
      // Defence in depth: only a plain https URL and a numeric zone id are ever
      // turned into a script, whatever a marker happens to say.
      if (!/^https:\/\/[^\s"'<>]+$/i.test(src) || !/^[0-9]{4,12}$/.test(zone)) return;
      var key = zone + "|" + src;
      if (seen[key]) return;
      seen[key] = true;
      var s = document.createElement("script");
      // The zone must be on the element before it fetches: Monetag's script
      // reads it from its own <script> tag when it starts.
      s.setAttribute("data-zone", zone);
      s.src = src;
      target.appendChild(s);
    });
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
  // array-like argument, not as three arguments. Both shapes are accepted: the
  // arguments object gtag sends, and a plain array pushed by anything else.
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
