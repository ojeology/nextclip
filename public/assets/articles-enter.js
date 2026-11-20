/* ================================================================
   BRYME ARTICLES — the way in
   ----------------------------------------------------------------
   One job: when a reader taps the "Enter the article world" band on
   the house hub, the band sweeps and the page follows them in, so the
   section feels like a place you step into rather than a page that
   simply replaces the one you were on.

   Kept deliberately narrow:
   * it is a plain link underneath — no fetch, no history rewriting, so
     middle-click, ctrl-click, back/forward, sharing and the crawler all
     behave exactly as they would without this file;
   * the delay is 260ms, under the 300ms threshold where a navigation
     starts to feel sluggish, and the navigation is fired from a timer
     so a slow device cannot swallow it;
   * prefers-reduced-motion navigates immediately, with no animation;
   * if this file never loads, the link still works.

   Loaded only on the house hub, which is why it is separate from
   articles.js (that one runs inside the section).
   ================================================================ */
(function () {
  "use strict";

  var links = document.querySelectorAll("[data-articles-enter]");
  if (!links.length) return;

  var reduce = false;
  try {
    reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (e) { reduce = false; }

  function enter(link, ev) {
    /* Let the browser do its own thing for new-tab / new-window clicks. */
    if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey || ev.button !== 0) return;
    if (link.target && link.target !== "_self") return;
    if (reduce) return;                     /* straight there, no theatre */

    ev.preventDefault();
    link.classList.add("is-leaving");
    document.documentElement.classList.add("ba-leaving");

    var done = false;
    function go() {
      if (done) return;
      done = true;
      /* articles.js reads this on arrival and fades the section in. */
      try { window.sessionStorage.setItem("bryme.articles.entered", "1"); } catch (e) {}
      window.location.href = link.href;
    }
    window.setTimeout(go, 260);
    /* If the animation never fires (background tab, throttled device), the
       timer above still navigates. This is the belt, not the braces. */
    link.addEventListener("animationend", go, { once: true });
  }

  Array.prototype.forEach.call(links, function (link) {
    link.addEventListener("click", function (ev) { enter(link, ev); });
  });
})();
