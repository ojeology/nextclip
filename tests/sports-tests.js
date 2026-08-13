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

/* 2. Transfer pages */
section('Transfer trackers');
{
  for (const lg of ['premier-league', 'la-liga', 'serie-a', 'bundesliga', 'ligue-1']) {
    const s = read('sports/transfers/' + lg + '-2026-27/index.html');
    assert(/Transfer In/.test(s) && /Transfer Out/.test(s), lg + ': in/out sections');
    assert(/Confirmed/.test(s) && /Reported/.test(s) && /Rumoured/.test(s), lg + ': status legend');
    assert(/Transfer information changes frequently/.test(s), lg + ': disclaimer');
    assert(/never presented as confirmed/.test(s), lg + ': no rumour-as-confirmed');
    var canon = s.match(/rel="canonical" href="([^"]+)"/);
    assert(canon && canon[1] === 'https://ojeology.github.io/nextclip/sports/transfers/' + lg + '-2026-27/', lg + ': canonical correct (' + (canon && canon[1]) + ')');
    assert(!/href="https:\/\/ojeology\.github\.io\/nextclip\/transfers\//.test(s), lg + ': no unprefixed links');
  }
  const hub = read('sports/transfers/index.html');
  assert(hub.indexOf('Transfer trackers 2026/27') > -1, 'transfers hub title');
  assert(hub.indexOf('Managers In &amp; Out') > -1, 'transfers hub links managers');
}

/* 3. Managers page */
section('Managers');
{
  const s = read('sports/managers-2026-27/index.html');
  assert(/Managers In &amp; Out — 2026\/27/.test(s), 'managers title');
  for (const lg of ['Premier League', 'La Liga', 'Serie A', 'Bundesliga', 'Ligue 1']) assert(s.indexOf(lg) > -1, 'league section: ' + lg);
  assert(/once confirmed by clubs/.test(s), 'confirmation-only note');
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
  assert(/@media\(min-width:1440px\)\{\.sp-hero-track\{grid-auto-columns:calc\(\(100% - 64px\)\/5\)\}/.test(css), 'desktop: five cards');
  assert(/\.sp-table\{[^}]*min-width:640px/.test(css), 'tables scroll horizontally instead of overflowing');
}

console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
