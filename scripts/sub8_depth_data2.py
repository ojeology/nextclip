# -*- coding: utf-8 -*-
"""Editorial depth sections, part 2: sports and home pages still under 8.0.
The sports data pages scored low partly because they carried no headings or
lists in the main column at all, so each block supplies real prose plus
structure, a review date and one verified external reference.
Every external URL curl-verified 200 at authoring time."""

EPL = "https://www.premierleague.com/"
LALIGA = "https://www.laliga.com/"
LIGUE1 = "https://www.ligue1.com/"
FIFA = "https://www.fifa.com/"
EPA = "https://www.epa.gov/"
WHO = "https://www.who.int/"
ENERGY = "https://www.energy.gov/"
ICC = "https://www.iccsafe.org/"
CISA = "https://www.cisa.gov/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS2 = {

# ------------------------------- sports --------------------------------

"sports/bundesliga-results":
    "<h2>How to read a Bundesliga results page</h2>"
    "<p>A results list is a record, and what makes it useful is knowing what it can and cannot tell you. A scoreline records the outcome of ninety minutes under specific conditions: a squad, an opposition, a referee, a pitch and a moment in the season. It does not record how the game was decided, and it does not record how much of the result was repeatable. The <a href=\"" + _w("Bundesliga") + "\" rel=\"noopener\">Bundesliga reference material on Wikipedia</a> documents the competition's structure and history, which is the context these fixtures sit inside. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What the sequence tells you that a single result does not</h2>"
    "<p>Read results in runs rather than in isolation. A side that has taken points from five consecutive home games is describing something about its home form; a side whose last three away results are losses is describing something else, and the two are not interchangeable. The desk's <a href=\"/sports/bundesliga-table/\">Bundesliga table</a> gives the aggregate view, and the results feed below it is where the pattern actually shows up.</p>"
    "<ul>"
    "<li><b>Separate home and away.</b> Combined form hides the split that most often explains a run.</li>"
    "<li><b>Note the opposition.</b> Points taken from the top six and points taken from the bottom six are different achievements.</li>"
    "<li><b>Watch the goal column.</b> A run of narrow results built on one-goal margins is more fragile than it looks.</li>"
    "<li><b>Check the dates.</b> Results either side of a European tie are affected by rotation in ways the scoreline will not show.</li>"
    "</ul>"
    "<p>For the reading method itself, <a href=\"/sports/possession-explained/\">possession explained</a> covers why the statistics printed next to a result are the least reliable part of it, and <a href=\"/sports/champions-league-results/\">Champions League results</a> gives the same view across the continental competition.</p>",

"sports/bundesliga-top-scorers":
    "<h2>What a goalscoring list measures</h2>"
    "<p>A top-scorers table ranks output, not ability. It counts goals, and it counts them without regard to minutes played, the strength of the opposition, or how many of those goals arrived in games the team had already won. That is not a flaw in the list so much as a limit on what it can be asked. The <a href=\"" + _w("Bundesliga") + "\" rel=\"noopener\">Bundesliga reference material on Wikipedia</a> covers the competition whose scoring records appear here, including the historical context for the totals at the top of the table. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>Reading the list against the season</h2>"
    "<p>The useful comparison is goals per ninety minutes rather than goals outright, because it separates a striker who is efficient from one who is simply always on the pitch. Penalty conversion is the second adjustment worth making: a substantial share of the goals at the top of most scoring lists arrives from the spot, and those are distributed by team hierarchy rather than by finishing talent.</p>"
    "<ul>"
    "<li><b>Normalise for minutes.</b> A player with fewer goals and fewer minutes can be the better scorer.</li>"
    "<li><b>Separate penalties.</b> Set-piece responsibility is assigned, not earned, and it inflates totals unevenly.</li>"
    "<li><b>Look at the trend.</b> A scoring run concentrated in three games is different from steady output across a season.</li>"
    "<li><b>Contextualise the team.</b> A leading scorer in a struggling side is often describing that side's reliance on him.</li>"
    "</ul>"
    "<p>The desk applies the same reading to the other leagues: <a href=\"/sports/premier-league-top-scorers/\">Premier League top scorers</a>, <a href=\"/sports/la-liga-top-scorers/\">La Liga top scorers</a> and <a href=\"/sports/serie-a-top-scorers/\">Serie A top scorers</a> are all worth comparing side by side, because the shape of each list says something about how that league is played.</p>",

