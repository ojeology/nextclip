#!/usr/bin/env python3
"""Build THE BRYME ecosystem — the four publications + master homepage.

Per the Master Ecosystem Rebuild plan:
  thebryme.com            -> ecosystem/hub/            (parent homepage)
  writers.thebryme.com    -> the existing site (this repo's main build)
  sports.thebryme.com     -> ecosystem/sports/        (newsroom identity)
  entertainment.thebryme.com -> ecosystem/entertainment/ (cinematic identity)
  tech.thebryme.com       -> ecosystem/tech/          (modern-technical identity)

Each directory is a self-contained static service (own css, sitemap,
robots). The production hostname comes from the PRODUCTION_DOMAIN env
var, falling back to ecosystem/config.json — never hard-coded. This
script is run manually (python3 scripts/build-ecosystem.py); its output
is committed so each dir can be pointed at by its own Render service.

Content rules honoured: no betting content in Sports; no piracy in
Entertainment (information only); recovered archive articles keep their
own words, re-typeset, with honest archive labels.
"""
from __future__ import annotations

import html
import shutil
import json
import os
import sys
import re
from pathlib import Path
from xml.sax.saxutils import escape as xesc

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
OUT = ROOT / "ecosystem"
CFG = json.loads((ROOT / "ecosystem" / "config.json").read_text(encoding="utf-8"))
DOMAIN = os.environ.get("PRODUCTION_DOMAIN") or CFG["domain"]
MODE = os.environ.get("ROUTING_MODE") or CFG.get("mode", "path")
ORIGIN = os.environ.get("ORIGIN") or CFG.get("origin", "https://bryme.onrender.com")
TODAY = "2026-09-09"

# ---------------------------------------------------------------- family css
BASE_CSS = """
:root{--paper:%(paper)s;--sheet:%(sheet)s;--ink:%(ink)s;--muted:%(muted)s;--dim:%(dim)s;
--brand:%(brand)s;--brand-deep:%(brand_deep)s;--accent:%(accent)s;
--line:rgba(%(line)s,.18);--line-strong:rgba(%(line)s,.4);--shadow:0 1px 2px rgba(0,0,0,.05),0 14px 38px rgba(0,0,0,.08);
--serif:Georgia,'Iowan Old Style','Palatino Linotype',serif;--sans:Inter,ui-sans-serif,system-ui,sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;min-height:100vh;color:var(--ink);background:var(--paper);font:16px/1.65 var(--sans);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}::selection{background:rgba(176,141,87,.3)}
.wrap{width:min(calc(100%% - 48px),1080px);margin:0 auto}
a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.skip-link{position:fixed;z-index:99;top:10px;left:10px;transform:translateY(-160%%);padding:10px 16px;background:var(--brand);color:var(--sheet);font-weight:700}
.skip-link:focus{transform:none}
.head{position:sticky;z-index:50;top:0;background:var(--paper);border-bottom:1px solid var(--line-strong)}
.head::before{content:"";display:block;height:6px;background:var(--brand)}
.head::after{content:"";display:block;height:2px;background:var(--accent)}
.mast{display:flex;align-items:baseline;gap:18px;padding:18px 0 12px;flex-wrap:wrap}
.mast-brand{font-family:var(--serif);font-size:34px;line-height:.9;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.mast-brand span{color:var(--accent)}
.mast-tag{font:italic 13px var(--serif);color:var(--muted);flex:1;min-width:200px}
.parent-link{font:750 10.5px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);padding:7px 11px;border-radius:2px}
.parent-link:hover{color:var(--ink);border-color:var(--line-strong)}
.cover{padding:clamp(46px,8vw,96px) 0 clamp(36px,6vw,64px);border-bottom:3px double var(--line-strong)}
.kicker{color:var(--accent);font:800 11.5px var(--sans);letter-spacing:.22em;text-transform:uppercase;margin:0 0 20px}
h1.cover-title{font-family:var(--serif);font-weight:700;letter-spacing:-.018em;font-size:clamp(36px,6.4vw,70px);line-height:1.03;margin:0;max-width:15em}
.cover-dek{font-family:var(--serif);font-size:clamp(16.5px,2.2vw,20px);line-height:1.62;color:var(--muted);max-width:58ch;margin:24px 0 0}
.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.btn{min-height:46px;display:inline-flex;align-items:center;padding:11px 20px;border:1px solid var(--brand);border-radius:2px;background:var(--brand);color:var(--sheet);font:700 13.5px var(--sans);letter-spacing:.04em;cursor:pointer}
.btn:hover{background:var(--brand-deep);border-color:var(--brand-deep)}
.btn.secondary{background:transparent;color:var(--brand);border-color:var(--line-strong)}
.btn.secondary:hover{border-color:var(--brand);background:transparent}
.section{padding:clamp(42px,7vw,80px) 0}
.section.alt{background:var(--paper-2,transparent);outline:1px solid var(--line);outline-offset:-1px}
.section-head{margin-bottom:28px}
.section-head h2{font-family:var(--serif);font-weight:700;font-size:clamp(23px,3.2vw,32px);line-height:1.12;margin:6px 0 0;letter-spacing:-.012em}
.section-head h2::after{content:"";display:block;width:46px;height:4px;background:var(--accent);margin-top:14px}
.lede{font-family:var(--serif);font-size:17.5px;line-height:1.65;color:var(--muted);max-width:60ch;margin:18px 0 0}
.list{list-style:none;margin:0;padding:0;border-top:1px solid var(--line-strong)}
.list li{border-bottom:1px solid var(--line)}
.list a{display:flex;gap:22px;align-items:baseline;padding:18px 6px;transition:background .15s ease,padding-left .15s ease}
.list a:hover{background:var(--sheet);padding-left:14px}
.list b{font-family:var(--serif);font-size:19px;line-height:1.3}
.list a:hover b{color:var(--brand)}
.list small{display:block;font:13px var(--sans);color:var(--muted);margin-top:3px}
.list .meta{margin-left:auto;flex:none;font:750 11px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.prose{max-width:720px;margin:0 auto;padding:clamp(28px,5vw,54px) 0 26px}
.prose h2{font-family:var(--serif);font-size:clamp(22px,3vw,29px);line-height:1.16;margin:44px 0 12px;padding-top:24px;border-top:1px solid var(--line)}
.prose h3{font-family:var(--serif);font-size:19.5px;margin:28px 0 8px}
.prose h3::before{content:"";display:inline-block;width:20px;height:4px;background:var(--accent);margin-right:11px;vertical-align:middle}
.prose p,.prose li{font-family:var(--serif);font-size:18px;line-height:1.78}
.prose p{margin:0 0 19px}
.prose ul,.prose ol{padding-left:26px;margin:0 0 19px}
.prose li+li{margin-top:9px}
.prose a{color:var(--brand);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
.prose blockquote{margin:32px 0;padding:6px 0 6px 24px;border-left:4px solid var(--accent);font-family:var(--serif);font-style:italic;font-size:21px;line-height:1.5}
.prose img{max-width:100%%;border:1px solid var(--line);padding:6px;background:var(--sheet)}
.crumb{padding:18px 0 10px;font:11.5px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.crumb a{color:var(--muted)}.crumb a:hover{color:var(--accent)}
.byline{margin:16px 0 0;font-size:13px;color:var(--muted);border-top:1px solid var(--line);padding-top:13px}
.foot{margin-top:44px;border-top:3px double var(--line-strong);background:var(--paper-2,transparent)}
.foot-in{padding:34px 0 30px;display:flex;flex-wrap:wrap;gap:14px 34px;justify-content:space-between;font:13px var(--sans);color:var(--muted)}
.foot-in a:hover{color:var(--ink)}
.foot small{display:block;margin-top:8px;font:italic 12.5px var(--serif);color:var(--dim)}
.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.pub-card{border:1px solid var(--line-strong);border-top:6px solid var(--pc);background:var(--sheet);padding:26px 26px 22px;display:flex;flex-direction:column}
.pub-card h3{font-family:var(--serif);font-size:24px;margin:0 0 4px;letter-spacing:-.01em}
.pub-card .pc-kicker{font:800 10.5px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--pc);margin:0 0 12px}
.pub-card p{font-size:14.5px;line-height:1.6;color:var(--muted);margin:0 0 18px}
.pub-card .btn{margin-top:auto;align-self:flex-start}
.pub-card.live{box-shadow:var(--shadow)}
.pub-card.soon{opacity:.92}
.soon-tag{font:800 10px var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--muted);border:1px dashed var(--line-strong);align-self:flex-start;padding:8px 12px;margin-top:auto}
@media(max-width:820px){.cards{grid-template-columns:1fr}.mast-tag{display:none}}
@media print{.head,.foot,.actions,.btn{display:none!important}body{background:#fff}}
"""

FAMILY = {
    "writers":       dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#14213d", brand_deep="#0c1526", accent="#a8752a", line="20,33,61"),
    "hub":           dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#14213d", brand_deep="#0c1526", accent="#a8752a", line="20,33,61"),
    "sports":        dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#2f6b4f", brand_deep="#1f4d37", accent="#2f6b4f", line="20,33,61"),
    "entertainment": dict(paper="#17151a", sheet="#201d24", ink="#efe9dd", muted="#b5ad9f", dim="#8b8478", brand="#6d1832", brand_deep="#4d1023", accent="#a8752a", line="239,233,221"),
    "tech":          dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#14213d", brand_deep="#0c1526", accent="#5b6b7a", line="20,33,61"),
}

FAMILY["fitness"] = dict(FAMILY["tech"])
FAMILY["home"] = dict(FAMILY["tech"])

HOME_CSS_EXTRA = """
html{color-scheme:light}
[data-theme="dark"]{--paper:#131318;--sheet:#1b1b23;--ink:#e9e6df;--muted:#a7a29a;--dim:#7e7970;--brand:#4a7aa8;--brand-deep:#3a628c;--accent:#c9994e;--line:rgba(233,230,223,.14);--line-strong:rgba(233,230,223,.32);--shadow:0 1px 2px rgba(0,0,0,.45),0 14px 38px rgba(0,0,0,.5);color-scheme:dark}
[data-theme="dark"] .btn{color:#fff}
[data-theme="dark"] .skip-link{color:#fff}
[data-theme="dark"] ::selection{background:rgba(201,153,78,.35)}
.theme-btn{margin-left:auto;flex:none;align-self:center;border:1px solid var(--line-strong);background:transparent;color:var(--muted);border-radius:99px;width:44px;height:36px;cursor:pointer;font-size:15px;line-height:1}
.theme-btn:hover{color:var(--ink);border-color:var(--accent)}
.h-layout{display:grid;grid-template-columns:236px minmax(0,1fr);gap:48px;align-items:start}
.h-side{position:sticky;top:112px;padding:28px 0}
.h-side-title{font:800 10.5px var(--sans);letter-spacing:.22em;text-transform:uppercase;color:var(--dim);margin:0 0 10px;padding-left:10px}
.h-side nav{display:block}
.h-side nav a{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:9px 10px;border-left:2px solid transparent;font:600 13.5px var(--sans);color:var(--muted)}
.h-side nav a:hover{color:var(--ink);background:var(--sheet)}
.h-side nav a.active{color:var(--brand);border-left-color:var(--brand);background:var(--sheet)}
.h-side nav a.flag{color:var(--accent)}
.h-side nav a.active.flag{color:var(--accent)}
.h-side nav a .n{font:700 10.5px var(--sans);color:var(--dim);border:1px solid var(--line);padding:1px 7px;border-radius:99px;flex:none}
.h-main .cover{padding:clamp(30px,5vw,58px) 0 clamp(26px,4vw,44px)}
.h-main h1.cover-title{font-size:clamp(30px,4.8vw,52px)}
.h-sec-card{border:1px solid var(--line);padding:20px 22px;background:var(--sheet)}
.h-sec-card h3{font-family:var(--serif);font-size:21px;margin:6px 0 6px}
.h-sec-card p{margin:0;color:var(--muted);font-size:14.5px}
.h-sec-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
@media (max-width:920px){.h-layout{display:block}.h-side{position:static;padding:16px 0;border-bottom:1px solid var(--line)}
.h-side nav{display:flex;gap:8px;overflow-x:auto;padding-bottom:4px}
.h-side nav a{border:1px solid var(--line);border-radius:99px;padding:7px 14px;white-space:nowrap;border-left-width:1px}
.h-side nav a.active{border-color:var(--brand)}
.h-sec-grid{grid-template-columns:1fr}}
"""

FITNESS_CSS_EXTRA = """
.fp-week .fp-day { display: grid; grid-template-columns: 44px 1fr auto; gap: 14px; align-items: center; }
.fp-day .fp-num { font-family: var(--serif); font-size: 22px; color: var(--accent); text-align: right; }
.fp-day small { display: block; color: var(--dim); font-size: 12.5px; margin-top: 2px; }
.fp-day.done { opacity: .55; }
.fp-day.done .fp-num::after { content: " \u2713"; color: var(--brand); }
.fp-progressbar { height: 10px; background: var(--sheet); border: 1px solid var(--line); border-radius: 99px; overflow: hidden; }
.fp-fill { height: 100%; width: 0%; background: var(--brand); transition: width .3s ease; }
@media (max-width: 640px) { .fp-week .fp-day { grid-template-columns: 34px 1fr; } .fp-day .fp-done { grid-column: 2; justify-self: start; } }
"""

def css_for(pub):
    return BASE_CSS % FAMILY[pub] + (FITNESS_CSS_EXTRA if pub in ("fitness", "home") else "") + (HOME_CSS_EXTRA if pub == "home" else "")

def shell(pub, title, desc, route, body, card=None, robots="index,follow"):
    d = route  # mode-aware base URL from SUB
    og = f"https://{route}/assets/og.png" if route else f"https://{DOMAIN}/assets/og.png"
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{d}{'' if route.endswith('/') else ''}">
<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{d}"><meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<style>{css_for(pub)}</style>
</head><body><a class="skip-link" href="#main">Skip to content</a>
{body}
</body></html>"""

def head(pub, tagline, parent=True):
    pl = f'<a class="parent-link" href="https://{DOMAIN}/">THE BRYME</a>' if parent and pub != "hub" else ""
    name = "THE&nbsp;BRYME" if pub == "hub" else f"{{'BRYME'}}&nbsp;<span>{PUB_NAME[pub].upper()}</span>"
    brand = "THE&nbsp;BRYME" if pub == "hub" else f'BRYME&nbsp;<span style="color:var(--accent)">{PUB_NAME[pub].upper()}</span>'
    return f"""<header class="head"><div class="wrap mast">
<a class="mast-brand" href="/">{brand}</a>
<span class="mast-tag">{tagline}</span>
{pl}
</div></header>"""

def foot(pub, extra=""):
    _trust = (' \u00b7 <a href="/tech/methodology/">Methodology</a> \u00b7 <a href="/tech/corrections/">Corrections</a>'
              ' \u00b7 <a href="/tech/terms/">Terms</a> \u00b7 <a href="/tech/disclaimer/">Disclaimer</a>') if pub == "tech" else ""
    x = extra or _trust
    return f"""<footer class="foot"><div class="wrap foot-in">
<div>© 2026 THE BRYME — {PUB_NAME[pub] if pub != 'hub' else 'the BRYME publications'}.</div>
<div><a href="/{'writers' if pub == 'hub' else pub}/about/">About</a> · <a href="/{'writers' if pub == 'hub' else pub}/privacy/">Privacy</a> · <a href="/{'writers' if pub == 'hub' else pub}/contact/">Contact</a>{x}</div>
<div><a href="https://{DOMAIN}/">thebryme.com</a></div>
</div></footer>"""

def write_placeholder(key, name, tagline, identity, planned):
    """Foundation-era property: one honest page + the standard legal pages, all noindex."""
    items = "".join("<li>" + html.escape(x) + "</li>" for x in planned)
    body = (head(key, tagline)
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/">THE BRYME</a> / ' + html.escape(name) + "</nav>"
        + '<section class="cover"><p class="kicker">Under construction \u00b7 foundation laid</p>'
        + '<h1 class="cover-title">' + html.escape(name) + "</h1>"
        + '<p class="cover-dek">' + html.escape(identity) + "</p></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The plan</p><h2>What this desk will cover.</h2></div>'
        + '<ul class="list">' + items + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Honest status</p><h2>Nothing to read here yet.</h2></div>'
        + '<p class="lede">This property is at the foundation stage: the route, standards and plan exist; the guides are being built and will open when they are worth reading. In the meantime, the live desks are <a href="/writers/">BRYME Writers</a>, <a href="/tech/">BRYME Tech</a>, <a href="/sports/">BRYME Sport</a>, <a href="/entertainment/">BRYME Entertainment</a> and <a href="/fitness/">BRYME Fitness</a>.</p>'
        + '</section></div></main>' + foot(key))
    base = OUT / key
    base.mkdir(parents=True, exist_ok=True)
    for route, title, desc, pbody in [("/", name + " | BRYME", tagline, body)] + legal_pages(key, name, tagline):
        f = base / ("index.html" if route == "/" else route.lstrip("/") + "/index.html")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(shell(key, title, desc, ORIGIN + "/" + key + route, pbody, robots="noindex,follow"), encoding="utf-8")
    print(key + ": foundation page + legal (noindex, no sitemap)")


PUB_NAME = {"sports": "Sport", "entertainment": "Entertainment", "tech": "Tech", "fitness": "Fitness", "home": "Home & DIY"}

def write_service(pub, pages):
    base = OUT / pub
    base.mkdir(parents=True, exist_ok=True)
    # clear stale output from earlier builds; the recovery store survives
    for e in base.iterdir():
        if e.name == "_recovered":
            continue
        shutil.rmtree(e) if e.is_dir() else e.unlink()
    (base / "assets").mkdir(exist_ok=True)
    (base / "assets" / "site.css").write_text(css_for(pub), encoding="utf-8")
    urls = []
    for route, title, desc, body in pages:
        p = base / route.lstrip("/")
        p.mkdir(parents=True, exist_ok=True)
        full = shell(pub, title, desc, SUB[pub] + route, body)
        (p / "index.html").write_text(full, encoding="utf-8")
        urls.append(SUB[pub] + route)
    (base / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
        + "\n</urlset>\n", encoding="utf-8")
    (base / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SUB[pub]}/sitemap.xml\n", encoding="utf-8")
    print(f"{pub}: {len(pages)} pages, sitemap, robots")

PREFIX = {"sports": "/sports", "entertainment": "/entertainment", "tech": "/tech", "fitness": "/fitness", "home": "/home"}
if MODE == "subdomain":
    SUB = {k: f"https://{v}.{DOMAIN}" for k, v in CFG["subdomains"].items() if k in PREFIX}
    SUB["writers"] = f"https://writers.{DOMAIN}"
else:
    SUB = {k: ORIGIN + pfx for k, pfx in PREFIX.items()}
    SUB["writers"] = ORIGIN + "/writers"
SUB["hub"] = f"https://{DOMAIN}" if MODE == "subdomain" else ORIGIN

def legal_pages(pub, name, tagline):
    about_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / About</nav>
<section class="cover"><p class="kicker">About</p><h1 class="cover-title">{name}</h1>
<p class="cover-dek">{tagline}</p></section>
<section class="section"><div class="prose">
<p>{name} is one of the BRYME publications — a family of independent, specialist sites under THE BRYME. Each publication has its own focus, its own standards and its own editorial line; what they share is the house discipline: research before publishing, dates on anything time-sensitive, and no fabricated experience or statistics.</p>
<p>BRYME began as a writers' resource and grew into a small ecosystem of publications. The family is edited from Lagos, Nigeria, and written for a global readership.</p>
<h2>Editorial standards</h2>
<ul>
<li>Evergreen, genuinely useful work over volume.</li>
<li>First-hand experience where we have it; clearly labelled archive or research material where we don't.</li>
<li>Corrections in the open, on the page that made the claim.</li>
<li>No betting content, no piracy, no fabricated data — the house rules, applying everywhere.</li>
</ul>
</div></section></div>"""
    privacy_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Privacy</nav>
