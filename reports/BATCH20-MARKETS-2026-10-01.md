# Batch 20 — The Missouri Review, and the end of the fee-only tail

One new record, read off the publication's own guidelines page on 2026-10-01. Raw text
under `research/rebuild/raw/missouri_review.txt`.

| | |
|---|---|
| records added | 1 (`missouri-review`) |
| dataset after batch | **280 records** |
| allowlist | 647 routes, reviewed 2026-10-01 |
| gate results | build + all six gates exit 0; **280 publication pages**, 0 problems |

## 1. The market

| field | value | sentence |
|---|---|---|
| pay, print | $25 per printed page | "Authors are paid $25 per printed page." |
| pay, online feature | $100 per story or essay | "BLAST authors are paid $100 per story." / "BLAST authors are paid $100 per essay." |
| AI | **disclosure required**, not banned | "If artificial intelligence has been used to generate any portion of your submission, you must disclose your usage in specific detail within the piece and in your cover letter." |
| simultaneous | accepted, notify | "Simultaneous submissions are OK as long as you notify us if accepted elsewhere." |
| response | 10–12 weeks | "Standard response time is 10–12 weeks." |
| window | year-round | "The Missouri Review is open for submissions year-round." |
| postal route | accepted | "We also accept physical submissions. Please enclose a cover letter and self-addressed, stamped envelope…" |
| rights | **not stated** | no rights language on the submissions page |
| fee | **not stated** | no submission fee published on the page |

**Two rates in different units.** $25 a printed page and $100 a piece are not comparable, so
they are named separately in the record rather than averaged into one number. The range
(25–100) is the honest span of the two stated figures, with the display spelling out which is
which.

**Prize money stays context.** The 2026 Jeffrey E. Smith Editors' Prize pays $5,000 in each of
three genres; the Poem of the Year Prize and the William Peden Prize pay $1,000. None is a
rate for published work, and none is recorded as one — the same rule applied to the Fairy Tale
Magazine's $100 contest prize in batch 15.

**The AI position is unusual and is recorded as unusual.** Of 280 records, 110 prohibit AI and
7 require disclosure. The Missouri Review is in the second group: it does not ban the tools, it
demands specifics in the piece and the cover letter.

US filing: the page carries the University of Missouri's copyright line. Eligibility carries no
country restriction.

## 2. Fee-only markets read in the same pass — held

None of these states a contributor rate, and a fee is never a rate:

| market | what its page states |
|---|---|
| Beloit Fiction Journal | "Due to the cost of maintaining our online submission platform, we charge a ser[ial]" |
| Breakwater Review | "we charge a reading fee of $3 for general submissions" |
| Cola Literary Review | "Paid reading period (with a submission fee of $3)" |
| Flyway | "a nominal fee of $3 per submission" |
| Hole in the Head Review | "Submission fee is $20.00." |
| Harpur Palate | "The entry fee is $19 per story." |
| CutBank | writing submissions carry a $5–$7 fee; the only $250 figure is **cover art** |

## 3. Verification

Full scratch clone at the batch-20 tip, then the same again on a merged tree (see the
rehearsal addendum):

| gate | branch |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` | exit 0 |
| `validate:money` / `validate:hometools` | exit 0 |
| `audit_dockets.py` | **280 publication pages**, 973 unanswered rows, 145 rankings, **0 problems** |

## 4. Session running total

| batch | records | dataset |
|---|---|---|
| 14 | 6 | 261 |
| 15 | 3 | 264 |
| 16 | 8 | 272 |
| 17 | 5 | 277 |
| 18 | 1 | 278 |
| 19 | 1 | 279 |
| 20 | 1 | **280** |

**25 records added this session**, each read off the publication's own page on the check date.
