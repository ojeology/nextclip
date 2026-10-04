#!/usr/bin/env python3
"""Phase 17 — is the Writers section one coherent product?

The roadmap asks for consistency across nine things: navigation, typography,
components, breadcrumbs, research labels, verification indicators, tool design,
internal linking and calls to action. "Consistent" is only meaningful if it is
measured, so each of the nine is checked mechanically here and any page that
breaks the pattern is named.

Two rules keep this honest:

* The navigation is compared AFTER removing `aria-current="page"`. That attribute
  marks the section a reader is in, so it MUST differ page to page; comparing raw
  markup would report five variants and call correct behaviour a defect.
* Pages that are noindex redirect stubs, and the section root itself, are exempt
  from breadcrumbs. They are not part of the reading experience the check is
  about, and requiring a breadcrumb on a 400-word redirect would be noise.

Run: python3 scripts/audit-brand-consistency.py
Exits non-zero on any finding.
"""
from __future__ import annotations

import collections
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path


def _today() -> str:
    """The date this report should carry.

    Both the payload and the filename used to be the literal "2026-09-30", so
    every later run overwrote that day's artifact with a later tree's numbers -
    a report labelled with a date it was not run against, which is the one thing
    a dated artifact must not be. Honours SOURCE_DATE_EPOCH like the builders so
    CI stays reproducible.
    """
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "")
    if epoch.isdigit():
        return dt.datetime.fromtimestamp(int(epoch), dt.timezone.utc).date().isoformat()
    return dt.date.today().isoformat()


TODAY = _today()

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
SECT = PUB / "writers"
ROBOTS = re.compile(r'<meta\s+name="robots"\s+content="([^"]*)"', re.I)
NAV = re.compile(r'<nav class="main-nav".*?</nav>', re.S)
CRUMB = re.compile(r'<nav class="breadcrumb">(.*?)</nav>', re.S)

# CTA classes the section is allowed to use. A new one is not automatically
# wrong - it means a designer made a decision, and it should be recorded here
# deliberately rather than appearing silently.
CTA_OK = {"btn", "btn secondary", "btn ghost", "btn secondary tk-importlabel"}

# A page may add one stylesheet of its own on top of the universal base sheet.
# The hub does it for the card grid it needs. The portfolio builder does it
# because its live preview must render the standalone document the tool
# generates - that document carries its own type scale (Georgia headings,
# system-ui body) because it is the product, not the section chrome. Recorded
# per route like CTA_OK, so a future deviation is still a visible decision.
EXTRA_SHEET_OK = {
    ("/writers/tools/portfolio-builder/", "/assets/writer-portfolio-builder.css"),
}


def pages() -> list[tuple[str, Path, str]]:
    out = []
    for f in sorted(SECT.rglob("index.html")):
        h = f.read_text(encoding="utf-8", errors="replace")
        route = "/" + f.parent.relative_to(PUB).as_posix() + "/"
        out.append((route, f, h))
    return out


def is_noindex(h: str) -> bool:
    m = ROBOTS.search(h)
    return bool(m and "noindex" in m.group(1).lower())


def is_stub(route: str, h: str) -> bool:
    return is_noindex(h) or route == "/writers/"


