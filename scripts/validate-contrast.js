#!/usr/bin/env node
"use strict";
/**
 * BRYME contrast + navigation-motion gate.
 *
 * Added after a regression shipped in which the shared section nav painted a
 * near-black animated gradient underneath near-black link text: the contrast
 * ratio oscillated down to 1.02:1 and the navigation became unreadable as it
 * moved. Nothing in the release gates caught it, so this file exists to make
 * that class of bug fail the build.
 *
 * It asserts, in a real browser, across mobile/tablet/desktop:
 *   1. Every measured text/background pair meets WCAG AA (4.5:1 normal,
 *      3:1 large), with translucent layers correctly alpha-composited.
 *   2. Navigation does not animate or auto-scroll on its own.
 *   3. The country filter is a static selection control, not a moving bar.
 *   4. A home link is present in the header of every page.
 *
 * Usage: node scripts/validate-contrast.js
 */
const net = require("net");
const path = require("path");
const { spawn } = require("child_process");
const { chromium } = require("playwright");

const ROOT = path.resolve(__dirname, "..");
const failures = [];
const check = (ok, msg) => { if (!ok) failures.push(msg); };

const ROUTES = [
  "/", "/writing/", "/learn/", "/tools/", "/glossary/", "/templates/",
  "/checklists/", "/problems/", "/search/", "/guides/", "/tested/", "/about/",
  "/writing/the-republic/", "/guides/how-to-write-a-pitch/",
  "/learn/writing-basics/sentence-basics/", "/tools/word-counter/",
];

const VIEWPORTS = [
  { name: "mobile", width: 390, height: 844 },
  { name: "tablet", width: 768, height: 1024 },
  { name: "desktop", width: 1440, height: 1000 },
];

/* ---- colour maths (WCAG 2.1) ---- */
const parse = (c) => {
  const m = String(c).match(/[\d.]+/g);
  if (!m) return null;
  return { r: +m[0], g: +m[1], b: +m[2], a: m.length > 3 ? +m[3] : 1 };
};
const over = (fg, bg) => ({
  r: fg.r * fg.a + bg.r * (1 - fg.a),
  g: fg.g * fg.a + bg.g * (1 - fg.a),
  b: fg.b * fg.a + bg.b * (1 - fg.a),
  a: 1,
});
const lum = (c) => {
  const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
  return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
};
const ratio = (a, b) => {
  const la = lum(a), lb = lum(b);
  return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
};

function freePort() {
  return new Promise((resolve, reject) => {
    const s = net.createServer();
    s.listen(0, "127.0.0.1", () => { const p = s.address().port; s.close(() => resolve(p)); });
    s.on("error", reject);
  });
}
async function ready(url) {
  for (let i = 0; i < 80; i++) {
    try { if ((await fetch(url)).ok) return; } catch {}
    await new Promise((r) => setTimeout(r, 100));
  }
  throw new Error("server did not start");
}

