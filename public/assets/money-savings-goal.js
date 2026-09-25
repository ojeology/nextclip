/* BRYME Money - savings goal calculator (CSP-safe, no inline JS, no storage).
   Pure-maths core is exported for testing; DOM wiring is browser-only. */
(function () {
  "use strict";

  function monthsOf(years) { return Math.round(years * 12); }

  /* Future value with monthly compounding: P grows for n months, each
     monthly contribution C earns interest from the month it lands. */
  function futureValue(start, monthly, annualPct, years) {
    var i = annualPct / 100 / 12, n = monthsOf(years);
    if (i === 0) return start + monthly * n;
    var growth = Math.pow(1 + i, n);
    return start * growth + monthly * ((growth - 1) / i);
  }

  /* Goal mode: rearrange the same equation to solve for C. */
  function requiredMonthly(start, goal, annualPct, years) {
    var i = annualPct / 100 / 12, n = monthsOf(years);
    if (i === 0) return (goal - start) / n;
    var growth = Math.pow(1 + i, n);
    return (goal - start * growth) * i / (growth - 1);
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { futureValue: futureValue, requiredMonthly: requiredMonthly };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }
  var mode = $("msg-mode"), cur = $("msg-cur"), start = $("msg-start"),
      month = $("msg-month"), rate = $("msg-rate"), years = $("msg-years"),
      goal = $("msg-goal"), grow = $("msg-grow"), crow = $("msg-crow"),
      out = $("msg-out"), warn = $("msg-warn");
  if (!out) return;

  function num(el) {
    var v = parseFloat(el && el.value);
    return isNaN(v) ? null : v;
  }
  function fmt(n, sym, d) {
    return sym + n.toLocaleString(undefined, { maximumFractionDigits: d === undefined ? 2 : d });
  }

  function calc() {
    if (!warn || !out) return;
    warn.textContent = "";
    var isGoal = mode && mode.value === "goal";
    if (grow) grow.hidden = !isGoal;
    if (crow) crow.hidden = isGoal;
    var p = num(start), r = num(rate), y = num(years), sym = (cur && cur.value) || "";
    if (p === null || p < 0 || r === null || r < 0 || y === null || y <= 0 || y > 60) {
      out.textContent = "Enter a starting balance, an annual rate and years (up to 60) to see the projection.";
      return;
    }
    var i = r / 100 / 12, n = monthsOf(y);
    var growth = Math.pow(1 + i, n);
    if (!isGoal) {
      var c = num(month);
      if (c === null || c < 0) {
        out.textContent = "Add a monthly contribution (0 is fine) to see the projection.";
        return;
      }
      var fv = futureValue(p, c, r, y);
      var inTotal = p + c * n, interest = fv - inTotal;
      out.innerHTML = "Future value after " + y + " year" + (y === 1 ? "" : "s") + ": <b>" + fmt(fv, sym) + "</b><br>"
        + "What you put in: " + fmt(inTotal, sym) + " (start " + fmt(p, sym) + " + " + n + " \u00d7 " + fmt(c, sym) + ")<br>"
        + "Interest earned: <b>" + fmt(interest, sym) + "</b><br>"
        + "Working: i = " + r + "% \u00f7 12, n = " + n + " months, growth (1+i)^n = " + growth.toFixed(4)
        + "<br>FV = " + fmt(p, sym) + " \u00d7 " + growth.toFixed(4) + " + " + fmt(c, sym)
        + " \u00d7 [((1+i)^n \u2212 1) \u00f7 i]";
      if (interest > fv * 0.5) {
        warn.textContent = "Over half the result is projected interest \u2014 check the rate is realistic for a savings account, not an investment.";
      }
    } else {
      var g = num(goal);
      if (g === null || g <= 0) {
        out.textContent = "Enter the goal amount to solve for the monthly contribution.";
        return;
      }
      var need = requiredMonthly(p, g, r, y);
      if (need < 0) {
        out.innerHTML = "Your starting balance of " + fmt(p, sym) + " already grows past " + fmt(g, sym)
          + " in " + y + " years at " + r + "% \u2014 <b>no monthly contribution needed</b>.<br>"
          + "Working: " + fmt(p, sym) + " \u00d7 " + growth.toFixed(4) + " = " + fmt(p * growth, sym) + " \u2265 goal.";
        return;
      }
      out.innerHTML = "Monthly contribution needed: <b>" + fmt(need, sym) + "</b> for " + n + " months at "
        + r + "% a year.<br>"
        + "Total you would put in: " + fmt(p + need * n, sym) + " (start " + fmt(p, sym)
        + " + " + n + " \u00d7 " + fmt(need, sym) + ")<br>"
        + "Working: C = (goal \u2212 start \u00d7 (1+i)^n) \u00d7 i \u00f7 ((1+i)^n \u2212 1), with i = "
        + r + "% \u00f7 12 and (1+i)^n = " + growth.toFixed(4) + ".";
    }
  }

  [mode, cur, start, month, rate, years, goal].forEach(function (el) {
    if (el) { el.addEventListener("input", calc); el.addEventListener("change", calc); }
  });
  calc();
})();
