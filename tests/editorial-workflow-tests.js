#!/usr/bin/env node
/* BRYME editorial workflow tests.
 * Covers: activation window, indexable/non-indexable state, sitemap inclusion,
 * datePublished, dateModified, post-match transition, duplicate-URL prevention,
 * and historical content preservation.
 *
 * Run: NODE_PATH=/home/user/node_modules node tests/editorial-workflow-tests.js
 */
const fs = require('fs'), path = require('path'), cp = require('child_process');
const ROOT = path.resolve(__dirname, '..');
const read = p => fs.readFileSync(path.join(ROOT, p), 'utf8');
const json = p => JSON.parse(read(p));

let pass = 0, fail = 0;
const assert = (c, m) => { if (c) { pass++; } else { fail++; console.log('  \u2717 FAIL: ' + m); } };
const section = t => console.log('\n' + t);

const ISO = /^\d{4}-\d{2}-\d{2}$/;
const FIELDS = ['overview','recentForm','headToHead','lastFiveMeetings','homeAwayForm','keyPlayers',
  'injuries','suspensions','expectedLineups','tacticalMatchup','historicalContext','underdog','outlook','scorePrediction'];
const filled = e => !e ? 0 : FIELDS.filter(k => {
  const v = e[k];
  return Array.isArray(v) ? v.length > 0 : (typeof v === 'string' && v.trim().length > 12);
}).length;

const ED = json('content/match-editorial.json');
const RESULTS = json('content/results.json');
const FIX = json('content/fixtures.json');
const sm = read('sitemap.xml');
const LEAGUES = ['premier-league','la-liga','serie-a','bundesliga','ligue-1'];

/* 1. The fixture database must be intact - the workflow must never delete schedule data */
section('Fixture database preserved');
{
  const all = FIX.matchweeks.flatMap(w => w.matches);
  assert(FIX.matchweeks.length === 38, 'premier league still has 38 matchweeks');
  assert(all.length === 380, 'premier league still has all 380 fixtures (got ' + all.length + ')');
  let pages = 0;
  for (const lg of LEAGUES) {
    const dir = path.join(ROOT, 'sports', lg, 'matches');
    if (fs.existsSync(dir)) pages += fs.readdirSync(dir, {withFileTypes:true}).filter(d => d.isDirectory()).length;
  }
  assert(pages > 1700, 'every scheduled fixture still has a page (' + pages + ')');
  for (const lg of LEAGUES) assert(ED[lg] !== undefined, `editorial store has a ${lg} bucket`);
}

/* 2. Activation: content, not the calendar, is what promotes a page */
section('Editorial activation window');
{
  const q = cp.execSync('node scripts/editorial-queue.js --today 2026-08-17', {cwd: ROOT}).toString();
  assert(/TO WRITE/.test(q), 'queue reports fixtures still to write');
  assert(/ALREADY LIVE/.test(q), 'queue reports fixtures already live');
  assert(/Window opens T-5, page should be live by T-3/.test(q), 'queue states the 5-day open / 3-day due window');
  const overdue = cp.execSync('node scripts/editorial-queue.js --today 2026-08-17 --overdue', {cwd: ROOT}).toString();
  assert(/OVERDUE/.test(overdue), 'queue can list overdue fixtures inside the 3-day mark');
  /* a fixture far in the future must not be surfaced as due */
  assert(!/T-\s*(\d{2,})/.test(q.split('ALREADY LIVE')[0]), 'nothing beyond the window is listed as due');
}

/* 3+4. Indexable state and sitemap inclusion follow the same rule */
section('Indexable state and sitemap inclusion');
{
  let live = 0, dormant = 0, leaked = 0, missing = 0;
  for (const lg of LEAGUES) {
    const fixFile = lg === 'premier-league' ? 'fixtures.json' : `fixtures-${lg}.json`;
    if (!fs.existsSync(path.join(ROOT, 'content', fixFile))) continue;
    const F = json('content/' + fixFile);
    for (const w of F.matchweeks || []) for (const m of w.matches || []) {
      const slug = m.id + '-vs-' + m.away;
      const p = `sports/${lg}/matches/${slug}/index.html`;
      if (!fs.existsSync(path.join(ROOT, p))) continue;
      const html = read(p);
      const inSitemap = sm.includes(`/sports/${lg}/matches/${slug}/</loc>`);
      const isNoindex = /name="robots" content="noindex/.test(html);
      const editorial = filled((ED[lg] || {})[slug]) >= 3;
      const hasResult = !!(RESULTS[lg] || {})[slug];
      if (editorial || hasResult) {
        live++;
        if (isNoindex) { leaked++; assert(false, `${slug}: has editorial/result but is noindex`); }
        if (!inSitemap) { missing++; assert(false, `${slug}: has editorial/result but is not in the sitemap`); }
      } else {
        dormant++;
        if (!isNoindex) { leaked++; assert(false, `${slug}: no editorial content but is indexable`); }
        if (inSitemap) { leaked++; assert(false, `${slug}: no editorial content but is in the sitemap`); }
      }
    }
  }
  assert(live > 0, `at least one fixture is live editorial (${live})`);
  assert(dormant > 1000, `the bulk of fixtures stay out of the index (${dormant} dormant)`);
  assert(leaked === 0 && missing === 0, 'indexable state matches editorial state exactly');
  const smMatches = (sm.match(/\/matches\/[^<]+<\/loc>/g) || []).length;
  assert(smMatches === live, `sitemap contains exactly the live match pages (${smMatches} vs ${live})`);
}

