/* BRYME Fitness - Hyrox pace planner (CSP-safe, no storage, no network).
   Arithmetic only: a goal time is split into the eight 1 km runs and the
   station budget YOU set. Nothing here predicts your fitness - the station
   budget is yours to adjust to your own level. Maths exported for testing;
   DOM wiring is browser-only. */
(function () {
  "use strict";

  /* The Hyrox race format: 8 x 1 km runs, each followed by one station.
     Distances and reps are the standard Hyrox course. */
  var STATIONS = [
    { name: "SkiErg", detail: "1000 m" },
    { name: "Sled push", detail: "50 m" },
    { name: "Sled pull", detail: "50 m" },
    { name: "Burpee broad jumps", detail: "80 m" },
    { name: "Rowing", detail: "1000 m" },
    { name: "Farmers carry", detail: "200 m" },
    { name: "Sandbag lunges", detail: "100 m" },
    { name: "Wall balls", detail: "100 reps" }
  ];

  function parseClock(text) {
    // Accepts "1:30:00", "90:00" or "90". Returns seconds or null.
    var parts = String(text).trim().split(":");
    if (!parts.length || parts.length > 3) return null;
    var nums = parts.map(function (p) { return parseInt(p, 10); });
    if (nums.some(function (n) { return isNaN(n) || n < 0; })) return null;
    var secs = 0;
    for (var i = 0; i < nums.length; i++) secs = secs * 60 + nums[i];
    return secs > 0 ? secs : null;
  }

  function formatClock(totalSeconds) {
    var s = Math.max(0, Math.round(totalSeconds));
    var h = Math.floor(s / 3600);
    var m = Math.floor((s % 3600) / 60);
    var sec = s % 60;
    return (h > 0 ? h + ":" + String(m).padStart(2, "0") : String(m)) +
      ":" + String(sec).padStart(2, "0");
  }

  function formatPace(secondsPerKm) {
    return formatClock(secondsPerKm) + " /km";
  }

  /* The plan: split (goal - station budget) across 8 km of running. */
  function plan(goalSeconds, stationSeconds) {
    if (!goalSeconds || !stationSeconds) return null;
    if (stationSeconds >= goalSeconds) return null;
    var runTotal = goalSeconds - stationSeconds;
    var perKm = runTotal / 8;
    var perStation = stationSeconds / 8;
    var rows = [];
    var clock = 0;
    for (var i = 0; i < STATIONS.length; i++) {
      clock += perKm;
      var afterRun = clock;
      clock += perStation;
      rows.push({
        leg: i + 1,
        station: STATIONS[i].name,
        detail: STATIONS[i].detail,
        afterRun: afterRun,
        afterStation: clock
      });
    }
    return {
      perKm: perKm,
      perStation: perStation,
      runTotal: runTotal,
      rows: rows,
      total: goalSeconds
    };
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { parseClock: parseClock, plan: plan, formatClock: formatClock, formatPace: formatPace };
  }

  function wire() {
    var goalEl = document.getElementById("hyrox-goal");
    var statEl = document.getElementById("hyrox-stations");
    var goEl = document.getElementById("hyrox-go");
    var outEl = document.getElementById("hyrox-out");
    if (!goalEl || !statEl || !goEl || !outEl) return;

    function render() {
      var goal = parseClock(goalEl.value);
      var stations = parseFloat(statEl.value);
      if (!goal) { outEl.textContent = "Enter your goal finish time, like 1:30:00."; return; }
      if (isNaN(stations) || stations <= 0) { outEl.textContent = "Set how many minutes you expect to spend in the eight stations."; return; }
      var stationSeconds = stations * 60;
      var p = plan(goal, stationSeconds);
      if (!p) { outEl.textContent = "The station budget must be less than the goal time."; return; }
      var html = "<b>Run pace: " + formatPace(p.perKm) + "</b> for each of the 8 km " +
        "(running total " + formatClock(p.runTotal) + "). Stations average " +
        formatClock(p.perStation) + " each at your " + stations + "-minute budget.";
      html += "<table class='calc-table'><thead><tr><th>#</th><th>Station</th><th>Clock after the run</th><th>Clock after the station</th></tr></thead><tbody>";
      p.rows.forEach(function (r) {
        html += "<tr><td>" + r.leg + "</td><td>" + r.station + " <small>(" + r.detail + ")</small></td><td>" +
          formatClock(r.afterRun) + "</td><td>" + formatClock(r.afterStation) + "</td></tr>";
      });
      html += "</tbody></table>";
      html += "<p class='calc-note'>Even splits assume you hold one pace and one station rhythm. Most first-timers go out too fast on runs 1-2 - if that is you, add 10-15 seconds per km here and bank it early.</p>";
      outEl.innerHTML = html;
    }

    goEl.addEventListener("click", render);
    [goalEl, statEl].forEach(function (el) {
      el.addEventListener("keydown", function (e) { if (e.key === "Enter") render(); });
    });
  }

  if (typeof document !== "undefined") {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", wire);
    } else {
      wire();
    }
  }
})();
