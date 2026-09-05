/* BRYME country filter for the writing-opportunities hub.
   Each job card carries data-country (base country ISO2, or "" for online/international)
   and data-open ("international" | "regional"). Picking a country shows that
   country's publications PLUS everything that is open to writers worldwide. */
(function () {
  "use strict";
  var form = document.getElementById("writing-filter");
  if (!form) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll("[data-country]"));
  var chips = Array.prototype.slice.call(form.querySelectorAll(".country-chip"));
  var countEl = document.getElementById("filter-count");
  var emptyEl = document.getElementById("filter-empty");
  var noteEl = document.getElementById("filter-note");

  var REGIONS = {
    africa: ["NG", "ZA", "NA", "KE", "GH", "ZW", "UG", "TZ"],
    europe: ["IE", "DE", "FR", "ES", "NL"],
    asia: ["NP", "IN", "PK", "SG"],
  };

  function baseOf(card) { return (card.getAttribute("data-country") || "").toUpperCase(); }
  function openOf(card) { return (card.getAttribute("data-open") || ""); }

  function matches(card, filter) {
    if (filter === "all") return true;
    if (filter === "international") return openOf(card) === "international";
    var base = baseOf(card);
    var inTarget = REGIONS[filter] ? REGIONS[filter].indexOf(base) !== -1 : base === filter;
    /* selected country/region + everything open internationally */
    return inTarget || openOf(card) === "international";
  }

  function apply(chip) {
    var filter = chip.getAttribute("data-filter") || "all";
    var shown = 0;
    cards.forEach(function (c) {
      var on = matches(c, filter);
      c.style.display = on ? "" : "none";
      if (on) shown += 1;
    });
    chips.forEach(function (c) {
      var active = c === chip;
      c.setAttribute("aria-pressed", active ? "true" : "false");
      c.classList.toggle("is-active", active);
    });
    if (countEl) countEl.textContent = String(shown);
    if (emptyEl) emptyEl.hidden = shown !== 0;
    if (noteEl) {
      var label = chip && chip.textContent ? chip.textContent.trim() : "All publications";
      noteEl.textContent = "Showing " + shown + " publication" + (shown === 1 ? "" : "s") + " · " + label;
    }
  }

  chips.forEach(function (c) {
    c.addEventListener("click", function () { apply(c); });
  });

  /* keep each chip's count badge in sync with the live filter */
  function refreshCounts() {
    chips.forEach(function (c) {
      var f = c.getAttribute("data-filter") || "all";
      var n = cards.filter(function (card) { return matches(card, f); }).length;
      var badge = c.querySelector(".chip-count");
      if (badge) badge.textContent = "· " + n;
    });
  }
  refreshCounts();

  /* respect a ?country= param so links can deep-link to a filter */
  var params = new URLSearchParams(window.location.search);
  var wanted = (params.get("country") || "all").toLowerCase();
  var target = chips.filter(function (c) {
    return (c.getAttribute("data-filter") || "all") === wanted;
  })[0];
  apply(target || chips[0] || { setAttribute: function () {}, classList: { toggle: function () {} }, textContent: "" });
})();
