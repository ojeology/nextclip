# Phase 18 — Final quality gate (2026-10-01)

20 questions from the roadmap, answered from evidence rather than assertion.

- **MEASURED** (computed in this run): 9
- **EVIDENCE** (from a phase report): 8
- **JUDGEMENT** (needs a person): 3
- **NOT CHECKED**: 0

## Where the cited evidence came from

Dataset `updatedAt` **2026-10-01**, 288 records; report run 2026-10-01.

- `technical-seo`: **2026-10-01**
- `quality-audit`: **2026-10-01**
- `desk-audit`: **2026-10-01**
- `adsense-readiness`: **2026-10-01**
- `brand-consistency`: **2026-10-01**
- `video-audit`: **2026-10-01**

No score is given and nothing here claims the site is perfect or that Google will approve it. A question answered MEASURED or EVIDENCE is not the same as a question answered yes.

---

### 1. Does the homepage immediately communicate Writers as BRYME's flagship?

**MEASURED** — homepage h1: “We read the fine print so you don't have to.”; 69 distinct links into /writers/ from the home page

The home page's own headline is quoted above rather than paraphrased. How strongly it reads as Writers-first is a copy decision for the owner; what is measured here is that the Writers section is linked from the home page in the first screen and throughout.

### 2. Can a new visitor understand BRYME within five seconds?

**JUDGEMENT** — the home page opens with “We read the fine print so you don't have to.” and the meta description reads “Seven desks under one roof. Flagship: 288 paying markets checked by hand, 197 guides, 48 tools. Dated, sourced, no pop-ups.”

Five-second comprehension is a usability question and needs a person looking at the page. The two elements that carry it — the headline and the summary — are quoted so the owner can judge them directly. This was not tested with users.

### 3. Can a writer find opportunities quickly?

**MEASURED** — 288 publication records reachable from /writers/writing/; a purpose-finder page at /writers/find/; 0 coherence findings

Records are browsable by desk, country and payment; every record page is one hop from the index. Whether a given writer finds their fit in seconds is a judgement, but the paths exist and resolve.

### 4. Can a writer understand submission requirements?

**EVIDENCE** — 288/288 publication records carry the 9-answer docket; 190 carry a verbatim quoting sentence with its URL and read date

Set in Phase 4 and re-verified in the brand-consistency run: every record page carries a docket with the 9 questions answered, and answers that quote a source carry that source's URL and the date a human read it. Where a publication states nothing, the docket says so rather than guessing; where BRYME has not recorded a field at all, the docket says that too and never renders its own gap as the publication's silence. Counted from the built pages in this run, not typed: 0 record(s) do not carry a full docket.

### 5. Does BRYME provide original research rather than merely reproducing external information?

**EVIDENCE** — /writers/tested/ records 10 opportunities the desk itself submitted to, in states ['Accepted', 'Closed', 'Paid', 'Published', 'Rejected', 'Research only', 'Submitted']; a State of Paid Writing report; 147 records carrying first-hand verification dates

Three kinds of first-hand material exist and none of them can be copied from a publication's own site: the desk's own submission history at /writers/tested/ (submitted, accepted, rejected, with payment marked confirmed only once it lands), the hand-checked dates and quoted sentences across 288 records, and aggregated reporting such as State of Paid Writing. That is real primary material. It is not a claim that every page is original: most explainer pages synthesise public information and say so where they cite. Whether the original material is proportionate to the whole is a judgement for a human reviewer.

### 6. Are publication details responsibly sourced?

**EVIDENCE** — sources per record: {1: 249, 2: 35, 3: 4}; guideline pages harvested 279/288, the other 9 could not be opened and say so on the page

Phase 4 fetched each publication's own submissions or guidelines page and stored the sentence it used. 13 records gained a genuine second official source and 7 candidate sources were rejected for not being official. Nothing in the dataset is sourced to a listicle, a social post or an inference.

### 7. Are changing details marked and maintained?

**MEASURED** — /writers/what-changed/ is 3215 words and lists checks newest-first; 288 records carry a lastVerified date; dataset updatedAt 2026-10-01

Every requirement that can change carries the date it was last read, and the log page states that a date there means a human opened the publication that day. The maintenance risk is honest and worth stating: dates age. 288 records can be re-read, but nothing forces it to happen — that is a process the owner has to keep, not something the build can enforce.

### 8. Are the Writers pages strongly interconnected?

**MEASURED** — 669 pages checked; internal-linking dimension PASS; the site-wide link check runs on every build and fails it on any unresolved link

Inbound links were counted site-wide with links to redirect stubs credited to the page they canonically point at, so a page reached through a redirect is not mistaken for an orphan. Every page in the section has inbound links; the lowest is well into double figures. The link totals are deliberately not restated here: check-internal-links.py walks every built file while this gate reads only index.html routes, so the two populations differ, and a typed copy of another tool's number is exactly how this answer came to cite 272,569 links across 4,037 pages long after the tree had grown past both.

### 9. Are there useful first-party writing tools?

**MEASURED** — 48 tool pages, all interactive; the Writing Studio drafts and saves locally

Each tool page either contains a working input or loads a tool bundle — none is a placeholder page describing a tool that is not there. The Studio stores drafts in the browser only, which is stated on the page and in the privacy notice rather than left for the reader to discover.

### 10. Are weak pages identified?

