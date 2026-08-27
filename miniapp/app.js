/* BRYME Mini App — "quick-access dashboard".
 * Website = full library. Mini App = fast dashboard. Same backend content.
 * Router: hash routes (single system):
 *   #/home #/latest #/money #/tech #/sports #/sports-news #/movies #/trading
 *   #/internet #/comics #/article/:slug #/comp/:id
 * Deep links arrive in TWO carriers — hash (primary) and ?r= (fallback) —
 * plus Telegram native startapp params (tgWebAppStartParam / start_param). */
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
      if (TG && TG.BackButton) { if (show) TG.BackButton.show(); else TG.BackButton.hide(); }
    } catch (e) {}
  }

  /* ---------- deep-link boot (the fix for "everything opens Home") ---------- */
  /* Bot buttons carry ?r=<route> AND #/<route>. If the fragment is dropped by
   * the Telegram webview, ?r= still carries the destination. startapp params
   * (t.me deep links) are honoured too. Resolve ONCE before first route. */
  function normalizeDest(s) {
    s = String(s == null ? "" : s).trim().replace(/^#?\/?/, "");
    if (!s) return "";
    var parts = s.split("/").filter(Boolean).map(function (x) { return x.replace(/[^a-zA-Z0-9\-_]/g, ""); });
    return parts.join("/");
  }
  (function bootDeepLink() {
    if (/^#\/.+/.test(location.hash || "")) return; /* fragment survived — router reads it */
    var q = new URLSearchParams(location.search);
    var dest = normalizeDest(q.get("r") || q.get("section") || q.get("startapp") || q.get("tgWebAppStartParam") || "");
    if (!dest) {
      try { if (TG && TG.initDataUnsafe && TG.initDataUnsafe.start_param) dest = normalizeDest(TG.initDataUnsafe.start_param); } catch (e) {}
    }
    if (dest) location.replace("#/" + dest);
  })();

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
    if (typeof window.BRYME_MONETIZE === "function") {
      document.querySelectorAll("[data-monetization-slot]").forEach(function (s) { window.BRYME_MONETIZE(s, s.getAttribute("data-monetization-slot")); });
    }
  }
  function backBar(href, label) {
    return '<a class="back" href="' + href + '">← ' + esc(label || "Back") + "</a>";
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

  /* ---------- navigation stack (Telegram back button) ---------- */
  var navStack = [];
  var prevHash = "";
  function goBack() {
    while (navStack.length && navStack[navStack.length - 1] === location.hash) navStack.pop();
    location.hash = navStack.pop() || "#/home";
  }

  /* ---------- HOME: "What are you looking for?" ---------- */
  function pageHome() {
    setBack(false); markDock("home");
    view.innerHTML =
      '<h1 class="pg">🔥 BRYME</h1>' +
      '<p class="pg-sub">What are you looking for?</p>' +
      slot("home-top") +
      '<div class="grid big" id="home-grid"></div>' +
      '<div class="kick green">🔥 Trending now</div><div id="home-trend"></div>' +
      '<div class="kick">🆕 Latest</div><div id="home-latest"></div>' + slot("home-bottom");
    var grid = document.getElementById("home-grid");
    Object.keys(CATS).forEach(function (k) {
      grid.appendChild(el('<a class="tile" href="#/' + k + '"><em>' + CATS[k].label.split(" ")[0] + "</em><b>" +
        esc(CATS[k].label.replace(/^\S+\s/, "").toUpperCase()) + "</b></a>"));
    });
    document.getElementById("home-trend").innerHTML = '<div class="skel"><i style="width:45%"></i><i></i></div>';
    document.getElementById("home-latest").innerHTML = '<div class="skel"><i style="width:55%"></i><i></i></div>';
    /* Trending = the newest story from four different desks (real posts, no fake popularity). */
    apiGet("/api/posts/latest?limit=30").then(function (d) {
      var seen = {}, picks = [];
      (d.posts || []).forEach(function (p) {
        if (picks.length < 4 && !seen[p.category] && p.category !== "trading" && p.category !== "internet") {
          seen[p.category] = 1; picks.push(p);
        }
      });
      document.getElementById("home-trend").innerHTML = picks.map(cardHtml).join("") ||
        '<p class="pg-sub">Stories will appear here momentarily.</p>';
      monetize();
    }).catch(function () {
      document.getElementById("home-trend").innerHTML = '<p class="pg-sub">Stories will appear here momentarily.</p>';
    });
    apiGet("/api/posts/latest?limit=5").then(function (d) {
      document.getElementById("home-latest").innerHTML = (d.posts || []).map(cardHtml).join("");
      monetize();
    }).catch(function () {
      document.getElementById("home-latest").innerHTML = '<p class="pg-sub">Latest posts will appear here momentarily.</p>';
    });
  }

  /* ---------- section hubs (money / tech / movies / internet / trading / comics) ---------- */
  var HUBS = {
    money: {
      title: "💰 MAKE MONEY", sub: "Practical ways to earn — checked by the desk.", api: "money",
      featured: "writing",
      chips: [
        ["🔥 Opportunities", /opportunit|make-money-online|beginners-guide|income-skills|microtask|online-services|platform-review|affiliate/i],
        ["✍️ Writing", /writing|content-creation|field-notes/i],
        ["💻 Freelancing", /freelanc|remote-work/i],
        ["🤖 AI & Work", /ai-assisted|outlier|mindrift|prolific/i],
        ["📱 Apps & Websites", /website-monet|coding|digital-products|online-business/i]
      ]
    },
    tech: {
      title: "🤖 TECH & AI", sub: "Tools and guides that actually save time.", api: "tech",
      chips: [
        ["🔥 AI Tools", /ai-tools|ai-assistant|ai-coding|arena-ai|chatgpt|claude|deepseek|gemini/i],
        ["🆕 Latest AI", /new-tech|vs-chatgpt|deepseek|gemini|arena-ai/i],
        ["💻 Apps", /android-app|streaming-app|app-alternative|photopea|pixlr|polotno|plasfy|notion|bitwarden|signal|lyra/i],
        ["🌐 Websites", /useful-website|hosting|website-building|internet-tools/i],
        ["📱 Android", /android|termux|phone/i],
        ["🧠 AI Guides", /ai-tutorial|beginner-coding|automation|productivity/i]
      ]
    },
    movies: {
      title: "🎬 ENTERTAINMENT", sub: "Movies, series and anime — what to watch next.", api: "entertainment",
      chips: [
        ["🔥 Trending", /./],
        ["🎥 Movies", /movie|interstellar|dune|nolan|alien|parasite|cinema|thriller/i],
        ["🍿 Series", /series|shows|breaking-bad|prison-break|squid|borderland|badlands|season/i],
        ["🇯🇵 Anime", /anime|one-piece|naruto|solo-leveling|eren|hunter-x/i]
      ]
    },
    internet: { title: "🌐 INTERNET", sub: "The useful corners of the web.", api: "internet" },
    trading: { title: "📈 TRADING", sub: "Learn the craft before the charts.", api: "trading" },
    comics: { title: "😂 COMICS", sub: "The matchweek, drawn.", api: "comics" }
  };

  function featuredCard(p) {
    return '<a class="feat" href="#/article/' + encodeURIComponent(p.slug) + '">' +
      (p.image ? '<img class="feat-img" src="' + esc(p.image) + '" alt="" loading="lazy">' : "") +
      '<span class="feat-kick">🔥 Featured</span><b>' + esc(p.title) + "</b>" +
      (p.excerpt ? "<p>" + esc(p.excerpt) + "</p>" : "") +
      '<span class="feat-cta">Read now →</span></a>';
  }

  function pageHub(key) {
    var hub = HUBS[key];
    setBack(true); markDock(key);
    view.innerHTML =
      '<h1 class="pg">' + esc(hub.title) + "</h1>" +
      '<p class="pg-sub">' + esc(hub.sub) + "</p>" +
      slot("hub-" + key + "-top") +
      '<div id="hub-featured"></div>' +
      '<div class="chips" id="hub-chips" hidden></div>' +
      '<div id="hub-feed"></div>' + slot("hub-" + key + "-bottom");
    document.getElementById("hub-feed").innerHTML = '<div class="skel"><i style="width:50%"></i><i></i></div><div class="skel"><i style="width:40%"></i><i></i></div>';
    document.getElementById("hub-featured").innerHTML = '<div class="skel"><i style="width:35%"></i><i></i><i></i></div>';

    apiGet("/api/posts/category/" + hub.api + "?limit=30").then(function (d) {
      var posts = d.posts || [];
      if (!posts.length) {
        view.innerHTML = "";
        stateBox("🌱", "Nothing new here yet.", "Check back soon — or explore the latest posts.", "🆕 Latest Posts", "#/latest");
        return;
      }
      /* featured: referenced by slug, fetched from the same API (no duplicated content) */
      var f = document.getElementById("hub-featured");
      if (hub.featured) {
        var pick = posts.filter(function (p) { return p.slug === hub.featured; })[0] || posts[0];
        f.innerHTML = featuredCard(pick);
      } else f.innerHTML = "";

      /* chips: only subsections that actually contain posts */
      var active = 0;
      var chips = (hub.chips || []).map(function (c, i) {
        return { label: c[0], re: c[1], i: i, n: posts.filter(function (p) { return c[1].test(p.slug + " " + p.title); }).length };
      }).filter(function (c) { return c.n > 0; });
      var bar = document.getElementById("hub-chips");
      if (chips.length > 1) {
        bar.hidden = false;
        chips.forEach(function (c, idx) {
          bar.appendChild(el('<button class="chip' + (idx === 0 ? " on" : "") + '" type="button" data-i="' + c.i + '">' + c.label + "</button>"));
        });
        bar.addEventListener("click", function (e) {
          var b = e.target.closest("button.chip"); if (!b) return;
          haptic();
          bar.querySelectorAll(".chip").forEach(function (x) { x.classList.remove("on"); });
          b.classList.add("on");
          active = Number(b.getAttribute("data-i"));
          renderFeed();
        });
      }
      function renderFeed() {
        var re = chips.length ? chips.filter(function (c) { return c.i === active; })[0] : null;
        var list = re && re.re ? posts.filter(function (p) { return re.re.test(p.slug + " " + p.title); }) : posts;
        document.getElementById("hub-feed").innerHTML = list.map(cardHtml).join("") ||
          '<div class="state" style="padding:24px 12px"><b>Nothing in this subsection yet.</b></div>';
      }
      renderFeed();
      monetize();
    }).catch(function () {
      stateBox("📡", "Couldn't load this section.", "Check your connection and try again.", "Retry");
    });
  }

  /* ---------- SPORTS ---------- */
  var compsCache = null;
  function loadComps() {
    if (compsCache) return Promise.resolve(compsCache);
    return apiGet("/api/sports/competitions").then(function (d) {
      if (d && d.competitions && d.competitions.length) compsCache = d;
      return d;
    });
  }

  function compCardHtml(c) {
    var line = "";
    var lineLogos = "";
    if (c.fixtures && c.fixtures.length) {
      var f = c.fixtures[0];
      line = "Next: " + f.hshort + " vs " + f.ashort + " · " + f.date;
      lineLogos = (f.hlogo ? '<img src="' + esc(f.hlogo) + '" alt="" loading="lazy">' : "") +
        '<i>vs</i>' + (f.alogo ? '<img src="' + esc(f.alogo) + '" alt="" loading="lazy">' : "");
    } else if (c.scores && c.scores.length) {
      var s = c.scores[0];
      line = s.hshort + " " + s.hs + "–" + s.as + " " + s.ashort + " · " + s.date;
      lineLogos = (s.hlogo ? '<img src="' + esc(s.hlogo) + '" alt="" loading="lazy">' : "") +
        '<b>' + s.hs + "–" + s.as + "</b>" + (s.alogo ? '<img src="' + esc(s.alogo) + '" alt="" loading="lazy">' : "");
    } else if (c.scorers && c.scorers.length) {
      line = "Top scorer: " + c.scorers[0].name + " · " + c.scorers[0].goals + " goals";
      lineLogos = c.scorers[0].logo ? '<img src="' + esc(c.scorers[0].logo) + '" alt="" loading="lazy">' : "";
    } else if (c.teams.reduce(function (n, t) { return n + (t.pts || 0); }, 0) > 0) {
      line = c.teams[0].short + " lead the table · " + (c.teams[0].pts || 0) + " pts";
      lineLogos = c.teams[0].logo ? '<img src="' + esc(c.teams[0].logo) + '" alt="" loading="lazy">' : "";
    } else {
      line = "Season starting — table fills automatically.";
    }
    return '<a class="lg" href="#/comp/' + encodeURIComponent(c.id) + '">' +
      '<span class="lg-top">' + c.flag + " <b>" + esc(c.name) + "</b><i>→</i></span>" +
      (lineLogos ? '<span class="lg-strip">' + lineLogos + "</span>" : "") +
      '<span class="lg-next">' + esc(line) + "</span></a>";
  }

  function pageSports() {
    setBack(true); markDock("sports");
    view.innerHTML =
      '<h1 class="pg">⚽ SPORTS</h1>' +
      '<p class="pg-sub">Tables, scores, fixtures — and the BRYME desk.</p>' +
      '<div class="kick green">🏆 Competitions</div><div id="sp-comps"></div>' +
      '<div class="kick">🔥 BRYME Sports</div>' +
      '<a class="card row-card" href="#/sports-news"><span class="cat">📰</span><b>Latest News</b><p>Every BRYME sports story, newest first.</p></a>' +
      '<a class="card row-card" href="#/comics"><span class="cat">😂</span><b>Matchweek Comics</b><p>The weekend\'s storylines, drawn.</p></a>' +
      '<div class="kick">📰 Latest posts</div><div id="sp-posts"></div>';
    document.getElementById("sp-comps").innerHTML = '<div class="skel"><i style="width:40%"></i><i></i></div><div class="skel"><i style="width:35%"></i><i></i></div>';
    document.getElementById("sp-posts").innerHTML = '<div class="skel"><i style="width:55%"></i><i></i></div>';
    loadComps().then(function (d) {
      document.getElementById("sp-comps").innerHTML =
        ((d && d.competitions) || []).map(compCardHtml).join("") || '<p class="pg-sub">Competitions will appear here shortly.</p>';
    }).catch(function () { document.getElementById("sp-comps").innerHTML = ""; });
    apiGet("/api/posts/category/sports?limit=15").then(function (d) {
      document.getElementById("sp-posts").innerHTML = (d.posts || []).map(cardHtml).join("") || '<p class="pg-sub">Nothing new here yet — check back soon.</p>';
    }).catch(function () { document.getElementById("sp-posts").innerHTML = '<p class="pg-sub">Posts will appear here momentarily.</p>'; });
  }

  function pageSportsNews() {
    setBack(true); markDock("sports");
    view.innerHTML = '<h1 class="pg">📰 SPORTS NEWS</h1><p class="pg-sub">Every BRYME sports story, newest first.</p>';
    skeletons(5);
    apiGet("/api/posts/category/sports?limit=15").then(function (d) {
      var posts = d.posts || [];
      if (!posts.length) { stateBox("🌱", "Nothing new here yet.", "Check back soon.", "⚽ Sports", "#/sports"); return; }
      view.innerHTML = backBar("#/sports", "Sports") + '<h1 class="pg">📰 SPORTS NEWS</h1><p class="pg-sub">' + posts.length + ' stories from the desk.</p>' + posts.map(cardHtml).join("");
    }).catch(function () { stateBox("📡", "Couldn't load posts.", "Check your connection and try again.", "Retry"); });
  }

  var KW_SKIP = { nice: 1, lens: 1, real: 1, city: 1, united: 1, monaco: 1 };
  function leagueNews(posts, comp) {
    var kws = {};
    comp.teams.forEach(function (t) {
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

  function tableHtml(comp) {
    var rows = comp.teams.map(function (t) {
      return '<div class="tbl-r' + (t.pos <= 4 ? " ucl" : "") + '"><i>' + t.pos + "</i>" +
        "<span>" + (t.logo ? '<img src="' + esc(t.logo) + '" alt="" loading="lazy">' : "") + esc(t.short) + "</span>" +
        "<b>" + t.p + "</b><b>" + t.w + "-" + t.d + "-" + t.l + "</b><b>" + esc(t.gd) + "</b><em>" + t.pts + "</em></div>";
    }).join("");
    return '<div class="tbl"><div class="tbl-r tbl-h"><i>#</i><span>Club</span><b>P</b><b>W-D-L</b><b>GD</b><em>Pts</em></div>' + rows + "</div>";
  }
  function scoresHtml(comp) {
    if (!comp.scores || !comp.scores.length) return '<div class="empty">No completed matches in the last few days.</div>';
    return comp.scores.map(function (s) {
      return '<div class="score">' +
        '<span class="s-team">' + (s.hlogo ? '<img src="' + esc(s.hlogo) + '" alt="" loading="lazy">' : "") + esc(s.hshort) + "</span>" +
        '<span class="s-num">' + s.hs + "–" + s.as + "</span>" +
        '<span class="s-team away">' + esc(s.ashort) + (s.alogo ? '<img src="' + esc(s.alogo) + '" alt="" loading="lazy">' : "") + "</span>" +
        '<span class="s-date">' + esc(s.date) + "</span></div>";
    }).join("");
  }
  function fixturesHtml(comp) {
    if (!comp.fixtures || !comp.fixtures.length) return '<div class="empty">No fixtures in the next week.</div>';
    return comp.fixtures.map(function (f) {
      return '<div class="fixt">' +
        '<span class="f-when">' + esc(f.date) + (f.time ? " · " + esc(f.time) : "") + "</span>" +
        '<span class="f-teams"><img src="' + esc(f.hlogo) + '" alt="" loading="lazy">' + esc(f.hshort) + " <i>vs</i> " + esc(f.ashort) + '<img src="' + esc(f.alogo) + '" alt="" loading="lazy"></span></div>';
    }).join("");
  }
  function scorersHtml(comp) {
    if (comp.scorers && comp.scorers.length) {
      return comp.scorers.map(function (s, i) {
        return '<div class="fixt"><span class="f-when">#' + (i + 1) + " · " + s.goals + " goal" + (s.goals === 1 ? "" : "s") + "</span>" +
          '<span class="f-teams">' + (s.logo ? '<img src="' + esc(s.logo) + '" alt="" loading="lazy">' : "") + esc(s.name) + " <i>" + esc(s.team || "") + (s.apps ? " · " + s.apps + " apps" : "") + "</i></span></div>";
      }).join("");
    }
    if (comp.scores && comp.scores.length) return '<div class="empty">No scoring data yet for this competition.</div>';
    return '<div class="empty">⚽ Season starting — top scorers appear here automatically once matches are played.</div>';
  }

  function pageComp(id) {
    setBack(true); markDock("sports");
    skeletons(6);
    loadComps().then(function (d) {
      var c = ((d && d.competitions) || []).filter(function (x) { return x.id === id; })[0];
      if (!c) { stateBox("😕", "Competition not found.", "Back to all sports sections.", "⚽ Sports", "#/sports"); return; }
      var when = d.builtAt ? new Date(d.builtAt) : null;
      var whenStr = when && !isNaN(when.getTime()) ? when.toLocaleDateString(undefined, { day: "numeric", month: "short" }) : "";
      var tabs = [["table", "📊 Table"], ["scores", "⚽ Scores"], ["fixtures", "📅 Fixtures"], ["scorers", "🥇 Scorers"], ["news", "📰 News"]];

      function pane(tab) {
        if (tab === "table") return tableHtml(c);
        if (tab === "scores") return scoresHtml(c);
        if (tab === "fixtures") return fixturesHtml(c);
        if (tab === "scorers") return scorersHtml(c);
        /* news */
        var out = '<div id="comp-news"><div class="skel"><i style="width:50%"></i><i></i></div></div>';
        return out;
      }
      function fillCompNews() {
        apiGet("/api/posts/category/sports?limit=30").then(function (dp) {
          var node = document.getElementById("comp-news");
          if (!node) return;
          var posts = dp.posts || [];
          var news = leagueNews(posts, c).slice(0, 6);
          if (news.length) { node.innerHTML = news.map(cardHtml).join(""); return; }
          /* honest fallback: no club-matched stories yet — list real sports posts */
          node.innerHTML = '<div class="empty">No ' + esc(c.name) + ' stories yet — latest from the desk:</div>' +
            posts.slice(0, 4).map(cardHtml).join("");
        }).catch(function () {
          var node = document.getElementById("comp-news");
          if (node) node.innerHTML = '<div class="empty">News will appear here momentarily.</div>';
        });
      }
      function mount(active) {
        view.innerHTML =
          backBar("#/sports", "Sports") +
          '<h1 class="pg">' + c.flag + " " + esc(c.name).toUpperCase() + "</h1>" +
          '<p class="pg-sub">Standings, scores and fixtures' + (whenStr ? " · updated " + whenStr : "") + "</p>" +
          '<div class="seg">' + tabs.map(function (t) {
            return '<button class="seg-b' + (t[0] === active ? " on" : "") + '" type="button" data-tab="' + t[0] + '">' + t[1] + "</button>";
          }).join("") + "</div>" +
          '<div class="seg-pane" id="seg-pane"></div>';
        document.getElementById("seg-pane").innerHTML = pane(active);
        if (active === "news") fillCompNews();
      }
      mount("table");
      view.querySelector(".seg").addEventListener("click", function (e) {
        var b = e.target.closest("button.seg-b"); if (!b) return;
        haptic();
        view.querySelectorAll(".seg-b").forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        document.getElementById("seg-pane").innerHTML = pane(b.getAttribute("data-tab"));
        if (b.getAttribute("data-tab") === "news") fillCompNews();
      });
    }).catch(function () {
      stateBox("📡", "Couldn't load the competition.", "Check your connection and try again.", "Retry");
    });
  }

  /* ---------- latest + article ---------- */
  function pageLatest() {
    setBack(true); markDock("");
    view.innerHTML = '<h1 class="pg">🆕 LATEST</h1><p class="pg-sub">The newest published BRYME stories.</p>';
    skeletons(6);
    apiGet("/api/posts/latest?limit=12").then(function (d) {
      var posts = d.posts || [];
      if (!posts.length) { stateBox("🌱", "Nothing published yet.", "Check back soon.", "🏠 Home", "#/home"); return; }
      view.innerHTML = '<h1 class="pg">🆕 LATEST</h1><p class="pg-sub">The newest published BRYME stories.</p>' + posts.map(cardHtml).join("");
      monetize();
    }).catch(function () { stateBox("📡", "Couldn't load posts.", "Check your connection and try again.", "Retry"); });
  }

  function pageArticle(slug) {
    setBack(true); markDock("");
    view.innerHTML = '<div class="skel"><i style="width:70%"></i><i></i><i></i><i></i><i style="width:50%"></i></div>';
    apiGet("/api/posts/" + encodeURIComponent(slug)).then(function (p) {
      view.innerHTML = backBar("#", "Back") +
        '<article class="art">' +
        '<div class="kick green">' + esc(p.categoryLabel || "") + "</div>" +
        "<h1>" + esc(p.title) + "</h1>" +
        '<p class="meta">' + esc((p.author || "BRYME") + (p.publishedAt ? " · " + p.publishedAt : "") + (p.readingTime ? " · " + p.readingTime : "")) + "</p>" +
        slot("article-top") +
        (p.hasBody
          ? '<div class="art-body">' + p.body + "</div>"
          : '<p class="pg-sub">' + esc(p.excerpt || "") + "</p>" +
            '<a class="btn" href="' + esc(/^https?:/.test(p.url) ? p.url : "https://bryme.onrender.com" + p.url) + '" target="_blank" rel="noopener">Open the full guide on bryme.onrender.com</a>') +
        slot("article-bottom") +
        '</article><div class="kick">Keep reading</div><div id="art-more"></div>';
      var back = view.querySelector(".back");
      back.addEventListener("click", function (e) {
        e.preventDefault();
        if (navStack.length > 1) { navStack.pop(); location.hash = navStack[navStack.length - 1]; }
        else goBack();
      });
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

  /* ---------- router (single system) ---------- */
  var HUB_KEYS = ["money", "tech", "movies", "trading", "internet", "comics"];
  function route() {
    var hash = (location.hash || "#/home").replace(/^#\/?/, "");
    var parts = hash.split("/").filter(Boolean);
    sheet.hidden = true;
    window.scrollTo(0, 0);
    if (!parts.length) return pageHome();
    if (parts[0] === "latest") return pageLatest();
    if (parts[0] === "article" && parts[1]) return pageArticle(decodeURIComponent(parts[1]));
    if (parts[0] === "comp" && parts[1]) return pageComp(decodeURIComponent(parts[1]));
    if (parts[0] === "sports") return pageSports();
    if (parts[0] === "sports-news") return pageSportsNews();
    if (parts[0] === "home") return pageHome();
    if (HUB_KEYS.indexOf(parts[0]) > -1) return pageHub(parts[0]);
    return pageHome();
  }
  window.addEventListener("hashchange", function () {
    haptic();
    if (prevHash && prevHash !== location.hash) navStack.push(prevHash);
    if (navStack.length > 24) navStack.shift();
    prevHash = location.hash;
    route();
  });
  window.addEventListener("DOMContentLoaded", function () { prevHash = location.hash || "#/home"; route(); });
  if (document.readyState !== "loading") { prevHash = location.hash || "#/home"; route(); }

  /* back button (telegram + in-app) */
  if (TG && TG.BackButton) {
    try {
      TG.BackButton.onClick(function () {
        if ((location.hash || "#/home") === "#/home" || location.hash === "") { setBack(false); try { TG.close(); } catch (e) {} }
        else goBack();
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
