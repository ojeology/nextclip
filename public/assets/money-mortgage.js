/* BRYME Money - mortgage payment calculator (CSP-safe, no storage).
   Standard amortisation maths; pure core exported for testing, DOM wiring
   is browser-only. Educational arithmetic, not lending advice. */
(function () {
  "use strict";

  var MAX_MONTHS = 1200; /* 100-year sanity cap */

  /* Standard fixed-rate monthly payment:
     M = P * i * (1+i)^n / ((1+i)^n - 1), with the 0% case handled plainly. */
  function monthlyPayment(principal, annualRatePct, years) {
    if (principal <= 0 || years <= 0) return 0;
    var i = annualRatePct / 100 / 12, n = Math.round(years * 12);
    if (i === 0) return principal / n;
    var f = Math.pow(1 + i, n);
    return principal * i * f / (f - 1);
  }

  /* First-month split of a payment into interest and principal. */
  function firstSplit(principal, annualRatePct, payment) {
    var mi = principal * annualRatePct / 100 / 12;
    return { interest: mi, principal: payment - mi };
  }

  /* Totals over the full term at the scheduled payment. */
  function termTotals(principal, annualRatePct, years) {
    var m = monthlyPayment(principal, annualRatePct, years);
    var n = Math.round(years * 12);
    return { monthly: m, totalPaid: m * n, totalInterest: m * n - principal };
  }

  /* Simulate an extra monthly payment until the balance clears.
     Returns {months, totalInterest, clears}. */
  function monthsWithExtra(principal, annualRatePct, payment, extra) {
    var i = annualRatePct / 100 / 12, months = 0, interest = 0;
    if (principal <= 0) return { months: 0, totalInterest: 0, clears: true };
    if (payment + extra <= principal * i) {
      return { months: Infinity, totalInterest: Infinity, clears: false };
    }
    var bal = principal;
    while (bal > 0.005 && months < MAX_MONTHS) {
      var mi = bal * i;
      var pay = Math.min(payment + extra, bal + mi);
      bal = bal + mi - pay;
      interest += mi;
      months += 1;
    }
    return { months: months, totalInterest: interest, clears: bal <= 0.005 };
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { monthlyPayment: monthlyPayment, firstSplit: firstSplit,
                       termTotals: termTotals, monthsWithExtra: monthsWithExtra };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }

  function fmt(v, cur) {
    if (!isFinite(v)) return "never clears at this payment";
    var s = v < 100 ? v.toFixed(2) : Math.round(v).toLocaleString("en");
    return (cur || "") + s;
  }

  function run() {
    var out = $("mpc-out"), warn = $("mpc-warn");
    if (!out) return;
    var P = parseFloat($("mpc-principal").value);
    var R = parseFloat($("mpc-rate").value);
    var Y = parseFloat($("mpc-years").value);
    var E = parseFloat($("mpc-extra").value) || 0;
    var cur = ($("mpc-cur").value) || "";
    warn.textContent = "";
    if (!(P > 0) || !(Y > 0) || !(R >= 0)) {
      out.textContent = "Fill in the loan amount, rate and term to see the maths.";
      return;
    }
    if (R > 40) {
      warn.textContent = "That annual rate is above anything a mainstream mortgage carries — double-check whether it is a monthly or annual figure.";
    }
    var t = termTotals(P, R, Y);
    var fs = firstSplit(P, R, t.monthly);
    var html = '<table class="tbl"><tbody>'
      + "<tr><th>Monthly payment (interest + principal)</th><td>" + fmt(t.monthly, cur) + "</td></tr>"
      + "<tr><th>Of the first payment: interest</th><td>" + fmt(fs.interest, cur) + "</td></tr>"
      + "<tr><th>Of the first payment: principal</th><td>" + fmt(fs.principal, cur) + "</td></tr>"
      + "<tr><th>Total paid over the term</th><td>" + fmt(t.totalPaid, cur) + "</td></tr>"
      + "<tr><th>Total interest over the term</th><td>" + fmt(t.totalInterest, cur) + "</td></tr>"
      + "</tbody></table>";
    if (E > 0) {
      var w = monthsWithExtra(P, R, t.monthly, E);
      if (w.clears) {
        var saved = t.totalInterest - w.totalInterest;
        var mSaved = Math.round(Y * 12) - w.months;
        html += '<p class="calc-note">Adding ' + fmt(E, cur) + " a month clears the loan in about <b>"
          + Math.round(w.months / 12 * 10) / 10 + " years</b> (" + mSaved
          + " months earlier) and saves roughly <b>" + fmt(saved, cur)
          + "</b> of interest. Early months buy the most because interest is charged on a bigger balance.</p>";
      } else {
        html += '<p class="calc-note">Even with the extra, that payment does not cover the interest — the balance would never shrink.</p>';
      }
    }
    out.innerHTML = html;
  }

  var ids = ["mpc-cur", "mpc-principal", "mpc-rate", "mpc-years", "mpc-extra"];
  ids.forEach(function (id) {
    var el = $(id);
    if (el) { el.addEventListener("input", run); el.addEventListener("change", run); }
  });
  run();
})();
