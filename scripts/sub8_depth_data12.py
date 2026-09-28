# -*- coding: utf-8 -*-
"""Editorial depth sections, part 12: batch H, the 654-668 word tranche against
the 750-word bar, two tools under the 669 tool bar (data-usage-estimator,
upload-time-calculator as t8b), plus t8b top-ups (premier-league-results,
github-token-hygiene). 56 pages total.
Every external URL from the curl-verified pool; every internal link verified
to a real page."""

WHO = "https://www.who.int/"
EPA = "https://www.epa.gov/"
GOVUK = "https://www.gov.uk/"
NFPA = "https://www.nfpa.org/"
CLMP = "https://www.clmp.org/"
PL = "https://www.premierleague.com/"
LITHUB = "https://lithub.com/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS12 = {

"tech/affinity-now-free":
    "<h2>What free actually means here</h2>"
    "<p>Canva's move made the full Affinity desktop applications free with a Canva account — photo editing, vector design and desktop publishing with the file formats designers already use, including layered PSD interchange. The economics shifted, but the tooling did not shrink: this is professional-grade software now funded by the platform around it. The <a href=\"" + _w("raster+graphics+editor") + "\" rel=\"noopener\">graphics editor category</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Who should switch today</h2>"
    "<ul>"
    "<li><b>Photo retouchers on a budget.</b> The develop and layer tooling covers the daily workflow.</li>"
    "<li><b>Vector work for print.</b> Affinity Designer handles the formats printers expect.</li>"
    "<li><b>Anyone paying monthly for occasional use.</b> The maths of a subscription only works when the software works weekly.</li>"
    "<li><b>Teams already in PSD.</b> Interchange is good enough for most handoffs; test the edge cases first.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/photopea-vs-photoshop/\">Photopea versus Photoshop</a>, <a href=\"/tech/canva-vs-adobe-express/\">Canva versus Adobe Express</a> and <a href=\"/tech/free-software-alternatives/\">free software alternatives</a>.</p>",

"tech/overfitting-detection-guide":
    "<h2>The signature of overfitting</h2>"
    "<p>Overfitting is a model that has memorised the past and calls it a signal — and the expensive part is that it feels like discovery. In-sample performance rises while genuine predictive power falls. The discipline that catches it is boring on purpose: hold out data the model never sees, and judge the system only there. The <a href=\"" + _w("overfitting") + "\" rel=\"noopener\">overfitting problem</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Detection habits that work</h2>"
    "<ul>"
    "<li><b>Walk-forward, not one split.</b> A single train/test cut can flatter any strategy.</li>"
    "<li><b>Watch parameter sensitivity.</b> If small changes flip the result, the result is noise.</li>"
    "<li><b>Count the experiments.</b> Tried a hundred variants and kept the best? That is the real test you must now pass.</li>"
    "<li><b>Write the rule before the data.</b> Hypotheses first, fitting second.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/backtest-validation-checklist/\">the backtest validation checklist</a>, <a href=\"/tech/lookahead-bias-explained/\">lookahead bias explained</a> and <a href=\"/tech/survivorship-bias-the-quiet-data-trap/\">survivorship bias</a>.</p>",

"writers/learn/dos-and-donts/dos-and-donts-of-an-essay":
    "<h2>Do: let the argument carry the page</h2>"
    "<p>An essay earns its length through argument, not description. Every paragraph should advance a claim a reader could disagree with; the introduction should state the position early enough that the reader knows why they are still reading. The <a href=\"" + _w("essay") + "\" rel=\"noopener\">essay form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The shortlist</h2>"
    "<ul>"
    "<li><b>Do</b> make one claim per paragraph and prove it before moving on.</li>"
    "<li><b>Don't</b> open with a dictionary definition — it signals you have nothing sharper.</li>"
    "<li><b>Do</b> end by answering the question, not by apologising for it.</li>"
    "<li><b>Don't</b> hedge every sentence; confidence is a feature of good essays.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-an-essay/\">how to write an essay</a>, <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-academic-writing/\">the dos and don'ts of academic writing</a> and <a href=\"/writers/learn/academic-writing/how-to-write-an-exam-essay/\">how to write an exam essay</a>.</p>",

"writers/learn/types-of-writing/how-to-write-an-essay":
    "<h2>The argument before the outline</h2>"
    "<p>Structure follows the claim. Decide what the essay is arguing first, then give each paragraph one job in that argument: establish the point, evidence it, and say why the evidence moves the claim forward. The classic introduction-body-conclusion shape is a container, not a plan. The <a href=\"" + _w("essay") + "\" rel=\"noopener\">essay form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Building the draft</h2>"
    "<ul>"
    "<li><b>Write the thesis as one sentence.</b> If it needs two, the argument is not decided yet.</li>"
    "<li><b>Order paragraphs by logic, not by discovery.</b> The reader never sees the order you found things in.</li>"
    "<li><b>Save the strongest point for its natural place.</b> Front-loading every good line makes an essay shouty.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-an-essay/\">the dos and don'ts of an essay</a>, <a href=\"/writers/learn/writing-basics/\">writing basics</a> and <a href=\"/writers/learn/academic-writing/how-to-structure-a-research-paper/\">how to structure a research paper</a>.</p>",

"tech/blue-screen-stop-code-triage":
    "<h2>What the stop code tells you</h2>"
    "<p>A blue screen is Windows shutting itself down to protect hardware and leaving a name behind: the stop code. The code narrows the field before any hardware is touched — memory faults, driver faults and storage faults each leave different signatures in the code and in the dump file. The <a href=\"" + _w("Blue+Screen+of+Death") + "\" rel=\"noopener\">blue screen</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The triage order</h2>"
    "<ul>"
    "<li><b>Write the code down first.</b> The reboot erases the only clue most users have.</li>"
    "<li><b>Recent change before deep diagnosis.</b> A driver installed this morning beats any theory.</li>"
    "<li><b>Memory and storage next.</b> Their tests are free and they cause most codes.</li>"
    "<li><b>One change, one reboot.</b> Fixing three things at once teaches nothing.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/pc-no-power-no-post-triage/\">PC no-power and no-POST triage</a>, <a href=\"/tech/how-to-read-an-error-message/\">how to read an error message</a> and <a href=\"/tech/laptop-no-display-boot-ladder/\">the laptop no-display boot ladder</a>.</p>",

"tech/photopea-vs-photoshop":
    "<h2>Where Photopea stops</h2>"
    "<p>Photopea opens and saves PSD files, runs in a browser tab and never uploads your file — the processing stays on your own machine. For most editing jobs it is genuinely enough. The gaps appear at the edges of professional work: some advanced filters, automation and the deep printing pipeline. The <a href=\"" + _w("raster+graphics+editor") + "\" rel=\"noopener\">graphics editor category</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing honestly</h2>"
    "<ul>"
    "<li><b>Occasional editors win.</b> No subscription, no install, files stay local.</li>"
    "<li><b>PSD handoffs mostly work.</b> Test your exact stack of smart objects before promising a client.</li>"
    "<li><b>Print and automation stay with the incumbents.</b> Colour management and batch pipelines are the moat.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/affinity-now-free/\">Affinity is free now</a>, <a href=\"/tech/canva-vs-adobe-express/\">Canva versus Adobe Express</a> and <a href=\"/tech/pixlr-vs-canva/\">Pixlr versus Canva</a>.</p>",

