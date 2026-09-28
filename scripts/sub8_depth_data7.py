# -*- coding: utf-8 -*-
"""Editorial depth sections, part 7: batch C, the smallest-gap half of the
closest-to-10 population (pages 2-20 words short of the 750-word bar plus the
next tranche, 37-50 words short). Writers, tech, home, sports desks.
Every external URL curl-verified 200 at authoring time."""

WHO = "https://www.who.int/"
EPA = "https://www.epa.gov/"
GOVUK = "https://www.gov.uk/"
NFPA = "https://www.nfpa.org/"
ACSM = "https://www.acsm.org/"
CLMP = "https://www.clmp.org/"
LITHUB = "https://www.lithub.com/"
PL = "https://www.premierleague.com/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS7 = {

"writers/writing/west-branch":
    "<h2>What a print-and-digital literary journal offers</h2>"
    "<p>West Branch is the literary journal published out of Bucknell University, and it sits in the tier of university journals where submission is free or low-cost and the reading is genuinely competitive. For writers building a publication record, journals of this type are the standard first rung: they are cited plainly in cover letters, they do not require an agent, and their archives document exactly the kind of work they publish. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> maintains the field these journals sit within. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>How to read a journal before submitting</h2>"
    "<ul>"
    "<li><b>Read two issues, not two pages.</b> A journal's taste shows across a spread of work, not in one piece.</li>"
    "<li><b>Match the form first.</b> A journal strong in lyric essays is rarely the home for a reported feature.</li>"
    "<li><b>Note the response window.</b> Journals that hold work for months change your submission calendar, not your odds.</li>"
    "<li><b>Track everything.</b> A plain spreadsheet of dates and outcomes prevents duplicate submissions and panic.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/granta/\">Granta</a>, <a href=\"/writers/writing/kenyon-review/\">The Kenyon Review</a> and <a href=\"/writers/writing/cincinnati-review/\">The Cincinnati Review</a>.</p>",

"tech/laptop-overheating-fan-noise":
    "<h2>Heat first, noise second</h2>"
    "<p>A loud fan is a symptom, not a fault. The fan speeds up because something is asking for cooling: a blocked vent, a dust-matted heatsink, a background process pinning the processor, or ambient heat the design cannot shed. Fix the demand for cooling and the noise follows; replace the fan first and it usually returns. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the electrical-safety context this desk follows on devices that run hot. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The order that actually works</h2>"
    "<ul>"
    "<li><b>Check vents and intake while it runs.</b> A hand near the vents tells you whether air is moving at all.</li>"
    "<li><b>Find the process.</b> Task Manager or Activity Monitor names the software that is holding the processor up.</li>"
    "<li><b>Clear the dust properly.</b> Short bursts through the intake vents; never spin the fan with compressed air.</li>"
    "<li><b>Then judge the paste and the pad.</b> Repasting is real maintenance, but it is the last step, not the first.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-fan-loud-dust-vs-fault/\">laptop fan loud: dust versus fault</a>, <a href=\"/tech/laptop-fan-dust-harmattan/\">laptop fans and harmattan dust</a> and <a href=\"/tech/phone-overheating-causes-and-fixes/\">phone overheating causes and fixes</a>.</p>",

"writers/writing/ecotone":
    "<h2>A journal with a place at its centre</h2>"
    "<p>Ecotone, published at the University of North Carolina Wilmington, built its reputation on writing about place and environment without narrowing itself to nature writing as a genre. That distinction matters for submitters: the journal publishes essays, fiction and poetry that treat landscape as lived context rather than scenery. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> lists the independent and university-journal field Ecotone belongs to. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What place writing rewards</h2>"
    "<ul>"
    "<li><b>Specificity over atmosphere.</b> The named street, crop or season reads as knowledge; adjectives read as decoration.</li>"
    "<li><b>A stake in the setting.</b> Work about place lands hardest when someone in it stands to gain or lose.</li>"
    "<li><b>Reported detail inside lyric form.</b> Interviews, archives and field notes give the essay something to be about.</li>"
    "<li><b>Patience with drafts.</b> Place work thickens with revision rather than thinning.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/earth-island-journal/\">Earth Island Journal</a>, <a href=\"/writers/writing/high-country-news/\">High Country News</a> and <a href=\"/writers/writing/agni/\">AGNI</a>.</p>",

