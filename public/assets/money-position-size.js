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
    var raw = el && el.value;
    if (raw === null || raw === undefined || String(raw).trim() === "") return null;
    var v = Number(raw);
    return (!Number.isFinite(v) || v < 0) ? null : v;
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
    if (bal === null || bal <= 0 || pct === null || pct <= 0 || pct > 100 ||
        en === null || st === null || en === 0 || st === 0 || en === st) {
      out.textContent = "Enter a positive balance and prices, a different stop and a planned risk between 0 and 100%.";
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
      // Never display a two-decimal lot figure rounded UP above the planned
      // quote-currency loss. Product-specific minimums/steps still need checking.
      var roundedDown = Math.floor(lots * 100) / 100;
      var units = roundedDown * 100000;
      html = "Planned price loss (quote currency): <b>" + riskAmt.toLocaleString(undefined, { maximumFractionDigits: 2 }) + "</b> \u00b7 "
           + "Stop distance: <b>" + stopPips.toLocaleString(undefined, { maximumFractionDigits: 1 }) + " pips</b><br>"
           + (roundedDown > 0 ? "Size rounded DOWN to 0.01 lot: <b>" + roundedDown.toFixed(2) + " lots</b> (" + fmt(units) + " units)<br>"
                              : "Calculated size is below 0.01 lot; do not round it up to fit a broker minimum.<br>")
           + "<small>" + opt.getAttribute("data-name") + " \u00b7 1 pip = " + pipSizeStr
           + " \u00b7 pip value per standard lot: " + pipValuePerLot.toLocaleString(undefined, { maximumFractionDigits: dp })
           + " (quote currency). Assumes account balance in quote currency and a fill at the stop; "
           + "before fees, gaps and conversion.</small>";
      if (roundedDown < 0.01) {
        warn.textContent = "The theoretical size is below 0.01 lot. Check your product's minimum and do not round up above your plan.";
      }
    } else {
      var u = riskAmt / dist;
      html = "Planned price loss: <b>" + riskAmt.toLocaleString(undefined, { maximumFractionDigits: 2 }) + "</b> \u00b7 "
           + "Stop distance: <b>" + dist.toLocaleString(undefined, { maximumFractionDigits: 6 }) + "</b><br>"
           + "Theoretical size: <b>" + fmt(u) + " units</b><br>"
           + "<small>Exposure \u2248 " + fmt(u * en) + " at entry. Round DOWN to the allowed contract step; "
           + "verify contract multiplier and account currency. Before fees, gaps and slippage.</small>";
    }
    out.innerHTML = html;
    if (pct > 3) {
      warn.textContent += (warn.textContent ? " " : "") + "A planned loss of " + pct + "% per trade can create a rapid drawdown; no percentage limits actual gap or margin losses.";
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
