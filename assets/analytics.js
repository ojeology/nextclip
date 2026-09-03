/* BRYME analytics + cookie consent.
 *
 * Nothing that stores or transmits data runs until the visitor chooses.
 * Google Consent Mode v2 defaults are set to "denied" before any tag loads,
 * so the pre-consent state is compliant and ready for AdSense later.
 *
 * Decline => GA4 is never loaded at all.
 * Accept  => GA4 loads and consent is granted.
 *
 * Choice persists in localStorage for 6 months. Users can change it any time
 * via the footer "Cookie settings" link (or any [data-cookie-settings] element).
 */
(function () {
  "use strict";

  var GA_ID = "G-NQKHPBYFE8";
  var KEY = "bryme.consent.v1";
  var MAX_AGE_DAYS = 180;

  /* ---------- Consent Mode v2 defaults: denied, before anything else ---------- */
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;

  gtag("consent", "default", {
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    analytics_storage: "denied",
    functionality_storage: "granted",
    security_storage: "granted",
    wait_for_update: 500
  });

  /* ---------- stored choice ---------- */
  function read() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return null;
      var v = JSON.parse(raw);
      if (!v || !v.choice || !v.at) return null;
      var age = (Date.now() - v.at) / 86400000;
      if (age > MAX_AGE_DAYS) return null;   // expired: ask again
      return v.choice;                        // "accepted" | "declined"
    } catch (e) { return null; }
  }

  function write(choice) {
    try {
      localStorage.setItem(KEY, JSON.stringify({ choice: choice, at: Date.now() }));
    } catch (e) { /* private mode: choice lasts the session only */ }
  }

  /* ---------- GA4, loaded only on accept ---------- */
  var loaded = false;
  function loadGA() {
    if (loaded) return;
    if (!GA_ID || !/^G-[A-Z0-9]+$/.test(GA_ID)) return;
    loaded = true;

    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);

    gtag("js", new Date());
    gtag("config", GA_ID, { anonymize_ip: true });
  }

  function grant() {
    gtag("consent", "update", {
      ad_storage: "granted",
      ad_user_data: "granted",
      ad_personalization: "granted",
      analytics_storage: "granted"
    });
    loadGA();
  }

  function deny() {
    gtag("consent", "update", {
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied",
      analytics_storage: "denied"
    });
  }

  /* ---------- global privacy signals: honour without prompting ---------- */
  function signalsSayNo() {
    try {
      if (navigator.globalPrivacyControl === true) return true;
      var dnt = navigator.doNotTrack || window.doNotTrack || navigator.msDoNotTrack;
      return dnt === "1" || dnt === 1 || dnt === "yes";
    } catch (e) { return false; }
  }

  /* ---------- banner ---------- */
  var STYLE_ID = "bryme-consent-style";
  var CSS =
    '.bc-bar{position:fixed;left:0;right:0;bottom:0;z-index:9999;' +
    'background:rgba(12,14,17,.97);border-top:1px solid #272b31;' +
    'box-shadow:0 -10px 30px rgba(0,0,0,.45);padding:16px 20px;' +
    'font:14px/1.55 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:#f4f5f6;' +
    'animation:bc-in .22s ease-out}' +
    '@keyframes bc-in{from{transform:translateY(100%)}to{transform:translateY(0)}}' +
    '@media(prefers-reduced-motion:reduce){.bc-bar{animation:none}}' +
    '.bc-in{max-width:1180px;margin:auto;display:flex;gap:18px;align-items:center;flex-wrap:wrap}' +
    '.bc-tx{flex:1 1 420px;min-width:260px;margin:0;color:#c9ced4;font-size:13.5px}' +
    '.bc-tx b{color:#f4f5f6;display:block;margin-bottom:3px;font-size:14.5px}' +
    '.bc-tx a{color:#e7bb5c;text-decoration:underline}' +
    '.bc-btns{display:flex;gap:10px;flex:0 0 auto;flex-wrap:wrap}' +
    '.bc-btn{font:inherit;font-weight:800;font-size:13.5px;padding:11px 20px;border-radius:6px;' +
    'cursor:pointer;border:1px solid #272b31;background:#171b20;color:#f4f5f6;transition:.15s}' +
    '.bc-btn:hover{border-color:#4a525d}' +
    '.bc-ok{background:#e7bb5c;border-color:#e7bb5c;color:#14171d}' +
    '.bc-ok:hover{filter:brightness(1.07);border-color:#e7bb5c}' +
    '.bc-btn:focus-visible{outline:2px solid #e7bb5c;outline-offset:2px}' +
    /* light theme (site supports [data-theme="light"]) */
    '[data-theme="light"] .bc-bar{background:rgba(255,255,255,.98);border-top-color:rgba(20,30,44,.16);' +
    'box-shadow:0 -10px 30px rgba(20,30,44,.14);color:#171b22}' +
    '[data-theme="light"] .bc-tx{color:#4a5560}' +
    '[data-theme="light"] .bc-tx b{color:#171b22}' +
    '[data-theme="light"] .bc-tx a{color:#a9761b}' +
    '[data-theme="light"] .bc-btn{background:#fff;border-color:rgba(20,30,44,.22);color:#171b22}' +
    '[data-theme="light"] .bc-btn:hover{border-color:#8b929b}' +
    '[data-theme="light"] .bc-ok{background:#e7bb5c;border-color:#d9a83f;color:#14171d}' +
    '@media(max-width:760px){.bc-bar{padding:14px}.bc-in{gap:12px}' +
    '.bc-btns{width:100%}.bc-btn{flex:1 1 0;text-align:center;padding:12px 10px}}';

  function injectStyle() {
    if (document.getElementById(STYLE_ID)) return;
    var st = document.createElement("style");
    st.id = STYLE_ID;
    st.textContent = CSS;
    document.head.appendChild(st);
  }

  var bar = null;

  function close() {
    if (bar && bar.parentNode) bar.parentNode.removeChild(bar);
    bar = null;
  }

  /* Record the choice, apply it, and tell the rest of the site (the Monetag
     loader in site-app.js listens for this so ads can start without a reload). */
  function choose(choice) {
    write(choice);
    if (choice === "accepted") { grant(); } else { deny(); }
    close();
    try {
      window.dispatchEvent(new CustomEvent("bryme:consent", { detail: { choice: choice } }));
    } catch (e) { /* older browsers: the choice still applies on next pageview */ }
  }

  function show() {
    if (bar) return;
    injectStyle();

    bar = document.createElement("div");
    bar.className = "bc-bar";
    bar.setAttribute("role", "dialog");
    bar.setAttribute("aria-live", "polite");
    bar.setAttribute("aria-label", "Cookie choices");

    var inner = document.createElement("div");
    inner.className = "bc-in";

    var tx = document.createElement("p");
    tx.className = "bc-tx";
    tx.innerHTML =
      "<b>Cookies on BRYME</b>We use analytics cookies to understand which pages people " +
      "actually read. They are only set if you accept. Decline and nothing is loaded \u2014 " +
      'the site works exactly the same. <a href="/privacy/#cookies">Privacy policy</a>.';

    var btns = document.createElement("div");
    btns.className = "bc-btns";

    var no = document.createElement("button");
    no.type = "button";
    no.className = "bc-btn";
    no.textContent = "Decline";

    var yes = document.createElement("button");
    yes.type = "button";
    yes.className = "bc-btn bc-ok";
    yes.textContent = "Accept";

    no.addEventListener("click", function () { choose("declined"); });
    yes.addEventListener("click", function () { choose("accepted"); });

    btns.appendChild(no);
    btns.appendChild(yes);
    inner.appendChild(tx);
    inner.appendChild(btns);
    bar.appendChild(inner);

    (document.body || document.documentElement).appendChild(bar);
    yes.focus({ preventScroll: true });
  }

  /* ---------- let users revisit the choice ---------- */
  window.brymeCookieSettings = function () {
    try { localStorage.removeItem(KEY); } catch (e) {}
    deny();
    show();
    return false;
  };

  function wireSettingsLinks() {
    var nodes = document.querySelectorAll("[data-cookie-settings]");
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].addEventListener("click", function (ev) {
        ev.preventDefault();
        window.brymeCookieSettings();
      });
    }
  }

  /* ---------- boot ---------- */
  function boot() {
    wireSettingsLinks();

    var choice = read();
    if (choice === "accepted") { grant(); return; }
    if (choice === "declined") { deny(); return; }

    if (signalsSayNo()) { write("declined"); deny(); return; }

    show();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
