/* BRYME Sport - transfer amortisation calculator (CSP-safe, no storage).
   Accounting arithmetic only: fee / contract years, book value, profit on
   sale. Pure-maths core exported for testing; DOM wiring is browser-only. */
(function () {
  "use strict";

  /* Straight-line yearly charge: fee spread evenly over the contract. */
  function annualCharge(fee, years) { return fee / years; }

  /* Book value after n completed years (never below zero). */
  function bookValue(fee, years, afterYears) {
    var v = fee - annualCharge(fee, years) * afterYears;
    return v < 0 ? 0 : v;
  }

  /* Accounting profit/loss booked in the year of sale. */
  function profitOnSale(salePrice, fee, years, afterYears) {
    return salePrice - bookValue(fee, years, afterYears);
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = {
      annualCharge: annualCharge,
      bookValue: bookValue,
      profitOnSale: profitOnSale
    };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }
  var fee = $("tam-fee"), years = $("tam-years"), cur = $("tam-cur"),
      sale = $("tam-sale"), syear = $("tam-syear"),
      out = $("tam-out"), warn = $("tam-warn");
  if (!out) return;

  function num(el) {
    var v = parseFloat(el && el.value);
    return isNaN(v) ? null : v;
  }
  function fmt(n, sym) {
    var neg = n < 0;
    return (neg ? "\u2212" : "") + sym
      + Math.abs(Math.round(n * 100) / 100).toLocaleString(undefined, { maximumFractionDigits: 2 });
  }

  function calc() {
    if (!warn || !out) return;
    warn.textContent = "";
    var f = num(fee), y = Math.round(num(years) || 0), sym = (cur && cur.value) || "";
    if (f === null || f <= 0 || !y || y < 1 || y > 10) {
      out.textContent = "Enter a transfer fee and a contract length (1-10 years) to see the yearly charge.";
      return;
    }
    var annual = annualCharge(f, y);
    var html = "Yearly amortisation: <b>" + fmt(annual, sym) + "</b> per season"
      + " &nbsp;(= " + fmt(f, sym) + " \u00f7 " + y + " years)<br>";
    html += "<table><tr><th>Season</th><th>Charge</th><th>Book value after</th></tr>";
    for (var i = 1; i <= y; i++) {
      html += "<tr><td>Year " + i + "</td><td>" + fmt(annual, sym) + "</td><td>"
        + fmt(bookValue(f, y, i), sym) + "</td></tr>";
    }
    html += "</table>";
    var sp = num(sale), sy = num(syear);
    if (sp !== null && sp > 0) {
      if (sy === null || sy < 0 || sy > y) {
        warn.textContent = "Add the number of full years after which the sale happens (0-" + y + ").";
      } else {
        sy = Math.round(sy);
        var bv = bookValue(f, y, sy), p = profitOnSale(sp, f, y, sy);
        html += "Sale after " + sy + " full year" + (sy === 1 ? "" : "s") + " for " + fmt(sp, sym) + ":<br>"
          + "Book value at sale: " + fmt(f, sym) + " \u2212 (" + fmt(annual, sym) + " \u00d7 " + sy + ") = <b>"
          + fmt(bv, sym) + "</b><br>"
          + "Accounting " + (p >= 0 ? "profit" : "loss") + " on sale: " + fmt(sp, sym) + " \u2212 "
          + fmt(bv, sym) + " = <b>" + (p >= 0 ? "+" : "") + fmt(p, sym) + "</b>";
      }
    }
    out.innerHTML = html;
  }

  [fee, years, cur, sale, syear].forEach(function (el) {
    if (el) { el.addEventListener("input", calc); el.addEventListener("change", calc); }
  });
  calc();
})();
