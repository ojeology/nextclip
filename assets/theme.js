/* BRYME theme switch — light (default) / dark, remembered per browser.
 *
 * Loaded synchronously in <head> so the correct theme is applied before the
 * first paint. Without that, a reader who chose dark gets a bright flash of
 * the light theme on every navigation.
 *
 * No inline script is used anywhere on the site (CSP-friendly), so the
 * pre-paint work has to live in this file.
 */
(function () {
  "use strict";
  var KEY = "bryme-theme";
  var root = document.documentElement;

  function stored() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function remember(v) {
    try { localStorage.setItem(KEY, v); } catch (e) { /* private mode */ }
  }
  function prefersDark() {
    return !!(window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches);
  }
  function resolve() {
    var s = stored();
    if (s === "dark" || s === "light") return s;
    return prefersDark() ? "dark" : "light";
  }

  function apply(theme) {
    if (theme === "dark") root.setAttribute("data-theme", "dark");
    else root.removeAttribute("data-theme");
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", theme === "dark" ? "#12100e" : "#faf6ee");
    sync(theme);
  }

  function sync(theme) {
    var dark = theme === "dark";
    var btns = document.querySelectorAll("[data-theme-toggle]");
    for (var i = 0; i < btns.length; i++) {
      btns[i].setAttribute("aria-pressed", dark ? "true" : "false");
      btns[i].setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
      var t = btns[i].querySelector(".theme-toggle-text");
      if (t) t.textContent = dark ? "Switch to light theme" : "Switch to dark theme";
    }
  }

  /* Run immediately — the <html> element exists by the time head scripts run. */
  apply(resolve());

  document.addEventListener("DOMContentLoaded", function () {
    sync(root.getAttribute("data-theme") === "dark" ? "dark" : "light");
    document.addEventListener("click", function (ev) {
      var btn = ev.target.closest && ev.target.closest("[data-theme-toggle]");
      if (!btn) return;
      ev.preventDefault();
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      remember(next);
      apply(next);
    });
  });

  /* Follow the OS only while the reader has not made an explicit choice. */
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onChange = function (e) { if (!stored()) apply(e.matches ? "dark" : "light"); };
    if (mq.addEventListener) mq.addEventListener("change", onChange);
    else if (mq.addListener) mq.addListener(onChange);
  }
})();
