# Phase 19 — Global publication expansion: a staged roadmap, proposed for review

Written 2026-10-01 against commit `c31cecfe225` and the tree it builds. Every number
here was measured from `content/opportunities.json`, `content/hub/pub-countries.json`
or the built pages on that date; nothing is carried over from an earlier report.

Item 6 of Phase 19 asks for this document rather than another batch of pages:

> Produce this as a long-form, staged roadmap (not a single batch of new pages) — the
> agent should propose the roadmap for review before mass-producing any new
> publication pages, in keeping with the "no mass-generation" rule.

So this is a proposal. It does not authorise itself, and no stage below begins until
the composition question in §7 is answered.

---

## 1. Where Phase 19's six items actually stand

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | Expand market by market, tier-one first, then widen | **In progress** | 288 records; batches 14–22 landed 2026-09-30/10-01. 712 short of the 1,000-market target the owner set. |
| 2 | Same verification standard for every new record | **Fixed this commit; backlog remains** | Audited all 288 against the nine named fields. Eight present on 288/288. Reading periods was recorded on 85 and rendered on **none** — now a ninth docket row. See §4. |
| 3 | A clear path for complete beginners | **Done** | `/writers/start/` numbered path, `/writers/find/` purpose-finder, first-publication and new-and-emerging browse pages. |
| 4 | Tag by experience level and country/region | **Done, two gaps found** | Experience: 47 stated / 91 read-and-silent / 141 not yet assessed / 9 unread = 288. Country: 13 base tiles + a remote tile. Gaps: one mis-folded genre tag (fixed) and one genre with no browse page (open, §5 Stage 0.4). |
| 5 | Sequence expansion from Search Console signal | **Blocked on the owner** | The only export on file is 20–29 Sep: 52 clicks, 8,075 impressions, 0.64% CTR, average position ~35. Too small and too old to sequence by. Owner's instruction on 2026-10-01 was to wait for more October data. |
| 6 | This roadmap, for review before mass production | **This document** | — |

---

## 2. The database as it measures today

**288 records**, all on the writing desk.

By the publication's own base:

| Base | Records | | Base | Records |
|---|---|---|---|---|
| remote / base not established | **125** | | Nigeria | 5 |
| United States | 94 | | India | 5 |
| United Kingdom | 22 | | Kenya | 2 |
| Canada | 18 | | South Africa · Nepal · Namibia · Ireland · Germany · Portugal | 1 each |
| Australia | 11 | | | |

Tier-one as the brief defines it (US, UK, CA, AU, IE) is **146 of 288 — 51%**. The
brief says tier-one is "the starting wave of a global build, not the ceiling". Measured
against that, the database is still at the starting wave.

**Payment.** 171 of 288 state an amount. Currencies: USD 153, GBP 19, CAD 17, AUD 9,
NGN 5, EUR 2, INR 1. The other 117 either state that they pay without publishing a
figure or say nothing about pay; the docket distinguishes those two cases rather than
merging them.

**Genre**, after normalisation into the 13 canonical buckets the filters use:

fiction 180 · poetry 156 · essays 113 · creative-nonfiction 110 · reviews 46 ·
journalism 41 · articles 32 · analysis 29 · interviews 24 · personal-essays 23 ·
opinion 21 · translation 17 · other 13

**The honest backlogs.** Each of these is published on the pages as a gap rather than
hidden, which is the point of recording them here:

| Field | Recorded | Missing | What the page says when missing |
|---|---|---|---|
| Reading period | 85 | **203** | "Not yet assessed" (194) or "Not known" (9, guideline unreadable) |
| Experience question put to the guideline | 147 (47 state a stage, 91 read-and-silent, 9 unreadable) | **141** | "Not yet assessed" |
| Guideline readable at all | 279 | **9** | "Not known" |
| Simultaneous-submission note (the quoted sentence) | 170 | **118** | the policy value without its verbatim evidence |
| Submission email | 66 | 222 | not a gap — most markets use a portal |
| Editor-experience note | 275 | 13 | — |

