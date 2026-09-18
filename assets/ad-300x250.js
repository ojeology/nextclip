/* BRYME static display unit v2 (19 Sep: re-enabled alone - the two-unit
   deploy broke real-visitor clicks, Social Bar stays OFF as prime suspect.
   This unit is an in-flow box: structurally cannot cover buttons.)
   Owner-confirmed Adsterra 300x250 banner (key 51fc16f82ddc690721deee07bcd8bccd).
   Placement: bottom of page content, just above the footer - directly above the
   Native Banner mounted by ad-slot.js. Rules from the owner's brief: standard
   inline box - NOT sticky, NOT overlaying content, its own container, never
   merged with other units.
   Wiring note: the provider snippet is (atOptions + synchronous invoke.js that
   renders via document.write). The site CSP forbids inline scripts and the
   quality gate forbids ad-host strings in HTML, so this same-origin loader IS
   the snippet, served as a file: it sets window.atOptions and document.writes
   the labelled container + provider script at its own parse position. That is
   byte-equivalent to the provider's tag and keeps both rules satisfied. If this
   file ever executes outside the parser (readyState !== "loading") it does
   nothing - document.write after load would replace the page. */
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
    '<div class="bryme-ad-static">' +
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

  /* Self-clean (same policy as the v17 native slot): if the zone serves
     nothing visibly filled, the labelled box is removed. The iframe is the
     fill signal for display units, so require a real, sized iframe. */
  function filled() {
    var f = document.querySelectorAll(".bryme-ad-static-box iframe");
    for (var i = 0; i < f.length; i++) {
      var r = f[i].getBoundingClientRect();
      if (r && r.width > 8 && r.height > 8) return true;
    }
    return false;
  }
  setTimeout(function () {
    if (!filled()) setTimeout(function () {
      if (!filled()) {
        var slots = document.querySelectorAll(".bryme-ad-static");
        for (var i = 0; i < slots.length; i++) slots[i].parentNode.removeChild(slots[i]);
      }
    }, 15000);
  }, 25000);
})();