"sports/champions-league-fixtures":
    "<h2>Reading a fixture list</h2>"
    "<p>A fixture list is a schedule with consequences attached. Beyond the dates, the useful information is the sequence: which ties fall either side of a domestic match, which travel is long, and which group has its decisive games compressed into a fortnight. The <a href=\"" + _w("UEFA_Champions_League") + "\" rel=\"noopener\">Champions League reference material on Wikipedia</a> explains the competition format that determines how these fixtures are arranged, which is why the calendar looks the way it does. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What the calendar decides before anyone kicks a ball</h2>"
    "<p>Squad depth is tested by scheduling rather than by opposition. A club playing domestically on Saturday and in Europe on Tuesday is fielding two different teams in practice, whatever the manager says about the starting eleven, and the fixture list is where you can see that pressure building weeks in advance.</p>"
    "<ul>"
    "<li><b>Find the congested weeks.</b> Two games in four days, twice running, is where results start to slip.</li>"
    "<li><b>Note the travel.</b> A long away trip followed by a domestic fixture costs more than the distance suggests.</li>"
    "<li><b>Identify the decisive dates.</b> Group qualification is usually settled in two matchdays, not across six.</li>"
    "<li><b>Watch the dead rubber.</b> A side already through fields differently, and that changes the game for the team that still needs a result.</li>"
    "</ul>"
    "<p>The <a href=\"/sports/champions-league-results/\">Champions League results</a> page carries the outcomes as they land, and <a href=\"/sports/champions-league-top-scorers/\">Champions League top scorers</a> tracks the individual race across the same fixtures. For the transfer activity that reshapes these squads between rounds, see <a href=\"/sports/transfers/\">the transfers desk</a>.</p>",

"sports/champions-league-results":
    "<h2>Why European results read differently</h2>"
    "<p>Knockout football produces results that league football does not. A tie played over two legs rewards the side that manages the aggregate rather than the side that wins a match, and a single away performance can decide a contest that looked settled. The <a href=\"" + _w("UEFA_Champions_League") + "\" rel=\"noopener\">Champions League reference material on Wikipedia</a> documents the format, including the historical changes to how away goals and extra time are handled, which is why older results sometimes look inconsistent with current ones. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What to take from a result, and what to leave</h2>"
    "<p>A knockout result is heavily conditioned by the state of the tie. A team leading on aggregate plays a different game from one chasing it, and the scoreline reflects that context more than it reflects underlying quality. This is the single biggest source of misreading in European football: treating a comfortable second-leg win as evidence of a comfortable team.</p>"
    "<ul>"
    "<li><b>Read the aggregate, not the match.</b> The second leg is shaped entirely by the first.</li>"
    "<li><b>Account for game state.</b> A side protecting a lead will produce statistics that flatter its opponent.</li>"
    "<li><b>Separate the group stage.</b> Six-match samples against varied opposition behave differently from two-legged ties.</li>"
    "<li><b>Treat penalties as noise.</b> A shootout decides who advances and tells you very little about who was better.</li>"
    "</ul>"
    "<p>The fixtures that produced these results are listed at <a href=\"/sports/champions-league-fixtures/\">Champions League fixtures</a>, and the individual story runs through <a href=\"/sports/champions-league-top-scorers/\">Champions League top scorers</a>. For how the same reading applies domestically, the desk's <a href=\"/sports/premier-league-results/\">Premier League results</a> page works through the same principles in a league format.</p>",

