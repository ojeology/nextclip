/* BRYME Tech — hosting true-cost calculator (batch 47, 12 Sep 2026).
   CSP-safe IIFE; mounts at #hosting-cost-calc. The trap it exposes: advertised
   prices are long-prepay intro rates that renew at 2–5×. Defaults are
   DIRECTIONAL 2026 figures (ahosting.net, bearhost Hostinger pricing tables,
   prestigetechnologies SMB guide) — every field editable; your cart decides. */
(function () {
  "use strict";
  var root = document.getElementById("hosting-cost-calc");
  if (!root) return;

  var PRESETS = {
    shared:  [2.99, 10.99],
    wordpress: [3.99, 16.99],
    vps: [6.49, 11.99],
    cloud: [7.99, 25.99],
    dedicated: [95, 129],
    custom: [0, 0]
  };

  var h = '<p class="hc-note">The homepage price is an intro rate on a long prepay; the renewal is the real price. Fill your plan (or start from a preset) and see the honest 3-year number.</p>';
  h += '<div class="hc-grid"><div class="hc-fields">';
  h += '<label>Plan type <select id="hc-preset">';
  for (var k in PRESETS) if (PRESETS.hasOwnProperty(k)) h += '<option value="' + k + '"' + (k === "shared" ? " selected" : "") + ">" + k + "</option>";
  h += '</select></label>';
  h += '<label>Intro price ($/mo) <input id="hc-intro" type="text" inputmode="decimal" value="2.99"></label>';
  h += '<label>Intro term <select id="hc-term"><option value="12">12 months</option><option value="24">24 months</option><option value="36">36 months</option><option value="48" selected>48 months</option></select></label>';
  h += '<label>Renewal price ($/mo) <input id="hc-renew" type="text" inputmode="decimal" value="10.99"></label>';
  h += '<label>Domain ($/yr) <input id="hc-domain" type="text" inputmode="decimal" value="14.99"></label>';
  h += '<label>Email mailboxes <input id="hc-mailn" type="text" inputmode="decimal" value="1"></label>';
  h += '<label>$ per mailbox/mo <input id="hc-mailp" type="text" inputmode="decimal" value="1.59"></label>';
  h += '<label>One-off (migration/setup $) <input id="hc-once" type="text" inputmode="decimal" value="0"></label>';
  h += '</div><div class="hc-out" id="hc-out" aria-live="polite"></div></div>';
  h += '<p class="hc-disc">General guidance, not a quote — taxes and promo exceptions vary. The multiplier that matters is renewal ÷ intro; everything else is arithmetic.</p>';
  root.innerHTML = h;

  function num(id) {
    var v = parseFloat(String(document.getElementById(id).value).replace(/[^0-9.\-]/g, ""), 10);
    return isFinite(v) && v >= 0 ? v : 0;
  }
  function money(v) { return "$" + Math.round(v).toLocaleString("en-US"); }

  function calc() {
    var intro = num("hc-intro"), term = num("hc-term"), renew = num("hc-renew");
    var domain = num("hc-domain"), mn = num("hc-mailn"), mp = num("hc-mailp"), once = num("hc-once");
    var out = document.getElementById("hc-out");
    if (intro <= 0 && renew <= 0) { out.innerHTML = '<p class="hc-note">Enter an intro or renewal price to start.</p>'; return; }
    var emailMo = mn * mp;
    function year(hostCost) { return hostCost + domain + emailMo * 12; }
    var y1 = year(intro * Math.min(term, 12)), y2 = year(renew * 12), y3 = year(renew * 12);
    var total3 = y1 + y2 + y3 + once;
    var mult = intro > 0 ? renew / intro : 0;
    var rows = [
      ["Year 1 (intro" + (term < 12 ? ", partial" : "") + ")", money(y1)],
      ["Year 2 (renewal)", money(y2)],
      ["Year 3 (renewal)", money(y3)],
      ["<b>True 3-year total</b>", "<b>" + money(total3) + "</b>"],
      ["True average per month", money(total3 / 36)],
      ["The trap: renewal ÷ intro", mult > 0 ? "<b>" + mult.toFixed(1) + "×</b> (the homepage showed $" + intro.toFixed(2) + "/mo; years 2+ cost $" + renew.toFixed(2) + "/mo)" : "—"]
    ];
    var t = "<table>";
    for (var i = 0; i < rows.length; i++) t += "<tr><td>" + rows[i][0] + "</td><td style=\"text-align:right;white-space:nowrap\">" + rows[i][1] + "</td></tr>";
    t += "</table>";
    if (mult >= 2) t += '<p class="hc-note">A ' + mult.toFixed(1) + '× renewal jump is typical — budget from the renewal column, not the homepage.</p>';
    t += '<p class="hc-note">Before you pay: hosting this very site costs $0/mo on a static host — match the plan to the site, not the marketing (<a href="/tech/free-vs-paid-hosting/">free vs paid, honestly</a>).</p>';
    out.innerHTML = t;
  }

  document.getElementById("hc-preset").addEventListener("change", function () {
    var p = PRESETS[this.value];
    if (p && p[0] > 0) {
      document.getElementById("hc-intro").value = p[0];
      document.getElementById("hc-renew").value = p[1];
    }
    calc();
  });
  root.addEventListener("input", calc);
  root.addEventListener("change", calc);
  calc();
})();
