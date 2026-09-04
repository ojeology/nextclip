# BRYME remediation completion record

**Date:** 4 September 2026 (Africa/Lagos)
**Repository baseline:** `f033af2dd4`
**Scope:** repository-controlled remediation following the full-site audit

## Outcome

The repository-controlled Search, trust, content-integrity, privacy, routing, performance and deployment defects identified in `BRYME_FULL_SITE_AUDIT_2026-09-04.md` have been remediated. Production activation and account-level work remain owner actions.

BRYME is now intentionally a small, source-first publication rather than a Search-indexable interface over thousands of commodity catalogue and sports URLs.

## Completed in the repository

- Established an explicit 64-route Search allowlist in `content/index-allowlist.json`.
- Applied `noindex,follow` containment to 3,228 non-eligible pages, including 1,035 title interfaces and 1,947 paused sports pages.
- Replaced inferred provider collections with explanatory retirement pages; the hardened Node service returns HTTP 410 for them.
- Rebuilt `sitemap.xml` as an exact projection of the allowlist, made the Google News sitemap intentionally empty, and limited RSS to 30 eligible Article pages.
- Added deterministic builders for the focused site, lean editorial CSS, discovery files and repeatable remediation.
- Rebuilt the main navigation and 14 primary pages around verified jobs, practical technology, original editorial and visible trust policies.
- Published 13 manually checked, Nigeria-relevant vacancies linked to exact employer or ATS pages, with timestamps, location caveats and a public verification method. No unauthorized `JobPosting` schema is used.
- Removed unsupported ratings, provider claims, “my list” controls and title entity schema from contained trailer pages.
- Made trailers explicit-click only and reduced the legacy browser application to a small, contained interaction layer with no advertising, analytics, storage or automatic playback.
- Disabled third-party advertising and analytics across public pages and the Telegram Mini App; updated privacy, terms, disclaimer and generator copy to match.
- Added visible authorship and publication dates that agree with Article structured data.
- Removed duplicate, route-mismatched and unsupported structured data.
- Corrected material runtime and provenance errors, including Oppenheimer, The Black Book, The Invite, Avatar Aang and The Last House.
- Repaired every stored competition row so `gd = gf - ga`; all 132 rows now satisfy the invariant. Sports publishing remains paused from Search pending source-rights and production approval.
- Replaced the mutating scheduled results bot with a read-only GitHub quality gate.
- Added keyboard skip links and stable main landmarks throughout the compiled site.
- Replaced the 263 KB stylesheet and unnecessary client JavaScript on all Search-eligible editorial pages with a roughly 21 KB static stylesheet and zero client JavaScript.
- Hardened `server/server.js` with an explicit public-file boundary, canonical routing, correct 404/410 behavior and security headers.
- Added root and server Render Blueprints for a Node 22 Web Service.
- Guarded the destructive historical generator behind `ALLOW_DESTRUCTIVE_BUILD=1`.

## Release evidence

The release gates report:

- 3,293 non-report HTML files assessed
- 64 allowlisted/indexable pages
- 3,228 `noindex` pages
- 1,035 contained title pages
- 1,947 visibly paused sports pages
- 132 valid standings rows
- 13 job records
- 64 sitemap URLs
- 0 News sitemap URLs
- 30 RSS items
- full filesystem internal-link validation passed
- local HTTP routing, 404/410, public allowlist, security headers, API and HEAD checks passed
- all 64 eligible routes rendered at 390×844 and 1440×1000: 128 browser cases passed with no horizontal overflow, broken local images, console errors or client scripts
- explicit-click trailer behavior passed in Chromium
- remediation rerun reports no changes

Run the same gates with:

```bash
npm run build
npm test
python3 scripts/validate-browser.py
```

## IMDb and Google ranking

IMDb does **not** impose a Google ranking penalty on BRYME. IMDb is a licensing and attribution issue: copying IMDb text, ratings, images or datasets without permission can create copyright, accuracy and trust problems. The ranking blockers found here were the large volume of low-value interfaces, unsupported claims, inaccurate data/schema, misleading controls, weak provenance and inconsistent crawl signals. Those repository-controlled blockers have been contained or corrected.

## Owner-only actions before production approval

1. **Deploy the hardened Node service.** Apply `render.yaml` (or equivalent) so production runs `server/server.js`; a generic static host will not deliver all prepared redirects, 404/410 statuses and headers.
2. **Choose and connect the permanent domain.** Purchase/configure it, enable managed TLS and one canonical host, then replace the current `https://bryme.onrender.com` base consistently before requesting broad recrawling.
3. **Use Google Search Console.** Verify the final domain, submit `/sitemap.xml`, inspect representative pages, review Page Indexing, Manual Actions and Security Issues, and monitor old contained URLs as Google recrawls them.
4. **Confirm content and data rights.** Keep records for images, trailer embeds, feeds and any future sports source. Do not resume automated sports publication until the source licence and editorial verification process are approved.
5. **Recheck dated vacancies.** The 4 September 2026 roundup says “open when checked”; refresh, close or archive every record before promoting it later.
6. **Delay AdSense activation.** Advertising is intentionally off. Apply only after the final domain, production deployment, sustained original publishing, clear traffic quality and policy review are in place. Before serving personalized ads in the EEA, UK or Switzerland, implement a Google-certified CMP and update the privacy disclosures to match deployed behavior.
7. **Keep editorial operations active.** Publish corrections, refresh source dates, avoid bulk-generated catalogue expansion and use the allowlists as release policy—not as a one-time cleanup.

## Decision

The repository is ready to deploy as a focused, non-monetized quality rebuild. It is **not** a claim that Google will index/rank every allowed page or approve AdSense; those are external platform decisions and require the owner actions above.
