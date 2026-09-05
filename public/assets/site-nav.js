/* BRYME site chrome: easy slide-out sidebar + gently auto-scrolling section navs.
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

  /* ---------------- Moving section navs ---------------- */
  function setupNav(nav) {
    if (!nav || nav.dataset.moving) return;
    nav.dataset.moving = "1";
    var idle = null, dir = 1;

    function canScroll() { return nav.scrollWidth > nav.clientWidth + 2; }
    function start() {
      if (!canScroll()) return;
      nav.classList.add("is-moving");
      clearInterval(idle);
      idle = setInterval(function () {
        if (!canScroll()) return;
        /* slowly drift; bounce at the ends for a gentle "moving" feel */
        var next = nav.scrollLeft + dir * 0.4;
        if (next <= 0) { dir = 1; next = 0; }
        if (next >= nav.scrollWidth - nav.clientWidth) { dir = -1; }
        nav.scrollLeft = next;
      }, 24);
    }
    function stop() {
      clearInterval(idle); idle = null;
      nav.classList.remove("is-moving");
    }
    /* pause while the user interacts */
    ["pointerenter", "focusin", "touchstart"].forEach(function (ev) {
      nav.addEventListener(ev, stop, { passive: true });
    });
    ["pointerleave", "focusout", "touchend"].forEach(function (ev) {
      nav.addEventListener(ev, function () { start(); }, { passive: true });
    });
    start();
  }
  document.querySelectorAll(".section-nav").forEach(setupNav);
})();
