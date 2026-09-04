/* BRYME Writing Hub — client-side writing tools (no account, no network). */
(function () {
  "use strict";
  var WAT = function (el) { return (el && el.value) || ""; };
  function fit(ta) {
    var lc = ta.value.split("\n").length;
    ta.style.height = "auto";
    ta.style.height = Math.min(Math.max(ta.scrollHeight, 140), 420) + "px";
  }
  function words(s) { var m = s.trim().match(/[A-Za-z\u00C0-\u024F\u2019']+(?:['\u2019][A-Za-z\u00C0-\u024F]+)*/g); return m ? m.length : 0; }
  function chars(s) { return s.length; }
  function charsNoSpace(s) { return s.replace(/\s/g, "").length; }
  function sentences(s) {
    var m = s.trim().match(/[^.!?]+[.!?]+/g);
    var n = m ? m.length : 0;
    return n || (s.trim().length ? 1 : 0);
  }
  function paragraphs(s) { return s.trim() ? s.split(/\n\s*\n/).filter(function (p) { return p.trim(); }).length : 0; }
  function readingTime(s) {
    var w = words(s);
    var min = Math.max(1, Math.round(w / 200));
    var sec = Math.max(1, Math.round((w / 200) * 60));
    var hh = Math.floor(sec / 3600), mm = Math.floor((sec % 3600) / 60), ss = sec % 60;
    var pad = function (n) { return String(n).padStart(2, "0"); };
    return hh > 0 ? (hh + "h " + mm + "m") : (mm + "m " + ss + "s (" + min + " min at 200 wpm)");
  }
  function density(s) {
    var m = s.toLowerCase().match(/[a-z\u00C0-\u024F]+/g) || [];
    var stop = new Set("the and of to in a is it that was for on are as be with his they at by this had not but from have or an he we she their which when what there one you her all its so how just were like out them has can about".split(" "));
    var map = {};
    m.forEach(function (w) { if (w.length > 2 && !stop.has(w)) map[w] = (map[w] || 0) + 1; });
    var top = Object.keys(map).map(function (w) { return { w: w, n: map[w] }; }).sort(function (a, b) { return b.n - a.n; }).slice(0, 12);
    var total = top.reduce(function (a, b) { return a + b.n; }, 0);
    return { top: top, total: total, words: m.length };
  }
  function caseConv(s, mode) {
    var words = s.split(/\s+/);
    var lower = function (x) { return x.toLowerCase(); };
    var upper = function (x) { return x.toUpperCase(); };
    var cap = function (x) { return x.charAt(0).toUpperCase() + x.slice(1).toLowerCase(); };
    var title = function (x) { return cap(x); };
    var sent = words.map(function (w, i) { return i === 0 ? cap(w) : (w === w.toUpperCase() && w.length > 1 ? lower(w) : lower(w)); }).map(function (w, i) { return i === 0 ? cap(w) : w; });
    switch (mode) {
      case "lower": return words.map(lower).join(" ");
      case "upper": return words.map(upper).join(" ");
      case "title": return words.map(title).join(" ");
      case "sentence": {
        var done = false, out = [];
        for (var i = 0; i < words.length; i++) {
          var w = words[i];
          if (!done && w.length) { out.push(cap(w)); done = true; }
          else out.push(w.toLowerCase());
        }
        return out.join(" ");
      }
      case "camel": {
        var res = "";
        words.forEach(function (w, i) { var c = lower(w).replace(/[^a-z0-9]/g, ""); res += i === 0 ? c : cap(c); });
        return res;
      }
    }
    return s;
  }
  function clean(s) {
    return s.replace(/\u00A0/g, " ").replace(/[ \t]+/g, " ").replace(/ *\n */g, "\n").replace(/\n{3,}/g, "\n\n").trim();
  }
  function removeExtraSpaces(s) { return s.replace(/[^\S\n]+/g, " ").replace(/\n{3,}/g, "\n\n").trim(); }
  function removeLines(s, blankOnly) {
    return s.split("\n").filter(function (l) { return blankOnly ? l.trim() !== "" : l.trim() !== ""; }).join("\n");
  }
  function sortLines(s, desc) {
    return s.split("\n").filter(function (l) { return l.trim(); }).sort(function (a, b) {
      return desc ? b.localeCompare(a) : a.localeCompare(b);
    }).join("\n");
  }
  function dedupe(s) {
    var seen = new Set(), out = [];
    s.split("\n").forEach(function (l) { var t = l.trim(); if (t && !seen.has(t)) { seen.add(t); out.push(l); } });
    return out.join("\n");
  }

  var tools = {
    "word-counter": function () {
      var input = q("ta"), out = q("out");
      function run() { var t = WAT(input); out.innerHTML = "<b>" + words(t) + "</b> words &middot; " + chars(t) + " characters"; fit(input); }
      bind(input, run); run();
    },
    "character-counter": function () {
      var input = q("ta"), out = q("out");
      function run() { out.innerHTML = "<b>" + chars(WAT(input)) + "</b> characters"; fit(input); }
      bind(input, run); run();
    },
    "character-counter-no-spaces": function () {
      var input = q("ta"), out = q("out");
      function run() { out.innerHTML = "<b>" + charsNoSpace(WAT(input)) + "</b> characters (no spaces)"; fit(input); }
      bind(input, run); run();
    },
    "sentence-counter": function () {
      var input = q("ta"), out = q("out");
      function run() { var t = WAT(input); out.innerHTML = "<b>" + sentences(t) + "</b> sentences &middot; " + paragraphs(t) + " paragraphs"; fit(input); }
      bind(input, run); run();
    },
    "paragraph-counter": function () {
      var input = q("ta"), out = q("out");
      function run() { var t = WAT(input); out.innerHTML = "<b>" + paragraphs(t) + "</b> paragraphs &middot; " + sentences(t) + " sentences"; fit(input); }
      bind(input, run); run();
    },
    "reading-time": function () {
      var input = q("ta"), out = q("out");
      function run() { var t = WAT(input); out.innerHTML = "<b>" + readingTime(t) + "</b> &middot; " + words(t) + " words"; fit(input); }
      bind(input, run); run();
    },
    "word-density": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var d = density(WAT(input));
        var rows = d.top.map(function (x) { return "<tr><td>" + x.w + "</td><td>" + x.n + "</td><td>" + Math.round((x.n / Math.max(d.words, 1)) * 100) + "%</td></tr>"; }).join("");
        out.innerHTML = (d.top.length ? "<table class='tool-table'><thead><tr><th>Word</th><th>Count</th><th>Share</th></tr></thead><tbody>" + rows + "</tbody></table>" : "<p>Type some text to see your most-used content words.</p>");
        fit(input);
      }
      bind(input, run); run();
    },
    "case-converter": function () {
      var input = q("ta"), out = q("out"), sel = q("mode");
      function run() { out.value = caseConv(WAT(input), sel.value || "title"); fit(input); }
      bind(input, run); bind(sel, run); run();
    },
    "text-cleaner": function () {
      var input = q("ta"), out = q("out");
      function run() { out.value = clean(WAT(input)); fit(input); }
      bind(input, run); run();
    },
    "remove-extra-spaces": function () {
      var input = q("ta"), out = q("out");
      function run() { out.value = removeExtraSpaces(WAT(input)); fit(input); }
      bind(input, run); run();
    },
    "line-break-cleaner": function () {
      var input = q("ta"), out = q("out");
      function run() { out.value = removeLines(WAT(input)); fit(input); }
      bind(input, run); run();
    },
    "text-sorter": function () {
      var input = q("ta"), out = q("out"), sel = q("dir");
      function run() { out.value = sortLines(WAT(input), (sel.value === "desc")); fit(input); }
      bind(input, run); bind(sel, run); run();
    },
    "duplicate-line-remover": function () {
      var input = q("ta"), out = q("out");
      function run() { out.value = dedupe(WAT(input)); fit(input); }
      bind(input, run); run();
    },
    "writing-timer": function () {
      var display = q("time"), startBtn = q("start"), resetBtn = q("reset"), setBtn = q("setgoal"), goal = q("goal");
      var sec = 0, iv = null, goalSec = 25 * 60;
      function render() { var h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60), s = sec % 60; var p = function (n) { return String(n).padStart(2, "0"); }; display.textContent = h ? (h + ":" + p(m) + ":" + p(s)) : (p(m) + ":" + p(s)); }
      function tick() { sec++; render(); }
      startBtn.onclick = function () { if (iv) { clearInterval(iv); iv = null; startBtn.textContent = "Start"; } else { iv = setInterval(tick, 1000); startBtn.textContent = "Pause"; } };
      resetBtn.onclick = function () { sec = 0; render(); if (iv) { clearInterval(iv); iv = null; startBtn.textContent = "Start"; } };
      setBtn.onclick = function () { goalSec = Math.max(1, parseInt(goal.value, 10) || 25) * 60; };
      render();
    },
    "article-outline-generator": function () {
      var title = q("t"), points = q("p"), out = q("out");
      var sections = ["Introduction", "Background", "Main point 1", "Main point 2", "Main point 3", "Counter-argument or nuance", "Conclusion"];
      function run() {
        var t = title.value.trim() || "Your article";
        var ps = points.value.split(/\n/).map(function (x) { return x.trim(); }).filter(Boolean);
        var parts = [];
        if (ps.length) {
          ps.forEach(function (p, i) { parts.push((i + 1) + ". <b>" + p.charAt(0).toUpperCase() + p.slice(1) + "</b> — support this with evidence or examples."); });
        } else {
          parts = sections;
        }
        out.innerHTML = "<div class='tool-result'><p class='tool-result-title'>Outline: " + t.charAt(0).toUpperCase() + t.slice(1) + "</p><ol>" + parts.map(function (x) { return "<li>" + x + "</li>"; }).join("") + "</ol></div>";
      }
      bind(title, run); bind(points, run); run();
    },
    "writing-checklist-generator": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var lines = WAT(input).split(/\n/).map(function (x) { return x.trim(); }).filter(Boolean);
        out.innerHTML = lines.length ? "<div class='tool-result'><label class='tool-check'><input type='checkbox'> " + lines.join("</label><label class='tool-check'><input type='checkbox'> ") + "</label></div>" : "<p>Enter checklist items, one per line.</p>";
        fit(input);
      }
      bind(input, run); run();
    }
  };

  function q(id) { return document.getElementById(id); }
  function bind(el, fn) { if (el) el.addEventListener("input", fn); }
  function boot(id) { if (id && tools[id]) tools[id](); }
  function glossaryBoot() {
    var i = q("gsearch"), d = q("glossary");
    if (!i || !d) return;
    var items = [].slice.call(d.querySelectorAll("dt"));
    i.addEventListener("input", function () {
      var query = i.value.toLowerCase();
      items.forEach(function (dt) {
        var txt = (dt.textContent + " " + dt.nextElementSibling.textContent).toLowerCase();
        var show = txt.indexOf(query) > -1;
        dt.style.display = dt.nextElementSibling.style.display = show ? "" : "none";
      });
    });
  }
  function searchBoot() {
    var i = q("q"), box = q("results");
    if (!i || !box) return;
    function show(val) {
      var query = (val || "").trim().toLowerCase();
      var items = (window.__INDEX || []).filter(function (x) {
        return !query || (x.t + " " + x.d + " " + x.s).toLowerCase().indexOf(query) > -1;
      });
      if (!items.length) {
        box.innerHTML = '<p class="muted">No matches for &ldquo;' + query + '&rdquo;. Try "intro", "essay", "comma", "email" or "outline".</p>';
        return;
      }
      box.innerHTML = items.slice(0, 30).map(function (x) {
        return '<a class="guide-card" href="' + x.u + '"><span class="card-num">' + x.s.toUpperCase() + '</span><h3>' + x.t + '</h3><p>' + x.d + '</p><span class="card-link">Open →</span></a>';
      }).join("");
    }
    i.addEventListener("input", function () { show(i.value); });
    var p = new URLSearchParams(location.search).get("q");
    if (p) i.value = p;
    show(i.value);
  }
  // Capture the including <script> tag; CSP-safe (no inline scripts).
  var SCRIPT = document.currentScript;
  window.HUB_TOOLS = { boot: boot };
  document.addEventListener("DOMContentLoaded", function () {
    var id = (SCRIPT && SCRIPT.getAttribute("data-hub-tool")) || window.__HUB_TOOL;
    boot(id);
    if (SCRIPT && SCRIPT.hasAttribute("data-hub-glossary")) glossaryBoot();
    if (SCRIPT && SCRIPT.hasAttribute("data-hub-search")) searchBoot();
  });
})();
