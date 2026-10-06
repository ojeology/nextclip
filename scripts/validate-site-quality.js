#!/usr/bin/env node
/* Zero-dependency release gate for the focused BRYME work publication. */
"use strict";
const fs=require("fs"), path=require("path");
const {URL}=require("url");
const ROOT=path.resolve(__dirname,"..");
const QUICK=process.argv.includes("--quick");
const failures=[], warnings=[];
const fail=x=>failures.push(x), warn=x=>warnings.push(x);
const read=r=>fs.readFileSync(path.join(ROOT,r),"utf8");
const json=r=>JSON.parse(read(r));
const site=String(json("site.config.json").siteUrl).replace(/\/$/,"");
// Analytics is sanctioned only when site.config.json says so, mirroring the
// AdSense rails. The ad networks checked below stay banned unconditionally -
// googletagmanager used to sit in that banned list, which is why adding the
// owner's GA4 stream failed this gate on every page.
const ANALYTICS=(()=>{try{return json("site.config.json").analytics||{}}catch{return{}}})();
const GA_ON=!!ANALYTICS.enabled&&/^G-[A-Z0-9]{6,}$/.test(String(ANALYTICS.gaId||""));
const GA_ID=GA_ON?String(ANALYTICS.gaId):"";
const PINTEREST_VERIFICATION=String((json("site.config.json").pinterest||{}).domainVerification||"").trim();
// Third-party ad networks are banned by default -- PropellerAds, popunders, any
// Adsterra format not configured below and any Monetag zone or host not
// configured below all fail this build.
// The exceptions are config-driven, not hardcoded: every unit configured in
// site.config.json under adsterra (the shared key/host, each enabled
// placements.* Native Banner, the displayBanner classic unit and the
// socialBar script) and under monetag (each enabled zone's script URL) is
// sanctioned by its own loader URL, and nothing else is.
// Clear a unit from the config and its exception disappears by itself, so the
// ban is always in force for anything not pasted in. Owner-approved reversal
// of the 20 Sep removal recorded 2026-09-29; owner-approved activation of the
// Social Bar and the classic display banner recorded 2026-10-03; owner-approved
// activation of Monetag In-Page Push and Vignette recorded 2026-10-06
// (docs/ADS.md).
const ADSTERRA=(()=>{try{return json("site.config.json").adsterra||{}}catch{return{}}})();
// Sanctioned units are config-driven. Units may be declared in the legacy shared
// slot (adsterra.key + adsterra.host) and/or per-placement under
// adsterra.placements.* (the 2026-10-03 move that put the Native Banner in the
// top slot). Union every configured key/host pair so clearing one slot only
// withdraws that unit's exception.
const ADSTERRA_PAIRS=(()=>{const pairs=[];
  const add=(k,h)=>{k=String(k||"").trim();h=String(h||"").trim();if(k&&h)pairs.push([k,h]);};
  add(ADSTERRA.key,ADSTERRA.host);
  const pl=ADSTERRA.placements||{};
  for(const name of Object.keys(pl)){const u=pl[name]||{};if(u.enabled===false)continue;add(u.key,u.host);}
  const disp=ADSTERRA.displayBanner||{};
  if(disp.enabled!==false)add(disp.key,disp.host);
  return pairs;})();
// The Social Bar's loader is one external script URL (no invoke.js pairing),
// sanctioned exactly as configured. Owner-approved activation of the Social Bar
// and the classic display banner recorded 2026-10-03; the AdSense-era refusal
// of both was lifted by the Adsterra pivot (docs/ADS.md).
const ADSTERRA_SOCIAL_URL=String((ADSTERRA.socialBar||{}).script||"").trim();
const esc=s=>s.replace(/[.*+?^${}()|[\]\\]/g,"\\$&");
const ADSTERRA_SANCTIONED=(()=>{const alts=ADSTERRA_PAIRS.map(([k,h])=>esc(h)+"\\/"+esc(k)+"\\/invoke\\.js");
  if((ADSTERRA.socialBar||{}).enabled!==false&&ADSTERRA_SOCIAL_URL)alts.push(esc(ADSTERRA_SOCIAL_URL));
  return alts;})();
