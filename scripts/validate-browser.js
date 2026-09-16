#!/usr/bin/env node
"use strict";
const fs=require("fs"),net=require("net"),path=require("path"),{spawn}=require("child_process");
const {chromium}=require("playwright");
const ROOT=path.resolve(__dirname,"..");
/* The published artifact uses the routed scheme: build-routing.py prefixes every
   writers' route with /writers/ and adds the family hub at /. The allowlist
   artifact still holds the unprefixed routes, so map them the same way routing
   does. Verified: all 509 map to a real file under public/writers/. */
const routed=r=>r==="/"?"/writers/":"/writers"+r;
const routes=JSON.parse(fs.readFileSync(path.join(ROOT,"content/index-allowlist.json"),"utf8")).routes.map(routed);
const failures=[];const check=(ok,msg)=>{if(!ok)failures.push(msg)};
/* Owner-mandated monetisation (Monetag zones 11610753 + 11610749, wired in
   ec1329042, caps loosened per owner in 95167a850). Production's CSP is
   `script-src 'self' https:` so these load in production. They are intercepted
   here: the gate must not depend on a third-party network being reachable,
   fast, or serving the same creative twice. */
const AD_HOSTS=/(?:profitableratecpmnetwork|monetag|highperformanceformat|n6wxm|nap5k|propellerads)\./i;
/* Answer ad requests with a benign empty payload rather than aborting them. An
   abort makes Chromium log a failed request, which surfaces as a net::ERR_FAILED
   console error on every page - an artifact of the harness, not a defect in the
   site, and validate-browser fails on any console error. Fulfilling with an empty
   body of the right type keeps the run clean, deterministic and offline-safe
   while still never letting the ad network's own code execute. Images get a real
   1x1 transparent GIF so nothing reports a broken-image decode error. */
const AD_BLANK_GIF=Buffer.from("R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7","base64");
function adFulfill(rt){const image=rt.request().resourceType()==="image";
 return rt.fulfill({status:200,contentType:image?"image/gif":"application/javascript",body:image?AD_BLANK_GIF:""});}

