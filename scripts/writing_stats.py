#!/usr/bin/env python3
"""Dataset statistics that pages publish, computed once and shared.

Why this module exists
----------------------
Nine guides under content/hub/guides published counts drawn from the
opportunities dataset as hand-typed literals - "41 of 142 verified
publications prohibit AI-assisted work", "only 55 of 142 state their rights
terms". Every one of those was true when it was written and every one of them
has been drifting ever since, silently, because nothing connected the sentence
to the data it described.

The desk's own data report, State of Paid Writing 2026, already had the right
answer: compute every figure from content/opportunities.json at build time.
This module gives the guides the same footing. Guides reference figures as
{{tokens}}; build-writing-hub.py fills them in load_guides(), which is the one
place every guide passes through - so a figure cannot reach a page uncomputed.

The counting rules are stated explicitly below because a number in a published
guide has to be auditable. Each one is a rule, not a judgement call made per
record.

Money note: BRYME publishes no rate here, so these are all counts, not amounts.
"""
from __future__ import annotations

import json
import pathlib
import re
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
_OPPS = ROOT / "content" / "opportunities.json"

# The site's own canonical fold, mirrored from AI_POLICY_MAP in
# build-writing-first.py so a page cannot disagree with the record card it
# links to. "limited" and "disclosure-required" land on "disclosure", which is
# not a prohibition, so they are counted separately below.
_AI_PROHIBITING = ("prohibited", "no-ai", "strict")
_AI_DISCLOSURE = ("disclosure-required", "limited")

# A rights field counts as STATING terms only when it describes what the
# publication acquires. Three shapes do not qualify:
#   - blank
#   - an explicit disclaimer ("Not publicly stated on the pitch page.")
#   - an explicit partial ("Not fully stated on the submit page.")
# The guides' own framing is "either say nothing, or say something so partial
# it cannot be relied on", so partial and silent are counted together there.
_RIGHTS_ABSENT = re.compile(
    r"^\s*(not stated|not publicly stated|not fully stated|unknown|n/?a|none|—|-)\b",
    re.I)


def _load() -> list[dict]:
    return json.loads(_OPPS.read_text(encoding="utf-8"))["opportunities"]


def _countries() -> dict:
    return json.loads((ROOT / "content" / "hub" / "pub-countries.json")
                      .read_text(encoding="utf-8"))


# A per-word rate is a rate expressed against words. The dataset has no
# rate-basis field, so this is inferred from the stated display - and the rule
# is deliberately narrow: "per word", "/word" or "cents per word". It does NOT
# match a word count in a flat fee ("From $300 for 500-600 words" is a per-piece
# figure that happens to mention words), which a looser \bword\b test swallowed
# when this was first written.
_PER_WORD = re.compile(r"(?:per\s+word|/word|cents?\s+per\s+word|\bper\b[^.\n]{0,12}\bword\b)", re.I)


def pay_shape(rec: dict) -> str:
    """"word" when the stated rate is quoted against words, else "piece".

    Lives here rather than in each builder so the guides and the publication
    dockets classify a record the same way. The docket leans on this: it only
    places a rate against other records of the same shape, because a per-word
    rate and a flat fee are not the same quantity and averaging them across a
    cohort produces a comparison that reads as precise and is not.
    """
    return "word" if _PER_WORD.search(
        str((rec.get("pay") or {}).get("display") or "")) else "piece"


def based(iso: str) -> dict:
    """Counts and pay distribution for the records based in one market.

    Definitions, all testable against the records:

      total          every record the country map places in this market
      states_figure  a numeric stated minimum (pay.amountMin > 0). This is the
                     population the rate percentiles are computed over, so the
                     table and the counts describe the same set.
      silent         total - states_figure: no numeric figure published. These
                     are not necessarily unpaid - the dataset's own position is
                     that "not stated" is a finding, not a zero.
      per_word       of those that state a figure, how many quote it per word
                     rather than as a flat fee. Narrow pattern on purpose; see
                     _PER_WORD.
      min/p25/median/p75/max   the stated minimums, in the currency quoted.

    The earlier hand-written version of this guide counted "43 publish a
    per-piece figure" and "14 quote a per-word rate" and "18 publish no figure"
    - three labels that cannot be reconciled with each other or with the data
    today, because 43 already contains the per-word markets. Recomputing meant
    fixing the labels to say what they measure.
    """
    recs = _load()
    countries = _countries()
    mine = [r for r in recs if (countries.get(r["slug"]) or {}).get("base") == iso]
    stated = [r for r in mine if (r.get("pay") or {}).get("amountMin") or 0]
    values = sorted((r["pay"]["amountMin"]) for r in stated)
    per_word = sum(1 for r in stated if pay_shape(r) == "word")

    def pct(p: float) -> int:
        """Linear-interpolated percentile, rounded to whole currency units.

        Rounded because the guide prints these beside published rates, which
        are whole numbers; half-up so 42.5 reads $43 rather than Python's
        banker's-rounding answer of $42.
        """
        if not values:
            return 0
        k = (len(values) - 1) * p
        f = int(k)
        c = min(f + 1, len(values) - 1)
        v = values[f] + (values[c] - values[f]) * (k - f)
        return int(v + 0.5)

    import statistics as _st
    return {
        "total": len(mine),
        "states_figure": len(stated),
        "silent": len(mine) - len(stated),
        "per_word": per_word,
        "min": values[0] if values else 0,
        "p25": pct(0.25),
        "median": int(_st.median(values)) if values else 0,
        "p75": pct(0.75),
        "max": values[-1] if values else 0,
    }


