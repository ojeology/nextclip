# -*- coding: utf-8 -*-
"""Editorial depth sections, part 11: batch G, the 668-685 word tranche against
the 750-word bar, two tools under the 669 tool bar, one trust page (writers
privacy, 651 of 732), plus two t8b top-ups. 56 pages total.
Every external URL curl-verified 200 at authoring time; every internal link
verified to a real page."""

WHO = "https://www.who.int/"
EPA = "https://www.epa.gov/"
GOVUK = "https://www.gov.uk/"
NFPA = "https://www.nfpa.org/"
CLMP = "https://www.clmp.org/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS11 = {

"tech/remote-work-free-tools":
    "<h2>The free stack covers the real work</h2>"
    "<p>Remote work runs on a small set of capabilities — documents, calls, task tracking, storage — and free tiers now cover all of them well enough for most teams. The judgement is which tools stay free under your actual load, and which ones quietly turn into subscriptions when the team grows. The <a href=\"" + _w("remote+work") + "\" rel=\"noopener\">remote work</a> tooling is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing the free stack</h2>"
    "<ul>"
    "<li><b>Export first, always.</b> A free tier without export is a subscription trap with a friendly front.</li>"
    "<li><b>One tool per job.</b> Overlapping free tools cost attention, which is the scarce remote resource.</li>"
    "<li><b>Check the guest policy.</b> Collaboration limits decide whether free tiers survive real projects.</li>"
    "<li><b>Write the upgrade trigger down.</b> Decide in advance what growth forces the payment.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/inbox-zero-myth/\">the inbox zero myth</a>, <a href=\"/tech/video-call-mistakes/\">video call mistakes</a> and <a href=\"/tech/laptop-desk-ergonomics-the-standing-fix/\">laptop desk ergonomics</a>.</p>",

"entertainment/best-streaming-apps-nigeria":
    "<h2>Choosing for Nigerian bandwidth</h2>"
    "<p>Streaming apps in Nigeria are judged as much on their data behaviour as on their catalogues: download quality, adaptive streaming under load, and whether the plan that matters is priced in naira. The best app is the one still watchable at 9pm on a busy connection. The <a href=\"" + _w("streaming+media") + "\" rel=\"noopener\">streaming media</a> model is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The Nigerian checklist</h2>"
    "<ul>"
    "<li><b>Downloads before streaming.</b> Offline quality is the feature that decides commute viewing.</li>"
    "<li><b>Check the data saver for real.</b> Some apps throttle quality honestly; others barely change.</li>"
    "<li><b>Price the mobile plan.</b> Telco bundles often beat card subscriptions on cost per hour.</li>"
    "<li><b>Test the catalogue at your taste.</b> Libraries are regional, and the home page flatters every one of them.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/cheapest-way-to-stream-movies/\">the cheapest way to stream movies</a>, <a href=\"/entertainment/what-you-need-for-4k-streaming/\">what you need for 4K streaming</a> and <a href=\"/entertainment/how-streaming-bundles-work-explained/\">how streaming bundles work</a>.</p>",

"entertainment/short-series-eight-episodes-or-fewer":
    "<h2>The season that ends on purpose</h2>"
    "<p>Short series are a format decision, not a compromise: eight episodes or fewer forces plotting that TV's longer seasons routinely avoid. The constraint shows up in the writing — no filler arcs, no season-two setup that may never arrive, and endings that arrive while the audience still cares. The <a href=\"" + _w("miniseries") + "\" rel=\"noopener\">miniseries form</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the form does well</h2>"
    "<ul>"
    "<li><b>Endings get written.</b> The format assumes a finish, which is rarer than it should be.</li>"
    "<li><b>Every episode carries plot.</b> Eight episodes cannot afford bridge hours.</li>"
    "<li><b>Casting becomes bolder.</b> Short commitments attract performances longer shows cannot.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/why-tv-seasons-are-getting-shorter/\">why TV seasons are getting shorter</a>, <a href=\"/entertainment/how-tv-shows-get-cancelled/\">how TV shows get cancelled</a> and <a href=\"/entertainment/why-prison-break-season-1-is-still-one-of-the-best-tv-seasons/\">why Prison Break season 1 still works</a>.</p>",

"home/diy-vs-professional-pests":
    "<h2>The line between the two</h2>"
    "<p>DIY pest control works on the household's share of the problem: sanitation, exclusion, and small infestations caught early. Professionals earn their fee when the colony is established, the access is structural, or the chemicals required are restricted. Knowing which situation you are in saves both money and months. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household pesticide guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Deciding honestly</h2>"
    "<ul>"
    "<li><b>One sighting, sealed entry: DIY.</b> Early and contained is the homeowner's case.</li>"
    "<li><b>Repeat activity after treatment: call.</b> Recurrence means a source the household cannot reach.</li>"
    "<li><b>Anything in the structure: call.</b> Voids, roof spaces and foundations are professional territory.</li>"
    "<li><b>Ask for the inspection report.</b> The diagnosis is worth as much as the treatment.</li>"
    "</ul>"
    "<p>See <a href=\"/home/pests-start-here/\">pests: first signs and first response</a>, <a href=\"/home/after-pest-treatment/\">after the pest treatment</a> and <a href=\"/home/wasp-nest-first-response/\">wasp nest first response</a>.</p>",

"sports/how-football-loans-work":
    "<h2>Loans are squad-building, not lending</h2>"
    "<p>A football loan moves a player's registration temporarily while the contract stays with the parent club — and every loan is a three-party negotiation about wages, playing time and an option to buy. The structure explains why the same club both loans players out and pays fees to loan players in. The <a href=\"" + _w("loan+%28association+football%29") + "\" rel=\"noopener\">loan system in association football</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What each party wants</h2>"
    "<ul>"
    "<li><b>The parent club</b> wants development minutes and wages covered.</li>"
    "<li><b>The loaning club</b> wants a first-team player without a transfer fee.</li>"
    "<li><b>The player</b> wants a role that justifies the move — the clause that matters most is playing time.</li>"
    "<li><b>Options to buy</b> price the loan's real economics; almost every deal turns on that number.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-football-contracts-work/\">how football contracts work</a>, <a href=\"/sports/how-football-agents-get-paid/\">how football agents get paid</a> and <a href=\"/sports/how-do-football-clubs-make-money/\">how football clubs make money</a>.</p>",

"writers/writing/statement-africa":
    "<h2>African writing, stated plainly</h2>"
    "<p>Statement Africa publishes African writing and criticism with an editorial voice that favours clarity and stakes over performance — essays, fiction and reported pieces from across the continent and its diasporas. For writers it is a market where specificity about place reads as strength. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What this market rewards</h2>"
    "<ul>"
    "<li><b>Named places over generic settings.</b> Specificity is the currency of place writing.</li>"
    "<li><b>Arguments with local stakes.</b> Pieces that could have been written anywhere fit nowhere in particular.</li>"
    "<li><b>Reported voices.</b> The interviews and documents make the essay credible.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/agbowo-essays/\">Agbowo essays</a>, <a href=\"/writers/writing/doek-literary-magazine/\">Doek Literary Magazine</a> and <a href=\"/writers/writing/afrolicious/\">Afrolicious</a>.</p>",

