#!/usr/bin/env python3
"""Read-only repository-wide HTML/SEO inventory for the BRYME audit.

This script never runs the site's generators and never edits product files. It only
reads the committed tree and writes reports/site-inventory.csv plus
reports/site-audit-data.json.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from collections import Counter, defaultdict
from copy import copy
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HOST = "bryme.onrender.com"
ORIGIN = f"https://{HOST}"
OUT_CSV = ROOT / "reports" / "site-inventory.csv"
OUT_JSON = ROOT / "reports" / "site-audit-data.json"
WORD_RE = re.compile(r"[\w’'\-]+", re.UNICODE)
SPACE_RE = re.compile(r"\s+")
SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")


def rel_to_route(rel: str) -> str:
    rel = rel.replace(os.sep, "/")
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def clean_text(node) -> str:
    if not node:
        return ""
    return SPACE_RE.sub(" ", node.get_text(" ", strip=True)).strip()


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def get_meta(soup, name=None, prop=None):
    attrs = {}
    if name:
        attrs["name"] = re.compile(rf"^{re.escape(name)}$", re.I)
    if prop:
        attrs["property"] = re.compile(rf"^{re.escape(prop)}$", re.I)
    tag = soup.find("meta", attrs=attrs)
    return (tag.get("content") or "").strip() if tag else ""


def schema_types(obj, out=None):
    if out is None:
        out = []
    if isinstance(obj, dict):
        t = obj.get("@type")
        if isinstance(t, str):
            out.append(t)
        elif isinstance(t, list):
            out.extend(x for x in t if isinstance(x, str))
        for value in obj.values():
            schema_types(value, out)
    elif isinstance(obj, list):
        for value in obj:
            schema_types(value, out)
    return out


def find_schema_objects(obj, wanted: set[str], out=None):
    if out is None:
        out = []
    if isinstance(obj, dict):
        t = obj.get("@type")
        ts = {t} if isinstance(t, str) else set(t or []) if isinstance(t, list) else set()
        if ts & wanted:
            out.append(obj)
        for value in obj.values():
            find_schema_objects(value, wanted, out)
    elif isinstance(obj, list):
        for value in obj:
            find_schema_objects(value, wanted, out)
    return out


def route_category(route: str) -> str:
    if route == "/":
        return "home"
    return route.strip("/").split("/", 1)[0] or "home"


def parse_sitemap(filename: str):
    p = ROOT / filename
    tree = ET.parse(p)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9", "news": "http://www.google.com/schemas/sitemap-news/0.9"}
    rows = []
    for url in tree.findall(".//sm:url", ns):
        loc = (url.findtext("sm:loc", default="", namespaces=ns) or "").strip()
        lm = (url.findtext("sm:lastmod", default="", namespaces=ns) or "").strip()
        pub = (url.findtext("news:news/news:publication_date", default="", namespaces=ns) or "").strip()
        rows.append({"url": loc, "path": urlsplit(loc).path, "lastmod": lm, "publication_date": pub})
    return rows


def internal_path(href: str, source_route: str):
    if not href or href.startswith("#") or href.lower().startswith(SKIP_SCHEMES):
        return None
    try:
        u = urlsplit(urljoin(ORIGIN + source_route, href))
    except Exception:
        return None
    host = (u.hostname or "").lower()
    if host and host != HOST:
        return None
    path = unquote(u.path or "/")
    path = re.sub(r"/{2,}", "/", path)
    return path


def map_path_to_route(path: str, known_routes: set[str]):
    if path == "/index.html":
        return "/"
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    if path in known_routes:
        return path
    if not Path(path).suffix and not path.endswith("/") and path + "/" in known_routes:
        return path + "/"
    return path


def norm_fingerprint(text: str):
    text = text.casefold()
    text = re.sub(r"\b20\d{2}\b", " YEAR ", text)
    text = re.sub(r"\b\d+(?:[.,:]\d+)*\b", " NUM ", text)
    text = re.sub(r"[^\w]+", " ", text)
    return SPACE_RE.sub(" ", text).strip()


def main_content_clone(soup):
    base = soup.find("main") or soup.body or soup
    clone = BeautifulSoup(str(base), "lxml")
    for bad in clone.select("script,style,noscript,template,svg,canvas,form"):
        bad.decompose()
    return clone


def parse_file(path: Path, route: str):
    raw = path.read_text("utf-8", errors="replace")
    soup = BeautifulSoup(raw, "lxml")
    robots = " ".join([get_meta(soup, "robots"), get_meta(soup, "googlebot")]).casefold()
    noindex = bool(re.search(r"(?:^|[\s,])noindex(?:$|[\s,])", robots))
    title = clean_text(soup.title)
    desc = get_meta(soup, "description")
    canon_tag = soup.find("link", rel=lambda v: v and "canonical" in [str(x).lower() for x in (v if isinstance(v, list) else [v])])
    canonical = (canon_tag.get("href") or "").strip() if canon_tag else ""
    canonical_path = urlsplit(canonical).path if canonical else ""

    main_clone = main_content_clone(soup)
    main_text = clean_text(main_clone)
    main_words = len(words(main_text))
    h1s = [clean_text(x) for x in soup.find_all("h1")]
    headings = Counter((x.name or "").lower() for x in soup.find_all(re.compile(r"^h[1-6]$")))

    schema_blobs = []
    schema_errors = 0
    for tag in soup.find_all("script", attrs={"type": re.compile(r"application/ld\+json", re.I)}):
        try:
            schema_blobs.append(json.loads(tag.string or tag.get_text() or "null"))
        except Exception:
            schema_errors += 1
    types = []
    article_objs = []
    video_objs = []
    faq_objs = []
    job_objs = []
    for blob in schema_blobs:
        types.extend(schema_types(blob))
        article_objs.extend(find_schema_objects(blob, {"Article", "NewsArticle", "BlogPosting", "SportsArticle"}))
        video_objs.extend(find_schema_objects(blob, {"VideoObject"}))
        faq_objs.extend(find_schema_objects(blob, {"FAQPage"}))
        job_objs.extend(find_schema_objects(blob, {"JobPosting"}))

    authors = []
    dates_published = []
    dates_modified = []
    for obj in article_objs:
        a = obj.get("author")
        vals = a if isinstance(a, list) else [a]
        for v in vals:
            if isinstance(v, dict) and v.get("name"):
                authors.append(str(v["name"]))
            elif isinstance(v, str):
                authors.append(v)
        if obj.get("datePublished"):
            dates_published.append(str(obj["datePublished"]))
        if obj.get("dateModified"):
            dates_modified.append(str(obj["dateModified"]))

    links = []
    main_links = []
    main_base = soup.find("main") or soup
    for a in soup.find_all("a", href=True):
        links.append((a.get("href", "").strip(), clean_text(a)))
    for a in main_base.find_all("a", href=True):
        main_links.append((a.get("href", "").strip(), clean_text(a)))

    imgs = soup.find_all("img")
    img_hosts = Counter()
    for img in imgs:
        src = (img.get("src") or img.get("data-src") or "").strip()
        host = (urlsplit(urljoin(ORIGIN + route, src)).hostname or "").lower() if src else ""
        if host:
            img_hosts[host] += 1

    hidden_nodes = soup.select("[hidden]")
    hidden_words = sum(len(words(clean_text(n))) for n in hidden_nodes)

    # Permanently/initially CSS-hidden title-page elements. Tabs count separately because
    # their content is user-revealable; trailer labels/fallbacks are permanently hidden.
    permanent_hidden_selectors = [
        ".nm-trailer-embed .video-context",
        ".nm-trailer-embed .trailer-fallback",
        ".nm-trailer-embed .video-figure figcaption",
        ".nm-trailer-embed .trailer-meta",
        ".nm-detail-extra .nm-extra-head",
        ".desk-hint",
    ]
    permanent_nodes = []
    seen_ids = set()
    for sel in permanent_hidden_selectors:
        for n in soup.select(sel):
            if id(n) not in seen_ids:
                seen_ids.add(id(n)); permanent_nodes.append(n)
    css_hidden_words = sum(len(words(clean_text(n))) for n in permanent_nodes)
    tab_hidden_words = sum(len(words(clean_text(n))) for n in soup.select(".nm-panel:not(.is-on)"))
    title_page = bool(soup.select_one("main.tp-page"))

    # Build text fingerprints from publisher content, not global chrome.
    exact_hash = hashlib.sha256(main_text.encode()).hexdigest() if main_text else ""
    normalized = norm_fingerprint(main_text)
    norm_hash = hashlib.sha256(normalized.encode()).hexdigest() if normalized else ""

    return {
        "file": str(path.relative_to(ROOT)).replace(os.sep, "/"),
        "route": route,
        "category": route_category(route),
        "bytes": len(raw.encode("utf-8")),
        "noindex": noindex,
        "indexable": not noindex,
        "robots": robots.strip(),
        "title": title,
        "title_chars": len(title),
        "description": desc,
        "description_chars": len(desc),
        "canonical": canonical,
        "canonical_path": canonical_path,
        "h1_count": len(h1s),
        "h1": " | ".join(h1s),
        "main_words": main_words,
        "paragraphs": len((soup.find("main") or soup).find_all("p")),
        "h2_count": headings["h2"],
        "internal_links_raw": 0,
        "external_links": 0,
        "main_internal_links_raw": 0,
        "main_external_links": 0,
        "links": links,
        "main_links": main_links,
        "images": len(imgs),
        "images_missing_alt": sum(1 for i in imgs if not (i.get("alt") or "").strip()),
        "images_missing_dimensions": sum(1 for i in imgs if not (i.get("width") and i.get("height"))),
        "youtube_images": sum(img_hosts[h] for h in ("i.ytimg.com", "img.youtube.com")),
        "image_hosts": dict(img_hosts),
        "iframes": len(soup.find_all("iframe")),
        "schema_types": sorted(set(types)),
        "schema_errors": schema_errors,
        "article_schema": len(article_objs),
        "video_schema": len(video_objs),
        "faq_schema": len(faq_objs),
        "job_schema": len(job_objs),
        "authors": sorted(set(authors)),
        "date_published": sorted(set(dates_published)),
        "date_modified": sorted(set(dates_modified)),
        "hidden_attr_nodes": len(hidden_nodes),
        "hidden_attr_words": hidden_words,
        "css_permanent_hidden_nodes": len(permanent_nodes),
        "css_permanent_hidden_words": css_hidden_words,
        "css_tab_hidden_words": tab_hidden_words,
        "title_page_nav_css_hidden": title_page,
        "exact_content_hash": exact_hash,
        "normalized_content_hash": norm_hash,
        "main_text": main_text,
    }


def grouped_duplicates(rows, key, min_words=20):
    groups = defaultdict(list)
    for r in rows:
        if r["main_words"] >= min_words and r[key]:
            groups[r[key]].append(r["route"])
    return sorted((v for v in groups.values() if len(v) > 1), key=lambda x: (-len(x), x[0]))


def summarize_counts(rows, predicate=lambda r: True):
    return dict(sorted(Counter(r["category"] for r in rows if predicate(r)).items()))


def main():
    html_files = sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)
    routes = {rel_to_route(str(p.relative_to(ROOT))): p for p in html_files}
    known_routes = set(routes)
    rows = [parse_file(p, route) for route, p in sorted(routes.items())]
    by_route = {r["route"]: r for r in rows}

    incoming_all = Counter()
    incoming_indexable = Counter()
    incoming_main_all = Counter()
    incoming_main_indexable = Counter()
    raw_noncanonical_link_variants = Counter()
    broken_internal_targets = Counter()
    internal_links_to_noindex = Counter()

    for r in rows:
        for field, inc_all, inc_idx in [
            ("links", incoming_all, incoming_indexable),
            ("main_links", incoming_main_all, incoming_main_indexable),
        ]:
            for href, anchor in r[field]:
                p = internal_path(href, r["route"])
                if p is None:
                    if field == "links" and href and not href.startswith("#") and not href.lower().startswith(SKIP_SCHEMES):
                        try:
                            if urlsplit(urljoin(ORIGIN + r["route"], href)).hostname not in (None, "", HOST):
                                r["external_links"] += 1
                        except Exception:
                            pass
                    if field == "main_links" and href and not href.startswith("#") and not href.lower().startswith(SKIP_SCHEMES):
                        try:
                            if urlsplit(urljoin(ORIGIN + r["route"], href)).hostname not in (None, "", HOST):
                                r["main_external_links"] += 1
                        except Exception:
                            pass
                    continue
                target = map_path_to_route(p, known_routes)
                if field == "links":
                    r["internal_links_raw"] += 1
                else:
                    r["main_internal_links_raw"] += 1
                if target in known_routes:
                    if target != r["route"]:
                        inc_all[target] += 1
                        if r["indexable"]:
                            inc_idx[target] += 1
                    if field == "links" and by_route[target]["noindex"]:
                        internal_links_to_noindex[target] += 1
                    if p != target:
                        raw_noncanonical_link_variants[p] += 1
                elif not p.startswith(("/assets/", "/api/")):
                    # Do not call image/data assets broken page links here; retain likely page paths.
                    if field == "links" and (not Path(p).suffix or p.endswith((".html", "/"))):
                        broken_internal_targets[p] += 1

    for r in rows:
        r["inlinks_all"] = incoming_all[r["route"]]
        r["inlinks_from_indexable"] = incoming_indexable[r["route"]]
        r["main_inlinks_all"] = incoming_main_all[r["route"]]
        r["main_inlinks_from_indexable"] = incoming_main_indexable[r["route"]]
        cp = map_path_to_route(r["canonical_path"], known_routes) if r["canonical_path"] else ""
        r["canonical_target_route"] = cp
        r["self_canonical"] = bool(cp and cp == r["route"])
        r["canonical_target_exists"] = bool(cp in known_routes)
        r["canonical_target_noindex"] = bool(cp in by_route and by_route[cp]["noindex"])

    sitemap = parse_sitemap("sitemap.xml")
    news_sitemap = parse_sitemap("news-sitemap.xml")
    sitemap_paths = {map_path_to_route(x["path"], known_routes) for x in sitemap}
    news_paths = {map_path_to_route(x["path"], known_routes) for x in news_sitemap}
    for r in rows:
        r["in_sitemap"] = r["route"] in sitemap_paths
        r["in_news_sitemap"] = r["route"] in news_paths

    indexable = [r for r in rows if r["indexable"]]
    noindex = [r for r in rows if r["noindex"]]
    indexable_self = [r for r in indexable if r["self_canonical"]]
    indexable_orphans = [r for r in indexable_self if not r["inlinks_from_indexable"] and r["route"] != "/"]
    main_orphans = [r for r in indexable_self if not r["main_inlinks_from_indexable"] and r["route"] != "/"]
    hidden_indexable = [r for r in indexable_self if not r["in_sitemap"] and not r["inlinks_from_indexable"] and r["route"] != "/"]

    canonical_groups = defaultdict(list)
    for r in rows:
        if r["canonical"]:
            canonical_groups[r["canonical"]].append(r["route"])
    many_to_one = sorted((v for v in canonical_groups.values() if len(v) > 1), key=lambda x: (-len(x), x[0]))

    title_groups = defaultdict(list)
    desc_groups = defaultdict(list)
    for r in indexable:
        if r["title"]:
            title_groups[r["title"]].append(r["route"])
        if r["description"]:
            desc_groups[r["description"]].append(r["route"])
    duplicate_titles = sorted((v for v in title_groups.values() if len(v)>1), key=lambda x:(-len(x),x[0]))
    duplicate_descs = sorted((v for v in desc_groups.values() if len(v)>1), key=lambda x:(-len(x),x[0]))

    thin_bands = {}
    for label, lo, hi in [
        ("0-99", 0, 99), ("100-199", 100, 199), ("200-299", 200, 299),
        ("300-499", 300, 499), ("500-999", 500, 999), ("1000+", 1000, 10**9),
    ]:
        thin_bands[label] = sum(lo <= r["main_words"] <= hi for r in indexable_self)

    # Compact row version for JSON (CSV retains the details); do not embed full page text/links.
    keep_fields = [
        "file","route","category","bytes","noindex","indexable","robots","title","title_chars",
        "description_chars","canonical","canonical_target_route","self_canonical","canonical_target_exists",
        "canonical_target_noindex","h1_count","h1","main_words","paragraphs","h2_count",
        "internal_links_raw","external_links","main_internal_links_raw","main_external_links",
        "inlinks_all","inlinks_from_indexable","main_inlinks_all","main_inlinks_from_indexable",
        "images","images_missing_alt","images_missing_dimensions","youtube_images","iframes",
        "schema_types","schema_errors","article_schema","video_schema","faq_schema","job_schema",
        "authors","date_published","date_modified","hidden_attr_nodes","hidden_attr_words",
        "css_permanent_hidden_nodes","css_permanent_hidden_words","css_tab_hidden_words",
        "title_page_nav_css_hidden","in_sitemap","in_news_sitemap",
    ]

    summary = {
        "generated_at": "2026-09-04",
        "html_files": len(rows),
        "indexable": len(indexable),
        "noindex": len(noindex),
        "self_canonical_indexable": len(indexable_self),
        "sitemap_urls": len(sitemap),
        "news_sitemap_urls": len(news_sitemap),
        "by_category_all": summarize_counts(rows),
        "by_category_indexable": summarize_counts(rows, lambda r:r["indexable"]),
        "by_category_noindex": summarize_counts(rows, lambda r:r["noindex"]),
        "sitemap_noindex": sorted(r["route"] for r in rows if r["in_sitemap"] and r["noindex"]),
        "sitemap_nonself_canonical": sorted(r["route"] for r in rows if r["in_sitemap"] and not r["self_canonical"]),
        "sitemap_missing_file": sorted(p for p in sitemap_paths if p not in known_routes),
        "indexable_self_missing_sitemap": sorted(r["route"] for r in indexable_self if not r["in_sitemap"]),
        "indexable_nonself_canonical": sorted(r["route"] for r in indexable if not r["self_canonical"]),
        "missing_canonical_indexable": sorted(r["route"] for r in indexable if not r["canonical"]),
        "canonical_target_missing": sorted(r["route"] for r in rows if r["canonical"] and not r["canonical_target_exists"]),
        "canonical_target_noindex": sorted(r["route"] for r in rows if r["canonical_target_noindex"]),
        "indexable_orphans_global_links": sorted(r["route"] for r in indexable_orphans),
        "indexable_orphans_main_links": sorted(r["route"] for r in main_orphans),
        "hidden_indexable_no_sitemap_no_inlinks": sorted(r["route"] for r in hidden_indexable),
        "indexable_css_nav_hidden_title_pages": sorted(r["route"] for r in indexable if r["title_page_nav_css_hidden"]),
        "indexable_with_permanent_css_hidden_words": sorted(
            ({"route":r["route"],"hidden_words":r["css_permanent_hidden_words"]} for r in indexable if r["css_permanent_hidden_words"]),
            key=lambda x:(-x["hidden_words"],x["route"])
        ),
        "indexable_with_hidden_attr_words": sorted(
            ({"route":r["route"],"hidden_words":r["hidden_attr_words"],"nodes":r["hidden_attr_nodes"]} for r in indexable if r["hidden_attr_words"]),
            key=lambda x:(-x["hidden_words"],x["route"])
        ),
        "thin_bands_indexable_self_canonical": thin_bands,
        "indexable_self_under_200_words": sorted(
            ({"route":r["route"],"words":r["main_words"]} for r in indexable_self if r["main_words"]<200),
            key=lambda x:(x["words"],x["route"])
        ),
        "indexable_self_under_300_words": sorted(
            ({"route":r["route"],"words":r["main_words"]} for r in indexable_self if r["main_words"]<300),
            key=lambda x:(x["words"],x["route"])
        ),
        "indexable_duplicate_titles": duplicate_titles,
        "indexable_duplicate_descriptions": duplicate_descs,
        "exact_main_content_duplicate_groups": grouped_duplicates(rows,"exact_content_hash"),
        "normalized_main_content_duplicate_groups": grouped_duplicates(rows,"normalized_content_hash"),
        "canonical_many_to_one_groups": many_to_one,
        "raw_noncanonical_internal_link_variants": dict(raw_noncanonical_link_variants.most_common()),
        "broken_likely_page_targets": dict(broken_internal_targets.most_common()),
        "most_linked_noindex_targets": dict(internal_links_to_noindex.most_common()),
        "schema_type_counts_indexable": dict(sorted(Counter(t for r in indexable for t in r["schema_types"]).items())),
        "indexable_schema_errors": sorted(r["route"] for r in indexable if r["schema_errors"]),
        "indexable_articles_without_schema_author": sorted(r["route"] for r in indexable if r["article_schema"] and not r["authors"]),
        "indexable_articles_without_published_date": sorted(r["route"] for r in indexable if r["article_schema"] and not r["date_published"]),
        "indexable_articles_without_modified_date": sorted(r["route"] for r in indexable if r["article_schema"] and not r["date_modified"]),
        "image_summary_indexable": {
            "images": sum(r["images"] for r in indexable),
            "missing_alt": sum(r["images_missing_alt"] for r in indexable),
            "missing_dimensions": sum(r["images_missing_dimensions"] for r in indexable),
            "youtube_images": sum(r["youtube_images"] for r in indexable),
            "pages_only_youtube_images": sum(bool(r["images"]) and r["images"]==r["youtube_images"] for r in indexable),
        },
        "sitemap_lastmod_counts": dict(Counter(x["lastmod"] for x in sitemap)),
        "news_publication_date_counts": dict(Counter(x["publication_date"] for x in news_sitemap)),
    }

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keep_fields)
        writer.writeheader()
        for r in rows:
            row = {k:r.get(k,"") for k in keep_fields}
            for k,v in list(row.items()):
                if isinstance(v,(list,dict)):
                    row[k]=json.dumps(v,ensure_ascii=False,separators=(",",":"))
            writer.writerow(row)

    payload = {
        "summary": summary,
        "sitemap": sitemap,
        "news_sitemap": news_sitemap,
        "pages": [{k:r.get(k) for k in keep_fields} for r in rows],
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({k:v for k,v in summary.items() if k in {
        "html_files","indexable","noindex","self_canonical_indexable","sitemap_urls","news_sitemap_urls",
        "by_category_all","by_category_indexable","by_category_noindex","thin_bands_indexable_self_canonical",
        "image_summary_indexable","sitemap_lastmod_counts","news_publication_date_counts"
    }}, indent=2))
    print("sitemap_noindex", len(summary["sitemap_noindex"]))
    print("sitemap_nonself", len(summary["sitemap_nonself_canonical"]))
    print("indexable_self_missing_sitemap", len(summary["indexable_self_missing_sitemap"]))
    print("indexable_nonself", len(summary["indexable_nonself_canonical"]))
    print("orphans_global", len(summary["indexable_orphans_global_links"]))
    print("orphans_main", len(summary["indexable_orphans_main_links"]))
    print("hidden_indexable", len(summary["hidden_indexable_no_sitemap_no_inlinks"]))
    print("exact_duplicate_groups", len(summary["exact_main_content_duplicate_groups"]))
    print("normalized_duplicate_groups", len(summary["normalized_main_content_duplicate_groups"]))
    print("duplicate_title_groups", len(summary["indexable_duplicate_titles"]))
    print("duplicate_desc_groups", len(summary["indexable_duplicate_descriptions"]))
    print("broken_likely_targets", len(summary["broken_likely_page_targets"]))
    print(OUT_CSV.relative_to(ROOT), OUT_JSON.relative_to(ROOT))


if __name__ == "__main__":
    main()
