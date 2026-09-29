# Pinterest account + domain-claim checklist (owner action)

The Pinterest kit is prepared. **Account control, website claim and the final
Verify click remain owner actions.** The owner-supplied verification value is
now configured at `site.config.json` → `pinterest.domainVerification`; the root
hub generator emits it on the homepage only. Do not send passwords or recovery
codes.

## Create or convert the account

1. Create a Pinterest Business account using the BRYME business email, or
   convert an existing account if that is the owner’s preference.
2. Set the profile website to `https://thebryme.com/` and use BRYME branding.
3. Keep the account credentials and two-factor recovery with the owner. No
   third-party scheduler or ad account is needed for the prepared organic pins.

## Claim the website

1. In Pinterest, open **Settings → Link to Pinterest → Claim** beside
   **Websites**.
2. Enter `https://thebryme.com/` (the apex canonical domain; `www` redirects).
3. Choose **Add HTML tag** and copy the personalized verification tag.
4. The tag is now emitted on the root homepage by the source generator, and the
   committed `ecosystem/hub/index.html` is carried into `/` and `public/` by the
   routing/build steps. After rebuilding and deploying, inspect `https://thebryme.com/`
   to confirm the tag is in `<head>`, then click **Verify** in Pinterest.
5. After Pinterest confirms the claim, retain the tag unless Pinterest says it
   can be removed without affecting the claim. Record the confirmation date.

Pinterest also offers an HTML file or a DNS TXT record. Prefer the HTML tag for
this static-site pipeline; if Pinterest does not offer it for the account, the
owner can choose the file or DNS route instead. DNS changes belong to the domain
owner and may take up to 72 hours to propagate.

Official instructions: [Pinterest Help — Claim your website](https://help.pinterest.com/en/business/article/claim-your-website).

## After verification

- Start with the prepared boards and seeded URLs in
  `docs/TRACK-B2-B6-PREP.md`; the committed Pinterest kit contains 180 designs.
- Use the house pin spec there: 1000 × 1500 (2:3), text ≤20% of the canvas,
  and alt text drawn from the destination page’s actual meta description.
- Begin at 3–5 fresh pins per week. Review outbound clicks weekly; do not use
  fabricated claims, clickbait, affiliate-style overlays or unverified dates.
- This is organic publishing only. Do not install the Pinterest advertising
  conversion tag or enable paid campaigns without a separate owner decision.
