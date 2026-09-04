# BRYME Money & Opportunities Rebuild — Implementation Report

Date: 4 September 2026 · Author: BRYME (Ojeology) technical implementation

This report covers the technical foundation rebuild of the **BRYME / NEXTCLIP**
repository (`ojeology/nextclip`) toward the new strategic direction described in
`BRYME-Money-Opportunities-Rebuild.md`. Per the brief's final objective, the
**technical foundation was built first** — the site was **not** mass-populated
with jobs. The implementation is complete and the deterministic build plus the
site-quality and HTTP release gates pass.

---

## 1. What this rebuild changed (summary)

The repo was already a focused work publication. This pass hardens and extends
it along the primary business objective: **a trustworthy platform for verified
jobs, remote work and legitimate ways to earn**, with the core differentiator
"**We verify opportunities.**"

### Achieved
- **Single configurable domain source** (`SITE_URL`) — custom-domain ready; no
  `bryme.onrender.com` is hard-coded anywhere in the build or server.
- **Central config module** (`scripts/bryme_config.py`).
- **Site-wide Organization + WebSite structured data** (with a `SearchAction`)
  on every page, plus a configurable `google-adsense-account` meta (off by
  default).
- **New information architecture** in the primary nav (Jobs · Remote · Make
  Money · Writing · Guides · About), a desktop search field, and a 7-item mobile
  bottom nav plus footer Legal column.
- **Location-first discovery**: country hub (`/jobs/nigeria/`) and city hubs
  (`/jobs/lagos/`, `/jobs/abuja/`, `/jobs/port-harcourt/`, `/jobs/ibadan/`,
  `/jobs/kaduna/`) plus new job-type hubs (`/jobs/entry-level/`,
  `/jobs/customer-service/`, `/jobs/sales/`, `/jobs/administrative/`). Empty
  hubs are built but stay `noindex` until they hold real records (no thin
  indexed pages).
- **Verification badge system** on job cards and detail pages
  (🟢 SOURCE VERIFIED / 🔵 APPLICATION CHECKED / 🟣 BRYME TESTED / 🔴 CLOSED /
  ⚠️ NEEDS RECHECK), with a verification note, last-verified date, explicit
  `SOURCE:` attribution, and a required `Apply on <source>` button.
- **Full job detail page structure**: title, employer, location, eligible
  locations, employment type, work mode, salary (only when confirmed),
  experience, education, deadline, summary, "who this suits", BRYME verification
  notes, application instructions, official source link, last verified, "Report
  an outdated listing" mailto, related jobs, and related guides.
- **JobPosting structured data infra** (gated — see §6) and a **Google Indexing
  API service** (module + guarded endpoints, dry-run by default).
- **Afrolicious case study** updated (§7) — reflects a real, confirmed journey
  (submitted → accepted → scheduled for publication), with payment **not**
  claimed until confirmed.
- **AdSense readiness** and **SEO** (canonical, sitemap, robots, breadcrumbs,
  clean URLs, no accidental noindex, custom-domain canonicalization).
- **Performance / mobile UX**: hubs are independently accessible pages (not a
  single in-memory app), lazy, minimal JS (no client scripts), responsive grids
  and bottom nav.

---

## 2. Files changed / added

### New files
- `scripts/bryme_config.py` — single source of truth for `SITE_URL`, site name/
  description, IndexNow key, and the AdSense publisher config.
- `server/indexing-api.js` — Google Indexing API client (dependency-free,
  JWT/OAuth2, dedup, logging, dry-run, job-pages-only).

### Modified build / config files
- `scripts/build-focus-site.py` — central config import; `BASE = cfg.site_url()`;
  site-wide `Organization`/`WebSite` graph; conditional AdSense meta; new nav/
  footer; `verify_state()` + badges; `job_card()`; location & type hub builders
  (`is_nigeria_location`, `job_city_slugs`, `job_is_remote`, `job_in_nigeria`,
  `location_hub_pages`, `type_hub_pages`, `_write_hub`); rewritten `jobs_index()`
  with location/type/category grids; rewritten `job_detail_pages()` with the full
  structure and gated `job_posting_schema()`; reframed `home()` hero.
- `scripts/apply-audit-remediation.py` — replaced every hard-coded
  `bryme.onrender.com` in JSON-LD/breadcrumb/canonical with `SITE`
  (`cfg.site_url()`).
- `scripts/build-discovery.py` — `SITE = cfg.site_url()`.
- `scripts/validate-site-quality.js` — made route/job-page counts data-driven and
  added the location/type hub set to the reserved-slug regex.
- `scripts/validate-http.js` — updated the homepage copy assertion.
- `content/index-allowlist.json` — added `/jobs/nigeria/`, `/jobs/lagos/`.
- `content/opportunities.json` — **Afrolicious** record: new
  `editorExperience` (submitted → accepted → scheduled; payment not confirmed).
