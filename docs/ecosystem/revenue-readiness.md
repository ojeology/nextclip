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
