#!/usr/bin/env python3
"""Final-chain no-op: the entertainment catalogue is no longer index-registered.

History: this step used to guarantee the separated entertainment catalogue
sitemap (entertainment/sitemap-catalogue.xml) appeared in the root sitemap
index even if a cached/generated root sitemap omitted it.

2026-10-01 (owner decision, AdSense review): the 719 catalogue cards went
noindex,follow until AdSense approval - URLs stay published at 200 with their
internal links intact, but nothing is submitted for indexing. The catalogue
sitemap's urlset is deliberately empty and build-routing.py no longer appends
it to the root index. There is therefore nothing to ensure.

The step is kept (not deleted) so the `npm run build` chain order and the
historical logs stay readable; it exits without touching any file. When the
cards are re-indexed after approval, restore registration in build-routing.py
(step 3 root-index append + step 5 catalogue allowlist block - both still
present, the latter already tolerant of an empty urlset) and refill the
sitemap via build-ecosystem.py.
"""
print("sitemap-index: catalogue delisted 2026-10-01 (noindex until AdSense approval); nothing to ensure")
