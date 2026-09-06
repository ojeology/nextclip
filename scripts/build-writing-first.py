#!/usr/bin/env python3
"""Build the WRITING-FIRST BRYME main branch.

Reuses the existing focused-site shell (page(), esc(), schema(), write(), BASE,
SITE, cfg, TODAY) from build-focus-site.py so the infrastructure — site_config,
SITE_URL env handling, canonical/OG/twitter/schema head, server, discovery —
is shared rather than forked.

This builder emits the writing-first surface:
  /                       writing-first homepage
  /writing/               hub + all 55 publication cards
  /writing/<slug>/        one permanent page per publication (canonical)
  /guides/                writing-guide hub
  /guides/<slug>/         writing guide pages
  /tested/                BRYME Tested index
  /about/                 writing-first about page
  + trust/legal pages and 404/410.

Legacy multi-niche output is preserved on the `legacy-multiniche` branch and
archived in-tree under legacy-site/ — it is not generated here and not promoted.
"""
from __future__ import annotations
import importlib.util
import json
import datetime as _dt
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))  # scripts import `bryme_config` by name

# Reuse the working focused-site shell (not a fork): page(), esc(), schema(),
# write(), BASE, SITE, cfg, TODAY, TODAY_HUMAN, footer().
_spec = importlib.util.spec_from_file_location("build_focus_site", ROOT / "scripts" / "build-focus-site.py")
_build_focus = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_build_focus)
ROOT = _build_focus.ROOT
BASE = _build_focus.BASE
TODAY = _build_focus.TODAY
TODAY_HUMAN = _build_focus.TODAY_HUMAN
SITE = _build_focus.SITE
cfg = _build_focus.cfg
esc = _build_focus.esc
schema = _build_focus.schema
write = _build_focus.write
footer = _build_focus.footer


def footer() -> str:
    """Writing Hub footer."""
    return '''<footer class="site-foot"><div class="wrap foot-grid">
  <div class="foot-brand"><a class="logo" href="/"><span class="logo-mark" aria-hidden="true">B</span>BRYME</a><p>BRYME is a free writing resource — guides, tools, and verified opportunities to get published and paid.</p></div>
  <div class="foot-col"><b>How to write</b><a href="/start/">Beginner path</a><a href="/find/">What do you want to write?</a><a href="/intelligence/">Writing Intelligence</a><a href="/compare/">Compare formats</a><a href="/writing/by-country/">Writing by country</a><a href="/regional/">Writing conventions</a><a href="/learn/">Writing hub</a><a href="/learn/examples/">Examples</a><a href="/learn/dos-and-donts/">Dos &amp; don'ts</a><a href="/learn/types-of-writing/">Types of writing</a><a href="/learn/grammar-language/">Grammar</a></div>
  <div class="foot-col"><b>Tools &amp; publish</b><a href="/tools/">Writing tools</a><a href="/templates/">Templates</a><a href="/checklists/">Checklists</a><a href="/writing/">Paid opportunities</a><a href="/writing-opportunities/">Browse by country</a><a href="/today/">Today&rsquo;s opportunities</a><a href="/tracker/">Submission tracker</a><a href="/tested/">BRYME Tested</a></div>
  <div class="foot-col"><b>Trust</b><a href="/about/">About</a><a href="/verification/">What statuses mean</a><a href="/editorial-policy/">Editorial policy</a><a href="/corrections/">Corrections</a><a href="/privacy/">Privacy</a><a href="/contact/">Contact</a></div>
  <div class="foot-col"><b>Legal</b><a href="/terms/">Terms</a><a href="/disclaimer/">Disclaimer</a><a href="/copyright/">Copyright</a></div>
</div><div class="wrap foot-bottom">© 2026 BRYME · Independent editorial project · No acceptance, publication or payment is guaranteed.</div></footer>'''


WRITING = json.loads((ROOT / "content/opportunities.json").read_text(encoding="utf-8"))["opportunities"]

# Base country (where each publication is based) for the country selector.
# "" = online / international — no single verified base country to claim.
PUB_COUNTRIES = json.loads((ROOT / "content/hub/pub-countries.json").read_text(encoding="utf-8"))
FX = json.loads((ROOT / "content/hub/fx-rates.json").read_text(encoding="utf-8"))

# ---------------------------------------------------------------------------
# Facet vocabularies.
#
# The raw records grew organically and use several spellings for the same
# thing ("essays"/"essay", "interviews"/"interview", "reviews"/"book-review").
# A filter built straight on the raw values silently splits its own results,
# so everything is folded through these maps before it reaches the UI.
# Nothing is discarded — the raw label is still shown on the card.
# ---------------------------------------------------------------------------

WRITING_TYPE_MAP = {
    "essays": "essays", "essay": "essays", "critical-essay": "essays",
    "personal-essays": "personal-essays", "personal-essay": "personal-essays",
    "creative-nonfiction": "creative-nonfiction", "narrative-nonfiction": "creative-nonfiction",
    "nonfiction": "creative-nonfiction",
    "fiction": "fiction", "drama": "fiction",
    "poetry": "poetry",
    "journalism": "journalism", "reportage": "journalism", "news": "journalism",
    "reported-feature": "journalism",
    "articles": "articles", "listicle": "articles", "technical": "articles",
    "reading-list": "articles", "quiz": "articles", "gallery": "articles",
    "analysis": "analysis", "money": "analysis", "personal-finance": "analysis",
    "opinion": "opinion", "humor": "opinion",
    "reviews": "reviews", "book-review": "reviews", "culture": "reviews",
    "interviews": "interviews", "interview": "interviews",
    "translation": "translation",
    "other": "other",
}

WRITING_TYPE_LABELS = {
    "essays": "Essays", "personal-essays": "Personal essays",
    "creative-nonfiction": "Creative nonfiction", "fiction": "Fiction",
    "poetry": "Poetry", "journalism": "Journalism & reporting",
    "articles": "Articles & explainers", "analysis": "Analysis",
    "opinion": "Opinion", "reviews": "Reviews & criticism",
    "interviews": "Interviews", "translation": "Translation", "other": "Other",
}

# Brief §3: one status vocabulary across the whole site.
STATUS_MAP = {
    "open": "open", "rolling": "rolling", "upcoming": "seasonal",
    "deadline": "deadline", "closed": "closed", "unknown": "unknown",
}
STATUS_LABELS = {
    "open": ("Open", "Accepting submissions now, with no stated closing date."),
    "rolling": ("Rolling", "Reads year-round; no submission window to wait for."),
    "seasonal": ("Seasonal", "Opens in windows. Currently between reading periods."),
    "deadline": ("Deadline", "Open now, but closes on a stated date."),
    "closed": ("Closed", "Not accepting submissions at the last check."),
    "unknown": ("Unknown", "The official page does not state a current status."),
}

AI_POLICY_MAP = {
    "prohibited": "prohibited", "no-ai": "prohibited", "strict": "prohibited",
    "disclosure-required": "disclosure", "limited": "disclosure",
    "not-stated": "not-stated",
}
AI_POLICY_LABELS = {
    "prohibited": "AI-generated work prohibited",
    "disclosure": "AI use must be disclosed",
    "not-stated": "AI policy not stated",
}


def norm_types(rec: dict) -> list[str]:
    """Folded, de-duplicated, order-stable writing types for one record."""
    out = []
    for t in rec.get("writingTypes") or []:
        n = WRITING_TYPE_MAP.get(t, "other")
        if n not in out:
            out.append(n)
    return out


def norm_status(rec: dict) -> str:
    return STATUS_MAP.get(rec.get("submissionStatus"), "unknown")


def norm_ai(rec: dict) -> str:
    return AI_POLICY_MAP.get(rec.get("aiPolicy"), "not-stated")


def usd_amount(rec: dict):
    """Lowest stated pay, normalised to USD, for sorting and filtering only.

    Returns None when the publication states no number — never a guess. A
    record with unstated pay must not sort as if it paid nothing.
    """
    pay = rec.get("pay") or {}
    amt = pay.get("amountMin")
    if amt is None:
        return None
    cur = (pay.get("currency") or "USD").upper() or "USD"
    rate = FX["perUsd"].get(cur)
    if rate is None:
        return None
    return round(amt / rate, 2)


def usd_approx(rec: dict) -> str:
    """Dated approximate USD, shown *beside* the publication's own figure.

    The stated figure stays primary because that is the verified fact; this is
    a convenience for comparison and is always labelled as approximate.
    """
    pay = rec.get("pay") or {}
    cur = (pay.get("currency") or "").upper()
    if not cur or cur == "USD":
        return ""
    lo, hi = pay.get("amountMin"), pay.get("amountMax")
    if lo is None:
        return ""
    rate = FX["perUsd"].get(cur)
    if not rate:
        return ""
    def fmt(v):
        u = v / rate
        return f"${u:,.0f}" if u >= 10 else f"${u:,.2f}"
    span = fmt(lo) if (hi is None or hi == lo) else f"{fmt(lo)}\u2013{fmt(hi)}"
    return f"\u2248 {span} USD"


def pub_country(rec: dict) -> dict:
    return PUB_COUNTRIES.get(rec.get("slug") or rec.get("id") or "", {"base": "", "label": "International"})

TRUST_CONTENT = json.loads((ROOT / "content/hub/trust-pages.json").read_text(encoding="utf-8"))
BASE_NAMES = {"NG": "Nigeria", "US": "United States", "UK": "United Kingdom", "CA": "Canada",
              "AU": "Australia", "IE": "Ireland", "DE": "Germany", "ZA": "South Africa",
              "NA": "Namibia", "NP": "Nepal", "KE": "Kenya"}


def base_country(slug: str) -> str:
    return (PUB_COUNTRIES.get(slug) or {}).get("base") or ""


def open_internationally(rec: dict) -> bool:
    """True when the publication does not restrict submissions to one country/region."""
    el = rec.get("eligibility") or {}
    return el.get("mode") != "restricted"

