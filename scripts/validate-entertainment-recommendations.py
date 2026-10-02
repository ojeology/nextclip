#!/usr/bin/env python3
"""Release gate for the curated Entertainment watch-next batches.

Only batches marked "released" may be indexable. The source HTML, routed tree,
public artifact, sitemap, and generated allowlist must all agree.
"""
from __future__ import annotations

import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "content" / "entertainment-recommendations"
TIERS = {"ecosystem": ROOT / "ecosystem", "site": ROOT, "public": ROOT / "public"}
ROUTE_RE = re.compile(r"^/entertainment/movie/[a-z0-9-]+/$")
ROBOTS = re.compile(r'<meta\b(?=[^>]*\bname=["\']robots["\'])[^>]*>', re.I)
CANON = re.compile(r'<link\b(?=[^>]*\brel=["\']canonical["\'])[^>]*\bhref=["\']([^"\']+)', re.I)
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


def fail(message: str) -> None:
    raise SystemExit("entertainment recommendations: FAIL: " + message)


def page_path(root: Path, route: str) -> Path:
    return root / route.strip("/") / "index.html"


def robots_value(text: str, route: str) -> str:
    head = re.search(r"<head\b[^>]*>(.*?)</head>", text, re.S | re.I)
    if not head:
        fail(f"{route}: missing head")
    tags = ROBOTS.findall(head.group(1))
    if len(tags) != 1:
        fail(f"{route}: expected one robots meta, found {len(tags)}")
    content = re.search(r"\bcontent\s*=\s*([\"'])(.*?)\1", tags[0], re.I)
    return content.group(2).lower() if content else ""


