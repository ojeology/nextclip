# BRYME Full-Site Google Search, AdSense, Content and Product Audit

**Audit date:** 4 September 2026 (Africa/Lagos)
**Production reviewed:** `https://bryme.onrender.com`
**Repository reviewed:** `/home/user/nextclip`, branch `main`, commit `f033af2dd4`
**Scope:** the entire repository and production site—not only the homepage
**Status:** audit only. No website upgrade has been implemented.

> This report supersedes `AUDIT_AND_IMPLEMENTATION_PLAN.md`, which describes an older prototype and should not be used as the current decision document.

---

## 1. Executive verdict

### Decision

| Question | Verdict |
|---|---|
| Is BRYME technically visible to Google? | **Partly yes.** The site is crawlable, and 1,377 content routes are indexable and self-canonical. |
| Is the current 1,377-page search surface ready to rank competitively? | **No.** The dominant problems are low original value, unreliable or unsupported claims, source/build drift, weak discovery, inaccurate structured data and lack of editorial focus. |
| Is BRYME ready for an AdSense application or re-review? | **No. Do not submit yet.** Large low-value/unfinished sections, misleading controls, privacy contradictions and current ad behavior are blocking risks. |
| Does IMDb prevent BRYME trailer pages from ranking? | **No.** IMDb creates neither a blanket ranking ban nor an automatic penalty. BRYME's page quality, differentiation, provenance and licensing are the real issues. |
| Should the site receive another visual skin before cleanup? | **No.** First reduce and control the search surface, repair deployment/data/privacy, and choose a focused product. Then redesign the retained product. |
| Is a custom domain mandatory for AdSense? | **Not proven.** `onrender.com` is on the Public Suffix List, so the subdomain is not automatically disqualified. A custom domain is nevertheless strongly recommended before growth. |

### The five most important findings

1. **The search surface is much larger than the useful editorial surface.** Of 1,377 self-canonical indexable routes, 459 have fewer than 100 words in source `<main>` and another 84 have 100–299. Word count is not a Google quota, but the family-level pattern exposes unfinished and generated pages.
2. **The entertainment proposition is not trustworthy enough.** The catalogue has 726 records, a 19-word median description, 599 records without a rating, and 694 without either facts or watch links. Yet pages make broad claims about verified trailers, official destinations, “Match” and HD.
3. **Sports publication is operationally broken.** There are 26 unmerged results branches; workflow errors are hidden by `|| true`; all 132 standings rows store goal difference as zero and 83 contradict `GF − GA`.
4. **Production is serving the repository as a static directory, not the intended Node service.** Redirect logic is inactive, aliases and slash variants return duplicate `200` responses, and source/configuration files are publicly downloadable.
5. **Privacy and advertising behavior contradict the site's own policy.** GA4 runs site-wide although the privacy page says BRYME does not use analytics; there is no evident consent gate; a Monetag vignette can load after dwell time.

### Recommended strategic direction

BRYME should stop acting like four incomplete specialist products joined together. The strongest practical direction is:

> **BRYME helps Nigerians and Africa-based applicants find verified opportunities and use practical technology to act on them.**

That gives one audience and one job-to-be-done:

- **Primary:** verified jobs, paid opportunities and carefully checked application guides.
- **Supporting:** practical Tech/AI tutorials and tools that help users qualify, apply or work.
- **Entertainment:** retain only a small, differentiated editorial/watch pilot; do not operate an unverified pseudo-streaming catalogue.
- **Sports:** pause/noindex generated detail inventory until BRYME has dependable, lawful data and an operational publishing workflow.

This is a recommendation, not a claim that Google imposes a “single-niche penalty.” Large multi-topic publishers can rank. BRYME currently lacks the staff, data contracts, editorial systems and brand authority needed to operate four competitive verticals at once.

---

## 2. What was audited

The audit covered:

- all **4,293 repository files** and **3,377 HTML files**;
- every route family, including content not exposed in visible navigation;
- robots directives, canonicals, sitemaps, News sitemap, RSS and redirects;
- 166,079 internal references and likely page/image targets;
- source content, compiled HTML and generator reconciliation;
- all 726 entertainment catalogue records;
- structured data across every indexable page;
- production HTTP status, aliases, headers, cache behavior and exposed internals;
- browser-rendered mobile and desktop behavior using Chromium/Selenium;
- nine synthetic Lighthouse runs;
- sports data, workflows, scripts, branches and pull-request history;
- analytics, ad code, privacy statements and consent behavior;
- Make Money outbound links;
- Google Search, AdSense, CMP, JobPosting, video, sitemap and robots guidance;
- IMDb data-use guidance and Render domain behavior;
- leading product patterns in entertainment, sports, jobs, opportunity and tech publishing;
- first-party hiring sources current on 4 September 2026.

### Important limitations

The following evidence was not available:

- Google Search Console Page Indexing, Sitemaps, Manual Actions, Security Issues, Performance, Links and URL Inspection reports;
- Google Analytics account data;
- AdSense account status, Policy Center messages or rejection correspondence;
- server logs and Googlebot request history;
- backlink data from an independent index;
- field Core Web Vitals/CrUX data;
- historical credential scanning across the complete Git history.

Consequently:

- external `site:` searches cannot establish how many URLs Google has indexed;
- this report cannot rule in or rule out a manual action or security issue;
- Lighthouse data is synthetic laboratory data, not real-user field data;
- bulk removal decisions must be reconciled against Search Console clicks, impressions, links and conversions before implementation.

---

## 3. Current inventory and index surface

### 3.1 Top-level counts

| Metric | Count |
|---|---:|
| HTML files | 3,377 |
| Indexable HTML files | 1,379 |
| `noindex` HTML files | 1,998 |
| Indexable + self-canonical content routes | 1,377 |
| Verification HTML files that account for the two-route difference | 2 |
| Unique URLs in the main sitemap | 1,284 |
| Main-sitemap URLs that are `noindex` | 0 |
| Main-sitemap URLs with missing files | 0 |
| Self-canonical indexable routes missing from the sitemap | 93 |
| News-sitemap URLs | 20 |
| Indexable/self-canonical routes with zero HTML inlinks | 64 |
| Those 64 also absent from the sitemap | 44 |
| Routes with no main-content inlink from an indexable page | 81 |

### 3.2 Source-main-content diagnostic

| Source `<main>` words | Indexable/self-canonical routes |
|---|---:|
| 0–99 | 459 |
| 100–199 | 51 |
| 200–299 | 33 |
| 300–499 | 670 |
| 500–999 | 131 |
| 1,000+ | 33 |

