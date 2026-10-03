#!/usr/bin/env python3
"""Ad bands - Adsterra-first monetization (owner decision 2026-10-03).

AdSense rejected the site after the 2026-10-01 cleanup; the owner pivoted the
house to Adsterra as the PRIMARY network, keeping AdSense as a possible later
pivot. This file wires every approved ad surface, all consent-gated, all
off-switchable from site.config.json with no code change.

WHAT SHIPS

  adsterra native banner - up to three placements per content page:
      top     just inside <main>, under the page header
      middle  after the median paragraph of the article body
      bottom  after </main> (the original band position)
  adsterra social bar   - owner's Social Bar snippet, before </body>
  adsterra display      - owner's classic banner snippet, after </main>
  adsense native band   - fallback; renders only if nativeSlotId is filled

WHY ONE ADSTERRA UNIT KEY PER PLACEMENT: Adsterra's native banner snippet is a
container div plus invoke.js, and the network identifies the install through
that pairing. Running one key in three containers means duplicate ids and an
unverifiable install - Adsterra support checks installs via View Page Source.
Each placement therefore resolves its OWN key/host from
adsterra.placements.<name>, falling back to the shared adsterra.key/host only
when the placement carries none. Create one Native Banner unit per placement
in the Adsterra dashboard and paste each unit's key/host; the slots are
already wired and the build does the rest.

WHY THE LOADER IS SERVER-RENDERED INTO THE HTML: Adsterra's support team
checks an install through "View page source". A loader added by client-side JS
never appears there, so the unit reads as not installed. The container div and
the data-ad-src pointer are both rendered here, div first, so the loader always
finds its container.

CONSENT: /assets/adsterra-loader.js loads each slot immediately outside the
EEA/UK/CH and only after granted ad consent inside them (see that file). The
gateConsent flag still exists; setting it false restores plain inline tags for
every visitor everywhere - read the loader's header before doing that.

NEVER ON A NOINDEX PAGE: stub and soft-redirect pages are noindex precisely
because they carry no content of their own. Ads on contentless inventory is
the pattern that gets a site refused, so those pages are skipped. The guard
matches the robots meta tag, not the bare word.

CSP: script-src 'self' https: with no unsafe-inline. Native-banner loaders are
external https scripts and the creatives render in https iframes, so nothing
here relaxes the policy. The social-bar and display snippets the owner pastes
are external scripts too; if a snippet needs inline script it must be refused,
not allowed by weakening CSP.

HOUSE RULES KEPT FROM docs/ADS.md: no placement may resemble a job card,
employer link, application button or navigation control. Popunders, forced
redirects and notification prompts stay banned - the Adsterra formats approved
are Native Banner, Social Bar and classic display banners only.
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
PLACEMENTS = ("top", "middle", "bottom")
LOADER_TAG = '<script src="/assets/adsterra-loader.js" defer></script>'

# --- AdSense band (future pivot; renders only with a filled nativeSlotId) ----
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

# --- Adsterra native banner (per-placement) ----------------------------------
ADSTERRA_MARK = 'data-adband="adsterra"'

ADSTERRA_BAND = (
    '<aside class="adband-native" ' + ADSTERRA_MARK + ' data-placement="{placement}" '
    'aria-label="' + LABEL + '">'
    '<style>'
    '.adband-native{margin:0;padding:26px 0 0}'
    '.adband-native[data-placement="top"]{padding:14px 0 0}'
    '.adband-native .adband-in{max-width:1100px;margin:0 auto;padding:0 20px;overflow:hidden}'
    '.adband-native .adband-label{display:block;font:500 10px/1 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'
    'letter-spacing:.14em;text-transform:uppercase;color:#8a8578;margin:0 0 10px}'
    '.adband-native .adband-slot{margin:0 auto;max-width:100%;min-height:0}'
    '.adband-native::before{content:"";display:block;max-width:1100px;margin:0 auto 26px;'
    'padding:0 20px;border-top:1px solid rgba(0,0,0,.08)}'
    '.adband-native[data-placement="top"]::before{display:none}'
    '</style>'
    '<div class="adband-in">'
    '<span class="adband-label">' + LABEL + '</span>'
    '<div class="adband-slot" id="container-{key}" '
    'data-ad-src="https://{host}/{key}/invoke.js"></div>'
    '</div>'
    '</aside>'
)

# Raw (ungated) loader, kept for adsterra.gateConsent = false only.
ADSTERRA_RAW_LOADER = ('<script async data-cfasync="false" '
                       'src="https://{host}/{key}/invoke.js"></script>')

# --- Adsterra classic display banner (owner unit, atOptions family) ----------
# The dashboard snippet pairs an inline `atOptions = {...}` config with an
# external invoke.js. The site CSP (script-src 'self' https:, no unsafe-inline)
# bans the inline half, so the band ships only the slot: /assets/adsterra-
# loader.js sets the atOptions object inside a dedicated iframe and loads
# invoke.js there, under the same consent gate as the native slots.
ADSTERRA_DISPLAY_MARK = 'data-adband="adsterra-display"'

ADSTERRA_DISPLAY_BAND = (
    '<aside class="adband-display" ' + ADSTERRA_DISPLAY_MARK +
    ' aria-label="' + LABEL + '">'
    '<style>'
    '.adband-display{margin:0;padding:26px 0 0}'
    '.adband-display .adband-in{max-width:1100px;margin:0 auto;padding:0 20px;overflow:hidden}'
    '.adband-display .adband-label{display:block;font:500 10px/1 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;'
    'letter-spacing:.14em;text-transform:uppercase;color:#8a8578;margin:0 0 10px}'
    '.adband-display .adband-slot-display{margin:0 auto;max-width:100%;border:0}'
    '.adband-display::before{content:"";display:block;max-width:1100px;margin:0 auto 26px;'
    'padding:0 20px;border-top:1px solid rgba(0,0,0,.08)}'
    '</style>'
    '<div class="adband-in">'
    '<span class="adband-label">' + LABEL + '</span>'
    '<div class="adband-slot adband-slot-display" data-ad-kind="display" '
    'data-ad-src="https://{host}/{key}/invoke.js" data-ad-key="{key}" '
    'data-ad-format="{format}" data-ad-width="{width}" data-ad-height="{height}" '
    'style="width:{width}px;height:{height}px;max-width:100%"></div>'
    '</div>'
    '</aside>'
)

ADSTERRA_SOCIAL_MARK = 'data-adband="adsterra-social"'

REVERT_RES = (
    re.compile(r'<aside class="adband" ' + ADSENSE_MARK + r'[\s\S]*?</aside>'
               r'<script src="/assets/ads-init\.js" defer></script>'),
    re.compile(r'<aside class="adband-native" ' + ADSTERRA_MARK +
               r'(?: data-placement="(?:top|middle|bottom)")?[\s\S]*?</aside>'),
    re.compile(r'<script src="/assets/adsterra-loader\.js" defer></script>'),
    re.compile(r'<script async data-cfasync="false" src="https://[^"]+/invoke\.js"></script>'),
    re.compile(r'<div data-adband="adsterra-social"[^>]*></div>'),
    re.compile(r'<aside class="adband-display" ' + ADSTERRA_DISPLAY_MARK +
               r'[\s\S]*?</aside>'),
)


def config() -> dict:
    """Resolve the full ad state from site.config.json."""
    try:
        cfg = json.loads((ROOT / "site.config.json").read_text(encoding="utf-8"))
    except Exception as exc:                                    # pragma: no cover
        print(f"ads: could not read site.config.json ({exc}) - skipping")
        return {}

    ast = cfg.get("adsterra") or {}
    out: dict = {"gate": True, "natives": {}, "social": "", "display": "",
                 "adsense": None}
    if not ast.get("enabled", True):
        return out
    try:
        out["gate"] = bool(ast.get("gateConsent", True))
    except Exception:
        out["gate"] = True

    shared_key = str(ast.get("key") or "").strip()
    shared_host = str(ast.get("host") or "").strip().lstrip("/")
    placements = ast.get("placements") or {}
    for name in PLACEMENTS:
        p = placements.get(name) or {}
        if not p.get("enabled", False):
            continue
        key = str(p.get("key") or "").strip()
        host = str(p.get("host") or "").strip().lstrip("/")
        # Only the bottom placement may borrow the shared unit: Adsterra binds
        # invoke.js to one container per key, so top/middle sharing it would
        # duplicate the container id and render an unverifiable install.
        if not (key and host) and name == "bottom":
            key, host = shared_key, shared_host
        if key and host:
            out["natives"][name] = {"key": key, "host": host}
        else:
            print(f"ads: native placement '{name}' is enabled but has no unit "
                  f"key/host yet - slot stays off until the dashboard unit is "
                  f"pasted into site.config.json")

    social = ast.get("socialBar") or {}
    if social.get("enabled") and str(social.get("script") or "").strip():
        out["social"] = str(social["script"]).strip()
    display = ast.get("displayBanner") or {}
    if display.get("enabled"):
        dkey = str(display.get("key") or "").strip()
        dhost = str(display.get("host") or "").strip().lstrip("/")
        if dkey and dhost:
            out["display"] = {
                "key": dkey, "host": dhost,
                "format": str(display.get("format") or "iframe").strip() or "iframe",
                "width": int(display.get("width") or 300),
                "height": int(display.get("height") or 250),
            }
        else:
            print("ads: displayBanner is enabled but has no unit key/host yet - "
                  "slot stays off until the dashboard unit is pasted into "
                  "site.config.json")

    ads = cfg.get("adsense") or {}
    if ads.get("enabled", True):
        client = str(ads.get("caId") or "").strip()
        slot = str(ads.get("nativeSlotId") or "").strip()
        if client and slot:
            out["adsense"] = {
                "client": client,
                "slot": slot,
                "fmt": str(ads.get("nativeFormat") or "auto").strip() or "auto",
            }
    return out


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


def native_block(name: str, p: dict, gate: bool) -> str:
    band = (ADSTERRA_BAND
            .replace("{placement}", name)
            .replace("{key}", p["key"])
            .replace("{host}", p["host"]))
    if not gate:
        band += (ADSTERRA_RAW_LOADER.replace("{key}", p["key"])
                                    .replace("{host}", p["host"]))
    return band


def apply_page(t: str, state: dict) -> tuple[str, int]:
    """Insert every configured unit once; returns (new_text, bands_added)."""
    for rx in REVERT_RES:
        t = rx.sub("", t)

    bands = 0
    gate = state["gate"]
    loader = False  # LOADER_TAG emitted at least once on this page

    natives = state["natives"]
    main_open = re.search(r"<main[^>]*>", t)

    # bottom band (also carries the shared gated loader when gating is on)
    if "bottom" in natives and t.count("</main>") == 1:
        block = native_block("bottom", natives["bottom"], gate)
        if gate:
            block += LOADER_TAG
            loader = True
        t = t.replace("</main>", "</main>" + block, 1)
        bands += 1

    # top band, just inside <main>
    if "top" in natives and main_open:
        block = native_block("top", natives["top"], gate)
        if gate and "bottom" not in natives:
            block += LOADER_TAG
            loader = True
        pos = main_open.end()
        t = t[:pos] + block + t[pos:]
        bands += 1

    # middle band, after the median paragraph of the main body
    if "middle" in natives and main_open:
        m = re.search(r"<main[^>]*>([\s\S]*?)</main>", t)
        if m:
            paras = [pm for pm in re.finditer(r"<p\b[\s\S]*?</p>", m.group(1))
                     if "adband" not in pm.group(0)]
            if len(paras) >= 4:
                mid = paras[len(paras) // 2]
                block = native_block("middle", natives["middle"], gate)
                if gate and "bottom" not in natives and "top" not in natives:
                    block += LOADER_TAG
                    loader = True
                insert_at = m.start(1) + mid.end()
                t = t[:insert_at] + block + t[insert_at:]
                bands += 1

    # AdSense native band (future pivot), after </main>
    if state["adsense"] and t.count("</main>") == 1:
        a = state["adsense"]
        block = (ADSENSE_BAND.replace("{client}", a["client"])
                             .replace("{slot}", a["slot"])
                             .replace("{fmt}", a["fmt"]))
        t = t.replace("</main>", "</main>" + block, 1)
        bands += 1

    # display banner, after </main>. Always loader-driven: the atOptions
    # config cannot ship inline (CSP), so adsterra-loader.js builds it inside
    # a dedicated iframe. When gating is off the native slots go raw, but the
    # display banner keeps the loader - consent-gating these formats is the
    # house rule and the loader is the only CSP-legal path to it.
    if state["display"] and t.count("</main>") == 1:
        d = state["display"]
        block = (ADSTERRA_DISPLAY_BAND
                 .replace("{key}", d["key"]).replace("{host}", d["host"])
                 .replace("{format}", d["format"])
                 .replace("{width}", str(d["width"]))
                 .replace("{height}", str(d["height"])))
        if not loader:
            block += LOADER_TAG
            loader = True
        t = t.replace("</main>", "</main>" + block, 1)
        bands += 1

    # social bar, before </body>. Marker div only: the loader appends the
    # network's external script under the same consent gate, and the script
    # mounts its own floating widget. Same gate rule as the display banner.
    if state["social"] and "</body>" in t:
        block = ('<div ' + ADSTERRA_SOCIAL_MARK + ' data-ad-kind="social" '
                 'data-ad-src="' + state["social"] + '" hidden aria-hidden="true"></div>')
        if not loader:
            block += LOADER_TAG
            loader = True
        t = t.replace("</body>", block + "</body>", 1)
        bands += 1

    return t, bands


def revert() -> int:
    """Remove every injected unit. Undo for the activation test."""
    n = 0
    for f in targets():
        t = f.read_text(encoding="utf-8", errors="replace")
        if "data-adband" not in t:
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

    state = config()
    natives = state.get("natives", {})
    if not natives and not state.get("social") and not state.get("display") \
            and not state.get("adsense"):
        print("ads: nothing configured -> all bands stay off (0 pages touched)")
        return 0

    applied = skipped = problems = upgraded = 0
    total_bands = 0

    for f in targets():
        try:
            t = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        had_band = "data-adband" in t
        if NOINDEX.search(t) or NOCONTENT.search(t):
            if had_band:
                for rx in REVERT_RES:
                    t = rx.sub("", t)
                f.write_text(t, encoding="utf-8")
            problems += 1
            continue
        new_t, bands = apply_page(t, state)
        if new_t == t:
            if had_band:
                skipped += 1
            continue
        f.write_text(new_t, encoding="utf-8")
        total_bands += bands
        if had_band:
            upgraded += 1
        else:
            applied += 1

    summary = ", ".join(f"{n}: {p['key'][:8]}..." for n, p in sorted(natives.items()))
    print(f"ads: wired {total_bands} unit(s) - native [{summary or 'none'}]"
          f"{' + social bar' if state.get('social') else ''}"
          f"{' + display banner' if state.get('display') else ''}"
          f"{' + adsense band' if state.get('adsense') else ''}; "
          f"{applied} page(s) new, {upgraded} upgraded, {skipped} already "
          f"current, {problems} skipped (noindex/stub)")
    if not state["gate"] and natives:
        print("ads: WARNING adsterra.gateConsent=false - units load for every "
              "visitor before any consent, including the EEA and UK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