<section class="cover"><p class="kicker">Privacy</p><h1 class="cover-title">What we collect: almost nothing.</h1></section>
<section class="section"><div class="prose">
<p>{name} is a static publication. It sets no tracking cookies, runs no analytics on these pages, and asks for no personal information. Reading it is between you and your browser.</p>
<p>If interactive tools are added later, any data they store will stay in <em>your</em> browser's local storage on <em>your</em> device — the standing BRYME pattern — and this page will be updated before that changes.</p>
<p>Advertising, when introduced, will follow Google AdSense policies: clearly separated from content and navigation, never covering text, never encouraging clicks. Ad partners may set their own cookies under their own policies.</p>
<p>Questions: see <a href="/contact/">Contact</a>.</p>
</div></section></div>"""
    contact_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Contact</nav>
<section class="cover"><p class="kicker">Contact</p><h1 class="cover-title">Reach the desk.</h1>
<p class="cover-dek">Corrections first: if something on {name} is wrong, that is the most valuable email in the world to us.</p></section>
<section class="section"><div class="prose">
<p>Editorial contact details go live with the publication's domain launch. Until then, {name} is reached through <a href="https://writers.thebryme.com/contact/">the BRYME Writers contact page</a>, which routes to the same editorial desk.</p>
<h2>What to include</h2>
<ul><li>The page address and the exact claim that needs correcting.</li>
<li>For pitches: a two-paragraph summary and one relevant sample. No attachments.</li></ul>
</div></section></div>"""
    def _m(b):
        return b if "<main" in b else '<main id="main"><div class="wrap">' + b + "</div></main>"
    return [("/about/", f"About {name} | BRYME", f"What {name} is and the standards it holds.", _m(about_body)),
            ("/privacy/", f"Privacy | {name}", "What BRYME collects (almost nothing) and how advertising will be handled.", _m(privacy_body)),
            ("/contact/", f"Contact | {name}", "Corrections, pitches and the editorial desk.", _m(contact_body))]


# ------------------------------------------------------------------ 1. HUB
HUB_PUBS = [
    ("writers", "BRYME Writers", "The flagship.", "The practical digital library and workspace for writers \u2014 191 researched guides, 44 free browser tools, a hand-verified opportunity database and the essays behind the market. Free, independent, human-verified.", "live"),
    ("sports", "BRYME Sport", "The desk reopens.", "Football coverage from BRYME's media desk \u2014 transfer reporting, matchweek guides and the 2026-27 season, with the archive's thin pages honestly retired. No betting content, ever.", "live"),
    ("entertainment", "BRYME Entertainment", "Recovered from the archive.", "Cinema, TV and anime \u2014 guides, explainers and opinion rebuilt from BRYME's earliest editorial research, re-typeset and honestly labelled. No download sites, no piracy \u2014 only writing about the work.", "live"),
    ("tech", "BRYME Tech", "Practical technology. No theatre.", "Deployment walkthroughs, domain and DNS specifics, token hygiene, front-end patterns \u2014 written from first-hand builds, not press releases. Evergreen on purpose.", "live"),
]
WORKSHOP_PUBS = [
    ("fitness", "BRYME Fitness", "Foundation laid.", "Practical fitness guidance \u2014 beginner programs, walking and strength challenges, and 30-day plans built around returning one day at a time. General fitness information, never medical advice. The first programs are being built now.", "foundation"),
    ("home", "BRYME Home & DIY", "Now open.", "Practical help for fixing, maintaining and understanding your home \u2014 low-risk repairs explained honestly, an in-browser seasonal checklist, and safety boundaries stated without apology.", "live"),
]

def hub_pages():
    cards = ""
    for key, name, tag, desc, state in HUB_PUBS + WORKSHOP_PUBS:
        kicker = PUB_NAME.get(key, "").upper() if key != "writers" else "THE FLAGSHIP"
        if state == "live":
            cta = f'<a class="btn" href="{SUB[key]}/">Enter {name.split(" ")[1]} →</a>'
            cls = "pub-card live"
        else:
            cta = '<span class="soon-tag">In build — opens soon</span>'
            cls = "pub-card soon"
        cards += f'<article class="{cls}" style="--pc:{FAMILY[key]["brand"] if key!="hub" else "#1e3a5f"}"><p class="pc-kicker">{kicker}</p><h3>{name}</h3><p>{desc}</p>{cta}</article>'
    body = f"""{head("hub", "Five publications. One house standard.", parent=False)}
<main id="main"><div class="wrap">
<section class="cover"><p class="kicker">A family of independent publications</p>
<h1 class="cover-title">THE BRYME</h1>
<p class="cover-dek">BRYME is a small ecosystem of specialist publications, each with its own focus and its own standards, held to one house rule: research before publishing, and say exactly what you know. Pick a desk.</p></section>
<section class="section"><div class="section-head"><p class="kicker">The publications</p><h2>Choose your desk</h2></div>
<div class="cards">{cards}</div></section>
<section class="section alt"><div class="section-head"><p class="kicker">The house</p><h2>One standard, five voices.</h2></div>
<p class="lede">Every BRYME publication is edited by the same desk, run on the same discipline — dates on time-sensitive claims, corrections in the open, no fabricated experience, no pages built to game a search engine — and none of them share a navigation bar. When you enter one, you are in that world.</p>
</section></div></main>
{foot("hub")}"""
    hub_index = [("index.html placeholder", "", "", "")]
    return [("/", "THE BRYME — a family of independent publications",
             "BRYME is four specialist publications — Writers, Sport, Entertainment and Tech — under one house standard. Choose your desk.", body)]


# ------------------------------------------------------- 2. ENTERTAINMENT
def clean_recovered(raw):
    raw = re.sub(r"<h1\b[^>]*>[\s\S]*?</h1>", "", raw, count=1)
    # strip links to the retired catalog (dead routes) — keep external http(s)
    raw = re.sub(r'<a\s[^>]*href="(/[^"]*)"[^>]*>(.*?)</a>', r"\2", raw, flags=re.S)
    raw = re.sub(r"<img[^>]*>", "", raw)
    return raw

ENT_SECTIONS = {
    "recommendations": ("What to watch next", "Recommendations, starter routes and watch orders \u2014 the answer to \u201cwhat should I watch tonight?\u201d, argued honestly rather than scraped."),
    "explainers": ("Explainers & comparisons", "Why a show became a phenomenon, what a character\u2019s choice really meant, and the head-to-heads fans actually argue about."),
    "opinion": ("Opinion & lists", "Reviews with a spine, cult favourites defended, and lists with a reason behind every entry \u2014 labelled as opinion, written as argument."),
}
ENT_SLUG_SECT = {
    "10-anime-like-solo-leveling-you-should-watch": "recommendations",
    "10-shows-like-alice-in-borderland-you-should-watch-next": "recommendations",
    "movies-like-deadpool-and-wolverine": "recommendations",
    "movies-like-interstellar-guide": "recommendations",
    "movies-like-parasite": "recommendations",
    "christopher-nolan-movies-order": "recommendations",
    "korean-cinema-starter-guide-rebuilt": "recommendations",
    "indian-cinema-first-five": "recommendations",
    "modern-horror-starter-route": "recommendations",
    "nigerian-thrillers-worth-your-time": "recommendations",
    "how-to-pick-a-movie-tonight": "recommendations",
    "best-streaming-apps-nigeria": "recommendations",
    "dune-sci-fi-epics-guide": "recommendations",
    "alien-franchise-in-order": "recommendations",
    "squid-game-season-1-why-it-became-a-global-phenomenon": "explainers",
    "was-eren-yeager-really-the-villain": "explainers",
    "solo-leveling-e-rank-to-s-rank": "explainers",
    "alice-in-borderland-vs-squid-game": "explainers",
    "one-piece-vs-naruto": "explainers",
    "solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences": "explainers",
    "breaking-bad-two-seasons-opinion": "opinion",
    "5-movies-that-broke-the-internet": "opinion",
    "7-movies-we-wished-never-ended": "opinion",
    "into-the-badlands-was-underrated": "opinion",
    "why-prison-break-season-1-is-still-one-of-the-best-tv-seasons": "opinion",
}
# consolidation: the second slug is folded into the first as a labelled companion piece
ENT_MERGE = {
    "solo-leveling-e-rank-to-s-rank": "solo-leveling-from-e-rank-hunter-to-one-of-animes-most-powerful-characters",
    "why-prison-break-season-1-is-still-one-of-the-best-tv-seasons": "prison-break-season-1-watching-all-night",
    "movies-like-interstellar-guide": "interstellar-ending-explained",
    "modern-horror-starter-route": "5-vampire-movies-that-changed-horror",
    "dune-sci-fi-epics-guide": "why-dune-part-two-feels-large",
}
ENT_START = ["how-to-pick-a-movie-tonight", "how-to-build-a-watchlist", "christopher-nolan-movies-order",
             "best-streaming-apps-nigeria", "korean-cinema-starter-guide-rebuilt"]

def _first_line(body_html, fallback=""):
    m = re.search(r"<p[^>]*>([\s\S]*?)</p>", body_html)
    if not m:
        return fallback
    txt = _strip_tags(m.group(1))
    txt = html.unescape(re.sub(r"\s+", " ", txt)).strip()
    return (txt[:157] + "\u2026") if len(txt) > 160 else txt

def _strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)

def entertainment_pages():
    rec = OUT / "entertainment" / "_recovered"
    manifest = json.loads((rec / "manifest.json").read_text())
    by_slug = {m["slug"]: m for m in manifest}
    # the moved piece joins the manifest with its own record
    by_slug["best-streaming-apps-nigeria"] = {
        "slug": "best-streaming-apps-nigeria",
        "title": "Best Streaming Apps in Nigeria (2026), Honestly Compared",
        "words": 900, "moved": True}
    # evergreen guides: original pieces, no archive provenance
    import entertainment_guides_data
    guide_bodies = {}
    for slug, sect, title, dek, body in entertainment_guides_data.ENT_GUIDES:
        ENT_SLUG_SECT[slug] = sect
        by_slug[slug] = {"slug": slug, "title": title, "words": len(re.sub(r"<[^>]+>", " ", body).split()),
                         "new": True}
        guide_bodies[slug] = body
    shelf = sorted(ENT_SLUG_SECT)
    merged_away = set(ENT_MERGE.values())
    bodies = {}
    for slug in shelf + sorted(merged_away):
        if slug in guide_bodies:
            bodies[slug] = guide_bodies[slug]
        else:
            raw = (rec / f"{slug}.html").read_text()
            bodies[slug] = clean_recovered(raw)
    arts = {}
    for slug in shelf:
        if slug in merged_away:
            continue
        m = by_slug[slug]
        sect = ENT_SLUG_SECT[slug]
        moved = m.get("moved")
        if m.get("new"):
            kick = "Evergreen guide \u00b7 "
        elif moved:
            kick = "Moved from the BRYME tech desk \u00b7 "
        else:
            kick = "Archive edition (2025) \u00b7 "
        comp_html = ""
        if slug in ENT_MERGE:
            other = ENT_MERGE[slug]
            comp_html = ('<h2>Companion piece, restored: ' + html.escape(by_slug[other]["title"]) + "</h2>"
                         + "<p><em>Merged from the archive so the whole argument lives on one page.</em></p>"
                         + bodies[other])
        summ = _first_line(bodies[slug])
        rel_pool = [s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == sect and s2 != slug]
        rel = rel_pool[:3]
        while len(rel) < 3:
            for s2 in shelf:
                if s2 not in merged_away and s2 != slug and s2 not in rel:
                    rel.append(s2)
                    break
            if len(rel) >= 3:
                break
        rel_html = "".join('<li><a href="/' + s2 + '/">' + html.escape(by_slug[s2]["title"]) + "</a></li>" for s2 in rel)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": m["title"],
                  "author": {"@type": "Organization", "name": "BRYME Entertainment desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/entertainment/" + slug + "/",
                  "description": summ}
        import json as _j
        byline = ("Written by the BRYME Entertainment desk \u00b7 reviewed " + TODAY
                  + " \u00b7 evergreen \u2014 re-checked whenever the facts move") if m.get("new") else (
                  "Recovered from the archive \u00b7 " + str(m["words"]) + " words \u00b7 re-typeset and reviewed "
                  + TODAY + (" \u00b7 prices in older pieces change \u2014 confirm with the service" if slug == "best-streaming-apps-nigeria" else ""))
        abody = (head("entertainment", "Cinema, TV and anime \u2014 written about, never pirated.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/entertainment/">Entertainment</a> / <a href="/entertainment/' + sect + '/">'
            + html.escape(ENT_SECTIONS[sect][0]) + "</a> / " + html.escape(m["title"]) + "</nav>"
            + '<section class="cover"><p class="kicker">' + kick + "no piracy, no scrapes \u2014 written about the work</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(m["title"]) + "</h1>"
            + '<p class="byline">BRYME Entertainment desk \u00b7 ' + html.escape(byline) + "</p></section>"
            + ('<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(summ) + "</p></div></section>" if summ else "")
            + '<section class="section"><div class="prose">' + bodies[slug] + comp_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from ' + html.escape(ENT_SECTIONS[sect][0]) + '.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/entertainment/' + sect + '/">All of ' + html.escape(ENT_SECTIONS[sect][0]) + '</a>'
            + '<a class="btn secondary" href="/entertainment/">All of BRYME Entertainment</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("entertainment"))
        arts[slug] = (("/" + slug + "/"), m["title"] + " | BRYME Entertainment", summ or "From the BRYME archive \u2014 re-typeset and honestly labelled.", abody)

    sect_pages = {}
    for cslug, (cname, cdesc) in ENT_SECTIONS.items():
        lst = [s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == cslug]
        lst.sort(key=lambda s2: -by_slug[s2]["words"])
        rows = "".join(
            '<li><a href="/' + s2 + '/"><span><b>' + html.escape(by_slug[s2]["title"]) + "</b><small>"
            + html.escape(_first_line(bodies[s2])[:110]) + "\u2026</small></span>"
            '<span class="meta">' + str(by_slug[s2]["words"]) + " words</span></a></li>" for s2 in lst)
        others = "".join('<a class="btn secondary" href="/entertainment/' + c2 + '/">' + html.escape(ENT_SECTIONS[c2][0]) + "</a>"
                         for c2 in ENT_SECTIONS if c2 != cslug)
        cbody = (head("entertainment", "Cinema, TV and anime \u2014 written about, never pirated.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/entertainment/">Entertainment</a> / ' + html.escape(cname) + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Entertainment \u00b7 section</p>'
            + '<h1 class="cover-title">' + html.escape(cname) + "</h1>"
            + '<p class="cover-dek">' + html.escape(cdesc) + "</p></section>"
            + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(lst)) + ' pieces</p><h2>Everything in ' + html.escape(cname) + '.</h2></div>'
            + '<ul class="list">' + rows + "</ul></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Keep watching</p><h2>Elsewhere on this desk.</h2></div>'
            + '<div class="actions">' + others + "</div></section></div></main>" + foot("entertainment"))
        sect_pages[cslug] = [("/" + cslug + "/", cname + " | BRYME Entertainment", cdesc, cbody)]

    start_rows = "".join(
        '<li><a href="/' + s2 + '/"><span><b>' + html.escape(by_slug[s2]["title"]) + "</b><small>"
        + html.escape(_first_line(bodies[s2])[:110]) + "\u2026</small></span><span class=\"meta\">Start here</span></a></li>"
        for s2 in ENT_START)
    cat_cards = "".join(
        '<article class="pub-card live" style="--pc:#6d1832"><p class="pc-kicker">' + str(len([s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == c])) + ' PIECES</p>'
        + "<h3>" + html.escape(ENT_SECTIONS[c][0]) + "</h3><p>" + html.escape(ENT_SECTIONS[c][1][:130]) + "\u2026</p>"
        + '<a class="btn" href="/entertainment/' + c + '/">Browse ' + html.escape(ENT_SECTIONS[c][0]) + " \u2192</a></article>"
        for c in ENT_SECTIONS)
    retired_rows = "".join(
        '<li><span><b>' + html.escape(m["title"]) + "</b><small>" + str(m["words"]) + " words \u00b7 reviewed by the audit \u2014 retired on merit</small></span>"
        '<span class="meta">Retired</span></li>'
        for m in manifest if m["slug"] not in ENT_SLUG_SECT and m["slug"] not in set(ENT_MERGE.values())
        and m["slug"] not in {"korean-cinema-starter-guide", "movies-like-interstellar"})
    index_body = (head("entertainment", "Cinema, TV and anime \u2014 written about, never pirated.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Entertainment</p>'
        + '<h1 class="cover-title">What should I watch \u2014 and why?</h1>'
        + '<p class="cover-dek">Recommendations with reasons, explainers without spoilers-for-sport, and opinion labelled as opinion. Everything here is written about the work: no download pages, no fake play buttons, no piracy \u2014 ever.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Handpicked</p><h2>Start here.</h2></div>'
        + '<ul class="list">' + start_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Browse by need</p><h2>Sections of this desk.</h2></div>'
        + '<div class="cards">' + cat_cards + "</div></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The house rule</p><h2>Written about the work, never trafficking in it.</h2></div>'
        + '<p class="lede">BRYME Entertainment does not stream, host, link or hint at pirated copies. External trailers may support a piece; the value on the page is the argument. Restored editions say so plainly, carry their word counts, and were re-typeset \u2014 not quietly re-scraped.</p>'
        + '<ul class="list" style="margin-top:14px">' + retired_rows + "</ul>"
        + "</section></div></main>" + foot("entertainment"))
    pages = [("/", "BRYME Entertainment \u2014 what to watch, and why",
              "Film, TV and anime recommendations with reasons, explainers and opinion \u2014 written about the work, never piracy.", index_body)]
    for pl in sect_pages.values():
        pages.extend(pl)
    pages.extend(arts[s] for s in shelf if s not in merged_away)
    return pages + legal_pages("entertainment", "BRYME Entertainment", "Writing about film, TV and anime for people who love the work.")



# ------------------------------------------------------------- 3. SPORTS
def sports_pages():
    rec = Path(OUT / "sports" / "_recovered")
    manifest = json.loads((rec / "manifest.json").read_text())
    REAL = {"premier-league-transfer-tracker-august-2026", "premier-league-matchweek-2-preview",
            "elliot-anderson-man-city-record-signing", "deadline-day-dont-try-to-make-sense-of-it",
            "premier-league-matchweek-1-guide"}
    by = {m["slug"]: m for m in manifest}
    restored, retired = [], []
    pages = []
    for slug in sorted(REAL):
        m = by.get(slug)
        if not m:
            continue
        body_file = rec / f"{slug}.body.html"
        if not body_file.exists():
            continue
        body_html = clean_recovered(body_file.read_text())
        route = f"/{slug}/"
        archive = slug in {"premier-league-transfer-tracker-august-2026",
                           "premier-league-matchweek-1-guide", "premier-league-matchweek-2-preview",
                           "deadline-day-dont-try-to-make-sense-of-it"}
        kick = ("Season 2026-27 \u00b7 archive edition" if archive else "The desk \u00b7 2026-27 season")
        arch_note = (" \u00b7 written during the live season window and kept as archive \u2014 "
                     "new editions return with the season" if archive else "")
        restored.append(f'<li><a href="{route}"><span><b>{html.escape(m["title"])}</b>'
                        f'<small>From the media desk · {m["words"]} words · {TODAY}</small></span>'
                        f'<span class="meta">Read</span></a></li>')
        pbody = f"""{head("sports", "Analysis, stories and the long view \u2014 never betting.")}
<main id="main"><div class="wrap">
<nav class="crumb"><a href="/">Home</a> / {html.escape(m["title"])}</nav>
<section class="cover"><p class="kicker">{kick}</p>
<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">{html.escape(m["title"])}</h1>
<p class="byline">From the BRYME media desk · recovered edition, re-typeset {TODAY}{arch_note}</p></section>
<section class="section"><div class="prose">{body_html}</div></section>
</div></main>{foot("sports")}"""
        pages.append((route, f'{m["title"]} | BRYME Sport',
                      "From the BRYME media desk — recovered edition, re-typeset.", pbody))

    # evergreen explainers: laws, formats and roles — no fixtures, no data rights, no betting
    import sports_explainers_data
    import json as _j
    expl_rows = []
    for slug, title, dek, body, sources, related in sports_explainers_data.SPORT_EXPLAINERS:
        src_html = ""
        if sources:
            src_html = ('<h2>Sources</h2><ul class="list">'
                        + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                        + "</ul>")
        rel_html = "".join('<li><a href="/' + s + '/">' + rt + "</a></li>" for s, rt in related)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": title,
                  "author": {"@type": "Organization", "name": "BRYME Sport desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/sports/" + slug + "/",
                  "description": dek}
        ebody = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/sports/explainers/">Explainers</a> / ' + title + "</nav>"
            + '<section class="cover"><p class="kicker">Explainer \u00b7 evergreen</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + title + "</h1>"
            + '<p class="byline">BRYME Sport desk \u00b7 reviewed ' + TODAY + " \u00b7 evergreen explainer \u2014 no odds, no tips, no invented facts</p></section>"
            + '<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + dek + "</p></div></section>"
            + '<section class="section"><div class="prose">' + body + src_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from the shelf.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/sports/explainers/">All explainers</a>'
            + '<a class="btn secondary" href="/sports/">All of BRYME Sport</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("sports"))
        pages.append(("/" + slug + "/", title + " | BRYME Sport", dek[:155], ebody))
        expl_rows.append('<li><a href="/' + slug + '/"><span><b>' + title + "</b><small>" + dek[:110] + "\u2026</small></span>"
                         '<span class="meta">Explainer</span></a></li>')

    # the analysis shelf: how the game is played (batch 3)
    import sports_analysis_data
    analysis_rows = []
    for slug, title, dek, body, sources, related in sports_analysis_data.SPORT_ANALYSIS:
        src_html = ""
        if sources:
            src_html = ('<h2>Sources</h2><ul class="list">'
                        + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                        + "</ul>")
        rel_html = "".join('<li><a href="/' + s + '/">' + rt + "</a></li>" for s, rt in related)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": title,
                  "author": {"@type": "Organization", "name": "BRYME Sport desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/sports/" + slug + "/",
                  "description": dek}
        abody = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/analysis/">Analysis</a> / ' + title + "</nav>"
            + '<section class="cover"><p class="kicker">Analysis \u00b7 evergreen</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + title + "</h1>"
            + '<p class="byline">BRYME Sport desk \u00b7 reviewed ' + TODAY + " \u00b7 evergreen analysis \u2014 no odds, no tips, no invented facts</p></section>"
            + '<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + dek + "</p></div></section>"
            + '<section class="section"><div class="prose">' + body + src_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from the shelf.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/analysis/">All analysis</a>'
            + '<a class="btn secondary" href="/sports/">All of BRYME Sport</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("sports"))
        pages.append(("/" + slug + "/", title + " | BRYME Sport", dek[:155], abody))
        analysis_rows.append('<li><a href="/' + slug + '/"><span><b>' + title + "</b><small>" + dek[:110] + "\u2026</small></span>"
                         '<span class="meta">Analysis</span></a></li>')

    # the analysis shelf hub
    analysis_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The analysis shelf</nav>'
        + '<section class="cover"><p class="kicker">The analysis shelf \u00b7 how the game is played</p>'
        + '<h1 class="cover-title">Read the game, not the noise.</h1>'
        + '<p class="cover-dek">The ideas behind the tactics \u2014 expected goals, pressing, possession, the short build-up and the trap \u2014 explained plainly and argued honestly. Concepts only, evergreen: no odds, no tips, no invented numbers.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(sports_analysis_data.SPORT_ANALYSIS)) + ' pieces</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + "".join(analysis_rows) + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">The honest bit</p><h2>How this desk uses numbers.</h2></div>'
        + '<div class="prose"><p>Analysis pieces explain concepts; where a number has a model behind it, the piece says what the model measures and what it misses. No betting angles, ever &mdash; understanding the game is the product, not tipping it.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/analysis/", "The analysis shelf \u2014 how the game is played | BRYME Sport",
                  "xG, pressing, possession, the short build-up and the offside trap \u2014 the ideas behind modern football, explained honestly and evergreen.", analysis_hub))

    # the transfer desk: one hub for the window's editions and mechanics
    transfers_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The transfer desk</nav>'
        + '<section class="cover"><p class="kicker">The transfer desk \u00b7 the window, in one place</p>'
        + '<h1 class="cover-title">Transfers, covered honestly.</h1>'
        + '<p class="cover-dek">No rumour mill, no betting angles: the desk covers transfers as journalism &mdash; how deals actually happen, who makes them happen, and a tracker of what this desk could verify while the window was open. Live window coverage returns as a fresh edition every window.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The archive editions</p><h2>The 2026 summer window, as we covered it.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/premier-league-transfer-tracker-august-2026/"><span><b>The August 2026 transfer tracker</b><small>Archive edition &mdash; the window as it happened, kept with its date on its sleeve.</small></span><span class="meta">Archive</span></a></li>'
        + '<li><a href="/deadline-day-dont-try-to-make-sense-of-it/"><span><b>Deadline day: don\u2019t try to make sense of it</b><small>A field guide to the window\u2019s strangest evening.</small></span><span class="meta">Archive</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">The mechanics</p><h2>How deals actually happen.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/why-football-transfers-collapse/"><span><b>Why transfers collapse</b><small>Fee, terms, medical, paperwork &mdash; four doors, and the window\u2019s favourite tragedies live in the gaps.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/what-does-a-sporting-director-do/"><span><b>What does a sporting director actually do?</b><small>The role that builds the machine behind every deal.</small></span><span class="meta">Explainer</span></a></li>'
        + '</ul></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The calendar</p><h2>When the next window opens.</h2></div>'
        + '<div class="prose"><p>In England the summer window typically closes on the evening of 1 September, and a winter window runs through January; other leagues set their own dates within FIFA\u2019s framework, confirmed window by window. When the next one opens, the tracker returns as a new dated edition &mdash; until then, the archive stands exactly as it was written.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/transfers/", "The transfer desk \u2014 window coverage, honestly | BRYME Sport",
                  "Transfer coverage without the rumour mill: archive window editions, how deals actually happen, and when live coverage returns.", transfers_hub))

    # the Champions League shelf
    ucl_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The Champions League shelf</nav>'
        + '<section class="cover"><p class="kicker">The Champions League shelf \u00b7 understand the competition</p>'
        + '<h1 class="cover-title">Europe\u2019s big cup, explained.</h1>'
        + '<p class="cover-dek">The new 36-team format has been confusing people since 2024 &mdash; these explainers walk the whole journey from qualification to the final. Match-by-match coverage returns with the season as verified editions; this desk does not run a live-scores product.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The shelf</p><h2>Start here.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/how-the-champions-league-works/"><span><b>How the Champions League works</b><small>Who gets in, the eight-game league phase, the playoffs, one final on one night.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/champions-league-new-format-explained/"><span><b>The new format: what actually changed</b><small>Old groups vs the 36-team league &mdash; and the honest case each side makes.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/why-does-afcon-move-around/"><span><b>Why AFCON moves around the calendar</b><small>The other championship whose dates collide with Europe\u2019s &mdash; climate, calendars, television.</small></span><span class="meta">Explainer</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">The honest bit</p><h2>What this shelf will not do.</h2></div>'
        + '<div class="prose"><p>It will not invent results, quote odds, or pretend to track live scores. During the season the desk publishes verified editions on the stories that matter; between them, the explainers keep the competition understandable. Sources: UEFA\u2019s official competition pages.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/champions-league/", "The Champions League shelf \u2014 the format, explained | BRYME Sport",
                  "How the Champions League works and what the new 36-team format changed \u2014 evergreen explainers, verified editions in season.", ucl_hub))

    # the /explainers/ section page
    all_rows = "".join('<li><a href="/' + s + '/"><span><b>' + ti + "</b><small>" + dek[:130] + "\u2026</small></span>"
                       '<span class="meta">Explainer</span></a></li>'
                       for s, ti, dek, b, so, re in sports_explainers_data.SPORT_EXPLAINERS)
    sect_body = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / Explainers</nav>'
        + '<section class="cover"><p class="kicker">BRYME Sport \u00b7 the explainer shelf</p>'
        + '<h1 class="cover-title">Understand the game.</h1>'
        + '<p class="cover-dek">The laws, the formats and the roles of football \u2014 explained plainly, argued honestly, and evergreen: nothing here expires with the fixtures. No betting content, ever.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(sports_explainers_data.SPORT_EXPLAINERS)) + ' explainers</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + all_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Also on this desk</p><h2>The season archive.</h2></div>'
        + '<div class="actions"><a class="btn secondary" href="/analysis/">The analysis shelf</a><a class="btn secondary" href="/sports/">Back to BRYME Sport</a></div></section>'
        + "</div></main>" + foot("sports"))
    pages.insert(1, ("/explainers/", "Football explainers \u2014 laws, formats and roles | BRYME Sport",
                     "The offside rule, VAR, promotion and relegation, transfer mechanics, sporting directors and AFCON's calendar \u2014 football explained plainly, evergreen.", sect_body))

    for m in manifest:
        if m["slug"] not in REAL:
            retired.append(f'<li><span><b>{html.escape(m["title"])}</b>'
                           f'<small>{m["words"]} words · reviewed \u2014 retired: teaser stub, not an article</small></span>'
                           f'<span class="meta">Retired</span></li>')
    index_body = f"""{head("sports", "Analysis, stories and the long view \u2014 never betting.")}
<main id="main"><div class="wrap">
<section class="cover"><p class="kicker">BRYME Sport · the 2026-27 desk</p>
<h1 class="cover-title">Sport as reporting, not noise.</h1>
<p class="cover-dek">Football first: the transfer window read plainly, the matchweeks reviewed, the season's stories followed as they happen. Restored from the BRYME media desk \u2014 and, as a house rule, never betting odds or gambling-adjacent tips.</p></section>
<section class="section"><div class="section-head"><p class="kicker">Evergreen explainers</p><h2>Understand the game.</h2></div>
<ul class="list">{''.join(expl_rows)}</ul></section>
<section class="section"><div class="section-head"><p class="kicker">The shelves</p><h2>Analysis, the transfer desk &amp; the Champions League.</h2></div>
<ul class="list">
<li><a href="/analysis/"><span><b>The analysis shelf</b><small>How the game is actually played &mdash; xG, pressing, possession, the build-up and the trap.</small></span><span class="meta">Shelf</span></a></li>
<li><a href="/transfers/"><span><b>The transfer desk</b><small>The window in one place &mdash; archive editions, deal mechanics, and when live coverage returns.</small></span><span class="meta">Desk</span></a></li>
<li><a href="/champions-league/"><span><b>The Champions League shelf</b><small>The 36-team format, explained honestly &mdash; with match coverage returning in season.</small></span><span class="meta">Shelf</span></a></li>
</ul></section>
<section class="section"><div class="section-head"><p class="kicker">The restored desk</p><h2>Recovered editions</h2></div>
<ul class="list">{''.join(restored)}</ul></section>
<section class="section alt"><div class="section-head"><p class="kicker">The honest bit</p><h2>What stayed retired.</h2></div>
<ul class="list">{''.join(retired)}</ul>
<p class="lede">The archive also held roughly two thousand match-data pages from finished fixtures. They are data, not journalism; they stay retired rather than being republished stale. New reporting accumulates here as the season runs.</p>
</section></div></main>{foot("sports")}"""
    pages.insert(0, ("/", "BRYME Sport \u2014 football reporting, never betting",
              "Transfer reporting, matchweek guides and season stories from the BRYME media desk. Independent, checkable, strictly no gambling content.", index_body))
    return pages + legal_pages("sports", "BRYME Sport", "Analysis, stories and the long view of sport \u2014 checkable, and never betting.")


