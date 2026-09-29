# BRYME Production Audit & Safe Improvements

**Audit date:** 2026-09-29
**Repository baseline:** `main` at `e850a1e` (shallow/partial checkout)
**Release status:** pushed to GitHub on `audit/seo-home-writers-fixes-2026-09-29`. No production deployment was performed; the branch is isolated from `main`.

> **Scope note:** This is an evidence-led audit pass with one targeted repair, not a claim that every page, data record, device state, or Search Console result has been exhaustively inspected. The repository was intentionally kept partial; production output was sampled live. Search Console, GA4 reporting, Lighthouse, field Core Web Vitals, and real CMP behavior were not available for this pass.

## Executive summary

BRYME is a seven-desk static publishing and tools ecosystem, not a conventional app backed by a production Node API. The live primary sitemap is materially smaller than the brief’s historical estimate: **2,583 unique URLs** across eight child sitemaps. Sampled pages generally had self-canonicals, one H1, `index,follow` where expected, and parseable JSON-LD. The live `robots.txt` allows general crawlers, excludes source-oriented paths, and lists the primary sitemap and desk sitemaps.

The most consequential confirmed implementation defect was in Home: its custom renderer already returned a complete HTML document, then the generator wrapped it in a second shared document shell. This affected **279 of 288 materialized Home `index.html` pages in each of three trees**. The generator and affected artifacts have been repaired locally: page bodies, titles, canonicals, and JSON-LD are preserved; two inconsistent meta/OG descriptions were reconciled to the more detailed route-level values already supplied to the shared shell. The published Home subtree is **6,865,080 raw HTML bytes (6.55 MiB, 36.8%) smaller** after removing the duplicate shell. This is not a measured Core Web Vitals improvement, and the change is not live until a full build passes and a separate deployment is authorized.

The highest remaining risks are (1) legacy URL paths that return `200` noindex pages with zero-second meta refreshes instead of HTTP redirects; (2) an unreferenced sitemap-index alias that omits the film catalogue; and (3) the inability to verify Google indexation or real consent behavior without Search Console/browser access. The Writers hub’s 92-vs-99 count mismatch has a source-verified generator fix staged locally but is not yet live.

**Largest opportunity:** use Search Console and consent-respecting analytics to find which existing guides, tools, and databases earn useful impressions and repeat use, then improve those clusters instead of increasing URL count. **Largest current risk:** sampled live Home pages still served nested document shells; the local correction is not deployed. A complete build/test and separate deployment approval are required before production is fixed.

**No content was deleted, no URLs were changed, and no new pages were generated.** Safe local changes include the Home document repair, a Writers aggregate-count correction, regression checks, the retired-host fallback, and stale repository documentation updates.

## What is working

- The live root and seven desk sections return successfully. The active Sport and Entertainment desks are present; a noncanonical legacy test URL must not be used to infer either section is retired.
- The primary sitemap contains 2,583 unique same-host URLs with non-future `lastmod` values, no query strings, and the expected trailing-slash pattern. `robots.txt` references the primary index and all eight child sitemaps.
- Sampled indexable pages had self-canonicals, one H1, and parseable JSON-LD. Sampled noindex search and migration routes were distinguishable from substantive pages.
- `/writers/writing/` is a substantial opportunities product, not a job board: the live page describes 142 researched publications and explicitly says a listing is an invitation to pitch, not a job offer or promise of payment. A sampled record showed source guidelines, eligibility, pay, a human-check date, and BRYME’s own experience with payment still unconfirmed.
- The house privacy page now mentions Money (the older external finding that Money was omitted is stale). The house page is `noindex,follow`; sampled desk privacy pages are indexable and disclose GA4, AdSense, cookies, and consent.
- A fabricated unknown URL returned a real 404/noindex page. `/writers/search/` is noindex with a clean canonical; a query-string search variant canonicalizes to the base search route.

## What is broken or needs follow-up

