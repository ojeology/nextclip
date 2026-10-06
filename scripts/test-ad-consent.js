/* Behavioural test for the ad consent gates - Adsterra and Monetag.
 *
 * Claims about consent gating are worthless unless a browser proves them, so
 * this runs the real pages in a real Chromium with the clock set to different
 * parts of the world. Both networks ride the same rule, and each case asserts
 * both:
 *
 *   - outside the EEA, UK and Switzerland every configured unit loads at once
 *     (Lagos, New York) - non-European traffic is the owner's revenue;
 *   - inside them (Berlin = EEA, London = UK, Zurich = CH) NOTHING loads and no
 *     request may reach an ad host while consent is missing or refused;
 *   - a granted ad-consent signal releases every unit, whether it arrives as
 *     the plain array a test might push or as the call Google's CMP really
 *     makes - the page's own gtag(), which pushes an `arguments` object.
 *
 * Monetag (In-Page Push + Vignette, owner decision 2026-10-06) adds three more
 * guarantees, because the owner asked for the zones on EVERY eligible page load:
 *
 *   - six consecutive page loads in one browser profile each request both zone
 *     scripts. The retired loader capped Vignette at 4 loads per 4 hours and
 *     Push at 12 per 12 hours in localStorage, so a regression to any cap fails
 *     on the fifth load;
 *   - the loader itself never touches cookies or Web Storage (a hook records any
 *     such call whose stack runs through monetag-loader.js, and a positive
 *     control proves the hook can see one);
 *   - noindex and redirect stubs and the 404 page carry no Monetag markup.
 *
 * The ad hosts are never really fetched; the test only records that they were
 * asked for. Google's endpoints are stubbed too so the run is hermetic.
 *
 * Run: node scripts/test-ad-consent.js   (needs a built tree)
 *
 * Post-deploy check: LIVE_URL=https://thebryme.com node scripts/test-ad-consent.js
 * runs the very same assertions against a deployed site instead of starting the
 * local server. Ad hosts are still intercepted in the browser, so no real ad
 * request is made. It reads site.config.json from the checkout, so run it from
 * the commit that was deployed.
 */
const {chromium} = require("playwright");
const {spawn} = require("child_process");
const net = require("net");
const fs = require("fs");
const ROOT = __dirname + "/..";
const LIVE = String(process.env.LIVE_URL || "").replace(/\/+$/, "");
const CFG = (() => {
  try { return JSON.parse(fs.readFileSync(ROOT + "/site.config.json", "utf8")); } catch { return {}; }
})();
const AD_HOST = /profitableratecpmnetwork\.com|highrevenueformat\.com/i;
const GOOGLE_HOST = /googletagmanager\.com|google-analytics\.com|googlesyndication\.com|googleadservices\.com|doubleclick\.net|fundingchoicesmessages\.google\.com/i;
const EMPTY_JS = {status: 200, contentType: "application/javascript", body: "/* test stub */"};

// Expected Adsterra ad-host requests per page load = the number of configured,
// enabled units (each fires its loader request to its own host). Mirrors
// scripts/inject-ads.py: native placements with a key/host (bottom may fall
// back to the shared unit), plus the social bar script and the classic
// display banner once their units are pasted in.
const EXPECTED_UNITS = (() => {
  try {
    const ast = CFG.adsterra || {};
    if (ast.enabled === false) return 0;
    let units = 0;
    const pl = ast.placements || {};
    for (const name of ["top", "middle", "bottom"]) {
      const u = pl[name] || {};
      if (!u.enabled) continue;
      let key = String(u.key || "").trim(), host = String(u.host || "").trim();
      if (!key && name === "bottom") { key = String(ast.key || "").trim(); host = String(ast.host || "").trim(); }
      if (key && host) units++;
    }
    const soc = ast.socialBar || {};
    if (soc.enabled && String(soc.script || "").trim()) units++;
    const disp = ast.displayBanner || {};
    if (disp.enabled && String(disp.key || "").trim() && String(disp.host || "").trim()) units++;
    return units;
  } catch { return 1; }
})();

