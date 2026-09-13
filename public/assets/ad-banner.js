/* BRYME advertising component v17 (ad-banner.js twin).
   v17 (15 Sep, owner: "forget the social bar... delete the not working ones;
   Adsterra is just a test before AdSense and buying the domain"):
   the engine carries ONLY the owner-confirmed WORKING unit - the Native
   Banner at the BOTTOM (after content, before footer), one instance per page,
   self-cleaning when its zone serves nothing visible.
   Everything else (Social Bar, dead 300x250, Smart Link) is gone - full
   history in git. Next (owner-approved): owner creates MORE Native Banner
   zones (one code for TOP, one for MIDDLE of content) and pastes them here;
   each gets wired the same day with its own container ID. */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return;
  window.__BRYME_AD__ = true;

  /* Verbatim zone identifiers from the owner's instructions. */
  var NATIVE_INVOKE = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
  var NATIVE_CONTAINER = "container-ba9b1b5b135e5f465955aadf88ed0ad5";

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

  function init() {
    var main = document.querySelector("main") || document.body;
    var foot = document.querySelector("footer.foot");

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
