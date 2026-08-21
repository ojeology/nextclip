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
  const expected = ['Top 10 Today','Trending Now','Latest Release','Hot New Releases','Bollywood',
    'South Indian Hits','Indian Originals','Hollywood','Action Movies','Drama Series','Comedy',
    'Thrillers','Sci-Fi','Romance','Horror','Animation','Trending Globally'];
  expected.forEach(function (want, i) {
    assert(heads[i] && heads[i].includes(want), (i + 1) + ': ' + want + ' (got: ' + heads[i] + ')');
  });
}

/* 2. Top 10 Today rail: exact 10 reference cards, ascending ranks, real links */
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

/* 4. Hero embeds: 3 slides carry official trailer IDs */
section('Hero embeds');
{
  const vids = Array.from(ent.matchAll(/data-video="([^"]+)"/g)).map(m => m[1]);
  assert(vids.length === 3, '3 hero slides have embeds (' + vids.length + ')');
  const known = ['m08TxIsFTRI', 'QCc8yAd64x8', 'P9mwtI82k6E'];
  assert(known.every(v => vids.includes(v)), 'hero embed IDs match official trailers');
}