// Monetag zones exactly as scripts/inject-ads.py resolves them: monetag.enabled
// and the unit's own enabled, with a numeric zone and an https script URL.
const MONETAG_UNITS = (() => {
  const m = CFG.monetag || {};
  const out = [];
  if (!m.enabled) return out;
  for (const [key, unit] of [["inPagePush", "inpage-push"], ["vignette", "vignette"]]) {
    const u = m[key] || {};
    if (!u.enabled) continue;
    const zone = String(u.zone || "").trim(), src = String(u.script || "").trim();
    if (/^[0-9]{4,12}$/.test(zone) && /^https:\/\/[A-Za-z0-9.-]+\/[A-Za-z0-9._~%+/-]+$/.test(src)) out.push({unit, zone, src});
  }
  return out;
})();
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const MONETAG_HOST = new RegExp(MONETAG_UNITS.length
  ? [...new Set(MONETAG_UNITS.map((u) => esc(new URL(u.src).hostname)))].join("|") : "(?!)", "i");
const WANT = MONETAG_UNITS.map((u) => u.zone + "|" + u.src).sort();

function freePort() {
  return new Promise((res) => {
    const s = net.createServer();
    s.listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => res(p)); });
  });
}
async function ready(url, tries = 60) {
  for (let i = 0; i < tries; i++) {
    try { const r = await fetch(url); if (r.ok) return true; } catch {}
    await new Promise((r) => setTimeout(r, 250));
  }
  throw new Error("server never came up");
}