- `site.config.json` — new `adsense` block; updated `siteDescription`.
- `assets/bryme-v2.css` — styles for verification badges, chip grids, section
  subheads, location picker, report box, job-card titles/badges, editor journey,
  7-col bottom nav, search field.
- `render.yaml` + `server/render.yaml` — `SITE_URL`, `INDEXING_API_TOKEN`,
  `GOOGLE_INDEXING_CREDENTIALS` env vars.
- `server/server.js` — loaded `indexing-api`; `GET /api/index/status` and
  `POST /api/index/notify` (handled before the read-only method gate).
- `README.md`, `docs/ADS.md`, `docs/INDEXING.md` — documentation of the new
  architecture, verification system, AdSense switch, and Indexing API.
- `make-money/writing/afrolicious/index.html` — updated Editor's Experience
  (and its CSS via `.oc-journey`).

### New generated pages (output)
`jobs/nigeria/`, `jobs/lagos/`, `jobs/abuja/`, `jobs/port-harcourt/`,
`jobs/ibadan/`, `jobs/kaduna/`, `jobs/entry-level/`, `jobs/customer-service/`,
`jobs/sales/`, `jobs/administrative/` — all from the existing jobs feed, so the
counts are real.

---

## 3. Verification (the differentiator)

- Every job record carries a **verification status** that maps to an honest,
  source-backed state (never invented).
- Job detail pages clearly separate: **original source**, **BRYME verification**,
  **BRYME's own editorial notes**, and (for writing) **first-hand experience**.
- For externally sourced jobs, the page shows `SOURCE: <platform>` and an
  `Apply on <platform>` button to the exact official page. BRYME is never named
  as the employer and does not collect applications.
- Writing detail pages render a **journey** (pitch → response → accepted →
  scheduled → published → paid) without claiming payment until it happens.

---

## 4. Jobs workflow (how a verified job gets on the site)

1. A BRYME editor opens the **exact** employer/ATS page and records the role's
   fields into `content/jobs.json` (`sourceUrl`, `sourceBoardUrl`,
   `sourceSystem`, `eligibleCountries`, `locationTextRaw`, `workMode`,
   `employmentType`, `compensationRaw` (only when confirmed), `notes`,
   `category`, `remoteEligible`, `status`, `verifiedAt`).
2. Set an honest `status` (`open_when_checked` default).
3. If a role is **genuinely open and the rich fields are complete**, set
   `jobPosting.eligible: true` plus `datePosted`/`validThrough`/`description` to
   emit valid `JobPosting` markup. **Do not** set it for historical or closed
   records.
4. `npm run build` regenerates the job card, category/location/type hubs, the
   detail page, the verification badge, related jobs, and sitemap/robots from
   the allowlist.
5. Add the new detail route to `content/index-allowlist.json` **only if** it
   should be indexable and is genuinely current.
6. `npm test` (quality + HTTP gates) must pass before deployment.

## 5. Indexing API workflow

- Intended for **qualifying JobPosting pages only** (not articles/hubs/guides).
- Authorise a Google service account for the Indexing API; point
  `GOOGLE_INDEXING_CREDENTIALS` at it; set `INDEXING_API_TOKEN` and `SITE_URL`.
- `POST /api/index/notify {"url":"/jobs/<id>/","type":"published|updated|deleted"}`
  (bearer `INDEXING_API_TOKEN`). The module validates the route (job pages
  only), de-duplicates within a window, calls Google, and logs
  `server/indexing-log.jsonl` with timestamp, URL, type and response status.
- Without credentials it runs in **dry-run** (logs and returns a clear message;
  nothing is sent). A notification **does not guarantee indexing** — Google
  decides.

---

## 6. JobPosting structured data (Google policy considerations)

- Emitted **only** when `jobPosting.eligible` is true on a job record and the
  source fields are complete.
