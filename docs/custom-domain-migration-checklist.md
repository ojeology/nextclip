# BRYME — Custom Domain Migration Checklist (and the AdSense gate)

**Why this matters:** the custom domain is the single remaining blocker to the AdSense application (Part B of the master strategy). Everything else — content, country pages, verification record — is in place. Do this before applying.

Current canonical origin: `https://bryme.onrender.com` (in `site.config.json` → `siteUrl`).
All generated canonicals, OG tags, sitemap and internal URLs follow that value, so there is exactly **one config flip**, then a rebuild.

---

## Phase 1 — Buy and wire the domain

- [ ] **1.** Choose the domain. Short, brandable, writer-legible: `bryme.` + `.com` first choice; `.co` / `.writers.` variants only if `.com` is hostile. Avoid hyphens/numbers.
- [ ] **2.** Register it (Cloudflare Registrar, Porkbun, or Namecheap — at-cost pricing, no upsells). Turn on **auto-renew** and registrar lock the moment it's live.
- [ ] **3.** In Render → your `bryme-website` static service → **Settings → Custom Domains → Add**, enter the domain (apex `bryme.example.com` **and** `www`).
- [ ] **4.** Render shows the DNS records to create. At the registrar:
  - **Apex:** `A` record → Render's IP (shown in the dashboard) — or ALIAS/ANAME if the registrar supports it
  - **www:** `CNAME` → your Render subdomain (`bryme-website.onrender.com` or similar)
  - Let Render provision the **TLS certificate** (automatic, free). Wait for both hostnames to show "Verified".
- [ ] **5.** Decide the canonical host: **apex** (recommended — cleaner in print/audio) or `www`. Redirect the other one to it. Render does this in the domain settings ("Redirect to primary domain").

## Phase 2 — Flip the config (the one true change)

- [ ] **6.** Update `site.config.json` → `"siteUrl": "https://YOUR-DOMAIN"` locally.
- [ ] **7.** In Render's environment, set **`SITE_URL=https://YOUR-DOMAIN`** (the env var already declared in `render.yaml` as `sync: false`). This is what the live build uses.
- [ ] **8.** Commit the `site.config.json` change and push → Render auto-deploys → the build regenerates every canonical, the sitemap, RSS and OG tags on the new origin.
- [ ] **9.** Run the gate both ways:
  ```bash
  python3 scripts/check-canonical-domain.py                     # no old-host leakage
  SITE_URL=https://YOUR-DOMAIN python3 scripts/check-canonical-domain.py
  npm run validate
  ```
- [ ] **10.** Spot-check live: homepage canonical, one article, `/sitemap.xml`, `/robots.txt` — all must show the new domain. Old `bryme.onrender.com` URLs should still resolve (Render keeps the subdomain; it now mirrors the site — fine, it's not linked anywhere).

## Phase 3 — Search engines and the IndexNow key

- [ ] **11.** Google Search Console: add a **new property for the new domain** (Domain property if you can do DNS TXT; URL-prefix otherwise). Keep the old property — history is data.
- [ ] **12.** Submit the new **sitemap** (`/sitemap.xml`) in the new property; use **URL Inspection → Request indexing** on the homepage and the money pages (Rates & business cluster, country pages).
- [ ] **13.** The `google2ec8f794263d784f.html` verification file and IndexNow key file are already committed at the repo root — they'll be served on the new domain automatically. Re-verify Bing/IndexNow once the domain resolves.
- [ ] **14.** Update any external profiles/author bios that link the old URL (social, bylines, directories). These are your earliest trust signals for the new host.

## Phase 4 — The AdSense gate (only after Phase 3 is green)

- [ ] **15.** Confirm all of the following before applying:
  - [ ] Site serves on the custom domain over HTTPS, canonicals flipped
  - [ ] `/about/`, `/contact/`, `/editorial-policy/`, `/privacy/`, `/corrections/`, `/disclaimer/` all live (they are — verified 2026-09-06)
  - [ ] `privacy` page mentions ads/cookies *before* ads exist (AdSense checks this)
- [ ] **16.** Apply at adsense.google.com with the **custom domain only**. Expect 1–14 days of review; do not change anything structural while it's pending.
- [ ] **17.** On approval: put the `ca-pub-...` ID in `site.config.json` → `adsense.caId`, flip `enabled` to `true`, and review the consent/privacy flow **before** redeploying. The config note stands: ads must never resemble job cards or application buttons.
- [ ] **18.** After ads go live, re-run `npm run validate` and eyeball 3–4 money pages — layout shift around ads is a UX and a quality-policy issue.

---

**Sequencing rule from the strategy (Part H):** audience → commercial demand → monetise. The domain unblocks the application; the 50-article roadmap is what makes approval and revenue likely. Nothing in this checklist replaces that.

*Prepared 6 September 2026 alongside the tax-guide batch (US/Canada/Australia).*
