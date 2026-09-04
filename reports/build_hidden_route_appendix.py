#!/usr/bin/env python3
"""Build the route-level appendix for indexable pages with zero HTML inlinks."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "reports/site-audit-data.json").read_text())
ORPHANS = set(DATA["summary"]["indexable_orphans_global_links"])
TRUE_DISCOVERY = set(DATA["summary"]["hidden_indexable_no_sitemap_no_inlinks"])
with (ROOT / "reports/site-inventory.csv").open(newline="", encoding="utf-8") as fh:
    inventory = {row["route"]: row for row in csv.DictReader(fh)}


def decision(route: str) -> tuple[str, str, str]:
    if route.startswith("/article/"):
        return (
            "RETAIN_IMPROVE_AND_LINK",
            "P1",
            "Editorial page has substance but no HTML discovery path; link from the relevant title, article hub, and related-story modules.",
        )
    if route == "/make-money/microtasks/":
        return (
            "301_MERGE_TO_REMOTE_WORK",
            "P0",
            "Thin duplicate doorway: its title duplicates /make-money/remote-work/ and its copy tells users to use that page.",
        )
    if route in {"/make-money/ai-assisted-work/", "/make-money/content-creation/", "/make-money/income-skills/"}:
        return (
            "NOINDEX_THEN_MERGE_OR_BUILD",
            "P0",
            "Thin navigational doorway with no HTML inlinks; either merge into the main opportunities taxonomy or populate before indexing.",
        )
    if route == "/make-money/platform-reviews/":
        return (
            "RETAIN_BUILD_AND_LINK",
            "P1",
            "Useful guide index concept, but currently thin and undiscoverable; add summaries, verification dates, and a main-hub link.",
        )
    if route.startswith("/tech/"):
        return (
            "NOINDEX_UNTIL_POPULATED_OR_MERGED",
            "P0",
            "Empty/thin topic hub with no HTML inlinks; consolidate the taxonomy or publish enough reviewed child content first.",
        )
    if "/reports/" in route:
        return (
            "NOINDEX_ARCHIVE_OR_DELETE",
            "P0",
            "Generated 47–94-word match report; no indexable HTML inlink and insufficient standalone editorial value.",
        )
    if "/matches/" in route:
        return (
            "NOINDEX_UNTIL_DATA_AND_TEMPLATE_PASS",
            "P0",
            "Programmatic match page is undiscoverable in HTML and depends on the currently unreliable sports data pipeline.",
        )
    if route.endswith(("/fixtures/", "/results/")):
        return (
            "RETAIN_AFTER_DATA_FIX_AND_LINK",
            "P1",
            "Potentially useful league utility, but currently not linked from the Premier League hub and the data pipeline is unreliable.",
        )
    return ("MANUAL_REVIEW", "P1", "No safe family rule; review before changing index state.")


def family(route: str) -> str:
    if route.startswith("/article/"):
        return "entertainment editorial"
    if route.startswith("/tech/"):
        return "tech topic hub"
    if route.startswith("/make-money/"):
        return "make-money hub"
    if "/reports/" in route:
        return "sports match report"
    if "/matches/" in route:
        return "sports match page"
    if route.endswith("/fixtures/"):
        return "sports fixtures"
    if route.endswith("/results/"):
        return "sports results"
    return "other"

rows = []
for route in sorted(ORPHANS):
    r = inventory[route]
    action, priority, reason = decision(route)
    rows.append(
        {
            "route": route,
            "family": family(route),
            "title": r["title"],
            "source_main_words": r["main_words"],
            "in_sitemap": r["in_sitemap"],
            "html_inlinks_all_pages": r["inlinks_all"],
            "discovery_class": (
                "NO_SITEMAP_AND_NO_HTML_INLINKS" if route in TRUE_DISCOVERY else "SITEMAP_ONLY_NO_HTML_INLINKS"
            ),
            "current_state": "INDEXABLE_SELF_CANONICAL",
            "proposed_action": action,
            "priority": priority,
            "reason": reason,
        }
    )

output = ROOT / "reports/hidden-indexable-routes.csv"
with output.open("w", newline="", encoding="utf-8") as fh:
    writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {len(rows)} rows to {output.relative_to(ROOT)}; {len(TRUE_DISCOVERY)} lack both sitemap and HTML inlinks.")
