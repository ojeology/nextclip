#!/usr/bin/env python3
"""Build BRYME Articles — the editorial section of the Writers publication.

Routes generated (un-routed form; build-routing.py mounts them under /writers/):

  /articles/                 the section landing page
  /articles/<category>/      one page per category that has a live story
  /articles/<story>/         the reusable story template

Plus one file outside the page tree: assets/articles/invitation.json, the
payload the pop-up fetches. assets/ is never rewritten by the router, so that
payload carries the routed URLs itself (see articles_content.PUBLIC_PREFIX).

What this builder refuses to do, because the brief does:
  * publish a draft, or a story dated in the future;
  * invent a headline, a cover, a view count or a "most read" order;
  * generate an empty category page;
  * render an invitation when no story is live.

Everything else — categories, which story is featured, the invitation's delay and
cooldown — is configuration in content/articles/index.json, so the section can be
run by an editor without touching Python.
"""
from __future__ import annotations

import html as _html
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import articles_content as ac  # noqa: E402

# Reuse the writing-first shell (page_wf, esc, write, BASE, nav, mobile_nav) so
# head/canonical/OG/schema and the primary navigation stay identical to the rest
# of the publication. Same import dance as build-writing-hub.py: the filename
# has dashes, so it cannot be imported by name.
_spec = importlib.util.spec_from_file_location(
    "build_writing_first", str(ROOT / "scripts" / "build-writing-first.py"))
_bwf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bwf)

esc = _bwf.esc
write = _bwf.write
BASE = _bwf.BASE
page_wf = _bwf.page_wf

STYLESHEET = "/assets/articles.css"
SCRIPT = "/assets/articles.js"
ORG = {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}
AUTHOR = {"@type": "Person", "name": ac.DEFAULT_AUTHOR, "url": BASE + ac.AUTHOR_ROUTE}


# ---------------------------------------------------------------------------
# Markdown → HTML
#
# The essays renderer in build-writing-hub.py handles paragraphs, headings,
# bold and links. A story needs figures with captions, pull quotes, ordered and
# unordered lists and a source list, so this is the smallest renderer that
# covers the brief's "rich text" requirement — and it validates as it goes: an
# image without alt text is a build failure, not a silent accessibility hole.
# ---------------------------------------------------------------------------
IMAGE_RE = re.compile(r'^!\[(.*?)\]\((\S+?)(?:\s+"(.*?)")?\)$')
ORDERED_RE = re.compile(r"^\d+\.\s+")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def inline(text: str) -> str:
    out = _html.escape(text, quote=False)
    out = LINK_RE.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def _is_block_start(line: str) -> bool:
    s = line.strip()
    return bool(
        s.startswith(("## ", "### ", "> ", "- ", "* "))
        or ORDERED_RE.match(s)
        or IMAGE_RE.match(s)
        or s == "---"
    )


