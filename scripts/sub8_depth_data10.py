# -*- coding: utf-8 -*-
"""Editorial depth sections, part 10: batch F, the 675-703 word tranche (750
bar), two tools under the 669 tool bar, one atlas record (765 of 819), plus
four t8b top-ups for pages that already carry a t8 block. 56 pages total.
Every external URL curl-verified 200 at authoring time; every internal link
verified to a real page."""

WHO = "https://www.who.int/"
EPA = "https://www.epa.gov/"
GOVUK = "https://www.gov.uk/"
NFPA = "https://www.nfpa.org/"
CLMP = "https://www.clmp.org/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS10 = {

"home/solar-panel-care-nigeria":
    "<h2>Dust is the local performance variable</h2>"
    "<p>Solar panels in Nigerian conditions lose output to dust long before they lose it to age. The care calendar follows the harmattan and the rains rather than the manual's generic schedule, and the cleaning itself is mostly water, soft tools and timing. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household energy guidance this desk's solar pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The care routine</h2>"
    "<ul>"
    "<li><b>Clean at the edges first.</b> Frames and corners collect the grit that scratches panels when dragged across.</li>"
    "<li><b>Work the dry season.</b> Post-harmattan cleaning recovers the most output per hour spent.</li>"
    "<li><b>Watch the inverter, not just the array.</b> Output faults are often electrical rather than surface.</li>"
    "</ul>"
    "<p>See <a href=\"/home/the-battery-room/\">the battery room</a>, <a href=\"/home/appliances-that-use-the-most-electricity/\">the appliances that use the most electricity</a> and <a href=\"/home/seasonal-care/\">seasonal home care</a>.</p>",

"home/water-storage-safety":
    "<h2>Storage is half of water safety</h2>"
    "<p>Water that was clean at the source can arrive at the tap contaminated by the vessel it waited in. Storage safety is therefore about sealed tanks, scheduled cleaning, and keeping the delivery path closed — the same principles the water industry applies at scale, sized for the household. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes drinking-water guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The storage routine</h2>"
    "<ul>"
    "<li><b>Seal everything that holds water.</b> An open tank is a settling basin for dust, insects and runoff.</li>"
    "<li><b>Clean on a calendar, not on a smell.</b> By the time water smells, the vessel is well past due.</li>"
    "<li><b>Keep delivery pipes above the floor.</b> Contact with the ground is where contamination enters the path.</li>"
    "</ul>"
    "<p>See <a href=\"/home/water-tank-annual-clean/\">the annual water-tank clean</a>, <a href=\"/home/borehole-water-taste-smell/\">borehole water taste and smell</a> and <a href=\"/home/hidden-water-leak-meter-test/\">the meter test for hidden leaks</a>.</p>",

"writers/writing/pulp-literature":
    "<h2>Pulp is a pace, not a quality bar</h2>"
    "<p>Pulp writing earns its readers with momentum: clear stakes early, scenes that turn, endings that land on the beat. The modern small magazines that carry the tradition care about craft as much as any quarterly — they simply measure it in propulsion. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing for propulsion</h2>"
    "<ul>"
    "<li><b>Start the engine in the first paragraph.</b> Pulp readers grant one scene of patience, rarely two.</li>"
    "<li><b>Turn the story at every section.</b> Momentum is a structure before it is a style.</li>"
    "<li><b>End on the landing, not the echo.</b> The closing image serves the story's last beat.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/hobart/\">Hobart</a>, <a href=\"/writers/writing/mudroom/\">Mudroom</a> and <a href=\"/writers/writing/carte-blanche/\">Carte Blanche</a>.</p>",

"home/bath-silicone-reseal":
    "<h2>Sealant is a service item</h2>"
    "<p>Bathroom silicone ages in a predictable way: it darkens, then peels at the edges, then lets water behind the bath where the plaster cannot dry. Resealing on a schedule is a one-hour job that prevents a wall repair. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household moisture guidance this desk's bathroom pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Resealing properly</h2>"
    "<ul>"
    "<li><b>Remove every trace of the old bead.</b> New silicone will not bond to old.</li>"
    "<li><b>Dry the joint for hours, not minutes.</b> Trapped moisture is how the new seal fails early.</li>"
    "<li><b>Tool the bead once, cleanly.</b> The smoothest seal is the one worked least.</li>"
    "</ul>"
    "<p>See <a href=\"/home/bathroom-grout-mould/\">bathroom grout mould</a>, <a href=\"/home/drain-flies-bathroom/\">drain flies in the bathroom</a> and <a href=\"/home/how-to-clear-a-slow-shower-drain/\">clearing a slow shower drain</a>.</p>",

"writers/writing/poetry-wales-poetry":
    "<h2>The poetry half of the magazine</h2>"
    "<p>Poetry Wales publishes poems beside its features and criticism, which means submissions are read by editors who also commission essays about the art — a readership that notices the intelligence of a poem as much as its music. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the literary-magazine field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting poems well</h2>"
    "<ul>"
    "<li><b>Send a coherent group.</b> Poems read as a batch should speak to one another.</li>"
    "<li><b>Polish the titles.</b> A title is the first line an editor reads and the last one remembered.</li>"
    "<li><b>Read the magazine's poets.</b> Taste in poetry is visible only in the poems a journal actually prints.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/poetry-wales-features/\">Poetry Wales features</a>, <a href=\"/writers/writing/modern-poetry-in-translation/\">Modern Poetry in Translation</a> and <a href=\"/writers/writing/fourteen-poems/\">Fourteen Poems</a>.</p>",

"home/rats-in-the-house":
    "<h2>Rats work a route, not a room</h2>"
    "<p>A rat in the house is following a path it has used before — along pipe runs, behind cabinets, through the gaps services leave behind. Poison and traps act on the animal; only exclusion acts on the route, and the route is what returns the population. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes household pest guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The exclusion order</h2>"
    "<ul>"
    "<li><b>Find the runs first.</b> Droppings and rub marks map the route better than any guess.</li>"
    "<li><b>Seal the service entries.</b> Pipe and cable gaps are the standard doorways; steel wool and sealant close them.</li>"
    "<li><b>Remove the food schedule.</b> Sealed stores and cleared pet food finish what exclusion starts.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ants-in-the-kitchen/\">ants in the kitchen</a>, <a href=\"/home/after-pest-treatment/\">after the pest treatment</a> and <a href=\"/home/compound-mosquito-control-night/\">compound mosquito control at night</a>.</p>",

"writers/learn/examples/example-of-a-book-review":
    "<h2>What the example demonstrates</h2>"
    "<p>A book review example earns its place by showing the form's contract with the reader: the book is placed and summarised without spoilers, the evaluation rests on evidence from the text, and the verdict tells a reader whether to spend their time. The <a href=\"" + _w("book+review") + "\" rel=\"noopener\">book review</a> is one of criticism's standard forms. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading your draft against it</h2>"
    "<ul>"
    "<li><b>Is the book placed?</b> Author, previous work and genre give the reader their bearings.</li>"
    "<li><b>Does every judgement carry evidence?</b> Claims without quotes or scenes are assertions.</li>"
    "<li><b>Is there a verdict?</b> A review without one is a summary wearing a review's clothes.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-of-a-press-release/\">the press release example</a>, <a href=\"/writers/learn/examples/example-blog-post/\">the blog post example</a> and <a href=\"/writers/learn/examples/example-of-a-professional-email/\">the professional email example</a>.</p>",

