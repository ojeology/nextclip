# Batch 17 — five paid markets, read 1 October 2026

Fifth batch of the resumed pw.org backlog. Five new records, each read off the
publication's **own** guidelines page on the desk date 2026-10-01. Raw text under
`research/rebuild/raw/<slug>.txt`.

| | |
|---|---|
| records added | 5 |
| dataset after batch | **277 records** |
| allowlist | 644 routes, reviewed 2026-10-01 |
| gate results | build + all six gates exit 0; **277 publication pages**, 0 problems |
| new base countries | none |

## 1. The five markets

| market | rate | the sentence |
|---|---|---|
| **Frontier Poetry** | $50 per poem, New Voices route | "We are thrilled to offer significant payment to our partner poets: $50 per poem." / "New Voices Free – Always a free way to submit and we always pay for the work. We pay new poets $50 per poem selected." |
| **Half Mystic Journal** | US$20 per accepted piece | "We pay US$20 per accepted piece, and submissions close in April 2027." |
| **Infrarrealista Review** | $100 review/essay; $50 interview; $50 newspaper piece | "We pay $100 per review." / "We pay $50 per interview." / "We pay $100 per essay." / "CHE pays $50 per publication." |
| **InterrobangLit** | $3 token payment | "As of February 2026, we offer a token payment of $3 through PayPal." |
| **The Literary Fantasy Magazine** | $10 token payment, web | "We offer a token payment of $10 for submissions accepted for publication on the web." |

## 2. Where the route is the story

- **Frontier Poetry.** The $50 belongs to **New Voices** — "Always open. Always free."
  The same page runs the Discover New Art Prize, which charges **$20** per submission of
  up to three poems and pays prizes of $500/$200/$100. Recording "$50 per poem" without the
  route invents a payment that exists only on one path; folding the $20 in turns a writer's
  cost into a payout. The rate is recorded with its route, and the challenge is named in the
  conditions as a separate thing, exactly as the contest rule requires.
- **Infrarrealista Review.** Four figures across four sections. The record shows
  $50–$100 with both ends quoted; nothing is averaged.
- **Half Mystic Journal.** The journal pays US$20 a piece; the press route pays
  royalties on full-length manuscripts. A royalty is not a per-piece rate, so only the
  journal figure is pay and the manuscript model is named in the conditions.
- **The Literary Fantasy Magazine.** $10 on the web, and "Our print magazines offer higher
  pay" — with no print figure published. Only the stated rate is recorded; the sentence
  about print is kept as context, not converted into a number.

## 3. Two month-level deadlines, recorded as month-level

Neither page gives a day:

- **Half Mystic** — "submissions close in April 2027". Display text: *"Submissions for the
  Fioritura issue close in April 2027 (the page states the month, not a day)."*
- **The Literary Fantasy Magazine** — a "special submission window in October" 2026, open only
  to Storytelling Collective's Short Story September participants. Display: *"a special window
  in October 2026 runs for Storytelling Collective's Short Story September participants only."*

Each record's sort key uses the last day of the stated month so it can be ordered. **That is
an internal device, not the publication's date**, and the display text says so.

## 4. Status on the check date

| market | status | why |
|---|---|---|
| Frontier Poetry | open | New Voices is "Always open" |
| Half Mystic Journal | open | closes April 2027 |
| Infrarrealista Review | open | page states "We are currently open" |
| InterrobangLit | closed | window 1–8 September 2026 has closed; cadence is every other month from the 1st, closing on the 8th or at the cap; **the page does not name the next window**, so none is invented |
| The Literary Fantasy Magazine | closed | general submissions closed after a 376-submission June 2026 window; only the October special window is announced |

## 5. Rights, AI and what the pages do not say

- **Rights:** Frontier Poetry holds first publication rights for three months. Infrarrealista
  states it asks for *none* — "Creatives owning their work. We do not ask for your rights to
  your work." InterrobangLit asks for first electronic, 30-day exclusive electronic and
  archival rights. The Literary Fantasy Magazine asks for first printing and internet archival
  rights, with republication allowed after six months. **Half Mystic states nothing** — recorded
  as not stated.
- **AI:** Frontier Poetry, InterrobangLit and The Literary Fantasy Magazine prohibit it, each
  with its own wording (Literary Fantasy allows Grammarly and ProWritingAid "but highly
  discouraged"). Half Mystic and Infrarrealista state nothing — both recorded as not stated.
- **Fees:** the New Voices route is free and InterrobangLit's windows are free. No fee is
  stated on the other three pages, and **no fee is recorded** for any of them.

## 6. A false positive worth naming

**Emerald City Ghosts** matched the batch's payment filter on the heading *"Do We Pay?
Unfortunately, no."* It is unpaid and stays out of the dataset. The pattern matched the
question, not the answer — the same class of trap as *appalachia*'s subscription billing in
batch 14.

## 7. Verification

Full scratch clone at the batch-17 tip `c7345644c3`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` | exit 0 |
| `validate:money` / `validate:hometools` | exit 0 |
| `audit_dockets.py` | **277 publication pages**, 966 unanswered rows, 142 rankings, **0 problems** |

**Not verified here, by construction:** the four batch-17 records that state a simultaneous
policy (`frontier-poetry`, `interrobanglit`, `literary-fantasy-magazine` accepted;
`infrarrealista-review` and `half-mystic-journal` are `not-stated` and carry no note) must be
verified on the merged tree, which is the only place the note row renders.

## 8. Running total on the backlog

277 records on the branch, 14 shipped this session (batch 14's six, batch 15's three, batch
16's eight, batch 17's five). The pw.org queue stands at 285 detail pages read; the remainder
of the pass is thinning out — most of what is left is unpaid, fee-only, or pays on a route
that needs its own reading. The crawlers are still running, so later batches will draw on
pages that have not been fetched yet.
