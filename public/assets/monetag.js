/* BRYME Monetag integration v1 (owner file: "Final Setup - Remove HilltopAds,
   Deploy Monetag Site-Wide", overrides conflicting instructions).
   Two Monetag zones, site-wide, each loads ONCE per page (static MPA + this
   guard; no SPA re-render double-fire):
     Zone 11610753 - Vignette Banner (n6wxm.com/vignette.min.js)
     Zone 11610749 - second tag (nap5k.com/tag.min.js)
   Snippets are the owner's, adapted ONLY in placement: inline code is blocked
   by the site CSP (script-src 'self' https:), so the identical statements run
   from this external engine file - same execution, same append target.
   OWNER DASHBOARD REQUIREMENTS (from the same file, before judging results):
     - zone 11610749 must be a NON-intrusive format (In-Page Push or Banner),
       not Popunder/Interstitial/Push;
     - frequency capping on BOTH zones (occasional, not every page load;
       smart/adaptive capping as the default starting point). */
(function () {
  "use strict";
  if (window.__BRYME_MONETAG__) return;
  window.__BRYME_MONETAG__ = true;

  /* Zone 11610753 - Vignette Banner (verbatim owner logic). */
  (function (s) {
    s.dataset.zone = "11610753";
    s.src = "https://n6wxm.com/vignette.min.js";
  })([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement("script")));

  /* Zone 11610749 - second Monetag tag (verbatim owner logic). */
  (function (s) {
    s.dataset.zone = "11610749";
    s.src = "https://nap5k.com/tag.min.js";
  })([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement("script")));
})();
