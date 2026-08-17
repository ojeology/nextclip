#!/usr/bin/env node
/* Build indexable static movie, series, anime, genre, year and article pages.
   The legacy hash app (legacy/index.html) remains untouched.
   Frontend architecture: types are separated (/movies, /series, /anime),
   trending is a transparent editorial+algorithmic score, genres are per-type. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'legacy', 'index.html'), 'utf8');
const script = html.match(/<script>\n([\s\S]*)<\/script>\s*<\/body>/)[1];
const dataSource = script.slice(0, script.indexOf('/* ============ HELPERS'));
const ctx = {};
vm.createContext(ctx);
vm.runInContext(dataSource, ctx, { timeout: 1000 });

const config = JSON.parse(fs.readFileSync(path.join(root, 'site.config.json'), 'utf8'));
const site = { name: config.siteName, url: String(config.siteUrl).replace(/\/$/, ''), description: config.siteDescription };
if (!/^https:\/\/[^\s]+$/i.test(site.url)) throw new Error('site.config.json requires an absolute https siteUrl.');
const CURRENT_YEAR = new Date().getFullYear();
const clean = v => String(v || '').replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();
const slugify = v => clean(v).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const esc = v => String(v ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
/* Internal links are root-relative so the site works from any host (Render today,
   a custom domain later). absUrl() builds absolute production URLs where the web
   requires them (canonical, og:url, sitemap, robots, structured data). */
const url = p => {
  const q = String(p || '/');
  return q.charAt(0) === '/' ? q : '/' + q;
};
const absUrl = p => site.url + url(p);
const breadcrumbs = items => ({ '@context':'https://schema.org', '@type':'BreadcrumbList', itemListElement:items.map((item, index) => ({ '@type':'ListItem', position:index+1, name:item.name, item:absUrl(item.path) })) });
const normalizeYouTube = value => {
  const raw = String(value || '').trim();
  if (!raw) return null;
  if (/^[A-Za-z0-9_-]{11}$/.test(raw)) return raw;
  try {
    const parsed = new URL(raw);
    const host = parsed.hostname.replace(/^www\./, '');
    if (host === 'youtu.be') return /^[A-Za-z0-9_-]{11}$/.test(parsed.pathname.slice(1)) ? parsed.pathname.slice(1) : null;
    if (host.endsWith('youtube.com')) {
      const candidate = parsed.searchParams.get('v') || parsed.pathname.match(/\/(?:embed|shorts)\/([A-Za-z0-9_-]{11})/)?.[1];
      return candidate && /^[A-Za-z0-9_-]{11}$/.test(candidate) ? candidate : null;
    }
  } catch (e) {}
  return null;
};
const poster = m => m.poster || (m.youtubeId ? `https://i.ytimg.com/vi/${m.youtubeId}/hqdefault.jpg` : '');

const warnings = [];
const existing = new Set();
const movies = [...ctx.LIB, ...ctx.ANIME].map((raw, i) => {
  let slug = slugify(raw.title); if (existing.has(slug)) slug += '-' + raw.year; existing.add(slug);
  const isRich = raw.about || raw.teaser;
  const youtubeId = normalizeYouTube(raw.ytId);
  return {
    id: raw.id, title: clean(raw.title), slug, description: clean(raw.about || raw.teaser || ''), year: Number(raw.year) || null,
    genre: clean(raw.genre), country: null, language: null,
    poster: youtubeId ? `https://i.ytimg.com/vi/${youtubeId}/hqdefault.jpg` : null,
    backdrop: null,
    trailer: youtubeId ? `https://www.youtube.com/watch?v=${youtubeId}` : null, youtubeId,
    cast: [], legacyCastNotes: Array.isArray(ctx.CAST?.[raw.id]) ? ctx.CAST[raw.id].map(clean) : [], director: null, runtime: null,
    rating: raw.score == null ? null : { value: raw.score, source: 'BRYME editorial score' },
    status: 'published', createdAt: null, updatedAt: null, legacyType: raw.genre === 'Anime' ? 'legacy-anime' : (raw.genre === 'Series' ? 'legacy-series' : 'movie'), typeDir: raw.genre === 'Anime' ? 'anime' : (raw.genre === 'Series' ? 'series' : 'movie'),
    teaser: clean(raw.teaser || ''), facts: Array.isArray(raw.facts) ? raw.facts.map(clean) : [],
    watchLinks: Array.isArray(raw.links) ? raw.links.map(x => ({ name: clean(x.name), url: x.url })) : []
  };
});
const cataloguePath = path.join(root, 'content', 'catalogue.json');
if (fs.existsSync(cataloguePath)) {
  const additional = JSON.parse(fs.readFileSync(cataloguePath, 'utf8'));
  const ids = new Set(movies.map(m => m.id)), slugs = new Set(movies.map(m => m.slug));
  additional.forEach(record => {
    if (!record || record.status !== 'published') return;
    if (!record.id || !record.title || !record.slug || !record.description || !record.year || !record.genre) throw new Error(`Invalid catalogue record: ${record && record.id || 'unknown'}`);
    if (ids.has(record.id) || slugs.has(record.slug)) throw new Error(`Duplicate catalogue record: ${record.id}`);
    const youtubeId = normalizeYouTube(record.youtubeId || record.trailer);
    movies.push({ id:record.id, title:clean(record.title), slug:slugify(record.slug), description:clean(record.description), year:Number(record.year), genre:clean(record.genre), country:record.country||null, language:record.language||null, poster:record.poster||null, backdrop:record.backdrop||null, trailer:youtubeId?`https://www.youtube.com/watch?v=${youtubeId}`:null, youtubeId, cast:Array.isArray(record.cast)?record.cast:[], director:record.director||null, runtime:record.runtime||null, rating:record.rating||null, status:'published', createdAt:record.createdAt||null, updatedAt:record.updatedAt||null, legacyType: record.genre === 'Anime' ? 'legacy-anime' : (record.genre === 'Series' ? 'legacy-series' : 'movie'), typeDir: record.genre === 'Anime' ? 'anime' : (record.genre === 'Series' ? 'series' : 'movie'), teaser:clean(record.description), facts:[], watchLinks:[] });
    ids.add(record.id); slugs.add(record.slug);
  });
}

/* ------------------------------------------------------------------ */
/* Verified title metadata overlay (content/title-metadata.json)      */
/* ------------------------------------------------------------------ */
/* Director, cast, runtime, country and language sourced from Wikidata
   (CC0 structured data) by scripts/enrich-wikidata.py. The overlay only
   FILLS BLANKS — any value already present in the catalogue or in the
   legacy data wins, so editorial corrections are never overwritten.
   Each enriched record keeps the Wikidata id and Wikipedia link so the
   title page can say where the facts came from. */
const titleMetaPath = path.join(root, 'content', 'title-metadata.json');
let titleMeta = {};
if (fs.existsSync(titleMetaPath)) titleMeta = JSON.parse(fs.readFileSync(titleMetaPath, 'utf8'));
let enrichedCount = 0;
movies.forEach(m => {
  const meta = titleMeta[m.id];
  if (!meta) return;
  let used = false;
  if (!m.director && meta.director) { m.director = clean(meta.director); used = true; }
  if ((!m.cast || !m.cast.length) && Array.isArray(meta.cast) && meta.cast.length) { m.cast = meta.cast.map(clean); used = true; }
  if (!m.runtime && meta.runtime) { m.runtime = clean(meta.runtime); used = true; }
  if (!m.country && meta.country) { m.country = clean(meta.country); used = true; }
  if (!m.language && meta.language) { m.language = clean(meta.language); used = true; }
  if (used && meta.source) { m.metaSource = meta.source; enrichedCount++; }
  if (m.cast && m.cast.length && meta.castSource) m.castSource = meta.castSource;
});

/* ------------------------------------------------------------------ */
/* Frontend enrichment (does NOT touch content/catalogue.json)        */
/* ------------------------------------------------------------------ */
const typeGenresPath = path.join(root, 'content', 'type-genres.json');
let typeGenres = {};
if (fs.existsSync(typeGenresPath)) typeGenres = JSON.parse(fs.readFileSync(typeGenresPath, 'utf8'));
/* ================================================================
   RANKINGS — three independent, editorially controlled concepts:
     🔥 TRENDING NOW  (content/rankings.json -> trending, per type)
     ⭐ POPULAR       (content/rankings.json -> popular, per type)
     👑 EDITOR'S PICKS (content/rankings.json -> editorPicks)
   Trending is NOT derived from scores/ratings/recency. Real traffic
   analytics can replace it later without changing this file's shape.
   ================================================================ */
const rankingsPath = path.join(root, 'content', 'rankings.json');
let rankings = {};
if (fs.existsSync(rankingsPath)) { try { rankings = JSON.parse(fs.readFileSync(rankingsPath, 'utf8')); } catch (e) { warnings.push('rankings.json unreadable'); } }
const slugIndex = new Map(movies.map(m => [m.slug, m]));
const TODAY = new Date().toISOString().slice(0, 10); // YYYY-MM-DD for trendingUntil expiry

const RANK_FIELDS = { trending: 'trendingRank', popular: 'popularRank', editorPicks: 'editorPickRank' };
function resolveRankList(entries, kind, typeDir) {
  const out = [];
  (entries || []).forEach(e => {
    if (!e || !e.slug) { warnings.push(`rankings.json: ${kind} entry missing slug`); return; }
    const rec = slugIndex.get(e.slug);
    if (!rec) { warnings.push(`rankings.json: ${kind} unknown slug "${e.slug}"`); return; }
    if (typeDir && rec.typeDir !== typeDir) warnings.push(`rankings.json: ${kind} type mismatch for "${e.slug}" (expected ${typeDir}, record is ${rec.typeDir})`);
    if (e.title && clean(e.title).toLowerCase() !== rec.title.toLowerCase()) warnings.push(`rankings.json: ${kind} title mismatch for "${e.slug}" (config says "${e.title}", catalogue says "${rec.title}")`);
    if (e.until && String(e.until) < TODAY) { warnings.push(`rankings.json: ${kind} "${e.slug}" expired (until ${e.until}) — excluded`); return; }
    const rankField = RANK_FIELDS[kind] || 'rank';
    out.push({ slug: e.slug, rank: Number(e[rankField] ?? e.rank) || out.length + 1, until: e.until || null, note: e.note || null });
  });
  out.sort((a, b) => a.rank - b.rank);
  return out;
}
const heroCfg = (rankings.hero && slugIndex.has(rankings.hero.slug)) ? rankings.hero : null;
const trendingCfg = { movie: resolveRankList(rankings.trending && rankings.trending.movie, 'trending', 'movie'), series: resolveRankList(rankings.trending && rankings.trending.series, 'trending', 'series'), anime: resolveRankList(rankings.trending && rankings.trending.anime, 'trending', 'anime') };
const popularCfg = { movie: resolveRankList(rankings.popular && rankings.popular.movie, 'popular', 'movie'), series: resolveRankList(rankings.popular && rankings.popular.series, 'popular', 'series'), anime: resolveRankList(rankings.popular && rankings.popular.anime, 'popular', 'anime') };
const editorCfg = resolveRankList(rankings.editorPicks, 'editorPicks', null);
const animeFilms = new Set((typeGenres.anime || {}).films || []);

const typeLabelOf = d => d === 'series' ? 'TV Series' : (d === 'anime' ? 'Anime' : 'Movie');
movies.forEach(m => {
  const tgs = (typeGenres[m.typeDir] || {})[m.slug];
  if (tgs && (!Array.isArray(tgs) || tgs.length === 0)) warnings.push(`type-genres.json: empty genres for ${m.slug}`);
  m.genres = Array.isArray(tgs) ? tgs.slice(0, 3) : [];
  m.typeLabel = typeLabelOf(m.typeDir);
  // Structured ranking fields (all editorial, deterministic)
  const tr = trendingCfg[m.typeDir].find(x => x.slug === m.slug);
  m.trending = !!tr;
  m.trendingRank = tr ? tr.rank : null;
  m.trendingUntil = tr ? tr.until : null;
  const pr = popularCfg[m.typeDir].find(x => x.slug === m.slug);
  m.popular = !!pr;
  m.popularRank = pr ? pr.rank : null;
  m.popularityScore = pr ? Math.max(1, 101 - pr.rank) : null;
  const ep = editorCfg.find(x => x.slug === m.slug);
  m.editorPick = !!ep;
  m.editorPickRank = ep ? ep.rank : null;
  m.editorPickNote = ep ? ep.note : null;
  m.isFeatured = !!(heroCfg && heroCfg.slug === m.slug);
  m.isNewRelease = !!m.year && m.year >= CURRENT_YEAR - 2;
});
if (heroCfg && !slugIndex.has(heroCfg.slug)) warnings.push('rankings.json: hero slug not found');

/* ------------------------------------------------------------------ */
/* Trailer system: multi-candidate verified trailers                   */
/* Priority: official-trailer > official-teaser > official-clip > fan-made > unavailable */
/* ------------------------------------------------------------------ */
// Raw IDs from catalogue.json + legacy (source of truth), written BEFORE any
// audit filtering so the audit can always re-verify every known video ID.
fs.mkdirSync(path.join(root, 'data'), {recursive:true});
fs.writeFileSync(path.join(root, 'data', 'trailer-sources.json'), JSON.stringify(movies.map(m => ({ slug: m.slug, title: m.title, youtubeIds: [m.youtubeId].filter(Boolean) })), null, 1) + '\n');
const TRAILER_PRIORITY = { 'official-trailer': 0, 'official-teaser': 1, 'official-clip': 2, 'fan-made': 3 };
const TRAILER_LABELS = {
  'official-trailer': 'Official Trailer',
  'official-teaser': 'Official Teaser',
  'official-clip': 'Official Clip',
  'fan-made': 'Community trailer'
};
const TRAILER_PATHS = {
  'official-trailer': '/movies/',
  'official-teaser': '/movies/',
  'official-clip': '/movies/',
  'fan-made': '/movies/'
};
let trailerAudit = {}, trailerOverrides = {};
const trailerAuditPath = path.join(root, 'content', 'trailer-audit.json');
if (fs.existsSync(trailerAuditPath)) { try { trailerAudit = JSON.parse(fs.readFileSync(trailerAuditPath, 'utf8')); } catch (e) { warnings.push('trailer-audit.json unreadable'); } }
const trailerOverridesPath = path.join(root, 'content', 'trailers.json');
if (fs.existsSync(trailerOverridesPath)) { try { trailerOverrides = JSON.parse(fs.readFileSync(trailerOverridesPath, 'utf8')); } catch (e) { warnings.push('trailers.json unreadable'); } }
const trailerStats = { official: 0, teaser: 0, clip: 0, fan: 0, missing: 0, broken: 0, brokenList: [] };
movies.forEach(m => {
  const auditRec = trailerAudit[m.slug] || {};
  const override = trailerOverrides[m.slug];
  const candidates = [];
  if (!(override && override.excludeTrailers)) {
    if (override && Array.isArray(override.candidates) && override.candidates.length) {
      override.candidates.forEach(c => {
        if (!c || !/^[A-Za-z0-9_-]{11}$/.test(c.videoId || '')) { warnings.push(`trailers.json: invalid videoId for ${m.slug}`); return; }
        candidates.push({ videoId: c.videoId, type: c.type || 'official-trailer', title: c.title || TRAILER_LABELS[c.type] || 'Trailer', source: c.source || 'YouTube', channel: c.channel || '', verified: !!c.verified, status: c.verified ? 'verified' : 'manual', lastChecked: c.lastChecked || null });
      });
    } else if (auditRec.videoId || (Array.isArray(auditRec.candidates) && auditRec.candidates.length)) {
      const srcList = (Array.isArray(auditRec.candidates) && auditRec.candidates.length) ? auditRec.candidates : [auditRec];
      srcList.forEach(ar => {
        if (!ar || !ar.videoId) return;
        const playable = ar.status === 'verified' || ar.status === 'community';
        candidates.push({
          videoId: ar.videoId,
          type: ar.status === 'community' ? 'fan-made' : (ar.type || 'official-trailer'),
          title: ar.status === 'community' ? 'Community trailer' : (TRAILER_LABELS[ar.type] || 'Trailer'),
          source: 'YouTube',
          channel: ar.channel || '',
          channelClass: ar.channelClass || null,
          verified: playable && ar.status !== 'community' ? true : (ar.status === 'community' ? false : false),
          status: ar.status || 'broken',
          videoTitle: ar.videoTitle || null,
          lastChecked: ar.lastChecked || null
        });
        if (!playable) {
          trailerStats.broken++;
          trailerStats.brokenList.push({ slug: m.slug, title: m.title, videoId: ar.videoId, status: ar.status, channel: ar.channel, videoTitle: ar.videoTitle, lastChecked: ar.lastChecked });
        }
      });
    }
  }
  candidates.sort((a, b) => (TRAILER_PRIORITY[a.type] ?? 9) - (TRAILER_PRIORITY[b.type] ?? 9));
  m.trailers = candidates;
  const playable = candidates.filter(c => c.verified || c.status === 'community' || c.status === 'manual');
  const primary = playable[0] || null;
  m.youtubeId = primary ? primary.videoId : null;
  m.trailer = primary ? `https://www.youtube.com/watch?v=${primary.videoId}` : null;
  m.poster = primary ? `https://i.ytimg.com/vi/${primary.videoId}/hqdefault.jpg` : null;
  m.trailerType = primary ? primary.type : null;
  m.trailerLabel = primary ? TRAILER_LABELS[primary.type] || primary.title : null;
  m.trailerChannel = primary ? primary.channel || '' : '';
  m.trailerVerified = primary ? !!primary.verified : false;
  m.trailerLastChecked = primary ? primary.lastChecked || null : null;
  if (!m.youtubeId) trailerStats.missing++;
  else if (m.trailerType === 'official-trailer') trailerStats.official++;
  else if (m.trailerType === 'official-teaser') trailerStats.teaser++;
  else if (m.trailerType === 'official-clip') trailerStats.clip++;
  else trailerStats.fan++;
});
const trailerAdminRows = movies.map(m => {
  let status = m.youtubeId ? (m.trailerType === 'fan-made' ? 'fan-made' : 'official') : 'none';
  if (!status || status === 'none') {
    const bad = (m.trailers || []).filter(t => !t.verified && t.status && t.status !== 'manual');
    if (bad.length) status = 'broken';
  }
  return {
    slug: m.slug, title: m.title, typeDir: m.typeDir,
    status,
    trailerType: m.trailerType || null,
    label: m.trailerLabel || null,
    videoId: m.youtubeId || null,
    channel: m.trailerChannel || null,
    verified: m.trailerVerified,
    lastChecked: m.trailerLastChecked || null,
    candidates: (m.trailers || []).map(t => ({ id: t.videoId, type: t.type, channel: t.channel || '', verified: !!t.verified, status: t.status || null }))
  };
});
const bySlug = slug => slugIndex.get(slug) || null;
const resolveList = cfg => cfg.map(x => bySlug(x.slug)).filter(Boolean);
const hero = heroCfg ? bySlug(heroCfg.slug) : movies.filter(m => m.typeDir === 'movie').sort((a,b) => (b.rating?.value||0) - (a.rating?.value||0))[0];

/* ================================================================
   HOMEPAGE HERO CAROUSEL + RECOMMENDATION ENGINE (client-side data)
   Hero slides are configured in content/homepage.json (slugs only —
   catalogue data is reused). Rec data is embedded for a no-backend
   similarity engine; the engine can be swapped for a real AI service
   later without changing the page structure.
   ================================================================ */
const homepageCfgPath = path.join(root, 'content', 'homepage.json');
let homepageCfg = {};
if (fs.existsSync(homepageCfgPath)) { try { homepageCfg = JSON.parse(fs.readFileSync(homepageCfgPath, 'utf8')); } catch (e) { warnings.push('homepage.json unreadable'); } }
const heroSlides = (homepageCfg.hero || []).map(item => {
  const rec = slugIndex.get(item.slug);
  if (!rec) { warnings.push(`homepage.json: unknown hero slug "${item.slug}" — excluded`); return null; }
  if (!rec.youtubeId || !rec.poster) { warnings.push(`homepage.json: hero "${item.slug}" has no verified trailer/poster — excluded`); return null; }
  return {
    slug: rec.slug, title: rec.title, typeDir: rec.typeDir, typeLabel: rec.typeLabel,
    year: rec.year, genres: rec.typeDir === 'movie' ? [rec.genre] : rec.genres,
    genreLabel: rec.typeDir === 'movie' ? rec.genre : ((rec.genres || [])[0] || rec.genre),
    poster: rec.poster, youtubeId: rec.youtubeId, trailer: rec.trailer,
    rating: (rec.rating && rec.rating.value != null) ? rec.rating.value : null,
    description: rec.description || rec.teaser || '', tagline: item.tagline || null,
    url: url('/' + rec.typeDir + '/' + rec.slug + '/')
  };
}).filter(Boolean).slice(0, 6);
if (!heroSlides.length) warnings.push('homepage.json: no valid hero slides configured — hero falls back to the rankings hero.');
const heroSlide = heroSlides[0] || hero;

// --- recommendation engine embedded data ---
const STOPWORDS = new Set(('the a an and or but of to in on for with from by is are was were his her their its it he she they you your we our as at be been being has have had not no so if than then that this these those when who which into after before about against between over under again once only own same such very just but what all can will would could should may might must do does did done get gets got go goes one two new now also much many more most some any other another each few both first last long great good big small high low old young man men woman women people world life time way thing things story stories series movie movies anime film films show shows watch watching watchlist making made make like likes love loves become becomes became find finds found take takes took keep keeps kept comes come came know knows known see sees saw say says said think thinks thought want wants need needs help helps start starts started end ends ended turn turns turned fight fights fought follow follows followed face faces faced bring brings brought leave leaves left return returns returned reveal reveals revealed discover discovers discovered experience experiences feel feels felt grow grows grew growing powerful power powers dead death deaths die dies died kill kills killed survive survives survived survival escape escapes escaped freedom dark darkest magic worlds years year episode episodes season seasons part parts final real really actually entire everything something nothing anything everyone someone nobody somebody ever never always still even though without within along around away back behind below beside beyond down during inside near off onto outside past since through throughout toward towards underneath until up upon via with according across almost amid among apart appear appears appeared approximately around asked asking became began begin begins begun being believe believes best better between both brief briefly came cannot cause causes certain certainly clearly could differ different differently doing done dont down downwards during each either else elsewhere enough etc every everybody everywhere except few for former formerly from further gave give given gives going got had happen happens hardly here how however immediately important in indeed instead into itself just least less lest let lets likely little look looked looking looks mainly many maybe meantime meanwhile might mine more moreover most mostly much must namely neither never nevertheless none nor normally not nothing nowhere obviously often oh ok okay old once ones only onto or other others otherwise ought our out over overall own per perhaps please plus possible presumably probably quite rather regardless relatively right said same saw saying says seem seemed seeming seems seen shall shortly showed shown shows significant significantly similar similarly since slightly so somebody somehow someone something sometimes somewhat somewhere soon specifically still stopped such suddenly suppose supposed than thee their theirs them themselves then thence there thereafter thereby therefore therein thereupon these they thick thin third this those though three through thru thus to together too took toward towards tried tries truly try trying twice under underneath unfortunately unless unlike unlikely until unto up upon us use used useful uses using usually various very via viz was way we well went were what whatever when whence whenever where whereafter whereas whereby wherein whereupon wherever whether which while whither who whoever whole whom whomever whose why will willing wish within without wonder would yet yours yourself yourselves').split(' '));
function descKeywords(text){
  if (!text) return [];
  const counts = {};
  String(text).toLowerCase().replace(/[^a-z0-9\s-]/g, ' ').split(/\s+/).forEach(w => {
    if (w.length >= 4 && !STOPWORDS.has(w)) counts[w] = (counts[w] || 0) + 1;
  });
  return Object.keys(counts).sort((a, b) => counts[b] - counts[a]).slice(0, 8);
}
const recItems = movies.filter(m => m.status === 'published').map(m => ({
  s: m.slug, t: m.title, y: m.year || null, ty: m.typeDir,
  g: m.typeDir === 'movie' ? [m.genre] : m.genres,
  p: m.poster,
  r: (m.rating && m.rating.value != null) ? m.rating.value : null,
  k: descKeywords(m.description || m.teaser).slice(0, 6)
}));
const homeRelationsPath = path.join(root, 'content', 'title-relationships.json');
let homeRelations = {};
if (fs.existsSync(homeRelationsPath)) { try { homeRelations = JSON.parse(fs.readFileSync(homeRelationsPath, 'utf8')); } catch (e) {} }
if (homeRelations._comment) delete homeRelations._comment;
const homePopular = ['movie', 'series', 'anime'].flatMap(td => (popularCfg[td] || []).map(x => x.slug)).slice(0, 9);
const recEmbed = JSON.stringify({ items: recItems, relations: homeRelations, popular: homePopular }).replace(/</g, '\\u003c');
fs.writeFileSync(path.join(root, 'data', 'rec-data.json'), JSON.stringify({ items: recItems, relations: homeRelations, popular: homePopular }));
// Trending: ONLY editorially flagged titles, ordered by trendingRank ASC.
// No scores, no recency, no random selection. Deterministic.
const trendingByType = {
  movie: resolveList(trendingCfg.movie),
  series: resolveList(trendingCfg.series),
  anime: resolveList(trendingCfg.anime)
};
const trendingList = [...trendingByType.movie, ...trendingByType.series, ...trendingByType.anime];
const popularByType = {
  movie: resolveList(popularCfg.movie),
  series: resolveList(popularCfg.series),
  anime: resolveList(popularCfg.anime)
};
const popularList = [...popularByType.movie, ...popularByType.series, ...popularByType.anime];
const editorPicksList = resolveList(editorCfg);
const newReleases = [...movies].sort((a,b) => ((b.year||0) - (a.year||0)) || a.title.localeCompare(b.title)).filter(m => m.isNewRelease);
const classics = movies.filter(m => m.year && m.year <= 2000).sort((a,b) => ((b.rating?.value||0) - (a.rating?.value||0)) || ((b.year||0) - (a.year||0)));
// Browse rows on the homepage: plain editorial-score ordering, NOT labelled
// as Trending/Popular — just a convenient way to keep exploring.
const sortPopular = (a,b) => ((b.rating?.value||0) - (a.rating?.value||0)) || ((b.year||0) - (a.year||0)) || a.title.localeCompare(b.title);
const sortNewest = (a,b) => ((b.year||0) - (a.year||0)) || a.title.localeCompare(b.title);
const sortAZ = (a,b) => a.title.localeCompare(b.title);

/* ------------------------------------------------------------------ */
/* Data outputs                                                       */
/* ------------------------------------------------------------------ */
fs.mkdirSync(path.join(root, 'data'), {recursive:true});
fs.mkdirSync(path.join(root, 'reports'), {recursive:true});
fs.writeFileSync(path.join(root, 'data/movies.json'), JSON.stringify(movies, null, 2)+'\n');
const youtubeAudit = movies.map(m => ({ id:m.id, title:m.title, youtubeId:m.youtubeId, status:m.youtubeId ? 'valid-id' : 'unavailable', watchUrl:m.trailer })).sort((a,b)=>a.status.localeCompare(b.status));
fs.writeFileSync(path.join(root, 'reports/youtube-audit.json'), JSON.stringify({ generatedAt:new Date().toISOString(), total:youtubeAudit.length, valid:youtubeAudit.filter(v=>v.status==='valid-id').length, unavailable:youtubeAudit.filter(v=>v.status==='unavailable').length, records:youtubeAudit }, null, 2)+'\n');
const trailerReport = {
  generatedAt: new Date().toISOString(),
  totalTitles: movies.length,
  officialTrailers: trailerStats.official,
  officialTeasers: trailerStats.teaser,
  officialClips: trailerStats.clip,
  fanMade: trailerStats.fan,
  titlesWithVerifiedTrailer: trailerStats.official + trailerStats.teaser + trailerStats.clip + trailerStats.fan,
  noCandidateAtAll: movies.filter(m => !(m.trailers || []).length).length,
  noVerifiedTrailer: trailerStats.missing,
  brokenUnavailable: trailerStats.broken,
  brokenList: trailerStats.brokenList,
  note: 'Counts reflect the primary (highest-priority) trailer per title. Fan-made videos are only used as a fallback and are labelled as community-created on the site. noVerifiedTrailer includes titles with broken/wrong candidates.'
};
fs.writeFileSync(path.join(root, 'reports', 'trailer-report.json'), JSON.stringify(trailerReport, null, 2) + '\n');
fs.writeFileSync(path.join(root, 'data', 'trailer-report.json'), JSON.stringify(trailerReport, null, 2) + '\n');
fs.writeFileSync(path.join(root, 'data', 'trailers.json'), JSON.stringify(trailerAdminRows, null, 2) + '\n');
fs.writeFileSync(path.join(root, 'data', 'trending.json'), JSON.stringify({ generatedAt:new Date().toISOString(), mode:'editorial-curation', note:'Trending Now is editorially curated (content/rankings.json). No live traffic data is claimed. When real analytics exist, Trending Score = recent engagement + growth rate + searches + clicks + recency can replace this list without changing the site architecture.', futureSignals:['pageViews','searches','cardClicks','trailerClicks','watchInteractions','favorites','shares','recentGrowth'], records:trendingList.map(m => ({ slug:m.slug, title:m.title, typeDir:m.typeDir, year:m.year, trendingRank:m.trendingRank, trendingUntil:m.trendingUntil })) }, null, 2)+'\n');

const legacyArticleCategories = { 'broke-internet':'Movie Facts', 'never-end':'Movie Recommendations', 'agent-kim':'Movie Explainers', 'korean-movies':'Movie Recommendations', 'vampire-horror':'Movie Facts' };
let articles = (ctx.ARTICLES || []).map(a => ({ id:a.id, slug:slugify(a.title), title:clean(a.title), description:clean(a.intro), category:legacyArticleCategories[a.id] || 'Editorial', tags:(a.tags||[]).map(clean), emoji:a.emoji || '', items:(a.items||[]).map(x=>({heading:clean(x.h), body:clean(x.p)})), relatedMovieSlugs:[], status:'archived', updatedAt:null, createdAt:null }));
const authoredEditorialPath = path.join(root, 'content', 'editorial.json');
if (fs.existsSync(authoredEditorialPath)) {
  const authoredEditorial = JSON.parse(fs.readFileSync(authoredEditorialPath, 'utf8'));
  authoredEditorial.forEach(a => articles.push({ id:a.id, slug:a.slug, title:clean(a.title), description:clean(a.excerpt), category:clean(a.category), tags:(a.tags||[]).map(clean), emoji:'', items:(a.content||[]).map(x=>({heading:clean(x.heading), body:clean(x.body)})), blocks:(a.blocks||[]).map(x=>({type:x.type||'paragraph', text:String(x.text||'')})), relatedMovieSlugs:a.relatedMovieSlugs||[], status:a.status||'draft', author:a.author||null, createdAt:a.publishedAt||null, updatedAt:a.updatedAt||null }));
}
articles = articles.filter(a => a.status === 'published');
fs.writeFileSync(path.join(root, 'data/articles.json'), JSON.stringify(articles, null, 2)+'\n');
const topicSourcePath = path.join(root, 'content', 'topics.json');
const topics = fs.existsSync(topicSourcePath) ? JSON.parse(fs.readFileSync(topicSourcePath, 'utf8')).filter(t => t.status === 'published') : [];
fs.writeFileSync(path.join(root, 'data/topics.json'), JSON.stringify(topics, null, 2)+'\n');
const searchIndex = { movies: movies.filter(m => m.status === 'published').map(m => ({type:m.typeDir||'movie',title:m.title,slug:m.slug,year:m.year,genre:m.genre,genres:m.genres,country:m.country,language:m.language,poster:m.poster,trailerStatus:m.youtubeId ? (m.trailerType === 'fan-made' ? 'fan-made' : 'official') : 'none'})), articles: articles.map(a => ({type:'article',title:a.title,slug:a.slug,description:a.description,category:a.category,tags:a.tags})), topics: topics.map(t => ({type:'topic',title:t.title,slug:t.slug,description:t.description})) };
fs.writeFileSync(path.join(root, 'data/search-index.json'), JSON.stringify(searchIndex)+'\n');

