#!/usr/bin/env python3
"""Resolve content/opportunities.json when merging this branch into main.

THIS IS A ONE-OFF, FOR THAT MERGE. It is committed so the resolution does not have
to be re-derived, and because it will refuse to write unless the merge is sound.
It is not a build step and nothing imports it.

Verified against main at c61f1ff46cf: see
reports/MERGE-REHEARSAL-2026-09-30.md.

The conflict is one hunk in one file. Everything else - the allowlist, the
pub-countries map, build-writing-first.py - auto-merges.

WHY A SCRIPT AND NOT A HAND EDIT
--------------------------------
The two sides edited DIFFERENT FIELDS of the same records. Main's Phase 4 and
experience work added `simultaneousSubmissions`, `simultaneousNote` and
experience fields to its 147 records; this branch rewrote `howToSubmit` and
`lastVerified` on three of those same records while adding 108 records of its
own. Taking either side wholesale throws away real work:

  take main's file   -> lose the branch's 108 markets and 3 howToSubmit fixes
  take branch's file -> lose Phase 4 on all 147, and the experience batch

So this does a real three-way merge per record:

  for each field, if the branch changed it and main did not, take the branch's
  value; otherwise take main's.

and appends the branch-only records. The result is checked before it is written.

Run from the repository root with the merge in progress:
    python3 resolve-merge.py
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
OPPS = ROOT / "content/opportunities.json"
MAIN = "origin/main"
BRANCH = "origin/bryme/markets-batch-verified"


def load(rev: str) -> list[dict]:
    out = subprocess.run(["git", "show", f"{rev}:content/opportunities.json"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return json.loads(out)["opportunities"]


def main() -> int:
    mb = subprocess.run(["git", "merge-base", MAIN, BRANCH], cwd=ROOT,
                        capture_output=True, text=True, check=True).stdout.strip()
    base = {o["slug"]: o for o in load(mb)}
    theirs = {o["slug"]: o for o in load(MAIN)}          # main: Phase 4 + experience
    ours = {o["slug"]: o for o in load(BRANCH)}          # this branch: 108 more markets

    print(f"merge base   : {mb[:9]}")
    print(f"main         : {len(theirs)} records")
    print(f"branch       : {len(ours)} records")

    merged: list[dict] = []
    branch_wins = 0
    for o in load(BRANCH):
        slug = o["slug"]
        if slug not in theirs:
            merged.append(o)                              # branch-only: keep as-is
            continue
        b, t = base.get(slug, {}), theirs[slug]
        rec = dict(t)                                     # main is the base
        for k, v in o.items():
            branch_changed = (k not in b
                              or json.dumps(b[k], sort_keys=True) != json.dumps(v, sort_keys=True))
            if not branch_changed:
                continue
            # main left it alone if main's value still equals the merge base's,
            # or if main does not carry the key at all.
            main_changed = (k in t and k in b
                            and json.dumps(t[k], sort_keys=True) != json.dumps(b[k], sort_keys=True))
            if not main_changed:
                rec[k] = v
                branch_wins += 1
        merged.append(rec)

    # The working file carries conflict markers, so it is not parseable. Take the
    # document skeleton (disclaimer, earningCategories, ...) from main, whose
    # copy is the newer of the two for everything outside `opportunities`.
    main_doc = json.loads(subprocess.run(
        ["git", "show", f"{MAIN}:content/opportunities.json"], cwd=ROOT,
        capture_output=True, text=True, check=True).stdout)
    branch_doc = json.loads(subprocess.run(
        ["git", "show", f"{BRANCH}:content/opportunities.json"], cwd=ROOT,
        capture_output=True, text=True, check=True).stdout)
    doc = dict(main_doc)
    # any document-level key the branch added but main lacks
    for k, v in branch_doc.items():
        if k != "opportunities" and k not in main_doc:
            doc[k] = v
    doc["opportunities"] = merged
    # updatedAt: the later of the two, so the file does not claim to be staler
    # than either side.
    dates = [d for d in (branch_doc.get("updatedAt"), main_doc.get("updatedAt")) if d]
    if dates:
        doc["updatedAt"] = max(dates)

    # ---- checks before writing -------------------------------------------------
    errs = []
    if len(merged) != len(ours):
        errs.append(f"record count changed: {len(merged)} != {len(ours)}")
    slugs = [r["slug"] for r in merged]
    if len(set(slugs)) != len(slugs):
        errs.append("duplicate slugs in the merged set")
    # every rule main's data satisfies must still hold
    missing = [s for s in theirs if s not in set(slugs)]
    if missing:
        errs.append(f"records lost from main: {missing[:5]}")
    no_sim = [r["slug"] for r in merged if "simultaneousSubmissions" not in r]
    if no_sim:
        errs.append(f"{len(no_sim)} records still without simultaneousSubmissions: {no_sim[:5]}")
    for r in merged:
        if "simultaneousSubmissions" in r:
            v = r["simultaneousSubmissions"]
            if v not in ("accepted", "not-accepted", "not-stated"):
                errs.append(f"{r['slug']}: bad value {v!r}")
            if v == "not-stated" and r.get("simultaneousNote"):
                errs.append(f"{r['slug']}: not-stated but carries a note")
            if v != "not-stated" and not r.get("simultaneousNote"):
                errs.append(f"{r['slug']}: states a policy with no supporting sentence")

    # The invariant that matters, and the one the first version of this script
    # failed while reporting success: every field the branch changed and main did
    # not must still equal the branch's value. Without this check an inverted
    # condition silently reverted three records' howToSubmit to empty and the
    # script printed "all checks passed".
    lost: list[str] = []
    by_slug = {r["slug"]: r for r in merged}
    for o in ours.values():
        slug = o["slug"]
        if slug not in theirs:
            continue
        b, t, m = base.get(slug, {}), theirs[slug], by_slug[slug]
        for k, v in o.items():
            branch_changed = (k not in b
                              or json.dumps(b[k], sort_keys=True) != json.dumps(v, sort_keys=True))
            if not branch_changed:
                continue
            main_changed = (k in t and k in b
                            and json.dumps(t[k], sort_keys=True) != json.dumps(b[k], sort_keys=True))
            if main_changed:
                continue                                   # main's edit legitimately wins
            if json.dumps(m.get(k), sort_keys=True) != json.dumps(v, sort_keys=True):
                lost.append(f"{slug}.{k}")
    if lost:
        errs.append(f"{len(lost)} branch edit(s) did not survive the merge: {lost[:6]}")

    if errs:
        print("\nREFUSING TO WRITE:")
        for e in errs:
            print("  -", e)
        return 1

    OPPS.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nmerged records        : {len(merged)}")
    print(f"  from main, phase 4  : {sum(1 for r in merged if 'simultaneousSubmissions' in r)}")
    print(f"  branch fields kept  : {branch_wins} (across {len(ours)} records)")
    print(f"  updatedAt           : {doc.get('updatedAt')}")
    print("all checks passed; written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
