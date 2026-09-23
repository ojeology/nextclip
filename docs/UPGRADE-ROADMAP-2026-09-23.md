# BRYME upgrade roadmap — from 2026-09-23

## Progress log (update after each shipped batch)

- **Film depth batches 1–4 SHIPPED** (commits `d5e4ae5`, `c6972ca4`, `7ace2537`, `24dc02db`): 100/490 movie/TV pages enriched with verdict + FAQ + similar-picks (median enriched ~370 words). Venue date-cap fix `f991a25f` (all page dates ≤ reviewedAt 2026-09-21) is live.
- **Home & Fitness volume batch SHIPPED 2026-09-23**: fitness desk 45 → 55 pages (10 beginner guides: push-up progression, squat form, soreness vs injury, resistance bands, stretching timing, Nigerian protein foods, beginner running plan, workout timing, fitness trackers, workout hydration) + home desk 229 → 235 pages (generator sizing, kitchen ants, home-office setup, ceiling vs standing fan, power-cut first hour, bathroom drain flies). Sitemap 3,555 → 3,571 URLs, additions-only (verified pre-push). Related-link maps + section counts wired for all 16.
- **Fitness batch 2 + video-schema fix SHIPPED 2026-09-23** (commit `37dcd50`, LIVE): fitness 55 → 65 pages (10 evidence-anchored guides, fact-checked before writing: ACV honesty, bodybuilding must-knows, downside of stimulants, creatine, protein powder, gym-results timeline, realistic muscle-gain rates, bulking & cutting, beginner splits, testosterone-booster truth). `uploadDate` added to trailer VideoObject on ALL 689 movie pages - fixes GSC "videos missing upload date". Allowlist 2,049 → 2,059.
- **Tier-1 batch 3 SHIPPED 2026-09-23**: fitness 65 → 75 (hydration physiology, electrolytes honesty, ice-bath truth incl. verified post-lift hypertrophy finding, sauna evidence, massage guns vs foam rolling, personal-trainer economics, budget home gym, walking pads, intermittent-fasting boundaries) + home 235 → 243 (2026 solar maths post-tax-credit, HVAC filter sizes & MERV, water-heater flush, dryer-vent fire prevention, smart-device sorting, water-main shutoff, garage-spring safety, gutter guards). Public sitemap 2,059 → 2,077, additions-only verified.
- **Film batch 5 + tier-1 batch 4 SHIPPED 2026-09-23**: film enrichment 100 → 117 titles (the-godfather, the-dark-knight, the-matrix, whiplash, casino-royale, die-hard, coco, toy-story, wall-e, back-to-the-future, alien, the-shining, zodiac, your-name, 3-idiots, dangal, anikulapo). Fitness 75 → 83 (zone 2, pre-workout food, anabolic-window myth, standing desks, rowing machines, dumbbells vs barbells, supplement waste bin, grip strength) + home 243 → 249 (water softeners, DOE-anchored thermostat settings, repair-vs-replace, air purifiers/HEPA, sump pumps, ice dams). Public sitemap 2,077 → 2,091, additions-only verified.
- **Film batch 6 + tier-1 batch 5 SHIPPED 2026-09-23**: film enrichment 117 → 136 titles (akira, alien-romulus, amelie, blade-runner, eternal-sunshine, ex-machina, the-prestige, the-social-network, totoro, forrest-gump, fight-club, gladiator, se7en, andhadhun, tumbbad, a-tribe-called-judah, the-wedding-party, citation, chief-daddy). Fitness 83 → 89 (DOMS relief, gym anxiety, rep ranges via Schoenfeld 2017, deloads, cardio/weights order, protein before bed) + home 249 → 255 (fan direction DOE-verified, washer hoses, attic insulation, frozen pipes, mice signs, window film). Public sitemap 2,091 → 2,103, additions-only verified.
- **Fitness catch-up batch SHIPPED 2026-09-23**: fitness 89 → 101 pages - crossed 100. Twelve guides broadening exercise-type coverage (swimming, cycling, jump rope, kettlebells, Pilates, yoga, HIIT, elliptical) + healthy staples (eight desk stretches, post-workout plate, exercise-and-mood via verified 2026 umbrella review, mobility vs flexibility). HIIT time-efficiency and mood-effect claims verified against meta-analyses before writing. Public sitemap 2,103 → 2,115, additions-only.
- **TOOLS PROGRAMME LAUNCHED 2026-09-23**: tech toolbox grew to 11 tools - new flagship "Internet speed calculator" (/tech/tool/internet-speed-calculator/, client-side, WebApplication schema, links new-router-for-slow-internet + data-usage estimator). Stale 8-tool nav fixed to the full 11. BUILD INCIDENT: first deploy failed twice (~25s, logs sealed) - cause was `import tech_tools_data` inside the shared _nav_items builder (runs during writers build stage); fix = hardcode the tool list in nav (commit 201ba208, live). Rule: keep shared-nav builders import-free - hardcode lists there.
- Next tools candidates (in demand, AI-proof, client-side): device electricity running-cost calculator, video file-size estimator, upload-time calculator, AI subscription cost comparer, password strength checker. Next content: film batch 7, home batch, fitness batch, GSC 50%-indexed checkpoint end-Oct.

