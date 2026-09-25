# -*- coding: utf-8 -*-
"""desk_hub_render.py — the living-machine hub, generalized to any desk.

Derived from tech_hub_render.py (the tech desk rebuild, 2026-09-24), which
remains the untouched reference implementation for /tech/. Owner brief
(25 Sep 2026): "Tech is now the standard. Every other niche must follow tech."
This module carries that standard to the other desks — same contract:

* Rebuild the display, preserve every URL. The renderer only links to routes
  the caller's catalogue already contains, plus the desk's own legal pages.
* A living machine: the hub carries the WHOLE desk in the HTML — every piece
  linkable with JS off — then filters, sorts and remembers on-device.
* Honest telemetry: every number counted from the catalogue at build time.
* Ethical pull only: save-for-later, continue-reading, new-since-last-visit.
  All localStorage, nothing leaves the device, no streaks, no guilt counters.
* No inline JS. Behaviour lives in assets/tech-hub.js (shared; it reads the
  desk from data-tm-desk and namespaces its storage keys per desk), styling in
  assets/tech-hub.css (token-driven: each desk's accent comes from its own
  inlined family CSS).

render(arts, tools, cat, cfg, url_prefix="", stamp="") — cfg carries the desk's
identity (brand, headline, dek, needs, cadence, gauges spec, rules, clusters).
"""
from __future__ import annotations

import html
import re

_RE_COMPARE = re.compile(r"-vs-|^vs-|vs\b|compared|comparison|versus|side-by-side")
_RE_UNDERSTAND = re.compile(
    r"^what-|what-|-explained$|^explained|explained-|myth|^why-|^benefits-of|"
    r"actually-does|what-evidence|honest|truth|worth|does-to-your-body")


def esc(value: object) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def now_iso() -> str:
    import os, datetime
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc).date().isoformat()
    return datetime.date.today().isoformat()


def _add_days(iso: str, days: int) -> str:
    import datetime
    return (datetime.date.fromisoformat(iso) + datetime.timedelta(days=days)).isoformat()


def U(path: str, up: str) -> str:
    return path if not up else up + path


def needs_for(a: dict, need_keys: list) -> list:
    """Primary need is the catalogue's own assignment; the slug may add
    secondaries (a comparison is always also filterable as a comparison)."""
    hits = [a.get("need") or "understand"]
    slug = a["slug"]
    if _RE_COMPARE.search(slug) and "compare" not in hits:
        hits.append("compare")
    if _RE_UNDERSTAND.search(slug) and "understand" not in hits:
        hits.append("understand")
    prim = next((nk for nk in need_keys if nk in hits), need_keys[-1])
    return [prim] + [h for h in hits if h != prim]


def badge_for(a: dict, kind_badges: dict) -> str:
    return kind_badges.get(a.get("kind", ""), "Guide")


def _row(a: dict, up: str, kind_badges: dict, need_keys: list) -> str:
    slug = a["slug"]
    needs = needs_for(a, need_keys)
    date = a.get("upd") or a.get("pub") or ""
    badge = badge_for(a, kind_badges)
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
    out.append('<button type="button" class="tm-save" aria-pressed="false">'
               '<span class="tm-save-ic" aria-hidden="true">\u25c7</span>'
               '<span class="tm-save-t">Save</span></button>')
    out.append("</div>")
    return "".join(out)


def _tool_row(t, up: str, tool_prefix: str) -> str:
    slug, name, dek, guide = t[0], t[1], t[2], (t[3] if len(t) > 3 else "")
    out = ['<div class="tm-tool" data-tool><a href="' + esc(U(tool_prefix + "/" + slug + "/", up)) + '"><b>'
           + esc(name) + "</b><small>" + esc(dek[:88]) + ("\u2026" if len(dek) > 88 else "") + "</small></a>"]
    if guide:
        out.append('<a class="tm-tool-g" href="' + esc(U("/" + guide + "/", up)) + '">the guide</a>')
    out.append("</div>")
    return "".join(out)


