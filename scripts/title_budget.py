#!/usr/bin/env python3
"""SERP title budget (audit H3, batch 7 - 17 September 2026).

Every rendered <title> (and the og:/twitter: cards that mirror it) should fit
the ~60-char SERP window. This module is the single generator-level choke
point - the same house ladder style batch 4 used for the 719 movie pages:

  1. keep the body intact and shorten the brand suffix
     (full desk suffix -> " | BRYME" -> no suffix);
  2. if the body alone is over budget, trim it at the first deck break
     (em dash, en dash, colon, semicolon, " - ") when that leaves a
     meaningful head (>= 15 chars), then re-run the suffix ladder;
  3. last resort: word-boundary trim (never cut mid-word) against the
     longest suffix that still leaves a meaningful head.

The function is idempotent: titles already inside budget are returned
untouched (whitespace-normalised). It never raises - on any weird input it
falls back to a hard word-boundary trim of the whole string.
"""

from __future__ import annotations

import re

LIMIT = 60        # SERP window we budget against
MIN_HEAD = 15     # a trimmed head shorter than this is a stub, not a title
SEPS = (" \u2014 ", " \u2013 ", ": ", "; ", " - ")

# Break points we prefer when we have to cut a title short.
#
# Punctuation-based rather than "separator plus space", because a separator
# often sits at the very END of the cut with no space after it: the string
# "\u2026get paid by Substack," contains no ", " to find. An earlier version
# searched only for separator-plus-space, missed it, and fell through to the
# dangling-word rule - publishing "\u2026get paid" where "\u2026by Substack" fitted.
#
# Dashes are matched only in their SPACED forms. A bare en dash is how ranges
# are written - "$200\u2013$500" - and treating it as a break cut titles down to
# "Something long here \u2014 $200".
_BREAK = re.compile(r"[,;:?!]| \u2014 | \u2013 | - ")

# Words that cannot end an English title. Conservative on purpose: it lists
# only function words that would leave the fragment ungrammatical, and
# deliberately excludes words that legitimately end a phrase - "it", "over",
# "on", "in", "out", "up", "away". "How to move into it" is a complete title
# and must not be shortened just because "it" is a short word.
_DANGLING = frozenset("""
a an the and or nor but of to for with from by at as than that which whose
in into onto upon about between during through without against per via
""".split())


def _clean(s: str) -> str:
    return " ".join(str(s).split())


def _balance(s: str) -> str:
    """Drop a trailing unclosed bracket or unmatched quote left by a cut.

    "How to become a SaaS writer (and the" is not a title; "How to become a
    SaaS writer" is. Only trailing imbalance is repaired - a balanced pair
    earlier in the string is left alone.
    """
    while s.count("(") > s.count(")") and "(" in s:
        s = s[:s.rfind("(")].strip(" ,;:-\u2014\u2013")
    while s.count("[") > s.count("]") and "[" in s:
        s = s[:s.rfind("[")].strip(" ,;:-\u2014\u2013")
    for open_q, close_q in (("\u201c", "\u201d"), ('"', '"')):
        if s.count(open_q) > s.count(close_q) and open_q in s:
            s = s[:s.rfind(open_q)].strip(" ,;:-\u2014\u2013")
    return s


def _word_trim(body: str, room: int) -> str:
    """Trim to <= room chars, landing on a break a reader would accept.

    Cutting at a word boundary is not enough on its own. It produced live
    search-result titles like "How to become a SaaS writer (and the" and
    "Can a Nigerian writer actually get paid by" - a truncated fragment is a
    worse result than a slightly shorter complete phrase, and it is the first
    line a searcher reads. So, having cut at a word boundary, this walks back
    to the nearest natural break, then strips anything that would dangle, then
    closes or drops unbalanced bracketing.

    Safe to be this aggressive here because this function is only ever reached
    when a title is over budget: titles that fit are returned intact by the
    caller and never pass through it.
    """
    # Trim to a word boundary without yet touching punctuation: a trailing
    # comma IS the natural break we are about to look for, so stripping it
    # first would destroy the boundary and push us onto the dangling-word
    # rule. That is what turned "…get paid by Substack," into "…get paid".
    # Drop a partial word, but KEEP a token that ends on a separator.
    #
    # The original code did body[:room].rsplit(" ", 1)[0] unconditionally,
    # silently discarding the last token even when the cut had landed exactly
    # on a separator. Cutting "Can a Nigerian writer actually get paid by
    # Substack," at 52 chars ends on that comma - and rsplit then threw away
    # "Substack," whole, so the break we were about to search for was already
    # gone. That is how "...get paid by Substack" became "...get paid".
    raw = body[:room]
    if len(body) > room and raw and raw[-1] not in " \t,;:?!\u2014\u2013-":
        raw = raw.rsplit(" ", 1)[0]
    cut = raw.rstrip()
    if not cut:
        return ""

    # 1. Prefer the LAST break inside the cut, so we keep as much of the title
    #    as still reads as a whole phrase rather than the first clause of it.
    #
    #    Commas between digits are thousands separators, not breaks. Without
    #    this test "Communiqué: \u20a6150,000 (or $100 outside Nigeria) per piece"
    #    cut at the comma and published "Communiqué: \u20a6150" - a title that
    #    states a rate ten thousand times too low, on a page whose whole job is
    #    to publish rates accurately.
    def _is_break(m: "re.Match") -> bool:
        if m.start() < MIN_HEAD:
            return False
        if m.group(0) == "," and 0 < m.start() < len(cut) - 1 \
                and cut[m.start() - 1].isdigit() and cut[m.start() + 1].isdigit():
            return False
        return True

    hits = [m for m in _BREAK.finditer(cut) if _is_break(m)]
    if hits:
        m = hits[-1]
        # keep a terminal question or exclamation mark; drop lesser separators
        cut = (cut[:m.end()] if m.group(0) in ("?", "!") else cut[:m.start()])
        cut = cut.strip(" ,;:-\u2014\u2013")

    # 2. Repair bracketing before stripping words, so "(and the" collapses to
    #    the phrase before the bracket rather than to "and".
    cut = _balance(cut)

    # 3. Drop trailing function words that cannot end a title.
    while True:
        parts = cut.split()
        if not parts:
            return ""
        if parts[-1].lower().strip(".,;:()\u2014\u2013-\u201c\u201d\"'") in _DANGLING:
            cut = " ".join(parts[:-1]).strip(" ,;:-\u2014\u2013")
        else:
            break

    return _balance(cut).strip(" ,;:-\u2014\u2013")


