/* BRYME atlas: pick a random currently-accepting opportunity. CSP-safe, ES5. */
(function () {
  "use strict";
  var btn = document.getElementById("atlas-surprise");
  var note = document.getElementById("atlas-note");
  var dataEl = document.getElementById("atlas-open");
  if (!btn || !dataEl) return;
  var open = [];
  try { open = JSON.parse(dataEl.textContent); } catch (e) {}
  btn.addEventListener("click", function () {
    if (!open.length) { if (note) note.textContent = "Nothing accepting right now \u2014 check the desk."; return; }
    var pick = open[Math.floor(Math.random() * open.length)];
    if (note) note.textContent = "Rolled: " + pick.p + ". Opening\u2026";
    setTimeout(function () { window.location.href = pick.u; }, 350);
  });
})();
