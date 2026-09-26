# BRYME Audit Findings Register

Living register for Track A (owner master-audit brief). Every finding: issue · URLs · severity · evidence · fix · status.
Severity: P0 = broken live / P1 = compliance-trust blocker / P2 = SEO-quality gap / P3 = polish.

Last sweep: 2026-09-26 · deploy `dep-das1307f` (commit `b93550f`) live.

---

## Fixed & verified live

| # | Severity | Issue | Evidence | Fix | Status |
|---|----------|-------|----------|-----|--------|
| A1 | P1 | House privacy policy (`/privacy/`) omitted the Money desk — desk list read "Writers, Tech, Sport, Entertainment, Fitness and Home & DIY", while Money runs its own policy at `/money/privacy/` | External audit appendix + `scripts/build-ecosystem.py` L7283/L7311 | Dek now names all 7 desks; "What each desk does" gained a Money bullet linking `/money/privacy/`; meta description corrected | **FIXED — live-verified** `b93550f`, probe: `/privacy/` contains "BRYME Money privacy" ✓ |
| A2 | P2 | Stale desk counts: OG house-standard card said "Six publications" | `scripts/make_og_image.py` L27 | Changed to "Seven publications" | **FIXED — shipped** `b93550f` |
| A4 | P2 | Error-handling sweep: do unknown URLs soft-404? | Probed `/nonexistent-page-xyz/`, `/money/nonexistent-guide/`, `/entertainment/definitely-not-here/` | All return true **HTTP 404** with branded "Page not found \| THE BRYME" title — no soft-404s, no HTML-on-200 | **VERIFIED CLEAN** |
| A6 | P2 | Security sweep | Secrets scan of `public/` (ghp_/rnd_/AKIA/sk- patterns): clean. `robots.txt` live: 8 desk sitemaps listed, build dirs (`/scripts/`, `/content/`, `/docs/`, `/server/`, `/ecosystem/`) disallowed, AI-crawler block (GPTBot, Google-Extended, CCBot, Applebot-Extended, Meta-ExternalAgent, Amazonbot, Bytespider → Disallow: /) | npm audit gated in CI (quality.yml) | **VERIFIED CLEAN** (note: AI-crawler block interacts with Track B1 GEO — see D5) |
| A7 | P2 | Measured performance (no synthetic scores): TTFB 0.12–0.17s across hub/privacy/money/tech. Page weights: `/` 59KB, `/privacy/` 25KB, `/money/` 108KB, `/tech/` 260KB (heaviest hub — watch item). Heaviest assets: `pdfjs.worker.min.js` 1.09MB, `pdf-lib.min.js` 525KB (vendor, PDF tool pages only) | curl timing probes 2026-09-26 | No action needed; keep tech hub under review as clusters grow (A8) | **VERIFIED — baseline recorded** |

## Open findings

| # | Severity | Issue | URLs | Evidence | Proposed fix | Status |
|---|----------|-------|------|----------|--------------|--------|
| A5 | P2 | ~~Zero JSON-LD on Money/Sports pages~~ **CORRECTED**: original sweep ran during the churn window and was wrong. Re-verified against git HEAD: every page has JSON-LD; Sports/Fitness/Ent guides already carry Article. Real gap: **Money guides were typed WebPage instead of Article** (inconsistent with the other desks) | `/money/<guide>/` (101 pages incl. Tier-A) | Type scan of committed tree, 2026-09-26 | `_page_ld` in build-ecosystem.py now emits Article (headline, author=BRYME Money desk org, mainEntityOfPage) for money pages carrying a review byline; no datePublished invented — dateModified = visible review date. Validator updated to enforce the real invariant (schema URL = page URL, dateModified = manifest reviewed date) regardless of node type | **FIXED** — 101 Article / 13 WebPage (hub, privacy, about, drawers correctly stay WebPage); validators green |
| A3 | P2 | Indexation architecture classification: which URL classes are discoverable vs orphaned (crawl paths) | site-wide | Needs the full internal-link graph pass (261,085 links / 3,923 pages last audit) re-run per desk with class tagging | **OPEN** |
| A8 | P2 | Desk programs: Money jurisdiction clarity banner, Ent thin-catalogue analysis, Sport timestamps, Home problem-intent, Tech clusters, Writers DB protection | per-desk | Owner brief §desk programs | Per-desk work plans after A3–A5 | **OPEN** |
| A9 | P3 | Internal-link density audit on newest pages (Tier-A wave) | 24 Tier-A slugs | Tier-A pages carry 2–4 contextual links each by construction; shelf/hub links exist | Include in A3 graph pass | **OPEN** |
| A10 | P3 | AdSense/consent mechanics sweep | site-wide | Not yet swept | After A5 | **OPEN** |
| D5 | decision | robots.txt blocks all major AI crawlers — conflicts with Track B1 GEO ambition (being cited by LLMs needs crawlable pages or llms.txt + selective allow) | `/robots.txt` | Live fetch 2026-09-26 | Owner decision: keep block, or allow GPTBot/PerplexityBot etc. selectively | **OPEN — owner** |

## Verified non-issues (do not re-investigate)

- **"Explainers shelf regression" (28 vs 60 pieces)** — false alarm ×2. Cause 1: sandbox snapshot truncation deleted 6,113 tracked files mid-session; restored + rebuild returned 60/60. Cause 2: probe URLs built from memory lacked the `-explained` suffix and assumed an `explainers/` subpath. Canonical URLs live in the desk sitemaps; **24/24 Tier-A slugs probed 200** on 2026-09-26.
- Money sitemap = 115 URLs; sports 188; fitness 180; entertainment 1,584; tech 371 — all match HEAD exactly.

## Probe protocol (learned the hard way)

1. Never construct probe URLs from memory — extract them from the desk sitemaps (`grep -o "https://thebryme.com[^<]*<slug>"`).
2. All Tier-A pages live at desk-root (`/desk/slug-explained/`), not in subdirectories.
3. After any workspace restore, run `build-ecosystem.py` **before** `npm run build` (npm chain does not regenerate `ecosystem/`).
4. **Never record an audit finding from a working tree during a churn window** — snapshot truncation struck twice on 2026-09-26 (6,113 files each time, once mid-turn). Findings must be verified against committed HEAD (`git show HEAD:<path>`) before entering this register. Both "regressions" this session (explainers shelf, zero JSON-LD) were truncation artifacts.