"home/hidden-water-leak-meter-test":
    "<h2>The two-number test</h2>"
    "<p>A hidden leak announces itself in meter readings, not on the ceiling. Read the meter, use no water for an hour, read it again: movement means water is leaving the system somewhere. The toilet cistern is the commonest culprit and food colouring settles that question in five minutes. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household leak guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The one quiet hour</h2>"
    "<ul>"
    "<li><b>Photograph both readings.</b> The argument with yourself is settled by numbers, not memory.</li>"
    "<li><b>Test the toilet first.</b> Silent cistern leaks waste more than drips.</li>"
    "<li><b>Check the run to any outbuilding.</b> Buried runs leak invisibly for months.</li>"
    "<li><b>Escalate on movement with everything off.</b> That is a plumber's job, not a guess.</li>"
    "</ul>"
    "<p>See <a href=\"/home/small-leak-ripple-effect/\">why a small leak never stays small</a>, <a href=\"/home/ceiling-water-stain-removal/\">ceiling water stain removal</a> and <a href=\"/home/dripping-tap-cartridge-fix/\">the dripping tap cartridge fix</a>.</p>",

"tech/monitor-dead-pixel-guide":
    "<h2>Dead, stuck, or dust</h2>"
    "<p>The black dot and the coloured dot are different faults. A dead pixel is dark and permanent; a stuck pixel is lit in one colour and occasionally negotiable; dust sits on the surface and moves when the screen does. Knowing which you have decides whether to try gentle pressure cycles or reach for the warranty. The <a href=\"" + _w("defective+pixel") + "\" rel=\"noopener\">defective pixel</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The thirty-second test</h2>"
    "<ul>"
    "<li><b>Full-screen solid colours.</b> Red, green, blue, white, black — every fault shows somewhere.</li>"
    "<li><b>Try the pressure method once.</b> Gentle, warm, and never on a warranty you value.</li>"
    "<li><b>Read the pixel policy before buying.</b> Manufacturers count allowed dead pixels in the small print.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/monitor-buying-specs/\">monitor buying specs</a>, <a href=\"/tech/monitor-refresh-rate-explained/\">refresh rate explained</a> and <a href=\"/tech/monitor-panel-type-for-text-work/\">panel types for text work</a>.</p>",

"home/washing-machine-heavy-items":
    "<h2>Why heavy loads break machines</h2>"
    "<p>Rubber-backed mats, rugs and weighted blankets hold water like a sponge and hit the drum asymmetrically at spin speed. The bearings take the punishment, the drum walks, and the repair bill approaches a new machine. The item's label usually warns; the machine's manual always does. The <a href=\"" + _w("washing+machine") + "\" rel=\"noopener\">washing machine</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What to do instead</h2>"
    "<ul>"
    "<li><b>Wash mats at a laundrette.</b> Their machines are built for the load.</li>"
    "<li><b>Never wash weighted blankets at home.</b> The filling decides, not the label's optimism.</li>"
    "<li><b>Balance small with small.</b> One heavy item alone is the worst case.</li>"
    "<li><b>Listen for the walk.</b> A machine that moves at spin is already losing.</li>"
    "</ul>"
    "<p>See <a href=\"/home/dryer-lint-every-load/\">dryer lint every load</a>, <a href=\"/home/dishwasher-loading-mistakes/\">dishwasher loading mistakes</a> and <a href=\"/home/appliances-that-use-the-most-electricity/\">appliances that use the most electricity</a>.</p>",

"writers/learn/common-problems":
    "<h2>The problems cluster</h2>"
    "<p>Writers bring the same handful of complaints: the introduction will not land, the prose sounds like a committee, and finished drafts read long. Each is a symptom of a fixable habit rather than a talent gap — usually structure decided too late, or editing skipped as a stage. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing craft</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Where each problem starts</h2>"
    "<ul>"
    "<li><b>Weak openings</b> usually mean the writer is still deciding the point. Decide first.</li>"
    "<li><b>Formal distance</b> usually means writing to impress rather than to inform.</li>"
    "<li><b>Endless drafts</b> usually mean no finishing rule. Set the cut line before you edit.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/common-problems/my-introduction-is-weak/\">my introduction is weak</a>, <a href=\"/writers/learn/common-problems/my-writing-sounds-too-formal/\">my writing sounds too formal</a> and <a href=\"/writers/learn/common-problems/how-to-tell-if-your-writing-is-good/\">how to tell if your writing is good</a>.</p>",

"entertainment/imax-and-70mm-explained":
    "<h2>Two different promises</h2>"
    "<p>70mm is a film format and a lens choice; IMAX is a capture and projection system with its own frame. A ticket labelled either promises scale, but they deliver different things — 70mm the image texture, IMAX the immersion. Marketing blurs the line constantly, which is why the print details matter at checkout. The <a href=\"" + _w("IMAX") + "\" rel=\"noopener\">IMAX system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Which ticket is worth it</h2>"
    "<ul>"
    "<li><b>Filmed in the format, projected in the format.</b> The only combination that delivers the promise.</li>"
    "<li><b>Shot on IMAX, shown on a big screen.</b> Still worth it; less than the full package.</li>"
    "<li><b>Blown up from another format.</b> Paying extra for a name — check before booking.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/aspect-ratios-in-film-explained/\">aspect ratios in film explained</a>, <a href=\"/entertainment/directors-cut-vs-theatrical-explained/\">director's cut versus theatrical</a> and <a href=\"/entertainment/how-movie-release-windows-work/\">how movie release windows work</a>.</p>",

"writers/learn/writing-process":
    "<h2>The loop that repeats</h2>"
    "<p>A writing process is a loop, not a ladder: draft fast with the editor off, rest the draft, edit with the reader on, then proof with the language tools out. Writers who skip the rest stage edit too early and sand the life out of the work. The <a href=\"" + _w("writing+process") + "\" rel=\"noopener\">writing process</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The four stations</h2>"
    "<ul>"
    "<li><b>Draft.</b> Momentum beats quality here; nothing said in draft is final.</li>"
    "<li><b>Rest.</b> Time is the cheapest editing tool available.</li>"
    "<li><b>Edit.</b> Structure, argument, cuts — the reader's needs in order.</li>"
    "<li><b>Proof.</b> Spelling and rhythm last, never first.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/editing-proofreading/how-to-edit-your-own-writing/\">how to edit your own writing</a>, <a href=\"/writers/learn/writing-basics/\">writing basics</a> and <a href=\"/writers/learn/editing-proofreading/\">editing and proofreading</a>.</p>",

"home/borehole-pump-no-water":
    "<h2>Prime, foot valve, or air leak</h2>"
    "<p>A pump that runs and delivers nothing has three usual suspects: lost prime, a failing foot valve, or an air leak on the suction line. Each announces itself differently — the sound, the pressure gauge and the first litre tell you which. Diagnosis before a rig saves a call-out. The <a href=\"" + _w("water+well") + "\" rel=\"noopener\">water well system</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The order of tests</h2>"
    "<ul>"
    "<li><b>Re-prime and listen.</b> An air-bound pump sounds wrong before it looks wrong.</li>"
    "<li><b>Check the foot valve.</b> Water running back down the borehole is the classic sign.</li>"
    "<li><b>Inspect every joint on the suction side.</b> Air gets in where water never gets out.</li>"
    "<li><b>Then suspect the table.</b> A dropping water level is seasonal; a dry borehole is structural.</li>"
    "</ul>"
    "<p>See <a href=\"/home/borehole-water-taste-smell/\">borehole water taste and smell</a>, <a href=\"/home/borehole-water-and-your-kettle/\">borehole water and your kettle</a> and <a href=\"/home/hidden-water-leak-meter-test/\">the hidden leak meter test</a>.</p>",

