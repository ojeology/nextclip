/* Push the AdSense units present on the page.
 *
 * External file on purpose: the site CSP is
 *   script-src 'self' https:
 * with no 'unsafe-inline', so an inline
 *   <script>(adsbygoogle = window.adsbygoogle || []).push({})</script>
 * is blocked by the browser and never runs. That is one of the two reasons the
 * original _ads_slot() helper in build-ecosystem.py could never have worked.
 *
 * Safe to load when no units exist: the query returns nothing and the file
 * exits. load() before the AdSense library is fine -- window.adsbygoogle is
 * initialised here and the library pushes from the same queue when it arrives.
 */
(function () {
  "use strict";

  function pushUnits() {
    var units = document.querySelectorAll("ins.adsbygoogle");
    if (!units.length) return;
    var queue = (window.adsbygoogle = window.adsbygoogle || []);
    for (var i = 0; i < units.length; i++) {
      // Skip anything AdSense has already processed, so a second call (or a
      // component that re-renders) cannot double-push and error in console.
      if (units[i].getAttribute("data-adsbygoogle-status")) continue;
      queue.push({});
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", pushUnits);
  } else {
    pushUnits();
  }
})();
