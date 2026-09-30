#!/usr/bin/env node
/* Re-ask the "not-stated" market records through a real browser.

   WHY THIS EXISTS
   ---------------
   Main's commit c61f1ff46cf found that 15 records were publishing `not-stated`
   for a page nobody had ever read: a blocked fetch was being rendered as a
   finding of silence. When those pages were re-asked through a real Chromium,
   six opened and THREE of the six contained a real policy.

   This branch made the same class of claim. Batch 13's simultaneous-submission
   backfill classified 20 branch-only records as `not-stated` from plain HTTP
   fetches. `not-stated` is a claim - "I read the guideline and it is silent" -
   and if the fetch only ever got a JavaScript shell, or a bot wall, that claim
   is false rather than merely unproven.

   So the same 20 are asked again here, through Chromium, with JavaScript
   allowed to run. The script does not classify anything: it prints what each
   page says about submitting elsewhere, and whether the browser got materially
   more text than a plain fetch did.

   Usage:  node scripts/verify-not-stated-browser.js --targets research/not-stated.json
*/
"use strict";
const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const ROOT = path.resolve(__dirname, "..");
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > -1 ? process.argv[i + 1] : d; };
const OUT = path.resolve(ROOT, arg("--out", "research/browser-verify"));
const TARGETS = arg("--targets", "research/not-stated.json");

// Anything that could carry a policy on submitting elsewhere. Deliberately
// broad - this produces reading material, not answers.
const PROBE = /simultaneous|at the same time|other publication|other journal|elsewhere|exclusiv|under consideration|concurrent|multiple (submissions|pieces)|one (submission|piece) at a time/i;

// A page shorter than this did not render - it is a challenge page, a bot wall
// or an error. The FIRST version of this script called anything with no probe
// hit "silent", which meant five bot-walled pages ("Confirm you are human",
// "403 - Forbidden") were reported as findings of silence. That is exactly the
// defect main's c61f1ff46cf documents: a blocked fetch rendered as a finding of
// silence. A short page is UNREADABLE, never silent.
const MIN_READABLE = 400;
const CHALLENGE = /confirm you are human|not a robot|access to this page is forbidden|just a moment|checking your browser|enable javascript|captcha|attention required|cf-error|403 forbidden/i;

/* A plain HTTP fallback, used when Chromium itself gets walled. A headless
   browser is not always the less suspicious client: five pages that returned a
   "Confirm you are human" challenge to Chromium served their full guideline to
   a plain fetch carrying a normal Safari user-agent. */
