/* BRYME fitness tools v2 - calculators + 1RM + plate loader + workout builder.
   Everything runs in this browser. No network calls, no storage:
   the numbers never leave the device. */
(function () {
  "use strict";
  function out(id) { return document.getElementById(id); }
  function r2(v) { return Math.round(v * 10) / 10; }
  function toNearest(v, step) { return Math.round(v / step) * step; }

  var REP_PCTS = [[1, 100], [2, 95], [3, 93], [4, 90], [5, 87], [6, 85], [7, 82], [8, 80], [9, 77], [10, 75], [11, 72], [12, 70]];

  var fn = {
    bmi: function () {
      var h = parseFloat((out("bmi-h") || {}).value), w = parseFloat((out("bmi-w") || {}).value);
      if (!(h > 100 && h < 230 && w > 30 && w < 250)) return "Please enter a height (100-230 cm) and weight (30-250 kg).";
      var v = w / Math.pow(h / 100, 2);
      var band = v < 18.5 ? "below the usual healthy band"
        : v < 25 ? "inside the usual healthy band"
        : v < 30 ? "above the usual healthy band"
        : "well above the usual healthy band";
      return "BMI " + (Math.round(v * 10) / 10) + " - " + band + ". A rough screen, not a verdict.";
    },
    h2o: function () {
      var w = parseFloat((out("h2o-w") || {}).value);
      if (!(w > 30 && w < 250)) return "Please enter a weight (30-250 kg).";
      var lo = Math.round(w * 30) / 10, hi = Math.round(w * 35) / 10;
      return "About " + lo + "-" + hi + " litres of fluid a day - food covers part of it.";
    },
    pro: function () {
      var w = parseFloat((out("pro-w") || {}).value);
      if (!(w > 30 && w < 250)) return "Please enter a weight (30-250 kg).";
      return "About " + Math.round(w * 1.2) + "-" + Math.round(w * 2.0) + " g of protein a day if you train.";
    },
    rm: function () {
      var w = parseFloat((out("rm-w") || {}).value), r = parseInt((out("rm-r") || {}).value, 10);
      if (!(w > 0 && w < 500) || !(r > 0 && r <= 12)) return "Enter the weight you lifted and the reps (1-12). Past 12 reps the estimate gets unreliable - so we stop at 12.";
      var orm = w * (1 + r / 30); /* Epley */
      var unit = "kg";
      var step = 2.5;
      var rows = "";
      for (var i = 0; i < REP_PCTS.length; i++) {
        var reps = REP_PCTS[i][0], pct = REP_PCTS[i][1];
        rows += "<tr><td>" + pct + "%</td><td>" + toNearest(orm * pct / 100, step) + " " + unit + "</td><td>~" + reps + " rep" + (reps > 1 ? "s" : "") + "</td></tr>";
      }
      return "Estimated one-rep max: <b>" + toNearest(orm, step) + " kg</b> (rounded to " + step + " kg). An estimate, not a measurement."
        + ' <table class="rm-table"><thead><tr><th>Of max</th><th>Weight</th><th>Reps</th></tr></thead><tbody>' + rows + "</tbody></table>"
        + "You never need to test a true one-rep max: training around 75-85% for 3-8 reps builds the same strength with far less risk.";
    },
    plates: function () {
      var t = parseFloat((out("pl-t") || {}).value);
      var bar = parseFloat((out("pl-bar") || {}).value);
      if (!(t > 0 && t < 600) || !(bar >= 0 && bar < 100)) return "Enter a target weight and the bar weight.";
      if (t < bar) return "That is below the bar alone (" + bar + " kg). Lower the target or use a lighter bar.";
      var kg = [25, 20, 15, 10, 5, 2.5, 1.25];
      var per = (t - bar) / 2;
      var left = per, picked = [];
      for (var i = 0; i < kg.length; i++) {
        while (left >= kg[i] - 0.001) { picked.push(kg[i]); left -= kg[i]; }
      }
      if (!picked.length) return "The bar alone (" + bar + " kg) is your weight - nothing to load.";
      var s = picked.join(" + ");
      var tail = left > 0.01 ? " (about " + r2(left * 2) + " kg short - round weights are fine)" : "";
      return "Each side: <b>" + s + " kg</b>" + tail + ". Same plates go on both sides.";
    },
    builder: function () {
      var goal = (out("wb-goal") || {}).value, days = (out("wb-days") || {}).value;
      var plan = BUILDER_PLANS[goal + "-" + days];
      if (!plan) return "Pick a goal and a number of days, then build.";
      var html = "";
      for (var d = 0; d < plan.length; d++) {
        var day = plan[d], items = "";
        for (var j = 0; j < day.moves.length; j++) {
          var m = day.moves[j];
          items += '<li><a href="' + m[1] + '">' + m[0] + "</a> - " + m[2] + "</li>";
        }
        html += '<div class="wb-day"><b>' + day.name + "</b><ul>" + items + "</ul></div>";
      }
      html += '<p class="wb-note">Warm up five minutes first (see <a href="/fitness/how-to-warm-up/">how to warm up</a>). '
        + "Stop 1-2 reps short of failure. When the top of a range feels easy two sessions running, add a rep or a little weight. "
        + "Rest 60-90 seconds between sets. This is a starting template, not medical advice - results are not guaranteed.</p>";
      return html;
    }
  };

  /* The builder's plans. Links are full /fitness/ paths: this file is static
     and only runs on fitness pages, so the prefix is safe. */
  var BUILDER_PLANS = {
    "health-3": [
      { name: "Day A - full body", moves: [
        ["Bodyweight squat", "/fitness/exercise-library-legs/#bodyweight-squat", "3 x 8-12"],
        ["Incline push-up", "/fitness/exercise-library-push/#incline-push-up", "3 x 6-12"],
        ["Doorway row", "/fitness/exercise-library-pull/#doorway-row", "3 x 8-12"],
        ["Glute bridge", "/fitness/exercise-library-legs/#glute-bridge", "3 x 10-15"],
        ["Forearm plank", "/fitness/exercise-library-core/#forearm-plank", "3 x 20-40 sec"],
        ["Marching in place", "/fitness/exercise-library-cond/#marching-in-place", "5-10 min"]] },
      { name: "Day B - full body", moves: [
        ["Reverse lunge", "/fitness/exercise-library-legs/#reverse-lunge", "3 x 6-10 per leg"],
        ["Dumbbell shoulder press", "/fitness/exercise-library-push/#dumbbell-shoulder-press", "3 x 8-12"],
        ["Towel row", "/fitness/exercise-library-pull/#towel-row", "3 x 8-12"],
        ["Dead bug", "/fitness/exercise-library-core/#dead-bug", "3 x 6-10 per side"],
        ["Jumping jack", "/fitness/exercise-library-cond/#jumping-jack", "3 x 30-60 sec"]] },
      { name: "Day C - full body", moves: [
        ["Step-up", "/fitness/exercise-library-legs/#step-up", "3 x 6-10 per leg"],
        ["Bench dip", "/fitness/exercise-library-push/#bench-dip", "3 x 6-12"],
        ["Band pull-apart", "/fitness/exercise-library-pull/#band-pull-apart", "3 x 12-20"],
        ["Bird dog", "/fitness/exercise-library-core/#bird-dog", "3 x 6-8 per side"],
        ["Stair climbing", "/fitness/exercise-library-cond/#stair-climb", "5-10 min"]] }
    ],
    "muscle-4": [
      { name: "Day 1 - upper body", moves: [
        ["Push-up", "/fitness/exercise-library-push/#push-up", "3 x 5-15"],
        ["One-arm dumbbell row", "/fitness/exercise-library-pull/#one-arm-dumbbell-row", "3 x 8-12 per side"],
        ["Dumbbell shoulder press", "/fitness/exercise-library-push/#dumbbell-shoulder-press", "3 x 8-12"],
        ["Band pulldown", "/fitness/exercise-library-pull/#band-pulldown", "3 x 10-15"],
        ["Dumbbell curl", "/fitness/exercise-library-pull/#dumbbell-curl", "2 x 10-15"],
        ["Forearm plank", "/fitness/exercise-library-core/#forearm-plank", "3 x 30-45 sec"]] },
      { name: "Day 2 - lower body", moves: [
        ["Goblet squat", "/fitness/exercise-library-legs/#goblet-squat", "3 x 8-12"],
        ["Dumbbell Romanian deadlift", "/fitness/exercise-library-legs/#romanian-deadlift", "3 x 8-12"],
        ["Walking lunge", "/fitness/exercise-library-legs/#walking-lunge", "2 x 10-14 steps"],
        ["Calf raise", "/fitness/exercise-library-legs/#calf-raise", "3 x 12-20"],
        ["Lying leg raise", "/fitness/exercise-library-core/#lying-leg-raise", "3 x 8-12"]] },
      { name: "Day 3 - upper body", moves: [
        ["Dumbbell bench press", "/fitness/exercise-library-push/#dumbbell-bench-press", "3 x 8-12"],
        ["Band face pull", "/fitness/exercise-library-pull/#band-face-pull", "3 x 12-15"],
        ["Bench dip", "/fitness/exercise-library-push/#bench-dip", "3 x 6-12"],
        ["Dumbbell lateral raise", "/fitness/exercise-library-push/#dumbbell-lateral-raise", "3 x 12-15"],
        ["Hammer curl", "/fitness/exercise-library-pull/#hammer-curl", "2 x 10-15"],
        ["Band Pallof press", "/fitness/exercise-library-core/#pallof-press", "3 x 8-10 per side"]] },
      { name: "Day 4 - lower body", moves: [
        ["Step-up", "/fitness/exercise-library-legs/#step-up", "3 x 8-10 per leg"],
        ["Single-leg glute bridge", "/fitness/exercise-library-legs/#single-leg-glute-bridge", "3 x 8-12 per side"],
        ["Sumo squat", "/fitness/exercise-library-legs/#sumo-squat", "3 x 10-15"],
        ["Wall sit", "/fitness/exercise-library-legs/#wall-sit", "3 x 20-45 sec"],
        ["Suitcase carry", "/fitness/exercise-library-core/#suitcase-carry", "3 x 30-40 steps per side"]] }
    ],
    "strength-3": [
      { name: "Day A - squat + push + pull", moves: [
        ["Goblet squat", "/fitness/exercise-library-legs/#goblet-squat", "5 x 5, heavy"],
        ["Push-up", "/fitness/exercise-library-push/#push-up", "5 x 5 (harder version when 5x5 is easy)"],
        ["Towel row", "/fitness/exercise-library-pull/#towel-row", "5 x 5, steep angle"],
        ["Suitcase carry", "/fitness/exercise-library-core/#suitcase-carry", "3 heavy carries"]] },
      { name: "Day B - hinge + press", moves: [
        ["Dumbbell Romanian deadlift", "/fitness/exercise-library-legs/#romanian-deadlift", "5 x 5, slow"],
        ["Pike push-up", "/fitness/exercise-library-push/#pike-push-up", "5 x 5"],
        ["One-arm dumbbell row", "/fitness/exercise-library-pull/#one-arm-dumbbell-row", "5 x 5 per side"],
        ["Dead bug", "/fitness/exercise-library-core/#dead-bug", "3 x 8 slow per side"]] },
      { name: "Day C - legs + arms + core", moves: [
        ["Step-up", "/fitness/exercise-library-legs/#step-up", "5 x 5 per leg, weighted"],
        ["Bench dip", "/fitness/exercise-library-push/#bench-dip", "5 x 5, legs straight"],
        ["Band pulldown", "/fitness/exercise-library-pull/#band-pulldown", "5 x 5, thick band"],
        ["Hollow hold", "/fitness/exercise-library-core/#hollow-hold", "3 x 10-20 sec"]] }
    ]
  };

  document.addEventListener("click", function (e) {
    var b = e.target && e.target.closest ? e.target.closest(".calc-go") : null;
    if (!b) return;
    var kind = b.getAttribute("data-calc");
    var ids = { bmi: "bmi-out", h2o: "h2o-out", pro: "pro-out", rm: "rm-out", plates: "plates-out", builder: "builder-out" };
    var o = out(ids[kind]);
    if (!o || !fn[kind]) return;
    var v = fn[kind]();
    if (b.getAttribute("data-html") === "1") o.innerHTML = v; else o.textContent = v;
  }, false);
})();
