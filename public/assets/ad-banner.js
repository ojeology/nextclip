/* BRYME advertising component v15 (ad-banner.js twin).
   v15 (owner OVERRIDE "placement swap" — supersedes ALL earlier placements):
     FINAL LAYOUT: header/nav → [300x250 at TOP + Social Bar renders top-area]
       → page title → content → [Native Banner at BOTTOM].
     ZONE TOP: the 300x250 banner (51fc / highrevenueformat), directly below
       the header/navigation, above the title. Snippet untouched. HIDDEN until
       a real ad iframe fills it; removes itself if the zone never fills —
       an unfilled zone shows nothing (no empty "Advertisement" boxes, owner rule).
     ZONE BOTTOM: the Native Banner (ba9b invoke + container), after the main
       content, where the 300x250 used to sit; exactly one container per page;
       self-cleans if the zone serves nothing visible.
     ZONE SOCIAL: self-injecting script once per page; its render position is
       network-controlled (expected top area).
     SMART LINK: PAUSED by the owner — never implement, link, or redirect to
       it without a new written instruction.
   Owner's binding definition of "working": VISIBLY RENDERING on the live page
   in a real browser (incognito, no blocker). Code presence alone is not
   "working" and must never be reported as such. */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return;
  window.__BRYME_AD__ = true;

  /* Verbatim zone identifiers from the owner's instructions. */
  var BANNER_INVOKE = "https://www.highrevenueformat.com/51fc16f82ddc690721deee07bcd8bccd/invoke.js";
  var NATIVE_INVOKE = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
  var NATIVE_CONTAINER = "container-ba9b1b5b135e5f465955aadf88ed0ad5";
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
    var foot = document.querySelector("footer.foot");

    /* ZONE TOP: 300x250 banner - directly below the header, above the title.
       Hidden until a real ad iframe exists; 2 retries, then removes itself. */
    var top = makeSlot("Advertisement");
    var frame = document.createElement("iframe");
    frame.id = "bryme-ad-300x250";
    frame.width = "300";
    frame.height = "250";
    frame.setAttribute("scrolling", "no");
    frame.setAttribute("frameborder", "0");
    frame.setAttribute("title", "Advertisement");
    top.appendChild(frame);
    top.style.display = "none"; /* invisible until a real ad fills it */
    main.parentNode.insertBefore(top, main);
    var bd = bannerDoc(frame);
    if (bd) {
      var tries = 0;
      function bcheck() {
        var doc = null;
        try { doc = frame.contentDocument; } catch (e) { return; }
        if (!doc || !doc.body) return;
        if (doc.querySelector("iframe")) { top.style.display = ""; return; } /* filled: reveal */
        tries++;
        if (tries <= 2) { bannerDoc(frame); setTimeout(bcheck, 8000); }
        else top.remove();
      }
      setTimeout(bcheck, 7000);
    } else { top.remove(); }

    /* ZONE BOTTOM: Native Banner - after the content, before the footer.
       Exactly one container per page; self-cleans when not visibly filled. */
    var bot = makeSlot("Advertisement");
    var nscr = document.createElement("script");
    nscr.async = true;
    nscr.setAttribute("data-cfasync", "false");
    nscr.src = NATIVE_INVOKE;
    bot.appendChild(nscr);
    var nbox = document.createElement("div");
    nbox.id = NATIVE_CONTAINER;
    nbox.className = "bryme-ad-ipp";
    bot.appendChild(nbox);
    if (foot) foot.parentNode.insertBefore(bot, foot); else main.appendChild(bot);
    setTimeout(function () {
      if (!nativeFilled(nbox)) setTimeout(function () {
        if (!nativeFilled(nbox)) bot.remove();
      }, 15000);
    }, 25000);

    /* ZONE SOCIAL: once per page, self-injecting; render position is
       controlled by the network (expected in the top area). */
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
