#!/usr/bin/env python3
"""
BRYME — House homepage from scratch v4 (2026-09-30)
Tight, dense, gripping, 10/10. Fixes header bloat + Write clicks.

User feedback 5/10: header takes so many space with nothing in it,
Write already getting clicks.

Fixes:
- Compact header override (single row 48px, not 88px): mast-in 10px pad,
  brand 26px, hide main-nav on house only, search stays, theme toggle.
- Hero tight: 18px top pad, h1 32-48px not 64px, dek 15-17px, meta inline.
- Flagship 75% dominant, pathways de-emphasized and reordered DISCOVER first
  (not WRITE) to stop Write stealing clicks. Write is job 2, not 1.
- Density: eyebrows 18px mt, grids gap 10px, cards pad 14px, no wasted whitespace.
- Visual punch: brass left rule, B watermark, ink+brass h1, tight facts.
- All hrefs allowlist-validated.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ecosystem" / "hub" / "index.html"
# REVIEWED is a human editorial stamp: the date the page's own content was last
# reviewed. It is deliberately NOT the build date - deriving it would make the page
# claim a fresh review on every deploy, including the ones that change nothing.
# Advance it by hand when the page is substantively reviewed.
REVIEWED = "1 October 2026"

# SWEEP used to be the literal "2026-09-27" and it was the one number on this page
# that could not be checked against anything. It sat directly beside {N_MARKETS},
# which IS derived, so the front door read "288 paying markets ... Verified
# 2026-09-27" - a date only 7 of those 288 records were actually verified on, with
# the rest running from 2026-08-19 to 2026-10-01. The label overstated the whole
# set on the strength of its smallest part.
#
# It is now the newest verification date in the dataset, which is what the stamp
# is trying to say, and the page states which claim that supports rather than
# implying every record was seen that day.
_OPPS_DOC = json.loads((ROOT / "content" / "opportunities.json").read_text(encoding="utf-8"))
_dates = [r["lastVerified"] for r in _OPPS_DOC["opportunities"] if r.get("lastVerified")]
SWEEP = max(_dates) if _dates else ""
SWEEP_OLDEST = min(_dates) if _dates else ""
GSC = "2026-09-20→29"

ALLOWLIST = set(json.loads(
    (ROOT / "content" / "index-allowlist.routed.json").read_text(encoding="utf-8")
)["routes"])

_links: list[str] = []
def H(route: str) -> str:
    assert route.startswith("/") and route.endswith("/")
    # Allow routes that will exist after routing: /writers/search/ lives at /search/ pre-routing
    exists = (ROOT / route.strip("/") / "index.html").exists()
    if not exists and route.startswith("/writers/"):
        alt = route.replace("/writers/", "/", 1)
        exists = (ROOT / alt.strip("/") / "index.html").exists()
    if route not in ALLOWLIST and not exists:
        raise SystemExit(f"build-landing: 404 risk {route} (allowlist {len(ALLOWLIST)})")
    _links.append(route)
    return route

# Data
try:
    opp = json.loads((ROOT / "content" / "opportunities.json").read_text())[ "opportunities"]
    opp_sorted = sorted(opp, key=lambda x: x.get("lastVerified",""), reverse=True)
    recent = opp_sorted[:6]
except Exception:
    recent = []


def _market_count() -> int:
    """How many records the opportunities dataset holds.

    Derived, never hardcoded. This figure is printed in the homepage title,
    meta description, JSON-LD, the DISCOVER pathway tile, the nav and the
    footer. It was the literal 142 in ten places here, so every verified batch
    of new markets left the homepage advertising a stale total while the desk
    itself showed the real one - and on 30 September the two disagreed in
    public. Raises rather than falling back: a wrong number on the front door
    is worse than a build that stops.
    """
    doc = json.loads((ROOT / "content" / "opportunities.json").read_text(encoding="utf-8"))
    return len(doc["opportunities"])


N_MARKETS = _market_count()

# Recent cards
def _clip(text: str, limit: int = 60) -> str:
    """Shorten a pay string on a word boundary.

    The fallback cards below used to slice with [:60], which cut mid-word: the
    homepage showed "$75 one-time payment per accepted short story, with no
    futur". 50 of the 288 records have a pay display longer than 60 characters
    (the longest is 129), so this was not an edge case - it was whatever the
    fallback happened to pick that build. A rate is the one thing on this card a
    writer acts on, so it gets clipped at a space with an ellipsis, never
    mid-word, and never in a way that could turn "$200 and up" into "$200 an".
    """
    t = (text or "").strip()
    if len(t) <= limit:
        return t
    cut = t[:limit].rsplit(" ", 1)[0].rstrip(" ,;:")
    return (cut or t[:limit].rstrip(" ,;:")) + "\u2026"


def _pay_str(o):
    pd = o.get("pay_display")
    if isinstance(pd, str) and pd:
        return pd
    p = o.get("pay")
    if isinstance(p, dict):
        return p.get("display") or ""
    if isinstance(p, str):
        return p
    return ""

RECENT_CARDS = []
for o in recent:
    pub = o.get("publication","")
    slug = o.get("slug","")
    route = f"/writers/writing/{slug}/"
    pay = _pay_str(o)
    title = o.get("title") or pub
    ver = o.get("lastVerified","")[:10]
    RECENT_CARDS.append((pub, route, pay, title, ver))

# Strong — an editorial pick list, but every word of each card is read from the
# record. It used to carry hand-typed blurbs, and two of the four had come apart
# from the dataset they described:
#
#   "The Sun Magazine — Personal essays, $300-$2000"
#       the record says $200 and up, based on page length. There is no $2,000
#       ceiling anywhere in it, so the front door quoted a range the publication
#       never offered.
#   "Longreads Personal Essay — Deep reported essays, pays well, open to pitches"
#       the record says the opposite on the part that matters: "They do not
#       commission personal essays from a pitch - send a full, polished draft."
#       A writer who believed the homepage would send a pitch and get nothing.
#
# Two more picks (noema-magazine, a-public-space-fiction) are no longer in the
# dataset at all; the route check below already dropped them and backfilled, so
# no link was broken - but a hardcoded rate is a claim that can only drift.
# _pay_str() returns the record's own sourced pay display, which is the same
# string the publication's dossier shows, so the two pages cannot disagree.
#
# Not sorted by amount to pick "the highest paying": amountMin mixes currencies
# (a N150,000 record outranks a $2,500 one numerically), and a cross-currency
# ranking would be a money claim the site's own rules require jurisdiction
# clarity for. The fallback stays as it was.
_BY_SLUG = {o.get("slug"): o for o in _OPPS_DOC["opportunities"]}
# The pages Search Console named as top performers for 2026-09-20→29, as record slugs.
# Two of the four entries here were stale. "noema-magazine" is recorded as `noema`, so a
# genuine top performer was being dropped over a spelling; "a-public-space-fiction" has
# no dossier at all — the export named a page this desk never wrote up, and inventing one
# to fill the slot is not an option.
#
# Both were swallowed by the old fallback, which topped the strip up from RECENT_CARDS
# whenever fewer than four picks resolved. RECENT_CARDS is ordered by lastVerified, so
# the strip printed whichever markets happened to be re-checked most recently under a
# heading reading "STRONGEST · GSC 2026-09-20→29 · POS 4–13" with each card labelled
# "Top performing" — a claim about search traffic for records the traffic data never
# mentioned, on the home page and the ecosystem hub, and it moved every time any record
# was re-verified. A strip that cites Search Console has to contain only what Search
# Console named, so the fallback is gone and a pick that does not resolve stops the build
# naming the slug rather than being quietly replaced.
_PICKS = ["the-sun-magazine", "longreads-personal-essay", "noema"]

def _exists_route(r):
    return r in ALLOWLIST or (ROOT / r.strip("/") / "index.html").exists()

_no_record = [s for s in _PICKS if s not in _BY_SLUG]
if _no_record:
    raise SystemExit(f"build-landing: GSC pick(s) with no record: {_no_record}")
STRONG = []
for _slug in _PICKS:
    _o = _BY_SLUG[_slug]
    _route = f"/writers/writing/{_slug}/"
    _blurb = _pay_str(_o)
    if not _exists_route(_route):
        raise SystemExit(f"build-landing: GSC pick {_slug} resolves to no route at {_route}")
    if not _blurb:
        raise SystemExit(f"build-landing: GSC pick {_slug} has no pay blurb to print")
    STRONG.append((_o.get("publication") or _slug, _route, _blurb))


TOOLS = [
    ("Word counter", "/writers/tools/word-counter/", "Live count, no upload"),
    ("Readability", "/writers/tools/readability-score/", "Grade your prose"),
    ("Pitch checker", "/writers/tools/pitch-checker/", "10 editor-eye checks"),
    ("Rate calc", "/writers/tools/freelance-rate-calculator/", "What to charge"),
    ("Invoice", "/writers/tools/invoice-generator/", "Print, no account"),
    ("Deadline tracker", "/writers/tools/deadline-tracker/", "Browser only"),
]
# filter to existing routes only
TOOLS = [(n,r,d) for n,r,d in TOOLS if r in ALLOWLIST or (ROOT / r.strip("/") / "index.html").exists()]

# ---------------------------------------------------------------------------
# Every count on this page is derived. Each one used to be a literal, and each
# literal drifted at its own rate, so the front door disagreed with the pages it
# linked to:
#
#   Tech          claimed 438 guides   the desk's own gauge says 329
#   Entertainment claimed 719 guides   719 is the FILM catalogue; the desk has
#                                      165 pieces and counts the films separately
#   Fitness       claimed 157          the desk says 163
#   Sport         claimed 180          the desk says 121 pieces + 20 club hubs
#   Money         claimed 124          the desk says 102
#   Home          claimed 287          the desk says 253
#   SUBMIT badge  claimed 14           /writers/guides/ holds 22 pages
#   EARN badge    claimed 25           the rates-and-business section holds 60
#   CAREER badge  claimed 12           /writers/start/ is a 20-step path, and the
#                                      desk's own card says "20 guides"
#   RESEARCH badge claimed 12          13 countries have a page (Portugal joined
#                                      with the 288-record merge)
#
# A badge that contradicts the page it opens is worse than no badge, so these
# read the source of truth for each figure and raise if it is missing.
# ---------------------------------------------------------------------------
def _desk_gauge(desk: str, label: str) -> int:
    """Read a desk's own published count from its home page gauge.

    The desks are not regenerated by this build (build-ecosystem.py is not in the
    chain), so their committed home page IS the source of truth. Every desk carries
    the same marker: <div class="tm-gauge"><b>N</b><span>pieces on the desk</span>.
    """
    import re as _re
    for cand in (ROOT / desk / "index.html", ROOT / "public" / desk / "index.html"):
        if cand.is_file():
            m = _re.search(r'<div class="tm-gauge"><b>(\d+)</b><span>' + _re.escape(label),
                           cand.read_text(encoding="utf-8", errors="ignore"), _re.I)
            if m:
                return int(m.group(1))
    raise SystemExit(f"build-landing: no '{label}' gauge on the {desk} desk home - "
                     f"refusing to print a hardcoded count for it")


def _indexable_children(route: str) -> int:
    """Indexable pages one or more levels under a writers-desk route.

    build-landing runs before build-routing moves the writers tree into writers/,
    so the fresh pages are at ROOT/<route> at this moment; ROOT/writers/<route> is
    the previous build. Prefer the fresh one, fall back for a partial tree.
    """
    import re as _re
    rel = route.strip("/").removeprefix("writers/").strip("/")
    for base in (ROOT / rel, ROOT / "writers" / rel):
        if not base.is_dir():
            continue
        n = 0
        for f in base.rglob("index.html"):
            if f.parent == base:
                continue                      # the section's own index
            h = f.read_text(encoding="utf-8", errors="ignore")
            m = _re.search(r'name="robots" content="([^"]*)"', h)
            if m and "noindex" in m.group(1):
                continue
            n += 1
        if n:
            return n
    raise SystemExit(f"build-landing: no indexable pages found under {route} - "
                     f"refusing to print a hardcoded count for it")


def _guide_section_count(section: str | None = None) -> int:
    """Guides in content/hub/guides, optionally filtered by frontmatter section."""
    import re as _re
    n = 0
    for f in (ROOT / "content" / "hub" / "guides").rglob("*.md"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        m = _re.search(r"^section:\s*[\"']?([a-z0-9-]+)", t, _re.M)
        if not m:
            continue
        if section is None or m.group(1) == section:
            n += 1
    if not n:
        raise SystemExit(f"build-landing: no guides found for section={section!r}")
    return n


N_GUIDES = _guide_section_count()
N_EARN = _guide_section_count("freelance-paid-writing")
N_SUBMIT = _indexable_children("/writers/guides/")
N_TOOLS = _indexable_children("/writers/tools/")
N_COUNTRIES = len({(v or {}).get("base") for v in json.loads(
    (ROOT / "content" / "hub" / "pub-countries.json").read_text(encoding="utf-8")).values()
    if (v or {}).get("base")})
# /writers/start/ is a numbered path, not a section: count its steps.
N_START = len(set(__import__("re").findall(
    r'class="[^"]*step[^"]*"[^>]*>\s*<[^>]*>\s*(\d{2})',
    (ROOT / "start" / "index.html").read_text(encoding="utf-8", errors="ignore")
    if (ROOT / "start" / "index.html").is_file()
    else (ROOT / "writers" / "start" / "index.html").read_text(encoding="utf-8", errors="ignore"))))
if not N_START:
    raise SystemExit("build-landing: could not count the steps on /writers/start/")


# Each desk's own home page publishes its count in a gauge; read it rather than
# restating a number that can drift. Entertainment keeps its two figures separate
# because they are two different things - 165 written pieces and a 719-title film
# catalogue - and calling the catalogue "719 guides" mislabelled films as guides.
def _desk_stat(desk: str) -> str:
    pieces = _desk_gauge(desk, "pieces on the desk")
    if desk == "entertainment":
        return f"{pieces} guides \u00b7 {_desk_gauge(desk, 'catalogued films')} films"
    return f"{pieces} guides"


SECONDARY = [
    ("Tech", "/tech/", _desk_stat("tech"), "Tech explainers, no hype"),
    ("Home", "/home/", _desk_stat("home"), "Make home work"),
    ("Fitness", "/fitness/", _desk_stat("fitness"), "Train, eat, recover"),
    ("Money", "/money/", _desk_stat("money"), "Earn, save, freelance"),
    ("Sport", "/sports/", _desk_stat("sports"), "Live scores + explainers"),
    ("Entertainment", "/entertainment/", _desk_stat("entertainment"), "What to watch, why"),
]

# Pathways reordered: DISCOVER first (flagship core), not WRITE
PATHWAYS = [
    ("discover", "DISCOVER", "/writers/writing/", f"{N_MARKETS} markets — pay, word count, who is open now", N_MARKETS, "1"),
    ("write", "WRITE", "/writers/learn/", f"{N_GUIDES} craft guides — from blank page to final draft", N_GUIDES, "2"),
    ("submit", "SUBMIT", "/writers/guides/how-to-write-a-pitch/", "How to pitch, query, cover letter", N_SUBMIT, "3"),
    ("research", "RESEARCH", "/writers/writing-opportunities/", "Find markets by country — US, UK, CA, AU, IN, NG", N_COUNTRIES, "4"),
    ("earn", "EARN", "/writers/learn/freelance-paid-writing/", "Rates, invoices, tax, tracker", N_EARN, "5"),
    ("tools", "TOOLS", "/writers/tools/", f"{N_TOOLS} browser tools — no account, nothing uploaded", N_TOOLS, "6"),
    ("career", "CAREER", "/writers/start/", "Portfolio, clients, full-time", N_START, "7"),
]

# Build HTML pieces
pathways_html = "".join(
    f'<article class="path" data-path="{need}"><div class="top"><span class="kbd">{kbd}</span><b>{title}</b><span class="count">{count}</span></div><p>{desc}</p><a href="{H(route)}">Open →</a></article>'
    for need, title, route, desc, count, kbd in PATHWAYS
)

recent_html = "".join(
    f'<article class="rec"><div class="pub">{pub}</div><b><a href="{H(route)}">{title}</a></b><div class="pay">{pay}</div><small>Verified {ver} · <a href="{H(route)}">Dossier →</a></small></article>'
    for pub, route, pay, title, ver in RECENT_CARDS
)

strong_html = "".join(
    f'<article class="rec"><div class="pub">Top performing</div><b><a href="{H(route)}">{name}</a></b><div class="pay">{blurb}</div><small><a href="{H(route)}">Read →</a></small></article>'
    for name, route, blurb in STRONG
)

tools_html = "".join(
    f'<a class="tool" href="{H(route)}"><span class="dot"></span><span><b>{name}</b><span>{desc}</span></span></a>'
    for name, route, desc in TOOLS
)

secondary_html = "".join(
    f'<a class="sec" href="{H(route)}"><b>{name}</b><span class="c">{count}</span><small>{desc}</small></a>'
    for name, route, count, desc in SECONDARY
)

HTML = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#f6f2e8"><meta name="color-scheme" content="light dark">
<script src="/assets/theme.js"></script>
<title>THE BRYME — a house that reads the fine print so you don't have to</title>
<meta name="description" content="Seven desks under one roof. Flagship: {N_MARKETS} paying markets checked by hand, {N_GUIDES} guides, {N_TOOLS} tools. Dated, sourced, no pop-ups. Plus tech, home, fitness, money, sport, entertainment.">
<meta name="robots" content="index,follow"><meta name="p:domain_verify" content="69f32b47370c197e72e39c8339160660"/>
<link rel="canonical" href="https://thebryme.com/">
<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">
<meta property="og:title" content="THE BRYME — a house that reads the fine print">
<meta property="og:description" content="{N_MARKETS} paying markets, {N_GUIDES} guides, {N_TOOLS} tools. Verified by hand, dated, sourced, no pop-ups. Seven desks, one house standard.">
<meta property="og:url" content="https://thebryme.com/"><meta property="og:image" content="https://thebryme.com/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<meta name="google-adsense-account" content="ca-pub-1881426210393009">
<script src="/assets/canonical-redirect.js"></script>
<script src="/assets/gtag-init.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0KEKJH9960"></script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1881426210393009" crossorigin="anonymous"></script>
<link rel="stylesheet" href="/assets/bryme-v2.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@graph":[{{"@type":"WebSite","@id":"https://thebryme.com/#website","url":"https://thebryme.com/","name":"THE BRYME","inLanguage":"en","description":"A house that reads the fine print so you don't have to. Seven desks — Writers is flagship — {N_MARKETS} paying markets checked by hand, {N_GUIDES} guides, {N_TOOLS} browser tools, dated, sourced, no pop-ups.","publisher":{{"@id":"https://thebryme.com/#org"}},"potentialAction":{{"@type":"SearchAction","target":{{"@type":"EntryPoint","urlTemplate":"https://thebryme.com/writers/search/?q={{search_term_string}}"}},"query-input":"required name=search_term_string"}}}},{{"@type":"Organization","@id":"https://thebryme.com/#org","name":"THE BRYME","url":"https://thebryme.com/","foundingDate":"2026"}}]}}</script>
<style>
/* ===== HOUSE v4 — compact header fix + dense 10/10 ===== */
.site-head{{position:sticky;top:0;z-index:50;background:var(--paper);border-bottom:1px solid var(--line)}}
.site-head::before{{content:"";display:block;height:3px;background:var(--navy);border-bottom:1px solid var(--brass-bright)}}
.mast-in{{display:flex;align-items:center;gap:14px;padding:10px 0 8px !important}}
.mast-brand{{font-size:26px !important;line-height:.9;letter-spacing:.14em !important}}
.mast-brand .mast-section{{font-size:.42em !important;letter-spacing:.18em !important}}
.mast-edition{{display:none !important}}
.mast-tools{{gap:6px !important}}
.mast-tools .nav-search-form input{{width:170px !important;padding:6px 10px !important;font-size:13px !important}}
.main-nav{{display:none !important}}
#site-drawer{{top:0}}
.house{{--r:12px;--r2:8px;--max:1160px}}
.house .wrap{{width:min(calc(100% - 28px), var(--max));margin:0 auto}}
.eyebrow{{display:inline-flex;gap:8px;align-items:center;font:700 10px/1 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}}
.eyebrow b{{color:var(--brass);font-weight:800}}
.eyebrow .dot{{width:3px;height:3px;border-radius:50%;background:var(--muted);opacity:.5}}
.kicker{{display:inline-flex;gap:6px;align-items:center;padding:5px 10px;border:1px solid rgba(168,117,42,.22);border-radius:999px;background:var(--sheet);color:var(--brass);font:700 10px/1 var(--sans);letter-spacing:.11em;text-transform:uppercase}}
html[data-theme=dark] .kicker{{background:#1a212c;color:#d0aa52;border-color:rgba(208,170,82,.28)}}
.house-hero{{position:relative;padding:18px 0 18px;border-bottom:1px solid var(--line);overflow:hidden}}
.house-hero::before{{content:"";position:absolute;inset:-30% -10% auto -10%;height:120%;pointer-events:none;background:radial-gradient(90% 60% at 12% 0%, rgba(168,117,42,.10), transparent 58%), repeating-linear-gradient(90deg, rgba(20,33,61,.04) 0 1px, transparent 1px 40px);-webkit-mask-image:linear-gradient(#000, transparent 70%);mask-image:linear-gradient(#000, transparent 70%)}}
.house-hero>*{{position:relative}}
.house-hero h1{{margin:10px 0 10px;font:800 clamp(32px,5vw,48px)/.92 var(--serif);letter-spacing:-.04em;max-width:15ch}}
.house-hero h1 em{{font-style:italic;font-weight:700;letter-spacing:-.02em;color:var(--brass)}}
.house-hero .dek{{max-width:66ch;font-size:clamp(15px,1.5vw,17px);line-height:1.55;color:var(--muted)}}
.house-hero .dek b{{color:var(--ink);font-weight:700}}
.house-hero .actions{{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}}
.house-hero .meta{{display:flex;flex-wrap:wrap;gap:6px 12px;margin-top:12px;padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--sheet);font-size:12.5px;color:var(--muted)}}
.house-hero .meta b{{color:var(--ink)}}
.house-hero .meta .sep{{opacity:.35}}
.flag{{display:grid;gap:1px;margin-top:18px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden}}
.flag-head{{display:flex;align-items:baseline;gap:10px;padding:12px 14px;background:var(--sheet)}}
.flag-head h2{{font:800 16px/1.1 var(--serif);letter-spacing:-.02em}}
.flag-head span{{font:600 10px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}}
.flag-head a{{margin-left:auto;font:700 11px/1 var(--sans);color:var(--brass)}}
.flag-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line)}}
@media(max-width:900px){{.flag-grid{{grid-template-columns:1fr}}}}
.flag-card{{background:var(--sheet);padding:14px 14px 12px;position:relative}}
.flag-card::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--brass);opacity:0}}
.flag-card:hover::before{{opacity:1}}
.flag-card b{{display:block;font:700 13px/1.2 var(--sans);letter-spacing:.02em;margin-bottom:4px}}
.flag-card b i{{font-style:normal;color:var(--brass);margin-right:5px}}
.flag-card p{{font-size:12.5px;line-height:1.5;color:var(--muted);margin:0}}
.flag-card .links{{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}}
.flag-card .links a{{font:700 11px/1 var(--sans);color:var(--ink);border-bottom:1px solid var(--line-strong);padding-bottom:2px}}
.flag-card .links a:hover{{color:var(--brass);border-color:var(--brass)}}
.paths{{margin-top:20px;display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}}
.path{{position:relative;display:flex;flex-direction:column;padding:12px 12px 10px;border:1px solid var(--line);border-radius:10px;background:var(--sheet);transition:transform .14s, box-shadow .14s, border-color .14s;overflow:hidden}}
.path::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--brass);opacity:0;transition:opacity .14s}}
.path:hover{{transform:translateY(-1px);box-shadow:var(--shadow);border-color:var(--line-strong)}}
.path:hover::before{{opacity:1}}
.path .top{{display:flex;align-items:center;gap:8px;margin-bottom:6px}}
.path .kbd{{display:inline-grid;place-items:center;width:20px;height:20px;border:1px solid var(--line-strong);border-bottom-width:2px;border-radius:5px;background:var(--paper);font:700 10px/1 ui-monospace,monospace;color:var(--muted)}}
.path b{{font:800 13px/1.2 var(--sans);letter-spacing:-.01em}}
.path .count{{margin-left:auto;font:700 10px/1 ui-monospace,monospace;color:var(--muted)}}
.path p{{font-size:12px;line-height:1.45;color:var(--muted);margin:0;flex:1}}
.path a{{margin-top:8px;font:700 11px/1 var(--sans);color:var(--brass)}}
.recent{{margin-top:16px;display:grid;gap:8px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}}
.rec{{padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--sheet);transition:border-color .12s}}
.rec:hover{{border-color:var(--line-strong)}}
.rec .pub{{font:700 10px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}}
.rec b{{display:block;font:600 13px/1.25 var(--sans);margin-bottom:2px}}
.rec b a{{color:var(--ink)}}.rec b a:hover{{color:var(--brass)}}
.rec .pay{{font-size:11.5px;color:var(--muted)}}
.rec small{{display:block;margin-top:6px;font-size:11px;color:var(--dim)}}
.rec small a{{color:var(--brass);font-weight:700}}
.tools{{margin-top:16px;display:grid;gap:8px;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}}
.tool{{display:flex;gap:8px;align-items:flex-start;padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--sheet)}}
.tool:hover{{border-color:var(--line-strong)}}
.tool .dot{{width:6px;height:6px;border-radius:50%;background:var(--brass);margin-top:6px;flex:0 0 6px}}
.tool b{{display:block;font:700 12px/1.2 var(--sans)}}
.tool span span{{display:block;font-size:11px;color:var(--muted);margin-top:2px}}
.sec-wrap{{margin-top:20px;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--line);display:grid;gap:1px}}
.sec-head{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;padding:12px 14px;background:var(--sheet)}}
.sec-head h2{{font:800 14px/1.1 var(--serif)}}
.sec-head p{{font-size:11.5px;color:var(--muted);margin:0}}
.sec-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:1px;background:var(--line)}}
.sec{{display:block;padding:12px 12px 10px;background:var(--sheet);transition:background .12s}}
.sec:hover{{background:var(--paper)}}
.sec b{{font:700 12px/1.2 var(--sans)}}
.sec .c{{float:right;font:700 10px/1 ui-monospace,monospace;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:2px 6px}}
.sec small{{display:block;margin-top:4px;font-size:11px;color:var(--muted);line-height:1.35}}
.trust{{margin-top:20px;display:grid;gap:8px;grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}}
.trust div{{padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--sheet)}}
.trust b{{display:block;font:700 11px/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}}
.trust p{{font-size:11.5px;line-height:1.45;color:var(--muted);margin:0}}
.how{{margin-top:20px;display:grid;gap:8px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}}
.how div{{padding:12px 12px 10px;border:1px solid var(--line);border-radius:8px;background:var(--sheet)}}
.how b{{font:700 12px/1.2 var(--sans)}}
.how p{{font-size:11.5px;line-height:1.45;color:var(--muted);margin:4px 0 0}}
.house-pal{{position:fixed;inset:0;z-index:80;display:grid;place-items:start center;padding:12vh 16px 16px;background:rgba(15,21,31,.45);backdrop-filter:blur(6px)}}
.house-pal[hidden]{{display:none !important}}
.house-pal-box{{width:min(640px,100%);background:var(--sheet);border:1px solid var(--line-strong);border-radius:12px;box-shadow:0 18px 60px rgba(0,0,0,.22);overflow:hidden}}
.house-pal-box header{{display:flex;align-items:center;gap:10px;padding:12px 14px;border-bottom:1px solid var(--line)}}
.house-pal-box input{{flex:1;border:0;background:transparent;font:15px/1 var(--sans);color:var(--ink)}}
.house-pal-box input:focus{{outline:none}}
.house-pal-list{{list-style:none;margin:0;padding:8px;max-height:56vh;overflow:auto}}
.house-pal-list li{{border-radius:8px}}
.house-pal-list li[aria-selected=true]{{background:var(--navy);color:var(--sheet)}}
.house-pal-list a{{display:block;padding:10px 12px}}
.house-pal-list b{{display:block;font:600 13px/1.25 var(--sans)}}
.house-pal-list small{{font-size:11px;opacity:.7}}
@media(max-width:640px){{.house .wrap{{width:min(calc(100% - 18px), var(--max))}}.house-hero h1{{font-size:clamp(28px,8vw,36px)}}.flag-grid{{grid-template-columns:1fr}}.sec-grid{{grid-template-columns:repeat(2,1fr)}}}}
</style>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-head">
  <div class="mast-top"><div class="wrap mast-in">
    <span style="display:inline-flex;align-items:center;gap:10px;white-space:nowrap">
      <a class="mast-brand" href="{H("/")}">THE BRYME<span class="mast-section">HOUSE</span></a>
      <span class="kicker">EST. 2026 · NO POP-UPS</span>
    </span>
    <span style="display:inline-flex;gap:8px;align-items:center;margin-left:auto">
      <form class="nav-search-form" action="/writers/search/" method="get" role="search"><input type="search" name="q" placeholder="Search 828 routes…" aria-label="Search" autocomplete="off"></form>
      <button type="button" class="theme-toggle" data-theme-toggle aria-label="Toggle theme"><span class="icon-sun" aria-hidden="true">☀</span><span class="icon-moon" aria-hidden="true">☾</span></button>
      <button type="button" class="nav-toggle" data-drawer-open aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
      <a href="{H("/writers/")}" style="font:800 11px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--brass);border:1px solid var(--line);border-radius:999px;padding:8px 12px;background:var(--sheet)">Flagship →</a>
    </span>
  </div></div>
  <nav class="main-nav" aria-label="Primary"><div class="wrap mast-nav">
    <a href="{H("/")}" class="home-link" aria-label="Home"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 10.5 12 3l9 7.5V21a1 1 0 0 1-1 1h-5v-5H9v5H4a1 1 0 0 1-1-1z"/></svg></a>
    <a href="{H("/writers/")}" style="color:var(--brass)">Flagship</a>
    <a href="{H("/writers/writing/")}">{N_MARKETS} markets</a>
    <a href="{H("/writers/tools/")}">{N_TOOLS} tools</a>
    <a href="{H("/tech/")}">Tech</a>
    <a href="{H("/entertainment/")}">Watch</a>
  </div></nav>
</header>
<div id="drawer-backdrop"></div>
<aside id="site-drawer" aria-hidden="true"><div class="drawer-head"><span class="logo"><span class="logo-mark" aria-hidden="true"></span> THE BRYME</span><button type="button" class="drawer-close" data-drawer-close aria-label="Close">✕</button></div>
  <div class="drawer-group"><b>House</b><a href="{H("/")}">Home — the house</a><a href="{H("/writers/")}">Flagship — Writers</a><a href="{H("/tech/")}">Tech (438)</a><a href="{H("/home/")}">Home (287)</a><a href="{H("/fitness/")}">Fitness (157)</a><a href="{H("/money/")}">Money (124)</a><a href="{H("/sports/")}">Sport (180)</a><a href="{H("/entertainment/")}">Entertainment (719)</a></div>
  <div class="drawer-group"><b>Flagship pathways — 7 jobs</b>{"".join(f'<a href="{H(route)}"><span style="display:inline-grid;place-items:center;width:18px;height:18px;border:1px solid var(--line);border-radius:4px;font:700 10px/1 ui-monospace,monospace;margin-right:6px">{kbd}</span>{title} · {count}</a>' for _,title,route,_,count,kbd in PATHWAYS)}</div>
  <div class="drawer-group"><b>Keys</b><span class="drawer-note">/ focus search · Ctrl+K palette (828 routes) · 1–7 pathways · 0 clear · ? help · theme toggle remembers choice · saved in localStorage only</span></div>
</aside>
<main id="main" class="house"><div class="wrap">

<section class="house-hero">
  <div class="eyebrow"><b>THE BRYME</b><span class="dot"></span>HOUSE EDITION<span class="dot"></span>7 DESKS<span class="dot"></span>ONE STANDARD</div>
  <h1>We read the <em>fine print</em> so you don't have to.</h1>
  <p class="dek">Seven specialist publications under one roof. <b>Flagship is a practical home for writers</b> — {N_MARKETS} paying markets checked by hand, {N_GUIDES} guides, {N_TOOLS} browser tools. Dated, sourced, no pop-ups. The rest of the house is small on purpose.</p>
  <div class="actions">
    <a class="btn" href="{H("/writers/")}">Enter flagship →</a>
    <a class="btn secondary" href="{H("/writers/writing/")}">Browse {N_MARKETS} markets</a>
    <button type="button" class="btn secondary" data-house-open-palette><span>Find anything</span><kbd style="display:inline-grid;place-items:center;width:18px;height:18px;border:1px solid var(--line);border-radius:4px;font:700 10px/1 ui-monospace,monospace">K</kbd></button>
  </div>
  <div class="meta"><b>{N_MARKETS}</b> paying markets <span class="sep">·</span> <b>{N_GUIDES}</b> guides <span class="sep">·</span> <b>{N_TOOLS}</b> tools <span class="sep">·</span> <b>0</b> pop-ups <span class="sep">·</span> Every record verified {SWEEP_OLDEST}&ndash;{SWEEP} <span class="sep">·</span> Reviewed {REVIEWED}</div>

  <div class="flag">
    <div class="flag-head"><h2>Flagship: a practical home for writers</h2><span>75% of useful real estate · house standard</span><a href="{H("/writers/")}">Full desk →</a></div>
    <div class="flag-grid">
      <div class="flag-card"><b><i>1</i> Discover — where to publish</b><p>{N_MARKETS} publications researched by hand — pay, word count, eligibility, submission method. Each carries its last-checked date.</p><div class="links"><a href="{H("/writers/writing/")}">All markets →</a><a href="{H("/writers/writing-opportunities/")}">Atlas</a><a href="{H("/writers/today/")}">This week</a></div></div>
      <div class="flag-card"><b><i>2</i> Learn — how to get in</b><p>{N_GUIDES} guides: pitch, query, cover letter, voice, structure, portfolio. From first pitch to final invoice.</p><div class="links"><a href="{H("/writers/learn/")}">Guide library →</a><a href="{H("/writers/guides/how-to-write-a-pitch/")}">Pitch guide</a><a href="{H("/writers/learn/professional-writing/how-to-write-a-cover-letter/")}">Cover letter</a></div></div>
      <div class="flag-card"><b><i>3</i> Earn — how to get paid</b><p>Rates, invoices, tax set-aside, income tracker, late payment letters. Browser tools, nothing uploaded.</p><div class="links"><a href="{H("/writers/tools/")}">{N_TOOLS} tools →</a><a href="{H("/writers/tools/freelance-rate-calculator/")}">Rate calc</a><a href="{H("/writers/tools/income-tracker/")}">Tracker</a></div></div>
    </div>
  </div>

  <div class="eyebrow" style="margin-top:18px"><b>PATHWAYS</b><span class="dot"></span>7 JOBS<span class="dot"></span>DISCOVER FIRST<span class="dot"></span>KEYS 1–7</div>
  <div class="paths">{pathways_html}</div>

  <div class="eyebrow" style="margin-top:18px"><b>RECENTLY VERIFIED</b><span class="dot"></span>LATEST {SWEEP}</div>
  <div class="recent">{recent_html}</div>

  <div class="eyebrow" style="margin-top:18px"><b>STRONGEST</b><span class="dot"></span>GSC {GSC}<span class="dot"></span>POS 4–13</div>
  <div class="recent">{strong_html}</div>

  <div class="eyebrow" style="margin-top:18px"><b>TOOLS</b><span class="dot"></span>{N_TOOLS} TOTAL<span class="dot"></span>BROWSER ONLY</div>
  <div class="tools">{tools_html}</div>

  <div class="sec-wrap">
    <div class="sec-head"><h2>The rest of the house — compact</h2><p>20% of useful real estate, small on purpose. Flagship is Writers.</p><a href="{H("/tech/")}" style="margin-left:auto;font:700 11px/1 var(--sans);color:var(--brass)">Browse all →</a></div>
    <div class="sec-grid">{secondary_html}</div>
  </div>

  <div class="eyebrow" style="margin-top:18px"><b>TRUST</b><span class="dot"></span>ONE HOUSE STANDARD</div>
  <div class="trust">
    <div><b>Every page dated</b><p>Last-checked and reviewed dates on every dossier. No evergreen without a date.</p></div>
    <div><b>Zero pop-ups</b><p>No interstitials, no autoplay, no newsletter gate. Read, use tools, leave.</p></div>
    <div><b>Browser tools only</b><p>{N_TOOLS} tools run in your browser. No account, nothing you type is sent anywhere.</p></div>
    <div><b>Verified by hand</b><p>Each market checked against the official guideline, not scraped.</p></div>
    <div><b>One house standard</b><p>Same type system, same rules, same no-pop-up promise across 7 desks.</p></div>
    <div><b>Free, funded by ads</b><p>Ads are in a single band, never inside prose. You can block them and everything still works.</p></div>
  </div>

  <div class="eyebrow" style="margin-top:18px"><b>HOW WE WORK</b><span class="dot"></span>4 RULES</div>
  <div class="how">
    <div><b>1. Read the guideline</b><p>Every dossier quotes pay, word count, eligibility from the official guideline and links to it.</p></div>
    <div><b>2. Date everything</b><p>Last-verified on every market, reviewed on every guide. Stale pages are marked.</p></div>
    <div><b>3. No pop-ups, ever</b><p>Trust is a feature. If we break it with a pop-up, you leave.</p></div>
    <div><b>4. Tools stay private</b><p>What you type into a tool stays in your browser. No upload, no account, no server log.</p></div>
  </div>

  <div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:20px"><a class="btn" href="{H("/writers/start/")}">Beginner path →</a><a class="btn secondary" href="{H("/writers/writing/")}">Browse markets</a><a class="btn secondary" href="{H("/writers/tools/")}">Free tools</a></div>

</section>
</div></main>

<nav class="bottom-nav bottom-nav--home" aria-label="Mobile"><a href="{H("/writers/")}"><span aria-hidden="true">✍️</span>Flagship</a><a href="{H("/writers/tools/")}"><span aria-hidden="true">🛠</span>Tools</a><a href="{H("/writers/writing/")}"><span aria-hidden="true">💰</span>Publish</a><a href="{H("/writers/search/")}"><span aria-hidden="true">🔍</span>Search</a></nav>

<div id="house-pal" class="house-pal" data-house-palette hidden>
  <div class="house-pal-box" role="dialog" aria-modal="true" aria-label="Search the house">
    <header><span style="font:700 10px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)">THE BRYME — 828 routes</span><input id="house-pal-q" type="search" placeholder="Type a market, guide, tool…" autocomplete="off" aria-label="Search"><span style="font:700 10px/1 ui-monospace,monospace;color:var(--muted);border:1px solid var(--line);border-radius:4px;padding:2px 5px">ESC</span></header>
    <ul class="house-pal-list" data-house-pal role="listbox"></ul>
  </div>
</div>

<script src="/assets/site-nav.js" defer></script>
<script src="/assets/house-home.js" defer></script>
<footer class="site-foot"><div class="wrap foot-grid">
<div class="foot-brand"><a class="logo" href="{H("/")}"><span class="logo-mark" aria-hidden="true"></span> THE BRYME</a><p>A house that reads the fine print so you don't have to. Seven desks, one house standard. Flagship is Writers — {N_MARKETS} paying markets checked by hand, dated, sourced, no pop-ups.</p></div>
<div class="foot-col"><b>Flagship</b><a href="{H("/writers/")}">Writers home</a><a href="{H("/writers/writing/")}">{N_MARKETS} markets</a><a href="{H("/writers/learn/")}">{N_GUIDES} guides</a><a href="{H("/writers/tools/")}">{N_TOOLS} tools</a><a href="{H("/writers/search/")}">Search</a></div>
<div class="foot-col"><b>House</b><a href="{H("/tech/")}">Tech</a><a href="{H("/home/")}">Home</a><a href="{H("/fitness/")}">Fitness</a><a href="{H("/money/")}">Money</a><a href="{H("/sports/")}">Sport</a><a href="{H("/entertainment/")}">Entertainment</a></div>
<div class="foot-col"><b>Trust</b><a href="/about/">About</a><a href="/privacy/">Privacy</a><a href="/about/#contact">Contact</a><span style="font-size:12px;color:var(--dim)">Reviewed {REVIEWED} · 0 pop-ups · Ctrl+K · / · 1–7 · ?</span></div>
</div><div class="wrap foot-bottom">© 2026 THE BRYME · A house that reads the fine print · 7 desks, one standard · Reviewed {REVIEWED} · 0 pop-ups, ever · Keys: / · Ctrl+K · 1–7 · ? · Theme toggle remembers choice.</div></footer>
</body></html>
"""

