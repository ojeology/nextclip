/* BRYME advertising component v11 (ad-banner.js twin).
   v11 (13 Sep 2026, owner order): the mid 300x250 and the desktop rail units
   are REMOVED - their zones served no fill, leaving permanent empty
   "Advertisement" placeholder boxes (owner: "ads are not loading inside them,
   remove them"). What remains: the config-gated TOP slot (waits for the
   owner's single-widget native), the self-injecting Social Bar (invisible
   until its zone serves; no placeholder possible), and the owner's container
   unit at the BOTTOM (confirmed working). The retired zones can be restored
   from git history if their dashboard zones are ever re-activated. */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return;
  window.__BRYME_AD__ = true;

  /* The owner's multi-widget container unit (ba9b...) renders at the BOTTOM
     (owner, 12 Sep 2026: it is annoying at the top; it belongs below the page).
     The TOP slot is reserved for the owner's single-widget native unit - it
     activates the moment assets/ad-top-config.js defines window.BRYME_TOP. */
  var BOTTOM_INVOKE = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
  var BOTTOM_CONTAINER = "container-ba9b1b5b135e5f465955aadf88ed0ad5";
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
  function realKids(el) {
    return Array.prototype.filter.call((el && el.children) || [], function (c) { return c.tagName !== "SCRIPT"; }).length;
  }

  function init() {
    /* 1. TOP: reserved for the owner's single-widget native (config-driven). */
    var main = document.querySelector("main") || document.body;
    var T = window.BRYME_TOP;
    if (T && T.invoke && T.container) {
      var top = makeSlot("Advertisement");
      var nscr = document.createElement("script");
      nscr.async = true;
      nscr.setAttribute("data-cfasync", "false");
      nscr.src = T.invoke;
      top.appendChild(nscr);
      var native = document.createElement("div");
      native.id = T.container;
      native.className = "bryme-ad-ipp";
      top.appendChild(native);
      main.parentNode.insertBefore(top, main);
      setTimeout(function () { if (!realKids(native)) top.remove(); }, 25000);
    }

    /* 2. (v11: mid 300x250 removed - dead zone, placeholder boxes) */

    /* 3. (v11: desktop rail removed - dead zone, placeholder boxes) */

    /* 4. SOCIAL BAR: once per page (self-injecting; owner keeps least-intrusive
       dashboard settings; owner click-test governs whether it stays). If the
       zone is off or unfilled it renders nothing and leaves no box. */
    var sb = document.createElement("script");
    sb.src = SOCIAL_SRC;
    document.body.appendChild(sb);

    /* 5. BOTTOM: the owner's container unit - below the page, where it belongs
       (confirmed working by the owner, 13 Sep 2026). */
    var bot = makeSlot("Advertisement");
    var bscr = document.createElement("script");
    bscr.async = true;
    bscr.setAttribute("data-cfasync", "false");
    bscr.src = BOTTOM_INVOKE;
    bot.appendChild(bscr);
    var bbox = document.createElement("div");
    bbox.id = BOTTOM_CONTAINER;
    bot.appendChild(bbox);
    var f1 = document.querySelector("footer.foot");
    if (f1) f1.parentNode.insertBefore(bot, f1); else main.appendChild(bot);
    setTimeout(function () { if (!realKids(bbox)) bot.remove(); }, 25000);

    var css = document.createElement("style");
    css.textContent =
      ".bryme-ad{margin:30px auto;max-width:340px;text-align:center;overflow:hidden}" +
      ".bryme-ad-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
      ".bryme-ad-ipp{min-height:0}";
    document.head.appendChild(css);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
