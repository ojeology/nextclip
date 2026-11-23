/* ================================================================
   The catalogue filter — assets/catalogue.js
   ----------------------------------------------------------------
   Six hundred rows, one input. Everything runs on the reader's own
   device, on a list that is already in the HTML, so:
     · it works before any network round-trip,
     · the no-JavaScript page is the same complete index,
     · nothing about what a reader searches for leaves the page.

   Two filters, expected to compose: a free-text needle and a first
   letter. Counts update live in the sticky bar and in each register
   heading, and a register with no matches disappears rather than
   sitting there empty.
   ================================================================ */
(function () {
  "use strict";

  var q = document.getElementById("cat-q");
  var bar = document.getElementById("cat-bar");
  var count = document.getElementById("cat-count");
  var empty = document.getElementById("cat-empty");
  var reset = document.getElementById("cat-reset");
  var az = document.getElementById("cat-az");
  if (!q || !bar) return;

  var rows = Array.prototype.slice.call(document.querySelectorAll(".cat-row"));
  var groups = Array.prototype.slice.call(document.querySelectorAll("[data-rg]"));
  var letterBtn = {};
  var needle = "";
  var letter = "";

  /* The sticky filter bar has to sit under the masthead, which is itself
     sticky and 100–140px tall depending on the viewport. Measuring it is
     more reliable than guessing a height in CSS. */
  function measureHead() {
    var head = document.querySelector("header.site-head, .site-head, header");
    var h = head ? Math.round(head.getBoundingClientRect().height) : 0;
    document.documentElement.style.setProperty("--mast-h", h + "px");
  }

  function apply() {
    var shown = 0;
    var perGroup = {};
    for (var i = 0; i < rows.length; i++) {
      var row = rows[i];
      var text = row.getAttribute("data-k") || "";
      var first = (row.querySelector(".cat-t") || { textContent: "" }).textContent.trim().charAt(0).toUpperCase();
      var ok = (!needle || text.indexOf(needle) !== -1) && (!letter || first === letter);
      row.hidden = !ok;
      if (ok) {
        shown++;
        var g = row.closest("[data-rg]");
        if (g) perGroup[g.getAttribute("data-rg")] = (perGroup[g.getAttribute("data-rg")] || 0) + 1;
      }
    }
    var jumps = Array.prototype.slice.call(document.querySelectorAll("[data-jump]"));
    jumps.forEach(function (el) {
      el.textContent = perGroup[el.getAttribute("data-jump")] || 0;
    });
    groups.forEach(function (g) {
      var key = g.getAttribute("data-rg");
      var n = perGroup[key] || 0;
      g.hidden = n === 0;
      var c = g.querySelector("[data-count]");
      if (c) c.textContent = n;
    });
    if (count) {
      count.textContent = shown === rows.length
        ? rows.length + " entries"
        : shown + " of " + rows.length;
    }
    if (empty) empty.hidden = shown !== 0;
  }

  function setLetter(next) {
    letter = next;
    Object.keys(letterBtn).forEach(function (k) {
      letterBtn[k].setAttribute("aria-pressed", k === letter ? "true" : "false");
    });
    apply();
  }

  q.addEventListener("input", function () {
    needle = q.value.trim().toLowerCase();
    apply();
  });

  if (az) {
    az.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-letter]");
      if (!b) return;
      letterBtn[b.getAttribute("data-letter")] = b;
      var l = b.getAttribute("data-letter");
      setLetter(letter === l ? "" : l);
    });
  }

  if (reset) {
    reset.addEventListener("click", function () {
      q.value = "";
      needle = "";
      setLetter("");
      q.focus();
    });
  }

  measureHead();
  window.addEventListener("resize", measureHead);
  apply();
})();