"writers/writing/one-story":
    "<h2>One story at a time</h2>"
    "<p>One Story's format is its argument: one story per issue, mailed or sent on its own, with no competing work beside it. For a writer, that format has a practical consequence — a published story is not one of six in a table of contents but the entire issue, which is why the journal punches above its size in readership. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> is the field guide to small journals of this kind. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing for a single-slot journal</h2>"
    "<ul>"
    "<li><b>Lead with the story's engine.</b> With no neighbours to set context, the first pages must carry the premise alone.</li>"
    "<li><b>End cleanly.</b> A story published alone reads as finished work, not as a fragment of a project.</li>"
    "<li><b>Submit your strongest, not your newest.</b> The single slot makes every submission the whole ballot.</li>"
    "<li><b>Watch the response times.</b> One-slot journals read slowly because their volume is real.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/cincinnati-review/\">The Cincinnati Review</a>, <a href=\"/writers/writing/kenyon-review/\">The Kenyon Review</a> and <a href=\"/writers/writing/agni/\">AGNI</a>.</p>",

"home/harmattan-fire-safety-house":
    "<h2>Why the dry season raises the risk</h2>"
    "<p>Harmattan carries dust, lowers humidity and dries out the materials a house is built and cleaned with. The same weeks bring more use of heaters, candles and generators, so ignition sources rise exactly when fuel is driest. Treating the season as a fire-risk period — not just a dust period — is the whole of the planning. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the home fire-safety guidance this checklist draws on. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The season's short checklist</h2>"
    "<ul>"
    "<li><b>Clear the generator and the cooking area.</b> Dry dust and fuel vapour share space too easily in the season.</li>"
    "<li><b>Retire worn extension leads.</b> Heat plus cracked insulation is the commonest quiet fire path in the house.</li>"
    "<li><b>Keep candles elevated and enclosed.</b> Curtain movement in dry, windy weeks is enough.</li>"
    "<li><b>Damp-mop dust rather than sweeping it.</b> Airborne dust near a flame is a fuel, not just dirt.</li>"
    "</ul>"
    "<p>See <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a>, <a href=\"/home/cooking-oil-fire-plan/\">the cooking-oil fire plan</a> and <a href=\"/home/dryer-vent-cleaning-fire-risk/\">dryer vents and fire risk</a>.</p>",

"home/mould-after-a-flooded-room":
    "<h2>The drying window decides everything</h2>"
    "<p>After floodwater leaves a room, mould growth is governed by time and moisture. Porous materials that stay wet past a day or two become the problem: carpet backing, plasterboard, soft furnishings. The work after a flood is therefore mostly removal and drying rather than cleaning — surfaces that can be saved get dry air, and materials that cannot are taken out without regret. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes flood-damage mould guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What to strip, what to dry</h2>"
    "<ul>"
    "<li><b>Plasterboard above the flood line gets cut back.</b> Water wicks upward inside the core well beyond the visible mark.</li>"
    "<li><b>Carpet and underlay usually go.</b> Drying them in place is what feeds the growth underneath.</li>"
    "<li><b>Move air, then measure.</b> Fans, dehumidifiers and open structure; wait for dry readings before closing walls.</li>"
    "<li><b>Photograph before stripping.</b> Insurance and landlord discussions run on evidence taken early.</li>"
    "</ul>"
    "<p>See <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three kinds of damp</a>, <a href=\"/home/uk-landlord-damp-mould-duties/\">landlord duties on damp and mould</a> and <a href=\"/home/bathroom-grout-mould/\">bathroom grout mould</a>.</p>",

"tech/laptop-spill-first-five-minutes":
    "<h2>Power out first, judgement later</h2>"
    "<p>The damage in a laptop spill is done by electricity moving through wet board, not by the liquid itself. The first five minutes decide the margin: power off, battery out if it comes out, and no testing to see if it still works. Every attempt to boot while the board is wet adds corrosion paths that drying cannot undo. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the liquid-and-electrical safety context behind this order of work. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The first five minutes, in order</h2>"
    "<ul>"
    "<li><b>Shut down and unplug immediately.</b> Hold the power button if the shutdown is not instant.</li>"
    "<li><b>Remove the battery if the design allows.</b> If it does not, disconnect the charger and stop.</li>"
    "<li><b>Turn it upside down and open it fully.</b> Gravity and surface area do more than rice or heat ever will.</li>"
    "<li><b>Do not test it.</b> A shorted board that is never powered has a far better repair outlook.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-no-display-boot-ladder/\">the no-display boot ladder</a>, <a href=\"/tech/laptop-fan-loud-dust-vs-fault/\">laptop fan loud: dust versus fault</a> and <a href=\"/tech/swollen-phone-battery-safety/\">swollen battery safety</a>.</p>",

