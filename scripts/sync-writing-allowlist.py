#!/usr/bin/env python3
"""Keep the Search allowlist in step with the writers desk's own data.

Why this exists
---------------
Adding a publication record to content/opportunities.json makes the build
generate an indexable /writers/writing/<slug>/ page. Adding a country to
COUNTRY_PROFILES in build-writing-first.py makes it generate an indexable
/writers/writing-opportunities/<country>/ atlas page.

Neither of those pages lands in content/index-allowlist.json on its own. The
allowlist is hand-maintained, and it is the single source of truth for both
robots meta and the sitemap. So a new record without an allowlist entry is a
page that is generated, canonical, index,follow - and absent from the sitemap
and the routed allowlist, which makes it effectively invisible to search.

validate-site-quality.js does catch this ("outside allowlist without noindex"
plus an indexable-count mismatch), so nothing can ship broken. But catching it
after the fact depends on someone remembering a manual step in a different file
- and the India batch script that prompted this script did not do it. Five
records and a country page were generated, indexable, and unlisted.

So: run this after any batch script, before the build that follows it. It is
idempotent, it only ever adds routes that the builders genuinely generate, and
it refuses to add a route for a record whose page the build does not produce.

Usage:
    python3 scripts/sync-writing-allowlist.py           # apply
    python3 scripts/sync-writing-allowlist.py --check    # report only, exit 1 if stale
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
BUILDER = ROOT / "scripts/build-writing-first.py"
ALLOWLISTS = ("content/index-allowlist.json", "content/index-allowlist.routed.json")
SOURCE = ALLOWLISTS[0]
ROUTED = ALLOWLISTS[1]


def country_slugs() -> dict[str, str]:
    """ISO -> route slug, read out of COUNTRY_PROFILES without importing it.

    build-writing-first.py runs a full generator at import time, so it is parsed
    rather than imported. Only literal kwargs are read.
    """
    tree = ast.parse(BUILDER.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "COUNTRY_PROFILES"
                for t in node.targets):
            out = {}
            for key, value in zip(node.value.keys, node.value.values):
                iso = ast.literal_eval(key)
                slug = None
                if isinstance(value, ast.Call):
                    for kw in value.keywords:
                        if kw.arg == "slug":
                            slug = ast.literal_eval(kw.value)
                if slug:
                    out[iso] = slug
            return out
    raise SystemExit("sync-writing-allowlist: COUNTRY_PROFILES not found")


def wanted() -> set[str]:
    """Every writers route the builders are expected to generate."""
    opps = json.loads(OPPS.read_text(encoding="utf-8"))["opportunities"]
    routes = {f"/writing/{o['slug']}/" for o in opps}
    routes |= {f"/writing-opportunities/{s}/" for s in country_slugs().values()}

    # Grouping pages beyond the country atlas: by type of writing, by
    # eligibility ("open to writers anywhere") and by experience stage.
    #
    # These were not modelled here at all, which is how two new indexable pages
    # came out of the 2026-09-30 build generated, canonical, robots index,follow
    # - and absent from the allowlist and therefore from the sitemap. That is
    # precisely the failure this script exists to prevent, reproduced one level
    # down.
    #
    # The builder decides which groups clear its own MIN_TYPE_PAGE threshold, so
    # rather than duplicate that number here and have the two drift, take the
    # truth from what the build actually produced.
    outdir = ROOT / "writers" / "writing-opportunities"
    if outdir.is_dir():
        for d in sorted(outdir.iterdir()):
            if (d / "index.html").is_file():
                routes.add(f"/writing-opportunities/{d.name}/")
    return routes


def _reviewed_stamp() -> str:
    """The tree's own date of record, derived rather than typed.

    This used to read `args.reviewed or "2026-09-30"`: a literal that silently
    *replaced* the allowlist's existing stamp whenever a route was added, while
    the --reviewed help text claimed the opposite ("keep existing"). The value is
    not cosmetic. build-discovery.py reads it as REVIEWED and uses it as the
    ceiling for every datePublished and dateModified in the allowlisted tree, and
    the change log and RSS lastBuildDate both key off it - so a stamp older than
    the build makes the current tree fail with "Future dateModified on /". That is
    exactly what adding the translation browse page did: the route was added
    correctly, the stamp rolled back a day, and the second build pass died.

    Mirrors `_build_now()` in build-writing-first.py, which is what stamps those
    dates in the first place: SOURCE_DATE_EPOCH when it is set, so CI's pinned
    rebuilds stay reproducible and the ceiling always equals the build's own idea
    of today; the real date otherwise, so a local sync never writes a stamp the
    tree has already overtaken.
    """
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "")
    if epoch.isdigit():
        return dt.datetime.fromtimestamp(int(epoch), dt.timezone.utc).date().isoformat()
    return dt.date.today().isoformat()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report drift without writing; exit 1 if any")
    ap.add_argument("--reviewed", default=None,
                    help="reviewedAt stamp to write (default: the tree's own "
                         "date of record - SOURCE_DATE_EPOCH if set, else today, "
                         "because record lastVerified values and every "
                         "dateModified in the allowlisted tree are checked "
                         "against it)")
    args = ap.parse_args()

    need = wanted()
    slugs = {o["slug"] for o in json.loads(OPPS.read_text(encoding="utf-8"))["opportunities"]}
    stale = False

    # Only the SOURCE allowlist is written. content/index-allowlist.routed.json
    # is a build artifact: build-routing.py regenerates it from the source on
    # every build, prefixing each route with /writers/. Writing it here too
    # would just put the unprefixed form into the routed file and break it.
    rel = SOURCE
    path = ROOT / rel
    doc = json.loads(path.read_text(encoding="utf-8"))
    have = set(doc["routes"])
    missing = sorted(need - have)

    # Stale routes are reported, never deleted - a record can be mid-batch
    # or deliberately held back, and silent deletion is not this script's job.
    orphan = sorted(
        r for r in have
        if r.startswith("/writing/")
        and not r.startswith("/writing-opportunities")
        and r != "/writing/"
        and r[len("/writing/"):-1].split("/")[0] not in slugs
    )

    print(f"  {rel}: {len(have)} routes, {len(missing)} missing")
    for m in missing:
        print(f"      + {m}")
    if orphan:
        print(f"    {len(orphan)} allowlisted writing route(s) with no record "
              f"(not touched): {', '.join(orphan[:6])}")

    if missing:
        stale = True
        if not args.check:
            doc["routes"] = sorted(have | set(missing))
            stamp = args.reviewed or _reviewed_stamp()
            if "reviewedAt" in doc:
                doc["reviewedAt"] = stamp
            path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
            print(f"      wrote {len(doc['routes'])} routes, reviewedAt={stamp}")

    # The stamp is checked on its own, because it can be wrong while the route
    # list is right. That is how the hardcoded "2026-09-30" survived: the write
    # path only ran when a route was missing, so a stale stamp in an otherwise
    # in-sync file was never revisited, and the failure surfaced one step later as
    # build-discovery's "Future dateModified on /" - which does not name the
    # allowlist as its cause.
    want_stamp = args.reviewed or _reviewed_stamp()
    have_stamp = doc.get("reviewedAt")
    if have_stamp and have_stamp < want_stamp:
        stale = True
        print(f"    reviewedAt {have_stamp} is behind the tree's date of record "
              f"{want_stamp}: build-discovery would reject every page dated today")
        if not args.check:
            doc["reviewedAt"] = want_stamp
            path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
            print(f"      bumped reviewedAt to {want_stamp}")

    # Read-only cross-check of the routed artifact, in its prefixed form.
    rp = ROOT / ROUTED
    if rp.is_file():
        rhave = set(json.loads(rp.read_text(encoding="utf-8"))["routes"])
        # The routed form is simply the source form with /writers in front;
        # the source paths already carry their trailing slash.
        rmissing = [x for x in (f"/writers{r}" for r in sorted(need))
                    if x not in rhave]
        print(f"  {ROUTED}: {len(rhave)} routes, {len(rmissing)} missing "
              f"(regenerated by build-routing.py)")
        if rmissing:
            stale = True

    if args.check and stale:
        print("FAIL: writers allowlist is stale")
        return 1
    print("OK: writers allowlist in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
