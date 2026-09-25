#!/usr/bin/env node
"use strict";
/**
 * BRYME Tech — living-hub behaviour gate (added with the 2026-09-24 rebuild).
 *
 * validate-browser.js proves the page renders and is silent; it does not touch
 * the desk machine, because that behaviour only exists on /tech/. This file is
 * the check that runs the changed code paths: filtering, the need router,
 * sorting, save-for-later, the command palette, the tracker-driven memory
 * panel, the no-JavaScript fallback and the reduced-motion path.
 *
 * It also re-asserts the rebuild's core promise: the hub links every piece on
 * the desk and creates no URL of its own.
 */
const net = require("net");
const path = require("path");
const { spawn } = require("child_process");
const { chromium } = require("playwright");

const ROOT = path.resolve(__dirname, "..");
const AD_HOSTS = /(?:profitableratecpmnetwork|highrevenueformat|monetag|highperformanceformat|n6wxm|nap5k|propellerads|googlesyndication|googleadservices|doubleclick|googletagmanager|google-analytics)\./i;
const failures = [];
const check = (ok, msg) => { if (!ok) failures.push(msg); };

function freePort() {
  return new Promise((resolve, reject) => {
    const s = net.createServer();
    s.listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => resolve(p)); });
    s.on("error", reject);
  });
}
async function ready(url, tries = 60) {
  for (let i = 0; i < tries; i++) {
    try { const r = await fetch(url); if (r.status === 200) return; } catch (e) {}
    await new Promise(r => setTimeout(r, 250));
  }
  throw new Error("server never became ready");
}
const errorsOf = (page, sink) => {
  page.on("console", m => { if (m.type() === "error" && !AD_HOSTS.test(m.text())) sink.push(`console: ${m.text()}`); });
  page.on("pageerror", e => { if (!AD_HOSTS.test(e.message)) sink.push(`page: ${e.message}`); });
};
const rowsOf = page => page.evaluate(() => {
  const rows = [...document.querySelectorAll(".tm-row")];
  return {
    total: rows.length,
    shown: rows.filter(r => !r.hidden).length,                 /* passing the filter */
    painted: rows.filter(r => !r.hidden && r.offsetParent !== null).length, /* also un-clipped */
    first: (rows.find(r => !r.hidden && r.offsetParent !== null) || {}).innerText || "",
    second: (rows.filter(r => !r.hidden && r.offsetParent !== null)[1] || {}).innerText || "",
    countText: (document.querySelector("[data-tm-count]") || {}).textContent || "",
    htmlClass: document.documentElement.className,
    shelvesHidden: [...document.querySelectorAll(".tm-shelf")].filter(s => s.hidden).length,
    memoryHidden: document.querySelector("[data-tm-memory]") ? document.querySelector("[data-tm-memory]").hidden : null,
    savedItems: document.querySelectorAll("[data-tm-saved] li").length,
    recentItems: document.querySelectorAll("[data-tm-recent] li").length,
    links: [...document.querySelectorAll(".tm-row-a")].map(a => a.getAttribute("href")).filter(Boolean),
    scroll: document.documentElement.scrollWidth,
    client: document.documentElement.clientWidth,
  };
});

