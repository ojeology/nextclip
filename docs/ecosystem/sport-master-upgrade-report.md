# BRYME Sport master upgrade — final report (spec compliance), 2026-09-10

Executed in batches 3–7 against the "9.5/10 master upgrade specification". This report follows the spec's §40 structure.

## COMPLETED
- **Permanent competition architecture (§4–6):** `/sports/premier-league/` hub; permanent table at `/sports/premier-league/table/`; permanent fixtures area at `/sports/premier-league/fixtures/`; the LaLiga desk, the Champions League shelf, and new Serie A / Bundesliga / Ligue 1 hubs complete the six-competition structure, all presented in a competition grid on the Sport homepage (§26).
- **Club hub system (§9):** `/sports/clubs/<club>/` ×20 — every correct 2026-27 Premier League club (verified membership; Hull City, Coventry City, Sunderland promoted; Burnley/West Ham/Wolves correctly absent), each with position, points, goal difference, W-D-L, ground, foundation year, an identity paragraph, next fixture, and gateway links. Plus `/sports/premier-league/clubs/` index.
- **Matchweek system (§8):** MW4 live desk edition (results-preview pattern with fixtures, table context, storylines, explicit unknowns, editorial labelling, no invented awards); archive MW1/MW2 editions retained as published.
- **Football Explained expansion (§14/§19):** now 13 explainers — new: how-the-Premier-League-table-works (points/GD/goals-scored/playoff order, no head-to-head), how-do-football-clubs-make-money (three engines + player trading + FFP frame, no invented figures), what-is-a-release-clause (mechanism, Spain vs England). Existing: offside, promotion/relegation, VAR, xG, pressing, playing-out, transfers-collapse, sporting director, shirt numbers, AFCON, LaLiga, El Clásico.
- **Editorial layer (§12/§13):** content typed across NEWS (archive editions) / ANALYSIS / EXPLAINER, editorial selections labelled, predictions never presented as fact, unknowns stated.
- **Data-integrity system (§23):** league data isolated in `scripts/sports_leagues_data.py` with a written data policy; every published table/fixture carries a last-verified stamp and named sources; unverified data published as an explicit "honest gap" instead of guessed numbers.
- **Gateway model (§20/§28):** every new page links onward — table→clubs, clubs→fixtures/table/hub, hubs→explainers, explainers→competitions. Sports mega nav rebuilt around the model (hub/table/fixtures/clubs live items; Serie A/Bundesliga/Ligue 1 in the Desks menu).
- **Mobile-first (§25):** table renders in a horizontally scrollable card with tabular numerals; fixture rows wrap; all pages inherit the Writers header system with dark mode and drawer.
- **Not broken (§34):** all pre-existing routes live; the editorial desk `/sports/epl/` kept alongside the new `/sports/premier-league/` hub (desk = editorial archive, hub = data gateway — cross-linked, no duplication).

## RECOVERED FROM OLD SPORT (§2/§35 audit verdicts)
- **KEEP (already live):** 6 substantial recovered pieces (266–576 words): transfer tracker, MW2 preview, MW1 guide, deadline-day guide, Elliot Anderson/Man City, plus the desk-articles structure that powers the archive desk.
- **RETIRED (permanent):** 15 recovered stubs at 53–60 words each (banter table, "five things" lists, 54-word season previews) — too thin to improve without total rewrite; republishing them would violate §3 and the AdSense/AI policy. Recorded here as the written second-chance audit.
- **Not present in the old implementation:** club logos, fixtures datasets, tables, results feeds — so §10 resolves to: no logo reuse exists; the publication stays text-first and scrapes nothing.

## NEW CONTENT CREATED
Premier League hub, table, fixtures, clubs index; 20 club hubs; 3 competition hubs (Serie A, Bundesliga, Ligue 1); 3 evergreen explainers. Net: **+30 pages**, all passing the §37 quality test (substantive, sourced, internally linked, distinguishable).

## INDEXABLE CORE (high priority per §22)
Sport homepage · 6 competition hubs · PL table · PL fixtures · 20 club hubs · PL clubs index · 13 explainers · 4 archive editions · MW4 live edition · analysis/transfers shelves. All current Sport URLs qualify as INDEX; no NOINDEX, parameter, or duplicate utility URLs exist to suppress.

