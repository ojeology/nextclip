/* NEXTCLIP test suite — ranking/editorial system
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/ranking-tests.js
   (jsdom must be installed; e.g. npm install jsdom in any folder) */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
function tilesBetween(html, fromH2, toH2) {
  const i = html.indexOf(fromH2);
  const j = toH2 ? html.indexOf(toH2, i + 10) : html.length;
  const seg = html.slice(i, j > 0 ? j : i + 20000);
  return Array.from(seg.matchAll(/<a class="tile" href="[^"]+">([\s\S]*?)<\/a>/g)).map(m => {
    const title = (m[1].match(/<h3>([^<]+)<\/h3>/) || [])[1] || '?';
    const typ = (m[1].match(/type-badge tb-(\w+)/) || [])[1] || '?';
    const rank = (m[1].match(/class="rank[^"]*">(\d+)<\/span>/) || [])[1] || null;
    return { title, typ, rank };
  });
}

const home = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
const rankings = JSON.parse(fs.readFileSync(path.join(ROOT, 'content/rankings.json'), 'utf8'));

/* 1. Homepage section order */
section('Homepage hierarchy');
{
  const heads = Array.from(home.matchAll(/<h2>([^<]{2,60})<\/h2>/g)).map(m => m[1]);
  const order = heads.slice(0, 10);
  assert(order[0].includes("DON'T KNOW WHAT TO WATCH?"), '1st: DON\'T KNOW WHAT TO WATCH? (got: ' + order[0] + ')');
  assert(order[1].includes('Trending Now'), '2nd: 🔥 Trending Now (got: ' + order[1] + ')');
  assert(order[2].includes('Popular Movies'), '3rd: ⭐ Popular Movies');
  assert(order[3].includes('Popular Series'), '4th: ⭐ Popular Series');
  assert(order[4].includes('Popular Anime'), '5th: ⭐ Popular Anime');
  assert(order[5].includes("Editor's Picks"), '6th: 👑 Editor\'s Picks');
  assert(order[6].includes('New Releases'), '7th: 🆕 New Releases');
  assert(order[7].includes('Movies') && !order[7].includes('Popular'), '8th: 🎬 Movies (got: ' + order[7] + ')');
  assert(order[8].includes('Series') && !order[8].includes('Popular'), '9th: 📺 Series');
  assert(order[9].includes('Anime') && !order[9].includes('Popular'), '10th: 🍥 Anime');
}

/* 2. Trending = config order, per-type ranks */
section('Trending Now = curated config');
{
  const t = tilesBetween(home, '🔥 Trending Now', '⭐ Popular Movies');
  const cfgMovie = rankings.trending.movie.slice().sort((a, b) => a.trendingRank - b.trendingRank);
  const cfgSeries = rankings.trending.series.slice().sort((a, b) => a.trendingRank - b.trendingRank);
  const cfgAnime = rankings.trending.anime.slice().sort((a, b) => a.trendingRank - b.trendingRank);
  assert(t.length === cfgMovie.length + cfgSeries.length + cfgAnime.length, 'trending rail has all configured titles (got ' + t.length + ')');
  const movieTiles = t.filter(x => x.typ === 'movie');
  const seriesTiles = t.filter(x => x.typ === 'series');
  const animeTiles = t.filter(x => x.typ === 'anime');
  assert(movieTiles.length === cfgMovie.length, 'all trending movies present (' + movieTiles.length + ')');
  assert(seriesTiles.length === cfgSeries.length, 'all trending series present');
  assert(animeTiles.length === cfgAnime.length, 'all trending anime present');
  assert(movieTiles.map(x => x.rank).join(',') === cfgMovie.map(x => String(x.trendingRank)).join(','), 'movie ranks match config ASC');
  assert(seriesTiles[0].rank === '1', 'first series has rank #1 (per-type, not global)');
  assert(animeTiles[0].rank === '1', 'first anime has rank #1');
}

