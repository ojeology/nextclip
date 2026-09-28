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
from sub8_depth_data7 import DEPTH_SECTIONS7  # noqa: E402
from sub8_depth_data8 import DEPTH_SECTIONS8  # noqa: E402
from sub8_depth_data9 import DEPTH_SECTIONS9, TOPUP_SECTIONS9  # noqa: E402
from sub8_depth_data10 import DEPTH_SECTIONS10, TOPUP_SECTIONS10  # noqa: E402
from sub8_depth_data11 import DEPTH_SECTIONS11, TOPUP_SECTIONS11  # noqa: E402

DEPTH_SECTIONS = {**DEPTH_SECTIONS, **DEPTH_SECTIONS2, **DEPTH_SECTIONS3, **DEPTH_SECTIONS4, **DEPTH_SECTIONS5, **DEPTH_SECTIONS6, **DEPTH_SECTIONS7, **DEPTH_SECTIONS8, **DEPTH_SECTIONS9, **DEPTH_SECTIONS10, **DEPTH_SECTIONS11}
TOPUP_SECTIONS = {**TOPUP_SECTIONS9, **TOPUP_SECTIONS10, **TOPUP_SECTIONS11}
TOPUP_MARK = 'data-esrc="t8b"'

MARK = 'data-esrc="t8"'
BASES = (ROOT, PUB)


def _inject(sections: dict, mark: str, label: str) -> int:
    applied = skipped = problems = 0
    for route, html in sorted(sections.items()):
        hit = False
        for base in BASES:
            f = base / route / "index.html"
            if not f.is_file():
                continue
            hit = True
            t = f.read_text(encoding="utf-8")
            if mark in t:
                skipped += 1
                continue
            if t.count("</main>") != 1:
                print(f"  !! {label}: ambiguous main on {base}/{route}/")
                problems += 1
                continue
            t = t.replace(
                "</main>",
                '<section class="section" ' + mark + '><div class="prose">' + html + "</div></section></main>",
                1,
            )
            f.write_text(t, encoding="utf-8")
            applied += 1
        if not hit:
            print(f"  !! {label}: missing page {route}/")
            problems += 1
    print(f"{label}: {applied} injected, {skipped} already present, {problems} problems "
          f"(routes {len(sections)}, trees {len(BASES)})")
    return problems


def main() -> None:
    problems = _inject(DEPTH_SECTIONS, MARK, "sub8-depth")
    if TOPUP_SECTIONS:
        problems += _inject(TOPUP_SECTIONS, TOPUP_MARK, "sub8-topup")
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
