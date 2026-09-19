/* BRYME ad gate v4 (19 Sep night). Owns the TOP 300x250 banner slot styling
   and the mobile nav guard for the Social Bar. The provider snippets (the
   config file + invoke.js, and the bar script) are PLAIN verbatim <script>
   tags in the page HTML at their placement points - visible to the network's
   own code detection, exactly the provider's documented wiring - while this
   file, same-origin and host-free, only decorates: it keeps the banner box
   hidden until the invoke actually paints a sized creative (owner fix: no
   "Advertisement" sign with no ad under it), deletes the box 12s after load
   when the zone serves no fill, and lifts the bottom navigation's stacking
   level on small screens so the social bar can never trap navigation. */
(function () {
  "use strict";
  if (window.__BRYME_AD_GATE__) return;
  window.__BRYME_AD_GATE__ = true;

  function injectCss() {
    var s = document.createElement("style");
    s.textContent =
      ".bryme-ad-static{margin:18px auto 0;max-width:340px;text-align:center;overflow:hidden}" +
      ".bryme-ad-static-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
      "@media(max-width:340px){.bryme-ad-static iframe{transform:scale(.9);transform-origin:top center}}" +
      "@media(max-width:720px){.bottom-nav,.mobile-nav{z-index:2147483000}}";
    document.head.appendChild(s);
  }

  function box() { return document.querySelector(".bryme-ad-static"); }
  function filled(b) {
    var els = b.querySelectorAll("iframe,img");
    for (var i = 0; i < els.length; i++) {
      var r = els[i].getBoundingClientRect();
      if (r && r.width > 8 && r.height > 8) return true;
    }
    return false;
  }

  function boot() {
    injectCss();
    if (!box()) return;
    var waited = 0;
    var t = setInterval(function () {
      var b = box();
      if (!b) { clearInterval(t); return; }
      if (filled(b)) {
        b.style.visibility = "visible";
        clearInterval(t);
        return;
      }
      waited += 500;
      if (waited >= 12000) {
        clearInterval(t);
        if (b.parentNode) b.parentNode.removeChild(b);
      }
    }, 500);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