def render_markdown(markdown: str, where: str = "story") -> str:
    lines = markdown.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        s = raw.strip()
        if not s:
            i += 1
            continue
        if s.startswith("### "):
            out.append(f"<h3>{inline(s[4:])}</h3>")
            i += 1
            continue
        if s.startswith("## "):
            out.append(f"<h2>{inline(s[3:])}</h2>")
            i += 1
            continue
        if s == "---":
            out.append('<hr class="ba-rule">')
            i += 1
            continue
        m = IMAGE_RE.match(s)
        if m:
            alt, src, caption = m.group(1).strip(), m.group(2), (m.group(3) or "").strip()
            if len(alt) < 4:
                raise ac.ArticleError(f"{where}: every image needs descriptive alt text ({src})")
            cap = f"<figcaption>{inline(caption)}</figcaption>" if caption else ""
            out.append(
                f'<figure class="ba-figure"><img src="{esc(src)}" alt="{esc(alt)}" '
                f'width="1600" height="900" loading="lazy" decoding="async">{cap}</figure>')
            i += 1
            continue
        if s.startswith("> "):
            quoted = []
            while i < n and lines[i].strip().startswith("> "):
                quoted.append(lines[i].strip()[2:].strip())
                i += 1
            out.append('<blockquote class="ba-pullquote"><p>'
                       + inline(" ".join(quoted)) + "</p></blockquote>")
            continue
        if s.startswith(("- ", "* ")):
            items = []
            while i < n and lines[i].strip().startswith(("- ", "* ")):
                items.append(lines[i].strip()[2:].strip())
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        if ORDERED_RE.match(s):
            items = []
            while i < n and ORDERED_RE.match(lines[i].strip()):
                items.append(ORDERED_RE.sub("", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue
        para = [s]
        i += 1
        while i < n and lines[i].strip() and not _is_block_start(lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(para)) + "</p>")
    return "\n".join(out)


def split_sections(markup: str) -> list[str]:
    """Split rendered body HTML at its top-level H2 boundaries."""
    parts = re.split(r"(?=<h2>)", markup)
    return [p for p in parts if p.strip()]


def insert_mid_recommendation(markup: str, block: str) -> str:
    """Place the compact recommendation after the second H2, when there is one.

    Mid-article placement is where a reader is most likely to want a second
    story; a story with only one or two sections keeps the block at the end
    instead of being chopped in half by it.
    """
    if not block:
        return markup
    parts = split_sections(markup)
    if len(parts) < 3:
        return markup
    return "".join(parts[:2]) + block + "".join(parts[2:])


# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------
def crumbs(trail: list[tuple[str, str]]) -> str:
    inner = ['<a href="/">Home</a>']
    for label, href in trail:
        inner.append(f'<a href="{esc(href)}">{esc(label)}</a>' if href else f"<span>{esc(label)}</span>")
    # Exactly the house markup: the brand audit matches `<nav class="breadcrumb">`
    # so a decorated variant here would read as a section that skipped it.
    return '<nav class="breadcrumb">' + " / ".join(inner) + "</nav>"


def meta_line(article: dict, *, include_date: bool = True) -> str:
    bits = []
    if include_date:
        bits.append(f'<time datetime="{article["published"].isoformat()}">'
                    f'{esc(ac.human_date(article["published"]))}</time>')
    bits.append(f'{article["reading_minutes"]} min read')
    return '<p class="ba-meta">' + "<span aria-hidden=\"true\">·</span>".join(bits) + "</p>"


def card(article: dict, *, eager: bool = False) -> str:
    """The one article card used on every surface: cover, title, excerpt,
    category, reading time, date, link. Mobile-safe by construction: a single
    column on narrow screens, a 16:9 cover with intrinsic dimensions so nothing
    jumps while it loads."""
    load = 'loading="eager"' if eager else 'loading="lazy"'
    return f'''<article class="ba-card">
  <a class="ba-card-media" href="{esc(article["route"])}" tabindex="-1">
    <img src="{esc(article["cover"])}" alt="{esc(article["cover_alt"])}" width="{article["cover_width"]}" height="{article["cover_height"]}" {load} decoding="async">
  </a>
  <p class="ba-card-cat"><a href="{esc(ac.CATEGORY_ROUTE.format(slug=article["category"]["slug"]))}">{esc(article["category"]["name"])}</a></p>
  <h3 class="ba-card-title"><a href="{esc(article["route"])}">{esc(article["title"])}</a></h3>
  <p class="ba-card-excerpt">{esc(article["description"])}</p>
  {meta_line(article)}
</article>'''


def recommendation(article: dict, heading: str = "Also worth your time") -> str:
    """The small, reusable recommendation unit.

    Used mid-article, on category pages and in the landing page's discovery rail.
    One story, one line of context, one link — sized to sit inside a column
    without competing with the piece the reader is already in.
    """
    return f'''<aside class="ba-reco" aria-label="{esc(heading)}">
  <p class="ba-reco-head">{esc(heading)}</p>
  <a class="ba-reco-link" href="{esc(article["route"])}">
    <img src="{esc(article["cover"])}" alt="{esc(article["cover_alt"])}" width="{article["cover_width"]}" height="{article["cover_height"]}" loading="lazy" decoding="async">
    <span class="ba-reco-text"><b>{esc(article["title"])}</b>
    <span>{esc(article["category"]["name"])} · {article["reading_minutes"]} min read</span></span>
  </a>
</aside>'''


def discovery_block(article: dict, articles: list[dict]) -> str:
    """"There's More to Discover" — up to three stories at the end of a piece."""
    picks = ac.related_articles(article, articles, 3)
    if not picks:
        return ""
    cards = "".join(card(p) for p in picks)
    return f'''<section class="section ba-discover" aria-labelledby="ba-discover-title">
  <div class="section-head"><div><p class="eyebrow">Keep reading</p>
  <h2 id="ba-discover-title">There&rsquo;s More to Discover</h2></div></div>
  <div class="ba-grid">{cards}</div>
</section>'''


def ad_slot() -> str:
    """Where the section's first ad unit goes.

    scripts/inject-ads.py appends the configured band after the marker, so the
    mark survives a rebuild and the band is stripped and re-inserted rather than
    stacked. The slot exists because the section, not the injector, knows where
    an ad can sit without wrecking the page: below the lead story, not above the
    masthead, which is where the generic top-of-<main> rule put it and where it
    shoved the headline down every time a creative arrived.
    """
    return '<div class="ba-adslot"><!--ba-ad--></div>'


def head_extra_for(article: dict | None = None) -> str:
    # Order matters, and this is the order the browser sees: page_wf() puts the
    # house sheet after head_extra, so everything here is EARLIER in the cascade
    # than bryme-v2.css. A section rule that must beat a house rule of equal
    # specificity therefore needs one extra qualifier (see .section.ba-shelf in
    # assets/articles.css) - do not "fix" it by moving this link.
    bits = [f'<link rel="stylesheet" href="{STYLESHEET}">']
    if article:
        bits.append(
            f'<meta property="article:published_time" content="{article["published"].isoformat()}">'
            f'<meta property="article:modified_time" content="{article["updated"].isoformat()}">'
            f'<meta property="article:section" content="{esc(article["category"]["name"])}">'
            f'<meta property="article:author" content="{esc(article["author"])}">')
    return "".join(bits)


def schema_for(article: dict) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "@id": BASE + article["route"] + "#article",
        "headline": article["title"],
        "description": article["description"],
        "url": BASE + article["route"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": BASE + article["route"]},
        "datePublished": article["published"].isoformat() + "T09:00:00+01:00",
        "dateModified": article["updated"].isoformat() + "T09:00:00+01:00",
        "author": AUTHOR,
        "publisher": ORG,
        "image": [BASE + article["cover"]],
        "articleSection": article["category"]["name"],
        "keywords": ", ".join(article["keywords"]),
        "wordCount": article["words"],
        "timeRequired": f"PT{article['reading_minutes']}M",
        "inLanguage": "en-NG",
        "isPartOf": {"@type": "CollectionPage", "name": ac.INVITE_LABEL.split(" FROM ")[0].title() + " Articles",
                     "url": BASE + ac.LANDING_ROUTE},
    }


def breadcrumb_schema(trail: list[tuple[str, str]]) -> dict:
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}]
    pos = 2
    for label, href in trail:
        entry = {"@type": "ListItem", "position": pos, "name": label}
        if href:
            entry["item"] = BASE + href
        items.append(entry)
        pos += 1
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


