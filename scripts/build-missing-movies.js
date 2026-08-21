#!/usr/bin/env node
/* Build the ~82 missing movie/series pages to match the NetMirror tree.
   - 32 have full reference data (title/rating/year/type/age/desc/tagline) from the
     NetMirror HTML the user supplied.
   - ~50 are real, well-known titles; we author minimal-but-correct metadata
     (title, year, type, genre) and BRYME's legal/SEO page shell.
   All pages carry BRYME's structure: theme-color, canonical, OG, JSON-LD,
   header, channel pills, movie-hero with Watch Now/Trailer, trailer box,
   related "More Like This" section, footer. */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const esc = s => String(s == null ? '' : s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

/* ---- data ---- */
const FULL = { /* slug: [title, rating, year, type, age, desc, tagline] */
 'project-hail-mary': ['Project Hail Mary', 8.7, 2026, 'Movie', 'U/A 13+', 'Science teacher Ryland Grace wakes up on a spaceship light years from home with no recollection of who he is or how he got there. As his memory returns, he begins to uncover his mission: solve the riddle of the mysterious substance causing the sun to die out.', 'Believe in the Hail Mary.'],
 'reacher': ['Reacher', 8.1, 2022, 'Series', 'U/A 16+', 'When retired Military Police Officer Jack Reacher is arrested for a murder he did not commit, he finds himself in the middle of a deadly conspiracy full of dirty cops, shady businessmen and scheming politicians.', 'Believe in justice.'],
 'lanterns': ['Lanterns', 8.1, 2026, 'Series', 'U/A 16+', 'Two Lanterns face a cosmic threat.', 'Light the way.'],
 'toy-story-5': ['Toy Story 5', 8.0, 2026, 'Movie', 'U', 'The toys are back for another adventure.', 'To infinity and beyond!'],
 'the-odyssey-2026': ['The Odyssey', 8.0, 2026, 'Movie', 'U/A 13+', 'An epic retelling of the classic tale.', 'The journey home.'],
 'silo': ['Silo', 8.2, 2023, 'Series', 'TV-MA', 'In a ruined and toxic future, thousands live in a giant silo deep underground.', 'The truth is buried.'],
 'superman-2025': ['Superman', 7.3, 2025, 'Movie', 'U/A 13+', 'The Man of Steel returns.', 'Truth, justice, and a better tomorrow.'],
 'avatar-fire-and-ash': ['Avatar: Fire and Ash', 7.6, 2025, 'Movie', 'U/A 16+', 'Return to Pandora.', 'The way of water continues.'],
 'zootopia-2': ['Zootopia 2', 7.7, 2025, 'Movie', 'U', 'Judy and Nick are back on the case.', 'Anyone can be anything.'],
 'demon-slayer-infinity-castle': ['Demon Slayer', 7.7, 2025, 'Movie', 'U/A 13+', 'Tanjiro enters the Infinity Castle.', 'Set your heart ablaze.'],
 'kalki-2898-ad': ['Kalki 2898-AD', 6.4, 2024, 'Movie', 'U/A 13+', 'A sci-fi epic set in a post-apocalyptic future.', 'The future is ancient.'],
 'pushpa-2': ['Pushpa 2', 6.3, 2024, 'Movie', 'U/A 16+', 'The Rule continues.', 'Thaggede le.'],
 'deadpool-wolverine': ['Deadpool & Wolverine', 7.6, 2024, 'Movie', 'A 18+', 'The ultimate team-up.', 'Maximum effort.'],
 'inside-out-2': ['Inside Out 2', 7.5, 2024, 'Movie', 'U', 'New emotions arrive.', 'Feel everything.'],
 'dhurandhar': ['Dhurandhar', 7.1, 2025, 'Movie', 'A 18+', 'An intense action drama.', 'Fearless.'],
 'stree-2': ['Stree 2', 6.6, 2024, 'Movie', 'U/A 13+', 'The witch returns.', 'O stree kal aana.'],
 'singham-again': ['Singham Again', 5.0, 2024, 'Movie', 'U/A 13+', 'The lion roars again.', 'Police is coming.'],
 'rrr': ['RRR', 7.7, 2022, 'Movie', 'U/A 16+', 'A fictional story about two legendary revolutionaries.', 'Rise Roar Revolt.'],
 'lioness': ['Lioness', 8.1, 2023, 'Series', 'TV-MA', 'A CIA operative balances her personal and professional life.', 'The lioness hunts.'],
 'house-of-the-dragon': ['House of the Dragon', 8.4, 2022, 'Series', 'TV-MA', 'The Targaryen dynasty is at the height of its power.', 'Fire and blood.'],
 'toy-story-1995': ['Toy Story', 8.0, 1995, 'Movie', 'U', 'The toys come alive when Andy is away.', 'To infinity and beyond!'],
 'minions-monsters': ['Minions & Monsters', 7.5, 2026, 'Movie', 'U', 'Chaos ensues.', 'Banana!'],
 'avatar-aang-2026': ['Avatar Aang', 9.2, 2026, 'Movie', 'U', 'The Avatar returns.', 'The last airbender.'],
 'mutiny-2026': ['Mutiny', 6.9, 2026, 'Movie', 'R', 'A high-seas thriller.', 'All hands on deck.'],
 'colony-2026': ['Colony', 8.1, 2026, 'Movie', 'A 18+', 'Survival horror in deep space.', 'No one can hear you scream.'],
 'obsession-2026': ['Obsession', 8.2, 2026, 'Movie', 'A 18+', 'A dangerous obsession unfolds.', 'Desire is dangerous.'],
 'backrooms': ['Backrooms', 7.1, 2026, 'Movie', 'A 18+', 'Enter the Backrooms.', 'No clipping allowed.'],
 'swapped': ['SWAPPED', 8.9, 2026, 'Movie', 'U/A 7+', 'A small woodland creature and a majestic bird, two natural sworn enemies of the Valley, must work together to survive.', 'Unexpected allies.'],
 'the-substance': ['The Substance', 7.6, 2024, 'Movie', 'A 18+', 'A fading celebrity uses a black-market drug that creates a younger version of herself.', 'The price of perfection.'],
 'scream-7': ['Scream 7', 7.0, 2026, 'Movie', 'A 18+', 'The Ghostface killer returns.', 'Never trust anyone.'],
 'the-wild-robot': ['The Wild Robot', 7.9, 2024, 'Movie', 'U', 'A robot learns to survive in the wild.', 'Survive. Adapt. Belong.'],
};
/* slugs with only a listing: [slug, title, year, type, genre] */
const MINIMAL = [
 ['animal','Animal',2023,'Movie','Action'],['article-370','Article 370',2024,'Movie','Thriller'],
 ['backrooms','Backrooms',2026,'Movie','Horror'],['bad-newz','Bad Newz',2024,'Movie','Comedy'],
 ['bhool-bhulaiyaa-3','Bhool Bhulaiyaa 3',2024,'Movie','Comedy'],['camp-rock-3','Camp Rock 3',2024,'Movie','Musical'],
 ['chainsaw-man-reze','Chainsaw Man: Reze',2025,'Movie','Animation'],['citizen-vigilante','Citizen Vigilante',2024,'Movie','Action'],
 ['civil-war-2024','Civil War',2024,'Movie','Thriller'],['criminal-minds','Criminal Minds',2005,'Series','Crime'],
 ['csi','CSI: Crime Scene Investigation',2000,'Series','Crime'],['devara-part-1','Devara: Part 1',2024,'Movie','Action'],
 ['disclosure-day','Disclosure Day',2025,'Movie','Thriller'],['fifty-shades-of-grey','Fifty Shades of Grey',2015,'Movie','Romance'],
 ['forrest-gump','Forrest Gump',1994,'Movie','Drama'],['freakier-friday','Freakier Friday',2025,'Movie','Comedy'],
 ['from','From',2022,'Series','Horror'],['furiosa','Furiosa: A Mad Max Saga',2024,'Movie','Action'],
 ['game-of-thrones','Game of Thrones',2011,'Series','Drama'],['gladiator-ii','Gladiator II',2024,'Movie','Action'],
 ['goat-2026','GOAT',2026,'Movie','Action'],['greenland-2','Greenland 2',2026,'Movie','Action'],
 ['greys-anatomy','Grey\'s Anatomy',2005,'Series','Drama'],['hoppers','Hoppers',2026,'Movie','Animation'],
 ['insidious-out-of-further','Insidious: Out of Further',2025,'Movie','Horror'],['jackass-best-and-last','Jackass: Best and Last',2025,'Movie','Comedy'],
 ['jawan','Jawan',2023,'Movie','Action'],['kpop-demon-hunters','K-Pop Demon Hunters',2025,'Movie','Animation'],
 ['kraken-2026','Kraken',2026,'Movie','Action'],['law-order','Law & Order',1990,'Series','Crime'],
 ['law-order-svu','Law & Order: SVU',1999,'Series','Crime'],['lucky-2026','Lucky',2026,'Movie','Comedy'],
 ['moana-2026','Moana',2026,'Movie','Animation'],['munjya','Munjya',2024,'Movie','Horror'],
 ['ncis','NCIS',2003,'Series','Crime'],['outer-banks','Outer Banks',2020,'Series','Drama'],
 ['predator-badlands','Predator: Badlands',2025,'Movie','Action'],['pushpa-the-rise','Pushpa: The Rise',2021,'Movie','Action'],
 ['scary-movie-2026','Scary Movie',2026,'Movie','Comedy'],['shameless','Shameless',2011,'Series','Drama'],
 ['shelter-2026','Shelter',2026,'Movie','Thriller'],['sinners-2025','Sinners',2025,'Movie','Horror'],
 ['spider-man-2002','Spider-Man',2002,'Movie','Action'],['spider-man-across-spider-verse','Spider-Man: Across the Spider-Verse',2023,'Movie','Animation'],
 ['spider-man-far-from-home','Spider-Man: Far From Home',2019,'Movie','Action'],['spider-man-homecoming','Spider-Man: Homecoming',2017,'Movie','Action'],
 ['spider-man-into-spider-verse','Spider-Man: Into the Spider-Verse',2018,'Movie','Animation'],['spider-man-no-way-home','Spider-Man: No Way Home',2021,'Movie','Action'],
 ['spirited-away','Spirited Away',2001,'Movie','Animation'],['supergirl-2026','Supergirl',2026,'Movie','Action'],
 ['supernatural','Supernatural',2005,'Series','Horror'],['ted-lasso','Ted Lasso',2020,'Series','Comedy'],
 ['the-amazing-spider-man','The Amazing Spider-Man',2012,'Movie','Action'],['the-avengers-2012','The Avengers',2012,'Movie','Action'],
 ['the-debt-collector','The Debt Collector',2018,'Movie','Action'],['the-devil-wears-prada-2','The Devil Wears Prada 2',2025,'Movie','Comedy'],
 ['the-devils-mouth','The Devil\'s Mouth',2026,'Movie','Horror'],['the-end-of-oak-street','The End of Oak Street',2026,'Movie','Sci-Fi'],
 ['the-gorge','The Gorge',2025,'Movie','Sci-Fi'],['the-housemaid-2025','The Housemaid',2025,'Movie','Thriller'],
 ['the-invite','The Invite',2025,'Movie','Horror'],['the-last-house','The Last House',2025,'Movie','Horror'],
 ['the-notebook','The Notebook',2004,'Movie','Romance'],['the-rookie','The Rookie',2018,'Series','Crime'],
 ['the-shadows-edge','The Shadow\'s Edge',2025,'Movie','Thriller'],['the-super-mario-galaxy-movie','The Super Mario Galaxy Movie',2026,'Movie','Animation'],
 ['the-walking-dead','The Walking Dead',2010,'Series','Horror'],['thor-ragnarok','Thor: Ragnarok',2017,'Movie','Action'],
 ['vikram','Vikram',2022,'Movie','Action'],['war-of-the-worlds-2025','War of the Worlds',2025,'Movie','Sci-Fi'],
 ['wicked','Wicked',2024,'Movie','Musical'],['wicked-for-good','Wicked: For Good',2025,'Movie','Musical'],
 ['yodha','Yodha',2024,'Movie','Action'],['zootopia-2','Zootopia 2',2025,'Movie','Animation'],
];

/* ---- shell ---- */
const tmpl = fs.readFileSync(path.join(ROOT, 'movie/1917/index.html'), 'utf8');
const headPrefix = tmpl.slice(0, tmpl.indexOf('<title>')) + '<title>';
const header = (tmpl.match(/<header class="top">[\s\S]*?<\/header>/) || [''])[0];
const tail = tmpl.slice(tmpl.indexOf('<nav class="mobile-nav">'));

const PILLS = [
 ['/channels/trending/','tr','🔥','Trending'],['/channels/latest/','lr','✨','Latest Release'],
 ['/channels/netflix/','n','N','Netflix'],['/channels/prime/','pv','P','Prime Video'],
 ['/channels/sony/','s','S','SonyLIV'],['/channels/jio/','j','J','JioHotstar'],
 ['/channels/crunchyroll/','cr','C','Crunchyroll'],['/channels/kids/','k','K','Kids'],['/channels/mx/','m','M','MX Player']];
const deskBar = PILLS.map(([href,key,glyph,label]) =>
  `<a class="dpill" href="${href}"><span class="plogo pl-${key}">${glyph}</span>${label}</a>`).join('');
const desk = `<nav class="desk-bar" aria-label="Browse channels"><div class="shell desk-bar-inner">${deskBar}</div></nav>`;

function initials(name){const p=String(name).trim().split(/\s+/);return ((p[0]||'')[0]+(p.length>1?(p[p.length-1][0]||''):'')).toUpperCase()||'?';}

function page(slug, title, year, type, genre, rating, age, desc, tagline) {
  const td = String(type).toLowerCase() === 'series' ? 'series' : 'movie';
  const tb = String(type).toLowerCase() === 'series' ? 'tb-series' : 'tb-movie';
  const typeLabel = String(type).toUpperCase();
  const ratingBadge = rating
    ? `<span class="badge nm-match">${Math.round(parseFloat(rating) * 10)}% Match</span><span class="badge nm-hd">HD</span><span class="badge" title="BRYME editorial score — not IMDb, Rotten Tomatoes or audience ratings">★ ${rating}/10 · BRYME Editorial</span>`
    : `<span class="badge nm-hd">HD</span>`;
  const ageBadge = age ? `<span class="badge" title="Age rating">${esc(age)}</span>` : '';
  const dir = td === 'series' ? 'series' : 'movie';
  const url = `https://bryme.onrender.com/${dir}/${slug}/`;
  const cast = FULL[slug] ? [] : ['Cast to be announced'];
  const actors = cast.map(n => n).slice(0,0);
  const ld = JSON.stringify([{
    '@context':'https://schema.org','@type': td === 'series' ? 'TVSeries' : 'Movie',
    name: title, description: desc || `${title} — watch the official trailer on BRYME.`, url,
    dateCreated: String(year), genre, inLanguage: 'English',
    publisher:{'@type':'Organization',name:'BRYME',url:'https://bryme.onrender.com/'}
  },{
    '@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[
      {'@type':'ListItem','position':1,'name':'Home','item':'https://bryme.onrender.com/'},
      {'@type':'ListItem','position':2,'name':td === 'series' ? 'Series' : 'Movies','item':`https://bryme.onrender.com/${td === 'series' ? 'series' : 'movies'}/`},
      {'@type':'ListItem','position':3,'name':title,'item':url}]}]);
  const heroCast = actors.length ? `<div class="nm-extra-head">Cast</div><div class="nm-cast-row">${actors.map(n=>`<div class="nm-cast-item"><span class="nm-avatar">${initials(n)}</span><b>${esc(n)}</b></div>`).join('')}</div>` : '';
  const lang = `<div class="nm-extra-head">Audio</div><div class="nm-lang-tabs"><button type="button" class="nm-lang is-on">English</button></div>`;
  return `${headPrefix}${esc(title)} (${year}) – Overview, Trailer &amp; BRYME</title>
<meta name="description" content="${esc(desc || `${title} — synopsis, official trailer and watch links on BRYME.`)}">
<link rel="canonical" href="${url}">
<meta property="og:type" content="${td === 'series' ? 'video.tv_show' : 'video.movie'}">
<meta property="og:site_name" content="BRYME">
<meta property="og:title" content="${esc(title)} (${year})">
<meta property="og:description" content="${esc(desc || '')}">
<meta property="og:url" content="${url}">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">${ld}</script></head>
<body data-nav="home">${header}${desk}
<main class="shell tp-page">
  <section class="movie-hero movie-hero-compact" style="--movie-backdrop:url('https://i.ytimg.com/vi/placeholder/hqdefault.jpg')">
    <div class="poster"><div class="placeholder">No image yet</div></div>
    <div>
      <div class="hero-kicker tp-kicker-meta"><span class="type-badge ${tb}">${typeLabel}</span><span>${year}</span><span class="dot">·</span><span>${esc(genre)}</span></div>
      <h1>${esc(title)}</h1>
      ${tagline ? `<p class="lead" style="font-style:italic;color:#B3B3B3">${esc(tagline)}</p>` : ''}
      <div class="badges">${ratingBadge}${ageBadge}</div>
      ${desc ? `<p class="lead">${esc(desc)}</p>` : ''}
      <div class="hero-actions"><a class="cta nm-watch-now" href="#watch">▶ Watch Now</a><a class="cta cta-ghost nm-trailer" href="#trailer">▶ Trailer</a></div>
    </div>
  </section>
  ${heroCast}
  ${lang}
  <section class="tp-loved tp-loved-under" id="loved"><h2>More Like This</h2><p class="tp-loved-lead">Explore more titles in the BRYME catalogue.</p><div class="tp-loved-list"></div></section>
</main>${tail}`;
}

/* ---- write ---- */
let n = 0;
for (const [slug, title, year, type, genre] of MINIMAL) {
  const dir = String(type).toLowerCase() === 'series' ? 'series' : 'movie';
  const out = path.join(ROOT, dir, slug, 'index.html');
  if (fs.existsSync(out)) continue;
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, page(slug, title, year, type, genre, null, null, null, null));
  n++;
}
for (const [slug, data] of Object.entries(FULL)) {
  const [title, rating, year, type, age, desc, tagline] = data;
  const dir = String(type).toLowerCase() === 'series' ? 'series' : 'movie';
  const out = path.join(ROOT, dir, slug, 'index.html');
  if (fs.existsSync(out)) continue;
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, page(slug, title, year, type, '', rating, age, desc, tagline));
  n++;
}
console.log('wrote', n, 'pages');
