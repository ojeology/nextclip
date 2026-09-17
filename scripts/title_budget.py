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

LIMIT = 60        # SERP window we budget against
MIN_HEAD = 15     # a trimmed head shorter than this is a stub, not a title
SEPS = (" \u2014 ", " \u2013 ", ": ", "; ", " - ")


def _clean(s: str) -> str:
    return " ".join(str(s).split())


def _word_trim(body: str, room: int) -> str:
    """Trim to <= room chars at a word boundary; strip trailing connectors."""
    wt = body[:room].rsplit(" ", 1)[0].strip(" ,-;:\u2014\u2013")
    return wt


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
    for src, want in cases:
        got = budget_title(src)
        assert len(got) <= LIMIT, (len(got), got)
        print(("OK  " if got == want else "DIFF") + f" [{len(got)}] {got}")