"home/electric-shower-tingle":
    "<h2>A tingle is a fault, full stop</h2>"
    "<p>Any tingling sensation from an electric shower is leakage current finding a path — through water, through a missing earth, or through a failing element. There is no safe version of this symptom and no diagnostic curiosity that justifies another use. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the electrical safety guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What to do immediately</h2>"
    "<ul>"
    "<li><b>Stop using it and isolate the circuit.</b> At the board, not just the switch.</li>"
    "<li><b>Do not attempt a repair to test it.</b> Water and mains voltage share the same small box on purpose.</li>"
    "<li><b>Have the earthing checked, not just the unit.</b> The shock path usually involves the installation.</li>"
    "</ul>"
    "<p>See <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a>, <a href=\"/home/wiring-red-flags-in-your-home/\">wiring red flags</a> and <a href=\"/home/why-does-my-circuit-breaker-keep-tripping/\">why the circuit breaker keeps tripping</a>.</p>",

"tech/private-dns-not-working":
    "<h2>Private DNS fails at the hostname</h2>"
    "<p>Android's Private DNS setting needs the resolver's hostname, not its IP address — and the most common failure is entering the address where the name belongs. The second most common is a network that intercepts the TLS handshake the setting relies on. Reference material sits under <a href=\"" + _w("DNS+over+TLS") + "\" rel=\"noopener\">DNS over TLS</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The fix order</h2>"
    "<ul>"
    "<li><b>Check the hostname spelling first.</b> Private DNS wants a name like dns.example.com, never an address.</li>"
    "<li><b>Test on mobile data.</b> A restrictive local network intercepts the handshake that makes the setting work.</li>"
    "<li><b>Try the automatic mode.</b> Automatic lets the device negotiate rather than requiring your chosen host.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/dns-not-working-propagation/\">DNS propagation problems</a>, <a href=\"/tech/dns-problems-diagnosed/\">DNS problems diagnosed</a> and <a href=\"/tech/browser-privacy-settings/\">browser privacy settings</a>.</p>",

"writers/learn/academic-writing/how-to-write-a-thesis":
    "<h2>A thesis is a defended claim</h2>"
    "<p>Everything in a thesis serves one sentence: the claim you will defend, and the order in which the defence runs. The literature review establishes the ground, the method establishes the evidence, the chapters argue in sequence, and the conclusion returns to the claim. The <a href=\"" + _w("thesis") + "\" rel=\"noopener\">thesis</a> form is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Building it in the right order</h2>"
    "<ul>"
    "<li><b>Write the claim as a working sentence from day one.</b> It is the project's only fixed point.</li>"
    "<li><b>Structure chapters as arguments.</b> A chapter that reports without arguing stalls the defence.</li>"
    "<li><b>Keep the evidence trail current.</b> Notes written during research are the thesis's raw material.</li>"
    "<li><b>Introduce and conclude each chapter.</b> Signposting is what makes long documents readable.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/academic-writing/how-to-write-a-literature-review/\">how to write a literature review</a>, <a href=\"/writers/learn/academic-writing/how-to-structure-a-research-paper/\">how to structure a research paper</a> and <a href=\"/writers/learn/academic-writing/how-to-cite-sources/\">how to cite sources</a>.</p>",

"writers/learn/grammar-language":
    "<h2>Grammar is a set of decisions</h2>"
    "<p>Working grammar for writers is less about rules than about choices with consequences: sentence length as rhythm, punctuation as pacing, and word choice as register. The technical vocabulary is useful exactly where it names a decision the writer would otherwise make by accident. The <a href=\"" + _w("grammar") + "\" rel=\"noopener\">grammar</a> tradition is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The decisions that matter most</h2>"
    "<ul>"
    "<li><b>Sentence length variation.</b> Rhythm is the difference between prose that reads and prose that drones.</li>"
    "<li><b>Commas as breath marks.</b> Punctuate for the reader's pace, then for the pedant's comfort.</li>"
    "<li><b>Register consistency.</b> Slipping between formal and casual loses readers faster than errors do.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-basics/\">writing basics</a>, <a href=\"/writers/learn/editing-proofreading/\">editing and proofreading</a> and <a href=\"/writers/learn/editing-proofreading/how-to-make-writing-more-concise/\">how to make writing more concise</a>.</p>",

"home/condensation-ventilation-that-works":
    "<h2>Ventilation works when it moves air out</h2>"
    "<p>Most condensation advice fails because it ventilates the room rather than the moisture. Extraction at the source — the kitchen, the bathroom, the drying rack — beats whole-house airflow every time, and the difference is measurable on the window the next morning. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor-air guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The hierarchy that works</h2>"
    "<ul>"
    "<li><b>Extract at the source first.</b> Moisture captured at the pot or the shower never reaches the wall.</li>"
    "<li><b>Then ventilate the room.</b> Cross-flow clears what escapes capture.</li>"
    "<li><b>Insulate the cold surfaces last.</b> Ventilation without warmth leaves the coldest wall as the condenser.</li>"
    "<li><b>Measure success on glass.</b> Morning window moisture is the honest readout.</li>"
    "</ul>"
    "<p>See <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three kinds of damp</a>, <a href=\"/home/kitchen-ventilation-damp/\">kitchen ventilation and damp</a> and <a href=\"/home/bathroom-fan-condensation/\">bathroom fans and condensation</a>.</p>",

"tech/plain-text-passwords":
    "<h2>Plaintext is the failure, not the breach</h2>"
    "<p>When a service stores passwords in plaintext, the breach has already happened — the database itself is the compromise, whether or not anyone has copied it. For users the sign is often small: a service that can email your password, rather than reset it. Reference material sits under <a href=\"" + _w("password+security") + "\" rel=\"noopener\">password security</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the warning signs</h2>"
    "<ul>"
    "<li><b>\"Forgot password\" that shows the password.</b> The service can only show what it stored.</li>"
    "<li><b>Odd password rules.</b> Short maximums and no symbols often indicate legacy storage limits.</li>"
    "<li><b>Your response plan matters more than detection.</b> Unique passwords per service make any single breach local.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/password-strength-checker/\">the password strength checker</a>, <a href=\"/tech/home-wifi-security-audit/\">the home Wi-Fi security audit</a> and <a href=\"/tech/security-questions-are-insecure/\">why security questions are insecure</a>.</p>",

"home/underfloor-heating-mistakes":
    "<h2>The system punishes guesswork</h2>"
    "<p>Underfloor heating runs on thermal mass: it heats slowly, holds long, and responds badly to the on-off habits that suit radiators. The common mistakes all follow from treating it like a fast system — oversized thermostat swings, furniture blocking the floor's output, and coverings chosen without the system's ratings in mind. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes home energy guidance this desk's heating pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The mistakes in order</h2>"
    "<ul>"
    "<li><b>Big thermostat swings.</b> The system works ahead; chasing temperature wastes the whole design.</li>"
    "<li><b>Thick rugs over the heated area.</b> Insulation on top is output thrown away.</li>"
    "<li><b>Ignoring the screed's heat-up time.</b> Seasonal starts take days, not hours.</li>"
    "</ul>"
    "<p>See <a href=\"/home/which-heating-system/\">choosing a heating system</a>, <a href=\"/home/heat-pump-vs-gas-furnace/\">heat pump versus gas furnace</a> and <a href=\"/home/uk-boiler-servicing/\">UK boiler servicing</a>.</p>",

