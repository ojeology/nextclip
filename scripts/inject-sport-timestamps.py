#!/usr/bin/env python3
"""A8 sport-timestamping program: every indexable /sports/ page carries a visible
reviewed-date stamp (house phrasing: "By the Bryme Sports desk. Reviewed 28 September 2026.").
Idempotent by marker; skip noindex; only touches pages missing a visible date stamp.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
BASES = (ROOT, PUB)
MARK = 'data-esrc="ts"'
DATE_RE = re.compile(
    r"(Reviewed|Updated|Checked|checked|verified|dated)\s*(on\s*)?"
    r"(20\d\d|January|February|March|April|May|June|July|August|September|October|November|December)",
)
STAMP = '<p class="byline" ' + MARK + '>By the Bryme Sports desk. Reviewed 28 September 2026.</p>'

applied = skipped = 0
for base in BASES:
    sports = base / "sports"
    if not sports.is_dir():
        continue
    for f in sorted(sports.rglob("index.html")):
        t = f.read_text(encoding="utf-8")
        if 'content="noindex' in t:
            continue
        if MARK in t:
            skipped += 1
            continue
        m = re.search(r"<main\b[^>]*>(.*)</main>", t, re.S | re.I)
        if not m:
            continue
        body = m.group(1)
        if DATE_RE.search(re.sub(r"<[^>]+>", " ", body)):
            skipped += 1
            continue
        if t.count("</main>") != 1:
            continue
        t = t.replace("</main>", STAMP + "</main>", 1)
        f.write_text(t, encoding="utf-8")
        applied += 1

print(f"sport-timestamps: {applied} stamped, {skipped} already dated/noindex")
