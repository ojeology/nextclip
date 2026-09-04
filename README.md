# BRYME

BRYME is a source-first Nigerian publication for verified opportunities, practical technology and original entertainment editorial.

**Current public host:** <https://bryme.onrender.com/>

**Project owner:** Ojeology

## Editorial focus

- **Verified jobs:** dated links to exact employer or applicant-tracking-system vacancies, with Nigeria eligibility and work-location caveats.
- **Practical technology:** task-first guides for Nigerian and Africa-based readers.
- **Opportunities:** researched earning and application guidance without guaranteed-income claims.
- **Watch & Read:** original entertainment recommendations and commentary.

Legacy movie, series, anime and sports interfaces remain available only as contained archives. They are excluded from Search unless explicitly admitted by `content/index-allowlist.json`. Automated sports publishing is paused pending source-rights and production approval.

## Build

The public site is deterministic and has no package dependencies:

```bash
npm run build
```

That command builds the lean editorial stylesheet and focused pages, applies the idempotent audit remediation, then regenerates robots, sitemap, News sitemap and RSS from explicit policy files.

Do **not** run `scripts/build-static-foundation.js` casually. It is a destructive historical generator and requires `ALLOW_DESTRUCTIVE_BUILD=1`.

## Release gates

```bash
npm test
python3 scripts/validate-browser.py  # requires Chromium, ChromeDriver and Selenium
```

The Node gate validates indexability, canonicals, schema, titles, sports integrity, links, discovery files, jobs, provenance, deployment hardening and workflows. It also starts the production server locally and tests the HTTP contract.

## Server and deployment

Production should run:

```bash
npm start
```

`server/server.js` provides:

- an explicit public-file allowlist;
- canonical redirects;
- real 404 and 410 responses;
- security headers;
- the read-only competitions endpoint; and
- health checking at `/healthz`.

`render.yaml` defines the intended Node 22 Render Web Service. A generic static deployment will not enforce the same routing and security behavior.

## Search and discovery policy

- `content/index-allowlist.json` — routes permitted to be indexable and included in the standard sitemap.
- `content/news-allowlist.json` — timely, original reporting eligible for Google News discovery; intentionally empty until a route qualifies.
- `scripts/build-discovery.py` — generates `robots.txt`, `sitemap.xml`, `news-sitemap.xml` and `feed.xml` from those policies.

Do not add a URL merely because a page exists. It must be useful, original, accurate, visibly sourced and maintained.

## Privacy and monetization

Third-party advertising and analytics are disabled. Trailer players load only after explicit interaction. Do not reintroduce ad or tracking code until deployed behavior, privacy disclosures and any required consent platform are reviewed together.

## Audit records

- `BRYME_FULL_SITE_AUDIT_2026-09-04.md` — complete baseline audit.
- `BRYME_REMEDIATION_COMPLETION_2026-09-04.md` — implemented fixes, release evidence and owner-only next actions.
