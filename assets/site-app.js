/* BRYME frontend app: lazy trailers, share buttons, load-more,
   per-type category browsers (genre/year/country/language/sort) and global search.
   Written in ES5 for maximum compatibility. */
(function () {
  'use strict';
  var BASE = typeof window.BRYME_BASE !== 'undefined' ? window.BRYME_BASE : '';
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function cardHtml(m, typeDir) {
    var label = typeDir === 'series' ? 'SERIES' : (typeDir === 'anime' ? 'ANIME' : 'MOVIE');
    var genre = m.g || '';
    var rating = m.r != null ? '<p class="tile-rating" title="BRYME editorial score">★ ' + m.r + '/10 · Editorial</p>' : '';
    var img = m.p ? '<img loading="lazy" src="' + esc(m.p) + '" alt="' + esc(m.t) + ' trailer thumbnail">' : '<div class="placeholder">' + esc(m.t) + '</div>';
    return '<a class="tile" href="' + BASE + '/' + typeDir + '/' + esc(m.s) + '/"><div class="poster">' + img + '</div><h3>' + esc(m.t) + '</h3><div class="tile-meta"><span class="type-badge tb-' + typeDir + '">' + label + '</span><span>' + (m.y || '') + '</span>' + (genre ? '<span class="sep">·</span><span>' + esc(genre) + '</span>' : '') + '</div>' + rating + '</a>';
  }

  /* ---------- theme toggle, back-to-top, scroll progress, / shortcut ---------- */
  var SUN_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
  var MOON_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }
  function applyTheme(t) {
    var m = document.querySelector('meta[name=theme-color]');
    if (t === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
      document.documentElement.style.colorScheme = 'light';
      if (m) m.setAttribute('content', '#f4f5f7');
    } else {
      document.documentElement.removeAttribute('data-theme');
      document.documentElement.style.colorScheme = '';
      if (m) m.setAttribute('content', '#08090b');
    }
  }
  function themeBtnIcon(t) { return t === 'light' ? MOON_SVG : SUN_SVG; }
  var header = document.querySelector('.top-tools') || document.querySelector('.top .shell');
  var themeBtn = null;
  if (header) {
    themeBtn = document.createElement('button');
    themeBtn.type = 'button';
    themeBtn.className = 'theme-toggle';
    themeBtn.title = 'Switch between dark and light theme';
    themeBtn.setAttribute('aria-label', 'Switch to ' + (currentTheme() === 'light' ? 'dark' : 'light') + ' theme');
    themeBtn.innerHTML = themeBtnIcon(currentTheme());
    themeBtn.addEventListener('click', function () {
      var next = currentTheme() === 'light' ? 'dark' : 'light';
      try { localStorage.setItem('bryme-theme', next); } catch (e) {}
      applyTheme(next);
      themeBtn.innerHTML = themeBtnIcon(next);
      themeBtn.setAttribute('aria-label', 'Switch to ' + (next === 'light' ? 'dark' : 'light') + ' theme');
    });
    header.appendChild(themeBtn);
  }
  // Reading progress bar (thin gradient at the very top)
  var prog = document.createElement('div');
  prog.id = 'bryme-progress';
  prog.setAttribute('aria-hidden', 'true');
  document.body.appendChild(prog);
  // Back-to-top button
  var topBtn = document.createElement('button');
  topBtn.type = 'button';
  topBtn.className = 'bryme-top';
  topBtn.setAttribute('aria-label', 'Back to top');
  topBtn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"/></svg>';
  topBtn.addEventListener('click', function () { try { window.scrollTo({ top: 0, behavior: 'smooth' }); } catch (e) { window.scrollTo(0, 0); } });
  document.body.appendChild(topBtn);
  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    topBtn.classList.toggle('is-visible', y > 420);
    var h = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (prog) prog.style.width = (h > 0 ? (y / h * 100) : 0) + '%';
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();
  // Press "/" to jump straight to Search (or the homepage recommendation box)
  document.addEventListener('keydown', function (e) {
    if (e.key !== '/') return;
    var el = document.activeElement;
    var tag = (el && el.tagName) || '';
    if (/INPUT|TEXTAREA|SELECT/.test(tag)) return;
    if (el && el.isContentEditable) return;
    e.preventDefault();
    var s = document.getElementById('search-q');
    if (s) { s.focus(); try { s.select(); } catch (err) {} return; }
    var r = document.querySelector('[data-rec-input]');
    if (r) r.focus();
  });

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
  var TRAILER_WATCHDOG_MS = (typeof window.BRYME_TRAILER_TIMEOUT !== 'undefined') ? window.BRYME_TRAILER_TIMEOUT : 30000;
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
    var S = { movies: [], articles: [], topics: [], verticals: [] };
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
      var foundV = (S.verticals || []).filter(function (t) { return match(t, tokens, ['title', 'description']); });
      var VEMOJI = { entertainment: '🎬', sports: '⚽', memes: '😂', 'make-money': '💰', tech: '🤖' };
      var showM = activeTab === 'all' || activeTab === 'movie' || activeTab === 'series' || activeTab === 'anime';
      var showA = activeTab === 'all' || activeTab === 'article';
      var showT = activeTab === 'all';
      var showV = activeTab === 'all';
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
      if (showV && foundV.length) {
        total += foundV.length;
        html += '<div class="search-group">Verticals (' + foundV.length + ')</div>';
        html += foundV.map(function (v) {
          var emoji = VEMOJI[v.type] || '🔎';
          var vlabel = { entertainment: 'ENTERTAINMENT', sports: 'SPORTS', memes: 'MEMES & STICKERS', 'make-money': 'MAKE MONEY', tech: 'TECH & AI' }[v.type] || v.type.toUpperCase();
          var bcls = v.type === 'sports' ? 'tb-sports' : v.type === 'memes' ? 'tb-memes' : v.type === 'make-money' ? 'tb-money' : v.type === 'tech' ? 'tb-tech' : 'tb-ent';
          return '<a class="row" href="' + BASE + '/' + esc(v.slug) + '/"><div><b>' + emoji + ' ' + esc(v.title) + '</b><span class="meta" style="font-size:12px;color:var(--muted)"><span class="type-badge ' + bcls + '">' + vlabel + '</span> · ' + esc((v.description || '').slice(0, 90)) + '</span></div></a>';
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

  /* ---------- homepage hero carousel ---------- */
  var heroEl = document.querySelector('[data-hero]');
  if (heroEl) {
    var slides = Array.prototype.slice.call(heroEl.querySelectorAll('[data-slide]'));
    var dots = Array.prototype.slice.call(heroEl.querySelectorAll('[data-hero-dot]'));
    var prevBtn = heroEl.querySelector('[data-hero-prev]');
    var nextBtn = heroEl.querySelector('[data-hero-next]');
    var muteBtn = heroEl.querySelector('[data-hero-mute]');
    var pauseBtn = heroEl.querySelector('[data-hero-pause]');
    var videoBox = heroEl.querySelector('[data-hero-video]');
    var idx = 0, timer = null, advanceTimer = null, playing = false, userPaused = false, heroVisible = true, muted = true;
    var interval = parseInt(heroEl.getAttribute('data-interval') || '8000', 10);
    var VIDEO_HOLD_MS = 12000; // how long an actively playing trailer holds before rotating

    function clearHeroTimers() { if (timer) { clearTimeout(timer); timer = null; } if (advanceTimer) { clearTimeout(advanceTimer); advanceTimer = null; } }
    function heroOrigin() { try { if (/^https?:\/\//i.test(window.location.origin || '')) return '&origin=' + encodeURIComponent(window.location.origin); } catch (e) {} return ''; }
    function hideHeroVideo() {
      if (videoBox) { videoBox.hidden = true; videoBox.innerHTML = ''; }
      if (muteBtn) muteBtn.hidden = true;
      if (pauseBtn) pauseBtn.hidden = false;
      playing = false;
    }
    function loadHeroVideo(withSound) {
      var s = slides[idx];
      if (!s) return;
      var vid = s.getAttribute('data-video');
      if (!vid) return;
      hideHeroVideo();
      videoBox.hidden = false;
      if (muteBtn) { muteBtn.hidden = false; muteBtn.textContent = withSound ? '\u{1F50A}' : '\u{1F507}'; muteBtn.setAttribute('aria-label', withSound ? 'Mute trailer' : 'Unmute trailer'); }
      if (pauseBtn) pauseBtn.hidden = false;
      var iframe = document.createElement('iframe');
      // autoplay is ALWAYS muted on load; sound only ever comes from an explicit user tap
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + vid + '?autoplay=1&mute=' + (withSound ? 0 : 1) + '&playsinline=1&loop=1&playlist=' + vid + '&rel=0&modestbranding=1&enablejsapi=1' + heroOrigin();
      iframe.setAttribute('allow', 'autoplay; encrypted-media; picture-in-picture');
      iframe.setAttribute('allowfullscreen', '');
      iframe.title = s.getAttribute('data-title') + ' trailer';
      videoBox.innerHTML = '';
      videoBox.appendChild(iframe);
      playing = false;
      muted = !withSound;
      var loaded = false;
      iframe.addEventListener('load', function () {
        loaded = true;
        // player page is up; assume muted autoplay began. If the browser blocked
        // autoplay we still hold a reasonable time, then rotate — never 1-2s.
        playing = true;
        scheduleHeroAdvance();
      });
      // fallback: if the player page never even loads (blocked/error), drop to poster
      advanceTimer = setTimeout(function () {
        if (!loaded) { hideHeroVideo(); scheduleHero(); }
      }, 6000);
      scheduleHeroAdvance();
    }
    function scheduleHeroAdvance() {
      if (advanceTimer) { clearTimeout(advanceTimer); advanceTimer = null; }
      advanceTimer = setTimeout(function () {
        if (playing) { nextSlide(); } else { scheduleHero(); }
      }, VIDEO_HOLD_MS);
    }
    function scheduleHero() {
      clearHeroTimers();
      if (!heroVisible || userPaused) return;
      timer = setTimeout(function () {
        if (playing) { scheduleHero(); return; } // never cut an active video short
        nextSlide();
      }, interval);
    }
    function setSlide(i) {
      clearHeroTimers();
      hideHeroVideo();
      idx = ((i % slides.length) + slides.length) % slides.length;
      slides.forEach(function (sl, k) { sl.classList.toggle('is-active', k === idx); });
      dots.forEach(function (d, k) { d.classList.toggle('is-active', k === idx); d.setAttribute('aria-selected', k === idx); });
      if (heroVisible && !userPaused) {
        var slide = slides[idx];
        if (slide && !slide.style.backgroundImage) {
          var posterUrl = slide.getAttribute('data-poster');
          if (posterUrl) slide.style.backgroundImage = "url('" + posterUrl + "')";
        }
        scheduleHero();
      }
    }
    function nextSlide() { setSlide(idx + 1); }
    function prevSlide() { setSlide(idx - 1); }
    if (prevBtn) prevBtn.addEventListener('click', function () { userPaused = false; if (pauseBtn) pauseBtn.textContent = '\u23F8'; prevSlide(); });
    if (nextBtn) nextBtn.addEventListener('click', function () { userPaused = false; if (pauseBtn) pauseBtn.textContent = '\u23F8'; nextSlide(); });
    dots.forEach(function (d) { d.addEventListener('click', function () { userPaused = false; if (pauseBtn) pauseBtn.textContent = '\u23F8'; setSlide(parseInt(d.getAttribute('data-hero-dot'), 10)); }); });
    heroEl.querySelectorAll('[data-hero-watch]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (videoBox && !videoBox.hidden) { hideHeroVideo(); return; }
        loadHeroVideo(false); // still starts muted; the unmute button gives sound
      });
    });
    if (muteBtn) muteBtn.addEventListener('click', function () {
      // toggle sound: reload current video with the opposite mute state
      loadHeroVideo(muted);
    });
    if (pauseBtn) pauseBtn.addEventListener('click', function () {
      userPaused = !userPaused;
      pauseBtn.textContent = userPaused ? '\u25B6' : '\u23F8';
      pauseBtn.setAttribute('aria-label', userPaused ? 'Resume rotation' : 'Pause rotation');
      if (userPaused) { clearHeroTimers(); hideHeroVideo(); } else { scheduleHero(); }
    });
    window.addEventListener('message', function (e) {
      var d = e.data;
      if (!d || typeof d !== 'object' || !d.event) return;
      if (d.event === 'onStateChange') {
        var st = d.info;
        if (st === 1) { playing = true; scheduleHeroAdvance(); }
        else if (st === 0) { nextSlide(); } // video finished -> advance
        else if (st === 2 || st === 5) { playing = false; scheduleHero(); } // paused/blocked -> poster rotation
      } else if (d.event === 'onError') { hideHeroVideo(); scheduleHero(); }
    });
    // touch swipe
    var touchX = null;
    heroEl.addEventListener('touchstart', function (e) { touchX = e.touches ? e.touches[0].clientX : null; }, { passive: true });
    heroEl.addEventListener('touchend', function (e) {
      if (touchX === null || !e.changedTouches) return;
      var dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) { if (dx < 0) nextSlide(); else prevSlide(); }
      touchX = null;
    }, { passive: true });
    heroEl.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') nextSlide();
      if (e.key === 'ArrowLeft') prevSlide();
    });
    // stop audio/video when the hero leaves the viewport or the tab hides
    if ('IntersectionObserver' in window) {
      var heroIO = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          heroVisible = en.isIntersecting;
          if (!heroVisible) { clearHeroTimers(); hideHeroVideo(); } else { scheduleHero(); }
        });
      }, { threshold: 0.12 });
      heroIO.observe(heroEl);
    }
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) { clearHeroTimers(); hideHeroVideo(); }
      else if (heroVisible && !userPaused) { scheduleHero(); }
    });
    // Poster first. Trailer iframe loads only when the visitor taps Watch Trailer.
    var first = slides[0];
    if (first && !first.style.backgroundImage) {
      var firstPoster = first.getAttribute('data-poster');
      if (firstPoster) first.style.backgroundImage = "url('" + firstPoster + "')";
    }
    scheduleHero();
  }

  /* ---------- sports hero carousel arrows (scroll-snap track) ---------- */
  var spHero = document.querySelector('.sp-hero');
  if (spHero) {
    var spTrack = spHero.querySelector('.sp-hero-track');
    var spPrev = spHero.querySelector('[data-sp-hero-prev]');
    var spNext = spHero.querySelector('[data-sp-hero-next]');
    var spCards = spHero.querySelectorAll('.sp-hero-card');
    function spCanScroll() {
      return spTrack && spTrack.scrollWidth > spTrack.clientWidth + 4;
    }
    function spUpdateArrows() {
      if (!spPrev || !spNext) return;
      var can = spCanScroll();
      spPrev.style.display = can ? 'grid' : 'none';
      spNext.style.display = can ? 'grid' : 'none';
    }
    function spScroll(dir) {
      if (!spTrack || !spCanScroll()) return;
      var card = spTrack.querySelector('.sp-hero-card');
      var w = card ? card.getBoundingClientRect().width + 16 : spTrack.clientWidth * 0.8;
      var max = spTrack.scrollWidth - spTrack.clientWidth;
      var target = spTrack.scrollLeft + dir * w;
      if (target < 0) target = 0;
      if (target > max) target = max;
      spTrack.scrollTo({ left: target, behavior: 'smooth' });
    }
    if (spPrev) spPrev.addEventListener('click', function () { spScroll(-1); });
    if (spNext) spNext.addEventListener('click', function () { spScroll(1); });
    // hide arrows when everything fits (desktop 5-card view)
    spUpdateArrows();
    if (typeof ResizeObserver !== 'undefined' && spTrack) {
      new ResizeObserver(spUpdateArrows).observe(spTrack);
    }
    window.addEventListener('resize', spUpdateArrows);
  }

  /* ---------- homepage recommendation engine (catalogue-based) ---------- */
  var recForm = document.querySelector('[data-rec-form]');
  if (recForm) {
    var recInput = recForm.querySelector('[data-rec-input]');
    var recStatus = document.querySelector('[data-rec-status]');
    var recResults = document.querySelector('[data-rec-results]');
    var recData = null;
    var COMMON_G = { action: 1, adventure: 1, comedy: 1, drama: 1, fantasy: 1, 'sci-fi': 1, thriller: 1, romance: 1, crime: 1, horror: 1, animation: 1, family: 1 };
    function recNorm(x) { return String(x || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').replace(/^\s+|\s+$/g, ''); }
    function recTokens(x) { return recNorm(x).split(/\s+/).filter(Boolean); }
    function recLoad(cb) {
      if (recData) { cb(); return; }
      fetch(BASE + '/data/rec-data.json').then(function (r) { return r.json(); }).then(function (d) {
        recData = d; cb();
      }).catch(function () {
        recStatus.textContent = 'Recommendations are unavailable right now. Please try again later.';
      });
    }
    function recMatch(q) {
      var qt = recTokens(q);
      if (!qt.length) return null;
      var best = null, bestScore = 0;
      recData.items.forEach(function (it) {
        var t = recTokens(it.t);
        var hit = 0;
        qt.forEach(function (w) { if (t.indexOf(w) > -1) hit++; });
        var score = hit / qt.length;
        if (score > bestScore) { bestScore = score; best = it; }
      });
      return (best && bestScore >= 0.6) ? best : null;
    }
    function recExplain(src, cand) {
      var sharedG = (src.g || []).filter(function (g) { return (cand.g || []).indexOf(g) > -1; });
      var sharedK = (src.k || []).filter(function (k) { return (cand.k || []).indexOf(k) > -1; });
      return { genres: sharedG, keys: sharedK.slice(0, 3) };
    }
    function recScore(src, cand) {
      var score = 0;
      var rel = (recData.relations && recData.relations[src.s]) || [];
      if (rel.indexOf(cand.s) > -1) score += 100;
      (cand.g || []).forEach(function (g) { if ((src.g || []).indexOf(g) > -1) score += COMMON_G[g] ? 2 : 6; });
      if (cand.ty === src.ty) score += 3;
      if (src.y && cand.y && Math.abs(src.y - cand.y) <= 3) score += 1;
      (src.k || []).forEach(function (k) { if ((cand.k || []).indexOf(k) > -1) score += 1; });
      return score;
    }
    function recCard(it) {
      var img = it.p ? '<img loading="lazy" width="480" height="360" src="' + esc(it.p) + '" alt="' + esc(it.t) + ' poster">' : '<div class="placeholder">' + esc(it.t) + '</div>';
      var rating = it.r != null ? '<p class="tile-rating">★ ' + it.r + '/10 · Editorial</p>' : '';
      var url = BASE + '/' + it.ty + '/' + it.s + '/';
      return '<div class="tile"><div class="poster">' + img + '</div><h3>' + esc(it.t) + '</h3><div class="tile-meta"><span class="type-badge tb-' + it.ty + '">' + it.ty.toUpperCase() + '</span><span>' + (it.y || '') + '</span></div>' + rating + '<div class="rec-actions"><a class="ra-trailer" href="' + url + '#trailer">Watch Trailer</a><a class="ra-details" href="' + url + '">View Details</a></div></div>';
    }
    function recBySlug(slug) {
      var found = null;
      recData.items.forEach(function (x) { if (x.s === slug) found = x; });
      return found;
    }
    // --- live title suggestions below the input (click to open the title page) ---
    var recSuggest = document.createElement('div');
    recSuggest.className = 'rec-suggest';
    recSuggest.hidden = true;
    recInput.parentNode.insertBefore(recSuggest, recInput.nextSibling);
    var suggestTimer = null;
    function recRenderSuggestions() {
      var q = (recInput.value || '').trim();
      if (q.length < 2) { recSuggest.hidden = true; recSuggest.innerHTML = ''; return; }
      recLoad(function () {
        if ((recInput.value || '').trim() !== q) return; // stale keystroke
        var qt = recTokens(q);
        var matches = [];
        recData.items.forEach(function (it) {
          var t = recTokens(it.t);
          var hit = 0;
          qt.forEach(function (w) { if (t.indexOf(w) > -1) hit++; });
          if (hit === qt.length) matches.push(it);
        });
        matches.sort(function (a, b) { return (b.r || 0) - (a.r || 0); });
        if (!matches.length) { recSuggest.hidden = true; recSuggest.innerHTML = ''; return; }
        recSuggest.innerHTML = matches.slice(0, 6).map(function (it) {
          var img = it.p ? '<img loading="lazy" width="60" height="45" src="' + esc(it.p) + '" alt="">' : '<span class="rec-sug-ph"></span>';
          return '<button type="button" class="rec-sug-item" data-sug="' + esc(it.s) + '">' + img + '<span class="rec-sug-txt"><b>' + esc(it.t) + '</b><small>' + it.ty.toUpperCase() + (it.y ? ' · ' + it.y : '') + '</small></span></button>';
        }).join('');
        recSuggest.hidden = false;
      });
    }
    recInput.addEventListener('input', function () {
      if (suggestTimer) clearTimeout(suggestTimer);
      suggestTimer = setTimeout(recRenderSuggestions, 180);
    });
    recInput.addEventListener('focus', function () { if ((recInput.value || '').trim().length >= 2) recRenderSuggestions(); });
    recSuggest.addEventListener('click', function (e) {
      var btn = e.target.closest ? e.target.closest('[data-sug]') : null;
      if (!btn) return;
      var slug = btn.getAttribute('data-sug');
      var it = null;
      recData.items.forEach(function (x) { if (x.s === slug) it = x; });
      if (it) { window.location.href = BASE + '/' + it.ty + '/' + it.s + '/'; }
    });
    document.addEventListener('click', function (e) {
      if (!recSuggest.contains(e.target) && e.target !== recInput) { recSuggest.hidden = true; }
    });
    recForm.addEventListener('submit', function (ev) {
      ev.preventDefault();
      recSuggest.hidden = true;
      var q = (recInput.value || '').trim();
      if (!q) { recStatus.textContent = 'Type a movie, series or anime title first.'; return; }
      recStatus.textContent = 'Finding your next watch...';
      recResults.innerHTML = '';
      recLoad(function () {
        var src = recMatch(q);
        if (!src) {
          recStatus.textContent = '';
          var links = (recData.popular || []).map(function (slug) {
            var it = recBySlug(slug);
            return it ? '<a href="' + BASE + '/' + it.ty + '/' + it.s + '/">' + esc(it.t) + '</a>' : '';
          }).join('');
          recResults.innerHTML = '<div class="rec-miss"><b>We couldn\'t find that title on BRYME.</b><span>Try another movie or series — or start with one of these:</span><span class="rec-pop">' + links + '</span></div>';
          return;
        }
        var scored = [];
        recData.items.forEach(function (it) { if (it.s !== src.s) scored.push({ it: it, sc: recScore(src, it) }); });
        scored.sort(function (a, b) { return (b.sc - a.sc) || ((b.it.r || 0) - (a.it.r || 0)) || (b.it.t < a.it.t ? -1 : 1); });
        var picks = scored.slice(0, 8);
        // explanation built from the signals these picks actually share with the source
        var signalCount = {};
        picks.forEach(function (p) {
          var e = recExplain(src, p.it);
          e.genres.concat(e.keys).forEach(function (x) { signalCount[x] = (signalCount[x] || 0) + 1; });
        });
        var topSignals = Object.keys(signalCount).sort(function (a, b) { return signalCount[b] - signalCount[a]; }).slice(0, 4);
        var why = topSignals.length ? 'You might enjoy these because they share ' + topSignals.join(', ') + '.' : 'You might enjoy these picks based on similar themes and genres.';
        recStatus.textContent = '';
        recResults.innerHTML = '<h3>Because you liked <b>' + esc(src.t) + '</b>...</h3><p class="rec-reason">' + esc(why) + '</p><div class="rec-grid">' + picks.map(function (p) { return recCard(p.it); }).join('') + '</div>';
        if (recResults.scrollIntoView) recResults.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });
    });
  }
})();
/* Persistent back control */
(function () {
  'use strict';
  if (location.pathname === '/' || document.querySelector('[data-bryme-back]')) return;
  var back = document.createElement('button');
  back.type = 'button'; back.className = 'bryme-back'; back.setAttribute('data-bryme-back','');
  back.setAttribute('aria-label', 'Go back'); back.textContent = '←';
  back.addEventListener('click', function () {
    if (history.length > 1 && document.referrer && new URL(document.referrer).origin === location.origin) history.back();
    else location.href = '/';
  });
  document.body.appendChild(back);
})();

