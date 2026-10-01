# Batch 21 — seven markets a too-narrow filter had hidden

Seven new records, each read off the publication's own guidelines page on 2026-10-01. Raw
text under `research/rebuild/raw/<slug>.txt`.

| | |
|---|---|
| records added | 7 |
| dataset after batch | **287 records** |
| allowlist | 654 routes, reviewed 2026-10-01 |
| gate results | build + all six gates exit 0; **287 publication pages**, 0 problems |

## 1. Why this batch exists after batch 20 said the queue was empty

Batch 20 concluded the pass was finished. It was not — **my triage filter was the problem,
not the queue.** It matched a narrow set of phrasings ("we pay", "pays $", "payment of $",
"honorarium", explicit unit rates) and therefore missed every page that says the same thing in
a different shape:

| market | the phrasing that slipped through |
|---|---|
| Idaho Review | "we … pay contributors $300 for short stories" |
| Berkeley Fiction Review | "we now offer a $25 payment for accepted stories" |
| Blue Marble Review | "Contributors published online … will receive $30 per published piece" |
| Claudine | "Pay is $25 upon publication." |
| HEART | "PAY: $25 upon publication" |
| Ink In Thirds | "Our current payment is $5 USD per contributor" |
| F(r)iction | "Payment / $25 per final printed page" |

A looser pass — any dollar figure in a sentence that also mentions paying, contributors,
writers or publication — surfaced **21 candidate pages**, of which these seven state a
contributor rate. The rest are prizes, fees or revenue shares.

**The lesson, recorded in the script and the commit:** a payment filter that matches one
grammatical shape reports an empty queue long before the queue is empty. Any claim that a
backlog is "read out" has to survive a second, looser sweep.

## 2. The seven markets

| market | rate | key sentence |
|---|---|---|
| **Idaho Review** | $300 a story, $75 a poem | "We buy first worldwide serial rights and pay contributors $300 for short stories and $75 for each accepted poem. In addition, we send two copies…" |
| **F(r)iction** | $25 per final printed page | "Payment / $25 per final printed page and two free contributor's copies" |
| **Berkeley Fiction Review** | $25 an accepted story | "we now offer a $25 payment for accepted stories and continue to offer a complimentary copy of the Issue" |
| **Blue Marble Review** | $30 a piece, $75 cover art | "Contributors published online in Blue Marble Review will receive $30 per published piece, $75 for cover art." |
| **Claudine** | $25 on publication | "Pay is $25 upon publication." (microfiction and micro creative nonfiction) |
| **HEART** | $25 on publication | "PAY: $25 upon publication on website and digital copy if published in issue." |
| **Ink In Thirds** | $5 per contributor | "Our current payment is $5 USD per contributor (it can vary based on yearly donations but will not be less than $3 per contributor)." |

## 3. Figures that are not rates

- **F(r)iction's $2.50** is a submission charge. Its page says "100% of our reading fees go
  toward paying the contributors" — the sentence that turns a fee into an apparent rate. The
  fee is recorded as the writer's cost.
- **Idaho Review's "There is no entry fee"** is a cost statement, and the rate for **creative
  nonfiction is never stated** even though stories and poems have figures. The record leaves
  that rate absent rather than borrowing the story rate — the same rule that keeps a poetry
  rate out of a prose field.
- **HEART's $500** is the HEART Poetry Award. An outcome, not a rate.
- **Blue Marble's $75** is cover art against $30 a piece: two routes, both quoted.
- **Ink In Thirds pays per contributor, not per piece**, with a floor the page states ($3).
  Recording "$5 per piece" would overstate it for anyone publishing twice in an issue.

## 4. Eligibility that is an age limit, not a country bar

Blue Marble Review: *"We welcome submissions from students ages 13-22."* Recorded as
`restricted` with the reason spelled out in the summary — an age range, no country restriction
stated — so it cannot be mistaken for a nationality bar by a reader or by the country pages.

## 5. One defect caught in review

The Idaho Review's pay range was first written **300–300**, correct for stories and wrong for
everything else: it hid the $75 poem rate inside a single number. It is now **75–300**, the span
of the two stated figures, with the display naming both. Caught by the post-write assertion
step, not by a gate.

## 6. Verification

Full scratch clone at the batch-21 tip `e9d096e4f8`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` | exit 0 |
| `validate:money` / `validate:hometools` | exit 0 |
| `audit_dockets.py` | **287 publication pages**, 996 unanswered rows, 152 rankings, **0 problems** |

All seven new pages generated (30.2–31.3 KB).

**Not verified here:** the six new simultaneous notes (Idaho, F(r)iction, Berkeley, Claudine,
Ink In Thirds accepted; Heart and Blue Marble not stated, so no note). They render only on a
merged tree — and the full note audit run earlier this session on the previous merged tree
covered 164 notes with 0 defects, so the method is established and needs re-running after any
further records.

## 7. Session running total

| batch | records | dataset |
|---|---|---|
| 14–20 | 25 | 280 |
| **21** | **7** | **287** |

**32 records this session.** Batch 20's "the queue is finished" claim is withdrawn: the loose
pass found seven more paying markets in the same pool, and the remaining candidates from that
pass (prizes, fees, revenue shares) are now named in the script so the next sweep starts from
the honest position rather than from zero.
