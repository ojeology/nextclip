#!/usr/bin/env python3
"""Inject the bottom-of-page ad band — but ONLY once a real ad slot exists.

Deliberately inert by default. The band is built, styled, CSP-correct and wired
into `npm run build`; it renders nothing until `adsense.nativeSlotId` is set in
site.config.json. That is the switch: one value, one deploy, no code change.

Why gated rather than live (2026-09-29):
  AdSense does not serve to a site that has not passed review. With the site
  currently refused on content grounds, a wired unit would render an empty box
  at the foot of every page and still earn nothing. Empty ad space on a site
  already refused for thin content is a negative signal at re-review, and the
  downside is asymmetric: a refusal is recoverable, a served-ads-on-thin-content
  policy violation is not.

Two defects in the original helper this replaces (build-ecosystem.py _ads_slot):
  1. no data-ad-slot attribute, so there was no unit to request
  2. an inline push script, which the site CSP (script-src 'self' https:, no
     'unsafe-inline') blocks — it could never have executed even if wired

Placement: after </main>, before <footer>, so it never interrupts the article.
Reserved height prevents layout shift when the ad fills. A visible
"Advertisement" label keeps it distinguishable from content, which matters
because site.config.json forbids anything that resembles a job card or CTA.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASES = (ROOT, ROOT / "public")

# Tiers that also carry published copies of the shell pages.
EXTRA_TIERS = ("ecosystem", "writers", "tech", "sports", "entertainment",
               "fitness", "home", "money")

MARK = 'data-adband="bottom"'

LABEL = "Advertisement"

BAND = (
    '<aside class="adband" ' + MARK + ' aria-label="' + LABEL + '">'
    '<style>'
    '.adband{margin:0;padding:24px 0 0}'
    '.adband-in{max-width:1100px;margin:0 auto;padding:0 20px}'
    '.adband-label{display:block;font:500 10px/1 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'
    'letter-spacing:.14em;text-transform:uppercase;color:#8a8578;margin:0 0 10px}'
    '.adband .adsbygoogle{display:block;min-height:280px}'
    '.adband::before{content:"";display:block;max-width:1100px;margin:0 auto 24px;'
    'padding:0 20px;border-top:1px solid rgba(0,0,0,.08)}'
    '</style>'
    '<div class="adband-in">'
    '<span class="adband-label">' + LABEL + '</span>'
    '<ins class="adsbygoogle" style="display:block" '
    'data-ad-client="{client}" data-ad-slot="{slot}" '
    'data-ad-format="{fmt}" data-full-width-responsive="true"></ins>'
    '</div>'
    '</aside>'
    '<script src="/assets/ads-init.js" defer></script>'
)


def config() -> tuple[str, str, str]:
    """(client, slot, format) — slot empty means the band stays off."""
    try:
        cfg = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
    except Exception as exc:                                    # pragma: no cover
        print(f"ads: could not read site.config.json ({exc}) - skipping")
        return "", "", ""
    ads = cfg.get("adsense") or {}
    client = str(ads.get("caId") or "").strip()
    slot = str(ads.get("nativeSlotId") or "").strip()
    fmt = str(ads.get("nativeFormat") or "auto").strip() or "auto"
    if not ads.get("enabled", True):
        return "", "", ""
    return client, slot, fmt


def targets() -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for base in BASES:
        if base.is_dir():
            for root, dirs, files in os.walk(base):
                dirs[:] = [d for d in dirs
                           if d not in ("node_modules", "_recovered", ".git")]
                if "index.html" in files:
                    seen.add(Path(root) / "index.html")
    for tier in EXTRA_TIERS:
        base = ROOT / tier
        if not base.is_dir():
            continue
        for root, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs
                       if d not in ("node_modules", "_recovered", ".git")]
            if "index.html" in files:
                seen.add(Path(root) / "index.html")
    for f in sorted(seen):
        out.append(f)
    return out


def revert() -> int:
    """Remove every injected band. Used for the activation test and as an undo."""
    import re as _re
    pat = _re.compile(r'<aside class="adband" data-adband="bottom".*?</aside>'
                      r'\s*<script src="/assets/ads-init.js" defer></script>\n?', _re.S)
    n = 0
    for f in targets():
        t = f.read_text(encoding="utf-8", errors="replace")
        if MARK not in t:
            continue
        f.write_text(pat.sub("", t), encoding="utf-8")
        n += 1
    print(f"ads: reverted {n} file(s)")
    return 0


def main() -> int:
    if "--revert" in sys.argv:
        return revert()
    client, slot, fmt = config()
    if not slot:
        print("ads: nativeSlotId not set in site.config.json -> band stays off (0 pages touched)")
        print("ads: to activate, set adsense.nativeSlotId to the unit ID from your AdSense dashboard")
        return 0
    if not client:
        print("ads: adsense.caId missing in site.config.json -> band stays off")
        return 0

    # plain substitution, not str.format: the inline CSS is full of braces.
    block = (BAND.replace("{client}", client)
                 .replace("{slot}", slot)
                 .replace("{fmt}", fmt))
    applied = skipped = problems = 0

    for f in targets():
        try:
            t = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if MARK in t:
            skipped += 1
            continue
        if t.count("</main>") != 1:
            problems += 1
            continue
        if "<footer" not in t.split("</main>", 1)[1]:
            problems += 1
            continue
        f.write_text(t.replace("</main>", "</main>\n" + block, 1), encoding="utf-8")
        applied += 1

    print(f"ads: {applied} band(s) wired, {skipped} already present, "
          f"{problems} skipped (no single </main> or no footer after it)")
    print(f"ads: client {client} slot {slot} format {fmt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
