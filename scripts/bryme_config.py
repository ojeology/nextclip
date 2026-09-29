#!/usr/bin/env python3
"""Shared source for generated canonical origins and site metadata.

Generated absolute URLs that use this helper resolve in this order:
  1. The ``SITE_URL`` environment variable.
  2. ``site.config.json`` -> ``siteUrl``.
  3. The current public origin, ``https://thebryme.com``.

The committed config already selects the custom-domain origin. Keep the final
fallback aligned with it so a missing environment/config value cannot silently
reintroduce the retired Render hostname into canonicals or sitemaps.
"""
from __future__ import annotations

import html
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
    return _config().get("siteUrl", "https://thebryme.com").rstrip("/")


def site_name() -> str:
    return (_config().get("siteName") or "BRYME")


def site_description() -> str:
    return (_config().get("siteDescription") or
            "Legitimate paid-writing opportunities, practical writing guides, and BRYME's firsthand verification record.")


def index_now_key() -> str:
    return str(_config().get("indexNowKey") or "")


def publisher_config() -> dict:
    return _config().get("adsense", {}) or {}


def pinterest_verification_meta() -> str:
    """Return the escaped Pinterest domain-verification tag, if configured."""
    settings = _config().get("pinterest") or {}
    if not isinstance(settings, dict):
        return ""
    value = str(settings.get("domainVerification") or "").strip()
    if not value:
        return ""
    return (
        '<meta name="p:domain_verify" content="'
        + html.escape(value, quote=True)
        + '"/>'
    )