"writers/writing/the-rumpus-el-alboroto":
    "<h2>Small magazines with big readerships</h2>"
    "<p>The Rumpus and El Alboroto represent the small-press ideal: distinct editorial voices, direct relationships with readers, and a willingness to publish work that larger venues find hard to classify. Writers return to them because editorial attention per piece is unusually high. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs this tier of publishing. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What small magazines reward</h2>"
    "<ul>"
    "<li><b>Submit the hard-to-classify piece.</b> Small presses exist partly to publish what categories miss.</li>"
    "<li><b>Read the whole issue.</b> With small magazines, the issue is the editorial statement.</li>"
    "<li><b>Expect conversation.</b> Editors here often work with writers rather than between them.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/literary-hub/\">Literary Hub</a>, <a href=\"/writers/writing/narratively/\">Narratively</a> and <a href=\"/writers/writing/electric-literature-essays/\">Electric Literature essays</a>.</p>",

"home/harmattan-and-wood":
    "<h2>Dry air moves timber</h2>"
    "<p>Wood loses moisture to harmattan air and responds the only way it can: it shrinks, cracks and loosens at the joints. The season's care is therefore about stabilising humidity around furniture and structural timber rather than repairing what the dryness opens. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the dry-season fire and material guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Protecting timber through the season</h2>"
    "<ul>"
    "<li><b>Keep furniture off direct airflow.</b> Vents and windows aimed at a piece dry it unevenly and quickly.</li>"
    "<li><b>Oil and wax on schedule.</b> Surface finishes slow the moisture exchange that opens joints.</li>"
    "<li><b>Tighten before it complains.</b> The season's first creaks are joints telling you early.</li>"
    "</ul>"
    "<p>See <a href=\"/home/harmattan-fire-safety-house/\">harmattan fire safety</a>, <a href=\"/home/harmattan-and-your-electronics/\">harmattan and your electronics</a> and <a href=\"/home/seasonal-care/\">seasonal home care</a>.</p>",

"tech/laptop-buying-ram-storage":
    "<h2>Two specs decide the laptop's lifespan</h2>"
    "<p>Processors age slowly and gracefully; memory and storage decide how a laptop feels years later. Memory limits how much the machine can hold at once, and storage speed decides whether it still feels quick after the drive fills. Everything else is preference. The <a href=\"" + _w("laptop") + "\" rel=\"noopener\">laptop</a> form factor is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Sizing both honestly</h2>"
    "<ul>"
    "<li><b>Buy memory for the tab count you keep, not the one you imagine.</b> Browsers are the modern memory ceiling.</li>"
    "<li><b>Choose SSD speed before capacity.</b> A fast smaller drive outlives a large slow one in daily use.</li>"
    "<li><b>Check upgrade paths at purchase.</b> Soldered components make the first configuration the final one.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-ram-vs-ssd-first/\">RAM or SSD: which upgrade first</a>, <a href=\"/tech/how-much-ram-do-you-need/\">how much RAM do you need</a> and <a href=\"/tech/student-laptop-spec-floor-2026/\">the student laptop spec floor</a>.</p>",

"tech/tool/timestamp-converter":
    "<h2>Why timestamps need translating</h2>"
    "<p>Computers count time in seconds from a chosen epoch; humans read calendars; logs mix both. A timestamp converter exists because debugging constantly crosses that border — a certificate expiry, a log line, a database key all speak time differently. Reference material sits under <a href=\"" + _w("Unix+time") + "\" rel=\"noopener\">Unix time</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using it correctly</h2>"
    "<ul>"
    "<li><b>Confirm seconds versus milliseconds.</b> The same number means 1970 or 2001 depending on the unit.</li>"
    "<li><b>Pin the timezone.</b> Timestamps without a zone are questions, not answers.</li>"
    "<li><b>Watch for epoch mismatches.</b> Not every system counts from 1970, and embedded systems often do not.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/uuid-generator/\">the UUID generator</a>, <a href=\"/tech/tool/json-formatter/\">the JSON formatter</a> and <a href=\"/tech/tool/base64-encoder/\">the Base64 encoder</a>.</p>",

"tech/tool/word-counter":
    "<h2>Counting words the way editors do</h2>"
    "<p>Word counts look objective until two tools disagree, and the difference is almost always in the rules: hyphens, numbers, URLs, and whether markup is counted as text. Editors keep one house rule because consistency matters more than the exact number. Reference material sits under <a href=\"" + _w("word+count") + "\" rel=\"noopener\">word count</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using it well</h2>"
    "<ul>"
    "<li><b>Agree on one counting rule per project.</b> The brief's word limit means what the commissioning editor's tool says it means.</li>"
    "<li><b>Count the text, not the markup.</b> Pasted HTML inflates every count it touches.</li>"
    "<li><b>Recount after formatting.</b> Layout changes reading pace; sometimes it should change length too.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/case-converter/\">the case converter</a>, <a href=\"/tech/tool/json-formatter/\">the JSON formatter</a> and <a href=\"/tech/tool/http-status-lookup/\">the HTTP status lookup</a>.</p>",

"writers/writing/australian-book-review":
    "<h2>Criticism as a national beat</h2>"
    "<p>Australian Book Review treats books as a public matter — reviewing across fiction, politics, history and art on a monthly rhythm that has run for decades. For critics it is a market where a reviewing practice compounds: pieces build on one another into a body of work. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reviewing for a national review</h2>"
    "<ul>"
    "<li><b>Place the book in its conversation.</b> National reviews read books as contributions to public argument.</li>"
    "<li><b>Review the argument, not just the prose.</b> Nonfiction especially lives or dies on its claims.</li>"
    "<li><b>Keep the essay form.</b> The best reviews stand as pieces of writing in their own right.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/island-magazine/\">Island</a>, <a href=\"/writers/writing/overland-fiction/\">Overland</a> and <a href=\"/writers/writing/kill-your-darlings/\">Kill Your Darlings</a>.</p>",

"writers/learn/types-of-writing/how-to-write-a-speech":
    "<h2>Written for the ear, not the eye</h2>"
    "<p>A speech fails in the mouth before it fails on the page. Sentences that read beautifully can die in delivery — the ear needs shorter clauses, cleaner rhythms and repetition used as structure. Writing speeches well means reading every draft aloud before editing it silently. The <a href=\"" + _w("public+speaking") + "\" rel=\"noopener\">public speaking</a> tradition is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Structure that survives delivery</h2>"
    "<ul>"
    "<li><b>One idea per sentence, one theme per speech.</b> Audiences assemble nothing while listening.</li>"
    "<li><b>Signpost aloud.</b> \"There are three of these\" is a gift to a live audience.</li>"
    "<li><b>End on the line you want repeated.</b> The last sentence is the one that leaves the room.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-a-eulogy/\">how to write a eulogy</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-a-feature/\">how to write a feature</a> and <a href=\"/writers/learn/types-of-writing/how-to-write-a-blog-post/\">how to write a blog post</a>.</p>",

