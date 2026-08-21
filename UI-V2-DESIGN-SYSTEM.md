# BRYME v2 · Streaming UI (Netflix-style design system)

Applied 2026-08-21. Re-skins the whole static site to a modern streaming interface
while keeping every existing class hook, page structure, and the JS behaviour intact.

## Design tokens (dark default)

| Role              | Value   |
|-------------------|---------|
| Background        | `#0D0E12` |
| CTA red           | `#E50914` |
| Container grey    | `#1F222A` |
| Soft white text   | `#FFFFFF` |
| Muted grey text   | `#9E9E9E` |
| Star badge yellow | `#FFC107` |

## What changed

1. **`assets/site.css`** — appended the full v2 override layer (final block,
   labelled `BRYME v2 · STREAMING UI`). To revert, delete that block and the
   legacy file is otherwise untouched.
   - Flat `#0D0E12` canvas (removed the old coloured radial smears)
   - Typography scale: 24px bold hero/page titles · 18px bold row headers ·
     16px semi-bold card titles · 12px medium badges · 14px detail text
   - **Top bar**: sticky dark bar + integrated search pill (`#1A1C23`, 20px radius)
   - **Category pills**: inactive `#1F222A` dark pills, active pill **outlined red**
   - **Hero carousel**: ~300–470px, top gradient overlay, white "Watch Trailer"
     primary button + translucent dark "View Details" secondary, pagination dots
     (active = white pill, inactive = `#555`), red hover controls
   - **Content rows**: 2:3 cards, 8px radius, hover lift; **star rating badge
     (top-right)** and **SERIES/MOVIE/ANIME tag (top-left)** overlay every poster
   - **Top-10 row**: the Trending rail now uses big outlined numerals (text-stroke)
     sitting behind the posters — no markup duplication
   - Panels, chips, filters, footer, mobile nav, search page, and detail pages all
     re-skinned; sports/money/tech verticals keep their identity colours
2. **`index.html`** — integrated search form in the top bar, Trending rail tagged
   `rail-t10`, carousel interval 8s → 5s, theme-color `#0D0E12`.
3. **`assets/site-app.js`** — theme-color meta now writes `#0D0E12`.
4. **All pages** — `theme-color` meta swapped `#08090b` → `#0D0E12` (2,970 files).
5. **`manifest.webmanifest`** — background/theme colour updated.

## Verified

- `tests/homepage-tests.js` passes (hero structure/navigation/trailer behaviour).
- Other suites show identical results to the pre-change baseline — the only
  failures are pre-existing content/data mismatches, none related to styling.
- Home, title, and search pages all serve with the new CSS (`python3 -m http.server`).

## Notes

- Card images are 16:9 YouTube thumbs cropped to 2:3 (`object-fit: cover`);
  where `/assets/cards/*.svg` posters exist they already render 2:3.
- Overlay badges are pure CSS (absolute positioning inside `.tile`), so no page
  markup needed to change — including the ~2,900 generated title pages.
- Light theme is preserved with matching light-surface overrides.
