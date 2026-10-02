#!/usr/bin/env python3
"""Publish released, curated Watch This / Then Try This paths on title pages.

A recommendation batch is a first-class content input under
content/entertainment-recommendations/. Only batches explicitly marked
"released" are rendered or made indexable. This keeps unfinished catalogue
pages noindex while each completed batch earns its place with five distinct,
editorially explained next watches.

Run before build-routing.py: it decorates the generated ecosystem source pages
and updates the Entertainment property sitemap; routing then copies the pages
and derives the global search allowlist from that sitemap.
"""
from __future__ import annotations

import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "content" / "entertainment-recommendations"
ECOSYSTEM = ROOT / "ecosystem"
START = "<!-- nextclip-watch-next:start -->"
END = "<!-- nextclip-watch-next:end -->"
STYLE_ID = "nx-watch-next-style"

sys.path.insert(0, str(ROOT / "scripts"))
import bryme_config as cfg  # noqa: E402

SITE = cfg.site_url().rstrip("/")
ROUTE_RE = re.compile(r"^/entertainment/movie/[a-z0-9-]+/$")
ROBOTS_TAG_RE = re.compile(r"<meta\b(?=[^>]*\bname=[\"']robots[\"'])[^>]*>", re.I)
OLD_RECS_RE = re.compile(
    r"<h2>More like this</h2>\s*<ul class=[\"']nx-facts[\"']>.*?</ul>", re.S | re.I
)
URL_BLOCK_RE = re.compile(r"<url\b[^>]*>.*?</url>", re.S | re.I)
LOC_RE = re.compile(r"<loc>\s*([^<]+?)\s*</loc>", re.I)
MAIN_RE = re.compile(r"<(main|article)\b[^>]*>(.*?)</\1>", re.S | re.I)
STRIP_RE = re.compile(r"<(script|style|noscript|svg|template)\b[^>]*>.*?</\1>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
ENTITY_RE = re.compile(r"&[a-z#0-9]{2,8};")
SPACE_RE = re.compile(r"\s+")
WORD_RE = re.compile(r"\b[\w’'-]+\b")


def main_word_count(text: str) -> int:
    match = MAIN_RE.search(text)
    body = match.group(2) if match else text
    body = STRIP_RE.sub(" ", body)
    body = TAG_RE.sub(" ", body)
    body = ENTITY_RE.sub(" ", body)
    body = SPACE_RE.sub(" ", body).strip()
    return len(WORD_RE.findall(body))


CSS = """<style id=\"nx-watch-next-style\">
.nx-next-path{margin:34px 0;padding:25px 0;border-top:1px solid #2c3138;border-bottom:1px solid #2c3138}
.nx-next-kicker{margin:0 0 8px;color:#d8b64a;font-size:11px;font-weight:850;letter-spacing:.16em;text-transform:uppercase}
.nx-next-path>.nx-next-title{margin:0 0 10px;color:#fff;font-family:Georgia,'Times New Roman',serif;font-size:clamp(24px,3.5vw,34px);line-height:1.12}
.nx-next-intro{max-width:64ch;margin:0 0 20px;color:#b9bfc7;font-size:15px;line-height:1.65}
.nx-next-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:0;padding:0;list-style:none}
.nx-next-card{min-width:0;padding:18px;background:#101318;border:1px solid #2c3138;border-top:2px solid #d8b64a;border-radius:3px}
.nx-next-card:first-child{grid-column:1/-1}
.nx-next-card-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
.nx-next-route{color:#d8b64a;font-size:10px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
.nx-next-number{color:#9aa2ab;font-size:11px;font-variant-numeric:tabular-nums}
.nx-next-card h3{margin:9px 0 2px;font-size:20px;line-height:1.25}
.nx-next-card h3 a{color:#fff;text-decoration:underline;text-decoration-color:#65707d;text-underline-offset:3px}
.nx-next-card h3 a:hover{color:#f3d879;text-decoration-color:#f3d879}
.nx-next-meta{margin:0 0 11px!important;color:#9aa2ab!important;font-size:12px;line-height:1.5!important}
.nx-next-why,.nx-next-diff{margin:9px 0!important;color:#d9dde1!important;font-size:15px;line-height:1.65!important}
.nx-next-diff strong{color:#fff}
.nx-next-headsup{margin:14px 0 0!important;padding-top:12px;border-top:1px solid #2c3138;color:#cbd0d6!important;font-size:14px;line-height:1.65!important}
.nx-next-headsup strong{display:block;margin-bottom:3px;color:#fff;font-size:12px;letter-spacing:.04em}
.nx-next-headsup span{display:block}
@media(max-width:680px){.nx-next-list{grid-template-columns:1fr}.nx-next-card:first-child{grid-column:auto}.nx-next-path{padding:21px 0}}
</style>"""
EMPTY_CATALOGUE = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<!-- Unreviewed title pages stay out of search. Released recommendation batches '
    'are listed in entertainment/sitemap.xml. -->\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    '</urlset>\n'
)


