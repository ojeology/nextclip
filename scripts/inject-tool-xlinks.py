#!/usr/bin/env python3
"""A9 internal-link gap-fill: wire each desk's own tools into the pages where the
tool is genuinely relevant (no stuffing). Idempotent by marker data-esrc="tx".
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
BASES = (ROOT, PUB)
MARK = 'data-esrc="tx"'

MAP = {
    # league table pages -> tiebreak + points-race calculators
    "sports/la-liga-table": ["sports/league-tiebreak-calculator", "sports/points-race-calculator"],
    "sports/serie-a-table": ["sports/league-tiebreak-calculator", "sports/points-race-calculator"],
    "sports/ligue-1-table": ["sports/league-tiebreak-calculator", "sports/points-race-calculator"],
    "sports/bundesliga-table": ["sports/league-tiebreak-calculator", "sports/points-race-calculator"],
    "sports/how-the-premier-league-table-works": ["sports/league-tiebreak-calculator", "sports/points-race-calculator"],
    "sports/champions-league-table": ["sports/league-tiebreak-calculator", "sports/points-race-calculator"],
    "sports/the-weekend-ahead": ["sports/points-race-calculator"],
    "sports/how-the-transfer-window-works": ["sports/transfer-amortisation-calculator"],
    "sports/why-darts-starts-at-501-explained": ["sports/darts-checkout-trainer"],
    "sports/how-football-transfer-medicals-work": ["sports/transfer-amortisation-calculator"],
    "sports/how-transfer-fee-amortisation-works": ["sports/transfer-amortisation-calculator"],
    "sports/transfer-window-explained": ["sports/transfer-amortisation-calculator"],
    "sports/bundesliga-transfers": ["sports/transfer-amortisation-calculator"],
    "sports/la-liga-transfers": ["sports/transfer-amortisation-calculator"],
    "sports/league-transfers": ["sports/transfer-amortisation-calculator"],
    "sports/premier-league-transfers": ["sports/transfer-amortisation-calculator"],
}
# every club file -> wage-revenue-ratio calculator (club finances are in every file)
_clubs = sorted(p.name for p in (PUB / "sports" / "clubs").iterdir() if p.is_dir())
for c in _clubs:
    MAP.setdefault(f"sports/clubs/{c}", ["sports/wage-revenue-ratio-calculator"])

def label(slug):
    return slug.split("/")[-1].replace("-", " ").replace(" calculator", " calculator")

applied = skipped = 0
for base in BASES:
    for route, tools in MAP.items():
        f = base / route / "index.html"
        if not f.is_file():
            continue
        t = f.read_text(encoding="utf-8")
        if 'content="noindex' in t or MARK in t:
            skipped += 1
            continue
        links = " or the ".join(
            f'<a href="/{s}/">{label(s)}</a>' for s in tools
        )
        extra = f'<p {MARK}>See also the {links} &mdash; the desk tool that runs the numbers behind this page.</p>'
        if t.count("</main>") != 1:
            skipped += 1
            continue
        t = t.replace("</main>", extra + "</main>", 1)
        f.write_text(t, encoding="utf-8")
        applied += 1

print(f"tool-xlinks: {applied} linked, {skipped} skipped/marked")