# ---------------------------------------------------------------------------
# Navigation — Writing Hub desktop + 4-item mobile bottom bar
# ---------------------------------------------------------------------------
def nav(current: str = "") -> str:
    links = [
        ("learn", "/learn/", "How to write"),
        ("essays", "/essays/", "Essays"),
        ("tools", "/tools/", "Writing tools"),
        ("writing", "/writing/", "Write & get paid"),
    ]
    items = []
    for key, href, label in links:
        aria = ' aria-current="page"' if key == current else ""
        cls = ' class="nav-cta"' if key == "writing" else ""
        items.append(f'<a{cls}{aria} href="{href}">{label}</a>')
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in">
  <div class="brand-group">
    <a class="home-link" href="/"{' aria-current="page"' if current == "home" else ""} aria-label="BRYME home"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.5V20a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1V9.5"/><path d="M9.5 21v-6h5v6"/></svg></a>
    <a class="logo" href="/"><span class="logo-mark" aria-hidden="true">B</span>BRYME</a>
  </div>
  <nav class="main-nav" aria-label="Primary">{''.join(items)}</nav>
  <form class="nav-search-form" action="/search/" method="get" role="search"><input type="search" name="q" placeholder="Search guides, tools…" aria-label="Search BRYME" autocomplete="off"></form>
  <button type="button" class="theme-toggle" data-theme-toggle aria-pressed="false" aria-label="Switch to dark theme"><svg class="icon-sun" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M4.2 4.2l1.6 1.6M18.2 18.2l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.2 19.8l1.6-1.6M18.2 5.8l1.6-1.6"/></svg><svg class="icon-moon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 14.3A8.6 8.6 0 0 1 9.7 3.5a8.6 8.6 0 1 0 10.8 10.8Z"/></svg><span class="sr-only theme-toggle-text">Switch to dark theme</span></button>
  <button type="button" class="nav-toggle" data-drawer-open aria-label="Open menu" aria-expanded="false"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>'''


# How-to sub-navigation bar — a dedicated category nav shown across the
# writing-guide library and every how-to guide page.
HOWTO_LINKS = [
    ("start", "/start/", "Beginner path"),
    ("find", "/find/", "What do you want to write?"),
    ("intelligence", "/intelligence/", "Intelligence"),
    ("compare", "/compare/", "Compare formats"),
    ("by-country", "/writing/by-country/", "By country"),
    ("regional", "/regional/", "Conventions"),
    ("learn", "/learn/", "All how-tos"),
    ("examples", "/learn/examples/", "Examples"),
    ("dos-and-donts", "/learn/dos-and-donts/", "Dos & don'ts"),
    ("types-of-writing", "/learn/types-of-writing/", "Writing types"),
    ("start-writing", "/learn/start-writing/", "Start writing"),
    ("writing-basics", "/learn/writing-basics/", "Basics"),
    ("writing-process", "/learn/writing-process/", "Process"),
    ("academic-writing", "/learn/academic-writing/", "Academic"),
    ("professional-writing", "/learn/professional-writing/", "Professional"),
    ("creative-writing", "/learn/creative-writing/", "Creative"),
    ("online-writing", "/learn/online-writing/", "Online"),
    ("journaling-personal", "/learn/journaling-personal/", "Personal"),
    ("grammar-language", "/learn/grammar-language/", "Grammar"),
    ("editing-proofreading", "/learn/editing-proofreading/", "Editing"),
    ("writing-for-publication", "/learn/writing-for-publication/", "Get published"),
]


def howto_nav(current: str = "") -> str:
    """Dedicated navigation bar for the how-to / writing-guide area."""
    items = []
    for key, href, label in HOWTO_LINKS:
        aria = ' aria-current="page"' if key == current else ""
        items.append(f'<a{aria} href="{href}">{label}</a>')
    return f'''<nav class="section-nav" aria-label="How-to guides">{"".join(items)}</nav>'''


def section_nav(links, label="Sections", current="", field=("key", "href", "text")):
    """Generic moving category bar for any section hub."""
    items = []
    for link in links:
        key, href, text = link[0], link[1], link[2]
        aria = ' aria-current="page"' if key == current else ""
        items.append(f'<a{aria} href="{href}">{esc(text)}</a>')
    return f'<nav class="section-nav" aria-label="{esc(label)}">{"".join(items)}</nav>'


# --- Country selector for the writing hub -----------------------------------
# Continent map. BRYME is global, so the filter control is generated from the
# data rather than a hand-kept list of six countries: any ISO code that turns up
# in content/hub/pub-countries.json is placed in its continent group
# automatically. Adding a publication from a new country needs no code change.
CONTINENT_OF = {
    # Africa
    "NG": "Africa", "ZA": "Africa", "KE": "Africa", "GH": "Africa", "NA": "Africa",
    "ZW": "Africa", "UG": "Africa", "TZ": "Africa", "EG": "Africa", "MA": "Africa",
    "ET": "Africa", "RW": "Africa", "SN": "Africa", "CM": "Africa", "BW": "Africa",
    "ZM": "Africa", "MW": "Africa", "CI": "Africa", "TN": "Africa", "DZ": "Africa",
    # North America
    "US": "North America", "CA": "North America", "MX": "North America",
    "JM": "North America", "TT": "North America", "BB": "North America",
    # Europe
    "UK": "Europe", "GB": "Europe", "IE": "Europe", "DE": "Europe", "FR": "Europe",
    "ES": "Europe", "NL": "Europe", "IT": "Europe", "PT": "Europe", "SE": "Europe",
    "NO": "Europe", "DK": "Europe", "FI": "Europe", "PL": "Europe", "BE": "Europe",
    "AT": "Europe", "CH": "Europe", "GR": "Europe", "CZ": "Europe", "RO": "Europe",
    "UA": "Europe", "HU": "Europe", "IS": "Europe",
    # Asia
    "IN": "Asia", "PK": "Asia", "BD": "Asia", "NP": "Asia", "LK": "Asia",
    "SG": "Asia", "MY": "Asia", "PH": "Asia", "ID": "Asia", "JP": "Asia",
    "KR": "Asia", "CN": "Asia", "HK": "Asia", "AE": "Asia", "SA": "Asia",
    "QA": "Asia", "IL": "Asia", "TR": "Asia", "VN": "Asia", "TH": "Asia",
    # Oceania
    "AU": "Oceania", "NZ": "Oceania", "FJ": "Oceania", "PG": "Oceania",
    # South America
    "BR": "South America", "AR": "South America", "CL": "South America",
    "CO": "South America", "PE": "South America",
}
CONTINENT_ORDER = ["Africa", "North America", "Europe", "Asia", "Oceania", "South America"]

COUNTRY_NAMES = {
    "NG": "Nigeria", "US": "United States", "UK": "United Kingdom", "GB": "United Kingdom",
    "CA": "Canada", "AU": "Australia", "IE": "Ireland", "DE": "Germany",
    "ZA": "South Africa", "NA": "Namibia", "NP": "Nepal", "KE": "Kenya",
    "GH": "Ghana", "ZW": "Zimbabwe", "UG": "Uganda", "TZ": "Tanzania", "EG": "Egypt",
    "MA": "Morocco", "ET": "Ethiopia", "RW": "Rwanda", "SN": "Senegal",
    "CM": "Cameroon", "BW": "Botswana", "ZM": "Zambia", "MW": "Malawi",
    "CI": "Côte d'Ivoire", "TN": "Tunisia", "DZ": "Algeria",
    "MX": "Mexico", "JM": "Jamaica", "TT": "Trinidad & Tobago", "BB": "Barbados",
    "FR": "France", "ES": "Spain", "NL": "Netherlands", "IT": "Italy",
    "PT": "Portugal", "SE": "Sweden", "NO": "Norway", "DK": "Denmark",
    "FI": "Finland", "PL": "Poland", "BE": "Belgium", "AT": "Austria",
    "CH": "Switzerland", "GR": "Greece", "CZ": "Czechia", "RO": "Romania",
    "UA": "Ukraine", "HU": "Hungary", "IS": "Iceland",
    "IN": "India", "PK": "Pakistan", "BD": "Bangladesh", "LK": "Sri Lanka",
    "SG": "Singapore", "MY": "Malaysia", "PH": "Philippines", "ID": "Indonesia",
    "JP": "Japan", "KR": "South Korea", "CN": "China", "HK": "Hong Kong",
    "AE": "United Arab Emirates", "SA": "Saudi Arabia", "QA": "Qatar",
    "IL": "Israel", "TR": "Türkiye", "VN": "Vietnam", "TH": "Thailand",
    "NZ": "New Zealand", "FJ": "Fiji", "PG": "Papua New Guinea",
    "BR": "Brazil", "AR": "Argentina", "CL": "Chile", "CO": "Colombia", "PE": "Peru",
}
# Kept for backwards compatibility with existing call sites.
BASE_NAMES_EXTRA = COUNTRY_NAMES


def region_slug(name: str) -> str:
    return name.lower().replace(" ", "-")


def continent_of(iso: str) -> str:
    return CONTINENT_OF.get((iso or "").upper(), "")


def country_name(iso: str) -> str:
    iso = (iso or "").upper()
    return COUNTRY_NAMES.get(iso) or BASE_NAMES.get(iso) or iso


def _filter_matches(rec: dict, flt: str, mode: str = "based") -> bool:
    """Does this record match a country/region filter?

    Two modes, because "which UK magazines take pitches?" and "what can I apply
    to from Nigeria?" are different questions and the option counts have to
    match whichever the control is set to. `based` is the default, so the
    counts in the <select> are counts of publications actually based there —
    the inclusive count was 98 for every country and told the user nothing.
    """
    base = (base_country(rec["slug"]) or "").upper()
    open_to = open_internationally(rec)
    if flt == "all":
        return True
    if flt == "international":
        return open_to
    here = bool(base) and (flt == base or flt == region_slug(continent_of(base)))
    if mode == "opento":
        return here or open_to
    return here


def writing_nav(current_flt: str = "") -> str:
    """Static country filter for the /writing/ hub.

    A real selection control — not a scrolling header. Every country present in
    the data is inside it, grouped by continent, with an "All countries" reset
    and an "Open worldwide" option. It is a native <select>, so it is keyboard
    accessible, screen-reader friendly and uses the OS picker on mobile."""
    bases = sorted({(base_country(r["slug"]) or "").upper() for r in WRITING} - {""})

    # Group the countries actually present in the data by continent.
    groups: dict[str, list[str]] = {}
    for iso in bases:
        groups.setdefault(continent_of(iso) or "Other regions", []).append(iso)

    n_all = len(WRITING)
    n_intl = sum(1 for r in WRITING if _filter_matches(r, "international"))

    opts = [
        f'<option value="all" selected>All countries — {n_all} publications</option>',
        f'<option value="international">Open worldwide (no country restriction) — {n_intl}</option>',
    ]

    # Region shortcuts first, then the individual countries per continent.
    region_opts = []
    for cont in CONTINENT_ORDER + sorted(set(groups) - set(CONTINENT_ORDER)):
        if cont not in groups:
            continue
        rslug = region_slug(cont)
        n = sum(1 for r in WRITING if _filter_matches(r, rslug))
        region_opts.append(f'<option value="{esc(rslug)}">{esc(cont)} — {n}</option>')
    if region_opts:
        opts.append('<optgroup label="Regions">' + "".join(region_opts) + "</optgroup>")

    for cont in CONTINENT_ORDER + sorted(set(groups) - set(CONTINENT_ORDER)):
        if cont not in groups:
            continue
        rows = []
        for iso in sorted(groups[cont], key=country_name):
            n = sum(1 for r in WRITING if _filter_matches(r, iso))
            rows.append(f'<option value="{esc(iso)}">{esc(country_name(iso))} — {n}</option>')
        opts.append(f'<optgroup label="{esc(cont)}">' + "".join(rows) + "</optgroup>")

    # Counts are computed from the real records so no option ever advertises
    # results that do not exist.
    tcount = {}
    for r in WRITING:
        for t in norm_types(r):
            tcount[t] = tcount.get(t, 0) + 1
    type_opts = "".join(
        f'<option value="{esc(k)}">{esc(WRITING_TYPE_LABELS[k])} — {tcount[k]}</option>'
        for k in sorted(tcount, key=lambda k: (-tcount[k], WRITING_TYPE_LABELS[k])))

    scount = {}
    for r in WRITING:
        k = norm_status(r)
        scount[k] = scount.get(k, 0) + 1
    accepting = sum(scount.get(k, 0) for k in ("open", "rolling", "deadline"))
    status_opts = f'<option value="acceptingnow">Accepting now — {accepting}</option>' + "".join(
        f'<option value="{esc(k)}">{esc(STATUS_LABELS[k][0])} — {scount[k]}</option>'
        for k in ("open", "rolling", "seasonal", "deadline", "closed", "unknown") if scount.get(k))

    def n_at_least(v):
        return sum(1 for r in WRITING if (usd_amount(r) or -1) >= v)
    pay_opts = "".join(
        f'<option value="{v}">${v}+ — {n_at_least(v)}</option>'
        for v in (50, 100, 250, 500, 1000) if n_at_least(v))

    n_global = sum(1 for r in WRITING if (r.get("eligibility") or {}).get("mode") in ("open", "worldwide"))

    return f'''<form id="opp-filter" class="opp-filter" aria-label="Search and filter writing opportunities">
  <div class="opp-filter-search">
    <label class="sr-only" for="f-q">Search opportunities</label>
    <input id="f-q" type="search" placeholder="Search publications, genres, topics — e.g. personal essay, poetry, Lagos" autocomplete="off">
  </div>
  <div class="opp-filter-grid">
    <div class="opp-field"><label for="f-country">Country</label>
      <select id="f-country" name="country" autocomplete="country">{"".join(opts)}</select></div>
    <div class="opp-field"><label for="f-cmode">Country means</label>
      <select id="f-cmode">
        <option value="based">Publication is based there</option>
        <option value="opento">Open to writers from there</option>
      </select></div>
    <div class="opp-field"><label for="f-type">Type of writing</label>
      <select id="f-type"><option value="">Any type</option>{type_opts}</select></div>
    <div class="opp-field"><label for="f-status">Status</label>
      <select id="f-status"><option value="">Any status</option>{status_opts}</select></div>
    <div class="opp-field"><label for="f-pay">Pays at least</label>
      <select id="f-pay"><option value="">Any pay</option>{pay_opts}</select></div>
    <div class="opp-field"><label for="f-words">Length</label>
      <select id="f-words"><option value="">Any length</option>
        <option value="short">Short — under 1,200 words</option>
        <option value="medium">Medium — 800 to 3,000</option>
        <option value="long">Long — 2,500+</option></select></div>
    <div class="opp-field"><label for="f-sort">Sort by</label>
      <select id="f-sort"><option value="default">BRYME order</option>
        <option value="pay">Highest pay</option>
        <option value="verified">Most recently verified</option>
        <option value="deadline">Closing soonest</option>
        <option value="name">Publication name</option></select></div>
  </div>
  <div class="opp-filter-row">
    <label class="opp-check"><input type="checkbox" id="f-global"> Open to writers anywhere — {n_global}</label>
    <button type="button" id="f-reset" class="country-reset">Reset all</button>
  </div>
  <p class="country-filter-hint"><b>Publication is based there</b> answers &ldquo;which UK magazines take pitches?&rdquo;. <b>Open to writers from there</b> answers &ldquo;what can I apply to from Nigeria?&rdquo; and includes everything open worldwide. A minimum-pay filter hides publications that do not state a figure &mdash; BRYME will not guess what they pay.</p>
</form>
<div id="f-chips" class="f-chips" hidden></div>
<p id="filter-note" class="filter-status" aria-live="polite"><b id="f-count">{n_all} opportunities</b></p>
<p id="f-empty" class="filter-status empty" hidden>Nothing matches all of those filters. Remove one — or <a href="/writing/">see all {n_all}</a>.</p>'''



def mobile_nav(current: str = "") -> str:
    links = [
        ("learn", "/learn/", "📚", "How to"),
        ("essays", "/essays/", "✍️", "Essays"),
        ("tools", "/tools/", "🛠", "Tools"),
        ("writing", "/writing/by-country/", "💰", "Publish"),
    ]
    return '<nav class="bottom-nav bottom-nav--writing" aria-label="Primary mobile">' + ''.join(
        f'<a href="{href}"' + (' aria-current="page"' if key == current else '') +
        f'><span aria-hidden="true">{icon}</span>{label}</a>' for key, href, icon, label in links
    ) + '</nav>'


def drawer(current: str = "") -> str:
    """Easy slide-out sidebar: every section in one tappable place."""
    def group(label, items):
        rows = []
        for key, href, text, icon in items:
            aria = ' aria-current="page"' if key == current else ""
            rows.append(f'<a{aria} href="{href}"><span aria-hidden="true">{icon}</span>{esc(text)}</a>')
        return f'<div class="drawer-group"><b>{esc(label)}</b>{"".join(rows)}</div>'

    howto = [
        ("learn", "/learn/", "All how-tos", "📚"),
        ("examples", "/learn/examples/", "Examples", "✳️"),
        ("dos-and-donts", "/learn/dos-and-donts/", "Dos & don'ts", "✅"),
        ("types-of-writing", "/learn/types-of-writing/", "Writing types", "🧩"),
        ("start-writing", "/learn/start-writing/", "Start writing", "🚀"),
        ("academic-writing", "/learn/academic-writing/", "Academic", "🎓"),
        ("creative-writing", "/learn/creative-writing/", "Creative", "✍️"),
        ("editing-proofreading", "/learn/editing-proofreading/", "Editing & proofreading", "🧹"),
        ("writing-for-publication", "/learn/writing-for-publication/", "Get published", "📮"),
    ]
    tools = [("tools", "/tools/", "All tools", "🛠️"),
             ("templates", "/templates/", "Templates", "📄"),
             ("checklists", "/checklists/", "Checklists", "☑️"),
             ("glossary", "/glossary/", "Glossary", "🔤")]
    write = [("writing", "/writing/", "All publications", "💰"),
             ("guides", "/guides/", "Writing guides", "🗺️"),
             ("tested", "/tested/", "BRYME Tested", "🧪")]
    country = [("writing-NG", "/writing/?country=NG", "Nigeria & open worldwide", "🇳🇬"),
               ("writing-africa", "/writing/?country=africa", "Africa & diaspora", "🌍"),
               ("writing-US", "/writing/?country=US", "United States", "🇺🇸"),
               ("writing-UK", "/writing/?country=UK", "United Kingdom", "🇬🇧"),
               ("writing-CA", "/writing/?country=CA", "Canada", "🇨🇦"),
               ("writing-AU", "/writing/?country=AU", "Australia", "🇦🇺")]
    trust = [("about", "/about/", "About", "ℹ️"),
             ("verification", "/verification/", "What statuses mean", "🏷️"),
             ("editorial-policy", "/editorial-policy/", "Editorial policy", "📜"),
             ("corrections", "/corrections/", "Corrections", "✏️"),
             ("privacy", "/privacy/", "Privacy", "🔒"),
             ("contact", "/contact/", "Contact", "✉️")]
    return f'''<div id="drawer-backdrop"></div>
<aside id="site-drawer" aria-hidden="true" aria-label="Site menu" role="dialog" aria-modal="true">
  <div class="drawer-head"><a class="logo" href="/"><span class="logo-mark" aria-hidden="true">B</span>BRYME</a><button type="button" class="drawer-close" data-drawer-close aria-label="Close menu"><svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>
  {group("Start here", [("home", "/", "Home", "🏠"), ("start", "/start/", "Complete beginner path", "🧭"), ("find", "/find/", "What do you want to write?", "❓"), ("intelligence", "/intelligence/", "Writing Intelligence", "🧭"), ("compare", "/compare/", "Compare formats", "⚖️"), ("essays", "/essays/", "Essays", "✍️"), ("today", "/today/", "Today's opportunities", "📅"), ("tracker", "/tracker/", "Submission tracker", "📋"), ("by-country", "/writing/by-country/", "Writing by country", "🌍"), ("search", "/search/", "Search BRYME", "🔍")])}
  {group("How to write", howto)}
  {group("Tools & templates", tools)}
  {group("Write & get paid", write)}
  <div class="drawer-group"><b>Publications by country</b>
    <div class="drawer-sub">{"".join(f'<a href="{h}">{esc(t)}</a>' for _, h, t, _ in country)}</div>
  </div>
  {group("Trust & about", trust)}
  <p class="drawer-note">BRYME is a free, independent writing resource. Guides and tools work right in your browser — no account, no charge.</p>
</aside>'''


def page_wf(*, title: str, description: str, route: str, current: str, body: str,
            schema_data: object | None = None, robots: str = "index,follow") -> str:
    """Writing-first page: the shared shell with a writing-first graph + nav.

    (Copied from build_focus_site.page so the writing branch controls its own
    SearchAction/site graph and nav while keeping the same hardened head.)
    """
    canonical = BASE + route
    ca_id = str(cfg.publisher_config().get("caId") or "").strip()
    adsense_meta = f'<meta name="google-adsense-account" content="{esc(ca_id)}">' if ca_id else ""
    structured = schema_data or {
        "@context": "https://schema.org", "@type": "WebPage",
        "name": title.split(" | ")[0], "description": description, "url": canonical,
        "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
    }
    site_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": BASE + "/#org", "name": SITE["name"],
             "url": BASE + "/", "description": SITE["description"],
             "founder": {"@type": "Person", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/"}},
            {"@type": "WebSite", "@id": BASE + "/#site", "name": SITE["name"],
             "url": BASE + "/", "description": SITE["description"],
             "publisher": {"@id": BASE + "/#org"},
             "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint",
                                   "urlTemplate": BASE + "/writing/?q={search_term_string}"},
                                 "query-input": "required name=search_term_string"}},
        ],
    }
    return f'''<!doctype html>
