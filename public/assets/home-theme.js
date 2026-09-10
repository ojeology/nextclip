/* BRYME Home & DIY — dark/light theme toggle.
   External file on purpose: the site's Content-Security-Policy is script-src 'self',
   so the theme logic must not live in inline <script> blocks. */
(function () {
  var KEY = "bryme-home-theme";
  function apply(t) {
    if (t === "dark") { document.documentElement.setAttribute("data-theme", "dark"); }
    else { document.documentElement.removeAttribute("data-theme"); }
  }
  function current() {
    try {
      var t = localStorage.getItem(KEY);
      if (t === "dark" || t === "light") return t;
    } catch (e) {}
    return (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches) ? "dark" : "light";
  }
  apply(current()); /* runs from <head>, before first paint: no flash of the wrong theme */
  function wire() {
    var b = document.getElementById("home-theme");
    if (!b) return;
    function sync() {
      b.setAttribute("aria-pressed",
        document.documentElement.getAttribute("data-theme") === "dark" ? "true" : "false");
    }
    sync();
    b.addEventListener("click", function () {
      var next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      apply(next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
      sync();
    });
  }
  if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", wire); }
  else { wire(); }
})();
