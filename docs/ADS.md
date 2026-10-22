# Advertising status — Adsterra active, Monetag removed (owner decision 2026-10-22)

- **Adsterra is the active primary ad network.**
- **Monetag has been removed entirely** (`monetag` removed from `site.config.json`, `/assets/monetag-loader.js` deleted, and all Monetag zone markers and verification meta tags stripped).
- **AdSense stays verification-only** (`ca-pub-1881426210393009` verification snippet and `ads.txt` remain live; `adsense.nativeSlotId` is empty so no AdSense ad units render).

## Approved Adsterra formats

| Format | Placement | Config key |
|---|---|---|
| Native Banner | top of content pages (inside `<main>`) — LIVE | `adsterra.placements.top` |
| Native Banner | middle of the article body | `adsterra.placements.middle` |
| Native Banner | bottom of content pages (after `</main>`) | `adsterra.placements.bottom` |
| Social Bar | floating widget, before `</body>` — LIVE | `adsterra.socialBar.script` |
| Classic display banner (300×250) | after `</main>` — LIVE | `adsterra.displayBanner.key`/`host` |

## Consent gating

`/assets/adsterra-loader.js` loads every Adsterra unit immediately outside the EEA/UK/CH and only after granted ad consent inside them (`Europe/*` timezones). `scripts/test-ad-consent.js` verifies this in headless Chromium and confirms that zero Monetag scripts or zone markers exist on any page.