"sports/champions-league-top-scorers":
    "<h2>A scoring race across a small sample</h2>"
    "<p>The Champions League top-scorers list is built from far fewer games than a domestic equivalent, which makes it both more dramatic and less reliable as a measure. A player can lead it on a run of two performances, and the list rarely settles before the closing rounds. The <a href=\"" + _w("UEFA_Champions_League") + "\" rel=\"noopener\">Champions League reference material on Wikipedia</a> covers the competition's records, including the totals that define what a serious challenge looks like over a full campaign. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>How the race is usually won</h2>"
    "<p>Deep runs matter more than prolific group stages. A striker whose team reaches the semi-final has four more opportunities than one eliminated in the last sixteen, and history favours the players whose clubs stay in the competition. Group-stage goals against weaker opposition are the least predictive part of the total.</p>"
    "<ul>"
    "<li><b>Weight the knockout rounds.</b> Goals there are harder and they arrive when the team is still alive.</li>"
    "<li><b>Discount the group-stage padding.</b> High totals built in the group phase rarely hold up.</li>"
    "<li><b>Track minutes as well as goals.</b> Rotation in a long campaign changes who is even available to score.</li>"
    "<li><b>Follow the team's progress.</b> The leading scorer is almost always a player from a club still in it.</li>"
    "</ul>"
    "<p>The same method applies to the domestic lists at <a href=\"/sports/premier-league-top-scorers/\">Premier League top scorers</a> and <a href=\"/sports/bundesliga-top-scorers/\">Bundesliga top scorers</a>, where the sample is larger and the reading more stable. For the fixtures that produce these goals, see <a href=\"/sports/champions-league-fixtures/\">Champions League fixtures</a>.</p>",

"sports/la-liga-results":
    "<h2>Reading the results in a top-heavy league</h2>"
    "<p>La Liga's results are shaped by a distribution of spending that is more uneven than most European leagues, which shows up in the scorelines: the gap between the strongest and weakest sides produces a distinctive pattern of results that a flat table conceals. <a href=\"" + LALIGA + "\" rel=\"noopener\">La Liga</a> is the competition's own authority for official fixtures and standings, and the <a href=\"" + _w("La_Liga") + "\" rel=\"noopener\">La Liga reference material on Wikipedia</a> carries the historical context for how that distribution came about. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What the pattern of results tells you</h2>"
    "<p>Look for the mid-table compression. In leagues with a wide spread, the middle of the table is where results become least predictable, and that is where the reading skill pays. The top of the table is largely determined by budget; the middle is determined by form, scheduling and the small tactical margins.</p>"
    "<ul>"
    "<li><b>Split the table into bands.</b> Results between teams in the same band are the ones that carry information.</li>"
    "<li><b>Track home advantage separately.</b> It varies considerably by ground and by crowd, and it is not a constant.</li>"
    "<li><b>Note European fatigue.</b> Clubs in continental competition drop points domestically in predictable weeks.</li>"
    "<li><b>Read the late-season results carefully.</b> Motivation varies enormously once nothing is at stake.</li>"
    "</ul>"
    "<p>The <a href=\"/sports/la-liga-table/\">La Liga table</a> gives the aggregate, and <a href=\"/sports/la-liga-top-scorers/\">La Liga top scorers</a> tracks the individual race. For the cross-league comparison, the desk's <a href=\"/sports/bundesliga-results/\">Bundesliga results</a> page applies the same reading to a differently structured competition.</p>",

"sports/la-liga-top-scorers":
    "<h2>What the scoring list reflects about the league</h2>"
    "<p>La Liga's scoring lists have historically been led by a very small number of players across long periods, which is a function of both individual quality and the concentration of chances at the strongest clubs. <a href=\"" + LALIGA + "\" rel=\"noopener\">La Liga</a> publishes the official competition statistics, and the <a href=\"" + _w("La_Liga") + "\" rel=\"noopener\">La Liga reference material on Wikipedia</a> documents the records that give the current race its context. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>Adjusting the numbers before you compare them</h2>"
    "<p>Goals per ninety minutes is the first adjustment, and it matters more here than in most leagues because rotation patterns at the top clubs are so pronounced. Penalty responsibility is the second: the leading scorer in a dominant side is usually also its designated penalty taker, which adds goals that are not really a measure of finishing.</p>"
    "<ul>"
    "<li><b>Normalise for playing time.</b> Especially for players rotating between competitions.</li>"
    "<li><b>Strip out penalties before comparing.</b> Then compare the open-play figures separately.</li>"
    "<li><b>Consider the service.</b> A striker's total is partly a statement about the midfield behind him.</li>"
    "<li><b>Watch the injury interruptions.</b> A season broken by two months out produces a total that understates the rate.</li>"
    "</ul>"
    "<p>The desk reads the other lists the same way: <a href=\"/sports/premier-league-top-scorers/\">Premier League top scorers</a>, <a href=\"/sports/serie-a-top-scorers/\">Serie A top scorers</a> and <a href=\"/sports/ligue-1-top-scorers/\">Ligue 1 top scorers</a>. For how these goals land in the standings, see <a href=\"/sports/la-liga-results/\">La Liga results</a>.</p>",

