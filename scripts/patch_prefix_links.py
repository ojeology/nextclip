#!/usr/bin/env python3
"""One-shot repair: give tech/fitness related-link hrefs their property prefix.

Why this exists
---------------
build-routing.py::rewrite_prop_paths() is the pass that turns a property's
root-absolute hrefs (/slug/) into prefixed ones (/tech/slug/). But
build-routing.py is one-shot: on an already-routed tree it aborts with exit 1
("tree is already routed") before it ever copies ecosystem/<prop> into <prop>/.
So every page authored since routing last ran ships its "Related on this desk"
links unprefixed, which 404 in production.

Verified blast radius before this patch: 67 broken links across 14 files
    fitness   40 links /  5 files
    tech      27 links /  9 files
    sports, entertainment, home: 0   (home already routes through _hurl())

Line-anchored on purpose: sports_pages() and entertainment_pages() contain
byte-identical rel_html lines that must NOT change, because those properties
currently resolve at the root.

Run: python3 scripts/patch_prefix_links.py [--check]
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = "--check" in sys.argv

DQ = chr(34)  # double quote
NEEDLE = "href=" + DQ + "/"          # href="/
GUARD = "rel_html"                   # every target line is a rel_html builder

# line -> property prefix to insert
PREFIX_LINE = {2823: "tech", 3067: "fitness"}

# line -> (old literal, new literal) for the hard-coded fitness hub links
LITERAL_LINE = {
    3337: ("/exercise-library/",    "/fitness/exercise-library/"),
    3340: ("/fitness-calculators/", "/fitness/fitness-calculators/"),
    3343: ("/1rm-calculator/",      "/fitness/1rm-calculator/"),
    3346: ("/workout-builder/",     "/fitness/workout-builder/"),
}


def main() -> int:
    target = ROOT / "scripts" / "build-ecosystem.py"
    lines = target.read_text(encoding="utf-8").split("\n")
    problems: list[str] = []
    changed = 0

    for lineno, prop in sorted(PREFIX_LINE.items()):
        line = lines[lineno - 1]
        want = NEEDLE + prop + "/"
        if GUARD not in line:
            problems.append(f"line {lineno}: not a {GUARD} line -> {line.strip()[:110]}")
        elif want in line:
            print(f"  skip line {lineno}: already prefixed /{prop}/")
        elif NEEDLE not in line:
            problems.append(f"line {lineno}: no {NEEDLE} -> {line.strip()[:110]}")
        else:
            lines[lineno - 1] = line.replace(NEEDLE, want, 1)
            changed += 1
            print(f"  patched line {lineno}: {NEEDLE} -> {want}  ({prop}_pages related links)")

    for lineno, (old, new) in sorted(LITERAL_LINE.items()):
        line = lines[lineno - 1]
        o = "href=" + DQ + old + DQ
        n = "href=" + DQ + new + DQ
        if n in line:
            print(f"  skip line {lineno}: already patched")
        elif o not in line:
            problems.append(f"line {lineno}: {o} absent -> {line.strip()[:110]}")
        else:
            lines[lineno - 1] = line.replace(o, n, 1)
            changed += 1
            print(f"  patched line {lineno}: {old} -> {new}")

    if problems:
        print("\nABORTED, nothing written:")
        for p in problems:
            print("  !", p)
        return 1

    if CHECK:
        print(f"\n--check: {changed} line(s) would change")
        return 0
    if changed:
        target.write_text("\n".join(lines), encoding="utf-8")
        print(f"\nwrote scripts/build-ecosystem.py ({changed} line(s))")
    else:
        print("\nno change needed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