# ---------------------------------------------------------------------------
# Landing page
# ---------------------------------------------------------------------------
def lead_block(article: dict) -> str:
    """The lead story: the front page's first decision.

    Set as a newspaper lead rather than a boxed card - a rule over the block, a
    wide picture, the headline at display size and nothing else competing with
    it. The previous version wrapped the same content in a bordered, shadowed
    panel that started below the fold, which is the one thing a landing page
    cannot afford.
    """
    return f'''<section class="ba-lead" aria-labelledby="ba-lead-title">
  <p class="ba-band-label"><span>The lead story</span></p>
  <article class="ba-lead-card">
    <a class="ba-lead-media" href="{esc(article["route"])}" tabindex="-1">
      <img src="{esc(article["cover"])}" alt="{esc(article["cover_alt"])}" width="{article["cover_width"]}" height="{article["cover_height"]}" loading="eager" fetchpriority="high" decoding="async">
    </a>
    <div class="ba-lead-body">
      <p class="ba-lead-cat"><a href="{esc(ac.CATEGORY_ROUTE.format(slug=article["category"]["slug"]))}">{esc(article["category"]["name"])}</a></p>
      <h2 class="ba-lead-title" id="ba-lead-title"><a href="{esc(article["route"])}">{esc(article["title"])}</a></h2>
      <p class="ba-lead-dek">{esc(article["description"])}</p>
      {meta_line(article)}
      <p class="ba-lead-cta"><a class="ba-link-cta" href="{esc(article["route"])}">Read the story<span aria-hidden="true"> &rarr;</span></a></p>
    </div>
  </article>
</section>'''


