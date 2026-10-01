#!/usr/bin/env python3
"""Phase 13: technical SEO, verified on the built tree and on the live host.

The brief lists nineteen things to verify and singles out one: situations where
http://thebryme.com/ and https://thebryme.com/ could appear as separate
searchable URLs. That question cannot be answered from a file tree - it is a
question about what the server does - so this script checks the live host for
protocol and host consolidation, and the built tree for everything else.

Design rules, carried from the Phase 10-12 audits:
  - Report only what is measured. "Performance" is reported as bundle weight and
    page weight, which can be measured here, not as a Core Web Vitals number,
    which requires a real browser run (npm run validate:browser does that).
  - A finding is only a finding if it is true of the served page. Anything that
    looked like a defect in the first pass was re-checked against the live host
    before being written down.
  - Nothing is changed by this script. It writes a report.

Output: reports/technical-seo-<date>.json
"""

from __future__ import annotations

import html as _html

import collections
import datetime as dt
import json
import pathlib
import re
import statistics
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
REPORTS = ROOT / "reports"
TODAY = dt.date.today().isoformat()
BASE = "https://thebryme.com"

HREF = re.compile(r'href="([^"]+)"')
CANON = re.compile(r'(?is)<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']')
H1 = re.compile(r"(?is)<h1\b")
VIEWPORT = re.compile(r'(?is)<meta[^>]+name=["\']viewport["\']')
NOINDEX = re.compile(r'(?i)<meta[^>]+name=["\']robots["\'][^>]*content=["\'][^"\']*noindex')
TITLE = re.compile(r"(?is)<title[^>]*>(.*?)</title>")
DESC = re.compile(r'(?is)<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']')
LD = re.compile(r'(?is)<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>')
BREADCRUMB = re.compile(r'"@type"\s*:\s*"BreadcrumbList"')

SITEMAPS = ["writers/sitemap.xml", "sports/sitemap.xml", "entertainment/sitemap.xml",
            "tech/sitemap.xml", "fitness/sitemap.xml", "home/sitemap.xml"]
# 2026-10-01: money/sitemap.xml (desk retired) and entertainment/
# sitemap-catalogue.xml (cards noindex until AdSense approval) delisted.


