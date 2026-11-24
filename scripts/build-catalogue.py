#!/usr/bin/env python3
"""Build /catalogue/ — one page that lists everything on the writers' desk.

Why this page exists
--------------------
The owner, reading his own site: "visually appealing website looks with
separate catalogue of everything". The desk had grown to 686 pages reachable
only through mega-menus, filters and search. Search answers a question you
already know how to ask; a catalogue answers "what is in here?".

Design decisions, so the next person does not undo them by accident
--------------------------------------------------------------------
* Source of truth is `content/index-allowlist.json` — the same list that feeds
  robots and the sitemap — plus the *generated* HTML for titles and summaries.
  Nothing is hand-listed here, so a new market, guide or tool appears in the
  catalogue the next time the site is built. (A hand-maintained index would rot
  within a month; this one cannot.)
* Five registers, matching the colour system in assets/bryme-v2.css:
  markets (indigo), guides (ochre), tools (teal), essays (plum), articles
  (brick) — and the desk's own pages in slate. Colour means "which kind of
  thing", never "look at me".
* Filtering is client-side and instant (assets/catalogue.js). Without
  JavaScript the page is still a complete, printable A–Z index; the filter bar
  is simply inert, and every link still works.
* Rows, not cards. Six hundred boxes is a wall; six hundred lines of type with
  hairline rules is an index you can scan.

Emits: public/writers/catalogue/index.html
"""
from __future__ import annotations

import html
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

_spec = importlib.util.spec_from_file_location(
    "build_writing_first", str(ROOT / "scripts" / "build-writing-first.py"))
_bwf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bwf)

write = _bwf.write
page_wf = _bwf.page_wf

ALLOWLIST = ROOT / "content" / "index-allowlist.json"
PUBLIC = ROOT / "public" / "writers"

# Register order is the order we recommend reading the desk in, and it is the
# order of the numbered headings on the page.
REGISTERS = [
    ("markets", "01", "Markets",
     "Publications that pay, one row each — what they pay, whether they are open, and the "
     "date a human last checked it.",
     ("/writing/", "/writing-opportunities/")),
    ("guides", "02", "Guides",
     "Craft, process, grammar and the business of freelancing — the whole library, in "
     "reading order by title.",
     ("/learn/", "/guides/", "/compare/", "/problems/")),
    ("tools", "03", "Tools",
     "Forty-nine utilities that run inside your browser. Nothing you type into them is "
     "uploaded, and none of them asks for an account.",
     ("/tools/",)),
    ("essays", "04", "Essays",
     "The argument behind the desk: what we think about pay, editors, and writing from "
     "Nigeria in 2026.",
     ("/essays/", "/intelligence/")),
    ("articles", "05", "Articles",
     "BRYME Articles — reported pieces and long reads, published on their own schedule.",
     ("/articles/",)),
]
DESK = ("desk", "06", "The desk itself",
        "How this place works and who runs it: the beginner path, the standards, the "
        "policies, the tools index and the corrections log.", ())

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")
_META_DESC = re.compile(
    r'<meta\s+name="description"\s+content="([^"]*)"', re.I)
_TITLE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)


def route_file(route: str) -> Path:
    """public/writers/<route>/index.html for a writers-relative route."""
    rel = route.strip("/")
    return PUBLIC / rel / "index.html" if rel else PUBLIC / "index.html"


def clean(text: str) -> str:
    return _WS.sub(" ", html.unescape(_TAG.sub(" ", text))).strip()


def trim(text: str, limit: int = 132) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(",;:—-")
    return cut + "…"


def read_page(route: str) -> tuple[str, str, str]:
    """(title, summary) read from the page the build already wrote."""
    path = route_file(route)
    try:
        src = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "", "", ""
    # The visible <h1> is the entry's name ("Afrolicious", "Word counter"); the
    # <title> is the search-engine sentence ("Afrolicious writing submissions:
    # $75 for 600–800 words") and is far too long to line up in a column of six
    # hundred. Fall back to the title only when a page has no h1.
    title = ""
    m = _H1.search(src) or _TITLE.search(src)
    if m:
        title = clean(m.group(1)).rstrip(". ")
        for sep in (" | BRYME", " — BRYME", " - BRYME", "| The BRYME", "| BRYME Writers"):
            title = title.split(sep)[0].strip()
    summary = ""
    d = _META_DESC.search(src)
    if d:
        summary = trim(clean(d.group(1)))
    seo = ""
    s = _TITLE.search(src)
    if s:
        seo = clean(s.group(1))
        for sep in (" | BRYME", " — BRYME", " - BRYME", "| The BRYME", "| BRYME Writers"):
            seo = seo.split(sep)[0].strip()
    return title, summary, seo


