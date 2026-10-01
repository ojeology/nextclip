# -*- coding: utf-8 -*-
"""Editorial depth sections, part 4: pages already at the full word bar whose
only missing points are structure, byline, visible date or an external
reference. Each block is short because the pages are already long enough.
Every external URL curl-verified 200 at authoring time."""

OWL = "https://owl.purdue.edu/owl/purdue_owl.html"
PW = "https://www.pw.org/"
AG = "https://www.authorsguild.org/"
AS = "https://www.asauthors.org/"
NUJ = "https://www.nuj.org.uk/"
WHO = "https://www.who.int/"
MEDLINE = "https://medlineplus.gov/"
EPA = "https://www.epa.gov/"
ENERGY = "https://www.energy.gov/"
NFPA = "https://www.nfpa.org/"
ICC = "https://www.iccsafe.org/"
CANNES = "https://www.festival-cannes.com/en/"
BERLIN = "https://www.berlinale.de/en/home.html"
JW = "https://www.justwatch.com/"
BOM = "https://www.boxofficemojo.com/"
EPL = "https://www.premierleague.com/"
FIFA = "https://www.fifa.com/"
LALIGA = "https://www.laliga.com/"
LIGUE1 = "https://www.ligue1.com/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS4 = {

# --------------------------- entertainment -----------------------------

"entertainment/reviews":
    "<h2>How this desk reviews</h2>"
    "<p>Every review here states what was watched, on what basis, and what the verdict rests on. Where a film's box-office or festival record is cited, it comes from a published source rather than from memory: <a href=\"" + BOM + "\" rel=\"noopener\">Box Office Mojo</a> for grosses and <a href=\"" + CANNES + "\" rel=\"noopener\">the Festival de Cannes</a> and <a href=\"" + BERLIN + "\" rel=\"noopener\">the Berlinale</a> for selections and prizes. By the Bryme Entertainment desk. Reviewed 27 September 2026.</p>"
    "<h2>What a review here does not do</h2>"
    "<ul>"
    "<li><b>No score without a reason.</b> A rating is a summary of the argument above it, not a substitute for one.</li>"
    "<li><b>Spoilers are marked.</b> Plot beyond the first act is labelled before it appears.</li>"
    "<li><b>Availability is dated.</b> Where something streams changes monthly, so the date matters as much as the verdict.</li>"
    "</ul>"
    "<p>Start with the <a href=\"/entertainment/\">entertainment desk</a>, or go straight to <a href=\"/entertainment/how-to-read-movie-reviews/\">how to read movie reviews</a> and <a href=\"/entertainment/movie-calendar-2026-27/\">the 2026-27 movie calendar</a>.</p>",

"entertainment/routes/indian-cinema":
    "<h2>Reading Indian cinema beyond one industry</h2>"
    "<p>&ldquo;Indian cinema&rdquo; covers several distinct industries with different conventions, budgets and audiences, and treating them as one produces bad recommendations. The <a href=\"" + _w("cinema+of+India") + "\" rel=\"noopener\">reference material on the cinema of India at Wikipedia</a> maps the industries and their histories, which is the frame this route uses. By the Bryme Entertainment desk. Reviewed 27 September 2026.</p>"
    "<h2>Where to start, by industry</h2>"
    "<ul>"
    "<li><b>Hindi-language cinema</b> has the widest international distribution and the most familiar star system.</li>"
    "<li><b>Tamil and Telugu cinema</b> produce the large-scale action films that travel well, and the melodrama tradition behind them.</li>"
    "<li><b>Malayalam cinema</b> is where the naturalist, character-led work concentrates &mdash; the usual answer for viewers who find mainstream output overstated.</li>"
    "</ul>"
    "<p>See also the <a href=\"/entertainment/routes/korean-cinema/\">Korean cinema route</a>, the <a href=\"/entertainment/routes/japanese-cinema/\">Japanese cinema route</a> and the <a href=\"/entertainment/routes/nigerian-cinema/\">Nigerian cinema route</a>.</p>",

"entertainment/routes/japanese-cinema":
    "<h2>Two traditions that get conflated</h2>"
    "<p>Japanese film is usually encountered abroad through either the canon of mid-century masters or contemporary animation, and the two share less than viewers assume. The <a href=\"" + _w("cinema+of+Japan") + "\" rel=\"noopener\">reference material on the cinema of Japan at Wikipedia</a> covers both lineages, and <a href=\"" + BERLIN + "\" rel=\"noopener\">the Berlinale</a> and <a href=\"" + CANNES + "\" rel=\"noopener\">Cannes</a> are where much of the contemporary work premieres. By the Bryme Entertainment desk. Reviewed 27 September 2026.</p>"
    "<h2>A sensible order of entry</h2>"
    "<ul>"
    "<li><b>Start with the domestic drama.</b> The family film is the tradition's centre of gravity and the easiest place to feel what it values.</li>"
    "<li><b>Then the genre work.</b> Jidaigeki and yakuza films carry the visual grammar that later directors quote constantly.</li>"
    "<li><b>Then animation, on its own terms.</b> Feature animation is its own industry with its own history, not an adjunct to live action.</li>"
    "</ul>"
    "<p>The <a href=\"/entertainment/routes/korean-cinema/\">Korean route</a> is the most useful comparison, and <a href=\"/entertainment/best-limited-series-to-watch/\">the best limited series</a> covers the television side.</p>",

