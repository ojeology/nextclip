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

## SEO AUDIT COMPLETE (2026-09-23)

- Brief executed end-to-end; final report delivered to owner (bryme-seo-audit-report.md in agent workspace).
- SHIPPED commit 5f938302: real per-URL sitemap lastmods (writers post-build step scripts/fix-writers-lastmod.py wired into npm run build AFTER build-public-dir; desk sitemaps per-URL in build-ecosystem; index = per-child max). URL sets byte-identical; no IndexNow (lastmod-only).
- Verified live post-Cloudflare-cache: writers 509 URLs / 5 distinct real dates. Phase 1 PASS + Phase 2 PASS; no keyword/template fixes needed (titles already intent-specific).
- Open owner decisions: GSC sitemap resubmit (optional), Consent Mode v2 via Google Privacy & Messaging (not installed per constraint), img width attrs + dates on 109 legacy writers templates (future template tweaks).
- NOTE: git origin for the site repo is github.com/ojeology/nextclip.git (historical name) — it IS the live thebryme.com repo; Render auto-deploys pushes to main.

## BANDWIDTH FIX (2026-09-23)

- Render emailed owner: 70% of free bandwidth used. CAUSE: Render April-2026 repricing cut Hobby free allowance 100GB -> 5GB/month (forced migration Aug 1 2026); allowance is workspace-wide (Bryme + Bryme-backend + createit share it); AI training bots + recrawl surge burn it. At 100% with no card: services disabled until next month.
- SHIPPED fae6b032: robots.txt blocks GPTBot, Google-Extended, CCBot, Applebot-Extended, Meta-ExternalAgent, Amazonbot, Bytespider (owner chose to keep PerplexityBot/ClaudeBot). Verified live. URL sets identical.
- PENDING owner actions: Cloudflare toggles (Tiered Cache; optional AI-scrapers block) + possible Cloudflare Pages migration (unlimited bandwidth, USD 0) — explained, awaiting decision. DO NOT add payment card to Render.
- LESSON: workspace snapshots do not keep .git — re-clone at turn start for any git work; never git stash in disposable clones (stash ate generated files once).

## TOOL 12: ELECTRICITY COST CALCULATOR (2026-09-23)

- SHIPPED 47b85fab34, LIVE & verified (page 200, JS 200, hub "12 free browser tools", tech sitemap 293, IndexNow 200).
- TIER-1 FOCUS per owner: defaults US ~18.4c/kWh (EIA Sep 2026), UK 26.11p (Ofgem cap Jul-Sep 2026), CA C\$0.14, AU A\$0.33; custom rate field wins; appliance presets (heater 1500W, AC, dryer 3000W, EV L2 7200W, etc.); costs per hour/day/month/year. No Nigeria preset (owner targets Tier 1).
- Pattern notes: (1) tech desk ships as COMMITTED ARTIFACTS - run scripts/build-ecosystem.py manually, then npm run build, then commit; (2) title_budget.py caps SERP titles at 60 chars - keep <title> keyword-first <=46 chars incl " | BRYME Tools"; long title survives as H1; (3) tools.json is writers-only, tech tools do not touch it.
- Typo debt CLEARED: kettlebell ballswing x2 + bow-arrow, deload "the lifer", desk-stretches "a upper back".
- Next-tool candidates remain: video file-size estimator, upload-time calculator, AI subscription cost comparer, password strength checker (all Tier-1 angles first).

## HOME BATCH 19 (2026-09-23)

- SHIPPED: 6 new tier-1 guides (caulk-vs-grout, lawn-mower, wasp-nest, pressure-washer, dishwasher-drain, baby-proofing). LESSON: 5 originally-planned topics ALREADY EXISTED (dryer-vent-cleaning-fire-risk, water-heater-flush-how-to, smart-thermostat-payback, garage-door-spring-safety, fridge-not-cooling) - ALWAYS curl live /home/<slug>/ before writing a batch. New home-batch wiring = 3 registries: HOME_SLUG_SECT + related_map (KeyError if missing!) + import/extend.

