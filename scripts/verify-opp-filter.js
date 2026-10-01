#!/usr/bin/env node
/* Browser verification for the 2026-09-30 eligibility-discovery fix.

   Drives the real /writers/writing/ filter in a real browser and asserts the
   things that were broken or that the fix could plausibly have broken.

   The counts here are DERIVED from content/opportunities.json, not hardcoded.
   They used to be literals (142 cards, 77 worldwide, 49 not-stated), which
   meant every verified batch of new markets broke the gate for a reason that
   was not a regression. Deriving them keeps the gate honest in both
   directions: it still fails if the page and the data disagree, but adding a
   verified record no longer looks like a bug.

   The rule being asserted, straight from the data:
     "Open worldwide"        == records whose eligibility.mode is open|worldwide
     "Eligibility not stated"== records whose eligibility.mode is not-stated
   Neither may absorb the other. That is the defect this file exists for: the
   filter used to answer "open worldwide - 127" by treating a guideline that
   says nothing about geography as though it said "everyone is welcome". */
"use strict";
const path = require("node:path"), net = require("node:net"), fs = require("node:fs");
const { spawn } = require("node:child_process"), { chromium } = require("playwright");
const ROOT = path.resolve(__dirname, "..");

const AD_HOSTS = /(?:profitableratecpmnetwork|highrevenueformat|monetag|highperformanceformat|n6wxm|nap5k|propellerads|googlesyndication|googleadservices|doubleclick|googletagmanager|google-analytics|fundingchoicesmessages)\./i;
const freePort = () => new Promise((res, rej) => { const s = net.createServer(); s.listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => res(p)); }); s.on("error", rej); });
async function ready(url) { for (let i = 0; i < 70; i++) { try { if ((await fetch(url)).ok) return; } catch {} await new Promise(r => setTimeout(r, 100)); } throw new Error("server did not start"); }

// ---- expectations, computed from the dataset ------------------------------
const DATA = path.join(ROOT, "content", "opportunities.json");
if (!fs.existsSync(DATA)) { console.error(`verify-opp-filter: no dataset at ${DATA}`); process.exit(2); }
const records = JSON.parse(fs.readFileSync(DATA, "utf8")).opportunities;
const modeOf = r => (r.eligibility || {}).mode || "unknown";
const EXPECT_TOTAL = records.length;
const EXPECT_INTL = records.filter(r => ["open", "worldwide"].includes(modeOf(r))).length;
const EXPECT_NOT_STATED = records.filter(r => modeOf(r) === "not-stated").length;

/* The experience facet, derived the same way. `experience` is assigned only from
   a publication's own guideline, so:
     "first-timer-friendly" == records whose guideline says unpublished writers
                                are welcome
     "stated"               == the union of the three named stages, i.e. every
                                record that said anything about who may submit
   Records whose guideline could not be read carry `not-stated`, exactly like a
   record whose guideline was read and was silent, so neither may appear under
   a named stage. That is the whole point of the field. */
const expOf = r => r.experience || "not-stated";
const EXPECT_FTF = records.filter(r => expOf(r) === "first-timer-friendly").length;
const EXPECT_EMERGING = records.filter(r => expOf(r) === "emerging").length;
const EXPECT_ESTABLISHED = records.filter(r => expOf(r) === "established").length;
const EXPECT_STATED = records.filter(r => expOf(r) !== "not-stated").length;

