# Pinterest account + domain-claim checklist (owner action)

The Pinterest kit is prepared; **account creation and claim authorization must be
performed by the site owner**. Do not send passwords or recovery codes. When
Pinterest generates its one-time verification value, share only that value (or
paste the exact meta tag) so it can be added at the generator level.

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
4. Send the exact tag to the implementation owner. The tag will be inserted
   into the root-page `<head>` by the source generator, not by editing generated
   HTML; then rebuild, verify the public root page serves the tag, and let the
   owner click **Verify** in Pinterest.
5. After Pinterest confirms the claim, retain the tag unless Pinterest says it
   can be removed without affecting the claim. Record the confirmation date.

Pinterest also offers an HTML file or a DNS TXT record. Prefer the HTML tag for
this static-site pipeline; if Pinterest does not offer it for the account, the
owner can choose the file or DNS route instead. DNS changes belong to the domain
owner and may take up to 72 hours to propagate.

Official instructions: [Pinterest Help — Claim your website](https://help.pinterest.com/en/business/article/claim-your-website).

## After verification

- Start with the five prepared boards and the seeded URLs in
  `docs/TRACK-B2-B6-PREP.md`; the existing pin kit contains 180 designs.
- Use the house pin spec there: 1000 × 1500 (2:3), text ≤20% of the canvas,
  and alt text drawn from the destination page’s actual meta description.
- Begin at 3–5 fresh pins per week. Review outbound clicks weekly; do not use
  fabricated claims, clickbait, affiliate-style overlays or unverified dates.
- This is organic publishing only. Do not install the Pinterest advertising
  conversion tag or enable paid campaigns without a separate owner decision.
