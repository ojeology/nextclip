# -*- coding: utf-8 -*-
"""BRYME Tech — the living-machine hub display (rebuild 2026-09-24).

One responsibility: turn the tech desk's own catalogue into the HTML for
``/tech/``. Imported by ``build-ecosystem.py`` (``tech_pages()``) and by
``build-tech-hub.py`` so the generator and the refresh path share one renderer
and can never drift apart.

Design contract (owner brief, 24 Sep 2026)
------------------------------------------
* "Rebuild the display, preserve every URL." No route is created, renamed,
  removed or redirected here. Every link this module emits points at a URL that
  already existed in the committed tree — enforced twice:
  ``scripts/validate-site-quality.js`` fails on any missing local target, and
  ``reports/tech-hub-2026-09-24/diff-urls.py`` compares the /tech/ URL set of
  the rebuilt artifact against the pre-rebuild baseline (must be identical).
* A living machine, not a blog feed: the hub carries the WHOLE desk in the
  HTML — every piece, linkable with JS switched off — then re-routes itself by
  what the visitor came to do, filters instantly, sorts, and remembers.
* Honest telemetry only. Every number printed here is counted from the
  catalogue at build time. No visitor counters we do not have, no simulated
  "live" activity, no invented freshness. The hub also reports the shelves it
  has not filled, because a machine that can read itself is more trustworthy
  than one that struts.
* Addiction, the ethical kind: the pull is utility — a keyboard palette,
  saved-for-later, "new since your last visit", "continue where you left off",
  a random deep cut into the long tail. All of it is ``localStorage`` on the
  visitor's device; nothing leaves the page; there are no streaks, no guilt
  counters, no manufactured urgency, and no control that cannot be closed.
* No inline JS anywhere (the family ships ``script-src 'self' https:``).
  Behaviour lives in ``assets/tech-hub.js``, styling in ``assets/tech-hub.css``,
  both self-hosted. Motion is gated on ``prefers-reduced-motion``; with JS off
  every row is still a plain link and every shelf is fully open.
"""
from __future__ import annotations

import html
import re

# The six ways a person arrives at a technology desk. The order is the filter
# priority used to pick a piece's primary shelf; secondary needs live in
# data-need, which is what the chips and the palette match against.
NEEDS = [
    ("solve", "Fix what broke",
     "Something stopped working. Diagnosis first, then the fix, in the order that finds the cause fastest."),
    ("secure", "Lock it down",
     "Passwords, 2FA, privacy settings, tokens, phishing: protection you can actually finish today."),
    ("compare", "Compare two things",
     "This or that, side by side, with the trade-off named instead of buried in paragraph nine."),
    ("choose", "Choose what to use",
     "Buying guides, free alternatives and subscription maths, for budgets that are real."),
    ("build", "Build and ship it",
     "Deploys, DNS, hosting, HTTP, Python and tooling, from people who ran the deploy and wrote down the failure."),
    ("understand", "Understand a thing",
     "What it is, how it works, who needs it, what it costs: the plain explanation before the decision."),
]
NEED_KEYS = [n[0] for n in NEEDS]

# Chip labels are single words so the toolbar stays scannable on a phone.
_CHIPS = [("solve", "Fix"), ("secure", "Secure"), ("compare", "Compare"),
          ("choose", "Choose"), ("build", "Build"), ("understand", "Understand")]

# Deterministic keyword rules. Display-only: they label and group, they move no
# URL, and the hub says out loud that the sorting is by keyword.
_RE_SOLVE = re.compile(
    r"not-?working|won-t|won\u2019t|no-sound|fail|fixed|fix-|-fix|problem|diagnos|error|crash"
    r"|slow|broken|black-screen|not-arriving|warning|debug|triage|checklist|signs|loud"
    r"|overheat|stuck|frozen|dies|glitch|acting-up")
_RE_SECURE = re.compile(
    r"password|2fa|mfa|two-factor|phish|privacy|encrypt|token|secure|security|breach|scam"
    r"|safety|permission|authenticat|vpn|backup|tracker|data-training|suspicious|is-it-safe")