// BASED+NG: records the country map places in Nigeria.
const PUBC = path.join(ROOT, "content", "hub", "pub-countries.json");
const countries = fs.existsSync(PUBC) ? JSON.parse(fs.readFileSync(PUBC, "utf8")) : {};
const EXPECT_BASED_NG = records.filter(r => (countries[r.slug] || {}).base === "NG").length;

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
      return route.fulfill({ status: 200, contentType: "application/javascript", body: "" });
    });
    const page = await ctx.newPage();
    const errors = [];
    page.on("pageerror", e => errors.push("pageerror: " + e.message));
    page.on("console", m => { if (m.type() === "error") errors.push("console: " + m.text()); });
    await page.goto(base + "/writers/writing/", { waitUntil: "domcontentloaded" });
    await page.waitForSelector(".job-card");

    const total = await page.locator(".job-card").count();
    console.log(`\n/writers/writing/ — ${total} cards rendered (dataset: ${EXPECT_TOTAL} records)\n`);
    check(total === EXPECT_TOTAL, `every record renders a card (${EXPECT_TOTAL}, got ${total})`);

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
    check(ngCount > 0 && ngCount < EXPECT_TOTAL,
      `OPENTO+NG is a real filter, not everything (${ngCount} of ${EXPECT_TOTAL})`);

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
    check(intl === EXPECT_INTL,
      `"Open worldwide" equals the records that actually say so (${EXPECT_INTL}, got ${intl})`);
    check(intl < EXPECT_TOTAL,
      `"Open worldwide" is a subset, not everything (${intl} of ${EXPECT_TOTAL})`);
    check(!(await slugVisible("litmag-online")),
      "a not-stated guideline is NOT listed as open worldwide");

    await setSel("#f-country", "notstated");
    const ns = await visible();
    check(ns === EXPECT_NOT_STATED,
      `"Eligibility not stated" equals the silent records (${EXPECT_NOT_STATED}, got ${ns})`);
    check(EXPECT_INTL + EXPECT_NOT_STATED < EXPECT_TOTAL,
      "the two options are disjoint, and neither absorbs the restricted records");
    check(await slugVisible("litmag-online"), "the not-stated option does show the silent records");

    // ---- 4. based mode still means based ------------------------------
    await setSel("#f-country", "NG");
    await setSel("#f-cmode", "based");
    const based = await visible();
    check(based === EXPECT_BASED_NG,
      `BASED+NG equals the records the country map places in Nigeria (${EXPECT_BASED_NG}, got ${based})`);
    check(!(await slugVisible("afrolicious")), "BASED+NG correctly excludes an unbased record");

    await setSel("#f-country", "all");
    check((await visible()) === EXPECT_TOTAL, "reset to All shows every card again");

    // ---- 5. the new India batch is reachable from the filter ----------
    // India exists as a country option only because IN is in COUNTRY_PROFILES;
    // this guards the wiring between the dataset and the atlas route.
    const inCards = records.filter(r => (countries[r.slug] || {}).base === "IN");
    if (inCards.length) {
      await setSel("#f-cmode", "based");
      await setSel("#f-country", "IN");
      const india = await visible();
      check(india === inCards.length,
        `BASED+IN equals the India records (${inCards.length}, got ${india})`);
      check(await slugVisible(inCards[0].slug), `BASED+IN shows ${inCards[0].slug}`);
      await setSel("#f-country", "all");
    }

    // ---- 6. the experience facet, and the URL that drives it ----------
    // These are the links the beginner pages use. They are asserted through the
    // URL rather than the control, because a shareable link is what a reader
    // actually receives - if only the select worked, the CTAs would still be
    // broken for everyone who clicked one.
    const viaUrl = async qs => {
      await page.goto(base + "/writers/writing/" + qs, { waitUntil: "domcontentloaded" });
      // "attached", not visible: a filtered page has cards present but hidden,
      // and waiting for a VISIBLE card times out on exactly the URLs where the
      // filter worked.
      await page.waitForSelector(".job-card", { state: "attached" });
      await page.waitForTimeout(250);
      return visible();
    };
    await setSel("#f-exp", "first-timer-friendly");
    const ftf = await visible();
    check(ftf === EXPECT_FTF,
      `experience=first-timer-friendly equals the welcoming records (${EXPECT_FTF}, got ${ftf})`);
    check(ftf > 0 && ftf < EXPECT_TOTAL, "and it is a real subset, not everything");

    await setSel("#f-exp", "emerging");
    const emg = await visible();
    check(emg === EXPECT_EMERGING, `experience=emerging (${EXPECT_EMERGING}, got ${emg})`);

    await setSel("#f-exp", "established");
    const est = await visible();
    check(est === EXPECT_ESTABLISHED, `experience=established (${EXPECT_ESTABLISHED}, got ${est})`);

    await setSel("#f-exp", "stated");
    const stated = await visible();
    check(stated === EXPECT_STATED,
      `experience=stated is the union of the named stages (${EXPECT_STATED}, got ${stated})`);
    check(stated === ftf + emg + est,
      `and it equals its parts (${ftf}+${emg}+${est}=${ftf + emg + est}, got ${stated})`);

    // A record whose guideline could not be read must never be filtered into a
    // welcome. agni is one of the nine; it is not stated, and it is not read.
    const unread = records.filter(r => expOf(r) === "not-stated").map(r => r.slug);
    if (unread.length) {
      await setSel("#f-exp", "first-timer-friendly");
      check(!(await slugVisible(unread[0])),
        `a record with no stated stage (${unread[0]}) is not listed as welcoming beginners`);
    }

    check((await viaUrl("?experience=first-timer-friendly")) === EXPECT_FTF,
      "the URL the beginner pages link to filters correctly on load");
    check((await viaUrl("?experience=stated")) === EXPECT_STATED,
      "the URL the browse index links to filters correctly on load");

    await page.goto(base + "/writers/writing/", { waitUntil: "domcontentloaded" });
    await page.waitForSelector(".job-card", { state: "attached" });
    await page.waitForTimeout(250);
    check((await visible()) === EXPECT_TOTAL, "and a bare URL shows everything again");

    check(errors.length === 0, `no console/page errors (${errors.slice(0, 2).join(" | ") || "none"})`);
  } finally {
    if (browser) await browser.close();
    child.kill("SIGKILL");
  }
  console.log(failures.length ? `\nFAILED (${failures.length})\n` : "\nALL ASSERTIONS PASSED\n");
  process.exit(failures.length ? 1 : 0);
})();
