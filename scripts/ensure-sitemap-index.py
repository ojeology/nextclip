#!/usr/bin/env python3
"""No-op guard for the intentionally empty legacy title-catalogue sitemap.

History: this step used to register entertainment/sitemap-catalogue.xml in the
root sitemap index. Thin title pages were later held out of search while their
recommendation experience was rebuilt. Released Watch This / Then Try This
batches now enter entertainment/sitemap.xml directly, after five distinct
recommendations and their editorial copy pass the batch checks. Unreleased
pages remain noindex and out of the property sitemap; the legacy catalogue
sitemap stays empty and deliberately unregistered.

Kept in the build chain for historical continuity. It must not re-register the
legacy catalogue sitemap or undo the batch-level discovery policy.
"""
print("sitemap-index: legacy title-catalogue sitemap remains empty; released batches use entertainment/sitemap.xml")