Also open: the build warns that **6 records have a passed deadline but a live status** —
`chicken-soup`, `the-fiction-desk`, `granta`, `aurealis`, `ecotone`, `32-poems`. The
renderer flips them to closed rather than presenting a lapsed window as open, so no page
lies; but the underlying records need a human re-read.

And one number that is easy to misread: the eligibility filter offers
**"Eligibility not stated — 177"**. That is not 177 missing fields. All 288 records
carry an `eligibility` object; 177 of them record that the guideline states no
nationality restriction either way. The field is present and the answer is documented
silence — which the site refuses to render as "open worldwide".

---

## 3. The gap between this and what the brief asked for

The brief names the widening explicitly:

> …then widening deliberately to other English-language and internationally-submittable
> markets (for example: India, Nigeria, South Africa, Philippines, and other countries
> with active English-language literary and freelance markets)

Measured against that list: **India 5, Nigeria 5, South Africa 1, Philippines 0.** The
Philippines has no records at all. Three of the four named countries have five or fewer.

The owner is in Lagos, the GSC export shows real impression volume from the US, UK and
India, and a Nigerian writer is the reader this desk is most useful to — yet the
database carries 5 Nigerian publications against 94 American ones. That is the single
largest divergence between the stated intent and the measured state, and it is the
argument for Stage 2 below being sequenced before the tier-one tail is finished.

The 125 records with no established base cut the other way. There are 13 country browse
pages — australia, canada, germany, india, ireland, kenya, namibia, nepal, nigeria,
portugal, south-africa, united-kingdom, usa — covering the 163 records whose base is
known; the other 125 sit on a single `/writing-opportunities/remote/` page. For a site
whose money content carries a jurisdiction-clarity rule, "we could not establish where
this publication sits" is a real limitation and is labelled as one — but it also means
country-level expansion cannot be measured accurately until those bases are established.

---

## 4. The verification standard, as a checklist (item 2)

Every record added or changed under this roadmap carries all nine fields the brief
names, read from the publication's own guideline page. The right-hand column is what
the page must say when the answer is not available — because the failure mode this desk
keeps finding is not a missing field, it is a missing field that renders as though the
publication had been asked and said nothing.

| # | Field | Dataset key | Counts as filled | When it cannot be filled |
|---|---|---|---|---|
| 1 | Genre | `writingTypes` | ≥1 tag **present in `WRITING_TYPE_MAP`** | never — and an unmapped spelling now stops the build (§5, Stage 0.6) |
| 2 | Submission method | `applyMethod`, `applyUrl` | the route the guideline states | "Not stated" only where the guideline is silent |
| 3 | Payment | `pay` | an amount, **or** a display saying the market pays without publishing a figure | null amounts with an honest display; never an invented typical rate |
| 4 | Reading periods | `deadline` | `{display}` read from the guideline, plus `date`/`openingDate` where the page gives one | "Not yet assessed" (ours) or "Not known" (guideline unreadable) — **never** "Not stated" |
| 5 | Response times | `response` | a band plus the label the guideline supports | "Not stated" where the guideline is silent |
| 6 | Simultaneous submissions | `simultaneousSubmissions` + `simultaneousNote` | the policy **and** the verbatim sentence it was read from | "Not stated" / "Not known", with the note explaining the risk either way |
| 7 | International eligibility | `eligibility` | `mode` + `summary`; `notStated: true` where the guideline says nothing | documented silence — never promoted to "open worldwide" |
| 8 | Last-verified date | `lastVerified` | the date a human opened the guideline | never absent |
| 9 | Primary-source link | `sources[]` | ≥1 official URL, with the sentence used | a record with no official source is not added |

Three labels, and the distinction between them is the whole discipline:

- **"Not stated"** — the guideline was read and is silent. The publication's gap.
- **"Not yet assessed"** — BRYME has not put the question to the guideline. Our gap.
- **"Not known"** — the guideline could not be opened at all, and no archive carried it.

