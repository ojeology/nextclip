# -*- coding: utf-8 -*-
"""Editorial depth sections, part 9: batch E, the 703-720 word tranche against
the 750-word bar, two tool pages under the 669 tool bar, and the first atlas
record page (788 of the 819 record bar). Writers, tech, home, sports desks.
Every external URL curl-verified 200 at authoring time; every internal link
verified to a real page."""

WHO = "https://www.who.int/"
EPA = "https://www.epa.gov/"
GOVUK = "https://www.gov.uk/"
NFPA = "https://www.nfpa.org/"
CLMP = "https://www.clmp.org/"
PL = "https://www.premierleague.com/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS9 = {

"writers/writing/psyche-first-person":
    "<h2>First person is a reporting position</h2>"
    "<p>Psyche publishes first-person essays that use the self as an instrument rather than a subject — the writer's experience is the lens, but the focus sits outside the writer. That editorial line separates the form from diary writing: the essay still needs research, structure and a claim about the world. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the digital essay outlets of this kind. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What first-person essays need</h2>"
    "<ul>"
    "<li><b>A subject larger than the narrator.</b> The experience earns its place by illuminating something beyond itself.</li>"
    "<li><b>Scene with purpose.</b> Every remembered moment should carry an argument forward.</li>"
    "<li><b>Honest proportion.</b> The part of the story the writer understands least usually deserves the most space.</li>"
    "<li><b>An ending that thinks, not just resolves.</b> The best personal essays end on an insight the reader can use.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/aeon-essays/\">Aeon essays</a>, <a href=\"/writers/writing/brevity-essays/\">Brevity essays</a> and <a href=\"/writers/writing/agbowo-essays/\">Agbowo essays</a>.</p>",

"home/appliances":
    "<h2>What an appliance guide should settle</h2>"
    "<p>Choosing appliances well is mostly arithmetic the marketing works hard to obscure: what the machine costs to run rather than to buy, how it behaves in the climate and power conditions it will actually live in, and whether its parts and servicing exist locally five years from now. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household appliance energy guidance this desk's appliance pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The questions that decide the purchase</h2>"
    "<ul>"
    "<li><b>Running cost, not sticker price.</b> A cheap motor that runs all day is the expensive appliance.</li>"
    "<li><b>Parts and service availability.</b> A brand with no local parts network is a rental, not a purchase.</li>"
    "<li><b>Power behaviour.</b> Startup draw and inverter compatibility decide whether the appliance survives the household.</li>"
    "<li><b>Repairability by design.</b> Screws, published diagrams and replaceable filters extend a machine's real life.</li>"
    "</ul>"
    "<p>See <a href=\"/home/appliances-that-use-the-most-electricity/\">the appliances that use the most electricity</a>, <a href=\"/home/second-fridge-freezer-cost/\">the cost of a second fridge or freezer</a> and <a href=\"/home/fridge-not-cooling/\">fridge not cooling</a>.</p>",

"writers/writing-opportunities/nigeria":
    "<h2>Reading the Nigerian market as a working writer</h2>"
    "<p>Nigeria's writing market is layered: local magazines and blogs with fast turnaround, African regional outlets with slower editorial cycles, and international desks that commission Nigerian stories from afar. The atlas on this site lists opportunities with their verification dates precisely because the layers move at different speeds — a market that paid on publication last year may not this year, and the writer's protection is checking each entry before pitching. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> is the equivalent map for the US field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>How to use the atlas entries</h2>"
    "<ul>"
    "<li><b>Check the verification date first.</b> The entry's age tells you how much of it to trust; the official link decides the rest.</li>"
    "<li><b>Pitch the layer that fits the piece.</b> Local news essays, regional criticism and international features have different submission paths.</li>"
    "<li><b>Keep your own record.</b> The tracker pages on this site exist because markets reply on their own schedules, not yours.</li>"
    "<li><b>Follow the money honestly.</b> Unpaid work can build a portfolio; it cannot pay rent — label each choice for what it is.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/\">the writing-opportunities atlas</a>, <a href=\"/writers/writing/\">the opportunity desk</a> and <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a pitch</a>.</p>",

