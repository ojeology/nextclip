#!/usr/bin/env python3
"""BRYME Articles — the content model behind /writers/articles/.

This module is data only: it reads ``content/articles/`` and answers questions
about it. ``build_articles.py`` renders it, and ``sync-writing-allowlist.py``
imports :func:`routes` so a new story reaches the allowlist, the sitemap and the
release gate the moment its markdown file lands — the failure mode this desk has
paid for before is a page that is generated, canonical and robots ``index,follow``
but absent from the allowlist, which is exactly how pages go missing from search.

The publishing rule, stated once so every surface agrees:

  a story is live when it is not a draft AND its ``published`` date is on or
  before the build's publish ceiling.

Nothing else about a story is invented here: no view counts, no "most read"
ordering, no placeholder covers. A category page is only generated when at least
one live story sits in it, and the invitation pop-up renders nothing at all when
no live story exists — the brief's rule is "never a page of empty shelves".

Design note on dates: the ceiling is ``max(SOURCE_DATE_EPOCH, today)``. CI pins
SOURCE_DATE_EPOCH for reproducible rebuilds, but a story dated today must still
go live today, otherwise a scheduled publication silently disappears in a pinned
rebuild. Articles are content, not generated timestamps, so the ceiling never
moves a story forward — only backwards for a story that is genuinely scheduled.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content" / "articles"
CONFIG_PATH = CONTENT_DIR / "index.json"

# Routes are authored in their un-routed form, exactly like every other builder
# in this tree: build-routing.py mounts the whole publication under /writers/.
LANDING_ROUTE = "/articles/"
CATEGORY_ROUTE = "/articles/{slug}/"
ARTICLE_ROUTE = "/articles/{slug}/"

# assets/ is never rewritten by the router, so the one file in assets/ that has
# to link into the section — assets/articles/invitation.json, fetched at runtime
# by the pop-up — must spell the routed form itself. Kept in one place so the
# hard-coded prefix cannot drift away from build-routing.py.
PUBLIC_PREFIX = "/writers/articles/"

MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")

DEFAULT_AUTHOR = "Ibrahim Sodiq"
AUTHOR_ROUTE = "/author/ibrahim-sodiq/"
WORDS_PER_MINUTE = 220
INVITE_LABEL = "A STORY FROM BRYME"
INVITE_STORAGE_KEY = "bryme.articles.invitation"


class ArticleError(SystemExit):
    """A content problem the build must refuse to publish."""


# ---------------------------------------------------------------------------
# Dates and formatting
# ---------------------------------------------------------------------------
def publish_ceiling() -> dt.date:
    """The date a story has to reach before it is shown to a reader."""
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "")
    if epoch.isdigit():
        pinned = dt.datetime.fromtimestamp(int(epoch), dt.timezone.utc).date()
        return max(pinned, dt.date.today())
    return dt.date.today()


def iso_date(value: object, where: str) -> dt.date:
    text = str(value or "").strip()
    try:
        return dt.date.fromisoformat(text[:10])
    except ValueError:
        raise ArticleError(f"{where}: published/updated must be YYYY-MM-DD, got {text!r}")


def human_date(day: dt.date) -> str:
    return f"{day.day} {MONTHS[day.month - 1]} {day.year}"


# ---------------------------------------------------------------------------
# Frontmatter
#
# The essays loader in build-writing-hub.py reads flat ``key: value`` lines. A
# story needs two list shapes that parser cannot express (``related:`` of slugs
# and ``sources:`` of pipe-separated citations), so this reads a small, strict
# subset: ``key: value``, ``key: [a, b]`` and block lists written as
# ``  - item``. Anything else is an error rather than a silently ignored key,
# because a typo in ``teaser`` must not quietly publish a story with no teaser.
# ---------------------------------------------------------------------------
_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
ITEM_RE = re.compile(r"^\s*-\s+(.*)$")
KNOWN_KEYS = {
    "title", "description", "category", "published", "updated", "cover",
    "cover_alt", "cover_caption", "cover_width", "cover_height", "cover_credit",
    "teaser", "reading_minutes", "keywords", "related", "sources", "draft",
    "author", "pull_quote",
}


def parse_frontmatter(text: str, where: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        raise ArticleError(f"{where}: missing frontmatter block (--- ... ---)")
    end = text.find("\n---", 3)
    if end == -1:
        raise ArticleError(f"{where}: frontmatter block is never closed")
    raw = text[3:end]
    body = text[end + 4:].lstrip("\n")
    data: dict = {}
    current_list: str | None = None
    for line in raw.split("\n"):
        if not line.strip():
            continue
        item = ITEM_RE.match(line)
        if item and current_list:
            data[current_list].append(item.group(1).strip().strip("\"'"))
            continue
        m = _KEY_RE.match(line)
        if not m:
            raise ArticleError(f"{where}: cannot read frontmatter line {line!r}")
        key, value = m.group(1).strip(), m.group(2).strip()
        if key not in KNOWN_KEYS:
            raise ArticleError(
                f"{where}: unknown frontmatter key {key!r} "
                f"(known: {', '.join(sorted(KNOWN_KEYS))})")
        current_list = None
        if value == "":
            data[key] = []
            current_list = key
            continue
        value = value.strip().strip("\"'")
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [x.strip().strip("\"'") for x in inner.split(",") if x.strip()] if inner else []
        else:
            data[key] = value
    return data, body


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
def load_config() -> dict:
    if not CONFIG_PATH.is_file():
        raise ArticleError(f"content/articles/index.json is missing")
    cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    cats = cfg.get("categories") or []
    if not cats:
        raise ArticleError("index.json: no categories configured")
    seen = set()
    for cat in cats:
        for key in ("slug", "name", "blurb"):
            if not str(cat.get(key) or "").strip():
                raise ArticleError(f"index.json: category is missing {key}: {cat!r}")
        if cat["slug"] in seen:
            raise ArticleError(f"index.json: duplicate category slug {cat['slug']!r}")
        if not re.fullmatch(r"[a-z0-9-]+", cat["slug"]):
            raise ArticleError(f"index.json: category slug must be lowercase-with-dashes: {cat['slug']!r}")
        seen.add(cat["slug"])
    cfg["categories"] = sorted(cats, key=lambda c: (c.get("order", 99), c["name"]))
    inv = cfg.setdefault("invitation", {})
    inv.setdefault("enabled", True)
    inv.setdefault("delaySeconds", 10)
    inv.setdefault("maxPerSession", 1)
    inv.setdefault("cooldownDays", 7)
    inv.setdefault("article", None)
    if not isinstance(inv["delaySeconds"], int) or not 5 <= inv["delaySeconds"] <= 120:
        raise ArticleError("index.json: invitation.delaySeconds must be an integer between 5 and 120 "
                           "(the brief forbids an immediate pop-up)")
    if not isinstance(inv["cooldownDays"], int) or inv["cooldownDays"] < 0:
        raise ArticleError("index.json: invitation.cooldownDays must be an integer >= 0")
    if not isinstance(inv["maxPerSession"], int) or inv["maxPerSession"] < 1:
        raise ArticleError("index.json: invitation.maxPerSession must be an integer >= 1")
    return cfg


def categories(cfg: dict) -> list[dict]:
    return cfg["categories"]


def category_by_slug(cfg: dict, slug: str) -> dict:
    for cat in cfg["categories"]:
        if cat["slug"] == slug:
            return cat
    raise ArticleError(
        f"index.json: unknown category {slug!r} "
        f"(known: {', '.join(c['slug'] for c in cfg['categories'])})")


# ---------------------------------------------------------------------------
# Stories
# ---------------------------------------------------------------------------
def _word_count(markdown: str) -> int:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", markdown)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#>*_`-]", " ", text)
    return len(re.findall(r"[A-Za-z0-9’']+", text))


def _required(meta: dict, key: str, where: str) -> str:
    value = str(meta.get(key) or "").strip()
    if not value:
        raise ArticleError(f"{where}: missing {key}")
    return value


def _truthy(value: object) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "draft"}


def _parse_sources(meta: dict, where: str) -> list[dict]:
    out = []
    for raw in meta.get("sources") or []:
        parts = [p.strip() for p in str(raw).split("|")]
        if len(parts) < 2 or not parts[1].startswith("http"):
            raise ArticleError(f"{where}: sources entries must read \"Title | https://…\" (got {raw!r})")
        out.append({"title": parts[0], "url": parts[1],
                    "publisher": parts[2] if len(parts) > 2 else ""})
    return out


def _load_one(path: Path, cfg: dict) -> dict:
    where = f"content/articles/{path.name}"
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"), where)
    if not body.strip():
        raise ArticleError(f"{where}: the story has no body")
    slug = path.stem
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ArticleError(f"{where}: filename must be lowercase-with-dashes (it becomes the URL)")
    cat = category_by_slug(cfg, _required(meta, "category", where))
    published = iso_date(_required(meta, "published", where), where)
    updated = iso_date(meta.get("updated") or published, where)
    if updated < published:
        raise ArticleError(f"{where}: updated {updated} is before published {published}")
    cover = _required(meta, "cover", where)
    if not cover.startswith("/assets/"):
        raise ArticleError(f"{where}: cover must be a path under /assets/ (got {cover!r})")
    if not (ROOT / cover.lstrip("/")).is_file():
        raise ArticleError(f"{where}: cover file does not exist: {cover}")
    cover_alt = _required(meta, "cover_alt", where)
    if len(cover_alt) < 12:
        raise ArticleError(f"{where}: cover_alt must describe the image, not repeat the headline")
    teaser = _required(meta, "teaser", where)
    if len(teaser) < 40:
        raise ArticleError(f"{where}: teaser is the invitation's copy — write at least a sentence "
                           f"that makes a reader curious (40+ characters)")
    if len(teaser) > 260:
        raise ArticleError(f"{where}: teaser must stay under 260 characters so the pop-up stays short")
    words = _word_count(body)
    minutes = meta.get("reading_minutes")
    if minutes:
        try:
            minutes = int(str(minutes))
        except ValueError:
            raise ArticleError(f"{where}: reading_minutes must be a whole number")
    else:
        minutes = max(1, round(words / WORDS_PER_MINUTE))
    keywords = meta.get("keywords") or []
    if isinstance(keywords, str):
        keywords = [keywords]
    pull_quote = str(meta.get("pull_quote") or "").strip()
    return {
        "slug": slug,
        "route": ARTICLE_ROUTE.format(slug=slug),
        "title": _required(meta, "title", where),
        "description": _required(meta, "description", where),
        "category": cat,
        "published": published,
        "updated": updated,
        "cover": cover,
        "cover_alt": cover_alt,
        "cover_caption": str(meta.get("cover_caption") or "").strip(),
        "cover_credit": str(meta.get("cover_credit") or "").strip(),
        "cover_width": int(str(meta.get("cover_width") or 1600)),
        "cover_height": int(str(meta.get("cover_height") or 840)),
        "teaser": teaser,
        "pull_quote": pull_quote,
        "reading_minutes": minutes,
        "words": words,
        "keywords": [str(k).strip() for k in keywords if str(k).strip()],
        "related": [str(r).strip() for r in (meta.get("related") or []) if str(r).strip()],
        "sources": _parse_sources(meta, where),
        "author": str(meta.get("author") or DEFAULT_AUTHOR).strip(),
        "draft": _truthy(meta.get("draft")),
        "body": body.strip(),
    }


def load_all(cfg: dict | None = None) -> list[dict]:
    """Every story on disk, drafts included, newest first."""
    cfg = cfg or load_config()
    if not CONTENT_DIR.is_dir():
        return []
    out = []
    for path in sorted(CONTENT_DIR.glob("*.md")):
        if path.stem.lower() in {"readme", "template", "_template"}:
            continue
        out.append(_load_one(path, cfg))
    slugs = {a["slug"] for a in out}
    if len(slugs) != len(out):
        raise ArticleError("content/articles: two stories share a filename")
    for a in out:
        for rel in a["related"]:
            if rel not in slugs:
                raise ArticleError(f"content/articles/{a['slug']}.md: related story {rel!r} does not exist")
            if rel == a["slug"]:
                raise ArticleError(f"content/articles/{a['slug']}.md: a story cannot relate to itself")
    out.sort(key=lambda a: (a["published"], a["slug"]), reverse=True)
    return out


def load_published(cfg: dict | None = None, ceiling: dt.date | None = None) -> list[dict]:
    """Live stories only: not drafts, and published on or before the ceiling."""
    ceiling = ceiling or publish_ceiling()
    return [a for a in load_all(cfg) if not a["draft"] and a["published"] <= ceiling]


# ---------------------------------------------------------------------------
# Derived views
# ---------------------------------------------------------------------------
def categories_in_use(cfg: dict, articles: list[dict]) -> list[dict]:
    """Configured categories that at least one live story sits in."""
    live = {a["category"]["slug"] for a in articles}
    return [c for c in cfg["categories"] if c["slug"] in live]


def in_category(articles: list[dict], slug: str) -> list[dict]:
    return [a for a in articles if a["category"]["slug"] == slug]


def featured(cfg: dict, articles: list[dict]) -> dict | None:
    """The one story promoted in the hero slot.

    ``featured`` in index.json wins when it names a live story; an editor can
    pin a specific piece. When it is null (the default) the newest live story
    takes the slot, so the section never needs a story hard-coded into code.
    """
    want = cfg.get("featured")
    if want:
        for a in articles:
            if a["slug"] == want:
                return a
        raise ArticleError(
            f"index.json: featured story {want!r} is not a live story "
            f"(live: {', '.join(a['slug'] for a in articles) or 'none'})")
    return articles[0] if articles else None


def invitation_article(cfg: dict, articles: list[dict]) -> dict | None:
    """The story the pop-up offers.

    ``invitation.article`` pins it; otherwise the featured story is used, which
    keeps the pop-up and the hero in agreement. Any live story works, so the
    pop-up keeps running after the first story as the section fills up.
    """
    pinned = cfg["invitation"].get("article")
    if pinned:
        for a in articles:
            if a["slug"] == pinned:
                return a
        raise ArticleError(
            f"index.json: invitation.article {pinned!r} is not a live story "
            f"(live: {', '.join(a['slug'] for a in articles) or 'none'})")
    return featured(cfg, articles)


def related_articles(article: dict, articles: list[dict], limit: int = 3) -> list[dict]:
    """Up to ``limit`` stories to offer at the end of this one.

    Order of preference, as the brief specifies: the editor's own ``related``
    list, then the same category, then the newest live stories from anywhere.
    Nothing is ever suggested twice and the story itself never appears.
    """
    by_slug = {a["slug"]: a for a in articles}
    picked: list[dict] = []
    for slug in article.get("related") or []:
        a = by_slug.get(slug)
        if a and a["slug"] != article["slug"] and a not in picked:
            picked.append(a)
    for a in in_category(articles, article["category"]["slug"]):
        if len(picked) >= limit:
            break
        if a["slug"] != article["slug"] and a not in picked:
            picked.append(a)
    for a in articles:
        if len(picked) >= limit:
            break
        if a["slug"] != article["slug"] and a not in picked:
            picked.append(a)
    return picked[:limit]


def most_read(cfg: dict, articles: list[dict], limit: int = 3) -> list[dict]:
    """Curated "most read" — only ever what an editor has measured.

    The brief forbids invented popularity. There is no analytics read here, so
    this returns an empty list until ``mostRead`` in index.json names real
    stories in a real order; the landing page then renders no such block at all
    rather than a shelf built on a guess.
    """
    order = cfg.get("mostRead") or []
    by_slug = {a["slug"]: a for a in articles}
    out = [by_slug[s] for s in order if s in by_slug]
    for slug in order:
        if slug not in by_slug:
            raise ArticleError(f"index.json: mostRead names {slug!r}, which is not a live story")
    return out[:limit]


def routes(cfg: dict | None = None, ceiling: dt.date | None = None) -> set[str]:
    """Every indexable route the section generates right now."""
    cfg = cfg or load_config()
    articles = load_published(cfg, ceiling)
    out = {LANDING_ROUTE}
    out |= {a["route"] for a in articles}
    out |= {CATEGORY_ROUTE.format(slug=c["slug"]) for c in categories_in_use(cfg, articles)}
    return out


# ---------------------------------------------------------------------------
# The invitation payload consumed by assets/articles.js
# ---------------------------------------------------------------------------
def public_url(route: str) -> str:
    """Routed, same-origin URL for a route authored in un-routed form.

    Root-relative rather than absolute on purpose: the payload is fetched by the
    browser that is already on the page, so a relative URL keeps the invitation
    inside whatever host the reader is on (production, a preview, a staging
    copy) instead of hard-coding thebryme.com into a file that ships everywhere.
    """
    return PUBLIC_PREFIX + route[len(LANDING_ROUTE):]


def invitation_payload(cfg: dict, articles: list[dict]) -> dict:
    """What assets/articles.js fetches once, when it decides to show the pop-up.

    ``article`` is None when nothing is live: the script then renders nothing,
    removes its timer and never asks again this session. The payload carries the
    behaviour too (delay, cooldown, cap) so the rules live in one reviewable
    place instead of being split between JSON and JavaScript.
    """
    inv = cfg["invitation"]
    article = invitation_article(cfg, articles) if inv["enabled"] else None
    payload = {
        "enabled": bool(inv["enabled"]) and article is not None,
        "delaySeconds": inv["delaySeconds"],
        "maxPerSession": inv["maxPerSession"],
        "cooldownDays": inv["cooldownDays"],
        "storageKey": INVITE_STORAGE_KEY,
        "dismissLabel": "Maybe later",
        "ctaLabel": "Read the Full Story",
        "asideLabel": "Read later — the full story is one tap away, and nothing here blocks the page.",
        "article": None,
    }
    if article:
        payload["article"] = {
            "label": INVITE_LABEL,
            "category": article["category"]["name"],
            "headline": article["title"],
            "teaser": article["teaser"],
            "url": public_url(article["route"]),
            "cover": article["cover"],
            "coverAlt": article["cover_alt"],
            "coverWidth": article["cover_width"],
            "coverHeight": article["cover_height"],
            "readingMinutes": article["reading_minutes"],
            "published": article["published"].isoformat(),
            "publishedLabel": human_date(article["published"]),
        }
    return payload
