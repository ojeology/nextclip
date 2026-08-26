#!/usr/bin/env python3
"""Apply the Sports Desk v2 chrome to every /sports/ page.

For each sports/**/*.html:
  1. ensure /assets/sports-hub.css + /assets/sports-skin.css load after site.css
  2. inject the scores bar (ticker auto-filtered to the page's league) and the
     league rail (correct chip marked active) right after </header>
Idempotent: pages already carrying [data-bsd-chrome] are skipped.
Usage: python3 scripts/apply-sports-skin.py [--dry]
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry" in sys.argv

SKIN_LINKS = (
    '<link rel="stylesheet" href="/assets/sports-hub.css">\n'
    '<link rel="stylesheet" href="/assets/sports-skin.css">'
)

# path segment -> (rail key, espn-style league filter)
LEAGUES = {
    "premier-league": "premier-league",
    "la-liga": "la-liga",
    "serie-a": "serie-a",
    "bundesliga": "bundesliga",
    "ligue-1": "ligue-1",
}
RAIL_KEYS = list(LEAGUES) + [
    "champions-league", "international", "transfers", "fpl",
    "comics", "clubs", "players", "records", "history",
]

RAIL = (
    ('premier-league', 'Premier League', '', ''),
    ('la-liga', 'La Liga', '', ''),
    ('serie-a', 'Serie A', '', ''),
    ('bundesliga', 'Bundesliga', '', ''),
    ('ligue-1', 'Ligue 1', '', ''),
    ('champions-league', 'Champions League', 'UCL', ''),
    ('international', 'International', '', ''),
    ('SEP', '', '', ''),
    ('transfers', 'Transfers', 'Live', 'is-live'),
    ('fpl', 'Fantasy', '', ''),
    ('comics', 'Comics', '', ''),
    ('clubs', 'Clubs', '', ''),
    ('players', 'Players', '', ''),
    ('records', 'Records', '', ''),
    ('history', 'History', '', ''),
)

ARROW = (
    '<svg viewBox="0 0 24 24" fill="none" width="13" height="13" aria-hidden="true">'
    '<path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2.2" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)

FALLBACK_TICKER = (
    '<div class="tk-track">'
    '<span class="tk"><em>Premier League</em><b>MCI 2\u20131 BOU</b><i>FT</i></span>'
    '<span class="tk"><em>Premier League</em><b>NEW 2\u20132 LIV</b><i>FT</i></span>'
    '<span class="tk"><em>La Liga</em><b>ELC 0\u20135 BAR</b><i>FT</i></span>'
    '<span class="tk"><em>Serie A</em><b>ROM 4\u20130 FIO</b><i>FT</i></span>'
    '</div>'
)


def league_filter(rel):
    """First sports/ path segment that names a league, if any."""
    parts = rel.split(os.sep)
    for seg in parts:
        if seg in LEAGUES:
            return seg
    return None


def active_key(rel):
    for seg in rel.split(os.sep):
        if seg in RAIL_KEYS:
            return seg
    return None


def build_chrome(rel):
    lg = league_filter(rel)
    act = active_key(rel)

    ticker_attr = ' data-sp-league="%s"' % lg if lg else ""
    cta_href = ("/sports/%s/matches/" % lg) if lg else "/sports/premier-league/matches/"

    chips = []
    for key, label, note, note_cls in RAIL:
        if key == "SEP":
            chips.append('<span class="bsd-ln-sep" aria-hidden="true"></span>')
            continue
        cur = ' aria-current="page"' if key == act else ""
        note_html = ' <span class="bsd-ln-note %s">%s</span>' % (note_cls, note) if note else ""
        chips.append('<a class="bsd-ln%s" href="/sports/%s/"%s>%s%s</a>' % (
            " is-active" if key == act else "", key, cur, label, note_html))

    return (
        '<div class="bsd-chrome" data-bsd-chrome>\n'
        '<div class="bsd-scoresbar" aria-label="Latest results">\n'
        '<div class="shell bsd-scoresbar-in">\n'
        '<span class="bsd-scoresbar-tag"><i class="bsd-live-dot"></i>Results</span>\n'
        '<div data-sp-engine data-sp-ticker%s>%s</div>\n'
        '<a class="bsd-scoresbar-cta" href="%s">Match centre %s</a>\n'
        '</div>\n</div>\n'
        '<nav class="bsd-leaguenav" aria-label="Leagues and desks">\n'
        '<div class="bsd-leaguenav-in">%s</div>\n'
        '</nav>\n</div>\n'
    ) % (ticker_attr, FALLBACK_TICKER, cta_href, ARROW, "".join(chips))


def patch(html, rel, is_hub):
    changed = False

    # 1. stylesheet links (idempotent per file)
    if "/assets/sports-skin.css" not in html:
        if is_hub:
            marker = '<link rel="stylesheet" href="/assets/sports-hub.css">'
            html = html.replace(
                marker, marker + '\n<link rel="stylesheet" href="/assets/sports-skin.css">', 1)
        else:
            marker = '<link rel="stylesheet" href="/assets/site.css">'
            html = html.replace(marker, marker + "\n" + SKIN_LINKS, 1)
        changed = True

    # 2. chrome (hub already has it)
    if not is_hub and "data-bsd-chrome" not in html:
        m = re.search(r"</header>", html)
        if m:
            html = html[:m.end()] + "\n" + build_chrome(rel) + html[m.end():]
            changed = True
            chrome = "chrome+"
        else:
            chrome = "NO-HEADER "
    else:
        chrome = ""

    return html, changed, chrome


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "sports", "**", "*.html"), recursive=True))
    stats = {"patched": 0, "skipped": 0, "errors": 0}
    for f in files:
        rel = os.path.relpath(f, ROOT)
        try:
            html = open(f, encoding="utf-8").read()
        except OSError as e:
            print("READ FAIL", rel, e)
            stats["errors"] += 1
            continue
        if 'data-nav="sports"' not in html:
            # sports page missing its nav context — restore it so scoped styles apply
            m = re.search(r"<body([^>]*)>", html)
            if m and "spx" in m.group(1):
                html = html[:m.start()] + '<body data-nav="sports"%s>' % m.group(1) + html[m.end():]
            else:
                stats["skipped"] += 1
                continue
        is_hub = rel == os.path.join("sports", "index.html")
        new, changed, chrome = patch(html, rel, is_hub)
        if changed and not DRY:
            open(f, "w", encoding="utf-8").write(new)
        stats["patched" if changed else "skipped"] += 1
        if chrome:
            print(chrome, rel)
    print(stats, "| dry-run" if DRY else "| applied")


if __name__ == "__main__":
    main()
