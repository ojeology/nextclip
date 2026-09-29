#!/usr/bin/env python3
"""
AdSense catalogue triage (2026-09-29).

Holds the thin film/TV catalogue out of the index while it is upgraded, so a
reviewer sampling thebryme.com no longer lands on sub-500-word pages. This is
NOT a deletion: every page stays live and readable, keeps its inbound links,
and can be returned to the index individually or in bulk with --revert.

Why this is the right lever (audit 2026-09-29):
  - Entertainment = 902 indexable pages at avg 7.74 (site avg is 9.03).
  - 621 of the site's 623 sub-8.0 pages live in /entertainment/movie/.
  - Those pages carry a 380-word median, 99% shared section furniture.
  - Entertainment's 183 editorial guides average 9.71 and are untouched here.

Enforces the same invariants as scripts/validate-site-quality.js, atomically:
  L64  allowlisted route            => robots must be index,follow
  L65  non-allowlisted, not verified => robots must be noindex
  L102 indexable count              == allowlist size
  L134 every sitemap route is allowlisted

Writes a manifest (content/catalogue-triage-manifest.json) listing exactly which
routes were held back, so --revert is exact. Idempotent; deterministic.

Usage:
  python3 scripts/catalogue-triage.py --apply              # hold back <600w
  python3 scripts/catalogue-triage.py --apply --max-words 400
  python3 scripts/catalogue-triage.py --report             # dry run, no writes
  python3 scripts/catalogue-triage.py --revert
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "content" / "catalogue-triage-manifest.json"

# Same tiers the other house injectors keep byte-identical.
# "" = the repo root, where build-routing.py stages the routed tree and where
# scripts/validate-site-quality.js reads from (ROOT + route, no extra prefix).
TIERS = ("ecosystem", "", "public")
CATALOGUE_REL = Path("entertainment") / "movie"
SITEMAP_REL = Path("entertainment") / "sitemap-catalogue.xml"
ALLOWLISTS = ("content/index-allowlist.routed.json", "content/index-allowlist.json")
ORIGIN = "https://thebryme.com"

ROBOTS_RE = re.compile(r'(<meta\s+name="robots"\s+content=")([^"]*)(")', re.I)
STRIP_RE = re.compile(r"<(script|style|noscript|svg|template)\b[^>]*>.*?</\1>", re.S | re.I)
MAIN_RE = re.compile(r"<(main|article)\b[^>]*>(.*?)</\1>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
ENT_RE = re.compile(r"&[a-z#0-9]{2,8};")
WS_RE = re.compile(r"\s+")


def word_count(html: str) -> int:
    m = MAIN_RE.search(html)
    h = m.group(2) if m else html
    h = STRIP_RE.sub(" ", h)
    h = TAG_RE.sub(" ", h)
    h = ENT_RE.sub(" ", h)
    return len(WS_RE.sub(" ", h).strip().split())


def route_of(index_html: Path) -> str:
    """Repo-absolute route, e.g. /entertainment/movie/1917/ (tier prefix stripped)."""
    parts = index_html.parent.relative_to(ROOT).as_posix().split("/")
    return "/" + "/".join(parts[1:]) + "/"


def tier_file(tier: str, route: str) -> Path:
    """Resolve a route inside a publish tier. "" is the repo root itself."""
    sub = (Path(tier) / route.strip("/")) if tier else Path(route.strip("/"))
    return ROOT / sub / "index.html"


def set_robots(text: str, value: str) -> tuple[str, bool]:
    """Return (text, changed). Only touches the <head> robots meta."""
    def _sub(m: re.Match[str]) -> str:
        if m.group(2).lower() == value:
            return m.group(0)
        return f"{m.group(1)}{value}{m.group(3)}"
    new, n = ROBOTS_RE.subn(_sub, text, count=1)
    return new, (n > 0 and new != text)


def scan(source_tier: str, max_words: int) -> dict[str, dict]:
    """route -> {words, cur_robots} for catalogue pages below the threshold."""
    base = ROOT / source_tier / CATALOGUE_REL
    if not base.is_dir():
        raise SystemExit(f"catalogue-triage: missing {base.relative_to(ROOT)}")
    out: dict[str, dict] = {}
    for f in sorted(base.rglob("index.html")):
        html = f.read_text(encoding="utf-8")
        w = word_count(html)
        if w >= max_words:
            continue
        m = ROBOTS_RE.search(html)
        out[route_of(f)] = {"words": w, "robots": (m.group(2) if m else "")}
    return out


def in_allowlist() -> set[str]:
    for rel in ALLOWLISTS:
        p = ROOT / rel
        if p.is_file():
            return set(json.loads(p.read_text(encoding="utf-8"))["routes"])
    raise SystemExit("catalogue-triage: no allowlist found")


def write_allowlists(remove: set[str], add: set[str]) -> tuple[int, int]:
    """Apply to both allowlist files. Returns (before, after) for the routed one."""
    before = after = 0
    for rel in ALLOWLISTS:
        p = ROOT / rel
        if not p.is_file():
            continue
        doc = json.loads(p.read_text(encoding="utf-8"))
        routes = doc["routes"]
        if rel.endswith("routed.json"):
            before = len(routes)
        keep = [r for r in routes if r not in remove]
        for r in sorted(add):
            if r not in keep:
                keep.append(r)
        keep = sorted(set(keep))
        doc["routes"] = keep
        if rel.endswith("routed.json"):
            after = len(keep)
        p.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return before, after


def write_sitemaps(remove: set[str]) -> int:
    """Drop held-back URLs from the catalogue sitemap in every tier."""
    total_removed = 0
    for tier in TIERS:
        p = ROOT / tier / SITEMAP_REL
        if not p.is_file():
            continue
        txt = p.read_text(encoding="utf-8")
        blocks = re.findall(r"<url>.*?</url>", txt, re.S)
        def _is_held(block: str) -> bool:
            for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", block):
                path = re.sub(r"^[a-z]+://[^/]+", "", loc).rstrip("/") + "/"
                if path in remove:
                    return True
            return False
        kept = [b for b in blocks if not _is_held(b)]
        if len(kept) != len(blocks):
            total_removed = len(blocks) - len(kept)
            head = txt[:txt.find("<url>")] if "<url>" in txt else txt
            tail = "</urlset>"
            p.write_text(head + "\n".join(kept) + "\n" + tail + "\n", encoding="utf-8")
    return total_removed


SITEMAP_DECLS = {
    "public": ("public/sitemap.xml", "public/robots.txt"),
    "": ("sitemap.xml", "robots.txt"),
    "ecosystem": ("ecosystem/hub/sitemap.xml", None),
}


def deregister_empty_sitemap() -> int:
    """Never submit a sitemap with zero URLs: it is a negative signal, and
    Search Console reports it as an error. If the catalogue sitemap has emptied
    out, drop its <sitemap> entry from the index and its Sitemap: line from
    robots.txt in every tier. Called after ensure-sitemap-index so nothing
    re-adds it."""
    dropped = 0
    for tier, (index_rel, robots_rel) in SITEMAP_DECLS.items():
        idx = ROOT / index_rel
        cat = ((ROOT / tier / SITEMAP_REL) if tier else (ROOT / SITEMAP_REL))
        if not idx.is_file() or not cat.is_file():
            continue
        if re.search(r"<loc>", cat.read_text(encoding="utf-8")):
            continue  # still has URLs, leave the declaration alone
        text = idx.read_text(encoding="utf-8")
        new = re.sub(r"<sitemap>\s*<loc>[^<]*sitemap-catalogue\.xml</loc>.*?</sitemap>", "", text)
        if new != text:
            idx.write_text(new, encoding="utf-8")
            dropped += 1
        if robots_rel:
            rob = ROOT / robots_rel
            if rob.is_file():
                rtext = rob.read_text(encoding="utf-8")
                rnew = re.sub(r"^Sitemap: \S*sitemap-catalogue\.xml\s*\n?", "", rtext, flags=re.M)
                if rnew != rtext:
                    rob.write_text(rnew, encoding="utf-8")
                    dropped += 1
    return dropped


def reregister_sitemap() -> None:
    """Undo deregister_empty_sitemap: put the catalogue back in the index and
    robots.txt for any tier that has it again."""
    entry = (f"<sitemap><loc>{ORIGIN}/entertainment/sitemap-catalogue.xml</loc>"
             f"<lastmod>2026-09-27</lastmod></sitemap>")
    for tier, (index_rel, robots_rel) in SITEMAP_DECLS.items():
        idx = ROOT / index_rel
        if idx.is_file():
            text = idx.read_text(encoding="utf-8")
            if "sitemap-catalogue.xml" not in text and "</sitemapindex>" in text:
                idx.write_text(text.replace("</sitemapindex>", entry + "</sitemapindex>"),
                               encoding="utf-8")
        if robots_rel:
            rob = ROOT / robots_rel
            if rob.is_file():
                rtext = rob.read_text(encoding="utf-8")
                line = f"Sitemap: {ORIGIN}/entertainment/sitemap-catalogue.xml\n"
                if "sitemap-catalogue.xml" not in rtext:
                    rob.write_text(rtext.rstrip("\n") + "\n" + line, encoding="utf-8")


def sync_tiers(routes: set[str], value: str) -> int:
    changed = 0
    for tier in TIERS:
        for r in routes:
            f = tier_file(tier, r)
            if not f.is_file():
                continue
            txt = f.read_text(encoding="utf-8")
            new, ch = set_robots(txt, value)
            if ch:
                f.write_text(new, encoding="utf-8")
                changed += 1
    return changed


def apply(max_words: int) -> None:
    targets = scan("ecosystem", max_words)
    allow = in_allowlist()
    hold = {r for r in targets if r in allow}
    print(f"catalogue-triage: {len(targets)} pages under {max_words} words")
    print(f"catalogue-triage: {len(hold)} of them currently indexable -> holding back")

    changed = sync_tiers({r for r in targets if r in allow or True}, "noindex,follow")
    removed_sm = write_sitemaps(hold)
    before, after = write_allowlists(hold, set())

    MANIFEST.write_text(json.dumps({
        "applied": "2026-09-29",
        "maxWords": max_words,
        "heldBack": sorted(hold),
        "previousRobots": {r: targets[r]["robots"] for r in hold},
    }, indent=2) + "\n", encoding="utf-8")

    print(f"catalogue-triage: robots updated on {changed} files across {len(TIERS)} tiers")
    print(f"catalogue-triage: {removed_sm} URLs removed from catalogue sitemap")
    dropped = deregister_empty_sitemap()
    if dropped:
        print(f"catalogue-triage: catalogue sitemap emptied -> de-registered ({dropped} files)")
    print(f"catalogue-triage: allowlist {before} -> {after}")
    print(f"catalogue-triage: manifest -> {MANIFEST.relative_to(ROOT)}")
    print("\nNow run the repo's own gates to confirm the invariants hold:")
    print("  node scripts/validate-site-quality.js --quick")


def revert() -> None:
    if not MANIFEST.is_file():
        raise SystemExit("catalogue-triage: no manifest - nothing to revert")
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    routes = set(m["heldBack"])
    prev = m.get("previousRobots", {})

    # restore robots per-page to whatever it was before
    by_value: dict[str, set[str]] = {}
    for r in routes:
        by_value.setdefault(prev.get(r, "index,follow"), set()).add(r)
    changed = 0
    for value, rs in by_value.items():
        changed += sync_tiers(rs, value)

    write_allowlists(set(), routes)
    # restore sitemap entries
    for tier in TIERS:
        p = ROOT / tier / SITEMAP_REL
        if not p.is_file():
            continue
        txt = p.read_text(encoding="utf-8")
        have = set(re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", txt))
        add = "".join(
            f"<url><loc>{ORIGIN}{r}</loc><changefreq>monthly</changefreq>"
            f"<priority>0.5</priority></url>\n"
            for r in sorted(routes) if (ORIGIN + r) not in have)
        if add:
            p.write_text(txt.replace("</urlset>", add + "</urlset>"), encoding="utf-8")

    reregister_sitemap()
    MANIFEST.unlink()
    print(f"catalogue-triage: reverted {len(routes)} routes ({changed} robots writes)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--apply", action="store_true")
    g.add_argument("--revert", action="store_true")
    g.add_argument("--report", action="store_true")
    ap.add_argument("--max-words", type=int, default=600,
                    help="hold back catalogue pages below this word count (default 600)")
    a = ap.parse_args()

    if a.revert:
        revert(); return
    if a.report:
        t = scan("ecosystem", a.max_words)
        allow = in_allowlist()
        hold = sorted(r for r in t if r in allow)
        print(f"DRY RUN - no files written")
        print(f"  under {a.max_words} words : {len(t)}")
        print(f"  indexable now   : {len(hold)}")
        print(f"  indexable after : {len(allow) - len(hold)}")
        for r in hold[:10]:
            print(f"    {r}  ({t[r]['words']} words)")
        if len(hold) > 10:
            print(f"    ... +{len(hold)-10} more")
        return

    apply(a.max_words)


if __name__ == "__main__":
    main()