"sports/boxing-decisions-explained":
    "<h2>What the cards decide</h2>"
    "<p>Every boxing decision is arithmetic over scorecards the judges fill round by round. Unanimous, split and majority describe how much the three judges agreed — not how close the fight felt. A draw is one of the possible sums, and the rematches it forces are part of the business. The <a href=\"" + _w("boxing") + "\" rel=\"noopener\">boxing rules</a> are documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>The four outcomes</h2>"
    "<ul>"
    "<li><b>Unanimous.</b> All three judges agree on the winner.</li>"
    "<li><b>Split.</b> Two agree, one dissents — the argument lives on the cards.</li>"
    "<li><b>Majority.</b> Two agree, one scores it even.</li>"
    "<li><b>Draw.</b> The sums cannot separate them; the rematch sells itself.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/boxing-scoring-explained/\">boxing scoring explained</a>, <a href=\"/sports/how-boxing-fights-end-explained/\">how boxing fights end</a> and <a href=\"/sports/boxing-rounds-and-fight-length-explained/\">rounds and fight length</a>.</p>",

"tech/powerline-adapters-old-wiring":
    "<h2>Why the wiring is the network</h2>"
    "<p>A powerline adapter turns your home's electrical circuit into the cable — so the circuit's quality is the network's quality. Old wiring, multiple consumer units and the meter between phases each cut throughput sharply, and no adapter's box speed survives a bad run. The <a href=\"" + _w("power-line+communication") + "\" rel=\"noopener\">power-line communication</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Before you buy</h2>"
    "<ul>"
    "<li><b>Check the meter boundary.</b> Adapters rarely cross it; keep both units on one side.</li>"
    "<li><b>Avoid extension leads and surge strips.</b> They filter exactly the signal you need.</li>"
    "<li><b>Test on a borrowed pair.</b> The same kit that flies in one flat can die in the next room.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/ethernet-cable-categories-honest/\">ethernet cable categories, honestly</a>, <a href=\"/tech/wifi-channel-congestion-fix/\">the Wi-Fi channel congestion fix</a> and <a href=\"/tech/router-placement-nigerian-flat/\">router placement in a Nigerian flat</a>.</p>",

"writers/learn/types-of-writing/how-to-write-a-screenplay":
    "<h2>Write what the camera sees</h2>"
    "<p>A screenplay is instructions for a film, not a story on the page: what the camera sees, what the ear hears, and nothing else. Standard format exists so a reader can time the film while reading — slug lines, action in present tense, dialogue under names. The <a href=\"" + _w("screenplay") + "\" rel=\"noopener\">screenplay form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The habits that read professional</h2>"
    "<ul>"
    "<li><b>Trust the image.</b> If the shot carries it, the line is padding.</li>"
    "<li><b>Give every character a want.</b> Scenes without wants are descriptions.</li>"
    "<li><b>Enter late, leave early.</b> The oldest cut that instantly improves a scene.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/screenplay-format-basics/\">screenplay format basics</a>, <a href=\"/writers/guides/where-to-start-with-a-screenplay/\">where to start with a screenplay</a> and <a href=\"/writers/learn/creative-writing/how-to-write-dialogue/\">how to write dialogue</a>.</p>",

"home/small-leak-ripple-effect":
    "<h2>What the drip actually costs</h2>"
    "<p>Household leaks waste thousands of gallons a year in the average home — and water is the cheap part. Behind the waste sits rot, mould and the slow structural damage that appears once the plaster gives up. A drip you can hear is a warning system still working. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household leak guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Why early wins matter</h2>"
    "<ul>"
    "<li><b>Water travels.</b> The stain is rarely directly under the leak.</li>"
    "<li><b>Insurance asks when you knew.</b> Delay converts a repair into a dispute.</li>"
    "<li><b>Mould follows moisture.</b> The health bill arrives with the structural one.</li>"
    "</ul>"
    "<p>See <a href=\"/home/hidden-water-leak-meter-test/\">the hidden leak meter test</a>, <a href=\"/home/ceiling-leak-11pm/\">the ceiling leak at 11pm</a> and <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">condensation versus rising versus penetrating damp</a>.</p>",

"writers/learn/types-of-writing/how-to-write-an-article":
    "<h2>The lede earns the read</h2>"
    "<p>An article is reporting shaped for a reader: the lede carries the news, the nut graf carries the meaning, and the rest earns the trust the opening spent. Feature or news, the same spine holds — find the story, verify it, then structure the telling. The <a href=\"" + _w("news+writing") + "\" rel=\"noopener\">news writing form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Structure that holds up</h2>"
    "<ul>"
    "<li><b>One story per article.</b> The second story is the next pitch.</li>"
    "<li><b>Quote for evidence, not decoration.</b> A source that changes the reader's mind is the one to cut to.</li>"
    "<li><b>End on the news, not on a shrug.</b> Kicker endings are written, never discovered.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-a-blog-post/\">how to write a blog post</a>, <a href=\"/writers/guides/how-to-submit-a-freelance-article/\">how to submit a freelance article</a> and <a href=\"/writers/learn/online-writing/how-to-write-search-friendly-content/\">how to write search-friendly content</a>.</p>",

"entertainment/movies-like-parasite":
    "<h2>What to watch for next</h2>"
    "<p>Parasite's recipe is specific: class tension played as genre, tonal shifts that turn on a scene, and a house as a set of social stairs. Films that share the recipe rarely copy the plot — they share the discipline of escalation and the willingness to change the film's rules midstream. The <a href=\"" + _w("Parasite+%282019+film%29") + "\" rel=\"noopener\">Parasite</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Where the tension lives</h2>"
    "<ul>"
    "<li><b>Class as plot, not backdrop.</b> The best of these make status physical.</li>"
    "<li><b>One tonal turn per act.</b> The gear change is the thrill.</li>"
    "<li><b>Architecture with opinions.</b> Stairs, doors and sightlines do the arguing.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/10-korean-movies-everyone-should-watch/\">ten Korean movies everyone should watch</a>, <a href=\"/entertainment/best-thriller-movies-of-all-time/\">the best thrillers of all time</a> and <a href=\"/entertainment/best-horror-movies-of-all-time/\">the best horror movies of all time</a>.</p>",

"home/ceiling-fan-mounting-right":
    "<h2>The box, the rod, the brace</h2>"
    "<p>A ceiling fan is a spinning weight, and the mounting is the engineering that keeps it overhead. The electrical box must be rated for fan weight, the downrod sets the blade height that moves air, and the brace spans the joists the box hangs from. Fans that wobble are telling you one of the three is wrong. The <a href=\"" + _w("ceiling+fan") + "\" rel=\"noopener\">ceiling fan</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Getting the mount right</h2>"
    "<ul>"
    "<li><b>Fan-rated box, always.</b> Light boxes fail under spin load.</li>"
    "<li><b>Match downrod to ceiling height.</b> Blades need clearance to move air, not decor.</li>"
    "<li><b>Balance after mounting.</b> The kit's clip and weight find the wobble cheaply.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ceiling-fan-direction-summer-winter/\">ceiling fan direction in summer and winter</a>, <a href=\"/home/ceiling-fan-vs-standing-fan/\">ceiling fan versus standing fan</a> and <a href=\"/home/ceiling-light-flicker-fix/\">the ceiling light flicker fix</a>.</p>",

