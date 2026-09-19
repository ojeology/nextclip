/* BRYME static display unit v3 (19 Sep night). Owner: "I see the advertisements
   sign but no ads" - the zone serves no fill to some visitors, and v2 left a
   naked "Advertisement" label up to ~40s while self-clean waited. v3 renders
   the slot HIDDEN until a real ad materialises, shows it the moment it does,
   and removes everything silently if nothing fills inside 12s: when the zone
   has no fill, the page shows nothing at all. Owner-confirmed Adsterra 300x250
   display banner (key 51fc16f82ddc690721deee07bcd8bccd), in-flow box above the
   native banner - not sticky, never overlays, own container (per bryme-ad-
   scripts.md §1). Wiring: same-origin synchronous loader; document.write at
   parse position is the provider snippet byte-equivalent (CSP bans inline
   scripts; quality gate bans ad-host strings in HTML). If this file ever runs
   outside the parser it does nothing (document.write post-load would replace
   the page). */
(function () {
  "use strict";
  if (window.__BRYME_AD_STATIC__) return;
  window.__BRYME_AD_STATIC__ = true;
  if (document.readyState !== "loading") return;

  var KEY = "51fc16f82ddc690721deee07bcd8bccd";
  window.atOptions = {
    "key": KEY,
    "format": "iframe",
    "height": 250,
    "width": 300,
    "params": {}
  };

  document.write(
    '<div class="bryme-ad-static" style="visibility:hidden">' +
      '<div class="bryme-ad-static-label">Advertisement</div>' +
      '<div class="bryme-ad-static-box"><script src="https://www.highrevenueformat.com/' + KEY + '/invoke.js"><\/script></div>' +
    '</div>'
  );

  var css = document.createElement("style");
  css.textContent =
    ".bryme-ad-static{margin:26px auto;max-width:340px;text-align:center;overflow:hidden}" +
    ".bryme-ad-static-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
    "@media(max-width:340px){.bryme-ad-static iframe{transform:scale(.9);transform-origin:top center}}";
  document.head.appendChild(css);

  /* Fill-gate: show ONLY when a real creative exists; vanish silently if not. */
  function box() { return document.querySelector(".bryme-ad-static-box"); }
  function filled() {
    var b = box();
    if (!b) return false;
    var els = b.querySelectorAll("iframe,img");
    for (var i = 0; i < els.length; i++) {
      var r = els[i].getBoundingClientRect();
      if (r && r.width > 8 && r.height > 8) return true;
    }
    return false;
  }
  var waited = 0;
  var t = setInterval(function () {
    var slot = document.querySelector(".bryme-ad-static");
    if (!slot) { clearInterval(t); return; }
    if (filled()) {
      slot.style.visibility = "visible";
      clearInterval(t);
      return;
    }
    waited += 500;
    if (waited >= 12000) {
      clearInterval(t);
      slot.parentNode.removeChild(slot);
    }
  }, 500);
})();
