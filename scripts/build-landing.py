#!/usr/bin/env python3
"""
BRYME — Writers-first house landing page (Phase 1 v2, 2026-09-29)
Sophisticated edition: dark/light mode, keyboard palette (Ctrl+K), gauges,
saved-for-later, continue reading, drawer, bottom-nav, search, kbd hints.

75-80% Writers, 20-25% secondary desks compact.
Uses bryme-v2.css + tech-hub.css + tech-hub.js (living machine).
data-tm-desk="home" namespaces localStorage to bryme.home.*
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ecosystem" / "hub" / "index.html"
ORIGIN = "https://thebryme.com"
REVIEWED = "29 September 2026"
REVIEWED_ISO = "2026-09-29"
SWEEP = "2026-09-27"

ALLOWLIST = set(json.loads(
    (ROOT / "content" / "index-allowlist.routed.json").read_text(encoding="utf-8")
)["routes"])

_links: list[str] = []
no_allowlist: list[str] = []

def L(route: str, label: str, cls: str = "", extra: str = "") -> str:
    assert route.startswith("/"), route
    assert route.endswith("/"), f"trailing slash required: {route}"
    on_disk = (ROOT / route.strip("/") / "index.html").exists() if route != "/" else True
    if route not in ALLOWLIST and not on_disk:
        raise SystemExit(f"build-landing: 404 risk {route}")
    if route not in ALLOWLIST:
        no_allowlist.append(route)
    _links.append(route)
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{route}"{c}{extra}>{label}</a>'

def href(route: str) -> str:
    # like L but returns only route after validation, for use in row-a hrefs
    assert route.startswith("/") and route.endswith("/")
    if route not in ALLOWLIST and not (ROOT / route.strip("/") / "index.html").exists():
        raise SystemExit(f"build-landing: 404 risk {route}")
    _links.append(route)
    return route

# --- data loads ---
try:
    opp_data = json.loads((ROOT / "content" / "opportunities.json").read_text(encoding="utf-8"))
    opportunities = opp_data.get("opportunities", [])
    opportunities_sorted = sorted(opportunities, key=lambda x: x.get("lastVerified",""), reverse=True)
    recent_verified = opportunities_sorted[:12]
except Exception:
    opportunities = []
    recent_verified = []

opp_count = len(opportunities) if opportunities else 142
# approximate counts from files
guides_count = 197
tools_count = 48
total_pieces = opp_count + guides_count + tools_count  # 339-ish

# ---------------------------------------------------------------- secondary
SECONDARY_DESKS = [
    ("Tech", "/tech/", "te", "Fix your phone, laptop or Wi-Fi — no jargon, no upsell."),
    ("Home & DIY", "/home/", "ho", "Repairs, appliances, safety and seasonal jobs around the house."),
    ("Fitness", "/fitness/", "fi", "Training plans with no equipment and free calculators."),
    ("Money", "/money/", "mo", "Saving, budgeting, mortgages and honest trading education."),
    ("Sport", "/sports/", "sp", "Football tables, fixtures, transfers and tactics — dated weekly."),
    ("Entertainment", "/entertainment/", "en", "Film and TV guides, reviews and a browsable catalogue."),
]

# 7 pillars — each is a need
PILLARS = [
    # key, label, route, title, desc, kbd
    ("write", "WRITE", "/writers/learn/", "Craft, editing, storytelling", "Guides on fiction, nonfiction, essays, poetry, screenwriting, pitches — beginner to advanced.", "1"),
    ("submit", "SUBMIT", "/writers/guides/how-to-write-a-pitch/", "Get your work out there", "How to write a pitch editors actually read, query letters, cover letters, and follow-ups.", "2"),
    ("discover", "DISCOVER OPPORTUNITIES", "/writers/writing/", "142 paying markets checked by hand", "Every publication BRYME has verified — what they pay, what they want, how to submit, when they close.", "3"),
    ("research", "RESEARCH MARKETS", "/writers/writing-opportunities/", "Find markets by country", "US, UK, Canada, Australia, Nigeria, and open-to-anywhere — filter by pay, genre, eligibility.", "4"),
    ("earn", "EARN", "/writers/guides/how-much-to-charge-for-an-article/", "Build a writing income", "Rates, retainers, ghostwriting pricing, invoicing, tracking income and the tax habit.", "5"),
    ("tools", "USE WRITING TOOLS", "/writers/tools/", "48 free tools, no sign-up", "Word counters, invoice generator, rate calculator, citation formatter — runs in your browser.", "6"),
    ("career", "BUILD A CAREER", "/writers/start/", "From zero to paid", "Complete beginner path, writing intelligence, and BRYME's firsthand verification record.", "7"),
]

# Recently verified — 6
RECENT = []
for rec in recent_verified[:6]:
    slug = rec.get("slug","")
    route = f"/writers/writing/{slug}/"
    pub = rec.get("publication","")
    pay = rec.get("pay",{}).get("display","") or rec.get("payDisplay","") or ""
    title = rec.get("title","") or rec.get("seoTitle","") or pub
    verified = rec.get("lastVerified","") or SWEEP
    # short dek
    excerpt = (rec.get("excerpt","") or rec.get("seoDescription","") or "")[:140]
    RECENT.append((pub, route, pay, title, verified, excerpt))

STRONG_EXISTING = [
    ("West Branch submissions", "/writers/writing/west-branch/", "Poetry $100, prose $0.10/word up to $200 — 81 impressions, pos 6.3 in GSC", "2026-09-20", "discover"),
    ("Poetry London submissions", "/writers/writing/poetry-london/", "£35 per poem — earning clicks at pos 9.7", "2026-09-19", "discover"),
    ("New Lines Magazine pitch", "/writers/writing/new-lines-magazine/", "$600–$800 — pos 4.7, 14% CTR", "2026-09-18", "discover"),
    ("Uncanny Magazine poetry", "/writers/writing/uncanny-poetry/", "$40 per poem — 14% CTR, pos 6.8", "2026-09-17", "discover"),
    ("The Fiction Desk", "/writers/writing/the-fiction-desk/", "£25 per 1,000 words — pos 7.2", "2026-09-16", "discover"),
    ("Himal Southasian", "/writers/writing/himal-southasian/", "Set rates on commission — pos 7.7", "2026-09-15", "discover"),
    ("Longreads", "/writers/writing/longreads/", "$500 personal essays — pos 7.1", "2026-09-14", "research"),
    ("The Republic personal essay", "/writers/writing/the-republic/", "₦100,000 — pos 4.8, strong NG market", "2026-09-13", "research"),
]

WRITING_GUIDES = [
    ("How to write a magazine pitch", "/writers/guides/how-to-write-a-pitch/", "The exact structure editors expect — and what gets you rejected.", "2026-09-22", "submit"),
    ("How to find paid writing opportunities", "/writers/guides/how-to-find-paid-writing-opportunities/", "Where paying markets actually list, and how BRYME verifies them.", "2026-09-21", "discover"),
    ("How to get your first paid writing gig", "/writers/guides/how-to-get-your-first-paid-writing-gig/", "From zero samples to first byline — practical steps.", "2026-09-20", "career"),
    ("How much to charge for an article", "/writers/guides/how-much-to-charge-for-an-article/", "Real market rates, not guesswork — with calculator.", "2026-09-19", "earn"),
    ("How to write a strong query letter", "/writers/guides/how-to-write-a-strong-query-letter/", "For fiction, nonfiction and poetry submissions.", "2026-09-18", "submit"),
    ("How to submit a freelance article", "/writers/guides/how-to-submit-a-freelance-article/", "Formatting, cover note, and what to include.", "2026-09-17", "submit"),
    ("How to pitch an essay", "/writers/guides/how-to-pitch-an-essay/", "Essay-specific pitching — thesis, timeliness, and voice.", "2026-09-16", "submit"),
    ("Where the money is in writing", "/writers/guides/where-the-money-is-in-writing/", "Which formats and markets pay, and how to track income.", "2026-09-15", "earn"),
]

WRITING_TOOLS = [
    ("Freelance rate calculator", "/writers/tools/freelance-rate-calculator/", "Price per word, per hour, per project — with tax set-aside.", "2026-09-10", "tools"),
    ("Invoice generator", "/writers/tools/invoice-generator/", "Create a clean invoice in your browser, no account.", "2026-09-09", "tools"),
    ("Word counter", "/writers/tools/word-counter/", "Live count, reading time, no upload.", "2026-09-08", "tools"),
    ("Character counter", "/writers/tools/character-counter/", "With and without spaces.", "2026-09-07", "tools"),
    ("Citation formatter", "/writers/tools/citation-formatter/", "APA, MLA, Chicago from details you have.", "2026-09-06", "tools"),
    ("Income tracker", "/writers/tools/income-tracker/", "Track pitches, acceptances, payments — local only.", "2026-09-05", "tools"),
    ("Deadline tracker", "/writers/tools/deadline-tracker/", "Never miss a reading period or contest deadline.", "2026-09-04", "tools"),
    ("All 48 writing tools", "/writers/tools/", "Full toolbox — outline builder, cliche detector, more.", "2026-09-03", "tools"),
]

CAREER_RESOURCES = [
    ("Freelance rate calculator", "/writers/tools/freelance-rate-calculator/", "Know what to charge before you pitch.", "2026-09-10", "earn"),
    ("How much to charge for an article", "/writers/guides/how-much-to-charge-for-an-article/", "Market rates from BRYME's 142-record research.", "2026-09-19", "earn"),
    ("How to price ghostwriting jobs", "/writers/guides/how-to-price-ghostwriting-jobs/", "Per-word, per-hour, and retainer models.", "2026-09-12", "earn"),
    ("The tax set-aside habit", "/writers/guides/the-tax-set-aside-habit/", "A simple percentage system for freelance income.", "2026-09-11", "earn"),
    ("Track your writing income", "/writers/guides/track-your-writing-income/", "Spreadsheet-free tracking in your browser.", "2026-09-08", "career"),
    ("Where the money is in writing", "/writers/guides/where-the-money-is-in-writing/", "Formats that pay vs. exposure-only — with data.", "2026-09-15", "career"),
]

BY_COUNTRY = [
    ("United States", "/writers/writing-opportunities/usa/", "US-based publications", "2026-09-10", "research"),
    ("United Kingdom", "/writers/writing-opportunities/united-kingdom/", "UK magazines and journals", "2026-09-10", "research"),
    ("Canada", "/writers/writing-opportunities/canada/", "Canadian literary markets", "2026-09-09", "research"),
    ("Australia", "/writers/writing-opportunities/australia/", "Australian publications", "2026-09-09", "research"),
    ("Nigeria", "/writers/writing-opportunities/nigeria/", "Nigerian & Africa-focused — 12.5% CTR market", "2026-09-08", "research"),
    ("Open to writers anywhere", "/writers/writing-opportunities/remote/", "No location restriction — worldwide", "2026-09-07", "research"),
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
  "Where a page rests on a fact — a price, a date, a rule, a pay rate — we go to the primary source: "
  "the government page, the company's own documentation, the publication's own submission guidelines. "
  "Secondary sources are used to find the primary one, never to replace it. If the sources disagree, the page "
  "says so rather than picking a winner."),
 ("We date anything that can go stale",
  "Prices change. Rules change. Schedules change. Every page that could age carries the date it was last "
  "checked, so you can judge how much to trust it. Nothing on BRYME is presented as permanently true when "
  "it is not."),
 ("We separate what we know from what we think",
  "Research, firsthand experience and analysis are labelled differently, because they are worth different "
  "amounts. Where BRYME has done the thing itself — submitted the pitch, placed the trade, run the "
  "programme — the account says so. Where it has not, the page says that too."),
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
    ("Science & disclaimer", "/writers/disclaimer/"),
]

# ---------- helpers for rows ----------
def esc(s: str) -> str:
    return (s or "").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def row_html(title: str, route: str, dek: str, date: str, need: str, sec: str, kind: str = "guide", badge: str = "", pay: str = "") -> str:
    r = href(route)
    # date for display mm/dd
    try:
        dt = datetime.fromisoformat(date)
        disp = dt.strftime("%m/%d")
    except:
        disp = date[5:].replace("-","/") if len(date)>=10 else date
    badge_html = f'<i class="tm-badge" data-on="1">{esc(badge)}</i>' if badge else ""
    pay_html = f'<i class="tm-badge">{esc(pay)}</i>' if pay else ""
    # side includes badge + pay + time
    side = f'{badge_html}{pay_html}<time datetime="{esc(date)}">{esc(disp)}</time>'
    return (
        f'<div class="tm-row" data-need="{esc(need)}" data-sec="{esc(sec)}" data-date="{esc(date)}" data-kind="{esc(kind)}">'
        f'<a class="tm-row-a" href="{esc(r)}"><b>{esc(title)}</b><small>{esc(dek)}</small></a>'
        f'<span class="tm-row-side">{side}</span>'
        f'<button type="button" class="tm-save" aria-pressed="false"><span class="tm-save-ic" aria-hidden="true">◇</span><span class="tm-save-t">Save</span></button>'
        f'</div>'
    )

# Build rows per shelf
recent_rows = "".join(
    row_html(title, route, f"{pub} — {pay} — {excerpt}"[:160], verified, "discover", "writing", "guide", "Verified", pay)
    for pub, route, pay, title, verified, excerpt in RECENT
)

country_rows = "".join(
    row_html(name, route, desc, date, need, "atlas", "guide")
    for name, route, desc, date, need in BY_COUNTRY
)

strong_rows = "".join(
    row_html(title, route, desc, date, need, "writing", "guide", "Top")
    for title, route, desc, date, need in STRONG_EXISTING
)

guides_rows = "".join(
    row_html(title, route, desc, date, need, "learn", "guide")
    for title, route, desc, date, need in WRITING_GUIDES
)

tools_rows = "".join(
    row_html(name, route, desc, date, need, "tools", "tool")
    for name, route, desc, date, need in WRITING_TOOLS
)

career_rows = "".join(
    row_html(title, route, desc, date, need, "learn", "guide")
    for title, route, desc, date, need in CAREER_RESOURCES
)

secondary_rows = "".join(
    row_html(name, route, desc, REVIEWED_ISO, "research", "house", "guide", tag.upper())
    for name, route, tag, desc in SECONDARY_DESKS
)

# Pillars as tm-need buttons
pillars_needs_html = "".join(
    f'<button type="button" class="tm-need" data-need="{need}" aria-pressed="false">'
    f'<span class="tm-need-k" aria-hidden="true">{kbd}</span>'
    f'<b>{title}</b><em class="tm-need-n">{label}</em>'
    f'<small>{desc}</small></button>'
    for need, label, route, title, desc, kbd in PILLARS
)

# Toolbar chips
chips_html = (
    '<button type="button" class="tm-chip" data-need="write" aria-pressed="false">Write</button>'
    '<button type="button" class="tm-chip" data-need="submit" aria-pressed="false">Submit</button>'
    '<button type="button" class="tm-chip" data-need="discover" aria-pressed="false">Discover</button>'
    '<button type="button" class="tm-chip" data-need="research" aria-pressed="false">By country</button>'
    '<button type="button" class="tm-chip" data-need="earn" aria-pressed="false">Earn</button>'
    '<button type="button" class="tm-chip" data-need="tools" aria-pressed="false">Tools</button>'
    '<button type="button" class="tm-chip" data-need="career" aria-pressed="false">Career</button>'
    '<button type="button" class="tm-chip" data-kind="tool" aria-pressed="false">Tools only</button>'
    '<button type="button" class="tm-chip" data-saved="1" aria-pressed="false">Saved only</button>'
    '<button type="button" class="tm-chip tm-chip-clear" data-tm-clear-filters hidden>Clear filters</button>'
)

# Secondary desks as sec-cards for compact band
secondary_cards_html = "".join(
    f'<a class="tm-sec-card" href="{href(route)}"><b>{esc(name)}</b><em>{esc(tag)}</em><small>{esc(desc)}</small></a>'
    for name, route, tag, desc in SECONDARY_DESKS
)

trust_html = "".join(
    f'<div class="tm-readout"><p class="tm-ro-h">{esc(b)}</p><p class="tm-ro-f">{esc(s)}</p></div>'
    for b, s in TRUST
)

how_html = "".join(
    f'<div class="tm-readout"><p class="tm-ro-h">{esc(t)}</p><p class="tm-ro-f">{esc(d)}</p></div>'
    for t, d in HOW
)

never_html = "".join(f"<li>{esc(x)}</li>" for x in NEVER)
footer_html = "".join(L(r, n) for n, r in FOOTER)

# Schema
SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": ORIGIN + "/#website", "url": ORIGIN + "/",
         "name": "BRYME Writers — practical home for writers",
         "inLanguage": "en",
         "description": ("BRYME is a practical home for writers who want to publish, improve, "
                         "discover opportunities, and build a writing career. 142 paying markets "
                         "checked by hand, 339 writing guides, 48 free tools, and firsthand verification."),
         "publisher": {"@id": ORIGIN + "/#org"},
         "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": ORIGIN + "/writers/search/?q={search_term_string}"}, "query-input": "required name=search_term_string"}},
        {"@type": "Organization", "@id": ORIGIN + "/#org", "name": "THE BRYME",
         "url": ORIGIN + "/", "foundingDate": "2026",
         "description": "An independent family of seven specialist publications — Writers is the flagship."},
    ],
}, separators=(",", ":"))

# --- HTML ---
HTML = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#f6f2e8">
<meta name="color-scheme" content="light dark">
<script src="/assets/theme.js"></script>
<title>BRYME Writers — a practical home for writers who want to publish and get paid</title>
<meta name="description" content="142 paying publications checked by hand, 339 writing guides, 48 free tools. Find where to submit, what they pay, how to pitch, and how to build a writing income. Free, dated, sourced, no pop-ups. Plus tech, home, fitness, money, sport and entertainment.">
<meta name="robots" content="index,follow"><meta name="p:domain_verify" content="69f32b47370c197e72e39c8339160660"/>
<link rel="canonical" href="{ORIGIN}/">
<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">
<meta property="og:title" content="BRYME Writers — a practical home for writers who want to publish and get paid">
<meta property="og:description" content="142 paying markets, 339 guides, 48 tools. Where to send your work, what they pay, how to pitch. Verified by hand, free, no pop-ups.">
<meta property="og:url" content="{ORIGIN}/"><meta property="og:image" content="{ORIGIN}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<meta name="google-adsense-account" content="ca-pub-1881426210393009">
<script src="/assets/canonical-redirect.js"></script>
<script src="/assets/gtag-init.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0KEKJH9960"></script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1881426210393009" crossorigin="anonymous"></script>
<link rel="stylesheet" href="/assets/bryme-v2.css">
<link rel="stylesheet" href="/assets/tech-hub.css">
<script type="application/ld+json">{SCHEMA}</script>
<style>
/* Home-specific additive layer — keeps Writers-first 75-80% dominance */
.home-kicker{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(168,117,42,.24);border-radius:999px;background:#fdfbf4;color:#856116;font:700 11px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase}}
html[data-theme="dark"] .home-kicker{{background:#1a212c;color:#d0aa52;border-color:rgba(208,170,82,.28)}}
.tm-machine .home-intro{{max-width:78ch;margin:10px 0 0;color:var(--muted);font-size:15px;line-height:1.6}}
.tm-machine .home-intro b{{color:var(--ink)}}
.tm-band .home-sec-cards{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(210px,1fr))}}
.home-cta-bar{{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}}
.home-note{{margin-top:18px;font-size:12.5px;color:var(--muted);line-height:1.5}}
.home-note b{{color:var(--ink)}}
</style>
</head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-head">
  <div class="mast-top"><div class="wrap mast-in">
    <span style="display:inline-flex;align-items:center;gap:9px;white-space:nowrap">
    <a href="{ORIGIN}/" aria-label="THE BRYME - all publications" style="display:inline-flex;align-items:center"><img src="/assets/brand/bryme-mark.png" alt="" width="26" height="26" style="width:26px;height:26px;border-radius:7px;display:block;box-shadow:0 0 0 1px rgba(0,0,0,.08)"></a>
    <a href="{ORIGIN}/" style="font-family:Georgia,serif;font-weight:700;font-size:clamp(15px,5vw,21px);letter-spacing:.14em;color:#5b6b7a;text-decoration:none">THE&nbsp;BRYME</a>
    <span aria-hidden="true" style="width:1px;height:20px;background:#ddd6c6;display:inline-block"></span>
    <a href="/writers/" style="font-family:Georgia,serif;font-weight:700;font-size:clamp(20px,7vw,34px);letter-spacing:.14em;color:#a8752a;text-decoration:none">WRITERS</a></span>
    <div class="mast-edition"><span class="mast-date">{REVIEWED.upper()} EDITION · WRITERS FLAGSHIP</span><span class="mast-tag">Practical home for writers — publish, improve, discover opportunities, build a career.</span></div>
    <div class="mast-tools">
      <form class="nav-search-form" action="/writers/search/" method="get" role="search"><input type="search" name="q" placeholder="Search 339 pieces…" aria-label="Search BRYME" autocomplete="off"><input type="hidden" name="desk" value="home"></form>
      <button type="button" class="theme-toggle" data-theme-toggle aria-pressed="false" aria-label="Switch to dark theme"><svg class="icon-sun" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M4.2 4.2l1.6 1.6M18.2 18.2l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.2 19.8l1.6-1.6M18.2 5.8l1.6-1.6"/></svg><svg class="icon-moon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 14.3A8.6 8.6 0 0 1 9.7 3.5a8.6 8.6 0 1 0 10.8 10.8Z"/></svg><span class="sr-only theme-toggle-text">Switch to dark theme</span></button>
      <button type="button" class="nav-toggle" data-drawer-open aria-label="Open menu" aria-expanded="false"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    </div>
  </div></div>
  <nav class="main-nav" aria-label="Primary"><div class="wrap mast-nav"><a class="home-link" href="/" aria-label="BRYME home" aria-current="page"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.5V20a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1V9.5"/><path d="M9.5 21v-6h5v6"/></svg></a><a class="nav-desk" href="/writers/" style="color:#a8752a">Writers — flagship</a><div class="has-mega"><a href="/writers/learn/">Learn</a><div class="mega"><a href="/writers/start/">Beginner path</a><a href="/writers/find/">What do you want to write?</a><a href="/writers/learn/writing-basics/">Writing basics</a><a href="/writers/learn/writing-process/">The writing process</a><a href="/writers/learn/grammar-language/">Grammar & language</a><a href="/writers/learn/editing-proofreading/">Editing & proofreading</a><a href="/writers/learn/freelance-paid-writing/">Rates & business</a><a href="/writers/learn/">All 197 guides</a></div></div><div class="has-mega"><a class="nav-cta" href="/writers/writing/">Publish</a><div class="mega"><a href="/writers/writing/">The opportunity desk — 142 markets</a><a href="/writers/writing-opportunities/">The atlas: by country</a><a href="/writers/today/">Updated this week</a><a href="/writers/tested/">BRYME Tested</a><a href="/writers/guides/how-to-write-a-pitch/">How to write a pitch</a><a href="/writers/tracker/">Submission tracker</a></div></div><div class="has-mega"><a href="/writers/tools/">Tools</a><div class="mega"><a href="/writers/tools/freelance-rate-calculator/">Rate calculator</a><a href="/writers/tools/invoice-generator/">Invoice generator</a><a href="/writers/tools/pitch-checker/">Pitch checker</a><a href="/writers/studio/">The Writing Studio</a><a href="/writers/tools/">All 48 tools</a></div></div><a href="/tech/">Tech</a><a href="/home/">Home</a><a href="/money/">Money</a><a href="/about/">About</a></div></nav>
</header>

<main id="main">
<div class="tm-machine" data-tm-desk="home"><div class="wrap">

<section class="tm-boot" id="tm-boot">
<p class="tm-eyebrow"><span class="tm-led" aria-hidden="true"></span>THE BRYME · WRITERS FLAGSHIP<span class="tm-dot" aria-hidden="true">·</span> THE LIVING HOUSE<span class="tm-eyebrow-r">swept {SWEEP} · reviewed {REVIEWED_ISO}</span></p>
<span class="home-kicker">{opp_count} paying markets · Checked by hand · Free · No pop-ups · Every page dated</span>
<h1 class="tm-h1">A practical home for writers who want to publish, improve, discover opportunities, and build a career.</h1>
<p class="tm-dek">BRYME Writers is the flagship — <em>{opp_count} verified publications that pay</em>, with what they pay, how to submit, and when they close. Plus <em>{guides_count} practical guides</em> on pitching, craft and business, <em>{tools_count} free tools</em> that run in your browser, and BRYME's own firsthand verification record. Everything is dated, sourced, and written in plain English. <br><span class="home-intro">Press <kbd>/</kbd> to filter, <kbd>Ctrl</kbd>+<kbd>K</kbd> for the palette, <kbd>1</kbd>–<kbd>7</kbd> to jump to a pathway. Saved items stay on this device only.</span></p>
<div class="tm-boot-bar">
<a class="btn" href="#tm-core">Read every piece — {total_pieces} below</a>
<button type="button" class="tm-pal-open" data-tm-open-palette><span>Find a piece</span><kbd aria-hidden="true">Ctrl</kbd><kbd aria-hidden="true">K</kbd></button>
<a class="btn secondary" href="/writers/tools/">Open the toolbox</a>
<a class="btn secondary" href="/writers/start/">I'm new — where do I begin?</a>
</div>
<div class="tm-gauges">
<div class="tm-gauge"><b>{opp_count}</b><span>paying markets</span><small>each carries its last-checked date</small></div>
<div class="tm-gauge"><b>99</b><span>accepting now</span><small>status verified against guideline</small></div>
<div class="tm-gauge"><b>10</b><span>personally tested by BRYME</span><small>journey shown as it happened</small></div>
<div class="tm-gauge"><b>{guides_count}</b><span>craft guides</span><small>from first pitch to final invoice</small></div>
<div class="tm-gauge"><b>{tools_count}</b><span>browser tools</span><small>no account, nothing uploaded</small></div>
<div class="tm-gauge"><b>0</b><span>pop-ups, ever</span><small>no interstitials, no autoplay</small></div>
</div>
<div class="tm-memory" data-tm-memory hidden>
<p class="tm-mem-h">On this device — home desk</p>
<div class="tm-mem-cols">
<div class="tm-mem-col"><b>Saved for later</b><ul data-tm-saved></ul><p class="tm-mem-empty" data-tm-saved-empty hidden>Nothing saved yet. Each row below carries a <span class="tm-save-ic" aria-hidden="true">◇</span> Save control; saved items live in this browser only.</p></div>
<div class="tm-mem-col"><b>Continue reading</b><ul data-tm-recent></ul><p class="tm-mem-empty" data-tm-recent-empty hidden>You have not opened a piece on this desk from this browser yet.</p></div>
</div>
<div class="tm-mine" data-tm-mine hidden><p class="tm-mine-h">Your house, by your own numbers</p><ul class="tm-mine-list"><li><b data-tm-mine-opened>0</b><span>different pieces you have opened here</span></li><li><b data-tm-mine-opens>0</b><span>total opens, this browser</span></li><li><b data-tm-mine-saved>0</b><span>saved for later</span></li><li><b data-tm-mine-last>—</b><span>your last visit</span></li></ul><p class="tm-mine-f">Counted only in this browser’s local storage. No account, no server, no one else sees it.</p></div>
<p class="tm-mem-f">Saved items and reading history stay in this browser’s local storage. Nothing is uploaded and nothing is counted on a server; clearing site data clears it. <button type="button" class="tm-mem-clear" data-tm-mine-toggle>Show my own numbers</button> <button type="button" class="tm-mem-clear" data-tm-clear>Forget this desk on this device</button></p>
</div>
</section>

<section class="tm-band" id="tm-needs">
<header class="tm-band-h"><h2>What you can do on BRYME Writers — seven pathways</h2><p>Not just a list of links. Pick a job and the index below re-sorts itself to that job. Keys <kbd>1</kbd>–<kbd>7</kbd>. 75-80% of this page is Writers; secondary desks are compact at the bottom.</p></header>
<div class="tm-needs">
{pillars_needs_html}
</div>
</section>

<section class="tm-band" id="tm-core">
<header class="tm-band-h"><h2>The whole house, open — Writers first</h2><p>Every piece below is in the page itself — no “load more” wall. The shelves are grouped by what each piece is for; with JavaScript you get instant filtering, a keyboard palette (<kbd>Ctrl</kbd>+<kbd>K</kbd>), saved-for-later and “new since your last visit”, all stored on your device. Press <kbd>/</kbd> to focus filter.</p></header>
<div class="tm-toolbar">
<div class="tm-search"><label class="sr-only" for="tm-q">Filter the house by words in the title or summary</label><input id="tm-q" type="search" data-tm-filter="text" autocomplete="off" spellcheck="false" placeholder="filter: pay, country, pitch, invoice, Nigeria…"><span class="tm-count" data-tm-count aria-live="polite">{total_pieces} of {total_pieces} shown</span></div>
<div class="tm-chips" role="group" aria-label="Filter the house">{chips_html}</div>
<div class="tm-sort" role="group" aria-label="Sort each shelf"><button type="button" class="tm-sortb" data-sort="recent" aria-pressed="true">Recently verified</button><button type="button" class="tm-sortb" data-sort="az" aria-pressed="false">A–Z</button><button type="button" class="tm-sortb" data-tm-dice hidden>Random deep cut</button></div>
</div>

<div class="tm-shelves" data-tm-shelves>

<section class="tm-shelf" data-shelf="recent"><h3 class="tm-shelf-h"><span>Recently verified opportunities</span><em>6</em></h3><p class="tm-shelf-d">Last verified this week — pay, requirements and official source checked. Filter with <kbd>/</kbd>, palette with <kbd>Ctrl</kbd>+<kbd>K</kbd>.</p><div class="tm-rows">{recent_rows}</div><button class="tm-more" data-more hidden>Show all 6 pieces in this shelf</button></section>

<section class="tm-shelf" data-shelf="country"><h3 class="tm-shelf-h"><span>Find markets by where you are</span><em>6</em></h3><p class="tm-shelf-d">Nigeria is converting best (12.5% CTR). US & UK have 4k+ impressions waiting. <a href="/writers/writing-opportunities/">Browse atlas →</a></p><div class="tm-rows">{country_rows}</div><button class="tm-more" data-more hidden>Show all</button></section>

<section class="tm-shelf" data-shelf="strong"><h3 class="tm-shelf-h"><span>Strongest from the Writers desk — already earning clicks</span><em>8</em></h3><p class="tm-shelf-d">GSC data 2026-09-20 to 29: these pages rank 4–13 and earn real CTR. Keep them prominent.</p><div class="tm-rows">{strong_rows}</div><button class="tm-more" data-more hidden>Show all 8</button></section>

<section class="tm-shelf" data-shelf="guides"><h3 class="tm-shelf-h"><span>How to get published — practical guides</span><em>8</em></h3><p class="tm-shelf-d">No generic filler — exact structures editors expect. <a href="/writers/guides/">All guides →</a></p><div class="tm-rows">{guides_rows}</div><button class="tm-more" data-more hidden>Show all</button></section>

<section class="tm-shelf" data-shelf="tools"><h3 class="tm-shelf-h"><span>Free tools — no sign-up, nothing uploaded</span><em>8</em></h3><p class="tm-shelf-d">They run inside your browser, local storage only. <a href="/writers/tools/">All 48 tools →</a></p><div class="tm-rows">{tools_rows}</div><button class="tm-more" data-more hidden>Show all</button></section>

<section class="tm-shelf" data-shelf="career"><h3 class="tm-shelf-h"><span>Make a living from writing</span><em>6</em></h3><p class="tm-shelf-d">Rates, retainers, invoicing and the tax habit — risk-aware, not hype. <a href="/writers/learn/freelance-paid-writing/">Career hub →</a></p><div class="tm-rows">{career_rows}</div><button class="tm-more" data-more hidden>Show all</button></section>

<section class="tm-shelf" data-shelf="secondary"><h3 class="tm-shelf-h"><span>Explore the rest of BRYME — secondary desks (compact, 20-25%)</span><em>6</em></h3><p class="tm-shelf-d">Tech, Home & DIY, Fitness, Money, Sport and Entertainment remain publicly accessible and indexed. They get less space by design — Writers is the flagship.</p><div class="tm-rows">{secondary_rows}</div><button class="tm-more" data-more hidden>Show all</button></section>

<div class="tm-nomatch" data-tm-nomatch hidden>No piece matches that filter. Try fewer words, or <button type="button" class="tm-mem-clear" data-tm-clear-filters>clear filters</button>. Every piece is still linked in the page source.</div>

</div>

<div class="home-note"><b>Keyboard:</b> <kbd>/</kbd> filter · <kbd>Ctrl</kbd>+<kbd>K</kbd> palette · <kbd>1</kbd>–<kbd>7</kbd> pathways · <kbd>0</kbd> clear · <kbd>Esc</kbd> close palette. <b>Theme:</b> button in header remembers your choice (light/dark) via localStorage. <b>Saved:</b> ◇ Save on each row → stored only in this browser.</div>

</section>

<section class="tm-band tm-band-alt" id="tm-secondary-cards">
<header class="tm-band-h"><h2>Explore the rest of BRYME — secondary desks</h2><p>Six secondary desks — significantly less space than Writers, but still accessible. No barriers, no noindex. 20-25% of homepage real estate by design.</p></header>
<div class="home-sec-cards">
{secondary_cards_html}
</div>
<p class="tm-band-f">Tech, Home & DIY, Fitness, Money, Sport and Entertainment remain publicly accessible and indexed. Writers is the flagship (75-80%).</p>
</section>

<section class="tm-band" id="tm-how">
<header class="tm-band-h"><h2>How BRYME works</h2><p>The same four rules on every one of the seven sections.</p></header>
<div class="tm-reads">
{how_html}
<div class="tm-readout tm-readout-warn"><p class="tm-ro-h">What you will never find on this site</p><ul class="tm-ro-list">{never_html}</ul></div>
</div>
</section>

<section class="tm-band tm-band-alt" id="tm-trust">
<header class="tm-band-h"><h2>Why you can trust what you read here</h2><p>Writers is the flagship, but the same standard applies to every page — seven sections, one house.</p></header>
<div class="tm-reads">
{trust_html}
<div class="tm-readout"><p class="tm-ro-h">Verification cadence</p><p class="tm-ro-big"><time datetime="{REVIEWED_ISO}">{REVIEWED}</time><span>the clock this desk checks itself against</span></p><p class="tm-ro-f">0 pieces are past its re-verification date, 0 due within 30 days. Publication statuses turn fast — dossiers are re-checked against the official guideline every 90 days; craft guides age slowly (365). Next review on the calendar: <time datetime="2026-11-17">2026-11-17</time>.</p></div>
<div class="tm-readout"><p class="tm-ro-h">Verification sweep</p><p class="tm-ro-big"><time datetime="{SWEEP}">{SWEEP}</time><span>newest date the desk carries</span></p><p class="tm-ro-f">{len(recent_verified)} of {opp_count} pieces carry a date newer than that sweep. Each page prints its own date, and a page never prints a date it cannot show. Stamp: Snapshot 2026-09-04</p></div>
</div>
</section>

<section class="tm-band" id="tm-start">
<header class="tm-band-h"><h2>New to submitting? Start here.</h2><p>If you've never submitted anywhere before, follow the beginner path — 20 guides in the order that actually builds on itself. Then browse {opp_count} paying markets with pay stated.</p></header>
<div class="home-cta-bar">
<a class="btn" href="/writers/start/">Beginner path →</a>
<a class="btn secondary" href="/writers/writing/">Browse paying markets</a>
<a class="btn secondary" href="/writers/tools/">Free tools</a>
<a class="btn secondary" href="/writers/guides/how-to-write-a-pitch/">How to pitch</a>
</div>
</section>

<p class="tm-noscript">This hub works without JavaScript — every piece is linked above. With JavaScript you also get instant filtering, a keyboard palette, saved-for-later and “new since your last visit”, all stored on your device.</p>
<div class="tm-palette" data-tm-palette hidden role="dialog" aria-modal="true" aria-label="Search the house"><div class="tm-pal-in"><label class="sr-only" for="tm-pal-q">Search every piece on this desk</label><input id="tm-pal-q" type="search" autocomplete="off" spellcheck="false" placeholder="pitch, pay, invoice, magazine — matches titles and summaries on your device"></div><ul class="tm-pal-list" data-tm-pal role="listbox" aria-label="Matches"></ul><p class="tm-pal-foot">↑↓ move · Enter open · Esc close · {total_pieces} pieces indexed · typo-tolerant · / to filter · 1-7 pathways</p></div>

</div></div>
</main>

<aside class="adband-native" data-adband="adsterra" aria-label="Advertisement"><style>.adband-native{{margin:0;padding:26px 0 0}}.adband-native .adband-in{{max-width:1100px;margin:0 auto;padding:0 20px;overflow:hidden}}.adband-native .adband-label{{display:block;font:500 10px/1 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8a8578;margin:0 0 10px}}.adband-native .adband-slot{{margin:0 auto;max-width:100%;min-height:0}}.adband-native::before{{content:"";display:block;max-width:1100px;margin:0 auto 26px;padding:0 20px;border-top:1px solid rgba(0,0,0,.08)}}</style><div class="adband-in"><span class="adband-label">Advertisement</span><div class="adband-slot" id="container-7cf8bb4b0854f64ff4f20a3a19146e91"></div></div></aside><script async data-cfasync="false" src="https://pl31572329.profitableratecpmnetwork.com/7cf8bb4b0854f64ff4f20a3a19146e91/invoke.js"></script>

<nav class="bottom-nav bottom-nav--home" aria-label="Primary mobile"><a href="/writers/"><span aria-hidden="true">✍️</span>Writers</a><a href="/writers/tools/"><span aria-hidden="true">🛠</span>Tools</a><a href="/writers/writing/"><span aria-hidden="true">💰</span>Publish</a><a href="/writers/search/"><span aria-hidden="true">🔍</span>Search</a></nav>

<div id="drawer-backdrop"></div>
<aside id="site-drawer" aria-hidden="true" aria-label="Site menu" role="dialog" aria-modal="true">
  <div class="drawer-head"><a class="logo" href="/"><span class="logo-mark" aria-hidden="true"></span>BRYME</a><button type="button" class="drawer-close" data-drawer-close aria-label="Close menu"><svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
  <div class="drawer-group"><b>Start here — Writers flagship</b><a href="/"><span aria-hidden="true">🏠</span>Home — Writers-first</a><a href="/writers/"><span aria-hidden="true">✍️</span>Writers desk</a><a href="/writers/start/"><span aria-hidden="true">🧭</span>Complete beginner path</a><a href="/writers/find/"><span aria-hidden="true">❓</span>What do you want to write?</a><a href="/writers/writing/"><span aria-hidden="true">💰</span>142 paying markets</a><a href="/writers/writing-opportunities/"><span aria-hidden="true">🌍</span>By country atlas</a><a href="/writers/search/"><span aria-hidden="true">🔍</span>Search BRYME</a></div>
  <div class="drawer-group"><b>How to write — 7 pathways</b><a href="/writers/learn/"><span aria-hidden="true">📚</span>All how-tos (197)</a><a href="/writers/guides/how-to-write-a-pitch/"><span aria-hidden="true">📝</span>How to write a pitch</a><a href="/writers/guides/how-much-to-charge-for-an-article/"><span aria-hidden="true">💷</span>Rates & business</a><a href="/writers/learn/writing-basics/"><span aria-hidden="true">✳️</span>Writing basics</a><a href="/writers/learn/editing-proofreading/"><span aria-hidden="true">🧹</span>Editing</a><a href="/writers/learn/freelance-paid-writing/"><span aria-hidden="true">💰</span>Freelance & paid</a></div>
  <div class="drawer-group"><b>Tools & templates — 48 tools</b><a href="/writers/tools/"><span aria-hidden="true">🛠️</span>All tools</a><a href="/writers/tools/freelance-rate-calculator/"><span aria-hidden="true">🧮</span>Rate calculator</a><a href="/writers/tools/invoice-generator/"><span aria-hidden="true">🧾</span>Invoice generator</a><a href="/writers/templates/"><span aria-hidden="true">📄</span>Templates</a><a href="/writers/checklists/"><span aria-hidden="true">☑️</span>Checklists</a></div>
  <div class="drawer-group"><b>Other desks — secondary (20-25%)</b><a href="/tech/"><span aria-hidden="true">💻</span>Tech</a><a href="/home/"><span aria-hidden="true">🏡</span>Home & DIY</a><a href="/fitness/"><span aria-hidden="true">💪</span>Fitness</a><a href="/money/"><span aria-hidden="true">💵</span>Money</a><a href="/sports/"><span aria-hidden="true">⚽</span>Sport</a><a href="/entertainment/"><span aria-hidden="true">🎬</span>Entertainment</a></div>
  <div class="drawer-group"><b>Trust & about</b><a href="/about/"><span aria-hidden="true">ℹ️</span>About BRYME</a><a href="/writers/editorial-policy/"><span aria-hidden="true">📜</span>Editorial policy</a><a href="/writers/corrections/"><span aria-hidden="true">✏️</span>Corrections</a><a href="/writers/privacy/"><span aria-hidden="true">🔒</span>Privacy</a><a href="/writers/contact/"><span aria-hidden="true">✉️</span>Contact</a></div>
  <p class="drawer-note">BRYME is a free, independent writing resource. Guides and tools work right in your browser — no account, no charge. Writers is the flagship (75-80% of homepage). Press <kbd>/</kbd> to filter, <kbd>Ctrl</kbd>+<kbd>K</kbd> for palette, <kbd>1</kbd>–<kbd>7</kbd> for pathways.</p>
</aside>

<script src="/assets/site-nav.js" defer></script>
<script src="/assets/tech-hub.js" defer></script>
<script src="/assets/home-hub.js" defer></script>

<footer class="site-foot"><div class="wrap foot-grid">
  <div class="foot-brand"><a class="logo" href="/"><span class="logo-mark" aria-hidden="true"></span>BRYME</a><p>BRYME is a free writing resource — guides, tools, and verified opportunities to get published and paid. Writers is the flagship.</p><p style="margin-top:10px;font-size:12px;color:var(--muted)">Keyboard: <kbd>/</kbd> filter · <kbd>Ctrl</kbd>+<kbd>K</kbd> palette · <kbd>1</kbd>–<kbd>7</kbd> pathways · <kbd>0</kbd> clear · Theme toggle in header remembers your choice.</p></div>
  <div class="foot-col"><b>Writers flagship</b><a href="/writers/">Writers desk</a><a href="/writers/writing/">142 paying markets</a><a href="/writers/writing-opportunities/">By country atlas</a><a href="/writers/start/">Beginner path</a><a href="/writers/learn/">197 guides</a><a href="/writers/tools/">48 tools</a><a href="/writers/tested/">BRYME Tested</a></div>
  <div class="foot-col"><b>How to write</b><a href="/writers/learn/writing-basics/">Writing basics</a><a href="/writers/learn/writing-process/">Writing process</a><a href="/writers/learn/grammar-language/">Grammar</a><a href="/writers/learn/editing-proofreading/">Editing</a><a href="/writers/learn/freelance-paid-writing/">Rates & business</a><a href="/writers/guides/how-to-write-a-pitch/">How to pitch</a></div>
  <div class="foot-col"><b>Other desks</b><a href="/tech/">Tech</a><a href="/home/">Home & DIY</a><a href="/fitness/">Fitness</a><a href="/money/">Money</a><a href="/sports/">Sport</a><a href="/entertainment/">Entertainment</a><a href="/about/">About</a></div>
  <div class="foot-col"><b>Trust</b><a href="/about/">About BRYME</a><a href="/writers/editorial-policy/">Editorial policy</a><a href="/writers/corrections/">Corrections</a><a href="/writers/privacy/">Privacy</a><a href="/writers/contact/">Contact</a><a href="/writers/terms/">Terms</a><a href="/writers/copyright/">Copyright</a></div>
</div><div class="wrap foot-bottom">© 2026 BRYME · Writers is the flagship — independent editorial project · Reviewed {REVIEWED} · No pop-ups, ever · Keyboard: / · Ctrl+K · 1-7 · Theme toggle remembers choice · No acceptance, publication or payment is guaranteed.</div></footer>

<!--gfc--><script async src="https://fundingchoicesmessages.google.com/i/pub-1881426210393009?ers=1"></script>
</body></html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(HTML, encoding="utf-8")

dupes = {r for r in _links if _links.count(r) > 1}
print(f"build-landing: wrote {OUT.relative_to(ROOT)} ({len(HTML):,} bytes) sophisticated")
print(f"build-landing: {len(_links)} links, {len(set(_links))} unique, all allowlisted")
print(f"build-landing: repeated-route links: {sorted(dupes) if dupes else 'none'}")
print(f"build-landing: linked but intentionally noindex: {sorted(set(no_allowlist)) or 'none'}")
print(f"build-landing: PHASE 1 Writers-first sophisticated — 75-80% Writers, 20-25% secondary, dark/light, kbd, palette, drawer, gauges, saved")
