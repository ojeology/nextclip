# Track B2 (Pinterest) + B6 (Forums) — prep pack

Prepared 2026-09-27 under delegated authority ("do whatever best"). Pinterest
publishing remains an owner action: finish any business-account setup and click
Pinterest **Verify**. The owner-supplied verification value is configured in the
source generator and is live on the root homepage (HTTP 200 and tag checked on
2026-09-29). The B6 forums routine can begin without a Pinterest account; the
30-pin kit is generated and committed. Nothing here invents claims — every
landing page is a live, indexed route.

## B2 — Pinterest (prep-mode)

**Why these pages:** Pinterest is an evergreen-save + plan engine, and writers
plan careers on it — saves and outbound clicks are the two numbers that matter,
and both are measurable per pin.

Pin spec: 1000×1500 (2:3, Pinterest’s recommended aspect ratio); keep essential
copy within the frame and use page-derived alt text if Pinterest presents that
field. Pinterest’s [image specs](https://help.pinterest.com/en/business/article/pinterest-product-specs)
warn that taller-than-2:3 images may be cropped in feeds. The kit covers one
board — the publication BRYME actually runs. See `pinterest/HOWTO.md` and
`pinterest/launch-schedule-4-weeks.csv`. Use the board name in
`pinterest/manifest.csv` exactly. No affiliate-style overlays or clickbait
text — house honesty rules apply:

| Board | Seed pins (live routes) |
|---|---|
| Paid Writing & Freelance Careers | `/writers/writing/` · `/writers/writing-opportunities/` · `/writers/state-of-paid-writing-2026/` · `/writers/writing-calendar/` |

Cadence: 3 fresh pins/week for the first four weeks (the 12-pin schedule in
`pinterest/launch-schedule-4-weeks.csv`), then judge by outbound clicks per pin.

**Owner action needed:** complete any remaining Pinterest business-account
setup and finish the claim for `https://thebryme.com/` by clicking **Verify**.
The supplied verification value is wired through the source generator and is
already live on the homepage. See `docs/PINTEREST-OWNER-ACTION.md` for the steps;
do not send account passwords or recovery codes.

## B6 — Forums / communities (answer-first, never link-dropping)

Policy: participate as a person, disclose affiliation only if a community asks,
link only when a page genuinely answers the thread. No posting the same link in
multiple communities in one week. Newsletter CTA already exists site-wide
(/newsletter/ digest) — forums feed it by reputation, not by promotion.

Priority communities by desk (verify each community's self-promo rules before
first post; rules change):

| Desk | Communities | What we'd answer with |
|---|---|---|
| Writers | r/freelanceWriters, r/DestructiveReaders, Absolute Write, Contently community threads | State-of-Paid-Writing figures (computed from our own 142-record DB), deadline calendar, rate-verification method |
| Fitness | r/Hyrox, r/Fitness (wiki-friendly threads only), r/BeginnerFitness | Hyrox pace-planner maths, zone-2 explainers — general info, never medical advice, red flags → professional |
| Home | r/HomeImprovement, r/homeowners (rules: many ban links — answer in-text, link only on explicit ask) | Seasonal checklist logic, safe-scope framing ("call a pro for X") |
| Money | r/personalfinance (strict no-links — text answers only), r/UKPersonalFinance | APR-vs-APY arithmetic, jurisdiction-sourced corrections |
| Tech | r/buildapc, r/laptops (spec-floor threads) | Spec-floor reasoning, battery-health method |

Weekly budget: 2 hours, 3–5 substantive answers, 0–1 link. Track: referral
sessions per source in GA4; drop communities with zero 4-week referrals.

**Owner action:** participation itself belongs to a real human. Use the answer-first policy in `docs/FORUMS-ROUTINE.md`; do not create or automate desk personas. Follow each community's current rules and disclose affiliation if asked.

## What remains owner-side

- Pinterest account/domain claim, live **Verify** click and manual pin publishing;
  the 180 designs and manifest are already committed.
- No forum account creation was attempted — platform terms and house E-E-A-T
  both say these are the owner's identities to hold. Actual forum participation
  remains a real-human task, never an automated persona.
