#!/usr/bin/env node
/* BRYME auto-scores — ESPN public API -> content/results.json.
   Never overwrites; validates pairings against fixtures. Dry: --dry */
const fs = require("fs");
const path = require("path");
const root = path.resolve(__dirname, "..");
const LEAGUES = {
  "premier-league": { file: "fixtures.json", code: "eng.1" },
  "la-liga": { file: "fixtures-la-liga.json", code: "esp.1" },
  "serie-a": { file: "fixtures-serie-a.json", code: "ita.1" },
  "bundesliga": { file: "fixtures-bundesliga.json", code: "ger.1" },
  "ligue-1": { file: "fixtures-ligue-1.json", code: "fra.1" }
};
const ALIASES = {
  "internazionale": "inter", "inter milan": "inter", "as roma": "roma",
  "marseille": "olympique de marseille", "paris saint germain": "psg", "paris sg": "psg",
  "deportivo la coruna": "coruna", "deportivo de la coruna": "coruna", "deportivo": "coruna",
  "atalanta bc": "atalanta", "ac milan": "milan", "athletic club": "athletic bilbao",
  "rayo": "rayo vallecano", "spurs": "tottenham", "tottenham hotspur": "tottenham",
  "manchester city": "man city", "manchester united": "man utd", "newcastle": "newcastle united",
  "brighton and hove albion": "brighton", "brighton hove albion": "brighton", "brighton hove": "brighton",
  "wolves": "wolverhampton", "nottm forest": "nottingham forest", "west ham united": "west ham",
  "leicester city": "leicester", "rc lens": "lens", "ogc nice": "nice", "fc lorient": "lorient",
  "stade brestois": "brest", "stade brestois 29": "brest", "toulouse fc": "toulouse",
  "angers sco": "angers", "lille osc": "lille", "lille losc": "lille", "rc strasbourg": "strasbourg",
  "strasbourg alsace": "strasbourg", "le mans fc": "le mans", "aj auxerre": "auxerre",
  "lyon": "olympique lyonnais", "estac troyes": "troyes", "rennes": "stade rennais",
  "hull": "hull city", "coventry": "coventry city", "ac monza": "monza"
};
const DENY = new Set(["ligue-1/rennes-vs-psg"]);
const STRIP = /^(as|ac|sc|rc|ogc|aj|fc|usc|ss|calcio|club|deportivo de la|the)\s+/i;
function norm(name) {
  let n = name.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    .replace(/&/g, "and").replace(/[^a-z0-9 ]/g, " ").replace(/\s+/g, " ").trim();
  if (ALIASES[n]) return ALIASES[n];
  let s = n.replace(STRIP, "").replace(/\s+(fc|cf|afc|bk|sk)\b/g, "").trim();
  if (ALIASES[s]) return ALIASES[s];
  return s;
}
function iso(d) { return d.toISOString().slice(0, 10); }
(async () => {
  const dry = process.argv.includes("--dry");
  const resultsPath = path.join(root, "content/results.json");
  const results = JSON.parse(fs.readFileSync(resultsPath, "utf8"));
  const days = [];
  const now = new Date();
  for (let i = 4; i >= 0; i--) { const d = new Date(now); d.setUTCDate(d.getUTCDate() - i); days.push(iso(d)); }
  let added = 0, skipped = 0, unmatched = 0;
  const report = [];
  for (const [lg, cfg] of Object.entries(LEAGUES)) {
    const fx = JSON.parse(fs.readFileSync(path.join(root, "content", cfg.file), "utf8"));
    const validPairs = new Set();
    fx.matchweeks.forEach(w => w.matches.forEach(m => validPairs.add(`${m.id}-vs-${m.away}`)));
    const byNorm = {};
    fx.matchweeks.forEach(w => w.matches.forEach(m => {
      const h = norm(m.homeName), a = norm(m.awayName);
      byNorm[h] = byNorm[h] || {};
      byNorm[h].homeId = m.id; byNorm[h].homeName = m.homeName;
      byNorm[a] = byNorm[a] || {};
      byNorm[a].awayId = m.away; byNorm[a].awayName = m.awayName;
    }));
    for (const day of days) {
      let json;
      try {
        const r = await fetch(`https://site.api.espn.com/apis/site/v2/sports/soccer/${cfg.code}/scoreboard?dates=${day.replace(/-/g, "")}`);
        json = await r.json();
      } catch (e) { report.push(`FETCH-FAIL ${lg} ${day}: ${e.message}`); continue; }
      for (const ev of (json.events || [])) {
        const comp = ev.competitions && ev.competitions[0];
        if (!comp) continue;
        const home = comp.competitors.find(c => c.homeAway === "home");
        const away = comp.competitors.find(c => c.homeAway === "away");
        if (!home || !away) continue;
        if (!ev.status || !ev.status.type || ev.status.type.state !== "post") continue;
        const h = byNorm[norm(home.team.displayName)];
        const a = byNorm[norm(away.team.displayName)];
        if (!h || !a || !h.homeId || !a.awayId) {
          unmatched++;
          report.push(`UNMATCHED ${lg}: ${home.team.displayName} v ${away.team.displayName} (${day})`);
          continue;
        }
        const key = `${h.homeId}-vs-${a.awayId}`;
        if (DENY.has(lg + "/" + key)) { skipped++; continue; }
        if (!validPairs.has(key)) {
          unmatched++;
          report.push(`NO-FIXTURE ${lg}: -> ${key} (${day})`);
          continue;
        }
        results[lg] = results[lg] || {};
        if (results[lg][key]) { skipped++; continue; }
        const homeNorm = norm(home.team.displayName);
        const scorers = [];
        for (const d of (comp.details || [])) {
          if (!d.type || !/goal|penalty|own goal/i.test(d.type.text || "")) continue;
          const who = (d.athletesInvolved || [])[0];
          if (!who) continue;
          const tn = (d.team && (d.team.displayName || d.team.name)) || d.teamDisplayName;
          if (!tn) continue;
          scorers.push({
            team: norm(tn) === homeNorm ? "home" : "away",
            player: who.displayName || who.shortName || "",
            minute: String((d.clock && d.clock.displayValue) || "").replace(/\s/g, "")
          });
        }
        const link = (ev.links || []).find(l => /espn\.com/.test(l.href || ""));
        results[lg][key] = {
          homeScore: parseInt(home.score, 10) || 0,
          awayScore: parseInt(away.score, 10) || 0,
          status: "FT",
          playedOn: day,
          source: { name: "ESPN", url: (link && link.href) || "https://www.espn.com/soccer/" }
        };
        if (scorers.length) results[lg][key].scorers = scorers;
        added++;
        report.push(`ADDED ${lg}: ${h.homeName} ${home.score}-${away.score} ${a.awayName} => ${key} (${day})`);
      }
    }
  }
  console.log(report.join("\n"));
  console.log(`\nsummary: ${added} added, ${skipped} already known, ${unmatched} unmatched`);
  if (dry || added === 0) { console.log(added === 0 ? "no changes" : "dry run — not writing"); process.exit(0); }
  fs.writeFileSync(resultsPath, JSON.stringify(results, null, 2) + "\n");
  console.log("results.json updated");
})();
