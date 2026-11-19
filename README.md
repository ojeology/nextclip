# BRYME

**BRYME Writers** — an independent publication for people who want to get published
and paid for writing: paid markets checked by hand, craft and pitching guides, and
private browser tools.

**Live:** <https://thebryme.com/> · **Owner:** Ojeology · **Editor:** Ibrahim Sodiq

BRYME publishes **one desk**. Everything on the domain — the homepage, `/about/`,
`/privacy/`, the Pinterest kit, the assets, the build pipeline — serves that desk.
There is no second publication, no media catalogue, and no leftover route for one.

## What the site contains

- **Paid markets (`/writers/writing/`)** — every record is built from the
  publication's own submission guidelines: pay, word count, eligibility,
  submission method, rights, AI policy, and the month it was last checked. Where a
  guideline does not state something, the record says *not stated* rather than
  estimating it.
- **Craft and pitching guides (`/writers/learn/`)** — 197 guides from first pitch
  to final draft, written from primary sources and labelled honestly.
- **Browser tools (`/writers/tools/`)** — 49 tools (counters, readability and
  passive-voice checkers, rate and tax calculators, invoice and contract builders,
  PDF and document tools). Everything runs locally in the browser; nothing typed
  into a tool is uploaded.
- **BRYME Articles (`/writers/articles/`)** — the desk's editorial section: reported
  stories about people, life, money and the world around us, in five categories.
  It is a section of this desk, not a second publication, and it carries no story
  until a real one is published — the landing page, the category pages, the sitemap
  entries and the editorial invitation are all generated from `content/articles/`.
  See `docs/BRYME-ARTICLES.md` for the behaviour and `content/articles/README.md`
  for how to publish a story.
- **Trust pages** — about, editorial policy, verification statuses, corrections,
  disclosure, terms, disclaimers, copyright and privacy, plus the house pages at
  `/about/` and `/privacy/`.

## Layout of the published site

```
/                     house hub (from ecosystem/hub)
/about/               house about page (from ecosystem/hub/about)
/privacy/             house privacy policy (from ecosystem/hub/privacy)
/writers/…            the entire publication, canonical home for every page
/writers/articles/…   BRYME Articles: the editorial section of that publication
/assets/…             shared CSS, JS and images
```

Every pre-routing and retired URL 301s to its routed twin, or — where no twin
exists — to the nearest real page. Rules are declared in `render.yaml`, mirrored for
the local test server in `_redirects`, and additionally enforced at file level inside
the build by `scripts/purge-stale-publish.py`, because a published file outranks an
edge rule.

## Build

```bash
npm ci
npm run build
```

The build is deterministic and ordered:

1. `build-writing-first.py` regenerates the publication tree at the repo root;
2. `build-writing-hub.py` adds the guide/tool surface;
3. `build-articles.py` builds BRYME Articles from `content/articles/` and writes the
   invitation payload (`assets/articles/invitation.json`);
4. `build-discovery.py` writes robots, sitemaps and RSS from explicit allowlists;
5. `build-landing.py` / `ecosystem/` produce the house hub and trust pages;
6. `build-routing.py` moves the publication under `/writers/` and partitions the tree;
7. `build-public-dir.py` stages `public/`, the directory Render publishes;
8. `purge-stale-publish.py` deletes stale legacy directories and writes the
   byte-stable redirect stubs;
9. the injectors add analytics, breadcrumbs, sources, consent and ad bands;
10. `build-llms-txt.py`, `trim-meta-descriptions.py` and `fix-stub-canonicals.py`
   finish the discovery surface.

`public/`, the root sitemaps and both index allowlists are committed build outputs.
CI re-runs the build with `SOURCE_DATE_EPOCH` pinned to the tree's own date and
requires an empty `git diff`, so any commit can be rebuilt byte-for-byte on a later
day. Production deploys set no pin and therefore stay date-fresh.