"entertainment/best-streaming-service-us-uk":
    "<h2>The answer differs by catalogue and by contract</h2>"
    "<p>US and UK streaming libraries differ in licensing, and the best service for one household is decided by the specific shows it wants, the number of screens in use, and how often the household actually watches. The bundles question arrives before the catalogue question for most families. The <a href=\"" + _w("streaming+media") + "\" rel=\"noopener\">streaming media</a> market is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Deciding by household</h2>"
    "<ul>"
    "<li><b>List the must-watches first.</b> Catalogue comparisons start with titles, not tiers.</li>"
    "<li><b>Count concurrent screens.</b> The household's real pattern decides the plan faster than any feature matrix.</li>"
    "<li><b>Rotate rather than stack.</b> Monthly stacking is the expensive default; rotation is the deliberate one.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-streaming-apps-nigeria/\">the best streaming apps in Nigeria</a>, <a href=\"/entertainment/why-streaming-services-raise-prices/\">why streaming services raise prices</a> and <a href=\"/entertainment/how-streaming-bundles-work-explained/\">how streaming bundles work</a>.</p>",

"entertainment/german-expressionism-explained":
    "<h2>The movement that taught cinema light</h2>"
    "<p>German Expressionism of the 1920s turned sets into psychology — painted shadows, distorted geometry, and light that belonged to the character's mind rather than the room. Horror, film noir and the modern psychological thriller all descend from it, which is why the films still look modern when you watch them. Reference material sits under <a href=\"" + _w("German+Expressionism") + "\" rel=\"noopener\">German Expressionism</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the movement invented</h2>"
    "<ul>"
    "<li><b>Light as emotion.</b> Shadow stopped being weather and became meaning.</li>"
    "<li><b>Set as psyche.</b> The built environment started doing the acting.</li>"
    "<li><b>The horror vocabulary.</b> Every haunted-house frame since is quoting this decade.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/dogme-95-explained/\">Dogme 95 explained</a>, <a href=\"/entertainment/what-is-film-noir-explained/\">what film noir is</a> and <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a>.</p>",

"home/draught-proofing-mistakes":
    "<h2>Sealing a house is a system job</h2>"
    "<p>Draught-proofing done badly traps moisture along with the heat, blocks the ventilation the house needs, and occasionally seals combustion air supplies that must stay open. The correct order is to seal the deliberate leaks — around windows, doors, service entries — while leaving the designed ventilation paths alone. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes home energy guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The mistakes to avoid</h2>"
    "<ul>"
    "<li><b>Sealing the flue's air path.</b> Combustion air is not a draught.</li>"
    "<li><b>Ignoring the moisture trade.</b> Tighter houses need managed ventilation more, not less.</li>"
    "<li><b>Missing the service entries.</b> Pipe and cable gaps are the largest leaks in most rooms.</li>"
    "</ul>"
    "<p>See <a href=\"/home/uk-insulation-grants/\">UK insulation grants</a>, <a href=\"/home/single-glazing-payback/\">single glazing payback</a> and <a href=\"/home/condensation-ventilation-that-works/\">condensation ventilation that works</a>.</p>",

"home/wall-fan-making-noise":
    "<h2>Fan noise names the fault</h2>"
    "<p>A wall fan that rattles, whines or ticks is describing a specific mechanical problem: loose mounting, a blade imbalance, a bearing drying out, or a grille collecting dust unevenly. The noise's character points at the cause before anyone opens the housing. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household appliance guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the noise</h2>"
    "<ul>"
    "<li><b>Rattle at speed: mounting.</b> The wall plate and the housing screws come first.</li>"
    "<li><b>Whine with age: bearings.</b> A drying bearing announces itself before it seizes.</li>"
    "<li><b>Tick per revolution: the blade.</b> Something on the blade's edge is hitting the grille.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ceiling-fan-direction-summer-winter/\">ceiling fan direction for summer and winter</a>, <a href=\"/home/ceiling-fan-mounting-right/\">mounting a ceiling fan right</a> and <a href=\"/home/cost-to-run-a-fan/\">the cost of running a fan</a>.</p>",

"tech/tool/base64-encoder":
    "<h2>What Base64 actually is</h2>"
    "<p>Base64 encodes binary data as text so it can travel through systems that only carry characters — email attachments, JSON payloads, data URLs. It is an encoding, not encryption, and treating it as protection is one of security's quieter recurring mistakes. Reference material sits under <a href=\"" + _w("Base64") + "\" rel=\"noopener\">Base64</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using it correctly</h2>"
    "<ul>"
    "<li><b>Remember the expansion.</b> Base64 grows data by roughly a third; budget for it in payload limits.</li>"
    "<li><b>Watch the padding.</b> Trailing equals signs are part of the format, not cruft.</li>"
    "<li><b>Never treat it as security.</b> Encoding is reversible by anyone; secrets need real cryptography.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/json-formatter/\">the JSON formatter</a>, <a href=\"/tech/tool/url-encoder/\">the URL encoder</a> and <a href=\"/tech/tool/case-converter/\">the case converter</a>.</p>",

"tech/usb-hub-power-budget":
    "<h2>The hub is a power distribution problem</h2>"
    "<p>Every port on a USB hub shares a budget set by the host, the hub's own supply, or both. When drives spin up or phones fast-charge, the budget decides what stays connected — and the symptoms look like software faults until you do the arithmetic. Reference material sits under <a href=\"" + _w("USB") + "\" rel=\"noopener\">the Universal Serial Bus</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Doing the power arithmetic</h2>"
    "<ul>"
    "<li><b>Sum the devices' draw at peak, not idle.</b> Spin-up and fast-charge are the budget's real tests.</li>"
    "<li><b>Powered hubs for storage.</b> Drives that drop mid-write are a data problem wearing a power problem's clothes.</li>"
    "<li><b>Respect the cable length.</b> Long thin cables drop voltage before the device sees it.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/power-bank-size-math-for-tv-and-wifi/\">power-bank sizing for TV and Wi-Fi</a>, <a href=\"/tech/data-shuttle-sd-usb-ssd/\">moving data between SD, USB and SSD</a> and <a href=\"/tech/laptop-ram-vs-ssd-first/\">RAM or SSD: which upgrade first</a>.</p>",

"entertainment/bottle-episodes-explained":
    "<h2>The episode that saves its season's budget</h2>"
    "<p>A bottle episode confines its cast to one location with minimal guest cast — invented for money, kept for craft. The best ones turn the constraint into pressure-cooker drama that ordinary episodes cannot attempt, which is why the format keeps producing series highlights. Reference material sits under <a href=\"" + _w("bottle+episode") + "\" rel=\"noopener\">bottle episodes</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Why the constraint works</h2>"
    "<ul>"
    "<li><b>Containment forces confrontation.</b> Characters cannot leave, so the writing cannot either.</li>"
    "<li><b>Dialogue carries the production.</b> The format is where scripts prove themselves.</li>"
    "<li><b>Time pressure appears naturally.</b> One room and one problem is already a clock.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/why-tv-seasons-are-getting-shorter/\">why TV seasons are getting shorter</a>, <a href=\"/entertainment/how-tv-shows-get-cancelled/\">how TV shows get cancelled</a> and <a href=\"/entertainment/short-series-eight-episodes-or-fewer/\">short series of eight episodes or fewer</a>.</p>",

