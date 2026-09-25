/* BRYME Money - credit card payoff calculator (CSP-safe, no storage).
   Monthly amortisation loop: interest first, then principal. Pure-maths
   core exported for testing; DOM wiring is browser-only. */
(function () {
  "use strict";

  var MAX_MONTHS = 1200; /* 100-year sanity cap */

  /* Simulate a fixed monthly payment until the balance clears.
     Returns {months, totalInterest, totalPaid, clears}. */
  function simulateFixed(balance, apr, payment) {
    var i = apr / 100 / 12, months = 0, interest = 0;
    if (balance <= 0) return { months: 0, totalInterest: 0, totalPaid: 0, clears: true };
    if (payment <= balance * i) {
      return { months: Infinity, totalInterest: Infinity, totalPaid: Infinity, clears: false };
    }
    var bal = balance;
    while (bal > 0.005 && months < MAX_MONTHS) {
      var mi = bal * i;
      var pay = Math.min(payment, bal + mi);
      bal = bal + mi - pay;
      interest += mi;
      months += 1;
    }
    return { months: months, totalInterest: interest,
             totalPaid: balance + interest, clears: bal <= 0.005 };
  }

  /* Simulate a percentage-of-balance minimum with a floor.
     Payment each month = max(balance * pct/100, floor). */
  function simulateMinimum(balance, apr, minPct, floor) {
    var i = apr / 100 / 12, months = 0, interest = 0;
    if (balance <= 0) return { months: 0, totalInterest: 0, totalPaid: 0, clears: true };
    var bal = balance;
    while (bal > 0.005 && months < MAX_MONTHS) {
      var mi = bal * i;
      var pay = Math.max(bal * minPct / 100, floor);
      pay = Math.min(pay, bal + mi);
      bal = bal + mi - pay;
      interest += mi;
      months += 1;
    }
    return { months: months, totalInterest: interest,
             totalPaid: balance + interest, clears: bal <= 0.005 };
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { simulateFixed: simulateFixed, simulateMinimum: simulateMinimum };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }
  var cur = $("mcp-cur"), bal = $("mcp-bal"), apr = $("mcp-apr"),
      fixed = $("mcp-fixed"), minpct = $("mcp-minpct"), minfloor = $("mcp-minfloor"),
      out = $("mcp-out"), warn = $("mcp-warn");
  if (!out) return;

  function num(el) {
    var v = parseFloat(el && el.value);
    return isNaN(v) ? null : v;
  }
  function fmt(n, sym) {
    if (!isFinite(n)) return "\u221e";
    return sym + Math.round(n).toLocaleString(undefined);
  }
  function dur(m) {
    if (!isFinite(m)) return "never (payment does not cover interest)";
    var y = Math.floor(m / 12), r = m % 12;
    return (y > 0 ? y + " year" + (y === 1 ? "" : "s") + " " : "") + r + " month" + (r === 1 ? "" : "s");
  }

  function calc() {
    if (!warn || !out) return;
    warn.textContent = "";
    var b = num(bal), a = num(apr), f = num(fixed),
        mp = num(minpct), mf = num(minfloor), sym = (cur && cur.value) || "";
    if (b === null || b <= 0 || a === null || a < 0 || a > 100) {
      out.textContent = "Enter your current balance and APR to compare payoff paths.";
      return;
    }
    var html = "";
    var fixedRun = null;
    if (f !== null && f > 0) {
      fixedRun = simulateFixed(b, a, f);
      html += "<b>Fixed payment of " + fmt(f, sym) + "/month</b><br>"
        + "Debt-free in: <b>" + dur(fixedRun.months) + "</b><br>"
        + "Total interest: <b>" + fmt(fixedRun.totalInterest, sym) + "</b>"
        + " &nbsp;\u00b7&nbsp; total paid: " + fmt(fixedRun.totalPaid, sym) + "<br>";
      if (!fixedRun.clears) {
        html += "<span class=\"warn\">This payment barely covers the interest \u2014 the balance never clears. Raise it.</span><br>";
      }
    }
    if (mp !== null && mp > 0) {
      var minRun = simulateMinimum(b, a, mp, mf === null ? 0 : mf);
      if (html) html += "<hr style=\"border:none;border-top:1px solid var(--line-strong);margin:12px 0\">";
      html += "<b>Minimum payment (" + mp + "% of balance" + (mf ? ", floor " + fmt(mf, sym) : "") + ")</b><br>"
        + "Debt-free in: <b>" + dur(minRun.months) + "</b><br>"
        + "Total interest: <b>" + fmt(minRun.totalInterest, sym) + "</b>"
        + " &nbsp;\u00b7&nbsp; total paid: " + fmt(minRun.totalPaid, sym);
      if (fixedRun && fixedRun.clears && minRun.clears) {
        html += "<br><br><b>The gap:</b> paying a fixed " + fmt(f, sym)
          + " instead saves <b>" + fmt(minRun.totalInterest - fixedRun.totalInterest, sym)
          + "</b> in interest and <b>" + (minRun.months - fixedRun.months) + " months</b>.<br>"
          + "Working: monthly interest = balance \u00d7 " + a + "% \u00f7 12; each payment pays "
          + "interest first, then principal. Real cards compound daily, so exact figures differ slightly.";
      }
    }
    if (!html) {
      out.textContent = "Add a fixed monthly payment and/or a minimum-payment percentage to see the comparison.";
      return;
    }
    out.innerHTML = html;
  }

  [cur, bal, apr, fixed, minpct, minfloor].forEach(function (el) {
    if (el) { el.addEventListener("input", calc); el.addEventListener("change", calc); }
  });
  calc();
})();