def rights_bucket(rec: dict) -> str:
    text = str(rec.get("rights") or "").strip()
    if not text:
        return "empty"
    if not _RIGHTS_ABSENT.match(text):
        return "stated"
    if text.lower().startswith("not fully stated"):
        return "partial"
    return "silent"


# ---------------------------------------------------------------------------
# "States clearly that copyright stays with the author"
#
# A separate question from rights_bucket above. rights_bucket asks whether the
# guideline addresses rights AT ALL; this asks whether it says who ends up
# OWNING the work. The State of Paid Writing report used to answer the second
# question with a startswith test - the rights text had to BEGIN with "copyright
# remains", "author retains" and four other openers. At 147 records that counted
# 8. At 288 it still counted 8, while 72 more records said the same thing in
# different words, usually after naming what the magazine buys first:
#
#   "Adi acquires first exclusive, world English-language publication rights.
#    Copyright remains with the author."                      -> missed
#   "Pays for first serial rights; copyright remains with the author." -> missed
#   "Following publication, all rights revert back to the author."     -> missed
#
# So the report published "only 8 of 288 state clearly that copyright remains
# with the author. The other 280 are silent or vague" - telling writers that 280
# publications had not answered a question that 72 of them had answered plainly.
# That is the same defect class as rendering an unread guideline as the
# publication's silence: a false claim about somebody else's magazine.
#
# Two phrases look like retention and are not, and both were caught by reading
# every classified record rather than by reasoning about the regex:
#   "Send only work for which you hold copyright."   - an eligibility rule for
#     submitting, saying nothing about who owns the work afterwards.
#   "No specific rights transfer is stated on the submissions page." - the text
#     itself reports that nothing is stated, so it cannot be a statement.
# Ownership moving the other way is excluded too ("copyright ... transfer to
# Listverse Limited", "becomes the owner of the article").
_RETAIN = re.compile(
    r"(?:copyright|rights?)\s+(?:remain|remains|stay|stays|rest|rests|revert"
    r"|reverts|reverted|return|returns)"
    r"|(?:author|writer|contributor|creator|you)\s+(?:retain|retains|retained"
    r"|keep|keeps|holds?|hold)"
    r"|(?:retain|retains|keep|keeps|holds?)\s+(?:all\s+|full\s+|the\s+"
    r"|other\s+)?(?:rights|copyright)"
    r"|copyright\s+(?:returns|reverts|rests)", re.I)
_TRANSFER_AWAY = re.compile(
    r"transfer(?:s|red)?\s+to\s+(?!the\s+(?:author|writer|contributor))"
    r"|becomes the owner|no further copyright", re.I)
_NOTHING_STATED = re.compile(
    r"no\s+(?:specific\s+|further\s+)?(?:rights\s+)?transfer\s+is\s+stated", re.I)
_SUBMIT_PRECONDITION = re.compile(
    r"(?:send|submit|submissions?|previously published|artists must|must own"
    r"|you (?:must|need to|should))[^.]*(?:hold|holds|own|owns)[^.]*"
    r"(?:copyright|rights)", re.I)


def author_retains(rec: dict) -> bool:
    """True when the record's own rights text says the author keeps copyright."""
    text = str(rec.get("rights") or "").strip()
    if not text:
        return False
    if not _RETAIN.search(text):
        return False
    return not (_TRANSFER_AWAY.search(text) or _NOTHING_STATED.search(text)
                or _SUBMIT_PRECONDITION.search(text))


