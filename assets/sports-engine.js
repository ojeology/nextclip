/* BRYME Match Engine v2 — self-updating boards + tables.
   <div data-sp-engine>…fallback…</div>  |  data-sp-league="premier-league"  |  data-sp-table="premier-league" */
(function () {
  "use strict";
  var LEAGUES = {
    "premier-league": { label: "Premier League", file: "fixtures.json", crest: "pl" },
    "serie-a": { label: "Serie A", file: "fixtures-serie-a.json", crest: "club" },
    "la-liga": { label: "La Liga", file: "fixtures-la-liga.json", crest: "club" },
    "bundesliga": { label: "Bundesliga", file: "fixtures-bundesliga.json", crest: "club" },
    "ligue-1": { label: "Ligue 1", file: "fixtures-ligue-1.json", crest: "club" }
  };
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function todayStr() { var d = new Date(); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
  function niceDate(iso) { var p = iso.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]).toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long" }); }
  function crest(lg, id) { var dir = LEAGUES[lg].crest === "pl" ? "/assets/img/sports/pl/" : "/assets/img/sports/"; return dir + (LEAGUES[lg].crest === "pl" ? id : "club-" + id) + ".svg"; }
  function card(lg, m, r) {
    var url = "/sports/" + lg + "/matches/" + m.id + "-vs-" + m.away + "/";
    var pill = r ? '<span class="sp-sc-pill ft">FT</span>' : '<span class="sp-sc-pill">' + esc(m.time || "TBC") + "</span>";
    var hn = r ? r.homeScore : "\u2013", an = r ? r.awayScore : "\u2013";
    return '<a class="sp-scorecard" href="' + url + '"><div class="sp-sc-top">' + pill +
      '<span class="sp-sc-go">' + (r ? "Result \u2192" : "Preview \u2192") + "</span></div><div>" +
      '<div class="sp-sc-row"><div class="sp-sc-club"><img src="' + crest(lg, m.id) + '" alt="" width="32" height="32" loading="lazy" decoding="async" onerror="this.style.display=\'none\'"><span>' + esc(m.homeName) + '</span></div><b class="sp-sc-num">' + hn + "</b></div>" +
      '<div class="sp-sc-row"><div class="sp-sc-club"><img src="' + crest(lg, m.away) + '" alt="" width="32" height="32" loading="lazy" decoding="async" onerror="this.style.display=\'none\'"><span>' + esc(m.awayName) + '</span></div><b class="sp-sc-num">' + an + "</b></div></div></a>";
  }
  function group(lg, items, results) {
    var cards = items.map(function (m) { return card(lg, m, results[lg + "/" + m.id + "-vs-" + m.away]); }).join("");
    return '<div class="sp-lg"><div class="sp-lg-head"><b>' + LEAGUES[lg].label + '</b><a href="/sports/' + lg + '/matches/">Match Centre \u2192</a></div><div class="sp-score-grid">' + cards + "</div></div>";
  }
  function computeTable(lg, matches, results) {
    var T = {};
    matches.forEach(function (m) {
      T[m.id] = T[m.id] || { name: m.homeName, p: 0, w: 0, d: 0, l: 0, gf: 0, ga: 0, pts: 0 };
      T[m.away] = T[m.away] || { name: m.awayName, p: 0, w: 0, d: 0, l: 0, gf: 0, ga: 0, pts: 0 };
      var r = results[lg + "/" + m.id + "-vs-" + m.away];
      if (!r) return;
      [[m.id, r.homeScore, r.awayScore], [m.away, r.awayScore, r.homeScore]].forEach(function (x) {
        var t = T[x[0]]; t.p++; t.gf += x[1]; t.ga += x[2];
        if (x[1] > x[2]) { t.w++; t.pts += 3; } else if (x[1] === x[2]) { t.d++; } else { t.l++; }
      });
    });
    return Object.keys(T).map(function (id) { T[id].id = id; return T[id]; })
      .sort(function (a, b) { return b.pts - a.pts || (b.gf - b.ga) - (a.gf - a.ga) || b.gf - a.gf || (a.name < b.name ? -1 : 1); });
  }
  function renderTable(lg, matches, results) {
    var rows = computeTable(lg, matches, results).map(function (x, i) {
      return "<tr><td>" + (i + 1) + "</td><td><b>" + esc(x.name) + "</b></td><td>" + x.p + "</td><td>" + x.w +
        "</td><td>" + x.d + "</td><td>" + x.l + "</td><td>" + x.gf + ":" + x.ga + "</td><td>" +
        (x.gf - x.ga > 0 ? "+" : "") + (x.gf - x.ga) + "</td><td><b>" + x.pts + "</b></td></tr>";
    }).join("");
    return '<div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>#</th><th>Team</th><th>P</th><th>W</th><th>D</th><th>L</th><th>Goals</th><th>GD</th><th>Pts</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
      '<p class="sp-result-meta">Live standings — recomputed from BRYME\u2019s verified results on every visit.</p>';
  }
  var DATA = null;
  function load() {
    if (DATA) return DATA;
    DATA = fetch("/content/results.json", { cache: "no-cache" }).then(function (r) { return r.json(); })
      .then(function (results) {
        var res = {};
        Object.keys(LEAGUES).forEach(function (lg) {
          Object.keys(results[lg] || {}).forEach(function (k) { res[lg + "/" + k] = results[lg][k]; });
        });
        return Promise.all(Object.keys(LEAGUES).map(function (lg) {
          return fetch("/content/" + LEAGUES[lg].file, { cache: "no-cache" })
            .then(function (r) { return r.json(); })
            .then(function (fx) { return { lg: lg, ms: (fx.matchweeks || []).reduce(function (a, w) { return a.concat(w.matches || []); }, []) }; });
        })).then(function (leagues) { return { results: res, leagues: leagues }; });
      });
    return DATA;
  }
  function boot() {
    var nodes = document.querySelectorAll("[data-sp-engine]");
    if (!nodes.length) return;
    load().then(function (data) {
      var today = todayStr();
      nodes.forEach(function (el) {
        var lgFilter = el.getAttribute("data-sp-league");
        var lgTable = el.getAttribute("data-sp-table");
        if (lgTable && LEAGUES[lgTable]) {
          var L = data.leagues.find(function (x) { return x.lg === lgTable; });
          if (L) { el.innerHTML = renderTable(lgTable, L.ms, data.results); el.setAttribute("data-sp-live", "1"); }
          return;
        }
        var played = [], upcoming = [], todays = [];
        data.leagues.forEach(function (L) {
          if (lgFilter && L.lg !== lgFilter) return;
          L.ms.forEach(function (m) {
            var r = data.results[L.lg + "/" + m.id + "-vs-" + m.away];
            if (m.date === today) todays.push({ lg: L.lg, m: m });
            else if (r) played.push({ lg: L.lg, m: m });
            else if (m.date > today) upcoming.push({ lg: L.lg, m: m });
          });
        });
        function byD(a, b) { return a.m.date < b.m.date ? -1 : a.m.date > b.m.date ? 1 : 0; }
        played.sort(function (a, b) { return -byD(a, b); }); upcoming.sort(byD);
        played = played.slice(0, lgFilter ? 9 : 12); upcoming = upcoming.slice(0, lgFilter ? 9 : 12);
        function section(title, arr, withDate) {
          if (!arr.length) return "";
          var html = '<div class="sp-board-head"><div><div class="eyebrow">Live desk</div><h2>' + title + "</h2></div>";
          if (withDate && arr[0].m.date) html += '<span class="sp-board-date">' + esc(niceDate(arr[0].m.date)) + "</span>";
          html += "</div>";
          var byLg = {};
          arr.forEach(function (b) { (byLg[b.lg] = byLg[b.lg] || []).push(b.m); });
          html += Object.keys(byLg).map(function (lg) { return group(lg, byLg[lg], data.results); }).join("");
          return html;
        }
        var out = section("Today", todays, false);
        out += section("Latest results", played, true);
        out += section("Next up", upcoming, true);
        if (out) { el.innerHTML = out; el.setAttribute("data-sp-live", "1"); }
      });
      document.querySelectorAll("[data-sp-date]").forEach(function (s) { s.textContent = niceDate(today); });
    }).catch(function () {});
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
