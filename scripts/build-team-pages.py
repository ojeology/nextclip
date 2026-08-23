#!/usr/bin/env python3
"""BRYME permanent football team pages + Matchweek Chronicles.

ONE template + content/teams.json + fixtures + sourced results = every team page.

Does not invent scores, scorers, plots or official league positions.
Re-run after a sourced result is added:

    python3 scripts/build-team-pages.py
"""
from __future__ import annotations

import html as H
import json
import re
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://bryme.onrender.com"
TODAY = date(2026, 8, 23)

FIXTURE_FILES = {
    "premier-league": "fixtures.json",
    "la-liga": "fixtures-la-liga.json",
    "serie-a": "fixtures-serie-a.json",
    "bundesliga": "fixtures-bundesliga.json",
    "ligue-1": "fixtures-ligue-1.json",
}

LL_CREST = {
    "alaves": "alaves.png",
    "athletic-bilbao": "athletic.png",
    "atletico-madrid": "atletico.png",
    "barcelona": "barcelona.png",
    "celta-vigo": "celta.png",
    "deportivo": "deportivo.png",
    "elche": "elche.png",
    "espanyol": "espanyol.png",
    "getafe": "getafe.png",
    "levante": "levante.png",
    "malaga": "malaga.png",
    "osasuna": "osasuna.png",
    "racing": "racing.png",
    "rayo-vallecano": "rayo.png",
    "real-betis": "betis.png",
    "real-madrid": "real-madrid.png",
    "real-sociedad": "real-sociedad.png",
    "sevilla": "sevilla.png",
    "valencia": "valencia.png",
    "villarreal": "villarreal.png",
}

HEADER = (
    '<header class="top"><div class="shell"><a class="brand" href="/">BRY<b>ME</b></a>'
    '<nav class="topnav"><a href="/">Home</a><a href="/entertainment/">🎬 Entertainment</a>'
    '<a href="/sports/" class="active">⚽ Sports</a><a href="/make-money/">💰 Make Money</a>'
    '<a href="/tech/">🤖 Tech &amp; AI</a><a class="nav-search" href="/search/">Search</a></nav>'
    '<div class="top-tools"><a class="header-search" href="/search/" aria-label="Search">Search</a>'
    "</div></div></header>"
)

FOOTER = """<nav class="mobile-nav"><a href="/"><span class="mn-ico">🏠</span>Home</a><a href="/entertainment/"><span class="mn-ico">🎬</span>Entertain</a><a href="/sports/" class="active"><span class="mn-ico">⚽</span>Sports</a><a href="/make-money/"><span class="mn-ico">💰</span>Money</a><a href="/tech/"><span class="mn-ico">🤖</span>Tech</a><a href="/search/"><span class="mn-ico">🔍</span>Search</a></nav><footer class="footer"><div class="shell"><div class="footer-grid">
  <div class="footer-brand"><a class="brand" href="/">BRY<b>ME</b></a><p>Discover what you love. Learn what you need. Find what's next.</p></div>
  <nav class="footer-col" aria-label="Explore"><h3>Verticals</h3><a href="/entertainment/">🎬 Entertainment</a><a href="/sports/">⚽ Sports</a><a href="/make-money/">💰 Make Money</a><a href="/tech/">🤖 Tech &amp; AI</a></nav>
  <nav class="footer-col" aria-label="Explore"><h3>Entertainment</h3><a href="/trending/">What's Trending</a><a href="/movies/">Movies</a><a href="/series/">Series</a><a href="/anime/">Anime</a><a href="/articles/">Articles</a><a href="/genres/">Genres</a></nav>
  <nav class="footer-col" aria-label="Information"><h3>Information</h3><a href="/about/">About</a><a href="/contact/">Contact</a><a href="/editorial-policy/">Editorial Policy</a></nav>
  <nav class="footer-col" aria-label="Legal"><h3>Legal</h3><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Use</a><a href="/disclaimer/">Disclaimer</a><a href="/copyright/">Copyright / DMCA</a></nav>
</div>
<p class="footer-note">BRYME · Discover what you love. Learn what you need. Find what's next. Trailer links lead to YouTube and viewing links lead to third parties.<small>Trending Now is editorially curated by BRYME — it is not live traffic data. Popular and Editor's Picks are independent rankings. Real user analytics will replace trending once the site has enough traffic. · Team pages 2026-08-23</small></div></footer><script>window.BRYME_BASE=''</script><script src="/assets/site-app.js"></script>"""


def esc(s) -> str:
    return H.escape("" if s is None else str(s), quote=True)


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def crest_for(league: str, team_id: str) -> str:
    if league == "premier-league":
        return f"/assets/img/sports/pl/{team_id}.svg"
    if league == "la-liga":
        fn = LL_CREST.get(team_id, f"{team_id}.png")
        return f"/assets/img/sports/ll/{fn}"
    if league == "serie-a":
        ext = ".png" if team_id == "lazio" else ".svg"
        return f"/assets/img/sports/sa/{team_id}{ext}"
    if league == "ligue-1":
        return f"/assets/img/sports/l1/{team_id}.webp"
    if league == "bundesliga":
        p = ROOT / f"assets/img/sports/bl/{team_id}.svg"
        if p.exists():
            return f"/assets/img/sports/bl/{team_id}.svg"
        alt = ROOT / f"assets/img/sports/club-{team_id}.svg"
        if alt.exists():
            return f"/assets/img/sports/club-{team_id}.svg"
        return f"/assets/img/sports/bl/{team_id}.svg"
    return ""