/* ------------------------------------------------------------------ */
/* Stylesheet                                                         */
/* ------------------------------------------------------------------ */
const css = `:root{--bg:#08090b;--panel:#111419;--line:#272b31;--text:#f4f5f6;--muted:#9aa1a9;--accent:#e94b2c;--gold:#e7bb5c;--movie:#e94b2c;--series:#4f8ef7;--anime:#b06ef7;--sports:#3ddc84;--memes:#ffd24a;--money:#e7bb5c;--tech:#4f8ef7;--ent:#e94b2c}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.55 Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}a{color:inherit;text-decoration:none}img{max-width:100%}.shell{max-width:1180px;margin:auto;padding:0 20px}.top{position:sticky;top:0;z-index:40;background:rgba(8,9,11,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}.top .shell{min-height:62px;display:flex;align-items:center;justify-content:space-between;gap:20px}.brand{font-weight:900;letter-spacing:.1em;font-size:17px;white-space:nowrap}.brand b{color:var(--accent)}.topnav{display:flex;gap:16px;overflow-x:auto;font-size:13px;font-weight:700;color:var(--muted);scrollbar-width:none}.topnav::-webkit-scrollbar{display:none}.topnav a:hover{color:#fff}.topnav a.active{color:#fff}.nav-search{color:var(--gold)!important}.hero{padding:64px 0 40px;background:radial-gradient(600px 260px at 70% 0,rgba(233,75,44,.15),transparent 70%)}.eyebrow{color:var(--gold);font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}.hero h1{font-size:clamp(32px,6vw,60px);line-height:1.05;max-width:850px;margin:10px 0 14px}.lead{max-width:680px;color:var(--muted);font-size:17px}.section{padding:26px 0}.section h2{font-size:22px;margin:0 0 14px}.section-head{display:flex;align-items:end;justify-content:space-between;gap:16px;margin:0 0 14px}.section-head h2{font-size:clamp(21px,3vw,28px);margin:0;line-height:1.15}.section-head>a{font-size:12px;font-weight:800;color:var(--gold);white-space:nowrap}.section-note{font-size:12px;color:var(--muted);margin:-8px 0 14px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(148px,1fr));gap:16px}.grid-2{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}.crumb{padding:22px 0 0;color:var(--muted);font-size:13px}.crumb a:hover{color:#fff}.poster{aspect-ratio:2/3;background:#171b20;border:1px solid var(--line);overflow:hidden;border-radius:4px;box-shadow:0 12px 28px rgba(0,0,0,.22);position:relative}.poster img{width:100%;height:100%;object-fit:cover;display:block}.placeholder{height:100%;display:grid;place-items:center;padding:16px;text-align:center;font-weight:800;font-size:13px;background:linear-gradient(145deg,#242b35,#0d0f13)}.tile{min-width:0;display:block;transition:transform .25s ease}.tile:hover{transform:translateY(-5px)}.tile h3{font-size:13.5px;margin:8px 0 0;line-height:1.3;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:2.6em}.tile-meta{display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-size:11.5px;color:var(--muted);margin:4px 0 0}.tile-meta .sep{opacity:.5}.tile-rating{font-size:11px;color:var(--gold);margin:3px 0 0;font-weight:700}.type-badge{display:inline-block;font-size:9.5px;font-weight:900;letter-spacing:.07em;padding:2.5px 6px;border-radius:3px;line-height:1;text-transform:uppercase;color:#0a0b0d}.tb-movie{background:var(--movie)}.tb-series{background:var(--series)}.tb-anime{background:var(--anime)}.tb-sports{background:var(--sports)}.tb-memes{background:var(--memes);color:#14171d}.tb-money{background:var(--money);color:#14171d}.tb-tech{background:var(--tech)}.tb-ent{background:var(--ent)}.rank{position:absolute;top:6px;left:6px;z-index:2;background:rgba(8,9,11,.82);border:1px solid rgba(255,255,255,.25);color:#fff;font-size:11px;font-weight:900;min-width:22px;height:22px;border-radius:4px;display:grid;place-items:center;padding:0 4px}.rank.top{border-color:var(--gold);color:var(--gold)}.rail{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(148px,182px);overflow-x:auto;gap:14px;padding:2px 1px 14px;scroll-snap-type:x mandatory}.rail .tile{scroll-snap-align:start}.loadmore{display:block;margin:18px auto 0;background:transparent;border:1px solid var(--line);color:var(--text);font:inherit;font-weight:700;padding:11px 22px;border-radius:5px;cursor:pointer}.loadmore:hover{border-color:var(--accent);color:#fff}.count-line{font-size:12.5px;color:var(--muted);margin:0 0 14px}.filterbar{display:flex;flex-wrap:wrap;gap:10px;align-items:end;padding:16px;margin:0 0 22px;background:#101318;border:1px solid var(--line);border-radius:6px}.ffield{display:flex;flex-direction:column;gap:4px;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}.ffield select{background:#171b20;color:var(--text);border:1px solid var(--line);border-radius:4px;font:inherit;font-size:13px;padding:8px 30px 8px 10px;max-width:190px}.fbtn{background:#171b20;border:1px solid var(--line);color:var(--muted);font:inherit;font-size:12.5px;font-weight:700;border-radius:4px;padding:8px 12px;cursor:pointer}.fbtn:hover{color:#fff;border-color:#444}.fbtn-clear{color:var(--gold)}.movie-hero{padding:34px 0 28px;display:grid;grid-template-columns:190px minmax(0,1fr);gap:28px}.movie-hero .poster{max-height:285px}.movie-hero h1{font-size:clamp(34px,6vw,58px);line-height:1.05;margin:8px 0}.badges{display:flex;flex-wrap:wrap;gap:7px}.badge{border:1px solid var(--line);color:var(--muted);padding:4px 9px;font-size:12px;border-radius:3px}.badge a:hover{color:#fff}.body{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:42px;padding:22px 0 60px}.prose h2{font-size:20px;margin:28px 0 8px}.prose p{color:#d9dde1}.aside{border-left:1px solid var(--line);padding-left:22px}.aside dt{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.08em;margin-top:16px}.aside dd{margin:3px 0}.cta{display:inline-block;background:var(--accent);padding:10px 15px;font-weight:800;margin-top:10px;border-radius:4px}.list{border-top:1px solid var(--line)}.row{display:flex;gap:14px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)}.row .thumb{height:64px;width:45px;background:#171b20;flex:none;border-radius:3px;overflow:hidden}.row .thumb img{height:100%;width:100%;object-fit:cover}.row b{display:block}.footer{border-top:1px solid var(--line);padding:28px 0 92px;color:var(--muted);font-size:13px}.footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:26px;margin:0 0 20px}.footer-brand p{margin:10px 0 0;max-width:260px;font-size:12.5px;line-height:1.6}.footer-col{display:flex;flex-direction:column;gap:8px}.footer-col h4{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--text);margin:0 0 4px}.footer-col a{color:var(--muted);font-size:13px}.footer-col a:hover{color:#fff}.footer-note{margin:0 0 14px}@media(max-width:760px){.footer-grid{grid-template-columns:1fr 1fr;gap:18px}.footer-brand{grid-column:1/-1}}.footer .foot-links{display:flex;flex-wrap:wrap;gap:16px;margin:12px 0 18px;font-weight:700}.footer .foot-links a:hover{color:#fff}.footer small{display:block;max-width:720px;line-height:1.6;opacity:.75}.mobile-nav{display:none}@media(max-width:760px){.shell{padding:0 14px}.top .shell{min-height:56px;padding:0 14px}.topnav{display:none}.hero{padding:44px 0 26px}.movie-hero{grid-template-columns:108px minmax(0,1fr);gap:15px}.movie-hero .poster{max-height:162px}.body{display:block}.aside{border-left:0;border-top:1px solid var(--line);padding:16px 0;margin-top:28px}.grid{grid-template-columns:repeat(3,1fr);gap:10px}.rail{grid-auto-columns:128px;gap:10px}.tile h3{font-size:12px;min-height:2.7em}.tile-meta{font-size:10.5px}.filterbar{flex-wrap:nowrap;overflow-x:auto;padding:12px;gap:8px}.ffield select{max-width:150px}.section-head{flex-wrap:wrap}}`;
fs.mkdirSync(path.join(root,'assets'),{recursive:true});
fs.writeFileSync(path.join(root,'assets/site.css'), css + '\n' + '.sports-feature{position:relative;display:grid;place-items:center;min-height:390px;margin:0 -20px 10px;padding:42px 24px;overflow:hidden;text-align:center;background:radial-gradient(ellipse at 50% 110%,rgba(61,220,132,.32),transparent 47%),linear-gradient(135deg,#06140d 0%,#0c2016 48%,#080b0d 100%);border-bottom:1px solid rgba(61,220,132,.35);isolation:isolate}.sports-feature:before{content:"";position:absolute;inset:-35% -10% 0;background:repeating-linear-gradient(118deg,transparent 0 74px,rgba(255,255,255,.035) 75px 77px,transparent 78px 152px);transform:skewY(-5deg);z-index:-1}.sports-feature:after{content:"⚽";position:absolute;right:7%;bottom:-20px;font-size:clamp(170px,28vw,350px);line-height:1;color:rgba(255,255,255,.045);z-index:-1}.sports-feature-inner{max-width:760px}.sports-feature .eyebrow{color:#77e9a8}.sports-feature h1{font-size:clamp(38px,6vw,70px);line-height:1.02;letter-spacing:-.035em;margin:12px auto}.sports-feature p{max-width:610px;margin:0 auto;color:#c3d0c8;font-size:clamp(15px,2vw,18px);line-height:1.6}.sports-feature .cta{margin-top:24px;background:#3ddc84;color:#07120b;padding:12px 19px;border-radius:5px}.sports-feature .cta:hover{filter:brightness(1.08)}.sports-feature-meta{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:18px}.sports-feature-meta span{font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#b9c9bf;border:1px solid rgba(255,255,255,.17);border-radius:20px;padding:5px 10px;background:rgba(4,12,8,.34)}@media(max-width:760px){.sports-feature{min-height:365px;margin:0 -14px 6px;padding:38px 18px}.sports-feature h1{font-size:40px}.sports-feature:after{right:-15px;font-size:230px}.sports-feature-meta{gap:7px}}\\n' + `/* Primary platform experience */
.home-hero{min-height:560px;display:flex;align-items:end;position:relative;isolation:isolate;background:#111820}.home-hero:before{content:"";position:absolute;inset:0;z-index:-2;background-image:var(--hero-image);background-size:cover;background-position:center;filter:saturate(.78) contrast(1.08)}.home-hero:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(5,7,10,.96) 0%,rgba(5,7,10,.72) 42%,rgba(5,7,10,.18) 100%),linear-gradient(0deg,#08090b,transparent 52%)}.home-hero-inner{padding-top:120px;padding-bottom:64px;max-width:1180px;width:100%}.home-hero h1{font-size:clamp(42px,7vw,78px);line-height:.96;max-width:720px;margin:10px 0}.home-hero p{max-width:580px;color:#d2d6d9;font-size:16.5px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.hero-facts{font-size:14px;color:#d3d7d9;display:flex;gap:8px;align-items:center;flex-wrap:wrap}.hero-actions{display:flex;gap:18px;align-items:center;margin-top:22px}.quiet-link{font-weight:750;color:#fff;border-bottom:1px solid rgba(255,255,255,.4);padding:9px 0}.home-main{padding-bottom:30px}.home-section{padding:30px 0}.home-section h2{font-size:clamp(21px,3vw,27px);margin:0}.genre-trio{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.genre-panel{background:#101318;border:1px solid var(--line);border-radius:6px;padding:18px}.genre-panel h3{font-size:15px;margin:0 0 12px;display:flex;align-items:center;gap:8px}.genre-panel .gp-count{font-size:11px;color:var(--muted);font-weight:700}.genre-chips{display:flex;flex-wrap:wrap;gap:7px}.genre-chips a{font-size:12px;font-weight:700;padding:6px 10px;border:1px solid var(--line);border-radius:20px;color:#d9dde1}.genre-chips a:hover{border-color:var(--accent);color:#fff}.genre-chips a b{color:var(--muted);font-weight:700;margin-left:3px}.editorial-row{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.editorial-card{display:block}.editorial-card .poster{aspect-ratio:16/10}.editorial-card h3{font-size:18px;margin:5px 0}.editorial-card span,.editorial-card p{font-size:12px;color:var(--muted)}.editorial-card p{margin:0}.story-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#30343a}.story-grid a{min-height:225px;padding:22px;background:#111419;display:flex;flex-direction:column;align-items:flex-start}.story-grid a:hover{background:#191d23}.story-grid span{font-size:11px;font-weight:800;color:var(--gold);text-transform:uppercase;letter-spacing:.08em}.story-grid h3{font-size:21px;line-height:1.1;margin:10px 0}.story-grid p{font-size:13px;color:var(--muted);margin:0 0 14px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.story-grid b{font-size:13px;margin-top:auto}.discover-cta{margin:40px 0 0;padding:40px;display:flex;align-items:center;justify-content:space-between;gap:30px;border-top:1px solid #353940;background:linear-gradient(90deg,#14171c,#0e1014)}.discover-cta p{color:var(--muted);max-width:480px}.discover-cta .cta{margin:0}.share-action{background:none;border:0;cursor:pointer;margin-left:14px;font:inherit}.article-hero .share-action{margin:16px 0 0}.article-hero{padding:70px 0 30px;max-width:820px}.article-hero h1{font-size:clamp(36px,6vw,60px);line-height:1.04;margin:10px 0}.article-meta{color:var(--muted);font-size:13px;margin-top:18px;display:flex;flex-wrap:wrap;align-items:center;gap:10px}.article-meta span+span:before{content:"\\00b7";margin-right:10px;opacity:.55}.article-body{max-width:760px;padding:28px 0 70px}.article-body h2{margin-top:38px;font-size:28px;line-height:1.16}.article-body p{font-size:18px;line-height:1.75;color:#d9dde1}.article-body blockquote{margin:24px 0;padding:4px 0 4px 22px;border-left:3px solid var(--gold);font-size:clamp(20px,3vw,27px);line-height:1.35;color:#fff}.article-source{font-size:13px!important;color:var(--gold)!important;font-weight:750;letter-spacing:.02em}.article-related{margin-top:56px;padding-top:28px;border-top:1px solid var(--line)}.article-related p{font-size:15px}.movie-hero{max-width:1180px;margin:0 auto;padding:64px 20px 40px;grid-template-columns:190px minmax(0,620px);align-items:end;min-height:470px;position:relative}.movie-hero:before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,#08090b 18%,rgba(8,9,11,.72) 55%,rgba(8,9,11,.95)),linear-gradient(0deg,#08090b,transparent),var(--movie-backdrop);background-size:cover;background-position:center}.movie-hero .poster{border-radius:4px}.movie-hero .lead{font-size:16px;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}.movie-hero h1{font-size:clamp(30px,5vw,52px)}.trailer-section{padding:0 20px 18px}.trailer-frame{position:relative;max-width:860px;aspect-ratio:16/9;background:#000;border-radius:6px;overflow:hidden;cursor:pointer;border:1px solid var(--line)}.trailer-frame img{width:100%;height:100%;object-fit:cover;opacity:.85}.trailer-frame iframe{width:100%;height:100%;border:0;display:block}.trailer-play{position:absolute;inset:0;margin:auto;width:74px;height:50px;border:0;border-radius:10px;background:rgba(233,75,44,.92);cursor:pointer;display:grid;place-items:center}.trailer-play:before{content:"";border-left:16px solid #fff;border-top:10px solid transparent;border-bottom:10px solid transparent;margin-left:4px}.trailer-play:hover{background:var(--accent)}.trailer-fallback{font-size:12.5px;color:var(--muted);margin:10px 0 0}.trailer-unavailable{padding:34px 18px;border:1px dashed var(--line);border-radius:6px;max-width:860px;text-align:center;color:var(--muted)}.trailer-unavailable b{display:block;color:var(--text);margin-bottom:4px}.searchbox{width:100%;max-width:640px;background:#101318;border:1px solid var(--line);border-radius:6px;color:var(--text);font:inherit;font-size:18px;padding:14px 16px;margin:14px 0}.searchbox:focus{outline:0;border-color:var(--accent)}.searchnote{color:var(--muted);font-size:13px;margin:0 0 18px}.search-tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px}.stabs{background:#101318;border:1px solid var(--line);color:var(--muted);font:inherit;font-size:12.5px;font-weight:800;padding:8px 14px;border-radius:20px;cursor:pointer}.stabs.active{background:var(--accent);border-color:var(--accent);color:#fff}.search-group{grid-column:1/-1;font-size:12px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin:14px 0 0;display:flex;align-items:center;gap:10px}.search-group:after{content:"";flex:1;height:1px;background:var(--line)}.trend-note{font-size:13px;color:var(--muted);background:#101318;border:1px solid var(--line);border-left:3px solid var(--gold);padding:14px 18px;border-radius:0 6px 6px 0;margin:0 0 26px}.trend-note code{color:var(--gold);font-size:12px}.boost-reason{font-size:11px;color:var(--muted);margin:3px 0 0}.score-pill{display:inline-flex;align-items:center;gap:4px;font-size:10.5px;font-weight:900;color:var(--gold);border:1px solid rgba(231,187,92,.4);border-radius:20px;padding:2px 8px}.mobile-nav{position:fixed;bottom:0;left:0;right:0;z-index:50;background:rgba(12,14,17,.97);backdrop-filter:blur(15px);border-top:1px solid #2a2e34;display:none;grid-auto-flow:column;grid-auto-columns:74px;overflow-x:auto;scrollbar-width:none;justify-content:start}.mobile-nav::-webkit-scrollbar{display:none}.mobile-nav a{text-align:center;padding:10px 2px 9px;color:#b6bdc5;font-size:10px;font-weight:800;line-height:1.2}.mobile-nav a:active,.mobile-nav a.active{color:#fff;background:#1a1e23}.mobile-nav .mn-ico{display:block;font-size:15px;margin-bottom:2px}@media(max-width:760px){body{padding-bottom:62px}.mobile-nav{display:grid}.home-hero{min-height:500px}.home-hero:after{background:linear-gradient(0deg,#08090b 0%,rgba(8,9,11,.86) 36%,rgba(8,9,11,.22) 100%)}.home-hero-inner{padding-top:170px;padding-bottom:36px}.home-hero h1{font-size:42px}.home-hero p{font-size:14.5px}.split-none{display:none}.editorial-row{grid-template-columns:repeat(2,1fr);gap:12px}.editorial-card .poster{aspect-ratio:1/1}.editorial-card p{display:none}.discover-cta{margin:30px -14px 0;padding:26px 14px;display:block}.discover-cta .cta{margin-top:12px}.genre-trio{grid-template-columns:1fr}.genre-panel h3{font-size:16px}.movie-hero{padding:110px 14px 24px;min-height:400px;grid-template-columns:100px minmax(0,1fr);gap:14px}.movie-hero .lead{display:none}.movie-hero .poster{max-height:150px}.trailer-section{padding:0 14px 14px}.story-grid{grid-template-columns:1fr}.story-grid a{min-height:170px}.article-hero{padding:44px 0 18px}.article-body{padding-top:16px}.article-body p{font-size:16px;line-height:1.7}.article-body h2{font-size:24px}}.trailer-section-inner{max-width:860px}.trailer-head{display:flex;align-items:center;gap:12px;margin:0 0 12px}.trailer-status{font-size:13px;font-weight:900;letter-spacing:.04em;padding:5px 12px;border-radius:20px;border:1px solid var(--line)}.trailer-status.t-ok{color:#3ddc84;border-color:rgba(61,220,132,.45)}.trailer-status.t-fan{color:#e7bb5c;border-color:rgba(231,187,92,.5)}.trailer-status.t-none{color:var(--muted)}.trailer-meta{font-size:12.5px;color:var(--muted);margin:10px 0 0}.trailer-verif-note{color:var(--gold);font-size:11px;margin-left:6px}.trailer-disclaimer{font-size:12.5px;color:#d9a441;background:rgba(231,187,92,.08);border:1px solid rgba(231,187,92,.3);padding:8px 12px;border-radius:5px;margin:10px 0 0}.trailer-error{border:1px dashed #b34a3a;background:rgba(179,74,58,.08);border-radius:6px;padding:18px 16px;margin:10px 0 0;color:var(--muted)}.trailer-error b{display:block;color:#ff8a75;margin-bottom:4px}.trailer-error-actions{display:flex;gap:18px;margin-top:10px}.trailer-alt{display:inline-block;margin-top:12px;background:transparent;border:1px solid var(--line);color:var(--text);font:inherit;font-size:13px;font-weight:700;padding:9px 16px;border-radius:5px;cursor:pointer}.trailer-alt:hover{border-color:var(--accent)}.trailer-retry{background:transparent;border:1px solid var(--line);color:var(--text);font:inherit;font-size:12.5px;font-weight:700;padding:7px 14px;border-radius:4px;cursor:pointer;margin-left:12px}.trailer-retry:hover{border-color:var(--accent)}.trailer-table{width:100%;border-collapse:collapse;font-size:13px}.trailer-table th,.trailer-table td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.trailer-table th{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em}.tr-tag{display:inline-block;font-size:10px;font-weight:900;padding:2px 7px;border-radius:3px;letter-spacing:.05em}.tr-tag.ok{background:rgba(61,220,132,.15);color:#3ddc84}.tr-tag.fan{background:rgba(231,187,92,.15);color:#e7bb5c}.tr-tag.miss{background:rgba(154,161,169,.12);color:var(--muted)}.tr-tag.bad{background:rgba(179,74,58,.15);color:#ff8a75}.trailer-admin-filters{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 16px}.trailer-admin-filters select,.trailer-admin-filters input{background:#171b20;color:var(--text);border:1px solid var(--line);border-radius:4px;font:inherit;font-size:13px;padding:8px 12px}.legal-prose{max-width:760px;padding:10px 0 70px}.legal-prose h2{margin-top:34px}.legal-prose p{font-size:16px;line-height:1.75}@media(max-width:760px){.legal-prose p{font-size:15px}}.hero-carousel{position:relative;min-height:560px;background:#0d0f13;overflow:hidden;isolation:isolate}.hero-slides{position:absolute;inset:0}.hero-slide{position:absolute;inset:0;opacity:0;transform:scale(1.04);transition:opacity .8s ease,transform 8s linear;background-size:cover;background-position:center 28%;visibility:hidden}.hero-slide.is-active{opacity:1;transform:scale(1.08);visibility:visible;z-index:1}.hero-slide-shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,7,10,.97) 0%,rgba(5,7,10,.78) 40%,rgba(5,7,10,.25) 100%),linear-gradient(0deg,#08090b 0%,rgba(8,9,11,0) 55%)}.hero-slide-inner{position:relative;z-index:2;padding-top:120px;padding-bottom:64px;max-width:1180px;width:100%}.hero-slide-kicker{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:13px;font-weight:800;color:#d3d7d9;letter-spacing:.06em;margin-bottom:12px}.hero-slide-kicker .dot{opacity:.35}.hero-slide h1{font-size:clamp(42px,7vw,78px);line-height:.96;max-width:760px;margin:0 0 10px}.hero-slide-rating{color:var(--gold);font-weight:800;font-size:14px;margin:0 0 10px}.hero-slide p{max-width:560px;color:#d2d6d9;font-size:16.5px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.hero-slide .hero-actions{margin-top:22px}.hero-video{position:absolute;inset:0;z-index:1}.hero-video iframe{width:100%;height:100%;border:0;display:block}.hero-ctrl{position:absolute;top:50%;transform:translateY(-50%);z-index:5;width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.25);background:rgba(8,9,11,.6);color:#fff;font-size:22px;line-height:1;cursor:pointer;display:grid;place-items:center;backdrop-filter:blur(4px)}.hero-ctrl:hover{background:rgba(8,9,11,.9);border-color:var(--accent)}.hero-prev{left:14px}.hero-next{right:14px}.hero-dots{position:absolute;bottom:18px;left:50%;transform:translateX(-50%);z-index:5;display:flex;gap:8px}.hero-dot{width:10px;height:10px;border-radius:50%;border:1px solid rgba(255,255,255,.5);background:transparent;padding:0;cursor:pointer}.hero-dot.is-active{background:var(--accent);border-color:var(--accent)}.hero-vctrl{position:absolute;right:14px;top:14px;z-index:5;width:40px;height:40px;border-radius:50%;border:1px solid rgba(255,255,255,.3);background:rgba(8,9,11,.65);color:#fff;font-size:16px;cursor:pointer;display:grid;place-items:center}.hero-pause{right:60px}.rec-section{padding:44px 0}.rec-inner{background:linear-gradient(135deg,#151922,#0e1014);border:1px solid var(--line);border-radius:10px;padding:34px 30px;display:grid;gap:18px}.rec-copy h2{font-size:clamp(26px,4vw,40px);margin:6px 0 6px}.rec-sub{color:var(--muted);font-size:15.5px;margin:0;max-width:560px}.rec-form{display:flex;gap:12px;flex-wrap:wrap}.rec-form input{flex:1 1 280px;background:#0d1013;border:1px solid var(--line);border-radius:6px;color:var(--text);font:inherit;font-size:16px;padding:15px 16px}.rec-form input:focus{outline:2px solid var(--accent);outline-offset:-1px}.rec-cta{font-size:15px;padding:15px 22px;margin:0}.rec-status{color:var(--muted);font-size:14px;min-height:0}.rec-suggest{position:relative;z-index:8;background:#101318;border:1px solid var(--line);border-radius:8px;margin-top:6px;overflow:hidden;max-height:280px;overflow-y:auto}.rec-suggest[hidden]{display:none}.rec-sug-item{display:flex;align-items:center;gap:12px;width:100%;background:none;border:0;border-bottom:1px solid var(--line);color:var(--text);font:inherit;text-align:left;padding:8px 12px;cursor:pointer}.rec-sug-item:last-child{border-bottom:0}.rec-sug-item:hover,.rec-sug-item:focus-visible{background:#1a1e25;outline:none}.rec-sug-item img{width:60px;height:45px;object-fit:cover;border-radius:4px;flex:none}.rec-sug-ph{width:60px;height:45px;flex:none;border-radius:4px;background:#1a1e25}.rec-sug-txt{display:flex;flex-direction:column;gap:2px;min-width:0}.rec-sug-txt b{font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.rec-sug-txt small{font-size:11px;color:var(--muted);font-weight:800;letter-spacing:.05em}.rec-results{margin-top:8px}.rec-results h3{font-size:clamp(19px,3vw,24px);margin:0 0 4px}.rec-reason{color:var(--muted);font-size:14px;margin:0 0 18px}.rec-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:16px}.rec-grid .tile .tile-meta{margin-top:4px}.rec-tag{display:inline-block;font-size:10.5px;font-weight:800;color:var(--gold);border:1px solid rgba(231,187,92,.35);border-radius:12px;padding:2px 8px;margin:5px 3px 0 0}.rec-actions{display:flex;gap:8px;margin-top:8px}.rec-actions a{font-size:11.5px;font-weight:800;padding:7px 10px;border-radius:4px}.rec-actions .ra-trailer{background:var(--accent);color:#fff}.rec-actions .ra-details{border:1px solid var(--line);color:var(--muted)}.rec-actions .ra-details:hover{color:#fff;border-color:var(--accent)}.rec-miss{background:#101318;border:1px dashed var(--line);border-radius:8px;padding:20px}.rec-miss b{display:block;font-size:17px;margin-bottom:4px}.rec-miss .rec-pop{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.rec-miss .rec-pop a{border:1px solid var(--line);padding:6px 12px;border-radius:20px;font-size:12.5px;font-weight:700}.brand-strip{padding:30px 0 6px}.brand-slogan{font-size:clamp(16px,2.6vw,22px);font-weight:800;letter-spacing:.02em;color:var(--text);margin:0 0 18px}.vchips{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}.vchip{position:relative;display:flex;flex-direction:column;gap:6px;padding:16px 18px;border:1px solid var(--line);border-radius:10px;background:linear-gradient(145deg,#14171d,#0e1014);overflow:hidden;transition:transform .2s,box-shadow .2s}.vchip:hover{transform:translateY(-3px);box-shadow:0 10px 26px rgba(0,0,0,.35)}.vchip:before{content:"";position:absolute;inset:0;opacity:.16;background:radial-gradient(200px 80px at 30% 0%,var(--vc,#fff),transparent 70%);pointer-events:none}.vchip-emoji{font-size:22px}.vchip-name{font-weight:900;font-size:14.5px}.vchip-tag{font-size:11.5px;color:var(--muted);line-height:1.45}.vchip-sports{--vc:#3ddc84}.vchip-memes{--vc:#ffd24a}.vchip-make-money{--vc:#e7bb5c}.vchip-tech{--vc:#4f8ef7}.vchip-entertainment{--vc:#e94b2c}.vhero{border-bottom:1px solid var(--line)}.vhero-sports{background:radial-gradient(500px 220px at 70% 0,rgba(61,220,132,.14),transparent 70%)}.vhero-memes{background:radial-gradient(500px 220px at 70% 0,rgba(255,210,74,.13),transparent 70%)}.vhero-make-money{background:radial-gradient(500px 220px at 70% 0,rgba(231,187,92,.14),transparent 70%)}.vhero-tech{background:radial-gradient(500px 220px at 70% 0,rgba(79,142,247,.15),transparent 70%)}.vcat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}.vcat{display:flex;flex-direction:column;gap:4px;padding:15px 17px;border:1px solid var(--line);border-radius:8px;background:#101318}.vcat:hover{border-color:var(--accent)}.vcat b{font-size:14.5px}.vcat span{font-size:12px;color:var(--muted);line-height:1.5}.vnote{border:1px solid var(--line);border-left:3px solid var(--gold);background:#101318;padding:12px 16px;border-radius:0 6px 6px 0;font-size:13px;color:var(--muted);line-height:1.6;max-width:820px}.vstate{border:1px dashed var(--line);border-radius:8px;padding:28px;text-align:center;color:var(--muted)}.sp-result{border:1px solid var(--line);border-left:3px solid #3ddc84;background:#101318;border-radius:0 8px 8px 0;padding:18px 20px;margin:14px 0}.sp-pill-ft{background:rgba(61,220,132,.15);color:#3ddc84;border-color:rgba(61,220,132,.45)}.sp-score{display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-size:clamp(19px,3vw,25px);margin:10px 0 4px}.sp-score b{font-size:1.25em;font-variant-numeric:tabular-nums}.sp-score i{opacity:.45;font-style:normal}.sp-score span{color:#d9dde1}.sp-pens{font-size:13px;color:var(--gold);font-weight:700}.sp-result-meta{font-size:12.5px;color:var(--muted);margin:2px 0 0}.sp-scorers{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0 4px}.sp-scorers b{font-size:12.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.05em}.sp-scorers ul{list-style:none;padding:0;margin:6px 0 0}.sp-scorers li{font-size:14px;padding:2px 0}.sp-scorers li span{color:var(--muted);font-size:12px}.sp-scorers .sp-none{color:var(--muted)}@media(max-width:600px){.sp-scorers{grid-template-columns:1fr}}.vstate b{display:block;font-size:17px;color:var(--text);margin-bottom:6px}
/* ==== BRYME SPORTS ==== */
.sp-pl-hero{padding:44px 0 8px}.sp-pl-hero h1{font-size:clamp(34px,6vw,64px);line-height:1.02;margin:8px 0}
.sp-hero{position:relative;margin:26px 0 10px;max-width:100%;overflow:hidden}.sp-hero-track{display:grid;grid-auto-flow:column;grid-auto-columns:calc((100% - 48px)/3);gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:4px 2px 18px;scrollbar-width:none;overscroll-behavior-x:contain;scrollbar-gutter:stable}.sp-hero-track::-webkit-scrollbar{display:none}.sp-hero-card{scroll-snap-align:start}
.sp-hero-card{position:relative;min-height:240px;display:flex;flex-direction:column;justify-content:flex-end;gap:8px;padding:22px;border-radius:12px;background:linear-gradient(150deg,#14241c,#0d1511 70%);border:1px solid rgba(61,220,132,.25);overflow:hidden;scroll-snap-align:start;transition:transform .2s,box-shadow .2s;isolation:isolate}.sp-hero-card:after{content:"";position:absolute;inset:0;z-index:-1;background-image:var(--card-img);background-size:cover;background-position:center;opacity:.28;transition:opacity .3s}.sp-hero-card:hover:after{opacity:.4}.sp-hero-card>*{position:relative;z-index:1;text-shadow:0 2px 8px rgba(0,0,0,.85)}.sp-hero-card:hover{transform:translateY(-4px);box-shadow:0 14px 30px rgba(0,0,0,.4)}.sp-hero-card:before{content:"";position:absolute;inset:0;opacity:.14;background:radial-gradient(240px 120px at 80% 0,rgba(61,220,132,.8),transparent 70%);pointer-events:none}.sp-hero-first{border-color:rgba(61,220,132,.55)}
.sp-hero-tag{font-size:10.5px;font-weight:900;letter-spacing:.1em;color:var(--sports);text-transform:uppercase}.sp-hero-card h3{font-size:clamp(17px,1.6vw,21px);line-height:1.2;margin:0}.sp-hero-card p{font-size:12.5px;color:var(--muted);line-height:1.5;margin:0;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.sp-hero-crests{display:flex;align-items:center;gap:7px}.sp-hero-crests img{width:26px;height:32px;object-fit:contain;filter:drop-shadow(0 2px 6px rgba(0,0,0,.6))}.sp-hero-crests b{color:var(--muted);font-size:10px;font-weight:800}.sp-hero-go{font-size:12px;font-weight:800;color:var(--sports)}
.sp-hero-arrow{position:absolute;top:40%;transform:translateY(-50%);z-index:3;width:38px;height:38px;border-radius:50%;border:1px solid rgba(255,255,255,.25);background:rgba(8,9,11,.7);color:#fff;font-size:20px;cursor:pointer;display:grid;place-items:center}.sp-hero-prev{left:2px}.sp-hero-next{right:2px}.sp-hero-arrow:hover{border-color:var(--sports)}
.sp-table-wrap{overflow-x:auto;margin:10px 0 26px;border:1px solid var(--line);border-radius:8px}.sp-table{width:100%;border-collapse:collapse;font-size:13px;min-width:640px}.sp-table th,.sp-table td{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left}.sp-table th{background:#101318;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.07em}.sp-table td{vertical-align:top}.sp-empty td{color:var(--muted);font-style:italic;padding:22px;line-height:1.6;text-align:center}
.sp-dir{font-size:17px;margin:22px 0 6px}.sp-st-conf,.sp-st-rep,.sp-st-rum{display:inline-block;font-size:11px;font-weight:800;padding:2px 9px;border-radius:12px;margin-right:6px}.sp-st-conf{background:rgba(61,220,132,.15);color:#3ddc84;border:1px solid rgba(61,220,132,.4)}.sp-st-rep{background:rgba(231,187,92,.12);color:#e7bb5c;border:1px solid rgba(231,187,92,.4)}.sp-st-rum{background:rgba(154,161,169,.12);color:var(--muted);border:1px solid rgba(154,161,169,.4)}
.sp-ed-label{display:inline-block;background:rgba(231,187,92,.12);color:#e7bb5c;border:1px solid rgba(231,187,92,.45);font-size:12px;font-weight:900;letter-spacing:.06em;padding:6px 14px;border-radius:20px;margin:10px 0}
.sp-article{max-width:820px;margin:0 auto;padding:10px 0 60px}.sp-article-head{padding:34px 0 24px}.sp-article-head h1{font-size:clamp(30px,5vw,52px);line-height:1.05;margin:10px 0}.sp-meta{display:flex;flex-wrap:wrap;gap:8px 18px;color:var(--muted);font-size:12.5px;margin-top:16px}
.sp-img{aspect-ratio:16/7;background:linear-gradient(145deg,#1a2026,#0d1013);border:1px dashed var(--line);border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:var(--muted);text-align:center;padding:20px}.sp-img span{font-weight:800;color:var(--text)}.sp-img small{font-size:11px}
.sp-body-placeholder{border:1px dashed var(--line);border-radius:10px;padding:30px;margin:18px 0;text-align:center}.sp-body-placeholder b{font-size:17px;display:block;margin-bottom:6px}.sp-body-placeholder p{color:var(--muted);font-size:14px;max-width:560px;margin:0 auto;line-height:1.6}
.sp-source{margin-top:30px;border:1px solid var(--line);border-radius:8px;padding:18px 20px;background:#101318}.sp-source h2{font-size:16px;margin:0 0 8px}.sp-source p{margin:6px 0;font-size:13.5px}.sp-source-note{font-size:12.5px;color:var(--muted);line-height:1.6;margin:8px 0 0}
.sp-related{margin-top:34px;padding-top:24px;border-top:1px solid var(--line)}.sp-related h2{font-size:18px;margin:0 0 14px}.sp-rel-grid{display:flex;flex-wrap:wrap;gap:10px}.sp-rel{border:1px solid var(--line);border-radius:20px;padding:8px 14px;font-size:12.5px;font-weight:700;color:#d9dde1}.sp-rel:hover{border-color:var(--sports);color:#fff}.sp-rel-static{color:var(--muted);cursor:default}
.sp-mc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin:18px 0}.sp-mc-card{min-height:120px;border:1px dashed var(--line);border-radius:10px;padding:18px;display:flex;flex-direction:column;justify-content:flex-end;background:#101318}.sp-mc-card b{font-size:15px}.sp-mc-card p{font-size:12.5px;color:var(--muted);margin:4px 0 0;line-height:1.5}
.sp-live{display:flex;gap:14px;align-items:flex-start;background:linear-gradient(135deg,rgba(61,220,132,.1),rgba(61,220,132,.03));border:1px solid rgba(61,220,132,.35);border-radius:10px;padding:18px 20px;margin:6px 0 14px}.sp-live-dot{flex:none;width:12px;height:12px;border-radius:50%;background:#3ddc84;margin-top:5px;box-shadow:0 0 0 0 rgba(61,220,132,.6);animation:spPulse 2s infinite}@keyframes spPulse{0%{box-shadow:0 0 0 0 rgba(61,220,132,.55)}70%{box-shadow:0 0 0 9px rgba(61,220,132,0)}100%{box-shadow:0 0 0 0 rgba(61,220,132,0)}}.sp-live b{font-size:15px;letter-spacing:.04em}.sp-live p{margin:4px 0 0;font-size:13px;color:var(--muted);line-height:1.6}.sp-updated{font-size:12.5px;color:var(--gold);font-weight:800;margin:0 0 16px}.sp-truth{display:flex;gap:12px;align-items:flex-start;background:rgba(231,187,92,.06);border:1px solid rgba(231,187,92,.3);border-radius:10px;padding:14px 18px;margin:0 0 14px}.sp-truth b{color:var(--gold);font-size:13px;flex:none}.sp-legend-line{font-size:12.5px;color:var(--muted);margin:0 0 14px}.sp-mgr-club{display:flex;align-items:center;gap:10px}.sp-mgr-club img{flex:none}.sp-mgr-badge{display:inline-block;font-size:10.5px;font-weight:900;letter-spacing:.06em;padding:2px 8px;border-radius:12px;margin-right:8px}.sp-mgr-new{background:rgba(61,220,132,.15);color:#3ddc84;border:1px solid rgba(61,220,132,.4)}.sp-mgr-keep{background:rgba(154,161,169,.12);color:var(--muted);border:1px solid rgba(154,161,169,.35)}.sp-mgr-note{font-size:12px;color:var(--muted)}.sp-mgr-pending{color:var(--muted);font-style:italic}.sp-credits{font-size:11.5px;color:var(--muted);line-height:1.6;border:1px solid var(--line);border-left:3px solid var(--gold);background:#101318;padding:10px 14px;border-radius:0 6px 6px 0;margin:0 0 18px}.sp-truth p{margin:0;font-size:12.5px;color:var(--muted);line-height:1.6}.sp-freq-note{font-size:12.5px;color:var(--muted);margin:-8px 0 16px;font-style:italic}
.sp-club-nav{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 22px}.sp-club-nav a{font-size:12px;font-weight:700;border:1px solid var(--line);border-radius:16px;padding:5px 11px;color:var(--muted)}.sp-club-nav a:hover{color:#fff;border-color:var(--sports)}
.sp-clubs{display:flex;flex-direction:column;gap:20px}.sp-club{border:1px solid var(--line);border-radius:12px;background:#101318;overflow:hidden}.sp-club-head{display:flex;gap:16px;align-items:center;padding:16px 20px;background:linear-gradient(90deg,#151a21,#101318)}.sp-club-head img{width:56px;height:67px;object-fit:contain;filter:drop-shadow(0 4px 10px rgba(0,0,0,.5))}.sp-club-head h2{font-size:22px;margin:0}.sp-club-man{font-size:13px;color:var(--muted);margin:3px 0 0}.sp-club-man b{color:var(--text)}.sp-club-cols{display:grid;grid-template-columns:1fr 1fr;gap:0}.sp-club-col{padding:6px 20px 18px}.sp-club-col h3{font-size:13px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--sports);margin:12px 0 8px}.sp-club-col+.sp-club-col{border-left:1px solid var(--line)}.sp-club .sp-table{min-width:0}.sp-club-notes{font-size:13px;color:#c9ced4;line-height:1.65;border-top:1px solid var(--line);padding:14px 20px;margin:0}.sp-club-notes b{color:var(--gold)}.sp-rumours{margin:0 20px 12px;border:1px dashed rgba(231,187,92,.4);border-radius:8px;padding:12px 16px;font-size:13px}.sp-rumours b{color:#e7bb5c;display:block;margin-bottom:6px}.sp-rumours p{margin:3px 0;color:var(--muted)}
.sp-window-note{margin:26px 0 0;font-size:13px;color:var(--muted);font-style:italic}.sp-signoff{margin:26px 0 8px;font-size:13px;color:var(--gold);font-weight:800}
.sp-mw{border:1px solid var(--line);border-radius:10px;background:#101318;margin:0 0 18px;overflow:hidden}.sp-mw-head{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px;padding:12px 18px;background:linear-gradient(90deg,#151a21,#101318);border-bottom:1px solid var(--line)}.sp-mw-head h2{font-size:17px;margin:0}.sp-mw-date{font-size:12px;color:var(--muted);font-weight:700}.sp-fixture{display:grid;grid-template-columns:1fr auto;gap:4px 18px;align-items:center;padding:11px 18px;border-bottom:1px solid var(--line)}.sp-fixture:last-child{border-bottom:0}.sp-fixture:hover{background:#161b22}.sp-fixt{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font-size:14.5px;font-weight:700}.sp-fixt img{width:22px;height:27px;object-fit:contain;filter:drop-shadow(0 2px 5px rgba(0,0,0,.5))}.sp-fixt .sp-vs{color:var(--muted);font-weight:400;font-size:12px}.sp-fixt a{color:var(--text)}.sp-fixt a:hover{color:var(--sports)}.sp-fixt-info{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font-size:12px;color:var(--muted)}.sp-fixt-day{font-weight:800;color:#c9ced4}.sp-fixt-time{font-weight:800;color:var(--text)}.sp-std{font-size:10px;color:var(--muted);font-weight:700}.sp-tv{font-size:10.5px;font-weight:900;letter-spacing:.04em;padding:2px 8px;border-radius:11px;background:rgba(79,142,247,.14);color:#7fb0ff;border:1px solid rgba(79,142,247,.35)}.sp-tv.tnt{background:rgba(233,75,44,.12);color:#ff9d8a;border-color:rgba(233,75,44,.35)}.sp-matchlink{font-size:12px;font-weight:800;color:var(--sports)}.sp-matchlink:hover{text-decoration:underline}.sp-mwnav{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 18px}.sp-mwnav a{font-size:11.5px;font-weight:800;border:1px solid var(--line);border-radius:14px;padding:4px 9px;color:var(--muted)}.sp-mwnav a:hover{color:#fff;border-color:var(--sports)}.sp-fix-legend{font-size:12px;color:var(--muted);line-height:1.7;border:1px dashed var(--line);border-radius:8px;padding:12px 16px;margin:0 0 20px}.sp-match-hero{display:flex;gap:20px;align-items:center;flex-wrap:wrap;margin:10px 0 22px;padding:22px 24px;border:1px solid var(--line);border-radius:12px;background:linear-gradient(90deg,#151a21,#101318)}.sp-match-hero img{width:64px;height:77px;object-fit:contain;filter:drop-shadow(0 4px 10px rgba(0,0,0,.5))}.sp-match-hero .sp-mh-vs{font-size:18px;color:var(--muted);font-weight:800}.sp-match-hero h1{font-size:clamp(24px,4vw,36px);margin:0;line-height:1.05}.sp-match-meta{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13px;color:var(--muted);margin:0 0 4px}.sp-match-meta b{color:var(--text)}.sp-pill{display:inline-block;font-size:11px;font-weight:900;letter-spacing:.05em;padding:3px 10px;border-radius:13px;background:rgba(61,220,132,.13);color:#3ddc84;border:1px solid rgba(61,220,132,.4);margin-right:6px}.sp-msec-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;margin:14px 0 8px}.sp-msec{min-height:96px;border:1px dashed var(--line);border-radius:9px;padding:14px 16px;background:#0f1217;display:flex;flex-direction:column;gap:5px}.sp-msec b{font-size:13.5px;color:#d9dde1}.sp-msec p{font-size:12px;color:var(--muted);margin:0;line-height:1.5}.sp-msec .sp-pend{font-size:10.5px;font-weight:900;letter-spacing:.06em;color:var(--gold);text-transform:uppercase}.sp-mc-card.solid{border:1px solid var(--line);border-style:solid;background:linear-gradient(180deg,#14181f,#101318)}.sp-mc-card a.sp-mc-go{font-size:12px;font-weight:800;color:var(--sports);text-decoration:none;margin-top:8px}.sp-mc-card a.sp-mc-go:hover{text-decoration:underline}.sp-mc-crests{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:10px}.sp-mc-crests img{width:30px;height:36px;object-fit:contain;filter:drop-shadow(0 2px 6px rgba(0,0,0,.5))}.sp-mc-crests .sp-vs{color:var(--muted);font-size:11px;font-weight:800}
@media(max-width:760px){.sp-club-cols{grid-template-columns:1fr}.sp-club-col+.sp-club-col{border-left:0;border-top:1px solid var(--line)}.sp-club-head{padding:14px 16px}.sp-club-head h2{font-size:19px}.sp-club .sp-table{min-width:430px}.sp-live{padding:14px 16px}}
.sp-gw-sec{padding:16px 0;border-bottom:1px solid var(--line)}.sp-gw-sec h2{font-size:19px;margin:0 0 6px}.sp-empty-line{color:var(--muted);font-size:13.5px}
@media(max-width:1024px){.sp-hero-track{grid-auto-columns:calc((100% - 32px)/2)}}@media(min-width:1025px) and (max-width:1439px){.sp-hero{max-width:1180px;margin-left:auto;margin-right:auto}}
@media(max-width:640px){.sp-hero-track{grid-auto-columns:calc(100% - 40px)}.sp-hero-arrow{display:none}.sp-hero-card{min-height:200px}.sp-article-head h1{font-size:30px}}
@media(min-width:1440px){.sp-hero-track{grid-auto-columns:calc((100% - 64px)/5);grid-auto-flow:column}}
.visually-hidden{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}@media(max-width:760px){.hero-carousel{min-height:520px}.hero-slide-inner{padding-top:150px;padding-bottom:52px}.hero-slide h1{font-size:40px}.hero-slide p{font-size:14.5px}.hero-ctrl{width:40px;height:40px;font-size:19px}.hero-prev{left:8px}.hero-next{right:8px}.rec-inner{padding:26px 18px}.rec-cta{width:100%;text-align:center}}.hero-kicker{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:12px;font-weight:800;color:var(--muted);letter-spacing:.05em;text-transform:uppercase;margin-bottom:10px}.hero-kicker .dot{opacity:.35}.cta-ghost{background:transparent;border:1px solid var(--accent);color:#fff}.cta-ghost:hover{background:var(--accent)}.take-card{margin-top:28px;border:1px solid var(--line);border-left:3px solid var(--gold);background:#101318;padding:18px 20px;border-radius:0 6px 6px 0}.take-card h3{font-size:19px;line-height:1.25;margin:6px 0}.take-card p{font-size:14px;color:var(--muted);margin:0 0 12px}.take-card .cta{margin:0}.sub-section{padding:8px 0 34px}.sub-section h2{font-size:clamp(20px,3vw,26px)}.sub-section .lead,.sub-section p.sec-note{font-size:13px;color:var(--muted);margin:0 0 14px}@media(max-width:760px){.hero-kicker{font-size:10.5px;gap:6px}.take-card{padding:15px 14px}.hero-actions .cta{min-height:44px;display:inline-flex;align-items:center}.story-grid-title{grid-template-columns:repeat(2,1fr)}@media(max-width:760px){.story-grid-title{grid-template-columns:1fr}.story-grid-title a{min-height:150px}}}`);
fs.appendFileSync(path.join(root,'assets/site.css'), `\n/* Verified metadata attribution */\n.meta-source{margin:10px 0 0;font-size:12px;line-height:1.55;color:#8b93a1}.meta-source a{color:#a9b3c2;text-decoration:underline;text-underline-offset:2px}.meta-source a:hover{color:#fff}\n`);
fs.appendFileSync(path.join(root,'assets/site.css'), `
/* ============================================================
   COLOUR & DEPTH LAYER
   Appended last so it layers over the base sheet without
   rewriting it. Adds the vertical colour identities, gradients
   and hover states across the site. Structure is untouched -
   this is presentation only.
   ============================================================ */
:root{
  --grad-brand:linear-gradient(115deg,#ff6a3d,#e94b2c 45%,#c2341c);
  --grad-gold:linear-gradient(115deg,#f7d489,#e7bb5c 50%,#c99a37);
  --grad-sports:linear-gradient(115deg,#4dffa0,#3ddc84 48%,#1fa862);
  --grad-money:linear-gradient(115deg,#ffd98a,#e7bb5c 48%,#b98f2f);
  --grad-tech:linear-gradient(115deg,#7fb0ff,#4f8ef7 48%,#2a63c9);
  --grad-ent:linear-gradient(115deg,#ff7d5c,#e94b2c 48%,#b8331b);
  --ring:0 0 0 1px rgba(255,255,255,.06);
}
/* page canvas: soft coloured light instead of flat black */
body{
  background:
    radial-gradient(1100px 520px at 12% -8%, rgba(233,75,44,.14), transparent 62%),
    radial-gradient(900px 460px at 88% 0%, rgba(79,142,247,.12), transparent 60%),
    radial-gradient(760px 420px at 50% 108%, rgba(61,220,132,.09), transparent 62%),
    var(--bg);
  background-attachment:fixed;
}
/* brand wordmark */
.brand,.logo,header .top b{letter-spacing:.02em}
.brand-grad,.footer-brand b{background:var(--grad-brand);-webkit-background-clip:text;background-clip:text;color:transparent}
/* primary action */
.cta{
  background:var(--grad-brand);border:0;color:#fff;border-radius:7px;
  box-shadow:0 6px 20px rgba(233,75,44,.28), var(--ring);
  transition:transform .18s ease, box-shadow .18s ease, filter .18s ease;
}
.cta:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(233,75,44,.4), var(--ring);filter:saturate(1.08)}
.cta:active{transform:translateY(0)}
/* every section heading gets a coloured lead-in bar */
.section-head h2,.home-section h2,.section>h2,main h2,.brand-slogan{position:relative;padding-left:15px}
.section-head h2:before,.home-section h2:before,.section>h2:before,main h2:before,.brand-slogan:before{
  content:"";position:absolute;left:0;top:.16em;bottom:.16em;width:5px;border-radius:4px;background:var(--grad-brand);
}
.article-body h2:before,.legal-prose h2:before{background:var(--grad-gold)}
body[data-nav="sports"] main h2:before,body[data-nav="sports"] .section-head h2:before{background:var(--grad-sports)}
body[data-nav="make-money"] main h2:before{background:var(--grad-money)}
body[data-nav="tech"] main h2:before{background:var(--grad-tech)}
body[data-nav="sports"] .cta{background:var(--grad-sports);box-shadow:0 6px 20px rgba(61,220,132,.28),var(--ring);color:#06210f}
body[data-nav="tech"] .cta{background:var(--grad-tech);box-shadow:0 6px 20px rgba(79,142,247,.3),var(--ring)}
body[data-nav="make-money"] .cta{background:var(--grad-money);box-shadow:0 6px 20px rgba(231,187,92,.28),var(--ring);color:#2a1e05}
.section-head a{color:var(--gold);font-weight:800;font-size:13px}
.section-head a:hover{color:#fff}
/* big page titles pick up a warm gradient */
.hero h1,.vhero h1,.article-hero h1{
  background:linear-gradient(100deg,#ffffff 30%,#ffd9c9 62%,#ffb08e);
  -webkit-background-clip:text;background-clip:text;color:transparent;
}
.vhero-sports h1{background:linear-gradient(100deg,#ffffff 30%,#c9ffe3 62%,#6affab);-webkit-background-clip:text;background-clip:text}
.vhero-tech h1{background:linear-gradient(100deg,#ffffff 30%,#cfe0ff 62%,#8fb6ff);-webkit-background-clip:text;background-clip:text}
.vhero-make-money h1{background:linear-gradient(100deg,#ffffff 30%,#ffeec4 62%,#f5cd76);-webkit-background-clip:text;background-clip:text}
/* category cards: lit top edge, brighter surface, coloured lift */
.vcat{position:relative;overflow:hidden;background:linear-gradient(160deg,#181d26,#11151b);border-color:rgba(255,255,255,.1)}
.vcat:before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:var(--grad-brand);opacity:.9}
body[data-nav="sports"] .vcat:before{background:var(--grad-sports)}
body[data-nav="make-money"] .vcat:before{background:var(--grad-money)}
body[data-nav="tech"] .vcat:before{background:var(--grad-tech)}
body[data-nav="sports"] .prose a,body[data-nav="sports"] .sp-table a{color:#7dffb9}
body[data-nav="tech"] .prose a{color:#a8c8ff}
.vcat:hover{transform:translateY(-4px);border-color:rgba(255,255,255,.22);box-shadow:0 16px 34px rgba(0,0,0,.45)}
.vcat b{font-size:15px}
/* data tables read as content, not spreadsheets */
.sp-table thead th{background:linear-gradient(180deg,rgba(255,255,255,.06),transparent);color:#cfd5db;border-bottom-color:rgba(255,255,255,.14)}
.sp-table tbody tr:hover{background:rgba(255,255,255,.035)}
.sp-table a{color:#ffcaa8}.sp-table a:hover{color:#fff}
/* panels lift off the page */
.sp-msec,.genre-panel,.rec-miss{background:linear-gradient(160deg,#161b23,#0f1216)}
.sp-rel{background:linear-gradient(160deg,#171c24,#101318);transition:transform .16s ease,border-color .16s ease}
.sp-rel:hover{transform:translateY(-2px);border-color:rgba(255,255,255,.25)}
/* cards and tiles lift with light */
.tile:hover{transform:translateY(-5px)}
.tile .poster,.editorial-card .poster{transition:box-shadow .22s ease, filter .22s ease}
.tile:hover .poster,.editorial-card:hover .poster{box-shadow:0 16px 34px rgba(0,0,0,.55);filter:saturate(1.06) contrast(1.03)}
.vcat{background:linear-gradient(150deg,#141821,#0f1216);transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease}
.vcat:hover{transform:translateY(-3px);box-shadow:0 12px 26px rgba(0,0,0,.4)}
.story-grid a{transition:background .2s ease,transform .2s ease}
.story-grid a:hover{transform:translateY(-3px)}
/* vertical identity: colour the chips and hubs properly */
.vchip{border-color:rgba(255,255,255,.09)}
.vchip:before{opacity:.3}
.vchip-sports:hover{border-color:rgba(61,220,132,.55);box-shadow:0 12px 30px rgba(61,220,132,.16)}
.vchip-make-money:hover{border-color:rgba(231,187,92,.55);box-shadow:0 12px 30px rgba(231,187,92,.16)}
.vchip-tech:hover{border-color:rgba(79,142,247,.55);box-shadow:0 12px 30px rgba(79,142,247,.16)}
.vchip-entertainment:hover{border-color:rgba(233,75,44,.55);box-shadow:0 12px 30px rgba(233,75,44,.16)}
.vhero{position:relative;overflow:hidden}
.vhero:after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;opacity:.85}
.vhero-sports:after{background:var(--grad-sports)}
.vhero-make-money:after{background:var(--grad-money)}
.vhero-tech:after{background:var(--grad-tech)}
.vhero-sports{background:radial-gradient(620px 260px at 72% -10%,rgba(61,220,132,.22),transparent 68%)}
.vhero-make-money{background:radial-gradient(620px 260px at 72% -10%,rgba(231,187,92,.22),transparent 68%)}
.vhero-tech{background:radial-gradient(620px 260px at 72% -10%,rgba(79,142,247,.24),transparent 68%)}
/* eyebrows and pills */
.eyebrow{background:var(--grad-gold);-webkit-background-clip:text;background-clip:text;color:transparent;font-weight:900}
.vhero-sports .eyebrow{background:var(--grad-sports);-webkit-background-clip:text;background-clip:text}
.vhero-tech .eyebrow{background:var(--grad-tech);-webkit-background-clip:text;background-clip:text}
.genre-chips a:hover{background:rgba(233,75,44,.14);border-color:var(--accent);color:#fff}
.stabs.active{background:var(--grad-brand);border-color:transparent;box-shadow:0 4px 14px rgba(233,75,44,.3)}
.score-pill{background:rgba(231,187,92,.1)}
.sp-pill{background:rgba(255,255,255,.05)}
/* type accents on cards */
.tile-meta b,.card-type{color:var(--muted)}
/* navigation */
.topnav a{position:relative;transition:color .16s ease}
.topnav a:after{content:"";position:absolute;left:0;right:0;bottom:-6px;height:2px;border-radius:2px;background:var(--grad-brand);transform:scaleX(0);transition:transform .18s ease}
.topnav a:hover:after,.topnav a.active:after{transform:scaleX(1)}
.top{background:linear-gradient(180deg,rgba(10,12,15,.97),rgba(10,12,15,.82));border-bottom-color:rgba(255,255,255,.08)}
/* article reading experience */
.article-body h2{position:relative;padding-left:15px}
.article-body h2:before{content:"";position:absolute;left:0;top:.22em;bottom:.22em;width:3px;border-radius:3px;background:var(--grad-gold)}
.article-hero .eyebrow{letter-spacing:.1em}
.prose a{color:#ffb199;border-bottom:1px solid rgba(255,177,153,.35)}
.prose a:hover{color:#fff;border-bottom-color:#fff}
/* panels */
.vstate{background:linear-gradient(150deg,#12161c,#0e1114)}
.vnote,.trend-note{background:linear-gradient(90deg,rgba(231,187,92,.07),transparent 70%),#101318}
.sp-result{background:linear-gradient(90deg,rgba(61,220,132,.09),transparent 62%),#101318}
.rec-inner{background:linear-gradient(135deg,#181d27,#0e1014);box-shadow:0 20px 60px rgba(0,0,0,.35)}
/* footer */
.footer{position:relative;background:linear-gradient(180deg,#0b0d11,#08090b)}
.footer:before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#e94b2c,#e7bb5c 32%,#3ddc84 64%,#4f8ef7)}
.footer-col a:hover{color:#fff}
/* mobile bar */
.mobile-nav a.active{background:linear-gradient(180deg,rgba(233,75,44,.22),transparent)}
/* Back control: it is fixed-position, so keep it clear of the breadcrumb rather
   than letting it sit on top of the first line of text. */
body .bryme-back{top:auto;bottom:78px;left:14px;opacity:.92}
body .bryme-back:hover{opacity:1}
@media(min-width:761px){body .bryme-back{bottom:24px;left:18px}}
/* ---------- editorial layout variants ----------
   One tile component, four presentations. The wrapper class decides the
   shape, so curated order, counts and ranks are never altered by layout. */
.home-section{padding:44px 0}
.section-note{font-size:13px;color:var(--muted);margin:6px 0 0;max-width:640px}
.section-head{align-items:start}
.section-head>div{min-width:0}

/* Variants must undo the base rail's horizontal-scroll grid before laying out. */
.rail-lead,.rail-wall,.rail-chart,.rail-spread{
  grid-auto-flow:row;grid-auto-columns:auto;overflow-x:visible;
  scroll-snap-type:none;padding:2px 1px 4px;
}
.rail-lead .tile,.rail-wall .tile,.rail-chart .tile,.rail-spread .tile{scroll-snap-align:none}

/* LEAD - mosaic: one feature at 2x2, the rest fill around it.
   Works with any number of items, so a curated list is never truncated. */
.rail-lead{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;overflow:visible}
.rail-lead .tile{min-width:0}
.rail-lead .tile .poster{aspect-ratio:2/3}
.rail-lead .tile:first-child{grid-column:span 2;grid-row:span 2;display:flex;flex-direction:column}
.rail-lead .tile:first-child .poster{aspect-ratio:auto;flex:1;min-height:300px}
.rail-lead .tile:first-child .poster img{width:100%;height:100%;object-fit:cover}
.rail-lead .tile:first-child h3{font-size:clamp(20px,2.2vw,27px);line-height:1.15;margin-top:12px}
.rail-lead .tile:first-child .tile-meta{font-size:13px}
.rail-lead h3{font-size:14px;line-height:1.3}
.rail-lead .tile:not(:first-child) .tile-rating{display:none}
/* WALL - dense poster grid */
.rail-wall{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:16px;overflow:visible}
.rail-wall .tile{min-width:0}
.rail-wall .tile .poster{aspect-ratio:2/3}
.rail-wall h3{font-size:13.5px;line-height:1.3}
.rail-wall .tile-rating{display:none}

/* CHART - numbered two-column list */
.rail-chart{display:grid;grid-template-columns:1fr 1fr;gap:0 28px;counter-reset:ch;overflow:visible}
.rail-chart .tile{counter-increment:ch;display:grid;grid-template-columns:40px 48px minmax(0,1fr);gap:13px;align-items:center;padding:9px 6px;border-bottom:1px solid rgba(255,255,255,.055);border-radius:8px;transition:background .16s}
.rail-chart .tile:hover{background:rgba(255,255,255,.045)}
.rail-chart .tile:before{content:counter(ch);font-size:25px;font-weight:900;text-align:center;color:transparent;-webkit-text-stroke:1.4px rgba(255,255,255,.32);font-variant-numeric:tabular-nums}
.rail-chart .tile:nth-child(-n+3):before{-webkit-text-stroke:0;background:var(--grad-brand);-webkit-background-clip:text;background-clip:text}
.rail-chart .poster{width:48px;aspect-ratio:2/3;margin:0;border-radius:5px}
.rail-chart h3{font-size:15px;line-height:1.25;margin:0}
.rail-chart .tile-meta{font-size:11.5px}
.rail-chart .tile-rating{display:none}

/* SPREAD - equal-weight features, image behind the text */
.rail-spread{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;overflow:visible}
.rail-spread .tile{position:relative;min-height:300px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.09);display:flex;flex-direction:column;justify-content:flex-end;padding:18px}
.rail-spread .tile .poster{position:absolute;inset:0;margin:0;border-radius:0;aspect-ratio:auto;z-index:-2}
.rail-spread .tile .poster img{width:100%;height:100%;object-fit:cover}
.rail-spread .tile:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(6,8,11,.985) 22%,rgba(6,8,11,.8) 52%,rgba(6,8,11,.35))}
.rail-spread h3{font-size:21px;line-height:1.16;margin:6px 0 4px}
.rail-spread .tile-meta,.rail-spread .tile-rating{position:relative}

@media(max-width:1080px){.rail-wall{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media(max-width:980px){
  .rail-lead{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rail-lead .tile:first-child .poster{min-height:210px}
  .rail-chart,.rail-spread{grid-template-columns:1fr}
}
@media(max-width:620px){.rail-wall{grid-template-columns:repeat(3,minmax(0,1fr));gap:11px}.home-section{padding:30px 0}}
/* ---------- match editorial workflow ---------- */
.sp-preview{margin:18px 0 0}
.sp-msec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:12px}
.sp-msec{background:linear-gradient(160deg,#161b23,#0f1216);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:15px 17px}
.sp-msec>b{display:block;font-size:11.5px;font-weight:900;letter-spacing:.09em;text-transform:uppercase;color:var(--gold);margin-bottom:7px}
.sp-msec p{margin:0 0 8px;font-size:14.5px;line-height:1.62;color:#d9dde1}
.sp-msec p:last-child{margin-bottom:0}
.sp-msec ul{margin:0;padding-left:18px;font-size:14px;line-height:1.6;color:#d9dde1}
/* an unconfirmed field is visibly a gap in the record, not filler */
.sp-msec-unknown{border-style:dashed;background:#0f1216}
.sp-msec-unknown>b{color:var(--muted)}
.sp-unknown{display:block;font-size:13.5px;line-height:1.6;color:var(--muted);font-style:italic}
/* the preserved pre-match preview, once the match has been played */
.sp-preview-archived{margin-top:26px;padding-top:4px;border-top:1px solid var(--line)}
.sp-archive-note{background:linear-gradient(90deg,rgba(231,187,92,.09),transparent 70%);border:1px solid rgba(231,187,92,.28);border-left:3px solid var(--gold);border-radius:0 8px 8px 0;padding:13px 16px;margin:18px 0 14px}
.sp-archive-note b{display:block;font-size:14.5px;margin-bottom:3px}
.sp-archive-note p{margin:0;font-size:13px;color:var(--muted);line-height:1.6}
.sp-preview-archived .sp-msec{opacity:.86}
.sp-postmatch{margin-top:20px}
.sp-postmatch .sp-msec>b{color:#3ddc84}
@media(max-width:760px){.sp-msec-grid{grid-template-columns:1fr}}
/* ---------- clubs directory ---------- */
.cd-jumps{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 6px}
.cd-jump{font-size:12.5px;font-weight:800;text-transform:capitalize;padding:7px 13px;border:1px solid var(--line);border-radius:20px;color:#d9dde1;background:#101318}
.cd-jump:hover{border-color:var(--sports,#3ddc84);color:#fff}
.cd-count{font-size:12px;font-weight:700;color:var(--muted);margin-left:8px}
.cd-table{font-size:13.5px}
.cd-table td{vertical-align:middle}
.cd-table tbody tr:nth-child(even){background:rgba(255,255,255,.018)}
.cd-na{color:var(--muted);font-style:italic;font-size:12.5px}
.mp-card{position:relative}
.mp-when{display:block;font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);margin-bottom:2px}
.sec-previews .vcat b{font-size:16px;line-height:1.25;margin:2px 0 4px;display:block}
body[data-nav="sports"] .mp-when{color:#3ddc84}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
`);
fs.appendFileSync(path.join(root,'assets/site.css'), `\n/* Persistent navigation control */\n.bryme-back{position:fixed;left:14px;top:74px;z-index:80;display:grid;place-items:center;width:34px;height:34px;border:1px solid rgba(255,255,255,.22);border-radius:50%;background:rgba(8,9,11,.88);backdrop-filter:blur(10px);color:#fff;font:900 21px/1 system-ui,sans-serif;padding:0;cursor:pointer;box-shadow:0 7px 22px rgba(0,0,0,.35)}.bryme-back:hover{border-color:var(--sports,#3ddc84);transform:translateX(-1px)}@media(max-width:760px){.bryme-back{left:10px;top:64px;width:32px;height:32px}}\n`);
/* ------------------------------------------------------------------ */
/* Shared markup helpers                                              */
/* ------------------------------------------------------------------ */
function image(m){
  const p = poster(m);
  if (p) return `<div class="poster"><img loading="lazy" width="480" height="360" src="${esc(p)}" alt="${esc(m.title)} poster"></div>`;
  return `<div class="poster"><div class="placeholder">${esc(m.title)}</div></div>`;
}
function card(m, opts){
  opts = opts || {};
  const typeDir = m.typeDir || 'movie';
  const label = typeDir === 'series' ? 'SERIES' : (typeDir === 'anime' ? 'ANIME' : 'MOVIE');
  const genre = m.genreLabel || m.genre || '';
  const rating = m.rating && m.rating.value != null ? `<p class="tile-rating" title="BRYME editorial score">★ ${esc(String(m.rating.value))}/10 · Editorial</p>` : '';
  const rank = opts.rank ? `<span class="rank${opts.rank <= 3 ? ' top' : ''}">${opts.rank}</span>` : '';
  return `<a class="tile" href="${url('/' + typeDir + '/' + m.slug + '/')}"><div class="poster">${rank}${poster(m) ? `<img loading="lazy" width="480" height="360" src="${esc(poster(m))}" alt="${esc(m.title)} poster">` : `<div class="placeholder">${esc(m.title)}</div>`}</div><h3>${esc(m.title)}</h3><div class="tile-meta"><span class="type-badge tb-${typeDir}">${label}</span><span>${esc(m.year || '')}</span>${genre ? `<span class="sep">·</span><span>${esc(genre)}</span>` : ''}</div>${rating}</a>`;
}
function progressiveGrid(items, initial){
  const shown = items.slice(0, initial), hidden = items.slice(initial);
  const hiddenHtml = hidden.map(m => `<div class="more-tile" hidden>${card(m)}</div>`).join('');
  const button = hidden.length ? `<button class="loadmore" type="button" data-load-more>Show more (${hidden.length} remaining)</button>` : '';
  return `<div class="grid" data-cards>${shown.map(m => card(m)).join('')}${hiddenHtml}</div>${button}`;
}
function articleRow(a){
  return `<a class="row" href="${url('/article/' + a.slug + '/')}"><div><b>${esc(a.title)}</b><span class="meta" style="font-size:12px;color:var(--muted)">${esc(a.category)} · ${esc(a.description.slice(0, 120))}</span></div></a>`;
}
function trailerSection(m){
  const tTitle = esc(m.title);
  if (!m.trailers || !m.trailers.length || !m.youtubeId) {
    return `<div class="trailer-section-inner"><div class="trailer-head"><span class="eyebrow">Trailer</span><span class="trailer-status t-none">🎬 Trailer unavailable</span></div><div class="trailer-unavailable"><b>Trailer unavailable</b><span>We couldn't find a suitable verified trailer for this title yet.</span></div></div>`;
  }
  const list = m.trailers.map(t => ({
    id: t.videoId,
    type: t.type,
    label: t.type === 'fan-made' ? 'Community trailer' : (TRAILER_LABELS[t.type] || 'Trailer'),
    channel: t.channel || '',
    videoTitle: t.videoTitle || null,
    verified: !!t.verified,
    watch: 'https://www.youtube.com/watch?v=' + t.videoId
  }));
  return `<div class="trailer-section-inner" data-trailer-box data-trailer-candidates="${esc(JSON.stringify(list))}" data-trailer-title="${tTitle}">${trailerBoxInner(m, 0)}</div>`;
}
function trailerBoxInner(m, idx){
  const t = m.trailers[idx];
  const isFan = t.type === 'fan-made';
  const dot = isFan ? '🟡' : '🟢';
  const badge = t.type === 'fan-made' ? 'Community trailer' : (TRAILER_LABELS[t.type] || 'Trailer');
  const disclaimer = isFan ? `<p class="trailer-disclaimer">This is a community-created video and is not an official trailer.</p>` : '';
  const sourceLine = t.channel ? `YouTube · via ${esc(t.channel)}` : 'YouTube';
  const verifiedNote = t.verified ? '' : `<span class="trailer-verif-note">(pending re-verification)</span>`;
  const altBtn = m.trailers.length > 1 ? `<button type="button" class="trailer-alt" data-trailer-alt>Try another trailer</button>` : '';
  return `<div class="trailer-head"><span class="eyebrow">Trailer</span><span class="trailer-status ${isFan ? 't-fan' : 't-ok'}">${dot} ${esc(badge)}</span></div>
  <div class="trailer-frame" data-trailer-id="${t.videoId}"><img loading="lazy" src="https://i.ytimg.com/vi/${t.videoId}/hqdefault.jpg" alt="${esc(m.title)} poster"><button type="button" class="trailer-play">Play trailer</button></div>
  <p class="trailer-meta">${sourceLine}${verifiedNote}</p>${disclaimer}
  <div class="trailer-error" data-trailer-error hidden><b>Trailer currently unavailable.</b><span>This video could not be played right now.</span><span class="trailer-error-actions"><a class="quiet-link" data-trailer-watch href="${esc(t.watch)}" target="_blank" rel="noopener">Watch on YouTube</a><button type="button" class="trailer-retry" data-trailer-retry>Try again</button></span></div>
  <p class="trailer-fallback">If the embedded player is unavailable, <a href="${esc(t.watch)}" target="_blank" rel="noopener">watch the trailer on YouTube</a>.</p>${altBtn}`;
}
function pageScript(){
  return `<script>window.BRYME_BASE=''<\/script><script src="${url('/assets/site-app.js')}"><\/script>`;
}
/* Search-engine ownership verification. Codes live in site.config.json so a new
   engine is one config line, never a hand-edited HTML file that the next build
   would overwrite. Empty config -> no tags emitted at all. */
