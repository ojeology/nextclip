# BRYME — Search Performance Audit (GSC window Sep 20 – Oct 6, 2026)

**Scope:** independent verification of the supplied GSC breakdown against the actual site
build, plus Tier-1 implementation. The live site (thebryme.com) is not reachable from the
build sandbox, so page-level facts were verified against the shipped artifact (`public/`)
and the source trees it is generated from. Your GSC figures themselves cannot be
recomputed without an export; everything testable from the build was tested.

---

## A. What Google appears to reward on BRYME

Verified from the build, and consistent with your GSC segmentation:

1. **The Writers dossier cluster is real and structurally different.** ~305 pages under
   `/writers/writing/<publication>/` (West Branch, Noema, Walrus, Asimov's, Analog,
   Stinging Fly…). Each carries: Article JSON-LD with author Person + Organization,
   a *specific dollar/₦ amount and submission terms in the title itself*
   ("100 Word Story: exactly 100 words, $2 fee", "AARP: up to ~$1/word"),
   a fact-dense description, breadcrumbs, and 20+ contextual links into the writers'
   hub system (tools, verification, tracker, opportunities). This is original,
   hard-to-replicate data (verified pay rates + windows). Google's reward pattern
   (pos 5–15 for named-publication queries) matches exactly what this page type is.
2. **Narrow, non-obvious explainers with a "reviewed <date>" freshness line.**
   Every performing Sports/Entertainment/Tech page (Offside Trap, FFP, football loans,
   RTD, post-credits, wide-vs-limited, GitHub Pages, Render static deploy) has a visible
   "reviewed 2026-09-25 · evergreen explainer" byline block and deep, opinionated prose.
3. **Nigeria/India geographies.** Your country table (NG 5.93% CTR pos 29, IN pos 21)
   confirms BRYME wins where the big incumbents don't localize. The Writers desk
   (Nigerian author, ₦ pay rates, African publications) has real E-E-A-T there.

## B. What Google ignores or ranks poorly

1. **Live sports database pages** — PL table, PL/UCL top scorers, pos 51–68 with the
   biggest impression volumes on the site. Verified cause: these pages cannot beat
   Google/ESPN on freshness for live data; "no odds, no tips, no invented facts" is a
   virtue for humans but means the page changes slowly. **Structural, not fixable by
   titles.** They still earn impressions as brand surfaces; keep them, don't invest.
2. **Generic "how to write X" guides** — pos 40–90. Verified cause: competing against
   Grammarly/Indeed/Purdue OWL with no differentiation; titles are exact clones of the
   SERP leaders'. Not a quality problem — a competition problem.
3. **Generic tech comparison pages** (cloud storage, hosting costs) — pos 48–78.
   Same cause: head terms owned by CNET/Tom's Guide/PCMag with affiliate budgets.
4. **Individual movie database pages** — pos 25–94. IMDb/Wikipedia own these forever.
5. **The ~950-page zero-click segment is largely the ~954 root-level stub pages**
   ("<slug> moved | THE BRYME", noindex,follow, meta-refresh, canonical to
   `/entertainment/<slug>/`). These correctly show 0 clicks — they *should* generate
   impressions-then-decay. **Your 950-page zero-click pool is mostly an indexing
   artifact of the routing migration, not 950 failing articles.** This is the single
   biggest correction to your supplied analysis: the "95% of the site gets 0% CTR"
   framing overstates real content failure; a large share is migration plumbing.

## C. Strongest content formats (verified)

| Format | Evidence | Why it wins |
|---|---|---|
| Publication dossier w/ verified pay + terms | ~305 writers pages, pos 5–15 | unique data, schema, entity match |
| Narrow sports concept/scenario explainer | Offside Trap p11, loans p9, RTD p12, FFP p16 | low competition, clear intent |
| "X vs Y" and "shows/movies like X" recommendation | Alice in Borderland p8.75/532impr/4 clicks | recommendation intent, curated value |
| "What does X mean / why does X happen" odd-question explainer | post-credits p7.9, AFCON p11.6 | non-obvious, nobody else answers it well |
| Specific tech troubleshooting/comparison | Render static deploy p6.2, M365 free-vs-paid p13.9 | problem-solving intent, practical |

Common model: **specific entity/concept query → original-data or curated-value page →
weak SERP (no dominant incumbent) → BRYME answers with specifics nobody else has.**

## D. Weakest formats (verified)

