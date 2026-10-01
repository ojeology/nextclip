#!/usr/bin/env node
/* Static release gate for the RETIRED Money desk (owner decision 2026-10-01,
   AdSense review). No network needed.

   Formerly this gate asserted the researched Money publication shipped: hub +
   guides present in every tier, routed allowlist membership, index,follow,
   sitemap parity. The desk is now unpublished, so the polarity is inverted -
   every assertion below fails the build if Money content can still reach
   production, while the archive (content/money-guides, the generator scripts)
   must stay intact in-repo for history and possible future relaunch.

   Retirement mechanics: files are simply absent from the artifact, so
   /money/* answers 404 by absence on Render (true 410 is impossible on a
   Render static site; same shape as the retired /movie/ family). The local
   server keeps parity: "money" is in MEDIA_FAMILIES and no 410.html is
   published, so it 404s too. The browser-level probes live in
   validate-money-browser.js. */
"use strict";
const fs = require("node:fs"), path = require("node:path");
const ROOT = path.resolve(__dirname, "..");
const read = p => fs.readFileSync(path.join(ROOT, p), "utf8");
const exists = p => fs.existsSync(path.join(ROOT, p));
const reasons = [];
const check = (okay, text) => {if (!okay) reasons.push(text)};

/* 1. The desk trees are gone from every tier. */
for (const tree of ["money", "ecosystem/money", "public/money"])
  check(!exists(tree), `retired Money tree still present: ${tree}/`);

/* 2. No Money routes in either allowlist artifact. */
for (const f of ["content/index-allowlist.json", "content/index-allowlist.routed.json"]) {
  const routes = JSON.parse(read(f)).routes;
  const money = routes.filter(r => r.startsWith("/money/"));
  check(money.length === 0, `${f}: ${money.length} /money/ routes still allowlisted`);
}

/* 3. Discovery surfaces are clean: robots, root sitemap index, desk sitemaps. */
const robots = read("public/robots.txt");
check(!/\/money\//.test(robots), "public/robots.txt still references /money/");
check(!/sitemap-catalogue/.test(robots), "public/robots.txt still registers the delisted catalogue sitemap");
const rootSitemap = read("public/sitemap.xml");
check(!/money/.test(rootSitemap), "public/sitemap.xml still lists a money sitemap");
check(!/sitemap-catalogue/.test(rootSitemap), "public/sitemap.xml still lists the delisted catalogue sitemap");
check(!exists("public/money/sitemap.xml"), "public/money/sitemap.xml still present");
const catalogue = read("public/entertainment/sitemap-catalogue.xml");
check(!/<loc>/.test(catalogue), "public/entertainment/sitemap-catalogue.xml still submits card URLs");

/* 4. No published page links to the retired desk (walk the deployed artifact). */
let linked = [];
(function walk(dir) {
  for (const e of fs.readdirSync(dir, {withFileTypes: true})) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith(".html")) {
      const html = read(path.relative(ROOT, p));
      if (html.includes('href="/money/') || html.includes("thebryme.com/money/")) linked.push(path.relative(ROOT, p));
    }
    else if (false)
      linked.push(path.relative(ROOT, p));
  }
})(path.join(ROOT, "public"));
check(linked.length === 0, `published pages still link to /money/: ${linked.slice(0, 5).join(", ")}${linked.length > 5 ? " …" : ""}`);

/* 5. Deploy config carries no Money redirects, and the local server keeps
      404 parity with production (family listed, no 410.html published). */
/* Only live rules count - both files carry dated comments explaining the
   retirement itself, and those legitimately mention /money/. */
const activeLines = f => read(f).split("\n").filter(l => l.trim() && !l.trim().startsWith("#"));
check(!activeLines("render.yaml").some(l => l.includes("/money/")), "render.yaml still carries /money/ redirect rules");
check(!activeLines("_redirects").some(l => l.includes("/money/")), "_redirects still carries /money/ redirect rules");
const server = read("server/server.js");
check(/"money"/.test(server.match(/MEDIA_FAMILIES=new Set\(\[[^\]]*\]\)/)[0]),
  'server.js MEDIA_FAMILIES lost "money" - local 404 parity with prod would silently depend on the generic handler');
check(!exists("public/410.html"), "public/410.html must stay unpublished (test/prod parity doctrine: prod 404s by absence)");

/* 6. The build chain must not regenerate the desk, and the archive must
      survive (never destroy existing work; relaunch stays possible). */
const pkg = JSON.parse(read("package.json"));
check(!/build-money-desk|money_evergreen/.test(pkg.scripts.build), "npm run build still invokes a Money generator");
for (const f of ["content/money-guides/manifest.json", "scripts/build-money-desk.py", "scripts/money_evergreen_data.py"])
  check(exists(f), `Money archive artifact missing: ${f} (retirement must not destroy the regeneration path)`);
const manifest = JSON.parse(read("content/money-guides/manifest.json"));
check(Array.isArray(manifest.articles) && manifest.articles.length >= 10,
  "Money archive manifest unexpectedly small - archive damaged?");

if (reasons.length) {
  console.error(`money-retirement gate: ${reasons.length} failure(s)`);
  for (const r of reasons) console.error("  ✗ " + r);
  process.exit(1);
}
console.log(`money-retirement gate: green - desk trees absent from all tiers, allowlists/robots/sitemaps clean, `
  + `0 published /money/ links, deploy rules purged, 404-by-absence parity intact, archive preserved (${manifest.articles.length} guides)`);
