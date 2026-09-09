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
import json
import os
import re
from pathlib import Path
from xml.sax.saxutils import escape as xesc

ROOT = Path(__file__).resolve().parents[1]
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

def css_for(pub):
    return BASE_CSS % FAMILY[pub]

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
    return f"""<footer class="foot"><div class="wrap foot-in">
<div>© 2026 THE BRYME — {PUB_NAME[pub] if pub != 'hub' else 'the BRYME publications'}.</div>
<div><a href="/{'writers' if pub == 'hub' else pub}/about/">About</a> · <a href="/{'writers' if pub == 'hub' else pub}/privacy/">Privacy</a> · <a href="/{'writers' if pub == 'hub' else pub}/contact/">Contact</a>{extra}</div>
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
        + '<p class="lede">This property is at the foundation stage: the route, standards and plan exist; the guides are being built and will open when they are worth reading. In the meantime, the live desks are <a href="/writers/">BRYME Writers</a>, <a href="/tech/">BRYME Tech</a>, <a href="/sports/">BRYME Sport</a> and <a href="/entertainment/">BRYME Entertainment</a>.</p>'
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

PREFIX = {"sports": "/sports", "entertainment": "/entertainment", "tech": "/tech"}
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
    ("home", "BRYME Home & DIY", "Foundation laid.", "Practical help for fixing, maintaining, improving and understanding your home \u2014 fix it, clean it, maintain it, understand it. Safe, low-risk guidance first; dangerous work belongs to qualified professionals. The first guides are being built now.", "foundation"),
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
    body = f"""{head("hub", "Four publications. One house standard.", parent=False)}
<main id="main"><div class="wrap">
<section class="cover"><p class="kicker">A family of independent publications</p>
<h1 class="cover-title">THE BRYME</h1>
<p class="cover-dek">BRYME is a small ecosystem of specialist publications, each with its own focus and its own standards, held to one house rule: research before publishing, and say exactly what you know. Pick a desk.</p></section>
<section class="section"><div class="section-head"><p class="kicker">The publications</p><h2>Choose your desk</h2></div>
<div class="cards">{cards}</div></section>
<section class="section alt"><div class="section-head"><p class="kicker">The house</p><h2>One standard, four voices.</h2></div>
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

