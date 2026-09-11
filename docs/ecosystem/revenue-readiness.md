# BRYME Revenue Readiness Dashboard
**Policy (owner, 11 Sep 2026):** the domain is purchased only when every niche rates 9–10/10. **Primary target: AdSense revenue.** This dashboard tracks both. Updated per batch.

## AdSense rails (built, awaiting the owner's flip)
| Rail | State |
|---|---|
| `site.config.json → adsense.caId` + `enabled` | **Off.** Paste a real `ca-pub-…` id and set enabled=true after approval |
| `<head>` account meta + auto-ads script | ✅ injected on every page when enabled (batch 19, `shell()`) |
| Responsive slot helper (`_ads_slot`) | ✅ in the build; renders nothing while off |
| `ads.txt` | ✅ auto-emitted (root + ecosystem) when enabled; deleted when off |
| Privacy disclosure | ✅ approval-grade on all five property privacy pages (Google cookies, ad settings opt-out, EEA/UK consent, house separation rules) — dated 11 Sep 2026 |
| Trust pages (about/contact/corrections) | ✅ every property |
| Consent management (EEA/UK) | ⚠️ Google requires a **certified CMP** for personalised ads in EEA/UK — decide: certified CMP vs non-personalised-only at flip time |
| House ad rules (config note) | ✅ "never resemble job cards / application buttons / nav" — enforced by placement review at flip |

## Niche readiness (rating → what 9–10 requires)
| Property | Rating (desk) | Gap to 9–10 | Revenue levers |
|---|---|---|---|
| Writers | A | flagship — protect; keep cadence | affiliate rails already scaffolded (`site.config.affiliate`), premium guides |
| Tech | A− | +6–10 evergreen guides (already 98), tool keep-fresh loop | high-RPM niche; tools = return traffic |
| Home & DIY | A− | depth in top categories; seasonal refresh | **highest RPM niche in the portfolio** — prioritise |
| Fitness | B+ (post-b18) | interactive tools #2; soreness/stretching guides | plan-completion email capture (mailto exists) |
| Sport | 8.5 (self) | cadence history; player pages gated on data | traffic volume niche; low RPM — value = audience scale |
| Entertainment | B+ (post-b19, 9 guides + list depth) | recommendations lists (dated, rot-checked) | volume niche; low RPM |

## Flip-day checklist (when approved)
1. Paste `ca-pub-…` into `site.config.json`, set `enabled: true` → deploy (ads.txt + meta + script appear everywhere automatically).
2. Choose CMP vs non-personalised for EEA/UK; document the choice on the privacy pages.
3. Review first-week placements against the config note; kill anything resembling nav/cards.
4. Only then consider `affiliate.enabled=true` per `docs/revenue-rails.md`.

## Batch 21 (11 Sep 2026) — fitness card live, old host purged, ENT ×11, Home ×8
- Fitness landing card: WORKSHOP_PUBS flipped to "live" → real anchor on the hub ("Enter Fitness →"); hub meta now "Six publications. One house standard."
- Old GitHub Pages links: clean_recovered() now rewrites ANY ojeology.github.io/nextclip/* URL to /entertainment/ and keeps /entertainment/ anchors live when stripping site-relative links. Site-wide old-host references: 0.
- Entertainment: +6 evergreen guides (box office mechanics, shorter seasons, canon vs filler, K-drama starter route, cult classics, reading reviews) + 3 recovered gems published (10 Korean movies, best anime now, Agent Kim/Squid Game S3) + 2 archive merges (Interstellar pair, Korean-cinema pair). 43 pages: recommendations 18, explainers 19, opinion 6. `beginners-guide-to-making-money-online` stays retired permanently (Money removed + YMYL/AdSense risk).
- Home & DIY: roadmap batch 10 (+8 kitchen & bedroom classics: oven, shower drain, freezer defrost, mattress, washer seal mould, kettle descale, cast iron, fridge temperature). Home property: 107 pages.
- Chain: 922 pages / 99,128 links OK; allowlist v26 (912 routes). Ratings moved: Home A−→A, Fitness B+→A−, Entertainment B+→A−.

## Batch 22 (11 Sep 2026) — catalogue + chrome parity
- Browse-the-movies catalogue (40 titles, 63 verified links) = AdSense "helpful inventory": deep internal linking from a browse surface, zero thin pages.
- Entertainment + Fitness now carry the full site chrome (drawer nav, dark mode) — UX parity across all six niches; nothing for an AdSense reviewer to flag as half-built.
- Entertainment holds at A−; next levers: Writers depth, Sport content wave.