An absent field must never render as any of the three by accident. Twice now the tree
has done exactly that: 141 records with no `experience` key each asserted "the guideline
sets no experience requirement", and 98 records asserted "BRYME has read this
publication's guideline for pay, route and deadline" while recording no deadline. Both
are fixed; both are the reason the checklist above has a right-hand column.

---

## 5. The staged plan

Batch size throughout is **10–15 records**, which is what batches 14–22 sustained while
still reading every guideline page and writing a per-batch report. Larger batches are
how fabrication creeps in.

### Stage 0 — Retire the backlog on what already exists (no new records)

The argument for doing this first: a new record costs the same nine fields as an old
one, so adding 712 markets on top of 203 unrecorded windows does not grow coverage, it
grows the gap. Stage 0 is also the cheapest work available — the guideline pages are
already identified and 279 of them are already known to be readable.

| | Task | Size | Done when |
|---|---|---|---|
| 0.1 | Re-verify the 6 records with a passed deadline and a live status | 6 | the build warning clears |
| 0.2 | Record reading periods for the 194 "Not yet assessed" | ~13 batches | the docket's ninth row shows a window or a documented silence on every page |
| 0.3 | Assess the experience question for the 141 | ~10 batches | `experienceNotAssessed` is empty; the four-way accounting still sums to 288 |
| 0.4 | Add the missing **translation** browse page | 17 records, 1 route | `/writers/writing-opportunities/translation/` exists; `tslug` gains the entry |
| 0.5 | Establish a base for the 125 remote/unstated records **where the guideline states one** | ~9 batches | the atlas tiles more than 163; records with no stated base stay in "remote" and say so |
| 0.6 | *(done this commit)* Genre tags: `humour` was unmapped and silently folded into "other"; unmapped tags now raise | — | — |

0.4 is a genuine item-4 gap: `MIN_TYPE_PAGE` is 8 and translation carries 17 records,
but the browse-page map omits it, so those 17 markets are reachable only through the
filter dropdown and not through the browse-path network. Opinion has a page with 21.

### Stage 1 — Tier-one depth (US, UK, CA, AU, IE)

The brief's priority, and the tier the existing search signal supports. 146 today.
Target **300** — roughly 11 batches. Focus on paying markets the current filter cannot
yet show: ones that state a figure (the 117 that do not are disproportionately here),
and genres thin in the mix — translation (17), interviews (24), analysis (29).

### Stage 2 — The named widening (India, Nigeria, South Africa, Philippines)

Sequenced **before** the tier-one tail is finished, for the reason in §3. Targets:

| Country | Today | Target | Note |
|---|---|---|---|
| Nigeria | 5 | **40** | The owner's own market and the desk's most useful audience. Includes NGN-paying markets, which the cross-currency ranking rule already protects from being compared to USD figures. |
| India | 5 | **40** | GSC shows real impression volume from India. English-language literary and freelance markets. |
| South Africa | 1 | **20** | Named in the brief; currently a single record. |
| Philippines | 0 | **20** | Named in the brief; currently none at all. |

~12 batches. Every record still carries all nine fields, and a market that pays in a
local currency records that currency rather than a converted headline.

### Stage 3 — Other English-language and internationally-submittable markets

Kenya (2), Nepal (1), Namibia (1), Germany (1), Portugal (1) today, plus Ireland,
Scotland, Wales, Singapore, Ghana, Uganda, Zimbabwe, Trinidad, Jamaica, Malaysia,
Pakistan, Bangladesh, Sri Lanka, Egypt, Morocco, Brazil (English-language outlets),
Japan (English-language outlets), and the Nordic English-language magazines.
Target **150**, ~11 batches, ordered by whether they accept international submissions
rather than by country size.

### Stage 4 — Non-English and multilingual submissions, where they exist