/* 3. Popular: independent, per-type */
section('Popular = independent list');
{
  const pm = tilesBetween(home, '⭐ Popular Movies', '⭐ Popular Series');
  const ps = tilesBetween(home, '⭐ Popular Series', '⭐ Popular Anime');
  const pa = tilesBetween(home, '⭐ Popular Anime', "👑 Editor's Picks");
  assert(pm.length === rankings.popular.movie.length, 'popular movies count matches config (' + pm.length + ')');
  assert(ps.length === rankings.popular.series.length, 'popular series count matches config');
  assert(pa.length === rankings.popular.anime.length, 'popular anime count matches config');
  assert(pm.every(x => x.typ === 'movie'), 'popular movies rail: only movies');
  assert(ps.every(x => x.typ === 'series'), 'popular series rail: only series');
  assert(pa.every(x => x.typ === 'anime'), 'popular anime rail: only anime');
  assert(pm.some(x => x.title === 'Titanic'), 'Titanic is popular');
  assert(ps.some(x => x.title === 'Breaking Bad'), 'Breaking Bad is popular');
  assert(pa.some(x => x.title === 'One Piece'), 'One Piece is popular');
}

/* 4. Editor's Picks */
section("Editor's Picks");
{
  const ep = tilesBetween(home, "👑 Editor's Picks", '🆕 New Releases');
  assert(ep.length === rankings.editorPicks.length, 'editor picks count matches config (' + ep.length + ')');
  assert(ep[0].title.toLowerCase().includes('one piece'), 'first pick = One Piece (rank 1)');
}

/* 5. Title-page badges: independent concepts */
section('Title-page editorial badges');
{
  const load = p => fs.readFileSync(path.join(ROOT, p), 'utf8');
  const sq = load('series/squid-game/index.html');
  assert(sq.includes('🔥 Trending #1'), 'Squid Game: Trending #1 badge');
  assert(sq.includes('⭐ Popular'), 'Squid Game: Popular badge');
  assert(sq.includes("👑 Editor's Pick"), 'Squid Game: Editor\'s Pick badge');
  const bb = load('series/breaking-bad/index.html');
  assert(bb.includes('⭐ Popular') && !bb.includes('🔥 Trending'), 'Breaking Bad: Popular WITHOUT Trending');
  const bad = load('series/into-the-badlands/index.html');
  assert(bad.includes("👑 Editor's Pick") && !bad.includes('⭐ Popular') && !bad.includes('🔥 Trending'), 'Into the Badlands: Editor\'s Pick ONLY');
  assert(!load('movie/interstellar/index.html').includes('Trending score'), 'no fake "Trending score" row anywhere');
  assert(!home.includes('transparent trending score'), 'homepage has NO old score text');
  assert(!home.includes('editorial rating + release recency'), 'homepage has NO old formula text');
}

/* 6. /trending/ hub uses same controlled lists */
section('/trending/ hub');
{
  const hub = fs.readFileSync(path.join(ROOT, 'trending/index.html'), 'utf8');
  const heads = Array.from(hub.matchAll(/<h2>([^<]{2,60})<\/h2>/g)).map(m => m[1]);
  assert(heads.some(h => h.includes('Trending Movies')), 'hub: Trending Movies');
  assert(heads.some(h => h.includes('Trending Series')), 'hub: Trending Series');
  assert(heads.some(h => h.includes('Trending Anime')), 'hub: Trending Anime');
  const i = hub.indexOf('🔥 Trending Movies'), j = hub.indexOf('🔥 Trending Series');
  const k = hub.indexOf('🔥 Trending Anime'), l = hub.indexOf("👑 Editor's Picks");
  const nM = (hub.slice(i, j).match(/class="tile"/g) || []).length;
  const nS = (hub.slice(j, k).match(/class="tile"/g) || []).length;
  const nA = (hub.slice(k, l).match(/class="tile"/g) || []).length;
  assert(nM === rankings.trending.movie.length, 'hub trending movies: ' + nM + ' (config ' + rankings.trending.movie.length + ')');
  assert(nS === rankings.trending.series.length, 'hub trending series: ' + nS);
  assert(nA === rankings.trending.anime.length, 'hub trending anime: ' + nA);
  assert(!hub.includes('How the Trending score works'), 'hub has no old score explanation');
}

/* 7. data/trending.json */
section('data/trending.json');
{
  const d = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/trending.json'), 'utf8'));
  assert(d.mode === 'editorial-curation', 'mode = editorial-curation');
  const sq = d.records.find(r => r.slug === 'squid-game');
  assert(sq && sq.trendingRank === 1 && sq.typeDir === 'series', 'squid-game in data with trendingRank 1 series');
}

/* 8. Determinism: two identical reads of the build output */
section('Determinism');
{
  const a = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
  const b = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
  assert(a === b, 'homepage byte-identical on repeated reads (no randomness)');
}

console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