# ---------------------------------------------------------------- 4. MONEY

TECH_ARTICLES = [
 ("render-static-deploy", "How to deploy a static site on Render — from a site that did it",
  "Push-to-deploy, the publish directory, spooling deploys and the free-tier cold start: the whole path, written by someone whose production site runs on exactly this.",
  """<p>This site you are reading runs on Render's free static hosting, and so does its 500-page sibling. Everything below is first-hand, not documentation paraphrase.</p>
<h2>The three decisions that matter</h2>
<p><strong>1. Build command vs publish directory.</strong> Render runs your build command, then serves whatever directory you name as the publish directory. Ours is <code>npm run build</code> publishing <code>public/</code>. The classic mistake is testing locally, deploying, and looking at a stale page — because the publish directory points at the source folder instead of the build output. Point it at generated output, always.</p>
<p><strong>2. The build can fail and the site still serves.</strong> A static host serves the last good deploy. That is resilience, but it hides breakage: your build can be red for days while the site looks fine. Wire a status notification (Render's dashboard hooks or a simple build-badge check) — trust the build log, not the homepage.</p>
<p><strong>3. Redirects live with the host.</strong> A <code>_redirects</code> file works on some hosts and is ignored on others; Render static sites use a redirects file format of their own (<code>_redirects</code> in the publish directory), and dashboard-level redirect rules shadow everything. When a path "mysteriously" serves the wrong page, check the dashboard rules first.</p>
<h2>The free tier, honestly</h2>
<p>Free static hosting on Render does not sleep — static sites are served from CDN edges, so there is no cold start (that applies to free <em>web services</em>, a different product). The real limits are build minutes and bandwidth. For a text-first site with system fonts and no framework, both are a rounding error: this deployment serves hundreds of thousands of internal links across ~500 pages on the free tier.</p>
<h2>The checklist</h2>
<ul>
<li>Build command tested locally, byte-identical output.</li>
<li>Publish directory = generated output only.</li>
<li>Custom redirects declared once, in the file the host actually reads.</li>
<li>After the first deploy: curl every critical URL. Never sample — verify.</li>
</ul>"""),
 ("custom-domain-dns-order", "Custom domains: the DNS order that avoids downtime",
  "Apex, www, CNAME flattening and verification order — the sequence that works, learned while moving a live site.",
  """<p>Moving a site to a custom domain is simple in principle and annoying in practice because the steps have an order, and doing them out of order produces hours of "why is this still showing the old site".</p>
<h2>The order</h2>
<p><strong>1. Buy the domain at a registrar with honest pricing</strong> (at-cost resellers like Cloudflare or Porkbun), and keep DNS hosted there. Free WHOIS privacy comes standard now; pay for it nowhere.</p>
<p><strong>2. Add the domain in your host's dashboard first.</strong> Render (and most hosts) gives you the exact DNS records to create — an apex record and a www record. Adding the domain before the records exist means verification completes the moment DNS propagates.</p>
<p><strong>3. Create the records exactly as given.</strong> Apex domains usually get ALIAS/ANAME or A records; www gets a CNAME. If your registrar supports CNAME flattening at the apex, flattening to the host's target is the clean path.</p>
<p><strong>4. Change the site's canonical URLs in config, not in pages.</strong> Every canonical link, sitemap entry and Open Graph URL should come from one configuration value. Ours is a single <code>SITE_URL</code> in one config file feeding every builder; grep your codebase for the old hostname and the only hit should be the changelog.</p>
<p><strong>5. Verify with the registry, not your browser.</strong> Browser caches lie about DNS for hours. Check with <code>dig</code>/<code>nslookup</code>, and confirm the old domain 301s to the new one at the host level.</p>
<h2>The mistake that costs a week</h2>
<p>Hard-coding the staging hostname into canonicals, then migrating. Search engines index what your canonicals say; if every page declares the staging URL canonical, the new domain can sit unindexed for weeks. Centralise the hostname before you migrate — the five minutes of config refactor is the whole game.</p>"""),
 ("github-token-hygiene", "Personal access tokens: using them without leaking them",
  "Least-scope tokens, where they can and cannot appear, and the rotation habit — written after months of daily build use.",
  """<p>A GitHub personal access token in a build pipeline is a standing temptation to do the lazy thing: paste it into a script, commit, move on. Don't. Here is the discipline that works day-to-day.</p>
<h2>Scope it to the minimum</h2>
<p>A token that only pushes to one repository needs exactly one scope: contents read/write on that repo. Fine-grained tokens (now the default in GitHub's settings) let you select the single repository and the single permission. If your token's description says "for everything", it is wrong.</p>
<h2>Where a token may appear</h2>
<ul>
<li><strong>CI secrets / environment variables:</strong> yes. Render, Actions, and friends inject them at build time.</li>
<li><strong>A chat message to your own agent or notes:</strong> tolerable only if you plan rotation — and "planning" means a date on the calendar, not intentions.</li>
<li><strong>A committed file, a URL, a screenshot:</strong> never. Committed tokens live forever in history; GitHub's secret scanning will revoke some automatically, and attackers find the rest first.</li>
</ul>
<h2>The rotation habit</h2>
<p>Rotate on a schedule you would be embarrassed to break: 90 days for personal tokens is a good default, immediately after any suspected exposure, and whenever a collaborator leaves. Rotation costs five minutes if your pipeline reads the token from one secret; it costs an evening if the token is pasted in six places.</p>
<h2>The tell you're doing it right</h2>
<p>Grep your repository for the token prefix right now (<code>ghp_</code> for classic tokens). The correct number of results is zero — including in history, which you can check with <code>git log -S ghp_</code>. If history is dirty and the repo is public, the token is burned: revoke first, refactor second.</p>"""),
 ("csp-safe-front-end", "A front end that survives redesigns: CSP-safe patterns that work",
  "No jQuery, no inline scripts, no build step — the four patterns behind a 500-page site's entire JavaScript layer.",
  """<p>The pages on this site's family run on a few kilobytes of hand-written ES5. No framework, no bundler, no jQuery — and, because the sites ship a Content-Security-Policy, no inline scripts anywhere. These are the patterns that make that livable.</p>
<h2>1. One entry point per page, found by attribute</h2>
<p>Every page that needs behaviour carries a <code>&lt;script src=... data-tool="name"&gt;</code> tag. The shared script file reads <code>document.currentScript.dataset.tool</code> at load time and dispatches to that module. It is dependency-free page-to-script wiring that survives any redesign of the HTML around it.</p>
<h2>2. IDs are the contract</h2>
<p>Scripts address the DOM by element ID and data attributes, never by styling classes. Styling classes belong to CSS and change constantly; IDs are semantics and change rarely. When a redesign came through recently, the entire JavaScript audit was "grep for getElementById" — every hook held.</p>
<h2>3. Progressive enhancement, for real</h2>
<p>Filters, editors and calculators here all render their no-JS state first and enhance if the script loads. The test: disable JavaScript and the page must still be a complete, readable document. This is also the cheapest accessibility audit there is.</p>
<h2>4. localStorage with a versioned envelope</h2>
<p>Anything a user creates in the browser (drafts, trackers, tool state) is stored as <code>{"v":1,...}</code>. When the shape changes, bump the version and migrate on read. The day accounts arrive, local data upgrades instead of breaking.</p>
<p>The reward for all this discipline is boring: pages that load fast on hotel Wi-Fi, zero console errors, and redesigns that touch CSS files rather than JavaScript.</p>"""),
 ("sitemap-indexnow", "Sitemaps and IndexNow: telling search engines the honest way",
  "What to ping, when to ping it, and why sampled verification is how broken launches happen.",
  """<p>Every launch conversation eventually asks: do we need to "submit" the site anywhere? The honest answer for most of the job is no — but the parts that are yes, people get wrong constantly.</p>
<h2>The sitemap is a claim, so keep it true</h2>
<p>A sitemap asserts "these are the canonical, indexable URLs." Every assertion that isn't true is a small editorial lie to the crawler: staged-but-unbuilt routes, parameterised duplicates, pages your robots file blocks. Generate the sitemap from the same source of truth as your build, and add an assertion to the build that fails when a sitemap route lacks a built page. Ours fails the build on any mismatch; it has caught three launch mistakes that sampled checking would have missed.</p>
<h2>IndexNow: for changes, not for begging</h2>
<p>IndexNow lets you notify participating engines when URLs are created or materially change. The protocol is a keyed GET/POST with the changed URLs — not a substitute for sitemaps, and not something to hammer on a schedule. Our practice: ping after every meaningful deploy, listing exactly the new and changed URLs, and keep a JSONL log of what was announced when. The log settles every "did we tell them?" argument.</p>
<h2>Search Console is the feedback loop</h2>
<p>Verification via a DNS record takes minutes. The property then tells you what the crawlers actually did with your claims: indexed, ignored, or blocked. Read it monthly, export the queries, and let real impressions — not vanity traffic — pick what gets expanded next.</p>
<h2>What never to do</h2>
<p>Never ping URLs that return 404, never submit a sitemap whose URLs contradict your canonicals, and never generate pages to fill a sitemap. The systems are designed by people who have seen every trick; the only sustainable strategy is to have the site actually be as described.</p>"""),
]

