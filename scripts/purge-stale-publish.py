#!/usr/bin/env python3
"""batch 66e: enforce the legacy-route scheme at FILE level, and purge the stale publish.

Why this script exists (investigation of 2026-09-16, after a report that
"/tech returns 404"):

1. RESOLVED 2026-09-16 via the Render API: the live service now runs
   exactly the render.yaml routes (PUT /v1/services/{id}/routes). Before the
   sync it ran 18 dashboard-era rules from before that file existed: bare
   /tech 301ed to /guides/, /make-money 301ed to /opportunities/, and NONE
   of the 104 declared rules fired. The stale rules are only visible through
   the dedicated /routes endpoint - the service-details API does not expose
   them, which is how the drift hid. The old chain that explained the
   "/tech 404" report: /tech -> 301 -> /guides/ -> agents that normalise the
   trailing slash request /guides -> 404. This script stays: published files
   outrank edge rules, so the stubs remain the enforcement of record and the
   insurance against future config drift.

2. The buildCommand's `git clean -xdf public/` never ran on Render (its
   `|| echo` fallback swallowed the failure) until 2026-09-16, when the live
   buildCommand was synced to the render.yaml version via the Render API;
   before that, Render's cached build
   workspace kept republishing the 2026-09-14 vintage of the pre-routing
   public/ tree: 18 root directories (guides, writing, learn, tools, today,
   tested, templates, checklists, compare, contact, copyright, corrections,
   disclaimer, editorial-policy, essays, find, glossary, intelligence) with
   ~500 index,follow pages, each self-canonical, duplicating the identical
   /writers/ pages that have been the canonical home since the routing
   migration.

This script is the enforcement layer that does not depend on the dashboard or
on git being available in the build image. It runs as the final step of
`npm run build` (which the deployed buildCommand invokes whatever else it
does):

  a. PURGE: deletes public/<segment>/ for every legacy segment whose root
     scheme is not live (guard: the routed allowlist must contain no route at
     /<segment>/... - a segment that ever becomes a real property is skipped
     loudly instead of purged).
  b. STUB: regenerates, byte-stably, the file-level equivalents of the
     dormant render.yaml rules, using the exact batch-66c stub shape already
     proven in this repo (noindex,follow; instant meta-refresh; canonical to
     the destination; a visible link for no-JS visitors):
       - one root stub per legacy segment  (/<seg>/  -> destination)
       - one stub per routed sub-page      (/<seg>/<rest>/ -> /writers/<seg>/<rest>/)
     Flat-mapped segments (jobs, make-money, opportunities - whose wildcard
     rules collapse to /writers/writing/ without capture) get the root stub
     only, exactly like the rules they mirror.

The segment table and destinations are parsed from render.yaml at runtime -
one source of truth, no duplicated list to drift. Output carries no dates, so
regeneration is byte-identical and the CI reproducibility diff stays clean.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
RENDER_YAML = ROOT / "render.yaml"
ALLOWLIST = ROOT / "content" / "index-allowlist.routed.json"

RULE_RE = re.compile(
    r"\{\s*type:\s*redirect,\s*source:\s*(?P<src>[^,]+?),\s*destination:\s*(?P<dst>[^}]+?)\s*\}"
)


def parse_rules() -> dict[str, str]:
    """Return the bare legacy-segment -> destination map declared in render.yaml."""
    text = RENDER_YAML.read_text(encoding="utf-8")
    bare: dict[str, str] = {}
    for m in RULE_RE.finditer(text):
        src, dst = m.group("src").strip(), m.group("dst").strip()
        if "*" in src or "/" in src.strip("/"):
            continue                   # wildcards and nested sources (by-country)
        seg = src.strip("/")
        if seg and not src.endswith("/"):
            bare[seg] = dst
    return bare


def stub_html(dest: str, label: str) -> str:
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>" + label + " moved | THE BRYME</title>"
        '<meta name="robots" content="noindex,follow">'
        '<meta http-equiv="refresh" content="0;url=' + dest + '">'
        '<link rel="canonical" href="https://bryme.onrender.com' + dest + '"></head>'
        '<body><p>This page moved. Continue to <a href="' + dest + '">the current page</a>.</p></body></html>'
    )


def main() -> int:
    bare = parse_rules()
    if not bare:
        print("purge-stale-publish: no redirect rules parsed from render.yaml", file=sys.stderr)
        return 1

    al = json.loads(ALLOWLIST.read_text(encoding="utf-8"))
    routes = al["routes"] if isinstance(al, dict) else al

    purged = skipped = root_stubs = sub_stubs = 0
    for seg in sorted(bare):
        dest = bare[seg]
        # Guard: never touch a segment that is a live root property.
        live = [r for r in routes if r == f"/{seg}/" or r.startswith(f"/{seg}/")]
        if live:
            print(f"purge-stale-publish: SKIP /{seg}/ - live root property ({len(live)} allowlisted routes)")
            skipped += 1
            continue

        d = PUBLIC / seg
        if d.exists():
            shutil.rmtree(d)
            purged += 1

        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(stub_html(dest, seg), encoding="utf-8")
        root_stubs += 1

        # Sub-stubs: the file-level twin of the dormant `/<seg>/* -> /writers/<seg>/*`
        # rule. Flat-mapped hubs (jobs, make-money, opportunities) need no special
        # case: they have no routes under /writers/<seg>/, so this loop writes
        # nothing for them and the root stub above is their whole coverage.
        prefix = f"/writers/{seg}/"
        for r in routes:
            if not r.startswith(prefix) or r == prefix:
                continue
            rel = r[len(prefix):].strip("/")
            sub = PUBLIC / seg / rel
            sub.mkdir(parents=True, exist_ok=True)
            (sub / "index.html").write_text(stub_html(r, rel.split("/")[-1]), encoding="utf-8")
            sub_stubs += 1

    # Batch 11 (audit 2026-09-17): the served tree is public/ (server.js PUBLISH_DIR),
    # and Render's cached build workspace keeps UNTRACKED files across deploys while
    # the buildCommand's `git clean -xdf public/` demonstrably does not run (its
    # `|| echo` fallback swallows the failure). Pre-2026-09-14 builds copied the
    # _recovered/ archive source store into public/{entertainment,sports}/, where it
    # stayed publicly served (duplicate content, dead legacy breadcrumbs) long after
    # the sources moved to content/*-recovered/. Purge any _recovered/ dir under the
    # publish workspace by name class - deterministic, idempotent, no git needed.
    stale_rec = 0
    for base in (PUBLIC, ROOT, ROOT / "ecosystem"):
        for prop in ("sports", "entertainment", "tech", "fitness", "home", "writers"):
            d = base / prop / "_recovered"
            if d.is_dir():
                shutil.rmtree(d)
                stale_rec += 1

    print(f"purge-stale-publish: purged {purged} stale dirs, skipped {skipped} live, "
          f"wrote {root_stubs} root stubs + {sub_stubs} sub-stubs, "
          f"removed {stale_rec} stale _recovered dirs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
