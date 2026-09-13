/* BRYME Home — moving cost estimator (batch 44, 12 Sep 2026).
   CSP-safe IIFE; mounts at #moving-cost-calc. Defaults are DIRECTIONAL 2026 US
   figures (ConsumerAffairs, Coastal Moving Services, StorageScholars guides) —
   every number editable; three written quotes decide. General guidance only. */
(function () {
  "use strict";
  var root = document.getElementById("moving-cost-calc");
  if (!root) return;

  var SIZES = [
    ["Studio", 2, 3, 3000],
    ["1 bedroom", 2, 4, 5000],
    ["2 bedrooms", 3, 5, 7500],
    ["3 bedrooms", 4, 7, 10000],
    ["4+ bedrooms", 5, 9, 13000]
  ];

  var h = '<p class="mv-note">Directional US 2026 ranges — edit any number to your market and quotes.</p>';
  h += '<div class="mv-grid"><div class="mv-fields">';
  h += '<label>Home size <select id="mv-size">';
  for (var i = 0; i < SIZES.length; i++) h += '<option value="' + i + '"' + (i === 2 ? " selected" : "") + ">" + SIZES[i][0] + "</option>";
  h += '</select></label>';
  h += '<label>Distance (miles) <input id="mv-miles" type="text" inputmode="decimal" value="20"></label>';
  h += '<label>Local rate per mover per hour ($ — US 2026: $40\u2013$100) <input id="mv-rate" type="text" inputmode="decimal" value="50"></label>';
  h += '<label><input type="checkbox" id="mv-packing"> Packing service (+$350\u2013600)</label>';
  h += '<label><input type="checkbox" id="mv-stairs"> Stairs / no elevator (+$100\u2013300)</label>';
  h += '<label><input type="checkbox" id="mv-storage"> One month of storage (+$150\u2013400)</label>';
  h += '<label><input type="checkbox" id="mv-materials"> Boxes &amp; materials (+$100\u2013300)</label>';
  h += '</div><div class="mv-out" id="mv-out" aria-live="polite"></div></div>';
  h += '<p class="mv-disc">General guidance, not a quote. Long-distance pricing switches on automatically past 100 miles (weight + distance model). Get three written, itemised estimates \u2014 and never hire a mover who demands a big cash deposit before truck day.</p>';
  root.innerHTML = h;

  function num(id) {
    var v = parseFloat(String(document.getElementById(id).value).replace(/[^0-9.\-]/g, ""), 10);
    return isFinite(v) && v >= 0 ? v : 0;
  }
  function chk(id) { return document.getElementById(id).checked; }
  function money(v) { return "$" + Math.round(v).toLocaleString("en-US"); }

  function calc() {
    var s = SIZES[parseInt(document.getElementById("mv-size").value, 10)] || SIZES[2];
    var crew = s[1], hours = s[2], lbs = s[3];
    var miles = num("mv-miles"), rate = num("mv-rate") || 50;
    var exLo = 0, exHi = 0;
    if (chk("mv-packing")) { exLo += 350; exHi += 600; }
    if (chk("mv-stairs")) { exLo += 100; exHi += 300; }
    if (chk("mv-storage")) { exLo += 150; exHi += 400; }
    if (chk("mv-materials")) { exLo += 100; exHi += 300; }
    var local = miles < 100, rows = [], lo, hi, assum;
    if (local) {
      lo = crew * hours * rate * 0.85 + exLo;
      hi = crew * (hours + 2) * rate * 1.25 + exHi;
      assum = crew + " movers \u00d7 " + hours + "h (+up to 2h travel fee) \u00d7 $" + rate + "/mover-hr, " + miles + " miles";
    } else {
      lo = 1200 + miles * 0.9 + lbs * 0.12 + exLo;
      hi = 2800 + miles * 1.6 + lbs * 0.25 + exHi;
      assum = "weight-and-distance model: \u2248" + lbs.toLocaleString("en-US") + " lbs over " + miles.toLocaleString("en-US") + " miles";
    }
    var dlo = local ? 200 + miles * 0.3 : 1200 + miles * 0.35;
    var dhi = local ? 900 + miles * 0.3 : 2800 + miles * 0.35;
    rows.push(["<b>Hiring movers (pro)</b>", "<b>" + money(lo) + " \u2013 " + money(hi) + "</b>"]);
    rows.push(["Full DIY (truck + fuel" + (local ? " + supplies" : " + lodging") + ")", money(dlo) + " \u2013 " + money(dhi)]);
    rows.push(["What the range assumes", assum]);
    var h2 = "<table>";
    for (var i = 0; i < rows.length; i++) h2 += "<tr><td>" + rows[i][0] + "</td><td style=\"text-align:right;white-space:nowrap\">" + rows[i][1] + "</td></tr>";
    h2 += "</table><p class=\"mv-note\">Three written estimates beat any calculator \u2014 and a <a href=\"/home/emergency-repair-fund/\">repair-sized buffer</a> absorbs the surprise fee every move has.</p>";
    document.getElementById("mv-out").innerHTML = h2;
  }
  root.addEventListener("input", calc);
  root.addEventListener("change", calc);
  calc();
})();
