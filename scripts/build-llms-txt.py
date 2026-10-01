#!/usr/bin/env python3
"""Track B1 (GEO): generate /llms.txt - the machine-readable site summary.

Follows the llms.txt convention: H1 name, blockquote description, H2
sections of curated links. Curated, not a sitemap dump: LLM assistants
get the house, the seven desks, their flagship pages and the tools, with
one honest line each. Every link is asserted to exist in the published
tree, so the file can never advertise a phantom page.

Honesty rules (master brief): no fabricated claims, counts read from the
real sitemaps, review date = today (this file is regenerated each build).
"""
import datetime as _dt
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
ORIGIN = "https://thebryme.com"


def _build_today() -> str:
    """The build date, honouring SOURCE_DATE_EPOCH.

    This file is the last generator that read the wall clock directly, and it
    cost a CI run: the quality workflow pins SOURCE_DATE_EPOCH to the tree's own
    date of record so any commit rebuilds byte-for-byte on any later day, and
    then compares with `git diff --exit-code`. Every other stamp obeyed the pin;
    this one did not, so the moment a build straddled midnight UTC the diff
    failed on the `_Generated <date>_` line alone - and nothing about the site
    had actually changed.

    Same convention as _build_now() in build-writing-first.py, build-routing.py
    and build-ecosystem.py. Behaviour is UNCHANGED when the variable is unset,
    which is what production does: deploys stay date-fresh, only CI is pinned.
    """
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "")
    if epoch.isdigit():
        try:
            return _dt.datetime.fromtimestamp(int(epoch), _dt.timezone.utc).date().isoformat()
        except (OverflowError, OSError, ValueError):
            pass
    return _dt.datetime.now(_dt.timezone.utc).date().isoformat()


TODAY = _build_today()


def sitemap_count(desk):
    p = PUB / desk / "sitemap.xml"
    return len(re.findall(r"<loc>", p.read_text(encoding="utf-8"))) if p.exists() else 0


def sitemap_count_all(desk):
    """Every sitemap for the desk - after the A8-Ent split, entertainment
    publishes a second sitemap for its catalogue pages; both are live pages
    and both count."""
    n = sitemap_count(desk)
    for extra in (PUB / desk).glob("sitemap-*.xml"):
        n += len(re.findall(r"<loc>", extra.read_text(encoding="utf-8")))
    return n


def check(route):
    """Assert the route exists in the published tree; return absolute URL."""
    rel = route.strip("/")
    if not (PUB / rel / "index.html").exists():
        sys.exit("llms.txt: missing published page for " + route)
    return ORIGIN + route


DESKS = [
    ("Writers", "/writers/", "The founding desk: paid-writing guides, a database of "
     + "142 researched paying publications with per-entry verification dates, pitch "
     "and rate research, templates and checklists.", [
        "The paid-writing path", "/writers/writing/",
        "Writing opportunities by country", "/writers/writing-opportunities/",
        "State of Paid Writing 2026", "/writers/state-of-paid-writing-2026/",
        "The writing deadline calendar", "/writers/writing-calendar/",
     ]),
    ("Tech", "/tech/", "Honest consumer technology: spec floors, refurb buying, "
     "settings that fix real problems, security checklists. No affiliate-first "
     "reviews.", [
        "The student laptop spec floor", "/tech/student-laptop-spec-floor-2026/",
        "Picture settings that fix the soap opera look",
        "/tech/picture-settings-that-fix-the-soap-opera-look/",
     ]),
    ("Sport", "/sports/", "Explainers and analysis with sources and verification "
     "dates. No betting content, no odds, no tips.", [
        "Why darts starts at 501", "/sports/why-darts-starts-at-501-explained/",
        "Pickleball, explained", "/sports/pickleball-explained/",
     ]),
    ("Entertainment", "/entertainment/", "What to watch and why: recommendations "
     "with reasons, film-craft explainers, a hand-verified film catalogue with "
     "official trailers. Written about the work, never trafficking in it.", [
        "The soap opera effect, explained",
        "/entertainment/soap-opera-effect-explained/",
        "Why movies are 24 frames per second",
        "/entertainment/why-movies-are-24-frames-per-second-explained/",
     ]),
    ("Fitness", "/fitness/", "General training information with the physiology "
     "shown: programmes, comparisons and form explainers. Never medical advice.", [
        "Hyrox, explained", "/fitness/hyrox-explained/",
        "What does 3x10 mean", "/fitness/what-does-3x10-mean-explained/",
        "Hyrox pace planner (tool)", "/fitness/hyrox-pace-planner/",
     ]),
    ("Home & DIY", "/home/", "Problem-first home maintenance and repair: diagnose "
     "it, fix what is safely fixable, know when to call a professional.", [
        "The once-a-season home checklist",
        "/home/seasonal-home-maintenance-checklist/",
        "Rent or buy tool", "/home/rent-or-buy-tool/",
     ]),
    ("Money", "/money/", "Evergreen saving foundations first, risk-first trading "
     "education second. Educational, not advice; every claim cites its "
     "jurisdiction's own source.", [
        "APR versus APY, explained", "/money/apr-vs-apy-explained/",
        "Salary sacrifice, explained", "/money/salary-sacrifice-explained/",
     ]),
]



