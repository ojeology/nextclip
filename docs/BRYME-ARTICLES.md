# BRYME Articles — how the section works

BRYME Articles is the editorial section of the Writers publication, mounted at
`/writers/articles/`. It is not a second publication: it uses the same shell, the
same navigation, the same analytics property and the same release gates as the rest
of the desk, and it lives inside `/writers/` because that is where this desk's pages
live.

Publishing a story is documented in [`content/articles/README.md`](../content/articles/README.md).
This file is the implementation record: what exists, why it is built this way, and
what each part refuses to do.

## Files

| Path | Role |
| --- | --- |
| `content/articles/index.json` | Section config: the five categories, the featured slot, the invitation's behaviour |
| `content/articles/*.md` | One story per file — frontmatter + markdown |
| `scripts/articles_content.py` | The content model: loads, validates, decides what is live, derives routes |
| `scripts/build-articles.py` | Renders the landing page, category pages, story pages, the desk ribbon and the invitation payload |
| `assets/articles.css` | Section styling, namespaced `.ba-*`, built on the existing design tokens |
| `assets/articles.js` | The invitation pop-up and the section's analytics — no dependencies, no build step |
| `assets/articles/invitation.json` | Generated at build time; the only file the pop-up fetches |

Touched to wire it in (each change is small and additive):

| File | Change |
| --- | --- |
| `scripts/build-writing-first.py` | `nav()` gains a "BRYME Articles" item after the desk name; `drawer()` gains it under "Start here"; `mobile_nav()` maps the section to the "Articles" tab; `page_wf()` gains four optional arguments (`og_type`, `og_image`, `og_image_w/h`, `body_scripts`) |
| `scripts/build-writing-hub.py` | the desk home gets the ribbon band, `articles.css` and `articles.js` |
| `scripts/sync-writing-allowlist.py` | article routes enter the index allowlist (and leave it again when a story is deleted) |
| `scripts/validate-site-quality.js` | `/articles/` is no longer treated as a retired media family |
| `assets/bryme-v2.css` | the nav item's marker (propagates into `content-v2.css` via `build-content-css.py`) |
| `content/hub/trust-pages.json` | the privacy policy's browser-storage section now names the invitation's two values |

## Routes

| Route | Exists when |
| --- | --- |
| `/writers/articles/` | always |
| `/writers/articles/<category>/` | at least one live story in that category |
| `/writers/articles/<story>/` | the story is live |

"Live" means: not `draft: true` **and** `published` is on or before the build's
publish ceiling. The ceiling is `max(SOURCE_DATE_EPOCH, today)` so CI's pinned
rebuilds stay reproducible while a story dated today still publishes today.

There is no sixth category page and no `?page=` variant: the section is a finite
index, and a category with one story is a page with one story rather than a
pagination shell. Routes are derived from disk, never typed, so the allowlist, the
sitemap, the release gate and the pages themselves cannot disagree.

## The story template

One template, generated from frontmatter, at a permanent URL:

* breadcrumb (Home / BRYME Articles / Category / Story), category kicker, H1, standfirst;
* byline with the publication date and a computed reading time (220 wpm, overridable);
* cover figure with optional caption and credit, `loading="eager"` + `fetchpriority="high"`;
* rich body: H2/H3 subheads, paragraphs, bulleted and numbered lists, figures with
  captions (lazy-loaded), pull quotes, rules, inline links, bold/italic;
* optional "Sources and further reading" list;
* "Filed under", revision date when the story has been updated, correction link;
* "There's More to Discover" — up to three stories: the editor's `related` list
  first, then the same category, then the newest live stories.

Heading hierarchy is exactly one H1 and ordered H2/H3 below it. Every image carries
alt text; a body image without alt fails the build.

## The small recommendation component

`recommendation()` in `build-articles.py` is the compact unit: one cover thumbnail,
one headline, category and reading time. It is reused mid-article (inserted after the
second H2 on stories over 900 words), in the landing page's "Recommended reading"
strip, and on category pages. Same markup everywhere, so a change lands everywhere.

## The editorial invitation

