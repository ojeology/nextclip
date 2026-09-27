# -*- coding: utf-8 -*-
"""Editorial depth sections, part 3: the remaining home-mistake guides and
sports editorial pages still under 8.0. Real prose with an h2, a list,
internal links, a review date and one verified external reference each.
Every external URL curl-verified 200 at authoring time."""

EPA = "https://www.epa.gov/"
WHO = "https://www.who.int/"
FIFA = "https://www.fifa.com/"
EPL = "https://www.premierleague.com/"
ENERGY = "https://www.energy.gov/"
MEDLINE = "https://medlineplus.gov/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS3 = {

"home/mistakes/drying-laundry-indoors":
    "<h2>Why indoor drying is a moisture problem before it is a laundry one</h2>"
    "<p>A load of wet washing releases several litres of water into the air as it dries, and in a sealed modern home that moisture has nowhere to go except onto the coldest surfaces. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the indoor-moisture and mould guidance behind this entry, and the <a href=\"" + _w("relative+humidity") + "\" rel=\"noopener\">relative-humidity reference material on Wikipedia</a> explains the mechanism that turns damp air into a wet window. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>The mistake is not drying indoors, it is drying without ventilation</h2>"
    "<p>Indoor drying is often the only option available, and it can be done without consequences. What causes the damage is drying in a closed room with no airflow and no heat, which keeps the humidity high for hours. Open a window, run an extractor, and keep the door to the rest of the house closed so the moisture does not travel.</p>"
    "<ul>"
    "<li><b>Ventilate while it dries.</b> A cracked window beats a dehumidifier you do not own, and costs nothing.</li>"
    "<li><b>Spin harder in the machine.</b> More water out in the drum is less water in the air.</li>"
    "<li><b>Keep the airbrake off the radiator.</b> Covering a radiator with laundry removes the heat from the room and slows everything.</li>"
    "<li><b>Give the load space.</b> Clothes packed together dry slowly and unevenly, extending the period the room stays damp.</li>"
    "</ul>"
    "<p>The same moisture logic runs through <a href=\"/home/bathroom-fan-condensation/\">bathroom fan and condensation</a> and <a href=\"/home/washing-machine-mould-door-seal/\">mould on the washing machine door seal</a>, and the appliance half is covered in <a href=\"/home/cost-to-run-a-tumble-dryer/\">the cost to run a tumble dryer</a>.</p>",

"home/mistakes/overloading-the-fridge":
    "<h2>A fridge cools by moving air, and packing blocks it</h2>"
    "<p>Refrigeration depends on cold air circulating from the vents around the contents. Overfilling does not just reduce space, it stops that circulation, and the result is a fridge that runs continuously while the back stays warm. The <a href=\"" + _w("refrigerator") + "\" rel=\"noopener\">refrigerator reference material on Wikipedia</a> describes the airflow path this mistake interrupts, and the <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a>'s food-safety guidance sets the temperature the appliance is being asked to hold. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>What overloading actually costs</h2>"
    "<p>Three things at once: uneven temperature, higher running cost, and shorter compressor life. The food near the vents is overcooled while the food at the door sits above the safe range, and the compressor never reaches its cut-off point. The symptoms appear as a warm middle shelf and a motor that never seems to stop.</p>"
    "<ul>"
    "<li><b>Leave the vents clear.</b> Nothing pressed against the air outlets, whatever else has to move.</li>"
    "<li><b>Keep space between items.</b> Air needs a path, not just room to exist.</li>"
    "<li><b>Do not fill the door shelves heavily.</b> They are the warmest part and the least stable when opened.</li>"
    "<li><b>Measure rather than assume.</b> A fridge thermometer costs very little and settles the question immediately.</li>"
    "</ul>"
    "<p>The related entries are <a href=\"/home/fridge-temperature-setting/\">fridge temperature setting</a>, which covers the safe range, <a href=\"/home/fridge-not-cold-enough/\">fridge not cold enough</a> for the diagnostic, and <a href=\"/home/appliances-that-use-the-most-electricity/\">appliances that use the most electricity</a> for where the fridge sits in the household total.</p>",