- **Home double document — repaired locally, not released.** 279 Home article/section pages had two nested document shells. This can cause browser/parser ambiguity, duplicate metadata and scripts, and unnecessary payload. See the implementation and verification section below.
- **Legacy migration stubs — review needed.** Probed `/writing/`, `/writing-opportunities/`, `/jobs/`, `/opportunities/`, `/make-money/`, and `/search/` returned `200` noindex pages with zero-second meta refreshes rather than HTTP redirects. `/writers/writing/by-country/` showed a further refresh hop. This is not proof that every such page is harmful; map each old path and its query behavior before choosing an exact 301 or a true 404/410.
- **Sitemap alias — inconsistent.** `/sitemap.xml` contains an eight-child index; `/sitemap_index.xml` is a live seven-child alias that omits the 719-URL catalogue. Robots does not reference the alias. It was deliberately left unchanged because Search Console submission history and hosting behavior were not available.
- **Writers status totals — live mismatch, generator corrected locally.** The live hub reports 92 “currently accepting,” while its filter says “Accepting now — 99.” Source status labels define deadline records as open until their stated dates. `build-writing-first.py` now counts `open + rolling + active deadline` in the hero, matching the filter; a read-only check of the 142-record source gives 99 for both. The production page still needs a full build and authorized deployment.
- **Static deployment vs runtime API — operational mismatch.** Repository `render.yaml` defines a Render static site publishing `public/`. Live `/healthz` and `/api/index/status` probes returned 404. The checked-in local test server and Indexing API helper are not evidence of live production endpoints.
- **Consent — presence is not behavior.** GA4 (`G-0KEKJH9960`), the AdSense loader, and the Funding Choices bootstrap appeared in sampled markup. A static fetch does not show whether a CMP dialog appears, whether choices update tags, or whether account settings match the repository.
- **Security hardening — verify at the edge.** Sampled responses had CSP, `X-Frame-Options`, `X-Content-Type-Options`, Referrer-Policy, Permissions-Policy, and COOP. The CSP permits broad HTTPS scripts and inline styles. HSTS was not observed on three samples; confirm domain/subdomain policy before enabling it.

## Technical SEO findings

| Finding | Affected URLs | Severity | Evidence | Recommendation / status |
|---|---|---:|---|---|
| Nested HTML document in Home output | 279 non-root Home pages per tree (`ecosystem/home/`, `home/`, `public/home/`) | **P1** | Eight live non-root pages sampled before the fix had duplicate `html/head/body/title`; source shows `_home_page()` returns a document and `write_service()` wrapped it in `shell(...)`. Full local trees: 279/288 duplicated; two inner meta/OG descriptions differed from the richer route-level description. | Generator and all three materialized artifact trees fixed locally. Bodies, titles, canonicals, and JSON-LD are preserved; the two conflicting meta/OG descriptions now use the richer route-level values. Run the full build and release gates before any authorized deployment. |
| Legacy roots use meta refresh with HTTP 200 | Sampled `/writing/`, `/writing-opportunities/`, `/jobs/`, `/opportunities/`, `/make-money/`, `/search/`; also `/writers/writing/by-country/` | **P2** | Live GETs returned noindex pages with zero-second refreshes; not HTTP 301s. One sample is a refresh chain. | Build an exact migration table using current routes, parameters, backlinks and Search Console. Replace only true moved routes with exact redirects; keep search semantics intact; return 404/410 only when no genuine replacement exists. No redirects changed. |
| Sitemap-index alias omits catalogue | `/sitemap_index.xml` | **P2** | Live alias lists seven child sitemaps; primary `/sitemap.xml` lists eight, including 719 catalogue URLs. Alias is not in `robots.txt`. | Check Search Console submissions and CDN/static-host behavior first. Do not remove or update merely to make the two files match. |
| Primary sitemap inventory | Eight child sitemaps | **Good, monitor** | 2,583 unique URLs: Writers 511; Sport 197; Entertainment editorial 183; Tech 373; Fitness 187; Home 291; Money 122; catalogue 719. Home’s 291 includes `/`, `/about/`, and `/event-calendar/`; the local Home subtree has 288 pages. | Retain the allowlist-based indexation model. Reconcile sitemap entries to status, canonical, robots, and content value—not raw repository file counts. |
| Raw `index.html` counts exceed sitemap | Repository `public/**`, `ecosystem/**`, nested trees | **P2 investigation** | Git-tree count: 3,942 `public/**/index.html`, 2,769 `ecosystem/**/index.html`, and 3,277 nested `index.html` paths outside those trees. These counts include possible noindex pages, stubs, copies, and non-routed artifacts. | Classify the complete publish tree into indexable, noindex, redirects/stubs, utility pages, and source copies before calling the gap an indexation defect or deleting anything. |
| Search/filter behavior | `/writers/search/`, `?q=...`, `/search/` | **Good with legacy alias** | Writers search is `noindex,follow` and canonicalizes query variants to the base search route. `/search/` is a 200 meta-refresh alias to the Writers search surface. | Keep result/filter states out of sitemaps. Review whether the alias can become an exact redirect without losing query behavior. |
| Slash variant | `/tools/json-formatter` | **P3** | No-slash route returned 200 with a canonical to `/tech/tool/json-formatter/`. | Not a demonstrated indexing defect. Consider a 301 only if static-host rules can implement and test it reliably. |
| Retired-host fallback | Generator origin helper | **P2, fixed locally** | `site.config.json` selects `https://thebryme.com`, but `bryme_config.py`’s last-resort default was `bryme.onrender.com`. | Fallback now matches the current apex domain. Test verifies the configured value and `SITE_URL` override; normal builds already using the config are unchanged. |
| Writers acceptance metric | `/writers/writing/` | **P2, fixed in generator locally** | Live summary says 92; filter says 99. Source labels say deadline records are open until their stated date; read-only evaluation of `content/opportunities.json` gives 99 active records. | Generator now counts open, rolling, and non-expired deadline records in both places. Confirm in a full build; the live artifact remains unchanged until deployment. |
| Structured data / metadata | Sampled root and desk pages | **No broad defect established** | Sampled canonicals matched tested routes; indexable samples had one H1 and parseable JSON-LD. | Continue full-tree validation in CI. Do not add schema to writing opportunities as if they were employer vacancies. |

