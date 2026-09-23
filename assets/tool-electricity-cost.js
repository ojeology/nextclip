/* BRYME electricity cost calculator — client-side only, CSP-safe (no inline JS). */
(function () {
  "use strict";
  var appliance = document.getElementById("tt-appliance");
  var watts = document.getElementById("tt-watts");
  var hours = document.getElementById("tt-hours");
  var region = document.getElementById("tt-region");
  var rate = document.getElementById("tt-rate");
  var calc = document.getElementById("tt-calc");
  var out = document.getElementById("tt-out");
  var msg = document.getElementById("tt-msg");
  var lastSym = "$";

  function fill() {
    if (region.value !== "custom") {
      var parts = region.value.split("|");
      rate.value = parts[0];
      lastSym = parts[1];
    } else {
      rate.value = "";
      rate.focus();
    }
  }

  function money(v) { return lastSym + v.toFixed(2); }

  function go() {
    msg.textContent = "";
    out.textContent = "";
    var w = appliance.value === "custom" ? parseFloat(watts.value) : parseFloat(appliance.value);
    var h = parseFloat(hours.value);
    var r = parseFloat(rate.value);
    if (!isFinite(w) || w <= 0) {
      msg.textContent = "Enter the appliance wattage - it is on the label or in the manual.";
      return;
    }
    if (!isFinite(h) || h <= 0 || h > 24) {
      msg.textContent = "Hours per day must be a number between 0 and 24.";
      return;
    }
    if (!isFinite(r) || r <= 0) {
      msg.textContent = "Enter your rate per kWh - copy it straight off your electricity bill.";
      return;
    }
    var kwhHour = w / 1000;
    var perHour = kwhHour * r;
    var perDay = perHour * h;
    var perMonth = perDay * 30.4;
    var perYear = perDay * 365;
    var kwhYear = kwhHour * h * 365;
    out.textContent =
      "Per hour: " + money(perHour) + "\n" +
      "Per day (" + h + " h): " + money(perDay) + "\n" +
      "Per month (30-day): " + money(perMonth) + "\n" +
      "Per year: " + money(perYear) + "\n\n" +
      "That is about " + Math.round(kwhYear).toLocaleString() + " kWh of electricity a year.";
  }

  if (calc && region) {
    region.addEventListener("change", fill);
    calc.addEventListener("click", go);
  }
})();
