#!/usr/bin/env python3
"""Phase 10 — content quality audit of every indexable Writers URL.

The brief asks for each page to be classified A-E and, crucially, for the audit
to tell apart four things that look identical in a click report:

    genuinely weak content
    good content that has not yet ranked
    pages with low impressions because they are new
    pages with strong search potential but poor rankings

Per-page Search Console data is not available to this script, so it classifies
on EVIDENCE IT CAN SEE — the built page itself — and marks the pages whose grade
could move once impressions exist, instead of guessing at traffic. That is why
`new` is an annotation and not a grade: a three-week-old page with a thin body
is not the same object as a three-year-old page with a thin body.

GRADES
    A  strong and useful
    B  useful, needs improvement
    C  thin or weak
    D  duplicate / redundant
    E  should probably not remain indexable

--- the duplicate rule, and the mistake it took to get there ---------------

The first version compared 8-word shingles of each page's opening text. It
reported 52 duplicates, and they were not duplicates: every publication page on
this desk carries the same "How to write for them" block, the same nine-step
pitch pattern, the same safety notice. Two pages about different magazines
overlapped 68% because 68% of their text is the desk's own template. A shingle
test over raw page text measures how much boilerplate two pages share, which is
a fact about the template, not about the content.

So template is removed first. A paragraph appearing on four or more pages is
desk furniture, not copy, and is dropped before anything is compared. What is
left is the text that makes the page that page — and the shingle comparison runs
on that, which is what "duplicate" was always supposed to mean.
"""
from __future__ import annotations

import collections
import datetime as dt
import json
import pathlib
import re
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "writers" / "sitemap.xml"
REPORTS = ROOT / "reports"
TODAY = dt.date.today().isoformat()

CHROME = re.compile(r"(?is)<(script|style|nav|header|footer|svg|noscript|aside)\b.*?</\1>")
HREF = re.compile(r'href="([^"]+)"')
WORDS = re.compile(r"[A-Za-z0-9\u2019'-]+")

NEW_DAYS = 45          # inside this window a page is not judgeable on traffic
TEMPLATE_MIN_PAGES = 4  # a paragraph on this many pages is desk furniture
SHINGLE_N = 10
DUP_OVERLAP = 0.70


def routes() -> list[str]:
    xml = SITEMAP.read_text(encoding="utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def file_for(url: str) -> pathlib.Path:
    path = url.replace("https://thebryme.com/writers", "").strip("/")
    return ROOT / "writers" / (path + "/index.html") if path else ROOT / "writers" / "index.html"


def main_text(html: str) -> str:
    m = re.search(r"(?is)<main\b.*?</main>", html)
    body = m.group(0) if m else html
    body = CHROME.sub(" ", body)
    body = re.sub(r"(?i)</(p|div|li|h[1-6]|tr|section)\s*>", "\n", body)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"&[a-z#0-9]+;", " ", body)
    return body


def paragraphs(text: str) -> list[str]:
    out = []
    for chunk in text.split("\n"):
        c = re.sub(r"\s+", " ", chunk).strip()
        if len(WORDS.findall(c)) >= 8:
            out.append(c)
    return out


def key(p: str) -> str:
    return " ".join(WORDS.findall(p.lower()))


