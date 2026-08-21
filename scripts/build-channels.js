#!/usr/bin/env node
/* Build /channels/{netflix,prime-video,crunchyroll,kids}/ — NetMirror channel landing pages */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

const esc = s => String(s == null ? '' : s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/movies.json'), 'utf8'));
const items = Array.isArray(data) ? data : (data.movies || data.items || []);
const byType = { movie: [], series: [], anime: [] };
for (const it of items) {
  if (it && it.typeDir && byType[it.typeDir]) byType[it.typeDir].push(it);
}
const sortTiles = list => list
  .filter(x => x && x.status !== 'draft')
  .sort((a, b) => (b.rating && b.rating.value || 0) - (a.rating && a.rating.value || 0) || (b.year || 0) - (a.year || 0));

const KIDS_GENRES = new Set(['animation', 'kids', 'family']);
const kids = sortTiles([...byType.movie, ...byType.series].filter(x => KIDS_GENRES.has(String(x.genre || '').toLowerCase())));

const CHANNELS = [
  {
    slug: 'netflix', name: 'Netflix', tag: 'N', key: 'n',
    glow: 'rgba(229,9,20,.20)', color: '#E50914',
    desc: 'The movies lane. Every BRYME movie links to official, licensed destinations — availability on Netflix varies by region.',
    title: 'Netflix Channel — Movies | BRYME',
    list: sortTiles(byType.movie),
  },
  {
    slug: 'prime-video', name: 'Prime Video', tag: 'pv', key: 'pv',
    glow: 'rgba(0,168,225,.18)', color: '#00A8E1',
    desc: 'The series lane. BRYME\u2019s TV series catalogue links to official, licensed destinations — availability on Prime Video varies by region.',
    title: 'Prime Video Channel — Series | BRYME',
    list: sortTiles(byType.series),
  },
  {
    slug: 'crunchyroll', name: 'Crunchyroll', tag: 'CR', key: 'cr',
    glow: 'rgba(244,117,33,.18)', color: '#F47521',
    desc: 'The anime lane. Every anime on BRYME links to official, licensed destinations — availability on Crunchyroll varies by region.',
    title: 'Crunchyroll Channel — Anime | BRYME',
    list: sortTiles(byType.anime),
  },
  {
    slug: 'kids', name: 'Kids', tag: 'K', key: 'k',
    glow: 'rgba(255,193,7,.16)', color: '#FFC107',
    desc: 'Kids & family picks — animation and family titles across movies and series, all linking to official, licensed destinations.',
    title: 'Kids Channel — Animation & Family | BRYME',
    list: kids,
  },
];

// ---- shell pieces from an existing catalogue page ----
const tmpl = fs.readFileSync(path.join(ROOT, 'movies/index.html'), 'utf8');
const headPrefix = tmpl.slice(0, tmpl.indexOf('<title>')) + '<title>'; // through <title>
const header = (tmpl.match(/<header class="top">[\s\S]*?<\/header>/) || [''])[0];
const tail = tmpl.slice(tmpl.indexOf('<nav class="mobile-nav">')); // mobile-nav + footer + scripts

function deskBar(activeSlug) {
  const pills = [
    ['/trending/', 'tr', '🔥', 'Trending'],
    ['/channels/netflix/', 'n', 'N', 'Netflix'],
    ['/channels/prime-video/', 'pv', 'pv', 'Prime Video'],
    ['/channels/crunchyroll/', 'cr', 'CR', 'Crunchyroll'],
    ['/channels/kids/', 'k', 'K', 'Kids'],
  ];
  const links = pills.map(([href, key, glyph, label]) =>
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
    ? `<p class="tile-rating" title="BRYME editorial score">★ ${it.rating.value}/10</p>` : '';
  return `<a class="tile" href="/${td}/${esc(it.slug)}/"><div class="poster">${poster}<span class="tile-play" aria-hidden="true"></span></div><h3>${esc(it.title)}</h3><div class="tile-meta"><span class="type-badge tb-${td}">${type}</span><span>${esc(it.year || '')}</span><span class="sep">·</span><span>${esc(it.genre || '')}</span></div>${rating}</a>`;
}

for (const ch of CHANNELS) {
  const url = `https://bryme.onrender.com/channels/${ch.slug}/`;
  const desc = ch.desc;
  const tiles = ch.list.map(tile).join('');
  const grid = `<main><div class="shell">
    <section class="ch-hero" style="--ch-glow:${ch.glow}">
      <div class="shell">
        <div class="ch-logo" style="background:${ch.color}">${ch.tag}</div>
        <h1>${ch.name} Channel</h1>
        <p>${esc(desc)}</p>
      </div>
    </section>
    <p class="ch-note">Editorially curated by BRYME. Trailer links lead to YouTube and viewing links lead to third-party official services — always check availability on the destination service.</p>
    <p class="ch-count">${ch.list.length} ${ch.name.toLowerCase() === 'kids' ? 'kids &amp; family titles' : 'titles'} · ranked by BRYME editorial score</p>
    <div class="grid">${tiles}</div>
  </div></main>`;
  const ld = JSON.stringify([{
    '@context': 'https://schema.org', '@type': 'CollectionPage',
    name: `${ch.name} Channel | BRYME`, description: desc, url,
    publisher: { '@type': 'Organization', name: 'BRYME', url: 'https://bryme.onrender.com/' },
  }]);
  const page = `${headPrefix}${esc(ch.title)}</title>
<meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BRYME">
<meta property="og:title" content="${esc(ch.title.replace(' | BRYME', ''))}">
<meta property="og:description" content="${esc(desc)}">
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
