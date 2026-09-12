/* BRYME advertising experiment — single 300x250 placement per page (12 Sep 2026).
   v2, DUAL-FILE: identical to ad-slot.js — this path is kept alive because caches worldwide
   still hold pre-rename HTML that points here. Never delete while cached HTML exists.
   Design rules (owner instruction, 12 Sep 2026):
   - ONE placement per page, inserted between content sections, never over content,
     navigation, forms or calculators.
   - The unit runs inside a fixed 300x250 iframe, so it cannot cover anything,
     overflow the viewport, or reflow editorial content.
   - Provider code embedded EXACTLY as supplied: key, format, dimensions, params
     and invoke URL are unaltered.
   - Failsafe: if the provider script is blocked (CSP or network), the slot
     removes itself so pages stay clean and fast.
   - No popunders, no redirects, no aggressive formats are created here. */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return; /* duplicate-load guard */
  window.__BRYME_AD__ = true;

  var PROVIDER_KEY = "51fc16f82ddc690721deee07bcd8bccd";
  var INVOKE_SRC = "https://www.highrevenueformat.com/" + PROVIDER_KEY + "/invoke.js";

  function init() {
    if (document.getElementById("bryme-ad-slot")) return;
    var main = document.querySelector("main") || document.body;

    var slot = document.createElement("div");
    slot.id = "bryme-ad-slot";
    slot.className = "bryme-ad";
    var label = document.createElement("div");
    label.className = "bryme-ad-label";
    label.textContent = "Advertisement";
    var frame = document.createElement("iframe");
    frame.id = "bryme-ad-300x250";
    frame.width = "300";
    frame.height = "250";
    frame.setAttribute("scrolling", "no");
    frame.setAttribute("frameborder", "0");
    frame.setAttribute("title", "Advertisement");
    slot.appendChild(label);
    slot.appendChild(frame);

    /* In-Page Push unit (owner authorization "any ads", 12 Sep 2026): the supplied
       invoke.js + container pair, embedded exactly as provided. On-page format -
       no popunder, no redirect, no new tabs; adult ads remain OFF. */
    var ippScr = document.createElement("script");
    ippScr.async = true;
    ippScr.setAttribute("data-cfasync", "false");
    ippScr.src = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
    slot.appendChild(ippScr);
    var ipp = document.createElement("div");
    ipp.id = "container-ba9b1b5b135e5f465955aadf88ed0ad5";
    ipp.className = "bryme-ad-ipp";
    slot.appendChild(ipp);
    var css2 = document.createElement("style");
    css2.textContent = ".bryme-ad-ipp{margin-top:8px;min-height:0}";
    document.head.appendChild(css2);

    /* content ↓ ad ↓ more content: before the 3rd h2 when the page has one,
       before the 2nd on shorter pages, above the footer otherwise. */
    var h2s = main.querySelectorAll("h2");
    if (h2s.length >= 3) h2s[2].parentNode.insertBefore(slot, h2s[2]);
    else if (h2s.length === 2) h2s[1].parentNode.insertBefore(slot, h2s[1]);
    else {
      var f = document.querySelector("footer.foot");
      if (f) f.parentNode.insertBefore(slot, f); else main.appendChild(slot);
    }

    var css = document.createElement("style");
    css.textContent =
      ".bryme-ad{margin:30px auto;max-width:300px;text-align:center;overflow:hidden}" +
      ".bryme-ad-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
      "@media(max-width:340px){.bryme-ad iframe{transform:scale(.9);transform-origin:top center}}";
    document.head.appendChild(css);

    var d = frame.contentDocument || (frame.contentWindow && frame.contentWindow.document);
    if (!d) return;
    function fill() {
    d.open();
    /* CSP-clean: the provider's atOptions lives in an EXTERNAL same-origin file
       (assets/ad-300x250-config.js, values unaltered) because the site's
       Content-Security-Policy forbids inline scripts. No inline code here. */
    d.write(
      '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">' +
      '<style>html,body{margin:0;padding:0;overflow:hidden}</style></head><body>' +
      '<script src="/assets/ad-300x250-config.js"><\/script>' +
      '<script src="' + INVOKE_SRC + '"><\/script>' +
      "</body></html>"
    );
    d.close();
    }

    fill();

    /* DEBUG MODE: visit any page with ?addebug=1 to see the live ad-chain report
       (loads, failures, CSP blocks, fill counts) directly on the page. */
    if (/\baddebug\b/.test(window.location.search)) {
      var dbg = document.createElement("div");
      dbg.id = "bryme-ad-debug";
      dbg.style.cssText = "position:fixed;left:8px;bottom:8px;z-index:99999;background:#101a2b;color:#7fff9e;font:11px/1.5 monospace;padding:10px 12px;border-radius:8px;max-width:340px;box-shadow:0 4px 14px rgba(0,0,0,.4)";
      var dlog = function (m) {
        var p = document.createElement("div");
        p.textContent = new Date().toTimeString().slice(0, 8) + "  " + m;
        dbg.appendChild(p);
      };
      document.body.appendChild(dbg);
      dlog("slot created (banner+IPP)");
      window.addEventListener("securitypolicyviolation", function (e) {
        dlog("CSP BLOCKED: " + e.violatedDirective + " " + String(e.blockedURL).slice(0, 70));
      });
      ippScr.addEventListener("load", function () { dlog("IPP invoke.js LOADED"); });
      ippScr.addEventListener("error", function () { dlog("IPP invoke.js FAILED TO LOAD"); });
      frame.addEventListener("load", function () { dlog("banner iframe fired load"); });
      var dbgTimer = setInterval(function () {
        if (!document.getElementById("bryme-ad-slot")) { dlog("slot gone from DOM"); clearInterval(dbgTimer); return; }
        var ib = 0;
        try {
          ib = frame.contentDocument && frame.contentDocument.body ? frame.contentDocument.body.children.length : -1;
        } catch (e) { dlog("banner: CROSS-ORIGIN = creative live"); clearInterval(dbgTimer); return; }
        var ic = document.getElementById("container-ba9b1b5b135e5f465955aadf88ed0ad5");
        dlog("banner children:" + ib + " | IPP children:" + (ic ? ic.children.length : "?"));
        if (ib > 0 || (ic && ic.children.length > 0)) { dlog(">>> FILL DETECTED <<<"); clearInterval(dbgTimer); }
      }, 4000);
      setTimeout(function () { clearInterval(dbgTimer); }, 60000);
    }

    /* Failsafe: slow networks and empty fills get two retries (7s, 15s, 23s)
       before the slot collapses. Once the creative lands, its document turns
       cross-origin and the checks stop touching it. */
    var tries = 0;
    function check() {
      var empty = false;
      try {
        var b = frame.contentDocument && frame.contentDocument.body;
        var ippBox = document.getElementById("container-ba9b1b5b135e5f465955aadf88ed0ad5");
        var ippFilled = ippBox && ippBox.children.length > 0;
        empty = (!b || b.children.length === 0) && !ippFilled;
      } catch (e) { return; }
      if (!empty) return;
      tries++;
      if (tries <= 2) { fill(); setTimeout(check, 8000); }
      else slot.style.display = "none";
    }
    setTimeout(check, 7000);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
