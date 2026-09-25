/* BRYME Sport — points race calculator (2026-09-25).
   Arithmetic, not prediction: projects a final points total from the table
   numbers you enter, shows every step of the working, and never invents a
   probability. Deterministic, on-device only — no storage, no network. */
(function () {
  "use strict";

  /* ---------- pure maths core (unit-tested; no DOM below this line) ---- */
  function project(points, played, total, ppg) {
    var remaining = Math.max(0, total - played);
    return { remaining: remaining, projected: points + remaining * ppg };
  }
  function needs(points, played, total, target) {
    var remaining = Math.max(0, total - played);
    var gap = Math.max(0, target - points);
    var wins = Math.floor(gap / 3);
    var draws = gap - wins * 3;           /* 0, 1 or 2 leftover points = draws */
    var requiredPPG = remaining > 0 ? gap / remaining : (gap > 0 ? Infinity : 0);
    return {
      gap: gap, wins: wins, draws: draws,
      gamesNeeded: wins + draws,
      feasible: wins + draws <= remaining,
      requiredPPG: requiredPPG
    };
  }
  function formPPG(form) {
    var s = String(form || "").toUpperCase().replace(/[^WD L]/g, "").replace(/\s/g, "");
    if (!s) return null;
    var pts = 0;
    for (var i = 0; i < s.length; i++) pts += s[i] === "W" ? 3 : s[i] === "D" ? 1 : 0;
    return pts / s.length;
  }
  var CORE = { project: project, needs: needs, formPPG: formPPG };
  if (typeof module !== "undefined" && module.exports) module.exports = CORE;

  /* ---------- DOM glue -------------------------------------------------- */
  function mount() {
    var root = document.getElementById("points-race-calculator");
    if (!root) return;
    var TARGETS = [["40", "40 pts — the old safety line"], ["60", "60 pts — European contention"],
                   ["85", "85 pts — title range in a 38-game season"], ["custom", "Custom target"]];
    var html =
      '<div class="pr-card">' +
      '<div class="pr-flds">' +
      '<label>Current points<input id="pr-points" type="number" min="0" max="200" value="29"></label>' +
      '<label>Games played<input id="pr-played" type="number" min="0" max="60" value="29"></label>' +
      '<label>Season length<input id="pr-total" type="number" min="1" max="60" value="38"></label>' +
      '<label>Last five results (W/D/L)<input id="pr-form" type="text" maxlength="8" value="WWDLW" spellcheck="false"></label>' +
      '<label>Target<select id="pr-target">' +
      TARGETS.map(function (t) { return '<option value="' + t[0] + '">' + t[1] + "</option>"; }).join("") +
      '</select></label>' +
      '<label id="pr-custom-row" hidden>Custom target<input id="pr-custom" type="number" min="1" max="200" value="50"></label>' +
      "</div>" +
      '<div class="pr-out" id="pr-out" aria-live="polite"></div>' +
      '<p class="pr-privacy">Arithmetic only — no prediction model, no odds, nothing stored or sent. ' +
      "The maths is shown in full so you can check every line.</p>" +
      "</div>";
    root.innerHTML = html;
    var $ = function (id) { return document.getElementById(id); };
    function run() {
      var points = Math.max(0, Number($("pr-points").value) || 0);
      var played = Math.max(0, Number($("pr-played").value) || 0);
      var total = Math.max(1, Number($("pr-total").value) || 38);
      var tgtSel = $("pr-target").value;
      $("pr-custom-row").hidden = tgtSel !== "custom";
      var target = tgtSel === "custom" ? Math.max(1, Number($("pr-custom").value) || 0) : Number(tgtSel);
      var ppg = formPPG($("pr-form").value);
      if (ppg === null) ppg = played > 0 ? points / played : 0;
      var p = project(points, played, total, ppg);
      var n = needs(points, played, total, target);
      var lines = [];
      lines.push("Remaining games: " + total + " \u2212 " + played + " = <b>" + p.remaining + "</b>");
      lines.push("Points per game (" + ($("pr-form").value.trim() ? "last five" : "season average") + "): <b>" + ppg.toFixed(2) + "</b>");
      lines.push("Projected final total: " + points + " + (" + p.remaining + " \u00d7 " + ppg.toFixed(2) + ") = <b>" + p.projected.toFixed(1) + "</b>");
      lines.push("Gap to " + target + ": " + target + " \u2212 " + points + " = <b>" + n.gap + "</b> point" + (n.gap === 1 ? "" : "s"));
      if (n.gap === 0) {
        lines.push("Target already reached — the maths says relax.");
      } else {
        lines.push("Minimum route: <b>" + n.wins + " win" + (n.wins === 1 ? "" : "s") + " and " + n.draws +
                   " draw" + (n.draws === 1 ? "" : "s") + "</b> (" + n.gamesNeeded + " game" + (n.gamesNeeded === 1 ? "" : "s") +
                   "), or " + n.requiredPPG.toFixed(2) + " points per game across the run-in.");
        lines.push(n.feasible
          ? "Feasible on paper: it fits inside the " + p.remaining + " games left."
          : "<span class='pr-warn'>Not reachable in the games left</span> — the run-in is shorter than the minimum route.");
      }
      $("pr-out").innerHTML = "<h3>The working</h3><ul>" + lines.map(function (l) { return "<li>" + l + "</li>"; }).join("") + "</ul>";
    }
    ["pr-points", "pr-played", "pr-total", "pr-form", "pr-target", "pr-custom"].forEach(function (id) {
      $(id).addEventListener("input", run);
      $(id).addEventListener("change", run);
    });
    run();
  }
  if (typeof document !== "undefined") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount);
    else mount();
  }
})();
