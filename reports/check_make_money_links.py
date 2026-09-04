#!/usr/bin/env python3
"""Read-only HTTP status audit for external links on indexable Make Money pages.

Results distinguish an origin-confirmed 404/410 from bot protection (401/403/429)
and transport failures. A reachable HTTP response does not verify the factual
content or whether an opportunity is accepting submissions.
"""
from __future__ import annotations

import asyncio
import csv
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reports" / "site-inventory.csv"
OUTPUT = ROOT / "reports" / "make-money-external-link-status.csv"
CONCURRENCY = 8
TIMEOUT = aiohttp.ClientTimeout(total=25, connect=10, sock_read=15)
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/152.0 Safari/537.36 BRYME-Link-Audit/1.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Range": "bytes=0-32767",
}


def collect() -> dict[str, set[str]]:
    links: dict[str, set[str]] = defaultdict(set)
    with INPUT.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if not (
                row["category"] == "make-money"
                and row["indexable"] == "True"
                and row["self_canonical"] == "True"
            ):
                continue
            soup = BeautifulSoup((ROOT / row["file"]).read_text(errors="ignore"), "lxml")
            for anchor in soup.find_all("a", href=True):
                url = anchor["href"].strip()
                if url.startswith(("https://", "http://")):
                    links[url].add(row["route"])
    return links


def bucket(status: int | None, error: str) -> str:
    if status in (404, 410):
        return "LIKELY_DEAD"
    if status and 200 <= status < 400:
        return "REACHABLE"
    if status in (401, 403, 405, 406, 409, 418, 425, 426, 429, 451):
        return "PROTECTED_OR_RATE_LIMITED"
    if status and status >= 400:
        return "HTTP_ERROR_REVIEW"
    return "TRANSPORT_UNKNOWN" if error else "UNKNOWN"


async def check_one(session: aiohttp.ClientSession, sem: asyncio.Semaphore, url: str) -> dict:
    status = None
    final_url = ""
    error = ""
    content_type = ""
    try:
        async with sem:
            async with session.get(url, allow_redirects=True) as response:
                status = response.status
                final_url = str(response.url)
                content_type = response.headers.get("content-type", "")
                await response.content.read(1024)
    except Exception as exc:  # transport/TLS/DNS failures remain explicitly unknown
        error = f"{type(exc).__name__}: {exc}"[:500]
    return {
        "url": url,
        "domain": urlparse(url).netloc.lower(),
        "status": status if status is not None else "",
        "bucket": bucket(status, error),
        "final_url": final_url,
        "content_type": content_type,
        "error": error,
    }


async def run() -> None:
    links = collect()
    sem = asyncio.Semaphore(CONCURRENCY)
    connector = aiohttp.TCPConnector(limit=CONCURRENCY, ssl=True)
    async with aiohttp.ClientSession(timeout=TIMEOUT, headers=HEADERS, connector=connector) as session:
        results = await asyncio.gather(*(check_one(session, sem, url) for url in sorted(links)))
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        fields = ["url", "domain", "status", "bucket", "final_url", "content_type", "source_page_count", "source_pages", "error"]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for result in sorted(results, key=lambda r: (r["bucket"], r["domain"], r["url"])):
            result["source_page_count"] = len(links[result["url"]])
            result["source_pages"] = " | ".join(sorted(links[result["url"]]))
            writer.writerow(result)
    from collections import Counter
    counts = Counter(r["bucket"] for r in results)
    print(f"Checked {len(results)} unique links -> {OUTPUT.relative_to(ROOT)}")
    for key, value in sorted(counts.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(run())
