# Advertising (AdSense) status and readiness

Advertising and third-party analytics are disabled across BRYME during the
quality rebuild. The code is AdSense-ready but ads are **off** until the items
below are satisfied.

## What is in place now

- `site.config.json` → `adsense` block holds `caId`, `enabled`, and a note.
- `scripts/build-focus-site.py` emits the `google-adsense-account` meta tag
  **only** when a real `ca-pub-...` ID is configured. No ad script is loaded
  while `enabled` is false.
- The AdSense tag, when enabled, will never be allowed to resemble a job card,
  employer link, application button or navigation control. The validator also
  refuses to ship any page that references ad/tracking endpoints.

## Release checklist before enabling

1. Confirm the final production domain and an updated privacy policy.
2. Implement region-appropriate consent controls (Google-certified CMP where
   Google requires one) and only then serve personalized ads.
3. Review placements on mobile and desktop for the work publication.
4. Ensure every monetized page provides substantial original value (no thin
   pages). Empty location/type hubs stay `noindex`.
5. No placement may be mistaken for a job card, employer link, application
   button or navigation control.
6. Roll out on a small, explicitly approved route allowlist and pass the
   privacy, accessibility, performance and browser release gates.

Popunders, forced redirects, notification prompts and full-screen interstitials
are not approved for the work platform. Job and opportunity pages must never
imply that an advertiser is an employer or that clicking an ad is part of an
application.

## How to enable

1. Set `site.config.json` `adsense.caId` to the verified `ca-pub-...` value.
2. Rebuild. The meta tag appears and the account can be verified in Search
   Console / AdSense.
3. After review, set `adsense.enabled` to `true` and add the ad code (in a
   clearly-labelled container, never overlaid on application flow).
4. Deploy and re-run the release gates.
