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

  /* ---------- sports: top-five leagues ---------- */
  var leaguesCache = null;
  function loadLeagues() {
    if (leaguesCache) return Promise.resolve(leaguesCache);
    return apiGet("/api/sports/leagues").then(function (d) {
      if (d && d.leagues && d.leagues.length) leaguesCache = d;
      return d;
    });
  }
  function leagueCardHtml(l) {
    var rows = l.teams.slice(0, 3).map(function (t) {
      return '<span class="lg-row"><i>' + t.pos + "</i><b>" + esc(t.short) + "</b><em>" + t.pts + "</em></span>";
    }).join("");
    return '<a class="lg" href="#/league/' + encodeURIComponent(l.id) + '">' +
      '<span class="lg-top">' + l.flag + " <b>" + esc(l.name) + '</b><i>Table &amp; news →</i></span>' + rows + "</a>";
  }
  var KW_SKIP = { nice: 1, lens: 1, real: 1, city: 1, united: 1, monaco: 1 };
  function leagueNews(posts, league) {
    var kws = {};
    league.teams.forEach(function (t) {
      var k = (t.short || "").toLowerCase().trim();
      if (k && k.length > 2 && !KW_SKIP[k]) kws[k] = 1;
      k.split(/[^a-z0-9]+/).forEach(function (w) { if (w.length >= 4 && !KW_SKIP[w]) kws[w] = 1; });
    });
    var patterns = Object.keys(kws).map(function (k) {
      return new RegExp("\\b" + k.replace(/[^a-z0-9 ]/g, "").replace(/ /g, "\\s+") + "\\b");
    });
    return posts.filter(function (p) {
      var hay = (p.title + " " + (p.excerpt || "")).toLowerCase();
      return patterns.some(function (re) { return re.test(hay); });
    });
  }
  function pageSports() {
    setBack(true); markDock("sports");
    view.innerHTML =
      '<h1 class="pg">⚽ Sports</h1><p class="pg-sub">Top-five league tables and the latest from the desk.</p>' +
      '<div class="kick green">🏆 League tables</div><div id="lg-list"></div>' +
      '<div class="kick">Latest sports posts</div><div id="sp-posts"></div>';
    document.getElementById("lg-list").innerHTML = '<div class="skel"><i style="width:45%"></i><i></i></div><div class="skel"><i style="width:35%"></i><i></i></div>';
    document.getElementById("sp-posts").innerHTML = '<div class="skel"><i style="width:55%"></i><i></i></div>';
    loadLeagues().then(function (d) {
      document.getElementById("lg-list").innerHTML =
        ((d && d.leagues) || []).map(leagueCardHtml).join("") || '<p class="pg-sub">League tables will appear here shortly.</p>';
    }).catch(function () { document.getElementById("lg-list").innerHTML = ""; });
    apiGet("/api/posts/category/sports?limit=15").then(function (d) {
      document.getElementById("sp-posts").innerHTML =
        (d.posts || []).map(cardHtml).join("") || '<p class="pg-sub">Nothing new here yet — check back soon.</p>';
    }).catch(function () { document.getElementById("sp-posts").innerHTML = '<p class="pg-sub">Posts will appear here momentarily.</p>'; });
  }
  function pageLeague(id) {
    setBack(true); markDock("sports");
    skeletons(6);
    loadLeagues().then(function (d) {
      var l = ((d && d.leagues) || []).filter(function (x) { return x.id === id; })[0];
      if (!l) { stateBox("😕", "League not found.", "Back to all sports sections.", "⚽ Sports", "#/sports"); return; }
      var when = d.builtAt ? new Date(d.builtAt) : null;
      var whenStr = when && !isNaN(when.getTime()) ? when.toLocaleDateString(undefined, { day: "numeric", month: "short" }) : "";
      var rows = l.teams.map(function (t) {
        return '<div class="tbl-r' + (t.pos <= 4 ? " ucl" : "") + '"><i>' + t.pos + "</i>" +
          "<span>" + (t.logo ? '<img src="' + esc(t.logo) + '" alt="" loading="lazy">' : "") + esc(t.short) + "</span>" +
          "<b>" + t.p + "</b><b>" + t.w + "-" + t.d + "-" + t.l + "</b><b>" + esc(t.gd) + "</b><em>" + t.pts + "</em></div>";
      }).join("");
      view.innerHTML =
        '<a class="back" href="#/sports">← Sports</a>' +
        '<h1 class="pg">' + l.flag + " " + esc(l.name) + "</h1>" +
        '<p class="pg-sub">Standings' + (whenStr ? " · updated " + whenStr : "") + "</p>" +
        '<div class="tbl"><div class="tbl-r tbl-h"><i>#</i><span>Club</span><b>P</b><b>W-D-L</b><b>GD</b><em>Pts</em></div>' + rows + "</div>" +
        '<div id="lg-news"></div>';
      document.getElementById("lg-news").innerHTML = '<div class="skel"><i style="width:50%"></i><i></i></div>';
      apiGet("/api/posts/category/sports?limit=30").then(function (dp) {
        var news = leagueNews(dp.posts || [], l).slice(0, 6);
        document.getElementById("lg-news").innerHTML = news.length
          ? '<div class="kick green">📰 ' + esc(l.name) + " news</div>" + news.map(cardHtml).join("")
          : '<div class="kick green">📰 More from the desk</div><a class="card" href="#/sports"><span class="cat">⚽ Sports</span><b>All the latest BRYME sports posts</b><p>Every sports story, in one feed.</p></a>';
        monetize();
      }).catch(function () { document.getElementById("lg-news").innerHTML = ""; });
    }).catch(function () {
      stateBox("📡", "Couldn't load the table.", "Check your connection and try again.", "Retry");
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
    if (parts[0] === "league" && parts[1]) return pageLeague(decodeURIComponent(parts[1]));
    if (CATS[parts[0]]) { if (parts[0] === "sports") return pageSports(); return pageCategory(parts[0]); }
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
