# Batch 24 — ten markets, and the money on each page sorted by kind

Ten new records, each read off its own page, plus five closed leads and one
duplicate resolved. **300 records** after this batch.

| | |
|---|---|
| records added | 10 |
| dataset after batch | **300 records** |
| allowlist | 674 routes, reviewed 2026-10-02 |
| gate results | build + all six gates exit 0; **300 publication pages**, 0 problems |
| note audit | 180 notes, 0 defects |
| closed leads | 5, with the sentence that closes each |

## 1. The batch

| market | rate recorded | window | notes |
|---|---|---|---|
| Exposition Review | $50.00 USD | 1 Oct – 15 Dec (open now) | copyright stays with author |
| Mulberry Literary | $25 USD flat | closed; July windows | free / pay-what-you-can July windows |
| Claudine | $25 per micro | Jan–Nov (open) | 400 words firm; free to submit |
| Nimrod International Journal | $20 per poem or prose page, $300 max | 1–31 Oct (open now) | free general submissions |
| Old Pal | $50 | closed; spring and fall | rights revert on publication |
| Overtime | $40–$60 per story | rolling | 5,000–10,000 words, work as theme |
| Pacifica Literary Review | $25 per published piece | year-round with 3 closure months | |
| Palette Poetry | $50 per poem, up to $150 | year-round, free | |
| Pangyrus | $30 per accepted piece | 15 Sep – 15 Nov (open now) | $3 charge per category |
| Kweli Journal | **no figure published** | 1 Sep – 30 May (open) | "Payment is after publication." |

## 2. Where the money on a page is not all the same kind

Four of these pages mix money, and the record sorts them:

**Nimrod** pays $20 per poem and per page of prose with a $300 maximum. The
same page advertises the Literary Awards — $2,000 first, $1,000 second — which
sit behind a $25 entry. The prizes are contest outcomes; the fee is a cost; the
recorded rate is the $20/300 arrangement, and general submissions are free.

**Pangyrus** and **Palette Poetry** both sell extras: a $3 charge per
submission category, and paid Fast Response and Editorial Feedback options.
Those are the writer's costs. The rates are $30 a piece and $50 a poem up to
$150. Neither fee word appears in the recorded rate.

**Mulberry Literary** runs two July windows — free (1–14) and
pay-what-you-can (15–31). The donation is a cost, not pay; the rate is a flat
$25 USD, distributed by PayPal.

**Kweli** is the honest blank: its page says only "Payment is after
publication." No amount is published, so none is recorded — the same shape the
dataset already uses for Black Warrior Review. Recording a guess, or dropping
the market as unpaid, would both have been wrong.

## 3. Leads closed in this batch

| lead | why it closes |
|---|---|
| Action Spectacle | No rate for general publication. All money on the page is fee-backed contests ($20 Editors' Prize entry, $25 book/chapbook entries, $1,000 prizes). |
| Anacapa Review | No payment stated for publication; $3 an entry. The $500 and 10 author copies are the John Ridland Poetry Prize, behind a $30/$25 entry and open to poets 55+. |
| Blue Earth Review | "Payment is two contributor's copies." |
| Chicago Quarterly Review | "PAYMENT FOR PUBLICATION: Two copies of the Chicago Quarterly Review." |
| Dunes Review | "Payment comes in the form of two copies of the journal, or one digital copy for international contributors." |

The three copies-only journals are unpaid markets in their own words; copies
are not money, and the index is for paid opportunities. The two contest pages
are the clearest version of the rule the desk keeps re-learning: a prize is
context and a fee is never the rate.

## 4. The duplicate, resolved rather than re-added

The long pw.org slug
`after_dinner_conversation_philosophy_ethics_short_story_magazine` turned out to
be the same market the dataset already holds as `after-dinner-conversation`. The
page was re-fetched on the desk date; the $75 rate and the AI ban are unchanged.
`lastVerified` was bumped to 2026-10-02 by
`scripts/refresh-after-dinner-conversation-2026-10-02.py`, which refuses to run
twice or against an unexpected record shape. No second record was created.

## 5. Verification

Scratch clone at the batch tip `b09fc95608`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` / `validate:money` / `validate:hometools` | all exit 0 |
| `audit_dockets.py` | **300 publication pages**, 1356 unanswered rows, 0 problems |
| new pages | all ten built, 31,421–32,255 b |
| note audit | **180 notes, 0 defects** — sentence renders, correct label, punctuation clean |

Five existing records were also re-read against their saved pages while working
this batch — Blackbird, Booth, Consequence, First Line and Gavialidae. Each
already matched its page (rate, windows, AI policy, simultaneous policy, word
counts), so no field needed changing and no date was touched: their pages were
fetched by the crawler, not re-fetched today, and the desk does not count a
saved-page read as a fresh verification.

## 6. Session running total

| | |
|---|---|
| batches this session | 14–24 (eleven batches) |
| records added | **45** |
| dataset | **300 records** |

## 7. The backlog, honestly

The "queue exhausted" claim stays dead. While this batch was being worked, the
candidate reader kept fetching, and the saved corpus grew from 332 pages to
370 — of which ~250 still have no record and no recorded decision. The focused
sweep has already surfaced the next candidates:

- **hoot_review** — a revenue-share arrangement ("pay the author 30% of the
  whole $2"); needs a careful read before any figure is recorded.
- **no_dear** — "$200 + 10 copies" for a chapbook selection; needs reading to
  see whether it is a rate or a selection prize.
- **north_carolina_literary_review** — the $250 sums are honouraria for
  specific named content, not a general rate; needs reading before deciding.
- A long tail of pages whose only payment sentence is "upon publication" or
  "receive a copy", which are copies-only exclusions to document in the next
  batch rather than records.

Next unit of work: read and decide those three, then work the remaining
copies-only and fee-only tail into documented exclusions.
