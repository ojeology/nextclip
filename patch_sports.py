import ast

p = "scripts/build-ecosystem.py"
src = open(p).read()

# 1. define SPO_SWEEP next to the other sweep stamps
anchor = 'ENT_SWEEP = "2026-09-25"  # entertainment desk freshness sweep date'
assert anchor in src
src = src.replace(anchor, anchor + '\nSPO_SWEEP = "2026-09-25"  # sport desk freshness sweep date', 1)

# 2. region-scoped freshness sweep (sports_pages only)
i0 = src.find("def sports_pages()")
i1 = src.find("def money_pages()")
assert 0 < i0 < i1
seg = src[i0:i1]
n = 0
for old, new, cnt in [
    ('\u00b7 {TODAY}</small>', '\u00b7 {SPO_SWEEP}</small>', 1),
    ("re-typeset {TODAY}", "re-typeset {SPO_SWEEP}", 1),
    ('"datePublished": TODAY, "dateModified": TODAY,', '"datePublished": TODAY, "dateModified": SPO_SWEEP,', 2),
    ("reviewed ' + TODAY + \" \\u00b7 evergreen", "reviewed ' + SPO_SWEEP + \" \\u00b7 evergreen", 2),
]:
    assert seg.count(old) == cnt, (old, seg.count(old))
    seg = seg.replace(old, new)
    n += cnt
print("freshness sites swept:", n)

# 3. wiring: machine hub + /season/ shelf, right after the existing pages.insert(0, ...)
marker = '''    pages.insert(0, ("/", "BRYME Sport \\u2014 football reporting, never betting",
              "Matchweek guides, season stories and the August deadline-day archive from the BRYME media desk. Independent, checkable, strictly no gambling content.", index_body))'''