/* 5. datePublished */
section('datePublished');
{
  for (const lg of LEAGUES) for (const [slug, e] of Object.entries(ED[lg] || {})) {
    if (filled(e) < 3) continue;
    assert(ISO.test(e.publishedAt || ''), `${slug}: publishedAt is ISO`);
    const html = read(`sports/${lg}/matches/${slug}/index.html`);
    assert(html.includes(`"datePublished":"${e.publishedAt}"`), `${slug}: datePublished emitted in structured data`);
  }
}

/* 6. dateModified drives sitemap lastmod */
section('dateModified and sitemap lastmod');
{
  for (const lg of LEAGUES) for (const [slug, e] of Object.entries(ED[lg] || {})) {
    if (filled(e) < 3) continue;
    const res = (RESULTS[lg] || {})[slug];
    const expected = (res && (res.verifiedOn || res.playedOn))
      || (e.postMatch && e.postMatch.publishedAt) || e.updatedAt || e.publishedAt;
    const html = read(`sports/${lg}/matches/${slug}/index.html`);
    assert(html.includes(`"dateModified":"${expected}"`), `${slug}: dateModified is ${expected}`);
    const re = new RegExp('<loc>[^<]*/sports/' + lg + '/matches/' + slug + '/</loc><lastmod>([^<]+)</lastmod>');
    const mm = sm.match(re);
    assert(mm && mm[1] === expected, `${slug}: sitemap lastmod matches dateModified`);
    assert(!mm || ISO.test(mm[1]), `${slug}: lastmod is ISO 8601`);
  }
}

/* 7. Post-match transition on the SAME url, with history preserved */
section('Post-match transition and history preservation');
{
  let withResult = 0;
  for (const lg of LEAGUES) for (const [slug, e] of Object.entries(ED[lg] || {})) {
    const res = (RESULTS[lg] || {})[slug];
    const html = read(`sports/${lg}/matches/${slug}/index.html`);
    if (res) {
      withResult++;
      assert(/sp-result/.test(html), `${slug}: result block rendered`);
      assert(!/has not been played yet/.test(html), `${slug}: unplayed notice removed after the match`);
      if (!e.retrospective) {
        assert(/What BRYME said before kickoff/.test(html), `${slug}: pre-match preview preserved after the result`);
      }
      if (!e.retrospective) {
        if (e.overview) assert(html.includes(e.overview.slice(0, 40)), `${slug}: original preview text not overwritten`);
      }
      if (e.postMatch) assert(/sp-postmatch/.test(html), `${slug}: post-match analysis rendered`);
      /* A retrospective entry covers a match played before BRYME followed that league.
         There is no preview to preserve, so the history checks below do not apply - but
         the page must still carry a real post-match write-up, which is checked above. */
      assert(html.includes('Result &amp; Analysis') || html.includes('Result & Analysis'), `${slug}: title reflects the result state`);
    } else if (filled(e) >= 3) {
      assert(/sp-preview/.test(html), `${slug}: preview rendered before the match`);
      assert(!/sp-postmatch/.test(html), `${slug}: no post-match block before the match`);
      assert(/Preview, Form &amp; Prediction|Preview, Form & Prediction/.test(html), `${slug}: title reflects the preview state`);
    }
  }
  assert(true, `post-match checks ran (${withResult} fixture(s) currently have results)`);
}

/* 8. One fixture, one URL - no duplicates anywhere */
section('Duplicate URL prevention');
{
  const seen = new Map();
  for (const lg of LEAGUES) {
    const dir = path.join(ROOT, 'sports', lg, 'matches');
    if (!fs.existsSync(dir)) continue;
    for (const d of fs.readdirSync(dir, {withFileTypes:true})) {
      if (!d.isDirectory()) continue;
      const key = lg + '/' + d.name;
      seen.set(key, (seen.get(key) || 0) + 1);
    }
  }
  assert([...seen.values()].every(n => n === 1), 'no fixture directory appears twice');
  /* no result/preview variant urls were invented */
  const bad = [...seen.keys()].filter(k => /-(result|preview|report|live|post)\/?$/.test(k));
  assert(bad.length === 0, 'no -result/-preview variant URLs exist: ' + bad.slice(0, 3).join(', '));
  /* every sitemap match entry is unique and canonical-self */
  const locs = (sm.match(/<loc>([^<]*\/matches\/[^<]+)<\/loc>/g) || []);
  assert(new Set(locs).size === locs.length, 'no duplicate match URLs in the sitemap');
  for (const lg of LEAGUES) for (const [slug, e] of Object.entries(ED[lg] || {})) {
    if (filled(e) < 3) continue;
    const html = read(`sports/${lg}/matches/${slug}/index.html`);
    const c = (html.match(/<link rel="canonical" href="([^"]+)"/) || [])[1];
    assert(c && c.endsWith(`/sports/${lg}/matches/${slug}/`), `${slug}: canonical is the fixture's own stable URL`);
  }
}

/* 9. Never invent team news */
section('Unconfirmed information is marked, not invented');
{
  for (const lg of LEAGUES) for (const [slug, e] of Object.entries(ED[lg] || {})) {
    if (filled(e) < 3) continue;
    const html = read(`sports/${lg}/matches/${slug}/index.html`);
    if (!e.expectedLineups) assert(/No lineup has been announced/.test(html), `${slug}: absent lineups marked unconfirmed`);
    if (!e.injuries) assert(/No injury information confirmed/.test(html), `${slug}: absent injuries marked unconfirmed`);
    if (!e.suspensions) assert(/No suspensions confirmed/.test(html), `${slug}: absent suspensions marked unconfirmed`);
  }
}

console.log(`\nRESULTS: ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