def main() -> int:
    P = pages()
    findings: list[str] = []
    print(f"Phase 17 — Writers section coherence  ({len(P)} pages)\n")

    # 1. navigation -----------------------------------------------------------
    nav_norm: dict[str, str] = {}
    for route, _f, h in P:
        m = NAV.search(h)
        if not m:
            findings.append(f"navigation: no main-nav on {route}")
            continue
        x = re.sub(r"\s+", " ", m.group(0)).replace(' aria-current="page"', "")
        nav_norm.setdefault(hashlib.md5(x.encode()).hexdigest()[:8], []).append(route)
    print(f"1 navigation          : {len(nav_norm)} distinct menu(s) across {len(P)} pages")
    for k, v in sorted(nav_norm.items(), key=lambda kv: -len(kv[1])):
        print(f"     {len(v):4} pages  {k}   e.g. {v[0]}")
    if len(nav_norm) > 1:
        findings.append(f"navigation: {len(nav_norm)} distinct menus")

    # 2. typography -----------------------------------------------------------
    # What matters is that the BASE stylesheet is universal; a page may add one
    # on top of it for layout specific to that page. Demanding a single
    # stylesheet site-wide would flag the section hub for loading the card-grid
    # sheet it legitimately needs.
    css = collections.Counter()
    sheets_by_route: dict[str, list[str]] = {}
    for route, _f, h in P:
        sheets = re.findall(r'<link[^>]+href="(/assets/[^"]+\.css)"', h)
        sheets_by_route[route] = sheets
        for s in sheets:
            css[s] += 1
    base = [s for s, n in css.items() if n == len(P)]
    extras: dict[str, list[str]] = collections.defaultdict(list)
    for route, sheets in sheets_by_route.items():
        for s in sheets:
            if s not in base:
                extras[s].append(route)
    print(f"2 typography          : base {base} on all {len(P)} pages; "
          f"additions {dict((s, len(v)) for s, v in extras.items())}")
    if len(base) != 1:
        findings.append(f"typography: {len(base)} base stylesheets, expected 1")
    for s, v in extras.items():
        stray = [r for r in v if r != "/writers/" and (r, s) not in EXTRA_SHEET_OK]
        if stray:
            findings.append(f"typography: supplementary {s} used outside the section hub: {stray[:4]}")

    # 3. components -----------------------------------------------------------
    comps = set()
    for _r, _f, h in P:
        comps.update(c for c in re.findall(r'class="(chip-card|path-card|card-num|card-link|'
                                           r'docket-row|docket-note|verify-badge|trust-action)"', h))
    print(f"3 components          : {len(comps)} shared component classes in use")

    # 4. breadcrumbs ----------------------------------------------------------
    no_crumb = []
    wrong_root = []
    for route, _f, h in P:
        if is_stub(route, h):
            continue
        m = CRUMB.search(h)
        if not m:
            no_crumb.append(route)
            continue
        if 'href="/writers/"' not in m.group(1):
            wrong_root.append(route)
    print(f"4 breadcrumbs         : {len(P) - len(no_crumb) - len(wrong_root)} ok, "
          f"{len(no_crumb)} missing, {len(wrong_root)} not rooted at /writers/")
    for r in no_crumb:
        findings.append(f"breadcrumbs: {r} has none")
    for r in wrong_root:
        findings.append(f"breadcrumbs: {r} is not rooted at /writers/")

    # 5 + 6. research labels and verification indicators on records ----------
    recs = [t for t in P if t[0].startswith("/writers/writing/") and not is_stub(t[0], t[2])
            and t[0] != "/writers/writing/"]
    no_docket = [r for r, _f, h in recs if 'id="docket"' not in h]
    no_badge = [r for r, _f, h in recs if 'class="verify-badge' not in h]
    print(f"5 research labels     : {len(recs) - len(no_docket)}/{len(recs)} publication records carry the docket")
    print(f"6 verification badge  : {len(recs) - len(no_badge)}/{len(recs)} publication records carry the badge")
    for r in no_docket:
        findings.append(f"research labels: {r} has no docket")
    for r in no_badge:
        findings.append(f"verification: {r} has no verify-badge")

    # 7. tool design ----------------------------------------------------------
    tools = [t for t in P if t[0].startswith("/writers/tools/") and t[0] != "/writers/tools/"]
    dead = [r for r, _f, h in tools
            if "<input" not in h and not re.search(r'<script[^>]+src="/assets/[^"]*tool[^"]*\.js"', h)]
    print(f"7 tool design         : {len(tools) - len(dead)}/{len(tools)} tool pages interactive (input or bundle)")
    for r in dead:
        findings.append(f"tool design: {r} is not interactive")

    # 8. internal linking -----------------------------------------------------
    # Count inbound links site-wide, and credit a link to a redirect stub to the
    # page it canonically points at. Resolving both ways matters: /writers/studio/
    # is linked from every page in the site through the /studio/ stub, so a
    # section-only <main> scan calls it an orphan when it is one of the best
    # linked pages on the site.
    canon: dict[str, str] = {}
    for f in PUB.rglob("index.html"):
        h = f.read_text(encoding="utf-8", errors="replace")
        r = "/" + f.parent.relative_to(PUB).as_posix() + "/"
        m = re.search(r'<link rel="canonical" href="https://thebryme\.com([^"]*)"', h)
        canon[r] = m.group(1) if m else r

    def resolve(href: str) -> str:
        href = href if href == "/" else "/" + href.strip("/") + "/"
        seen = set()
        while href in canon and canon[href] != href and href not in seen:
            seen.add(href)
            href = canon[href]
        return href

    inbound: collections.Counter = collections.Counter()
    for f in PUB.rglob("index.html"):
        h = f.read_text(encoding="utf-8", errors="replace")
        src = "/" + f.parent.relative_to(PUB).as_posix() + "/"
        for href in set(re.findall(r'href="(/[^"#?]*)"', h)):
            t = resolve(href)
            if t != src:
                inbound[t] += 1
    orphans = [r for r, _f, h in P if not is_stub(r, h) and inbound.get(r, 0) == 0]
    print(f"8 internal linking    : {len(P) - len(orphans)}/{len(P)} pages have inbound links "
          f"(site-wide, redirects resolved)")
    for r in orphans:
        findings.append(f"internal linking: {r} has no inbound link anywhere on the site")

    # 9. calls to action ------------------------------------------------------
    ctas = collections.Counter()
    for _r, _f, h in P:
        for c in re.findall(r'class="(btn[^"]*)"', h):
            ctas[c] += 1
    unexpected = {k: v for k, v in ctas.items() if k not in CTA_OK}
    print(f"9 calls to action     : {len(ctas)} distinct button classes {dict(ctas)}")
    for k, v in unexpected.items():
        findings.append(f"CTA: unexpected button class '{k}' ({v} uses)")

    print(f"\nfindings: {len(findings)}")
    for f in findings:
        print(f"  FAIL {f}")

    report = {"generated": TODAY, "pages": len(P), "dimensions": 9,
              "navVariants": len(nav_norm), "findings": findings}
    out = ROOT / "reports" / f"brand-consistency-{TODAY}.json"
    out.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