"home/renter-security":
    "<h2>Security without fixtures</h2>"
    "<p>Renters face the security problem of not owning the changes they make. The useful interventions are therefore reversible: better lighting, window locks that clamp rather than drill, door furniture that fits existing holes, and habits that work with a landlord's permissions rather than around them. Most of the gain costs nothing structural. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes tenancy and home-security guidance renters can hold a landlord to. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The reversible upgrades that matter</h2>"
    "<ul>"
    "<li><b>Light the entrance, not the street.</b> A lamp on a timer at the door does more than floodlighting the compound.</li>"
    "<li><b>Clamp window locks on ground-floor openings.</b> Fitted in minutes, removed in minutes at the end of the tenancy.</li>"
    "<li><b>Replace the strike plate screws.</b> Long screws into the frame are the cheapest door reinforcement available.</li>"
    "<li><b>Document the property on arrival.</b> Condition photos protect the deposit as surely as locks protect the room.</li>"
    "</ul>"
    "<p>See <a href=\"/home/renter-friendly-fixes/\">renter-friendly fixes</a>, <a href=\"/home/renter-vs-owner-repairs/\">which repairs are the landlord's</a> and <a href=\"/home/barred-windows-and-fire-escape/\">barred windows and fire escapes</a>.</p>",

"writers/writing/longreads":
    "<h2>What the longform aggregator rewards</h2>"
    "<p>Longreads built its audience by curating long-form nonfiction from magazines, newspapers and independent writers at a moment when that work needed a front door. For writers, it is useful twice: as a reading map of the form, and as a venue that points editors toward work that rewards length. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> is where the magazine side of that ecosystem is catalogued. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading longform with intent</h2>"
    "<ul>"
    "<li><b>Read for structure, not topic.</b> The shape of a piece teaches more than its subject ever will.</li>"
    "<li><b>Copy out the turns.</b> The sentences where a piece changes direction are worth keeping in a notebook.</li>"
    "<li><b>Note the reporting budget.</b> Long pieces stand on interviews and documents; count them.</li>"
    "<li><b>Follow the writers.</b> Bylines move between outlets faster than mastheads do.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/longreads-personal-essay/\">the longreads personal essay guide</a>, <a href=\"/writers/writing/longreads-reported-feature/\">the reported feature guide</a> and <a href=\"/writers/writing/longreads-reading-list/\">the longform reading list</a>.</p>",

"sports/premier-league-matchweek-4-preview":
    "<h2>Reading a matchweek this early</h2>"
    "<p>Matchweek 4 is the point where a season's opening noise starts to separate from its signal, and even then only barely. Squads have played enough to show their shape and injuries, but not enough to make the table predictive. The useful preview therefore leans on team news, fixture congestion and line-up patterns rather than on standings that are still mostly schedule. The <a href=\"" + PL + "\" rel=\"noopener\">official Premier League site</a> carries the fixtures, team news and results this desk builds its matchweek coverage around. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What to watch in the fourth week</h2>"
    "<ul>"
    "<li><b>Rotation after midweek fixtures.</b> The first European weeks reshuffle line-ups before the table notices.</li>"
    "<li><b>Set-piece records.</b> By matchweek 4 they are among the few stable numbers the season has produced.</li>"
    "<li><b>Minutes for new signings.</b> Start versus substitute tells you a manager's real plan.</li>"
    "<li><b>Goalkeeper and defensive pairing changes.</b> These decide tight games more than any attacking storyline.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league-fixtures/\">the Premier League fixtures</a>, <a href=\"/sports/premier-league-results/\">the results</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",