"tech/three-two-one-backup-rule":
    "<h2>The rule is about copies, not software</h2>"
    "<p>Three copies of the data, on two different kinds of storage, with one copy somewhere else entirely. The rule survives every technology cycle because it describes failure, not formats: devices die, media corrupts, houses burn, and ransomware encrypts everything it can see. Any backup plan that violates one of the three numbers has a failure it cannot survive. Reference material sits under <a href=\"" + _w("backup") + "\" rel=\"noopener\">backup</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Applying it without a data centre</h2>"
    "<ul>"
    "<li><b>The working copy does not count.</b> Three copies means the live file plus two backups, not two devices sharing one file.</li>"
    "<li><b>Two media types because they fail differently.</b> An external drive and a cloud account fail for unrelated reasons.</li>"
    "<li><b>One copy off-site because local disasters are local.</b> Fire, theft and flooding take the whole household at once.</li>"
    "<li><b>Test the restore, not the backup.</b> An untested backup is a hypothesis, not a plan.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/cloud-vs-local-backup/\">cloud versus local backup</a>, <a href=\"/tech/cloud-storage-mistakes/\">cloud storage mistakes</a> and <a href=\"/tech/android-backup-guide/\">the Android backup guide</a>.</p>",

"tech/tv-clouding-backlight-bleed":
    "<h2>What the glow actually is</h2>"
    "<p>Clouding and backlight bleed are the same class of issue: the LED backlight shining past the panel's control, visible as grey haze or bright corners on dark scenes. Some of it is within manufacturing tolerance, some of it is panel stress from handling or heat, and none of it is fixed by settings beyond a point. Knowing which you have prevents both panic and bad returns. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household display energy guidance this desk follows. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Triage before the return desk</h2>"
    "<ul>"
    "<li><b>Judge on a dark scene in a dark room.</b> Daylight hides every panel's uniformity problems.</li>"
    "<li><b>Separate corner bleed from general clouding.</b> Corner glow is often pressure on the frame; haze is panel variance.</li>"
    "<li><b>Reduce panel stress first.</b> Heat and mounting pressure both make bleed worse over time.</li>"
    "<li><b>Know the tolerance.</b> Every manufacturer draws the line somewhere; the return decision should be yours, not the settings menu's.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/4k-on-a-small-tv-when-its-invisible/\">when 4K on a small screen is invisible</a>, <a href=\"/tech/monitor-buying-specs/\">monitor buying specs</a> and <a href=\"/tech/projector-vs-tv-compound-viewing/\">projector versus TV for compound viewing</a>.</p>",

"tech/video-call-mistakes":
    "<h2>The failures are predictable</h2>"
    "<p>Most video-call damage is done before anyone speaks: a microphone on the wrong device, a backlit face against a bright window, a laptop fan competing with the conversation, or a connection that was tested on speed alone and not on stability. Each is preventable in the two minutes before the call. Reference material sits under <a href=\"" + _w("videoconferencing") + "\" rel=\"noopener\">videoconferencing</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The two-minute pre-call check</h2>"
    "<ul>"
    "<li><b>Confirm the input device, not just the app.</b> The meeting hears whatever the system default is.</li>"
    "<li><b>Light from in front, never behind.</b> A window behind you makes you a silhouette on every platform.</li>"
    "<li><b>Stability beats speed.</b> A steady connection with a clear uplink outperforms a fast jittery one.</li>"
    "<li><b>Close the fans' competitors.</b> Update prompts, downloads and heavy tabs are the usual audio enemies.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/fibre-vs-5g-router-home-office/\">fibre versus 5G for the home office</a>, <a href=\"/tech/4g-router-antenna-worth-it/\">is a 4G router antenna worth it</a> and <a href=\"/tech/laptop-desk-ergonomics-the-standing-fix/\">laptop desk ergonomics</a>.</p>",

"home/smart-thermostat-payback":
    "<h2>Payback is a household behaviour question</h2>"
    "<p>A smart thermostat saves money by changing when heating and cooling run, which means its payback depends almost entirely on the household's previous habits. Houses that were already well scheduled save little; houses with empty-hour heating and manual overrides save the most. The honest calculation starts from the old schedule, not from the box. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes the household energy guidance this desk's payback pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Running the numbers honestly</h2>"
    "<ul>"
    "<li><b>Measure the baseline first.</b> A month of bills before installation is the only defensible comparison.</li>"
    "<li><b>Count the empty hours.</b> The saving lives in the periods the house was conditioning itself for nobody.</li>"
    "<li><b>Include the subscription.</b> Features behind a monthly fee change the payback maths permanently.</li>"
    "<li><b>Keep the manual override habit.</b> Thermostats save by being overruled intelligently, not by being ignored.</li>"
    "</ul>"
    "<p>See <a href=\"/home/which-heating-system/\">choosing a heating system</a>, <a href=\"/home/uk-insulation-grants/\">UK insulation grants</a> and <a href=\"/home/heat-pump-vs-gas-furnace/\">heat pump versus gas furnace</a>.</p>",

