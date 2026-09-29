/* BRYME Home — sophisticated layer for Writers-first landing.
   Additive only, no network, no storage beyond what tech-hub.js already uses.
   Handles 1-7 pathways, keyboard help (?), and theme-aware gauges.
   CSP: script-src 'self' https: — no inline, no eval.
*/
(function () {
  "use strict";
  function on(el, ev, fn) { if (el) el.addEventListener(ev, fn); }
  function all(sel, root) { return [].slice.call((root || document).querySelectorAll(sel)); }

  var root = document.querySelector('[data-tm-desk="home"]');
  if (!root) return;

  // Enhance gauge hover with theme awareness
  var gauges = all(".tm-gauge", root);
  gauges.forEach(function (g) {
    on(g, "mouseenter", function () { g.setAttribute("data-hover", "1"); });
    on(g, "mouseleave", function () { g.removeAttribute("data-hover"); });
  });

  // Keyboard help: ? shows an alert with shortcuts (non-blocking, no modal)
  on(document, "keydown", function (ev) {
    var tag = ((ev.target && ev.target.tagName) || "").toUpperCase();
    var typing = tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT";
    if (typing) return;
    if (ev.key === "?" || (ev.shiftKey && ev.key === "/")) {
      ev.preventDefault();
      var help = [
        "BRYME Home — keyboard shortcuts",
        "",
        "/ — focus filter",
        "Ctrl+K — open command palette",
        "1–7 — jump to Writers pathways (Write, Submit, Discover, Research, Earn, Tools, Career)",
        "0 — clear all filters",
        "Esc — close palette / drawer",
        "? — this help",
        "",
        "Theme toggle in header remembers your choice (light/dark) via localStorage.",
        "◇ Save on each row saves to this browser only."
      ].join("\n");
      // Use a small non-intrusive toast instead of alert for better UX
      var toast = document.getElementById("home-kbd-help");
      if (!toast) {
        toast = document.createElement("div");
        toast.id = "home-kbd-help";
        toast.setAttribute("role", "status");
        toast.setAttribute("aria-live", "polite");
        toast.style.cssText = "position:fixed;bottom:20px;left:50%;transform:translateX(-50%);max-width:520px;white-space:pre-line;background:var(--sheet, #fff);color:var(--ink, #000);border:1px solid var(--line-strong, #ccc);border-radius:10px;padding:16px 18px;box-shadow:0 10px 30px rgba(0,0,0,.15);font:13px/1.5 ui-sans-serif,system-ui;z-index:100;cursor:pointer";
        toast.textContent = help + "\n\n(click to dismiss)";
        on(toast, "click", function () { if (toast.parentNode) toast.parentNode.removeChild(toast); });
        document.body.appendChild(toast);
        setTimeout(function () { if (toast && toast.parentNode) toast.parentNode.removeChild(toast); }, 8000);
      } else {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }
    }
  });

  // Ensure secondary cards are also filterable via same search if needed
  // No-op: tech-hub.js already handles .tm-row only; secondary as cards are outside shelves intentionally (20-25% compact).

  // Mark home as ready
  document.documentElement.classList.add("home-js");
  try { console.log("[BRYME home] living house ready — 7 pathways, palette Ctrl+K, / filter, ? help"); } catch (e) {}
})();