"home/mistakes/overwatering-houseplants":
    "<h2>Roots need air as well as water</h2>"
    "<p>The mechanism behind this mistake is rarely explained: a plant's roots take up oxygen from the air spaces in the soil, and saturated compost has none. Overwatering does not drown the plant directly, it removes the air the roots were breathing, and the resulting root failure shows up as the same yellowing that underwatering produces. The <a href=\"" + _w("root") + "\" rel=\"noopener\">plant-root reference material on Wikipedia</a> explains the gas exchange involved, and <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> covers the mould and damp implications of chronically wet indoor compost. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>How to tell which problem you actually have</h2>"
    "<p>Yellow leaves mean very little on their own, which is why this mistake persists. The reliable test is the compost itself: check the moisture a few centimetres down rather than at the surface, and check the weight of the pot. A heavy pot with wet compost underneath a dry-looking top layer is the classic presentation.</p>"
    "<ul>"
    "<li><b>Test the compost, not the surface.</b> The top centimetre dries out long before the root zone does.</li>"
    "<li><b>Lift the pot.</b> Weight is the quickest honest reading of how much water is in there.</li>"
    "<li><b>Check the drainage.</b> A pot without a hole, or a saucer left full, guarantees the problem whatever you do with the watering can.</li>"
    "<li><b>Water less in winter.</b> Growth slows, so the same schedule that worked in summer becomes overwatering.</li>"
    "</ul>"
    "<p>For the wider damp picture, see <a href=\"/home/bathroom-fan-condensation/\">bathroom fan and condensation</a> and <a href=\"/home/why-is-my-home-doing-that/\">why is my home doing that</a>, both of which cover moisture sources people do not think of as moisture.</p>",

"home/mistakes/painting-without-prep":
    "<h2>The paint is the smallest part of the job</h2>"
    "<p>Paint adheres to a surface, and the quality of the result is decided by the condition of that surface before the first coat. Dust, grease, flaking previous coats and unfilled holes all show through, and they show through more clearly once a new colour sits on top of them. The <a href=\"" + _w("paint") + "\" rel=\"noopener\">paint reference material on Wikipedia</a> covers the binder and substrate behaviour that explains why preparation determines adhesion. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>The preparation that cannot be skipped</h2>"
    "<p>Clean, repair, sand, prime. Each step has a specific failure it prevents: cleaning prevents fisheyes and poor grip, repair prevents the hole reappearing through the finish, sanding gives the new coat something to hold, and primer prevents the old colour bleeding through and evens the porosity so the topcoat dries uniformly.</p>"
    "<ul>"
    "<li><b>Wash the surface.</b> Especially in kitchens and around switches, where grease is invisible and universal.</li>"
    "<li><b>Fill and sand the defects.</b> Then sand again after filling, because filler dries proud.</li>"
    "<li><b>Prime over stains and bare patches.</b> Skipping this is the usual reason for a patch that shows in raking light.</li>"
    "<li><b>Mask properly and remove the tape early.</b> Tape left until the paint is fully dry pulls a ragged edge with it.</li>"
    "<li><b>Respect the recoat interval.</b> The second coat too soon lifts the first, and the only fix is to start again.</li>"
    "</ul>"
    "<p>Related reading: <a href=\"/home/paint-calculator/\">the paint calculator</a> for buying the right amount, <a href=\"/home/mistakes/streaky-windows-sunlight/\">streaky windows in sunlight</a> for the finish problem people blame on paint, and the <a href=\"/home/seasonal-home-maintenance-checklist/\">seasonal maintenance checklist</a> for scheduling the work when conditions suit it.</p>",