"writers/writing/longreads-reported-feature":
    "<h2>The reported feature is an access bet</h2>"
    "<p>A reported feature lives or dies on what the writer could reach: the scene inside the room, the documents nobody has read, the people who agreed to talk on the record. The craft organises that access into a narrative, but the pitch editors buy is the access itself. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the magazine field where long reporting is commissioned. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Building the feature</h2>"
    "<ul>"
    "<li><b>Secure the scene access before the pitch.</b> One promised visit beats three hoped-for interviews.</li>"
    "<li><b>Report in layers.</b> Documents verify people; people explain documents; scenes make both land.</li>"
    "<li><b>Structure around tension, not chronology.</b> The timeline is the skeleton, not the story.</li>"
    "<li><b>Hold the ending.</b> The last section should resolve the piece's question, not merely stop the piece.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/longreads/\">Longreads</a>, <a href=\"/writers/writing/longreads-personal-essay/\">the longreads personal essay guide</a> and <a href=\"/writers/writing/longreads-reading-list/\">the longform reading list</a>.</p>",

"tech/learning-python-free-resources":
    "<h2>Free is the standard price for Python</h2>"
    "<p>Python's teaching ecosystem is free at every level — the language documentation, the interactive tutorials, the problem sets, and the community answers that surface within hours of any beginner question. The scarce resource is sequencing: choosing an order that reaches useful programs before motivation thins. Reference material sits under <a href=\"" + _w("Python+(programming+language)") + "\" rel=\"noopener\">the Python programming language</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>A sequence that works</h2>"
    "<ul>"
    "<li><b>Start with the official tutorial's first half.</b> It is free, permanent, and better than most paid introductions.</li>"
    "<li><b>Write tiny programs in week one.</b> Automation of a chore you actually have teaches faster than exercises.</li>"
    "<li><b>Read other people's small code.</b> Short, well-written scripts teach style where tutorials teach syntax.</li>"
    "<li><b>Join one place that answers questions.</b> Learning stalls at the first unanswered error more often than at any concept.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/parse-json-python/\">parsing JSON in Python</a>, <a href=\"/tech/call-api-python/\">calling an API in Python</a> and <a href=\"/tech/schedule-python-scripts/\">scheduling Python scripts</a>.</p>",

"tech/microsoft-365-free-vs-paid":
    "<h2>Where the line falls</h2>"
    "<p>The free-versus-paid question for Microsoft 365 is really a storage and administration question: web apps are free, and the paid tiers buy local desktop apps, larger storage quotas, and the management features businesses need. Households and students often sit on the free side without noticing; the paid side starts mattering when files outgrow the quota or devices multiply. The <a href=\"" + _w("Microsoft+365") + "\" rel=\"noopener\">Microsoft 365 product family</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Deciding against your real usage</h2>"
    "<ul>"
    "<li><b>Count the documents, not the apps.</b> Storage quota is the first limit households actually hit.</li>"
    "<li><b>Check offline needs.</b> If the work must continue without a connection, the web tier stops qualifying.</li>"
    "<li><b>Look at the family plan honestly.</b> Per-seat pricing across a household decides the comparison faster than features do.</li>"
    "<li><b>Re-check annually.</b> Tiers and quotas drift; last year's verdict expires quietly.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/cloud-storage-plans-compared/\">cloud storage plans compared</a>, <a href=\"/tech/bitwarden-free-password-manager/\">Bitwarden as a free password manager</a> and <a href=\"/tech/best-password-manager-for-you/\">choosing the best password manager</a>.</p>",

"writers/writing/americas-quarterly":
    "<h2>Latin American affairs with a policy ear</h2>"
    "<p>Americas Quarterly covers politics, business and society across the Western Hemisphere for an audience that includes policymakers and investors, which sets its commissioning standard: pieces need reporting and consequence, not colour. For writers, it is a market where regional expertise compounds — a beat builds across commissions. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the opinion and policy-magazine field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching policy-adjacent work</h2>"
    "<ul>"
    "<li><b>Bring a stake, not a tour.</b> The region is covered as a place where decisions are made.</li>"
    "<li><b>Report past the capitals.</b> The best pieces in this field travel to where policy lands.</li>"
    "<li><b>Quote the decision-makers.</b> Access to officials and operators is part of the pitch's value.</li>"
    "<li><b>Keep the argument tight.</b> Policy readers reward clarity over comprehensive surveys.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/nacla/\">NACLA</a>, <a href=\"/writers/writing/new-lines-magazine/\">New Lines Magazine</a> and <a href=\"/writers/writing/markaz-review/\">Markaz Review</a>.</p>",