### URL-classification strategy

| URL type | Observed behavior | Recommended handling |
|---|---|---|
| Canonical editorial, guide, tool, category, and useful database pages | 200, sampled self-canonical; sitemap-listed when intended | Keep indexable if the page has independent value, stable content, and internal links. Preserve trailing-slash canonicals. |
| Search/filter combinations | `/writers/search/` is noindex; query variants canonicalize to the base | Keep noindex and out of sitemaps; retain functionality. Do not block CSS/JS needed by the UI. |
| Legacy moved routes | Several roots are 200 noindex meta-refresh stubs | Map each source to the exact destination, including parameters. Use 301 only for a genuine move; use 404/410 where there is no replacement. Avoid homepage redirects. |
| Root privacy and desk privacy | Root policy is noindex; sampled desk policies are indexable | Compare content and Search Console value; choose a consistent policy strategy only after that review. No privacy indexing change made. |
| Alias sitemap index | Seven-child stale alias; not referenced by robots | Confirm Search Console and host behavior before updating, redirecting, or removing. |
| Unknown/fabricated route | 404 with noindex | Retain useful 404 behavior; do not redirect every missing URL to `/`. |

### `robots.txt` and discovery

The live file allows `User-agent: *`, disallows repository-oriented paths such as `/scripts/`, `/content/`, `/docs/`, `/server/`, `/ecosystem/`, and a recovered Entertainment path, and references `/sitemap.xml` plus the desk sitemaps. Google-facing CSS/JS lives under `/assets/`, which is not disallowed. Several named third-party crawlers are explicitly disallowed by policy. The primary index and child sitemaps parsed successfully in the live audit; all 2,583 primary URLs were unique and same-host, with valid non-future `lastmod` values.

No Search Console sitemap status was available, so sitemap acceptance, actual indexed counts, excluded reasons, crawl stats, and canonical selection by Google remain unknown.

## Section analysis

These are live sitemap counts and representative checks, not a full editorial or safety review of every record.