Governing principle: the plumbing (SEO, security, speed, monetization rails)
is already excellent. Every upgrade from here is **content depth and
freshness**, desk by desk, weakest first. Each phase ends with one (and only
one) IndexNow ping and a check of the release gates.

## Phase 0 — Hygiene quick wins — ✅ DONE 2026-09-23 (see audit doc for the corrections)

1. **Purge "Moved:" tombstones from `entertainment/sitemap.xml`** — and fix the
   generator (`build-ecosystem.py`) so renamed slugs never re-enter the
   sitemap. Sitemaps list canonical pages only.
2. **Add `datePublished` / `dateModified`** to writers and sports article
   schema (generator + template change, applies desk-wide automatically).
3. **Revive the sports data agent**: add free `FOOTBALL_DATA_API_KEY` as a
   GitHub secret (football-data.org), trigger `sports-update.yml` manually
   once, confirm the 18 thin fixture pages refresh with real tables.
4. Re-run `npm run validate` gates; commit; deploy.
- **Done when**: sitemap has 0 tombstones, writers/sports articles carry dates,
  sports fixtures show current-season data.

## Phase 1 — Entertainment depth program (weeks 1–4) — the flagship

Goal: turn 847 stubs into articles. Median 153 → 600+ words; thin 85% → <5%.

1. **Enrich the data model first** (`content/` JSON feeding
   `build-ecosystem.py`): per-title fields for
   `verdict` (2–3 sentence editorial take), `where_to_watch` (NG first, plus
   US/UK availability), `similar_picks` (3 internal links — fixes the 47/page
   link deficit), `faq` (3 Q&As → `FAQPage` schema).
2. **Extend the movie/TV template** to render those blocks. Because the desk
   is generator-built, one template change upgrades every page at once; the
   per-title text is the real work.
3. **Batch it**: batch 1 = top 100 titles (by demand: current theatrical,
   streamers' hits, anime evergreens — Squid Game/anime slugs already earn
   internal links). Batches of ~100/week → all 847 in ~8 weeks; 300 pages
   improved is enough to move indexing.
4. **Quality bar per page**: ≥600 unique words, 3+ internal links, FAQ block,
   no two pages sharing sentences (the generator makes this auditable — add a
   duplicate-shingle check to `validate-site-quality.js`).
5. After each batch: single IndexNow ping; watch GSC impressions for the desk.
- **Done when**: desk median ≥500 words, thin% <5%, entertainment indexed
  pages climb from near-zero to 50%+ of sitemap.

## Phase 2 — Writers + fitness volume (weeks 2–6, parallel with Phase 1)

1. **Writers venue pages (~40)**: each gets pay rates, submission windows,
   response times, acceptance difficulty, verdict — 500+ words. These are
   money pages for the work publication; highest RPM-per-word on the site.
2. **Fitness desk 45 → ~120 pages**: programmes, equipment guides, calculator
   companions (calculators already exist under ecosystem). Interlink every new
   page from the calculator/tool pages.
3. **Home desk**: add visible "Last updated" stamps + dates in schema; set a
   quarterly review rotation (DIY/YMYL-adjacent trust signal).
- **Done when**: 0 thin venue pages, fitness ≥100 pages, home pages dated.

## Phase 3 — Monetization on-ramp (when you say go)

1. Watch ads.txt flip to **Authorized** (normal window: 2–7 days from 21 Sep).
2. Confirm CMP serves with an EU VPN + fresh Incognito (message was published
   22 Sep).
3. Add the **US state regulations** message in Privacy & messaging.
4. Wire ad units: `_ads_slot()` in `build-ecosystem.py` already exists — place
   after-lede / mid-article / before-footer in clearly labelled containers,
   never resembling job cards (per `docs/ADS.md`). Keep Google auto-ads OFF
   until placements are reviewed.
5. Re-run all release gates + browser validation before enabling.
- **Done when**: ads serve on improved desks only, RPM baseline recorded.

## Phase 4 — Growth & measurement (ongoing)

- **GSC targets**: 50% of 2,033 URLs indexed by end of Oct; 80% by year-end
  (baseline ~300 on 23 Sep). Review weekly, per desk.
- **GA4**: content-group by desk; compare engagement before/after Phase 1
  batches — depth upgrades should lift time-on-page.
- **IndexNow discipline**: one ping per meaningful batch, nothing more.
- **CI**: after next push, check the Actions tab — `quality.yml` must be green
  on every commit; fix any gate it flags before merging further work.
- **Ops note for workspace copies**: the full tree is ~490 MB (public/ alone
  is 156 MB). Keep sandbox/VM copies sparse (`git sparse-checkout`, skip
  `public/ reports/ assets/`) or they truncate and produce false audit
  findings — this bit the 23 Sep audit's first pass.

## Suggested weekly cadence

| Day | Block |
|---|---|
| Mon | Phase-1 batch content (100 titles' data) |
| Tue | Rebuild + gates + deploy + 1 IndexNow ping |
| Wed | Phase-2 (writers venues / fitness) |
| Thu | Sports agent review, dates/schema fixes |
| Fri | GSC/GA4 review, next-batch selection, roadmap tick |

## What NOT to do

- Don't touch CSP, header stack, canonical scheme, or the build order — they
  are verified correct.
- Don't mass-ping IndexNow or resubmit sitemaps repeatedly.
- Don't enable auto-ads or ad units before the CMP is confirmed and placements
  are reviewed against `docs/ADS.md`.
