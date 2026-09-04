#!/usr/bin/env python3
"""Single source of truth for BRYME site configuration.

Custom-domain readiness: every generated absolute URL (canonical, sitemap,
JSON-LD, Open Graph, robots, internal canonicalization) comes from this
module. Nothing in the build hard-codes ``bryme.onrender.com``.

Resolution order (highest first):
  1. The ``SITE_URL`` environment variable (used by the Render service and any
     future custom-domain deployment).
  2. ``site.config.json`` -> ``siteUrl`` (the committed default).

The committed default remains the current Render host so that a build with no
``SITE_URL`` set stays byte-identical (deterministic and idempotent) to the
existing release. Setting ``SITE_URL`` at build time repoints the whole site to
a custom domain without touching code.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_CONFIG = ROOT / "site.config.json"


def _config() -> dict:
    return json.loads(_CONFIG.read_text(encoding="utf-8"))


def site_url() -> str:
    """Return the primary canonical origin, without a trailing slash."""
    env = (os.environ.get("SITE_URL") or "").strip().rstrip("/")
    if env:
        return env
    return _config().get("siteUrl", "https://bryme.onrender.com").rstrip("/")


def site_name() -> str:
    return (_config().get("siteName") or "BRYME")


def site_description() -> str:
    return (_config().get("siteDescription") or
            "Verified jobs, remote work and legitimate ways to earn.")


def index_now_key() -> str:
    return str(_config().get("indexNowKey") or "")


def publisher_config() -> dict:
    return _config().get("adsense", {}) or {}
