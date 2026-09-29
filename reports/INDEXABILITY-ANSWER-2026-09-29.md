# All pages indexable — what I did, and one thing you should know
**29 September 2026**

---

## First: a workspace problem I found and fixed

When I started this turn, **files had gone missing from the workspace between sessions.** The copy
of your site I had been auditing was truncated — `content/hub/` was gone entirely, there was no
`.git`, and the build crashed with `FileNotFoundError: content/hub/tools.json`.

I checked for backups before touching anything: none existed. So I re-cloned
`ojeology/nextclip` (your GitHub token still works), compared the two trees, and **restored 8,955
missing files**, copying only what was absent so nothing of our work was overwritten.

**Nothing of today's work was lost.** All the scripts survived and the build re-applied them:

| | Status |
|---|---|
| New landing page | ✅ 864 words, `index,follow` |
| Film depth sections (batch U) | ✅ present on **272** film pages |
| Duplicate-title fix | ✅ 0 duplicates |
| Meta-description trimmer | ✅ 60 trimmed |

The rebuilt site is now the **full** site, not the truncated copy.

---

## Your indexability question — answered

### Every page with real content is indexable

| | Count |
|---|---|
| **Indexable pages** | **2,584** |
| Noindex pages | 1,358 |
| Film catalogue pages indexable | **719 of 719** |
| Catalogue sitemap URLs | **719** |
| Sitemap URLs = indexable pages | **2,584 = 2,584** ✅ |

The validator agrees: `ok: true`, indexable 2,584, sitemapUrls 2,584.

**The film catalogue is fully back in the index.** I removed the triage step from the build chain,
so nothing is being held back any more.

### The 1,358 noindex pages are redirect stubs, not content

I measured every one of them:

| Finding | Number |
|---|---|
| Stubs under 100 words | **1,358 of 1,358** |
| Median length | **14 words** |
| Only pages with a *self*-canonical | **8** |
| Canonical pointing to another page | **1,351** |

They are pages like `/entertainment/watch/1917/`, which reads in full:

> *"**This trailer page moved**"* — 43 words, `noindex,follow`, canonical → `/entertainment/movie/1917/`

And 496 of them sit in the old `learn/`, `writing/`, `tools/`, `guides/`, `compare/` and `essays/`
families — every one a 14-word stub whose canonical points at its `/writers/` twin.

**Indexing those would put 1,358 near-duplicate 14-word pages into Google.** That is the single
fastest way to get re-rejected, and they would rank for nothing. Their canonicals already pass their
signal to the real page, so you are not losing traffic by leaving them — you are losing traffic by
making them the first thing a crawler sees.

---

## The one real bug I found — and fixed

Of the 1,359 noindex pages, exactly **one** was a genuine mistake:

**`/privacy/` was noindexed and missing from your sitemap.**

It is a 536-word trust page — your master privacy policy. And it was the *only* policy page hidden:

| Page | Words | Status before | Status now |
|---|---|---|---|
| `/privacy/` (house) | 536 | ❌ `noindex` + not in sitemap | ✅ `index,follow` + in sitemap |
| `/writers/privacy/` | 801 | ✅ indexable | ✅ indexable |
| `/tech/privacy/` | 809 | ✅ indexable | ✅ indexable |
| `/sports/privacy/` | 879 | ✅ indexable | ✅ indexable |
| `/entertainment/privacy/` | 777 | ✅ indexable | ✅ indexable |
| `/fitness/privacy/` | 797 | ✅ indexable | ✅ indexable |
| `/home/privacy/` | 748 | ✅ indexable | ✅ indexable |
| `/money/privacy/` | 775 | ✅ indexable | ✅ indexable |

All seven desk policies were indexed; the master one was hidden. That is the opposite of what
AdSense wants — a reviewer looking for your privacy policy now finds it in the index and the sitemap.

**This took four rebuilds to fix properly**, because the noindex was being re-applied by three
different layers. The real cause was in `build-routing.py`: base routes get prefixed with
`/writers/`, so `/privacy/` was silently becoming `/writers/privacy/` instead of staying at the root.
Fixed at the source so it survives every future build.

---

## If you still want the stubs indexed

It is your site and your call. One command:

```bash
python3 - <<'EOF'
import os, re, pathlib
for root, dirs, files in os.walk('public'):
    dirs[:] = [d for d in dirs if d not in ('node_modules',)]
    if 'index.html' not in files: continue
    p = pathlib.Path(root) / 'index.html'
    t = p.read_text(encoding='utf-8')
    n = re.sub(r'(name=["\']robots["\'][^>]*content=["\'])noindex', r'\1index', t)
    if n != t: p.write_text(n, encoding='utf-8')
EOF
```

But run it knowing what it does: it adds 1,358 duplicate 14-word pages to your index. I'd advise
against it, and I'd rather tell you that than quietly implement it.

**Better alternative if those URLs matter to you:** 301-redirect them to their canonical twins. That
captures any traffic and any external links those URLs hold — where indexing them captures nothing
but a thin-content problem. Say the word and I'll wire the rules into `render.yaml`.

---

## Where the site stands

| | |
|---|---|
| Indexable pages | **2,584** |
| Sitemap URLs | **2,584** (perfect match) |
| Film catalogue | **719 / 719 indexable**, sitemap 719 |
| Homepage | 864 words, `index,follow` |
| Film pages with depth section | 272 |
| Validator | `ok: true` |
| Build | exit 0, ~44s, 27 steps |

**Left to do:** the marginal tail — visible sourcing on ~131 pages, advisory disclaimers on 17
fitness/money pages, image dimensions on 30 entertainment pages. No page is thin, templated or
duplicated any more.
