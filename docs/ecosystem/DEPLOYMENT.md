# THE BRYME — Deployment Runbook (build → domain → subdomains → AdSense)

**Sequence (per master plan §26, unchanged):** BUILD → TEST → AUDIT → APPROVE DESIGN → BUY DOMAIN → CONNECT DNS → CONNECT SUBDOMAINS → VERIFY → SEARCH CONSOLE → SITEMAPS → INDEXING → ADSENSE.

**Flag resolved:** `thebryme.com` **is available** (verified against the Verisign .com registry, 8 Sep 2026). Buy it when the design is approved — not before (§23–26).

**Trade-off confirmed in the plan:** the AdSense application now happens *after* the four publications are built. Expect approval revenue later than the old sequence; that is the accepted cost of the ecosystem architecture.

## What exists in the repo today

| Publication | Directory / source | Status |
|---|---|---|
| THE BRYME (master homepage) | `ecosystem/hub/` | **Built** — publication directory, family cards |
| BRYME Writers (flagship) | this repo's main build (`public/`) | **Live** — 191 guides, 44 tools, 489 routes; becomes `writers.thebryme.com` |
| BRYME Entertainment | `ecosystem/entertainment/` | **Built** — recovered archive shelf (6 restored editions + restoration queue) |
| BRYME Sport | `ecosystem/sports/` | **Skeleton** — opens after the archive/Bing-data audit; no betting content, ever |
| BRYME Tech | `ecosystem/tech/` | **Built** — 5 first-hand launch articles + house promise |
| Retired-content audit | `docs/ecosystem/retired-content-audit.md` | **Done** — every old URL classified A–E |

Each `ecosystem/*` dir is a self-contained static site (own stylesheet in its family identity, own sitemap.xml, robots.txt, about/privacy/contact). Regenerate all of them with `python3 scripts/build-ecosystem.py`. The main site build is untouched (the dir is excluded from the Writers build and its validator).

## Hostname configuration (no hard-coding, per plan §10–12)

- The Writers site's canonical origin already comes from one choke point: `site.config.json` → `SITE_URL`, and a **`SITE_URL` environment variable overrides the config on Render** — set it at migration, change nothing else.
- The ecosystem services read `PRODUCTION_DOMAIN` (env) or `ecosystem/config.json` (default `thebryme.com`).
- The Writers footer carries a **parent-brand hook**: set `site.config.json → parent.url = "https://thebryme.com"` at migration and the "one of the BRYME publications" line appears; until then it renders nothing.

## Render services to create (when you approve the design)

1. **`thebryme-hub`** — Static site · repo `ojeology/nextclip` · publish directory `ecosystem/hub` · build command: none needed (files are committed).
2. **`thebryme-entertainment`** — same, publish dir `ecosystem/entertainment`.
3. **`thebryme-sports`** — publish dir `ecosystem/sports`.
4. **`thebryme-tech`** — publish dir `ecosystem/tech`.
5. **Writers keeps its existing service** (this one). No rebuild.

## DNS (after buying the domain)

- At the registrar (Cloudflare/Porkbun recommended): add apex `A`/ALIAS records + `www` CNAME → master hub service; then CNAMEs for `writers`, `sports`, `entertainment`, `tech` → their services (Render shows the exact targets per custom domain).
- Add each custom domain inside each Render service, wait for certificate issue.
- Update Writers: set `SITE_URL=https://writers.thebryme.com` env var + `parent.url` config; run `python3 scripts/check-canonical-domain.py`.

## Search Console & sitemaps

- Verify a **Domain property** for `thebryme.com` (DNS TXT).
- Submit each service's own sitemap separately (`/sitemap.xml` on each subdomain — they contain only their own URLs by construction).
- Never submit a sitemap whose URLs don't resolve on the property it's submitted to.

## AdSense (last)

- Apply on the flagship (Writers) after the ecosystem stabilises; approval covers subdomains automatically per the plan's verified note.
- Ad-safety rule stays non-negotiable: ads never masquerade as navigation, tools, listings or buttons; no popups.

## Repo note (plan §"Repo check")

BRYME lives entirely in `ojeology/nextclip` — the name is a leftover from the pre-pivot movie site. Rename the repo to `bryme` in GitHub settings (redirects are automatic), then update the Render service's linked repo. Safe any time; do it before the domain migration to keep the runbook names clean.
