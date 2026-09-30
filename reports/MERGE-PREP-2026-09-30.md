# Merge prep, 30 September 2026 — the two validator failures and the simultaneous backfill

Three pieces of branch debt cleared, all verified against a full build. This is
work on `bryme/markets-batch-verified`; it is not a market batch.

| item | before | after |
|---|---|---|
| `npm run validate` | **FAIL (2)** | **exit 0 — passes** |
| `simultaneousSubmissions` coverage | 7 of 255 records | **108 of 255** (the 147 shared with main are main's) |
| branch-only records with no simultaneous answer | 101 | **0** |

---

## 1. The `pt` dead link — a real page was missing, not a bad link

`validate` reported:

```
/writers/writing-opportunities/: missing local target /writers/writing-opportunities/pt/
```

The cause is in `build-writing-first.py`. Two pieces of code disagreed:

- `country_cards` renders a link **only** for a country in `COUNTRY_PROFILES`
  (`... if i in COUNTRY_PROFILES`), and
- `_atlas_items` renders a tile for **every** country present in
  `pub-countries.json`, linking to `COUNTRY_PROFILES[iso].slug` or falling back
  to `iso.lower()` — with no filter.

`country_page()` is only written for a country that has a profile. So any base
country without a profile produces a tile pointing at a page nothing generates.
Of the 14 base values in the data, 12 had profiles. The two without were `''`
(international, which produces no tile) and — the one that broke — **`PT`**.

`PT` comes from `lisbon-literary-review`, added by this branch. `PT` was also
missing from `COUNTRY_FLAGS`, so the country had neither a flag nor a page.

**Fixed by adding the country, not by hiding the tile.** BRYME tracks a
Portugal-based publication, so Portugal is a real desk that was simply never
given its page; suppressing the link would have made the dead link disappear
while leaving the gap. The alternative — deleting `lisbon-literary-review`'s
base — would have been a lie about where the journal is.

Verified as Portugal-based before recording it:
> "Rooted in the cultural crossroads of Lisbon, we serve as a bridge between the
> English- and Portuguese-speaking literary worlds"

> "The Lisbon Literary Review is a project developed with the support of the
> Futura Foundation, a community and space for reflection based in Lisbon"

Source: <https://www.lisbonliteraryreview.com/about> — read 2026-09-30.

The profile follows the `NA` / `NP` precedent for a country BRYME tracks but has
not researched:

```python
"PT": dict(slug="portugal", cur="EUR", spelling=None, dates=None, cv=None,
           quotes=None, guide=None, note="BRYME has not separately verified a
           Portuguese house-style profile. …")
```

`cur="EUR"` is a plain fact about the country. **No spelling, date, CV, quotation
or guide convention was invented** — those are left `None` and the note says they
are unverified, exactly as the Nepal and Namibia profiles do.

Two follow-on effects, both handled:

- The new page needed an allowlist entry. `sync-writing-allowlist.py` derives
  `/writing-opportunities/<slug>/` from `COUNTRY_PROFILES` and added
  `/writing-opportunities/portugal/`, taking the source allowlist to 626 routes.
- That, in turn, is what makes the indexable count match the allowlist again.

The latent bug is **not** fixed: `_atlas_items` is still unfiltered. A future
batch that adds a publication from a country with no profile will recreate this
exact failure. This is recorded rather than silently patched because the tile
behaviour is arguably right — the real fix is that adding a country should mean
adding its profile.

## 2. Poetry South — the record contradicted itself

`validate` reported:

```
/writers/writing/poetry-south/: "the American South" is in the record's eligibility
but not in data-open-to
```

The record said three things at once:

- `mode: "not-stated"`, `notStated: true` — "we do not know who this is open to"
- `includesRegions: ["the American South"]` — a place it accepts work from
- a summary explaining that the Southern emphasis is "an editorial emphasis
  rather than a restriction, because the magazine does not exclude writers from
  elsewhere"

Only the summary was right. `includesRegions` feeds `eligible_iso_set()`, which
decides which eligibility filters can find a record — and `"the American South"`
is a free-text phrase, the only non-canonical value in the whole corpus (every
other is a token such as `africa`, `uk`, `canada` or an ISO code). It could
never match a filter, and the validator was right to fail it.

Reading the publication's own page settled what the record should say:

> "Poetry South is an international journal that considers all kinds of poetry.
> Though we pay particular attention to writers from the South — born, raised, or
> living here — all poetry within our covers has a claim to the South because it
> is published here. The magazine has a tradition of including poets from other
> regions in the US and other countries."

Source: <https://www.muw.edu/poetrysouth/submit/> — read 2026-09-30.

So the page does **not** say nothing about geography. It says it is international
and includes writers from other countries. The record now reads:

- `mode: "worldwide"`, `notStated: false`, `includesRegions: []`
- a summary quoting both sentences, and stating that the Southern emphasis is
  editorial, not a restriction

`aiPolicy: "prohibited"` and `lastVerified: 2026-09-30` were already correct and
were left alone. The record now appears under "Open worldwide" rather than being
invisible to the country filters, which is the visible consequence of the fix.

## 3. The simultaneous-submissions backfill — 101 records read

Main's Phase 4 added `simultaneousSubmissions` / `simultaneousNote` to its 147
records. This branch predates that. After the merge, the 101 records this branch
added on its own would still have had no answer for the eighth question in every
publication docket — so this was a merge blocker, not a nicety.

**Only the 101 branch-only records were touched.** The 147 shared records were
left alone deliberately: main already carries Phase 4's values for them, and
writing our own would turn a clean merge into a conflict over 147 records that
are already answered. `scripts/backfill-simultaneous.py` takes an explicit
`--targets` list for exactly this reason, and `apply-simultaneous-backfill.py`
refuses to run without it.

Result, from reading all 101 guidelines pages on 2026-09-30:

| answer | records |
|---|---|
| `accepted` | **73** |
| `not-accepted` | **8** |
| `not-stated` (page genuinely silent) | **20** |

### Nothing was classified by keyword

Phase 4's commit records that keyword matching was wrong at nearly every step.
It was wrong here too, and reading caught it:

- **Cholla Needles** — *"We answer quickly, and do not appreciate or accept
  simultaneous submissions."* Contains the substring `accept simultaneous
  submissions`.
- **Hanging Loose** — *"We do not accept simultaneous submissions."*
- **Peach** — *"Because we do not accept simultaneous submissions…"* and later
  *"While Peach does not consider simultaneous submissions…"*
- **The New Verse News** — *"No simultaneous submissions."*
- **Stygian Lepus** — *"No simultaneous submissions, please, they will be
  disqualified."*
- **The Fictional Cafe** — *"submitted exclusively to us. We do not accept
  simultaneous submissions or requests to review books."*

Those six state a refusal while containing the positive substring, so they are
carried as an explicit list rather than a pattern. A seventh, **Foreign Affairs**,
states a presumption of exclusivity — *"Unless otherwise informed, we assume any
piece submitted to us is being offered exclusively…"* — and is recorded as a
refusal with the full sentence preserved so the "unless otherwise informed"
survives into the record.

**And one market refuses without ever saying the word:**

> "Material submitted to Modern Haiku is to be the author's original work,
> previously unpublished and **not under consideration by any other
> publication**, including Web-based journals."

A search for "simultaneous" reports Modern Haiku as silent. It is not silent. A
wide sweep across all 101 pages for `under consideration`, `other publication`,
`exclusive`, `concurrent` and similar phrasing found this one case and no others.

### A defect in this work, caught before it shipped

The first pass quoted a **heading** where a policy belonged. Cast of Wonders and
Pseudopod both have a section headed "Multiple and Simultaneous Submissions", and
the extractor glued that heading to the sentence beneath it, which was about
*multiple* submissions:

> ✗ "Multiple and Simultaneous Submissions We do not accept multiple submissions
> from an author at the same time."

The classification was right and the quote was misleading — which is exactly the
failure this desk exists to avoid, since the note is the evidence. The extractor
was rebuilt to rejoin wrapped sentences **without** gluing a heading to the next
line, and to prefer a sentence that reads as a policy. It now records:

> ✓ "We don't mind if you submit your story to us and other venues at the same
> time (simultaneous submission) unless our specific submission call says
> otherwise…" — Cast of Wonders

> ✓ "Simultaneous submissions are acceptable WITH DISCLOSURE." — Pseudopod

Every quoted note is machine-checked to appear verbatim in the saved page text:
**84 notes checked, 0 not verbatim.**

## 4. What the branch still cannot do, and why that is correct

**The eighth docket row does not render on this branch.** It renders on main.

`build-writing-first.py` on this branch contains no occurrence of the word
"simultaneous"; its docket draws seven rows (Payment, Length, Who can submit,
Response time, AI policy, Rights, Experience). Main's copy renders eight —
main's Phase 4 added both the field and the row:

```
"accepted":     "You may submit elsewhere at the same time"
"not-accepted": "Not accepted — send to one place at a time"
anything else:  "Not stated" + a gap entry
```

So the 101 records now carry answers the branch's own renderer ignores. That is
the right place to stop: main owns the docket change, and duplicating a builder
change across a diverged branch is how merges break. The data was written in
exactly the vocabulary and note shape main reads (`"<sentence> — <url>
(read <date>)"`), so the merge lights it up with no data change.

**Checked:** every value written is inside main's vocabulary
(`accepted` / `not-accepted` / `not-stated`) — none outside it.

## 5. Verification

Full build, 255 records, clean tree:

| gate | result |
|---|---|
| `npm run build` | **exit 0** |
| `npm run validate` | **exit 0** — `"ok": true`, indexable 2699 = allowlist 2699, 255 records |
| `verify:allowlist` | **PASS** |
| `verify:titles` | **PASS** |
| `verify:dockets` | **PASS** — 255 pages, 7 rows each, 0 problems |
| `validate:money` | **PASS** |
| `validate:hometools` | **PASS** |
| `validate:techhub` | `MODULE_NOT_FOUND` — missing dev dependency in this sandbox, not a data problem |

The two original `validate` failures are gone and no new ones appeared. This is
the first time this branch has passed `validate` cleanly.

## 6. Still outstanding for the merge

1. **`_atlas_items` is unfiltered** (see §1). Adding a country without a profile
   recreates the dead link.
2. **The docket row comes from main** (see §4). Nothing to do; recorded so it is
   not mistaken for a missing feature.
3. **`audit_dockets.py` expects a different row count on each side** — 7 here,
   and a `DOCKET_ROWS` constant on main. This will need reconciling at merge.
4. **The branch's `.git` is shallow** in this workspace, so `git fetch --depth 1
   origin main` is required before the tools that compare against main will run.