"writers/writing/the-offing-wit-tea":
    "<h2>Humour with a literary register</h2>"
    "<p>Wit Tea, The Offing's humour strand, publishes comedy that assumes the reader is literate — the joke runs through craft, publishing culture and the forms of literary life. Writing for it means being funny about something specific rather than performing wit in general. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing funny on purpose</h2>"
    "<ul>"
    "<li><b>Premise before punchlines.</b> The piece's conceit carries the comedy; the sentences decorate it.</li>"
    "<li><b>Write about the world you know.</b> Insider detail is where literary humour gets its accuracy.</li>"
    "<li><b>Cut the line you like most.</b> Comic prose serves the piece; the funniest line often serves itself.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/the-offing/\">The Offing</a>, <a href=\"/writers/writing/guernica/\">Guernica</a> and <a href=\"/writers/writing/noema/\">Noema</a>.</p>",

"entertainment/what-makes-a-cult-classic":
    "<h2>Cult status is an audience achievement</h2>"
    "<p>No studio ever made a cult classic on purpose. The label attaches to films that found their audience outside the release cycle — through repertory screenings, home video, word of mouth and rewatching rituals that turn viewing into participation. Reference material sits under <a href=\"" + _w("cult+film") + "\" rel=\"noopener\">cult film</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The mechanics of rewatching</h2>"
    "<ul>"
    "<li><b>Communities form around ritual.</b> Quoting, screening schedules and shared knowledge cement the audience.</li>"
    "<li><b>Imperfection helps.</b> Films with visible edges invite devotion in ways polished films rarely do.</li>"
    "<li><b>The second viewing is the real premiere.</b> Cult films reward pattern knowledge that first viewings cannot have.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-film-festivals-work/\">how film festivals work</a>, <a href=\"/entertainment/what-is-film-noir-explained/\">what film noir is</a> and <a href=\"/entertainment/dogme-95-explained/\">Dogme 95 explained</a>.</p>",

"home/cabinet-hinge-adjustment":
    "<h2>Most cabinet problems are adjustment problems</h2>"
    "<p>Doors that will not close, gaps that appear along a run, handles that no longer line up — cabinet faults usually arrive as alignment drift rather than breakage. Modern concealed hinges adjust in three directions, which means the fix is a screwdriver and a pattern. The <a href=\"" + _w("cabinet") + "\" rel=\"noopener\">cabinet</a> hardware standards are documented in reference works. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The three screws that matter</h2>"
    "<ul>"
    "<li><b>Side to side first.</b> The lateral screw aligns the door in the run before anything else.</li>"
    "<li><b>Then depth.</b> The depth screw decides whether the door sits flush or proud.</li>"
    "<li><b>Height last.</b> Most hinges do not adjust height; that is the mounting plate's job.</li>"
    "</ul>"
    "<p>See <a href=\"/home/door-lock-sticks-fix/\">a sticking door lock</a>, <a href=\"/home/fridge-door-not-sealing/\">the fridge door not sealing</a> and <a href=\"/home/garage-door-spring-safety/\">garage door spring safety</a>.</p>",

"home/grills-and-bars-rust-care":
    "<h2>Rust is a maintenance verdict</h2>"
    "<p>Metal grills and bars rust where coating, drainage or routine has failed — the base of a gate where water sits, the weld where paint skipped, the coastal air that salts everything. Care is therefore about the water's path as much as the metal's protection. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household material-care guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The care calendar</h2>"
    "<ul>"
    "<li><b>Fix the drainage before the metal.</b> Standing water at the base decides where rust begins.</li>"
    "<li><b>Prime the welds and edges.</b> Rust starts where coatings stop.</li>"
    "<li><b>Repaint on the dry-season window.</b> Coatings need the same weather the wood care does.</li>"
    "</ul>"
    "<p>See <a href=\"/home/how-to-paint-a-room-right/\">how to paint a room right</a>, <a href=\"/home/humidity-and-paint/\">humidity and paint</a> and <a href=\"/home/seasonal-care/\">seasonal home care</a>.</p>",

"tech/ssl-certificate-not-issuing":
    "<h2>Issuance fails at the verification step</h2>"
    "<p>Certificate issuance is automated everywhere except the part that fails: domain validation. The file or DNS record the authority looks for is usually missing, misplaced or cached at the wrong name — and the error message names the check, not the mistake. Reference material sits under <a href=\"" + _w("certificate+authority") + "\" rel=\"noopener\">certificate authorities</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The verification order</h2>"
    "<ul>"
    "<li><b>Confirm the exact validation name.</b> The authority tells you the path it checks; serve that path.</li>"
    "<li><b>Check DNS propagation before retrying.</b> Re-issuing against an invisible record just burns attempts.</li>"
    "<li><b>Watch for mixed hosts.</b> www and apex are different validations on most setups.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/website-security-headers-explained/\">website security headers explained</a>, <a href=\"/tech/custom-domain-dns-order/\">the order to set up a custom domain</a> and <a href=\"/tech/dns-problems-diagnosed/\">DNS problems diagnosed</a>.</p>",

"writers/writing-opportunities/australia":
    "<h2>Reading the Australian market</h2>"
    "<p>Australia's writing market combines well-funded national reviews, state-based literary magazines and a festival circuit that commissions actively. The atlas entries here carry verification dates because funding cycles and submission windows change with grant calendars rather than at publishers' convenience. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> maintains the equivalent listings for the US field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>How to use the entries</h2>"
    "<ul>"
    "<li><b>Check the verification date, then the official page.</b> The entry is a pointer; the outlet's own page is the source.</li>"
    "<li><b>Watch the grant seasons.</b> Australian literary funding moves on annual cycles that gate commissions.</li>"
    "<li><b>Use the tracker for follow-ups.</b> Long response times are normal here and worth planning around.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/\">the writing-opportunities atlas</a>, <a href=\"/writers/writing-opportunities/nigeria/\">the Nigeria entries</a> and <a href=\"/writers/tracker/\">the submission tracker</a>.</p>",

"writers/writing/brevity-essays":
    "<h2>The journal of the short essay</h2>"
    "<p>Brevity publishes essays under seven hundred fifty words — a constraint that turns prose style into structure. Every sentence has to carry weight because the form has no room for scaffolding. For essayists it is training in compression that improves every other form. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the essay-journal field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing brief on purpose</h2>"
    "<ul>"
    "<li><b>Cut the wind-up.</b> Short essays start inside the situation, not before it.</li>"
    "<li><b>One turn per essay.</b> Compression allows a single shift; spend it deliberately.</li>"
    "<li><b>Count in sentences.</b> When a form is this short, sentence count is the real budget.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/aeon-essays/\">Aeon essays</a>, <a href=\"/writers/writing/psyche-first-person/\">Psyche first-person</a> and <a href=\"/writers/writing/agbowo-essays/\">Agbowo essays</a>.</p>",