_RE_UNDERSTAND = re.compile(
    r"^what-is|what-is-|-explained$|^explained|explained-|primer|myth|^why-|glossary|decode"
    r"|decoded|difference|similarities|meaning|actually-does|really-means|was-|were-")
_RE_COMPARE = re.compile(r"-vs-|^vs-|vs\b|compared|comparison|versus|matrix|scenario-table|side-by-side")
_RE_CHOOSE = re.compile(
    r"buying|best-|-worth|worth-it|refurb|alternativ|free-|plans|pricing|cost|which|fits-you"
    r"|spec-|specs|should-i|subscription|budget|saver|cheapest|worth")
_RE_BUILD = re.compile(
    r"deploy|build|host|domain|dns|ssl|cdn|git|api|python|json|server|static|sitemap|css"
    r"|front-end|setup|set-up|migrat|install|docker|command|script|terminal|sqlite|flask"
    r"|gunicorn|cron|schedule|curl|http|base64|uuid|regex|cli")

# Category -> primary need when the keywords say nothing.
_CAT_NEED = {
    "safety": "secure", "android": "solve", "windows": "solve",
    "web-and-hosting": "build", "coding": "build", "quant": "build",
    "smart-home": "build", "ai": "understand", "tools": "choose",
    "subscriptions": "choose", "streaming": "choose", "buying": "choose",
}

_KIND_BADGE = {
    "troubleshooting": "Diagnostic tree",
    "firsthand": "First-hand",
    "guide": "Guide",
}


def esc(value: object) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def now_iso() -> str:
    """The build date, honouring SOURCE_DATE_EPOCH (mirrors build-ecosystem's
    _build_now) so CI stays byte-deterministic while a real deploy gets the live
    date. The freshness engine compares real piece dates against this."""
    import os, datetime
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc).date().isoformat()
    return datetime.date.today().isoformat()


# Review cadence per shelf, from the master brief's Section 12: price/vendor-heavy
# shelves turn over fastest (90 days); stable mechanics can wait (180). Every
# number the freshness engine prints is derived from real piece dates.
CAT_CADENCE_DAYS = {
    "subscriptions": 90, "buying": 90, "safety": 90, "ai": 90,
    "tools": 180, "streaming": 180, "smart-home": 180, "android": 180,
    "windows": 180, "web-and-hosting": 180, "coding": 180, "quant": 180,
}


def U(path: str, up: str) -> str:
    """Root-relative for the pre-routing tree, /tech-prefixed for a routed
    caller. The two artifacts differ only by this prefix (build-routing.py)."""
    return path if not up else up + path


def needs_for(slug: str, cat: str, kind: str = "") -> list:
    """Primary need first, then every secondary need the piece answers."""
    hay = slug + " " + slug.replace("-", " ")
    hits = []
    if kind == "troubleshooting" or _RE_SOLVE.search(hay):
        hits.append("solve")
    if cat == "safety" or _RE_SECURE.search(hay):
        hits.append("secure")
    if _RE_COMPARE.search(hay):
        hits.append("compare")
    if cat in ("buying", "subscriptions") or _RE_CHOOSE.search(hay):
        hits.append("choose")
    if cat in ("web-and-hosting", "coding", "quant") or _RE_BUILD.search(hay):
        hits.append("build")
    if _RE_UNDERSTAND.search(slug):
        hits.append("understand")
    if not hits:
        hits = [_CAT_NEED.get(cat, "understand")]
    prim = next((n for n in NEED_KEYS if n in hits), "understand")
    return [prim] + [h for h in hits if h != prim]


def badge_for(a: dict) -> str:
    """The piece's own label. Deliberately conservative: nothing on the hub
    claims first-hand work the catalogue does not record as first-hand."""
    if a.get("recovered"):
        return "Archive"
    return _KIND_BADGE.get(a.get("kind", ""), "Guide")