const VERIFY_TAGS = [
  site.bingVerification   ? `<meta name="msvalidate.01" content="${esc(site.bingVerification)}">` : '',
  site.googleVerification ? `<meta name="google-site-verification" content="${esc(site.googleVerification)}">` : '',
  site.yandexVerification ? `<meta name="yandex-verification" content="${esc(site.yandexVerification)}">` : ''
].join('');

function layout(o){
  const socialImage = o.image ? `<meta property="og:image" content="${esc(/^https?:\/\//i.test(o.image) ? o.image : absUrl(o.image))}"><meta name="twitter:image" content="${esc(/^https?:\/\//i.test(o.image) ? o.image : absUrl(o.image))}">` : '';
  const schema = o.schema ? `<script type="application/ld+json">${JSON.stringify(o.schema).replace(/</g,'\\u003c')}<\/script>` : '';
  const active = o.activeNav || '';
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(o.title)} | ${site.name}</title><meta name="description" content="${esc(o.description)}">${VERIFY_TAGS}${o.noindex?'<meta name="robots" content="noindex,follow">':''}<link rel="canonical" href="${absUrl(o.canonical || o.path)}"><meta property="og:type" content="${esc(o.ogType || 'website')}"><meta property="og:site_name" content="${site.name}"><meta property="og:title" content="${esc(o.title)}"><meta property="og:description" content="${esc(o.description)}"><meta property="og:url" content="${absUrl(o.path)}">${socialImage}<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="${esc(o.title)}"><meta name="twitter:description" content="${esc(o.description)}"><link rel="stylesheet" href="${url('/assets/site.css')}">${schema}</head><body data-nav="${esc(o.activeNav || '')}"><header class="top"><div class="shell"><a class="brand" href="${url('/')}">BRY<b>ME</b></a><nav class="topnav"><a href="${url('/')}"${active==='home'?' class="active"':''}>Home</a><a href="${url('/entertainment/')}"${active==='entertainment'?' class="active"':''}>🎬 Entertainment</a><a href="${url('/sports/')}"${active==='sports'?' class="active"':''}>⚽ Sports</a><a href="${url('/make-money/')}"${active==='make-money'?' class="active"':''}>💰 Make Money</a><a href="${url('/tech/')}"${active==='tech'?' class="active"':''}>🤖 Tech &amp; AI</a><a class="nav-search" href="${url('/search/')}">Search</a></nav></div></header>${o.body}<nav class="mobile-nav"><a href="${url('/')}"${active==='home'?' class="active"':''}><span class="mn-ico">🏠</span>Home</a><a href="${url('/entertainment/')}"${active==='entertainment'?' class="active"':''}><span class="mn-ico">🎬</span>Entertain</a><a href="${url('/sports/')}"${active==='sports'?' class="active"':''}><span class="mn-ico">⚽</span>Sports</a><a href="${url('/make-money/')}"${active==='make-money'?' class="active"':''}><span class="mn-ico">💰</span>Money</a><a href="${url('/tech/')}"${active==='tech'?' class="active"':''}><span class="mn-ico">🤖</span>Tech</a><a href="${url('/search/')}"><span class="mn-ico">🔍</span>Search</a></nav><footer class="footer"><div class="shell"><div class="footer-grid">
  <div class="footer-brand"><a class="brand" href="${url('/')}">BRY<b>ME</b></a><p>Discover what you love. Learn what you need. Find what's next.</p></div>
  <nav class="footer-col" aria-label="Explore"><h4>Verticals</h4><a href="${url('/entertainment/')}">🎬 Entertainment</a><a href="${url('/sports/')}">⚽ Sports</a><a href="${url('/make-money/')}">💰 Make Money</a><a href="${url('/tech/')}">🤖 Tech &amp; AI</a></nav>
  <nav class="footer-col" aria-label="Explore"><h4>Entertainment</h4><a href="${url('/movies/')}">Movies</a><a href="${url('/series/')}">Series</a><a href="${url('/anime/')}">Anime</a><a href="${url('/articles/')}">Articles</a><a href="${url('/genres/')}">Genres</a></nav>
  <nav class="footer-col" aria-label="Information"><h4>Information</h4><a href="${url('/about/')}">About</a><a href="${url('/contact/')}">Contact</a><a href="${url('/editorial-policy/')}">Editorial Policy</a></nav>
  <nav class="footer-col" aria-label="Legal"><h4>Legal</h4><a href="${url('/privacy/')}">Privacy Policy</a><a href="${url('/terms/')}">Terms of Use</a><a href="${url('/disclaimer/')}">Disclaimer</a><a href="${url('/copyright/')}">Copyright / DMCA</a></nav>
