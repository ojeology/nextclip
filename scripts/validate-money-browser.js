#!/usr/bin/env node
/* Money retirement browser gate (owner decision 2026-10-01, AdSense review).

   Formerly a Playwright sweep of the Money hub, 13 guides and legacy pages
   (layout, nav, calculator, local resources). The desk is retired: files are
   absent from the artifact, so every /money/* URL must answer 404 by absence
   with NO redirect hop (Render static cannot emit 410; 404-by-absence is the
   house pattern, same as the retired /movie/ family). This gate now proves
   exactly that against the real local server, plus the surviving-cards side
   of the decision: catalogue cards stay published at 200 with noindex,follow,
   and the delisted catalogue sitemap serves an empty urlset.

   Deliberately fetch-based (no Playwright): there is no Money page left to
   render, so a headless browser adds minutes and zero coverage. The npm
   script name (validate:money:browser) is kept so CI wiring is unchanged. */
"use strict";
const path = require("node:path"), net = require("node:net");
const {spawn} = require("node:child_process");
const ROOT = path.resolve(__dirname, "..");
const failures = [];
const check = (ok, label) => {if (!ok) failures.push(label)};

const freePort = () => new Promise((res, rej) => {const s = net.createServer();
  s.listen(0, "127.0.0.1", () => {const p = s.address().port; s.close(() => res(p))}); s.on("error", rej)});
async function ready(url) {
  for (let i = 0; i < 70; i++) {
    try {if ((await fetch(url)).ok) return;} catch {}
    await new Promise(r => setTimeout(r, 100));
  }
  throw new Error("local server did not start");
}

(async () => {
  const port = await freePort(), base = `http://127.0.0.1:${port}`;
  const child = spawn(process.execPath, ["server/server.js"], {cwd: ROOT,
    env: {...process.env, PORT: String(port), HOST: "127.0.0.1"}, stdio: "ignore"});
  let probed = 0;
  try {
    await ready(base + "/healthz");
    const get = async u => {const r = await fetch(base + u, {redirect: "manual"}); probed++; return r};

    /* 1. Retired desk: 404 by absence, no redirect hop, no Location header.
          Covers the hub, a live guide, the two batch-7 legacy URLs whose 301s
          were removed with the desk, and a tool page. */
    for (const u of ["/money/", "/money/how-to-save-for-a-house-deposit/",
                     "/money/saving-for-a-house-deposit-explained/",
                     "/money/saving-for-a-house-deposit-explained",
                     "/money/apr-vs-apy-explained/", "/money/position-size-calculator/",
                     "/money/sitemap.xml"]) {
      const r = await get(u);
      check(r.status === 404, `${u}: expected 404 by absence, got ${r.status}${r.headers.get("location") ? " -> " + r.headers.get("location") : ""}`);
      check(!r.headers.get("location"), `${u}: retired URL must not redirect (found Location: ${r.headers.get("location")})`);
    }

    /* 2. Homepage and trust pages: published, 200, and no Money nav link. */
    for (const u of ["/", "/about/", "/privacy/", "/event-calendar/"]) {
      const r = await get(u);
      check(r.status === 200, `${u}: expected 200, got ${r.status}`);
      const body = await r.text();
      check(!body.includes('href="/money/'), `${u}: still links to the retired Money desk`);
    }

    /* 3. Catalogue cards survive at 200 but are de-indexed (noindex,follow)
          with internal links intact - the don't-delete-URLs decision. */
    for (const u of ["/entertainment/movie/war-of-the-worlds/",
                     "/entertainment/movie/the-intouchables/"]) {
      const r = await get(u);
      check(r.status === 200, `card ${u}: expected 200 (URLs must stay live), got ${r.status}`);
      if (r.status === 200) {
        const body = await r.text();
        check(/name="robots" content="noindex,follow"/.test(body), `card ${u}: missing noindex,follow meta`);
        check(body.includes('href="/entertainment/'), `card ${u}: internal links lost`);
      }
    }

    /* 4. Discovery surfaces served live: delisted catalogue sitemap is an
          empty urlset; root index and robots carry no money/catalogue. */
    const cat = await get("/entertainment/sitemap-catalogue.xml");
    check(cat.status === 200, `catalogue sitemap: expected 200 (file stays served, just empty), got ${cat.status}`);
    check(!(await cat.text()).includes("<loc>"), "catalogue sitemap still submits <loc> entries");
    const sm = await get("/sitemap.xml");
    check(sm.status === 200, `root sitemap: expected 200, got ${sm.status}`);
    const smBody = await sm.text();
    check(!/money/.test(smBody), "root sitemap still references money");
    check(!/sitemap-catalogue/.test(smBody), "root sitemap still registers the delisted catalogue");
    const rb = await get("/robots.txt");
    check(rb.status === 200, `robots: expected 200, got ${rb.status}`);
    check(!/\/money\//.test(await rb.text()), "robots.txt still references /money/");
  } finally {
    child.kill("SIGTERM");
  }

  if (failures.length) {
    console.error(`money-retirement browser gate: ${failures.length} failure(s) over ${probed} probes`);
    for (const f of failures) console.error("  ✗ " + f);
    process.exit(1);
  }
  console.log(`money-retirement browser gate: green - ${probed} probes: /money/* 404 by absence (no redirects), hub/trust pages Money-free, cards 200 + noindex,follow, catalogue sitemap empty`);
})().catch(e => {console.error("money-retirement browser gate crashed:", e); process.exit(1)});
