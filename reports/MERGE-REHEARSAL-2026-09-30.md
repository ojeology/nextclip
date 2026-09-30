# Merge rehearsal — `bryme/markets-batch-verified` → `main`, 30 September 2026

The branch has never been merged. This rehearses it: a real three-way merge
against the current `main`, conflicts resolved, and the merged tree built and
validated end to end. **It merges cleanly, and the merged tree passes every
gate.**

| | |
|---|---|
| merge base | `9da69b439` |
| `main` | `c61f1ff46cf` — 8 commits past the base |
| branch | `10d4b02` — 17 commits past the base |
| conflicting files | **1** (`content/opportunities.json`) |
| records after merge | **255**, every one with `simultaneousSubmissions` and `experience` |
| merged-tree `npm run build` | **exit 0** |
| merged-tree `npm run validate` | **exit 0**, `"ok": true` |
| merged-tree gates | `verify:allowlist`, `verify:titles`, `verify:dockets`, `validate:hometools`, `validate:money` — **all pass** |
| merged docket rows | **8** — main's simultaneous-submissions row renders |

**This rehearsal found a real defect, and a bug in my own resolution script.**
Neither was visible from the branch. That is the case for rehearsing rather than
assuming.

---

## 1. The merge is almost entirely clean

Only one file conflicts. `content/index-allowlist.json`,
`content/hub/pub-countries.json`, `scripts/build-writing-first.py` and the rest
all auto-merge — which is the dividend from having kept main's builder untouched
(see `MERGE-PREP-2026-09-30.md` §4) instead of duplicating its docket change.

## 2. The one conflict, and how it was resolved

The branch's first 147 records are main's 147 **in the same order**, and the
branch appends 108 of its own. So the conflict is a whole-file one arising from
both sides editing the same array.

The two sides edited **different fields of the same records**:

| side | what it changed |
|---|---|
| main | `simultaneousSubmissions`, `simultaneousNote`, and experience fields — on its 147 |
| branch | `howToSubmit` + `lastVerified` on 3 of those same 147 records, plus 108 new records |

Taking either file wholesale loses real work: main's file drops 108 markets and
the 3 `howToSubmit` fixes; the branch's file drops Phase 4 and the experience
batch.

So the resolution is a **three-way merge per record**:

> for each field, if the branch changed it and main did not, take the branch's
> value; otherwise take main's.

Result: **255 records, 6 branch fields preserved** (3 records × `howToSubmit` +
`lastVerified`), and all 255 carrying main's `simultaneousSubmissions` and
`experience`.

The three records — `cracked`, `whatculture`, `statement-africa` — are worth
naming: each carries a branch finding that its publication has **no public
submissions page**, established by reading. Losing those to a careless `-X ours`
or `-X theirs` would have quietly reverted verified research.

## 3. The defect the branch build could not see

`verify:dockets` **passes on the branch** and **failed on the merged tree**:

```
FAIL copper-nickel:      space before punctuation: ' .'
FAIL peach-gcsu:         space before punctuation: ' .'
FAIL the-fictional-cafe: space before punctuation: ' .'
```

Three of my extracted sentences carried a space before the full stop. The cause
is the source markup: an inline tag sits where the full stop belongs, so
`requests to review books <em>.</em>` renders as `requests to review books .`.

On the branch this was invisible. The branch's docket draws seven rows and never
renders `simultaneousNote`, so nothing ever looked at those three strings.
`audit_dockets.py` only rejects the shape once **main's eighth row starts
printing the note**. A branch-local build therefore could not have caught it, no
matter how many times it was run.

Fixed by re-extracting the three notes from the three pages with a `tidy()` step
that tightens spacing around punctuation and changes nothing else. Each was
checked to differ from its previous value **only by whitespace before
punctuation**, so the quote is still the same words and still a slice of the
page. `apply-simultaneous-backfill.py` now carries the same `tidy()` plus a
guard that refuses to write any note matching `\s+[.,;:!?]`.

## 4. A bug in the resolution script — which reported success while losing data

The first version of `resolve-merge.py` had an **inverted condition**. It
preserved a branch edit when main had *also* changed the field — exactly
backwards — so it silently reverted all three records' `howToSubmit` to main's
empty array. And it printed:

```
merged records        : 255
  from main, phase 4  : 255
  branch fields kept  : 0
all checks passed; written
```

**`branch fields kept: 0` was the only tell, and "all checks passed" was
false.** The checks validated the `simultaneousSubmissions` rules and the record
count, but nothing asserted that the branch's own edits had survived — the one
thing the script existed to do.

Two fixes:

1. The comparison was corrected to preserve a branch edit when main left the
   field alone.
2. **The missing invariant was added**: every field the branch changed and main
   did not must still equal the branch's value in the merged output, or the
   script refuses to write.

The count went from `0` to `6` once the logic was right, which is what the
second check now guarantees.

## 5. The merged tree, verified

Run on `ef2205e` (the merge commit), in a scratch clone:

| gate | result |
|---|---|
| `npm run build` | **exit 0** |
| `npm run validate` | **exit 0** — `"ok": true`, indexable 2699, 255 records, 255 publication pages |
| `verify:allowlist` | **PASS** |
| `verify:titles` | **PASS** |
| `verify:dockets` | **PASS** — 255 pages, **8 rows each**, 0 problems |
| `validate:money` | **PASS** |
| `validate:hometools` | **PASS** |

The eighth row renders correctly for all three values on branch-only records:

| record | rendered |
|---|---|
| `brick-a-literary-journal` | "You may submit elsewhere at the same time" + the Brick sentence |
| `cholla-needles` | "Not accepted — send to one place at a time" + *"We answer quickly, and do not appreciate or accept simultaneous submissions."* |
| `epiphany-magazine` | "Not stated" + the honest silence explanation |

`cholla-needles` rendering as **"Not accepted"** is the payoff of not
classifying by keyword: the sentence contains the substring
`accept simultaneous submissions`, and a regex would have published it as a
**yes**.

## 6. What is left for the real merge

1. **`main` is moving.** It advanced from 5 commits past the base to 8 while
   this work was in progress, including `c61f1ff46cf` and `a7745a4e85e` on the
   same dataset. Rehearse again immediately before merging; the rehearsal is
   cheap (one conflict, one script) and the alternative is discovering a
   conflict in a 9,000-line JSON by hand.
2. **`_atlas_items` is still unfiltered** (`MERGE-PREP-2026-09-30.md` §1). A
   future country without a profile recreates the dead-link failure.
3. **`audit_dockets.py` row count differs by side** — 7 on the branch, 8 on
   main. The merge takes main's, which is what makes the eighth row render.
4. **`resolve-merge.py` should be reused, not re-derived.** It refuses to write
   unless the record count is preserved, no duplicates appear, every main record
   survives, every record has a valid `simultaneousSubmissions` with matching
   note rules, and every branch edit survives.

## 7. Reproducing this

```bash
git clone https://github.com/ojeology/nextclip.git && cd nextclip
git checkout -b rehearsal origin/bryme/markets-batch-verified
git merge origin/main            # one conflict, content/opportunities.json
python3 scripts/resolve-main-merge.py   # three-way per-record resolution + checks
git add content/opportunities.json && git commit --no-edit
npm run build && npm run validate
```

`resolve-merge.py` is committed as `scripts/resolve-main-merge.py`. It is a
one-off for this merge rather than a build step — nothing imports it and it does
not run in `npm run build` — but it is committed so the resolution does not have
to be re-derived, and because it refuses to write unless the merge is sound.
