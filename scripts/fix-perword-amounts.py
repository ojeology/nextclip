#!/usr/bin/env python3
"""Fix per-word rates stored as piece amounts (2026-09-06).

Repo convention: a per-word rate is NOT a piece amount and must carry
amountMin/amountMax = None, or it sorts and filters as if it were a fee.
A $1/word market was sorting below a $20 poem.

Separately, three records stored 0, which the standing rule forbids
outright: "records with no stated figure resolve to null, never 0".
doek-literary-magazine displayed "Not publicly stated" while storing 0.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
P = ROOT / "content/opportunities.json"
data = json.loads(P.read_text(encoding="utf-8"))
recs = {r["slug"]: r for r in data["opportunities"]}

# Per-word only -> no piece figure at all.
PER_WORD_ONLY = ["statement-africa", "griffith-review", "writers-digest",
                 "business-insider", "rest-of-world-2", "kenyon-review",
                 "diabolical-plots"]
# Stored 0 with nothing stated -> null, never 0.
NO_FIGURE = ["doek-literary-magazine"]
# Mixed: a real per-piece poetry fee alongside a per-word prose rate.
MIXED = {"haven-speculative": 20, "space-and-time": 5}

changed = []
for s in PER_WORD_ONLY + NO_FIGURE:
    if s not in recs:
        sys.exit(f"missing {s}")
    p = recs[s]["pay"]
    before = (p["amountMin"], p["amountMax"])
    p["amountMin"] = None
    p["amountMax"] = None
    changed.append((s, before, (None, None)))

for s, poem in MIXED.items():
    p = recs[s]["pay"]
    before = (p["amountMin"], p["amountMax"])
    p["amountMin"] = poem
    p["amountMax"] = poem
    changed.append((s, before, (poem, poem)))

# Contract: no record may store a zero pay amount.
for slug, r in recs.items():
    p = r["pay"]
    if p["amountMin"] == 0 or p["amountMax"] == 0:
        sys.exit(f"ERROR: {slug} still stores a zero pay amount")

P.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Fixed {len(changed)} records:")
for s, b, a in changed:
    print(f"  {s:<28} {b} -> {a}")
