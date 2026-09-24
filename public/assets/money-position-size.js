/* BRYME Money - position size calculator (CSP-safe, no inline JS, no storage). */
(function () {
  "use strict";
  function $(id) { return document.getElementById(id); }
  var mode = $("mc-mode"), pairRow = $("mc-pair-row"), pair = $("mc-pair"),
      balance = $("mc-balance"), risk = $("mc-risk"),
      entry = $("mc-entry"), stop = $("mc-stop"),
      out = $("mc-out"), warn = $("mc-warn");
  if (!mode || !out) return;

  function num(el) {
    var v = parseFloat(el && el.value);
    return (isNaN(v) || v < 0) ? null : v;
  }
  function fmt(n) {
    if (n >= 100) return n.toLocaleString(undefined, { maximumFractionDigits: 0 });
    if (n >= 1) return n.toLocaleString(undefined, { maximumFractionDigits: 2 });
    return n.toLocaleString(undefined, { maximumFractionDigits: 6 });
  }

  function calc() {
    if (!warn || !out) return;
    warn.textContent = "";
    var bal = num(balance), pct = num(risk), en = num(entry), st = num(stop);
    if (bal === null || bal <= 0 || pct === null || pct <= 0 || en === null || st === null || en === 0 || st === 0 || en === st) {
      out.textContent = "Fill in balance, risk %, entry and a different stop price to see the position size.";
      return;
    }
    var riskAmt = bal * pct / 100;
    var dist = Math.abs(en - st);
    var html;

    if (mode.value === "fx") {
      var opt = pair.options[pair.selectedIndex];
      var pipSize = parseFloat(opt.value);
      var pipSizeStr = String(opt.value);
      var dp = pipSizeStr.indexOf(".") === -1 ? 0 : pipSizeStr.length - pipSizeStr.indexOf(".") - 1;
      var stopPips = dist / pipSize;
      var pipValuePerLot = pipSize * 100000; /* quote currency per standard lot */
      var lots = riskAmt / (stopPips * pipValuePerLot);
      var units = lots * 100000;
      html = "Risk: <b>" + riskAmt.toLocaleString(undefined, { maximumFractionDigits: 2 }) + "</b> \u00b7 "
           + "Stop distance: <b>" + stopPips.toLocaleString(undefined, { maximumFractionDigits: 1 }) + " pips</b><br>"
           + "Position size: <b>" + lots.toFixed(2) + " lots</b> (" + fmt(units) + " units)<br>"
           + "<small>" + opt.getAttribute("data-name") + " \u00b7 1 pip = " + pipSizeStr
           + " \u00b7 pip value per standard lot: " + pipValuePerLot.toLocaleString(undefined, { maximumFractionDigits: dp })
           + " (quote currency)</small>";
      if (lots < 0.01) {
        warn.textContent = "Below 0.01 lots (the usual micro-lot minimum) \u2014 this risk fits a smaller account than this trade needs.";
      }
    } else {
      var u = riskAmt / dist;
      html = "Risk: <b>" + riskAmt.toLocaleString(undefined, { maximumFractionDigits: 2 }) + "</b> \u00b7 "
           + "Stop distance: <b>" + dist.toLocaleString(undefined, { maximumFractionDigits: 6 }) + "</b><br>"
           + "Position size: <b>" + fmt(u) + " units</b><br>"
           + "<small>Exposure \u2248 " + fmt(u * en) + " at entry</small>";
    }
    out.innerHTML = html;
    if (pct > 3) {
      warn.textContent = "Risking " + pct + "% per trade is aggressive \u2014 a normal losing streak becomes a deep drawdown fast. Most risk plans cap this at 1\u20132%.";
    }
  }

  var fields = [mode, pair, balance, risk, entry, stop];
  for (var i = 0; i < fields.length; i++) {
    if (fields[i]) {
      fields[i].addEventListener("input", calc);
      fields[i].addEventListener("change", calc);
    }
  }
  if (pairRow && mode) {
    pairRow.style.display = mode.value === "fx" ? "" : "none";
    mode.addEventListener("change", function () {
      pairRow.style.display = mode.value === "fx" ? "" : "none";
      calc();
    });
  }
})();