</div>
<p class="footer-note">BRYME · Discover what you love. Learn what you need. Find what's next. Trailer links lead to YouTube and viewing links lead to third parties.<small>Trending Now is editorially curated by BRYME — it is not live traffic data. Popular and Editor's Picks are independent rankings. Real user analytics will replace trending once the site has enough traffic. · Build ${new Date().toISOString().slice(0, 16).replace('T', ' ')} UTC</small></div></footer>${pageScript()}</body></html>`;
}

/* ------------------------------------------------------------------ */
/* Pages                                                              */
/* ------------------------------------------------------------------ */
function write(dir, content){ const out = path.join(root, dir, 'index.html'); fs.mkdirSync(path.dirname(out), {recursive:true}); fs.writeFileSync(out, content); }
/* ================================================================
   EDITORIAL LAYOUT COMPONENTS
   The homepage was nine identical card rails stacked on top of each
   other, which reads as a template rather than a publication. These
   give each section its own shape: a lead story with supporting grid,
   a ranked chart, a poster wall, and a magazine spread. Same data,
   same links - different hierarchy.
   ================================================================ */
function clip(text, n){
  const t = String(text || '').trim();
  if (t.length <= n) return t;
  const cut = t.slice(0, n);
  const sp = cut.lastIndexOf(' ');
  return (sp > n * 0.6 ? cut.slice(0, sp) : cut).replace(/[,;:.\s]+$/, '') + '…';
}
function sectionHead(title, emoji, moreUrl, note, eyebrow){
  return `<div class="section-head"><div>${eyebrow ? `<div class="eyebrow">${esc(eyebrow)}</div>` : ''}<h2>${emoji ? emoji + ' ' : ''}${esc(title)}</h2>${note ? `<p class="section-note">${esc(note)}</p>` : ''}</div>${moreUrl ? `<a href="${url(moreUrl)}">View all</a>` : ''}</div>`;
}
/* One dominant story plus a supporting column - the standard editorial lead. */
function leadSection(title, emoji, items, moreUrl, note, eyebrow){
  if (!items || !items.length) return '';
  const [lead, ...rest] = items;
  const side = rest.slice(0, 4);
  const typeDir = m => m.typeDir || 'movie';
  const label = m => typeDir(m) === 'series' ? 'SERIES' : (typeDir(m) === 'anime' ? 'ANIME' : 'MOVIE');
  const art = m => poster(m);
  return `<section class="home-section lead-section"><div class="shell">${sectionHead(title, emoji, moreUrl, note, eyebrow)}
    <div class="lead-grid">
      <a class="lead-main" href="${url('/' + typeDir(lead) + '/' + lead.slug + '/')}">
        <div class="lead-art"><img src="${esc(art(lead))}" alt="${esc(lead.title)}" loading="lazy" width="760" height="428"></div>
        <div class="lead-copy"><span class="lead-tag">${label(lead)}${lead.year ? ' · ' + lead.year : ''}</span><h3>${esc(lead.title)}</h3>${lead.description ? `<p>${esc(clip(lead.description, 165))}</p>` : ''}${lead.rating && lead.rating.value != null ? `<span class="lead-score">★ ${esc(String(lead.rating.value))}/10 · Editorial</span>` : ''}</div>
      </a>
      <div class="lead-side">${side.map(m => `<a class="lead-item" href="${url('/' + typeDir(m) + '/' + m.slug + '/')}">
        <img src="${esc(art(m))}" alt="${esc(m.title)}" loading="lazy" width="112" height="64">
        <div><span>${label(m)}${m.year ? ' · ' + m.year : ''}</span><b>${esc(m.title)}</b></div></a>`).join('')}</div>
    </div></div></section>`;
}
/* A ranked chart - big numerals, compact rows, reads as a list not a carousel. */
function chartSection(title, emoji, items, moreUrl, note, eyebrow){
  if (!items || !items.length) return '';
  const rows = items.slice(0, 10);
  const typeDir = m => m.typeDir || 'movie';
  return `<section class="home-section chart-section"><div class="shell">${sectionHead(title, emoji, moreUrl, note, eyebrow)}
    <ol class="chart">${rows.map((m, i) => `<li><a href="${url('/' + typeDir(m) + '/' + m.slug + '/')}">
      <span class="chart-n">${i + 1}</span>
      <img src="${esc(poster(m))}" alt="${esc(m.title)}" loading="lazy" width="46" height="66">
      <span class="chart-t"><b>${esc(m.title)}</b><i>${(typeDir(m) === 'series' ? 'Series' : typeDir(m) === 'anime' ? 'Anime' : 'Movie')}${m.year ? ' · ' + m.year : ''}${m.genreLabel || m.genre ? ' · ' + esc(m.genreLabel || m.genre) : ''}</i></span>
      ${m.rating && m.rating.value != null ? `<span class="chart-s">★ ${esc(String(m.rating.value))}</span>` : ''}
    </a></li>`).join('')}</ol></div></section>`;
}
/* A dense poster wall - browsing, not reading. */
function wallSection(title, emoji, items, moreUrl, note, eyebrow, limit){
  if (!items || !items.length) return '';
  const typeDir = m => m.typeDir || 'movie';
  return `<section class="home-section wall-section"><div class="shell">${sectionHead(title, emoji, moreUrl, note, eyebrow)}
    <div class="wall">${items.slice(0, limit || 12).map(m => `<a class="wall-item" href="${url('/' + typeDir(m) + '/' + m.slug + '/')}">
      <img src="${esc(poster(m))}" alt="${esc(m.title)}" loading="lazy" width="200" height="286">
      <span class="wall-cap"><b>${esc(m.title)}</b><i>${m.year || ''}</i></span></a>`).join('')}</div></div></section>`;
}
/* Magazine spread - equal-weight feature cards with the image behind the text. */
function spreadSection(title, emoji, items, moreUrl, note, eyebrow){
  if (!items || !items.length) return '';
  const typeDir = m => m.typeDir || 'movie';
  return `<section class="home-section spread-section"><div class="shell">${sectionHead(title, emoji, moreUrl, note, eyebrow)}
    <div class="spread">${items.slice(0, 3).map(m => `<a class="spread-card" href="${url('/' + typeDir(m) + '/' + m.slug + '/')}" style="--sp-img:url('${esc(poster(m))}')">
      <span class="spread-tag">${typeDir(m) === 'series' ? 'SERIES' : typeDir(m) === 'anime' ? 'ANIME' : 'MOVIE'}${m.year ? ' · ' + m.year : ''}</span>
      <b>${esc(m.title)}</b>${m.description ? `<p>${esc(clip(m.description, 118))}</p>` : ''}</a>`).join('')}</div></div></section>`;
}

function railSection(title, emoji, items, moreUrl, note, opts){
  /* opts.variant changes only the wrapper class. Every section keeps the same
     <a class="tile"> markup and the full configured item list, so curated order,
     per-type ranks and counts stay intact - the layout differences are CSS. */
  const v = (opts && opts.variant) ? String(opts.variant) : '';
  const secClass = v ? ' sec-' + v : '';
  const variant = v ? ' rail-' + v : '';
  const eyebrow = (opts && opts.eyebrow) ? `<div class="eyebrow">${esc(opts.eyebrow)}</div>` : '';
  return `<section class="home-section${secClass}"><div class="shell"><div class="section-head"><div>${eyebrow}<h2>${emoji ? emoji + ' ' : ''}${esc(title)}</h2>${note ? `<p class="section-note">${esc(note)}</p>` : ''}</div>${moreUrl ? `<a href="${url(moreUrl)}">View all</a>` : ''}</div><div class="rail${variant}">${items.map((m,i) => card(m, {rank: opts && opts.ranked ? (opts.rankKey ? (m[opts.rankKey] || i + 1) : i + 1) : null})).join('')}</div></div></section>`;
}

/* ================================================================
   BRYME VERTICALS — Sports, Make Money, Tech & AI,
   plus the Entertainment hub. Foundation pages only: real structure,
   unique SEO, honest placeholder states. No fabricated content.
   ================================================================ */
const VERTICALS = [
  {
    dir: 'sports', emoji: '⚽', name: 'BRYME Sports', short: 'Sports', active: 'sports', accent: '#3ddc84',
    tagline: 'Football, covered properly: Premier League, Champions League, La Liga, Serie A, Bundesliga and Ligue 1.',
    desc: 'BRYME Sports is football. The Premier League, Champions League, La Liga, Serie A, Bundesliga, Ligue 1 and international football — with club histories, rivalry explainers, records, player profiles, match previews and reports. We cover one sport properly rather than several thinly.',
    note: 'Current reporting (previews, results, transfers) is always researched before publication. No result, transfer, injury, fixture or statistic is ever invented.',
    categories: [
      { slug: 'football', name: 'Football', desc: 'Premier League, Champions League, La Liga, Serie A, Bundesliga, Ligue 1, FPL and the global game.' },
      /* These six hubs existed as orphaned static pages that no build step regenerated: they were
         live, stuck on the placeholder notice and missing from the sitemap. Declaring them here puts
         them back under the build, so they list their articles and de-index themselves while empty. */
      { slug: 'champions-league', name: 'Champions League', desc: 'Europe\u2019s premier club competition: format, qualification, the knockout bracket and the nights that define it.' },
      { slug: 'records', name: 'Records', desc: 'Titles, streaks, milestones and the numbers behind the achievements.' },
      { slug: 'clubs', name: 'Clubs', desc: 'Club histories, identities, rivalries and how they are run.' },
      { slug: 'history', name: 'Football History', desc: 'Eras, turning points and the matches that changed the sport.' },
      { slug: 'international', name: 'International', desc: 'World Cup, continental championships and national-team football.' },
      { slug: 'players', name: 'Players', desc: 'Careers, playing styles and the athletes shaping the game.' }
    ]
  },
  {
    dir: 'make-money', emoji: '💰', name: 'BRYME Make Money', short: 'Make Money', active: 'make-money', accent: '#e7bb5c',
    tagline: 'Practical, honest guides to legitimate online income.',
    desc: 'BRYME Make Money covers practical and legitimate online-income topics: freelancing, remote work, AI-assisted work, microtasks, content creation, affiliate marketing, website monetization, digital products and online businesses.',
    note: 'No fake income claims. No guaranteed earnings. No fabricated statistics. Every guide distinguishes possible earnings, typical/observed earnings where reliable evidence exists, requirements, risks, fees, country availability and payment methods. Earnings always vary.',
    categories: [
      { slug: 'freelancing', name: 'Freelancing', desc: 'Starting and growing a freelance career.' },
      { slug: 'remote-work', name: 'Remote Work', desc: 'Finding and succeeding in remote jobs.' },
      { slug: 'ai-assisted-work', name: 'AI-Assisted Work', desc: 'Using AI tools to work faster and earn.' },
      { slug: 'online-services', name: 'Online Services', desc: 'Selling services online — from design to writing to support.' },
      { slug: 'microtasks', name: 'Microtasks', desc: 'Small tasks, realistic expectations, honest reviews.' },
      { slug: 'content-creation', name: 'Content Creation', desc: 'YouTube, TikTok, blogging and creator income.' },
      { slug: 'affiliate-marketing', name: 'Affiliate Marketing', desc: 'How affiliate marketing actually works.' },
      { slug: 'website-monetization', name: 'Website Monetization', desc: 'Turning a website into an income source.' },
      { slug: 'digital-products', name: 'Digital Products', desc: 'Creating and selling digital products.' },
      { slug: 'online-businesses', name: 'Online Businesses', desc: 'Small online business models explained.' },
      { slug: 'income-skills', name: 'Income Skills', desc: 'Skills that can generate income and how to learn them.' },
      { slug: 'platform-reviews', name: 'Platform Reviews', desc: 'Earning platforms reviewed honestly, with risks and fees.' },
      { slug: 'beginner-guides', name: 'Beginner Guides', desc: 'Start here if you are new to online income.' }
    ]
  },
  {
    dir: 'tech', emoji: '🤖', name: 'BRYME Tech & AI', short: 'Tech & AI', active: 'tech', accent: '#4f8ef7',
    tagline: 'Practical technology: AI tools, apps, automation and useful websites.',
    desc: 'BRYME Tech & AI focuses on practical technology — what a tool can actually do for you — rather than generic tech news. AI tools and tutorials, ChatGPT assistants, Android apps, productivity, automation, beginner coding and website building.',
    note: 'Content is written for normal users in plain language. Highly technical topics are researched before publication; we do not pretend to be experts without doing the work.',
    categories: [
      { slug: 'ai-tools', name: 'AI Tools', desc: 'The most useful AI tools and what they actually do.' },
      { slug: 'ai-tutorials', name: 'AI Tutorials', desc: 'Step-by-step guides to getting real value from AI.' },
      { slug: 'ai-assistants', name: 'AI Assistants', desc: 'ChatGPT and AI assistants for everyday tasks.' },
      { slug: 'ai-image-video', name: 'AI Image & Video', desc: 'Generating images and video with AI.' },
      { slug: 'ai-coding', name: 'AI Coding', desc: 'Using AI to learn to code and code faster.' },
      { slug: 'useful-websites', name: 'Useful Websites', desc: 'Websites worth knowing about.' },
      { slug: 'android-apps', name: 'Android Apps', desc: 'Apps that make your phone more useful.' },
      { slug: 'productivity', name: 'Productivity', desc: 'Tools and habits that get things done.' },
      { slug: 'automation', name: 'Automation', desc: 'Letting software do the repetitive work.' },
      { slug: 'beginner-coding', name: 'Beginner Coding', desc: 'Learning to code from zero.' },
      { slug: 'developer-tools', name: 'Developer Tools', desc: 'Tools for people building software.' },
      { slug: 'website-building', name: 'Website Building', desc: 'Building websites without a degree in it.' },
      { slug: 'hosting', name: 'Hosting & Deployment', desc: 'Getting your website online.' },
      { slug: 'internet-tools', name: 'Internet Tools', desc: 'Everyday internet utilities explained.' },
      { slug: 'cybersecurity', name: 'Cybersecurity Awareness', desc: 'Staying safe online without the scare tactics.' },
      { slug: 'new-tech', name: 'New Technology', desc: 'New technology worth knowing about.' }
    ]
  }
];
searchIndex.verticals = [{ type:'entertainment', title:'BRYME Entertainment', slug:'entertainment', description:'Movies, TV series and anime with verified trailers and editorial articles.' }].concat(
  VERTICALS.flatMap(v => [{ type: v.dir, title: v.name, slug: v.dir, description: v.desc }].concat((v.categories || []).map(c => ({ type: v.dir, title: c.name, slug: v.dir + '/' + c.slug, description: c.desc }))))
);
fs.writeFileSync(path.join(root, 'data/search-index.json'), JSON.stringify(searchIndex)+'\n');
/* ================================================================
   VERTICAL ARTICLES — Make Money and Sports editorial.
   Published articles are rendered as real pages and listed on their
   category hub. A category with no published article keeps its honest
   placeholder but is marked noindex and kept out of the sitemap, so the
   site never submits empty pages to search engines. As soon as an
   article is published the hub becomes indexable again automatically.
   ================================================================ */
function loadVerticalArticles(file, key) {
  const f = path.join(root, 'content', file);
  if (!fs.existsSync(f)) return [];
  try {
    const raw = JSON.parse(fs.readFileSync(f, 'utf8'));
    const list = Array.isArray(raw) ? raw : (raw[key] || []);
    return list.filter(a => a && a.status === 'published');
  } catch (e) { return []; }
}
/* ================================================================
   AUTHORS — a byline is only a trust signal if it resolves to a real person.
   Bio content comes from content/authors.json and is supplied by the author;
   nothing here is generated or embellished. A byline with no matching record
   simply renders as plain text rather than linking nowhere.
   ================================================================ */
const AUTHORS = (() => {
  const f = path.join(root, 'content', 'authors.json');
  if (!fs.existsSync(f)) return new Map();
  try { return new Map(JSON.parse(fs.readFileSync(f, 'utf8')).map(a => [a.name, a])); }
  catch (e) { return new Map(); }
})();
const authorPath = a => '/author/' + a.slug + '/';
const authorLink = name => {
  const a = AUTHORS.get(name);
  return a ? `<a href="${url(authorPath(a))}" rel="author">${esc(name)}</a>` : esc(name);
};

/* Every vertical reads content/<dir>-articles.json, so adding a vertical needs no new code. */
const VERTICAL_ARTICLES = {};
const verticalArticleIndex = {};
/* article → category slug (explicit categorySlug wins; otherwise slugify the label) */
const articleCatSlug = a => slugify(a.categorySlug || a.category || '');
VERTICALS.forEach(v => {
  const list = loadVerticalArticles(v.dir + '-articles.json', 'articles');
  VERTICAL_ARTICLES[v.dir] = list;
  const idx = new Map();
  list.forEach(a => {
    const key = articleCatSlug(a);
    if (!idx.has(key)) idx.set(key, []);
    idx.get(key).push(a);
  });
  verticalArticleIndex[v.dir] = idx;
});
const moneyArticles = VERTICAL_ARTICLES['make-money'] || [];
const sportsArticlesPub = VERTICAL_ARTICLES.sports || [];
const articlePathFor = (dir, a) => '/' + dir + '/' + a.slug + '/';
/* An article slug must never collide with a category/section slug at the same level. */
VERTICALS.forEach(v => {
  const reserved = new Set(['articles'].concat((v.categories || []).map(c => c.slug)));
  (v.dir === 'sports' ? sportsArticlesPub : v.dir === 'make-money' ? moneyArticles : []).forEach(a => {
    if (reserved.has(a.slug)) throw new Error(`Article slug "${a.slug}" collides with a ${v.dir} section slug. Rename the article slug in content/${v.dir === 'sports' ? 'sports' : 'make-money'}-articles.json.`);
  });
});
const articleCard = (dir, a) => `<a class="vcat" href="${url(articlePathFor(dir, a))}"><b>${esc(a.title)}</b><span>${esc(a.excerpt || '')}</span></a>`;

const EMPTY_HUB_PATHS = new Set();
const verticalChip = v => `<a class="vchip vchip-${v.dir}" href="${url('/' + v.dir + '/')}"><span class="vchip-emoji">${v.emoji}</span><span class="vchip-name">${esc(v.name)}</span><span class="vchip-tag">${esc(v.tagline)}</span></a>`;
function verticalPage(v, category){
  const catPath = category ? '/' + v.dir + '/' + category.slug + '/' : '/' + v.dir + '/';
  const crumbs = [{name:'Home', path:'/'}, {name:v.name, path:'/' + v.dir + '/'}];
  if (category) crumbs.push({name:category.name, path:catPath});
  const catGrid = (v.categories || []).map(c => `<a class="vcat" href="${url('/' + v.dir + '/' + c.slug + '/')}"><b>${esc(c.name)}</b><span>${esc(c.desc)}</span></a>`).join('') + (v.dir === 'make-money' ? `<a class="vcat" href="${url('/make-money/beginners-guide-to-making-money-online/')}"><b>Beginner’s Guide to Making Money Online</b><span>An honest, skill-first guide to avoiding shortcuts and building value.</span></a>` : '');
  const sportsEditorial = (() => { const f = path.join(root, 'content', 'sports-articles.json'); if (!fs.existsSync(f)) return []; try { return (JSON.parse(fs.readFileSync(f, 'utf8')).articles || []).filter(a => a.status === 'published'); } catch (_) { return []; } })();
  const sportsStoriesBlock = (v.dir === 'sports' && !category) ? `<section class="section"><div class="section-head"><h2>BRYME Sports Stories</h2><a href="${url('/sports/articles/')}">All stories</a></div>${sportsEditorial.length ? `<div class="vcat-grid">${sportsEditorial.filter(a => (a.labels || []).some(x => ['featured','trending','editor-pick'].includes(x))).slice(0,6).map(a => `<a class="vcat" href="${url('/sports/articles/' + a.slug + '/')}"><b>${esc(a.title)}</b><span>${esc(a.category)} · ${esc((a.labels || []).join(' · '))}</span></a>`).join('')}</div>` : `<div class="vstate"><b>Stories are being prepared</b><p>Drafts are researched and reviewed before publication. Published BRYME Sports stories will appear here.</p><a class="quiet-link" href="${url('/sports/articles/')}">Visit the Sports editorial desk</a></div>`}</section>` : '';
  const sportsFeature = (v.dir === 'sports' && category && category.slug === 'football') ? `<section class="sp-hero" aria-label="Featured BRYME Sports stories"><div class="sp-hero-track"><a class="sp-hero-card sp-hero-first" href="${url('/sports/premier-league/')}" style="--card-img:url('/assets/img/sports/hero-premier-league.jpg')"><span class="sp-hero-tag">Welcome to the Premier League</span><h3>The 2026/27 season starts here</h3><p>Fixtures, clubs, match pages and the stories that will define the campaign.</p><span class="sp-hero-go">Explore the season →</span></a><a class="sp-hero-card" href="${url('/sports/fpl/')}" style="--card-img:url('/assets/img/sports/hero-fpl.jpg')"><span class="sp-hero-tag">Fantasy Premier League</span><h3>Top FPL picks for the new season</h3><p>Start with the fixtures, the key decisions and the players worth watching.</p><span class="sp-hero-go">Build your FPL view →</span></a><a class="sp-hero-card" href="${url('/sports/managers-2026-27/')}" style="--card-img:url('/assets/img/sports/hero-man-city-manager.jpg')"><span class="sp-hero-tag">Manchester City</span><h3>Enzo Maresca: a new chapter at City</h3><p>Follow the manager changes and the early storylines around the Premier League.</p><span class="sp-hero-go">See managers in &amp; out →</span></a></div></section>` : '';
  /* ---- Clubs directory: the Clubs hub IS the reference page ----
     Built from content/club-history/*.json, where every club record already carries an
     official source. Capacities come from the fixture venue data where it exists.
     Honours totals are deliberately absent - the existing source policy withholds them
     until each club is reconciled against official honours lists, and inventing them
     here to fill a column would be exactly the wrong trade. */
  const clubsDirectory = (() => {
    if (!(v.dir === 'sports' && category && category.slug === 'clubs')) return '';
    const dir = path.join(root, 'content', 'club-history');
    if (!fs.existsSync(dir)) return '';
    const order = ['premier-league','la-liga','serie-a','bundesliga','ligue-1','eredivisie'];
    const capsFor = (lgSlug) => {
      const fname = lgSlug === 'premier-league' ? 'fixtures.json' : `fixtures-${lgSlug}.json`;
      const fp = path.join(root, 'content', fname);
      if (!fs.existsSync(fp)) return {};
      try { return (JSON.parse(fs.readFileSync(fp, 'utf8')).venues) || {}; } catch (e) { return {}; }
    };
    let total = 0, checked = null;
    const tables = order.map(lgSlug => {
      const fp = path.join(dir, lgSlug + '.json');
      if (!fs.existsSync(fp)) return '';
      let D; try { D = JSON.parse(fs.readFileSync(fp, 'utf8')); } catch (e) { return ''; }
      const clubs = (D.clubs || []).slice().sort((a, b) => String(a.name).localeCompare(String(b.name)));
      if (!clubs.length) return '';
      total += clubs.length;
      checked = checked || D.lastChecked;
      const caps = capsFor(lgSlug);
      const anyCap = clubs.some(c => caps[c.slug] && caps[c.slug].capacity);
      return `<h3 class="sp-dir" id="${esc(lgSlug)}">${esc(D.league || lgSlug)} <span class="cd-count">${clubs.length} clubs</span></h3>
      <div class="sp-table-wrap"><table class="sp-table cd-table"><thead><tr><th>Club</th><th>Founded</th><th>City</th><th>Stadium</th>${anyCap ? '<th>Capacity</th>' : ''}<th>Source</th></tr></thead><tbody>
      ${clubs.map(c => {
        const cap = caps[c.slug] && caps[c.slug].capacity;
        return `<tr><td><b>${esc(c.name)}</b></td><td>${esc(c.founded || '—')}</td><td>${esc(c.city || '—')}</td><td>${esc(c.stadium || '—')}</td>${anyCap ? `<td>${cap ? esc(Number(cap).toLocaleString('en-GB')) : '<span class="cd-na">not recorded</span>'}</td>` : ''}<td>${c.source ? `<a href="${esc(c.source)}" rel="nofollow noopener">official</a>` : '<span class="cd-na">—</span>'}</td></tr>`;
      }).join('')}
      </tbody></table></div>`;
    }).filter(Boolean).join('');
    const jump = order.filter(o => fs.existsSync(path.join(dir, o + '.json')))
      .map(o => `<a class="cd-jump" href="#${o}">${esc(o.replace(/-/g, ' '))}</a>`).join('');
    return `<section class="section">
      <div class="vnote">Founding year, home city and stadium for <b>${total} clubs</b> across six European leagues. Every row is backed by an official club source, linked in the last column. Last reconciled ${esc(checked || 'recently')}.</div>
      <div class="cd-jumps">${jump}</div>
      ${tables}
      <div class="sp-truth"><b>Why there is no honours column.</b><p>BRYME does not publish major-honours totals until each club has been reconciled against official club and competition honours lists. Trophy counts differ between sources depending on whether defunct competitions, shared titles and regional championships are included, and a table that quietly picks one interpretation is worse than no table. The column will appear when the reconciliation is done, not before.</p></div>
    </section>`;
  })();
  const footballHub = `<section class="section"><div class="vnote">Football is BRYME’s first fully built sports hub. Pick a competition or follow fixtures, FPL, transfers and the game’s biggest stories.</div><h2 style="margin:26px 0 14px">Football competitions</h2><div class="vcat-grid"><a class="vcat" href="${url('/sports/premier-league/')}"><b>Premier League</b><span>England’s top flight: fixtures, clubs, transfers and FPL.</span></a><a class="vcat" href="${url('/sports/champions-league/')}"><b>Champions League</b><span>Europe’s biggest club competition.</span></a><a class="vcat" href="${url('/sports/la-liga/')}"><b>La Liga</b><span>Spanish football: Real Madrid, Barcelona and beyond.</span></a><a class="vcat" href="${url('/sports/serie-a/')}"><b>Serie A</b><span>Italian football and its storied clubs.</span></a><a class="vcat" href="${url('/sports/bundesliga/')}"><b>Bundesliga</b><span>German football and its fan culture.</span></a><a class="vcat" href="${url('/sports/ligue-1/')}"><b>Ligue 1</b><span>French football, fixtures and clubs.</span></a><a class="vcat" href="${url('/sports/international/')}"><b>International football</b><span>National teams, tournaments and qualifiers.</span></a></div><h2 style="margin:30px 0 14px">Follow the game</h2><div class="vcat-grid"><a class="vcat" href="${url('/sports/fpl/')}"><b>Fantasy Premier League</b><span>Picks, captains and fixture-led decisions.</span></a><a class="vcat" href="${url('/sports/transfers/')}"><b>Transfers</b><span>Verified transfer coverage and market context.</span></a><a class="vcat" href="${url('/sports/players/')}"><b>Players</b><span>Profiles, careers and stories.</span></a><a class="vcat" href="${url('/sports/clubs/')}"><b>Clubs</b><span>Histories, identities and fan culture.</span></a><a class="vcat" href="${url('/sports/history/')}"><b>History</b><span>Historic moments and great eras.</span></a><a class="vcat" href="${url('/sports/records/')}"><b>Records</b><span>Goals, titles, appearances and numbers.</span></a></div></section>`;
  const sportsTeaserBlock = (v.dir === 'sports' && !category) ? `<section class="section sports-teaser"><div class="section-head"><h2>Premier League 2026/27</h2></div><div class="trailer-frame" style="max-width:100%"><iframe width="100%" height="500" src="https://www.youtube.com/embed/nx8rgJrmSFY" title="Premier League 2026/27 — The Wait Is Over" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen><\/iframe></div></section>` : '';
  const fixturesBlock = (v.dir === 'sports' && !category) ? '<section class="section"><div class="section-head"><h2>Fixtures &amp; Results 2026/27</h2></div><div class="vcat-grid">' + LEAGUE_FIX.map(lg => { const F = loadLeagueFixtures(lg.slug); const total = (F.matchweeks || []).reduce((n, w) => n + w.matches.length, 0); return '<a class="vcat" href="' + url('/sports/' + lg.slug + '/fixtures/') + '"><b>' + esc(lg.name) + '</b><span>All ' + total + ' fixtures — dates, kickoffs &amp; match pages</span></a>'; }).join('') + '<a class="vcat" href="' + url('/sports/managers-2026-27/') + '"><b>Managers</b><span>Managers In &amp; Out — 2026/27</span></a></div></section>' : '';
  const defaultHero = `<section class="hero vhero vhero-${v.dir}" data-vertical="${v.dir}"><div class="eyebrow">${v.emoji} ${category ? esc(v.name) + ' · ' + esc(category.name) : esc(v.name)}</div><h1>${esc(category ? category.name : v.name)}</h1><p class="lead">${esc(category ? category.desc : v.tagline)}</p></section>`;
  const pageHero = defaultHero + sportsFeature;
  const catArticles = category ? ((verticalArticleIndex[v.dir] && verticalArticleIndex[v.dir].get(category.slug)) || []) : [];
  const catArticleBlock = catArticles.length
    ? `<div class="vcat-grid">${catArticles.map(a => articleCard(v.dir, a)).join('')}</div>`
    : '';
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / ${category ? `<a href="${url('/' + v.dir + '/')}">${esc(v.name)}</a> / ${esc(category.name)}` : esc(v.name)}</div>${pageHero}<section class="section">${category ? (v.dir === 'sports' && category.slug === 'football' ? (footballHub + catArticleBlock) : (clubsDirectory ? (clubsDirectory + catArticleBlock) : (catArticles.length ? catArticleBlock : `<div class="vstate"><b>${esc(category.name)} — foundation ready</b><p>This section is being built. Articles will appear here as they are researched and published.</p></div>`))) : `<p class="lead" style="margin-bottom:18px">${esc(v.desc)}</p><div class="vnote">${esc(v.note)}</div><h2 style="margin:26px 0 14px">Explore ${esc(v.short)}</h2><div class="vcat-grid">${catGrid}</div>`}</section>${(v.dir === 'sports' && !category) ? livePreviewBlock(10) : ''}${sportsTeaserBlock}${fixturesBlock}${sportsStoriesBlock}<section class="section"><div class="section-head"><h2>Explore BRYME</h2></div><div class="vchips">${VERTICALS.map(verticalChip).join('')}</div></section></main>`;
  const emptyHub = !!category && !catArticles.length && !clubsDirectory && !(v.dir === 'sports' && category.slug === 'football');
  if (emptyHub) EMPTY_HUB_PATHS.add(catPath);
  write(v.dir + (category ? '/' + category.slug : ''), layout({
    title: category ? `${category.name} – ${v.short}` : `${v.name} – ${v.tagline}`,
    description: category ? `${category.desc} ${v.name} — foundation section on BRYME.` : `${v.desc} ${v.note}`,
    noindex: emptyHub,
    path: catPath,
    activeNav: v.active,
    schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: category ? category.name : v.name, description: (category ? category.desc : v.desc), url: absUrl(catPath) }, breadcrumbs(crumbs)],
    body: body
  }));
}
/* ================================================================
   WEEKLY EDITORIAL WORKFLOW FOR MATCH PAGES
   ----------------------------------------------------------------
   The fixture database stays complete: every scheduled match keeps a
   page at its permanent URL. What changes is whether that page is an
   INDEXABLE EDITORIAL PAGE or a schedule entry.

   A fixture is written up roughly 3-5 days before kickoff. Adding an
   entry to content/match-editorial.json is what promotes it: the page
   gains the full preview, becomes indexable, and enters the sitemap
   with a lastmod. Without an entry it stays noindex and out of the
   sitemap, so thousands of unplayed fixtures are never submitted.

   After the match the SAME URL is updated - never a second URL. The
   result and post-match analysis go on top, and the pre-match preview
   is preserved below under its own heading so readers can see what
   BRYME expected and what actually happened.

   Nothing here invents team news. A field that is absent renders as an
   explicit "not confirmed" state.
   ================================================================ */
const EDITORIAL_WINDOW_DAYS = 5;   /* start writing this many days out */
const EDITORIAL_WINDOW_MIN  = 3;   /* page should be live by this many days out */
const BUILD_DAY = (process.env.BRYME_TODAY || new Date().toISOString().slice(0, 10));
const EDITORIAL = (() => {
  const f = path.join(root, 'content', 'match-editorial.json');
  if (!fs.existsSync(f)) return {};
  try { return JSON.parse(fs.readFileSync(f, 'utf8')); } catch (e) { return {}; }
})();
const PAGE_LASTMOD = new Map();     /* path -> YYYY-MM-DD for sitemap <lastmod> */
const EDITORIAL_FIELDS = ['overview','recentForm','headToHead','lastFiveMeetings','homeAwayForm',
  'keyPlayers','injuries','suspensions','expectedLineups','tacticalMatchup','historicalContext',
  'underdog','outlook','scorePrediction'];
function daysUntil(dateStr){
  if (!dateStr) return null;
  const a = Date.parse(dateStr + 'T00:00:00Z'), b = Date.parse(BUILD_DAY + 'T00:00:00Z');
  if (isNaN(a) || isNaN(b)) return null;
  return Math.round((a - b) / 86400000);
}
/* Sitemap <lastmod> and schema.org dates must be ISO 8601. Anything that is not a clean
   YYYY-MM-DD is dropped rather than emitted in a format crawlers will reject. */
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;
const BAD_DATES = [];
function isoDate(v, where){
  if (!v) return null;
  const t = String(v).trim();
  if (ISO_DATE.test(t)) return t;
  BAD_DATES.push(`${where}: "${t}" is not YYYY-MM-DD`);
  return null;
}
function editorialFor(leagueSlug, matchSlug){
  const e = ((EDITORIAL[leagueSlug] || {})[matchSlug]);
  if (!e) return null;
  /* "meaningful content" gate: a stub with only dates must not go into the sitemap */
  const filled = EDITORIAL_FIELDS.filter(k => {
    const v = e[k];
    return Array.isArray(v) ? v.length > 0 : (typeof v === 'string' && v.trim().length > 12);
  });
  if (filled.length < 3) return null;
  return e;
}
const UNKNOWN = txt => `<span class="sp-unknown">${esc(txt)}</span>`;
function edRow(label, value, unknownNote){
  const has = Array.isArray(value) ? value.length : (typeof value === 'string' && value.trim());
  const body = !has ? UNKNOWN(unknownNote || 'Not confirmed at the time of writing.')
    : Array.isArray(value) ? `<ul>${value.map(x => `<li>${esc(x)}</li>`).join('')}</ul>`
    : String(value).split(/\n{2,}/).map(t => `<p>${esc(t.trim())}</p>`).join('');
  return `<div class="sp-msec${has ? '' : ' sp-msec-unknown'}"><b>${esc(label)}</b>${body}</div>`;
}
function previewBlock(e, opts){
  const past = !!(opts && opts.past);
  return `<section class="sp-preview${past ? ' sp-preview-archived' : ''}">
    ${past ? `<div class="sp-archive-note"><b>What BRYME said before kickoff</b><p>This preview was published on ${esc(e.publishedAt || 'an earlier date')} and is preserved unchanged. It is what we expected, not what happened.</p></div>` : ''}
    <div class="sp-msec-grid">
      ${edRow('Match overview', e.overview)}
      ${edRow('Recent form', e.recentForm)}
      ${edRow('Head-to-head record', e.headToHead)}
      ${edRow('Last five meetings', e.lastFiveMeetings)}
      ${edRow('Home & away form', e.homeAwayForm)}
      ${edRow('Key players', e.keyPlayers)}
      ${edRow('Injuries', e.injuries, 'No injury information confirmed by the clubs at the time of writing. BRYME does not publish unverified team news.')}
      ${edRow('Suspensions', e.suspensions, 'No suspensions confirmed at the time of writing.')}
      ${edRow('Expected lineups', e.expectedLineups, 'No lineup has been announced. Expected XIs are not published here as speculation.')}
      ${edRow('Tactical matchup', e.tacticalMatchup)}
      ${edRow('Historical context', e.historicalContext)}
      ${edRow('The case for the underdog', e.underdog)}
      ${edRow('BRYME editorial outlook', e.outlook)}
      ${edRow('BRYME editorial score prediction', e.scorePrediction)}
    </div>
    ${Array.isArray(e.sources) && e.sources.length ? `<p class="sp-source-note">Sources: ${e.sources.map(x => x.url ? `<a href="${esc(x.url)}" rel="nofollow noopener">${esc(x.name || x.url)}</a>` : esc(x.name || '')).join(' · ')}</p>` : ''}
  </section>`;
}
function postMatchBlock(pm){
  return `<section class="sp-postmatch">
    <h3 class="sp-dir">Post-match analysis</h3>
    <div class="sp-msec-grid">
      ${edRow('What actually happened', pm.whatHappened)}
      ${edRow('Tactical developments', pm.tacticalDevelopments)}
      ${edRow('Key performers', pm.keyPerformers)}
      ${edRow('Disappointing performers', pm.disappointing)}
      ${edRow('Against the pre-match prediction', pm.vsPrediction)}
      ${edRow('BRYME post-match analysis', pm.analysis)}
    </div>
  </section>`;
}

/* ================================================================
   LIVE MATCH PREVIEWS — internal linking.
   A page linked only from two deep listing pages is a page a crawler
   reaches late and rarely. These are the fixtures written up and worth
   surfacing, so they get linked from the homepage and the sports hub
   rather than being buried in the Match Centre. The list builds itself
   from the editorial store, so a fixture appears here the moment its
   preview is published and drops off once it is old news.
   ================================================================ */
const LIVE_PREVIEWS = (() => {
  const files = { 'premier-league':'fixtures.json', 'la-liga':'fixtures-la-liga.json',
    'serie-a':'fixtures-serie-a.json', 'bundesliga':'fixtures-bundesliga.json', 'ligue-1':'fixtures-ligue-1.json' };
  const out = [];
  for (const [lg, file] of Object.entries(files)) {
    const fp = path.join(root, 'content', file);
    if (!fs.existsSync(fp)) continue;
    let F; try { F = JSON.parse(fs.readFileSync(fp, 'utf8')); } catch (e) { continue; }
    (F.matchweeks || []).forEach(w => (w.matches || []).forEach(m => {
      const slug = m.id + '-vs-' + m.away;
      if (!editorialFor(lg, slug)) return;
      const d = daysUntil(m.date);
      if (d === null || d < -2) return;                 // drop once it is old news
      out.push({ lg, slug, league: F.league || lg, round: w.number, date: m.date,
        dayLabel: m.dayLabel, time: m.time, home: m.homeName, away: m.awayName, d,
        url: '/sports/' + lg + '/matches/' + slug + '/' });
    }));
  }
  return out.sort((a, b) => String(a.date).localeCompare(String(b.date)));
})();
function livePreviewBlock(limit){
  const items = LIVE_PREVIEWS.slice(0, limit || 10);
  if (!items.length) return '';
  return `<section class="home-section sec-previews"><div class="shell">
    <div class="section-head"><div><div class="eyebrow">Matchday ahead</div><h2>\u26bd Match previews</h2><p class="section-note">Form, head-to-head and BRYME's editorial prediction \u2014 published before kickoff, updated with the result afterwards.</p></div><a href="${url('/sports/premier-league/matches/')}">Match Centre</a></div>
    <div class="vcat-grid">${items.map(m => `<a class="vcat mp-card" href="${url(m.url)}">
      <span class="mp-when">${esc(m.dayLabel || m.date)}${m.time ? ' \u00b7 ' + esc(m.time) : ''}</span>
      <b>${esc(m.home)} v ${esc(m.away)}</b>
      <span>${esc(m.league)} \u00b7 Matchweek ${esc(String(m.round))} \u2014 preview, form and prediction</span></a>`).join('')}</div>
  </div></section>`;
}

/* ---------------- Homepage ---------------- */
const trendNow = trendingList.slice(0, 24); // the complete curated trending list
const popularMovies = popularByType.movie.slice(0, 12);
const popularSeries = popularByType.series.slice(0, 12);
const popularAnime = popularByType.anime.slice(0, 12);
const editorPicksNow = editorPicksList.slice(0, 8);
const freshNow = (newReleases.length >= 8 ? newReleases : movies.filter(m => m.year).sort(sortNewest)).slice(0, 12);
const browseMovies = movies.filter(m => m.typeDir === 'movie').sort(sortPopular).slice(0, 12);
const browseSeries = movies.filter(m => m.typeDir === 'series').sort(sortPopular).slice(0, 12);
const browseAnime = movies.filter(m => m.typeDir === 'anime').sort(sortPopular).slice(0, 12);
const latestArticles = articles.slice(-3).reverse();

function genreChips(list, baseDir, max){
  const map = new Map();
  list.forEach(m => {
    const names = m.typeDir === 'movie' ? [m.genre] : m.genres;
    names.forEach(n => { if (!n) return; const s = slugify(n); if (!map.has(s)) map.set(s, {name:n, count:0}); map.get(s).count++; });
  });
  const arr = [...map.values()].sort((a,b) => b.count - a.count).slice(0, max || 10);
  return arr.map(g => `<a href="${url('/' + baseDir + '/' + slugify(g.name) + '/')}">${esc(g.name)}<b>${g.count}</b></a>`).join('');
}
function heroSlideMarkup(m, idx){
  const kicker = `<span class="type-badge tb-${m.typeDir}">${m.typeLabel.toUpperCase()}</span>${m.year ? `<span>${m.year}</span>` : ''}${m.genreLabel ? `<span class="dot">·</span><span>${esc(m.genreLabel)}</span>` : ''}`;
  const rating = m.rating != null ? `<p class="hero-slide-rating">★ ${m.rating}/10 · BRYME Editorial</p>` : '';
  const desc = esc((m.tagline || m.description || '').slice(0, 200));
  return `<div class="hero-slide${idx === 0 ? ' is-active' : ''}" data-slide data-video="${m.youtubeId}" data-title="${esc(m.title)}" data-url="${m.url}" style="background-image:url('${esc(m.poster)}')"><div class="hero-slide-shade"></div><div class="shell hero-slide-inner"><div class="hero-slide-kicker">${kicker}</div><h1>${esc(m.title)}</h1>${rating}<p>${desc}</p><div class="hero-actions"><button type="button" class="cta hero-watch" data-hero-watch>▶ Watch Trailer</button><a class="cta cta-ghost" href="${m.url}">View Details</a></div></div></div>`;
}
const heroEmbed = JSON.stringify(heroSlides.map(m => ({ t: m.title, ty: m.typeLabel, td: m.typeDir, y: m.year, g: m.genreLabel, r: m.rating, v: m.youtubeId, p: m.poster, d: (m.tagline || m.description || '').slice(0, 200), u: m.url }))).replace(/</g, '\u003c');
write('', layout({
  title: 'Movies, TV Series & Anime – Trailers, Stories & Discovery',
  description: 'BRYME helps you discover what to watch: 630+ movies, TV series and anime with verified trailers, editorial guides, plus sports, memes, practical money guides and tech & AI.',
  path: '/', image: poster(heroSlide), activeNav: 'home',
  schema: [{ '@context':'https://schema.org', '@type':'WebSite', name:site.name, url:url('/'), description:site.description }, { '@context':'https://schema.org', '@type':'CollectionPage', name:'BRYME – Discover Entertainment, Sports, Money & Tech', url:url('/') }],
  body: `<main>
  <section class="hero-carousel" data-hero role="region" aria-roledescription="carousel" aria-label="Featured titles" data-interval="8000">
    <div class="hero-slides">${heroSlides.map(heroSlideMarkup).join('')}</div>
    <button type="button" class="hero-ctrl hero-prev" data-hero-prev aria-label="Previous featured title">&#8249;</button>
    <button type="button" class="hero-ctrl hero-next" data-hero-next aria-label="Next featured title">&#8250;</button>
    <div class="hero-dots" data-hero-dots role="tablist" aria-label="Featured title slides">${heroSlides.map((m, i) => `<button type="button" class="hero-dot${i === 0 ? ' is-active' : ''}" data-hero-dot="${i}" role="tab" aria-label="${esc(m.title)}" aria-selected="${i === 0}"></button>`).join('')}</div>
    <button type="button" class="hero-vctrl hero-mute" data-hero-mute aria-label="Unmute trailer" hidden>&#128263;</button>
    <button type="button" class="hero-vctrl hero-pause" data-hero-pause aria-label="Pause rotation" hidden>&#9208;</button>
    <div class="hero-video" data-hero-video hidden></div>
  </section>
  <main class="shell home-main">
  <section class="home-section brand-strip"><div class="shell"><p class="brand-slogan">Discover what you love. Learn what you need. Find what's next.</p><div class="vchips">${VERTICALS.map(verticalChip).join('')}<a class="vchip vchip-entertainment" href="${url('/entertainment/')}"><span class="vchip-emoji">🎬</span><span class="vchip-name">BRYME Entertainment</span><span class="vchip-tag">Movies, series, anime & articles</span></a></div></div></section>
  <section class="home-section rec-section" id="recommend">
    <div class="shell rec-inner">
      <div class="rec-copy"><div class="eyebrow">Personalised discovery</div><h2>DON'T KNOW WHAT TO WATCH?</h2><p class="rec-sub">Tell us one movie or series you loved. We'll find your next watch.</p></div>
      <form class="rec-form" data-rec-form><label class="visually-hidden" for="rec-input">Enter a movie or series you loved</label><input id="rec-input" data-rec-input type="text" autocomplete="off" placeholder="Enter a movie or series you loved..." aria-label="Enter a movie or series you loved"><button type="submit" class="cta rec-cta">&#10024; RECOMMEND FOR ME</button></form>
      <div class="rec-status" data-rec-status aria-live="polite"></div>
      <div class="rec-results" data-rec-results aria-live="polite"></div>
    </div>
  </section>
  ${railSection('Trending Now', '🔥', trendNow, '/trending/', 'Curated by the BRYME editorial team — not live traffic data. Ranked per content type.', {ranked:true, rankKey:'trendingRank'})}
  ${railSection('Popular Movies', '⭐', popularMovies, '/movies/', 'Evergreen movie favourites, editorially ranked.', {variant:'lead', eyebrow:'Film'})}
  ${railSection('Popular Series', '⭐', popularSeries, '/series/', 'Evergreen TV series favourites, editorially ranked.', {variant:'lead', eyebrow:'Television'})}
  ${railSection('Popular Anime', '⭐', popularAnime, '/anime/', 'Evergreen anime favourites, editorially ranked.', {variant:'wall', eyebrow:'Animation'})}
  ${railSection('Editor\'s Picks', '👑', editorPicksNow, '/trending/#editors-picks', 'Hand-picked by the BRYME editorial desk — separate from trending and popularity.', {variant:'spread', eyebrow:'From the desk'})}
  ${railSection('New Releases', '🆕', freshNow, '/trending/#new-releases', 'Newest verified release years — old classics are never re-labelled as new.', {eyebrow:'Just added'})}
  ${railSection('Movies', '🎬', browseMovies, '/movies/', 'Keep exploring the movie catalogue.', {variant:'wall', eyebrow:'Browse'})}
  ${railSection('Series', '📺', browseSeries, '/series/', 'Keep exploring the series catalogue.', {variant:'chart', eyebrow:'Browse'})}
  ${railSection('Anime', '🍥', browseAnime, '/anime/', 'Keep exploring the anime catalogue.', {variant:'chart', eyebrow:'Browse'})}
  ${livePreviewBlock(10)}
  <section class="home-section"><div class="shell"><div class="section-head"><h2>🎭 Browse by genre</h2><a href="${url('/genres/')}">All genres</a></div><div class="genre-trio"><div class="genre-panel"><h3>🎬 Movie genres <span class="gp-count">${movies.filter(m=>m.typeDir==='movie').length} films</span></h3><div class="genre-chips">${genreChips(movies.filter(m=>m.typeDir==='movie'), 'movies', 9)}</div></div><div class="genre-panel"><h3>📺 Series genres <span class="gp-count">${movies.filter(m=>m.typeDir==='series').length} shows</span></h3><div class="genre-chips">${genreChips(movies.filter(m=>m.typeDir==='series'), 'series', 9)}</div></div><div class="genre-panel"><h3>🍥 Anime genres <span class="gp-count">${movies.filter(m=>m.typeDir==='anime').length} titles</span></h3><div class="genre-chips">${genreChips(movies.filter(m=>m.typeDir==='anime'), 'anime', 9)}</div></div></div></div></section>
  <section class="home-section"><div class="shell"><div class="section-head"><div><div class="eyebrow">From the editorial desk</div><h2>📰 Latest articles</h2></div><a href="${url('/articles/')}">All stories</a></div><div class="story-grid">${latestArticles.map(a => `<a href="${url('/article/' + a.slug + '/')}"><span>${esc(a.category)}</span><h3>${esc(a.title)}</h3><p>${esc(a.description)}</p><b>Read story</b></a>`).join('')}</div></div></section>
  <section class="discover-cta"><div><div class="eyebrow">Full catalogue</div><h2>Pick a lane: Movies, Series or Anime.</h2><p>Each section is strictly filtered to its own content type. No mixed-up walls of posters.</p></div><a class="cta" href="${url('/search/')}">Search everything</a></div></section></main></main><script id="hero-data" type="application/json">${heroEmbed}</script>`
}));