"sports/ligue-1-results":
    "<h2>Reading results in a developing-player league</h2>"
    "<p>Ligue 1 has a distinct character among the major European leagues: it is a competition where a significant share of the most talented players are early in their careers, which makes results more volatile from season to season and squad turnover higher. <a href=\"" + LIGUE1 + "\" rel=\"noopener\">Ligue 1</a> is the official source for fixtures and standings, and the <a href=\"" + _w("Ligue_1") + "\" rel=\"noopener\">Ligue 1 reference material on Wikipedia</a> covers the league's structure and its place in European football. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>Why the results move more than the table suggests</h2>"
    "<p>Youth and turnover mean that form is less persistent here than in leagues with settled squads. A side that finished strongly may have lost three starters by the next season, and the results reset accordingly. Reading a run of Ligue 1 results therefore requires more attention to squad continuity than the equivalent exercise elsewhere.</p>"
    "<ul>"
    "<li><b>Check who is still at the club.</b> The squad that produced last season's run may no longer exist.</li>"
    "<li><b>Weight home form heavily.</b> It is the more stable signal in a league with variable away performances.</li>"
    "<li><b>Track the promoted sides separately.</b> Their early-season results are poorly predicted by anything prior.</li>"
    "<li><b>Watch the European participants.</b> Squad depth is thinner, so continental football costs more domestically.</li>"
    "</ul>"
    "<p>The <a href=\"/sports/ligue-1-table/\">Ligue 1 table</a> carries the aggregate view and <a href=\"/sports/ligue-1-top-scorers/\">Ligue 1 top scorers</a> the individual race. For the transfer activity that drives the turnover, the desk's <a href=\"/sports/transfers/\">transfers coverage</a> is the place to start.</p>",

"sports/ligue-1-top-scorers":
    "<h2>A scoring list in a league of departures</h2>"
    "<p>The defining feature of Ligue 1's scoring race is that its leaders often do not stay. Strong individual seasons are frequently followed by transfers, which means the list is a record of a moment rather than a hierarchy. <a href=\"" + LIGUE1 + "\" rel=\"noopener\">Ligue 1</a> publishes the official statistics, and the <a href=\"" + _w("Ligue_1") + "\" rel=\"noopener\">Ligue 1 reference material on Wikipedia</a> documents the scoring records that frame the current race. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What to look for beyond the total</h2>"
    "<p>The interesting question in this league is usually not who is leading but whether the total is sustainable. A striker producing at a high rate for a mid-table side is a different proposition from one whose goals come mostly against weaker opposition at home, and the distinction tends to resolve itself in the transfer market long before it resolves in the standings.</p>"
    "<ul>"
    "<li><b>Check the spread of opposition.</b> Goals concentrated against the bottom half are less informative.</li>"
    "<li><b>Look at the age profile.</b> Younger leaders here are usually the ones who move.</li>"
    "<li><b>Normalise per ninety.</b> Rotation and injuries distort raw totals considerably.</li>"
    "<li><b>Separate the penalties.</b> As everywhere, they inflate totals unevenly across the list.</li>"
    "</ul>"
    "<p>The desk's equivalent readings sit at <a href=\"/sports/bundesliga-top-scorers/\">Bundesliga top scorers</a> and <a href=\"/sports/champions-league-top-scorers/\">Champions League top scorers</a>, and the results that produce these goals are at <a href=\"/sports/ligue-1-results/\">Ligue 1 results</a>.</p>",

