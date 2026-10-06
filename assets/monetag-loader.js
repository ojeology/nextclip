/* Monetag site loader, kept external for the site's strict CSP.
 *
 * This release only adds Monetag's static verification meta tag; this loader is
 * deliberately not injected into page HTML. Loading ads remains a separate
 * owner-approved deployment decision. If the loader is explicitly included,
 * it uses the two owner-supplied zones and conservative client-side frequency
 * caps so it cannot fire on every page view.
 *
 * Zone 11610753: vignette.min.js (4 loads / 4 hours)
 * Zone 11610749: tag.min.js (12 loads / 12 hours; owner-confirmed In-Page Push)
 */
(function () {
  "use strict";

  if (window.__BRYME_MONETAG__) return;
  window.__BRYME_MONETAG__ = true;

  function allow(key, max, hours) {
    var now = Date.now();
    var state = null;
    try {
      state = JSON.parse(window.localStorage.getItem(key) || "null");
    } catch (e) {
      state = null;
    }

    if (!state || !Number.isFinite(state.reset) || now >= state.reset) {
      state = { count: 0, reset: now + hours * 60 * 60 * 1000 };
    }
    if (state.count >= max) return false;

    state.count += 1;
    try {
      window.localStorage.setItem(key, JSON.stringify(state));
    } catch (e) {
      // Storage can be disabled; allow this page view without breaking it.
    }
    return true;
  }

  function load(zone, src, capKey, max, hours) {
    if (!allow(capKey, max, hours)) return;
    var script = document.createElement("script");
    script.async = true;
    script.dataset.zone = zone;
    script.src = src;
    (document.body || document.documentElement).appendChild(script);
  }

  load("11610753", "https://n6wxm.com/vignette.min.js", "bryme-mt-vig", 4, 4);
  load("11610749", "https://nap5k.com/tag.min.js", "bryme-mt-z2", 12, 12);
})();