"home/co-smoke-alarm-expiry":
    "<h2>Ten years, then retire</h2>"
    "<p>Smoke alarms carry expiry dates nobody reads: ten years from manufacture for the sensor, often sooner for carbon monoxide cells. The test button checks the circuit, not the sensing chamber — a past-date alarm can pass every weekly test and fail the fire. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the replacement guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The expiry routine</h2>"
    "<ul>"
    "<li><b>Read the back of the unit.</b> Manufacture date decides retirement, not installation date.</li>"
    "<li><b>CO alarms retire early.</b> Their sensors have shorter honest lives than smoke chambers.</li>"
    "<li><b>Replace, never repair.</b> A sealed unit's failure is not a maintenance problem.</li>"
    "</ul>"
    "<p>See <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a>, <a href=\"/home/cooking-oil-fire-plan/\">the cooking oil fire plan</a> and <a href=\"/home/dryer-vent-cleaning-fire-risk/\">dryer vent cleaning and fire risk</a>.</p>",

"tech/domain-names-explained":
    "<h2>What the annual fee actually buys</h2>"
    "<p>A domain rental is what the annual fee buys: the registration, the right to renew, and a listing in someone else's database. Teaser pricing, premium tiers and the sixty-day transfer lock are all policy, not technology. The <a href=\"" + _w("domain+name") + "\" rel=\"noopener\">domain name system</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the registrar deal</h2>"
    "<ul>"
    "<li><b>Check the renewal price first.</b> The teaser year is marketing; the third year is the product.</li>"
    "<li><b>Whois privacy should be standard.</b> Paying for it is a choice of registrar, not of the system.</li>"
    "<li><b>Know the sixty-day lock.</b> Fresh registrations and some transfers cannot move for two months.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/custom-domain-dns-order/\">custom domain DNS, in order</a>, <a href=\"/tech/dns-not-working-propagation/\">DNS not working: propagation</a> and <a href=\"/tech/free-vs-paid-hosting/\">free versus paid hosting</a>.</p>",

"tech/phone-died-no-backup":
    "<h2>The first thirty minutes</h2>"
    "<p>Phones are the most-lost, most-damaged and least-backed-up computers in daily life. When one dies without a backup, the first thirty minutes decide how much data survives: stop powering it, stop charging it if water is involved, and check whether the cloud was quietly doing its job. The <a href=\"" + _w("backup") + "\" rel=\"noopener\">backup discipline</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The recovery order</h2>"
    "<ul>"
    "<li><b>Check cloud sync first.</b> Photos, contacts and messages often live elsewhere already.</li>"
    "<li><b>Water damage: no power.</b> Every attempt to boot multiplies the damage.</li>"
    "<li><b>Physical recovery is a last resort.</b> Pay for it only when the data is worth the gamble.</li>"
    "<li><b>Then build the backup you wished for.</b> It takes one evening.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-backup-guide/\">the Android backup guide</a>, <a href=\"/tech/phone-photo-backup-options-nigeria/\">phone photo backup options in Nigeria</a> and <a href=\"/tech/three-two-one-backup-rule/\">the 3-2-1 backup rule</a>.</p>",

"tech/streaming-quality-vs-broadcast-bitrate":
    "<h2>Bitrate is the product</h2>"
    "<p>Two services can both sell '4K' while one sends five megabits a second and the other twenty-five. Bitrate — the raw data delivered per second — is what compression lives on, and the aerial's old broadcast signal often carries more of it than the streaming app's best tier. The <a href=\"" + _w("bitrate") + "\" rel=\"noopener\">bitrate</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What the difference looks like</h2>"
    "<ul>"
    "<li><b>Dark, busy scenes show compression first.</b> Fire, confetti and night shots are the stress test.</li>"
    "<li><b>Live streams carry the least data.</b> The encoder's clock does not wait for your screen.</li>"
    "<li><b>Your connection's bad moments cut quality before they buffer.</b> Adaptive streaming downgrades silently.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/streaming-quality-settings/\">streaming quality settings</a>, <a href=\"/tech/hours-of-video-per-gigabyte/\">hours of video per gigabyte</a> and <a href=\"/tech/antenna-vs-satellite-vs-streaming-live-tv/\">antenna versus satellite versus streaming</a>.</p>",

"tech/website-not-indexing-google":
    "<h2>The diagnostic order</h2>"
    "<p>A missing page is almost never a mystery by the time Search Console is open. The checks run in a fixed order — is it crawled, is it allowed, is it canonical, is it quality — because each step names the class of blocker before you touch anything. The <a href=\"" + _w("search+engine+indexing") + "\" rel=\"noopener\">indexing process</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The nine checks, compressed</h2>"
    "<ul>"
    "<li><b>site: search first.</b> It answers 'indexed?' in two seconds.</li>"
    "<li><b>Then the URL Inspection tool.</b> It names the crawl verdict.</li>"
    "<li><b>Robots, canonicals, noindex.</b> The three self-inflicted blockers.</li>"
    "<li><b>Quality last.</b> Thin pages get quietly dropped, without a message.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/check-if-google-indexed-your-page/\">check if Google indexed your page</a>, <a href=\"/tech/sitemap-indexnow/\">sitemap and IndexNow</a> and <a href=\"/tech/how-to-get-cited-by-ai-search/\">how to get cited by AI search</a>.</p>",

"writers/learn/academic-writing/how-to-structure-a-research-paper":
    "<h2>What each section does</h2>"
    "<p>A research paper's sections are a contract with the reader: the introduction states the question, methods make the work repeatable, results report what happened, and the discussion says what it means. The structure is a container, not a plan. The <a href=\"" + _w("IMRaD") + "\" rel=\"noopener\">IMRaD structure</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The section contract</h2>"
    "<ul>"
    "<li><b>Introduction.</b> The gap in the field, stated so a stranger can care.</li>"
    "<li><b>Methods.</b> Enough detail that a peer could repeat the study — the standard that keeps the field honest.</li>"
    "<li><b>Results.</b> The findings without the arguments; the data's day in court.</li>"
    "<li><b>Discussion.</b> What it means, what it does not, and what happens next.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/academic-writing/how-to-write-a-thesis/\">how to write a thesis</a>, <a href=\"/writers/learn/academic-writing/how-to-cite-sources/\">how to cite sources</a> and <a href=\"/writers/learn/academic-writing/how-to-write-a-literature-review/\">how to write a literature review</a>.</p>",