## CONTENT BATCHES: FIT-8 GLP-1 CLUSTER + HOME-20 ENERGY CLUSTER (2026-09-23)

- Fitness batch 8 (4): muscle-on-glp1-weight-loss-drugs, protein-when-appetite-is-gone, strength-training-while-losing-weight, keeping-weight-off-after-glp1. Sources: trial lean-mass ~25-40% hedged, protein >1.2-1.6 g/kg/day distributed, RT 2-3x/wk, S-LiTE, 2026 Fitbit study. Prescriber-leads framing.
- Home batch 20 (5): why-is-my-electric-bill-so-high, appliances-that-use-the-most-electricity, is-it-cheaper-to-heat-one-room, second-fridge-freezer-cost, off-peak-electricity-tariffs-explained. Cross-desk absolute tool links verified.
- GATE LESSONS: (1) href gate catches wrong-slug body links - it stopped smart-thermostat-worth-it + refrigerator-not-cooling-first-checks (real pages: smart-thermostat-payback, fridge-not-cooling); fitness articles get shared FIT_SOURCES external footer (WHO/CDC) - whitelist externals; (2) wiring fitness = extend + ART_SOURCES + related_map per slug (KeyError otherwise); home = extend + HOME_SLUG_SECT + related_map.

## TOOL 13: AI SUBSCRIPTION COST COMPARER (2026-09-23)

- SHIPPED & LIVE: /tech/tool/ai-subscription-cost-comparer/ (JS assets/tool-ai-subs.js). Defaults verified Sept-2026: ChatGPT Plus 20, Claude Pro 20, Google AI Pro 19.99, Perplexity Pro 20, Copilot Pro 20, SuperGrok 30, Midjourney 10. All editable; custom row; months 1-12; biggest-line-first + cancel-the-overlap hint.
- Same-day triple ship: fitness GLP-1 cluster (4) + home energy cluster (5) + this tool. Roadmap next: video file-size estimator, upload-time calculator, password strength checker.

## TOOLS 14-15: VIDEO FILE SIZE + UPLOAD TIME (2026-09-23)

- SHIPPED & LIVE: /tech/tool/video-file-size-estimator/ (assets/tool-filesize.js) + /tech/tool/upload-time-calculator/ (assets/tool-uploadtime.js). Bitrate table: 4K 40 / 1440p 20 / 1080p 10 / 720p 5 / 480p 2.5 Mbps @30fps H.264; fps x0.85/x1/x1.7; codec x1/x0.55/x0.45; audio 0.128/0.256/0.448. Upload: +15% real-world line, GB/hour translation. Hub + nav at 15.
- Same-day total: tools 12-15, fitness batch 8 (4), home batches 19-20 (11). Remaining roadmap: password strength checker, then fitness/home batches, film batch 7, GSC checkpoint end-Oct.

## BATCHES 21 HOME + 9 FITNESS: THE GEM ROUNDS (2026-09-23)

- Home batch 21 (9): cost-to-run series {dehumidifier, dryer, AC, EV, hot tub, dishwasher, fan, gaming PC} + heat-pump-vs-gas-furnace. All link the calculator (absolute URLs); related_map cross-links the cluster.
- Fitness batch 9 (11): GLP-1 plan, over-50 strength, loose skin + is-it-normal x8 {2-day sore, not-sore-anymore, plank shake, heart pounding, first-week scale, sleepy workouts, joint cracking, day-after hunger}. Red-flag lists lead to professionals; no medical advice.
- Strategy note: these implement the 5-bet brainstorm (cost-to-run series, GLP-1 expansion, is-it-normal pipeline, heat-pump CPC page). UK winter boiler/radiator cluster NOT yet written - next content batch. GSC export still pending from owner.

## OVERNIGHT: TOOL 16 + UK WINTER CLUSTER (2026-09-23 night)

