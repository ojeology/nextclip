# Batch 13 — verified writing markets, 30 September 2026

Seven new paid markets were added to `content/opportunities.json`, taking the
desk from 248 records to **255**. Every figure was read off the publication's
own guidelines page on **2026-09-30**. Nothing here was taken from a directory,
an aggregator's pay note, or a search result.

This file exists because batches 1–12 committed only the data, the script and
the allowlist. The research behind them was written to `research/`, which no batch
ever committed: `git log --all -- 'research/*'` returns nothing, on any branch. The
directory is not in `.gitignore` — it simply never entered the repository, so a
fresh clone has no backlog and the reading behind 101 records is not reviewable.
Batch 13 keeps its evidence in the repository instead.

---

## 1. Why this batch began with a rebuild

Batches 5 to 12 each open with the words *"read from the batch-4 backlog. No
crawling."* That backlog was 450 saved guidelines pages under `research/batch4/`. It was never
committed, so it does not exist in a fresh clone, and the method those batches
describe cannot be repeated. (It is not gitignored — it was simply never added.)

The backlog was rebuilt the way batch 4 built it — the Poets & Writers Literary
Magazines directory for **names and official submission URLs only**:

| stage | result |
|---|---|
| pw.org listing pages scraped | 35 pages → **849** magazine slugs |
| detail pages fetched | 849 → **84** with a submission-guidelines URL (765 still queued) |
| new to this desk | **62** |
| own guidelines pages fetched | **52** |
| shipped here | **7** |

pw.org publishes pay notes and reading-fee flags. **None were used or copied.**
Every rate, length, right, fee and AI statement below comes from the
publication's own page.

The 849-slug list is reproducible with `scripts/rebuild-pw-backlog.py`.

---

## 2. The seven markets, with the sentence each figure came from

### Brick — $65–720 by length
> "Brick pays its contributors upon publication and offers $65–720, depending on
> the length of accepted work, plus two copies of the issue the work appears in
> and a one-year subscription to the magazine."

> "Brick is open for submissions twice a year: from October 1 to October 31 and
> from April 1 to April 30."

> "While Brick does not set a word limit, we tend toward a range of 1,000–5,000
> words."

> "Brick does not accept submissions that make use of AI-generated content."

Source: <https://brickmag.com/submissions/> — read 2026-09-30.
Recorded `upcoming` with `openingDate` 2026-10-01: the window opened the day
after this reading.

### Epiphany — $75 per poem, $175 per essay or story in print
> "In print, we pay $75 per poem and $175 per essay or story. All print
> submissions are considered for online only publication, which pays $50 per
> poem and $150 per essay or story. Art payments are made on a sliding scale."

> "We typically respond to submissions within five to six months, and aim for
> much faster."

Source: <https://epiphanymagazine.org/submit> — read 2026-09-30.

**One thing deliberately not flattened.** The same page carries *"No writing
that is plagiarized or created with the use of AI will be accepted."* It appears
twice, and both times inside a different application: once in the **Fresh Voices
Fellowship** section and once in the **art submissions** section. It is not
attached to general writing submissions, whose own block states windows and pay
and says nothing about AI. The record therefore reads `aiPolicy: "not-stated"`
for writing. Recording it as a magazine-wide ban would have invented a rule
Epiphany has not published for the work this record is about.

### Bracken — $30 per piece
> "We pay $30 for each previously unpublished piece of writing, $30 per art
> feature (which may consist of a single or multiple images), and a negotiated
> rate for cover art."

> "We do not consider AI-generated or AI-assisted work."

> "Poetry: $3 per submission. […] If the $3 submission fee is prohibitive for
> you, please let us know at info@brackenmagazine.com so that we can arrange for
> you to be able to submit without paying the fee."

Source: <https://brackenmagazine.com/submit> — read 2026-09-30.
Rights: first worldwide English-language serial and electronic rights, author
retains all others. Response: within four months, stated.

### 32 Poems — $25 per poem
> "Contributors receive $25 per poem and two copies of the issue in which their
> writing appears."

