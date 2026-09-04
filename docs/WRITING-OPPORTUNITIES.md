# Paid-writing research catalogue

The public entry point is `/writing/`. Detailed paid-publication research lives at `/make-money/writing/{slug}/` and is generated from `content/opportunities.json`.

## Current publication rule

All 55 detail records are dated research last checked on 19 August 2026. They remain `noindex,follow` until a human reopens the official guideline, confirms the current submission state, pay language, eligibility and URL, updates `lastChecked`, and approves that specific route for Search.

An HTTP 200 response alone is not proof that submissions remain open. Do not turn an old `OPEN`, `ROLLING` or deadline value into a current claim without reading the official page.

## Adding or revalidating a record

1. Start with the publication's own submission or commissioning page.
2. Record only what the source states; use “not publicly stated” when appropriate.
3. Keep pay currency, unit and caveats together.
4. Distinguish a pitch window from a guaranteed commission.
5. Set `lastChecked` to the actual human-check date.
6. Run `npm run build && npm test`.
7. Add a route to the Search allowlist only after it has enough original explanation and a release review.

BRYME must never claim a response, acceptance or payment that did not happen.
