#!/usr/bin/env python3
"""Phase 12: audit the video/catalogue URLs.

The brief says BRYME has a large number of indexed video-related URLs and asks
whether each one carries original BRYME value beyond the embedded video. That
population is /entertainment/movie/<slug>/ - 719 pages, each embedding an
official trailer (689 of them; the other 30 do not) and each carrying an
editorial score, a desk verdict, context and links to sibling films.

This is NOT the definition of "thin embed page" the brief is worried about, and
the audit has to be able to show that rather than assert it. So each page is
measured for the seven things the brief names: commentary, context, explanation,
analysis, supporting information, related BRYME resources and meaningful text -
expressed as things a parser can count (words of the page's own text after
furniture removal, organised units, external sources, trailer presence, Movie
schema, inbound links) and never as a score invented out of nothing.

The catalogue has its own sitemap, public/entertainment/sitemap-catalogue.xml,
which IS registered in the root sitemap index and in robots.txt. Verified live
before writing this: the alternative reading - 719 indexable pages quietly
missing from every sitemap - was checked and is false. The seven /movie/ URLs
that ARE noindexed are redirect stubs for merged film entries; they are excluded
from grading and counted separately.

Output: reports/video-audit-<date>.json
"""

from __future__ import annotations

import collections
import datetime as dt
import importlib.util
import json
import pathlib
import re
import statistics
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
TODAY = dt.date.today().isoformat()
CATALOGUE = ROOT / "public" / "entertainment" / "sitemap-catalogue.xml"

_spec = importlib.util.spec_from_file_location("audit_quality", ROOT / "scripts" / "audit-quality.py")
aq = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(aq)

WORDS = aq.WORDS
HREF = aq.HREF

# What the brief asks a video page to earn its place with, as measurable things.
# A trailer is present either as an <iframe> straight in the HTML, or as the
# facade pattern: a thumbnail plus .trailer-facade, with the player injected when
# it nears the viewport. 30 catalogue pages ship the second way, and the first
# pass called all 30 trailerless. Both are trailers; one is lazier than the other.
TRAILER = re.compile(r"(?i)<iframe[^>]+(?:youtube-nocookie\.com|youtube\.com|youtu\.be|vimeo\.com)")
TRAILER_FACADE = re.compile(r'class="[^"]*(?:nx-trailer-frame|trailer-facade)[^"]*')
# The page stating that it has no trailer is now the honest case, not a gap:
NO_TRAILER_NOTE = "No trailer is embedded on this page"
NOINDEX = re.compile(r'(?i)<meta[^>]+name=["\']robots["\'][^>]*content=["\'][^"\']*noindex')


def catalogue_urls() -> list[str]:
    root = ET.parse(CATALOGUE).getroot()
    return [e.text.strip().replace("https://thebryme.com", "") for e in root.iter()
            if e.tag.endswith("loc") and e.text]


