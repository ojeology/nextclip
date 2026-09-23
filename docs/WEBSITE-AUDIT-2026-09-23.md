# BRYME full audit — 2026-09-23

Scope: live site (thebryme.com) + complete repo at `c8cdcb30` + build pipeline.
Method: live crawl verification (625-URL sample + all desk hubs), full
source-tree analysis (all 2,042 published pages), repo quality gates, live
performance probes.

> Process note: the first audit pass ran on a workspace copy truncated by a
> file-size cap, which produced three false alarms (missing quality.yml,
> missing pages, sitemap/404 mismatch). Every finding below was re-verified
> against a fresh clone and the live site. All clear — the repo on GitHub is
> complete and healthy.

## Site-wide health — what is right (do not touch)

| Area | Result |
|---|---|
| Sitemap integrity | All declared URLs verified reachable — **zero 404s** in the 625-URL live sample incl. every hub |
| Titles / meta descriptions | 0 missing across 2,042 pages (1 exception: one moved-page tombstone) |
| Canonicals | Correct on every sampled page; no legacy `onrender.com` refs published |
| Images | 100% alt coverage on sampled pages |
| Structured data | JSON-LD present site-wide (exceptions: moved-page tombstones only) |
| Performance (live TTFB / HTML weight) | 48–138 ms / 25–83 KB — excellent, no work needed |
| Security headers | Full CSP + HSTS + frame/permission policies verified |
| Quality gate | `validate-site-quality.js --quick` passes (0 duplicate sitemap listings) |
| Monetization rails | ads.txt, loader, consent defaults, GDPR CMP — verified this week |
| Automation | Daily sports-data agent exists (`sports-update.yml`, 06:00/22:00 UTC) |

## Errors and weaknesses found (ranked)

### 1. Entertainment desk is 85% thin — the site's biggest problem
- 726 of 847 pages carry **<300 words**; the 490 movie pages run **133–149
  words median, 194 max**. They are poster + synopsis stubs.
- Desk average internal links: 47/page vs 140 on writers.
- Impact: Google has indexed ~300/2,033 site URLs; a desk this thin plausibly
  suppresses crawling/indexing priority site-wide, and it can never qualify
  for good ad placement.

### ~~2. Stale/moved URLs in the entertainment sitemap~~ — CORRECTED, not an issue
- Re-verification (exact slug match against both sitemaps): the "Moved:"
  tombstones are **NOT listed in any sitemap** — the generator already
  excludes them. The earlier "3+" hits were substring matches against the
  canonical slugs (`grand-budapest` matches `the-grand-budapest-hotel`).
  No action needed; the build handles merges exactly right.

### 3. Dates missing from structured data — PARTIALLY FIXED 2026-09-23
- Correction: writers *articles* already carried real `datePublished` (from
  `publishedAt` in the content JSON). The undated 147 were venue/tool pages.
- Fixed: `_page_ld` now emits an honest `dateModified` (build date) on every
  generated desk page — covers home 223, sports 83, tech 33, plus writers
  venue pages. `datePublished` stays where a true date exists.

### 4. Sports fixture/stats pages are thin and possibly stale
- 18 pages (e.g. `bundesliga-top-scorers`, `champions-league-fixtures`) are
  <300 words. The daily data agent exists but likely isn't running — the
  `FOOTBALL_DATA_API_KEY` secret must be set in GitHub for it to act.

### 5. Writers desk has ~40 thin venue pages
- `make-money/writing/<venue>` pages and the by-country hub are stubs on an
  otherwise strong desk (median 651 words).

### 6. Minor
- Moved-tombstone pages lack OG image/schema (cosmetic; canonical consolidates).
- 5 "Page moved" tombstones under writers share a title (cosmetic).
- Workspace ops: the repo tree is ~490 MB with `public/`; workspace copies
  should stay lean (see roadmap Phase 0 note).

## Per-desk scorecard

| Desk | Pages | Median words | Thin (non-utility) | Undated | Grade |
|---|---|---|---|---|---|
| writers | 518 | 651 | ~40 venue pages | 147 | **B+** |
| tech | 291 | 628 | ~0 real | 33 | **B+** |
| home | 229 | 644 | ~0 real | 223 | **B** (newest, undated) |
| fitness | 45 | 492 | ~0 real | 8 | **B** (low volume) |
| sports | 111 | 457 | 18 | 83 | **C+** (agent idle?) |
| entertainment | 847 | 153 | ~690 | 18 | **F** ← weakest by far |

## Verification log (key probes)

- 625 sitemap URLs live-checked: 625 × HTTP 200.
- Desk hub TTFB: `/` 138 ms, `/writers/` 49 ms, `/entertainment/` 75 ms,
  `/tech/` 52 ms, `/home/` 60 ms, `/sports/` 71 ms, `/fitness/` 54 ms.
- `/home/fix/` live render: 2,090 main-words, self-canonical, indexable.
- Movie-page word distribution (490 pages): min 20 / p25 133 / median 141 /
  p75 149 / max 194.

## Fixes applied 2026-09-23 (Phase 0 + Phase 1 batch 1)

1. `dateModified` on all generated desk pages (`build-ecosystem.py`).
2. Entertainment film-page template upgrade: "The desk's verdict" section,
   "More like this" (3 same-genre internal links on **every** film page —
   fixes the 47/page link deficit), FAQ section + FAQPage JSON-LD.
3. `scripts/entertainment_enrichment.py` (new): batch-1 editorial layer for
   15 flagship titles (Dune II, Oppenheimer, Interstellar, Godzilla Minus One,
   Top Gun: Maverick, Endgame, No Way Home, EEAAO, Grand Budapest, 1917, 300,
   2001, Baahubali, Half of a Yellow Sun, Living in Bondage + MI: Final
   Reckoning). Verified build: enriched pages 328–440 words (from ~150),
   non-enriched pages degrade gracefully (links only, no stub sections).
4. Sports data agent confirmed WORKING with the owner-authorized fallback
   key (documented twice-daily runs; PRESERVE guard added after the 22 Sep
   incident). No action needed.
5. Audit corrections: sitemap tombstones (not an issue), writers article
   dates (already present).

Deployment note: Render's build does NOT run `build-ecosystem.py` — run it
locally (`python3 scripts/build-ecosystem.py` from the repo root), review the
tree diff, commit, push. Verified locally on a full checkout; the film-page
sample is in `bryme-changeset/samples/movie-page-enriched-sample.html`.
