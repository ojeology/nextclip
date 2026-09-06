# How to publish an essay on BRYME

Drop a markdown file in this folder and run `npm run build`. That is the whole
workflow. The file name becomes the URL: `my-essay.md` → `/essays/my-essay/`.

## Frontmatter

Every essay needs this block at the very top, between two `---` lines:

```markdown
---
title: The headline, written as a sentence
description: One or two sentences. This is what shows on the index page and in Google results.
dek: Optional standfirst that appears under the headline in larger type.
audience: uk
published: 2026-09-06
updated: 2026-09-06
keywords: [ai, submissions, editors, uk]
related: [british-vs-american-english, how-to-pitch-uk-editors]
---
```

| Field | Required | Notes |
|---|---|---|
| `title` | **yes** | The headline |
| `description` | **yes** | Index card text and meta description |
| `published` | **yes** | `YYYY-MM-DD`. Controls ordering — newest first |
| `audience` | no | `uk`, `us`, `ca`, `au`, `ng`, `intl`. Defaults to `intl`. Shown as a label on the card |
| `dek` | no | Standfirst under the headline |
| `updated` | no | Defaults to `published` |
| `keywords` | no | For search |
| `related` | no | **Guide slugs only** — file names from `content/hub/guides/` without `.md`. A wrong slug breaks the build on purpose |

The build fails loudly if `title`, `description` or `published` is missing, or
if `audience` is not one of the six values. That is deliberate — a broken essay
should never reach the live site quietly.

## The body

Plain markdown below the frontmatter. `##` for section headings, `**bold**`,
tables, lists, and `[links](/writing/)` all work.

Link internally wherever it is honest to — to [/writing/](/writing/) for paid
markets, to a guide, to a country page. Internal links are how a new essay
inherits the site's existing authority.

## After you add one

```bash
python3 scripts/build-writing-hub.py     # or: npm run build
```

Then add the route to `content/index-allowlist.json` under `routes`:

```json
"/essays/your-slug/"
```

**This step is not optional.** A page that is not in the allowlist is not in
the sitemap and is invisible to search engines. The build will emit the page
either way, so nothing warns you.

Then run `npm test` before pushing.

## What belongs here, and what does not

**Essays** make an argument. They have a point of view, a byline, and a date.
"Most magazines won't tell you what they pay" is an essay.

**Guides** (`content/hub/guides/`) answer a question neutrally and get updated
rather than dated. "How to pitch a UK editor" is a guide.

Keeping them apart matters. A reference library that argues is less trustworthy,
and an essay that refuses to take a position is not worth reading.

## What makes an essay worth publishing here

The site's advantage is that it holds verified data nobody else has bothered to
collect. The strongest essays use it:

- Original numbers from the 138 verified records
- Something learned by actually checking, not by aggregating
- A claim you can defend with a source

Avoid general-interest topics with no connection to writing. They will not rank,
because search engines treat sections that are starkly different from a site's
main subject as effectively separate — they inherit none of BRYME's authority.
An essay about writing markets starts with the site behind it. An essay about
anything else starts from zero.