## Release gates

```bash
npx playwright install chromium
npm test
```

| Gate | What it proves |
| --- | --- |
| `verify:allowlist` | every route the builders generate is in the index allowlist |
| `verify:titles` | no duplicate or over-budget titles |
| `verify:dockets` | every market record renders its full docket |
| `validate` (`validate-site-quality.js`, `validate-http.js`) | indexability, canonicals, structured data, retired routes gone, redirect stubs honest, containment of source files, security headers, method semantics |
| `validate:oppfilter` | the market filter's counts match the data |
| `validate:browser` | Playwright renders every allowlisted route at mobile, tablet and desktop |
| `validate:contrast` | WCAG 2.1 AA on every measured text/background pair |
| `check:adsense` / `check:brand` | AdSense readiness and house-consistency audits |
| `check:links` | no broken internal link anywhere in `public/` |

## Canonical origin

Every generated absolute URL (canonical, sitemap, JSON-LD, Open Graph, robots) comes
from one source of truth: the `SITE_URL` environment variable, falling back to
`site.config.json` → `siteUrl`. No origin is hard-coded in the build
(`scripts/bryme_config.py`); set `SITE_URL` to repoint the whole site without
touching code.

## Server and deployment

```bash
npm start
```

`server/server.js` is the local and gate-time static server for `public/`: a strict
public-file boundary, canonical redirects, redirect-rule replay, real 404s, security
headers and `/healthz`. Render publishes `public/` as a static site per
`render.yaml` (`staticPublishPath: public`, `autoDeploy: true`).

## Retired URLs and Render's static store

HTML deletions propagate: a page removed from `public/` stops serving, and every
retired route answers a noindex redirect stub (see `purge-stale-publish.py`).

**Binary and script deletions do not.** Render's static store is overlay-style: a
file that is deleted from the repository keeps answering 200 from the previous
deploy. That is why `purge-stale-publish.py` writes tombstones instead of relying on
deletion, and why the retired-desk asset paths (archived desk images, old calculator
scripts, the former `hub-robots.txt`) may still resolve for a while. They are
unreferenced — no page, sitemap or robots entry points at them — and the only way to
make such a URL stop answering is to publish something at the same path. If that ever
matters, the fix is a tombstone sweep in `purge-stale-publish.py`, not a re-import of
the retired files.

## Privacy and monetization

Advertising is configured in `site.config.json` and applied at build time by
`scripts/inject-ads.py`; the policy and change procedure are in `docs/ADS.md`.

- **Adsterra (primary network):** a native banner at the top of content pages, a
  classic display banner and a Social Bar (`adsterra.*`).
- **Google AdSense:** account verification only (`adsense.caId`, the `ca-pub` meta
  and loader, `ads.txt`). `adsense.nativeSlotId` is empty, so no AdSense ad unit
  renders. Keep Google-dashboard Auto ads **off**.

**Consent.** `/assets/adsterra-loader.js` applies one rule: outside the EEA, UK and
Switzerland units load at once; inside them nothing loads, and no request reaches an
ad host, until Google's consent message grants ad consent. `npm run test:ads` proves
it in a real browser. Google Analytics 4 runs with Consent Mode defaults scoped to the
same regions.

The browser gates intercept ad and analytics hosts (`AD_HOSTS` in
`scripts/validate-browser.js`) so every render case stays offline-safe and
deterministic; `www.google.com` is deliberately *not* in that list, so a real leak
would still fail the gate.

Ads must never resemble publication cards or tool buttons.

## Search policy

- Eligible routes are named explicitly in `content/index-allowlist.json`; nothing is
  indexable by accident, and the routed allowlist (`…routed.json`) is what
  `build-discovery.py` writes sitemaps from.
- No News sitemap routes are admitted without timely original reporting.
- Legacy URLs are never indexable: every stub carries `noindex,follow` and a
  canonical pointing at the page it forwards to.
