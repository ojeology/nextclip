#!/usr/bin/env python3
"""The Google Analytics 4 head block, defined once and shared.

Every generator and scripts/inject-analytics.py import this so that a page
regenerated from a template is byte-identical to a page that was injected in
place. Without a single definition the two paths drift apart and the next full
build shows a spurious diff across thousands of files.

Ordering inside the returned block is load-bearing:

  1. `gtag()` is defined and the Consent Mode v2 defaults are set, inline.
  2. The gtag.js loader is requested.
  3. `gtag('config', ...)` runs.

A Google tag that initialises without seeing a consent default assumes consent
was GRANTED, which is the opposite of what the EEA/UK rules require, so the
default has to be the first Google thing on the page - ahead of the AdSense
loader that callers already emit.

The defaults are scoped to the EEA, the UK and Switzerland by explicit ISO
region codes. Visitors elsewhere are never placed in a denied state, so
measurement still works for the audience that reads these desks. Google's own
CMP (AdSense > Privacy & messaging) sends the matching `consent update` when a
visitor makes a choice; this block only governs the moment before that.

Set `analytics.enabled` to false in site.config.json to emit nothing at all.
"""
from __future__ import annotations

import json
from pathlib import Path

# EEA = EU-27 plus Iceland, Liechtenstein and Norway; then the UK and
# Switzerland. Spelled out because the region parameter takes ISO codes.
CONSENT_REGIONS = (
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR",
    "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK",
    "SI", "ES", "SE", "IS", "LI", "NO", "GB", "CH",
)

LOADER_HOST = "googletagmanager.com/gtag/js"

_COMMENT = (
    "<!-- Google tag (gtag.js). Consent Mode v2 defaults precede every Google tag;\n"
    "     scoped to the EEA/UK/CH so visitors elsewhere are unaffected. -->\n"
)


def config(root: Path | None = None) -> dict:
    """The `analytics` block of site.config.json, or {} when absent."""
    root = Path(root) if root else Path(__file__).resolve().parent.parent
    try:
        cfg = json.loads((root / "site.config.json").read_text(encoding="utf-8"))
    except Exception:
        return {}
    return cfg.get("analytics") or {}


def ga_id(root: Path | None = None) -> str:
    an = config(root)
    if not an.get("enabled"):
        return ""
    gid = str(an.get("gaId") or "").strip()
    return gid if gid.startswith("G-") else ""


def ga_head(root: Path | None = None) -> str:
    """The full head block, or "" when analytics is off. Ends with a newline."""
    gid = ga_id(root)
    if not gid:
        return ""
    regions = ",".join("'" + r + "'" for r in CONSENT_REGIONS)
    return (
        _COMMENT
        + "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}\n"
        + "gtag('consent','default',{'ad_storage':'denied','ad_user_data':'denied',"
        + "'ad_personalization':'denied','analytics_storage':'denied',"
        + "'wait_for_update':500,'region':[" + regions + "]});\n"
        + "gtag('js',new Date());</script>\n"
        + '<script async src="https://www.googletagmanager.com/gtag/js?id=' + gid + '"></script>\n'
        + "<script>gtag('config','" + gid + "');</script>\n"
    )
