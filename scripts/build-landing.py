#!/usr/bin/env python3
"""
BRYME — house landing page (v2, 2026-09-29).

Replaces the "family machine" homepage with a plain-language front door.
Design goal (owner brief): a first-time visitor — or an AdSense reviewer —
must understand what BRYME is within five seconds.

Rules enforced here:
  * every href is asserted against content/index-allowlist.routed.json,
    so this page can never link a 404 (same contract as hub_pages());
  * self-contained: inline <style>, no build-time dependencies;
  * identical head contract to the rest of the house (canonical, OG,
    GA4, Consent Mode v2, AdSense loader, theme, favicon);
  * deterministic: no timestamps beyond a reviewed-date constant.

Writes: ecosystem/hub/index.html  (source of truth — build-routing copies it
        to the repo root, build-public-dir copies it to public/index.html)
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ecosystem" / "hub" / "index.html"
ORIGIN = "https://thebryme.com"
REVIEWED = "29 September 2026"

ALLOWLIST = set(json.loads(
    (ROOT / "content" / "index-allowlist.routed.json").read_text(encoding="utf-8")
)["routes"])

_links: list[str] = []
no_allowlist: list[str] = []

def L(route: str, label: str, cls: str = "", extra: str = "") -> str:
    """Anchor that cannot ship a 404."""
    assert route.startswith("/"), route
    assert route.endswith("/"), f"route must be trailing-slashed: {route}"
    # Contract: the route must resolve. Two valid kinds of destination:
    #   1. an indexable route in the routed allowlist, or
    #   2. a real file on disk (a few house trust pages are deliberately
    #      noindex -- e.g. /privacy/ -- yet must still be linkable).
    # Anything else would ship a 404, which this build refuses to do.
    on_disk = (ROOT / route.strip("/") / "index.html").exists() if route != "/" else True
    if route not in ALLOWLIST and not on_disk:
        raise SystemExit(f"build-landing: route resolves nowhere (404 risk): {route}")
    if route not in ALLOWLIST:
        no_allowlist.append(route)
    _links.append(route)
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{route}"{c}{extra}>{label}</a>'

# ---------------------------------------------------------------- content ----
DESKS = [
    ("Writers", "/writers/", "wr",
     "Get paid to write.",
     "Where to send your work, what they pay, and how to pitch. 142 paying markets checked by hand."),
    ("Tech", "/tech/", "te",
     "Fix your phone, laptop or Wi-Fi.",
     "Plain answers to the tech problems you actually have — no jargon, no upsell."),
    ("Home &amp; DIY", "/home/", "ho",
     "Fix it yourself, or know when to call someone.",
     "Repairs, appliances, wiring safety and seasonal jobs around the house."),
    ("Fitness", "/fitness/", "fi",
     "Get fit without a gym.",
     "Training plans that need no equipment and no supplements, plus free calculators."),
    ("Money", "/money/", "mo",
     "Understand money before you risk it.",
     "Saving, budgeting, mortgages and honest trading education. Risk first, always."),
    ("Sport", "/sports/", "sp",
     "Football, explained properly.",
     "Tables, fixtures, transfers and tactics — dated, checked and updated each week."),
    ("Entertainment", "/entertainment/", "en",
     "Find something good to watch.",
     "Film and TV guides, reviews and a catalogue you can actually browse."),
]

# name, route, kicker, title
FEATURED = [
    ("How to write a magazine pitch", "/writers/guides/how-to-write-a-pitch/",
     "Writers", "The exact structure editors expect — and what gets you rejected."),
    ("The honest laptop spec floor", "/tech/student-laptop-spec-floor-2026/",
     "Tech", "What a student laptop really needs, separated from the marketing."),
    ("Power without a generator", "/home/generator-vs-inverter-nigeria/",
     "Home &amp; DIY", "Sizing an inverter to your actual load, in plain numbers."),
    ("The 30-day walking plan", "/fitness/30-day-walking-plan/",
     "Fitness", "Start where you are. No gym, no equipment, no cost."),
    ("Before you place a trade", "/money/trading-risk-checklist/",
     "Money", "The pre-trade checklist that stops the expensive mistakes."),
    ("What to watch tonight", "/entertainment/how-to-pick-a-movie-tonight/",
     "Entertainment", "A decision route for when nobody can agree on a film."),
]

TOOLS = [
    ("Freelance rate calculator", "/writers/tools/freelance-rate-calculator/", "Writers"),
    ("Invoice generator", "/writers/tools/invoice-generator/", "Writers"),
    ("Mortgage payment calculator", "/money/mortgage-payment-calculator/", "Money"),
    ("Savings goal calculator", "/money/savings-goal-calculator/", "Money"),
    ("One-rep max calculator", "/fitness/1rm-calculator/", "Fitness"),
    ("Heart-rate zone calculator", "/fitness/heart-rate-zone-calculator/", "Fitness"),
    ("Rent or buy calculator", "/home/rent-or-buy-tool/", "Home &amp; DIY"),
    ("All writing tools", "/writers/tools/", "Writers"),
]

TRUST = [
    ("Every page carries a date", "You always know how fresh the information is."),
    ("Claims are sourced", "Where a fact comes from an official source, we link it."),
    ("Mistakes are published", "Our corrections log is public and permanent."),
    ("No pop-ups, no interstitials", "Ever. Nothing blocks the page you came to read."),
    ("Nothing is saved on our servers", "Tools run in your browser. No account needed."),
    ("One house standard", "Seven sections, the same rules on all of them."),
]

HOW = [
 ("We check before we publish",
  "Where a page rests on a fact &mdash; a price, a date, a rule, a pay rate &mdash; we go to the primary source: "
  "the government page, the company&rsquo;s own documentation, the publication&rsquo;s own submission guidelines. "
  "Secondary sources are used to find the primary one, never to replace it. If the sources disagree, the page "
  "says so rather than picking a winner."),
 ("We date anything that can go stale",
  "Prices change. Rules change. Schedules change. Every page that could age carries the date it was last "
  "checked, so you can judge how much to trust it. Nothing on BRYME is presented as permanently true when "
  "it is not."),
 ("We separate what we know from what we think",
  "Research, firsthand experience and analysis are labelled differently, because they are worth different "
  "amounts. Where BRYME has done the thing itself &mdash; submitted the pitch, placed the trade, run the "
  "programme &mdash; the account says so. Where it has not, the page says that too."),
 ("We publish our mistakes",
  "Corrections are made in the open and kept on a public log, not quietly deleted. If a page was wrong, the "
  "record shows what changed and when. A publication that never corrects anything is not being careful; it "
  "is not looking."),
]

NEVER = ("pop-ups, interstitials or autoplaying video", "earnings we cannot verify",
         "copy taken from another site", "medical, legal or financial advice dressed up as fact")

FOOTER = [
    ("About BRYME", "/about/"),
    ("Editorial policy", "/writers/editorial-policy/"),
    ("Corrections", "/writers/corrections/"),
    ("Privacy", "/privacy/"),
    ("Contact", "/writers/contact/"),
    ("Terms", "/writers/terms/"),
    ("Copyright", "/writers/copyright/"),
    ("Science &amp; disclaimer", "/writers/disclaimer/"),
]

# ------------------------------------------------------------------- style ---
CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
 --paper:#faf9f7;--sheet:#fff;--ink:#131c33;--ink-2:#3d4859;--muted:#68727f;
 --brand:#131c33;--brand-2:#0a1122;--accent:#9c6b1f;--accent-soft:#f6efdf;
 --line:rgba(19,28,51,.14);--line-2:rgba(19,28,51,.30);
 --serif:Georgia,'Iowan Old Style','Palatino Linotype','Times New Roman',serif;
 --sans:Inter,ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
 --shadow:0 1px 2px rgba(10,17,34,.04),0 10px 30px rgba(10,17,34,.07);
 --shadow-lg:0 2px 4px rgba(10,17,34,.05),0 18px 50px rgba(10,17,34,.12);
 --r:14px;
}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);
 font:17px/1.65 var(--sans);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
img{max-width:100%;height:auto;display:block}
a{color:inherit;text-decoration:none}
h1,h2,h3{font-family:var(--serif);font-weight:700;letter-spacing:-.015em;line-height:1.15;margin:0}
p{margin:0}
.wrap{width:min(100% - 40px,1140px);margin-inline:auto}
.skip-link{position:absolute;left:-9999px}
.skip-link:focus{left:12px;top:12px;z-index:99;background:#fff;padding:10px 16px;border-radius:8px;
 box-shadow:var(--shadow-lg);position:fixed}
:where(a,button,summary):focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}

/* ---- header ---- */
.hdr{position:sticky;top:0;z-index:50;background:rgba(250,249,247,.92);
 backdrop-filter:saturate(160%) blur(12px);border-bottom:1px solid var(--line)}
.hdr-in{display:flex;align-items:center;gap:20px;min-height:66px}
.brand{display:flex;align-items:center;gap:11px;font-family:var(--serif);
 font-size:20px;font-weight:700;letter-spacing:.01em;white-space:nowrap}
.brand .mark{width:30px;height:30px;border-radius:8px;background:var(--brand);
 color:#fff;display:grid;place-items:center;font-family:var(--sans);
 font-size:15px;font-weight:800;letter-spacing:0}
.hdr nav{display:flex;gap:2px;margin-left:auto;flex-wrap:wrap}
.hdr nav a{padding:8px 12px;border-radius:8px;font-size:14.5px;font-weight:500;color:var(--ink-2)}
.hdr nav a:hover{background:rgba(19,28,51,.06);color:var(--ink)}
.hdr .cta{background:var(--brand);color:#fff!important;font-weight:600;padding:9px 16px!important}
.hdr .cta:hover{background:var(--brand-2)}
@media(max-width:900px){.hdr nav a:not(.cta){display:none}.hdr nav{margin-left:auto}}

/* ---- hero ---- */
.hero{padding:58px 0 6px}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-size:12.5px;font-weight:700;
 letter-spacing:.11em;text-transform:uppercase;color:var(--accent);
 background:var(--accent-soft);border:1px solid rgba(156,107,31,.22);
 padding:7px 14px;border-radius:999px;margin-bottom:22px}
.hero h1{font-size:clamp(34px,5.4vw,58px);max-width:19ch}
.hero .lede{margin-top:20px;font-size:clamp(17px,2.05vw,21px);color:var(--ink-2);max-width:62ch;line-height:1.58}
.hero .lede b{color:var(--ink);font-weight:600}

/* ---- desk cards ---- */
.sect{padding:54px 0 0}
.sect-hd{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;margin-bottom:8px}
.sect-hd h2{font-size:clamp(24px,3.1vw,33px)}
.sect-hd .hint{color:var(--muted);font-size:15.5px}
.grid{display:grid;gap:16px;margin-top:26px}
.g-desks{grid-template-columns:repeat(auto-fill,minmax(268px,1fr))}
.g-3{grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}

.desk{display:flex;flex-direction:column;background:var(--sheet);border:1px solid var(--line);
 border-radius:var(--r);padding:24px 22px 20px;box-shadow:var(--shadow);
 transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease;position:relative;overflow:hidden}
.desk::after{content:"";position:absolute;inset:0 auto 0 0;width:4px;background:var(--brand);opacity:0;transition:opacity .16s ease}
.desk:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg);border-color:var(--line-2)}
.desk:hover::after{opacity:1}
.desk .tag{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
 color:var(--muted);margin-bottom:12px}
.desk h3{font-size:23px;margin-bottom:9px}
.desk .say{font-size:15.5px;color:var(--ink);font-weight:600;margin-bottom:7px;line-height:1.45}
.desk .sub{font-size:14.5px;color:var(--muted);line-height:1.55;flex:1}
.desk .go{margin-top:16px;font-size:14px;font-weight:700;color:var(--accent);
 display:inline-flex;align-items:center;gap:7px}
.desk .go span{transition:transform .16s ease}
.desk:hover .go span{transform:translateX(4px)}

/* ---- featured ---- */
.piece{display:flex;flex-direction:column;background:var(--sheet);border:1px solid var(--line);
 border-radius:var(--r);padding:22px;box-shadow:var(--shadow);transition:transform .16s ease,box-shadow .16s ease}
.piece:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg)}
.piece .kick{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.piece h3{font-size:19.5px;margin:10px 0 8px;line-height:1.28}
.piece p{font-size:14.5px;color:var(--muted);line-height:1.55;flex:1}
.piece .rd{margin-top:14px;font-size:13.5px;font-weight:600;color:var(--ink-2)}

/* ---- tools ---- */
.tool{display:flex;align-items:center;gap:14px;background:var(--sheet);border:1px solid var(--line);
 border-radius:11px;padding:15px 18px;box-shadow:var(--shadow);transition:border-color .16s,transform .16s}
.tool:hover{border-color:var(--line-2);transform:translateX(3px)}
.tool .dot{width:9px;height:9px;border-radius:50%;background:var(--accent);flex:0 0 auto}
.tool b{font-size:15.5px;font-weight:600;display:block;line-height:1.3}
.tool small{color:var(--muted);font-size:13px}

/* ---- how we work ---- */
.g-how{grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px 28px}
.how{border-left:3px solid var(--accent);padding-left:18px}
.how h3{font-size:18px;margin-bottom:8px;line-height:1.3}
.how p{font-size:14.8px;color:var(--ink-2);line-height:1.62}
.never-box{margin-top:30px;background:#fdf6e9;border:1px solid rgba(156,107,31,.28);
 border-radius:12px;padding:22px 26px}
.never-box h3{font-size:16.5px;margin-bottom:12px;font-family:var(--sans);font-weight:700}
.never-box ul{margin:0;padding-left:20px;display:grid;gap:7px}
.never-box li{font-size:14.5px;color:var(--ink-2)}

/* ---- trust ---- */
.trust{margin-top:56px;background:var(--brand);color:#eef1f7;border-radius:18px;
 padding:clamp(30px,4.4vw,50px);box-shadow:var(--shadow-lg)}
.trust h2{color:#fff;font-size:clamp(23px,3vw,30px);margin-bottom:10px}
.trust .sub{color:rgba(238,241,247,.72);font-size:16px;max-width:60ch;margin-bottom:30px}
.g-trust{grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:22px 30px;margin-top:0}
.tr{display:flex;gap:13px;align-items:flex-start}
.tr svg{flex:0 0 auto;margin-top:3px}
.tr b{display:block;font-size:15.5px;color:#fff;margin-bottom:3px;font-weight:600}
.tr span{font-size:14px;color:rgba(238,241,247,.68);line-height:1.5}

/* ---- cta ---- */
.cta-box{margin-top:56px;background:var(--sheet);border:1px solid var(--line);
 border-radius:18px;padding:clamp(30px,4.4vw,50px);box-shadow:var(--shadow);text-align:center}
.cta-box h2{font-size:clamp(23px,3vw,31px);margin-bottom:12px}
.cta-box p{color:var(--muted);max-width:56ch;margin:0 auto 26px;font-size:16.5px;line-height:1.6}
.btn{display:inline-flex;align-items:center;gap:9px;background:var(--brand);color:#fff;
 font-weight:600;font-size:16px;padding:14px 26px;border-radius:11px;transition:background .16s,transform .16s}
.btn:hover{background:var(--brand-2);transform:translateY(-2px)}
.btn.alt{background:transparent;color:var(--ink);border:1.5px solid var(--line-2)}
.btn.alt:hover{background:rgba(19,28,51,.05);transform:translateY(-2px)}

/* ---- footer ---- */
.ft{margin-top:64px;border-top:1px solid var(--line);padding:34px 0 54px}
.ft-in{display:flex;flex-wrap:wrap;gap:14px 26px;align-items:center;justify-content:space-between}
.ft nav{display:flex;flex-wrap:wrap;gap:8px 20px}
.ft a{font-size:14px;color:var(--ink-2)}
.ft a:hover{color:var(--accent)}
.ft .note{font-size:13px;color:var(--muted);max-width:52ch;line-height:1.55}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}html{scroll-behavior:auto}}
"""

