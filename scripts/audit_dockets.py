#!/usr/bin/env python3
"""Audit every rendered submission docket.

The docket makes two kinds of claim, and they fail in different ways.

Structural claims - eight rows, a value in each, a gap list whose length matches
the number of unanswered questions - fail when a record has a field shaped
unlike the others, which is exactly the shape a batch of 147 records never has
been.

Numerical claims - "The highest figure of the 36 records based in the United
States that state a figure", "9 of the other 12 ... state less, 1 state more, 2
state exactly this" - fail when the cohort rule in the builder and the cohort
rule in the reader's head disagree. That is the failure that matters, because a
wrong number here reads exactly as confidently as a right one. So this script
recomputes every published ranking from content/opportunities.json and
content/hub/pub-countries.json and compares it to the number on the page.

Written against the built HTML under writers/writing/<slug>/ rather than
against the builder's own helpers: the builder is the thing under test, and a
test that calls it the way it calls itself shares its mistakes. (The title
budget taught that lesson the expensive way - see scripts/audit_titles.py.)

Run: python3 scripts/audit_dockets.py
Exits non-zero on any problem.
"""
from __future__ import annotations

import collections
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from writing_stats import pay_shape  # noqa: E402  the shared pay-shape rule

PAY_COHORT_MIN = 5
ARTICLE_THE = {"United States", "United Kingdom"}

# Values that must never reach a page. Each one was produced by a real version
# of the builder during development, so each is a regression, not a hypothesis.
FORBIDDEN = [
    (re.compile(r"\bPaid\s+(?:[Pp]ayment|[Pp]rocessed|[Pp]aid)\b"),
     "doubled payment verb - a prefix was added to text that already had one"),
    (re.compile(r"\b(?:based in|other|of the)\s+International\b"),
     '"International" used as a place or a nationality'),
    (re.compile(r"\bother\s+(?:Nigeria|India|Canada|Kenya|Australia|Germany|"
                r"Ireland|Nepal|Namibia)\s+publication"),
     "country used as an adjective instead of 'records based in <country>'"),
    (re.compile(r"\{\{|\}\}"), "unfilled statistic token"),
    (re.compile(r"  +"), "double space"),
    # A word repeated across a phrase seam: "no other records on this desk
    # quoting in NGN quoting a flat fee". Each half was correct; only the join
    # was wrong, and it reached the live site because every check watched the
    # halves. Any word repeated within six words of itself is a seam defect.
    # A gerund repeated across a phrase seam: "…on this desk quoting in NGN
    # quoting a flat fee to compare this against". Each half was correct in
    # isolation; only the join was wrong, which is why every check that watched
    # the halves passed it. Narrow on purpose - a generic repeated-word test
    # fires on "state less and 3 state more" and "2 other records based in
    # Nigeria", which are the sentences working.
    (re.compile(r"\bquoting\b(?:\s+\w+){0,4}\s+quoting\b", re.I),
     "the same qualifier glued to itself across a seam"),
    (re.compile(r"\bthat state\b(?:\s+\w+){0,6}\s+that state\b", re.I),
     "the same qualifier glued to itself across a seam"),
    (re.compile(r"\s[,.;]"), "space before punctuation"),
    (re.compile(r"number could not be|None\b|nan\b|undefined"), "raw code value leaked"),
]

# These must track scripts/build-writing-first.py::_pay_position exactly. They
# fell out of step once already: the sentence was rephrased and every pattern
# silently stopped matching, so the audit reported "0 rankings recomputed" and
# 0 problems - a green run that checked nothing. The counts below are printed
# for that reason; a drop to zero is a failure of the audit, not a success.
CLAIM_HIGH = re.compile(r"The highest figure of the (\d+) (?:records .+?)\.")
CLAIM_LOW = re.compile(r"The lowest figure of the (\d+) (?:records .+?)\.")
CLAIM_SPLIT = re.compile(
    r"Of the other (\d+) (?:records .+?), (\d+) state less, (\d+) state more"
    r"(?:, (\d+) state exactly this)?\.")
# The floor-and-alone branch, which is also a cohort sentence: the record states
# a figure and there is nothing on the desk to place it against.
CLAIM_NONE = re.compile(r"BRYME records no other record .+? to compare this against\.")
CLAIM_THIN = re.compile(r"BRYME records (\d+) other (?:records .+?) — too few to rank")
# group 1 is the ` gap` class, group 2 the row. `findall` on a pattern whose
# only group was the class silently returned the class instead of the row, so
# every gap row read as answered - keep the marker as its own group.
# The seam between the record's own wording and BRYME's explanation, both of
# which end up in the same note. Checked inside a note, never across rows: the
# flattened docket legitimately reads "…AI policy Not stated The guideline is
# silent…", and a check that cannot tell a row boundary from a missing full stop
# reports 128 failures on a page set with none.
RUN_TOGETHER = re.compile(
    r"\b(?:stated|published|limit|terms|note)\s+(?:The|This|BRYME|It)\s")

