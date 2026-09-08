/* BRYME Writing Studio — a local-first drafting room.
 *
 * Scope (deliberately small and honest):
 *   - one editor, one title, live stats, an optional session goal
 *   - drafts autosaved to localStorage on this device only
 *   - export to .txt/.md, copy, print, focus mode
 * No accounts, no server, no AI writing. Nothing leaves the browser.
 * ES5 only; CSP-safe (no inline scripts).
 */
(function () {
  "use strict";
  var KEY = "bryme-studio";
  var root = document.getElementById("studio-root");
  if (!root) return;

  var el = function (id) { return document.getElementById(id); };
  var titleEl = el("st-title"), textEl = el("st-text"), listEl = el("st-list"),
      statsEl = el("st-stats"), meterEl = el("st-meter"), meterTxt = el("st-meter-txt"),
      goalEl = el("st-goal"), statusEl = el("st-status"), mirrorEl = el("st-mirror"),
      mirrorTitle = el("st-mirror-title");

  var state = { drafts: {}, current: null, goal: 500 };

  function load() {
    try {
      var raw = localStorage.getItem(KEY);
      if (raw) {
        var d = JSON.parse(raw);
        if (d && d.drafts) state = d;
      }
    } catch (e) {}
    if (!state.goal || state.goal < 50) state.goal = 500;
    if (goalEl) goalEl.value = state.goal;
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {}
  }
  function flash(msg) {
    if (!statusEl) return;
    statusEl.textContent = msg;
    statusEl.setAttribute("data-on", "1");
    clearTimeout(flash._t);
    flash._t = setTimeout(function () { statusEl.removeAttribute("data-on"); }, 1800);
  }
  function stats(text) {
    var clean = (text || "").trim();
    var words = clean ? clean.split(/\s+/).length : 0;
    var sentences = clean ? (clean.match(/[.!?]+(\s|$)/g) || []).length || (words ? 1 : 0) : 0;
    return { words: words, chars: (text || "").length, sentences: sentences, minutes: Math.ceil(words / 220) };
  }
  function currentDraft() {
    return state.drafts[state.current] || null;
  }
  function renderStats() {
    var s = stats(textEl.value);
    var mins = s.minutes === 1 ? "1 min" : s.minutes + " mins";
    statsEl.textContent = s.words.toLocaleString() + " words \u00b7 " + s.chars.toLocaleString() +
      " characters \u00b7 " + s.sentences + " sentences \u00b7 ~" + mins + " reading time";
    var goal = parseInt(goalEl.value, 10) || 0;
    state.goal = goal;
    if (goal >= 50) {
      var pct = Math.min(100, Math.round(s.words / goal * 100));
      meterEl.style.width = pct + "%";
      meterTxt.textContent = pct + "% of " + goal.toLocaleString() + "-word goal";
      meterEl.parentNode.setAttribute("data-done", pct >= 100 ? "1" : "0");
    } else {
      meterEl.style.width = "0";
      meterTxt.textContent = "set a goal above to track this session";
    }
  }
  function renderList() {
    if (!listEl) return;
    var ids = Object.keys(state.drafts).sort(function (a, b) {
      return (state.drafts[b].updated || 0) - (state.drafts[a].updated || 0);
    });
    if (!ids.length) {
      listEl.innerHTML = '<p class="st-none">No drafts yet. Write a line, it saves itself.</p>';
      return;
    }
    listEl.innerHTML = ids.map(function (id) {
      var d = state.drafts[id];
      var w = stats(d.text).words;
      var cur = id === state.current;
      return '<div class="st-draft' + (cur ? " st-cur" : "") + '">' +
        '<button type="button" class="st-open" data-id="' + id + '">' +
        '<b>' + esc(d.title || "Untitled") + '</b>' +
        '<span>' + w.toLocaleString() + " words \u00b7 " + new Date(d.updated).toLocaleDateString() + '</span></button>' +
        '<span class="st-acts">' +
        '<button type="button" class="st-ren" data-id="' + id + '" aria-label="Rename draft">rename</button>' +
        '<button type="button" class="st-del" data-id="' + id + '" aria-label="Delete draft">\u00d7</button>' +
        '</span></div>';
    }).join("");
  }
  function esc(v) { var d = document.createElement("div"); d.appendChild(document.createTextNode(v || "")); return d.innerHTML; }
  function renderAll() { renderStats(); renderList(); mirror(); }
  function mirror() {
    if (!mirrorEl) return;
    mirrorTitle.textContent = titleEl.value || "Untitled";
    mirrorEl.textContent = textEl.value || "";
  }
  function autosave() {
    var d = currentDraft();
    if (!d) {
      state.current = "d" + Date.now();
      d = state.drafts[state.current] = { title: "", text: "", updated: 0 };
    }
    d.title = titleEl.value;
    d.text = textEl.value;
    d.updated = Date.now();
    save();
    renderList();
  }
  var deb;
  function queueSave() { clearTimeout(deb); deb = setTimeout(autosave, 400); }

  function openDraft(id) {
    var d = state.drafts[id];
    if (!d) return;
    state.current = id;
    titleEl.value = d.title;
    textEl.value = d.text;
    save();
    renderAll();
    textEl.focus();
  }

  /* wire */
  load();
  if (!Object.keys(state.drafts).length) {
    state.current = "d" + Date.now();
    state.drafts[state.current] = { title: "", text: "", updated: Date.now() };
    save();
  } else if (!state.drafts[state.current]) {
    state.current = Object.keys(state.drafts).sort(function (a, b) {
      return state.drafts[b].updated - state.drafts[a].updated;
    })[0];
  }
  var cur = currentDraft();
  titleEl.value = cur.title; textEl.value = cur.text;

  textEl.addEventListener("input", function () { renderStats(); mirror(); queueSave(); });
  titleEl.addEventListener("input", function () { queueSave(); mirror(); });
  goalEl.addEventListener("input", function () { renderStats(); save(); });

  el("st-new").addEventListener("click", function () {
    state.current = "d" + Date.now();
    state.drafts[state.current] = { title: "", text: "", updated: Date.now() };
    titleEl.value = ""; textEl.value = "";
    save(); renderAll(); titleEl.focus();
  });
  listEl.addEventListener("click", function (e) {
    var t = e.target;
    if (t.classList.contains("st-open")) openDraft(t.getAttribute("data-id"));
    if (t.classList.contains("st-ren")) {
      var id = t.getAttribute("data-id");
      var name = window.prompt("Rename draft:", state.drafts[id].title || "Untitled");
      if (name !== null) { state.drafts[id].title = name; save(); renderAll(); }
    }
    if (t.classList.contains("st-del")) {
      var id2 = t.getAttribute("data-id");
      if (window.confirm("Delete this draft? This cannot be undone.")) {
        delete state.drafts[id2];
        if (state.current === id2) {
          var ids = Object.keys(state.drafts);
          state.current = ids.length ? ids[0] : null;
          if (state.current) { openDraft(state.current); return; }
          titleEl.value = ""; textEl.value = "";
        }
        save(); renderAll();
      }
    }
  });
  el("st-copy").addEventListener("click", function () {
    var txt = (titleEl.value ? titleEl.value + "\n\n" : "") + textEl.value;
    function fallback() {
      var ta = document.createElement("textarea");
      ta.value = txt; document.body.appendChild(ta); ta.select();
      try { document.execCommand("copy"); flash("Copied to clipboard"); } catch (e) {}
      document.body.removeChild(ta);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).then(function () { flash("Copied to clipboard"); }, fallback);
    } else { fallback(); }
  });
  function download(ext) {
    var name = (titleEl.value || "untitled").replace(/[^\w\s-]/g, "").trim().replace(/\s+/g, "-").toLowerCase() || "untitled";
    var blob = new Blob([(titleEl.value ? titleEl.value + "\n\n" : "") + textEl.value], { type: "text/plain;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = name + "." + ext;
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    flash("Exported as ." + ext);
  }
  el("st-txt").addEventListener("click", function () { download("txt"); });
  el("st-md").addEventListener("click", function () { download("md"); });
  el("st-print").addEventListener("click", function () { mirror(); window.print(); });
  el("st-focus").addEventListener("click", function () {
    var on = document.body.classList.toggle("studio-focus");
    this.textContent = on ? "Exit focus" : "Focus";
    flash(on ? "Focus mode — press Esc to exit" : "Back to the library");
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && document.body.classList.contains("studio-focus")) {
      document.body.classList.remove("studio-focus");
      el("st-focus").textContent = "Focus";
    }
    if ((e.metaKey || e.ctrlKey) && e.key === "s") {
      e.preventDefault(); autosave(); flash("Saved on this device");
    }
  });
  renderAll();
})();
