/* Behavioural test for the Adsterra consent gate.
 *
 * Claims about consent gating are worthless unless a browser proves them, so
 * this runs the real page in a real Chromium three times:
 *
 *   1. Lagos timezone  -> the banner script must load. Non-European traffic is
 *      unchanged, which is the owner's revenue.
 *   2. Berlin timezone, consent never granted -> the banner script must NOT
 *      load, and no request may reach the ad host at all.
 *   3. Berlin timezone, consent granted through the CMP's own signal
 *      (a dataLayer consent update, exactly what Google's CMP sends) -> the
 *      banner script must load.
 *
 * Run: node scripts/test-ad-consent.js   (needs a built tree)
 */
const {chromium} = require("playwright");
const {spawn} = require("child_process");
const net = require("net");
const fs = require("fs");
const ROOT = __dirname + "/..";
const AD_HOST = /profitableratecpmnetwork\.com|highrevenueformat\.com/i;

// Expected ad-host requests per page load = the number of configured, enabled
// Adsterra units (each fires its loader request to its own host). Mirrors
// scripts/inject-ads.py: native placements with a key/host (bottom may fall
// back to the shared unit), plus the social bar script and the classic
// display banner once their units are pasted in.
const EXPECTED_UNITS = (() => {
  try {
    const ast = (JSON.parse(fs.readFileSync(ROOT + "/site.config.json", "utf8")).adsterra) || {};
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
  const port = await freePort();
  const base = `http://127.0.0.1:${port}`;
  const srv = spawn(process.execPath, ["server/server.js"], {
    cwd: ROOT, env: {...process.env, PORT: String(port), HOST: "127.0.0.1"}, stdio: "ignore",
  });
  const route = "/sports/title-ix-explained/";
  let browser, failures = [];
  try {
    await ready(base + "/healthz");
    browser = await chromium.launch({headless: true});

    const run = async (label, timezone, grant) => {
      const ctx = await browser.newContext({timezoneId: timezone, serviceWorkers: "block"});
      // the ad host is never really fetched; we only record that it was asked for
      const asked = [];
      await ctx.route(AD_HOST, (r) => { asked.push(r.request().url()); r.abort(); });
      const page = await ctx.newPage();
      const loaded = [];
      page.on("request", (r) => { if (AD_HOST.test(r.url())) loaded.push(r.url()); });
      await page.goto(base + route, {waitUntil: "networkidle"});
      if (grant) {
        // exactly the signal Google's CMP sends when a visitor accepts
        await page.evaluate(() => {
          window.dataLayer = window.dataLayer || [];
          window.dataLayer.push(["consent", "update", {ad_storage: "granted"}]);
        });
        await page.waitForTimeout(1500);
      } else {
        await page.waitForTimeout(2500);
      }
      const loaderTag = await page.evaluate(() =>
        !!document.querySelector('script[src*="/assets/adsterra-loader.js"]'));
      const remoteTag = await page.evaluate(() =>
        [...document.querySelectorAll("script[src]")].some((s) => /invoke\.js/.test(s.src)));
      await ctx.close();
      return {label, timezone, grant, asked: asked.length, loaderTag, remoteTag};
    };

    const cases = [
      await run("Lagos, no consent needed", "Africa/Lagos", false),
      await run("Berlin, consent never given", "Europe/Berlin", false),
      await run("Berlin, consent granted", "Europe/Berlin", true),
    ];

    const expect = [
      {label: "Lagos, no consent needed", adHostHits: EXPECTED_UNITS, min: true, why: "non-European traffic is unchanged"},
      {label: "Berlin, consent never given", adHostHits: 0, min: false, why: "no request may reach the ad host"},
      {label: "Berlin, consent granted", adHostHits: EXPECTED_UNITS, min: true, why: "consent releases every configured unit"},
    ];
    for (let i = 0; i < cases.length; i++) {
      const c = cases[i], e = expect[i];
      // The no-consent case is exact (0 means 0). The loading cases accept
      // additional same-host fetches a unit may make once running, but every
      // configured unit must have fired at least its loader request.
      const pass = e.min ? c.asked >= e.adHostHits : c.asked === e.adHostHits;
      console.log(`${pass ? "PASS" : "FAIL"}  ${c.label}: ad-host requests ${c.asked} ` +
                  `(expected ${e.min ? ">= " : ""}${e.adHostHits}) - ${e.why}`);
      console.log(`      local loader present: ${c.loaderTag}, inline remote tag: ${c.remoteTag}`);
      if (!pass) failures.push(c.label);
    }
    console.log(failures.length ? `\nFAILED: ${failures.join(", ")}` : "\nAll three cases behave as specified.");
  } finally {
    if (browser) await browser.close();
    srv.kill("SIGTERM");
  }
  process.exit(failures.length ? 1 : 0);
})();
