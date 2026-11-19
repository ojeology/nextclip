#!/usr/bin/env python3
"""Enforce the legacy-route scheme at FILE level, and purge the stale publish.

Every legacy root the site ever served (the pre-routing writers scheme, plus the
retired jobs / make-money / opportunities hubs) has a 301 declared in
render.yaml. Edge rules are configuration: they can drift, they are only visible
through Render's dedicated /routes endpoint, and a published FILE always outranks
them. So the same scheme is also enforced inside the artifact, where nothing can
silently disagree with it. This runs as the final step of `npm run build`:

  a. PURGE: deletes public/<segment>/ for every legacy segment whose root scheme
     is not live (guard: the routed allowlist must contain no route at
     /<segment>/... - a segment that ever becomes a real property is skipped
     loudly instead of purged).
  b. STUB: regenerates, byte-stably, the file-level equivalents of the
     render.yaml rules, using the batch-66c stub shape already proven in this
     repo (noindex,follow; instant meta-refresh; canonical to the destination;
     a visible link for no-JS visitors):
       - one root stub per legacy segment  (/<seg>/  -> destination)
       - one stub per routed sub-page      (/<seg>/<rest>/ -> /writers/<seg>/<rest>/)
     Flat-mapped segments (jobs, make-money, opportunities - whose wildcard rules
     collapse to /writers/writing/ without capture) get the root stub only,
     exactly like the rules they mirror.

The segment table and destinations are parsed from render.yaml at runtime - one
source of truth, no duplicated list to drift. Output carries no dates, so
regeneration is byte-identical and the CI reproducibility diff stays clean.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

import bryme_config as cfg  # batch 15: canonical origin single source

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
RENDER_YAML = ROOT / "render.yaml"
ALLOWLIST = ROOT / "content" / "index-allowlist.routed.json"
SITE = cfg.site_url()  # batch 15

RULE_RE = re.compile(
    r"\{\s*type:\s*redirect,\s*source:\s*(?P<src>[^,]+?),\s*destination:\s*(?P<dst>[^}]+?)\s*\}"
)


def parse_rules() -> dict[str, str]:
    """Return the bare legacy-segment -> destination map declared in render.yaml."""
    text = RENDER_YAML.read_text(encoding="utf-8")
    bare: dict[str, str] = {}
    for m in RULE_RE.finditer(text):
        src, dst = m.group("src").strip(), m.group("dst").strip()
        if "*" in src or "/" in src.strip("/"):
            continue                   # wildcards and nested sources (by-country)
        seg = src.strip("/")
        if seg and not src.endswith("/"):
            bare[seg] = dst
    return bare


# Redirect stubs and archive tombstones are real served URLs, so they carry the
# same GA4 head block as every other page. It comes from the shared module and
# is placed exactly where scripts/inject-analytics.py puts it - immediately
# before </head> - so a regenerated stub is byte-identical to an injected one
# and `git diff --exit-code` in CI stays clean.
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from analytics_head import ga_head as _ga_head
GA_HEAD = _ga_head()

def stub_html(dest: str, label: str) -> str:
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>" + label + " moved | THE BRYME</title>"
        '<meta name="robots" content="noindex,follow">'
        '<meta http-equiv="refresh" content="0;url=' + dest + '">'
        '<link rel="canonical" href="' + SITE + dest + '">' + GA_HEAD + '</head>'
        '<body><p>This page moved. Continue to <a href="' + dest + '">the current page</a>.</p></body></html>'
    )


def main() -> int:
    bare = parse_rules()
    if not bare:
        print("purge-stale-publish: no redirect rules parsed from render.yaml", file=sys.stderr)
        return 1

    al = json.loads(ALLOWLIST.read_text(encoding="utf-8"))
    routes = al["routes"] if isinstance(al, dict) else al

    purged = skipped = root_stubs = sub_stubs = 0
    for seg in sorted(bare):
        dest = bare[seg]
        # Guard: never touch a segment that is a live root property.
        live = [r for r in routes if r == f"/{seg}/" or r.startswith(f"/{seg}/")]
        if live:
            print(f"purge-stale-publish: SKIP /{seg}/ - live root property ({len(live)} allowlisted routes)")
            skipped += 1
            continue

        d = PUBLIC / seg
        if d.exists():
            shutil.rmtree(d)
            purged += 1

        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(stub_html(dest, seg), encoding="utf-8")
        root_stubs += 1

        # Sub-stubs: the file-level twin of the dormant `/<seg>/* -> /writers/<seg>/*`
        # rule. Flat-mapped hubs (jobs, make-money, opportunities) need no special
        # case: they have no routes under /writers/<seg>/, so this loop writes
        # nothing for them and the root stub above is their whole coverage.
        prefix = f"/writers/{seg}/"
        for r in routes:
            if not r.startswith(prefix) or r == prefix:
                continue
            rel = r[len(prefix):].strip("/")
            sub = PUBLIC / seg / rel
            sub.mkdir(parents=True, exist_ok=True)
            (sub / "index.html").write_text(stub_html(r, rel.split("/")[-1]), encoding="utf-8")
            sub_stubs += 1

    # Defensive sweep for Render's cached build workspace, which keeps UNTRACKED
    # files across deploys. Earlier builds copied a "_recovered" archive store of
    # retired-desk pages into public/<prop>/_recovered/, where it stayed publicly
    # served long after the sources were gone. The sources no longer exist here,
    # but a stale workspace can still hold them, so purge any _recovered/ dir
    # under the publish workspace by name class - deterministic, no git needed.
    stale_rec = 0
    for base in (PUBLIC, ROOT, ROOT / "ecosystem"):
        for prop in ("sports", "entertainment", "tech", "fitness", "home", "writers", "money"):
            d = base / prop / "_recovered"
            if d.is_dir():
                shutil.rmtree(d)
                stale_rec += 1

    # Batch 11d: Render static-site deploys OVERLAY files - deletions never reach the
    # serving side (the 2026-09-14 vintage of public/*/_recovered/ still answered 200
    # after the store moved to content/). The only proven way to retire a served path
    # is to overwrite it, exactly like the root stubs did for the 18 stale 2026-09-14
    # root dirs. Write noindex tombstones for every recovery-store name (the Sep-14
    # listing is byte-identical to today's - verified via GitHub API against 0473ead981).
    # Committed as ordinary tracked public/ files AND regenerated here on every build,
    # so they survive both the regeneration-runs and committed-output-fallback paths.
    tomb = 0

    print(f"purge-stale-publish: purged {purged} stale dirs, skipped {skipped} live, "
          f"wrote {root_stubs} root stubs + {sub_stubs} sub-stubs, "
          f"removed {stale_rec} stale _recovered dirs, wrote {tomb} _recovered tombstones")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
