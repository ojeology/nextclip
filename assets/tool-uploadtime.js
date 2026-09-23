/* BRYME upload time calculator — client-side only, CSP-safe (no inline JS). */
(function () {
  "use strict";
  var size = document.getElementById("tt-size");
  var unit = document.getElementById("tt-unit");
  var speed = document.getElementById("tt-speed");
  var calc = document.getElementById("tt-calc");
  var out = document.getElementById("tt-out");
  var msg = document.getElementById("tt-msg");

  function hms(s) {
    var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = Math.round(s % 60);
    if (h > 0) return h + " h " + m + " min";
    if (m > 0) return m + " min " + (sec > 0 ? sec + " s" : "");
    return sec + " seconds";
  }

  function go() {
    msg.textContent = "";
    out.textContent = "";
    var mb = parseFloat(size.value) * parseFloat(unit.value);
    var sp = parseFloat(speed.value);
    if (!isFinite(mb) || mb <= 0) {
      msg.textContent = "Enter the file size.";
      return;
    }
    if (!isFinite(sp) || sp <= 0) {
      msg.textContent = "Enter your upload speed in Mbps - from a speed test, not the plan's brochure.";
      return;
    }
    var seconds = mb * 8 / sp;
    var lines = [
      Math.round(mb) + " MB at " + sp + " Mbps upload:",
      "",
      "About " + hms(seconds) + " in ideal conditions.",
      "Plan for " + hms(seconds * 1.15) + " in the real world (overhead and dips).",
      "",
      "At this speed you move about " + (sp * 3600 / 8000).toFixed(1) + " GB per hour.",
      "Wi-Fi, an old router or a busy network can slow it further - a cable to the router is the cheapest speed boost there is."
    ];
    out.textContent = lines.join("\n");
  }

  if (calc) { calc.addEventListener("click", go); }
})();