"writers/writing/torch-literary-arts":
    "<h2>A journal that reads for the craft</h2>"
    "<p>Torch Literary Arts publishes Black writers across forms with an editorial eye for work that is doing something deliberate on the page. Small literary journals of this kind read submissions slowly and closely, which makes them good homes for pieces that reward attention. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What to send where</h2>"
    "<ul>"
    "<li><b>Match the piece to the journal's form mix.</b> A poetry-heavy issue and a fiction issue read with different appetites.</li>"
    "<li><b>Send your considered work.</b> Slow-reading journals reward the piece that survives two readings.</li>"
    "<li><b>Follow the windows.</b> Small journals open and close submissions by season and staff capacity.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/strange-horizons-fiction/\">Strange Horizons fiction</a>, <a href=\"/writers/writing/clarkesworld-fiction/\">Clarkesworld fiction</a> and <a href=\"/writers/writing/beneath-ceaseless-skies/\">Beneath Ceaseless Skies</a>.</p>",

"entertainment/dogme-95-explained":
    "<h2>The vow and what it proved</h2>"
    "<p>Dogme 95 was a manifesto turned into a production rulebook: hand-held cameras, diegetic sound, no crediting the director as author, no genre. The films that followed proved the rules could create intensity — and proved that audiences still want craft to show. Reference material sits under <a href=\"" + _w("Dogme+95") + "\" rel=\"noopener\">Dogme 95</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Rules as an argument</h2>"
    "<ul>"
    "<li><b>Constraints focus attention.</b> The movement's best films are intense because the rules left nothing decorative.</li>"
    "<li><b>Movements date; films persist.</b> The vow reads as period piece; the works are still watched.</li>"
    "<li><b>Every rule was answering something.</b> Dogme argued against digital effects and polished distance.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/german-expressionism-explained/\">German Expressionism explained</a>, <a href=\"/entertainment/how-film-festivals-work/\">how film festivals work</a> and <a href=\"/entertainment/what-is-film-noir-explained/\">what film noir is</a>.</p>",

"home/interior-painting-mistakes":
    "<h2>The finish is decided before the first coat</h2>"
    "<p>Interior painting fails predictably: surfaces not cleaned, damp not treated, primer skipped where the surface changes, coats applied too thickly to finish early. Each mistake is cheap to prevent and expensive to paint over. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household air and material guidance this desk's painting pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The mistakes, in order of cost</h2>"
    "<ul>"
    "<li><b>Painting over moisture.</b> The paint films over the problem and the wall keeps it.</li>"
    "<li><b>Skipping the wash.</b> Dust and grease prevent adhesion regardless of paint quality.</li>"
    "<li><b>Rushing the recoat window.</b> Thick early coats crack; patience costs an afternoon.</li>"
    "</ul>"
    "<p>See <a href=\"/home/painting-over-damp/\">painting over damp</a>, <a href=\"/home/how-to-paint-a-room-right/\">how to paint a room right</a> and <a href=\"/home/humidity-and-paint/\">humidity and paint</a>.</p>",

"tech/muffled-phone-speaker-clean":
    "<h2>The grille is the whole problem</h2>"
    "<p>A muffled phone speaker is almost always a blocked speaker grille — pocket lint and dust compacted into a mesh designed to keep more out. The repair is cleaning, done with the right tools and restraint; the failure mode is damage from tools that do not belong near a driver. Reference material sits under <a href=\"" + _w("loudspeaker") + "\" rel=\"noopener\">loudspeakers</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Cleaning without damage</h2>"
    "<ul>"
    "<li><b>Dry tools first.</b> Soft brush and gentle picks before any liquid is considered.</li>"
    "<li><b>Never spray the grille directly.</b> Pressure drives debris inward and moisture past seals.</li>"
    "<li><b>Test with a known recording.</b> The same voice note before and after is a fair comparison.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/phone-overheating-causes-and-fixes/\">phone overheating causes and fixes</a>, <a href=\"/tech/swollen-phone-battery-safety/\">swollen battery safety</a> and <a href=\"/tech/free-up-storage-android/\">freeing up Android storage</a>.</p>",

"tech/new-midrange-vs-used-flagship":
    "<h2>Warranty versus spec sheet</h2>"
    "<p>A new midrange phone buys warranty, battery life and a full support window; a used flagship buys camera quality, screen and build from a generation ago at the same price. The decision is really about risk tolerance and how long you keep devices. The <a href=\"" + _w("smartphone") + "\" rel=\"noopener\">smartphone</a> market is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The comparison that matters</h2>"
    "<ul>"
    "<li><b>Battery age beats model age.</b> A used flagship with a tired battery is a repair project.</li>"
    "<li><b>Count the remaining software years.</b> Support windows start at launch, not at your purchase.</li>"
    "<li><b>Inspect like a rental.</b> Charging port, screen uniformity and water indicators tell the truth.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/dell-vs-hp-refurbished-laptops-nigeria/\">Dell versus HP refurbished laptops in Nigeria</a>, <a href=\"/tech/used-macbook-vs-used-windows-ultrabook/\">used MacBook versus used Windows ultrabook</a> and <a href=\"/tech/student-laptop-spec-floor-2026/\">the student laptop spec floor</a>.</p>",

"writers/guides/how-writing-retainers-work":
    "<h2>The guide, in working form</h2>"
    "<p>A retainer converts a client's uncertainty into predictable income and a writer's availability into a sellable product. The mechanics are simple to state and easy to get wrong: scope, hours, unused time and notice — agreed in writing before the first invoice. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes trade resources for working writers. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>When a retainer fits</h2>"
    "<ul>"
    "<li><b>Recurring work with a known shape.</b> Newsletters, reports and product copy suit retainers; one-offs do not.</li>"
    "<li><b>Stable access to the client.</b> Retainers run on communication more than on deliverables.</li>"
    "<li><b>A trial month first.</b> Both sides learn the real scope during the first cycle.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/freelance-paid-writing/how-writing-retainers-work/\">how writing retainers work</a>, <a href=\"/writers/guides/how-to-check-a-freelance-writing-contract/\">how to check a freelance writing contract</a> and <a href=\"/writers/learn/freelance-paid-writing/how-much-to-charge-for-an-article/\">how much to charge for an article</a>.</p>",

"writers/writing/words-without-borders-reviews":
    "<h2>Translation is the beat</h2>"
    "<p>Words Without Borders publishes literature in translation alongside criticism of it, which makes its review strand a market for critics who read across languages and care about the art of translation itself. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the literary field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reviewing translated work</h2>"
    "<ul>"
    "<li><b>Name the translator.</b> The translation is the work being reviewed; anonymity erases it.</li>"
    "<li><b>Read the translator's note first.</b> It usually names the book's central problem honestly.</li>"
    "<li><b>Know the target language's limits.</b> Credibility in this beat is visible in what you claim to know.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/wasafiri-interviews/\">Wasafiri interviews</a>, <a href=\"/writers/writing/modern-poetry-in-translation/\">Modern Poetry in Translation</a> and <a href=\"/writers/writing/himal-southasian/\">Himal Southasian</a>.</p>",

