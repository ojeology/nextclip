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
const url = p => site.url + p;
const breadcrumbs = items => ({ '@context':'https://schema.org', '@type':'BreadcrumbList', itemListElement:items.map((item, index) => ({ '@type':'ListItem', position:index+1, name:item.name, item:url(item.path) })) });
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
    rating: raw.score == null ? null : { value: raw.score, source: 'NEXTCLIP editorial score' },
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
/* Frontend enrichment (does NOT touch content/catalogue.json)        */
/* ------------------------------------------------------------------ */
const typeGenresPath = path.join(root, 'content', 'type-genres.json');
let typeGenres = {};
if (fs.existsSync(typeGenresPath)) typeGenres = JSON.parse(fs.readFileSync(typeGenresPath, 'utf8'));
const featuredPath = path.join(root, 'content', 'featured.json');
const featuredCfg = fs.existsSync(featuredPath) ? JSON.parse(fs.readFileSync(featuredPath, 'utf8')) : { hero:null, featured:[], boosts:[] };

const slugIndex = new Map(movies.map(m => [m.slug, m]));
const boosts = new Map();
(featuredCfg.featured || []).forEach(f => {
  const rec = slugIndex.get(f.slug);
  if (!rec) { warnings.push(`featured.json: unknown slug "${f.slug}"`); return; }
  if (rec.typeDir !== f.typeDir) warnings.push(`featured.json: type mismatch for "${f.slug}" (expected ${f.typeDir}, record is ${rec.typeDir})`);
  boosts.set(f.slug, { boost: 20, reason: 'Editor\'s pick', label: f.label || null });
});
(featuredCfg.boosts || []).forEach(b => {
  const rec = slugIndex.get(b.slug);
  if (!rec) { warnings.push(`featured.json: unknown boost slug "${b.slug}"`); return; }
  if (rec.typeDir !== b.typeDir) warnings.push(`featured.json: boost type mismatch for "${b.slug}"`);
  const cur = boosts.get(b.slug);
  if (cur) cur.boost += Number(b.boost) || 0; else boosts.set(b.slug, { boost: Number(b.boost) || 0, reason: b.reason || 'Editorially highlighted' });
});
const heroCfg = (featuredCfg.hero && slugIndex.has(featuredCfg.hero.slug)) ? featuredCfg.hero
  : (featuredCfg.featured || []).map(f => ({ slug:f.slug, typeDir:f.typeDir })).find(f => slugIndex.has(f.slug)) || null;
const animeFilms = new Set((typeGenres.anime || {}).films || []);

const typeLabelOf = d => d === 'series' ? 'TV Series' : (d === 'anime' ? 'Anime' : 'Movie');
movies.forEach(m => {
  const tgs = (typeGenres[m.typeDir] || {})[m.slug];
  if (tgs && (!Array.isArray(tgs) || tgs.length === 0)) warnings.push(`type-genres.json: empty genres for ${m.slug}`);
  m.genres = Array.isArray(tgs) ? tgs.slice(0, 3) : [];
  m.typeLabel = typeLabelOf(m.typeDir);
  m.popularity = m.rating && m.rating.value != null ? Math.round(m.rating.value * 10) : 0;
  m.recency = m.year ? Math.max(0, 100 - (CURRENT_YEAR - m.year) * 8) : 0;
  const boost = boosts.get(m.slug);
  m.editorialBoost = boost ? boost.boost : 0;
  m.boostReason = boost ? boost.reason : null;
  m.trendingScore = m.popularity + m.recency + m.editorialBoost;
  m.isFeatured = !!(boost && boost.reason === 'Editor\'s pick');
  m.isNewRelease = !!m.year && m.year >= CURRENT_YEAR - 2;
});
if (heroCfg && !movies.find(m => m.slug === heroCfg.slug)) warnings.push('featured.json: hero slug not found');

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
const hero = heroCfg ? movies.find(m => m.slug === heroCfg.slug) : movies.filter(m => m.typeDir === 'movie').sort((a,b) => (b.rating?.value||0) - (a.rating?.value||0))[0];
const featuredList = movies.filter(m => m.isFeatured).slice(0, 10);
const trendingList = [...movies].sort((a,b) => (b.trendingScore - a.trendingScore) || ((b.year||0) - (a.year||0)) || a.title.localeCompare(b.title));
const newReleases = [...movies].sort((a,b) => ((b.year||0) - (a.year||0)) || a.title.localeCompare(b.title)).filter(m => m.isNewRelease);
const classics = movies.filter(m => m.year && m.year <= 2000).sort((a,b) => ((b.rating?.value||0) - (a.rating?.value||0)) || ((b.year||0) - (a.year||0)));
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
fs.writeFileSync(path.join(root, 'data', 'trending.json'), JSON.stringify({ generatedAt:new Date().toISOString(), formula:{ popularity:'Editorial score x 10 (0-100)', recency:'100 - (currentYear - releaseYear) x 8, minimum 0', editorialBoost:'Featured +20, configured boosts up to +30', note:'No viewer statistics are used. Real analytics can replace this layer later.' }, records:trendingList.map(m => ({ slug:m.slug, title:m.title, typeDir:m.typeDir, year:m.year, trendingScore:m.trendingScore, popularity:m.popularity, recency:m.recency, editorialBoost:m.editorialBoost, boostReason:m.boostReason })) }, null, 2)+'\n');