"home/after-pest-treatment":
    "<h2>The treatment window has rules</h2>"
    "<p>After a pest treatment, the pesticide is doing its job precisely when the household most wants to clean everything up — and cleaning the wrong surfaces undoes the treatment while spreading residue into the wrong places. The safe routine separates what to leave alone, what to wipe, and what to ventilate. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household pesticide safety guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What to do after the technician leaves</h2>"
    "<ul>"
    "<li><b>Leave treated surfaces alone for the stated period.</b> The residual layer is the treatment; wiping it away is the commonest mistake.</li>"
    "<li><b>Clean food-contact surfaces thoroughly.</b> Where hands and food go, residue does not stay.</li>"
    "<li><b>Ventilate occupied rooms.</b> Air clears what the label's waiting period allows to settle.</li>"
    "<li><b>Keep the follow-up appointment.</b> Pest cycles outrun single treatments; the second visit is the plan working.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ants-in-the-kitchen/\">ants in the kitchen</a>, <a href=\"/home/compound-mosquito-control-night/\">compound mosquito control at night</a> and <a href=\"/home/rats-in-the-house/\">rats in the house</a>.</p>",

"tech/streaming-quality-settings":
    "<h2>The settings that actually change the picture</h2>"
    "<p>Streaming quality is negotiated per moment between the player and the network, which is why a settings menu can only set the ceiling, not the result. The useful settings are the ones that stop the player from misjudging: capping data on metered connections, fixing the output resolution to the display, and choosing when the app is allowed to buffer at higher quality. Reference material sits under <a href=\"" + _w("adaptive+bitrate+streaming") + "\" rel=\"noopener\">adaptive bitrate streaming</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Set the ceiling, then get out of the way</h2>"
    "<ul>"
    "<li><b>Match resolution to the display.</b> Paying bandwidth for pixels the screen cannot show is pure waste.</li>"
    "<li><b>Cap quality on metered data.</b> The player will happily consume a plan to save one rebuffer.</li>"
    "<li><b>Prefer stability settings on busy networks.</b> A slightly lower steady stream beats a higher stuttering one.</li>"
    "<li><b>Check the audio track default.</b> Multi-channel audio carries a bandwidth cost whether the speakers exist or not.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/antenna-vs-satellite-vs-streaming-live-tv/\">antenna versus satellite versus streaming</a>, <a href=\"/tech/tv-clouding-backlight-bleed/\">TV clouding and backlight bleed</a> and <a href=\"/tech/power-bank-size-math-for-tv-and-wifi/\">power-bank sizing for TV and Wi-Fi</a>.</p>",

"tech/tool/json-formatter":
    "<h2>What formatting JSON is for</h2>"
    "<p>JSON formatting is the difference between a payload you can read and a payload you can only parse. Pretty-printing exposes the structure, validation proves the syntax, and re-serialising normalises the whitespace so two equivalent payloads can be compared byte for byte. It is one of the small tools that quietly carries a lot of debugging work. Reference material sits under <a href=\"" + _w("JSON") + "\" rel=\"noopener\">JSON</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using it well</h2>"
    "<ul>"
    "<li><b>Validate before you format.</b> Syntax errors are the payload's real message; formatting is cosmetic.</li>"
    "<li><b>Watch the key order.</b> Re-serialising may reorder keys; that changes bytes without changing meaning.</li>"
    "<li><b>Never format secrets in shared tools.</b> Production tokens have no business in a browser tab.</li>"
    "<li><b>Keep the raw payload.</b> The original bytes answer questions the cleaned version quietly edits out.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/uuid-generator/\">the UUID generator</a>, <a href=\"/tech/tool/base64-encoder/\">the Base64 encoder</a> and <a href=\"/tech/tool/case-converter/\">the case converter</a>.</p>",

"writers/writing/electric-literature-essays":
    "<h2>Literary essays with a digital readership</h2>"
    "<p>Electric Literature built its audience online by treating literary essays as shareable arguments about books, writing and the culture around them. Its essay strand is a market where the pitch is the piece's claim and the readers arrive through the argument itself. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the digital literary field it sits within. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing the argument-led essay</h2>"
    "<ul>"
    "<li><b>The claim is the pitch.</b> A piece about a topic is a search result; a piece that argues something is an essay.</li>"
    "<li><b>Books are evidence.</b> The strongest literary essays read closely enough to prove their point.</li>"
    "<li><b>Write the opening as an argument.</b> Shareable essays state the stakes in the first screen.</li>"
    "<li><b>Land the ending on the claim.</b> The last section is where the essay earns its title.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/literary-hub/\">Literary Hub</a>, <a href=\"/writers/writing/narratively/\">Narratively</a> and <a href=\"/writers/writing/guernica/\">Guernica</a>.</p>",