This is a diagnostic, **not a minimum-word rule**. A concise score page can be useful, while a 500-word templated page can still be low value. Two caveats matter:

- JavaScript-rendered sports tables add visible data after load, so source counts understate some sports utility.
- Movie pages can exceed 300 words because templates repeat metadata and interface copy even though the median catalogue description is only 19 words.

### 3.3 Thin-route concentration

| Family | Indexable/self-canonical | Under 100 source-main words | 100–299 | Zero HTML inlinks |
|---|---:|---:|---:|---:|
| Movie routes | 564 | 0 | 26 | 0 |
| Series routes | 124 | 42 | 1 | 0 |
| Anime routes | 103 | 29 | 6 | 0 |
| Sports | 353 | 319 | 9 | 49 |
| Make Money | 76 | 9 | 3 | 5 |
| Year hubs | 44 | 30 | 14 | 0 |
| Tech | 36 | 17 | 1 | 8 |
| Entertainment articles | 24 | 0 | 2 | 2 |
| Movie-list hubs | 17 | 5 | 7 | 0 |
| Branded channels | 9 | 0 | 3 | 0 |
| Topic hubs | 7 | 6 | 1 | 0 |

### 3.4 What is working technically

BRYME is not literally “nothing.” The reusable foundations include:

- all 1,377 self-canonical indexable content routes have a title, meta description, canonical and exactly one H1;
- no `noindex` URL is currently submitted in the main sitemap;
- no main-sitemap target is missing from the repository;
- all 166,079 likely internal references resolved to a local target in the filesystem audit;
- indexable descriptions are not exact duplicates;
- schema JSON parses without syntax errors;
- sampled local resources returned successfully and browser sessions showed no JavaScript console errors;
- legal, contact, editorial and author routes exist;
- the catalogue and sports data already have some structured source material that can be migrated.

These basics explain why automated SEO scores can look green. They do **not** prove factual quality, policy readiness, index coverage or rankworthiness.

---

## 4. Hidden and indexable content

### 4.1 Objective hidden-route result

The audit defines an objective route-level hidden condition as:

- indexable;
- self-canonical;
- no incoming link from any audited HTML page.

There are **64** such routes. The complete row-level appendix is:

- [`reports/hidden-indexable-routes.csv`](reports/hidden-indexable-routes.csv)

| Discovery state | Count | Composition |
|---|---:|---|
| In sitemap, but no HTML inlinks | 20 | 8 Tech topic hubs, 4 Make Money hubs, 4 sports match pages, 2 entertainment editorials, 1 fixtures page, 1 results page |
| Neither sitemap nor HTML inlinks | 44 | 43 generated sports reports and `/make-money/microtasks/` |

The 43 completely undiscoverable reports break down as:

- Premier League: 9
- La Liga: 9
- Serie A: 9
- Bundesliga: 8
- Ligue 1: 8

### 4.2 Recommended hidden-route decisions

| Family | Count | Decision |
|---|---:|---|
| Generated sports reports | 43 | Noindex/archive now; republish only after a substantive report standard, source proof and contextual links exist. |
| Sports match pages | 4 | Noindex until data accuracy, server-rendering and linking pass. |
| Sports fixtures/results | 2 | Retain only after the data pipeline is fixed; then link from league hubs. |
| Tech hubs | 8 | Temporarily noindex; populate as genuine task hubs or merge into the nearest strong hub. |
| Make Money hubs | 5 | Redirect `/microtasks/`; noindex/merge three weak thematic hubs; build and link `/platform-reviews/` if reviews are first-hand and method-based. |
| Entertainment editorials | 2 | Retain if editorially useful; add contextual links from relevant title and article pages. |

Notable route-specific decisions are already encoded in the CSV, including:

- `/make-money/microtasks/` → one-hop `301` to `/make-money/remote-work/`;
- `/make-money/writing-opportunities/` → one-hop `301` to `/make-money/writing/`;
- `/article/best-anime-to-watch-now/` and `/article/movies-like-deadpool-and-wolverine/` → retain/improve/link;
- eight named Tech hubs → noindex until populated or merged.

### 4.3 Hidden DOM/CSS findings

The repository also contains hidden attributes, modal content, responsive navigation, tabs and permanently hidden template fragments. These should **not** all be called cloaking:

- responsive desktop/mobile navigation is normal;
- collapsed controls and video modals can be legitimate;
- search embeds a large client-side catalogue payload that inflates `textContent`, but script data is not equivalent to visible prose;
- the serious user-facing CSS problem is that global rules hide the desktop header/navigation on **791 indexable movie, series and anime routes**, leaving users in a streaming-style interface with limited escape paths.

No deliberate search-engine cloaking was established. The confirmed problems are orphaned routes, misleading template semantics, excessive hidden payload and navigation suppressed on a very large route family.

---

## 5. Search and technical SEO audit

### 5.1 Deployment is the first technical blocker

The repository describes an intended Node service in `server/server.js` and `server/render.yaml`. Production does not behave like it:

- `/healthz` returns `404`, although the Node service defines a health route;
- `/server/server.js` returns `200 application/javascript` and exposes the server source;
- `_redirects`, package/configuration files, workflow YAML and documentation are publicly downloadable;
- the redirects the Node server is designed to parse are not running;
- static-file cache behavior is present instead of the intended application routing behavior.

Sampled production results:

| Path | Actual result | Intended result |
|---|---|---|
| `/movie/breaking-bad/` | `200`, 959-byte noindex move page | `301` to `/series/breaking-bad/` |
| `/movie/dune-part-two` | `200` | `301` to slash canonical |
| `/movie/dune-part-two/` | `200` | canonical `200` |
| `/channels/netflix` | `200` | `301` to slash canonical |
| `/server/server.js` | `200` | `404` / not deployed |
| `/healthz` | `404` | `200` if Node is the chosen runtime |

`_redirects` contains **302 repository-defined rules whose intended status is 301**. The file itself warns that Render Static Sites ignore it. Canonical tags help consolidate duplicates, but they are signals rather than a substitute for correct HTTP routing.

**Required architecture decision:** either deploy the tested Node service or use a true static publish directory plus platform-native redirect configuration. Do not continue serving the repository root.

### 5.2 Public-source exposure

Confirmed public `200` responses include application source/configuration such as:

- `server/server.js`;
- `.github/workflows/results-agent.yml`;
- `package.json`;
- `README.md`;
- `_redirects`;
- `server/render.yaml`.

No active credential was found by the current-tree common-pattern scan. That is not a security guarantee, and Git history was not exhaustively secret-scanned. Robots rules are not access control. Build and deploy an allowlisted public artifact containing only pages, public assets, sitemaps, feed, manifest and required verification files.

