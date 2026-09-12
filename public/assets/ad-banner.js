/* BRYME advertising component v6 (ad-banner.js twin - legacy path kept alive for cached HTML; asset law). */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return;
  window.__BRYME_AD__ = true;

  var IPP_INVOKE = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
  var IPP_CONTAINER = "container-ba9b1b5b135e5f465955aadf88ed0ad5";

  function makeSlot(labelText) {
    var slot = document.createElement("div");
    slot.className = "bryme-ad";
    var label = document.createElement("div");
    label.className = "bryme-ad-label";
    label.textContent = labelText;
    slot.appendChild(label);
    return slot;
  }

  function init() {
    var main = document.querySelector("main") || document.body;

    /* placement 1: the 300x250 banner */
    var s1 = makeSlot("Advertisement");
    var frame = document.createElement("iframe");
    frame.id = "bryme-ad-300x250";
    frame.width = "300";
    frame.height = "250";
    frame.setAttribute("scrolling", "no");
    frame.setAttribute("frameborder", "0");
    frame.setAttribute("title", "Advertisement");
    s1.appendChild(frame);

    var h2s = main.querySelectorAll("h2"), placed1 = false;
    if (h2s.length >= 3) { h2s[2].parentNode.insertBefore(s1, h2s[2]); placed1 = true; }
    else if (h2s.length === 2) { h2s[1].parentNode.insertBefore(s1, h2s[1]); placed1 = true; }
    if (!placed1) {
      var f0 = document.querySelector("footer.foot");
      if (f0) f0.parentNode.insertBefore(s1, f0); else main.appendChild(s1);
    }

    /* placement 2: Native container at the TOP — directly below header/navigation,
       above the page title (owner file #2, 12 Sep 2026). Single instance per page:
       the container ID must never be duplicated, so the former end-of-content slot
       is retired in favour of this instructed position. */
    var s2 = makeSlot("Advertisement");
    var ippScr = document.createElement("script");
    ippScr.async = true;
    ippScr.setAttribute("data-cfasync", "false");
    ippScr.src = IPP_INVOKE;
    s2.appendChild(ippScr);
    var ipp = document.createElement("div");
    ipp.id = IPP_CONTAINER;
    ipp.className = "bryme-ad-ipp";
    s2.appendChild(ipp);
    main.parentNode.insertBefore(s2, main);

    /* placement 3: fixed desktop rail (wide screens only, never over content) */
    var s3 = makeSlot("Advertisement");
    s3.className = "bryme-ad bryme-ad-side";
    var rail = document.createElement("iframe");
    rail.id = "bryme-ad-side-300x250";
    rail.width = "300";
    rail.height = "250";
    rail.setAttribute("scrolling", "no");
    rail.setAttribute("frameborder", "0");
    rail.setAttribute("title", "Advertisement");
    rail.setAttribute("loading", "lazy");
    s3.appendChild(rail);
    document.body.appendChild(s3);

    var css = document.createElement("style");
    css.textContent =
      ".bryme-ad{margin:30px auto;max-width:300px;text-align:center;overflow:hidden}" +
      ".bryme-ad-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
      ".bryme-ad-ipp{margin-top:8px;min-height:0}" +
      ".bryme-ad-side{display:none}" +
      "@media(min-width:1420px){.bryme-ad-side{display:block;position:fixed;right:10px;top:50%;transform:translateY(-50%);margin:0;z-index:50}}" +
      "@media(max-width:340px){.bryme-ad iframe{transform:scale(.9);transform-origin:top center}}";
    document.head.appendChild(css);

    /* banner fill: atOptions (external config) + invoke, inside the iframe */
    var d = frame.contentDocument || (frame.contentWindow && frame.contentWindow.document);
    if (d) {
      function fill() {
        d.open();
        d.write(
          '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">' +
          '<style>html,body{margin:0;padding:0;overflow:hidden}</style></head><body>' +
          '<script src="/assets/ad-300x250-config.js?v=3"><\/script>' +
          '<script src="https://www.highrevenueformat.com/51fc16f82ddc690721deee07bcd8bccd/invoke.js"><\/script>' +
          "</body></html>"
        );
        d.close();
      }
      fill();

      var tries = 0;
      function check() {
        var empty = false;
        try {
          var b = frame.contentDocument && frame.contentDocument.body;
          empty = !b || Array.prototype.filter.call(b.children || [], function (c) { return c.tagName !== "SCRIPT"; }).length === 0;
        } catch (e) { return; }
        if (!empty) return;
        tries++;
        if (tries <= 2) { fill(); setTimeout(check, 8000); }
        else s1.style.display = "none";
      }
      setTimeout(check, 7000);
    }

    /* Social Bar (owner file #2): self-injecting floating unit, no container.
       Loaded once globally; position/behaviour per the network's dashboard.
       Owner must run the click-safety test (file #2 checklist); if it fires
       popups/redirects on page clicks and the dashboard cannot restrict it,
       it gets disabled in a follow-up batch. */
    var sb = document.createElement("script");
    sb.src = "https://pl31304019.profitableratecpmnetwork.com/7c/e5/f0/7ce5f0421abe8df585e6bba232f4e614.js";
    document.body.appendChild(sb);

    /* rail fill (same zone, own document) + self-clean if empty */
    var rd = rail.contentDocument || (rail.contentWindow && rail.contentWindow.document);
    if (rd) {
      rfill();
      function rfill() {
        rd.open();
        rd.write(
          '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">' +
          '<style>html,body{margin:0;padding:0;overflow:hidden}</style></head><body>' +
          '<script src="/assets/ad-300x250-config.js?v=3"><\/script>' +
          '<script src="https://www.highrevenueformat.com/51fc16f82ddc690721deee07bcd8bccd/invoke.js"><\/script>' +
          "</body></html>"
        );
        rd.close();
      }
      setTimeout(function () {
        try {
          var b = rd.body;
          var real = b ? Array.prototype.filter.call(b.children || [], function (c) { return c.tagName !== "SCRIPT"; }).length : 0;
          if (!real) { s3.remove(); return; }
        } catch (e) { /* cross-origin = creative live */ }
      }, 9000);
    }

    /* Native self-clean: if the top container never fills, retire that slot */
    setTimeout(function () {
      var ic = document.getElementById(IPP_CONTAINER);
      if (ic && ic.children.length === 0) s2.style.display = "none";
    }, 25000);

  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
