#!/usr/bin/env node
/* BRYME v5 · NetMirror channel pages — exact 9-channel structure
   /channels/{trending,latest,netflix,prime,sony,jio,crunchyroll,kids,mx}/ */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const esc = s => String(s == null ? '' : s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/movies.json'), 'utf8'));
const items = Array.isArray(data) ? data : (data.movies || data.items || []);
const byType = { movie: [], series: [], anime: [] };
for (const it of items) if (it && byType[it.typeDir]) byType[it.typeDir].push(it);

const sortTiles = list => list
  .filter(x => x && x.status !== 'draft')
  .sort((a, b) => (b.rating && b.rating.value || 0) - (a.rating && a.rating.value || 0) || (b.year || 0) - (a.year || 0));

const indian = x => /indian/i.test(String(x.genre || '')) || /india/i.test(String(x.country || ''));
const KIDS = new Set(['animation', 'kids', 'family']);
const SONYLIV = new Set(['drama', 'crime', 'thriller']);

const CHANNELS = [
  {
    slug: 'trending', name: 'Trending', tag: '🔥', key: 'tr', color: 'linear-gradient(135deg,#FF6B00,#FF9500)',
    desc: 'What everyone is watching right now — BRYME\u2019s editorially curated trending titles across movies, series and anime.',
    title: 'Trending — Top Titles Now | BRYME',
    list: sortTiles([...items].filter(x => x.trending || x.isNewRelease || (x.year || 0) >= 2025)).slice(0, 40),
  },
  {
    slug: 'latest', name: 'Latest Release', tag: '✨', key: 'lr', color: 'linear-gradient(135deg,#00C853,#00E676)',
    desc: 'The newest additions to the catalogue — fresh movies, series and anime, ready to explore.',
    title: 'Latest Releases | BRYME',
    list: sortTiles(items.filter(x => x.isNewRelease || (x.year || 0) >= 2025)),
  },
  {
    slug: 'netflix', name: 'Netflix', tag: 'N', key: 'n', color: '#E50914',
    desc: 'The movies lane. Every BRYME movie links to official, licensed destinations — availability on Netflix varies by region.',
    title: 'Netflix Channel — Movies | BRYME',
    list: sortTiles(byType.movie),
  },
  {
    slug: 'prime', name: 'Prime Video', tag: 'P', key: 'pv', color: '#00A8E1',
    desc: 'The series lane. BRYME\u2019s TV series catalogue links to official, licensed destinations — availability on Prime Video varies by region.',
    title: 'Prime Video Channel — Series | BRYME',
    list: sortTiles(byType.series),
  },
  {
    slug: 'sony', name: 'SonyLIV', tag: 'S', key: 's', color: '#1A3C8A',
    desc: 'Drama, crime and thriller — the SonyLIV lane of BRYME\u2019s catalogue, linking to official, licensed destinations.',
    title: 'SonyLIV Channel — Drama, Crime & Thriller | BRYME',
    list: sortTiles(items.filter(x => SONYLIV.has(String(x.genre || '').toLowerCase()))),
  },
  {
    slug: 'jio', name: 'JioHotstar', tag: 'J', key: 'j', color: 'linear-gradient(135deg,#6A1B9A,#9C27B0)',
    desc: 'Indian cinema and series — the JioHotstar lane of BRYME, linking to official, licensed destinations.',
    title: 'JioHotstar Channel — Indian Cinema & Series | BRYME',
    list: sortTiles(items.filter(indian)),
  },
  {
    slug: 'crunchyroll', name: 'Crunchyroll', tag: 'C', key: 'cr', color: '#F47521',
    desc: 'The anime lane. Every anime on BRYME links to official, licensed destinations — availability on Crunchyroll varies by region.',
    title: 'Crunchyroll Channel — Anime | BRYME',
    list: sortTiles(byType.anime),
  },
  {
    slug: 'kids', name: 'Kids', tag: 'K', key: 'k', color: '#E91E63',
    desc: 'Kids & family picks — animation and family titles across movies and series, all linking to official, licensed destinations.',
    title: 'Kids Channel — Animation & Family | BRYME',
    list: sortTiles([...byType.movie, ...byType.series].filter(x => KIDS.has(String(x.genre || '').toLowerCase()))),
  },
  {
    slug: 'mx', name: 'MX Player', tag: 'M', key: 'm', color: '#1E88E5',
    desc: 'Indian movies — the MX Player lane of BRYME, linking to official, licensed destinations.',
    title: 'MX Player Channel — Indian Movies | BRYME',
    list: sortTiles(byType.movie.filter(indian)),
  },
];

const tmpl = fs.readFileSync(path.join(ROOT, 'movies/index.html'), 'utf8');
const headPrefix = tmpl.slice(0, tmpl.indexOf('<title>')) + '<title>';
const header = (tmpl.match(/<header class="top">[\s\S]*?<\/header>/) || [''])[0];
const tail = tmpl.slice(tmpl.indexOf('<nav class="mobile-nav">'));

const PILLS = [
  ['/channels/trending/', 'tr', '🔥', 'Trending'],
  ['/channels/latest/', 'lr', '✨', 'Latest Release'],
  ['/channels/netflix/', 'n', 'N', 'Netflix'],
  ['/channels/prime/', 'pv', 'P', 'Prime Video'],
  ['/channels/sony/', 's', 'S', 'SonyLIV'],
  ['/channels/jio/', 'j', 'J', 'JioHotstar'],
  ['/channels/crunchyroll/', 'cr', 'C', 'Crunchyroll'],
  ['/channels/kids/', 'k', 'K', 'Kids'],
  ['/channels/mx/', 'm', 'M', 'MX Player'],
];
function deskBar(activeSlug) {
  const links = PILLS.map(([href, key, glyph, label]) =>
    `<a class="dpill${href === '/channels/' + activeSlug + '/' ? ' is-on' : ''}" href="${href}"><span class="plogo pl-${key}">${glyph}</span>${label}</a>`).join('');
  return `<nav class="desk-bar" aria-label="Browse channels"><div class="shell desk-bar-inner">${links}</div></nav>`;
}

function tile(it) {
  const td = it.typeDir;
  const type = td === 'movie' ? 'MOVIE' : td === 'series' ? 'SERIES' : 'ANIME';
  const poster = it.poster
    ? `<img loading="lazy" decoding="async" width="320" height="180" src="${esc(it.poster)}" alt="${esc(it.title)} thumbnail">`
    : `<div class="placeholder">No image</div>`;
  const rating = it.rating && it.rating.value
    ? `<p class="tile-rating" title="BRYME editorial score">${it.rating.value}/10</p>` : '';
  return `<a class="tile" href="/${td}/${esc(it.slug)}/"><div class="poster">${poster}<span class="tile-play" aria-hidden="true"></span></div><h3>${esc(it.title)}</h3><div class="tile-meta"><span class="type-badge tb-${td}">${type}</span><span>${esc(it.year || '')}</span><span class="sep">·</span><span>${esc(it.genre || '')}</span></div>${rating}</a>`;
}

for (const ch of CHANNELS) {
  const url = `https://bryme.onrender.com/channels/${ch.slug}/`;
  const tiles = ch.list.map(tile).join('');
  const grid = `<main><div class="shell">
    <section class="ch-hero" style="--ch-glow:${ch.color}">
      <div class="shell">
        <div class="ch-logo" style="background:${ch.color}">${ch.tag}</div>
        <h1>${ch.name} Channel</h1>
        <p>${esc(ch.desc)}</p>
      </div>
    </section>
    <p class="ch-note">Editorially curated by BRYME. Trailer links lead to YouTube and viewing links lead to third-party official services — always check availability on the destination service.</p>
    <p class="ch-count">${ch.list.length} titles · ranked by BRYME editorial score</p>
    <div class="grid">${tiles || '<p class="ch-count">No titles yet — the catalogue is growing.</p>'}</div>
  </div></main>`;
  const ld = JSON.stringify([{
    '@context': 'https://schema.org', '@type': 'CollectionPage',
    name: `${ch.name} Channel | BRYME`, description: ch.desc, url,
    publisher: { '@type': 'Organization', name: 'BRYME', url: 'https://bryme.onrender.com/' },
  }]);
  const page = `${headPrefix}${esc(ch.title)}</title>
<meta name="description" content="${esc(ch.desc)}">
<link rel="canonical" href="${url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BRYME">
<meta property="og:title" content="${esc(ch.name)} Channel">
<meta property="og:description" content="${esc(ch.desc)}">
<meta property="og:url" content="${url}">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">${ld}</script></head>
<body data-nav="home">${header}${deskBar(ch.slug)}${grid}${tail}`;
  const out = path.join(ROOT, 'channels', ch.slug, 'index.html');
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, page);
  console.log('wrote', ch.slug, '(' + ch.list.length + ' tiles)');
}
console.log('done');
