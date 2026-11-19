/* Legacy-host guard: a bryme.onrender.com page bounces to the same path on
   thebryme.com. Inert on every other host — the real domain, localhost,
   preview hosts, staging copies. Built for the Bing Site Move
   (docs/LEGACY-HOST-MOVE.md) - deliberately permanent: inert unless the legacy
   host is ever re-enabled, and then it protects visitors from the duplicate
   immediately.

   2026-11-19: this used to be an ALLOWLIST of "known good" hosts (thebryme.com,
   www, localhost, 127.0.0.1, *.localhost), so every other hostname was treated
   as the legacy host. That is what broke previews of this repo: a preview
   serves the same pages from a proxy hostname, the guard fired, and the page
   navigated itself to https://thebryme.com — where the panel cannot frame it,
   so the preview went blank. The stated intent was always the legacy Render
   host, so it is now matched directly and everything else is a no-op. */
(function () {
  "use strict";
  var h = location.hostname;
  if (!(h === "onrender.com" || /\.onrender\.com$/i.test(h))) return;
  var to = "https://thebryme.com" + location.pathname + location.search + location.hash;
  try { window.location.replace(to); } catch (e) { window.location.href = to; }
})();
