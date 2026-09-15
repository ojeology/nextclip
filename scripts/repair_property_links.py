#!/usr/bin/env python3
"""Scoped repair: prefix the property-internal hrefs that build-routing.py
never got to prefix, on exactly the pages verified broken in production.

Background
----------
build-routing.py::rewrite_prop_paths() turns /slug/ into /<prop>/slug/ when it
copies ecosystem/<prop> into <prop>/. But build-routing.py is one-shot and now
aborts ("tree is already routed", exit 1) on every build, so pages authored
since it last ran shipped root-absolute hrefs that 404 in production.

Verified live (2026-09-15): /exercise-library-push/ -> 404 while
/fitness/exercise-library-push/ -> 200; same for all 13 tech targets.

Scope is deliberately narrow: the 14 pages measured broken, in the deployed
tree, its public/ mirror and its ecosystem/ source. Validity of every rewrite
target is decided from the git tree listing (authoritative) rather than the
local working copy, which is missing ~2200 files.

Rewrite rule for href="/X/" (optional #anchor preserved):
    X must be a real page of the property  ->  <prop>/X/index.html in git tree
    X must NOT exist at the domain root    ->  X/index.html absent from git tree
    X must not already be prefixed
Idempotent, and safe to re-run.

Run: python3 scripts/repair_property_links.py [--check] [--verbose]
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = "--check" in sys.argv
VERBOSE = "--verbose" in sys.argv
TREE_CACHE = Path("/tmp/tree.json")
REPO = "ojeology/nextclip"
BRANCH = "main"

DQ = chr(34)

SCOPE = {
    "fitness": ["exercise-library-push", "exercise-library-pull", "exercise-library-legs",
                "exercise-library-core", "exercise-library-cond"],
    "tech": ["do-you-need-a-smart-home-hub", "how-much-ram-do-you-need",
             "matter-vs-thread-vs-zigbee-vs-wifi", "microsoft-365-free-vs-paid",
             "render-vs-vercel-vs-netlify", "smart-plug-going-offline", "ssd-vs-hdd",
             "wi-fi-standards-compared", "windows-storage-full"],
}

# fitness tools live under /fitness/ but are not article dirs in every listing
ALWAYS_FITNESS = {"exercise-library", "exercise-library-push", "exercise-library-pull",
                  "exercise-library-legs", "exercise-library-core", "exercise-library-cond",
                  "workout-builder", "1rm-calculator", "fitness-calculators", "weekly-planner"}

HREF_RE = re.compile(r'href=' + DQ + r'/([a-z0-9][a-z0-9\-]*/)(#[^' + DQ + r']*)?' + DQ)


def git_index() -> set[str]:
    """Every path in the upstream tree (cached)."""
    if TREE_CACHE.is_file():
        d = json.loads(TREE_CACHE.read_text())
        if not d.get("truncated"):
            return {e["path"] for e in d["tree"]}
    url = f"https://api.github.com/repos/{REPO}/git/trees/{BRANCH}?recursive=1"
    d = json.loads(urllib.request.urlopen(url, timeout=60).read())
    TREE_CACHE.write_text(json.dumps(d))
    return {e["path"] for e in d["tree"]}


def main() -> int:
    paths = git_index()
    print(f"authoritative git index: {len(paths)} paths")

    total = 0
    touched = 0
    skipped_root: list[str] = []
    unknown: list[str] = []

    for prop, slugs in SCOPE.items():
        prop_pages = {p.split("/")[1] + "/" for p in paths
                      if p.startswith(prop + "/") and p.endswith("/index.html")
                      and p.count("/") == 2}
        prop_pages |= ALWAYS_FITNESS if prop == "fitness" else set()
        root_pages = {p.split("/")[0] + "/" for p in paths
                      if p.endswith("/index.html") and p.count("/") == 1}

        for slug in slugs:
            for base in (f"{prop}/{slug}", f"public/{prop}/{slug}", f"ecosystem/{prop}/{slug}"):
                f = ROOT / base / "index.html"
                if not f.is_file():
                    continue
                text = f.read_text(encoding="utf-8", errors="replace")
                fixes: list[str] = []

                def sub(m, prop=prop, prop_pages=prop_pages, root_pages=root_pages, fixes=fixes):
                    target, anchor = m.group(1), m.group(2) or ""
                    if target.startswith(prop + "/"):
                        return m.group(0)
                    if target in root_pages:
                        skipped_root.append(target)
                        return m.group(0)
                    if target not in prop_pages:
                        unknown.append(target)
                        return m.group(0)
                    fixes.append(target)
                    return "href=" + DQ + "/" + prop + "/" + target + anchor + DQ

                new = HREF_RE.sub(sub, text)
                if not fixes:
                    continue
                total += len(fixes)
                touched += 1
                print(f"  {base}/index.html  ({len(fixes)} href)")
                if VERBOSE:
                    for t in sorted(set(fixes)):
                        print(f"        /{t} -> /{prop}/{t}")
                if not CHECK:
                    f.write_text(new, encoding="utf-8")

    print()
    if skipped_root:
        print("left alone (a real root page exists):", sorted(set(skipped_root)))
    if unknown:
        print("left alone (not a page of this property):", sorted(set(unknown)))
    print()
    print(("would fix: " if CHECK else "fixed: ") + f"{total} href(s) across {touched} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