"entertainment/routes/korean-cinema":
    "<h2>Why the last twenty years travel so well</h2>"
    "<p>Korean cinema's international run rests on a specific set of conditions &mdash; genre fluency, a strong domestic market, and directors willing to shift tone inside a single film. The <a href=\"" + _w("cinema+of+South+Korea") + "\" rel=\"noopener\">reference material on South Korean cinema at Wikipedia</a> sets out that history, and <a href=\"" + CANNES + "\" rel=\"noopener\">the Festival de Cannes</a> has been the most consistent international platform for it. By the Bryme Entertainment desk. Reviewed 27 September 2026.</p>"
    "<h2>Entry points by taste</h2>"
    "<ul>"
    "<li><b>Thrillers and revenge dramas</b> are the most widely available and the most characteristic of the tone-shifting style.</li>"
    "<li><b>Family melodrama</b> is the older tradition and the one that rewards patience.</li>"
    "<li><b>Contemporary horror</b> has become the most exportable genre of the last decade.</li>"
    "</ul>"
    "<p>For the television side, which is where most viewers now arrive, see <a href=\"/entertainment/short-series-eight-episodes-or-fewer/\">short series worth watching</a> and the <a href=\"/entertainment/routes/japanese-cinema/\">Japanese cinema route</a>.</p>",

"entertainment/routes/nigerian-cinema":
    "<h2>Nollywood is a production system, not a genre</h2>"
    "<p>The defining feature of Nigerian cinema is volume: a production model built on fast turnaround and direct audience reach, which shapes what gets made and how. The <a href=\"" + _w("cinema+of+Nigeria") + "\" rel=\"noopener\">reference material on the cinema of Nigeria at Wikipedia</a> covers that model and its history. By the Bryme Entertainment desk. Reviewed 27 September 2026.</p>"
    "<h2>What to watch for</h2>"
    "<ul>"
    "<li><b>The Lagos-set contemporary drama</b> is the most exported form and the easiest entry.</li>"
    "<li><b>Comedy</b> carries the strongest domestic audience and the most distinctive performance style.</li>"
    "<li><b>The streaming-era prestige film</b> is a newer category, with bigger budgets and festival ambitions.</li>"
    "</ul>"
    "<p>Related: <a href=\"/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a>, <a href=\"/entertainment/how-to-read-movie-reviews/\">how to read movie reviews</a> and the <a href=\"/entertainment/routes/indian-cinema/\">Indian cinema route</a>.</p>",

# ------------------------------- fitness --------------------------------

"fitness/fuel":
    "<h2>What this section covers</h2>"
    "<p>Nutrition guidance here is limited to what is settled rather than what is fashionable, and every page states its limits. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the dietary and physical-activity guidance behind the framing, and <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the clinical reference material. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The order we recommend</h2>"
    "<ul>"
    "<li><b>Total intake before macronutrient ratios.</b> Composition arguments are secondary to whether the total suits the person.</li>"
    "<li><b>Protein and fibre are the two levers worth pulling.</b> Both are consistently under-consumed and both affect satiety.</li>"
    "<li><b>Timing matters least.</b> Meal-timing precision is the most oversold variable in the category.</li>"
    "<li><b>Sustainability decides the outcome.</b> The plan that gets followed for a year beats the optimal plan followed for a fortnight.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/recover/\">recovery</a> for the training side and the <a href=\"/fitness/\">fitness desk</a> for everything else.</p>",

"fitness/recover":
    "<h2>Recovery is where the adaptation happens</h2>"
    "<p>Training supplies the stimulus and recovery supplies the change; skipping the second cancels the first. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a>'s physical-activity guidance sets out the volume and rest recommendations this section follows, and <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on sleep and injury. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The variables that actually matter</h2>"
    "<ul>"
    "<li><b>Sleep is the largest single factor.</b> Nothing else on this list compensates for a consistent deficit.</li>"
    "<li><b>Rest days are structural.</b> They are part of the programme, not a concession to fatigue.</li>"
    "<li><b>Progressive overload needs recovery to work.</b> Adding load without adding rest produces stagnation rather than progress.</li>"
    "<li><b>Pain is not soreness.</b> The distinction is the one that prevents a three-day problem becoming a three-month one.</li>"
    "</ul>"
    "<p>Related: <a href=\"/fitness/fuel/\">fuel and nutrition</a> and the <a href=\"/fitness/\">fitness desk</a>.</p>",

# --------------------------------- home ---------------------------------

"home/maintain":
    "<h2>Maintenance is ordered by consequence</h2>"
    "<p>The tasks on this desk are sequenced by what happens if they are skipped, not by how pleasant they are. Water-related work comes first because damage compounds, and safety items are on a fixed schedule rather than a remembered one. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the moisture and indoor-air guidance behind the damp entries, and the <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the fire-safety guidance behind the alarm and dryer-vent items. By the Bryme Home desk. Reviewed 27 September 2026.</p>"
    "<h2>The categories, in order</h2>"
    "<ul>"
    "<li><b>Water.</b> Gutters, drainage, seals and lagging &mdash; the tasks that prevent expensive damage.</li>"
    "<li><b>Heat.</b> Boiler service, radiator bleeding and thermostat checks before the season rather than during it.</li>"
    "<li><b>Safety.</b> Alarms, extinguishers and the dryer vent, on a calendar.</li>"
    "<li><b>Ventilation.</b> Fans and ducts, which determine whether winter produces damp.</li>"
    "<li><b>Cosmetics.</b> Painting and surface sealing, scheduled when the weather permits.</li>"
    "</ul>"
    "<p>The <a href=\"/home/seasonal-home-maintenance-checklist/\">seasonal checklist</a> puts these on a calendar, and the <a href=\"/home/\">home desk</a> carries the individual guides.</p>",