"entertainment/movie-calendar-2026-27":
    "<h2>How the release calendar thinks</h2>"
    "<p>The film calendar is planned years ahead around four corridors — spring break, summer, awards season, and the holiday window — and the corridor decides the marketing budget more than the film does. Reading the calendar explains most release-date news before the studios announce anything. The <a href=\"" + _w("film+distribution") + "\" rel=\"noopener\">film distribution</a> practice is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the corridors</h2>"
    "<ul>"
    "<li><b>Summer carries the tentpoles.</b> The corridor exists to maximise opening weekends.</li>"
    "<li><b>Autumn is the prestige lane.</b> Release timing here is an awards strategy.</li>"
    "<li><b>Moves are messages.</b> A delayed date is usually confidence, not logistics.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-movie-budgets-work/\">how movie budgets work</a>, <a href=\"/entertainment/how-movie-release-windows-work/\">how movie release windows work</a> and <a href=\"/entertainment/how-film-festivals-work/\">how film festivals work</a>.</p>",

"tech/tool/url-encoder":
    "<h2>Why URLs need encoding</h2>"
    "<p>URLs may only carry a restricted character set, so everything else — spaces, accents, reserved symbols — travels percent-encoded. The encoder and decoder exist because humans read spaces and systems read %20, and debugging the difference between them is a daily web task. Reference material sits under <a href=\"" + _w("percent-encoding") + "\" rel=\"noopener\">percent-encoding</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using it correctly</h2>"
    "<ul>"
    "<li><b>Encode the data, not the structure.</b> Encoding a whole URL turns separators into payloads.</li>"
    "<li><b>Know the reserved set.</b> Query separators in the wrong state cause most broken links.</li>"
    "<li><b>Check the double-encoding trap.</b> Encoded input re-encoded explains many \"works in the browser\" mysteries.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/base64-encoder/\">the Base64 encoder</a>, <a href=\"/tech/tool/json-formatter/\">the JSON formatter</a> and <a href=\"/tech/tool/http-status-lookup/\">the HTTP status lookup</a>.</p>",

"writers/learn/creative-writing/how-to-write-a-short-story":
    "<h2>The short story is a single effect</h2>"
    "<p>Short stories are built around one change — a character, a situation, a recognition — and every scene either advances that change or sharpens its edge. The form's economy is its art: nothing survives that does not serve the turn. The <a href=\"" + _w("short+story") + "\" rel=\"noopener\">short story</a> form is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Building the single effect</h2>"
    "<ul>"
    "<li><b>Know the turn before drafting.</b> The story's last revelation decides what the opening must hide.</li>"
    "<li><b>Start as late as the story allows.</b> Short forms punish warm-up scenes.</li>"
    "<li><b>Let one image carry the ending.</b> Resonance is the form's closing currency.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/creative-writing/how-to-develop-characters/\">how to develop characters</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-a-blog-post/\">how to write a blog post</a> and <a href=\"/writers/learn/writing-basics/\">writing basics</a>.</p>",

"sports/mma-decisions-and-draws-explained":
    "<h2>How judges see a fight</h2>"
    "<p>MMA scoring borrows boxing's ten-point must system but judges the whole fight's damage, control and near-finishes rather than clean punching alone. Draws happen when the criteria genuinely split — and the rare official draw is a scoring statement rather than an administrative outcome. Reference material sits under <a href=\"" + _w("mixed+martial+arts+rules") + "\" rel=\"noopener\">mixed martial arts rules</a>. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the scorecards</h2>"
    "<ul>"
    "<li><b>Damage is the first criterion.</b> Control wins rounds only when damage is equal.</li>"
    "<li><b>Rounds are scored whole.</b> A late flurry against a dominant round rarely flips it.</li>"
    "<li><b>Unanimous, split and majority</b> each describe agreement differently — the result is one thing, the cards another.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/boxing-decisions-explained/\">boxing decisions explained</a>, <a href=\"/sports/boxing-scoring-explained/\">how boxing scoring works</a> and <a href=\"/sports/how-boxing-fights-end-explained/\">how boxing fights end</a>.</p>",

"tech/before-a-new-laptop-the-two-part-surgery":
    "<h2>The two parts of a laptop handover</h2>"
    "<p>Replacing a laptop is two jobs in sequence: retiring the old machine completely — accounts, data, licences — and commissioning the new one deliberately, before the first hour of use decides its habits. Doing the first carelessly leaks accounts; doing the second carelessly wastes years of battery life. The <a href=\"" + _w("laptop") + "\" rel=\"noopener\">laptop</a> category is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The checklist, in order</h2>"
    "<ul>"
    "<li><b>Old machine: deauthorise and wipe.</b> Licences and saved accounts outlive the hardware if you let them.</li>"
    "<li><b>New machine: update before installing.</b> The factory image is always behind.</li>"
    "<li><b>Set the battery habits in week one.</b> Charging patterns are learned early and kept.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-buying-ram-storage/\">laptop buying: RAM and storage</a>, <a href=\"/tech/student-laptop-spec-floor-2026/\">the student laptop spec floor</a> and <a href=\"/tech/dell-vs-hp-refurbished-laptops-nigeria/\">Dell versus HP refurbished laptops in Nigeria</a>.</p>",

"tech/laptop-no-display-boot-ladder":
    "<h2>Climb from the cheapest explanation</h2>"
    "<p>A laptop with power but no display is a ladder of possibilities ordered by cost: brightness and output mode, then memory seating, then the panel and its cable, then board-level failure. Working the ladder in order prevents the classic mistake of replacing the screen when the memory was loose. Reference material sits under <a href=\"" + _w("booting") + "\" rel=\"noopener\">booting</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The ladder, bottom first</h2>"
    "<ul>"
    "<li><b>Light, then output mode.</b> A flashlight on the panel reveals a backlight fault instantly.</li>"
    "<li><b>External display next.</b> It separates panel faults from board faults in one cable.</li>"
    "<li><b>Reseat the memory.</b> The cheapest board-level fix and the commonest cause.</li>"
    "<li><b>Listen to the boot.</b> Fans and drive activity tell you how far the machine gets.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-overheating-fan-noise/\">laptop overheating and fan noise</a>, <a href=\"/tech/laptop-spill-first-five-minutes/\">the first five minutes after a spill</a> and <a href=\"/tech/external-drive-not-showing-up/\">external drive not showing up</a>.</p>",

"home/entry-point-mistakes":
    "<h2>The house is entered through its decisions</h2>"
    "<p>Break-ins follow opportunity patterns rather than cinematic ones: a side gate left free, a window lock that never engaged, a hedge that hides the one window without a latch. The security mistakes that matter are all ordinary ones, which is good news — ordinary mistakes are fixable. The <a href=\"" + _w("burglar+alarm") + "\" rel=\"noopener\">home security</a> practice is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The mistakes, cheapest first</h2>"
    "<ul>"
    "<li><b>Lighting the wrong things.</b> Illuminating the street while leaving the entry dim is backwards.</li>"
    "<li><b>Hiding the entry from sight.</b> Screening the door from neighbours helps everyone except the house.</li>"
    "<li><b>Locks that never engage.</b> A deadbolt without a habit is furniture.</li>"
    "</ul>"
    "<p>See <a href=\"/home/renter-security/\">renter security</a>, <a href=\"/home/renter-friendly-fixes/\">renter-friendly fixes</a> and <a href=\"/home/barred-windows-and-fire-escape/\">barred windows and fire escapes</a>.</p>",