def _row(a: dict, up: str) -> str:
    slug = a["slug"]
    needs = needs_for(slug, a["cat"], a.get("kind", ""))
    date = a.get("upd") or a.get("pub") or ""
    badge = badge_for(a)
    title = esc(a["title"])
    dek = (a.get("excerpt") or "").strip()
    if len(dek) > 72:
        dek = dek[:72].rstrip() + "\u2026"
    href = U("/" + slug + "/", up)
    out = ['<div class="tm-row" data-need="', esc(" ".join(needs)),
           '" data-sec="', esc(a["cat"]), '" data-date="', esc(date),
           '" data-kind="', esc(badge.lower().replace(" ", "-")), '">']
    out.append('<a class="tm-row-a" href="' + esc(href) + '"><b>' + title + "</b>")
    if dek:
        out.append("<small>" + esc(dek) + "</small>")
    out.append("</a>")
    out.append('<span class="tm-row-side">')
    if badge != "Guide":
        out.append('<i class="tm-badge" data-on="1">' + esc(badge) + "</i>")
    if date:
        out.append('<time datetime="' + esc(date) + '">' + esc(date[5:].replace("-", "/")) + "</time>")
    out.append("</span>")
    # No data-save attribute: build-routing.py rewrites href/src/action/content
    # only, so a URL parked in a custom attribute would ship unrouted
    # (/slug/ instead of /tech/slug/) and the saved list would link to a 404.
    # The button reads its target from the row's own anchor at click time.
    out.append('<button type="button" class="tm-save" aria-pressed="false">'
               '<span class="tm-save-ic" aria-hidden="true">\u25c7</span>'
               '<span class="tm-save-t">Save</span></button>')
    out.append("</div>")
    return "".join(out)


def _tool_row(t, up: str) -> str:
    slug, name, dek, art = t[0], t[1], t[3], t[4]
    out = ['<div class="tm-tool" data-tool><a href="' + esc(U("/tool/" + slug + "/", up)) + '"><b>'
           + esc(name) + "</b><small>" + esc(dek[:88]) + ("\u2026" if len(dek) > 88 else "") + "</small></a>"]
    if art:
        out.append('<a class="tm-tool-g" href="' + esc(U("/" + art + "/", up)) + '">the guide</a>')
    out.append("</div>")
    return "".join(out)


def _gauge(value: str, label: str, sub: str) -> str:
    return ('<div class="tm-gauge"><b>' + esc(value) + "</b><span>" + esc(label)
            + "</span><small>" + esc(sub) + "</small></div>")


def stats_for(arts: list, cat: dict) -> dict:
    """Every number the hub prints, counted from the catalogue."""
    by_cat: dict = {}
    for a in arts:
        by_cat.setdefault(a["cat"], []).append(a)
    for lst in by_cat.values():
        lst.sort(key=lambda x: (x.get("upd") or x.get("pub") or "", x["title"]), reverse=True)
    dates = sorted({(a.get("upd") or a.get("pub") or "") for a in arts} - {""})
    newest = dates[-1] if dates else ""
    need_rows: dict = {k: [] for k in NEED_KEYS}
    for a in arts:
        need_rows[needs_for(a["slug"], a["cat"], a.get("kind", ""))[0]].append(a)
    return {
        "by_cat": by_cat,
        "need_rows": need_rows,
        "n_pieces": len(arts),
        "n_sections": len(cat),
        "n_solve": sum(1 for a in arts if a.get("kind") == "troubleshooting"),
        "n_cmp": sum(1 for a in arts if _RE_COMPARE.search(a["slug"])),
        "n_hand": sum(1 for a in arts if a.get("kind") == "firsthand" and not a.get("recovered")),
        "n_arch": sum(1 for a in arts if a.get("recovered")),
        "newest": newest,
        "n_older": sum(1 for a in arts if (a.get("upd") or a.get("pub") or "") != newest),
        "thin": sorted((len(v), k) for k, v in by_cat.items() if len(v) < 10),
        "fresh": _freshness(arts),
    }


