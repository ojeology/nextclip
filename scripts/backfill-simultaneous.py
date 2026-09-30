#!/usr/bin/env python3
"""Fetch the guidelines page for every market record missing a simultaneous policy.

WHY THIS EXISTS
---------------
Main's Phase 4 added simultaneousSubmissions / simultaneousNote to its 147
records by reading each publication's guideline. This branch predates that, and
it added 101 records of its own, so after the merge 101 records would still have
no answer for the eighth question in every publication docket.

WHAT THIS DOES, AND WHAT IT DELIBERATELY DOES NOT DO
----------------------------------------------------
It fetches each record's own guidelines page and pulls every passage that
mentions submitting elsewhere, so a human can read them. It does NOT classify
anything.

Phase 4's commit records why: keyword classification was wrong at nearly every
step.
  - "We do not accept simultaneous submissions" contains the substring
    "accept simultaneous submissions".
  - "We no longer accept simultaneous submissions" puts the negation four words
    before the verb.
  - Two publications answer only in an FAQ, so a sentence-window search stores
    the QUESTION ("Does One Story accept simultaneous submissions?") where a
    policy belongs.
  - The Malahat Review refuses simultaneity FOR CONTESTS and accepts it for
    regular submissions.

So this script produces reading material, not answers. A record is only
recorded as accepted / not-accepted when a human has read the sentence. Absence
of any mention is recorded as "not-stated", which is the honest value and the
majority answer.

OUTPUT
------
    research/backfill/<slug>.txt        raw page text, for re-reading
    research/backfill/candidates.json   every passage worth reading, per record

Usage:
    python3 scripts/backfill-simultaneous.py            # fetch and extract
    python3 scripts/backfill-simultaneous.py --limit 5  # try a few first
"""
from __future__ import annotations

import argparse
import html as H
import json
import pathlib
import re
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
OUT = ROOT / "research/backfill"
UA = "Mozilla/5.0 (compatible; BRYME-research/1.0; +https://thebryme.com)"

# Phrases that can carry a policy. Deliberately broad - the point is to surface
# passages for reading, not to decide anything.
PROBES = [
    "simultaneous", "elsewhere", "at the same time", "multiple submissions",
    "multiple pieces", "one submission at a time", "withdraw",
    "previously published", "exclusive",
]


def fetch(url: str, tries: int = 3) -> tuple[int | None, str]:
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "en-US,en;q=0.9",
            })
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                return r.status, raw.decode(r.headers.get_content_charset() or "utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            code = getattr(e, "code", None)
            if code in (401, 403, 404, 410):
                return code, ""
            time.sleep(1.5 * (i + 1))
    return None, ""


def to_text(html: str) -> str:
    h = re.sub(r"<(script|style|nav|footer|svg|head)[^>]*>.*?</\1>", " ", html,
               flags=re.S | re.I)
    h = re.sub(r"<br\s*/?>|</p>|</li>|</div>|</h[1-6]>|</tr>", "\n", h, flags=re.I)
    t = H.unescape(re.sub(r"<[^>]+>", " ", h))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    out, prev = [], None
    for line in (l.strip() for l in t.split("\n")):
        if line and line != prev:
            out.append(line)
            prev = line
    return "\n".join(out)


def passages(text: str) -> list[str]:
    """Every paragraph that mentions submitting elsewhere, plus a tight window."""
    found: list[str] = []
    seen: set[str] = set()
    for para in text.split("\n"):
        low = para.lower()
        if any(p in low for p in PROBES):
            key = re.sub(r"\W+", "", low)[:80]
            if key not in seen:
                seen.add(key)
                found.append(re.sub(r"\s+", " ", para).strip()[:700])
    # windows around the sharpest probe, to catch a question/answer split
    for m in re.finditer(r"simultaneous", text, re.I):
        w = re.sub(r"\s+", " ", text[max(0, m.start() - 220): m.end() + 220]).strip()
        key = re.sub(r"\W+", "", w.lower())[:80]
        if key not in seen:
            seen.add(key)
            found.append(w)
    return found[:12]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--targets", default=None,
                    help="JSON list of slugs to restrict to. Use this to touch ONLY "
                         "the branch-only records: the 147 records this branch shares "
                         "with main already carry Phase 4's values, and re-deriving "
                         "them here would only create merge conflicts.")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    cand_path = OUT / "candidates.json"
    cand: dict = json.loads(cand_path.read_text()) if cand_path.exists() else {}

    recs = json.loads(OPPS.read_text(encoding="utf-8"))["opportunities"]
    todo = [o for o in recs if "simultaneousSubmissions" not in o]
    if args.targets:
        keep = set(json.loads(pathlib.Path(args.targets).read_text()))
        before = len(todo)
        todo = [o for o in todo if o["slug"] in keep]
        print(f"--targets: scoped {before} -> {len(todo)} record(s)")
    todo = [o for o in todo if o["slug"] not in cand]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(todo)} record(s) to read", flush=True)

    for i, rec in enumerate(todo, 1):
        slug = rec["slug"]
        url = rec.get("officialUrl") or rec.get("applyUrl") or ""
        code, html = fetch(url) if url.startswith("http") else (None, "")
        entry: dict = {"slug": slug, "publication": rec["publication"], "url": url,
                       "http": code}
        if html:
            text = to_text(html)
            (OUT / f"{slug}.txt").write_text(text, encoding="utf-8")
            entry["passages"] = passages(text)
            entry["chars"] = len(text)
        else:
            entry["passages"] = []
            entry["error"] = "fetch-failed"
        cand[slug] = entry
        if i % 10 == 0:
            cand_path.write_text(json.dumps(cand, indent=1))
            hit = sum(1 for v in cand.values() if v.get("passages"))
            print(f"  {i}/{len(todo)}  cached={len(cand)}  with-passages={hit}", flush=True)
        time.sleep(0.4)

    cand_path.write_text(json.dumps(cand, indent=1))
    hit = [s for s, v in cand.items() if v.get("passages")]
    none = [s for s, v in cand.items() if not v.get("passages") and not v.get("error")]
    fail = [s for s, v in cand.items() if v.get("error")]
    print(f"\nfetched {len(cand)}")
    print(f"  passages to read : {len(hit)}")
    print(f"  no mention found : {len(none)}  (candidates for not-stated)")
    print(f"  fetch failed     : {len(fail)}")
    if fail:
        print("  failed:", ", ".join(fail[:15]))
    print(f"\nRead every passage before recording. Nothing here is classified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
