/* BRYME Fitness: 30-day plan progress. ES5, CSP-safe, localStorage only. */
(function () {
  "use strict";
  var days = document.querySelectorAll(".fp-day");
  if (!days.length) return;
  var KEY = "bryme-fitness-walking-30";
  var fill = document.getElementById("fp-fill");
  var status = document.getElementById("fp-status");
  var saved = {};
  try { saved = JSON.parse(window.localStorage.getItem(KEY) || "{}") || {}; } catch (e) { saved = {}; }
  function count() {
    var n = 0;
    for (var i = 0; i < days.length; i++) {
      if (days[i].classList.contains("done")) n++;
    }
    return n;
  }
  function render() {
    var n = count();
    for (var i = 0; i < days.length; i++) {
      var d = days[i];
      var btn = d.querySelector(".fp-done");
      if (!btn) continue;
      var on = d.classList.contains("done");
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      btn.textContent = on ? "Done \u2713" : "Done";
    }
    if (fill) fill.style.width = Math.round((n / days.length) * 100) + "%";
    if (status) {
      status.textContent = n === 0
        ? "Day 0 of " + days.length + " complete. Tick days off as you go \u2014 your browser will remember."
        : "Day " + n + " of " + days.length + " complete." + (n === days.length ? " Finished the month \u2014 see you in week four, round two." : " Keep the rhythm.");
    }
  }
  for (var i = 0; i < days.length; i++) {
    (function (d) {
      var num = d.getAttribute("data-day");
      if (saved[num]) d.classList.add("done");
      var btn = d.querySelector(".fp-done");
      if (!btn) return;
      btn.addEventListener("click", function () {
        d.classList.toggle("done");
        saved[num] = d.classList.contains("done") ? 1 : 0;
        try { window.localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {}
        render();
      });
    })(days[i]);
  }
  render();
})();
