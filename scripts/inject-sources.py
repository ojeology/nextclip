#!/usr/bin/env python3
"""Inject a "Referenced in this piece" sources section into pages that name
recognised institutions/outlets but carry no outbound source links.

Phase 3 (AdSense readiness, 2026-09-27, gap G6 - first tranche). Honest by
construction: the section only names entities the page's own text already
mentions, and links them to their official ROOT sites - never deep links,
never invented citations. Pages that already carry an outbound link in their
main content are left untouched (they have their own sourcing).

Rules:
  - indexable pages only (noindex stubs skipped, like inject-breadcrumbs)
  - entities matched in the page's visible main-content text, first mention
  - at most 6 entity links per page (first-seen order)
  - section carries an h2 (structure) + a desk byline (attribution) and is
    appended before </main>
  - idempotent: a page that already contains the section is skipped
  - mirrored byte-identically across the publish tiers so the strict
    "public mirror == routed page" gates hold (same design as the analytics
    and breadcrumb injectors)

Deterministic, no timestamps, no network.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "public"
PUBLISH_TIERS = ("ecosystem", "public", "entertainment", "writers", "tech",
                 "home", "sports", "fitness", "about", "money")

# (display name, URL, case-sensitive pattern or None for distinctive names)
ENTITIES = [
    ("NHS", "https://www.nhs.uk/", "NHS"),
    ("gov.uk", "https://www.gov.uk/", r"gov\.uk"),
    ("Ofgem", "https://www.ofgem.org.uk/", None),
    ("Ofcom", "https://www.ofcom.org.uk/", None),
    ("HMRC", "https://www.gov.uk/government/organisations/hm-revenue-customs", "HMRC"),
    ("Citizens Advice", "https://www.citizensadvice.org.uk/", None),
    ("StepChange", "https://www.stepchange.org/", None),
    ("MoneyHelper", "https://www.moneyhelper.org.uk/", None),
    ("IRS", "https://www.irs.gov/", "IRS"),
    ("CFPB", "https://www.consumerfinance.gov/", "CFPB"),
    ("FCA", "https://www.fca.org.uk/", "FCA"),
    ("SEC", "https://www.sec.gov/", "SEC"),
    ("FINRA", "https://www.finra.org/", "FINRA"),
    ("ASIC", "https://asic.gov.au/", "ASIC"),
    ("Medicare", "https://www.medicare.gov/", None),
    ("FDA", "https://www.fda.gov/", "FDA"),
    ("USDA", "https://www.usda.gov/", "USDA"),
    ("EPA", "https://www.epa.gov/", "EPA"),
    ("CPSC", "https://www.cpsc.gov/", "CPSC"),
    ("CDC", "https://www.cdc.gov/", "CDC"),
    ("NIH", "https://www.nih.gov/", "NIH"),
    ("WHO", "https://www.who.int/", "WHO"),
    ("Mayo Clinic", "https://www.mayoclinic.org/", None),
    ("IEEE", "https://www.ieee.org/", "IEEE"),
    ("W3C", "https://www.w3.org/", "W3C"),
    ("MDN", "https://developer.mozilla.org/", "MDN"),
    ("IMDb", "https://www.imdb.com/", None),
    ("Rotten Tomatoes", "https://www.rottentomatoes.com/", None),
    ("Box Office Mojo", "https://www.boxofficemojo.com/", None),
    ("BBC", "https://www.bbc.com/", "BBC"),
    ("Reuters", "https://www.reuters.com/", None),
    ("ESPN", "https://www.espn.com/", "ESPN"),
    ("Premier League", "https://www.premierleague.com/", None),
    ("UEFA", "https://www.uefa.com/", "UEFA"),
    ("FIFA", "https://www.fifa.com/", "FIFA"),
    ("Transfermarkt", "https://www.transfermarkt.com/", None),
]
_COMPILED = [(name, url, re.compile(pat if pat else re.escape(name),
                                    0 if pat else re.IGNORECASE))
             for name, url, pat in ENTITIES]

ROBOTS_RE = re.compile(r'<meta\s+name="robots"\s+content="([^"]*)"', re.I)
MAIN_RE = re.compile(r"<main[^>]*>(.*)</main>", re.S | re.I)


def is_indexable(doc: str) -> bool:
    r = ROBOTS_RE.search(doc)
    return not (r and "noindex" in r.group(1).lower())


def desk_byline(route: str) -> str:
    seg = route.strip("/").split("/")[0] if route.strip("/") else ""
    name = {"writers": "BRYME Writers desk", "tech": "BRYME Tech desk",
            "sports": "BRYME Sport desk", "entertainment": "BRYME Entertainment desk",
            "fitness": "BRYME Fitness desk", "home": "BRYME Home & DIY desk",
            "money": "BRYME Money desk"}.get(seg, "the BRYME editorial desk")
    return f"Maintained by {name}."


def section_for(doc: str) -> str | None:
    m = MAIN_RE.search(doc)
    if not m:
        return None
    main = m.group(1)
    if "Referenced in this piece" in main:
        return None
    # strip scripts/styles from the text scan, keep tags out of matches
    vis = re.sub(r"<[^>]+>", " ", re.sub(
        r"<(script|style)[^>]*>.*?</\1>", " ", main, flags=re.S | re.I))
    if re.search(r'href="https?://', main):
        return None  # page already carries outbound source links
    hits: list[tuple[str, str]] = []
    seen_spans: list[tuple[int, int]] = []
    for name, url, rx in _COMPILED:
        for mm in rx.finditer(vis):
            a, b = mm.span()
            if any(not (b <= s or a >= e) for s, e in seen_spans):
                continue
            seen_spans.append((a, b))
            hits.append((name, url))
            break  # first mention per entity
        if len(hits) >= 6:
            break
    if not hits:
        return None
    links = " &middot; ".join(
        f'<a href="{u}" rel="noopener" target="_blank">{n}</a>' for n, u in hits)
    route_guess = ""  # byline derived at call site
    return ('<section class="section"><div class="prose">'
            "<h2>Referenced in this piece</h2>"
            "<p>Named in this piece, with their official sites: " + links + ".</p>"
            "<p>Official pages change; the date printed on this page is the "
            "desk's last check. Errors are fixed in the open &mdash; see the "
            "corrections page.</p>"
            "</div></section>")


def main() -> None:
    if not PUB.exists():
        print("inject-sources: no public/ tree - skipping", flush=True)
        sys.exit(0)
    files = sorted(PUB.rglob("index.html"))
    injected = skipped_sourced = skipped_noindex = 0
    for f in files:
        rel = f.parent.relative_to(PUB).as_posix()
        route = "/" if rel == "." else "/" + rel + "/"
        try:
            doc = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if not is_indexable(doc):
            skipped_noindex += 1
            continue
        sec = section_for(doc)
        if sec is None:
            # count pages that already have outbound links as "sourced"
            m = MAIN_RE.search(doc)
            if m and re.search(r'href="https?://', m.group(1)):
                skipped_sourced += 1
            continue
        by = desk_byline(route)
        sec = sec.replace("</div></section>",
                          f'<p class="byline">{by}</p></div></section>', 1)
        cut = doc.rfind("</main>")
        if cut == -1:
            continue
        f.write_text(doc[:cut] + sec + doc[cut:], encoding="utf-8")
        injected += 1
    # mirror byte-identically to tiers (same design as inject-breadcrumbs)
    tiers_done: dict[str, int] = {}
    for tier in PUBLISH_TIERS:
        base = ROOT / tier
        if not base.is_dir() or tier == "public":
            continue
        n = 0
        for f in sorted(base.rglob("index.html")):
            try:
                doc = f.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if "Referenced in this piece" in doc or not is_indexable(doc):
                continue
            sec = section_for(doc)
            if sec is None:
                continue
            rel = f.parent.relative_to(base).as_posix()
            route = "/" + ("" if rel == "." else rel + "/")
            by = desk_byline(route)
            sec = sec.replace("</div></section>",
                              f'<p class="byline">{by}</p></div></section>', 1)
            cut = doc.rfind("</main>")
            if cut == -1:
                continue
            f.write_text(doc[:cut] + sec + doc[cut:], encoding="utf-8")
            n += 1
        if n:
            tiers_done[tier] = n
    print(f"inject-sources: sections added on {injected} public pages "
          f"(already sourced: {skipped_sourced}, noindex skipped: {skipped_noindex})"
          + ("; tiers: " + ", ".join(f"{k} {v}" for k, v in tiers_done.items())
             if tiers_done else ""), flush=True)


if __name__ == "__main__":
    main()
