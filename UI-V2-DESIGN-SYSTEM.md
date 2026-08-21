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

---

# v3 · NetMirror-style polish (2026-08-21)

Applied on top of v2 per the NetMirror app blueprint. BRYME branding kept;
visual design matches the NetMirror screens (home + details).

## What changed

1. **Channel pills** (every page's desk-bar): catalogue pills replaced with
   `🔥 Trending` (active, red border + flame) · Netflix · Prime Video ·
   Crunchyroll · Kids — each with a small brand-logo tile. Pills link to new
   `/channels/{netflix,prime-video,crunchyroll,kids}/` landing pages
   (movies / series / anime / kids&family catalogues, 493/81/74/44 tiles).
2. **Mobile bottom nav**: added Movies / Series / Anime links so the
   catalogue stays reachable on mobile now that the pills are channels.
3. **Home hero (NetMirror)**: `🔥 TRENDING NOW` tag, HD chip, yellow star
   rating chip, 2-line synopsis clamp, `▶ Watch Now` (white) + `More Info`
   (translucent) buttons, `U/A` age badge bottom-right (per-slide), white
   pill/grey dot pagination.
4. **Top 10 Today**: trending rail header renamed with red accent bar.
5. **Detail pages (648 title pages)**:
   - `▶ Watch Now` (white) + `▶ Trailer` (translucent) CTAs
   - `XX% Match` (green) + `HD` chips beside the BRYME editorial badge
   - **Cast** carousel — circular initials avatars (JSON-LD cast data)
   - **Audio** tabs — data-driven languages, active tab with red underline
   - `More Like This` header (red accent bar) on the related row
6. **Sitemap**: 4 channel URLs added.

## Data honesty notes
- `% Match` only shows where an editorial score exists (127 titles have
  `rating.value` in `data/movies.json`) — no invented scores.
- Cast avatars use initials because no portrait photos are stored.
- Channel pages carry an editorial disclaimer: availability on each service
  varies by region; links point to official destinations.

## Verified
- Full test suite: identical results to the pristine commit `3e7a4e8`
  (15 ranking / 32 editorial / 9 titlepage / 5 sports / 4 frontend / 1 bryme /
  1 trailer pre-existing failures — zero new).
- Builders kept in `scripts/build-channels.js` + `scripts/nm-transform.js`.
