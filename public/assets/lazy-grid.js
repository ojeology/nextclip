/* BRYME lazy shelf expansion (batch 12, audit LOW: heavy DOMs).

   The entertainment catalogue hub renders the first tiles of every genre
   shelf as HTML; the remaining tiles ride in a JSON sidecar next to the page
   (nx-shelves.json) and are appended on demand when a shelf's "Show N more"
   button is clicked. Discovery is unaffected: every film is in the property
   sitemap, and the first tiles of each shelf stay crawlable in the HTML.

   No framework, no build coupling: buttons carry data-shelf keys, and the
   sidecar URL comes from the script tag's own data-nx-shelves attribute
   (relative, so it resolves identically in every served tree). External by
   necessity - the site CSP is script-src 'self' with no unsafe-inline. */
(function () {
  "use strict";
  var buttons = document.querySelectorAll(".nx-more[data-shelf]");
  if (!buttons.length) return;
  var tag = document.querySelector("script[data-nx-shelves]");
  var url = tag ? tag.getAttribute("data-nx-shelves") : "nx-shelves.json";
  var data = null;
  var waiting = [];
  var loading = false;
  function load(cb) {
    if (data) { cb(data); return; }
    waiting.push(cb);
    if (loading) return;
    loading = true;
    fetch(url, { credentials: "same-origin" })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (j) {
        data = j || {};
        var q = waiting;
        waiting = [];
        q.forEach(function (f) { f(data); });
      })
      .catch(function () { loading = false; });
  }
  Array.prototype.forEach.call(buttons, function (btn) {
    btn.addEventListener("click", function () {
      btn.disabled = true;
      load(function (d) {
        var tiles = d[btn.getAttribute("data-shelf")];
        btn.disabled = false;
        if (!tiles || !tiles.length) { btn.remove(); return; }
        var rail = btn.parentNode ? btn.parentNode.querySelector(".nx-rail") : null;
        if (rail) rail.insertAdjacentHTML("beforeend", tiles.join(""));
        btn.remove();
      });
    });
  });
})();
