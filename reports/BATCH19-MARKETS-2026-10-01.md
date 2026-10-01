# Batch 19 — Menagerie, and the difference between a rate and a job

One new record, read off the publication's own guidelines page on 2026-10-01. Raw text
under `research/rebuild/raw/menagerie_magazine.txt`.

| | |
|---|---|
| records added | 1 (`menagerie-magazine`) |
| dataset after batch | **279 records** |
| allowlist | 646 routes, reviewed 2026-10-01 |
| gate results | build + all six gates exit 0; **279 publication pages**, 0 problems |

## 1. The market

| field | value | sentence |
|---|---|---|
| pay | $50 per acceptance | "We pay $50 per acceptance (e.g. one piece of prose or one to three poems) and acquire first serial rights." |
| rights | first serial; no reprints | "We do not republish work that has already appeared el[sewhere]." |
| limits | prose ≤5,000 words; poetry 3–5 poems | "Stories and essays should be no more than 5K. We tend to publish in the 1-3K category more frequently…" |
| response | 60–90 days | "Please expect a response time of 60-90 days." |
| simultaneous | allowed, withdraw | "Simultaneous submissions are allowed. If your work is accepted elsewhere, please withdraw it." |
| AI | refused | "Absolutely no AI. We're interested in writing that reflects real, lived experience, not the hallucinations of LLMs." |
| status | temporarily closed, no date | "Status: Menagerie is TEMPORARILY CLOSED for submissions to catch up on our backlog. We will reopen as soon as we can." |

The page states no fee and no rights beyond first serial; both are recorded as stated, and
nothing is inferred from other magazines of its size. Base country: none stated, so the
record is filed International.

**On the closure:** there is no reopening date, so the record carries **no deadline object at
all** rather than a placeholder date, and the closure is repeated in the requirements and
how-to-submit text where a writer will actually meet it.

## 2. Midnight & indigo — why it is not here

It surfaced in the same pass on "We pay for all accepted work and are 100% Black woman-owned."
Reading the page it points to, the only pay figure is for its **Writing Program**: a per-hour
rate for teaching roles, "discussed with chosen applicants upon receipt of the query". That is
employment, not a rate for published writing, and recording it would put a teaching salary in
a writers' pay field. No contributor rate is stated on the submissions page, so no record is
made.

## 3. Verification

Full scratch clone at the batch-19 tip `7212775d3b`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` | exit 0 |
| `validate:money` / `validate:hometools` | exit 0 |
| `audit_dockets.py` | **279 publication pages**, 971 unanswered rows, 144 rankings, **0 problems** |

**Not verified here:** the new `simultaneousNote` again — the branch draws seven docket rows,
so notes only render on the merged tree.

## 4. Running total

| batch | records |
|---|---|
| 14 | 6 |
| 15 | 3 |
| 16 | 8 |
| 17 | 5 |
| 18 | 1 |
| 19 | 1 |
| **session total** | **24 records → 279 on the branch** |

The crawler keeps fetching while the desk reads (650+ detail pages cached), so later batches
will draw on pages that did not exist when this one shipped.