### 5.3 Robots rules

Current `robots.txt` has a wildcard group that disallows `/server/`, followed by separate `Googlebot` and `AdsBot-Google` groups containing only `Allow: /`.

Google selects the most specific matching group and does not inherit wildcard rules into that group. The result is that `/server/` is allowed to Googlebot and AdsBot-Google despite the wildcard exclusion.

Fix by simplifying to one correct group unless a crawler genuinely needs special treatment. More importantly, remove server/source files from public deployment. Do not block a URL in robots before Google has been able to see a needed `noindex` directive.

### 5.4 Sitemap and date integrity

Main sitemap:

- 1,284 unique URLs;
- no missing, noindex or non-self-canonical entries;
- 93 self-canonical indexable routes omitted: 89 sports and four Make Money;
- every URL has the same `lastmod`: `2026-09-02`.

News sitemap:

- 20 URLs;
- publication dates are 23–25 August 2026;
- all are outside Google's preceding-two-day News-sitemap window on the audit date.

Required fixes:

- generate sitemaps only from explicit `indexEligible` records;
- use significant, verified modification times—not build time copied to every URL;
- remove articles from the News sitemap after two days while keeping them in the normal sitemap when otherwise eligible;
- do not solve the 93 omissions by blindly adding every route: many omitted routes should first be noindexed or consolidated.

### 5.5 Internal linking and architecture

The filesystem link checker found no likely missing internal target, but existence is not architecture.

- 64 indexable/self-canonical routes have zero incoming HTML links.
- 81 have no link from the main content of an indexable page.
- title pages often depend on catalogue cards and then hide normal desktop navigation.
- sitemap-only discovery is especially common in Tech and generated sports.

Every retained indexable page should sit in a clear hierarchy and receive at least one contextual, crawlable `<a href>` from an indexable page. Automated builds should reject unintended orphans.

### 5.6 Search page

`/search/` shows roughly 32 visible main-content words in the tested state while a rendered `textContent` diagnostic sees roughly 20,817 words because the catalogue payload is embedded on the page. This is primarily a payload/architecture issue, not proof of cloaking.

Recommended options:

1. keep search as a utility and `noindex,follow` it; or
2. rebuild it with a separate data endpoint/index, useful server result states and strict parameter-index controls.

Do not expose arbitrary thin query URLs to indexing.

### 5.7 Metadata

The metadata baseline is stronger than the content:

- all 1,377 self-canonical indexable routes have a title, 120–160-character description, canonical and one H1;
- 274 titles are over 60 characters and 199 are under 30, though title length alone is not a violation;
- the only exact duplicate indexable title pair is `/make-money/microtasks/` and `/make-money/remote-work/`.

Descriptions appear mechanically length-controlled. A technically valid snippet is not a substitute for accurate, page-specific value.

### 5.8 Structured data

Schema parses, but much of it is inaccurate or unsupported:

- 737 indexable pages contain `VideoObject`;
- 717 share `uploadDate: 2024-01-01` and generic descriptions;
- all audited VideoObjects lack `duration` and `contentUrl`;
- 717 lack a publisher;
- 611 `Movie`/`TVSeries` entities use a YouTube trailer URL as `sameAs`, although `sameAs` should identify the title entity;
- 143 affected pages with Article markup lack an author;
- 155 lack `datePublished`;
- 100 lack `dateModified`.

This is an accuracy issue, not merely a validator issue. Remove schema that cannot be supported. For retained videos, use the actual trailer title, uploader/publisher, thumbnail and upload date, keep the playable embed prominent, and ensure visible text matches the markup. For retained articles, show and mark up real bylines and dates.

### 5.9 Secondary deployment and hardening observations

- Production sends HSTS and `X-Content-Type-Options: nosniff`, which are useful baselines.
- No Content-Security-Policy, Referrer-Policy or Permissions-Policy was observed on the sampled homepage response. Add and test appropriate controls; the current mix of analytics, advertising and video origins makes an explicit policy especially useful.
- `/favicon.ico` returns `404`. Declared SVG/PNG icon links may still work, but a valid crawlable root icon and Search favicon compliance should be tested.
- `feed.xml` mixes authored articles with generated match reports. Rebuild the feed after the retain/noindex decisions so it represents current, maintained publication content.
- A comment-only `/ads.txt` is live in production but absent from the current Git tree, another small sign that the deployed file set is not fully reproducible.

### 5.10 Search Console evidence required

Before broad deindexing or migration, export:

- Page Indexing, including every exclusion/reason row;
- submitted and discovered sitemap data;
- URL Inspection for representative routes from every template;
- Performance for 16 months by query, page, country, device and search appearance;
- Core Web Vitals;
- Links/top linked pages;
- Manual Actions;
- Security Issues;
- Removals history.

External `site:` results are useful for spot checks only; Google explicitly says search operators are not exhaustive.

---

## 6. Entertainment and trailer audit

### 6.1 Catalogue reality

| Metric | Finding |
|---|---:|
| Catalogue records | 726 |
| Median description | 19 words |
| Records without a rating | 599 |
| Records without facts or watch links | 694 |
| Records with a trailer | 695 |
| Records with no trailer | 31 |
| Trailer-present records marked fan-made | 17 |
| Records with null `createdAt` | 726 |
| Records with null `updatedAt` | 648 |
| Records with any `updatedAt` value | 78 |
| Indexable title-like routes with controls | 791 |
| Actual non-placeholder detail routes | 736 |
| Indexable “More details coming soon” pages | 55 |

Source/build reconciliation also shows drift:

- 719 detail routes match a current catalogue record;
- 17 compiled series detail pages have no current JSON record;
- seven JSON movie slugs are alias forms without a self-canonical detail page;
- the current Netflix channel HTML contains 493 tiles even though the present generator maps Netflix to all current movie records and would now select 571.

This is evidence that compiled HTML, source JSON and generators do not have a single reproducible truth.

### 6.2 Placeholder pages

Fifty-five indexable Series/Anime pages visibly say “More details coming soon”; all 55 are submitted in the main sitemap.

Decision: remove them from the sitemap and apply `noindex` immediately. A page should not become indexable simply because a slug and title exist.

### 6.3 Unsupported claims and controls

The homepage/catalogue experience claims verified or official trailers, but:

- 48 records do not meet that claim: 17 are marked fan-made and 31 have no trailer;
- “Watch Now” opens a trailer rather than the title itself;
- “My List” and “Rate” appear on 791 indexable routes but have no corresponding handlers;
- “90% Match” is just a stored rating multiplied by ten, with no published matching method;
- “HD” is shown without BRYME hosting or verifying playback quality;
- ratings are described as editorial without a clear named reviewer/method on most pages.

