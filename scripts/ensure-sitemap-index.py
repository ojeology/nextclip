#!/usr/bin/env python3
"""Ensure the separated entertainment catalogue is in the root sitemap index.

The catalogue has its own sitemap for maintainability, but remains part of the
indexable URL architecture. This final build step runs after routing and public
mirroring, so a cached/generated root sitemap cannot silently omit it.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRY = '<sitemap><loc>https://thebryme.com/entertainment/sitemap-catalogue.xml</loc><lastmod>2026-09-27</lastmod></sitemap>'

for path in (ROOT / "sitemap.xml", ROOT / "public" / "sitemap.xml"):
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    if "sitemap-catalogue.xml" not in text and "</sitemapindex>" in text:
        text = text.replace("</sitemapindex>", ENTRY + "</sitemapindex>")
        path.write_text(text, encoding="utf-8")
        print(f"sitemap-index: registered catalogue in {path.relative_to(ROOT)}")