def compute() -> dict:
    recs = _load()
    n = len(recs)

    ai = {}
    for rec in recs:
        ai[str(rec.get("aiPolicy") or "not-stated")] = ai.get(
            str(rec.get("aiPolicy") or "not-stated"), 0) + 1
    ai_prohibiting = sum(ai.get(k, 0) for k in _AI_PROHIBITING)
    ai_disclosure = sum(ai.get(k, 0) for k in _AI_DISCLOSURE)
    ai_silent = ai.get("not-stated", 0)

    rights = {"stated": 0, "partial": 0, "silent": 0, "empty": 0}
    author_keeps = 0
    for rec in recs:
        rights[rights_bucket(rec)] += 1
        if author_retains(rec):
            author_keeps += 1
            # A record that says the author keeps the copyright has, by
            # definition, addressed rights - so this bucket must sit inside
            # "stated". Asserted rather than assumed: the guide library
            # publishes rights_stated and the data report publishes this
            # figure, and if the nesting ever broke the two pages would
            # contradict each other in public.
            assert rights_bucket(rec) == "stated", (
                f"writing_stats: {rec.get('slug')} says the author retains "
                f"copyright but rights_bucket() calls it "
                f"{rights_bucket(rec)!r} - the two published figures would "
                f"disagree")
    # "cannot be relied on" = everything that is not a full statement
    rights_unreliable = n - rights["stated"]

    _indem = re.compile(r"indemnif|liabilit|\bliabl", re.I)
    indemnity = sum(
        1 for rec in recs
        if _indem.search(json.dumps({k: v for k, v in rec.items() if k != "pay"},
                                    ensure_ascii=False)))

    stamps = sorted(str(r.get("lastVerified") or "")[:10] for r in recs)
    stamps = [s for s in stamps if s]
    window = ""
    if stamps:
        first, last = date.fromisoformat(stamps[0]), date.fromisoformat(stamps[-1])
        window = f"{first.strftime('%-d %B')}–{last.strftime('%-d %B %Y')}"

    us = based("US")

    return {
        "records": n,
        "ai_prohibiting": ai_prohibiting,
        "ai_disclosure": ai_disclosure,
        "ai_silent": ai_silent,
        "rights_stated": rights["stated"],
        "rights_partial": rights["partial"],
        "rights_unreliable": rights_unreliable,
        "rights_author_keeps": author_keeps,
        # Of the records that address rights at all, how many never say who
        # ends up owning the work. Derived, not counted separately, so the two
        # figures on the page cannot fail to add up.
        "rights_stated_no_owner": rights["stated"] - author_keeps,
        "indemnity": indemnity,
        "verified_window": window,
        "based_us": us["total"],
        "us_states_figure": us["states_figure"],
        "us_silent": us["silent"],
        "us_per_word": us["per_word"],
        "us_min": f'{us["min"]:,}',
        "us_p25": f'{us["p25"]:,}',
        "us_median": f'{us["median"]:,}',
        "us_p75": f'{us["p75"]:,}',
        "us_max": f'{us["max"]:,}',
    }


STATS = compute()

# Spelled-out forms, for the places where a sentence reads better with a word
# than a digit ("one record", not "1 record").
_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
          7: "seven", 8: "eight", 9: "nine", 10: "ten"}

TOKENS = dict(STATS)
TOKENS["indemnity_word"] = _WORDS.get(STATS["indemnity"], str(STATS["indemnity"]))

# Deliberately permissive: anything between doubled braces is treated as a
# token and either resolves or raises. An earlier version matched only
# [a-z_]+ , which silently skipped any token containing a digit - so
# {{us_p25}} passed through to the published page as literal text, and the
# validator's own guard had the identical blind spot and missed it too. A
# substitution that fails open is worse than one that fails loudly.
_TOKEN_RE = re.compile(r"\{\{([^{}]*)\}\}")


def fill(text: str) -> str:
    """Replace {{token}} with its computed value. Anything unknown raises."""
    def _sub(m: re.Match) -> str:
        key = m.group(1).strip()
        if key not in TOKENS:
            raise KeyError(
                f"writing_stats: unknown token {{{{{key}}}}} - known tokens: "
                f"{', '.join(sorted(TOKENS))}")
        return str(TOKENS[key])
    return _TOKEN_RE.sub(_sub, text)


def fill_mapping(values: dict) -> dict:
    """Fill tokens across every string in a frontmatter mapping."""
    return {k: (fill(v) if isinstance(v, str)
                else [fill(x) if isinstance(x, str) else x for x in v]
                if isinstance(v, list) else v)
            for k, v in values.items()}


if __name__ == "__main__":
    for k, v in STATS.items():
        print(f"{k:20} {v}")
    print()
    print("check: rights buckets sum to records:",
          STATS["rights_stated"] + STATS["rights_unreliable"] == STATS["records"])
    print("check: retention sits inside rights_stated:",
          STATS["rights_author_keeps"] <= STATS["rights_stated"])
    print("check: ai buckets sum to records:",
          STATS["ai_prohibiting"] + STATS["ai_disclosure"] + STATS["ai_silent"]
          == STATS["records"])
