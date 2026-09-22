#!/usr/bin/env python3
"""Inject the Google Analytics 4 gtag into every published static page.

Why a script and not a hand edit: the tag has to land in every page across
three tiers - ecosystem/ (source of truth), the root desk staging trees, and
public/ (what Render publishes) - which is several thousand files. By hand that
is unauditable and cannot be repeated when a desk is added.

The markup comes from analytics_head.py, the same module the desk generators
import, so an injected page and a regenerated page are byte-identical.

Placement: immediately ahead of the AdSense loader, which is already the first
Google tag on every page. That ordering is the point - the Consent Mode v2
default has to run before any Google tag initialises, because a tag that sees
no default assumes consent was granted. Pages with no AdSense loader fall back
to just before </head>.

Idempotent: a page that already carries the gtag loader is skipped, so this is
safe to re-run after adding pages.

    python3 scripts/inject-analytics.py [--dry]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from analytics_head import LOADER_HOST, ga_head, ga_id  # noqa: E402

SKIP_DIRS = {".git", "node_modules", ".arena", ".cache", "dist", "out"}

# Only published tiers. Deliberately EXCLUDED, with reasons:
#   content/        - body fragments (they begin mid-document with
#                     <div class="crumb">) consumed by build-ecosystem.py,
#                     never served as pages in their own right.
#   reports/, docs/ - internal artifacts, not part of the site.
PUBLISH_TIERS = {
    "ecosystem", "public", "entertainment", "writers", "tech", "home",
    "sports", "fitness", "about",
}
ROOT_PAGES = {"index.html"}

# google2ec8f794263d784f.html and friends are search-engine ownership tokens.
# Their exact contents ARE the verification, so they must never be edited.
VERIFICATION_FILE = re.compile(r"^(?:google|yandex|bing)[0-9a-fA-F_]{6,}\.html$")

ADSENSE_LOADER = re.compile(
    r'<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js[^"]*"[^>]*></script>'
)


def html_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if VERIFICATION_FILE.match(rel.name):
            continue
        if len(rel.parts) == 1:
            if rel.name in ROOT_PAGES:
                out.append(p)
            continue
        if rel.parts[0] in PUBLISH_TIERS:
            out.append(p)
    return sorted(out)


def main() -> int:
    dry = "--dry" in sys.argv
    gid = ga_id(ROOT)
    if not gid:
        print("analytics.gaId missing/disabled in site.config.json - nothing to do")
        return 0

    snippet = ga_head(ROOT)
    injected = skipped = unhandled = 0
    by_tier: dict[str, int] = {}
    problems: list[str] = []

    for f in html_files():
        rel = f.relative_to(ROOT)
        text = f.read_text(encoding="utf-8")
        if LOADER_HOST in text:
            skipped += 1
            continue
        m = ADSENSE_LOADER.search(text)
        if m:
            at = m.start()
        elif "</head>" in text:
            at = text.index("</head>")
        else:
            unhandled += 1
            problems.append(str(rel))
            continue
        if not dry:
            f.write_text(text[:at] + snippet + text[at:], encoding="utf-8")
        injected += 1
        tier = rel.parts[0] if len(rel.parts) > 1 else "(root)"
        by_tier[tier] = by_tier.get(tier, 0) + 1

    print(f"GA4 {gid} - {'would inject' if dry else 'injected'} into {injected} pages, "
          f"{skipped} already had it")
    for tier in sorted(by_tier, key=lambda k: -by_tier[k]):
        print(f"  {tier:16} {by_tier[tier]}")
    if unhandled:
        print(f"  !! {unhandled} page(s) have neither an AdSense loader nor </head>:")
        for p in problems[:15]:
            print(f"     {p}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
