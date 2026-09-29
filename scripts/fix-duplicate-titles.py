#!/usr/bin/env python3
"""
Fix the duplicate <title> collisions found in the 2026-09-29 AdSense audit.

Two articles were shipping their *category hub's* short name as their own
<title>, so each collided with the hub page:

  /fitness/start/                          (hub)     "Starting from zero | BRYME Fitness"
  /fitness/how-to-start-working-out/       (article) "Starting from zero | BRYME Fitness"

  /tech/refurbished-vs-new-tech/                     "Refurbished vs new | BRYME Tech"
  /tech/refurbished-vs-new-the-warranty-math/        "Refurbished vs new | BRYME Tech"

The hub legitimately keeps the category name -- it IS the category. The article
gets its own descriptive title, taken from what the page already says about
itself (its H1), so nothing is invented.

Updates <title>, og:title and twitter:title together. Applies to every publish
tier so the "public mirror == routed page" gates stay true. Idempotent.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIERS = ("ecosystem", "", "public")   # "" is the repo root

# route -> (old base title, new title). The hub pages are deliberately absent:
# they keep the category name that is correctly theirs.
FIXES: dict[str, tuple[str, str]] = {
    "/fitness/how-to-start-working-out/": (
        "Starting from zero",
        "How to start working out from zero | BRYME Fitness",
    ),
    "/tech/refurbished-vs-new-the-warranty-math/": (
        "Refurbished vs new",
        "Refurbished vs new: the warranty maths | BRYME Tech",
    ),
    "/tech/refurbished-vs-new-tech/": (
        "Refurbished vs new",
        "When refurbished tech is the smarter buy | BRYME Tech",
    ),
}

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)


def tier_file(tier: str, route: str) -> Path:
    sub = (Path(tier) / route.strip("/")) if tier else Path(route.strip("/"))
    return ROOT / sub / "index.html"


def patch(text: str, old: str, new: str) -> tuple[str, int]:
    n = 0

    def _t(m: re.Match[str]) -> str:
        nonlocal n
        if m.group(1).strip().startswith(old):
            n += 1
            return f"<title>{new}</title>"
        return m.group(0)

    text = TITLE_RE.sub(_t, text, count=1)

    # keep the social cards in step with the <title>
    for prop in ('property="og:title"', 'name="twitter:title"'):
        pat = re.compile(
            rf'(<meta\s+{re.escape(prop)}\s+content=")([^"]*)(")', re.I)

        def _c(m: re.Match[str]) -> str:
            nonlocal n
            if m.group(2).strip().startswith(old):
                n += 1
                return f"{m.group(1)}{new}{m.group(3)}"
            return m.group(0)

        text = pat.sub(_c, text, count=1)

    return text, n


def main() -> None:
    total = 0
    for route, (old, new) in sorted(FIXES.items()):
        for tier in TIERS:
            f = tier_file(tier, route)
            if not f.is_file():
                continue
            text = f.read_text(encoding="utf-8")
            patched, n = patch(text, old, new)
            if patched != text:
                f.write_text(patched, encoding="utf-8")
                total += n
                print(f"  {tier or '(root)':10s} {route}")
    print(f"fix-duplicate-titles: {total} tag writes across {len(TIERS)} tiers")
    if total == 0:
        print("fix-duplicate-titles: nothing to do (already applied)")


if __name__ == "__main__":
    main()