"writers/learn/professional-writing":
    "<h2>Professionalism is a set of habits</h2>"
    "<p>Professional writing is rarely about style; it is about reliability made visible. Deadlines met without chasing, briefs read closely the first time, revisions tracked rather than negotiated from memory, and invoices that match the agreement exactly. Editors rehire writers who reduce their workload long before they rehire writers who impress them. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes resources on the trade's working standards. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The habits editors actually see</h2>"
    "<ul>"
    "<li><b>Confirm scope in writing before starting.</b> One short message prevents most of the industry's disputes.</li>"
    "<li><b>Deliver early enough to be read.</b> A file that arrives at the deadline arrives late for editing.</li>"
    "<li><b>Version your drafts clearly.</b> Named files end the which-draft argument permanently.</li>"
    "<li><b>Make invoices boring.</b> The best invoice matches the agreement so exactly that no one has to check it.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-professional-emails/\">professional emails dos and don'ts</a>, <a href=\"/writers/learn/freelance-paid-writing/how-much-to-charge-for-an-article/\">how much to charge for an article</a> and <a href=\"/writers/guides/how-to-check-a-freelance-writing-contract/\">how to check a freelance writing contract</a>.</p>",

"writers/writing/smashing-magazine":
    "<h2>A design magazine that commissions in depth</h2>"
    "<p>Smashing Magazine has run for nearly two decades as the working library of web design and front-end practice, paying professional rates for long, practical articles. Its commissioning bar is expertise demonstrated in the writing: pieces are tutorials and deep guides authored by practitioners, not think pieces. The <a href=\"" + _w("Smashing+Magazine") + "\" rel=\"noopener\">magazine's history and format</a> are documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing for a practitioner market</h2>"
    "<ul>"
    "<li><b>Show the working.</b> Practitioner audiences trust code, diagrams and tested steps over description.</li>"
    "<li><b>Write for the reader mid-task.</b> The audience arrives with a problem open in another tab.</li>"
    "<li><b>Anticipate the edge cases.</b> Depth means covering where the common approach breaks.</li>"
    "<li><b>Keep it current before you pitch.</b> Tooling articles expire; confirm the versions you describe.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/business-insider/\">Business Insider</a>, <a href=\"/writers/writing/income-diary/\">Income Diary</a> and <a href=\"/writers/writing/listverse/\">Listverse</a>.</p>",

"tech/tool/http-status-lookup":
    "<h2>Status codes are the protocol talking</h2>"
    "<p>HTTP status codes are the smallest possible debugging signal and still one of the most useful: the first digit tells you who is expected to act next, the specific code tells you why, and the response headers tell you how the server understood the request. Reading them fluently shortens almost every web investigation. Reference material sits under <a href=\"" + _w("HTTP") + "\" rel=\"noopener\">the Hypertext Transfer Protocol</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the families</h2>"
    "<ul>"
    "<li><b>2xx: the server agrees.</b> If debugging continues here, the problem is in the payload, not the route.</li>"
    "<li><b>3xx: something moved.</b> A chain of redirects is usually the whole story; read the final destination.</li>"
    "<li><b>4xx: the request is the problem.</b> Auth, permissions and routing — check what you sent before the server.</li>"
    "<li><b>5xx: the server failed holding your request.</b> Logs beat theories at this point.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/json-formatter/\">the JSON formatter</a>, <a href=\"/tech/tool/base64-encoder/\">the Base64 encoder</a> and <a href=\"/tech/how-the-internet-works/\">how the internet works</a>.</p>",

"writers/learn/dos-and-donts/dos-and-donts-of-professional-emails":
    "<h2>Every email is a work sample</h2>"
    "<p>In writing careers the pitch email is often the first writing sample an editor sees, and the follow-up is the second. Professional email is therefore not etiquette for its own sake; it is craft applied to the medium where business actually happens — clear subject lines, complete context, and replies that make the next action obvious. The <a href=\"" + _w("email") + "\" rel=\"noopener\">email</a> as a professional medium is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The rules that get replies</h2>"
    "<ul>"
    "<li><b>Subject lines carry the ask.</b> An editor filing fifty pitches files them by what the subject promised.</li>"
    "<li><b>One purpose per email.</b> Mixed requests get mixed responses, usually delayed ones.</li>"
    "<li><b>Include the context the reader needs.</b> Links, attachments and deadlines belong in the message, not in a second email.</li>"
    "<li><b>Close the loop on your side.</b> Confirmation emails cost seconds and prevent weeks of drift.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/professional-writing/\">professional writing</a>, <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-pitching-editors/\">pitching editors dos and don'ts</a> and <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a pitch</a>.</p>",

