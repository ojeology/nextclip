/* BRYME Sports test suite — hero carousel, transfers, managers, table, FPL, placeholders
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/sports-tests.js */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
const read = p => fs.readFileSync(path.join(ROOT, p), 'utf8');

/* 1. PL hub hero carousel */
section('PL hero carousel');
{
  const s = read('sports/premier-league/index.html');
  assert(/<h1>The Premier League Is Here<\/h1>/.test(s), 'kicker: THE PREMIER LEAGUE IS HERE');
  assert(/Everything you need to know about the 2026\/27 season/.test(s), 'subtitle: 2026/27 season');
  assert((s.match(/class="sp-hero-card/g) || []).length === 5, 'exactly 5 hero cards');
  const tags = ['MATCHWEEK AHEAD', 'FPL WATCH', "WHO'S READY TO BREAK OUT?", "WHO'S IN? WHO'S OUT?", "THE MATCHES YOU CAN'T MISS"];
  for (const t of tags) assert(s.indexOf(t) > -1, 'hero card tag: ' + t);
  assert(/data-sp-hero-prev/.test(s) && /data-sp-hero-next/.test(s), 'carousel arrows present');
  assert(/href="https:\/\/ojeology\.github\.io\/nextclip\/sports\/premier-league\/matchweek-1-preview\/"/.test(s), 'card 1 links to matchweek preview');
  assert(/href="https:\/\/ojeology\.github\.io\/nextclip\/sports\/fpl\/gameweek-1-players-to-watch\/"/.test(s), 'card 2 links to FPL watch');
  assert(s.indexOf('NEXTCLIP') === -1, 'no NEXTCLIP literal');
}

/* 2b. Full PL tracker (populated) */
section('PL transfer tracker (populated)');
{
  const s = read('sports/transfers/premier-league-2026-27/index.html');
  assert(/LIVE TRANSFER WINDOW/.test(s), 'live window banner');
  assert(!/snapshot/i.test(s), 'never described as a snapshot');
  assert(/Last updated: 13 August 2026/.test(s), 'last updated date');
  assert((s.match(/class="sp-club"/g) || []).length === 20, 'all 20 clubs');
  assert((s.match(/<h3>Players In<\/h3>/g) || []).length === 20, '20 Players In sections');
  assert((s.match(/<h3>Players Out<\/h3>/g) || []).length === 20, '20 Players Out sections');
  assert((s.match(/Manager:/g) || []).length === 20, '20 manager lines');
  assert(s.indexOf('Bruno Guimarães') > -1 && s.indexOf('Morgan Rogers') > -1 && s.indexOf('Sandro Tonali') > -1 && s.indexOf('Elliot Anderson') > -1, 'key transfers present');
  assert(/Rumour \/ Reported interest — not confirmed/.test(s), 'rumours section separated');
  assert(s.indexOf('Bouaddi') > -1 && s.indexOf('Rodri') > -1, 'Man City rumours in the rumours section');
  assert((s.match(/sports\/pl\/[a-z-]+\.svg/g) || []).length === 20, '20 official PL crest SVGs');
  assert((s.match(/sports\/club-[a-z-]+\.svg/g) || []).length === 0, 'no AI-generated PL crests remain on the PL page');
  assert(s.indexOf('© Copyright The Football Association Premier League Limited, 2016') > -1, 'required PL copyright notice present');
  assert(/not affiliated with, endorsed or sponsored/.test(s), 'non-affiliation statement present');
  assert(/Transfer window still open/.test(s), 'window-still-open footer note');
  assert(/Discover what you love, learn what you need, and find what's next/.test(s), 'BRYME signoff');
  assert(/Transfer information changes frequently/.test(s), 'frequency disclaimer');
  for (const st of ['Confirmed', 'Departed', 'Released', 'Retired', 'Loan', 'Free']) assert(s.indexOf(st) > -1, 'status vocabulary: ' + st);
  var canon = s.match(/rel="canonical" href="([^"]+)"/);
  assert(canon && canon[1] === 'https://ojeology.github.io/nextclip/sports/transfers/premier-league-2026-27/', 'PL tracker canonical correct');
  assert(s.indexOf('NEXTCLIP') === -1, 'no NEXTCLIP literal');
}

/* 2c. League trackers — all four populated (user-verified), truth-first rules */
section('League transfer trackers');
{
  const leagues = [['la-liga', 'La Liga', 20], ['serie-a', 'Serie A', 20], ['bundesliga', 'Bundesliga', 18], ['ligue-1', 'Ligue 1', 18]];
  for (const [id, name, clubCount] of leagues) {
    const s = read('sports/transfers/' + id + '-2026-27/index.html');
    assert(new RegExp('>' + name.replace('+', '\\+') + ' Transfers 2026/27<').test(s), id + ': page title');
    assert(/LIVE TRANSFER WINDOW/.test(s), id + ': live banner');
    assert(/Truth first — nothing fabricated/.test(s), id + ': truth banner');
    assert((s.match(/class="sp-club"/g) || []).length === clubCount, id + ': ' + clubCount + ' club cards');
    const officialCrests = {
      'la-liga': ['ll/', 20], 'bundesliga': ['bl/', 17], 'ligue-1': ['l1/', 18], 'serie-a': ['sa/', 7]
    }[id];
    const abstractCrests = { 'la-liga': 0, 'bundesliga': 1, 'ligue-1': 0, 'serie-a': 13 }[id];
    const o = s.split('assets/img/sports/' + officialCrests[0]).length - 1;
    const a = s.split('assets/img/sports/club-').length - 1;
    assert(o === officialCrests[1], id + ': ' + officialCrests[1] + ' official crests (got ' + o + ')');
    assert(a === abstractCrests, id + ': ' + abstractCrests + ' abstract crests (got ' + a + ')');
    assert(/sp-credits/.test(s), id + ': attribution/credit line present');
    const rows = (s.match(/<tr><td><b>/g) || []).length;
    assert(rows > 15, id + ': populated with confirmed transfers (' + rows + ' rows)');
    assert(/Last updated: 13 August 2026/.test(s), id + ': real last-updated date');
    assert(!/must be verified before publishing/.test(s), id + ': composition verified (no warning note)');
    assert(/Status legend/.test(s), id + ': status legend');
    assert(/Transfer window still open/.test(s), id + ': window note');
    assert(/Discover what you love, learn what you need, and find what's next/.test(s), id + ': signoff');
    assert(s.indexOf('NEXTCLIP') === -1, id + ': no NEXTCLIP literal');
  }
  // La Liga
  {
    const s = read('sports/transfers/la-liga-2026-27/index.html');
    assert(s.indexOf('Yan Diomande') > -1 && s.indexOf('Mourinho') > -1 && s.indexOf('Aubameyang') > -1 && s.indexOf('Sergio Canales') > -1, 'la-liga: key deals present');
    assert(!/Rumour \/ Reported interest/.test(s), 'la-liga: no rumours box (data had none)');
  }
  // Serie A
  {
    const s = read('sports/transfers/serie-a-2026-27/index.html');
    assert(s.indexOf('Gonçalo Ramos') > -1 && s.indexOf('Dovbyk') > -1 && s.indexOf('Chalobah') > -1 && s.indexOf('Akor Adams') > -1, 'serie-a: key deals present');
    assert(/Rumour \/ Reported interest — not confirmed/.test(s), 'serie-a: rumours box present');
    assert(s.indexOf('Vlahović') > -1 && s.indexOf('Lukaku') > -1, 'serie-a: rumours kept out of confirmed tables');
    assert(/Nine clubs changed head coach/.test(s), 'serie-a: league note (9 manager changes)');
  }
  // Bundesliga
  {
    const s = read('sports/transfers/bundesliga-2026-27/index.html');
    assert(s.indexOf('Saibari') > -1 && s.indexOf('Karetsas') > -1 && s.indexOf('Höfler') > -1 && s.indexOf('Adamu') > -1, 'bundesliga: key deals present');
    assert(s.indexOf('Nmecha') > -1, 'bundesliga: Nmecha rumour present');
    assert(/Rumour \/ Reported interest/.test(s), 'bundesliga: rumours box present');
    assert(/Manuel Neuer has signed a one-year contract extension/.test(s), 'bundesliga: Neuer renewal noted as not a transfer');
  }
  // Ligue 1
  {
    const s = read('sports/transfers/ligue-1-2026-27/index.html');
    assert(s.indexOf('Koleosho') > -1 && s.indexOf('Génésio') > -1 && s.indexOf('Abline') > -1 && s.indexOf('Mayenda') > -1, 'ligue-1: key deals present');
    assert(/18 clubs, 12 with a new head coach/.test(s), 'ligue-1: record manager-changes note');
    assert(/Metz and Nantes were relegated/.test(s), 'ligue-1: relegation/promotion note');
    assert(/Rumour \/ Reported interest/.test(s), 'ligue-1: rumours box present');
    assert(s.indexOf('Adeyemi') > -1, 'ligue-1: flagged Lyon/Adeyemi item present');
  }
}

/* 3. Managers page (populated from the trackers) */
section('Managers');
{
  const s = read('sports/managers-2026-27/index.html');
  assert(/Managers In &amp; Out — 2026\/27/.test(s), 'managers title');
  for (const lg of ['Premier League', 'La Liga', 'Serie A', 'Bundesliga', 'Ligue 1']) assert(s.indexOf(lg) > -1, 'league section: ' + lg);
  assert((s.match(/sp-mgr-club/g) || []).length === 96, 'all 96 clubs listed (got ' + (s.match(/sp-mgr-club/g) || []).length + ')');
  assert((s.match(/sports\/pl\/[a-z-]+\.svg/g) || []).length === 20, 'managers page: 20 official PL crests');
  assert((s.match(/sports\/ll\/[a-z0-9-]+\.png/g) || []).length === 20, 'managers page: 20 official La Liga shields');
  assert((s.match(/sports\/bl\/[a-z0-9-]+\.svg/g) || []).length === 17, 'managers page: 17 official Bundesliga crests');
  assert((s.match(/sports\/l1\/[a-z0-9-]+\.webp/g) || []).length === 18, 'managers page: 18 official Ligue 1 crests');
  assert((s.match(/sports\/sa\/[a-z0-9-]+\.(?:png|webp)/g) || []).length === 7, 'managers page: 7 official Serie A crests');
  assert((s.match(/sports\/club-[a-z0-9-]+\.svg/g) || []).length === 14, 'managers page: 14 abstract crests (HSV + 13 Serie A)');
  assert(s.indexOf('© Copyright The Football Association Premier League Limited, 2016') > -1, 'managers page: PL copyright notice');
  assert((s.match(/sp-mgr-new/g) || []).length > 30, 'NEW manager badges present (' + (s.match(/sp-mgr-new/g) || []).length + ')');
  assert((s.match(/sp-mgr-keep/g) || []).length > 40, 'No-change badges present (' + (s.match(/sp-mgr-keep/g) || []).length + ')');
  assert(s.indexOf('Pending verification') === -1, 'zero pending managers');
  for (const name of ['Mourinho', 'Kompany', 'Allegri', 'Xabi Alonso', 'Luis Enrique', 'Arteta', 'Demichelis', 'Génésio', 'Maresca']) {
    assert(s.indexOf(name) > -1, 'manager present: ' + name);
  }
  assert(/Last updated: 13 August 2026/.test(s), 'managers last updated date');
  assert(s.indexOf('NEXTCLIP') === -1, 'no NEXTCLIP literal');
}

/* 4. Editorial table */
section('Editorial table');
{
  const s = read('sports/premier-league/table/index.html');
  assert(/BRYME Editorial Prediction — Not the Official League Table/.test(s), 'clear not-official label');
  assert(/not a guarantee/.test(s), 'not-a-guarantee note');
  for (const c of ['Position', 'Team', 'Predicted points', 'Predicted wins', 'Predicted draws', 'Predicted losses', 'Predicted goal difference']) {
    assert(s.indexOf(c) > -1, 'table column: ' + c);
  }
  assert(/official Premier League table/.test(s), 'can be replaced by official table');
}

/* 5. FPL */
section('FPL');
{
  const hub = read('sports/fpl/index.html');
  assert(/Fantasy Premier League/.test(hub), 'FPL hub title');
  for (const sec of ['Gameweek Players to Watch', 'Popular Picks', 'Differential Picks', 'Captaincy Discussion', 'Fixture Difficulty', 'Injury Updates', 'New Signings to Watch', 'Gameweek Review']) {
    assert(hub.indexOf(sec) > -1, 'FPL section: ' + sec);
  }
  const gw = read('sports/fpl/gameweek-1/index.html');
  assert(/FPL Gameweek 1/.test(gw), 'gameweek hub title');
  assert(/No picks, predictions or difficulty ratings are shown before they are researched/.test(gw), 'no fabricated picks');
}

/* 6. Article placeholders */
section('Article placeholders');
{
  for (const r of ['premier-league/matchweek-1-preview', 'premier-league/players-to-watch-matchweek-1',
                   'premier-league/injuries-matchweek-1', 'premier-league/biggest-matches-matchweek-1',
                   'fpl/gameweek-1-players-to-watch']) {
    const s = read('sports/' + r + '/index.html');
    assert(/<h1>/.test(s), r + ': h1');
    assert(/By BRYME Sports Editorial/.test(s), r + ': author/editorial label');
    assert(/Original report/.test(s), r + ': source section');
    assert(/structured placeholder/.test(s), r + ': honest placeholder state');
    assert(/rel="canonical" href="https:\/\/ojeology\.github\.io\/nextclip\/sports\//.test(s), r + ': canonical has sports/ prefix');
    assert(/sp-rel/.test(s), r + ': related-content block');
    assert(JSON.parse(s.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]).some(d => d['@type'] === 'Article'), r + ': Article schema');
  }
}

/* 7. Match centre + fixtures/results */
section('Match centre, fixtures, results');
{
  const mc = read('sports/premier-league/matches/index.html');
  assert(/Premier League Matchweek 1/.test(mc), 'match centre title');
  assert(/No fixtures are shown before they are verified/.test(mc), 'no fabricated fixtures');
  for (const sec of ['Match overview', 'Head-to-head record', 'Expected lineups', 'Tactical matchup', 'BRYME editorial outlook', 'Editorial score prediction', 'Post-match analysis']) {
    assert(mc.indexOf(sec) > -1, 'match page section: ' + sec);
  }
  assert(read('sports/premier-league/fixtures/index.html').indexOf('kickoff times are confirmed') > -1, 'fixtures: verified-only note');
  assert(read('sports/premier-league/results/index.html').indexOf('only after matches are actually played') > -1, 'results: no assumed results');
}

/* 8. Sitemap coverage + no stray unprefixed pages */
section('Sitemap');
{
  const sm = read('sitemap.xml');
  for (const p of ['/sports/premier-league/matchweek-1-preview/', '/sports/fpl/gameweek-1/', '/sports/transfers/premier-league-2026-27/', '/sports/managers-2026-27/', '/sports/premier-league/table/', '/sports/premier-league/matches/']) {
    assert(sm.indexOf('nextclip' + p) > -1, 'sitemap: ' + p);
  }
  assert(!/nextclip\/premier-league\//.test(sm), 'no unprefixed PL URLs in sitemap');
  assert(!/nextclip\/fpl\//.test(sm), 'no unprefixed FPL URLs in sitemap');
}

/* 9. Mobile CSS — one card on mobile, responsive */
section('Responsive CSS');
{
  const css = read('assets/site.css');
  assert(/@media\(max-width:640px\)\{\.sp-hero-track\{grid-auto-columns:calc\(100% - 40px\)\}/.test(css), 'mobile: one hero card at a time');
  assert(/@media\(max-width:1024px\)\{\.sp-hero-track\{grid-auto-columns:calc\(\(100% - 32px\)\/2\)\}/.test(css), 'tablet: two cards');
  assert(css.indexOf('@media(min-width:1440px){.sp-hero-track{grid-auto-columns:calc((100% - 64px)/5);grid-auto-flow:column}}') > -1, 'desktop: five cards, no overflow');
  assert(/\.sp-table\{[^}]*min-width:640px/.test(css), 'tables scroll horizontally instead of overflowing');
}

console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
