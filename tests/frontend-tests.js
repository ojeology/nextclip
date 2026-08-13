/* NEXTCLIP test suite — category browsers + search
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/frontend-tests.js */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const app = fs.readFileSync(path.join(ROOT, 'assets/site-app.js'), 'utf8');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
function run(html, fn) {
  const dom = new JSDOM(html, { runScripts: 'dangerously', url: 'https://ojeology.github.io/nextclip/movies/' });
  dom.window.eval(app);
  return fn(dom);
}

section('Movies category browser');
const moviesHtml = fs.readFileSync(path.join(ROOT, 'movies/index.html'), 'utf8');
const jsonMatch = moviesHtml.match(/<script id="catalogue-data" type="application\/json">([\s\S]*?)<\/script>/);
assert(!!jsonMatch, 'movies page embeds catalogue-data JSON');
let meta;
try { meta = JSON.parse(jsonMatch[1]); assert(meta.items.length === 477, '477 movies embedded (got ' + meta.items.length + ')'); }
catch (e) { assert(false, 'embed JSON parses: ' + e.message); }
run(moviesHtml, (dom) => {
  const w = dom.window, d = w.document;
  const genreEl = d.getElementById('f-genre');
  assert(genreEl && genreEl.options.length > 19, 'genre select has 19+ options');
  assert(d.getElementById('f-sort'), 'sort select exists');
  assert(d.getElementById('f-year'), 'year select exists');
  assert(d.getElementById('f-country'), 'country select exists');
  assert(d.getElementById('f-language'), 'language select exists');
  assert(d.querySelectorAll('[data-cards] .tile').length === 40, 'initial render shows 40 tiles');
  genreEl.value = 'Action';
  genreEl.dispatchEvent(new w.Event('change'));
  const tiles = d.querySelectorAll('[data-cards] .tile');
  assert(tiles.length === 40, 'Action filter renders 40 tiles');
  assert(tiles[0].querySelector('.type-badge').textContent === 'MOVIE', 'cards show MOVIE badge');
  const count = d.querySelector('[data-count]').textContent;
  assert(count.indexOf('72 of 477') > -1, 'count line reflects filter (got: ' + count + ')');
  const sortEl = d.getElementById('f-sort');
  sortEl.value = 'newest'; sortEl.dispatchEvent(new w.Event('change'));
  assert(d.querySelector('[data-cards] .tile h3').textContent.length > 0, 'newest sort renders');
  d.querySelector('[data-clear]').click();
  assert(d.querySelector('[data-count]').textContent.indexOf('477 movies') > -1, 'clear restores full count');
  const badges = Array.from(d.querySelectorAll('[data-cards] .type-badge')).map(b => b.textContent);
  assert(badges.every(b => b === 'MOVIE'), 'no series/anime badges in movies page');
  assert(!!d.querySelector('.loadmore'), 'load more button appears');
  dom.window.close();
});

section('Series category browser');
run(fs.readFileSync(path.join(ROOT, 'series/index.html'), 'utf8'), (dom) => {
  const d = dom.window.document;
  const badges = Array.from(d.querySelectorAll('[data-cards] .type-badge')).map(b => b.textContent);
  assert(badges.length === 40, 'series page renders tiles');
  assert(badges.every(b => b === 'SERIES'), 'series page shows only SERIES badges');
  const g = d.getElementById('f-genre');
  g.value = 'Crime';
  g.dispatchEvent(new dom.window.Event('change'));
  const titles = Array.from(d.querySelectorAll('[data-cards] h3')).map(h => h.textContent);
  assert(titles.includes('Breaking Bad') || titles.includes('Money Heist') || titles.includes('Ozark'), 'Crime filter shows crime series');
  dom.window.close();
});

section('Anime category browser');
run(fs.readFileSync(path.join(ROOT, 'anime/index.html'), 'utf8'), (dom) => {
  const d = dom.window.document;
  const badges = Array.from(d.querySelectorAll('[data-cards] .type-badge')).map(b => b.textContent);
  assert(badges.every(b => b === 'ANIME'), 'anime page shows only ANIME badges');
  const g = d.getElementById('f-genre');
  g.value = 'Shonen';
  g.dispatchEvent(new dom.window.Event('change'));
  const titles = Array.from(d.querySelectorAll('[data-cards] h3')).map(h => h.textContent);
  assert(titles.includes('One Piece') && titles.includes('Naruto'), 'Shonen filter shows One Piece + Naruto');
  dom.window.close();
});

section('Search page');
const searchHtml = fs.readFileSync(path.join(ROOT, 'search/index.html'), 'utf8');
const sjson = searchHtml.match(/<script id="search-data" type="application\/json">([\s\S]*?)<\/script>/);
assert(!!sjson, 'search page embeds data');
assert(JSON.parse(sjson[1]).movies.length === 630, 'search index has 630 titles');
run(searchHtml, (dom) => {
  const w = dom.window, d = w.document;
  const q = d.getElementById('search-q');
  q.value = 'breaking bad';
  q.dispatchEvent(new w.Event('input'));
  setTimeout(() => {
    const cards = d.querySelectorAll('#search-results .tile');
    assert(cards.length === 1, 'search "breaking bad" -> 1 result (got ' + cards.length + ')');
    assert(d.querySelector('#search-results .type-badge').textContent === 'SERIES', 'result shows SERIES badge');
    d.querySelector('[data-tab="movie"]').click();
    assert(d.querySelectorAll('#search-results .tile').length === 0, 'movie tab excludes series');
    d.querySelector('[data-tab="anime"]').click();
    q.value = 'one piece';
    q.dispatchEvent(new w.Event('input'));
    setTimeout(() => {
      assert(d.querySelector('#search-results .type-badge').textContent === 'ANIME', 'anime tab + "one piece" shows ANIME badge');
      d.querySelector('[data-tab="article"]').click();
      q.value = 'prison break';
      q.dispatchEvent(new w.Event('input'));
      setTimeout(() => {
        const rows = d.querySelectorAll('#search-results .row');
        assert(rows.length === 2, 'article search finds matching articles (got ' + rows.length + ')');
        finish();
      }, 200);
    }, 200);
  }, 200);
});
function finish() {
  section('Genre page load-more');
  run(fs.readFileSync(path.join(ROOT, 'movies/horror/index.html'), 'utf8'), (dom) => {
    const d = dom.window.document;
    const hidden = d.querySelectorAll('.more-tile[hidden]');
    assert(hidden.length > 0, 'genre page has hidden tiles for load-more');
    const btn = d.querySelector('[data-load-more]');
    assert(!!btn, 'load-more button exists');
    btn.click();
    assert(d.querySelectorAll('.more-tile[hidden]').length === 0, 'load-more reveals hidden tiles');
    console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
    process.exit(fail ? 1 : 0);
  });
}
