#!/usr/bin/env node
/* End-to-end browser check for the Adsterra consent gate & Monetag removal. */
"use strict";
const fs = require("fs");
const path = require("path");
const http = require("http");
const {spawn} = require("child_process");
const {chromium} = require("playwright");

const ROOT = path.resolve(__dirname, "..");
const cfg = JSON.parse(fs.readFileSync(path.join(ROOT, "site.config.json"), "utf8"));
const ast = cfg.adsterra || {};

const EXPECTED_UNITS = (() => {
  if (!ast.enabled) return 0;
  let n = 0;
  const pl = ast.placements || {};
  for (const k of Object.keys(pl)) {
    const u = pl[k] || {};
    if (u.enabled !== false && u.key && u.host) n++;
  }
  if (!n && ast.key && ast.host) n++;
  const disp = ast.displayBanner || {};
  if (disp.enabled !== false && disp.key && disp.host) n++;
  const sb = ast.socialBar || {};
  if (sb.enabled !== false && sb.script) n++;
  return n;
})();

const AD_HOST = /profitableratecpmnetwork\.com|highrevenueformat\.com|highperformanceformat\.com/i;
const MONETAG_HOST = /nap5k\.com|n6wxm\.com|monetag\.com/i;
const GOOGLE_HOST = /googletagmanager\.com|google-analytics\.com|googlesyndication\.com|doubleclick\.net|fundingchoicesmessages\.google\.com/i;
const EMPTY_JS = {status: 200, contentType: "application/javascript", body: "/* stubbed */"};

function ready(url, timeoutMs = 15000) {
  const deadline = Date.now() + timeoutMs;
  return new Promise((resolve, reject) => {
    const tick = () => {
      const req = http.get(url, (res) => { res.resume(); resolve(); });
      req.on("error", () => Date.now() < deadline ? setTimeout(tick, 150) : reject(new Error("server did not start")));
    };
    tick();
  });
}

(async () => {
  const port = 8890 + Math.floor(Math.random() * 100);
  const base = `http://127.0.0.1:${port}`;
  const route = "/writers/learn/writing-basics/what-is-writing/";
  const srv = spawn(process.execPath, [path.join(ROOT, "server/server.js")], {
    env: {...process.env, PORT: String(port)}, stdio: "ignore",
  });
  let browser, checks = 0;
  const failures = [];
  const check = (ok, label, detail = "") => {
    checks++;
    console.log(`${ok ? "PASS" : "FAIL"}  ${label}${detail ? " - " + detail : ""}`);
    if (!ok) failures.push(label);
  };
  const section = (t) => console.log(`\n${t}`);

  try {
    await ready(base + "/healthz");
    browser = await chromium.launch({headless: true});

    const open = async (timezone) => {
      const ctx = await browser.newContext({timezoneId: timezone, serviceWorkers: "block"});
      const log = {adsterra: [], monetag: []};
      await ctx.route(AD_HOST, (r) => { log.adsterra.push(r.request().url()); r.abort(); });
      await ctx.route(MONETAG_HOST, (r) => { log.monetag.push(r.request().url()); r.fulfill(EMPTY_JS); });
      await ctx.route(GOOGLE_HOST, (r) => r.fulfill(EMPTY_JS));
      return {ctx, page: await ctx.newPage(), log};
    };
    const visit = (h, r) => h.page.goto(base + r, {waitUntil: "networkidle"});
    const snap = (h) => h.page.evaluate(() => ({
      adsterraLoader: !!document.querySelector('script[src*="/assets/adsterra-loader.js"]'),
      monetagLoader: !!document.querySelector('script[src*="/assets/monetag-loader.js"]'),
      zones: [...document.querySelectorAll("script[data-zone]")].length,
    }));
    const grantArray = (h) => h.page.evaluate(() => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(["consent", "update", {ad_storage: "granted"}]);
    });
    const grantGtag = (h) => h.page.evaluate(() => window.gtag("consent", "update", {
      ad_storage: "granted", ad_user_data: "granted", ad_personalization: "granted", analytics_storage: "granted"}));
    const denyGtag = (h) => h.page.evaluate(() => window.gtag("consent", "update", {
      ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "denied"}));

    for (const [label, tz] of [["Lagos", "Africa/Lagos"], ["New York", "America/New_York"]]) {
      section(`${label} (${tz}) - no consent needed`);
      const h = await open(tz);
      await visit(h, route);
      await h.page.waitForTimeout(600);
      const s = await snap(h);
      check(h.log.adsterra.length >= EXPECTED_UNITS, `${label}: Adsterra loads`,
        `${h.log.adsterra.length} ad-host requests (expected >= ${EXPECTED_UNITS})`);
      const served = await (await h.page.request.get(base + route)).text();
      const rawTag = /<script\b[^>]*\bsrc=["']https:\/\/[^"']*invoke\.js/i.test(served);
      check(s.adsterraLoader && !rawTag, `${label}: Adsterra goes through its first-party loader`,
        `loader present ${s.adsterraLoader}, raw invoke.js tag in served HTML ${rawTag}`);
      check(!s.monetagLoader && s.zones === 0 && h.log.monetag.length === 0, `${label}: Monetag is completely absent`);
      await h.ctx.close();
    }

    for (const [label, tz] of [["Berlin (EEA)", "Europe/Berlin"], ["London (UK)", "Europe/London"], ["Zurich (CH)", "Europe/Zurich"]]) {
      section(`${label} (${tz}) - consent never given`);
      const h = await open(tz);
      await visit(h, route);
      await h.page.waitForTimeout(1500);
      const s = await snap(h);
      check(h.log.adsterra.length === 0, `${label}: no request reaches an Adsterra host`, `${h.log.adsterra.length} requests`);
      check(!s.monetagLoader && h.log.monetag.length === 0, `${label}: Monetag is completely absent`);
      await h.ctx.close();
    }

    section("Berlin - consent explicitly refused through gtag()");
    {
      const h = await open("Europe/Berlin");
      await visit(h, route);
      await denyGtag(h);
      await h.page.waitForTimeout(1500);
      check(h.log.adsterra.length === 0, "Berlin: a refusal keeps Adsterra off", `Adsterra ${h.log.adsterra.length}`);
      await h.ctx.close();
    }

    for (const [label, grant] of [["a consent update pushed as a plain array", grantArray], ["the real CMP call, gtag('consent','update')", grantGtag]]) {
      section(`Berlin - consent granted through ${label}`);
      const h = await open("Europe/Berlin");
      await visit(h, route);
      await h.page.waitForTimeout(400);
      const before = h.log.adsterra.length;
      await grant(h);
      await h.page.waitForTimeout(1500);
      check(before === 0, "Berlin: nothing loaded before the grant", `${before} requests`);
      check(h.log.adsterra.length >= EXPECTED_UNITS, "Berlin: consent releases every Adsterra unit",
        `${h.log.adsterra.length} ad-host requests (expected >= ${EXPECTED_UNITS})`);
      await h.ctx.close();
    }

    console.log(failures.length
      ? `\nFAILED (${failures.length} of ${checks}): ${failures.join("; ")}`
      : `\nAll ${checks} checks pass: Adsterra consent gate works as specified and Monetag is completely removed.`);
  } finally {
    if (browser) await browser.close();
    if (srv) srv.kill("SIGTERM");
  }
  process.exit(failures.length ? 1 : 0);
})();