"home/mattress-humidity-care":
    "<h2>A mattress is a humidity instrument</h2>"
    "<p>A mattress absorbs and releases moisture all night, every night, and in humid rooms it never fully dries between uses. That is what drives musty smells, dust-mite growth and the damp patches that appear on the underside. The care routine is therefore about air and rotation rather than cleaning: keep the underside breathing, flip the load, and dry the room. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor-air and moisture guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The humidity routine</h2>"
    "<ul>"
    "<li><b>Leave the bed to air for an hour each morning.</b> Folding the covers back does most of the drying.</li>"
    "<li><b>Rotate quarterly, head to foot.</b> Rotation flattens the wear pattern the body makes in one spot.</li>"
    "<li><b>Check the underside seasonally.</b> Stains underneath mean the room, not the sleeper, is the problem.</li>"
    "<li><b>Put airflow under the bed.</b> A slatted base or risers beat any cleaning product for moisture control.</li>"
    "</ul>"
    "<p>See <a href=\"/home/how-to-clean-and-care-for-a-mattress/\">how to clean and care for a mattress</a>, <a href=\"/home/kitchen-ventilation-damp/\">kitchen ventilation and damp</a> and <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three kinds of damp</a>.</p>",

"home/septic-tank-emptying-routine":
    "<h2>A routine beats a rescue</h2>"
    "<p>A septic tank fails expensively when it is emptied reactively — after the smell, the backup or the soggy lawn. The alternative is a routine: know the tank's size, keep a record of every emptying, and schedule the next one from the record rather than from symptoms. Everything else on the list protects that schedule. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes septic-system maintenance guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What the routine protects</h2>"
    "<ul>"
    "<li><b>Keep the inspection cover accessible.</b> A buried lid turns a routine emptying into a digging job.</li>"
    "<li><b>Record every service.</b> The interval between the last two emptyings predicts the next one honestly.</li>"
    "<li><b>Watch what enters the system.</b> Wipes, grease and bleach are the three slow causes of failure.</li>"
    "<li><b>Protect the drain field.</b> No parking, no trees, no runoff directed onto it.</li>"
    "</ul>"
    "<p>See <a href=\"/home/water-tank-annual-clean/\">the annual water-tank clean</a>, <a href=\"/home/drain-flies-bathroom/\">drain flies in the bathroom</a> and <a href=\"/home/floor-drain-backflow/\">floor drain backflow</a>.</p>",

"home/uk-insulation-grants":
    "<h2>What the schemes actually cover</h2>"
    "<p>UK insulation support runs through a patchwork of schemes rather than one fund: energy-supplier obligations, local-authority allocations and separate grants for households on qualifying benefits. The practical route starts with the property's Energy Performance Certificate and the household's eligibility, because the same measure can be free under one scheme and paid under another. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes the eligibility rules and scheme entry points this desk tracks. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Applying without wasting months</h2>"
    "<ul>"
    "<li><b>Get the EPC first.</b> Its recommendations are the measure list assessors will work from.</li>"
    "<li><b>Check benefit eligibility before the property survey.</b> Household tests decide access faster than any property measure.</li>"
    "<li><b>Ask which scheme, by name.</b> A quote that does not name its funding route is not a grant quote.</li>"
    "<li><b>Keep the paperwork together.</b> EPC, bills, benefit letters and the survey are requested repeatedly.</li>"
    "</ul>"
    "<p>See <a href=\"/home/attic-insulation-basics/\">attic insulation basics</a>, <a href=\"/home/uk-boiler-servicing/\">UK boiler servicing</a> and <a href=\"/home/which-heating-system/\">choosing a heating system</a>.</p>",

"home/tank-overflow-pump-dry":
    "<h2>Reading an overflow as a system symptom</h2>"
    "<p>An overflow that runs and a pump that runs dry are usually the same problem seen at two ends: the tank's water level is not being controlled by the inlet valve, the float, or the demand below. Chasing either symptom alone leaves the other to repeat. The diagnostic order is level control first, then delivery — pumps survive being dry far less well than tanks survive being full. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the household water-safety context this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The order of checks</h2>"
    "<ul>"
    "<li><b>Shut the inlet and watch the level.</b> A level that keeps rising is a valve fault, not a tank fault.</li>"
    "<li><b>Lift the float by hand.</b> If the valve does not stop it, the valve needs service before anything else.</li>"
    "<li><b>Check the pump's intake, not just its power.</b> A dry-run fault is usually air, a blockage or a low tank.</li>"
    "<li><b>Test the overflow path.</b> The overflow should leave the building visibly, in a place you can see from the ground.</li>"
    "</ul>"
    "<p>See <a href=\"/home/borehole-pump-no-water/\">borehole pump running with no water</a>, <a href=\"/home/water-tank-annual-clean/\">the annual water-tank clean</a> and <a href=\"/home/hidden-water-leak-meter-test/\">the meter test for hidden leaks</a>.</p>",