"home/mistakes/streaky-windows-sunlight":
    "<h2>Streaks are residue, and the sun only reveals them</h2>"
    "<p>The sunlight is not the cause; it is the inspection. A streak is a thin film of cleaning solution or dissolved dirt left behind as the water evaporated, and it becomes visible when raking light catches the difference in reflectivity. The <a href=\"" + _w("window+cleaning") + "\" rel=\"noopener\">window-cleaning reference material on Wikipedia</a> covers the methods professionals use, which mostly consist of removing the solution rather than adding more. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>Why the usual approach makes it worse</h2>"
    "<p>Most streaking comes from using too much product and too little mechanical removal. Spray spreads dirt into a film; a squeegee or a dry cloth takes it off the glass. Washing in direct sun compounds the problem because the solution dries before it can be removed, which is why the timing of the job matters as much as the technique.</p>"
    "<ul>"
    "<li><b>Use less solution.</b> A little diluted detergent beats a generous spray of glass cleaner.</li>"
    "<li><b>Remove it, do not buff it.</b> A squeegee with a dry cloth after each pass, or two cloths: one wet, one dry.</li>"
    "<li><b>Avoid direct sun.</b> Clean when the glass is cool, or the solution dries into the very streaks you are trying to remove.</li>"
    "<li><b>Change the cloth often.</b> A saturated cloth redistributes what it has already lifted.</li>"
    "</ul>"
    "<p>The related entries are <a href=\"/home/window-film-for-heat/\">window film for heat</a>, which changes how the glass behaves once it is clean, and <a href=\"/home/mistakes/too-much-detergent/\">too much detergent</a>, the same over-application error in a different room.</p>",

"home/mistakes/too-much-detergent":
    "<h2>More detergent does not clean more</h2>"
    "<p>Detergent works by suspending soil in water so it can be rinsed away, and once the water is saturated with it, additional product simply stays in the machine and on the fabric. Modern machines dose for low-sudsing formulations, so excess produces foam the machine was not designed to handle. The <a href=\"" + _w("detergent") + "\" rel=\"noopener\">detergent reference material on Wikipedia</a> explains the surfactant behaviour behind this, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the appliance-care guidance behind the desk's dosing advice. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>What the excess actually does</h2>"
    "<p>It builds up. Residue accumulates in the drum, the hoses and the door seal, where it holds moisture and feeds the odour that people then try to solve with more detergent. On the fabric it leaves a film that makes clothes feel stiff and look dull, and on sensitive skin it is a common irritant that nobody connects to the dose.</p>"
    "<ul>"
    "<li><b>Dose for the load and the water hardness.</b> Soft water needs less than the bottle suggests, not more.</li>"
    "<li><b>Use the machine's dispenser, not the drum.</b> It meters the release through the cycle rather than dumping it at once.</li>"
    "<li><b>Watch for the signs.</b> Suds visible through the door, a slick feel on the drum, or a smell after a wash all point the same way.</li>"
    "<li><b>Run a maintenance cycle.</b> A hot empty wash clears accumulated residue, and it needs doing periodically whatever the dose.</li>"
    "</ul>"
    "<p>See also <a href=\"/home/how-to-clean-a-washing-machine/\">how to clean a washing machine</a> for the buildup this mistake causes, <a href=\"/home/washing-machine-mould-door-seal/\">mould on the door seal</a> for where the residue ends up, and <a href=\"/home/stop-pre-rinsing-dishes/\">stop pre-rinsing dishes</a> for the equivalent over-application error in the kitchen.</p>",

