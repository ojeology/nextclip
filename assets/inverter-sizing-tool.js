/* BRYME Home & DIY — inverter & battery sizing calculator (2026-09-25).
   Sizes an inverter, battery bank and solar array from YOUR actual load,
   with every step of the working shown. Deterministic, on-device only —
   no storage, no network. General information; a real installation needs
   a real electrician and nameplate readings. */
(function () {
  "use strict";

  /* ---------- pure maths core (unit-tested; no DOM below this line) ---- */
  var STD_SIZES = [500, 800, 1000, 1500, 2000, 2500, 3500, 5000, 7500, 10000];

  function dailyWh(items) {
    var sum = 0;
    for (var i = 0; i < items.length; i++) {
      var it = items[i];
      sum += Math.max(0, it.watts) * Math.max(0, it.hours) * Math.max(0, it.qty);
    }
    return sum;
  }
  function peakWatts(items) {
    var sum = 0;
    for (var i = 0; i < items.length; i++) {
      sum += Math.max(0, items[i].watts) * Math.max(0, items[i].qty);
    }
    return sum;
  }
  function inverterVA(peak, surgeFactor) {
    var need = peak * (surgeFactor || 1.25);
    for (var i = 0; i < STD_SIZES.length; i++) if (STD_SIZES[i] >= need) return STD_SIZES[i];
    return Math.ceil(need / 1000) * 1000;
  }
  function batteryAh(whPerDay, systemV, dod, autonomyDays) {
    var usable = Math.max(1, systemV) * Math.min(0.95, Math.max(0.1, dod));
    return (whPerDay * Math.max(0.25, autonomyDays)) / usable;
  }
  function solarW(whPerDay, sunHours, sysEff) {
    return whPerDay / (Math.max(1, sunHours) * Math.min(0.95, Math.max(0.3, sysEff || 0.75)));
  }
  var CORE = { dailyWh: dailyWh, peakWatts: peakWatts, inverterVA: inverterVA,
               batteryAh: batteryAh, solarW: solarW, STD_SIZES: STD_SIZES };
  if (typeof module !== "undefined" && module.exports) module.exports = CORE;

  /* ---------- DOM glue -------------------------------------------------- */
  var PRESETS = [
    { name: "LED lights (4 bulbs)", watts: 10, hours: 5, qty: 4 },
    { name: "Ceiling fan", watts: 70, hours: 8, qty: 1 },
    { name: "TV + decoder", watts: 100, hours: 4, qty: 1 },
    { name: "Fridge (cycling average)", watts: 80, hours: 10, qty: 1 },
    { name: "Laptop charger", watts: 65, hours: 4, qty: 1 },
    { name: "Phone charging", watts: 15, hours: 3, qty: 2 },
    { name: "Router / modem", watts: 12, hours: 24, qty: 1 },
    { name: "Standing fan (high)", watts: 90, hours: 6, qty: 1 },
    { name: "Water pump (short duty)", watts: 750, hours: 0.5, qty: 1 }
  ];

  function mount() {
    var root = document.getElementById("inverter-sizing-calculator");
    if (!root) return;
    var rows = PRESETS.map(function (p, i) {
      return '<label class="iv-row"><input type="checkbox" data-i="' + i + '"' + (i < 5 ? " checked" : "") + ">" +
        "<span>" + p.name + "</span><small>" + p.watts + " W \u00d7 " + p.hours + " h" +
        (p.qty > 1 ? " \u00d7 " + p.qty : "") + "</small></label>";
    }).join("");
    root.innerHTML =
      '<div class="iv-card"><fieldset><legend>Your load — tick what actually runs</legend>' + rows +
      '<p class="iv-note">Add anything missing to the maths by adjusting: watts = the nameplate number, ' +
      "hours = how long it runs a day. A fridge cycles, so its average is far below its starting surge.</p>" +
      "</fieldset>" +
      '<div class="iv-flds">' +
      '<label>Battery voltage<select id="iv-v"><option>12</option><option>24</option><option selected>48</option></select></label>' +
      '<label>Battery type<select id="iv-dod"><option value="0.5">Lead-acid / tubular (50% usable)</option>' +
      '<option value="0.8" selected>Lithium LiFePO4 (80% usable)</option></select></label>' +
      '<label>Autonomy<select id="iv-days"><option value="0.5">Half a day</option>' +
      '<option value="1" selected>One full day</option><option value="2">Two days</option></select></label>' +
      '<label>Peak sun hours<select id="iv-sun"><option value="4">4 (cloudy / harmattan)</option>' +
      '<option value="5" selected>5 (typical Nigeria)</option><option value="6">6 (clear dry season)</option></select></label>' +
      "</div>" +
      '<div class="iv-out" id="iv-out" aria-live="polite"></div>' +
      '<p class="iv-privacy">Runs on your device; nothing is stored or sent. General information — ' +
      "verify nameplate watts and let a qualified electrician do the actual install.</p></div>";

    var $ = function (id) { return document.getElementById(id); };
    function selected() {
      var out = [];
      root.querySelectorAll("input[type=checkbox]").forEach(function (cb) {
        if (cb.checked) out.push(PRESETS[Number(cb.getAttribute("data-i"))]);
      });
      return out;
    }
    function run() {
      var items = selected();
      var wh = dailyWh(items);
      var peak = peakWatts(items);
      var va = inverterVA(peak, 1.25);
      var v = Number($("iv-v").value);
      var dod = Number($("iv-dod").value);
      var days = Number($("iv-days").value);
      var sun = Number($("iv-sun").value);
      var ah = batteryAh(wh, v, dod, days);
      var kwh = (ah * v) / 1000;
      var sw = solarW(wh, sun, 0.75);
      var lines = [];
      lines.push("Daily energy: " + items.map(function (i) { return i.watts + "\u00d7" + i.hours + "h" + (i.qty > 1 ? "\u00d7" + i.qty : ""); }).join(" + ") +
                 " = <b>" + Math.round(wh) + " Wh/day</b> (" + (wh / 1000).toFixed(2) + " kWh)");
      lines.push("Simultaneous peak (all ticked at once): <b>" + peak + " W</b>");
      lines.push("Inverter: peak \u00d7 1.25 surge margin = " + Math.round(peak * 1.25) +
                 " VA \u2192 next standard size <b>" + va + " VA</b>");
      lines.push("Battery: " + Math.round(wh) + " Wh \u00d7 " + days + " day" + (days === 1 ? "" : "s") + " \u00f7 (" + v +
                 " V \u00d7 " + Math.round(dod * 100) + "% usable) = <b>" + Math.ceil(ah) + " Ah</b> at " + v +
                 " V (\u2248 " + kwh.toFixed(2) + " kWh of bank)");
      lines.push("Solar to refill daily: " + Math.round(wh) + " Wh \u00f7 (" + sun +
                 " sun-hours \u00d7 0.75 system efficiency) = <b>" + Math.ceil(sw / 50) * 50 + " W</b> of panels");
      $("iv-out").innerHTML = "<h3>The working</h3><ul>" +
        lines.map(function (l) { return "<li>" + l + "</li>"; }).join("") + "</ul>";
    }
    root.addEventListener("change", run);
    run();
  }
  if (typeof document !== "undefined") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount);
    else mount();
  }
})();