def classify(route: str) -> str:
    for key, _n, _label, _blurb, prefixes in REGISTERS:
        if any(route == p or route.startswith(p) for p in prefixes):
            return key
    return DESK[0]


def letter_of(title: str) -> str:
    for ch in title:
        if ch.isalnum():
            return ch.upper()
    return "#"


def build_rows(routes: list[str]) -> dict[str, list[dict]]:
    """Every allowlisted page, classified and de-duplicated exactly once.

    De-duplication is global, not per register: the allowlist carries both
    /checklists/ and /learn/writing-checklists/, and listing a page twice under
    two headings makes the index look careless even when both routes exist.
    """
    order = [r[0] for r in REGISTERS] + [DESK[0]]
    rows: list[dict] = []
    for route in routes:
        key = classify(route)
        title, summary, seo = read_page(route)
        if not title:
            continue
        rows.append({
            "reg": key,
            "href": "/writers" + route if route != "/" else "/writers/",
            "title": title,
            "summary": summary,
            "seo": seo,
            "key": (title + " " + summary + " " + route).lower(),
        })
    rows.sort(key=lambda r: (order.index(r["reg"]), r["title"].lower()))
    kept = dedupe(rows)
    buckets: dict[str, list[dict]] = {k: [] for k in order}
    for r in kept:
        buckets[r["reg"]].append(r)
    return buckets


def dedupe(rows: list[dict]) -> list[dict]:
    """One line per thing.

    The allowlist contains ~55 routes that are word-for-word duplicates of
    another route in it - an older /guides/ path kept alongside the /learn/ one.
    An entry whose summary is identical to one already kept is dropped.

    Entries that share a name but not a summary are genuinely different pages -
    two Analog pages, one for fact one for fiction - so both stay, each with a
    small muted label taken from its own search title so a reader can tell them
    apart at a glance.
    """
    by_title: dict[str, list[dict]] = {}
    for r in rows:
        by_title.setdefault(r["title"].lower(), []).append(r)
    out: list[dict] = []
    for group in by_title.values():
        kept: list[dict] = []
        for r in group:
            if any(other["summary"] == r["summary"] for other in kept):
                continue
            kept.append(r)
        if len(kept) > 1:
            for r in kept:
                r["label"] = distinguishing_label(r)
        out.extend(kept)
    out.sort(key=lambda r: r["title"].lower())
    return out


def distinguishing_label(row: dict) -> str:
    """What tells two same-named pages apart.

    Prefer the tail of the page's own search title — it is written for a human
    ("…: 8–10 cents a word for short fiction") — and fall back to the parent
    shelf's path when the titles are identical too.
    """
    name = row["title"].lower()
    seo = (row.get("seo") or "").strip()
    tail = seo
    if tail.lower().startswith(name):
        tail = tail[len(name):]
    tail = tail.strip(" :—-–·")
    if tail:
        return tail if len(tail) <= 52 else tail[:52].rsplit(" ", 1)[0] + "…"
    parent = "/".join(row["href"].rstrip("/").split("/")[:-1])
    return parent or row["href"]


def render_row(row: dict) -> str:
    """One index line. The whole row is the link, so the tap target on a phone
    is the full width of the page rather than the first four words of a title."""
    data = html.escape(row["key"], quote=True)
    title = html.escape(row["title"])
    label = row.get("label")
    if label:
        title += f'<span class="cat-x">· {html.escape(label)}</span>'
    summary = html.escape(row["summary"])
    body = f'<a href="{row["href"]}"><span class="cat-t">{title}</span>'
    if summary:
        body += f'<span class="cat-s">{summary}</span>'
    body += "</a>"
    return f'<li class="cat-row" data-k="{data}">{body}</li>'