def _gauge(value: str, label: str, sub: str) -> str:
    return ('<div class="tm-gauge"><b>' + esc(value) + "</b><span>" + esc(label)
            + "</span><small>" + esc(sub) + "</small></div>")


def stats_for(arts: list, cat: dict, need_keys: list, cadence: dict) -> dict:
    by_cat: dict = {}
    for a in arts:
        by_cat.setdefault(a["cat"], []).append(a)
    for lst in by_cat.values():
        lst.sort(key=lambda x: (x.get("upd") or x.get("pub") or "", x["title"]), reverse=True)
    dates = sorted({(a.get("upd") or a.get("pub") or "") for a in arts} - {""})
    newest = dates[-1] if dates else ""
    need_rows: dict = {k: [] for k in need_keys}
    for a in arts:
        need_rows[needs_for(a, need_keys)[0]].append(a)
    return {
        "by_cat": by_cat,
        "need_rows": need_rows,
        "n_pieces": len(arts),
        "n_sections": len(cat),
        "n_cmp": sum(1 for a in arts if _RE_COMPARE.search(a["slug"])),
        "n_prog": sum(1 for a in arts if a.get("kind") == "programme"),
        "newest": newest,
        "n_older": sum(1 for a in arts if (a.get("upd") or a.get("pub") or "") != newest),
        "thin": sorted((len(v), k) for k, v in by_cat.items() if len(v) < 10),
        "fresh": _freshness(arts, cadence),
    }


def _freshness(arts: list, cadence: dict) -> dict:
    import datetime
    now = now_iso()
    overdue = soon = undated = 0
    due = []
    for a in arts:
        d = a.get("upd") or a.get("pub") or ""
        days = cadence.get(a["cat"], 180)
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


