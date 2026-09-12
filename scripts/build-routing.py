#!/usr/bin/env python3
"""STEP 3 of the ecosystem build: path-based routing on the current deployment.

Transforms the built tree from "one writers site at /" into the five-
publication layout:

    /                    -> THE BRYME hub (from ecosystem/hub)
    /writers/<route>     -> the entire existing Writers publication
    /sports/             -> BRYME Sport (from ecosystem/sports)
    /entertainment/      -> BRYME Entertainment (from ecosystem/entertainment)
    /tech/               -> BRYME Tech (from ecosystem/tech)
    /fitness/ /home/     -> foundation placeholders (noindex, from ecosystem/)

Everything is config-driven: ROUTING_MODE=subdomain (later) flips the
properties to their own hosts as a deployment change, not a rebuild.
Writers' page URLs are rewritten (href/src/action/canonical/og/sitemap/
feed/manifest/search-index); shared assets stay at /assets/. Indexing is
explicitly out of scope at this stage (build spec STEP 8).
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROPS = ["sports", "entertainment", "tech", "fitness", "home"]
SITEMAP_PROPS = ["sports", "entertainment", "tech", "fitness", "home"]  # live, indexable properties only
KEEP_AT_ROOT_DIRS = {".git", ".github", "assets", "scripts", "content", "docs", "server", "reports",
                     "node_modules", "public", "ecosystem", ".git"} | set(PROPS) | {"writers"}
KEEP_AT_ROOT_FILES = {"robots.txt", "_redirects", "favicon.ico", "package.json",
                      "package-lock.json", "render.yaml", "site.config.json",
                      "seo-pilot-matrix.csv"}
# verification + provenance files stay at the domain root
import fnmatch
VERIF = {p.name for p in ROOT.glob("google*.html")} | {p.name for p in ROOT.glob("yandex*.html")} | {p.name for p in ROOT.glob("*.txt") if p.name.startswith("17")}

ORIGIN = "https://bryme.onrender.com"
PROP_PREFIXES = tuple(f"/{x}" for x in PROPS) + ("/writers", "/assets")

ATTR_RE = re.compile(r'(\s(?:href|src|action|content)=\x22)(/(?!assets/|writers|sports|entertainment|tech|fitness|home)([^\x22]*))(\x22)')
ABS_RE = re.compile(re.escape(ORIGIN) + r'/(?!writers|sports|entertainment|tech|fitness|home)([^"\'<\s)]*)')


def rewrite_writer_paths(text: str) -> tuple[str, int]:
    """Prefix root-absolute page URLs with /writers (assets stay shared)."""
    n = 0
    text, c = ATTR_RE.subn(r'\1/writers/\3\4', text); n += c
    text, c = ABS_RE.subn(ORIGIN + r'/writers/\1', text); n += c
    # bare home links
    text, c = re.subn(r'(href|action)="/"', r'\1="/writers/"', text); n += c
    return text, n


def rewrite_prop_paths(text: str, prop: str) -> tuple[str, int]:
    """Point a property's root-absolute links at its own prefix."""
    n = 0
    text, c = re.subn(r'href="/(?!/)(?!assets/)(?!' + "|".join(x.lstrip("/") for x in PROP_PREFIXES) + r')(.*?)(")',
                      rf'href="/{prop}/\1\2', text); n += c
    text, c = re.subn(r'href="/"', rf'href="/{prop}/"', text); n += c
    return text, n


def strip_arrows(text: str) -> str:
    """STEP 6: no trailing -> arrows on links/buttons, anywhere."""
    return re.sub(r"\s*(?:&rarr;|→)\s*</a>", "</a>", text)


