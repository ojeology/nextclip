# Advertising status — Adsterra active, Monetag removed (owner decision 2026-10-22)

- **Adsterra is the active primary ad network.**
- **Monetag has been removed entirely** (`monetag` removed from `site.config.json`, `/assets/monetag-loader.js` deleted, and all Monetag zone markers and verification meta tags stripped).
- **AdSense stays verification-only** (`ca-pub-1881426210393009` verification snippet and `ads.txt` remain live; `adsense.nativeSlotId` is empty so no AdSense ad units render).

## Approved Adsterra formats

| Format | Placement | Config key |
|---|---|---|
| Native Banner | the spot the page names, else the top of `<main>` — LIVE | `adsterra.placements.top` |
| Native Banner | middle of the article body | `adsterra.placements.middle` |
| Native Banner | bottom of content pages (after `</main>`) | `adsterra.placements.bottom` |
| Social Bar | floating widget, before `</body>` — **SUSPENDED 2026-11-23** | `adsterra.socialBar.enabled` |
| Classic display banner (300×250) | after `</main>` — LIVE | `adsterra.displayBanner.key`/`host` |

## Why the Social Bar is off (2026-11-23)

The Social Bar's script mounts its own fixed layer on top of the page and keeps
the layer's geometry to itself. On the Articles section readers reported that the
navigation stopped accepting taps once ads had loaded, and that a reload fixed it
until the widget mounted again. That is the Social Bar's signature: a floating
layer over the masthead, invisible in a static DOM snapshot, gone after a reload.

No CSS can prove the widget sits under our chrome, and third-party creative
z-indexes are outside our control, so the unit is switched off in
`site.config.json` (`adsterra.socialBar.enabled: false`). The script, the marker
and the loader path are untouched: setting it back to `true` and rebuilding
restores it in one pass. Revenue from that one unit is not worth an unclickable
masthead.

The other two units stayed, because neither can intercept a tap:

- the native band renders **inside** `<main>` in normal flow, and its container is
  `isolation: isolate` (`scripts/inject-ads.py`), so a creative that sets a huge
  `z-index` is contained by the band;
- the display banner renders in its own 300×250 iframe, also in flow.

## Placement contract: the page names the spot

Generic top-of-`<main>` placement put the unit **above the breadcrumb and the
headline** on the Articles pages, where the creative's arrival moved the whole
page down after the reader had started aiming at it. So the layout can now own
the position:

- `scripts/build-articles.py` writes `<div class="ba-adslot"><!--ba-ad--></div>`
  where the section wants the first unit — after the lead story on the landing
  page, mid-story in a piece, below the grid on a beat page;
- `scripts/inject-ads.py` appends the configured band **after** that marker and
  skips the top-of-`<main>` rule on any page that has one;
- the marker survives injection, so a rebuild strips and re-inserts the band
  instead of stacking a second one.

Two house rules follow from it. An unfilled band draws nothing at all
(`:has(.adband-slot:empty)` collapses it) rather than an "Advertisement" label
over an empty box, which is what readers with an ad blocker used to see. And no
band may ever be placed above the headline of a page or over the navigation.

## Chrome owns the top of the z-index range

`assets/bryme-v2.css` declares the stacking tokens. The masthead, the drawers,
the mobile bottom bar and the skip link sit at `2147400000`–`2147405000`; in-flow
content and ad bands sit at `0`–`45`. The numbers are large on purpose: a
third-party creative arrives with an inline `z-index` of its own choosing —
commonly `999`, `9999` or `2147483647` — after first paint. At the old 50–200
band the masthead lost that fight silently, and a reader cannot tell a
nav-overlay from a frozen page.