"writers/learn/dos-and-donts":
    "<h2>The rules that travel</h2>"
    "<p>Every genre has its own conventions, but a handful of rules travel across all of them: write for the reader, cut what does not carry weight, and make the point early enough to be checked. The rest of this library is those rules applied in context. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing craft</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The travelling set</h2>"
    "<ul>"
    "<li><b>Clarity before style.</b> Style is what remains when the confusion is gone.</li>"
    "<li><b>One idea per sentence.</b> Readers parse; they do not unpack.</li>"
    "<li><b>Finish before polishing.</b> Drafts improve; half-drafts only shrink.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-writing/\">the dos and don'ts of writing</a>, <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-an-essay/\">the dos and don'ts of an essay</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-blogging/\">the dos and don'ts of blogging</a>.</p>",

"writers/learn/grammar-language/common-grammar-mistakes":
    "<h2>The errors that cost the most</h2>"
    "<p>Most grammar mistakes are cheap to fix and expensive to keep: the its/it's family, comma splices and subject-verb disagreement each make readers recalculate the writer's competence mid-sentence. The fixes are rules, not tastes — learnable in an afternoon and worth the afternoon. The <a href=\"" + _w("English+grammar") + "\" rel=\"noopener\">English grammar</a> rules are documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Fix the habit, not the sentence</h2>"
    "<ul>"
    "<li><b>Its versus it's.</b> One is possession, one is a contraction; the apostrophe is the whole difference.</li>"
    "<li><b>The comma splice.</b> Two full sentences need more than a comma's salary.</li>"
    "<li><b>Agreement under load.</b> Long subjects hide their number; read the verb against the head word.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/grammar-language/\">grammar and language</a>, <a href=\"/writers/learn/editing-proofreading/\">editing and proofreading</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-writing/\">the dos and don'ts of writing</a>.</p>",

"writers/learn/professional-writing/how-to-write-a-grant-application":
    "<h2>Make the case fundable</h2>"
    "<p>A grant application is an argument with a budget attached: the need is real, the plan is credible, and the money has a job it can be held to. Funders read for evidence of both need and capacity — the best applications make the reader's decision easy rather than impressive. The <a href=\"" + _w("grant+writing") + "\" rel=\"noopener\">grant writing discipline</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What funders check</h2>"
    "<ul>"
    "<li><b>The need, evidenced.</b> One number that matters beats a page of adjectives.</li>"
    "<li><b>The plan, costed honestly.</b> Budgets that survive scrutiny are built before the prose.</li>"
    "<li><b>The accountability.</b> How will you know, and how will they?</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/professional-writing/how-to-write-a-formal-appeal/\">how to write a formal appeal</a>, <a href=\"/writers/learn/professional-writing/how-to-write-a-business-letter/\">how to write a business letter</a> and <a href=\"/writers/learn/freelance-paid-writing/how-to-price-your-freelance-writing/\">how to price your freelance writing</a>.</p>",

"writers/learn/types-of-writing/how-to-write-a-press-release":
    "<h2>Write it like the newsdesk wants</h2>"
    "<p>A press release is a news story about something that has not been covered yet, written so an editor can lift it intact: headline that states the news, dateline, the story in the first paragraph, and quotes that add the human evidence. Everything else is boilerplate. The <a href=\"" + _w("press+release") + "\" rel=\"noopener\">press release form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The format journalists use</h2>"
    "<ul>"
    "<li><b>The headline is the news.</b> If it needs reading twice, it is a slogan.</li>"
    "<li><b>First paragraph answers who, what, when, where, why.</b> The rest is optional in the editor's mind.</li>"
    "<li><b>Boilerplate last.</b> The company description is not the story; it is the receipt.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-an-article/\">how to write an article</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-a-blog-post/\">how to write a blog post</a> and <a href=\"/writers/guides/how-to-submit-a-freelance-article/\">how to submit a freelance article</a>.</p>",

"writers/writing/the-stinging-fly":
    "<h2>What the magazine pays for</h2>"
    "<p>The Stinging Fly pays per magazine page for fiction and nonfiction — with a stated minimum and maximum — and flat rates for flash and poetry, terms that put it among the honest Irish markets. It favours work that surprises the form over work that performs it. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Before you submit</h2>"
    "<ul>"
    "<li><b>Read a recent issue.</b> The magazine's taste is on the page, not on the guidelines.</li>"
    "<li><b>Mind the reading window.</b> The open periods are the whole submission policy.</li>"
    "<li><b>Submit the piece that fits, not the best piece.</b> Fit decides more acceptances than polish.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/the-drift/\">The Drift</a>, <a href=\"/writers/writing/the-sun-magazine/\">The Sun Magazine</a> and <a href=\"/writers/writing/statement-africa/\">Statement Africa</a>.</p>",

"entertainment/directors-cut-vs-theatrical-explained":
    "<h2>Who decided the runtime</h2>"
    "<p>The same film can exist in four labelled versions, each a different contract between studio, director and runtime: theatrical for the release plan, director's cut for the author, extended edition for the shelf. The labels are marketing and history at once — and the differences range from a restored subplot to a different ending. The <a href=\"" + _w("director%27s+cut") + "\" rel=\"noopener\">director's cut</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the labels</h2>"
    "<ul>"
    "<li><b>Theatrical.</b> The cut that was sold; pacing tuned by test screenings.</li>"
    "<li><b>Director's cut.</b> The director's case, sometimes years after the fact.</li>"
    "<li><b>Extended or unrated.</b> More footage is not always a better film.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/imax-and-70mm-explained/\">IMAX and 70mm explained</a>, <a href=\"/entertainment/aspect-ratios-in-film-explained/\">aspect ratios in film explained</a> and <a href=\"/entertainment/how-movie-release-windows-work/\">how movie release windows work</a>.</p>",

"entertainment/how-movie-trailers-are-made":
    "<h2>The ninety-second film</h2>"
    "<p>A trailer is a film about a film, made by people who usually did not direct either: specialist trailer houses cut to test scores and test audiences, months before release, with notes flying from marketing, producers and the director. The finished ninety seconds are a negotiated artefact. The <a href=\"" + _w("trailer+%28promotion%29") + "\" rel=\"noopener\">film trailer</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>How the sausage is graded</h2>"
    "<ul>"
    "<li><b>Temp music sets the rhythm first.</b> The famous trailer sound is a borrowed language.</li>"
    "<li><b>Test screenings steer the cut.</b> Confusion in a room becomes a reshuffled reel.</li>"
    "<li><b>Teaser and final trailer do different jobs.</b> One sells a world, one sells the plot's promise.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-movie-budgets-work/\">how movie budgets work</a>, <a href=\"/entertainment/how-box-office-works/\">how box office works</a> and <a href=\"/entertainment/how-award-season-actually-works/\">how award season actually works</a>.</p>",

"tech/api-returns-error-diagnostic":
    "<h2>Read the code before the message</h2>"
    "<p>API errors are conversations in a fixed vocabulary: the status code tells you which side failed and why the contract was broken, and the message is a footnote. 401 versus 403, 404 versus 410, 429 as a rate limit — each names a different fix. The <a href=\"" + _w("HTTP+status+code") + "\" rel=\"noopener\">HTTP status code</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The diagnostic tree</h2>"
    "<ul>"
    "<li><b>401: who are you.</b> Credentials and token expiry live here.</li>"
    "<li><b>403: who you are is not enough.</b> Scope and permissions, not passwords.</li>"
    "<li><b>429: slow down.</b> Backoff is the fix; the clock is in the headers.</li>"
    "<li><b>CORS errors are not server errors.</b> The browser is talking; the API answered fine.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/http-status-codes-explained/\">HTTP status codes explained</a>, <a href=\"/tech/handle-api-errors-python/\">handling API errors in Python</a> and <a href=\"/tech/how-to-read-an-error-message/\">how to read an error message</a>.</p>",

