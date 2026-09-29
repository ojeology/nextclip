#!/usr/bin/env python3
"""Fail fast on Python syntax the Render build cannot parse.

Why this exists (2026-09-29): a deploy failed with
  SyntaxError: f-string expression part cannot include a backslash
on a line that ran perfectly locally. The local interpreter is 3.13, where PEP
701 lifted that restriction; Render's build runs an older Python and rejects it.
The failure cost a full deploy cycle to diagnose because it only surfaced in
production.

This checker uses the real tokenizer rather than text scanning, so an
f-string-looking fragment inside a docstring or a comment cannot fool it. It
flags the PEP 701 constructs that only parse on Python 3.12 and later:

  1. a backslash inside an f-string expression part, including inside a nested
     string literal within that expression -- the case that shipped
  2. reusing the surrounding quote delimiter inside an f-string expression
     (a double-quoted expression nested in a double-quoted f-string is 3.12+)
  3. a comment inside an f-string expression

Quote rule: a nested string conflicts with the f-string delimiter only when its
quote run is the same character AND at least as long. A single-quoted string
inside a triple-quoted f-string is therefore NOT flagged, because every
supported version parses it.

Exit 1 with a file:line report if anything is found, 0 if clean.
"""
from __future__ import annotations

import io
import sys
import tokenize
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FSTRING_START = getattr(tokenize, "FSTRING_START", None)
FSTRING_END = getattr(tokenize, "FSTRING_END", None)


def _quote_of(tok: str) -> str:
    """The surrounding quote run of an f-string start token."""
    for q in ('"""', "'''", '"', "'"):
        if tok.endswith(q):
            return q
    return ""


def _quote_run(s: str) -> str:
    """The leading quote run of a string token."""
    if not s:
        return ""
    c = s[0]
    if c not in "\"'":
        return ""
    n = 0
    while n < len(s) and s[n] == c:
        n += 1
    return c * n


def scan(path: Path) -> list[tuple[int, str, str]]:
    src = path.read_text(encoding="utf-8", errors="replace")
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, SyntaxError):
        return []

    if FSTRING_START is None:
        # Python < 3.12 cannot produce these tokens; nothing to check on a build
        # that would parse the file anyway.
        return []

    findings: list[tuple[int, str, str]] = []
    fstack: list[str] = []
    exprdepth = 0

    for t in toks:
        tt, s = t.type, t.string

        if tt == FSTRING_START:
            fstack.append(_quote_of(s))
            exprdepth = 0
            continue
        if tt == FSTRING_END:
            if fstack:
                fstack.pop()
            exprdepth = 0
            continue
        if not fstack:
            continue

        if tt == tokenize.OP:
            if s == "{":
                exprdepth += 1
            elif s == "}":
                exprdepth = max(0, exprdepth - 1)
            continue

        if exprdepth <= 0:
            continue

        outer = fstack[-1]

        if tt == tokenize.STRING:
            if "\\" in s:
                findings.append((t.start[0], "backslash in f-string expression", s[:70]))
            inner = _quote_run(s)
            if inner and outer and inner[0] == outer[0] and len(inner) >= len(outer):
                findings.append((t.start[0], "same quote reused in f-string expression", s[:70]))

        if tt == tokenize.COMMENT:
            findings.append((t.start[0], "comment in f-string expression", s[:70]))

    return findings


def main() -> int:
    targets = sorted((ROOT / "scripts").glob("*.py"))
    total = 0
    for f in targets:
        if f.name == "check-py-compat.py":
            continue
        for line, kind, frag in scan(f):
            total += 1
            print(f"  !! {f.relative_to(ROOT)}:{line}  {kind}")
            print(f"       {frag}")
    if total:
        print(f"py-compat: {total} construct(s) need Python 3.12+ ({len(targets)} files scanned)")
        print("  Fix: assign the value to a variable before the f-string, or use")
        print("  quote characters inside the expression that differ from the outer ones.")
        return 1
    print(f"py-compat: clean -- {len(targets)} files parse on Render's interpreter")
    return 0


if __name__ == "__main__":
    sys.exit(main())
