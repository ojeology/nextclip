#!/usr/bin/env python3
"""Inject BreadcrumbList JSON-LD into every indexable page of the built site.

Phase 0 (AdSense readiness, 2026-09-27, gap G8): the site had visible
breadcrumb trail lines on many templates but zero BreadcrumbList structured
data anywhere. This step runs AFTER the publish tree is assembled (post
build-public-dir / purge-stale-publish / inject-analytics) and adds one
JSON-LD node per page, built only from ancestors that actually exist as
published, indexable pages. Nothing is invented:

  - name of each crumb = the ancestor page's own <title> (first segment)
  - a crumb only appears if its index.html exists and is indexable
  - pages that already declare BreadcrumbList are left untouched
  - noindex pages (redirect stubs, 404, foundation placeholders) are skipped
  - the homepage itself gets no breadcrumb (nothing to trail from)

Like inject-analytics.py, this walks every publish tier (ecosystem/ as source
of truth, the root desk staging trees, and public/ which Render publishes) and
writes the byte-identical script to each tier, so the strict
"public mirror == routed page" release gates stay true.

Deterministic: sorted walk, cached names, no timestamps. Idempotent: safe to
run repeatedly; a second run changes nothing.
"""
from __future__ import annotations
import html as _html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "public"
# Same tiers inject-analytics.py keeps in sync (see that file for the rationale).
PUBLISH_TIERS = ("ecosystem", "public", "entertainment", "writers", "tech",
                 "home", "sports", "fitness", "about", "money")
CFG = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
ORIGIN = (CFG.get("siteUrl") or "").rstrip("/")
if not ORIGIN:
    print("inject-breadcrumbs: no siteUrl in site.config.json - skipping", flush=True)
    sys.exit(0)

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
ROBOTS_RE = re.compile(r'<meta\s+name="robots"\s+content="([^"]*)"', re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
LD_BC_RE = re.compile(
    r'<script type="application/ld\+json">\{"@context":"https://schema\.org",'
    r'"@type":"BreadcrumbList".*?</script>', re.S)

_name_cache: dict[str, str] = {}


def _visible_title(raw: str) -> str:
    return _html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()


def page_name(rel: str, doc: str) -> str:
    """Name for a crumb: h1 if present, else first title segment."""
    if rel in _name_cache:
        return _name_cache[rel]
    m = H1_RE.search(doc)
    name = _visible_title(m.group(1)) if m else ""
    if not name:
        t = TITLE_RE.search(doc)
        name = _visible_title(t.group(1)).split(" | ")[0].strip() if t else rel
    _name_cache[rel] = " ".join(name.split())[:110]
    return _name_cache[rel]


def is_indexable(doc: str) -> bool:
    r = ROBOTS_RE.search(doc)
    return not (r and "noindex" in r.group(1).lower())


def script_for(route: str, doc: str) -> str | None:
    """Build the BreadcrumbList JSON-LD script for one page, or None."""
    if route == "/" or "BreadcrumbList" in doc or not is_indexable(doc):
        return None
    segs = [s for s in route.split("/") if s]
    items = [{"name": "Home", "item": ORIGIN + "/"}]
    for i in range(1, len(segs)):
        anc = "/" + "/".join(segs[:i]) + "/"
        f = PUB / anc.lstrip("/") / "index.html"
        if not f.exists():
            continue
        try:
            adoc = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if not is_indexable(adoc):
            continue
        items.append({"name": page_name(anc, adoc), "item": ORIGIN + anc})
    items.append({"name": page_name(route, doc), "item": ORIGIN + route})
    if len(items) < 2:
        return None
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList",
          "itemListElement": [{"@type": "ListItem", "position": i + 1,
                               "name": it["name"], "item": it["item"]}
                              for i, it in enumerate(items)]}
    return ('<script type="application/ld+json">'
            + json.dumps(ld, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def insert(doc: str, script: str) -> str | None:
    cut = doc.rfind("</head>")
    if cut == -1:
        return None
    return doc[:cut] + script + doc[cut:]


def main() -> None:
    if not PUB.exists():
        print("inject-breadcrumbs: no public/ tree - skipping", flush=True)
        sys.exit(0)
    # Pass 1 - public/ is authoritative: compute the script per route.
    scripts: dict[str, str] = {}
    skipped_ld = skipped_noindex = 0
    for f in sorted(PUB.rglob("index.html")):
        _rel = f.parent.relative_to(PUB).as_posix()
        route = "/" if _rel == "." else "/" + _rel.strip("/") + "/"
        try:
            doc = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if "BreadcrumbList" in doc:
            skipped_ld += 1
            # Already injected in an earlier run - reuse the exact script so
            # the other tiers still reach byte parity with public/.
            m = LD_BC_RE.search(doc)
            if m:
                scripts[route] = m.group(0)
            continue
        s = script_for(route, doc)
        if s is None:
            if not is_indexable(doc):
                skipped_noindex += 1
            continue
        scripts[route] = s
        new = insert(doc, s)
        if new is not None:
            f.write_text(new, encoding="utf-8")
    # Pass 2 - replicate byte-identically to the other publish tiers so the
    # strict mirror-equality release gates hold.
    tiers_done: dict[str, int] = {}
    for tier in PUBLISH_TIERS:
        base = ROOT / tier
        if not base.is_dir() or tier == "public":
            continue
        n = 0
        for route, s in scripts.items():
            if not route.endswith("/"):
                continue
            if tier == "ecosystem":
                # full tree: routes map 1:1 under ecosystem/
                f = base / route.lstrip("/")
            else:
                # desk staging tree: only its own desk's routes, prefix stripped
                prefix = "/" + tier + "/"
                if not route.startswith(prefix):
                    continue
                f = base / route[len(prefix):]
            f = f / "index.html"
            if not f.is_file():
                continue
            try:
                doc = f.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if "BreadcrumbList" in doc or not is_indexable(doc):
                continue
            new = insert(doc, s)
            if new is not None:
                f.write_text(new, encoding="utf-8")
                n += 1
        if n:
            tiers_done[tier] = n
    print(f"inject-breadcrumbs: injected {len(scripts)} routes into public/"
          f" (already had LD: {skipped_ld}, noindex skipped: {skipped_noindex})"
          + ("; tiers: " + ", ".join(f"{k} {v}" for k, v in tiers_done.items())
             if tiers_done else ""), flush=True)


if __name__ == "__main__":
    main()
