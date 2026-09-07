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

# Top-level directories that are part of the published site. The explicit
# floor covers dirs without their own index.html (assets); everything else is
# auto-discovered so a newly built page dir can never be forgotten again
# (2026-09-07: /disclosure/ shipped while unstaged — third time this class of
# bug bit, so the list became code).
PUBLIC_DIRS = [
    "about", "author", "contact", "copyright", "corrections", "disclaimer",
    "editorial-policy", "guides", "privacy", "terms", "tested", "writing", "assets",
    "learn", "tools", "glossary", "templates", "checklists", "problems", "search",
    "verification", "find", "start", "compare", "regional", "intelligence", "tracker", "today", "writing-opportunities", "essays", "read",
    "newsletter", "opportunities", "jobs", "make-money", "tech",
]
AUTO_EXCLUDE = {".git", "node_modules", "public", "content", "docs", "scripts", "server", "reports"}
_auto = sorted(
    d.name for d in ROOT.iterdir()
    if d.is_dir() and d.name not in AUTO_EXCLUDE and (d / "index.html").is_file()
)
_auto_added = [n for n in _auto if n not in PUBLIC_DIRS]
PUBLIC_DIRS = sorted(set(PUBLIC_DIRS) | set(_auto))
if _auto_added:
    print("public-dir: auto-staged new page dirs:", ", ".join(_auto_added))
# Root-level files that belong on the published site.
PUBLIC_FILES = [
    "index.html", "404.html", "410.html", "robots.txt", "sitemap.xml",
    "news-sitemap.xml", "feed.xml", "favicon.ico", "manifest.webmanifest",
    "sw.js", "google2ec8f794263d784f.html", "yandex_78fdd841f95fa2e1.html",
    "1740cdb82c02b9af13911b38c853e85d2f708322fa0c2c55.txt", "_redirects",
]

PUB.mkdir(exist_ok=True)
# Assertion: every route in the sitemap must stage into public/. This turns
# "built but never published" from a silent deploy defect into a build failure.
import re as _re
_sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
_missing = set()
for _u in _re.findall(r"<loc>([^<]+)</loc>", _sm):
    _path = _u.split(BASE_URL_HINT, 1)[-1] if False else _u
    _seg = _re.sub(r"^[a-z]+://[^/]+", "", _u).strip("/")
    if _seg and not _seg.startswith("assets/"):
        _top = _seg.split("/", 1)[0]
        if _top not in PUBLIC_DIRS and _top not in [f.split(".")[0] for f in PUBLIC_FILES]:
            _missing.add(_top)
if _missing:
    raise SystemExit(f"public-dir: sitemap routes under un-staged top-level dirs: {sorted(_missing)}")
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
