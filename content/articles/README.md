# BRYME Articles — how to publish a story

This directory is the whole editorial system for `/writers/articles/`. A story is
one markdown file here; everything else (the landing page, the category pages, the
sitemap, the invitation pop-up) is generated from whatever is in this folder.

Nothing publishes by accident:

* a file appears on the site only when its `published` date has arrived **and** it
  is not marked `draft`;
* a category page exists only while a live story sits in that category;
* the invitation pop-up renders nothing at all when no story is live.

## Adding a story

1. **Write the file.** Copy the template below to `content/articles/<slug>.md`.
   The filename becomes the URL, so use lowercase-with-dashes:
   `life-of-a-gambler.md` → `/writers/articles/life-of-a-gambler/`.
2. **Put the cover in `assets/articles/covers/`.** 1600×840 (16:9), JPEG, progressive,
   under ~250 KB. Covers are used three times: the card, the story header and the
   social card. `cover_alt` must describe the picture, not repeat the headline —
   the build rejects alt text shorter than a dozen characters.
3. **Fill in the frontmatter.** Every field below is required unless marked optional;
   the build stops with a message naming the file and the field it is missing.
4. **Build.** `npm run build` (then `python3 scripts/sync-writing-allowlist.py` if you
   added the first story in a category — see "Routes" below).
5. **Check it.** `npm test`. It runs the release gate: allowlist, sitemap, canonical,
   one-H1, alt text, schema, ads, links, contrast and the browser pass.

```markdown
---
title: The headline as it appears on the page and in the browser tab
description: One sentence. Used as the standfirst, the card excerpt and the meta description.
category: lives-and-lifestyles
published: 2026-11-25
updated: 2026-11-25
cover: /assets/articles/covers/life-of-a-gambler.jpg
cover_alt: A description of what is actually in the photograph
cover_caption: Optional caption printed under the photograph.
cover_credit: Photo: Name / Agency
cover_width: 1600
cover_height: 840
teaser: One curious sentence used by the invitation pop-up — never the standfirst again.
keywords: gambling, risk, nigeria
reading_minutes: 12
related: [another-story-slug]
sources:
  - Title of the source | https://example.com/the-source | Publisher
draft: false
---

Opening paragraphs. No heading here — the headline is already the H1.

## A subhead

Body copy. **Bold**, *italic*, [links](/learn/) and lists all work.

> A pull quote sits on its own line, starting with a greater-than sign.

![Alt text describing the image](/assets/articles/covers/inline-image.jpg "Optional caption under this image.")

- A list item
- Another list item

## Another subhead

More copy.
```

### What the renderer supports

| Markdown | Renders as |
| --- | --- |
| `## Heading` | section subhead (H2) |
| `### Heading` | sub-subhead (H3) |
| `> quoted line` | pull quote |
| `- item` / `1. item` | bulleted / numbered list |
| `![alt](src "caption")` | figure with a caption, lazy-loaded |
| `---` | section rule |
| `**bold**`, `*italic*`, `[text](url)` | inline formatting |

Images inside the body are lazy-loaded and **must** have alt text — a missing
alt is a build error, not a warning. Everything is plain HTML after rendering: no
scripts, no embeds, no third-party widgets.

## The category system

Categories live in `index.json`, not in the story files, so the section's structure
is one reviewable list:

| Slug | Name |
| --- | --- |
| `living-in-africa` | Living in Africa |
| `lives-and-lifestyles` | Lives and Lifestyles |
| `money-and-ambition` | Money and Ambition |
| `human-behaviour` | Human Behaviour |
| `unusual-jobs-and-hidden-worlds` | Unusual Jobs and Hidden Worlds |

Adding a category is a new entry in `categories`; the landing page lists it as
"Opening soon" until a story is published into it, and only then does its page
exist. Removing a category with live stories is a build error, by design.

## Choosing the featured story

`featured` in `index.json`:

* `null` (the default) → **the newest live story** takes the hero slot. Nothing is
  hard-coded, so the section keeps working as stories are added.
* `"some-slug"` → that story is pinned to the hero until you change it. If the slug
  is not a live story the build fails rather than quietly falling back.

The invitation pop-up follows the featured story unless `invitation.article` names
a different one. Either way it is a *live* story with its own teaser, cover and URL —
never the same text for every story, and never a story that has not been published.

## Choosing the teaser

`teaser` is the only copy in the invitation card, and it is the reason the card
works or does not. Rules that keep it honest:

* one or two sentences, 40–260 characters (the build enforces the range);
* it has to make a reader curious, not summarise the piece — the invitation offers
  a story, it does not replace it;
* it must be specific to *this* story. A teaser that could sit above any article is
  a teaser that sells nothing.

## The invitation pop-up

Behaviour is configuration, in `invitation`:

```json
{ "enabled": true, "delaySeconds": 10, "article": null, "maxPerSession": 1, "cooldownDays": 7 }
```

* `delaySeconds` — how long after landing it may appear. Validation refuses anything
  under 5 seconds, because the brief forbids an immediate pop-up.
* `maxPerSession` — how many times one browser session can see it (1 by default).
* `cooldownDays` — how long after a dismissal a returning visitor is left alone.
* `article` — pin a specific story, or leave `null` to follow the featured story.
* `enabled: false` — switches the card off entirely (the analytics stay).

Implementation: `assets/articles.js` (no dependencies), payload generated at build
time into `assets/articles/invitation.json`, styling in `assets/articles.css`.
The card never opens a window, never blocks scrolling or navigation, waits if the
reader is typing in search or has the menu open, and gives up rather than
interrupting. See `docs/BRYME-ARTICLES.md` for the full behaviour table.

## Routes

| URL | When it exists |
| --- | --- |
| `/writers/articles/` | always |
| `/writers/articles/<category>/` | while at least one live story is in the category |
| `/writers/articles/<story>/` | while the story is live |

Routes are decided by `scripts/articles_content.py` and picked up by
`scripts/sync-writing-allowlist.py`, which is what puts them in the sitemap and in
the release gate's index allowlist. Run it after adding the first story in a new
category — `npm run verify:allowlist` tells you if it is out of date.

## Deleting or unpublishing a story

Delete the markdown file, run `sync-writing-allowlist.py` (it prunes article
routes, which are derived from disk), then `npm run build`. The page, its sitemap
entry and any invitation pointing at it disappear together. To keep the file but
take the story down, set `draft: true` — the same thing happens, reversibly.

## What never happens

* No invented headlines, covers, view counts or "most read" ordering. `mostRead`
  stays empty until measured reads exist; the block is not rendered while it is.
* No empty category pages, no placeholder stories, no scheduled story shown early.
* No second analytics platform: events go to the site's existing GA4 property
  (`articles_landing_view`, `articles_article_view`, `articles_invite_impression`,
  `articles_invite_click`, `articles_invite_dismiss`, `articles_related_click`,
  `articles_nav_click`, `articles_story_click`, `articles_desk_home_view`).