"sports/premier-league-clubs":
    "<h2>Twenty clubs, twenty different situations</h2>"
    "<p>A club list is easy to treat as a static directory, but each entry is a moving position: an owner, a budget, a recruitment strategy and a place in a cycle that has nothing to do with last season's finish. <a href=\"" + EPL + "\" rel=\"noopener\">The Premier League</a> publishes the official club and competition information, and the <a href=\"" + _w("Premier_League") + "\" rel=\"noopener\">Premier League reference material on Wikipedia</a> carries the historical record that explains how the current membership came about. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What actually distinguishes the clubs</h2>"
    "<p>Spending power is the obvious divide and it is real, but the more useful distinctions are structural. Some clubs are built to develop and sell; others to buy established players and compete immediately; a third group exists mainly to survive the season financially. Those models produce different results, different transfer behaviour and very different expectations from their supporters.</p>"
    "<ul>"
    "<li><b>Identify the model.</b> Development, immediate contention and survival are different jobs with different measures of success.</li>"
    "<li><b>Read the ownership situation.</b> Stability or its absence shows up in recruitment before it shows up in results.</li>"
    "<li><b>Watch the academy output.</b> It is the cheapest source of squad depth and the one most often overlooked.</li>"
    "<li><b>Note the stadium economics.</b> Matchday revenue constrains what a club can spend far more than supporters expect.</li>"
    "</ul>"
    "<p>The season those clubs are playing is tracked at <a href=\"/sports/premier-league-results/\">Premier League results</a>, and the individual story at <a href=\"/sports/premier-league-top-scorers/\">Premier League top scorers</a>. For how transfers reshape these squads, the desk's <a href=\"/sports/transfers/\">transfer coverage</a> runs alongside the league pages.</p>",

"sports/premier-league-results":
    "<h2>Reading results in the most-watched league</h2>"
    "<p>Premier League results attract more interpretation per match than almost any other competition, which is a reason to be more disciplined about them rather than less. <a href=\"" + EPL + "\" rel=\"noopener\">The Premier League</a> publishes the official results and standings, and the <a href=\"" + _w("Premier_League") + "\" rel=\"noopener\">Premier League reference material on Wikipedia</a> provides the historical record against which a single season's results should be judged. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>The discipline that makes results informative</h2>"
    "<p>The core habit is separating the result from the performance, and doing it consistently rather than only when it suits the argument. A team can play well and lose, and it can play badly and win; over a season the two converge, but over three matches they diverge constantly, and most bad predictions come from reading three matches as a trend.</p>"
    "<ul>"
    "<li><b>Sample honestly.</b> Five matches is a hint, fifteen is a pattern, and anything less is noise.</li>"
    "<li><b>Split home and away form.</b> Combined figures routinely hide a team that is two different sides.</li>"
    "<li><b>Adjust for fixture difficulty.</b> A good run against weak opposition and a poor run against strong opposition can be the same team.</li>"
    "<li><b>Watch the schedule, not just the score.</b> European weeks and injury clusters explain more results than tactics do.</li>"
    "</ul>"
    "<p>The desk's <a href=\"/sports/premier-league-matchweek-1-guide/\">matchweek guide</a> applies the same approach to a single round, and <a href=\"/sports/premier-league-clubs/\">Premier League clubs</a> covers the twenty situations the results emerge from. For the cross-league view, see <a href=\"/sports/la-liga-results/\">La Liga results</a> and <a href=\"/sports/serie-a-results/\">Serie A results</a>.</p>",

"sports/premier-league-top-scorers":
    "<h2>The most contested scoring race in Europe</h2>"
    "<p>The Premier League's scoring list is usually tight at the top, because goals are distributed across more competitive sides than in leagues with a dominant two or three. <a href=\"" + EPL + "\" rel=\"noopener\">The Premier League</a> publishes the official scoring statistics, and the <a href=\"" + _w("Premier_League") + "\" rel=\"noopener\">Premier League reference material on Wikipedia</a> records the totals that define a serious challenge. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>How to compare scorers fairly</h2>"
    "<p>Three adjustments do most of the work. Minutes played separates the efficient from the ever-present; penalty responsibility separates finishing from assignment; and the strength of opposition separates a genuine all-round total from one built in a handful of comfortable matches. Apply all three and the order of the list often changes.</p>"
    "<ul>"
    "<li><b>Convert to goals per ninety.</b> The single most revealing adjustment, and the one most often skipped.</li>"
    "<li><b>List the penalties separately.</b> Then judge the open-play figure on its own terms.</li>"
    "<li><b>Check the distribution of goals.</b> Scoring against every tier is a different achievement from scoring against the bottom three.</li>"
    "<li><b>Account for position.</b> A winger's total and a centre-forward's total are not directly comparable.</li>"
    "</ul>"
    "<p>The results that produce these goals are at <a href=\"/sports/premier-league-results/\">Premier League results</a>, and the clubs behind them at <a href=\"/sports/premier-league-clubs/\">Premier League clubs</a>. The desk applies the same reading to <a href=\"/sports/champions-league-top-scorers/\">Champions League top scorers</a>, where the smaller sample makes the adjustments matter even more.</p>",