def main() -> int:
    site = str(json.loads((ROOT / "site.config.json").read_text(encoding="utf-8")).get("siteUrl", "")).rstrip("/")
    batches = sorted(DATA_DIR.glob("*.json")) if DATA_DIR.is_dir() else []
    active: dict[str, tuple[str, dict]] = {}
    notes: list[str] = []
    for data_path in batches:
        doc = json.loads(data_path.read_text(encoding="utf-8"))
        if doc.get("status") != "released":
            continue
        batch = str(doc.get("batch", data_path.stem))
        if len(doc.get("sources", [])) != int(doc.get("source_count", -1)):
            fail(f"{batch}: source_count mismatch")
        if sum(len(s.get("recommendations", [])) for s in doc.get("sources", [])) != int(doc.get("recommendation_count", -1)):
            fail(f"{batch}: recommendation_count mismatch")
        for source in doc["sources"]:
            route = source.get("source_route", "")
            if not ROUTE_RE.fullmatch(route):
                fail(f"{batch}: invalid source route {route!r}")
            if route in active:
                fail(f"duplicate released source {route}")
            items = source.get("recommendations", [])
            if len(items) != 5 or sorted(item.get("slot") for item in items) != [1, 2, 3, 4, 5]:
                fail(f"{route}: expected slots 1–5 exactly once")
            targets = []
            for item in items:
                target = item.get("target_route", "")
                if not ROUTE_RE.fullmatch(target):
                    fail(f"{route}: invalid recommendation target {target!r}")
                if target == route:
                    fail(f"{route}: self-link")
                targets.append(target)
                if not (ROOT / "ecosystem" / target.strip("/") / "index.html").is_file():
                    fail(f"{route}: target does not exist in canonical source tree: {target}")
                note = str(item.get("editors_heads_up", "")).strip()
                if len(re.findall(r"\b[\w’'-]+\b", note)) < 20:
                    fail(f"{route} slot {item.get('slot')}: Editor's Heads-Up under 20 words")
                notes.append(note)
            if len(targets) != len(set(targets)):
                fail(f"{route}: duplicate target within five picks")
            active[route] = (batch, source)
    if not active:
        print("entertainment recommendations: no released batches; gate skipped")
        return 0
    if len(notes) != len(set(notes)):
        fail("released Editor's Heads-Up notes are not unique")

    total_cards = 0
    for route, (batch, source) in active.items():
        wanted = {item["target_route"] for item in source["recommendations"]}
        for tier, root in TIERS.items():
            f = page_path(root, route)
            if not f.is_file():
                fail(f"{tier}: missing page {route}")
            text = f.read_text(encoding="utf-8")
            words = main_word_count(text)
            if words < 600:
                fail(f"{tier}: {route} has only {words} main-text words; minimum indexability gate is 600")
            if robots_value(text, route) != "index,follow":
                fail(f"{tier}: {route} is not index,follow")
            canon = CANON.search(text)
            if not canon or canon.group(1).rstrip("/") != (site + route).rstrip("/"):
                fail(f"{tier}: {route} canonical changed or missing")
            if text.count("<!-- nextclip-watch-next:start -->") != 1 or text.count("<!-- nextclip-watch-next:end -->") != 1:
                fail(f"{tier}: {route} has missing or duplicate Watch This / Then Try This block")
            block = text.split("<!-- nextclip-watch-next:start -->", 1)[1].split("<!-- nextclip-watch-next:end -->", 1)[0]
            if len(re.findall(r'class="nx-next-card"', block)) != 5:
                fail(f"{tier}: {route} does not have exactly five recommendation cards")
            links = set(re.findall(r'<h3><a href="([^"]+)"', block))
            if links != wanted:
                fail(f"{tier}: {route} rendered recommendation links differ from content data")
            for label in ("What changes:", "Editor's Heads-Up"):
                if block.count(label) != 5:
                    fail(f"{tier}: {route} must render five {label!r} labels")
            if "<h2>More like this</h2>" in text:
                fail(f"{tier}: {route} still has the generic unreasoned recommendation list")
        total_cards += 5

    # Unfinished or unreleased title pages remain noindex in the canonical source.
    movie_root = ROOT / "ecosystem" / "entertainment" / "movie"
    for f in movie_root.glob("*/index.html"):
        route = "/" + f.parent.relative_to(ROOT / "ecosystem").as_posix() + "/"
        robots = robots_value(f.read_text(encoding="utf-8"), route)
        if route in active and robots != "index,follow":
            fail(f"released route lost indexability: {route}")
        if route not in active and "noindex" not in robots:
            fail(f"unreleased title page must remain noindex: {route}")

    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for tier, root in TIERS.items():
        ent = root / "entertainment" / "sitemap.xml"
        if not ent.is_file():
            fail(f"{tier}: missing Entertainment sitemap")
        locs = [n.text for n in ET.parse(ent).getroot().findall("s:url/s:loc", ns) if n.text]
        movie_routes = {urlsplit(loc).path for loc in locs if "/entertainment/movie/" in urlsplit(loc).path}
        if movie_routes != set(active):
            fail(f"{tier}: Entertainment sitemap has {len(movie_routes)} title routes; expected the {len(active)} released routes")
        cat = root / "entertainment" / "sitemap-catalogue.xml"
        if cat.is_file() and any(n.tag.endswith("loc") for n in ET.parse(cat).getroot().iter()):
            fail(f"{tier}: legacy catalogue sitemap must remain empty")
    routed_allowlist = json.loads((ROOT / "content/index-allowlist.routed.json").read_text(encoding="utf-8"))
    missing = set(active) - set(routed_allowlist.get("routes", []))
    if missing:
        fail(f"released pages absent from routed index allowlist: {sorted(missing)[:5]}")
    root_index = (ROOT / "public" / "sitemap.xml").read_text(encoding="utf-8")
    if f"{site}/entertainment/sitemap.xml" not in root_index:
        fail("root sitemap index does not list the Entertainment property sitemap")
    print(f"entertainment recommendations: PASS — {len(active)} released pages, {total_cards} curated links (5 distinct picks per page), crawlable next-watch links; all other title pages remain noindex")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
