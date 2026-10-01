# Batch 23 — the six stale windows re-verified at their own pages

**Date of record:** 1 October 2026 · **Phase 19 Stage 0.1** · **Records changed:** 6 · **Records added:** 0

## Why this batch exists

Every build has carried the same warning since before the markets merge:

```
WARNINGS (1)
  - 6 record(s) have a passed deadline but a live status — re-verify:
    chicken-soup, the-fiction-desk, granta, aurealis, ecotone, 32-poems
```

The warning is `validate-site-quality.js` line 197: `deadline.date` is earlier than
today while `submissionStatus` is still `open`, `deadline` or `rolling`. It is not a
reader-facing lie — the renderer flips a lapsed window to closed at build time, so no
page tells a writer a window is open when it is not. It is a **record** that has gone
stale, and the honest fix is not to silence the warning but to go and read the six
guideline pages again. All six sit on 30 September 2026 windows, which closed yesterday.

Each was fetched today from the publication's own page, and each URL is already in that
record's `sources` array — no new source was invented.

## What each page said, and what changed

### chicken-soup — still a live deadline, just a nearer one

`chickensoup.com/story-submissions/possible-book-topics`, read 1 Oct 2026. Chicken Soup
runs one deadline per book topic, and the publisher extends them. Random acts of kindness
(extended to 30 September 2026) has now closed; **Humorous stories has been extended to
15 October 2026** and is the nearest open deadline.

`deadline.date` 2026-09-30 → **2026-10-15**. `windowEnd` stays 2026-11-30 — in this
record that field means the last 2026 topic deadline (Married/couples, extended to
30 November 2026), not the nearest one, and it is still correct. Display rewritten to the
full current sequence: Humorous 15 Oct 2026 · Married/couples 30 Nov 2026 · Pets
31 Jan 2027 · Positive thinking 28 Feb 2027 · Dogs 31 Mar 2027 · Cats and Holiday
30 May 2027. Status stays `deadline`; the page renders "🟡 Limited window — Open now, but
closes on a stated date." The page also repeats in capitals that it accepts no
AI-generated or AI-assisted work, which the record already carries.

### the-fiction-desk — closed, and the next call has no published date

`thefictiondesk.com/submissions/`, read 1 Oct 2026: *"we run three seasonal submission
calls a year. Our winter call will be opening soon. Sign up for our newsletter … to hear
all about it."*

`submissionStatus` `deadline` → **`closed`**. This is the one where the temptation is to
guess a December date; the page does not give one, so the record says the winter call is
announced but undated and points at the newsletter. Nothing invented.

### granta — four windows a year; December is next

`granta.com/submissions/`, read 1 Oct 2026: *"We will be open for non-fiction and fiction
submissions during the following periods in 2026: 1 March – 31 March, 1 June – 30 June,
1 September – 30 September, 1 December – 31 December … We are currently closed for poetry
submissions but we aim to re-open soon. Submissions can be made from 10 a.m. UK time on
the opening day until midnight UK time on the closing day."*

`submissionStatus` `deadline` → **`upcoming`**; `openingDate` **2026-12-01**,
`windowStart` 2026-12-01, `windowEnd` and `date` **2026-12-31**. The old display said
"Open 1–30 September 2026. Further 2026 windows: 1–31 December" — it named the December
window but left the record pointing at September, which is why the warning fired. The page
renders "🟡 Opens soon · Seasonal". The £3.50 full-length-prose fee and the 200 free
low-income submissions per opening period were already recorded and re-confirmed today.

### aurealis — the 2026 window closed; 2027 splits by who you are

`aurealis.com.au/submissions/`, read 1 Oct 2026: *"Submissions from Australian writers and
Subscribers from anywhere: 1 February – 30 September. Submissions from anyone anywhere:
1 – 14 March."*

`submissionStatus` `open` → **`upcoming`**; `openingDate` **2027-02-01**, `windowEnd` and
`date` 2027-09-30. The two windows are not the same window and the display now says so
explicitly: a writer who is neither Australian nor a subscriber has **only 1–14 March
2027**, not the February–September run. That distinction is the difference between a
usable record and a misleading one. Pay re-confirmed unchanged: AUD 2–6c a word, *"For all
stories published in 2027, Aurealis will be paying AUD6c a word"*, A$40 non-fiction, A$25
black-and-white art; 2,000–8,000 words; email only, rtf only; no simultaneous submissions;
no AI; no reprints.

### ecotone — closed early, and the next period is stated in months

`ecotonemagazine.org/submissions/`, read 1 Oct 2026: *"Fall 2026 — Due to overwhelming
response, we must close our general window for fall 2026. We will open to fee-free
submissions from current subscribers for the month of September."* That subscriber window
has now passed too. *"Each year, when possible, we offer two reading periods, beginning in
January/February and in August/September … we may need to close before the end of our
general window."*

`submissionStatus` `deadline` → **`closed`**; `date` set to 2026-09-30 so the closed call
is dated (mirroring `efiko`, the existing closed-and-recurring record). The display says
the next general period begins **in January or February 2027** and that Ecotone publishes
months rather than dates — no day invented. Honorarium $100 minimum re-confirmed.

