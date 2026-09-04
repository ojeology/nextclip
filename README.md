# BRYME

BRYME is a focused Nigerian publication for verified jobs, paid-writing research, practical opportunities and work guides.

**Current public host:** <https://bryme.onrender.com/>

**Project owner:** Ojeology

## Publication focus

- **Jobs:** exact employer and ATS records with visible verification dates and Nigeria/location context.
- **Writing:** writing and language contracts plus researched paid-publication guidelines.
- **Opportunities:** grounded platform, freelance and income-skill guidance without guaranteed-earnings claims.
- **Guides:** practical technology, account safety, portfolio and independent-publishing help.

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

`server/server.js` provides a strict public-file boundary, canonical routing, 301 work-hub consolidation, 410 responses for migrated media families, real 404 responses, security headers and `/healthz`.

Use the Node 22 Web Service defined in `render.yaml`; a generic static deployment will not preserve all HTTP behavior.

## Privacy and monetization

Third-party advertising and analytics remain disabled. Do not reintroduce them until the final domain, consent requirements, privacy disclosures and ad placement are reviewed together. Ads must never resemble job cards or application buttons.
