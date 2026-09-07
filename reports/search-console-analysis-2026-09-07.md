# Search Console Analysis — 7 September 2026

**Data:** Keyword + page reports exported 9/7/2026 (window predates most of the 46 roadmap articles published this week). Headline numbers include 1,520 impressions from `site:` operator checks — excluded below as non-organic.

## The honest numbers

| Metric | Value | Read |
|---|---|---|
| Organic keywords | 64 | small, early |
| Organic impressions | 178 | ~46% of raw page impressions are legacy URLs |
| Organic clicks | 16 | **CTR 8.99%** — strong for this traffic mix |
| Brand ("bryme") | pos 1.8, 7 clicks | brand is #1-2, as it should be |

## What's genuinely working (the signal)

1. **Writing-intent queries are clicking.** "does mcsweeney's internet tendency pay for submissions" (pos 5, 1 click), "can i include names in a personal essay on longreads" (pos 3, 1 click), "how to find paid writing opportunities" (**pos 1.0**, 1 click). Exactly the Layer B queries the strategy predicted we'd win first.
2. **New hub content is already surfacing.** `/learn/types-of-writing/how-to-write-a-thank-you-note/` — published days ago — sits **pos 8.0** for "how to write a thank you note" (9 impressions). Page-one bottom; pushable with internal links.
3. **Brand holds.** "bryme" at 1.8 with 7/33 clicks. People are also typing `bryme.onrender.com` as a query (43 impressions) — real humans navigating to the subdomain. Every one of them is a person the domain migration will re-route.

## What's noise (don't celebrate it)

- **Legacy multi-niche URLs** (`/movies/`, `/sports/*`, `/entertainment/`, `/series/`, `/trending/`, `/anime/*`, `/articles/`, `/years/`) — verified **404 live** — still hold ~250 impressions and ~10 clicks from Google's index of the pre-BRYME site. Clicks are landing on dead pages. This decays over weeks; the domain migration resets it entirely. Do not build redirects for retired media content — 404 decay is correct here.
- **`/make-money/writing/mcsweeneys/` and `/make-money/writing/longreads-personal-essay/` return 200 live** although the current build has no `make-money/` directory (canonicals: `/writing/mcsweeneys/`, `/writing/longreads-personal-essay/`). The Render route `/make-money/*` appears not to be rewriting deep legacy paths as intended. Harm or help is unclear (the pages rank and click), but it's serving non-canonical URLs — worth checking Render's redirect behaviour after the domain migration, then adding explicit deep-path routes or letting the domain reset fix it.

## Actions (in order)

1. **Nothing heroic on this data.** The window predates the 46 new articles + six pillar hubs. Re-pull this report in 2–4 weeks; that pull will be the first real reading on the roadmap content.
2. **Internal-link the thank-you-note guide** from 2–3 related pages (it's pos 8; a nudge can take it top-5).
3. **After domain migration:** recheck the `/make-money/*` deep-path behaviour, submit the new sitemap, request indexing on the money pages.
4. **Keep the fortnightly rhythm:** publish → `npm run validate` → push → ping script → re-pull GSC.

*Analysis of exported GSC reports; live URL statuses verified 7 September 2026 via HTTP checks.*
