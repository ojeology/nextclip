/* BRYME Tech — the living machine.
   Self-hosted, deferred, dependency-free, no network call, no inline JS
   (the family ships script-src 'self' https:). Everything it remembers lives
   in this browser's localStorage; nothing leaves the page.

   Two halves:
     1. the tracker — runs on every page under /tech/ and records visits, so
        the hub can offer "continue where you left off" and "new since your
        last visit" without a server, a cookie or an account;
     2. the desk — runs only on /tech/ (guarded by element presence): instant
        filtering, sorting, save-for-later, the command palette, the deep-cut
        shuffle and the scroll reveals.
   Both are additive. With JavaScript switched off the hub is still a complete
   index of the desk, every row a plain link, nothing collapsed. */
(function () {
  "use strict";

  var K_SAVED = "bryme.tech.saved.v1";
  var K_SEEN = "bryme.tech.seen.v1";
  var K_VISIT = "bryme.tech.visit.v1";
  var K_PREFS = "bryme.tech.prefs.v1";
  var MAX_SEEN = 40, MAX_SAVED = 40, MAX_LIST = 6;

  var prevVisit = "";   /* captured before this page updates it, see tracker() */

  /* ---------- storage that never throws ---------- */
  function read(key, fallback) {
    try {
      var raw = window.localStorage.getItem(key);
      if (!raw) return fallback;
      var v = JSON.parse(raw);
      return (v === null || v === undefined) ? fallback : v;
    } catch (e) { return fallback; }
  }
  function write(key, value) {
    try { window.localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* private mode: stay quiet */ }
  }
  function drop(key) { try { window.localStorage.removeItem(key); } catch (e) {} }

  function today() {
    var d = new Date();
    var m = d.getMonth() + 1, day = d.getDate();
    return d.getFullYear() + "-" + (m < 10 ? "0" : "") + m + "-" + (day < 10 ? "0" : "") + day;
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function on(el, ev, fn) { if (el) el.addEventListener(ev, fn); }
  function all(sel, root) { return [].slice.call((root || document).querySelectorAll(sel)); }
  function reduceMotion() {
    return !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  }

  /* ---------- 1. the tracker (every tech page) ---------- */
  function tracker() {
    var path = location.pathname;
    if (path.indexOf("/tech/") !== 0) return;
    var h1 = document.querySelector("#main h1") || document.querySelector("h1");
    var title = String((h1 ? h1.textContent : document.title) || "").replace(/\s+/g, " ").trim().slice(0, 120);
    if (!title) return;

    var t = document.querySelector("time[datetime]");
    var stamp = t ? String(t.getAttribute("datetime") || "").slice(0, 10) : "";

    prevVisit = read(K_VISIT, "");
    var seen = read(K_SEEN, {}) || {};
    if (!seen[path] || typeof seen[path] !== "object") seen[path] = { t: title, d: stamp, n: 0, ts: 0 };
    var e = seen[path];
    e.t = title; e.n = (e.n || 0) + 1; e.ts = new Date().getTime();
    if (stamp) e.d = stamp;

    var keys = Object.keys(seen).sort(function (a, b) { return (seen[b].ts || 0) - (seen[a].ts || 0); });
    if (keys.length > MAX_SEEN) {
      var trimmed = {};
      for (var i = 0; i < MAX_SEEN; i++) trimmed[keys[i]] = seen[keys[i]];
      seen = trimmed;
    }
    write(K_SEEN, seen);
    if (prevVisit !== today()) write(K_VISIT, today());
  }

  /* ---------- 2. the desk (the hub) ---------- */
  function desk() {
    var root = document.querySelector("[data-tm-shelves]");
    if (!root) return;
    document.documentElement.classList.add("tm-js");

    var rows = all(".tm-row", root);
    var shelves = all(".tm-shelf", root);
    var countEl = document.querySelector("[data-tm-count]");
    var noMatch = document.querySelector("[data-tm-nomatch]");
    var input = document.getElementById("tm-q");
    var clearBtn = document.querySelector("[data-tm-clear-filters]");
    var mem = document.querySelector("[data-tm-memory]");
    var pal = document.querySelector("[data-tm-palette]");
    var palQ = document.getElementById("tm-pal-q");
    var palList = document.querySelector("[data-tm-pal]");

    var prefs = read(K_PREFS, {}) || {};
    var state = { q: "", need: "", kind: "", saved: false, sort: "recent" };
    if (typeof prefs.need === "string") state.need = prefs.need;
    if (prefs.sort === "az" || prefs.sort === "recent") state.sort = prefs.sort;

    var saved = read(K_SAVED, []) || [];
    var openShelf = {};
    var palHits = [], palIdx = 0;

    function savedIdx() {
      var m = {};
      for (var i = 0; i < saved.length; i++) m[saved[i].u] = i;
      return m;
    }
    var sIdx = savedIdx();
    function persistSaved() { saved = saved.slice(0, MAX_SAVED); write(K_SAVED, saved); sIdx = savedIdx(); }
    function persistPrefs() { write(K_PREFS, { need: state.need, sort: state.sort }); }

    /* --- "new since your last visit": real dates, one honest comparison --- */
    if (prevVisit) {
      rows.forEach(function (r) {
        var d = r.getAttribute("data-date") || "";
        var side = r.querySelector(".tm-row-side");
        if (d && side && d > prevVisit) {
          var b = document.createElement("b");
          b.className = "tm-new";
          b.textContent = "new";
          b.title = "Verified " + d + " \u2014 newer than your last visit to this desk";
          side.appendChild(b);
        }
      });
    }

    /* --- save controls --- */
    function saveTarget(btn) {
      var row = btn.parentNode;
      var a = row && row.querySelector ? row.querySelector(".tm-row-a") : null;
      if (!a) return null;
      var b = a.querySelector("b");
      return {
        u: a.getAttribute("href") || "",
        t: (b ? b.textContent : a.textContent || "").replace(/\s+/g, " ").trim(),
        d: (row.getAttribute("data-date") || "")
      };
    }
    function paintSave(btn) {
      var tgt = saveTarget(btn);
      if (!tgt) return;
      var url = tgt.u;
      var isOn = sIdx[url] !== undefined;
      btn.setAttribute("aria-pressed", isOn ? "true" : "false");
      var t = btn.querySelector(".tm-save-t");
      if (t) t.textContent = isOn ? "Saved" : "Save";
      btn.setAttribute("aria-label", (isOn ? "Remove from saved: " : "Save for later: ")
        + (tgt.t || "this piece"));
    }
    function repaintSave(url) {
      all(".tm-save").forEach(function (b) {
        var tgt = saveTarget(b);
        if (tgt && tgt.u === url) paintSave(b);
      });
    }
    all(".tm-save").forEach(function (btn) {
      paintSave(btn);
      on(btn, "click", function (ev) {
        ev.preventDefault();
        var tgt = saveTarget(btn);
        if (!tgt || !tgt.u) return;
        var url = tgt.u;
        if (sIdx[url] !== undefined) saved.splice(sIdx[url], 1);
        else saved.unshift({ u: url, t: tgt.t || url, d: tgt.d });
        persistSaved();
        repaintSave(url);
        apply();
        renderMemory();
      });
    });

    /* --- filtering + sorting (no re-render of text: nodes move, never rebuild) --- */
    function matches(r) {
      if (state.need && (r.getAttribute("data-need") || "").indexOf(state.need) === -1) return false;
      if (state.kind && r.getAttribute("data-kind") !== state.kind) return false;
      if (state.saved) {
        var a = r.querySelector(".tm-row-a");
        if (!a || sIdx[a.getAttribute("href")] === undefined) return false;
      }
      if (state.q) {
        var hay = (r.textContent || "").toLowerCase();
        var toks = state.q.toLowerCase().split(/\s+/);
        for (var i = 0; i < toks.length; i++) {
          if (toks[i] && hay.indexOf(toks[i]) === -1) return false;
        }
      }
      return true;
    }
    function textOf(r) { var b = r.querySelector("b"); return b ? b.textContent : ""; }
    function sortRows(list) {
      var copy = list.slice();
      if (state.sort === "az") return copy.sort(function (a, b) { return textOf(a).localeCompare(textOf(b)); });
      return copy.sort(function (a, b) {
        var da = a.getAttribute("data-date") || "", db = b.getAttribute("data-date") || "";
        if (da === db) return textOf(a).localeCompare(textOf(b));
        return da < db ? 1 : -1;
      });
    }
    function wireMore(sh, n) {
      var body = sh.querySelector(".tm-rows");
      var btn = sh.querySelector("[data-more]");
      if (!body || !btn) return;
      var flat = !!(state.q || state.need || state.kind || state.saved) || !!openShelf[sh.getAttribute("data-shelf")];
      if (body.classList) body.classList[flat ? "remove" : "add"]("tm-clipped");
      btn.hidden = n <= 8;
      btn.textContent = flat ? "Shorten this shelf" : "Show all " + n + " pieces in this shelf";
    }
    function apply() {
      var shown = 0;
      shelves.forEach(function (sh) {
        var body = sh.querySelector(".tm-rows");
        if (!body) return;
        var mine = all(".tm-row", body);
        var keep = sortRows(mine.filter(matches));
        keep.forEach(function (r) { r.hidden = false; body.appendChild(r); });
        mine.forEach(function (r) { if (keep.indexOf(r) === -1) r.hidden = true; });
        shown += keep.length;
        sh.hidden = keep.length === 0;
        var em = sh.querySelector(".tm-shelf-h em");
        if (em) em.textContent = String(keep.length);
        wireMore(sh, keep.length);
      });
      if (countEl) countEl.textContent = shown + " of " + rows.length + " shown";
      if (noMatch) noMatch.hidden = shown !== 0;
      if (clearBtn) clearBtn.hidden = !(state.q || state.need || state.kind || state.saved);
      all(".tm-chip").forEach(function (c) {
        var p = false;
        if (c.getAttribute("data-need")) p = state.need === c.getAttribute("data-need");
        else if (c.getAttribute("data-kind")) p = state.kind === c.getAttribute("data-kind");
        else if (c.hasAttribute("data-saved")) p = state.saved;
        c.setAttribute("aria-pressed", p ? "true" : "false");
      });
      all(".tm-need").forEach(function (c) {
        c.setAttribute("aria-pressed", state.need === c.getAttribute("data-need") ? "true" : "false");
      });
      all(".tm-sortb[data-sort]").forEach(function (b) {
        b.setAttribute("aria-pressed", state.sort === b.getAttribute("data-sort") ? "true" : "false");
      });
      persistPrefs();
    }
    shelves.forEach(function (sh) {
      on(sh.querySelector("[data-more]"), "click", function () {
        var k = sh.getAttribute("data-shelf");
        openShelf[k] = !openShelf[k];
        apply();
      });
    });

    /* --- controls --- */
    var debounce = 0;
    if (input) {
      on(input, "input", function () {
        var v = input.value;
        window.clearTimeout(debounce);
        debounce = window.setTimeout(function () { state.q = v.trim(); apply(); }, 90);
      });
    }
    function clearAll() {
      state.q = ""; state.need = ""; state.kind = ""; state.saved = false;
      if (input) input.value = "";
      apply();
    }
    all(".tm-chip").forEach(function (c) {
      on(c, "click", function () {
        if (c.hasAttribute("data-tm-clear-filters")) return clearAll();
        if (c.getAttribute("data-need")) {
          var nd = c.getAttribute("data-need");
          state.need = state.need === nd ? "" : nd;
        } else if (c.getAttribute("data-kind")) {
          var kd = c.getAttribute("data-kind");
          state.kind = state.kind === kd ? "" : kd;
        } else if (c.hasAttribute("data-saved")) {
          state.saved = !state.saved;
        }
        apply();
      });
    });
    all(".tm-need").forEach(function (btn) {
      on(btn, "click", function () {
        var nd = btn.getAttribute("data-need");
        state.need = state.need === nd ? "" : nd;
        apply();
        var core = document.getElementById("tm-core");
        if (core && core.scrollIntoView) core.scrollIntoView({ behavior: reduceMotion() ? "auto" : "smooth", block: "start" });
      });
    });
    all(".tm-sortb[data-sort]").forEach(function (b) {
      on(b, "click", function () { state.sort = b.getAttribute("data-sort"); apply(); });
    });
    var dice = document.querySelector("[data-tm-dice]");
    if (dice) {
      dice.hidden = false;
      on(dice, "click", function () {
        var pool = rows.filter(function (r) { return !r.hidden; });
        if (!pool.length) pool = rows;
        var a = pool[Math.floor(Math.random() * pool.length)].querySelector(".tm-row-a");
        if (a) location.href = a.getAttribute("href");
      });
    }

    /* --- memory panel --- */
    function memItem(url, title, meta, removable) {
      return "<li><a href=\"" + esc(url) + "\">" + esc(title) + "</a>"
        + (meta ? "<i>" + esc(meta) + "</i>" : "")
        + (removable ? "<button type=\"button\" data-unsave=\"" + esc(url)
          + "\" aria-label=\"Remove from saved\">" + "&#10005;</button>" : "") + "</li>";
    }
    function renderMemory() {
      if (!mem) return;
      var savedUl = document.querySelector("[data-tm-saved]");
      var recentUl = document.querySelector("[data-tm-recent]");
      var sHtml = "", rHtml = "", any = false, i;
      if (saved.length) {
        any = true;
        for (i = 0; i < Math.min(saved.length, MAX_LIST); i++) sHtml += memItem(saved[i].u, saved[i].t, saved[i].d, true);
      }
      var seen = read(K_SEEN, {}) || {};
      var keys = Object.keys(seen).sort(function (a, b) { return (seen[b].ts || 0) - (seen[a].ts || 0); });
      var shown = 0;
      for (i = 0; i < keys.length && shown < MAX_LIST; i++) {
        if (keys[i] === location.pathname) continue;
        any = true; shown++;
        rHtml += memItem(keys[i], seen[keys[i]].t || keys[i], "read " + (seen[keys[i]].n || 1) + "\u00d7", false);
      }
      if (savedUl) savedUl.innerHTML = sHtml;
      if (recentUl) recentUl.innerHTML = rHtml;
      all("[data-tm-saved-empty]", mem).forEach(function (el) { el.hidden = !!saved.length; });
      all("[data-tm-recent-empty]", mem).forEach(function (el) { el.hidden = !!rHtml; });
      mem.hidden = !any;
      all("[data-unsave]", mem).forEach(function (b) {
        on(b, "click", function () {
          var u = b.getAttribute("data-unsave"), m = savedIdx();
          if (m[u] !== undefined) saved.splice(m[u], 1);
          persistSaved(); repaintSave(u); apply(); renderMemory();
        });
      });
    }
    on(document.querySelector("[data-tm-clear]"), "click", function () {
      drop(K_SAVED); drop(K_SEEN); drop(K_VISIT); drop(K_PREFS);
      saved = []; persistSaved();
      all(".tm-save").forEach(paintSave);
      all(".tm-new").forEach(function (n) { if (n.parentNode) n.parentNode.removeChild(n); });
      apply(); renderMemory();
    });

    /* --- command palette (the hook that pays for itself: it is the fastest
           way to the answer on this desk) --- */
    function palOpen() {
      if (!pal) return;
      pal.hidden = false;
      document.documentElement.style.overflow = "hidden";
      if (palQ) { palQ.value = ""; palQ.focus(); }
      palSearch("");
    }
    function palClose() {
      if (!pal) return;
      pal.hidden = true;
      document.documentElement.style.overflow = "";
      var o = document.querySelector("[data-tm-open-palette]");
      if (o) o.focus();
    }
    function palSearch(q) {
      if (!palList) return;
      var toks = String(q || "").toLowerCase().split(/\s+/).filter(Boolean);
      palHits = toks.length ? rows.filter(function (r) {
        var hay = (r.textContent || "").toLowerCase();
        for (var i = 0; i < toks.length; i++) if (hay.indexOf(toks[i]) === -1) return false;
        return true;
      }).slice(0, 12) : [];
      var out = "";
      palHits.forEach(function (r, i) {
        var a = r.querySelector(".tm-row-a");
        out += "<li role=\"option\" aria-selected=\"" + (i === 0 ? "true" : "false") + "\">"
          + "<a href=\"" + esc(a.getAttribute("href")) + "\"><b>" + esc(textOf(r)) + "</b>"
          + "<small>" + esc((r.getAttribute("data-sec") || "").replace("-", " ")) + " \u00b7 "
          + esc(r.getAttribute("data-date") || "no date") + "</small></a></li>";
      });
      palList.innerHTML = out || "<li><small>Type a word \u2014 the match runs on the "
        + rows.length + " pieces already in this page. Nothing is sent anywhere.</small></li>";
      palIdx = 0;
    }
    function palMove(dir) {
      var items = all("li[role='option']", palList);
      if (!items.length) return;
      if (items[palIdx]) items[palIdx].setAttribute("aria-selected", "false");
      palIdx = (palIdx + dir + items.length) % items.length;
      items[palIdx].setAttribute("aria-selected", "true");
      if (items[palIdx].scrollIntoView) items[palIdx].scrollIntoView({ block: "nearest" });
    }
    on(document.querySelector("[data-tm-open-palette]"), "click", palOpen);
    on(pal, "click", function (ev) { if (ev.target === pal) palClose(); });
    on(palQ, "input", function () { palSearch(palQ.value); });
    on(palQ, "keydown", function (ev) {
      if (ev.key === "ArrowDown") { ev.preventDefault(); palMove(1); }
      else if (ev.key === "ArrowUp") { ev.preventDefault(); palMove(-1); }
      else if (ev.key === "Enter") {
        var a = all("li[role='option']", palList)[palIdx];
        a = a && a.querySelector("a");
        if (a) { ev.preventDefault(); location.href = a.getAttribute("href"); }
      }
    });
    on(document, "keydown", function (ev) {
      var tag = ((ev.target && ev.target.tagName) || "").toUpperCase();
      var typing = tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT";
      if ((ev.metaKey || ev.ctrlKey) && (ev.key === "k" || ev.key === "K")) {
        ev.preventDefault();
        if (pal && pal.hidden) palOpen(); else palClose();
        return;
      }
      if (ev.key === "Escape" && pal && !pal.hidden) { palClose(); return; }
      if (typing) return;
      if (ev.key === "/") { ev.preventDefault(); if (input) input.focus(); return; }
      if (ev.key === "0") { clearAll(); return; }
      var n = parseInt(ev.key, 10);
      if (n >= 1 && n <= 6) {
        var btns = all(".tm-need");
        if (btns[n - 1]) btns[n - 1].click();
      }
    });

    /* --- reveals: motion that never hides content behind it --- */
    if (!reduceMotion() && "IntersectionObserver" in window) {
      var targets = all(".tm-boot, .tm-band");
      targets.forEach(function (el) { el.classList.add("tm-anim"); });
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("tm-in"); io.unobserve(en.target); }
        });
      }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
      targets.forEach(function (el) { io.observe(el); });
    }

    apply();
    renderMemory();
  }

  function boot() {
    try { tracker(); } catch (e) { /* memory is a convenience, never a dependency */ }
    try { desk(); } catch (e) { /* ditto: the page is already a complete index */ }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