/* ---------------- League fixtures (all five leagues) ---------------- */
const LEAGUE_FIXTURE_FILES = {
  'premier-league': 'fixtures.json',
  'la-liga': 'fixtures-la-liga.json',
  'serie-a': 'fixtures-serie-a.json',
  'bundesliga': 'fixtures-bundesliga.json',
  'ligue-1': 'fixtures-ligue-1.json'
};
const LEAGUE_FIX = [
  { slug:'premier-league', name:'Premier League', roundLabel:'Matchweek', tz:'Europe/London', timeSuffix:'UK',
    stdSlot:'<b>(std)</b> marks the Premier League\'s standard slot — 15:00 on weekend/Bank Holiday dates and 20:00 midweek — where no specific time was published. ',
    crest:id=>url('/assets/img/sports/pl/'+id+'.svg'), alt:(id,name)=> name + ' official club crest' },
  { slug:'la-liga', name:'La Liga', roundLabel:'Jornada', tz:'Europe/Madrid', timeSuffix:null,
    crest:id=>url('/assets/img/sports/ll/'+(LL_NAME[id]||id)+'.png'), alt:(id,name)=> name + ' official club crest' },
  { slug:'serie-a', name:'Serie A', roundLabel:'Giornata', tz:'Europe/Rome', timeSuffix:null,
    crest:id=>url('/assets/img/sports/sa/'+id+(id==='lazio'?'.png':'.svg')), alt:(id,name)=> name + ' official club crest' },
  { slug:'bundesliga', name:'Bundesliga', roundLabel:'Spieltag', tz:'Europe/Berlin', timeSuffix:null,
    crest:id=> id==='hamburg' ? url('/assets/img/sports/club-hamburg.svg') : url('/assets/img/sports/bl/'+id+'.svg'),
    alt:(id,name)=> id==='hamburg' ? 'Abstract crest for '+name+' — BRYME-generated illustration' : name + ' official club crest' },
  { slug:'ligue-1', name:'Ligue 1', roundLabel:'Journée', tz:'Europe/Paris', timeSuffix:null,
    crest:id=>url('/assets/img/sports/l1/'+id+'.webp'), alt:(id,name)=> name + ' official club crest' }
];
const LEAGUE_FIXTURES_DATA = {};
const LEAGUE_MATCH_PATHS = [];
const UNPLAYED_MATCH_PATHS = new Set();
function loadLeagueFixtures(slug){
  if (LEAGUE_FIXTURES_DATA[slug]) return LEAGUE_FIXTURES_DATA[slug];
  const file = LEAGUE_FIXTURE_FILES[slug];
  try { LEAGUE_FIXTURES_DATA[slug] = JSON.parse(fs.readFileSync(path.join(root, 'content', file), 'utf8')); }
  catch (e) { warnings.push(file + ' unreadable'); LEAGUE_FIXTURES_DATA[slug] = { matchweeks: [], venues: {} }; }
  return LEAGUE_FIXTURES_DATA[slug];
}

for (const v of VERTICALS) {
  verticalPage(v, null);
  (v.categories || []).forEach(c => verticalPage(v, c));
}

// Entertainment hub — the existing mature section, presented under BRYME Entertainment
write('entertainment', layout({
  title: 'BRYME Entertainment – Movies, TV Series & Anime',
  description: 'BRYME Entertainment: 630+ movies, TV series and anime with verified trailers, editorial articles and curated recommendations.',
  path: '/entertainment/', activeNav: 'entertainment',
  schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:'BRYME Entertainment', description:'Movies, TV series and anime discovery on BRYME.', url:url('/entertainment/') }, breadcrumbs([{name:'Home', path:'/'}, {name:'BRYME Entertainment', path:'/entertainment/'}])],
  body: `<main class="shell"><section class="hero"><div class="eyebrow">🎬 BRYME Entertainment</div><h1>Movies, series &amp; anime worth your time.</h1><p class="lead">Browse 630+ titles with verified trailers, editorial articles and curated recommendations — all in one place.</p></section>
  <section class="section"><div class="grid-2" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px">${[['Movies','/movies/','🎬'],['Series','/series/','📺'],['Anime','/anime/','🍥'],['Articles','/articles/','📰'],['Genres','/genres/','🎭'],['Years','/years/','🗓️'],['Trending & Picks','/trending/','🔥'],['Topics','/topics/','🧭']].map(x => `<a class="vcat" href="${url(x[1])}"><b>${x[2]} ${x[0]}</b><span>Explore the ${x[0].toLowerCase()} section</span></a>`).join('')}</div></section>
  <section class="section"><div class="section-head"><h2>🔥 Trending Now</h2><a href="${url('/trending/')}">View all</a></div><div class="rail">${trendNow.slice(0, 10).map(card).join('')}</div></section>
  <section class="section"><div class="section-head"><h2>⭐ Popular Movies</h2><a href="${url('/movies/')}">All movies</a></div><div class="rail">${popularMovies.slice(0, 10).map(card).join('')}</div></section>
  <section class="section"><div class="section-head"><h2>⭐ Popular Series</h2><a href="${url('/series/')}">All series</a></div><div class="rail">${popularSeries.slice(0, 10).map(card).join('')}</div></section>
  <section class="section"><div class="section-head"><h2>⭐ Popular Anime</h2><a href="${url('/anime/')}">All anime</a></div><div class="rail">${popularAnime.slice(0, 10).map(card).join('')}</div></section>
  <section class="section"><div class="section-head"><h2>📰 Latest articles</h2><a href="${url('/articles/')}">All stories</a></div><div class="story-grid">${latestArticles.map(a => `<a href="${url('/article/' + a.slug + '/')}"><span>${esc(a.category)}</span><h3>${esc(a.title)}</h3><p>${esc(a.description.slice(0, 120))}</p><b>Read story</b></a>`).join('')}</div></section></main>`
}));

/* ================================================================
   BRYME SPORTS — hero carousel, transfers, managers, editorial
   table, FPL, match centre, fixtures/results, article placeholders.
   Structure first, content later. No fabricated data.
   ================================================================ */
const sportsCfgPath = path.join(root, 'content', 'sports.json');
let sportsCfg = {};
if (fs.existsSync(sportsCfgPath)) { try { sportsCfg = JSON.parse(fs.readFileSync(sportsCfgPath, 'utf8')); } catch (e) { warnings.push('sports.json unreadable'); } }
const S = sportsCfg || {};
const SEASON = S.season || '2026/27';
const MW = S.matchweek || 1;
const mwLabel = 'Matchweek ' + MW;