def parse_date(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def season_date(raw: str | None, mw: int | None) -> date | None:
    """Calendar date for sorting/display. 2026/27 MW19+ rows stored as Jan–May 2026 are 2027."""
    d = parse_date(raw)
    if not d:
        return None
    if d.year == 2026 and d.month <= 6 and (mw or 0) >= 19:
        try:
            return d.replace(year=2027)
        except ValueError:
            return d
    return d


def fmt_date(s: str | None, mw: int | None = None) -> str:
    d = season_date(s, mw) if mw is not None else parse_date(s)
    if not d:
        return "Date TBC"
    return d.strftime("%a %-d %b %Y")


def fmt_time(t) -> str:
    if not t:
        return "TBC"
    return f"{t} UK"


def match_slug(home_id: str, away_id: str) -> str:
    return f"{home_id}-vs-{away_id}"


def match_href(league: str, home_id: str, away_id: str) -> str:
    return f"/sports/{league}/matches/{match_slug(home_id, away_id)}/"


def empty_row() -> dict:
    return {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0, "gd": 0, "pts": 0, "form": []}


def apply_result(table: dict, home: str, away: str, hs: int, as_: int, played: str | None):
    for tid in (home, away):
        table.setdefault(tid, empty_row())
    table[home]["p"] += 1
    table[away]["p"] += 1
    table[home]["gf"] += hs
    table[home]["ga"] += as_
    table[away]["gf"] += as_
    table[away]["ga"] += hs
    table[home]["gd"] = table[home]["gf"] - table[home]["ga"]
    table[away]["gd"] = table[away]["gf"] - table[away]["ga"]
    if hs > as_:
        table[home]["w"] += 1
        table[away]["l"] += 1
        table[home]["pts"] += 3
        table[home]["form"].append("W")
        table[away]["form"].append("L")
    elif hs < as_:
        table[away]["w"] += 1
        table[home]["l"] += 1
        table[away]["pts"] += 3
        table[home]["form"].append("L")
        table[away]["form"].append("W")
    else:
        table[home]["d"] += 1
        table[away]["d"] += 1
        table[home]["pts"] += 1
        table[away]["pts"] += 1
        table[home]["form"].append("D")
        table[away]["form"].append("D")


def standings_for(league: str, fixtures: dict, results: dict) -> tuple[dict, list[str]]:
    table = {}
    names = {}
    for mw in fixtures.get("matchweeks", []):
        for m in mw.get("matches", []):
            table.setdefault(m["id"], empty_row())
            table.setdefault(m["away"], empty_row())
            names[m["id"]] = m.get("homeName") or m["id"]
            names[m["away"]] = m.get("awayName") or names.get(m["away"], m["away"])
    league_results = results.get(league) or {}
    dated = []
    for slug, r in league_results.items():
        if "vs" not in slug:
            continue
        home, away = slug.split("-vs-", 1)
        dated.append((r.get("playedOn") or "", home, away, r))
    dated.sort(key=lambda x: x[0])
    for _, home, away, r in dated:
        apply_result(table, home, away, int(r["homeScore"]), int(r["awayScore"]), r.get("playedOn"))
    ranked = sorted(
        table.keys(),
        key=lambda tid: (-table[tid]["pts"], -table[tid]["gd"], -table[tid]["gf"], names.get(tid, tid)),
    )
    return table, ranked


def collect_team_matches(team_id: str, fixtures: dict, results: dict, league: str) -> list[dict]:
    out = []
    league_results = results.get(league) or {}
    venues = fixtures.get("venues") or {}
    for mw in fixtures.get("matchweeks", []):
        num = mw.get("number")
        for m in mw.get("matches", []):
            if m["id"] != team_id and m["away"] != team_id:
                continue
            slug = match_slug(m["id"], m["away"])
            res = league_results.get(slug)
            home = m["id"] == team_id
            opp_id = m["away"] if home else m["id"]
            opp_name = m["awayName"] if home else m["homeName"]
            row = {
                "mw": num,
                "homeId": m["id"],
                "awayId": m["away"],
                "homeName": m["homeName"],
                "awayName": m["awayName"],
                "date": m.get("date"),
                "time": m.get("time"),
                "timePublished": bool(m.get("timePublished")),
                "tv": m.get("tv") or "",
                "venue": (m.get("venue") or (venues.get(m["id"]) or {}).get("name") or ""),
                "slug": slug,
                "href": match_href(league, m["id"], m["away"]),
                "home": home,
                "oppId": opp_id,
                "oppName": opp_name,
                "result": None,
            }
            if res and "homeScore" in res and "awayScore" in res:
                hs, aws = int(res["homeScore"]), int(res["awayScore"])
                if hs > aws:
                    wdl_home, wdl_away = "W", "L"
                elif hs < aws:
                    wdl_home, wdl_away = "L", "W"
                else:
                    wdl_home = wdl_away = "D"
                row["result"] = {
                    "hs": hs,
                    "as": aws,
                    "status": res.get("status") or "FT",
                    "playedOn": res.get("playedOn") or m.get("date"),
                    "scorers": res.get("scorers") or [],
                    "source": res.get("source") or {},
                    "wdl": wdl_home if home else wdl_away,
                }
            out.append(row)
    # Matchweek order is the season order. Some 2026/27 second-half rows
    # were stored as Jan–May 2026; do not let those jump ahead of August.
    out.sort(key=lambda r: (r["mw"] or 99, r["date"] or "9999", r["time"] or "99:99"))
    return out


def blurb(team: dict) -> str:
    return (
        f"{team['name']} are a {team['leagueName']} club from {team['city']}. "
        f"Founded in {team['founded']}, they play at {team['stadium']}."
    )


def form_html(letters: list[str]) -> str:
    if not letters:
        return '<span class="tp-form-empty">No sourced result yet</span>'
    bits = []
    for ch in letters[-5:]:
        bits.append(f'<span class="tp-pill tp-pill-{ch.lower()}">{esc(ch)}</span>')
    return '<span class="tp-form">' + "".join(bits) + "</span>"


def gd_txt(n: int) -> str:
    if n > 0:
        return f"+{n}"
    return str(n)


def page_head(title: str, desc: str, url: str, extra_ld: list) -> str:
    t, d, u = esc(title), esc(desc), esc(url)
    crumbs = extra_ld
    ld = json.dumps(crumbs, ensure_ascii=False, separators=(",", ":"))
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#08090b"><meta name="color-scheme" content="dark light"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="/assets/favicon.png" type="image/png" sizes="32x32"><link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png"><link rel="manifest" href="/manifest.webmanifest"><title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{u}"><meta property="og:type" content="website"><meta property="og:site_name" content="BRYME"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{u}"><meta property="og:image" content="https://bryme.onrender.com/assets/bryme-card.png"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="BRYME"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="https://bryme.onrender.com/assets/bryme-card.png"><meta name="twitter:image:alt" content="BRYME"><link rel="stylesheet" href="/assets/site.css"><script type="application/ld+json">{ld}</script></head>"""


def fallback_story(team: dict, match: dict, art: dict) -> dict:
    res = match["result"]
    line = f"{match['homeName']} {res['hs']}–{res['as']} {match['awayName']}"
    wdl = res["wdl"]
    mood = "celebrate" if wdl == "W" else ("concede" if wdl == "L" else "kickoff")
    return {
        "teamId": team["id"],
        "matchweek": match["mw"],
        "matchSlug": match["slug"],
        "headline": f"Matchweek {match['mw']} is in the book",
        "resultLine": line,
        "status": "complete",
        "panels": [
            {
                "art": "arrival",
                "title": "Before kickoff",
                "caption": f"{match['homeName']} against {match['awayName']}, matchweek {match['mw']}.",
                "bubble": "Let's get the points and go home.",
            },
            {
                "art": mood,
                "title": "The match",
                "caption": f"Final score {line}. Named scorers are only shown when BRYME has them sourced.",
                "bubble": "That's the number on the board.",
            },
            {
                "art": "table",
                "title": "Full time",
                "caption": f"{res['status']} {line}. Result sits on the team page until the next sourced match.",
                "bubble": "File it. Next week is a different comic.",
            },
        ],
    }


def story_for(team: dict, match: dict, comics: dict) -> dict | None:
    if not match.get("result"):
        return None
    for s in comics.get("stories") or []:
        if s.get("teamId") == team["id"] and s.get("matchSlug") == match["slug"]:
            return s
    return fallback_story(team, match, comics.get("art") or {})


def render_panels(story: dict, art: dict, lazy: bool) -> str:
    loading = "lazy" if lazy else "lazy"
    bits = ['<ol class="mwc-panels">']
    for i, p in enumerate(story.get("panels") or [], 1):
        src = art.get(p.get("art") or "", art.get("kickoff", ""))
        bubble = p.get("bubble") or ""
        bubble_html = (
            f'<p class="mwc-bubble"><span>{esc(bubble)}</span></p>' if bubble else ""
        )
        alt = p.get("title") or f"Matchweek comic panel {i}"
        bits.append(
            f'<li class="mwc-panel">'
            f'<figure><img src="{esc(src)}" alt="{esc(alt)}" width="1200" height="669" loading="{loading}" decoding="async">'
            f'<figcaption><b>Panel {i}: {esc(p.get("title") or "")}</b>'
            f'<span>{esc(p.get("caption") or "")}</span></figcaption></figure>'
            f"{bubble_html}</li>"
        )
    bits.append("</ol>")
    return "".join(bits)


def render_awaiting(art: dict, match: dict | None, mw: int) -> str:
    src = art.get("awaiting", "")
    if match:
        when = f"{fmt_date(match['date'])} · {fmt_time(match['time'])}"
        body = (
            f"<p>Matchweek {mw} has not been locked. "
            f"Next listed fixture: <a href=\"{esc(match['href'])}\">{esc(match['homeName'])} vs {esc(match['awayName'])}</a> "
            f"({esc(when)}). The comic is written after a sourced full-time result, not before.</p>"
        )
    else:
        body = f"<p>Matchweek {mw} has not been played. The chronicle stays empty until a sourced full-time result exists.</p>"
    return (
        f'<div class="mwc-await">'
        f'<img src="{esc(src)}" alt="Empty night pitch, awaiting the next BRYME matchweek comic" width="1200" height="669" loading="lazy" decoding="async">'
        f"<div><p class=\"eyebrow\">Awaiting matchweek {mw}</p>{body}</div></div>"
    )


def render_team_page(team: dict, ctx: dict) -> str:
    matches = ctx["matches"]
    table = ctx["table"]
    ranked = ctx["ranked"]
    comics = ctx["comics"]
    art = comics.get("art") or {}
    by_id = ctx["by_id"]
    league = team["league"]
    stats = table.get(team["id"], empty_row())
    pos = ranked.index(team["id"]) + 1 if team["id"] in ranked else None
    completed = [m for m in matches if m.get("result")]
    upcoming = [m for m in matches if not m.get("result")]
    prev_m = None
    if completed:
        prev_m = max(
            completed,
            key=lambda m: (
                m["result"].get("playedOn") or m.get("date") or "",
                m.get("time") or "",
            ),
        )
    future = [
        m
        for m in upcoming
        if season_date(m.get("date"), m.get("mw"))
        and season_date(m.get("date"), m.get("mw")) >= TODAY
    ]
    next_m = (
        min(
            future,
            key=lambda m: (
                season_date(m.get("date"), m.get("mw")) or date(9999, 1, 1),
                m.get("time") or "",
            ),
        )
        if future
        else (upcoming[0] if upcoming else None)
    )
    upcoming = sorted(
        upcoming,
        key=lambda m: (
            season_date(m.get("date"), m.get("mw")) or date(9999, 1, 1),
            m.get("time") or "",
            m.get("mw") or 99,
        ),
    )

    title = f"{team['name']} Fixtures, Results & Matchweek Stories | BRYME"
    desc = (
        f"{team['name']} fixtures, results, upcoming matches, league position, "
        f"recent form and BRYME matchweek football comics. {team['leagueName']} 2026/27."
    )
    url = f"{SITE}/sports/teams/{team['slug']}/"
    page_ld = [
        {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": title.replace(" | BRYME", ""),
            "description": desc,
            "url": url,
            "isPartOf": {"@type": "WebSite", "name": "BRYME", "url": SITE + "/"},
        },
        {
            "@context": "https://schema.org",
            "@type": "SportsTeam",
            "name": team["name"],
            "sport": "Soccer",
            "url": url,
            "logo": SITE + team["crest"],
            "foundingDate": str(team.get("founded") or ""),
            "location": {"@type": "Place", "name": team.get("city") or ""},
            "memberOf": {
                "@type": "SportsOrganization",
                "name": team["leagueName"],
                "url": f"{SITE}/sports/{league}/",
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "BRYME Sports", "item": SITE + "/sports/"},
                {"@type": "ListItem", "position": 3, "name": "Teams", "item": SITE + "/sports/teams/"},
                {"@type": "ListItem", "position": 4, "name": team["name"], "item": url},
            ],
        },
    ]
    if next_m:
        page_ld.append(
            {
                "@context": "https://schema.org",
                "@type": "SportsEvent",
                "name": f"{next_m['homeName']} v {next_m['awayName']}",
                "sport": "Soccer",
                "startDate": f"{next_m['date']}T{(next_m['time'] or '15:00')}:00",
                "eventStatus": "https://schema.org/EventScheduled",
                "location": {"@type": "Place", "name": next_m.get("venue") or team["stadium"]},
                "homeTeam": {"@type": "SportsTeam", "name": next_m["homeName"]},
                "awayTeam": {"@type": "SportsTeam", "name": next_m["awayName"]},
                "url": SITE + next_m["href"],
            }
        )

    # carousel matchweeks: first 6 involving this team
    mws_seen = []
    mw_first_match = {}
    for m in matches:
        if m["mw"] not in mw_first_match:
            mw_first_match[m["mw"]] = m
            mws_seen.append(m["mw"])
    carousel_mws = mws_seen[:6]
    current_mw = (prev_m or next_m or matches[0])["mw"] if matches else 1

    cards = []
    stories_html = []
    archive = []
    for i, mw in enumerate(carousel_mws):
        mw_matches = [m for m in matches if m["mw"] == mw]
        done = [m for m in mw_matches if m.get("result")]
        story = story_for(team, done[-1], comics) if done else None
        is_cur = mw == current_mw
        state = "complete" if done else "awaiting"
        if done:
            last = done[-1]
            label = last["result"]
            sub = f"{last['homeName']} {label['hs']}–{label['as']} {last['awayName']}"
        elif mw_matches:
            sub = f"{mw_matches[0]['homeName']} vs {mw_matches[0]['awayName']}"
        else:
            sub = "Awaiting"
        cards.append(
            f'<button type="button" class="mwc-card{" is-current" if is_cur else ""}" data-mwc-card="{mw}" aria-pressed="{"true" if is_cur else "false"}">'
            f'<span class="mwc-card-kicker">Matchweek {mw}</span>'
            f'<span class="mwc-card-state mwc-{state}">{ "Complete" if done else "Awaiting" }</span>'
            f'<span class="mwc-card-sub">{esc(sub)}</span></button>'
        )
        if story:
            stories_html.append(
                f'<article class="mwc-story{" is-active" if is_cur else ""}" data-mwc-story="{mw}" id="mw-{mw}">'
                f'<header class="mwc-story-head"><p class="eyebrow">Matchweek {mw} complete</p>'
                f"<h3>{esc(story.get('headline') or f'Matchweek {mw}')}</h3>"
                f'<p class="mwc-resultline">{esc(story.get("resultLine") or sub)}</p>'
                f'<p class="mwc-jump">Match report: <a href="{esc(done[-1]["href"])}">{esc(done[-1]["homeName"])} vs {esc(done[-1]["awayName"])}</a></p></header>'
                f'{render_panels(story, art, lazy=not is_cur)}</article>'
            )
            archive.append(
                f'<li><a href="#mw-{mw}">'
                f"<b>Matchweek {mw}</b><span>{esc(story.get('resultLine') or sub)}</span>"
                f"<em>Read comic</em></a></li>"
            )
        else:
            stories_html.append(
                f'<article class="mwc-story{" is-active" if is_cur else ""}" data-mwc-story="{mw}" id="mw-{mw}">'
                f'<header class="mwc-story-head"><p class="eyebrow">Matchweek {mw}</p>'
                f"<h3>Awaiting matchweek {mw}</h3></header>"
                f'{render_awaiting(art, mw_matches[0] if mw_matches else None, mw)}</article>'
            )
            archive.append(
                f'<li class="is-await"><span><b>Matchweek {mw}</b><span>{esc(sub)}</span></span><em>Awaiting</em></li>'
            )

    # next / prev blocks
    def side_card(kind: str, match: dict | None) -> str:
        if not match:
            return (
                f'<div class="tp-side"><p class="tp-side-k">{kind}</p>'
                f"<p class=\"tp-side-empty\">No sourced {kind.lower()} yet.</p></div>"
            )
        if match.get("result"):
            r = match["result"]
            score = f"{match['homeName']} {r['hs']}–{r['as']} {match['awayName']}"
            meta = f"{fmt_date(r.get('playedOn') or match['date'], match.get('mw'))} · {r['wdl']}"
        else:
            score = f"{match['homeName']} vs {match['awayName']}"
            meta = f"{fmt_date(match['date'], match.get('mw'))} · {fmt_time(match['time'])} · {'Home' if match['home'] else 'Away'}"
        opp_crest = crest_for(league, match["oppId"])
        return (
            f'<a class="tp-side" href="{esc(match["href"])}">'
            f'<p class="tp-side-k">{kind}</p>'
            f'<div class="tp-side-row"><img src="{esc(opp_crest)}" alt="{esc(match["oppName"])} crest" width="36" height="36">'
            f"<div><b>{esc(score)}</b><span>{esc(meta)}</span></div></div></a>"
        )

    pos_txt = str(pos) if pos else "—"
    sourced_n = sum(1 for tid in table if table[tid]["p"] > 0)
    pos_note = (
        f"BRYME table from {sum(s['p'] for s in table.values()) // 2} sourced full-time results "
        f"across {sourced_n} clubs. Sunday 23 August matches stay as previews until a source URL exists. "
        f"This is not an official {team['leagueName']} table."
    )

    # fixtures / results tables
    def rows_for(items: list[dict], kind: str) -> str:
        if not items:
            empty = "No upcoming league fixture in the file." if kind == "up" else "No sourced full-time result yet."
            return f'<p class="tp-empty">{empty}</p>'
        body = []
        for m in items:
            ha = "Home" if m["home"] else "Away"
            status = "Upcoming"
            score = "–"
            wdl = ""
            if m.get("result"):
                r = m["result"]
                status = r["status"]
                score = f"{r['hs']}–{r['as']}"
                wdl = f'<span class="tp-pill tp-pill-{r["wdl"].lower()}">{r["wdl"]}</span>'
            elif m.get("date") and parse_date(m["date"]) == TODAY:
                status = f"Today · {fmt_time(m['time'])}"
            else:
                status = fmt_time(m["time"])
            opp_page = by_id.get(m["oppId"])
            opp_cell = esc(m["oppName"])
            if opp_page:
                label = f"{m['oppName']} fixtures" if kind == "up" else f"{m['oppName']} results"
                opp_cell = f'<a href="/sports/teams/{esc(opp_page["slug"])}/">{esc(label)}</a>'
            body.append(
                f"<tr><td>{esc(fmt_date(m['date'], m.get('mw')))}</td>"
                f"<td>MW {esc(m['mw'])}</td>"
                f"<td>{esc(team['leagueName'])}</td>"
                f"<td>{opp_cell}</td>"
                f"<td>{ha}</td>"
                f"<td>{esc(status)}</td>"
                f"<td><a href=\"{esc(m['href'])}\">{esc(score) if m.get('result') else 'Preview'}</a> {wdl}</td></tr>"
            )
        head = "<thead><tr><th>Date</th><th>MW</th><th>Competition</th><th>Opponent</th><th>H/A</th><th>Status</th><th>Score</th></tr></thead>"
        return f'<div class="sp-table-wrap"><table class="sp-table tp-table">{head}<tbody>{"".join(body)}</tbody></table></div>'

    same_league = [t for t in ctx["teams"] if t["league"] == league and t["id"] != team["id"]]
    other_links = "".join(
        f'<a href="/sports/teams/{esc(t["slug"])}/">{esc(t["name"])} fixtures</a>' for t in same_league
    )
    related = "".join(
        f'<a href="{esc(r["href"])}">{esc(r["label"])}</a>' for r in (team.get("related") or [])
    )

    color = team.get("color") or "#3ddc84"
    hero = f"""
<section class="tp-hero" style="--tp:{esc(color)}">
  <div class="tp-hero-id">
    <img class="tp-crest" src="{esc(team['crest'])}" alt="{esc(team['name'])} crest" width="88" height="88">
    <div>
      <p class="eyebrow">{esc(team['leagueName'])} · 2026/27 season</p>
      <h1>{esc(team['name'])}</h1>
      <p class="tp-meta"><a href="/sports/{esc(league)}/">{esc(team['leagueName'])} desk</a>
      · Founded {esc(team['founded'])} · {esc(team['city'])} · {esc(team['stadium'])}</p>
      <p class="tp-blurb">{esc(blurb(team))}
      <a class="quiet-link" href="{esc(team['historySource'])}" rel="nofollow noopener">Club history source ↗</a></p>
    </div>
  </div>
  <div class="tp-hero-sides">
    {side_card("Next match", next_m)}
    {side_card("Previous result", prev_m)}
  </div>
</section>"""

    overview = f"""
<section class="tp-overview" id="season">
  <div class="section-head"><div><div class="eyebrow">Current season</div><h2>2026/27 overview</h2></div>
  <a href="/sports/{esc(league)}/">Open the {esc(team['leagueName'])} desk</a></div>
  <p class="section-note">{esc(pos_note)}</p>
  <ul class="tp-stats" aria-label="Season totals from sourced results">
    <li><b>{stats['p']}</b><span>Played</span></li>
    <li><b>{stats['w']}</b><span>Won</span></li>
    <li><b>{stats['d']}</b><span>Drawn</span></li>
    <li><b>{stats['l']}</b><span>Lost</span></li>
    <li><b>{stats['gf']}</b><span>GF</span></li>
    <li><b>{stats['ga']}</b><span>GA</span></li>
    <li><b>{esc(gd_txt(stats['gd']))}</b><span>GD</span></li>
    <li><b>{stats['pts']}</b><span>Points</span></li>
    <li><b>{esc(pos_txt)}</b><span>Position</span></li>
  </ul>
  <p class="tp-form-row"><span>Form</span> {form_html(stats['form'])}</p>
</section>"""

    chronicles = f"""
<section class="mwc" id="chronicles" data-mwc>
  <div class="section-head"><div><div class="eyebrow">Original BRYME comic</div>
  <h2>BRYME Matchweek Chronicles</h2></div></div>
  <p class="section-note">Cartoon storylines drawn from sourced full-time results. No broadcast stills, no player photographs. Speech bubbles are fictional squad chatter, not quotes.</p>
  <div class="mwc-carousel">
    <button type="button" class="sp-hero-arrow sp-hero-prev" data-mwc-prev aria-label="Previous matchweek">‹</button>
    <div class="mwc-track" data-mwc-track>{''.join(cards)}</div>
    <button type="button" class="sp-hero-arrow sp-hero-next" data-mwc-next aria-label="Next matchweek">›</button>
  </div>
  <div class="mwc-stories">{''.join(stories_html)}</div>
  <div class="mwc-archive" id="archive">
    <h3>Matchweek archive</h3>
    <ul>{''.join(archive)}</ul>
  </div>
</section>"""

    body = f"""<body data-nav="sports" class="tp-page team-desk">
{HEADER}
<main class="shell tp-main">
  <div class="crumb"><a href="/">Home</a> / <a href="/sports/">BRYME Sports</a> / <a href="/sports/teams/">Teams</a> / {esc(team['name'])}</div>
  {chronicles}
  {hero}
  {overview}
  <section class="tp-fix" id="fixtures">
    <div class="section-head"><div><div class="eyebrow">Calendar</div><h2>Upcoming fixtures</h2></div>
    <a href="/sports/{esc(league)}/fixtures/">Full {esc(team['leagueName'])} fixture list</a></div>
    {rows_for(upcoming, "up")}
  </section>
  <section class="tp-res" id="results">
    <div class="section-head"><div><div class="eyebrow">History</div><h2>Recent results</h2></div>
    <a href="/sports/{esc(league)}/results/">All sourced {esc(team['leagueName'])} results</a></div>
    {rows_for(list(reversed(completed)), "res")}
  </section>
  <section class="tp-links" id="also">
    <div class="section-head"><div><div class="eyebrow">Also on BRYME</div><h2>Related</h2></div></div>
    <div class="tp-linkrow"><b>This league</b>{other_links}</div>
    <div class="tp-linkrow"><b>Stories</b>{related}<a href="/sports/clubs/">Club directory</a><a href="/sports/">Sports hub</a></div>
  </section>
</main>
{FOOTER}
</body></html>"""
    return page_head(title, desc, url, page_ld) + body


