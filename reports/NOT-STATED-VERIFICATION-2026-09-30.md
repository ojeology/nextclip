# Verifying the `not-stated` claims — 20 records, 30 September 2026

`not-stated` is not a blank. It is a claim: **"a human read the guideline and it
says nothing about submitting elsewhere."** Main's commit c61f1ff46cf found that
15 records on its side were making that claim about *a page nobody had ever
read* — a blocked fetch was being rendered as a finding of silence — and that
when the pages were re-asked through a real browser, **three of six contained a
real policy**.

This branch made the same class of claim with the same method. The batch-13
simultaneous-submissions backfill classified **20 branch-only records** as
`not-stated` from plain HTTP fetches. Those 20 were re-asked here.

**Result: all 20 hold.** 0 records had to be changed. But the exercise found a
defect — in the verification tool itself.

---

## 1. What was re-asked, and how

| client | why |
|---|---|
| Chromium via Playwright, JavaScript allowed, real `Accept-Language`, 1.5s settle after network idle | a JavaScript shell returns far less than a reader sees |
| plain HTTPS fetch with a normal Safari user-agent, `gzip`/`deflate` handled | added after Chromium **itself** was walled (see §3) |

Neither client decides anything. The script prints what each page says about
submitting elsewhere; reading decides.

| verdict | records |
|---|---|
| silent in the browser | **11** |
| browser walled, plain fetch worked and was silent | **3** |
| text found to read | **6** |
| **still unreadable** | **0** |

## 2. The six that needed reading — all false positives

The probe is deliberately wide, so it catches things that are not about
simultaneity. All six were read, and none addresses submitting elsewhere:

| record | what the probe caught | what it actually is |
|---|---|---|
| africa-is-a-country | *"We're happy for you if you are able to sell the work you publish here elsewhere; however, please make sure that Africa's a Country is credited and linked to."* | reuse **after** publication, plus an attribution ask |
| raleigh-review | *"Please do not combine multiple submissions in one file."* / *"the same piece that was published elsewhere"* | **multiple** submissions in one file; **prior** publication. Also discusses reprints of poems from a chapbook |
| raleigh-review | *"Ai, plagiarism, abridging and/or renaming the same piece that was published elsewhere are unwelcome here"* | plagiarism and prior publication |
| literary-veganism | *"we are not in the business of re-hashing work, so please do not submit work that has already been published elsewhere"* | **prior** publication |
| farmer-ish | *"if you have published your work on a personal blog, you can re-purpose it for us … mention Farmer-ish as the original publisher if your work appears elsewhere"* | repurposing your own blog work; attribution |
| hemlock-journal | *"the non-exclusive right to publish"* / *"You are free to republish your work elsewhere after publication"* | rights granted, and reuse **after** publication |
| nonbinary-review | *"exclusive access to early submissions"* | a newsletter perk in marketing copy |

**None of these states a policy on submitting the same piece to another journal
at the same time.** `not-stated` stands for all six.

Recorded explicitly because the probe is the kind of signal that gets trusted as
a classifier. It is not one: a wide probe over these 20 records produced seven
hits and **zero** were about the thing being measured. That is the same lesson
Phase 4 recorded, from the other direction.

## 3. A defect in the verification tool — the same one main documented

The first version of `verify-not-stated-browser.js` decided:

```js
rec.verdict = hits.length ? "HAS-TEXT-TO-READ" : "silent";
```

So a page that rendered **no text at all** had no probe hits, and was reported
as `silent`. Five pages hit this, and what the browser had actually received was:

```
100-word-story       403 - Forbidden / Access to this page is forbidden.  (49 chars)
farmer-ish           Confirm you are human / We need to check you're not a robot …  (100)
hemlock-journal      Confirm you are human …  (100)
metachrosis-literary Confirm you are human …  (100)
pennsylvania-…       Confirm you are human …  (100)
```

A bot wall was being reported as a finding of silence — **precisely the defect
main's c61f1ff46cf exists to describe, reproduced in the tool built to check for
it.** The tell was in the output all along: the five "silent" pages were 49–100
characters while every genuinely silent page was 2,000+.

Fixed three ways:

1. `MIN_READABLE = 400` — a page shorter than that did not render, whatever it
   says.
2. A `CHALLENGE` pattern for the phrasings bot walls use ("Confirm you are
   human", "Just a moment", "Checking your browser", "403 Forbidden", …).
3. A **plain-fetch fallback**: when Chromium is walled, ask again with a plain
   HTTPS request before concluding anything.

That third fix is what actually recovered the pages. Re-asked as a plain fetch,
all five returned full guidelines:

| record | browser | plain fetch | simultaneous hits |
|---|---|---|---|
| 100-word-story | 49 chars (403) | **4,466 chars** | 0 |
| farmer-ish | 100 chars | **5,526 chars** | 0 (1 wide-probe hit — see §2) |
| hemlock-journal | 199 chars | **8,375 chars** | 0 (2 wide-probe hits — see §2) |
| metachrosis-literary | 100 chars | **3,693 chars** | 0 |
| pennsylvania-literary-journal | 100 chars | **12,635 chars** | 0 |

### The finding runs in both directions

Main's c61f1ff46cf established that **a 403 to a script is not a page a reader
cannot open** — Chromium got in where a fetch was refused, and three of six had
something to say.

This batch found the inverse. **A challenge to a headless browser is not a page
a reader cannot open either** — a plain fetch got in where Chromium was walled,
on five pages out of twenty.

Neither client is systematically the more trusted one, so neither can be the
only one. The rule that survives both cases is the same and is the point:

> A failed fetch may never be recorded as a finding of silence. If neither
> client can read the page, the honest value is **unreadable**, and it must be
> distinguishable from `not-stated` — which is why main's open question about
> a third badge state applies to this branch too.

On this branch the question is now moot for these 20: **0 remain unreadable.**

## 4. What was not done

- **The other 81 records were not re-verified.** The 73 `accepted` and 8
  `not-accepted` records quote a sentence, and every one of those sentences was
  machine-checked to appear verbatim in the saved page text (84 checked, 0 not
  verbatim). A quote that reads correctly out of real page text is a stronger
  guarantee than a silence, so the risk sat with the silences and that is what
  was checked. A fuller pass could still re-ask all 101.
- **The 147 records shared with main were not touched.** Main owns those and
  has already re-harvested them; its c61f1ff46cf reports nine still-unread
  records as its own open item.
- **No record was changed by this exercise.** The value for all 20 stays
  `not-stated`, now on the strength of two independent reads rather than one.

## 5. Evidence

`scripts/verify-not-stated-browser.js` is committed. The per-record text it
fetched lives under `research/`, which is **not committed** and did not survive
a workspace snapshot, so the table above is the durable record.

Re-running is one command and takes about two minutes:

```
node scripts/verify-not-stated-browser.js --targets research/not-stated.json
```

Chromium is a dev dependency (`playwright`) and needs `npx playwright install
chromium` plus `npx playwright install-deps chromium` — the system libraries are
not in a fresh container, and install them into the environment rather than the
repository.
