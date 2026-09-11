#!/usr/bin/env python3
"""BRYME Sport data agent.

Fetches verified league tables, recent results, top scorers (with assists and
appearances where published) and Premier League club squads from
football-data.org (v4 API, free tier) and writes content/sports-live.json,
which the static build renders into the permanent table / results / scorers /
club pages. Run automatically by .github/workflows/sports-update.yml.

Throttling (per football-data.org guidance): the free tier allows a limited
number of requests per minute. This client reads the X-Requests-Available and
X-RequestCounter-Reset response headers, paces its calls, and backs off (and
retries on HTTP 429) until the counter resets. It never hammers the API.

House rules:
- It NEVER invents data. If the API is unreachable it writes nothing for the
  failed league and keeps the last verified snapshot. Stale-but-sourced beats
  fresh-but-guessed.
- Every write stamps its own source and generation time.
- Fields the source does not publish (e.g. some assists values) are stored as
  null and rendered as an em dash, never as zero.

Auth (security requirement, football-hub rebuild spec s47): the token is NEVER
hard-coded and NEVER committed. It is read from, in order:
  1. the FOOTBALL_DATA_API_KEY environment variable (GitHub Actions secret), or
  2. the untracked local file content/.football-data-key (dev machines).
With neither, the run exits non-zero and the previous snapshot survives.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "sports-live.json"
KEYFILE = ROOT / "content" / ".football-data-key"

LEAGUES = {
    "premier-league": "PL",
    "la-liga": "PD",
    "serie-a": "SA",
    "bundesliga": "BL1",
    "ligue-1": "FL1",
    "champions-league": "CL",
}

# normalise API club names onto the desk's naming (used for PL club-hub links)
NAME_FIX = {
    "Arsenal FC": "Arsenal", "Chelsea FC": "Chelsea", "Everton FC": "Everton",
    "Fulham FC": "Fulham", "Liverpool FC": "Liverpool", "Manchester City FC": "Manchester City",
    "Manchester United FC": "Manchester United", "Newcastle United FC": "Newcastle United",
    "Nottingham Forest FC": "Nottingham Forest", "Tottenham Hotspur FC": "Tottenham Hotspur",
    "West Ham United FC": "West Ham United", "Wolverhampton Wanderers FC": "Wolverhampton Wanderers",
    "Brighton and Hove Albion": "Brighton & Hove Albion", "Brighton & Hove Albion": "Brighton & Hove Albion",
    "Brighton & Hove Albion FC": "Brighton & Hove Albion",
    "AFC Bournemouth": "AFC Bournemouth", "Leeds United FC": "Leeds United",
    "Sunderland AFC": "Sunderland", "Hull City AFC": "Hull City", "Coventry City FC": "Coventry City",
    "Ipswich Town FC": "Ipswich Town", "Crystal Palace FC": "Crystal Palace",
    "Brentford FC": "Brentford", "Aston Villa FC": "Aston Villa",
}


def resolve_key():
    """Env var first, then the untracked dev keyfile. Never a committed secret."""
    key = os.environ.get("FOOTBALL_DATA_API_KEY", "").strip()
    if key:
        return key, "env"
    if KEYFILE.exists():
        key = KEYFILE.read_text().strip()
        if key:
            return key, "keyfile"
    return None, "none"


def get(url, key, tries=4):
    """GET with throttle-header awareness. Paces calls, honours the reset
    window advertised by the API, and retries 429s with its backoff."""
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"X-Auth-Token": key})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                avail = r.headers.get("X-Requests-Available", "")
                reset = r.headers.get("X-RequestCounter-Reset", "")
                body = r.read().decode("utf-8")
                if avail.isdigit() and int(avail) <= 1 and reset.isdigit():
                    wait = int(reset) + 2
                    print(f"  throttle: {avail} requests left, resting {wait}s")
                    time.sleep(wait)
                else:
                    time.sleep(2)  # gentle default pace between calls
                return json.loads(body)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                reset = (e.headers or {}).get("X-RequestCounter-Reset", "")
                wait = int(reset) + 2 if reset.isdigit() else 60
                print(f"  rate-limited (429): waiting {wait}s, attempt {attempt + 1}/{tries}")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("gave up after repeated rate-limiting: " + url)


def _stamp():
    return "fetched " + datetime.now(timezone.utc).strftime("%A %d %B %Y, %H:%M UTC")


def league_data(code, key):
    d = {}
    st = get(f"https://api.football-data.org/v4/competitions/{code}/standings", key)
    table = st["standings"][0]["table"]
    d["table"] = [[row["position"], NAME_FIX.get(row["team"]["name"], row["team"]["name"]),
                   row["playedGames"], row["won"], row["draw"], row["lost"],
                   row["goalsFor"], row["goalsAgainst"], row["goalDifference"], row["points"]]
                  for row in table]
    d["table_updated"] = _stamp()

    ms = get(f"https://api.football-data.org/v4/competitions/{code}/matches?status=FINISHED", key)
    by_mw = {}
    for m in ms.get("matches", []):
        ft = m.get("score", {}).get("fullTime", {})
        if ft.get("home") is None or ft.get("away") is None:
            continue
        by_mw.setdefault(m.get("matchday", 0), []).append({
            "d": (m.get("utcDate") or "")[:10],
            "h": NAME_FIX.get(m["homeTeam"]["name"], m["homeTeam"]["name"]),
            "hs": ft["home"], "as": ft["away"],
            "a": NAME_FIX.get(m["awayTeam"]["name"], m["awayTeam"]["name"]),
        })
    recent = sorted(by_mw)[-3:]
    d["results"] = [{"mw": mw, "matches": by_mw[mw]} for mw in recent]
    d["results_updated"] = _stamp()

    ms2 = get(f"https://api.football-data.org/v4/competitions/{code}/matches?status=SCHEDULED", key)
    up = []
    for m in ms2.get("matches", []):
        up.append({"d": (m.get("utcDate") or "")[:16].replace("T", " "),
                   "h": NAME_FIX.get(m["homeTeam"]["name"], m["homeTeam"]["name"]),
                   "a": NAME_FIX.get(m["awayTeam"]["name"], m["awayTeam"]["name"]),
                   "mw": m.get("matchday", 0)})
    d["upcoming"] = up[:12]
    d["upcoming_updated"] = _stamp()

    try:
        sc = get(f"https://api.football-data.org/v4/competitions/{code}/scorers", key)
        d["scorers"] = [{"p": s["player"]["name"],
                         "c": NAME_FIX.get((s.get("team") or {}).get("name", ""), (s.get("team") or {}).get("name", "")),
                         "g": s["goals"],
                         "a": s.get("assists"),
                         "pm": s.get("playedMatches")} for s in sc.get("scorers", [])[:10]]
        d["scorers_updated"] = _stamp()
    except Exception as e:  # scorers are optional; table+results are the core
        print(f"  scorers unavailable for {code}: {e}")
    return d


def fetch_squads(key):
    """Premier League club squads from /v4/teams/{id}. One standings call for
    the team ids, one call per club. Per-club failure tolerated."""
    st = get("https://api.football-data.org/v4/competitions/PL/standings", key)
    teams = [(NAME_FIX.get(row["team"]["name"], row["team"]["name"]), row["team"]["id"])
             for row in st["standings"][0]["table"]]
    squads, ok = {}, 0
    for name, tid in teams:
        try:
            t = get(f"https://api.football-data.org/v4/teams/{tid}", key)
            players = [[p.get("name", ""), p.get("position") or "", p.get("nationality") or "",
                        (p.get("dateOfBirth") or ""), p.get("shirtNumber")]
                       for p in (t.get("squad") or [])]
            squads[name] = {"id": tid,
                            "founded": t.get("founded"),
                            "venue": t.get("venue") or "",
                            "colors": t.get("clubColors") or "",
                            "players": players}
            ok += 1
            print(f"  squad {name}: {len(players)} players")
        except Exception as e:
            print(f"  squad {name}: FAILED ({e}) - skipped this run")
    if not ok:
        return None
    return {"squads": squads,
            "updated": _stamp() + f" ({ok}/{len(teams)} clubs listed)"}


def main():
    key, where = resolve_key()
    if not key:
        print("No API key: set FOOTBALL_DATA_API_KEY (or write content/.football-data-key). "
              "Nothing fetched - keeping the previous verified snapshot.")
        return 1
    print(f"API key source: {where}")

    old = {}
    if OUT.exists():
        try:
            old = json.loads(OUT.read_text())
        except Exception:
            old = {}
    leagues = old.get("leagues", {})
    ok = 0
    for slug, code in LEAGUES.items():
        try:
            leagues[slug] = dict(leagues.get(slug, {}), **league_data(code, key))
            leagues[slug].pop("pending", None)
            leagues[slug].pop("note", None)
            ok += 1
            print(f"  {slug}: OK")
        except Exception as e:
            print(f"  {slug}: FAILED ({e}) - keeping previous verified snapshot")
    if not ok:
        print("All leagues failed - nothing written.")
        return 1

    if "premier-league" in leagues and leagues["premier-league"].get("table"):
        try:
            sq = fetch_squads(key)
            if sq:
                leagues["premier-league"]["squads"] = sq["squads"]
                leagues["premier-league"]["squads_updated"] = sq["updated"]
        except Exception as e:
            print(f"  squads unavailable this run ({e}) - keeping any previous list")

    OUT.write_text(json.dumps({
        "_comment": "Written by scripts/sports_update_agent.py - source: football-data.org v4. The desk never publishes unverified data.",
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "source": "football-data.org v4",
        "leagues": leagues,
    }, ensure_ascii=False, indent=1))
    print(f"Wrote {OUT} ({ok}/{len(LEAGUES)} leagues updated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
