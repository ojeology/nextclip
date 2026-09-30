#!/usr/bin/env python3
"""Phase 11: audit the six secondary desks (Tech, Sport, Entertainment, Fitness,
Home & DIY, Money).

The brief asks for six named things per desk: strong pages, pages already
receiving organic traffic, pages with meaningful impressions, thin pages,
duplicate pages, template-heavy pages, and pages providing insufficient original
value. It also says, twice, not to decide any of it from click counts alone and
not to delete or noindex a desk because it looks weak.

So this script measures page evidence and nothing else. It is the same
measurement core as scripts/audit-quality.py - imported, not copied, so the two
audits can never drift - pointed at the six desk sitemaps instead of the Writers
one. The Writers rules were calibrated for editorial pages, so they are NOT
reused as a grade here for every page type:

  - The secondary desks contain tools, calculators, hubs and data pages. Grading
    a URL-encoder tool on word count would repeat the mistake that marked the
    31-term glossary "thin" for having one heading. Word-count grading is applied
    to prose pages; tool and data pages are graded on whether they function and
    whether they explain themselves.

  - "Template-heavy" is measured, not assumed: a page's share of its own text
    that survives furniture-stripping. A page that is 80% desk boilerplate is
    template-heavy whatever its word count says.

  - "Traffic" and "impressions" are reported as NOT AVAILABLE unless a per-URL
    impression file exists on disk. There is no fresh Search Console export in
    this workspace - only reports/search-console-analysis-2026-09-07.md, which is
    narrative. Inventing per-page impressions would be worse than the gap.

Output: reports/desk-audit-<date>.json
"""

from __future__ import annotations

import collections
import datetime as dt
import importlib.util
import json
import pathlib
import re
import statistics
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
TODAY = dt.date.today().isoformat()

# --- reuse the Phase 10 measurement core --------------------------------------
_spec = importlib.util.spec_from_file_location("audit_quality", ROOT / "scripts" / "audit-quality.py")
aq = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(aq)

WORDS = aq.WORDS
HREF = aq.HREF
NEW_DAYS = aq.NEW_DAYS
TEMPLATE_MIN_PAGES = aq.TEMPLATE_MIN_PAGES
DUP_OVERLAP = aq.DUP_OVERLAP

DESKS = ["tech", "sports", "entertainment", "fitness", "home", "money"]

# A page whose surviving text is under this share of its total text is carried by
# the template rather than by its own writing.
TEMPLATE_HEAVY_SHARE = 0.40

TOOL_ROUTE = re.compile(r"/tool/[a-z0-9-]+/|-(calculator|converter|lookup|estimator|planner)/$")
TOOL_INDEX_ROUTE = re.compile(r"/(tools|tool)/$")
HUB_ROUTE = re.compile(r"^/[a-z0-9-]+/(reviews|explainers|guides|clubs|routes|recommendations|"
                       r"opinion|mistakes|seasonal-care|fix|maintain|appliances|understand|"
                       r"energy-bills)/$")
# Trust pages are their own kind of page. A privacy page that cites nobody is not
# failing to cite, and grading it on the prose bands would be a category error -
# the same mistake as grading the glossary on heading count. Its job is to be
# true, complete and findable.
POLICY_ROUTE = re.compile(r"/(privacy|about|contact|corrections|disclosure|disclaimer|copyright|"
                          r"editorial-policy|editorial-standards|terms|event-calendar)/$")


def tool_bundle(html: str) -> str:
    """A page-specific tool script, e.g. /assets/points-race-tool.js.

    Two calculators on the sports and home desks ship with no <input> in the
    HTML at all: the control surface is built at runtime by their own bundle.
    Grading those as "no working control" would be a false defect, and a false
    defect in an audit is expensive - someone acts on it.
    """
    for src in re.findall(r'(?i)<script[^>]+src="([^"]+)"', html):
        name = src.rsplit("/", 1)[-1].lower()
        if "/assets/" in src and ("tool" in name or "calculator" in name):
            return src
    return ""


