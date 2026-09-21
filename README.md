# BRYME

BRYME is a focused publication for **verified jobs, remote work and legitimate ways to earn** — primarily for Nigerians and Africa-based readers.

**Current public host:** <https://thebryme.com/>

> The former `bryme.onrender.com` origin is **retired and unreachable**: Render
> blocks the subdomain (`x-render-routing: blocked-render-subdomain`) and every
> URL there returns a plain-text 404, so it cannot serve redirects, a 410, or an
> IndexNow key file. Those URLs decay on recrawl. Nothing in the published
> artifact links to that host; it survives only inside the dated audit snapshots
> under `reports/`, which are historical records and are deliberately immutable.

**Project owner:** Ojeology

## Publication focus

- **Jobs:** exact employer/ATS records plus job-board listings with visible verification dates, and global, location-first discovery (choose your country → city → job type). Board-listed roles are labelled separately (⚪ LISTED ON JOB BOARD) so they are not confused with BRYME-checked employer pages.
- **Remote work:** a dedicated remote hub and remote-eligible roles.
- **Make Money:** grounded platform, freelance, writing and income-opportunity guidance without guaranteed-earnings claims.
- **Writing:** language contracts plus researched paid-publication guidelines, including BRYME's own tested journeys.
- **Guides:** practical application, portfolio, account-safety and independent-publishing help.

BRYME **verifies opportunities** — it distinguishes the original source, BRYME's verification record, and first-hand experience. It never claims to own a vacancy that belongs to another employer or platform, and never claims payment until it is confirmed.

## Custom-domain readiness

Every generated absolute URL (canonical, sitemap, JSON-LD, Open Graph, robots) comes from a single source of truth: the `SITE_URL` environment variable, falling back to `site.config.json` → `siteUrl`. Set `SITE_URL` to the custom domain to repoint the whole site without touching code. No origin is hard-coded in the build (`scripts/bryme_config.py`). The retired `bryme.onrender.com` string now survives in exactly two places: the dated audit snapshots under `reports/` (historical records, deliberately immutable), and the body prose of `/tech/render-deployment-failures-what-they-taught-me/`, which is an article *about* that incident. No generated link, canonical, sitemap or Open Graph URL points at it.

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

The release gates inspect every retained HTML file, indexability, canonicals, structured data, internal links, jobs, writing records, discovery files, media removal, HTTP status codes, redirects, public-file containment and security headers. Playwright renders all 509 allowlisted Writers routes at mobile, tablet and desktop sizes (1,527 render cases), then checks navigation, overflow, images, console errors, landmarks and third-party resource leakage.

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

- 2,032 routes are eligible for indexing (routed allowlist v26). Of the 2,640 published `index.html` files, 608 stay `noindex`.
- All 142 paid-publication detail records under `/writers/writing/` are indexable — the 55 held back for re-verification have since been reverified. The only `noindex` page in that tree is `/writers/writing/by-country/`, a navigational filter rather than a record.
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

**AdSense account verification is live; ad units are not.** `site.config.json` → `adsense` is the single switch, and it is currently `enabled: true` with an owner-supplied `caId` (`ca-pub-1881426210393009`). That injects the account meta tag and the `pagead2.googlesyndication.com` loader into `<head>` on every page, and emits `ads.txt` — which is what Google's verification check needs. **No ad unit renders**: `_ads_slot` has no call sites, so nothing is placed until the owner wires them. Keep Google-dashboard Auto ads **off** until then. Analytics remain disabled.

Two consequences worth knowing:

- The browser gate intercepts the AdSense loader (`AD_HOSTS` in `scripts/validate-browser.js`) so the 1,527 render cases stay offline-safe and deterministic. `www.google.com` is deliberately *not* in that list, so a real Google leak would still fail the gate.
- EEA/UK personalised ads require a **certified CMP**. That decision is still open and must be made, and documented on the privacy pages, before ad units are wired. See `docs/ecosystem/revenue-readiness.md`.

Ads must never resemble job cards or application buttons (see `docs/ADS.md`).
