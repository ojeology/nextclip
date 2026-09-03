# BRYME Site Audit — 3 September 2026

Full-site audit, vertical by vertical, benchmarked against the leaders in each niche.

**Headline:** the technical SEO is genuinely strong — that 95% Ahrefs score is earned. The gaps are not technical. They are **strategic** (one vertical is in a category Google actively demoted in March 2026), **commercial** (zero monetisation code on a site built to monetise), and **legal** (GA4 runs with no consent banner).

---

## 1. What the site actually is

| Vertical | Pages | Median words | Verdict |
|---|---|---|---|
| Movies | 764 | 456 | Real content, unique descriptions |
| Sports | 2,036 | — | 1,660 correctly noindexed match stubs |
| Series | 145 | 411 | Solid |
| Anime | 128 | 372 | Solid |
| Make Money | 80 | 53 | **Mostly hub/listing pages — thin** |
| Tech & AI | 36 | 350 | Under-built |
| Articles | 24 | 640 | Best writing on the site |

**Technical health — genuinely good, leave it alone:**
- 100% image alt coverage (1,694 images sampled)
- Schema everywhere: 2,911 BreadcrumbList, 1,848 SportsEvent, 776 VideoObject, 622 Movie, 304 Article
- 399/400 movie meta descriptions unique
- All 7 trust pages exist; sitemap valid; every vertical hub has 3,000+ inbound internal links
- 1,660 unplayed match pages correctly `noindex,follow` — only 97 match URLs in sitemap. This is disciplined work.
- Sports auto-updates 3×/day via GitHub Actions with source-verification that refuses unsourced results

---

## 2. The five things that actually matter

### 🔴 #1 — Movies is in the category Google demoted (biggest strategic risk)

The **March 2026 core update** hit "where to watch" content hard. Sites that exist to tell you where a title streams were, in Amsive's analysis, *decimated* — **JustWatch −24%, OnTVTonight −39.5%, Pluto.tv −37.8%** — while first-party platforms gained (IMDB +79.3, Netflix +11.9). Arts & Entertainment led all loser categories.

764 movie pages — 60% of the site's real content — sit in exactly that bucket. They're well built, but "What X is about / Why you might like it / Where to watch" is the pattern Google just devalued, and BRYME will never outrank IMDb on it.

**Fix:** stop competing on catalogue data, compete on **angles no database has**. Nigeria is the unfair advantage:
- "Where to watch X in Nigeria" — actual local availability: Showmax, DStv, Netflix NG pricing in ₦, which VPNs are needed. You already have one such page; it should be a hundred.
- Nollywood. There is no serious, well-structured English-language Nollywood discovery site. IMDb's coverage is shallow. This is an open goal and it is *yours*, not a global competitor's.
- Data-per-page nobody else has: naira subscription cost comparisons, data-usage-per-hour for streaming on Nigerian networks.

### 🔴 #2 — Zero monetisation code, and a consent problem blocking it

`grep` for `adsbygoogle|ca-pub` returns **0 files**. The site is built for AdSense and has no ad code. Separately:

**GA4 (`G-NQKHPBYFE8`) loads on every page with no cookie consent banner.** Zero files match a consent/GDPR pattern. The privacy policy does mention cookies and analytics, so policy/reality are aligned — but running analytics cookies with no consent mechanism is both a GDPR exposure and a documented AdSense rejection trigger. One publisher in the research cited 15 rejections fixed purely by aligning consent with actual cookie behaviour.

**Fix, in order:** (1) add a consent banner before applying; (2) then add AdSense. Also worth noting: `data-no-ads="1"` is already set on the predictions page — good instinct, keep ads off prediction content.

### 🟠 #3 — Make Money is your best commercial asset and your weakest content

Median **53 words** across 80 pages. Highest-CPC vertical on the site, and it's mostly empty hubs. This is the single biggest revenue gap.

Worse, it's **YMYL** — Google applies its strictest quality bar to money content. Only **1 of 80** money pages carries a "not financial advice" style disclaimer. You have a page on the Pocket Option / Quotex trap, which is exactly the right protective-journalism angle, but binary-options content without risk disclaimers is a live AdSense policy risk.