def empty_state(cfg: dict) -> str:
    """What the landing page says before the first story is published.

    No placeholder headline, no invented numbers, no link that leads nowhere:
    a plain statement of what the section is, what it is waiting for, and where
    the reader can go in the meantime.
    """
    return f'''<section class="section ba-empty" aria-labelledby="ba-empty-title">
  <div class="ba-empty-card">
    <p class="eyebrow">In preparation</p>
    <h2 id="ba-empty-title">The first stories are being reported, not padded.</h2>
    <p>This section is built and waiting for its first story. When that story is published it
    takes the featured slot above — dated, edited and fact-checked like everything else on this
    desk — and this notice disappears. Until then this page carries no placeholder headlines, no
    invented readership figures and no empty category pages.</p>
    <p>The first piece in the queue is <b>The Life of a Gambler</b>. It will be linked here the day
    it is ready; nothing on BRYME publishes early to fill a space.</p>
    <div class="actions">
      <a class="btn secondary" href="/writing/">Browse paid writing opportunities &rarr;</a>
      <a class="btn secondary" href="/learn/">Read the how-to guides</a>
    </div>
  </div>
</section>'''


def masthead(cfg: dict, articles: list[dict], *, title: str, kicker: str,
             standfirst: str) -> str:
    """The section's own masthead.

    One heading, one standfirst, one line of facts. The old header said "BRYME
    Articles" three times (breadcrumb, kicker, h1) over two paragraphs and a rule,
    which pushed the first story 700px down the page. Facts are computed from the
    live story list, never typed.
    """
    live = ac.categories_in_use(cfg, articles)
    beats = "".join(
        f'<a class="ba-beat-chip is-live" href="{esc(ac.CATEGORY_ROUTE.format(slug=c["slug"]))}">'
        f'{esc(c["name"])}</a>' for c in live)
    chips = (f'<nav class="ba-beats" aria-label="Beats in this section">'
             f'<a class="ba-beat-chip is-all" href="{ac.LANDING_ROUTE}">All stories</a>{beats}</nav>'
             if live else "")
    facts = []
    n = len(articles)
    if n:
        facts.append(f'<span><b>{n}</b> {"story" if n == 1 else "stories"}</span>')
    if len(live) == 1:
        facts.append('<span><b>1</b> beat open</span>')
    elif live:
        facts.append(f'<span><b>{len(live)}</b> beats</span>')
    facts.append('<span>Published when a story is ready</span>')
    facts_html = '<p class="ba-mast-facts">' + "".join(facts) + "</p>"
    return f'''<header class="ba-mast">
  <p class="ba-mast-kicker">{esc(kicker)}</p>
  <h1 class="ba-mast-title">{esc(title)}</h1>
  <div class="ba-mast-cols">
    <p class="ba-mast-dek">{esc(standfirst)}</p>
    <div class="ba-mast-side">{facts_html}{chips}</div>
  </div>
</header>'''


def category_map(cfg: dict, articles: list[dict]) -> str:
    """The five beats, as tiles rather than a five-row table.

    Each tile states the beat, what it covers and whether it is open. Closed
    beats are not links - a tile that looks pressable and goes nowhere is worse
    than one that says "opening soon" in muted ink.
    """
    tiles = []
    for cat in cfg["categories"]:
        n = len(ac.in_category(articles, cat["slug"]))
        if n:
            head = f'<a href="{esc(ac.CATEGORY_ROUTE.format(slug=cat["slug"]))}">{esc(cat["name"])}</a>'
            state = f'is-live'
            note = f'{n} {"story" if n == 1 else "stories"}'
        else:
            head = f"<span>{esc(cat['name'])}</span>"
            state = "is-soon"
            note = "Opening soon"
        tiles.append(f'''<li class="ba-beat {state}">
      <p class="ba-beat-name">{head}</p>
      <p class="ba-beat-note">{esc(note)}</p>
      <p class="ba-beat-blurb">{esc(cat["blurb"])}</p>
    </li>''')
    return f'''<section class="section ba-cats" id="categories" aria-labelledby="ba-cats-title">
  <div class="ba-band-label"><span>What we cover</span><a class="ba-band-link" href="/editorial-policy/">How the desk works</a></div>
  <h2 class="ba-section-title" id="ba-cats-title">Five beats, one question: how people actually live.</h2>
  <ul class="ba-beat-grid">{"".join(tiles)}</ul>
</section>'''


