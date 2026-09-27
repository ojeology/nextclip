#!/usr/bin/env python3
"""Inject writers-desk depth sections (Phase 3 tranche 5).

Two idempotent-plus passes, written into BOTH the routed source tree (writers/)
and the published mirror (public/writers/), because build-routing.py mirrors
public/ from the routed tree inside its own run and build-public-dir.py does not
re-stage writers/. Must run AFTER inject-sources.py so nothing re-stages over
the marks. Fail-closed: a page missing from both trees, or with an ambiguous
<main>, aborts the build.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
sys.path.insert(0, str(Path(__file__).parent))
from writers_depth_data import WRITERS_DEPTH  # noqa: E402
from writers_depth_data2 import WRITERS_DEPTH2  # noqa: E402
from writers_depth_data3 import WRITERS_DEPTH3  # noqa: E402
from writers_depth_data4 import WRITERS_DEPTH4  # noqa: E402

BASES = (ROOT, PUB)


def inject(depth: dict, mark: str) -> tuple:
    applied = skipped = problems = 0
    for route, html in sorted(depth.items()):
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
                print(f"  !! writers-depth: ambiguous main on {base.name}/{route}/")
                problems += 1
                continue
            t = t.replace("</main>", '<section class="section" ' + mark + ">" + html + "</section></main>", 1)
            f.write_text(t, encoding="utf-8")
            applied += 1
        if not hit:
            print(f"  !! writers-depth: missing page {route}/")
            problems += 1
    return applied, skipped, problems


def main() -> None:
    results = []
    for depth, mark in ((WRITERS_DEPTH, 'data-wdepth="t5"'),
                        (WRITERS_DEPTH2, 'data-wdepth="t5b"'),
                        (WRITERS_DEPTH3, 'data-wdepth="t5c"'),
                        (WRITERS_DEPTH4, 'data-wdepth="t5d"')):
        results.append(inject(depth, mark))
    tot = [sum(r[i] for r in results) for i in range(3)]
    print(f"writers-depth: {tot[0]} injected, {tot[1]} already present, {tot[2]} problems "
          f"(routes {len(WRITERS_DEPTH)}, trees {len(BASES)})")
    if tot[2]:
        sys.exit(1)


if __name__ == "__main__":
    main()
