# Batch 16 — eight paid markets, read 1 October 2026

Batch 16 continues the pw.org backlog on the side branch. Eight new records, each read off
the publication's **own** guidelines page on the desk date 2026-10-01. Raw text of every
page is under `research/rebuild/raw/<slug>.txt`.

| | |
|---|---|
| records added | 8 |
| dataset after batch | **272 records** |
| allowlist | 639 routes, reviewed 2026-10-01 |
| gate results | build + all six gates exit 0; 272 publication pages, 0 problems |
| new base countries | none — US, UK and International all exist |

## 1. A method fix that changed this batch's candidate list

The crawler names its files with underscores (`colorado_review`); records use hyphens
(`colorado-review`). Excluding already-shipped markets by exact slug match therefore treats
every shipped market as new, and the "unshipped" pool looked 30-odd markets bigger than it
is. Normalising before the exclusion (`_` → `-`, strip a trailing `_0`) cut the real candidate
list to **18 pages with rate language**, of which eight held up. Batches 14 and 15 were read
from the same pool; the leak was in the triage, not in their records.

## 2. The eight markets, with the sentence each figure came from

| market | rate | key sentence |
|---|---|---|
| **Booth** | $50 flat, any length | "We pay $50, regardless of length. This will be issued via PayPal after the online publication of your work." |
| **Chicago Review of Books** | $25 reviews/interviews; $75 features | "Currently, we are able to pay $25 for reviews and interviews and $75 for features." |
| **Consequence** | $20 poem (print), $30–$50 prose by length, $150 eight-page art spread, $50 online, $30 Substack | "Print: $20 per piece / Online Feature: $50 / Substack: $30"; prose "Print 1-4 pp: $30 / Print 5-10 pp: $40 / Print 11+ pp: $50"; art "Print: $150 for eight-page spread" |
| **Fahmidan Journal** | $35 per piece | "Payment is $35 per piece, delivered on publication." / "increased Contributor pay to $35 from Issue 24 (as of Sept 2025)" |
| **The First Line** | $10 poem, $25 nonfiction, $25–$50 fiction | "We pay on publication: $25.00 - $50.00 for fiction, $10.00 for poetry, and $25.00 for nonfiction (all U.S. dollars)." |
| **Free the Verse** | $10 issue poem; $20 Marginalia | issue route "What we pay / USD $10"; Marginalia "What we pay / USD $20" |
| **Invisible City** | $20 per published piece | "We compensate our contributors with a $20 honorarium per published piece." |
| **Fairy Tale Review** | $50 + two copies | "Contributors will receive two (2) copies of the issue and a $50 honorarium upon publication." |

## 3. The one record that says **no**

**The First Line refuses simultaneous submissions**, in as many words: *"just to be clear, we
do not accept simultaneous submissions."* Only eight records in the whole dataset are
`not-accepted`; the easy error is to score this as `not-stated` because a refusal is
unusual. It is recorded as a refusal with the sentence attached, because it is the single
most useful fact about the market for a writer planning a month of submissions.

It also states, in a passage about literary-magazine contests, *"We do not - nor will we ever
- charge a submission fee."* That is recorded as a fee policy, not a rate.

## 4. Rates that would be wrong if flattened

- **Consequence** pays by *route* (print / online / Substack) and, in print, by *page count*.
  A single "we pay $20–$150" would misstate every figure in it; the record keeps the ladder
  and the conditions quote it.
- **Free the Verse** pays two different rates for two different routes — a $10 issue poem and
  a $20 annotated Marginalia draft. Both are quoted; the range is real, not a fudge.
- **Booth** pays a flat $50 and charges **$3** to submit. The fee is the writer's cost, kept
  out of the pay display and named in the conditions.
- **Fahmidan** points to Submittable for submission prices. The page publishes no fee amount,
  so **no fee is recorded** — not even "there may be a fee".
- **Consequence** states no rights position, no fee, and no simultaneous policy; all three are
  recorded as not stated. **Chicago Review of Books** likewise states nothing about fees,
  rights or AI.
- **Fairy Tale Review** states no AI policy and no fee; both are recorded as absences.

## 5. Closures and windows

- **Fairy Tale Review** — the only window on its page ran **15 March to 15 July 2025**, and
  Volume 22 is published (Spring 2026). The record is `closed` and its deadline text says no
  later window is stated. No 2027 window is invented.
- **Consequence** — fall window 15 July to 15 October, open on the check date; translations
  and visual art are read year-round.
- **Fahmidan** — four seasonal windows; on the check date the open one is 15 September to
  15 December (Spring issue).
- **The First Line** — quarterly, next deadline 1 November 2026.
- **Free the Verse** — issue deadline 25 November 2026; Marginalia always open.
- **Invisible City** — "Submissions are open!" with no closing date stated; recorded `open`
  with no invented deadline.
- **Booth** — 1 September to 30 November, then 1 January to 31 March.
- **Chicago Review of Books** — rolling pitches, two to three months ahead of publication.

## 6. Base countries

Recorded only where the page itself places the publication:

| filed | markets | evidence on the page |
|---|---|---|
| US | Booth, Chicago Review of Books, Invisible City | "Butler" employees/students/MFA; "Chicago" (×23); "University of San Francisco" |
| UK | Fahmidan Journal | "London", "England", "United Kingdom" |
| International | Consequence, The First Line, Free the Verse, Fairy Tale Review | no location stated on the page |

Three markets were first drafted as US from a familiar masthead and corrected to
International when the page turned out to say nothing about where it is based. Guessing a
desk would put a record on a country page it has not earned.

## 7. Verification

Full scratch clone at the batch-16 tip `216ae0ca2e`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` | exit 0 |
| `verify:allowlist` | exit 0 |
| `verify:titles` | exit 0 |
| `verify:dockets` | exit 0 |
| `validate:money` | exit 0 |
| `validate:hometools` | exit 0 |
| `audit_dockets.py` | **272 publication pages**, 950 unanswered rows, 137 rankings, **0 problems** |

All eight new pages generated (`public/writers/writing/<slug>/index.html`, 30.4–31.2 KB).

**Not verified here, by construction:** the three batch-16 records that state a simultaneous
policy (`booth`, `fahmidan-journal`, `invisible-city` accepted; `first-line` not-accepted)
carry notes that the branch cannot render — it draws seven docket rows and main's eighth row
is what prints the note. They must be verified on the merged tree, as batch 14's six and
batch 15's three were.

## 8. Held, with the reason

| market | why |
|---|---|
| Frontier Poetry | pays $50 a poem on named routes ("partner poets", "New Voices") alongside a $20-fee challenge; each route needs its own reading before a rate is recorded |
| Half Mystic Journal | states US$20 a piece with an April 2027 close; needs a full reading of the submission routes |
| Infrarrealista Review | "$100 per review" — one route only; confirm scope before recording |
| Interrobang Lit | "a token payment of $3 through PayPal" — real, but needs the page read in full |
| CutBank | $250 is for **cover art**; not a prose rate |
| BlazeVOX | "10% royalties on fiction and poetry books" — a royalty model, not a per-piece rate |
| Harpur Palate | the only figure is the $19 **entry fee** |
| Berkeley Fiction Review, Blue Earth Review, i70 Review, Interim, Ink in Thirds, Fiction (0), Literary Fantasy Magazine, Emerald City Ghosts | contributor copies or no rate stated; unpaid as far as their pages say |
