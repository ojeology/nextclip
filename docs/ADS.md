# Advertising status — Adsterra primary (owner decision 2026-10-03)

AdSense rejected the site after the 2026-10-01 cleanup (indexable surface cut
2,735 → 1,894; the re-review verdict came back negative). The house pivots:

- **Adsterra is the primary ad network now.**
- **AdSense stays verification-only** (the `ca-pub` meta and verification
  snippet remain live) as a possible later pivot. Its ad units stay unwired
  until a future owner decision; `adsense.nativeSlotId` is the off-switch.

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

**Still banned:** popunders, forced redirects, notification prompts,
full-screen interstitials. The AdSense-era refusal of the Social Bar is lifted
by the pivot; the ban list above stands.

## Consent gating (unchanged)

`/assets/adsterra-loader.js` loads every Adsterra unit — each native slot,
the Social Bar and the classic display banner — immediately outside the
EEA/UK/CH and only after granted ad consent inside them (timezone-based
regioning; details in the loader header). Google Consent Mode defaults gate
Google's own tags; the loader extends the same consent standard to every
Adsterra format on the site; `scripts/test-ad-consent.js` proves all three
behaviours in a real browser on every test run. `adsterra.gateConsent: false`
restores ungated inline tags for the NATIVE slots only — the social bar and
the display banner stay loader-driven either way (CSP and consent both demand
it). Do not flip the flag casually.

## House rules (unchanged, enforced by validators)

- No placement may resemble a job card, employer link, application button or
  navigation control.
- Ads render on indexable content pages only — never on noindex stubs or
  soft-redirect pages (the injector skips them by robots-meta guard).
- Every ad block is labelled "Advertisement".
- The Money desk keeps its educational-not-advice standard; no ad may imply
  earnings, signals or a broker relationship.

## How to change placements

1. Edit `site.config.json` (`adsterra.placements.*`, `socialBar`, `displayBanner`).
2. Rebuild (`npm run build` — `scripts/inject-ads.py` runs in the pipeline).
3. Run `npm test`; the quality gate and money gates must stay green.
4. Deploy; verify each unit via Adsterra's "View page source" check.

To kill every unit: set `adsterra.enabled: false`, rebuild, deploy.
