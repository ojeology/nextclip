#!/usr/bin/env python3
"""Inject external source notes (Phase 3 step 1: pages scoring 9.75 whose only
missing point is no-external-source).

Writes into BOTH the property source tree (tech/, entertainment/, ...) and the
published mirror (public/...), because build-routing.py mirrors public/ inside
its own run. Runs last among the injectors so nothing re-stages over the marks.
Idempotent by marker; fail-closed on missing pages or ambiguous <main>.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
sys.path.insert(0, str(Path(__file__).parent))
from external_source_data import EXTERNAL_SOURCES  # noqa: E402
from external_source_data2 import EXTERNAL_SOURCES2  # noqa: E402
from external_source_data3 import EXTERNAL_SOURCES3  # noqa: E402
from external_source_data4 import EXTERNAL_SOURCES4  # noqa: E402

EXTERNAL_SOURCES = {**EXTERNAL_SOURCES, **EXTERNAL_SOURCES2, **EXTERNAL_SOURCES3, **EXTERNAL_SOURCES4}

MARK = 'data-esrc="t7"'
BASES = (ROOT, PUB)


def main() -> None:
    applied = skipped = problems = 0
    for route, html in sorted(EXTERNAL_SOURCES.items()):
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
                print(f"  !! ext-source: ambiguous main on {base}/{route}/")
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
            print(f"  !! ext-source: missing page {route}/")
            problems += 1
    print(f"ext-source: {applied} injected, {skipped} already present, {problems} problems "
          f"(routes {len(EXTERNAL_SOURCES)}, trees {len(BASES)})")
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