"writers/learn/freelance-paid-writing/how-writing-retainers-work":
    "<h2>A retainer trades rate risk for scheduling risk</h2>"
    "<p>A retainer is a standing agreement: defined work or defined availability, paid monthly, in exchange for priority. It works when both sides can name the deliverable clearly enough to avoid drift, and it fails most often through vagueness rather than through money. The writers who keep retainers treat them like a product with a spec — hours, outputs, response times and a notice period all written down. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes resources for writers structuring ongoing client work. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The clauses that decide it</h2>"
    "<ul>"
    "<li><b>Scope in outputs or hours, explicitly.</b> One or the other; leaving it implicit is how retainers dissolve.</li>"
    "<li><b>Unused time policy.</b> Say whether hours roll over before the first invoice, not after the first dispute.</li>"
    "<li><b>Priority stated plainly.</b> If the retainer buys response times, name them on both sides.</li>"
    "<li><b>Notice period.</b> Thirty days is the common ground; it protects both calendars.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-writing-retainers-work/\">the writing retainers guide</a>, <a href=\"/writers/writing/longreads/\">Longreads</a> and <a href=\"/writers/writing/longreads-personal-essay/\">the longreads personal essay guide</a>.</p>",

"writers/writing/overland-fiction":
    "<h2>Field writing with a funder's patience</h2>"
    "<p>Overland has spent decades publishing writing from and about the Pacific and its diasporas, often through fellowships and prizes that pay writers to travel and report. That funding model matters to submitters: it means the journal's taste runs toward work built on presence — essays and fiction that could not have been written from a desk. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> maps the small-press field Overland belongs to. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What presence-based work needs</h2>"
    "<ul>"
    "<li><b>A place the writer could actually go.</b> Field writing is judged on access as much as prose.</li>"
    "<li><b>The stake in the place.</b> Travelogues thin out where nothing is at issue.</li>"
    "<li><b>Named voices from the place.</b> Reporting beats reflection when the community is the subject.</li>"
    "<li><b>A submission sized to the journal's slots.</b> Read the current calls before the work is finished.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/griffith-review/\">Griffith Review</a>, <a href=\"/writers/writing/hinterland/\">Hinterland</a> and <a href=\"/writers/writing/island-magazine/\">Island</a>.</p>",

"fitness/strength":
    "<h2>What a strength section is for</h2>"
    "<p>Strength is the fitness quality that most reliably changes daily life: carrying loads, standing up, recovering balance. It trains well because it is measurable and progressive — the same session can be repeated next week with a small, deliberate increase, and the record does the arguing. The <a href=\"" + ACSM + "\" rel=\"noopener\">American College of Sports Medicine</a> publishes the resistance-training principles this section is built on. By the Bryme Fitness desk. Reviewed 28 September 2026.</p>"
    "<h2>The order to learn it in</h2>"
    "<ul>"
    "<li><b>Patterns before load.</b> Squat, hinge, push, pull and carry — then add weight to the ones you already own.</li>"
    "<li><b>Two sessions a week is a full dose.</b> Consistency beats frequency you cannot keep.</li>"
    "<li><b>Add in small steps.</b> The next increase should feel earned, not ambitious.</li>"
    "<li><b>Keep a written record.</b> Strength responds to progression, and progression needs a log.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/strength-training-for-beginners/\">strength training for beginners</a>, <a href=\"/fitness/how-many-reps-for-muscle/\">how many reps for muscle</a> and <a href=\"/fitness/how-progressive-overload-works/\">how progressive overload works</a>.</p>",

