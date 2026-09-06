/* BRYME /read/ — filters the server-rendered article list.
   Progressive enhancement: every article is already in the HTML. */
(function () {
  "use strict";
  var input = document.getElementById("article-search");
  var list = document.getElementById("article-list");
  if (!list) return;
  var rows = Array.prototype.slice.call(list.querySelectorAll("[data-hay]"));
  var chips = Array.prototype.slice.call(document.querySelectorAll(".filter-chip"));
  var empty = document.getElementById("article-empty");
  var status = document.getElementById("article-status");
  var group = "";

  function apply() {
    var q = (input && input.value || "").toLowerCase().trim();
    var shown = 0;
    rows.forEach(function (r) {
      var okQ = !q || r.getAttribute("data-hay").indexOf(q) !== -1;
      var okG = !group || r.getAttribute("data-group") === group;
      var hit = okQ && okG;
      r.hidden = !hit;
      if (hit) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
    if (status) status.textContent = shown + (shown === 1 ? " article" : " articles");
  }

  if (input) { input.addEventListener("input", apply); input.addEventListener("search", apply); }
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      group = c.getAttribute("data-filter") || "";
      chips.forEach(function (o) { o.classList.toggle("is-on", o === c); });
      apply();
    });
  });
  apply();
})();
