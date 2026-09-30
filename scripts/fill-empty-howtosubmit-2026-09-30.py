#!/usr/bin/env python3
"""Fill the empty howToSubmit arrays on three original-147 records.

cracked, whatculture and statement-africa all render a blank "How to write for
them" section because howToSubmit is []. That has been flagged since batch 5.

The obvious fix - write the submission instructions - is not available. Checked
2026-09-30 with curl:

  cracked.com              968 words, but the only links are /about-us and
                           article permalinks. No write-for-us, no submissions,
                           no contribute, no pitch page exists.
  statementafrica.com      685 words. Links are /about/, /about/legal/ and
                           /contact/. No submissions route.
  whatculture.com/
      write-for-us         Returns 0 bytes of readable text and no links at all.
                           The URL exists but the page is client-rendered, so
                           its terms cannot be read in an HTTP-only environment.

Inventing instructions would breach the rule this expansion runs on: never
fabricate. So this writes what was actually verified - that no readable public
submissions route was found, and where to go instead. A writer reading the
dossier gets a true statement and a next step, rather than a blank or a guess.

Only howToSubmit changes. No pay figure, word count, right or AI policy is
touched, and no other record is modified.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
V = "2026-09-30"

FILL = {
    "cracked": [
        "Cracked does not publish a public submissions page. Checked 2026-09-30: "
        "cracked.com links only to /about-us and to article permalinks, with no "
        "write-for-us, submissions, contribute or pitch route anywhere on the site.",
        "Use the contact route on the /about-us page and ask whether the site is "
        "commissioning, rather than sending work unsolicited.",
        "The rates recorded here come from Cracked's own published pay structure, but "
        "without a public submissions page there is no stated route in — treat this "
        "as a commissioning market rather than an open one.",
    ],
    "whatculture": [
        "WhatCulture's write-for-us page exists at whatculture.com/write-for-us but "
        "is rendered entirely in the browser. Checked 2026-09-30: it returns no "
        "readable text and no links to an HTTP client, so its current terms could "
        "not be read and are not reproduced here.",
        "Open whatculture.com/write-for-us in a normal browser to read the live "
        "requirements before pitching.",
        "The rate recorded here is WhatCulture's own stated figure per list; confirm "
        "it on that page, since BRYME could not verify the surrounding terms.",
    ],
    "statement-africa": [
        "STATEMENT Africa does not publish a public submissions page. Checked "
        "2026-09-30: statementafrica.com links to /about/, /about/legal/ and "
        "/contact/ only, with no write-for-us or submissions route.",
        "Use the contact page at statementafrica.com/contact/ to ask about "
        "commissioning.",
        "Note that statement-africa.com — with a hyphen — does not resolve at all. "
        "The correct domain is statementafrica.com, which is live over both http and "
        "https.",
    ],
}


def main():
    data = json.loads(OPPS.read_text(encoding="utf-8"))
    changed = []
    for o in data["opportunities"]:
        if o["slug"] in FILL:
            if o["howToSubmit"]:
                sys.exit(f"ERROR: {o['slug']} already has howToSubmit; refusing to overwrite")
            o["howToSubmit"] = FILL[o["slug"]]
            o["lastVerified"] = V
            changed.append(o["slug"])
    missing = sorted(set(FILL) - set(changed))
    if missing:
        sys.exit(f"ERROR: slugs not found: {missing}")
    data["updatedAt"] = V
    OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Filled howToSubmit on {len(changed)} records: {', '.join(changed)}")


if __name__ == "__main__":
    main()
