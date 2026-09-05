/* BRYME country filter for the writing-opportunities hub.

   The control is a static <select> (not a scrolling header): every country in
   the data is inside it, grouped by continent, plus "All countries" and
   "Open worldwide". Each card carries data-country (ISO2 base country, "" for
   online/international), data-region (continent slug) and data-open
   ("international" | "regional").

   Picking a country shows that country's publications PLUS everything open to
   writers worldwide, so the list is never misleadingly empty.

   Supports ?country=NG in the URL (the sidebar links use this) and keeps the
   URL in sync so a filtered view can be shared or bookmarked. */
(function () {
  "use strict";

  var form = document.getElementById("writing-filter");
  if (!form) return;

  var select = document.getElementById("country-select");
  var reset = document.getElementById("country-reset");
  var cards = Array.prototype.slice.call(document.querySelectorAll("[data-country]"));
  var countEl = document.getElementById("filter-count");
  var emptyEl = document.getElementById("filter-empty");
  var noteEl = document.getElementById("filter-note");
  if (!select) return;

  /* Never submit — this filters in place. */
  form.addEventListener("submit", function (e) { e.preventDefault(); });

  function matches(card, filter) {
    if (filter === "all") return true;
    var open = card.getAttribute("data-open") === "international";
    if (filter === "international") return open;
    var base = (card.getAttribute("data-country") || "").toUpperCase();
    var region = card.getAttribute("data-region") || "";
    if (base && filter === base) return true;
    if (region && filter === region) return true;
    return open;
  }

  function labelFor(value) {
    var opt = select.querySelector('option[value="' + value + '"]');
    if (!opt) return "All countries";
    /* strip the trailing " — 12" count from the option label */
    return opt.textContent.replace(/\s+—\s+\d+.*$/, "").trim();
  }

  function apply(value, pushUrl) {
    var shown = 0;
    cards.forEach(function (c) {
      var on = matches(c, value);
      c.hidden = !on;
      if (on) shown += 1;
    });

    if (countEl) countEl.textContent = String(shown);
    if (emptyEl) emptyEl.hidden = shown !== 0;
    if (noteEl) {
      noteEl.textContent = "";
      var b = document.createElement("b");
      b.id = "filter-count";
      b.textContent = String(shown);
      noteEl.appendChild(b);
      noteEl.appendChild(document.createTextNode(
        " publication" + (shown === 1 ? "" : "s") + " · " + labelFor(value)));
      countEl = b;
    }
    if (reset) reset.hidden = value === "all";

    if (pushUrl && window.history && window.history.replaceState) {
      var url = new URL(window.location.href);
      if (value === "all") url.searchParams.delete("country");
      else url.searchParams.set("country", value);
      window.history.replaceState({}, "", url);
    }
  }

  function normalise(raw) {
    if (!raw) return "all";
    var v = String(raw).trim();
    /* accept ?country=ng and ?country=Africa */
    var exact = select.querySelector('option[value="' + v + '"]');
    if (exact) return v;
    var upper = select.querySelector('option[value="' + v.toUpperCase() + '"]');
    if (upper) return v.toUpperCase();
    var lower = select.querySelector('option[value="' + v.toLowerCase() + '"]');
    if (lower) return v.toLowerCase();
    return "all";
  }

  select.addEventListener("change", function () { apply(select.value, true); });

  if (reset) {
    reset.addEventListener("click", function () {
      select.value = "all";
      apply("all", true);
      select.focus();
    });
  }

  /* Deep link: /writing/?country=NG */
  var initial = "all";
  try {
    initial = normalise(new URL(window.location.href).searchParams.get("country"));
  } catch (e) { initial = "all"; }
  select.value = initial;
  apply(initial, false);
})();
