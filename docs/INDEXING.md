# Getting new pages seen quickly

Four mechanisms, in order of how much they actually matter for BRYME.

---

## 1. Sitemap — the workhorse (Google, Bing, everyone)

`sitemap.xml` is rebuilt on every build. 862 URLs, `lastmod` on anything that changed.

Submit **once** in Search Console → Sitemaps → `sitemap.xml`. After that Google rechecks it
on its own schedule. Don't resubmit.

Google **ignores** `<priority>` and `<changefreq>` — the build doesn't emit them. It uses
`<lastmod>` only when it's "consistently and verifiably accurate", which ours is, because it
comes from real content changes rather than the build clock.

## 2. News sitemap — time-sensitive football

`news-sitemap.xml`, also rebuilt every build, advertised in `robots.txt`.

Google's rules, which the build enforces:

- Articles from the **last two days only** — older entries drop out automatically
- Max **1,000** entries
- Required tags: publication name, language, publication date, title
- **Same file, updated** — never a new one
- An **empty file is valid** between publishing runs. Search Console may warn; ignore it.

**What goes in it:**

- Match pages that gained a preview or a result in the window — automatic
- Sports articles that explicitly opt in with `"newsworthy": true`

**The opt-in matters.** Evergreen pieces — the Champions League format explainer, all-time
records, the season guide — are reference material, not news. A news sitemap padded with
explainers is one Google learns to distrust. Default is *excluded*; you have to mark a piece
as news deliberately.

```json
{ "slug": "community-shield-2026-arsenal-manchester-city", "newsworthy": true }
```

Honest expectation: Google News surfaces weigh expertise, authority and a **consistent
history of original reporting**. This file makes BRYME technically eligible. It does not
manufacture a track record. It's plumbing laid early, not a shortcut.

## 3. IndexNow — Bing, Yandex, Seznam

```bash
node scripts/indexnow.js --since 2026-08-17          # dry run
node scripts/indexnow.js --since 2026-08-17 --send   # submit
```

Free, no daily cap, no content-type restriction, usually fetched within hours.

**Google does not participate.** This does nothing for Google. It is worth running anyway
because Bing traffic is real and football content is time-sensitive.

URLs come from `lastmod` in both sitemaps, so only genuinely changed pages are submitted.
The key lives at `/<key>.txt` in the site root and is recorded in `site.config.json` —
if that file stops being served, IndexNow returns 403.

## 4. Manual Request Indexing — Google, ~10/day

Search Console → paste URL in the top search bar → **Request Indexing**.

```bash
node scripts/request-indexing.js --since 2026-08-17
```

Prints only genuinely changed URLs. Quota is shared between inspections and requests, so
every URL you *look up* also counts. Spend it on pages where the delay actually costs
something — a match preview before kickoff, a result page just after.

Don't resubmit the same URL. It doesn't help and it burns tomorrow's quota.

---

## What is NOT available

**The Google Indexing API does not apply to BRYME.** Google's documentation restricts it to
pages carrying `JobPosting` or `BroadcastEvent` structured data — job listings and
*livestreaming video*. Match previews and reports are neither.

Faking `BroadcastEvent` markup to qualify would be structured-data spam, risks a manual
action on the whole domain, and Google states outright that abuse can have API access
revoked. Not worth it for pages that get crawled anyway.

**Google Publisher Center is not an application.** There has been no approval process since
December 2019 — Google's own help page says "Google automatically considers all web content
for inclusion in Google News, so you don't need to apply." Google also stopped using RSS
feeds submitted through Publisher Center, and publication pages are now auto-generated.
It's a branding tool for sites already being picked up, not a way in.

**The sitemap ping endpoint was deprecated in 2023.** Nothing to call.

---

## Matchday routine

```bash
# after adding a result and post-match analysis
node scripts/build-static-foundation.js
git add -A && git commit -m "Result: ..." && git push

# once Render has deployed
node scripts/indexnow.js --since $(date +%F) --send     # Bing, instant, free
node scripts/request-indexing.js --since $(date +%F)    # then submit these by hand
```

The news sitemap updates itself in the same build. Nothing extra to remember.
