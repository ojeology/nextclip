#!/usr/bin/env python3
"""Emit the Google Indexing API queue for genuinely qualifying JobPosting pages.

The Indexing API is a crawler *notification*, not an indexing guarantee and not a
general-purpose indexer. This builder only queues:
  - newly flagged jobPosting.eligible pages  -> "published"
  - eligible pages whose record changed       -> "updated"
  - previously-eligible pages now removed/closed -> "deleted"

It keeps `content/index-queue-state.json` so the next run can compute what
changed, which prevents irrelevant re-submissions. Non-job routes (hubs, guides,
articles, trust pages) are never queued.

Run as part of the build (after build-discovery) via:
  python3 scripts/build-index-queue.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import bryme_config as cfg

ROOT = Path(__file__).resolve().parents[1]
JOBS_FILE = ROOT / "content/jobs.json"
QUEUE_FILE = ROOT / "content/index-queue.json"
STATE_FILE = ROOT / "content/index-queue-state.json"


def eligible_urls() -> dict[str, dict]:
    """Return {url: record} for roles currently flagged jobPosting.eligible."""
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8")).get("jobs", [])
    out: dict[str, dict] = {}
    for job in jobs:
        spec = job.get("jobPosting") or {}
        if not spec.get("eligible"):
            continue
        url = "/jobs/" + str(job["id"]) + "/"
        # Never queue closed roles.
        if job.get("status") == "closed":
            continue
        out[url] = {"id": job["id"], "url": url, "datePosted": spec.get("datePosted") or job.get("verifiedAt", "")[:10]}
    return out


def main() -> int:
    current = eligible_urls()
    try:
        prev = json.loads(STATE_FILE.read_text(encoding="utf-8")).get("eligible", {})
    except Exception:
        prev = {}

    queue: list[dict] = []
    for url, rec in current.items():
        if url not in prev:
            queue.append({"url": url, "type": "published", **rec})
        elif prev[url] != rec:
            queue.append({"url": url, "type": "updated", **rec})
    for url in prev:
        if url not in current:
            queue.append({"url": url, "type": "deleted"})

    state = {"updatedAt": "2026-09-04", "eligible": current}
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    QUEUE_FILE.write_text(json.dumps({"site": cfg.site_url(), "items": queue}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Indexing queue: {len(queue)} notification(s) | {len(current)} eligible job page(s).")
    for item in queue:
        print(f"  {item['type']:9} {cfg.site_url()}{item['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
