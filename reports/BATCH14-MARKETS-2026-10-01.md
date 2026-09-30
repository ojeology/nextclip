# Batch 14 — verified writing markets, 1 October 2026

Six new markets, read off each publication's **own** guidelines page on
**1 October 2026**. The desk goes from 255 records to **261**. Raw text of every
page read is kept at `research/rebuild/raw/<slug>.txt` so a reading can be
re-checked without re-fetching.

---

## 1. Why the date is 2026-10-01

The crawl runs on the sandbox's UTC clock; the desk is in Lagos. The reads in this
batch happened between **2026-09-30 23:18 UTC** and **2026-10-01 00:5x UTC**,
which is **2026-10-01 00:18–01:5x West Africa Time** — already the next day at the
desk. The desk's own local date is the check date, so every record here carries
`lastVerified: 2026-10-01`, and each raw file is stamped with both clocks:

```
# fetched 2026-09-30 23:18 UTC = 2026-10-01 00:18 WAT (desk date 2026-10-01)
```

Without the second stamp the evidence would look a day stale beside the record it
supports.

## 2. Where these candidates came from

Batch 13 shipped with **765 pw.org detail pages still queued**. This batch resumed
that queue rather than re-crawling, and triaged the results against the desk:

| stage | result |
|---|---|
| detail pages fetched (resumed queue) | 200 at the time of writing, climbing |
| candidates not already on this desk | 104 pages fetched |
| read | 104 |
| shipped here | **6** |

pw.org supplied names and official submission URLs only. Its own pay notes and
reading-fee flags were not read and are not used anywhere in these records.

## 3. The six markets, with the sentence each figure came from

### American Poetry Journal — $25 honorarium per poet or artist
> "Poets and artists will each get paid a $25 honorarium for publication."

Opens **1 November 2026** for the February 2027 issue, with a free DEI submission
day on 13 November. Poetry: up to 3 poems in one file, 7 pages. Cover art: up to 5
pieces. Simultaneous submissions are fine if declared; multiple submissions within
a period are not considered.

**The trap in this record:** the page also says the **$3.00** submission fee helps
"pay contributors and poet staff". That sentence read carelessly becomes a rate.
It is the *writer's* money and is recorded as a fee.

### After Dinner Conversation — $75 one-time, no future royalties
> "Accepted short stories from unsolicited submissions are paid a one-time amount
> of $75 with no future royalties."

Adult stories 1,500–7,000 words (2,500–4,500 fare best), YA under 3,500, children's
under 1,500. Won't consider work already readable on the open web; no AI-generated
writing. The $25 Fast Pass and $80 feedback service are the writer's costs.

### American Short Fiction — paid on publication, amount not published
> "Payment is competitive and upon publication. American Short Fiction purchases
> first serial rights. All rights revert to the author upon publication."

Unsolicited submissions run **September through December**, cost **$3**, and are
read one story at a time. Recorded as paid-but-not-published: the page states that
payment happens and publishes no figure, so no figure is invented and it is not
recorded as "not stated" either.

### Bayou Magazine — $150 / $100 for fiction by length
> "Payment for fiction of >3000 words is $150, <3000 words is $100."

The same page's general line reads "Payment is one contributor's copy unless
otherwise specified by genre", so both sentences are recorded: the cash rate is the
fiction rate, and other genres are paid in copies. Fiction up to 7,500 words.
Reading period **15 September – 15 December**. "We will not publish work that has
been composed, revised, or edited by AI", with the right to check between
acceptance and publication. University of New Orleans students, faculty and alumni
are not eligible — recorded in eligibility, not hidden in prose.

### Bennington Review — $120 / $250 for prose, $25 per poem
> "We pay contributors $120 for prose of six typeset pages and under, $250 for
> prose of over six typeset pages, and $25 per poem, in addition to two copies of
> the issue in which the piece is published and a copy of the subsequent issue."

Next reading period **4 January – 5 March 2027**. Acquires first North American
serial rights. Work must be unpublished in print or online, **including on personal
blogs**. Current or recent Bennington College students, faculty and staff may not
submit; alumni wait three years.