/* Parked first-visit notice (desktop hint). Code stays for a later use.
   Flip to true to show it again. When false, ads use normal timing. */
window.BRYME_HINT_ENABLED = false;

/* Monetag (zone 11610560): first-party worker at /sw.js.
   Register after a short wait or the first tap/scroll — not on first paint,
   and not after a long delay that misses the visit. First mobile visit
   waits until the desktop hint is closed. */
(function () {
  'use strict';
  if (!('serviceWorker' in navigator)) return;
  var done = false;
  function firstMobile() {
    if (!window.BRYME_HINT_ENABLED) return false;
    var mobile = !!(window.matchMedia && window.matchMedia('(max-width: 760px)').matches);
    var seen = false;
    try { seen = !!localStorage.getItem('bryme-desk-hint'); } catch (e) {}
    return mobile && !seen;
  }
  function hintOpen() {
    return !!document.querySelector('[data-bryme-desk-hint]');
  }
  function reg() {
    if (done) return;
    if (hintOpen() || firstMobile()) return;
    done = true;
    navigator.serviceWorker.register('/sw.js', { scope: '/' }).catch(function () {});
  }
  window.addEventListener('load', function () { setTimeout(reg, firstMobile() ? 16000 : 5000); });
  document.addEventListener('bryme-desk-hint-done', function () { setTimeout(reg, 8000); });
  ['scroll', 'touchstart', 'click'].forEach(function (ev) {
    window.addEventListener(ev, function () {
      if (hintOpen() || firstMobile()) return;
      setTimeout(reg, 600);
    }, { once: true, passive: true });
  });
})();

