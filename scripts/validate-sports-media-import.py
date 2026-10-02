#!/usr/bin/env python3
"""Guard the Sports media import as a noindex-only staging overlay.

Checks the source record counts, the staged route inventory, canonical/robots
metadata in both the ecosystem source tree and the public build, required v3
assets, and the no-sitemap/no-allowlist boundary. Internal-link resolution is
covered by scripts/check-internal-links.py in the full test suite.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "content" / "sports-media" / "migration-manifest.json"
SPORTS = ROOT / "ecosystem" / "sports"
PUBLIC = ROOT / "public"


def fail(message: str) -> None:
    print(f"sports-media-import: FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def route_of(file: Path, base: Path) -> str:
    rel = file.relative_to(base).parent.as_posix().strip("/")
    return "/sports/" + rel + "/"


def canonical(html: str) -> str | None:
    tags = re.findall(r'<link\b(?=[^>]*\brel=["\']canonical["\'])[^>]*>', html, re.I)
    if len(tags) != 1:
        return None
    m = re.search(r'\bhref=["\']([^"\']+)', tags[0], re.I)
    return m.group(1) if m else None


def robots(html: str) -> list[str]:
    return re.findall(r'<meta\b(?=[^>]*\bname=["\']robots["\'])[^>]*\bcontent=["\']([^"\']*)', html, re.I)


def staged_files(base: Path, core_slugs: list[str]) -> list[Path]:
    other = sorted((base / "other").rglob("index.html"))
    core = [base / "explainers" / slug / "index.html" for slug in core_slugs]
    return other + core


def sitemap_routes() -> set[str]:
    candidates = set()
    for base in (ROOT, PUBLIC):
        if not base.is_dir():
            continue
        for file in base.rglob("*sitemap*.xml"):
            if file.is_file():
                candidates.add(file)
    candidates.add(SPORTS / "sitemap.xml")
    candidates.add(ROOT / "sports" / "sitemap.xml")
    candidates.add(PUBLIC / "sports" / "sitemap.xml")
    found: set[str] = set()
    for file in candidates:
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8", errors="replace")
        for value in re.findall(r"<loc>(.*?)</loc>", text, re.I | re.S):
            found.add(urlsplit(value.strip()).path)
    return found


def main() -> int:
    if not MANIFEST.is_file():
        fail("migration manifest is missing")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    selection = manifest["selection"]
    expected_origin = str(json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))["siteUrl"]).rstrip("/")

    evergreen_file = ROOT / "content" / "sports-media" / "other-sports-evergreen-1213.json"
    scenario_file = ROOT / "content" / "sports-media" / "scenario-evergreen-400.json"
    evergreen = json.loads(evergreen_file.read_text(encoding="utf-8"))
    scenarios = json.loads(scenario_file.read_text(encoding="utf-8"))
    evergreen_rows = evergreen.get("explainers", [])
    scenario_rows = scenarios.get("explainers", [])
    evergreen_slugs = {str(row.get("slug", "")) for row in evergreen_rows}
    scenario_slugs = {str(row.get("slug", "")) for row in scenario_rows}
    if len(evergreen_rows) != selection["evergreen_explainer_records"] or len(evergreen_slugs) != len(evergreen_rows):
        fail("evergreen JSON count/slug uniqueness does not match the manifest")
    if len(scenario_rows) != selection["scenario_records"] or len(scenario_slugs) != len(scenario_rows):
        fail("scenario JSON count/slug uniqueness does not match the manifest")
    if not scenario_slugs <= evergreen_slugs:
        fail("the scenario set is no longer a subset of the evergreen slugs")

    core_slugs = selection.get("ready_core_explainer_slugs", [])
    if len(core_slugs) != selection["ready_core_explainers_imported_for_crosslinks"] or len(set(core_slugs)) != len(core_slugs):
        fail("ready core route list is missing or inconsistent")
    source_files = staged_files(SPORTS, core_slugs)
    expected_total = selection["new_html_pages_total"]
    if len(source_files) != expected_total:
        fail(f"staged source HTML count is {len(source_files)}, expected {expected_total}")
    evergreen_pages = list((SPORTS / "other" / "explainers").glob("*/index.html"))
    if len(evergreen_pages) != selection["evergreen_explainer_records"]:
        fail(f"staged evergreen route count is {len(evergreen_pages)}, expected {selection['evergreen_explainer_records']}")
    if len(list((SPORTS / "other").rglob("index.html"))) != selection["other_sports_html_routes_and_hubs"]:
        fail("other-sports hub/index/page count differs from the migration manifest")

    for name in ("media-v3.css", "media-v3.js"):
        if not (ROOT / "assets" / name).is_file() or not (PUBLIC / "assets" / name).is_file():
            fail(f"required v3 shell asset is missing: {name}")

    checked = 0
    for base, source in ((SPORTS, True), (PUBLIC / "sports", False)):
        for source_file in staged_files(base, core_slugs):
            if not source_file.is_file():
                fail(f"built staged route is missing: {source_file.relative_to(ROOT)}")
            html = source_file.read_text(encoding="utf-8", errors="replace")
            route = route_of(source_file, base)
            want = expected_origin + route
            robots_values = robots(html)
            if len(robots_values) != 1 or robots_values[0].strip().lower() != "noindex,follow":
                fail(f"{route}: expected exactly one noindex,follow robots meta, found {robots_values}")
            if canonical(html) != want:
                fail(f"{route}: canonical should be {want!r}, got {canonical(html)!r}")
            if 'href="/assets/media-v3.css"' not in html or 'src="/assets/media-v3.js"' not in html:
                fail(f"{route}: v3 shell CSS/JS links are missing")
            checked += 1

    # All new routes must remain outside the routed index allowlist and every
    # sitemap. The existing /sports/explainers/ index route is intentionally not
    # in this exact set and is unaffected.
    imported_routes = {route_of(p, SPORTS) for p in source_files}
    allowlist_file = ROOT / "content" / "index-allowlist.routed.json"
    if allowlist_file.is_file():
        allowlist_doc = json.loads(allowlist_file.read_text(encoding="utf-8"))
        routes = {str(route).rstrip("/") + "/" for route in allowlist_doc.get("routes", [])}
        overlap = imported_routes & routes
        if overlap:
            fail(f"staged routes were added to routed index allowlist: {sorted(overlap)[:4]}")
    listed = imported_routes & {r.rstrip("/") + "/" for r in sitemap_routes()}
    if listed:
        fail(f"staged routes were added to a sitemap: {sorted(listed)[:4]}")

    print(f"sports-media-import: PASS — {checked} staged pages checked in source+public; "
          f"{len(evergreen_rows)} evergreen records, {len(scenario_rows)} overlapping scenarios; "
          "noindex/canonical/v3 assets verified; no sitemap or allowlist entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
