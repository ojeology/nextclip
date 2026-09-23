/* BRYME video file size estimator — client-side only, CSP-safe (no inline JS). */
(function () {
  "use strict";
  var res = document.getElementById("tt-res");
  var fps = document.getElementById("tt-fps");
  var codec = document.getElementById("tt-codec");
  var audio = document.getElementById("tt-audio");
  var mins = document.getElementById("tt-min");
  var calc = document.getElementById("tt-calc");
  var out = document.getElementById("tt-out");
  var msg = document.getElementById("tt-msg");

  function go() {
    msg.textContent = "";
    out.textContent = "";
    var m = parseFloat(mins.value);
    if (!isFinite(m) || m <= 0 || m > 100000) {
      msg.textContent = "Enter the length in minutes (any positive number).";
      return;
    }
    var baseMbps = parseFloat(res.value.split("|")[0]);
    var resName = res.value.split("|")[1];
    var fpsMul = parseFloat(fps.value.split("|")[0]);
    var fpsName = fps.value.split("|")[1];
    var codecMul = parseFloat(codec.value.split("|")[0]);
    var codecName = codec.value.split("|")[1];
    var audMbps = parseFloat(audio.value.split("|")[0]);
    var audName = audio.value.split("|")[1];
    if (res.value === "custom") {
      msg.textContent = "Pick a resolution - the estimates are built from typical bitrates per resolution.";
      return;
    }
    var videoMbps = baseMbps * fpsMul * codecMul;
    var totalMbps = videoMbps + audMbps;
    var mbPerMin = totalMbps * 60 / 8;
    var totalMB = mbPerMin * m;
    var big = totalMB >= 1024 ? (totalMB / 1024).toFixed(2) + " GB" : Math.round(totalMB) + " MB";
    var lines = [
      resName + " at " + fpsName + ", " + codecName + (audName !== "no audio" ? ", " + audName : "") + ":",
      "",
      "Estimated file size for " + m + " min: " + big,
      "That is about " + Math.round(mbPerMin) + " MB per minute of video."
    ];
    lines.push("");
    lines.push("Real files land within roughly 20% of this either way - scene complexity, encoder settings and the platform's own processing all move it. Need the transfer time? The upload time calculator is the sibling tool.");
    out.textContent = lines.join("\n");
  }

  if (calc) { calc.addEventListener("click", go); }
})();