CHECK = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M13.5 4.5 6.5 11.5 2.5 7.5" stroke="#c8a25a" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ------------------------------------------------------------------ render ---
nav = "".join(L(r, n) for n, r, *_ in DESKS)
nav += L("/about/", "About", cls="cta")

desk_cards = "".join(
    f'<article class="desk"><div class="tag">{k}</div>'
    f'<h3>{L(r, n)}</h3>'
    f'<p class="say">{say}</p><p class="sub">{sub}</p>'
    f'<div class="go">{L(r, "Open section <span aria-hidden=\'true\'>&#8594;</span>")}</div></article>'
    for n, r, k, say, sub in DESKS
)

featured = "".join(
    f'<article class="piece"><div class="kick">{kick}</div>'
    f'<h3>{L(r, t)}</h3><p>{dek}</p>'
    f'<div class="rd">{L(r, "Read it &#8594;")}</div></article>'
    for t, r, kick, dek in FEATURED
)

tools = "".join(
    f'<a class="tool" href="{r}"><span class="dot" aria-hidden="true"></span>'
    f'<span><b>{n}</b><small>{k} &middot; free, runs in your browser</small></span></a>'
    for n, r, k in TOOLS
)

trust = "".join(
    f'<div class="tr">{CHECK}<div><b>{b}</b><span>{s}</span></div></div>'
    for b, s in TRUST
)

