#!/usr/bin/env python3
"""Apply the simultaneous-submissions policy to the 101 branch-only records.

WHAT THIS COMPLETES
-------------------
Main's Phase 4 added simultaneousSubmissions / simultaneousNote to its 147
records. This branch predates that and added 101 records of its own, so after
the merge those 101 would still have no answer for the eighth question in every
publication docket. scripts/backfill-simultaneous.py fetched each record's own
guideline; this script records what those pages say.

The 147 records shared with main are deliberately NOT touched. Main already
carries Phase 4's values for them, and writing our own would turn a clean merge
into a conflict over 147 records that are already answered.

HOW THE DECISION WAS MADE
-------------------------
By reading. All 101 pages were fetched and read on 2026-09-30. Nothing here is
classified by keyword, because Phase 4 documented that keyword classification
was wrong at nearly every step:

  - Cholla Needles: "we do not appreciate or accept simultaneous submissions."
    Contains the substring "accept simultaneous submissions".
  - Peach: "Because we do not accept simultaneous submissions" and later
    "While Peach does not consider simultaneous submissions".
  - Hanging Loose: "We do not accept simultaneous submissions."
  - The New Verse News: "No simultaneous submissions."
  - Stygian Lepus: "No simultaneous submissions, please, they will be
    disqualified."
  - The Fictional Cafe: "submitted exclusively to us. We do not accept
    simultaneous submissions..."

Those seven all state a refusal and are the reason REFUSE_BY_WORD exists as an
explicit list rather than a regex.

THE ONE THAT NEVER SAYS THE WORD
--------------------------------
Modern Haiku refuses without ever using "simultaneous":

    "Material submitted to Modern Haiku is to be the author's original work,
     previously unpublished and not under consideration by any other
     publication, including Web-based journals."

A keyword pass over the word "simultaneous" reports this market as silent. It
is not silent; it refuses. It is carried in REFUSE_BY_MEANING with its anchor
phrase, which is the same discipline Phase 4 applied when it found two
publications answering only in an FAQ.

Foreign Affairs is recorded as a refusal for a related reason. Its guideline
reads: "Unless otherwise informed, we assume any piece submitted to us is being
offered exclusively..." That is a presumption of exclusivity, so the answer a
writer needs is "no, unless you tell them". The full sentence is kept in the
note so the "unless otherwise informed" survives into the record.

WHAT IS RECORDED FOR EVERY OTHER ACCEPTED MARKET
------------------------------------------------
The exact sentence, its URL and the reading date - the same shape Phase 4 used.
Sentences are extracted from the saved page text by anchor, never retyped, so a
note cannot drift from its source.

Every record whose page never mentions submitting elsewhere is recorded
"not-stated". That is a real answer, not a gap: it is what the guideline says.
Phase 4 found the same thing for two-thirds of the literary markets it read.

Usage:
    python3 scripts/apply-simultaneous-backfill.py --dry-run
    python3 scripts/apply-simultaneous-backfill.py
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
TEXT = ROOT / "research/backfill"
V = "2026-09-30"

# A stated refusal that does use the word. Listed explicitly, never matched.
REFUSE_BY_WORD = {
    "cholla-needles": "simultaneous",
    "hanging-loose": "simultaneous",
    "peach-gcsu": "simultaneous",
    "stygian-lepus": "simultaneous",
    "the-fictional-cafe": "simultaneous",
    "the-new-verse-news": "simultaneous",
    "foreign-affairs": "offered exclusively",
}

# Stated refusals that never say "simultaneous". Anchor phrase -> the sentence
# is pulled from the page by that phrase.
REFUSE_BY_MEANING = {
    "modern-haiku": "not under consideration by any other publication",
}


# Verbs that carry a policy. Used to reject a bare heading as a quote.
POLICY_WORDS = re.compile(
    r"\b(accept|accepts|accepted|allow|allows|welcome|welcomes|consider|considers|"
    r"fine|permit|permitted|okay|ok|encourage|encourages|disclosure|mind|"
    r"do not|don't|does not|doesn't|no |not |never|refuse|decline|disqualif)\b", re.I)


def logical_lines(text: str) -> list[str]:
    """Rejoin a wrapped sentence without ever gluing a heading onto the next line.

    The saved text is one paragraph or heading per line. A sentence that wraps
    ("...timely\\nresponse.") must be rejoined or the quote is recorded as a
    half-sentence. But a heading ("Multiple and Simultaneous Submissions") must
    NOT be glued to the sentence under it, which is what a blanket whitespace
    collapse did - and which produced quotes about multiple submissions filed
    under a simultaneous-submissions policy for Cast of Wonders and Pseudopod.

    The rule: continue a line only when the next line reads as a continuation,
    i.e. it starts lower-case, a digit, or an opening bracket or quote.
    """
    out: list[str] = []
    for raw in text.split("\n"):
        line = re.sub(r"\s+", " ", raw).strip()
        if not line:
            continue
        if out and not re.search(r"[.!?:]$", out[-1]) and \
                re.match(r"^(?:[a-z0-9(\[\u201c\"'])", line):
            out[-1] = out[-1] + " " + line
        else:
            out.append(line)
    return out


def _sentences(lines: list[str]) -> list[str]:
    sents: list[str] = []
    for line in lines:
        for s in re.split(r"(?<=[.!?])\s+", line):
            s = s.strip()
            if s:
                sents.append(s)
    return sents


def sentence_at(text: str, anchor: str) -> str | None:
    """The sentence containing `anchor`, taken verbatim from the page text.

    Where a page mentions the anchor more than once - usually a heading and then
    the policy itself - the sentence that reads like a policy wins, so a heading
    is never quoted as the rule. Nothing is retyped: the returned string is a
    slice of the page text.
    """
    # A leading list marker is markup, not the sentence.
    sents = [re.sub(r"^[\*\u2022\u2713\u2013\u2014\-\s]+", "", s)
             for s in _sentences(logical_lines(text))]
    sents = [s for s in sents if s]
    cands = [s for s in sents if anchor.lower() in s.lower()]
    if not cands:
        return None
    scored = sorted(
        cands,
        key=lambda s: (1 if POLICY_WORDS.search(s) else 0,
                       -abs(len(s) - 180)),   # prefer a readable policy sentence
        reverse=True,
    )
    return scored[0]


def tidy(s: str) -> str:
    """Tighten spacing around punctuation, and nothing else.

    A source page often renders a space before a full stop because an inline tag
    sits there: "requests to review books <em>.</em>" comes out as "review books .".
    That is a transcription artefact of the markup, not something the publication
    wrote, and the desk's own audit_dockets.py rejects it as "space before
    punctuation". Normalising it changes no word, and the note stays a slice of
    the page otherwise.

    This was found by the merge rehearsal, not on the branch: the branch's docket
    does not render the note, so three records sat here with ' .' until main's
    eighth docket row started printing them and audit_dockets.py failed.
    """
    s = re.sub(r"\s+([.,;:!?])", r"\1", s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\s+\)", ")", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def note_for(slug: str, url: str, text: str, anchor: str) -> str:
    s = sentence_at(text, anchor)
    if not s:
        return f"Stated in the guideline at {url} (read {V})."
    return f"{tidy(s)} \u2014 {url} (read {V})"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="recompute the field for scoped records that already have it")
    args = ap.parse_args()

    if not TEXT.is_dir():
        sys.exit(f"no saved page text at {TEXT} - run scripts/backfill-simultaneous.py first")

    data = json.loads(OPPS.read_text(encoding="utf-8"))
    recs = data["opportunities"]

    # Only branch-only records: the 147 shared with main already carry Phase 4.
    import subprocess
    try:
        main_json = subprocess.run(
            ["git", "show", "FETCH_HEAD:content/opportunities.json"],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout
        shared = {o["slug"] for o in json.loads(main_json)["opportunities"]}
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"cannot read main's record set to scope the backfill ({exc}).\n"
                 "Run: git fetch --depth 1 origin main")

    # Scope is ALWAYS the explicit branch-only target list, so --force can never
    # reach back into a record that a previous batch already answered.
    tp = ROOT / "research/backfill-targets.json"
    if tp.exists():
        targets = set(json.loads(tp.read_text()))
        todo = [r for r in recs if r["slug"] in targets and r["slug"] not in shared]
    else:
        todo = [r for r in recs
                if r["slug"] not in shared
                and (args.force or "simultaneousSubmissions" not in r)]

    accepted = refused = silent = missing = 0
    applied = []
    for rec in todo:
        slug = rec["slug"]
        p = TEXT / f"{slug}.txt"
        if not p.exists():
            missing += 1
            print(f"  SKIP {slug}: no saved page text")
            continue
        text = p.read_text(encoding="utf-8")
        url = rec.get("officialUrl") or rec.get("applyUrl") or ""

        if slug in REFUSE_BY_WORD:
            val = "not-accepted"
            note = note_for(slug, url, text, REFUSE_BY_WORD[slug])
            refused += 1
        elif slug in REFUSE_BY_MEANING:
            val = "not-accepted"
            note = note_for(slug, url, text, REFUSE_BY_MEANING[slug])
            refused += 1
        elif re.search(r"simultaneous", text, re.I):
            val = "accepted"
            note = note_for(slug, url, text, "simultaneous")
            accepted += 1
        else:
            val = "not-stated"
            note = None
            silent += 1

        rec["simultaneousSubmissions"] = val
        rec["simultaneousNote"] = note
        applied.append((slug, val))

    # Guard: the merge rehearsal caught three notes carrying a space before the
    # full stop, which audit_dockets.py rejects once main's docket renders the
    # note. Refuse to write that shape again.
    offenders = [r["slug"] for r in todo
                 if r.get("simultaneousNote") and re.search(r"\s+[.,;:!?]", r["simultaneousNote"])]
    if offenders:
        sys.exit(f"ERROR: space before punctuation in note for: {offenders}")

    if not args.dry_run:
        data["opportunities"] = recs
        OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")

    print(f"\nrecords in scope        : {len(todo)}")
    print(f"  accepted              : {accepted}")
    print(f"  not-accepted          : {refused}")
    print(f"  not-stated (page silent): {silent}")
    if missing:
        print(f"  no page text (skipped) : {missing}")
    print(f"\n{'DRY RUN - nothing written' if args.dry_run else 'written to content/opportunities.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