def shelf_block(articles: list[dict], featured_slug: str) -> str:
    """Everything else on the shelf, newest first."""
    rest = [a for a in articles if a["slug"] != featured_slug]
    if not rest:
        return ""
    cards = "".join(card(a) for a in rest[:6])
    n = len(rest)
    return f'''<section class="section ba-shelf" aria-labelledby="ba-shelf-title">
  <div class="ba-band-label"><span>Also on the shelf</span><span class="ba-band-count">{n} {"story" if n == 1 else "stories"}</span></div>
  <h2 class="ba-section-title" id="ba-shelf-title">More from the section</h2>
  <div class="ba-grid">{cards}</div>
</section>'''


def most_read_block(cfg: dict, articles: list[dict], featured_slug: str) -> str:
    """A numbered rail of what readers are actually opening.

    Only rendered once the section has enough stories for the rail to say
    something the shelf does not: with four stories it repeated the same three
    cards, so the page ended with the same titles twice before the footer.
    """
    picks = [a for a in ac.most_read(cfg, articles) if a["slug"] != featured_slug]
    if len(articles) < 6 or not picks:
        return ""
    rows = "".join(
        f'''<li><a class="ba-rank-row" href="{esc(a["route"])}">
      <span class="ba-rank-n">{i + 1:02d}</span>
      <span class="ba-rank-title">{esc(a["title"])}</span>
      <span class="ba-rank-meta">{esc(a["category"]["name"])} &middot; {a["reading_minutes"]} min</span>
    </a></li>''' for i, a in enumerate(picks[:5]))
    return f'''<section class="section ba-mostread" aria-labelledby="ba-mostread-title">
  <div class="ba-band-label"><span>Most read</span><span class="ba-band-count">Measured, not guessed</span></div>
  <h2 class="ba-section-title" id="ba-mostread-title">What readers are opening</h2>
  <ol class="ba-rank">{rows}</ol>
</section>'''


def standards_block() -> str:
    """House standards, plus the one date the page can honestly claim.

    page_wf() appends a generic "Page reviewed <sweep date>" line to any page with
    no date of its own. That generic stamp is older than this section's first day,
    so the landing page states its own build date instead — a real, derived date
    (SOURCE_DATE_EPOCH in CI) rather than a constant.
    """
    import datetime as _dt
    built = ac.human_date(_dt.date.fromisoformat(str(_bwf.TODAY)[:10]))
    return f'''<section class="section alt ba-standards" aria-labelledby="ba-standards-title">
  <div class="ba-band-label"><span>How this section works</span></div>
  <h2 class="ba-section-title" id="ba-standards-title">Editorial standards, in plain language.</h2>
  <div class="ba-standards-grid">
    <div><h3>People are asked, not assumed</h3><p>Every story is reported from conversations with the people in it. Quotes are checked back with the person who said them before publication.</p></div>
    <div><h3>Dates mean something</h3><p>A story carries the date it was published and, where it was revised, the date it changed. Nothing is quietly rewritten and left looking new.</p></div>
    <div><h3>Corrections are public</h3><p>If something here turns out to be wrong, it is corrected on the page and recorded in the <a href="/corrections/">corrections log</a>.</p></div>
    <div><h3>No invented numbers</h3><p>Reading times are computed from the text. Nothing on this page ranks stories by popularity unless that ranking comes from measured reads.</p></div>
  </div>
  <p class="ba-standards-foot">The full detail is in the <a href="/editorial-policy/">editorial policy</a>.
  Reviewed <time datetime="{_bwf.TODAY}">{built}</time>.</p>
</section>'''