def signals(url: str, html: str) -> dict:
    text = main_text(html)
    title = re.search(r"(?is)<title>(.*?)</title>", html)
    desc = re.search(r'(?is)<meta[^>]+name="description"[^>]+content="([^"]*)"', html)
    hrefs = [h for h in HREF.findall(html) if not h.startswith(("#", "mailto:", "tel:", "javascript:"))]
    external = {h for h in hrefs if h.startswith("http") and "thebryme.com" not in h}
    return {
        "url": url.replace("https://thebryme.com", ""),
        "file": str(file_for(url).relative_to(ROOT)),
        "words": len(WORDS.findall(re.sub(r"\s+", " ", text))),
        "title": (title.group(1).strip() if title else ""),
        "desc_len": len(desc.group(1)) if desc else 0,
        "h2": len(re.findall(r"<h2\b", html)),
        "h3": len(re.findall(r"<h3\b", html)),
        "lists": len(re.findall(r"<li\b", html)),
        "tables": len(re.findall(r"<table\b", html)),
        # ORGANISED UNITS, not headings. A glossary organises 31 terms as a
        # definition list, a country page organises its records as cards, a
        # comparison organises rows in a table - none of them need an <h2> to do
        # it, and grading structure by heading count alone marked the glossary
        # "thin or weak" on 1 heading while 1,047 pages link to it.
        "dt": len(re.findall(r"<dt\b", html)),
        "rows": len(re.findall(r"<tr\b", html)),
        "cards": len(re.findall(r'class="[^"]*(?:job-card|path-card|chip-card|pub-card)[^"]*"', html)),
        "external_links": len(external),
        "internal_links": len({h for h in hrefs if h.startswith("/")}),
        "has_jsonld": '"@context"' in html,
        "newest_date": _newest(html),
        "paras": paragraphs(text),
    }


def _newest(html: str) -> str:
    ds = re.findall(r'"(?:datePublished|dateModified)"\s*:\s*"(\d{4}-\d{2}-\d{2})', html)
    ds += re.findall(r'<time[^>]+datetime="(\d{4}-\d{2}-\d{2})"', html)
    return max(ds) if ds else ""


def shingles(tokens: list[str], n: int = SHINGLE_N) -> set[str]:
    return {" ".join(tokens[i:i + n]) for i in range(max(0, len(tokens) - n + 1))}


