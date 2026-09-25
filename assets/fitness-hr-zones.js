/* BRYME Fitness - heart-rate zone calculator (CSP-safe, no storage).
   Zone maths exported for testing; DOM wiring is browser-only. */
(function () {
  "use strict";

  /* Classic population estimate of maximum heart rate. */
  function maxHR(age) { return 220 - age; }

  /* Karvonen target for a given intensity fraction (0-1). */
  function karvonenTarget(resting, max, fraction) {
    return resting + (max - resting) * fraction;
  }

  /* Zone bands as intensity fractions [low, high). */
  var ZONES = [
    { name: "Zone 1 - very easy", low: 0.50, high: 0.60 },
    { name: "Zone 2 - easy / conversational", low: 0.60, high: 0.70 },
    { name: "Zone 3 - comfortably hard", low: 0.70, high: 0.80 },
    { name: "Zone 4 - hard", low: 0.80, high: 0.90 },
    { name: "Zone 5 - near maximum", low: 0.90, high: 1.00 }
  ];

  /* Full zone table for both methods. */
  function zoneTable(age, resting) {
    var max = maxHR(age);
    var rows = ZONES.map(function (z) {
      var row = {
        name: z.name,
        pctLow: Math.round(z.low * 100), pctHigh: Math.round(z.high * 100),
        simpleLow: Math.round(max * z.low), simpleHigh: Math.round(max * z.high)
      };
      if (resting !== null) {
        row.kLow = Math.round(karvonenTarget(resting, max, z.low));
        row.kHigh = Math.round(karvonenTarget(resting, max, z.high));
      }
      return row;
    });
    return { max: max, rows: rows };
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { maxHR: maxHR, karvonenTarget: karvonenTarget, zoneTable: zoneTable, ZONES: ZONES };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }
  var go = $("hr-go"), ageEl = $("hr-age"), restEl = $("hr-rest"), out = $("hr-out");
  if (!go || !out) return;

  function run() {
    var age = parseInt(ageEl && ageEl.value, 10);
    if (isNaN(age) || age < 10 || age > 100) {
      out.textContent = "Enter an age between 10 and 100.";
      return;
    }
    var restRaw = parseInt(restEl && restEl.value, 10);
    var rest = (!isNaN(restRaw) && restRaw >= 30 && restRaw <= 120) ? restRaw : null;
    if (rest !== null && rest >= maxHR(age)) {
      out.textContent = "Resting heart rate must be below the estimated maximum (" + maxHR(age) + " bpm).";
      return;
    }
    var t = zoneTable(age, rest);
    var html = "Estimated max heart rate: <b>" + t.max + " bpm</b> (220 \u2212 " + age + ")"
      + (rest !== null ? " &nbsp;\u00b7&nbsp; heart-rate reserve: " + t.max + " \u2212 " + rest + " = " + (t.max - rest) + " bpm" : "")
      + "<table><tr><th>Zone</th><th>%</th><th>220 \u2212 age (bpm)</th>"
      + (rest !== null ? "<th>Karvonen (bpm)</th>" : "") + "</tr>";
    t.rows.forEach(function (r) {
      html += "<tr><td>" + r.name + "</td><td>" + r.pctLow + "\u2013" + r.pctHigh + "%</td>"
        + "<td>" + r.simpleLow + "\u2013" + r.simpleHigh + "</td>"
        + (rest !== null ? "<td>" + r.kLow + "\u2013" + r.kHigh + "</td>" : "") + "</tr>";
    });
    html += "</table>Karvonen: target = resting + (max \u2212 resting) \u00d7 intensity."
      + " Zones are conventions, not physiology \u2014 the talk test beats the table when they disagree.";
    out.innerHTML = html;
  }
  go.addEventListener("click", run);
})();
