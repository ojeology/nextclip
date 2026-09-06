/* BRYME country discovery: filters the server-rendered country cards as you
   type. Progressive enhancement only — every card and every count is already
   in the HTML, so the page works fully with JavaScript disabled. */
(function () {
  "use strict";
  var input = document.getElementById("country-search");
  var grid = document.getElementById("country-grid");
  if (!input || !grid) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll("[data-country]"));
  var empty = document.getElementById("country-empty");
  var status = document.getElementById("country-status");
  var total = cards.length;

  function norm(s) { return (s || "").toLowerCase().trim(); }

  function apply() {
    var q = norm(input.value);
    var shown = 0;
    cards.forEach(function (c) {
      var hay = norm(c.getAttribute("data-country")) + " " + norm(c.getAttribute("data-iso"));
      var hit = !q || hay.indexOf(q) !== -1;
      c.hidden = !hit;
      if (hit) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
    if (status) {
      status.textContent = q
        ? shown + (shown === 1 ? " country matches" : " countries match") + ' "' + input.value.trim() + '"'
        : total + " countries with publications BRYME has verified";
    }
  }

  input.addEventListener("input", apply);
  input.addEventListener("search", apply);
  apply();
})();
