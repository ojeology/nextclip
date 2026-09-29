# BRYME

BRYME is a family of seven specialist publications with one shared hub: **Writers, Tech, Sport, Entertainment, Fitness, Home & DIY, and Money**. The site combines editorial, verified opportunity records, databases, browser tools, and calculators; it is not a single job board or an ad-only blog.

**Current public host:** <https://thebryme.com/>

> A homepage fetch of the former `bryme.onrender.com` host returned a `Not Found`
> body on 2026-09-29. Do not rely on that origin to serve content, redirects, or
> verification files. The current public hostname is `thebryme.com`; generated
> canonical and discovery URLs should follow `SITE_URL`.

**Project owner:** Ojeology

## Publication focus

- **Writers:** paid-publication and writing-opportunity records, editorial guides, templates, checklists, and browser tools.
- **Tech:** practical technology explainers, comparisons, and utilities.
- **Sport:** football and other sport coverage, explainers, data, and calculators.
- **Entertainment:** reviews, viewing guides, and a structured film catalogue.
- **Fitness:** evidence-aware training guides, plans, and tools.
- **Home & DIY:** low-risk repair, maintenance, safety, and household-cost guidance.
- **Money:** saving and trading education, calculators, and jurisdiction-labelled financial explainers.

The Writers desk distinguishes the original opportunity source, BRYME's verification record, and first-hand experience. It never claims to own a vacancy or publication opportunity that belongs to another organisation, and never claims payment until it is confirmed.

## Custom-domain readiness

Generated absolute URLs are resolved through `scripts/bryme_config.py`: `SITE_URL` takes precedence over `site.config.json` → `siteUrl`. The committed site URL and the live primary sitemaps use `https://thebryme.com`; the former Render hostname still appears in historical code, migration notes, and archived material, so a repository-wide string match is not evidence that it is emitted to users. Before changing any legacy-host routing, confirm the exact canonical destination and hosting behavior.

The live `/sports/` and `/entertainment/` sections are active. Do not infer that a media catalogue or route family is retired from a noncanonical test URL; check the current Entertainment sitemap and migration map before deciding whether to redirect or retire a historical path. The published artifact currently has no `410.html`.

## Build

```bash
npm ci
npm run build
```

The build is static-generator driven. `npm run build` rebuilds the Writers publication, routes the committed desk trees into the published `public/` artifact, applies the policy injectors, and regenerates discovery files (robots, sitemaps, RSS, and `llms.txt`) from explicit allowlists.

`python3 scripts/build-ecosystem.py` is a separate generator for the seven desk source trees under `ecosystem/`; it is **not** in the `npm run build` chain. When changing a desk's generator/data, run it deliberately and commit the resulting `ecosystem/` output before the normal build. This avoids silently publishing stale generated desk pages.

## Release gates

```bash
npx playwright install chromium
npm test
```

The release gates inspect indexability, canonicals, structured data, internal links, Writers records, discovery files, HTTP status codes, redirects, public-file containment, and security headers. Playwright exercises the configured route set at mobile, tablet, and desktop sizes, checking navigation, overflow, images, console errors, landmarks, and third-party resource leakage. Route and case counts vary with the allowlist; use the latest test output rather than treating an old count as current.

`npm run validate:contrast` additionally enforces the readability rules that the
moving-navigation regression broke:

- every measured text/background pair meets **WCAG 2.1 AA** (4.5:1 normal,
  3:1 large), with translucent layers alpha-composited the way a browser paints
  them — token changes that quietly reduce contrast now fail the build;
- **navigation never animates or auto-scrolls on its own** (a nav that drifts
  moves links out from under the pointer and made text unreadable);
- the country filter is a **static selection control**, never a scrolling bar,
  and always offers an "All countries" reset plus a worldwide option;
- a **home link with an accessible name** is present in the header of every page.

## Navigation policy

