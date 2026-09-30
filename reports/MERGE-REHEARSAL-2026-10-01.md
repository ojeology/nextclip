# Merge rehearsal — batch 14, 1 October 2026

Second and final rehearsal before merging `bryme/markets-batch-verified` into `main`.
Replaces `MERGE-REHEARSAL-2026-09-30.md` as the operative document; the earlier one
predates batch 14 and the resolver fix.

Everything below was done in a **full scratch clone** (`/home/user/build/rehearse`), never in
the research clone, which has no `public/` and no article tree and therefore cannot build
or run a single gate. All numbers are from that clone at the commit named.

| | |
|---|---|
| merge base | `9da69b439` |
| branch | `dd417cd` — 23 commits ahead of base |
| main | `c61f1ff46c` — 8 commits ahead of base |
| merged tree | `3c78b15542` (rehearsal commit, never pushed) |
| conflicting files | `content/opportunities.json` only |

## 1. The resolver was broken by the move into `scripts/`

`scripts/resolve-main-merge.py` derived its paths from `Path(__file__).resolve().parent`.
Written at the repository root, that was the root; committed under `scripts/`, it silently
became `scripts/`, so `OPPS` pointed at `scripts/content/opportunities.json`, which does not
exist. The first run of the real merge would have died on a bare `FileNotFoundError` — the
safe direction, but only by luck. Fixed in `dd417cd`: the root is now the parent of the
script's directory, asserted at import (`ROOT = /home/user/repo`, `OPPS` exists).

This is the second defect in this rehearsal cycle found only by re-running the script from
where it is actually committed.

## 2. The merge itself

Only `content/opportunities.json` conflicted. Base 147 records, main 147, branch 261, merged
**261**. Resolution is per record, three-way: the branch's field where the branch moved it
off base, otherwise main's.

The resolver prints "all checks passed", and that is not evidence — an earlier version of
this script printed the same line while silently reverting three records' `howToSubmit`. So
the merged document was checked independently, against the three inputs, on four properties:

| property | result |
|---|---|
| P1 no record lost, none invented (union of both sides) | lost 0, extra 0 |
| P2 per-field three-way across all 147 shared records | **0 violations** |
| P3 114 branch-only records present and byte-identical to the branch | pass |
| P4 six batch-14 records present and intact | pass |

261 = 147 main + 114 branch-only. The three records the old resolver had damaged
(`cracked`, `whatculture`, `statement-africa`) all carry `howToSubmit` and their
`2026-09-30` verification dates.

## 3. Branch-local blind spot, now closed

The branch's publication page draws **seven** docket rows and never renders
`simultaneousNote`. Main's `cd84236d43` adds the eighth row that prints it. So the six notes
written in batch 14 could not be verified on the branch at all — the same blind spot that hid
three `" ."` quote defects in batch 13.

Verified on the merged tree, in the six generated pages:

| slug | note renders | label correct | read-date | format |
|---|---|---|---|---|
| american-poetry-journal | yes | yes | 2026-10-01 | ok |
| after-dinner-conversation | yes | yes | 2026-10-01 | ok |
| american-short-fiction | yes | yes | 2026-10-01 | ok |
| bayou-magazine | yes | yes | 2026-10-01 | ok |
| bennington-review | yes | yes | 2026-10-01 | ok |
| blackbird | yes | yes | 2026-10-01 | ok |

Label check is main's `You may submit elsewhere at the same time`; format check is
`<sentence> — <url> (read <date>)`. A punctuation sweep flagged
`after-dinner-conversation`; inspection showed a legitimate ellipsis inside the quoted
sentence (`Yes, but... It is one thing…`) and CSS inside a `<style>` block, i.e. a false
positive of the sweep, not a defect.

**All six batch-14 notes are therefore verified.** Nothing else in the branch is
unverifiable branch-locally.

## 4. Gates on the merged tree