def render(arts: list, tools: list, cat: dict, cfg: dict,
           url_prefix: str = "", stamp: str = "") -> str:
    """The hub ``<main>`` body for any desk. ``cfg`` keys: brand, h1, dek,
    needs [(key,label,blurb)], cadence, kind_badges, chips_extra, css, desk,
    tool_prefix, gauges [(value,label,sub)] (values may be callables of stats),
    rules [li,...], rules_links [(slug,label)], clusters [(route,title,dek)],
    palette_label, palette_placeholder, toolbox_blurb."""
    up = (url_prefix or "").rstrip("/")
    need_keys = [nk[0] for nk in cfg["needs"]]
    kind_badges = cfg.get("kind_badges", {})
    st = stats_for(arts, cat, need_keys, cfg.get("cadence", {}))
    by_cat = st["by_cat"]
    need_rows = st["need_rows"]
    n = st["n_pieces"]

    gauges = "".join(
        _gauge(str(v(st) if callable(v) else v), lbl, sub)
        for v, lbl, sub in cfg["gauges"](st, tools))

    need_tiles = ""
    for i, (key, label, blurb) in enumerate(cfg["needs"], start=1):
        need_tiles += ('<button type="button" class="tm-need" data-need="' + key
                       + '" aria-pressed="false"><span class="tm-need-k" aria-hidden="true">' + str(i)
                       + "</span><b>" + esc(label) + '</b><em class="tm-need-n">'
                       + str(len(need_rows[key])) + ' pieces</em><small>' + esc(blurb) + "</small></button>")

    shelves = ""
    for key, label, blurb in cfg["needs"]:
        lst = sorted(need_rows[key], key=lambda x: (x.get("upd") or "", x["title"]), reverse=True)
        if not lst:
            continue
        rows = "".join(_row(a, up, kind_badges, need_keys) for a in lst)
        shelves += ('<section class="tm-shelf" data-shelf="' + key + '"><h3 class="tm-shelf-h"><span>'
                    + esc(label) + "</span><em>" + str(len(lst)) + '</em></h3><p class="tm-shelf-d">'
                    + esc(blurb) + '</p><div class="tm-rows">' + rows
                    + '</div><button type="button" class="tm-more" data-more hidden>'
                    "Show every piece in this shelf</button></section>")

    sec_cards = ""
    for cslug, cvals in cat.items():
        cname, cdesc = cvals[0], cvals[1]
        href = esc(U("/" + cslug + "/", up))
        desc = cdesc[:112] + ("\u2026" if len(cdesc) > 112 else "")
        sec_cards += ('<a class="tm-sec-card" href="' + href + '"><b>' + esc(cname) + "</b><em>"
                      + str(len(by_cat.get(cslug, []))) + "</em><small>" + esc(desc) + "</small></a>")

    tool_prefix = cfg.get("tool_prefix", "/tool")
    tools_html = "".join(_tool_row(t, up, tool_prefix) for t in tools)

    comp = [a for a in arts if _RE_COMPARE.search(a["slug"])]
    wall_subs = sorted({a["cat"] for a in comp}, key=lambda k: (-sum(1 for x in comp if x["cat"] == k), k))
    wall_chips = "".join(
        '<button type="button" class="tm-wallchip" data-wallsub="' + esc(k) + '" aria-pressed="false">'
        + esc(cat.get(k, (k,))[0].split(",")[0].split(" &")[0]) + " <em>" + str(sum(1 for x in comp if x["cat"] == k)) + "</em></button>"
        for k in wall_subs)
    wall_cards = "".join(
        '<a class="tm-wall-card" data-wallsub="' + esc(a["cat"]) + '" href="' + esc(U("/" + a["slug"] + "/", up)) + '">'
        + "<b>" + esc(a["title"]) + "</b><small>" + esc((a.get("excerpt") or "")[:90])
        + ("\u2026" if len(a.get("excerpt") or "") > 90 else "") + "</small></a>"
        for a in sorted(comp, key=lambda x: x["cat"]))
    if comp:
        wall = ('<section class="tm-band tm-band-alt" id="tm-wall"><header class="tm-band-h">'
                "<h2>" + esc(cfg.get("wall_h", "The comparison wall.")) + "</h2><p>"
                + esc(cfg.get("wall_p", str(len(comp)) + " side-by-side pieces on this desk, grouped "
                        "by subject. Every card names its trade-off; pick a subject to narrow the wall."))
                + "</p></header>"
                '<div class="tm-chips" role="group" aria-label="Filter comparisons by subject">' + wall_chips + "</div>"
                '<div class="tm-wall" data-tm-wall>' + wall_cards + "</div></section>")
    else:
        wall = ""

    if cfg.get("hide_thin"):
        thin_html = ""
    elif st["thin"]:
        thin_items = "".join(
            '<li><a href="' + esc(U("/" + k + "/", up)) + '">' + esc(cat[k][0]) + "</a> <span>"
            + str(cnt) + " pieces</span></li>" for cnt, k in st["thin"])
        thin_html = ('<div class="tm-readout tm-readout-warn"><p class="tm-ro-h">Self-read: thin shelves</p>'
                     '<ul class="tm-ro-list">' + thin_items + '</ul><p class="tm-ro-f">Under ten pieces is a'
                     " stack of notes, not a shelf. These are what this desk builds next, in order. If one of"
                     ' them is your problem, <a href="' + esc(U("/" + cfg.get("contact_slug", "contact") + "/", up)) + '">say so</a> \u2014 reader'
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
               + '. ' + esc(cfg.get("cadence_blurb", "Shelves carry their own review cadence; the fastest-turning subjects are checked first. "))
               + 'Next review on the calendar: <time datetime="' + esc(fr["next"]) + '">' + esc(fr["next"]) + '</time>.</p></div>')

    freshness = ('<div class="tm-readout"><p class="tm-ro-h">Verification sweep</p><p class="tm-ro-big">'
                 + ('<time datetime="' + esc(st["newest"]) + '">' + esc(st["newest"]) + "</time>" if st["newest"]
                    else "<time>\u2014</time>")
                 + '<span>newest date the desk carries</span></p><p class="tm-ro-f">'
                 + str(st["n_older"]) + " of " + str(n) + " pieces carry a date older than that sweep. "
                 "Each page prints its own date, and a page never prints a date it cannot show."
                 + (" Stamp: " + esc(stamp) if stamp else "") + "</p></div>")

    rules = ('<div class="tm-readout"><p class="tm-ro-h">Standing rules</p><ul class="tm-ro-list">'
             + "".join("<li>" + li + "</li>" for li in cfg["rules"])
             + '</ul><p class="tm-ro-f">'
             + " \u00b7 ".join('<a href="' + esc(U("/" + r + "/", up)) + '">' + lbl + "</a>"
                              for r, lbl in cfg["rules_links"])
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

    toolbox_href = esc(U(cfg.get("toolbox_href", "/tool/"), up))
    count_href = "#tm-core"

    clusters = cfg.get("clusters", [])
    if clusters:
        _cluster_cards = "".join(
            '<a class="tm-sec-card" href="' + esc(U(r, up)) + '"><b>' + esc(t) + "</b><small>" + esc(d) + "</small></a>"
            for r, t, d in clusters)
        cluster_band = ('<section class="tm-band" id="tm-clusters"><header class="tm-band-h">'
            "<h2>" + esc(cfg.get("clusters_h", "Dive into a cluster.")) + "</h2>"
            "<p>" + esc(cfg.get("clusters_p", "")) + "</p></header>"
            '<div class="tm-secs">' + _cluster_cards + "</div></section>")
    else:
        cluster_band = ""

    chips = "".join('<button type="button" class="tm-chip" data-need="' + k + '" aria-pressed="false">'
                    + lbl + "</button>" for k, lbl in cfg.get("chips", []))
    kind_chips = "".join('<button type="button" class="tm-chip" data-kind="' + kid + '" aria-pressed="false">'
                         + lbl + "</button>" for kid, lbl in cfg.get("kind_chips", []))

    desk_attr = ' data-tm-desk="' + esc(cfg.get("desk", "")) + '"' if cfg.get("desk") else ""

    return "".join([
        '<main id="main" class="tm-machine"' + desk_attr + '><div class="wrap">',

        '<section class="tm-boot" id="tm-boot">',
        '<p class="tm-eyebrow"><span class="tm-led" aria-hidden="true"></span>'
        + esc(cfg["brand"]) + ' <span class="tm-dot" aria-hidden="true">\u00b7</span> ' + esc(cfg.get("eyebrow", "THE LIVING DESK"))
        + '<span class="tm-eyebrow-r">' + esc("swept " + st["newest"] if st["newest"] else "") + "</span></p>",
        '<h1 class="tm-h1">' + esc(cfg["h1"]) + "</h1>",
        '<p class="tm-dek">' + cfg["dek"] + "</p>",
        '<div class="tm-boot-bar"><a class="btn" href="' + count_href + '">'
        + esc(cfg.get("boot_btn", "Read every one of the " + str(n) + " pieces")) + "</a>"
        '<button type="button" class="tm-pal-open" data-tm-open-palette><span>Find a piece</span>'
        '<kbd aria-hidden="true">Ctrl</kbd><kbd aria-hidden="true">K</kbd></button>'
        + ('<a class="btn secondary" href="' + toolbox_href + '">Open the toolbox</a>' if tools else "")
        + "</div>",
        '<div class="tm-gauges">' + gauges + "</div>",
        memory,
        "</section>",

        cluster_band,

        '<section class="tm-band" id="tm-needs"><header class="tm-band-h">'
        "<h2>" + esc(cfg.get("needs_h", "What brought you to the desk?")) + "</h2>"
        "<p>" + (cfg.get("needs_p") if cfg.get("needs_p") is not None else
                 str(len(cfg["needs"])) + " jobs. Pick one and the index below re-sorts itself to that job. Keys "
                 "<kbd>1</kbd>\u2013<kbd>" + str(len(cfg["needs"])) + "</kbd>.") + "</p></header>"
        '<div class="tm-needs">' + need_tiles + "</div></section>",

        '<section class="tm-band" id="tm-core"><header class="tm-band-h">'
        "<h2>" + esc(cfg.get("core_h", "The whole desk, open.")) + "</h2>"
        "<p>" + cfg.get("core_p", "Every published piece on this desk is listed here, in the page itself \u2014 no &ldquo;load "
        "more&rdquo; wall standing between you and the answer. The shelves are grouped by what each piece is "
        "for; the section pages below are the formal index.") + "</p></header>",
        '<div class="tm-toolbar"><div class="tm-search">'
        '<label class="sr-only" for="tm-q">Filter the desk by words in the title or summary</label>'
        '<input id="tm-q" type="search" data-tm-filter="text" autocomplete="off" spellcheck="false" '
        'placeholder="' + esc(cfg.get("filter_placeholder", "filter\u2026")) + '">'
        '<span class="tm-count" data-tm-count aria-live="polite">' + str(n) + " of " + str(n)
        + ' shown</span></div>',
        '<div class="tm-chips" role="group" aria-label="Filter the desk">'
        + chips + kind_chips
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

        ('<section class="tm-band tm-band-alt" id="tm-toolbox"><header class="tm-band-h">'
         "<h2>" + esc(cfg.get("toolbox_h", "The toolbox.")) + "</h2><p>" + str(len(tools)) + " utilities that run entirely in your browser. No "
         "account, no upload, and nothing you type into one is sent anywhere \u2014 including to us.</p></header>"
         '<div class="tm-tools">' + tools_html + "</div>"
         '<p class="tm-band-f">' + cfg.get("toolbox_blurb", "") + "</p></section>") if tools else "",
        wall,

        '<section class="tm-band" id="tm-sections"><header class="tm-band-h">'
        "<h2>" + esc(cfg.get("sections_h", "Sections, in their own words.")) + "</h2><p>"
        + cfg.get("sections_p", "The formal shelves. Same pieces, arranged by subject "
        "instead of by need.") + "</p></header>"
        '<div class="tm-secs">' + sec_cards + "</div></section>",

        '<section class="tm-band tm-band-alt" id="tm-standards"><header class="tm-band-h">'
        "<h2>" + esc(cfg.get("standards_h", "Read the machine before you trust it.")) + "</h2><p>"
        + cfg.get("standards_p", "What this desk will and will not tell you, and "
        "where it currently falls short.") + "</p></header>"
        '<div class="tm-reads">' + cadence + freshness + thin_html + rules + "</div></section>",

        '<p class="tm-noscript">This hub works without JavaScript \u2014 every piece is linked above. With '
        "JavaScript you also get instant filtering, a keyboard palette, saved-for-later and \u201cnew since "
        "your last visit\u201d, all stored on your device.</p>",
        '<div class="tm-palette" data-tm-palette hidden role="dialog" aria-modal="true" '
        'aria-label="' + esc(cfg.get("palette_label", "Search the desk")) + '"><div class="tm-pal-in">'
        '<label class="sr-only" for="tm-pal-q">Search every piece on this desk</label>'
        '<input id="tm-pal-q" type="search" autocomplete="off" spellcheck="false" '
        'placeholder="' + esc(cfg.get("palette_placeholder", "a question \u2014 matches titles and summaries on your device")) + '">'
        "</div>"
        '<ul class="tm-pal-list" data-tm-pal role="listbox" aria-label="Matches"></ul>'
        '<p class="tm-pal-foot">\u2191\u2193 move \u00b7 Enter open \u00b7 Esc close \u00b7 ' + str(n)
        + " pieces indexed \u00b7 typo-tolerant</p></div>",
        "</div></main>",
        '<link rel="stylesheet" href="' + esc(cfg.get("css", "/assets/tech-hub.css")) + '">',
    ])
