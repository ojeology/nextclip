# Custom-domain migration (onrender.com -> your TLD)

BRYME's build already takes its canonical origin from one source of truth:
`SITE_URL` (env) → `site.config.json` → `siteUrl` (`scripts/bryme_config.py`).
There is **no hard-coded `bryme.onrender.com`** anywhere in the build, schema,
sitemap, robots or server. This document is the checklist to move to a custom
domain.

> **AdSense note:** Google AdSense requires an **owned top-level domain**. You
> cannot apply with `*.onrender.com`. Buy a TLD (e.g. `bryme.<brand>.com`),
> connect it, then apply for AdSense. Ads in subdomains are only allowed after
> the main TLD is approved.

## 1. Buy the domain
Choose a short, brandable TLD (`.com` preferred). `bryme.com` may be taken; a
brand variant keeps it clean and memorable.

## 2. Add the domain to Render and point DNS
- In the Render service, add the custom domain under **Settings → Custom Domains**.
- Set the required DNS record (usually a `CNAME` to `<service>.onrender.com`,
  or an `A`/`ALIAS`).
- Render will show the exact records to add at your DNS provider.
- Wait for the DNS to propagate and Render to issue the SSL/TLS certificate.

## 3. Switch `SITE_URL`
Set the `SITE_URL` env var in the Render service to the custom origin, e.g.:
```
SITE_URL=https://bryme.example.com
```
Then redeploy. All generated canonicals, sitemap `<loc>`, JSON-LD, Open Graph
and robots `Sitemap:` lines now point at the new host. `site.config.json`
keeps the Render host as a fallback; only the env var should differ in prod.

## 4. Verify with the readiness gate
```bash
SITE_URL=https://bryme.example.com npm run build
SITE_URL=https://bryme.example.com python3 scripts/check-canonical-domain.py
npm test
```
The check tool errors if any generated page still references `onrender.com` or
if a canonical/sitemap `<loc>` does not start with the configured `SITE_URL`.

## 5. Search Console / verification
- Register the new domain property in Google Search Console and Bing Webmaster
  Tools (DNS or HTML verification).
- Submit `/sitemap.xml` once.
- Add the new domain as the AdSense site **after** it is live and AdSense-ready.

## 6. Redirects and the transition (keep Render functional)
- Keep the Render deployment running so the old URL still serves during the
  transition.
- Set the custom domain as canonical (the `SITE_URL` env). Do **not** leave
  mixed canonicals between the subdomain and the new host.
- Optionally add a `301` redirect from the Render subdomain to the custom domain
  once Search has settled — but only after verification, and always with the
  canonical kept consistent on one host at a time.

## 7. Enabling AdSense AFTER the domain is approved
`site.config.json` → `adsense`:
- set `caId` to your real `ca-pub-...` ID;
- review `docs/ADS.md` (consent/CMP, placement rules, never over job cards/app
  flow);
- set `enabled: true` and add the ad code in clearly-labelled containers;
- run the release gates before deploying.