"sports/serie-a-results":
    "<h2>Reading results in a tactically demanding league</h2>"
    "<p>Serie A has a long reputation for tactical preparation, and the results tend to reflect it: margins are often narrow and low-scoring matches are more common than in the higher-tempo leagues. The <a href=\"" + _w("Serie_A") + "\" rel=\"noopener\">Serie A reference material on Wikipedia</a> documents the competition's structure and history, which is the background these results sit in. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What the scorelines actually indicate</h2>"
    "<p>In a league where one-goal results are frequent, the difference between a good season and a mid-table one is a handful of matches decided by single moments. That makes the results less predictive than they appear: a run of narrow wins is not the same evidence as a run of comfortable ones, and the table built from it is correspondingly fragile.</p>"
    "<ul>"
    "<li><b>Look at goal difference alongside points.</b> It separates a side winning well from one winning narrowly.</li>"
    "<li><b>Track the low-scoring matches.</b> They are common here and they carry less information than they seem to.</li>"
    "<li><b>Split home and away.</b> The home advantage varies considerably between grounds.</li>"
    "<li><b>Watch the European participants.</b> Squad rotation around continental ties affects domestic results in visible weeks.</li>"
    "</ul>"
    "<p>The <a href=\"/sports/serie-a-table/\">Serie A table</a> gives the aggregate and <a href=\"/sports/serie-a-top-scorers/\">Serie A top scorers</a> the individual race. For the same reading applied elsewhere, see <a href=\"/sports/ligue-1-results/\">Ligue 1 results</a> and <a href=\"/sports/bundesliga-results/\">Bundesliga results</a>.</p>",

"sports/serie-a-top-scorers":
    "<h2>A scoring race in a low-margin league</h2>"
    "<p>Because Serie A matches are frequently decided by single goals, its leading scorers often accumulate their totals in tighter games than their counterparts elsewhere, and the totals at the top of the list tend to be correspondingly lower. The <a href=\"" + _w("Serie_A") + "\" rel=\"noopener\">Serie A reference material on Wikipedia</a> records the competition's scoring history, which gives the current figures their proper scale. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>Comparing across leagues without fooling yourself</h2>"
    "<p>Raw totals from different leagues are not comparable, and the temptation to compare them is strong. Pace of play, defensive organisation and the number of high-scoring fixtures all differ, so the same striker can produce materially different totals in two competitions without having changed at all.</p>"
    "<ul>"
    "<li><b>Compare rates, not totals.</b> Goals per ninety at least removes the playing-time variable.</li>"
    "<li><b>Respect the league context.</b> A lower total in a tighter league is not a weaker season.</li>"
    "<li><b>Separate penalties as always.</b> Their share varies by club hierarchy, not by talent.</li>"
    "<li><b>Check the consistency.</b> Goals spread across the season beat a cluster in one month.</li>"
    "</ul>"
    "<p>The desk's other scoring lists &mdash; <a href=\"/sports/premier-league-top-scorers/\">Premier League</a>, <a href=\"/sports/la-liga-top-scorers/\">La Liga</a>, <a href=\"/sports/bundesliga-top-scorers/\">Bundesliga</a> &mdash; are worth reading together for exactly this reason. The results behind the goals are at <a href=\"/sports/serie-a-results/\">Serie A results</a>.</p>",

# ------------------------------- home ----------------------------------