`npm install` (playwright only, no runtime deps), then:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` | exit 0 |
| `verify:allowlist` | exit 0 |
| `verify:titles` | exit 0 |
| `verify:dockets` | exit 0 |
| `validate:money` | exit 0 |
| `validate:hometools` | exit 0 |
| `audit_dockets.py` | 261 publication pages, **8 docket rows per page**, 1016 unanswered rows, 127 rankings, **0 problems** |

Docket rows are main's 8, not the branch's 7 — the branch must not be allowed to win this
file. In the first pass of this rehearsal the branch's `build-writing-first.py` was copied
over the merged one by hand and `verify:dockets` immediately failed with
`7 docket rows, expected 8` on every page. That is the correct, loud failure; the merge
itself takes main's version cleanly.

## 5. Discoverability of the six new records

No orphans. Each of the six is linked from the desk index, its genre page(s) and
`what-changed/`; `american-poetry-journal` is additionally on
`/writing-opportunities/remote/` because its guideline states it is open internationally.
The other five are filed `International` in `pub-countries.json` and, correctly, carry no
country page.

## 6. `_atlas_items` — investigated, and it is not a defect

The atlas page draws one tile per country group in the data and links to
`COUNTRY_PROFILES[iso].slug or iso.lower()`, while a country page is only written when a
profile exists. On the branch's file the tile list is unfiltered, which looks like it can
produce a tile pointing at a page nobody generated. It was investigated as a possible
blocker, and the conclusion is the opposite of the working assumption:

**The unfiltered tile is deliberate.** The comment on `COUNTRY_PROFILES["PT"]` records the
same class of bug found earlier with `lisbon-literary-review`: a Portugal record produced a
tile pointing at `/writing-opportunities/pt/`, which nothing generated, and
`validate-site-quality.js` (inside `npm run validate`) caught it as a missing local target.
The decision recorded there is explicit — *"Adding the profile is the fix rather than
suppressing the tile: BRYME tracks a Portugal-based publication, so Portugal is a real desk
and was simply never given its page."*

Reproduced end to end during this rehearsal by filing one record under `NL` (a real country
with no profile):

- `build-writing-first.py` writes the tile, and the built page renders a link to
  `/writers/writing-opportunities/nl/`;
- no such page exists — a genuine dead link;
- `npm run validate` **fails**: `missing local target /writers/writing-opportunities/nl/`.

So the tile is a tripwire that a desk is missing its page, and the gate catches it at build
time. A filter on `_atlas_items` was drafted, tested as output-neutral today (the atlas page
was byte-identical, since every country currently in the data has a profile) and then
**discarded**: it would hide a real desk from the atlas and disable the tripwire. Nothing
was committed.

Consequence for batch 15: **any new base country needs a `COUNTRY_PROFILES` entry in the
same commit as the record**, or `validate` fails and the run stops. That belongs in the
batch checklist.

Related trap found while chasing this: `write()` puts pages at the **repository root**
(`writing-opportunities/index.html`), and the `writers/…` and `public/…` copies are produced
later by the copy step. Reading `writers/…` after running one script alone reads a stale
file from the previous full build and has already produced one wrong intermediate
conclusion in this rehearsal. Verify against `public/` after a full build, or against the
root path for a single script.

## 7. Environment hazard, recorded

`/tmp` is a 993 MB tmpfs and a full clone plus a build fills it. When it filled mid-session,
`npm run build` returned exit 1 with an **empty log**, and later a python run returned exit
120 with an empty log — both because the log file itself could not be written, not because
of anything in the tree. Scratch work now lives in `/home/user/build/`, which is
snapshot-excluded and therefore does not count against the workspace cap. If a gate fails
with empty output, check `df -h /tmp` before debugging the code.

## 8. What remains before the real merge

- Re-rehearse immediately before merging if main has moved; this document is only valid
  against `c61f1ff46c`.
- Merge procedure: fetch main, merge into the branch, run `scripts/resolve-main-merge.py`
  from the repository root (it works from anywhere now, but the root is where the paths it
  touches resolve), commit, then build and run all six gates plus `audit_dockets.py`.
- The branch must contribute no docket-row change; take main's `build-writing-first.py`.
- Verification must run on the merged tree, never branch-locally: the branch cannot render
  `simultaneousNote` at all.
- `research/` is still untracked and still wiped by snapshots. Nothing the merge depends on
  lives there.

## 9. Verdict

The merged tree builds and passes every gate with 261 records, 8 docket rows and 0 problems.
The one conflict resolves correctly under an independent three-way check, not merely the
resolver's own report. The six batch-14 notes render correctly with the right label and
read-date. The `_atlas_items` question is closed as by-design, with the batch-15 consequence
written down.

**The branch is ready to merge into main on the verification standard set for it.**