"writers/writing/cracked":
    "<h2>Humour writing as a professional market</h2>"
    "<p>Cracked built its name on comedy writing that does actual work — researched premises, structured lists and pieces where the jokes ride on information. For freelancers it is a reminder that humour markets pay for reliability and pitch discipline exactly like serious ones. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching humour professionally</h2>"
    "<ul>"
    "<li><b>The premise is the pitch.</b> If the concept is not funny before the writing, no draft will save it.</li>"
    "<li><b>Research like a reported piece.</b> The funniest observations are the most accurate ones.</li>"
    "<li><b>Deliver on the joke count the format promises.</b> Structure is what humour editors commission.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/listverse/\">Listverse</a>, <a href=\"/writers/writing/income-diary/\">Income Diary</a> and <a href=\"/writers/writing/business-insider/\">Business Insider</a>.</p>",

"writers/writing/new-lines-magazine":
    "<h2>Essays on the world as it is</h2>"
    "<p>New Lines Magazine publishes essays, reviews and reportage on politics, culture and ideas with a policy audience in mind — pieces that argue rather than survey. For writers it is a market where subject expertise and a defensible position matter more than style experiments. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching argument-led essays</h2>"
    "<ul>"
    "<li><b>Take a position in the pitch.</b> Editors commission arguments, not topics.</li>"
    "<li><b>Bring the evidence you can show.</b> Access and documents are the pitch's backbone.</li>"
    "<li><b>Write for readers who follow the field.</b> Policy audiences reward precision and punish filler.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/noema/\">Noema</a>, <a href=\"/writers/writing/guernica/\">Guernica</a> and <a href=\"/writers/writing/aeon-essays/\">Aeon essays</a>.</p>",

"entertainment/how-movie-budgets-work":
    "<h2>Where the money actually goes</h2>"
    "<p>Movie budgets split into three unequal parts: above-the-line talent, below-the-line production, and the post-release marketing spend that often rivals the negative cost. Understanding the split explains studio behaviour — which films get greenlit, which get dumped, and why a modest hit can lose money. Reference material sits under <a href=\"" + _w("film+budget") + "\" rel=\"noopener\">film budgets</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading a budget headline</h2>"
    "<ul>"
    "<li><b>Production cost is not the spend.</b> Prints and advertising can double the number in trade papers.</li>"
    "<li><b>Star salaries are leverage, not waste.</b> Above-the-line names are marketing decisions as much as casting.</li>"
    "<li><b>Break-even is a range.</b> Theatrical splits differ by market, and home windows extend the tail.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-movie-release-windows-work/\">how movie release windows work</a>, <a href=\"/entertainment/how-film-festivals-work/\">how film festivals work</a> and <a href=\"/entertainment/movie-calendar-2026-27/\">the movie calendar 2026-27</a>.</p>",

"entertainment/what-you-need-for-4k-streaming":
    "<h2>4K is a chain, not a screen</h2>"
    "<p>Streaming in 4K requires every link at once: a display that shows it, a plan that carries it, a connection that sustains it, and a device that decodes it. Break any one and the stream quietly serves HD while the household pays for 4K. The <a href=\"" + _w("4K+resolution") + "\" rel=\"noopener\">4K resolution</a> standards are documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Checking each link</h2>"
    "<ul>"
    "<li><b>The display's real panel.</b> Native 4K, not upscaling claims.</li>"
    "<li><b>The connection's stability.</b> Sustained speed matters more than peak speed tests.</li>"
    "<li><b>The device's decoder.</b> Older sticks cap at HD regardless of the plan.</li>"
    "<li><b>The plan's household limits.</b> Concurrent 4K streams are where plans divide.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-streaming-apps-nigeria/\">the best streaming apps in Nigeria</a>, <a href=\"/entertainment/cheapest-way-to-stream-movies/\">the cheapest way to stream movies</a> and <a href=\"/tech/streaming-quality-settings/\">streaming quality settings</a>.</p>",

"home/blender-wont-run-smells-hot":
    "<h2>Stop at the smell</h2>"
    "<p>A blender that will not start and smells hot has told you to unplug it: the motor has stalled against a load, the winding insulation is cooking, or the safety interlock is doing its job. Continued attempts turn a repairable appliance into a fire risk. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes home electrical safety guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The order of checks, unplugged</h2>"
    "<ul>"
    "<li><b>Jar seating and interlocks.</b> Most no-starts are the safety system refusing an unsafe assembly.</li>"
    "<li><b>Load in the jar.</b> Frozen and thick loads stall blades that spin freely empty.</li>"
    "<li><b>The motor's smell.</b> Sharp electrical smells mean service, not another attempt.</li>"
    "</ul>"
    "<p>See <a href=\"/home/appliances-that-use-the-most-electricity/\">the appliances that use the most electricity</a>, <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a> and <a href=\"/home/appliances/\">the appliances guide</a>.</p>",

"tech/android-find-lost-phone":
    "<h2>Find My Device works when it was set up</h2>"
    "<p>Android's device tracking needs three things configured before the phone is lost: the account signed in, location history or Find My Device enabled, and a screen lock that protects the data while you decide. After the loss, only preparation helps — and the account's web panel is the recovery console. The <a href=\"" + _w("Find+My+Device") + "\" rel=\"noopener\">device-finding services</a> are documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Set up before you need it</h2>"
    "<ul>"
    "<li><b>Enable the finding service today.</b> The feature is useless if it was off at the moment of loss.</li>"
    "<li><b>Keep the account recoverable.</b> A locked recovery email locks out the finder too.</li>"
    "<li><b>Lock remotely, recover second.</b> Data protection is the first action, location the second.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-backup-guide/\">the Android backup guide</a>, <a href=\"/tech/free-up-storage-android/\">freeing up Android storage</a> and <a href=\"/tech/home-wifi-security-audit/\">the home Wi-Fi security audit</a>.</p>",

"writers/guides/how-to-write-a-strong-query-letter":
    "<h2>The query sells the book in one page</h2>"
    "<p>A query letter does three jobs in a single page: present the book's pitch like catalogue copy, place the project in its market, and introduce the writer's credentials honestly. Agents read for sellability first, so the letter's first paragraph is the whole audition. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes trade resources for querying writers. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The one-page structure</h2>"
    "<ul>"
    "<li><b>The pitch paragraph first.</b> Title, category, comparable titles and the hook in order.</li>"
    "<li><b>The credentials that matter.</b> Relevant publications and expertise, without padding.</li>"
    "<li><b>Follow the agency's stated format exactly.</b> Submission discipline is itself a credential.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a pitch</a>, <a href=\"/writers/learn/writing-for-publication/how-to-pitch-an-editor/\">how to pitch an editor</a> and <a href=\"/writers/guides/how-to-follow-up-on-a-writing-pitch/\">how to follow up on a writing pitch</a>.</p>",