Trigger: 10 s after a reader lands on `/writers/` or `/writers/articles/`
(`delaySeconds` in `content/articles/index.json`, validated to be ≥ 5 s so it can
never be immediate). It offers one eligible story — the pinned
`invitation.article`, else the featured story, else the newest live one — with its own
cover, teaser and URL.

| Rule | How it is enforced |
| --- | --- |
| Never immediate | `delaySeconds` floor of 5 in `articles_content.load_config()` |
| Once per session | `sessionStorage` counter against `maxPerSession` |
| Configurable cooldown for repeat visits | `localStorage` timestamp against `cooldownDays` |
| Nothing when no story is live | `invitation_payload()` emits `enabled: false` and `article: null`; `articles.js` then installs no timer at all |
| Never blocks reading or navigation | No backdrop, no `aria-modal`, no focus trap, no scroll lock; `position: fixed`, so zero layout shift |
| Does not interrupt active use | Postpones 12 s (up to three times) if the tab is hidden, the menu drawer is open, another dialog is up, or the cursor is in a search box; then gives up silently |
| Obvious dismissal | An "×" button on the image and a "Maybe later" text button, plus Escape when focus is inside the card |
| No new window | The CTA is a plain same-tab link |
| Not an advertisement | No ad styling, no countdown, no second ask; it looks like the publication and sits where a reading suggestion would |
| Not hard-coded to one story | The story, its teaser and its cover all come from frontmatter and config |

Measured in a headless browser: appears at 10 s, 0.0000 layout shift attributable to
the card, absent on a second visit in the same session, absent on a return visit
inside the cooldown, absent on story pages, and the page underneath stays clickable
while it is open.

## SEO

* Unique `<title>` and description per page, both inside the 60-character budget.
* Self-referential canonical on every route; no duplicate URL variants.
* `BlogPosting` with `@id`, `datePublished`, `dateModified`, visible `author`,
  `publisher`, `image`, `articleSection`, `keywords`, `wordCount`, `timeRequired`,
  plus `BreadcrumbList`; `CollectionPage` + `ItemList` on the landing and category pages.
* `og:type=article`, `article:published_time` / `modified_time` / `section` / `author`,
  and the story's own cover as the social card at its real dimensions.
* Every published route reaches `/writers/sitemap.xml` through the allowlist; drafts
  and future-dated stories reach neither the sitemap nor the allowlist.
* The section is reachable from every page of the site through the primary nav, and
  from the desk home through the ribbon — no page is an orphan.

## Analytics

All events go to the site's existing GA4 property. Nothing else is added.

| Event | When |
| --- | --- |
| `articles_desk_home_view` | `/writers/` visit (the top of the funnel) |
| `articles_landing_view` | `/writers/articles/` visit |
| `articles_article_view` | story view, with slug, category, reading time, `returning`, `articles_this_session` |
| `articles_nav_click` / `articles_story_click` | any link into the section, with the surface that carried it |
| `articles_related_click` | a click in "There's More to Discover" or the recommendation unit |
| `articles_invite_impression` / `_click` / `_dismiss` | the invitation, the dismissal carrying `reason` (`close`, `maybe-later`, `escape`) |

`returning` is a boolean derived from a first-seen timestamp; `articles_this_session`
counts story views in the session, which is the "articles per session" measure. No
reading history, no identifiers and no third-party analytics are involved.

## Performance and advertising

No new JavaScript libraries, no web fonts, no animation beyond one 220 ms fade on the
invitation. Every image slot declares intrinsic dimensions or an aspect ratio, so
covers cannot shift the page while they load; body images below the fold are lazy.
The ad bands come from the existing injector and are labelled "ADVERTISEMENT"; none is
placed inside the story header, the breadcrumb or the primary navigation, and the
invitation is deliberately not an ad slot.

## What is deliberately absent

* No story content. The section ships empty and says so on the landing page.
* No "most read" block. `mostRead` is empty, so the block is not rendered rather than
  ordered by a guess.
* No empty category pages, no placeholder headlines, no invented readership figures.
* No sixth publication, and no changes to writing opportunities, publication profiles,
  submissions, the homepage design or the Writers identity.