Required fixes:

- rename `Watch Now` to `Play trailer`;
- remove or fully implement `My List` and `Rate`;
- remove “Match” and HD or define, verify and visibly explain them;
- do not call a trailer official unless the uploader/source was checked;
- show the source channel and checked date;
- do not imply that BRYME streams a title.

### 6.4 Branded “channel” pages are misleading

`scripts/build-channels.js` does not use provider availability:

- **Netflix** = all movie records;
- **Prime Video** = all series records;
- **Crunchyroll** = all anime records;
- **SonyLIV** = broad drama/crime/thriller genre matching;
- **JioHotstar/MX Player** = broad India/Indian text matching;
- **Kids** = broad genre matching.

The page disclaimer that availability “varies by region” does not cure the primary impression created by the brand names, logos and “channel” UI. `/channels/netflix/` currently lists 493 titles although 694 of 726 catalogue records have no facts or watch links.

Decision options, in priority order:

1. **Remove/noindex branded pages now.**
2. Rename non-provider concepts as neutral, accurate editorial collections, such as “Movies,” “Series,” “Anime” or “Indian cinema picks.”
3. Rebuild provider pages only with a licensed/current availability source, country/region, provider type, destination URL and `verifiedAt` timestamp.

A region-specific catalogue would need to distinguish subscription, rent, buy and free-with-ads. It must never infer service availability from content type or genre.

### 6.5 Data accuracy and provenance

Examples requiring correction include implausible runtime values (`Oppenheimer` at 10,809 minutes and `The Black Book` at four minutes) and `/movie/the-invite/`, whose source label says Wikipedia while linking to IMDb.

Provenance coverage is inconsistent:

- many records name Wikidata as a metadata source;
- numerous records have no metadata source;
- cast provenance is incomplete;
- 695 poster/thumbnail choices depend on YouTube-hosted imagery;
- 10,325 of 11,026 images used on indexable pages are YouTube-hosted, and 691 pages use only YouTube images.

Build a rights/provenance ledger for every retained fact and image. YouTube embeds and thumbnails are not a substitute for a durable image-rights pipeline. Seek legal review for commercial reuse and hotlinking rather than assuming that public visibility equals a reusable license.

### 6.6 Why IMDb is not the ranking blocker

**Direct answer:** Google does not have a published rule saying that a page cannot rank because IMDb covers the same title or because a lawful citation points to IMDb.

What does make ranking difficult:

- the query is already served by YouTube, studios, IMDb, Rotten Tomatoes, streaming services and large publishers;
- a short database synopsis plus a third-party embed is commodity content;
- BRYME currently provides little original analysis, regional availability or first-hand review value on most title pages;
- facts/schema are sometimes inaccurate;
- title-page navigation and controls are misleading;
- authority, links and real Search Console performance are unknown.

IMDb presents a **separate licensing issue**. IMDb's help guidance restricts commercial reuse/scraping without permission. Do not scrape IMDb or copy its descriptions, ratings, images or data at scale unless BRYME has the necessary licence. A genuine IMDb title URL may be used as a citation or entity reference where permitted; it should not be mislabeled as Wikipedia.

### 6.7 A BRYME trailer page that could deserve indexing

A retained page should provide a combination such as:

- a verified official trailer embed from the studio/distributor channel;
- actual video title, channel and upload date;
- a named BRYME reviewer/editor and original reason-to-watch or analysis;
- Nigeria-specific lawful availability, with provider type and checked date;
- carefully sourced runtime, certification, cast and release information;
- content notes or audience guidance created by BRYME;
- a useful comparison/order guide linked contextually;
- lawful, attributed imagery;
- click-to-load video with no autoplay;
- accurate Movie/TVSeries and VideoObject markup matching visible content.

There is no magic word count. If BRYME has no original or regional value beyond an embed and a generic synopsis, the page should remain noindex or should not exist.

---

## 7. Sports audit

### 7.1 Search surface

- 2,035 sports HTML files exist.
- 353 are indexable.
- 1,682 are `noindex`.
- 319 of the 353 indexable routes have fewer than 100 source-main words.
- 88 generated reports contain 47–94 source-main words each.
- all 88 reports are omitted from the main sitemap;
- 43 have neither a sitemap entry nor any HTML inlink.

JavaScript adds tables and match data after load on some routes, so not every low source count equals an empty visible page. Google can render JavaScript, but critical score/table content should still be server-rendered or statically generated for reliability, speed, sharing and failure tolerance.

### 7.2 Data integrity

- all 132 standings rows store goal difference as zero;
- 83 rows contradict the invariant `GF − GA`;
- the production competition bundle was built on 2 September 2026 at the time of audit;
- the compact and full sports data sources have separate update paths;
- result pages and generated reports can drift from the actual update branches.

A sports product is trust-sensitive: one wrong table can discredit every result. CI must reject impossible invariants, duplicate fixtures, missing teams, unsupported statuses and stale builds.

### 7.3 Automation failure

`.github/workflows/results-agent.yml` tries to create/merge result updates, but:

- the requested `results-agent` label does not exist;
- pull-request and merge failures are followed by `|| true`;
- workflow runs can therefore appear green after publication failed;
- 26 `origin/agent/results-*` branches remain unmerged.

Required fix:

- remove error suppression;
- create/configure any required label;
- add explicit permissions and branch cleanup;
- validate data before opening a PR;
- alert on failure;
- prove the process with one controlled end-to-end result update.

### 7.4 Product decision

BRYME should not try to match Flashscore/Sofascore/ESPN breadth with an unlicensed or brittle updater. Choose one of two paths:

1. **Pause:** noindex generated match/team/report inventory and keep only a small editorial sports section.
2. **Commit:** obtain a lawful data source with documented terms/SLA, server-render a narrow set of leagues, monitor freshness, and add original previews/reports rather than feed transformations.

Do not monetize stale or thin score screens.

---

## 8. Make Money, opportunities and trust-sensitive content

### 8.1 Current strengths

This vertical contains some of BRYME's longest and most practically useful pages. Of 76 indexable/self-canonical Make Money routes, 64 have at least 300 source-main words. The direct-link orientation can become a real differentiator if verification is made visible and repeatable.

### 8.2 Current weaknesses

- 55 of 62 indexable Make Money routes carrying Article markup have no parsed schema author;
- the same 55 have no parsed `datePublished`;
- opportunity status and verification dates are not consistently visible;
- broad earning claims are trust-sensitive and need evidence/disclosure;
- five hubs have no HTML inlinks;
- `/microtasks/` duplicates `/remote-work/` at title/purpose level;
- `/writing-opportunities/` overlaps `/writing/`.