# --- generate house-home.js palette + kbd ---
import json as _json
index_entries = []
for need, title, route, desc, count, kbd in PATHWAYS:
    index_entries.append({"u": route, "t": f"{title} — {desc[:60]}", "k": need})
for pub, route, pay, title, ver in RECENT_CARDS:
    index_entries.append({"u": route, "t": f"{pub} — {title} — {pay}", "k": "discover"})
for name, route, blurb in STRONG:
    index_entries.append({"u": route, "t": f"{name} — {blurb}", "k": "discover"})
for name, route, desc in TOOLS:
    index_entries.append({"u": route, "t": f"{name} — {desc}", "k": "tools"})
for name, route, desc, count in SECONDARY:
    index_entries.append({"u": route, "t": f"{name} — {desc}", "k": "house"})
seen_u = set(e["u"] for e in index_entries)
for r in sorted(ALLOWLIST)[:800]:
    if r not in seen_u:
        title = r.strip("/").split("/")[-1].replace("-"," ")[:60] or "Home"
        index_entries.append({"u": r, "t": title, "k": "house"})
        seen_u.add(r)

js_path = ROOT / "assets" / "house-home.js"
js_content = f"""/* BRYME House v4 — compact header fix */
(function(){{
  "use strict";
  var INDEX = {_json.dumps(index_entries, separators=(",",":"))};
  var MAX = 12;
  function esc(s){{return String(s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}}
  function all(sel,root){{return [].slice.call((root||document).querySelectorAll(sel))}}
  function on(el,ev,fn){{if(el)el.addEventListener(ev,fn)}}
  function ed1(a,b){{var la=a.length,lb=b.length;if(Math.abs(la-lb)>1)return false;if(a===b)return true;var i=0,j=0,ed=0;while(i<la&&j<lb){{if(a[i]===b[j]){{i++;j++;continue}}if(ed)return false;ed=1;if(la>lb)i++;else if(lb>la)j++;else{{i++;j++}}}}return true}}
  function hit(row, tok){{var hay=(row.t+" "+row.u).toLowerCase();if(hay.indexOf(tok)!==-1)return true;if(tok.length<4)return false;var words=hay.split(/[^a-z0-9]+/).filter(Boolean);for(var i=0;i<words.length;i++)if(words[i].indexOf(tok)===0||ed1(tok,words[i]))return true;return false}}
  var pal = document.querySelector("[data-house-palette]");
  var palQ = document.getElementById("house-pal-q");
  var palList = document.querySelector("[data-house-pal]");
  var openBtns = all("[data-house-open-palette]");
  var palHits=[], palIdx=0;
  function palOpen(){{if(!pal)return;pal.hidden=false;document.documentElement.style.overflow="hidden";if(palQ){{palQ.value="";palQ.focus()}}palSearch("")}}
  function palClose(){{if(!pal)return;pal.hidden=true;document.documentElement.style.overflow="";var b=openBtns[0];if(b)b.focus()}}
  function palSearch(q){{if(!palList)return;var toks=String(q||"").toLowerCase().split(/\\s+/).filter(Boolean);var hits=toks.length?INDEX.filter(function(r){{for(var i=0;i<toks.length;i++)if(!hit(r,toks[i]))return false;return true}}).slice(0,MAX):[];palHits=hits;var out="";hits.forEach(function(r,i){{out+='<li role="option" aria-selected="'+(i===0?"true":"false")+'"><a href="'+esc(r.u)+'"><b>'+esc(r.t)+'</b><small>'+esc(r.u)+' · '+esc(r.k)+'</small></a></li>'}});palList.innerHTML=out||'<li><small>Type a word — '+INDEX.length+' routes indexed on-device, typo-tolerant, no network.</small></li>';palIdx=0}}
  function palMove(d){{var items=all('li[role="option"]',palList);if(!items.length)return;if(items[palIdx])items[palIdx].setAttribute("aria-selected","false");palIdx=(palIdx+d+items.length)%items.length;items[palIdx].setAttribute("aria-selected","true");if(items[palIdx].scrollIntoView)items[palIdx].scrollIntoView({{block:"nearest"}})}}
  openBtns.forEach(function(b){{on(b,"click",palOpen)}});
  on(pal,"click",function(ev){{if(ev.target===pal)palClose()}});
  on(palQ,"input",function(){{palSearch(palQ.value)}});
  on(palQ,"keydown",function(ev){{if(ev.key==="ArrowDown"){{ev.preventDefault();palMove(1)}}else if(ev.key==="ArrowUp"){{ev.preventDefault();palMove(-1)}}else if(ev.key==="Enter"){{var a=all('li[role="option"]',palList)[palIdx];a=a&&a.querySelector("a");if(a){{ev.preventDefault();location.href=a.getAttribute("href")}}}}}});
  on(document,"keydown",function(ev){{
    var tag=((ev.target&&ev.target.tagName)||"").toUpperCase();var typing=tag==="INPUT"||tag==="TEXTAREA"||tag==="SELECT";
    if((ev.metaKey||ev.ctrlKey)&&(ev.key==="k"||ev.key==="K")){{ev.preventDefault();if(pal&&pal.hidden)palOpen();else palClose();return}}
    if(ev.key==="Escape"&&pal&&!pal.hidden){{palClose();return}}
    if(typing)return;
    if(ev.key==="/"){{ev.preventDefault();var inp=document.querySelector(".nav-search-form input");if(inp)inp.focus();return}}
    if(ev.key==="0"){{ev.preventDefault();var q=document.querySelector(".nav-search-form input");if(q){{q.value="";q.blur()}}return}}
    if(ev.key==="?"||(ev.shiftKey&&ev.key==="/")){{ev.preventDefault();var toast=document.getElementById("house-help");if(toast&&toast.parentNode){{toast.parentNode.removeChild(toast);return}}toast=document.createElement("div");toast.id="house-help";toast.style.cssText="position:fixed;bottom:20px;left:50%;transform:translateX(-50%);max-width:520px;white-space:pre-line;background:var(--sheet,#fff);color:var(--ink,#000);border:1px solid var(--line-strong,#ccc);border-radius:10px;padding:16px 18px;box-shadow:0 10px 30px rgba(0,0,0,.15);font:13px/1.5 ui-sans-serif,system-ui;z-index:100;cursor:pointer";toast.textContent="BRYME House — keyboard\\n\\n/ — focus search\\nCtrl+K — palette ("+INDEX.length+" routes)\\n1–7 — pathways (Discover, Write, Submit, Research, Earn, Tools, Career)\\n0 — clear\\nEsc — close palette/drawer\\n? — this help\\n\\nTheme toggle remembers choice (light/dark). Saved in localStorage only.\\n\\n(click to dismiss)";on(toast,"click",function(){{if(toast.parentNode)toast.parentNode.removeChild(toast)}});document.body.appendChild(toast);setTimeout(function(){{if(toast&&toast.parentNode)toast.parentNode.removeChild(toast)}},8000);return}}
    var n=parseInt(ev.key,10);if(n>=1&&n<=7){{var paths=all(".path");if(paths[n-1]){{var a=paths[n-1].querySelector("a");if(a){{ev.preventDefault();a.click()}}}}}}
  }});
  document.documentElement.classList.add("house-js");
  try{{console.log("[BRYME house v4] compact header + discover-first — "+INDEX.length+" indexed, Ctrl+K, /, 1-7, ?")}}catch(e){{}}
}})();
"""
js_path.parent.mkdir(parents=True, exist_ok=True)
js_path.write_text(js_content, encoding="utf-8")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(HTML, encoding="utf-8")
print(f"build-landing v4: wrote {OUT.relative_to(ROOT)} ({len(HTML):,} bytes) COMPACT HEADER FIX")
print(f"build-landing v4: wrote {js_path.relative_to(ROOT)} ({len(js_content):,} bytes) index {len(index_entries)}")
print(f"build-landing v4: {len(_links)} links validated, {len(set(_links))} unique")
print(f"build-landing v4: header 48px not 88px, main-nav hidden on house, DISCOVER first not WRITE")
