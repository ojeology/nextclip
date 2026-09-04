#!/usr/bin/env python3
"""Stage and merge newly *verified* jobs into BRYME's jobs feed.

This is the intake path for the first real verified jobs. It does NOT invent
verification and does NOT scrape job boards. You must have opened the exact
employer/ATS page yourself (or confirmed it through BRYME's source hierarchy —
see /jobs/methodology/) and recorded the fields honestly.

How to add a verified job:
  1. Copy one object from the TEMPLATE below into `content/jobs-inbox.json`
     (an array). Fill every field. Only set `status` to `open_when_checked`
     (or another honest state) and `lastVerified` to the day you actually
     checked it.
  2. Only set `jobPosting.eligible` to `true` if the role is genuinely open,
     you recorded a real `description`, `datePosted` and `validThrough`, and
     the source is the employer's own page. Otherwise leave it off.
  3. Run:  python3 scripts/import-jobs.py --dry-run   (to review)
           python3 scripts/import-jobs.py             (to merge into jobs.json)

The script validates required fields, rejects duplicates (by id/sourceUrl),
warns on any `jobPosting.eligible` record that is missing a complete description
or date, and prints the list of routes you should add to
`content/index-allowlist.json` (only for genuinely current, indexable roles).

Run `python3 scripts/import-jobs.py --dry-run` first; commit the inbox file and
the merged jobs.json together so the change is auditable.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JOBS_FILE = ROOT / "content/jobs.json"
INBOX_FILE = ROOT / "content/jobs-inbox.json"

REQUIRED = [
    "id", "employer", "employerType", "title", "locationTextRaw",
    "eligibleCountries", "workMode", "employmentType", "sourceUrl",
    "sourceBoardUrl", "sourceSystem", "status", "verifiedAt", "notes",
    "category", "remoteEligible",
]
CATEGORIES = {"technology", "writing", "creative", "leadership", "finance", "customer-service", "marketing", "operations", "other"}
STATUSES = {"open_when_checked", "verified", "application_checked", "tested", "closed", "needs_recheck"}

TEMPLATE = """{
  "id": "employer-123456",
  "employer": "Example Employer",
  "employerType": "direct",
  "title": "Example Role Title",
  "locationTextRaw": "Lagos, Nigeria",
  "eligibleCountries": ["Nigeria"],
  "workMode": "Remote / Hybrid / Onsite",
  "employmentType": "Full time",
  "compensationRaw": null,
  "experience": "Not established from the source BRYME recorded.",
  "education": "Not established from the source BRYME recorded.",
  "deadline": "Not publicly stated",
  "sourceUrl": "https://example-employer.com/careers/123456-example-role",
  "sourceBoardUrl": "https://example-employer.com/careers",
  "sourceSystem": "Example employer careers",
  "sourceUpdatedAt": "2026-09-04T00:00:00Z",
  "status": "open_when_checked",
  "verifiedAt": "2026-09-04T08:35:00+01:00",
  "lastVerified": "2026-09-04",
  "notes": "What the source actually said when a BRYME editor opened it.",
  "summary": "A short original BRYME summary, not copied from the board.",
  "suitableFor": "Who this role realistically suits.",
  "category": "technology",
  "remoteEligible": false,
  "jobPosting": { "eligible": false }
}"""


def load(path: Path):
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Merge verified jobs into BRYME's feed.")
    ap.add_argument("--dry-run", action="store_true", help="Validate and report only; do not write.")
    args = ap.parse_args()

    existing = load(JOBS_FILE)
    inbox = load(INBOX_FILE)
    if inbox is None:
        print("No content/jobs-inbox.json found. Nothing to stage.")
        print("Use the template below to add your first verified job(s):\n")
        print(TEMPLATE)
        return 1

    jobs = (existing or {}).get("jobs", []) if isinstance(existing, dict) else []
    ids = {j["id"] for j in jobs}
    urls = {j.get("sourceUrl") for j in jobs}
    new = []
    problems: list[str] = []

    for idx, rec in enumerate(inbox):
        tag = f"inbox[{idx}]"

        if rec.get("_template"):  # user left the template text
            problems.append(f"{tag}: looks like an unfilled template — remove it before running.")
            continue
        missing = [k for k in REQUIRED if k not in rec or rec[k] in (None, "") or (isinstance(rec[k], list) and not rec[k])]
        if missing:
            problems.append(f"{tag}: missing required field(s): {', '.join(missing)}")
        if rec.get("id") in ids:
            problems.append(f"{tag}: duplicate id {rec.get('id')} already exists")
        if rec.get("sourceUrl") in urls:
            problems.append(f"{tag}: duplicate sourceUrl {rec.get('sourceUrl')}")
        if rec.get("category") not in CATEGORIES:
            problems.append(f"{tag}: category {rec.get('category')!r} not in {sorted(CATEGORIES)}")
        if rec.get("status") not in STATUSES:
            problems.append(f"{tag}: status {rec.get('status')!r} not in {sorted(STATUSES)}")
        if rec.get("remoteEligible") is True and rec.get("workMode", "").lower() in ("", "onsite", "hybrid"):
            problems.append(f"{tag}: remoteEligible=true but workMode does not say remote")

        # JobPosting eligibility requires complete rich fields — never fabricate.
        jp = rec.get("jobPosting") or {}
        if jp.get("eligible"):
            for field in ("description", "datePosted", "validThrough"):
                if not rec.get(field) and not jp.get(field):
                    problems.append(f"{tag}: jobPosting.eligible=true but missing {field} — set eligible=false until the source fields are complete.")
            if str(rec.get("sourceUrl", "")).lower().startswith(("https://", "http://")) is False:
                problems.append(f"{tag}: jobPosting.eligible=true but sourceUrl missing.")

        if not problems or all(not p.startswith(tag) for p in problems):
            ids.add(rec["id"])
            urls.add(rec.get("sourceUrl"))
            new.append(rec)

    if problems:
        print("PROBLEMS (fix before importing):")
        for p in problems:
            print("  -", p)
        return 2

    if args.dry_run:
        print(f"DRY-RUN: {len(new)} record(s) would be merged into content/jobs.json")
        for rec in new:
            print(f"  + {rec['id']} — {rec['employer']} · {rec['title']}")
        print("\nRoutes to consider adding to content/index-allowlist.json "
              "(only genuinely current/indexable roles):")
        for rec in new:
            print(f'    "/jobs/{rec["id"]}/",')
        return 0

    # Merge (deterministic: sort by employer then id).
    merged = jobs + new
    merged.sort(key=lambda j: (str(j.get("employer", "")).lower(), str(j.get("id", ""))))
    doc = dict(existing or {})
    doc["jobs"] = merged
    doc.setdefault("sourceCount", len({j.get("sourceUrl") for j in merged}))
    doc["updatedAt"] = "2026-09-04"
    JOBS_FILE.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Imported {len(new)} verified job(s). content/jobs.json now has {len(merged)} records.")
    print("Now add each indexable detail route to content/index-allowlist.json, then run:")
    print("  npm run build && npm test")
    return 0


if __name__ == "__main__":
    sys.exit(main())
