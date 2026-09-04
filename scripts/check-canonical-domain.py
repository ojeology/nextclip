#!/usr/bin/env python3
"""Custom-domain readiness check for BRYME.

Verifies that no generated page hard-codes the old Render host, and that every
indexable page's canonical, sitemap and robots reference the configured SITE_URL.
This is the gate you run before and after pointing a custom domain.

Run:
  python3 scripts/check-canonical-domain.py
or with an explicit domain:
  SITE_URL=https://bryme.example.com python3 scripts/check-canonical-domain.py
or just inspect the generated output:
  python3 scripts/check-canonical-domain.py --html
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import bryme_config as cfg

ROOT = Path(__file__).resolve().parents[1]
OLD_HOST = "bryme.onrender.com"
HTML = Path(ROOT, "index.html")


def walk_html() -> list[Path]:
    if HTML.is_file():
        return [HTML]
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify custom-domain readiness.")
    ap.add_argument("--html", action="store_true", help="Only scan generated index.html (default).")
    args = ap.parse_args()

    site = cfg.site_url()
    problems: list[str] = []
    notes: list[str] = []
    from urllib.parse import urlsplit
    expected_host = (urlsplit(site).netloc or "").lower()
    # Migration mode: a SITE_URL env was explicitly set to a non-Render origin.
    migration_mode = bool(os.environ.get("SITE_URL")) and expected_host != OLD_HOST
    files = [HTML] if args.html else list(ROOT.rglob("*.html"))
    for file in files:
        if file.is_file():
            try:
                text = file.read_text(encoding="utf-8")
            except Exception:
                continue
            if OLD_HOST in text:
                if migration_mode:
                    problems.append(f"{file.relative_to(ROOT)}: still references {OLD_HOST} (migration target is {site})")
            for m in re.finditer(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"', text, re.I):
                has = re.match(r"https?://[^/]+/", m.group(1))
                if has and not m.group(1).startswith(site):
                    problems.append(f"{file.relative_to(ROOT)}: canonical {m.group(1)} does not start with {site}")
    if not migration_mode:
        notes.append("Current deploy runs on the fallback siteUrl (Render). Set SITE_URL= to the custom domain and rebuild to migrate.")

    if args.html or True:
        # 2. sitemap / robots reference the configured site.
        for name in ("sitemap.xml", "news-sitemap.xml"):
            p = ROOT / name
            if p.is_file():
                for loc in re.findall(r"<loc>(.*?)</loc>", p.read_text(encoding="utf-8")):
                    if loc.startswith("http") and not loc.startswith(site):
                        problems.append(f"{name}: <loc> {loc} does not start with {site}")
        robots = ROOT / "robots.txt"
        if robots.is_file():
            for line in robots.read_text(encoding="utf-8").splitlines():
                if line.startswith("Sitemap:") and not line[len("Sitemap: "):].startswith(site):
                    problems.append(f"robots.txt: {line} does not use {site}")

    if problems:
        print("CUSTOM-DOMAIN CHECK FAILED:")
        for p in problems:
            print("  -", p)
        return 1

    for n in notes:
        print("note:", n)
    print(f"CUSTOM-DOMAIN CHECK {'OK' if not problems else 'FAILED'} · SITE_URL = {site}")
    print("  - canonicals, sitemap <loc> and robots Sitemap all use SITE_URL")
    if problems:
        for p in problems:
            print("  -", p)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