- Password strength checker LIVE (/tech/tool/password-strength-checker/, assets/tool-password.js) - toolbox roadmap COMPLETE (16 tools).
- Home batch 22 LIVE (6): boiler-pressure, radiators-cold, pipe-lagging, EPC, storage-heaters, condensate-pipe - shipped early, indexed before the wave.
- LESSONS: (1) multi-line patch anchors must match actual file wrapping; (2) phantom-slug pattern - drafts default to "worth-it" endings; real pages end -payback / -explained. Href gate caught it twice; keep trusting the gate.
- Remaining: film batch 7, GSC checkpoint end-Oct, Bing parked (owner), Cloudflare parked.

## FILM BATCH 7 (2026-09-24)

- SHIPPED: 30 titles enriched (verdict+FAQ), ENRICH 136 -> 166. Facts cross-checked against entertainment_platform_data records (annihilation 115, barry-lyndon 181, battle-royale 113, before-sunrise 97 - data file corrected memory). Awards stated only where certain. URL sets unchanged.
- Pool remaining: ~553 unenriched titles.

## FILM BATCH 8 (2026-09-24)

- SHIPPED: 30 more titles, ENRICH 166 -> 196 (719 total; ~27% enriched). Mix: Hollywood classics, Ghibli, shonen/seinen, K-dramas, prestige TV, Bollywood/Telugu, Nollywood. Same fact rules.
- Pool remaining: ~523.

## FILM BATCH 9 (2026-09-24)

- SHIPPED: 30 more, ENRICH 196 -> 226 (719 total; ~31% enriched). Kurosawa pair, Star Wars core, superhero pillars, horror canon (Conjuring/Exorcist/Halloween/Thing/Midsommar), anime (JJK/Demon Slayer/Howl/Fireflies/Bebop), Drishyam identified as Malayalam original, GoT/Chernobyl/Wire, Bong Host.
- Pool remaining: ~493.

## FILM BATCH 10 (2026-09-24)

- SHIPPED: 30 more, ENRICH 226 -> 256 (719 total; ~36% enriched). Family animation 8, action staples 8, sci-fi 6, superhero 4, prestige 4.
- Pool remaining: ~463.

## FILM BATCH 11 (2026-09-24)

- SHIPPED: 30 more, ENRICH 256 -> 286 (719 total; ~40% enriched). Kubrick cult pair, beloved classics, mega-TV (Friends/Sopranos/BCS/Black Mirror/Dark), anime (DBZ/Frieren/Chainsaw Man), Korean pair, Bollywood giants, Nollywood 93 Days. Batch-10 Finding Nemo typo fixed same commit.
- Pool remaining: ~433.

## FILM BATCH 12 (2026-09-24)

- SHIPPED: 30 more, ENRICH 286 -> 316 (719 total; ~44% enriched). TV giants (Office/Downton/Vikings/TWD/Witcher/Wednesday/Yellowjackets), MCU backfill 4 + Penguin, Eggers pair + Ring + Us, 28 Years Later, comedy trio, world-cinema masters (Ozu/Hamaguchi/Intouchables/Bittersweet), Tamil/Hindi trio, anime pair, Gangs of Lagos.
- Pool remaining: ~403.

## FILM BATCH 13 (2026-09-24)

- SHIPPED: 30 more, ENRICH 316 -> 346 (719 total; ~48% enriched). Oscar winners (Anora/Shape of Water/Zone of Interest/Lives of Others/Departures/Holdovers), K-cinema deep cuts (Burning/Decision to Leave/Man from Nowhere/Extreme Job), auteurs (Aftersun/Florida Project/Green Knight/Farewell), action backfill (Con Air/Face-Off/Transporter/Equalizer/Creed), India pair, Nollywood landmark The Figurine. NOTE: the-big-lebowski not in MOVIES pool - checked before authoring.
- Pool remaining: ~373.

## FILM BATCH 14 (2026-09-24) - 50% MILESTONE

