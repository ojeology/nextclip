/* BRYME Home — buy vs rent calculator (batch 35, 12 Sep 2026).
   CSP-safe IIFE: no eval, no fetch, no storage; mounts at #buy-vs-rent-calc.
   Monthly simulation: buying (P&I + tax + insurance + maintenance, equity recovered on sale)
   vs renting (rent inflating, differences invested at an assumed return).
   General guidance only — never financial advice. */
(function () {
  "use strict";
  var root = document.getElementById("buy-vs-rent-calc");
  if (!root) return;
  root.innerHTML =
    '<div class="bvr-grid">' +
    '<div class="bvr-fields">' +
    '<b>The home</b>' +
    '<label>Home price ($) <input id="bvr-price" type="text" inputmode="decimal" value="400000"></label>' +
    '<label>Down payment (%) <input id="bvr-down" type="text" inputmode="decimal" value="20"></label>' +
    '<label>Mortgage rate (% / year) <input id="bvr-rate" type="text" inputmode="decimal" value="6.76"></label>' +
    '<label>Property tax (% of price / year — set yours) <input id="bvr-tax" type="text" inputmode="decimal" value="1.0"></label>' +
    '<label>Maintenance (% of price / year, rule of thumb) <input id="bvr-maint" type="text" inputmode="decimal" value="1.0"></label>' +
    '<label>Home insurance ($ / month) <input id="bvr-ins" type="text" inputmode="decimal" value="150"></label>' +
    '<b>The renting side</b>' +
    '<label>Rent for a comparable place ($ / month) <input id="bvr-rent" type="text" inputmode="decimal" value="2000"></label>' +
    '<label>Rent inflation (% / year, assumption) <input id="bvr-rinf" type="text" inputmode="decimal" value="3"></label>' +
    '<b>The assumptions</b>' +
    '<label>Years you expect to stay <select id="bvr-years">' + (function () { var o = "", y; for (y = 1; y <= 30; y++) o += '<option value="' + y + '"' + (y === 7 ? " selected" : "") + '>' + y + " year" + (y > 1 ? "s" : "") + "</option>"; return o; })() + "</select></label>" +
    '<label>Home appreciation (% / year, assumption) <input id="bvr-app" type="text" inputmode="decimal" value="3"></label>' +
    '<label>Investment return if you invest the difference (% / year, assumption) <input id="bvr-inv" type="text" inputmode="decimal" value="6"></label>' +
    '<label>Buyer closing costs (% of price, often 2\u20135%) <input id="bvr-close" type="text" inputmode="decimal" value="3"></label>' +
    '<label>Selling costs when you leave (% of price, agent + fees) <input id="bvr-sell" type="text" inputmode="decimal" value="6"></label>' +
    "</div>" +
    '<div class="bvr-out" id="bvr-out" aria-live="polite"></div>' +
    "</div>" +
    '<p class="bvr-disc">General guidance, not financial advice \u2014 every assumption above is editable, and the verdict moves with it. Rate prefilled at the Freddie Mac 30-year weekly average of 10 Sep 2026 (6.76%).</p>';

  function num(id) {
    var v = parseFloat(String(document.getElementById(id).value).replace(/[^0-9.\-]/g, ""), 10);
    return isFinite(v) ? v : 0;
  }
  function money(v) { return "$" + Math.round(v).toLocaleString("en-US"); }

  function calc() {
    var price = num("bvr-price"), downPct = num("bvr-down"), rate = num("bvr-rate"),
        taxPct = num("bvr-tax"), maintPct = num("bvr-maint"), ins = num("bvr-ins"),
        rent0 = num("bvr-rent"), rinf = num("bvr-rinf"),
        years = parseInt(document.getElementById("bvr-years").value, 10),
        app = num("bvr-app"), inv = num("bvr-inv"),
        closePct = num("bvr-close"), sellPct = num("bvr-sell");
    var out = document.getElementById("bvr-out");
    if (price <= 0 || rent0 <= 0) { out.innerHTML = "<p>Enter a home price and a comparable rent to run the comparison.</p>"; return; }
    var loan = Math.max(price * (1 - Math.min(Math.max(downPct, 0), 100) / 100), 0);
    var n = 360, mr = rate / 100 / 12;
    var pi = (mr <= 0) ? loan / n : loan * mr * Math.pow(1 + mr, n) / (Math.pow(1 + mr, n) - 1);
    var monthlyOwn = pi + price * taxPct / 100 / 12 + price * maintPct / 100 / 12 + ins;
    var upfront = loan > 0 ? price * Math.min(Math.max(downPct, 0), 100) / 100 + price * Math.min(Math.max(closePct, 0), 100) / 100 : price * Math.min(Math.max(closePct, 0), 100) / 100;

    var bal = loan, val = price, port = upfront, months = 360, mo, rentM, diff;
    var sumRent = 0, sumOwn = upfront, mrate = app / 100 / 12, irate = inv / 100 / 12, rrate = rinf / 100 / 12;
    var beYear = null;
    var buyNetAt = [], rentNetAt = [];
    for (mo = 1; mo <= months; mo++) {
      rentM = rent0 * Math.pow(1 + rrate, mo);
      sumRent += rentM;
      sumOwn += monthlyOwn;
      diff = monthlyOwn - rentM;
      port = (port + diff) * (1 + irate);
      var i = bal * mr; bal -= (pi - i);
      val *= (1 + mrate);
      var buyNet = sumOwn - Math.max(val * (1 - Math.min(Math.max(sellPct, 0), 100) / 100) - Math.max(bal, 0), 0);
      var rentNet = sumRent - port;
      buyNetAt[mo] = buyNet; rentNetAt[mo] = rentNet;
      if (beYear === null && buyNet <= rentNet && mo <= 360) beYear = Math.ceil(mo / 12);
    }
    function f(m) { return money(buyNetAt[m]); }
    var buyNet = buyNetAt[months], rentNet = rentNetAt[months], gap = Math.abs(buyNet - rentNet);
    var verdict;
    var beNote = beYear === null ? " \u2014 no crossover within 30 years at these assumptions" : " \u2014 the crossover lands around year " + beYear;
    if (buyNet <= rentNet) verdict = "<b>Buying comes out ahead by " + money(gap) + "</b> after " + years + " years" + (beYear && beYear <= years ? " (crossover at about year " + beYear + ")" : "") + ".";
    else if (beYear !== null) verdict = "Renting is cheaper over your " + years + "-year horizon \u2014 " + money(gap) + " ahead \u2014 <b>but the crossover lands around year " + beYear + "</b>, so a longer stay flips the verdict. Stretch \u201cyears you\u2019ll stay\u201d and watch it.";
    else verdict = "<b>Renting comes out ahead by " + money(gap) + "</b> across all " + years + " years at these assumptions" + beNote + ".";
    var pr = price / (rent0 * 12), prBand = pr < 15 ? "below 15 \u2014 historically a buy-leaning zone" : (pr <= 20 ? "between 15 and 20 \u2014 the middle zone where rates and holding period decide" : "above 20 \u2014 historically a rent-leaning zone");
    var h = "<table>" +
      "<tr><td>Price-to-rent ratio</td><td style=\"text-align:right\"><b>" + pr.toFixed(1) + "</b> \u2014 " + prBand + "</td></tr>" +
      "<tr><td>Cash to close (down payment + closing costs)</td><td style=\"text-align:right\">" + money(upfront) + "</td></tr>" +
      "<tr><td>Owner\u2019s monthly (P&amp;I + tax + maintenance + insurance)</td><td style=\"text-align:right\">" + money(monthlyOwn) + "</td></tr>" +
      "<tr><td>Rent at start \u2192 at year " + years + "</td><td style=\"text-align:right\">" + money(rent0) + " \u2192 " + money(rent0 * Math.pow(1 + rrate, months)) + "</td></tr>" +
      "<tr><td>Net cost of buying after " + years + " yrs (equity recovered)</td><td style=\"text-align:right\"><b>" + f(months) + "</b></td></tr>" +
      "<tr><td>Net cost of renting after " + years + " yrs (difference invested)</td><td style=\"text-align:right\"><b>" + money(rentNet) + "</b></td></tr>" +
      "</table><p>" + verdict + "</p>";
    out.innerHTML = h;
  }
  root.addEventListener("input", calc);
  root.addEventListener("change", calc);
  calc();
})();