def _freshness(arts: list) -> dict:
    """The freshness engine: per-piece next-review-due dates derived from each
    piece's own date plus its shelf's cadence (CAT_CADENCE_DAYS). A piece with no
    date is counted as due now, which is the honest reading."""
    import datetime
    now = now_iso()
    overdue = soon = undated = 0
    due = []
    for a in arts:
        d = a.get("upd") or a.get("pub") or ""
        days = CAT_CADENCE_DAYS.get(a["cat"], 180)
        if not d:
            undated += 1; due.append(now); continue
        try:
            rd = (datetime.date.fromisoformat(d) + datetime.timedelta(days=days)).isoformat()
        except ValueError:
            undated += 1; rd = now
        due.append(rd)
        if rd < now: overdue += 1
        elif rd <= _add_days(now, 30): soon += 1
    future = sorted(x for x in due if x >= now)
    return {"now": now, "overdue": overdue, "soon": soon, "undated": undated,
            "next": future[0] if future else now}


def _add_days(iso: str, days: int) -> str:
    import datetime
    return (datetime.date.fromisoformat(iso) + datetime.timedelta(days=days)).isoformat()


def render(arts: list, tools: list, cat: dict, url_prefix: str = "", stamp: str = "") -> str:
    """The hub ``<main>`` body. ``url_prefix`` is "" for the pre-routing
    ecosystem tree and "/tech" when a caller wants routed-style URLs."""
    up = (url_prefix or "").rstrip("/")
    st = stats_for(arts, cat)
    by_cat = st["by_cat"]
    need_rows = st["need_rows"]
    n = st["n_pieces"]

    gauges = "".join([
        _gauge(str(n), "pieces on the desk", "every one linked below"),
        _gauge(str(st["n_sections"]), "sections", "each with its own shelf"),
        _gauge(str(len(tools)), "browser tools", "run on your device"),
        _gauge(str(st["n_cmp"]), "comparisons", "trade-offs named"),
        _gauge(str(st["n_solve"]), "diagnostic trees", "problem \u2192 cause \u2192 fix"),
        _gauge(str(st["n_hand"]), "first-hand builds", "we ran it, we wrote it"),
    ])

    need_tiles = ""
    for i, (key, label, blurb) in enumerate(NEEDS, start=1):
        need_tiles += ('<button type="button" class="tm-need" data-need="' + key
                       + '" aria-pressed="false"><span class="tm-need-k" aria-hidden="true">' + str(i)
                       + "</span><b>" + esc(label) + "</b><em class=\"tm-need-n\">"
                       + str(len(need_rows[key])) + " pieces</em><small>" + esc(blurb) + "</small></button>")

    shelves = ""
    for key, label, blurb in NEEDS:
        lst = sorted(need_rows[key], key=lambda x: (x.get("upd") or "", x["title"]), reverse=True)
        if not lst:
            continue
        rows = "".join(_row(a, up) for a in lst)
        shelves += ('<section class="tm-shelf" data-shelf="' + key + '"><h3 class="tm-shelf-h"><span>'
                    + esc(label) + "</span><em>" + str(len(lst)) + "</em></h3><p class=\"tm-shelf-d\">"
                    + esc(blurb) + "</p><div class=\"tm-rows\">" + rows
                    + "</div><button type=\"button\" class=\"tm-more\" data-more hidden>"
                    "Show every piece in this shelf</button></section>")

    sec_cards = ""
    for cslug, cvals in cat.items():
        cname, cdesc = cvals[0], cvals[1]
        href = esc(U("/" + cslug + "/", up))
        desc = cdesc[:112] + ("\u2026" if len(cdesc) > 112 else "")
        sec_cards += ('<a class="tm-sec-card" href="' + href + '"><b>' + esc(cname) + "</b><em>"
                      + str(len(by_cat.get(cslug, []))) + "</em><small>" + esc(desc) + "</small></a>")

    tools_html = "".join(_tool_row(t, up) for t in tools)

    if st["thin"]:
        thin_items = "".join(
            '<li><a href="' + esc(U("/" + k + "/", up)) + '">' + esc(cat[k][0]) + "</a> <span>"
            + str(cnt) + " pieces</span></li>" for cnt, k in st["thin"])
        thin_html = ('<div class="tm-readout tm-readout-warn"><p class="tm-ro-h">Self-read: thin shelves</p>'
                     '<ul class="tm-ro-list">' + thin_items + "</ul><p class=\"tm-ro-f\">Under ten pieces is a"
                     " stack of notes, not a shelf. These are what this desk builds next, in order. If one of"
                     " them is your problem, <a href=\"" + esc(U("/contact/", up)) + "\">say so</a> \u2014 reader"
                     " questions move the queue.</p></div>")
    else:
        thin_html = ('<div class="tm-readout"><p class="tm-ro-h">Self-read</p><p class="tm-ro-big">'
                     '<span>every section carries ten pieces or more</span></p></div>')

    fr = st["fresh"]
    cadence = ('<div class="tm-readout"><p class="tm-ro-h">Verification cadence</p>'
               '<p class="tm-ro-big"><time datetime="' + esc(fr["now"]) + '">' + esc(fr["now"]) + '</time>'
               '<span>the clock this desk checks itself against</span></p>'
               '<p class="tm-ro-f">' + str(fr["overdue"]) + ' piece' + ('s are' if fr["overdue"] != 1 else ' is')
               + ' past its re-verification date, ' + str(fr["soon"]) + ' due within 30 days'
               + (', ' + str(fr["undated"]) + ' carrying no date at all' if fr["undated"] else '')
               + '. Price- and vendor-heavy shelves turn over every 90 days, stable mechanics every 180. '
               + 'Next review on the calendar: <time datetime="' + esc(fr["next"]) + '">' + esc(fr["next"]) + '</time>.</p></div>')

    freshness = ('<div class="tm-readout"><p class="tm-ro-h">Verification sweep</p><p class="tm-ro-big">'
                 + ('<time datetime="' + esc(st["newest"]) + '">' + esc(st["newest"]) + "</time>" if st["newest"]
                    else "<time>\u2014</time>")
                 + "<span>newest date the desk carries</span></p><p class=\"tm-ro-f\">"
                 + str(st["n_older"]) + " of " + str(n) + " pieces carry a date older than that sweep. "
                 "Price- and vendor-dependent pages are re-verified on a rolling basis; each page prints its "
                 "own date, and a page never prints a date it cannot show."
                 + (" Stamp: " + esc(stamp) if stamp else "") + "</p></div>")

    rules = ('<div class="tm-readout"><p class="tm-ro-h">Standing rules</p><ul class="tm-ro-list">'
             "<li>No benchmark we did not run, and no \u201ctested\u201d without the machine in front of someone here.</li>"
             "<li>No pricing without a dated source; volatile numbers carry the day they were read.</li>"
             "<li>No fake winners in a comparison \u2014 choose A if / choose B if, and you decide.</li>"
             "<li>" + str(st["n_arch"]) + " pieces are recovered archive and labelled as such, not re-badged as fresh work.</li>"
             "<li>Corrections land on the page that was wrong, and are listed.</li></ul><p class=\"tm-ro-f\">"
             + " \u00b7 ".join('<a href="' + esc(U("/" + r + "/", up)) + '">' + lbl + "</a>"
                              for r, lbl in (("methodology", "Methodology"), ("corrections", "Corrections"),
                                             ("about", "About the desk"), ("contact", "Contact"),
                                             ("privacy", "Privacy")))
             + "</p></div>")

    memory = ('<div class="tm-memory" data-tm-memory hidden><p class="tm-mem-h">On this device</p>'
              '<div class="tm-mem-cols">'
              '<div class="tm-mem-col"><b>Saved for later</b><ul data-tm-saved></ul>'
              '<p class="tm-mem-empty" data-tm-saved-empty hidden>Nothing saved yet. Each row below carries a '
              '<span class="tm-save-ic" aria-hidden="true">\u25c7</span> Save control; saved items live in this '
              'browser only.</p></div>'
              '<div class="tm-mem-col"><b>Continue reading</b><ul data-tm-recent></ul>'
              '<p class="tm-mem-empty" data-tm-recent-empty hidden>You have not opened a piece on this desk from '
              'this browser yet.</p></div>'
              '</div>'
              '<div class="tm-mine" data-tm-mine hidden><p class="tm-mine-h">Your desk, by your own numbers</p>'
              '<ul class="tm-mine-list">'
              '<li><b data-tm-mine-opened>0</b><span>different pieces you have opened here</span></li>'
              '<li><b data-tm-mine-opens>0</b><span>total opens, this browser</span></li>'
              '<li><b data-tm-mine-saved>0</b><span>saved for later</span></li>'
              '<li><b data-tm-mine-last>\u2014</b><span>your last visit</span></li>'
              '</ul><p class="tm-mine-f">Counted only in this browser\u2019s local storage. No account, no server, no one else sees it.</p></div>'
              '<p class="tm-mem-f">Saved items and reading history stay in this browser\u2019s local storage. '
              'Nothing is uploaded and nothing is counted on a server; clearing site data clears it. '
              '<button type="button" class="tm-mem-clear" data-tm-mine-toggle>Show my own numbers</button> '
              '<button type="button" class="tm-mem-clear" data-tm-clear>Forget this desk on this device</button></p></div>')

    toolbox_href = esc(U("/tool/", up))
    count_href = "#tm-core"

    return "".join([
        '<main id="main" class="tm-machine"><div class="wrap">',

        '<section class="tm-boot" id="tm-boot">',
        '<p class="tm-eyebrow"><span class="tm-led" aria-hidden="true"></span>'
        'BRYME TECH <span class="tm-dot" aria-hidden="true">\u00b7</span> THE LIVING DESK'
        '<span class="tm-eyebrow-r">' + esc("swept " + st["newest"] if st["newest"] else "") + "</span></p>",
        '<h1 class="tm-h1">Practical technology. No theatre.</h1>',
        '<p class="tm-dek">You have a technology problem, question or decision. This desk is built to answer '
        'it: guides checked against the real products and real deploys, dated honestly, and arranged below by '
        'what you came here to <em>do</em> \u2014 not by when we filed it.</p>',
        '<div class="tm-boot-bar"><a class="btn" href="' + count_href + '">Read every one of the '
        + str(n) + ' pieces</a>'
        '<button type="button" class="tm-pal-open" data-tm-open-palette><span>Find a piece</span>'
        '<kbd aria-hidden="true">Ctrl</kbd><kbd aria-hidden="true">K</kbd></button>'
        '<a class="btn secondary" href="' + toolbox_href + '">Open the toolbox</a></div>',
        '<div class="tm-gauges">' + gauges + "</div>",
        memory,
        "</section>",

        '<section class="tm-band" id="tm-needs"><header class="tm-band-h">'
        "<h2>What brought you to the desk?</h2>"
        "<p>Six jobs. Pick one and the index below re-sorts itself to that job. Keys "
        '<kbd>1</kbd>\u2013<kbd>6</kbd>.</p></header>'
        '<div class="tm-needs">' + need_tiles + "</div></section>",

        '<section class="tm-band" id="tm-core"><header class="tm-band-h">'
        "<h2>The whole desk, open.</h2>"
        "<p>Every published piece on this desk is listed here, in the page itself \u2014 no &ldquo;load "
        "more&rdquo; wall standing between you and the answer. The shelves are grouped by the words in each "
        "title and summary; the section pages below are the formal index.</p></header>",
        '<div class="tm-toolbar"><div class="tm-search">'
        '<label class="sr-only" for="tm-q">Filter the desk by words in the title or summary</label>'
        '<input id="tm-q" type="search" data-tm-filter="text" autocomplete="off" spellcheck="false" '
        'placeholder="filter: dns, backup, python, router, free\u2026">'
        '<span class="tm-count" data-tm-count aria-live="polite">' + str(n) + " of " + str(n)
        + " shown</span></div>",
        '<div class="tm-chips" role="group" aria-label="Filter the desk">'
        + "".join('<button type="button" class="tm-chip" data-need="' + k + '" aria-pressed="false">'
                  + lbl + "</button>" for k, lbl in _CHIPS)
        + '<button type="button" class="tm-chip" data-kind="diagnostic-tree" aria-pressed="false">Diagnostic trees</button>'
        + '<button type="button" class="tm-chip" data-kind="first-hand" aria-pressed="false">First-hand</button>'
        + '<button type="button" class="tm-chip" data-saved="1" aria-pressed="false">Saved only</button>'
        + '<button type="button" class="tm-chip tm-chip-clear" data-tm-clear-filters hidden>Clear filters</button>'
        + "</div>",
        '<div class="tm-sort" role="group" aria-label="Sort each shelf">'
        '<button type="button" class="tm-sortb" data-sort="recent" aria-pressed="true">Recently verified</button>'
        '<button type="button" class="tm-sortb" data-sort="az" aria-pressed="false">A\u2013Z</button>'
        '<button type="button" class="tm-sortb" data-tm-dice hidden>Random deep cut</button>'
        "</div></div>",
        '<div class="tm-shelves" data-tm-shelves>' + shelves + "</div>",
        '<p class="tm-nomatch" data-tm-nomatch hidden>Nothing on the desk matches that yet. Try a plainer '
        "word \u2014 or ask us for it: the queue is built from reader questions, and the thin shelves above "
        "are the ones we are filling.</p>",
        "</section>",

        '<section class="tm-band tm-band-alt" id="tm-toolbox"><header class="tm-band-h">'
        "<h2>The toolbox.</h2><p>" + str(len(tools)) + " utilities that run entirely in your browser. No "
        "account, no upload, and nothing you type into one is sent anywhere \u2014 including to us.</p></header>"
        '<div class="tm-tools">' + tools_html + "</div>"
        '<p class="tm-band-f"><a href="' + toolbox_href + '">The whole shelf</a> \u00b7 each tool has a '
        "companion guide explaining the format underneath it.</p></section>",

        '<section class="tm-band" id="tm-sections"><header class="tm-band-h">'
        "<h2>Sections, in their own words.</h2><p>The formal shelves. Same pieces, arranged by subject "
        "instead of by need.</p></header>"
        '<div class="tm-secs">' + sec_cards + "</div></section>",

        '<section class="tm-band tm-band-alt" id="tm-standards"><header class="tm-band-h">'
        "<h2>Read the machine before you trust it.</h2><p>What this desk will and will not tell you, and "
        "where it currently falls short.</p></header>"
        '<div class="tm-reads">' + cadence + freshness + thin_html + rules + "</div></section>",

        '<p class="tm-noscript">This hub works without JavaScript \u2014 every piece is linked above. With '
        "JavaScript you also get instant filtering, a keyboard palette, saved-for-later and \u201cnew since "
        "your last visit\u201d, all stored on your device.</p>",
        '<div class="tm-palette" data-tm-palette hidden role="dialog" aria-modal="true" '
        'aria-label="Search the technology desk"><div class="tm-pal-in">'
        '<label class="sr-only" for="tm-pal-q">Search every piece on this desk</label>'
        '<input id="tm-pal-q" type="search" autocomplete="off" spellcheck="false" '
        'placeholder="a problem, a tool, a protocol \u2014 matches titles and summaries on your device">'
        "</div>"
        '<ul class="tm-pal-list" data-tm-pal role="listbox" aria-label="Matches"></ul>'
        '<p class="tm-pal-foot">\u2191\u2193 move \u00b7 Enter open \u00b7 Esc close \u00b7 ' + str(n)
        + " pieces indexed</p></div>",
        "</div></main>",
        # Only the stylesheet is emitted here. The machine script itself is
        # injected once per page by shell() for every tech page (hub included),
        # because the tracker half has to run on article pages too. Emitting it
        # here as well loaded the desk twice: the two keydown handlers toggled
        # the palette open and straight shut again.
        '<link rel="stylesheet" href="/assets/tech-hub.css">',
    ])
