#!/usr/bin/env python3
"""Sweep every internal href in the BUILT site and verify it resolves.

Why this exists: the quality validators check front-matter `related:` /
`tools:` slots and structure, but raw body links were a blind spot — a
dead /learn/writing-basics/how-to-cite-sources/ slug shipped and lived
on the live site for days. This script reads public/**/*.html directly,
so nothing that renders can dodge it. It runs at the end of `npm run
build` (see package.json) and fails the build on any broken link.

Scope: internal path links (/...) and same-canonical-domain absolute
URLs. External http(s) links are out of scope here (they need network;
checked editorially per the YMYL source rules).
"""
import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
CANONICAL_HOST = "bryme.onrender.com"

HREF = re.compile(r"""href=["']([^"']+)["']""")


def resolves(path: str) -> bool:
    """True if a built file exists for this site path."""
    if path.endswith("/"):
        return (PUBLIC / path.lstrip("/") / "index.html").is_file()
    base = PUBLIC / path.lstrip("/")
    return (
        (base / "index.html").is_file()
        or base.is_file()
        or Path(str(base) + ".html").is_file()
    )


def internal_path(raw: str):
    """Normalise an href to a checkable site path, or None to skip."""
    href = html.unescape(raw).strip()
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    if href.startswith(("http://", "https://")):
        u = urlparse(href)
        if u.netloc != CANONICAL_HOST:
            return None  # external link, out of scope
        path = u.path
    else:
        if not href.startswith("/"):
            return None  # relative links are not used by the build
        path = href
    path = unquote(path.split("#", 1)[0].split("?", 1)[0])
    return path or None


def main() -> int:
    if not PUBLIC.is_dir():
        print(f"check-links: {PUBLIC} missing — run the build first")
        return 1

    pages = 0
    checked = 0
    broken: dict = {}
    for page in sorted(PUBLIC.rglob("*.html")):
        pages += 1
        text = page.read_text(encoding="utf-8", errors="replace")
        for m in HREF.finditer(text):
            path = internal_path(m.group(1))
            if path is None:
                continue
            checked += 1
            if not resolves(path):
                key = str(page.relative_to(PUBLIC))
                broken.setdefault(key, set()).add(path)

    if broken:
        total_targets = sum(len(v) for v in broken.values())
        print(f"check-links: FAILED — {total_targets} broken internal link(s) "
              f"on {len(broken)} page(s):")
        for src in sorted(broken):
            for target in sorted(broken[src]):
                print(f"  {src}  ->  {target}")
        return 1

    print(f"check-links: OK — {checked} internal links across {pages} pages, "
          f"all resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
