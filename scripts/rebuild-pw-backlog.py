#!/usr/bin/env python3
"""Rebuild the Poets & Writers candidate backlog for a writing-market batch.

WHY THIS IS COMMITTED
---------------------
Batches 5 to 12 of the market research each say "read from the batch-4 backlog.
No crawling." That backlog was 450 saved guidelines pages under research/batch4/. It was never
committed on any branch - git log --all -- 'research/*' returns nothing, and it is
not in .gitignore either, it is simply absent - so a fresh clone has no backlog and
those batches cannot be continued by the method they document. Batch 13 had to
rebuild it from scratch before it could do any market research at all.

Batches 5-12 shipped only the data, the script and the allowlist, so the reading
behind 101 records is not reviewable. This script makes the candidate list
reproducible instead of depending on a gitignored directory surviving.

WHAT IT DOES
------------
Stage 1  scrape the pw.org Literary Magazines directory for magazine slugs
Stage 2  fetch each magazine's detail page and pull the publication's OWN
         submission-guidelines URL

pw.org is used ONLY for names and official URLs. It publishes pay notes and
reading-fee flags of its own - this script deliberately does not read them.
Every rate in a batch must come from the publication's own page.

pw.org rate-limits concurrent detail fetches (6 workers got ~85% failures), so
stage 2 is sequential with backoff, resumes from a cache, and saves as it goes.
It is safe to interrupt and re-run.

USAGE
-----
    python3 scripts/rebuild-pw-backlog.py --out research/rebuild
    python3 scripts/rebuild-pw-backlog.py --out research/rebuild --stage 2

Then, per candidate, fetch the publication's own guidelines page and read it.
Nothing in this script reads a pay figure, and nothing it outputs may be
recorded as one.

NOTE ON OUTPUT
--------------
Output goes under research/, which is NOT gitignored - so committing is a
deliberate act, not something to fall into. The raw pages are bulky and stay
local; the evidence worth keeping is summarised into reports/ instead, as
reports/BATCH13-MARKETS-2026-09-30.md does for batch 13.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import time
import urllib.request

UA = "Mozilla/5.0 (compatible; BRYME-research/1.0; +https://thebryme.com)"
BASE = "https://www.pw.org/literary_magazines"
LIST_PAGES = 35
# the A-Z index pages that appear alongside real magazine slugs in the listing
INDEX_LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def get(url: str, tries: int = 4, pause: float = 0.3) -> str:
    """GET a URL as text, with backoff. Returns "" on failure."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - network errors vary by host
            code = getattr(e, "code", None)
            time.sleep(min(2.0 ** i, 12) + (4 if code in (403, 429) else 0))
    return ""


def stage1(outdir: pathlib.Path) -> list[str]:
    """Directory listing pages -> magazine slugs."""
    slugs: set[str] = set()
    for p in range(LIST_PAGES):
        url = BASE + (f"?page={p}" if p else "")
        html = get(url)
        slugs.update(s for s in re.findall(r'href="/literary_magazines/([A-Za-z0-9_\-\.]+)"', html)
                     if s.upper() not in INDEX_LETTERS)
        print(f"  page {p:2d}: {len(slugs)} slugs so far", flush=True)
        time.sleep(0.2)
    out = sorted(slugs)
    (outdir / "slugs.json").write_text(json.dumps(out, indent=1))
    print(f"stage 1: {len(out)} magazine slugs -> {outdir/'slugs.json'}")
    return out


def field(html: str, name: str) -> str | None:
    m = re.search(r'field-name-field-%s.*?</div>\s*</div>' % name, html, re.S)
    if not m:
        return None
    hrefs = re.findall(r'href="(https?://[^"]+)"', m.group(0))
    return hrefs[0].replace("&amp;", "&") if hrefs else None


def text_field(html: str, name: str) -> str | None:
    m = re.search(r'field-name-field-%s[^>]*>(.*?)</div>\s*</div>' % name, html, re.S)
    if not m:
        return None
    t = re.sub(r"<[^>]+>", " ", m.group(1))
    return re.sub(r"\s+", " ", t).replace("&nbsp;", " ").strip(" :") or None


def title_of(html: str) -> str | None:
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    return re.sub(r"\s+", " ", m.group(1)).split("|")[0].strip() if m else None


def stage2(outdir: pathlib.Path, slugs: list[str]) -> list[dict]:
    """Detail pages -> each publication's own submission-guidelines URL."""
    cache = outdir / "detail_cache.json"
    rows: dict[str, dict] = json.loads(cache.read_text()) if cache.exists() else {}
    rows = {s: r for s, r in rows.items() if not r.get("error")}
    todo = [s for s in slugs if s not in rows]
    print(f"stage 2: {len(rows)} cached, {len(todo)} to fetch")

    def save() -> None:
        tmp = cache.with_suffix(".tmp")
        tmp.write_text(json.dumps(rows, indent=1))
        tmp.replace(cache)

    for n, s in enumerate(todo, 1):
        html = get(f"{BASE}/{s}")
        if html:
            rows[s] = {
                "slug": s, "name": title_of(html),
                "website": field(html, "website"),
                "guidelines": field(html, "submission-guidelines-url"),
                # These two are pw.org's own summaries. Kept for orientation only.
                # They are NOT a source for any recorded rate or policy.
                "pw_unsolicited": text_field(html, "unsolicited-submissions"),
                "pw_reading_fee": text_field(html, "reading-fee"),
            }
        else:
            rows[s] = {"slug": s, "error": "fetch-failed"}
        if n % 20 == 0:
            save()
            ok = sum(1 for r in rows.values() if r.get("guidelines"))
            print(f"  {n}/{len(todo)}  cached={len(rows)}  with-guidelines={ok}", flush=True)
        time.sleep(0.3)
    save()

    out = [r for r in rows.values() if r.get("guidelines")]
    (outdir / "detail.json").write_text(json.dumps(sorted(rows.values(), key=lambda r: r["slug"]),
                                                   indent=1))
    print(f"stage 2: {len(rows)} fetched, {len(out)} with a guidelines URL")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="research/rebuild",
                    help="output directory (default research/rebuild)")
    ap.add_argument("--stage", choices=["1", "2", "both"], default="both")
    args = ap.parse_args()

    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    if args.stage in ("1", "both"):
        slugs = stage1(outdir)
    else:
        sp = outdir / "slugs.json"
        if not sp.exists():
            raise SystemExit(f"no slug list at {sp} - run stage 1 first")
        slugs = json.loads(sp.read_text())

    if args.stage in ("2", "both"):
        ok = stage2(outdir, slugs)
        print(f"\n{len(ok)} candidates have an official submission URL.")
        print("Next: fetch each publication's OWN guidelines page and read it. "
              "Nothing from pw.org is a source for a recorded rate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