const legacyArticleCategories = { 'broke-internet':'Movie Facts', 'never-end':'Movie Recommendations', 'agent-kim':'Movie Explainers', 'korean-movies':'Movie Recommendations', 'vampire-horror':'Movie Facts' };
let articles = (ctx.ARTICLES || []).map(a => ({ id:a.id, slug:slugify(a.title), title:clean(a.title), description:clean(a.intro), category:legacyArticleCategories[a.id] || 'Editorial', tags:(a.tags||[]).map(clean), emoji:a.emoji || '', items:(a.items||[]).map(x=>({heading:clean(x.h), body:clean(x.p)})), relatedMovieSlugs:[], status:'archived', updatedAt:null, createdAt:null }));
const authoredEditorialPath = path.join(root, 'content', 'editorial.json');
if (fs.existsSync(authoredEditorialPath)) {
  const authoredEditorial = JSON.parse(fs.readFileSync(authoredEditorialPath, 'utf8'));
  authoredEditorial.forEach(a => articles.push({ id:a.id, slug:a.slug, title:clean(a.title), description:clean(a.excerpt), category:clean(a.category), tags:(a.tags||[]).map(clean), emoji:'', items:(a.content||[]).map(x=>({heading:clean(x.heading), body:clean(x.body)})), blocks:(a.blocks||[]).map(x=>({type:x.type||'paragraph', text:String(x.text||'')})), relatedMovieSlugs:a.relatedMovieSlugs||[], status:a.status||'draft', author:a.author||null, createdAt:null, updatedAt:null }));
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
const css = `:root{--bg:#08090b;--panel:#111419;--line:#272b31;--text:#f4f5f6;--muted:#9aa1a9;--accent:#e94b2c;--gold:#e7bb5c;--movie:#e94b2c;--series:#4f8ef7;--anime:#b06ef7}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.55 Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}a{color:inherit;text-decoration:none}img{max-width:100%}.shell{max-width:1180px;margin:auto;padding:0 20px}.top{position:sticky;top:0;z-index:40;background:rgba(8,9,11,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}.top .shell{min-height:62px;display:flex;align-items:center;justify-content:space-between;gap:20px}.brand{font-weight:900;letter-spacing:.1em;font-size:17px;white-space:nowrap}.brand b{color:var(--accent)}.topnav{display:flex;gap:16px;overflow-x:auto;font-size:13px;font-weight:700;color:var(--muted);scrollbar-width:none}.topnav::-webkit-scrollbar{display:none}.topnav a:hover{color:#fff}.topnav a.active{color:#fff}.nav-search{color:var(--gold)!important}.hero{padding:64px 0 40px;background:radial-gradient(600px 260px at 70% 0,rgba(233,75,44,.15),transparent 70%)}.eyebrow{color:var(--gold);font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}.hero h1{font-size:clamp(32px,6vw,60px);line-height:1.05;max-width:850px;margin:10px 0 14px}.lead{max-width:680px;color:var(--muted);font-size:17px}.section{padding:26px 0}.section h2{font-size:22px;margin:0 0 14px}.section-head{display:flex;align-items:end;justify-content:space-between;gap:16px;margin:0 0 14px}.section-head h2{font-size:clamp(21px,3vw,28px);margin:0;line-height:1.15}.section-head>a{font-size:12px;font-weight:800;color:var(--gold);white-space:nowrap}.section-note{font-size:12px;color:var(--muted);margin:-8px 0 14px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(148px,1fr));gap:16px}.grid-2{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}.crumb{padding:22px 0 0;color:var(--muted);font-size:13px}.crumb a:hover{color:#fff}.poster{aspect-ratio:2/3;background:#171b20;border:1px solid var(--line);overflow:hidden;border-radius:4px;box-shadow:0 12px 28px rgba(0,0,0,.22);position:relative}.poster img{width:100%;height:100%;object-fit:cover;display:block}.placeholder{height:100%;display:grid;place-items:center;padding:16px;text-align:center;font-weight:800;font-size:13px;background:linear-gradient(145deg,#242b35,#0d0f13)}.tile{min-width:0;display:block;transition:transform .25s ease}.tile:hover{transform:translateY(-5px)}.tile h3{font-size:13.5px;margin:8px 0 0;line-height:1.3;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;min-height:2.6em}.tile-meta{display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-size:11.5px;color:var(--muted);margin:4px 0 0}.tile-meta .sep{opacity:.5}.tile-rating{font-size:11px;color:var(--gold);margin:3px 0 0;font-weight:700}.type-badge{display:inline-block;font-size:9.5px;font-weight:900;letter-spacing:.07em;padding:2.5px 6px;border-radius:3px;line-height:1;text-transform:uppercase;color:#0a0b0d}.tb-movie{background:var(--movie)}.tb-series{background:var(--series)}.tb-anime{background:var(--anime)}.rank{position:absolute;top:6px;left:6px;z-index:2;background:rgba(8,9,11,.82);border:1px solid rgba(255,255,255,.25);color:#fff;font-size:11px;font-weight:900;min-width:22px;height:22px;border-radius:4px;display:grid;place-items:center;padding:0 4px}.rank.top{border-color:var(--gold);color:var(--gold)}.rail{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(148px,182px);overflow-x:auto;gap:14px;padding:2px 1px 14px;scroll-snap-type:x mandatory}.rail .tile{scroll-snap-align:start}.loadmore{display:block;margin:18px auto 0;background:transparent;border:1px solid var(--line);color:var(--text);font:inherit;font-weight:700;padding:11px 22px;border-radius:5px;cursor:pointer}.loadmore:hover{border-color:var(--accent);color:#fff}.count-line{font-size:12.5px;color:var(--muted);margin:0 0 14px}.filterbar{display:flex;flex-wrap:wrap;gap:10px;align-items:end;padding:16px;margin:0 0 22px;background:#101318;border:1px solid var(--line);border-radius:6px}.ffield{display:flex;flex-direction:column;gap:4px;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}.ffield select{background:#171b20;color:var(--text);border:1px solid var(--line);border-radius:4px;font:inherit;font-size:13px;padding:8px 30px 8px 10px;max-width:190px}.fbtn{background:#171b20;border:1px solid var(--line);color:var(--muted);font:inherit;font-size:12.5px;font-weight:700;border-radius:4px;padding:8px 12px;cursor:pointer}.fbtn:hover{color:#fff;border-color:#444}.fbtn-clear{color:var(--gold)}.movie-hero{padding:34px 0 28px;display:grid;grid-template-columns:190px minmax(0,1fr);gap:28px}.movie-hero .poster{max-height:285px}.movie-hero h1{font-size:clamp(34px,6vw,58px);line-height:1.05;margin:8px 0}.badges{display:flex;flex-wrap:wrap;gap:7px}.badge{border:1px solid var(--line);color:var(--muted);padding:4px 9px;font-size:12px;border-radius:3px}.badge a:hover{color:#fff}.body{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:42px;padding:22px 0 60px}.prose h2{font-size:20px;margin:28px 0 8px}.prose p{color:#d9dde1}.aside{border-left:1px solid var(--line);padding-left:22px}.aside dt{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.08em;margin-top:16px}.aside dd{margin:3px 0}.cta{display:inline-block;background:var(--accent);padding:10px 15px;font-weight:800;margin-top:10px;border-radius:4px}.list{border-top:1px solid var(--line)}.row{display:flex;gap:14px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)}.row .thumb{height:64px;width:45px;background:#171b20;flex:none;border-radius:3px;overflow:hidden}.row .thumb img{height:100%;width:100%;object-fit:cover}.row b{display:block}.footer{border-top:1px solid var(--line);padding:28px 0 92px;color:var(--muted);font-size:13px}.footer .foot-links{display:flex;flex-wrap:wrap;gap:16px;margin:12px 0 18px;font-weight:700}.footer .foot-links a:hover{color:#fff}.footer small{display:block;max-width:720px;line-height:1.6;opacity:.75}.mobile-nav{display:none}@media(max-width:760px){.shell{padding:0 14px}.top .shell{min-height:56px;padding:0 14px}.topnav{display:none}.hero{padding:44px 0 26px}.movie-hero{grid-template-columns:108px minmax(0,1fr);gap:15px}.movie-hero .poster{max-height:162px}.body{display:block}.aside{border-left:0;border-top:1px solid var(--line);padding:16px 0;margin-top:28px}.grid{grid-template-columns:repeat(3,1fr);gap:10px}.rail{grid-auto-columns:128px;gap:10px}.tile h3{font-size:12px;min-height:2.7em}.tile-meta{font-size:10.5px}.filterbar{flex-wrap:nowrap;overflow-x:auto;padding:12px;gap:8px}.ffield select{max-width:150px}.section-head{flex-wrap:wrap}}`;
fs.mkdirSync(path.join(root,'assets'),{recursive:true});
fs.writeFileSync(path.join(root,'assets/site.css'), css + '\n' + `/* Primary platform experience */
.home-hero{min-height:560px;display:flex;align-items:end;position:relative;isolation:isolate;background:#111820}.home-hero:before{content:"";position:absolute;inset:0;z-index:-2;background-image:var(--hero-image);background-size:cover;background-position:center;filter:saturate(.78) contrast(1.08)}.home-hero:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(5,7,10,.96) 0%,rgba(5,7,10,.72) 42%,rgba(5,7,10,.18) 100%),linear-gradient(0deg,#08090b,transparent 52%)}.home-hero-inner{padding-top:120px;padding-bottom:64px;max-width:1180px;width:100%}.home-hero h1{font-size:clamp(42px,7vw,78px);line-height:.96;max-width:720px;margin:10px 0}.home-hero p{max-width:580px;color:#d2d6d9;font-size:16.5px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.hero-facts{font-size:14px;color:#d3d7d9;display:flex;gap:8px;align-items:center;flex-wrap:wrap}.hero-actions{display:flex;gap:18px;align-items:center;margin-top:22px}.quiet-link{font-weight:750;color:#fff;border-bottom:1px solid rgba(255,255,255,.4);padding:9px 0}.home-main{padding-bottom:30px}.home-section{padding:30px 0}.home-section h2{font-size:clamp(21px,3vw,27px);margin:0}.genre-trio{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.genre-panel{background:#101318;border:1px solid var(--line);border-radius:6px;padding:18px}.genre-panel h3{font-size:15px;margin:0 0 12px;display:flex;align-items:center;gap:8px}.genre-panel .gp-count{font-size:11px;color:var(--muted);font-weight:700}.genre-chips{display:flex;flex-wrap:wrap;gap:7px}.genre-chips a{font-size:12px;font-weight:700;padding:6px 10px;border:1px solid var(--line);border-radius:20px;color:#d9dde1}.genre-chips a:hover{border-color:var(--accent);color:#fff}.genre-chips a b{color:var(--muted);font-weight:700;margin-left:3px}.editorial-row{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.editorial-card{display:block}.editorial-card .poster{aspect-ratio:16/10}.editorial-card h3{font-size:18px;margin:5px 0}.editorial-card span,.editorial-card p{font-size:12px;color:var(--muted)}.editorial-card p{margin:0}.story-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#30343a}.story-grid a{min-height:225px;padding:22px;background:#111419;display:flex;flex-direction:column;align-items:flex-start}.story-grid a:hover{background:#191d23}.story-grid span{font-size:11px;font-weight:800;color:var(--gold);text-transform:uppercase;letter-spacing:.08em}.story-grid h3{font-size:21px;line-height:1.1;margin:10px 0}.story-grid p{font-size:13px;color:var(--muted);margin:0 0 14px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.story-grid b{font-size:13px;margin-top:auto}.discover-cta{margin:40px 0 0;padding:40px;display:flex;align-items:center;justify-content:space-between;gap:30px;border-top:1px solid #353940;background:linear-gradient(90deg,#14171c,#0e1014)}.discover-cta p{color:var(--muted);max-width:480px}.discover-cta .cta{margin:0}.share-action{background:none;border:0;cursor:pointer;margin-left:14px;font:inherit}.article-hero .share-action{margin:16px 0 0}.article-hero{padding:70px 0 30px;max-width:820px}.article-hero h1{font-size:clamp(36px,6vw,60px);line-height:1.04;margin:10px 0}.article-meta{color:var(--muted);font-size:13px;margin-top:18px}.article-body{max-width:760px;padding:28px 0 70px}.article-body h2{margin-top:38px;font-size:28px;line-height:1.16}.article-body p{font-size:18px;line-height:1.75;color:#d9dde1}.article-body blockquote{margin:24px 0;padding:4px 0 4px 22px;border-left:3px solid var(--gold);font-size:clamp(20px,3vw,27px);line-height:1.35;color:#fff}.article-source{font-size:13px!important;color:var(--gold)!important;font-weight:750;letter-spacing:.02em}.article-related{margin-top:56px;padding-top:28px;border-top:1px solid var(--line)}.article-related p{font-size:15px}.movie-hero{max-width:1180px;margin:0 auto;padding:64px 20px 40px;grid-template-columns:190px minmax(0,620px);align-items:end;min-height:470px;position:relative}.movie-hero:before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,#08090b 18%,rgba(8,9,11,.72) 55%,rgba(8,9,11,.95)),linear-gradient(0deg,#08090b,transparent),var(--movie-backdrop);background-size:cover;background-position:center}.movie-hero .poster{border-radius:4px}.movie-hero .lead{font-size:16px;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}.movie-hero h1{font-size:clamp(30px,5vw,52px)}.trailer-section{padding:0 20px 18px}.trailer-frame{position:relative;max-width:860px;aspect-ratio:16/9;background:#000;border-radius:6px;overflow:hidden;cursor:pointer;border:1px solid var(--line)}.trailer-frame img{width:100%;height:100%;object-fit:cover;opacity:.85}.trailer-frame iframe{width:100%;height:100%;border:0;display:block}.trailer-play{position:absolute;inset:0;margin:auto;width:74px;height:50px;border:0;border-radius:10px;background:rgba(233,75,44,.92);cursor:pointer;display:grid;place-items:center}.trailer-play:before{content:"";border-left:16px solid #fff;border-top:10px solid transparent;border-bottom:10px solid transparent;margin-left:4px}.trailer-play:hover{background:var(--accent)}.trailer-fallback{font-size:12.5px;color:var(--muted);margin:10px 0 0}.trailer-unavailable{padding:34px 18px;border:1px dashed var(--line);border-radius:6px;max-width:860px;text-align:center;color:var(--muted)}.trailer-unavailable b{display:block;color:var(--text);margin-bottom:4px}.searchbox{width:100%;max-width:640px;background:#101318;border:1px solid var(--line);border-radius:6px;color:var(--text);font:inherit;font-size:18px;padding:14px 16px;margin:14px 0}.searchbox:focus{outline:0;border-color:var(--accent)}.searchnote{color:var(--muted);font-size:13px;margin:0 0 18px}.search-tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px}.stabs{background:#101318;border:1px solid var(--line);color:var(--muted);font:inherit;font-size:12.5px;font-weight:800;padding:8px 14px;border-radius:20px;cursor:pointer}.stabs.active{background:var(--accent);border-color:var(--accent);color:#fff}.search-group{grid-column:1/-1;font-size:12px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin:14px 0 0;display:flex;align-items:center;gap:10px}.search-group:after{content:"";flex:1;height:1px;background:var(--line)}.trend-note{font-size:13px;color:var(--muted);background:#101318;border:1px solid var(--line);border-left:3px solid var(--gold);padding:14px 18px;border-radius:0 6px 6px 0;margin:0 0 26px}.trend-note code{color:var(--gold);font-size:12px}.boost-reason{font-size:11px;color:var(--muted);margin:3px 0 0}.score-pill{display:inline-flex;align-items:center;gap:4px;font-size:10.5px;font-weight:900;color:var(--gold);border:1px solid rgba(231,187,92,.4);border-radius:20px;padding:2px 8px}.mobile-nav{position:fixed;display:grid;grid-template-columns:repeat(6,1fr);bottom:0;left:0;right:0;z-index:50;background:rgba(12,14,17,.97);backdrop-filter:blur(15px);border-top:1px solid #2a2e34;display:none}.mobile-nav a{text-align:center;padding:10px 2px 9px;color:#b6bdc5;font-size:10px;font-weight:800;line-height:1.2}.mobile-nav a:active,.mobile-nav a.active{color:#fff;background:#1a1e23}.mobile-nav .mn-ico{display:block;font-size:15px;margin-bottom:2px}@media(max-width:760px){body{padding-bottom:62px}.mobile-nav{display:grid}.home-hero{min-height:500px}.home-hero:after{background:linear-gradient(0deg,#08090b 0%,rgba(8,9,11,.86) 36%,rgba(8,9,11,.22) 100%)}.home-hero-inner{padding-top:170px;padding-bottom:36px}.home-hero h1{font-size:42px}.home-hero p{font-size:14.5px}.split-none{display:none}.editorial-row{grid-template-columns:repeat(2,1fr);gap:12px}.editorial-card .poster{aspect-ratio:1/1}.editorial-card p{display:none}.discover-cta{margin:30px -14px 0;padding:26px 14px;display:block}.discover-cta .cta{margin-top:12px}.genre-trio{grid-template-columns:1fr}.genre-panel h3{font-size:16px}.movie-hero{padding:110px 14px 24px;min-height:400px;grid-template-columns:100px minmax(0,1fr);gap:14px}.movie-hero .lead{display:none}.movie-hero .poster{max-height:150px}.trailer-section{padding:0 14px 14px}.story-grid{grid-template-columns:1fr}.story-grid a{min-height:170px}.article-hero{padding:44px 0 18px}.article-body{padding-top:16px}.article-body p{font-size:16px;line-height:1.7}.article-body h2{font-size:24px}}.trailer-section-inner{max-width:860px}.trailer-head{display:flex;align-items:center;gap:12px;margin:0 0 12px}.trailer-status{font-size:13px;font-weight:900;letter-spacing:.04em;padding:5px 12px;border-radius:20px;border:1px solid var(--line)}.trailer-status.t-ok{color:#3ddc84;border-color:rgba(61,220,132,.45)}.trailer-status.t-fan{color:#e7bb5c;border-color:rgba(231,187,92,.5)}.trailer-status.t-none{color:var(--muted)}.trailer-meta{font-size:12.5px;color:var(--muted);margin:10px 0 0}.trailer-verif-note{color:var(--gold);font-size:11px;margin-left:6px}.trailer-disclaimer{font-size:12.5px;color:#d9a441;background:rgba(231,187,92,.08);border:1px solid rgba(231,187,92,.3);padding:8px 12px;border-radius:5px;margin:10px 0 0}.trailer-error{border:1px dashed #b34a3a;background:rgba(179,74,58,.08);border-radius:6px;padding:18px 16px;margin:10px 0 0;color:var(--muted)}.trailer-error b{display:block;color:#ff8a75;margin-bottom:4px}.trailer-error-actions{display:flex;gap:18px;margin-top:10px}.trailer-alt{display:inline-block;margin-top:12px;background:transparent;border:1px solid var(--line);color:var(--text);font:inherit;font-size:13px;font-weight:700;padding:9px 16px;border-radius:5px;cursor:pointer}.trailer-alt:hover{border-color:var(--accent)}.trailer-retry{background:transparent;border:1px solid var(--line);color:var(--text);font:inherit;font-size:12.5px;font-weight:700;padding:7px 14px;border-radius:4px;cursor:pointer;margin-left:12px}.trailer-retry:hover{border-color:var(--accent)}.trailer-table{width:100%;border-collapse:collapse;font-size:13px}.trailer-table th,.trailer-table td{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.trailer-table th{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em}.tr-tag{display:inline-block;font-size:10px;font-weight:900;padding:2px 7px;border-radius:3px;letter-spacing:.05em}.tr-tag.ok{background:rgba(61,220,132,.15);color:#3ddc84}.tr-tag.fan{background:rgba(231,187,92,.15);color:#e7bb5c}.tr-tag.miss{background:rgba(154,161,169,.12);color:var(--muted)}.tr-tag.bad{background:rgba(179,74,58,.15);color:#ff8a75}.trailer-admin-filters{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 16px}.trailer-admin-filters select,.trailer-admin-filters input{background:#171b20;color:var(--text);border:1px solid var(--line);border-radius:4px;font:inherit;font-size:13px;padding:8px 12px}`);
/* ------------------------------------------------------------------ */
/* Shared markup helpers                                              */
/* ------------------------------------------------------------------ */
function image(m){
  const p = poster(m);
  if (p) return `<div class="poster"><img loading="lazy" src="${esc(p)}" alt="${esc(m.title)} trailer thumbnail"></div>`;
  return `<div class="poster"><div class="placeholder">${esc(m.title)}</div></div>`;
}
function card(m, opts){
  opts = opts || {};
  const typeDir = m.typeDir || 'movie';
  const label = typeDir === 'series' ? 'SERIES' : (typeDir === 'anime' ? 'ANIME' : 'MOVIE');
  const genre = m.genreLabel || m.genre || '';
  const rating = m.rating && m.rating.value != null ? `<p class="tile-rating" title="NEXTCLIP editorial score">★ ${esc(String(m.rating.value))}/10 · Editorial</p>` : '';
  const rank = opts.rank ? `<span class="rank${opts.rank <= 3 ? ' top' : ''}">${opts.rank}</span>` : '';
  const reason = (opts.reason && m.boostReason) ? `<p class="boost-reason">${esc(m.boostReason)}</p>` : '';
  return `<a class="tile" href="${url('/' + typeDir + '/' + m.slug + '/')}"><div class="poster">${rank}${poster(m) ? `<img loading="lazy" src="${esc(poster(m))}" alt="${esc(m.title)} trailer thumbnail">` : `<div class="placeholder">${esc(m.title)}</div>`}</div><h3>${esc(m.title)}</h3><div class="tile-meta"><span class="type-badge tb-${typeDir}">${label}</span><span>${esc(m.year || '')}</span>${genre ? `<span class="sep">·</span><span>${esc(genre)}</span>` : ''}</div>${rating}${reason}</a>`;
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
  <div class="trailer-frame" data-trailer-id="${t.videoId}"><img loading="lazy" src="https://i.ytimg.com/vi/${t.videoId}/hqdefault.jpg" alt="${esc(m.title)} trailer thumbnail"><button type="button" class="trailer-play">Play trailer</button></div>
  <p class="trailer-meta">${sourceLine}${verifiedNote}</p>${disclaimer}
  <div class="trailer-error" data-trailer-error hidden><b>Trailer currently unavailable.</b><span>This video could not be played right now.</span><span class="trailer-error-actions"><a class="quiet-link" data-trailer-watch href="${esc(t.watch)}" target="_blank" rel="noopener">Watch on YouTube</a><button type="button" class="trailer-retry" data-trailer-retry>Try again</button></span></div>
  <p class="trailer-fallback">If the embedded player is unavailable, <a href="${esc(t.watch)}" target="_blank" rel="noopener">watch the trailer on YouTube</a>.</p>${altBtn}`;
}
function pageScript(){
  return `<script>window.NEXTCLIP_BASE=${JSON.stringify(site.url)}<\/script><script src="${url('/assets/site-app.js')}"><\/script>`;
}
function layout(o){
  const socialImage = o.image ? `<meta property="og:image" content="${esc(o.image)}"><meta name="twitter:image" content="${esc(o.image)}">` : '';
  const schema = o.schema ? `<script type="application/ld+json">${JSON.stringify(o.schema).replace(/</g,'\\u003c')}<\/script>` : '';
  const active = o.activeNav || '';
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(o.title)} | ${site.name}</title><meta name="description" content="${esc(o.description)}">${o.noindex?'<meta name="robots" content="noindex,follow">':''}<link rel="canonical" href="${url(o.canonical || o.path)}"><meta property="og:type" content="website"><meta property="og:site_name" content="${site.name}"><meta property="og:title" content="${esc(o.title)}"><meta property="og:description" content="${esc(o.description)}"><meta property="og:url" content="${url(o.path)}">${socialImage}<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="${esc(o.title)}"><meta name="twitter:description" content="${esc(o.description)}"><link rel="stylesheet" href="${url('/assets/site.css')}">${schema}</head><body><header class="top"><div class="shell"><a class="brand" href="${url('/')}">NEXT<b>CLIP</b></a><nav class="topnav"><a href="${url('/')}"${active==='home'?' class="active"':''}>Home</a><a href="${url('/movies/')}"${active==='movies'?' class="active"':''}>Movies</a><a href="${url('/series/')}"${active==='series'?' class="active"':''}>Series</a><a href="${url('/anime/')}"${active==='anime'?' class="active"':''}>Anime</a><a href="${url('/genres/')}"${active==='genres'?' class="active"':''}>Genres</a><a href="${url('/trending/')}"${active==='trending'?' class="active"':''}>Trending</a><a href="${url('/articles/')}"${active==='articles'?' class="active"':''}>Articles</a><a class="nav-search" href="${url('/search/')}">Search</a></nav></div></header>${o.body}<nav class="mobile-nav"><a href="${url('/')}"${active==='home'?' class="active"':''}><span class="mn-ico">🏠</span>Home</a><a href="${url('/movies/')}"${active==='movies'?' class="active"':''}><span class="mn-ico">🎬</span>Movies</a><a href="${url('/series/')}"${active==='series'?' class="active"':''}><span class="mn-ico">📺</span>Series</a><a href="${url('/anime/')}"${active==='anime'?' class="active"':''}><span class="mn-ico">🍥</span>Anime</a><a href="${url('/genres/')}"${active==='genres'?' class="active"':''}><span class="mn-ico">🎭</span>Genres</a><a href="${url('/search/')}"><span class="mn-ico">🔍</span>Search</a></nav><footer class="footer"><div class="shell"><nav class="foot-links"><a href="${url('/movies/')}">Movies</a><a href="${url('/series/')}">Series</a><a href="${url('/anime/')}">Anime</a><a href="${url('/genres/')}">Genres</a><a href="${url('/years/')}">Years</a><a href="${url('/topics/')}">Topics</a><a href="${url('/trending/')}">Trending</a><a href="${url('/articles/')}">Articles</a><a href="${url('/search/')}">Search</a></nav>NEXTCLIP · Movie, TV series and anime discovery with editorial guides. Trailer links lead to YouTube and viewing links lead to third parties.<small>Trending rankings use a transparent editorial score (editorial rating + release recency + editorial boost). No fake view counts.</small></div></footer>${pageScript()}</body></html>`;
}

/* ------------------------------------------------------------------ */
/* Pages                                                              */
/* ------------------------------------------------------------------ */
function write(dir, content){ const out = path.join(root, dir, 'index.html'); fs.mkdirSync(path.dirname(out), {recursive:true}); fs.writeFileSync(out, content); }
function railSection(title, emoji, items, moreUrl, note, opts){
  return `<section class="home-section"><div class="shell"><div class="section-head"><h2>${emoji ? emoji + ' ' : ''}${esc(title)}</h2>${moreUrl ? `<a href="${url(moreUrl)}">View all</a>` : ''}</div>${note ? `<p class="section-note">${esc(note)}</p>` : ''}<div class="rail">${items.map((m,i) => card(m, {rank: opts && opts.ranked ? i + 1 : null, reason: opts && opts.reasons})).join('')}</div></div></section>`;
}

/* ---------------- Homepage ---------------- */
const featuredRail = featuredList.length ? featuredList : movies.filter(m => m.typeDir === 'movie').sort(sortPopular).slice(0, 8);
const popularMovies = movies.filter(m => m.typeDir === 'movie').sort(sortPopular).slice(0, 12);
const popularSeries = movies.filter(m => m.typeDir === 'series').sort(sortPopular).slice(0, 12);
const popularAnime = movies.filter(m => m.typeDir === 'anime').sort(sortPopular).slice(0, 12);
const trendNow = trendingList.slice(0, 12);
const freshNow = (newReleases.length >= 8 ? newReleases : movies.filter(m => m.year).sort(sortNewest)).slice(0, 12);
const classicNow = classics.slice(0, 10);
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
write('', layout({
  title: 'Movies, TV Series & Anime – Trailers, Stories & Discovery',
  description: 'NEXTCLIP is a curated entertainment discovery platform: browse 630+ movies, TV series and anime with verified trailers, editorial guides and transparent trending rankings.',
  path: '/', image: poster(hero), activeNav: 'home',
  schema: [{ '@context':'https://schema.org', '@type':'WebSite', name:site.name, url:url('/'), description:site.description }, { '@context':'https://schema.org', '@type':'CollectionPage', name:'NEXTCLIP – Movies, TV Series & Anime', url:url('/') }],
  body: `<main><section class="home-hero" style="--hero-image:url('${esc(poster(hero))}')"><div class="shell home-hero-inner"><div class="eyebrow">Featured spotlight</div><h1>${esc(hero.title)}</h1><div class="hero-facts"><span class="type-badge tb-${hero.typeDir}">${hero.typeLabel.toUpperCase()}</span><span>${hero.year || ''}</span>${hero.genreLabel ? `<span>·</span><span>${esc(hero.genreLabel)}</span>` : ''}</div><p>${esc(hero.description || hero.teaser || 'Explore this title on NEXTCLIP.')}</p><div class="hero-actions"><a class="cta" href="${url('/' + hero.typeDir + '/' + hero.slug + '/')}">Explore ${hero.typeLabel.toLowerCase()}</a><a class="quiet-link" href="${url('/trending/')}">See what's trending</a></div></div></section><main class="shell home-main">
  ${railSection('Editor\'s picks', '⭐', featuredRail, '/genres/', 'Hand-picked by the NEXTCLIP editorial desk — featured is a manual choice, not an algorithm claim.')}
  ${railSection('Trending Now', '🔥', trendNow, '/trending/', 'Ranked by NEXTCLIP\'s transparent trending score: editorial rating + release recency + editorial boost. Not a claim of live viewership.', {ranked:true, reasons:true})}
  ${railSection('Popular Movies', '🎬', popularMovies, '/movies/', 'Movies ranked by NEXTCLIP editorial score.')}
  ${railSection('Popular Series', '📺', popularSeries, '/series/', 'TV series ranked by NEXTCLIP editorial score.')}
  ${railSection('Popular Anime', '🍥', popularAnime, '/anime/', 'Anime ranked by NEXTCLIP editorial score.')}
  ${railSection('New Releases', '🆕', freshNow, '/trending/#new-releases', 'Newest verified release years — old classics are never re-labelled as new.')}
  ${railSection('Classics', '🎞️', classicNow, '/trending/#classics', 'Beloved older titles, kept separate from trending and new releases.')}
  <section class="home-section"><div class="shell"><div class="section-head"><h2>🎭 Browse by genre</h2><a href="${url('/genres/')}">All genres</a></div><div class="genre-trio"><div class="genre-panel"><h3>🎬 Movie genres <span class="gp-count">${movies.filter(m=>m.typeDir==='movie').length} films</span></h3><div class="genre-chips">${genreChips(movies.filter(m=>m.typeDir==='movie'), 'movies', 9)}</div></div><div class="genre-panel"><h3>📺 Series genres <span class="gp-count">${movies.filter(m=>m.typeDir==='series').length} shows</span></h3><div class="genre-chips">${genreChips(movies.filter(m=>m.typeDir==='series'), 'series', 9)}</div></div><div class="genre-panel"><h3>🍥 Anime genres <span class="gp-count">${movies.filter(m=>m.typeDir==='anime').length} titles</span></h3><div class="genre-chips">${genreChips(movies.filter(m=>m.typeDir==='anime'), 'anime', 9)}</div></div></div></div></section>
  <section class="home-section"><div class="shell"><div class="section-head"><div><div class="eyebrow">From the editorial desk</div><h2>📰 Latest articles</h2></div><a href="${url('/articles/')}">All stories</a></div><div class="story-grid">${latestArticles.map(a => `<a href="${url('/article/' + a.slug + '/')}"><span>${esc(a.category)}</span><h3>${esc(a.title)}</h3><p>${esc(a.description)}</p><b>Read story</b></a>`).join('')}</div></div></section>
  <section class="discover-cta"><div><div class="eyebrow">Full catalogue</div><h2>Pick a lane: Movies, Series or Anime.</h2><p>Each section is strictly filtered to its own content type. No mixed-up walls of posters.</p></div><a class="cta" href="${url('/search/')}">Search everything</a></div></section></main></main>`
}));

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
    schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:t.label + ' on NEXTCLIP', description:tDesc, url:url('/' + t.pageDir + '/') }, breadcrumbs([{name:'Home', path:'/'}, {name:t.label, path:'/' + t.pageDir + '/'}])],
    body: `<main class="shell"><section class="hero"><div class="eyebrow">${t.seoNote}</div><h1>${esc(t.label)}</h1><p class="lead">${esc(tDesc)}</p></section><section class="section"><h2>Browse ${esc(t.label.toLowerCase())}</h2>${filterBar}<p class="count-line" data-count>${list.length} ${t.label.toLowerCase()} in the catalogue</p>${progressiveGrid(list, 40)}</section><script id="catalogue-data" type="application/json">${json}<\/script></main>`
  }));
}