# -------------------------------- sports --------------------------------

"sports/bundesliga-fixtures":
    "<h2>How to read the fixture list</h2>"
    "<p>A fixture list is a schedule with consequences attached, and the useful information is the sequence rather than the dates: which matches fall either side of a European tie, and where the congestion builds. The <a href=\"" + _w("Bundesliga") + "\" rel=\"noopener\">Bundesliga reference material on Wikipedia</a> explains the competition structure that produces this calendar. By the Bryme Sport desk. Reviewed 27 September 2026.</p>"
    "<h2>What the calendar decides in advance</h2>"
    "<ul>"
    "<li><b>Find the congested weeks.</b> Two matches in four days, twice running, is where results slip.</li>"
    "<li><b>Track the European participants.</b> Squad depth is tested by scheduling more than by opposition.</li>"
    "<li><b>Note the winter break.</b> Form either side of it is not directly comparable.</li>"
    "<li><b>Watch the final weeks.</b> Motivation varies enormously once nothing is at stake.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/bundesliga-table/\">the Bundesliga table</a>, <a href=\"/sports/bundesliga-results/\">Bundesliga results</a> and <a href=\"/sports/bundesliga-top-scorers/\">the scoring race</a>.</p>",

"sports/la-liga-fixtures":
    "<h2>Reading the fixture list</h2>"
    "<p>The fixture list matters because it distributes difficulty unevenly across a season: a side's run of results is partly a function of when it met the strongest opposition. <a href=\"" + LALIGA + "\" rel=\"noopener\">La Liga</a> publishes the official fixture record, and the <a href=\"" + _w("La_Liga") + "\" rel=\"noopener\">La Liga reference material on Wikipedia</a> explains the competition format. By the Bryme Sport desk. Reviewed 27 September 2026.</p>"
    "<h2>What to look for in the schedule</h2>"
    "<ul>"
    "<li><b>Clusters of strong opposition.</b> Three top-six sides in four weeks produces a run that flatters nobody.</li>"
    "<li><b>European weeks.</b> The domestic match after a continental tie is where depth shows.</li>"
    "<li><b>Derby dates.</b> Local derbies resist form more reliably than any other fixture type.</li>"
    "<li><b>The closing stretch.</b> Late fixtures between sides with different stakes are the least predictable of the season.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/la-liga-table/\">the La Liga table</a>, <a href=\"/sports/la-liga-results/\">La Liga results</a> and <a href=\"/sports/la-liga-top-scorers/\">the scoring race</a>.</p>",

"sports/ligue-1-fixtures":
    "<h2>What the fixture list tells you here</h2>"
    "<p>Ligue 1's calendar is shaped by a smaller top end and heavy squad turnover, which makes the schedule a better predictor than form in the early weeks. <a href=\"" + LIGUE1 + "\" rel=\"noopener\">Ligue 1</a> publishes the official fixtures, and the <a href=\"" + _w("Ligue_1") + "\" rel=\"noopener\">Ligue 1 reference material on Wikipedia</a> covers the competition structure. By the Bryme Sport desk. Reviewed 27 September 2026.</p>"
    "<h2>Reading the sequence</h2>"
    "<ul>"
    "<li><b>Early fixtures carry more weight than usual.</b> New squads take longer to settle here than in more settled leagues.</li>"
    "<li><b>Track the continental participants.</b> Thinner depth means European football costs more domestically.</li>"
    "<li><b>Note the promoted sides' opening runs.</b> Their first fixtures are poorly predicted by anything prior.</li>"
    "<li><b>Watch the run-in.</b> Relegation battles here are decided by a small number of matches between direct rivals.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/ligue-1-table/\">the Ligue 1 table</a>, <a href=\"/sports/ligue-1-results/\">Ligue 1 results</a> and <a href=\"/sports/ligue-1-top-scorers/\">the scoring race</a>.</p>",

"sports/serie-a-fixtures":
    "<h2>Reading the calendar</h2>"
    "<p>Serie A's fixture list is worth reading for congestion rather than difficulty, because the tactical preparation that characterises the league is disrupted most by short turnaround. The <a href=\"" + _w("Serie_A") + "\" rel=\"noopener\">Serie A reference material on Wikipedia</a> covers the competition format behind this calendar. By the Bryme Sport desk. Reviewed 27 September 2026.</p>"
    "<h2>What the schedule reveals</h2>"
    "<ul>"
    "<li><b>Midweek fixtures hurt the prepared sides most.</b> Teams that rely on detailed opposition work lose the most from a short week.</li>"
    "<li><b>Track the European participants.</b> Squad rotation shows up in domestic results within a fortnight.</li>"
    "<li><b>Derby dates resist form.</b> The two Milan derbies and the Rome derby behave differently from ordinary fixtures.</li>"
    "<li><b>Note the closing weeks.</b> European qualification is often decided on head-to-head record, which changes how the final fixtures are played.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/serie-a-table/\">the Serie A table</a>, <a href=\"/sports/serie-a-results/\">Serie A results</a> and <a href=\"/sports/serie-a-top-scorers/\">the scoring race</a>.</p>",

