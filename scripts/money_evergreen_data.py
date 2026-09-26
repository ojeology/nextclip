"""Source-driven, evergreen BRYME Money guides (not broker promotions).

Metadata and researched prose live in content/money-guides/. One route per
article; the ecosystem builder wraps it in the existing Money shell. This file
creates the hub shelves, breadcrumb, source list and related reading, so the
three published copies are generated from the same source.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "money-guides"
MANIFEST = json.loads((CONTENT / "manifest.json").read_text(encoding="utf-8"))
REVIEWED = MANIFEST["reviewed"]
SECTIONS = ("Save and grow", "Start here", "Markets & conditions", "Broker & platform checks", "Indicator lab")
# Existing Money routes are linked deliberately rather than re-published as
# competing copies. Navigation labels remain short on small screens.
MONEY_NAV = (
    ("Saving foundations", (
        ("emergency-fund-guide", "Emergency fund"),
        ("budget-50-30-20-explained", "50/30/20 budgeting"),
        ("debt-snowball-vs-avalanche", "Debt payoff methods"),
        ("compound-interest-explained", "Compound interest"),
        ("how-to-save-for-a-house-deposit", "House deposit plan"),
        ("how-mortgages-work-explained", "Mortgages, explained"),
        ("high-yield-savings-accounts-explained", "High-yield savings"),
        ("mortgage-payment-calculator", "Mortgage calculator"),
        ("index-funds-explained", "Index funds"),
        ("401k-explained", "401(k), explained"),
        ("how-state-pensions-work", "State pensions"),
        ("how-payslips-work-explained", "Payslips"),
        ("how-interest-rates-work-explained", "Interest rates"),
        ("debt-consolidation-explained", "Debt consolidation"),
        ("mortgage-types-explained", "Mortgage types"),
        ("mortgage-ltv-and-deposits-explained", "LTV and deposits"),
        ("sinking-funds-explained", "Sinking funds"),
        ("marginal-tax-calculator", "Tax bracket calculator"),
        ("life-insurance-basics-explained", "Life insurance basics"),
        ("how-insurance-premiums-are-calculated-explained", "How premiums work"),
        ("income-protection-insurance-explained", "Income protection"),
        ("savings-goal-calculator", "Savings goal calculator"),
        ("credit-card-payoff-calculator", "Card payoff calculator"))),
    ("Start here", (
        ("trading-for-beginners", "Trading for beginners"),
        ("stocks-forex-futures-and-cfds", "Markets & products"),
        ("trading-environments-explained", "Trading environments"),
        ("trade-types-explained", "Trade types & styles"),
        ("trading-risk-checklist", "Risk plan"))),
    ("Broker & costs", (
        ("how-to-check-a-trading-broker", "Check a broker"),
        ("how-to-choose-a-trading-platform", "Platform checklist"),
        ("trading-fees-explained", "Trading costs"),
        ("forex-spreads-and-pips", "Forex pips & spreads"),
        ("leverage-and-margin-explained", "Leverage & margin"))),
    ("Execution & indicators", (
        ("order-types-and-slippage", "Order execution"),
        ("technical-indicators-explained", "Indicator families"),
        ("rsi-indicator-guide", "RSI guide"),
        ("atr-indicator-guide", "ATR guide"),
        ("moving-averages-sma-vs-ema", "SMA vs EMA"))),
    ("Tools & research", (
        ("position-size-calculator", "Position size calculator"),
        ("expectancy-calculator", "Expectancy calculator"),
        ("backtesting-101", "Backtesting 101"),
        ("quantlab-explained", "QUANTLAB, explained"))),
)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def href(slug: str) -> str:
    return f"/money/{slug}/"


def guides() -> list[dict]:
    """Fail closed on malformed editorial metadata or missing content files."""
    if not re.fullmatch(r"20\d\d-\d\d-\d\d", REVIEWED):
        raise ValueError("Money guide review date is missing or invalid")
    rows = MANIFEST["articles"]
    if not rows or len({g["slug"] for g in rows}) != len(rows):
        raise ValueError("Money guide slugs must be nonempty and unique")
    known = {g["slug"] for g in rows} | {
        "technical-indicators-explained", "trade-types-explained", "position-sizing-101",
        "position-size-calculator", "expectancy-calculator", "backtesting-101", "quantlab-explained",
        "savings-goal-calculator", "credit-card-payoff-calculator",
        "mortgage-payment-calculator", "marginal-tax-calculator",
    }
    for g in rows:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", g["slug"]):
            raise ValueError(f"Invalid money guide slug: {g['slug']!r}")
        if g["section"] not in SECTIONS:
            raise ValueError(f"Invalid money guide section: {g['section']!r}")
        for key in ("title", "h1", "dek", "description", "summary"):
            if not g.get(key):
                raise ValueError(f"{g['slug']}: missing {key}")
        if len(g["description"]) > 170:
            raise ValueError(f"{g['slug']}: meta description too long")
        if len(g["description"]) < 70:
            raise ValueError(f"{g['slug']}: meta description too short")
        if not g.get("sources") or any(urlparse(s["url"]).scheme != "https" for s in g["sources"]):
            raise ValueError(f"{g['slug']}: an official/reference source URL must use HTTPS")
        if any(s not in known for s in g.get("related", [])):
            raise ValueError(f"{g['slug']}: related guide missing")
        text = (CONTENT / (g["slug"] + ".html")).read_text(encoding="utf-8")
        if re.search(r"<\s*(?:script|style|iframe|h1|main)\b", text, re.I):
            raise ValueError(f"{g['slug']}: article body contains an unsafe or duplicate shell element")
        if len(re.findall(r"<h2\s+id=", text)) < 3 or len(re.sub(r"<[^>]+>", "", text)) < 1800:
            raise ValueError(f"{g['slug']}: article needs substantial, structured original text")
        g["body_html"] = text
    for _, nav in MONEY_NAV:
        if any(slug not in known for slug, _ in nav):
            raise ValueError("Money navigation points to an unknown route")
    return rows


GUIDES = guides()
BY_SLUG = {g["slug"]: g for g in GUIDES}


def nav_groups():
    return tuple(
        (group, [(href(slug), label) for slug, label in links]) for group, links in MONEY_NAV
    )


def shelves_html() -> str:
    """One scannable, internal-link-rich index; no duplicate article excerpts."""
    blocks = [
        '<section class="section money-library" id="money-guides">',
        '<div class="section-head"><p class="kicker">Explore the subject</p>',
        '<h2>Build the base. Learn the market. Check the costs.</h2>',
        '<p class="lede">Evergreen explanations, not broker rankings or trading signals. '
        'Start with the saving foundations, then follow the linked calculations and primary sources.</p></div>',
    ]
    for section in SECTIONS:
        subset = [g for g in GUIDES if g["section"] == section]
        blocks.append(f'<h3 class="money-shelf-title">{esc(section)}</h3><div class="money-guide-grid">')
        for g in subset:
            blocks.append('<article class="money-guide-card"><span class="money-card-topic">'
                          + esc(section) + '</span><h4><a href="' + href(g["slug"]) + '">'
                          + esc(g["h1"]) + '</a></h4><p>' + esc(g["summary"])
                          + '</p><span class="money-card-action" aria-hidden="true">Read the guide</span></article>')
        blocks.append('</div>')
    blocks.append('</section>')
    return "".join(blocks)


def body_for(g: dict, disclaimer: str) -> str:
    # Guide HTML is hand-authored and only bundled into this trusted repository;
    # all manifest values and TOC labels are escaped before entering markup.
    headings = re.findall(r'<h2 id="([a-z0-9-]+)">([^<]+)</h2>', g["body_html"])
    if len(headings) < 3 or len({i for i, _ in headings}) != len(headings):
        raise ValueError(f"{g['slug']}: H2 anchors must be unique and present")
    toc = ('<nav class="money-toc" aria-label="On this page"><b>In this guide</b><ol>'
           + "".join('<li><a href="#' + esc(ident) + '">' + esc(label) + '</a></li>'
                     for ident, label in headings)
           + '</ol></nav>')
    sources = ('<section class="money-source-block" aria-labelledby="sources-title">'
               '<h2 id="sources-title">Sources and further reading</h2>'
               '<p>Links were reviewed ' + REVIEWED + '. Regulatory permissions, firm status and product terms can change; use the current official register before acting.</p><ol>'
               + "".join('<li><a href="' + esc(s["url"]) + '" rel="noopener">' + esc(s["label"]) + '</a></li>'
                         for s in g["sources"]) + '</ol></section>')
    related = ('<section class="money-related" aria-label="Read next"><h2>Keep learning</h2><ul>'
               + "".join('<li><a href="' + href(slug) + '">'
                         + esc(BY_SLUG[slug]["h1"] if slug in BY_SLUG else
                               next((label for _, links in MONEY_NAV for s, label in links if s == slug),
                                    slug.replace("-", " ").capitalize()))
                         + '</a></li>' for slug in g["related"]) + '</ul></section>')
    return ('<div class="wrap"><nav class="crumb" aria-label="Breadcrumb">'
            '<a href="/money/">Money</a> / ' + esc(g["h1"]) + '</nav>'
            '<section class="cover money-guide-cover"><p class="kicker">BRYME Money · '
            + esc(g["section"]) + '</p><h1 class="cover-title">' + esc(g["h1"])
            + '</h1><p class="cover-dek">' + esc(g["dek"]) + '</p>'
            '<p class="byline">BRYME Money editorial desk · Sources reviewed '
            + REVIEWED + ' · <a href="/money/editorial-policy/">Editorial policy</a></p>'
            '</section><section class="section money-article"><div class="prose">'
            + toc + g["body_html"] + sources + related + '</div></section>'
            + disclaimer + '</div>')


def pages(disclaimer: str) -> list[dict]:
    return [
        {"route": "/" + g["slug"] + "/", "title": g["title"],
         "desc": g["description"], "body": body_for(g, disclaimer)}
        for g in GUIDES
    ]
