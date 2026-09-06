#!/usr/bin/env python3
"""Stage the generated static site (committed at the repo root) into a `public/`
publish directory so Render's static-site deploy has something to serve.

Render's deploy for this service is a static site that publishes from `public/`
(the earlier builds failed with "Publish directory public does not exist").
This script copies the site files that are already generated/committed at the
repo root into ./public, mirroring the publish surface. It only copies files that
exist; it never invents content.
"""
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "public"

# Top-level directories that are part of the published site (all are HTML pages).
PUBLIC_DIRS = [
    "about", "author", "contact", "copyright", "corrections", "disclaimer",
    "editorial-policy", "guides", "privacy", "terms", "tested", "writing", "assets",
    "learn", "tools", "glossary", "templates", "checklists", "problems", "search",
    "verification", "find", "start", "compare", "regional", "intelligence", "tracker", "today", "writing-opportunities", "essays", "read",
]
# Root-level files that belong on the published site.
PUBLIC_FILES = [
    "index.html", "404.html", "410.html", "robots.txt", "sitemap.xml",
    "news-sitemap.xml", "feed.xml", "favicon.ico", "manifest.webmanifest",
    "sw.js", "google2ec8f794263d784f.html", "yandex_78fdd841f95fa2e1.html",
    "1740cdb82c02b9af13911b38c853e85d2f708322fa0c2c55.txt", "_redirects",
]

PUB.mkdir(exist_ok=True)
copied = 0
for name in PUBLIC_DIRS:
    src = ROOT / name
    if src.is_dir():
        dst = PUB / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        copied += 1
for name in PUBLIC_FILES:
    src = ROOT / name
    if src.is_file():
        shutil.copy2(src, PUB / name)
        copied += 1

print(f"staged public/: {copied} items")
