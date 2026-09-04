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
const allowDoc=json("content/index-allowlist.json"), allow=new Set(allowDoc.routes);
const verification=new Set(["google2ec8f794263d784f.html","yandex_78fdd841f95fa2e1.html","1740cdb82c02b9af13911b38c853e85d2f708322fa0c2c55.txt"]);
function walk(dir,out=[]){for(const e of fs.readdirSync(dir,{withFileTypes:true})){if([".git","node_modules","reports"].includes(e.name))continue;const p=path.join(dir,e.name);e.isDirectory()?walk(p,out):out.push(p)}return out}
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
if(allow.size!==allowDoc.routes.length)fail("allowlist contains duplicates");
if(allow.size!==58)fail(`expected 58 focused routes, found ${allow.size}`);
for(const r of allow)if(!fs.existsSync(routeFile(r)))fail(`allowlisted route missing: ${r}`);
for(const family of ["sports","movie","movies","series","anime","article","articles","entertainment","genre","genres","year","years","trailers","trending","channels","data","miniapp"]){if(fs.existsSync(path.join(ROOT,family)))fail(`media/legacy family still present on main: ${family}`)}
for(const old of ["assets/site.css","assets/site-app.js","assets/sports-engine.js","content/competitions.json","content/catalogue.json"]){if(fs.existsSync(path.join(ROOT,old)))fail(`legacy media artifact still present: ${old}`)}
const redirectSources=new Set(read("_redirects").split(/\r?\n/).map(x=>x.trim()).filter(x=>x&&!x.startsWith("#")).map(x=>norm(x.split(/\s+/)[0])));
const htmlFiles=walk(ROOT).filter(p=>p.endsWith(".html"));
let indexed=0,noindexed=0,writingArchive=0,jobDetails=0;
for(const file of htmlFiles){
 const r=routeFor(file), f=rel(file), s=fs.readFileSync(file,"utf8"), robots=meta(s,"robots").toLowerCase();
 const wanted=allow.has(r), isNo=robots.includes("noindex"), isIndex=/(?:^|,)\s*index(?:\s*,|$)/.test(robots)&&!isNo;
 if(isIndex)indexed++;if(isNo)noindexed++;
 if(wanted&&!isIndex)fail(`${r}: allowlisted but robots is ${JSON.stringify(robots)}`);
 if(!wanted&&!verification.has(f)&&!isNo)fail(`${r}: outside allowlist without noindex`);
 if(!verification.has(f)){
  if(/href=["']\/assets\/site\.css["']|src=["']\/assets\/site-app\.js["']/i.test(s))fail(`${r}: legacy CSS/JS remains`);
  if(!/assets\/(?:bryme-v2|content-v2)\.css/.test(s))fail(`${r}: forest-green stylesheet missing`);
  if(!/class=["'][^"']*(?:bottom-nav|mobile-nav)/.test(s))fail(`${r}: bottom mobile navigation missing`);
  if(/href=["']\/(?:sports|movie|movies|series|anime|article|articles|entertainment|trailers)(?:\/|["'])/i.test(s))fail(`${r}: local media link remains on main publication`);
 }
 if(/googletagmanager|google-analytics|n6wxm\.com|profitableratecpm|highperformanceformat|monetag\.com/i.test(s))fail(`${r}: tracking/advertising endpoint remains`);
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
 if(/^\/jobs\/(?!remote\/|technology\/|writing\/|creative\/|leadership\/|methodology\/|verified-)[^/]+\/$/.test(r)){
  jobDetails++;const id=r.split("/")[2],job=json("content/jobs.json").jobs.find(x=>x.id===id);
  if(!job)fail(`${r}: no matching jobs dataset record`);else if(!s.includes(job.sourceUrl))fail(`${r}: official source URL missing`);
 }
 if(r.startsWith("/make-money/writing/")&&r!=="/make-money/writing/"){writingArchive++;if(!isNo)fail(`${r}: writing research archive must remain noindex until reverified`)}
 if(wanted&&!QUICK){
  let m,ar=/\b(?:href|src)=["']([^"']+)["']/gi;while((m=ar.exec(s))){const v=m[1];if(!v||/^(?:#|mailto:|tel:|javascript:|data:|https?:\/\/)/i.test(v))continue;let p;try{p=new URL(v,site+r).pathname}catch{fail(`${r}: malformed local reference ${v}`);continue}let t=path.join(ROOT,p.replace(/^\//,"")),exists=fs.existsSync(t);if(exists&&fs.statSync(t).isDirectory())exists=fs.existsSync(path.join(t,"index.html"));if(!exists&&!path.extname(p))exists=fs.existsSync(path.join(t,"index.html"));if(!exists&&!redirectSources.has(norm(p)))fail(`${r}: missing local target ${v}`)}
 }
}
if(indexed!==allow.size)fail(`indexable count ${indexed} does not equal allowlist ${allow.size}`);
if(jobDetails!==13)fail(`expected 13 individual job pages, found ${jobDetails}`);
if(writingArchive!==55)fail(`expected 55 contained writing records, found ${writingArchive}`);
const sitemapRoutes=[...read("sitemap.xml").matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>norm(m[1]));
if(sitemapRoutes.length!==allow.size)fail(`sitemap has ${sitemapRoutes.length}, expected ${allow.size}`);
for(const r of allow)if(!sitemapRoutes.includes(norm(r)))fail(`sitemap missing ${r}`);
for(const r of sitemapRoutes)if(!allow.has(r))fail(`sitemap includes non-allowlisted ${r}`);
const news=[...read("news-sitemap.xml").matchAll(/<loc>(.*?)<\/loc>/g)];if(news.length)fail("News sitemap must remain empty without timely original reporting");
const feeds=[...read("feed.xml").matchAll(/<item>[\s\S]*?<link>(.*?)<\/link>/g)].map(m=>norm(m[1]));for(const r of feeds)if(!allow.has(r))fail(`RSS includes non-allowlisted ${r}`);
if(!read("robots.txt").includes(`Sitemap: ${site}/sitemap.xml`))fail("robots sitemap declaration missing");
const jobs=json("content/jobs.json");if(jobs.jobs?.length!==13)fail("jobs dataset must contain 13 reviewed records");
const ids=new Set(),urls=new Set();for(const j of jobs.jobs||[]){for(const k of ["id","employer","title","locationTextRaw","workMode","employmentType","sourceUrl","sourceSystem","status","verifiedAt","notes","category","remoteEligible"])if(!(k in j)||j[k]==="")fail(`job ${j.id||"?"}: missing ${k}`);if(ids.has(j.id))fail(`duplicate job id ${j.id}`);if(urls.has(j.sourceUrl))fail(`duplicate source ${j.sourceUrl}`);ids.add(j.id);urls.add(j.sourceUrl)}
const opportunities=json("content/opportunities.json").opportunities;if(opportunities.length!==55)fail(`expected 55 writing research records, found ${opportunities.length}`);
for(const o of opportunities)for(const k of ["slug","publication","officialUrl","lastVerified","submissionStatus"])if(!o[k])fail(`writing record ${o.slug||"?"}: missing ${k}`);
const server=read("server/server.js");for(const x of ["PUBLIC_HTML_DIRS","PUBLIC_ROOT_FILES","SECURITY_HEADERS","content-security-policy"])if(!server.includes(x))fail(`server hardening marker missing: ${x}`);
if(!fs.existsSync(path.join(ROOT,"render.yaml")))fail("Render blueprint missing");
const workflow=read(".github/workflows/quality.yml");if(/\|\|\s*true/.test(workflow))fail("quality workflow suppresses failures");
if(warnings.length){console.log(`WARNINGS (${warnings.length})`);warnings.forEach(x=>console.log("  - "+x))}
if(failures.length){console.error(`FAIL (${failures.length})`);failures.slice(0,120).forEach(x=>console.error("  - "+x));process.exit(1)}
console.log(JSON.stringify({ok:true,htmlFiles:htmlFiles.length,indexable:indexed,noindex:noindexed,jobs:jobs.jobs.length,jobDetailPages:jobDetails,writingResearchRecords:opportunities.length,containedWritingPages:writingArchive,sitemapUrls:sitemapRoutes.length,newsUrls:0,rssItems:feeds.length,mediaFamiliesOnMain:0,mode:QUICK?"quick":"full"},null,2));
