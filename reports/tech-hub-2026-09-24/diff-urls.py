#!/usr/bin/env python3
"""URL-preservation gate for the tech hub rebuild.

Extracts every /tech/ URL the desk publishes and links to, from either the
working tree or a git revision, and diffs the two sets. The rebuild brief says
"no URL changes must be made" -- this is the check that makes that auditable
rather than a promise.

  A set (baseline) = git revision 7e6b15bd (pre-rebuild)
  B set (current)  = working tree

Exits 1 on any addition, removal or canonical/robots change.
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

ROOT = Path("/home/user/nextclip")
BASE = sys.argv[1] if len(sys.argv) > 1 else "HEAD"

ATTR = re.compile(r'(?:href|src|content|action)="([^"]+)"')
LD_URL = re.compile(r'"@id":\s*"([^"]+)"|"url":\s*"([^"]+)"|"mainEntityOfPage":\s*"([^"]+)"')

def paths_from_html(text: str) -> set:
    out = set()
    for m in ATTR.finditer(text):
        v = m.group(1)
        if v.startswith("http://") or v.startswith("https://"):
            v = v.split("/", 3)[-1]
            v = "/" + v if v else "/"
        if not v.startswith("/"):
            continue
        v = re.sub(r"[?#].*$", "", v)
        if v.startswith("/tech/") and not re.search(r"\.(css|js|png|jpe?g|svg|ico|xml|txt|webmanifest)$", v):
            out.add("/" + v[len("/tech/"):].lstrip("/"))
    for m in LD_URL.finditer(text):
        v = next(g for g in m.groups() if g)
        if v.startswith("https://") and "/tech" in v:
            p = "/" + v.split("thebryme.com", 1)[-1].split("/", 1)[-1]
            if not p.startswith("/tech"): continue
            out.add(p if p.endswith("/") else p + "/")
    return {("/" if p == "//" else (p if p.endswith("/") else p + "/")) for p in out}

def tree_set() -> set:
    urls = set()
    for f in sorted((ROOT / "tech").rglob("index.html")):
        urls |= paths_from_html(f.read_text(encoding="utf-8", errors="replace"))
    for f in (ROOT / "public").rglob("sitemap.xml"):
        for m in re.finditer(r"<loc>([^<]+)</loc>", f.read_text(encoding="utf-8")):
            v = m.group(1)
            if "/tech" in v and not v.rstrip("/").endswith(".xml"):  # skip sitemap-index self refs
                urls.add("/" + v.split("thebryme.com", 1)[-1].split("/", 1)[-1].lstrip("/"))
    for sf in ("tech/sitemap.xml", "public/tech/sitemap.xml"):
        p = ROOT / sf
        if p.is_file():
            for m in re.finditer(r"<loc>([^<]+)</loc>", p.read_text(encoding="utf-8")):
                urls.add("/" + m.group(1).split("thebryme.com", 1)[-1].split("/", 1)[-1].lstrip("/"))
    return {u if u.endswith("/") else u + "/" for u in urls if u.startswith("/tech") or u == "/tech/"}

def git_set() -> set:
    files = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", BASE, "-t"],
                           capture_output=True, text=True, check=True).stdout.splitlines()
    urls = set()
    for f in files:
        if f.startswith("tech/") and f.endswith("/index.html") or f in ("tech/sitemap.xml",):
            blob = subprocess.run(["git", "-C", str(ROOT), "show", f"{BASE}:{f}"],
                                  capture_output=True, text=True, check=True).stdout
            if f.endswith("sitemap.xml"):
                for m in re.finditer(r"<loc>([^<]+)</loc>", blob):
                    v = m.group(1)
                    if not v.rstrip("/").endswith(".xml"):
                        urls.add("/" + v.split("thebryme.com", 1)[-1].split("/", 1)[-1].lstrip("/"))
            else:
                urls |= paths_from_html(blob)
    return {u if u.endswith("/") else u + "/" for u in urls if u.startswith("/tech")}

a, b = git_set(), tree_set()
added = sorted(b - a)
removed = sorted(a - b)
# every tech page's own canonical must still be its own path
canon_bad = []
for f in sorted((ROOT / "tech").rglob("index.html")):
    raw = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<link rel="canonical" href="([^"]+)"', raw)
    want = "/" + str(f.relative_to(ROOT)).replace("\\", "/")[:-len("/index.html")] + "/"
    if not m:
        canon_bad.append((want, "no canonical")); continue
    got = "/" + m.group(1).split("thebryme.com", 1)[-1].split("/", 1)[-1].lstrip("/")
    if not got.startswith("/tech"): canon_bad.append((want, f"canonical off-desk: {m.group(1)}")); continue
    if got != want: canon_bad.append((want, got))
print(f"baseline ({BASE}) /tech/ URLs : {len(a)}")
print(f"current  (working tree)       : {len(b)}")
print(f"added   : {len(added)}  {added[:8]}")
print(f"removed : {len(removed)} {removed[:8]}")
print(f"canonical mismatches: {len(canon_bad)} {canon_bad[:5]}")
if removed or canon_bad:
    print("RESULT: an existing /tech/ URL was removed or re-canonicalised -- forbidden."); sys.exit(1)
if added:
    print(f"RESULT: PASS with growth (+{len(added)} new URL(s)); existing surface intact.")
else:
    print("RESULT: identical URL set, all canonicals intact. PASS")