ROW = re.compile(r'<div class="docket-row( gap)?">(.*?)</div>', re.S)
# Payment, Length, Who can submit, Response time, Simultaneous submissions,
# AI policy, Rights, Experience.
DOCKET_ROWS = 8

DOCKET = re.compile(r'<section class="section docket-section".*?</section>', re.S)


import re as _re

def _text(fragment: str) -> str:
    """Readable text: tag boundaries become spaces so words never fuse."""
    return re.sub(r" +", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))
                  ).replace("\u00a0", " ").strip()


def _raw(fragment: str) -> str:
    """Text with tags removed outright, for judging source whitespace.

    The readable version has to insert a space at every tag boundary, which
    manufactures a double space wherever two tags meet - so a whitespace check
    run against it fails on all 147 pages and can never see a real one.
    """
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).replace("\u00a0", " ")


def load():
    opps = json.loads((ROOT / "content/opportunities.json").read_text(encoding="utf-8"))["opportunities"]
    countries = json.loads((ROOT / "content/hub/pub-countries.json").read_text(encoding="utf-8"))
    return opps, countries


def build_cohorts(opps, countries):
    """Recomputed from scratch, from the same three-part rule the page states."""
    cohorts: dict = collections.defaultdict(list)
    for r in opps:
        pay = r.get("pay") or {}
        amount, currency = pay.get("amountMin") or 0, pay.get("currency") or ""
        if not amount or not currency:
            continue
        base = (countries.get(r["slug"]) or {}).get("base") or "*"
        cohorts[(base, currency, pay_shape(r))].append(r)
    return cohorts