function plainFetch(url) {
  return new Promise((resolve) => {
    const https = require("node:https");
    const zlib = require("node:zlib");
    try {
      const rq = https.get(url, {
        headers: {
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " +
                        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
          "Accept": "text/html,application/xhtml+xml",
          "Accept-Language": "en-US,en;q=0.9",
          "Accept-Encoding": "gzip, deflate",
        },
        timeout: 30000,
      }, (res) => {
        const chunks = [];
        let stream = res;
        const enc = (res.headers["content-encoding"] || "").toLowerCase();
        if (enc.includes("gzip")) stream = res.pipe(zlib.createGunzip());
        else if (enc.includes("deflate")) stream = res.pipe(zlib.createInflate());
        stream.on("data", (d) => chunks.push(d));
        stream.on("end", () => {
          const html = Buffer.concat(chunks).toString("utf8");
          const text = html
            .replace(/<(script|style|nav|footer|head)[^>]*>[\s\S]*?<\/\1>/gi, " ")
            .replace(/<br\s*\/?>|<\/p>|<\/li>|<\/div>|<\/h[1-6]>/gi, "\n")
            .replace(/<[^>]+>/g, " ")
            .replace(/&nbsp;/g, " ").replace(/&amp;/g, "&")
            .replace(/&#8217;|&rsquo;/g, "\u2019").replace(/&quot;/g, '"')
            .replace(/[ \t\u00a0]+/g, " ");
          const lines = text.split("\n").map(l => l.trim()).filter(Boolean);
          const norm = [...new Set(lines)].join("\n").trim();
          const hits = norm.split("\n").filter(l => PROBE.test(l));
          resolve({ text: norm, chars: norm.length, hits });
        });
      });
      rq.on("error", () => resolve(null));
      rq.on("timeout", () => { rq.destroy(); resolve(null); });
    } catch { resolve(null); }
  });
}

(async () => {
  if (!fs.existsSync(TARGETS)) { console.error(`no target list at ${TARGETS}`); process.exit(2); }
  const targets = JSON.parse(fs.readFileSync(TARGETS, "utf8"));
  fs.mkdirSync(OUT, { recursive: true });

  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " +
               "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    locale: "en-US",
    extraHTTPHeaders: { "Accept-Language": "en-US,en;q=0.9" },
  });

  const results = [];
  for (const t of targets) {
    const slug = t.slug, url = t.url;
    const rec = { slug, publication: t.publication, url, browserChars: 0, httpChars: t.httpChars ?? null };
    let page;
    try {
      page = await ctx.newPage();
      const resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
      rec.status = resp ? resp.status() : null;
      // let client-side rendering settle
      try { await page.waitForLoadState("networkidle", { timeout: 15000 }); } catch {}
      await page.waitForTimeout(1500);
      const text = await page.evaluate(() => document.body ? document.body.innerText : "");
      const norm = text.replace(/[ \t\u00a0]+/g, " ").replace(/\n{2,}/g, "\n").trim();
      rec.browserChars = norm.length;
      fs.writeFileSync(path.join(OUT, `${slug}.browser.txt`), norm, "utf8");

      const hits = [];
      for (const line of norm.split("\n")) {
        if (PROBE.test(line)) {
          const s = line.trim();
          if (s && !hits.includes(s)) hits.push(s);
        }
      }
      rec.hits = hits.slice(0, 8);

      // Verdict: never let an unreadable page be recorded as silence.
      const looksBlocked = rec.browserChars < MIN_READABLE || CHALLENGE.test(norm);
      if (looksBlocked) {
        // The browser was walled. A plain fetch often is not - the inverse of
        // main's finding, where a script was walled and the browser was not.
        // Both cases have the same rule: the field may not claim silence.
        const alt = await plainFetch(url);
        if (alt && alt.chars >= MIN_READABLE) {
          rec.plainChars = alt.chars;
          rec.plainHits = alt.hits.slice(0, 8);
          fs.writeFileSync(path.join(OUT, `${slug}.plain.txt`), alt.text, "utf8");
          rec.verdict = alt.hits.length ? "HAS-TEXT-TO-READ" : "silent-plain-fetch";
          rec.hits = alt.hits.slice(0, 8);
        } else {
          rec.verdict = "unreadable";
        }
      } else {
        rec.verdict = hits.length ? "HAS-TEXT-TO-READ" : "silent";
      }
    } catch (e) {
      rec.error = String(e).split("\n")[0].slice(0, 160);
      rec.verdict = "unreadable";
    } finally {
      if (page) await page.close().catch(() => {});
    }
    results.push(rec);
    console.log(
      `  ${slug.padEnd(30)} http=${String(t.httpChars ?? "-").padStart(6)} ` +
      `browser=${String(rec.browserChars).padStart(6)}  ${rec.verdict}` +
      (rec.error ? `  (${rec.error})` : "")
    );
    fs.writeFileSync(path.join(OUT, "results.json"), JSON.stringify(results, null, 1));
  }

  await browser.close();
  const bad = results.filter(r => r.verdict === "HAS-TEXT-TO-READ");
  const unreadable = results.filter(r => r.verdict === "unreadable");
  const viaPlain = results.filter(r => r.verdict === "silent-plain-fetch");
  console.log(`\n${results.length} asked`);
  console.log(`  silent in the browser   : ${results.filter(r => r.verdict === "silent").length}`);
  console.log(`  silent, browser walled,`);
  console.log(`    plain fetch worked    : ${viaPlain.length}`);
  console.log(`  HAVE TEXT - must re-read: ${bad.length}`);
  console.log(`  STILL UNREADABLE        : ${unreadable.length}` +
              (unreadable.length ? "  <- must NOT be recorded as silent" : ""));
  if (bad.length) console.log("\nRE-READ THESE:", bad.map(r => r.slug).join(", "));
  if (unreadable.length) console.log("STILL UNREAD:", unreadable.map(r => r.slug).join(", "));
})();