def render_hub(teams: list[dict], ctxs: dict) -> str:
    title = "Football Team Pages — Fixtures, Results & Matchweek Comics | BRYME"
    desc = (
        "Permanent BRYME pages for the biggest clubs in the Premier League, La Liga, "
        "Serie A, Bundesliga and Ligue 1. Fixtures, sourced results, form and matchweek comics."
    )
    url = f"{SITE}/sports/teams/"
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "BRYME football team pages",
            "description": desc,
            "url": url,
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "BRYME Sports", "item": SITE + "/sports/"},
                {"@type": "ListItem", "position": 3, "name": "Teams", "item": url},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "BRYME team pages",
            "numberOfItems": len(teams),
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i,
                    "url": f"{SITE}/sports/teams/{t['slug']}/",
                    "name": t["name"],
                }
                for i, t in enumerate(teams, 1)
            ],
        },
    ]
    groups = []
    order = [
        ("premier-league", "Premier League"),
        ("la-liga", "La Liga"),
        ("serie-a", "Serie A"),
        ("bundesliga", "Bundesliga"),
        ("ligue-1", "Ligue 1"),
    ]
    for slug, name in order:
        club = [t for t in teams if t["league"] == slug]
        cards = []
        for t in club:
            matches = ctxs[t["id"]]["matches"]
            future = [
                m
                for m in matches
                if not m.get("result")
                and season_date(m.get("date"), m.get("mw"))
                and season_date(m.get("date"), m.get("mw")) >= TODAY
            ]
            nxt = (
                min(
                    future,
                    key=lambda m: (
                        season_date(m.get("date"), m.get("mw")) or date(9999, 1, 1),
                        m.get("time") or "",
                    ),
                )
                if future
                else next((m for m in matches if not m.get("result")), None)
            )
            prev = None
            done = [m for m in matches if m.get("result")]
            if done:
                prev = max(done, key=lambda m: (m["result"].get("playedOn") or m.get("date") or "", m.get("time") or ""))
            if nxt:
                nxt_line = f"Next: {nxt['homeName']} vs {nxt['awayName']}"
            else:
                nxt_line = "No upcoming fixture in the file"
            if prev:
                r = prev["result"]
                prev_line = f"Last: {prev['homeName']} {r['hs']}–{r['as']} {prev['awayName']}"
            else:
                prev_line = "No sourced result yet"
            cards.append(
                f'<a class="tp-hub-card" href="/sports/teams/{esc(t["slug"])}/" style="--tp:{esc(t.get("color") or "#3ddc84")}">'
                f'<img src="{esc(t["crest"])}" alt="{esc(t["name"])} crest" width="56" height="56">'
                f"<div><b>{esc(t['name'])}</b><span>{esc(nxt_line)}</span><span>{esc(prev_line)}</span></div></a>"
            )
        groups.append(
            f'<section class="tp-hub-lg" id="{esc(slug)}">'
            f'<div class="section-head"><h2>{esc(name)}</h2>'
            f'<a href="/sports/{esc(slug)}/">{esc(name)} desk</a></div>'
            f'<div class="tp-hub-grid">{"".join(cards)}</div></section>'
        )
    body = f"""<body data-nav="sports" class="tp-page">
{HEADER}
<main class="shell tp-main">
  <div class="crumb"><a href="/">Home</a> / <a href="/sports/">BRYME Sports</a> / Teams</div>
  <section class="hero"><div class="eyebrow">⚽ BRYME Sports · Teams</div>
  <h1>Team pages</h1>
  <p class="lead">Permanent pages for the clubs people actually search for. Fixtures, sourced results, form, and BRYME matchweek comics. More clubs can be added without changing the URL pattern.</p></section>
  <p class="vnote">Scores appear only after a sourced full-time result. Sunday 23 August matches stay as previews until a source URL exists. League positions on each team page are computed from those sourced results — not an official table.</p>
  {''.join(groups)}
</main>
{FOOTER}
</body></html>"""
    return page_head(title, desc, url, ld) + body


