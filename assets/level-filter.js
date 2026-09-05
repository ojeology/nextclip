/* BRYME skill-level filter.

   Progressive enhancement: the control is a group of native radio buttons, so
   it is keyboard and screen-reader native and the guides are all present in the
   HTML whether or not this script runs. JS only hides cards that don't match.

   Supports /learn/?level=beginner and keeps the URL in sync so a level view can
   be shared. */
(function () {
  "use strict";

  var form = document.getElementById("level-filter");
  if (!form) return;

  var radios = Array.prototype.slice.call(form.querySelectorAll('input[name="level"]'));
  var note = document.getElementById("level-note");
  var cards = Array.prototype.slice.call(document.querySelectorAll("[data-level]"));
  if (!radios.length || !cards.length) return;

  var LABELS = { all: "all levels", beginner: "beginner", intermediate: "intermediate", advanced: "advanced" };

  form.addEventListener("submit", function (e) { e.preventDefault(); });

  function apply(value, pushUrl) {
    var shown = 0;
    cards.forEach(function (c) {
      var on = value === "all" || c.getAttribute("data-level") === value;
      c.hidden = !on;
      if (on) shown += 1;
    });

    if (note) {
      note.textContent = value === "all"
        ? "Showing all " + shown + " guides."
        : "Showing " + shown + " " + LABELS[value] + " guide" + (shown === 1 ? "" : "s") + ".";
    }

    if (pushUrl && window.history && window.history.replaceState) {
      var url = new URL(window.location.href);
      if (value === "all") url.searchParams.delete("level");
      else url.searchParams.set("level", value);
      window.history.replaceState({}, "", url);
    }
  }

  radios.forEach(function (r) {
    r.addEventListener("change", function () { if (r.checked) apply(r.value, true); });
  });

  /* deep link */
  var initial = "all";
  try {
    var q = new URL(window.location.href).searchParams.get("level");
    if (q && LABELS[q.toLowerCase()]) initial = q.toLowerCase();
  } catch (e) { initial = "all"; }

  var match = radios.filter(function (r) { return r.value === initial; })[0];
  if (match) match.checked = true;
  apply(initial, false);
})();