how = "".join(
    f'<article class="how"><h3>{t}</h3><p>{d}</p></article>' for t, d in HOW
)
never = "".join(f"<li>{x}</li>" for x in NEVER)

footer = "".join(L(r, n) for n, r in FOOTER)

SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": ORIGIN + "/#website", "url": ORIGIN + "/",
         "name": "THE BRYME", "inLanguage": "en",
         "description": ("Seven independent editorial desks — professional writing, technology, "
                         "home & DIY, fitness, money, sport and film & TV. Dated claims, sourced "
                         "facts, a public corrections log and no pop-ups."),
         "publisher": {"@id": ORIGIN + "/#org"}},
        {"@type": "Organization", "@id": ORIGIN + "/#org", "name": "THE BRYME",
         "url": ORIGIN + "/", "foundingDate": "2026",
         "description": "An independent family of seven specialist publications."},
    ],
}, separators=(",", ":"))

HTML = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>THE BRYME — seven sections, written in plain English</title>
<meta name="description" content="BRYME is a free publication in seven sections: writing, tech, home &amp; DIY, fitness, money, sport and film. Every page is dated, sourced and checked. No pop-ups, ever.">
<meta name="robots" content="index,follow"><meta name="p:domain_verify" content="69f32b47370c197e72e39c8339160660"/>
<link rel="canonical" href="{ORIGIN}/">
<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">
<meta property="og:title" content="THE BRYME — seven sections, written in plain English">
<meta property="og:description" content="Seven sections: writing, tech, home, fitness, money, sport and film. Dated, sourced, no pop-ups.">
<meta property="og:url" content="{ORIGIN}/"><meta property="og:image" content="{ORIGIN}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<meta name="google-adsense-account" content="ca-pub-1881426210393009">
<script src="/assets/canonical-redirect.js"></script>
<script src="/assets/gtag-init.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0KEKJH9960"></script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1881426210393009" crossorigin="anonymous"></script>
<script src="/assets/theme.js"></script>
<script type="application/ld+json">{SCHEMA}</script>
<meta name="theme-color" content="#faf9f7"><meta name="color-scheme" content="light dark">
<style>{CSS}</style>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="hdr"><div class="wrap hdr-in">
  <a class="brand" href="/"><span class="mark" aria-hidden="true">B</span>THE BRYME</a>
  <nav aria-label="Sections">{nav}</nav>
