# Pinterest: what to pin first

**Start small:** three fresh pins a week for the first four weeks. Do not upload all
180 at once. This tests which desks and topics get saves and outbound clicks while
keeping the account active without flooding any board.

## The six prepared boards

Use the exact board names in `pinterest/manifest.csv`:

1. Paid Writing & Freelance Careers
2. Home & DIY That Actually Works
3. Money Guides in Plain English
4. Tech Buying & Fixes
5. Fitness, No Myths
6. What to Watch Tonight

## Four-week starter sequence

The exact title, description, destination link, alt text and JPEG path for each
post are in `pinterest/launch-schedule-4-weeks.csv`.

| Week | First post | Second post | Third post |
|---|---|---|---|
| 1 | Fitness — How to start going to the gym | Money — How to budget with irregular income | Entertainment — How to build a watchlist |
| 2 | Home — How to flush a water heater | Tech — Which password manager fits you? | Writers — How to invoice a publication |
| 3 | Fitness — How much protein do you actually need? | Money — What is escrow? | Entertainment — Where to start with Studio Ghibli |
| 4 | Home — Why your energy bill is high | Tech — 4K down the length of a room | Writers — How Nigerian writers can access US and UK publishing markets |

Use one posting day per pin (for example, Monday/Wednesday/Friday), but rotate
the days if that better fits the owner’s routine. No board appears more than
once in a week in this starter sequence.

## For each pin

1. Open the matching JPEG at the `image` path in the CSV.
2. Create a standard **image Pin** on the listed board; the art is already
   vertical **1000 × 1500 px (2:3)**.
3. Copy `pin_title` into the title field and `pin_description` into the
   description field. The destination URL is also included in the description
   text, but paste it separately into Pinterest’s link/destination field.
4. If Pinterest exposes an image alt-text field, paste `alt_text` from the CSV.
5. Preview the destination and image, then publish. Do not add unverified
   claims, clickbait overlays or a different URL.

The 12 selected destination pages were checked live (HTTP 200). All 180
manifest rows have a matching local destination page and unique JPEG; all images
are 1000 × 1500 and the deployed `public/pinterest/` mirror matches the source
kit byte-for-byte. The renderer now shortens previews at word boundaries and
adds an ellipsis instead of silently clipping text. Continue from each board’s
remaining manifest rows after reviewing the first six weeks of outbound clicks
and saves.

**Before publishing:** Pinterest’s website-verification tag is already in the
root homepage source and was confirmed live. The owner still needs to finish any
account setup and click **Verify** in Pinterest. See
`docs/PINTEREST-OWNER-ACTION.md`. Never share passwords or recovery codes.

**Review:** once a week, record impressions, saves and outbound clicks by board.
At six weeks, keep boards showing useful engagement and adjust the next batch
from real results; do not judge a board from a single Pin.