| Desk | Sitemap URLs | Findings and next action |
|---|---:|---|
| **Writers** | 511 | Strong differentiated opportunity product: `/writers/writing/` lists 142 researched publications and sample records show source guidelines, eligibility, verification date, and honest BRYME experience. The 92-vs-99 live mismatch is fixed in the generator using the same active statuses as the filter; full build/deployment remains. Keep search/filter results noindex. Do not label publication submissions with `JobPosting`. |
| **Tech** | 373 | Sampled guides/tools had expected metadata and parseable JSON-LD. `/tools/json-formatter` without a slash returns the canonical slash page. Full topic-cluster and link-depth audit was not rerun. |
| **Sport** | 197 | Active section and included in the primary sitemap. Sampled routes passed basic metadata/canonical checks; live table/fixture freshness and archive boundaries were not exhaustively checked. |
| **Entertainment** | 183 editorial + 719 catalogue | Both editorial and catalogue inventories appear in the primary sitemap. A prior `/movie/the-invite/` probe was not the sitemap-derived canonical route and must not be used to claim the catalogue is broken. Per-catalogue content quality was not re-audited in this pass. |
| **Fitness** | 187 | Sampled routes passed basic structural checks. Medical/health-claim safety and tool usability need a dedicated review. |
| **Home & DIY** | 291 including three family-root URLs | 288 local Home pages, of which 279 had nested document shells. All 279 were normalized in source/routed/published trees; no URLs or page bodies were removed. Recheck safety guidance separately; this change addressed document structure only. |
| **Money** | 122 | `/money/privacy/` returns 200 and the root privacy page mentions Money. Sampled Money pages had expected metadata; jurisdiction coverage was not exhaustively audited here. |

## Performance and mobile

No Lighthouse run, CrUX/field Core Web Vitals, or device/browser session was available, so no LCP, CLS, INP, TTFB, or mobile-usability score is claimed. The Home repair removed duplicate shell markup and reduced the raw bytes across the `public/home/` HTML subtree by 6.55 MiB (36.8%); compressed transfer savings and user-perceived speed were not measured. GA4 and AdSense loaders are each present once in the sampled Home output; consent behavior was not exercised in a browser.

Next measurements should use a reproducible mobile Lighthouse run and field CWV where available, then inspect LCP image delivery, layout shifts, JS execution, caching, and the real impact of any ad placements. Do not infer a CWV gain from HTML bytes alone.

## Trust, privacy, ads, and security

- `/privacy/` and seven desk privacy routes return 200. The house page is `noindex,follow` and mentions Money; sampled desk policies are `index,follow` and disclose GA4, AdSense, cookies, and consent.
- `site.config.json` enables GA4 and AdSense verification. Sampled markup carried one GA loader, one AdSense loader, and a Funding Choices bootstrap. The `_ads_slot` helper has no call sites, and sampled HTML contained no manual AdSense `<ins>` units. The repository note says to keep Auto ads off; the dashboard setting cannot be verified from HTML.
- Consent Mode defaults and the Funding Choices script are present in the code/output, but this does **not** prove a dialog appears, that regional selection updates tags correctly, or that the CMP is active in AdSense. Test in a real browser for EEA/UK/CH and verify account settings before enabling placements. No legal-compliance claim is made.
- Live response samples included CSP and common framing/content/referrer/permissions headers. HSTS was not observed in three samples. Review at the CDN/hosting edge; tighten CSP only with a complete inventory of required third-party scripts and styles.
- No full dependency, source-secret, CORS, or penetration scan was run in this partial checkout.

## Monetization opportunities

Current evidence supports **readiness work, not a revenue forecast**: AdSense verification is configured but manual ad units are unwired, and `affiliate.enabled` is false. Recommended order:

1. Validate the actual CMP/consent flow and privacy disclosures; keep ad units/Auto ads off until the owner confirms settings and usability.
2. If enabled, test sparse, clearly separated placements and measure viewability, CLS, and mobile usability before expanding.
3. Measure the Writers opportunity database and tools first. If repeat usage supports it, test optional, clearly priced alerts or research features without withholding basic verification and submission details.
4. Consider newsletter signup or sponsorships only with a real provider/relationship, explicit consent/disclosure, and an owner-approved workflow. The current configuration is `mailto`, not a verified email-capture service.
5. Keep affiliate links disabled until providers are active and placement/disclosure rules are implemented. No traffic, conversion, or revenue data was available.

## Prioritized roadmap

### Immediate — 0–7 days

1. From a complete checkout or CI, run a clean install/build, `npm test`, the HTTP gate, and Playwright/mobile checks. Confirm all Home routes retain one document, the published mirrors are correct, and sitemaps/URL counts are unchanged. This could not be run from the intentionally sparse checkout.
2. Review the Writers status source and reconcile 92 vs 99 “accepting” results.
3. Create an old-to-new route table for the sampled meta-refresh stubs, including query strings and `by-country` chains. Use Search Console/backlink evidence before applying exact 301s or true removals.
4. Check whether `/sitemap_index.xml` is submitted or referenced by external tools; keep the current alias unchanged until its role is known.
5. The user requested a GitHub push but not a production deployment. The audit is pushed to `audit/seo-home-writers-fixes-2026-09-29`; keep it off `main` until full build/release gates pass. No Render deployment was performed.

