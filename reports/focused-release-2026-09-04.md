# BRYME focused-release verification

**Release date:** 4 September 2026

**Publication:** jobs, paid writing, opportunities and practical guides

## Static integrity

- Retained HTML files checked: 118
- Explicitly Search-eligible routes: 58
- Pages carrying `noindex`: 59
- Main-repository media route families: 0
- Sitemap URLs: 58
- News sitemap URLs: 0
- RSS items: 25
- Internal-link, canonical, metadata, landmark and structured-data checks: passed
- Credential-pattern scan: passed

## Job publication

- Source-check records: 13
- Individual job pages: 13
- Populated categories: 5
- Explicitly remote-eligible records: 5
- Official employer/ATS URLs returning HTTP 200 during the release check: 13 of 13

A successful HTTP response is not treated as proof that a vacancy will remain open. Every page shows the check date and tells the reader to confirm the employer source before applying.

## Browser matrix

Playwright rendered every Search-eligible route at:

- 390 × 844 (mobile)
- 768 × 1024 (tablet)
- 1440 × 1000 (desktop)

Result: **174 of 174 route/viewport cases passed**.

The gate checks HTTP status, one H1, main and skip-link landmarks, substantial rendered content, horizontal overflow, current navigation, forest-green stylesheet loading, executable-script absence, image loading, third-party resource leakage, six-item mobile bottom navigation and fixed-navigation clearance. Separate browser checks confirmed the custom 404 and media-family 410 responses.

## HTTP and deployment behavior

Passed checks include:

- canonical trailing-slash redirects;
- consolidated work-hub 301 redirects;
- removed media-family 410 responses;
- genuine unknown-route 404 responses;
- blocked access to repository, configuration, content-data and report files;
- GET/HEAD behavior and 405 handling; and
- CSP, HSTS, referrer, permissions and MIME-sniffing headers.

## Contained research

The 55 paid-publication records checked on 19 August 2026 remain accessible for research but excluded from Search. They must not become indexable until each official guideline is reopened and its current state, pay wording, eligibility and URL are manually reverified.

## Reproduction

```bash
npm ci
npx playwright install chromium
npm run build
npm test
```