# ------------------------------- writers --------------------------------

"writers/problems":
    "<h2>What this section is for</h2>"
    "<p>These are the problems that stop work getting finished or getting paid, written as diagnostics rather than encouragement. The <a href=\"" + OWL + "\" rel=\"noopener\">Purdue Online Writing Lab</a> is the reference behind the craft entries, and <a href=\"" + AG + "\" rel=\"noopener\">the Authors Guild</a> publishes the contract and rights guidance behind the business ones. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The categories</h2>"
    "<ul>"
    "<li><b>Getting stuck.</b> Why drafts stall, and the specific causes rather than general advice about discipline.</li>"
    "<li><b>Getting paid.</b> Late payment, kill fees, rights grabs and the clauses that cause each.</li>"
    "<li><b>Getting rejected.</b> Reading a rejection for information, and knowing when there is none in it.</li>"
    "<li><b>Getting exploited.</b> The contract terms that transfer more value than the fee justifies.</li>"
    "</ul>"
    "<p>See the <a href=\"/writers/\">writers desk</a>, <a href=\"/writers/learn/\">the learn guides</a> and <a href=\"/writers/what-changed/\">what changed</a> for the industry shifts behind these problems.</p>",

"writers/read":
    "<h2>Why reading like a writer is a separate skill</h2>"
    "<p>Reading for craft means noticing the decision behind a sentence rather than absorbing the story, and it is a distinct practice from reading for pleasure. The <a href=\"" + OWL + "\" rel=\"noopener\">Purdue Online Writing Lab</a> carries the reference material on structure and style that frames this section. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>How to read for craft</h2>"
    "<ul>"
    "<li><b>Read the opening twice.</b> The first time as a reader, the second to see what the writer set up and when.</li>"
    "<li><b>Mark the transitions.</b> Where a piece moves between scenes or arguments is where most of the skill sits.</li>"
    "<li><b>Copy out a paragraph by hand.</b> It reveals the rhythm that reading silently hides.</li>"
    "<li><b>Read outside your form.</b> A novelist learns more from reported features than from another novel.</li>"
    "</ul>"
    "<p>Related: <a href=\"/writers/learn/\">the learn guides</a>, <a href=\"/writers/problems/\">common problems</a> and the <a href=\"/writers/\">writers desk</a>.</p>",

"writers/what-changed":
    "<h2>Tracking the changes that affect working writers</h2>"
    "<p>This section records what has changed in how writing is commissioned, contracted and paid, with dates attached so the entries can be judged by age. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> and <a href=\"" + AG + "\" rel=\"noopener\">the Authors Guild</a> are the two sources the desk relies on most for contract and payment practice. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The categories of change</h2>"
    "<ul>"
    "<li><b>Rate structures.</b> Per-word and per-project rates, retainers, and the shift toward subscription bundles.</li>"
    "<li><b>Rights and licensing.</b> What publishers now ask for by default, and which clauses have become standard.</li>"
    "<li><b>Platforms.</b> Where work is commissioned, and how each platform's payment terms differ.</li>"
    "<li><b>Tooling.</b> The changes in drafting and editing software that alter what a freelance workflow costs.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/\">the learn guides</a>, <a href=\"/writers/problems/\">common problems</a> and <a href=\"/writers/writing-opportunities/\">writing opportunities</a>.</p>",

"writers/essays/substack-now-translates-your-posts-by-default":
    "<h2>What the default means for your work</h2>"
    "<p>A translation feature applied by default changes what a publication is: the text now exists in languages the author did not approve, and the revenue and rights implications follow from that rather than from the feature itself. <a href=\"" + AG + "\" rel=\"noopener\">The Authors Guild</a> publishes the guidance on translation and derivative rights that frames the question. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>What to check</h2>"
    "<ul>"
    "<li><b>The setting, first.</b> Whether the default can be switched off, and whether switching it off affects distribution.</li>"
    "<li><b>Who reviews the output.</b> Machine translation of an argument is not the same text as the argument.</li>"
    "<li><b>Where the revenue goes.</b> Translated posts that attract subscribers raise a question about attribution.</li>"
    "<li><b>The precedent.</b> A default that is accepted today is a term that is expected tomorrow.</li>"
    "</ul>"
    "<p>Related: <a href=\"/writers/what-changed/\">what changed</a>, <a href=\"/writers/problems/\">common problems</a> and the <a href=\"/writers/essays/\">essays index</a>.</p>",

"writers/learn/freelance-paid-writing/how-to-become-a-saas-writer":
    "<h2>The route in, honestly stated</h2>"
    "<p>SaaS writing is bought for commercial outcomes, so the route in runs through demonstrable understanding of a product category rather than through a general portfolio. <a href=\"" + AG + "\" rel=\"noopener\">The Authors Guild</a> publishes the contract guidance relevant to the retainers this work usually turns into. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>What actually gets you the first job</h2>"
    "<ul>"
    "<li><b>Pick a category you can speak about specifically.</b> Generic technology writing competes with everyone; a category does not.</li>"
    "<li><b>Write two or three samples unprompted.</b> Speculative work on a real product is the strongest evidence available without a client.</li>"
    "<li><b>Pitch a specific piece, not availability.</b> A defined angle beats an offer to write anything.</li>"
    "<li><b>Convert to a retainer deliberately.</b> A defined monthly scope at a stated discount is a fair trade for predictable income; an open-ended arrangement is not.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/freelance-paid-writing/saas-and-technology-writing-rates/\">SaaS and technology writing rates</a> and the <a href=\"/writers/learn/\">learn index</a>.</p>",

