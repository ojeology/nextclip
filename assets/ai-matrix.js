/* BRYME Tech — AI assistant comparison matrix (batch 48, 12 Sep 2026).
   CSP-safe IIFE; mounts at #ai-matrix-calc. Needs-based chooser over a dated
   market table (checked 12 Sep 2026 from three comparison guides — axis-intelligence,
   omidsaffari, toolradar). AI products change MONTHLY: every number here is a
   checked-date directional, not a contract. Full static matrix lives in the article. */
(function () {
  "use strict";
  var root = document.getElementById("ai-matrix-calc");
  if (!root) return;

  /* [name, paidFrom $/mo, tags, limit note] */
  var AI = [
    ["ChatGPT", 8, ["writing", "code", "images", "free"], "free tier (ad-supported in the US); Plus $20; caps reset every ~3h"],
    ["Claude", 17, ["writing", "docs", "code", "free"], "free tier with daily caps; Pro $20/mo ($17 annual); per-5-hour caps"],
    ["Gemini", 4.99, ["google", "images", "free", "cheap"], "free tier; AI Plus $4.99 (cheapest paid step); AI Pro $19.99 + 2TB storage"],
    ["Perplexity", 16.67, ["research", "free"], "free = 5 Pro searches/day; Pro $20/mo ($200/yr); sources shown inline"],
    ["Microsoft Copilot", 20, ["microsoft", "writing", "free"], "free in Windows/M365 chat; Copilot Pro $20; full power needs a qualifying M365 licence"],
    ["Mistral Le Chat", 14.99, ["eu", "writing", "free"], "free tier rate-limited; Pro $14.99; EU data residency"],
    ["Grok", 30, ["free"], "free on X (account-tied); Premium+ $30/mo"],
    ["DeepSeek", 0, ["free", "code"], "free chat with caps; paid is API-only"],
    ["Meta AI", 0, ["free"], "free inside Meta apps (account-tied); no paid tier"]
  ];

  var NEEDS = [
    ["writing", "Writing & documents"],
    ["code", "Coding help"],
    ["research", "Research with visible sources"],
    ["images", "Understand images I upload"],
    ["google", "I live in Google Workspace"],
    ["microsoft", "I live in Microsoft 365"],
    ["free", "Must have a real free tier"],
    ["eu", "EU data residency matters"],
    ["cheap", "Cheapest sensible paid step"]
  ];

  var h = '<p class="am-note">Tick what you need — the matrix ranks what fits. Checked 12 Sep 2026; AI products change monthly, so treat prices as directional.</p>';
  h += '<div class="am-needs">';
  for (var i = 0; i < NEEDS.length; i++) h += '<label class="am-chip"><input type="checkbox" value="' + NEEDS[i][0] + '"> ' + NEEDS[i][1] + "</label>";
  h += '</div><div id="am-out" aria-live="polite"></div>';
  h += '<p class="am-disc">General guidance, not a recommendation to buy — free tiers and caps change without notice. The full matrix table is in the article below; the <a href="/tech/free-ai-tools-worth-using/">free-tier deep dive</a> and the <a href="/tech/chatgpt-vs-claude-vs-gemini/">head-to-head comparison</a> cover the detail.</p>';
  root.innerHTML = h;

  function chosen() {
    var boxes = root.querySelectorAll(".am-chip input"), out = [];
    for (var i = 0; i < boxes.length; i++) if (boxes[i].checked) out.push(boxes[i].value);
    return out;
  }

  function calc() {
    var needs = chosen();
    var out = document.getElementById("am-out");
    if (!needs.length) {
      out.innerHTML = '<p class="am-note">Tick a need to rank the field — or read the full matrix table below.</p>';
      return;
    }
    var scored = [];
    for (var i = 0; i < AI.length; i++) {
      var hits = 0;
      for (var j = 0; j < needs.length; j++) if (AI[i][2].indexOf(needs[j]) > -1) hits++;
      scored.push([AI[i][0], hits, AI[i][1], AI[i][3], AI[i][2]]);
    }
    scored.sort(function (a, b) { return b[1] - a[1] || a[2] - b[2]; });
    var top = scored[0][1];
    if (top === 0) { out.innerHTML = '<p class="am-note">No assistant matches that combination as of the checked date — loosen one requirement.</p>'; return; }
    var rows = "", shown = 0;
    for (var k = 0; k < scored.length && shown < 3; k++) {
      if (scored[k][1] < top) break;
      rows += '<li><b>' + scored[k][0] + "</b> — from $" + scored[k][2] + '/mo <small>(' + scored[k][3] + ")</small></li>";
      shown++;
    }
    var missing = [];
    for (var n = 0; n < needs.length; n++) if (scored[0][4].indexOf(needs[n]) === -1) missing.push(needs[n]);
    var missTxt = "";
    for (var q = 0; q < missing.length; q++) {
      for (var w = 0; w < NEEDS.length; w++) if (NEEDS[w][0] === missing[q]) missTxt += (missTxt ? ", " : "") + NEEDS[w][1];
    }
    out.innerHTML = '<p class="am-note">Best matches for your <b>' + needs.length + "</b> need" + (needs.length > 1 ? "s" : "") + ":</p><ol>" + rows + "</ol>" +
      (missTxt ? '<p class="am-note">No single tool covers <b>' + missTxt + "</b> together yet — the leaders above miss that one; run two tools or drop it.</p>" : "") +
      '<p class="am-note">Prices are the cheapest credible paid step on the checked date. Caps, not features, are what you\u2019re buying.</p>';
  }

  root.addEventListener("change", calc);
})();