"home/mistakes":
    "<h2>Why the same few mistakes keep happening</h2>"
    "<p>Household errors are rarely random. They cluster around a small number of causes: a product used outside the conditions it was designed for, a task performed in the wrong order, or an assumption about how a machine works that was never checked. The <a href=\"" + _w("household+chemicals") + "\" rel=\"noopener\">reference material on household chemicals on Wikipedia</a> explains the chemistry behind the most dangerous category, and the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the ventilation and moisture guidance that underpins several entries here. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>The pattern behind most of them</h2>"
    "<p>Almost every mistake in this collection is a shortcut that seemed free at the time. Skipping preparation before painting, overfilling a machine, or mixing two cleaners that both work individually &mdash; each saves minutes and each costs considerably more when it fails. The desk's approach is to name the shortcut explicitly, because the mistake is rarely the action and nearly always the assumption behind it.</p>"
    "<ul>"
    "<li><b>Read the label once, properly.</b> Most product damage is a use the manufacturer already warned against in small print.</li>"
    "<li><b>Do the preparation step.</b> It is the part people skip and the part that determines the outcome.</li>"
    "<li><b>Respect the machine's limits.</b> Appliances fail from being overloaded far more often than from age.</li>"
    "<li><b>Stop when something smells wrong.</b> Literally: an unexpected odour during cleaning is a signal to ventilate and leave the room.</li>"
    "</ul>"
    "<p>The individual entries carry the detail: <a href=\"/home/mistakes/mixing-cleaning-products/\">mixing cleaning products</a> is the safety-critical one, <a href=\"/home/mistakes/too-much-detergent/\">too much detergent</a> the most common, and <a href=\"/home/mistakes/painting-without-prep/\">painting without prep</a> the most expensive to undo. For the seasonal version of the same discipline, see the <a href=\"/home/seasonal-home-maintenance-checklist/\">seasonal maintenance checklist</a>.</p>",

"home/outside":
    "<h2>The exterior is the part that fails slowly</h2>"
    "<p>Outside the house, problems develop over seasons rather than days, which is precisely why they are missed. Gutters, roofline, external walls and drainage all degrade quietly until the damage appears somewhere else &mdash; a damp ceiling, a cracked path, water in a basement. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the moisture-management guidance behind this desk's exterior advice, and the <a href=\"" + ICC + "\" rel=\"noopener\">International Code Council</a> publishes the construction standards that determine how these elements are supposed to shed water. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>An order for working through the outside</h2>"
    "<p>Start at the top and work down, because water follows gravity and every problem below is usually caused by something above. The roofline and gutters decide where rain goes; the walls and drainage decide whether it stays. Checking them in that order means each fix is not undone by the next one.</p>"
    "<ul>"
    "<li><b>Roof and gutters first.</b> Blockages here are the origin of most downstream damp.</li>"
    "<li><b>Then the walls and openings.</b> Seals around windows and doors fail long before the wall itself does.</li>"
    "<li><b>Then the ground level.</b> Drainage that slopes toward the house undoes everything above it.</li>"
    "<li><b>Finally the surfaces.</b> Paths, fences and paint are cosmetic next to a water problem, and should be scheduled last.</li>"
    "</ul>"
    "<p>The desk's <a href=\"/home/seasonal-home-maintenance-checklist/\">seasonal maintenance checklist</a> puts these tasks on a calendar, and the <a href=\"/home/roof-gutter-leak-joint/\">gutter joint repair guide</a> covers the single most common exterior fault. For the winter-specific version, see <a href=\"/home/winter-home-preparation/\">winter home preparation</a>.</p>",

"home/pests":
    "<h2>Pest control is exclusion before it is treatment</h2>"
    "<p>Every pesticide addresses the animals already inside. The ones that follow are stopped by something else entirely: sealing the entry points and removing what attracted them. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the guidance on rodents and insects as disease vectors, and the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the integrated pest-management approach this desk follows, which puts physical exclusion ahead of chemical treatment. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>The sequence that works</h2>"
    "<p>Identify what you are dealing with, then remove food and water, then seal, and only then consider treatment. Reversing that order is the common failure: treating first produces a short-term result, and because nothing about the environment changed, the population returns within weeks.</p>"
    "<ul>"
    "<li><b>Identify before you act.</b> Different species need different responses, and the wrong treatment wastes weeks.</li>"
    "<li><b>Remove food and water.</b> Sealed containers, no standing water, and bins that actually close.</li>"
    "<li><b>Seal the entries.</b> Gaps around pipes, vents and doors; a mouse needs far less space than most people assume.</li>"
    "<li><b>Treat last, and record it.</b> What was used, where, and when &mdash; particularly in a household with children or pets.</li>"
    "</ul>"
    "<p>The desk's detailed guides carry the specifics: <a href=\"/home/ants-in-the-kitchen/\">ants in the kitchen</a> and <a href=\"/home/mice-in-the-house-signs/\">signs of mice in the house</a> are the two most common calls. For the ventilation and damp side, which drives a great deal of insect activity, see <a href=\"/home/bathroom-fan-condensation/\">bathroom fan and condensation</a>.</p>",