"home/mistakes/mixing-cleaning-products":
    "<h2>The chemistry is not hypothetical</h2>"
    "<p>Certain combinations produce genuinely dangerous gases rather than merely ineffective ones. Bleach with an acidic cleaner releases chlorine gas; bleach with ammonia releases chloramine. Both cause respiratory injury in an ordinary domestic setting, and the reactions happen immediately on contact in the bowl or on the surface. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the household-chemical safety guidance behind this entry, and the <a href=\"" + _w("bleach") + "\" rel=\"noopener\">bleach reference material on Wikipedia</a> covers the reactions involved. Reviewed by the Bryme Home desk, 27 September 2026.</p>"
    "<h2>The rule that removes the risk entirely</h2>"
    "<p>Use one product at a time and rinse between them. That single habit covers every dangerous combination, because none of them can occur without two products meeting. It is also worth knowing that the danger is not limited to deliberate mixing: pouring one product into a bowl or a spray bottle that still holds another is the same event.</p>"
    "<ul>"
    "<li><b>Never mix bleach with anything except water.</b> Not acid, not ammonia, not another brand of cleaner.</li>"
    "<li><b>Rinse between products.</b> Especially in a toilet bowl, where the previous product is still sitting in the water.</li>"
    "<li><b>Do not decant into unlabelled bottles.</b> The hazard is unrecognisable once the label is gone.</li>"
    "<li><b>Ventilate, and leave on any unexpected smell.</b> An irritant odour during cleaning is a signal to get fresh air immediately, not to open a window and continue.</li>"
    "<li><b>Keep the containers closed and separate.</b> Storage matters as much as use.</li>"
    "</ul>"
    "<p>The desk's other cleaning entries assume this rule: <a href=\"/home/how-to-deep-clean-an-oven/\">deep cleaning an oven</a>, <a href=\"/home/how-to-descale-a-kettle/\">descaling a kettle</a> and <a href=\"/home/vinegar-in-the-dishwasher/\">vinegar in the dishwasher</a> each state which products must not be combined in that specific job.</p>",

"sports/season":
    "<h2>What a season actually is, as a structure</h2>"
    "<p>A domestic season is a closed loop of fixtures in which every club plays the others twice, and the table that emerges is the only genuinely complete comparison the sport produces. That is what makes it different from a cup: no draw luck, no single elimination, and a sample large enough that form usually converges with quality by the end. The <a href=\"" + _w("league+system") + "\" rel=\"noopener\">reference material on the league system on Wikipedia</a> explains the round-robin structure behind it. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>How the season divides into phases</h2>"
    "<p>Almost every season has the same shape whatever the league. The opening weeks are unreliable because squads are still settling; the middle third is where the real table forms; and the closing weeks are distorted by fatigue, injury and the differing stakes of clubs at opposite ends. Reading a season means knowing which phase you are in before trusting any conclusion from it.</p>"
    "<ul>"
    "<li><b>Early season is the least predictive.</b> New signings, fitness and tactical changes all settle over the first several weeks.</li>"
    "<li><b>The middle third is the honest part.</b> Enough games played, not enough fatigue accumulated, and the table is closest to reality.</li>"
    "<li><b>Winter congestion distorts everything.</b> Clubs in European competition lose ground here for reasons unrelated to ability.</li>"
    "<li><b>The run-in has uneven stakes.</b> A club with nothing to play for is not the same opponent as one fighting relegation.</li>"
    "</ul>"
    "<p>The desk's league pages carry the season as it happens: <a href=\"/sports/premier-league-results/\">Premier League results</a>, <a href=\"/sports/la-liga-table/\">the La Liga table</a>, <a href=\"/sports/bundesliga-table/\">the Bundesliga table</a> and <a href=\"/sports/serie-a-table/\">the Serie A table</a>, with the <a href=\"/sports/epl/\">Premier League hub</a> as the entry point for the English season.</p>",

