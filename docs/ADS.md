# Advertising status — Adsterra primary, Monetag live (owner decisions 2026-10-03 and 2026-10-06)

AdSense rejected the site after the 2026-10-01 cleanup (indexable surface cut
2,735 → 1,894; the re-review verdict came back negative). The house pivots:

- **Adsterra is the primary ad network now.**
- **AdSense stays verification-only** (the `ca-pub` meta and verification
  snippet remain live) as a possible later pivot. Its ad units stay unwired
  until a future owner decision; `adsense.nativeSlotId` is the off-switch.
- **Monetag is live as a second network (2026-10-06):** In-Page Push and
  Vignette, on every indexable page view. See the Monetag section below.

## Approved Adsterra formats

| Format | Placement | Config key |
|---|---|---|
| Native Banner | top of content pages (inside `<main>`) | `adsterra.placements.top` |
| Native Banner | middle of the article body (after the median paragraph) | `adsterra.placements.middle` |
| Native Banner | bottom of content pages (after `</main>`) — LIVE | `adsterra.placements.bottom` → shared `adsterra.key` |
| Social Bar | floating widget, before `</body>` — LIVE 2026-10-03 | `adsterra.socialBar.script` |
| Classic display banner | after `</main>` — LIVE 2026-10-03 | `adsterra.displayBanner.key`/`host` |

**One Adsterra unit key per placement.** Adsterra identifies an install through
the container + `invoke.js` pairing, so top and middle each need their own
Native Banner unit created in the Adsterra dashboard. Paste each unit's
key/host into `site.config.json` and rebuild — the slots, consent gating and
loader are already wired. The bottom placement runs on the shared live unit.

**Live since 2026-10-03:** the Social Bar unit and the classic 300x250 display
banner (owner units pasted into `adsterra.socialBar.script` and
`adsterra.displayBanner`). Both ride the same consent gate as the native
slots. The classic banner's dashboard snippet pairs an inline `atOptions`
config script with `invoke.js`; the site CSP bans inline scripts, so the
loader sets the `atOptions` object itself on a dedicated iframe and runs
`invoke.js` inside it — nothing inline ever ships, and whatever the network's
script renders stays inside that iframe. The display banner therefore always
loads through `/assets/adsterra-loader.js`, even with `gateConsent: false`.

## Approved Monetag formats (owner decision 2026-10-06)

| Format | What it is | Zone | Script | Config key |
|---|---|---|---|---|
| In-Page Push | notification-styled ad box drawn inside the page; **not** a browser notification, asks for no permission | `11966342` | `https://nap5k.com/tag.min.js` | `monetag.inPagePush` |
| Vignette | overlay ad that can appear at page transitions | `11966367` | `https://n6wxm.com/vignette.min.js` | `monetag.vignette` |

**Every eligible page view, no local cap.** Both scripts are requested on
every indexable, non-stub page load. Vignette runs at page transitions and this
is a multi-page site, so each navigation is a fresh page load — the script has
to be there on every one for Vignette to ever run. There is no frequency cap,
counter or timer in the build or the loader, and the loader uses no cookies or
browser storage. How often an ad actually appears is Monetag's decision. (The
earlier Monetag wiring capped Vignette at 4 loads per 4 hours and Push at 12
per 12 hours in `localStorage`, under zones `11610753` / `11610749`; both caps
and both zones are retired, and the tests fail if either returns.)

**How it ships.** Monetag's dashboard snippet is an inline `<script>`, which the
site CSP (`script-src 'self' https:`, no `unsafe-inline`) blocks, so it cannot
be pasted in. Instead `scripts/inject-ads.py` renders, before `</body>` on each
eligible page, one hidden marker per enabled zone

```html
<div data-adband="monetag" data-ad-kind="monetag" data-ad-unit="vignette"
     data-ad-zone="11966367" data-ad-src="https://n6wxm.com/vignette.min.js" hidden></div>
<script src="/assets/monetag-loader.js" defer></script>
```

