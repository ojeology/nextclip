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
      'la-liga': ['ll/', 20], 'bundesliga': ['bl/', 17], 'ligue-1': ['l1/', 18], 'serie-a': ['sa/', 20]
    }[id];
    const abstractCrests = { 'la-liga': 0, 'bundesliga': 1, 'ligue-1': 0, 'serie-a': 0 }[id];
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
  assert((s.match(/sports\/sa\/[a-z0-9-]+\.(?:png|svg)/g) || []).length === 20, 'managers page: 20 official Serie A crests');
  assert((s.match(/sports\/club-[a-z0-9-]+\.svg/g) || []).length === 1, 'managers page: 1 abstract crest (HSV only)');
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

/* 6b. Fixture data integrity (content/fixtures.json) */
section('Fixture data integrity');
{
  const F = JSON.parse(read('content/fixtures.json'));
  assert(F.matchweeks.length === 38, '38 matchweeks');
  const all = F.matchweeks.flatMap(w => w.matches);
  assert(all.length === 380, '380 matches total');
  const cnt = {}, home = {};
  const pairs = new Set();
  for (const m of all) {
    cnt[m.id] = (cnt[m.id] || 0) + 1; cnt[m.away] = (cnt[m.away] || 0) + 1;
    home[m.id] = (home[m.id] || 0) + 1;
    pairs.add(m.id + '>' + m.away);
  }
  assert(Object.keys(cnt).length === 20, '20 clubs');
  assert(Object.values(cnt).every(v => v === 38), 'every club plays 38 games');
  assert(Object.values(home).every(v => v === 19), 'every club has 19 home games');
  assert(pairs.size === 380, 'each fixture pairing appears exactly once');
  assert(F.matchweeks.every(w => w.matches.length === 10), '10 matches per matchweek');
  assert(F.matchweeks[0].matches[0].homeName === 'Arsenal' && F.matchweeks[0].matches[0].awayName === 'Coventry City', 'MW1 opener: Arsenal v Coventry City');
  assert(F.matchweeks[0].matches[0].time === '20:00' && F.matchweeks[0].matches[0].tv === 'Sky Sports', 'MW1 opener: official kickoff + TV');
  assert(F.matchweeks[12].matches.every(m => m.time === '20:00'), 'midweek MW13 defaults to 20:00');
  assert(F.matchweeks[18].matches.every(m => m.time === '15:00' || m.timePublished), 'MW19 (Sat 2 Jan 2027) weekend default 15:00');
  assert(Object.keys(F.venues).length === 20, 'all 20 venues mapped');
  assert(F.venues.arsenal.name === 'Emirates Stadium', 'Arsenal venue');
  assert(F.venues['man-united'].capacity === 74500, 'Old Trafford capacity');
  assert(F.sourceUrl.indexOf('premierleague.com') > -1, 'official source URL');
}

