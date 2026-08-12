/* NEXTCLIP frontend app: lazy trailers, share buttons, load-more,
   per-type category browsers (genre/year/country/language/sort) and global search.
   Written in ES5 for maximum compatibility. */
(function () {
  'use strict';
  var BASE = typeof window.NEXTCLIP_BASE !== 'undefined' ? window.NEXTCLIP_BASE : '';
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function cardHtml(m, typeDir) {
    var label = typeDir === 'series' ? 'SERIES' : (typeDir === 'anime' ? 'ANIME' : 'MOVIE');
    var genre = m.g || '';
    var rating = m.r != null ? '<p class="tile-rating" title="NEXTCLIP editorial score">★ ' + m.r + '/10 · Editorial</p>' : '';
    var img = m.p ? '<img loading="lazy" src="' + esc(m.p) + '" alt="' + esc(m.t) + ' trailer thumbnail">' : '<div class="placeholder">' + esc(m.t) + '</div>';
    return '<a class="tile" href="' + BASE + '/' + typeDir + '/' + esc(m.s) + '/"><div class="poster">' + img + '</div><h3>' + esc(m.t) + '</h3><div class="tile-meta"><span class="type-badge tb-' + typeDir + '">' + label + '</span><span>' + (m.y || '') + '</span>' + (genre ? '<span class="sep">·</span><span>' + esc(genre) + '</span>' : '') + '</div>' + rating + '</a>';
  }

  /* ---------- share buttons ---------- */
  document.querySelectorAll('[data-share-path]').forEach(function (button) {
    button.addEventListener('click', function () {
      var link = BASE + button.getAttribute('data-share-path');
      var title = button.getAttribute('data-share-title') || document.title;
      if (navigator.share) { navigator.share({ title: title, url: link }).catch(function () {}); return; }
      if (navigator.clipboard) {
        navigator.clipboard.writeText(link).then(function () { button.textContent = 'Link copied'; });
      }
    });
  });

  /* ---------- lazy trailer players (multi-candidate, failure-safe) ---------- */
  var TRAILER_WATCHDOG_MS = (typeof window.NEXTCLIP_TRAILER_TIMEOUT !== 'undefined') ? window.NEXTCLIP_TRAILER_TIMEOUT : 30000;
  function frameHtml(id, title) {
    var iframe = document.createElement('iframe');
    var src = 'https://www.youtube-nocookie.com/embed/' + id + '?rel=0&modestbranding=1&playsinline=1&enablejsapi=1';
    // The origin parameter helps the IFrame API deliver events; only set it
    // when the page has a real http(s) origin (sandboxed previews don't).
    if (/^https?:\/\//i.test(window.location.origin || '')) src += '&origin=' + encodeURIComponent(window.location.origin);
    iframe.src = src;
    iframe.title = title + ' trailer';
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    return iframe;
  }
  document.querySelectorAll('[data-trailer-box]').forEach(function (box) {
    var candidates = [];
    try { candidates = JSON.parse(box.getAttribute('data-trailer-candidates')); } catch (e) { candidates = []; }
    if (!candidates.length) return;
    var title = box.getAttribute('data-trailer-title') || 'Movie';
    var index = 0;
    var current = candidates[index];
    var failTimer = null;
    var playerUp = false; // iframe finished loading (player page is up)

    function clearWatchdog() { if (failTimer) { clearTimeout(failTimer); failTimer = null; } }

    function showError() {
      clearWatchdog();
      var frame = box.querySelector('[data-trailer-id]');
      if (frame && frame.parentNode) frame.parentNode.removeChild(frame);
      var err = box.querySelector('[data-trailer-error]');
      if (err) {
        var watch = err.querySelector('[data-trailer-watch]');
        if (watch && current) watch.setAttribute('href', current.watch);
        err.hidden = false;
      }
      var alt = box.querySelector('[data-trailer-alt]');
      if (alt) alt.hidden = !(candidates.length > 1);
      var fb = box.querySelector('.trailer-fallback');
      if (fb) fb.hidden = true;
    }
    function play() {
      if (!current || !/^[A-Za-z0-9_-]{11}$/.test(current.id)) { showError(); return; }
      var err = box.querySelector('[data-trailer-error]');
      if (err) err.hidden = true;
      var frame = box.querySelector('[data-trailer-id]');
      if (!frame) return;
      playerUp = false;
      frame.innerHTML = '';
      var iframe = frameHtml(current.id, title);
      // PRIMARY readiness signal: the iframe's own load event. It fires in
      // every browser without needing the YouTube JS API, and once the
      // player page has loaded the video is in the user's hands — the
      // watchdog must NEVER fire after this, no matter how slow the stream.
      iframe.addEventListener('load', function () { playerUp = true; clearWatchdog(); });
      frame.appendChild(iframe);
      clearWatchdog();
      failTimer = setTimeout(function () { if (!playerUp) showError(); }, TRAILER_WATCHDOG_MS);
    }
    // Secondary signal: YouTube IFrame API postMessages. With enablejsapi=1
    // these report real errors (embedding blocked, video removed mid-play)
    // and confirm the player is alive.
    function onMessage(e) {
      var d = e.data;
      if (!d || typeof d !== 'object' || !d.event) return;
      if (d.event === 'onError') { showError(); }
      else if (d.event === 'onReady' || d.event === 'onStateChange' || d.event === 'infoDelivery') { playerUp = true; clearWatchdog(); }
    }
    window.addEventListener('message', onMessage);
    function render() {
      current = candidates[index];
      var frame = box.querySelector('[data-trailer-id]');
      if (frame) {
        frame.hidden = false;
        frame.setAttribute('data-trailer-id', current.id);
        frame.innerHTML = '<img loading="lazy" src="https://i.ytimg.com/vi/' + current.id + '/hqdefault.jpg" alt="' + title + ' trailer thumbnail"><button type="button" class="trailer-play">Play trailer</button>';
      }
      var err = box.querySelector('[data-trailer-error]');
      if (err) err.hidden = true;
      var fb = box.querySelector('.trailer-fallback');
      if (fb) { fb.hidden = false; fb.innerHTML = 'If the embedded player is unavailable, <a href="' + current.watch + '" target="_blank" rel="noopener">watch the trailer on YouTube</a>.'; }
      var alt = box.querySelector('[data-trailer-alt]');
      if (alt) alt.hidden = !(candidates.length > 1);
      var badge = box.querySelector('.trailer-status');
      if (badge) {
        var isFan = current.type === 'fan-made';
        badge.className = 'trailer-status ' + (isFan ? 't-fan' : 't-ok');
        badge.textContent = (isFan ? '🟡 ' : '🟢 ') + (current.label || 'Trailer');
      }
      var meta = box.querySelector('.trailer-meta');
      if (meta) meta.textContent = current.channel ? 'YouTube · via ' + current.channel : 'YouTube';
      var disc = box.querySelector('.trailer-disclaimer');
      if (disc) disc.hidden = !isFan;
      playerUp = false;
      clearWatchdog();
      var playBtn = frame && frame.querySelector('.trailer-play');
      if (playBtn) playBtn.addEventListener('click', play);
    }
    var playBtn = box.querySelector('.trailer-play');
    if (playBtn) playBtn.addEventListener('click', play);
    var altBtn = box.querySelector('[data-trailer-alt]');
    if (altBtn) altBtn.addEventListener('click', function () { index = (index + 1) % candidates.length; render(); });
    var retryBtn = box.querySelector('[data-trailer-retry]');
    if (retryBtn) retryBtn.addEventListener('click', function () {
      var err = box.querySelector('[data-trailer-error]');
      if (err) err.hidden = true;
      var frame = box.querySelector('[data-trailer-id]');
      if (!frame) {
        // re-create the frame if the error card removed it
        var head = box.querySelector('.trailer-head');
        if (head && head.nextSibling) {
          var fr = document.createElement('div');
          fr.className = 'trailer-frame';
          fr.setAttribute('data-trailer-id', current.id);
          fr.innerHTML = '<img loading="lazy" src="https://i.ytimg.com/vi/' + current.id + '/hqdefault.jpg" alt="' + title + ' trailer thumbnail"><button type="button" class="trailer-play">Play trailer</button>';
          box.insertBefore(fr, head.nextSibling);
        }
      }
      var p2 = box.querySelector('.trailer-play');
      if (p2) p2.addEventListener('click', play);
      play();
    });
  });

  /* ---------- trailer admin audit table (/trailers/) ---------- */
  var taData = document.getElementById('trailer-admin-data');
  if (taData) {
    var T = [];
    try { T = JSON.parse(taData.textContent); } catch (e) {}
    var taBody = document.getElementById('ta-body');
    var taFilter = document.getElementById('ta-filter');
    var taQ = document.getElementById('ta-q');
    function taTag(status) {
      if (status === 'official') return '<span class="tr-tag ok">OFFICIAL</span>';
      if (status === 'fan-made') return '<span class="tr-tag fan">COMMUNITY</span>';
      return '<span class="tr-tag miss">NO TRAILER</span>';
    }
    function taRender() {
      var q = (taQ ? taQ.value : '').trim().toLowerCase();
      var f = taFilter ? taFilter.value : '';
      var rows = T.filter(function (r) {
        if (f && r.status !== f) return false;
        if (q && (r.title + ' ' + r.slug).toLowerCase().indexOf(q) === -1) return false;
        return true;
      });
      taBody.innerHTML = rows.map(function (r) {
        return '<tr><td><b>' + esc(r.title) + '</b><br><span style="color:var(--muted);font-size:11px">' + esc(r.slug) + ' · ' + esc(r.typeDir) + '</span></td>' +
          '<td>' + taTag(r.status) + '</td>' +
          '<td>' + esc(r.label || '—') + '</td>' +
          '<td>' + (r.videoId ? '<code>' + esc(r.videoId) + '</code>' : '—') + (r.candidates && r.candidates.length > 1 ? '<br><span style="color:var(--muted);font-size:10px">+' + (r.candidates.length - 1) + ' more</span>' : '') + '</td>' +
          '<td>' + esc(r.channel || '—') + '</td>' +
          '<td>' + (r.verified ? '✓' : '—') + '</td>' +
          '<td>' + esc(r.lastChecked || '—') + '</td></tr>';
      }).join('') || '<tr><td colspan="7" style="color:var(--muted)">No titles match.</td></tr>';
    }
    if (taFilter) taFilter.addEventListener('change', taRender);
    if (taQ) taQ.addEventListener('input', taRender);
    taRender();
  }

  /* ---------- load-more (server-rendered grids) ---------- */
  document.querySelectorAll('[data-load-more]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.more-tile[hidden]').forEach(function (el) { el.hidden = false; });
      if (btn.parentNode) btn.parentNode.removeChild(btn);
    });
  });

  /* ---------- category browser (/movies/, /series/, /anime/) ---------- */
  var dataEl = document.getElementById('catalogue-data');
  if (dataEl) {
    var meta, items;
    try { var parsed = JSON.parse(dataEl.textContent); meta = parsed; items = parsed.items || []; } catch (e) { items = []; }
    if (items.length) {
      var typeDir = meta.type || 'movie';
      var grid = document.querySelector('[data-cards]');
      var countLine = document.querySelector('[data-count]');
      var bar = document.querySelector('[data-filterbar]');
      var sortEl = document.getElementById('f-sort');
      var genreEl = document.getElementById('f-genre');
      var yearEl = document.getElementById('f-year');
      var countryEl = document.getElementById('f-country');
      var languageEl = document.getElementById('f-language');
      var serverButton = document.querySelector('[data-load-more]');
      var state = { sort: 'popular', genre: '', year: '', country: '', language: '', shown: 40 };
      var PER_PAGE = 40;

      function applyFilters() {
        var out = items.slice();
        if (state.genre) out = out.filter(function (m) { return (m.genreSlug || m.gs || []).indexOf(state.genre) > -1 || m.g === state.genre; });
        if (state.year) out = out.filter(function (m) { return String(m.y) === state.year; });
        if (state.country) out = out.filter(function (m) { return m.c === state.country; });
        if (state.language) out = out.filter(function (m) { return m.l === state.language; });
        if (state.sort === 'popular') out.sort(function (a, b) { return (b.r || 0) - (a.r || 0) || (b.y || 0) - (a.y || 0) || a.t.localeCompare(b.t); });
        else if (state.sort === 'newest') out.sort(function (a, b) { return (b.y || 0) - (a.y || 0) || a.t.localeCompare(b.t); });
        else out.sort(function (a, b) { return a.t.localeCompare(b.t); });
        return out;
      }
      function render() {
        var out = applyFilters();
        var total = out.length;
        var slice = out.slice(0, state.shown);
        grid.innerHTML = slice.map(function (m) { return cardHtml(m, typeDir); }).join('');
        if (countLine) countLine.textContent = out.length === items.length
          ? items.length + ' ' + (meta.typeLabel || typeDir).toLowerCase() + ' in the catalogue'
          : total + ' of ' + items.length + ' ' + (meta.typeLabel || typeDir).toLowerCase() + ' match your filters';
        if (serverButton && serverButton.parentNode) serverButton.parentNode.removeChild(serverButton);
        if (total > state.shown) {
          var btn = document.createElement('button');
          btn.className = 'loadmore';
          btn.type = 'button';
          btn.textContent = 'Show more (' + (total - state.shown) + ' remaining)';
          btn.addEventListener('click', function () { state.shown += PER_PAGE; render(); });
          grid.parentNode.insertBefore(btn, grid.nextSibling);
        } else {
          var old = grid.parentNode.querySelector('.loadmore');
          if (old) old.parentNode.removeChild(old);
        }
      }
      function syncUrl() {
        var p = new URLSearchParams();
        if (state.sort !== 'popular') p.set('sort', state.sort);
        if (state.genre) p.set('genre', state.genre);
        if (state.year) p.set('year', state.year);
        if (state.country) p.set('country', state.country);
        if (state.language) p.set('language', state.language);
        var qs = p.toString();
        var kept = location.search.replace(/^\?/, '').split('&').filter(function (x) { return x && !/^(sort|genre|year|country|language)=/.test(x); });
        var next = qs ? '?' + qs + (kept.length ? '&' + kept.join('&') : '') : (kept.length ? '?' + kept.join('&') : '');
        try { history.replaceState(null, '', next); } catch (e) {}
      }
      function readUrl() {
        try {
          var p = new URLSearchParams(location.search);
          if (p.get('sort')) state.sort = p.get('sort');
          if (p.get('genre')) state.genre = p.get('genre');
          if (p.get('year')) state.year = p.get('year');
          if (p.get('country')) state.country = p.get('country');
          if (p.get('language')) state.language = p.get('language');
        } catch (e) {}
        if (sortEl) sortEl.value = state.sort;
        if (genreEl) genreEl.value = state.genre;
        if (yearEl) yearEl.value = state.year;
        if (countryEl) countryEl.value = state.country;
        if (languageEl) languageEl.value = state.language;
      }
      function bind() {
        var change = function () {
          state.sort = sortEl ? sortEl.value : 'popular';
          state.genre = genreEl ? genreEl.value : '';
          state.year = yearEl ? yearEl.value : '';
          state.country = countryEl ? countryEl.value : '';
          state.language = languageEl ? languageEl.value : '';
          state.shown = PER_PAGE;
          render(); syncUrl();
        };
        [sortEl, genreEl, yearEl, countryEl, languageEl].forEach(function (el) { if (el) el.addEventListener('change', change); });
        var clear = bar && bar.querySelector('[data-clear]');
        if (clear) clear.addEventListener('click', function () {
          state = { sort: 'popular', genre: '', year: '', country: '', language: '', shown: PER_PAGE };
          if (sortEl) sortEl.value = 'popular';
          [genreEl, yearEl, countryEl, languageEl].forEach(function (el) { if (el) el.value = ''; });
          render(); syncUrl();
        });
      }
      readUrl(); bind(); render();
    }
  }

  /* ---------- global search ---------- */
  var searchData = document.getElementById('search-data');
  if (searchData) {
    var S = { movies: [], articles: [], topics: [] };
    try { S = JSON.parse(searchData.textContent); } catch (e) {}
    var qEl = document.getElementById('search-q');
    var statusEl = document.getElementById('search-status');
    var resultsEl = document.getElementById('search-results');
    var tabEls = Array.prototype.slice.call(document.querySelectorAll('#search-tabs .stabs'));
    var activeTab = 'all';
    var lastQ = '';

    function rowHtml(href, title, meta) {
      return '<a class="row" href="' + href + '"><div><b>' + esc(title) + '</b><span class="meta" style="font-size:12px;color:var(--muted)">' + esc(meta) + '</span></div></a>';
    }
    function match(item, tokens, fields) {
      var hay = fields.map(function (f) { return String(item[f] == null ? '' : (Array.isArray(item[f]) ? item[f].join(' ') : item[f])).toLowerCase(); }).join(' ');
      return tokens.every(function (t) { return hay.indexOf(t) > -1; });
    }
    function render() {
      var q = qEl.value.trim().toLowerCase();
      if (!q) {
        resultsEl.innerHTML = '';
        statusEl.textContent = 'Start typing to search movies, TV series, anime and articles.';
        return;
      }
      var tokens = q.split(/\s+/).filter(Boolean);
      var foundM = S.movies.filter(function (m) { return match(m, tokens, ['title', 'genre', 'genres', 'country', 'language', 'year']); });
      if (activeTab === 'movie' || activeTab === 'series' || activeTab === 'anime') {
        foundM = foundM.filter(function (m) { return m.type === activeTab; });
      }
      var foundA = S.articles.filter(function (a) { return match(a, tokens, ['title', 'description', 'category', 'tags']); });
      var foundT = (S.topics || []).filter(function (t) { return match(t, tokens, ['title', 'description']); });
      var showM = activeTab === 'all' || activeTab === 'movie' || activeTab === 'series' || activeTab === 'anime';
      var showA = activeTab === 'all' || activeTab === 'article';
      var showT = activeTab === 'all';
      var html = '';
      var total = 0;
      if (showM && foundM.length) {
        total += foundM.length;
        html += '<div class="search-group">' + (activeTab === 'movie' ? 'Movies' : activeTab === 'series' ? 'Series' : activeTab === 'anime' ? 'Anime' : 'Titles') + ' (' + foundM.length + ')</div>';
        html += foundM.slice(0, 30).map(function (m) {
          var g = (m.genres && m.genres.length) ? m.genres[0] : (m.genre || '');
          return cardHtml({ s: m.slug, t: m.title, y: m.year, g: g, p: m.poster || '', r: null }, m.type || 'movie');
        }).join('');
      }
      if (showA && foundA.length) {
        total += foundA.length;
        html += '<div class="search-group">Articles (' + foundA.length + ')</div>';
        html += foundA.slice(0, 12).map(function (a) { return rowHtml(BASE + '/article/' + esc(a.slug) + '/', a.title, a.category + ' · ' + a.description.slice(0, 100)); }).join('');
      }
      if (showT && foundT.length) {
        total += foundT.length;
        html += '<div class="search-group">Topics (' + foundT.length + ')</div>';
        html += foundT.slice(0, 6).map(function (t) { return rowHtml(BASE + '/topic/' + esc(t.slug) + '/', t.title, t.description.slice(0, 100)); }).join('');
      }
      statusEl.textContent = total ? total + ' result' + (total === 1 ? '' : 's') + ' for “' + qEl.value.trim() + '”' : 'No matches for “' + qEl.value.trim() + '” — try another title, genre, country or year.';
      resultsEl.innerHTML = html || '<p style="color:var(--muted)">Nothing matched. Try “Dune”, “crime”, “Nigeria” or “2024”.</p>';
    }
    tabEls.forEach(function (tab) {
      tab.addEventListener('click', function () {
        activeTab = tab.getAttribute('data-tab');
        tabEls.forEach(function (t) { t.classList.toggle('active', t === tab); });
        render();
      });
    });
    var debounce;
    qEl.addEventListener('input', function () {
      clearTimeout(debounce);
      debounce = setTimeout(function () {
        var p = new URLSearchParams(); p.set('q', qEl.value);
        try { history.replaceState(null, '', '?q=' + encodeURIComponent(qEl.value)); } catch (e) {}
        render();
      }, 120);
    });
    try {
      var init = new URLSearchParams(location.search).get('q');
      if (init) { qEl.value = init; render(); }
    } catch (e) {}
  }
})();
