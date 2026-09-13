/* BRYME Home — seasonal focus panel for the Once-a-Season Checklist (batch 45).
   ES5, CSP-safe, localStorage only. Detects the visitor's current season
   (hemisphere toggle, remembered), shows that season's four focus tasks with
   their own saved progress (keyed by season + year), and links every task to
   an existing desk guide. Complements the 10-task once-a-season list below —
   it does not replace it. */
(function () {
  "use strict";
  var root = document.getElementById("seasonal-tool");
  if (!root) return;

  var SEASONS_N = ["Winter", "Spring", "Summer", "Autumn"]; // Dec=0
  var TASKS = {
    Winter: [
      ["Bleed any cold radiators", "/home/how-to-bleed-a-radiator/"],
      ["Pipe-freeze walkthrough before the cold snap", "/home/winter-home-preparation/"],
      ["Dryer lint trap + vent route", "/home/dryer-lint-every-load/"],
      ["Test smoke and CO alarms", "/home/test-alarms-monthly/"]
    ],
    Spring: [
      ["Deep-clean the washing machine", "/home/how-to-clean-a-washing-machine/"],
      ["Fridge coils, brushed and vacuumed", "/home/fridge-coils-twice-a-year/"],
      ["HVAC filter swapped", "/home/hvac-filter-change-habit/"],
      ["Condensation / damp walk-through", "/home/condensation-ventilation-that-works/"]
    ],
    Summer: [
      ["Fridge coping with the heat?", "/home/fridge-not-cold-enough/"],
      ["Washer door seal: mould check", "/home/washing-machine-mould-door-seal/"],
      ["Breaker tripping under AC load?", "/home/why-does-my-circuit-breaker-keep-tripping/"],
      ["Dishwasher habits, re-loaded", "/home/dishwasher-loading-mistakes/"]
    ],
    Autumn: [
      ["Freeze-proofing walkthrough, early", "/home/winter-home-preparation/"],
      ["Water heater once-over (flush + listen)", "/home/water-heater-explained/"],
      ["Thermostat strategy for the heating season", "/home/smart-thermostat-payback/"],
      ["Top up the emergency repair fund", "/home/emergency-repair-fund/"]
    ]
  };

  function get(k, d) { try { var v = window.localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } }
  function set(k, v) { try { window.localStorage.setItem(k, v); } catch (e) {} }

  var hemi = get("bryme-hemi", "N");
  var now = new Date();
  var m = now.getMonth(); // 0-11
  var idx = hemi === "N" ? Math.floor(((m + 1) % 12) / 3) : Math.floor(((m + 7) % 12) / 3);
  var season = SEASONS_N[idx];
  var next = SEASONS_N[(idx + 1) % 4];
  var skey = "bryme-season-" + now.getFullYear() + "-" + season + "-" + hemi;

  var saved = {};
  try { saved = JSON.parse(get(skey, "{}")) || {}; } catch (e) { saved = {}; }

  var h = '<div class="st-panel">';
  h += '<div class="st-head"><div><p class="st-kick">Your season right now</p>';
  h += '<p class="st-season">' + season + ' <span class="st-hemi"><button type="button" id="st-hemi" title="Switch hemisphere">' + (hemi === "N" ? "North" : "South") + ' \u21c4</button></span></p></div>';
  h += '<p class="st-count" id="st-count"></p></div>';
  h += '<ul class="st-tasks">';
  for (var i = 0; i < TASKS[season].length; i++) {
    var on = !!saved[i];
    h += '<li class="' + (on ? "st-on" : "") + '"><label><input type="checkbox" data-i="' + i + '"' + (on ? " checked" : "") + '> ' +
      '<span>' + TASKS[season][i][0] + ' <a href="' + TASKS[season][i][1] + '">the guide</a></span></label></li>';
  }
  h += '</ul>';
  h += '<p class="st-next">Next up: <b>' + next + '</b> \u2014 this panel rotates itself. The full once-a-season list below covers every home, every season.</p>';
  h += '</div>';
  root.innerHTML = h;

  var css = document.createElement("style");
  css.textContent =
    ".st-panel{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:18px 20px;max-width:720px;margin:0 auto}" +
    ".st-head{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}" +
    ".st-kick{letter-spacing:.14em;font-size:11px;text-transform:uppercase;color:var(--dim);margin:0 0 4px}" +
    ".st-season{font-family:var(--serif);font-size:30px;margin:0}" +
    ".st-hemi button{background:none;border:1px solid var(--line-strong);border-radius:999px;padding:2px 10px;font:inherit;font-size:12px;cursor:pointer;color:var(--dim)}" +
    ".st-count{font-size:14px;color:var(--accent);margin:0}" +
    ".st-tasks{list-style:none;padding:0;margin:14px 0 8px}" +
    ".st-tasks li{padding:7px 0;border-bottom:1px solid var(--line);font-size:15px}" +
    ".st-tasks li.st-on{opacity:.55}" +
    ".st-tasks label{display:flex;gap:10px;align-items:baseline}" +
    ".st-tasks a{margin-left:6px;font-size:13px}" +
    ".st-next{font-size:12.5px;color:var(--dim);margin:10px 0 0}";
  document.head.appendChild(css);

  function count() {
    var boxes = root.querySelectorAll("input[type=checkbox]"), n = 0;
    for (var i = 0; i < boxes.length; i++) if (boxes[i].checked) n++;
    return n;
  }
  function render() {
    var c = count(), boxes = root.querySelectorAll("input[type=checkbox]");
    document.getElementById("st-count").textContent = c + " of " + boxes.length + " done this " + season + (c === boxes.length ? " \u2014 season complete \u2713" : "");
    for (var i = 0; i < boxes.length; i++) boxes[i].parentNode.parentNode.className = boxes[i].checked ? "st-on" : "";
  }
  root.addEventListener("change", function (e) {
    if (e.target && e.target.matches("input[type=checkbox]")) {
      saved[e.target.getAttribute("data-i")] = e.target.checked ? 1 : 0;
      set(skey, JSON.stringify(saved));
      render();
    }
  });
  document.getElementById("st-hemi").addEventListener("click", function () {
    hemi = hemi === "N" ? "S" : "N";
    set("bryme-hemi", hemi);
    window.location.reload();
  });
  render();
})();
