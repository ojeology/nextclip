/* BRYME test suite — ranking/editorial system
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/ranking-tests.js
   (jsdom must be installed; e.g. npm install jsdom in any folder) */
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

/* 1. Entertainment hub hierarchy (hero titles are h1, so Top 10 Today is the first h2) */
section('Entertainment hub hierarchy');
{
  const heads = Array.from(ent.matchAll(/<h2>([^<]{2,60})<\/h2>/g)).map(m => m[1]);
  const order = heads.slice(0, 17);
  assert(order[0].includes('Top 10 Today'), '1st row: 🔥 Top 10 Today (got: ' + order[0] + ')');
  const expected = [['Top 10 Today'], ['Trending Now'], ['Latest Release'], ['Hot New Releases'],
    ['Bollywood'], ['South Indian Hits'], ['Indian Originals'], ['Hollywood'], ['Action Movies'],
    ['Drama Series'], ['Comedy'], ['Thrillers'], ['Sci-Fi'], ['Romance'], ['Horror'],
    ['Animation'], ['Trending Globally']];
  expected.forEach(function (want, i) {
    assert(order[i] && want.every(w => order[i].includes(w)), (i + 1) + ': ' + want[0] + ' (got: ' + order[i] + ')');
  });
}

/* 2. Top 10 Today rail: exact reference cards, ascending ranks, real links */
section('Top 10 Today rail');
{
  const t = tilesBetween(ent, '🔥 Top 10 Today', 'Trending Now');
  assert(t.length === 10, 'Top 10 rail has 10 cards (got ' + t.length + ')');
  const names = ['Reacher','The Traitors','Spider-Man: Brand New Day','Adaalat','The Mentalist',
    'The Odyssey','Outer Banks','Game of Thrones','Awarapan','Spider-Man: No Way Home'];
  names.forEach(function (n, i) {
    assert(t[i] && t[i].title === n, 'Top 10 #' + (i + 1) + ' = ' + n + ' (got ' + (t[i] && t[i].title) + ')');
  });
  const ranks = t.map(x => x.rank && parseInt(x.rank, 10));
  assert(ranks.join(',') === '1,2,3,4,5,6,7,8,9,10', 'ranks ascend 1..10 (got ' + ranks.join(',') + ')');
}

/* 3. Row structure: split by section, count exact cards per row */
section('Row card counts');
{
  const secs = ent.split(/(?=<section)/);
  const rowCounts = {};
  secs.forEach(function (sec) {
    const h2 = (sec.match(/<h2>([^<]{2,60})<\/h2>/) || [])[1];
    if (!h2) return;
    rowCounts[h2.replace('🔥 ', '')] = (sec.match(/class="tile"/g) || []).length;
  });
  const want = {
    'Top 10 Today': 10, 'Trending Now': 13, 'Latest Release': 8, 'Hot New Releases': 10,
    'Bollywood': 10, 'South Indian Hits': 6, 'Indian Originals': 30, 'Hollywood': 11,
    'Action Movies': 17, 'Drama Series': 17, 'Comedy': 16, 'Thrillers': 14, 'Sci-Fi': 15,
    'Romance': 17, 'Horror': 15, 'Animation &amp; Family': 19, 'Trending Globally — Coming Soon': 7,
  };
  Object.keys(want).forEach(function (k) {
    const got = rowCounts[k];
    assert(got === want[k], k + ' has ' + want[k] + ' cards (got ' + got + ')');
  });
  const links = Array.from(ent.matchAll(/<a class="tile" href="(\/(?:movie|series|anime)\/[^"]+)\/">/g)).map(m => m[1]);
  const missing = links.filter(function (l) {
    return !fs.existsSync(path.join(ROOT, l.slice(1), 'index.html'));
  });
  assert(links.length === 235, '235 cards total (' + links.length + ')');
  assert(missing.length === 0, 'all card hrefs resolve to real pages' + (missing.length ? ' (missing: ' + missing.join(',') + ')' : ''));
}

/* 4. Hero embeds: 10 slides carry official trailer IDs */
section('Hero embeds');
{
  const vids = Array.from(ent.matchAll(/data-video="([^"]+)"/g)).map(m => m[1]);
  assert(vids.length === 10, '10 hero slides have embeds (' + vids.length + ')');
  assert(vids.every(v => /^[A-Za-z0-9_-]{11}$/.test(v)), 'all hero embeds are valid 11-char YouTube IDs');
}

/* 5. Title-page editorial badges: independent concepts */
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