def rebuild_sitemap():
    urls = []
    for p in ROOT.rglob("index.html"):
        if any(x in p.parts for x in (".git", "reports", "node_modules", "__pycache__")):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        head = text[:5000]
        if "noindex" in head:
            continue
        rel = "/" + str(p.parent.relative_to(ROOT)).replace("\\", "/")
        if rel.endswith("/."):
            rel = ""
        if rel == "/.":
            rel = ""
        url = (rel if rel != "/" else "") + "/"
        can = re.search(r'rel="canonical" href="([^"]+)"', head)
        if can:
            dest = can.group(1).replace(SITE, "")
            if dest.rstrip("/") != url.rstrip("/") and dest.rstrip("/") + "/" != url:
                continue
        urls.append(SITE + (url if url.startswith("/") else "/" + url))
    seen, ordered = set(), []
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        ordered.append(u)
    ordered.sort()
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in ordered)
        + "</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    return len(ordered)


def patch_clubs_directory(teams: list[dict]) -> int:
    p = ROOT / "sports/clubs/index.html"
    html = p.read_text(encoding="utf-8")
    n = 0
    for t in teams:
        name = t["name"]
        href = f"/sports/teams/{t['slug']}/"
        old = f"<td><b>{H.escape(name)}</b></td>"
        new = f'<td><b><a href="{href}">{H.escape(name)} fixtures</a></b></td>'
        if old in html and href not in html.split(old)[0][-80:]:
            html = html.replace(old, new, 1)
            n += 1
        # some rows use slightly different names
        old2 = f"<td><b>{H.escape(name)}</b></td>"
        if old2 not in html and f'href="{href}"' not in html:
            # try without escaping accents already in file
            old3 = f"<td><b>{name}</b></td>"
            new3 = f'<td><b><a href="{href}">{name} fixtures</a></b></td>'
            if old3 in html:
                html = html.replace(old3, new3, 1)
                n += 1
    p.write_text(html, encoding="utf-8")
    return n