function freePort(){return new Promise((resolve,reject)=>{const s=net.createServer();s.listen(0,"127.0.0.1",()=>{const p=s.address().port;s.close(()=>resolve(p))});s.on("error",reject)})}
async function ready(url){for(let i=0;i<80;i++){try{if((await fetch(url)).ok)return}catch{}await new Promise(r=>setTimeout(r,100))}throw new Error("server did not start")}
(async()=>{const port=await freePort(),base=`http://127.0.0.1:${port}`;const child=spawn(process.execPath,["server/server.js"],{cwd:ROOT,env:{...process.env,PORT:String(port),HOST:"127.0.0.1"},stdio:"ignore"});let browser;
try{await ready(base+"/healthz");browser=await chromium.launch({headless:true});
 const viewports=[{name:"mobile",width:390,height:844},{name:"tablet",width:768,height:1024},{name:"desktop",width:1440,height:1000}];let rendered=0;
 for(const vp of viewports){const context=await browser.newContext({viewport:{width:vp.width,height:vp.height},serviceWorkers:"block"});await context.route(AD_HOSTS,adFulfill);const page=await context.newPage();let routeErrors=[];page.on("console",m=>{if(m.type()==="error"&&!AD_HOSTS.test(m.text()))routeErrors.push(`console: ${m.text()}`)});page.on("pageerror",e=>{if(!AD_HOSTS.test(e.message))routeErrors.push(`page: ${e.message}`)});page.on("requestfailed",r=>{if(!AD_HOSTS.test(r.url()))routeErrors.push(`request: ${r.url()} ${r.failure()?.errorText||"failed"}`)});
  for(const route of routes){routeErrors=[];const label=`${vp.name} ${route}`;try{const response=await page.goto(base+route,{waitUntil:"networkidle",timeout:15000});check(response&&response.status()===200,`${label}: HTTP ${response&&response.status()}`);const x=await page.evaluate(()=>{const css=e=>e?getComputedStyle(e):null,top=document.querySelector('.main-nav,.topnav'),bottom=document.querySelector('.bottom-nav,.mobile-nav'),main=document.querySelector('main#main'),imgs=[...document.images];return{title:document.title.trim(),h1:document.querySelectorAll('h1').length,main:!!main,skip:!!document.querySelector('.skip-link[href="#main"]'),text:(main?.innerText||'').trim().length,scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth,topDisplay:css(top)?.display||'none',topLinks:top?[...top.querySelectorAll('.has-mega > a')].map(a=>a.textContent.trim()):[],topCurrent:!!top?.querySelector('[aria-current="page"]'),bottomDisplay:css(bottom)?.display||'none',bottomLinks:bottom?[...bottom.querySelectorAll(':scope > a')].length:0,bottomCurrent:!!bottom?.querySelector('[aria-current="page"]'),bottomHeight:bottom?.getBoundingClientRect().height||0,paddingBottom:parseFloat(css(document.body)?.paddingBottom||'0'),styles:[...document.querySelectorAll('link[rel="stylesheet"]')].map(e=>e.href),scripts:[...document.querySelectorAll('script[src]')].map(e=>e.src),badImages:imgs.filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.currentSrc||i.src),externalResources:performance.getEntriesByType('resource').map(e=>e.name).filter(u=>{try{return new URL(u).origin!==location.origin}catch{return false}})}});
   check(x.title.length>=12,`${label}: short title`);check(x.h1===1,`${label}: H1 count ${x.h1}`);check(x.main&&x.skip,`${label}: main/skip landmark missing`);check(x.text>=120,`${label}: thin rendered body (${x.text})`);check(x.scroll<=x.client+2,`${label}: horizontal overflow ${x.scroll}>${x.client}`);check(x.styles.some(s=>/\/assets\/(?:bryme-v2|content-v2)\.css/.test(s)),`${label}: green stylesheet missing`);check(x.scripts.every(s=>/\/assets\//.test(s)||AD_HOSTS.test(s)),`${label}: unexpected scripts ${x.scripts.filter(s=>!AD_HOSTS.test(s)).join(', ')}`);const badImgs=x.badImages.filter(u=>!AD_HOSTS.test(u));check(badImgs.length===0,`${label}: broken images ${badImgs.join(', ')}`);const thirdParty=x.externalResources.filter(u=>!AD_HOSTS.test(u));check(thirdParty.length===0,`${label}: third-party resource ${thirdParty[0]||''}`);
   const noCurrent=[`/writers/`,`/writers/about/`,`/writers/author/ibrahim-sodiq/`,`/writers/editorial-policy/`,`/writers/corrections/`,`/writers/privacy/`,`/writers/terms/`,`/writers/disclaimer/`,`/writers/copyright/`,`/writers/contact/`,`/writers/tested/`,`/writers/disclosure/`,`/writers/newsletter/`,`/writers/studio/`];if(vp.name==="mobile"){check(x.bottomDisplay!=="none",`${label}: bottom navigation hidden`);check(x.bottomLinks===4,`${label}: bottom navigation has ${x.bottomLinks} links`);check(route==="/writers/"||noCurrent.includes(route)||x.bottomCurrent,`${label}: no current bottom-navigation item`);check(x.bottomHeight>=50,`${label}: bottom navigation too short (${x.bottomHeight})`);check(x.paddingBottom>=70,`${label}: insufficient bottom clearance (${x.paddingBottom})`)}else if(vp.name==="desktop"){check(x.bottomDisplay==="none",`${label}: bottom navigation visible on desktop`);check(x.topDisplay!=="none",`${label}: desktop navigation hidden`);check(x.topLinks.join('|')==="Learn|Publish|Tools|Intelligence",`${label}: desktop navigation is ${x.topLinks.join('|')}`);check(route==="/writers/"||noCurrent.includes(route)||x.topCurrent,`${label}: no current desktop-navigation item`)};
   if(routeErrors.length)failures.push(`${label}: ${routeErrors[0]}`);rendered++}catch(e){failures.push(`${label}: ${e.name}: ${e.message}`)}
  }await context.close()}
 const context=await browser.newContext({viewport:{width:390,height:844},serviceWorkers:"block"});const page=await context.newPage();/* Live properties render 200. Retired media families, unknown paths and the
    retired media answer 404 with the noindex 404 page (the unprefixed legacy
    roots moved to stub assertions below on 2026-09-16): the
    published artifact has no 410.html, so nothing answers 410 -- which matches
    production, where /movie/the-invite/ returns 404. /sports/ and /entertainment/
    were asserted as 410 here until 2026-09-15; both are live properties serving
    200 (111 and 806 sitemap URLs). domcontentloaded, not networkidle, so the
    YouTube thumbnails on /entertainment/ cannot stall the probe. */
   for(const route of ["/","/writers/","/sports/","/entertainment/","/tech/","/fitness/","/home/"]){const r=await page.goto(base+route,{waitUntil:"domcontentloaded"});check(r.status()===200,`${route}: browser HTTP ${r.status()}`)}
   for(const route of ["/movie/example/","/anime/","/not-a-page/"]){const r=await page.goto(base+route,{waitUntil:"domcontentloaded"});check(r.status()===404,`${route}: browser HTTP ${r.status()}`);const t404=(await page.textContent("body"))||"";check(/404/.test(t404)&&/(?:does not exist|never existed|page not found)/i.test(t404),`${route}: 404 explanation missing`)}
   /* Unprefixed legacy roots 2026-09-16: noindex meta-refresh stubs, not 404s.
      Production ignores the redirect rules declared in render.yaml (the live
      service was never synced to it and still runs dashboard-era rules), so
      scripts/purge-stale-publish.py ships the file-level equivalent: a stub per
      legacy root and per legacy sub-page, noindex,follow with an instant
      meta-refresh and canonical to the exact routed twin. Assert the stub shape
      and that a real browser lands on the twin. */
   for(const [route,twin] of [["/writing/","/writers/writing/"],["/guides/","/writers/guides/"],["/tools/","/writers/tools/"],["/today/","/writers/today/"]]){const sr=await page.request.get(base+route);check(sr.status()===200,`legacy stub ${route}: HTTP ${sr.status()}`);const th=await sr.text();check(/noindex/i.test(th),`legacy stub ${route}: lacks noindex`);check(!/index,follow/i.test(th.replace(/noindex,follow/g,"")),`legacy stub ${route}: looks indexable`);check(/http-equiv="refresh" content="0;url=\/writers\//i.test(th),`legacy stub ${route}: no instant meta-refresh to a /writers/ twin`);await page.goto(base+route,{waitUntil:"domcontentloaded"});await page.waitForURL(u=>u.pathname===twin,{timeout:5000}).catch(()=>{});check(page.url().endsWith(twin),`legacy stub ${route}: meta-refresh did not land on ${twin} (at ${page.url()})`)}await context.close();
 console.log(JSON.stringify({ok:failures.length===0,routes:routes.length,viewports:viewports.map(v=>`${v.width}x${v.height}`),renderedCases:rendered,failures:failures.slice(0,5000)},null,2));if(failures.length)process.exitCode=1;
}catch(e){console.error(e.stack||e);process.exitCode=1}finally{if(browser)await browser.close();child.kill("SIGTERM")}})();
