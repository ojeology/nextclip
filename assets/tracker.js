/* BRYME submission tracker (Agent Brief §12, §13).

   Local-first. Everything lives in this browser's localStorage under
   `bryme-tracker`. There is no account, no server, and nothing is transmitted.

   §13 asks that the data model be designed so accounts can be added cleanly
   later rather than building auth prematurely. So:

     - the store is a VERSIONED ENVELOPE: {v, updatedAt, entries:[...]}
     - every entry has a stable `id`, `createdAt` and `updatedAt`, which is
       what a future sync needs for last-write-wins merging
     - `source` records which BRYME opportunity an entry came from, so a
       server could later join entries to publications
     - export/import round-trips the exact envelope, so a user's data is
       portable today and migratable tomorrow

   Export exists because data with no account is data one cache-clear from
   gone, and shipping that without an escape hatch would be a dead end. */
(function () {
  "use strict";

  var KEY = "bryme-tracker";
  var VERSION = 1;

  var STATUSES = [
    ["draft",     "Draft",      "Written but not sent."],
    ["submitted", "Submitted",  "Sent. Clock started."],
    ["waiting",   "Waiting",    "Past the point where you'd expect a fast no."],
    ["followup",  "Follow-up",  "Time to nudge, once, politely."],
    ["accepted",  "Accepted",   "Commissioned or taken."],
    ["rejected",  "Rejected",   "A no. Log it and pitch it elsewhere."],
    ["paid",      "Paid",       "Money actually received."]
  ];
  var LABEL = {};
  STATUSES.forEach(function (s) { LABEL[s[0]] = s[1]; });

  var root = document.getElementById("tracker");
  if (!root) return;

  var listEl   = document.getElementById("tk-list");
  var emptyEl  = document.getElementById("tk-empty");
  var statsEl  = document.getElementById("tk-stats");
  var formEl   = document.getElementById("tk-form");
  var addBtn   = document.getElementById("tk-add");
  var cancelBtn= document.getElementById("tk-cancel");
  var exportBtn= document.getElementById("tk-export");
  var importInp= document.getElementById("tk-import");
  var filterEl = document.getElementById("tk-filter");
  var noticeEl = document.getElementById("tk-notice");

  /* ---- storage ------------------------------------------------------- */

  function blank() { return { v: VERSION, updatedAt: new Date().toISOString(), entries: [] }; }

  function read() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return blank();
      var d = JSON.parse(raw);
      if (!d || !Array.isArray(d.entries)) return blank();
      d.v = d.v || VERSION;
      return d;
    } catch (e) { return blank(); }
  }

  function write(d) {
    d.updatedAt = new Date().toISOString();
    try {
      localStorage.setItem(KEY, JSON.stringify(d));
      return true;
    } catch (e) {
      notice("Could not save — this browser's storage is full or blocked. Export your data to be safe.", true);
      return false;
    }
  }

  var store = read();

  function uid() {
    return "e" + Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
  }

  function notice(msg, bad) {
    if (!noticeEl) return;
    noticeEl.textContent = msg;
    noticeEl.className = "tk-notice" + (bad ? " bad" : "");
    noticeEl.hidden = false;
    clearTimeout(notice._t);
    notice._t = setTimeout(function () { noticeEl.hidden = true; }, 4000);
  }

  /* ---- helpers ------------------------------------------------------- */

  function esc(x) {
    return String(x == null ? "" : x).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function daysBetween(a, b) {
    return Math.round((b - a) / 86400000);
  }

  /* An entry is "overdue" when its own follow-up date has passed. We never
     invent an expected response time the publication did not state. */
  function overdue(e) {
    if (!e.followUp) return false;
    if (e.status === "accepted" || e.status === "rejected" || e.status === "paid") return false;
    return new Date(e.followUp) < new Date(new Date().toDateString());
  }

  /* ---- rendering ----------------------------------------------------- */

  function render() {
    var f = filterEl ? filterEl.value : "";
    var rows = store.entries.slice().sort(function (a, b) {
      return (b.submitted || b.createdAt || "").localeCompare(a.submitted || a.createdAt || "");
    });
    var shown = f ? rows.filter(function (e) { return e.status === f; }) : rows;

    listEl.innerHTML = shown.map(function (e) {
      var od = overdue(e);
      var age = e.submitted ? daysBetween(new Date(e.submitted), new Date()) : null;
      return '<li class="tk-row' + (od ? " overdue" : "") + '" data-id="' + esc(e.id) + '" data-status="' + esc(e.status) + '">' +
        '<div class="tk-main">' +
          '<div class="tk-head">' +
            '<span class="tk-status s-' + esc(e.status) + '">' + esc(LABEL[e.status] || e.status) + '</span>' +
            (od ? '<span class="tk-flag">Follow-up due</span>' : "") +
          '</div>' +
          '<h3 class="tk-pub">' + (e.url
              ? '<a href="' + esc(e.url) + '">' + esc(e.publication) + '</a>'
              : esc(e.publication)) + '</h3>' +
          (e.pitch ? '<p class="tk-pitch">' + esc(e.pitch) + '</p>' : "") +
          '<dl class="tk-facts">' +
            (e.submitted ? '<div><dt>Submitted</dt><dd>' + esc(e.submitted) +
              (age !== null && age >= 0 ? ' <span class="tk-age">' + age + 'd ago</span>' : "") + '</dd></div>' : "") +
            (e.expected ? '<div><dt>Reply expected</dt><dd>' + esc(e.expected) + '</dd></div>' : "") +
            (e.followUp ? '<div><dt>Follow up</dt><dd>' + esc(e.followUp) + '</dd></div>' : "") +
            (e.fee ? '<div><dt>Fee</dt><dd>' + esc(e.fee) + '</dd></div>' : "") +
          '</dl>' +
          (e.notes ? '<p class="tk-notes">' + esc(e.notes) + '</p>' : "") +
        '</div>' +
        '<div class="tk-actions">' +
          '<label class="sr-only" for="s-' + esc(e.id) + '">Status for ' + esc(e.publication) + '</label>' +
          '<select class="tk-set" id="s-' + esc(e.id) + '" data-id="' + esc(e.id) + '">' +
            STATUSES.map(function (s) {
              return '<option value="' + s[0] + '"' + (e.status === s[0] ? " selected" : "") + '>' + s[1] + '</option>';
            }).join("") +
          '</select>' +
          '<button type="button" class="tk-btn" data-edit="' + esc(e.id) + '">Edit</button>' +
          '<button type="button" class="tk-btn danger" data-del="' + esc(e.id) + '" ' +
            'aria-label="Delete the entry for ' + esc(e.publication) + '">Delete</button>' +
        '</div></li>';
    }).join("");

    emptyEl.hidden = shown.length !== 0;
    if (shown.length === 0 && store.entries.length > 0) {
      emptyEl.textContent = "No pitches with that status yet.";
    } else if (shown.length === 0) {
      emptyEl.textContent = "Nothing tracked yet. Add your first pitch — or open any opportunity and use “Track this pitch”.";
    }

    // Stats. Counts only; no invented rates.
    var n = store.entries.length;
    var by = {};
    store.entries.forEach(function (e) { by[e.status] = (by[e.status] || 0) + 1; });
    var live = (by.submitted || 0) + (by.waiting || 0) + (by.followup || 0);
    var due = store.entries.filter(overdue).length;
    statsEl.innerHTML = n === 0 ? "" :
      '<span><b>' + n + '</b> tracked</span>' +
      '<span><b>' + live + '</b> awaiting a reply</span>' +
      '<span><b>' + (by.accepted || 0) + '</b> accepted</span>' +
      '<span><b>' + (by.paid || 0) + '</b> paid</span>' +
      (due ? '<span class="due"><b>' + due + '</b> follow-up due</span>' : "");
  }

  /* ---- form ---------------------------------------------------------- */

  var editing = null;

  function openForm(entry) {
    editing = entry ? entry.id : null;
    formEl.hidden = false;
    formEl.querySelector("#tk-f-pub").value      = entry ? entry.publication : "";
    formEl.querySelector("#tk-f-pitch").value    = entry ? (entry.pitch || "") : "";
    formEl.querySelector("#tk-f-status").value   = entry ? entry.status : "draft";
    formEl.querySelector("#tk-f-submitted").value= entry ? (entry.submitted || "") : "";
    formEl.querySelector("#tk-f-expected").value = entry ? (entry.expected || "") : "";
    formEl.querySelector("#tk-f-follow").value   = entry ? (entry.followUp || "") : "";
    formEl.querySelector("#tk-f-fee").value      = entry ? (entry.fee || "") : "";
    formEl.querySelector("#tk-f-notes").value    = entry ? (entry.notes || "") : "";
    formEl.querySelector("#tk-f-url").value      = entry ? (entry.url || "") : "";
    formEl.querySelector("#tk-submit").textContent = entry ? "Save changes" : "Add pitch";
    formEl.querySelector("#tk-f-pub").focus();
  }

  function closeForm() { formEl.hidden = true; editing = null; formEl.reset(); }

  if (addBtn) addBtn.addEventListener("click", function () { openForm(null); });
  if (cancelBtn) cancelBtn.addEventListener("click", closeForm);

  formEl.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var pub = formEl.querySelector("#tk-f-pub").value.trim();
    if (!pub) return;
    var now = new Date().toISOString();
    var data = {
      publication: pub,
      pitch:     formEl.querySelector("#tk-f-pitch").value.trim(),
      status:    formEl.querySelector("#tk-f-status").value,
      submitted: formEl.querySelector("#tk-f-submitted").value,
      expected:  formEl.querySelector("#tk-f-expected").value,
      followUp:  formEl.querySelector("#tk-f-follow").value,
      fee:       formEl.querySelector("#tk-f-fee").value.trim(),
      notes:     formEl.querySelector("#tk-f-notes").value.trim(),
      url:       formEl.querySelector("#tk-f-url").value.trim(),
      updatedAt: now
    };
    if (editing) {
      var e = store.entries.filter(function (x) { return x.id === editing; })[0];
      if (e) Object.keys(data).forEach(function (k) { e[k] = data[k]; });
    } else {
      data.id = uid();
      data.createdAt = now;
      data.source = null;
      store.entries.push(data);
    }
    write(store); render(); closeForm();
    notice(editing ? "Saved." : "Added.");
  });

  /* ---- list interactions --------------------------------------------- */

  listEl.addEventListener("change", function (ev) {
    var sel = ev.target.closest(".tk-set");
    if (!sel) return;
    var e = store.entries.filter(function (x) { return x.id === sel.dataset.id; })[0];
    if (!e) return;
    e.status = sel.value;
    e.updatedAt = new Date().toISOString();
    /* Moving to Submitted with no date is almost always an oversight. */
    if (e.status === "submitted" && !e.submitted) {
      e.submitted = new Date().toISOString().slice(0, 10);
    }
    write(store); render();
  });

  listEl.addEventListener("click", function (ev) {
    var d = ev.target.closest("[data-del]");
    if (d) {
      var ent = store.entries.filter(function (x) { return x.id === d.dataset.del; })[0];
      if (ent && window.confirm("Delete the entry for " + ent.publication + "? This cannot be undone.")) {
        store.entries = store.entries.filter(function (x) { return x.id !== d.dataset.del; });
        write(store); render(); notice("Deleted.");
      }
      return;
    }
    var ed = ev.target.closest("[data-edit]");
    if (ed) {
      var e2 = store.entries.filter(function (x) { return x.id === ed.dataset.edit; })[0];
      if (e2) openForm(e2);
    }
  });

  if (filterEl) filterEl.addEventListener("change", render);

  /* ---- export / import ------------------------------------------------ */

  if (exportBtn) exportBtn.addEventListener("click", function () {
    var blob = new Blob([JSON.stringify(store, null, 2)], { type: "application/json" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "bryme-tracker-" + new Date().toISOString().slice(0, 10) + ".json";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  });

  if (importInp) importInp.addEventListener("change", function () {
    var file = importInp.files && importInp.files[0];
    if (!file) return;
    var r = new FileReader();
    r.onload = function () {
      try {
        var d = JSON.parse(r.result);
        if (!d || !Array.isArray(d.entries)) throw new Error("shape");
        var have = {};
        store.entries.forEach(function (e) { have[e.id] = e; });
        var added = 0, merged = 0;
        d.entries.forEach(function (e) {
          if (!e || !e.publication) return;
          if (!e.id) e.id = uid();
          if (have[e.id]) {
            /* last write wins — the field a future sync would use */
            if ((e.updatedAt || "") > (have[e.id].updatedAt || "")) {
              Object.keys(e).forEach(function (k) { have[e.id][k] = e[k]; });
              merged++;
            }
          } else {
            store.entries.push(e); added++;
          }
        });
        write(store); render();
        notice("Imported: " + added + " added, " + merged + " updated.");
      } catch (err) {
        notice("That file is not a BRYME tracker export.", true);
      }
      importInp.value = "";
    };
    r.readAsText(file);
  });

  /* ---- prefill from an opportunity page -------------------------------- */
  /* /tracker/?add=Publication%20Name&url=/writing/slug/ */
  (function prefill() {
    var p = new URLSearchParams(location.search);
    var pub = p.get("add");
    if (!pub) return;
    openForm(null);
    formEl.querySelector("#tk-f-pub").value = pub;
    var u = p.get("url");
    if (u && u.charAt(0) === "/") formEl.querySelector("#tk-f-url").value = u;
    formEl.querySelector("#tk-f-status").value = "draft";
    history.replaceState(null, "", location.pathname);
  })();

  render();
})();