def landing(cfg: dict, articles: list[dict]) -> None:
    feat = ac.featured(cfg, articles)
    # The front page reads in one line: what this section is, the story worth
    # starting with, then the shelf. The ad slot sits after the lead, never
    # above it - see ad_slot().
    parts = [
        f'<div class="wrap">{crumbs([("BRYME Articles", "")])}',
        masthead(cfg, articles, title="BRYME Articles", kicker="The section",
                 standfirst=cfg["intro"]),
        lead_block(feat) if feat else empty_state(cfg),
        ad_slot(),
    ]
    if feat:
        parts.append(shelf_block(articles, feat["slug"]))
    parts.append(category_map(cfg, articles))
    if feat:
        parts.append(most_read_block(cfg, articles, feat["slug"]))
    parts.append(standards_block())
    parts.append("</div>")
    schema_items = [{"@type": "ListItem", "position": i + 1, "url": BASE + a["route"], "name": a["title"]}
                    for i, a in enumerate(articles)]
    schema_data = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "@id": BASE + ac.LANDING_ROUTE + "#collection",
        "name": "BRYME Articles",
        "description": cfg["intro"],
        "url": BASE + ac.LANDING_ROUTE,
        "publisher": ORG,
        "isPartOf": {"@type": "WebSite", "name": "BRYME", "url": BASE + "/"},
    }
    if schema_items:
        schema_data["mainEntity"] = {"@type": "ItemList", "itemListElement": schema_items}
    write(ac.LANDING_ROUTE, page_wf(
        title="BRYME Articles: stories about people and money",
        description=("BRYME Articles: reported stories about people, life, society, money and "
                     "ambition — edited, dated and fact-checked by the BRYME Writers desk."),
        route=ac.LANDING_ROUTE,
        current="articles",
        body="\n".join(parts),
        schema_data=schema_data,
        schema_extra=breadcrumb_schema([("BRYME Articles", ac.LANDING_ROUTE)]),
        head_extra=head_extra_for(),
        body_scripts=f'<script src="{SCRIPT}" defer></script>',
    ))


# ---------------------------------------------------------------------------
# Category page — only ever generated when it has a live story
# ---------------------------------------------------------------------------
def category_page(cfg: dict, cat: dict, articles: list[dict]) -> None:
    stories = ac.in_category(articles, cat["slug"])
    if not stories:
        return
    route = ac.CATEGORY_ROUTE.format(slug=cat["slug"])
    others = [c for c in ac.categories_in_use(cfg, articles) if c["slug"] != cat["slug"]]
    other_links = "".join(
        f'<a class="ba-cat-chip" href="{esc(ac.CATEGORY_ROUTE.format(slug=c["slug"]))}">'
        f'{esc(c["name"])}</a>' for c in others)
    cards = "".join(card(a) for a in stories)
    small_pool = [a for a in articles if a["category"]["slug"] != cat["slug"]][:2]
    others_html = ""
    if other_links:
        others_html = ('<section class="section alt ba-othercats">'
                       '<div class="ba-band-label"><span>Elsewhere</span></div>'
                       '<h2 class="ba-section-title">Other beats</h2>'
                       f'<div class="ba-cat-chips">{other_links}</div></section>')
    reco_html = ""
    if small_pool:
        reco_html = ('<section class="section ba-recostrip">'
                     + "".join(recommendation(a) for a in small_pool) + "</section>")
    body = f'''<div class="wrap">{crumbs([("BRYME Articles", ac.LANDING_ROUTE), (cat["name"], "")])}
{masthead(cfg, articles, title=cat["name"], kicker="Beat", standfirst=cat["blurb"])}
<section class="section ba-shelf">
  <div class="ba-band-label"><span>{len(stories)} {"story" if len(stories) == 1 else "stories"} in this beat</span></div>
  <div class="ba-grid">{cards}</div>
</section>
{ad_slot()}
{others_html}
{reco_html}
<p class="ba-backlink"><a href="{ac.LANDING_ROUTE}">&larr; All BRYME Articles</a></p>
</div>'''
    write(route, page_wf(
        title=f'{cat["name"]} — BRYME Articles',
        description=f'{cat["blurb"]} {len(stories)} {"story" if len(stories) == 1 else "stories"} on BRYME Articles.',
        route=route,
        current="articles",
        body=body,
        schema_data={
            "@context": "https://schema.org", "@type": "CollectionPage",
            "@id": BASE + route + "#collection",
            "name": f'{cat["name"]} — BRYME Articles',
            "description": cat["blurb"],
            "url": BASE + route,
            "publisher": ORG,
            "mainEntity": {"@type": "ItemList", "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": BASE + a["route"], "name": a["title"]}
                for i, a in enumerate(stories)]},
        },
        schema_extra=breadcrumb_schema([("BRYME Articles", ac.LANDING_ROUTE), (cat["name"], route)]),
        head_extra=head_extra_for(),
    ))


