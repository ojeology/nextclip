/* ==========================================================================
   BRYME SPORTS HUB — CINEMATIC GLASS runtime (loaded ONLY on /sports/)
   --------------------------------------------------------------------------
   Presentation only. Does NOT touch the live data engine (sports-engine.js),
   the league boards, routes, or any content. It adds:
     · a smooth, GPU-accelerated horizontal carousel for .sh-car rails
     · a gentle scroll parallax for the cinematic background
     · reduced-motion + visibility awareness so autoplay never annoys
   ========================================================================== */
(function () {
  "use strict";
  var REDUCED = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------------ *
   *  1. Horizontal carousel  (.sh-car  >  .sh-car-view  >  .sh-car-track)
   * ------------------------------------------------------------------ */
  function setupCarousel(root) {
    var view = root.querySelector(".sh-car-view");
    var track = root.querySelector(".sh-car-track");
    if (!view || !track) return;

    var slides = Array.prototype.slice.call(track.children);
    if (!slides.length) return;

    var prevBtn = root.querySelector(".sh-car-nav.prev");
    var nextBtn = root.querySelector(".sh-car-nav.next");
    var index = 0;
    var pos = 0;
    var dragging = false;
    var startX = 0;
    var startPos = 0;
    var moved = false;
    var autoTimer = null;
    var autoOn = !REDUCED;

    function gap() {
      var g = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap || 0);
      return isNaN(g) ? 16 : g;
    }
    function step() {
      var w = slides[0] ? slides[0].getBoundingClientRect().width : 0;
      return w + gap();
    }
    function maxIndex() {
      var w = track.scrollWidth || view.offsetWidth;
      var st = step();
      var n = Math.max(0, Math.floor((w - view.clientWidth) / st) + 1);
      return Math.max(0, n - 1);
    }
    function clamp(i) { return Math.max(0, Math.min(i, maxIndex())); }
    function render() {
      pos = index * step();
      track.style.transform = "translate3d(" + (-pos) + "px,0,0)";
      if (prevBtn) prevBtn.style.visibility = index > 0 ? "visible" : "hidden";
      if (nextBtn) nextBtn.style.visibility = index < maxIndex() ? "visible" : "hidden";
    }
    function go(i) { index = clamp(i); render(); }

    function stopAuto() { if (autoTimer) { clearInterval(autoTimer); autoTimer = null; } }
    function startAuto() {
      stopAuto();
      if (!autoOn || REDUCED || document.hidden) return;
      autoTimer = setInterval(function () {
        if (document.hidden || root.querySelector(":hover") && view === document.querySelector(".sh-car-view:active")) return;
        if (document.hidden) return;
        var mx = maxIndex();
        if (index >= mx) { go(0); } else { go(index + 1); }
      }, 4800);
    }

    render();
    startAuto();

    [view, prevBtn, nextBtn].forEach(function (el) {
      if (!el) return;
      ["mouseenter", "touchstart", "pointerdown"].forEach(function (ev) {
        el.addEventListener(ev, function () { stopAuto(); }, { passive: true });
      });
    });
    [view, prevBtn, nextBtn].forEach(function (el) {
      if (!el) return;
      ["mouseleave", "pointerup", "touchend"].forEach(function (ev) {
        el.addEventListener(ev, function () { if (!dragging) startAuto(); }, { passive: true });
      });
    });

    if (prevBtn) prevBtn.addEventListener("click", function () { go(index - 1); });
    if (nextBtn) nextBtn.addEventListener("click", function () { go(index + 1); });

    view.addEventListener("dragstart", function (e) { e.preventDefault(); });
    view.addEventListener("pointerdown", function (e) {
      dragging = true; moved = false;
      startX = e.clientX; startPos = index * step();
      view.style.transition = "none";
      view.setPointerCapture && e.pointerId != null && view.setPointerCapture(e.pointerId);
    });
    view.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      var dx = e.clientX - startX;
      if (Math.abs(dx) > 4) moved = true;
      pos = startPos - dx;
      if (pos < 0) pos = 0;
      track.style.transform = "translate3d(" + (-pos) + "px,0,0)";
    });
    function up() {
      if (!dragging) return;
      dragging = false;
      view.style.transition = "";
      index = clamp(Math.round(pos / step()));
      render();
      startAuto();
    }
    view.addEventListener("pointerup", up);
    view.addEventListener("pointercancel", up);
    view.addEventListener("click", function (e) {
      if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; }
    }, true);

    var rt;
    window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { index = clamp(index); render(); }, 120); });

    /* allow keyboard users to move the carousel */
    root.setAttribute("tabindex", "-1");
    var key = function (e) {
      if (e.key === "ArrowRight") { go(index + 1); }
      else if (e.key === "ArrowLeft") { go(index - 1); }
    };
    view.addEventListener("keydown", function (e) { if (!view.closest("[data-loop]")) key(e); });
  }

  function initCarousels() {
    document.querySelectorAll(".sh-car").forEach(setupCarousel);
  }

  /* ------------------------------------------------------------------ *
   *  2. Cinematic background parallax (subtle, GPU-friendly)
   * ------------------------------------------------------------------ */
  var bgPhoto = document.querySelector(".sh-bg-photo");
  var heroPhoto = document.querySelector(".sh-hero-photo");
  var ticking = false;
  function parallax() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      ticking = false;
      if (REDUCED || document.hidden) return;
      var y = window.scrollY || 0;
      if (bgPhoto) bgPhoto.style.transform = "translate3d(0," + (-y * 0.06) + "px,0) scale(1.04)";
      if (heroPhoto) heroPhoto.style.transform = "translate3d(0," + (-y * 0.12) + "px,0) scale(1.05)";
    });
  }
  window.addEventListener("scroll", parallax, { passive: true });

  /* ------------------------------------------------------------------ *
   *  3. Pause auto-sliding rails when the tab is hidden
   * ------------------------------------------------------------------ */
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) {
      document.documentElement.classList.add("sh-hidden");
    } else {
      document.documentElement.classList.remove("sh-hidden");
      initCarousels(); /* restart timers now that we are visible */
    }
  });

  /* ------------------------------------------------------------------ *
   *  boot
   * ------------------------------------------------------------------ */
  function boot() {
    initCarousels();
    parallax();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