def patch_sports_hub() -> bool:
    p = ROOT / "sports/index.html"
    html = p.read_text(encoding="utf-8")
    card = (
        '<a class="sp-comp-card" href="/sports/teams/" style="--card-img:url(\'/assets/img/sports/hero-arsenal.jpg\')">'
        "<em>Clubs</em><b>Team pages</b>"
        "<span>Fixtures, sourced results, form and BRYME matchweek comics for the biggest clubs.</span></a>"
    )
    if 'href="/sports/teams/"' in html:
        return False
    needle = '<a class="sp-comp-card" href="/sports/clubs/"'
    if needle in html:
        html = html.replace(needle, card + needle, 1)
        p.write_text(html, encoding="utf-8")
        return True
    return False


def patch_rebuild_hub_script() -> bool:
    p = ROOT / "scripts/rebuild-sports-hub.py"
    t = p.read_text(encoding="utf-8")
    card = (
        '      <a class="sp-comp-card" href="/sports/teams/" style="--card-img:url(\'/assets/img/sports/hero-arsenal.jpg\')">'
        "<em>Clubs</em><b>Team pages</b>"
        "<span>Fixtures, sourced results, form and BRYME matchweek comics for the biggest clubs.</span></a>\n"
    )
    if 'href="/sports/teams/"' in t:
        return False
    needle = '      <a class="sp-comp-card" href="/sports/clubs/"'
    if needle in t:
        p.write_text(t.replace(needle, card + needle, 1), encoding="utf-8")
        return True
    return False


