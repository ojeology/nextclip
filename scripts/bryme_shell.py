#!/usr/bin/env python3
"""The shared page shell the BRYME generators build on.

Why this file exists
--------------------
The publishing infrastructure — the canonical origin, the page writer, the
HTML escaper and the JSON-LD dumper — used to live inside build-focus-site.py,
a builder for the retired jobs/make-money/tech desks. Generators imported it
for those four helpers, which meant the repository could not drop the retired
desks without also dropping the shell every live page depends on.

This module is that shell and nothing else: no content, no desks, no data
reads. build-writing-first.py imports it directly, so the Writing desk's build
has no dependency on any retired niche.
"""
from __future__ import annotations

import datetime as _dt
import html
import json
import os
from pathlib import Path

import bryme_config as cfg

ROOT = Path(__file__).resolve().parents[1]
BASE = cfg.site_url()  # canonical origin; SITE_URL env wins over site.config.json
SITE = {"name": cfg.site_name(), "description": cfg.site_description()}

# Static defaults. Generators that are date-sensitive rebind these from
# SOURCE_DATE_EPOCH-aware helpers (see _build_today in build-writing-first.py);
# importing this module must never touch the wall clock on its own.
TODAY = "2026-09-04"
TODAY_HUMAN = "4 September 2026"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def schema(data: object) -> str:
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            .replace("</", "<\\/") + "</script>")


def write(route: str, content: str) -> None:
    """Write a generated page to the tree the routing step then partitions."""
    if route == "/":
        target = ROOT / "index.html"
    else:
        target = ROOT / route.strip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print("wrote", target.relative_to(ROOT))


def footer() -> str:
    """Minimal footer; the Writing desk overrides this with its own."""
    return '''<footer class="site-foot"><div class="wrap foot-grid">
  <div class="foot-brand"><a class="logo" href="/"><span class="logo-mark" aria-hidden="true"></span>BRYME</a><p>BRYME is a free writing resource — guides, tools, and verified opportunities to get published and paid.</p></div>
  <div class="foot-col"><b>Trust</b><a href="/writers/about/">About</a><a href="/writers/editorial-policy/">Editorial policy</a><a href="/writers/corrections/">Corrections</a><a href="/privacy/">Privacy</a><a href="/writers/contact/">Contact</a></div>
  <div class="foot-col"><b>Legal</b><a href="/writers/terms/">Terms</a><a href="/writers/disclaimer/">Disclaimer</a><a href="/writers/copyright/">Copyright</a></div>
</div><div class="wrap foot-bottom">© 2026 BRYME · Independent editorial project · No acceptance, publication or payment is guaranteed.</div></footer>'''


def build_now() -> _dt.datetime:
    """The moment this build should believe it is.

    SOURCE_DATE_EPOCH is the reproducible-builds convention and the only reason
    this helper exists: CI pins it so any commit rebuilds byte-for-byte on a
    later day, while production deploys leave it unset and get the real date.
    """
    epoch = os.environ.get("SOURCE_DATE_EPOCH", "")
    if epoch.isdigit():
        try:
            return _dt.datetime.fromtimestamp(int(epoch), _dt.timezone.utc)
        except (OverflowError, OSError, ValueError):
            pass
    return _dt.datetime.now(_dt.timezone.utc)
