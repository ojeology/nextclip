# BRYME ROADMAP v2 — merged (owner master-audit brief × growth hypotheses)
**Supersedes:** ROADMAP v1 (28ebdeb). **Merged:** 2026-09-26 from owner's `bryme-master-audit-seo-optimization-prompt.md` + agent's GROWTH-HYPOTHESES.md. **Status:** ACTIVE — Track A executing now.

## Governing principles (from the owner brief — binding on all work)
1. Audit before changing; inspect actual implementation, never assume.
2. No rebuilds, no mass-generated pages, no deletions without evidence, no casual URL changes.
3. Fix root causes, not cosmetic patches; never claim fixed without testing.
4. Success = indexed quality, impressions, clicks, tool/database usage, trust — NOT URL count.
5. Change control: smallest safe change → local test → route/canonical/sitemap verification → ship. P0/P1 before P2/P3 effort.

## Track A — Audit & harden the existing 3,237 pages (owner brief) — NOW
**A1 (P1, confirmed by owner's external audit):** house `/privacy/` omits the Money desk → add the sentence + link to `/money/privacy/`. **EXECUTING.**
**A2 (P1):** site-wide grep for stale publication-count statements ("six publications", old desk lists) → fix at generator level.
**A3 (P1):** indexation architecture pass — classify URL types (high-priority / secondary / should-not-compete): search-result pages, empty states, parameter variants, thin catalogue pages. Evidence table per URL type before any noindex.
**A4 (P1):** error-handling sweep — 404 vs soft-404, trailing-slash, uppercase, malformed URLs, redirect chains (live probes).
**A5 (P1):** structured-data audit — what JSON-LD exists per page type, validity, gaps (Article, BreadcrumbList, WebSite, Organization; no fake schema; no FAQ/HowTo per master brief).
**A6 (P2):** security scan — secrets in published tree, dependency audit (CI already gates `npm audit --audit-level=high` ✓), CORS/admin surface.
**A7 (P2):** performance measurement — real TTFB/weight/TBT samples (never invent CWV numbers); mobile-first.
**A8 (P2):** desk programs — Money jurisdiction clarity in titles/bodies ("in the UK/US" where rules differ) · Entertainment catalogue thin-page analysis (word-count floor, enrich-or-noindex decision per page) · Sport timestamping/filter-sprawl check · Home problem-intent strengthening · Tech topical clusters (Hub→Guide→Tool) · Writers opportunity-DB protection.
**A9 (P2):** internal-link architecture — every important page: hub + siblings + 2–5 related + tool + next step (much already true via hubs; gap-fill, no stuffing).
**A10 (P2):** AdSense/consent — empty-slot behavior, layout shift, consent actual behavior vs documentation.
**Deliverable:** `BRYME-AUDIT-FINDINGS.md` — living findings register (issue · URLs · severity · evidence · fix · status) in the owner's report format.

## Track B — Growth surfaces (agent hypotheses) — starts as A's P0/P1 clear
**B1 (Phase 1):** AI-answer surface — llms.txt + desk digests + fact boxes on top-100 explainers (reuses the Bing pipeline we already run daily).
**B2 (Phase 1):** Pinterest — 6 boards × 30 pins from existing OG images (owner account decision needed: D3).
**B3 (Phase 2):** "State of Paid Writing 2026" data report from the 142-publication dataset + HARO routine → referring domains.
**B4 (Phase 3):** ONE shareable tool with a result-card share object (D1: Hyrox predictor vs darts checkout trainer).
**B5 (Phase 3):** Event calendar — 4 pre-event explainers/quarter (also the Discover door).
**B6 (Phase 4):** Forum answers where our own research shows forum-dominated SERPs; newsletter once there's traffic to retain.

## Track 0 — Standing machine (both tracks ride on this)
Bing 100/day (queue 3,044) · IndexNow per deploy · CI green gate · GSC/site: checks each session · owner: submit 8 sitemaps in Bing WMT.

## Cadence & rules of engagement
- Each work session: one Track A block + (once A's P1 set is clear) one Track B block, per-desk commits, full pipeline (build → sync → gate → push → deploy → probe → IndexNow/queue).
- Content additions stay in Tier-B backlog batches (~6/desk) — the owner brief's no-mass-generation rule is fully compatible: Tier B was selected for demand + weak SERPs, not volume.
- Every finding lands in BRYME-AUDIT-FINDINGS.md with severity before its fix ships.

## Open decisions (owner)
- D1: which single tool for B4. · D2: Tier-B cadence alongside Track A (recommend: continue, it funds Track 0). · D3: Pinterest account ownership. · D4: none blocking — Track A executes now.