### 8.3 Outbound-link audit

There are 121 unique external URLs across the audited Make Money pages:

| Result | Count | Interpretation |
|---|---:|---|
| Reachable | 109 | HTTP response succeeded at audit time; this does **not** prove the opportunity remains open. |
| Protected/rate-limited | 5 | `403` or similar; requires browser/manual review, not automatic deletion. |
| Transport unknown | 6 | TLS, timeout or client-limit issue; requires manual review. |
| Confirmed likely dead | 1 | TandF/Wasafiri submission URL returned `404`; update to the current Wasafiri destination. |

Full evidence: [`reports/make-money-external-link-status.csv`](reports/make-money-external-link-status.csv).

### 8.4 Editorial standard for money/opportunity pages

Every retained page should display:

- named writer and accountable editor/reviewer;
- published, materially updated and last-verified timestamps;
- direct primary source link;
- exact eligibility and geography in the source's words;
- fees, compensation and deadlines only when the source states them;
- affiliate/sponsorship disclosure where relevant;
- status: open, rolling, closing soon, closed or uncertain;
- next review date and a correction/report link.

Do not promise earnings, imply BRYME endorsement or infer Nigerian eligibility from “remote.”

---

## 9. Tech and AI audit

- 36 Tech pages are indexable.
- 17 have fewer than 100 source-main words.
- eight have no HTML inlinks at all.

The strongest route is not “more AI news.” BRYME should publish tested, task-focused guidance for its chosen audience, such as:

- how to verify whether an advertised remote role accepts Nigeria;
- how to prepare application files on a low-cost Android device;
- how to use a specific tool in a documented workflow;
- local connectivity/payment limitations;
- side-by-side tests with date, device, version, inputs and output evidence.

Merge empty topical taxonomies. A hub should exist only when it helps users navigate several strong child pages; a label plus cards is not automatically an indexable landing page.

---

## 10. Privacy, advertising and AdSense readiness

### 10.1 Current behavior

- `assets/analytics.js` loads GA4 ID `G-NQKHPBYFE8` site-wide.
- The privacy page says BRYME does not use analytics.
- No evident consent gate prevents GA4 before a choice where consent is required.
- Monetag code can load a vignette/interstitial after dwell time.
- Production serves a comment-only placeholder `/ads.txt`; no active publisher record is present.
- No live Google AdSense publisher tag was observed, so this is a readiness assessment rather than a finding about current AdSense delivery.

The privacy-policy contradiction must be fixed even if no AdSense application is planned.

### 10.2 AdSense blockers

| Area | Status | Why |
|---|---|---|
| Meaningful publisher content | **Fail** | Large families are unfinished, generated, replicated or template-heavy. |
| Navigation and controls | **Fail** | Header hidden on 791 routes; dead My List/Rate; Watch Now is mislabeled. |
| Under-construction screens | **Fail** | 55 indexable “More details coming soon” pages. |
| Replicated/low-added-value content | **High risk** | Generic descriptions, third-party trailer embeds and feed-like sports pages dominate. |
| Claims and trust | **Fail** | Unsupported official/verified/Match/HD/provider implications. |
| Privacy disclosures | **Fail** | Policy says no analytics while GA4 runs. |
| Consent | **Fail/unknown by region** | No evident gate; a Google-certified TCF CMP is required for certain AdSense use in the EEA, UK and Switzerland. |
| Existing ad experience | **High risk** | Monetag vignette adds interruption and consent complexity. |
| Site ownership/domain | **Potentially acceptable, not verified** | `onrender.com` is a public suffix, but account-level verification was unavailable. |
| `ads.txt` | **Pending** | Add the exact AdSense publisher line after an ID is issued; do not invent one. |
| AdSense account/Policy Center | **Unknown** | No account evidence supplied. |

Google publisher policies prohibit ads on screens without publisher content, with low-value content, under construction, used mainly for navigation/behavioral purposes, or containing replicated content without added value. The current surface includes several of those risk patterns. This audit does not claim that Google has issued a violation; the account evidence is unavailable.

### 10.3 Domain answer

Google's AdSense site-management guidance permits certain platform subdomains when the platform is on the Public Suffix List. `onrender.com` is listed, so **the Render subdomain is not the reason to assume automatic rejection**.

Still migrate to a custom domain because it provides:

- durable ownership independent of hosting;
- clearer brand/trust signals;
- cleaner Search Console, email, ads.txt and seller-transparency management;
- control over a future host migration;
- less startup/demo appearance.

A custom domain will not repair low-value content. Migrate only after route/redirect architecture is stable, and monitor the move in Search Console.

### 10.4 AdSense application gate

Do not apply until all are true:

- no indexable placeholders or misleading provider pages;
- every monetized template has substantial publisher value;
- dead controls and false labels are gone;
- privacy disclosures match actual network requests;
- consent behavior passes region-appropriate clean-browser tests;
- existing vignette/interstitial code is removed during review;
- source/config files are not publicly served;
- all aliases redirect and sitemaps are accurate;
- authorship, sourcing and corrections are visible;
- mobile navigation and accessibility pass;
- Search Console shows no Manual Action/Security Issue and desired pages are indexable;
- AdSense account/Policy Center requirements are resolved;
- ads are excluded from search, error, legal, empty, noindex and utility-only pages.

---

## 11. UX, accessibility and performance

### 11.1 Misleading streaming-app model

The current interface borrows the language of a streaming service—Watch Now, Match, HD, provider channels, My List and Rate—without providing streaming, a match algorithm, verified quality, real service catalogues or functioning list/rating features.

That is a product-trust problem, not merely a design preference. The redesign should use task-accurate labels:

- `Play official trailer`;
- `Open verified application`;
- `Source checked 4 Sep 2026`;
- `Subscription / Rent / Buy`;
- `Reviewed by …`.

### 11.2 Lighthouse results

Synthetic mobile-profile results from the audit environment:

| Template | Performance | LCP | Transfer | Requests | Key issue |
|---|---:|---:|---:|---:|---|
| Home | 65 | 6.2 s | 1,581 KiB | 21 | Large hero/LCP, global CSS, analytics |
| Sports | 71 | 4.7 s | 682 KiB | 24 | Late JS data/rendering |
| Make Money | 81 | 3.9 s | 250 KiB | 11 | Slow text paint despite low weight |
| Search | 90 | 3.2 s | 276 KiB | 9 | Embedded catalogue payload/architecture |
| Dune title | 85 | 1.5 s | 2,826 KiB | 50 | YouTube autoplay/player traffic; TBT 580 ms |
| Thor title | 90 | 1.7 s | 2,135 KiB | 49 | YouTube autoplay/player traffic |
| Editorial article | 94 | 2.7 s | 631 KiB | 20 | Article image/assets |
| Tech | 97 | 1.3 s | 246 KiB | 8 | Relatively light baseline |