Motion in navigation must be functional, never decorative. Section navs are
static; the only scripted movement is bringing the current page's link into
view. Any bar that scrolls text under the reader, or animates a background
behind it, is a defect — `validate-contrast.js` will reject it.


## Current Search policy

- A live production crawl on 2026-09-29 found **2,583 unique URLs** in the primary sitemap: Writers 511, Sport 197, Entertainment editorial 183, Tech 373, Fitness 187, Home 291 (including the family root, `/about/`, and `/event-calendar/`), Money 122, and the Entertainment catalogue 719. Treat this as a dated sitemap inventory, not as a raw-URL growth target; classify noindex pages and migration stubs separately.
- `/sitemap.xml` and `robots.txt` expose the primary eight-child sitemap index. The legacy `/sitemap_index.xml` alias currently contains only seven children and omits the catalogue; do not remove or alter it until Search Console/submission history and hosting behavior are checked.
- No News sitemap routes are admitted without timely original reporting.
- Treat publication submissions as writing opportunities, not employment vacancies; never apply `JobPosting` schema to them. Any real employer-vacancy schema requires a complete, current source record and visible page content.

Policy lives in:

- `content/index-allowlist.json`
- `content/news-allowlist.json`
- `scripts/build-discovery.py`

## Server and deployment

```bash
npm start
```

`server/server.js` is a local static-artifact test server used by the repository's HTTP gate; its health and indexing-control endpoints are not automatically deployed just because they exist in the checkout. The repository's `render.yaml` defines a **Render static site** that publishes `public/`, not a Node Web Service. Production probes on 2026-09-29 found `/healthz` and `/api/index/status` return 404. Do not depend on those runtime endpoints for production indexing; if they become a requirement, deploy and test a separate API service deliberately.

## Writers opportunity records

The live `/writers/writing/` hub currently describes 142 researched publications. A sampled record exposes its pay and word-count terms, eligibility, official guideline, last human-check date, and BRYME's own submission journey; payment remains explicitly unconfirmed until received. Keep this source-vs-BRYME-experience distinction and recheck time-sensitive listings against the publisher's own page.

## JobPosting schema and indexing endpoints

Writing opportunities are invitations to pitch, **not employment vacancies**; do not label them with `JobPosting` schema. The legacy roots `/jobs/`, `/opportunities/`, `/writing/`, and `/writing-opportunities/` currently serve 200 noindex meta-refresh stubs to Writers destinations rather than HTTP redirects. Map these destinations and review Search Console/backlink history before replacing them with exact 301s. The checkout contains a local Google Indexing API helper, but production `/api/index/status` returned 404 on 2026-09-29; do not describe that helper as a live API without a separately deployed and tested service.

## Privacy and monetization

**AdSense is configured for account verification; ad units were not found in sampled output.** `site.config.json` sets `adsense.enabled: true` with the owner-supplied publisher ID, and sampled live pages contained the account meta tag and AdSense loader. The `_ads_slot` helper has no call sites, and sampled pages had no rendered `<ins class="adsbygoogle">` units. The site config says to keep Google-dashboard Auto ads **off**; that account setting cannot be verified from page HTML.

GA4 is enabled in `site.config.json` (`G-0KEKJH9960`) and the loader was present in sampled live pages. Consent Mode v2 defaults are emitted from a separate asset and the Funding Choices bootstrap appeared in sampled Home/Writer/root markup. This static evidence does **not** prove that a consent dialog appears, that regional choices update tags correctly, or that production AdSense settings match the repository. Verify the CMP with a real browser in EEA/UK/CH test locations and in the AdSense dashboard before treating consent behavior as compliant or enabling ad units. Privacy pages disclose GA4, AdSense, cookies, and consent; that disclosure alone does not validate implementation.

The browser test gate intercepts analytics/ad hosts to stay deterministic, so it does not validate live third-party consent behavior. See `docs/ecosystem/revenue-readiness.md` and `docs/ADS.md` before wiring ad placements; ads must never resemble job cards or application buttons.