/* --- image placeholder system: alt/credit/source/license-capable --- */
function sportImgPlaceholder(alt, credit){
  return `<div class="sp-img" role="img" aria-label="${esc(alt)}"><span>${esc(alt)}</span>${credit ? `<small>Image: ${esc(credit)}</small>` : '<small>Image placeholder — licensed/reusable image to be added</small>'}</div>`;
}
/* --- article placeholder page (full structure, body pending) --- */
function sportArticlePlaceholder(art){
  const route = art.route;
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:art.title, path:'/' + route + '/'}];
  const schema = [
    { '@context':'https://schema.org', '@type':'Article', headline: art.title, description: art.excerpt,
      mainEntityOfPage: url('/' + route + '/'), publisher: { '@type':'Organization', name: site.name } },
    breadcrumbs(crumbs)
  ];
  const related = (art.related || []).map(r => `<a class="sp-rel" href="${url('/sports/' + r + '/')}">${esc(r.split('/').pop().replace(/-/g, ' '))}</a>`).join('');
  const body = `<main class="shell">
    <div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / ${esc(art.title)}</div>
    <article class="sp-article">
      <header class="sp-article-head"><div class="eyebrow">⚽ BRYME Sports · ${esc(art.category)}</div><h1>${esc(art.title)}</h1>
        <p class="lead">${esc(art.excerpt)}</p>
        <div class="sp-meta"><span>By BRYME Sports Editorial</span><span>Published: when the article is finalised</span><span>Last updated: —</span></div>
      </header>
      ${sportImgPlaceholder(art.title + ' — hero image', null)}
      <div class="sp-body-placeholder">
        <b>Article body — coming soon</b>
        <p>This page is a structured placeholder. The full article will be researched, written in BRYME's own editorial voice and published here. Facts, quotes, statistics and lineups are never invented.</p>
      </div>
      <section class="sp-source"><h2>Source</h2><p><b>Source:</b> [Source Name]</p><p><b>Original report:</b> [Link]</p><p class="sp-source-note">Information on this page is rewritten in BRYME's own original editorial voice, never copied. External selections and claims are always identified with their source.</p></section>
      ${related ? `<section class="sp-related"><h2>Related reading</h2><div class="sp-rel-grid">${related}</div></section>` : ''}
    </article></main>`;
  write('sports/' + route, layout({ title: art.title + ' | BRYME Sports', description: art.excerpt, path: '/sports/' + route + '/', activeNav: 'sports', schema, body }));
}
/* --- transfer page: structured table, legend, empty state --- */
function transferPage(league){
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Transfers', path:'/sports/transfers/'}, {name:league.title, path:'/sports/transfers/' + league.id + '-2026-27/'}];
  const legend = `<span class="sp-st-conf">${esc(S.transfers.legend.confirmed)}</span><span class="sp-st-rep">${esc(S.transfers.legend.reported)}</span><span class="sp-st-rum">${esc(S.transfers.legend.rumoured)}</span>`;
  const empty = `<tr class="sp-empty"><td colspan="6">No verified ${esc(league.name)} transfers listed yet. Entries appear here only when confirmed by clubs or reported by credible outlets — with the source shown. Rumours are never presented as confirmed.</td></tr>`;
  const row = (dir) => `<h3 class="sp-dir">${dir === 'in' ? '⬇ Transfer In' : '⬆ Transfer Out'}</h3><div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Player</th><th>From</th><th>To</th><th>Status</th><th>Date</th><th>Source</th></tr></thead><tbody>${empty}</tbody></table></div>`;
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/transfers/')}">Transfers</a> / ${esc(league.title)}</div>
    <section class="hero"><div class="eyebrow">⚽ Transfers · ${esc(league.name)}</div><h1>${esc(league.title)}</h1><p class="lead">Structured transfer tracker for ${esc(league.name)}. Status legend: ${legend}.</p></section>
    <div class="vnote">${esc(S.transfers.disclaimer)}</div>
    ${row('in')}${row('out')}
    <section class="sp-related"><h2>Other leagues</h2><div class="sp-rel-grid">${S.transfers.leagues.filter(l => l.id !== league.id).map(l => `<a class="sp-rel" href="${url('/sports/transfers/' + l.id + '-2026-27/')}">${esc(l.name)} Transfers</a>`).join('')}</div></section>
    <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/managers-2026-27/')}">Managers In &amp; Out</a><a class="sp-rel" href="${url('/sports/premier-league/matchweek-1-preview/')}">Matchweek ${MW} Preview</a></div></section></main>`;
  write('sports/transfers/' + league.id + '-2026-27', layout({ title: league.title + ' | BRYME Sports', description: 'Structured ' + league.name + ' transfer tracker for ' + SEASON + ' — confirmed, reported and rumoured deals, each with a source.', path: '/sports/transfers/' + league.id + '-2026-27/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: league.title, url: absUrl('/sports/transfers/' + league.id + '-2026-27/') }, breadcrumbs(crumbs)], body }));
}
/* --- transfers hub --- */
function transfersHub(){
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Transfers', path:'/sports/transfers/'}];
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / Transfers</div>
    <section class="hero"><div class="eyebrow">⚽ Transfers</div><h1>Transfer trackers ${SEASON}</h1><p class="lead">League-by-league transfer trackers. Every deal is labelled Confirmed, Reported or Rumoured — never presented as more than the source supports.</p></section>
    <div class="vnote">${esc(S.transfers.disclaimer)}</div>
    <section class="section"><div class="vcat-grid">${S.transfers.leagues.map(l => `<a class="vcat" href="${url('/sports/transfers/' + l.id + '-2026-27/')}"><b>${esc(l.name)}</b><span>Transfers ${SEASON} — tracker</span></a>`).join('')}<a class="vcat" href="${url('/sports/managers-2026-27/')}"><b>Managers</b><span>Managers In &amp; Out — ${SEASON}</span></a></div></section></main>`;
  write('sports/transfers', layout({ title: 'Transfers ' + SEASON + ' | BRYME Sports', description: 'League-by-league football transfer trackers for ' + SEASON + ' — Premier League, La Liga, Serie A, Bundesliga and Ligue 1, each deal labelled and sourced.', path: '/sports/transfers/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: 'Transfers ' + SEASON, url: absUrl('/sports/transfers/') }, breadcrumbs(crumbs)], body }));
}
/* --- managers page (real data from the transfer trackers) --- */
function managersPage(){
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Managers', path:'/sports/managers-2026-27/'}];
  // Gather manager data from the five league trackers
  const allClubs = [];
  const plPath2 = path.join(root, 'content', 'pl-transfers.json');
  if (fs.existsSync(plPath2)) {
    try {
      const pl2 = JSON.parse(fs.readFileSync(plPath2, 'utf8'));
      (pl2.clubs || []).forEach(c => allClubs.push({ league: 'Premier League', name: c.name, id: c.id, manager: c.manager, note: c.managerNote }));
    } catch (e) { warnings.push('pl-transfers.json unreadable (managers)'); }
  }
  const lgPath2 = path.join(root, 'content', 'league-transfers.json');
  if (fs.existsSync(lgPath2)) {
    try {
      const lg2 = JSON.parse(fs.readFileSync(lgPath2, 'utf8'));
      (lg2.leagues || []).forEach(lg => (lg.clubs || []).forEach(c => allClubs.push({ league: lg.name, name: c.name, id: c.id, manager: c.manager, note: c.managerNote })));
    } catch (e) { warnings.push('league-transfers.json unreadable (managers)'); }
  }
  const leagueOrder = ['Premier League', 'La Liga', 'Serie A', 'Bundesliga', 'Ligue 1'];
  const byLeague = {};
  allClubs.forEach(c => { (byLeague[c.league] = byLeague[c.league] || []).push(c); });
  const managerCrest = (league, id) => {
    const lgId = { 'Premier League':'premier-league', 'La Liga':'la-liga', 'Serie A':'serie-a', 'Bundesliga':'bundesliga', 'Ligue 1':'ligue-1' }[league];
    if (lgId === 'premier-league') return url('/assets/img/sports/pl/' + id + '.svg');
    if (lgId === 'la-liga') return url('/assets/img/sports/ll/' + (LL_NAME[id] || id) + '.png');
    if (lgId === 'bundesliga') return id === 'hamburg' ? url('/assets/img/sports/club-' + id + '.svg') : url('/assets/img/sports/bl/' + id + '.svg');
    if (lgId === 'ligue-1') return url('/assets/img/sports/l1/' + id + '.webp');
    if (lgId === 'serie-a') return url('/assets/img/sports/sa/' + id + (id === 'lazio' ? '.png' : '.svg'));
    return url('/assets/img/sports/club-' + id + '.svg');
  };
  const badge = note => {
    const n = (note || '').toLowerCase();
    if (/^new/.test(n)) return '<span class="sp-mgr-badge sp-mgr-new">NEW</span>';
    if (/no change/.test(n)) return '<span class="sp-mgr-badge sp-mgr-keep">No change</span>';
    return '';
  };
  const leagueBlocks = leagueOrder.filter(l => byLeague[l]).map(lg => {
    const rows = byLeague[lg].map(c => {
      const lgId = { 'Premier League':'premier-league', 'La Liga':'la-liga', 'Serie A':'serie-a', 'Bundesliga':'bundesliga', 'Ligue 1':'ligue-1' }[lg];
      const official = lg === 'Premier League' || lg === 'Serie A' || (['La Liga','Bundesliga','Ligue 1'].includes(lg) && c.id !== 'hamburg');
      return `<tr><td class="sp-mgr-club"><img src="${managerCrest(lg, c.id)}" alt="${official ? esc(c.name) + ' official club crest' : 'Abstract crest for ' + esc(c.name) + ' — BRYME-generated illustration'}" width="28" height="34" loading="lazy"><b>${esc(c.name)}</b></td><td>${c.manager ? '<b>' + esc(c.manager) + '</b>' : '<span class="sp-mgr-pending">Pending verification</span>'}</td><td>${badge(c.note)} <span class="sp-mgr-note">${esc(c.note || '')}</span></td></tr>`;
    }).join('');
    return `<h3 class="sp-dir">${esc(lg)}</h3><div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Club</th><th>Manager</th><th>Status / note</th></tr></thead><tbody>${rows}</tbody></table></div>`;
  }).join('');
  const note = 'Managerial changes are only listed once confirmed by the clubs or widely reported by credible outlets. Sources are always shown on the league transfer trackers.';
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / Managers</div>
    <section class="hero"><div class="eyebrow">⚽ Managers</div><h1>${esc(S.managers.title)}</h1><p class="lead">${esc(note)}</p></section>
    <p class="sp-updated">Last updated: ${esc('13 August 2026')}</p>
    <div class="sp-credits"><b>Premier League club crests</b> © Copyright The Football Association Premier League Limited, 2016, used under the Premier League Logo Site media licence for editorial reporting. BRYME Sports is not affiliated with, endorsed or sponsored by the Premier League or any club. Crests for La Liga (LaLiga), Serie A, Bundesliga (DFL) and Ligue 1 (LFP) clubs are © their respective clubs, retrieved from official league/club websites and Wikimedia Commons, and used solely for editorial reporting. Only Hamburger SV still shows a BRYME-generated abstract illustration.</div>
    <div class="sp-legend-line">${leagueOrder.filter(l => byLeague[l]).map(l => `<span class="sp-st-conf">${esc(l)}</span>`).join(' ')}</div>
    ${leagueBlocks}
    <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/transfers/')}">Transfer trackers</a><a class="sp-rel" href="${url('/sports/premier-league/matchweek-1-preview/')}">Matchweek ${MW} Preview</a></div></section></main>`;
  write('sports/managers-2026-27', layout({ title: S.managers.title + ' | BRYME Sports', description: note, path: '/sports/managers-2026-27/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: S.managers.title, url: absUrl('/sports/managers-2026-27/') }, breadcrumbs(crumbs)], body }));
}
/* --- editorial prediction table --- */
function editorialTablePage(){
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Premier League', path:'/sports/premier-league/'}, {name:'Table Prediction', path:'/sports/premier-league/table/'}];
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/premier-league/')}">Premier League</a> / Table Prediction</div>
    <section class="hero"><div class="eyebrow">⚽ Premier League · Editorial</div><h1>${esc(S.editorialTable.title)}</h1><div class="sp-ed-label">${esc(S.editorialTable.label)}</div><p class="lead">${esc(S.editorialTable.note)}</p></section>
    <div class="sp-table-wrap"><table class="sp-table sp-table-pred"><thead><tr>${S.editorialTable.columns.map(c => `<th>${esc(c)}</th>`).join('')}</tr></thead><tbody><tr class="sp-empty"><td colspan="7">The editorial prediction table will appear here once the BRYME Sports editorial team finalises it for ${mwLabel}. Predictions are never presented as guarantees or as the official table.</td></tr></tbody></table></div>
    <p class="sp-source-note">After the gameweek is completed, this component can be replaced with the official Premier League table.</p>
    <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/premier-league/fixtures/')}">Fixtures</a><a class="sp-rel" href="${url('/sports/premier-league/results/')}">Results</a><a class="sp-rel" href="${url('/sports/premier-league/matchweek-1-preview/')}">Matchweek ${MW}</a></div></section></main>`;
  write('sports/premier-league/table', layout({ title: S.editorialTable.title + ' | BRYME Sports', description: S.editorialTable.label + ' — ' + S.editorialTable.note, path: '/sports/premier-league/table/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: S.editorialTable.title, url: absUrl('/sports/premier-league/table/') }, breadcrumbs(crumbs)], body }));
}
/* --- FPL hub --- */
function fplHub(){
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Fantasy Premier League', path:'/sports/fpl/'}];
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / Fantasy Premier League</div>
    <section class="hero"><div class="eyebrow">⚽ Fantasy Premier League</div><h1>${esc(S.fpl.title)}</h1><p class="lead">${esc(S.fpl.desc)}</p></section>
    <section class="section"><div class="vcat-grid">${S.fpl.sections.map(s => `<a class="vcat" href="${url('/sports/fpl/gameweek-' + MW + '/#' + s.id + '/')}"><b>${esc(s.name)}</b><span>Gameweek ${MW} section</span></a>`).join('')}<a class="vcat" href="${url('/sports/fpl/gameweek-' + MW + '-players-to-watch/')}"><b>Gameweek ${MW} Players to Watch</b><span>Popular picks, differentials, captaincy</span></a></div></section>
    <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/premier-league/matchweek-1-preview/')}">Matchweek ${MW} Preview</a><a class="sp-rel" href="${url('/sports/premier-league/injuries-matchweek-1/')}">Injury Report</a></div></section></main>`;
  write('sports/fpl', layout({ title: 'Fantasy Premier League | BRYME Sports', description: S.fpl.desc, path: '/sports/fpl/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: 'Fantasy Premier League', url: absUrl('/sports/fpl/') }, breadcrumbs(crumbs)], body }));
  // gameweek hub
  const gwBody = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/fpl/')}">FPL</a> / Gameweek ${MW}</div>
    <section class="hero"><div class="eyebrow">⚽ FPL · Gameweek ${MW}</div><h1>FPL Gameweek ${MW}</h1><p class="lead">Gameweek-by-gameweek FPL content. Each section below fills with researched, sourced content.</p></section>
    <section class="section">${S.fpl.sections.map(s => `<div class="sp-gw-sec" id="${s.id}"><h2>${esc(s.name)}</h2><p class="sp-empty-line">Content for this section is being prepared. No picks, predictions or difficulty ratings are shown before they are researched and sourced.</p></div>`).join('')}</section>
    <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/fpl/gameweek-' + MW + '-players-to-watch/')}">Players to Watch</a><a class="sp-rel" href="${url('/sports/premier-league/matchweek-1-preview/')}">Matchweek ${MW} Preview</a></div></section></main>`;
  write('sports/fpl/gameweek-' + MW, layout({ title: 'FPL Gameweek ' + MW + ' | BRYME Sports', description: 'Fantasy Premier League Gameweek ' + MW + ' — players to watch, picks, captaincy and fixture difficulty.', path: '/sports/fpl/gameweek-' + MW + '/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: 'FPL Gameweek ' + MW, url: absUrl('/sports/fpl/gameweek-' + MW + '/') }, breadcrumbs([{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'FPL', path:'/sports/fpl/'}, {name:'Gameweek ' + MW, path:'/sports/fpl/gameweek-' + MW + '/'}])], body: gwBody }));
}
/* --- fixtures / results --- */
function euDstOffset(dateISO){
  // returns UTC offset hours for the league's local time on that date: +1 (CET) / +2 (CEST)
  const y = Number(dateISO.slice(0, 4));
  let start = new Date(Date.UTC(y, 2, 31)); while (start.getUTCDay() !== 0) start.setUTCDate(start.getUTCDate() - 1);
  let end = new Date(Date.UTC(y, 9, 31)); while (end.getUTCDay() !== 0) end.setUTCDate(end.getUTCDate() - 1);
  const t = Date.parse(dateISO + 'T12:00:00Z');
  return (t >= start.getTime() && t < end.getTime()) ? 2 : 1;
}
function leagueTimeInfo(lg, m){
  // returns { display, wat } for a match kickoff
  if (!m.time) return { display: '<span class="sp-fixt-time">Time TBC</span>', wat: '' };
  if (lg.slug === 'premier-league' && !m.timePublished) {
    return { display: `<span class="sp-fixt-time">${esc(m.time)} UK</span><span class="sp-std"> · std</span>`, wat: '' };
  }
  let offset;
  if (lg.slug === 'premier-league') {
    offset = euDstOffset(m.date) - 1; // BST +1 / GMT 0
  } else {
    offset = euDstOffset(m.date); // CEST +2 / CET +1
  }
  const tzSuffix = lg.timeSuffix || (offset === 2 ? 'CEST' : 'CET');
  let wat = '';
  if (offset !== 1) { // WAT = UTC+1; show when it differs from league-local time
    const [h, mn] = m.time.split(':').map(Number);
    let w = h + 1 - offset; if (w < 0) w += 24; if (w >= 24) w -= 24;
    wat = `<span class="sp-std"> · ${String(w).padStart(2, '0')}:${String(mn).padStart(2, '0')} WAT</span>`;
  }
  return { display: `<span class="sp-fixt-time">${esc(m.time)} ${tzSuffix}</span>`, wat };
}
function fixtureRowFor(lg, m){
  const t = leagueTimeInfo(lg, m);
  const tv = m.tv ? `<span class="sp-tv${(m.tv || '').toLowerCase().indexOf('tnt') > -1 ? ' tnt' : ''}">${esc(m.tv)}</span>` : '';
  const dayM = (m.dayLabel || '').match(/^(\w+)\s+(\d{1,2})\s+(\w+)(?:\s+(\d{4}))?/);
  const day = dayM ? esc(dayM[1] + ' ' + dayM[2] + ' ' + dayM[3]) + `<span class="sp-std">${esc(dayM[4] ? ' ' + dayM[4] : '')}</span>` : esc(m.dayLabel || m.date);
  const urlM = '/sports/' + lg.slug + '/matches/' + m.id + '-vs-' + m.away + '/';
  return `<div class="sp-fixture" aria-label="${esc(m.homeName)} v ${esc(m.awayName)}">
      <div class="sp-fixt"><span class="sp-fixt-day">${day}</span><img src="${lg.crest(m.id)}" alt="" width="22" height="27" loading="lazy"><a href="${url(urlM)}">${esc(m.homeName)}</a><span class="sp-vs">v</span><img src="${lg.crest(m.away)}" alt="" width="22" height="27" loading="lazy"><a href="${url(urlM)}">${esc(m.awayName)}</a></div>
      <div class="sp-fixt-info">${t.display}${t.wat}${tv}<a class="sp-matchlink" href="${url(urlM)}">Match page →</a></div>
    </div>`;
}
function fixturesResults(){
  for (const lg of LEAGUE_FIX) {
    const F = loadLeagueFixtures(lg.slug);
    const mwBlocks = (F.matchweeks || []).map(w => {
      const days = [...new Set(w.matches.map(m => m.dayLabel))];
      return `<section class="sp-mw" id="mw-${w.number}"><div class="sp-mw-head"><h2>${esc(lg.roundLabel)} ${w.number}</h2><span class="sp-mw-date">${esc(days.join(' · '))}</span></div>${w.matches.map(m => fixtureRowFor(lg, m)).join('')}</section>`;
    }).join('');
    const total = (F.matchweeks || []).reduce((n, w) => n + w.matches.length, 0);
    const crumb = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:F.league, path:'/sports/' + lg.slug + '/'}, {name:'Fixtures', path:'/sports/' + lg.slug + '/fixtures/'}];
    const hasTbc = (F.matchweeks || []).some(w => w.matches.some(m => !m.time));
    const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/' + lg.slug + '/')}">${esc(F.league)}</a> / Fixtures</div>
      <section class="hero"><div class="eyebrow">⚽ ${esc(F.league)} · Fixtures</div><h1>${esc(F.league)} Fixtures ${esc(F.season)}</h1><p class="lead">All ${total} fixtures of the ${esc(F.season)} ${esc(F.league)} season. ${F.source ? esc(F.source) : ''} Dates and kick-off times are shown exactly as published — nothing is invented.</p></section>
      <p class="sp-updated">Last updated: ${esc(F.lastUpdated || 'Pending verification')}</p>
      <div class="sp-truth"><b>Truth first.</b><p>This is the official fixture list as published for the ${esc(F.season)} ${esc(F.league)} season. ${F.subjectToChange ? esc(F.subjectToChange) : ''}</p></div>
      <div class="sp-fix-legend">${lg.stdSlot || ''}${hasTbc ? '<b>Time TBC</b> means the league has not yet published the kick-off time for that match — it appears here as soon as it is officially confirmed. ' : ''}${F.kickoffNote ? esc(F.kickoffNote) : ''}</div>
      <nav class="sp-mwnav" aria-label="Jump to round">${(F.matchweeks || []).map(w => `<a href="#mw-${w.number}">${esc(lg.roundLabel.slice(0, 2))} ${w.number}</a>`).join('')}</nav>
      ${mwBlocks}
      ${(F.footnotes && F.footnotes.length) ? `<div class="sp-fix-legend"><b>Fixture notes</b><br>${F.footnotes.map(n => '• ' + esc(n)).join('<br>')}</div>` : ''}
      <section class="sp-source"><h2>Source</h2><p><b>Source:</b> ${esc(F.source || 'Official league fixture release')}${F.sourceUrl ? ` — <a href="${esc(F.sourceUrl)}" rel="nofollow noopener">${esc(new URL(F.sourceUrl).hostname)}</a>` : ''}</p><p class="sp-source-note">Fixtures are summarised in BRYME's own words from official publications. Dates, kick-off times and venues are only listed as published; changes announced officially are reflected as soon as BRYME verifies them. Results are never shown before a match is played.</p></section>
      <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/' + lg.slug + '/results/')}">Results</a><a class="sp-rel" href="${url('/sports/' + lg.slug + '/matches/')}">Match Centre</a><a class="sp-rel" href="${url('/sports/transfers/' + lg.slug + '-2026-27/')}">Transfers</a><a class="sp-rel" href="${url('/sports/')}">BRYME Sports</a></div></section></main>`;
    write('sports/' + lg.slug + '/fixtures', layout({ title: `${F.league} Fixtures ${F.season}: All ${total} Matches`, description: `Complete ${F.league} ${F.season} fixture list — all ${total} matches across ${(F.matchweeks || []).length} rounds with dates and kick-off times from the official release. Nothing invented.`, path: '/sports/' + lg.slug + '/fixtures/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: `${F.league} Fixtures ${F.season}`, description: `All ${total} ${F.league} ${F.season} fixtures as published.`, url: absUrl('/sports/' + lg.slug + '/fixtures/') }, breadcrumbs(crumb)], body }));

    // ---- results page (honest empty state + next round preview) ----
    const mw1 = (F.matchweeks && F.matchweeks[0] && F.matchweeks[0].matches) || [];
    const nextBlock = mw1.length ? `<h3 class="sp-dir">Upcoming — ${esc(lg.roundLabel)} 1 (${esc([...new Set(mw1.map(m => m.dayLabel))].join(' · '))})</h3><div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Date</th><th>Fixture</th><th>Kickoff</th><th>TV</th></tr></thead><tbody>${mw1.map(m => `<tr><td>${esc(m.dayLabel)}</td><td><b>${esc(m.homeName)}</b> v <b>${esc(m.awayName)}</b></td><td>${m.time ? esc(m.time + (lg.timeSuffix || ' local')) : 'TBC'}</td><td>${esc(m.tv || '—')}</td></tr>`).join('')}</tbody></table></div>` : '';
    const crumbR = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:F.league, path:'/sports/' + lg.slug + '/'}, {name:'Results', path:'/sports/' + lg.slug + '/results/'}];
    const bodyR = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/' + lg.slug + '/')}">${esc(F.league)}</a> / Results</div>
      <section class="hero"><div class="eyebrow">⚽ ${esc(F.league)} · Results</div><h1>${esc(F.league)} Results ${esc(F.season)}</h1><p class="lead">Completed ${esc(F.league)} match results. Results appear only after matches are actually played and officially confirmed — never predicted or assumed.</p></section>
      <p class="sp-updated">Last updated: ${esc(F.lastUpdated || 'Pending verification')}</p>
      ${(() => {
        /* Played matches, newest round first. Driven entirely by content/results.json,
           so this page fills itself in as results are added - no separate edit needed. */
        const rows = [];
        (F.matchweeks || []).forEach(w => w.matches.forEach(m => {
          const r = resultFor(lg.slug, m.id + '-vs-' + m.away);
          if (r) rows.push({ w, m, r });
        }));
        if (!rows.length) return `<div class="vstate"><b>No matches played yet</b><p>The ${esc(F.season)} ${esc(F.league)} season ${(F.matchweeks && F.matchweeks[0] && F.matchweeks[0].matches[0]) ? 'starts ' + esc(F.matchweeks[0].matches[0].dayLabel) : 'has not started'} — so as of ${esc(F.lastUpdated || 'today')} no league fixtures have been played and there are no results to show. When matches are played, the official result and match data are added here after full-time — verified only.</p></div>`;
        rows.reverse();
        return `<h3 class="sp-dir">Results — ${rows.length} match${rows.length === 1 ? '' : 'es'} played</h3>
        <div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Round</th><th>Match</th><th>Score</th><th>Source</th></tr></thead><tbody>${rows.map(({w, m, r}) => `<tr><td>${esc(lg.roundLabel)} ${w.number}</td><td><a href="${url('/sports/' + lg.slug + '/matches/' + m.id + '-vs-' + m.away + '/')}">${esc(m.homeName)} v ${esc(m.awayName)}</a></td><td><b>${r.homeScore}&ndash;${r.awayScore}</b>${r.status && r.status !== 'FT' ? ` <span class="sp-pens">${esc(r.status)}</span>` : ''}</td><td><a href="${esc(r.source.url)}" rel="nofollow noopener">${esc(r.source.name || 'source')}</a></td></tr>`).join('')}</tbody></table></div>`;
      })()}
      ${nextBlock}
      <div class="sp-truth"><b>Truth first.</b><p>BRYME never publishes a result, scoreline or scorer before a match is played and the outcome is confirmed by the club or official league channels. If a result cannot be verified, it is not shown.</p></div>
      <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/' + lg.slug + '/fixtures/')}">Fixtures</a><a class="sp-rel" href="${url('/sports/' + lg.slug + '/matches/')}">Match Centre</a><a class="sp-rel" href="${url('/sports/transfers/' + lg.slug + '-2026-27/')}">Transfers</a></div></section></main>`;
    write('sports/' + lg.slug + '/results', layout({ title: `${F.league} Results ${F.season}`, description: `${F.league} ${F.season} results — only official, verified match results after matches are played. No results are predicted or assumed.`, path: '/sports/' + lg.slug + '/results/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: `${F.league} Results ${F.season}`, url: absUrl('/sports/' + lg.slug + '/results/') }, breadcrumbs(crumbR)], body: bodyR }));
  }
}

/* --- match centre + per-match pages (all five leagues) --- */
const MW1_REVIEW_PATH = path.join(root, 'content', 'premier-league-matchweek-1-analysis.json');
const MW1_REVIEW = fs.existsSync(MW1_REVIEW_PATH) ? JSON.parse(fs.readFileSync(MW1_REVIEW_PATH, 'utf8')).matches || {} : {};
/* ================================================================
   MATCH RESULTS — content/results.json is the single source of truth for
   what has actually been played. A fixture with no entry here is unplayed:
   it renders as a fixture, stays noindex and stays out of the sitemap.
   The moment a sourced result is added the page gains real content and
   becomes indexable automatically.

   A result is only published if it carries a source with a url. An
   unsourced result is refused and reported, never rendered - the site
   must never show a scoreline it cannot attribute.
   ================================================================ */
const RESULTS = (() => {
  const f = path.join(root, 'content', 'results.json');
  if (!fs.existsSync(f)) return {};
  try { return JSON.parse(fs.readFileSync(f, 'utf8')); } catch (e) { return {}; }
})();
const REJECTED_RESULTS = [];
function resultFor(leagueSlug, matchSlug){
  const r = ((RESULTS[leagueSlug] || {})[matchSlug]);
  if (!r) return null;
  const scored = Number.isInteger(r.homeScore) && Number.isInteger(r.awayScore);
  const sourced = r.source && r.source.url;
  if (!scored || !sourced) {
    REJECTED_RESULTS.push(`${leagueSlug}/${matchSlug}: ${!scored ? 'homeScore/awayScore must be integers' : 'missing source.url'}`);
    return null;
  }
  return r;
}
function resultBlock(m, r){
  const st = esc(r.status || 'FT');
  const pens = r.status === 'FT (pens)' && r.penalties ? ` <span class="sp-pens">(${esc(r.penalties)} on penalties)</span>` : '';
  const goals = Array.isArray(r.scorers) && r.scorers.length
    ? `<div class="sp-scorers"><div><b>${esc(m.homeName)}</b><ul>${r.scorers.filter(g => g.team === 'home').map(g => `<li>${esc(g.player)}${g.minute ? ` <span>${esc(String(g.minute))}'</span>` : ''}</li>`).join('') || '<li class="sp-none">—</li>'}</ul></div><div><b>${esc(m.awayName)}</b><ul>${r.scorers.filter(g => g.team === 'away').map(g => `<li>${esc(g.player)}${g.minute ? ` <span>${esc(String(g.minute))}'</span>` : ''}</li>`).join('') || '<li class="sp-none">—</li>'}</ul></div></div>`
    : '';
  const extra = [r.attendance ? `Attendance ${esc(String(r.attendance))}` : '', r.playedOn ? `Played ${esc(r.playedOn)}` : ''].filter(Boolean).join(' · ');
  return `<div class="sp-result"><span class="sp-pill sp-pill-ft">${st}</span>
    <div class="sp-score"><span>${esc(m.homeName)}</span><b>${r.homeScore}</b><i>&ndash;</i><b>${r.awayScore}</b><span>${esc(m.awayName)}</span></div>${pens}
    ${extra ? `<p class="sp-result-meta">${extra}</p>` : ''}${goals}
    <p class="sp-source-note">Result confirmed via <a href="${esc(r.source.url)}" rel="nofollow noopener">${esc(r.source.name || r.source.url)}</a>${r.verifiedOn ? ` · checked ${esc(r.verifiedOn)}` : ''}.</p></div>`;
}

function matchCentre(){
  for (const lg of LEAGUE_FIX) {
    const F = loadLeagueFixtures(lg.slug);
    const venueOf = (m) => {
      const v = (F.venues || {})[m.id] || {};
      const name = m.venue || v.name || null;
      const cap = v.capacity;
      return { name, cap };
    };
    const slug = m => m.id + '-vs-' + m.away;
    const matchUrl = m => '/sports/' + lg.slug + '/matches/' + slug(m) + '/';
    // --- per-match pages ---
    (F.matchweeks || []).forEach(w => w.matches.forEach(m => {
      const v = venueOf(m);
      const RES = resultFor(lg.slug, slug(m));
      const matchPlayed = !!RES;
      const ED = editorialFor(lg.slug, slug(m));
      /* Indexable once it is a real editorial page (preview written) or the match has a
         sourced result. Otherwise it stays a schedule entry: noindex, no sitemap. */
      const isEditorial = !!(ED || RES);
      if (!isEditorial) UNPLAYED_MATCH_PATHS.add(matchUrl(m));
      const datePublished = isoDate((ED && ED.publishedAt) || (RES && RES.playedOn), matchUrl(m) + ' datePublished');
      const dateModified = isoDate((RES && (RES.verifiedOn || RES.playedOn))
        || (ED && ED.postMatch && ED.postMatch.publishedAt)
        || (ED && (ED.updatedAt || ED.publishedAt)), matchUrl(m) + ' dateModified');
      if (isEditorial && dateModified) PAGE_LASTMOD.set(matchUrl(m), dateModified);
      const t = leagueTimeInfo(lg, m);
      let sections = (S.matchCentre.matchPageSections || []).map(s => {
        const isPost = /result after the game|post-match/i.test(s);
        return `<div class="sp-msec"><span class="sp-pend">${isPost ? 'After full-time' : 'Pending verification'}</span><b>${esc(s)}</b><p>${isPost ? 'This section is written after the match, once the result is officially confirmed.' : 'Filled in with verified data only — never predicted or fabricated.'}</p></div>`;
      }).join('');
      const reviewKey = m.id + '-vs-' + m.away;
      const review = MW1_REVIEW[reviewKey];
      if (review) {
        const base = [['Match overview',review.overview],['Recent form',review.form],['Head-to-head record','Historical and head-to-head context is included in the supplied editorial review and requires final source checking before publication.'],['Last five meetings','Recent-meeting context requires official-record verification before publication.'],['Home/away form','Home and away form context is included in the supplied editorial review and is subject to final verification.'],['Key players',review.context],['Injuries',review.injuries],['Suspensions','None reported in the supplied 14 August snapshot; reconfirm before kick-off.'],['Expected lineups','Provisional only. Recheck official team news before kick-off.'],['Tactical matchup',review.tactics],['Historical context',review.context],['Underdog discussion',review.context],['BRYME editorial outlook',review.outlook],['Editorial score prediction','BRYME editorial prediction: ' + review.prediction],['Match result after the game','Pending — complete only after the officially confirmed result.'],['Post-match analysis','Pending — complete with verified information after the match.']];
        sections = base.map(x => { const post = /result after the game|post-match/i.test(x[0]); return `<div class="sp-msec"><span class="sp-pend">${post ? 'After full-time' : 'Editorial review · 14 Aug 2026'}</span><b>${esc(x[0])}</b><p>${esc(x[1])}</p></div>`; }).join('');
      }
      const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:F.league, path:'/sports/' + lg.slug + '/'}, {name:'Match Centre', path:'/sports/' + lg.slug + '/matches/'}, {name:m.homeName + ' v ' + m.awayName, path: matchUrl(m)}];
      const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/' + lg.slug + '/')}">${esc(F.league)}</a> / <a href="${url('/sports/' + lg.slug + '/matches/')}">Match Centre</a> / ${esc(m.homeName)} v ${esc(m.awayName)}</div>
        <section class="hero"><div class="eyebrow">⚽ ${esc(F.league)} ${esc(F.season)} · ${esc(lg.roundLabel)} ${w.number}</div><h1>${esc(m.homeName)} v ${esc(m.awayName)}</h1></section>
        <div class="sp-match-hero"><img src="${lg.crest(m.id)}" alt="${lg.alt(m.id, m.homeName)}" width="64" height="77"><span class="sp-mh-vs">v</span><img src="${lg.crest(m.away)}" alt="${lg.alt(m.away, m.awayName)}" width="64" height="77"><div>${RES ? `<span class="sp-pill sp-pill-ft">${esc(RES.status || 'FT')} ${RES.homeScore}&ndash;${RES.awayScore}</span>` : `<span class="sp-pill">Upcoming — not yet played</span>`}<h1 style="margin-top:6px">${esc(m.homeName)} v ${esc(m.awayName)}</h1><p class="sp-match-meta"><span><b>Date:</b> ${esc(m.dayLabel)}</span><span><b>Kickoff:</b> ${m.time ? esc(t.display.replace(/<[^>]+>/g, '')) + (t.wat ? esc(t.wat.replace(/<[^>]+>/g, '')) : '') : 'TBC — announced closer to the round'}</span>${m.tv ? `<span><b>TV:</b> ${esc(m.tv)}</span>` : ''}<span><b>Venue:</b> ${esc(v.name || 'TBC')}${v.cap ? ' · ' + esc(Number(v.cap).toLocaleString('en-GB')) : ''}</span></p>${m.note ? `<p class="sp-match-meta" style="margin-top:6px"><b>Note:</b> ${esc(m.note)}</p>` : ''}</div></div>
        ${RES ? resultBlock(m, RES) : (ED ? '' : `<div class="sp-truth"><b>Truth first.</b><p>This match has not been played yet — there is no result, scoreline, lineup or statistic to report. Pre-match research below is an editorial review snapshot from 14 August 2026. Team news and expected lineups are provisional and must be rechecked close to kickoff. Match result and post-match analysis remain blank until official confirmation.</p></div>`)}
        ${(!RES && ED) ? `<div class="sp-truth"><b>Preview — not yet played.</b><p>This match has not been played. Everything below is pre-match editorial published on ${esc(ED.publishedAt || '')}; there is no result, lineup or statistic to report yet. Team news is only shown where a club or official source has confirmed it.</p></div>` : ''}
        ${(RES && ED && ED.postMatch) ? postMatchBlock(ED.postMatch) : ''}
        ${ED ? previewBlock(ED, {past: !!RES}) : ''}
        ${ED ? '' : `<h3 class="sp-dir">Match analysis sections</h3><div class="sp-msec-grid">${sections}</div>`}
        <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/' + lg.slug + '/fixtures/')}">Fixtures</a><a class="sp-rel" href="${url('/sports/' + lg.slug + '/results/')}">Results</a><a class="sp-rel" href="${url('/sports/' + lg.slug + '/matches/')}">Match Centre</a><a class="sp-rel" href="${url('/sports/')}">BRYME Sports</a></div></section></main>`;
      let startDate;
      const off = lg.slug === 'premier-league' ? (euDstOffset(m.date) - 1) : euDstOffset(m.date);
      if (m.time) {
        startDate = m.date + 'T' + m.time + ':00' + (off === 2 ? '+02:00' : off === 1 ? '+01:00' : '+00:00');
      } else {
        startDate = m.date;
      }
      /* A fixture that has not been played has no result, lineup or statistic to report: ~366 words
         of which all but roughly one sentence is template shared with every other fixture page.
         Submitting ~1,750 of those to Google buries the pages that do carry unique content and
         invites "Crawled - currently not indexed" across the whole site. So an unplayed fixture is
         kept for readers (kickoff time, venue, pre-match notes) but marked noindex,follow and left
         out of sitemap.xml. It becomes indexable automatically once it carries a real result. */
      write('sports/' + lg.slug + '/matches/' + slug(m), layout({
        noindex: !isEditorial,
        title: RES
          ? `${m.homeName} ${RES.homeScore}-${RES.awayScore} ${m.awayName} — Result & Analysis · ${F.league} ${F.season}`
          : (ED ? `${m.homeName} v ${m.awayName} — Preview, Form & Prediction · ${lg.roundLabel} ${w.number} · ${F.league}`
                : `${m.homeName} v ${m.awayName} — ${lg.roundLabel} ${w.number} · ${F.league} ${F.season}`),
        description: RES
          ? `${m.homeName} ${RES.homeScore}-${RES.awayScore} ${m.awayName}: full-time result, goalscorers and BRYME post-match analysis from ${F.league} ${lg.roundLabel} ${w.number}, ${F.season}.`
          : (ED ? `${m.homeName} v ${m.awayName} preview: form, head-to-head, tactical matchup and BRYME's editorial prediction for ${F.league} ${lg.roundLabel} ${w.number}${m.time ? `, kick-off ${m.time}` : ''}.`
                : `${m.homeName} v ${m.awayName}, ${F.season} ${F.league} ${lg.roundLabel} ${w.number} — ${m.dayLabel}${m.time ? ', ' + m.time + ' local' : ', kickoff TBC'}${v.name ? ' at ' + v.name : ''}. Match analysis sections appear once verified; no results are predicted.`),
        path: matchUrl(m), activeNav: 'sports',
        schema: (() => {
          const ev = [{ '@context':'https://schema.org', '@type':'SportsEvent', name: m.homeName + ' v ' + m.awayName, startDate, eventStatus: 'https://schema.org/EventScheduled', eventAttendanceMode: 'https://schema.org/OfflineEventAttendanceMode', location: v.name ? { '@type':'Place', name: v.name } : undefined, homeTeam: { '@type':'SportsTeam', name: m.homeName }, awayTeam: { '@type':'SportsTeam', name: m.awayName }, url: absUrl(matchUrl(m)) }, breadcrumbs(crumbs)];
          const sportsEvent = ev[0];
          if (RES) {
            sportsEvent.eventStatus = 'https://schema.org/EventScheduled';
            sportsEvent.homeTeam = { '@type':'SportsTeam', name: m.homeName };
            sportsEvent.awayTeam = { '@type':'SportsTeam', name: m.awayName };
          }
          if (isEditorial) {
            /* the editorial write-up itself, so datePublished/dateModified are expressed */
            ev.push({
              '@context':'https://schema.org', '@type':'Article',
              headline: RES ? `${m.homeName} ${RES.homeScore}-${RES.awayScore} ${m.awayName}: result and analysis`
                            : `${m.homeName} v ${m.awayName}: preview and prediction`,
              datePublished: datePublished || undefined,
              dateModified: dateModified || datePublished || undefined,
              author: { '@type':'Organization', name: 'BRYME Sports' },
              publisher: { '@type':'Organization', name: site.name },
              mainEntityOfPage: absUrl(matchUrl(m)),
              articleSection: F.league
            });
          }
          return ev;
        })(),
        body
      }));
      LEAGUE_MATCH_PATHS.push(matchUrl(m));
    }));
    // --- match centre hub ---
    const mw1 = (F.matchweeks && F.matchweeks[0]) || { number: 1, matches: [] };
    const heroImg = url('/assets/img/sports/hero-' + lg.slug + '.jpg');
    const cards = mw1.matches.map((m, i) => {
      const t = leagueTimeInfo(lg, m);
      const timeStr = m.time ? esc(t.display.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim()) : 'Time TBC';
      const tv = m.tv ? ' · ' + esc(m.tv) : '';
      return `<a class="sp-hero-card${i === 0 ? ' sp-hero-first' : ''}" href="${url(matchUrl(m))}" style="--card-img:url('${heroImg}')">
        <span class="sp-hero-crests"><img src="${lg.crest(m.id)}" alt="" width="26" height="32" loading="lazy"><b>v</b><img src="${lg.crest(m.away)}" alt="" width="26" height="32" loading="lazy"></span>
        <span class="sp-hero-tag">${esc(lg.roundLabel)} ${mw1.number} · ${timeStr}</span>
        <h3>${esc(m.homeName)} v ${esc(m.awayName)}</h3>
        <p>${esc(m.dayLabel)}${tv}</p>
        <span class="sp-hero-go">Match page →</span>
      </a>`;
    }).join('');
    const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:F.league, path:'/sports/' + lg.slug + '/'}, {name:'Match Centre', path:'/sports/' + lg.slug + '/matches/'}];
    const total = (F.matchweeks || []).reduce((n, w) => n + w.matches.length, 0);
    const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/' + lg.slug + '/')}">${esc(F.league)}</a> / Match Centre</div>
      <section class="hero"><div class="eyebrow">⚽ ${esc(F.league)} · Match Centre</div><h1>${esc(F.league)} ${esc(lg.roundLabel)} ${mw1.number}</h1><p class="lead">${esc(lg.roundLabel)} ${mw1.number} fixtures with dates and kick-off times from the official ${esc(F.league)} calendar. Every one of the ${total} matches in the ${esc(F.season)} season has its own match page.</p></section>
      <p class="sp-updated">Last updated: ${esc(F.lastUpdated || 'Pending verification')}</p>
      <div class="sp-truth"><b>Truth first.</b><p>Every fixture has its own match page with the officially published date${(F.matchweeks || []).some(w => w.matches.some(x => x.time)) ? ' and kick-off time' : ''}. Match analysis sections (lineups, injuries, form, result, post-match) are filled in only with verified data — never predicted or fabricated.</p></div>
      <h3 class="sp-dir">${esc(lg.roundLabel)} ${mw1.number} — ${esc([...new Set(mw1.matches.map(x => x.dayLabel))].join(' · '))}</h3>
      <section class="sp-hero" aria-label="${esc(F.league)} ${esc(lg.roundLabel)} ${mw1.number} fixtures"><div class="sp-hero-track">${cards}</div><button type="button" class="sp-hero-arrow sp-hero-prev" data-sp-hero-prev aria-label="Previous card">‹</button><button type="button" class="sp-hero-arrow sp-hero-next" data-sp-hero-next aria-label="Next card">›</button></section>
      <p class="sp-freq-note">Looking for the whole season? See <a href="${url('/sports/' + lg.slug + '/fixtures/')}">all ${total} fixtures across ${(F.matchweeks || []).length} rounds</a>.</p>
      <section class="sp-related"><h2>Match page sections</h2><p class="sp-source-note">Every match gets its own analysis page at /sports/${lg.slug}/matches/[team-a]-vs-[team-b]/ with:</p><div class="sp-rel-grid">${S.matchCentre.matchPageSections.map(s => `<span class="sp-rel sp-rel-static">${esc(s)}</span>`).join('')}</div></section>
      <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/' + lg.slug + '/fixtures/')}">Fixtures</a><a class="sp-rel" href="${url('/sports/' + lg.slug + '/results/')}">Results</a><a class="sp-rel" href="${url('/sports/transfers/' + lg.slug + '-2026-27/')}">Transfers</a><a class="sp-rel" href="${url('/sports/')}">BRYME Sports</a></div></section></main>`;
    write('sports/' + lg.slug + '/matches', layout({ title: `${F.league} ${lg.roundLabel} ${mw1.number}`, description: `${F.league} ${lg.roundLabel} ${mw1.number} — fixtures, kick-off times and match pages. All ${total} matches of the ${F.season} season have their own page; analysis sections fill in with verified data only.`, path: '/sports/' + lg.slug + '/matches/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: `${F.league} ${lg.roundLabel} ${mw1.number}`, url: absUrl('/sports/' + lg.slug + '/matches/') }, breadcrumbs(crumbs)], body }));
  }
}

/* --- PL hub: hero carousel + links --- */
function plHub(){
  const heroCards = (S.hero.cards || []).map((c, i) => `<a class="sp-hero-card${i === 0 ? ' sp-hero-first' : ''}" href="${url(c.route + '/')}" style="--card-img:url('${url('/assets/img/sports/' + (c.img || 'hero-matchweek.jpg'))}')"><span class="sp-hero-tag">${esc(c.tag)}</span><h3>${esc(c.title)}</h3><p>${esc(c.desc)}</p><span class="sp-hero-go">Read →</span></a>`).join('');
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Premier League', path:'/sports/premier-league/'}];
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / Premier League</div>
    <section class="sp-pl-hero"><div class="eyebrow">⚽ Premier League · ${SEASON}</div><h1>${esc(S.hero.kicker)}</h1><p class="lead">${esc(S.hero.subtitle)}</p></section>
    <section class="sp-hero" aria-label="Premier League matchweek ${MW} highlights"><div class="sp-hero-track">${heroCards}</div><button type="button" class="sp-hero-arrow sp-hero-prev" data-sp-hero-prev aria-label="Previous card">‹</button><button type="button" class="sp-hero-arrow sp-hero-next" data-sp-hero-next aria-label="Next card">›</button></section>
    <section class="section"><div class="section-head"><h2>Matchweek ${MW} hub</h2></div><div class="vcat-grid">
      <a class="vcat" href="${url('/sports/premier-league/matches/')}"><b>Match Centre</b><span>Matchweek ${MW} fixtures and match analysis</span></a>
      <a class="vcat" href="${url('/sports/premier-league/fixtures/')}"><b>Fixtures</b><span>Upcoming fixtures</span></a>
      <a class="vcat" href="${url('/sports/premier-league/results/')}"><b>Results</b><span>Completed results</span></a>
      <a class="vcat" href="${url('/sports/premier-league/table/')}"><b>Table</b><span>Editorial prediction + official table later</span></a>
      <a class="vcat" href="${url('/sports/fpl/')}"><b>FPL</b><span>Fantasy Premier League coverage</span></a>
      <a class="vcat" href="${url('/sports/transfers/premier-league-2026-27/')}"><b>Transfers</b><span>Premier League transfer tracker</span></a>
    </div></section>
    <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/transfers/')}">All transfer trackers</a><a class="sp-rel" href="${url('/sports/managers-2026-27/')}">Managers In &amp; Out</a><a class="sp-rel" href="${url('/sports/')}">BRYME Sports</a></div></section></main>`;
  write('sports/premier-league', layout({ title: 'Premier League ' + SEASON + ' | BRYME Sports', description: S.hero.kicker + ' — ' + S.hero.subtitle + ' Matchweek ' + MW + ' previews, transfers, FPL, injuries, fixtures, results and the BRYME editorial table prediction.', path: '/sports/premier-league/', activeNav: 'sports', schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: 'Premier League ' + SEASON, url: absUrl('/sports/premier-league/') }, breadcrumbs(crumbs)], body }));
}
/* --- league hub pages (La Liga, Serie A, Bundesliga, Ligue 1) — PL-style hero fixture cards --- */
function leagueHub(){
  for (const lg of LEAGUE_FIX.filter(l => l.slug !== 'premier-league')) {
    const F = loadLeagueFixtures(lg.slug);
    const mw1 = (F.matchweeks && F.matchweeks[0]) || { number: 1, matches: [] };
    const heroImg = url('/assets/img/sports/hero-' + lg.slug + '.jpg');
    const card = (m, i) => {
      const t = leagueTimeInfo(lg, m);
      const urlM = '/sports/' + lg.slug + '/matches/' + m.id + '-vs-' + m.away + '/';
      const timeStr = m.time ? esc(t.display.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim()) : 'Time TBC';
      const tv = m.tv ? ' · ' + esc(m.tv) : '';
      return `<a class="sp-hero-card${i === 0 ? ' sp-hero-first' : ''}" href="${url(urlM)}" style="--card-img:url('${heroImg}')">
        <span class="sp-hero-crests"><img src="${lg.crest(m.id)}" alt="" width="26" height="32" loading="lazy"><b>v</b><img src="${lg.crest(m.away)}" alt="" width="26" height="32" loading="lazy"></span>
        <span class="sp-hero-tag">${esc(lg.roundLabel)} ${mw1.number} · ${timeStr}</span>
        <h3>${esc(m.homeName)} v ${esc(m.awayName)}</h3>
        <p>${esc(m.dayLabel)}${m.venue ? ' · ' + esc(m.venue) : ''}${tv}</p>
        <span class="sp-hero-go">Match page →</span>
      </a>`;
    };
    const cards = mw1.matches.map(card).join('');
    const total = (F.matchweeks || []).reduce((n, w) => n + w.matches.length, 0);
    const rounds = (F.matchweeks || []).length;
    const kicker = F.league + ' ' + F.season;
    const subtitle = F.league + ' ' + F.season + ' — all ' + total + ' fixtures across ' + rounds + ' rounds from the official calendar. Every match has its own page with the officially published date' + ((F.matchweeks || []).some(w => w.matches.some(x => x.time)) ? ' and kick-off time' : '') + '.';
    const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:F.league, path:'/sports/' + lg.slug + '/'}];
    const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / ${esc(F.league)}</div>
      <section class="sp-pl-hero"><div class="eyebrow">⚽ ${esc(F.league)} · ${esc(F.season)}</div><h1>${esc(kicker)}</h1><p class="lead">${esc(subtitle)}</p></section>
      <section class="sp-hero" aria-label="${esc(F.league)} ${esc(lg.roundLabel)} ${mw1.number} fixtures"><div class="sp-hero-track">${cards}</div><button type="button" class="sp-hero-arrow sp-hero-prev" data-sp-hero-prev aria-label="Previous card">‹</button><button type="button" class="sp-hero-arrow sp-hero-next" data-sp-hero-next aria-label="Next card">›</button></section>
      <section class="section"><div class="section-head"><h2>${esc(lg.roundLabel)} ${mw1.number} hub</h2></div><div class="vcat-grid">
        <a class="vcat" href="${url('/sports/' + lg.slug + '/matches/')}"><b>Match Centre</b><span>${esc(lg.roundLabel)} ${mw1.number} fixtures and match analysis</span></a>
        <a class="vcat" href="${url('/sports/' + lg.slug + '/fixtures/')}"><b>Fixtures</b><span>All ${total} fixtures — dates, kickoffs &amp; match pages</span></a>
        <a class="vcat" href="${url('/sports/' + lg.slug + '/results/')}"><b>Results</b><span>Completed results</span></a>
        <a class="vcat" href="${url('/sports/transfers/' + lg.slug + '-2026-27/')}"><b>Transfers</b><span>${esc(F.league)} transfer tracker</span></a>
        <a class="vcat" href="${url('/sports/managers-2026-27/')}"><b>Managers</b><span>Managers In &amp; Out — ${F.season}</span></a>
      </div></section>
      <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/transfers/')}">All transfer trackers</a><a class="sp-rel" href="${url('/sports/managers-2026-27/')}">Managers In &amp; Out</a><a class="sp-rel" href="${url('/sports/')}">BRYME Sports</a></div></section></main>`;
    write('sports/' + lg.slug, layout({
      title: `${F.league} ${F.season}`,
      description: `${kicker} — ${F.league} ${F.season} ${lg.roundLabel} ${mw1.number} fixtures, ${total} matches across ${rounds} rounds, transfers, results and match pages from the official calendar.`,
      path: '/sports/' + lg.slug + '/', activeNav: 'sports',
      schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: `${F.league} ${F.season}`, url: absUrl('/sports/' + lg.slug + '/') }, breadcrumbs(crumbs)],
      body
    }));
  }
}

/* --- full Premier League transfer tracker (20 clubs) --- */
function buildPlTransferTracker(){
  const plPath = path.join(root, 'content', 'pl-transfers.json');
  let pl = {};
  if (fs.existsSync(plPath)) { try { pl = JSON.parse(fs.readFileSync(plPath, 'utf8')); } catch (e) { warnings.push('pl-transfers.json unreadable'); } }
  const imgUrl = id => url('/assets/img/sports/pl/' + id + '.svg');
  const statusBadge = t => t === 'Loan' ? 'sp-st-conf' : (t === 'Free' ? 'sp-st-rep' : (t === 'Released' || t === 'Retired' || t === 'Departed' ? 'sp-st-rum' : 'sp-st-conf'));
  const statusLabel = t => t === 'Confirmed' ? 'Confirmed' : t;
  const rows = list => list.length ? list.map(r => `<tr><td><b>${esc(r.player)}</b></td><td>${esc(r.from || r.to || '—')}</td><td>${esc(r.detail)}</td><td><span class="${statusBadge(r.type)}">${esc(statusLabel(r.type))}</span></td></tr>`).join('')
    : `<tr class="sp-empty"><td colspan="4">No confirmed ${esc('')}transfers listed yet — nothing is added before it is officially confirmed.</td></tr>`;
  const clubCard = c => `<article class="sp-club" id="${esc(c.id)}">
    <header class="sp-club-head"><img src="${imgUrl(c.id)}" alt="${esc(c.name)} official club crest" width="64" height="77" loading="lazy"><div><h2>${esc(c.name)}</h2><p class="sp-club-man">Manager: <b>${esc(c.manager)}</b> · ${esc(c.managerNote)}</p></div></header>
    <div class="sp-club-cols">
      <div class="sp-club-col"><h3>Players In</h3><div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Player</th><th>From</th><th>Transfer type / fee</th><th>Status</th></tr></thead><tbody>${rows(c.playersIn)}</tbody></table></div></div>
      <div class="sp-club-col"><h3>Players Out</h3><div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Player</th><th>To</th><th>Transfer type / fee</th><th>Status</th></tr></thead><tbody>${rows(c.playersOut)}</tbody></table></div></div>
    </div>
    ${(c.rumours && c.rumours.length) ? `<div class="sp-rumours"><b>Rumour / Reported interest — not confirmed</b>${c.rumours.map(r => `<p>${esc(r)}</p>`).join('')}</div>` : ''}
    ${c.notes ? `<p class="sp-club-notes"><b>Transfer notes.</b> ${esc(c.notes)}</p>` : ''}
  </article>`;
  const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Transfers', path:'/sports/transfers/'}, {name:'Premier League Transfers 2026/27', path:'/sports/transfers/premier-league-2026-27/'}];
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/transfers/')}">Transfers</a> / Premier League</div>
    <section class="hero"><div class="eyebrow">⚽ BRYME Sports · Transfers</div><h1>Premier League Transfers ${esc(pl.windowClose ? '2026/27' : '')}</h1></section>
    <div class="sp-live"><span class="sp-live-dot"></span><div><b>LIVE TRANSFER WINDOW</b><p>Premier League 2026/27 Transfers — All Clubs. This page shows the transfers completed by each Premier League club as they stand right now. The transfer window is still open, so players may move clubs, deals may be completed, and squad information may change before the transfer window closes${pl.windowClose ? ' (' + esc(pl.windowClose) + ')' : ''}. BRYME will continue updating this page as new transfers are confirmed.</p></div></div>
    <p class="sp-updated">Last updated: ${esc(pl.lastUpdated || '—')}</p>
    <div class="sp-credits"><b>Club crests</b> © Copyright The Football Association Premier League Limited, 2016. Used under the Premier League Logo Site media licence by BRYME Sports as an editorial sports publication. Crests may be resized for editorial presentation but not altered. BRYME Sports is an independent publication and is not affiliated with, endorsed or sponsored by the Premier League or any club. Other clubs' crests shown here are BRYME-generated abstract illustrations.</div>
    <p class="sp-freq-note">Transfer information changes frequently. This list is updated as new information becomes available and may not include breaking or unannounced developments.</p>
    <nav class="sp-club-nav" aria-label="Jump to club">${(pl.clubs || []).map(c => `<a href="#${esc(c.id)}">${esc(c.name.replace(' &amp; Hove Albion', '').replace('Hotspur', ''))}</a>`).join('')}</nav>
    <div class="sp-clubs">${(pl.clubs || []).map(clubCard).join('')}</div>
    <p class="sp-window-note">Transfer window still open: this page will be updated as new deals are officially confirmed.</p>
    <section class="sp-source"><h2>Sources</h2><p>${(pl.sources || []).map(esc).join(' · ')}</p><p class="sp-source-note">Transfer information is summarised in BRYME's own words. Where an external report is used, the source is named. Rumours are never presented as confirmed transfers.</p></section>
    <p class="sp-signoff">BRYME Sports — Discover what you love, learn what you need, and find what's next.</p></main>`;
  write('sports/transfers/premier-league-2026-27', layout({
    title: 'Premier League 2026/27 Transfers: All 20 Clubs, Players In & Out',
    description: 'Track every confirmed Premier League 2026/27 transfer. See players joining and leaving all 20 clubs, managers, major deals and the latest transfer updates.',
    path: '/sports/transfers/premier-league-2026-27/', activeNav: 'sports',
    schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: 'Premier League 2026/27 Transfers', description: 'Confirmed Premier League transfers for the 2026/27 season, all 20 clubs.', url: absUrl('/sports/transfers/premier-league-2026-27/') }, breadcrumbs(crumbs)],
    body
  }));
}
/* --- league transfer trackers (La Liga, Serie A, Bundesliga, Ligue 1) ---
   TRUTH-FIRST: nothing is listed until officially confirmed by a club or
   widely reported by credible outlets. Club shells are placeholders for
   verified data; the 2026/27 club composition must be confirmed. */
/* Official crest constants shared by league trackers + managers page */
const LL_NAME = { 'atletico-madrid':'atletico', 'athletic-bilbao':'athletic', 'real-betis':'betis', 'celta-vigo':'celta', 'rayo-vallecano':'rayo', 'deportivo':'deportivo', 'racing':'racing' };
const SA_OFFICIAL = ['inter','milan','juventus','napoli','roma','lazio','atalanta','bologna','fiorentina','como','genoa','sassuolo','udinese','lecce','parma','frosinone','torino','monza','venezia','cagliari'];
function buildLeagueTrackers(){
  const pathLg = path.join(root, 'content', 'league-transfers.json');
  let lgData = { leagues: [] };
  if (fs.existsSync(pathLg)) { try { lgData = JSON.parse(fs.readFileSync(pathLg, 'utf8')); } catch (e) { warnings.push('league-transfers.json unreadable'); } }
  function crestUrl(league, id){
    if (league === 'la-liga') return url('/assets/img/sports/ll/' + (LL_NAME[id] || id) + '.png');
    if (league === 'bundesliga') {
      if (id === 'hamburg') return url('/assets/img/sports/club-' + id + '.svg');
      return url('/assets/img/sports/bl/' + id + '.svg');
    }
    if (league === 'ligue-1') return url('/assets/img/sports/l1/' + id + '.webp');
    if (league === 'serie-a') {
      return url('/assets/img/sports/sa/' + id + (id === 'lazio' ? '.png' : '.svg'));
    }
    return url('/assets/img/sports/club-' + id + '.svg');
  }
  function crestAlt(league, id, name){
    if (league === 'bundesliga' && id === 'hamburg') return 'Abstract crest for ' + name + ' — BRYME-generated illustration';
    return league === 'premier-league' || ['la-liga','bundesliga','ligue-1'].includes(league) || league === 'serie-a'
      ? name + ' official club crest' : 'Abstract crest for ' + name + ' — BRYME-generated illustration';
  }
  const CREDIT_LINES = {
    'premier-league': '<b>Club crests</b> © Copyright The Football Association Premier League Limited, 2016, used under the Premier League Logo Site media licence for editorial reporting. BRYME Sports is an independent publication, not affiliated with, endorsed or sponsored by the Premier League or any club.',
    'la-liga': '<b>Club shields</b> © the respective clubs and LaLiga, obtained from the official LaLiga website (files.laliga.es) and used solely for editorial reporting on BRYME Sports. BRYME Sports is not affiliated with, endorsed or sponsored by LaLiga or any club.',
    'bundesliga': '<b>Club crests</b> © the respective clubs and the DFL, obtained from the official bundesliga.com website and used solely for editorial reporting on BRYME Sports. BRYME Sports is not affiliated with, endorsed or sponsored by the DFL/Bundesliga or any club. Crests may be resized for editorial presentation but are not altered.',
    'ligue-1': '<b>Club crests</b> © the respective clubs and the LFP, obtained from the official ligue1.com website (official marks) and used solely for editorial reporting on BRYME Sports. BRYME Sports is not affiliated with, endorsed or sponsored by the LFP/Ligue 1 or any club.',
    'serie-a': '<b>Club crests</b> © the respective clubs, retrieved from Wikimedia Commons (Wikipedia) and official club websites, and used solely for editorial reporting on BRYME Sports. BRYME Sports is not affiliated with, endorsed or sponsored by Lega Serie A or any club.'
  };
  const imgUrl = id => url('/assets/img/sports/club-' + id + '.svg');
  const statusBadge = t => t === 'Loan' ? 'sp-st-conf' : (t === 'Free' ? 'sp-st-rep' : (t === 'Released' || t === 'Retired' || t === 'Departed' ? 'sp-st-rum' : 'sp-st-conf'));
  const statusLabel = t => t === 'Confirmed' ? 'Confirmed' : t;
  const rows = (list, kind) => list && list.length ? list.map(r => `<tr><td><b>${esc(r.player)}</b></td><td>${esc(r.from || r.to || '—')}</td><td>${esc(r.detail || '—')}</td><td><span class="${statusBadge(r.type)}">${esc(statusLabel(r.type))}</span></td></tr>`).join('')
    : `<tr class="sp-empty"><td colspan="4">No confirmed ${esc(kind)} listed yet — BRYME only lists transfers that are officially confirmed by a club or widely reported by credible outlets. Nothing is invented to fill this table.</td></tr>`;
  const clubCard = (c, lgId) => `<article class="sp-club" id="${esc(c.id)}">
    <header class="sp-club-head"><img src="${crestUrl(lgId, c.id)}" alt="${crestAlt(lgId, c.id, c.name)}" width="64" height="77" loading="lazy"><div><h2>${esc(c.name)}</h2><p class="sp-club-man">Manager: <b>${esc(c.manager || 'Pending verification')}</b>${c.managerNote ? ' · ' + esc(c.managerNote) : ''}</p></div></header>
    <div class="sp-club-cols">
      <div class="sp-club-col"><h3>Players In</h3><div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Player</th><th>From</th><th>Transfer type / fee</th><th>Status</th></tr></thead><tbody>${rows(c.playersIn, 'arrivals')}</tbody></table></div></div>
      <div class="sp-club-col"><h3>Players Out</h3><div class="sp-table-wrap"><table class="sp-table"><thead><tr><th>Player</th><th>To</th><th>Transfer type / fee</th><th>Status</th></tr></thead><tbody>${rows(c.playersOut, 'departures')}</tbody></table></div></div>
    </div>
    ${(c.rumours && c.rumours.length) ? `<div class="sp-rumours"><b>Rumour / Reported interest — not confirmed</b>${c.rumours.map(r => `<p>${esc(r)}</p>`).join('')}</div>` : ''}
    ${c.notes ? `<p class="sp-club-notes"><b>Transfer notes.</b> ${esc(c.notes)}</p>` : ''}
  </article>`;
  for (const lg of lgData.leagues || []) {
    const crumbs = [{name:'Home', path:'/'}, {name:'BRYME Sports', path:'/sports/'}, {name:'Transfers', path:'/sports/transfers/'}, {name:lg.name + ' Transfers 2026/27', path:'/sports/transfers/' + lg.id + '-2026-27/'}];
    const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/sports/')}">BRYME Sports</a> / <a href="${url('/sports/transfers/')}">Transfers</a> / ${esc(lg.name)}</div>
      <section class="hero"><div class="eyebrow">⚽ BRYME Sports · Transfers</div><h1>${esc(lg.name)} Transfers 2026/27</h1></section>
      <div class="sp-live"><span class="sp-live-dot"></span><div><b>LIVE TRANSFER WINDOW</b><p>${esc(lg.name)} 2026/27 Transfers — All Clubs. This page shows the transfers completed by each club as they stand right now. The transfer window is still open, so players may move clubs, deals may be completed, and squad information may change before the transfer window closes. BRYME will continue updating this page as new transfers are confirmed.</p></div></div>
      <div class="sp-truth"><b>Truth first — nothing fabricated.</b><p>BRYME only lists transfers that are officially confirmed by the club or widely reported by credible outlets, with the source shown. Rumours are never presented as confirmed. If a transfer is uncertain, it is left out until it can be verified.</p></div>
      <p class="sp-legend-line">Status legend: <span class="sp-st-conf">Confirmed</span><span class="sp-st-rep">Loan · Free</span><span class="sp-st-rum">Released · Retired · Departed</span><span class="sp-st-rum">Rumour (never in confirmed tables)</span></p>
      <p class="sp-updated">Last updated: ${esc(lg.lastUpdated || 'Pending verification')}</p>
      ${lg.leagueNote ? `<div class="vnote" style="margin:0 0 14px">${esc(lg.leagueNote)}</div>` : ''}
      <p class="sp-freq-note">Transfer information changes frequently. This list is updated as new information becomes available and may not include breaking or unannounced developments.${lg.compositionVerified ? '' : ' Club list: based on the most recent completed season — the 2026/27 line-up (promoted/relegated clubs) must be verified before publishing.'}</p>
      <nav class="sp-club-nav" aria-label="Jump to club">${(lg.clubs || []).map(c => `<a href="#${esc(c.id)}">${esc(c.name.replace(' &amp; Hove Albion', '').replace('Hotspur', ''))}</a>`).join('')}</nav>
      <div class="sp-clubs">${(lg.clubs || []).map(c => clubCard(c, lg.id)).join('')}</div>
      <div class="sp-credits">${CREDIT_LINES[lg.id] || ''}</div>
      <p class="sp-window-note">Transfer window still open: this page will be updated as new deals are officially confirmed.</p>
      <section class="sp-source"><h2>Sources</h2><p>${(lg.sources || []).map(esc).join(' · ')}</p><p class="sp-source-note">Transfer information is summarised in BRYME's own words. Where an external report is used, the source is named. Rumours are never presented as confirmed transfers.</p></section>
      <section class="sp-related"><h2>Related</h2><div class="sp-rel-grid"><a class="sp-rel" href="${url('/sports/' + lg.id + '/fixtures/')}">Fixtures</a><a class="sp-rel" href="${url('/sports/' + lg.id + '/results/')}">Results</a><a class="sp-rel" href="${url('/sports/' + lg.id + '/matches/')}">Match Centre</a><a class="sp-rel" href="${url('/sports/managers-2026-27/')}">Managers</a></div></section>
      <p class="sp-signoff">BRYME Sports — Discover what you love, learn what you need, and find what's next.</p></main>`;
    write('sports/transfers/' + lg.id + '-2026-27', layout({
      title: lg.name + ' Transfers 2026/27: All Clubs, Players In & Out',
      description: 'Track every confirmed ' + lg.name + ' 2026/27 transfer. See players joining and leaving clubs, managers, major deals and the latest transfer updates. Only officially confirmed deals are listed.',
      path: '/sports/transfers/' + lg.id + '-2026-27/', activeNav: 'sports',
      schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name: lg.name + ' Transfers 2026/27', description: 'Confirmed ' + lg.name + ' transfers for the 2026/27 season, all clubs.', url: absUrl('/sports/transfers/' + lg.id + '-2026-27/') }, breadcrumbs(crumbs)],
      body
    }));
  }
}
/* --- execute --- */
(S.articlePlaceholders || []).forEach(sportArticlePlaceholder);
buildPlTransferTracker(); buildLeagueTrackers();
transfersHub(); managersPage(); editorialTablePage(); fplHub(); fixturesResults(); matchCentre(); plHub(); leagueHub();
// cleanup any stray non-prefixed sports pages (from earlier builds)
for (const stray of ['premier-league', 'fpl']) {
  if (fs.existsSync(path.join(root, stray)) && !['premier-league', 'fpl'].includes(stray)) {}
}
const sportsExtraPaths = [];
['sports/transfers', 'sports/managers-2026-27', 'sports/premier-league/table', 'sports/fpl', 'sports/fpl/gameweek-' + MW].forEach(p => sportsExtraPaths.push('/' + p + '/'));
['premier-league','la-liga','serie-a','bundesliga','ligue-1'].forEach(slug => ['fixtures','results','matches'].forEach(pp => sportsExtraPaths.push('/sports/' + slug + '/' + pp + '/')));
['premier-league','la-liga','serie-a','bundesliga','ligue-1'].forEach(slug => sportsExtraPaths.push('/sports/' + slug + '/'));
(S.articlePlaceholders || []).forEach(a => sportsExtraPaths.push('/sports/' + a.route + '/'));
(S.hero.cards || []).forEach(c => sportsExtraPaths.push(c.route + '/'));
S.transfers.leagues.forEach(l => sportsExtraPaths.push('/sports/transfers/' + l.id + '-2026-27/'));

/* ---------------- Type category pages (/movies/, /series/, /anime/) ---------------- */
const typeConfig = [
  { dir:'movie', pageDir:'movies', label:'Movies', title:'Movies – Discover Popular & Trending Movies', desc:n => `Browse ${n}+ films — Hollywood, Nollywood, Korean, Indian, anime films and more — with trailers, genres, years, countries and languages. Strictly movies, no series or anime mixed in.`, activeNav:'movies', seoNote:'Movie catalogue' },
  { dir:'series', pageDir:'series', label:'TV Series', title:'TV Series – Discover Popular & Trending Series', desc:n => `Browse ${n}+ TV series — American, British, Korean, African and more — with trailers, genres, years and countries. Strictly series, no movies or anime mixed in.`, activeNav:'series', seoNote:'Series catalogue' },
  { dir:'anime', pageDir:'anime', label:'Anime', title:'Anime – Discover Popular Anime, New Releases & Classics', desc:n => `Browse ${n}+ anime series and films — shonen classics, isekai, Studio Ghibli and the latest seasons — with trailers, genres and years. Strictly anime.`, activeNav:'anime', seoNote:'Anime catalogue' }
];
for (const t of typeConfig) {
  const list = movies.filter(m => m.typeDir === t.dir).sort(sortPopular);
  const tDesc = t.desc(list.length);
  const genreMapT = new Map();
  list.forEach(m => {
    const names = m.typeDir === 'movie' ? [m.genre] : m.genres;
    names.forEach(n => { if (!n) return; const s = slugify(n); if (!genreMapT.has(s)) genreMapT.set(s, {name:n, count:0}); genreMapT.get(s).count++; });
  });
  const years = [...new Set(list.map(m => m.year).filter(Boolean))].sort((a,b) => b - a);
  const countries = [...new Set(list.map(m => m.country).filter(Boolean))].sort();
  const languages = [...new Set(list.map(m => m.language).filter(Boolean))].sort();
  const embed = list.map(m => ({ s:m.slug, t:m.title, y:m.year||null, g:m.genreLabel || m.genre || '', gs:m.typeDir === 'movie' ? [m.genre] : m.genres, c:m.country||'', l:m.language||'', r:m.rating && m.rating.value != null ? m.rating.value : null, p:poster(m) }));
  const select = (id, label, options, placeholder) => `<div class="ffield"><label for="${id}">${label}</label><select id="${id}"><option value="">${placeholder}</option>${options.map(o => `<option value="${esc(o)}">${esc(o)}</option>`).join('')}</select></div>`;
  const filterBar = `<div class="filterbar" data-filterbar data-type="${t.dir}">
    <div class="ffield"><label for="f-sort">Sort</label><select id="f-sort"><option value="popular">Popular (Editorial score)</option><option value="newest">Newest</option><option value="az">A–Z</option></select></div>
    ${select('f-genre', 'Genre', [...genreMapT.values()].sort((a,b) => b.count - a.count).map(g => g.name), 'All genres')}
    ${select('f-year', 'Year', years, 'All years')}
    ${select('f-country', 'Country', countries, 'All countries')}
    ${select('f-language', 'Language', languages, 'All languages')}
    <button type="button" class="fbtn fbtn-clear" data-clear>Clear filters</button>
  </div>`;
  const json = JSON.stringify({ type:t.dir, typeLabel:t.label, items:embed }).replace(/</g, '\\u003c');
  write(t.pageDir, layout({
    title: t.title,
    description: tDesc,
    path: '/' + t.pageDir + '/',
    activeNav: t.activeNav,
    image: list[0] ? poster(list[0]) : undefined,
    schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:t.label + ' on BRYME', description:tDesc, url:url('/' + t.pageDir + '/') }, breadcrumbs([{name:'Home', path:'/'}, {name:t.label, path:'/' + t.pageDir + '/'}])],
    body: `<main class="shell"><section class="hero"><div class="eyebrow">${t.seoNote}</div><h1>${esc(t.label)}</h1><p class="lead">${esc(tDesc)}</p></section><section class="section"><h2>Browse ${esc(t.label.toLowerCase())}</h2>${filterBar}<p class="count-line" data-count>${list.length} ${t.label.toLowerCase()} in the catalogue</p>${progressiveGrid(list, 40)}</section><script id="catalogue-data" type="application/json">${json}<\/script></main>`
  }));
}

/* ---------------- Per-type genre pages ---------------- */
/* A listing with fewer than this many items adds nothing over its parent page:
   noindexed and kept out of the sitemap until it fills up. Self-healing. */
const THIN_ARCHIVE_MIN = 3;            // below this an archive is noindexed and left out of the sitemap
const thinArchive = list => (list || []).length < THIN_ARCHIVE_MIN;
const THIN_LISTING_PATHS = new Set();
const genreIndexByType = { movie: new Map(), series: new Map(), anime: new Map() };
for (const t of typeConfig) {
  const list = movies.filter(m => m.typeDir === t.dir);
  const map = genreIndexByType[t.dir];
  list.forEach(m => {
    const names = m.typeDir === 'movie' ? [m.genre] : m.genres;
    names.forEach(n => { if (!n) return; const s = slugify(n); if (!map.has(s)) map.set(s, {name:n, items:[]}); map.get(s).items.push(m); });
  });
  const titleSlugs = new Set(list.map(m => m.slug));
  for (const [s, g] of map) {
    if (titleSlugs.has(s)) { warnings.push(`genre page /${t.dir}/${s}/ collides with a title page slug — skipped`); continue; }
    const items = [...g.items].sort(sortPopular);
    const genreLabel = t.dir === 'movie' ? 'movies' : (t.dir === 'series' ? 'series' : 'anime');
    if (thinArchive(items)) THIN_LISTING_PATHS.add(`/${t.pageDir}/${s}/`);
    write(`${t.pageDir}/${s}`, layout({
      noindex: thinArchive(items),
      title: `${g.name} ${genreLabel} – Browse & Discover`,
      description: `Explore ${g.name.toLowerCase()} ${genreLabel} in the BRYME catalogue: trailers, years, countries and editorial information. ${items.length} ${genreLabel} in this collection.`,
      path: `/${t.pageDir}/${s}/`,
      activeNav: t.activeNav, image: items[0] ? poster(items[0]) : undefined,
      schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:`${g.name} ${genreLabel}`, description:`${g.name} ${genreLabel} on BRYME.`, url:url(`/${t.pageDir}/${s}/`) }, breadcrumbs([{name:'Home', path:'/'}, {name:t.label, path:'/' + t.pageDir + '/'}, {name:g.name, path:`/${t.pageDir}/${s}/`}])],
      body: `<main class="shell"><div class="crumb"><a href="${url('/genres/')}">Genres</a> / <a href="${url('/' + t.pageDir + '/')}">${esc(t.label)}</a> / ${esc(g.name)}</div><section class="hero"><div class="eyebrow">${esc(t.label)} genre</div><h1>${esc(g.name)} ${esc(genreLabel)}</h1><p class="lead">${items.length} ${genreLabel} in this collection — strictly ${esc(t.label.toLowerCase())}, nothing else mixed in.</p></section><section class="section">${progressiveGrid(items, 36)}</section></main>`
    }));
  }
}

/* ---------------- Genres hub ---------------- */
const genreHubPanels = typeConfig.map(t => {
  const list = movies.filter(m => m.typeDir === t.dir);
  const map = genreIndexByType[t.dir];
  const chips = [...map.values()].sort((a,b) => b.items.length - a.items.length)
    .map(g => `<a href="${url('/' + t.pageDir + '/' + slugify(g.name) + '/')}">${esc(g.name)}<b>${g.items.length}</b></a>`).join('');
  return `<div class="genre-panel"><h3>${t.dir === 'movie' ? '🎬' : (t.dir === 'series' ? '📺' : '🍥')} ${esc(t.label)} genres <span class="gp-count">${list.length} ${t.label.toLowerCase()}</span></h3><div class="genre-chips">${chips}</div></div>`;
}).join('');
write('genres', layout({
  title: 'Genres – Movie, Series & Anime categories',
  description: 'Browse BRYME genres with strict content-type separation: movie genres, TV series genres and anime genres each have their own category pages.',
  path: '/genres/', activeNav: 'genres',
  schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:'BRYME genres', url:url('/genres/') }],
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Browse by category</div><h1>Genres, separated by type.</h1><p class="lead">Every genre page is scoped to a single content type — movie genres never contain series, and anime genres never contain movies.</p></section><section class="section"><div class="genre-trio">${genreHubPanels}</div></section><section class="section"><h2>Legacy movie genre pages</h2><p class="lead">The original genre routes remain available: <a class="quiet-link" href="${url('/genre/action/')}">Action</a>, <a class="quiet-link" href="${url('/genre/horror/')}">Horror</a>, <a class="quiet-link" href="${url('/genre/sci-fi/')}">Sci-Fi</a> and <a class="quiet-link" href="${url('/genre/comedy/')}">Comedy</a>.</p></section></main>`
}));

/* ---------------- Legacy /genre/ pages (movie-only, canonical to /movies/{genre}/) ---------------- */
for (const [s, g] of genreIndexByType.movie) {
  if (!fs.existsSync(path.join(root, 'genre', s))) continue;
  const items = [...g.items].sort(sortPopular);
  write(`genre/${s}`, layout({
    title: `${g.name} movies – Browse & Discover`,
    description: `Explore ${g.name.toLowerCase()} movies in the BRYME catalogue: trailers, years and editorial information.`,
    path: `/genre/${s}/`, canonical: `/movies/${s}/`, activeNav: 'movies',
    schema: { '@context':'https://schema.org', '@type':'CollectionPage', name:`${g.name} movies`, url:url(`/genre/${s}/`) },
    body: `<main class="shell"><div class="crumb"><a href="${url('/genres/')}">Genres</a> / ${esc(g.name)}</div><section class="hero"><div class="eyebrow">Genre</div><h1>${esc(g.name)} movies</h1><p class="lead">A curated selection from the existing BRYME movie catalogue. The canonical version of this page lives at <a class="quiet-link" href="${url('/movies/' + s + '/')}">${esc(g.name)} movies</a>.</p></section><section class="section">${progressiveGrid(items, 36)}</section></main>`
  }));
}
// Stale mixed-content legacy genre pages (no inbound links) are removed,
// plus any artifacts wrongly generated under the singular /movie/ dir.
for (const stale of ['genre/anime', 'genre/series', 'movie/index.html']) {
  if (fs.existsSync(path.join(root, stale))) { fs.rmSync(path.join(root, stale), {recursive:true, force:true}); warnings.push(`removed stale mixed-content page ${stale}/`); }
}
for (const s of genreIndexByType.movie.keys()) {
  const wrong = path.join(root, 'movie', s);
  if (fs.existsSync(wrong)) { fs.rmSync(wrong, {recursive:true, force:true}); warnings.push(`removed mis-placed genre page movie/${s}/ (now at movies/${s}/)`); }
}

/* ---------------- Years (per content type) ---------------- */
const yearMap = new Map();        // movies  -> /year/{y}/
const seriesYearMap = new Map();  // series  -> /series/{y}/
const animeYearMap = new Map();   // anime   -> /anime/{y}/
movies.forEach(m => {
  if (!m.year) return;
  const map = m.typeDir === 'movie' ? yearMap : (m.typeDir === 'series' ? seriesYearMap : animeYearMap);
  if (!map.has(m.year)) map.set(m.year, []);
  map.get(m.year).push(m);
});
const yearChip = (map, base, label) => [...map.keys()].sort((a, b) => b - a)
  .map(y => `<a href="${url('/' + base + '/' + y + '/')}">${y} <b>${map.get(y).length}</b></a>`).join('');
write('years', layout({
  title: 'Browse by year — Movies, Series & Anime',
  description: 'Browse BRYME years with strict content-type separation: movies by year, TV series by year and anime by year each have their own index.',
  path: '/years/', activeNav: 'years',
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Browse by year</div><h1>Years, separated by type.</h1><p class="lead">Series and anime are never mixed into the movie year index. Each type has its own year pages.</p></section><section class="section"><div class="genre-trio"><div class="genre-panel"><h3>🎬 Movies <span class="gp-count">${yearMap.size} years</span></h3><div class="genre-chips">${yearChip(yearMap, 'year', 'movies')}</div></div><div class="genre-panel"><h3>📺 Series <span class="gp-count">${seriesYearMap.size} years</span></h3><div class="genre-chips">${yearChip(seriesYearMap, 'series', 'series')}</div></div><div class="genre-panel"><h3>🍥 Anime <span class="gp-count">${animeYearMap.size} years</span></h3><div class="genre-chips">${yearChip(animeYearMap, 'anime', 'anime')}</div></div></div></section></main>`
}));
for (const [year, list] of yearMap) write(`year/${year}`, layout({
  title: `Movies from ${year}`, description: `Explore movies from ${year} in the BRYME catalogue.`, path: `/year/${year}/`, noindex: thinArchive(list), activeNav: 'movies', image: list[0] ? poster(list[0]) : undefined,
  body: `<main class="shell"><div class="crumb"><a href="${url('/years/')}">Years</a> / <a href="${url('/movies/')}">Movies</a> / ${year}</div><section class="hero"><div class="eyebrow">Year · Movies</div><h1>Movies from ${year}</h1></section><section class="section">${progressiveGrid(list, 36)}</section></main>`
}));
for (const [year, list] of seriesYearMap) write(`series/${year}`, layout({
  title: `Series from ${year}`, description: `Explore TV series from ${year} in the BRYME catalogue.`, path: `/series/${year}/`, noindex: thinArchive(list), activeNav: 'series', image: list[0] ? poster(list[0]) : undefined,
  body: `<main class="shell"><div class="crumb"><a href="${url('/years/')}">Years</a> / <a href="${url('/series/')}">Series</a> / ${year}</div><section class="hero"><div class="eyebrow">Year · Series</div><h1>Series from ${year}</h1></section><section class="section">${progressiveGrid(list, 36)}</section></main>`
}));
for (const [year, list] of animeYearMap) write(`anime/${year}`, layout({
  title: `Anime from ${year}`, description: `Explore anime from ${year} in the BRYME catalogue.`, path: `/anime/${year}/`, noindex: thinArchive(list), activeNav: 'anime', image: list[0] ? poster(list[0]) : undefined,
  body: `<main class="shell"><div class="crumb"><a href="${url('/years/')}">Years</a> / <a href="${url('/anime/')}">Anime</a> / ${year}</div><section class="hero"><div class="eyebrow">Year · Anime</div><h1>Anime from ${year}</h1></section><section class="section">${progressiveGrid(list, 36)}</section></main>`
}));

