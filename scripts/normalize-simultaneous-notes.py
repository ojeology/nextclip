#!/usr/bin/env python3
"""Normalise the three simultaneous notes that use a hyphen before the source URL.

The dataset's convention, set when the field was backfilled in batch 13, is:

    <verbatim sentence> — <url> (read <date>)

Three records carried " - https" instead of " — https": brick-a-literary-journal,
bracken and metphrastics. They were left alone at the time as pre-existing drift.
They are corrected here because they are the only three of 164 notes that break
the convention, and a reader scanning the field sees the difference.

WHAT THIS SCRIPT WILL NOT DO
----------------------------
It touches nothing but the separator. It does not add, remove or rewrite any
word of the quoted sentence, the URL, or the read date, and it refuses to run if
the count of affected records is anything other than the three named here - so a
reenvisioned record cannot be silently normalised along with them.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"

EXPECTED = {"brick-a-literary-journal", "bracken", "metphrastics"}
# a hyphen (with spaces) immediately before an http URL, inside the note only
PATTERN = re.compile(r"\s-\s+(?=https?://)")


def main() -> int:
    data = json.loads(OPPS.read_text(encoding="utf-8"))
    opps = data["opportunities"]

    targets = [r for r in opps if r.get("simultaneousNote") and PATTERN.search(r["simultaneousNote"])]
    found = {r["slug"] for r in targets}
    if found != EXPECTED:
        sys.exit(f"ERROR: expected exactly {sorted(EXPECTED)}, found {sorted(found)}; refusing to run")

    for r in targets:
        note = r["simultaneousNote"]
        fixed, n = PATTERN.subn(" — ", note)
        if n != 1:
            sys.exit(f"ERROR: {r['slug']} had {n} separators to fix, expected 1")
        # Nothing but the separator may change. Strip either separator from both
        # sides before comparing, or the em-dash in the fixed text counts as a
        # difference and the guard fires on its own repair.
        strip = lambda s: re.sub(r"\s[—-]\s+(?=https?://)", "", s)
        if strip(note) != strip(fixed):
            sys.exit(f"ERROR: {r['slug']} would change more than the separator")
        if " - https" in fixed or " — https" not in fixed:
            sys.exit(f"ERROR: {r['slug']} still malformed after the fix")
        r["simultaneousNote"] = fixed
        print(f"normalised {r['slug']}")

    data["opportunities"] = opps
    OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OPPS.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