def entertainment_pages():
    manifest = json.loads((OUT / "entertainment" / "_recovered" / "manifest.json").read_text())
    picks = ["korean-cinema-starter-guide-rebuilt", "christopher-nolan-movies-order",
             "nigerian-thrillers-worth-your-time", "indian-cinema-first-five",
             "modern-horror-starter-route", "how-to-pick-a-movie-tonight"]
    # The full restored shelf (audit grades A+B+C): the 2025 research corpus
    # worth keeping is back online as archive editions. True duplicates and
    # the audited-out pieces stay retired (see retired-content-audit.md).
    picks += [
        "10-anime-like-solo-leveling-you-should-watch",
        "10-shows-like-alice-in-borderland-you-should-watch-next",
        "solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences",
        "solo-leveling-from-e-rank-hunter-to-one-of-animes-most-powerful-characters",
        "solo-leveling-e-rank-to-s-rank",
        "breaking-bad-two-seasons-opinion",
        "squid-game-season-1-why-it-became-a-global-phenomenon",
        "why-prison-break-season-1-is-still-one-of-the-best-tv-seasons",
         "prison-break-season-1-watching-all-night", "one-piece-vs-naruto",
        "alice-in-borderland-vs-squid-game",
        "was-eren-yeager-really-the-villain",
        "into-the-badlands-was-underrated",
        "movies-like-interstellar-guide",
        "movies-like-parasite",
        "movies-like-deadpool-and-wolverine",
        "5-movies-that-broke-the-internet",
        "7-movies-we-wished-never-ended",
    ]
    # superseded duplicates: the rebuilt/newer edition is the one restored
    dupes = {"korean-cinema-starter-guide", "movies-like-interstellar"}
    by_slug = {m["slug"]: m for m in manifest}
    art_rows = ""
    pages = []
    for slug in picks:
        m = by_slug.get(slug)
        if not m: continue
        raw = (OUT / "entertainment" / "_recovered" / f"{slug}.html").read_text()
        body_html = clean_recovered(raw)
        route = f"/{slug}/"
        art_rows += f'<li><a href="{route}"><span><b>{html.escape(m["title"])}</b><small>From the archive · {m["words"]} words · re-typeset 2026</small></span><span class="meta">Read →</span></a></li>'
        pbody = f"""{head("entertainment", "Cinema, TV and anime — written about, never pirated.")}
<main id="main"><div class="wrap">
<nav class="crumb"><a href="/">Home</a> / <a href="/">Archive</a> / {html.escape(m["title"])}</nav>
<section class="cover"><p class="kicker">The archive · re-typeset</p><h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">{html.escape(m["title"])}</h1>
<p class="byline">Recovered from the BRYME archive (2025) · words unchanged, presentation renewed · reviewed {TODAY}</p></section>
<section class="section"><div class="prose">{body_html}</div></section>
</div></main>{foot("entertainment")}"""
        pages.append((route, f'{m["title"]} | BRYME Entertainment',
                      "From the BRYME archive — re-typeset and honestly labelled.", pbody))
    archive_note = "".join(
        f'<li><span><b>{html.escape(m["title"])}</b><small>{m["words"]} words · reviewed by the audit — retired on merit</small></span><span class="meta">Retired</span></li>'
        for m in manifest if m["slug"] not in picks and m["slug"] not in dupes)
    index_body = f"""{head("entertainment", "Cinema, TV and anime — written about, never pirated.")}
<main id="main"><div class="wrap">
<section class="cover"><p class="kicker">BRYME Entertainment</p>
<h1 class="cover-title">Written about the work, never trafficking in it.</h1>
<p class="cover-dek">Guides, explainers and opinion on film, television and anime — rebuilt from BRYME's earliest editorial research, re-typeset, and labelled exactly as what they are. No download pages, no streaming links, no piracy: writing about the work, and only that.</p></section>
<section class="section"><div class="section-head"><p class="kicker">The recovered shelf</p><h2>Restored editions</h2></div>
<ul class="list">{art_rows}</ul></section>
<section class="section alt"><div class="section-head"><p class="kicker">In restoration</p><h2>The rest of the archive</h2></div>
<ul class="list">{archive_note}</ul></section></div></main>{foot("entertainment")}"""
    pages = [("/", "BRYME Entertainment — film, TV and anime, written honestly",
              "Guides, explainers and opinion on cinema and anime from the BRYME archive — information only, never piracy.", index_body)] + pages + legal_pages("entertainment", "BRYME Entertainment", "Writing about film, TV and anime for people who love the work.")
    return pages


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
        restored.append(f'<li><a href="{route}"><span><b>{html.escape(m["title"])}</b>'
                        f'<small>From the media desk · {m["words"]} words · {TODAY}</small></span>'
                        f'<span class="meta">Read</span></a></li>')
        pbody = f"""{head("sports", "Analysis, stories and the long view \u2014 never betting.")}
<main id="main"><div class="wrap">
<nav class="crumb"><a href="/">Home</a> / {html.escape(m["title"])}</nav>
<section class="cover"><p class="kicker">The desk · 2026-27 season</p>
<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">{html.escape(m["title"])}</h1>
<p class="byline">From the BRYME media desk · recovered edition, re-typeset {TODAY}</p></section>
<section class="section"><div class="prose">{body_html}</div></section>
</div></main>{foot("sports")}"""
        pages.append((route, f'{m["title"]} | BRYME Sport',
                      "From the BRYME media desk — recovered edition, re-typeset.", pbody))
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
    "web-and-hosting": ("Web & hosting", "Domains, DNS, deploys and the front end \u2014 written from first-hand builds of this very site, failures included.", "hero-hosting.jpg"),
    "safety": ("Safety & privacy", "Passwords, messaging, tokens and your data \u2014 practical protection without the scaremongering.", "hero-privacy.jpg"),
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

def tech_pages():
    arts = _load_tech()
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
        tag = ("Recovered from the BRYME tech archive \u00b7 " if a["recovered"] else "First-hand \u00b7 ")
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
        + '<p class="lede" style="margin-top:18px">Coding coverage is growing from one honest piece: <a href="/learning-to-code-on-a-phone-termux/">learning to code on a phone, and what actually broke</a>.</p></section>'
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
    return pages + legal_pages("tech", "BRYME Tech", "Practical technology from people who ran the thing.")


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
    write_placeholder("fitness", "BRYME Fitness",
        "Practical fitness guidance \u2014 programs, challenges and progress, without medical claims.",
        "BRYME Fitness will answer one question: how do I build a fitness routine I can actually sustain? Beginner programs, walking and strength challenges, exercise and equipment guides, and 30-day plans built around one honest idea \u2014 a reason to come back tomorrow.",
        ["Beginner programs \u2014 start-from-zero plans with sensible progression",
         "30-day challenges \u2014 one day at a time, tracked as you go",
         "Walking plans \u2014 the most underrated habit in fitness",
         "Strength starters \u2014 simple, safe, progressive",
         "Exercise & equipment guides \u2014 what it works, who it fits"])
    write_placeholder("home", "BRYME Home & DIY",
        "Practical help for fixing, maintaining, improving and understanding your home.",
        "BRYME Home & DIY will answer the questions every household hits: why is this not working, how do I maintain it, and can I fix it myself? Low-risk practical problems first \u2014 and clear, non-negotiable safety boundaries: electrical, gas and structural work belongs to qualified professionals.",
        ["Fix it \u2014 household problems and beginner repairs",
         "Clean it \u2014 cleaning and maintenance that actually works",
         "Maintain it \u2014 preventive home maintenance, season by season",
         "Understand it \u2014 appliance symbols, noises and questions",
         "Improve it \u2014 organisation and safe DIY projects"])
    print(f"ecosystem built for {DOMAIN}")


if __name__ == "__main__":
    main()