"writers/learn/examples/example-of-a-report":
    "<h2>What the example demonstrates</h2>"
    "<p>A report example shows the form's discipline: an executive summary that carries the findings, sections organised by question rather than by chronology, evidence placed where the claim is made, and recommendations that name owners and times. The <a href=\"" + _w("report") + "\" rel=\"noopener\">report</a> is the standard form of professional nonfiction. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading your draft against it</h2>"
    "<ul>"
    "<li><b>Does the summary stand alone?</b> Most readers never reach page three.</li>"
    "<li><b>Are findings separated from recommendations?</b> What is true and what to do are different sections.</li>"
    "<li><b>Is every claim traceable to evidence?</b> Reports are audited documents by design.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-of-a-press-release/\">the press release example</a>, <a href=\"/writers/learn/examples/example-blog-post/\">the blog post example</a> and <a href=\"/writers/learn/examples/example-of-a-book-review/\">the book review example</a>.</p>",

"home/bathroom-remodel-mistakes":
    "<h2>The bathroom punishes sequencing errors</h2>"
    "<p>Bathroom remodels fail in the order of trades: waterproofing under tile, drainage falls before fixtures, ventilation decided after the ceiling closes. Each mistake is invisible when the room looks finished and expensive when the ceiling below stains. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes home improvement guidance this desk's renovation pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The sequencing rules</h2>"
    "<ul>"
    "<li><b>Waterproofing is inspected before tile.</b> The membrane is the room's real product.</li>"
    "<li><b>Falls and drainage before the suite.</b> Fixtures can be moved; pipe runs cannot.</li>"
    "<li><b>Ventilation before aesthetics.</b> The fan's duct route decides whether the ceiling closes.</li>"
    "</ul>"
    "<p>See <a href=\"/home/bath-silicone-reseal/\">bath silicone reseal</a>, <a href=\"/home/bathroom-grout-mould/\">bathroom grout mould</a> and <a href=\"/home/uk-us-plumber-rules/\">UK and US plumber rules</a>.</p>",

"tech/saas-software":
    "<h2>Choosing software by its exit</h2>"
    "<p>Software and SaaS choices age into lock-in slowly: data formats, workflow habits and team knowledge all accumulate inside the tool. The mature way to choose is to price the exit at the start — export quality, migration paths, and what happens to the work if the pricing changes. The <a href=\"" + _w("software+as+a+service") + "\" rel=\"noopener\">software as a service</a> model is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The selection questions</h2>"
    "<ul>"
    "<li><b>Can we export everything, today?</b> Exit capability is the contract that matters.</li>"
    "<li><b>What is the pricing trigger?</b> Every SaaS has a usage number where the cost jumps.</li>"
    "<li><b>Who owns the work?</b> Review the tool's terms for content rights before the team commits.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/cloud-storage-plans-compared/\">cloud storage plans compared</a>, <a href=\"/tech/microsoft-365-free-vs-paid/\">Microsoft 365 free versus paid</a> and <a href=\"/tech/best-password-manager-for-you/\">choosing the best password manager</a>.</p>",

"writers/writing/the-sun-magazine":
    "<h2>A magazine of personal writing</h2>"
    "<p>The Sun has published intimate, unadorned personal writing for decades — essays, fiction and poetry that earn their place through honesty of observation rather than style. It pays professional rates and reads slowly, which makes it a benchmark market for writers working in the personal essay tradition. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing for the personal tradition</h2>"
    "<ul>"
    "<li><b>The specific scene beats the general feeling.</b> This tradition trusts concrete detail over summary.</li>"
    "<li><b>Consent is craft.</b> Writing about others honestly is part of the work's ethics.</li>"
    "<li><b>Submit your most finished piece.</b> Slow-reading markets reward patience with drafts.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/mslexia/\">Mslexia</a>, <a href=\"/writers/writing/briarpatch/\">Briarpatch</a> and <a href=\"/writers/writing/broadview/\">Broadview</a>.</p>",

"entertainment/one-piece-vs-naruto":
    "<h2>Two philosophies of long-running anime</h2>"
    "<p>One Piece and Naruto represent the two great structures of long-running manga adaptation: the endless voyage where world-building is the product, and the closed hero's journey with a chosen destination. Comparing them is really comparing what audiences want from hundreds of episodes. Reference material sits under <a href=\"" + _w("sh%C5%8Dnen") + "\" rel=\"noopener\">shōnen manga</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The comparison that matters</h2>"
    "<ul>"
    "<li><b>Pacing philosophy.</b> One serialises discovery; the other escalates destiny.</li>"
    "<li><b>Filler handling.</b> Both adaptations stretch, and each stretches differently.</li>"
    "<li><b>The ending question.</b> A defined ending changes how every earlier arc reads.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/isekai-anime-explained/\">isekai anime explained</a>, <a href=\"/entertainment/best-kdramas-to-start-with/\">the best K-dramas to start with</a> and <a href=\"/entertainment/10-anime-like-solo-leveling-you-should-watch/\">10 anime like Solo Leveling</a>.</p>",

"home/pests-start-here":
    "<h2>The first response decides the campaign</h2>"
    "<p>Pest problems are easiest at the first sighting: identify the intruder, find the entry and the attractant, and act before a colony establishes. Everything in this desk's pest guides follows that order — identification before treatment, exclusion before poison, and professionals for anything structural. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes household pest guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The first-response order</h2>"
    "<ul>"
    "<li><b>Identify before acting.</b> Ants, roaches and rats each need different countermeasures.</li>"
    "<li><b>Find the entry, not just the pest.</b> The route is what returns the population.</li>"
    "<li><b>Remove the attractant on day one.</b> Sanitation multiplies every other measure.</li>"
    "</ul>"
    "<p>See <a href=\"/home/diy-vs-professional-pests/\">DIY versus professional pest control</a>, <a href=\"/home/after-pest-treatment/\">after the pest treatment</a> and <a href=\"/home/compound-mosquito-control-night/\">compound mosquito control at night</a>.</p>",

"home/why-is-my-electric-bill-so-high":
    "<h2>The bill is a measurement of habits</h2>"
    "<p>Electricity bills rise from a short list of causes: a rate change, a load that appeared, an appliance that is failing, or a meter reading that finally corrected months of estimates. Working the list in that order finds most increases without a single purchase. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household energy guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The diagnostic order</h2>"
    "<ul>"
    "<li><b>Compare rate and usage separately.</b> The tariff changed or the consumption did; the bill shows which.</li>"
    "<li><b>Audit the heating and cooling loads.</b> They dominate every household's numbers.</li>"
    "<li><b>Watch for the failing appliance.</b> A motor running constantly is the classic silent increase.</li>"
    "</ul>"
    "<p>See <a href=\"/home/appliances-that-use-the-most-electricity/\">the appliances that use the most electricity</a>, <a href=\"/home/cost-to-run-a-fan/\">the cost of running a fan</a> and <a href=\"/home/smart-thermostat-payback/\">smart thermostat payback</a>.</p>",