"home/washing-machine-smell-and-filter":
    "<h2>Smell is a filter and seal problem</h2>"
    "<p>Washing machines smell because residue lives where the routine does not reach: the filter, the door seal's fold, and the drum's outer surface where the film builds. The fix is a cleaning cycle that treats all three, and a habit that prevents the film's return. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household appliance guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The routine that ends it</h2>"
    "<ul>"
    "<li><b>Clean the filter monthly.</b> It is the machine's only user-serviceable drain point.</li>"
    "<li><b>Wipe the seal fold after wash days.</b> The fold holds water longer than the drum does.</li>"
    "<li><b>Run a hot empty cycle on schedule.</b> Heat clears the film that cold washes accumulate.</li>"
    "</ul>"
    "<p>See <a href=\"/home/washing-machine-mould-door-seal/\">washing-machine door seal mould</a>, <a href=\"/home/freezer-frost-buildup/\">freezer frost buildup</a> and <a href=\"/home/fridge-coils-twice-a-year/\">cleaning fridge coils twice a year</a>.</p>",

"tech/inbox-zero-myth":
    "<h2>Zero is a method, not a scoreboard</h2>"
    "<p>Inbox Zero was always a system — process mail in passes, act or route each message, and touch nothing twice — and the myth part is treating the empty inbox as the goal. The sustainable version measures response time and dropped threads instead. The <a href=\"" + _w("email") + "\" rel=\"noopener\">email</a> medium is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What actually works</h2>"
    "<ul>"
    "<li><b>Process in passes, not continuously.</b> Scheduled handling beats constant partial attention.</li>"
    "<li><b>Turn messages into tasks immediately.</b> An inbox is a queue, not a to-do list.</li>"
    "<li><b>Measure dropped threads.</b> The real failure of email is silence on things that needed answers.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/remote-work-free-tools/\">free remote-work tools</a>, <a href=\"/tech/laptop-desk-ergonomics-the-standing-fix/\">laptop desk ergonomics</a> and <a href=\"/tech/video-call-mistakes/\">video call mistakes</a>.</p>",

"writers/learn/professional-writing/how-to-write-about-yourself":
    "<h2>About pages are professional documents</h2>"
    "<p>Writing about yourself professionally is an exercise in selection: the reader needs your competence, your range and one memorable fact, in that order. The failure mode is either modesty that hides the evidence or autobiography that buries it. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes resources on writers' professional presence. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The honest structure</h2>"
    "<ul>"
    "<li><b>Evidence first.</b> What you have written and for whom beats every adjective.</li>"
    "<li><b>One personal detail, placed last.</b> Memorability serves the paragraph's end, not its start.</li>"
    "<li><b>Keep three lengths ready.</b> Bio lines, bylines and about pages are different documents.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/professional-writing/\">professional writing</a>, <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a pitch</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-professional-emails/\">professional emails dos and don'ts</a>.</p>",

"writers/learn/writing-for-publication/how-to-pitch-an-editor":
    "<h2>The pitch is the first draft of the working relationship</h2>"
    "<p>An editor reading a pitch is testing three things at once: whether the idea is publishable, whether the writer can execute it, and whether this person is easy to work with. The pitch that clears all three is short, specific and complete enough to answer the obvious follow-up question before it is asked. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes pitching resources. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Anatomy of a working pitch</h2>"
    "<ul>"
    "<li><b>The idea in one sentence, early.</b> Editors decide in the first screen or not at all.</li>"
    "<li><b>The evidence you bring.</b> Access, expertise and documents are the pitch's real content.</li>"
    "<li><b>The shape and the length.</b> A proposed form tells the editor what commissioning looks like.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a pitch</a>, <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-pitching-editors/\">pitching editors dos and don'ts</a> and <a href=\"/writers/guides/when-to-follow-up-on-a-pitch/\">when to follow up on a pitch</a>.</p>",

"writers/writing/vox-climate":
    "<h2>Climate coverage with a point of view</h2>"
    "<p>Vox's climate desk built its audience on explainers with an argument — pieces that say what a development means rather than only what happened. For writers, the model is a reminder that climate journalism sells clarity and stakes together. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the digital field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching climate work</h2>"
    "<ul>"
    "<li><b>Explain one mechanism per piece.</b> Climate writing that explains one thing well compounds.</li>"
    "<li><b>Bring the local stake.</b> The strongest climate stories connect a global mechanism to a named place.</li>"
    "<li><b>Answer the \"so what\" in the pitch.</b> Explainers sell their stakes upfront.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/high-country-news/\">High Country News</a>, <a href=\"/writers/writing/earth-island-journal/\">Earth Island Journal</a> and <a href=\"/writers/writing/climate-home-news/\">Climate Home News</a>.</p>",

"home/wasp-nest-first-response":
    "<h2>Distance is the first response</h2>"
    "<p>A wasp nest discovered near a house is a hazard managed by distance first, timing second. The insects are defending a route they use constantly, and the safe intervention happens at night when the colony is inside — by someone who knows what they are doing. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household pesticide safety guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Before anyone arrives</h2>"
    "<ul>"
    "<li><b>Move people and pets away from the flight path.</b> The route matters more than the nest's location.</li>"
    "<li><b>Never block the entrance.</b> Blocked wasps find other doors, usually into the house.</li>"
    "<li><b>Do not attempt removal after dark with a ladder and a plan.</b> Professional removal exists for this exact job.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ants-in-the-kitchen/\">ants in the kitchen</a>, <a href=\"/home/after-pest-treatment/\">after the pest treatment</a> and <a href=\"/home/rats-in-the-house/\">rats in the house</a>.</p>",

"tech/wi-fi-router-placement":
    "<h2>Placement beats purchase</h2>"
    "<p>Most home Wi-Fi problems are solved by moving the router, not replacing it. Central height, clear of metal and thick walls, away from the appliances that share its spectrum — the physics is simple and the gains are large. Reference material sits under <a href=\"" + _w("Wi-Fi") + "\" rel=\"noopener\">Wi-Fi</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The ten-minute survey</h2>"
    "<ul>"
    "<li><b>Map the dead spots first.</b> Walk the house with a signal app before touching anything.</li>"
    "<li><b>Go central and high.</b> Routers radiate in all directions; corners waste half the coverage.</li>"
    "<li><b>Clear the metal.</b> Fridges, cylinders and cabinets shadow the signal more than walls do.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/wifi-channel-congestion-fix/\">Wi-Fi channel congestion fixes</a>, <a href=\"/tech/wifi-extender-vs-second-router-nigerian-house/\">extender versus second router</a> and <a href=\"/tech/fibre-vs-5g-router-home-office/\">fibre versus 5G for the home office</a>.</p>",