"writers/writing/uncanny-poetry":
    "<h2>Speculative poetry, professionally</h2>"
    "<p>Uncanny Magazine buys original unpublished speculative poetry during fixed annual reading windows, at professional rates and with guidelines that respect the form's length range. For poets, the window is the whole strategy: the work must be ready before the door opens. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Track the window.</b> Closed means closed; the calendar is the policy.</li>"
    "<li><b>Speculative means the idea is load-bearing.</b> Atmosphere alone rarely clears the bar.</li>"
    "<li><b>Follow the length guidance.</b> Every market has poems it cannot physically print.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/strange-horizons-fiction/\">Strange Horizons fiction</a>, <a href=\"/writers/writing/space-and-time/\">Space and Time</a> and <a href=\"/writers/writing/shoreline-of-infinity/\">Shoreline of Infinity</a>.</p>",

"tech/bitwarden-free-password-manager":
    "<h2>What the free tier covers</h2>"
    "<p>Bitwarden's free account still covers unlimited passwords on unlimited devices — the part of password management that matters for security, left free on purpose. Sharing and reporting live in the paid tiers, which suits households better than individuals. The <a href=\"" + _w("password+manager") + "\" rel=\"noopener\">password manager</a> category is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Getting the most of free</h2>"
    "<ul>"
    "<li><b>Turn on two-factor for the vault itself.</b> The account guards everything else.</li>"
    "<li><b>Run the breach reports when offered.</b> Reused passwords are the actual risk.</li>"
    "<li><b>Keep the emergency sheet.</b> The master password resets nothing if it is forgotten.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/best-password-manager-for-you/\">the best password manager for you</a>, <a href=\"/tech/password-manager-or-browser/\">password manager or browser</a> and <a href=\"/tech/password-manager-migration-weekend/\">the password manager migration weekend</a>.</p>",

"writers/learn/academic-writing/how-to-cite-sources":
    "<h2>Citation is an argument</h2>"
    "<p>Citation is how scholarship says where the ground under a claim is solid: the in-text marker points to the reference list, the reference list points to the evidence, and the chosen style keeps the whole apparatus readable. Consistency matters more than the style you pick. The <a href=\"" + _w("citation") + "\" rel=\"noopener\">citation practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Citing honestly</h2>"
    "<ul>"
    "<li><b>Cite the claim you actually used.</b> The source you skimmed is not the source you used.</li>"
    "<li><b>One style, all the way through.</b> Mixed styles read as carelessness, not range.</li>"
    "<li><b>Quote the page, paraphrase the idea.</b> Both need the marker; only one needs the words.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/academic-writing/how-to-structure-a-research-paper/\">how to structure a research paper</a>, <a href=\"/writers/learn/academic-writing/how-to-write-a-literature-review/\">how to write a literature review</a> and <a href=\"/writers/learn/common-problems/how-plagiarism-and-ai-checkers-are-made/\">how plagiarism and AI checkers are made</a>.</p>",

"writers/learn/freelance-paid-writing/how-to-price-your-freelance-writing":
    "<h2>A rate is a defence</h2>"
    "<p>Per-word, per-piece or per-day: the unit is less important than the boundary. A rate is a defence against scope — it names what the client is buying and what is a new conversation. Rates vary widely by market and niche; what does not vary is the discipline of quoting the job, not the hour. The <a href=\"" + _w("freelancing") + "\" rel=\"noopener\">freelancing model</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Setting a rate you can defend</h2>"
    "<ul>"
    "<li><b>Price the deliverable.</b> Clients buy outcomes; hours invite negotiation against you.</li>"
    "<li><b>Write the revision count into the quote.</b> The undefined draft is where rates die.</li>"
    "<li><b>Raise on the next engagement.</b> Loyalty discounts are a choice, not a rule.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-much-to-charge-for-an-article/\">how much to charge for an article</a>, <a href=\"/writers/learn/freelance-paid-writing/per-word-day-rate-or-project-fee/\">per-word, day rate or project fee</a> and <a href=\"/writers/learn/freelance-paid-writing/how-to-raise-your-freelance-rates/\">how to raise your freelance rates</a>.</p>",

"entertainment/how-oscars-voting-works-explained":
    "<h2>Preferential, not popular</h2>"
    "<p>The Oscars are not a verdict of the public, or even of a single committee: thousands of members vote within their branches for nominations, and Best Picture uses a preferential ballot that rewards broadly liked films over passionately loved ones. The system's design explains most of its surprises. The <a href=\"" + _w("Academy+Awards") + "\" rel=\"noopener\">Academy Awards</a> process is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Where upsets come from</h2>"
    "<ul>"
    "<li><b>Branches nominate their own.</b> Editors pick editing; actors pick actors.</li>"
    "<li><b>The preferential count rewards consensus.</b> Second-choice votes decide close years.</li>"
    "<li><b>Campaigns work on both electorates.</b> Nominations and wins need different arguments.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-award-season-actually-works/\">how award season actually works</a>, <a href=\"/entertainment/how-box-office-works/\">how box office works</a> and <a href=\"/entertainment/how-cinematic-universes-work/\">how cinematic universes work</a>.</p>",

"entertainment/nollywood-golden-age-explained":
    "<h2>The video economy that built it</h2>"
    "<p>Nollywood's origin story runs on videotape: cheap cameras, weekend shoots, and a distribution network of market stalls that moved films faster than any cinema chain could. The budgets were rumours and the schedules were punishing, but the volume built an audience across a continent. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood industry</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the golden age changed</h2>"
    "<ul>"
    "<li><b>Distribution was the innovation.</b> The market stall was the streaming service of its decade.</li>"
    "<li><b>Volume created the stars.</b> Audiences met actors faster than critics did.</li>"
    "<li><b>The economics shaped the art.</b> Tight schedules taught dialogue and performance to carry production.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a>, <a href=\"/entertainment/film-movements-explained/\">film movements explained</a> and <a href=\"/entertainment/how-movie-budgets-work/\">how movie budgets work</a>.</p>",

"entertainment/reviews/mokalik":
    "<h2>What the day in the workshop reveals</h2>"
    "<p>Mokalik follows an eleven-year-old across one day in a mechanic's workshop, and the film's intelligence is in its observation: the boy learns class the way children do, by noticing who holds the tools. The workshop scenes carry the texture that the coming-of-age frame organises. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What stays with you</h2>"
    "<ul>"
    "<li><b>The performances breathe.</b> The workshop ensemble plays status, not plot.</li>"
    "<li><b>The child's eye view is exact.</b> Class arrives as observation, never as speech.</li>"
    "<li><b>The runtime respects the day.</b> A small frame carrying a large subject.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/nollywood-golden-age-explained/\">Nollywood's golden age</a>, <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a> and <a href=\"/entertainment/film-movements-explained/\">film movements explained</a>.</p>",

