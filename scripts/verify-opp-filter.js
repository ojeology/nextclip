#!/usr/bin/env node
/* One-off verification for the 2026-09-30 eligibility-discovery fix.
   Drives the real /writers/writing/ filter in a real browser and asserts the
   four things that were broken or that the fix could plausibly have broken. */
"use strict";
const path = require("node:path"), net = require("node:net");
const { spawn } = require("node:child_process"), { chromium } = require("playwright");
const ROOT = path.resolve(__dirname, "..");

const AD_HOSTS = /(?:profitableratecpmnetwork|highrevenueformat|monetag|highperformanceformat|n6wxm|nap5k|propellerads|googlesyndication|googleadservices|doubleclick|googletagmanager|google-analytics|fundingchoicesmessages)\./i;
const freePort = () => new Promise((res, rej) => { const s = net.createServer(); s.listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => res(p)); }); s.on("error", rej); });
async function ready(url) { for (let i = 0; i < 70; i++) { try { if ((await fetch(url)).ok) return; } catch {} await new Promise(r => setTimeout(r, 100)); } throw new Error("server did not start"); }

const failures = [];
const check = (ok, label) => { console.log((ok ? "  PASS  " : "  FAIL  ") + label); if (!ok) failures.push(label); };

(async () => {
  const port = await freePort(), base = `http://127.0.0.1:${port}`;
  const child = spawn(process.execPath, ["server/server.js"], { cwd: ROOT, env: { ...process.env, PORT: String(port), HOST: "127.0.0.1" }, stdio: "ignore" });
  let browser;
  try {
    await ready(base + "/healthz");
    browser = await chromium.launch({ headless: true });
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 1000 }, serviceWorkers: "block" });
    await ctx.route("**/*", async route => {
      const url = route.request().url();
      if (url.startsWith(base)) return route.continue();
      if (!AD_HOSTS.test(url)) return route.fulfill({ status: 200, contentType: "application/javascript", body: "" });
      return route.fulfill({ status: 200, contentType: "application/javascript", body: "" });
    });
    const page = await ctx.newPage();
    const errors = [];
    page.on("pageerror", e => errors.push("pageerror: " + e.message));
    page.on("console", m => { if (m.type() === "error") errors.push("console: " + m.text()); });
    await page.goto(base + "/writers/writing/", { waitUntil: "domcontentloaded" });
    await page.waitForSelector(".job-card");

    const total = await page.locator(".job-card").count();
    console.log(`\n/writers/writing/ — ${total} cards rendered\n`);
    check(total === 142, `142 cards rendered (got ${total})`);

    /* The filter hides cards with the `hidden` attribute, so assert on that
       directly rather than on a visibility pseudo-class. */
    const visible = async () => page.evaluate(() =>
      [...document.querySelectorAll(".job-card")].filter(c => !c.hidden).length);
    const slugVisible = async s => page.evaluate(slug =>
      document.querySelectorAll(`.job-card:not([hidden]) a[href="/writers/writing/${slug}/"]`).length > 0, s);
    const setSel = async (sel, val) => { await page.selectOption(sel, val); await page.waitForTimeout(150); };

    // ---- 1. the regression this fix exists for -------------------------
    await setSel("#f-cmode", "opento");
    await setSel("#f-country", "NG");
    check(await slugVisible("afrolicious"),
      "OPENTO+NG shows Afrolicious (its own record says \"Nigeria qualifies\")");
    const ngCount = await visible();
    check(ngCount > 0 && ngCount < 142, `OPENTO+NG is a real filter, not everything (${ngCount} of 142)`);

    await setSel("#f-country", "KE");
    check(await slugVisible("afrolicious"), "OPENTO+KE shows Afrolicious (africa region expands)");

    // ---- 2. a named country list ---------------------------------------
    await setSel("#f-country", "ZA");
    check(await slugVisible("listverse"), "OPENTO+ZA shows Listverse (it names South Africa in includesCountries)");
    await setSel("#f-country", "AU");
    check(await slugVisible("listverse"), "OPENTO+AU shows Listverse");

    await setSel("#f-country", "AU");
    check(await slugVisible("island-magazine"), "OPENTO+AU shows Island (australia region, restricted)");

    // ---- 3. the honesty correction -------------------------------------
    await setSel("#f-country", "international");
    const intl = await visible();
    check(intl === 77, `"Open worldwide" is 77, not 127 (got ${intl})`);
    check(!(await slugVisible("litmag-online")),
      "a not-stated guideline is NOT listed as open worldwide");

    await setSel("#f-country", "notstated");
    const ns = await visible();
    check(ns === 49, `"Eligibility not stated" is 49 (got ${ns})`);
    check(await slugVisible("litmag-online"), "the not-stated option does show the silent records");

    // ---- 4. based mode still means based ------------------------------
    await setSel("#f-country", "NG");
    await setSel("#f-cmode", "based");
    const based = await visible();
    check(based === 5, `BASED+NG is still 5 publications (got ${based})`);
    check(!(await slugVisible("afrolicious")), "BASED+NG correctly excludes an unbased record");

    await setSel("#f-country", "all");
    check((await visible()) === 142, "reset to All shows every card again");

    check(errors.length === 0, `no console/page errors (${errors.slice(0, 2).join(" | ") || "none"})`);
  } finally {
    if (browser) await browser.close();
    child.kill("SIGKILL");
  }
  console.log(failures.length ? `\nFAILED (${failures.length})\n` : "\nALL ASSERTIONS PASSED\n");
  process.exit(failures.length ? 1 : 0);
})();