// Monetag (owner decision 2026-10-06): In-Page Push + Vignette, sanctioned
// exactly as configured. A unit counts only when monetag.enabled AND the unit's
// own enabled are true and its zone id / script URL are well formed - the same
// rule scripts/inject-ads.py applies when it renders the markers, so the gate
// and the build can never disagree about what should be on a page.
const MONETAG=(()=>{try{return json("site.config.json").monetag||{}}catch{return{}}})();
const MONETAG_UNITS=(()=>{const out=[];if(!MONETAG.enabled)return out;
  for(const [key,unit] of [["inPagePush","inpage-push"],["vignette","vignette"]]){
    const u=MONETAG[key]||{};if(!u.enabled)continue;
    const zone=String(u.zone||"").trim(),src=String(u.script||"").trim();
    if(/^[0-9]{4,12}$/.test(zone)&&/^https:\/\/[A-Za-z0-9.-]+\/[A-Za-z0-9._~%+\/-]+$/.test(src))out.push({key,unit,zone,src});
    else fail(`site.config.json: monetag.${key} is enabled but its zone/script is missing or malformed`);}
  return out;})();
// Monetag's own privacy policy is the one other Monetag URL a page may carry:
// the privacy pages link it so a reader can see who the partner is and what it
// says. It is sanctioned only while Monetag is switched on.
const MONETAG_PRIVACY_URL="https://monetag.com/privacy/";
const MONETAG_SANCTIONED=MONETAG_UNITS.length?[...MONETAG_UNITS.map(u=>esc(u.src)),esc(MONETAG_PRIVACY_URL)]:[];
// The sanctioned set, all of it config-driven: each configured unit's loader URL,
// the band's data attribute, and the site's own consent-gating bootstrap at
// /assets/adsterra-loader.js. That last one is a local file whose name states
// what it gates - banning the bare word "adsterra" would fail the very page that
// keeps the network honest. Clear every configured key and all the exceptions
// disappear together.
const SANCTIONED_AD=new RegExp(
  ([...ADSTERRA_SANCTIONED,...MONETAG_SANCTIONED].length
    ? [...ADSTERRA_SANCTIONED,...MONETAG_SANCTIONED].join("|")
    : "(?!)")+"|data-adband=\"adsterra[^\"]*\"","gi");