def main() -> int:
    urls = catalogue_urls()
    rows, stubs, missing = [], [], []
    for u in urls:
        f = ROOT / "public" / u.strip("/") / "index.html"
        if not f.exists():
            missing.append(u)
            continue
        html = f.read_text(encoding="utf-8", errors="replace")
        if NOINDEX.search(html):
            stubs.append(u)
            continue
        r = aq.signals(u, html)
        r["file"] = str(f.relative_to(ROOT))
        r["trailer"] = bool(TRAILER.search(html) or TRAILER_FACADE.search(html))
        r["trailerMode"] = ("iframe" if TRAILER.search(html)
                            else "facade" if TRAILER_FACADE.search(html) else "none")
        r["statesNoTrailer"] = NO_TRAILER_NOTE in html
        r["iframe_title"] = (re.findall(r'(?i)<iframe[^>]+title="([^"]*)"', html) or [""])[0]
        r["movie_schema"] = '"Movie"' in html
        r["has_score"] = bool(re.search(r'(?i)editorial score', html))
        # the heading is entity-encoded in the HTML (desk&rsquo;s verdict), so
        # matching the literal character counted 2 pages out of 719
        r["verdict"] = bool(re.search(r"(?i)verdict", html))
        r["more_like_this"] = "More like this" in html
        rows.append(r)

    # Furniture is stripped inside the catalogue family: the trailer caption, the
    # "The story" label and the score line repeat on hundreds of these pages and
    # are not the page's own writing.
    seen = collections.Counter()
    for r in rows:
        for p in {aq.key(x) for x in r["paras"]}:
            seen[p] += 1
    template = {p for p, n in seen.items() if n >= aq.TEMPLATE_MIN_PAGES}
    for r in rows:
        uniq = [p for p in r["paras"] if aq.key(p) not in template]
        r["unique_words"] = len(WORDS.findall(" ".join(uniq)))
        r["own_share"] = round(r["unique_words"] / max(1, r["words"]), 3)
        r["units"] = r["h2"] + r["h3"] + r["rows"]

    known = {r["url"] for r in rows}
    inbound = collections.Counter()
    for r in rows:
        html = (ROOT / r["file"]).read_text(encoding="utf-8", errors="replace")
        for href in HREF.findall(html):
            if not href.startswith("/") or href.startswith("//"):
                continue
            t = href.split("#")[0].rstrip("/") + "/"
            if t in known:
                inbound[t] += 1

    for r in rows:
        r["inbound"] = inbound.get(r["url"], 0)
        w, uw, ext = r["words"], r["unique_words"], r["external_links"]
        # The brief's test, in order: is there anything here that is BRYME's own?
        if not r["trailer"] and uw < 200:
            r["grade"], r["reason"] = "E", f"no trailer and only {uw} words of its own"
        elif uw < 150:
            r["grade"], r["reason"] = "C", f"{uw} words of its own — carried by the template"
        elif r["trailer"] and w >= 600 and uw >= 400 and ext >= 2 and r["inbound"] >= 3:
            r["grade"], r["reason"] = "A", (f"trailer, {w}w ({uw} own), {ext} outside sources, "
                                            f"{r['inbound']} inbound links")
        else:
            gaps = []
            if not r["trailer"]:
                gaps.append("no trailer")
            if w < 600:
                gaps.append(f"{w}w")
            if uw < 400:
                gaps.append(f"{uw} own words")
            if ext < 2:
                gaps.append(f"{ext} outside sources")
            if r["inbound"] < 3:
                gaps.append(f"{r['inbound']} inbound links")
            r["grade"], r["reason"] = "B", "original verdict and context, but " + ", ".join(gaps)

    counts = collections.Counter(r["grade"] for r in rows)
    w = sorted(r["words"] for r in rows)
    uw = sorted(r["unique_words"] for r in rows)
    out = {
        "generated": TODAY,
        "method": {
            "population": "the 719 URLs in public/entertainment/sitemap-catalogue.xml",
            "verifiedBeforeAudit": [
                "the catalogue sitemap is registered in the root sitemap index and in robots.txt, "
                "and both are live (HTTP 200) - these pages are NOT missing from the sitemaps",
                "the 7 /movie/ URLs that are noindexed are redirect stubs for merged film entries and sit "
            "outside the catalogue sitemap, so they are not in this population",
            ],
            "valueTest": "the brief's seven things, as measurable: own text after furniture removal, "
                         "organised units, trailer presence, Movie schema, external sources, inbound "
                         "links, desk verdict",
            "furniture": f"paragraphs appearing on >= {aq.TEMPLATE_MIN_PAGES} catalogue pages",
        },
        "population": {
            "urlsInCatalogueSitemap": len(urls), "graded": len(rows),
            "noindexRedirectStubs": len(stubs), "missingBuild": missing,
            "withTrailer": sum(1 for r in rows if r["trailer"]),
            "trailerModes": dict(collections.Counter(r["trailerMode"] for r in rows)),
            "pagesStatingNoTrailer": sum(1 for r in rows if r["statesNoTrailer"]),
            "withMovieSchema": sum(1 for r in rows if r["movie_schema"]),
            "withDeskVerdict": sum(1 for r in rows if r["verdict"]),
            "withMoreLikeThis": sum(1 for r in rows if r["more_like_this"]),
            "withEditorialScore": sum(1 for r in rows if r["has_score"]),
            "templateParagraphsRemoved": len(template),
        },
        "grades": {g: counts.get(g, 0) for g in "ABCDE"},
        "distributions": {
            "words": {"min": w[0], "p10": w[len(w) // 10], "median": int(statistics.median(w)),
                      "p90": w[int(len(w) * 0.9)], "max": w[-1]},
            "uniqueWords": {"min": uw[0], "p10": uw[len(uw) // 10],
                            "median": int(statistics.median(uw)),
                            "p90": uw[int(len(uw) * 0.9)], "max": uw[-1]},
            "ownShareMedian": round(statistics.median(r["own_share"] for r in rows), 3),
            "inboundMedian": int(statistics.median(r["inbound"] for r in rows)),
        },
        "gaps": {
            "noOutsideSource": sum(1 for r in rows if r["external_links"] == 0),
            "underThreeHundredWords": sum(1 for r in rows if r["words"] < 300),
            "noTrailer": [r["url"] for r in rows if not r["trailer"]],
            "noInbound": sum(1 for r in rows if r["inbound"] == 0),
        },
        "pages": [{k: v for k, v in r.items() if not k.startswith("_") and k != "paras"}
                  for r in sorted(rows, key=lambda x: (x["grade"], x["words"]))],
    }
    REPORTS.mkdir(exist_ok=True)
    path = REPORTS / f"video-audit-{TODAY}.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    p = out["population"]
    d = out["distributions"]
    print(f"catalogue: {p['graded']} graded of {p['urlsInCatalogueSitemap']} "
          f"({p['noindexRedirectStubs']} noindex stubs excluded, {len(missing)} missing)")
    print(f"trailers {p['withTrailer']}   Movie schema {p['withMovieSchema']}   "
          f"desk verdict {p['withDeskVerdict']}   editorial score {p['withEditorialScore']}   "
          f"'more like this' {p['withMoreLikeThis']}")
    print(f"own-words median {d['uniqueWords']['median']} of {d['words']['median']} total "
          f"(own share {d['ownShareMedian']}), inbound median {d['inboundMedian']}")
    print(f"grades: {out['grades']}")
    print(f"gaps: {out['gaps']['noOutsideSource']} cite nobody, "
          f"{out['gaps']['underThreeHundredWords']} under 300w, "
          f"{len(out['gaps']['noTrailer'])} without a trailer, {out['gaps']['noInbound']} with no inbound")
    print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