assert marker in seg
wire = marker + '''
    # Living-machine hub (tech-standard display): the editorial desk becomes
    # ground zero. League data pages, club pages and shelf hubs stay exactly
    # where they are and become cluster cards; the wall carries the 41
    # editorial pieces only. One new section shelf is added: /season/.
    import desk_hub_render
    import sports_hub_data as _shd
    import sports_explainers_data as _sed
    import sports_analysis_data as _sad
    _expl_slugs = {t[0] for t in _sed.SPORT_EXPLAINERS}
    _anal_slugs = {t[0] for t in _sad.SPORT_ANALYSIS}
    _bigq_slugs = set(_shd.SPO_BIGQ)
    _cat_arts = []
    for (_r, _t, _d, _b) in pages:
        _s = _r.strip("/").split("/")[-1]
        if (_r == "/" or _r.startswith("/clubs/") or _s in _shd.SPO_SKIP_SLUGS
                or _s.endswith(_shd.SPO_SKIP_SUFFIX)):
            continue
        if _s in _expl_slugs:
            _cn, _nd, _kd = "explainers", "learn", "guide"
        elif _s in _anal_slugs:
            _cn, _nd, _kd = "analysis", "read", "analysis"
        elif _s in _bigq_slugs:
            _cn, _nd, _kd = "season", "follow", "tracker"
        elif _s in _shd.SPO_REAL_ARCHIVE:
            _cn, _nd, _kd = "season", "follow", "archive"
        elif _s in _shd.SPO_REAL_LIVE:
            _cn, _nd, _kd = "season", "follow", "feature"
        elif _s in _shd.SPO_WEEKEND:
            _cn, _nd, _kd = "season", "weekend", _shd.SPO_WEEKEND[_s]
        else:
            raise AssertionError("sports page without taxonomy entry: " + _s)
        _cat_arts.append({"slug": _s, "title": _t.split(" | ")[0], "excerpt": _d,
                          "cat": _cn, "need": _nd, "pub": TODAY, "upd": SPO_SWEEP,
                          "kind": _kd})
    _spo_cfg = {
        "brand": "BRYME SPORT",
        "h1": "Sport as reporting, not noise.",
        "dek": ('You have a question about the game: what the rule means, why the tactic works, '
                'who wins the league, what is on this weekend. This desk answers it with reporting, '
                'dated honestly and arranged below by what you came here to <em>do</em> \\u2014 and it '
                'never sells you a bet.'),
        "needs": _shd.SPO_NEEDS,
        "cadence": _shd.SPO_CADENCE,
        "cadence_blurb": "The season desk turns weekly (30 days \\u2014 matchweeks and windows move); the laws of the game can wait (365). ",
        "kind_badges": {"archive": "Archive edition", "tracker": "Living tracker",
                        "analysis": "Analysis", "feature": "Desk feature"},
        "chips": [("weekend", "This weekend"), ("learn", "Learn the laws"),
                  ("read", "Read the game"), ("follow", "Follow the season")],
        "kind_chips": [("archive", "Archive editions"), ("tracker", "Living trackers")],
        "gauges": lambda st, tools: [
            (st["n_pieces"], "pieces on the desk", "explainers, analysis, season desk"),
            ("6", "leagues covered", "table, fixtures, results, scorers"),
            ("20", "club pages", "Premier League 2026-27"),
            (str(len(_expl_slugs) + len(_anal_slugs)), "evergreen pieces", "laws, formats, tactics"),
            (str(sum(1 for a in _cat_arts if a["kind"] == "archive")), "archive editions", "kept dated, never re-badged"),
        ],
        "rules": [
            "No betting content, no odds, no tips \\u2014 the house rule, on every page of this desk.",
            "Fixture and table data is fetched on schedule and stamped with when it last moved.",
            "Dated editions stay dated: a matchweek preview is labelled archive the moment it passes.",
            "Transfer news runs only when it is sourced; rumours are labelled as rumours.",
            "Corrections land on the page that was wrong, and are listed.",
        ],
        "rules_links": [("about", "About the desk"), ("editorial-policy", "Editorial policy"),
                        ("corrections", "Corrections"), ("contact", "Contact"), ("privacy", "Privacy")],
        "clusters": _shd.SPO_CLUSTERS,
        "clusters_h": "The live surfaces.",
        "clusters_p": "Tables, fixtures, results, scorers, clubs and the transfer desk \\u2014 fetched on schedule, stamped with when they last moved.",
        "palette_label": "Search the sport desk",
        "palette_placeholder": "offside, VAR, transfers, FPL \\u2014 matches titles and summaries on your device",
        "filter_placeholder": "filter: offside, transfers, xG\\u2026",
        "toolbox_href": "",
        "contact_slug": "contact",
        "desk": "sports",
        "css": "/assets/tech-hub.css",
        "tool_prefix": "",
    }
    _spo_hub = (head("sports", "Analysis, stories and the long view \\u2014 never betting.")
        + desk_hub_render.render(_cat_arts, [], _shd.SPO_CATS, _spo_cfg, "", TODAY)
        + '<script src="/assets/tech-hub.js" defer></script>'
        + foot("sports"))
    pages[0] = ("/", "BRYME Sport \\u2014 football reporting, never betting",
                "Matchweek guides, season stories and the August deadline-day archive from the BRYME media desk. Independent, checkable, strictly no gambling content.",
                _spo_hub)
    _sn, _sd = _shd.SPO_CATS["season"]
    _rows = sorted((a for a in _cat_arts if a["cat"] == "season"), key=lambda a: a["title"])
    _lis = "".join('<li><a href="/sports/' + a["slug"] + '/"><span><b>' + html.escape(a["title"])
                   + "</b><small>" + html.escape((a["excerpt"] or "")[:110]) + "</small></span></a></li>"
                   for a in _rows)
    _sec_body = (head("sports", _sn + " \\u2014 BRYME Sport")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb" style="padding-top:22px"><a href="/sports/">Sport</a> / ' + html.escape(_sn) + "</nav>"
        + '<section class="cover"><p class="kicker">Section shelf \\u00b7 ' + str(len(_rows)) + " pieces</p>"
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(_sn) + "</h1>"
        + '<p class="lede">' + html.escape(_sd) + "</p></section>"
        + '<section class="section"><ul class="list">' + _lis + "</ul>"
        + '<div class="actions"><a class="btn secondary" href="/sports/">The whole desk</a></div></section>'
        + "</div></main>" + foot("sports"))
    pages.append(("/season/", _sn + " | BRYME Sport", _sd[:155], _sec_body))'''
seg = seg.replace(marker, wire, 1)
src = src[:i0] + seg + src[i1:]
open(p, "w").write(src)
ast.parse(src)
print("wired + AST OK")