def budget_title(t, limit: int = LIMIT) -> str:
    t = _clean(t)
    if len(t) <= limit:
        return t

    # Split the brand suffix at the last " | ".
    body, pipe, brand = t.rpartition(" | ")
    if not pipe:
        body, brand = t, ""
    sufs = []
    if brand:
        sufs.append(" | " + brand)
        if brand != "BRYME":
            sufs.append(" | BRYME")
    sufs.append("")

    # Pass 1: body intact, shorten the suffix (batch-4 movie-ladder order).
    for s in sufs:
        if len(body) + len(s) <= limit:
            return body + s

    # Pass 2: trim the body at the first deck break, then re-run the ladder.
    head = None
    for sep in SEPS:
        if sep in body:
            cand = body.split(sep, 1)[0].strip(" ,-;:\u2014\u2013")
            if len(cand) >= MIN_HEAD:
                head = cand
            break
    if head:
        for s in sufs:
            if len(head) + len(s) <= limit:
                return head + s
        # deck head still too long even bare: word-trim the head itself
        wt = _word_trim(head, limit)
        if len(wt) >= MIN_HEAD:
            return wt

    # Pass 3: word-boundary trim against the longest suffix that leaves room.
    for s in sufs:
        room = limit - len(s)
        if room < MIN_HEAD:
            continue
        wt = _word_trim(body, room)
        if len(wt) >= MIN_HEAD and len(wt) + len(s) <= limit:
            return wt + s

    # Degenerate fallback (single huge token, no suffix): hard trim.
    return _word_trim(body, limit) or t[:limit]


if __name__ == "__main__":  # tiny self-test
    cases = [
        ("Short | BRYME", "Short | BRYME"),
        ("The shelves \u2014 every film the desk covers | BRYME Entertainment",
         "The shelves \u2014 every film the desk covers | BRYME"),
        ("Australian tax for freelance writers \u2014 the $18,200 threshold, the "
         "$75,000 GST line, and the super trap | BRYME",
         "Australian tax for freelance writers | BRYME"),
        ("Solo Leveling vs Hunter x Hunter: the similarities and the "
         "differences explained | BRYME",
         "Solo Leveling vs Hunter x Hunter | BRYME"),
    ]
    # Regressions from the 30 September sweep of 354 source titles. Left column
    # is the source, right is what the old word-boundary trim published.
    REGRESSIONS = [
        ("How to become a SaaS writer (and the budget trap nobody warns you "
         "about) | BRYME writing guides",
         "How to become a SaaS writer | BRYME writing guides"),
        ("How to choose a grammar checker (and why \"best\" is the wrong "
         "question) | BRYME writing guides",
         "How to choose a grammar checker | BRYME writing guides"),
        ("Gutter: flat \u00a350 per piece, Scottish and international writing | "
         "BRYME",
         "Gutter: flat \u00a350 per piece | BRYME"),
        ("Broadview: 40\u00a2 a word for opinion, 65\u00a2 a word for reported "
         "features | BRYME",
         "Broadview: 40\u00a2 a word for opinion | BRYME"),
        # Thousands separator, not a break point: cutting here published
        # "Communiqu\u00e9: \u20a6150" - a rate ten thousand times too low.
        ("Communiqu\u00e9: \u20a6150,000 (or $100 outside Nigeria) per "
         "contributed piece | BRYME",
         "Communiqu\u00e9: \u20a6150,000 (or $100 outside Nigeria) | BRYME"),
    ]
    # Must NOT be shortened: complete phrases that happen to end on a short word.
    UNTOUCHED = [
        "UX writing \u2014 what it pays and how to move into it | BRYME",
        "Onchain publishing for writers is quietly over | BRYME",
    ]
    # The suite below is called BOTH with and without a brand suffix, because
    # the builders do both and the answer differs: with a suffix there is less
    # room, so the cut lands in a different place. A sweep that only tested one
    # form reported this file clean while the built pages still said
    # "get paid by | BRYME".
    SUFFIXED = [
        ("Can a Nigerian writer actually get paid by Substack, Medium or "
         "Vocal? | BRYME",
         "Can a Nigerian writer actually get paid by Substack | BRYME"),
    ]

    def run(src, want):
        got = budget_title(src)
        assert len(got) <= LIMIT, (len(got), got)
        assert budget_title(got) == got, f"not idempotent: {got!r}"
        return got, want

    for src, want in cases + REGRESSIONS + SUFFIXED:
        got, _ = run(src, want)
        print(("OK  " if got == want else "DIFF") + f" [{len(got)}] {got}")
        if got != want:
            print(f"       wanted: {want}")
    for src in UNTOUCHED:
        got, _ = run(src, None)
        print(("OK  " if got == src else "DIFF") + f" [untouched {len(got)}] {got}")
