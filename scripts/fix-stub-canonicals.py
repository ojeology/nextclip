#!/usr/bin/env python3
"""Repoint the canonical on "moved" redirect stubs at the page they now point to.

Why this exists (2026-09-29): six legacy stubs under /writers/ carry
robots=noindex,follow and a visible "This page moved" body linking to the
current page, but their canonical still names *themselves*. A self-canonical on
a redirect stub tells Google "this URL is the original", which contradicts both
the redirect and the noindex -- and it is the one combination that keeps a dead
URL competing with the live page it forwards to.

Safe by construction:
  - only touches pages that are noindex AND look like move stubs
    (meta http-equiv=refresh, or an h1 containing "moved")
  - only when the canonical currently points at the page itself
  - only when the body links to exactly one distinct internal route
  - never touches genuine noindex tools/pages (e.g. /writers/search/, whose
    h1 is "Search BRYME." and which correctly canonicals to itself)
Idempotent: a stub whose canonical already names the destination is skipped.
Mirrors every change across the publish tiers so the byte-identical gates hold.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIERS = ("public", "ecosystem", "writers", "tech", "sports", "entertainment",
         "fitness", "home", "money")
ORIGIN = "https://thebryme.com"

CANON_RE = re.compile(r'(<link[^>]+rel=["\']canonical["\'][^>]*href=["\'])([^"\']+)(["\'])', re.I)
OGURL_RE = re.compile(r'(<meta[^>]+property=["\']og:url["\'][^>]*content=["\'])([^"\']+)(["\'])', re.I)
ROBOTS_RE = re.compile(r'<meta[^>]+name=["\']robots["\'][^>]*content=["\']([^"\']*)', re.I)
MAIN_RE = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S | re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
REFRESH_RE = re.compile(r'http-equiv=["\']refresh["\'][^>]*url=([^"\'>\s]+)', re.I)


def is_move_stub(html: str) -> bool:
    if "noindex" not in (ROBOTS_RE.search(html).group(1) if ROBOTS_RE.search(html) else ""):
        return False
    if REFRESH_RE.search(html):
        return True
    m = H1_RE.search(html)
    return bool(m and re.search(r"\bmoved\b", re.sub(r"<[^>]+>", "", m.group(1)), re.I))


def link_targets(html: str) -> list[str]:
    m = MAIN_RE.search(html)
    if not m:
        return []
    out, seen = [], set()
    for href in re.findall(r'href=["\'](/[^"\'#?]*)["\']', m.group(1)):
        if not href.endswith("/") and "." not in os.path.basename(href):
            href += "/"
        if href not in seen:
            seen.add(href)
            out.append(href)
    return out


def main() -> int:
    checked = fixed = skipped = problems = 0
    for tier in TIERS:
        base = ROOT / tier
        if not base.is_dir():
            continue
        for root, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in ("node_modules", "_recovered", ".git")]
            if "index.html" not in files:
                continue
            f = Path(root) / "index.html"
            html = f.read_text(encoding="utf-8", errors="replace")
            checked += 1
            if not is_move_stub(html):
                continue
            cm = CANON_RE.search(html)
            if not cm:
                continue
            own = ORIGIN + "/" + os.path.relpath(root, base).replace(os.sep, "/") + "/"
            own = own.replace("/./", "/")
            if cm.group(2).rstrip("/") != own.rstrip("/"):
                skipped += 1          # already points elsewhere: nothing to do
                continue
            targets = link_targets(html)
            if len(targets) != 1:
                problems += 1
                print(f"  !! {tier}/: {os.path.relpath(root, base)}/ links to {len(targets)} routes - left alone")
                continue
            dest = ORIGIN + targets[0]
            new = CANON_RE.sub(lambda m: m.group(1) + dest + m.group(3), html, count=1)
            new = OGURL_RE.sub(lambda m: m.group(1) + dest + m.group(3), new, count=1)
            if new != html:
                f.write_text(new, encoding="utf-8")
                fixed += 1

    print(f"stub-canonicals: {fixed} repointed, {skipped} already correct, "
          f"{problems} ambiguous (routes {checked})")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
