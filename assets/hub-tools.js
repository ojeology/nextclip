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
    "freelance-rate-calculator": function () {
      var mode = q("rc-mode"), out = q("out");
      if (!out) return;
      function n(id) { var e = q(id); return e ? parseFloat(e.value) || 0 : 0; }
      function money(v) { return "$" + v.toLocaleString(undefined, {maximumFractionDigits: 0}); }

      function calc() {
        var target = n("rc-target"), weeks = n("rc-weeks") || 48,
            billable = n("rc-billable") || 20, expenses = n("rc-expenses"),
            taxPct = n("rc-tax");

        if (!target) { out.innerHTML = "<p class='tool-note'>Enter what you need to earn in a year.</p>"; return; }

        // Gross-up for tax and expenses: you must bill enough to cover both.
        var needed = (target + expenses) / Math.max(0.05, 1 - taxPct / 100);
        var hours = weeks * billable;
        var hourly = hours ? needed / hours : 0;

        var wpm = n("rc-wpm") || 500;          // words drafted per billable hour
        var perWord = wpm ? hourly / wpm : 0;

        var pieceWords = n("rc-piece") || 1200;
        var perPiece = perWord * pieceWords;

        out.innerHTML =
          "<div class='rc-grid'>" +
            "<div class='rc-cell'><b>" + money(needed) + "</b><span>you must invoice per year</span></div>" +
            "<div class='rc-cell'><b>" + money(hourly) + "</b><span>per billable hour</span></div>" +
            "<div class='rc-cell'><b>$" + perWord.toFixed(2) + "</b><span>per word</span></div>" +
            "<div class='rc-cell'><b>" + money(perPiece) + "</b><span>for a " + pieceWords.toLocaleString() + "-word piece</span></div>" +
          "</div>" +
          "<p class='tool-note'><b>Why the invoice figure is higher than your target.</b> " +
          "It has to cover " + money(expenses) + " of expenses and " + taxPct + "% tax before anything reaches you. " +
          "It also assumes only <b>" + billable + " billable hours a week</b> — the rest goes to pitching, admin, " +
          "invoicing and chasing payment, which are real hours nobody pays you for.</p>" +
          "<p class='tool-note'>These are arithmetic, not market rates. What a market actually pays is on its " +
          "<a href='/writing/'>BRYME listing</a> — compare your number against real stated rates before quoting.</p>";
      }
      ["rc-target","rc-weeks","rc-billable","rc-expenses","rc-tax","rc-wpm","rc-piece"].forEach(function (id) {
        var e = q(id); if (e) e.addEventListener("input", calc);
      });
      if (mode) mode.addEventListener("change", calc);
      calc();
    },

    "word-count-to-pages": function () {
      var out = q("out"), words = q("wp-words");
      if (!out || !words) return;
      function val(id, d) { var e = q(id); return e ? (e.value || d) : d; }

      // Pages depend entirely on the spec. These are the standard ones, and the
      // tool states which it used rather than pretending "pages" is universal.
      var PRESETS = {
        "manuscript": { wpp: 250, label: "Standard manuscript (double-spaced, 12pt, 1in margins)" },
        "double-12":  { wpp: 250, label: "Double-spaced, 12pt Times New Roman" },
        "single-12":  { wpp: 500, label: "Single-spaced, 12pt" },
        "double-11":  { wpp: 280, label: "Double-spaced, 11pt Arial" },
        "single-11":  { wpp: 560, label: "Single-spaced, 11pt Arial" },
        "a4-academic":{ wpp: 300, label: "A4 academic, 1.5 spacing, 12pt" },
        "book":       { wpp: 300, label: "Printed book page (6x9in trade paperback)" }
      };

      function calc() {
        var w = parseInt(String(words.value).replace(/[^0-9]/g, ""), 10) || 0;
        var key = val("wp-format", "manuscript");
        var p = PRESETS[key] || PRESETS.manuscript;
        if (!w) { out.innerHTML = "<p class='tool-note'>Enter a word count.</p>"; return; }

        var pages = w / p.wpp;
        var speakMin = w / 140;   // 140 wpm is a measured speaking pace, not fast reading
        var readMin  = w / 240;   // 240 wpm silent reading

        function mins(v) {
          if (v < 1) return "under a minute";
          var m = Math.floor(v), s = Math.round((v - m) * 60);
          return m + " min" + (s >= 30 ? " 30 s" : "");
        }

        out.innerHTML =
          "<div class='rc-grid'>" +
            "<div class='rc-cell'><b>" + (pages < 1 ? pages.toFixed(2) : pages.toFixed(1)) + "</b><span>pages</span></div>" +
            "<div class='rc-cell'><b>" + w.toLocaleString() + "</b><span>words</span></div>" +
            "<div class='rc-cell'><b>" + mins(readMin) + "</b><span>to read silently</span></div>" +
            "<div class='rc-cell'><b>" + mins(speakMin) + "</b><span>to read aloud</span></div>" +
          "</div>" +
          "<p class='tool-note'>Using <b>" + p.label + "</b> at about " + p.wpp + " words per page.</p>" +
          "<p class='tool-note'><b>&ldquo;Pages&rdquo; is not a fixed unit.</b> The same 1,000 words is " +
          (1000 / 250).toFixed(1) + " double-spaced pages or " + (1000 / 500).toFixed(1) + " single-spaced. " +
          "If a brief asks for a page count, ask which spec it means &mdash; and if you are submitting somewhere, " +
          "give the word count too, because that is what editors actually work from.</p>";
      }
      words.addEventListener("input", calc);
      var f = q("wp-format"); if (f) f.addEventListener("change", calc);
      calc();
    },

    "outline-builder": function () {
      var titleEl = q("t"), typeEl = q("otype"), listEl = q("sections"),
          addBtn = q("add"), out = q("out"), copyBtn = q("copy");
      if (!listEl) return;

      /* Starting scaffolds. The point of the tool is that you then edit them:
         a generic outline is worthless, a generic outline you have argued with
         is a plan. */
      var SCAFFOLDS = {
        essay: ["Introduction — hook, context, thesis",
                "Point 1 — claim, evidence, why it matters",
                "Point 2 — claim, evidence, why it matters",
                "Counter-argument — the strongest objection, answered",
                "Conclusion — what follows from all this"],
        article: ["Lead — the most surprising true thing",
                  "Nut graf — why this, why now",
                  "Background the reader needs",
                  "The main reporting",
                  "The complication or counter-view",
                  "Close — what happens next"],
        report: ["Executive summary — findings and recommendation",
                 "Introduction — scope and terms of reference",
                 "Method — how the work was done",
                 "Findings — what the evidence shows",
                 "Discussion — what it means",
                 "Recommendations — what to do",
                 "Appendices"],
        blog: ["The answer, near the top",
               "Who this is for and what they need first",
               "Step 1", "Step 2", "Step 3",
               "Common mistakes",
               "What to do next"],
        story: ["Opening image — the world before",
                "Inciting incident — what breaks it",
                "Rising complication",
                "Midpoint — the turn",
                "Crisis — the worst choice",
                "Climax", "Resolution — the world after"],
        speech: ["Who I am and why I am up here",
                 "Opening — one concrete image",
                 "The story",
                 "What the story means",
                 "The turn — the serious beat",
                 "Close and toast"],
        blank: ["Section 1"]
      };

      var state = [];

      function esc(x) {
        return String(x).replace(/&/g, "&amp;").replace(/</g, "&lt;")
                        .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
      }

      function render() {
        listEl.innerHTML = state.map(function (row, i) {
          return '<li class="ob-row" draggable="true" data-i="' + i + '">' +
            '<span class="ob-num">' + (i + 1) + '</span>' +
            '<input class="ob-head" type="text" value="' + esc(row.head) + '" ' +
              'aria-label="Section ' + (i + 1) + ' heading" placeholder="Section heading">' +
            '<input class="ob-note" type="text" value="' + esc(row.note) + '" ' +
              'aria-label="Section ' + (i + 1) + ' notes" placeholder="What goes in here…">' +
            '<span class="ob-words">' +
              '<label class="sr-only" for="ob-w' + i + '">Target words for section ' + (i + 1) + '</label>' +
              '<input id="ob-w' + i + '" class="ob-wc" type="number" min="0" step="25" value="' + (row.words || 0) + '">' +
            '</span>' +
            '<span class="ob-btns">' +
              '<button type="button" class="ob-mini" data-up="' + i + '" aria-label="Move section ' + (i + 1) + ' up"' + (i === 0 ? " disabled" : "") + '>↑</button>' +
              '<button type="button" class="ob-mini" data-down="' + i + '" aria-label="Move section ' + (i + 1) + ' down"' + (i === state.length - 1 ? " disabled" : "") + '>↓</button>' +
              '<button type="button" class="ob-mini ob-del" data-del="' + i + '" aria-label="Delete section ' + (i + 1) + '">×</button>' +
            '</span></li>';
        }).join("");
        summarise();
      }

      function summarise() {
        var total = state.reduce(function (n, r) { return n + (+r.words || 0); }, 0);
        var filled = state.filter(function (r) { return r.note.trim(); }).length;
        out.innerHTML = "<p><b>" + state.length + "</b> section" + (state.length === 1 ? "" : "s") +
          " &middot; <b>" + total + "</b> words planned &middot; " + filled + " of " +
          state.length + " with notes</p>" +
          (total ? "<p class='tool-note'>At 200 words per section-minute of drafting, this is roughly " +
            Math.max(1, Math.round(total / 200)) + " focused writing block" +
            (Math.round(total / 200) === 1 ? "" : "s") + ".</p>" : "") +
          "<p class='tool-note'>Nothing here leaves your browser. Copy the outline before you close the tab.</p>";
      }

      function load(kind) {
        state = (SCAFFOLDS[kind] || SCAFFOLDS.blank).map(function (h) {
          var bits = h.split(" — ");
          return { head: bits[0], note: bits[1] || "", words: 0 };
        });
        render();
      }

      listEl.addEventListener("input", function (e) {
        var row = e.target.closest(".ob-row"); if (!row) return;
        var i = +row.dataset.i;
        if (e.target.classList.contains("ob-head")) state[i].head = e.target.value;
        else if (e.target.classList.contains("ob-note")) state[i].note = e.target.value;
        else if (e.target.classList.contains("ob-wc")) state[i].words = +e.target.value || 0;
        summarise();
      });

      listEl.addEventListener("click", function (e) {
        var b = e.target.closest("button"); if (!b) return;
        if (b.dataset.del !== undefined) { state.splice(+b.dataset.del, 1); }
        else if (b.dataset.up !== undefined) {
          var i = +b.dataset.up; if (i > 0) state.splice(i - 1, 0, state.splice(i, 1)[0]);
        } else if (b.dataset.down !== undefined) {
          var j = +b.dataset.down; if (j < state.length - 1) state.splice(j + 1, 0, state.splice(j, 1)[0]);
        } else return;
        if (!state.length) state = [{ head: "Section 1", note: "", words: 0 }];
        render();
      });

      if (addBtn) addBtn.addEventListener("click", function () {
        state.push({ head: "Section " + (state.length + 1), note: "", words: 0 });
        render();
        var inputs = listEl.querySelectorAll(".ob-head");
        if (inputs.length) inputs[inputs.length - 1].focus();
      });

      if (typeEl) typeEl.addEventListener("change", function () { load(typeEl.value); });

      function asText() {
        var lines = [];
        if (titleEl && titleEl.value.trim()) { lines.push(titleEl.value.trim()); lines.push(""); }
        state.forEach(function (r, i) {
          lines.push((i + 1) + ". " + (r.head || "Untitled section") +
            (r.words ? "  (" + r.words + " words)" : ""));
          if (r.note.trim()) lines.push("   " + r.note.trim());
        });
        var total = state.reduce(function (n, r) { return n + (+r.words || 0); }, 0);
        if (total) { lines.push(""); lines.push("Target: " + total + " words"); }
        return lines.join("\n");
      }

      if (copyBtn) copyBtn.addEventListener("click", function () {
        var text = asText();
        var done = function () {
          copyBtn.textContent = "Copied";
          setTimeout(function () { copyBtn.textContent = "Copy outline"; }, 1600);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, function () { fallback(text, done); });
        } else fallback(text, done);
      });

      function fallback(text, done) {
        var ta = document.createElement("textarea");
        ta.value = text; ta.setAttribute("readonly", "");
        ta.style.position = "absolute"; ta.style.left = "-9999px";
        document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); done(); } catch (e) { /* ignore */ }
        document.body.removeChild(ta);
      }

      load(typeEl ? typeEl.value : "essay");
    },
    "tone-checker": function () {
      var input = q("ta"), out = q("out");
      var FORMAL = ["furthermore","moreover","therefore","consequently","nevertheless","however","additionally","subsequently","accordingly","hereby","whom","shall","regarding","pursuant","utilise","utilize","commence","terminate","endeavour","endeavor","request","require","obtain","provide","assist","inform","advise","sincerely","faithfully","respectfully"];
      var CASUAL = ["really","pretty","kind of","sort of","a lot","stuff","things","guys","okay","ok","yeah","cool","awesome","huge","tons","loads","basically","actually","literally","super","gonna","wanna","kinda","totally","great","nice","big deal","no worries","cheers"];
      var CONTRACTIONS = /\b\w+['\u2019](s|t|re|ve|ll|d|m)\b/gi;
      function count(t, list) {
        var n = 0;
        list.forEach(function (w) {
          var m = t.match(new RegExp("\\b" + w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b", "gi"));
          if (m) n += m.length;
        });
        return n;
      }
      function run() {
        var t = WAT(input);
        var w = words(t);
        if (!w) { out.innerHTML = "<p class='muted'>Paste some writing to estimate its tone.</p>"; fit(input); return; }
        var f = count(t, FORMAL);
        var c = count(t, CASUAL);
        var contr = (t.match(CONTRACTIONS) || []).length;
        var excl = (t.match(/!/g) || []).length;
        var firstPerson = (t.match(/\b(I|we|my|our|me|us)\b/g) || []).length;
        var secondPerson = (t.match(/\b(you|your|yours)\b/g) || []).length;
        var sents = sentences(t);
        var avgLen = sents ? w / sents : w;
        /* informality signals per 100 words, vs formality signals */
        var informal = (c + contr * 1.2 + excl * 1.5 + secondPerson * 0.4) / w * 100;
        var formal = (f * 1.4 + (avgLen > 22 ? 3 : 0)) / w * 100;
        /* Compressive curve: keeps ordinary prose spread across the middle
           instead of pinning everything to 0 or 100. */
        var d = (formal - informal) / 12;
        var tanh = (Math.exp(2 * d) - 1) / (Math.exp(2 * d) + 1);
        var score = Math.max(0, Math.min(100, 50 + 48 * tanh));
        var band = score >= 72 ? "Formal" : score >= 55 ? "Neutral–formal" : score >= 42 ? "Neutral" : score >= 26 ? "Conversational" : "Very informal";
        var advice = score >= 72
          ? "Good for academic work, official letters, reports and applications. If it feels stiff for the reader, allow a few contractions."
          : score >= 42
          ? "A middle register that suits most business writing, articles and general non-fiction."
          : "Good for blogs, newsletters, social copy and personal essays. Too casual for an application, a complaint or an academic piece.";
        out.innerHTML =
          "<p><b>" + band + "</b> &middot; formality estimate <b>" + Math.round(score) + "/100</b></p>" +
          "<div class='tone-bar' role='img' aria-label='Formality " + Math.round(score) + " out of 100'>" +
            "<span class='tone-fill' style='width:" + Math.round(score) + "%'></span></div>" +
          "<p class='tool-note'>" + advice + "</p>" +
          "<table class='tool-table'><thead><tr><th>Signal</th><th>Found</th></tr></thead><tbody>" +
          "<tr><td>Formal connectives (however, therefore&hellip;)</td><td>" + f + "</td></tr>" +
          "<tr><td>Casual words (really, stuff, loads&hellip;)</td><td>" + c + "</td></tr>" +
          "<tr><td>Contractions (don't, it's&hellip;)</td><td>" + contr + "</td></tr>" +
          "<tr><td>Exclamation marks</td><td>" + excl + "</td></tr>" +
          "<tr><td>Addresses the reader as &ldquo;you&rdquo;</td><td>" + secondPerson + "</td></tr>" +
          "<tr><td>First person (I, we)</td><td>" + firstPerson + "</td></tr>" +
          "<tr><td>Average sentence length</td><td>" + avgLen.toFixed(1) + " words</td></tr>" +
          "</tbody></table>" +
          "<p class='tool-note'>This is an estimate from surface signals, not a judgement of quality. Tone is a choice — match it to your reader.</p>";
        fit(input);
      }
      bind(input, run); run();
    },
    "citation-formatter": function () {
      var out = q("out");
      var ids = ["author","title","container","year","publisher","url","accessed"];
      var f = {}; ids.forEach(function (i) { f[i] = q(i); });
      var style = q("style"), type = q("ctype");
      function v(k) { return (f[k] && f[k].value || "").trim(); }
      function lastFirst(name) {
        var parts = name.trim().split(/\s+/);
        if (parts.length < 2) return name.trim();
        var last = parts.pop();
        return last + ", " + parts.join(" ");
      }
      function initials(name) {
        var parts = name.trim().split(/\s+/);
        if (parts.length < 2) return name.trim();
        var last = parts.pop();
        return last + ", " + parts.map(function (p) { return p.charAt(0).toUpperCase() + "."; }).join(" ");
      }
      function italic(t) { return t ? "<em>" + t + "</em>" : ""; }
      function run() {
        var a = v("author"), t = v("title"), cont = v("container"), y = v("year"),
            pub = v("publisher"), url = v("url"), acc = v("accessed");
        if (!a && !t) { out.innerHTML = "<p class='muted'>Fill in at least an author or a title.</p>"; return; }
        var st = style.value, ty = type.value, s = "";
        if (st === "apa") {
          s = (a ? initials(a) + " " : "") + (y ? "(" + y + "). " : "(n.d.). ");
          s += ty === "book" ? italic(t) + ". " + (pub ? pub + ". " : "")
             : t + ". " + (cont ? italic(cont) + ". " : "");
          if (url) s += url;
        } else if (st === "mla") {
          s = (a ? lastFirst(a) + ". " : "");
          s += ty === "book" ? italic(t) + ". " + (pub ? pub + ", " : "") + (y ? y + "." : "")
             : "&ldquo;" + t + ".&rdquo; " + (cont ? italic(cont) + ", " : "") + (y ? y + ", " : "");
          if (url) s += " " + url + ".";
          if (acc) s += " Accessed " + acc + ".";
        } else {
          s = (a ? lastFirst(a) + ". " : "");
          s += ty === "book" ? italic(t) + ". " + (pub ? pub + ", " : "") + (y ? y + "." : "")
             : "&ldquo;" + t + ".&rdquo; " + (cont ? italic(cont) + " " : "") + (y ? "(" + y + ")." : "");
          if (url) s += " " + url + ".";
        }
        s = s.replace(/\s+/g, " ").replace(/\s+\./g, ".").trim();
        out.innerHTML = "<p class='citation-out'>" + s + "</p>" +
          "<p class='tool-note'>Always check against your institution's own style sheet — editions differ, and a marker's version is the one that counts.</p>";
      }
      ids.forEach(function (i) { if (f[i]) bind(f[i], run); });
      [style, type].forEach(function (el) { if (el) el.addEventListener("change", run); });
      run();
    },
    "word-alternatives": function () {
      var input = q("w"), out = q("out");
      var T = {
        "said":["noted","argued","observed","admitted","replied","explained","insisted","recalled","added","countered"],
        "very":["(cut it — strengthen the adjective instead)","markedly","acutely","profoundly","strikingly"],
        "really":["(usually deletable)","genuinely","distinctly","undeniably"],
        "good":["strong","careful","effective","sound","assured","competent","valuable"],
        "bad":["weak","careless","flawed","harmful","poor","unconvincing"],
        "big":["substantial","considerable","sweeping","vast","significant"],
        "small":["slight","modest","minor","narrow","marginal"],
        "important":["central","decisive","pivotal","consequential","material"],
        "interesting":["surprising","revealing","unexpected","telling","strange"],
        "nice":["generous","thoughtful","warm","gracious","welcome"],
        "thing":["(name it — 'thing' hides the noun)","factor","element","detail","feature"],
        "get":["obtain","receive","secure","acquire","reach","become"],
        "make":["create","produce","build","form","cause","assemble"],
        "show":["reveal","demonstrate","indicate","expose","illustrate","suggest"],
        "look":["examine","study","inspect","glance","scan","survey"],
        "think":["believe","suspect","conclude","reckon","judge","suppose"],
        "help":["support","assist","enable","ease","aid","bolster"],
        "use":["employ","apply","deploy","draw on","harness"],
        "start":["begin","open","launch","initiate","set out"],
        "end":["conclude","close","finish","resolve","cease"],
        "change":["shift","alter","revise","transform","adjust","recast"],
        "happy":["glad","content","pleased","relieved","delighted","buoyant"],
        "sad":["downcast","bereft","subdued","despondent","low"],
        "angry":["furious","indignant","incensed","irritated","seething"],
        "walk":["stride","amble","trudge","pace","wander","stroll"],
        "run":["sprint","dash","bolt","jog","tear","race"],
        "beautiful":["striking","elegant","lovely","radiant","handsome"],
        "difficult":["demanding","awkward","testing","thorny","stubborn"],
        "easy":["simple","effortless","straightforward","undemanding"],
        "a lot":["a great deal","considerably","substantially","(or give the number)"],
        "in order to":["to"],
        "due to the fact that":["because"],
        "at this point in time":["now"],
        "in my opinion":["(usually deletable — the sentence is already yours)"],
        "basically":["(usually deletable)"],
        "actually":["(usually deletable)"],
        "literally":["(only if it is literally true)"],
        "just":["(usually deletable — it softens without adding)"],
        "definitely":["(usually deletable)"],
        "utilise":["use"], "utilize":["use"],
        "commence":["start","begin"],
        "terminate":["end","stop"],
        "endeavour":["try"], "endeavor":["try"],
        "ascertain":["find out","confirm"],
        "facilitate":["help","enable"],
        "leverage":["use"],
        "impactful":["effective","powerful","(or say what it did)"]
      };
      var keys = Object.keys(T).sort();
      function run() {
        var t = (WAT(input) || "").toLowerCase().trim();
        if (!t) {
          out.innerHTML = "<p class='muted'>Type an overused word — try <b>said</b>, <b>very</b>, <b>important</b>, <b>get</b> or <b>in order to</b>.</p>" +
            "<p class='tool-note'>" + keys.length + " words and phrases covered.</p>";
          return;
        }
        var hit = T[t];
        if (!hit) {
          var near = keys.filter(function (k) { return k.indexOf(t) === 0 || t.indexOf(k) === 0; });
          out.innerHTML = near.length
            ? "<p>No exact entry. Did you mean: " + near.slice(0, 6).map(function (k) { return "<b>" + k + "</b>"; }).join(", ") + "?</p>"
            : "<p>Not in BRYME's list. This is a curated set of the words that most often weaken writing &mdash; not a full thesaurus.</p>";
          return;
        }
        out.innerHTML = "<p>Instead of <b>" + t + "</b>:</p><ul class='alt-list'>" +
          hit.map(function (x) { return "<li>" + x + "</li>"; }).join("") + "</ul>" +
          "<p class='tool-note'>A stronger word is not always a longer one. If the plain word is the honest one, keep it.</p>";
      }
      bind(input, run); run();
    },
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
    },
    "word-document-converter": function () {
      var input = q("ta"), btn = q("download"), fmt = q("format"), out = q("out");
      function htmlFrom(text) {
        var esc = text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        var paras = esc.split(/\n\s*\n/).map(function (p) { return "<p>" + p.replace(/\n/g, "<br>") + "</p>"; }).join("");
        return '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40"><head><meta charset="utf-8"><title>BRYME Writing Document</title><!--[if gte mso 9]><xml><w:WordDocument><w:View>Print</w:View><w:Zoom>100</w:Zoom></w:WordDocument></xml><![endif]--><style>body{font-family:Calibri,Arial,sans-serif;font-size:12pt;line-height:1.5}p{margin:0 0 12pt}</style></head><body>' + paras + '</body></html>';
      }
      btn.onclick = function () {
        var text = WAT(input);
        if (!text) { return; }
        var choice = (fmt.value || "doc");
        var blob, name;
        if (choice === "txt") { blob = new Blob([text], { type: "text/plain;charset=utf-8" }); name = "bryme-document.txt"; }
        else { blob = new Blob(["\ufeff" + htmlFrom(text)], { type: "application/msword" }); name = "bryme-document.doc"; }
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob); a.download = name;
        document.body.appendChild(a); a.click(); document.body.removeChild(a);
        setTimeout(function () { URL.revokeObjectURL(a.href); }, 2500);
        out.innerHTML = "<p>Downloaded <b>" + name + "</b>. Open it in Word, Google Docs or LibreOffice.</p>";
      };
      fit(input);
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