def route_ok(route: object, context: str) -> str:
    if not isinstance(route, str) or not ROUTE_RE.fullmatch(route):
        raise ValueError(f"{context}: invalid canonical entertainment route {route!r}")
    return route


def read_batches() -> tuple[dict[str, dict], dict[str, str]]:
    grouped: dict[str, dict] = {}
    release_dates: dict[str, str] = {}
    if not DATA_DIR.is_dir():
        return grouped, release_dates
    for path in sorted(DATA_DIR.glob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        if doc.get("status") != "released":
            print(f"watch-next: skip unreleased batch {doc.get('batch', path.stem)}")
            continue
        date = doc.get("released_on", "")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(date)):
            raise ValueError(f"{path.relative_to(ROOT)}: released_on must be YYYY-MM-DD")
        batch = str(doc.get("batch", path.stem))
        for source in doc.get("sources", []):
            source_route = route_ok(source.get("source_route"), f"{batch} source")
            if source_route in grouped:
                raise ValueError(f"duplicate released source route across batches: {source_route}")
            recommendations = source.get("recommendations", [])
            if len(recommendations) != 5:
                raise ValueError(f"{source_route}: expected 5 recommendations, found {len(recommendations)}")
            slots = [item.get("slot") for item in recommendations]
            if sorted(slots) != [1, 2, 3, 4, 5]:
                raise ValueError(f"{source_route}: recommendation slots must be exactly 1–5")
            target_routes = []
            for item in recommendations:
                route = route_ok(item.get("target_route"), f"{source_route} target")
                if route == source_route:
                    raise ValueError(f"{source_route}: self-recommendation")
                target_routes.append(route)
                for field in ("title", "relationship", "why_it_fits", "what_differs", "editors_heads_up"):
                    if not str(item.get(field, "")).strip():
                        raise ValueError(f"{source_route}: slot {item.get('slot')} missing {field}")
                note_words = len(re.findall(r"\b[\w’'-]+\b", item["editors_heads_up"]))
                if note_words < 20:
                    raise ValueError(f"{source_route}: slot {item.get('slot')} Editor's Heads-Up is too short ({note_words} words)")
                target_file = ECOSYSTEM / route.strip("/") / "index.html"
                if not target_file.is_file():
                    raise ValueError(f"{source_route}: recommendation target is missing: {route}")
            if len(target_routes) != len(set(target_routes)):
                raise ValueError(f"{source_route}: duplicate recommendation targets")
            source_file = ECOSYSTEM / source_route.strip("/") / "index.html"
            if not source_file.is_file():
                raise ValueError(f"released source page is missing: {source_file.relative_to(ROOT)}")
            grouped[source_route] = {"batch": batch, "title": source["source_title"],
                                     "recommendations": sorted(recommendations, key=lambda x: x["slot"])}
            release_dates[source_route] = date
        if int(doc.get("source_count", len(doc.get("sources", [])))) != len(doc.get("sources", [])):
            raise ValueError(f"{batch}: source_count does not match sources array")
    return grouped, release_dates


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def render_section(source_title: str, batch: str, recommendations: list[dict]) -> str:
    cards = []
    for item in recommendations:
        meta = " · ".join(str(x) for x in (item.get("format"), item.get("year")) if str(x or "").strip())
        cards.append(
            '  <li class="nx-next-card">\n'
            '    <div class="nx-next-card-top">'
            f'<span class="nx-next-route">{e(item["relationship"])}</span>'
            f'<span class="nx-next-number">{int(item["slot"]):02d} / 05</span></div>\n'
            f'    <h3><a href="{e(item["target_route"])}">{e(item["title"])}</a></h3>\n'
            f'    <p class="nx-next-meta">{e(meta)}</p>\n'
            f'    <p class="nx-next-why">{e(item["why_it_fits"])}</p>\n'
            f'    <p class="nx-next-diff"><strong>What changes:</strong> {e(item["what_differs"])}</p>\n'
            f'    <p class="nx-next-headsup"><strong>Editor\'s Heads-Up</strong><span>{e(item["editors_heads_up"])}</span></p>\n'
            '  </li>'
        )
    return (
        f"{START}\n"
        f'<section class="nx-next-path" data-recommendation-batch="{e(batch)}" aria-labelledby="nx-next-path-title">\n'
        '  <p class="nx-next-kicker">Watch this · then try this</p>\n'
        f'  <h2 class="nx-next-title" id="nx-next-path-title">Where to go after {e(source_title)}</h2>\n'
        '  <p class="nx-next-intro">Five carefully chosen next watches. Each one gives you a specific connection, what shifts, and a spoiler-free note on the experience.</p>\n'
        '  <ol class="nx-next-list">\n' + "\n".join(cards) + "\n"
        '  </ol>\n'
        '</section>\n'
        f"{END}"
    )