/* ---------------- Per-type genre pages ---------------- */
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
    write(`${t.pageDir}/${s}`, layout({
      title: `${g.name} ${genreLabel} – Browse & Discover`,
      description: `Explore ${g.name.toLowerCase()} ${genreLabel} in the NEXTCLIP catalogue: trailers, years, countries and editorial information. ${items.length} ${genreLabel} in this collection.`,
      path: `/${t.pageDir}/${s}/`,
      activeNav: t.activeNav,
      schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:`${g.name} ${genreLabel}`, description:`${g.name} ${genreLabel} on NEXTCLIP.`, url:url(`/${t.pageDir}/${s}/`) }, breadcrumbs([{name:'Home', path:'/'}, {name:t.label, path:'/' + t.pageDir + '/'}, {name:g.name, path:`/${t.pageDir}/${s}/`}])],
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
  description: 'Browse NEXTCLIP genres with strict content-type separation: movie genres, TV series genres and anime genres each have their own category pages.',
  path: '/genres/', activeNav: 'genres',
  schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:'NEXTCLIP genres', url:url('/genres/') }],
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Browse by category</div><h1>Genres, separated by type.</h1><p class="lead">Every genre page is scoped to a single content type — movie genres never contain series, and anime genres never contain movies.</p></section><section class="section"><div class="genre-trio">${genreHubPanels}</div></section><section class="section"><h2>Legacy movie genre pages</h2><p class="lead">The original genre routes remain available: <a class="quiet-link" href="${url('/genre/action/')}">Action</a>, <a class="quiet-link" href="${url('/genre/horror/')}">Horror</a>, <a class="quiet-link" href="${url('/genre/sci-fi/')}">Sci-Fi</a> and <a class="quiet-link" href="${url('/genre/comedy/')}">Comedy</a>.</p></section></main>`
}));

/* ---------------- Legacy /genre/ pages (movie-only, canonical to /movies/{genre}/) ---------------- */
for (const [s, g] of genreIndexByType.movie) {
  if (!fs.existsSync(path.join(root, 'genre', s))) continue;
  const items = [...g.items].sort(sortPopular);
  write(`genre/${s}`, layout({
    title: `${g.name} movies – Browse & Discover`,
    description: `Explore ${g.name.toLowerCase()} movies in the NEXTCLIP catalogue: trailers, years and editorial information.`,
    path: `/genre/${s}/`, canonical: `/movies/${s}/`, activeNav: 'movies',
    schema: { '@context':'https://schema.org', '@type':'CollectionPage', name:`${g.name} movies`, url:url(`/genre/${s}/`) },
    body: `<main class="shell"><div class="crumb"><a href="${url('/genres/')}">Genres</a> / ${esc(g.name)}</div><section class="hero"><div class="eyebrow">Genre</div><h1>${esc(g.name)} movies</h1><p class="lead">A curated selection from the existing NEXTCLIP movie catalogue. The canonical version of this page lives at <a class="quiet-link" href="${url('/movies/' + s + '/')}">${esc(g.name)} movies</a>.</p></section><section class="section">${progressiveGrid(items, 36)}</section></main>`
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

/* ---------------- Years ---------------- */
const yearMap = new Map();
movies.filter(m => m.typeDir === 'movie' && m.year).forEach(m => { if (!yearMap.has(m.year)) yearMap.set(m.year, []); yearMap.get(m.year).push(m); });
write('years', layout({
  title: 'Movies by year', description: 'Browse useful year collections from the NEXTCLIP movie catalogue.', path: '/years/', activeNav: 'movies',
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Browse by year</div><h1>Movies by year</h1><p class="lead">Only years with titles in the catalogue are listed.</p></section><section class="section"><div class="list">${[...yearMap.keys()].sort((a,b) => b - a).map(y => `<a class="row" href="${url('/year/' + y + '/')}"><div><b>${y}</b><span class="meta" style="font-size:12px;color:var(--muted)">${yearMap.get(y).length} movies</span></div></a>`).join('')}</div></section></main>`
}));
for (const [year, list] of yearMap) write(`year/${year}`, layout({
  title: `Movies from ${year}`, description: `Explore movies from ${year} in the NEXTCLIP catalogue.`, path: `/year/${year}/`, activeNav: 'movies',
  body: `<main class="shell"><div class="crumb"><a href="${url('/years/')}">Years</a> / ${year}</div><section class="hero"><div class="eyebrow">Year</div><h1>Movies from ${year}</h1></section><section class="section">${progressiveGrid(list, 36)}</section></main>`
}));

