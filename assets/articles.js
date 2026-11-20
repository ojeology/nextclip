/* ================================================================
   BRYME ARTICLES — editorial invitation + section analytics
   ----------------------------------------------------------------
   Two jobs, one small file, no dependencies, no build step.

   1. THE INVITATION. Ten seconds after a reader lands on the Writers
      desk home or the BRYME Articles landing page, a card offers one
      story. It is deliberately unambitious as an interface: no
      backdrop, no focus trap, no scroll lock, no new window, nothing
      that can stop a reader navigating or reading underneath it. The
      rules are configuration (assets/articles/invitation.json, built
      from content/articles/index.json):

        delaySeconds      never immediate — validated to be 5s or more
        maxPerSession     how many times one browser session may see it
        cooldownDays      how long a returning visitor is left alone
        article           null → nothing renders at all, ever

      It also refuses to appear while the reader is busy: another tab
      is focused, the menu drawer is open, another dialog is up, or the
      cursor is in the search field. It waits, three times, then leaves
      for that page view rather than interrupting.

   2. ANALYTICS. Everything is sent through the site's existing GA4
      property — there is no second analytics platform and no new
      library. Events are fire-and-forget and never block a click.

   Loaded only by the Writers desk home and BRYME Articles pages.
   ================================================================ */