Lighthouse gave many pages an SEO score of 100 while this audit found major quality, trust and index-control defects. This illustrates why Lighthouse SEO is a checklist, not a Google-readiness score.

### 11.3 Root causes

- global CSS is approximately 263 KB; Lighthouse estimated about 86% unused on the homepage;
- the global script is approximately 62 KB and serves unrelated verticals;
- GA/GTM transferred roughly 172 KB and contributed about 293 ms blocking in the audited home trace;
- title autoplay transferred roughly 1.6–2.3 MiB of YouTube traffic before intentional interaction;
- the homepage loads oversized/competing hero imagery;
- the Netflix channel HTML alone is about 225 KB because hundreds of cards are emitted into one document.

### 11.4 Accessibility

Automated accessibility scores were generally 93–100, but the audit found:

- contrast failures across several representative templates;
- sports heading-order issues;
- 10–11px navigation/search text in some views;
- title-page navigation removed on desktop;
- controls whose accessible names promise behavior that does not exist.

Target WCAG 2.2 AA and perform keyboard/screen-reader testing; automated scores alone are insufficient.

### 11.5 Performance gates

- click-to-load lightweight video embed; no YouTube requests before play;
- template-specific CSS/JS rather than one global legacy bundle;
- responsive AVIF/WebP images with dimensions and fallbacks;
- pagination or deliberate finite collections rather than 493-card documents;
- server/static rendering for critical jobs and sports facts;
- field p75 targets: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 after sufficient data exists;
- internal initial-transfer budgets defined per template.

---

## 12. Competitor benchmark and the lesson for BRYME

The purpose of the benchmark is not to copy layouts. Leading products win through defensible value and operational reliability.

| Space | Illustrative leaders | Defensible value pattern | BRYME gap | Achievable BRYME angle |
|---|---|---|---|---|
| Entertainment discovery | JustWatch, IMDb, Rotten Tomatoes, Letterboxd, TMDB | Deep entity data, regional availability, critic/community identity, reliable graphs and links | Generic descriptions; unverified channel availability; no clear rating method | Small Nigeria-focused “where to watch + verified trailer + editor note” collection |
| Sports scores/data | Flashscore, Sofascore, ESPN | Breadth, speed, data reliability, live operations, alerts, specialist reporting | Broken updater, wrong standings invariant, thin generated reports | Narrow licensed league utility or original editorial only |
| Nigeria/Africa jobs | Jobberman, MyJobMag, LinkedIn, employer ATS boards | Employer relationships, inventory, recency, applications and local context | No jobs product yet; stale-source risk | Human-verified Nigeria/Africa eligibility and direct employer links |
| Remote/startup jobs | Wellfound, Remote OK and specialist boards | Clear filters, recency, company context, alerting | “Remote” eligibility can be misread; no expiry system | Conflict-checked eligibility, verified-at timestamp and closure monitoring |
| Opportunity/finance guidance | NerdWallet-style methodology publishers, FlexJobs, ProBlogger and official source directories | Editorial standards, testing/vetting, disclosures and trust | Missing authors/dates/status on many pages | Transparent verification ledger and direct-source-first advice |
| African tech publishing | TechCabal, Techpoint Africa and specialist how-to publishers | Local reporting, named writers, sources, tested utility | Thin taxonomy and no demonstrated test method | Task-first tools/guides for Nigerian applicants and workers |

### What BRYME should copy

- named accountability;
- visible methodology;
- direct, current sources;
- task completion rather than card volume;
- a reason to return: alerts, saved verification, correction history or useful updates;
- original data/research that earns links;
- a narrow promise the team can keep.

### What BRYME should not copy

- the visual shell of Netflix without its rights/catalogue;
- live-score breadth without an operational data stack;
- high-volume job aggregation without authorization and expiry control;
- generic AI listicles;
- thousands of query/genre/year pages merely to increase URL count.

---

## 13. Recommended simplification and information architecture

### 13.1 Quality-first search surface

Do not treat all 1,377 routes as assets. Preserve the user-facing data where useful, but make search eligibility earned.

A practical temporary operational target is roughly **150–250 genuinely maintained indexable pages**, subject to Search Console evidence—not because Google prefers that number, but because it is a realistic quality ceiling for the current project. The exact retained set must be determined by the publishing gate and existing traffic/links.

### 13.2 Proposed navigation

```text
Home
├── Verified Opportunities
│   ├── Jobs in Nigeria
│   ├── Remote roles accepting Nigeria
│   ├── Paid writing calls
│   ├── Freelance / contractor opportunities
│   └── Verification method
├── Practical Tech
│   ├── Application tools
│   ├── AI/work workflows
│   └── Tested how-to guides
├── Watch (small pilot, optional)
│   ├── Verified trailers
│   ├── Nigeria availability
│   └── Original guides/reviews
└── About / Editorial method / Corrections / Privacy / Contact
```

Sports should not return to primary navigation until its data and editorial service level are dependable.

### 13.3 Retain / merge / noindex / delete framework

| Action | Use when | Current examples |
|---|---|---|
| **Retain and improve** | Distinct user task, original value, accurate facts, source proof, maintenance owner, contextual inlink | Strong Make Money pages; selected Tech guides; 24 entertainment editorials; selected title pilots |
| **Merge + 301** | Same intent or one page cannot justify itself | Microtasks → Remote Work; Writing Opportunities → Writing; duplicate/empty hubs |
| **Noindex while available** | Useful to some users but not yet competitive/verified for Search | Placeholders; current search utility; weak topic/year hubs; current sports detail inventory; unreviewed titles |
| **Delete/410** | No users, links, substitute, legal purpose or future value | Abandoned compiled pages after GSC/link review |
| **Redirect + remove physical file from publish output** | Old route has a clear replacement | Type-mismatch and duplicate-title aliases currently represented as `200` noindex files |

Do not block noindexed pages in robots until crawlers have processed the noindex. Do not mass-404 pages with clicks or links. Preserve a route migration map permanently.

### 13.4 Publishing gate

A page may be indexable only if all applicable checks pass:

1. a clear user task and distinct intent;
2. meaningful BRYME-created value;
3. facts verified against identified lawful sources;
4. author/editor and meaningful dates;
5. image/data rights recorded;
6. complete, accurate initial HTML;
7. at least one contextual inlink;
8. self-canonical `200` URL and correct sitemap state;
9. structured data matches visible content;
10. mobile navigation, accessibility and performance pass;
11. a named maintenance owner and review/expiry rule;
12. no misleading claim or dead control.

