#!/usr/bin/env python3
"""Ping every available search-engine discovery surface for BRYME.

This is *notification*, not a guarantee of indexing or ranking. It sends:
  - IndexNow (https://api.indexnow.org) — a single open submission that notifies
    participating engines (Bing, Yandex, Naver, Seznam, Yep and others).
  - A sitemap ping to Google, Bing, Baidu and Naver (where supported).

Required env / config:
  - SITE_URL      -> the public canonical origin (must be reachable from the web).
  - indexNowKey   -> from site.config.json (the committed key).
  - INDEXNOW_KEY  -> optional override.

Usage:
  python3 scripts/ping-search-engines.py            # ping all engines
  python3 scripts/ping-search-engines.py --dry-run  # show what would be sent

Best-effort: a failed ping is logged and never fails the build.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import bryme_config as cfg

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "docs/search-ping-log.jsonl"
KEY = (os.environ.get("INDEXNOW_KEY") or cfg.index_now_key() or "").strip()
SITE = cfg.site_url()


def log(engine: str, ok: bool, detail: str) -> None:
    row = {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "engine": engine,
           "ok": ok, "detail": detail, "site": SITE}
    try:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    except Exception:
        pass
    print(f"  [{engine}] {'OK ' if ok else 'ERR'} {detail}")


def get(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "BRYME-pinger/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def post_json(url: str, payload: dict, timeout: int = 20) -> str:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST", headers={
        "Content-Type": "application/json; charset=utf-8", "User-Agent": "BRYME-pinger/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def sitemap_url() -> str:
    return SITE + "/sitemap.xml"


def try_ping(engine: str, fn) -> None:
    try:
        log(engine, True, fn())
    except urllib.error.HTTPError as e:
        log(engine, False, f"HTTP {e.code} {e.reason}")
    except Exception as e:  # noqa: BLE001
        log(engine, False, f"{type(e).__name__}: {e}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Ping search engines for BRYME.")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be sent without sending.")
    args = ap.parse_args()

    smp = sitemap_url()
    print(f"BRYME search-engine ping · SITE_URL={SITE} · key={('set' if KEY else 'MISSING')}")
    print(f"  sitemap: {smp}")

    if args.dry_run:
        print("DRY-RUN (nothing sent):")
        print("  - IndexNow  -> https://api.indexnow.org/indexnow (key + url list)")
        print("  - Google    -> https://www.google.com/ping?sitemap=" + smp)
        print("  - Bing      -> https://www.bing.com/ping?sitemap=" + smp)
        print("  - Baidu     -> https://www.baidu.com/ping?sitemap=" + smp)
        print("  - Naver     -> https://searchadvisor.naver.com/ping?sitemap=" + smp)
        return 0

    # IndexNow: a single POST notifies all participating engines.
    if KEY:
        try_ping("IndexNow", lambda: post_json("https://api.indexnow.org/indexnow", {
            "host": SITE.split("//")[-1].split("/")[0],
            "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt", "urlList": [SITE + "/", smp],
        }))
    else:
        log("IndexNow", False, "no IndexNow key configured; skipping (set INDEXNOW_KEY or site.config indexNowKey)")

    # Sitemap pings are largely deprecated (Google and Bing now rely on IndexNow
    # and sitemap<lastmod>). Kept best-effort for the engines that still support
    # them; 404/410 responses are expected and harmless.
    try_ping("Google", lambda: get("https://www.google.com/ping?sitemap=" + smp))
    try_ping("Bing", lambda: get("https://www.bing.com/ping?sitemap=" + smp))
    try_ping("Baidu", lambda: get("https://www.baidu.com/ping?sitemap=" + smp))
    try_ping("Naver", lambda: get("https://searchadvisor.naver.com/ping?sitemap=" + smp))
    return 0


if __name__ == "__main__":
    sys.exit(main())
