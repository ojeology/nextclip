/* BRYME fitness calculators - everything runs in this browser.
   No network calls, no storage: the numbers never leave the device. */
(function () {
  "use strict";
  function out(id) { return document.getElementById(id); }
  var fn = {
    bmi: function () {
      var h = parseFloat((out("bmi-h") || {}).value), w = parseFloat((out("bmi-w") || {}).value);
      if (!(h > 100 && h < 230 && w > 30 && w < 250)) return "Please enter a height (100-230 cm) and weight (30-250 kg).";
      var v = w / Math.pow(h / 100, 2);
      var band = v < 18.5 ? "below the usual healthy band"
        : v < 25 ? "inside the usual healthy band"
        : v < 30 ? "above the usual healthy band"
        : "well above the usual healthy band";
      return "BMI " + (Math.round(v * 10) / 10) + " - " + band + ". A rough screen, not a verdict.";
    },
    h2o: function () {
      var w = parseFloat((out("h2o-w") || {}).value);
      if (!(w > 30 && w < 250)) return "Please enter a weight (30-250 kg).";
      var lo = Math.round(w * 30) / 10, hi = Math.round(w * 35) / 10;
      return "About " + lo + "-" + hi + " litres of fluid a day - food covers part of it.";
    },
    pro: function () {
      var w = parseFloat((out("pro-w") || {}).value);
      if (!(w > 30 && w < 250)) return "Please enter a weight (30-250 kg).";
      return "About " + Math.round(w * 1.2) + "-" + Math.round(w * 2.0) + " g of protein a day if you train.";
    }
  };
  document.addEventListener("click", function (e) {
    var b = e.target && e.target.closest ? e.target.closest(".calc-go") : null;
    if (!b) return;
    var kind = b.getAttribute("data-calc");
    var o = out({ bmi: "bmi-out", h2o: "h2o-out", pro: "pro-out" }[kind]);
    if (o && fn[kind]) o.textContent = fn[kind]();
  }, false);
})();
