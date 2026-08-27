/* BRYME ad configuration — Monetag Rewarded Popup (Telegram Mini App SDK).
 * Zone 11668156 · dashboard snippet: show_11668156('pop') */
window.BRYME_AD_CONFIG = {
  sdkUrl: "https://libtl.com/sdk.js",
  zoneId: 11668156,
  smartlink: "",
  /* In-App Interstitial — auto interstitials for ALL visitors.
   * frequency 2 / capping 0.1h (6 min) / interval 30s / timeout 5s / everyPage false.
   * Set inApp: false to switch off instantly (one deploy). */
  inApp: true,
  inAppSettings: { frequency: 1, capping: 0.1, interval: 30, timeout: 15, everyPage: false }
};

window.BRYME_AD = (function () {
  var loading = null;
  function loadSdk() {
    var cfg = window.BRYME_AD_CONFIG || {};
    if (!cfg.sdkUrl || !cfg.zoneId) return Promise.resolve(false);
    if (loading) return loading;
    loading = new Promise(function (resolve) {
      try {
        var s = document.createElement("script");
        s.src = cfg.sdkUrl;
        s.setAttribute("data-zone", String(cfg.zoneId));
        s.setAttribute("data-sdk", "show_" + cfg.zoneId);
        s.onload = function () { resolve(true); };
        s.onerror = function () { resolve(false); };
        (document.head || document.documentElement).appendChild(s);
      } catch (e) { resolve(false); }
    });
    return loading;
  }
  function configured() {
    var cfg = window.BRYME_AD_CONFIG || {};
    return Boolean(cfg.sdkUrl && cfg.zoneId) || Boolean(cfg.smartlink);
  }
  /* Rewarded Popup — must run inside a user gesture (our unlock tap). */
  function showRewarded() {
    var cfg = window.BRYME_AD_CONFIG || {};
    if (!cfg.sdkUrl || !cfg.zoneId) return Promise.resolve({ ok: false, reason: "not-configured" });
    return loadSdk().then(function (loaded) {
      if (!loaded) return { ok: false, reason: "sdk-failed" };
      var fn = window["show_" + cfg.zoneId];
      if (typeof fn !== "function") return { ok: false, reason: "no-handler" };
      /* dashboard-canonical call: show_<zone>('pop') → resolves when the
       * rewarded view completes; rejects on ad errors. */
      return fn("pop").then(
        function () { return { ok: true }; },
        function () { return { ok: false, reason: "ad-error" }; }
      );
    });
  }
  return { configured: configured, showRewarded: showRewarded, preload: loadSdk };
})();

/* preload the SDK immediately when configured → zero latency on the tap */
if (window.BRYME_AD.configured()) {
  window.BRYME_AD.preload().then(function (ok) {
    /* In-App Interstitial: initialized once per session after the SDK loads.
     * Session persists across in-app navigation (everyPage: false), so a
     * visitor sees at most `frequency` interstitials per 6 minutes. */
    var cfg = window.BRYME_AD_CONFIG || {};
    if (ok && cfg.inApp && typeof window["show_" + cfg.zoneId] === "function") {
      try { window["show_" + cfg.zoneId]({ type: "inApp", inAppSettings: cfg.inAppSettings }); } catch (e) {}
    }
  });
}