> "For electronic submissions, we charge a $3 processing fee, but that fee is
> waived for current subscribers." […] "we continue to accept fee-free postal
> submissions"

Source: <https://32poems.com/submission-guidelines> — read 2026-09-30.

Recorded `open` with `windowEnd` **2026-09-30** — the reading date is the closing
day of the August 1 to September 30 window. `build-writing-first.py`'s
`deadline_passed()` flips a lapsed window to closed at render time and prints the
honest "This window has closed" notice, so this record degrades correctly on its
own rather than needing a human to remember. The next window opens February 1.

### Metphrastics — $10 per poem, no fee, year-round
> "Payment: $10 per poem"

> "There is no fee to submit."

> "We welcome submissions year-round responding to works in the Metropolitan
> Museum of Art's permanent collection and special exhibits […] All styles are
> welcome from poets around the world."

> "AI-Generated Work: No, thanks."

Source: <https://metphrastics.com/submit> — read 2026-09-30.

This is the only record in the batch with a **stated** geographic scope, so it is
the only one recorded `mode: "worldwide"` rather than `not-stated`. The other six
say nothing about geography, and `not-stated` is the honest value — the same
position main's Phase 4 took on simultaneous submissions, where two-thirds of
markets had never published a policy.

### A Velvet Giant — $20 per author on publication
> "We pay our contributors $20 per author upon publication."

> "Donated funds are used to pay our illustrator and all of our contributors, as
> well as to maintain the website."

Source: <https://avelvetgiant.com/submit> — read 2026-09-30.

The rate depends on donations; that condition is recorded rather than hidden
behind a bare "$20". Submissions were **closed** on the reading date. Rights:
first serial, with acknowledgement requested in future publication. Response: no
more than six months, stated.

### Thriller Magazine — $15 per story, $4.49 to submit
> "Pay: $15 for accepted short stories"
> "Length: 1,000–7,000 words"
> "Response time: 4–5 weeks"
> "Submission fee: $4.49 (non-refundable)"

Source: <https://thrillermagazine.org/submissions> — read 2026-09-30.

The fee is charged to the writer and is **not** recorded as payment. At $15 for
an accepted story against $4.49 to submit, the record says plainly that the fee
applies whether or not the story is accepted, and that the detailed editorial
feedback on every submission is what a writer is actually buying alongside the
chance at the rate.

---

## 3. Simultaneous submissions — the Phase 4 field, carried forward

Main's Phase 4 added `simultaneousSubmissions` and `simultaneousNote` to all 147
records. The branch's 101 newer records do not have them. Batch 13's records do,
in the established shape, and **nothing is classified by keyword** — Phase 4
documented that substring matching was wrong at nearly every step.

| market | value | basis |
|---|---|---|
| Brick | `accepted` | *"We will read simultaneous submissions…"* |
| Bracken | `accepted` | *"Simultaneous submissions are considered."* |
| Metphrastics | `accepted` | *"Simultaneous Submissions: Absolutely fine."* |
| Epiphany | `not-stated` | no policy on the writing submissions block |
| 32 Poems | `not-stated` | no policy stated |
| A Velvet Giant | `not-stated` | no policy stated |
| Thriller Magazine | `not-stated` | no policy stated |

Where a policy is stated, `simultaneousNote` carries the exact sentence with its
URL and reading date, matching the shape Phase 4 used.

**Merge task:** the 101 branch records added before batch 13 still need this
field backfilled by reading each guideline. That is a separate pass and was not
attempted here — inventing the field for them would defeat the point of it.

---

## 4. Held back, and why

Batch 4 established the precedent of holding rather than rushing. Held here:

