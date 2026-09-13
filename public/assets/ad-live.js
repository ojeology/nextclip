/* BRYME /ad-test/ copy - third twin under a NEVER-SERVED-BEFORE filename. */
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
      '<script src="/assets/ad-300x250-config.js?v=3"><\/script>' +
      '<script src="' + BANNER_INVOKE + '"><\/script>' +
      "</body></html>"
    );
    d.close();
    return d;
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

    /* 2. MID: 300x250 in-content */
    var mid = makeSlot("Advertisement");
    var frame = document.createElement("iframe");
    frame.id = "bryme-ad-300x250";
    frame.width = "300";
    frame.height = "250";
    frame.setAttribute("scrolling", "no");
    frame.setAttribute("frameborder", "0");
    frame.setAttribute("title", "Advertisement");
    mid.appendChild(frame);
    var h2s = main.querySelectorAll("h2"), placed = false;
    if (h2s.length >= 3) { h2s[2].parentNode.insertBefore(mid, h2s[2]); placed = true; }
    else if (h2s.length === 2) { h2s[1].parentNode.insertBefore(mid, h2s[1]); placed = true; }
    if (!placed) {
      var f0 = document.querySelector("footer.foot");
      if (f0) f0.parentNode.insertBefore(mid, f0); else main.appendChild(mid);
    }
    var md = bannerDoc(frame);
    if (md) {
      var tries = 0;
      function mfill() { bannerDoc(frame); }
      function mcheck() {
        var empty = false;
        try { empty = realKids(md.body) === 0; } catch (e) { return; }
        if (!empty) return;
        tries++;
        if (tries <= 2) { mfill(); setTimeout(mcheck, 8000); }
        else mid.remove();
      }
      setTimeout(mcheck, 7000);
    } else { mid.remove(); }

    /* 3. RAIL: fixed desktop unit (wide viewports only; margin position) */
    var rail = makeSlot("Advertisement");
    rail.className = "bryme-ad bryme-ad-side";
    var rframe = document.createElement("iframe");
    rframe.id = "bryme-ad-side-300x250";
    rframe.width = "300";
    rframe.height = "250";
    rframe.setAttribute("scrolling", "no");
    rframe.setAttribute("frameborder", "0");
    rframe.setAttribute("title", "Advertisement");
    rframe.setAttribute("loading", "lazy");
    rail.appendChild(rframe);
    document.body.appendChild(rail);
    var rd = bannerDoc(rframe);
    if (rd) {
      setTimeout(function () {
        try { if (!realKids(rd.body)) rail.remove(); } catch (e) { /* cross-origin = live */ }
      }, 9000);
    } else { rail.remove(); }

    /* 4. SOCIAL BAR: once per page (self-injecting; owner keeps least-intrusive
       dashboard settings; owner click-test governs whether it stays) */
    var sb = document.createElement("script");
    sb.src = SOCIAL_SRC;
    document.body.appendChild(sb);

    /* 5. BOTTOM: the owner's container unit - below the page, where it belongs. */
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
      ".bryme-ad-ipp{min-height:0}" +
      ".bryme-ad-side{display:none}" +
      "@media(min-width:1420px){.bryme-ad-side{display:block;position:fixed;right:10px;top:50%;transform:translateY(-50%);margin:0;z-index:50}}" +
      "@media(max-width:340px){.bryme-ad iframe{transform:scale(.9);transform-origin:top center}}";
    document.head.appendChild(css);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
