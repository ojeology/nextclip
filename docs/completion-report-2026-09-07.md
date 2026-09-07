# BRYME — Completion Report & Handover

**Date:** 7 September 2026 · **Repo:** `Ojeology/nextclip` (pushed to `main`) · **Live:** https://bryme.onrender.com

---

## 1. What the site is now

| Metric | Count |
|---|---|
| Learn-hub guides | **191** |
| Essays | 9 |
| Browser tools | **43** |
| Indexable routes (== sitemap == allowlist v23) | **487** |
| OG share cards | 201 |
| Internal links (build-gate-verified) | 54,428 across 498 pages |

The original 50-article master-strategy roadmap is **complete** — including Article 50
(`Emerging writing platforms: Polymemo`), which was held back until the platform could be
verified independently. It shipped today as a claim-vs-verified-vs-unknown piece, aligned
with the earlier essay `Polymemo review — the 49% nobody mentions` (70/20/10 split, 5,000-pt
redemption floor at a 70% rate = 49¢ per reader dollar; earning proposition untested).

## 2. Recent ships (this stretch)

| Commit | What |
|---|---|
| `16c31a0245` | Late-payment letter builder tool (3-stage escalation, 10 currencies, copy-as-text) — closes the get-paid trio: agree → bill → chase |
| `0572d95aeb` | **Link integrity build gate** — `scripts/check-internal-links.py` sweeps every href in `public/`, runs inside `npm run build`, fails the build on any broken internal link (failure path tested) |
| `a7a8ebafbd` | Fixed the last dead body link (`choosing-research-tools` → correct `academic-writing/how-to-cite-sources/` slug) |
| `a3c01f935c` | Nigeria + India rates guides (rates family now 9 markets) + freelance agreement builder (10 clauses, 10 currencies) |
| `75d161d20e` | Invoice generator (9 currencies, line items + tax, print isolation) |
| this push | **Article 50** — `emerging-writing-platforms-polymemo` guide (international pillar, 8 guides) |

## 3. Everything blocked is blocked on YOU — the activation checklist

These need no code changes, only your actions:

1. **Custom domain** → unblocks AdSense. Follow `docs/custom-domain-migration-checklist.md`;
   after DNS propagates run `python3 scripts/check-canonical-domain.py`.
2. **Render dashboard cleanup** — delete any dashboard redirect rules; they shadow site paths.
3. **Newsletter provider** — when chosen, set in `site.config.json`:
   `newsletter.mode: "form"` + the form `endpoint`. The `/newsletter/` page already renders it.
4. **Channels** — `follow.telegram` and `follow.whatsapp` URLs in `site.config.json`.
5. **Affiliate rails** — `affiliate.enabled: true` + `affiliate: true` front matter on chosen guides.
6. **GitHub token** — the token pasted in chat is still live; revoke/regenerate it (reminder ×10).

## 4. Pending work with runbooks

- **GSC re-pull (due 2–4 weeks from 2026-09-07):** export the four query/page CSVs from
  Search Console → save to `/home/user/uploads/` → rerun the analysis (baseline:
  `reports/search-console-analysis-2026-09-07.md`; 64 kw / 178 impr / 16 clicks / CTR 8.99%).
  This data gates **wave 2 winner-expansion**: expand the pages already earning impressions.
- **Editor interviews:** the Lagos outreach kit (`BRYME-LAGOS-OUTREACH-KIT/`) is ready to send;
  interviews unlock quoting named editors (E-E-A-T).

## 5. Maintenance commands

```bash
npm run build                      # full rebuild — now FAILS on any broken internal link
node scripts/validate-site-quality.js   # structure, metadata, sitemap==allowlist==indexable
python3 scripts/check-canonical-domain.py
npm run submit:engines             # IndexNow + sitemap ping after every push
```

Standing content rules: 5+ genuine internal links per article (body links now build-enforced),
YMYL protocol for tax/legal/health (current primary sources, exact jurisdiction, disclaimers,
last-reviewed dates), no earnings claims without evidence.