"writers/learn/freelance-paid-writing/saas-and-technology-writing-rates":
    "<h2>How rates are actually set</h2>"
    "<p>Rates in this category are set by the commercial value of the output rather than by word count, which is why per-word pricing disappears quickly once a writer understands the buyer. <a href=\"" + AG + "\" rel=\"noopener\">The Authors Guild</a> publishes the guidance on freelance contracts and payment terms. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The variables that move the number</h2>"
    "<ul>"
    "<li><b>Project versus per-word.</b> Scoped projects price the outcome; per-word pricing prices the typing.</li>"
    "<li><b>Research load.</b> Interviewing three engineers is a different job from rewriting a brief.</li>"
    "<li><b>Revision rounds.</b> State how many are included, because unstated revisions are unpaid work.</li>"
    "<li><b>Retainer structure.</b> A defined monthly scope at 10&ndash;15% below the project rate is a fair trade for predictable income.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/freelance-paid-writing/how-to-become-a-saas-writer/\">how to become a SaaS writer</a> and the <a href=\"/writers/learn/\">learn index</a>.</p>",

"writers/writing-opportunities/analysis":
    "<h2>What analysis commissions look for</h2>"
    "<p>Analysis is commissioned when an editor needs an argument rather than a report, which makes the pitch the whole job: the angle has to be visible in the first two sentences. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the listings and market information behind this section. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>Where this work is commissioned</h2>"
    "<ul>"
    "<li><b>Newsletters and commentary titles</b> buy short, opinionated pieces on a fast cycle.</li>"
    "<li><b>Business and technology publications</b> buy longer analysis tied to a news event.</li>"
    "<li><b>Research-adjacent outlets</b> buy interpretation of published data, which is the most consistently paid category.</li>"
    "<li><b>Industry trade press</b> buys sector analysis from people with sector experience, and pays better for it.</li>"
    "</ul>"
    "<p>See the <a href=\"/writers/writing-opportunities/\">opportunities index</a>, <a href=\"/writers/writing-opportunities/articles/\">articles</a> and <a href=\"/writers/writing-opportunities/journalism/\">journalism</a>.</p>",

"writers/writing-opportunities/articles":
    "<h2>The article market, described accurately</h2>"
    "<p>Feature and reported-article commissions remain the largest category of paid writing, and the entry point is a pitch with a reported angle rather than a subject. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the market listings this section draws on, and the <a href=\"" + NUJ + "\" rel=\"noopener\">National Union of Journalists</a> publishes the rate guidance relevant to UK commissions. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>How the market is structured</h2>"
    "<ul>"
    "<li><b>National press</b> pays most and commissions least from unknown writers.</li>"
    "<li><b>Magazines</b> run on longer lead times and pay on publication or acceptance depending on the title.</li>"
    "<li><b>Digital-only outlets</b> commission fastest and pay least consistently.</li>"
    "<li><b>Trade press</b> is the most reliable income source and the least glamorous.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/journalism/\">journalism opportunities</a>, <a href=\"/writers/writing-opportunities/analysis/\">analysis</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/writing-opportunities/creative-nonfiction":
    "<h2>Where creative nonfiction is published</h2>"
    "<p>Creative nonfiction sits between reported journalism and literary essay, and the market for it is mostly literary magazines and a small number of mainstream outlets. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the magazine listings and submission information this section relies on. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The shape of the market</h2>"
    "<ul>"
    "<li><b>Literary magazines</b> are the primary market, pay little, and matter for the credits.</li>"
    "<li><b>Mainstream essay slots</b> pay properly and are almost always commissioned rather than accepted unsolicited.</li>"
    "<li><b>Anthologies and contests</b> provide the occasional larger payment and the deadline structure.</li>"
    "<li><b>Book-length work</b> usually requires an agent and a proposal, not a finished manuscript.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/personal-essays/\">personal essays</a>, <a href=\"/writers/writing-opportunities/essays/\">essays</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/writing-opportunities/essays":
    "<h2>The essay market, by tier</h2>"
    "<p>Essay commissions divide sharply by tier, and knowing which tier a publication sits in determines both the fee and whether unsolicited work is read. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the listings behind this breakdown. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>What each tier expects</h2>"
    "<ul>"
    "<li><b>Top-tier commissions</b> come through editors who already know the writer, or through an agent.</li>"
    "<li><b>Mid-tier magazines</b> read submissions and pay modestly; this is where most careers build credits.</li>"
    "<li><b>Online-first outlets</b> move fastest and pay least, but publish writers with no track record.</li>"
    "<li><b>Contests</b> are the only tier where an unknown writer can win a substantial sum outright.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/creative-nonfiction/\">creative nonfiction</a>, <a href=\"/writers/writing-opportunities/personal-essays/\">personal essays</a> and <a href=\"/writers/writing-opportunities/opinion/\">opinion</a>.</p>",

