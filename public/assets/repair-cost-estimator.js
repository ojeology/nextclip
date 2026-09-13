/* BRYME Home — repair cost estimator (batch 42, 12 Sep 2026).
   CSP-safe IIFE: no eval, no fetch, no storage; mounts at #repair-cost-calc.
   Defaults are DIRECTIONAL 2026 US ranges compiled from industry cost guides
   (fixhomecosts/BLS analysis, joinbreasy plumbing guide, Angi) — every value is
   editable because your market and your quotes decide. General guidance only. */
(function () {
  "use strict";
  var root = document.getElementById("repair-cost-calc");
  if (!root) return;

  var ITEMS = [
    ["Drain clog", 125, 300],
    ["Toilet repair", 150, 400],
    ["Faucet / cartridge", 150, 350],
    ["Pipe leak (accessible)", 175, 500],
    ["Burst pipe", 500, 2000],
    ["Water heater repair", 230, 1000],
    ["Water heater replacement", 880, 1830],
    ["Electrical outlet / fixture", 150, 400],
    ["Roof leak repair", 400, 1500],
    ["HVAC service call", 150, 600],
    ["HVAC replacement", 5000, 12000],
    ["Drywall patch + paint", 200, 800]
  ];

  var h = '<p class="rc-note">Directional US ranges (2026 industry guides) — <b>edit any number</b> to your market, then tick what you need. A real written quote always beats an estimate.</p>';
  h += '<div class="rc-rows">';
  for (var i = 0; i < ITEMS.length; i++) {
    h += '<div class="rc-row"><label class="rc-tick"><input type="checkbox" data-i="' + i + '"> ' + ITEMS[i][0] + "</label>" +
      '<span class="rc-nums">$<input type="text" inputmode="decimal" class="rc-lo" data-i="' + i + '" value="' + ITEMS[i][1] + '"> – $<input type="text" inputmode="decimal" class="rc-hi" data-i="' + i + '" value="' + ITEMS[i][2] + '"></span>' +
      '<span class="rc-qty">× <input type="text" inputmode="decimal" class="rc-q" data-i="' + i + '" value="1"></span></div>';
  }
  h += "</div>";
  h += '<div class="rc-global"><label>Urgency <select id="rc-urgency"><option value="1" selected>Flexible / scheduled (×1)</option><option value="1.25">Urgent this week (×1.25)</option><option value="1.5">Emergency / same-day (×1.5)</option></select></label></div>';
  h += '<div id="rc-out" aria-live="polite"></div>';
  h += '<p class="rc-disc">General guidance, not a quote. DIY usually lands near 30–40% of these pro figures (parts + your time) — and only where the job is genuinely safe to self-do (gas, mains electrics, structural and roof work are always pro territory).</p>';
  root.innerHTML = h;

  function num(el) {
    var v = parseFloat(String(el.value).replace(/[^0-9.\-]/g, ""), 10);
    return isFinite(v) && v >= 0 ? v : 0;
  }
  function money(v) { return "$" + Math.round(v).toLocaleString("en-US"); }

  function calc() {
    var mult = parseFloat(document.getElementById("rc-urgency").value) || 1;
    var lo = 0, hi = 0, rows = [];
    var boxes = root.querySelectorAll(".rc-tick input");
    for (var i = 0; i < boxes.length; i++) {
      if (!boxes[i].checked) continue;
      var k = boxes[i].getAttribute("data-i");
      var rlo = num(root.querySelector('.rc-lo[data-i="' + k + '"]')) * num(root.querySelector('.rc-q[data-i="' + k + '"]')) * mult;
      var rhi = num(root.querySelector('.rc-hi[data-i="' + k + '"]')) * num(root.querySelector('.rc-q[data-i="' + k + '"]')) * mult;
      rows.push("<tr><td>" + ITEMS[k][0] + (mult > 1 ? ' <em>(urgency ×' + mult + ")</em>" : "") + "</td><td style=\"text-align:right;white-space:nowrap\">" + money(rlo) + " – " + money(rhi) + "</td></tr>");
      lo += rlo; hi += rhi;
    }
    var out = document.getElementById("rc-out");
    if (!rows.length) { out.innerHTML = "<p class=\"rc-note\">Tick the repairs above to build an estimate.</p>"; return; }
    var diyLo = lo * 0.3, diyHi = hi * 0.4;
    out.innerHTML = "<table>" + rows.join("") +
      '<tr><td><b>Estimated total (pro)</b></td><td style="text-align:right;white-space:nowrap"><b>' + money(lo) + " – " + money(hi) + "</b></td></tr>" +
      '<tr><td>If safely DIY (parts + time, ~30–40%)</td><td style="text-align:right;white-space:nowrap">' + money(diyLo) + " – " + money(diyHi) + "</td></tr></table>" +
      '<p class="rc-note">Get at least two written, itemised quotes before committing — the estimate above only sizes the hole in your budget (<a href="/home/emergency-repair-fund/">the emergency repair fund</a> absorbs it).</p>';
  }
  root.addEventListener("input", calc);
  root.addEventListener("change", calc);
})();
