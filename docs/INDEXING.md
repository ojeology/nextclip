# BRYME indexing, discovery and the Google Indexing API

BRYME does not infer Search eligibility from the existence of an HTML file.
Every indexable route must be named in `content/index-allowlist.json` and pass
the release validator.

## Build outputs

`python3 scripts/build-discovery.py` generates:

- `sitemap.xml` from the index allowlist;
- `news-sitemap.xml` from the separate News allowlist;
- `feed.xml` from eligible, dated editorial records; and
- `robots.txt` (which also `Disallow`s `/api/`).

All absolute URLs in these files follow one source of truth: `SITE_URL` (env) →
`site.config.json` → `siteUrl` (see `scripts/bryme_config.py`). The build rejects
missing routes, noindex allowlist entries, duplicate routes and invalid dates.

## Indexing API (Google, for eligible JobPosting pages)

The Indexing API is **an additional discovery notification mechanism, not a
guarantee of indexing**, and not a general-purpose indexer. BRYME uses it only
for genuinely qualifying `JobPosting` pages, never for ordinary articles, hubs
or guides.

### Module and endpoints

- `server/indexing-api.js` — dependency-free client. Validates the route
  (job pages only, `/jobs/...`), de-duplicates the same URL+type within a
  window, exchanges a service-account key for an OAuth token, calls
  `urlNotifications:publish` (or `delete`), logs every attempt with timestamp,
  URL, type and status to `server/indexing-log.jsonl`, and fails safely.
- `server/server.js` — guarded control endpoints:
  - `GET  /api/index/status` → `{ configured, site }`
  - `POST /api/index/notify {"url":"/jobs/<id>/","type":"published|updated|deleted"}`

The endpoints are secured by the `INDEXING_API_TOKEN` bearer secret. Without a
service-account JSON the module runs in **dry-run**: it logs what would be sent
and returns a clear message, without sending anything to Google.

### Configure

Set in the Render service (see `render.yaml`):

- `SITE_URL` — canonical origin.
- `INDEXING_API_TOKEN` — shared secret.
- `GOOGLE_INDEXING_CREDENTIALS` — path to a service-account JSON authorised for
  the Indexing API (leave empty to stay in dry-run).

### When to use / when not to

- Use for a real, currently open job page carrying valid `JobPosting` markup.
- Do **not** use for closed/expired jobs, hubs, guides or articles.
- Do not submit `deleted` unless the page is genuinely removed.
- A notification does not force indexing or ranking.

## Current policy

- Indexable: job hubs, source-check records, maintained guides, trust pages.
- `noindex` until individually reverified: the 55 paid-publication research
  detail pages.
- Empty location/type hubs are built but stay `noindex` until they hold real
  records.
- `JobPosting` structured data is only published for roles explicitly flagged
  `jobPosting.eligible` in `content/jobs.json`; none are emitted today until
  the source fields are complete.

## Release sequence

```bash
npm run build
npm test
```

After deployment, verify the canonical production host and submit `/sitemap.xml`
once in Search Console and Bing Webmaster Tools. Use URL Inspection for a small
number of genuinely new or materially improved pages. Do not automate bulk
submission.
