/* NEXTCLIP test suite — title page quality (year index, related, hero, seasons, stories)
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/titlepage-tests.js */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
const read = p => fs.readFileSync(path.join(ROOT, p), 'utf8');
const relTitles = (html) => {
  const m = html.match(/You may also like<\/h2>([\s\S]*?)(?:<h2>|<\/article>)/);
  return m ? Array.from(m[1].matchAll(/<h3>([^<]+)<\/h3>/g)).map(x => x[1]) : [];
};

/* 1. Year index respects content type */
section('Year index is type-aware');
{
  const aib = read('series/alice-in-borderland/index.html');
  assert(/<dt>Year index<\/dt><dd><a href="https:\/\/ojeology\.github\.io\/nextclip\/series\/2020\/">2020 series<\/a>/.test(aib), 'Alice in Borderland -> /series/2020/ "2020 series"');
  assert(!/year\/2020\//.test(aib), 'no movie year link on series page');
  assert(/<div class="crumb">.*?\/ <a href="https:\/\/ojeology\.github\.io\/nextclip\/series\/2020\/">2020<\/a> \/ Alice in Borderland/.test(aib.replace(/\n/g, ' ')), 'breadcrumb: Home / TV Series / 2020 / Alice in Borderland');
  const interstellar = read('movie/interstellar/index.html');
  assert(/<dt>Year index<\/dt><dd><a href="https:\/\/ojeology\.github\.io\/nextclip\/year\/2014\/">2014 movies<\/a>/.test(interstellar), 'Interstellar -> /year/2014/ "2014 movies"');
  const solo = read('anime/solo-leveling/index.html');
  assert(/<dt>Year index<\/dt><dd><a href="https:\/\/ojeology\.github\.io\/nextclip\/anime\/2024\/">2024 anime<\/a>/.test(solo), 'Solo Leveling -> /anime/2024/ "2024 anime"');
  const pb = read('series/prison-break/index.html');
  assert(/<dt>Year index<\/dt><dd><a href="https:\/\/ojeology\.github\.io\/nextclip\/series\/2005\/">2005 series<\/a>/.test(pb), 'Prison Break -> /series/2005/');
  // audit: no series/anime page links a /year/ (movie) index
  let bad = [];
  for (const d of ['series', 'anime']) {
    for (const slug of fs.readdirSync(path.join(ROOT, d))) {
      if (!/^\d{4}$/.test(slug)) continue;
    }
    for (const f of fs.readdirSync(path.join(ROOT, d))) {
      if (!fs.existsSync(path.join(ROOT, d, f, 'index.html'))) continue;
      const html = read(d + '/' + f + '/index.html');
      if (/<dt>Year index<\/dt><dd><a href="https:\/\/ojeology\.github\.io\/nextclip\/year\//.test(html)) bad.push(d + '/' + f);
    }
  }
  assert(bad.length === 0, 'no series/anime page links the movie year index (got ' + bad.join(', ') + ')');
}

/* 2. Year pages exist per type */
section('Per-type year pages');
{
  assert(read('series/2020/index.html').includes('Series from 2020'), '/series/2020/ exists');
  assert(read('anime/2020/index.html').includes('Anime from 2020'), '/anime/2020/ exists');
  assert(read('year/2020/index.html').includes('Movies from 2020'), '/year/2020/ exists');
}

/* 3. Related titles: manual + themed, no generic superhero spill */
section('Related titles quality');
{
  const aib = relTitles(read('series/alice-in-borderland/index.html'));
  const expectFirst = ['Squid Game', 'All of Us Are Dead'];
  assert(aib[0] === 'Squid Game' && aib[1] === 'All of Us Are Dead', 'AIB: manual picks first (got ' + aib.slice(0, 4).join(', ') + ')');
  assert(aib.every(t => !/Secret Invasion|Andor/.test(t)), 'no unrelated superhero titles in AIB related');
  assert(aib.length >= 6, 'AIB has 6+ related');
  const rel2 = relTitles(read('series/alice-in-borderland/index.html'));
  assert(JSON.stringify(aib) === JSON.stringify(rel2), 'related list is deterministic across reads');
  const solo = relTitles(read('anime/solo-leveling/index.html'));
  assert(solo[0] === 'Demon Slayer: Kimetsu no Yaiba' || solo[0] === 'Jujutsu Kaisen', 'Solo Leveling: themed picks first (got ' + solo[0] + ')');
}

/* 4. Hero: WATCH TRAILER + READ BRYME STORY when article exists */
section('Hero CTAs');
{
  const aib = read('series/alice-in-borderland/index.html');
  assert(/WATCH TRAILER/.test(aib), 'AIB hero: WATCH TRAILER');
  assert(/READ BRYME STORY/.test(aib), 'AIB hero: READ BRYME STORY (article exists)');
  const titanic = read('movie/titanic/index.html');
  assert(!/READ BRYME STORY/.test(titanic), 'Titanic hero: no story CTA (no article)');
}

/* 5. Editorial rating label */
section('Editorial rating');
{
  const sq = read('series/squid-game/index.html');
  assert(/★ 9\/10 · BRYME Editorial/.test(sq), 'Squid Game badge: "★ 9/10 · BRYME Editorial"');
  assert(/not IMDb, Rotten Tomatoes or audience ratings/.test(sq), 'badge explicitly disclaims third-party rating sources');
  assert(!/<span class="badge"[^>]*>[^<]*(?:IMDb|Rotten Tomatoes)[^<]*<\/span>/.test(sq), 'no third-party rating shown as the badge value');
}

/* 6. Seasons architecture */
section('Seasons (series/anime only)');
{
  assert(/<h2>Seasons<\/h2>/.test(read('series/prison-break/index.html')), 'Prison Break shows Seasons');
  assert(/<h2>Seasons<\/h2>/.test(read('series/squid-game/index.html')), 'Squid Game shows Seasons');
  assert(/<h2>Seasons<\/h2>/.test(read('series/alice-in-borderland/index.html')), 'Alice in Borderland shows Seasons');
  assert(!/<h2>Seasons<\/h2>/.test(read('movie/interstellar/index.html')), 'Interstellar (movie) has NO Seasons');
  assert(!/<h2>Seasons<\/h2>/.test(read('movie/titanic/index.html')), 'Titanic has NO Seasons');
  const pb = read('series/prison-break/index.html');
  assert(/Season 5 \(Revival\)/.test(pb) && /9 episodes/.test(pb), 'Prison Break S5 data renders');
  const ld = JSON.parse(read('series/squid-game/index.html').match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  const tv = ld.find(x => x['@type'] === 'TVSeries');
  assert(tv.numberOfSeasons === 3, 'Squid Game schema numberOfSeasons = 3');
  assert(tv.numberOfEpisodes === 22, 'Squid Game schema numberOfEpisodes = 22 (9+7+6)');
}

/* 7. Stories section: cards with READ ARTICLE, absent when no articles */
section('Related stories');
{
  const aib = read('series/alice-in-borderland/index.html');
  assert(/Latest stories about Alice in Borderland/.test(aib), 'AIB: Latest stories section');
  assert(/READ ARTICLE →/.test(aib), 'AIB: READ ARTICLE card CTA');
  const titanic = read('movie/titanic/index.html');
  assert(!/Latest stories about/.test(titanic), 'Titanic: no empty stories section');
}

/* 8. SEO essentials on a sample */
section('SEO essentials');
{
  const aib = read('series/alice-in-borderland/index.html');
  assert(/<title>Alice in Borderland \(2020\) – Series Overview, Trailer &amp; BRYME/.test(aib), 'unique title tag');
  assert(/<link rel="canonical" href="https:\/\/ojeology\.github\.io\/nextclip\/series\/alice-in-borderland\/">/.test(aib), 'canonical');
  assert(/property="og:title"/.test(aib) && /property="og:url"/.test(aib), 'Open Graph');
  const ld = JSON.parse(aib.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert(ld.some(x => x['@type'] === 'TVSeries') && ld.some(x => x['@type'] === 'BreadcrumbList'), 'TVSeries + BreadcrumbList schema');
}

console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