<html lang="en-NG"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#faf6ee">
<meta name="color-scheme" content="light dark">
<script src="/assets/theme.js"></script>
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{esc(robots)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="BRYME">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}">
{adsense_meta}
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/bryme-v2.css">
{schema(site_graph)}
{schema(structured)}
</head><body>{nav(current)}<main id="main">{body}</main>{mobile_nav(current)}{drawer(current)}<script src="/assets/site-nav.js" defer></script><script src="/assets/level-filter.js" defer></script><script src="/assets/purpose-finder.js" defer></script>{footer()}</body></html>'''


# ---------------------------------------------------------------------------
# Status helpers
# ---------------------------------------------------------------------------
STATUS_ROBOTS = {
    "open":   ("🟢 Currently accepting",            "accepting",  "open"),
    "rolling":("🟢 Rolling submissions",            "rolling",    "open"),
    "upcoming":("🟡 Opens soon",                    "upcoming",   "unknown"),
    "deadline":("🟡 Limited window",                "limited",    "unknown"),
    "closed": ("🔴 Currently closed",               "closed",     "closed"),
    "unknown":("🟡 Information needs verification", "needs-verification", "unknown"),
}


def status_of(rec: dict) -> tuple[str, str, str]:
    by = {"open": "open", "rolling": "open", "upcoming": "unknown",
          "deadline": "unknown", "closed": "closed", "unknown": "unknown",
          None: "unknown"}
    from_status = rec.get("submissionStatus")
    label, cls, _ = STATUS_ROBOTS.get(from_status, STATUS_ROBOTS["unknown"])
    return label, cls, by.get(from_status, "unknown")


def status_badge(rec: dict) -> str:
    label, cls, _ = status_of(rec)
    return f'<span class="verify-badge {cls}">{esc(label)}</span>'


def verify_badge(rec: dict) -> str:
    """BRYME verification state for the publication card."""
    ex = rec.get("editorExperience") or {}
    st = ex.get("status")
    if not ex.get("applied"):
        return '<span class="verify-badge board-listed">🟡 Research only</span>'
    m = {"submitted": "🔵 Submitted", "accepted": "🟢 Accepted", "accepted-scheduled": "🟢 Accepted, scheduled",
         "published": "📖 Published", "paid": "💰 Paid", "rejected": "🔴 Rejected", "closed": "⚪ Closed"}
    return f'<span class="verify-badge verify">{m.get(st, st or "🔵 Submitted")}</span>'


def pub_card(rec: dict, heading: str = "h2") -> str:
    pay = (rec.get("pay") or {}).get("display") or "See page"
    wc = (rec.get("wordCount") or {}).get("display") or "—"
    el = (rec.get("eligibility") or {}).get("summary") or "See eligibility"
    url = f"/writing/{esc(rec['slug'])}/"
    base = esc((base_country(rec["slug"]) or "").upper())
    open_to = "international" if open_internationally(rec) else "regional"
    region = esc(region_slug(continent_of(base_country(rec["slug"]))))
    _iso = base_country(rec["slug"])
    region_label = esc(country_name(_iso) if _iso else "Open to all")
    # --- facet attributes (Brief §6/§7) -----------------------------------
    # Everything the filter engine needs is emitted onto the card so filtering
    # is pure DOM work with no fetch and no JSON payload to keep in sync.
    st = norm_status(rec)
    types = norm_types(rec)
    usd = usd_amount(rec)
    wcmin = (rec.get("wordCount") or {}).get("min")
    wcmax = (rec.get("wordCount") or {}).get("max")
    cur = ((rec.get("pay") or {}).get("currency") or "").upper()
    elig = rec.get("eligibility") or {}
    # "Can I apply from anywhere?" — the brief's first-class question.
    globally_open = elig.get("mode") in ("open", "worldwide")
    approx = usd_approx(rec)
    approx_html = f'<span class="pay-approx" title="Approximate, converted at the mid-market rate on {esc(FX["fetchedAt"])}">{esc(approx)}</span>' if approx else ""
    # `deadline` is an object, not a string: {date?, display?, openingDate?}.
    # Only the ISO date is machine-usable; stringifying the dict put a Python
    # repr into the attribute and made "closing soonest" sort on punctuation.
    _dl = rec.get("deadline") or {}
    deadline = (_dl.get("date") or "") if isinstance(_dl, dict) else ""
    deadline_display = (_dl.get("display") or "") if isinstance(_dl, dict) else ""
    search_blob = " ".join(filter(None, [
        rec.get("publication", ""), rec.get("title", ""), rec.get("writingTypeLabel", ""),
        rec.get("excerpt", ""), " ".join(rec.get("keywords") or []), region_label,
    ])).lower()

    return f'''<article class="job-card" data-country="{base}" data-region="{region}" data-open="{open_to}"
  data-status="{esc(st)}" data-types="{esc(" ".join(types))}" data-currency="{esc(cur)}"
  data-usd="{"" if usd is None else usd}" data-wcmin="{wcmin if wcmin is not None else ""}"
  data-wcmax="{wcmax if wcmax is not None else ""}" data-global="{"1" if globally_open else "0"}"
  data-ai="{esc(norm_ai(rec))}" data-deadline="{esc(deadline)}"
  data-verified="{esc(rec.get("lastVerified") or "")}"
  data-pub="{esc(rec.get("publication", ""))}" data-search="{esc(search_blob)}">
  <div class="job-card-badges">{status_badge(rec)}{verify_badge(rec)}<span class="verify-badge country">{region_label}</span></div>
  <{heading} class="job-card-title"><a href="{url}">{esc(rec['publication'])}</a></{heading}>
  <p class="job-card-sub">{esc(rec.get('writingTypeLabel') or rec.get('title') or '')}</p>
  <dl class="pub-facts">
    <dt>Pay</dt><dd>{esc(pay)}{approx_html}</dd>
    <dt>Words</dt><dd>{esc(wc)}</dd>
    <dt>Eligible</dt><dd>{esc(el.split('.')[0])}</dd>
    <dt>Verified</dt><dd>{esc((rec.get('lastVerified') or TODAY)[:7])}</dd>
  </dl>
  <div class="job-card-foot"><a class="card-link" href="{url}">View publication →</a></div>
</article>'''


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
def home() -> None:
    # Featured: the BRYME-tested record first, then a curated set of open ones.
    tested = [r for r in WRITING if (r.get("editorExperience") or {}).get("applied")]
    rest = [r for r in WRITING if not (r.get("editorExperience") or {}).get("applied")]
    def key(r):
        return 0 if r.get("submissionStatus") in ("open", "rolling") else 1
    rest.sort(key=key)
    featured = tested + rest[:5]
    cards = "".join(pub_card(r, "h3") for r in featured)
    n_open = sum(1 for r in WRITING if status_of(r)[2] == "open")
    body = f'''<section class="hero"><div class="wrap hero-grid"><div>
  <p class="kicker"><span class="kicker-dot"></span>Writing + research + trust</p>
  <h1>Find writing opportunities. Get published. Get <em>paid.</em></h1>
  <p class="hero-copy">BRYME researches legitimate writing opportunities — the publications, the pay, the word counts and who they're open to — and gives writers practical guides for pitching, submitting and getting published.</p>
  <div class="actions"><a class="btn" href="/writing/">Explore writing opportunities →</a><a class="btn secondary" href="/guides/">Browse writing guides</a><a class="btn secondary" href="/tested/">BRYME Tested</a></div>
