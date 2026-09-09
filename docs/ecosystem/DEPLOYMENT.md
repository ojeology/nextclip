# BRYME deployment — single service, path-based routing

**Current mode: `path`** — one Render static service serves THE BRYME hub at `/` and all five
publications under path prefixes. Subdomains are a config flip, not a rebuild (see below).

## The five publications

| Publication | Path on the Render service | Future subdomain |
| --- | --- | --- |
| THE BRYME (hub) | `/` | thebryme.com |
| BRYME Writers (flagship) | `/writers/` | writers.thebryme.com |
| BRYME Sports | `/sports/` | sports.thebryme.com |
| BRYME Tech | `/tech/` | tech.thebryme.com |
| BRYME Entertainment | `/entertainment/` | entertainment.thebryme.com |
| BRYME Money | `/money/` | money.thebryme.com |

## Build chain (run in this order)

```
npm run build                        # writers site at root (hub build restores content/index-allowlist.json to v24 form)
python3 scripts/build-ecosystem.py   # hub + sports + tech + entertainment + money into ecosystem/ (reads ecosystem/config.json)
python3 scripts/build-routing.py     # migrates the tree: writers/ -> writers/, props to root paths, hub to index.html
node scripts/validate-site-quality.js
python3 scripts/check-internal-links.py
```

Notes that will bite you if skipped:

- `content/index-allowlist.json` is derived. `npm run build` regenerates it from the clean root
  tree (489 writers routes); `build-routing.py` rewrites it to v25 (543 routes: writers-prefixed +
  `/` + property sitemap locations). It is idempotent, but **always start a full rebuild from a
  clean tree** (`rm -rf writers sports entertainment tech money public <root pages>` first) —
  the build walks whatever is on disk and will happily absorb stale routed state.
- `build-routing.py` owns: the `writers/` move, URL rewrites (63k+ hrefs, search-index `u` values,
  sitemaps, feeds), property copies from `ecosystem/`, the hub `index.html` + root `sitemap.xml`,
  the global `robots.txt` (5 sitemap declarations, no indexing directives), allowlist v25, the
  `public/` mirror, and the root `sw.js`/`favicon.ico` copies. Do not run `build-public-dir.py`
  after routing — it would clobber the mirror.
- `.git`, `.github`, `assets/`, `scripts/`, `content/`, `docs/`, `server/`, `reports/`,
  verification files (`google*.html`, `yandex_*.html`, `1740cdb…txt`), `package/render/site.config/BRYME*`
  stay at the root. Shared `assets/` are NOT duplicated per property.

## Configuration

`ecosystem/config.json`:

```json
{"domain": "thebryme.com", "mode": "path", "origin": "https://bryme.onrender.com",
 "subdomains": {"writers": "writers.thebryme.com", "sports": "sports.thebryme.com",
                "tech": "tech.thebryme.com", "entertainment": "entertainment.thebryme.com",
                "money": "money.thebryme.com"}}
```

`mode: "subdomains"` flips the builders to emit canonical/sitemap/og URLs on the subdomains
(`SUB` map in `build-ecosystem.py`, PREFIX mode in routing). Env overrides for CI:
`PRODUCTION_DOMAIN`, `ROUTING_MODE`, `ORIGIN`.

## Switching to subdomains later (deployment change only)

1. Set `mode: "subdomains"` in `ecosystem/config.json`.
2. Rebuild with the chain above (pages are emitted with subdomain canonicals; routing skips
   path-prefix rewrites).
3. Render: add the five custom domains; DNS CNAME each subdomain at the registrar when
   thebryme.com is purchased.
4. Canonicals move with the config; no page rewrites by hand, ever.

## Indexing posture (FINAL spec Step 8)

Indexing work is deliberately ON HOLD until the real domain is purchased: no noindex campaigns,
no IndexNow, no GSC/Bing submissions against the Render URL. `robots.txt` carries only the five
`Sitemap:` lines. The archive-recovery rule stands: recovered pages ship `noindex,follow` only
where the allowlist excludes them (9 pages: stubs and feeds).

## Quality gates

- `validate-site-quality.js` — allowlist v25 = sitemap = robots = indexable (543); per-page
  canonical/H1/main/lang checks on every allowlisted page; writers design-system checks scoped to
  `writers/` (property shells carry their own inline design tokens per FINAL spec Step 6).
- `check-internal-links.py` — 70,944 internal links resolve (post-routing count, 2026-09-09).