def main() -> int:
    opps, countries = load()
    by_slug = {r["slug"]: r for r in opps}
    cohorts = build_cohorts(opps, countries)

    problems: list[str] = []
    claims_checked = 0
    pages = 0
    gaps_total = 0
    silent_rows = 0

    def fail(slug: str, msg: str) -> None:
        problems.append(f"{slug}: {msg}")

    for slug, rec in sorted(by_slug.items()):
        page = ROOT / "writers" / "writing" / slug / "index.html"
        if not page.exists():
            fail(slug, "publication page missing")
            continue
        pages += 1
        source = page.read_text(encoding="utf-8")

        found = DOCKET.search(source)
        if not found:
            fail(slug, "no docket on the page")
            continue
        block = found.group(0)

        rows = ROW.findall(block)
        if len(rows) != DOCKET_ROWS:
            fail(slug, f"{len(rows)} docket rows, expected {DOCKET_ROWS}")

        gap_rows = len(re.findall(r'class="docket-row gap"', block))
        asked = gap_rows
        gap_list = re.search(r'<div class="docket-gaps">.*?</div>', block, re.S)
        if gap_list:
            listed = len(re.findall(r"<li>", gap_list.group(0)))
            gaps_total += listed
            if listed != asked:
                fail(slug, f"{listed} gaps listed but {asked} rows marked unanswered")
            if listed == DOCKET_ROWS:
                if "leaves all eight questions" not in block:
                    fail(slug, "all eight unanswered but the headline does not say so")
            elif f"leaves {listed} of the eight questions" not in block:
                fail(slug, f"gap headline does not match the {listed} listed")
        elif asked:
            fail(slug, f"{asked} unanswered rows but no gap list")

        for gap_flag, row in rows:
            label = _text(row.split("</dt>")[0])
            dd = row.split("</dt>")[-1]
            value = _text(dd.split("</b>")[0])
            is_gap = bool(gap_flag)
            if not value:
                fail(slug, f'row "{label}" has no value')
            # The invariant the whole "what this record does not tell you"
            # section rests on: a row reads "Not stated" if and only if the
            # docket counts it as one of the unanswered questions. Break it
            # either way and the gap list starts describing a different page
            # from the one above it.
            if (value == "Not stated") != is_gap:
                fail(slug, f'row "{label}" value {value!r} but gap={is_gap}')
            if label.endswith(("Restricted to a stated group",)):
                fail(slug, "verdict text leaked into the label")
            if value == "Not stated":
                silent_rows += 1
            seam = RUN_TOGETHER.search(_text(row.split("</b>")[-1]))
            if seam:
                fail(slug, f"note runs two sentences together: {seam.group(0)!r}")
            # The desk's public promise, machine-checked: never describe a record
            # as open when the record only means "the guideline is silent".
            # `eligibility.notStated` is that distinction, and 34 records carry
            # it - the exact set this row got wrong.
            if value in ("Open internationally", "Open worldwide"):
                el = rec.get("eligibility") or {}
                if el.get("notStated"):
                    fail(slug, f'claims "{value}" but the record flags notStated')
                if (el.get("mode") or "") not in ("open", "worldwide"):
                    fail(slug, f'claims "{value}" but mode is {el.get("mode")!r}')

        flat = _text(block)
        raw = _raw(block)
        for pattern, why in FORBIDDEN:
            target = raw if pattern.pattern in (r"  +", r"\s[,.;]") else flat
            hit = pattern.search(target)
            if hit:
                fail(slug, f"{why}: {hit.group(0)!r}")

        # ---- the experience evidence must be on the page ---------------------
        # A label whose source sentence is not printed is a label the reader has
        # to take on trust, which is the one thing a docket exists to remove. The
        # quote and its URL are rendered verbatim, so both are checked verbatim.
        note = rec.get("experienceNote") or ""
        exp = str(rec.get("experience") or "not-stated")
        if exp != "not-stated" and not note:
            fail(slug, f"labelled {exp!r} with no evidence note")
        if note:
            m = re.match(r"^(.+?) \u2014 (https?://\S+) \(read ([0-9-]+)\)$", note)
            if not m:
                fail(slug, "evidence note is not in the stored <quote> — <url> (read <date>) shape")
            else:
                quote, url, read = m.groups()
                if _text(quote) not in flat:
                    fail(slug, "the quoted evidence is not printed on the page")
                if url not in block:
                    fail(slug, "the evidence URL is not printed on the page")
                if read not in block:
                    fail(slug, "the evidence read-date is not printed on the page")

        # ---- recompute every numerical claim on the page --------------------
        pay = rec.get("pay") or {}
        amount = pay.get("amountMin") or 0
        base = (countries.get(slug) or {}).get("base") or "*"
        cohort = cohorts.get((base, pay.get("currency") or "", pay_shape(rec)), [])
        others = [r for r in cohort if r["slug"] != slug]
        lower = sum(1 for r in others if (r["pay"]["amountMin"] or 0) < amount)
        higher = sum(1 for r in others if (r["pay"]["amountMin"] or 0) > amount)
        same = len(others) - lower - higher

        if pay.get("display") and amount:
            claim = CLAIM_HIGH.search(flat)
            if claim:
                claims_checked += 1
                if int(claim.group(1)) != len(cohort):
                    fail(slug, f'claims "{claim.group(1)}" records, cohort is {len(cohort)}')
                if higher or same:
                    fail(slug, f'"highest figure" but {higher} higher and {same} equal, in cohort')
            claim = CLAIM_LOW.search(flat)
            if claim:
                claims_checked += 1
                if int(claim.group(1)) != len(cohort):
                    fail(slug, f'claims "{claim.group(1)}" records, cohort is {len(cohort)}')
                if lower or same:
                    fail(slug, f'"lowest figure" but {lower} lower and {same} equal, in cohort')
            claim = CLAIM_SPLIT.search(flat)
            if claim:
                claims_checked += 1
                c_others, c_lower, c_higher = int(claim.group(1)), int(claim.group(2)), int(claim.group(3))
                c_same = int(claim.group(4) or 0)
                if (c_lower, c_others, c_higher, c_same) != (lower, len(others), higher, same):
                    fail(slug, f"published others={c_others} lower={c_lower} higher={c_higher} "
                               f"same={c_same} but the dataset computes others={len(others)} "
                               f"lower={lower} higher={higher} same={same}")
                if c_lower + c_higher + c_same != c_others:
                    fail(slug, "split claim does not add up to the cohort it names")
            # A thin-cohort record must not ALSO be carrying a ranking sentence,
            # and the peer count it names has to be the cohort's real size.
            thin = CLAIM_THIN.search(flat)
            if thin:
                if int(thin.group(1)) != len(others):
                    fail(slug, f'thin-cohort line names {thin.group(1)} peers, cohort has {len(others)}')
                if CLAIM_HIGH.search(flat) or CLAIM_LOW.search(flat) or CLAIM_SPLIT.search(flat):
                    fail(slug, "published a ranking inside the too-thin-to-rank branch")
            claimed = bool(claim or thin or CLAIM_NONE.search(flat)
                           or CLAIM_HIGH.search(flat) or CLAIM_LOW.search(flat))
            if not claimed and amount and pay.get("currency"):
                fail(slug, "states a figure but publishes no cohort sentence at all")
            ranked = bool(CLAIM_HIGH.search(flat) or CLAIM_LOW.search(flat) or CLAIM_SPLIT.search(flat))
            if ranked and len(cohort) < PAY_COHORT_MIN:
                fail(slug, f"ranked against a cohort of {len(cohort)}, below the {PAY_COHORT_MIN} floor")
            if ranked and "quoted the same way" not in flat:
                fail(slug, "ranking published without the same-shape caveat")

    print(f"publication pages      : {pages}")
    print(f"docket rows per page   : {DOCKET_ROWS} (structural errors above if not)")
    print(f"unanswered rows        : {silent_rows}")
    print(f"gaps listed to readers : {gaps_total}")
    print(f"rankings recomputed    : {claims_checked}")
    print(f"problems               : {len(problems)}")
    for p in problems[:40]:
        print(f"  FAIL {p}")
    if len(problems) > 40:
        print(f"  ... and {len(problems) - 40} more")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
