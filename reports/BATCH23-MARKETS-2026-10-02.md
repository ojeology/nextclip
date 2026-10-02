# Batch 23 — two markets, and a prize kept apart from a rate

Two new records, read off each publication's own page. Both pages were **re-fetched on the
desk date 2026-10-02** and every figure re-checked against the saved text before recording.

| | |
|---|---|
| records added | 2 |
| dataset after batch | **290 records** |
| allowlist | 664 routes, reviewed 2026-10-02 |
| gate results | build + all gates exit 0; **290 publication pages**, 0 problems |
| note audit | 171 notes, 0 defects, verified on this tree |

## 1. Let me tell you a story — `let-me-tell-you-a-story`

| field | value | sentence |
|---|---|---|
| pay | $10 CAD per accepted story | "For our upcoming reading season, we offer $10 CAD per accepted story." |
| fee | none | "We never charge fees and we give each story careful attention." |
| length | under 1,000 words, one per writer | "One story per writer / Under 1,000 words" |
| title rule | must begin "Let me tell you a story..." | "Title must begin with 'Let me tell you a story...'" |
| window | 15 July – 15 August 2026 | "Call for submission: Flash fiction summer 2026 … the submission window runs between July 15 to Aug 15." |
| response | 1–3 months | "Response time: 1-3 months" |
| rights | first electronic + non-exclusive archive; all other rights with the author | "We ask for first electronic rights and the non-exclusive right to keep your story archived on our site. All other rights remain with the author." |
| AI | **not stated** | no AI language on the page |
| how to submit | email, no form | "Send to: lyw.write@gmail.com … We don't use a submission form" |

Currency is recorded as **CAD** because the page says CAD, not because of an assumption about
where it is published. **No base country is recorded** — the page names none. Status is `closed`:
the summer window ended six weeks before the read, and the record does not invent a next one.

## 2. The Lemonwood Quarterly — `lemonwood-quarterly`

This one needed care, because three different kinds of money sit on the same page.

| field | value | sentence |
|---|---|---|
| **rate** | $200 per published piece | "Every three months, ten stories or plays are selected for publication in that season's issue of The Lemonwood Quarterly. The authors are awarded $200 payment…" |
| **writer's cost** | $4.00 per submission | the window listing reads "…Contest $1000 — Ends on $4.00" |
| **prizes (context only)** | $1,000 fiction, $500 play, December final round | "…advances to the final round in December for consideration for the $1000 Charlotte Ann Porter Prize for Fiction" |
| limits | 2,000–10,000 words; fiction or plays only | "We are looking for superbly written stories and play pieces between 2,000 and 10,000 words." |
| eligibility | worldwide | "We welcome and encourage submissions from writers of every gender, age, race, ethnicity, sexuality, and nationality…" |
| AI | refused | "Please do not send us work that includes machine-generated or AI text." |
| rights | first worldwide electronic; non-exclusive online; author keeps copyright | "…includes the following rights: First worldwide electronic publication rights; non-exclusive online rights on our website, and other limited rights. Copyright is retained by the author." |
| response | within 30 days of the window deadline | "We respond to all submissions within thirty days of the submission window deadline." |
| simultaneous | fine, withdraw at once | "Simultaneous Submissions to other publications are fine, but please withdraw your submission immediately if your work is accepted elsewhere." |

**Why $200 is the rate and not a prize.** The sentence ties the payment to *selection for
publication* — ten pieces per issue — and calls it "payment". The prize is a separate thing
those same pieces then advance to. Recording the $1,000 as the rate would have overstated the
market tenfold; recording nothing because "it's a contest" would have erased a real $200.

**Why there is no closing date.** The listing renders its close date client-side. It appears in
the page only as `Ends on` with nothing after it. I re-fetched the page on the desk date to
check that this was not a crawl artefact — it is not; the date is not in the reachable text.
Rather than guess a plausible window end, **the record carries no deadline object at all**, and
its requirements say so in as many words.

Note also what the page excludes by name: no poetry, no flash, no nonfiction — so the record is
typed `fiction` and `drama` only, and the flash-fiction desk will not surface it.

## 3. Verification

Scratch clone at the batch-23 tip `ef251a4eb5`:

| gate | result |
|---|---|
| `npm run build` | exit 0 |
| `validate` / `verify:allowlist` / `verify:titles` / `verify:dockets` / `validate:money` / `validate:hometools` | all exit 0 |
| `audit_dockets.py` | **290 publication pages**, 1318 unanswered rows, 153 rankings, **0 problems** |
| new pages | `let-me-tell-you-a-story` 31,762 b; `lemonwood-quarterly` 31,939 b |

**Note layer: 171 notes, 0 defects** — sentence renders on every page, correct reader-facing
label, no punctuation defects, and the three archived-source notes still in their legitimate
second shape. Because the branch now carries main's nine-row docket, this check runs on the
branch tree itself rather than only on a rehearsal merge — the longstanding blind spot is gone.

## 4. Session running total

| | |
|---|---|
| batches this session | 14–23 (ten batches) |
| records added | **35** |
| dataset | **290 records** |

## 5. Evidence durability — a known limit

The raw page texts these readings rest on live under `research/rebuild/raw/`, which is
**untracked**, exactly as every previous batch left it. That means the evidence is only as
durable as this workspace: snapshots have already wiped `research/` twice this session. The
durable record of *what was read and what it said* is the batch report in `reports/`, which
quotes the sentence behind every figure. If the desk wants the raw texts themselves in version
control, that is a one-line policy change (`git add research/rebuild/raw`) and about 2.5 MB —
but it is a repo-wide convention change, so it is the user's call, not one I made mid-batch.
