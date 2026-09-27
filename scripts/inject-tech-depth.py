#!/usr/bin/env python3
"""Inject BRYME Tech depth sections (Phase 3 tranche 6).

Writes into BOTH the tech/ source tree and the public/tech/ mirror, because
build-routing.py mirrors public/ inside its own run. Runs after inject-sources.py
so nothing re-stages over the marks. Idempotent by marker; fail-closed.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
sys.path.insert(0, str(Path(__file__).parent))
from tech_depth_data import TECH_DEPTH  # noqa: E402

MARK = 'data-tdepth="t6"'
BASES = (ROOT / "tech", PUB / "tech")


def main() -> None:
    applied = skipped = problems = 0
    for slug, html in sorted(TECH_DEPTH.items()):
        hit = False
        for base in BASES:
            f = base / slug / "index.html"
            if not f.is_file():
                continue
            hit = True
            t = f.read_text(encoding="utf-8")
            if MARK in t:
                skipped += 1
                continue
            if t.count("</main>") != 1:
                print(f"  !! tech-depth: ambiguous main on {base}/{slug}/")
                problems += 1
                continue
            t = t.replace("</main>", '<section class="section" ' + MARK + "><div class=\"prose\">" + html + "</div></section></main>", 1)
            f.write_text(t, encoding="utf-8")
            applied += 1
        if not hit:
            print(f"  !! tech-depth: missing page {slug}/")
            problems += 1
    print(f"tech-depth: {applied} injected, {skipped} already present, {problems} problems "
          f"(routes {len(TECH_DEPTH)}, trees {len(BASES)})")
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
