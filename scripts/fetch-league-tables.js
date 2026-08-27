#!/usr/bin/env node
/* BRYME — ESPN public standings API -> content/league-tables.json
   Top-five league tables for the Mini App sports section.
   Agent-safe: a league that fails to fetch/validate is skipped;
   if nothing validates, the existing file is kept untouched. */
"use strict";
const fs = require("fs");
const path = require("path");
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "content", "league-tables.json");

const LEAGUES = [
  { id: "premier-league", code: "eng.1", name: "Premier League", flag: "🏴󠁧󠁢󠁥󠁮󠁧󠁿" },
  { id: "la-liga",        code: "esp.1", name: "LaLiga",         flag: "🇪🇸" },
  { id: "serie-a",        code: "ita.1", name: "Serie A",        flag: "🇮🇹" },
  { id: "bundesliga",     code: "ger.1", name: "Bundesliga",     flag: "🇩🇪" },
  { id: "ligue-1",        code: "fra.1", name: "Ligue 1",        flag: "🇫🇷" }
];

function statMap(entry) {
  const m = {};
  (entry.stats || []).forEach((s) => { m[s.name] = s; });
  return m;
}
function num(v) { const n = Number(v); return Number.isFinite(n) ? n : 0; }

async function fetchLeague(lg) {
  const r = await fetch("https://site.api.espn.com/apis/v2/sports/soccer/" + lg.code + "/standings", {
    headers: { "user-agent": "bryme-agent/1.0" }, signal: AbortSignal.timeout(20000)
  });
  if (!r.ok) throw new Error(lg.id + " HTTP " + r.status);
  const d = await r.json();
  const entries = d && d.children && d.children[0] && d.children[0].standings && d.children[0].standings.entries;
  if (!Array.isArray(entries) || entries.length < 6) throw new Error(lg.id + " thin standings");
  const teams = entries.map((e) => {
    const s = statMap(e);
    const team = e.team || {};
    return {
      pos: num((s.rank || {}).summary) || 0,
      name: team.displayName || team.name || "?",
      short: team.shortDisplayName || team.abbreviation || team.displayName || "?",
      logo: (team.logos && team.logos[0] && team.logos[0].href) || "",
      p: num((s.gamesPlayed || {}).displayValue ?? (s.gamesPlayed || {}).summary),
      w: num((s.wins || {}).displayValue ?? (s.wins || {}).summary),
      d: num((s.ties || {}).displayValue ?? (s.ties || {}).summary),
      l: num((s.losses || {}).displayValue ?? (s.losses || {}).summary),
      gf: num((s.pointsFor || {}).displayValue ?? (s.pointsFor || {}).summary),
      ga: num((s.pointsAgainst || {}).displayValue ?? (s.pointsAgainst || {}).summary),
      gd: String((s.pointDifferential || {}).summary ?? (s.pointDifferential || {}).displayValue ?? "0"),
      pts: num((s.points || {}).displayValue ?? (s.points || {}).summary)
    };
  }).filter((t) => t.name !== "?")
    .sort((a, b) => b.pts - a.pts || num(b.gd) - num(a.gd) || b.gf - a.gf || a.name.localeCompare(b.name));
  teams.forEach((t, i) => { t.pos = i + 1; });
  if (teams.length < 6) throw new Error(lg.id + " too few valid teams");
  return { id: lg.id, name: lg.name, flag: lg.flag, teams };
}

(async () => {
  const leagues = [];
  for (const lg of LEAGUES) {
    try { leagues.push(await fetchLeague(lg)); console.log("ok  ", lg.id, "(" + leagues[leagues.length - 1].teams.length + " teams)"); }
    catch (e) { console.log("skip", e.message); }
  }
  if (!leagues.length) {
    if (fs.existsSync(OUT)) { console.log("no data — keeping existing file"); process.exit(0); }
    console.error("no data at all"); process.exit(1);
  }
  const out = { builtAt: new Date().toISOString(), leagues };
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + "\n");
  console.log("wrote", path.relative(ROOT, OUT), "—", leagues.length, "leagues,", leagues.reduce((n, l) => n + l.teams.length, 0), "teams");
})().catch((e) => { console.error(e.message); process.exit(1); });
