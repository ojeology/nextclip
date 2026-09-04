# BRYME

BRYME is a focused publication for **verified jobs, remote work and legitimate ways to earn** — primarily for Nigerians and Africa-based readers.

**Current public host:** <https://bryme.onrender.com/>

**Project owner:** Ojeology

## Publication focus

- **Jobs:** exact employer/ATS records with visible verification dates, Nigeria and location-first discovery (country → city → job type).
- **Remote work:** a dedicated remote hub and remote-eligible roles.
- **Make Money:** grounded platform, freelance, writing and income-opportunity guidance without guaranteed-earnings claims.
- **Writing:** language contracts plus researched paid-publication guidelines, including BRYME's own tested journeys.
- **Guides:** practical application, portfolio, account-safety and independent-publishing help.

BRYME **verifies opportunities** — it distinguishes the original source, BRYME's verification record, and first-hand experience. It never claims to own a vacancy that belongs to another employer or platform, and never claims payment until it is confirmed.

## Custom-domain readiness

Every generated absolute URL (canonical, sitemap, JSON-LD, Open Graph, robots) comes from a single source of truth: the `SITE_URL` environment variable, falling back to `site.config.json` → `siteUrl`. Set `SITE_URL` to the custom domain to repoint the whole site without touching code. No `bryme.onrender.com` host is hard-coded in the build (`scripts/bryme_config.py`).

Sports, movie, series, anime and entertainment-editorial files were extracted to the separate [`ojeology/bryme-media`](https://github.com/ojeology/bryme-media) repository. Media route families return HTTP 410 on this publication until a stable media hostname is deployed and permanent redirects can be installed.

## Build

```bash
npm ci
npm run build
```

The deterministic content build:

1. creates the shared forest-green stylesheets;
2. builds the focused hubs, 13 individual job records, five populated job categories and trust pages;
3. applies idempotent indexability, schema, navigation and performance policy; and
4. regenerates robots, sitemap, News sitemap and RSS from explicit allowlists.

## Release gates

```bash
npx playwright install chromium
npm test
```

The release gates inspect every retained HTML file, indexability, canonicals, structured data, internal links, jobs, writing records, discovery files, media removal, HTTP status codes, redirects, public-file containment and security headers. Playwright renders all 58 Search-eligible routes at mobile, tablet and desktop sizes, then checks navigation, overflow, images, console errors, landmarks and third-party resource leakage.

## Current Search policy

- 58 focused routes are eligible for indexing.
- 55 paid-publication detail records remain `noindex` until each source is individually reverified.
- No News sitemap routes are admitted without timely original reporting.
- No `JobPosting` structured data is published yet: the current source records do not consistently contain the complete job-description and original posting-date fields needed for responsible markup.

Policy lives in:

- `content/index-allowlist.json`
- `content/news-allowlist.json`
- `scripts/build-discovery.py`

## Server and deployment

```bash
npm start
```

`server/server.js` provides a strict public-file boundary, canonical routing, 301 work-hub consolidation, 410 responses for migrated media families, real 404 responses, security headers, `/healthz`, and the guarded Google Indexing API control endpoints (`GET /api/index/status`, `POST /api/index/notify` — see `docs/INDEXING.md`).

Use the Node 22 Web Service defined in `render.yaml`; a generic static deployment will not preserve all HTTP behavior.

## Verification system

Job cards and detail pages show a verification badge (🟢 SOURCE VERIFIED, 🔵 APPLICATION CHECKED, 🟣 BRYME TESTED, 🔴 CLOSED, ⚠️ NEEDS RECHECK), a last-verified date, verification note, an official source link with an explicit "SOURCE: …", and a "Report an outdated listing" control. Writing-opportunity detail pages record BRYME's own first-hand journey (pitch submitted → accepted → scheduled → published → paid) without claiming payment until it is actually received.

## JobPosting structured data and indexing

`JobPosting` JSON-LD is emitted **only** for roles explicitly flagged `jobPosting.eligible` in `content/jobs.json` with complete source fields. It is never used for closed or historical records, and `hiringOrganization` is always the employer — never BRYME. The Indexing API module (`server/indexing-api.js`) is dry-run by default and also limited to `/jobs/` pages. See `docs/INDEXING.md`.

## Privacy and monetization

Advertising and analytics remain disabled. `site.config.json` → `adsense` is the single switch: set `caId` (a real `ca-pub-...`), review consent/privacy, and enable only after the release gates pass. Ads must never resemble job cards or application buttons (see `docs/ADS.md`).