# ---------------------------------------------------------------------------
# Story page — the reusable template
# ---------------------------------------------------------------------------
def insert_ad_anchor(markup: str) -> str:
    """Place the section's ad slot inside the story, not above the headline.

    After the fifth paragraph, and only when the piece has at least eight, so the
    slot never lands in the opening screen or near the end where the sources and
    the next-stories block already carry the reader's attention. It goes after a
    closed </p> - never inside one - because an element opened mid-paragraph is
    how the figure bug of 22 November shipped literal markdown.
    """
    if markup.count("</p>") < 8:
        return markup
    ends = [m.end() for m in re.finditer(r"</p>", markup)]
    cut = ends[4]
    return markup[:cut] + ad_slot() + markup[cut:]


def article_page(cfg: dict, article: dict, articles: list[dict]) -> None:
    cat = article["category"]
    cat_route = ac.CATEGORY_ROUTE.format(slug=cat["slug"])
    where = f"content/articles/{article['slug']}.md"
    body_html = render_markdown(article["body"], where)
    picks = ac.related_articles(article, articles, 3)
    mid = recommendation(picks[0], heading="While you're here") if picks and article["words"] > 900 else ""
    body_html = insert_mid_recommendation(body_html, mid)
    body_html = insert_ad_anchor(body_html)

    if article.get("pull_quote"):
        pass  # a pull quote written as `> …` in the body is rendered in place

    caption_bits = []
    if article["cover_caption"]:
        caption_bits.append(esc(article["cover_caption"]))
    if article["cover_credit"]:
        caption_bits.append(f'<span class="ba-credit">{esc(article["cover_credit"])}</span>')
    caption = f'<figcaption>{" ".join(caption_bits)}</figcaption>' if caption_bits else ""

    sources = ""
    if article["sources"]:
        items = "".join(
            f'<li><a href="{esc(s["url"])}" rel="noopener nofollow">{esc(s["title"])}</a>'
            + (f' <span>{esc(s["publisher"])}</span>' if s["publisher"] else "") + "</li>"
            for s in article["sources"])
        sources = f'''<section class="ba-sources" aria-labelledby="ba-sources-title">
  <h2 id="ba-sources-title">Sources and further reading</h2>
  <ol>{items}</ol></section>'''

    updated = ""
    if article["updated"] > article["published"]:
        updated = (f'<p class="ba-updated">Updated <time datetime="{article["updated"].isoformat()}">'
                   f'{esc(ac.human_date(article["updated"]))}</time></p>')

    body = f'''<div class="wrap">{crumbs([("BRYME Articles", ac.LANDING_ROUTE), (cat["name"], cat_route), (article["title"], "")])}
<article class="ba-article">
  <header class="ba-article-head">
    <p class="ba-article-kicker"><a href="{esc(cat_route)}">{esc(cat["name"])}</a></p>
    <h1>{esc(article["title"])}</h1>
    <p class="ba-dek">{esc(article["description"])}</p>
    <p class="ba-byline">By <a href="{ac.AUTHOR_ROUTE}">{esc(article["author"])}</a>
      <span aria-hidden="true">&middot;</span>
      <time datetime="{article["published"].isoformat()}">{esc(ac.human_date(article["published"]))}</time>
      <span aria-hidden="true">&middot;</span>
      <span>{article["reading_minutes"]} min read</span></p>
  </header>
  <figure class="ba-cover">
    <img src="{esc(article["cover"])}" alt="{esc(article["cover_alt"])}" width="{article["cover_width"]}" height="{article["cover_height"]}" loading="eager" fetchpriority="high" decoding="async">
    {caption}
  </figure>
  <div class="ba-body prose prose-essay">{body_html}</div>
  {sources}
  <footer class="ba-article-foot">
    <p class="ba-filed">Filed under <a href="{esc(cat_route)}">{esc(cat["name"])}</a>.</p>
    {updated}
    <p class="ba-readnext">Something here you want corrected? <a href="/corrections/">Tell the desk</a>.</p>
  </footer>
</article>
{discovery_block(article, articles)}
</div>'''
    write(article["route"], page_wf(
        title=f'{article["title"]} | BRYME Articles',
        description=article["description"],
        route=article["route"],
        current="articles",
        body=body,
        schema_data=schema_for(article),
        schema_extra=breadcrumb_schema([("BRYME Articles", ac.LANDING_ROUTE),
                                        (cat["name"], cat_route),
                                        (article["title"], "")]),
        head_extra=head_extra_for(article),
        og_type="article",
        og_image=article["cover"],
        og_image_w=article["cover_width"],
        og_image_h=article["cover_height"],
        body_scripts=(f'<script src="{SCRIPT}" defer></script>'
                      f'<script type="application/json" id="ba-article-meta">'
                      + json.dumps({"slug": article["slug"], "category": cat["slug"],
                                    "readingMinutes": article["reading_minutes"]})
                      + "</script>"),
    ))