def patch_league_hubs(teams: list[dict]) -> int:
    n = 0
    by_lg = defaultdict(list)
    for t in teams:
        by_lg[t["league"]].append(t)
    for league, club in by_lg.items():
        p = ROOT / f"sports/{league}/index.html"
        if not p.exists():
            continue
        html = p.read_text(encoding="utf-8")
        if 'id="team-pages"' in html:
            continue
        links = "".join(
            f'<a class="tp-lg-chip" href="/sports/teams/{esc(t["slug"])}/">'
            f'<img src="{esc(t["crest"])}" alt="" width="22" height="22">{esc(t["shortName"])} fixtures</a>'
            for t in club
        )
        block = (
            f'<section class="tp-league-teams" id="team-pages"><div class="shell">'
            f'<div class="section-head"><div><div class="eyebrow">Permanent pages</div>'
            f"<h2>Team pages</h2></div>"
            f'<a href="/sports/teams/">All team pages</a></div>'
            f'<div class="tp-lg-chips">{links}</div></div></section>'
        )
        # insert before related / after first section
        if '<section class="sp-hero"' in html:
            html = html.replace('<section class="sp-hero"', block + '<section class="sp-hero"', 1)
        elif "</main>" in html:
            html = html.replace("</main>", block + "</main>", 1)
        else:
            continue
        p.write_text(html, encoding="utf-8")
        n += 1
    return n