def main() -> int:
    urls = routes()
    rows, missing = [], []
    for u in urls:
        f = file_for(u)
        if not f.exists():
            missing.append(u)
            continue
        r = signals(u, f.read_text(encoding="utf-8", errors="replace"))
        r["grade"] = ""
        r["reason"] = ""
        rows.append(r)

    # ---- desk furniture: paragraphs that appear on many pages --------------
    seen = collections.Counter()
    for r in rows:
        for p in {key(x) for x in r["paras"]}:
            seen[p] += 1
    template = {p for p, n in seen.items() if n >= TEMPLATE_MIN_PAGES}
    for r in rows:
        unique = [p for p in r["paras"] if key(p) not in template]
        r["unique_words"] = len(WORDS.findall(" ".join(unique)))
        r["_sh"] = shingles(WORDS.findall(" ".join(unique).lower()))
    removed = sum(1 for r in rows if not r["_sh"])
    template_pct = 100 * (1 - (sum(r["unique_words"] for r in rows)
                               / max(1, sum(r["words"] for r in rows))))

    # ---- inbound internal links across the whole writers tree --------------
    inbound = collections.Counter()
    for r in rows:
        html = (ROOT / r["file"]).read_text(encoding="utf-8", errors="replace")
        for href in HREF.findall(html):
            if href.startswith("/writers/"):
                inbound[href.rstrip("/") + "/"] += 1

    # ---- D: duplicates on UNIQUE text, checked first -----------------------
    for i, a in enumerate(rows):
        if a["grade"]:
            continue
        for b in rows[i + 1:]:
            if b["grade"] or not a["_sh"] or not b["_sh"]:
                continue
            inter = len(a["_sh"] & b["_sh"])
            overlap = inter / min(len(a["_sh"]), len(b["_sh"]))
            if overlap >= DUP_OVERLAP:
                a["grade"] = b["grade"] = "D"
                a["reason"] = f"unique text {overlap:.0%} identical to {b['url']}"
                b["reason"] = f"unique text {overlap:.0%} identical to {a['url']}"
                break

    # ---- A / B / C / E -----------------------------------------------------
    cutoff = (dt.date.today() - dt.timedelta(days=NEW_DAYS)).isoformat()
    for r in rows:
        r["inbound"] = inbound.get(r["url"], 0)
        r["new"] = bool(r["newest_date"] and r["newest_date"] >= cutoff)
        if r["grade"]:
            continue
        w = r["words"]
        # "structured" = has headings OR organises itself some other deliberate way
        h = r["h2"] + r["h3"]
        r["units"] = h + r["dt"] + r["rows"] + r["cards"]
        ext, inb = r["external_links"], r["inbound"]
        if w < 120:
            r["grade"], r["reason"] = "E", f"{w} words of main text"
        elif re.search(r"[?&](page|filter|sort)=", r["url"]):
            r["grade"], r["reason"] = "E", "filter/parameter view of another page"
        elif w < 400:
            r["grade"], r["reason"] = "C", f"{w} words — below the 400 floor"
        elif w < 600 and ext == 0:
            r["grade"], r["reason"] = "C", f"{w} words and cites no outside source"
        elif w >= 900 and r["units"] >= 4 and ext >= 2 and inb >= 3:
            r["grade"], r["reason"] = "A", "long, structured, sourced, linked into"
        else:
            gaps = []
            if w < 900:
                gaps.append(f"{w}w")
            if r["units"] < 4:
                gaps.append(f"{r['units']} organised units")
            if ext < 2:
                gaps.append(f"{ext} outside sources")
            if inb < 3:
                gaps.append(f"{inb} inbound links")
            if r["new"]:
                gaps.append("recently published")
            r["grade"], r["reason"] = "B", "useful; " + ", ".join(gaps)

    counts = collections.Counter(r["grade"] for r in rows)
    out = {
        "generated": TODAY,
        "population": {"urlsInSitemap": len(urls), "built": len(rows),
                       "missingBuild": missing, "newWindowDays": NEW_DAYS,
                       "templateParagraphsRemoved": len(template),
                       "templateShareOfText": round(template_pct, 1),
                       "pagesWithNoUniqueText": removed},
        "grades": {g: counts.get(g, 0) for g in "ABCDE"},
        "newPages": sum(1 for r in rows if r["new"]),
        "totals": {
            "wordsMedian": int(statistics.median([r["words"] for r in rows])),
            "uniqueWordsMedian": int(statistics.median([r["unique_words"] for r in rows])),
            "citesNothing": sum(1 for r in rows if r["external_links"] == 0),
            "noInbound": sum(1 for r in rows if r["inbound"] == 0),
            "noJsonLd": sum(1 for r in rows if not r["has_jsonld"]),
            "thinDesc": sum(1 for r in rows if r["desc_len"] < 60),
        },
        "structureUnits": {r["url"]: r["units"] for r in rows if r["units"] < 3},
        "pages": [{k: v for k, v in r.items() if not k.startswith("_") and k != "paras"}
                  for r in sorted(rows, key=lambda x: (x["grade"], x["words"]))],
    }
    REPORTS.mkdir(exist_ok=True)
    (REPORTS / f"quality-audit-{TODAY}.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"indexable Writers URLs : {len(urls)}   built and audited: {len(rows)}   missing: {len(missing)}")
    print(f"desk furniture removed : {len(template)} paragraphs "
          f"({out['population']['templateShareOfText']}% of all text)")
    print()
    for g, label in (("A", "strong and useful"), ("B", "useful, needs improvement"),
                     ("C", "thin or weak"), ("D", "duplicate/redundant"),
                     ("E", "should probably not remain indexable")):
        print(f"  {g}  {counts.get(g, 0):>4}  {label}")
    t = out["totals"]
    print(f"\nmedian main text {t['wordsMedian']}w   median unique text {t['uniqueWordsMedian']}w")
    print(f"cites nobody {t['citesNothing']}   no inbound links {t['noInbound']}   "
          f"no JSON-LD {t['noJsonLd']}   thin description {t['thinDesc']}")
    print(f"published in last {NEW_DAYS}d: {out['newPages']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
