#!/usr/bin/env python3
"""Bottom-of-page ad bands. Two providers, both switched off until a key exists.

  adsterra  -- native banner, the format the owner asked for
  adsense   -- native unit, the fallback

Which one runs is decided by site.config.json, in this order:

  1. adsense.nativeSlotId set            -> AdSense band
  2. adsterra.key and adsterra.host set  -> Adsterra native banner
  3. neither                             -> nothing renders (current state)

That empty key is the on-switch. No code change, one value, one deploy.

WHY THE ADSTERRA LOADER IS WRITTEN INTO THE STATIC HTML RATHER THAN INJECTED
BY JAVASCRIPT: Adsterra's support team checks an install through "View page
source". A loader added by client-side JS never appears there, so the unit
reads as not installed. The container div and the invoke.js tag are both
server-rendered here, div first, so the loader always finds its container.

WHY THE NATIVE BANNER AND NOT THE OTHER ADSTERRA FORMATS:
  - Native Banner: one async script plus a container div. No document.write.
  - Classic banner (atOptions + invoke.js): invoke.js calls document.write().
    Harmless during parsing, but it wipes the whole page when it runs after
    load, and atOptions is a page-level global, so a second banner on the same
    page overwrites the first one's config.
  - Popunder and Social Bar: intrusive by definition. AdSense's site behavior
    policy prohibits pages carrying pop-ups or other intrusive ads, so either
    would put the AdSense application at risk.
This file implements the Native Banner only and refuses the rest.

NEVER ON A NOINDEX PAGE: the stub and soft-redirect pages are noindex precisely
because they carry no content of their own. Ads on contentless inventory is the
pattern that gets a site refused, so those pages are skipped. The guard matches
the robots meta tag, not the bare word -- a page that merely discusses noindex
in its copy is still a content page and still gets the band.

WHY NO RESERVED HEIGHT (unlike a fixed-size unit): a native banner's height
varies with how many cards the network returns, so a guessed reservation shifts
the page anyway, and when it does not fill the reservation becomes a visible
hole that then collapses -- a second shift. The slot sits below the whole
article, so growth happens outside the viewport. Unfilled, the wrapper measures
zero and leaves no gap. The wrapper is never display:none, because the loader
measures its container to decide what to render. overflow:hidden is
load-bearing: max-width alone does not constrain a child the loader injects,
and an unresponsive wide creative would otherwise add a horizontal scrollbar.

CSP: the site sends script-src 'self' https: with no unsafe-inline, which is
why the original build-ecosystem.py _ads_slot() could never have worked -- its
push was an inline script. The native banner's loader is an external https
script and the creative renders in an https iframe, so nothing here needs the
policy relaxed and 'unsafe-inline' stays out.

REVERSIBILITY: injection inserts the block immediately after </main> and adds
no whitespace of its own, so --revert restores the file byte for byte.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASES = (ROOT, ROOT / "public")

EXTRA_TIERS = ("ecosystem", "writers", "tech", "sports", "entertainment",
               "fitness", "home", "money")

NOINDEX = re.compile(r'name=["\']robots["\'][^>]*content=["\'][^"\']*noindex', re.I)
NOCONTENT = re.compile(r'<meta[^>]+http-equiv=["\']refresh["\']', re.I)

LABEL = "Advertisement"

# --- AdSense band (fallback) --------------------------------------------------
ADSENSE_MARK = 'data-adband="adsense"'

ADSENSE_BAND = (
    '<aside class="adband" ' + ADSENSE_MARK + ' aria-label="' + LABEL + '">'
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

# --- Adsterra native banner ---------------------------------------------------
ADSTERRA_MARK = 'data-adband="adsterra"'

ADSTERRA_BAND = (
    '<aside class="adband-native" ' + ADSTERRA_MARK + ' aria-label="' + LABEL + '">'
    '<style>'
    '.adband-native{margin:0;padding:26px 0 0}'
    '.adband-native .adband-in{max-width:1100px;margin:0 auto;padding:0 20px;overflow:hidden}'
    '.adband-native .adband-label{display:block;font:500 10px/1 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'
    'letter-spacing:.14em;text-transform:uppercase;color:#8a8578;margin:0 0 10px}'
    '.adband-native .adband-slot{margin:0 auto;max-width:100%;min-height:0}'
    '.adband-native::before{content:"";display:block;max-width:1100px;margin:0 auto 26px;'
    'padding:0 20px;border-top:1px solid rgba(0,0,0,.08)}'
    '</style>'
    '<div class="adband-in">'
    '<span class="adband-label">' + LABEL + '</span>'
    '<div class="adband-slot" id="container-{key}" '
    'data-ad-src="https://{host}/{key}/invoke.js"></div>'
    '</div>'
    '</aside>'
    + '{loader}'
)

REVERT_RES = (
    re.compile(r'<aside class="adband" ' + ADSENSE_MARK + r'[\s\S]*?</aside>'
               r'<script src="/assets/ads-init\.js" defer></script>'),
    re.compile(r'<aside class="adband-native" ' + ADSTERRA_MARK + r'[\s\S]*?</aside>'
               r'(?:<script src="/assets/adsterra-loader\.js" defer></script>'
               r'|<script async data-cfasync="false" src="https://[^"]+"></script>)'),
)


def config() -> tuple[str, dict]:
    """Return (provider, params). provider == '' means the band stays off."""
    try:
        cfg = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
    except Exception as exc:                                    # pragma: no cover
        print(f"ads: could not read site.config.json ({exc}) - skipping")
        return "", {}

    ads = cfg.get("adsense") or {}
    ast = cfg.get("adsterra") or {}

    if ads.get("enabled", True):
        client = str(ads.get("caId") or "").strip()
        slot = str(ads.get("nativeSlotId") or "").strip()
        if client and slot:
            return "adsense", {
                "client": client,
                "slot": slot,
                "fmt": str(ads.get("nativeFormat") or "auto").strip() or "auto",
            }

    if ast.get("enabled", True):
        key = str(ast.get("key") or "").strip()
        host = str(ast.get("host") or "").strip().lstrip("/")
        if key and host:
            if re.search(r"(popunder|socialbar|social-bar|^9d/|/54/)", key + host, re.I):
                print("ads: that Adsterra id looks like a popunder or social-bar unit.")
                print("ads: refusing - those are intrusive, and AdSense's site behavior")
                print("ads: policy bars pages carrying pop-ups. Use the Native Banner key.")
                return "", {}
            try:
                gate = bool((ast or {}).get("gateConsent", True))
            except Exception:
                gate = True
            if not gate:
                print("ads: adsterra.gateConsent is false - the loader will execute for")
                print("ads: every visitor before any consent, including the EEA and UK.")
            return "adsterra", {"key": key, "host": host, "gate": gate}

    return "", {}


def targets() -> list[Path]:
    seen: set[Path] = set()
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
    return sorted(seen)


# The plain loader, kept for adsterra.gateConsent = false. It executes for every
# visitor in every region before any consent, which is why it is not the default.
ADSTERRA_RAW_LOADER = ('<script async data-cfasync="false" '
                       'src="https://{host}/{key}/invoke.js"></script>')

# The default: one local bootstrap that decides when to load the remote script.
ADSTERRA_GATED_LOADER = '<script src="/assets/adsterra-loader.js" defer></script>'


def block_for(provider: str, p: dict) -> str:
    if provider == "adsense":
        # plain substitution, not str.format: the inline CSS is full of braces
        return (ADSENSE_BAND.replace("{client}", p["client"])
                            .replace("{slot}", p["slot"])
                            .replace("{fmt}", p["fmt"]))
    loader = (ADSTERRA_GATED_LOADER if p.get("gate", True)
              else ADSTERRA_RAW_LOADER.replace("{key}", p["key"]).replace("{host}", p["host"]))
    return (ADSTERRA_BAND.replace("{key}", p["key"])
                        .replace("{host}", p["host"])
                        .replace("{loader}", loader))


def revert() -> int:
    """Remove every injected band. Undo for the activation test."""
    n = 0
    for f in targets():
        t = f.read_text(encoding="utf-8", errors="replace")
        if ADSENSE_MARK not in t and ADSTERRA_MARK not in t:
            continue
        for rx in REVERT_RES:
            t = rx.sub("", t)
        f.write_text(t, encoding="utf-8")
        n += 1
    print(f"ads: reverted {n} file(s)")
    return 0


def main() -> int:
    if "--revert" in sys.argv:
        return revert()

    provider, params = config()
    if not provider:
        print("ads: no ad key configured -> band stays off (0 pages touched)")
        print("ads: to activate the Adsterra native banner, set adsterra.key and")
        print("ads: adsterra.host in site.config.json (leave nativeSlotId empty)")
        return 0

    block = block_for(provider, params)
    applied = skipped = problems = upgraded = 0

    for f in targets():
        try:
            t = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if ADSENSE_MARK in t or ADSTERRA_MARK in t:
            # Re-render any existing band to the current template. Skipping
            # outright meant a change to this file never reached the 2,585 pages
            # that already carried the old markup.
            new_t = t
            for rx in REVERT_RES:
                new_t = rx.sub("", new_t)
            new_t = new_t.replace("</main>", "</main>" + block, 1) if "</main>" in new_t else new_t
            if new_t != t:
                f.write_text(new_t, encoding="utf-8")
                upgraded += 1
            else:
                skipped += 1
            continue
        if NOINDEX.search(t) or NOCONTENT.search(t):
            problems += 1
            continue
        if t.count("</main>") != 1:
            problems += 1
            continue
        if "<footer" not in t.split("</main>", 1)[1]:
            problems += 1
            continue
        # inserted with no whitespace of our own, so --revert is byte exact
        f.write_text(t.replace("</main>", "</main>" + block, 1), encoding="utf-8")
        applied += 1

    print(f"ads: {applied} {provider} band(s) wired, {upgraded} upgraded to the current "
          f"template, {skipped} already current, {problems} skipped "
          f"(noindex/stub, no single </main>, or no footer after it)")
    if provider == "adsterra":
        mode = ("consent-gated local bootstrap" if params.get("gate", True)
                else "PLAIN inline tag, no consent gate")
        print(f"ads: container container-{params['key']}, loader "
              f"//{params['host']}/{params['key']}/invoke.js ({mode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