</div><aside class="verify-card" aria-label="BRYME writing snapshot"><div class="verify-head"><h2 class="verify-title">Writing research snapshot</h2><span class="live-tag">Verified</span></div><p class="verify-date">{TODAY_HUMAN}</p><div class="metric-row"><div class="metric"><b>{len(WRITING)}</b><span>Publications</span></div><div class="metric"><b>{n_open}</b><span>Accepting now</span></div><div class="metric"><b>{len(tested)}</b><span>BRYME tested</span></div></div><p class="verify-note">Every publication page shows its last human-check date. "Open" is a timestamp, not a guarantee — always confirm the official guideline before pitching.</p></aside></div>
<div class="wrap location-picker"><p class="location-picker-label">Start with an opportunity <span class="location-picker-hint">— reviewed for pay, words and eligibility</span></p><div class="chip-grid">{''.join(f'<a class="chip-card" href="/writing/{esc(r["slug"])}/"><b>{esc((r.get("pay") or {}).get("display") or "—")}</b><span>{esc(r["publication"])}</span></a>' for r in WRITING[:6])}</div></div></section>
<section class="trust-strip"><div class="wrap trust-grid"><div class="trust-item"><span class="trust-icon">✓</span>Official submission guideline linked</div><div class="trust-item"><span class="trust-icon">✓</span>Pay and word count researched</div><div class="trust-item"><span class="trust-icon">✓</span>Eligibility and diaspora rules recorded</div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Featured opportunities</p><h2>Publications that pay writers.</h2></div><p>Each card links to a permanent BRYME page with the full detail and the official guideline.</p></div><div class="guide-grid">{cards}</div><div class="actions"><a class="btn" href="/writing/">See all {len(WRITING)} publications →</a></div></div></section>
<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Guides</p><h2>From first pitch to first payment.</h2></div><p>Practical, writer-first resources that connect to the opportunities above.</p></div><div class="card-grid">
<a class="path-card" href="/guides/how-to-write-a-pitch/"><span class="card-num">01</span><h3>How to write a pitch</h3><p>The structure, subject line and clips that get a publication to say yes — explained plainly.</p><span class="card-link">Open the guide →</span></a>
<a class="path-card" href="/guides/how-to-find-paid-writing-opportunities/"><span class="card-num">02</span><h3>Find paid writing opportunities</h3><p>Where to look, how to judge legitimacy, and how to read a guidelines page.</p><span class="card-link">Open the guide →</span></a>
<a class="path-card" href="/guides/how-to-follow-up-on-a-writing-pitch/"><span class="card-num">03</span><h3>Follow up on a pitch</h3><p>When to wait, what to say, and how to treat silence without burning bridges.</p><span class="card-link">Open the guide →</span></a>
</div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Transparent by design</p><h2>What BRYME claims — and what it will not.</h2></div></div><div class="card-grid">
<div class="path-card"><span class="card-num">VERIFY</span><h3>Official guidelines first</h3><p>BRYME links to, and checks against, each publication's own guideline — not third-party reposts.</p></div>
<div class="path-card"><span class="card-num">TESTED</span><h3>Marked as it happens</h3><p>Where BRYME has personally pitched, the journey is shown step by step — accepted, published, paid — never assumed.</p></div>
<div class="path-card"><span class="card-num">LIMIT</span><h3>No guaranteed outcome</h3><p>An open submission window does not guarantee acceptance, publication or payment.</p></div>
</div></div></section>'''
    structured = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": "BRYME",
         "url": BASE + "/", "description": SITE["description"]},
        {"@context": "https://schema.org", "@type": "Organization", "name": "BRYME", "url": BASE + "/",
         "founder": {"@type": "Person", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/"}},
    ]
    write("/", page_wf(title="BRYME | Writing opportunities, guides and getting published",
                       description="BRYME researches legitimate paid writing opportunities for African and international writers, and gives practical guides for pitching, submitting and getting paid.",
                       route="/", current="writing", body=body, schema_data=structured))


# ---------------------------------------------------------------------------
# /writing/ hub
# ---------------------------------------------------------------------------

def tracker_page() -> None:
    """Submission tracker (Brief §12). Local-first, no account.

    Deliberately not a "coming soon" stub: it is fully functional today
    against localStorage, with export/import so the data is portable, and the
    stored envelope is versioned so accounts can be layered on later (§13)
    without a migration that loses anyone's pitches."""
    statuses = [
        ("draft", "Draft", "Written but not sent."),
        ("submitted", "Submitted", "Sent. Clock started."),
        ("waiting", "Waiting", "Past the point where you would expect a fast no."),
        ("followup", "Follow-up", "Time to nudge, once, politely."),
        ("accepted", "Accepted", "Commissioned or taken."),
        ("rejected", "Rejected", "A no. Log it and pitch it elsewhere."),
        ("paid", "Paid", "Money actually received."),
    ]
    opts = "".join(f'<option value="{esc(k)}">{esc(l)}</option>' for k, l, _ in statuses)
    filter_opts = '<option value="">All pitches</option>' + opts
    flow = "".join(
        f'<li><b>{esc(l)}</b><span>{esc(d)}</span></li>' for k, l, d in statuses)

    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Submission tracker</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Your pitches</p>
<h1>Submission tracker.</h1>
<p>Pitching is a numbers game and the numbers are impossible to hold in your head. Track what you sent, where, when, and what came back — so you know which markets to chase and which to stop pitching.</p>
<p class="notice"><b>This stays in your browser.</b> No account, no sign-up, nothing sent to BRYME or anyone else. That also means it is tied to this browser on this device: use <b>Export</b> to keep a copy, and <b>Import</b> to move it or restore it.</p>
</section></div>
<section class="section"><div class="wrap">
  <div id="tracker">
    <div class="tk-bar">
      <button type="button" class="btn" id="tk-add">Add a pitch</button>
      <div class="tk-bar-right">
        <label class="sr-only" for="tk-filter">Show</label>
        <select id="tk-filter">{filter_opts}</select>
        <button type="button" class="btn secondary" id="tk-export">Export</button>
        <label class="btn secondary tk-importlabel" for="tk-import">Import
          <input type="file" id="tk-import" accept="application/json,.json" hidden></label>
      </div>
    </div>
    <p id="tk-notice" class="tk-notice" role="status" hidden></p>
    <div id="tk-stats" class="tk-stats" aria-live="polite"></div>

    <form id="tk-form" class="tk-form" hidden>
      <div class="tk-form-grid">
        <div class="tk-field wide"><label for="tk-f-pub">Publication <span aria-hidden="true">*</span></label>
          <input id="tk-f-pub" type="text" required placeholder="e.g. The Republic" autocomplete="off"></div>
        <div class="tk-field wide"><label for="tk-f-pitch">Pitch or title</label>
          <input id="tk-f-pitch" type="text" placeholder="What you sent them" autocomplete="off"></div>
        <div class="tk-field"><label for="tk-f-status">Status</label>
          <select id="tk-f-status">{opts}</select></div>
        <div class="tk-field"><label for="tk-f-submitted">Date submitted</label>
          <input id="tk-f-submitted" type="date"></div>
        <div class="tk-field"><label for="tk-f-expected">Reply expected by</label>
          <input id="tk-f-expected" type="date"></div>
        <div class="tk-field"><label for="tk-f-follow">Follow up on</label>
          <input id="tk-f-follow" type="date"></div>
        <div class="tk-field"><label for="tk-f-fee">Fee</label>
          <input id="tk-f-fee" type="text" placeholder="e.g. $250 or ₦100,000" autocomplete="off"></div>
        <div class="tk-field"><label for="tk-f-url">BRYME page</label>
          <input id="tk-f-url" type="text" placeholder="/writing/the-republic/" autocomplete="off"></div>
        <div class="tk-field wide"><label for="tk-f-notes">Notes</label>
          <textarea id="tk-f-notes" rows="2" placeholder="Editor's name, what they asked for, what to try next"></textarea></div>
      </div>
      <div class="tk-form-actions">
        <button type="submit" class="btn" id="tk-submit">Add pitch</button>
        <button type="button" class="btn secondary" id="tk-cancel">Cancel</button>
      </div>
    </form>

    <ul id="tk-list" class="tk-list"></ul>
    <p id="tk-empty" class="filter-status empty">Nothing tracked yet. Add your first pitch — or open any opportunity and use &ldquo;Track this pitch&rdquo;.</p>
  </div>
</div></section>
<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">The stages</p>
<h2>What each status means.</h2></div></div>
<ol class="tk-flow">{flow}</ol>
<p class="tool-note">A listing on BRYME is an invitation to pitch, never a promise of acceptance or payment. Mark something <b>Paid</b> only when the money has actually arrived.</p>
</div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Next</p>
<h2>While you wait.</h2></div></div>
<div class="card-grid">
<a class="path-card" href="/writing/?status=acceptingnow&amp;sort=pay"><span class="card-num">FIND</span><h3>Find the next market</h3><p>The best answer to one pending pitch is another pitch. Filter by pay, country and status.</p><span class="card-link">Search opportunities →</span></a>
<a class="path-card" href="/learn/writing-for-publication/how-to-pitch-an-editor/"><span class="card-num">PITCH</span><h3>Write a better pitch</h3><p>What editors actually read, and the follow-up rule.</p><span class="card-link">Read the guide →</span></a>
<a class="path-card" href="/learn/writing-for-publication/how-to-handle-a-rejection/"><span class="card-num">NO</span><h3>Handle a rejection</h3><p>What a no usually means, and what to do with the piece next.</p><span class="card-link">Read the guide →</span></a>
</div></div></section>
<script src="/assets/tracker.js" defer></script>'''
    write("/tracker/", page_wf(
        title="Submission tracker: track your writing pitches | BRYME",
        description="Track every pitch you send — publication, date, status, follow-up date and fee. Free, private, stored in your browser with no account. Export any time.",
        route="/tracker/", current="writing", body=body,
        schema_data={"@context": "https://schema.org", "@type": "WebApplication",
                     "name": "BRYME Submission Tracker",
                     "applicationCategory": "BusinessApplication",
                     "operatingSystem": "Any modern browser",
                     "url": BASE + "/tracker/",
                     "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}))



# ---------------------------------------------------------------------------
# Brief §14: "Today's Opportunities" — a reason to come back.
#
# Every section here is computed from real dates and real figures. Where a
# section would be empty or misleading it is omitted entirely rather than
# padded, and the page says how many there were. A feed that claims "new
# today" on a day when nothing changed teaches people to stop checking.
# ---------------------------------------------------------------------------

def _dl_date(rec: dict) -> str:
    d = rec.get("deadline") or {}
    return (d.get("date") or "") if isinstance(d, dict) else ""


def _days_since(iso: str) -> int:
    try:
        y, m, d = (int(x) for x in iso[:10].split("-"))
        return (_dt.date.fromisoformat(TODAY) - _dt.date(y, m, d)).days
    except Exception:
        return 10**6


def _days_until(iso: str) -> int:
    return -_days_since(iso)


def today_feed() -> None:
    recent = sorted((r for r in WRITING if _days_since(r.get("lastVerified") or "") <= 7),
                    key=lambda r: r.get("lastVerified") or "", reverse=True)

    closing = sorted((r for r in WRITING
                      if _dl_date(r) and 0 <= _days_until(_dl_date(r)) <= 90
                      and norm_status(r) not in ("closed",)),
                     key=lambda r: _dl_date(r))

    paying = sorted((r for r in WRITING
                     if usd_amount(r) is not None
                     and norm_status(r) in ("open", "rolling", "deadline")),
                    key=lambda r: usd_amount(r) or 0, reverse=True)[:8]

    anywhere = [r for r in WRITING
                if (r.get("eligibility") or {}).get("mode") in ("open", "worldwide")
                and norm_status(r) in ("open", "rolling")][:8]

    opening = sorted((r for r in WRITING
                      if isinstance(r.get("deadline"), dict)
                      and (r["deadline"].get("openingDate") or "")
                      and _days_until(r["deadline"]["openingDate"]) >= 0),
                     key=lambda r: r["deadline"]["openingDate"])

    def block(title, eyebrow, blurb, rows, empty_msg, limit=8):
        if not rows:
            return (f'<section class="section"><div class="wrap"><div class="section-head"><div>'
                    f'<p class="eyebrow">{esc(eyebrow)}</p><h2>{esc(title)}</h2></div></div>'
                    f'<p class="filter-status empty">{esc(empty_msg)}</p></div></section>')
        shown = rows[:limit]
        more = ""
        if len(rows) > limit:
            more = (f'<p class="tool-note">{len(rows) - limit} more not shown here — '
                    f'<a href="/writing/">search the full list</a>.</p>')
        return (f'<section class="section"><div class="wrap"><div class="section-head"><div>'
                f'<p class="eyebrow">{esc(eyebrow)}</p><h2>{esc(title)}</h2></div>'
                f'<p>{esc(blurb)}</p></div>'
                f'<div class="opp-list">{"".join(pub_card(r, "h3") for r in shown)}</div>'
                f'{more}</div></section>')

    blocks = [
        block("Checked in the last seven days", "Freshly verified",
              f"{len(recent)} listings had their pay, status and guideline re-checked by hand this week.",
              recent, "Nothing was re-checked in the last seven days."),
        block("Closing within 90 days", "Closing soon",
              "Dated windows that are still open. Past deadlines are excluded — they have closed, not 'closing soon'.",
              closing, "No listing has a stated deadline inside the next 90 days."),
        block("Highest stated pay, open now", "Best paid",
              "Ranked on the figure the publication itself states, converted to USD only for comparison.",
              paying, "No open listing currently states a figure."),
        block("Open to writers anywhere", "No country restriction",
              "Publications whose own guideline places no geographic restriction on who may submit.",
              anywhere, "No listing is currently recorded as open worldwide."),
    ]
    if opening:
        rows = "".join(
            f'<li><b>{esc(r["deadline"]["openingDate"])}</b> — '
            f'<a href="/writing/{esc(r["slug"])}/">{esc(r["publication"])}</a>'
            f'{" · " + esc(r["deadline"].get("display","")) if r["deadline"].get("display") else ""}</li>'
            for r in opening[:8])
        blocks.append(
            f'<section class="section alt"><div class="wrap"><div class="section-head"><div>'
            f'<p class="eyebrow">Opens later</p><h2>Reopening on a stated date.</h2></div>'
            f'<p>Closed today, with the publication naming when it reopens. Worth a diary note.</p></div>'
            f'<ul class="today-open">{rows}</ul></div></section>')

    n_open = sum(1 for r in WRITING if norm_status(r) in ("open", "rolling", "deadline"))
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Today</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Updated {TODAY}</p>
<h1>Today&rsquo;s opportunities.</h1>
<p>What changed, what is closing, and what pays most — recomputed from the record every time BRYME rebuilds. Every figure below is the publication&rsquo;s own; nothing here is estimated.</p>
<div class="source-line"><span><b>{len(WRITING)}</b> tracked</span><span><b>{n_open}</b> accepting now</span><span><b>{len(recent)}</b> verified this week</span><span><b>{len(closing)}</b> closing within 90 days</span></div>
</section></div>
{"".join(blocks)}
<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Keep track</p>
<h2>Do not rely on memory.</h2></div></div>
<div class="card-grid">
<a class="path-card" href="/tracker/"><span class="card-num">TRACK</span><h3>Submission tracker</h3><p>Log what you sent and when the follow-up is due. Free, private, stays in your browser.</p><span class="card-link">Open the tracker →</span></a>
<a class="path-card" href="/writing/"><span class="card-num">SEARCH</span><h3>Search everything</h3><p>Filter all {len(WRITING)} by country, genre, pay, length and status.</p><span class="card-link">Open the search →</span></a>
<a class="path-card" href="/learn/writing-for-publication/how-to-pitch-an-editor/"><span class="card-num">PITCH</span><h3>Write the pitch</h3><p>What editors read first, and the follow-up rule.</p><span class="card-link">Read the guide →</span></a>
</div></div></section>'''
    write("/today/", page_wf(
        title=f"Today's writing opportunities: verified {TODAY} | BRYME",
        description=f"Writing opportunities re-verified this week, windows closing within 90 days, and the highest-paying open markets — recomputed from {len(WRITING)} researched publications.",
        route="/today/", current="writing", body=body,
        schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": "Today's writing opportunities", "url": BASE + "/today/",
                     "dateModified": TODAY}))



# ---------------------------------------------------------------------------
# Brief §15: programmatic pages, "only where real data supports them".
#
# The guard is MIN_FOR_PAGE. A facet with three listings does not get a page,
# because a near-empty landing page is the thin programmatic SEO the brief
# and the earlier proposal both prohibit. Each page that IS generated carries
# figures computed from its own subset (pay range, typical length, how many
# are open, how many are open worldwide) plus hand-written framing — so it is
# not merely a filtered list with a heading.
# ---------------------------------------------------------------------------

# Two thresholds, not one. A genre page is a list — under 8 entries it reads as
# thin. A country page also carries hand-written market guidance and a second,
# much larger "open to writers here" view, so 5 researched listings is a real
# page. Brief §7 is explicit that Nigeria/Africa must not be sidelined while
# expanding US/UK coverage, and a single blanket threshold would have dropped
# Nigeria, the UK, Canada and Australia while keeping the 71-listing US page.
MIN_COUNTRY_PAGE = 5
MIN_TYPE_PAGE = 8
MIN_FOR_PAGE = MIN_TYPE_PAGE

PROG_COUNTRY_NOTES = {
    "US": "The largest group in the database by a wide margin, and the most competitive. Rates are usually stated per word or per piece, and most US publications pay 30 days after publication rather than on acceptance.",
    "NG": "Nigerian publications pay in naira and usually require a Nigerian bank account. Fees are smaller in absolute terms than US or UK markets; they are also far less competitive, reply faster, and are the most realistic first published credit for a writer based in Nigeria.",
    "UK": "UK magazines tend to want a tight pitch rather than a finished piece, and usually state rates per 1,000 words. Follow UK spelling and punctuation conventions throughout.",
    "CA": "Canadian markets frequently prioritise Canadian writers or Canadian subject matter — check each guideline, because BRYME does not treat a missing statement as an open call.",
    "AU": "Australian rates are quoted in Australian dollars, and several titles add superannuation on top of the fee for contributors. Reading periods are often seasonal.",
}

PROG_TYPE_NOTES = {
    "essays": "The broadest category here and the most competitive. An essay pitch lives or dies on the angle, not the subject — editors receive the subject constantly and the angle rarely.",
    "personal-essays": "Personal essays sell on what the experience reveals, not on the experience itself. Most markets want the piece finished rather than pitched, because voice cannot be judged from a summary.",
    "fiction": "Almost every fiction market wants the complete story, not a query. Read the word limits precisely: over the cap is an automatic decline at most journals.",
    "poetry": "Submission windows matter more here than in any other category, and most journals cap the number of poems per submission. Simultaneous submissions are usually allowed if you withdraw promptly.",
    "journalism": "Reported work needs access before it needs a pitch. Say in the pitch who you can already reach — that is often what decides a commission.",
    "articles": "Service and explainer work is the steadiest paid writing in this list. Editors are buying reliability and structure as much as prose.",
    "analysis": "Analysis markets want a defensible argument and sources. Say what you are claiming in the first two sentences.",
    "opinion": "Opinion desks move fast and reject fast. Timeliness is usually the deciding factor, so pitch within a day or two of the news it hangs on.",
    "reviews": "Most review commissions go to writers the desk already knows, so lead with your relationship to the form and any prior criticism you have published.",
    "creative-nonfiction": "Longer-form nonfiction with a literary register. Expect slow reading periods and set your expectations accordingly.",
    "interviews": "Interview commissions usually depend on access. If you can already reach the subject, say so first.",
}


def _prog_stats(rows: list) -> str:
    amts = [usd_amount(r) for r in rows]
    amts = [a for a in amts if a is not None]
    n_open = sum(1 for r in rows if norm_status(r) in ("open", "rolling", "deadline"))
    n_glob = sum(1 for r in rows if (r.get("eligibility") or {}).get("mode") in ("open", "worldwide"))
    bits = [f"<span><b>{len(rows)}</b> publications</span>",
            f"<span><b>{n_open}</b> accepting now</span>",
            f"<span><b>{n_glob}</b> open worldwide</span>"]
    if amts:
        lo, hi = min(amts), max(amts)
        bits.append(f"<span><b>${lo:,.0f}&ndash;${hi:,.0f}</b> stated pay (USD equiv.)</span>")
        bits.append(f"<span><b>{len(rows) - len(amts)}</b> state no figure</span>")
    return f'<div class="source-line">{"".join(bits)}</div>'


def _prog_page(slug: str, h1: str, kicker: str, intro: str, note: str,
               rows: list, filter_href: str, guides: list,
               extra_cta: tuple | None = None) -> None:
    rows = sorted(rows, key=lambda r: (0 if norm_status(r) in ("open", "rolling") else 1,
                                       -(usd_amount(r) or 0)))
    cards = "".join(pub_card(r, "h3") for r in rows)
    glinks = "".join(
        f'<a class="purpose-alt" href="{esc(h)}">{esc(t)}</a>' for h, t in guides)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / <a href="/writing/">Opportunities</a> / {esc(h1)}</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(kicker)}</p>
<h1>{esc(h1)}</h1>
<p>{esc(intro)}</p>
{_prog_stats(rows)}
<p class="notice">{esc(note)}</p>
<p class="prog-ctas"><a class="btn" href="{esc(filter_href)}">Filter these by pay, length and status →</a>
{f'<a class="btn secondary" href="{esc(extra_cta[0])}">{esc(extra_cta[1])}</a>' if extra_cta else ''}</p>
</section></div>
<section class="section"><div class="wrap"><div class="opp-list">{cards}</div></div></section>
<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Before you pitch</p>
<h2>Read these first.</h2></div></div><div class="purpose-links">{glinks}</div>
<p class="tool-note">Every listing links to the publication&rsquo;s own guideline and shows the date BRYME last checked it. A listing is an invitation to pitch &mdash; never a promise of acceptance or payment.</p>
</div></section>'''
    write(f"/writing-opportunities/{slug}/", page_wf(
        title=f"{h1} | BRYME",
        description=f"{len(rows)} researched publications — {intro[:120]}",
        route=f"/writing-opportunities/{slug}/", current="writing", body=body,
        schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": h1, "url": f"{BASE}/writing-opportunities/{slug}/",
                     "dateModified": TODAY,
                     "numberOfItems": len(rows)}))


PROG_ROUTES: list[str] = []



# ---------------------------------------------------------------------------
# Country discovery — the front door for "what can I pitch from here?"
#
# Everything on this page is server-rendered, including every count. The search
# box only hides cards that are already present in the HTML, so the page is
# complete and usable with JavaScript disabled.
#
# Two counts per country, deliberately not merged into one:
#   based here    - publications headquartered in that country
#   open to you   - publications whose OWN guideline confirms they accept you:
#                   explicitly open/worldwide, plus anything based there, plus
#                   restricted calls that name the writer's region.
#
# The "open to you" figure deliberately EXCLUDES records whose eligibility is
# not stated. BRYME's standing rule is that silence is not an open call, and
# counting silence would inflate every country to about 125 and tell a writer
# nothing useful. Those records get their own separate count on each card.
# ---------------------------------------------------------------------------
COUNTRY_FLAGS = {"US": "\U0001F1FA\U0001F1F8", "UK": "\U0001F1EC\U0001F1E7",
                 "CA": "\U0001F1E8\U0001F1E6", "AU": "\U0001F1E6\U0001F1FA",
                 "NG": "\U0001F1F3\U0001F1EC", "ZA": "\U0001F1FF\U0001F1E6",
                 "KE": "\U0001F1F0\U0001F1EA", "IE": "\U0001F1EE\U0001F1EA",
                 "DE": "\U0001F1E9\U0001F1EA", "NA": "\U0001F1F3\U0001F1E6",
                 "NP": "\U0001F1F3\U0001F1F5"}

REGION_MEMBERS = {
    "africa": {"NG", "KE", "ZA", "NA", "GH", "ET", "TZ", "UG", "RW", "SN", "EG", "MA"},
    "uk": {"UK"}, "ireland": {"IE"}, "canada": {"CA"},
    "australia": {"AU"}, "new-zealand": {"NZ"},
}
# Filled from COUNTRY_PROFILES below — every country has a page.


def _elig_mode(rec: dict) -> str:
    return (rec.get("eligibility") or {}).get("mode") or "not-stated"


def _names_your_region(rec: dict, iso: str) -> bool:
    """True when a restricted call explicitly names the writer's region."""
    for reg in ((rec.get("eligibility") or {}).get("includesRegions") or []):
        if iso in REGION_MEMBERS.get(reg, set()):
            return True
    return False


def country_discovery_page() -> None:
    by_base: dict[str, list] = {}
    for r in WRITING:
        b = (base_country(r["slug"]) or "").upper()
        if b:
            by_base.setdefault(b, []).append(r)

    worldwide = [r for r in WRITING if _elig_mode(r) in ("open", "worldwide")]
    n_worldwide = len(worldwide)
    ww_slugs = {r["slug"] for r in worldwide}

    rows = []
    for iso, based in sorted(by_base.items(), key=lambda kv: (-len(kv[1]), country_name(kv[0]))):
        name = country_name(iso)
        based_slugs = {r["slug"] for r in based}
        extras = [r for r in WRITING
                  if _elig_mode(r) == "restricted" and _names_your_region(r, iso)
                  and r["slug"] not in based_slugs]
        confirmed = ww_slugs | {r["slug"] for r in based} | {r["slug"] for r in extras}
        n_conf = len(confirmed)
        n_silent = sum(1 for r in WRITING
                       if _elig_mode(r) in ("not-stated", "unknown")
                       and r["slug"] not in confirmed)

        # A country with only one or two publications gets links straight to
        # those records rather than a near-empty listing page.
        prof = COUNTRY_PROFILES.get(iso) or {}
        cslug = prof.get("slug") or iso.lower()
        noun = "publication" if len(based) == 1 else "publications"
        based_cta = ('<div class="actions"><a class="btn secondary" href='
                     '"/writing-opportunities/' + esc(cslug) + '/">'
                     'See ' + str(len(based)) + ' ' + noun + ' in ' + esc(name)
                     + ' &rarr;</a></div>')

        extra_line = ""
        if extras:
            named = " &middot; ".join(
                '<a href="/writing/' + esc(r["slug"]) + '/">' + esc(r["publication"]) + '</a>'
                for r in extras)
            verb = 'welcomes' if len(extras) == 1 else 'welcome'
            extra_line = ('<p class="meta"><b>+' + str(len(extras)) + '</b> that specifically '
                          + verb + ' writers from ' + esc(name) + ' or its region: '
                          + named + '</p>')

        rows.append(
            '<article class="guide-card" data-country="' + esc(name) + '" data-iso="' + esc(iso) + '">'
            '<p class="kicker"><span class="kicker-dot"></span>'
            + COUNTRY_FLAGS.get(iso, "") + " " + esc(name) + '</p>'
            '<p class="country-counts"><b>' + str(len(based)) + '</b> based here &middot; <b>'
            + str(n_conf) + '</b> confirmed open to you</p>'
            + based_cta
            + '<div class="actions"><a class="btn" href="/writing-opportunities/remote/">'
            + str(n_worldwide) + ' open to writers anywhere &rarr;</a></div>'
            + extra_line
            + '<p class="meta">' + str(n_silent) + ' more do not state an eligibility rule '
            '&mdash; read each guideline before pitching.</p></article>')

    grid = "".join(rows)
    n_all = len(WRITING)
    body = (
        '<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / '
        '<a href="/writing/">Opportunities</a> / By country</nav>'
        '<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>By country</p>'
        '<h1>Find publications by country</h1>'
        '<div class="prose">'
        '<p><b>Where a magazine is based and who it accepts are two different questions.</b> '
        'A publication in New York may take pitches from anywhere; one in Lagos may only take '
        'Nigerian writers. Both facts matter, and most country lists collapse them into a single '
        'number that answers neither.</p>'
        '<p>So this page keeps them apart. For every country you get the publications '
        '<b>based there</b>, and separately the publications whose own guideline <b>confirms they '
        'are open to you</b> &mdash; wherever in the world those publications happen to sit.</p>'
        '<p>The second number counts only what a guideline actually says. Where a publication is '
        'silent about eligibility, BRYME records that as <b>not stated</b> and counts it '
        'separately rather than assuming a welcome. And a listing is an invitation to pitch, not '
        'a promise: no acceptance, publication or payment is ever guaranteed.</p>'
        '</div></section>'
        '<section class="section"><div class="wrap">'
        '<form class="country-search-form" role="search" onsubmit="return false;">'
        '<label for="country-search"><b>Search your country</b></label>'
        '<input type="search" id="country-search" name="country" autocomplete="country-name" '
        'placeholder="Type a country &mdash; Nigeria, United States, Kenya&hellip;" '
        'aria-describedby="country-status"></form>'
        '<p class="filter-status" id="country-status" aria-live="polite">'
        + str(len(by_base)) + ' countries with publications BRYME has verified</p>'
        '<div class="guide-grid" id="country-grid">' + grid + '</div>'
        '<p class="filter-status empty" id="country-empty" hidden>No country by that name yet '
        '&mdash; <a href="/writing/">search all ' + str(n_all) + ' opportunities</a> instead.</p>'
        '</div></section>'
        '<section class="section alt"><div class="wrap"><div class="section-head"><div>'
        '<p class="eyebrow">If yours is missing</p><h2>No country of your own on the list?</h2>'
        '</div></div><div class="prose"><p>BRYME only names a country here once it has verified a '
        'publication based there. A missing country does not mean you are shut out: the '
        '<b>' + str(n_worldwide) + ' publications open to writers anywhere</b> accept submissions '
        'regardless of where you live, and that is the right place to start.</p></div>'
        '<div class="actions"><a class="btn" href="/writing-opportunities/remote/">'
        'Open to writers anywhere &rarr;</a>'
        '<a class="btn secondary" href="/writing/">Search all ' + str(n_all) + ' opportunities</a>'
        '<a class="btn secondary" href="/regional/">Writing conventions by country</a></div>'
        '</div></section></div>'
        '<script src="/assets/country-filter.js" defer></script>')

    write("/writing/by-country/", page_wf(
        title="Find publications by country | BRYME",
        description=("Pick your country and see two numbers: publications based there, and "
                     "publications whose own guideline confirms they are open to writers "
                     "from there."),
        route="/writing/by-country/", current="writing", body=body,
        schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": "Writing opportunities by country",
                     "description": "Paid writing publications by country of publication and by stated eligibility.",
                     "url": BASE + "/writing/by-country/", "dateModified": TODAY,
                     "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


# ---------------------------------------------------------------------------
# Per-country publication pages.
#
# These replace the old five country views. Every country in the data now gets
# a page, including the ones with a single publication, because each page now
# carries genuinely country-specific editorial content and not just a filtered
# list: the flag, the two eligibility counts, the region-specific markets that
# name that country, its house spelling/date/CV conventions, its currency at a
# dated rate, and its pitching guide where one exists.
#
# That distinction matters. Eleven pages that differ only by a filtered list
# would be near-duplicates; eleven pages that answer "what do I need to know to
# pitch from here" are eleven different pages.
#
# Convention profiles are only asserted where BRYME has a source. Where a
# country is not covered by content/hub/regional.json, the page says so rather
# than inventing a profile.
# ---------------------------------------------------------------------------
COUNTRY_PROFILES = {
    "US": dict(slug="usa", cur="USD", spelling="-ize and -or: organize, color, honor, labor",
               dates="April 3, 2026 \u2014 month first, comma after the day",
               cv="R\u00e9sum\u00e9, usually one page, never with a photo",
               quotes="Double quotes, and commas and full stops go <em>inside</em> them",
               guide=("/learn/writing-for-publication/how-to-pitch-us-editors/", "How to pitch US editors"),
               note="The largest market BRYME tracks, and the one most likely to state a per-word rate up front."),
    "UK": dict(slug="united-kingdom", cur="GBP", spelling="-ise and -our: organise, colour, honour \u2014 though Oxford University Press and most UK academic journals use -ize",
               dates="3 April 2026 \u2014 day first, no commas",
               cv="CV, one to two pages, never with a photo",
               quotes="Single quotes are common, and punctuation goes <em>outside</em> unless it belonged to the quotation",
               guide=("/learn/writing-for-publication/how-to-pitch-uk-editors/", "How to pitch UK editors"),
               note="UK rates are usually quoted per 1,000 words rather than per word. Several UK markets charge a small submission fee."),
    "CA": dict(slug="canada", cur="CAD", spelling="A genuine hybrid: British vowels, American endings. <b>colour</b> and <b>organize</b> in the same sentence is correct here",
               dates="Both orders are in use, which makes numeric dates genuinely ambiguous \u2014 spell the month out",
               cv="Both CV and r\u00e9sum\u00e9 are used; never with a photo",
               quotes="US-style: punctuation inside the quotation marks",
               guide=("/learn/writing-for-publication/how-to-pitch-canadian-editors/", "How to pitch Canadian editors"),
               note="Canadian literary magazines publish their rates more openly than any other market BRYME has researched, largely because of arts-council funding norms. The authority is the Canadian Oxford Dictionary and Canadian Press style."),
    "AU": dict(slug="australia", cur="AUD", spelling="-ise and -our, followed more strictly than in Britain. But <b>program</b>, not programme, and <b>jail</b>, not gaol",
               dates="3 April 2026 \u2014 day first",
               cv="CV, never with a photo",
               quotes="Largely British usage; house styles vary",
               guide=("/learn/writing-for-publication/how-to-pitch-australian-editors/", "How to pitch Australian editors"),
               note="<b>Labor</b> without the u only ever refers to the Australian Labor Party \u2014 everywhere else it is labour. Getting that wrong in a political piece is an immediate tell. The authority is the Macquarie Dictionary."),
    "NG": dict(slug="nigeria", cur="NGN", spelling="-ise and -our, following British convention",
               dates="3 April 2026 \u2014 day first",
               cv="CV, and a photo is conventional and often expected, unlike in the US or UK",
               quotes="British usage",
               guide=None,
               note="Nigerian publications rarely publish a rate, which is why BRYME lists comparatively few. Several international markets specifically welcome African writers \u2014 they are listed below."),
    "KE": dict(slug="kenya", cur="KES", spelling="-ise and -our, following British convention",
               dates="3 April 2026 \u2014 day first", cv="CV", quotes="British usage", guide=None,
               note="A small base of Kenya-based markets, but the Africa-focused international calls below are open to Kenyan writers by name."),
    "ZA": dict(slug="south-africa", cur="ZAR", spelling="-ise and -our, following British convention",
               dates="3 April 2026 \u2014 day first", cv="CV", quotes="British usage", guide=None,
               note="South African writers are named in several Africa-focused international calls listed below."),
    "IE": dict(slug="ireland", cur="EUR", spelling="-ise and -our, following British convention",
               dates="3 April 2026 \u2014 day first", cv="CV, never with a photo",
               quotes="British usage", guide=("/learn/writing-for-publication/how-to-pitch-uk-editors/", "How to pitch UK and Irish editors"),
               note="Irish writers are eligible for UK-and-Ireland calls that exclude the rest of the world \u2014 see below."),
    "DE": dict(slug="germany", cur="EUR", spelling="Publications here writing in English generally follow US or UK house style \u2014 check the publication",
               dates="3 April 2026 in British style; 2026-04-03 ISO is common in technical writing",
               cv="A photo is conventional on a German CV, unlike almost everywhere else BRYME covers",
               quotes="Follow the publication's own house style", guide=None,
               note="BRYME currently tracks one Germany-based publication that pays in English."),
    "NA": dict(slug="namibia", cur=None, spelling=None, dates=None, cv=None, quotes=None, guide=None,
               note="BRYME has not separately verified a Namibian house-style profile. Southern African publishing generally follows British convention, but confirm against the publication's own guideline rather than assuming."),
    "NP": dict(slug="nepal", cur=None, spelling=None, dates=None, cv=None, quotes=None, guide=None,
               note="BRYME has not separately verified a Nepali house-style profile. South Asian English-language publishing generally follows British convention, but confirm against the publication's own guideline."),
}


def _fx_line(cur: str | None) -> str:
    """A dated, real conversion line. Never invents a rate."""
    if not cur or cur == "USD":
        return ""
    try:
        fx = json.loads((ROOT / "content/hub/fx-rates.json").read_text(encoding="utf-8"))
        rate = (fx.get("perUsd") or {}).get(cur)
        when = fx.get("fetchedAt", "")
    except Exception:
        return ""
    if not rate:
        return ""
    sym = {"NGN": "\u20a6", "GBP": "\u00a3", "EUR": "\u20ac", "CAD": "CA$",
           "AUD": "A$", "KES": "KSh", "ZAR": "R"}.get(cur, cur + " ")
    approx = f"{sym}{rate * 100:,.0f}"
    return ('<p class="meta">Pay below is shown exactly as each publication states it. '
            'For scale, <b>US$100</b> is about <b>' + approx + '</b> at the mid-market rate of '
            + esc(when) + '. BRYME never converts a stated rate \u2014 it only shows an approximation.</p>')


def _conventions_block(iso: str, name: str) -> str:
    p = COUNTRY_PROFILES.get(iso) or {}
    rows = [("Spelling", p.get("spelling")), ("Dates", p.get("dates")),
            ("CV or r\u00e9sum\u00e9", p.get("cv")), ("Quotation", p.get("quotes"))]
    rows = [(k, v) for k, v in rows if v]
    if not rows:
        return ('<section class="section"><div class="wrap"><h2>House style in ' + esc(name) + '</h2>'
                '<div class="prose"><p>' + (p.get("note") or "") + '</p></div>'
                '<div class="actions"><a class="btn secondary" href="/regional/">'
                'Full writing conventions reference &rarr;</a></div></div></section>')
    body = "".join('<tr><th scope="row">' + esc(k) + "</th><td>" + v + "</td></tr>" for k, v in rows)
    return ('<section class="section"><div class="wrap">'
            '<h2>House style when you write for ' + esc(name) + '</h2>'
            '<div class="prose"><p>Getting these wrong will not sink a good idea, but they are the '
            'fastest way for an editor to tell you have not read them.</p></div>'
            '<div class="compare-scroll"><table class="compare-table"><tbody>' + body + '</tbody></table></div>'
            '<div class="prose"><p>' + (p.get("note") or "") + '</p></div>'
            '<div class="actions"><a class="btn secondary" href="/regional/">'
            'Full writing conventions reference &rarr;</a></div></div></section>')


def country_page(iso: str, based: list) -> str:
    """One rich page per country. Returns the route written."""
    p = COUNTRY_PROFILES.get(iso) or {}
    slug = p.get("slug") or iso.lower()
    name = country_name(iso)
    flag = COUNTRY_FLAGS.get(iso, "")

    worldwide = [r for r in WRITING if _elig_mode(r) in ("open", "worldwide")]
    based_slugs = {r["slug"] for r in based}
    extras = [r for r in WRITING if _elig_mode(r) == "restricted"
              and _names_your_region(r, iso) and r["slug"] not in based_slugs]
    confirmed = {r["slug"] for r in worldwide} | based_slugs | {r["slug"] for r in extras}
    n_silent = sum(1 for r in WRITING if _elig_mode(r) in ("not-stated", "unknown")
                   and r["slug"] not in confirmed)

    ordered = sorted(based, key=lambda r: (0 if norm_status(r) in ("open", "rolling") else 1,
                                           -(usd_amount(r) or 0)))
    cards = "".join(pub_card(r, "h3") for r in ordered)

    extras_block = ""
    if extras:
        ex_cards = "".join(pub_card(r, "h3") for r in sorted(
            extras, key=lambda r: (0 if norm_status(r) in ("open", "rolling") else 1,
                                   -(usd_amount(r) or 0))))
        extras_block = (
            '<section class="section alt"><div class="wrap"><div class="section-head"><div>'
            '<p class="eyebrow">Open to you by name</p><h2>' + str(len(extras))
            + ' more that specifically welcome writers from ' + esc(name) + '</h2></div></div>'
            '<div class="prose"><p>These are based elsewhere, but their own guidelines name '
            + esc(name) + ' or its region. They are closed to most of the world and open to you.</p></div>'
            '<div class="opp-list">' + ex_cards + '</div></div></section>')

    guide = p.get("guide")
    guide_cta = ('<a class="btn secondary" href="' + esc(guide[0]) + '">' + esc(guide[1])
                 + ' &rarr;</a>') if guide else ""

    body = (
        '<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / '
        '<a href="/writing/">Opportunities</a> / <a href="/writing/by-country/">By country</a> / '
        + esc(name) + '</nav>'
        '<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>'
        + flag + ' ' + esc(name) + '</p>'
        '<h1>Writing opportunities in ' + esc(name) + '</h1>'
        '<p><b>' + str(len(based)) + '</b> ' + ('publication is' if len(based) == 1
          else 'publications are') + ' based in ' + esc(name)
        + ', and <b>' + str(len(confirmed)) + '</b> in total confirm in their own guidelines that '
        'they are open to writers from here. A further ' + str(n_silent) + ' do not state an '
        'eligibility rule either way.</p>'
        + _fx_line(p.get("cur")) +
        '<p class="notice">A listing is an invitation to pitch, never a promise of acceptance or '
        'payment. Every entry links to the publication&rsquo;s own guideline and the date BRYME '
        'last checked it.</p>'
        '<p class="prog-ctas"><a class="btn" href="/writing-opportunities/remote/">'
        + str(len(worldwide)) + ' open to writers anywhere &rarr;</a>'
        + guide_cta +
        '<a class="btn secondary" href="/writing/by-country/">Pick another country</a></p>'
        '</section></div>'
        '<section class="section"><div class="wrap"><div class="section-head"><div>'
        '<p class="eyebrow">Based here</p><h2>' + str(len(based)) + ' '
        + ('publication' if len(based) == 1 else 'publications') + ' based in '
        + esc(name) + '</h2></div></div><div class="opp-list">' + cards + '</div></div></section>'
        + extras_block
        + _conventions_block(iso, name) +
        '<section class="section alt"><div class="wrap"><div class="section-head"><div>'
        '<p class="eyebrow">Before you pitch</p><h2>Read these first.</h2></div></div>'
        '<div class="purpose-links">'
        '<a class="purpose-alt" href="/learn/writing-for-publication/how-to-pitch-an-editor/">How to pitch an editor</a>'
        '<a class="purpose-alt" href="/learn/freelance-paid-writing/how-to-find-paying-publications/">How to find paying publications</a>'
        '<a class="purpose-alt" href="/learn/freelance-paid-writing/how-to-price-your-freelance-writing/">How to price your writing</a>'
        '<a class="purpose-alt" href="/tracker/">Track your pitches</a>'
        + ('<a class="purpose-alt" href="' + esc(guide[0]) + '">' + esc(guide[1]) + '</a>' if guide else '')
        + '</div></div></section>')

    route = "/writing-opportunities/" + slug + "/"
    write(route, page_wf(
        title="Writing opportunities in " + name + " | BRYME",
        description=(str(len(based)) + " publications based in " + name + " that pay writers, plus "
                     + str(len(confirmed)) + " open to writers from " + name
                     + " — with stated pay, eligibility and house-style conventions."),
        route=route, current="writing", body=body,
        schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": "Writing opportunities in " + name,
                     "url": BASE + route, "dateModified": TODAY,
                     "numberOfItems": len(based)}))
    return route

def programmatic_pages() -> None:
    PROG_ROUTES.clear()
    base_guides = [("/learn/writing-for-publication/how-to-pitch-an-editor/", "How to pitch an editor"),
                   ("/learn/freelance-paid-writing/how-to-find-paying-publications/", "How to find paying publications"),
                   ("/tracker/", "Track your pitches")]

    # --- by country of publication -----------------------------------------
    # Every country now gets a page. The old MIN_COUNTRY_PAGE gate existed
    # because a filtered list of one is a thin page; country_page() carries
    # per-country conventions, currency, region-specific calls and a pitching
    # guide, so a one-publication country still has a real page behind it.
    groups: dict[str, list] = {}
    for r in WRITING:
        b = (base_country(r["slug"]) or "").upper()
        if b:
            groups.setdefault(b, []).append(r)
    for iso, rows in sorted(groups.items(), key=lambda kv: (-len(kv[1]), country_name(kv[0]))):
        if iso not in COUNTRY_PROFILES:
            continue
        PROG_ROUTES.append(country_page(iso, rows))

    # --- open worldwide -----------------------------------------------------
    remote = [r for r in WRITING
              if (r.get("eligibility") or {}).get("mode") in ("open", "worldwide")]
    if len(remote) >= MIN_TYPE_PAGE:
        _prog_page(
            "remote", "Writing opportunities open to writers anywhere",
            "No country restriction",
            "Publications whose own guideline places no geographic restriction on who may submit — the starting point if you are writing from outside the US and UK.",
            "BRYME only lists a publication here when its guideline actually says so. A guideline that is silent about eligibility is recorded as \u201cnot stated\u201d, not as open worldwide.",
            remote, "/writing/?global=1",
            base_guides + [("/regional/", "Writing conventions by country"),
                           ("/learn/writing-for-publication/why-your-first-pitch-may-be-rejected/", "Why a first pitch gets rejected")])
        PROG_ROUTES.append("/writing-opportunities/remote/")

    # --- by type of writing --------------------------------------------------
    tslug = {"essays": "essays", "personal-essays": "personal-essays", "fiction": "fiction",
             "poetry": "poetry", "journalism": "journalism", "articles": "articles",
             "analysis": "analysis", "opinion": "opinion", "reviews": "reviews",
             "creative-nonfiction": "creative-nonfiction", "interviews": "interviews"}
    tgroups: dict[str, list] = {}
    for r in WRITING:
        for t in norm_types(r):
            tgroups.setdefault(t, []).append(r)
    for t, rows in sorted(tgroups.items()):
        if t not in tslug or len(rows) < MIN_TYPE_PAGE:
            continue
        label = WRITING_TYPE_LABELS[t]
        _prog_page(
            tslug[t], f"Publications that pay for {label.lower()}",
            label,
            f"Markets currently recorded as publishing {label.lower()}, with the pay and word count each one states.",
            PROG_TYPE_NOTES.get(t, "Read the official guideline before pitching."),
            rows, f"/writing/?type={t}", base_guides)
        PROG_ROUTES.append(f"/writing-opportunities/{tslug[t]}/")

    # --- index --------------------------------------------------------------
    def li(href, label, n):
        return (f'<a class="guide-card" href="{esc(href)}"><span class="card-num">{n}</span>'
                f'<h3>{esc(label)}</h3><span class="card-link">Open →</span></a>')
    def cli(href, flag, label, n):
        return (f'<a class="guide-card" href="{esc(href)}"><span class="card-num">{n}</span>'
                f'<h3>{flag} {esc(label)}</h3><span class="card-link">Open &rarr;</span></a>')
    country_cards = "".join(
        cli(f"/writing-opportunities/{(COUNTRY_PROFILES[i] or {}).get('slug') or i.lower()}/",
            COUNTRY_FLAGS.get(i, ""), country_name(i), len(g))
        for i, g in sorted(groups.items(), key=lambda kv: (-len(kv[1]), country_name(kv[0])))
        if i in COUNTRY_PROFILES)
    type_cards = "".join(
        li(f"/writing-opportunities/{tslug[t]}/", WRITING_TYPE_LABELS[t], len(g))
        for t, g in sorted(tgroups.items(), key=lambda kv: -len(kv[1]))
        if t in tslug and len(g) >= MIN_TYPE_PAGE)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / <a href="/writing/">Opportunities</a> / Browse</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Browse by</p>
<h1>Writing opportunities by country and genre.</h1>
<p>Ready-made views of the {len(WRITING)} publications BRYME has researched. Every country gets a page — each carries its own house-style conventions, currency and region-specific calls, not just a filtered list. Genre views are only published where there are at least {MIN_TYPE_PAGE} real listings behind them.</p>
</section></div>
<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">By country</p><h2>Pick your country.</h2></div></div>
<div class="card-grid">{country_cards}
{li("/writing-opportunities/remote/", "Open to writers anywhere", len(remote))}</div></div></section>
<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">By what you write</p><h2>Genre and form.</h2></div></div>
<div class="card-grid">{type_cards}</div>
<p class="tool-note">Need a combination these pages do not cover — say, poetry in Canada paying over $100? <a href="/writing/">Use the full search</a>, which filters on all nine facets at once.</p>
</div></section>'''
    write("/writing-opportunities/", page_wf(
        title="Writing opportunities by country and genre | BRYME",
        description=f"Browse {len(WRITING)} researched paid-writing publications by country (USA, Nigeria, UK, Canada, Australia) and by genre (essays, fiction, poetry, journalism and more).",
        route="/writing-opportunities/", current="writing", body=body,
        schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": "Writing opportunities by country and genre",
                     "url": BASE + "/writing-opportunities/"}))
    PROG_ROUTES.append("/writing-opportunities/")


def country_band() -> str:
    """Country-first entry strip, shown at the top of /writing/.

    The Publish surface should ask "where are you writing from?" before it
    shows 138 cards. Server-rendered, flags included, every link a real page.
    """
    by_base: dict[str, list] = {}
    for r in WRITING:
        b = (base_country(r["slug"]) or "").upper()
        if b:
            by_base.setdefault(b, []).append(r)
    n_ww = sum(1 for r in WRITING if _elig_mode(r) in ("open", "worldwide"))
    chips = []
    for iso, rows in sorted(by_base.items(), key=lambda kv: (-len(kv[1]), country_name(kv[0]))):
        prof = COUNTRY_PROFILES.get(iso)
        if not prof:
            continue
        chips.append('<a class="country-chip" href="/writing-opportunities/'
                     + esc(prof["slug"]) + '/"><span class="chip-flag" aria-hidden="true">'
                     + COUNTRY_FLAGS.get(iso, "") + '</span><span class="chip-name">'
                     + esc(country_name(iso)) + '</span><span class="chip-n">'
                     + str(len(rows)) + '</span></a>')
    return ('<section class="section country-band"><div class="wrap">'
            '<div class="section-head"><div><p class="eyebrow">Start here</p>'
            '<h2>Where are you writing from?</h2></div>'
            '<a class="card-link" href="/writing/by-country/">Compare all countries &rarr;</a></div>'
            '<div class="prose"><p>Pick your country to see the publications based there, the calls '
            'that name your region, and the house style editors there expect. Or browse all '
            + str(len(WRITING)) + ' below.</p></div>'
            '<div class="country-chips">' + "".join(chips)
            + '<a class="country-chip country-chip--all" href="/writing-opportunities/remote/">'
            '<span class="chip-flag" aria-hidden="true">\U0001F30D</span>'
            '<span class="chip-name">Open to anyone</span><span class="chip-n">'
            + str(n_ww) + '</span></a></div></div></section>')

def writing_hub() -> None:
    n_open = sum(1 for r in WRITING if status_of(r)[2] == "open")
    cards = "".join(pub_card(r, "h2") for r in WRITING)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Writing opportunities</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Publications that pay writers</p>
<h1>Writing opportunities.</h1>
<p>{len(WRITING)} publications researched by BRYME. Each permanent page shows the type of writing, the published pay, word count, who it's open to, the submission method, and the official guideline to confirm before you pitch. A listing is an invitation to pitch — not a job offer or a promise of payment.</p>
<div class="source-line"><span><b>{len(WRITING)}</b> researched publications</span><span><b>{n_open}</b> currently accepting</span><span><b>{len([r for r in WRITING if (r.get("editorExperience") or {}).get("applied")])}</b> personally tested by BRYME</span></div></section>
{country_band()}
{writing_nav()}
<section class="section"><div class="how-steps"><h2 class="section-sub">How make-money writing works with BRYME</h2><ol class="steps">
<li><b>Pick an opportunity.</b> Each page names who it is open to — BRYME does not treat a missing country list as "open worldwide." Eligibility and diaspora rules are recorded where the publication states them.</li>
<li><b>Read the official guideline, not just the rate card.</b> Every page links to the publication's own guidelines and shows its last human-check date.</li>
<li><b>Understand the money before you pitch.</b> Payment is the published fee per accepted piece (or the real range), how and when it is paid, and whether it is per word, per piece or a variable honorarium. Rates are never invented.</li>
<li><b>Check the AI policy and rights.</b> Many publications reject AI-assisted work and take specific rights. BRYME records what each page says.</li>
<li><b>Pitch exactly as asked.</b> Send what the guideline requests through the official channel — a submission URL, form, or email.</li>
<li><b>Track it honestly.</b> Where BRYME has personally tested an opportunity, the journey is shown as it happens — pitch sent, response, accepted, scheduled, published, paid — and payment is only marked confirmed once it actually lands.</li>
</ol></div></section>
<section class="section alt"><div class="wrap opp-list" id="opp-list">{cards}</div></section>
<script src="/assets/opp-filter.js" defer></script></div>'''
    write("/writing/", page_wf(title="Writing opportunities for African and international writers | BRYME",
                              description=f"{len(WRITING)} paid writing publications researched by BRYME — with published pay, word count, eligibility, submission method and the official guideline to confirm before pitching.",
                              route="/writing/", current="writing", body=body,
                              schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                                           "name": "BRYME writing opportunities", "url": BASE + "/writing/",
                                           "dateModified": TODAY, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


# ---------------------------------------------------------------------------
# /writing/<slug>/ publication page
# ---------------------------------------------------------------------------
def _facts(rec: dict) -> str:
    pay = rec.get("pay") or {}
    wc = rec.get("wordCount") or {}
    el = rec.get("eligibility") or {}
    resp = rec.get("response") or {}
    sub = rec.get("submissionStatus") or "unknown"
    rows = [
        ("Payment", pay.get("display") or "See official guideline"),
        ("Word count", wc.get("display") or "See official guideline"),
        ("Submission", (rec.get("applyMethod") or "See official guideline")),
        ("International writers", "Yes" if el.get("allowsDiaspora") or el.get("mode") != "restricted" else "No — see eligibility"),
        ("Status", status_of(rec)[0]),
        ("Last verified", (rec.get("lastVerified") or TODAY)[:7]),
    ]
    cells = "".join(f'<dt>{esc(k)}</dt><dd>{esc(v)}</dd>' for k, v in rows)
    return f'<div class="quick-facts"><h2 class="section-sub">Quick facts</h2><dl>{cells}</dl></div>'


def _list(label: str, items: list | None) -> str:
    if not items:
        return ""
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return f'<h3>{esc(label)}</h3><ul>{lis}</ul>'


def _prose_list(label: str, text: str | None) -> str:
    if not text:
        return ""
    return f'<h3>{esc(label)}</h3><p>{esc(text)}</p>'


def _timeline(rec: dict) -> str:
    ex = rec.get("editorExperience") or {}
    if not ex.get("applied"):
        return ('<section class="section"><div class="notice"><strong>🟡 Research only.</strong> '
                'BRYME has researched this opportunity but has not yet submitted to it. Nothing here should be read as '
                'a claim of acceptance, publication or payment.</div></section>')
    stages = ex.get("stages") or {}
    labels = [
        ("pitch_submitted", "Pitch submitted"), ("response_received", "Editor responded"),
        ("accepted", "Pitch accepted"), ("article_submitted", "Article submitted"),
        ("scheduled_for_publication", "Scheduled / published"), ("published", "Published"),
        ("payment_confirmed", "Payment confirmed"), ("payment_received", "Payment received"),
    ]
    dots = []
    for key, label in labels:
        if stages.get(key):
            dots.append(f'<li class="tl-on"><span class="tl-dot"></span>{esc(label)}</li>')
    paid = bool(stages.get("payment_confirmed") or stages.get("payment_received"))
    status = (ex.get("status") or "submitted").replace("-", " ")
    return f'''<div class="timebox"><h3>BRYME experience</h3>
<p class="tl-status">Status (as recorded): <b>{esc(status.capitalize())}</b> · Payment: <b>{'Confirmed' if paid else 'Pending / Not confirmed'}</b></p>
<p class="tl-note">This is BRYME's own firsthand record. Payment is only marked confirmed once it actually lands — never assumed. Dates, where shown, are when each step happened.</p>
<ul class="tl">{''.join(dots)}</ul></div>'''


def verification_legend_page() -> None:
    """The badge legend, reachable from every opportunity page.

    Roadmap 3: readers must be able to find out what a status means from
    wherever they meet it, and colour must never be the only signal.
    """
    rows = [
        ("🟢", "Currently accepting", "accepting",
         "The publication's own guideline said submissions were open on the date shown in “Last verified”. It is a timestamp, not a promise — always confirm on the official page before you pitch."),
        ("🟢", "Rolling submissions", "rolling",
         "The publication accepts work year-round rather than in windows. Still check the guideline: rolling markets close without notice."),
        ("🟡", "Opens soon", "upcoming",
         "A future window has been announced. Note the date and prepare the pitch now."),
        ("🟡", "Limited window", "limited",
         "Submissions are open only for a stated period. Check the closing date on the official guideline."),
        ("🟡", "Information needs verification", "needs-verification",
         "BRYME could not confirm the current state from the official guideline. Treat the details as unconfirmed until reverified."),
        ("🔴", "Currently closed", "closed",
         "The guideline said submissions were closed when BRYME last checked. Many publications reopen — the record stays up so you can watch for it."),
    ]
    exp = [
        ("🟡", "Research only", "board-listed",
         "BRYME researched the publication from its own guideline but has <b>not</b> submitted to it. Nothing on the page is a claim of acceptance, publication or payment."),
        ("🔵", "Submitted", "verify",
         "BRYME personally sent a pitch or a piece to this publication and is waiting on the outcome."),
        ("🟢", "Accepted", "verify",
         "BRYME pitched and the publication accepted. Payment is a separate step and is only shown once confirmed."),
        ("📖", "Published", "verify",
         "BRYME's work appeared in the publication."),
        ("💰", "Paid", "verify",
         "Payment actually landed. BRYME never marks this from a promise — only from money received."),
        ("🔴", "Rejected", "verify",
         "BRYME submitted and was turned down. These stay published: a rejection is useful information about a market."),
        ("⚪", "Closed", "verify",
         "BRYME's own journey with this publication ended without a decision — usually because the market closed."),
    ]

    def row(icon, label, cls, meaning):
        return (f'<tr><td><span class="verify-badge {cls}">{icon} {esc(label)}</span></td>'
                f'<td>{meaning}</td></tr>')

    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / <a href="/writing/">Writing opportunities</a> / What the statuses mean</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Verification</p>
<h1>What BRYME's statuses mean.</h1>
<p>Every publication page carries two separate signals: whether the publication is <em>open</em>, and whether <em>BRYME has personally been through it</em>. They are deliberately not the same thing.</p></section>
<section class="section"><div class="prose">
<h2>1. Submission status — is the publication open?</h2>
<p>This describes the <b>publication</b>, taken from its own guideline on the date in “Last verified”.</p>
<div class="legend-table-wrap"><table class="legend-table">
<caption class="sr-only">Submission status badges and their meanings</caption>
<thead><tr><th scope="col">Badge</th><th scope="col">What it means</th></tr></thead>
<tbody>{"".join(row(i, l, c, m) for i, l, c, m in rows)}</tbody>
</table></div>

<h2>2. BRYME's own record — has BRYME actually done this?</h2>
<p>This describes <b>BRYME</b>, not the publication. It exists so you can tell researched listings apart from ones BRYME has personally tested.</p>
<div class="legend-table-wrap"><table class="legend-table">
<caption class="sr-only">BRYME experience badges and their meanings</caption>
<thead><tr><th scope="col">Badge</th><th scope="col">What it means</th></tr></thead>
<tbody>{"".join(row(i, l, c, m) for i, l, c, m in exp)}</tbody>
</table></div>

<h2>Why the emoji is never the only signal</h2>
<p>Each badge carries its wording as text, not just a colour or an icon, so the meaning survives a screen reader, a monochrome screen and colour blindness. If you can only see the shape and not the colour, the label still tells you everything.</p>

<h2>What “Last verified” means</h2>
<p>It is the month a human at BRYME last opened the publication's official guideline and checked this record against it. It is shown to the month rather than the day because that is the honest resolution of the check — a guideline can change the day after any check, which is why every page links to the official source.</p>

<h2>What BRYME will never claim</h2>
<ul>
<li>That an open window guarantees acceptance, publication or payment.</li>
<li>That a rate exists when the guideline does not state one.</li>
<li>That BRYME was paid, until the payment has actually arrived.</li>
<li>That a vacancy or opportunity belongs to BRYME when it belongs to the publication.</li>
</ul>

<h2>Something out of date?</h2>
<p>Publications open and close constantly, and BRYME would rather be corrected than wrong. Every publication page has a <b>Report an outdated listing</b> link, or you can <a href="/contact/">contact the desk</a> directly. Material corrections are logged on the <a href="/corrections/">corrections page</a>.</p>
</div></section></div>'''
    write("/verification/", page_wf(
        title="What BRYME's verification statuses mean | BRYME",
        description="A plain explanation of every BRYME badge: submission status, BRYME's own firsthand record, what “last verified” means, and what BRYME will never claim.",
        route="/verification/", current="writing", body=body,
        schema_data={"@context": "https://schema.org", "@type": "WebPage",
                     "name": "What BRYME's verification statuses mean",
                     "url": BASE + "/verification/",
                     "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


def trust_block(rec: dict) -> str:
    """Per-opportunity trust footer — roadmap 3.

    Every opportunity page must expose: what the badges mean, how to report the
    listing as outdated, and the editorial policy. Previously these lived only
    in the site footer.
    """
    pub = rec.get("publication") or "this publication"
    slug = rec.get("slug") or ""
    verified = (rec.get("lastVerified") or TODAY)[:7]
    subject = quote(f"Outdated listing: {pub}")
    mail_body = quote(
        f"Publication: {pub}\n"
        f"BRYME page: {BASE}/writing/{slug}/\n"
        f"Last verified on the page: {verified}\n\n"
        "What is out of date (please include the official guideline URL if you have it):\n"
    )
    return f'''<section class="section"><div class="wrap"><div class="trust-actions" aria-label="Check or correct this record">
  <div class="trust-actions-head">
    <h2>Check, question or correct this record</h2>
    <p>BRYME publishes its working, not just its conclusions. Last human check: <b>{esc(verified)}</b>.</p>
  </div>
  <div class="trust-actions-grid">
    <a class="trust-action" href="/verification/">
      <span class="trust-action-icon" aria-hidden="true">🏷️</span>
      <b>What do these statuses mean?</b>
      <span>Every badge on this page explained — open, closed, researched, tested, paid.</span>
    </a>
    <a class="trust-action" href="mailto:sodiqibrahim03@gmail.com?subject={subject}&amp;body={mail_body}">
      <span class="trust-action-icon" aria-hidden="true">⚠️</span>
      <b>Report an outdated listing</b>
      <span>Guideline changed, link dead, or submissions closed? Tell the desk and it gets rechecked.</span>
    </a>
    <a class="trust-action" href="/editorial-policy/">
      <span class="trust-action-icon" aria-hidden="true">📜</span>
      <b>How BRYME verifies</b>
      <span>The editorial standard behind this record: sources, dates, corrections and limits.</span>
    </a>
  </div>
</div></div></section>'''


def pub_page(rec: dict) -> None:

    slug = rec["slug"]
    pay = rec.get("pay") or {}
    wc = rec.get("wordCount") or {}
    el = rec.get("eligibility") or {}
    resp = rec.get("response") or {}
    label, cls, _state = status_of(rec)
    what = rec.get("whatTheyWant") or []
    dont = rec.get("whatTheyDontWant") or []
    reqs = rec.get("requirements") or []
    how = rec.get("howToSubmit") or []
    topics = (rec.get("writingTypes") or [])
    topic_display = ", ".join(t.replace("-", " ").capitalize() for t in topics) or rec.get("writingTypeLabel") or "—"
    official = rec.get("officialUrl") or ""
    apply_url = rec.get("applyUrl") or ""
    apply_email = rec.get("applyEmail") or ""
    method = rec.get("applyMethod") or ""
    rights = rec.get("rights") or ""
    pub = esc(rec.get("publication") or "")
    ai = rec.get("aiPolicy") or "not-stated"
    ai_display = {"no-ai": "No / restricted (reported)", "not-stated": "Not stated in the guideline",
                  "unknown": "Unknown", "allowed": "Allowed (per guideline)"}.get(ai, ai.replace("-", " ").capitalize())

    # Guides that connect to this publication (by shared topic keywords).
    keywords = set(rec.get("keywords") or [])
    guide_links = []
    for g in GUIDES:
        gk = set(g.get("topics") or [])
        if keywords & gk:
            guide_links.append(g)
    guide_links = guide_links[:3]
    guide_html = "".join(f'<a class="chip-card" href="/guides/{esc(g["slug"])}/"><b>📚</b><span>{esc(g["title"])}</span></a>' for g in guide_links)

    # Brief §3: last-verified + official link stated in one consistent place,
    # and §12: a one-click route into the tracker with the publication prefilled.
    _st = norm_status(rec)
    _stlab, _stdesc = STATUS_LABELS[_st]
    track_href = f"/tracker/?add={quote(rec.get('publication',''))}&url=/writing/{esc(rec['slug'])}/"
    submit_block = f'''<div class="verify-line"><span class="verify-badge {esc(_st)}">{esc(_stlab)}</span>
<span class="verify-when">Last verified {esc(rec.get("lastVerified") or "—")}</span>
{f'<a class="verify-official" href="{esc(official)}">Official submission page →</a>' if official else ''}</div>
<p class="tool-note">{esc(_stdesc)}</p>
<p><a class="btn secondary" href="{track_href}">Track this pitch</a></p>
<h3>How to submit</h3><p><b>{esc(method or "See official guideline")}</b></p>
<p>Apply through the <strong>official</strong> channel below. BRYME only records submission destinations it has verified.</p>
<ul>
<li>Official guideline: {f'<a href="{esc(official)}">opens the publication guideline (new tab)</a>' if official else 'Not recorded'}</li>
<li>Submission: {f'<a href="{esc(apply_url)}">{esc(method or "open the submission page (new tab)")}</a>' if apply_url else esc(method or "See official guideline")}</li>
{f'<li>Submission email: {esc(apply_email)}</li>' if apply_email else ''}
</ul>
{_list('What the guideline asks you to prepare', how) if how else ''}
<div class="notice"><strong>Safety note.</strong> Never pay to submit your work. A legitimate publication does not ask writers to pay a fee or provide identity documents to be considered. If you are asked to, do not proceed.</div>'''

    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / <a href="/writing/">Writing opportunities</a> / {pub}</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(topic_display)}</p>
<h1>{esc(rec['publication'])}</h1>
<p>{esc(rec.get('excerpt') or rec.get('title') or '')}</p>
<p class="source-line">{status_badge(rec)} <span class="verify-badge {cls}">Verified {esc((rec.get('lastVerified') or TODAY)[:7])}</span> <span class="byline">Researched by <a href="/author/ibrahim-sodiq/">BRYME Editorial Desk</a>.</span></p>
</section>
<div class="wrap two-col"><div>{_facts(rec)}</div><div>{_timeline(rec)}</div></div>
<section class="section"><div class="prose">
<h2>What this publication wants</h2>
<p>This is BRYME's summary of the publication's focus — not a copy of their website. <em>Type of writing:</em> {esc(topic_display)}. <em>Official guideline:</em> {f'<a href="{esc(official)}">{pub} guidelines</a>' if official else 'See the official site below'}.</p>
{_list('Topics, themes and styles they look for', what) if what else ''}
{_list('Subjects they avoid', dont) if dont else ''}
{_list('Key requirements', reqs) if reqs else ''}
<h3>Who can submit</h3>
<p>{esc(el.get('summary') or 'See the official guideline.')}</p>
{f'<h3>Rights</h3><p>{esc(rights)}</p>' if rights else ''}
<h3>AI policy</h3><p>{esc(ai_display)}</p>
<h2>How to write for them</h2>
<p><b>Official requirement:</b> always follow the publication's own guideline exactly.</p>
<p><b>BRYME's practical advice:</b> write for the publication's audience, use a clear structure, keep paragraphs short, lead with a specific angle, and confirm the word count before submitting. These are practical suggestions — they are <em>not</em> the publication's official rules.</p>
<h2>How to pitch</h2>
<p>Where a pitch is required, this is the general pattern BRYME recommends — always adapt it to the publication's guideline.</p>
<ol class="steps">
<li>Research the publication and read several recent pieces.</li>
<li>Choose a specific idea that fits their beat and audience.</li>
<li>Write a concise subject line naming your idea.</li>
<li>Introduce yourself in one or two lines (who you are, where you publish).</li>
<li>Explain the proposed piece in a short paragraph — angle, structure, length.</li>
<li>Say why it fits this publication.</li>
<li>Include 2–3 relevant clips or links.</li>
<li>Close professionally and thank them for their time.</li>
<li>Send through the official channel only.</li>
</ol>
{submit_block}
<h2>What happens after submission</h2>
<p><b>Expected response:</b> {esc(resp.get('label') or 'Not stated — BRYME does not invent a response time.')}</p>
<p>If the publication does not state a response time, BRYME records that it is unknown. A follow-up is generally reasonable after a couple of weeks; if there is still no response, treat that as a likely non-acceptance rather than a rejection. Acceptance is normally communicated by the publication. If they accept, they will tell you exactly how to submit the final piece and, for most, how and when payment is made.</p>
{f'<div class="guide-grid">{guide_html}</div>' if guide_html else ''}
</div></section>
<section class="section"><div class="card-grid">
<a class="path-card" href="{esc(rec.get('officialUrl') or '/writing/')}"><span class="card-num">OFFICIAL</span><h3>Read the official guideline</h3><p>Open the publication's own page and confirm everything on this record before you pitch.</p><span class="card-link">Open →</span></a>
<a class="path-card" href="/guides/how-to-write-a-pitch/"><span class="card-num">GUIDE</span><h3>How to write a pitch</h3><p>A step-by-step structure for a pitch that a busy editor can act on.</p><span class="card-link">Open the guide →</span></a>
</div></section></div>
{trust_block(rec)}'''

    desc = (rec.get("seoTitle") or f"{rec['publication']} writing submissions — BRYME research").split(" | ")[0]
    title = f"{desc} | BRYME"
    schema_data = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": f"{rec['publication']}: {rec.get('writingTypeLabel') or rec.get('title') or 'writing opportunity'}",
        "description": desc, "url": f"{BASE}/writing/{slug}/",
        "datePublished": (rec.get("publishedAt") or rec.get("lastVerified") or TODAY) + "T00:00:00+01:00",
        "dateModified": (rec.get("lastVerified") or TODAY) + "T00:00:00+01:00",
        "author": {"@type": "Person", "name": "BRYME Editorial Desk", "url": BASE + "/author/ibrahim-sodiq/"},
        "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
        "mainEntityOfPage": f"{BASE}/writing/{slug}/",
    }
    write(f"/writing/{slug}/", page_wf(title=title, description=desc, route=f"/writing/{slug}/",
                                      current="writing", body=body, schema_data=schema_data))


# ---------------------------------------------------------------------------
# Guides
# ---------------------------------------------------------------------------
GUIDES = [
    {"slug": "how-to-write-a-pitch", "title": "How to write a magazine pitch",
     "description": "The structure, subject line and clips that get a publication to say yes.",
     "topics": ["pitch", "essay", "magazine"], "toc": ["Know the publication", "Choose a specific idea",
     "Write a tight subject line", "Introduce yourself", "State the angle and structure", "Show you fit", "Attach clips", "Close well"],
     "body": "A pitch is a short letter that sells an idea before you write it. The single biggest mistake is pitching a vague topic; the second is not saying why it fits the publication.\n\n**Know the publication first.** Read three or four recent pieces. Note the length, the tone, whether they use personal essays or reported features, and what they explicitly do not publish.\n\n**Choose a specific idea, not a topic.** \u201cAn essay about my mother\u201d is a topic. \u201cAn essay about the one phrase my mother said that I have never been able to hear the same way again\u201d is an idea.\n\n**Write a subject line that names the idea.** Editors skim. Make the line say what the piece is.\n\n**Introduce yourself in one or two lines.** Who you are, where you have published, and a reason to trust you with this idea.\n\n**State the angle and the structure.** In a short paragraph: the argument or story, how it develops, and a rough word count. Give them a reason to say yes.\n\n**Show that you fit.** Explain briefly why this is the right publication for this piece.\n\n**Attach two or three clips.** Links are fine; a couple of strong, relevant pieces beat a long list.\n\n**Close professionally.** Thank them, say you are happy to adjust, and send through the official channel."},
    {"slug": "how-to-pitch-an-essay", "title": "How to pitch an essay",
     "description": "Adapt a pitch for personal essay and nonfiction markets.",
     "topics": ["essay", "pitch"], "toc": ["Personal essays need a voice", "Find the universal", "Be honest", "Match the word count", "Send the whole essay if asked"],
     "body": "Personal essays are the most personal kind of pitch, and the most misunderstood.\n\n**The idea must carry a voice, not just a story.** Something happened to you; what matters is the perspective you bring to it and what it says about something larger.\n\n**Find the universal in the specific.** A personal essay works when a reader who is not you can still recognise themselves in it.\n\n**Be honest.** Do not invent events or feelings. If you are pitching a real experience, it must be real.\n\n**Match the word count.** Essay markets are often strict about length. Check the guideline before you claim a length.\n\n**Some markets want the full essay.** Where the guideline says to send the complete piece rather than a pitch, follow that. Sending a pitch to a market that expects the full essay wastes everyone's time."},
    {"slug": "how-to-find-paid-writing-opportunities", "title": "How to find publications that pay writers",
     "description": "Where to look, how to judge legitimacy, and how to read a guidelines page.",
     "topics": ["opportunities", "finding", "legitimate"], "toc": ["Start with the bibliography", "Judge the pay", "Check the guideline", "Confirm it is current", "Keep records"],
     "body": "Finding publications that genuinely pay writers is about knowing where to look and how to filter out the ones that do not.\n\n**Start with BRYME's own research.** The writing opportunities hub is built from checking publications' own guidelines — pay, words, eligibility and submission method.\n\n**Judge the pay, not the promise.** Does the publication state a fee per piece or per word? Many are honest about this; ones that say \u201cpayment varies\u201d with no range need more care. BRYME never invents a rate.\n\n**Read the guidelines page.** This is the single most important step. It tells you the type of writing, the length, whether they want a pitch or the full piece, and their rights and AI policy.\n\n**Confirm it is current.** Publications close and reopen. Check the date, or reach out. BRYME shows the last verified date on every page.\n\n**Keep records.** Note the date you checked, the official URL, and what the guideline said. That is what makes verification possible."},
    {"slug": "how-to-submit-a-freelance-article", "title": "How to submit a freelance article",
     "description": "From reading the guidelines to sending the finished piece the right way.",
     "topics": ["submit", "article", "freelance"], "toc": ["Read the submission instructions", "Formatting and files", "Attachments and clips", "The submission channel", "Track and confirm"],
     "body": "Submitting a freelance article is where many writers stumble over boring details, and details matter.\n\n**Read the submission instructions to the end.** The guideline tells you whether they want a pitch or the full article, the word count, the format and the channel.\n\n**Format it the way they asked.** Some want a docx; some want text in an email; some use a form. Do not guess when the answer is in the guideline.\n\n**Attach exactly what is required.** A cover note or clips if asked. Do not add a long cover letter if they did not ask for one.\n\n**Use the official channel.** An email, a form, or a submission portal from the publication — never an invented address.\n\n**Track and confirm.** Note the date you sent it and, if you can, confirm receipt. If there is no stated response time, it is reasonable to follow up after a couple of weeks."},
    {"slug": "how-to-build-writing-samples", "title": "How to build writing samples",
     "description": "Create a small portfolio that gets editors to say yes.",
     "topics": ["samples", "portfolio", "portfolio"], "toc": ["Quality over quantity", "Write a few strong pieces", "Match each sample to the publication", "Self-publish where allowed", "Keep them linkable"],
     "body": "You do not need dozens of clips to get published — you need a handful of strong, relevant ones.\n\n**Quality over quantity.** Two or three sharp pieces beat a long list of weak ones.\n\n**Write a few strong pieces in the style you want.** If you want to write essays, write essays. If you want features, write features.\n\n**Match each sample to the publication.** When you pitch, send the clips most like the piece you want to write.\n\n**Publish where you can.** A personal blog or a free platform counts, provided the work is genuinely yours and well done. (Check the guidelines — some publications will not consider previously self-published work.)\n\n**Keep them linkable.** Live links are easier for an editor than files they have to download."},
    {"slug": "how-to-write-a-strong-query-letter", "title": "How to write a strong query letter",
     "description": "A concise query that gets attention for nonfiction and journalism.",
     "topics": ["query", "pitch", "journalism"], "toc": ["Lead with the idea", "Show the reporting you will do", "Give a clear angle", "State the length and deadline", "End with your credibility"],
     "body": "A query letter sells a nonfiction piece before it exists. It should make the editor want the story.\n\n**Lead with the idea.** First line: what the article is, in one sentence.\n\n**Show what you will report.** Who you will talk to, what you will investigate, and why you are the one to do it.\n\n**Give a clear angle.** Not \u201cwe should talk about X\u201d but \u201cthis piece argues / reveals / shows Y.\u201d\n\n**State the length and any deadline.** Tell the editor what you are proposing and how long it will take.\n\n**End with credibility.** A line on your experience and any publication credits."},
    {"slug": "how-to-find-international-writing-opportunities", "title": "How to find international writing opportunities",
     "description": "Find paid markets beyond your home country without falling for scams.",
     "topics": ["international", "opportunities", "remote"], "toc": ["Look for markets that welcome you", "Check the eligibility", "Understand exchange and tax", "Use only official channels", "Beware of upfront fees"],
     "body": "International opportunities can pay better, but they come with extra things to check.\n\n**Look for markets that explicitly welcome writers where you live.** BRYME records which publications are open to African and diaspora writers, and which are not.\n\n**Check the eligibility carefully.** \u201cInternational submissions welcome\u201d is not the same as \u201copen to writers in every country.\u201d Some markets restrict who can apply, and some are region-specific.\n\n**Understand pay and exchange.** A rate in dollars or euros is not automatically better once conversion and transfer costs are considered. Note the currency and how payment is made.\n\n**Use only official channels.** International submissions go through the publication's own guideline, form or email — never through a third party promising to pitch on your behalf.\n\n**Beware of anything asking you to pay.** A legitimate publication does not charge writers to be considered, and it does not promise publication for a fee."},
    {"slug": "how-african-writers-can-find-paid-publications", "title": "How African writers find paid publications",
     "description": "Find paid, legitimate markets that welcome African and diaspora writers.",
     "topics": ["african", "opportunities", "international"], "toc": ["Look for markets that name you", "Know the diaspora rules", "Watch the currency and transfer", "Use guidelines, not reposts", "Protect your work"],
     "body": "African writers have genuine options — the key is finding markets that actually welcome you and that pay.\n\n**Look for publications that name African and diaspora writers.** BRYME records eligibility explicitly, including whether a market is restricted to Africans or to the African diaspora.\n\n**Understand the diaspora rules carefully.** Some markets welcome Black African diasporas; others are restricted to African residents. Read the eligibility line, and BRYME shows it.\n\n**Watch the currency and how you will be paid.** A fee quoted in a foreign currency may take a while to reach you or cost you fees. Note both.\n\n**Use the guidelines, not reposts.** A third-party repost can be outdated or wrong. Confirm against the publication's own page.\n\n**Protect your work.** Send to official channels, keep a record of every submission and its date, and never pay to be published."},
    {"slug": "how-to-follow-up-on-a-writing-pitch", "title": "How to follow up on a writing pitch",
     "description": "When to wait, what to say, and how to treat silence.",
     "topics": ["follow-up", "pitch", "response"], "toc": ["Wait a reasonable time", "Keep it short", "Confirm you can try elsewhere", "Treat silence as a sign", "Move on without burning bridges"],
     "body": "Following up is normal, but it has to be done well.\n\n**Wait a reasonable time.** If the publication states a response window, respect it. A short, polite follow-up after a couple of weeks is reasonable.\n\n**Keep it short.** One or two lines: reference your pitch, ask if they had a chance to consider it, and offer to adjust.\n\n**Confirm you can pitch elsewhere.** Many markets appreciate knowing you are holding the idea for them. Make it easy for them to say yes.\n\n**Treat silence as a sign.** If there is no response after a follow-up or two, that is usually a no. BRYME does not invent response times — it records when they are not stated.\n\n**Move on without burning bridges.** Publications have small teams and big inboxes. A later, better pitch to the same market is fine."},
    {"slug": "how-long-should-you-wait-for-an-editor", "title": "How long should you wait for an editor?",
     "description": "A realistic approach to editor response times and silence.",
     "topics": ["response", "follow-up", "pitch"], "toc": ["Read the stated window", "The default two-week rule", "What silence usually means", "When to move on", "Keep the relationship"],
     "body": "There is no universal answer, but good practices help.\n\n**Read the stated window first.** If the guideline says \u201cwe reply within two weeks,\u201d respect that. BRYME records stated response times and flags when they are not stated.\n\n**The default patience rule.** If nothing is stated, a couple of weeks before a short follow-up is reasonable.\n\n**Understand what silence usually means.** No response is rarely a personal rejection — it is usually just a busy editor. But it is also not acceptance.\n\n**When to move on.** After a follow-up or two with no reply, politely treat it as a pass and pitch elsewhere.\n\n**Keep the relationship.** A brief, gracious note leaves the door open for a future pitch."},
    {"slug": "how-to-find-remote-writing-work", "title": "How to find remote writing work",
     "description": "Legitimate remote and freelance writing opportunities you can do from anywhere.",
     "topics": ["remote", "freelance", "opportunities"], "toc": ["Separate jobs from gigs", "Use legitimate marketplaces", "Check who is hiring", "Beware of unpaid trials", "Verify before you commit"],
     "body": "Remote writing work spans two very different things: ongoing freelance contracts and one-off paid publications.\n\n**Separate jobs from gigs.** A paid publication call is not a job offer and not a promise of payment; a remote freelance contract is ongoing work. BRYME keeps them apart.\n\n**Use legitimate marketplaces and the publication's own channel.** For publication work, use the guideline. For freelance gigs, use reputable platforms — and read the terms carefully.\n\n**Check who is actually hiring.** A real remote role names a client or an agency. Vague \u201cwe need writers\u201d posts with no company need care.\n\n**Beware of unpaid trials.** A limited, clearly-scoped paid trial is one thing; a long \u201ctest\u201d you are expected to do for free is a red flag.\n\n**Verify before you commit.** Confirm the client, the pay, and how you will be paid. BRYME never invents a rate or a deadline."},
    {"slug": "how-to-get-your-first-paid-writing-gig", "title": "Your first paid writing gig: a five-step starting path",
     "description": "Five concrete steps from your first sample to a pitch an editor will actually read.",
     "deeper": ("/learn/freelance-paid-writing/how-to-get-your-first-paid-writer-gig/",
                "The full guide: how to get your first paid writing gig"),
     "topics": ["first", "gig", "paid"], "toc": ["Write first, publish somewhere", "Pick a small, reachable target", "Pitch one specific idea", "Send under the official channel", "Treat rejection as data"],
     "body": "The first paid gig is usually small — the point is to get on the board.\n\n**Write first.** You need something to show. Write a couple of strong pieces and publish them somewhere (a blog, a platform, or a publication that accepts your work).\n\n**Pick a small, reachable target.** Aim at a modest market that publishes work like yours and that you can genuinely match. BRYME lists many such markets with their pay and word counts.\n\n**Pitch one specific idea.** Not a general capability, but one angle for one publication.\n\n**Use the official channel.** An unfamiliar or invented submission address is how opportunities go wrong.\n\n**Treat rejection as data.** Editors are busy. A pass on one pitch is not a verdict on you as a writer. Note what the market wanted and keep going."},
]


def guides_hub() -> None:
    cards = "".join(f'<a class="guide-card" href="/guides/{esc(g["slug"])}/"><span class="card-num">GUIDE</span><h2>{esc(g["title"])}</h2><p>{esc(g["description"])}</p><span class="card-link">Open the guide →</span></a>' for g in GUIDES)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Writing guides</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Learn the craft</p>
<h1>Writing guides.</h1>
<p>Practical, writer-first resources on pitching, submitting, building samples and getting paid. Each guide connects to the relevant writing opportunities.</p></section>
{section_nav([("learn","/learn/","How to write"),("guides","/guides/","Writing guides"),("tools","/tools/","Tools"),("templates","/templates/","Templates"),("checklists","/checklists/","Checklists"),("writing","/writing/","Paid opportunities")], "Writing resources", "guides")}
<section class="section alt"><div class="guide-grid">{cards}</div></section></div>'''
    write("/guides/", page_wf(title="Writing guides for pitching, submitting and getting paid | BRYME",
                             description="Practical BRYME writing guides on pitching publications, submitting articles, building samples and getting paid for freelance work.",
                             route="/guides/", current="learn", body=body,
                             schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME writing guides", "url": BASE + "/guides/", "dateModified": TODAY, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


def guide_page(g: dict) -> None:
    toc = "".join(f'<li>{esc(t)}</li>' for t in g.get("toc", []))
    markdown = g["body"]
    # Render the small markdown subset used above (**bold**, blank-line paragraphs, - lists).
    paras = []
    for block in markdown.split("\n\n"):
        b = block.strip()
        if not b:
            continue
        if b.startswith("- "):
            lis = "".join(f"<li>{esc(x.strip())}</li>" for x in b.split("\n") if x.strip().startswith("- "))
            paras.append(f"<ul>{lis}</ul>")
        else:
            parts = b.split("\n")
            body_txt = " ".join(p.strip() for p in parts)
            # inline **bold**
            import re
            body_txt = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", body_txt)
            paras.append(f"<p>{body_txt}</p>")
    # A short overview page may point at a fuller guide elsewhere on the site.
    if g.get("deeper"):
        _href, _label = g["deeper"]
        paras.append(
            f'<p class="notice">This is the short version. '
            f'<a href="{esc(_href)}">{esc(_label)}</a> goes further: rates, '
            f'where to look, and what to do after the first yes.</p>'
        )
    sections = "".join(paras)
    # Related publications by topic.
    gk = set(g.get("topics", []))
    related = [r for r in WRITING if gk & set(r.get("keywords", []))][:4]
    rel_cards = "".join(f'<a class="chip-card" href="/writing/{esc(r["slug"])}/"><b>✎</b><span>{esc(r["publication"])}</span></a>' for r in related)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / <a href="/guides/">Guides</a> / {esc(g["title"])}</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Writing guide</p>
<h1>{esc(g["title"])}</h1>
<p>{esc(g["description"])}</p>
<p class="byline">Researched and written by <a href="/author/ibrahim-sodiq/">BRYME Editorial Desk</a>.</p></section>
<section class="section"><div class="prose"><nav class="guide-toc"><b>In this guide</b><ol>{toc}</ol></nav>{sections}
{f'<h2>Related publications</h2><div class="guide-grid">{rel_cards}</div>' if rel_cards else ''}</div></section></div>'''
    write(f"/guides/{g['slug']}/", page_wf(title=f"{g['title']} | BRYME writing guides",
                                          description=g["description"], route=f"/guides/{g['slug']}/",
                                          current="learn", body=body,
                                          schema_data={"@context": "https://schema.org", "@type": "Article",
                                                       "headline": g["title"], "description": g["description"],
                                                       "url": f"{BASE}/guides/{g['slug']}/",
                                                       "datePublished": TODAY + "T00:00:00+01:00", "dateModified": TODAY + "T00:00:00+01:00",
                                                       "author": {"@type": "Person", "name": "BRYME Editorial Desk", "url": BASE + "/author/ibrahim-sodiq/"},
                                                       "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
                                                       "mainEntityOfPage": f"{BASE}/guides/{g['slug']}/"}))


# ---------------------------------------------------------------------------
# /tested/ index
# ---------------------------------------------------------------------------
def tested_page() -> None:
    tested = [r for r in WRITING if (r.get("editorExperience") or {}).get("applied")]
    rows = ""
    if tested:
        for r in tested:
            ex = r.get("editorExperience") or {}
            st = ex.get("status")
            rows += f'<tr><td>{esc(r["publication"])}</td><td><b>{esc((st or "submitted").replace("-", " ").capitalize())}</b></td><td>{"Confirmed" if (ex.get("stages") or {}).get("payment_confirmed") else "Pending"}</td><td><a href="/writing/{esc(r["slug"])}/">View →</a></td></tr>'
        table = f'<table class="pub-table"><thead><tr><th>Publication</th><th>BRYME status</th><th>Payment</th><th>Page</th></tr></thead><tbody>{rows}</tbody></table>'
    else:
        table = '<p>BRYME has not yet submitted to any opportunity. When it does, this page will show the complete, honest record.</p>'
    statuses = [("🟡", "Research only"), ("🔵", "Submitted"), ("🟢", "Accepted"),
                ("📖", "Published"), ("💰", "Paid"), ("🔴", "Rejected"), ("⚪", "Closed")]
    legend = "".join(f'<div class="trust-item"><span class="trust-icon">{e}</span>{lab}</div>' for e, lab in statuses)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / BRYME Tested</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Firsthand verification</p>
<h1>BRYME Tested.</h1>
<p>Opportunities BRYME has personally researched, submitted to, been accepted by, published with, or been paid by. The record is shown as it happens — and payment is only ever marked confirmed once it actually lands.</p></section>
<section class="section"><div class="trust-grid">{legend}</div></section>
<section class="section alt"><div class="section-head"><div><p class="eyebrow">Current notes</p><h2>{len(tested)} opportunity·tested</h2></div></div>{table}</section></div>'''
    write("/tested/", page_wf(title="BRYME Tested — opportunities personally verified | BRYME",
                             description="Writing opportunities BRYME has personally submitted to, been accepted by, published with, or been paid by — shown as a staggered, honest record.",
                             route="/tested/", current="writing", body=body,
                             schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME Tested", "url": BASE + "/tested/", "dateModified": TODAY, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


# ---------------------------------------------------------------------------
# About + trust pages
# ---------------------------------------------------------------------------
def about_page() -> None:
    body = '''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / About</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>About BRYME</p>
<h1>BRYME helps writers get published and paid.</h1>
<p>BRYME is an independent, Lagos-based editorial project led by Ibrahim Sodiq. It researches legitimate writing opportunities — the pay, the word count, who they are open to, and the official guideline — and gives writers practical guides for pitching, submitting and getting published.</p></section>
<section class="section"><div class="prose">
<h2>What BRYME publishes now</h2>
<ul>
<li>Permanent pages for every researched publication, with the official guideline linked.</li>
<li>Writing guides on pitching, submitting, building samples and getting paid.</li>
<li>BRYME Tested — a firsthand record where BRYME has personally submitted, been accepted, published or paid.</li>
</ul>
<h2>How opportunities are researched &amp; verified</h2>
<p>BRYME checks a publication's <strong>own</strong> guidelines page, records what it actually says about pay, word count, eligibility, submission method, rights and AI policy, and shows the date it was last verified. A listing is an invitation to pitch — it is not a job offer, and it is not a promise of payment.</p>
<h2>What BRYME will not do</h2>
<ul>
<li>It will not invent a rate, a deadline, an email or a submission URL.</li>
<li>It will not mark an opportunity as paid unless payment was actually confirmed.</li>
<li>It will not present BRYME's practical advice as an official publication requirement.</li>
</ul>
<h2>Who is accountable</h2>
<p>BRYME is created and edited by <a href="/author/ibrahim-sodiq/">Ibrahim Sodiq</a>. Report factual, link or status errors through the <a href="/contact/">Contact page</a>; material changes are recorded in <a href="/corrections/">Corrections</a>.</p>
</div></section></div>'''
    schema_data = {"@context": "https://schema.org", "@type": "AboutPage", "name": "About BRYME", "url": BASE + "/about/",
                   "dateModified": TODAY, "mainEntity": {"@type": "Organization", "name": "BRYME", "url": BASE + "/",
                   "founder": {"@type": "Person", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/"}}}
    write("/about/", page_wf(title="About BRYME | Writing research, guides and verification",
                             description="BRYME is an independent platform for writers — it researches legitimate paid writing opportunities and gives practical guides for getting published.",
                             route="/about/", current="about", body=body, schema_data=schema_data))


def empty_pages() -> None:
    trust = [
        ("/editorial-policy/", "Editorial policy", "Trust standard",
         "BRYME's rules for sources, authorship, dates, verification, automation, opinion, advertising and corrections."),
        ("/privacy/", "Privacy", "Privacy", "How BRYME handles personal information, analytics and third-party services."),
        ("/terms/", "Terms of use", "Terms of use", "Terms for using BRYME's editorial information and original content."),
        ("/disclaimer/", "Disclaimer", "Important limits", "BRYME's limits: no guarantee of acceptance, publication or payment; verify independently."),
        ("/corrections/", "Corrections", "Corrections", "BRYME's public record of material corrections to publications, sources and statuses."),
        ("/copyright/", "Copyright and source use", "Rights", "Copyright, attribution and rights-contact information for BRYME."),
        ("/contact/", "Contact BRYME", "Contact the desk", "Report a correction, a broken source link, or a rights concern with evidence."),
    ]
    for route, title, kicker, ds in trust:
        key = route.strip("/")
        page = TRUST_CONTENT.get(key) or {}
        if page.get("sections"):
            kicker = page.get("kicker", kicker)
            title = page.get("title", title)
            intro = page.get("intro", ds)
            prose = "".join(f"<h2>{esc(h)}</h2>{html}" for h, html in page["sections"])
        else:
            intro = ds
            prose = ("<p>This page will be published on the writing-first BRYME platform. For now, the "
                     "editorial standard is: sources first, no invented facts, no fabricated experience, "
                     "and payment only recorded once confirmed.</p>")
        body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / {esc(title)}</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(kicker)}</p><h1>{esc(title)}.</h1><p>{esc(intro)}</p></section>
<section class="section"><div class="prose">{prose}</div></section></div>'''
        write(route, page_wf(title=f"{title} | BRYME", description=ds, route=route, current="about", body=body,
                             schema_data={"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": BASE + route, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))

    author_body = '''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Author / Ibrahim Sodiq</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Founder and editor</p><h1>Ibrahim Sodiq.</h1>
<p>Ibrahim leads BRYME's source checks, opportunity research and editorial standards from Lagos, Nigeria.</p></section>
<section class="section"><div class="prose"><p>BRYME now focuses on writing: legitimate paid writing opportunities, practical guides, and a firsthand record where BRYME has personally pitched, been accepted, published or paid.</p></div></section></div>'''
    write("/author/ibrahim-sodiq/", page_wf(title="Ibrahim Sodiq | BRYME founder and editor",
                                            description="About Ibrahim Sodiq, founder and editor of BRYME's writing opportunities and guides platform.",
                                            route="/author/ibrahim-sodiq/", current="about", body=author_body,
                                            schema_data={"@context": "https://schema.org", "@type": "ProfilePage", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/", "mainEntity": {"@type": "Person", "name": "Ibrahim Sodiq", "jobTitle": "Founder and editor of BRYME"}}))

    not_found = '''<div class="wrap"><section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>404 · Page not found</p>
<h1>This page is not part of the BRYME writing platform.</h1>
<p>BRYME is now focused on writing opportunities, writing guides and getting published. Use the sections below.</p>
<div class="actions"><a class="btn" href="/writing/">Writing opportunities</a><a class="btn secondary" href="/guides/">Writing guides</a><a class="btn secondary" href="/tested/">BRYME Tested</a></div></section></div>'''
    (ROOT / "404.html").write_text(page_wf(title="Page not found | BRYME", description="The requested BRYME page was not found.",
                                           route="/404.html", current="", body=not_found, robots="noindex,follow"), encoding="utf-8")
    print("wrote 404.html")

    gone = '''<div class="wrap"><section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>410 · Moved to legacy</p>
<h1>The multi-niche BRYME content moved to the legacy archive.</h1>
<p>The old jobs, sports, entertainment, make-money and technology site is preserved on the <b>legacy-multiniche</b> branch. BRYME's main branch now focuses entirely on writing opportunities and guides.</p>
<div class="actions"><a class="btn" href="/writing/">Writing opportunities</a><a class="btn secondary" href="/guides/">Writing guides</a></div></section></div>'''
    (ROOT / "410.html").write_text(page_wf(title="Content moved to legacy archive | BRYME", description="The former multi-niche BRYME content moved to the legacy-multiniche branch.",
                                           route="/410.html", current="", body=gone, robots="noindex,follow"), encoding="utf-8")
    print("wrote 410.html")


if __name__ == "__main__":
    # Homepage is owned by the Writing Hub builder (build-writing-hub.py) so the
    # hub surface reads as one site; this builder still owns /writing/, /guides/,
    # /tested/, /about/ and the trust/legal pages.
    writing_hub()
    country_discovery_page()
    tracker_page()
    today_feed()
    programmatic_pages()
    for r in WRITING:
        pub_page(r)
    guides_hub()
    for g in GUIDES:
        guide_page(g)
    tested_page()
    verification_legend_page()
    about_page()
    empty_pages()