## DATA SOURCES (as displayed on-page)
- PL table (MW3) and MW4 fixtures: cross-verified 2026-09-10 across NBC Sports, Sports Media Watch, footballfixtures.org, worldfootball.net (UK times cross-checked from CET/ET).
- Serie A / Bundesliga / Ligue 1 structure and champions: Wikipedia (Bundesliga/Ligue 1/Serie A), beIN Sports (Serie A 2026-27 dates), Transfermarkt (Inter 2025-26 scudetto). A 2–3 club discrepancy between Serie A sources → no club list published for Serie A until resolved.
- Evergreen explainers: premierleague.com, worldfootball.net, UEFA, Deloitte, LaLiga, BBC Sport, IFAB (on existing pieces).

## SEO CHANGES
Unique titles/descriptions and single-H1 structure on every new page; breadcrumbs (Sport → League → Table/Fixtures/Clubs → Club); descriptive anchors throughout; clean permanent URLs; sitemaps auto-include all 30 new routes (verified); last-verified timestamps on changing data; no keyword-stuffed titles; competition pages carry genuinely distinct facts.

## REMAINING WORK (honest)
1. **Weekly cadence:** results + matchweek reviews after each verified round; table update loop (the system exists; the habit is the product).
2. **LaLiga/Serie A/Bundesliga/Ligue 1/UCL live data desks** — same pattern as the PL hub, as rounds are verified.
3. **Results pages** with completed scores (requires post-round verification).
4. **Football Explained scale-up:** rules/technology/tactics/money/history categories per §14–17 (~30 more evergreen pieces at spec depth).
5. **Player pages** (§11): only when per-player verified data is reliably available.
6. **LaLiga/CL hub enrichment** to full PL-hub parity; international section (§18) after the six are established.
7. **Serie A promoted-club discrepancy** to be resolved before any Serie A club list is published.

## QUALITY SCORE
**7.5/10 — not 9.0 yet, by the spec's own standard.** The architecture (hubs, tables, clubs, matchweek system, gateway model, data integrity) now matches the 9+ blueprint, and everything published is verified. What separates 7.5 from 9.0–9.5 is cadence and depth: weekly verified results/reviews, live data for the other five competitions, and the full evergreen library. Those are next batches, and the system is built to absorb them without structural change.


## ADDENDUM — 2026-09-10, later: the detached old backend found and integrated (spec §2/§35 fulfilled in full)

The user pointed to the old Sport implementation on a detached branch (origin/agent-work-2026-09-03). Audit found the complete old backend and it is now integrated:

- **RECOVERED: official fixture calendars** — content/fixtures.json (all 380 PL matches, sourced to the official 19 June 2026 premierleague.com release, kickoff policy + change policy included) and four league calendars (LaLiga 380, Serie A 380, Bundesliga 306, Ligue 1 306, each with named sources, TBC policy for unpublished kick-off times).
- **NEW PAGES:** /premier-league-fixtures/ upgraded to the full 380-fixture calendar (verified MW4 card on top, every club linked to its hub, TV chips, TBC handling); four new permanent calendar pages /la-liga-fixtures/ /serie-a-fixtures/ /bundesliga-fixtures/ /ligue-1-fixtures/ (flat URLs — the router collapses nested sports paths, so nesting was rejected for robustness). All stamped with source + last-updated + change policy.
- **RECOVERED: club identity data** — content/club-history/*.json (already in-tree; 20 clubs with city + official source URLs, written source policy) now enriches every club page (city in byline, "official club history" source link) and the clubs index gained club badges.
- **RECOVERED: club badges** — 96 badge PNGs + five per-league SVG sets (PL/LaLiga/Serie A/Bundesliga/Ligue 1) extracted from the old branch into assets/img/sports/ (4.5 MB kept; 44 MB of unused hero/comic art pruned — remains recoverable on the origin branch). Badges live on club pages and the clubs index with lazy-loading, alt text and an identification note.
- **Slug bridges:** old short slugs (hull, man-city, coventry…) mapped to the current scheme at build time, with build-time assertions so a future data edit cannot silently break links.
- **Route conflict caught by gates:** validator flagged the nested-route collision and the /laliga/ vs /la-liga/ hub mismatch before push — fixed via flat routes + hub aliases.

**Site after integration:** 863 pages / 92,650 internal links OK, allowlist 853, validator ok, all four calendars in the live sitemap.

**REVISED QUALITY SCORE: 8/10.** The data spine the spec demanded (fixtures for all five league hubs, permanent calendar URLs, club gateways with sourced facts and badges) is now real and stamped. The remaining distance to 9+ is cadence (results/reviews after each verified round) and the evergreen library scale-up.
