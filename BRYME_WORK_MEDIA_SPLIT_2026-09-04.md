# BRYME work/media split

**Date:** 4 September 2026

## Decision

BRYME is now a focused work publication with four editorial pillars:

1. Jobs
2. Writing
3. Opportunities
4. Guides

Sports and entertainment are no longer repository families on the main publication.

## Media extraction

The complete sports and entertainment working set was copied to:

- Repository: `https://github.com/ojeology/bryme-media`
- Initial extraction commit: `4aaa21dc8c43ff31a936635447ce60c2d650a9a7`
- HTML files: 3,260
- Included families: sports, movies, series, anime, entertainment articles, genres, years, title/trailer data, sports data, assets and historical build scripts

Every media page is deliberately `noindex,follow` until the media project has a final hostname and passes a separate rights, freshness, accuracy and indexability review.

## Main publication

The rebuilt main repository contains:

- five populated job categories;
- 13 individual source-check records;
- a writing hub combining current language-work records with 55 paid-publication research records;
- an opportunities hub;
- a practical guides hub;
- 17 maintained technology guides;
- seven maintained work/income guides; and
- rebuilt author, trust, legal, 404 and 410 pages.

The 55 paid-publication detail records remain accessible but `noindex` until each official guideline receives a fresh human check. `JobPosting` markup is intentionally withheld until full visible descriptions and reliable posting-date fields are maintained.

## Visual and navigation policy

All retained public HTML uses the same forest-green BRYME system. Desktop navigation is:

`Jobs · Writing · Opportunities · Guides · About`

Mobile pages provide a fixed six-item bottom navigation:

`Home · Jobs · Writing · Earn · Guides · About`

## HTTP migration behavior

- Consolidated work hubs use HTTP 301 redirects.
- Removed media families use HTTP 410 until BRYME Media receives a stable public hostname.
- At that point, media URLs with a direct equivalent should be replaced with cross-domain HTTP 301 redirects rather than left as 410.

## Current release-gate target

- 58 Search-eligible routes
- 55 contained writing-detail routes
- zero media families on main
- zero active advertising or analytics endpoints
- empty News sitemap
- deterministic build and HTTP validation