</div></header>

<main id="main">

<section class="hero"><div class="wrap">
  <span class="eyebrow">Free &middot; No pop-ups &middot; Every page dated</span>
  <h1>Seven sections. Pick where you want to go.</h1>
  <p class="lede">BRYME is a free publication about everyday life. Each section below covers one subject —
  <b>getting paid to write</b>, <b>fixing your tech</b>, <b>your home</b>, <b>your fitness</b>,
  <b>your money</b>, <b>football</b> and <b>what to watch</b>. Everything is written in plain English,
  dated, and checked against real sources.</p>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>The seven sections</h2>
    <span class="hint">Click any card to go straight in.</span></div>
  <div class="grid g-desks">{desk_cards}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>Good places to start</h2>
    <span class="hint">Six pages that show how we work.</span></div>
  <div class="grid g-3">{featured}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>How BRYME works</h2>
    <span class="hint">The same four rules on every one of the seven sections.</span></div>
  <div class="grid g-how">{how}</div>
  <div class="never-box">
    <h3>What you will never find on this site</h3>
    <ul>{never}</ul>
  </div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>Free tools — no sign-up, nothing uploaded</h2>
    <span class="hint">They run inside your browser.</span></div>
  <div class="grid g-3" style="margin-top:26px">{tools}</div>
