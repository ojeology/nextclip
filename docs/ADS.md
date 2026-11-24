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
| Social Bar | floating widget, before `</body>` — LIVE, kept on by owner decision | `adsterra.socialBar.enabled` |
| Classic display banner (300×250) | inside the body at 55% of `<main>`, and after `</main>` — LIVE ×2 | `adsterra.displayBanner.key`/`host` + `inBody` |

## The Social Bar, and the taps (2026-11-23)

The Social Bar's script mounts its own fixed layer on top of the page and keeps
the layer's geometry to itself. On the Articles section readers reported that the
navigation stopped accepting taps once ads had loaded, and that a reload fixed it
until the widget mounted again. That is the Social Bar's signature: a floating
layer over the masthead, invisible in a static DOM snapshot, gone after a reload.

The widget chooses its own geometry and its own stacking, so it is the one unit
we cannot place. Two things changed in response, and one did not:

- the masthead, the drawer and the mobile bar moved into the `2147400000`
  z-index band (see below), so a widget layer at the usual ad-network values —
  999, 9999, 2147483000 — now stacks **below** the navigation instead of over it;
- the page records *where* its ad goes, so no unit sits above a headline any
  more.

**Owner decision: the unit stays on.** Revenue from it is worth keeping while the
navigation still wins the stacking fight. It is the one switch to reach for if
taps stop responding again: set `adsterra.socialBar.enabled` to `false` in
`site.config.json`, rebuild, done — no code change, and nothing else about the
unit is removed. A widget that sets an inline `z-index: 2147483647` would still
beat the chrome band, which is exactly the case that switch exists for.

The other two units are in flow and cannot intercept a tap:

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

## Ads in more than one place (2026-11-24)

Owner: *"Ads should be placed on multiple places of body not just one."*

A long page now carries up to four ad surfaces, in this order down the page:

1. **top** — the native banner just inside `<main>`, under the headline. Unchanged.
2. **in-body display** — the same 300×250 unit, repeated at 55% of `<main>`, at a
   real block boundary, never within 2,500 characters of the top band, and never
   on a page with fewer than six paragraphs. Switch: `displayBanner.inBody`.
3. **bottom display** — the 300×250 under `</main>`. Unchanged.
4. **Social Bar** — the floating widget, unchanged.

### Why the display unit may repeat and a native unit may not

A native banner binds invoke.js to `#container-<key>`. Two copies of one key put
two elements with the same id on the page and the network's install check can no
longer tell which container it is verifying, so natives stay one-per-key
(`adsterra.placements.middle` / `.bottom` still want units of their own).

A display banner is not bound that way. `/assets/adsterra-loader.js` renders each
display slot inside **its own iframe** with its own `atOptions`, so two slots are
two independent documents. The loader used to dedupe loads by script URL; it now
skips that dedupe for `data-ad-kind="display"` only, and keeps it for native and
social, which act on page-level state.

If a second, third or fourth *native* placement is wanted, create one Native
Banner unit per placement in the Adsterra dashboard and paste each key/host into
`adsterra.placements.middle` / `.bottom`; the slots are already wired, spaced and
gated, and the build does the rest.
