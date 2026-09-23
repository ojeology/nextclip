/* Legacy-host guard: any bryme.onrender.com page bounces to the same path on
   thebryme.com. No-op on the real domain, localhost and previews. Built for
   the Bing Site Move (docs/LEGACY-HOST-MOVE.md) - deliberately permanent:
   inert unless the legacy host is ever re-enabled, and then it protects
   visitors from the duplicate immediately. */
(function () {
  "use strict";
  var h = location.hostname;
  if (h === "thebryme.com" || h === "www.thebryme.com") return;
  if (h === "localhost" || h === "127.0.0.1" || h.indexOf(".localhost") !== -1) return;
  var to = "https://thebryme.com" + location.pathname + location.search + location.hash;
  try { window.location.replace(to); } catch (e) { window.location.href = to; }
})();