### Blackbird — $40 per poem, $200 per story or essay
> "We pay $40/poem." · "We pay $200/story." · "We pay $200/essay." · "We pay
> $100/book review, craft essay, and interview."

Submissions for Blackbird 2.0 are open; four issues a year. Poetry: 2–6 poems in one
document. "We do not accept work that has been produced or altered by AI in any
way." Simultaneous submissions acceptable if flagged.

## 4. Read and held back

Held is not rejected — most of these are real markets that pay nothing, and this
desk's index policy is research-backed **paid** opportunities.

| market | why held |
|---|---|
| apricity | "no submissions fee, nor is there any payment for publishing your work (currently)" |
| amsterdam_review | "unable to offer paid compensation for accepted submissions at present" |
| after_brunch_journal | "volunteer-based … not able to offer payment to our contributors" |
| appalachia | "very limited budget and cannot pay for most unsolicited material"; two contributor copies |
| aaduna | "does not provide publishing honorarium nor charges any fee" |
| atlantic_northeast | "right now we are unable to pay contributors for their work" |
| autumn_sky_poetry_daily | "There is no payment for contributors" |
| acorn_review | $5 reading fee, no contributor rate stated |
| allium | $3.00 reading fee; window opens 13 November 2026; no rate stated |
| alaska_quarterly_review | "The fee is $3." No rate stated |
| anomaly (ANMLY) | $3 fee with hardship waiver; no rate stated |
| arkana | the $50 figures are Editors' Choice Awards and an Arkansas Writers prize — a prize is not a rate |
| bacopa_literary_review | $2 fee and cash awards by category — contest money, not a rate |
| acdc | $5 tip jar buys a faster response; a writer's cost, no rate stated |
| aura_literary_arts_review | the $10/$15/$25/$50 figures are donation buttons |

## 5. Two markets a keyword scan would have shipped as paying

A money-word scan is a triage aid and never a source. Both of these produced
payment-language hits and neither pays writers for unsolicited work:

- **Appalachia** — 15,000 characters of "payment" language, all of it
  *subscription billing* ("Recurring Payment options", "Payment Method").
- **antiphony** — "$2,579.96", "From $107.50/mo": Squarespace newsletter-template
  boilerplate, not a rate.

The batch-13 precedent (cholla-needles, whose refusal contains the substring
"accept simultaneous") is the same failure mode in the other direction: text that
looks like a policy and is read as one.

## 6. Verification performed

Built and validated from a **full scratch clone** at the batch-14 commit, not from
the sparse research clone — the research clone has no article directories and no
`public/`, so it cannot render a page.

| check | result |
|---|---|
| `npm run build` | **exit 0** |
| `npm run validate` | **exit 0** — `ok: true` |
| `verify:allowlist` | **passes** — source allowlist 626 → **632 routes**, routed 2705, 0 missing |
| `verify:titles` | passes — 1,404 titles, 0 problems |
| `verify:dockets` | passes — **261 publication pages**, 0 problems |
| `validate:money` | passes |
| `validate:hometools` | passes |
| six new publication pages | all generated (`public/writers/writing/<slug>/index.html`) |

The allowlist step is not automatic: a new record generates an indexable page that
the hand-maintained allowlist does not know about, so
`sync-writing-allowlist.py --reviewed 2026-10-01` was run before the build. That is
the step batch 13's report identified as easy to forget.

### What this build could NOT check

The branch's docket draws **seven** rows; the simultaneous-submissions row is
main's eighth. So **nothing on this branch renders `simultaneousNote`** — including
the six new notes. They are verified on the merged tree in the merge rehearsal, not
here. This is the same blind spot that let three notes carrying `" ."` pass every
branch-local check in batch 13.

## 7. Backlog for batch 15

The pw.org queue is still running: 849 slugs, 200 detail pages at the time of
writing, ~10 rows/min. `research/rebuild/raw/` holds 104 read pages, 8 of them thin
(under 400 characters — JS walls or error pages, to be re-read with the browser
tool before anything is concluded about them).

Batch 15 should continue the same queue. `scripts/read-pw-candidates.py` fetches
each new candidate's own guidelines page in watch mode, and the six records here
came out of the first 104 pages read, so the queue is still yielding.
