# BRYME Fix Checklist

Working through the audit (`reports/site-audit-2026-09-03.md`) one item at a time.
Status: ⬜ not started · 🔄 in progress · ✅ done

---

## PHASE 1 — AdSense blockers (must clear before applying)

- 🔄 **1. Cookie consent banner** — GA4 loads on 3,201 pages with no consent. GDPR exposure + documented AdSense rejection trigger. Must block analytics until the user chooses.
- ⬜ **2. Resolve the 16 draft placeholders** — "Editorial draft — not published" pages in `/sports/articles/`. Noindexed, but a human reviewer still clicks them. Finish or delist.
- ⬜ **3. Sitewide disclosure block** — only 1 of 80 money pages has a financial disclaimer, on YMYL content incl. binary options. Add standing risk + affiliate disclosure.
- ⬜ **4. Author / E-E-A-T signals** — 1 author, 35 bylined pages of 3,378. Expand author page, byline everything, add "Reviewed on" dates.
- ⬜ **5. Pre-application sweep** — empty categories, broken links, mobile check, then apply.

## PHASE 2 — Revenue (next 30 days)

- ⬜ **6. Deepen 10 Make Money pages** — median is 53 words. Take ten to 1,200+ with first-hand Nigerian detail (real fees, withdrawal experience, payout proof).
- ⬜ **7. Naira streaming cost hub** — Netflix vs Showmax vs Prime vs DStv in ₦, data usage per hour on NG networks. Nothing like it exists.
- ⬜ **8. 10 more Tech `vs` comparisons** — the format already works and ranks.
- ⬜ **9. Add AdSense code** — only after 1–5 are clear.

## PHASE 3 — Moat (next 90 days)

- ⬜ **10. Nollywood vertical** — genuinely open territory; does not compete with IMDb.
- ⬜ **11. "Where to watch in Nigeria" template** — systematic across top 100 titles.
- ⬜ **12. FAQPage schema** — only 4 pages have it. Easy AI Overview wins.
- ⬜ **13. NewsArticle schema on sports** — currently 0, and `news-sitemap.xml` already exists.

## Explicitly NOT doing

- ❌ More movie pages in the current format (scaling into a category Google demoted in March 2026)
- ❌ Chasing live scores against FotMob
- ❌ Anime user accounts

---

## Log

### ✅ 1. Cookie consent banner — done 2026-09-03

**Problem.** `assets/analytics.js` fired GA4 (`G-NQKHPBYFE8`) immediately on all 3,201 pages. No consent UI anywhere on the site.

**Approach.** Rewrote `assets/analytics.js` as a consent gate rather than editing 3,201 HTML files — every page already loads that one script, so the fix propagates everywhere with no page edits and no risk of missing a template.

**What it does now:**
- GA4 is **not** loaded until the visitor accepts. Declining means the tag never loads at all.
- Google Consent Mode v2 defaults are set to `denied` *before* anything else, so even the pre-consent state is compliant and AdSense-ready (`ad_storage`, `ad_user_data`, `ad_personalization`, `analytics_storage`).
- Banner appears bottom-anchored, matching site dark theme, with equally-weighted Accept / Decline buttons (required — a hidden or de-emphasised decline is a dark pattern and fails review).
- Choice stored in `localStorage` for 6 months, then re-asked.
- Respects `navigator.globalPrivacyControl` and `Do Not Track` — auto-declines without showing the banner.
- Keyboard accessible, `role="dialog"`, focus-visible outlines, `prefers-reduced-motion` honoured.
- A "Cookie settings" link in the footer lets users change their mind (`/privacy/#cookies` or any `[data-cookie-settings]` element re-opens it).
- No external requests, no cookies of its own, no layout shift.

**Also:** added a `#cookies` section to the privacy policy documenting the choice and how to revisit it, and a "Cookie settings" footer link on the main hub pages.