def main() -> int:
    moved = 0
    # guard: routing is one-shot per build; a routed tree must be rebuilt clean
    if (ROOT / "writers/learn").is_dir() and not (ROOT / "writing").is_dir():
        print("routing: tree is already routed - rebuild clean (rm -rf writers ...) first, aborting")
        return 1
    # 1. move the writers tree into writers/
    wr = ROOT / "writers"
    if wr.exists():
        shutil.rmtree(wr)  # every build regenerates the root tree; re-move fresh
    wr.mkdir()
    for e in list(ROOT.iterdir()):
        name = e.name
        if e.is_dir():
            if name in KEEP_AT_ROOT_DIRS:
                continue
            shutil.move(str(e), str(wr / name))
            moved += 1
        else:
            if name in KEEP_AT_ROOT_FILES or name in VERIF or name.startswith(("BRYME", "BYME", "README")):
                continue
            if name in {"index.html", "404.html", "410.html", "sitemap.xml",
                        "news-sitemap.xml", "feed.xml", "manifest.webmanifest", "sw.js"}:
                shutil.move(str(e), str(wr / name))
                moved += 1
    # sw.js also stays at the root so old service-worker registrations get cleaned
    if (ROOT / "favicon.ico").exists():
        shutil.copy2(ROOT / "favicon.ico", wr / "favicon.ico")  # writers pages link /writers/favicon.ico after the rewrite
    if (wr / "sw.js").exists():
        shutil.copy2(wr / "sw.js", ROOT / "sw.js")
    if not (ROOT / "sw.js").exists():
        # the current build ships no service worker; keep a stub at the root so
        # visitors with the pre-ecosystem worker still get cleanly unregistered
        (ROOT / "sw.js").write_text(
            '// stale-SW cleanup: unregisters the legacy service worker and clears caches\n'
            'self.addEventListener("install", () => self.skipWaiting());\n'
            'self.addEventListener("activate", (e) => { e.waitUntil((async () => {\n'
            '  const keys = await caches.keys(); await Promise.all(keys.map((k) => caches.delete(k)));\n'
            '  await self.registration.unregister();\n'
            '})()); });\n',
            encoding="utf-8")
    if (wr / "favicon.ico").exists():
        shutil.copy2(wr / "favicon.ico", ROOT / "favicon.ico")

    # 2. rewrite writers URLs
    total = 0
    for f in wr.rglob("*"):
        if f.is_file() and f.suffix in (".html", ".xml", ".webmanifest", ".js", ".txt"):
            if f.name in ("hub-tools.js", "studio.js", "theme.js", "site-nav.js",
                          "level-filter.js", "opp-filter.js", "article-filter.js",
                          "purpose-finder.js", "country-filter.js", "tracker.js", "sw.js"):
                continue  # shared/inert scripts: DOM-only, no page URLs
            s = f.read_text(encoding="utf-8")
            s2, n = rewrite_writer_paths(s)
            if f.name == "search-index.js":
                s2, c = re.subn(r'"u":\s*"/(?!writers)', '"u": "/writers/', s2)
                n += c
            s2 = strip_arrows(s2)
            if s2 != s:
                f.write_text(s2, encoding="utf-8")
                total += 1

    # 3. properties + hub out of ecosystem/ to the root
    for prop in PROPS:
        src = ROOT / "ecosystem" / prop
        dst = ROOT / prop
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst,
                        ignore=shutil.ignore_patterns("_recovered"))
        for f in dst.rglob("*.html"):
            s = f.read_text(encoding="utf-8")
            s, _ = rewrite_prop_paths(s, prop)
            f.write_text(strip_arrows(s), encoding="utf-8")
    hub_src = ROOT / "ecosystem" / "hub" / "index.html"
    hub_out = ROOT / "index.html"
    s = hub_src.read_text(encoding="utf-8")
    hub_out.write_text(strip_arrows(s), encoding="utf-8")
    _hub_about = ROOT / "ecosystem" / "hub" / "about"
    if _hub_about.exists():
        shutil.copytree(_hub_about, ROOT / "about", dirs_exist_ok=True)
    import re as _re, datetime as _dt
    _sm = (ROOT / "ecosystem" / "hub" / "sitemap.xml").read_text(encoding="utf-8")
    _sm = _re.sub(r"<lastmod>[^<]*</lastmod>", "<lastmod>" + _dt.date.today().isoformat() + "</lastmod>", _sm)
    (ROOT / "sitemap.xml").write_text(_sm, encoding="utf-8")


    shutil.copy2(ROOT / "ecosystem" / "hub" / "robots.txt", ROOT / "hub-robots.txt")

    # 4. global robots.txt: five sitemaps, no indexing work (STEP 8: untouched)
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /scripts/\nDisallow: /content/\n"
        "Disallow: /docs/\nDisallow: /server/\nDisallow: /ecosystem/\n\n"
        f"Sitemap: {ORIGIN}/writers/sitemap.xml\n" +
        "".join(f"Sitemap: {ORIGIN}/{x}/sitemap.xml\n" for x in SITEMAP_PROPS), encoding="utf-8")

    # 5. allowlist v25: writers prefixed + hub + property routes
    al = json.loads((ROOT / "content" / "index-allowlist.json").read_text())
    routes = set()
    if any(r.startswith("/writers/") for r in al["routes"]):
        routes.update(al["routes"])  # already routed; idempotent re-run
    else:
        for r in al["routes"]:
            routes.add("/writers/" + r[1:] if r != "/" else "/writers/")
    routes.add("/")  # the hub
    routes.add("/about/")  # family about page (b36)
    for prop in SITEMAP_PROPS:
        sm = ROOT / prop / "sitemap.xml"
        for loc in re.findall(r"<loc>(.*?)</loc>", sm.read_text()):
            routes.add("/" + loc.split(ORIGIN + "/", 1)[1])
    al["version"] = 26
    al["routes"] = sorted(routes)
    (ROOT / "content" / "index-allowlist.routed.json").write_text(
        json.dumps(al, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # 6. refresh the public/ mirror to the routed tree
    pub = ROOT / "public"
    if pub.exists():
        shutil.rmtree(pub)
    pub.mkdir()
    EXCL_DIRS = {"scripts", "content", "docs", "server", "reports", "node_modules",
                 "ecosystem", ".git", ".github", "public"}
    MIRROR_FILES = {"index.html", "sitemap.xml", "robots.txt", "hub-robots.txt", "sw.js",
                    "favicon.ico", "manifest.webmanifest", "404.html", "410.html"} | VERIF
    for e in ROOT.iterdir():
        if e.is_dir():
            if e.name not in EXCL_DIRS:
                shutil.copytree(e, pub / e.name)
        elif e.name in MIRROR_FILES:
            shutil.copy2(e, pub / e.name)

    print(f"routing: writers moved ({moved} entries, {total} URL rewrites), "
          f"{len(PROPS)} properties at root paths, allowlist v26 ({len(routes)} routes), public/ mirrored")
    # house 404: branded, desk links, noindex (batch 31) - written AFTER the mirror
    _404 = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page not found | THE BRYME</title>
<meta name="robots" content="noindex,follow">
<style>
body{margin:0;font-family:Georgia,'Times New Roman',serif;background:#101a2b;color:#f5f1e8;display:flex;min-height:100vh;align-items:center;justify-content:center}
main{max-width:640px;padding:40px 24px;text-align:center}
p.kick{letter-spacing:.18em;font-size:12px;color:#c8a24a;text-transform:uppercase;margin:0 0 10px}
h1{font-size:clamp(34px,6vw,54px);margin:0 0 14px}
p{color:#d8d4c8;line-height:1.6;margin:0 0 28px}
nav a{display:inline-block;margin:6px;padding:10px 18px;border:1px solid #3a4a63;border-radius:999px;color:#f5f1e8;text-decoration:none;font-size:15px}
nav a:hover{border-color:#c8a24a}
small{display:block;margin-top:30px;color:#8a94a6}
</style></head>
<body><main>
<p class="kick">Error 404 \u00b7 the page does not exist</p>
<h1>Wrong desk, right house.</h1>
<p>This page either moved or never existed \u2014 and we do not publish fake placeholders in its place. Pick a desk:</p>
<nav>
<a href="/">THE BRYME</a><a href="/writers/">Writers</a><a href="/sports/">Sport</a>
<a href="/entertainment/">Entertainment</a><a href="/tech/">Tech</a><a href="/fitness/">Fitness</a><a href="/home/">Home &amp; DIY</a>
</nav>
<small>THE BRYME \u00b7 research before publishing, and say exactly what you know.</small>
</main></body></html>"""
    (ROOT / "public" / "404.html").write_text(_404, encoding="utf-8")

    # /ad-test/: owner's ad-confirmation page (b36k). Fresh path + fresh asset
    # filename = no cache layer anywhere can serve a stale byte of it.
    _at = ROOT / "public" / "ad-test"
    _at.mkdir(parents=True, exist_ok=True)
    (_at / "index.html").write_text(
        """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Ad confirmation test | THE BRYME</title>
<style>
body{margin:0;font-family:Georgia,serif;background:#fafaf8;color:#1d2735;display:flex;min-height:100vh;align-items:center;justify-content:center}
main{max-width:560px;padding:32px 22px;text-align:center}
p.kick{letter-spacing:.16em;font-size:12px;color:#a4762c;text-transform:uppercase;margin:0 0 8px}
h1{font-size:30px;margin:0 0 12px}
p{line-height:1.6;color:#3d4a5f}
code{background:#efece4;padding:2px 6px;border-radius:4px;font-size:13px}
a{color:#a4762c}
#ad-slot-here{margin:26px auto 8px;min-height:40px}
</style></head>
<body><main>
<p class="kick">Owner tool \u00b7 12 September 2026</p>
<h1>Ad confirmation test</h1>
<p>This page exists only to prove the advertising pipeline on your device. If the system works you will see, within about 30 seconds: a labelled ad slot below \u2014 and a small dark <b>diagnostic box with green text</b> in the bottom-left corner ending in a plain-English verdict.</p>
<div id="ad-slot-here"></div>
<p>If the green box says \u201cFILL DETECTED\u201d \u2014 ads work. If it says the provider sent no ad \u2014 the zones are the issue. If <b>no box appears at all</b>, something on this device or network is blocking the site\u2019s scripts (ad blocker, AdGuard DNS, or a proxy browser such as Opera Mini).</p>
<p><a href="/">Back to THE BRYME</a></p>
</main>
<script src="/assets/ad-live.js" defer></script>
</body></html>
""", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
