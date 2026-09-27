#!/usr/bin/env python3
"""Submit BRYME's queued URLs to the Bing Webmaster API safely.

The API key is read only from BING_WEBMASTER_API_KEY and is never written to
this repository. Bing enforces a daily quota, so the script submits in batches,
removes only confirmed successful URLs, and stops on a quota response.
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "bing-indexing-queue.txt"
ENDPOINT = "https://ssl.bing.com/webmaster/api.svc/json/SubmitUrlbatch"


def submit(key: str, urls: list[str]) -> tuple[bool, str]:
    payload = json.dumps({"siteUrl": "https://thebryme.com", "urlList": urls}).encode()
    req = urllib.request.Request(
        ENDPOINT + "?apikey=" + key,
        data=payload,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "BRYME-bing-submit/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return True, response.read().decode("utf-8", "replace")[:300]
    except urllib.error.HTTPError as error:
        return False, error.read().decode("utf-8", "replace")[:300]
    except Exception as error:  # noqa: BLE001
        return False, f"{type(error).__name__}: {error}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=500)
    args = parser.parse_args()

    key = os.environ.get("BING_WEBMASTER_API_KEY", "").strip()
    if not key and not args.dry_run:
        raise SystemExit("BING_WEBMASTER_API_KEY is required; it is never read from a committed file")
    urls = list(dict.fromkeys(line.strip() for line in QUEUE.read_text().splitlines() if line.strip()))
    if not urls:
        print("Bing queue is empty.")
        return 0

    batch_size = max(1, min(args.limit, 500))
    if args.dry_run:
        print(f"DRY RUN: {len(urls)} queued URLs; next batch would contain {min(batch_size, len(urls))}")
        return 0

    submitted = 0
    while urls:
        batch = urls[:batch_size]
        ok, detail = submit(key, batch)
        print(f"Bing batch: {len(batch)} URLs -> {'accepted' if ok else 'rejected'} ({detail})")
        if not ok:
            print("Queue preserved; retry after the reported Bing error or quota reset.")
            break
        urls = urls[len(batch):]
        submitted += len(batch)
        QUEUE.write_text("\n".join(urls) + ("\n" if urls else ""))
        if submitted >= args.limit:
            break

    print(f"Submitted {submitted}; remaining {len(urls)}.")
    return 0 if submitted or not urls else 1


if __name__ == "__main__":
    raise SystemExit(main())
