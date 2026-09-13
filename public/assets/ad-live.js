/* BRYME /ad-test/ copy - third twin under a NEVER-SERVED-BEFORE filename. */
(function () {
  "use strict";
  if (window.__BRYME_AD__) return;
  window.__BRYME_AD__ = true;

  var NATIVE_INVOKE = "https://pl31304018.profitableratecpmnetwork.com/ba9b1b5b135e5f465955aadf88ed0ad5/invoke.js";
  var NATIVE_CONTAINER = "container-ba9b1b5b135e5f465955aadf88ed0ad5";

  function init() {
    var slot = document.createElement("div");
    slot.className = "bryme-ad";
    var label = document.createElement("div");
    label.className = "bryme-ad-label";
    label.textContent = "Advertisement";
    slot.appendChild(label);
    var scr = document.createElement("script");
    scr.async = true;
    scr.setAttribute("data-cfasync", "false");
    scr.src = NATIVE_INVOKE;
    slot.appendChild(scr);
    var box = document.createElement("div");
    box.id = NATIVE_CONTAINER;
    box.className = "bryme-ad-ipp";
    slot.appendChild(box);
    var f = document.querySelector("footer.foot");
    if (f) f.parentNode.insertBefore(slot, f);
    else {
      var main = document.querySelector("main") || document.body;
      main.appendChild(slot);
    }

    var css = document.createElement("style");
    css.textContent =
      ".bryme-ad{margin:34px auto;max-width:340px;text-align:center;overflow:hidden}" +
      ".bryme-ad-label{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#8a94a6;margin-bottom:6px}" +
      ".bryme-ad-ipp{min-height:0}";
    document.head.appendChild(css);

    /* if the network sends nothing, the unit quietly removes itself */
    setTimeout(function () {
      var filled = false;
      try {
        filled = box.querySelectorAll("a, img, iframe").length > 0;
      } catch (e) { filled = true; }
      if (!filled) slot.remove();
    }, 25000);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