**Fix:** pick 10 pages, take each to 1,200+ words with real first-hand detail (payout screenshots, actual Nigerian withdrawal experience, real fee maths). Add a standing risk/affiliate disclosure block sitewide. Ibrahim's Termux-on-Android origin story is exactly the "experience" signal Google's first E rewards — use it far more.

### 🟠 #4 — Empty categories will fail an AdSense review on their own

Research is unambiguous: *"If you have a navigation menu link labeled 'Fitness' and clicking it reveals only one post, or worse, an empty page, the review bot immediately marks the site as incomplete."*

Current state: **16 draft placeholders** in `/sports/articles/` reading "Editorial draft — not published". All correctly noindexed — but a human reviewer clicking through the Articles index still sees construction-zone pages. Tech has 36 pages spread across ~20 subcategories.

**Fix:** before applying to AdSense, either finish those 16 or remove them from listings entirely. Noindex protects rankings; it does not protect you from a reviewer's click.

### 🟡 #5 — One author, 35 bylined pages out of 3,378

`authors.json` has exactly one entry. Only 35 pages carry Person/author markup. December 2025's core update specifically refined **author entity signals**.

**Fix:** byline everything, expand the author page (photo, credentials, social/professional profiles), add "Reviewed on" dates to money and tech pages. Cheap, high-leverage.

---

## 3. Niche-by-niche vs the leaders

| Vertical | Benchmarks | Your gap | Winnable? |
|---|---|---|---|
| **Movies** | IMDb, JustWatch, TMDB | Catalogue depth — unwinnable | ❌ head-on / ✅ via Nigeria + Nollywood |
| **Sports** | BBC Sport, FotMob, FBref | No live scores, no xG, no player stats | ⚠️ not on speed — ✅ on Nigerian-angle + form-backed picks |
| **Make Money** | NerdWallet, Nairametrics | Depth, disclosures, first-hand proof | ✅ **best opportunity** — local payment/withdrawal reality |
| **Tech & AI** | TechCabal, Techpoint Africa | Only 36 pages | ✅ your `vs` comparisons already rank-shaped |
| **Anime** | MAL, AniList | No user accounts/lists | ❌ deprioritise |

**Sports is stronger than you may realise.** The 3×/day sourced auto-updater with a validator that refuses unsourced results is real infrastructure most small sites lack. But no site beats FotMob on scores. The defensible position is what you just built on the predictions page: **transparent, evidence-backed opinion**. Nobody else shows the form behind every pick.

---

## 4. What I'd actually add (priority order)

**Before applying to AdSense**
1. Cookie consent banner (legal + rejection risk)
2. Resolve the 16 draft placeholders
3. Sitewide affiliate/financial disclosure block
4. Expand author page, byline everything

**Next 30 days — revenue**
5. Take 10 Make Money pages to 1,200+ words with first-hand Nigerian detail
6. Naira-priced streaming cost comparison hub (Netflix vs Showmax vs Prime NG)
7. 10 more Tech `vs` comparisons — the format already works

**Next 90 days — moat**
8. **Nollywood vertical.** Genuinely open territory, and nothing about it competes with IMDb.
9. "Where to watch in Nigeria" as a systematic template across the top 100 titles
10. FAQPage schema (only 4 pages have it — easy AI Overview/rich-result wins)
11. NewsArticle schema on sports (currently 0; you have a news-sitemap.xml already)

**Do not do**
- More movie pages in the current format — that's scaling into a demoted category
- Chasing live scores against FotMob
- Anime user accounts

---

## 5. Bottom line

You do not have a technical problem. You have **3,378 well-built pages, no ads on any of them, and 60% of your content in a category Google demoted five months ago.**

The three moves that matter: **get monetisation live (with consent first)**, **make Make Money actually deep**, and **build the Nigeria/Nollywood angle** — the one thing on this site that IMDb, JustWatch and FotMob cannot copy.