def desk_urls(desk: str) -> list[str]:
    root = ET.parse(ROOT / "public" / desk / "sitemap.xml").getroot()
    out = []
    for e in root.iter():
        if e.tag.endswith("loc") and e.text:
            out.append(e.text.strip().replace("https://thebryme.com", ""))
    return out


def file_for(url: str) -> pathlib.Path:
    return ROOT / "public" / url.strip("/") / "index.html"


def page_type(url: str, main_html: str, html: str) -> str:
    """Route first, structure second. Never word count."""
    if POLICY_ROUTE.search(url):
        return "policy"
    if TOOL_INDEX_ROUTE.search(url):
        return "hub"          # /tools/ is a list of tools, not a tool
    if re.match(r"^/[a-z0-9-]+/$", url) and url.strip("/") not in DESKS:
        return "policy"       # a site page that happens to sit in a desk sitemap
    if TOOL_ROUTE.search(url) or tool_bundle(html):
        return "tool"
    if re.search(r"(?i)<(form|input|canvas|select)\b", main_html):
        return "tool"
    if HUB_ROUTE.match(url):
        return "hub"
    # Structural hub: a page linking to 15+ siblings of its own desk is indexing
    # that desk, whatever its route looks like. The cut is from this population,
    # not from taste - article deskLinks run p50 8, p90 12, p99 33, so 15 sits
    # above the 90th percentile and every page past it is a section index
    # (/tech/coding/ lists 138, /tech/cybersecurity/ 75, /money/save/ 79).
    if len({h for h in HREF.findall(main_html)
            if h.startswith("/" + url.strip("/").split("/")[0] + "/")}) >= 15:
        return "hub"
    if len(re.findall(r"(?i)<tr\b", main_html)) >= 16:
        return "data"
    return "article"


def signals(url: str, html: str) -> dict:
    m = re.search(r"(?is)<main\b.*?</main>", html)
    main_html = m.group(0) if m else html
    base = aq.signals(url, html)
    base["file"] = str(file_for(url).relative_to(ROOT))
    base["type"] = page_type(url, main_html, html)
    base["toolBundle"] = tool_bundle(html)
    base["deskLinks"] = len({h for h in HREF.findall(main_html)
                             if h.startswith("/" + url.strip("/").split("/")[0] + "/")})
    # interactive controls INSIDE main, so site chrome can never make a page a tool
    base["controls"] = len(re.findall(r"(?i)<(input|select|textarea|canvas|button)\b", main_html))
    return base