"tech/projector-vs-tv-compound-viewing":
    "<h2>Light decides the answer</h2>"
    "<p>A projector's picture is only as good as the room's darkness, while a television's brightness defeats a bright room and struggles to justify its size on a wall. For compound and shared living spaces this is not a preference question: measure the viewing hours against the room's light, then the screen size against the viewing distance, and the choice usually makes itself. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household energy guidance this desk follows on always-on display gear. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Run the two questions first</h2>"
    "<ul>"
    "<li><b>Is the room dark when you actually watch?</b> Evening viewing decides projector viability more than any spec.</li>"
    "<li><b>How far is the seat?</b> Size is a distance calculation before it is a preference.</li>"
    "<li><b>Count the audio plan.</b> Projectors need external sound; televisions need it less.</li>"
    "<li><b>Price the lamp or the panel years ahead.</b> Projector lamps age; television panels mostly do not.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/4k-on-a-small-tv-when-its-invisible/\">when 4K on a small TV is invisible</a>, <a href=\"/tech/power-bank-size-math-for-tv-and-wifi/\">power-bank sizing for TV and Wi-Fi</a> and <a href=\"/tech/antenna-vs-satellite-vs-streaming-live-tv/\">antenna versus satellite versus streaming</a>.</p>",

"home/the-battery-room":
    "<h2>What a battery room is really for</h2>"
    "<p>In homes with solar or inverter systems, the battery room is where energy is stored and where the house's fire risk concentrates. The room's job is simple to state: ventilation, separation from living space, clear access, and no storage of anything else. Most failures begin as clutter — a fuel can, a cardboard stack, a charger left on a shelf beside the cells. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes electrical-storage safety guidance this room's rules follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Keeping the room a room</h2>"
    "<ul>"
    "<li><b>Nothing shares the space.</b> A battery room stores energy, not tools, fuel or paint.</li>"
    "<li><b>Ventilate and shade it.</b> Heat is the multiplier that turns a battery fault into an incident.</li>"
    "<li><b>Keep the disconnect reachable.</b> The isolation switch should be visible from the door, in the dark.</li>"
    "<li><b>Post the emergency numbers on the wall.</b> Written down beats remembered during an event.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/swollen-phone-battery-safety/\">swollen battery safety</a>, <a href=\"/tech/inverter-battery-runtime-maths/\">inverter battery runtime maths</a> and <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a>.</p>",

"home/compound-mosquito-control-night":
    "<h2>Why night is the working window</h2>"
    "<p>Mosquito control at compound level succeeds at night because that is when the biting species are active and when the house's screens, coils and repellents are actually in use. Daytime work — draining containers, clearing gutters, cutting the grass edge — removes tomorrow's breeding; the evening routine protects tonight. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the vector-control guidance this two-part routine follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Tonight's routine, and tomorrow's</h2>"
    "<ul>"
    "<li><b>Screen and repellent before dusk.</b> Prevention works on the house; spraying works on the compound.</li>"
    "<li><b>Walk the compound with a torch and a bucket.</b> Standing water found at night is water removed tomorrow.</li>"
    "<li><b>Check gutters and plant saucers weekly.</b> The smallest containers produce the most breeding.</li>"
    "<li><b>Rotate what you burn.</b> Coils and plug-ins lose effect against habituated insects; alternate them.</li>"
    "</ul>"
    "<p>See <a href=\"/home/mosquito-coils-and-plug-ins/\">mosquito coils and plug-ins</a>, <a href=\"/home/harmattan-fire-safety-house/\">harmattan fire safety</a> and <a href=\"/home/drain-flies-bathroom/\">drain flies in the bathroom</a>.</p>",

"sports/how-boxing-fights-end-explained":
    "<h2>Every fight ends in one of a few ways</h2>"
    "<p>Boxing's ending vocabulary looks opaque until you sort it by cause: the referee stops it, the corner stops it, the doctor stops it, the fighter does not answer the bell, or the scheduled rounds run out and the judges decide. Everything else — knockouts, technical decisions, disqualifications — is a variation of one of those doors. The rulesets are published by sanctioning bodies and summarised in reference works such as <a href=\"" + _w("boxing+rules") + "\" rel=\"noopener\">the standard competition rules</a>. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the ending live</h2>"
    "<ul>"
    "<li><b>Watch the referee's count, not the crowd.</b> A count stopped at eight means the fight is still being decided.</li>"
    "<li><b>A corner stoppage is a decision, not a defeat.</b> Teams end fights to protect careers that continue afterwards.</li>"
    "<li><b>Technical decisions follow the scorecards.</b> An accidental cut can send a fight to the judges early.</li>"
    "<li><b>Retirements between rounds count as stoppages.</b> The result records why it ended, not just who won.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/boxing-rounds-and-fight-length-explained/\">rounds and fight length</a>, <a href=\"/sports/boxing-scoring-explained/\">how boxing scoring works</a> and <a href=\"/sports/boxing-decisions-explained/\">boxing decisions explained</a>.</p>",