(function () {
  "use strict";

  var PAYLOAD_URL = "/assets/articles/invitation.json";
  var RETRY_MS = 12000;
  var RETRIES = 3;

  /* ---------- storage that cannot throw (private mode, no cookies) ---------- */
  function store(kind) {
    try {
      var s = window[kind];
      var probe = "__ba_probe__";
      s.setItem(probe, "1");
      s.removeItem(probe);
      return s;
    } catch (e) {
      return null;
    }
  }
  var session = store("sessionStorage");
  var local = store("localStorage");

  function read(s, key) {
    if (!s) return null;
    try { return s.getItem(key); } catch (e) { return null; }
  }
  function write(s, key, value) {
    if (!s) return;
    try { s.setItem(key, String(value)); } catch (e) { /* full or blocked */ }
  }

  /* ---------- analytics through the existing GA4 tag ---------- */
  function track(name, params) {
    var body = params || {};
    body.page_path = window.location.pathname;
    try {
      if (typeof window.gtag === "function") window.gtag("event", name, body);
    } catch (e) { /* analytics must never break the page */ }
  }

  /* ---------- section state ---------- */
  var path = window.location.pathname.replace(/\/+$/, "") + "/";
  var metaEl = document.getElementById("ba-article-meta");
  var articleMeta = null;
  if (metaEl) {
    try { articleMeta = JSON.parse(metaEl.textContent); } catch (e) { articleMeta = null; }
  }

  function returningVisitor() {
    var first = read(local, "bryme.articles.firstSeen");
    if (!first) {
      write(local, "bryme.articles.firstSeen", Date.now());
      return false;
    }
    return true;
  }
  var RETURNING = returningVisitor();

  /* articles per session */
  function bumpSessionArticles() {
    var n = parseInt(read(session, "bryme.articles.sessionCount") || "0", 10) || 0;
    n += 1;
    write(session, "bryme.articles.sessionCount", n);
    return n;
  }

  /* ---------- link analytics ---------- */
  function surfaceOf(el) {
    if (!el) return "unknown";
    if (el.closest(".ba-invite")) return "invite";
    if (el.closest(".nav-articles")) return "nav";
    if (el.closest(".ba-ribbon")) return "desk-ribbon";
    if (el.closest(".drawer")) return "mobile-drawer";
    if (el.closest("#site-drawer")) return "mobile-drawer";
    if (el.closest(".ba-discover")) return "related";
    if (el.closest(".ba-reco")) return "recommendation";
    if (el.closest(".ba-cat-chips")) return "category-nav";
    if (el.closest(".ba-cat-list")) return "category-map";
    if (el.closest(".ba-card") || el.closest(".ba-featured")) return "card";
    return "inline";
  }

  document.addEventListener("click", function (ev) {
    var a = ev.target && ev.target.closest ? ev.target.closest("a[href]") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var target = "";
    try { target = new URL(a.href, window.location.origin).pathname; } catch (e) { target = href; }
    if (target.indexOf("/articles/") === -1) return;
    var surface = surfaceOf(a);
    /* The invitation's own CTA and headline carry their own handler (it also
       restarts the cooldown), so the delegated tracker leaves them alone —
       otherwise one click reports twice. */
    if (surface === "invite") return;
    if (surface === "related" || surface === "recommendation") {
      track("articles_related_click", { surface: surface, target: target });
      return;
    }
    var isStory = target.replace(/^\/writers/, "").split("/").filter(Boolean).length >= 2;
    track(isStory ? "articles_story_click" : "articles_nav_click", { surface: surface, target: target });
  }, true);

  /* ---------- page-level analytics ---------- */
  /* Arrival: assets/articles-enter.js on the house hub drops a flag before it
     navigates, so the section can settle into place instead of appearing. The
     class is added after first paint and animates transform/opacity only, so it
     costs nothing in LCP or CLS, and it is skipped for reduced-motion readers. */
  try {
    if (sessionStorage.getItem("bryme.articles.entered")) {
      sessionStorage.removeItem("bryme.articles.entered");
      var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (!reduce) document.documentElement.classList.add("ba-arrived");
    }
  } catch (e) { /* storage blocked: no transition, page is unaffected */ }

  var isLanding = /^\/writers\/articles\/$/.test(path);
  var isArticle = !!articleMeta;

  if (isLanding) {
    track("articles_landing_view", { returning: RETURNING });
  } else if (articleMeta) {
    track("articles_article_view", {
      slug: articleMeta.slug,
      category: articleMeta.category,
      reading_minutes: articleMeta.readingMinutes,
      returning: RETURNING,
      articles_this_session: bumpSessionArticles()
    });
  }

  /* ---------- the invitation ---------- */
  var timer = null;
  var shown = false;
  var retries = 0;
  var payload = null;

  function clearTimer() {
    if (timer) { window.clearTimeout(timer); timer = null; }
  }

  function busy() {
    if (document.hidden) return true;
    if (document.querySelector('#site-drawer[aria-hidden="false"]')) return true;
    /* Any other open dialog that does trap focus (the site drawer is checked
       above; it stays in the DOM with aria-modal="true" even when closed, so a
       blanket [role=dialog] test here would mean the invite never appears). */
    if (document.querySelector('dialog[open], [role="dialog"][aria-modal="true"]:not(#site-drawer):not([aria-hidden="true"]):not([hidden])')) return true;
    var el = document.activeElement;
    if (el && /^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName)) return true;
    return false;
  }

  function eligible(later) {
    var p = later || payload;
    if (!p || !p.enabled || !p.article) return false;
    if (!p.surfaces || p.surfaces.indexOf(path) === -1) return false;
    var shownThisSession = parseInt(read(session, p.storageKey + ".shown") || "0", 10) || 0;
    if (shownThisSession >= (p.maxPerSession || 1)) return false;
    if (p.cooldownDays > 0) {
      var last = parseInt(read(local, p.storageKey + ".last") || "0", 10) || 0;
      if (last && Date.now() - last < p.cooldownDays * 86400000) return false;
    }
    return true;
  }

  /* Counted once, at the impression: maxPerSession is a cap on impressions,
     not on the clicks that follow one. */
  function markShown(p) {
    var n = parseInt(read(session, p.storageKey + ".shown") || "0", 10) || 0;
    write(session, p.storageKey + ".shown", n + 1);
    markEngaged(p);
  }
  /* Restarts the cooldown clock for a returning visitor. */
  function markEngaged(p) {
    write(local, p.storageKey + ".last", Date.now());
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function build(p) {
    var a = p.article;
    var card = el("aside", "ba-invite");
    card.setAttribute("role", "dialog");
    card.setAttribute("aria-labelledby", "ba-invite-title");
    card.setAttribute("aria-describedby", "ba-invite-teaser");
    card.hidden = true;

    var fig = el("figure", "ba-invite-figure");
    var img = document.createElement("img");
    img.src = a.cover;
    img.alt = a.coverAlt;
    img.width = a.coverWidth;
    img.height = a.coverHeight;
    img.loading = "lazy";
    img.decoding = "async";
    fig.appendChild(img);

    var label = el("p", "ba-invite-label", a.label);
    fig.appendChild(label);

    var close = el("button", "ba-invite-close");
    close.type = "button";
    close.setAttribute("aria-label", "Close this story suggestion");
    close.innerHTML =
      '<svg aria-hidden="true" viewBox="0 0 24 24" width="14" height="14" fill="none" ' +
      'stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>';
    fig.appendChild(close);

    var body = el("div", "ba-invite-body");
    body.appendChild(el("p", "ba-invite-cat",
      a.category + " · " + a.readingMinutes + " min read"));
    var title = el("h2", "ba-invite-title");
    title.id = "ba-invite-title";
    var titleLink = document.createElement("a");
    titleLink.href = a.url;
    titleLink.textContent = a.headline;
    title.appendChild(titleLink);
    body.appendChild(title);

    var teaser = el("p", "ba-invite-teaser", a.teaser);
    teaser.id = "ba-invite-teaser";
    body.appendChild(teaser);

    var actions = el("div", "ba-invite-actions");
    var cta = document.createElement("a");
    cta.className = "ba-invite-cta";
    cta.href = a.url;               /* same tab: never a new window */
    cta.textContent = p.ctaLabel;
    actions.appendChild(cta);
    var later = el("button", "ba-invite-dismiss", p.dismissLabel);
    later.type = "button";
    actions.appendChild(later);
    body.appendChild(actions);
    body.appendChild(el("p", "ba-invite-note", p.asideLabel));

    card.appendChild(fig);
    card.appendChild(body);
    return card;
  }

  function dismiss(card, p, reason) {
    card.classList.remove("is-in");
    card.classList.add("is-out");
    window.setTimeout(function () {
      card.hidden = true;
      card.classList.remove("is-out");
    }, 240);
    markEngaged(p);
    track("articles_invite_dismiss", { reason: reason, slug: p.article ? slugOf(p) : "" });
  }

  function slugOf(p) {
    var parts = (p.article && p.article.url ? p.article.url : "").split("/").filter(Boolean);
    return parts.length ? parts[parts.length - 1] : "";
  }

  function show(p) {
    if (shown || !eligible(p)) return;
    if (busy()) {
      if (retries < RETRIES) {
        retries += 1;
        timer = window.setTimeout(function () { show(p); }, RETRY_MS);
        return;
      }
      return;   /* gave up for this page view; no impression counted */
    }
    shown = true;
    var card = build(p);
    document.body.appendChild(card);
    card.hidden = false;
    /* next frame, so the transition runs from the built state */
    window.requestAnimationFrame(function () { card.classList.add("is-in"); });

    card.querySelector(".ba-invite-close").addEventListener("click", function () {
      dismiss(card, p, "close");
    });
    card.querySelector(".ba-invite-dismiss").addEventListener("click", function () {
      dismiss(card, p, "maybe-later");
    });
    card.querySelector(".ba-invite-cta").addEventListener("click", function () {
      markEngaged(p);
      track("articles_invite_click", { surface: "invite", slug: slugOf(p) });
    });
    card.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") { dismiss(card, p, "escape"); }
    });

    markShown(p);
    track("articles_invite_impression", { slug: slugOf(p), delay_seconds: p.delaySeconds });
  }

  if ("fetch" in window) {
    fetch(PAYLOAD_URL, { credentials: "same-origin" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (p) {
        if (!p) return;
        /* The desk home is where the section is announced, so its visits are
           counted too — that is the top of the funnel the invitation works on. */
        if (p.surfaces && p.surfaces[0] === path && !articleMeta) {
          track("articles_desk_home_view", { returning: RETURNING });
        }
        if (!p.enabled || !p.article) return;   /* nothing live: no timer at all */
        payload = p;
        if (!eligible(p)) return;
        timer = window.setTimeout(function () { show(p); }, (p.delaySeconds || 10) * 1000);
      })
      .catch(function () { /* offline or blocked: the page is unaffected */ });
  }

  window.addEventListener("pagehide", clearTimer);
})();
