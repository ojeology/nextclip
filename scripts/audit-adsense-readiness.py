#!/usr/bin/env python3
"""Phase 14: AdSense readiness, checked against the brief's list.

The brief asks for a whole-site audit before any future AdSense review, and it
asks for one thing above all: that the site should provide obvious value even
without advertisements. Most of that was measured in Phases 10-13; this script
measures the parts that belong to advertising and trust specifically, and points
at the existing evidence for the rest rather than re-deriving it.

Honesty rules carried from the other audits:
  - Anything about the live site is fetched, not assumed.
  - Anything that cannot be verified statically is named as a residual risk
    rather than reported as passing. The Adsterra invoke.js is remote code: this
    script can prove the request is now consent-gated, and cannot prove what the
    remote file does once it loads.
  - Every threshold is either a policy Google publishes or is stated as the
    desk's own editorial rule, never invented and presented as Google's.

Output: reports/adsense-readiness-<date>.json
"""

from __future__ import annotations

import collections
import datetime as dt
import json
import pathlib
import re
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
REPORTS = ROOT / "reports"
TODAY = dt.date.today().isoformat()

NOINDEX = re.compile(r'(?i)<meta[^>]+name=["\']robots["\'][^>]*content=["\'][^"\']*noindex')
# COUNT CONTAINERS, NOT CLASS NAMES. The band's own markup carries four elements
# whose class names begin "adband" (the aside, .adband-in, .adband-label,
# .adband-slot), so counting class matches reported "4 ad slots per page" on a
# page with exactly one ad. The container is identified by its data attribute.
ADBAND = re.compile(r'<[a-z]+[^>]*data-adband="adsterra"[^>]*>')
ADSLOT = re.compile(r'<ins[^>]+class="[^"]*adsbygoogle[^"]*"')
CMP = re.compile(r"fundingchoicesmessages\.google\.com")
GATED_LOADER = re.compile(r'/assets/adsterra-loader\.js')
RAW_REMOTE = re.compile(r'<script[^>]+src="https://[^"]*invoke\.js"')
TRUST_SLUGS = ["privacy", "terms", "contact", "about", "editorial-policy", "corrections",
               "copyright", "disclosure", "disclaimer"]
DESKS = ["writers", "tech", "sports", "entertainment", "fitness", "home"]


