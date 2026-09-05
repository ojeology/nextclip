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

  // --- style-analysis helpers ---
  var BE = /\b(?:am|is|are|was|were|been|being|be)\b/;
  var PAST = /\b(?:written|wrote|made|done|taken|given|seen|found|used|shown|known|brought|sent|held|read|created|produced|completed|approved|decided|handled|managed|run|won|lost|built|called|said|told|asked|salvaged|reported|sent|launched|raised|caught|considered|expected|released|included|informed|ordered|removed|replaced|resolved|revealed|reviewed|selected|served|shared|signed|started|stopped|tested|transferred|visited|won)\b/;
  function sentencesArr(s) {
    var m = s.trim().match(/[^.!?]+[.!?]+/g);
    return m ? m.map(function (x) { return x.trim(); }) : (s.trim() ? [s.trim()] : []);
  }
  function syllables(w) {
    w = w.toLowerCase().replace(/[^a-z]/g, "");
    if (!w) return 0;
    w = w.replace(/(?:[^laeiouy]es|ed|[^laeiouy]e)$/, "").replace(/^y/, "");
    var m = w.match(/[aeiouy]{1,2}/g);
    return Math.max(1, m ? m.length : 1);
  }
  function readability(txt) {
    var w = words(txt), s = Math.max(sentences(txt), 1), syl = 0;
    (txt.toLowerCase().match(/[a-z\u00C0-\u024F]+/g) || []).forEach(function (x) { syl += syllables(x); });
    if (!w) return { score: 0, grade: "—", words: 0 };
    var score = 206.835 - 1.015 * (w / s) - 84.6 * (syl / w);
    score = Math.max(0, Math.min(100, Math.round(score)));
    var grade = score >= 80 ? "Very easy — ages 11" : score >= 60 ? "Easy — ages 13" : score >= 40 ? "Fairly easy" : score >= 30 ? "Hard to read" : "Very hard to read";
    return { score: score, grade: grade, words: w, sentences: s };
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
    },
    "syllable-counter": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var t = WAT(input), tot = 0;
        (t.toLowerCase().match(/[a-z\u00C0-\u024F]+/g) || []).forEach(function (x) { tot += syllables(x); });
        out.innerHTML = "<b>" + tot + "</b> syllables &middot; <b>" + words(t) + "</b> words";
        fit(input);
      }
      bind(input, run); run();
    },
    "readability-score": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var r = readability(WAT(input));
        out.innerHTML = r.words ? "<div class='read-bar'><div class='read-fill' style='width:" + (r.score) + "%'></div><b class='read-num'>" + r.score + "/100</b></div><p><b>" + r.grade + "</b> &middot; Flesch reading ease &middot; " + r.words + " words in " + r.sentences + " sentences</p>" : "<p>Type something to see its readability score.</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "filler-word-finder": function () {
      var input = q("ta"), out = q("out");
      var fillers = { "very": "unnecessary intensifier", "really": "unnecessary intensifier", "just": "often filler", "quite": "unnecessary intensifier", "actually": "often filler", "basically": "often filler", "literally": "often filler", "totally": "unnecessary intensifier", "simply": "often filler", "extremely": "unnecessary intensifier", "very very": "redundant intensifier", "in order to": "wordy for 'to'", "due to the fact that": "wordy for 'because'", "at this point in time": "wordy for 'now'", "in the event that": "wordy for 'if'", "a large number of": "wordy for 'many'", "each and every": "redundant pair", "past history": "redundant pair", "basic fundamentals": "redundant pair" };
      function run() {
        var t = WAT(input).toLowerCase(), rows = [], total = 0;
        Object.keys(fillers).forEach(function (f) {
          var m = t.match(new RegExp("\\b" + f.replace(/ /g, "\\s+") + "\\b", "g"));
          if (m) { rows.push("<tr><td>" + f + "</td><td>" + m.length + "</td><td>" + fillers[f] + "</td></tr>"); total += m.length; }
        });
        out.innerHTML = "<p>" + (total ? "<b>" + total + "</b> filler/redundant phrase" + (total === 1 ? "" : "s") + " found:</p><table class='tool-table'><thead><tr><th>Phrase</th><th>Count</th><th>Why</th></tr></thead><tbody>" + rows.join("") + "</tbody></table>" : "No common filler or redundant phrases found — nice and tight.") + "</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "passive-voice-detector": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var found = [], ss = sentencesArr(WAT(input));
        ss.forEach(function (s) {
          var words = s.match(/\b[a-z\u00C0-\u024F]+\b/gi) || [];
          for (var i = 0; i < words.length; i++) {
            if (/^(?:am|is|are|was|were|been|being|be)$/i.test(words[i]) && words[i + 1] && (PAST.test(words[i + 1]) || /ed\b$/i.test(words[i + 1]))) {
              found.push(s); break;
            }
          }
        });
        out.innerHTML = found.length ? "<p><b>" + found.length + "</b> possible passive sentence" + (found.length === 1 ? "" : "s") + " — consider making the doer the subject:</p><ul class='tool-list'>" + found.slice(0, 12).map(function (s) { return "<li>" + s + "</li>"; }).join("") + "</ul>" : "<p>No obvious passive-voice sentences found — strong active writing.</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "word-repetition-checker": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var d = density(WAT(input));
        var repeated = d.top.filter(function (x) { return x.n >= 4; });
        var rows = repeated.map(function (x) { return "<tr><td>" + x.w + "</td><td>" + x.n + "</td></tr>"; }).join("");
        out.innerHTML = repeated.length ? "<p><b>" + repeated.length + "</b> word" + (repeated.length === 1 ? "" : "s") + " used 4+ times — check for overuse:</p><table class='tool-table'><thead><tr><th>Word</th><th>Times</th></tr></thead><tbody>" + rows + "</tbody></table>" : "<p>No content word appears 4+ times — good variety.</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "sentence-length-checker": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var ss = sentencesArr(WAT(input)), long = [];
        ss.forEach(function (s) {
          var w = words(s);
          if (w > 25) long.push({ s: s, w: w });
        });
        long.sort(function (a, b) { return b.w - a.w; });
        out.innerHTML = long.length ? "<p><b>" + long.length + "</b> sentence" + (long.length === 1 ? "" : "s") + " over 25 words — consider splitting:</p><ul class='tool-list'>" + long.slice(0, 8).map(function (x) { return "<li><b>" + x.w + "w:</b> " + x.s + "</li>"; }).join("") + "</ul>" : "<p>No sentence over 25 words — your sentences are varied and readable.</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "cliche-detector": function () {
      var input = q("ta"), out = q("out");
      var cliches = ["at the end of the day", "in this day and age", "think outside the box", "the elephant in the room", "at the touch of a button", "the tip of the iceberg", "in the nick of time", "last but not least", "a stone's throw away", "better late than never", "actions speak louder than words", "it goes without saying", "at the end of the day", "on the same page", "a win-win situation", "dive in head first", "take it to the next level", "move the needle", "game changer", "in the grand scheme of things", "with all due respect", "pull yourself up by your bootstraps", "a blessing in disguise", "due diligence", "low-hanging fruit"];
      function run() {
        var t = WAT(input).toLowerCase(), rows = [];
        cliches.forEach(function (c) {
          var m = t.match(new RegExp(c.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g"));
          if (m) rows.push("<tr><td>" + c + "</td><td>" + m.length + "</td></tr>");
        });
        out.innerHTML = rows.length ? "<p><b>" + rows.length + "</b> clich&eacute; found — replace with something specific and fresh:</p><table class='tool-table'><thead><tr><th>Clich&eacute;</th><th>Count</th></tr></thead><tbody>" + rows.join("") + "</tbody></table>" : "<p>No common clich&eacute;s found — your phrasing feels fresh.</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "adverb-finder": function () {
      var input = q("ta"), out = q("out");
      function run() {
        var t = WAT(input), m = t.match(/\b[a-z\u00C0-\u024F]+(?:ly)\b/gi) || [];
        var counts = {}, arr = [];
        m.forEach(function (w) { counts[w] = (counts[w] || 0) + 1; });
        Object.keys(counts).forEach(function (w) { arr.push({ w: w, n: counts[w] }); });
        arr.sort(function (a, b) { return b.n - a.n; });
        out.innerHTML = arr.length ? "<p><b>" + arr.length + "</b> -ly adverb" + (arr.length === 1 ? "" : "s") + " — replace weak ones with a stronger verb where you can:</p><ul class='tool-list'>" + arr.slice(0, 15).map(function (x) { return "<li>" + x.w + " × " + x.n + "</li>"; }).join("") + "</ul>" : "<p>No -ly adverbs found.</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "title-generator": function () {
      var topic = q("topic"), audience = q("audience"), out = q("out");
      var templates = [
        "{A}: the complete beginner's guide", "How to {A} (when you have no idea where to start)",
        "The only {A} guide you will ever need", "{A}, explained in plain English",
        "Why {A} matters more than you think", "{A}: 5 things I wish I knew sooner",
        "How {A} actually works — a practical walkthrough", "What nobody tells you about {A}",
        "A proven way to {A} without the guesswork", "{A} for people who are short on time",
        "The mistakes everyone makes with {A}", "How to master {A} step by step",
        "{A}: from beginning to confident", "An honest, no-fluff guide to {A}"
      ];
      function run() {
        var a = topic.value.trim().toLowerCase() || "your topic";
        var aud = audience.value.trim();
        var res = templates.map(function (t) {
          var s = t.replace(/\{A\}/g, a);
          if (aud) s = s.replace(".", " for " + aud.toLowerCase() + ".");
          return { title: s.charAt(0).toUpperCase() + s.slice(1) };
        });
        out.innerHTML = "<ul class='tool-list'>" + res.map(function (x) { return "<li>" + x.title + "</li>"; }).join("") + "</ul>";
      }
      bind(topic, run); bind(audience, run); run();
    },
    "meta-description-generator": function () {
      var topic = q("topic"), benefit = q("benefit"), out = q("out");
      function run() {
        var t = topic.value.trim() || "this guide";
        var b = benefit.value.trim() || "learn the essentials quickly";
        var base = "Learn " + t + " — " + b + ". Get practical, clear steps you can use today.";
        out.innerHTML = "<div class='tool-result'><p class='tool-result-title'>Meta description (" + base.length + "/160 chars)</p><p>" + base + "</p></div>";
      }
      bind(topic, run); bind(benefit, run); run();
    },
    "random-writing-prompt": function () {
      var out = q("out"), btn = q("new");
      var prompts = [
        "Write the scene from the point of view of someone who is afraid of telling the truth.",
        "Describe a room you spent a lot of time in, using only sensory detail and no adjectives like 'beautiful'.",
        "A character finds a letter addressed to them dated ten years in the future. What does it say?",
        "Write about a small lie that grew. Start with the lie, end with its cost.",
        "Describe your morning from the perspective of the first object you touched.",
        "A character is about to say the thing they have been avoiding for years. Write the moment just before.",
        "Write a short argument between two characters about something that is not really what they are arguing about.",
        "In 150 words, capture a memory you did not know you had until just now.",
        "Write a list of instructions for someone trying to get through a hard week.",
        "A character discovers the one object they buried. Write the moment of finding it.",
        "Write a paragraph in which 'dust' is the most important word.",
        "Two old friends meet after a decade. One line of dialogue reveals why they stopped talking."
      ];
      function run() {
        var p = prompts[Math.floor(Math.random() * prompts.length)];
        out.innerHTML = "<div class='tool-result'><p>" + p + "</p></div>";
      }
      btn.onclick = run; run();
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
