#!/usr/bin/env node
/* Money publication browser gate: 13 guides + hub + corrected legacy pages.
   Checks mobile/desktop layout, local resources, navigation and risk calculator.
   External AdSense/GA loaders are stubbed, as they are in the Writers gate. */
"use strict";
const fs = require("node:fs"), path = require("node:path"), net = require("node:net");
const {spawn} = require("node:child_process"), {chromium} = require("playwright");
const ROOT = path.resolve(__dirname, "..");
const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, "content/money-guides/manifest.json"), "utf8"));
const routes = ["/money/", ...manifest.articles.map(g => `/money/${g.slug}/`),
  "/money/position-size-calculator/", "/money/position-sizing-101/",
  "/money/trade-types-explained/", "/money/technical-indicators-explained/"];
const failures = [];
const check = (ok, label) => {if (!ok) failures.push(label)};
const AD_HOSTS = /(?:profitableratecpmnetwork|highrevenueformat|monetag|highperformanceformat|n6wxm|nap5k|propellerads|googlesyndication|googleadservices|doubleclick|googletagmanager|google-analytics)\./i;
const freePort = () => new Promise((res,rej)=>{const s=net.createServer();s.listen(0,"127.0.0.1",()=>{const p=s.address().port;s.close(()=>res(p))});s.on("error",rej)});
async function ready(url) {
  for (let i=0; i<70; i++) {
    try {if ((await fetch(url)).ok) return;} catch {}
    await new Promise(r=>setTimeout(r,100));
  }
  throw new Error("local server did not start");
}
(async()=>{
  const port = await freePort(), base = `http://127.0.0.1:${port}`;
  const child = spawn(process.execPath, ["server/server.js"], {
    cwd:ROOT, env:{...process.env,PORT:String(port),HOST:"127.0.0.1"},stdio:"ignore"
  });
  let browser;
  try {
    await ready(base + "/healthz");
    browser = await chromium.launch({headless:true});
    for (const viewport of [{name:"mobile",width:390,height:844},{name:"desktop",width:1440,height:960}]) {
      const context = await browser.newContext({viewport:{width:viewport.width,height:viewport.height},serviceWorkers:"block"});
      await context.route("**/*", async request => {
        const url = request.request().url();
        if (url.startsWith(base)) return request.continue();
        if (!AD_HOSTS.test(url)) errors.push(`unexpected third-party request: ${url}`);
        const type = request.request().resourceType();
        return request.fulfill({status:200,contentType:type==="image"?"image/gif":"application/javascript",body:""});
      });
      const page = await context.newPage();
      let errors=[];
      page.on("pageerror", err=>errors.push("page error: " + err.message));
      page.on("console", msg=>{if(msg.type()==="error")errors.push("console: " + msg.text())});
      page.on("response", r=>{if(r.url().startsWith(base)&&r.status()>=400)errors.push(`HTTP ${r.status()}: ${r.url()}`)});
      page.on("requestfailed", r=>{if(r.url().startsWith(base))errors.push(`failed: ${r.url()} ${r.failure()?.errorText||""}`)});
      for (const route of routes) {
        const label = `${viewport.name} ${route}`;
        errors=[];
        try {
          const response = await page.goto(base + route, {waitUntil:"networkidle",timeout:16000});
          check(response?.status()===200,`${label}: HTTP ${response?.status()}`);
          const state = await page.evaluate(()=>({
            h1:document.querySelectorAll("h1").length,
            text:(document.querySelector("main#main")?.innerText||"").trim().length,
            scroll:document.documentElement.scrollWidth,
            client:document.documentElement.clientWidth,
            toc:!!document.querySelector(".money-toc"),
            images:[...document.images].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src)
          }));
          check(state.h1===1, `${label}: expected exactly one H1`);
          check(state.text >= (route==="/money/"?900:450), `${label}: rendered main text too short (${state.text})`);
          check(state.scroll <= state.client + 2, `${label}: horizontal overflow ${state.scroll}>${state.client}`);
          check(state.images.length===0, `${label}: broken images ${state.images[0]||""}`);
          if (manifest.articles.some(g=>route===`/money/${g.slug}/`)) check(state.toc, `${label}: missing article table of contents`);
          if (route==="/money/" && viewport.name==="mobile") {
            await page.locator("[data-drawer-open]").click();
            check(await page.locator("#site-drawer").getAttribute("aria-hidden")==="false",`${label}: menu does not open`);
            check((await page.locator("#site-drawer a[href^='/money/']").count()) >= manifest.articles.length, `${label}: guides not in drawer`);
            await page.keyboard.press("Escape");
            check(await page.locator("#site-drawer").getAttribute("aria-hidden")==="true",`${label}: escape does not close menu`);
          }
          check(errors.length===0, `${label}: ${errors[0]||"resource error"}`);
        } catch(e) {failures.push(`${label}: ${e.message}`)}
      }
      // A real browser exercise of the pre-existing calculator after its
      // precision/wording correction. EUR/USD quote and balance are both USD.
      if (viewport.name==="desktop") {
        await page.goto(base + "/money/position-size-calculator/",{waitUntil:"networkidle"});
        await page.locator("#mc-balance").fill("5000");
        await page.locator("#mc-risk").fill("1");
        await page.locator("#mc-entry").fill("1.0850");
        await page.locator("#mc-stop").fill("1.0825");
        let value = await page.locator("#mc-out").innerText();
        check(value.includes("0.20 lots"), `calculator: EUR/USD example should show 0.20 lots, got ${value.slice(0,150)}`);
        check(value.includes("before fees, gaps"), "calculator: risk caveat not visible in the output");
        await page.locator("#mc-balance").fill("100");
        value = await page.locator("#mc-out").innerText();
        check(value.includes("below 0.01 lot"), "calculator: sub-minimum size should not be rounded UP");
        await page.locator("#mc-risk").fill("101");
        value = await page.locator("#mc-out").innerText();
        check(value.includes("between 0 and 100%"), "calculator: risk >100% should be rejected");
      }
      await context.close();
    }
    console.log(JSON.stringify({ok:failures.length===0,moneyRoutes:routes.length,viewportCases:routes.length*2,calculator:true,failures:failures.slice(0,80)},null,2));
    if(failures.length)process.exitCode=1;
  } catch(e) {console.error(e.stack||String(e));process.exitCode=1}
  finally {if(browser)await browser.close();child.kill("SIGTERM")}
})();