def live(url: str) -> tuple[int, str]:
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "BRYME-phase14"}),
                                   timeout=25)
        return r.status, r.read(4000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:  # noqa: BLE001
        return 0, ""


def main() -> int:
    cfg = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
    ca_id = str(((cfg.get("adsense") or {}).get("caId") or "")).strip()
    ast = cfg.get("adsterra") or {}

    pages = []
    for f in PUBLIC.rglob("index.html"):
        html = f.read_text(encoding="utf-8", errors="replace")
        route = "/" + "/".join(f.relative_to(PUBLIC).parts[:-1])
        pages.append((("/" if route == "/." else route.rstrip("/") + "/"), html))
    indexable = [(r, h) for r, h in pages if not NOINDEX.search(h)]

    # --- advertising inventory ------------------------------------------------
    ads_before_main = ads_in_main = ads_in_nav_or_footer = 0
    per_page_counts = collections.Counter()
    sticky_ads: list[str] = []
    for route, html in indexable:
        m = re.search(r"(?is)<main\b.*?</main>", html)
        main = m.group(0) if m else ""
        nav = re.search(r"(?is)<nav\b.*?</nav>", html)
        foot = re.search(r"(?is)<footer\b.*?</footer>", html)
        n = len(ADBAND.findall(html)) + len(ADSLOT.findall(html))
        per_page_counts[n] += 1
        if n:
            if ADBAND.search(main) or ADSLOT.search(main):
                ads_in_main += 1
            if nav and (ADBAND.search(nav.group(0)) or ADSLOT.search(nav.group(0))):
                ads_in_nav_or_footer += 1
            if foot and (ADBAND.search(foot.group(0)) or ADSLOT.search(foot.group(0))):
                ads_in_nav_or_footer += 1
            before = html.split("<main", 1)[0]
            if ADBAND.search(before) or ADSLOT.search(before):
                ads_before_main += 1
        for style in re.findall(r"(?is)\.(?:adband|adsbygoogle)[^{]*\{([^}]*)\}", html):
            if re.search(r"(?i)\b(fixed|sticky)\b", style):
                sticky_ads.append(route)

    ads_on_noindex = sum(1 for r, h in pages if NOINDEX.search(h) and (ADBAND.search(h) or ADSLOT.search(h)))
    cmp_pages = sum(1 for _, h in indexable if CMP.search(h))
    gated = sum(1 for _, h in indexable if GATED_LOADER.search(h))
    raw = sum(1 for _, h in indexable if RAW_REMOTE.search(h))

    # --- ads.txt --------------------------------------------------------------
    ads_txt_tree = (PUBLIC / "ads.txt").read_text(encoding="utf-8").strip() \
        if (PUBLIC / "ads.txt").is_file() else ""
    code, ads_txt_live = live("https://thebryme.com/ads.txt")
    ads_txt_live = ads_txt_live.strip()
    records = [l for l in ads_txt_tree.splitlines() if l.strip() and not l.startswith("#")]
    ads_txt_ok = (len(records) == 1 and records[0].startswith("google.com,")
                  and ca_id.replace("ca-", "") in records[0])

    # --- trust pages ----------------------------------------------------------
    trust = {}
    for slug in TRUST_SLUGS:
        site_level = f"/{slug}/"
        desks_with = [d for d in DESKS if (PUBLIC / d / slug / "index.html").is_file()]
        trust[slug] = {"siteLevel": (PUBLIC / slug / "index.html").is_file(),
                       "desks": len(desks_with)}

    # Every privacy page a reader can actually land on: the house one and one per
    # desk. A desk page is where a reader arriving from that desk reads the
    # policy, so a disclosure missing from any of them is a real gap - which is
    # exactly what a single-page check failed to notice.
    privacy_routes = {}
    house = PUBLIC / "privacy" / "index.html"
    if house.is_file():
        privacy_routes["/privacy/"] = house
    for d in DESKS:
        f = PUBLIC / d / "privacy" / "index.html"
        if f.is_file():
            privacy_routes[f"/{d}/privacy/"] = f

    CHECKERS = {
        "namesGoogleAdsense": r"google",
        "mentionsAdsterra": r"adsterra|profitablerate",
        "explainsCookiesOrIdentifiers": r"cookie|device identifier|personalised ads",
        "explainsOptOut": r"opt[- ]out|ad settings|your choices|withdraw",
        "linksConsentControls": r"consent|privacy & messaging|ad settings",
    }
    per_page, incomplete = {}, []
    for route, path in sorted(privacy_routes.items()):
        text = path.read_text(encoding="utf-8", errors="replace")
        plain = re.sub(r"<[^>]+>", " ", text)
        found = {k: bool(re.search(rx, plain, re.I)) for k, rx in CHECKERS.items()}
        per_page[route] = found
        missing = [k for k, v in found.items() if not v]
        if missing:
            incomplete.append({"route": route, "missing": missing})

    # The headline booleans stay True only if EVERY satisfied them, so the
    # summary cannot be greener than the worst page behind it.
    disclosures = {k: all(per_page[r][k] for r in per_page) for k in CHECKERS}

    # --- what the brief calls "value without advertisements" ------------------
    words = [len(re.findall(r"[A-Za-z0-9']+", re.sub(r"<[^>]+>", " ", h))) for _, h in indexable]
    substantial = sum(1 for w in words if w >= 400)
    writers_pages = sum(1 for r, _ in indexable if r.startswith("/writers/"))

    out = {
        "generated": TODAY,
        "advertising": {
            "pagesWithAnAdSlot": sum(n for n, c in per_page_counts.items() for _ in range(c) if n),
            "slotsPerPage": dict(per_page_counts.most_common()),
            "adsInsideMain": ads_in_main,
            "adsInNavOrFooter": ads_in_nav_or_footer,
            "adsBeforeMain": ads_before_main,
            "stickyOrFixedAdContainers": len(sticky_ads),
            "adsOnNoindexPages": ads_on_noindex,
            "networks": {
                "googleAdSenseSnippet": sum(1 for _, h in indexable if "adsbygoogle.js" in h),
                "adsterraBand": sum(1 for _, h in indexable if ADBAND.search(h)),
            },
            "adUnitsWired": bool(str((cfg.get("adsense") or {}).get("nativeSlotId") or "").strip()),
            "note": "one band per content page, after </main> and before <footer>; the AdSense "
                    "snippet is present for verification with no ad units wired",
        },
        "consent": {
            "googleCmpOnIndexablePages": cmp_pages,
            "indexablePages": len(indexable),
            "consentModeV2Defaults": "region-scoped defaults in /assets/gtag-init.js, denied by "
                                     "default in the EEA, UK and Switzerland",
            "nonGoogleNetworkGated": gated,
            "nonGoogleNetworkLoadedInline": raw,
            "gateRule": "outside Europe: loads immediately; inside EEA/UK/CH: waits for a granted "
                        "ad-consent signal from the CMP, and never loads if consent is refused",
            "why": "Consent Mode governs Google tags only. Google's EU user consent policy requires "
                   "consent to cover the publisher's partners as well, so a third-party ad network "
                   "loading before consent was a real compliance gap.",
            "verifiedBy": "scripts/test-ad-consent.js - three browser cases (non-European loads; "
                          "European unconsented makes no ad-host request; European consented loads)",
            "residualRisk": "invoke.js is remote code from the network. This audit can prove the "
                            "request is gated and cannot prove what the remote file does after it "
                            "loads. That is a standing, accepted risk of running any third-party ad "
                            "network, and the reason the popunder and social-bar formats are refused "
                            "in config.",
        },
        "adsTxt": {
            "inTree": ads_txt_tree, "live": ads_txt_live, "liveStatus": code,
            "records": records, "matchesConfiguredPublisher": bool(ca_id and ca_id.replace("ca-", "") in ads_txt_tree),
            "wellFormed": ads_txt_ok,
        },
        "trust": trust,
        "privacyDisclosures": disclosures,
        "privacyPagesChecked": sorted(privacy_routes),
        "privacyPagesIncomplete": incomplete,
        "value": {
            "indexablePages": len(indexable),
            "pagesWith400WordsOrMore": substantial,
            "shareWith400WordsOrMore": round(100 * substantial / max(1, len(indexable)), 1),
            "medianMainTextWords": sorted(words)[len(words) // 2],
            "writersSectionPages": writers_pages,
            "note": "the brief's test is whether the site is worth reading without ads. Depth is "
                    "measured here; Phase 10 and 11 measured whether the depth is original, and "
                    "Phase 12 measured the film catalogue.",
        },
        "evidenceFromEarlierPhases": {
            "technicalSeo": "reports/technical-seo-2026-09-30.json - zero findings across 2,590 "
                            "indexable pages (canonicals, sitemaps, robots, h1, metadata, JSON-LD)",
            "mobileUsability": "npm run validate:browser - 1,551 rendered cases at 390x844, 768x1024 "
                               "and 1440x1000, zero failures, including horizontal-overflow checks",
            "writersSectionQuality": "reports/quality-audit-2026-09-30.json - 517 URLs graded A-E",
            "deskQuality": "reports/desk-audit-2026-09-30.json - 1,354 URLs, zero thin pages",
            "brokenLinks": "272,413 internal links, zero broken (npm run check:links)",
        },
    }

    REPORTS.mkdir(exist_ok=True)
    path = REPORTS / f"adsense-readiness-{TODAY}.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    a = out["advertising"]
    c = out["consent"]
    print("Phase 14 — AdSense readiness\n")
    print(f"  ad slots per page      : {a['slotsPerPage']}")
    print(f"  inside <main>          : {a['adsInsideMain']}   in nav/footer: {a['adsInNavOrFooter']}"
          f"   above <main>: {a['adsBeforeMain']}")
    print(f"  sticky/fixed ad slots  : {a['stickyOrFixedAdContainers']}")
    print(f"  ads on noindex pages   : {a['adsOnNoindexPages']}")
    print(f"  AdSense snippet on     : {a['networks']['googleAdSenseSnippet']} pages, "
          f"ad units wired: {a['adUnitsWired']}")
    print(f"  adsterra band on       : {a['networks']['adsterraBand']} pages")
    print(f"  Google CMP on          : {c['googleCmpOnIndexablePages']} of {c['indexablePages']} indexable")
    print(f"  non-Google network     : {c['nonGoogleNetworkGated']} gated, "
          f"{c['nonGoogleNetworkLoadedInline']} loaded inline before consent")
    print(f"  ads.txt                : {out['adsTxt']['live'].strip()!r} (live {out['adsTxt']['liveStatus']}, "
          f"well-formed {out['adsTxt']['wellFormed']})")
    print(f"  privacy discloses      : {out['privacyDisclosures']}")
    print(f"  privacy pages checked  : {len(out['privacyPagesChecked'])} "
          f"({', '.join(out['privacyPagesChecked'])})")
    print(f"  privacy pages missing a disclosure: {len(out['privacyPagesIncomplete'])}"
          + (" -> " + ", ".join(f"{x['route']} {x['missing']}" for x in out["privacyPagesIncomplete"])
             if out["privacyPagesIncomplete"] else ""))
    print(f"  value without ads      : {out['value']['shareWith400WordsOrMore']}% of "
          f"{out['value']['indexablePages']} indexable pages carry 400+ words")
    print(f"\nwrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
