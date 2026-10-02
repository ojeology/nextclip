#!/usr/bin/env python3
"""Re-verify after-dinner-conversation on 2026-10-02.

The page was re-fetched on the desk date while resolving the long pw.org slug
after_dinner_conversation_philosophy_ethics_short_story_magazine, which turned
out to name the same market this record already covers. The $75 rate, the AI
ban and the rest of the guidelines are unchanged on the page, so only the
check date moves: lastVerified is the date the desk actually read the page.

Refuses to run twice or against an unexpected record shape.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
RAW = ROOT / "research/rebuild/raw/after_dinner_conversation_philosophy_ethics_short_story_magazine.txt"
NEW_DATE = "2026-10-02"

data = json.loads(OPPS.read_text(encoding="utf-8"))
rec = next((r for r in data["opportunities"] if r["slug"] == "after-dinner-conversation"), None)
if rec is None:
    sys.exit("ERROR: after-dinner-conversation not found")
if rec["lastVerified"] == NEW_DATE:
    sys.exit("ERROR: already refreshed to 2026-10-02")
if rec["lastVerified"] != "2026-10-01":
    sys.exit(f"ERROR: unexpected lastVerified {rec['lastVerified']!r}")

if RAW.exists():
    text = " ".join(RAW.read_text(encoding="utf-8").split())
    for probe in ("one-time amount of $75 with no future royalties",
                  "does not accept writing generated with AI software"):
        if probe not in text:
            sys.exit(f"ERROR: page text no longer contains: {probe!r}")

rec["lastVerified"] = NEW_DATE
OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"after-dinner-conversation lastVerified -> {NEW_DATE}")