### 32-poems — two fixed windows a year; February is next

`32poems.com/submission-guidelines/`, read 1 Oct 2026: *"32 Poems welcomes submissions from
February 1st to March 31st (2/1 – 3/31) and from August 1st to September 30th
(8/1 – 9/30)."*

`submissionStatus` `open` → **`upcoming`**; `openingDate` **2027-02-01**, `windowEnd` and
`date` 2027-03-31. These are fixed annual dates, so unlike Ecotone the day is published
and is recorded. Pay re-confirmed: $25 per poem plus two copies, $3 electronic processing
fee waived for current subscribers, fee-free postal submissions, five poems maximum in one
document, one active submission at a time, no translations.

## What this does not claim

- No record was added and no pay figure changed. The six pay records were re-read and
  found still correct, including Aurealis's 2027 rate rise, which was already recorded.
- Where a publication states months and not days (Ecotone), or announces a call and
  publishes no date (The Fiction Desk), the record says that. Two of the six are now
  `closed` rather than `upcoming` for exactly that reason.
- This retires the *stale-status* item on the Stage 0 list. It does not touch the other
  Stage 0 backlogs: 194 reading periods not yet assessed, 141 experience fields not yet
  assessed, 9 guidelines never read, 118 records with no simultaneous-submission note.

## What re-verifying six windows exposed on the home page

Setting `lastVerified` to today on six records moved them to the top of the
"RECENTLY VERIFIED" strip, which is correct — that strip is ordered by `lastVerified` and
is derived. It also moved two cards in the strip below it, and that strip was not correct.

The home page and the ecosystem hub both carry a block headed:

```
STRONGEST · GSC 2026-09-20→29 · POS 4–13
```

with every card inside it labelled **"Top performing"**. `build-landing.py` built it from
`_PICKS`, the four pages the September Search Console export named, and then ran this:

```python
STRONG = [(n,r,b) for n,r,b in STRONG if _exists_route(r) and b]
if len(STRONG) < 4:
    # fill from recent
    for pub, route, pay, title, ver in RECENT_CARDS:
        ...
```

Two of the four picks did not resolve. `noema-magazine` is a **stale slug** — the record
is `noema`, so a genuine top performer was being discarded over a spelling. And
`a-public-space-fiction` has **no record at all**: the export named a page this desk never
wrote up, and writing one up to fill the slot was never an option.

So the strip had only two real GSC cards, and the fallback silently filled the other two
from `RECENT_CARDS` — recently re-verified markets that the traffic data never mentioned —
under a heading citing Search Console and a position range of 4–13, each labelled "Top
performing". Before this batch those two slots held American Poetry Journal and After
Dinner Conversation; after it they held Chicken Soup for the Soul and The Fiction Desk.
The cards changed every time any record anywhere was re-verified, which is how a false
claim about search performance stayed invisible: it never looked stale, it just rotated.

This is the same defect class as the typed `147/147` literals in the Phase 18 report — a
number or label on a page that is not derived from the thing it claims to describe — and
the same rule applies: **derive it, and raise rather than fall back.**

The fix:

- `_PICKS` corrected to the slugs that exist: `the-sun-magazine`,
  `longreads-personal-essay`, `noema`. `a-public-space-fiction` is removed with its reason
  recorded in the source, not quietly dropped.
- The `fill from recent` fallback is **deleted**. A pick that has no record, no route or no
  pay blurb now raises `SystemExit` naming the slug, so a stale pick can never again be
  papered over by an unrelated market.
- The strip prints three cards, all three genuinely from the export. Three is fewer than
  four, and that is the honest result: the desk has dossiers for three of the pages GSC
  named. "POS 4–13" still describes them — a subset of a group whose positions fall in a
  range falls in that range.

If the fourth slot should be filled, the way to fill it is to research A Public Space at
its own guidelines page and add it as a record, which is Stage 1 work and belongs in a
markets batch with its own evidence — not in a fallback that relabels whatever was checked
most recently.

## State after the batch

| | before | after |
|---|---|---|
| build warnings | 1 (six records) | **0** |
| `submissionStatus` mix | open 214 · upcoming 27 · closed 23 · rolling 9 · unknown 8 · deadline 7 | open 212 · **upcoming 30** · **closed 25** · rolling 9 · unknown 8 · **deadline 4** |
| records `lastVerified` 2026-10-01 | 33 | **39** |
| "Top performing" cards on the home page that came from GSC | 2 of 4 | **3 of 3** |

Both totals are 288. The writing calendar followed the records rather than being edited
separately: it now carries Granta · 2026-12-01, Aurealis · 2027-02-01, 32 Poems ·
2027-02-01, Chicken Soup · 2026-11-30, Ecotone · 2026-09-30 and Fiction Desk ·
2026-09-30, each derived from the record it came from.

Two build passes exit 0 and `npm test` exits 0 across all 16 steps, with the WARNINGS
block absent from `validate-site-quality` for the first time since the merge.
