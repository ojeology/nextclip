# Thin pages + site-wide Lighthouse

**22 Aug 2026.** Lighthouse is a **per-page** tool. There is no single “whole website” score. This pass ran **15 representative URLs** covering every vertical, plus a thin stub and a rich title page.

## Do you have thin movie pages?

**Yes — a second, unfinished catalogue is live.** The 648 built titles (Shōgun, Interstellar, No Way Home…) are not thin. A later drop of extra `/movie/` and `/series/` files is.

| Class | Count | Indexable? | What it is |
|---|---:|---|---|
| Built catalogue titles | **648** | yes | Synopsis, trailer, details. Main-body median ~600 words. None under 150. |
| Empty stubs | **52** | **were yes — now noindex, out of sitemap** | Trailer chrome only. “More details coming soon.” No lead, no cast, no watch section. |
| Short / incomplete extras | ~125 | still yes | Live pages with a short or missing lead. Not empty, not as complete as the 648. |
| Type-mismatch `/movie/<series>/` | 156 | noindex redirects | Already contained in the previous commit. |

Worst bug on the 52 stubs: **canonical pointed at the homepage** (`https://bryme.onrender.com/`). Google was being told “this Blast / Coraline / Lockdown URL is really the home page.” That can dilute the real homepage.

### What I did just now (URLs kept)

- Self-canonical on all 52
- `noindex,follow`
- Removed from `sitemap.xml` (1,226 → **1,174**)
- Fixed `/series/lucky-2026/` homepage canonical (that one has a trailer page; it stays indexable)

I did **not** delete the URLs. I did **not** invent synopses. The brief said not to publish thin pages and not to add the remaining ~500 yet — these 52 should stay off the sitemap until they have real copy.

Full list: `reports/empty-title-stubs.txt`.

## Lighthouse (mobile, this tree)

| Area | URL | Perf | A11y | BP | SEO | LCP |
|---|---|---:|---:|---:|---:|---|
| Home | `/` | 72 | 96 | 100 | **100** | 7.7s |
| Entertainment | `/entertainment/` | 71 | 96 | 96 | 92 | 7.2s |
| Movies hub | `/movies/` | 73 | 100 | 100 | **100** | 5.2s |
| Series hub | `/series/` | **96** | 92 | 96 | **100** | 2.3s |
| Anime hub | `/anime/` | **96** | 92 | 96 | **100** | 2.3s |
| Search | `/search/` | 87 | 100 | 100 | **100** | 3.2s |
| Articles | `/articles/` | 73 | 98 | 100 | **100** | 8.7s |
| Sports | `/sports/` | 68 | 95 | 100 | **100** | 9.0s |
| Make Money | `/make-money/` | 87 | 100 | 100 | **100** | 3.1s |
| Tech | `/tech/` | 80 | 95 | 100 | **100** | 4.9s |
| **Shōgun** | `/series/shogun/` | **95** | 96 | 100 | **100** | 2.4s |
| **Interstellar** (rich title) | `/movie/interstellar/` | **95** | 96 | 100 | **100** | 2.4s |
| No Way Home | `/movie/spider-man-no-way-home/` | **93** | 96 | 100 | **100** | 2.7s |
| **Blast** (empty stub) | `/movie/blast/` | 96 | 92 | 96 | **92** | 2.3s |
| Editorial | `/article/christopher-nolan-movies-order/` | 82 | 100 | 100 | **100** | 4.4s |

### How to read this

- **Title pages that were built properly score like a finished product** (Shōgun / Interstellar: 95 perf, SEO 100).
- **Hub / home / sports are slower** because of big hero images (LCP 7–9s). That is not a movie-page problem.
- **Blast SEO 92** is the stub: empty “Watch Now” / “Watch on YouTube” anchors. That is why those 52 are now `noindex`.
- Entertainment SEO 92 is generic “click here”-style link text, not thin movies.

There is still **no one Lighthouse number for the whole site.** These 15 URLs are the map: every vertical + rich title + thin stub.

HTML reports live in `reports/lighthouse/` (local only — too large to commit).
