# BRYME deployment — single service, path-based routing

**Current mode: `path`** — one Render static service serves THE BRYME hub at `/` and all five
publications under path prefixes. Subdomains are a config flip, not a rebuild (see below).

## The five publications

| Publication | Path on the Render service | Future subdomain |
| --- | --- | --- |
| THE BRYME (hub) | `/` | thebryme.com |
| BRYME Writers (flagship) | `/writers/` | writers.thebryme.com |
> **Route decision — Home & DIY lives at `/home`** (not `/diy`): it matches the planned
> `home.thebryme.com`, and the property identity (fix/clean/maintain/understand/improve) is
> broader than DIY. Never create both.
>
> **Money was removed from the ecosystem entirely** (route, nav, config, sitemaps, robots).
> Its retired research files stay unpublished in `content/` (`make-money-articles.json`,
> `money-*.json`). Writer-specific money content (rates, invoicing, taxes) remains in
> BRYME Writers where it belongs.
| BRYME Sports | `/sports/` | sports.thebryme.com |
| BRYME Tech | `/tech/` | tech.thebryme.com |
| BRYME Entertainment | `/entertainment/` | entertainment.thebryme.com |
| BRYME Fitness | `/fitness/` | fitness.thebryme.com |
| BRYME Home & DIY | `/home/` | home.thebryme.com |

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

## Render deploy behaviour (important)

- `render.yaml` sets the build command to `npm install --omit=dev && npm run build &&
  python3 scripts/build-ecosystem.py && python3 scripts/build-routing.py`. **Render only
  re-reads `render.yaml` on a blueprint sync** — until someone syncs in the Render dashboard,
  deploys run `npm run build` alone. The chain is built to be correct either way:
  - `build-public-dir.py` (last npm step) stages the routed site from the committed
    `ecosystem/` output — hub at `/`, properties at their prefixes, unprefixed duplicates of
    `writers/` content excluded;
  - `build-discovery.py` picks the allowlist artifact by tree shape (routed artifact when
    `writers/` exists in the checkout — always true on Render);
  - when the python steps DO run, `build-routing.py` rebuilds `public/` itself afterwards and
    has the final word.
- The npm build's `|| echo` fallback masks build failures with exit 0 — a failed build still
  deploys the committed `public/`. That fallback is what kept the site correct while the
  allowlist/build mismatch was being fixed; treat any "deploy succeeded but output looks
  pre-routing" as a masked build failure and run the chain locally.
- Cloudflare sits in front of `bryme.onrender.com` and ignores query strings for its cache key —
  after a deploy, URL checks can return stale layers from previous deploys for a few minutes.
  Verify with `cf-cache-status`/`age` headers before diagnosing.

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
