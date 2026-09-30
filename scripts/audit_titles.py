#!/usr/bin/env python3
"""Audit every SERP title the builders generate, before it ships.

Why this exists
---------------
title_budget.budget_title() keeps <title> inside the ~60-char SERP window. On
30 September a sweep of the source titles passed 354/354 while the built pages
still published "Can a Nigerian writer actually get paid by | BRYME" - because
the sweep tested the title WITHOUT the brand suffix and the builders pass it
WITH one. Less room changes where the cut lands, so the two forms give different
answers. An audit that does not call the function exactly the way the builders
do is not an audit.

So this walks the same inputs the builders walk - guide and essay frontmatter,
and each opportunity's seoTitle - and budgets each one twice: bare, and with the
brand suffix appended the way each surface appends it.

Usage:
    python3 scripts/audit-titles.py            # audit, exit 1 on any problem
    python3 scripts/audit-titles.py --show     # also list every trimmed title
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from title_budget import LIMIT, MIN_HEAD, _DANGLING, budget_title  # noqa: E402
from writing_stats import fill  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# The suffixes the builders actually append, per surface.
SUFFIXES = (" | BRYME writing guides", " | BRYME", "")


def sources() -> list[tuple[str, str]]:
    """(label, title-as-the-builder-hands-it-over) for every generated page."""
    out: list[tuple[str, str]] = []
    for d in ("content/hub/guides", "content/essays"):
        for p in sorted((ROOT / d).glob("*.md")):
            head = p.read_text(encoding="utf-8")[:2000]
            m = re.search(r"^title:\s*(.+?)$", head, re.M)
            if m:
                out.append((f"{d}/{p.stem}", fill(m.group(1).strip())))
    doc = json.loads((ROOT / "content/opportunities.json").read_text(encoding="utf-8"))
    for r in doc["opportunities"]:
        out.append((f"opportunities/{r['slug']}", r["seoTitle"]))
    return out


_NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def truncated_number(src: str, out: str) -> str | None:
    """A number in the source that survives only as a fragment in the output.

    This desk's titles quote rates, so this is a correctness check, not a style
    one. "Communiqué: ₦150,000 (or $100 outside Nigeria) per piece" was cut at
    the comma inside 150,000 and published as "Communiqué: ₦150" - a rate ten
    thousand times too low, on a page whose entire job is to publish rates
    accurately. Any digit group of four or more that does not appear whole, but
    whose leading digits do, was truncated.
    """
    for m in _NUM.finditer(src):
        token = m.group(0).rstrip(",.")
        if len(token) < 4 or token in out:
            continue
        # "150,000" cut at the comma leaves "150" behind, so compare the
        # leading digit run - not a character prefix, which would compare
        # "150,00" against "150" and match nothing.
        lead = token.split(",")[0].split(".")[0]
        if len(lead) >= 3 and lead in out:
            return token
        # a bare digit run cut without separators: "1500" -> "150"
        if len(token) >= 4 and token[:-1] in out:
            return token
    return None


def problem(src: str, out: str) -> str | None:
    """None if `out` is an acceptable title for `src`, else the reason.

    Only a shortened BODY can be a fragment - a shorter brand suffix is not.
    """
    for suffix in SUFFIXES:
        if src.endswith(suffix) and out == src:
            return None
        body = src[: len(src) - len(suffix)] if suffix and src.endswith(suffix) else src
        if out.startswith(body):
            return None  # body intact
    b = out.split(" | ")[0].strip() if " | " in out else out.strip()
    if not b:
        return "empty"
    last = b.split()[-1].lower().strip(".,;:()\u2014\u2013-\"\u201c\u201d'")
    if last in _DANGLING:
        return f"dangling:{last}"
    if b.count("(") != b.count(")"):
        return "unbalanced-bracket"
    if b.count('"') % 2 or b.count("\u201c") != b.count("\u201d"):
        return "unbalanced-quote"
    if len(b) < MIN_HEAD:
        return "stub"
    frag = truncated_number(src, b)
    if frag:
        return f"truncated-number:{frag}"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", action="store_true", help="list every trimmed title")
    args = ap.parse_args()

    total = 0
    over = 0
    bad: list[tuple[str, str, str]] = []
    trimmed: list[tuple[str, str]] = []

    for label, src in sources():
        # pre-suffixed sources are tested as-is; bare ones get the builder's
        # suffix ladder, because that is what budget_title does with them.
        forms = [src] if " | " in src else [src + s for s in SUFFIXES]
        for form in forms:
            total += 1
            out = budget_title(form)
            if len(out) > LIMIT:
                over += 1
                bad.append((label, form, f"over-limit:{len(out)}"))
                continue
            if budget_title(out) != out:
                bad.append((label, form, "not-idempotent"))
                continue
            why = problem(form, out)
            if why:
                bad.append((label, form, why))
            elif out != form:
                trimmed.append((label, out))

    print(f"titles audited : {total}")
    print(f"over {LIMIT} chars : {over}")
    print(f"trimmed to fit : {len(trimmed)}")
    print(f"problems       : {len(bad)}")
    for label, form, why in bad:
        print(f"  [{why}] {label}")
        print(f"      in : {form}")
        print(f"      out: {budget_title(form)}")
    if args.show:
        print()
        for label, out in trimmed:
            print(f"  {len(out):>2}  {out}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