- **Hoot Review** — batch 4 already held it for this reason and it is unchanged:
  the payout is described in a comment thread ("average around $25", "30% of the
  whole $2"), not in the guidelines. It still cannot be recorded as a rate.
- **I-70 Review** — $15 entry fee and a $1,000 cash prize. A competition, not a
  rate for published work: the StoryQuarterly precedent from batch 12. No
  contributor rate is stated on the page.
- **Tadpole Press** — $5 to enter, $50 to one winner every other month, plus a
  $1,000 first prize. Same contest-prize problem.
- **Humana Obscura, Passages North, Mid-American Review, 2River, aaduna, TINGE,
  BoomerLitMag, Thin Skin** — each states plainly that it does not pay. Real
  markets, but not paying ones, and the index policy for this desk is
  research-backed **paid** opportunities. Batch 4 held the same class of market.
- **Relief Journal** — $3 submission fee, contributor copy, no stated cash rate.
  Fee-and-copy model; needs a fuller read before recording.

---

## 5. Verification performed

The build was run end to end on the 255-record data in a scratch tree.

| gate | result |
|---|---|
| `npm run build` | **passes** (exit 0) |
| 7 new `/writers/writing/<slug>/` pages generated | **7/7** |
| `verify:allowlist` | **passes** — 625 source routes, 2698 routed, 0 missing |
| `verify:titles` | **passes** — 1386 audited, 0 over 60 chars, 0 problems |
| `verify:dockets` | **passes** — 255 publication pages, 7 docket rows each, 0 problems |
| `validate:hometools` | **passes** |
| `validate:money` | **passes** — ok: true |
| `validate` | 2 failures, **both pre-existing and unrelated** (below) |
| `validate:techhub` | `MODULE_NOT_FOUND` — missing dev dependency in this sandbox, not a data problem |

### The build caught a real defect, which is the point of running it

The first build **failed**:

```
File "scripts/build-writing-first.py", line 810, in deadline_passed
    ds = dl.get(key)
AttributeError: 'str' object has no attribute 'get'
```

Three records (Brick, Bracken, 32 Poems) had been given a bare string deadline.
`deadline` is a structured object in this dataset (`display` / `date` /
`openingDate` / `windowStart` / `windowEnd` / `recurring`), and
`deadline_passed()` calls `.get()` on it. The string form crashes the build.

Confirmed as introduced by this batch, not pre-existing: deadline types at the
branch tip are 187 `null` and 61 `dict`, with **no strings**.

Fixed, and a guard was added to the batch script so the class of error cannot
return — the script now refuses to write a non-dict deadline, a deadline with no
display text, or a deadline that records no date of any kind.

### The two `validate` failures

Both are pre-existing branch debt, and this was established with a clean
baseline rather than an assumption: a **fresh `--depth 1` clone of the branch
tip** (248 records, built from an unbuilt tree) was built and validated, and it
fails on exactly the same two items and nothing else.

```
clean baseline (248 records, fresh clone)     FAIL (2)
batch 13       (255 records)                  FAIL (2)   <- identical set
```

1. `/writers/writing-opportunities/: missing local target /writers/writing-opportunities/pt/`
   — the `pt` mapping comes from `lisbon-literary-review`, which is mapped to
   base `pt` **identically at HEAD**. None of the seven new records maps to
   `pt`; all seven are `International`.
2. `/writers/writing/poetry-south/: "the American South" is in the record's
   eligibility but not in data-open-to`
   — `poetry-south` is present in the **HEAD** record set with that eligibility
   text and is not a batch-13 record.

An earlier baseline attempt copied an already-built 255-record tree and reverted
only the data files; it reported a spurious third failure (*"RSS includes
non-allowlisted /writers/writing/thriller-magazine/"*) because stale build output
for a record that exists only in batch 13 survived the rebase. That failure is an
artefact of the method, not a finding, and is recorded here so the mistake is not
repeated: **a baseline must be built from an unbuilt tree.**

Both genuine failures should be fixed before the branch is merged, but they are
branch debt, not batch-13 regressions.

---

## 6. Backlog for batch 14

**765 pw.org detail pages were still queued** when this batch shipped. pw.org
began rate-limiting the fetch run, which is why 849 slugs yielded 84 usable
guidelines URLs rather than batch 4's 450. The queue is kept under
`research/rebuild/` locally and the method is reproduced by
`scripts/rebuild-pw-backlog.py`.

Batch 14 should resume the queue rather than re-crawl, and should ship the
unpaid-but-real markets only if the desk decides to widen the index policy
beyond paid opportunities — a decision this batch deliberately left open.