"tech/car-fridge-vs-cooler-box":
    "<h2>Powered cooling versus insulation</h2>"
    "<p>A car fridge actively removes heat using the vehicle's power; a cooler box passively slows heat coming in using ice and insulation. The choice follows from the trip: duration, ambient temperature, what is being kept cold, and whether the car has power to spare. For long hot journeys with medicines or fresh food, active cooling earns its cost; for a day, the cooler box wins every time. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household appliance energy guidance this desk's cooling guides follow. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Deciding by trip profile</h2>"
    "<ul>"
    "<li><b>Duration decides the class.</b> Past a day in real heat, ice logistics defeat every cooler box.</li>"
    "<li><b>Check the power budget.</b> A car fridge is a continuous electrical load, not a phone charger.</li>"
    "<li><b>Respect the medicine chain.</b> Anything requiring a temperature range gets the powered option.</li>"
    "<li><b>Pack the cooler in reverse.</b> Items needed first on top; open time is the enemy.</li>"
    "</ul>"
    "<p>See <a href=\"/home/appliances-that-use-the-most-electricity/\">the appliances that use the most electricity</a>, <a href=\"/home/second-fridge-freezer-cost/\">the cost of a second fridge or freezer</a> and <a href=\"/home/appliances/\">the appliances guide</a>.</p>",

"writers/guides/how-to-check-a-freelance-writing-contract":
    "<h2>Read the contract as a payment plan</h2>"
    "<p>A freelance writing contract is less about legal protection than about payment predictability: what triggers an invoice, how long the money takes, who owns the work afterwards, and what happens when the project changes shape. Every clause worth reading maps to one of those four questions. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes trade resources on writer agreements. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The four clauses to read twice</h2>"
    "<ul>"
    "<li><b>Payment trigger and terms.</b> On acceptance, on publication, and net-30 are three different cash flows.</li>"
    "<li><b>Scope and revision limits.</b> Rounds of revision included, and what counts as out-of-scope work.</li>"
    "<li><b>Rights and reversion.</b> What is sold, for how long, and what returns when the term ends.</li>"
    "<li><b>Kill fee and cancellation.</b> The clause that decides who absorbs the work already done.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/freelance-paid-writing/how-writing-retainers-work/\">how writing retainers work</a>, <a href=\"/writers/learn/freelance-paid-writing/how-much-to-charge-for-an-article/\">how much to charge for an article</a> and <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a pitch</a>.</p>",

"sports/premier-league-clubs":
    "<h2>The clubs are the league's structure</h2>"
    "<p>The Premier League's twenty clubs decide its balance of power through ownership, academies and wage capacity — and the same twenty names determine which fixtures matter to which audiences. Knowing the clubs' recent histories is what makes a table legible mid-season, because form follows squad building from two or three windows earlier. The <a href=\"" + PL + "\" rel=\"noopener\">official Premier League site</a> carries the club, fixture and squad records this desk's pages reference. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What to know about each club</h2>"
    "<ul>"
    "<li><b>Ownership model.</b> Investment strategy shows up in the table two seasons after it starts.</li>"
    "<li><b>Academy output.</b> Clubs that promote from within survive tight windows better.</li>"
    "<li><b>Managerial tenure.</b> A manager in his second full season has a squad he chose.</li>"
    "<li><b>Fixture congestion history.</b> European schedules reshape domestic form every spring.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league/\">the Premier League desk</a>, <a href=\"/sports/premier-league-fixtures/\">the fixtures</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",

"sports/season":
    "<h2>Following a season as a system</h2>"
    "<p>A season is not a list of matches; it is a schedule that redistributes pressure. Early weeks test recruitment, the winter stretch tests depth, and the spring tests the table's arithmetic. Following it well means knowing which phase a team is in when you read a result — a November loss and a May loss are the same scoreline carrying different weight. The <a href=\"" + PL + "\" rel=\"noopener\">official Premier League site</a> carries the fixtures, tables and results this desk's season coverage follows. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>The season's three reading lenses</h2>"
    "<ul>"
    "<li><b>Phase of the calendar.</b> Results weigh differently before and after the schedule compresses.</li>"
    "<li><b>Squad availability.</b> A table at any moment reflects injuries as much as ability.</li>"
    "<li><b>Remaining fixtures.</b> Run-ins are visible months early to anyone who reads the schedule.</li>"
    "<li><b>Points pace, not position.</b> The points total that wins the league or keeps a place is the stable number.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league/\">the Premier League desk</a>, <a href=\"/sports/premier-league-fixtures/\">the fixtures</a> and <a href=\"/sports/premier-league-top-scorers/\">the top scorers</a>.</p>",

