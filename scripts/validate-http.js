#!/usr/bin/env node
"use strict";
/* HTTP gate for the artifact that actually ships.
 *
 * Production is a Render static site publishing `public/` (render.yaml:
 * `type: static`, `staticPublishPath: public`), so server/server.js is pointed
 * at that directory and this gate exercises the published tree over real HTTP:
 * the routed URL scheme (writers' pages under /writers/, five live properties at
 * the top level, the family hub at /), the redirect rules, method semantics,
 * containment of source files, and the security headers.
 *
 * History: this gate used to probe the pre-routing scheme (/writing/, /guides/,
 * /tools/, /learn/) and to require 410 Gone for /sports/ and /entertainment/ --
 * both of which are live properties now, serving 200 with 111 and 806 sitemap
 * URLs. All 29 of its failures were stale expectations rather than defects. A
 * permanently red gate is worse than no gate, because it trains everyone to
 * ignore the build.
 *
 * Every assertion below was verified against public/ and against production
 * (https://bryme.onrender.com) on 2026-09-15 rather than carried over; the
 * legacy-scheme assertions in check 5 were re-founded on 2026-09-16 after
 * production was found to ignore both render.yaml's routes and its buildCommand
 * purge (see the comment there).
 */
const fs=require("fs"),path=require("path");
const {server}=require("../server/server.js");
const ROOT=path.resolve(__dirname,"..");
const PUBLISH=path.join(ROOT,"public");
const failures=[];const check=(x,m)=>{if(!x)failures.push(m)};
const get=(base,p,o={})=>fetch(base+p,{redirect:"manual",...o});
const read=p=>fs.readFileSync(p,"utf8");

/* The published artifact must not carry source. Checked as files, independent of
   the server, because a leak here is a leak in what Render uploads. */
for(const leak of ["package.json","package-lock.json","scripts","content","server","ecosystem","node_modules",".git","reports","render.yaml"])
  check(!fs.existsSync(path.join(PUBLISH,leak)),`published artifact leaks source: public/${leak}`);
for(const need of ["index.html","404.html","robots.txt","sitemap.xml","favicon.ico","_redirects","assets"])
  check(fs.existsSync(path.join(PUBLISH,need)),`published artifact is missing ${need}`);
check(/noindex/i.test(read(path.join(PUBLISH,"404.html"))),"public/404.html lacks noindex");

/* Redirect rules, read from the published copy -- the same file the server
   loads. Each source must 301 to its declared destination AND that destination
   must resolve. The second half is the check that was missing: every rule here
   pointed at /writing/ or /writing-opportunities/, which have not existed in
   the artifact since the routing migration, so old links were 301ing to a 404. */
const rules=[];
for(const line of read(path.join(PUBLISH,"_redirects")).split(/\r?\n/)){
  const clean=line.trim();if(!clean||clean.startsWith("#"))continue;
  const [from,to,status]=clean.split(/\s+/);
  if(status==="301"&&from&&to)rules.push([from,to]);
}
check(rules.length>0,"no 301 rules found in public/_redirects");

