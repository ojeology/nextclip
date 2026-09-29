# Batch X — 36 film pages given depth sections

**Date:** 2026-09-29 · **Commit:** `0169124` · **Deploy:** live

---

## Result

The next 36 thinnest indexable film pages with no depth section. All 36 now carry
one, and **every one crossed the 600-word floor.**

| | Before | After |
|---|---|---|
| Section | none | 36 sections |
| Words | 489–499 w | **742–783 w** |
| Under 600 w | 36 of 36 | **0 of 36** |

**Catalogue after batch X:** 719 indexable film pages · **384 with a depth section**
(was 348) · **335 without** (was 371).

---

## Live verification

Six spot-checks on the real domain:

| Page | Words | Depth | Ad band |
|---|---|---|---|
| `vinland-saga` | 762 | ✅ | ✅ |
| `cowboy-bebop` | 763 | ✅ | ✅ |
| `sherlock` | 759 | ✅ | ✅ |
| `moon` | 746 | ✅ | ✅ |
| `rashomon` | 744 | ✅ | ✅ |
| `gladiator` | 761 | ✅ | ✅ |

New headings confirmed by direct string match on the live pages — e.g.
`<h2>A Revenge Story That Argues Against Itself</h2>` on vinland-saga,
`<h2>Four Witnesses, Four Films</h2>` on rashomon. The Adsterra band is present
on film pages and absent on `/jobs/`.

---

## Three defects the module's own asserts caught

All three were found **before** injection, which is the point of writing the
checks into the data module:

1. **`bridemaids`** — a typo that failed the route-exists check. Would have
   silently skipped the page.
2. **Three staged "desk note" rows** whose slugs carried a `#`
   (`aquaman-2#split`, `aquaman-2#hold`, `money-heist#wait`). Those are not
   routes, so the injector would have found no file for them and quietly done
   nothing. Dropped rather than shipped as dead weight.
3. **`the-falcon-winter-soldier`** was in the plan and then omitted from the
   rows entirely. Added back before the batch ran.

Without the route assertion, all three would have shipped as a batch that
looked complete and wasn't.

---

## Uniqueness — checked against the whole catalogue

Verified against every sibling module, not just within the batch:

| Check | Result |
|---|---|
| Unique h2 headings | **36 / 36** |
| h2 collisions vs **1,976** existing headings | **0** |
| Unique lead-ins | **216 / 216** |
| Lead-in collisions vs **3,533** already in use | **0** |
| Slug collisions | **0** |

**Fourteen labels had to be renamed.** Six repeated inside the batch
(`The ending` ×3, `The ensemble` ×2, and so on) and eight collided with batches
U/V/W and the earlier modules (`The sequel`, `The soundtrack`, `The tonal range`,
`Which version to watch`, `The heist structure`, `The three leads`, …).

Each rename was **scoped to a single row's span**. A global replace would have
hit the wrong sections, because the same label legitimately appears in several
films.

---

## Content grounding

Sections stay on documented ground: who directed it, what it adapts or follows,
which industry made it, and what is publicly recorded about its production and
release.

Where a title has a famous cliffhanger or a contested ending, that is **named as
such rather than resolved with invented detail** — Baahubali 2 is described as
existing to answer the first film's question, and the desk declines to settle
Gladiator vs Goodfellas. Reception is reported only in the broad terms the
record supports. No numbers, awards or quotes are asserted that the desk cannot
stand behind.

The batch is unusually mixed: studio sequels, prestige drama, anime, Nollywood,
Korean and Spanish television, plus two canon titles (Rashomon, Casino).

---

## Verification chain

| Check | Result |
|---|---|
| Injector | 72 injected (36 × 2 trees), **0 problems** |
| `npm run build` | exit 0 |
| Python compat | clean, 214 files |
| Validator | `ok: true`, indexable 2584 = sitemapUrls 2584 |
| Ad band on noindex stubs | **0** |

---

## What's next

**335 pages** still have no depth section. At 36 per batch that is roughly nine
more batches, then a second pass for anything still under 600 words.

Next 12 in the queue:

```
yellowjackets · barry-lyndon · bhool-bhulaiyaa-3 · citizen-vigilante
kingsman-the-secret-service · … (all ~500 w)
```

Note for the next census: seven entries in the film tree (`baahubali`,
`grand-budapest`, `spider-verse-2`, `everything-everywhere`, `half-yellow-sun`,
`living-in-bondage`, `mi-final-reckoning`) look like 20–26 word pages, but they
are `noindex,follow` stubs — correctly excluded from indexing **and** from ads.
Any census must filter on the robots meta tag or it will misreport them as
broken content.