"home/gas-cooker-wont-ignite":
    "<h2>Igniter, gas, or crumb</h2>"
    "<p>The clicking cooker splits into three cases in three minutes: a wet or dirty igniter, a gas supply problem, or debris in the burner. The sound, the smell and the spark tell you which — and the match test splits the diagnosis in half. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government gas safety guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The three-minute diagnosis</h2>"
    "<ul>"
    "<li><b>Dry the cap and the igniter.</b> Moisture is the commonest click-without-flame.</li>"
    "<li><b>Listen for gas.</b> No hiss at the burner is a supply question, not a spark question.</li>"
    "<li><b>Clear the burner ports.</b> Boil-over crumbs block the flame ring.</li>"
    "<li><b>Smell gas at any point: stop.</b> Ventilate and call the engineer — that boundary is not diagnostic.</li>"
    "</ul>"
    "<p>See <a href=\"/home/uk-us-plumber-rules/\">UK and US plumber rules</a>, <a href=\"/home/cooking-oil-fire-plan/\">the cooking oil fire plan</a> and <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a>.</p>",

"tech/how-to-tell-if-an-app-is-safe":
    "<h2>The pre-install check</h2>"
    "<p>An app's safety is readable before install: the developer's track record, the permission list against the app's actual job, the review patterns and the install count together make the picture. Four minutes of checking beats any post-install scanner. The <a href=\"" + _w("mobile+security") + "\" rel=\"noopener\">mobile security</a> field is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The four checks</h2>"
    "<ul>"
    "<li><b>Permissions against purpose.</b> A torch app wanting contacts is confessing.</li>"
    "<li><b>Review patterns, not stars.</b> Five-star bursts with no detail are bought.</li>"
    "<li><b>Install count and history.</b> Old apps with big counts have survived scrutiny.</li>"
    "<li><b>Official store, always.</b> Sideloaded APKs carry the risk the store's review absorbs.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-app-permissions/\">Android app permissions</a>, <a href=\"/tech/how-to-spot-a-suspicious-link/\">how to spot a suspicious link</a> and <a href=\"/tech/public-wifi-risks/\">public Wi-Fi risks</a>.</p>",

"tech/why-phones-slow-down":
    "<h2>Four kinds of drag</h2>"
    "<p>Phone slowdown is not one thing but four: batteries under load throttle the processor, full storage starves the system, app bloat eats the background, and updates eventually outgrow old hardware. Two of the four are fixable this week; one is maintenance; one is time. The <a href=\"" + _w("lithium-ion+battery") + "\" rel=\"noopener\">lithium-ion battery</a> behaviour is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What to fix first</h2>"
    "<ul>"
    "<li><b>Free storage before anything.</b> Flash storage slows as it fills.</li>"
    "<li><b>Audit background apps.</b> The list of what runs at boot is the list of what slows it.</li>"
    "<li><b>Check battery health.</b> Throttling for an ageing battery feels exactly like ageing hardware.</li>"
    "<li><b>Then decide about the update.</b> Sometimes the phone is simply done.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-battery-health/\">Android battery health</a>, <a href=\"/tech/free-up-storage-android/\">free up storage on Android</a> and <a href=\"/tech/phone-battery-charging-myths/\">phone battery charging myths</a>.</p>",

"writers/learn/dos-and-donts/dos-and-donts-of-writing":
    "<h2>The universal rules</h2>"
    "<p>A few rules improve almost every kind of writing: cut the words that carry nothing, prefer verbs to nouns about verbs, and read the draft aloud before calling it done. These are not styles; they are what remains when the writing works. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing craft</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The shortlist</h2>"
    "<ul>"
    "<li><b>Do</b> read it aloud — the ear catches what the eye forgives.</li>"
    "<li><b>Don't</b> open with throat-clearing; the first sentence is the promise.</li>"
    "<li><b>Do</b> cut adjectives doing an adverb's job.</li>"
    "<li><b>Don't</b> explain the joke twice; once is the joke.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-basics/\">writing basics</a>, <a href=\"/writers/learn/dos-and-donts/\">the dos and don'ts library</a> and <a href=\"/writers/learn/editing-proofreading/how-to-make-writing-more-concise/\">how to make writing more concise</a>.</p>",

"home/vacuum-lost-suction-fix":
    "<h2>Filter, hose, brush roll</h2>"
    "<p>Lost suction is a blockage question with three usual addresses: a filter washed and reinstalled damp, a hose holding the missing sock, or a brush roll wrapped into stillness. Each produces its own sound, and ten minutes of listening saves the repair booking. The <a href=\"" + _w("vacuum+cleaner") + "\" rel=\"noopener\">vacuum cleaner</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The ten-minute pass</h2>"
    "<ul>"
    "<li><b>Never wash a foam filter and refit it wet.</b> Damp ruins suction for the week.</li>"
    "<li><b>The hose test.</b> Detach and listen: the blockage is in whichever half loses the sound.</li>"
    "<li><b>Cut the brush roll free.</b> Hair and thread do what they do at every rotation.</li>"
    "</ul>"
    "<p>See <a href=\"/home/dryer-lint-every-load/\">dryer lint every load</a>, <a href=\"/home/deep-clean-schedule/\">the deep clean schedule</a> and <a href=\"/home/washing-machine-heavy-items/\">washing machine heavy items</a>.</p>",

"sports/xg-explained":
    "<h2>A probability, not a verdict</h2>"
    "<p>Expected goals turns every shot into a number: the chance that this shot, from this spot, against this keeper, becomes a goal. It measures chance quality over a season better than shots or possession ever did — and it says nothing at all about the next shot. The <a href=\"" + _w("expected+goals") + "\" rel=\"noopener\">expected goals model</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Using xG honestly</h2>"
    "<ul>"
    "<li><b>Sample size decides everything.</b> Ten games of xG is a direction, not a table.</li>"
    "<li><b>Every model disagrees a little.</b> Comparing providers, compare methods first.</li>"
    "<li><b>Finishing skill is real, and small.</b> The variance is mostly not skill.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-goal-line-technology-works/\">how goal-line technology works</a>, <a href=\"/sports/how-the-premier-league-table-works/\">how the Premier League table works</a> and <a href=\"/sports/how-football-scouting-works/\">how football scouting works</a>.</p>",

"home/stain-ladder-household":
    "<h2>Heat saves or heat sets</h2>"
    "<p>Stain removal is a ladder: which solvent, which order, and crucially, which temperature. Oil wants detergent before water, rust wants acid and never bleach, and dye needs patience — while heat sets many stains permanently. The one-minute rule beats every product. The <a href=\"" + _w("stain+removal") + "\" rel=\"noopener\">stain removal practice</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The household ladder</h2>"
    "<ul>"
    "<li><b>Blot, never rub.</b> Rubbing trades a stain for a worn patch.</li>"
    "<li><b>Oil first with detergent.</b> Water-first pushes oil deeper into the fibre.</li>"
    "<li><b>Rust needs acid.</b> Bleach on rust sets it; the wrong direction entirely.</li>"
    "<li><b>Heat is the last step.</b> Dryers set stains that washing would have released.</li>"
    "</ul>"
    "<p>See <a href=\"/home/washing-machine-heavy-items/\">washing machine heavy items</a>, <a href=\"/home/ceiling-water-stain-removal/\">ceiling water stain removal</a> and <a href=\"/home/bathroom-grout-mould/\">bathroom grout mould</a>.</p>",

