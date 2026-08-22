/* SEO pilot — watch intent, no fabricated availability, type-mismatch redirects.
   Run: node tests/seo-pilot-tests.js */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
const read = p => fs.readFileSync(path.join(ROOT, p), 'utf8');

section('Shōgun case study');
{
  const html = read('series/shogun/index.html');
  assert(/<link rel="canonical" href="https:\/\/bryme\.onrender\.com\/series\/shogun\/">/.test(html), 'canonical stays /series/shogun/');
  assert(/<title>Shōgun \(2024\) \| Cast, Trailer, Episodes &amp; Where to Watch \| BRYME<\/title>/.test(html), 'intent title kept');
  const desc = html.match(/<meta name="description" content="([^"]*)"/);
  assert(desc && !/beco…|host…/.test(desc[1]) && /does not host episodes/.test(desc[1].replace(/&#x27;/g, "'")), 'meta is complete, not truncated');
  assert(/does not host/.test(html), 'page says BRYME does not host');
  assert(/FX/.test(html) && /id="watch"/.test(html), 'watch block mentions FX');
  assert(!/<a class="svc-chip"[^>]*>Crunchyroll<\/a>/.test(html), 'no Crunchyroll chip on Shōgun');
  assert(!/<a class="svc-chip"[^>]*>Netflix<\/a>/.test(html), 'no generic Netflix chip on Shōgun');
  assert(/Where to watch/.test(html) && !/▶ Watch Now/.test(html), 'CTA is Where to watch, not Watch Now');
  assert(/Hiroyuki Sanada/.test(html) && /Anna Sawai/.test(html), 'cast includes more than one name');
  assert(/id="find-legally"/.test(html), 'watch-intent case-study section present');
  assert(desc && desc[1].length <= 160 && /legal stream|does not host/i.test(desc[1]), 'meta describes viewing help without stuffing');
}

section('Silo originating network');
{
  const html = read('series/silo/index.html');
  assert(/Apple TV/.test(html), 'Silo watch copy can mention Apple TV+ (catalogue already does)');
  assert(!/<a class="svc-chip"[^>]*>Crunchyroll<\/a>/.test(html), 'no Crunchyroll chip on Silo');
  assert(/does not host/.test(html), 'Silo says BRYME does not host');
}

section('Type-mismatch redirects');
{
  const stub = read('movie/shogun/index.html');
  assert(/noindex/.test(stub), '/movie/shogun/ is noindex');
  assert(/series\/shogun\//.test(stub), '/movie/shogun/ points at /series/shogun/');
  assert(/has moved/i.test(stub), '/movie/shogun/ is a moved stub');
  const sm = read('sitemap.xml');
  assert(!sm.includes('/movie/shogun/'), 'sitemap does not list /movie/shogun/');
  assert(sm.includes('/series/shogun/'), 'sitemap still lists canonical /series/shogun/');
  const redirs = read('_redirects');
  assert(/\/movie\/shogun\/\s+\/series\/shogun\/\s+301/.test(redirs), '_redirects has 301 for Shōgun');
}

section('Sitemap hygiene');
{
  const sm = read('sitemap.xml');
  assert(!/noindex/.test(sm), 'sitemap file itself is URL list only');
  const movieShogun = (sm.match(/\/movie\/shogun\//g) || []).length;
  assert(movieShogun === 0, 'zero /movie/shogun/ sitemap entries');
}

section('Guidance file is conservative');
{
  const g = JSON.parse(read('content/watch-guidance.json'));
  assert(g.shogun.originalNetwork === 'FX', 'Shōgun network is FX');
  assert(g.shogun.check.every(c => c.name !== 'Hulu' || true), 'check list exists');
  assert(!g['the-notebook'] || !g['the-notebook'].originalNetwork, 'no invented network for The Notebook');
}

console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