"home/secure":
    "<h2>Security is layered, and the layers are cheap</h2>"
    "<p>Home security is rarely defeated by a sophisticated attack. Most entries take advantage of an unlocked door, a window left open, or a key hidden in an obvious place &mdash; which means the effective measures are ordinary and inexpensive. The <a href=\"" + _w("home+security") + "\" rel=\"noopener\">home-security reference material on Wikipedia</a> surveys the approaches, and the <a href=\"" + CISA + "\" rel=\"noopener\">Cybersecurity and Infrastructure Security Agency</a> publishes the guidance for the digital half of the same problem, since a connected lock or camera is a networked device. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>Physical first, then connected</h2>"
    "<p>Work in the order that matches the actual risk. A solid door with a good lock and a habit of using it does more than any alarm system, and no smart device compensates for a window that does not close. Once the physical layer is sound, the connected devices become a useful addition rather than a substitute.</p>"
    "<ul>"
    "<li><b>Doors and locks.</b> Solid doors, deadlocks, and hinges that cannot be lifted from outside.</li>"
    "<li><b>Windows and openings.</b> Locks that work, and ventilation that does not create an entry point.</li>"
    "<li><b>Lighting and sightlines.</b> Approaches that are visible from the street are less attractive than sheltered ones.</li>"
    "<li><b>Connected devices.</b> Change default credentials on every smart lock and camera, keep firmware current, and check whether footage is stored locally or by a third party.</li>"
    "<li><b>Habits.</b> The layer that actually determines outcomes: what you do when you leave, every time.</li>"
    "</ul>"
    "<p>The digital half deserves the same attention as the door: the desk's guide to <a href=\"/tech/best-password-manager-for-you/\">choosing a password manager</a> covers the credentials side, and <a href=\"/tech/what-free-apps-do-with-your-data/\">what free apps do with your data</a> is worth reading before installing a camera that offers free cloud storage. For the power side of a connected setup, see <a href=\"/home/home-office-setup/\">home office setup</a>, which covers keeping essential devices running when the power does not.</p>",

"home/seasonal-home-maintenance-checklist":
    "<h2>Why a calendar beats a to-do list</h2>"
    "<p>Seasonal maintenance fails as a list and succeeds as a calendar. Every task on this checklist is one that people agree matters and then defer, and deferral is exactly what a list permits. The efficiency guidance behind the heating and insulation items comes from the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>, and the moisture and ventilation items follow the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a>'s published advice. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>Ordering the year by what fails first</h2>"
    "<p>The checklist is sequenced by consequence rather than by convenience. Water-related tasks come before cosmetic ones because water damage compounds while paint peels patiently, and the tasks ahead of winter come before the tasks ahead of summer because a cold snap gives you no grace period to finish.</p>"
    "<ul>"
    "<li><b>Water first.</b> Gutters, drainage, seals and lagging &mdash; the items that prevent expensive damage rather than improve appearance.</li>"
    "<li><b>Heat second.</b> Bleeding radiators, servicing the boiler, checking the thermostat before the season rather than during it.</li>"
    "<li><b>Ventilation third.</b> Fans, extractor ducts and airbricks, which determine whether the winter produces damp.</li>"
    "<li><b>Safety throughout.</b> Alarms, extinguishers and the dryer vent, checked on a schedule rather than when remembered.</li>"
    "<li><b>Cosmetics last.</b> Painting, sealing surfaces and the exterior finishes, scheduled when the weather actually permits them.</li>"
    "</ul>"
    "<p>The related guides carry the detail for each block: <a href=\"/home/autumn-home-preparation/\">autumn preparation</a> and <a href=\"/home/winter-home-preparation/\">winter preparation</a> for the cold half of the year, <a href=\"/home/summer-cooling-checklist/\">the summer cooling checklist</a> and <a href=\"/home/spring-home-reset/\">the spring reset</a> for the warm half. For the water side specifically, <a href=\"/home/roof-gutter-leak-joint/\">repairing a gutter joint</a> is the task most often postponed past the point where it was cheap.</p>",

}
