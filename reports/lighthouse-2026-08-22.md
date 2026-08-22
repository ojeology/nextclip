# Lighthouse — 22 Aug 2026 (mobile)

Ran locally against the committed tree (`bc2d01f`), Chromium 151, Lighthouse 12.8.2.  
Live Render may take a few minutes to match.

| Page | Perf | A11y | Best practices | SEO |
|---|---:|---:|---:|---:|
| `/series/shogun/` | **95** | 96 | **100** | **100** |
| `/movie/spider-man-no-way-home/` | **93** | 96 | **100** | **100** |
| `/` homepage | 72 | 96 | **100** | **100** |

HTML reports: `reports/lighthouse/shogun-mobile.report.html`, `nwh-mobile.report.html`, `home-mobile.report.html`.

## Shōgun (the SEO case study)

- FCP / LCP 2.4s, TBT 10ms, CLS 0.005
- SEO 100: crawlable, indexable, unique title/description, valid canonical, tap targets
- Only a11y miss: **color-contrast** (same site-wide muted text on dark)

## Homepage 72

Not a regression from this SEO pass. LCP 7.7s is the homepage hero image. Title-page LCP is fine.

## Not done from these scores

- Contrast on muted labels (pre-existing)
- Homepage LCP (out of this SEO phase)