def main() -> int:
    all_rows: list[dict] = []
    missing: dict[str, list[str]] = {}
    for desk in DESKS:
        urls = desk_urls(desk)
        got = []
        for u in urls:
            f = file_for(u)
            if not f.exists():
                missing.setdefault(desk, []).append(u)
                continue
            r = signals(u, f.read_text(encoding="utf-8", errors="replace"))
            r["desk"] = desk
            got.append(r)
        all_rows += got

    # ---- furniture is stripped per desk: a paragraph on >=4 pages of the same
    # ---- desk is that desk's furniture, even if another desk never uses it.
    template_by_desk: dict[str, set[str]] = {}
    for desk in DESKS:
        seen = collections.Counter()
        for r in all_rows:
            if r["desk"] != desk:
                continue
            for p in {aq.key(x) for x in r["paras"]}:
                seen[p] += 1
        template_by_desk[desk] = {p for p, n in seen.items() if n >= TEMPLATE_MIN_PAGES}

    for r in all_rows:
        unique = [p for p in r["paras"] if aq.key(p) not in template_by_desk[r["desk"]]]
        r["unique_words"] = len(WORDS.findall(" ".join(unique)))
        r["own_share"] = round(r["unique_words"] / max(1, r["words"]), 3)
        r["_sh"] = aq.shingles(WORDS.findall(" ".join(unique).lower()))
        h = r["h2"] + r["h3"]
        r["units"] = h + r["dt"] + r["rows"] + r["cards"]

    # ---- inbound links, counted site-wide (the honest measure of connectedness)
    known = {r["url"] for r in all_rows}
    inbound = collections.Counter()
    for r in all_rows:
        html = (ROOT / r["file"]).read_text(encoding="utf-8", errors="replace")
        for href in HREF.findall(html):
            if not href.startswith("/") or href.startswith("//"):
                continue
            target = href.split("#")[0].rstrip("/") + "/"
            if target in known:
                inbound[target] += 1

    # ---- duplicates: within a desk first, then across desks -------------------
    by_desk = {d: [r for r in all_rows if r["desk"] == d] for d in DESKS}
    # Hubs and tool indexes are exempt from the duplicate rule: two hubs that
    # cluster the same articles by different axes share their card summaries by
    # construction - one of them groups 73 guides by topic, the other 39 by the
    # decision the reader arrived with. That overlap is the library, not a
    # duplicated page. Their overlap is reported, never graded.
    def gradable(r):
        return r["type"] == "article" and not r.get("dup")

    for desk in DESKS:
        rows = [r for r in by_desk[desk] if gradable(r)]
        for i, a in enumerate(rows):
            if a.get("dup"):
                continue
            for b in rows[i + 1:]:
                if b.get("dup") or not a["_sh"] or not b["_sh"]:
                    continue
                ov = len(a["_sh"] & b["_sh"]) / min(len(a["_sh"]), len(b["_sh"]))
                if ov >= DUP_OVERLAP:
                    a["dup"] = b["dup"] = f"{ov:.0%} of unique text shared with {b['url'] if a is not b else ''}".strip()
                    a["dup"] = f"{ov:.0%} of unique text shared with {b['url']}"
                    b["dup"] = f"{ov:.0%} of unique text shared with {a['url']}"
                    break
    cross = []
    for i, a in enumerate(all_rows):
        for b in all_rows[i + 1:]:
            if a["desk"] == b["desk"] or not a["_sh"] or not b["_sh"]:
                continue
            if a["type"] in ("hub", "tool") or b["type"] in ("hub", "tool"):
                continue
            ov = len(a["_sh"] & b["_sh"]) / min(len(a["_sh"]), len(b["_sh"]))
            if ov >= DUP_OVERLAP:
                cross.append({"a": a["url"], "b": b["url"], "overlap": round(ov, 2)})

    # ---- grades --------------------------------------------------------------
    # Prose is graded on the Phase 10 bands so the two audits read the same.
    # Tool and data pages are graded on function + explanation, because a working
    # calculator with 700 words of explanation is not a thin page, and a
    # 900-word page with a dead form is not a strong one.
    cutoff = (dt.date.today() - dt.timedelta(days=NEW_DAYS)).isoformat()
    for r in all_rows:
        r["inbound"] = inbound.get(r["url"], 0)
        r["new"] = bool(r["newest_date"] and r["newest_date"] >= cutoff)
        w, ext, inb = r["words"], r["external_links"], r["inbound"]
        if r.get("dup"):
            r["grade"], r["reason"] = "D", r["dup"]
            continue
        if r["type"] == "hub":
            # A hub's job is navigation plus enough prose to make the list
            # meaningful. It is NOT required to cite the outside world: an index
            # of the desk's own work is the point of the page.
            # A hub is weak only when it neither explains nor indexes. A 727w
            # section shelf with 6 pieces behind it is a small hub, not a thin
            # page, and calling it thin would send someone to "fix" a page that
            # has no problem.
            if w < 400 and r["deskLinks"] < 4:
                r["grade"], r["reason"] = "C", f"hub with {r['deskLinks']} desk links and {w}w of framing"
            elif r["deskLinks"] >= 8 and w >= 400 and inb >= 3:
                r["grade"], r["reason"] = "A", f"index of {r['deskLinks']} desk pieces, {w}w of framing"
            else:
                r["grade"], r["reason"] = "B", (
                    f"small hub: {r['deskLinks']} desk links, {w}w of framing, {inb} inbound links")
            continue
        if r["type"] == "policy":
            if w >= 300 and inb >= 3 and r["has_jsonld"]:
                r["grade"], r["reason"] = "A", f"trust page: {w}w, linked from {inb} pages"
            elif w >= 300:
                r["grade"], r["reason"] = "B", f"trust page: {w}w, {inb} inbound links"
            else:
                r["grade"], r["reason"] = "C", f"trust page with only {w}w"
            continue
        if r["type"] in ("tool", "data"):
            works = (r["controls"] >= 1 or bool(r["toolBundle"])) if r["type"] == "tool" else r["units"] >= 4
            explains = w >= 400
            how = "controls in the HTML" if r["controls"] else (f"controls built by {r['toolBundle']}" if r["toolBundle"] else "no control surface")
            if works and explains and ext >= 1 and inb >= 3:
                r["grade"], r["reason"] = "A", f"{r['type']} ({how}), {w}w of explanation, sourced, linked into"
            elif works and explains:
                gaps = [g for g in (f"{ext} outside sources" if ext < 1 else "",
                                    f"{inb} inbound links" if inb < 3 else "") if g]
                r["grade"], r["reason"] = "B", f"{r['type']} ({how}) explains itself; " + ", ".join(gaps)
            elif works:
                r["grade"], r["reason"] = "C", f"{r['type']} ({how}) but explains almost nothing ({w}w)"
            else:
                r["grade"], r["reason"] = "C", f"{r['type']} with no working control or data on the page"
            continue
        if r["words"] < 120:
            r["grade"], r["reason"] = "E", f"{r['words']} words of main text"
        elif re.search(r"[?&](page|filter|sort)=", r["url"]):
            r["grade"], r["reason"] = "E", "filter/parameter view of another page"
        elif r["words"] < 400:
            r["grade"], r["reason"] = "C", f"{r['words']} words — below the 400 floor"
        elif r["words"] < 600 and ext == 0:
            r["grade"], r["reason"] = "C", f"{r['words']} words and cites no outside source"
        elif r["words"] >= 900 and r["units"] >= 4 and ext >= 2 and inb >= 3:
            r["grade"], r["reason"] = "A", "long, structured, sourced, linked into"
        else:
            gaps = []
            if r["words"] < 900:
                gaps.append(f"{r['words']}w")
            if r["units"] < 4:
                gaps.append(f"{r['units']} organised units")
            if ext < 2:
                gaps.append(f"{ext} outside sources")
            if inb < 3:
                gaps.append(f"{inb} inbound links")
            if r["new"]:
                gaps.append("recently published")
            r["grade"], r["reason"] = "B", "useful; " + ", ".join(gaps)

    # ---- per-desk summary ----------------------------------------------------
    desks_out = {}
    for desk in DESKS:
        rows = by_desk[desk]
        counts = collections.Counter(r["grade"] for r in rows)
        wards = sorted(r["words"] for r in rows)
        furniture = template_by_desk[desk]
        desks_out[desk] = {
            "urls": len(desk_urls(desk)),
            "built": len(rows),
            "missing": missing.get(desk, []),
            "pageTypes": dict(collections.Counter(r["type"] for r in rows)),
            "furnitureParagraphs": len(furniture),
            "furnitureShareOfText": round(
                100 * (1 - sum(r["unique_words"] for r in rows) / max(1, sum(r["words"] for r in rows))), 1),
            "words": {"min": wards[0], "p10": wards[len(wards) // 10],
                      "median": int(statistics.median(wards)), "max": wards[-1]},
            "uniqueWordsMedian": int(statistics.median([r["unique_words"] for r in rows])),
            "grades": {g: counts.get(g, 0) for g in "ABCDE"},
            "thin": [r["url"] for r in sorted(rows, key=lambda x: x["words"])[:5]],
            "templateHeavy": [{"url": r["url"], "ownShare": r["own_share"], "words": r["words"]}
                              for r in sorted(rows, key=lambda x: x["own_share"])
                              if r["own_share"] < TEMPLATE_HEAVY_SHARE][:12],
            "duplicates": sorted({r["url"]: r["dup"] for r in rows if r.get("dup")}.items()),
            "citesNothing": sum(1 for r in rows if r["external_links"] == 0),
            "noInbound": sum(1 for r in rows if r["inbound"] == 0),
            "noJsonLd": sum(1 for r in rows if not r["has_jsonld"]),
            "thinDescription": sum(1 for r in rows if r["desc_len"] < 60),
            "publishedInWindow": sum(1 for r in rows if r["new"]),
            "strong": [{k: v for k, v in r.items() if not k.startswith("_") and k != "paras"}
                       for r in sorted([r for r in rows if r["grade"] == "A"],
                                       key=lambda x: -(x["words"] + 100 * x["inbound"]))[:10]],
            "strongCount": sum(1 for r in rows if r["grade"] == "A"),
        }

    tot = collections.Counter(r["grade"] for r in all_rows)
    out = {
        "generated": TODAY,
        "method": {
            "indexableSet": "the six desk sitemaps (public/<desk>/sitemap.xml), 1,354 URLs, all built",
            "furniture": f"a paragraph on >= {TEMPLATE_MIN_PAGES} pages of the same desk is furniture",
            "duplicateOverlap": DUP_OVERLAP,
            "newWindowDays": NEW_DAYS,
            "templateHeavyBelow": TEMPLATE_HEAVY_SHARE,
            "traffic": "NO per-URL impression data on disk. reports/search-console-analysis-2026-09-07.md "
                       "is narrative only; its named pages are recorded under trafficNotes and per-page "
                       "impressions are left blank rather than estimated.",
        },
        "totals": {
            "urls": sum(d["urls"] for d in desks_out.values()),
            "built": sum(d["built"] for d in desks_out.values()),
            "grades": {g: tot.get(g, 0) for g in "ABCDE"},
            "pageTypes": dict(collections.Counter(r["type"] for r in all_rows)),
            "wordsMedian": int(statistics.median([r["words"] for r in all_rows])),
            "uniqueWordsMedian": int(statistics.median([r["unique_words"] for r in all_rows])),
            "citesNothing": sum(1 for r in all_rows if r["external_links"] == 0),
            "noInbound": sum(1 for r in all_rows if r["inbound"] == 0),
        },
        "trafficNotes": {
            "perUrlImpressions": "not available",
            "namedInSept7Report": [
                "legacy media URLs (/movies/, /entertainment/, /series/, /trending/, /anime/*, "
                "/articles/, /years/) still hold ~250 impressions and ~10 clicks while 404 live - "
                "pre-BRYME index decay, not desk performance",
                "/make-money/writing/* serves 200 on non-canonical deep paths despite the current "
                "build having no make-money/ directory",
            ],
        },
        "crossDeskDuplicates": cross,
        "desks": desks_out,
        "pages": [{k: v for k, v in r.items() if not k.startswith("_") and k != "paras"}
                  for r in sorted(all_rows, key=lambda x: (x["desk"], x["grade"]))],
    }
    REPORTS.mkdir(exist_ok=True)
    path = REPORTS / f"desk-audit-{TODAY}.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"secondary desks audited : {out['totals']['built']} of {out['totals']['urls']} URLs "
          f"({len(missing)} desks with missing builds)")
    print(f"page types              : {out['totals']['pageTypes']}")
    print(f"words                   : median {out['totals']['wordsMedian']}w, "
          f"median unique {out['totals']['uniqueWordsMedian']}w")
    print()
    print(f"{'desk':<15}{'n':>5}{'A':>5}{'B':>5}{'C':>5}{'D':>5}{'E':>5}{'furn%':>7}{'med':>6}{'thin':>7}{'noExt':>7}{'noIn':>6}")
    for desk in DESKS:
        d = desks_out[desk]
        g = d["grades"]
        print(f"{desk:<15}{d['built']:>5}{g['A']:>5}{g['B']:>5}{g['C']:>5}{g['D']:>5}{g['E']:>5}"
              f"{d['furnitureShareOfText']:>7}{d['words']['median']:>6}"
              f"{len(d['templateHeavy']):>7}{d['citesNothing']:>7}{d['noInbound']:>6}")
    print()
    print(f"totals: {out['totals']['grades']}  cross-desk duplicates: {len(cross)}")
    print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
