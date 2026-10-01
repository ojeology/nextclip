# Batch 22 — Black Warrior Review, a paying market that publishes no figure

One new record, read off the publication's own guidelines page on 2026-10-01. Raw text
under `research/rebuild/raw/black_warrior_review.txt`.

| | |
|---|---|
| records added | 1 (`black-warrior-review`) |
| dataset after batch | **288 records** |
| allowlist | 655 routes, reviewed 2026-10-01 |
| gate results | build + all six gates exit 0; **288 publication pages**, 0 problems |

## 1. The market, and why it has no number

| field | value | sentence |
|---|---|---|
| pay | **stated, amount not published** | "Black Warrior Review is a paying market. The amount per contributor or piece is dependent on our overall number of contributors for a given issue, and the budget allocated to us by our presiding office at the University of Alabama, the Office of Student Media." |
| pay (again) | same | "We always pay our contributors." |
| windows | 15 Dec – 1 Mar and 1 Jun – 30 Sep, liable to change | "…predominantly in the winter (December 15th-March 1st) and summer (June 1st-September 30th)." / "These dates are liable to change…" |
| limits | prose ≤6,000 words; nonfiction ≤4,000 | "We accept pieces of up to 6,000 words…" / "please limit your submissions to 4000 words" (nonfiction) |
| response | 3–6 months | "the average response time for submissions is between 3-6 months" |
| simultaneous | welcome if noted | "Simultaneous submissions are welcome, if noted, and please notify us immediately if the work is accepted somewhere else." |
| AI | refused | "Black Warrior Review will not consider any submissions translated, written, developed, or assisted by these tools." (naming ChatGPT) |
| rights | revert on publication | "Rights revert to author upon publication." |
| fee | mentioned, **not quantified** | "we also offer fee waivers for writers whom the submission fee would present financial hardship, and we offer free submissions for incarcerated writers" |

**The judgement this record makes.** Two wrong answers were available. Inventing a typical
small-press figure would be a fabrication. Dropping the market because it publishes no number
would erase a market whose own page states twice, plainly, that contributors are paid — the
thing a writer most needs to know. The record carries null amounts with the display *"Payment
stated, amount not published"*, the same shape batch 14 used for American Short Fiction's
"Payment is competitive", and the conditions quote the sentence that explains the variability.

The $15 and $25 figures on the page are **subscription prices**, not pay and not fees. The
submission fee is real but unquantified in the text as read, so no fee figure is recorded
either — the same discipline that keeps a fee out of a rate, applied to a fee with no amount.

**Status on the check date:** closed. The summer window ended 30 September 2026, one day before
the check; the winter window opens 15 December 2026. Both dates are recorded with the page's own
warning that they can shift as the masthead turns over.

## 2. Verification

Full scratch clone at the batch-22 tip `79601a5204`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` | exit 0 |
| `validate:money` / `validate:hometools` | exit 0 |
| `audit_dockets.py` | **288 publication pages**, 999 unanswered rows, 152 rankings, **0 problems** |
| new page | `public/writers/writing/black-warrior-review/index.html`, 30,899 bytes |

## 3. Session running total

| batches | records added | dataset |
|---|---|---|
| 14–21 | 32 | 287 |
| **22** | **1** | **288** |

**33 records added this session**, every figure read off the publication's own page on the
check date, every absence recorded as an absence.
