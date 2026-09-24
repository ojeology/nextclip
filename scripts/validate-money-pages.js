#!/usr/bin/env node
/* Static release gate for the researched Money publication. No network needed. */
"use strict";
const fs = require("node:fs"), path = require("node:path"), assert = require("node:assert/strict");
const ROOT = path.resolve(__dirname, "..");
const read = p => fs.readFileSync(path.join(ROOT, p), "utf8");
const manifest = JSON.parse(read("content/money-guides/manifest.json"));
const allow = JSON.parse(read("content/index-allowlist.routed.json")).routes;
const publicPrefix = "/money/";
const routes = manifest.articles.map(g => publicPrefix + g.slug + "/");
const origin = JSON.parse(read("site.config.json")).siteUrl.replace(/\/$/, "");
const reasons = [];
const check = (okay, text) => {if (!okay) reasons.push(text)};
const sourceCode = read("scripts/money_evergreen_data.py");
check(manifest.articles.length >= 10, "evergreen library unexpectedly small");
check(new Set(routes).size === routes.length, "duplicate guide slugs");
check(sourceCode.includes("MONEY_NAV"), "Money navigation source missing");
const descriptions = new Set(), titles = new Set();
const escapeText = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\"/g, "&quot;").replace(/'/g, "&#x27;");
const unescapeText = s => s.replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#x27;|&#39;/g, "'");
for (const [i, g] of manifest.articles.entries()) {
  const route = routes[i], name = `money/${g.slug}/index.html`;
  const fragment = read(`content/money-guides/${g.slug}.html`);
  const rootFile = path.join(ROOT, name), publicFile = path.join(ROOT, "public", name);
  check(fs.existsSync(rootFile) && fs.existsSync(publicFile), `${route}: missing routed or published page`);
  if (!fs.existsSync(rootFile) || !fs.existsSync(publicFile)) continue;
  const html = read(name), pub = read(`public/${name}`), eco = read(`ecosystem/${name}`);
  check(html === pub, `${route}: public mirror differs from routed page`);
  check(eco.includes(escapeText(g.h1)), `${route}: ecosystem source page differs from manifest`);
  check(html.includes(`href="${origin}${route}"`), `${route}: missing exact canonical`);
  check(html.includes('name="robots" content="index,follow"'), `${route}: noindex or missing robots`);
  check(html.includes(`content="${g.description}"`), `${route}: description mismatch`);
  check((html.match(/<h1\b/g) || []).length === 1 && html.includes(escapeText(g.h1)), `${route}: wrong H1`);
  check(html.includes('id="main"') && html.includes('href="#main"'), `${route}: accessibility landmarks absent`);
  check(html.includes("General information, not financial advice"), `${route}: missing financial disclaimer`);
  check(html.includes(`Sources reviewed ${manifest.reviewed}`), `${route}: visible review stamp absent`);
  check(html.includes("Sources and further reading"), `${route}: no source section`);
  check(fragment.split(/\s+/).length >= 350, `${route}: text below substantial guide floor`);
  check(!/<\s*(script|iframe|h1|main)\b/i.test(fragment), `${route}: source contains shell/script element`);
  check(!/\b(?:guaranteed profit|risk[- ]free income|best broker to trade with)\b/i.test(fragment), `${route}: misleading return/endorsement claim`);
  check(g.sources.every(s => s.url.startsWith("https://") && html.includes(`href="${s.url}"`)), `${route}: unlinked official sources`);
  check(!descriptions.has(g.description), `${route}: duplicate description`); descriptions.add(g.description);
  const titleMatch = html.match(/<title>([^<]+)<\/title>/);
  const visibleTitle = titleMatch ? unescapeText(titleMatch[1]) : "";
  check(titleMatch && visibleTitle.length <= 60 && !titles.has(visibleTitle), `${route}: title too long or duplicate`);
  if (titleMatch) titles.add(visibleTitle);
  const ld = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)].map(m => {try{return JSON.parse(m[1])}catch{return null}});
  check(ld.length > 0 && ld.every(Boolean), `${route}: invalid or absent JSON-LD`);
  const pages = ld.flatMap(v => v && (v["@graph"] || [v]));
  check(pages.some(v => v["@type"] === "WebPage" && v.url === `${origin}${route}` && v.dateModified === manifest.reviewed), `${route}: schema URL/date not the page and reviewed date`);
  for (const m of html.matchAll(/href="(\/money\/[^"#?]*)(?:["#?])/g)) {
    const dest = m[1];
    check(fs.existsSync(path.join(ROOT, dest.slice(1), "index.html")), `${route}: broken local link ${dest}`);
  }
  for (const rel of g.related) check(html.includes(`/money/${rel}/`), `${route}: related link ${rel} missing`);
  for (const m of fragment.matchAll(/<h2 id="([a-z0-9-]+)">/g)) {
    check(html.includes(`href="#${m[1]}"`), `${route}: TOC anchor #${m[1]} missing`);
  }
}
const siteMoney = read("money/sitemap.xml");
const sitemapLocs = [...siteMoney.matchAll(/<loc>(.*?)<\/loc>/g)].map(m => m[1]);
check(sitemapLocs.length === 15 + routes.length, `Money sitemap should contain 15 original + ${routes.length} guides, has ${sitemapLocs.length}`);
for (const route of routes) {
  check(allow.includes(route), `${route}: missing routed allowlist entry`);
  check(sitemapLocs.includes(origin + route), `${route}: missing Money sitemap entry`);
  check(read("money/index.html").includes(`href="${route}"`), `${route}: not linked from Money hub`);
}
check(read("money/sitemap.xml") === read("public/money/sitemap.xml"), "Money sitemap not staged");
check(read("sitemap.xml") === read("public/sitemap.xml"), "root sitemap index not staged");
check(read("public/assets/money-position-size.js") === read("assets/money-position-size.js"), "position-size calculator source/publish mismatch");
for (const prop of ["sports", "tech", "entertainment", "fitness", "home", "money"]) {
  check(fs.existsSync(path.join(ROOT, "public", prop, "favicon.ico")), `${prop}: published favicon missing`);
}
if (reasons.length) {
  console.error(`FAIL Money release gate (${reasons.length}):\n  - ${reasons.slice(0, 60).join("\n  - ")}`);
  process.exit(1);
}
console.log(JSON.stringify({ok:true, newGuides:routes.length, moneySitemapUrls:sitemapLocs.length, reviewDate:manifest.reviewed, copiedPathsChecked:routes.length, markets:["US","UK","CA","AU"]}, null, 2));