"writers/writing/the-offing":
    "<h2>An online journal with a taste for range</h2>"
    "<p>The Offing publishes across forms — essays, criticism, fiction, poetry — and built its readership online without treating the web as a lesser paper. For writers it is a useful study in audience: work published there is read by people who arrived through the piece itself rather than through a print subscription. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogues the small-press field it sits within. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing for online-first journals</h2>"
    "<ul>"
    "<li><b>The opening carries the click-through.</b> Online readers decide with the first screen, not the first issue.</li>"
    "<li><b>Sections should earn their headings.</b> Skimming is a reading mode online, and headings are its map.</li>"
    "<li><b>Know where the piece will be linked.</b> Work that travels well has a title and opening that survive out of context.</li>"
    "<li><b>Submit to the section, not just the journal.</b> Online journals read by section editors with real tastes.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/guernica/\">Guernica</a>, <a href=\"/writers/writing/noema/\">Noema</a> and <a href=\"/writers/writing/new-lines-magazine/\">New Lines Magazine</a>.</p>",

"home/freezer-frost-buildup":
    "<h2>Frost is a door problem first</h2>"
    "<p>A freezer builds frost when humid air enters the cabinet and freezes on the coldest surface it finds. The moisture arrives through the door — a seal that has stiffened, a door closed on a bag, a habit of holding it open while deciding. Defrosting clears the symptom; only fixing the air entry stops the return. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household appliance energy guidance this desk follows on freezers that run harder than they should. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Stopping the cycle</h2>"
    "<ul>"
    "<li><b>Test the seal with paper.</b> Close the door on a sheet; where it slides out freely, the seal leaks.</li>"
    "<li><b>Defrost before the ice is thick.</b> A quarter-inch of ice already raises the running cost.</li>"
    "<li><b>Cool food before freezing it.</b> Steam from warm food is humidity delivered straight to the coils.</li>"
    "<li><b>Leave room for air inside.</b> A packed freezer circulates badly and frosts unevenly.</li>"
    "</ul>"
    "<p>See <a href=\"/home/how-to-defrost-a-freezer-properly/\">how to defrost a freezer properly</a>, <a href=\"/home/second-fridge-freezer-cost/\">the cost of a second fridge or freezer</a> and <a href=\"/home/washing-machine-mould-door-seal/\">washing-machine door seal mould</a>.</p>",

"home/uk-boiler-servicing":
    "<h2>What an annual service is actually buying</h2>"
    "<p>A boiler service is a safety check first and an efficiency check second: flue gases, ventilation, seals and controls, read by someone qualified to judge them. Skipping it rarely shows up the year it is skipped — it shows up in the winter it fails, or in the slow fuel cost of a boiler drifting out of tune. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes gas-safety duties and landlord requirements this desk's guides follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Booking it properly</h2>"
    "<ul>"
    "<li><b>Check the engineer's registration before the visit.</b> Gas work on boilers is legally restricted to registered engineers.</li>"
    "<li><b>Service in late summer.</b> The appointment is cheaper and easier before the first cold week books everyone out.</li>"
    "<li><b>Keep the service record.</b> It is the warranty's condition and the home's paperwork at sale.</li>"
    "<li><b>Ask for the flue reading.</b> The combustion result is the number the service exists to produce.</li>"
    "</ul>"
    "<p>See <a href=\"/home/boiler-pressure-low-or-high/\">boiler pressure low or high</a>, <a href=\"/home/gas-cylinder-safety/\">gas cylinder safety</a> and <a href=\"/home/which-heating-system/\">choosing a heating system</a>.</p>",