/* ---------------- Rankings hub (/trending/) ---------------- */
const trendTopMovie = trendingByType.movie.slice(0, 24);
const trendTopSeries = trendingByType.series.slice(0, 24);
const trendTopAnime = trendingByType.anime.slice(0, 24);
const popularTop = [...popularByType.movie, ...popularByType.series, ...popularByType.anime].slice(0, 36);
const editorTop = editorPicksList.slice(0, 12);
const newTop = (newReleases.length >= 8 ? newReleases : movies.filter(m => m.year).sort(sortNewest)).slice(0, 24);
const classicTop = classics.slice(0, 24);
write('trending', layout({
  title: 'Trending, Popular, Editor\'s Picks & New Releases',
  description: 'BRYME\'s editorial rankings: trending (curated per content type), popular, editor\'s picks, new releases and classics. No fake view counts.',
  path: '/trending/', activeNav: 'trending',
  schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:'Trending & Popular on BRYME', url:url('/trending/') }],
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Editorial rankings</div><h1>Trending, Popular &amp; Picks</h1><p class="lead">Four independent concepts, curated by the BRYME editorial team. No fake view counts, no live-traffic claims — real analytics will plug in here later.</p></section>
  <div class="trend-note"><b style="color:var(--text)">How Trending Now works.</b><br>Trending Now is an <b>editorially curated list</b> (managed in content/rankings.json). It is NOT derived from ratings, recency or traffic. When BRYME has real user activity, Trending can switch to: recent engagement + growth rate + searches + clicks + recency — without changing the site architecture.</div>
  <section class="section" id="trending-now"><div class="section-head"><h2>🔥 Trending Movies</h2></div><p class="section-note">Curated by the editorial team.</p><div class="grid grid-2">${trendTopMovie.map((m,i) => card(m, {rank: m.trendingRank})).join('') || '<p style="color:var(--muted)">No trending movies configured yet.</p>'}</div></section>
  <section class="section"><div class="section-head"><h2>🔥 Trending Series</h2></div><p class="section-note">Curated by the editorial team.</p><div class="grid grid-2">${trendTopSeries.map((m,i) => card(m, {rank: m.trendingRank})).join('') || '<p style="color:var(--muted)">No trending series configured yet.</p>'}</div></section>
  <section class="section"><div class="section-head"><h2>🔥 Trending Anime</h2></div><p class="section-note">Curated by the editorial team.</p><div class="grid grid-2">${trendTopAnime.map((m,i) => card(m, {rank: m.trendingRank})).join('') || '<p style="color:var(--muted)">No trending anime configured yet.</p>'}</div></section>
  <section class="section" id="editors-picks"><div class="section-head"><h2>👑 Editor\'s Picks</h2></div><p class="section-note">Personal recommendations from the BRYME desk — independent of trending and popularity.</p><div class="grid grid-2">${editorTop.map(m => card(m)).join('') || '<p style="color:var(--muted)">No editor\'s picks configured yet.</p>'}</div></section>
  <section class="section"><div class="section-head"><h2>⭐ Popular</h2></div><p class="section-note">Evergreen favourites, editorially ranked per content type.</p><div class="grid">${popularTop.map(card).join('')}</div></section>
  <section class="section" id="new-releases"><div class="section-head"><h2>🆕 New Releases</h2></div><p class="section-note">Newest verified release years (${CURRENT_YEAR - 2}–${CURRENT_YEAR}). Older titles are never re-labelled as new.</p><div class="grid">${newTop.map(card).join('')}</div></section>
  <section class="section" id="classics"><div class="section-head"><h2>🎞️ Classics</h2></div><p class="section-note">Titles from 2000 and earlier, ranked by editorial score.</p><div class="grid">${classicTop.map(card).join('')}</div></section></main>`
}));

/* ---------------- Search ---------------- */
const searchEmbed = JSON.stringify({ movies: searchIndex.movies, articles: searchIndex.articles, topics: searchIndex.topics }).replace(/</g, '\\u003c');
write('search', layout({
  title: 'Search Movies, TV Series & Anime',
  description: 'Search across BRYME — movies, TV series, anime, sports, memes, money guides and tech — every result is labelled with its vertical.',
  path: '/search/', noindex: true,
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Global search</div><h1>What are you looking for?</h1><p class="lead">Search movies, TV series, anime, sports, memes, money guides and tech & AI. Every result shows its vertical.</p></section><section class="section"><input class="searchbox" id="search-q" autocomplete="off" placeholder="Try Dune, Breaking Bad, One Piece, Horror, 2024…"><p class="searchnote" id="search-status"></p><div class="search-tabs" id="search-tabs"><button type="button" class="stabs active" data-tab="all">All</button><button type="button" class="stabs" data-tab="movie">🎬 Movies</button><button type="button" class="stabs" data-tab="series">📺 Series</button><button type="button" class="stabs" data-tab="anime">🍥 Anime</button><button type="button" class="stabs" data-tab="article">📰 Articles</button></div><div class="grid" id="search-results"></div></section><script id="search-data" type="application/json">${searchEmbed}<\/script></main>`
}));

/* ---------------- Title pages ---------------- */
function relatedArticlesFor(m){
  if (!m.relatedMovieSlugs) return [];
  return (m.relatedMovieSlugs || []).map(slug => articles.find(a => a.slug === slug)).filter(Boolean).slice(0, 3);
}
articles.forEach(a => a.relatedMovieSlugs = a.relatedMovieSlugs || []);
const articleToMovies = new Map();
articles.forEach(a => { (a.relatedMovieSlugs || []).forEach(slug => { const m = slugIndex.get(slug); if (m) { if (!articleToMovies.has(m.slug)) articleToMovies.set(m.slug, []); articleToMovies.get(m.slug).push(a); } }); });

/* ================================================================
   TITLE PAGES — premium individual pages
   Related-title algorithm (deterministic):
   manual editorial relationship (+100) + shared genres + same era
   (±3 years) + editorial rating. Same type always required.
   ================================================================ */
const titleRelationsPath = path.join(root, 'content', 'title-relationships.json');
let titleRelations = {};
if (fs.existsSync(titleRelationsPath)) {
  try { titleRelations = JSON.parse(fs.readFileSync(titleRelationsPath, 'utf8')); } catch (e) { warnings.push('title-relationships.json unreadable'); }
}
// Normalise manual relationships: titleRelations[slug] may be a plain array
// (legacy) or { relatedTitles: [...] } — the spec's optional relatedTitles form.
const REL = {};
for (const [from, val] of Object.entries(titleRelations)) {
  if (from === '_comment') continue;
  if (!slugIndex.has(from)) { warnings.push(`title-relationships.json: unknown key slug "${from}"`); continue; }
  const list = Array.isArray(val) ? val : (val && Array.isArray(val.relatedTitles) ? val.relatedTitles : []);
  if (!Array.isArray(val) && !(val && Array.isArray(val.relatedTitles))) warnings.push(`title-relationships.json: invalid value for "${from}"`);
  REL[from] = list;
  list.forEach(t => { if (!slugIndex.has(t)) warnings.push(`title-relationships.json: unknown related slug "${t}" (from ${from})`); });
}
// Distinctive genres carry more signal than generic ones (Survival vs Action).
const COMMON_GENRES = new Set(['action', 'adventure', 'comedy', 'drama', 'fantasy', 'sci-fi', 'thriller', 'romance', 'crime', 'horror', 'animation', 'family']);
const DISTINCTIVE_WEIGHT = 6, COMMON_WEIGHT = 2;
function genreWeight(g) { return COMMON_GENRES.has(slugify(g)) ? COMMON_WEIGHT : DISTINCTIVE_WEIGHT; }
function relatedFor(m) {
  const typeDir = m.typeDir || 'movie';
  const manual = new Set(REL[m.slug] || []);
  const mGenres = typeDir === 'movie' ? [m.genre].filter(Boolean) : (m.genres || []);
  return movies
    .filter(x => x.id !== m.id && (x.typeDir || 'movie') === typeDir)
    .map(x => {
      let score = 0;
      if (manual.has(x.slug)) score += 100; // manual editorial relationship
      const xGenres = typeDir === 'movie' ? [x.genre].filter(Boolean) : (x.genres || []);
      for (const g of mGenres) if (xGenres.includes(g)) score += genreWeight(g); // strong genre/theme match beats popularity
      if (x.country && m.country && x.country === m.country) score += 2;
      if (x.language && m.language && x.language === m.language) score += 1;
      if (x.year && m.year && Math.abs(x.year - m.year) <= 3) score += 1;
      if (x.rating && x.rating.value != null) score += x.rating.value / 10; // popularity tiebreak only
      return { x, score };
    })
    .sort((a, b) => (b.score - a.score) || ((b.x.rating?.value || 0) - (a.x.rating?.value || 0)) || ((b.x.year || 0) - (a.x.year || 0)) || a.x.title.localeCompare(b.x.title))
    .slice(0, 8)
    .map(r => r.x);
}
/* Seasons (series/anime only, optional) — architecture for future season data.
   Source: content/seasons.json (or a future catalogue field). Nothing is
   invented; if no seasons are recorded, no Seasons section is rendered. */
const seasonsPath = path.join(root, 'content', 'seasons.json');
let seasonsData = {};
if (fs.existsSync(seasonsPath)) {
  try { seasonsData = JSON.parse(fs.readFileSync(seasonsPath, 'utf8')); } catch (e) { warnings.push('seasons.json unreadable'); }
}
movies.forEach(m => {
  let seasons = seasonsData[m.slug] || [];
  if (!Array.isArray(seasons)) seasons = [];
  seasons = seasons.filter(x => x && typeof x === 'object').map(x => ({
    seasonNumber: Number(x.seasonNumber) || null,
    title: x.title ? clean(x.title) : null,
    year: Number(x.year) || null,
    episodeCount: Number(x.episodeCount) || null
  })).filter(x => x.seasonNumber != null);
  m.seasons = (m.typeDir === 'movie') ? [] : seasons;
  m.numberOfSeasons = m.seasons.length || null;
  m.numberOfEpisodes = m.seasons.reduce((sum, x) => sum + (x.episodeCount || 0), 0) || null;
});

for (const m of movies) {
  const typeDir = m.typeDir || 'movie';
  const label = m.typeLabel;
  const schemaType = typeDir === 'series' ? 'TVSeries' : (typeDir === 'anime' ? (animeFilms.has(m.slug) ? 'Movie' : 'TVSeries') : 'Movie');
  const typeWord = typeDir === 'series' ? 'Series Overview' : (typeDir === 'anime' ? 'Anime Overview' : 'Movie Overview');
  const seoTitle = m.year ? `${m.title} (${m.year}) – ${typeWord}, Trailer & BRYME` : `${m.title} – ${typeWord}, Trailer & BRYME`;
  const genreText = m.genres.length ? m.genres[0] : (m.genre || '');
  const seoDesc = `Explore ${m.title}${m.year ? ' (' + m.year + ')' : ''} on BRYME — a ${m.typeLabel.toLowerCase()}${genreText ? ' ' + genreText.toLowerCase() : ''} overview with trailer, key details, related titles and our editorial take.`;
  const relatedArts = (articleToMovies.get(m.slug) || []).slice(0, 2);
  const schema = { '@context':'https://schema.org', '@type':schemaType, name:m.title, description:m.description || m.teaser || undefined, dateCreated:m.year ? String(m.year) : undefined, genre:(m.genres[0] || m.genre) || undefined, sameAs:m.trailer || undefined, image: poster(m) || undefined };
  if (m.country) schema.countryOfOrigin = m.country;
  if (m.language) schema.inLanguage = m.language;
  /* Verified credits (Wikidata/Wikipedia overlay) — only emitted when real. */
  if (m.director) {
    const directors = m.director.split(';').map(d => d.trim()).filter(Boolean);
    if (directors.length) schema.director = directors.map(name => ({ '@type':'Person', name }));
  }
  if (m.cast && m.cast.length) schema.actor = m.cast.map(name => ({ '@type':'Person', name }));
  if (m.runtime) {
    const mins = parseInt(String(m.runtime).replace(/[^0-9]/g, ''), 10);
    if (mins > 0) schema.duration = `PT${mins}M`;
  }
  if (schemaType === 'TVSeries' && m.year) schema.startDate = String(m.year);
  if (schemaType === 'TVSeries' && m.numberOfSeasons) schema.numberOfSeasons = m.numberOfSeasons;
  if (schemaType === 'TVSeries' && m.numberOfEpisodes) schema.numberOfEpisodes = m.numberOfEpisodes;
  if (relatedArts.length) schema.about = relatedArts.map(a => ({ '@type':'Article', name:a.title, url:url('/article/' + a.slug + '/') }));
  Object.keys(schema).forEach(k => schema[k] === undefined && delete schema[k]);
  const pagePath = `/${typeDir}/${m.slug}/`;
  const yearPath = typeDir === 'movie' ? '/year/' + m.year + '/' : '/' + typeDir + '/' + m.year + '/';
  const yearLabel = m.year ? (typeDir === 'movie' ? m.year + ' movies' : (typeDir === 'series' ? m.year + ' series' : m.year + ' anime')) : null;
  const crumbs = [{name:'Home', path:'/'}, {name: label === 'TV Series' ? 'TV Series' : (label === 'Anime' ? 'Anime' : 'Movies'), path: '/' + (typeDir === 'movie' ? 'movies' : typeDir) + '/'}];
  if (m.year) crumbs.push({name: String(m.year), path: yearPath});
  const genreBadges = [];
  if (typeDir === 'movie' && m.genre) genreBadges.push(`<a class="badge" href="${url('/movies/' + slugify(m.genre) + '/')}">${esc(m.genre)}</a>`);
  else (m.genres || []).forEach(g => { genreBadges.push(`<a class="badge" href="${url('/' + typeDir + '/' + slugify(g) + '/')}">${esc(g)}</a>`); crumbs.push({name:g, path:`/${typeDir}/${slugify(g)}/`}); });
  const schemaList = [schema, breadcrumbs(crumbs)];
  // VideoObject structured data is emitted ONLY when the primary trailer is a
  // verified official video whose title we actually know from oEmbed. No
  // fabricated upload dates, durations or creators.
  if (m.trailers.length && m.trailerType && m.trailerType !== 'fan-made' && m.trailerVerified) {
    const t0 = m.trailers[0];
    schemaList.push({ '@context':'https://schema.org', '@type':'VideoObject', name: t0.videoTitle || `${m.title} official trailer`, description: `Official trailer for ${m.title}.`, thumbnailUrl: `https://i.ytimg.com/vi/${t0.videoId}/hqdefault.jpg`, embedUrl: `https://www.youtube-nocookie.com/embed/${t0.videoId}`, uploadDate: t0.lastChecked ? t0.lastChecked : undefined, publisher: t0.channel ? { '@type':'Organization', name: t0.channel } : undefined });
    Object.keys(schemaList[schemaList.length - 1]).forEach(k => schemaList[schemaList.length - 1][k] === undefined && delete schemaList[schemaList.length - 1][k]);
  }
  crumbs.push({name:m.title, path:pagePath});
  const related = relatedFor(m);
  const relatedArticles = (articleToMovies.get(m.slug) || []).slice(-4).reverse(); // newest-connected first
  write(`${typeDir}/${m.slug}`, layout({
    title: seoTitle,
    description: (m.description || '').length >= 80 ? (m.description || seoDesc).slice(0, 158) : seoDesc,
    path: pagePath,
    activeNav: typeDir === 'movie' ? 'movies' : (typeDir === 'series' ? 'series' : 'anime'),
    schema: schemaList,
    image: poster(m),
    body: `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/' + (typeDir === 'movie' ? 'movies' : typeDir) + '/')}">${esc(typeDir === 'movie' ? 'Movies' : label)}</a>${m.year ? ` / <a href="${url(yearPath)}">${m.year}</a>` : ''} / ${esc(m.title)}</div>
  <section class="movie-hero" style="--movie-backdrop:url('${esc(poster(m))}')">
    ${image(m)}
    <div>
      <div class="hero-kicker"><span class="type-badge tb-${typeDir}">${typeDir === 'series' ? 'SERIES' : (typeDir === 'anime' ? 'ANIME' : 'MOVIE')}</span>${m.year ? `<span>${m.year}</span>` : ''}${m.genres.length ? `<span class="dot">·</span><span>${m.genres.map(esc).join(' · ')}</span>` : ''}</div>
      <h1>${esc(m.title)}</h1>
      <div class="badges">${m.rating && m.rating.value != null ? `<span class="badge" title="BRYME editorial score — not IMDb, Rotten Tomatoes or audience ratings">★ ${esc(String(m.rating.value))}/10 · BRYME Editorial</span>` : ''}${m.trending ? `<span class="badge" title="Editorially curated — not live traffic data">🔥 Trending #${m.trendingRank}</span>` : ''}${m.popular ? `<span class="badge" title="Editorial popular pick">⭐ Popular</span>` : ''}${m.editorPick ? `<span class="badge" title="BRYME editor's recommendation">👑 Editor's Pick</span>` : ''}</div>
      <p class="lead">${esc(m.description || m.teaser || 'Information is being added for this title.')}</p>
      <div class="hero-actions"><a class="cta" href="#trailer">WATCH TRAILER</a>${relatedArticles.length ? `<a class="cta cta-ghost" href="${url('/article/' + relatedArticles[0].slug + '/')}">READ BRYME STORY</a>` : ''}<button class="quiet-link share-action" type="button" data-share-path="${pagePath}" data-share-title="${esc(m.title)}">Share</button></div>
    </div>
  </section>
  <section class="shell trailer-section" id="trailer">${trailerSection(m)}</section>
  <section class="body">
    <article class="prose">
      ${(() => {
        /* Only render an About section when it says something the hero synopsis did not.
           Previously this reprinted m.description verbatim under a heading on 71% of title
           pages - padding that reads as filler and adds no information for a reader or a
           crawler. If a longer in-house synopsis is written later it appears here
           automatically; otherwise the page relies on the hero synopsis and the verified
           Details block below. */
        const long = m.longDescription || m.synopsis || m.about || '';
        const lead = (m.description || '').trim();
        if (long && long.trim() !== lead) {
          return `<h2>About ${esc(m.title)}</h2>` + long.trim().split(/\n{2,}/).map(t => `<p>${esc(t.trim())}</p>`).join('');
        }
        if (!lead) return `<h2>About ${esc(m.title)}</h2><p>A full synopsis is not currently available for this title.</p>`;
        return '';
      })()}
      ${m.facts.length ? `<h2>Notes</h2><ul>${m.facts.map(f => `<li>${esc(f)}</li>`).join('')}</ul>` : ''}
      ${(typeDir !== 'movie' && m.seasons.length) ? `<h2>Seasons</h2><div class="list">${m.seasons.map(x => `<div class="row"><div><b>${esc(x.title || ('Season ' + x.seasonNumber))}</b><span class="meta" style="font-size:12px;color:var(--muted)">${x.year ? x.year + ' · ' : ''}${x.episodeCount ? x.episodeCount + ' episodes' : 'episode count unavailable'}</span></div></div>`).join('')}</div>` : ''}
      <h2>You may also like</h2>
      ${related.length ? `<div class="grid">${related.map(card).join('')}</div>` : '<p>Related titles are not available yet.</p>'}
      ${relatedArticles.length ? `<h2>Latest stories about ${esc(m.title)}</h2><div class="story-grid story-grid-title">${relatedArticles.map(a => `<a href="${url('/article/' + a.slug + '/')}"><span>${esc(a.category)}</span><h3>${esc(a.title)}</h3><p>${esc(a.description.slice(0, 140))}</p><b>READ ARTICLE →</b></a>`).join('')}</div>` : ''}
    </article>
    <aside class="aside">
      <h2>Details</h2>
      <dl><dt>Type</dt><dd>${esc(label)}</dd><dt>Year</dt><dd>${m.year || 'Information unavailable'}</dd><dt>Genre</dt><dd>${m.genres.length ? m.genres.map(g => `<a href="${url('/' + typeDir + '/' + slugify(g) + '/')}">${esc(g)}</a>`).join(', ') : (esc(m.genre || 'Information unavailable'))}</dd>${m.country ? `<dt>Country</dt><dd>${esc(m.country)}</dd>` : ''}${m.language ? `<dt>Language</dt><dd>${esc(m.language)}</dd>` : ''}${m.runtime ? `<dt>Runtime</dt><dd>${esc(m.runtime)}</dd>` : ''}${m.director ? `<dt>Director</dt><dd>${esc(m.director)}</dd>` : ''}${m.cast && m.cast.length ? `<dt>Cast</dt><dd>${m.cast.map(esc).join('; ')}</dd>` : ''}<dt>Year index</dt><dd><a href="${url(yearPath)}">${esc(yearLabel)}</a></dd>${m.trending ? `<dt>Trending</dt><dd>🔥 #${m.trendingRank} (editorially curated)${m.trendingUntil ? ` · until ${m.trendingUntil}` : ''}</dd>` : ''}${m.popular ? `<dt>Popular</dt><dd>⭐ #${m.popularRank} (editorial popular pick)</dd>` : ''}${m.editorPick ? `<dt>Editor's Pick</dt><dd>👑 #${m.editorPickRank}${m.editorPickNote ? ` — ${esc(m.editorPickNote)}` : ''}</dd>` : ''}</dl>
      ${m.metaSource ? `<p class="meta-source">Director, runtime, country and language from <a href="${esc(m.metaSource.url)}" rel="nofollow noopener">Wikidata</a>${m.castSource && m.castSource.url ? `; billed cast from <a href="${esc(m.castSource.url)}" rel="nofollow noopener">Wikipedia</a>` : ''}${m.metaSource.retrieved ? ` · retrieved ${esc(m.metaSource.retrieved)}` : ''}. BRYME's synopsis and editorial score are written in-house.</p>` : ''}
    </aside>
  </section></main>`
  }));
  if (typeDir !== 'movie') {
    write(`movie/${m.slug}`, layout({
      title: seoTitle, description: m.description || m.teaser || seoDesc, path: `/movie/${m.slug}/`, canonical: pagePath, noindex: true, image: poster(m),
      body: `<main class="shell" style="padding-top:80px;text-align:center"><p>This title has moved. <a href="${url(pagePath)}">View ${esc(m.title)}</a>.</p></main><meta http-equiv="refresh" content="0;url=${url(pagePath)}">`
    }));
  }
}

/* ---------------- Articles & topics ---------------- */
function articleBlocks(article) {
  if (article.blocks && article.blocks.length) return article.blocks.map(block => {
    const text = esc(block.text);
    if (block.type === 'heading') return `<h2>${text}</h2>`;
    if (block.type === 'quote') return `<blockquote>${text}</blockquote>`;
    if (block.type === 'source') return `<p class="article-source">${text}</p>`;
    return `<p>${text}</p>`;
  }).join('');
  return (article.items || []).map(item => `<h2>${esc(item.heading)}</h2><p>${esc(item.body)}</p>`).join('');
}
function articleWordCount(article) {
  const text = article.blocks && article.blocks.length ? article.blocks.map(b => b.text).join(' ') : (article.items || []).map(i => i.heading + ' ' + i.body).join(' ');
  return text.trim().split(/\s+/).filter(Boolean).length;
}
write('articles', layout({
  title: 'Editorial – Movie, Series & Anime guides',
  description: 'Original editorial from BRYME: movie lists, explainers and guides that link back to the catalogue.',
  path: '/articles/', activeNav: 'articles',
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Editorial</div><h1>Stories behind the screen.</h1><p class="lead">Original guides and lists — separate from the catalogue, and always linking back to the movies, series and anime they talk about.</p></section><section class="section"><div class="list">${articles.map(articleRow).join('')}</div></section></main>`
}));
for (const a of articles) {
  const relatedMovies = (a.relatedMovieSlugs || []).map(slug => slugIndex.get(slug)).filter(Boolean);
  const relatedStories = articles.filter(x => x.slug !== a.slug && (x.category === a.category || x.tags.some(t => a.tags.includes(t)))).slice(0, 3);
  const schema = { '@context':'https://schema.org', '@type':'Article', headline:a.title, description:a.description, mainEntityOfPage:url(`/article/${a.slug}/`), publisher:{'@type':'Organization', name:site.name} };
  if (a.author) schema.author = { '@type': 'Person', name: a.author };
  write(`article/${a.slug}`, layout({
    title: a.title, description: a.description, path: `/article/${a.slug}/`, activeNav: 'articles', ogType: 'article',
    schema: [schema, breadcrumbs([{name:'Home', path:'/'}, {name:'Articles', path:'/articles/'}, {name:a.title, path:`/article/${a.slug}/`}])],
    image: relatedMovies[0] ? poster(relatedMovies[0]) : undefined,
    body: `<main class="shell"><div class="crumb"><a href="${url('/articles/')}">Editorial</a> / ${esc(a.title)}</div><section class="article-hero"><div class="eyebrow">${esc(a.category)}</div><h1>${esc(a.title)}</h1><p class="lead">${esc(a.description)}</p><div class="article-meta">${a.author ? 'By ' + esc(a.author) + ' · ' : ''}Editorial guide · ${a.createdAt ? 'Published ' + esc(a.createdAt) + ' · ' : ''}${a.updatedAt ? 'Last updated ' + esc(a.updatedAt) + ' · ' : ''}Reading time: about ${Math.max(2, Math.ceil(articleWordCount(a) / 220))} minutes</div><button class="quiet-link share-action" type="button" data-share-path="/article/${a.slug}/" data-share-title="${esc(a.title)}">Share</button></section><article class="prose article-body">${articleBlocks(a)}<section class="article-related"><h2>Related titles</h2>${relatedMovies.length ? `<div class="grid">${relatedMovies.map(card).join('')}</div>` : '<p>Related titles will be added when there is a useful match.</p>'}<h2>Keep reading</h2>${relatedStories.length ? `<div class="list">${relatedStories.map(articleRow).join('')}</div>` : ''}</section></article></main>`
  }));
}
write('topics', layout({
  title: 'Topics – focused collections',
  description: 'Explore focused movie, series and anime collections on BRYME.', path: '/topics/',
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Explore by topic</div><h1>Collections with a point of view.</h1><p class="lead">Focused routes through the catalogue and related editorial reading.</p></section><section class="section"><div class="story-grid">${topics.map(t => `<a href="${url('/topic/' + t.slug + '/')}"><span>Topic</span><h3>${esc(t.title)}</h3><p>${esc(t.description)}</p><b>Explore collection</b></a>`).join('') || '<p>No topic collections are published yet.</p>'}</div></section></main>`
}));
for (const topic of topics) {
  const topicMovies = (topic.movieSlugs || []).map(slug => slugIndex.get(slug)).filter(Boolean);
  const topicArticles = (topic.articleSlugs || []).map(slug => articles.find(a => a.slug === slug)).filter(Boolean);
  write(`topic/${topic.slug}`, layout({
    title: topic.title, description: topic.description, path: `/topic/${topic.slug}/`,
    schema: { '@context':'https://schema.org', '@type':'CollectionPage', name:topic.title, description:topic.description, url:url(`/topic/${topic.slug}/`) },
    body: `<main class="shell"><div class="crumb"><a href="${url('/topics/')}">Topics</a> / ${esc(topic.title)}</div><section class="hero"><div class="eyebrow">Topic collection</div><h1>${esc(topic.title)}</h1><p class="lead">${esc(topic.description)}</p></section><section class="section"><h2>Featured titles</h2><div class="grid">${topicMovies.map(card).join('')}</div></section><section class="section"><h2>Related reading</h2>${topicArticles.length ? `<div class="list">${topicArticles.map(articleRow).join('')}</div>` : '<p>Related editorial reading will be added when useful.</p>'}</section></main>`
  }));
}
const articleCategoryMap = new Map();
articles.forEach(a => { const s = slugify(a.category); if (!articleCategoryMap.has(s)) articleCategoryMap.set(s, {name:a.category, articles:[]}); articleCategoryMap.get(s).articles.push(a); });
for (const [slug, category] of articleCategoryMap) {
  const catCount = (category.items || category.articles || []).length;
  if (catCount < THIN_ARCHIVE_MIN) THIN_LISTING_PATHS.add(`/articles/${slug}/`);
  write(`articles/${slug}`, layout({
  noindex: catCount < THIN_ARCHIVE_MIN,
  title: `${category.name} articles`, description: `Original ${category.name.toLowerCase()} guides from BRYME.`, path: `/articles/${slug}/`, activeNav: 'articles',
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Editorial category</div><h1>${esc(category.name)}</h1><p class="lead">Useful guides and original editorial reading.</p></section><section class="section"><div class="list">${category.articles.map(articleRow).join('')}</div></section></main>`
}));
}