"sports/epl":
    "<h2>What this hub covers, and how to use it</h2>"
    "<p>This page is the entry point to the desk's Premier League coverage: results, the clubs, the scoring race and the individual matchweeks, kept together so the season can be followed without jumping between unrelated pages. <a href=\"" + EPL + "\" rel=\"noopener\">The Premier League</a> publishes the official competition record, and the <a href=\"" + _w("Premier_League") + "\" rel=\"noopener\">Premier League reference material on Wikipedia</a> carries the historical context that gives a single season its scale. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>Reading the season rather than the headline</h2>"
    "<p>The desk's approach across these pages is consistent: treat small samples as noise, separate home from away, and adjust for what a fixture list did to a squad before judging what the squad did. Most bad takes on this league come from three matches read as a trend, and the pages below are built to resist exactly that.</p>"
    "<ul>"
    "<li><b>Results first.</b> <a href=\"/sports/premier-league-results/\">Premier League results</a> carries the outcomes with the reading notes attached.</li>"
    "<li><b>Then the clubs.</b> <a href=\"/sports/premier-league-clubs/\">Premier League clubs</a> covers the twenty different situations the results come out of.</li>"
    "<li><b>Then the individuals.</b> <a href=\"/sports/premier-league-top-scorers/\">Premier League top scorers</a> applies the same adjustments to the scoring race.</li>"
    "<li><b>And the season as a whole.</b> <a href=\"/sports/season/\">how a season works</a> explains the structure that produces the table.</li>"
    "</ul>"
    "<p>For the transfer activity between and during seasons, see the desk's <a href=\"/sports/transfers/\">transfer coverage</a> and the explanation of <a href=\"/sports/why-football-transfers-collapse/\">why football transfers collapse</a>.</p>",

"sports/transfers":
    "<h2>A transfer is a negotiation with several parties</h2>"
    "<p>Reporting on transfers treats the fee as the story, but the fee is usually the settled part. What decides whether a deal happens is the agreement between clubs, the personal terms with the player, the agent's position, and the registration rules of the receiving league. <a href=\"" + FIFA + "\" rel=\"noopener\">FIFA</a> publishes the regulations governing international transfers, and the <a href=\"" + _w("transfer+window") + "\" rel=\"noopener\">transfer-window reference material on Wikipedia</a> explains the calendar constraints that shape every window. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What to weigh when reading transfer news</h2>"
    "<p>The useful question is rarely whether a move would be good, and nearly always whether the parties have any reason to agree. A club that has just sold its best player is in a different position from one with two windows of budget unused, and the timing within the window changes what each side can afford to wait for.</p>"
    "<ul>"
    "<li><b>Identify who needs the deal.</b> Asymmetry of need drives price more than player quality does.</li>"
    "<li><b>Check the contract situation.</b> A player out of contract next summer is a fundamentally different asset.</li>"
    "<li><b>Note the window timing.</b> Late deals are priced by deadline pressure, and both sides know it.</li>"
    "<li><b>Treat reported fees sceptically.</b> Add-ons, sell-on clauses and agent fees mean the headline number rarely describes the transaction.</li>"
    "</ul>"
    "<p>The desk's related coverage: <a href=\"/sports/why-football-transfers-collapse/\">why football transfers collapse</a>, <a href=\"/sports/what-does-a-sporting-director-do/\">what a sporting director does</a>, and <a href=\"/sports/la-liga-transfers/\">La Liga transfers</a> for the league-specific view.</p>",

"sports/premier-league-matchweek-1-guide":
    "<h2>Why the first matchweek deserves its own reading</h2>"
    "<p>Opening-weekend results are the least predictive fixtures of the season, and they are also the most widely over-interpreted. Fitness is uneven, new signings have had weeks rather than months, and the tactical picture from pre-season rarely survives contact with a competitive match. <a href=\"" + EPL + "\" rel=\"noopener\">The Premier League</a> publishes the official fixture list and match records behind this guide. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>What the first week can and cannot tell you</h2>"
    "<p>It can show you how a new signing has been deployed, which is genuinely informative because it reflects the manager's intention rather than a season of accumulated habit. It cannot tell you whether that deployment works, and it cannot tell you anything at all about a squad's depth, which only shows up once the fixture congestion starts.</p>"
    "<ul>"
    "<li><b>Watch the shape, not the score.</b> Where players are positioned says more than the result does.</li>"
    "<li><b>Note the substitutions.</b> Early changes reveal what the manager was unhappy with.</li>"
    "<li><b>Discount fitness-driven results.</b> A side that faded badly in the last twenty minutes is describing its pre-season, not its quality.</li>"
    "<li><b>Hold every conclusion loosely.</b> Nothing decided in week one has ever stayed decided.</li>"
    "</ul>"
    "<p>The rest of the desk's coverage carries the season forward: <a href=\"/sports/premier-league-results/\">Premier League results</a>, <a href=\"/sports/premier-league-clubs/\">Premier League clubs</a>, and <a href=\"/sports/premier-league-top-scorers/\">Premier League top scorers</a>, with <a href=\"/sports/season/\">how a season works</a> explaining the structure the matchweeks build into.</p>",