/* ---------------- Trending hub ---------------- */
const trendTop = trendingList.slice(0, 24);
const popularTop = [...movies].sort(sortPopular).slice(0, 24);
const newTop = (newReleases.length >= 8 ? newReleases : movies.filter(m => m.year).sort(sortNewest)).slice(0, 24);
const classicTop = classics.slice(0, 24);
const boostReasons = [...boosts.entries()].map(([slug, b]) => ({ slug, boost: b.boost, reason: b.reason })).filter(b => b.boost !== 20 || b.reason !== 'Editor\'s pick');
write('trending', layout({
  title: 'Trending, Popular, New & Classics',
  description: 'NEXTCLIP\'s transparent rankings: trending by editorial score, popular by editorial rating, new releases by year and classics. No fake view counts.',
  path: '/trending/', activeNav: 'trending',
  schema: [{ '@context':'https://schema.org', '@type':'CollectionPage', name:'Trending & Popular on NEXTCLIP', url:url('/trending/') }],
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Transparent rankings</div><h1>Trending &amp; Popular</h1><p class="lead">Four separate concepts — trending, popular, new releases and classics — with the rules for each explained below.</p></section>
  <div class="trend-note"><b style="color:var(--text)">How the Trending score works.</b><br>Trending Score = editorial rating × 10 (0–100) + recency (100 − (${CURRENT_YEAR} − release year) × 8, minimum 0) + editorial boost (featured +20, topical boosts up to +30).<br>We have no real viewer statistics, so we never pretend to — this is an editorial/algorithmic blend, and real analytics can be plugged into the same pipeline later.<br>${boostReasons.length ? 'Current boosts: ' + boostReasons.map(b => `${esc(b.reason)} (+${b.boost})`).join(' · ') : ''}</div>
  <section class="section" id="trending-now"><div class="section-head"><h2>🔥 Trending Now</h2><a href="#new-releases">New releases ↓</a></div><p class="section-note">Top 24 by trending score. Old classics rarely appear here — that is the point.</p><div class="grid grid-2">${trendTop.map((m,i) => card(m, {rank: i+1, reason:true})).join('')}</div></section>
  <section class="section"><div class="section-head"><h2>⭐ Popular</h2></div><p class="section-note">Top 24 by NEXTCLIP editorial score.</p><div class="grid">${popularTop.map(card).join('')}</div></section>
  <section class="section" id="new-releases"><div class="section-head"><h2>🆕 New Releases</h2></div><p class="section-note">Newest verified release years (${CURRENT_YEAR - 2}–${CURRENT_YEAR}). Older titles are never re-labelled as new.</p><div class="grid">${newTop.map(card).join('')}</div></section>
  <section class="section" id="classics"><div class="section-head"><h2>🎞️ Classics</h2></div><p class="section-note">Titles from 2000 and earlier, ranked by editorial score.</p><div class="grid">${classicTop.map(card).join('')}</div></section></main>`
}));

/* ---------------- Search ---------------- */
const searchEmbed = JSON.stringify({ movies: searchIndex.movies, articles: searchIndex.articles, topics: searchIndex.topics }).replace(/</g, '\\u003c');
write('search', layout({
  title: 'Search Movies, TV Series & Anime',
  description: 'Search the NEXTCLIP catalogue across movies, TV series and anime — every result is labelled with its content type.',
  path: '/search/', noindex: true,
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Global search</div><h1>What are you looking for?</h1><p class="lead">Search movies, TV series and anime. Every result shows its content type, so a series never looks like a movie.</p></section><section class="section"><input class="searchbox" id="search-q" autocomplete="off" placeholder="Try Dune, Breaking Bad, One Piece, Horror, 2024…"><p class="searchnote" id="search-status"></p><div class="search-tabs" id="search-tabs"><button type="button" class="stabs active" data-tab="all">All</button><button type="button" class="stabs" data-tab="movie">🎬 Movies</button><button type="button" class="stabs" data-tab="series">📺 Series</button><button type="button" class="stabs" data-tab="anime">🍥 Anime</button><button type="button" class="stabs" data-tab="article">📰 Articles</button></div><div class="grid" id="search-results"></div></section><script id="search-data" type="application/json">${searchEmbed}<\/script></main>`
}));

