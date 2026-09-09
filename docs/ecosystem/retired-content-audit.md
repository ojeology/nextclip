# THE BRYME — Retired Content Audit (Entertainment & Sport corpus)

**Audited:** 8 September 2026 · **Source:** full git history of `ojeology/nextclip` (505 commits — the pre-pivot NEXTCLIP platform). All paths below were confirmed present in history; raw article bodies are extracted to `ecosystem/entertainment/_recovered/` (35 files + manifest).

**Rule applied (per master plan §4):** preserve the *value* of the research, not the old URLs. No mass redirects; retired URLs stay retired unless a genuine equivalent exists.

## Inventory

| Corpus | Pages in history | Classification |
|---|---|---|
| `article/*` editorial (film/TV/anime guides, explainers, opinion) | 35 | **A/B/C** — the real research; recovered |
| `articles/*` category hubs | 15 | **D** — thin index pages, superseded |
| `movie/<slug>` catalog pages (se7en, barbie, dunkirk…) | ~140 | **D** — template-generated metadata pages, boilerplate-heavy |
| `anime/*`, `year/*`, `search/*`, `matches/*`, sports data pages | ~340 | **D** — data/boilerplate, stale by definition |
| `assets/img/sports/badges/*`, memes | ~60 files | **D** — not content |
| `/privacy` | present | **E-adjacent** — superseded by new per-publication privacy pages |

## Classification of the 35 editorial articles

**STATUS UPDATE (8 Sep 2026, "bring back the dead parts" pass):** the entire A+B+C set is now restored — **24 archive editions live** on entertainment.thebryme.com (the 6 A-grade + all 12 B-grade + the 5 unique C-grade pieces, including `one-piece-vs-naruto` and both Prison Break essays). The two superseded duplicates stay merged into their newer editions. The 9 D-grade pieces below stay retired on merit; they are listed, with word counts, in the "reviewed — retired" section of the entertainment index.

- **A — Rebuild (recovered now, 6):** `korean-cinema-starter-guide-rebuilt`, `christopher-nolan-movies-order`, `nigerian-thrillers-worth-your-time`, `indian-cinema-first-five`, `modern-horror-starter-route`, `how-to-pick-a-movie-tonight` — evergreen, evergreen-framed, low legal surface. Live on entertainment.thebryme.com as the *recovered shelf*, re-typeset, honestly labelled "archive edition".
- **B — Update and rebuild (12) — RESTORED 8 Sep 2026:** the strong service/fandom pieces with time-sensitive hooks — `squid-game-season-1-…phenomenon`, `alice-in-borderland-vs-squid-game`, `solo-leveling-*` (3), `one-piece-vs-naruto`, `was-eren-yeager-really-the-villain`, `into-the-badlands-…`, `breaking-bad-two-seasons-opinion`, `prison-break-*` (2), `10-anime-like-solo-leveling`, `10-shows-like-alice-in-borderland`. Bodies recovered; rebuild when the Entertainment desk opens properly (refresh facts/season status first).
- **C — Consolidate (4–5) — restored individually 8 Sep 2026; the Interstellar pair uses the longer guide edition:** the "movies-like" cluster — `movies-like-interstellar` + `movies-like-interstellar-guide` (duplicates), `movies-like-parasite`, `movies-like-deadpool-and-wolverine`, `5-movies-that-broke-the-internet` + `7-movies-we-wished-never-ended` (listicle overlap). Merge into one "If you liked X" format per title family.
- **D — Do not migrate (13):** `beginners-guide-to-making-money-online` (off-niche for Entertainment + stale advice), `10-facts-about-agent-kim-squid-game-season-3` (thin, dated), `10-korean-movies-everyone-should-watch` (overlaps the A-grade starter guide), `5-vampire-movies-that-changed-horror` (overlaps `modern-horror-starter-route`), `dune-sci-fi-epics-guide`, `why-dune-part-two-feels-large`, `interstellar-ending-explained`, `alien-franchise-in-order`, `best-anime-to-watch-now` (time-anchored), and all `articles/*` category pages.
- **E — Redirect:** none. No old entertainment URL maps 1:1 to a new one (slugs change, site is a fresh subdomain); manufacturing redirects to a homepage is forbidden by §4.

## Sport corpus

The historical `sports/` section (157 pages) is **match/data pages and badge assets** — structurally stale, classified D. No recoverable editorial prose was found. BRYME Sport therefore launches on *new* reporting (scope: analysis, explainers, stories; **hard rule: no betting content**), with prioritisation awaiting the user's Bing/GSC export (the football/PL/transfer impressions data referenced in the plan).

## Legal surface check

Historical movie catalog pages contained incidental "watch" text but **no download infrastructure**. The new Entertainment property is information-only by construction (see its index promise), satisfying the plan's hard rule.


## 2026-09-09 — ecosystem map revision + Tech archive recovery

- **Money property removed** (spec order): /money/ (7 pages: index, 3 foundation essays, 3 legal)
  pulled from build, config, nav, sitemaps, robots. No redirects mass-created; research data
  files stay unpublished in content/. Business: never existed; confirmed absent.
- **Old BRYME Tech recovered** from content/tech-articles.json (17 published articles, Aug 2026,
  author Ibrahim Sodiq, named sources): all 17 RESTORED verbatim-in-content, re-typeset in the
  current shell with honest published/updated dates, sources lists and TechArticle schema.
  Classification: 17 RESTORE, 0 RETIRE (the archive was strong).
