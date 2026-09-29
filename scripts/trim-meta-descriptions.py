#!/usr/bin/env python3
"""
Trim over-length meta descriptions (audit 2026-09-29).

62 indexable pages shipped a <meta name="description"> longer than 170
characters. Google truncates around 155-160, so the tail was wasted, and an
over-long description is a small but real quality signal on review.

This trims at a clean boundary -- the last sentence end that fits, else the
last clause boundary, else the last whole word -- so the result reads as
deliberate prose rather than a chopped string. It never invents text and never
lengthens anything. Nothing else on the page is touched.

Runs across every publish tier so the "public mirror == routed page" gates
stay true. Idempotent. Reports every change so it can be reviewed.

Usage:
  python3 scripts/trim-meta-descriptions.py --report
  python3 scripts/trim-meta-descriptions.py --apply
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIERS = ("ecosystem", "writers", "tech", "home", "sports", "fitness", "money", "")
LIMIT = 170
ROBOTS_RE = re.compile(r'<meta\s+name="robots"\s+content="([^"]*)"', re.I)
# name/content in either order, single or double quotes
DESC_RES = [
    re.compile(r'(<meta\s+name=["\']description["\']\s+content=["\'])(.*?)(["\']\s*/?>)', re.I | re.S),
    re.compile(r'(<meta\s+content=["\'])(.*?)(["\']\s+name=["\']description["\']\s*/?>)', re.I | re.S),
]


def trim(desc: str, limit: int = LIMIT) -> str:
    """Shorten to <= limit chars at the best available boundary."""
    d = " ".join(desc.split())
    if len(d) <= limit:
        return desc
    window = d[: limit + 1]

    # 1. last sentence end
    for m in re.finditer(r"[.!?](?=\s)", window):
        if len(window[: m.end()].rstrip()) >= 110:
            return window[: m.end()].rstrip()
    # 2. last clause boundary
    for ch in ("; ", " — ", " – ", ", "):
        i = window.rfind(ch)
        if i >= 110:
            return window[:i].rstrip().rstrip(",;")
    # 3. last whole word
    i = window.rfind(" ")
    return (window[:i] if i > 0 else window).rstrip()


def patch(text: str) -> tuple[str, str | None, str | None]:
    """Return (new_text, old_desc, new_desc) -- unchanged if nothing to do."""
    for rx in DESC_RES:
        m = rx.search(text)
        if not m:
            continue
        old = m.group(2)
        if len(old) <= LIMIT:
            return text, None, None
        new = trim(old)
        start = m.start(2)
        return text[:start] + new + text[m.end(2):], old, new
    return text, None, None


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--apply", action="store_true")
    g.add_argument("--report", action="store_true")
    a = ap.parse_args()

    seen: set[Path] = set()
    changed = scanned = 0
    for tier in TIERS:
        base = (ROOT / tier) if tier else ROOT
        for f in sorted(base.rglob("index.html")):
            if f in seen or any(p in f.parts for p in
                                (".git", "node_modules", "reports", "content")):
                continue
            seen.add(f)
            text = f.read_text(encoding="utf-8", errors="ignore")
            m = ROBOTS_RE.search(text)
            if m and "noindex" in m.group(1).lower():
                continue
            scanned += 1
            new_text, old, new = patch(text)
            if old is None:
                continue
            changed += 1
            route = "/" + f.parent.relative_to(base).as_posix() + "/"
            if a.report:
                print(f"  {route}\n    - {len(old)}: {old[:120]}...\n    + {len(new)}: {new[:120]}")
            else:
                f.write_text(new_text, encoding="utf-8")

    verb = "would trim" if a.report else "trimmed"
    print(f"trim-meta-descriptions: {verb} {changed} of {scanned} indexable pages")
    if a.report and changed:
        print("\nre-run with --apply to write the changes")


if __name__ == "__main__":
    main()
