# BRYME HARO routine — journalist queries → referring domains

**Owner:** house ops · **Cadence:** 2×30 min weekly (Tue + Thu) · **Started:** 2026-09-28
**Goal:** earn referring domains (journalists/citation roundups linking thebryme.com)
by answering source queries with the two linkable assets the house already owns:

1. **The State of Paid Writing 2026 report** — `/writers/state-of-paid-writing-2026/`
   (computes pay bands, AI-policy counts, rights/response findings from the 142-record
   opportunities database at build time; every figure is citation-grade).
2. **The paying-publications database** — `/writing/` + `/writing-opportunities/`
   (142 records, per-entry verification dates).

## The platforms (checked 2026-09-28)

| Platform | URL | Status |
|---|---|---|
| Qwoted | qwoted.com | 200 — live |
| SourceBottle | sourcebottle.com | 200 — live |
| Help a B2B Writer | helpab2bwriter.com | 200 — live |
| JournoRequests | journorequests.com | 200 — live (X/#journorequest digest) |
| PitchResponse | pitchresponse.com | 200 — live |
| HARO/Connectively | helpareporter.com / connectively.us | reachable, rate-limited to our checks (429) — use the app, not scraping |

Register accounts on all six with the house mailbox. Query alerts go to a dedicated
folder/label (`bryme-haro`), never the editorial inbox.

## What we pitch (and what we never pitch)

- **Pitch:** data and expertise. "Our 142-record database shows X% of markets now state
  an AI policy; median stated USD minimum is $110 — full report at
  thebryme.com/writers/state-of-paid-writing-2026/." Numbers come straight from the
  report; never invent a figure the database does not compute.
- **Also pitch:** desk experts (sport rules explainers for rule-change stories; money
  guides for budget-season stories; tech spec floors for shopping-season stories) —
  always citing the specific guide URL.
- **Never pitch:** opinions as data, "our research shows" without the report link,
  embargoed or exclusive claims we cannot back with a published page, anything betting
  related (house rule), or a writer's personal experience as a house statistic.

## Response template (fill only with published facts)

> Hi [name] — [one-line answer to the query, with the number if the query asks for one].
> Source: BRYME's [report/guide] ([URL]) — computed from [n] verified records as of
> [month year]. Happy to provide the underlying breakdown ([what tables exist]).
> — [name], THE BRYME ([thebryme.com])

Rules: ≤150 words, one link max (the asset page), answer in the first sentence, reply
only when we genuinely answer the query (a 20% hit rate is normal; volume pitching is
how domains get banned).

## Weekly routine (2 × 30 min)

1. **Tue (25 min):** scan the six platforms for queries matching our asset areas
   (writing/freelance, media/AI policy, money, tech, sport rules). Log candidates in the
   tracker. Reply to the best ≤5.
2. **Thu (20 min):** follow-ups (none after one nudge), plus log wins in
   `docs/referring-domains-log.csv`.
3. **Monthly (15 min):** Bing Webmaster Tools → Backlinks + GSC → Links; record new
   referring domains in the log. Queries that produced coverage get re-pitched when the
   report rebuilds with a fresh window.

## Success metrics (monthly, in the log)

- Queries answered (target 8-10/month)
- Placements live with link (target 2-3/month)
- New referring domains (leading indicator; Bing/GSC link counts lag 2-4 weeks)

## Ground rules (house)

- Dates on everything; if a journalist cites our figure, the report must still compute it
  — if the dataset changes and a figure moves, we proactively correct the journalist.
- No fabricated statistics, no invented sources (master brief).
- The report is the pitch. Keep it fresh: it recomputes every deploy; the entry-level
  freshness is the dataset's own `updatedAt` and per-record `lastVerified`.
