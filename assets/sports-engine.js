/* BRYME Match Engine — self-updating match board.
   Reads /content/results.json + league fixture files and renders Today,
   Latest results and Next fixtures using the site's own scorecard styles.
   Container: <div data-sp-engine>…static fallback…</div> */
(function () {
  "use strict";
  var LEAGUES = {
    "premier-league": { label: "Premier League", file: "fixtures.json", crest: "pl" },
    "serie-a": { label: "Serie A", file: "fixtures-serie-a.json", crest: "club" },
    "la-liga": { label: "La Liga", file: "fixtures-la-liga.json", crest: "club" },
    "bundesliga": { label: "Bundesliga", file: "fixtures-bundesliga.json", crest: "club" },
    "ligue-1": { label: "Ligue 1", file: "fixtures-ligue-1.json", crest: "club" }
  };
  var HOST = "https://bryme.onrender.com";

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function todayStr() {
    var d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }
  function niceDate(iso) {
    var p = iso.split("-");
    var d = new Date(+p[0], +p[1] - 1, +p[2]);
    return d.toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long" });
  }
  function crest(lg, id) {
    var dir = LEAGUES[lg].crest === "pl" ? "/assets/img/sports/pl/" : "/assets/img/sports/";
    var name = LEAGUES[lg].crest === "pl" ? id : "club-" + id;
    return dir + name + ".svg";
  }
  function card(lg, m, r) {
    var url = "/sports/" + lg + "/matches/" + m.id + "-vs-" + m.away + "/";
    var pill = r ? '<span class="sp-sc-pill ft">FT</span>'
                 : '<span class="sp-sc-pill">' + esc(m.time || "TBC") + "</span>";
    var go = r ? "Result \u2192" : "Preview \u2192";
    var hn = r ? r.homeScore : "\u2013";
    var an = r ? r.awayScore : "\u2013";
    return '<a class="sp-scorecard" href="' + url + '"><div class="sp-sc-top">' + pill +
      '<span class="sp-sc-go">' + go + "</span></div><div>" +
      '<div class="sp-sc-row"><div class="sp-sc-club"><img src="' + crest(lg, m.id) +
      '" alt="" width="32" height="32" loading="lazy" decoding="async" onerror="this.style.display=\'none\'"><span>' +
      esc(m.homeName) + '</span></div><b class="sp-sc-num">' + hn + "</b></div>" +
      '<div class="sp-sc-row"><div class="sp-sc-club"><img src="' + crest(lg, m.away) +
      '" alt="" width="32" height="32" loading="lazy" decoding="async" onerror="this.style.display=\'none\'"><span>' +
      esc(m.awayName) + '</span></div><b class="sp-sc-num">' + an + "</b></div></div></a>";
  }
  function group(lg, items, results) {
    var cards = items.map(function (m) {
      return card(lg, m, results[lg + "/" + m.id + "-vs-" + m.away]);
    }).join("");
    return '<div class="sp-lg"><div class="sp-lg-head"><b>' + LEAGUES[lg].label +
      '</b><a href="/sports/' + lg + '/matches/">Match Centre \u2192</a></div>' +
      '<div class="sp-score-grid">' + cards + "</div></div>";
  }

  function boot() {
    var el = document.querySelector("[data-sp-engine]");
    if (!el) return;
    fetch("/content/results.json", { cache: "no-cache" })
      .then(function (r) { return r.json(); })
      .then(function (results) {
        var reqs = Object.keys(LEAGUES).map(function (lg) {
          return fetch("/content/" + LEAGUES[lg].file, { cache: "no-cache" })
            .then(function (r) { return r.json(); })
            .then(function (fx) {
              return { lg: lg, ms: (fx.matchweeks || []).reduce(function (a, w) { return a.concat(w.matches || []); }, []) };
            });
        });
        return Promise.all(reqs).then(function (leagues) {
          var res = {};
          Object.keys(LEAGUES).forEach(function (lg) {
            Object.keys(results[lg] || {}).forEach(function (k) { res[lg + "/" + k] = results[lg][k]; });
          });
          var today = todayStr();
          var played = [], upcoming = [], todays = [];
          leagues.forEach(function (L) {
            L.ms.forEach(function (m) {
              var key = L.lg + "/" + m.id + "-vs-" + m.away;
              var isPlayed = !!res[key];
              var box = { lg: L.lg, m: m };
              if (m.date === today) todays.push(box);
              else if (isPlayed) played.push(box);
              else if (m.date > today) upcoming.push(box);
            });
          });
          played.sort(function (a, b) { return b.m.date < a.m.date ? -1 : b.m.date > a.m.date ? 1 : 0; });
          upcoming.sort(function (a, b) { return a.m.date < b.m.date ? -1 : 1; });
          played = played.slice(0, 12); upcoming = upcoming.slice(0, 12);

          function section(title, arr, showLeagueDate) {
            if (!arr.length) return "";
            var html = '<div class="sp-board-head"><div><div class="eyebrow">Live desk</div><h2>' + title + "</h2></div>";
            if (showLeagueDate && arr[0].m.date) html += '<span class="sp-board-date">' + esc(niceDate(arr[0].m.date)) + "</span>";
            html += "</div>";
            var byLg = {};
            arr.forEach(function (b) { (byLg[b.lg] = byLg[b.lg] || []).push(b.m); });
            html += Object.keys(byLg).map(function (lg) { return group(lg, byLg[lg], res); }).join("");
            return html;
          }
          var out = section("Today", todays, false);
          out += section("Latest results", played, true);
          out += section("Next up", upcoming, true);
          el.innerHTML = out;
          el.setAttribute("data-sp-live", "1");
          document.querySelectorAll("[data-sp-date]").forEach(function (s) {
            s.textContent = niceDate(today);
          });
        });
      })
      .catch(function () { /* keep static fallback */ });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