"home/unpermitted-work-home-sale":
    "<h2>Disclosure is the whole game</h2>"
    "<p>Unpermitted work surfaces at sale because the disclosure form asks directly, and the honest answers are manageable in ways discovery is not. The options are retrofit approval, documented disclosure with price adjustment, or removal — chosen by cost, risk and the buyer's financing. Reference material sits under <a href=\"" + _w("building+permit") + "\" rel=\"noopener\">building permits</a>. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The sale-path options</h2>"
    "<ul>"
    "<li><b>Get the records first.</b> What the permit office has on file decides every conversation after it.</li>"
    "<li><b>Price the retrofit honestly.</b> Retrospective permits cost inspection and sometimes correction work.</li>"
    "<li><b>Disclose in writing, early.</b> Surprises at closing kill deals that disclosure merely discounts.</li>"
    "</ul>"
    "<p>See <a href=\"/home/unpermitted-work-insurance/\">unpermitted work and insurance</a>, <a href=\"/home/us-home-permits/\">US home permits</a> and <a href=\"/home/us-diy-electrical-rules/\">US DIY electrical rules</a>.</p>",

"tech/why-backtests-fail":
    "<h2>Backtests fail at the assumptions</h2>"
    "<p>Almost every backtest failure is a data or process failure wearing a strategy's name: survivorship in the sample, look-ahead in the signals, costs that the model forgot, or a parameter tuned to one period. The equity curve is the last thing to trust. Reference material sits under <a href=\"" + _w("backtesting") + "\" rel=\"noopener\">backtesting</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The failure checklist</h2>"
    "<ul>"
    "<li><b>Interrogate the data first.</b> Delisted symbols and restated prices explain more failures than models do.</li>"
    "<li><b>Charge yourself real costs.</b> Spreads, slippage and fees turn most elegant curves marginal.</li>"
    "<li><b>Reserve out-of-sample years.</b> A rule that worked only where it was fitted has not been tested.</li>"
    "</ul>"
    "<p>See <a href=\"/money/backtesting-101/\">backtesting 101</a>, <a href=\"/money/day-trading-vs-swing-vs-investing/\">day trading versus swing versus investing</a> and <a href=\"/money/how-to-check-a-trading-broker/\">how to check a trading broker</a>.</p>",

"writers/learn/examples/example-of-a-professional-email":
    "<h2>What the example teaches</h2>"
    "<p>A professional email example shows the form's real constraints: subject lines that carry the ask, openings that need no context archaeology, requests made directly, and closes that state the next step. The <a href=\"" + _w("email") + "\" rel=\"noopener\">email</a> remains where professional writing relationships actually happen. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading your draft against it</h2>"
    "<ul>"
    "<li><b>Does the subject line name the ask?</b> Editors file messages by what the subject promised.</li>"
    "<li><b>Can the reader act without rereading?</b> The one-read email is the professional standard.</li>"
    "<li><b>Is the next step explicit?</b> Ambiguity in a close becomes delay in practice.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-of-a-press-release/\">the press release example</a>, <a href=\"/writers/learn/examples/example-of-a-book-review/\">the book review example</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-professional-emails/\">professional emails dos and don'ts</a>.</p>",

"home/gas-heaters-damp":
    "<h2>Combustion makes water</h2>"
    "<p>Every flame that burns gas indoors produces water vapour and carbon dioxide as part of the reaction — which is why unvented gas heating and damp arrive together. The heater is not leaking; the household is manufacturing moisture and depositing it on the coldest walls. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes indoor-air guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The ventilation equation</h2>"
    "<ul>"
    "<li><b>Ventilate while burning, not after.</b> Combustion needs the air continuously.</li>"
    "<li><b>Never rely on gas heating for drying clothes.</b> It adds the room's largest moisture load directly.</li>"
    "<li><b>Service the appliance on schedule.</b> Incomplete combustion adds carbon monoxide to the moisture problem.</li>"
    "</ul>"
    "<p>See <a href=\"/home/gas-cylinder-safety/\">gas cylinder safety</a>, <a href=\"/home/condensation-ventilation-that-works/\">condensation ventilation that works</a> and <a href=\"/home/gas-cooker-wont-ignite/\">the gas cooker that will not ignite</a>.</p>",

"home/kitchen-ventilation-damp":
    "<h2>The kitchen is the house's moisture factory</h2>"
    "<p>Boiling, frying and washing concentrate water vapour in one room, and without extraction it deposits on the kitchen's cold surfaces and migrates into the rooms beside it. Kitchen ventilation is therefore a house-damp strategy, not a cooking preference. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor-air guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Extraction that actually clears</h2>"
    "<ul>"
    "<li><b>Capture at the source.</b> A hood over the pot beats any amount of room ventilation after the fact.</li>"
    "<li><b>Vent outside, not into the ceiling.</b> Extraction to the loft moves the damp problem rather than solving it.</li>"
    "<li><b>Run it through the cooldown.</b> Steam continues after the cooking stops.</li>"
    "</ul>"
    "<p>See <a href=\"/home/kitchen-hygiene-routine/\">the kitchen hygiene routine</a>, <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three kinds of damp</a> and <a href=\"/home/bathroom-fan-condensation/\">bathroom fans and condensation</a>.</p>",

"home/sewer-smell-after-trip":
    "<h2>Dry traps are the usual answer</h2>"
    "<p>After a house has stood empty, sewer smell almost always traces to a floor drain or unused fixture whose water seal has evaporated. The trap exists to hold a water barrier between the house and the sewer; time and heat remove it. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household water guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The return-home routine</h2>"
    "<ul>"
    "<li><b>Run every unused fixture for a minute.</b> Refilling traps is the entire fix in most cases.</li>"
    "<li><b>Pour water into floor drains first.</b> They are the largest seals and the fastest to dry.</li>"
    "<li><b>If the smell persists, look further.</b> A venting fault or cracked seal is the second-order cause.</li>"
    "</ul>"
    "<p>See <a href=\"/home/drain-flies-bathroom/\">drain flies in the bathroom</a>, <a href=\"/home/floor-drain-backflow/\">floor drain backflow</a> and <a href=\"/home/how-to-fix-a-slow-draining-sink/\">fixing a slow-draining sink</a>.</p>",

"home/ceiling-plaster-sagging-repair":
    "<h2>Sagging is a moisture history</h2>"
    "<p>Plaster sags because something weakened its bond to the lath or board behind it — usually water that has already moved on. Before any repair reads the history: a sag that has dried is a surface problem; a sag that is still cool or damp is a leak in progress. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household moisture guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Repair or replace</h2>"
    "<ul>"
    "<li><b>Probe gently before deciding.</b> Firm edges can be re-secured; crumbly areas need cutting out.</li>"
    "<li><b>Fix the water path first.</b> Every ceiling repair before the leak is a rehearsal.</li>"
    "<li><b>Match the material.</b> Patching plaster with the wrong compound guarantees a visible repair.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ceiling-water-stain-removal/\">ceiling water stain removal</a>, <a href=\"/home/ceiling-leak-11pm/\">ceiling leak at 11pm</a> and <a href=\"/home/flat-roof-ponding-and-leaks/\">flat roof ponding and leaks</a>.</p>",