/* ---------------- Title pages ---------------- */
function relatedArticlesFor(m){
  if (!m.relatedMovieSlugs) return [];
  return (m.relatedMovieSlugs || []).map(slug => articles.find(a => a.slug === slug)).filter(Boolean).slice(0, 3);
}
articles.forEach(a => a.relatedMovieSlugs = a.relatedMovieSlugs || []);
const articleToMovies = new Map();
articles.forEach(a => { (a.relatedMovieSlugs || []).forEach(slug => { const m = slugIndex.get(slug); if (m) { if (!articleToMovies.has(m.slug)) articleToMovies.set(m.slug, []); articleToMovies.get(m.slug).push(a); } }); });

for (const m of movies) {
  const typeDir = m.typeDir || 'movie';
  const label = m.typeLabel;
  const schemaType = typeDir === 'series' ? 'TVSeries' : (typeDir === 'anime' ? (animeFilms.has(m.slug) ? 'Movie' : 'TVSeries') : 'Movie');
  const seoTitle = m.year ? `${m.title} (${m.year}) – Trailer, Cast, Story & Details` : `${m.title} – Trailer, Cast, Story & Details`;
  const seoDesc = `Explore ${m.title}, including its story, cast, genre, release year and official trailer.`;
  const schema = { '@context':'https://schema.org', '@type':schemaType, name:m.title, description:m.description || m.teaser || undefined, dateCreated:m.year ? String(m.year) : undefined, genre:(m.genres[0] || m.genre) || undefined, sameAs:m.trailer || undefined };
  Object.keys(schema).forEach(k => schema[k] === undefined && delete schema[k]);
  const pagePath = `/${typeDir}/${m.slug}/`;
  const crumbs = [{name:'Home', path:'/'}, {name: label === 'TV Series' ? 'TV Series' : (label === 'Anime' ? 'Anime' : 'Movies'), path: '/' + (typeDir === 'movie' ? 'movies' : typeDir) + '/'}];
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
  const sameType = movies.filter(x => x.id !== m.id && x.typeDir === typeDir);
  const relatedByGenre = sameType
    .map(x => ({ x, overlap: typeDir === 'movie' ? (x.genre === m.genre ? 1 : 0) : (m.genres.length ? x.genres.filter(g => m.genres.includes(g)).length : 0) }))
    .filter(r => r.overlap > 0)
    .sort((a, b) => (b.overlap - a.overlap) || ((b.x.rating?.value || 0) - (a.x.rating?.value || 0)) || ((b.x.year || 0) - (a.x.year || 0)))
    .map(r => r.x);
  const related = (relatedByGenre.length ? relatedByGenre : sameType).slice(0, 6);
  const relatedArticles = (articleToMovies.get(m.slug) || []).slice(0, 3);
  write(`${typeDir}/${m.slug}`, layout({
    title: seoTitle,
    description: m.description || m.teaser || seoDesc,
    path: pagePath,
    activeNav: typeDir === 'movie' ? 'movies' : (typeDir === 'series' ? 'series' : 'anime'),
    schema: schemaList,
    image: poster(m),
    body: `<main class="shell"><div class="crumb"><a href="${url('/')}">Home</a> / <a href="${url('/' + (typeDir === 'movie' ? 'movies' : typeDir) + '/')}">${esc(typeDir === 'movie' ? 'Movies' : label)}</a> / ${esc(m.title)}</div><section class="movie-hero" style="--movie-backdrop:url('${esc(poster(m))}')">${image(m)}<div><div class="eyebrow">${esc(label)} information</div><h1>${esc(m.title)}</h1><div class="badges"><span class="badge"><span class="type-badge tb-${typeDir}">${typeDir === 'series' ? 'SERIES' : (typeDir === 'anime' ? 'ANIME' : 'MOVIE')}</span></span>${m.year ? `<span class="badge">${m.year}</span>` : ''}${genreBadges.join('')}${m.rating && m.rating.value != null ? `<span class="badge" title="${esc(m.rating.source || 'NEXTCLIP editorial score')}">Editorial score ${esc(String(m.rating.value))}/10</span>` : ''}</div><p class="lead">${esc(m.description || m.teaser || 'Information is being added for this title.')}</p>${m.trailer ? `<a class="cta" href="${esc(m.trailer)}" target="_blank" rel="noopener">Watch trailer on YouTube</a>` : ''}<button class="quiet-link share-action" type="button" data-share-path="${pagePath}" data-share-title="${esc(m.title)}">Share</button></div></section><section class="shell trailer-section">${trailerSection(m)}</section><section class="body"><article class="prose"><h2>About ${esc(m.title)}</h2><p>${esc(m.description || 'A full synopsis is not currently available for this title.')}</p>${m.facts.length ? `<h2>Notes</h2><ul>${m.facts.map(f => `<li>${esc(f)}</li>`).join('')}</ul>` : ''}<h2>More like this</h2>${related.length ? `<div class="grid">${related.map(card).join('')}</div>` : '<p>Related titles are not available yet.</p>'}<h2>Related reading</h2>${relatedArticles.length ? `<div class="list">${relatedArticles.map(a => `<a class="row" href="${url('/article/' + a.slug + '/')}"><div><b>${esc(a.title)}</b><span class="meta" style="font-size:12px;color:var(--muted)">${esc(a.category)}</span></div></a>`).join('')}</div>` : '<p>Related editorial reading is not available for this title yet.</p>'}</article><aside class="aside"><h2>Details</h2><dl><dt>Type</dt><dd>${esc(label)}</dd><dt>Year</dt><dd>${m.year || 'Information unavailable'}</dd><dt>Genre</dt><dd>${m.genres.length ? m.genres.map(esc).join(', ') : (esc(m.genre || 'Information unavailable'))}</dd><dt>Country</dt><dd>${esc(m.country || 'Information unavailable')}</dd><dt>Language</dt><dd>${esc(m.language || 'Information unavailable')}</dd><dt>Runtime</dt><dd>${esc(m.runtime || 'Information unavailable')}</dd><dt>Director</dt><dd>${esc(m.director || 'Information unavailable')}</dd><dt>Cast</dt><dd>${m.cast.length ? m.cast.map(esc).join('; ') : 'Information unavailable'}</dd>${m.trendingScore ? `<dt>Trending score</dt><dd>${m.trendingScore} <span class="score-pill" title="Popularity ${m.popularity} + recency ${m.recency} + editorial boost ${m.editorialBoost}">${m.editorialBoost ? '+' + m.editorialBoost + ' boost' : 'recency-based'}</span></dd>` : ''}</dl></aside></section></main>`
  }));
  if (typeDir !== 'movie') {
    write(`movie/${m.slug}`, layout({
      title: seoTitle, description: m.description || m.teaser || seoDesc, path: `/movie/${m.slug}/`, noindex: true, image: poster(m),
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
  description: 'Original editorial from NEXTCLIP: movie lists, explainers and guides that link back to the catalogue.',
  path: '/articles/', activeNav: 'articles',
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Editorial</div><h1>Stories behind the screen.</h1><p class="lead">Original guides and lists — separate from the catalogue, and always linking back to the movies, series and anime they talk about.</p></section><section class="section"><div class="list">${articles.map(articleRow).join('')}</div></section></main>`
}));
for (const a of articles) {
  const relatedMovies = (a.relatedMovieSlugs || []).map(slug => slugIndex.get(slug)).filter(Boolean);
  const relatedStories = articles.filter(x => x.slug !== a.slug && (x.category === a.category || x.tags.some(t => a.tags.includes(t)))).slice(0, 3);
  const schema = { '@context':'https://schema.org', '@type':'Article', headline:a.title, description:a.description, mainEntityOfPage:url(`/article/${a.slug}/`), publisher:{'@type':'Organization', name:site.name} };
  write(`article/${a.slug}`, layout({
    title: a.title, description: a.description, path: `/article/${a.slug}/`, activeNav: 'articles',
    schema: [schema, breadcrumbs([{name:'Home', path:'/'}, {name:'Articles', path:'/articles/'}, {name:a.title, path:`/article/${a.slug}/`}])],
    image: relatedMovies[0] ? poster(relatedMovies[0]) : undefined,
    body: `<main class="shell"><div class="crumb"><a href="${url('/articles/')}">Editorial</a> / ${esc(a.title)}</div><section class="article-hero"><div class="eyebrow">${esc(a.category)}</div><h1>${esc(a.title)}</h1><p class="lead">${esc(a.description)}</p><div class="article-meta">${a.author ? 'By ' + esc(a.author) + ' · ' : ''}Editorial guide · Reading time: about ${Math.max(2, Math.ceil(articleWordCount(a) / 220))} minutes</div><button class="quiet-link share-action" type="button" data-share-path="/article/${a.slug}/" data-share-title="${esc(a.title)}">Share</button></section><article class="prose article-body">${articleBlocks(a)}<section class="article-related"><h2>Related titles</h2>${relatedMovies.length ? `<div class="grid">${relatedMovies.map(card).join('')}</div>` : '<p>Related titles will be added when there is a useful match.</p>'}<h2>Keep reading</h2>${relatedStories.length ? `<div class="list">${relatedStories.map(articleRow).join('')}</div>` : ''}</section></article></main>`
  }));
}
write('topics', layout({
  title: 'Topics – focused collections',
  description: 'Explore focused movie, series and anime collections on NEXTCLIP.', path: '/topics/',
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
for (const [slug, category] of articleCategoryMap) write(`articles/${slug}`, layout({
  title: `${category.name} articles`, description: `Original ${category.name.toLowerCase()} guides from NEXTCLIP.`, path: `/articles/${slug}/`, activeNav: 'articles',
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Editorial category</div><h1>${esc(category.name)}</h1><p class="lead">Useful guides and original editorial reading.</p></section><section class="section"><div class="list">${category.articles.map(articleRow).join('')}</div></section></main>`
}));

/* ---------------- Trailer admin audit page ---------------- */
const trailerAdminJson = JSON.stringify(trailerAdminRows).replace(/</g, '\\u003c');
const trailerAdminFilters = `<div class="trailer-admin-filters"><select id="ta-filter"><option value="">All trailer states</option><option value="official">Official trailers</option><option value="fan-made">Community/fan-made trailers</option><option value="broken">Broken / wrong / unverifiable</option><option value="none">No trailer</option></select><input id="ta-q" placeholder="Search title or slug…" autocomplete="off"></div>`;
write('trailers', layout({
  title: 'Trailer status audit',
  description: "Internal trailer audit for NEXTCLIP: every title\u2019s trailer state, source channel and verification date.",
  path: '/trailers/', noindex: true,
  body: `<main class="shell"><section class="hero"><div class="eyebrow">Internal audit</div><h1>Trailer status</h1><p class="lead">Every title's trailer state — official, community fallback or none — with channel and last-check date. Editing is done via content/trailers.json (see scripts/trailer_admin.py); this page is read-only.</p></section><section class="section">${trailerAdminFilters}<div class="trailer-table-wrap" style="overflow-x:auto"><table class="trailer-table"><thead><tr><th>Title</th><th>State</th><th>Type</th><th>Video ID</th><th>Channel</th><th>Verified</th><th>Last checked</th></tr></thead><tbody id="ta-body"></tbody></table></div></section><script id="trailer-admin-data" type="application/json">${trailerAdminJson}<\/script></main>`
}));
/* ---------------- 404, sitemap, robots ---------------- */
const genrePaths = typeConfig.flatMap(t => [...genreIndexByType[t.dir].keys()].map(s => `/${t.pageDir}/${s}/`));
const paths = ['/','/movies/','/series/','/anime/','/trending/','/genres/','/years/','/topics/','/articles/', ...genrePaths, ...movies.map(m => `/${m.typeDir || 'movie'}/${m.slug}/`), ...[...yearMap.keys()].map(y => `/year/${y}/`), ...articles.map(a => `/article/${a.slug}/`), ...topics.map(t => `/topic/${t.slug}/`), ...[...articleCategoryMap.keys()].map(s => `/articles/${s}/`)];
fs.writeFileSync(path.join(root, '404.html'), layout({
  title: 'Page not found', description: 'This page is not available on NEXTCLIP.', path: '/404.html', noindex: true,
  body: `<main class="shell"><section class="hero"><div class="eyebrow">404</div><h1>Looks like this one disappeared.</h1><p class="lead">Try searching the catalogue, or browse a single content type.</p><p><a class="cta" href="${url('/search/')}">Search everything</a> <a class="quiet-link" href="${url('/movies/')}">Movies</a> <a class="quiet-link" href="${url('/series/')}">Series</a> <a class="quiet-link" href="${url('/anime/')}">Anime</a> <a class="quiet-link" href="${url('/articles/')}">Latest articles</a></p></section></main>`
}));
if (fs.existsSync(path.join(root, '404'))) { fs.rmSync(path.join(root, '404'), {recursive:true, force:true}); }
const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${[...new Set(paths)].map(p => `  <url><loc>${url(p)}</loc></url>`).join('\n')}\n</urlset>\n`;
fs.writeFileSync(path.join(root, 'sitemap.xml'), xml);
fs.writeFileSync(path.join(root, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${url('/sitemap.xml')}\n`);

/* ---------------- Catalogue report ---------------- */
const typeCounts = { movie:0, series:0, anime:0 };
movies.forEach(m => { typeCounts[m.typeDir] = (typeCounts[m.typeDir] || 0) + 1; });
const unknown = movies.filter(m => !m.typeDir || !['movie','series','anime'].includes(m.typeDir));
const report = [
  '# NEXTCLIP catalogue & frontend report',
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
  '## Trending (transparent score)',
  `- Formula: popularity (editorial rating × 10) + recency (100 − (${CURRENT_YEAR} − year) × 8) + editorial boost (featured +20, topical +10..30)`,
  `- Top 5: ${trendingList.slice(0, 5).map(m => `${m.title} (${m.trendingScore})`).join(', ')}`,
  `- No viewer statistics are used or claimed.`,
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
  `- Featured: ${featuredList.length} titles; boosts: ${boostReasons.length}`,
  ''
].join('\n');
fs.writeFileSync(path.join(root, 'reports', 'catalogue-report.md'), report);

if (warnings.length) {
  console.log('WARNINGS:');
  warnings.forEach(w => console.log('  - ' + w));
}
console.log(`Built ${movies.length} normalized catalogue records (${typeCounts.movie} movies / ${typeCounts.series} series / ${typeCounts.anime} anime), ${articles.length} articles and ${[...new Set(paths)].length} indexable URLs.`);