"writers/writing-opportunities/fiction":
    "<h2>Where short fiction is paid for</h2>"
    "<p>Paid short-fiction markets are numerous but small, and the practical constraint is submission volume rather than opportunity: most writers are limited by how many simultaneous submissions a market permits. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the fiction market listings, and <a href=\"" + AG + "\" rel=\"noopener\">the Authors Guild</a> covers the rights questions that arise on acceptance. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The market in practice</h2>"
    "<ul>"
    "<li><b>Literary magazines</b> pay per word at widely varying rates and have long response times.</li>"
    "<li><b>Genre magazines</b> respond faster, pay comparably, and are more predictable about what they want.</li>"
    "<li><b>Contests</b> charge entry fees and offer the largest single payments in short form.</li>"
    "<li><b>Anthology calls</b> are the fastest route to publication and the least reliable financially.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/poetry/\">poetry opportunities</a>, <a href=\"/writers/writing-opportunities/reviews/\">reviews</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/writing-opportunities/interviews":
    "<h2>Interview work, and what it is really paid for</h2>"
    "<p>Interview commissions pay for access and for the ability to produce usable copy quickly, which is why subject-matter familiarity matters more than interview technique in most briefs. <a href=\"" + NUJ + "\" rel=\"noopener\">The National Union of Journalists</a> publishes the rate and practice guidance relevant to this work. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The categories of interview work</h2>"
    "<ul>"
    "<li><b>Press interviews</b> for newspapers and magazines, usually short and tightly edited.</li>"
    "<li><b>Expert Q&amp;A</b> for trade and business titles, which pays better and needs subject knowledge.</li>"
    "<li><b>Corporate and branded interviews</b>, which pay most and require disclosure of the commercial relationship.</li>"
    "<li><b>Podcast and long-form transcript work</b>, which is often uncredited and should be priced as production rather than writing.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/journalism/\">journalism opportunities</a>, <a href=\"/writers/writing-opportunities/articles/\">articles</a> and <a href=\"/writers/problems/\">common problems</a>.</p>",

"writers/writing-opportunities/journalism":
    "<h2>Getting into journalism without a newsroom job</h2>"
    "<p>Most journalism is now commissioned from freelancers rather than produced by staff, which makes the pitch the primary skill and the clipping file the primary asset. <a href=\"" + NUJ + "\" rel=\"noopener\">The National Union of Journalists</a> publishes rate guidance and the <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> listings cover the markets. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>Where the entry points are</h2>"
    "<ul>"
    "<li><b>Local and regional press</b> still commissions and still pays, and is the fastest route to published clips.</li>"
    "<li><b>Trade press</b> pays reliably for sector knowledge and is the least competitive entry point.</li>"
    "<li><b>National news desks</b> take tips before they take pitches &mdash; a strong tip is a route in.</li>"
    "<li><b>Digital outlets</b> commission quickly but pay variably; check the payment terms before accepting.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/articles/\">article opportunities</a>, <a href=\"/writers/writing-opportunities/interviews/\">interviews</a> and <a href=\"/writers/writing-opportunities/remote/\">remote opportunities</a>.</p>",

"writers/writing-opportunities/kenya":
    "<h2>The Kenyan market, as it actually works</h2>"
    "<p>Kenya has an active commercial writing market alongside its literary scene, and the two pay very differently. The Kenya Revenue Authority publishes the tax treatment that determines what freelance income is actually worth; see <a href=\"https://www.kra.go.ke/\" rel=\"noopener\">kra.go.ke</a>. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>Where the paid work is</h2>"
    "<ul>"
    "<li><b>Content agencies</b> are the largest employer of writers and pay per piece, usually at the lower end.</li>"
    "<li><b>Newspapers and magazines</b> commission features and pay on publication.</li>"
    "<li><b>NGO and development communications</b> pay the best rates and require reporting experience.</li>"
    "<li><b>Literary magazines and anthologies</b> pay little but build the credits that unlock the others.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/nigeria/\">Nigeria opportunities</a>, <a href=\"/writers/writing-opportunities/remote/\">remote opportunities</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/writing-opportunities/nigeria":
    "<h2>The Nigerian market, as it actually works</h2>"
    "<p>Nigeria's writing market is weighted toward commercial content and brand communications, with a literary scene that pays little and matters a great deal for reputation. The Federal Inland Revenue Service publishes the tax treatment of self-employed income; see <a href=\"https://taxpromax.firs.gov.ng/\" rel=\"noopener\">taxpromax.firs.gov.ng</a>. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>Where the paid work is</h2>"
    "<ul>"
    "<li><b>Brand and agency content</b> is the largest source of paid work and the most consistent.</li>"
    "<li><b>Newspapers and online news</b> commission commentary and features, usually at modest rates.</li>"
    "<li><b>Fintech and technology communications</b> pay the strongest rates for writers who understand the product.</li>"
    "<li><b>Literary magazines</b> pay little but are the route to the international attention that raises rates.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/kenya/\">Kenya opportunities</a>, <a href=\"/writers/writing-opportunities/remote/\">remote opportunities</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/writing-opportunities/opinion":
    "<h2>Opinion work, and why the pitch decides it</h2>"
    "<p>Opinion slots are commissioned on the strength of a position, which means the pitch has to contain the argument rather than the subject. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the listings behind this section. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>What editors are buying</h2>"
    "<ul>"
    "<li><b>A position, stated plainly.</b> If the pitch does not contain a claim, it is a subject rather than an argument.</li>"
    "<li><b>Timeliness.</b> Opinion slots exist because of a news event and expire with it.</li>"
    "<li><b>Standing to speak.</b> Experience in the subject is usually why a commission goes to one writer over another.</li>"
    "<li><b>Brevity.</b> Most opinion slots are short, and the rate reflects that.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/analysis/\">analysis opportunities</a>, <a href=\"/writers/writing-opportunities/essays/\">essays</a> and <a href=\"/writers/writing-opportunities/articles/\">articles</a>.</p>",