# ---------------------------------------------------------------------------
# The desk-home ribbon
#
# /writers/ is rendered by a different renderer (desk_hub_render), so the
# section announces itself there with one band directly under the navigation —
# that is the brief's "near the top of the Writers landing page". It is built
# here rather than in build-writing-hub.py so the copy that mentions a story is
# generated from the same live-story list as everything else, and cannot go
# stale when the first story publishes.
# ---------------------------------------------------------------------------
def desk_ribbon(cfg: dict, articles: list[dict]) -> str:
    feat = ac.featured(cfg, articles)
    if feat:
        line = (f'Latest: <b>{esc(feat["title"])}</b> — {esc(feat["category"]["name"])}, '
                f'{feat["reading_minutes"]} min read.')
        cta = "Read BRYME Articles →"
    else:
        line = ("Reported stories about people, money, ambition and the world around us. "
                "The section opens with its first story.")
        cta = "Look inside →"
    return (f'<a class="ba-ribbon" href="{ac.LANDING_ROUTE}">'
            f'<span class="ba-ribbon-kicker">BRYME Articles</span>'
            f'<span class="ba-ribbon-line">{line}</span>'
            f'<span class="ba-ribbon-cta">{cta}</span></a>')


# ---------------------------------------------------------------------------
# Invitation payload (consumed at runtime by assets/articles.js)
# ---------------------------------------------------------------------------
def write_invitation(cfg: dict, articles: list[dict]) -> None:
    payload = ac.invitation_payload(cfg, articles)
    payload["surfaces"] = [
        ac.PUBLIC_PREFIX.split("/articles/")[0] + "/",   # /writers/ — the desk home
        ac.PUBLIC_PREFIX,                                # /writers/articles/ — the landing page
    ]
    out = ROOT / "assets" / "articles" / "invitation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    state = "one story" if payload["article"] else "nothing (no live story)"
    print(f"articles: invitation.json offers {state}")


def main() -> int:
    # The section is fully generated, so its output tree is rebuilt from scratch.
    # build-routing.py moves /articles/ under /writers/ at the end of a normal
    # build, so this only matters if the builder is run twice without a routing
    # pass - in which case a deleted story would otherwise leave its page behind,
    # generated, canonical and no longer in the allowlist.
    import shutil
    out = ROOT / "articles"
    if out.is_dir():
        shutil.rmtree(out)
    cfg = ac.load_config()
    articles = ac.load_published(cfg)
    landing(cfg, articles)
    for cat in ac.categories_in_use(cfg, articles):
        category_page(cfg, cat, articles)
    for article in articles:
        article_page(cfg, article, articles)
    write_invitation(cfg, articles)
    print(f"articles: landing + {len(articles)} story page(s) + "
          f"{len(ac.categories_in_use(cfg, articles))} category page(s) "
          f"(drafts on disk: {sum(1 for a in ac.load_all(cfg) if a['draft'])})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
