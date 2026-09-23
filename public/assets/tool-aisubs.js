/* BRYME AI subscription cost comparer — client-side only, CSP-safe (no inline JS). */
(function () {
  "use strict";
  var SERVICES = [
    ["tt-chatgpt", "tt-chatgpt-p", "ChatGPT Plus"],
    ["tt-claude", "tt-claude-p", "Claude Pro"],
    ["tt-gemini", "tt-gemini-p", "Google AI Pro"],
    ["tt-perplexity", "tt-perplexity-p", "Perplexity Pro"],
    ["tt-copilot", "tt-copilot-p", "Microsoft Copilot Pro"],
    ["tt-grok", "tt-grok-p", "SuperGrok"],
    ["tt-midjourney", "tt-midjourney-p", "Midjourney"],
    ["tt-custom", "tt-custom-p", "Your own row"]
  ];
  var months = document.getElementById("tt-months");
  var calc = document.getElementById("tt-calc");
  var out = document.getElementById("tt-out");
  var msg = document.getElementById("tt-msg");

  function money(v) { return "$" + v.toFixed(2); }

  function go() {
    msg.textContent = "";
    out.textContent = "";
    var m = parseFloat(months.value);
    if (!isFinite(m) || m < 1 || m > 12) {
      msg.textContent = "Months should be a number from 1 to 12.";
      return;
    }
    var rows = [];
    var totalMo = 0;
    var missing = [];
    SERVICES.forEach(function (s) {
      var box = document.getElementById(s[0]);
      var priceEl = document.getElementById(s[1]);
      if (!box || !box.checked) return;
      var p = parseFloat(priceEl.value);
      if (!isFinite(p) || p < 0) { missing.push(s[2]); return; }
      rows.push([s[2], p]);
      totalMo += p;
    });
    if (missing.length) {
      msg.textContent = "Tick a service only if you use it - and give it a price (0 counts). Problem with: " + missing.join(", ");
      return;
    }
    if (!rows.length) {
      msg.textContent = "Tick at least one subscription you pay for.";
      return;
    }
    rows.sort(function (a, b) { return b[1] - a[1]; });
    var lines = ["Your stack, biggest first:", ""];
    rows.forEach(function (r) {
      lines.push(r[0] + ": " + money(r[1]) + "/mo  (" + money(r[1] * 12) + "/yr)");
    });
    lines.push("");
    lines.push("Total: " + money(totalMo) + " per month");
    lines.push("Per year: " + money(totalMo * 12));
    if (m < 12) {
      lines.push("If you only keep them " + Math.round(m) + " months: " + money(totalMo * m) + " a year");
    }
    lines.push("That is about " + money(totalMo / 30) + " per day, every day.");
    if (rows.length > 1) {
      lines.push("");
      lines.push("Biggest line: " + rows[0][0] + " at " + money(rows[0][1]) + "/mo. The classic move: cancel the second-most-similar tool for a month and see if you actually miss it.");
    }
    out.textContent = lines.join("\n");
  }

  if (calc) { calc.addEventListener("click", go); }
})();