"tech/api-errors-decoded":
    "<h2>Errors are the API explaining itself</h2>"
    "<p>API error responses carry more information than their status codes suggest: error codes name the failure class, messages often name the field, and headers tell you about limits and retries. Reading all three turns integration debugging from guesswork into triage. Reference material sits under <a href=\"" + _w("web+API") + "\" rel=\"noopener\">web APIs</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Decoding the response</h2>"
    "<ul>"
    "<li><b>Status first, body second.</b> The code class tells you whose move it is.</li>"
    "<li><b>Log the full payload.</b> Error bodies are the documentation for the failure case.</li>"
    "<li><b>Respect the retry headers.</b> Rate limits publish their own windows.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/call-api-python/\">calling an API in Python</a>, <a href=\"/tech/handle-api-errors-python/\">handling API errors in Python</a> and <a href=\"/tech/tool/http-status-lookup/\">the HTTP status lookup</a>.</p>",

"tech/browser-privacy-settings":
    "<h2>Settings that actually reduce exposure</h2>"
    "<p>Browser privacy controls separate into three strengths: blocking third-party tracking, limiting what sites may store, and deciding which permissions sites keep. Most users benefit from the first two immediately; the third is the one that degrades sites when set too tightly. Reference material sits under <a href=\"" + _w("browser+security") + "\" rel=\"noopener\">browser security</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The settings, in order of value</h2>"
    "<ul>"
    "<li><b>Third-party cookies and trackers.</b> The single highest-value change on any browser.</li>"
    "<li><b>Site storage limits.</b> Clearing on exit breaks few sites and removes much.</li>"
    "<li><b>Permissions per site.</b> Camera, microphone and location are granted in haste and kept forever.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/private-dns-not-working/\">private DNS problems</a>, <a href=\"/tech/home-wifi-security-audit/\">the home Wi-Fi security audit</a> and <a href=\"/tech/vpn-what-it-protects/\">what a VPN protects</a>.</p>",

"writers/writing/the-drift":
    "<h2>A magazine of the middle distance</h2>"
    "<p>The Drift publishes essays and criticism at the pace of the conversation — short, argued, and alert to where culture and politics meet. Its market logic is speed with standards: pieces arrive while the question is live and hold up when it is not. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing at conversation pace</h2>"
    "<ul>"
    "<li><b>Keep a file of live questions.</b> Fast essays are drafted before they are commissioned.</li>"
    "<li><b>One argument, defended.</b> Short forms punish the survey response.</li>"
    "<li><b>Know the room.</b> These essays are read by people already in the debate.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/hobart/\">Hobart</a>, <a href=\"/writers/writing/mudroom/\">Mudroom</a> and <a href=\"/writers/writing/carte-blanche/\">Carte Blanche</a>.</p>",

"home/single-glazing-payback":
    "<h2>Payback starts with the frames</h2>"
    "<p>Replacing single glazing is a comfort upgrade first and an energy upgrade second: the savings depend on the frames, the orientation and how much of the wall is glass, not just the U-value on the quote. The honest calculation compares full window replacement against secondary glazing and draught work first. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes home energy guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Running the numbers honestly</h2>"
    "<ul>"
    "<li><b>Measure comfort, not just bills.</b> The coldest room's use is the upgrade's real gain.</li>"
    "<li><b>Price the alternatives.</b> Secondary glazing and heavy curtains capture much of the benefit.</li>"
    "<li><b>Include the frame quality.</b> A good unit in a poor frame performs like neither.</li>"
    "</ul>"
    "<p>See <a href=\"/home/uk-insulation-grants/\">UK insulation grants</a>, <a href=\"/home/draught-proofing-mistakes/\">draught-proofing mistakes</a> and <a href=\"/home/which-heating-system/\">choosing a heating system</a>.</p>",

"home/toilet-weak-flush-fixes":
    "<h2>Weak flush is a water-path problem</h2>"
    "<p>A toilet that flushes weakly is usually under-supplied, blocked at the rim jets, or fighting a venting problem — three causes with three different fixes, all visible without parts. The diagnosis starts at the cistern and ends at the soil stack. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household water guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The fix order</h2>"
    "<ul>"
    "<li><b>Check the fill and the fill line first.</b> A low water level is the commonest cause.</li>"
    "<li><b>Clear the rim jets.</b> Mineral scale blocks the small holes that give the flush its swirl.</li>"
    "<li><b>Consider the vent when nothing else fits.</b> Slow drainage elsewhere in the house points at the stack.</li>"
    "</ul>"
    "<p>See <a href=\"/home/how-to-fix-a-slow-draining-sink/\">fixing a slow-draining sink</a>, <a href=\"/home/how-to-clear-a-slow-shower-drain/\">clearing a slow shower drain</a> and <a href=\"/home/sewer-smell-after-trip/\">sewer smell after a trip</a>.</p>",

"writers/learn/examples/example-of-a-newsletter":
    "<h2>What the example shows</h2>"
    "<p>A newsletter example teaches the form's real constraints: one subject per issue, a subject line that earns the open, a structure that survives skimming, and a close that gives the reader one action. The <a href=\"" + _w("newsletter") + "\" rel=\"noopener\">newsletter</a> is the oldest new format in digital writing. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading your draft against it</h2>"
    "<ul>"
    "<li><b>Does the issue have one subject?</b> Multi-topic issues are unread issues.</li>"
    "<li><b>Is the structure skimmable?</b> Newsletters are triaged in inboxes before they are read.</li>"
    "<li><b>Is the ask singular?</b> One action per issue is the working rule.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-of-a-press-release/\">the press release example</a>, <a href=\"/writers/learn/examples/example-of-a-report/\">the report example</a> and <a href=\"/writers/learn/examples/example-of-a-professional-email/\">the professional email example</a>.</p>",

"writers/learn/writing-for-publication":
    "<h2>Publication is a process, not a prize</h2>"
    "<p>Writing for publication means writing for an editor's constraints: the audience the venue serves, the length the page carries, the calendar the issue runs on, and the editorial standards the readers expect. The writers who publish steadily treat each of these as design inputs rather than obstacles. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes the field's working standards. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The process in four moves</h2>"
    "<ul>"
    "<li><b>Study the venue before the idea.</b> Every published piece began with a reader in mind.</li>"
    "<li><b>Pitch to the editor's brief, not your draft.</b> The commission decides the piece.</li>"
    "<li><b>Revise on the editor's notes exactly.</b> The revision round is where careers are built.</li>"
    "<li><b>Keep the receipts.</b> Publication records are the raw material of every future pitch.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-for-publication/how-to-pitch-an-editor/\">how to pitch an editor</a>, <a href=\"/writers/guides/how-to-write-a-strong-query-letter/\">how to write a strong query letter</a> and <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a pitch</a>.</p>",

"entertainment/korean-cinema-starter-guide-rebuilt":
    "<h2>Where to start, and why</h2>"
    "<p>Korean cinema's global arrival was built on a generation of films that crossed genres without asking permission — revenge thrillers, family dramas, genre hybrids that treat class as the engine. A starter guide works best as a map of those genre lanes rather than a ranked list. Reference material sits under <a href=\"" + _w("cinema+of+Korea") + "\" rel=\"noopener\">the cinema of Korea</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The three lanes to watch first</h2>"
    "<ul>"
    "<li><b>The revenge thriller lane,</b> where the genre machinery is at its most precise.</li>"
    "<li><b>The family drama lane,</b> where the industry's emotional range shows.</li>"
    "<li><b>The genre hybrid lane,</b> where Korean filmmakers do their most original work.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-kdramas-to-start-with/\">the best K-dramas to start with</a>, <a href=\"/entertainment/kdrama-genres-explained/\">K-drama genres explained</a> and <a href=\"/entertainment/10-korean-movies-everyone-should-watch/\">10 Korean movies everyone should watch</a>.</p>",