- SHIPPED: 30 more, ENRICH 346 -> 376 (719 total; ~52% enriched - MAJORITY of movie desk now editorial). HBO pair (Euphoria/Agatha), The Boys spinoff Gen V, Fallout, Arcane S2 finale, anime 6 (Dandadan/Blue Lock/Black Clover/Code Geass/Toradora + WWDITS film), MCU/DC backfill 5, prestige pair (Road/Deep Water), Gorge/Atomic Blonde, comedy 4, Nollywood trio (Blood Sisters/Set Up/Eyimofe), Wandering Earth.
- Pool remaining: ~343.

## RELATED-LINKS UPGRADE (2026-09-24)

- SHIPPED: movie pages "More like this" 3 -> 6 same-genre links, nearest-era deterministic order. ~2,150 extra internal links; whole vertical re-pinged via IndexNow. URL sets unchanged. Full enrichment schema audit clean: 376/376 FAQPage JSON-LD valid with exact question counts.

## FUTURE-DATE FIX (2026-09-24)

- SHIPPED: 14 Nollywood review pages carried future dates (2026-09-25..30) leaking into JSON-LD, visible text, section sitemaps and root sitemapindex. Engines distrust future lastmod - plausible contributor to Bing discovery stall (981). Clamped at emit: review datePublished, visible Reviewed-on, defensive sitemap clamp. Verified live: entertainment index lastmod now build-day, 0 future dates anywhere.
- Re-ship lesson reinforced: ALWAYS fresh clone (stale clone lost content/ -> build fail; caught and re-cloned).

## FILM BATCH 15 (2026-09-24)

- SHIPPED: 30 more, ENRICH 376 -> 406 (719 total; ~56% enriched). Prestige TV 6 (Andor/Last Kingdom/White Lotus/Fargo/Sandman/Umbrella Academy), MCU TV+film 5, classics (Carrie/Ghostbusters-1984/Willow/Labyrinth/Alien Resurrection), 2024-25 tentpoles (Twisters/Mario/Zootopia 2/Conclave), anime arc 8 incl. both Demon Slayer films, K-drama The Glory, Vikram Vedha.
- Pool remaining: ~313.

## FILM BATCH 16 (2026-09-24)

- SHIPPED: 30 more, ENRICH 406 -> 436 (719 total; ~61% enriched). TV giants 6 (HotD/Succession/Severance/Peaky/Sherlock/Money Heist), anime 7 (MHA/OPM/SpyXFamily/HxH/Steins;Gate/Fairy Tail/DBS), 2025-26 thrillers (Housemaid/Bone Temple/Dhurandhar), Bollywood 8, Nollywood 4, Chinese 2, Fifty Shades/Freakier Friday. squid-game found already enriched; westworld not in pool - both dodged pre-write.
- Pool remaining: ~283.

## MONEY DESK LAUNCH (2026-09-24)

- SHIPPED: /money/ - 7th section live. Hub + position-size calculator + position-sizing-101 + legal set (10 URLs). Risk-first policy walls: never advice, no profit claims, no signals, no betting. E-E-A-T via open research links (QUANTLAB, mean-reversion-vwap-lab).
- Plumbing (7 builders touched): ecosystem (FAMILY/PUB_NAME/PREFIX/editions/drawer/nav/money_pages), routing (PROPS + SITEMAP_PROPS + allowlist missing-file guard + children), discovery (robots), public-dir (2 staging lists), purge-stale (prop loop), inject-analytics (PUBLISH_TIERS).
- Lessons: (1) inserting a top-level def mid-function swallowed the main-flow calls - IndentationError caught the dedent, def moved above main(); (2) KEEP_AT_ROOT_DIRS = set(PROPS) - the SECOND registry (PROPS, not just SITEMAP_PROPS) gates whether builds delete a new root dir; (3) routing aborts on manually-rerun trees but runs fully inside npm build.
- Next for money: pip/compounding/risk-reward calculators, research notes from GitHub repos.