server.listen(0,"127.0.0.1",async()=>{const base=`http://127.0.0.1:${server.address().port}`;try{
 /* 1. The family hub. Root / is the hub, not the writers' homepage. */
 let r=await get(base,"/");check(r.status===200,`/ returned ${r.status}`);
 const hub=await r.text();
 check((hub.match(/<h1\b/gi)||[]).length===1,"hub homepage: expected exactly one H1");
 check(/THE BRYME/.test(hub),"hub homepage: family name missing");
 for(const h of ["content-security-policy","referrer-policy","permissions-policy","strict-transport-security","x-content-type-options","x-frame-options"])
   check(r.headers.has(h),`hub homepage: missing ${h} header`);

 /* 2. The writers' property homepage at its routed path. */
 r=await get(base,"/writers/");check(r.status===200,`/writers/ returned ${r.status}`);
 const w=await r.text();
 check((w.match(/<h1\b/gi)||[]).length===1,"/writers/: expected exactly one H1");
 check(w.includes('id="home-q"'),"/writers/: search bar missing");
 check(w.includes("data-theme-toggle"),"/writers/: theme toggle missing");
 check(/<main\b/i.test(w),"/writers/: main landmark missing");
 check(/skip/i.test(w),"/writers/: skip link missing");

 /* 3. Redirect rules fire, and land somewhere real. */
 for(const [from,to] of rules){
   r=await get(base,from);
   check(r.status===301,`redirect ${from}: expected 301, got ${r.status}`);
   check(r.headers.get("location")===to,`redirect ${from}: location ${r.headers.get("location")}, expected ${to}`);
   const d=await get(base,to);
   check(d.status===200,`redirect ${from} -> ${to}: destination returned ${d.status}`);
   await d.arrayBuffer();
 }

 /* 4. Routed pages resolve. Writers' routes under /writers/, the five live
       properties at the top level, and shared assets. */
 for(const p of ["/writers/writing/","/writers/writing/afrolicious/","/writers/writing-opportunities/",
   "/writers/guides/","/writers/guides/how-to-write-a-pitch/","/writers/tested/","/writers/learn/",
   "/writers/learn/start-writing/","/writers/learn/start-writing/how-to-start-writing/",
   "/writers/learn/writing-basics/sentence-basics/","/writers/tools/","/writers/tools/word-counter/",
   "/writers/glossary/","/writers/templates/","/writers/checklists/","/writers/problems/","/writers/search/",
   "/writers/author/ibrahim-sodiq/","/writers/about/","/about/","/tech/","/sports/","/entertainment/",
   "/fitness/","/home/","/tech/paypal-vs-wise-vs-payoneer/","/assets/bryme-v2.css","/assets/hub-tools.js",
   "/assets/theme.js","/favicon.ico","/robots.txt","/sitemap.xml","/writers/sitemap.xml","/tech/sitemap.xml"]){
   r=await get(base,p);check(r.status===200,`${p}: ${r.status}`);await r.arrayBuffer();
 }

 /* 5. The unprefixed legacy scheme resolves ONLY as noindex redirect stubs.
       Policy change 2026-09-16, forced by production findings: the check here
       used to require bare 404s in the artifact because the redirect rules were
       "declared in render.yaml and honoured". They are not honoured: the live
       Render service was never synced to this repo's render.yaml (it still runs
       dashboard-era rules - /tech 301s to /guides/, /make-money 301s to
       /opportunities/ - and none of the 104 declared rules fire), and the
       buildCommand's `git clean -xdf public/` never ran there either (its
       `|| echo` fallback swallowed the failure), so Render's cached workspace
       kept republishing the 2026-09-14 vintage: ~500 index,follow, self-
       canonical duplicates of the /writers/ pages at the unprefixed roots.
       Rules that the host does not apply protect nothing. The enforcement that
       actually ships is now file-level: scripts/purge-stale-publish.py (final
       step of `npm run build`, which the deployed buildCommand invokes whatever
       else it does) purges those stale directories from the artifact and
       regenerates byte-stable stubs - noindex,follow, instant meta-refresh and
       canonical to the exact routed twin - for every legacy root and every
       legacy sub-page. If the blueprint is ever synced, the published stubs
       win over the rules on Render and serve the same destinations; if the
       stale dashboard rules are ever deleted, bare /tech serves the tech shelf
       directly again. These assertions keep the stub shape honest. */
 for(const p of ["/writing/","/guides/","/tools/","/learn/","/glossary/","/templates/","/checklists/",
   "/problems/","/search/","/writing-opportunities/","/opportunities/","/jobs/","/make-money/",
   "/today/","/tested/","/author/",
   "/guides/how-to-write-a-pitch/","/writing/afrolicious/","/learn/start-writing/"]){
   r=await get(base,p);
   check(r.status===200,`legacy stub ${p}: expected 200 stub, got ${r.status}`);
   const b=await r.text();
   check(/noindex/i.test(b),`legacy stub ${p}: lacks noindex`);
   check(!/index,follow/i.test(b.replace(/noindex,follow/g,"")),`legacy stub ${p}: looks indexable`);
   check(/http-equiv="refresh" content="0;url=\/writers\//i.test(b),`legacy stub ${p}: no instant meta-refresh to a /writers/ twin`);
   check(/rel="canonical" href="https:\/\/[^"]+\/writers\//.test(b),`legacy stub ${p}: canonical is not the routed twin`);
 }

 /* 6. Retired media families. There is no 410.html in the published artifact, so
       these answer 404 -- which is what production does (/movie/the-invite/
       returns 404 live). sports/ and entertainment/ are NOT in this list. */
 for(const p of ["/movie/the-invite/","/movies/","/anime/","/series/","/articles/","/genre/","/trailers/","/trending/"]){
   r=await get(base,p);check(r.status===404,`retired media ${p} should be 404, got ${r.status}`);await r.arrayBuffer();
 }

 /* 7. Containment: nothing outside the public surface, and every 404 body is
       noindex so a stray crawl cannot put one in the index. */
 for(const p of ["/missing","/not-a-page/","/package.json","/scripts/build-focus-site.py","/server/server.js",
   "/content/jobs.json","/content/opportunities.json","/content/index-allowlist.routed.json",
   "/reports/site-inventory.csv","/.git/HEAD","/ecosystem/hub/index.html","/render.yaml","/../package.json"]){
   r=await get(base,p);
   check(r.status===404,`${p} should be 404, got ${r.status}`);
   check(/noindex/i.test(await r.text()),`${p}: 404 body lacks noindex`);
 }

 /* 8. Method and URL-shape semantics. */
 r=await get(base,"/writers/writing/",{method:"POST",body:"x"});
 check(r.status===405,`POST returned ${r.status}`);
 check((r.headers.get("allow")||"").includes("GET"),"405 Allow header missing GET");
 r=await get(base,"/writers/writing/",{method:"HEAD"});
 check(r.status===200,`HEAD returned ${r.status}`);
 check((await r.text())==="","HEAD returned a body");
 r=await get(base,"/writers/writing/index.html");
 check(r.status===308,`index.html should 308 to the directory, got ${r.status}`);
 check(r.headers.get("location")==="/writers/writing/",`index.html 308 location ${r.headers.get("location")}`);
 r=await get(base,"/writers/writing");
 check(r.status===308,`missing trailing slash should 308, got ${r.status}`);
 check(r.headers.get("location")==="/writers/writing/",`trailing-slash 308 location ${r.headers.get("location")}`);

 /* 9. Health endpoint used as the readiness probe by the browser gates. */
 r=await get(base,"/healthz");check(r.status===200,"health failed");
 const health=await r.json();check(health.service==="bryme-work","health service mismatch");
 }catch(e){failures.push(e.stack||String(e))}finally{server.close(()=>{
  if(failures.length){console.error(`FAIL (${failures.length})`);failures.forEach(x=>console.error("  - "+x));process.exitCode=1}
  else console.log(JSON.stringify({ok:true,redirectRules:rules.length,checks:"published artifact, routed routes, redirect destinations, legacy stubs, containment, headers, HEAD/POST, health"},null,2));
 })}});
