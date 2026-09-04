# BRYME indexing and discovery

BRYME does not infer Search eligibility from the existence of an HTML file. Every indexable route must be named explicitly in `content/index-allowlist.json` and pass the release validator.

## Build outputs

`python3 scripts/build-discovery.py` generates:

- `sitemap.xml` from the index allowlist;
- `news-sitemap.xml` from the separate News allowlist; and
- `feed.xml` from eligible, dated editorial records.

The build rejects missing routes, noindex allowlist entries, duplicate routes and invalid dates. It does not emit `<priority>` or `<changefreq>`.

## Current policy

- Job hubs and individual source-check records can be indexable.
- Maintained work and technology guides can be indexable.
- Trust, author and legal pages can be indexable.
- The 55 dated paid-publication research details remain `noindex` until each official guideline is rechecked individually.
- News remains empty unless BRYME publishes timely original reporting that satisfies the News policy.
- Migrated media families are not part of this repository's index.

## Release sequence

```bash
npm run build
npm test
```

After deployment, verify the canonical production host and submit `/sitemap.xml` once in Search Console and Bing Webmaster Tools. Routine rebuilds update the same file; repeatedly resubmitting it does not force ranking or immediate crawling.

Use URL Inspection for a small number of genuinely new or materially improved pages. Do not automate bulk submission of low-value or unchanged URLs.
