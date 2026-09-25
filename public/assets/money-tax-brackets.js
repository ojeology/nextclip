/* BRYME Money - marginal tax calculator (CSP-safe, no storage).
   Progressive-band arithmetic; pure core exported for testing, DOM wiring
   is browser-only. Educational maths on illustrative bands - not tax advice. */
(function () {
  "use strict";

  /* Illustrative default bands [lower, upper, ratePct]. Users edit these
     to their own country's bands; the arithmetic is the lesson. */
  var DEFAULT_BANDS = [
    [0, 15000, 0],
    [15000, 50000, 20],
    [50000, 90000, 30],
    [90000, Infinity, 40]
  ];

  /* Tax owed on income under progressive bands.
     Returns {tax, effectiveRate, marginalRate, perBand} or null on bad input. */
  function computeTax(income, bands) {
    if (!(income >= 0)) return null;
    if (!bands || !bands.length) return null;
    for (var i = 0; i < bands.length; i++) {
      var b = bands[i];
      if (!(b[1] > b[0]) || !(b[2] >= 0)) return null;
    }
    var tax = 0, marginal = bands[0][2], rows = [];
    for (var j = 0; j < bands.length; j++) {
      var lo = bands[j][0], hi = bands[j][1], rate = bands[j][2];
      if (income > lo) {
        var taxed = Math.min(income, hi) - lo;
        var t = taxed * rate / 100;
        tax += t;
        marginal = rate;
        rows.push({ lo: lo, hi: hi, rate: rate, taxed: taxed, tax: t });
      }
    }
    return {
      tax: tax,
      effectiveRate: income > 0 ? (tax / income) * 100 : 0,
      marginalRate: marginal,
      perBand: rows
    };
  }

  /* The rate the NEXT unit of income is taxed at. */
  function marginalRate(income, bands) {
    var r = computeTax(income + 0.01, bands);
    return r ? r.marginalRate : null;
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { computeTax: computeTax, marginalRate: marginalRate,
                       DEFAULT_BANDS: DEFAULT_BANDS };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }

  function fmt(v, cur) {
    if (!isFinite(v)) return "\u2014";
    return (cur || "") + (v >= 100 ? Math.round(v).toLocaleString("en") : v.toFixed(2));
  }

  function run() {
    var out = $("mtc-out");
    if (!out) return;
    var income = parseFloat($("mtc-income").value);
    var cur = ($("mtc-cur").value) || "";
    var raw = ($("mtc-bands").value) || "";
    var bands = [];
    var lines = raw.split("\n");
    for (var i = 0; i < lines.length; i++) {
      var parts = lines[i].split(/[,\t ]+/).filter(Boolean);
      if (!parts.length) continue;
      if (parts.length !== 3) {
        out.textContent = "Each band needs three numbers: lower, upper, rate% - e.g. 15000, 50000, 20";
        return;
      }
      var lo = parseFloat(parts[0]), hi = parseFloat(parts[1]), rate = parseFloat(parts[2]);
      if (hi <= 0 || String(hi).toLowerCase() === "inf") hi = Infinity;
      bands.push([lo, hi, rate]);
    }
    if (!bands.length) bands = DEFAULT_BANDS;
    var r = computeTax(income, bands);
    if (!r) {
      out.textContent = "Enter a yearly income (and check the band lines are three numbers each).";
      return;
    }
    var html = '<table><tbody><tr><th>Band</th><th>Taxed at</th><th>Tax</th></tr>';
    for (var j = 0; j < r.perBand.length; j++) {
      var b = r.perBand[j];
      html += "<tr><td>" + fmt(b.lo, cur) + " \u2013 " + (isFinite(b.hi) ? fmt(b.hi, cur) : "\u2191")
            + "</td><td>" + b.rate + "% on " + fmt(b.taxed, cur) + "</td><td>" + fmt(b.tax, cur) + "</td></tr>";
    }
    html += "</tbody></table>"
      + "<p>Total tax: <b>" + fmt(r.tax, cur) + "</b> &middot; effective rate <b>"
      + r.effectiveRate.toFixed(1) + "%</b> &middot; marginal rate (next unit) <b>"
      + r.marginalRate + "%</b></p>"
      + '<p class="mtc-note">The default bands are illustrative, not any country\'s law - edit them to your own bands to see the shape of a progressive system. Not tax advice.</p>';
    out.innerHTML = html;
  }

  ["mtc-cur", "mtc-income", "mtc-bands"].forEach(function (id) {
    var el = $(id);
    if (el) { el.addEventListener("input", run); el.addEventListener("change", run); }
  });
  run();
})();