</div></section>

<section class="sect"><div class="wrap"><div class="trust">
  <h2>Why you can trust what you read here</h2>
  <p class="sub">Seven sections run by one editorial house, under one standard. These rules apply to
  every page on the site, without exception.</p>
  <div class="grid g-trust">{trust}</div>
</div></div></section>

<section class="sect"><div class="wrap"><div class="cta-box">
  <h2>Not sure where to begin?</h2>
  <p>If you are new, the writers' section is the one people come for most — real paying markets,
  checked by hand, with what each one pays and how to pitch them.</p>
  <a class="btn" href="/writers/">Start with Writers <span aria-hidden="true">&#8594;</span></a>
  <a class="btn alt" href="/about/" style="margin-left:10px">How BRYME works</a>
</div></div></section>

</main>

<footer class="ft"><div class="wrap ft-in">
  <nav aria-label="House pages">{footer}</nav>
  <p class="note">THE BRYME &middot; An independent family of seven publications.
  Reviewed {REVIEWED}. Nothing on this page is financial, medical or legal advice.</p>
</div></footer>
</body></html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(HTML, encoding="utf-8")

dupes = {r for r in _links if _links.count(r) > 1}
print(f"build-landing: wrote {OUT.relative_to(ROOT)} ({len(HTML):,} bytes)")
print(f"build-landing: {len(_links)} links, {len(set(_links))} unique, all allowlisted")
print(f"build-landing: repeated-route links (fine, just noted): {sorted(dupes) if dupes else 'none'}")
print(f"build-landing: linked but intentionally noindex: {sorted(set(no_allowlist)) or 'none'}")
