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

---

# v4 · NetMirror EXACT reference match (2026-08-21)

Matched 1:1 against the supplied NetMirror clone markup/CSS.

## Exact tokens adopted
- bg `#0B0B0B` · surface `#161616` · elevated `#1C1C1C` · search `#2A2A2A` · border `#333333`
- red `#E50914` · **orange `#FF6B00`** (active pill + section bars) · green `#46D369` · yellow `#F5C518`
- pill border `#444444`, secondary button `#333333`, radii 6/10/12/16/9999, system font stack

## What changed vs v3
1. **Header**: logo is now a split wordmark — `BRY` red + `ME` white (BRYME kept; same
   red/white treatment as NetMirror's Net/Mirror). Search pill `#2A2A2A`, full radius.
2. **Pills** — exact 9-pill row: 🔥 Trending (active: orange `#FF6B00` border +
   `rgba(255,107,0,.12)`), ✨ Latest Release → `/year/2026/`, Netflix → `/channels/netflix/`,
   Prime Video → `/channels/prime-video/`, JioHotstar / SonyLIV / MX Player →
   `/genre/indian/`, Crunchyroll → `/channels/crunchyroll/`, Kids → `/channels/kids/`.
   Inactive pills: transparent bg + `1.5px #444` border. Each pill has a brand icon chip.
3. **Hero**: to-top gradient overlay, red TRENDING NOW label (2px letterspacing),
   32px/800 title, yellow star chip + HD chip + year · genre meta, 3-line synopsis,
   **Watch Now** (white) + **More Info** (`#333333`) equal-width buttons, white-pill
   dots, `U/A` age badge bottom-right. Arrows hidden (reference has none; the hero
   JS keeps working — tests still pass).
4. **Cards**: 140px rails, posters radius 12px, hover `scale(1.03)`, SERIES tag
   top-left + ★ rating top-right as `rgba(0,0,0,.7)` blur chips.
5. **Top 10**: numbers 80px / `2px` white stroke, poster pushed right by 20px —
   exact reference composition.
6. **Section headers**: 4×22px `#FF6B00` bar + 18px white bold title (all rows).
7. **Detail pages**: floating `‹ Back` / `✕` bar over the hero; green `% Match`
   badge + HD chip; equal-width Watch Now (white) / Trailer (`#333`) buttons;
   Cast initials avatars (72px circles, `#161616` fill, `#333` ring); Audio tabs
   with red underline; More Like This with orange bar.
8. **Homepage**: NetMirror "Search Now" CTA card (elevated `#1C1C1C`, red button →
   `/search/`).
9. **Mobile bottom nav**: NetMirror gradient fade + `#808080` labels, active white.
10. Theme-color meta + manifest + PWA theme → `#0B0B0B`.

## Verified
- Full test suite identical to pristine `3e7a4e8` (no new failures).
- Builders `scripts/nm-exact.js`, `scripts/nm-transform.js`, `scripts/build-channels.js`
  all emit the exact pill row for future rebuilds.