def build() -> None:
    routes = json.loads(ALLOWLIST.read_text(encoding="utf-8"))["routes"]
    # The catalogue lists itself last, not first: it is the index, not the shelf.
    routes = [r for r in routes if r != "/catalogue/"]
    buckets = build_rows(routes)
    total = sum(len(v) for v in buckets.values())

    letters = sorted({letter_of(r["title"]) for b in buckets.values() for r in b})
    az = "".join(
        f'<button type="button" data-letter="{l}" aria-pressed="false">{l}</button>'
        for l in letters)

    # The count next to each register is live: the filter updates it in step with
    # the heading, so "55 of 686" never sits beside a stale "Markets 334".
    jump = ('<a href="#cat-markets" style="--reg:var(--reg-markets)">Markets '
            f'<span data-jump="markets">{len(buckets["markets"])}</span></a>')
    for key, _n, label, _blurb, _p in REGISTERS[1:]:
        jump += (f'<a href="#cat-{key}" style="--reg:var(--reg-{key})">{label} '
                 f'<span data-jump="{key}">{len(buckets[key])}</span></a>')
    jump += (f'<a href="#cat-desk" style="--reg:var(--reg-desk)">The desk itself '
             f'<span data-jump="desk">{len(buckets["desk"])}</span></a>')

    sections = []
    for key, num, label, blurb, _p in REGISTERS + [DESK]:
        rows = buckets[key]
        if not rows:
            continue
        sections.append(
            f'<section class="rg" id="cat-{key}" style="--reg:var(--reg-{key});'
            f'--reg-tint:var(--reg-{key}-tint)" data-rg="{key}">'
            '<header class="rg-head">'
            f'<p class="rg-n">{num}</p>'
            f'<div><h2 class="rg-t">{label} <span class="rg-c" data-count>{len(rows)}</span></h2>'
            f'<p class="rg-s">{html.escape(blurb)}</p></div></header>'
            '<ul class="cat-list">' + "".join(render_row(r) for r in rows) + "</ul></section>")

    body = f'''<div class="cat-page">
<div class="wrap"><nav class="breadcrumb"><a href="/writers/">Home</a> / Catalogue</nav></div>
<div class="wrap cat-hero">
  <p class="cat-kicker">The whole writers&rsquo; desk &middot; <span data-total>{total}</span> entries</p>
  <h1>Everything on the desk, in one place.</h1>
  <p class="cat-lede">Every market, guide, tool, essay and article this desk has published,
  listed once, by name. Type in the box to narrow it to what you are after &mdash; a country,
  a rate, a word you remember. Nothing here is behind an account.</p>
  <div class="cat-bar" id="cat-bar">
    <div class="cat-bar-in">
      <label class="sr-only" for="cat-q">Filter the catalogue</label>
      <input class="cat-q" id="cat-q" type="search" autocomplete="off" spellcheck="false"
             placeholder="Filter &mdash; &ldquo;nigeria&rdquo;, &ldquo;pitch&rdquo;, &ldquo;invoice&rdquo;, &ldquo;$100&rdquo;">
      <span class="cat-count" id="cat-count" aria-live="polite">{total} entries</span>
    </div>
    <nav class="cat-jump" aria-label="Jump to a register">{jump}</nav>
  </div>
  <div class="cat-az" id="cat-az" role="group" aria-label="Filter by first letter">{az}</div>
</div>
<!--ba-ad-->
<div class="wrap">
  {''.join(sections)}
  <p class="cat-empty" id="cat-empty" hidden>Nothing on the desk matches that. <button type="button"
    class="cat-reset" id="cat-reset">Clear the filter</button></p>
  <p class="cat-note">This index is generated from the same list that feeds the sitemap, so it is
  never out of date by hand. Last built {_bwf.TODAY}. Every page here carries its own
  date&nbsp;&mdash;&nbsp;<a href="/writers/about/">how the desk is run</a>.</p>
</div>
</div>'''

    write("/catalogue/", page_wf(
        title=f"Everything on the desk — all {total} pages, in one index",
        description=(f"Every market, guide, tool, essay and article on the BRYME writers\' desk, "
                     f"listed and filterable in one place — {total} pages, no account needed."),
        route="/catalogue/",
        current="catalogue",
        body=body,
        body_scripts='<script src="/assets/catalogue.js" defer></script>',
    ))
    print(f"catalogue: {total} entries "
          + ", ".join(f"{k} {len(v)}" for k, v in buckets.items()))


if __name__ == "__main__":
    build()