def patch_upgrade_league_script(teams: list[dict]) -> bool:
    p = ROOT / "scripts/upgrade-league-hubs.py"
    if not p.exists():
        return False
    t = p.read_text(encoding="utf-8")
    if "/sports/teams/" in t:
        return False
    # add a Teams chip to each league's chips list — light touch
    replacements = {
        "('/sports/premier-league/fixtures/', 'Fixtures'),": "('/sports/teams/', 'Team pages'),\n            ('/sports/premier-league/fixtures/', 'Fixtures'),",
        "('/sports/la-liga/fixtures/', 'Fixtures'),": "('/sports/teams/', 'Team pages'),\n            ('/sports/la-liga/fixtures/', 'Fixtures'),",
        "('/sports/serie-a/results/', 'Results'),": "('/sports/teams/', 'Team pages'),\n            ('/sports/serie-a/results/', 'Results'),",
    }
    new = t
    for a, b in replacements.items():
        if a in new and "/sports/teams/" not in new[new.find(a) - 80 : new.find(a) + 40]:
            new = new.replace(a, b, 1)
    if new != t:
        p.write_text(new, encoding="utf-8")
        return True
    return False


def patch_match_pages(teams: list[dict], ctxs: dict) -> int:
    by_id = {t["id"]: t for t in teams}
    n = 0
    for t in teams:
        for m in ctxs[t["id"]]["matches"]:
            path = ROOT / f"sports/{t['league']}/matches/{m['slug']}/index.html"
            if not path.exists():
                continue
            html = path.read_text(encoding="utf-8")
            marker = 'class="tp-match-jump"'
            if marker in html:
                continue
            links = []
            for tid, label_name in ((m["homeId"], m["homeName"]), (m["awayId"], m["awayName"])):
                if tid in by_id:
                    tm = by_id[tid]
                    links.append(
                        f'<a href="/sports/teams/{tm["slug"]}/">{H.escape(tm["name"])} fixtures</a>'
                    )
            if not links:
                continue
            jump = f'<p class="tp-match-jump">Team pages: {" · ".join(links)}</p>'
            if '<div class="sp-match-hero">' in html:
                html = html.replace('<div class="sp-match-hero">', jump + '<div class="sp-match-hero">', 1)
            elif "<h1" in html:
                html = re.sub(r"(</h1>)", r"\1" + jump, html, count=1)
            else:
                continue
            path.write_text(html, encoding="utf-8")
            n += 1
    return n