### Short term — 1–4 weeks

- Use Search Console exports to compare the 2,583 sitemap URLs with indexed/canonical/excluded reports. Classify the larger public artifact inventory instead of treating every file as indexable.
- Use GA4 reports with appropriate consent to identify useful landing pages, tool engagement, return use, and conversion paths.
- Test the CMP for EEA/UK/CH, confirm the real AdSense account state, and check privacy behavior—not just source markup.
- Run mobile Lighthouse and field CWV checks; review HSTS/CSP and caching at the static host/CDN edge.
- Review internal-link paths and content freshness by desk using current allowlists and actual queries. Prioritize improvements to existing useful pages; do not set raw URL targets.

### Medium term — 1–3 months

- Reconcile sitemap, allowlist, canonical, status code, and robots state for each route class; instrument a regression report in CI.
- Audit the Writers opportunity dataset for dated-source freshness and consistent filter/count semantics.
- Complete desk-specific checks: Tech cluster pathways; Sport data timestamps/archive status; Entertainment catalogue value; Fitness safety; Home task safety; Money jurisdiction labels.

### Long term — 3–12 months

- Run measured product experiments around opportunity alerts, tools, sponsorship, and carefully disclosed affiliate relationships only after usage and consent data supports them.
- Review indexation quality and returning-use metrics quarterly. The success metric is useful indexed pages and product engagement—not the number of generated URLs.

## Changes made in this audit

- `scripts/build-ecosystem.py`: Home full-document renderers now bypass the shared wrapper; Home’s bespoke head includes the missing common AdSense/analytics head and icons. Generator comments/log output reflect the current host/static-path architecture.
- `scripts/bryme_config.py`: emergency site-origin fallback now uses `https://thebryme.com`; the fallback site description now matches the current Writers product rather than the former jobs/remote-work description.
- `scripts/validate-site-quality.js` and `scripts/validate-http.js`: added exactly-one-doctype regression checks for eligible routed pages and the published Home artifact.
- `scripts/build-writing-first.py`: hero accepting-count now shares the filter’s normalized active-status set; source data check returns 99/99.
- `ecosystem/home/`, `home/`, `public/home/`: 279 nested pages per tree normalized (837 files total); nine single-document files per tree were left unchanged.
- `README.md`, `BRYME-AUDIT-FINDINGS.md`, and `ROADMAP.md`: corrected verified stale architecture, indexation, hosting, privacy/consent, monetization, and Pinterest-status statements; added findings and next steps.

## Validation performed and not performed

**Passed:**

- Python AST/syntax checks for the touched Python generators/config and Writers generator.
- `node --check` for both touched JavaScript validators.
- Read-only status-count check against the 142 records in `content/opportunities.json` at `e850a1e`: active-status hero total and filter total both evaluate to 99.
- `git diff --check`.
- Structural scan of all 288 local Home HTML files in each tier: one doctype, `html`, `head`, `body`, `title`, H1, and canonical; no failures.
- Root `home/` and `public/home/` copies match byte-for-byte across all 288 pages.
- Published Home pages each carry one GA bootstrap, one AdSense loader, and one Funding Choices reference.
- Comparison against the original `HEAD` public Home files: all 279 inner body sections, titles, canonicals, and JSON-LD were preserved; two shorter inner meta/OG descriptions were reconciled to their richer outer route-level values. Net published Home HTML reduction: 6,865,080 bytes.
- Origin helper test: configured apex and `SITE_URL` override both work.

**Not run / not available:**

- Full generator build, `npm test`, or the complete HTTP/Playwright gate; repository dependencies and most of `public/` are not present in this partial checkout.
- Real mobile-browser testing, Lighthouse, CrUX, Search Console, GA4 export, AdSense dashboard, or CMP interaction testing.
- Full page-by-page content safety/fact-check, all-route canonical/redirect audit, dependency/security scan, or orphan-link analysis.

The repaired artifacts are in the workspace, but production remains unchanged until a full build/test and an explicitly authorized deployment.