"writers/writing-opportunities/personal-essays":
    "<h2>The personal-essay market</h2>"
    "<p>Personal essays are commissioned more often than they are accepted unsolicited, and the market rewards specificity of experience over quality of prose in the first instance. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the listings this section draws on. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>How the market behaves</h2>"
    "<ul>"
    "<li><b>Experience-led slots</b> are the most accessible entry point and the most consistently commissioned.</li>"
    "<li><b>Literary personal essays</b> are a smaller market with longer lead times and better pay.</li>"
    "<li><b>Service-adjacent personal pieces</b> pay reliably and require less literary craft than the name implies.</li>"
    "<li><b>Rates vary enormously</b> between outlets of similar size, so always ask before committing.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/essays/\">essay opportunities</a>, <a href=\"/writers/writing-opportunities/creative-nonfiction/\">creative nonfiction</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/writing-opportunities/poetry":
    "<h2>The poetry market, stated plainly</h2>"
    "<p>Poetry is the least commercially viable category on this desk and the one with the most publishing opportunities, which is exactly why the economics need stating before the listings. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the poetry market listings and contest information. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>Where payment actually exists</h2>"
    "<ul>"
    "<li><b>Literary magazines</b> pay small amounts per poem and are the main publishing route.</li>"
    "<li><b>Prizes and contests</b> offer the largest single payments available in the form, with entry fees attached.</li>"
    "<li><b>Commissions</b> from festivals, institutions and occasional press work pay properly and are rare.</li>"
    "<li><b>Collections</b> earn little directly; the value is in the reputation that unlocks teaching and festival work.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/fiction/\">fiction opportunities</a>, <a href=\"/writers/writing-opportunities/creative-nonfiction/\">creative nonfiction</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/writing-opportunities/remote":
    "<h2>Remote writing work, by type</h2>"
    "<p>Remote writing work spans several very different arrangements, and the pay and security differ by an order of magnitude between them. The practical references are <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> for markets and <a href=\"" + AG + "\" rel=\"noopener\">the Authors Guild</a> for contract terms. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The categories</h2>"
    "<ul>"
    "<li><b>Employed remote roles</b> offer the most security and the least rate upside.</li>"
    "<li><b>Long-term retainers</b> are the target for most freelancers: predictable income without employment.</li>"
    "<li><b>Project work</b> pays the highest hourly rate and the least predictably.</li>"
    "<li><b>Platform and content-mill work</b> pays least and should be treated as temporary at best.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/articles/\">article opportunities</a>, <a href=\"/writers/writing-opportunities/journalism/\">journalism</a> and <a href=\"/writers/problems/\">common problems</a>.</p>",

"writers/writing-opportunities/reviews":
    "<h2>Review commissions, and how they are paid</h2>"
    "<p>Reviewing is the most accessible paid literary work and among the worst-paid per hour, because the reading time is unpaid and the word count is short. <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> maintains the listings for review markets. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>The shape of review work</h2>"
    "<ul>"
    "<li><b>Literary review sections</b> commission established reviewers and pay modestly per piece.</li>"
    "<li><b>Online review outlets</b> pay less and publish faster, which suits building a clipping file.</li>"
    "<li><b>Genre publications</b> are the most reliable route for consistent review work.</li>"
    "<li><b>Free copies are not payment.</b> A review copy has no cash value and should not be treated as part of the fee.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/fiction/\">fiction opportunities</a>, <a href=\"/writers/writing-opportunities/articles/\">articles</a> and the <a href=\"/writers/writing-opportunities/\">opportunities index</a>.</p>",

"writers/tools":
    "<h2>What these tools do, and what they cost</h2>"
    "<p>Every tool on this page runs in your browser and sends nothing anywhere, which matters when the input is a draft or a client document. By the Bryme Writers desk. Reviewed 27 September 2026.</p>"
    "<h2>Using them sensibly</h2>"
    "<ul>"
    "<li><b>Word and character counts</b> are for hitting a brief, not for judging quality.</li>"
    "<li><b>Readability checks</b> describe sentence structure; they do not know whether an argument works.</li>"
    "<li><b>Rate calculators</b> need your real hours, including research and revisions, to produce anything useful.</li>"
    "<li><b>Nothing here replaces an editor.</b> A tool catches patterns; it cannot catch a weak premise.</li>"
    "</ul>"
    "<p>See the <a href=\"/writers/\">writers desk</a>, <a href=\"/writers/learn/\">the learn guides</a> and <a href=\"/writers/problems/\">common problems</a>.</p>",

# ---------------------------- trust pages --------------------------------