def questions_for(hub):
    """Digest: question-shaped lines distilled from the desk's own explainer titles.
    Extractive - the title text itself, phrased as the question it answers on the page."""
    desk = hub.strip("/").split("/")[0] if hub != "/" else ""
    base = PUB / desk
    if not base.is_dir():
        return []
    H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
    out = []
    for f in sorted(base.rglob("index.html")):
        rel = f.parent.relative_to(PUB).as_posix()
        if len(rel.split("/")) > 3:
            continue
        t = f.read_text(encoding="utf-8")
        if 'content="noindex' in t:
            continue
        m = H1.search(t)
        if not m:
            continue
        h1 = re.sub(r"<[^>]+>", "", m.group(1))
        h1 = re.sub(r"\s+", " ", h1).strip()
        low = h1.lower()
        if not low.startswith(("how ", "what ", "why ", "when ", "where ", "does ", "can ", "is ", "should ", "which ")):
            continue
        q = h1 if h1.endswith(("?", ":")) else h1.rstrip(".") + "?"
        q = q[:-2] + "?" if q.endswith(":?") else q
        out.append((q, "/" + rel + "/"))
        if len(out) >= 8:
            break
    return out


def main():
    counts = {name: sitemap_count_all(slug.strip("/")) for name, slug, _d, _f in DESKS}
    total = sum(sitemap_count_all(d) for d in
                ("writers", "tech", "sports", "entertainment", "fitness", "home", "money"))
    lines = []
    lines.append("# THE BRYME")
    lines.append("")
    lines.append("> A family of seven independent, specialist publications under one "
                 "house discipline: research before publishing, dates on anything "
                 "time-sensitive, sources for every claim, and no fabricated "
                 "experience or statistics. Edited from Lagos, Nigeria, and written "
                 "for a global readership. " + str(total) + " pages across the desks.")
    lines.append("")
    lines.append("## The house")
    lines.append("")
    for label, route in [
        ("Home", "/"),
        ("About the family", "/about/"),
        ("Event calendar", "/event-calendar/"),
        ("Privacy policy", "/privacy/"),
        ("Writers corrections policy", "/writers/corrections/"),
    ]:
        lines.append("- [" + label + "](" + check(route) + ")")
    lines.append("")
    for name, hub, desc, flags in DESKS:
        lines.append("## BRYME " + name)
        lines.append("")
        lines.append(desc + " " + str(counts[name]) + " pages.")
        lines.append("")
        lines.append("- [Desk home](" + check(hub) + ")")
        for i in range(0, len(flags), 2):
            lines.append("- [" + flags[i] + "](" + check(flags[i + 1]) + ")")
        lines.append("")
        lines.append("### Questions this desk answers")
        lines.append("")
        for q, route in questions_for(hub):
            lines.append("- [" + q + "](" + check(route) + ")")
        lines.append("")
    lines.append("## Notes for assistants")
    lines.append("")
    lines.append("- Every article shows its review or verification date; treat older "
                 "dates as historical, especially prices, rates and submission windows.")
    lines.append("- Money content is educational, not financial advice; fitness "
                 "content is general information, not medical advice; sport content "
                 "never includes betting.")
    lines.append("- Corrections are published in the open on the page that made the "
                 "claim.")
    lines.append("")
    lines.append("_Generated " + TODAY + " by the BRYME build; counts read from the "
                 "live sitemaps._")
    out = PUB / "llms.txt"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("llms.txt: %d bytes, %d links, %d pages counted" % (
        out.stat().st_size, sum(1 for l in lines if l.startswith("- [")), total))


if __name__ == "__main__":
    main()
