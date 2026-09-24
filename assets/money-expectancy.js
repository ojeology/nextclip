/* BRYME Money - expectancy calculator (CSP-safe, no inline JS, no storage). */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var win = $("mcx-win"), winr = $("mcx-winr"), losr = $("mcx-losr"),
      bal = $("mcx-bal"), risk = $("mcx-risk"),
      out = $("mcx-out"), warn = $("mcx-warn");
  if (!out) return;

  function num(el) {
    var v = parseFloat(el && el.value);
    return isNaN(v) ? null : v;
  }
  function fmt(n, d) {
    return n.toLocaleString(undefined, { maximumFractionDigits: d === undefined ? 2 : d });
  }

  function calc() {
    if (!warn || !out) return;
    warn.textContent = "";
    var p = num(win), w = num(winr), l = num(losr), b = num(bal), r = num(risk);
    if (p === null || p < 0 || p > 100 || w === null || w < 0 || l === null || l < 0 || (w === 0 && l === 0)) {
      out.textContent = "Enter a win rate (0-100) and winner/loser sizes in R to see expectancy.";
      return;
    }
    var pw = p / 100, pl = 1 - pw;
    var e = pw * w - pl * l;               /* expectancy per trade, in R */
    var be = (w + l) > 0 ? (l / (w + l)) * 100 : 0;  /* breakeven win rate % */
    var html = "Expectancy: <b>" + (e >= 0 ? "+" : "") + e.toFixed(3) + " R per trade</b><br>"
             + "Breakeven win rate at this R:R: <b>" + be.toFixed(1) + "%</b><br>"
             + "Per 100 trades: <b>" + (e >= 0 ? "+" : "") + fmt(e * 100, 1) + " R</b>";
    if (b !== null && b > 0 && r !== null && r > 0 && r <= 100) {
      var oneR = b * r / 100;
      html += "<br>1R = " + fmt(oneR) + " \u00b7 Expectancy \u2248 <b>"
           + (e >= 0 ? "+" : "") + fmt(e * oneR) + "</b> per trade \u00b7 "
           + (e >= 0 ? "+" : "") + fmt(e * oneR * 100) + " per 100 trades";
    }
    out.innerHTML = html;
    if (e < 0) {
      warn.textContent = "Negative expectancy: as specified, this system loses on average per trade. No sizing plan fixes a negative edge.";
    } else if (p > 0 && p < be) {
      warn.textContent = "Win rate is below breakeven for this reward ratio \u2014 check the numbers.";
    }
  }

  var fields = [win, winr, losr, bal, risk];
  for (var i = 0; i < fields.length; i++) {
    if (fields[i]) {
      fields[i].addEventListener("input", calc);
      fields[i].addEventListener("change", calc);
    }
  }
})();