"writers/writing/carte-blanche":
    "<h2>A Quebec market with range</h2>"
    "<p>carte blanche, published by the Quebec Writers' Federation, pays a modest honorarium per accepted submission and works across fiction, nonfiction and poetry with a distinctly literary eye. For writers it is a market where the conversation matters as much as the craft. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Read the theme issues.</b> Themed calls decide fit absolutely.</li>"
    "<li><b>Simultaneous submissions are the norm.</b> Withdraw promptly on acceptance elsewhere.</li>"
    "<li><b>The honorarium is the floor.</b> The publication's reach is the rest of the payment.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/the-ex-puritan/\">The Ex-Puritan</a>, <a href=\"/writers/writing/the-malahat-review/\">The Malahat Review</a> and <a href=\"/writers/writing/prism-international/\">PRISM international</a>.</p>",

"tech/wifi-channel-congestion-fix":
    "<h2>The 8pm choke</h2>"
    "<p>When everyone's router shares three channels, the evening bandwidth is a traffic jam with a schedule. Channel congestion is why the line that flies at noon chokes at 8pm — and why the 'Auto' setting that stopped working years ago keeps picking the same crowded lane. The <a href=\"" + _w("Wi-Fi") + "\" rel=\"noopener\">Wi-Fi standard</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The fix order</h2>"
    "<ul>"
    "<li><b>Pick the channel yourself.</b> 2.4 GHz: 1, 6 or 11; everything else overlaps.</li>"
    "<li><b>Move what matters to 5 GHz.</b> Shorter range, empty lanes.</li>"
    "<li><b>Place the router like furniture.</b> Centrality beats antennae every time.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/router-placement-nigerian-flat/\">router placement in a Nigerian flat</a>, <a href=\"/tech/phone-wont-connect-to-wifi/\">phone won't connect to Wi-Fi</a> and <a href=\"/tech/new-router-for-slow-internet/\">a new router for slow internet</a>.</p>",

"writers/writing/business-insider":
    "<h2>What the strategy sections pay for</h2>"
    "<p>Business Insider's strategy-style sections pay professional rates for career and money essays — the pitch that lands names a concrete argument with the writer's own evidence inside it. The bar is usefulness: readers act on these pieces. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press coverage</a> this desk follows tracks where such essays live. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching the desk</h2>"
    "<ul>"
    "<li><b>Lead with the lesson, not the story.</b> The essay is the vehicle.</li>"
    "<li><b>Numbers from your own practice.</b> First-hand specifics are the currency.</li>"
    "<li><b>Read the section before pitching.</b> Career and money want different arguments.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/slate/\">Slate</a>, <a href=\"/writers/writing/wired/\">Wired</a> and <a href=\"/writers/writing/the-tyee/\">The Tyee</a>.</p>",

"writers/writing/the-forge-literary-magazine":
    "<h2>A small magazine with clear terms</h2>"
    "<p>The Forge Literary Magazine pays a flat rate for accepted prose, prefers stories under a stated length with room above it, and keeps its submission window free — terms that small magazines rarely state this clearly. It rewards precision over performance. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Before you submit</h2>"
    "<ul>"
    "<li><b>Respect the length preference.</b> Longer work is considered, not preferred.</li>"
    "<li><b>The free window is the policy.</b> Paid submissions elsewhere are a different market choice.</li>"
    "<li><b>Polish the first page.</b> Small magazines read slush honestly and fast.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/the-stinging-fly/\">The Stinging Fly</a>, <a href=\"/writers/writing/split-lip-magazine/\">Split Lip Magazine</a> and <a href=\"/writers/writing/torch-literary-arts/\">Torch Literary Arts</a>.</p>",

}

TOPUP_SECTIONS12 = {

"tech/tool/upload-time-calculator":
    "<h2>What the estimate assumes</h2>"
    "<p>Upload time is file size divided by the speed your connection actually sustains — which is usually lower than the speed on the box. The calculator's value is honesty about overhead: protocol costs, contention and the difference between megabits and megabytes turn a marketing number into a real one. Reference material sits under <a href=\"" + _w("data+transfer+rate") + "\" rel=\"noopener\">data transfer rates</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the result</h2>"
    "<ul>"
    "<li><b>Megabits, not megabytes.</b> The eight-times confusion is the classic wrong answer.</li>"
    "<li><b>Measure at the upload moment.</b> Evening speeds are not morning speeds.</li>"
    "<li><b>Batch small files together.</b> Thousands of tiny files lose to one archive.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/internet-speed-calculator/\">the internet speed calculator</a>, <a href=\"/tech/how-the-internet-works/\">how the internet works</a> and <a href=\"/tech/new-router-for-slow-internet/\">a new router for slow internet</a>.</p>",

"tech/tool/data-usage-estimator":
    "<h2>Reading the estimate</h2>"
    "<p>The estimate is arithmetic, not magic: hours of video at a chosen quality dominate the month, music and social media add a background hum, and one large download can move the total by weeks. The value of the calculator is seeing the trade before the bill does. Reference material sits under <a href=\"" + _w("mobile+broadband") + "\" rel=\"noopener\">mobile broadband</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using the number well</h2>"
    "<ul>"
    "<li><b>Measure one real week.</b> Guesses about screen time are famously generous.</li>"
    "<li><b>Set video quality deliberately.</b> Auto quality spends data on your behalf.</li>"
    "<li><b>Leave headroom.</b> The plan that ends at 99% used is the plan that ends early.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/mobile-data-plan-math/\">mobile data plan maths</a>, <a href=\"/tech/download-vs-stream-when-each-wins/\">download versus stream</a> and <a href=\"/tech/hours-of-video-per-gigabyte/\">hours of video per gigabyte</a>.</p>",

"sports/premier-league-results":
    "<h2>Results as form evidence</h2>"
    "<p>A results run tells the story the table compresses: which streaks are real form, which are schedule effects, and which sides are converting narrow games. Reading results as sequences is the oldest analytic discipline in football and still one of the most reliable. The <a href=\"" + PL + "\" rel=\"noopener\">Premier League</a> competition structure is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the run</h2>"
    "<ul>"
    "<li><b>Sequence over totals.</b> Form is a direction, not an aggregate.</li>"
    "<li><b>Note who scored first.</b> Teams that lead early win differently from teams that chase.</li>"
    "<li><b>Weight the opposition.</b> Results are samples; the schedule decides what they measure.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/champions-league-results/\">the Champions League results</a>, <a href=\"/sports/bundesliga-results/\">the Bundesliga results</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",

"tech/github-token-hygiene":
    "<h2>The rotation habit</h2>"
    "<p>Token hygiene is a rotation habit: least scope for the job, never in a repository, and replaced on a calendar rather than after an incident. The token is the password that machines use — and it leaks through logs, screenshots and CI output the way passwords never did. Reference material sits under <a href=\"" + _w("access+token") + "\" rel=\"noopener\">access tokens</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The habit, in full</h2>"
    "<ul>"
    "<li><b>Scope down before you copy.</b> Read-only until the job proves it needs more.</li>"
    "<li><b>Environment variables, always.</b> The repository is the one place tokens are public.</li>"
    "<li><b>Rotate on a schedule.</b> Expiry dates beat leak detection.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/github-beginner-mistakes/\">GitHub beginner mistakes</a>, <a href=\"/tech/git-errors-fixed/\">Git errors, fixed</a> and <a href=\"/tech/environment-variables-guide/\">the environment variables guide</a>.</p>",

}