The brief's last widening, and the one that needs a decision before it starts: whether
a market that publishes in Portuguese or accepts bilingual work belongs on an
English-language desk at all, and if so how the record states the language requirement
so a writer is not misled. Target **50–100**. Not scoped beyond that until Stage 3 is
measured.

### Stage 5 — Re-sequence from search signal (item 5)

Deferred by design. When a fresh Search Console export exists, Stages 1–4 get re-ordered
by query patterns and countries already showing impressions rather than by the brief's
example list. The owner's instruction on 2026-10-01 was to wait for more October data,
so nothing here assumes an export arrives before Stage 2.

**Total: 288 → ~1,000**, in 45–50 batches of 10–15, with Stage 0's ~35 batches of
backlog work interleaved so the gap closes as the database grows rather than after it.

---

## 6. What every batch must do to land

This is the procedure batches 14–22 followed, restated so a future batch cannot quietly
drop a step. `reports/MERGE-REHEARSAL-2026-10-01.md` is the authority on merging a
branch of them.

1. Read the publication's **own** guideline page. Store the raw text under
   `research/rebuild/raw/<slug>.txt`. No listicle, no social post, no inference.
2. Fill the nine fields in §4. Where a value cannot be read, record the gap in the
   vocabulary of §4 — never a plausible substitute.
3. Add via `scripts/add-batchNN-<date>.py`, which writes the record and the country
   entry together.
4. Update `content/index-allowlist.json`; run `./sync-sde.sh`; build **twice** (the
   discovery step validates the previous tree, so a first pass with new routes is not
   yet a valid tree).
5. Gates, all exit 0: `verify:allowlist`, `verify:titles`, `verify:dockets`,
   `validate`, `validate:money`, `validate:oppfilter`, `validate:browser`,
   `validate:contrast`, `check:links`, plus `audit_dockets.py` at 9 rows per page and
   0 problems.
6. Write `reports/BATCHNN-MARKETS-<date>.md`: the field/sentence table, the judgement
   the record makes where the guideline was ambiguous, and the gate results. Batch 22's
   report is the model — it names the two wrong answers that were available and says
   why neither was taken.
7. Never claim a record is verified beyond what the cited sentence supports, and never
   rank a figure across currencies.

---

## 7. Decisions this roadmap needs from the owner

1. **Composition.** The plan above puts Stage 2 (Nigeria, India, South Africa,
   Philippines) ahead of finishing the tier-one tail, because the brief calls tier-one
   "the starting wave, not the ceiling" and because the named countries are at 5, 5, 1
   and 0. If the search signal should lead instead, Stage 1 comes first and Stage 2
   waits for the GSC export.
2. **Stage 0 first, or interleaved?** Recommended: interleaved, one backlog slice per
   expansion batch, so coverage and completeness grow together. The alternative is to
   freeze expansion and close all 203 reading periods first, which is faster overall but
   adds nothing new for several weeks.
3. **The translation browse page (Stage 0.4).** A new route, so it needs the allowlist
   and two build passes. Small and uncontroversial, but it is a new URL and the standing
   rule is no casual URL changes — this one is an addition, not a change.
4. **Stage 4's language question.** Whether non-English markets belong on this desk at
   all, and how a language requirement is stated if they do.
5. **Hosting**, which is not Phase 19 but gates how often all of this can be deployed —
   see the separate Cloudflare assessment.

---

## 8. What this roadmap deliberately does not do

- **No mass generation.** Every record comes from a read guideline page, in batches of
  10–15, with a report.
- **No fabricated field.** A rate, date, window or citation that cannot be read is
  recorded as unread, in the vocabulary of §4.
- **No deletion for size or traffic.** Nothing is removed to make a number look better.
- **No casual URL changes.** New routes are additions with an allowlist entry; existing
  routes keep their URLs even where a date is baked into the path.
- **No cross-currency ranking.** A figure in NGN is never ranked against one in USD.
- **No claim of perfection.** Stage 0 exists because 203 records are missing a field,
  and this document says so on its first page.
