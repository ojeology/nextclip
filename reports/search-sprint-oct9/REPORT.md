# BRYME — five-page search improvement release

Research and implementation: 9 October 2026. Owner authorised publication after choosing the publish option.

## Scope and evidence

Five existing canonical URLs were improved; no new near-duplicate articles or URL changes. Baseline metrics are from the owner's Markdown GSC summary for 20 September–8 October, not a direct GSC connection. The summary contains inconsistent aggregate counts, and page-specific query/country/device exports are still unavailable. This is a factual/content-quality intervention with selective metadata changes, not a controlled title-only experiment or a promised CTR lift.

| Page | Baseline clicks | Impressions | Average position | Intervention |
|---|---:|---:|---:|---|
| Noema | 0 | 149 | 6.19 | Direct submission answer, 500-word minimum, explicit unknown rate, accurate case-by-case AI permission, substantive pitch checklist |
| Literary Hub | 0 | 134 | 8.22 | Correct accepted/excluded formats, 2–3 paragraph requirement, no invented pay/reply deadline, useful preparation advice |
| The Drift | 0 | 107 | 8.85 | Separate section inboxes, all four rates, poetry/fiction requirements, explicit AI restriction, remove misleading speed/deadline advice |
| Alice in Borderland recommendations | 5 | 579 | 8.79 | Preserve existing title and URL; ten actual series, clear format labels, direct chooser, differences and source links |
| Deadpool & Wolverine recommendations | 0 | 106 | 7.77 | Twelve distinct released films, individual reasons and caveats, remove unsupported streaming promise and unreleased recommendation |

Exact routes, new titles/descriptions and baseline figures: `content/search-improvements/pages.json`.

## Important corrections

### Writers

Official sources were read, not inferred from search snippets:

- Noema: https://www.noemamag.com/contact/ and its linked guidelines at https://docs.google.com/document/d/1Hu8dZS6s6HhT3mYeVmTZS0KyMJama4xtURsZPRj81sY/edit (read via export). No published standard commission rate. Required AI disclosure is not automatic permission; use is considered case by case. The existing firsthand rejection record was not converted into a payment claim.
- Literary Hub: https://lithub.com/how-to-pitch-lit-hub/ . Finished essays are permitted, but original fiction, poetry and current interview pitches are not. The page says it reads everything, not that it replies within a particular period. Previous clips are requested if available, not presented as mandatory for every applicant.
- The Drift: https://www.thedriftmag.com/about/ . Official page states $2,000 essays, $500–$1,000 short stories, $150 poems, $25 Mentions; a 2–4 paragraph nonfiction pitch; separate fiction and poetry inboxes; and excludes anything written by AI. Its essay development may take months, contrary to the old appended copy implying speed. The old AI field was incorrect and the source record now reflects the restriction.

The new pages do not call this an editor interview, new firsthand submission or human research conducted by the owner. They say official sources were checked. Unstated terms remain unstated. Removed boilerplate that treated silence after a couple of weeks as a rejection, and the blanket claim that any submission fee makes a publication illegitimate. Cross-links connect the three distinct editorial fits and the existing pitch guide.

### Entertainment

The existing Alice page counted Final Destination among ten shows. This update removes it from the TV list, substitutes 3%, replaces the unspecified Liar Game entry with the documented The 8 Show, and correctly identifies The Devil's Plan as reality competition. Most previous recommendations remain, but now each names its format and the limits of the comparison. The existing title is intentionally retained to avoid attributing future changes solely to a new headline.

The old Deadpool page promised legal viewing options without a country-specific verified listing and recommended Avengers: Doomsday as an available follow-up. Marvel's official page lists 18 December 2026: https://www.marvel.com/movies/avengers-doomsday . It is removed from the recommendations and the correction is visible. The page now has twelve distinct released films, not twelve undifferentiated names or an unreleased review. No Nigerian streaming availability is inferred from US studio pages. Similarity comparisons are editorial judgement, not a claim of a fresh screening.

Premise sources are linked in the copy: official Netflix title pages; HIDIVE's No Game No Life overview; IMDb's Tomodachi Game listing; Warner Bros' The 100 and The Suicide Squad pages; 20th Century Studios film pages; Marvel's film pages; Sony's No Way Home page. Some Netflix pages returned generic text to direct Python requests but the page-fetch tool returned the full listings. Marvel pages that blocked Python requests could be read with the page-fetch tool for Thor/Guardians; Ant-Man links are reference destinations, not newly verified regional availability claims. The source inventory records all linked external destinations, not an assertion that every outgoing page was fully audited.

## Implementation

- `content/opportunities.json`: authoritative records for Noema, Literary Hub and The Drift updated; verified dates advance only for these three records.
- `content/search-improvements/*.html`: maintained editorial copy for five pages.
- `content/search-improvements/pages.json`: titles, descriptions, route manifest and supplied baseline metrics.
- `scripts/build-search-improvements.py`: deterministic, dependency-free final build step. It replaces only these five editorial main sections inside existing site shells, preserving ad slots and external consent/analytics wiring. Running after legacy content injectors prevents generic filler from being appended after reviewed copy.
- `package.json`: append this step to the existing full build.
- Writers root/public and Entertainment source/root/public artifacts updated; same canonical URLs and indexability preserved.
- Matching child-sitemap lastmod values updated to the actual revision date. No new URL, FAQ rich-result promise, fake rating or invented engagement statistic.
- Article JSON-LD headline, description and modification dates match visible copy; Entertainment's original published date remains 9 September 2026. Breadcrumb labels updated consistently.

These five bodies intentionally replace verbose legacy dockets/filler with publication-specific guidance and film/show comparisons. Existing unrelated page content is not part of this release. Shared hub outputs may update on a production build because the three authoritative publication records changed; those are expected derived effects, not a separate mass rewrite.

## Validation

- Full `npm run build`: passed. Existing Sports media import validator: 2,584 source/public pages passed.
- Focused tests: all five pages have one H1, unchanged self-canonical, indexable robots, correct title/description, one matching Article, true modification dates and sitemap entries.
- Internal article links and TOC anchors resolve; exactly ten numbered shows and twelve numbered films.
- Re-running editorial step leaves pages unchanged: idempotence passed.
- Chromium at 360, 768 and 1440px for all five pages: HTTP 200, no page-wide horizontal overflow, working TOC navigation. Noema mobile screenshot reviewed.
- Browser tests block third-party ad/analytics calls: tests validate first-party/editorial layout, not ad network behaviour.
- No new runtime dependency for the builder. Focused test script uses BeautifulSoup and optional Playwright, installed locally for testing only.

Not claimed: full site-wide npm test suite, field Core Web Vitals, Lighthouse score, Google index update, search ranking improvement or confirmed increased traffic. Release/deployment/IndexNow status is recorded separately after production verification.

## Measurement and next decision

Record the actual live deployment timestamp. In GSC, compare each exact URL's queries/country/device cohorts after 14 and 28 days, allowing more time where impressions are sparse. Keep the same search type and distinguish branded publication queries from submission-intent queries. Treat the owner-supplied metrics as a starting snapshot, not a reliable controlled baseline.

Suggested review dates: 23 October and 6 November 2026. The three Writers pages need query exports to test intent matching. Do not credit title changes alone for any improvement: body content, corrections and internal links changed together. Do not repeatedly resubmit unchanged URLs; notify IndexNow once after the release is live.
