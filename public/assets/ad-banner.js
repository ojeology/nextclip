/* BRYME advertising experiment — single 300x250 placement per page (12 Sep 2026).
   Reusable component, loaded once from the shared footer template.
   Design rules (owner instruction, 12 Sep 2026):
   - ONE placement per page, inserted between content sections, never over content,
     navigation, forms or calculators.
   - The unit runs inside a fixed 300x250 iframe, so it cannot cover anything,
     overflow the viewport, or reflow editorial content.
   - Provider code embedded EXACTLY as supplied: key, format, dimensions, params
     and invoke URL are unaltered.
   - Failsafe: if the provider script is blocked (CSP or network), the slot
     removes itself so pages stay clean and fast.
   - No popunders, no redirects, no aggressive formats are created here. */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return; /* duplicate-load guard */
  window.__BRYME_AD__ = true;

  var PROVIDER_KEY = "51fc16f82ddc690721deee07bcd8bccd";
  var INVOKE_SRC = "https://www.highrevenueformat.com/" + PROVIDER_KEY + "/invoke.js";

  function init() {
    if (document.getElementById("bryme-ad-slot")) return;
    var main = document.querySelector("main") || document.body;

    var slot = document.createElement("div");
    slot.id = "bryme-ad-slot";
    slot.className = "bryme-ad";
    var label = document.createElement("div");
    label.className = "bryme-ad-label";
    label.textContent = "Advertisement";
    var frame = document.createElement("iframe");
    frame.id = "bryme-ad-300x250";
    frame.width = "300";
    frame.height = "250";
    frame.setAttribute("scrolling", "no");
    frame.setAttribute("frameborder", "0");
    frame.setAttribute("title", "Advertisement");
    slot.appendChild(label);
    slot.appendChild(frame);

    /* content ↓ ad ↓ more content: before the 3rd h2 when the page has one,
       before the 2nd on shorter pages, above the footer otherwise. */
    var h2s = main.querySelectorAll("h2");
    if (h2s.length >= 3) h2s[2].parentNode.insertBefore(slot, h2s[2]);
    else if (h2s.length === 2) h2s[1].parentNode.insertBefore(slot, h2s[1]);
    else {
      var f = document.querySelector("footer.foot");
      if (f) f.parentNode.insertBefore(slot, f); else main.appendChild(slot);
    }

    var css = document.createElement("style");
    css.textContent =
      ".bryme-ad{margin:30px auto;max-width:300px;text-align:center;overflow:hidden}" +
      ".bryme-ad-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
      "@media(max-width:340px){.bryme-ad iframe{transform:scale(.9);transform-origin:top center}}";
    document.head.appendChild(css);

    var d = frame.contentDocument || (frame.contentWindow && frame.contentWindow.document);
    if (!d) return;
    d.open();
    d.write(
      '<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">' +
      '<style>html,body{margin:0;padding:0;overflow:hidden}</style></head><body>' +
      "<script>atOptions = {\n" +
      "  'key' : '" + PROVIDER_KEY + "',\n" +
      "  'format' : 'iframe',\n" +
      "  'height' : 250,\n" +
      "  'width' : 300,\n" +
      "  'params' : {}\n" +
      "};<\/script>" +
      '<script src="' + INVOKE_SRC + '"><\/script>' +
      "</body></html>"
    );
    d.close();

    /* Failsafe: if the invoke script never rendered anything (blocked or down),
       collapse the slot. If the creative loaded cross-origin, leave it alone. */
    setTimeout(function () {
      try {
        var b = frame.contentDocument && frame.contentDocument.body;
        if (b && b.children.length === 0) slot.style.display = "none";
      } catch (e) { /* cross-origin access failure = creative is live */ }
    }, 5000);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
