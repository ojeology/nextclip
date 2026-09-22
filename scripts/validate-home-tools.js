#!/usr/bin/env node
/* BRYME — home tool integrity gate.
   Zero dependencies: pure Node fs/path/child_process, no Playwright, no npm install.

   WHY THIS EXISTS
   Gate 3 (validate-browser.js) covers 509 Writers routes only. Nothing loaded a
   Home & Property tool page, so a broken mount id, a missing asset, or a JS syntax
   error would ship silently. Five of the six directive tools build their forms via
   innerHTML, which means a static grep of page HTML for <input> finds nothing --
   that is exactly how a prior audit wrongly concluded the tools were "0/6 built".

   WHAT IT ASSERTS, per tool
     1. the page exists in public/
     2. the page actually references its JS asset
     3. the asset exists in assets/ AND public/assets/, and the two are identical
     4. the asset parses (node --check)
     5. MOUNT INTEGRITY: every getElementById("X") in the JS resolves -- either X
        exists in the page HTML, or the JS itself creates it via an id="X" string.
        This is the check that catches a silently blank tool.
     6. the tool is genuinely interactive: it creates or targets at least one
        input / select / textarea / button
     7. a YMYL disclaimer is present, unless the tool is on the allowlist of
        non-financial tools (a maintenance checklist makes no financial claim)

   Exit code 1 on any failure, with a per-tool report. Safe to run anywhere:
   it never writes, never touches the network, and needs no build step. */

"use strict";

const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");

/* slug -> [js asset basenames]. seasonal checklist is driven by two scripts. */
const TOOLS = [
  ["home/water-damage-insurance-coverage", ["water-claim-quiz.js"]],
  ["home/mortgage-payments-explained", ["mortgage-calculator.js"]],
  ["home/rent-vs-buy-explained", ["buy-vs-rent-calculator.js"]],
  ["home/home-repair-costs-explained", ["repair-cost-estimator.js"]],
  ["home/moving-costs-explained", ["moving-cost-estimator.js"]],
  ["home/seasonal-home-maintenance-checklist", ["seasonal-tool.js", "home-checklist.js"]],
];

/* Tools that legitimately carry no financial/legal disclaimer. */
const DISCLAIMER_EXEMPT = new Set(["seasonal-tool.js", "home-checklist.js"]);

const DISCLAIMER_RE = /not financial advice|general guidance|general information|never financial advice|estimate only|directional|your lender|your quotes|governs/i;
const INTERACTIVE_RE = /<(?:input|select|textarea|button)\b/i;

function read(p) {
  return fs.readFileSync(p, "utf8");
}
function exists(p) {
  try {
    fs.statSync(p);
    return true;
  } catch (e) {
    return false;
  }
}

/* Every id the JS asks the document for. */
function jsRequestedIds(js) {
  const out = new Set();
  const re = /getElementById\(\s*["']([^"']+)["']\s*\)/g;
  let m;
  while ((m = re.exec(js))) out.add(m[1]);
  return out;
}

/* Every id the JS creates for itself inside its own markup strings. */
function jsCreatedIds(js) {
  const out = new Set();
  const re = /\bid\s*=\s*(?:\\?["'])\s*([A-Za-z][\w:-]*)/g;
  let m;
  while ((m = re.exec(js))) out.add(m[1]);
  return out;
}

/* Every id present in the served page HTML. */
function pageIds(html) {
  const out = new Set();
  const re = /\bid\s*=\s*"([^"]+)"/g;
  let m;
  while ((m = re.exec(html))) out.add(m[1]);
  return out;
}

function parses(file) {
  try {
    execFileSync(process.execPath, ["--check", file], { stdio: "pipe" });
    return [true, ""];
  } catch (e) {
    const msg = String(e.stderr || e.message).split("\n").slice(0, 3).join(" ").trim();
    return [false, msg];
  }
}

let failures = 0;
const lines = [];

function fail(tool, msg) {
  failures++;
  lines.push(`  \u2717 ${tool}: ${msg}`);
}
function pass(tool, detail) {
  lines.push(`  \u2713 ${tool}${detail ? " \u2014 " + detail : ""}`);
}

for (const [slug, assets] of TOOLS) {
  const pagePath = path.join(ROOT, "public", slug, "index.html");
  const label = slug.replace("home/", "");

  /* 1. page exists */
  if (!exists(pagePath)) {
    fail(label, `page missing: public/${slug}/index.html`);
    continue;
  }
  const html = read(pagePath);
  const htmlIds = pageIds(html);

  const notes = [];
  for (const asset of assets) {
    const srcPath = path.join(ROOT, "assets", asset);
    const pubPath = path.join(ROOT, "public", "assets", asset);

    /* 2. page references the asset */
    if (!html.includes(`/assets/${asset}`)) {
      fail(label, `page does not reference /assets/${asset}`);
      continue;
    }

    /* 3. both copies exist and are identical */
    if (!exists(srcPath)) {
      fail(label, `source asset missing: assets/${asset}`);
      continue;
    }
    if (!exists(pubPath)) {
      fail(label, `served asset missing: public/assets/${asset}`);
      continue;
    }
    if (read(srcPath) !== read(pubPath)) {
      fail(label, `assets/${asset} and public/assets/${asset} DIFFER (stale mirror)`);
      continue;
    }

    const js = read(srcPath);

    /* 4. parses */
    const [ok, err] = parses(srcPath);
    if (!ok) {
      fail(label, `${asset} fails node --check: ${err}`);
      continue;
    }

    /* 5. mount integrity */
    const requested = jsRequestedIds(js);
    const created = jsCreatedIds(js);
    const unresolved = [...requested].filter((id) => !htmlIds.has(id) && !created.has(id));
    if (unresolved.length) {
      fail(label, `${asset} reads id(s) nothing provides: ${unresolved.join(", ")} \u2014 tool renders blank`);
      continue;
    }

    /* 6. genuinely interactive */
    if (!INTERACTIVE_RE.test(js) && !INTERACTIVE_RE.test(html)) {
      fail(label, `${asset} creates no input/select/textarea/button \u2014 not interactive`);
      continue;
    }

    /* 7. YMYL disclaimer */
    if (!DISCLAIMER_EXEMPT.has(asset) && !DISCLAIMER_RE.test(js) && !DISCLAIMER_RE.test(html)) {
      fail(label, `${asset} carries no YMYL disclaimer (required by the production directive)`);
      continue;
    }

    notes.push(`${asset}: mount ok, ${requested.size} id(s) resolved, parses, interactive`);
  }

  if (notes.length === assets.length) pass(label, notes.join("; "));
}

console.log("\nhome tool integrity gate \u2014 " + TOOLS.length + " tool pages, " +
  TOOLS.reduce((n, t) => n + t[1].length, 0) + " assets");
console.log(lines.join("\n"));

if (failures) {
  console.log(`\nFAIL \u2014 ${failures} problem(s). A broken home tool ships silently without this gate.`);
  process.exit(1);
}
console.log("\nPASS \u2014 all six Home & Property directive tools are wired, parse, mount and are interactive.");
process.exit(0);