(async () => {
  const port = await freePort();
  const base = `http://127.0.0.1:${port}`;
  const child = spawn(process.execPath, ["server/server.js"], {
    cwd: ROOT, env: { ...process.env, PORT: String(port), HOST: "127.0.0.1" }, stdio: "ignore",
  });
  let browser;
  let measured = 0;

  try {
    await ready(base + "/healthz");
    browser = await chromium.launch({ headless: true });

    for (const vp of VIEWPORTS) {
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height }, serviceWorkers: "block",
      });
      const page = await context.newPage();

      for (const route of ROUTES) {
        const label = `${vp.name} ${route}`;
        await page.goto(base + route, { waitUntil: "networkidle", timeout: 20000 });

        /* ---------- 1. contrast ---------- */
        const samples = await page.evaluate(() => {
          function layers(el) {
            if (getComputedStyle(el).backgroundImage !== "none") return null;
            const out = [];
            let n = el;
            while (n) {
              const cs = getComputedStyle(n);
              out.push(cs.backgroundColor);
              const m = cs.backgroundColor.match(/[\d.]+/g);
              const a = m && m.length > 3 ? parseFloat(m[3]) : 1;
              if (a >= 1) break;
              n = n.parentElement;
            }
            return out;
          }
          const SELECTORS = [
            ['.section-nav a:not([aria-current])', 'section-nav link'],
            ['.section-nav a[aria-current="page"]', 'section-nav active'],
            ['.breadcrumb', 'breadcrumb text'],
            ['.breadcrumb a', 'breadcrumb link'],
            ['#country-select', 'country select'],
            ['.country-filter-label', 'filter label'],
            ['.country-filter-hint', 'filter hint'],
            ['.country-reset', 'reset button'],
            ['#filter-note', 'filter status'],
            ['.home-link', 'home icon'],
            ['.main-nav a[aria-current="page"]', 'header nav active'],
            ['.main-nav a:not(.nav-cta):not([aria-current])', 'header nav link'],
            ['.nav-cta', 'header CTA'],
            ['.job-card-title a', 'card title'],
            ['.job-card-sub', 'card subtitle'],
            ['.verify-badge.country', 'country badge'],
            ['.bottom-nav a', 'bottom nav'],
            ['.foot-col a', 'footer link'],
            ['.prose p', 'body text'],
            ['.hero-copy', 'hero copy'],
          ];
          const out = [];
          for (const [sel, name] of SELECTORS) {
            const el = document.querySelector(sel);
            if (!el || !el.getClientRects().length) continue;
            const cs = getComputedStyle(el);
            const L = layers(el);
            if (!L) continue;
            const size = parseFloat(cs.fontSize);
            const bold = parseInt(cs.fontWeight, 10) >= 700;
            out.push({ name, color: cs.color, layers: L, large: size >= 24 || (size >= 18.66 && bold) });
          }
          return out;
        });

        for (const s of samples) {
          let bg = { r: 255, g: 255, b: 255, a: 1 };
          for (let i = s.layers.length - 1; i >= 0; i--) {
            const p = parse(s.layers[i]);
            if (p) bg = over(p, bg);
          }
          const fg = parse(s.color);
          if (!fg) continue;
          const cr = ratio(fg, bg);
          const need = s.large ? 3 : 4.5;
          measured++;
          check(cr >= need, `${label}: ${s.name} contrast ${cr.toFixed(2)}:1 (needs ${need}:1)`);
        }

        /* ---------- 2. navigation must not move on its own ---------- */
        const motion = await page.evaluate(() => {
          const navs = [...document.querySelectorAll(".section-nav, .country-filter")];
          return navs.map((n) => {
            const cs = getComputedStyle(n);
            return {
              cls: n.className,
              animation: cs.animationName,
              bgImage: cs.backgroundImage !== "none",
              scrollLeft: n.scrollLeft,
            };
          });
        });
        for (const m of motion) {
          check(m.animation === "none", `${label}: "${m.cls}" has CSS animation "${m.animation}"`);
          check(!m.bgImage, `${label}: "${m.cls}" uses a gradient/image background behind text`);
        }
        if (motion.length) {
          await page.waitForTimeout(1500);
          const after = await page.evaluate(() =>
            [...document.querySelectorAll(".section-nav, .country-filter")].map((n) => n.scrollLeft));
          after.forEach((v, i) => {
            check(v === motion[i].scrollLeft,
              `${label}: "${motion[i].cls}" auto-scrolled (${motion[i].scrollLeft} -> ${v})`);
          });
        }

        /* ---------- 3. home link in the header ---------- */
        const home = await page.evaluate(() => {
          const a = document.querySelector("header .home-link");
          if (!a) return null;
          const r = a.getBoundingClientRect();
          return { href: new URL(a.href).pathname, w: r.width, h: r.height,
                   label: a.getAttribute("aria-label"), svg: !!a.querySelector("svg") };
        });
        check(home !== null, `${label}: no home link in header`);
        if (home) {
          check(home.href === "/", `${label}: home link points to ${home.href}`);
          check(home.svg, `${label}: home link has no icon`);
          check(home.label && home.label.trim().length > 0, `${label}: home link has no accessible name`);
          check(home.w >= 24 && home.h >= 24, `${label}: home tap target ${Math.round(home.w)}x${Math.round(home.h)} < 24px`);
        }

        /* ---------- 4. the country filter is a real selection control ---------- */
        if (route === "/writing/") {
          const f = await page.evaluate(() => {
            const s = document.getElementById("country-select");
            if (!s) return null;
            return {
              tag: s.tagName,
              options: [...s.querySelectorAll("option")].map((o) => o.value),
              groups: [...s.querySelectorAll("optgroup")].map((g) => g.label),
              insideMovingBar: !!s.closest(".section-nav"),
            };
          });
          check(f !== null, `${label}: country filter control missing`);
          if (f) {
            check(f.tag === "SELECT", `${label}: country filter is <${f.tag}>, not a selection control`);
            check(!f.insideMovingBar, `${label}: country filter sits inside a scrolling nav bar`);
            check(f.options.includes("all"), `${label}: no "All countries" reset option`);
            check(f.options.includes("international"), `${label}: no worldwide/no-restriction option`);
            check(f.groups.length >= 3, `${label}: filter not grouped by region (${f.groups.length} groups)`);
          }
        }
      }
      await context.close();
    }

    console.log(JSON.stringify({
      ok: failures.length === 0,
      routes: ROUTES.length,
      viewports: VIEWPORTS.map((v) => `${v.width}x${v.height}`),
      contrastPairsMeasured: measured,
      standard: "WCAG 2.1 AA (4.5:1 normal, 3:1 large)",
      failures: failures.slice(0, 100),
    }, null, 2));
    if (failures.length) process.exitCode = 1;
  } catch (e) {
    console.error(e.stack || e);
    process.exitCode = 1;
  } finally {
    if (browser) await browser.close();
    child.kill("SIGTERM");
  }
})();
