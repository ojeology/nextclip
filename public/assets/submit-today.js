/* Submit today — the two conveniences that need script.
 *
 * 1. Copy the WhatsApp message that goes with the day's brief, so it can be
 *    pasted into a Status or a writing group instead of only opening wa.me.
 * 2. On the undated page, send a visitor to the dated page for *their* day when
 *    the build is older than today. The undated URL is the one that gets posted
 *    daily, so it has to keep meaning "today" even between rebuilds. A dated
 *    page never redirects (no loops), and the list of days is baked into the
 *    page, so this can only ever point at a page that exists.
 *
 * No storage, no network, no identifiers. If anything is missing, the page is
 * still complete: the message is in a textarea, and wa.me links work without JS.
 */
(function () {
  "use strict";

  // --- copy buttons -------------------------------------------------------
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-copy]");
    if (!btn) return;
    var target = document.querySelector(btn.getAttribute("data-copy"));
    if (!target) return;
    var text = target.value !== undefined ? target.value : target.textContent;
    var done = function () {
      var note = document.querySelector(btn.getAttribute("data-copy-note") || "");
      if (note) {
        note.hidden = false;
        setTimeout(function () { note.hidden = true; }, 2600);
      }
      var old = btn.getAttribute("data-label") || btn.textContent;
      btn.setAttribute("data-label", old);
      btn.textContent = "Copied";
      setTimeout(function () { btn.textContent = old; }, 2200);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () {
        if (target.select) { target.select(); }
      });
    } else if (target.select) {
      target.select();
      try { document.execCommand("copy"); done(); } catch (err) { /* selection is enough */ }
    }
  });

  // --- "this page means today" -------------------------------------------
  var root = document.querySelector("[data-st-today]");
  if (!root) return;
  if (/(^|\/)\d{4}-\d{2}-\d{2}\/$/.test(location.pathname)) return;

  var days = (root.getAttribute("data-st-days") || "").split(",").filter(Boolean);
  if (!days.length) return;
  var d = new Date();
  var today = d.getFullYear() + "-" +
              String(d.getMonth() + 1).padStart(2, "0") + "-" +
              String(d.getDate()).padStart(2, "0");
  if (days.indexOf(today) === -1) return;
  if (root.getAttribute("data-st-date") === today) return;
  location.replace(location.pathname.replace(/\/?$/, "/") + today + "/");
})();