(async () => {
  let srv, base = LIVE;
  if (!LIVE) {
    const port = await freePort();
    base = `http://127.0.0.1:${port}`;
    srv = spawn(process.execPath, ["server/server.js"], {
      cwd: ROOT, env: {...process.env, PORT: String(port), HOST: "127.0.0.1"}, stdio: "ignore",
    });
  } else {
    console.log(`Running against the deployed site: ${LIVE}`);
  }
  const route = "/sports/title-ix-explained/";
  let browser, failures = [], checks = 0;
  const check = (ok, label, detail) => {
    checks++;
    console.log(`${ok ? "PASS" : "FAIL"}  ${label}${detail ? " - " + detail : ""}`);
    if (!ok) failures.push(label);
  };
  const section = (t) => console.log(`\n${t}`);

  try {
    await ready(base + (LIVE ? "/" : "/healthz"));
    browser = await chromium.launch({headless: true});

    // A fresh browser profile with the clock in `timezone`. Everything an ad
    // host is asked for is recorded; nothing is fetched from the network.
    const open = async (timezone) => {
      const ctx = await browser.newContext({timezoneId: timezone, serviceWorkers: "block"});
      const log = {adsterra: [], monetag: []};
      await ctx.route(AD_HOST, (r) => { log.adsterra.push(r.request().url()); r.abort(); });
      await ctx.route(MONETAG_HOST, (r) => { log.monetag.push(r.request().url()); r.fulfill(EMPTY_JS); });
      await ctx.route(GOOGLE_HOST, (r) => r.fulfill(EMPTY_JS));
      // Record any cookie or Web Storage call whose stack runs through the
      // Monetag loader. Installed before any page script, in every document.
      await ctx.addInitScript(() => {
        window.__mtTouch = [];
        const rec = (kind) => { if (/monetag-loader/.test(new Error().stack || "")) window.__mtTouch.push(kind); };
        for (const m of ["getItem", "setItem", "removeItem", "clear", "key"]) {
          const orig = Storage.prototype[m];
          Storage.prototype[m] = function () { rec("storage." + m); return orig.apply(this, arguments); };
        }
        const d = Object.getOwnPropertyDescriptor(Document.prototype, "cookie");
        Object.defineProperty(document, "cookie", {
          configurable: true,
          get() { rec("cookie.get"); return d.get.call(document); },
          set(v) { rec("cookie.set"); d.set.call(document, v); },
        });
      });
      return {ctx, page: await ctx.newPage(), log};
    };
    const visit = (h, r) => h.page.goto(base + r, {waitUntil: "networkidle"});
    const snap = (h) => h.page.evaluate(() => ({
      adsterraLoader: !!document.querySelector('script[src*="/assets/adsterra-loader.js"]'),
      monetagLoader: !!document.querySelector('script[src*="/assets/monetag-loader.js"]'),
      zones: [...document.querySelectorAll("script[data-zone]")].map((s) => s.getAttribute("data-zone") + "|" + s.getAttribute("src")).sort(),
      touches: window.__mtTouch || [],
      capKeys: Object.keys(localStorage).filter((k) => /^bryme-mt/.test(k)),
    }));
    // exactly the configured zones, once each, and the request really went out
    const monetagLoaded = (s, h) => JSON.stringify(s.zones) === JSON.stringify(WANT) &&
      MONETAG_UNITS.every((u) => h.log.monetag.includes(u.src));
    const monetagSilent = (s, h) => s.zones.length === 0 && h.log.monetag.length === 0;
    const grantArray = (h) => h.page.evaluate(() => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(["consent", "update", {ad_storage: "granted"}]);
    });
    // what Google's CMP actually does: call the page's own gtag()
    const grantGtag = (h) => h.page.evaluate(() => window.gtag("consent", "update", {
      ad_storage: "granted", ad_user_data: "granted", ad_personalization: "granted", analytics_storage: "granted"}));
    const denyGtag = (h) => h.page.evaluate(() => window.gtag("consent", "update", {
      ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "denied"}));

    // ---- outside Europe: everything loads immediately --------------------
    for (const [label, tz] of [["Lagos", "Africa/Lagos"], ["New York", "America/New_York"]]) {
      section(`${label} (${tz}) - no consent needed`);
      const h = await open(tz);
      await visit(h, route);
      await h.page.waitForTimeout(600);
      const s = await snap(h);
      check(h.log.adsterra.length >= EXPECTED_UNITS, `${label}: Adsterra loads`,
        `${h.log.adsterra.length} ad-host requests (expected >= ${EXPECTED_UNITS})`);
      // The tag the LOADER appends is expected here; what must never exist is a
      // raw, ungated invoke.js tag in the HTML the server sends.
      const served = await (await h.page.request.get(base + route)).text();
      const rawTag = /<script\b[^>]*\bsrc=["']https:\/\/[^"']*invoke\.js/i.test(served);
      check(s.adsterraLoader && !rawTag, `${label}: Adsterra goes through its first-party loader`,
        `loader present ${s.adsterraLoader}, raw invoke.js tag in served HTML ${rawTag}`);
      check(s.monetagLoader, `${label}: page carries the first-party Monetag loader`);
      check(monetagLoaded(s, h), `${label}: every Monetag zone loads`,
        `zones on page [${s.zones.join(", ")}], requests ${h.log.monetag.length}`);
      await h.ctx.close();
    }

    // ---- inside Europe: nothing loads without consent --------------------
    for (const [label, tz] of [["Berlin (EEA)", "Europe/Berlin"], ["London (UK)", "Europe/London"], ["Zurich (CH)", "Europe/Zurich"]]) {
      section(`${label} (${tz}) - consent never given`);
      const h = await open(tz);
      await visit(h, route);
      await h.page.waitForTimeout(2500);
      const s = await snap(h);
      check(h.log.adsterra.length === 0, `${label}: no request reaches an Adsterra host`, `${h.log.adsterra.length} requests`);
      check(s.monetagLoader && monetagSilent(s, h), `${label}: no request reaches Monetag and no zone script is added`,
        `${h.log.monetag.length} requests, ${s.zones.length} zone scripts, loader present ${s.monetagLoader}`);
      await h.ctx.close();
    }

    section("Berlin - consent explicitly refused through gtag()");
    {
      const h = await open("Europe/Berlin");
      await visit(h, route);
      await denyGtag(h);
      await h.page.waitForTimeout(2500);
      const s = await snap(h);
      check(h.log.adsterra.length === 0 && monetagSilent(s, h), "Berlin: a refusal keeps both networks off",
        `Adsterra ${h.log.adsterra.length}, Monetag ${h.log.monetag.length}`);
      await h.ctx.close();
    }

    for (const [label, grant] of [["a consent update pushed as a plain array", grantArray], ["the real CMP call, gtag('consent','update')", grantGtag]]) {
      section(`Berlin - consent granted through ${label}`);
      const h = await open("Europe/Berlin");
      await visit(h, route);
      await h.page.waitForTimeout(400);
      const before = h.log.adsterra.length + h.log.monetag.length;
      await grant(h);
      await h.page.waitForTimeout(1500);
      const s = await snap(h);
      check(before === 0, "Berlin: nothing loaded before the grant", `${before} requests`);
      check(h.log.adsterra.length >= EXPECTED_UNITS, "Berlin: consent releases every Adsterra unit",
        `${h.log.adsterra.length} ad-host requests (expected >= ${EXPECTED_UNITS})`);
      check(monetagLoaded(s, h), "Berlin: consent releases every Monetag zone",
        `zones on page [${s.zones.join(", ")}], requests ${h.log.monetag.length}`);
      check(s.touches.length === 0, "Berlin: the Monetag loader touched no cookie or storage", `${s.touches.length} touches`);
      await h.ctx.close();
    }

    // ---- no local frequency cap: every page load, one browser profile ----
    section("Lagos - six page loads in ONE browser profile (no local frequency cap)");
    {
      const h = await open("Africa/Lagos");
      const routes = [route, "/writers/", "/tech/", "/home/", "/fitness/", "/sports/"];
      const bad = [];
      let touches = 0, capKeys = [];
      for (const r of routes) {
        h.log.monetag.length = 0;
        await visit(h, r);
        await h.page.waitForTimeout(500);
        const s = await snap(h);
        touches += s.touches.length;
        capKeys = s.capKeys;
        if (!(s.monetagLoader && monetagLoaded(s, h))) bad.push(r);
      }
      check(bad.length === 0, "every one of six consecutive page loads requests every Monetag zone",
        bad.length ? `missing on ${bad.join(", ")}` : `${routes.length}/${routes.length} loads, ${MONETAG_UNITS.length} zones each`);
      check(touches === 0 && capKeys.length === 0, "the loader wrote no cookie, storage entry or frequency-cap key",
        `${touches} touches, cap keys [${capKeys.join(", ")}]`);
      await h.ctx.close();
    }

    section("Instrument self-check - a loader-origin storage call must be visible to the hook");
    {
      const h = await open("Africa/Lagos");
      await h.ctx.route("**/__control/monetag-loader.js", (r) => r.fulfill({status: 200, contentType: "application/javascript",
        body: "try{localStorage.setItem('probe','1');document.cookie='probe=1'}catch(e){}"}));
      await visit(h, route);
      await h.page.evaluate(() => new Promise((res) => {
        const s = document.createElement("script"); s.src = "/__control/monetag-loader.js";
        s.onload = s.onerror = res; document.head.appendChild(s);
      }));
      const seen = await h.page.evaluate(() => window.__mtTouch.length);
      check(seen >= 2, "the hook records a storage write and a cookie write made from a monetag-loader script", `${seen} recorded`);
      await h.ctx.close();
    }

    // ---- pages that must NOT carry Monetag -------------------------------
    section("Stub and error pages carry no Monetag markup");
    {
      const h = await open("Africa/Lagos");
      for (const [r, what] of [["/writing/", "noindex redirect stub"], ["/not-a-page/", "404 page"]]) {
        const res = await h.page.request.get(base + r);
        const text = await res.text();
        check(!/data-adband="monetag"|monetag-loader/i.test(text), `${r} (${what}): no Monetag markers or loader`, `HTTP ${res.status()}`);
      }
      await h.ctx.close();
    }

    console.log(failures.length
      ? `\nFAILED (${failures.length} of ${checks}): ${failures.join("; ")}`
      : `\nAll ${checks} checks pass: both consent gates behave as specified, and Monetag loads on every eligible page view.`);
  } finally {
    if (browser) await browser.close();
    if (srv) srv.kill("SIGTERM");
  }
  process.exit(failures.length ? 1 : 0);
})();
