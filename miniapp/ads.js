/* BRYME ad configuration — Monetag Rewarded Popup (Telegram Mini App SDK).
 * Fill sdkUrl + zoneId from your Monetag dashboard ("Activate" on the
 * Rewarded Popup zone shows the integration snippet; the script URL goes in
 * sdkUrl and the numeric zone from show_XXXXXX() goes in zoneId).
 * Until both are set, market unlocks stay FREE (no placeholders, no dead ads). */
window.BRYME_AD_CONFIG = {
  sdkUrl: "",   // e.g. "https:// …… /sdk.js"  (from the dashboard snippet)
  zoneId: 0,    // e.g. 123456  (the number in show_123456)
  smartlink: "" // optional fallback direct link
};

/* Rewarded Popup loader — called on the unlock tap (needs the user gesture).
 * Docs: show_<zone>({type:"pop"}) opens the offer; the promise resolves with
 * { reward_event_type: "valued"|"not_valued", estimated_price, ... }. */
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
  function showRewarded(requestVar) {
    var cfg = window.BRYME_AD_CONFIG || {};
    if (!cfg.sdkUrl || !cfg.zoneId) return Promise.resolve({ ok: false, reason: "not-configured" });
    return loadSdk().then(function (loaded) {
      if (!loaded) return { ok: false, reason: "sdk-failed" };
      var fn;
      try { fn = window["show_" + cfg.zoneId]; } catch (e) { fn = null; }
      if (typeof fn !== "function") return { ok: false, reason: "no-handler" };
      return fn({ type: "pop", request_var: requestVar || "unlock" }).then(
        function (r) { return { ok: true, result: r || {} }; },
        function () { return { ok: false, reason: "rejected" }; }
      );
    });
  }
  return { configured: configured, showRewarded: showRewarded };
})();