/* First-visit mobile notice: BRYME is easier on a computer.
   Not an ad. Once only. Does not force desktop. Holds ads until
   the reader dismisses it, then still waits so they can switch. */
(function () {
  'use strict';
  var KEY = 'bryme-desk-hint';
  function isMobile() {
    return !!(window.matchMedia && window.matchMedia('(max-width: 760px)').matches);
  }
  function seen() {
    try { return !!localStorage.getItem(KEY); } catch (e) { return false; }
  }
  function mark() {
    try { localStorage.setItem(KEY, '1'); } catch (e) {}
  }
  function skipHere() {
    return /\/(privacy|disclaimer|terms|copyright|editorial-policy|contact)\/?$/.test(location.pathname || '');
  }
  function nationalityOpen() {
    var step = document.querySelector('[data-mm-step="nationality"]');
    return !!(step && !step.hidden);
  }
  function done(how) {
    mark();
    var el = document.querySelector('[data-bryme-desk-hint]');
    if (el && el.parentNode) el.parentNode.removeChild(el);
    document.documentElement.style.overflow = '';
    try { document.dispatchEvent(new CustomEvent('bryme-desk-hint-done', { detail: how || 'ok' })); } catch (e) {}
  }
  function show() {
    if (!window.BRYME_HINT_ENABLED) return;
    if (seen() || !isMobile() || skipHere() || nationalityOpen()) return;
    if (document.querySelector('[data-bryme-desk-hint]')) return;
    var wrap = document.createElement('div');
    wrap.className = 'desk-hint';
    wrap.setAttribute('data-bryme-desk-hint', '');
    wrap.setAttribute('role', 'dialog');
    wrap.setAttribute('aria-modal', 'true');
    wrap.setAttribute('aria-labelledby', 'desk-hint-title');
    wrap.innerHTML = '<div class="desk-hint-card">' +
      '<h2 id="desk-hint-title">Easier on a computer</h2>' +
      '<p>BRYME is built to be read on a larger screen. If you have a laptop or desktop, open this site there.</p>' +
      '<p>You can keep reading on this phone. This first look is yours — ads wait a moment.</p>' +
      '<button type="button" class="cta" data-desk-hint-ok>Keep reading here</button>' +
      '</div>';
    wrap.addEventListener('click', function (e) {
      if (e.target === wrap) done('backdrop');
    });
    var btn = wrap.querySelector('[data-desk-hint-ok]');
    if (btn) btn.addEventListener('click', function () { done('ok'); });
    document.body.appendChild(wrap);
    document.documentElement.style.overflow = 'hidden';
    try { if (btn) btn.focus(); } catch (e) {}
  }
  function boot() {
    if (!isMobile() || seen() || skipHere()) return;
    if (nationalityOpen()) {
      var hub = document.querySelector('[data-mm-app]');
      if (!hub || typeof MutationObserver === 'undefined') return;
      var mo = new MutationObserver(function () {
        if (nationalityOpen()) return;
        mo.disconnect();
        show();
      });
      mo.observe(hub, { attributes: true, subtree: true, attributeFilter: ['hidden'] });
      return;
    }
    show();
  }
  window.addEventListener('resize', function () {
    if (!isMobile()) {
      var el = document.querySelector('[data-bryme-desk-hint]');
      if (el) done('desktop');
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.querySelector('[data-bryme-desk-hint]')) done('esc');
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();

/* Monetag page tags — product first, then ads.
   Tag 11610749: lighter unit, once per page after the first screen is readable.
   Vignette 11610753: interruptive. Once per visit (session + 25-minute cooldown),
   only after the reader has had time on the page. Never on nationality, search,
   filters, card renders, legal/contact, or over official apply. */
(function () {
  'use strict';
  if (window.__brymeAdsInit) return;
  window.__brymeAdsInit = true;

  var TAG = { key: 'tag', zone: '11610749', src: 'https://nap5k.com/tag.min.js' };
  var VIGNETTE = { key: 'vignette', zone: '11610753', src: 'https://n6wxm.com/vignette.min.js' };
  var V_SESSION = 'bryme-ad-vignette';
  var V_AT = 'bryme-ad-vignette-at';
  var DESK_HINT = 'bryme-desk-hint';
  var V_COOLDOWN_MS = 18 * 60 * 1000;
  var TAG_DELAY_MS = 1800;
  var TAG_FIRST_MS = 14000;
  var VIGNETTE_DWELL_MS = 5000;
  var VIGNETTE_FIRST_MS = 28000;
  var VIGNETTE_SCROLL_PX = 300;

  var tagStarted = false;
  var vigStarted = false;
  var vigTimer = null;
  var vigRetry = null;
  var onboardingWatch = null;

  function nationalityOpen() {
    var step = document.querySelector('[data-mm-step="nationality"]');
    return !!(step && !step.hidden);
  }

  function pathOf() {
    return location.pathname || '';
  }

  function skipTagHere() {
    return /\/(privacy|disclaimer|terms|copyright|editorial-policy|contact)\/?$/.test(pathOf());
  }

  function isMobile() {
    return !!(window.matchMedia && window.matchMedia('(max-width: 760px)').matches);
  }

  function skipVignetteHere() {
    if (/\/search\/?$/.test(pathOf())) return true;
    return skipTagHere();
  }

  function seenDeskHint() {
    try { return !!localStorage.getItem(DESK_HINT); } catch (e) { return false; }
  }
  function deskHintOpen() {
    return !!document.querySelector('[data-bryme-desk-hint]');
  }
  function firstVisitMobile() {
    if (!window.BRYME_HINT_ENABLED) return false;
    return isMobile() && !seenDeskHint();
  }

  /* Hold only when an overlay would actually break the visit. */
  function firstScreenBusy() {
    if (nationalityOpen()) return true;
    if (deskHintOpen()) return true;
    if (document.querySelector('.trailer-section iframe')) return true;
    if (document.querySelector('.hero-video iframe')) return true;
    return false;
  }

  function vignetteHold() {
    if (isTyping() || officialApplyInView() || firstScreenBusy()) return true;
    return false;
  }

  function already(key) {
    return !!document.querySelector('script[data-bryme-ad="' + key + '"]');
  }

  function storeGet(which, key) {
    try { return which.getItem(key); } catch (e) { return null; }
  }

  function storeSet(which, key, val) {
    try { which.setItem(key, val); } catch (e) {}
  }

  function vignetteAllowed() {
    if (storeGet(sessionStorage, V_SESSION)) return false;
    var at = parseInt(storeGet(localStorage, V_AT) || '0', 10);
    if (at && (Date.now() - at) < V_COOLDOWN_MS) return false;
    return true;
  }

  function markVignette() {
    storeSet(sessionStorage, V_SESSION, '1');
    storeSet(localStorage, V_AT, String(Date.now()));
  }

  function pageUsable() {
    if (nationalityOpen()) return false;
    if (deskHintOpen()) return false;
    if (document.visibilityState === 'hidden') return false;
    if (document.prerendering) return false;
    return true;
  }

  function isTyping() {
    var el = document.activeElement;
    if (!el) return false;
    var tag = (el.tagName || '').toUpperCase();
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return true;
    return !!el.isContentEditable;
  }

  function officialApplyInView() {
    var links = document.querySelectorAll('a[href][target="_blank"], a[rel*="nofollow"]');
    var i, t, r;
    for (i = 0; i < links.length; i++) {
      t = (links[i].textContent || '').replace(/\s+/g, ' ').toLowerCase();
      if (t.indexOf('submit / apply') === -1 && !(t.indexOf('apply') > -1 && t.indexOf('official') > -1)) continue;
      r = links[i].getBoundingClientRect();
      if (r.width && r.height && r.top < window.innerHeight && r.bottom > 0) return true;
    }
    return false;
  }

  function inject(spec) {
    if (!spec || already(spec.key)) return false;
    var host = document.body || document.documentElement;
    if (!host) return false;
    var s = document.createElement('script');
    s.async = true;
    s.dataset.brymeAd = spec.key;
    s.dataset.zone = spec.zone;
    s.src = spec.src;
    host.appendChild(s);
    return true;
  }

  function startTag() {
    if (tagStarted || skipTagHere()) return;
    if (!pageUsable()) {
      setTimeout(startTag, 3000);
      return;
    }
    tagStarted = true;
    inject(TAG);
  }

  function startVignette() {
    if (vigStarted || skipVignetteHere()) return;
    if (!pageUsable()) return;
    if (!vignetteAllowed()) return;
    if (vignetteHold()) {
      if (!vigRetry) {
        vigRetry = setTimeout(function () {
          vigRetry = null;
          startVignette();
        }, 4000);
      }
      return;
    }
    vigStarted = true;
    if (inject(VIGNETTE)) markVignette();
  }

  function armVignette() {
    if (vigStarted || skipVignetteHere() || !vignetteAllowed()) return;
    if (deskHintOpen()) return;
    if (vigTimer) return;
    var wait = firstVisitMobile() ? VIGNETTE_FIRST_MS : (isMobile() ? 12000 : VIGNETTE_DWELL_MS);
    vigTimer = setTimeout(function () {
      vigTimer = null;
      startVignette();
    }, wait);
  }

  function onScroll() {
    if (vigStarted || skipVignetteHere() || nationalityOpen() || deskHintOpen()) return;
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    var need = firstVisitMobile() ? 520 : (isMobile() ? 280 : VIGNETTE_SCROLL_PX);
    if (y < need) return;
    startVignette();
  }

  function watchOnboarding() {
    var hub = document.querySelector('[data-mm-app]');
    if (!hub || onboardingWatch) return;
    onboardingWatch = new MutationObserver(function () {
      if (nationalityOpen()) return;
      onboardingWatch.disconnect();
      onboardingWatch = null;
      scheduleContentAds();
    });
    onboardingWatch.observe(hub, { attributes: true, subtree: true, attributeFilter: ['hidden'] });
  }

  function scheduleContentAds() {
    if (deskHintOpen()) return;
    var tagWait = firstVisitMobile() ? TAG_FIRST_MS : TAG_DELAY_MS;
    setTimeout(startTag, tagWait);
    armVignette();
  }

  function boot() {
    if (nationalityOpen() || deskHintOpen()) {
      watchOnboarding();
      return;
    }
    scheduleContentAds();
  }

  function kick() {
    if (document.prerendering) {
      document.addEventListener('prerenderingchange', boot, { once: true });
      return;
    }
    boot();
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  document.addEventListener('bryme-desk-hint-done', function () {
    scheduleContentAds();
  });
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden') return;
    if (nationalityOpen() || deskHintOpen()) return;
    if (firstVisitMobile()) return;
    if (!tagStarted && !skipTagHere()) startTag();
  });

  /* Start from DOM ready, not window load — images on slow networks
     would otherwise delay ads until after the reader has left. */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', kick);
  } else {
    kick();
  }
})();
