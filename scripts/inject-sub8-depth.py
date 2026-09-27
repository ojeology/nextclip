#!/usr/bin/env python3
"""Inject editorial depth sections into the last sub-8 pages (Phase 3 step 3).

These pages fail on word count and/or structure, not on a missing citation, so
each block carries real prose plus an h2, a list, internal links, a visible
review date and one verified external reference.

Writes into BOTH the property source tree and the published mirror (public/),
because build-routing.py mirrors public/ inside its own run.
Idempotent by marker; fail-closed on missing pages or ambiguous <main>.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
sys.path.insert(0, str(Path(__file__).parent))
from sub8_depth_data import DEPTH_SECTIONS  # noqa: E402
from sub8_depth_data2 import DEPTH_SECTIONS2  # noqa: E402
from sub8_depth_data3 import DEPTH_SECTIONS3  # noqa: E402
from sub8_depth_data4 import DEPTH_SECTIONS4  # noqa: E402
from sub8_depth_data5 import DEPTH_SECTIONS5  # noqa: E402
from sub8_depth_data6 import DEPTH_SECTIONS6  # noqa: E402

DEPTH_SECTIONS = {**DEPTH_SECTIONS, **DEPTH_SECTIONS2, **DEPTH_SECTIONS3, **DEPTH_SECTIONS4, **DEPTH_SECTIONS5, **DEPTH_SECTIONS6}

MARK = 'data-esrc="t8"'
BASES = (ROOT, PUB)


def main() -> None:
    applied = skipped = problems = 0
    for route, html in sorted(DEPTH_SECTIONS.items()):
        hit = False
        for base in BASES:
            f = base / route / "index.html"
            if not f.is_file():
                continue
            hit = True
            t = f.read_text(encoding="utf-8")
            if MARK in t:
                skipped += 1
                continue
            if t.count("</main>") != 1:
                print(f"  !! sub8-depth: ambiguous main on {base}/{route}/")
                problems += 1
                continue
            t = t.replace(
                "</main>",
                '<section class="section" ' + MARK + '><div class="prose">' + html + "</div></section></main>",
                1,
            )
            f.write_text(t, encoding="utf-8")
            applied += 1
        if not hit:
            print(f"  !! sub8-depth: missing page {route}/")
            problems += 1
    print(f"sub8-depth: {applied} injected, {skipped} already present, {problems} problems "
          f"(routes {len(DEPTH_SECTIONS)}, trees {len(BASES)})")
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