/* ---------------- Trailer admin audit page ---------------- */
const trailerAdminJson = JSON.stringify(trailerAdminRows).replace(/</g, '\\u003c');
const trailerAdminFilters = `<div class="trailer-admin-filters"><select id="ta-filter"><option value="">All trailer states</option><option value="official">Official trailers</option><option value="fan-made">Community/fan-made trailers</option><option value="broken">Broken / wrong / unverifiable</option><option value="none">No trailer</option></select><input id="ta-q" placeholder="Search title or slug…" autocomplete="off"></div>`;
write('trailers', layout({
  title: 'Trailer status audit',
  description: "Internal trailer audit for BRYME: every title\u2019s trailer state, source channel and verification date.",
  path: '/trailers/', noindex: true,
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Internal audit</div><h1>Trailer status</h1><p class="lead">Every title's trailer state — official, community fallback or none — with channel and last-check date. Editing is done via content/trailers.json (see scripts/trailer_admin.py); this page is read-only.</p></section><section class="section">${trailerAdminFilters}<div class="trailer-table-wrap" style="overflow-x:auto"><table class="trailer-table"><thead><tr><th>Title</th><th>State</th><th>Type</th><th>Video ID</th><th>Channel</th><th>Verified</th><th>Last checked</th></tr></thead><tbody id="ta-body"></tbody></table></div></section><script id="trailer-admin-data" type="application/json">${trailerAdminJson}<\/script></main>`
}));
/* ================================================================
   TRUST / LEGAL PAGES — About, Contact, Privacy, Terms, Disclaimer,
   Copyright/DMCA, Editorial Policy. Indexable, footer-linked only.
   ================================================================ */
function legalBody(sections){
  return sections.map(sec =>
    sec.h ? `<h2>${esc(sec.h)}</h2>` + (sec.p ? sec.p.map(p => `<p>${p}</p>`).join('') : '')
          : (sec.p ? sec.p.map(p => `<p>${p}</p>`).join('') : '')
  ).join('');
}
const LEGAL_CONTACT_EMAIL = 'Sodiqibrahim03@gmail.com';
const LEGAL_WHATSAPP = '0815 643 0614';
const legalPages = [
  {
    dir: 'about', schemaType: 'AboutPage',
    title: 'About BRYME – Entertainment Discovery Platform',
    description: 'What BRYME is: an entertainment discovery platform for movies, TV series and anime — with trailers, editorial guides and curated recommendations.',
    hero: 'About BRYME', eyebrow: 'About', lead: 'An entertainment discovery platform for movies, TV series and anime.',
    sections: [
      { h: 'What BRYME is', p: ['BRYME is an entertainment discovery website focused on movies, TV series and anime. It helps visitors find titles worth watching by combining a curated catalogue, verified trailer links and original editorial articles.', 'The site is built around discovery: browse by content type, genre, year or country; search across the catalogue; read personal, opinionated articles; and watch official trailers where they are available.'] },
      { h: 'What you will find here', p: ['Movies, TV series and anime with clean title pages that include synopses, key details (year, country, language, genre), related titles and editorial links when they exist.', 'Trailers are linked or embedded from external platforms such as YouTube. BRYME does not host video files and does not claim ownership of third-party trailers, posters or clips unless explicitly stated.', 'Editorial articles are written by BRYME and reflect the personal opinions of their authors.'] },
      { h: 'Who is behind BRYME', p: ['BRYME is created and edited by its founder as an independent entertainment discovery project. Editorial articles are published under the author name shown on each article.'] },
      { h: 'A note on trailers and images', p: ['Trailer thumbnails and embedded players come from YouTube (using YouTube\'s privacy-enhanced domain for embeds). Availability of any trailer is controlled by the external platform and the uploader, not by BRYME. If a trailer becomes unavailable, the site shows a clean \u201cTrailer unavailable\u201d state instead of a broken player.'] }
    ]
  },
  {
    dir: 'contact', schemaType: 'ContactPage',
    title: 'Contact BRYME – Report Issues & Send Feedback',
    description: 'Contact BRYME about incorrect information, trailer or link issues, copyright concerns or general feedback.',
    hero: 'Contact BRYME', eyebrow: 'Contact', lead: 'Questions, corrections, feedback — we want to hear from you.',
    sections: [
      { h: 'Email', p: [LEGAL_CONTACT_EMAIL] },
      { h: 'WhatsApp', p: [LEGAL_WHATSAPP + ' — fastest reply'] },
      { h: 'What to contact us about', p: ['Incorrect or outdated information on any title page.', 'Broken trailer links or trailers that have become unavailable.', 'Copyright concerns (see the Copyright / DMCA page for the full procedure).', 'General feedback, suggestions or questions about the site.'] },
      { h: 'How to make reporting easier', p: ['When reporting an issue, include the exact page URL and a short description of the problem. For copyright matters, please follow the reporting procedure on the Copyright / DMCA page.'] }
    ]
  },
  {
    dir: 'privacy', schemaType: 'WebPage',
    title: 'Privacy Policy – BRYME',
    description: 'BRYME privacy policy: what information is collected, how it is used, external services, cookies, analytics status and your rights.',
    hero: 'Privacy Policy', eyebrow: 'Legal', lead: 'Clear and honest information about privacy on BRYME.',
    sections: [
      { h: 'Information you provide voluntarily', p: ['If you contact BRYME by email or WhatsApp, you voluntarily provide the information contained in your message (such as your email address and the content of your enquiry). BRYME uses that information only to respond to you.'] },
      { h: 'Information collected automatically', p: ['BRYME is hosted on GitHub Pages. Like most web hosts, GitHub may process standard technical data (such as IP addresses and request logs) as part of operating the service. BRYME itself does not run analytics tracking on its pages.'] },
      { h: 'Cookies and local storage', p: ['BRYME does not set its own cookies for advertising or tracking, and does not rely on local storage for personal data. Standard browser mechanisms may operate as part of normal web use, but BRYME does not read or store personal information through them.'] },
      { h: 'Analytics', p: ['BRYME does not currently use Google Analytics or any other analytics service. If analytics is introduced in the future, this policy will be updated to describe it.'] },
      { h: 'External services and YouTube', p: ['Trailers are embedded from YouTube using the privacy-enhanced youtube-nocookie.com domain. When you play a trailer, YouTube\'s own privacy policy and cookie practices apply. BRYME has no control over YouTube\'s data handling.', 'Links to third-party websites (such as streaming platforms) leave BRYME; those websites have their own privacy policies.'] },
      { h: 'Advertising', p: ['BRYME does not currently display advertising and does not use advertising partners or advertising SDKs. If advertising or sponsored content is introduced later, it will be clearly identified and this policy will be updated.'] },
      { h: 'How information may be used', p: ['Information you send us is used to respond to your enquiry, improve the website and address reported issues. BRYME does not sell personal information.'] },
      { h: 'Data retention', p: ['Correspondence is kept only as long as needed to handle the enquiry. BRYME does not maintain user accounts or store visitor profiles.'] },
      { h: 'Your rights', p: ['You may contact BRYME at any time to ask what information we hold about you, to request correction or deletion, or to ask questions about this policy.'] },
      { h: 'Policy updates', p: ['This policy may be updated as the website evolves. Changes will be reflected on this page.'] },
      { h: 'Contact', p: ['Questions about privacy can be sent to ' + LEGAL_CONTACT_EMAIL + '.'] }
    ]
  },
  {
    dir: 'terms', schemaType: 'WebPage',
    title: 'Terms of Use – BRYME',
    description: 'The terms governing your use of BRYME: acceptable use, content, external links, intellectual property and liability.',
    hero: 'Terms of Use', eyebrow: 'Legal', lead: 'The rules for using BRYME.',
    sections: [
      { h: 'Acceptable use', p: ['Use BRYME for lawful, personal, non-commercial discovery purposes. Do not attempt to disrupt the website, scrape it at scale, or use it in any way that could damage or overload the service.'] },
      { h: 'Website content', p: ['Catalogue descriptions, articles and editorial content are provided for entertainment and discovery purposes. Editorial articles reflect the personal opinions of their authors and are clearly opinionated where relevant.'] },
      { h: 'External links and embedded content', p: ['BRYME links to and embeds content from external platforms such as YouTube and third-party streaming services. BRYME does not control those platforms, their content, their availability or their policies.'] },
      { h: 'Accuracy limitations', p: ['While BRYME aims for accuracy, catalogue information, synopses, years, genres and trailer availability may contain errors or become outdated. Information should be verified independently before relying on it.'] },
      { h: 'Intellectual property', p: ['BRYME does not claim ownership of third-party trailers, posters, film footage or other copyrighted material belonging to studios, distributors or rights holders. All trademarks and copyrighted works belong to their respective owners.', 'Original BRYME editorial text and site content are the property of BRYME unless stated otherwise.'] },
      { h: 'User responsibilities', p: ['Users are responsible for how they use the information on the site and for their own decisions about what to watch and where to watch it.'] },
      { h: 'Availability', p: ['BRYME is provided as a static website hosted on GitHub Pages. Availability depends on the hosting service and is provided on a best-effort basis without guarantee of uninterrupted access.'] },
      { h: 'Changes to the service', p: ['BRYME may change, add or remove features, content and pages at any time. These terms may also be updated; continued use of the site after changes means you accept the updated terms.'] },
      { h: 'Limitation of liability', p: ['BRYME is provided \u201cas is\u201d. To the maximum extent permitted by law, BRYME and its operator are not liable for any loss arising from the use of the site, reliance on its content, or the unavailability of third-party trailers or links.'] },
      { h: 'Contact', p: ['Questions about these terms can be sent to ' + LEGAL_CONTACT_EMAIL + '.'] }
    ]
  },
  {
    dir: 'disclaimer', schemaType: 'WebPage',
    title: 'Disclaimer – BRYME',
    description: 'BRYME disclaimer: an entertainment discovery platform; information may change, trailers are controlled by external platforms.',
    hero: 'Disclaimer', eyebrow: 'Legal', lead: 'Please read this before relying on anything you find here.',
    sections: [
      { h: 'Discovery platform', p: ['BRYME is an entertainment discovery and information platform. It helps visitors find movies, TV series and anime worth watching. It is not a streaming service and does not host video content.'] },
      { h: 'Information accuracy', p: ['Information on BRYME — including synopses, years, genres, countries and editorial claims — is provided in good faith but may contain errors or become outdated. Verify important information independently.'] },
      { h: 'Trailer availability', p: ['Trailers are provided by external platforms such as YouTube. Those platforms and their uploaders control the videos: a trailer can be removed, made private or restricted at any time. BRYME does not guarantee that any trailer will remain available, embeddable or playable.'] },
      { h: 'Third-party websites', p: ['Links to external websites lead away from BRYME. Those websites have their own terms, privacy policies and content. BRYME is not responsible for them.'] },
      { h: 'Editorial opinions', p: ['Articles on BRYME express the personal opinions of their authors. Rankings and recommendations are subjective unless explicitly stated otherwise.'] },
      { h: 'No professional advice', p: ['Nothing on BRYME constitutes professional, financial, legal or any other form of professional advice.'] }
    ]
  },
  {
    dir: 'copyright', schemaType: 'WebPage',
    title: 'Copyright & DMCA – BRYME',
    description: 'BRYME copyright notice and reporting procedure for rights holders concerned about potentially infringing material.',
    hero: 'Copyright / DMCA', eyebrow: 'Legal', lead: 'BRYME respects the rights of copyright owners.',
    sections: [
      { h: 'Our position', p: ['BRYME does not host video files, movies or television content. Trailers are linked or embedded from external platforms such as YouTube, and thumbnails are YouTube\'s generated preview images. BRYME does not claim ownership of third-party posters, trailers, screenshots or other copyrighted material — those belong to their respective owners.'] },
      { h: 'Reporting potentially infringing material', p: ['If you are a rights holder and believe material on BRYME infringes your copyright, contact us with the following information:', '1. The exact URL(s) on BRYME where the material appears.', '2. Identification of the copyrighted work you believe is affected.', '3. Your relationship to the material (for example, rights holder or authorized representative).', '4. Contact details so we can reply to you.'] },
      { h: 'How to report', p: ['Send reports to ' + LEGAL_CONTACT_EMAIL + '. Every legitimate report will be reviewed, and material that is found to infringe will be removed or corrected promptly.'] },
      { h: 'What happens next', p: ['BRYME reviews each report on its merits. Where a trailer or thumbnail is hosted by a third party such as YouTube, we may also point you to that platform\'s own reporting tools, since they control the underlying content.'] }
    ]
  },
  {
    dir: 'editorial-policy', schemaType: 'WebPage',
    title: 'Editorial Policy – BRYME',
    description: 'How BRYME articles are written: entertainment-focused, opinionated where labelled, fact-checked, correctable and transparent about sponsored content.',
    hero: 'Editorial Policy', eyebrow: 'Information', lead: 'How BRYME writes and publishes its articles.',
    sections: [
      { h: 'Purpose', p: ['BRYME articles are written for entertainment and discovery purposes: to help readers find something worth watching, understand why a title works, and compare options. They are not academic reviews and not objective buyer-style rankings unless explicitly stated.'] },
      { h: 'Opinions are subjective', p: ['Many articles are opinionated. Authors share personal views — which series gripped them, which anime they prefer and why. These opinions belong to the author and are presented as opinions, not universal facts.'] },
      { h: 'Facts and sources', p: ['Where articles state factual information — release years, episode counts, plot basics — BRYME aims for accuracy and checks facts against reliable sources. External sources may be referenced where appropriate. If a specific fact cannot be verified, it is not invented.'] },
      { h: 'Distinguishing opinion from fact', p: ['BRYME tries to keep the distinction clear: descriptive information (what a series is about, when it aired) is presented as information, while judgments (whether it is good, which one is better) are presented as the author\'s opinion.'] },
      { h: 'Corrections', p: ['When errors are discovered — in facts, links or metadata — BRYME will correct them as soon as practical. Readers are encouraged to report errors via the Contact page.'] },
      { h: 'Sponsored content and advertising', p: ['BRYME does not currently publish sponsored content or advertising. If sponsored or paid content is introduced in the future, it will be clearly identified as such so readers always know what they are reading.'] }
    ]
  }
];
for (const page of legalPages) {
  const schema = [
    { '@context':'https://schema.org', '@type': page.schemaType, name: page.hero, description: page.description, url: absUrl('/' + page.dir + '/') },
    breadcrumbs([{ name:'Home', path:'/' }, { name: page.hero, path: '/' + page.dir + '/' }])
  ];
  write(page.dir, layout({
    title: page.title,
    description: page.description,
    path: '/' + page.dir + '/',
    schema,
    body: `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / ${esc(page.hero)}</div><section class="hero"><div class="eyebrow">${esc(page.eyebrow)}</div><h1>${esc(page.hero)}</h1><p class="lead">${esc(page.lead)}</p></section><article class="prose legal-prose">${legalBody(page.sections)}</article></main>`
  }));
}

/* ================================================================
   VERTICAL ARTICLE PAGES — Make Money / Sports editorial.
   Rendered from content/*-articles.json so the JSON is the single source
   of truth. Only 'published' articles are rendered here; drafts stay out
   of the public site entirely.
   ================================================================ */
function renderVerticalArticle(dir, verticalName, a) {
  const pagePath = articlePathFor(dir, a);
  const cat = (VERTICALS.find(v => v.dir === dir)?.categories || []).find(c => c.slug === articleCatSlug(a));
  const crumbs = [{ name: 'Home', path: '/' }, { name: verticalName, path: '/' + dir + '/' }];
  if (cat) crumbs.push({ name: cat.name, path: '/' + dir + '/' + cat.slug + '/' });
  crumbs.push({ name: a.title, path: pagePath });

  const sections = (a.content || []).map(sec => {
    if (!sec) return '';
    const heading = sec.heading ? `<h2>${esc(sec.heading)}</h2>` : '';
    const paras = String(sec.body || sec.text || '')
      .split(/\n{2,}/)
      .filter(Boolean)
      .map(t => `<p>${esc(t.trim())}</p>`)
      .join('');
    const bullets = Array.isArray(sec.points) && sec.points.length
      ? `<ul>${sec.points.map(pt => `<li>${esc(pt)}</li>`).join('')}</ul>` : '';
    return heading + paras + bullets;
  }).join('');

  const sourceBlock = Array.isArray(a.sources) && a.sources.length
    ? `<section class="sp-source"><h2>Sources</h2><p>${a.sources.map(src =>
        src.url ? `<a href="${esc(src.url)}" rel="nofollow noopener">${esc(src.name || src.url)}</a>` : esc(src.name || src)
      ).join(' · ')}</p><p class="sp-source-note">Figures were checked against the sources above${a.sourcesCheckedOn ? ` on ${esc(a.sourcesCheckedOn)}` : ''}. Published terms change — confirm on the provider's own site before relying on them.</p></section>`
    : '';

  const related = (verticalArticleIndex[dir].get(articleCatSlug(a)) || []).filter(x => x.slug !== a.slug).slice(0, 3);
  const relatedBlock = related.length
    ? `<section class="section"><div class="section-head"><h2>More in ${esc(cat ? cat.name : verticalName)}</h2></div><div class="vcat-grid">${related.map(x => articleCard(dir, x)).join('')}</div></section>`
    : '';

  const updated = a.updatedAt && a.updatedAt !== a.publishedAt ? ` · updated ${esc(a.updatedAt)}` : '';
  const body = `<main class="shell"><div class="crumb">${crumbs.slice(0, -1).map(c => `<a href="${url(c.path)}">${esc(c.name)}</a>`).join(' / ')} / ${esc(a.title)}</div>
  <section class="article-hero"><div class="eyebrow">${esc(cat ? cat.name : verticalName)}</div><h1>${esc(a.title)}</h1>${a.excerpt ? `<p class="lead">${esc(a.excerpt)}</p>` : ''}<div class="article-meta">${a.author ? `<span>${authorLink(a.author)}</span>` : ''}${a.publishedAt ? `<span>${esc(a.publishedAt)}${updated}</span>` : ''}${a.readingTime ? `<span>${esc(a.readingTime)}</span>` : ''}</div></section>
  <article class="prose article-body">${sections}</article>
  ${sourceBlock}${relatedBlock}</main>`;

  write(dir + '/' + a.slug, layout({
    title: a.seoTitle || a.title,
    description: a.excerpt || `${a.title} — ${verticalName} on BRYME.`,
    path: pagePath,
    activeNav: dir,
    ogType: 'article',
    schema: [{
      '@context': 'https://schema.org', '@type': 'Article',
      headline: a.title,
      description: a.excerpt || undefined,
      datePublished: a.publishedAt || undefined,
      dateModified: a.updatedAt || a.publishedAt || undefined,
      author: (() => {
        const rec = AUTHORS.get(a.author);
        if (rec) return { '@type': 'Person', name: rec.name, url: absUrl(authorPath(rec)), jobTitle: rec.role || undefined, knowsAbout: rec.knowsAbout || undefined };
        return { '@type': a.author && /\s/.test(a.author) ? 'Person' : 'Organization', name: a.author || 'BRYME Editorial' };
      })(),
      publisher: { '@type': 'Organization', name: site.name },
      mainEntityOfPage: absUrl(pagePath),
      articleSection: cat ? cat.name : verticalName
    }, breadcrumbs(crumbs)],
    body
  }));
}
VERTICALS.forEach(v => (VERTICAL_ARTICLES[v.dir] || []).forEach(a => renderVerticalArticle(v.dir, v.name, a)));

/* ---------------- Author pages ---------------- */
const AUTHOR_PATHS = [];
AUTHORS.forEach(a => {
  const written = VERTICALS.flatMap(v => (VERTICAL_ARTICLES[v.dir] || [])
    .filter(x => x.author === a.name)
    .map(x => ({ art: x, dir: v.dir, vertical: v.name })));
  const crumbs = [{ name: 'Home', path: '/' }, { name: 'Authors', path: '/' }, { name: a.name, path: authorPath(a) }];
  const body = `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / ${esc(a.name)}</div>
  <section class="article-hero"><div class="eyebrow">${esc(a.role || 'Writer')}</div><h1>${esc(a.name)}</h1>${a.summary ? `<p class="lead">${esc(a.summary)}</p>` : ''}</section>
  <article class="prose article-body">${(a.bio || []).map(t => `<p>${esc(t)}</p>`).join('')}
  ${a.knowsAbout && a.knowsAbout.length ? `<h2>Works with</h2><p>${a.knowsAbout.map(esc).join(' · ')}</p>` : ''}
  ${a.contact ? `<h2>Contact</h2><p>${esc(a.contact)}</p>` : ''}</article>
  ${written.length ? `<section class="section"><div class="section-head"><h2>Articles by ${esc(a.name)}</h2></div><div class="vcat-grid">${written.map(w => articleCard(w.dir, w.art)).join('')}</div></section>` : ''}
  </main>`;
  write('author/' + a.slug, layout({
    title: `${a.name} — ${a.role || 'Writer'}`,
    description: a.summary || `${a.name} writes for ${site.name}.`,
    path: authorPath(a),
    schema: [{
      '@context': 'https://schema.org', '@type': 'ProfilePage',
      mainEntity: {
        '@type': 'Person', name: a.name, url: absUrl(authorPath(a)),
        jobTitle: a.role || undefined,
        description: (a.bio || []).join(' ') || undefined,
        knowsAbout: a.knowsAbout || undefined,
        worksFor: { '@type': 'Organization', name: site.name }
      }
    }, breadcrumbs(crumbs)],
    body
  }));
  AUTHOR_PATHS.push(authorPath(a));
});

/* ================================================================
   NEWS SITEMAP — Google News discovery for time-sensitive football.
   Built to Google's documented rules: articles from the last two days
   only, max 1,000 entries, the same file updated rather than replaced.
   Evergreen guides are deliberately excluded — a news sitemap listing
   explainers that are not news is the fastest way to have it ignored.
   An empty file is valid and expected between publishing runs.
   ================================================================ */
const NEWS_WINDOW_DAYS = 2;
const newsItems = [];
(() => {
  const withinWindow = (d) => {
    const iso = isoDate(d, 'news sitemap');
    if (!iso) return false;
    const days = -daysUntil(iso);          // days since publication
    return days !== null && days >= 0 && days <= NEWS_WINDOW_DAYS;
  };
  /* 1. Sports articles, but ONLY those explicitly marked newsworthy.
        An article has to opt in with "newsworthy": true. Evergreen explainers -
        how the Champions League format works, all-time records - are reference
        material, not news, and a news sitemap padded with them is one Google
        learns to distrust. Opt-in rather than opt-out so the default is safe. */
  (VERTICAL_ARTICLES.sports || []).forEach(a => {
    if (a.newsworthy !== true) return;
    const d = a.publishedAt;
    if (withinWindow(d)) newsItems.push({ path: articlePathFor('sports', a), title: a.title, date: d });
  });
  /* 2. Match pages that became editorial pages, or gained a result, inside the window. */
  const files = { 'premier-league':'fixtures.json', 'la-liga':'fixtures-la-liga.json',
    'serie-a':'fixtures-serie-a.json', 'bundesliga':'fixtures-bundesliga.json', 'ligue-1':'fixtures-ligue-1.json' };
  for (const [lg, file] of Object.entries(files)) {
    const fp = path.join(root, 'content', file);
    if (!fs.existsSync(fp)) continue;
    let F; try { F = JSON.parse(fs.readFileSync(fp, 'utf8')); } catch (e) { continue; }
    (F.matchweeks || []).forEach(w => (w.matches || []).forEach(m => {
      const slug = m.id + '-vs-' + m.away;
      const ed = editorialFor(lg, slug);
      const res = resultFor(lg, slug);
      if (!ed && !res) return;
      /* the date this became news: the result if there is one, else the preview */
      const d = (res && (res.verifiedOn || res.playedOn))
             || (ed && ed.postMatch && ed.postMatch.publishedAt)
             || (ed && (ed.updatedAt || ed.publishedAt));
      if (!withinWindow(d)) return;
      const title = res
        ? `${m.homeName} ${res.homeScore}-${res.awayScore} ${m.awayName}: result and analysis`
        : `${m.homeName} v ${m.awayName}: preview, form and prediction`;
      newsItems.push({ path: '/sports/' + lg + '/matches/' + slug + '/', title, date: d });
    }));
  }
})();
const newsCapped = newsItems.slice(0, 1000);   // Google's documented limit
const newsXml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n${newsCapped.map(n => `  <url>
    <loc>${absUrl(n.path)}</loc>
    <news:news>
      <news:publication>
        <news:name>${esc(site.name)}</news:name>
        <news:language>en</news:language>
      </news:publication>
      <news:publication_date>${esc(n.date)}</news:publication_date>
      <news:title>${esc(n.title)}</news:title>
    </news:news>
  </url>`).join('\n')}\n</urlset>\n`;
fs.writeFileSync(path.join(root, 'news-sitemap.xml'), newsXml);

/* ---------------- 404, sitemap, robots ---------------- */
const genrePaths = typeConfig.flatMap(t => [...genreIndexByType[t.dir].keys()].map(s => `/${t.pageDir}/${s}/`));
const legalPaths = legalPages.map(p => '/' + p.dir + '/');
const verticalPaths = ['/entertainment/','/sports/articles/']
  .concat(VERTICALS.flatMap(v => ['/' + v.dir + '/'].concat((v.categories || []).map(c => '/' + v.dir + '/' + c.slug + '/'))))
  .filter(p => !EMPTY_HUB_PATHS.has(p));
/* Published vertical articles are real, indexable pages. */
const verticalArticlePaths = VERTICALS.flatMap(v => (VERTICAL_ARTICLES[v.dir] || []).map(a => articlePathFor(v.dir, a)));
const paths = ['/','/movies/','/series/','/anime/','/trending/','/genres/','/years/','/topics/','/articles/', ...legalPaths, ...AUTHOR_PATHS, ...verticalPaths, ...verticalArticlePaths, ...sportsExtraPaths, ...LEAGUE_MATCH_PATHS.filter(p => !UNPLAYED_MATCH_PATHS.has(p)), ...genrePaths.filter(p => !THIN_LISTING_PATHS.has(p)), ...movies.map(m => `/${m.typeDir || 'movie'}/${m.slug}/`), ...[...yearMap].filter(([,l]) => !thinArchive(l)).map(([y]) => `/year/${y}/`), ...[...seriesYearMap].filter(([,l]) => !thinArchive(l)).map(([y]) => `/series/${y}/`), ...[...animeYearMap].filter(([,l]) => !thinArchive(l)).map(([y]) => `/anime/${y}/`), ...articles.map(a => `/article/${a.slug}/`), ...topics.map(t => `/topic/${t.slug}/`), ...[...articleCategoryMap.keys()].map(s => `/articles/${s}/`).filter(p => !THIN_LISTING_PATHS.has(p))];
fs.writeFileSync(path.join(root, '404.html'), layout({
  title: 'Page not found', description: 'This page is not available on BRYME.', path: '/404.html', noindex: true,
  body: `<main class="shell"><section class="hero"><div class="eyebrow">404</div><h1>Looks like this one disappeared.</h1><p class="lead">Try searching the catalogue, or browse a single content type.</p><p><a class="cta" href="${url('/search/')}">Search everything</a> <a class="quiet-link" href="${url('/movies/')}">Movies</a> <a class="quiet-link" href="${url('/series/')}">Series</a> <a class="quiet-link" href="${url('/anime/')}">Anime</a> <a class="quiet-link" href="${url('/articles/')}">Latest articles</a></p></section></main>`
}));
if (fs.existsSync(path.join(root, '404'))) { fs.rmSync(path.join(root, '404'), {recursive:true, force:true}); }
const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${[...new Set(paths)].map(p => `  <url><loc>${absUrl(p)}</loc>${PAGE_LASTMOD.has(p) ? `<lastmod>${PAGE_LASTMOD.get(p)}</lastmod>` : ''}</url>`).join('\n')}\n</urlset>\n`;
fs.writeFileSync(path.join(root, 'sitemap.xml'), xml);
fs.writeFileSync(path.join(root, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${absUrl('/sitemap.xml')}\nSitemap: ${absUrl('/news-sitemap.xml')}\n`);

/* ---------------- Catalogue report ---------------- */
const typeCounts = { movie:0, series:0, anime:0 };
movies.forEach(m => { typeCounts[m.typeDir] = (typeCounts[m.typeDir] || 0) + 1; });
const unknown = movies.filter(m => !m.typeDir || !['movie','series','anime'].includes(m.typeDir));
const report = [
  '# BRYME catalogue & frontend report',
  '',
  `Generated: ${new Date().toISOString()}`,
  '',
  '## Catalogue',
  `- Total titles: **${movies.length}**`,
  `- Movies: **${typeCounts.movie}**`,
  `- Series: **${typeCounts.series}**`,
  `- Anime: **${typeCounts.anime}**`,
  `- Unclassified / ambiguous type: **${unknown.length}**`,
  `- With verified trailers: **${youtubeAudit.filter(v => v.status === 'valid-id').length}**`,
  `- Without trailers: **${youtubeAudit.filter(v => v.status === 'unavailable').length}**`,
  `- With editorial ratings: **${movies.filter(m => m.rating && m.rating.value != null).length}**`,
  `- With country data: **${movies.filter(m => m.country).length}** / language: **${movies.filter(m => m.language).length}**`,
  '',
  '## Genre coverage (per type)',
  `- Movie genres: ${[...genreIndexByType.movie.keys()].map(s => `\`${s}\` (${genreIndexByType.movie.get(s).items.length})`).join(', ')}`,
  `- Series genres: ${[...genreIndexByType.series.keys()].map(s => `\`${s}\` (${genreIndexByType.series.get(s).items.length})`).join(', ')}`,
  `- Anime genres: ${[...genreIndexByType.anime.keys()].map(s => `\`${s}\` (${genreIndexByType.anime.get(s).items.length})`).join(', ')}`,
  '',
  '## Routes',
  `- Title pages: ${movies.length}`,
  `- Category pages: /movies/, /series/, /anime/`,
  `- Per-type genre pages: ${genrePaths.length}`,
  `- Indexable URLs in sitemap: **${[...new Set(paths)].length}**`,
  '',
  '## Rankings (editorially curated)',
  `- Trending Now: ${trendingList.length} titles (${trendingByType.movie.length} movies / ${trendingByType.series.length} series / ${trendingByType.anime.length} anime), ranked by trendingRank ASC from content/rankings.json`,
  `- Popular: ${popularList.length} titles (${popularByType.movie.length} movies / ${popularByType.series.length} series / ${popularByType.anime.length} anime), independent of trending`,
  `- Editor's Picks: ${editorPicksList.length} titles, independent of trending/popular`,
  `- Featured hero: ${hero ? hero.title : 'none'}`,
  `- Deterministic: same catalogue + same rankings.json always produces the same lists (no random, no score-based trending)`,
  `- Future: Trending Score = recent engagement + growth rate + searches + clicks + recency, once real analytics exist`,
  '',
  '## Trailer system',
  `- Official trailers: **${trailerStats.official}**`,
  `- Official teasers: **${trailerStats.teaser}**`,
  `- Official clips: **${trailerStats.clip}**`,
  `- Community/fan-made fallbacks (labelled): **${trailerStats.fan}**`,
  `- No verified trailer: **${trailerStats.missing}**`,
  `- Broken/unavailable detected: **${trailerStats.broken}**` + (trailerStats.brokenList.length ? '\n- Broken: ' + trailerStats.brokenList.map(b => b.title + ' (' + b.videoId + ') [' + b.status + ']').join('; ') : ''),
  '- Priority: official-trailer > official-teaser > official-clip > fan-made > unavailable',
  '- Fan-made videos are labelled "Community trailer" with a disclaimer; never "Official Trailer".',
  '',
  '## Editorial config',
  `- Featured hero: ${hero ? hero.title : 'none'} (content/rankings.json)`,
  ''
].join('\n');
fs.writeFileSync(path.join(root, 'reports', 'catalogue-report.md'), report);

if (warnings.length) {
  console.log('WARNINGS:');
  warnings.forEach(w => console.log('  - ' + w));
}
if (BAD_DATES.length) {
  console.error('\nNON-ISO DATES (dropped from sitemap/structured data):');
  BAD_DATES.forEach(d => console.error('  - ' + d));
  process.exitCode = 1;
}
if (REJECTED_RESULTS.length) {
  console.error('\nREFUSED to publish ' + REJECTED_RESULTS.length + ' result(s) - every result needs integer scores and a source.url:');
  REJECTED_RESULTS.forEach(r => console.error('  - ' + r));
  process.exitCode = 1;
}
console.log(`Built ${movies.length} normalized catalogue records (${typeCounts.movie} movies / ${typeCounts.series} series / ${typeCounts.anime} anime), ${articles.length} articles and ${[...new Set(paths)].length} indexable URLs.`);