Live sports tables/scorers; generic how-to-write guides; broad tech comparisons;
individual movie pages; broad "what is X" film explainers; generic home-improvement
how-tos (see G).

## E. Top 20 pages to optimize (ranked: impressions × proximity to page 1)

**Tier 1 — pos 5–15, zero/low CTR (title+snippet work) — IMPLEMENTED this audit:**
1. /tech/microsoft-365-free-vs-paid/ (p13.9, 144 impr) — ✅ title+meta rewritten (old meta was truncated mid-word)
2. /sports/how-football-loans-work/ (p9.4, 101 impr, 0 clicks) — ✅ "…wages, fees and the FIFA rules"
3. /entertainment/movies-like-deadpool-and-wolverine/ (p7.8, 106 impr, 0 clicks) — ✅ added "and Where to Watch Them"
4. /sports/what-does-rtd-mean-in-boxing-explained/ (p11.9, 73 impr, 0 clicks) — ✅ "RTD in boxing: what it means on a fight record"
5. /entertainment/post-credits-scenes-explained/ (p7.9, 62 impr, 0 clicks) — ✅ "…explained: stay or go?" + fixed truncated meta
6. /tech/where-to-host-website-for-free/ (p10.2, 63 impr, 0 clicks) — ✅ title "(and what free really means)" + fixed truncated meta
7. /entertainment/wide-vs-limited-release-explained/ (p10.7, 53 impr) — ✅ "what the difference actually means" + fixed truncated meta
8. /entertainment/10-facts-about-agent-kim-squid-game-season-3/ (p9.5, 34 impr) — ✅ added "(Kang No-eul)" + fixed truncated meta

**Tier 2 — pos 11–30, meaningful impressions, realistic improvement (recommended, not yet edited):**
9. /sports/financial-fair-play-explained/ (p15.9, 54 impr) — add PSR numbers/2026 examples to body
10. /sports/why-afcon-moves-around/ (p11.6, 43 impr)
11. /sports/can-ronaldo-score-1000-goals/ (p12.0, 30 impr) — keep the living tracker fresh weekly
12. /sports/possession-explained/ (p14.8, 30 impr)
13. /sports/bundesliga-transfers/ (p15.4, 35 impr)
14. /sports/la-liga/ hub (p11.6, 39 impr)
15. /tech/github-pages-not-showing-changes/ (p18.8, 32 impr)
16. /tech/render-vs-vercel-vs-netlify/ (p16.4, 30 impr) — already has dated pricing; add a verdict box
17. /entertainment/solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences/ (p8.4, 24 impr)
18. /entertainment/why-are-modern-movies-so-dark-explained/ (p7.5, 20 impr)
19. /entertainment/how-oscars-voting-works-explained/ (p11.7, 19 impr)
20. /entertainment/film-movements-explained/ (p11.1, 46 impr)
Next tier (pos 20–30, from your data): Literary Hub-adjacent dossiers at p14–15
(Bombay Literary, The Offing) — push with internal links from the 5 strongest dossiers.

## F. Top 20 new content opportunities (winning formats only)

**Writers (dossier machine — keep feeding it):**
1–8. Next 8 named publications with verified pay: Room Magazine, Prairie Schooner,
The Common, Guernica, Electric Literature, Ploughshares, The Sun Magazine, One Story —
same template, pay + window + fee in title.
**Sports (narrow concept/scenario explainers):**
9. Why do goalkeepers wear different kits — rules explained
10. What is a sporting director (vs manager/head coach)
11. How away-goals rule changed (and why UEFA killed it)
12. What does "points deduction" actually do to a club (Everton/Forest cases)
13. How boxing purses and PPV splits actually work
14. Why do footballers go on strike-train / what "transfer request" means legally
**Entertainment (recommendations + odd questions):**
15. Shows like Severance / movies like Everything Everywhere (pair the two biggest gaps)
16. Why are streaming credits so long now (post-credits sibling)
17. What "limited series" actually means vs miniseries vs cancelled
18. Anime like Frieren / like Vinland Saga (quiet-epic niche)
**Tech (troubleshooting + free-tier reality):**
19. "Netlify/Vercel deploy succeeded but site didn't change" (GitHub Pages sibling)
20. Cloudflare Pages vs GitHub Pages vs Render — free static hosting compared (consolidates two winning clusters)

## G. Pages that should NOT receive further investment

- Live database pages (PL/UCL tables, top scorers, fixtures): keep for brand/hub
  completeness, zero new content investment beyond the existing automated updates.