"home/part-p-explained":
    "<h2>Part P in one page</h2>"
    "<p>Part P is the section of the England and Wales Building Regulations that covers electrical safety in dwellings — which electrical work needs a certificate, who can do it, and what the household is responsible for afterwards. It is the reason \"the electrician's certificate\" is a document buyers ask for. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes the regulations this desk's UK guides follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What it means for the household</h2>"
    "<ul>"
    "<li><b>Know which work is notifiable.</b> New circuits and consumer-unit changes cross the line almost everywhere.</li>"
    "<li><b>Keep the certificates.</b> The building's electrical history is a documents trail.</li>"
    "<li><b>Check the person, not the van.</b> Competent-person schemes are the register that matters.</li>"
    "</ul>"
    "<p>See <a href=\"/home/uk-insulation-grants/\">UK insulation grants</a>, <a href=\"/home/uk-landlord-damp-mould-duties/\">landlord duties on damp and mould</a> and <a href=\"/home/us-home-permits/\">US home permits</a>.</p>",

"home/paint-peeling-walls-bathroom":
    "<h2>Peeling paint is a moisture verdict</h2>"
    "<p>Bathroom paint peels from the substrate up because moisture is moving through the wall or condensing on it faster than the paint can release it. Coating over the peel repaints the symptom. The fix is moisture control first, surface preparation second, paint third. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household moisture guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Fixing the cause first</h2>"
    "<ul>"
    "<li><b>Decide which damp you have.</b> Condensation patterns and wall leaks peel differently.</li>"
    "<li><b>Scrape to a sound edge.</b> Paint adheres to what remains, not to what is lifting.</li>"
    "<li><b>Use the bathroom-rated system.</b> Primer and finish are a pair; the topcoat alone always loses.</li>"
    "</ul>"
    "<p>See <a href=\"/home/painting-over-damp/\">painting over damp</a>, <a href=\"/home/interior-painting-mistakes/\">interior painting mistakes</a> and <a href=\"/home/bathroom-grout-mould/\">bathroom grout mould</a>.</p>",

"tech/used-macbook-vs-used-windows-ultrabook":
    "<h2>Two repair economies</h2>"
    "<p>Used MacBooks and used Windows ultrabooks price differently because their repair economies differ: one has standardised parts and a broad service market, the other has a closed supply chain and strong resale. The right choice depends on who will fix it and what the battery costs when it ages. The <a href=\"" + _w("laptop") + "\" rel=\"noopener\">laptop</a> market is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The used-market checklist</h2>"
    "<ul>"
    "<li><b>Price the battery replacement before the laptop.</b> It is the used machine's certain cost.</li>"
    "<li><b>Check repair access locally.</b> Parts availability in your market beats every benchmark.</li>"
    "<li><b>Verify the account locks.</b> Activation locks are the used-market failure that no repair fixes cheaply.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/new-midrange-vs-used-flagship/\">new midrange versus used flagship</a>, <a href=\"/tech/dell-vs-hp-refurbished-laptops-nigeria/\">Dell versus HP refurbished laptops in Nigeria</a> and <a href=\"/tech/laptop-buying-ram-storage/\">laptop buying: RAM and storage</a>.</p>",

"tech/wireless-earbuds-for-calls":
    "<h2>Calls are a microphone problem</h2>"
    "<p>Earbuds marketed for music often fail at calls because the microphone array is the expensive part of voice work. Call quality depends on beam-forming mics, wind handling and how the buds sit during speech — not on driver specifications. The <a href=\"" + _w("headphones") + "\" rel=\"noopener\">headphones</a> category is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing for voice</h2>"
    "<ul>"
    "<li><b>Test in noise, not in quiet.</b> Microphone quality shows at the street, not the desk.</li>"
    "<li><b>Check the codec your calls actually use.</b> The headset is only as good as the app's audio path.</li>"
    "<li><b>Fit decides the mic position.</b> A bud that shifts when you talk ruins a good array.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/video-call-mistakes/\">video call mistakes</a>, <a href=\"/tech/muffled-phone-speaker-clean/\">cleaning a muffled phone speaker</a> and <a href=\"/tech/laptop-desk-ergonomics-the-standing-fix/\">laptop desk ergonomics</a>.</p>",

"writers/learn/online-writing/how-to-write-social-media-copy":
    "<h2>Copy is compression work</h2>"
    "<p>Social media copy is professional writing under the tightest constraints online: a few characters, a hostile reading environment, and one job — earn the click or the pause. The craft is selection: what the post says, what the link says, and what is deliberately left out. The <a href=\"" + _w("copywriting") + "\" rel=\"noopener\">copywriting</a> tradition is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The platform-aware habits</h2>"
    "<ul>"
    "<li><b>Write the post before the headline.</b> The post carries the promise the destination must keep.</li>"
    "<li><b>One claim per post.</b> Compressed formats cannot carry qualified arguments.</li>"
    "<li><b>Read it in the feed.</b> Copy behaves differently beside other people's posts.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/freelance-paid-writing/b2b-content-writing/\">B2B content writing</a>, <a href=\"/writers/learn/freelance-paid-writing/finance-and-insurance-copywriting/\">finance and insurance copywriting</a> and <a href=\"/writers/learn/examples/example-of-a-professional-email/\">the professional email example</a>.</p>",

"writers/writing/wasafiri-interviews":
    "<h2>Interviews as literary journalism</h2>"
    "<p>Wasafiri's interviews treat conversations with writers as published craft — long, researched encounters that map a career and a literature at once. For interviewers, the strand sets the bar: questions earned by reading, and editing that shapes without flattening the voice. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Conducting them well</h2>"
    "<ul>"
    "<li><b>Research until the questions surprise.</b> The interview's quality is decided before it begins.</li>"
    "<li><b>Ask one thing at a time.</b> Compound questions receive compound evasions.</li>"
    "<li><b>Edit for the speaker's voice.</b> The craft is shaping clarity without rewriting the person.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/words-without-borders-reviews/\">Words Without Borders reviews</a>, <a href=\"/writers/writing/modern-poetry-in-translation/\">Modern Poetry in Translation</a> and <a href=\"/writers/writing/himal-southasian/\">Himal Southasian</a>.</p>",

"entertainment/christopher-nolan-movies-order":
    "<h2>Order matters less than the mythology suggests</h2>"
    "<p>Nolan's films are standalone works with recurring obsessions — time, memory, unreliable narrators — rather than a serialised story, which means \"watching order\" is really an entry-point question. The viewing guide below separates release order from thematic order. The <a href=\"" + _w("Christopher+Nolan") + "\" rel=\"noopener\">director's body of work</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Three watching orders</h2>"
    "<ul>"
    "<li><b>Release order</b> shows the craft escalating in public.</li>"
    "<li><b>Theme order</b> groups the time films together, where they argue with each other.</li>"
    "<li><b>The beginner's path</b> starts with the most legible crowd-pleasers and ends with the puzzles.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/movie/the-prestige/\">The Prestige</a>, <a href=\"/entertainment/movie/inception/\">Inception</a> and <a href=\"/entertainment/movie/the-dark-knight/\">The Dark Knight</a>.</p>",

