/* BRYME Mini App — hash router + Telegram WebApp integration.
 * Routes: #/home #/latest #/money #/tech #/sports #/movies #/trading #/internet #/comics #/article/:slug
 * Works inside Telegram and in a normal browser (dev). */
(function () {
  "use strict";

  /* ---------- Telegram context (safe) ---------- */
  var TG = (window.Telegram && window.Telegram.WebApp) || null;
  var inTelegram = Boolean(TG && TG.initData !== undefined && TG.platform && TG.platform !== "unknown");
  if (TG && TG.ready) TG.ready();
  if (TG && TG.expand) TG.expand();

  function haptic() { try { if (TG && TG.HapticFeedback) TG.HapticFeedback.impactOccurred("light"); } catch (e) {} }
  function setBack(show) {
    try {
      if (TG && TG.BackButton) {
        if (show) TG.BackButton.show(); else TG.BackButton.hide();
      }
    } catch (e) {}
  }

  /* ---------- API ---------- */
  var API = (function () {
    var q = new URLSearchParams(location.search).get("api");
    return (q || window.BRYME_API_BASE || "").replace(/\/+$/, "");
  })();
  function apiGet(path) {
    return fetch(API + path, { headers: { accept: "application/json" } }).then(function (r) {
      if (!r.ok && r.status === 404) { var e = new Error("not_found"); e.status = 404; throw e; }
      if (!r.ok) throw new Error("http_" + r.status);
      return r.json();
    });
  }

  /* ---------- helpers ---------- */
  var view = document.getElementById("view");
  var sheet = document.getElementById("sheet");
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function el(html) { var d = document.createElement("div"); d.innerHTML = html; return d.firstElementChild; }
  function skeletons(n) {
    var out = "";
    for (var i = 0; i < (n || 4); i++) out += '<div class="skel"><i style="width:40%"></i><i></i><i></i></div>';
    view.innerHTML = out;
  }
  function stateBox(emoji, title, sub, btnLabel, btnHref) {
    view.innerHTML = '<div class="state"><em>' + emoji + "</em><b>" + esc(title) + "</b><span>" + esc(sub || "") + "</span>" +
      (btnLabel ? '<a class="btn' + (btnHref ? "" : " ghost") + '" href="' + (btnHref || "#") + '" data-retry="1">' + esc(btnLabel) + "</a>" : "") + "</div>";
    var retry = view.querySelector("[data-retry]");
    if (retry && !btnHref) retry.addEventListener("click", function (e) { e.preventDefault(); route(); });
  }
  function slot(name) { return '<div class="mslot" data-monetization-slot="' + name + '"></div>'; }
  function monetize() {
    /* future: partners call window.BRYME_MONETIZE(slotEl, placement) */
    if (typeof window.BRYME_MONETIZE === "function") {
      document.querySelectorAll("[data-monetization-slot]").forEach(function (s) { window.BRYME_MONETIZE(s, s.getAttribute("data-monetization-slot")); });
    }
  }

  var CATS = {
    money: { label: "💰 Make Money", api: "money" },
    tech: { label: "🤖 Tech & AI", api: "tech" },
    sports: { label: "⚽ Sports", api: "sports" },
    movies: { label: "🎬 Movies & Anime", api: "entertainment" },
    trading: { label: "📈 Trading", api: "trading" },
    internet: { label: "🌐 Internet", api: "internet" },
    comics: { label: "😂 Comics", api: "comics" }
  };

  function cardHtml(p) {
    return '<a class="card" href="#/article/' + encodeURIComponent(p.slug) + '">' +
      '<span class="cat">' + esc(p.categoryLabel || "") + "</span>" +
      "<b>" + esc(p.title) + "</b>" +
      (p.excerpt ? "<p>" + esc(p.excerpt) + "</p>" : "") +
      '<span class="meta">' + esc((p.publishedAt || "BRYME") + (p.readingTime ? " · " + p.readingTime : "")) + "</span></a>";
  }

  function markDock(key) {
    document.querySelectorAll(".dock a").forEach(function (a) {
      a.classList.toggle("on", a.getAttribute("data-dock") === key);
    });
  }

  /* ---------- pages ---------- */
  function pageHome() {
    setBack(false); markDock("home");
    view.innerHTML =
      '<h1 class="pg">Discover what you love.</h1>' +
      '<p class="pg-sub">Money guides, Tech &amp; AI, Sports, Movies &amp; Anime — and the internet\'s useful corners. All inside Telegram.</p>' +
      slot("home-top") +
      '<div class="kick green">Explore</div><div class="grid" id="home-grid"></div>' +
      '<div class="kick">🆕 Latest on BRYME</div><div id="home-latest"></div>' + slot("home-bottom");
    var grid = document.getElementById("home-grid");
    Object.keys(CATS).forEach(function (k) {
      grid.appendChild(el('<a class="tile" href="#/' + k + '"><em>' + CATS[k].label.split(" ")[0] + "</em><b>" + esc(CATS[k].label.replace(/^\S+\s/, "")) + "</b><span>BRYME " + esc(CATS[k].label.replace(/^\S+\s/, "")) + "</span></a>"));
    });
    grid.appendChild(el('<a class="tile" href="#/latest"><em>🆕</em><b>Latest Posts</b><span>Everything new, one list</span></a>'));
    document.getElementById("home-latest").innerHTML = '<div class="skel"><i style="width:40%"></i><i></i></div><div class="skel"><i style="width:55%"></i><i></i></div>';
    apiGet("/api/posts/latest?limit=5").then(function (d) {
      document.getElementById("home-latest").innerHTML = (d.posts || []).map(cardHtml).join("") || "";
      monetize();
    }).catch(function () {
      document.getElementById("home-latest").innerHTML = '<p class="pg-sub">Latest posts will appear here momentarily.</p>';
    });
  }

  function pageCategory(key) {
    var c = CATS[key]; if (!c) return pageHome();
    setBack(true); markDock(key);
    view.innerHTML = '<h1 class="pg">' + esc(c.label) + '</h1><p class="pg-sub">The latest from the BRYME desk.</p>' + slot("cat-" + key + "-top");
    skeletons(5);
    apiGet("/api/posts/category/" + c.api + "?limit=15").then(function (d) {
      if (!(d.posts || []).length) {
        stateBox("🌱", "Nothing new here yet.", "Check back soon — or explore the latest posts.", "🆕 Latest Posts", "#/latest");
        return;
      }
      view.innerHTML = '<h1 class="pg">' + esc(c.label) + '</h1><p class="pg-sub">' + d.count + ' recent post' + (d.count === 1 ? "" : "s") + "</p>" +
        slot("cat-" + key + "-top") + d.posts.map(cardHtml).join("") + slot("cat-" + key + "-bottom");
      monetize();
    }).catch(function () {
      stateBox("📡", "Couldn't load this section.", "Check your connection and try again.", "Retry");
    });
  }

  function pageLatest() {
    setBack(true); markDock("");
    view.innerHTML = '<h1 class="pg">🆕 Latest Posts</h1><p class="pg-sub">The newest published BRYME stories.</p>';
    skeletons(6);
    apiGet("/api/posts/latest?limit=12").then(function (d) {
      view.innerHTML = '<h1 class="pg">🆕 Latest Posts</h1><p class="pg-sub">The newest published BRYME stories.</p>' +
        (d.posts || []).map(cardHtml).join("");
      monetize();
    }).catch(function () {
      stateBox("📡", "Couldn't load posts.", "Check your connection and try again.", "Retry");
    });
  }

  function pageArticle(slug) {
    setBack(true); markDock("");
    view.innerHTML = '<div class="skel"><i style="width:70%"></i><i></i><i></i><i></i><i style="width:50%"></i></div>';
    apiGet("/api/posts/" + encodeURIComponent(slug)).then(function (p) {
      view.innerHTML = '<article class="art">' +
        '<div class="kick green">' + esc(p.categoryLabel || "") + "</div>" +
        "<h1>" + esc(p.title) + "</h1>" +
        '<p class="meta">' + esc((p.author || "BRYME") + (p.publishedAt ? " · " + p.publishedAt : "") + (p.readingTime ? " · " + p.readingTime : "")) + "</p>" +
        slot("article-top") +
        (p.hasBody
          ? '<div class="art-body">' + p.body + "</div>"
          : '<p class="pg-sub">' + esc(p.excerpt || "") + "</p>" +
            '<a class="btn" href="' + esc(p.url) + '" target="_blank" rel="noopener">Open full guide on bryme.onrender.com</a>') +
        slot("article-bottom") +
        '</article><div class="kick">Keep reading</div><div id="art-more"></div>';
      document.getElementById("art-more").innerHTML = '<div class="skel"><i style="width:50%"></i><i></i></div>';
      monetize();
      apiGet("/api/posts/category/" + p.category + "?limit=4").then(function (d) {
        var more = (d.posts || []).filter(function (x) { return x.slug !== slug; }).slice(0, 3);
        document.getElementById("art-more").style.display = more.length ? "" : "none";
        document.getElementById("art-more").innerHTML = more.map(cardHtml).join("");
      }).catch(function () { document.getElementById("art-more").style.display = "none"; });
    }).catch(function (e) {
      if (e.status === 404) {
        stateBox("😕", "We couldn't find that article.", "Check the latest BRYME posts instead.", "🆕 Latest Posts", "#/latest");
      } else {
        stateBox("📡", "Couldn't load this article.", "Check your connection and try again.", "Retry");
      }
    });
  }

  /* ---------- router ---------- */
  function route() {
    var hash = (location.hash || "#/home").replace(/^#\/?/, "");
    var parts = hash.split("/").filter(Boolean);
    sheet.hidden = true;
    window.scrollTo(0, 0);
    if (!parts.length) return pageHome();
    if (parts[0] === "latest") return pageLatest();
    if (parts[0] === "article" && parts[1]) return pageArticle(decodeURIComponent(parts[1]));
    if (CATS[parts[0]]) return pageCategory(parts[0]);
    return pageHome();
  }
  window.addEventListener("hashchange", function () { haptic(); route(); });
  window.addEventListener("DOMContentLoaded", route);
  if (document.readyState !== "loading") route();

  /* back button (telegram + browser) */
  if (TG && TG.BackButton) {
    try {
      TG.BackButton.onClick(function () {
        if ((location.hash || "#/home") === "#/home" || location.hash === "") { setBack(false); try { TG.close(); } catch (e) {} }
        else { location.hash = "#/home"; }
      });
    } catch (e) {}
  }

  /* menu sheet */
  document.getElementById("btn-home").addEventListener("click", function () { haptic(); sheet.hidden = !sheet.hidden; });
  sheet.addEventListener("click", function (e) {
    var b = e.target.closest("button[data-go]");
    if (!b) return;
    sheet.hidden = true;
    location.hash = b.getAttribute("data-go");
  });
  document.addEventListener("click", function (e) { if (!e.target.closest("#sheet") && !e.target.closest("#btn-home")) sheet.hidden = true; });
})();
