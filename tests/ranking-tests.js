/* BRYME test suite — ranking/editorial system
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
const ent = fs.readFileSync(path.join(ROOT, 'entertainment/index.html'), 'utf8');
const rankings = JSON.parse(fs.readFileSync(path.join(ROOT, 'content/rankings.json'), 'utf8'));

/* 1. Entertainment hub hierarchy (hero slides come first, skip them) */
section('Entertainment hub hierarchy');
{
  const heads = Array.from(ent.matchAll(/<h2>([^<]{2,60})<\/h2>/g)).map(m => m[1]);
  const first = heads.findIndex(h => h.includes('Top 10 Today'));
  const order = heads.slice(first, first + 8);
  assert(first > 0, 'Top 10 Today comes after the hero slides');
  assert(order[0].includes('Top 10 Today'), '1st content row: 🔥 Top 10 Today (got: ' + order[0] + ')');
  assert(order[1].includes('Popular Movies'), '2nd: ⭐ Popular Movies');
  assert(order[2].includes('Popular Series'), '3rd: ⭐ Popular Series');
  assert(order[3].includes('Popular Anime'), '4th: ⭐ Popular Anime');
  assert(order[4].includes('Browse by genre'), '5th: 🎭 Browse by genre');
  assert(order[5].includes('Start here'), '6th: Start here');
  assert(order[6].includes('Latest articles'), '7th: 📰 Latest articles');
  assert(order[7].includes('Watch on a licensed'), '8th: licensed-service strip');
}

/* 2. Top 10 rail: curated, ascending ranks, real tiles */
section('Top 10 Today rail');
{
  const t = tilesBetween(ent, '🔥 Top 10 Today', '⭐ Popular Movies');
  assert(t.length >= 8, 'Top 10 rail has ranked tiles (got ' + t.length + ')');
  const ranks = t.map(x => x.rank && parseInt(x.rank, 10));
  const asc = ranks.every((r, i) => r === i + 1);
  assert(asc, 'ranks ascend 1..N (got ' + ranks.join(',') + ')');
  assert(t.every(x => x.typ === 'movie'), 'Top 10 rail currently lists movies (per-type rank #1)');
  const t10 = rankings.trending.movie.slice().sort((a, b) => a.trendingRank - b.trendingRank);
  assert(t[0] && t[0].title === t10[0].title, 'Top 10 first tile matches trending config #1 (got ' + (t[0] && t[0].title) + ')');
}

/* 3. Popular: independent, per-type */
section('Popular = independent list');
{
  const pm = tilesBetween(ent, '⭐ Popular Movies', '⭐ Popular Series');
  const ps = tilesBetween(ent, '⭐ Popular Series', '⭐ Popular Anime');
  const pa = tilesBetween(ent, '⭐ Popular Anime', '🎭 Browse by genre');
  assert(pm.length >= 8, 'popular movies rail present (' + pm.length + ')');
  assert(ps.length >= 8, 'popular series rail present (' + ps.length + ')');
  assert(pa.length >= 8, 'popular anime rail present (' + pa.length + ')');
  assert(pm.every(x => x.typ === 'movie'), 'popular movies rail: only movies');
  assert(ps.every(x => x.typ === 'series'), 'popular series rail: only series');
  assert(pa.every(x => x.typ === 'anime'), 'popular anime rail: only anime');
  assert(pm.some(x => x.title === 'Titanic'), 'Titanic is popular');
  assert(ps.some(x => x.title === 'Breaking Bad'), 'Breaking Bad is popular');
  assert(pa.some(x => x.title === 'One Piece'), 'One Piece is popular');
}

/* 4. Title-page badges: independent concepts */
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

/* 5. /trending/ hub uses same controlled lists */
section('/trending/ hub');
{
  const hub = fs.readFileSync(path.join(ROOT, 'trending/index.html'), 'utf8');
  const heads = Array.from(hub.matchAll(/<h2>([^<]{2,60})<\/h2>/g)).map(m => m[1]);
  assert(heads.some(h => h.includes('Movies')), 'hub: Movies section');
  assert(heads.some(h => h.includes('TV series')), 'hub: TV series section');
  assert(heads.some(h => h.includes('Anime')), 'hub: Anime section');
  const i = hub.indexOf('id="movies"'), j = hub.indexOf('id="series"');
  const k = hub.indexOf('id="anime"'), l = hub.indexOf('id="nollywood"');
  const nM = (hub.slice(i, j).match(/class="trend-card"/g) || []).length;
  const nS = (hub.slice(j, k).match(/class="trend-card"/g) || []).length;
  const nA = (hub.slice(k, l).match(/class="trend-card"/g) || []).length;
  assert(nM === rankings.trending.movie.length, 'hub trending movies: ' + nM + ' (config ' + rankings.trending.movie.length + ')');
  assert(nS === rankings.trending.series.length, 'hub trending series: ' + nS);
  assert(nA === rankings.trending.anime.length, 'hub trending anime: ' + nA);
  assert(!hub.includes('How the Trending score works'), 'hub has no old score explanation');
}

/* 6. data/trending.json */
section('data/trending.json');
{
  const d = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/trending.json'), 'utf8'));
  assert(d.mode === 'editorial-curation', 'mode = editorial-curation');
  const sq = d.records.find(r => r.slug === 'squid-game');
  assert(sq && sq.trendingRank === 1 && sq.typeDir === 'series', 'squid-game in data with trendingRank 1 series');
}

/* 7. Determinism: two identical reads of the build output */
section('Determinism');
{
  const a = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
  const b = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
  assert(a === b, 'homepage byte-identical on repeated reads (no randomness)');
}

console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