(async () => {
  const port = await freePort();
  const base = `http://127.0.0.1:${port}`;
  const child = spawn(process.execPath, ["server/server.js"], {
    cwd: ROOT, env: { ...process.env, PORT: String(port), HOST: "127.0.0.1" }, stdio: "ignore",
  });
  let browser;
  try {
    await ready(base + "/healthz");
    browser = await chromium.launch({ headless: true });

    /* ---------------- 1. the desk wakes up (desktop) ---------------- */
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 1000 }, serviceWorkers: "block" });
    await ctx.route(AD_HOSTS, rt => rt.fulfill({ status: 200, contentType: "application/javascript", body: "" }));
    const errs = [];
    const page = await ctx.newPage();
    errorsOf(page, errs);
    await page.goto(base + "/tech/", { waitUntil: "networkidle" });

    let r = await rowsOf(page);
    check(r.htmlClass.includes("tm-js"), "html.tm-js not applied - the machine did not boot");
    check(r.total >= 200, `hub should index the whole desk, found ${r.total} rows`);
    check(r.shown === r.total, `a fresh hub should show the whole desk: ${r.shown}/${r.total}`);
    check(r.painted < r.total, "expected the long shelves to be collapsed on first paint");
    check(/\d+ of \d+ shown/.test(r.countText), `count readout missing: ${JSON.stringify(r.countText)}`);
    check(r.links.every(h => h.startsWith("/tech/")), "a row link is not a /tech/ URL");
    check(new Set(r.links).size === r.links.length, "duplicate row links in the index");
    check(r.scroll <= r.client + 2, `horizontal overflow at desktop: ${r.scroll} > ${r.client}`);
    const gaugeVals = await page.evaluate(() => [...document.querySelectorAll(".tm-gauge b")].map(b => b.textContent));
    check(gaugeVals.length === 6 && gaugeVals.every(v => /^\d+$/.test(v)), "gauges are not all real counts: " + JSON.stringify(gaugeVals));

    /* ---------------- 2. instant filter ---------------- */
    await page.fill("#tm-q", "dns");
    await page.waitForTimeout(250);
    r = await rowsOf(page);
    const filtered = r.shown;
    check(filtered > 0 && filtered < r.total, `filter "dns" produced ${filtered} of ${r.total}`);
    check(/^(\d+) of/.exec(r.countText) && Number(/^(\d+)/.exec(r.countText)[1]) === filtered, "count readout disagrees with visible rows");
    const allMatch = await page.evaluate(() => [...document.querySelectorAll(".tm-row")].filter(x => !x.hidden)
      .every(x => /dns/i.test(x.innerText)));
    check(allMatch, "a visible row does not match the filter text");
    await page.fill("#tm-q", "");
    await page.waitForTimeout(200);

    /* ---------------- 3. need router + chips ---------------- */
    await page.click('.tm-need[data-need="solve"]');
    await page.waitForTimeout(200);
    r = await rowsOf(page);
    check(r.shelvesHidden > 0, "the need router left every shelf visible");
    check((await page.getAttribute('.tm-need[data-need="solve"]', "aria-pressed")) === "true", "need tile not marked pressed");
    await page.click('.tm-need[data-need="solve"]');
    await page.waitForTimeout(150);
    await page.click('.tm-chip[data-kind="first-hand"]');
    await page.waitForTimeout(200);
    r = await rowsOf(page);
    check(r.shown > 0 && r.shown < 30, `first-hand chip left ${r.shown} rows visible`);
    const kindOk = await page.evaluate(() => [...document.querySelectorAll(".tm-row")].filter(x => !x.hidden)
      .every(x => x.getAttribute("data-kind") === "first-hand"));
    check(kindOk, "kind chip leaked rows of another kind");
    await page.keyboard.press("0");
    await page.waitForTimeout(200);
    r = await rowsOf(page);
    check(r.shown === r.total, `"0" did not clear the desk (${r.shown}/${r.total})`);

    /* ---------------- 4. sorting ---------------- */
    await page.click('.tm-sortb[data-sort="az"]');
    await page.waitForTimeout(200);
    r = await rowsOf(page);
    check(r.first.localeCompare(r.second) <= 0, "A-Z sort left the first two rows out of order");
    await page.click('.tm-sortb[data-sort="recent"]');
    await page.waitForTimeout(200);

    /* ---------------- 4b. a collapsed shelf can be opened ---------------- */
    const beforePaint = (await rowsOf(page)).painted;
    const moreBtn = page.locator(".tm-more:not([hidden])").first();
    if (await moreBtn.count()) {
      await moreBtn.click();
      await page.waitForTimeout(200);
      const afterPaint = (await rowsOf(page)).painted;
      check(afterPaint > beforePaint, `show-all did not expand the shelf (${beforePaint} -> ${afterPaint})`);
    } else {
      check(false, "no collapsed shelf offered a show-all control");
    }

    /* ---------------- 5. save + memory ---------------- */
    const firstUrl = await page.evaluate(() => document.querySelector(".tm-row-a").getAttribute("href"));
    await page.click(".tm-save");
    await page.waitForTimeout(150);
    check((await page.getAttribute(".tm-save", "aria-pressed")) === "true", "save button did not latch");
    let ls = await page.evaluate(() => localStorage.getItem("bryme.tech.saved.v1"));
    check(!!ls && ls.includes(firstUrl), "saved list was not written to localStorage");
    check(!!ls && !/"u":"\/(?!tech\/)/.test(ls), "a saved URL is unrouted - routing rewrites href only, never custom attributes: " + ls);
    r = await rowsOf(page);
    check(r.memoryHidden === false, "memory panel did not open after saving");
    check(r.savedItems === 1, `memory shows ${r.savedItems} saved items, expected 1`);
    await page.click('.tm-chip[data-saved="1"]');
    await page.waitForTimeout(200);
    r = await rowsOf(page);
    check(r.shown === 1, `saved-only filter showed ${r.shown} rows, expected 1`);
    await page.keyboard.press("0");
    await page.waitForTimeout(150);

    /* ---------------- 6. tracker -> continue reading ---------------- */
    await page.goto(base + "/tech/web-hosting-costs-explained/", { waitUntil: "networkidle" });
    const seen = await page.evaluate(() => localStorage.getItem("bryme.tech.seen.v1") || "");
    check(seen.includes("/tech/web-hosting-costs-explained/"), "article visit was not recorded: " + seen.slice(0, 120));
    await page.goto(base + "/tech/", { waitUntil: "networkidle" });
    r = await rowsOf(page);
    check(r.recentItems >= 1, `continue-reading is empty after a real visit (${r.recentItems})`);
    check(await page.isHidden("[data-tm-recent-empty]"), "recent-empty note shown while entries exist");

    /* ---------------- 6b. freshness engine prints real derived dates ---------------- */
    const cad = await page.evaluate(() => {
      const el = [...document.querySelectorAll(".tm-ro-h")].find(x => /Verification cadence/i.test(x.textContent));
      if (!el) return null;
      const box = el.closest(".tm-readout");
      const t = box.querySelector("time");
      return { now: t ? t.getAttribute("datetime") : "", text: box.textContent };
    });
    check(!!cad, "verification-cadence readout missing from the self-read band");
    check(!!cad && /^\d{4}-\d{2}-\d{2}$/.test(cad.now), "cadence clock is not a real date: " + (cad && cad.now));
    check(!!cad && /Next review on the calendar:/.test(cad.text), "cadence readout lacks the next-review date");

    /* ---------------- 6c. private on-device numbers (opt-in) ---------------- */
    await page.click("[data-tm-mine-toggle]");
    await page.waitForTimeout(150);
    const mine = await page.evaluate(() => {
      const box = document.querySelector("[data-tm-mine]");
      const num = sel => { const e = box.querySelector(sel); return e ? e.textContent : null; };
      return { hidden: box.hidden, opened: Number(num("[data-tm-mine-opened]")), opens: Number(num("[data-tm-mine-opens]")), saved: Number(num("[data-tm-mine-saved]")) };
    });
    check(mine.hidden === false, "private numbers box did not open");
    check(mine.opened >= 1 && mine.opens >= 1, `private numbers not counted from local storage (${JSON.stringify(mine)})`);

    /* ---------------- 7. command palette ---------------- */
    await page.keyboard.press("Control+k");
    await page.waitForTimeout(200);
    check(await page.isVisible("[data-tm-palette]"), "Ctrl+K did not open the palette");
    await page.fill("#tm-pal-q", "vpn");
    await page.waitForTimeout(200);
    const hits = await page.locator("[data-tm-pal] li[role='option']").count();
    check(hits > 0, "palette found nothing for 'vpn'");
    const target = await page.getAttribute("[data-tm-pal] li[role='option'] a", "href");
    await page.keyboard.press("Enter");
    await page.waitForTimeout(400);
    check(page.url().includes(target), `palette Enter did not open ${target} (at ${page.url()})`);

    /* ---------------- 8. deep cut stays on-desk ---------------- */
    await page.goto(base + "/tech/", { waitUntil: "networkidle" });
    const diceHref = await page.evaluate(() => {
      const a = document.querySelector("[data-tm-dice]");
      const rows = [...document.querySelectorAll(".tm-row-a")];
      return { present: !!a && !a.hidden, n: rows.length };
    });
    check(diceHref.present && diceHref.n > 100, "random deep cut missing or desk too small");

    /* ---------------- 9. dark theme, no overflow, silent ---------------- */
    await page.click("[data-theme-toggle]");
    await page.waitForTimeout(250);
    const darkBoot = await page.evaluate(() => ({
      theme: document.documentElement.getAttribute("data-theme"),
      h1: getComputedStyle(document.querySelector(".tm-h1")).color,
      bg: getComputedStyle(document.querySelector(".tm-machine")).backgroundColor,
    }));
    check(darkBoot.theme === "dark", "dark theme did not apply on the hub");
    check(darkBoot.h1 !== darkBoot.bg, "dark theme paints the headline in the background colour");
    check(errs.length === 0, "console/page errors on the desk: " + errs.join(" | "));

    /* ---------------- 10. no-JavaScript fallback ---------------- */
    const nojs = await browser.newContext({ viewport: { width: 390, height: 844 }, javaScriptEnabled: false });
    const p2 = await nojs.newPage();
    await p2.goto(base + "/tech/", { waitUntil: "domcontentloaded" });
    const nj = await p2.evaluate(() => ({
      htmlClass: document.documentElement.className,
      rows: document.querySelectorAll(".tm-row").length,
      hiddenRows: [...document.querySelectorAll(".tm-row")].filter(x => x.hidden).length,
      shelfHidden: [...document.querySelectorAll(".tm-shelf")].filter(x => x.hidden).length,
      toolbarVisible: !!document.querySelector(".tm-toolbar") && document.querySelector(".tm-toolbar").offsetParent !== null,
      noscriptNote: getComputedStyle(document.querySelector(".tm-noscript")).display !== "none",
      clipped: document.querySelectorAll(".tm-clipped").length,
      links: [...document.querySelectorAll(".tm-row-a")].filter(a => a.getAttribute("href")).length,
      scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth,
    }));
    check(!nj.htmlClass.includes("tm-js"), "html.tm-js applied without JavaScript");
    check(nj.hiddenRows === 0 && nj.shelfHidden === 0, `no-JS hides content: ${nj.hiddenRows} rows, ${nj.shelfHidden} shelves`);
    check(nj.clipped === 0, "no-JS left a shelf clipped");
    check(nj.toolbarVisible === false, "the filter toolbar is visible without JavaScript (dead control)");
    check(nj.noscriptNote === true, "no-JS note is not shown");
    check(nj.links === nj.rows && nj.rows > 100, "no-JS index is incomplete");
    check(nj.scroll <= nj.client + 2, `no-JS horizontal overflow on mobile: ${nj.scroll} > ${nj.client}`);

    /* ---------------- 11. reduced motion ---------------- */
    const rm = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: "reduce" });
    const p3 = await rm.newPage();
    const errs3 = [];
    errorsOf(p3, errs3);
    await p3.goto(base + "/tech/", { waitUntil: "networkidle" });
    const rmState = await p3.evaluate(() => {
      const band = document.querySelector(".tm-band");
      return { opacity: getComputedStyle(band).opacity, anim: band.classList.contains("tm-anim"), scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth };
    });
    check(rmState.opacity === "1", "reduced-motion visitor sees a faded band (opacity " + rmState.opacity + ")");
    check(rmState.anim === false, "reduced-motion still registered a reveal animation");
    check(rmState.scroll <= rmState.client + 2, `mobile horizontal overflow: ${rmState.scroll} > ${rmState.client}`);
    check(errs3.length === 0, "console/page errors on mobile: " + errs3.join(" | "));
    await p3.screenshot({ path: path.join(ROOT, "reports/tech-hub-2026-09-24/hub-mobile.png") });
    await page.setViewportSize({ width: 1440, height: 1000 });
    await page.goto(base + "/tech/", { waitUntil: "networkidle" });
    await page.screenshot({ path: path.join(ROOT, "reports/tech-hub-2026-09-24/hub-desktop.png") });

    await ctx.close(); await nojs.close(); await rm.close();
  } finally {
    if (browser) await browser.close();
    child.kill();
  }

  if (failures.length) {
    console.error(`FAIL (${failures.length})`);
    failures.forEach(f => console.error("  - " + f));
    process.exit(1);
  }
  console.log(JSON.stringify({ ok: true, gate: "tech-hub behaviour", assertions: "filter, need router, chips, sort, save, tracker memory, palette, no-JS, reduced motion, dark theme, overflow" }, null, 2));
})().catch(e => { console.error("harness error:", e); process.exit(1); });