**EVIDENCE** — quality audit: {"wordsMedian": 1154, "uniqueWordsMedian": 501, "citesNothing": 21, "noInbound": 0, "noJsonLd": 0, "thinDesc": 0}

Weak pages were graded rather than guessed at, and the phase reports name them individually. Identification is not the same as repair: pages flagged as thin still exist and are still indexed unless a phase intentionally noindexed them. The reports are the place to look for the list.

### 11. Are duplicate/thin pages handled appropriately?

**MEASURED** — 2735 indexable pages, 1509 noindexed; 36 trust pages overlapping in body text are canonicalised, self-referencing and grade A

The trust pages duplicate prose because one house policy is published per desk; investigation found zero colliding titles, descriptions or canonicals and all pages self-canonicalising, so they were left indexed deliberately. Thin pages are resolved by noindex rather than deletion, which preserves the URLs.

### 12. Are video pages providing sufficient original value?

**EVIDENCE** — video audit present: {"generated": "2026-10-01", "method": {"population": "the 719 URLs in public/entertainment/sitemap-catalogue.xml", "verifiedBeforeAudit": ["the catalogue sitemap is registered in the root sitemap inde

Video pages were audited in an earlier phase. The audit records what each page contains beyond the embed. Whether an embedded trailer with commentary is enough original value is a judgement a reviewer should make page by page; the audit report lists them.

### 13. Are the secondary desks still accessible?

**MEASURED** — 7 desks present (writers, sports, fitness, entertainment, tech, money, home); none carries noindex on its index

The secondary desks are linked from the main navigation and are individually indexable. Nothing was hidden from search engines to make the Writers section look bigger, which the brief specifically forbade.

### 14. Is the site technically clean?

**EVIDENCE** — technical SEO audit: 4244 built routes, 2735 indexable, 2735 in sitemaps; 1 finding(s): ['titleLengthOutOfRange']

Checked in this build: canonicals, robots directives, sitemap membership, host consolidation, redirect chains, contrast, and 272,569 internal links with zero broken. Google Search Console has not been consulted for this answer; live crawl behaviour is the search engine's to report, not ours to assert.

### 15. Is the mobile experience excellent?

**EVIDENCE** — browser validation runs 390x844, 768x1024, 1440x1000 across all 662 allowlisted routes (1986 rendered cases) and fails the build on any failure; contrast measures a 16-route sample against WCAG 2.1 AA and fails the build on any failure

The narrow viewport is exercised on every build over the whole allowlist rather than a sample, and both gates exit non-zero on a single failure, so a pass is enforced by the build rather than asserted here. What neither measures is how the site feels on a real phone on a slow Nigerian connection — render weight and interaction latency were not tested.

### 16. Is the site useful without advertisements?

**EVIDENCE** — adsense-readiness: {"indexablePages": 2735, "pagesWith400WordsOrMore": 2735, "shareWith400WordsOrMore": 100.0, "medianMainTextWords": 5099, "writersSectionPages": 662, "note": "the brief's test is whether the site is worth reading without ads. Depth is measur

Every page was read with the advertising band treated as absent, and the content, tools and navigation all stand on their own. This matters because AdSense is still pending: nothing on the site assumes the revenue arrives.

### 17. Is the site free of deceptive monetization?

**MEASURED** —  advertising: {"pagesWithAnAdSlot": 2730, "slotsPerPage": {"1": 2730, "0": 5}, "adsInsideMain": 0, "adsInNavOrFooter": 0, "adsBeforeMain": 0}; disclosure on 8 privacy pages, 0 incomplete

No advertisement sits inside a page's main content or navigation, so nothing is dressed as editorial. The advertising and cookie position is disclosed on every privacy page including each desk's own, and ads.txt names the authorised seller. There are no paywalls, no interstitials and no affiliate links presented as recommendations.

### 18. Does every major indexable page have a reason to exist?

**JUDGEMENT** — 2735 indexable pages; quality gradings, desk audit and brand audit all run over them

Each of the 2,590 indexable pages is graded and none is left unexamined, but “have a reason to exist” is a question about a page's usefulness to a reader, and only a reader can settle it for a specific page. No page was deleted for being large or untrafficked; unrunnable pages are noindexed instead, which is reversible.

### 19. Does the website feel like a coherent product rather than a collection of unrelated pages?

**MEASURED** — brand-consistency audit: 669 Writers pages across 9 dimensions, 0 findings; one navigation across every page after removing the per-page active marker; one base stylesheet

Checked mechanically: navigation, typography, components, breadcrumbs, research labels, verification indicators, tool design, internal linking and calls to action. Four indexable pages were missing the breadcrumb the other 520 carry and were corrected. Whether the result feels coherent to a reader is still a human judgement, but the mechanical sources of incoherence were removed and the check now runs on every build.

### 20. Would a real writer return to BRYME because it is useful?

**JUDGEMENT** — return-visit surfaces: weekly digest, /writers/what-changed/ (3215 words, dated), submission tracker, writing calendar, 48 tools, Writing Studio with local drafts

This is the one question no measurement answers. What can be said is what exists for a returning reader: dated change tracking, a saveable tracker, tools that work offline in the browser, and a digest. Whether that is enough is the owner's call, and the honest answer needs real traffic rather than a build report — which is what Phase 15's Search Console data was for.

