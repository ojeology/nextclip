/* BRYME advertising component v13 (ad-slot.js twin).
   v13 (13 Sep 2026, owner order "delete them all, follow the file - three ad
   zones"): complete rebuild from the owner's master instructions.
   *** OWNER-FROZEN 14 Sep 2026: the TOP native is confirmed rendering and approved
   in place ("freeze it, it is so good there") - its placement must never change.
   v14: the mid 300x250 is HIDDEN until a real ad fills it (owner saw an empty
   "Advertisement" box on an unfilled zone). ***
   ZONE 1 - Native Banner (ba9b container): TOP of page, directly below the
     header/navigation, above the title/content; script once, container div
     exactly once per page; self-cleans if the zone serves nothing visible.
   ZONE 2 - 300x250 banner (51fc / highrevenueformat): IN-BETWEEN content
     (before the 3rd section heading; falls back to the end of the article
     body - never below the footer); CSP-safe iframe loader with literal
     script closers (the v12 fix) and a real-ad-iframe fill check that
     removes the unit if the zone serves nothing.
   ZONE 3 - Social Bar: self-injecting script once per page; renders nothing
     and leaves no artifact while its zone is dormant.
   Nothing renders at the bottom of the page. No config gates. */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return;
  window.__BRYME_AD__ = true;

  /* Verbatim zone identifiers from the owner's master instructions. */
  var NATIVE_INVOKE = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
  var NATIVE_CONTAINER = "container-ba9b1b5b135e5f465955aadf88ed0ad5";
  var BANNER_INVOKE = "https://www.highrevenueformat.com/51fc16f82ddc690721deee07bcd8bccd/invoke.js";
  var SOCIAL_SRC = "https://pl31304019.profitableratecpmnetwork.com/7c/e5/f0/7ce5f0421abe8df585e6bba232f4e614.js";

  function makeSlot(labelText) {
    var slot = document.createElement("div");
    slot.className = "bryme-ad";
    var label = document.createElement("div");
    label.className = "bryme-ad-label";
    label.textContent = labelText;
    slot.appendChild(label);
    return slot;
  }

  function nativeFilled(box) {
    var els = box.querySelectorAll("*");
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.tagName === "SCRIPT") continue;
      if (el.tagName === "IFRAME" || el.tagName === "IMG") return true;
      var r = el.getBoundingClientRect ? el.getBoundingClientRect() : null;
      if (r && r.width > 8 && r.height > 8) return true;
    }
    return false;
  }

  function bannerDoc(frame) {
    var d = frame.contentDocument || (frame.contentWindow && frame.contentWindow.document);
    if (!d) return null;
    d.open();
    d.write(
      '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">' +
      '<style>html,body{margin:0;padding:0;overflow:hidden}</style></head><body>' +
      '<script src="/assets/ad-300x250-config.js?v=3"></script>' +
      '<script src="' + BANNER_INVOKE + '"></script>' +
      "</body></html>"
    );
    d.close();
    return d;
  }

  function init() {
    var main = document.querySelector("main") || document.body;

    /* ZONE 1: Native Banner - top of page, below nav, above title/content. */
    var top = makeSlot("Advertisement");
    var nscr = document.createElement("script");
    nscr.async = true;
    nscr.setAttribute("data-cfasync", "false");
    nscr.src = NATIVE_INVOKE;
    top.appendChild(nscr);
    var nbox = document.createElement("div");
    nbox.id = NATIVE_CONTAINER;
    nbox.className = "bryme-ad-ipp";
    top.appendChild(nbox);
    main.parentNode.insertBefore(top, main);
    setTimeout(function () {
      if (!nativeFilled(nbox)) setTimeout(function () {
        if (!nativeFilled(nbox)) top.remove();
      }, 15000);
    }, 25000);

    /* ZONE 2: 300x250 banner - in-between content, before the 3rd heading. */
    var mid = makeSlot("Advertisement");
    var frame = document.createElement("iframe");
    frame.id = "bryme-ad-300x250";
    frame.width = "300";
    frame.height = "250";
    frame.setAttribute("scrolling", "no");
    frame.setAttribute("frameborder", "0");
    frame.setAttribute("title", "Advertisement");
    frame.setAttribute("loading", "lazy");
    mid.appendChild(frame);
    mid.style.display = "none"; /* v14: invisible until a real ad fills it */
    var h2s = main.querySelectorAll("h2"), placed = false;
    if (h2s.length >= 3) { h2s[2].parentNode.insertBefore(mid, h2s[2]); placed = true; }
    else if (h2s.length === 2) { h2s[1].parentNode.insertBefore(mid, h2s[1]); placed = true; }
    if (!placed) main.appendChild(mid);
    var bd = bannerDoc(frame);
    if (bd) {
      var tries = 0;
      function bcheck() {
        var doc = null;
        try { doc = frame.contentDocument; } catch (e) { return; }
        if (!doc || !doc.body) return;
        if (doc.querySelector("iframe")) { mid.style.display = ""; return; } /* filled: reveal */
        tries++;
        if (tries <= 2) { bannerDoc(frame); setTimeout(bcheck, 8000); }
        else mid.remove();
      }
      setTimeout(bcheck, 7000);
    } else { mid.remove(); }

    /* ZONE 3: Social Bar - once per page, self-injecting. */
    var sb = document.createElement("script");
    sb.src = SOCIAL_SRC;
    document.body.appendChild(sb);

    var css = document.createElement("style");
    css.textContent =
      ".bryme-ad{margin:30px auto;max-width:340px;text-align:center;overflow:hidden}" +
      ".bryme-ad-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
      ".bryme-ad-ipp{min-height:0}" +
      "@media(max-width:340px){.bryme-ad iframe{transform:scale(.9);transform-origin:top center}}";
    document.head.appendChild(css);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