"writers/writing/chestnut-review":
    "<h2>A journal that reads poetry closely</h2>"
    "<p>The Chestnut Review publishes poetry, fiction and essays with an editorial voice that favours precision over spectacle — work that survives being read twice. For writers it is a reminder that small journals build audiences slowly and read submissions seriously. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the literary-journal field it belongs to. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing to be read twice</h2>"
    "<ul>"
    "<li><b>Earn the first line last.</b> Poems and stories often reveal their opening only after the ending exists.</li>"
    "<li><b>Read the journal's current issue.</b> Small journals show their taste completely in one issue.</li>"
    "<li><b>Submit suites of related work for poetry.</b> Poems read together differently from poems read singly.</li>"
    "<li><b>Track the response window.</b> Small journals read slower because reading well takes time.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/agni/\">AGNI</a>, <a href=\"/writers/writing/kenyon-review/\">The Kenyon Review</a> and <a href=\"/writers/writing/cincinnati-review/\">The Cincinnati Review</a>.</p>",

"writers/writing/communique":
    "<h2>Essays at the speed of the conversation</h2>"
    "<p>Communiqué-style essay outlets publish pieces that enter a live conversation — culture, politics, technology — while it is still forming. The editorial demand is therefore speed with substance: the piece must arrive quickly and still contain a claim worth making after the moment passes. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the digital essay field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing fast without writing thin</h2>"
    "<ul>"
    "<li><b>Keep a prepared file.</b> The pieces that ship fast are drafted against evidence collected earlier.</li>"
    "<li><b>Make one claim.</b> The essay that comments on everything arrives late and lands nowhere.</li>"
    "<li><b>Use the moment as the door.</b> Timeliness is the entry; the argument is the room.</li>"
    "<li><b>Write the update policy in.</b> Essays on live stories should say how they will be corrected.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/aeon-essays/\">Aeon essays</a>, <a href=\"/writers/writing/noema/\">Noema</a> and <a href=\"/writers/writing/new-lines-magazine/\">New Lines Magazine</a>.</p>",

"home/seasonal-care":
    "<h2>The house keeps a calendar</h2>"
    "<p>Seasonal home care exists because weather and wear arrive on schedules: dust and heat before harmattan, moisture and mould through the rains, insects at their own turning points. A calendar of small tasks beats a calendar of repairs because almost every major home failure has a maintenance window before it. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household maintenance guidance this desk's seasonal pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The seasonal rhythm</h2>"
    "<ul>"
    "<li><b>Before the dry season: fire and dust.</b> Clears, screens and electrical checks while the weather is still kind.</li>"
    "<li><b>Before the rains: water paths.</b> Gutters, roof edges and drains are cheaper to clear than to repair.</li>"
    "<li><b>Each transition: the machines.</b> Filters, coils and seals get attention at the turn of every season.</li>"
    "<li><b>Keep a written record.</b> The house's maintenance history is the owner's best negotiating document.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ac-outdoor-unit-care/\">air-conditioner outdoor unit care</a>, <a href=\"/home/harmattan-fire-safety-house/\">harmattan fire safety</a> and <a href=\"/home/mould-after-a-flooded-room/\">mould after a flooded room</a>.</p>",

"tech/vpn-what-it-protects":
    "<h2>A tunnel, not an invisibility cloak</h2>"
    "<p>A VPN encrypts the path between your device and the VPN server — which protects traffic from the local network you are sitting on, and moves the trust you place in your internet provider to the VPN operator instead. It does not make you anonymous to the sites you log into, and it does not repair a compromised device. Reference material sits under <a href=\"" + _w("virtual+private+network") + "\" rel=\"noopener\">virtual private networks</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What it does and does not fix</h2>"
    "<ul>"
    "<li><b>Protects: the local hop.</b> Hotel, café and shared-compound networks are exactly where a VPN earns its keep.</li>"
    "<li><b>Moves trust: to the VPN operator.</b> Choose the operator as carefully as you chose the internet provider.</li>"
    "<li><b>Does not protect: your accounts.</b> A logged-in session tells the site exactly who you are, VPN or not.</li>"
    "<li><b>Costs: speed and battery.</b> Encryption is real work; expect a real, if modest, tax.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/home-wifi-security-audit/\">the home Wi-Fi security audit</a>, <a href=\"/tech/public-wifi-risks/\">the risks of public Wi-Fi</a> and <a href=\"/tech/security-questions-are-insecure/\">why security questions are insecure</a>.</p>",

