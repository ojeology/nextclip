# SECOND-PASS TRAILER DISCOVERY — COVERAGE REPORT

Generated: 2026-08-12T21:12:30.933Z

## Headline numbers
| Metric | Count |
|---|---|
| Total catalogue titles | **630** |
| Official full trailers | **568** |
| Official teasers | **14** |
| Official clips | **1** |
| Community / fan-made fallbacks (clearly labelled) | **17** |
| Still unavailable | **30** |
| Broken / wrong trailers detected & quarantined | **0** |
| **Trailer coverage** | **95.2%** (600/630) |

## Method
1. **Audit** — every title without a verified trailer listed with type/year/country/language/current status.
2. **Search** — 2–5 adapted YouTube queries per title: `[title] official trailer`, `[title] (year) official trailer`, `[title] official teaser`, plus platform adaptation (Crunchyroll for anime, Netflix/HBO for series) and language adaptation (Hindi/Yoruba/Korean/Japanese/Chinese for regional titles).
3. **Verify every candidate** — video exists (oEmbed), title overlap ≥ 0.6 (roman-numeral aware, e.g. "Frozen II" ↔ "Frozen 2"), ±1-year tolerance gate, channel on the 180+ studio/distributor/aggregator allowlist (word-boundary matched, so "podcast" can't match "DC"), trailer-word gate (rejects full-movie listings), spin-off colon gate ("The Walking Dead: Dead City" ≠ "The Walking Dead"), short-title prefix gate ("Poetry Season" ≠ "Poetry"), date-context gate ("Returns October 1" ≠ "October 1").
4. **Classify** — official-trailer / official-teaser / official-clip / fan-made (community channels only as last resort, always labelled).
5. **Human review of machine results** — 12 machine matches rejected after review (spin-offs, film-on-series, wrong-version trailers).
6. **Apply** — verified IDs written to content/catalogue.json (or content/trailers.json overrides for legacy records). No duplicate records created; existing verified data untouched.

## Still unavailable (30) — re-checkable next pass
A Bittersweet Life, Bajrangi Bhaijaan, Barry Lyndon, Dandadan, Dhoom 3, Fullmetal Alchemist: Brotherhood, Ije: The Journey, Kabir Singh, Kumbalangi Nights, Kuroko's Basketball, Living in Bondage: Breaking Free, Living in Bondage: Breaking Free, Masaan, Merry Men, Nneka the Pretty Serpent, Phone Swap, Sairat, Sholay, Slam Dunk, Speed 2: Cruise Control, Stree, Super Deluxe, The Figurine, The Great Indian Kitchen, The Man from Nowhere, The Milkmaid, Toradora!, Uri: The Surgical Strike, Violet Evergarden, X2: X-Men United

## Why these remain
- Official trailer exists only on non-verifiable channels (fan uploads of old classics like Sholay, Speed 2, X2).
- Official uploads exist but could not be surfaced in top search results without guessing IDs (Dandadan, FMA: Brotherhood) — next pass may find them.
- Series whose only official trailer is for the film adaptation (Slam Dunk, Violet Evergarden, Miraculous, Downton Abbey, The Walking Dead spin-offs).

## Future-proofing
- `trailerLastChecked` and `trailerVerificationStatus` on every candidate.
- `content/second-pass-results.json` remembers rejected video IDs so wrong videos are never re-attached.
- Re-run anytime: `python3 scripts/second_pass_discovery.py` → review → `python3 scripts/apply_second_pass.py` → build.
