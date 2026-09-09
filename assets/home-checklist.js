/* BRYME Home: once-a-season checklist. ES5, CSP-safe, localStorage only. */
(function () {
  "use strict";
  var days = document.querySelectorAll(".fp-day");
  if (!days.length) return;
  var KEY = "bryme-home-seasonal";
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
        ? "Nothing ticked yet. Tick items as you do them \u2014 your browser will remember."
        : n + " of " + days.length + " checked this season." + (n === days.length ? " Season fully maintained \u2014 see you in three months." : " Keep going \u2014 the slow failures are the cheap ones to catch.");
    }
  }
  for (var i = 0; i < days.length; i++) {
    (function (d) {
      var key = d.getAttribute("data-item");
      if (saved[key]) d.classList.add("done");
      var btn = d.querySelector(".fp-done");
      if (!btn) return;
      btn.addEventListener("click", function () {
        d.classList.toggle("done");
        saved[key] = d.classList.contains("done") ? 1 : 0;
        try { window.localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {}
        render();
      });
    })(days[i]);
  }
  render();
})();
