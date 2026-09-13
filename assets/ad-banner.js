/* BRYME advertising component v12 (ad-banner.js twin).
   v12 (13 Sep 2026): reconciled with the owner's master instructions.
   - The 300x250 banner (51fc... / highrevenueformat) returns to the BOTTOM of
     the page (master Unit 1: "already implemented and confirmed working
     (bottom of page)" ... "do not duplicate this exact unit elsewhere"), stacked
     above the native container. Exactly one instance per page.
   - New fill-safety: the banner unit counts real ad <iframe> elements (not
     wrapper nodes) - if the zone serves no iframe after two retries the unit
     removes itself, so a dead zone can no longer leave an empty placeholder
     box (owner order, 13 Sep: placeholders removed).
   - The native container (ba9b...) stays at the BOTTOM per the owner's verbal
     correction of 12 Sep ("annoying at the top, supposed to be at the bottom");
     the master file's TOP line for it is consciously overridden by that verbal
     ruling and reported as a tradeoff (master's own priority rule).
   - TOP slot stays config-gated: activates only when assets/ad-top-config.js
     defines window.BRYME_TOP (owner's single-widget native, still awaited).
   - Social Bar unchanged: once per page, self-injecting (renders nothing and
     leaves no artifact while its zone is dormant). */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return;
  window.__BRYME_AD__ = true;

  var BOTTOM_INVOKE = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
  var BOTTOM_CONTAINER = "container-ba9b1b5b135e5f465955aadf88ed0ad5";
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
  function realKids(el) {
    return Array.prototype.filter.call((el && el.children) || [], function (c) { return c.tagName !== "SCRIPT"; }).length;
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
    var foot = document.querySelector("footer.foot");
    var main = document.querySelector("main") || document.body;

    /* 1. TOP: reserved for the owner's single-widget native (config-driven). */
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

    /* 2. SOCIAL BAR: once per page (self-injecting; owner keeps least-intrusive
       dashboard settings; owner click-test governs whether it stays). If the
       zone is off or unfilled it renders nothing and leaves no box. */
    var sb = document.createElement("script");
    sb.src = SOCIAL_SRC;
    document.body.appendChild(sb);

    /* 3. BOTTOM-1: the 300x250 banner - back where it was confirmed working
       (master Unit 1: bottom of page, once per page). Self-cleaning: kept only
       while a real ad <iframe> exists in the inner document. */
    var botb = makeSlot("Advertisement");
    var frame = document.createElement("iframe");
    frame.id = "bryme-ad-300x250";
    frame.width = "300";
    frame.height = "250";
    frame.setAttribute("scrolling", "no");
    frame.setAttribute("frameborder", "0");
    frame.setAttribute("title", "Advertisement");
    frame.setAttribute("loading", "lazy");
    botb.appendChild(frame);
    if (foot) foot.parentNode.insertBefore(botb, foot); else main.appendChild(botb);
    var bd = bannerDoc(frame);
    if (bd) {
      var tries = 0;
      function bcheck() {
        var none = true;
        try { none = !bd.querySelector("iframe"); } catch (e) { return; }
        if (!none) return;
        tries++;
        if (tries <= 2) { bannerDoc(frame); setTimeout(bcheck, 8000); }
        else botb.remove();
      }
      setTimeout(bcheck, 7000);
    } else { botb.remove(); }

    /* 4. BOTTOM-2: the owner's container native unit - below the banner,
       still below the page (owner, 12 Sep: it belongs at the bottom). */
    var bot = makeSlot("Advertisement");
    var bscr = document.createElement("script");
    bscr.async = true;
    bscr.setAttribute("data-cfasync", "false");
    bscr.src = BOTTOM_INVOKE;
    bot.appendChild(bscr);
    var bbox = document.createElement("div");
    bbox.id = BOTTOM_CONTAINER;
    bot.appendChild(bbox);
    if (foot) foot.parentNode.insertBefore(bot, foot); else main.appendChild(bot);
    setTimeout(function () { if (!realKids(bbox)) bot.remove(); }, 25000);

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