def set_robots(html_text: str, route: str) -> str:
    head = re.search(r"<head\b[^>]*>(.*?)</head>", html_text, re.S | re.I)
    if not head:
        raise ValueError(f"{route}: missing head")
    tags = list(ROBOTS_TAG_RE.finditer(head.group(1)))
    if len(tags) > 1:
        raise ValueError(f"{route}: multiple robots meta tags")
    if tags:
        tag = tags[0].group(0)
        content_value = re.search(r"""(\bcontent\s*=\s*)([\"'])(.*?)(\2)""", tag, re.I)
        if not content_value:
            raise ValueError(f"{route}: robots meta has no content attribute")
        updated = tag[:content_value.start(3)] + "index,follow" + tag[content_value.end(3):]
        return html_text[:head.start(1)] + head.group(1).replace(tag, updated, 1) + html_text[head.end(1):]
    insert_at = head.start(1)
    return html_text[:insert_at] + '<meta name="robots" content="index,follow">\n' + html_text[insert_at:]


def inject_page(route: str, info: dict) -> bool:
    path = ECOSYSTEM / route.strip("/") / "index.html"
    original = path.read_text(encoding="utf-8")
    section = render_section(info["title"], info["batch"], info["recommendations"])
    if START in original:
        marked = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
        updated, n = marked.subn(lambda _: section, original, count=1)
        if n != 1:
            raise ValueError(f"{route}: malformed Watch This / Then Try This markers")
    else:
        updated, n = OLD_RECS_RE.subn(lambda _: section, original, count=1)
        if n != 1:
            raise ValueError(f"{route}: expected one existing 'More like this' section, found {n}")
    updated = set_robots(updated, route)
    style = re.search(rf"<style\s+id=[\"']{re.escape(STYLE_ID)}[\"']>.*?</style>", updated, re.S | re.I)
    if style:
        updated = updated[:style.start()] + CSS + updated[style.end():]
    else:
        if not re.search(r"</head>", updated, re.I):
            raise ValueError(f"{route}: missing closing head")
        updated = re.sub(r"</head>", CSS + "\n</head>", updated, count=1, flags=re.I)
    words = main_word_count(updated)
    if words < 600:
        raise ValueError(f"{route}: only {words} main-text words after recommendations; minimum for index release is 600")
    changed = updated != original
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