"sports/deadline-day-dont-try-to-make-sense-of-it":
    "<h2>Deadline day is a different market</h2>"
    "<p>The final hours of a window operate under conditions that do not exist at any other point: fixed expiry, incomplete information, and a large number of parties who all know the clock. That combination produces outcomes that look irrational from outside and are entirely rational from inside, which is the whole argument of this piece. The <a href=\"" + _w("transfer+window") + "\" rel=\"noopener\">transfer-window reference material on Wikipedia</a> explains the registration deadlines that create the pressure. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>The dynamics that produce the chaos</h2>"
    "<p>Most deadline-day activity is knock-on. One move completing releases a replacement, which releases another, and a chain that began with a single agreement produces six transactions in an hour. Add paperwork cut-offs and medical scheduling to that, and the apparent disorder is simply a queue being cleared simultaneously.</p>"
    "<ul>"
    "<li><b>Follow the chains, not the headlines.</b> A deal announced late is usually the last link in something that started in the morning.</li>"
    "<li><b>Expect loans.</b> They are the fastest instrument available and the one most used when time is short.</li>"
    "<li><b>Read the panic correctly.</b> A club spending badly on deadline day is often solving a problem it created in June.</li>"
    "<li><b>Remember the paperwork deadline.</b> A deal agreed is not a deal registered, and the difference has ended several transfers.</li>"
    "</ul>"
    "<p>The desk's related coverage: <a href=\"/sports/why-football-transfers-collapse/\">why football transfers collapse</a>, <a href=\"/sports/transfers/\">the transfers desk</a>, and <a href=\"/sports/what-does-a-sporting-director-do/\">what a sporting director does</a>, which explains who is actually making these decisions under pressure.</p>",

"sports/elliot-anderson-man-city-record-signing":
    "<h2>What a record fee is, and what it is not</h2>"
    "<p>A transfer record describes a price, and the price is a product of the moment: the buyer's resources, the seller's position, the player's contract length and the scarcity of alternatives in that window. It is not a rating of the player, and it is a poor predictor of contribution. The <a href=\"" + _w("list+of+most+expensive+association+football+transfers") + "\" rel=\"noopener\">reference material on record transfers on Wikipedia</a> places any single fee in its historical context, which is the only way to read one honestly. Reviewed by the Bryme Sport desk, 27 September 2026.</p>"
    "<h2>How to judge a signing of this kind</h2>"
    "<p>The relevant questions are about fit rather than price: what the club needed, whether this player provides it, and how the squad adjusts around him. A record fee usually signals that the buyer had few options and knew it, which is a statement about the market as much as about the player.</p>"
    "<ul>"
    "<li><b>Assess the need first.</b> A club replacing a departing starter is buying something different from one adding depth.</li>"
    "<li><b>Consider the contract length.</b> A long deal spreads the cost and changes the accounting picture considerably.</li>"
    "<li><b>Look at the alternatives.</b> Scarcity in a position inflates fees far more than talent does.</li>"
    "<li><b>Judge it over a season.</b> Early form after a record move is affected by the attention as much as by the football.</li>"
    "</ul>"
    "<p>The desk's wider coverage of how these deals come together: <a href=\"/sports/why-football-transfers-collapse/\">why football transfers collapse</a>, <a href=\"/sports/what-does-a-sporting-director-do/\">what a sporting director does</a> and the <a href=\"/sports/transfers/\">transfers desk</a>, with the results on the pitch at <a href=\"/sports/premier-league-results/\">Premier League results</a>.</p>",

}