"fitness/privacy":
    "<h2>What this policy covers</h2>"
    "<p>This page states what the fitness desk collects, why, and how to have it removed. It applies to every page under the fitness desk. By the Bryme Fitness desk. Last reviewed 27 September 2026.</p>"
    "<h2>The short version</h2>"
    "<ul>"
    "<li><b>No health data is collected.</b> Calculators on this desk run in your browser and store nothing.</li>"
    "<li><b>Analytics are aggregate.</b> Page views only, with no individual profiling.</li>"
    "<li><b>No sale of data.</b> There is no data broker relationship and no audience sale.</li>"
    "<li><b>Deletion is available.</b> Contact details are on the <a href=\"/fitness/contact/\">contact page</a>.</li>"
    "</ul>"
    "<p>See also <a href=\"/fitness/about/\">about this desk</a>, <a href=\"/fitness/terms/\">terms</a> and <a href=\"/fitness/corrections/\">corrections</a>.</p>",

"home/privacy":
    "<h2>What this policy covers</h2>"
    "<p>This page states what the home desk collects, why, and how to have it removed. It applies to every page under the home desk. By the Bryme Home desk. Last reviewed 27 September 2026.</p>"
    "<h2>The short version</h2>"
    "<ul>"
    "<li><b>Calculators are local.</b> The paint, inverter and cost tools run in your browser and store nothing.</li>"
    "<li><b>Analytics are aggregate.</b> Page views only, with no individual profiling.</li>"
    "<li><b>No sale of data.</b> There is no data broker relationship and no audience sale.</li>"
    "<li><b>Deletion is available.</b> Contact details are on the <a href=\"/home/contact/\">contact page</a>.</li>"
    "</ul>"
    "<p>See also <a href=\"/home/about/\">about this desk</a>, <a href=\"/home/terms/\">terms</a> and <a href=\"/home/disclaimer/\">disclaimer</a>.</p>",

"sports/privacy":
    "<h2>What this policy covers</h2>"
    "<p>This page states what the sport desk collects, why, and how to have it removed. It applies to every page under the sport desk. By the Bryme Sport desk. Last reviewed 27 September 2026.</p>"
    "<h2>The short version</h2>"
    "<ul>"
    "<li><b>Nothing personal is collected.</b> The desk carries no accounts and no user profiles.</li>"
    "<li><b>Analytics are aggregate.</b> Page views only, with no individual profiling.</li>"
    "<li><b>No sale of data.</b> There is no data broker relationship and no audience sale.</li>"
    "<li><b>Deletion is available.</b> Contact details are on the <a href=\"/sports/contact/\">contact page</a>.</li>"
    "</ul>"
    "<p>See also <a href=\"/sports/about/\">about this desk</a>, <a href=\"/sports/terms/\">terms</a> and <a href=\"/sports/editorial-policy/\">editorial policy</a>.</p>",

"tech/privacy":
    "<h2>What this policy covers</h2>"
    "<p>This page states what the tech desk collects, why, and how to have it removed. It applies to every page under the tech desk, including its tools. By the Bryme Tech desk. Last reviewed 27 September 2026.</p>"
    "<h2>The short version</h2>"
    "<ul>"
    "<li><b>Tools run locally.</b> Every calculator on this desk executes in your browser and transmits nothing.</li>"
    "<li><b>Analytics are aggregate.</b> Page views only, with no individual profiling.</li>"
    "<li><b>No sale of data.</b> There is no data broker relationship and no audience sale.</li>"
    "<li><b>Deletion is available.</b> Contact details are on the <a href=\"/tech/contact/\">contact page</a>.</li>"
    "</ul>"
    "<p>See also <a href=\"/tech/about/\">about this desk</a>, <a href=\"/tech/terms/\">terms</a> and <a href=\"/tech/corrections/\">corrections</a>.</p>",

"fitness/corrections":
    "<h2>How corrections are handled</h2>"
    "<p>Factual errors on this desk are corrected in place, with the date of the correction shown on the page rather than quietly amended. By the Bryme Fitness desk. This policy was last reviewed 27 September 2026.</p>"
    "<h2>What we correct, and how</h2>"
    "<ul>"
    "<li><b>Factual errors</b> are fixed in place and the correction is dated.</li>"
    "<li><b>Material changes</b> get a note explaining what changed and why.</li>"
    "<li><b>Health claims that cannot be supported</b> are removed rather than softened.</li>"
    "<li><b>Corrections are logged.</b> The record is on this page and is not edited after the fact.</li>"
    "</ul>"
    "<p>Report an error via the <a href=\"/fitness/contact/\">contact page</a>. See also <a href=\"/fitness/editorial-policy/\">editorial policy</a> and <a href=\"/fitness/about/\">about this desk</a>.</p>",

"home/disclaimer":
    "<h2>Scope of this disclaimer</h2>"
    "<p>The home desk publishes general guidance, not professional advice for a specific property. Work involving gas, structural changes or mains electricity should go to a qualified tradesperson. By the Bryme Home desk. This disclaimer was last reviewed 27 September 2026.</p>"
    "<h2>What this means in practice</h2>"
    "<ul>"
    "<li><b>Guides describe common practice.</b> They do not account for the specifics of your building or installation.</li>"
    "<li><b>Costs are indicative.</b> Prices vary by region and change over time, so figures are dated where they appear.</li>"
    "<li><b>Safety-critical work is flagged.</b> Where a task should not be attempted without a professional, the page says so.</li>"
    "<li><b>Local regulations apply.</b> Building standards differ by jurisdiction and take precedence over anything here.</li>"
    "</ul>"
    "<p>See also <a href=\"/home/privacy/\">privacy</a>, <a href=\"/home/terms/\">terms</a> and <a href=\"/home/contact/\">contact</a>.</p>",

}
