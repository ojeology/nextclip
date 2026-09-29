# BRYME Pinterest kit — how to post

Six boards, 30 pins each (180 total). Images are vertical 1000x1500 (2:3) JPEGs
in the house style. `manifest.csv` has, per pin: board, title, description
(keyword-rich, extractive from the page), destination URL, image path.

## Posting (owner account = roadmap decision D3)
1. Create the Pinterest account (or a business account under an existing one).
2. Create 6 boards using the exact board names in `manifest.csv`.
3. Pin in manifest order (strongest pages first per board). Native pin flow:
   choose the image, paste the title + description + destination URL.
4. Suggested cadence: 2-3 pins/day per account keeps distribution natural;
   the full kit lands in ~4-6 weeks.

Notes: descriptions already contain the destination URL in text form (safe if
the scheduler strips links); each pin's clickable link is the destination_url.
Vertical 2:3 is Pinterest's recommended format — the site's horizontal OG
cards (`assets/og/`) are fallbacks only if you prefer pixel-exact site imagery.
