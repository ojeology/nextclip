# BRYME Sport — Football Hub Rebuild: Phase-1 Audit & Gap Matrix

**Spec:** `docs/ecosystem/bryme-sport-football-hub-rebuild-spec.md` (51 sections, target 9.5–10/10).
**Date:** 11 September 2026. **Method:** every section mapped against the live implementation (batches 1–13), the retired Sport backend recovered in Batch 8 (`ecosystem/sports/_recovered/`, old branch `agent-work-2026-09-03`), and live probes of the football-data.org v4 API. Classification per spec §42: KEEP / IMPROVE / MERGE / REDIRECT / NOINDEX / DELETE already applied in Batch 8; this audit extends it to the new spec's demands.

## What already exists and satisfies the spec (KEEP/IMPROVE)

| Spec § | Requirement | Status | Evidence |
|---|---|---|---|
| 2 | Six permanent competition hubs | **DONE** | `/sports/<hub>/` ×6 (PL, LaLiga, Serie A, Bundesliga, Ligue 1, UCL), flat URLs (router collapses nested sports paths — the standing constraint; §8's "or equivalent clean URL architecture" is met) |
| 3 | Hub shows table first + clear nav | **DONE** | Every hub opens on the live table module/rows; nav shelf links Table/Scorers/Fixtures/Results/Clubs/Explainers |
| 4 | Top scorers per competition | **DONE + IMPROVED b13** | `/sports/<lg>-top-scorers/` ×6; now carries appearances + assists as published |
| 6 | Fixtures & results permanent pages | **DONE** | `/<lg>-fixtures/` (full-season calendars, 5 leagues) + `/<lg>-results/` (last 3 MWs, 6 comps) + `/<lg>-table/` ×6 |
| 7 | Matchweek system | **PARTIAL** | MW4 live preview + MW1–3 archive editions + weekend-forecast page. Awards/TOTW pieces not yet built (editorial, next phases) |
| 8–9 | Club hubs with identity | **DONE + IMPROVED b13** | 20 PL club hubs: badge, ground, founded, city (sourced), position/pts/GD/record, next fixture, story links. b13 adds API-verified squads |
| 10 | Squad section | **NEW b13** | `/sports/clubs/<club>/` renders the API squad grouped GK/DF/MF/FW with nationality + age-at-listing + shirt numbers; stamped with fetch time; 19/20 clubs on day one (absent-safe) |
| 11 | Player pages | **NOT BUILT (deliberate)** | Free API exposes no per-player season stats endpoint; spec forbids thin pages — deferred until a reliable source exists |
| 14 | Club fixtures/results/form | **PARTIAL** | Next fixture + record on every club hub; full per-club fixture lists deferred (URL-explosion guard §43) |
| 15 | Club latest stories | **DONE** | Story links wired per club (archive pieces) |
| 16 | Same architecture for all six | **LARGELY DONE** | UCL adapted to its real format (36-team league phase, matchdays not matchweeks, no relegation line) — spec's own example honoured |
| 17–18 | Reuse existing API integration; cache/snapshot architecture | **DONE** | Single server-side agent → `content/sports-live.json` snapshot → static build; graceful failure; stale-but-sourced beats fresh-but-guessed |
| 19, 41–42 | Old-hub recovery & classification | **DONE (Batch 8)** | Fixtures calendars (1,452 matches), club identities, 96 badges + 5 league SVG sets recovered; 44 MB junk pruned with receipts; slug bridges + assertions |
| 20 | Logos/assets | **DONE** | Existing badge sets (owner-sanctioned recovery); API crests not needed |
| 27 | Sport homepage architecture | **DONE + IMPROVED b13** | Portal: live hero, This-weekend strip, live data module, BIG SIX quick-nav (b13), deep league list, archive, explainers |
| 28, 51 | Evergreen knowledge library | **PARTIAL (~10 pieces)** | Offside, promotion/relegation, table mechanics, xG, pressing, VAR-adjacent pieces, UCL format, FPL, AFCON calendar. Spec lists ~70 more topics — scale-up batches planned (researched, not generated) |
| 32–34 | SEO architecture, indexing strategy, internal linking | **DONE** | Permanent flat URLs; routed allowlist v26 (873 routes); link checker 93k+ links green; dead-end-free journeys verified in QA needles |
| 35–36 | Sport-specific UX; mobile-first | **DONE** | Tables/panels/fixture rows; `.data-cols` stacks <900px; house standard kept |
| 37 | Freshness stamps | **DONE** | Every dynamic page carries its `*_updated` string |
| 38 | Sources & trust | **DONE** | football-data.org v4 named on every data page; club facts link official histories; no fake citations |
| 39–40 | AdSense safety; no placeholder | **DONE** | No odds/betting anywhere; forecasts labelled "BRYME forecast, not a tip" |
| 43 | No URL explosion | **ENFORCED** | 883 pages total; one URL per data page per league; validator gates |
| 45 | Tools (optional) | **DEFERRED** | Only after core architecture 100% (spec: build only what genuinely helps) |
| 46 | Performance | **DONE** | Static build, zero client-side API calls, lazy images |

## What changed in Batch 13 (this audit's build slice)

1. **SECURITY (spec §47 — the spec's hardest requirement):** the football-data.org token is no longer hard-coded anywhere in the repo. The agent now reads `FOOTBALL_DATA_API_KEY` (env / GitHub Actions secret) or the untracked dev keyfile `content/.football-data-key` (gitignored); no key ⇒ run exits and keeps the last snapshot (tested). The workflow passes `${{ secrets.FOOTBALL_DATA_API_KEY }}`. **Note:** the old token remains in git history — it must be regenerated on football-data.org and added as the repository secret (owner action; without it the twice-daily cron runs keyless and the data pages hold their last verified state, by design).
2. **Squads live:** agent fetches all 20 PL club squads (`/v4/teams/{id}`: 19/20 on first run — one transient SSL failure, absent-safe by design); club hubs render them grouped by position.
3. **Assists + appearances:** scorers pages show apps and assists exactly as the source publishes them (em dash when unpublished — never a zero by invention). No standalone assists leaderboards: **the free API has no assists endpoint**, so per spec §5 they are not fabricated; the honest note is on every scorers page.
4. **BIG SIX quick-nav** on `/sports/` (spec §27): six panels × Table/Fixtures/Results/Scorers (+Clubs).

## Honest "not available from the source" list (spec §5/§13/§38 compliance)

- **Assists leaderboard** — no API endpoint; only assists of the top-10 scorers are published. Not fabricated.
- **Manager/coach data** — the API `coach` field returns empty; managers now come from the owner-verified trackers (dated) on all 20 PL club hubs.
- **Injuries & suspensions** — no API coverage; per §13 nothing is invented. Not built.
- **Transfers** — RESOLVED: owner-verified trackers recovered from the retired branch and published (see CORRECTION below). Rumours stay unlisted.
- **Per-player season stats** — not in the free tier; player pages stay unbuilt (§11 anti-thin rule).

## Remaining phase plan (spec §48 order)

- **Phase 3 completion:** trophy cabinets + manager lines for 20 clubs (researched, cited, dated — one curated data file, build-verified); per-club fixtures sections (compact, from existing calendars); then extend the club architecture toward the other five competitions (LaLiga clubs next).
- **Phase 4:** matchweek awards pieces (BRYME-labelled, never "official").
- **Phase 5–6:** homepage "Big football questions" feature slots once the six locked living articles exist.
- **Phase 6:** the six locked living features (Ballon d'Or 2026, Ronaldo 1,000-goal tracker, PL title race, world's best players, UCL 2026/27 prediction, World Cup 2026 legacy) — each a researched, dated, update-in-place page. Scheduled next batches; every figure sourced.
- **Phase 7:** evergreen scale-up (~70 listed topics, prioritised by search value: records/milestones as living pages, CL format family, transfer-market rules, PSR/FFP family).
- **Phase 8–10:** news/analysis labels audit; SEO re-check; mobile/perf QA rerun.
- **International (§30):** after the six are unquestionably strong.

## CORRECTION (11 Sep 2026, later): §19 deep inspection was incomplete — now done

The first version of this audit claimed Batch 8 discharged the old-hub inspection. Against the new spec's wider §19 checklist that was wrong: **transfer data and manager data existed on the retired branch and were not recovered.** Found by file-level inspection of `origin/agent-work-2026-09-03` (4,318 files):

| §19 item | Found on old branch | Classification → action taken |
|---|---|---|
| Transfer information | `content/pl-transfers.json` (owner-supplied 13 Aug, updated 2 Sep: 20 clubs, 99 in / 83 out, strict statuses Confirmed/Loan/Free/Released/Departed/Retired, fee details, sources, rumours quarantined) + `content/league-transfers.json` (4 leagues, 120 in / 91 out, dated 13 Aug, compositionVerified) | **KEEP+IMPROVE → RECOVERED & PUBLISHED.** Five permanent pages: `/sports/premier-league-transfers/`, `/sports/{la-liga,serie-a,bundesliga,ligue-1}-transfers/` — statuses only, rumours never listed, mid-window dating note stated plainly on the four pre-deadline trackers |
| Manager information | `manager` + `managerNote` per club in both trackers | **KEEP → PUBLISHED.** Manager cell on all 20 PL club hubs + manager line per club on transfer pages, dated by tracker |
| Trophies | no files (0 hits) | nothing to recover — will be built from cited research, not invented |
| Stadium data | no dedicated files; ground names already live on club hubs from Batch 8 recovery | KEEP as-is |
| Player info | edition pages only (`players-to-watch…`, FPL gameweek page) — thin, dated editions | NOINDEX/retire (not resurrected); player pages remain gated on a real stats source (§11) |
| Injuries | one edition page (`injuries-matchweek-1`) | retire; no data source ⇒ §13 honoured, nothing invented |
| Old transfer HUB pages (5 league pages + hub) | presentation shells around the same JSON | MERGED into the new permanent pages (better layout + honesty notes) |
| Existing API code / DB | `server/` (express bot/backend), `data/*.json` (movie/entertainment domain, not sport) | DELETE-superseded (static build replaced it; non-sport data out of scope) |
| Assets | comics/hero art pruned in Batch 8 with receipts (recoverable on branch) | unchanged |

**Process note:** this correction exists because the audit-first rule was applied to the OLD spec's scope, not the new file's. The missing inspection is now done and every item above is classified per §42.