---

## 14. Jobs vertical: staged, verified and safe

### 14.1 Recommended launch model

Start with **dated editorial roundups**, not thousands of copied job pages.

Example format:

> “12 Nigeria-eligible roles verified 4 September 2026”

Each item links to the exact employer/ATS vacancy and shows what BRYME personally checked. Use Article markup for the roundup. Do not put `JobPosting` on a list page.

### 14.2 Verified source snapshot

Official-source research on 4 September 2026 found:

| Source | Snapshot evidence | Publishing decision |
|---|---|---|
| Moniepoint Greenhouse | 133 board openings; Nigeria-relevant roles present | Strong direct source; verify each leaf vacancy on publication day |
| Paystack careers | 8 ongoing roles | Strong direct source; do not imply Nigeria eligibility without role detail |
| M-KOPA Ashby remote filter | 11 remote-filtered openings | Inspect each description; “remote” may still be country-limited |
| SAND Technologies Greenhouse | 47 openings, including several Nigeria-labelled roles | Strong current source; verify leaf page and eligibility |
| Canonical | Active Africa/Nigeria-relevant engineering evidence | Verify role-level location and timezone |
| LILT | Active language/contract evidence | Clarify contractor status, language and location |
| Remotasks | Active contributor-board evidence | Label platform/contributor work accurately, not standard employment |
| Swoop | Nigeria-tagged evidence with conflicting metadata | Manual conflict review mandatory |
| Scale Army | Recruiting/staffing source with Nigeria-tagged evidence | Disclose agency role; reconcile conflicting location fields |
| Kuda SIWES | Direct Workable page said unavailable | **Do not publish as active** |

Full dated evidence: [`reports/jobs-source-snapshot-2026-09-04.csv`](reports/jobs-source-snapshot-2026-09-04.csv).

Counts are a dated snapshot, not evergreen facts.

### 14.3 Required job data model

Store at minimum:

```text
id
employer
employerType (direct / agency / platform)
title
sourceUrl (exact leaf vacancy)
sourceBoardUrl
sourceSystem
verifiedAt
verifiedBy
status
locationTextRaw
eligibleCountries
applicantLocationRequirements
workMode
employmentType
compensationRaw
currency
compensationPeriod
deadline
validThrough
applicationUrl
conflictNotes
firstPublishedAt
lastModifiedAt
nextCheckAt
```

Never infer salary, employment status, geography or remote eligibility. Preserve the source wording and record conflicts.

### 14.4 Verification workflow

1. Maintain a registry of direct employer and ATS sources.
2. Collect candidate links; do not automatically publish them.
3. Open the exact vacancy in a real browser on publication day.
4. Reconcile board card, JSON/API metadata and full job description.
5. Verify Nigeria/Africa eligibility, work mode, type, deadline and application path.
6. Record editor and timestamp.
7. Publish a dated roundup.
8. Recheck frequently; flag removed/changed pages for human review.
9. Mark closed promptly and retain a useful correction/archive record.
10. Never treat `403`, rate limiting or a search snippet as proof that a role is open or closed.

### 14.5 Stage 2: single-job pages

Only add single-job pages and `JobPosting` markup after BRYME has:

- permission/authorization or a clearly lawful feed/relationship;
- one page per real vacancy;
- a working application route;
- accurate visible data matching markup;
- `validThrough` and expiry automation;
- removal/404/410 or markup removal for closed roles;
- Search Console verification and tested Indexing API lifecycle where appropriate;
- no fees, fake employers or misleading aggregations.

Until then, direct-link editorial curation is safer and more differentiated.

### 14.6 Jobs differentiator

BRYME should not compete on raw job count. Compete on **eligibility confidence**:

- “Does remote really include Nigeria?”
- “Is this direct employer, agency or contributor platform?”
- “What exact location restriction did the employer state?”
- “When did a human last open the application page?”
- “What changed or conflicted?”

That is original editorial work and a product users can trust.

---

## 15. Rebuild architecture

### 15.1 One source of truth

Move to one content/data model and one deterministic renderer. A lightweight static generator such as Astro/Eleventy—or a disciplined custom build—is sufficient unless genuine server functionality is required.

Recommended structure:

```text
/content        # authored Markdown/MDX and editorial records
/data           # normalized catalogue/jobs/sports records
/templates      # versioned page families
/public         # explicit public static assets only
/build-output   # generated deploy artifact; never repository root
/redirects      # route manifest consumed by hosting/runtime
/tests          # content, schema, route, deployment and UI gates
```

### 15.2 Build rules

- clean checkout + one command must reproduce output;
- generators may not patch compiled HTML in place;
- a diff touching an unexpectedly large route count fails pending approval;
- public output is allowlisted;
- route status, canonical, sitemap and redirect come from one manifest;
- source facts include source URL, checked time and rights/provenance;
- index eligibility is an explicit field calculated by quality gates;
- staging must be `noindex` and protected from accidental production indexing.

### 15.3 CI gates

Fail deployment for:

- an indexable placeholder;
- an indexable route without canonical/title/H1/contextual inlink;
- sitemap/noindex/non-200 mismatch;
- redirect loop or chain;
- source/config file in the publish artifact;
- inaccurate required schema fields or placeholder dates;
- sports `GD != GF − GA`;
- expired active job;
- missing author/source/review date on trust-sensitive content;
- broken internal route;
- failed representative browser/a11y smoke test.

---

## 16. Prioritized implementation roadmap

The machine-readable backlog contains 43 items with priority, dependency, effort and acceptance test:

- [`reports/remediation-backlog.csv`](reports/remediation-backlog.csv)

### Phase 0 — preserve and measure

- tag/backup the current production state;
- collect Search Console, Analytics, AdSense and Render evidence;
- freeze destructive generators;
- protect pages with demonstrated clicks/links while they are triaged.

### Phase 1 — containment (P0)

- noindex/remove 55 placeholders;
- noindex/archive 88 thin reports;
- remove/noindex branded provider channels;
- disable Monetag and stop tracking until policy/consent match;
- restore navigation, remove dead controls and stop video autoplay;
- deploy only a public artifact;
- activate redirects and one URL form;
- repair robots rules;
- repair sports workflow and standings invariants;
- regenerate honest sitemaps and News sitemap.

### Phase 2 — foundation (P1)