TECH_CAT = {
    "ai": ("AI, without the hype", "What the assistants actually do, what the free tiers really include, and where your conversations go \u2014 checked against the real products, not the press releases.", "hero-assistants.jpg"),
    "tools": ("Free tools & real alternatives", "Free plans and alternatives we actually opened and used \u2014 what they include, what they hold back, and who each one fits.", "hero-alternatives.jpg"),
    "subscriptions": ("Subscriptions & clutter", "Recurring charges, free trials and the audit \u2014 keeping what you pay for fewer, cheaper and actually used.", ""),
    "streaming": ("Streaming & cord-cutting", "Quality settings, bandwidth reality and the honest math of replacing cable \u2014 what your stream costs and why it looks the way it does.", ""),
    "web-and-hosting": ("Web & hosting", "Domains, DNS, deploys and the front end \u2014 written from first-hand builds of this very site, failures included.", "hero-hosting.jpg"),
    "safety": ("Safety & privacy", "Passwords, messaging, tokens and your data \u2014 practical protection without the scaremongering.", "hero-privacy.jpg"),
    "smart-home": ("Smart home", "Devices worth owning, speakers that listen, and the Wi-Fi that quietly decides whether any of it works \u2014 setup honesty, not showroom promises.", ""),
    "android": ("Android & mobile", "Phone storage, permissions, battery and notifications \u2014 the settings that actually matter, explained without the jargon.", ""),
    "windows": ("Windows & PC", "Slow computers, browser trouble and update problems \u2014 triaged in the order that finds the cause fastest.", ""),
    "coding": ("Coding", "Beginner programming explained the honest way \u2014 errors, Git and APIs \u2014 from a desk that ships code.", ""),
    "quant": ("Quantitative computing", "The QuantLab project: a one-person research lab in Python, and what ~140 documented experiments taught \u2014 failures included. Educational research, never investment advice.", ""),
    "buying": ("Buying guides", "Specs vs marketing, refurbished vs new \u2014 the numbers that decide whether tech is still pleasant in year three.", ""),
}
_TECH_CAT_OF = {
    "hosting": "web-and-hosting", "ai-assistants": "ai", "beginner-coding": "coding",
    "app-alternatives": "tools", "useful-websites": "tools", "cybersecurity": "safety",
    "android-apps": "safety", "productivity": "tools",
}
_TECH_CUR_CAT = {
    "csp-safe-front-end": "web-and-hosting", "custom-domain-dns-order": "web-and-hosting",
    "render-static-deploy": "web-and-hosting", "sitemap-indexnow": "web-and-hosting",
    "github-token-hygiene": "safety",
}

def _norm_tech(rec):
    return {
        "slug": rec["slug"], "title": rec["title"], "excerpt": rec.get("excerpt", ""),
        "cat": _TECH_CAT_OF.get(rec.get("categorySlug", ""), "coding"),
        "pub": (rec.get("publishedAt") or "")[:10], "upd": (rec.get("updatedAt") or "")[:10],
        "read": rec.get("readingTime", ""), "author": rec.get("author", "BRYME Tech desk"),
        "blocks": rec.get("content", []), "sources": rec.get("sources", []), "recovered": True,
    }

def _load_tech():
    arts = [_norm_tech(r) for r in json.loads(
        (OUT.parent / "content" / "tech-articles.json").read_text(encoding="utf-8"))]
    by_slug = {a["slug"]: a for a in arts}
    for slug, title, blurb, body in TECH_ARTICLES:
        if slug in by_slug:
            continue
        arts.append({"slug": slug, "title": title, "excerpt": blurb,
                     "cat": _TECH_CUR_CAT.get(slug, "coding"), "pub": TODAY, "upd": TODAY,
                     "read": "", "author": "the BRYME Tech desk",
                     "blocks": [{"heading": "", "body": body, "html": True}],
                     "sources": [], "recovered": False})
    import tech_guides_data
    for slug, cat, kind, title, dek, body, sources, related in tech_guides_data.NEW_TECH_GUIDES:
        arts.append({"slug": slug, "title": title, "excerpt": dek, "cat": cat, "kind": kind,
                     "pub": TODAY, "upd": TODAY, "read": "", "author": "the BRYME Tech desk",
                     "blocks": [{"heading": "", "body": body, "html": True}],
                     "sources": [{"name": n, "url": u} for n, u in sources],
                     "recovered": False})
    return arts

def _tech_blocks(a):
    out = []
    for b in a["blocks"]:
        h = html.escape(b.get("heading") or "")
        if h:
            out.append("<h2>" + h + "</h2>")
        body = b.get("body") or ""
        if b.get("html"):
            out.append(body)
        else:
            out.append("".join("<p>" + html.escape(pp).replace("\n", " ") + "</p>"
                               for pp in body.split("\n\n") if pp.strip()))
    return "".join(out)

def _tech_related(a, arts, n=3):
    same = [x for x in arts if x["cat"] == a["cat"] and x["slug"] != a["slug"]]
    pool = ["where-to-host-website-for-free", "bitwarden-free-password-manager",
            "learning-to-code-on-a-phone-termux", "custom-domain-dns-order"]
    extra = [by for by in arts if by["slug"] in pool and by["slug"] != a["slug"] and by not in same]
    return (same + extra)[:n]

def tech_trust_pages():
    """Trust pages (master build M1): methodology, corrections, terms, disclaimer."""
    methodology_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Methodology</nav>
<section class="cover"><p class="kicker">How we work</p><h1 class="cover-title">How BRYME Tech researches what it publishes.</h1>
<p class="cover-dek">Every guide on this desk is written under one discipline: verify it live, name the source, date the volatile parts &mdash; or don't claim it at all.</p></section>
<section class="section"><div class="prose">
<h2>Two labels, and what they promise</h2>
<p><strong>BRYME Technical Guide</strong> is general technical reference: researched from official documentation and primary sources, written for the practical question in the title. <strong>First-Hand Project Report</strong> is different in kind: the piece comes from a project we actually ran &mdash; this publication's own deployment stack (Render, DNS, token hygiene, CSP patterns) and the <a href="/tech/quantlab-project-how-built/">QuantLab research project</a> are the current examples. First-hand means we ran the thing on our own accounts and hardware; where a piece is first-hand, the label says so, and where it isn't, we don't pretend.</p>
<h2>Where claims come from</h2>
<p>External facts come from primary sources: official documentation, official product and pricing pages, standards bodies, regulators. Numbers get a named source and a date in the text. Where third-party aggregators disagree &mdash; common with pricing and stats &mdash; we publish the named-source range or drop the number entirely; a conflicting figure is never averaged into confidence. <code>sources</code> lists that look empty are deliberate too: it means the piece makes no external factual claims, because it's engineering reasoning or our own experience.</p>
<h2>Verification before publish</h2>
<p>Volatile claims carry a hard gate: nothing publishes on a remembered number. Code examples are executed in a real environment before publishing where practical. And the site itself is machine-checked every build: internal links must all resolve, thin and duplicate pages fail a quality gate, and the deployed pages are spot-checked against their source claims &mdash; we verify the built page, not the intention.</p>
<h2>When facts age</h2>
<p>Technology pieces rot at the edges: prices, model names, menu paths, limits. Pieces with volatile claims are stamped in-text (&ldquo;checked September 2026&rdquo;) and treated as UPDATE-class: on re-review we re-verify against the official pages, patch the text, and add an explicit dated re-verified note. Dates are never quietly refreshed.</p>
<h2>What we refuse</h2>
<p>Fabricated benchmarks, invented statistics, fake screenshots, imagined experience, and pages built to exist rather than to be useful. A smaller number of pages that survive their own claims is the whole business model &mdash; see <a href="/tech/corrections/">what happens when one doesn't</a>.</p>
</div></section></div>"""
    corrections_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Corrections</nav>
<section class="cover"><p class="kicker">Corrections policy</p><h1 class="cover-title">Corrections, handled in the open.</h1>
<p class="cover-dek">Errors get fixed in the text, noted with a date, and never quietly. A publication that can't show its corrections is asking you to trust its averages instead of its record.</p></section>
<section class="section"><div class="prose">
<h2>How errors get found</h2>
<p>Three ways, in rough order of frequency: our own scheduled re-verification passes (volatile claims &mdash; pricing, limits, legal statuses &mdash; are re-checked against official pages before any piece is republished); the automated checks that run on every build (every internal link must resolve; thin and duplicate pages fail the build); and readers, who remain the best error-finding system ever invented. <a href="/tech/contact/">If you find one, that email is the most valuable one we get.</a></p>
<h2>What happens next</h2>
<p><strong>Substantive corrections</strong> &mdash; a wrong number, a broken method, a claim that no longer holds &mdash; are fixed in the text and noted on the page with the date and what changed. If a claim can no longer be verified at all, it is removed rather than softened into vagueness. <strong>Re-verifications</strong> (the claim still holds, re-checked on a later date) are noted the same way, because a date that silently refreshes is worth nothing. <strong>Wording fixes</strong> &mdash; typos, unclear phrasing &mdash; are fixed directly; they change nothing you'd rely on, so they don't get a stamp.</p>
<h2>The receipts habit</h2>
<p>Behind the published pages, every batch of work keeps a written record: which sources were checked live, which claims were gated and how they resolved, what was deliberately left out because the evidence didn't support it. When this desk's own numbers have changed under honest re-audit &mdash; and in the QuantLab project they have, dramatically &mdash; the change is the story, not an embarrassment: <a href="/tech/lookahead-bias-explained/">a backtest result that didn't survive its own entry-bar audit became the most useful article on the shelf</a>.</p>
<h2>The standard</h2>
<p>No silent re-dating, no retro-fitting claims to what turned out true, no deleting the evidence of what we wrote before. The record is the product.</p>
</div></section></div>"""
    terms_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Terms</nav>
<section class="cover"><p class="kicker">Terms of use</p><h1 class="cover-title">The plain terms.</h1>
<p class="cover-dek">Short version: this is a publication, not a professional service. Use it the way you'd use a good book &mdash; intelligently, and at your own discretion.</p></section>
<section class="section"><div class="prose">
<h2>What this site is</h2>
<p>BRYME Tech is an independent technical publication offering general information, guides, opinion and research notes. It is not a consultancy, an agency, or a professional service, and using it does not create any professional relationship or duty of care between you and the publisher.</p>
<h2>No warranties</h2>
<p>The site and its content are provided &ldquo;as is&rdquo;, without warranties of any kind, express or implied, including fitness for a particular purpose or accuracy beyond what the <a href="/tech/methodology/">published methodology</a> states. Technology changes under our feet; steps that worked when written may not work when read. Check official documentation before acting on anything consequential.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by applicable law, the publisher is not liable for any loss or damage arising from use of, or reliance on, the site or its content &mdash; including technical steps you run on your own systems, which you do at your own discretion and risk.</p>
<h2>The tools</h2>
<p>Browser tools on this site run entirely in your browser. Text you paste into them is processed on your device and is not uploaded, stored, or transmitted to us. Don't paste secrets into any web tool anyway &mdash; that's not a term, it's <a href="/tech/plain-text-passwords/">the same advice we give everywhere</a>.</p>
<h2>Ownership and trademarks</h2>
<p>Original text and structure are &copy; THE BRYME. Product names, logos and trademarks mentioned belong to their respective owners; mention implies no affiliation, sponsorship or endorsement, and no trademark is claimed. External links are references, not endorsements; we don't control those pages.</p>
<h2>Changes</h2>
<p>These terms may be updated as the publication grows; material changes get dated notes on this page rather than silent edits. Questions: <a href="/tech/contact/">Contact</a>. See also the <a href="/tech/disclaimer/">disclaimer</a> and <a href="/tech/privacy/">privacy</a> pages.</p>
</div></section></div>"""
    disclaimer_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Disclaimer</nav>
<section class="cover"><p class="kicker">Disclaimer</p><h1 class="cover-title">What this desk is, and isn't.</h1></section>
<section class="section"><div class="prose">
<h2>General information, not professional advice</h2>
<p>Everything on BRYME Tech is general technical information. Troubleshooting steps, security guides and configuration advice describe what has worked in specific situations and are not tailored advice for your systems; run them at your own discretion, and for high-stakes situations (production outages, security incidents, legal questions about technology) consult a professional who can see the whole picture.</p>
<h2>Quantitative and trading-adjacent research</h2>
<p>Research note: QuantLab experiments are presented for educational and research purposes. Historical backtests and simulations do not guarantee future results and should not be interpreted as investment advice.</p>
<p>In plain words: the <a href="/tech/quantlab-project-how-built/">QuantLab pieces</a> document a research process &mdash; statistics, software engineering, validation discipline, and a lot of instructive failure. They do not recommend any strategy, signal, instrument or trade, they do not republish performance as a promise, and nothing on this desk should move you to risk money. Most of the project's rigorous conclusions are that promising edges were not real. That is the point of publishing them.</p>
<h2>Products, names and dates</h2>
<p>Product names and trademarks belong to their owners; mention implies no affiliation or endorsement. Claims about products carry their check-date in the text and may have changed since &mdash; the official page is always the current truth. External links are provided for verification and reference, not endorsement.</p>
<p class="lede"><em>Last reviewed: September 2026. Found something wrong or stale? <a href="/tech/corrections/">This is how we fix it</a>.</em></p>
</div></section></div>"""
    def _pg(route, title, desc, body):
        return (route, title, desc, '<main id="main">' + body + "</main>")
    return [
        _pg("/methodology/", "Editorial methodology | BRYME Tech",
            "How BRYME Tech researches, verifies and labels what it publishes: primary sources, named dates, first-hand labels, and no remembered numbers.",
            methodology_body),
        _pg("/corrections/", "Corrections policy | BRYME Tech",
            "How errors are found, fixed, dated and never quietly: the BRYME Tech corrections policy and re-verification discipline.",
            corrections_body),
        _pg("/terms/", "Terms of use | BRYME Tech",
            "The plain terms of use for BRYME Tech: general information, no warranties, tools that run in your browser.",
            terms_body),
        _pg("/disclaimer/", "Disclaimer | BRYME Tech",
            "What BRYME Tech is and isn't: general information, not professional advice; QuantLab research is educational, never investment advice.",
            disclaimer_body),
    ]


_TECH_FIRSTHAND = {
    "quantlab-project-how-built": "BRYME Technical Research \u00b7 first-hand project report",
    "hundred-experiments-lessons": "BRYME Technical Research \u00b7 first-hand project report",
    "lookahead-bias-explained": "BRYME Technical Research \u00b7 first-hand project report",
    "backtest-validation-checklist": "BRYME Technical Research \u00b7 first-hand project report",
    "why-backtests-fail": "BRYME Technical Research \u00b7 first-hand project report",
    "paper-trading-bot-lessons": "BRYME Technical Research \u00b7 first-hand project report",
    "overfitting-detection-guide": "BRYME Technical Research \u00b7 first-hand project report",
}

_TOOL_JS = {"json-formatter": "json", "base64-encoder": "base64", "url-encoder": "url",
            "uuid-generator": "uuid", "timestamp-converter": "timestamp", "word-counter": "wordcount",
            "case-converter": "case", "http-status-lookup": "status"}