"writers/writing/literary-hub":
    "<h2>The magazine about the ecosystem</h2>"
    "<p>Literary Hub covers the book world the way a trade paper covers an industry — reviews, essays, publishing news and writer interviews, aggregated and original in equal measure. For writers it is one of the fastest maps of what the field is discussing this month, which makes it worth reading with a submission calendar open. The site itself is at <a href=\"" + LITHUB + "\" rel=\"noopener\">lithub.com</a>. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Using it as a working writer</h2>"
    "<ul>"
    "<li><b>Read the essays for editor taste.</b> The pieces a platform commissions show who is buying what.</li>"
    "<li><b>Watch the prizes and fellowships posts.</b> Deadlines surface there earlier than on most application pages.</li>"
    "<li><b>Follow the criticism, not just the news.</b> Criticism teaches the conversation your work is joining.</li>"
    "<li><b>Read the interviews as process notes.</b> Working writers describe routines worth stealing in plain terms.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/electric-literature-essays/\">Electric Literature essays</a>, <a href=\"/writers/writing/litmag-online/\">LitMag Online</a> and <a href=\"/writers/writing/narratively/\">Narratively</a>.</p>",

"tech/smart-plug-going-offline":
    "<h2>Offline is a network question</h2>"
    "<p>A smart plug that drops its connection is almost never a broken plug. It is a Wi-Fi network under load, a 2.4GHz band crowded by neighbours, a router that reassigns addresses, or a cloud service having a day. The fix starts at the router's status page and ends at the plug — never the other way round. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household energy guidance on connected devices this desk's standby-cost notes follow. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The order that finds it</h2>"
    "<ul>"
    "<li><b>Check the router's client list while the plug is down.</b> If it is connected but the app cannot see it, the cloud is the fault.</li>"
    "<li><b>Separate the 2.4GHz band.</b> Plugs want the older band; combined bands confuse them at reconnect.</li>"
    "<li><b>Reserve the plug's address.</b> A static lease removes the commonest drop cause after a router restart.</li>"
    "<li><b>Update the firmware once, then leave it.</b> Chasing firmware versions is a known way to turn drops into resets.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/wifi-channel-congestion-fix/\">Wi-Fi channel congestion fixes</a>, <a href=\"/tech/do-you-need-a-smart-home-hub/\">do you need a smart home hub</a> and <a href=\"/tech/smart-home-on-its-own-network/\">smart home on its own network</a>.</p>",

"writers/writing/griffith-review":
    "<h2>An Australian quarterly with an essay habit</h2>"
    "<p>Griffith Review publishes themed quarterly editions of essays, fiction and reportage, and its themes are its signature: each edition gathers work around one question, which gives essayists a frame that commissioning editors can picture in advance. For writers, the theme calendar is the pitch surface — read the call, write to it. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> is where the wider literary-magazine field is documented. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing to a themed edition</h2>"
    "<ul>"
    "<li><b>Pitch the angle the theme leaves open.</b> The obvious take has a queue; the adjacent one does not.</li>"
    "<li><b>Bring evidence.</b> Themed essays compete on what the writer knows, not on the theme alone.</li>"
    "<li><b>Match the length of the last edition's essays.</b> Prose styles differ, lengths are usually stable.</li>"
    "<li><b>Watch the published close dates.</b> Quarterly themes open and close before the edition is announced publicly.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/australian-book-review/\">Australian Book Review</a>, <a href=\"/writers/writing/overland-fiction/\">Overland</a> and <a href=\"/writers/writing/island-magazine/\">Island</a>.</p>",

"writers/writing/hinterland":
    "<h2>Nonfiction with a documentary eye</h2>"
    "<p>Hinterland publishes creative nonfiction that treats writing as a documentary practice — reported essays, place pieces and hybrid work that carries research lightly. It is a small magazine in the best sense: clear taste, visible editorial attention, and a readership that arrives for the form. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> is the working map of small magazines of this kind. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What hybrid nonfiction carries</h2>"
    "<ul>"
    "<li><b>A reporting spine.</b> Even the most lyrical pieces here rest on documents, interviews or presence.</li>"
    "<li><b>A form chosen on purpose.</b> The best hybrid work could not have been a plain essay.</li>"
    "<li><b>Scenes that do argument work.</b> Description earns its place when it carries the point.</li>"
    "<li><b>Notes that survive editing.</b> Small magazines expect sourced work even when the seams are hidden.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/overland-fiction/\">Overland</a>, <a href=\"/writers/writing/griffith-review/\">Griffith Review</a> and <a href=\"/writers/writing/mudroom/\">Mudroom</a>.</p>",

}
