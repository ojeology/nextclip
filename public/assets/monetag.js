/* BRYME Monetag integration v1 (owner file: "Final Setup - Remove HilltopAds,
   Deploy Monetag Site-Wide", overrides conflicting instructions).
   Two Monetag zones, site-wide, each loads ONCE per page (static MPA + this
   guard; no SPA re-render double-fire):
     Zone 11610753 - Vignette Banner (n6wxm.com/vignette.min.js)
     Zone 11610749 - second tag (nap5k.com/tag.min.js)
   Snippets are the owner's, adapted ONLY in placement: inline code is blocked
   by the site CSP (script-src 'self' https:), so the identical statements run
   from this external engine file - same execution, same append target.
   v2 (15 Sep): the owner confirms Monetag's dashboard offers NO frequency
   capping option - so the cap lives HERE, in our loader. The vignette script
   is loaded at most 1x per 12 hours per visitor; the second tag at most 4x
   per 24 hours (the exact bands the owner's instruction file proposed). When
   a cap is reached the script is not injected at all, so no impression can
   fire. Values are constants below - easy to tune.
   OWNER DASHBOARD NOTES (from the same file):
     - zone 11610749 must be a NON-intrusive format (In-Page Push or Banner),
       not Popunder/Interstitial/Push;
     - frequency capping on BOTH zones (occasional, not every page load;
       smart/adaptive capping as the default starting point). */
(function () {
  "use strict";
  if (window.__BRYME_MONETAG__) return;
  window.__BRYME_MONETAG__ = true;

  /* Code-side frequency capping: allow(key, max, hours) returns true at most
     MAX times per HOURS per browser, persisting the counter in localStorage. */
  function allow(key, max, hours) {
    var now = Date.now(), d = null;
    try { d = JSON.parse(localStorage.getItem(key) || "null"); } catch (e) { d = null; }
    if (!d || now >= d.reset) d = { count: 0, reset: now + hours * 3600000 };
    if (d.count >= max) { try { localStorage.setItem(key, JSON.stringify(d)); } catch (e) {} return false; }
    d.count += 1;
    try { localStorage.setItem(key, JSON.stringify(d)); } catch (e) {}
    return true;
  }
  var VIGNETTE_MAX = 1, VIGNETTE_HOURS = 12;   /* owner file: 1-2 per session */
  var SECOND_MAX = 4, SECOND_HOURS = 24;       /* owner file: limited per day */

  /* Zone 11610753 - Vignette Banner (owner logic, frequency-capped). */
  if (allow("bryme-mt-vig", VIGNETTE_MAX, VIGNETTE_HOURS))
  (function (s) {
    s.dataset.zone = "11610753";
    s.src = "https://n6wxm.com/vignette.min.js";
  })([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement("script")));

  /* Zone 11610749 - second Monetag tag (owner logic, frequency-capped). */
  if (allow("bryme-mt-z2", SECOND_MAX, SECOND_HOURS))
  (function (s) {
    s.dataset.zone = "11610749";
    s.src = "https://nap5k.com/tag.min.js";
  })([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement("script")));
})();