def tech_tool_pages():
    """BRYME Tools (master build M3): client-side tools at /tech/tool/<slug>/, CSP-safe."""
    import tech_tools_data
    tools = tech_tools_data.TOOLS
    pages = []
    for slug, name, title, dek, art, what, ui in tools:
        sibs = [t for t in tools if t[0] != slug]
        sib_btns = "".join('<a class="btn secondary" href="/tool/' + t[0] + '/">' + t[1].split(" (")[0].split(" / ")[0] + '</a>'
                           for t in (sibs[0], sibs[2], sibs[4], sibs[6]))
        guide_btn = ('<a class="btn secondary" href="/' + art + '/">Read the guide</a>') if art else ""
        tbody = (head("tech", "Practical technology. No theatre.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/tech/">Tech</a> / <a href="/tool/">Toolbox</a> / ' + name + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Tools \u00b7 runs entirely in your browser</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + title + "</h1>"
            + '<p class="cover-dek">' + dek + "</p></section>"
            + '<section class="section"><div class="wrap"><link rel="stylesheet" href="/assets/tech-tools.css">' + ui + "</div></section>"
            + '<section class="section alt"><div class="prose">' + what + "</div></section>"
            + '<section class="section"><div class="prose"><p><b>Privacy note:</b> every tool on this desk processes your input on your device, in this page \u2014 nothing is uploaded, stored or sent anywhere. The same policy the <a href="/tech/terms/">terms</a> and <a href="/tech/privacy/">privacy</a> pages promise.</p></div>'
            + '<div class="actions">' + guide_btn + sib_btns + '<a class="btn secondary" href="/tech/">All of BRYME Tech</a></div></section>'
            + '<script src="/assets/tool-' + _TOOL_JS[slug] + '.js" defer></script>'
            + "</div></main>" + foot("tech"))
        pages.append(("/tool/" + slug + "/", title + " | BRYME Tools", dek, tbody))
    hub_rows = "".join('<li><a href="/tool/' + slug + '/"><span><b>' + title + "</b><small>" + dek + "</small></span>"
                       '<span class="meta">Tool</span></a></li>' for slug, name, title, dek, art, what, ui in tools)
    hub = (head("tech", "Practical technology. No theatre.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/tech/">Tech</a> / The toolbox</nav>'
        + '<section class="cover"><p class="kicker">BRYME Tools \u00b7 the toolbox</p>'
        + '<h1 class="cover-title">Small tools, zero strings.</h1>'
        + '<p class="cover-dek">Developer and writer utilities that run entirely in your browser: no accounts, no uploads, no data collection \u2014 open the page, use the tool, close the page. Each one has a companion guide explaining the format behind it.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(tools)) + ' tools</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + hub_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">The honest bit</p><h2>What "runs in your browser" means.</h2></div>'
        + '<div class="prose"><p>Every tool here is a small script served with this page and executed by <em>your</em> browser on <em>your</em> device. There is no backend to send your text to, no logging, no account. The <a href="/tech/disclaimer/">disclaimer</a> applies: general-purpose utilities, provided as-is \u2014 and the standing advice holds everywhere: do not paste secrets into web tools, including these.</p></div></section>'
        + '</div></main>' + foot("tech"))
    pages.insert(0, ("/tool/", "BRYME Tools \u2014 browser tools, zero data collection | BRYME Tech",
                     "Eight free browser tools \u2014 JSON formatter, Base64, URL encoding, UUID generator, timestamps, word counter, case converter, HTTP status lookup. Client-side, no data collection.", hub))
    return pages


def tech_pages():
    arts = _load_tech()
    for a in arts:
        if a["slug"] in _TECH_FIRSTHAND:
            a["author"] = _TECH_FIRSTHAND[a["slug"]]
    by_cat = {}
    for a in arts:
        by_cat.setdefault(a["cat"], []).append(a)
    for lst in by_cat.values():
        lst.sort(key=lambda x: x["upd"] or x["pub"], reverse=True)

    cat_pages = {}
    for cslug, (cname, cdesc, _hero) in TECH_CAT.items():
        lst = by_cat.get(cslug, [])
        rows = "".join(
            '<li><a href="/' + a["slug"] + '/"><span><b>' + html.escape(a["title"]) + "</b>"
            "<small>" + html.escape(a["excerpt"][:110]) + ("\u2026" if len(a["excerpt"]) > 110 else "") + "</small></span>"
            '<span class="meta">' + (a["upd"] or a["pub"]) + "</span></a></li>"
            for a in lst)
        others = "".join('<a class="btn secondary" href="/' + c + '/">' + html.escape(TECH_CAT[c][0]) + "</a>"
                         for c in TECH_CAT if c != cslug)
        cbody = (head("tech", "Practical technology. No theatre.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/tech/">Tech</a> / ' + html.escape(cname) + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Tech \u00b7 section</p>'
            + '<h1 class="cover-title">' + html.escape(cname) + "</h1>"
            + '<p class="cover-dek">' + html.escape(cdesc) + "</p></section>"
            + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(lst)) + ' guides</p><h2>Everything in ' + html.escape(cname) + '.</h2></div>'
            + '<ul class="list">' + rows + "</ul></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Keep going</p><h2>Elsewhere on this desk.</h2></div>'
            + '<div class="actions">' + others + '</div></section></div></main>' + foot("tech"))
        cat_pages[cslug] = [("/" + cslug + "/", cname + " | BRYME Tech", cdesc, cbody)]

    def art_page(a):
        cslug = a["cat"]
        cname = TECH_CAT.get(cslug, ("Coding",))[0] if cslug in TECH_CAT else "Coding"
        chref = "/tech/" if cslug not in TECH_CAT else "/tech/" + cslug + "/"
        rel = _tech_related(a, arts)
        rel_html = "".join('<li><a href="/' + r["slug"] + '/">' + html.escape(r["title"]) + "</a></li>" for r in rel)
        src_html = ""
        if a["sources"]:
            src_html = ('<h2>Sources</h2><ul class="list">'
                        + "".join('<li><a href="' + html.escape(s["url"]) + '" rel="noopener">' + html.escape(s["name"]) + "</a></li>"
                                  for s in a["sources"]) + "</ul>")
        meta_bits = ["By " + html.escape(a["author"])]
        if a["pub"]:
            meta_bits.append("published " + a["pub"])
        if a["upd"] and a["upd"] != a["pub"]:
            meta_bits.append("updated " + a["upd"])
        if a["read"]:
            meta_bits.append(a["read"])
        kind_kick = {"firsthand": "First-hand \u00b7 ", "guide": "Practical guide \u00b7 "}
        tag = ("Recovered from the BRYME tech archive \u00b7 " if a["recovered"]
               else kind_kick.get(a.get("kind", "firsthand"), "Practical guide \u00b7 "))
        summ = ('<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> '
                + html.escape(a["excerpt"]) + "</p></div></section>") if a["excerpt"] else ""
        schema = {"@context": "https://schema.org", "@type": "TechArticle",
                  "headline": a["title"], "author": {"@type": "Person", "name": a["author"]},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": a["pub"] or None, "dateModified": a["upd"] or a["pub"] or None,
                  "mainEntityOfPage": ORIGIN + "/tech/" + a["slug"] + "/"}
        import json as _j
        abody = (head("tech", "Practical technology. No theatre.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/tech/">Tech</a> / <a href="' + chref + '">' + html.escape(cname) + "</a> / " + html.escape(a["title"]) + "</nav>"
            + '<section class="cover"><p class="kicker">' + tag + "verified against the real thing</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(a["title"]) + "</h1>"
            + '<p class="byline">' + " \u00b7 ".join(meta_bits) + "</p></section>"
            + summ
            + '<section class="section"><div class="prose">' + _tech_blocks(a) + src_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + '</ul>'
            + '<div class="actions"><a class="btn secondary" href="' + chref + '">All of ' + html.escape(cname) + '</a>'
            + '<a class="btn secondary" href="/tech/">All of BRYME Tech</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("tech"))
        return (("/" + a["slug"] + "/"), a["title"] + " | BRYME Tech", a["excerpt"][:155], abody)

    latest = sorted(arts, key=lambda x: x["upd"] or x["pub"], reverse=True)[:5]
    latest_rows = "".join(
        '<li><a href="/' + a["slug"] + '/"><span><b>' + html.escape(a["title"]) + "</b><small>"
        + html.escape(a["excerpt"][:100]) + "\u2026</small></span><span class=\"meta\">" + (a["upd"] or a["pub"]) + "</span></a></li>"
        for a in latest)
    start_here = ["where-to-host-website-for-free", "bitwarden-free-password-manager",
                  "render-deployment-failures-what-they-taught-me"]
    start_rows = "".join(
        '<li><a href="/' + s + '/"><span><b>' + html.escape(next(a["title"] for a in arts if a["slug"] == s))
        + "</b><small>" + html.escape(next(a["excerpt"][:110] for a in arts if a["slug"] == s))
        + "\u2026</small></span><span class=\"meta\">Start here</span></a></li>" for s in start_here)
    cat_cards = "".join(
        '<article class="pub-card live" style="--pc:#1e3a5f"><p class="pc-kicker">' + str(len(by_cat.get(c, []))) + ' GUIDES</p>'
        + "<h3>" + html.escape(TECH_CAT[c][0]) + "</h3><p>" + html.escape(TECH_CAT[c][1][:130]) + "\u2026</p>"
        + '<a class="btn" href="/' + c + '/">Browse ' + html.escape(TECH_CAT[c][0].split(",")[0].split(" &")[0]) + ' \u2192</a></article>'
        for c in TECH_CAT)
    index_body = (head("tech", "Practical technology. No theatre.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Tech</p>'
        + '<h1 class="cover-title">Practical technology. No theatre.</h1>'
        + '<p class="cover-dek">You have a technology problem, question or decision. This desk helps you understand or solve it \u2014 with guides checked against the real products and real deploys, dated honestly, and evergreen on purpose.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Handpicked</p><h2>Start here.</h2></div>'
        + '<ul class="list">' + start_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Browse by need</p><h2>Sections of this desk.</h2></div>'
        + '<div class="cards">' + cat_cards + "</div>"
        + '</section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Interactive</p><h2>The toolbox.</h2></div>'
        + '<p class="lede">Eight small tools that run entirely in your browser &mdash; nothing you type or paste is sent anywhere: <a href="/tool/json-formatter/">JSON formatter</a> &middot; <a href="/tool/base64-encoder/">Base64 encoder</a> &middot; <a href="/tool/url-encoder/">URL encoder</a> &middot; <a href="/tool/uuid-generator/">UUID generator</a> &middot; <a href="/tool/timestamp-converter/">timestamp converter</a> &middot; <a href="/tool/word-counter/">word counter</a> &middot; <a href="/tool/case-converter/">case converter</a> &middot; <a href="/tool/http-status-lookup/">HTTP status lookup</a>. Each has a <a href="/tech/what-is-json/">companion guide</a> explaining the underlying format.</p>'
        + '</section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Freshly dated</p><h2>Recently updated.</h2></div>'
        + '<ul class="list">' + latest_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">The promise</p><h2>What "no theatre" means here.</h2></div>'
        + '<p class="lede">No AI-tool hype cycles, no top-ten lists assembled from other top-ten lists, no benchmarks without the machine in front of us. If a piece says first-hand, someone on this desk did the thing and wrote down what happened \u2014 including what went wrong. Time-sensitive facts carry their verification dates and named sources.</p>'
        + '</section></div></main>' + foot("tech"))
    pages = [("/", "BRYME Tech \u2014 practical technology help, no theatre",
              "Practical technology guides: AI checked against real products, free-tool alternatives, hosting and DNS from real deploys, and safety without scaremongering.", index_body)]
    for cslug, pl in cat_pages.items():
        pages.extend(pl)
    pages.extend(art_page(a) for a in arts)
    pages.extend(tech_tool_pages())
    return pages + tech_trust_pages() + legal_pages("tech", "BRYME Tech", "Practical technology from people who ran the thing.")



# ------------------------------------------------------------------ 5. FITNESS
FIT_WALK_DAYS = [
    (1, "10 minutes, easy pace. Just show up.", "The first week is about the habit, not the speed."),
    (2, "10 minutes, easy pace.", "Same time of day as yesterday. Routine beats motivation."),
    (3, "12 minutes.", "Add two minutes, not ten. Slow progress is progress that sticks."),
    (4, "12 minutes, relaxed.", "Land softly, look ahead, let your arms swing."),
    (5, "15 minutes.", "If you can talk while walking, the pace is right for now."),
    (6, "15 minutes, anywhere new.", "A new route counts as entertainment."),
    (7, "Rest, or 10 gentle minutes if you would miss it.", "Rest days are part of the plan, not a failure."),
    (8, "15 minutes.", "Two weeks in: judge the calendar, not the mirror."),
    (9, "18 minutes.", "Breathe in rhythm \u2014 steps in, steps out."),
    (10, "18 minutes.", "Hills count double for effort. Take them slowly."),
    (11, "15 minutes, easy.", "An easy day after a harder one is smart training."),
    (12, "20 minutes.", "Twenty minutes is a milestone. Notice it."),
    (13, "20 minutes.", "Drink water before you leave, not just after."),
    (14, "Rest, or 10 gentle minutes.", "Two weeks done. Most people quit by now. You did not."),
    (15, "22 minutes.", "The habit is forming. Protect the schedule."),
    (16, "22 minutes, the last 5 slightly faster.", "Finish a little quicker than you started."),
    (17, "25 minutes.", "Longer day: pick a route with some shade."),
    (18, "20 minutes, easy.", "Recovery walks help you come back stronger."),
    (19, "25 minutes.", "Track one thing: time, distance, or how you felt."),
    (20, "30 minutes.", "Half an hour \u2014 the classic benchmark. You are here."),
    (21, "Rest, or 15 gentle minutes.", "Soreness that fades in a day or two is normal. Sharp pain is not \u2014 respect it."),
    (22, "30 minutes.", "Keep the pace conversational."),
    (23, "30 minutes, a brisk middle 10.", "Brisk means you can talk, but not sing."),
    (24, "25 minutes, easy.", "Easy days are what let the stronger days work."),
    (25, "35 minutes.", "The longest walk of the month. Start unhurried."),
    (26, "25 minutes.", "Notice the difference from Day 1."),
    (27, "30 minutes.", "Same time, same rhythm. Almost there."),
    (28, "20 minutes, easy.", "Taper day. Let your body bank the work."),
    (29, "30 minutes on your favourite route.", "Pick the walk you enjoyed most this month."),
    (30, "30+ minutes \u2014 finish, then decide what is next.", "Day 30 is a beginning: repeat week four, or try the strength basics next."),
]

FIT_SOURCES = [
    ("WHO \u2014 Physical activity (fact sheet)", "https://www.who.int/news-room/fact-sheets/detail/physical-activity"),
    ("CDC \u2014 Physical Activity Basics", "https://www.cdc.gov/physical-activity-basics/"),
]

FIT_ARTICLES = [
    ("how-to-start-working-out",
     "Starting from zero: how to begin exercising when you are out of the habit",
     "The practical, no-miracle starting guide: begin low, progress slowly, and let the calendar \u2014 not motivation \u2014 carry you.",
     """<p>The hardest workout of your life is the one that gets you off the sofa the first time. Not because exercise is brutal, but because the habit does not exist yet. The good news, supported by every mainstream public-health guideline, is that the first week does not need to be impressive. It needs to be repeatable.</p>
<h2>Start low, go slow</h2>
<p>Public-health agencies, including the WHO and the CDC, use the same phrase for returning beginners: start low and go slow. For most people that means short sessions of moderate activity \u2014 brisk walking is the classic \u2014 increasing gradually over weeks. The adult guideline worth knowing is around 150 minutes of moderate aerobic activity spread across a week, plus muscle-strengthening on two or more days. You do not start there. You build toward it.</p>
<h2>The two-day rule</h2>
<p>Early on, the only metric that matters is this: do not let two scheduled days pass in a row without doing the session. Ten minutes on a day you feel flat protects the habit. A heroic 90-minute session followed by ten silent days does not. Motivation is weather; the calendar is climate.</p>
<h2>What counts as exercise</h2>
<p>More than people assume. Brisk walking counts. Carrying shopping counts. Taking the stairs, digging a garden bed, dancing badly in your kitchen \u2014 all of it raises your breathing and counts toward the week. If a gym feels like a hostile planet, start at home. The 30-day walking plan on this desk exists precisely because walking is the most underrated entry point in fitness.</p>
<h2>Equipment: none</h2>
<p>A beginner needs shoes that do not hurt and a door. Everything sold as essential is optional. Buy things later, when a specific gap annoys you three sessions in a row \u2014 that is evidence, unlike advertising.</p>
<h2>When to get professional advice first</h2>
<p>This is general information, not medical advice. If you have a health condition, have been inactive for a long time, are pregnant, or get chest pain, dizziness or unusual breathlessness during effort, talk to a qualified health professional before starting. That is not a formality \u2014 it is the difference between a plan and a risk.</p>
<h2>Where to begin on this desk</h2>
<p><a href="/30-day-walking-plan/">The 30-day walking plan</a> is the structured route in. <a href="/how-many-steps-a-day/">The honest guide to step counts</a> sets realistic expectations, and <a href="/rest-days-and-recovery/">the recovery guide</a> explains the part most beginners skip.</p>"""),
    ("how-many-steps-a-day",
     "How many steps a day actually matter? The honest answer",
     "Where 10,000 steps came from, what the research actually found, and the number a beginner should care about instead.",
     """<p>Ask how many steps you should walk and you will hear one number: 10,000. It is on every fitness tracker by default. What almost nobody mentions is where the number came from \u2014 and what the research actually says.</p>
<h2>The number was marketing, not medicine</h2>
<p>The 10,000-step figure is often traced to a 1960s Japanese walking-club campaign around a pedometer whose name can be read as \u201c10,000-step meter\u201d. It was catchy, round and optimistic. It was not a clinical threshold. It became a default because devices shipped with it, and it spread from there.</p>
<h2>What a large study actually found</h2>
<p>One of the most cited step studies followed more than 16,000 older women and compared step counts with deaths over time (Lee et al., JAMA Internal Medicine, 2019). The pattern: the least active group averaged around 2,700 steps a day, mortality was lower in groups averaging around 4,400 steps, and the benefit continued as steps rose, levelling off at roughly 7,500. Two honest caveats: the participants were older women, so the exact numbers do not transfer automatically to everyone; and the study shows association, not a magic threshold you cross and lock in.</p>
<h2>The practical takeaway for a beginner</h2>
<p>More is generally better than less, the biggest jump in benefit is going from very few steps to a modest number, and there is no cliff at 10,000. If your normal day is 3,000 steps, aiming at 6,000 beats aiming at 10,000 and quitting in week two. That is why the <a href="/30-day-walking-plan/">30-day walking plan</a> is built around time and consistency first, with steps as a side effect.</p>
<h2>How to count \u2014 and how not to obsess</h2>
<p>A phone in your pocket estimates steps adequately for trends. Treat any single day as noise and the weekly average as signal. If a tracker makes you anxious, leave it home once in a while \u2014 the walk works with nobody counting.</p>
<h2>The rest of the guideline</h2>
<p>Steps cover the aerobic half. The other half of the adult guideline is muscle-strengthening work on two or more days a week \u2014 see <a href="/strength-training-for-beginners/">the beginner strength guide</a>.</p>"""),
    ("strength-training-for-beginners",
     "Strength training for beginners: six moves, two days, no gym",
     "Why the guidelines want you lifting at least twice a week, the six patterns that cover it, and how to progress without equipment.",
     """<p>Walking is the front door to fitness; strength is the part that keeps the house standing. Public-health guidelines are specific here: muscle-strengthening activity on two or more days a week, working the major muscle groups. It protects bone, joint function and the ability to keep doing everything else you enjoy \u2014 and it does not require a gym.</p>
<h2>The six patterns</h2>
<p>Nearly every useful strength exercise is a variation of six movements. Learn them with bodyweight or household load, and you have a lifetime programme:</p>
<p>Sit down and stand back up from a chair, slowly, without using your hands. That is a squat pattern. Lie face down and push the floor away from your knees or toes \u2014 a push-up, scaled to a wall or a counter if needed. Hinge at the hips with a flat back and stand back up \u2014 the deadlift pattern, with a backpack of books when you are ready. Pull something toward you: a door-frame row, a towel row, or a backpack curl. Carry something moderately heavy from one end of the room to the other and put it down carefully \u2014 the carry, the most underrated exercise there is. Finally, hold a plank position on forearms and knees or toes, and breathe.</p>
<h2>Two days, twenty minutes</h2>
<p>Pick one exercise from each pattern. Do each for a number of repetitions that leaves you feeling like you could do two or three more with good form \u2014 that is what \u201cmoderate\u201d means in practice. Rest, then repeat twice. Two such sessions a week, with at least one day between them, satisfies the guideline.</p>
<h2>Progressive overload, honestly explained</h2>
<p>Muscle adapts to what you ask of it. When the current work feels comfortable, ask slightly more: one more repetition, a slower lowering phase, a heavier backpack, a lower surface for push-ups. Small and boring wins. Pain is not part of the plan; effort is.</p>
<h2>Soreness is not the goal</h2>
<p>New movements commonly cause soreness a day or two later. It fades. It is not a score. Chasing soreness is how beginners get hurt or quit \u2014 see <a href="/rest-days-and-recovery/">the recovery guide</a> for what to do instead. This page is general information, not medical advice; if something hurts sharply or persistently, stop and get qualified advice.</p>"""),
    ("rest-days-and-recovery",
     "Rest days and recovery: the part of training that actually builds you",
     "Why adaptation happens between sessions, what DOMS really is, and the difference between rest and quitting.",
     """<p>Exercise is the question. Recovery is the answer. When you walk, lift or carry, you create a small stress; your body responds during the hours and days afterwards, rebuilding slightly stronger than before. Skip the recovery and you skip the adaptation \u2014 the training was just wear.</p>
<h2>What rest day means</h2>
<p>A rest day is not a sofa day and it is not a failure. It means no planned training. Gentle movement \u2014 an unhurried walk, stretching while the kettle boils \u2014 is fine and often feels better than nothing. What it does not mean is swapping your schedule because enthusiasm dipped. Enthusiasm is allowed to dip. The calendar stands.</p>
<h2>DOMS, explained honestly</h2>
<p>Soreness that arrives a day or so after unfamiliar exercise \u2014 especially the lowering phase of movements \u2014 is called delayed-onset muscle soreness (DOMS). It commonly peaks in the first day or two and settles within several days. It is a normal response to new work, not a badge of quality: a session that leaves you unable to walk downstairs was overdone, not superior. Mechanisms are still debated in the research; the practical handling is not \u2014 move gently, hydrate, sleep, and let it pass before hitting the same muscles hard again.</p>
<h2>Sleep is the strongest legal performance aid</h2>
<p>Nothing sold in a shaker compares with enough sleep. It is when the bulk of recovery happens. If you must choose between an extra hour asleep and a groggy extra session, take the sleep more often than not.</p>
<h2>When soreness is a warning</h2>
<p>Sharp pain, pain that worsens past a few days, swelling, or soreness paired with dark urine are not DOMS and are not to be trained through. This is general information, not medical advice \u2014 a qualified professional should assess anything that fails those tests.</p>
<h2>How the walking plan handles rest</h2>
<p>Every seventh day of the <a href="/30-day-walking-plan/">30-day walking plan</a> is a rest day by design. That rhythm \u2014 stress, recover, repeat slightly stronger \u2014 is the whole trick behind every serious training programme ever written.</p>"""),
]

def _fit_shell(pub, kicker, title, dek, extra_disclaimer=False):
    band = ('<section class="section alt" style="border-left:4px solid var(--brand)"><div class="wrap"><p class="lede"><b>General information, not medical advice.</b> '
            "If you have a health condition, have been inactive for a long time, or something hurts sharply, talk to a qualified health professional first.</p></div></section>")
    return band

def fitness_pages():
    def src_html(sources):
        if not sources:
            return ""
        return ('<h2>Sources</h2><ul class="list">'
                + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                + "</ul>")

    def art(slug, title, dek, body_html, sources, related, schema_type="Article"):
        import json as _j
        rel_html = "".join('<li><a href="/' + s + '/">' + rt + "</a></li>" for s, rt in related)
        schema = {"@context": "https://schema.org", "@type": schema_type,
                  "headline": title,
                  "author": {"@type": "Organization", "name": "BRYME Fitness desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/fitness/" + slug + "/",
                  "description": dek}
        abody = (head("fitness", "Practical fitness \u2014 no miracles, no medical claims.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/fitness/">Fitness</a> / ' + html.escape(title) + "</nav>"
            + '<section class="cover"><p class="kicker">' + kicker_default + "</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(title) + "</h1>"
            + '<p class="byline">BRYME Fitness desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not medical advice</p></section>"
            + '<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(dek) + "</p></div></section>"
            + '<section class="section"><div class="prose">' + body_html + src_html(sources) + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Keep going</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/fitness/">All of BRYME Fitness</a></div></section>'
            + _fit_shell("fitness", "", "", "", True)
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("fitness"))
        return (("/" + slug + "/"), title + " | BRYME Fitness", dek[:155], abody)

    kicker_default = "Evidence-aware \u00b7 beginner-first \u00b7 no miracle claims"
    related_map = {
        "how-to-start-working-out": [("30-day-walking-plan", "The 30-day walking plan"),
                                     ("how-many-steps-a-day", "How many steps a day actually matter?"),
                                     ("rest-days-and-recovery", "Rest days and recovery")],
        "how-many-steps-a-day": [("30-day-walking-plan", "The 30-day walking plan"),
                                 ("how-to-start-working-out", "Starting from zero"),
                                 ("strength-training-for-beginners", "Strength training for beginners")],
        "strength-training-for-beginners": [("rest-days-and-recovery", "Rest days and recovery"),
                                            ("how-to-start-working-out", "Starting from zero"),
                                            ("30-day-walking-plan", "The 30-day walking plan")],
        "rest-days-and-recovery": [("strength-training-for-beginners", "Strength training for beginners"),
                                   ("how-to-start-working-out", "Starting from zero"),
                                   ("30-day-walking-plan", "The 30-day walking plan")],
    }

    # ---- the 30-day plan page (the product) ----
    week_rows = ""
    for wk_start in (1, 8, 15, 22):
        label = {1: "Week 1 \u00b7 show up", 8: "Week 2 \u00b7 rhythm",
                 15: "Week 3 \u00b7 range", 22: "Week 4 \u00b7 finish strong"}[wk_start]
        wk_end = wk_start + (9 if wk_start == 22 else 7)
        rows = ""
        for d, task, tip in FIT_WALK_DAYS:
            if not (wk_start <= d < (wk_start + 9 if wk_start == 22 else wk_start + 7)):
                continue
            rows += ('<li class="fp-day" data-day="' + str(d) + '">'
                     '<span class="fp-num">' + str(d) + "</span><span><b>" + task + "</b>"
                     "<small>" + tip + "</small></span>"
                     '<button type="button" class="btn secondary fp-done" aria-pressed="false">Done</button></li>')
        week_rows += ('<section class="section"><div class="section-head"><p class="kicker">Days '
                      + str(wk_start) + "\u2013" + str(wk_end - 1) + "</p><h2>" + label + "</h2></div>"
                      + '<ul class="list fp-week">' + rows + "</ul></section>")
    import json as _j
    plan_schema = {"@context": "https://schema.org", "@type": "Article",
                   "headline": "The 30-Day Walking Plan",
                   "author": {"@type": "Organization", "name": "BRYME Fitness desk"},
                   "publisher": {"@type": "Organization", "name": "THE BRYME"},
                   "datePublished": TODAY, "dateModified": TODAY,
                   "mainEntityOfPage": ORIGIN + "/fitness/30-day-walking-plan/",
                   "description": "A beginner walking plan built around one honest idea: show up every day for a month. Progress is tracked in your browser \u2014 no account, nothing sent anywhere."}
    plan_body = (head("fitness", "Practical fitness \u2014 no miracles, no medical claims.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/fitness/">Fitness</a> / The 30-Day Walking Plan</nav>'
        + '<section class="cover"><p class="kicker">' + kicker_default + "</p>"
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The 30-Day Walking Plan</h1>'
        + '<p class="byline">BRYME Fitness desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not medical advice</p></section>"
        + '<section class="section alt"><div class="wrap"><p class="lede"><b>One honest idea:</b> show up every day for a month. The plan is built on time, not distance, and every seventh day is a rest day by design. Progress is saved in your browser \u2014 no account, nothing sent anywhere.</p></div></section>'
        + '<section class="section"><div class="wrap"><div class="fp-progressbar" role="img" aria-label="Plan progress"><div class="fp-fill" id="fp-fill"></div></div>'
        + '<p class="lede" id="fp-status">Day 0 of 30 complete. Tick days off as you go \u2014 your browser will remember.</p></div></section>'
        + week_rows
        + '<section class="section"><div class="section-head"><p class="kicker">The fine print</p><h2>How to use this plan sensibly.</h2></div>'
        + '<div class="prose"><p>\u201cEasy pace\u201d means you can hold a conversation; \u201cbrisk\u201d means you can talk but not sing. If a day feels too hard, repeat the previous day \u2014 the numbering is a suggestion, your body is the schedule. Sharp pain, dizziness or unusual breathlessness: stop. This is general information, not medical advice; if you have a health condition or have been inactive for a long time, see a qualified professional first.</p>'
        + '<p>Finished? Repeat week four, move the brisk blocks earlier, or add two strength days from <a href="/strength-training-for-beginners/">the beginner strength guide</a>.</p></div></section>'
        + '<section class="section alt">' + src_html(FIT_SOURCES) + "</section>"
        + _fit_shell("fitness", "", "", "", True)
        + '<script type="application/json" id="fit-plan-data">{"total": 30}</script>'
        + '<script src="/assets/fitness-plan.js" defer></script>'
        + '<script type="application/ld+json">' + _j.dumps(plan_schema) + "</script>"
        + "</div></main>" + foot("fitness"))
    plan_page = [("/30-day-walking-plan/", "The 30-Day Walking Plan | BRYME Fitness",
                  "A beginner walking plan built on one honest idea: show up every day for a month. Time-based, rest days built in, progress saved in your browser.", plan_body)]

    ART_SOURCES = dict((s, FIT_SOURCES) for s, _, _, _ in FIT_ARTICLES)
    ART_SOURCES["how-many-steps-a-day"] = FIT_SOURCES + [
        ("Lee et al., JAMA Internal Medicine (2019) \u2014 Association of Step Volume and Intensity With All-Cause Mortality in Older Women",
         "https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2731911")]
    import more_guides_data
    FIT_ARTICLES.extend((s, ti, dek, b) for (s, _k, ti, dek, b) in more_guides_data.FIT_MORE)
    ART_SOURCES.update((s, FIT_SOURCES) for (s, _k, ti, dek, b) in more_guides_data.FIT_MORE)
    related_map["walking-vs-running"] = [("30-day-walking-plan", "The 30-day walking plan"),
                                         ("how-to-warm-up", "How to warm up"),
                                         ("how-to-start-working-out", "Starting from zero")]
    related_map["how-to-warm-up"] = [("strength-training-for-beginners", "Strength training for beginners"),
                                     ("walking-vs-running", "Walking or running?"),
                                     ("rest-days-and-recovery", "Rest days and recovery")]
    arts = [art(s, ti, dek, b, ART_SOURCES[s], related_map[s])
            for (s, ti, dek, b) in FIT_ARTICLES]

    start_rows = ('<li><a href="/how-to-start-working-out/"><span><b>Starting from zero</b>'
                  "<small>The practical, no-miracle guide to beginning when the habit does not exist yet.</small></span>"
                  '<span class="meta">Start here</span></a></li>'
                  '<li><a href="/30-day-walking-plan/"><span><b>The 30-day walking plan</b>'
                  "<small>Show up every day for a month. Time-based, rest days built in, progress saved locally.</small></span>"
                  '<span class="meta">The plan</span></a></li>'
                  '<li><a href="/strength-training-for-beginners/"><span><b>Six moves, two days, no gym</b>'
                  "<small>The strength patterns that satisfy the guideline, scaled to a door and a backpack.</small></span>"
                  '<span class="meta">Build</span></a></li>')
    more_rows = ('<li><a href="/how-many-steps-a-day/"><span><b>How many steps a day actually matter?</b>'
                 "<small>Where 10,000 came from, what a 16,000-person study found, and the number to aim at instead.</small></span>"
                 '<span class="meta">Understand</span></a></li>'
                 '<li><a href="/rest-days-and-recovery/"><span><b>Rest days and recovery</b>'
                 "<small>Why adaptation happens between sessions \u2014 and when soreness is a warning.</small></span>"
                 '<span class="meta">Understand</span></a></li>')
    index_body = (head("fitness", "Practical fitness \u2014 no miracles, no medical claims.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Fitness</p>'
        + '<h1 class="cover-title">Build a routine you can actually keep.</h1>'
        + '<p class="cover-dek">Practical fitness guidance for people starting from zero: programs, challenges and progress \u2014 evidence-aware, beginner-first, and clearly separated from medical advice. No \u201cshred\u201d, no \u201cmelt fat\u201d, no 30-day body promises: 30-day <em>habits</em>.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Handpicked</p><h2>Start here.</h2></div>'
        + '<ul class="list">' + start_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Understand the craft</p><h2>Read before you push.</h2></div>'
        + '<ul class="list">' + more_rows + "</ul></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The desk\u2019s rules</p><h2>What BRYME Fitness will never do.</h2></div>'
        + '<div class="prose"><p>It will not promise a body in 30 days; it will not dress general information up as medical advice; it will not sell you equipment you do not need. Every guide carries its reviewed date and, where numbers are quoted, its sources. That is the whole identity: <b>practical fitness guidance, programs, challenges and progress</b> \u2014 sustainable on purpose.</p></div></section>'
        + "</div></main>" + foot("fitness"))
    pages = [("/", "BRYME Fitness \u2014 practical fitness, no miracle claims",
              "Beginner-first fitness: how to start, the 30-day walking plan with in-browser progress tracking, strength basics and recovery \u2014 evidence-aware, never medical advice.", index_body)]
    pages.extend(plan_page)
    pages.extend(arts)
    return pages + legal_pages("fitness", "BRYME Fitness", "Practical fitness guidance \u2014 responsible, evidence-aware, clearly separated from medical advice.")




# ------------------------------------------------------------------ 6. HOME & DIY
HOME_CHECK = [
    ("Water & drainage", "Run water in every unused sink, shower and floor drain",
     "Traps dry out and let sewer smells back in. A jug of water a month keeps the seal."),
    ("Water & drainage", "Look inside the cabinets under your sinks",
     "Damp rings, swollen board or a slow drip caught early is a five-minute fix, not a flood."),
    ("Safety devices", "Press the test button on your RCD / GFCI outlets",
     "The button exists so you can prove the protection works. If it does not trip, get it checked."),
    ("Safety devices", "Test your smoke alarms",
     "Fire services recommend testing monthly. Press the button; replace batteries on the schedule the maker states."),
    ("Safety devices", "Check the torch you keep for power cuts",
     "Batteries die quietly. Give it thirty seconds of light now, not darkness later."),
    ("Appliances", "Clean the coils behind or under your refrigerator",
     "Dust on coils makes the compressor work harder and run hotter. Unplug first, brush gently."),
    ("Appliances", "Inspect the washing machine hoses",
     "Bulges, cracks or weeping fittings on rubber hoses are how laundry rooms flood. Makers commonly advise replacing ageing hoses before they fail."),
    ("Appliances", "Descale the kettle and coffee machine",
     "Wherever water is hard, scale shortens appliance life and ruins the taste. Your maker\u2019s descaling guide beats any hack."),
    ("Seals & airflow", "Walk the windows and doors",
     "Daylight around a closed door or cracked sealant means lost heat/cooling and moisture where you do not want it."),
    ("Seals & airflow", "Vacuum vents, radiators and the dryer\u2019s full lint path",
     "Dryer lint beyond the filter is a known fire risk; blocked vents make everything work harder."),
]

HOME_SOURCES = [
    ("NFPA \u2014 smoke alarm safety (testing guidance)", "https://www.nfpa.org/education-and-research/home-fire-safety/smoke-alarms"),
    ("U.S. Fire Administration \u2014 dryer fire safety", "https://www.usfa.fema.gov/prevention/home-fires/prevent-hfires/dryers/"),
]

HOME_ARTICLES = [
    ("how-to-fix-a-slow-draining-sink",
     "How to fix a slow-draining sink, honestly",
     "What actually clears a slow sink (in order of effort), what is mostly theatre, and the point at which a plumber earns their fee.",
     """<p>A slow sink is almost always a partial blockage in the trap or the first metre of pipe: hair, soap, fat, or the slow accretion of all three. You rarely need chemicals and you never need panic. Work down this list and stop when the water runs.</p>
<h2>First: the honest physics</h2>
<p>Drain cleaners and home remedies get marketed hard. The honest order of effectiveness for a slow (not fully blocked) sink is mechanical: physically removing the gunk beats dissolving it, and dissolving beats hoping. Hot water alone is theatre for a genuine soap-fat clog, though it helps flush a cleared pipe.</p>
<h2>Step 1: the plunger, properly</h2>
<p>Block the overflow opening with a wet cloth (a basin has a small hole near the top; cover it or the plunger\u2019s pressure escapes there). Add enough water to cover the plunger\u2019s cup. Push and pull sharply for twenty to thirty seconds. Most slow sinks end here.</p>
<h2>Step 2: open the trap</h2>
<p>Under the sink is the U-bend (P-trap). Put a bucket under it, hand-loosen the slip nuts, and lift the trap off. Empty it. What you find inside is usually the entire story \u2014 a compacted plug of hair and soap. Rinse both directions, refit hand-tight, run hot water and check for drips before closing the cabinet. If the pipe from the wall also holds gunk, a plastic hand-crank drain snake costs little and reaches where fingers cannot.</p>
<h2>What about baking soda and vinegar?</h2>
<p>The famous fizz is mostly theatre for real blockages \u2014 it is a mild reaction, not a solvent. It will not harm anything, and it can freshen a smelly (rather than slow) drain, but do not let it replace the plunger and the trap.</p>
<h2>Chemicals: the safety boundary</h2>
<p>If you do use a caustic drain cleaner, follow the label exactly, ventilate, and never mix products \u2014 especially anything containing bleach with anything containing ammonia or acid; the reaction gases are genuinely dangerous. Chemicals also sit in the pipe, waiting for whoever opens the trap next. That is why this guide puts chemicals last, if at all.</p>
<h2>Call a plumber when</h2>
<p>Several fixtures drain slowly at once (the blockage is downstream, often in the main drain), water comes up in a different fixture when another drains, or the trap will not come apart because fittings are corroded or glued. Also call if there is sewage smell that a water top-up does not fix \u2014 a dried trap is a jug of water; a broken vent or seal is a professional.</p>
<h2>Prevention</h2>
<p>A mesh screen over the plug hole, fat into a jar rather than the sink, and a monthly kettle\u2019s worth of hot water down each drain. Three habits; zero emergencies. The <a href="/seasonal-home-maintenance-checklist/">once-a-season home checklist</a> includes the drain top-up.</p>"""),
    ("how-to-fix-a-dripping-tap",
     "A dripping tap (faucet), and what you can honestly fix yourself",
     "Why taps drip, the washer-and-cartridge reality behind most of them, and the ten-minute test that tells you whether it is your job or a plumber\u2019s.",
     """<p>A tap that drips once a second wastes more water over a month than most people expect, and the sound has driven stronger people than you to madness. The good news: the majority of dripping taps are a small, cheap, mechanical fix \u2014 provided you can turn the water off and tell the difference between the two most common tap insides.</p>
<h2>Before anything: the isolation test</h2>
<p>Find the shut-off valve for that tap (under the sink in most homes) and close it, or close the main if there is none. Open the tap to confirm the flow has stopped. No isolation valve and no main you can find? That is the professional\u2019s first visit, not yours.</p>
<h2>What kind of tap is it?</h2>
<p>Two families dominate. Traditional taps with a spindle you turn several times usually seal with a rubber washer and a seat \u2014 dripping when off, usually the washer. Modern single-lever or quarter-turn taps usually seal with a ceramic cartridge \u2014 dripping or failing to shut smoothly, usually the cartridge. Brand matters for parts: open nothing until you know the make, or plan to take the old part to a hardware shop as the specimen.</p>
<h2>The washer job, in one honest paragraph</h2>
<p>With water off: prise the decorative cap, unscrew the handle, unscrew the spindle with an adjustable spanner, and look at the end \u2014 a squashed, grooved or torn rubber washer is your culprit. Replace it with an identical size (take the old one shopping), check the seat it presses against is not scored, reassemble in reverse, reopen the water slowly. Ten to twenty minutes the first time.</p>
<h2>The cartridge job</h2>
<p>Same isolation, then the retaining clip or nut holds the cartridge. Cartridges are brand-specific parts \u2014 photograph the tap and its brand before buying. They swap in minutes once you hold the right part, and they are usually the only part that ever needs replacing on those taps.</p>
<h2>When it is not your job</h2>
<p>Water weeping from the tap body itself, corrosion that will not let fittings separate, no way to isolate the supply, or anything involving the pipes inside the wall: that is a plumber\u2019s territory. Paying for an hour of plumbing is cheaper than a flooded cabinet \u2014 see <a href="/how-to-fix-a-slow-draining-sink/">what lives inside sink cabinets</a> when they stay damp.</p>
<h2>Prevention, such as it is</h2>
<p>Taps wear from use, not neglect. What you can prevent is the collateral: close taps firmly but never forced \u2014 over-tightening chews washers faster. And once a season, glance at every tap\u2019s isolation valve; a valve that has not moved in years is the one that will seize. It is on the <a href="/seasonal-home-maintenance-checklist/">seasonal checklist</a>.</p>"""),
    ("why-does-my-circuit-breaker-keep-tripping",
     "Why your circuit breaker keeps tripping \u2014 and where DIY must stop",
     "What breakers actually protect you from, the safe way to narrow down the cause, and the hard boundary that separates a homeowner from an electrician.",
     """<p>A tripping breaker is not a malfunction. It is your electrical panel doing exactly its job: cutting power when the circuit is asked to carry more current than is safe, or when it detects a leak of current to earth. The nuisance is the clue. Read it correctly and it is one of the most useful signals in your home.</p>
<h2>The three usual causes</h2>
<p>Overload: too many things drawing power on one circuit \u2014 the kettle, heater and iron sharing one socket circuit, say. Short circuit: live and neutral touching somewhere they should not, often a damaged appliance, cable or plug \u2014 the trip is instant. Earth leak (the RCD/GFCI part of the protection): current escaping along a path it should not, often moisture or a failing appliance \u2014 these trips feel random and are the ones you must never ignore, because that protection exists to stop shocks.</p>
<h2>The safe way to narrow it down</h2>
<p>Unplug everything on the dead circuit. Reset the breaker firmly. If it holds: plug items back in one at a time, with a pause between each \u2014 the item that trips it again has named itself; retire or repair it. If it trips immediately with nothing plugged in, or trips repeatedly with everything unplugged, stop there. That is wiring, not appliances, and it is not a homeowner diagnosis.</p>
<h2>The reset, done properly</h2>
<p>Breakers trip to OFF or to a middle position. Push fully to OFF first, then to ON \u2014 resetting from the middle position is the classic reason a breaker \u201cwill not reset\u201d. One or two resets to diagnose is normal. A breaker you find yourself resetting weekly is telling you something is wrong; solving that by resetting harder is how problems escalate.</p>
<h2>The hard boundary</h2>
<p>Resetting a breaker and unplugging appliances: homeowner territory, do it today. Everything else \u2014 panel work, adding circuits, repeated trips with no load, burning smells, warm outlets, any work behind sockets \u2014 belongs to a qualified electrician. This page is general information, not electrical advice, and it deliberately stops at the panel cover. Electricity does not give second chances.</p>
<h2>Where this fits the house</h2>
<p>The <a href="/seasonal-home-maintenance-checklist/">once-a-season checklist</a> includes testing RCD/GFCI outlets and smoke alarms \u2014 the thirty seconds that prove the protective parts of your home still work.</p>"""),
    ("how-to-clean-a-washing-machine",
     "How to clean a washing machine (including the parts that actually cause the smell)",
     "Why machines smell and mark laundry, the gasket-and-filter truth behind it, and a maintenance rhythm that prevents both.",
     """<p>A washing machine that smells damp, or marks clean clothes with grey streaks, is not broken. It is dirty in the three specific places detergent residue and water sit long enough to grow things: the door gasket, the detergent drawer, and the filter. Cleaning those beats every scented product marketed to mask the problem.</p>
<h2>The gasket is the crime scene</h2>
<p>On front loaders, fold back the rubber door gasket and look: black speckles, slime, the odd lost sock. Wipe it out with a cloth and warm soapy water, getting into the folds. Leave the door and drawer ajar between washes so the inside dries \u2014 sealed-in moisture is what grows the smell in the first place.</p>
<h2>The detergent drawer slides out</h2>
<p>Most drawers release fully with a press of a recessed clip (your manual shows where, or the internet knows your model). Wash it under the tap with an old toothbrush; check the jet holes above where it sits and clear the residue that blocks rinse water.</p>
<h2>The filter you have been avoiding</h2>
<p>Behind a small hatch near the floor lives the drain filter \u2014 the place coins, hair clips and lint go to retire. Put a shallow tray or towel down, open it slowly (water will come), remove and rinse the filter, and screw it back snugly. Once a season is the honest rhythm; more if you have pets or small humans.</p>
<h2>Hot wash, occasionally</h2>
<p>Cold-wash habits let grease and residue accumulate. A monthly hot cycle \u2014 empty, with a maker-approved cleaner or plain washing soda per its instructions \u2014 flushes the tub and the pipes behind it. Skip the folk chemistry; heat does the work.</p>
<h2>Prevention rhythm</h2>
<p>Door ajar after washes; drawer ajar; filter each season; a monthly hot cycle; and measure detergent honestly \u2014 most people use far more than the machine needs, and the surplus is what rots. All of this except the hot cycle is on the <a href="/seasonal-home-maintenance-checklist/">once-a-season checklist</a>.</p>"""),
    ("fridge-not-cold-enough",
     "Fridge not cold enough? Five checks before you pay for a repair",
     "The settings, airflow and coil checks that fix most \u201cwarm fridge\u201d calls, and the signs that say it really is a technician\u2019s problem.",
     """<p>A fridge that runs but does not quite cool is one of the most common \u201crepair\u201d calls \u2014 and a decent share of them are fixed in ten minutes with no parts. Work these checks in order; stop and call a technician the moment the path says so.</p>
<h2>1. The thermostat, honestly</h2>
<p>Dials marked 1\u20135 say nothing absolute; the manual says which end is colder. Confirm the setting first \u2014 dials get nudged by grocery bags. A fridge thermometer (cheap, honest) beats any built-in dial: you want roughly at or below 4\u00b0C / 40\u00b0F on the shelf, freezer around \u201318\u00b0C / 0\u00b0F.</p>
<h2>2. Airflow inside</h2>
<p>Cold air travels through vents between freezer and fridge. Boxes jammed against the back wall and vents blocked by a bag of peas mimic a failing fridge. Create space; let air move.</p>
<h2>3. The door seal test</h2>
<p>Close the door on a piece of paper; if it slides out with no resistance at several points, the gasket is not sealing and cold air leaks out. Clean sticky residue off the gasket; a perished or torn one is a replaceable part on most models \u2014 cheaper than a new fridge.</p>
<h2>4. The coils you never see</h2>
<p>Unplug the fridge, find the coils (behind the kick plate or on the back), and brush/vacuum the dust blanket off. Coils choked with dust shed heat poorly and the cabinet warms. This is the single most common neglected maintenance on kitchen appliances \u2014 it is on the <a href="/seasonal-home-maintenance-checklist/">seasonal checklist</a> for that reason.</p>
<h2>5. Give it time, then listen</h2>
<p>After any change, give the fridge several hours with the door kept closed. Then listen: a compressor that clicks on and off every few minutes, or hums constantly without cooling, is failing \u2014 and that, along with frost patterns that suggest a defrost-system fault, is genuinely a technician\u2019s job. Refrigerant and sealed systems are not DIY, full stop.</p>
<h2>When you call, say this</h2>
<p>\u201cCompressor runs continuously, cabinet at 10\u00b0C, coils cleaned, seal tested\u201d gets a better visit than \u201cit\u2019s warm\u201d \u2014 and sometimes a better answer: knowing the checks were done may save you the call-out entirely.</p>"""),
]

HOME_SECTIONS = [
    ("fix", "Fix it", "Household problems and beginner repairs, honestly ordered."),
    ("maintain", "Maintain it", "Preventive care, and the kit that does it."),
    ("appliances", "Appliances", "Keep the machines honest."),
    ("understand", "Understand it", "What the symptoms actually mean."),
    ("outside", "Outside", "Gutters, grills, sheds and the seasons \u2014 the half of the house that faces the weather."),
    ("pests", "Pests", "Unwelcome guests \u2014 prevention, honest decisions, and the aftercare that makes treatment work."),
    ("secure", "Secure it", "Doors, windows, locks and the nightly habits that make a house a hard target."),
    ("owning", "Owning it", "Moving in, budgets, insurance, responsibility and value \u2014 the owner\u2019s ledger."),
    ("mistakes", "Common mistakes", "The errors most homes make - and the fixes."),
]
HOME_SLUG_SECT = {
    "how-to-fix-a-slow-draining-sink": "fix",
    "how-to-fix-a-dripping-tap": "fix",
    "how-to-unblock-a-toilet": "fix",
    "how-to-bleed-a-radiator": "maintain",
    "basic-toolkit-checklist": "maintain",
    "how-to-clean-a-washing-machine": "appliances",
    "washing-machine-wont-drain": "appliances",
    "why-does-my-circuit-breaker-keep-tripping": "understand",
    "fridge-not-cold-enough": "understand",
}
HOME_SLUG_SECT.update({s: "appliances" for s in (
    "washing-machine-heavy-items", "dryer-lint-every-load", "dishwasher-loading-mistakes",
    "stop-pre-rinsing-dishes", "vinegar-in-the-dishwasher", "fridge-coils-twice-a-year",
    "fridge-door-seal-test", "garbage-disposal-mistakes", "induction-hob-wiring",
    "smart-appliances-worth-it")})

HOME_SLUG_SECT.update({s: "understand" for s in (
    "uk-carbon-monoxide-alarm-law", "how-many-smoke-co-alarms", "co-smoke-alarm-expiry",
    "condensation-vs-rising-vs-penetrating-damp", "uk-landlord-damp-mould-duties",
    "gas-heaters-damp")})
HOME_SLUG_SECT.update({s: "maintain" for s in (
    "test-alarms-monthly", "condensation-ventilation-that-works")})

HOME_SLUG_SECT.update({s: "maintain" for s in (
    "hvac-filter-change-habit", "uk-boiler-servicing", "ac-outdoor-unit-care")})
HOME_SLUG_SECT.update({s: "understand" for s in (
    "hvac-noises-decoded", "hvac-diy-warranty-rules", "uk-us-plumber-rules")})
HOME_SLUG_SECT.update({s: "fix" for s in (
    "small-leak-ripple-effect", "leaky-faucet-diy")})

HOME_SLUG_SECT.update({s: "fix" for s in (
    "interior-painting-mistakes", "humidity-and-paint", "painting-over-damp")})
HOME_SLUG_SECT.update({s: "understand" for s in (
    "electrical-fire-warning-signs", "outlet-overloading-danger")})

HOME_SLUG_SECT.update({s: "understand" for s in (
    "us-home-permits", "building-regs-vs-planning-permission", "unpermitted-work-home-sale",
    "part-p-explained", "us-diy-electrical-rules")})

HOME_SLUG_SECT.update({s: "outside" for s in (
    "gutter-cleaning-damage", "fence-shed-insurance", "outdoor-cooking-safety",
    "inspection-checklist-gaps")})
HOME_SLUG_SECT.update({s: "maintain" for s in (
    "draught-proofing-mistakes", "wet-mop-floor-warranty", "deep-clean-schedule")})
HOME_SLUG_SECT.update({s: "understand" for s in (
    "single-glazing-payback", "underfloor-heating-mistakes")})

HOME_SLUG_SECT.update({s: "pests" for s in (
    "clean-home-pests-myth", "ignore-single-pest-sighting", "moving-cardboard-pests",
    "after-pest-treatment", "diy-vs-professional-pests")})
HOME_SLUG_SECT.update({s: "fix" for s in ("bathroom-remodel-mistakes",)})
HOME_SLUG_SECT.update({s: "maintain" for s in (
    "kitchen-ventilation-damp", "grout-sealant-neglect")})

HOME_SLUG_SECT.update({s: "understand" for s in (
    "energy-bill-high-unchanged", "smart-thermostat-payback")})
HOME_SLUG_SECT.update({s: "maintain" for s in ("uk-insulation-grants",)})
HOME_SLUG_SECT.update({s: "secure" for s in (
    "entry-point-mistakes", "smart-locks-cameras-worth-it", "renter-security")})

HOME_SLUG_SECT.update({s: "owning" for s in (
    "pre-move-inspection", "moving-week-by-week", "secondhand-furniture-mistakes",
    "emergency-repair-fund", "someday-maintenance-cost", "unpermitted-work-insurance",
    "renter-vs-owner-repairs", "improvements-no-resale-value")})


def _home_theme_init():
    # External file: the site CSP is script-src 'self' - inline scripts never run.
    # Loaded blocking in <head> so the theme applies before first paint (no flash).
    return '<script src="/assets/home-theme.js"></script>'

def _home_toggle_js():
    # wiring lives in /assets/home-theme.js (CSP: script-src self)
    return ""

def _home_mast():
    return ('<header class="head"><div class="wrap mast">'
            '<a class="mast-brand" href="/home/">BRYME&nbsp;<span>HOME &amp; DIY</span></a>'
            '<span class="mast-tag">Fix it. Clean it. Maintain it. Understand it.</span>'
            '<button type="button" class="theme-btn" id="home-theme" aria-pressed="false" aria-label="Toggle dark mode" title="Toggle dark mode">&#9789;</button>'
            '</div></header>')

def _home_sidebar(current):
    import home_mistakes_data
    counts = {}
    for s in HOME_SLUG_SECT.values():
        counts[s] = counts.get(s, 0) + 1

    def a(href, label, key, n=None, flag=False):
        cls = ""
        if key == current:
            cls = 'active'
        if flag:
            cls += ' flag'
        cls_attr = ' class="' + cls.strip() + '"' if cls else ''
        nn = '<span class="n">' + str(n) + '</span>' if n is not None else ''
        return '<a' + cls_attr + ' href="' + href + '">' + label + nn + '</a>'

    items = (a("/home/", "Desk home", "home")
        + a("/home/fix/", "Fix it", "fix", counts.get("fix", 0))
        + a("/home/maintain/", "Maintain it", "maintain", counts.get("maintain", 0))
        + a("/home/appliances/", "Appliances", "appliances", counts.get("appliances", 0))
        + a("/home/understand/", "Understand it", "understand", counts.get("understand", 0))
        + a("/home/mistakes/", "Common mistakes", "mistakes", len(home_mistakes_data.HOME_MISTAKES), True)
        + a("/home/seasonal-home-maintenance-checklist/", "The seasonal checklist", "checklist", None, True))
    return ('<aside class="h-side"><p class="h-side-title">The desk</p>'
            '<nav aria-label="Home and DIY sections">' + items + "</nav></aside>")

def _home_page(title, desc, route, cover_html, main_html, sidebar_current):
    canonical = ORIGIN + "/home" + route
    og = "https://" + DOMAIN + "/assets/og.png"
    return ('<!doctype html>\n<html lang="en"><head>\n'
        '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>" + html.escape(title) + "</title>\n"
        '<meta name="description" content="' + html.escape(desc) + '">\n'
        '<meta name="robots" content="index,follow">\n'
        '<link rel="canonical" href="' + canonical + '">\n'
        '<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">\n'
        '<meta property="og:title" content="' + html.escape(title) + '"><meta property="og:description" content="' + html.escape(desc) + '">\n'
        '<meta property="og:url" content="' + canonical + '"><meta property="og:image" content="' + og + '">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        + _home_theme_init() + "\n<style>" + css_for("home") + "</style>\n</head>"
        '<body><a class="skip-link" href="#main">Skip to content</a>\n'
        + _home_mast()
        + '<div class="wrap h-layout">' + _home_sidebar(sidebar_current)
        + '<main id="main" class="h-main">' + cover_html + main_html + "</main></div>\n"
        + foot("home") + "\n" + _home_toggle_js() + "</body></html>")

def home_pages():
    import home_mistakes_data
    import more_guides_data
    _mset = {m2[0] for m2 in home_mistakes_data.HOME_MISTAKES}
    def _hurl(s):
        return ("/home/mistakes/" + s + "/") if s in _mset else ("/home/" + s + "/")
    _have = {s2[0] for s2 in HOME_ARTICLES}
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in more_guides_data.HOME_MORE if s2 not in _have)
    import home_roadmap_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap_data.HOME_ROADMAP if s2 not in _have)
    import home_roadmap2_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap2_data.HOME_ROADMAP_2 if s2 not in _have)
    import home_roadmap3_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap3_data.HOME_ROADMAP_3 if s2 not in _have)
    import home_roadmap4_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap4_data.HOME_ROADMAP_4 if s2 not in _have)
    import home_roadmap5_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap5_data.HOME_ROADMAP_5 if s2 not in _have)
    import home_roadmap6_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap6_data.HOME_ROADMAP_6 if s2 not in _have)
    import home_roadmap7_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap7_data.HOME_ROADMAP_7 if s2 not in _have)
    import home_roadmap8_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap8_data.HOME_ROADMAP_8 if s2 not in _have)
    import home_roadmap9_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap9_data.HOME_ROADMAP_9 if s2 not in _have)

    def src_html(sources):
        if not sources:
            return ""
        return ('<h2>Sources</h2><ul class="list">'
                + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                + "</ul>")

    def band(text):
        return ('<section class="section alt" style="border-left:4px solid var(--brand)"><div class="wrap"><p class="lede">'
                + text + "</p></div></section>")

    DISCLAIMER = band("<b>General information, not professional advice.</b> Homes differ \u2014 if a job is beyond your confidence or the guide\u2019s boundary, that is what tradespeople are for.")
    SAFETY = band("<b>Safety boundary.</b> Electrical panel work, gas, structural changes and anything at height belong to qualified professionals. Every guide here stops where that line starts.")

    def sec_label(key):
        for k2, l2, _d in HOME_SECTIONS:
            if k2 == key:
                return l2
        return key

    out = []

    # ---------- index ----------
    mistake_rows = []
    mistake_pages = []
    for n2, (slug, theme, mtitle, one_liner, mbody, sources, related) in enumerate(home_mistakes_data.HOME_MISTAKES, 1):
        mistake_rows.append('<li><a href="/mistakes/' + slug + '/"><span><b>' + html.escape(mtitle) + "</b><small>"
                            + html.escape(one_liner) + "</small></span>"
                            '<span class="meta">' + html.escape(theme) + "</span></a></li>")
        rel_html = "".join('<li><a href="' + _hurl(s) + '">' + rt + "</a></li>" for s, rt in related)
        mcover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / '
                  '<a href="/home/mistakes/">Common mistakes</a> / ' + html.escape(mtitle) + "</nav>"
            + '<section class="cover"><p class="kicker">Common mistake ' + str(n2) + ' of ' + str(len(home_mistakes_data.HOME_MISTAKES)) + " \u00b7 " + html.escape(theme) + "</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.8vw,52px)">' + html.escape(mtitle) + "</h1>"
            + '<p class="byline">BRYME Home &amp; DIY desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not professional advice</p></section>")
        mmain = ('<section class="section alt"><div class="wrap"><p class="lede"><b>The mistake:</b> ' + html.escape(one_liner) + "</p></div></section>"
            + '<section class="section"><div class="prose">' + mbody + src_html(sources) + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/home/mistakes/">All common mistakes</a>'
            + '<a class="btn secondary" href="/home/">Desk home</a></div></section>'
            + DISCLAIMER)
        mistake_pages.append(("/mistakes/" + slug + "/", mtitle + " | BRYME Home & DIY", one_liner[:155],
                              _home_page(mtitle + " | BRYME Home & DIY", one_liner[:155], "/mistakes/" + slug + "/", mcover, mmain, "mistakes")))

    icover = ('<section class="cover"><p class="kicker">BRYME Home &amp; DIY</p>'
        + '<h1 class="cover-title">Fix it. Clean it. Maintain it. Understand it.</h1>'
        + '<p class="cover-dek">Practical help for the problems every household hits \u2014 written for low-risk work, with the boundaries stated plainly: electrical panels, gas, structure and height belong to qualified professionals, and every guide here says exactly where that line is.</p></section>')
    sec_cards = "".join(
        '<div class="h-sec-card"><p class="kicker" style="margin:0">'
        + str(len([s2 for s2, k2 in HOME_SLUG_SECT.items() if k2 == key]) if key != "mistakes" else len(home_mistakes_data.HOME_MISTAKES))
        + " PIECES</p><h3>" + label + "</h3><p>" + sdek + '</p><a class="btn secondary" style="margin-top:12px" href="/home/' + key + '/">Open ' + label + "</a></div>"
        for key, label, sdek in HOME_SECTIONS)
    imain = ('<section class="section"><div class="section-head"><p class="kicker">Start with the classics</p><h2>The common mistakes shelf.</h2></div>'
        + '<ul class="list">' + "".join(mistake_rows[:4]) + "</ul>"
        + '<div class="actions"><a class="btn" href="/home/mistakes/">All ' + str(len(home_mistakes_data.HOME_MISTAKES)) + " common mistakes</a></div></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Browse the desk</p><h2>Sections.</h2></div>'
        + '<div class="h-sec-grid">' + sec_cards + "</div></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The product</p><h2>The once-a-season checklist.</h2></div>'
        + '<div class="prose"><p><a href="/seasonal-home-maintenance-checklist/"><b>The once-a-season home checklist</b></a> \u2014 ten checks across water, safety devices, appliances and airflow, with progress your browser remembers. Homes fail slowly, then suddenly; this catches the slow part.</p></div></section>'
        + SAFETY)
    out.append(("/", "BRYME Home & DIY \u2014 fix, clean, maintain, understand",
                "Low-risk home repairs and maintenance, honestly explained \u2014 with sections, a common-mistakes shelf and the once-a-season checklist.",
                _home_page("BRYME Home & DIY \u2014 fix, clean, maintain, understand",
                           "Low-risk home repairs and maintenance, honestly explained.", "/",
                           icover, imain, "home")))

    # ---------- section pages ----------
    data_by_slug = {s2[0]: s2 for s2 in HOME_ARTICLES}
    for key, label, sdek in HOME_SECTIONS:
        if key == "mistakes":
            continue
        slugs = [s for s, k2 in HOME_SLUG_SECT.items() if k2 == key]
        rows = ""
        for s in slugs:
            _s2, ti, dek, _b = data_by_slug[s]
            rows += ('<li><a href="' + _hurl(s) + '"><span><b>' + html.escape(ti) + "</b><small>" + html.escape(dek) + "</small></span>"
                     '<span class="meta">Guide</span></a></li>')
        others = "".join('<a class="btn secondary" href="/home/' + k2 + '/">' + l2 + "</a>"
                         for k2, l2, _d in HOME_SECTIONS if k2 != key)
        cover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / ' + label + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Home &amp; DIY \u00b7 section</p>'
            + '<h1 class="cover-title">' + label + "</h1>"
            + '<p class="cover-dek">' + sdek + "</p></section>")
        main = ('<section class="section"><div class="section-head"><p class="kicker">' + str(len(slugs)) + ' guides</p><h2>Everything in ' + label + '.</h2></div>'
            + '<ul class="list">' + rows + "</ul>"
            + '<div class="actions">' + others
            + '<a class="btn secondary" href="/home/">Desk home</a></div></section>')
        out.append(("/" + key + "/", label + " | BRYME Home & DIY", sdek,
                    _home_page(label + " | BRYME Home & DIY", sdek, "/" + key + "/", cover, main, key)))

    # ---------- mistakes hub ----------
    mcover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / Common mistakes</nav>'
        + '<section class="cover"><p class="kicker">The most-visited shelf on this desk</p>'
        + '<h1 class="cover-title">Common mistakes, and how to fix them.</h1>'
        + '<p class="cover-dek">The errors most homes make \u2014 with too much soap, the wrong cleaner combo, a watering can on a schedule, a drill in the dark. Every piece follows the same honest shape: the mistake, why it backfires, the fix, and how to keep it from happening again.</p></section>')
    mmain = ('<section class="section"><div class="section-head"><p class="kicker">'
             + str(len(home_mistakes_data.HOME_MISTAKES)) + ' mistakes, no shaming</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + "".join(mistake_rows) + "</ul></section>"
        + SAFETY)
    out.append(("/mistakes/", "Common home mistakes \u2014 and how to fix them | BRYME Home & DIY",
                "The errors most homes make: too much detergent, mixed cleaners, overwatering, blind drilling \u2014 why they backfire and the honest fixes.",
                _home_page("Common home mistakes \u2014 and how to fix them | BRYME Home & DIY",
                           "The errors most homes make, why they backfire and the honest fixes.", "/mistakes/",
                           mcover, mmain, "mistakes")))
    out.extend(mistake_pages)

    # ---------- guides ----------
    related_map = {
        "how-to-fix-a-slow-draining-sink": [("how-to-unblock-a-toilet", "The blocked toilet"),
                                            ("how-to-fix-a-dripping-tap", "A dripping tap, fixed honestly"),
                                            ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "how-to-fix-a-dripping-tap": [("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                      ("basic-toolkit-checklist", "The basic toolkit"),
                                      ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "how-to-unblock-a-toilet": [("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                    ("basic-toolkit-checklist", "The basic toolkit"),
                                    ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "how-to-bleed-a-radiator": [("basic-toolkit-checklist", "The basic toolkit"),
                                    ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                    ("washing-machine-wont-drain", "The machine that won't drain")],
        "basic-toolkit-checklist": [("how-to-bleed-a-radiator", "Bleeding a radiator"),
                                    ("drilling-without-checking", "Drilling without checking"),
                                    ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker")],
        "how-to-clean-a-washing-machine": [("washing-machine-wont-drain", "The machine that won't drain"),
                                           ("too-much-detergent", "Too much detergent"),
                                           ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "washing-machine-wont-drain": [("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                       ("fridge-not-cold-enough", "Fridge not cold enough"),
                                       ("basic-toolkit-checklist", "The basic toolkit")],
        "why-does-my-circuit-breaker-keep-tripping": [("drilling-without-checking", "Drilling without checking"),
                                                      ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                                      ("fridge-not-cold-enough", "Fridge not cold enough")],
        "fridge-not-cold-enough": [("overloading-the-fridge", "Packing the fridge solid"),
                                   ("washing-machine-wont-drain", "The machine that won't drain"),
                                   ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker")],
        "washing-machine-heavy-items": [("washing-machine-wont-drain", "The machine that won't drain"),
                                        ("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                        ("too-much-detergent", "Too much detergent")],
        "dryer-lint-every-load": [("washing-machine-heavy-items", "The load that kills machines"),
                                  ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                  ("basic-toolkit-checklist", "The basic toolkit")],
        "dishwasher-loading-mistakes": [("stop-pre-rinsing-dishes", "Skip the pre-rinse"),
                                        ("vinegar-in-the-dishwasher", "Not with vinegar"),
                                        ("too-much-detergent", "Too much detergent")],
        "stop-pre-rinsing-dishes": [("dishwasher-loading-mistakes", "Load it so it cleans"),
                                    ("vinegar-in-the-dishwasher", "Not with vinegar"),
                                    ("too-much-detergent", "Too much detergent")],
        "vinegar-in-the-dishwasher": [("dishwasher-loading-mistakes", "Load it so it cleans"),
                                      ("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                      ("mistakes/mixing-cleaning-products", "Never mix cleaners")],
        "fridge-coils-twice-a-year": [("fridge-door-seal-test", "The dollar-bill seal test"),
                                      ("fridge-not-cold-enough", "Fridge not cold enough"),
                                      ("overloading-the-fridge", "Packing the fridge solid")],
        "fridge-door-seal-test": [("fridge-coils-twice-a-year", "Clean the coils twice a year"),
                                  ("fridge-not-cold-enough", "Fridge not cold enough"),
                                  ("overloading-the-fridge", "Packing the fridge solid")],
        "garbage-disposal-mistakes": [("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                      ("how-to-unblock-a-toilet", "The blocked toilet"),
                                      ("basic-toolkit-checklist", "The basic toolkit")],
        "induction-hob-wiring": [("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                 ("drilling-without-checking", "Drilling without checking"),
                                 ("basic-toolkit-checklist", "The basic toolkit")],
        "smart-appliances-worth-it": [("fridge-coils-twice-a-year", "Clean the coils twice a year"),
                                      ("washing-machine-heavy-items", "The load that kills machines"),
                                      ("dishwasher-loading-mistakes", "Load it so it cleans")],
        "uk-carbon-monoxide-alarm-law": [("co-alarm-wrong-place", "The CO alarm that can't work"),
                                         ("co-smoke-alarm-expiry", "The expiry date nobody reads"),
                                         ("how-many-smoke-co-alarms", "How many alarms you need")],
        "how-many-smoke-co-alarms": [("uk-carbon-monoxide-alarm-law", "UK CO alarm law"),
                                     ("co-smoke-alarm-expiry", "The expiry date nobody reads"),
                                     ("test-alarms-monthly", "The monthly alarm habit")],
        "co-smoke-alarm-expiry": [("co-alarm-wrong-place", "The CO alarm that can't work"),
                                  ("test-alarms-monthly", "The monthly alarm habit"),
                                  ("how-many-smoke-co-alarms", "How many alarms you need")],
        "test-alarms-monthly": [("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                ("dryer-lint-every-load", "The dryer lint habit"),
                                ("co-smoke-alarm-expiry", "The expiry date nobody reads")],
        "condensation-vs-rising-vs-penetrating-damp": [("condensation-ventilation-that-works", "Ventilation that works"),
                                                       ("uk-landlord-damp-mould-duties", "Landlord damp duties"),
                                                       ("drying-laundry-indoors", "Drying laundry indoors")],
        "uk-landlord-damp-mould-duties": [("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                          ("condensation-ventilation-that-works", "Ventilation that works"),
                                          ("gas-heaters-damp", "Gas heat and damp")],
        "condensation-ventilation-that-works": [("drying-laundry-indoors", "Drying laundry indoors"),
                                                ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                                ("gas-heaters-damp", "Gas heat and damp")],
        "gas-heaters-damp": [("co-alarm-wrong-place", "The CO alarm that can't work"),
                             ("uk-carbon-monoxide-alarm-law", "UK CO alarm law"),
                             ("condensation-ventilation-that-works", "Ventilation that works")],
        "hvac-filter-change-habit": [("ac-outdoor-unit-care", "The outdoor unit"),
                                     ("hvac-diy-warranty-rules", "DIY, warranty and the law"),
                                     ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "hvac-noises-decoded": [("hvac-diy-warranty-rules", "DIY, warranty and the law"),
                                ("hvac-filter-change-habit", "The filter habit"),
                                ("uk-boiler-servicing", "The annual boiler service")],
        "hvac-diy-warranty-rules": [("hvac-filter-change-habit", "The filter habit"),
                                    ("uk-boiler-servicing", "The annual boiler service"),
                                    ("mistakes/co-alarm-wrong-place", "The CO alarm that can't work")],
        "uk-boiler-servicing": [("uk-carbon-monoxide-alarm-law", "UK CO alarm law"),
                                ("co-smoke-alarm-expiry", "The expiry date nobody reads"),
                                ("gas-heaters-damp", "Gas heat and damp")],
        "ac-outdoor-unit-care": [("hvac-filter-change-habit", "The filter habit"),
                                 ("hvac-noises-decoded", "HVAC noises decoded"),
                                 ("fridge-coils-twice-a-year", "Clean the coils twice a year")],
        "small-leak-ripple-effect": [("leaky-faucet-diy", "Fix the dripping tap"),
                                     ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                     ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "leaky-faucet-diy": [("small-leak-ripple-effect", "Why small leaks never stay small"),
                             ("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                             ("basic-toolkit-checklist", "The basic toolkit")],
        "uk-us-plumber-rules": [("leaky-faucet-diy", "Fix the dripping tap"),
                                ("induction-hob-wiring", "Induction wiring rules"),
                                ("uk-boiler-servicing", "The annual boiler service")],
        "interior-painting-mistakes": [("mistakes/painting-without-prep", "Skipping prep"),
                                       ("humidity-and-paint", "Humidity and paint"),
                                       ("painting-over-damp", "Painting over damp")],
        "humidity-and-paint": [("interior-painting-mistakes", "The full painting mistakes list"),
                               ("condensation-ventilation-that-works", "Ventilation that works"),
                               ("painting-over-damp", "Painting over damp")],
        "painting-over-damp": [("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                               ("uk-landlord-damp-mould-duties", "Landlord damp duties"),
                               ("humidity-and-paint", "Humidity and paint")],
        "electrical-fire-warning-signs": [("outlet-overloading-danger", "The overloaded outlet"),
                                          ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                          ("how-many-smoke-co-alarms", "How many alarms you need")],
        "outlet-overloading-danger": [("electrical-fire-warning-signs", "The warning signs"),
                                      ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                      ("mistakes/drilling-without-checking", "Drilling without checking")],
        "us-home-permits": [("unpermitted-work-home-sale", "When unpermitted work resurfaces"),
                            ("us-diy-electrical-rules", "US DIY electrical rules"),
                            ("hvac-diy-warranty-rules", "DIY, warranty and the law")],
        "building-regs-vs-planning-permission": [("part-p-explained", "Part P explained"),
                                                 ("unpermitted-work-home-sale", "When unpermitted work resurfaces"),
                                                 ("uk-us-plumber-rules", "UK vs US plumbing rules")],
        "unpermitted-work-home-sale": [("building-regs-vs-planning-permission", "Building Regs vs planning"),
                                       ("us-home-permits", "US permit basics"),
                                       ("part-p-explained", "Part P explained")],
        "part-p-explained": [("induction-hob-wiring", "Induction wiring rules"),
                             ("outlet-overloading-danger", "The overloaded outlet"),
                             ("building-regs-vs-planning-permission", "Building Regs vs planning")],
        "us-diy-electrical-rules": [("outlet-overloading-danger", "The overloaded outlet"),
                                    ("electrical-fire-warning-signs", "The warning signs"),
                                    ("us-home-permits", "US permit basics")],
        "gutter-cleaning-damage": [("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                   ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                   ("small-leak-ripple-effect", "Why small leaks never stay small")],
        "fence-shed-insurance": [("small-leak-ripple-effect", "Sudden vs gradual damage"),
                                 ("us-home-permits", "US permit basics"),
                                 ("building-regs-vs-planning-permission", "Building Regs vs planning"),
                                 ("outlet-overloading-danger", "The overloaded outlet")],
        "outdoor-cooking-safety": [("test-alarms-monthly", "The monthly alarm habit"),
                                   ("mistakes/co-alarm-wrong-place", "The CO alarm that can't work"),
                                   ("electrical-fire-warning-signs", "The warning signs")],
        "inspection-checklist-gaps": [("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                      ("small-leak-ripple-effect", "The meter test"),
                                      ("condensation-ventilation-that-works", "Ventilation that works")],
        "draught-proofing-mistakes": [("condensation-ventilation-that-works", "Ventilation that works"),
                                      ("single-glazing-payback", "The single-glazing maths"),
                                      ("uk-boiler-servicing", "The annual boiler service")],
        "single-glazing-payback": [("draught-proofing-mistakes", "Draught-proofing, done right"),
                                   ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                   ("interior-painting-mistakes", "The painting mistakes list")],
        "wet-mop-floor-warranty": [("underfloor-heating-mistakes", "Underfloor heating mistakes"),
                                   ("unpermitted-work-home-sale", "Paperwork wins arguments"),
                                   ("smart-appliances-worth-it", "Smart appliances, honestly")],
        "underfloor-heating-mistakes": [("wet-mop-floor-warranty", "The floor-warranty rules"),
                                        ("mistakes/drilling-without-checking", "Drilling without checking"),
                                        ("condensation-ventilation-that-works", "Ventilation that works")],
        "deep-clean-schedule": [("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                ("vinegar-in-the-dishwasher", "Not with vinegar"),
                                ("mistakes/streaky-windows-sunlight", "Streaky windows in sunlight")],
        "clean-home-pests-myth": [("ignore-single-pest-sighting", "The one-sighting protocol"),
                                  ("moving-cardboard-pests", "Boxes are pest vehicles"),
                                  ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "ignore-single-pest-sighting": [("diy-vs-professional-pests", "DIY vs professional"),
                                        ("clean-home-pests-myth", "The clean-home myth"),
                                        ("small-leak-ripple-effect", "Why small leaks never stay small")],
        "moving-cardboard-pests": [("clean-home-pests-myth", "The clean-home myth"),
                                   ("ignore-single-pest-sighting", "The one-sighting protocol"),
                                   ("diy-vs-professional-pests", "DIY vs professional")],
        "after-pest-treatment": [("diy-vs-professional-pests", "DIY vs professional"),
                                 ("mistakes/mixing-cleaning-products", "Never mix cleaning products"),
                                 ("deep-clean-schedule", "The deep-clean rotation")],
        "diy-vs-professional-pests": [("after-pest-treatment", "After the treatment"),
                                      ("ignore-single-pest-sighting", "The one-sighting protocol"),
                                      ("clean-home-pests-myth", "The clean-home myth")],
        "bathroom-remodel-mistakes": [("grout-sealant-neglect", "Grout and sealant care"),
                                      ("condensation-ventilation-that-works", "Ventilation that works"),
                                      ("part-p-explained", "Part P explained")],
        "kitchen-ventilation-damp": [("condensation-ventilation-that-works", "Ventilation that works"),
                                     ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                     ("induction-hob-wiring", "Induction wiring rules")],
        "grout-sealant-neglect": [("bathroom-remodel-mistakes", "Before you remodel"),
                                  ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                  ("small-leak-ripple-effect", "Why small leaks never stay small")],
        "energy-bill-high-unchanged": [("uk-insulation-grants", "What the government funds"),
                                       ("smart-thermostat-payback", "The thermostat maths"),
                                       ("fridge-coils-twice-a-year", "Clean the coils twice a year")],
        "uk-insulation-grants": [("energy-bill-high-unchanged", "Why bills rise anyway"),
                                 ("condensation-ventilation-that-works", "Ventilate what you insulate"),
                                 ("single-glazing-payback", "The window maths")],
        "smart-thermostat-payback": [("energy-bill-high-unchanged", "Why bills rise anyway"),
                                     ("uk-boiler-servicing", "The annual boiler service"),
                                     ("uk-insulation-grants", "Insulation help, dated")],
        "entry-point-mistakes": [("smart-locks-cameras-worth-it", "Smart locks & cameras"),
                                 ("fence-shed-insurance", "Insurance small print"),
                                 ("test-alarms-monthly", "The monthly alarm habit")],
        "smart-locks-cameras-worth-it": [("entry-point-mistakes", "The entry-point list"),
                                         ("smart-appliances-worth-it", "Smart appliances, honestly"),
                                         ("renter-security", "Security for renters")],
        "renter-security": [("entry-point-mistakes", "The entry-point list"),
                            ("smart-locks-cameras-worth-it", "Smart locks & cameras"),
                            ("uk-landlord-damp-mould-duties", "Report it in writing")],
        "pre-move-inspection": [("moving-week-by-week", "The week-by-week plan"),
                                ("inspection-checklist-gaps", "What gets missed"),
                                ("small-leak-ripple-effect", "The meter test")],
        "moving-week-by-week": [("pre-move-inspection", "The day-one inspection"),
                                ("moving-cardboard-pests", "Boxes are pest vehicles"),
                                ("deep-clean-schedule", "The deep-clean rotation")],
        "secondhand-furniture-mistakes": [("moving-cardboard-pests", "The moving-box risk"),
                                          ("ignore-single-pest-sighting", "The one-sighting protocol"),
                                          ("smart-appliances-worth-it", "Buy for the long term")],
        "emergency-repair-fund": [("someday-maintenance-cost", "The cost of someday"),
                                  ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                  ("uk-boiler-servicing", "The annual boiler service")],
        "someday-maintenance-cost": [("small-leak-ripple-effect", "Why leaks never stay small"),
                                     ("grout-sealant-neglect", "The five-pound tube"),
                                     ("emergency-repair-fund", "The repair fund")],
        "unpermitted-work-insurance": [("us-home-permits", "US permit basics"),
                                       ("unpermitted-work-home-sale", "When it resurfaces at sale"),
                                       ("fence-shed-insurance", "The small-print habit")],
        "renter-vs-owner-repairs": [("uk-landlord-damp-mould-duties", "Landlord duties, dated"),
                                    ("condensation-vs-rising-vs-penetrating-damp", "Whose damp is it?"),
                                    ("renter-security", "Security for renters")],
        "improvements-no-resale-value": [("single-glazing-payback", "The window maths"),
                                         ("someday-maintenance-cost", "The cost of someday"),
                                         ("unpermitted-work-home-sale", "Paperwork at sale")],
    }
    for slug, ti, dek, b in HOME_ARTICLES:
        key = HOME_SLUG_SECT[slug]
        rel_html = "".join('<li><a href="' + _hurl(s2) + '">' + rt + "</a></li>" for s2, rt in related_map[slug])
        cover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / '
                 '<a href="/home/' + key + '/">' + sec_label(key) + "</a> / " + html.escape(ti) + "</nav>"
            + '<section class="cover"><p class="kicker">' + sec_label(key) + " \u00b7 practical guide</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.8vw,52px)">' + html.escape(ti) + "</h1>"
            + '<p class="byline">BRYME Home &amp; DIY desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not professional advice</p></section>")
        main = ('<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(dek) + "</p></div></section>"
            + '<section class="section"><div class="prose">' + b + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/home/' + key + '/">All of ' + sec_label(key) + "</a>"
            + '<a class="btn secondary" href="/home/mistakes/">Common mistakes</a></div></section>'
            + DISCLAIMER)
        out.append(("/" + slug + "/", ti + " | BRYME Home & DIY", dek[:155],
                    _home_page(ti + " | BRYME Home & DIY", dek[:155], "/" + slug + "/", cover, main, key)))

    # ---------- the checklist product ----------
    groups = []
    seen = []
    for g2, task, why in HOME_CHECK:
        if g2 not in seen:
            seen.append(g2)
    cur = ""
    items = ""
    n3 = 0
    for g2, task, why in HOME_CHECK:
        if g2 != cur:
            if items:
                groups.append((cur, items))
            cur = g2
            items = ""
        n3 += 1
        items += ('<li class="fp-day" data-item="' + html.escape(task[:40]) + '">'
                  '<span class="fp-num">' + str(n3) + "</span>"
                  "<span><b>" + html.escape(task) + "</b><small>" + html.escape(why) + "</small></span>"
                  '<button type="button" class="btn secondary fp-done" aria-pressed="false">Done</button></li>')
    if items:
        groups.append((cur, items))
    weeks_html = "".join(
        '<section class="section"><div class="section-head"><p class="kicker">The checks</p><h2>' + html.escape(g2) + "</h2></div>"
        + '<ul class="list fp-week">' + rows2 + "</ul></section>" for g2, rows2 in groups)
    import json as _j
    cschema = {"@context": "https://schema.org", "@type": "Article",
               "headline": "The Once-a-Season Home Checklist",
               "author": {"@type": "Organization", "name": "BRYME Home & DIY desk"},
               "publisher": {"@type": "Organization", "name": "THE BRYME"},
               "datePublished": TODAY, "dateModified": TODAY,
               "mainEntityOfPage": ORIGIN + "/home/seasonal-home-maintenance-checklist/",
               "description": "A short, season-proof home maintenance checklist with progress saved in your browser."}
    ccover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / The Once-a-Season Checklist</nav>'
        + '<section class="cover"><p class="kicker">The desk\u2019s product \u00b7 season-proof \u00b7 no hemisphere assumptions</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.8vw,52px)">The Once-a-Season Home Checklist</h1>'
        + '<p class="byline">BRYME Home &amp; DIY desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not professional advice</p></section>")
    cmain = ('<section class="section alt"><div class="wrap"><p class="lede"><b>One honest idea:</b> homes fail slowly, then suddenly. '
             + "A short list of checks every season catches the slow failures while they are still cheap. Progress is saved in your browser \u2014 no account, nothing sent anywhere.</p></div></section>"
        + '<section class="section"><div class="wrap"><div class="fp-progressbar" role="img" aria-label="Checklist progress"><div class="fp-fill" id="fp-fill"></div></div>'
        + '<p class="lede" id="fp-status">Nothing ticked yet. Tick items as you do them \u2014 your browser will remember.</p></div></section>'
        + weeks_html
        + '<section class="section"><div class="section-head"><p class="kicker">Boundaries</p><h2>What is deliberately not on this list.</h2></div>'
        + '<div class="prose"><p>Nothing here asks you near an electrical panel, a gas supply, a roof or a structure. Those are the qualified professional\u2019s territory \u2014 the checklist proves your protective devices work, and their visit proves the rest does.</p></div></section>'
        + '<section class="section alt">' + src_html(HOME_SOURCES) + "</section>"
        + '<script type="application/json" id="fit-plan-data">{"total": ' + str(len(HOME_CHECK)) + "}</script>"
        + '<script src="/assets/home-checklist.js" defer></script>'
        + '<script type="application/ld+json">' + _j.dumps(cschema) + "</script>")
    out.append(("/seasonal-home-maintenance-checklist/", "The Once-a-Season Home Checklist | BRYME Home & DIY",
                "A short, season-proof home maintenance checklist \u2014 water, safety devices, appliances, seals, airflow \u2014 with progress saved in your browser.",
                _home_page("The Once-a-Season Home Checklist | BRYME Home & DIY",
                           "A short, season-proof home maintenance checklist with progress saved in your browser.",
                           "/seasonal-home-maintenance-checklist/", ccover, cmain, "checklist")))

    return out + legal_pages("home", "BRYME Home & DIY", "Practical help for fixing, maintaining, improving and understanding your home \u2014 safe, low-risk guidance with clear professional boundaries.")



def main() -> None:
    (OUT / "hub").mkdir(parents=True, exist_ok=True)
    hp = hub_pages()
    base = OUT / "hub"
    for route, title, desc, body in hp:
        f = base / ("index.html" if route == "/" else route.lstrip("/") + "/index.html")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(shell("hub", title, desc, SUB["hub"], body), encoding="utf-8")
    (base / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"<url><loc>https://{DOMAIN}/</loc><lastmod>{TODAY}</lastmod></url>\n</urlset>\n", encoding="utf-8")
    (base / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n", encoding="utf-8")
    (base / "assets").mkdir(parents=True, exist_ok=True)
    (base / "assets" / "site.css").write_text(css_for("hub"), encoding="utf-8")
    print("hub: built (thebryme.com homepage)")
    write_service("entertainment", entertainment_pages())
    write_service("sports", sports_pages())
    write_service("tech", tech_pages())
    write_service("fitness", fitness_pages())
    write_service("home", home_pages())
    print(f"ecosystem built for {DOMAIN}")


if __name__ == "__main__":
    main()
