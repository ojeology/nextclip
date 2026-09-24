#!/usr/bin/env python3
"""Rebuild only the Money publication from source on an already-routed tree.

A direct full ecosystem rebuild would regenerate other publications. The
standard npm build runs routing for Writers but does not rebuild Money's source
pages. This narrow generator creates Money in ecosystem/, routes it exactly as
build-routing does, stages public/, and synchronizes the routed allowlist and
sitemap index. It is safe to run twice and never uses deployment credentials.
"""
from __future__ import annotations

import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def load_script(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / name)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def sitemap_routes(file: Path, origin: str) -> set[str]:
    doc = ET.parse(file)
    locs = [e.text or "" for e in doc.getroot().iter() if e.tag.endswith("}loc")]
    if not locs or len(locs) != len(set(locs)):
        raise ValueError(f"{file}: empty or duplicate sitemap URLs")
    out = set()
    for loc in locs:
        parsed = urlsplit(loc)
        if f"{parsed.scheme}://{parsed.netloc}" != origin or not parsed.path.startswith("/money/") or not parsed.path.endswith("/"):
            raise ValueError(f"{file}: unexpected sitemap route: {loc}")
        out.add(parsed.path)
    return out


def main():
    eco = load_script("build-ecosystem.py")
    routing = load_script("build-routing.py")
    if eco.MODE != "path" or not (ROOT / "writers" / "learn").is_dir():
        raise SystemExit("Expected the committed path-routed tree; do not run full routing here")
    eco.write_service("money", eco.money_pages())
    source = ROOT / "ecosystem" / "money"
    root = ROOT / "money"
    published = ROOT / "public" / "money"
    if root.exists():
        shutil.rmtree(root)
    shutil.copytree(source, root)
    for file in root.rglob("*.html"):
        text, _ = routing.rewrite_prop_paths(file.read_text(encoding="utf-8"), "money")
        file.write_text(routing.strip_arrows(text), encoding="utf-8")
    if published.exists():
        shutil.rmtree(published)
    shutil.copytree(root, published)
    shutil.copy2(ROOT / "assets" / "money-position-size.js",
                 ROOT / "public" / "assets" / "money-position-size.js")

    routes = sitemap_routes(root / "sitemap.xml", eco.ORIGIN)
    for route in routes:
        path = root / route.removeprefix("/money/") / "index.html"
        if not path.is_file():
            raise ValueError(f"Money sitemap route without a built page: {route}")
    allow_file = ROOT / "content" / "index-allowlist.routed.json"
    allow = json.loads(allow_file.read_text(encoding="utf-8"))
    existing = set(allow["routes"])
    allow["routes"] = sorted({r for r in existing if not r.startswith("/money/")} | routes)
    allow_file.write_text(json.dumps(allow, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sitem = (root / "sitemap.xml").read_text(encoding="utf-8")
    dates = re.findall(r"<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>", sitem)
    if len(dates) != len(routes):
        raise ValueError("Money sitemap lastmod count must equal its URL count")
    index = ROOT / "sitemap.xml"
    original = index.read_text(encoding="utf-8")
    pattern = (r"(<sitemap><loc>" + re.escape(eco.ORIGIN)
               + r"/money/sitemap\.xml</loc><lastmod>)[^<]+(</lastmod></sitemap>)")
    updated, count = re.subn(pattern, lambda m: m.group(1) + max(dates) + m.group(2), original)
    if count != 1:
        raise ValueError("Root sitemap index must already contain Money exactly once")
    index.write_text(updated, encoding="utf-8")
    for name in ("sitemap.xml", "sitemap_index.xml"):
        (ROOT / "public" / name).write_text(updated, encoding="utf-8")
    print(f"money: {len(routes)} sitemap URLs; ecosystem/ + root + public/ synced; other properties untouched")


if __name__ == "__main__":
    main()