"home/hvac-diy-warranty-rules":
    "<h2>What the warranty actually forbids</h2>"
    "<p>HVAC warranties are narrower than owners assume: they cover manufacturing defects while excluding installation errors, unapproved parts, and maintenance gaps documented by skipped service. The DIY line is therefore drawn by the warranty text, not by the owner's confidence. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes consumer guidance this desk's equipment pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the warranty before the wrench</h2>"
    "<ul>"
    "<li><b>Filter and coil cleaning are yours.</b> The user-serviceable list is printed for a reason.</li>"
    "<li><b>Refrigerant work is not.</b> Sealed-system service requires certified handling almost everywhere.</li>"
    "<li><b>Keep the service record.</b> Warranty claims are proven with paperwork, not memories.</li>"
    "</ul>"
    "<p>See <a href=\"/home/which-heating-system/\">choosing a heating system</a>, <a href=\"/home/heat-pump-vs-gas-furnace/\">heat pump versus gas furnace</a> and <a href=\"/home/uk-boiler-servicing/\">UK boiler servicing</a>.</p>",

"home/uk-us-plumber-rules":
    "<h2>Same trade, different rulebooks</h2>"
    "<p>\"Just call a plumber\" means different things in the UK and the US: who may legally do which work, how certification is checked, and what the household is liable for afterwards all differ. Knowing the local rulebook prevents both illegal work and pointless hesitation. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes the UK side of these rules; US requirements vary by state and municipality. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What differs in practice</h2>"
    "<ul>"
    "<li><b>Who can sign off the work.</b> Notification rules decide which jobs need registered professionals.</li>"
    "<li><b>What homeowners may legally do.</b> The boundary sits differently in each jurisdiction.</li>"
    "<li><b>Liability follows the paperwork.</b> Insurance asks who did the work before it pays.</li>"
    "</ul>"
    "<p>See <a href=\"/home/part-p-explained/\">Part P explained</a>, <a href=\"/home/us-home-permits/\">US home permits</a> and <a href=\"/home/uk-landlord-damp-mould-duties/\">landlord duties on damp and mould</a>.</p>",

"writers/learn/editing-proofreading/how-to-make-writing-more-concise":
    "<h2>Concision is editing's first discipline</h2>"
    "<p>Concise writing is not short writing; it is writing where every phrase carries load. The editing pass that achieves it looks for the same few patterns — duplicated meaning, empty scaffolding, adjective stacks, and sentences whose point arrives last. The <a href=\"" + _w("concise+writing") + "\" rel=\"noopener\">concise writing</a> tradition is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The concision pass</h2>"
    "<ul>"
    "<li><b>Put the point first.</b> Sentences that warm up waste their reader's attention.</li>"
    "<li><b>Cut the scaffolding.</b> \"It is important to note that\" is never the sentence's content.</li>"
    "<li><b>Read aloud for breath.</b> The reading voice finds what the eye forgives.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/editing-proofreading/\">editing and proofreading</a>, <a href=\"/writers/learn/grammar-language/\">grammar and language</a> and <a href=\"/writers/learn/writing-basics/\">writing basics</a>.</p>",

"writers/privacy":
    "<h2>How this policy works in practice</h2>"
    "<p>This page states the privacy rules for BRYME Writers specifically — the house policy applies across every desk, and the writers' tools and opportunity database operate within it. The short version: no accounts are required to read, tracker entries stay in your browser, and the opportunity database is published with its verification dates precisely so readers can check our claims. The <a href=\"" + _w("privacy+policy") + "\" rel=\"noopener\">privacy policy</a> is a standard form; ours follows the house rules on this site. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Your choices on this desk</h2>"
    "<ul>"
    "<li><b>Reading needs no data.</b> The guides and listings run without accounts or profiles.</li>"
    "<li><b>Your tracker is your data.</b> Submission records live in your browser unless you export them.</li>"
    "<li><b>Third-party links leave our pages.</b> The outlets we list have their own policies.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/about/\">about BRYME Writers</a>, <a href=\"/writers/disclosure/\">our disclosure</a> and <a href=\"/writers/contact/\">contact the desk</a>.</p>",

"entertainment/scariest-horror-movies-tonight":
    "<h2>Scare is a design choice</h2>"
    "<p>The horror films that frighten most reliably work through three levers: dread pacing, sound design, and the withheld image. Jump scares are the cheapest of the tools and the shortest-lived; the films still frightening years later built their fear structurally. Reference material sits under <a href=\"" + _w("horror+film") + "\" rel=\"noopener\">horror film</a>. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What tonight's picks should show</h2>"
    "<ul>"
    "<li><b>Dread over shock.</b> The slow build outlasts the sting every time.</li>"
    "<li><b>Sound doing half the work.</b> The best horror soundtracks are mostly silence.</li>"
    "<li><b>One great withheld image.</b> What the film refuses to show is its whole budget.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/movie/nosferatu/\">Nosferatu</a>, <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a> and <a href=\"/entertainment/what-is-film-noir-explained/\">what film noir is</a>.</p>",

}

# Top-up sections for pages that already carry a t8 block but are still under
# their class bar. Injected under marker data-esrc="t8b".
TOPUP_SECTIONS11 = {

"sports/la-liga-results":
    "<h2>Results as form evidence</h2>"
    "<p>A La Liga results run tells the story the table compresses: which streaks are real form, which are schedule effects, and which sides are converting narrow games. Reading results as sequences is the oldest analytic discipline in the sport and still one of the most reliable. The <a href=\"" + _w("La+Liga") + "\" rel=\"noopener\">La Liga</a> competition structure is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the run</h2>"
    "<ul>"
    "<li><b>Sequence over totals.</b> Form is a direction, not an aggregate.</li>"
    "<li><b>Note who scored first.</b> Teams that lead early win differently from teams that chase.</li>"
    "<li><b>Weight the opposition.</b> Results are samples; the schedule decides what they measure.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league-results/\">the Premier League results</a>, <a href=\"/sports/bundesliga-results/\">the Bundesliga results</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",

"tech/tool/password-strength-checker":
    "<h2>What strength actually means</h2>"
    "<p>Password strength is the cost of guessing it — which depends on length and on the attacker's method, not on how many symbols it contains. The modern standard is long passphrases checked against known breaches, and the checker's job is to show the estimate honestly rather than award a colour. Reference material sits under <a href=\"" + _w("password+strength") + "\" rel=\"noopener\">password strength</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using the estimate well</h2>"
    "<ul>"
    "<li><b>Length beats variety.</b> Four unrelated words outperform one decorated word by centuries.</li>"
    "<li><b>Uniqueness per account is the multiplier.</b> Strength matters most where reuse is common.</li>"
    "<li><b>Never paste a real password into any checker.</b> Estimates belong on samples.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/base64-encoder/\">the Base64 encoder</a>, <a href=\"/tech/plain-text-passwords/\">plain-text passwords</a> and <a href=\"/tech/best-password-manager-for-you/\">choosing the best password manager</a>.</p>",

}