- establish one source/build pipeline;
- add `indexEligible` gates;
- move to a custom domain with measured redirects;
- triage all 736 detail pages using traffic, quality and provenance;
- rebuild schema and image provenance;
- add authors/dates/sources/status to opportunity content;
- merge thin Tech/Make Money hubs;
- replace stale tests and add deployment/content CI;
- split CSS/JS and meet template budgets.

### Phase 3 — focused product (P2)

- launch the simplified information architecture;
- publish verified jobs roundups;
- rebuild practical Tech around applicant/user tasks;
- run a small entertainment pilot only if BRYME can supply unique regional/editorial value;
- restore sports only with dependable lawful data;
- implement region-appropriate privacy controls and a Google-certified CMP where required.

### Phase 4 — prove quality before monetization

- monitor Page Indexing, query/page performance and crawl behavior;
- collect real-user Core Web Vitals;
- run correction/freshness audits;
- earn links through original useful research, not volume;
- apply to AdSense only after every readiness gate is signed off.

### What not to do

- do not run `node scripts/build-static-foundation.js` against the live branch;
- do not generate more year/genre/title/job pages to “look bigger”;
- do not buy a domain and assume SEO is fixed;
- do not apply to AdSense while Monetag/privacy/placeholder issues remain;
- do not scrape IMDb;
- do not publish jobs from snippets or stale third-party posts;
- do not mass-delete before Search Console/backlink review;
- do not trust a green workflow when errors are explicitly suppressed.

---

## 17. Definition of done

### Search readiness

- [ ] zero unintended indexable orphans;
- [ ] zero indexable placeholders;
- [ ] zero sitemap/indexability/status mismatches;
- [ ] every alias is a one-hop 301 to one canonical URL;
- [ ] slash policy is enforced;
- [ ] no source/configuration route returns `200`;
- [ ] robots rules test as intended;
- [ ] schema is accurate, visible and source-backed;
- [ ] all retained pages pass the publishing gate;
- [ ] Search Console shows no unresolved Manual Action or Security Issue;
- [ ] priority routes show expected canonical/index status in URL Inspection;
- [ ] field Core Web Vitals meet targets where sufficient data exists.

### AdSense readiness

- [ ] privacy policy matches actual requests;
- [ ] consent is correctly implemented and revocable where required;
- [ ] Monetag/interstitial behavior removed during review;
- [ ] no ads planned for empty/search/error/legal/noindex/utility screens;
- [ ] original publisher value is obvious across the primary section;
- [ ] navigation and controls are complete and non-misleading;
- [ ] owner, editorial method, authors and corrections are visible;
- [ ] domain/site ownership verified in the AdSense account;
- [ ] Policy Center/rejection issues resolved;
- [ ] correct `ads.txt` line published only after the real publisher ID exists.

### Jobs readiness

- [ ] every active item uses the exact direct leaf URL;
- [ ] every item has a named verifier and `verifiedAt`;
- [ ] remote/Nigeria eligibility is checked from full role details;
- [ ] agencies/platforms are disclosed;
- [ ] conflicts receive human review;
- [ ] stale/closed records are updated promptly;
- [ ] no JobPosting markup appears on roundup/list pages;
- [ ] single-job schema is used only after authorization and lifecycle automation.

---

## 18. Audit artifacts

| Artifact | Purpose |
|---|---|
| [`reports/site-inventory.csv`](reports/site-inventory.csv) | Row-level metrics for all 3,377 HTML files |
| [`reports/site-audit-data.json`](reports/site-audit-data.json) | Aggregated counts and route lists |
| [`reports/hidden-indexable-routes.csv`](reports/hidden-indexable-routes.csv) | All 64 objective hidden/indexable routes and decisions |
| [`reports/remediation-backlog.csv`](reports/remediation-backlog.csv) | 43 implementation tasks with acceptance tests |
| [`reports/jobs-source-snapshot-2026-09-04.csv`](reports/jobs-source-snapshot-2026-09-04.csv) | Dated employer/ATS hiring evidence and caveats |
| [`reports/make-money-external-link-status.csv`](reports/make-money-external-link-status.csv) | 121 outbound-link checks |
| [`reports/browser-render-audit.json`](reports/browser-render-audit.json) | Rendered mobile/desktop behavior |
| [`reports/current-lighthouse/`](reports/current-lighthouse/) | Nine Lighthouse JSON reports |
| [`reports/route-audit.json`](reports/route-audit.json) | Route validation results |
| [`reports/build_full_inventory.py`](reports/build_full_inventory.py) | Reproducible inventory builder |
| [`reports/build_hidden_route_appendix.py`](reports/build_hidden_route_appendix.py) | Reproducible hidden-route classifier |
| [`reports/check_make_money_links.py`](reports/check_make_money_links.py) | Reproducible external-link checker |

Audit artifacts are currently uncommitted. Website behavior and production content were not modified.

---

## 19. Primary external guidance used

### Google Search

- [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Spam policies for Google Web Search](https://developers.google.com/search/docs/essentials/spam-policies)
- [Optimizing for generative AI features: valuable, non-commodity content](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [How Google interprets robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt)
- [Build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google News sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap)
- [Video SEO best practices](https://developers.google.com/search/docs/appearance/video)
- [Video structured data](https://developers.google.com/search/docs/appearance/structured-data/video)
- [JobPosting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting)
- [`site:` search operator limitations](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site)

### AdSense and privacy

- [Google-served ads on screens without publisher content / low-value content](https://support.google.com/adsense/answer/10502938)
- [Manage sites in AdSense and public-suffix subdomains](https://support.google.com/adsense/answer/12170421)
- [Google-certified CMP requirements](https://support.google.com/adsense/answer/13554116)
- [EU user consent controls](https://support.google.com/adsense/answer/7670013)

### Platform/data

- [IMDb data use in software](https://help.imdb.com/article/imdb/general-information/can-i-use-imdb-data-in-my-software/G5JTRESSHJBBHTGX)
- [Render custom domains](https://render.com/docs/custom-domains)
- [Public Suffix List](https://publicsuffix.org/list/public_suffix_list.dat)

---

## Final conclusion

BRYME's main problem is not IMDb, the lack of a domain, or one missing SEO tag. It is the mismatch between **the number and confidence of its claims** and **the evidence, originality and operational systems behind them**.

The fastest route forward is not to beautify all 3,377 HTML files. It is to:

1. contain the misleading/unfinished index surface;
2. make deployment, routing, privacy and data trustworthy;
3. choose one audience and one product promise;
4. publish a much smaller body of accountable, source-backed work;
5. use Search Console evidence to expand only what earns and deserves visibility;
6. seek AdSense review only after the product passes that standard.

That is the massive upgrade: fewer claims, fewer indexable pages, better evidence, better operations and a product people can trust.
