/* BRYME Sport - wage-to-revenue ratio checker (CSP-safe, no storage).
   Pure maths exported for testing; DOM wiring is browser-only.
   Context, not verdict: squad-cost definitions differ from wages alone. */
(function () {
  "use strict";

  /* Wage bill as a percentage of revenue. */
  function ratio(revenue, wages) {
    if (!(revenue > 0)) return null;
    return (wages / revenue) * 100;
  }

  /* Honest bands: headroom, the UEFA 70% squad-cost line zone, the PL
     proposed 85% shadow line zone, and beyond revenue. Bands are context
     markers, not compliance verdicts. */
  function band(pct) {
    if (pct === null) return { key: "invalid", label: "Enter a revenue figure first." };
    if (pct < 60) return { key: "headroom", label: "Under 60% — below the lines most regulators discuss." };
    if (pct < 80) return { key: "uefa", label: "60–79% — the zone around UEFA's 70% squad-cost target (which also counts amortised fees and agent costs)." };
    if (pct < 100) return { key: "pl", label: "80–99% — above the 85% the Premier League proposed as a shadow squad-cost line; little room for error." };
    return { key: "over", label: "100%+ — the wage bill alone exceeds revenue; survival depends on owner funding or player sales." };
  }

  /* What revenue would need to be to reach a target ratio (e.g. 70%). */
  function revenueForTarget(wages, targetPct) {
    if (!(targetPct > 0)) return null;
    return wages / (targetPct / 100);
  }

  if (typeof module !== "undefined" && module.exports) {
    module.exports = { ratio: ratio, band: band, revenueForTarget: revenueForTarget };
  }
  if (typeof document === "undefined") return;

  function $(id) { return document.getElementById(id); }

  function fmt(v) {
    if (v === null) return "—";
    if (v >= 1e9) return (v / 1e9).toFixed(2) + "bn";
    if (v >= 1e6) return (v / 1e6).toFixed(1) + "m";
    return Math.round(v).toLocaleString("en");
  }

  function run() {
    var out = $("wrr-out");
    if (!out) return;
    var rev = parseFloat($("wrr-rev").value);
    var wag = parseFloat($("wrr-wag").value);
    var cur = ($("wrr-cur").value) || "£";
    if (!(rev > 0) || !(wag >= 0)) {
      out.textContent = "Enter the annual revenue and the annual wage bill (same units, e.g. millions).";
      return;
    }
    if (wag > rev * 3) {
      out.textContent = "That wage bill looks implausible against the revenue — double-check the units (millions vs thousands).";
      return;
    }
    var p = ratio(rev, wag);
    var b = band(p);
    var need70 = revenueForTarget(wag, 70);
    var need85 = revenueForTarget(wag, 85);
    out.innerHTML = '<table><tbody>'
      + "<tr><th>Wage-to-revenue ratio</th><td><b>" + p.toFixed(1) + "%</b></td></tr>"
      + "<tr><th>Revenue needed for 70% (UEFA line, wages only)</th><td>" + cur + fmt(need70) + "</td></tr>"
      + "<tr><th>Revenue needed for 85% (PL proposed line)</th><td>" + cur + fmt(need85) + "</td></tr>"
      + "</tbody></table>"
      + "<p><b>" + b.label + "</b></p>"
      + "<p class=\"wrr-note\">Wages alone are narrower than the official squad-cost measures, which add amortised transfer fees and agent costs — so this ratio usually understates them. Context, not a verdict.</p>";
  }

  ["wrr-cur", "wrr-rev", "wrr-wag"].forEach(function (id) {
    var el = $(id);
    if (el) { el.addEventListener("input", run); el.addEventListener("change", run); }
  });
  run();
})();
