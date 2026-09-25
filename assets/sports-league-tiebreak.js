/* BRYME Sport - league tiebreak calculator (CSP-safe, no storage).
   Applies the Premier League tiebreak order step by step. Pure core
   exported for testing; DOM wiring is browser-only. */
(function () {
  "use strict";

  /* Premier League order for teams level on points:
     goal difference -> goals scored -> head-to-head points ->
     head-to-head goal difference -> head-to-head away goals -> play-off.
     Each team: {points, gd, gf, h2hPoints, h2hGd, h2hAway}.
     Returns {steps: [{rule, a, b, result}], winner: "a"|"b"|"level"}. */
  function tiebreak(a, b) {
    var steps = [];
    function cmp(rule, av, bv) {
      var r = av === bv ? "level" : (av > bv ? "a" : "b");
      steps.push({ rule: rule, a: av, b: bv, result: r });
      return r;
    }
    var r = cmp("Points", a.points, b.points);
    if (r === "level") r = cmp("Goal difference", a.gd, b.gd);
    if (r === "level") r = cmp("Goals scored", a.gf, b.gf);
    if (r === "level") r = cmp("Head-to-head points", a.h2hPoints, b.h2hPoints);
    if (r === "level") r = cmp("Head-to-head goal difference", a.h2hGd, b.h2hGd);
    if (r === "level") r = cmp("Head-to-head away goals", a.h2hAway, b.h2hAway);
    return { steps: steps, winner: r };
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { tiebreak: tiebreak };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }
  var out = $("ltb-out"), warn = $("ltb-warn");
  if (!out) return;
  var fields = ["name", "pts", "gd", "gf", "hp", "hgd", "hag"];
  function read(t) {
    var o = {};
    fields.forEach(function (f) {
      var el = $("ltb-" + t + "-" + f);
      var v = parseFloat(el && el.value);
      o[f] = (f === "name") ? ((el && el.value.trim()) || ("Team " + t.toUpperCase()))
                            : (isNaN(v) ? null : v);
    });
    return o;
  }

  function calc() {
    if (!out || !warn) return;
    warn.textContent = "";
    var A = read("a"), B = read("b");
    var need = ["pts", "gd", "gf", "hp", "hgd", "hag"];
    for (var i = 0; i < need.length; i++) {
      if (A[need[i]] === null || B[need[i]] === null) {
        out.textContent = "Fill in every number for both teams (head-to-head figures are the two league meetings between them) to see the tiebreak.";
        return;
      }
    }
    var res = tiebreak({
      points: A.pts, gd: A.gd, gf: A.gf,
      h2hPoints: A.hp, h2hGd: A.hgd, h2hAway: A.hag
    }, {
      points: B.pts, gd: B.gd, gf: B.gf,
      h2hPoints: B.hp, h2hGd: B.hgd, h2hAway: B.hag
    });
    var html = "<table><tr><th>Step</th><th>Rule</th><th>" + A.name + "</th><th>" + B.name + "</th><th>Result</th></tr>";
    res.steps.forEach(function (st, i) {
      html += "<tr><td>" + (i + 1) + "</td><td>" + st.rule + "</td><td>" + st.a + "</td><td>" + st.b + "</td><td>"
        + (st.result === "level" ? "level &rarr; next rule"
           : "<b>" + (st.result === "a" ? A.name : B.name) + " ahead</b>") + "</td></tr>";
    });
    html += "</table>";
    if (res.winner === "level") {
      html += "<b>Every rule is level &mdash; the table is decided by a play-off match at a neutral ground.</b>";
    } else {
      html += "<b>" + (res.winner === "a" ? A.name : B.name)
        + " finishes above " + (res.winner === "a" ? B.name : A.name) + "</b>, decided at the rule above.";
    }
    html += "<br><small>Premier League order. UEFA club competitions put head-to-head first; check your competition's handbook.</small>";
    out.innerHTML = html;
  }

  fields.forEach(function (f) {
    ["a", "b"].forEach(function (t) {
      var el = $("ltb-" + t + "-" + f);
      if (el) { el.addEventListener("input", calc); el.addEventListener("change", calc); }
    });
  });
  calc();
})();
