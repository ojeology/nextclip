/* Third-party advertising is disabled during BRYME's 2026-09 quality rebuild.
 * Keep this inert compatibility surface so the Mini App can call the existing
 * methods without loading an ad SDK or making a third-party network request.
 */
"use strict";
window.BRYME_AD_CONFIG = { disabled: true };
window.BRYME_AD = {
  configured: function () { return false; },
  preload: function () { return Promise.resolve(false); },
  showRewarded: function () {
    return Promise.resolve({ ok: false, reason: "disabled" });
  }
};