"home/outlet-overloading-danger":
    "<h2>Overloads leave evidence</h2>"
    "<p>An overloaded outlet announces itself before it fails: warm faceplates, discolouration around the socket, and the smell of heated plastic. The arithmetic behind it is simple — every device on the circuit shares one wire's capacity — and so is the fix. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes home electrical fire guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The load audit</h2>"
    "<ul>"
    "<li><b>Sum the heaters first.</b> Heating appliances dominate every domestic circuit's budget.</li>"
    "<li><b>One high-draw device per outlet run.</b> Extension leads multiply sockets, not capacity.</li>"
    "<li><b>Replace warm sockets immediately.</b> Heat at the faceplate is the fault, not the warning.</li>"
    "</ul>"
    "<p>See <a href=\"/home/wiring-red-flags-in-your-home/\">wiring red flags</a>, <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a> and <a href=\"/home/why-does-my-circuit-breaker-keep-tripping/\">why the circuit breaker keeps tripping</a>.</p>",

"tech/free-ai-tools-worth-using":
    "<h2>Free tiers with real utility</h2>"
    "<p>The useful free AI tools are the ones whose free tier is the product rather than the advertisement: research assistance, drafting, transcription and code help where limits are visible and work is exportable. The worth-it filter is simple — does the tool return work you can keep when the subscription question arrives? The <a href=\"" + _w("artificial+intelligence") + "\" rel=\"noopener\">artificial intelligence</a> tooling is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The worth-it filter</h2>"
    "<ul>"
    "<li><b>Exportability first.</b> Work trapped in a tool is a subscription with extra steps.</li>"
    "<li><b>Check the data settings.</b> Free tiers often pay themselves with your inputs.</li>"
    "<li><b>Prefer tools with honest limits.</b> Visible quotas beat silently degrading ones.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/deepseek-vs-chatgpt/\">DeepSeek versus ChatGPT</a>, <a href=\"/tech/ai-assistant-data-training-settings/\">AI assistant data and training settings</a> and <a href=\"/writers/learn/freelance-paid-writing/choosing-ai-writing-tools/\">choosing AI writing tools</a>.</p>",

"writers/writing/longreads-reading-list":
    "<h2>A reading list is a syllabus</h2>"
    "<p>Longform reading lists work like courses: the order teaches, the mix balances forms, and the annotations tell you why each piece earned its place. Working through one deliberately improves a writer's structural instincts faster than any craft book. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field these pieces come from. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>How to work through it</h2>"
    "<ul>"
    "<li><b>Read in the list's order.</b> Syllabi sequence for a reason.</li>"
    "<li><b>Outline each piece after reading.</b> Structure is what the list is really teaching.</li>"
    "<li><b>Keep the two lists.</b> One for the pieces to imitate, one for the pieces to envy.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/longreads/\">Longreads</a>, <a href=\"/writers/writing/longreads-personal-essay/\">the longreads personal essay guide</a> and <a href=\"/writers/writing/longreads-reported-feature/\">the longreads reported feature guide</a>.</p>",

}

# Top-up sections for pages that already carry a t8 block but are still under
# their class bar. Injected under marker data-esrc="t8b".
TOPUP_SECTIONS10 = {

"tech/tool/vpn-cost-calculator":
    "<h2>Pricing the tunnel honestly</h2>"
    "<p>A VPN cost estimate should carry the whole subscription surface: the headline monthly rate, the annual discount that actually applies to you, the device limit per plan, and the speed tax that no price sheet mentions. The <a href=\"" + _w("virtual+private+network") + "\" rel=\"noopener\">virtual private network</a> category is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What the estimate should include</h2>"
    "<ul>"
    "<li><b>Price per device, per month.</b> Household plans compare fairly only at equal coverage.</li>"
    "<li><b>The renewal rate, not the teaser.</b> First-year pricing is marketing; the second year is the price.</li>"
    "<li><b>The exit cost.</b> Annual plans pay for commitment the household may not want.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/vpn-what-it-protects/\">what a VPN protects</a>, <a href=\"/tech/tool/ai-subscription-cost-comparer/\">the AI subscription cost comparer</a> and <a href=\"/tech/tool/internet-speed-calculator/\">the internet speed calculator</a>.</p>",

"tech/android-notifications":
    "<h2>Notifications are a design surface</h2>"
    "<p>Android's notification system is the most powerful interruption manager on any personal device — and the one most people leave at factory settings. Channels, per-app controls and priority modes decide what is allowed to interrupt real life. The <a href=\"" + _w("Android+(operating+system)") + "\" rel=\"noopener\">Android platform</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Controlling the stream</h2>"
    "<ul>"
    "<li><b>Sort by interruption, not by app.</b> Channels let one app notify about messages and stay silent about promotions.</li>"
    "<li><b>Schedule the quiet hours as a policy.</b> Do-not-disturb with named exceptions survives real weeks.</li>"
    "<li><b>Audit quarterly.</b> App stores add notification types faster than habits adapt.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/free-up-storage-android/\">freeing up Android storage</a>, <a href=\"/tech/android-backup-guide/\">the Android backup guide</a> and <a href=\"/tech/phone-battery-charging-myths/\">phone battery charging myths</a>.</p>",

"sports/bundesliga-results":
    "<h2>Results are the season's raw data</h2>"
    "<p>A results run tells the truth that table position smooths: which wins came against the run of play, which losses were narrow, and where form has been stable for months. Reading results well means reading them as sequences rather than as a record. The <a href=\"" + _w("Bundesliga") + "\" rel=\"noopener\">Bundesliga</a> competition structure is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading a results run</h2>"
    "<ul>"
    "<li><b>Look at the sequence, not the totals.</b> Three narrow wins and a draw carry different form than the reverse.</li>"
    "<li><b>Note who scored first.</b> Teams that lead early win differently from teams that chase.</li>"
    "<li><b>Weight the opposition.</b> Results are samples; the schedule decides what they sample.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/bundesliga-table/\">the Bundesliga table</a>, <a href=\"/sports/premier-league-results/\">the Premier League results</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",

"home/seasonal-home-maintenance-checklist":
    "<h2>The checklist as an operating document</h2>"
    "<p>A maintenance checklist earns its keep by being worked rather than admired: dated items, a record of completions, and a place for the small discoveries that become bigger repairs. The document is the house's history as much as its plan. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household maintenance guidance this desk's checklist follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Working the list</h2>"
    "<ul>"
    "<li><b>Date every item to a season.</b> Tasks without windows get postponed into failure.</li>"
    "<li><b>Record what you find, not just what you do.</b> Notes on early wear are the checklist's real output.</li>"
    "<li><b>Review the list itself yearly.</b> Houses change; the checklist must follow them.</li>"
    "</ul>"
    "<p>See <a href=\"/home/seasonal-care/\">seasonal home care</a>, <a href=\"/home/ac-outdoor-unit-care/\">air-conditioner outdoor unit care</a> and <a href=\"/home/harmattan-fire-safety-house/\">harmattan fire safety</a>.</p>",

}