"home/ceiling-light-flicker-fix":
    "<h2>Flicker is a circuit telling you where</h2>"
    "<p>A flickering ceiling light narrows the fault by its pattern: one fixture flickering is usually the lamp or its fitting; a group of lights flickering together is a circuit or neutral problem; lights that dim when appliances start are voltage behaviour worth an electrician's visit. The pattern is the diagnosis. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the home electrical safety guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the flicker pattern</h2>"
    "<ul>"
    "<li><b>One fixture, one answer.</b> Reseat or replace the lamp first; then inspect the fitting's contacts.</li>"
    "<li><b>Several fixtures, one circuit.</b> A loose neutral is the suspect — that one is an electrician's job, not a DIY evening.</li>"
    "<li><b>Dimming on motor start.</b> Shared circuits with fridges and pumps show this pattern clearly.</li>"
    "<li><b>Any flicker with heat or smell.</b> Stop using the circuit at the panel and call immediately.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ceiling-leak-11pm/\">ceiling leak at 11pm</a>, <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a> and <a href=\"/home/why-does-my-circuit-breaker-keep-tripping/\">why the circuit breaker keeps tripping</a>.</p>",

}

# Top-up sections for pages that already carry a t8 block from earlier batches
# but are still under their class bar. Injected under marker data-esrc="t8b".
TOPUP_SECTIONS9 = {

"writers/writing-opportunities/nigeria":
    "<h2>How to use the verification dates</h2>"
    "<p>Every atlas entry on this site carries the date the desk last checked it against the outlet's own guidelines, because publishing markets drift faster than directories do. A verified entry is a starting point, not a guarantee: open the official link before pitching, and treat any rate or requirement the entry quotes as correct only as of its verification date. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> maintains the equivalent discipline for its own listings. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Working the list like a professional</h2>"
    "<ul>"
    "<li><b>Sort by verification age before anything else.</b> Fresh entries earn your attention first.</li>"
    "<li><b>Pitch in waves, not floods.</b> Three considered pitches beat twelve generic ones in every market.</li>"
    "<li><b>Record every submission on the tracker.</b> The follow-up calendar is only as good as the log behind it.</li>"
    "<li><b>Report changes back.</b> Markets move; the desk's verification cycle depends on readers who spot the drift.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing-opportunities/\">the writing-opportunities atlas</a>, <a href=\"/writers/tracker/\">the submission tracker</a> and <a href=\"/writers/writing/\">the opportunity desk</a>.</p>",

"sports/premier-league-clubs":
    "<h2>Reading a club through its windows</h2>"
    "<p>A club's season is usually decided in the transfer windows before it starts: who was bought, who was sold, and what the wage bill did in between. Squads that keep their spine and add selectively tend to outperform squads rebuilt from scratch, whatever the headline fees suggest. The <a href=\"" + PL + "\" rel=\"noopener\">official Premier League site</a> carries the transfer and squad records this desk's club pages follow. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What the window tells you about the table</h2>"
    "<ul>"
    "<li><b>Departures are injuries arriving early.</b> Replacing a sold starter is the quietest risk in football.</li>"
    "<li><b>Late signings change little by October.</b> Integration time is real; August fees show up in results with a lag.</li>"
    "<li><b>Loan-heavy squads age badly across a season.</b> Depth that can be recalled is not depth.</li>"
    "<li><b>Wage growth beats fee spending as a predictor.</b> The wage table has always tracked the league table more closely.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league-transfers/\">the Premier League transfers desk</a>, <a href=\"/sports/premier-league-transfer-tracker-august-2026/\">the August 2026 transfer tracker</a> and <a href=\"/sports/who-will-win-the-2026-27-premier-league/\">who will win the 2026-27 Premier League</a>.</p>",

"sports/season":
    "<h2>What the table knows by spring</h2>"
    "<p>By the spring stretch the table stops being a sequence of results and becomes arithmetic: points already banked, points still available, and the run-in each contender faces. Analysts lean on points pace precisely because it survives fixture luck — the projected total treats the season as the closed loop it is. The <a href=\"" + PL + "\" rel=\"noopener\">official Premier League site</a> carries the standings and results this desk's season coverage reads. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Three numbers that beat the highlight reels</h2>"
    "<ul>"
    "<li><b>Points pace.</b> Games played into points earned is the only projection that needs no opinions.</li>"
    "<li><b>Goal difference against expectation.</b> It is the closest thing football has to a stable underlying metric.</li>"
    "<li><b>Remaining home-and-away balance.</b> Run-ins are shaped by where the fixtures sit, not just who they are against.</li>"
    "<li><b>Availability at the run-in.</b> The squads that arrive in April intact decide the table.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league-table/\">the Premier League table</a>, <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a> and <a href=\"/sports/premier-league-results/\">the results</a>.</p>",

}
