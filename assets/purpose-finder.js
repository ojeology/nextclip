/* BRYME "what do you want to write?" finder.

   Progressive enhancement only: every purpose and every link is in the HTML and
   works with JavaScript disabled. This just narrows a long list as you type. */
(function () {
  "use strict";

  var input = document.getElementById("purpose-q");
  if (!input) return;

  var rows = Array.prototype.slice.call(document.querySelectorAll(".purpose-row"));
  var blocks = Array.prototype.slice.call(document.querySelectorAll("[data-cat-block]"));
  var countEl = document.getElementById("purpose-count");
  var emptyEl = document.getElementById("purpose-empty");
  var total = rows.length;

  var form = input.closest("form");
  if (form) form.addEventListener("submit", function (e) { e.preventDefault(); });

  function norm(s) { return (s || "").toLowerCase().trim(); }

  function apply(q) {
    q = norm(q);
    var shown = 0;

    rows.forEach(function (r) {
      var hay = r.getAttribute("data-purpose") || "";
      var on = !q || hay.indexOf(q) !== -1;
      r.hidden = !on;
      if (on) shown += 1;
    });

    /* hide a whole category block when nothing in it matches */
    blocks.forEach(function (b) {
      var any = b.querySelector(".purpose-row:not([hidden])");
      b.hidden = !any;
    });

    if (countEl) {
      countEl.textContent = !q
        ? total + " things to write"
        : shown + " match" + (shown === 1 ? "" : "es") + " for “" + q + "”";
      countEl.hidden = shown === 0;
    }
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  var t = null;
  input.addEventListener("input", function () {
    clearTimeout(t);
    t = setTimeout(function () { apply(input.value); }, 80);
  });

  /* support /find/?q=email */
  try {
    var q = new URL(window.location.href).searchParams.get("q");
    if (q) { input.value = q; apply(q); }
  } catch (e) { /* ignore */ }
})();
