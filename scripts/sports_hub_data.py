# BRYME Sport desk — taxonomy for the living-machine hub (batch 1).
# Wall rows = editorial pieces only (explainers, analysis, season desk).
# League data pages (tables/fixtures/results/scorers/transfers), club pages
# and shelf hubs stay as clusters/links — they are live data, not articles.

SPO_CATS = {
    "explainers": ("Understand the game",
                   "Laws, formats and roles: offside, VAR, xG, loans, release clauses, shirt numbers — the rules behind the noise, evergreen."),
    "analysis": ("The tactics board",
                 "How the game is actually played: pressing, possession, building from the back, the offside trap — read as argument, never as tips."),
    "season": ("The season desk 2026-27",
               "Matchweek editions, the transfer window, the living trackers and the big questions — dated honestly, archived when the moment passes."),
}

# (key, label, blurb)
SPO_NEEDS = [
    ("weekend", "This weekend",
     "What is on, what it means and what to watch first — the matchweek, immediately."),
    ("learn", "Learn the laws",
     "Offside, VAR, extra time, loans, windows: the rules and formats, explained once and properly."),
    ("read", "Read the game",
     "Tactics with the receipts: pressing triggers, possession myths, set-piece maths."),
    ("follow", "Follow the season",
     "Title races, the Ballon d'Or, Ronaldo's thousand, the window that never sleeps — tracked, dated, revisable."),
]

# slugs carried by the wall, per layer (used by the wiring's asserts)
SPO_BIGQ = ["who-will-win-the-2026-ballon-dor", "can-ronaldo-score-1000-goals",
            "who-will-win-the-2026-27-premier-league", "best-football-players-in-the-world-2026",
            "who-will-win-the-2026-27-champions-league", "what-the-2026-world-cup-changed"]
SPO_REAL_ARCHIVE = ["premier-league-transfer-tracker-august-2026", "premier-league-matchweek-1-guide",
                    "premier-league-matchweek-2-preview", "deadline-day-dont-try-to-make-sense-of-it"]
SPO_REAL_LIVE = ["elliot-anderson-man-city-record-signing"]
SPO_WEEKEND = {"the-weekend-ahead": "archive", "premier-league-matchweek-4-preview": "feature"}

# routes that are live-data or shelf surfaces, not wall rows
SPO_SKIP_SLUGS = {
    "epl", "premier-league", "laliga", "bundesliga", "serie-a", "ligue-1", "champions-league",
    "explainers", "analysis", "transfers", "fpl", "form-board", "premier-league-clubs",
    "about", "contact", "privacy", "terms", "copyright", "corrections", "editorial-policy",
    "points-race-calculator",  # desk tool (toolbox band, not the pieces wall)
    "transfer-amortisation-calculator",  # desk tool (growth batch 2026-09-25)
}
SPO_SKIP_SUFFIX = ("-fixtures", "-results", "-table", "-top-scorers", "-transfers")

# cluster cards: the live surfaces of the desk
SPO_CLUSTERS = [
    ("/epl/", "Premier League", "The desk hub: table, fixtures, results and scorers, verified on a schedule."),
    ("/champions-league/", "Champions League", "The 36-team league phase, explained and tracked."),
    ("/laliga/", "LaLiga", "Spain's league and the Clásico, explained plainly."),
    ("/bundesliga/", "Bundesliga", "Germany's shelf: table, calendar, scorers, window."),
    ("/serie-a/", "Serie A", "Italy's shelf: table, calendar, scorers, window."),
    ("/ligue-1/", "Ligue 1", "France's shelf: table, calendar, scorers, window."),
    ("/transfers/", "The transfer desk", "The window in one place — done deals sourced, rumours labelled."),
    ("/premier-league-clubs/", "The 20 clubs", "Every Premier League club, 2026-27."),
    ("/fpl/", "Fantasy Premier League", "The honest FPL guide — no tips sold as certainties."),
    ("/form-board/", "The Form Board", "Last-five form across the six leagues, one table."),
]

SPO_CADENCE = {"explainers": 365, "analysis": 365, "season": 30}
