/* BRYME Fitness — the weekly planner.
   Same house pattern as the 30-day plan: everything stays in YOUR browser's
   local storage. No account, nothing sent anywhere. Resets each Monday. */
(function () {
  "use strict";
  var KEY = "bryme-weekly-planner-v1";
  var DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
  var KINDS = ["move", "strength", "wind"];

  function mondayOf(d) {
    var x = new Date(d.getFullYear(), d.getMonth(), d.getDate());
    var day = (x.getDay() + 6) % 7; // 0 = Monday
    x.setDate(x.getDate() - day);
    return x.getFullYear() + "-" + String(x.getMonth() + 1).padStart(2, "0") + "-" + String(x.getDate()).padStart(2, "0");
  }

  function load() {
    var now = new Date();
    var wk = mondayOf(now);
    try {
      var raw = localStorage.getItem(KEY);
      if (raw) {
        var st = JSON.parse(raw);
        if (st && st.week === wk && st.days) return st;
      }
    } catch (e) { /* private mode etc. */ }
    return { week: wk, days: {} };
  }

  function save(st) {
    try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) { /* ignore */ }
  }

  function init() {
    var grid = document.getElementById("wp-grid");
    var status = document.getElementById("wp-status");
    var reset = document.getElementById("wp-reset");
    if (!grid || !status) return;
    var st = load();
    var sharedNote = "";
    var mm = /[#&]p=([a-z:,]+)/.exec(window.location.hash || "");
    if (mm) {
      st = { week: st.week, days: {} };
      mm[1].split(",").forEach(function (seg) {
        var parts = seg.split(":");
        if (parts.length === 2 && DAYS.indexOf(parts[0]) !== -1) {
          st.days[parts[0]] = {};
          parts[1].split("").forEach(function (ch) {
            var kk = { m: "move", s: "strength", w: "wind" }[ch];
            if (kk) { st.days[parts[0]][kk] = 1; }
          });
        }
      });
      sharedNote = " Showing a shared week \u2014 edit any cell to make it yours.";
    }

    function summary() {
      var move = 0, strength = 0, wind = 0;
      DAYS.forEach(function (d) {
        var q = st.days[d] || {};
        move += q.move ? 1 : 0;
        strength += q.strength ? 1 : 0;
        wind += q.wind ? 1 : 0;
      });
      var parts = [];
      parts.push("<b>" + move + " of 7 days</b> with 30 minutes of movement" + (move >= 5 ? " — the 150-minute week is in reach." : " (aim for 5 — brisk walking counts)."));
      parts.push("<b>" + strength + " strength day" + (strength === 1 ? "" : "s") + "</b>" + (strength >= 2 ? " — the guideline, met." : " (the guideline is 2)."));
      parts.push("<b>" + wind + " on-time night" + (wind === 1 ? "" : "s") + "</b>" + (wind >= 5 ? " — the recovery habit is holding." : " (7+ hours starts with an on-time evening)."));
      var done = move >= 5 && strength >= 2 && wind >= 5;
      status.innerHTML = (done ? "<b>The honest week, complete.</b> " : "") + parts.join(" ") + sharedNote;
    }

    function paint(btn, on) {
      btn.setAttribute("aria-pressed", on ? "true" : "false");
      if (on) { btn.classList.add("on"); } else { btn.classList.remove("on"); }
    }

    Array.prototype.forEach.call(grid.querySelectorAll(".wp-chip"), function (btn) {
      var d = btn.getAttribute("data-day"), k = btn.getAttribute("data-kind");
      paint(btn, !!(st.days[d] && st.days[d][k]));
      btn.addEventListener("click", function () {
        st.days[d] = st.days[d] || {};
        st.days[d][k] = st.days[d][k] ? 0 : 1;
        paint(btn, !!st.days[d][k]);
        save(st);
        sharedNote = "";
        summary();
      });
    });

    if (reset) {
      reset.addEventListener("click", function () {
        st = { week: mondayOf(new Date()), days: {} };
        save(st);
        Array.prototype.forEach.call(grid.querySelectorAll(".wp-chip"), function (btn) {
          paint(btn, false);
        });
        summary();
      });
    }
    var shb = document.createElement("button");
    shb.type = "button";
    shb.textContent = "Copy shareable week";
    sh.style.cssText="display:inline-block;margin-top:10px;font:800 12px/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;background:none;border:1px solid var(--line-strong);color:var(--ink);padding:10px 14px;cursor:pointer";
    shb.addEventListener("click", function () {
      var segs = [];
      DAYS.forEach(function (d2) {
        var q = st.days[d2] || {};
        var s2 = "";
        if (q.move) { s2 += "m"; }
        if (q.strength) { s2 += "s"; }
        if (q.wind) { s2 += "w"; }
        if (s2) { segs.push(d2 + ":" + s2); }
      });
      var url = window.location.href.split("#")[0] + (segs.length ? "#p=" + segs.join(",") : "");
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url);
        shb.textContent = "Copied \u2713 the link carries your week, nothing else";
      } else { window.prompt("Copy this link", url); }
      window.setTimeout(function () { shb.textContent = "Copy shareable week"; }, 3500);
    });
    if (status.parentNode) { status.parentNode.insertBefore(shb, status.nextSibling); }
    summary();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