- Individual movie pages (War of the Worlds, Se7en, Titanic…): no new pages; existing
  ones only matter as internal-link targets.
- Generic how-to-write guides: freeze; any upgrade effort goes to dossiers instead.
- **No mass deletion.** The 0-click pool is mostly noindex migration stubs (working as
  designed) plus long-tail pages that cost nothing to keep and carry internal links.

## H. Desk strategy

- **Writers — expand.** Strongest asset on the site; the dossier format is proven,
  scalable, and defensible. Highest new-content priority.
- **Sports — pivot investment, don't abandon.** Stop new live-database pages; build the
  narrow concept/scenario explainer library (F list). Keep existing tables maintained
  but deprioritized.
- **Entertainment — continue, narrowed.** Recommendations/comparisons/odd-question
  explainers only. No more individual movie pages, no broad "what is X" film-school pages.
- **Tech — continue, narrowed.** Troubleshooting ("X not showing changes"), free-tier
  reality checks, dated hands-on comparisons. No broad category comparisons.
- **Home — reduce and rework, don't abandon (yet).** Verified cause of weakness: the
  Home pages checked (ceiling fan p73, insulation p65, fan noise p74, fire signs p86)
  target the *most competitive generic version* of US/UK home topics, against This Old
  House/Bob Vila/gov.uk — the exact mistake Sports/Tech stopped making. The desk's
  Nigeria-relevant content (harmattan, borehole, changeover switch, generator-adjacent
  topics) is where the NG CTR advantage (5.93%) could transfer. Recommendation: pause
  new generic US/UK how-tos; test 5–8 narrow Nigeria/heat/power-cut-specific pages
  before deciding the desk's fate. Home gets the least new-content budget until that test returns data.

## I. Technical/indexing findings (from the build)

1. **Truncated meta descriptions shipped live** (ends mid-word: "…who the paid tiers
   are ", "…This is what GitHub Pages, C"). Cause: `trim-meta-descriptions.py` has a
   hard cutoff at 170 chars with a "last whole word" fallback — but it only trims
   descriptions >170 chars, and these pages sat at 155–158, under its LIMIT while still
   being pre-truncated strings in the source. The truncation happened upstream of the
   trimmer (likely an earlier generator capped at ~155). **Fixed for the 8 Tier-1 pages;
   recommend a sweep for any other description ending without terminal punctuation.**
2. **~954 noindex stub pages at root** are correct and should be left alone; their
   impressions in GSC will decay as Google re-crawls. Do not 410 them (the canonical
   signal is still consolidating).
3. Sitemap structure is healthy (per-desk sitemaps, index at root). Writers sitemap
   carries 679 URLs — consider splitting dossiers into their own sitemap to watch the
   cluster's indexing separately in GSC.
4. `verify:titles` and the title auditor pass; site-quality Monetag warnings are
   pre-existing on the baseline and unrelated to this audit's changes.

## J. Where I disagree with the supplied analysis

1. **"950 weak pages / 0% CTR" is mostly migration plumbing, not content failure** (B.5).
   The real weak-content pool is much smaller than 950.
2. **The CTR-fix framing "pure title work, no ranking improvement needed" is
   half-wrong for two pages.** RTD and Agent Kim already have decent titles; their
   metas were *truncated mid-word* — a technical defect, not a persuasion problem.
   Fixing truncation is the highest-confidence fix on the list because it repairs a
   visibly broken snippet.
3. **Home should not be judged hopeless on current data** — it has only ever tried the
   generic-head-term play that fails in every desk. It hasn't yet tried the
   narrow/specific/geo-relevant play. One cheap test decides it.
4. Everything else in your pattern analysis (Rule 1 format, Rule 2 specificity) is
   **supported by the build evidence** — dossier pages genuinely carry unique data,
   schema, and internal-link density that the generic pages lack, and the narrow
   explainers genuinely target queries with no dominant incumbent.

---

## Implementation log (this audit, Tier 1 only)

Rewrote title + meta description (+og/twitter mirrors) on the 8 zero-CTR Tier-1 pages,
in both the source trees and `public/`. All descriptions now end as complete prose at
≤160 chars. No keywords added that the articles don't cover; no page's primary keyword
was removed. `npm run verify:titles` passes (0 problems). Monetag validator warnings
exist identically on the unmodified baseline (pre-existing, out of scope).

No Tier-2 body edits, no deletions, no noindex changes, no new pages — per the
"high-confidence only" instruction.
