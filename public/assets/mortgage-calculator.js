/* BRYME Home — monthly mortgage calculator (batch 34, 12 Sep 2026).
   CSP-safe IIFE: no eval, no fetch, no storage; mounts at #mortgage-calc.
   Shows P&I plus optional tax/insurance/other for a full monthly picture.
   General guidance only — never financial advice. */
(function () {
  "use strict";
  var root = document.getElementById("mortgage-calc");
  if (!root) return;
  root.innerHTML =
    '<div class="mc-grid">' +
    '<div class="mc-fields">' +
    '<label>Home price <input id="mc-price" type="text" inputmode="decimal" value="350000"></label>' +
    '<label>Down payment (% of price) <input id="mc-down" type="text" inputmode="decimal" value="20"></label>' +
    '<label>Interest rate (% / year) <input id="mc-rate" type="text" inputmode="decimal" value="6.76"></label>' +
    '<label>Term <select id="mc-term"><option value="30" selected>30 years</option><option value="20">20 years</option><option value="15">15 years</option><option value="10">10 years</option></select></label>' +
    '<label>Property tax (per month, optional) <input id="mc-tax" type="text" inputmode="decimal" placeholder="0"></label>' +
    '<label>Home insurance (per month, optional) <input id="mc-ins" type="text" inputmode="decimal" placeholder="0"></label>' +
    '<label>PMI / HOA / other (per month, optional) <input id="mc-oth" type="text" inputmode="decimal" placeholder="0"></label>' +
    "</div>" +
    '<div class="mc-out" id="mc-out" aria-live="polite"></div>' +
    "</div>" +
    '<p class="mc-disc">General guidance, not financial advice \u2014 your lender\u2019s Loan Estimate and your policy/tax bills govern. Rates change; the prefilled 6.76% was the Freddie Mac 30-year weekly average on 10 Sep 2026.</p>';

  function num(id) {
    var v = parseFloat(String(document.getElementById(id).value).replace(/[^0-9.\-]/g, ""), 10);
    return isFinite(v) ? v : 0;
  }
  function money(v) { return "$" + Math.round(v).toLocaleString("en-US"); }

  function calc() {
    var price = num("mc-price"), downPct = num("mc-down"), rate = num("mc-rate"),
        years = parseInt(document.getElementById("mc-term").value, 10),
        tax = num("mc-tax"), ins = num("mc-ins"), oth = num("mc-oth");
    var out = document.getElementById("mc-out");
    var loan = Math.max(price * (1 - Math.min(Math.max(downPct, 0), 100) / 100), 0);
    if (loan <= 0 || price <= 0) { out.innerHTML = "<p>Enter a home price and down payment to see the monthly math.</p>"; return; }
    var n = years * 12, r = rate / 100 / 12, m;
    if (r <= 0) { m = loan / n; } else { m = loan * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1); }
    var pi = m, totalInt = m * n - loan, monthly = m + tax + ins + oth;
    var rows = [
      ["Loan amount (" + (100 - Math.min(Math.max(downPct, 0), 100)).toFixed(0) + "% of price)", money(loan)],
      ["Principal &amp; interest", money(pi) + " / mo"],
      ["Tax + insurance + other", money(tax + ins + oth) + " / mo"],
      ["<b>Estimated monthly total</b>", "<b>" + money(monthly) + "</b>"],
      ["Total interest over " + years + " years", money(totalInt)],
      ["Total of all payments", money(m * n)]
    ];
    var h = "<table>";
    for (var i = 0; i < rows.length; i++) h += "<tr><td>" + rows[i][0] + "</td><td style=\"text-align:right;white-space:nowrap\">" + rows[i][1] + "</td></tr>";
    h += "</table>";
    if (downPct < 20 && downPct >= 0) h += "<p>Under 20% down, most US lenders add private mortgage insurance (PMI) \u2014 put an estimate in the \u201cother\u201d field to see it in the total.</p>";
    out.innerHTML = h;
  }
  root.addEventListener("input", calc);
  root.addEventListener("change", calc);
  calc();
})();
