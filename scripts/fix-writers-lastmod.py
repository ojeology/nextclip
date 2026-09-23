#!/usr/bin/env python3
"""Post-build: give every writers URL its own real lastmod.

build-routing.py writes the writers sitemap while article files are still
being routed into place, so its per-page date extraction can only see the
hand-authored property pages (the articles have not landed under
public/writers/ yet). After build-public-dir.py the finished pages exist,
so this step reads each page's JSON-LD dates and rewrites <lastmod> per
URL. Fallback: keep the value the build wrote (today for freshly built
articles) - never invent a date.

Also refreshes the writers <lastmod> in the sitemap index files so the
index always reports the max of the child's real per-URL values.
"""
import re
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
DATE_RE = re.compile(r'"date(?:Modified|Published)": ?"(\d{4}-\d{2}-\d{2})')
ORIGIN = "https://thebryme.com"


def main() -> int:
    sm_path = PUB / "writers" / "sitemap.xml"
    text = sm_path.read_text(encoding="utf-8")
    urls = re.findall(r"<url><loc>(.*?)</loc><lastmod>(.*?)</lastmod></url>", text)
    if len(urls) < 400:
        sys.exit(f"fix-writers-lastmod: only {len(urls)} urls found - unexpected tree, aborting")
    changed = 0
    real = 0
    for loc, old_lm in urls:
        route = loc.split(ORIGIN, 1)[1].strip("/")
        pf = PUB / route / "index.html"
        new_lm = old_lm
        if pf.is_file():
            m = DATE_RE.search(pf.read_text(encoding="utf-8", errors="replace"))
            if m:
                new_lm = m.group(1)
                real += 1
        if new_lm != old_lm:
            old = f"<loc>{loc}</loc><lastmod>{old_lm}</lastmod>"
            new = f"<loc>{loc}</loc><lastmod>{new_lm}</lastmod>"
            assert text.count(old) == 1, f"expected exactly one entry for {loc}"
            text = text.replace(old, new)
            changed += 1
    sm_path.write_text(text, encoding="utf-8")
    (ROOT / "writers" / "sitemap.xml").write_text(text, encoding="utf-8")
    lms = re.findall(r"<lastmod>(.*?)</lastmod>", text)
    if lms:
        mx = max(lms)
        child = f"{ORIGIN}/writers/sitemap.xml"
        for idxp in (ROOT / "sitemap.xml", PUB / "sitemap.xml", PUB / "sitemap_index.xml"):
            if not idxp.is_file():
                continue
            t2 = idxp.read_text(encoding="utf-8")
            t2, n = re.subn(
                r"(<loc>" + re.escape(child) + r"</loc><lastmod>)[^<]+(</lastmod>)",
                lambda m: m.group(1) + mx + m.group(2),
                t2,
            )
            if n:
                idxp.write_text(t2, encoding="utf-8")
    print(f"fix-writers-lastmod: {len(urls)} urls, {real} with real JSON-LD dates, {changed} lastmods corrected")


if __name__ == "__main__":
    sys.exit(main())
