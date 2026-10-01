# Batch 18 — The Maine Review, and the end of this pass

One new record, read off the publication's own guidelines page on 2026-10-01. Raw text
under `research/rebuild/raw/maine_review.txt`.

| | |
|---|---|
| records added | 1 (`maine-review`) |
| dataset after batch | **278 records** |
| allowlist | 645 routes, reviewed 2026-10-01 |
| gate results | build + all six gates exit 0; **278 publication pages**, 0 problems |

## 1. The market

| field | value | sentence |
|---|---|---|
| pay, prose | $25 per flash, $50 over 1,000 words | "Fiction and Nonfiction writers receive a $25 honorarium per published flash (1,000 words or fewer) and a $50 honorarium for work 1,001 words or more." |
| pay, poetry | $25 per poem | "Poets receive a $25 honorarium per published poem." |
| pay, artwork | $50 on publication | "Contributors are paid $50 upon publication." (artwork call) |
| writer's cost | $3 per submission | "we ask writers to pay a $3 fee per submission, of which we receive $1.86" |
| free route | 28 Sep – 5 Oct 2026 | "free submissions from September 28 to October 5 or until we reach our allowed free submission[s]" |
| windows | 1 Sep – 30 Nov now; three a year | "open for nonfiction, fiction, and poetry submissions from January 1–March 31, May 1–June 30, and September 1–November 30" |
| limits | prose ≤3,000 words or 3 flashes ≤1,000; poetry ≤3 poems, 5 pages | "One piece of 3,000 words or fewer … or three flash pieces no more than 1,000 words each" |
| simultaneous | accepted, withdraw at once | "We encourage simultaneous submissions, but please withdraw your submission immediately if it is accepted elsewhere." |
| AI | refused | "We do not publish AI-generated work. Such work will be automatically declined." |
| response | six months or longer | "Please allow us six months before querying." |
| rights | **not stated** | no rights language on the page |

The $3 is the writer's cost and is kept out of the rate. The free window is recorded
because a writer who can wait for it pays nothing — the same reasoning that keeps contest
fees out of the rate, applied in the writer's favour.

**Base country: none.** The page never states where the review is based; only its name says
Maine. It is filed International rather than placed on a country page it has not earned — the
same standard applied to three batch-16 records that were drafted US and corrected.

## 2. Why the batch is one record: the pass is finished

After the slug-normalisation fix from batch 16, the unshipped pool was re-triaged. The
newly fetched names carry no contributor-rate language on their pages as read:

| page | state as read |
|---|---|
| Mania, MAP Literary, Maudlin House, Ranger | readable, no rate stated |
| Marrow (143 chars), Massachusetts Review (159), Poetry Is Currency (162) | JavaScript walls — **not established**, never recorded as "unpaid" |
| Aaduna | "does not provide publishing honorarium" — unpaid |
| BlazeVOX | "10% royalties on fiction and poetry books" — a royalty model, not a per-piece rate |
| CutBank | $250 is cover art; writing submissions carry a $5 fee and no stated rate |
| Harpur Palate | $19 entry fee only |
| Emerald City Ghosts | "Do We Pay? Unfortunately, no." — unpaid |

The standing backlog rule applies: a market whose page states no rate is not recorded as
unpaid unless its own words say so, and a thin render is not evidence of anything.

**This is the end of this queue, not the end of the backlog:** the crawler was still running
when the batch shipped (620 detail pages cached, 305 read), so pages fetched after this point
can carry later batches. Nothing in the branch depends on them.

## 3. Verification

Full scratch clone at the batch-18 tip `e50a5d1abe`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` | exit 0 |
| `validate:money` / `validate:hometools` | exit 0 |
| `audit_dockets.py` | **278 publication pages**, 969 unanswered rows, 143 rankings, **0 problems** |
| new page | `public/writers/writing/maine-review/index.html`, 31,254 bytes |

**Not verified here, by construction:** the new `simultaneousNote` for `maine-review` does not
render on the branch, which draws seven docket rows. It needs the merged tree, where main's
eighth row prints the note.

## 4. Session total

| batch | records | markets |
|---|---|---|
| 14 | 6 | American Poetry Journal, After Dinner Conversation, American Short Fiction, Bayou, Bennington Review, Blackbird |
| 15 | 3 | Colorado Review, Gavialidae, The Fairy Tale Magazine |
| 16 | 8 | Booth, Chicago Review of Books, Consequence, Fahmidan, The First Line, Free the Verse, Invisible City, Fairy Tale Review |
| 17 | 5 | Frontier Poetry, Half Mystic, Infrarrealista, InterrobangLit, The Literary Fantasy Magazine |
| 18 | 1 | The Maine Review |

**23 records this session; 278 on the branch.** Every figure was read off the publication's
own page on the check date, and every gap — rights, fees, AI, timing — is recorded as a gap.