- `hiringOrganization` is always the **employer**, never BRYME; `directApply`
  and `url` point at the official source — so BRYME does not impersonate the
  employer/recruiter (compliant with Google's structured-data policy).
- Closed/expired jobs are not marked as available, and the validator currently
  rejects any page that publishes `JobPosting` before source fields are ready.
  **Today no records are flagged eligible**, so the markup is demonstrated in
  `scripts/build-focus-site.py::job_posting_schema()` but not emitted. This is
  the intended starting state — do not mass-publish it on historical records.

## 7. Afrolicious case study

`content/opportunities.json` and
`make-money/writing/afrolicious/index.html` were updated: the creator
**submitted** a pitch, **received a response**, and it was **accepted** and
**scheduled for publication**. The page now shows an honest Editor's Experience
journey and explicitly states **"Payment is NOT confirmed"** until publication
and actual payment occur. Official information stays separate from BRYME's
personal experience.

---

## 8. What remains (follow-up, out of scope for the foundation)

- **Populate the first real verified jobs** now that verified and empty-page
  policies are in place (content quality first, thin pages avoided).
- **Enable `JobPosting`** on genuine, currently-open roles once their fields are
  verified complete.
- **Attach Google Indexing API credentials + service account** (currently
  dry-run) and a scheduled/CI caller for publish/updated/deleted.
- **Enable AdSense** after the domain, privacy/consent, and placement review are
  done (set `site.config.json` → `adsense.caId`).
- **Custom domain migration**: set `SITE_URL` to the new host in Render, add the
  domain/search-console verification, then remove the Render host. Keep the
  Render deployment live during the transition.
- **Browser release gate** (`npm run validate:browser`) requires
  `npm ci` + `npx playwright install chromium` (not installed in this sandbox).
- Future: expand filters (salary, experience, date posted, verification status,
  application status); country-specific earning guides; a BRYME-tested stage
  tracker.

## 9. Risks & Google policy notes

- **Guard against hidden re-introduction of sports/betting content** into the
  work platform — the validator still rejects media families and any ad/tracker
  endpoints.
- **Indexing API and JobPosting must never be treated as ranking or indexing
  guarantees.** Use them only for genuinely qualifying pages.
- **AdSense**: do not place ads over job cards or application flow; require
  consent/CMP for personalized ads and keep placements clearly labelled.
- **Custom domain**: verify the canonical host in Search Console and update
  `SITE_URL` before pointing the domain, to avoid mixed canonical URLs between
  the Render subdomain and the new host.
- **Verification claims** must stay source-backed; the empty hub pages are
  `noindex` precisely so BRYME does not index pages with no substance.

---

## 10. Current status

- `npm run build` → deterministic, idempotent (rebuild produces no new changes).
- `npm run validate` (site quality + HTTP) → pass.
- Sitemap: 60 indexable routes · news: 0 · RSS: 25 items · jobs dataset: 13.
- New location/type hubs present; `/jobs/nigeria/` and `/jobs/lagos/` indexed,
  all empty hubs `noindex`.

---

## Phase 2 (follow-up) — added after the foundation

### Job intake / verification pipeline
- `scripts/import-jobs.py` — stages genuinely **verified** jobs from
  `content/jobs-inbox.json` into `content/jobs.json`. Validates required fields,
  rejects duplicates, refuses to mark `jobPosting.eligible` without a complete
  description/date/source, and prints the routes to allowlist. Supports
  `--dry-run`. **No scraping and no invented verification** — you confirm the
  exact employer/ATS source first. See `docs/ADDING-JOBS.md`.

### Google Indexing API — configuration + CI caller
- `scripts/build-index-queue.py` — generates `content/index-queue.json` (with a
  state file for diffing) containing only `jobPosting.eligible` pages, emitting
  `published`/`updated`/`deleted` as records change and never queueing non-job
  routes. Wired into `npm run build`.
- `scripts/index-notify.js` + `.github/workflows/indexing.yml` — posts the queue
  to the guarded `POST /api/index/notify` endpoint (bearer token), reports
  sent/deduplicated/dry-run/error, and never fails the pipeline (it is an
  optional crawler notification, never a release gate).
- Requires `GOOGLE_INDEXING_CREDENTIALS` (service account) on the service to
  actually reach Google; dry-run until then. See `docs/INDEXING.md`.

### Custom-domain migration (ready in one command)
- `scripts/check-canonical-domain.py` (`npm run check:domain`) — verifies no
  generated page references the old Render host and that every canonical,
  sitemap `<loc>` and robots `Sitemap:` uses `SITE_URL`. Fails in migration
  mode (when `SITE_URL` is a non-Render origin) if any Render reference remains.
- `scripts/apply-audit-remediation.py` now rewrites every baked-in old-host
  reference (`og:image`, content links, breadcrumbs, JSON-LD) to `SITE_URL`'s
  host, so a migration is just setting one env var and rebuilding. Proven:
  `SITE_URL=https://jobs.bryme.com npm run build && npm run check:domain` → OK.
- `docs/DOMAIN-MIGRATION.md` — step-by-step DNS/Render/Search-Console guide and
  the AdSense-on-owned-TLD note.
- New `SITE_URL`, `INDEXING_API_TOKEN`, `GOOGLE_INDEXING_CREDENTIALS` env vars in
  `render.yaml` / `server/render.yaml`; `package.json` gains `index:notify`,
  `check:domain`.

### AdSense (on hold as requested)
Advertising is **not** enabled; `adsense` stays off in `site.config.json`.
Purchasing a domain is the prerequisite (see below).
