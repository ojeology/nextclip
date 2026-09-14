/* BRYME home tools v1 - paint calculator + cleaning rota.
   Everything runs in this browser. No network calls:
   the numbers never leave the device. */
(function () {
  "use strict";
  function out(id) { return document.getElementById(id); }

  var fn = {
    paint: function () {
      var L = parseFloat((out("pc-l") || {}).value), W = parseFloat((out("pc-w") || {}).value),
          H = parseFloat((out("pc-h") || {}).value),
          doors = parseInt((out("pc-doors") || {}).value, 10) || 0,
          wins = parseInt((out("pc-windows") || {}).value, 10) || 0,
          coats = parseInt((out("pc-coats") || {}).value, 10) || 2;
      if (!(L > 0 && L <= 30) || !(W > 0 && W <= 30) || !(H >= 1.5 && H <= 6)) {
        return "Enter the room's length, width and wall height in metres (height 1.5-6 m).";
      }
      var gross = 2 * (L + W) * H;
      var net = gross - doors * 1.9 - wins * 1.4;
      if (net < 1) return "The doors and windows you entered cover the whole room - check the counts.";
      var litres = net / 10 * coats * 1.1; /* ~10 m2 per litre per coat, +10% for trays and drips */
      litres = Math.ceil(litres * 2) / 2;
      var left = litres, cans = [];
      [5, 2.5, 1].forEach(function (c) {
        while (left >= c - 0.01) { cans.push(c); left -= c; }
      });
      if (left > 0.01) cans.push(1); /* round the remainder up, never down */
      if (!cans.length) cans.push(1);
      var combo = {}, order = [];
      cans.forEach(function (c) { if (!combo[c]) { combo[c] = 0; order.push(c); } combo[c]++; });
      var label = order.map(function (c) { return combo[c] + " x " + c + "L"; }).join(" + ");
      return "Walls about <b>" + Math.round(net) + " m&sup2;</b>. For " + coats + " coat" + (coats > 1 ? "s" : "") +
        ": roughly <b>" + litres + " litres</b> - about " + label + ". Approximate: add a coat for dark-over-light or bare plaster; textured walls drink up to 20% more; the ceiling adds about " + Math.round(L * W) + " m&sup2; per coat.";
    },
    rota: function () {
      var size = (out("rota-size") || {}).value, days = parseInt((out("rota-days") || {}).value, 10) || 3;
      var zones = {
        studio: ["Kitchen (15 min)", "Bathroom (10 min)", "Main room (15 min)"],
        b1: ["Kitchen (15 min)", "Bathroom (10 min)", "Bedroom (10 min)", "Living room (15 min)"],
        b2: ["Kitchen (15 min)", "Bathroom (10 min)", "Bedroom 1 (10 min)", "Bedroom 2 (10 min)", "Living + hallway (15 min)"],
        family: ["Kitchen (20 min)", "Bathroom 1 (10 min)", "Bathroom 2 (10 min)", "Bedroom 1 (10 min)", "Bedroom 2 (10 min)", "Bedroom 3 (10 min)", "Living + hallway (15 min)"]
      }[size];
      if (!zones) return "Pick your home size, then build the week.";
      var names = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"];
      var plan = [], per = Math.ceil(zones.length / days), k = 0;
      for (var d = 0; d < days; d++) {
        var chunk = zones.slice(k, k + per); k += per;
        if (chunk.length) plan.push("<b>" + names[d] + ":</b> " + chunk.join(" + "));
      }
      var deep = [
        ['the washing machine', "/home/how-to-clean-a-washing-machine/"],
        ['the oven', "/home/how-to-deep-clean-an-oven/"],
        ['the mattress', "/home/how-to-clean-and-care-for-a-mattress/"],
        ['the fridge coils', "/home/fridge-coils-twice-a-year/"],
        ['the dryer lint path', "/home/dryer-lint-every-load/"]
      ];
      var week = Math.floor(Date.now() / (7 * 86400000)) % deep.length;
      return "<p>" + plan.join("</p><p>") + "</p><p><b>This week's deep task:</b> <a href=\"" + deep[week][1] + "\">" + deep[week][0] + "</a> - it rotates every week.</p>" +
        '<p class="wb-note">Miss a day? Fold that zone into the next one and move on. The schedule serves the home, not the other way round.</p>';
    }
  };

  document.addEventListener("click", function (e) {
    var b = e.target && e.target.closest ? e.target.closest(".calc-go") : null;
    if (!b) return;
    var kind = b.getAttribute("data-calc");
    var ids = { paint: "pc-out", rota: "rota-out" };
    var o = out(ids[kind]);
    if (!o || !fn[kind]) return;
    var v = fn[kind]();
    if (b.getAttribute("data-html") === "1") o.innerHTML = v; else o.textContent = v;
  }, false);
})();