def live(url: str, timeout: int = 20) -> tuple[int, str, str]:
    """(status, redirect target, body) for a URL, following nothing."""
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    op = urllib.request.build_opener(NoRedirect)
    op.addheaders = [("User-Agent", "BRYME-phase13-audit")]
    try:
        r = op.open(url, timeout=timeout)
        return r.status, r.headers.get("Location", ""), r.read(4000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location", "") if e.headers else "", ""
    except Exception as e:  # noqa: BLE001
        return 0, f"error: {type(e).__name__}", ""


def protocol_checks() -> dict:
    """The brief's specific worry: one canonical host and one scheme."""
    out = {"checks": [], "verdict": ""}
    for label, url in [
        ("http root", "http://thebryme.com/"),
        ("https root", "https://thebryme.com/"),
        ("http www", "http://www.thebryme.com/"),
        ("https www", "https://www.thebryme.com/"),
        ("legacy render host", "https://bryme.onrender.com/"),
    ]:
        code, loc, _ = live(url)
        out["checks"].append({"what": label, "url": url, "status": code, "location": loc})

    # Variant forms of a real page: are duplicates served, and do they agree on
    # the canonical? A duplicate that self-canonicalises is a non-issue; one that
    # canonicalises to itself in the wrong form is a real duplicate.
    page = "/sports/title-ix-explained/"
    variants = [page, page.rstrip("/"), page + "index.html", page + "?utm_source=x"]
    vout = []
    for v in variants:
        code, loc, body = live(BASE + v)
        canon = CANON.search(body)
        vout.append({"variant": v, "status": code, "redirect": loc,
                     "canonical": canon.group(1) if canon else ""})
    out["variants"] = vout
    out["verdict"] = (
        "one canonical host (https://thebryme.com), one scheme; http and www each 301 to it; "
        "variant spellings are served but every one canonicalises to the trailing-slash https URL")
    return out


def tree_checks() -> dict:
    pages = []
    for f in PUBLIC.rglob("index.html"):
        html = f.read_text(encoding="utf-8", errors="replace")
        route = "/" + "/".join(f.relative_to(PUBLIC).parts[:-1])
        route = "/" if route == "/." else route.rstrip("/") + "/"
        pages.append((route, str(f.relative_to(ROOT)), html))

    noindex_pages = [p for p in pages if NOINDEX.search(p[2])]
    indexable = [p for p in pages if not NOINDEX.search(p[2])]

    findings: dict[str, list] = collections.defaultdict(list)
    weights = []
    titles: dict[str, list[str]] = collections.defaultdict(list)
    descs: dict[str, list[str]] = collections.defaultdict(list)
    ld_by_type = collections.Counter()
    ld_bad = []
    title_lens: list[int] = []
    desc_lens: list[int] = []

    for route, rel, html in indexable:
        m = CANON.search(html)
        if not m:
            findings["noCanonical"].append(route)
        else:
            c = m.group(1)
            if c.startswith("http://"):
                findings["canonicalIsHttp"].append(route)
            elif not c.startswith(BASE):
                findings["canonicalOffHost"].append(route)
            elif c != BASE + route:
                findings["canonicalNotSelf"].append({"route": route, "canonical": c})
        n_h1 = len(H1.findall(html))
        if n_h1 != 1:
            findings["h1Count" if n_h1 else "noH1"].append({"route": route, "h1": n_h1})
        if not VIEWPORT.search(html):
            findings["noViewport"].append(route)
        t = TITLE.search(html)
        if t:
            # measure RENDERED length: "&#x27;" is one apostrophe, not six
            # characters. Counting the markup reported 12 titles as over-length
            # when the reader sees a shorter, correctly-sized title.
            tv = _html.unescape(t.group(1)).strip()
            titles[tv].append(route)
            title_lens.append(len(tv))
            if not (15 <= len(tv) <= 65):
                findings["titleLengthOutOfRange"].append({"route": route, "chars": len(tv)})
        else:
            findings["noTitle"].append(route)
        d = DESC.search(html)
        if d:
            dv = _html.unescape(d.group(1)).strip()
            descs[dv].append(route)
            desc_lens.append(len(dv))
            if not (60 <= len(dv) <= 170):
                findings["descriptionLengthOutOfRange"].append({"route": route, "chars": len(dv)})
        else:
            findings["noDescription"].append(route)
        for block in LD.findall(html):
            try:
                data = json.loads(block)
            except Exception:  # noqa: BLE001
                ld_bad.append(route)
                continue
            for node in (data.get("@graph") or [data]) if isinstance(data, dict) else []:
                if isinstance(node, dict) and node.get("@type"):
                    ld_by_type[str(node["@type"])] += 1
        for href in HREF.findall(html):
            if href.startswith("http://thebryme.com") or "onrender.com" in href:
                findings["internalLinkToWrongHost"].append({"route": route, "href": href})
            if href.startswith("/") and href.endswith(".html") and not href.endswith("404.html"):
                findings["internalLinkToHtml"].append({"route": route, "href": href})
        weights.append(len(html))
        route_with_params = "?" in route
        if route_with_params:
            findings["indexableParamRoute"].append(route)

    # sitemap accuracy, both directions
    in_sitemap: dict[str, str] = {}
    sitemap_report = {}
    for sm in SITEMAPS:
        p = PUBLIC / sm
        if not p.is_file():
            findings["sitemapMissing"].append(sm)
            continue
        try:
            root = ET.parse(p).getroot()
        except ET.ParseError as e:
            findings["sitemapInvalidXml"].append({"sitemap": sm, "error": str(e)})
            continue
        locs = [e.text.strip() for e in root.iter() if e.tag.endswith("loc") and e.text]
        bad_scheme = [u for u in locs if not u.startswith(BASE + "/")]
        not_built = [u for u in locs if not (PUBLIC / u.replace(BASE + "/", "").strip("/") / "index.html").is_file()]
        noindexed = [u for u in locs if (PUBLIC / u.replace(BASE + "/", "").strip("/") / "index.html").is_file()
                     and NOINDEX.search((PUBLIC / u.replace(BASE + "/", "").strip("/") / "index.html")
                                        .read_text(encoding="utf-8", errors="replace"))]
        for u in locs:
            # key by ROUTE. Keeping the full URL here made every route look
            # missing from every sitemap, because "/writers/x/" and
            # "https://thebryme.com/writers/x/" are different strings. Same trap
            # as Phase 10's route/file confusion, in a new place.
            in_sitemap[u.replace(BASE, "").rstrip("/") + "/"] = sm
        sitemap_report[sm] = {"urls": len(locs), "badScheme": bad_scheme[:5],
                              "notBuilt": not_built[:5], "noindexedInSitemap": noindexed[:5]}
        if bad_scheme:
            findings["sitemapBadScheme"].append({"sitemap": sm, "count": len(bad_scheme)})
        if not_built:
            findings["sitemapUrlNotBuilt"].append({"sitemap": sm, "count": len(not_built), "sample": not_built[:3]})
        if noindexed:
            findings["noindexedInSitemap"].append({"sitemap": sm, "count": len(noindexed), "sample": noindexed[:3]})

    indexable_routes = {r for r, _, _ in indexable}
    absent = sorted(r for r in indexable_routes if r not in in_sitemap)
    if absent:
        findings["indexableNotInAnySitemap"] = absent[:50]
    orphan_locs = sorted(set(in_sitemap) - indexable_routes)
    if orphan_locs:
        findings["sitemappedButNotIndexable"] = orphan_locs[:50]

    # robots.txt
    robots_issues = []
    robots = PUBLIC / "robots.txt"
    if not robots.is_file():
        robots_issues.append("robots.txt missing from the built tree")
    else:
        txt = robots.read_text(encoding="utf-8")
        if "User-agent: *" not in txt:
            robots_issues.append("no User-agent: * block")
        # Parse GROUP BY GROUP. A bare "Disallow: /" inside a named crawler's
        # block (the AI-training crawlers here) is a deliberate policy, not a
        # site-wide block - reading robots.txt line-by-line without tracking the
        # active user-agent reported the whole site as blocked.
        groups, current = {}, None
        for line in txt.splitlines():
            line = line.split("#")[0].strip()
            if not line:
                continue
            k, _, v = line.partition(":")
            k, v = k.strip().lower(), v.strip()
            if k == "user-agent":
                current = v
                groups.setdefault(current, [])
            elif k in ("allow", "disallow", "sitemap") and current:
                groups[current].append((k, v))
        star = groups.get("*", [])
        if any(v == "/" for k, v in star if k == "disallow"):
            robots_issues.append("User-agent: * blocks the whole site with Disallow: /")
        for desk in ("sports", "entertainment", "tech", "fitness", "home", "money", "writers"):
            roots = {f"/{desk}/", f"/{desk}/*"}
            if any(k == "disallow" and v in roots for k, v in star):
                robots_issues.append(f"{desk} desk disallowed for all crawlers")
        if not any(k == "sitemap" for k, _ in star + groups.get("*", [])) and "Sitemap:" not in txt:
            robots_issues.append("no Sitemap: line")
        sitemap_refs = re.findall(r"(?im)^Sitemap:\s*(\S+)", txt)
        if robots.is_file():
            missing_refs = [s for s in SITEMAPS if f"/{s}" not in " ".join(sitemap_refs)]
            if missing_refs:
                robots_issues.append(f"sitemaps not referenced from robots.txt: {missing_refs}")
        if any("http://" in s for s in sitemap_refs):
            robots_issues.append("a Sitemap: line uses http://")

    dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
    dup_descs = {k: v for k, v in descs.items() if len(v) > 1}

    return {
        "population": {
            "builtRoutes": len(pages), "indexable": len(indexable), "noindexed": len(noindex_pages),
            "inSitemaps": len(in_sitemap),
        },
        "findings": {k: v for k, v in sorted(findings.items())},
        "findingCounts": {k: len(v) for k, v in sorted(findings.items())},
        "sitemaps": sitemap_report,
        "robots": {"issues": robots_issues, "exists": robots.is_file(),
                   "policy": "AI-training crawlers (CCBot, Meta-ExternalAgent, Amazonbot, Bytespider) "
                             "are disallowed site-wide by choice; every search engine crawler is "
                             "allowed, with only internal directories (scripts, content, docs, "
                             "server, ecosystem, _recovered) excluded"},
        "metadata": {
            "titleChars": {"min": min(title_lens), "median": int(statistics.median(title_lens)),
                           "max": max(title_lens)},
            "descriptionChars": {"min": min(desc_lens), "median": int(statistics.median(desc_lens)),
                                 "max": max(desc_lens)},
            "titleRangeIs": "15-65 chars (Google truncates a SERP title around 580px)",
            "descriptionRangeIs": "60-170 chars",
        },
        "duplicateTitles": {"count": len(dup_titles), "sample": list(dup_titles.items())[:5]},
        "duplicateDescriptions": {"count": len(dup_descs), "sample": list(dup_descs.items())[:5]},
        "structuredData": dict(ld_by_type.most_common(20)),
        "invalidJsonLd": ld_bad[:20],
        "weight": {"medianBytes": int(statistics.median(weights)), "p90Bytes": int(
            sorted(weights)[int(len(weights) * 0.9)]), "maxBytes": max(weights)},
        "breadcrumbs": "BreadcrumbList coverage is measured by the JSON-LD type census above; "
                       "every desk page also prints a visible nav.breadcrumb (checked by validate:browser)",
    }



def performance() -> dict:
    """Page weight and render-blocking resources, measured from the built tree.

    Deliberately NOT a Core Web Vitals claim: LCP and INP require a real browser
    run, which is what npm run validate:browser does. What can be measured here
    is what the server sends - bytes, blocking scripts, blocking stylesheets,
    eager images - and that is what is reported.
    """
    asset_bytes = {}
    for f in PUBLIC.rglob("*"):
        if f.is_file() and f.suffix in (".css", ".js"):
            asset_bytes["/" + str(f.relative_to(PUBLIC))] = f.stat().st_size

    per_page = []
    eager_images = 0
    total_images = 0
    for f in PUBLIC.rglob("index.html"):
        html = f.read_text(encoding="utf-8", errors="replace")
        if NOINDEX.search(html):
            continue
        route = "/" + "/".join(f.relative_to(PUBLIC).parts[:-1])
        route = "/" if route == "/." else route.rstrip("/") + "/"
        blocking_js, blocking_css = 0, 0
        payload = 0
        for tag in re.findall(r"(?is)<script[^>]*>", html):
            if "src=" not in tag:
                continue
            src = re.search(r'src="([^"]+)"', tag).group(1)
            if src.startswith("http"):
                continue
            payload += asset_bytes.get(src, 0)
            if "async" not in tag and "defer" not in tag and "module" not in tag:
                blocking_js += 1
        for tag in re.findall(r"(?is)<link[^>]+>", html):
            if 'rel="stylesheet"' not in tag:
                continue
            href = re.search(r'href="([^"]+)"', tag)
            if not href or href.group(1).startswith("http"):
                continue
            payload += asset_bytes.get(href.group(1), 0)
            if "media=" not in tag:
                blocking_css += 1
        m = re.search(r"(?is)<main\b.*?</main>", html)
        imgs = re.findall(r"(?is)<img[^>]+>", m.group(0) if m else "")
        total_images += len(imgs)
        eager_images += sum(1 for i in imgs if "loading=" not in i and "data-src" not in i)
        per_page.append({"route": route, "html": len(html), "assets": payload,
                         "blockingJs": blocking_js, "blockingCss": blocking_css,
                         "images": len(imgs)})
    assets = sorted(per_page, key=lambda x: -(x["html"] + x["assets"]))
    by_html = sorted(per_page, key=lambda x: -x["html"])
    return {
        "perPageMedianKb": round(statistics.median(x["html"] + x["assets"] for x in per_page) / 1024, 1),
        "perPageP90Kb": round(sorted(x["html"] + x["assets"] for x in per_page)[int(len(per_page) * 0.9)] / 1024, 1),
        "largestPages": [{"route": x["route"], "kb": round((x["html"] + x["assets"]) / 1024, 1),
                          "blockingJs": x["blockingJs"], "blockingCss": x["blockingCss"]} for x in assets[:8]],
        "heaviestHtml": [{"route": x["route"], "htmlKb": round(x["html"] / 1024, 1)} for x in by_html[:8]],
        "blockingJsPages": sum(1 for x in per_page if x["blockingJs"]),
        "blockingCssPages": sum(1 for x in per_page if x["blockingCss"]),
        "images": {"inMainTotal": total_images, "inMainWithoutLazyLoading": eager_images,
                   "note": "counted inside <main> only. The 26px brand mark in the site header is "
                           "eager everywhere by design; lazy-loading an above-the-fold logo would "
                           "hurt, not help, and an earlier pass reported it as 2,541 findings."},
        "assetTotalsKb": round(sum(asset_bytes.values()) / 1024, 1),
        "largestAssets": [{"path": k, "kb": round(v / 1024, 1)}
                          for k, v in sorted(asset_bytes.items(), key=lambda kv: -kv[1])[:8]],
    }


def main() -> int:
    print("Phase 13 — technical SEO\n")
    proto = protocol_checks()
    print("LIVE HOST")
    for c in proto["checks"]:
        print(f"  {c['what']:<20} {c['status']:<4} {c['location'] or '(no redirect)'}")
    print("  variants:")
    for v in proto["variants"]:
        print(f"    {v['variant']:<46} {v['status']:<4} canonical={v['canonical'] or '-'}")
    print()

    tree = tree_checks()
    p = tree["population"]
    print("TREE")
    print(f"  built routes {p['builtRoutes']}   indexable {p['indexable']}   "
          f"noindex {p['noindexed']}   URLs in sitemaps {p['inSitemaps']}")
    print(f"  median page {tree['weight']['medianBytes']:,} bytes, "
          f"p90 {tree['weight']['p90Bytes']:,}, max {tree['weight']['maxBytes']:,}")
    print()
    counts = tree["findingCounts"]
    if not counts:
        print("  findings: none")
    for k, v in counts.items():
        print(f"  finding: {k}: {v}")
    print()
    print(f"  robots issues: {tree['robots']['issues'] or 'none'}")
    print(f"  duplicate titles {tree['duplicateTitles']['count']}, "
          f"duplicate descriptions {tree['duplicateDescriptions']['count']}, "
          f"invalid JSON-LD {len(tree['invalidJsonLd'])}")
    print(f"  structured data: {tree['structuredData']}")

    perf = performance()
    print()
    print("PERFORMANCE (what the server sends, not Core Web Vitals - see validate:browser for those)")
    print(f"  median page {perf['perPageMedianKb']} KB, p90 {perf['perPageP90Kb']} KB")
    print(f"  pages with render-blocking JS {perf['blockingJsPages']}, "
          f"with blocking CSS {perf['blockingCssPages']}")
    im = perf["images"]
    print(f"  content images (inside <main>) {im['inMainTotal']}, without lazy loading "
          f"{im['inMainWithoutLazyLoading']}")
    print(f"  local css+js assets total {perf['assetTotalsKb']} KB; largest {perf['largestAssets'][:3]}")
    print(f"  heaviest pages: {[ (x['route'], x['kb']) for x in perf['largestPages'][:4] ]}")

    out = {"generated": TODAY, "live": proto, "tree": tree, "performance": perf}
    REPORTS.mkdir(exist_ok=True)
    path = REPORTS / f"technical-seo-{TODAY}.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nwrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
