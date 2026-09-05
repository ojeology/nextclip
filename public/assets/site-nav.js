/* BRYME site chrome: slide-out sidebar + static section navs.
   External file (CSP disallows inline scripts). Progressive enhancement only. */
(function () {
  "use strict";

  /* ---------------- Easy sidebar (drawer) ---------------- */
  var drawer = document.getElementById("site-drawer");
  var backdrop = document.getElementById("drawer-backdrop");
  var toggles = document.querySelectorAll("[data-drawer-open]");
  var closers = document.querySelectorAll("[data-drawer-close]");

  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add("open");
    if (backdrop) backdrop.classList.add("show");
    document.body.classList.add("drawer-open");
    drawer.setAttribute("aria-hidden", "false");
    var first = drawer.querySelector("a,button");
    if (first && window.innerWidth > 640) first.focus();
  }
  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove("open");
    if (backdrop) backdrop.classList.remove("show");
    document.body.classList.remove("drawer-open");
    drawer.setAttribute("aria-hidden", "true");
  }

  toggles.forEach(function (b) { b.addEventListener("click", openDrawer); });
  closers.forEach(function (b) { b.addEventListener("click", closeDrawer); });
  if (backdrop) backdrop.addEventListener("click", closeDrawer);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeDrawer();
  });
  /* Close when a link inside is chosen. */
  if (drawer) {
    drawer.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (a) closeDrawer();
    });
  }

  /* ---------------- Section navs ----------------
     These bars are navigation, not decoration. They no longer drift on their
     own (that made text unreadable and moved links out from under the cursor).
     The only motion left is functional: bring the current page's link into
     view so "you are here" is visible on a narrow screen. */
  function setupNav(nav) {
    if (!nav || nav.dataset.navReady) return;
    nav.dataset.navReady = "1";
    var current = nav.querySelector('[aria-current="page"]');
    if (!current) return;
    if (nav.scrollWidth <= nav.clientWidth + 2) return;
    /* centre the active link without animating the page */
    var target = current.offsetLeft - (nav.clientWidth - current.offsetWidth) / 2;
    nav.scrollLeft = Math.max(0, target);
  }
  document.querySelectorAll(".section-nav").forEach(setupNav);
})();