const allowDoc=fs.existsSync(path.join(ROOT,"content/index-allowlist.routed.json"))?json("content/index-allowlist.routed.json"):json("content/index-allowlist.json"), allow=new Set(allowDoc.routes);
// Every page under /writing/ must be either a real publication record or an
// explicitly declared non-record child. Declaring them here keeps the check
// strict: an unexpected /writing/ page is now a failure, not a silent count.
const PUB_SLUGS=new Set(json("content/opportunities.json").opportunities.map(o=>o.slug));
const NON_PUB_WRITING=new Set(["by-country"]);
const verification=new Set(["google2ec8f794263d784f.html","yandex_78fdd841f95fa2e1.html","1740cdb82c02b9af13911b38c853e85d2f708322fa0c2c55.txt"]);
function walk(dir,out=[]){for(const e of fs.readdirSync(dir,{withFileTypes:true})){if([".git","node_modules","reports","public","ecosystem","content"].includes(e.name))continue;const p=path.join(dir,e.name);e.isDirectory()?walk(p,out):out.push(p)}return out}
const rel=p=>path.relative(ROOT,p).replace(/\\/g,"/");
function routeFor(p){const r=rel(p);return r==="index.html"?"/":r.endsWith("/index.html")?"/"+r.slice(0,-10):"/"+r}
function attrs(tag){const o={};let m,r=/([:\w-]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/g;while((m=r.exec(tag)))o[m[1].toLowerCase()]=m[2]??m[3]??m[4]??"";return o}
function meta(s,n){for(const t of s.match(/<meta\b[^>]*>/gi)||[]){const a=attrs(t);if((a.name||"").toLowerCase()===n)return a.content||""}return ""}
function canonical(s){for(const t of s.match(/<link\b[^>]*>/gi)||[]){const a=attrs(t);if((a.rel||"").split(/\s+/).includes("canonical"))return a.href||""}return ""}
function norm(v){if(v&&typeof v==="object")v=v["@id"]||v.url||"";try{let p=new URL(v,site).pathname.replace(/\/{2,}/g,"/");return p==="/"?"/":p.replace(/\/+$/,"")+"/"}catch{return ""}}
function visible(s){return s.replace(/<script\b[\s\S]*?<\/script>/gi," ").replace(/<style\b[\s\S]*?<\/style>/gi," ").replace(/<[^>]+>/g," ").replace(/&amp;/gi,"&").replace(/&#39;|&apos;/gi,"'").replace(/&quot;/gi,'"').replace(/\s+/g," ").trim()}
function schema(s,route){const out=[];let m,r=/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;while((m=r.exec(s))){try{const x=JSON.parse(m[1]);out.push(...(Array.isArray(x)?x:[x]))}catch(e){fail(`${route}: invalid JSON-LD (${e.message})`)}}return out}
function flatten(x,out=[]){if(Array.isArray(x))x.forEach(v=>flatten(v,out));else if(x&&typeof x==="object"){if(x["@type"])out.push(x);Object.values(x).forEach(v=>{if(v&&typeof v==="object")flatten(v,out)})}return out}
const routeFile=r=>path.join(ROOT,r==="/"?"index.html":r.replace(/^\//,"")+"index.html");
if(PINTEREST_VERIFICATION){
 for(const f of ["ecosystem/hub/index.html","index.html","public/index.html"]){
  if(!fs.existsSync(path.join(ROOT,f))){fail(`${f}: homepage artifact missing for Pinterest verification check`);continue;}
  const head=(read(f).match(/<head\b[^>]*>([\s\S]*?)<\/head>/i)||[])[1]||"";
  const tags=(head.match(/<meta\b[^>]*>/gi)||[]).map(attrs).filter(a=>(a.name||"").toLowerCase()==="p:domain_verify");
  if(tags.length!==1||tags[0].content!==PINTEREST_VERIFICATION)fail(`${f}: expected exactly one configured Pinterest verification meta in <head>`);
 }
}
// --- Monetag (owner decision 2026-10-06) -------------------------------------
// 1. Homepage verification: the owner-supplied token must sit in the <head> of
//    every copy of the canonical homepage, exactly once (the same shape as the
//    Pinterest check above). Generated by scripts/inject-ads.py at build time.
const MONETAG_VERIFICATION=String(MONETAG.verification||"").trim();
if(MONETAG_VERIFICATION){
 for(const f of ["ecosystem/hub/index.html","index.html","public/index.html"]){
  if(!fs.existsSync(path.join(ROOT,f))){fail(`${f}: homepage artifact missing for Monetag verification check`);continue;}
  const head=(read(f).match(/<head\b[^>]*>([\s\S]*?)<\/head>/i)||[])[1]||"";
  const tags=(head.match(/<meta\b[^>]*>/gi)||[]).map(attrs).filter(a=>(a.name||"").toLowerCase()==="monetag");
  if(tags.length!==1||tags[0].content!==MONETAG_VERIFICATION)fail(`${f}: expected exactly one configured Monetag verification meta in <head>`);
 }
}
// 2. The first-party loader. Both tracked copies must be identical (the build
//    copies assets/ into public/), must carry no local frequency cap or storage
//    of any kind, must not hard-code a zone or host (zones come only from
//    site.config.json via the markers), and must keep the SAME consent gate as
//    /assets/adsterra-loader.js: the owner's EEA/UK/CH behaviour is one rule
//    implemented twice, so the two copies are compared rather than trusted.
const stripJsComments=t=>t.replace(/\/\*[\s\S]*?\*\//g,"").replace(/(^|[^:\\])\/\/[^\n]*/g,"$1");
const gateOf=t=>{const c=stripJsComments(t).replace(/\s+/g," ");const i=c.indexOf("function looksEuropean");return i<0?"":c.slice(i).trim()};
const RETIRED_MONETAG_ZONES=["11610753","11610749"];
if(MONETAG_UNITS.length){
 const copies=["assets/monetag-loader.js","public/assets/monetag-loader.js"].map(f=>[f,fs.existsSync(path.join(ROOT,f))?read(f):null]);
 for(const [f,src] of copies){
  if(src===null){fail(`${f}: Monetag is enabled but its loader is missing`);continue;}
  const code=stripJsComments(src);
  if(/localStorage|sessionStorage|document\s*\.\s*cookie|indexedDB/.test(code))fail(`${f}: the loader touches browser storage - Monetag must run with no local frequency cap and no storage of its own`);
  if(/\b\d{5,}\b/.test(code)||/nap5k|n6wxm|monetag\.com/i.test(code))fail(`${f}: a zone id or Monetag host is hard-coded in the loader - zones come only from site.config.json`);
  if(RETIRED_MONETAG_ZONES.some(z=>src.includes(z)))fail(`${f}: retired Monetag zone id present`);
  if(!/\^Europe\\\//.test(code)||!/google_tag_data/.test(code)||!/dataLayer/.test(code))fail(`${f}: the EEA/UK/CH consent gate is missing`);
  const adsterra=fs.existsSync(path.join(ROOT,"assets/adsterra-loader.js"))?read("assets/adsterra-loader.js"):"";
  if(!gateOf(src)||gateOf(src)!==gateOf(adsterra))fail(`${f}: the consent gate differs from /assets/adsterra-loader.js - the two loaders must apply the same EEA/UK/CH rule; change both together`);
 }
 if(copies[0][1]!==null&&copies[1][1]!==null&&copies[0][1]!==copies[1][1])fail("assets/monetag-loader.js and public/assets/monetag-loader.js differ - the build copies assets/ into public/, keep both tracked copies identical");
}
// 3. Page markup: every indexable, non-stub index.html carries exactly one
//    loader tag and exactly the configured zone markers; noindex and redirect
//    stubs carry none; and with Monetag switched off nothing carries it. The
//    skip rule mirrors scripts/inject-ads.py and also honours robots read
//    order-insensitively, so a page the injector would wrongly treat as
//    indexable is caught instead of silently shipping an ad on a stub.
const monetagSeen={root:0,public:0};
function checkMonetagPage(f,s,tree){
 const markers=(s.match(/<div\b[^>]*\bdata-adband=["']monetag["'][^>]*>\s*<\/div>/gi)||[]).map(attrs);
 const loaders=(s.match(/<script\b[^>]*\bsrc=["']\/assets\/monetag-loader\.js["'][^>]*>\s*<\/script>/gi)||[]).length;
 const stub=/name=["']robots["'][^>]*content=["'][^"']*noindex/i.test(s)||/<meta[^>]+http-equiv=["']refresh["']/i.test(s)||meta(s,"robots").toLowerCase().includes("noindex");
 if(stub||!MONETAG_UNITS.length||!/<\/body>/i.test(s)){
  if(markers.length||loaders)fail(`${f}: Monetag markup on a page that must not carry it (${stub?"noindex or redirect stub":!MONETAG_UNITS.length?"Monetag is switched off in site.config.json":"no </body>"})`);
  return;
 }
 monetagSeen[tree]++;
 if(loaders!==1)fail(`${f}: expected exactly one /assets/monetag-loader.js tag, found ${loaders}`);
 if(markers.length!==MONETAG_UNITS.length)fail(`${f}: expected ${MONETAG_UNITS.length} Monetag zone markers, found ${markers.length}`);
 for(const u of MONETAG_UNITS){
  const m=markers.filter(a=>a["data-ad-unit"]===u.unit);
  if(m.length!==1||m[0]["data-ad-zone"]!==u.zone||m[0]["data-ad-src"]!==u.src)fail(`${f}: Monetag ${u.unit} marker is missing or does not match site.config.json (zone ${u.zone}, ${u.src})`);
 }
 if(RETIRED_MONETAG_ZONES.some(z=>s.includes(z)))fail(`${f}: retired Monetag zone id present`);
}
function walkIndex(dir,out=[]){if(!fs.existsSync(dir))return out;for(const e of fs.readdirSync(dir,{withFileTypes:true})){if(e.name==="node_modules"||e.name==="_recovered"||e.name.startsWith("."))continue;const p=path.join(dir,e.name);if(e.isDirectory())walkIndex(p,out);else if(e.name==="index.html")out.push(p)}return out}
// The writing-first publication has no employer jobs on main. Individual
// publication pages under /writing/<slug>/ are verified writing records, not
// employer vacancies, so no JobPosting schema is ever emitted.
if(allow.size!==allowDoc.routes.length)fail("allowlist contains duplicates");
// Allowlist size is intentionally data-driven (grows as tabs/hubs are added); the
// strong guarantees are: every route exists, is index,follow, canonical, on sitemap.
if(allow.size<1)fail("allowlist unexpectedly empty");
for(const r of allow)if(!fs.existsSync(routeFile(r)))fail(`allowlisted route missing: ${r}`);
for(const family of ["movie","movies","series","anime","genre","genres","year","years","trailers","trending","channels","data","miniapp"]){if(fs.existsSync(path.join(ROOT,family)))fail(`media/legacy family still present on main: ${family}`)}
for(const old of ["assets/site.css","assets/site-app.js","assets/sports-engine.js","content/competitions.json","content/catalogue.json"]){if(fs.existsSync(path.join(ROOT,old)))fail(`legacy media artifact still present: ${old}`)}
const redirectSources=new Set(read("_redirects").split(/\r?\n/).map(x=>x.trim()).filter(x=>x&&!x.startsWith("#")).map(x=>norm(x.split(/\s+/)[0])));
const htmlFiles=walk(ROOT).filter(p=>p.endsWith(".html"));
let indexed=0,noindexed=0;let pubRecords=0;
for(const file of htmlFiles){
 const r=routeFor(file), f=rel(file), s=fs.readFileSync(file,"utf8"), robots=meta(s,"robots").toLowerCase();
 const wanted=allow.has(r), isNo=robots.includes("noindex"), isIndex=/(?:^|,)\s*index(?:\s*,|$)/.test(robots)&&!isNo;
 if(isIndex)indexed++;if(isNo)noindexed++;
 if(wanted&&!isIndex)fail(`${r}: allowlisted but robots is ${JSON.stringify(robots)}`);
 if(!wanted&&!verification.has(f)&&!isNo)fail(`${r}: outside allowlist without noindex`);
 // Dataset figures in the hub guides are written as {{tokens}} and filled from
 // content/opportunities.json by writing_stats, inside build-writing-hub's
 // load_guides() - the one place every guide passes through. A token surviving
 // to a page means either a guide used a name that does not exist, or it
 // reached a surface that bypassed load_guides(). Both should stop the build,
 // because the alternative is publishing a number that is not in the data.
 const _tok=(s.match(/\{\{[^{}]*\}\}/)||[])[0];
 if(_tok)fail(`${r}: unfilled dataset token ${_tok} reached the page`);
 if(!verification.has(f)&&f.startsWith("writers/")){
  if(/href=["']\/assets\/site\.css["']|src=["']\/assets\/site-app\.js["']/i.test(s))fail(`${r}: legacy CSS/JS remains`);
  if(!/assets\/(?:bryme-v2|content-v2)\.css/.test(s))fail(`${r}: forest-green stylesheet missing`);
  if(!/class=["'][^"']*(?:bottom-nav|mobile-nav)/.test(s))fail(`${r}: bottom mobile navigation missing`);
  if(/href=["']\/(?:sports|movie|movies|series|anime|article|articles|entertainment|trailers)(?:\/|["'])/i.test(s))fail(`${r}: local media link remains on main publication`);
 }
 // A name blocklist alone cannot catch an unknown ad host, so the test runs on the
 // page with the sanctioned unit already removed: anything still matching a banned
 // network fails, AND any remaining Adsterra-format loader (/invoke.js) fails even
 // when its host is one we have never seen.
 const UNSANCTIONED=s.replace(SANCTIONED_AD,"");
 // Endpoints and formats, not brand names: naming a network in a privacy policy is
// required disclosure, while loading an unsanctioned endpoint is the thing worth
// failing. PropellerAds, popunders and any Adsterra or Monetag endpoint that
// site.config.json does not configure are caught by their hosts and format
// strings.
if(/n6wxm\.com|nap5k\.com|propellerads|monetag\.com|profitableratecpmnetwork|highrevenueformat|highperformanceformat/i.test(UNSANCTIONED))fail(`${r}: disallowed advertising endpoint remains (only the Adsterra and Monetag units configured in site.config.json are permitted; PropellerAds, popunders and any other endpoint fail)`);
 if(/\/invoke\.js/i.test(UNSANCTIONED))fail(`${r}: unsanctioned Adsterra-format ad loader present - only the Adsterra units configured in site.config.json are permitted`);
 if(path.basename(file)==="index.html")checkMonetagPage(f,s,"root");
 if(r!=="/"&&!verification.has(f)&&meta(s,"monetag"))fail(`${r}: Monetag verification meta belongs on the homepage only`);
 if(/googletagmanager|google-analytics/i.test(s)){
  if(!GA_ON)fail(`${r}: analytics endpoint present but analytics.enabled is not true in site.config.json`);
  else if(GA_ID&&!s.includes(GA_ID))fail(`${r}: analytics tag does not carry the configured gaId (${GA_ID})`);
 }
 if(wanted){
  if(norm(canonical(s))!==norm(r))fail(`${r}: canonical mismatch (${canonical(s)||"missing"})`);
  if((s.match(/<h1\b/gi)||[]).length!==1)fail(`${r}: expected exactly one H1`);
  if(!/<html\b[^>]*lang=["'][^"']+/i.test(s))fail(`${r}: html lang missing`);
  if(!/<main\b[^>]*id=["']main["']/i.test(s))fail(`${r}: main#main missing`);
  if(!/class=["']skip-link["'][^>]*href=["']#main["']/i.test(s))fail(`${r}: skip link missing`);
  if(!meta(s,"description"))fail(`${r}: meta description missing`);
  for(const tag of s.match(/<img\b[^>]*>/gi)||[])if(!("alt" in attrs(tag)))fail(`${r}: image missing alt`);
 }
 const entities=schema(s,r), flat=flatten(entities);
 if(flat.some(x=>x["@type"]==="JobPosting"))fail(`${r}: JobPosting published before full source fields are ready`);
 if(wanted) for(const e of entities){
  if(["Article","NewsArticle","BlogPosting"].includes(e["@type"])){
   const own=norm(e.mainEntityOfPage||e.url);if(own&&own!==norm(r))fail(`${r}: Article schema describes ${own}`);
   if(!e.author||!e.datePublished||!e.dateModified)fail(`${r}: Article schema missing author/dates`);
   const name=Array.isArray(e.author)?e.author[0]?.name:e.author?.name;if(name&&!visible(s).toLowerCase().includes(String(name).toLowerCase()))fail(`${r}: schema author is not visible`);
  }
 }
 {const wm=/^\/writers\/writing\/([^/]+)\/$/.exec(r);
  if(wm){ if(PUB_SLUGS.has(wm[1]))pubRecords++;
          else if(!NON_PUB_WRITING.has(wm[1]))fail(`unexpected page under /writing/: ${r}`); }}
 if(wanted&&!QUICK){
  let m,ar=/\b(?:href|src)=["']([^"']+)["']/gi;while((m=ar.exec(s))){const v=m[1];if(!v||/^(?:#|mailto:|tel:|javascript:|data:|https?:\/\/)/i.test(v))continue;let p;try{p=new URL(v,site+r).pathname}catch{fail(`${r}: malformed local reference ${v}`);continue}let t=path.join(ROOT,p.replace(/^\//,"")),exists=fs.existsSync(t);if(exists&&fs.statSync(t).isDirectory())exists=fs.existsSync(path.join(t,"index.html"));if(!exists&&!path.extname(p))exists=fs.existsSync(path.join(t,"index.html"));if(!exists&&!redirectSources.has(norm(p)))fail(`${r}: missing local target ${v}`)}
 }
}
if(indexed!==allow.size)fail(`indexable count ${indexed} does not equal allowlist ${allow.size}`);
const expectedPubs=PUB_SLUGS.size;
/* ---- eligibility discovery invariants (added 2026-09-30) ----------------
   The /writing/ filter is generated by build-writing-first.py and executed by
   assets/opp-filter.js. Nothing tied the two together, so they drifted:
   `data-open` was set from `mode != restricted` (127 cards) while `data-global`
   on the same card used the honest test (77), and the option labelled "Open
   worldwide (no country restriction)" therefore advertised 49 publications
   whose guideline is SILENT about eligibility - contradicting this desk's own
   printed rule. Separately, `includesCountries` / `includesRegions` were read
   by nothing, so a market recorded as open to Nigeria matched no country
   filter at all. These assertions pin the generated cards to their records. */
{
  const wf=path.join(ROOT,"public/writers/writing/index.html");
  if(!fs.existsSync(wf)){fail("public/writers/writing/index.html missing: cannot check eligibility discovery");}
  else{
    const page=fs.readFileSync(wf,"utf8");
    const cards=(page.match(/<article class="job-card"[\s\S]*?<\/article>/g)||[]);
    if(cards.length!==expectedPubs)fail(`/writers/writing/: ${cards.length} cards for ${expectedPubs} records`);
    /* option text ends "… — <n></option>"; capture the number immediately
       before the closing tag so a count is never read out of the label. */
    const optCount=(v)=>{const m=page.match(new RegExp(`<option value="${v}"[^>]*>[^<]*?(\\d+)</option>`));return m?Number(m[1]):null};
    let nIntl=0,nNs=0;
    const recBySlug=new Map(json("content/opportunities.json").opportunities.map(o=>[o.slug,o]));
    for(const c of cards){
      const a=s=>{const m=c.match(new RegExp(`data-${s}="([^"]*)"`));return m?m[1]:null};
      const link=c.match(/href="\/writers\/writing\/([^/"]+)\//);
      if(!link){fail("/writers/writing/: a card has no publication link");continue;}
      const rec=recBySlug.get(link[1]);
      if(!rec){fail(`/writers/writing/: card for unknown record ${link[1]}`);continue;}
      const openTo=a("open-to"), elig=a("elig");
      if(openTo===null||elig===null){fail(`/writers/writing/${link[1]}/: card is missing data-open-to/data-elig`);continue;}
      if(elig!==((rec.eligibility||{}).mode||"not-stated"))fail(`/writers/writing/${link[1]}/: data-elig does not match the record`);
      /* data-open must be the honest test the desk states on its own hub. */
      const honest=(rec.eligibility||{}).mode==="open"||(rec.eligibility||{}).mode==="worldwide";
      if(a("open")!==(honest?"international":"regional"))fail(`/writers/writing/${link[1]}/: data-open is not the stated-eligibility test`);
      if(honest)nIntl++;
      if((rec.eligibility||{}).mode==="not-stated")nNs++;
      /* Every place the record says it accepts work from must be searchable. */
      const want=new Set();
      for(const iso of ((rec.eligibility||{}).includesCountries||[]))want.add(String(iso).toUpperCase());
      const REGION_MEMBERS={africa:["NG","KE","ZA","NA","GH","ET","TZ","UG","RW","SN","EG","MA"],uk:["UK"],ireland:["IE"],canada:["CA"],australia:["AU"],"new-zealand":["NZ"]};
      for(const reg of ((rec.eligibility||{}).includesRegions||[])){want.add(String(reg));for(const iso of (REGION_MEMBERS[reg]||[]))want.add(iso);}
      const have=new Set(openTo.split(/\s+/).filter(Boolean));
      for(const w of want)if(!have.has(w))fail(`/writers/writing/${link[1]}/: "${w}" is in the record's eligibility but not in data-open-to`);
    }
    if(nIntl!==optCount("international"))fail(`/writers/writing/: "Open worldwide" option does not match the ${nIntl} honestly-open cards`);
    if(nNs!==optCount("notstated"))fail(`/writers/writing/: "Eligibility not stated" option does not match the ${nNs} silent records`);
  }
}
// A recorded submission window lapses on its own, with no edit to the record.
// The build downgrades those to closed so the site is never wrong, but the
// maintainer still needs telling that the data needs re-verifying.
const _today=new Date().toISOString().slice(0,10);
const staleWindows=json("content/opportunities.json").opportunities.filter(o=>{
  const d=(o.deadline||{}); const ds=d.date||d.windowEnd; if(!ds)return false;
  return String(ds).slice(0,10)<_today && ["open","deadline","rolling"].includes(o.submissionStatus);
}).map(o=>o.slug);
if(staleWindows.length)warn(`${staleWindows.length} record(s) have a passed deadline but a live status — re-verify: ${staleWindows.join(", ")}`);
if(pubRecords!==expectedPubs)fail(`expected ${expectedPubs} indexed publication records under /writing/, found ${pubRecords}`);
// All seven live property sitemaps must partition the routed index allowlist.
// 2026-10-03: money/sitemap.xml restored (desk relaunched, owner decision -
// monetization pivot to Adsterra after the AdSense rejection).
// Entertainment title pages enter entertainment/sitemap.xml only after their
// curated Watch This / Then Try This batch is released; unfinished catalogue
// pages remain noindex. The legacy sitemap-catalogue.xml stays empty/delisted.
const propertySitemaps=[
  "writers/sitemap.xml", "sports/sitemap.xml", "entertainment/sitemap.xml",
  "tech/sitemap.xml", "fitness/sitemap.xml", "home/sitemap.xml", "money/sitemap.xml",
];
const sitemapRoutes=propertySitemaps.flatMap(sf=>{if(!fs.existsSync(path.join(ROOT,sf)))return[];return[...read(sf).matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>norm(m[1]))});
const sitemapUnique=new Set(sitemapRoutes);
// Writers is writers-only; the two house URLs (/, /about/) live in Home's
// sitemap. The six children must be pairwise disjoint and cover the allowlist.
const idxText=read("sitemap.xml");
if(!idxText.includes("<sitemapindex"))fail("root sitemap.xml must be a sitemapindex");
const idxLocs=[...idxText.matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>{try{return new URL(m[1],site).pathname}catch{return ""}});  // raw paths: norm() would append route-style trailing slashes
for(const sf of propertySitemaps)if(!idxLocs.includes(`/${sf}`))fail(`root sitemap index missing /${sf}`);
if(idxLocs.length!==propertySitemaps.length)fail(`root sitemap index must reference exactly ${propertySitemaps.length} property sitemaps, found ${idxLocs.length}`);
if(sitemapRoutes.length!==sitemapUnique.size)fail(`property sitemaps overlap: ${sitemapRoutes.length} locs but ${sitemapUnique.size} unique`);
if(sitemapUnique.size!==allow.size)fail(`sitemap has ${sitemapUnique.size} unique routes, expected ${allow.size}`);
for(const r of allow)if(!sitemapUnique.has(norm(r)))fail(`sitemap missing ${r}`);
for(const r of sitemapRoutes)if(!allow.has(r))fail(`sitemap includes non-allowlisted ${r}`);
const news=[...read("writers/news-sitemap.xml").matchAll(/<loc>(.*?)<\/loc>/g)];if(news.length)fail("News sitemap must remain empty without timely original reporting");
const feeds=[...read("writers/feed.xml").matchAll(/<item>[\s\S]*?<link>(.*?)<\/link>/g)].map(m=>norm(m[1]));for(const r of feeds)if(!allow.has(r))fail(`RSS includes non-allowlisted ${r}`);
if(!read("robots.txt").includes(`Sitemap: ${site}/writers/sitemap.xml`))fail("robots sitemap declaration missing");
const opportunities=json("content/opportunities.json").opportunities;if(opportunities.length!==expectedPubs)fail(`expected ${expectedPubs} writing research records, found ${opportunities.length}`);
// Dataset statistics in the hub guides must be {{tokens}}, never literals.
// Nine guides used to state counts by hand - "41 of 142 verified publications
// prohibit AI-assisted work", "only 55 of 142 state their rights terms" - and
// every one of them drifted out of date without anything noticing, because no
// check connected the sentence to the data. The token guard above catches an
// unfilled token; this catches the opposite mistake, someone typing the number
// back in. Both are the same failure: a figure on a page that is not read from
// content/opportunities.json. If a new guide needs a figure, add it to
// scripts/writing_stats.py and use the token.
{
 const CLAIM=/(?:\b\d{1,4}\s+of\s+\d{1,4}\b[^.\n]{0,40}?\b(?:publications?|markets?|records?)\b)|(?:\b\d{1,4}\s+(?:verified|paying)\s+(?:publications?|markets?|records?)\b)|(?:\bone\s+in\s+\d{2,4}\b)|(?:\b\d{2,4}\s+(?:publications?|markets?|records?)\s+BRYME\b)|(?:\bof\s+\d{2,4}\s+(?:verified|paying)\b)/gi;
 const dir=path.join(ROOT,"content","hub","guides");
 if(fs.existsSync(dir))for(const f of fs.readdirSync(dir).filter(x=>x.endsWith(".md"))){
  const body=fs.readFileSync(path.join(dir,f),"utf8");
  const hit=body.match(CLAIM);
  if(hit)fail(`content/hub/guides/${f}: hardcoded dataset figure ${JSON.stringify(hit[0])} - use a {{token}} from scripts/writing_stats.py instead`);
 }
}
for(const o of opportunities)for(const k of ["slug","publication","officialUrl","lastVerified","submissionStatus"])if(!o[k])fail(`writing record ${o.slug||"?"}: missing ${k}`);
// public/ is what Render actually serves (staticPublishPath), and the walk above
// skips it, so the Monetag markup is checked there too.
for(const p of walkIndex(path.join(ROOT,"public")))checkMonetagPage(rel(p),fs.readFileSync(p,"utf8"),"public");
const server=read("server/server.js");for(const x of ["PUBLIC_HTML_DIRS","PUBLIC_ROOT_FILES","SECURITY_HEADERS","content-security-policy"])if(!server.includes(x))fail(`server hardening marker missing: ${x}`);
if(!fs.existsSync(path.join(ROOT,"render.yaml")))fail("Render blueprint missing");
const workflow=read(".github/workflows/quality.yml");if(/\|\|\s*true/.test(workflow))fail("quality workflow suppresses failures");
if(warnings.length){console.log(`WARNINGS (${warnings.length})`);warnings.forEach(x=>console.log("  - "+x))}
if(failures.length){console.error(`FAIL (${failures.length})`);failures.slice(0,120).forEach(x=>console.error("  - "+x));process.exit(1)}
console.log(JSON.stringify({ok:true,htmlFiles:htmlFiles.length,indexable:indexed,noindex:noindexed,writingResearchRecords:opportunities.length,publishedPublicationPages:pubRecords,sitemapUrls:sitemapUnique.size,sitemapListings:sitemapRoutes.length,sitemapDuplicateListings:sitemapRoutes.length-sitemapUnique.size,newsUrls:0,rssItems:feeds.length,mediaFamiliesOnMain:0,monetag:{zones:MONETAG_UNITS.map(u=>u.zone),pagesCheckedRoot:monetagSeen.root,pagesCheckedPublic:monetagSeen.public},mode:QUICK?"quick":"full"},null,2));
