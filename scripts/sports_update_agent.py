#!/usr/bin/env python3
"""BRYME Sport data agent.

Fetches verified league tables, recent results and top scorers from
football-data.org (v4 API, free tier) and writes content/sports-live.json,
which the static build renders into the permanent table / results / scorers
pages. Run automatically by .github/workflows/sports-update.yml.

House rules:
- It NEVER invents data. If the API is unreachable or no key is configured,
  it writes nothing and exits non-zero, leaving the last verified snapshot
  in place. Stale-but-sourced beats fresh-but-guessed.
- Every write stamps its own source and generation time.

Setup (one-time): add repository secret FOOTBALL_DATA_API_KEY with a free
key from https://www.football-data.org/client/register
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "sports-live.json"

LEAGUES = {
    "premier-league": "PL",
    "la-liga": "PD",
    "serie-a": "SA",
    "bundesliga": "BL1",
    "ligue-1": "FL1",
}

# normalise API club names onto the desk's naming (used for PL club-hub links)
NAME_FIX = {
    "Arsenal FC": "Arsenal", "Chelsea FC": "Chelsea", "Everton FC": "Everton",
    "Fulham FC": "Fulham", "Liverpool FC": "Liverpool", "Manchester City FC": "Manchester City",
    "Manchester United FC": "Manchester United", "Newcastle United FC": "Newcastle United",
    "Nottingham Forest FC": "Nottingham Forest", "Tottenham Hotspur FC": "Tottenham Hotspur",
    "West Ham United FC": "West Ham United", "Wolverhampton Wanderers FC": "Wolverhampton Wanderers",
    "Brighton and Hove Albion": "Brighton & Hove Albion", "Brighton & Hove Albion": "Brighton & Hove Albion",
    "AFC Bournemouth": "AFC Bournemouth", "Leeds United FC": "Leeds United",
    "Sunderland AFC": "Sunderland", "Hull City AFC": "Hull City", "Coventry City FC": "Coventry City",
    "Ipswich Town FC": "Ipswich Town", "Crystal Palace FC": "Crystal Palace",
    "Brentford FC": "Brentford", "Aston Villa FC": "Aston Villa",
}


def get(url, key):
    req = urllib.request.Request(url, headers={"X-Auth-Token": key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def league_data(code, key):
    d = {}
    st = get(f"https://api.football-data.org/v4/competitions/{code}/standings", key)
    table = st["standings"][0]["table"]
    d["table"] = [[row["position"], NAME_FIX.get(row["team"]["name"], row["team"]["name"]),
                   row["playedGames"], row["won"], row["draw"], row["lost"],
                   row["goalsFor"], row["goalsAgainst"], row["goalDifference"], row["points"]]
                  for row in table]
    d["table_updated"] = "fetched " + datetime.now(timezone.utc).strftime("%A %d %B %Y, %H:%M UTC")

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
    d["results_updated"] = "fetched " + datetime.now(timezone.utc).strftime("%A %d %B %Y, %H:%M UTC")

    try:
        sc = get(f"https://api.football-data.org/v4/competitions/{code}/scorers", key)
        d["scorers"] = [{"p": s["player"]["name"],
                         "c": NAME_FIX.get((s.get("team") or {}).get("name", ""), (s.get("team") or {}).get("name", "")),
                         "g": s["goals"]} for s in sc.get("scorers", [])[:10]]
        d["scorers_updated"] = "fetched " + datetime.now(timezone.utc).strftime("%A %d %B %Y, %H:%M UTC")
    except Exception as e:  # scorers are optional; table+results are the core
        print(f"  scorers unavailable for {code}: {e}")
    return d


def main():
    key = os.environ.get("FOOTBALL_DATA_API_KEY")
    if not key:
        print("FOOTBALL_DATA_API_KEY is not set - no update written.")
        print("The desk never fabricates data. Add the free key as a repository")
        print("secret (football-data.org) and re-run, or keep the last verified snapshot.")
        return 1

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

    OUT.write_text(json.dumps({
        "_comment": "Written by scripts/sports_update_agent.py - source: football-data.org v4. The desk never publishes unverified data.",
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "source": "football-data.org v4 (free tier)",
        "leagues": leagues,
    }, ensure_ascii=False, indent=1))
    print(f"Wrote {OUT} ({ok}/{len(LEAGUES)} leagues updated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