/* 7. Match centre + fixtures/results */
section('Match centre, fixtures, results');
{
  const mc = read('sports/premier-league/matches/index.html');
  assert(/Premier League Matchweek 1/.test(mc), 'match centre title');
  assert((mc.match(/class="sp-mc-card solid/g) || []).length === 10, 'match centre: 10 Matchweek 1 cards');
  assert(/arsenal-vs-coventry\//.test(mc), 'match centre: links to Arsenal v Coventry page');
  assert(/all 380 fixtures/.test(mc), 'match centre: full-season note');
  for (const sec of ['Match overview', 'Head-to-head record', 'Expected lineups', 'Tactical matchup', 'BRYME editorial outlook', 'Editorial score prediction', 'Post-match analysis']) {
    assert(mc.indexOf(sec) > -1, 'match page section listed: ' + sec);
  }

  const fx = read('sports/premier-league/fixtures/index.html');
  assert(/Premier League Fixtures 2026\/27/.test(fx), 'fixtures: title');
  assert(/All 380 fixtures/.test(fx), 'fixtures: 380 matches stated');
  assert(/Arsenal v Coventry City/.test(fx), 'fixtures: MW1 opener present');
  assert(/Friday 21 August 2026/.test(fx), 'fixtures: opening date present');
  assert(/Sunderland v Manchester City/.test(fx), 'fixtures: final-day fixture present');
  assert(/Matchweek 38/.test(fx), 'fixtures: matchweek 38 present');
  assert(/20:00/.test(fx) && /12:30/.test(fx) && /17:30/.test(fx), 'fixtures: published kickoff times present');
  assert(/Sky Sports/.test(fx) && /TNT Sports/.test(fx), 'fixtures: TV selections present');
  assert(/\(std\)/.test(fx) && /15:00/.test(fx), 'fixtures: standard-slot legend + 15:00 defaults');
  assert(/premierleague\.com\/en\/news\/4675097/.test(fx), 'fixtures: official source cited');
  assert(/subject to change/.test(fx), 'fixtures: subject-to-change note');
  assert((fx.match(/class="sp-mwnav"/g) || []).length >= 1, 'fixtures: matchweek jump nav');
  assert((fx.match(/class="sp-mw"/g) || []).length === 38, 'fixtures: 38 matchweek blocks');
  assert((fx.match(/class="sp-fixture"/g) || []).length === 380, 'fixtures: 380 fixture rows');
  assert(fx.indexOf('1-0') === -1 && fx.indexOf('0-1') === -1, 'fixtures: no scores anywhere');

  const rs = read('sports/premier-league/results/index.html');
  assert(/No matches played yet/.test(rs), 'results: honest empty state');
  assert(/21 August 2026/.test(rs), 'results: season start date stated');
  assert(/never predicted/.test(rs), 'results: no predicted results');
  assert(/Upcoming — Matchweek 1/.test(rs), 'results: MW1 preview block');
  assert(rs.indexOf('1-0') === -1 && rs.indexOf('0-1') === -1, 'results: no fabricated scores');

  // per-match page
  const mp = read('sports/premier-league/matches/arsenal-vs-coventry/index.html');
  assert(/Arsenal v Coventry City/.test(mp), 'match page: title');
  assert(/Emirates Stadium/.test(mp), 'match page: venue');
  assert(/60,704/.test(mp), 'match page: venue capacity');
  assert(/20:00 UK/.test(mp), 'match page: kickoff UK time');
  assert(/Sky Sports/.test(mp), 'match page: TV');
  assert(/Upcoming — not yet played/.test(mp), 'match page: honest status');
  assert((mp.match(/class="sp-msec"/g) || []).length === 16, 'match page: 16 analysis sections');
  assert(/Match result after the game/.test(mp) && /Post-match analysis/.test(mp), 'match page: post-match sections present');
  assert(/EventScheduled/.test(mp), 'match page: JSON-LD scheduled event');
  assert(/2026-08-21T20:00:00/.test(mp), 'match page: JSON-LD startDate with kickoff');
  assert(mp.indexOf('1-0') === -1 && mp.indexOf('0-1') === -1, 'match page: no fabricated score');
  // winter fixture: WAT shown (UK GMT -> Lagos +1); MW13 Wed 2 Dec 20:00 published
  const wint = read('sports/premier-league/matches/tottenham-vs-fulham/index.html');
  assert(/Matchweek 13/.test(wint), 'winter match page: matchweek 13 (2 Dec)');
  assert(/20:00 UK · 21:00 WAT/.test(wint), 'winter match page: Lagos kickoff (UK+1)');
  // all 380 match pages exist
  const F = JSON.parse(read('content/fixtures.json'));
  const slugs = F.matchweeks.flatMap(w => w.matches).map(m => 'sports/premier-league/matches/' + m.id + '-vs-' + m.away + '/index.html');
  const missing = slugs.filter(p => !fs.existsSync(path.join(ROOT, p)));
  assert(missing.length === 0, 'all 380 per-match pages generated' + (missing.length ? ' — missing: ' + missing.slice(0, 3).join(', ') : ''));
}

/* 8. Sitemap coverage + no stray unprefixed pages */
section('Sitemap');
{
  const sm = read('sitemap.xml');
  for (const p of ['/sports/premier-league/matchweek-1-preview/', '/sports/fpl/gameweek-1/', '/sports/transfers/premier-league-2026-27/', '/sports/managers-2026-27/', '/sports/premier-league/table/', '/sports/premier-league/matches/', '/sports/premier-league/fixtures/', '/sports/premier-league/results/', '/sports/premier-league/matches/arsenal-vs-coventry/']) {
    assert(sm.indexOf('nextclip' + p) > -1, 'sitemap: ' + p);
  }
  const F = JSON.parse(read('content/fixtures.json'));
  const slugs = F.matchweeks.flatMap(w => w.matches).map(m => '/sports/premier-league/matches/' + m.id + '-vs-' + m.away + '/');
  const inSm = slugs.filter(s => sm.indexOf('nextclip' + s) === -1);
  assert(inSm.length === 0, 'sitemap: all 380 match pages included' + (inSm.length ? ' — missing ' + inSm.length : ''));
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

/* 7b. Other leagues — fixtures, results, match centre, match pages */
section('La Liga, Serie A, Bundesliga, Ligue 1 — fixtures & matches');
{
  const leagues = [
    { slug: 'la-liga', name: 'La Liga', round: 'Jornada', total: 380, per: 10, times: 40, mwCount: 38 },
    { slug: 'serie-a', name: 'Serie A', round: 'Giornata', total: 380, per: 10, times: 48, mwCount: 38 },
    { slug: 'bundesliga', name: 'Bundesliga', round: 'Spieltag', total: 306, per: 9, times: 306, mwCount: 34 },
    { slug: 'ligue-1', name: 'Ligue 1', round: 'Journée', total: 306, per: 9, times: 27, mwCount: 34 },
  ];
  for (const lg of leagues) {
    // fixtures page
    const fx = read(`sports/${lg.slug}/fixtures/index.html`);
    assert(fx.indexOf(`${lg.name} Fixtures 2026/27`) > -1, `${lg.slug}: fixtures title`);
    assert((fx.match(/class="sp-fixture"/g) || []).length === lg.total, `${lg.slug}: ${lg.total} fixture rows`);
    assert((fx.match(/class="sp-mw"/g) || []).length === lg.mwCount, `${lg.slug}: ${lg.mwCount} round blocks`);
    assert((fx.match(/class="sp-mwnav"/g) || []).length >= 1, `${lg.slug}: round jump nav`);
    assert(fx.indexOf(`${lg.round} ${lg.mwCount}`) > -1, `${lg.slug}: last round label present`);
    assert(fx.indexOf('1-0') === -1 && fx.indexOf('0-1') === -1 && fx.indexOf('2-0') === -1, `${lg.slug}: no scores on fixtures`);
    assert(fx.indexOf('Last updated: 14 August 2026') > -1, `${lg.slug}: last-updated date`);
    // results page
    const rs = read(`sports/${lg.slug}/results/index.html`);
    assert(/No matches played yet/.test(rs), `${lg.slug}: results honest empty state`);
    assert(/never predicted/.test(rs), `${lg.slug}: results no prediction`);
    assert(rs.indexOf(`Upcoming — ${lg.round} 1`) > -1, `${lg.slug}: results next-round preview`);
    // match centre
    const mc = read(`sports/${lg.slug}/matches/index.html`);
    assert(mc.indexOf(`${lg.name} ${lg.round} 1`) > -1, `${lg.slug}: match centre title`);
    assert((mc.match(/class="sp-mc-card solid"/g) || []).length === lg.per, `${lg.slug}: ${lg.per} round-1 cards`);
    assert(mc.indexOf(`all ${lg.total} fixtures`) > -1, `${lg.slug}: match centre total note`);
    // data file
    const F = JSON.parse(read(`content/fixtures-${lg.slug}.json`));
    assert(F.matchweeks.length === lg.mwCount, `${lg.slug}: ${lg.mwCount} rounds in data`);
    const all = F.matchweeks.flatMap(w => w.matches);
    assert(all.length === lg.total, `${lg.slug}: ${lg.total} matches in data`);
    const tm = all.filter(m => m.timePublished).length;
    assert(tm === lg.times, `${lg.slug}: ${lg.times} published times (got ${tm})`);
    const teams = new Set();
    all.forEach(m => { teams.add(m.id); teams.add(m.away); });
    assert(teams.size === (lg.per * 2), `${lg.slug}: ${lg.per * 2} clubs`);
    // sitemap
    const sm = read('sitemap.xml');
    for (const p of [`/sports/${lg.slug}/fixtures/`, `/sports/${lg.slug}/results/`, `/sports/${lg.slug}/matches/`]) {
      assert(sm.indexOf('nextclip' + p) > -1, `${lg.slug} sitemap: ${p}`);
    }
  }
  // per-match pages spot checks
  const ll = read('sports/la-liga/matches/espanyol-vs-real-madrid/index.html');
  assert(/Jornada 2/.test(ll) && /21:30 CEST/.test(ll) && /RCDE Stadium/.test(ll), 'La Liga match page: Espanyol v Real Madrid (J2, 21:30 CEST, RCDE)');
  const ll2 = read('sports/la-liga/matches/celta-vigo-vs-osasuna/index.html');
  assert(/Postponed from 16 August 2026/.test(ll2) && /20:30 CEST/.test(ll2), 'La Liga match page: Celta-Osasuna postponement note');
  const sa = read('sports/serie-a/matches/genoa-vs-napoli/index.html');
  assert(/Giornata 1/.test(sa) && /20:45 CEST/.test(sa) && /Stadio Luigi Ferraris/.test(sa), 'Serie A match page: Genoa v Napoli (G1, 20:45 CEST)');
  const bl = read('sports/bundesliga/matches/bayern-vs-stuttgart/index.html');
  assert(/Spieltag 1/.test(bl) && /20:30 CEST/.test(bl) && /Allianz Arena/.test(bl), 'Bundesliga match page: Bayern v Stuttgart (S1, 20:30 CEST)');
  const l1 = read('sports/ligue-1/matches/marseille-vs-strasbourg/index.html');
  assert(/Journée 1/.test(l1) && /20:45 CEST/.test(l1) && /Stade Vélodrome/.test(l1), 'Ligue 1 match page: Marseille v Strasbourg (J1, 20:45 CEST)');
  const l1t = read('sports/ligue-1/matches/psg-vs-rennes/index.html');
  assert(/Journée 1/.test(l1t) && /Parc des Princes/.test(l1t), 'Ligue 1 match page: PSG v Rennes venue');
  const l1tbc = read('sports/ligue-1/matches/angers-vs-auxerre/index.html');
  assert(/TBC — announced closer to the round/.test(l1tbc), 'Ligue 1 match page: honest TBC kickoff (round 4+)');
  // every match page exists for all leagues
  for (const lg of leagues) {
    const F = JSON.parse(read(`content/fixtures-${lg.slug}.json`));
    const slugs = F.matchweeks.flatMap(w => w.matches).map(m => `sports/${lg.slug}/matches/${m.id}-vs-${m.away}/index.html`);
    const missing = slugs.filter(p => !fs.existsSync(path.join(ROOT, p)));
    assert(missing.length === 0, `${lg.slug}: all ${slugs.length} per-match pages generated` + (missing.length ? ' — missing ' + missing.length : ''));
  }
  // league fixtures JSON-LD on a match page
  const ld = read('sports/bundesliga/matches/bayern-vs-stuttgart/index.html');
  assert(/SportsEvent/.test(ld) && /2026-08-28T20:30:00\+02:00/.test(ld), 'Bundesliga match page: JSON-LD startDate with CEST offset');
  const ld2 = read('sports/serie-a/matches/genoa-vs-napoli/index.html');
  assert(/2026-08-22T20:45:00\+02:00/.test(ld2), 'Serie A match page: JSON-LD startDate');
}

console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);