def upsert_sitemap(release_dates: dict[str, str]) -> int:
    path = ECOSYSTEM / "entertainment" / "sitemap.xml"
    if not path.is_file():
        raise ValueError("missing ecosystem/entertainment/sitemap.xml")
    text = path.read_text(encoding="utf-8")
    if "<urlset" not in text or "</urlset>" not in text:
        raise ValueError("entertainment sitemap is not a urlset")
    seen: set[str] = set()
    kept: list[str] = []
    for match in URL_BLOCK_RE.finditer(text):
        block = match.group(0)
        loc_match = LOC_RE.search(block)
        if not loc_match:
            kept.append(block)
            continue
        loc = html.unescape(loc_match.group(1).strip())
        route = urlsplit(loc).path
        if route.startswith("/entertainment/movie/") and route not in release_dates:
            # A previous ecosystem generation can repopulate this legacy
            # catalogue sitemap. Keep only batches with released editorial copy.
            continue
        if route in release_dates:
            if route in seen:
                continue
            seen.add(route)
            date = release_dates[route]
            if re.search(r"<lastmod>.*?</lastmod>", block, re.S | re.I):
                block = re.sub(r"<lastmod>.*?</lastmod>", f"<lastmod>{date}</lastmod>", block, count=1, flags=re.S | re.I)
            else:
                block = block.replace("</url>", f"<lastmod>{date}</lastmod></url>")
        kept.append(block)
    missing = [route for route in sorted(release_dates) if route not in seen]
    new_blocks = [f"<url><loc>{e(SITE + route)}</loc><lastmod>{release_dates[route]}</lastmod></url>" for route in missing]
    prefix = text[:text.find("<url>")] if "<url>" in text else text[:text.find("</urlset>")]
    updated = prefix + "\n".join(kept + new_blocks) + "\n</urlset>\n"
    # Fail closed on duplicates or malformed XML before writing.
    root = ET.fromstring(updated)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [node.text for node in root.findall("s:url/s:loc", ns) if node.text]
    if len(locs) != len(set(locs)):
        raise ValueError("entertainment sitemap contains duplicate loc entries")
    path.write_text(updated, encoding="utf-8")
    return len(missing)


def main() -> int:
    grouped, release_dates = read_batches()
    if not grouped:
        print("watch-next: no released recommendation batches")
        return 0
    changed = sum(inject_page(route, info) for route, info in grouped.items())
    added = upsert_sitemap(release_dates)
    # The legacy catalogue sitemap is deliberately not a second discovery path:
    # only the main property sitemap gets pages whose recommendation batch is
    # complete and released. Keep all build tiers aligned before routing/copying.
    empty_catalogue = ECOSYSTEM / "entertainment" / "sitemap-catalogue.xml"
    if empty_catalogue.exists():
        empty_catalogue.write_text(EMPTY_CATALOGUE, encoding="utf-8")
    robots = ECOSYSTEM / "entertainment" / "robots.txt"
    if robots.exists():
        body = robots.read_text(encoding="utf-8")
        body = re.sub(r"^Sitemap:\s*\S*sitemap-catalogue\.xml\s*\n?", "", body, flags=re.M)
        robots.write_text(body, encoding="utf-8")
    print(f"watch-next: {len(grouped)} released titles, {sum(len(v['recommendations']) for v in grouped.values())} picks, {changed} pages updated, {added} sitemap URLs added")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"watch-next: ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
