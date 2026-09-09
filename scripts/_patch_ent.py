"""Phase 2 patch: rebuild entertainment_pages() into a sectioned publication."""
import ast
from pathlib import Path

p = Path("scripts/build-ecosystem.py")
t = p.read_text()

# ---- 1. save the moved streaming body into the recovery store ----
import re as _re
import html as _html
raw = Path("/tmp/streaming.html").read_text()
m = _re.search(r'<article class="prose article-body">([\s\S]*?)</article>', raw)
assert m, "streaming body not found"
body = m.group(1)
# dead link to an old sports route -> point at the live sports desk
body = body.replace('<a href="/sports/articles/where-to-watch-premier-league-in-nigeria/">', '<a href="/sports/">')
lead = _re.search(r'<p class="lead">([\s\S]*?)</p>', raw).group(1)
store = Path("ecosystem/entertainment/_recovered/best-streaming-apps-nigeria.html")
store.write_text('<p class="intro">' + lead + "</p>" + body, encoding="utf-8")
print("streaming body stored")

# ---- 2. replace entertainment_pages wholesale ----
i = t.index("def entertainment_pages")
j = t.index("\n# ------------------------------------------------------------- 3. SPORTS")
new_fn = '''ENT_SECTIONS = {
    "recommendations": ("What to watch next", "Recommendations, starter routes and watch orders \\u2014 the answer to \\u201cwhat should I watch tonight?\\u201d, argued honestly rather than scraped."),
    "explainers": ("Explainers & comparisons", "Why a show became a phenomenon, what a character\\u2019s choice really meant, and the head-to-heads fans actually argue about."),
    "opinion": ("Opinion & lists", "Reviews with a spine, cult favourites defended, and lists with a reason behind every entry \\u2014 labelled as opinion, written as argument."),
}
ENT_SLUG_SECT = {
    "10-anime-like-solo-leveling-you-should-watch": "recommendations",
    "10-shows-like-alice-in-borderland-you-should-watch-next": "recommendations",
    "movies-like-deadpool-and-wolverine": "recommendations",
    "movies-like-interstellar-guide": "recommendations",
    "movies-like-parasite": "recommendations",
    "christopher-nolan-movies-order": "recommendations",
    "korean-cinema-starter-guide-rebuilt": "recommendations",
    "indian-cinema-first-five": "recommendations",
    "modern-horror-starter-route": "recommendations",
    "nigerian-thrillers-worth-your-time": "recommendations",
    "how-to-pick-a-movie-tonight": "recommendations",
    "best-streaming-apps-nigeria": "recommendations",
    "squid-game-season-1-why-it-became-a-global-phenomenon": "explainers",
    "was-eren-yeager-really-the-villain": "explainers",
    "solo-leveling-e-rank-to-s-rank": "explainers",
    "alice-in-borderland-vs-squid-game": "explainers",
    "one-piece-vs-naruto": "explainers",
    "solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences": "explainers",
    "breaking-bad-two-seasons-opinion": "opinion",
    "5-movies-that-broke-the-internet": "opinion",
    "7-movies-we-wished-never-ended": "opinion",
    "into-the-badlands-was-underrated": "opinion",
    "why-prison-break-season-1-is-still-one-of-the-best-tv-seasons": "opinion",
}
# consolidation: the second slug is folded into the first as a labelled companion piece
ENT_MERGE = {
    "solo-leveling-e-rank-to-s-rank": "solo-leveling-from-e-rank-hunter-to-one-of-animes-most-powerful-characters",
    "why-prison-break-season-1-is-still-one-of-the-best-tv-seasons": "prison-break-season-1-watching-all-night",
}
ENT_START = ["how-to-pick-a-movie-tonight", "christopher-nolan-movies-order",
             "best-streaming-apps-nigeria", "korean-cinema-starter-guide-rebuilt"]

def _first_line(body_html, fallback=""):
    m = re.search(r"<p[^>]*>([\\s\\S]*?)</p>", body_html)
    if not m:
        return fallback
    txt = _strip_tags(m.group(1))
    txt = html.unescape(re.sub(r"\\s+", " ", txt)).strip()
    return (txt[:157] + "\\u2026") if len(txt) > 160 else txt

def _strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)

def entertainment_pages():
    rec = OUT / "entertainment" / "_recovered"
    manifest = json.loads((rec / "manifest.json").read_text())
    by_slug = {m["slug"]: m for m in manifest}
    # the moved piece joins the manifest with its own record
    by_slug["best-streaming-apps-nigeria"] = {
        "slug": "best-streaming-apps-nigeria",
        "title": "Best Streaming Apps in Nigeria (2026), Honestly Compared",
        "words": 900, "moved": True}
    shelf = sorted(ENT_SLUG_SECT)
    merged_away = set(ENT_MERGE.values())
    bodies = {}
    for slug in shelf:
        raw = (rec / f"{slug}.html").read_text()
        bodies[slug] = clean_recovered(raw)
    arts = {}
    for slug in shelf:
        if slug in merged_away:
            continue
        m = by_slug[slug]
        sect = ENT_SLUG_SECT[slug]
        moved = m.get("moved")
        kick = ("Moved from the BRYME tech desk \\u00b7 " if moved else "Archive edition (2025) \\u00b7 ")
        comp_html = ""
        if slug in ENT_MERGE:
            other = ENT_MERGE[slug]
            comp_html = ('<h2>Companion piece, restored: ' + html.escape(by_slug[other]["title"]) + "</h2>"
                         + "<p><em>Merged from the archive so the whole argument lives on one page.</em></p>"
                         + bodies[other])
        summ = _first_line(bodies[slug])
        rel_pool = [s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == sect and s2 != slug]
        rel = rel_pool[:3]
        while len(rel) < 3:
            for s2 in shelf:
                if s2 not in merged_away and s2 != slug and s2 not in rel:
                    rel.append(s2)
                    break
            if len(rel) >= 3:
                break
        rel_html = "".join('<li><a href="/' + s2 + '/">' + html.escape(by_slug[s2]["title"]) + "</a></li>" for s2 in rel)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": m["title"],
                  "author": {"@type": "Organization", "name": "BRYME Entertainment desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/entertainment/" + slug + "/",
                  "description": summ}
        import json as _j
        byline = ("Recovered from the archive \\u00b7 " + str(m["words"]) + " words \\u00b7 re-typeset and reviewed "
                  + TODAY + (" \\u00b7 prices in older pieces change \\u2014 confirm with the service" if slug == "best-streaming-apps-nigeria" else ""))
        abody = (head("entertainment", "Cinema, TV and anime \\u2014 written about, never pirated.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/entertainment/">Entertainment</a> / <a href="/entertainment/' + sect + '/">'
            + html.escape(ENT_SECTIONS[sect][0]) + "</a> / " + html.escape(m["title"]) + "</nav>"
            + '<section class="cover"><p class="kicker">' + kick + "no piracy, no scrapes \\u2014 written about the work</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(m["title"]) + "</h1>"
            + '<p class="byline">BRYME Entertainment desk \\u00b7 ' + html.escape(byline) + "</p></section>"
            + ('<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(summ) + "</p></div></section>" if summ else "")
            + '<section class="section"><div class="prose">' + bodies[slug] + comp_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from ' + html.escape(ENT_SECTIONS[sect][0]) + '.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/entertainment/' + sect + '/">All of ' + html.escape(ENT_SECTIONS[sect][0]) + '</a>'
            + '<a class="btn secondary" href="/entertainment/">All of BRYME Entertainment</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("entertainment"))
        arts[slug] = (("/" + slug + "/"), m["title"] + " | BRYME Entertainment", summ or "From the BRYME archive \\u2014 re-typeset and honestly labelled.", abody)

    sect_pages = {}
    for cslug, (cname, cdesc) in ENT_SECTIONS.items():
        lst = [s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == cslug]
        lst.sort(key=lambda s2: -by_slug[s2]["words"])
        rows = "".join(
            '<li><a href="/' + s2 + '/"><span><b>' + html.escape(by_slug[s2]["title"]) + "</b><small>"
            + html.escape(_first_line(bodies[s2])[:110]) + "\\u2026</small></span>"
            '<span class="meta">' + str(by_slug[s2]["words"]) + " words</span></a></li>" for s2 in lst)
        others = "".join('<a class="btn secondary" href="/entertainment/' + c2 + '/">' + html.escape(ENT_SECTIONS[c2][0]) + "</a>"
                         for c2 in ENT_SECTIONS if c2 != cslug)
        cbody = (head("entertainment", "Cinema, TV and anime \\u2014 written about, never pirated.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/entertainment/">Entertainment</a> / ' + html.escape(cname) + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Entertainment \\u00b7 section</p>'
            + '<h1 class="cover-title">' + html.escape(cname) + "</h1>"
            + '<p class="cover-dek">' + html.escape(cdesc) + "</p></section>"
            + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(lst)) + ' pieces</p><h2>Everything in ' + html.escape(cname) + '.</h2></div>'
            + '<ul class="list">' + rows + "</ul></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Keep watching</p><h2>Elsewhere on this desk.</h2></div>'
            + '<div class="actions">' + others + "</div></section></div></main>" + foot("entertainment"))
        sect_pages[cslug] = [("/" + cslug + "/", cname + " | BRYME Entertainment", cdesc, cbody)]

    start_rows = "".join(
        '<li><a href="/' + s2 + '/"><span><b>' + html.escape(by_slug[s2]["title"]) + "</b><small>"
        + html.escape(_first_line(bodies[s2])[:110]) + "\\u2026</small></span><span class=\\"meta\\">Start here</span></a></li>"
        for s2 in ENT_START)
    cat_cards = "".join(
        '<article class="pub-card live" style="--pc:#6d1832"><p class="pc-kicker">' + str(len([s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == c])) + ' PIECES</p>'
        + "<h3>" + html.escape(ENT_SECTIONS[c][0]) + "</h3><p>" + html.escape(ENT_SECTIONS[c][1][:130]) + "\\u2026</p>"
        + '<a class="btn" href="/entertainment/' + c + '/">Browse ' + html.escape(ENT_SECTIONS[c][0]) + " \\u2192</a></article>"
        for c in ENT_SECTIONS)
    retired_rows = "".join(
        '<li><span><b>' + html.escape(m["title"]) + "</b><small>" + str(m["words"]) + " words \\u00b7 reviewed by the audit \\u2014 retired on merit</small></span>"
        '<span class="meta">Retired</span></li>'
        for m in manifest if m["slug"] not in ENT_SLUG_SECT and m["slug"] not in set(ENT_MERGE.values())
        and m["slug"] not in {"korean-cinema-starter-guide", "movies-like-interstellar"})
    index_body = (head("entertainment", "Cinema, TV and anime \\u2014 written about, never pirated.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Entertainment</p>'
        + '<h1 class="cover-title">What should I watch \\u2014 and why?</h1>'
        + '<p class="cover-dek">Recommendations with reasons, explainers without spoilers-for-sport, and opinion labelled as opinion. Everything here is written about the work: no download pages, no fake play buttons, no piracy \\u2014 ever.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Handpicked</p><h2>Start here.</h2></div>'
        + '<ul class="list">' + start_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Browse by need</p><h2>Sections of this desk.</h2></div>'
        + '<div class="cards">' + cat_cards + "</div></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The house rule</p><h2>Written about the work, never trafficking in it.</h2></div>'
        + '<p class="lede">BRYME Entertainment does not stream, host, link or hint at pirated copies. External trailers may support a piece; the value on the page is the argument. Restored editions say so plainly, carry their word counts, and were re-typeset \\u2014 not quietly re-scraped.</p>'
        + '<ul class="list" style="margin-top:14px">' + retired_rows + "</ul>"
        + "</section></div></main>" + foot("entertainment"))
    pages = [("/", "BRYME Entertainment \\u2014 what to watch, and why",
              "Film, TV and anime recommendations with reasons, explainers and opinion \\u2014 written about the work, never piracy.", index_body)]
    for pl in sect_pages.values():
        pages.extend(pl)
    pages.extend(arts[s] for s in shelf if s not in merged_away)
    return pages + legal_pages("entertainment", "BRYME Entertainment", "Writing about film, TV and anime for people who love the work.")


'''
t = t[:i] + new_fn + t[j:]
ast.parse(t)
p.write_text(t)
print("entertainment_pages rebuilt")
