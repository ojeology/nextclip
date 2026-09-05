/* BRYME opportunity search & filter (Agent Brief §6, §7).

   Replaces the country-only <select> with a real facet engine over the 105
   opportunity cards. Everything is DOM-based: each card carries its own facet
   attributes, so there is no JSON payload to keep in sync with the build and
   no fetch on load.

   Design decisions worth knowing:

   - Country filtering shows that country's publications PLUS everything open
     worldwide, so the result is never misleadingly empty. That behaviour is
     inherited from the previous filter and is deliberate.
   - "Pays at least" compares against a USD figure normalised at build time.
     Records where the publication states no number are EXCLUDED from a
     minimum-pay filter rather than treated as zero — we do not know what they
     pay, and sorting them as if they paid nothing would misrepresent them.
   - Every filter writes to the URL so any result set is shareable, and the
     page reads the URL on load so the footer's country links keep working.
   - Progressive enhancement: with JS off, every card is visible and the form
     is inert. Nothing is hidden by default. */
(function () {
  "use strict";

  var root = document.getElementById("opp-filter");
  if (!root) return;

  var cards = Array.prototype.slice.call(document.querySelectorAll(".job-card[data-status]"));
  if (!cards.length) return;

  var els = {
    q: document.getElementById("f-q"),
    country: document.getElementById("f-country"),
    cmode: document.getElementById("f-cmode"),
    type: document.getElementById("f-type"),
    status: document.getElementById("f-status"),
    pay: document.getElementById("f-pay"),
    words: document.getElementById("f-words"),
    global: document.getElementById("f-global"),
    sort: document.getElementById("f-sort"),
    count: document.getElementById("f-count"),
    empty: document.getElementById("f-empty"),
    reset: document.getElementById("f-reset"),
    chips: document.getElementById("f-chips"),
    list: document.getElementById("opp-list")
  };

  root.addEventListener("submit", function (e) { e.preventDefault(); });

  function val(el) { return el && el.value ? el.value : ""; }

  /* ---- matching ---------------------------------------------------- */

  /* Two genuinely different questions share one control, so the mode is
     explicit rather than guessed:

       based  -> "which UK magazines take pitches?"  (where the publication is)
       opento -> "what can I apply to from Nigeria?" (who may submit)

     The old filter only did `opento`, which made "Nigeria" return 98 of 105
     results and was useless for the first question. */
  function matchCountry(card, f, mode) {
    if (!f || f === "all") return true;
    if (f === "international") return card.getAttribute("data-open") === "international";
    var base = (card.getAttribute("data-country") || "").toUpperCase();
    var region = card.getAttribute("data-region") || "";
    var here = (base && f === base) || (region && f === region);
    if (mode === "opento") {
      return here || card.getAttribute("data-open") === "international";
    }
    return !!here;
  }

  function matchType(card, f) {
    if (!f) return true;
    return (" " + (card.getAttribute("data-types") || "") + " ").indexOf(" " + f + " ") !== -1;
  }

  function matchStatus(card, f) {
    if (!f) return true;
    if (f === "acceptingnow") {
      var s = card.getAttribute("data-status");
      return s === "open" || s === "rolling" || s === "deadline";
    }
    return card.getAttribute("data-status") === f;
  }

  function matchPay(card, f) {
    if (!f) return true;
    var raw = card.getAttribute("data-usd");
    /* No stated figure => excluded from a minimum-pay filter. We do not know
       what it pays; pretending it pays nothing would be a fabrication. */
    if (raw === "" || raw === null) return false;
    return parseFloat(raw) >= parseFloat(f);
  }

  function matchWords(card, f) {
    if (!f) return true;
    var lo = parseFloat(card.getAttribute("data-wcmin"));
    var hi = parseFloat(card.getAttribute("data-wcmax"));
    if (isNaN(lo) && isNaN(hi)) return false;
    if (isNaN(lo)) lo = hi;
    if (isNaN(hi)) hi = lo;
    var bounds = { short: [0, 1200], medium: [800, 3000], long: [2500, 1e9] };
    var b = bounds[f];
    if (!b) return true;
    /* overlap, not containment: a 600-1500 market matches "short" */
    return lo <= b[1] && hi >= b[0];
  }

  function matchGlobal(card, on) {
    if (!on) return true;
    return card.getAttribute("data-global") === "1";
  }

  function matchQuery(card, q) {
    if (!q) return true;
    var hay = card.getAttribute("data-search") || "";
    var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    for (var i = 0; i < terms.length; i++) {
      if (hay.indexOf(terms[i]) === -1) return false;
    }
    return true;
  }

  /* ---- sorting ------------------------------------------------------ */

  function sortCards(list, mode) {
    if (!mode || mode === "default") return list;
    var copy = list.slice();
    copy.sort(function (a, b) {
      if (mode === "pay") {
        var pa = parseFloat(a.getAttribute("data-usd"));
        var pb = parseFloat(b.getAttribute("data-usd"));
        /* unstated pay always sinks, never sorts as zero */
        if (isNaN(pa) && isNaN(pb)) return 0;
        if (isNaN(pa)) return 1;
        if (isNaN(pb)) return -1;
        return pb - pa;
      }
      if (mode === "verified") {
        return (b.getAttribute("data-verified") || "").localeCompare(a.getAttribute("data-verified") || "");
      }
      if (mode === "name") {
        return (a.getAttribute("data-pub") || "").localeCompare(b.getAttribute("data-pub") || "");
      }
      if (mode === "deadline") {
        var da = a.getAttribute("data-deadline") || "";
        var db = b.getAttribute("data-deadline") || "";
        if (!da && !db) return 0;
        if (!da) return 1;
        if (!db) return -1;
        return da.localeCompare(db);
      }
      return 0;
    });
    return copy;
  }

  /* ---- active-filter chips ------------------------------------------ */

  function labelFor(sel, v) {
    if (!sel) return v;
    var o = sel.querySelector('option[value="' + (window.CSS && CSS.escape ? CSS.escape(v) : v) + '"]');
    return o ? o.textContent : v;
  }

  function renderChips(state) {
    if (!els.chips) return;
    var bits = [];
    if (state.q) bits.push(["q", '"' + state.q + '"']);
    if (state.country && state.country !== "all") bits.push(["country", labelFor(els.country, state.country).split(" \u2014 ")[0] + (state.cmode === "opento" ? " (open to)" : " (based in)")]);
    if (state.type) bits.push(["type", labelFor(els.type, state.type)]);
    if (state.status) bits.push(["status", labelFor(els.status, state.status)]);
    if (state.pay) bits.push(["pay", labelFor(els.pay, state.pay)]);
    if (state.words) bits.push(["words", labelFor(els.words, state.words)]);
    if (state.global) bits.push(["global", "Open to writers anywhere"]);
    els.chips.innerHTML = bits.map(function (b) {
      return '<button type="button" class="f-chip" data-clear="' + b[0] + '">' +
        b[1].replace(/[<>&]/g, "") + ' <span aria-hidden="true">\u00d7</span>' +
        '<span class="sr-only"> \u2014 remove this filter</span></button>';
    }).join("");
    els.chips.hidden = !bits.length;
  }

  /* ---- URL sync ------------------------------------------------------ */

  function readUrl() {
    var p = new URLSearchParams(location.search);
    if (els.q) els.q.value = p.get("q") || "";
    if (els.country) els.country.value = p.get("country") || "all";
    if (els.cmode) els.cmode.value = p.get("cmode") || "based";
    if (els.type) els.type.value = p.get("type") || "";
    if (els.status) els.status.value = p.get("status") || "";
    if (els.pay) els.pay.value = p.get("pay") || "";
    if (els.words) els.words.value = p.get("words") || "";
    if (els.global) els.global.checked = p.get("global") === "1";
    if (els.sort) els.sort.value = p.get("sort") || "default";
    /* a select can be given a value that has no matching option */
    ["country", "cmode", "type", "status", "pay", "words", "sort"].forEach(function (k) {
      var el = els[k];
      if (el && el.selectedIndex === -1) el.selectedIndex = 0;
    });
  }

  function writeUrl(state) {
    var p = new URLSearchParams();
    if (state.q) p.set("q", state.q);
    if (state.country && state.country !== "all") p.set("country", state.country);
    if (state.country && state.country !== "all" && state.cmode && state.cmode !== "based") p.set("cmode", state.cmode);
    if (state.type) p.set("type", state.type);
    if (state.status) p.set("status", state.status);
    if (state.pay) p.set("pay", state.pay);
    if (state.words) p.set("words", state.words);
    if (state.global) p.set("global", "1");
    if (state.sort && state.sort !== "default") p.set("sort", state.sort);
    var qs = p.toString();
    history.replaceState(null, "", qs ? "?" + qs : location.pathname);
  }

  /* ---- apply --------------------------------------------------------- */

  function apply(push) {
    var state = {
      q: val(els.q).trim(),
      country: val(els.country),
      cmode: val(els.cmode) || "based",
      type: val(els.type),
      status: val(els.status),
      pay: val(els.pay),
      words: val(els.words),
      global: els.global ? els.global.checked : false,
      sort: val(els.sort)
    };

    var shown = [];
    cards.forEach(function (c) {
      var ok = matchQuery(c, state.q) && matchCountry(c, state.country, state.cmode) &&
        matchType(c, state.type) && matchStatus(c, state.status) &&
        matchPay(c, state.pay) && matchWords(c, state.words) &&
        matchGlobal(c, state.global);
      c.hidden = !ok;
      if (ok) shown.push(c);
    });

    if (els.list) {
      sortCards(shown, state.sort).forEach(function (c) { els.list.appendChild(c); });
    }

    var n = shown.length;
    if (els.count) {
      els.count.textContent = n === cards.length
        ? n + " opportunities"
        : n + " of " + cards.length + " opportunities";
    }
    if (els.empty) els.empty.hidden = n !== 0;
    renderChips(state);
    if (push !== false) writeUrl(state);
  }

  /* ---- wiring -------------------------------------------------------- */

  ["q", "country", "cmode", "type", "status", "pay", "words", "global", "sort"].forEach(function (k) {
    var el = els[k];
    if (!el) return;
    el.addEventListener("change", function () { apply(); });
    if (el.tagName === "INPUT" && el.type === "search") {
      var t;
      el.addEventListener("input", function () {
        clearTimeout(t);
        t = setTimeout(function () { apply(); }, 140);
      });
    }
  });

  if (els.reset) els.reset.addEventListener("click", function () {
    if (els.q) els.q.value = "";
    if (els.country) els.country.value = "all";
    if (els.cmode) els.cmode.value = "based";
    ["type", "status", "pay", "words"].forEach(function (k) { if (els[k]) els[k].value = ""; });
    if (els.global) els.global.checked = false;
    if (els.sort) els.sort.value = "default";
    apply();
    if (els.q) els.q.focus();
  });

  if (els.chips) els.chips.addEventListener("click", function (e) {
    var b = e.target.closest("[data-clear]");
    if (!b) return;
    var k = b.getAttribute("data-clear");
    if (k === "q" && els.q) els.q.value = "";
    else if (k === "country" && els.country) els.country.value = "all";
    else if (k === "global" && els.global) els.global.checked = false;
    else if (els[k]) els[k].value = "";
    apply();
    if (els.q) els.q.focus();
  });

  readUrl();
  apply(false);
})();
