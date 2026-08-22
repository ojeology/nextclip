# Case study: why “Shōgun watch” was weak

**Date:** 2026-08-22  
**Canonical URL (do not change):** `https://bryme.onrender.com/series/shogun/`  
**This phase does not add catalogue pages.**

## What BRYME already ranked for

The brief’s example still holds as the working hypothesis until Search Console is exported:

| Query | Brief baseline | What the page actually offered |
|---|---|---|
| Shōgun 2024 | strong / #1 (reported) | Title, year, FX synopsis, official trailer |
| Shōgun watch | weak / ~page 13 (reported) | A “Where to watch” heading that did **not** say where to watch Shōgun |

Do not treat those positions as live GSC numbers. Fill `reports/seo-keyword-baseline.csv` from Search Console / Bing Webmaster for the real baseline.

## What competing “watch” pages do

Pages that rank for “how to watch Shōgun” / “Shōgun streaming” (Collider, Men’s Health, Rolling Stone, JustWatch, ComicBook) all do the same useful thing:

1. State that it is an **FX original**.
2. Name the **Disney-owned family** (Hulu in the US, Disney+ in many other territories).
3. Say how many episodes / that Season 1 is complete.
4. Link to the licensed service — or at least name it clearly.

They are not better designed than BRYME. They simply **answer the query**.

## What BRYME’s page did wrong

The Shōgun page already had:

- A unique URL (`/series/shogun/` — keep it)
- An intent-aware `<title>` mentioning “Where to Watch”
- Official FX Networks trailer
- Billed cast
- Related historical series

The watch block then listed **Netflix, Prime Video, Disney+, Crunchyroll, Apple TV+** with a footnote that opening those links is *not* a claim the title is there.

That fails the query:

- It does not say Shōgun is an FX original (even though the synopsis already does).
- It points at Crunchyroll and Netflix, which are not the originating home.
- A searcher who wants “where to watch” gets a disclaimer instead of a method.
- The hero CTA said **Watch Now**, which implies BRYME hosts the series.

This is also structured-data-adjacent spam risk: a visible “Watch Now” that jumps to generic storefront chips.

## What we changed (without fabricating availability)

We did **not** write “Stream Shōgun on Hulu now.” Rights move.

We did:

1. Say BRYME does not host the series.
2. State the originating network (**FX**) from BRYME’s own catalogue line and the official trailer channel.
3. Explain *how* to find a legal copy: search the licensed apps in your country (often the FX / Hulu / Disney+ family) and confirm on the service’s own title page.
4. Offer one **Check FX** button to the official network site — labelled Check, not Watch on.
5. Remove the generic five-service chip row from this page (and the rest of the 29-page pilot).
6. Rename the hero CTA from “Watch Now” to “Where to watch”.
7. Rewrite the meta description so it is not cut off at “beco…”.

## Duplicate URL (protected, not deleted)

`/movie/shogun/` existed as a full second page, was **in the sitemap**, and already canonicalised to `/series/shogun/`.

The build was supposed to keep `/movie/shogun/` as a **noindex redirect stub**. A later layout pass rebuilt it as a real title page.

This phase:

- Restores `/movie/shogun/` (and 155 other type-mismatch copies) as noindex + refresh stubs
- Removes those URLs from `sitemap.xml`
- Leaves the path in place so any already-indexed `/movie/` URL consolidates to the canonical type URL

That is URL preservation, not a migration.

## What to measure next

Same query set, after deploy, from Search Console and Bing Webmaster — not from one incognito search:

- Shōgun 2024
- Shōgun
- Shōgun trailer
- Shōgun cast
- Shōgun watch
- where to watch Shōgun
- Shōgun 2024 watch

Protect the “Shōgun 2024” ranking. Judge the watch queries over weeks, not a day.