- **Old tech IA retired**: 18 thin category hub pages from the old tech site replaced by 4
  earned sections (/tech/ai/, /tech/tools/, /tech/web-and-hosting/, /tech/safety/); coding
  waits at 1 article (no hub page until it earns one). best-streaming-apps-nigeria: MOVE
  candidate to Entertainment at its build.
- **Foundations added**: /fitness/ and /home/ — one honest plan page + standard legal each,
  all noindex,follow, no sitemap entries, no fake content.

## 2026-09-09 — Phase 2: Entertainment rebuilt as a publication

- **Identity live:** «What should I watch — and why?» Homepage rebuilt around it; archive-era
  "recovered shelf" framing replaced with a real desk: 3 earned sections —
  /entertainment/recommendations/ (12), /entertainment/explainers/ (6), /entertainment/opinion/ (5).
- **CONSOLIDATE (2):** solo-leveling-from-e-rank-hunter-… merged into solo-leveling-e-rank-to-s-rank;
  prison-break-season-1-watching-all-night merged into why-prison-break-season-1-is-still-one-of-
  the-best-tv-seasons — each as a labelled "Companion piece, restored" section. Old URLs retired
  (archive era, noindex history; no mass redirects).
- **MOVE (1):** best-streaming-apps-nigeria moved from the old tech desk to Entertainment
  recommendations — it is a watch-guide, not tech support. Dead link to a retired sports route
  repointed at /sports/; its own price-caveat table preserved ("estimates as of August 2026 —
  confirm on official pages").
- **Article template:** section breadcrumbs, honest byline (word count + re-typeset/reviewed date),
  "In one line" summary bar, Article schema (author/publisher/dates), related links per section.
- **RETIRE (stays):** the 29-row seo-pilot-matrix data-page set (cast/trailer/where-to-watch
  fixtures) remains retired — exactly the format §21 forbids rebuilding as substance. The 9
  audited-out stubs stay retired and are listed transparently on /entertainment/.
- Entertainment now 30 pages (index + 3 sections + 23 articles + legal). build-ecosystem's
  write_service now clears stale output per property (recovery store preserved).

## 2026-09-09 — Phase 3: Fitness foundation → publication

- **Identity live:** «Build a routine you can actually keep» — beginner-first, evidence-aware,
  no-miracle framing; desk rules on the homepage; general-information-not-medical-advice band
  on every guide and the plan.
- **Content (6 pages + legal, each earning its route):** 4 sourced guides — starting from zero,
  step counts (10k marketing origin; Lee et al. 2019 JAMA Intern Med framing stated with its
  caveats), beginner strength (six patterns, guideline 2+/week), rest & recovery (DOMS handled
  honestly) — plus the flagship **30-Day Walking Plan**: 30 real day entries (time-based,
  rest day every 7th), responsible wording, no body-transformation promises.
- **Product:** the plan page tracks completion locally (assets/fitness-plan.js, ES5, CSP-safe,
  localStorage only, no account, nothing transmitted); all 30 days render as content for no-JS
  visitors; progress bar + status line for JS users.
- **Foundations replaced:** the noindex placeholder is gone; fitness is indexable, sitemap'd
  (allowlist v26, 568 routes), in robots (5 sitemaps), and on the home placeholder's live-desk list.
- Source URLs: WHO physical-activity fact sheet, CDC Physical Activity Basics, JAMA Intern Med
  2019 (Lee et al.). Reviewed date on every page: 2026-09-09.

## 2026-09-09 — Tech focus begins: UPDATE pass (batch 1)

- **Verified current (9 Sept 2026):** ChatGPT Free/Go $8/Plus $20, Pro structure now documented
  ($100 + $200 tier); Google AI Plus $4.99 / Pro $19.99; Claude Pro $20 ($17 annual), Max $100+;
  Bitwarden Premium $1.65 / Families $3.99 — all recovered-article figures still hold.
- **UPDATE applied:** chatgpt-claude-alternatives — the Pro-tier ambiguity is resolved in-text
  ($100/$200 now documented); gemini-vs-chatgpt, deepseek-vs-chatgpt, arena-ai-vs-chatgpt,
  ai-assistant-data-training-settings, bitwarden-free-password-manager — re-verified notes +
  updatedAt 2026-09-09. Notion/other pieces keep their own explicit checked-dates by design.
- **Sport archive stamp:** the 4 season-window editions (transfer tracker, both matchweek
  previews, deadline-day) now carry "Season 2026-27 · archive edition" + a byline note that
  new editions return with the season — time-sensitive coverage no longer reads as current.

## 2026-09-09 — Tech batch 2: 14 original guides, three new sections

- **Sections earned and opened:** /tech/android/ (4), /tech/windows/ (3), /tech/coding/ (4 incl.
  the Termux archive piece). Tech homepage now seven sections; obsolete coding-note removed.
- **Safety 3→7:** suspicious links (FTC source), 2FA done right (CISA source), public Wi-Fi
  (myth-correcting: HTTPS fixed the old threat; evil twins/captive portals/humans remain),
  password manager vs browser vault.
- **Android:** storage triage, permission audit, battery health (charging myths retired),
  notification control. **Windows/PC:** slow-PC triage, browser fix list, stuck-update path.
  **Coding:** error messages, Git/GitHub (Pro Git + GitHub docs sources), what is an API.
- Kicker honesty system: First-hand / Practical guide / Archive edition by provenance.