and the first-party `/assets/monetag-loader.js` appends the same
`<script data-zone="…" src="…">` that Monetag's snippet would. Zones live **only**
in `site.config.json`; nothing about a zone is hard-coded in the loader, and
"View page source" shows both. Switch it off with `monetag.enabled: false` (or
a unit's own `enabled`), rebuild, deploy. `monetag.enabled` is independent of
`adsterra.enabled`. `monetag.verification` (the homepage `<meta name="monetag">`)
is unrelated to the zones and unchanged.

**What the loader does not control.** It sets no cookies and stores nothing, but
the two Monetag scripts it loads are third-party code: they make their own
requests and may use their own cookies, browser storage and device identifiers.
The privacy pages say so. The creative inside each format is chosen by Monetag's
ad feed, so BRYME cannot label it or vet it per ad, and the "no ad may imply
earnings, signals or a broker relationship" rule below cannot be enforced on it
by any validator — report offending creatives to Monetag with the page URL and a
screenshot.

## What is banned

**Still banned:** popunders (on-click pop ads), forced redirects, and classic
browser push-notification subscriptions (the permission prompt). Nothing here
may ask for notification permission.

**Amended 2026-10-06 (owner decision):** the earlier ban on "full-screen
interstitials" and "notification prompts" is lifted for exactly the two Monetag
formats above and nothing else — Vignette, an overlay shown at page transitions,
and In-Page Push, which is *styled* like a notification but is drawn inside the
page and asks for no permission. The AdSense-era refusal of the Social Bar was
lifted by the Adsterra pivot. Any other overlay, interstitial or push format
needs a new owner decision recorded here before it is wired.

**Public copy reworded (2026-10-06).** The homepage and the Writers home used to
say "0 pop-ups", "no interstitials" and "ads are in a single band, never inside
prose", which stopped being true once the Social Bar, In-Page Push and Vignette
went live. They now say what still holds: **no pop-up windows** (popunders and
forced redirects stay banned), no autoplay, no newsletter gate, no ad inserted
into the text of an article, and that some ads appear as overlays on the page
(`scripts/build-landing.py`, `scripts/build-writing-first.py`,
`scripts/build-writing-hub.py`, `scripts/build-ecosystem.py`). Do not reintroduce
"no pop-ups" or "no interstitials" wording while Vignette is enabled.

## Consent gating (unchanged)

`/assets/adsterra-loader.js` loads every Adsterra unit — each native slot,
the Social Bar and the classic display banner — immediately outside the
EEA/UK/CH and only after granted ad consent inside them (timezone-based
regioning; details in the loader header). `/assets/monetag-loader.js` applies
the **same gate** to both Monetag zones: no request to a Monetag host is made in
the EEA/UK/CH until a granted ad-consent signal arrives, and none ever if consent
is refused. Google Consent Mode defaults gate Google's own tags; the two loaders
extend the same consent standard to every other ad format on the site.

`scripts/test-ad-consent.js` proves it in a real browser on every test run:
Lagos and New York load everything; Berlin (EEA), London (UK) and Zurich (CH)
make zero Adsterra or Monetag requests without consent and after a refusal; a
grant releases everything, whether pushed as a plain array or sent the way
Google's CMP really does, through `gtag('consent','update')`; six page loads in
one browser profile each request both Monetag zones; the Monetag loader touches
no cookie or storage (a hook plus a positive control); stub and 404 pages carry
no Monetag markup. `scripts/validate-site-quality.js` additionally fails the
build if the two loaders' gate code ever differs, if the two tracked loader
copies drift, if the loader gains storage or hard-coded zones, or if any page
carries markup that does not match `site.config.json`.

`adsterra.gateConsent: false` restores ungated inline tags for the Adsterra
NATIVE slots only — the social bar and the display banner stay loader-driven
either way (CSP and consent both demand it). Monetag has no such switch: its
loader is the only route and it is always gated. Do not flip the Adsterra flag
casually.

**Known limit of the gate (unchanged).** The region is decided by IANA timezone
`Europe/*`. That covers the EEA, UK and Switzerland plus some non-EEA countries
(withholding ads there is the safe direction), but it does not cover EEA
territories whose timezone sits outside `Europe/` — for example `Atlantic/Canary`
and `Atlantic/Madeira`, `Atlantic/Azores` (Spain, Portugal) and
`Atlantic/Reykjavik` (Iceland). Those visitors load ads immediately. Fixing it
means changing the gate in both loaders together.

## House rules (unchanged, enforced by validators)

- No placement may resemble a job card, employer link, application button or
  navigation control.
- Ads render on indexable content pages only — never on noindex stubs or
  soft-redirect pages (the injector skips them by robots-meta guard). Known
  quirk (pre-existing): that guard is not anchored to a real `<meta>` tag, so
  one indexable page, `/tech/website-not-indexing-google/` (an article that
  quotes the noindex tag in a code sample), is treated as a stub and carries no
  ads from any network; the Monetag check in `scripts/validate-site-quality.js`
  mirrors the rule and agrees. Anchoring the regex in both places would fix it,
  and would also switch Adsterra on for that page.
- Every banner block we render is labelled "Advertisement". The overlay
  formats (Social Bar, In-Page Push, Vignette) are drawn entirely by the
  networks' own scripts, so any labelling inside them is the network's.
- The Money desk keeps its educational-not-advice standard; no ad may imply
  earnings, signals or a broker relationship.

## How to change placements

1. Edit `site.config.json` (`adsterra.placements.*`, `socialBar`, `displayBanner`,
   `monetag.inPagePush`, `monetag.vignette`).
2. Rebuild (`npm run build` — `scripts/inject-ads.py` runs in the pipeline).
3. Run `npm test`; the quality gate and money gates must stay green.
4. Deploy; verify each unit via "View page source" (Adsterra's own install
   check reads it; Monetag's zone markers are in the page the same way), then run
   the consent test against the live site from the deployed commit:
   `LIVE_URL=https://thebryme.com node scripts/test-ad-consent.js` (same
   assertions as `npm run test:ads`; ad hosts stay intercepted, so it makes no
   real ad request).

To kill every Adsterra unit: set `adsterra.enabled: false`, rebuild, deploy.
To kill both Monetag zones: set `monetag.enabled: false`, rebuild, deploy.

**Deploy note.** Render rebuilds the site from source on every push to `main`
(`npm run build`), so the ad markup is generated at deploy time and the committed
HTML is not what ships; that is also why CI's "Confirm deterministic output" step
(`git diff --exit-code` after the build) fails whenever ad markup changes without
the regenerated HTML being committed. The privacy pages for the house and the
six desks are different: they are committed output of
`scripts/build-ecosystem.py`, which is **not** in the npm build, so they change
only when that generator is run explicitly and its output committed (the Writers
privacy page comes from `content/hub/trust-pages.json` and does rebuild).
