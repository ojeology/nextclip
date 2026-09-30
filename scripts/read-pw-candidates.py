#!/usr/bin/env python3
"""Fetch the OWN guidelines page of each new Poets & Writers candidate.

Pipeline position, for a writing-market batch:

    pw.org directory          scripts/rebuild-pw-backlog.py
      -> names + official URLs only
    triage against this desk  this script
      -> candidates not already recorded
    the publication's OWN page  this script
      -> raw text saved for reading
    reading                   a human reads the text and records the figures

WHAT THIS SCRIPT DOES NOT DO
----------------------------
It does not read, extract, or record any figure. It fetches text and saves it;
the rates, word counts, rights and AI statements are read off the saved text by
hand, because every figure in a batch has to come from the publication's own
page and a regex cannot be trusted to tell a contributor rate from a submission
fee, a contest prize, or a pay note that belongs to pw.org rather than to the
publication. The raw text is kept so a reading can be re-checked without
re-fetching, which is what batch 13's docstring promises.

pw.org's own summaries (`pw_unsolicited`, `pw_reading_fee` in the detail cache)
are deliberately not consulted here. They are orientation only and must never
become a recorded rate.

USAGE
-----
    python3 scripts/read-pw-candidates.py                 # fetch what is pending
    python3 scripts/read-pw-candidates.py --delay 6
    python3 scripts/read-pw-candidates.py --list          # show the triage only

Resumable: a page already saved is never fetched again. Exit 2 means the run
stopped early because a host refused it - the saved pages are intact.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import time
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (compatible; BRYME-research/1.0; +https://thebryme.com)"
BLOCK_CODES = (403, 429)
BLOCK_LIMIT = 6

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE = ROOT / "research/rebuild/detail_cache.json"
RAW = ROOT / "research/rebuild/raw"
INDEX = ROOT / "research/rebuild/candidates.json"
OPPS = ROOT / "content/opportunities.json"


class RateLimited(RuntimeError):
    """A host refused several requests in a row. Stop rather than hammer it."""


_blocks = 0


def get(url: str, tries: int = 3) -> str:
    """GET a URL as text. Raises RateLimited after BLOCK_LIMIT refusals in a row."""
    global _blocks
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,text/plain;q=0.9,*/*;q=0.8"})
            with urllib.request.urlopen(req, timeout=30) as r:
                ctype = (r.headers.get("Content-Type") or "").lower()
                if "pdf" in ctype:
                    return ""  # a PDF needs a different reader; record why below
                body = r.read()
                _blocks = 0
                return body.decode(r.headers.get_content_charset() or "utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - network errors vary by host
            code = getattr(e, "code", None)
            if code in BLOCK_CODES:
                _blocks += 1
                if _blocks >= BLOCK_LIMIT:
                    raise RateLimited(f"{code} refused {_blocks} times in a row") from e
                hdrs = getattr(e, "headers", None)
                after = (hdrs.get("Retry-After") if hdrs else None) or ""
                time.sleep(min(float(after), 60) if after.strip().isdigit()
                           else min(2.0 ** i, 8) + 4)
            else:
                time.sleep(min(2.0 ** i, 8))
    return ""


def to_text(html: str) -> str:
    """Strip a page to readable text. Crude on purpose - it is a reading aid.

    The saved text is not the evidence. The LIVE page is the evidence, and every
    figure recorded is re-read there on the day it is recorded; this file only
    makes that reading cheaper to repeat and to check afterwards.
    """
    s = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", html)
    s = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h[1-6]|tr)>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = (s.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#39;", "'")
          .replace("&quot;", '"').replace("&lt;", "<").replace("&gt;", ">")
          .replace("&mdash;", " - ").replace("&ndash;", "-"))
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n\s*(\n\s*)+", "\n\n", s)
    return "\n".join(ln.strip() for ln in s.splitlines()).strip()


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


DESK_TZ = "Africa/Lagos"


def stamp() -> str:
    """The fetch instant, in both the sandbox clock and the desk's timezone.

    The desk is in Lagos and its dates are its own local ones. This crawl runs on
    a UTC clock, so for the hour that straddles midnight the two disagree by a
    day: a page fetched at 2026-09-30 23:20 UTC was read on 2026-10-01 in Lagos,
    and that is the date the record must carry. Stamping both means the raw file
    cannot look a day stale next to the record it supports.
    """
    import datetime, zoneinfo
    utc = datetime.datetime.now(datetime.timezone.utc)
    desk = utc.astimezone(zoneinfo.ZoneInfo(DESK_TZ))
    return (f"# fetched {utc:%Y-%m-%d %H:%M} UTC = {desk:%Y-%m-%d %H:%M} "
            f"{desk.tzname()} (desk date {desk:%Y-%m-%d})")


def host_of(url: str | None) -> str:
    m = re.match(r"https?://([^/]+)", url or "")
    return m.group(1).lower().replace("www.", "") if m else ""


def triage() -> list[dict]:
    """Candidate rows from the pw.org detail cache that this desk does not have."""
    if not CACHE.exists():
        raise SystemExit(f"no detail cache at {CACHE} - run rebuild-pw-backlog.py first")
    cache = json.loads(CACHE.read_text())
    rows = [r for r in cache.values() if not r.get("error") and r.get("guidelines")]

    recs = json.loads(OPPS.read_text(encoding="utf-8"))["opportunities"]
    have_norm = {norm(r.get("publication")) for r in recs}
    have_hosts = {h for r in recs
                  for h in (host_of(r.get("officialUrl")), host_of(r.get("applyUrl"))) if h}

    out = []
    for r in rows:
        n, h = norm(r.get("name")), host_of(r.get("guidelines"))
        if (n and n in have_norm) or (h and h in have_hosts):
            continue
        r = dict(r)
        r["host"] = h
        out.append(r)
    return sorted(out, key=lambda r: (r.get("name") or "").lower())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--delay", type=float, default=4.0,
                    help="seconds between fetches (default 4)")
    ap.add_argument("--list", action="store_true", help="print the triage and exit")
    ap.add_argument("--limit", type=int, default=0, help="stop after N fetches")
    ap.add_argument("--watch", type=float, default=0, metavar="SECONDS",
                    help="keep re-triaging every SECONDS so candidates found by a "
                         "still-running pw.org crawl are picked up as they appear; "
                         "exits when the crawl is complete and nothing is pending")
    args = ap.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    index = json.loads(INDEX.read_text()) if INDEX.exists() else {}
    total_rows = len(json.loads(CACHE.read_text()))

    if args.list:
        cands = triage()
        print(f"new candidates: {len(cands)} of {total_rows} cached rows")
        for c in cands:
            done = (RAW / f"{c['slug']}.txt").exists()
            print(f"  [{'x' if done else ' '}] {(c.get('name') or '?')[:34]:34} {c['guidelines'][:58]}")
        return 0

    fetched_this_run = 0
    while True:
        cands = triage()
        total_rows = len(json.loads(CACHE.read_text()))
        pending = [c for c in cands if not (RAW / f"{c['slug']}.txt").exists()]
        todo = pending[:max(0, args.limit - fetched_this_run)] if args.limit else pending
        print(f"[{time.strftime('%H:%M:%S')}] cache rows {total_rows}, "
              f"new candidates {len(cands)}, already fetched {len(cands) - len(pending)}, "
              f"pending {len(pending)}"
              + (f" (fetching {len(todo)} this pass)" if args.limit else ""), flush=True)

        for c in todo:
            fetched_this_run += 1
            try:
                html = get(c["guidelines"])
            except RateLimited as e:
                print(f"\nSTOPPED: {c['host']} {e}", flush=True)
                print(f"{fetched_this_run - 1} fetched this run; saved pages are intact. "
                      f"Re-run later.", flush=True)
                INDEX.write_text(json.dumps(index, indent=1, sort_keys=True))
                return 2
            text = to_text(html) if html else ""
            (RAW / f"{c['slug']}.txt").write_text(
                f"# {c.get('name')}\n# {c['guidelines']}\n{stamp()}\n"
                f"# chars: {len(text)}\n\n{text}", encoding="utf-8")
            index[c["slug"]] = {"name": c.get("name"), "url": c["guidelines"],
                                "host": c["host"], "chars": len(text)}
            if fetched_this_run % 10 == 0:
                INDEX.write_text(json.dumps(index, indent=1, sort_keys=True))
                print(f"  {fetched_this_run} fetched this run", flush=True)
            time.sleep(args.delay)

        INDEX.write_text(json.dumps(index, indent=1, sort_keys=True))

        # Stop when the pw.org crawl has finished every slug and nothing is pending.
        # Until then a watch loop keeps finding candidates the crawl has just added.
        crawl_done = total_rows >= len(json.loads((ROOT / "research/rebuild/slugs.json").read_text()))
        if not args.watch or (crawl_done and not todo):
            break
        time.sleep(args.watch)

    sizes = sorted(v["chars"] for v in index.values())
    thin = [k for k, v in index.items() if v["chars"] < 400]
    print(f"\nfetched {fetched_this_run} this run; {len(index)} pages saved -> {RAW}")
    if sizes:
        print(f"median {sizes[len(sizes)//2]} chars; {len(thin)} pages under 400 chars "
              f"(a wall or an error page - read these as 'not established', never as 'no fee')")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