def upsert_redirects(teams: list[dict]) -> int:
    p = ROOT / "_redirects"
    text = p.read_text(encoding="utf-8")
    block_lines = ["# Team page aliases → canonical /sports/teams/{slug}/"]
    n = 0
    for t in teams:
        canon = f"/sports/teams/{t['slug']}/"
        aliases = list(t.get("aliases") or [])
        # also map fixture id if it differs from slug
        if t["id"] != t["slug"]:
            aliases.append(t["id"])
        for a in aliases:
            if a == t["slug"]:
                continue
            line = f"/sports/teams/{a}/  {canon}  301"
            if line not in block_lines:
                block_lines.append(line)
                n += 1
    block = "\n".join(block_lines) + "\n"
    if "# Team page aliases" in text:
        text = re.sub(
            r"# Team page aliases[\s\S]*?(?=\n# |\Z)",
            block.rstrip() + "\n",
            text,
            count=1,
        )
    else:
        text = text.rstrip() + "\n" + block
    p.write_text(text, encoding="utf-8")
    return n


def main():
    registry = load_json("content/teams.json")
    comics = load_json("content/matchweek-comics.json")
    results = load_json("content/results.json")
    teams = registry["teams"]
    by_id = {t["id"]: t for t in teams}

    fixtures_by_league = {}
    table_by_league = {}
    ranked_by_league = {}
    for lg, fn in FIXTURE_FILES.items():
        fx = load_json(f"content/{fn}")
        fixtures_by_league[lg] = fx
        table, ranked = standings_for(lg, fx, results)
        table_by_league[lg] = table
        ranked_by_league[lg] = ranked

    ctxs = {}
    for t in teams:
        lg = t["league"]
        ctxs[t["id"]] = {
            "matches": collect_team_matches(t["id"], fixtures_by_league[lg], results, lg),
            "table": table_by_league[lg],
            "ranked": ranked_by_league[lg],
            "comics": comics,
            "by_id": by_id,
            "teams": teams,
        }

    out_hub = ROOT / "sports/teams/index.html"
    out_hub.parent.mkdir(parents=True, exist_ok=True)
    out_hub.write_text(render_hub(teams, ctxs), encoding="utf-8")

    for t in teams:
        dest = ROOT / "sports/teams" / t["slug"] / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_team_page(t, ctxs[t["id"]]), encoding="utf-8")

    clubs_n = patch_clubs_directory(teams)
    hub_n = patch_sports_hub()
    hub_script = patch_rebuild_hub_script()
    lg_n = patch_league_hubs(teams)
    up_n = patch_upgrade_league_script(teams)
    match_n = patch_match_pages(teams, ctxs)
    redir_n = upsert_redirects(teams)
    sm = rebuild_sitemap()

    print(f"Built {len(teams)} team pages + hub")
    print(f"Patched clubs directory rows: {clubs_n}")
    print(f"Sports hub card: {hub_n}  rebuild script: {hub_script}")
    print(f"League hubs: {lg_n}  upgrade script: {up_n}")
    print(f"Match pages linked: {match_n}")
    print(f"Redirect aliases: {redir_n}")
    print(f"Sitemap URLs: {sm}")


if __name__ == "__main__":
    main()
