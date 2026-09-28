# -*- coding: utf-8 -*-
"""Editorial depth sections, part 8: batch D, the 720-734 word tranche against
the 750-word bar (plus one tool page 25 words under the 669 tool bar).
Writers, tech, home desks. Every external URL curl-verified 200 at authoring
time; every internal link verified to a real page."""

WHO = "https://www.who.int/"
EPA = "https://www.epa.gov/"
GOVUK = "https://www.gov.uk/"
NFPA = "https://www.nfpa.org/"
CLMP = "https://www.clmp.org/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS8 = {

"tech/computer-fans-loud":
    "<h2>Loud fans are a report, not a verdict</h2>"
    "<p>A desktop or all-in-one that suddenly runs loud is telling you about heat before it tells you about hardware. Dust in the intake, a paste layer that has dried out, a case with no clear airflow path, or software holding the processor at full clock will each present as fan noise first. The diagnostic order is the same as for a laptop: air path, then load, then hardware. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the electrical-safety context this desk follows on machines that run hot. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The quiet-down order</h2>"
    "<ul>"
    "<li><b>Feel the exhaust while it screams.</b> Weak exhaust with high fan speed means obstruction, not workload.</li>"
    "<li><b>Read the load before touching hardware.</b> A single runaway process explains most sudden noise.</li>"
    "<li><b>Clear filters and intakes on a schedule.</b> Dust builds silently; the fan is the only alarm.</li>"
    "<li><b>Repaste last, and only with evidence.</b> Temperature logs that show thermal throttling are the permission slip.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-overheating-fan-noise/\">laptop overheating and fan noise</a>, <a href=\"/tech/laptop-fan-loud-dust-vs-fault/\">laptop fan loud: dust versus fault</a> and <a href=\"/tech/phone-overheating-causes-and-fixes/\">phone overheating causes and fixes</a>.</p>",

"tech/deepseek-vs-chatgpt":
    "<h2>Two assistants, one set of questions</h2>"
    "<p>Comparing DeepSeek and ChatGPT is less about which model scores higher on any given day and more about what you are asking it to do: which of them you can run where, what each does with your data, what the access costs, and how each handles the specific mix of reasoning, code and long documents your work actually needs. Reference material on the underlying technology is collected under <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large language models</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The comparison that holds up</h2>"
    "<ul>"
    "<li><b>Test on your own tasks.</b> Leaderboard wins move monthly; your prompt set does not.</li>"
    "<li><b>Check where the processing happens.</b> Self-hostable weights and cloud-only APIs are different products.</li>"
    "<li><b>Read the data settings first.</b> Work conversations decide the choice before model quality does.</li>"
    "<li><b>Watch the length behaviour.</b> Long-document handling separates assistants faster than short prompts do.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/ai-assistant-data-training-settings/\">AI assistant data and training settings</a>, <a href=\"/writers/compare/chatgpt-alternatives-for-writers/\">ChatGPT alternatives for writers</a> and <a href=\"/writers/learn/freelance-paid-writing/choosing-ai-writing-tools/\">choosing AI writing tools</a>.</p>",

"home/gas-cylinder-safety":
    "<h2>The cylinder is a pressure vessel, not furniture</h2>"
    "<p>A cooking gas cylinder stores a fuel that wants to be vapour, and nearly every domestic incident traces back to three habits: storing it where heat gathers, moving it while connected, or testing for leaks with a flame. The safe routine is short enough to memorise and boring enough to trust. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the fuel-handling safety context this desk's cylinder guides follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The routine that prevents the incident</h2>"
    "<ul>"
    "<li><b>Store it upright, outside, in shade.</b> Vapour pressure rises with temperature; the valve is designed for the upright position.</li>"
    "<li><b>Change cylinders with the regulator off and the area aired.</b> The changeover moment is the exposure window.</li>"
    "<li><b>Test leaks with soapy water, never a flame.</b> Bubbles answer the question safely.</li>"
    "<li><b>Retire the hose on time.</b> LPG hoses have service lives; a cracked hose is a slow release.</li>"
    "</ul>"
    "<p>See <a href=\"/home/gas-cylinder-change-safely/\">how to change a gas cylinder safely</a>, <a href=\"/home/gas-cooker-wont-ignite/\">gas cooker will not ignite</a> and <a href=\"/home/gas-heaters-damp/\">gas heaters and damp</a>.</p>",

"tech/external-drive-not-showing-up":
    "<h2>The drive is probably fine</h2>"
    "<p>When an external drive does not appear, the failure is usually in the path between the drive and the system rather than in the drive itself: a cable that carries power but not data, a port that cannot supply the current, a drive letter or mount point that was never assigned, or a disk that initialised on a different operating system. Work through the path before assuming data loss. Reference material on recovery practice sits under <a href=\"" + _w("data+recovery") + "\" rel=\"noopener\">data recovery</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The order that avoids damage</h2>"
    "<ul>"
    "<li><b>Change one thing at a time: cable, port, then machine.</b> A second computer answers most questions immediately.</li>"
    "<li><b>Look in the disk tool, not just the file manager.</b> An unassigned letter or unmounted volume looks identical to a dead drive.</li>"
    "<li><b>Never initialise to make it appear.</b> Initializing writes; writes are what destroy recoverable data.</li>"
    "<li><b>If the data matters, stop and image it.</b> Clone first, recover from the clone.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/cloud-vs-local-backup/\">cloud versus local backup</a>, <a href=\"/tech/cloud-storage-mistakes/\">cloud storage mistakes</a> and <a href=\"/tech/data-shuttle-sd-usb-ssd/\">moving data between SD, USB and SSD</a>.</p>",

"tech/website-wont-deploy-fix":
    "<h2>Deploys fail in layers</h2>"
    "<p>A deploy that will not ship is debugging in public, and the layers are consistent: the build step, the environment it runs in, the artifact it produces, and the routing that serves it. Nearly every stubborn deploy failure is a difference between the machine that built the artifact and the machine that serves it — a missing environment variable, a version mismatch, or a cache holding the previous output. The practice is summarised in reference works on <a href=\"" + _w("continuous+deployment") + "\" rel=\"noopener\">continuous deployment</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Read the failure from the outside in</h2>"
    "<ul>"
    "<li><b>Confirm the build ran the commit you pushed.</b> The wrong commit explains more failures than the wrong code does.</li>"
    "<li><b>Diff the environment, not the code.</b> Variables and versions are the usual silent differences.</li>"
    "<li><b>Check the artifact before the server.</b> If the output is wrong locally, the host is innocent.</li>"
    "<li><b>Clear caches last.</b> Cached output survives redeploys and is the classic stale-site cause.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/firebase-deployment-failing/\">Firebase deployment failing</a>, <a href=\"/tech/render-deployment-failures-what-they-taught-me/\">what Render deployment failures taught us</a> and <a href=\"/tech/deploy-python-app/\">deploying a Python app</a>.</p>",

"writers/writing/strange-horizons-fiction":
    "<h2>A speculative market with a clear shape</h2>"
    "<p>Strange Horizons publishes speculative fiction, poetry and essays on a weekly schedule, funded by its readers rather than by a media group, and its submission system has always been part of its identity — open windows, published response times, and a slush process writers can actually follow. For a speculative writer it is one of the first professional stops. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> maps the field it sits within. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting to a window-based market</h2>"
    "<ul>"
    "<li><b>Write to the window, not against it.</b> Closed periods are planning time, not lost time.</li>"
    "<li><b>Read the recent fiction, not the archive.</b> A weekly market's taste is visible in the last month.</li>"
    "<li><b>Follow the stated wait before querying.</b> Speculative markets publish their timelines precisely so writers can calibrate.</li>"
    "<li><b>One story at a time per market.</b> Simultaneous submissions are usually welcome; duplicate ones never are.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/clarkesworld-fiction/\">Clarkesworld fiction</a>, <a href=\"/writers/writing/asimovs-fiction/\">Asimov's fiction</a> and <a href=\"/writers/writing/beneath-ceaseless-skies/\">Beneath Ceaseless Skies</a>.</p>",

"home/borehole-water-taste-smell":
    "<h2>Taste and smell are screening tests</h2>"
    "<p>Water that tastes of metal, smells of eggs, or turns a kettle white is reporting its mineral and bacterial contents in the only language it has. Some of what it reports is harmless and cosmetic; some of it is not. The safe order is to identify the source before treating anything: the borehole, the storage tank, or the plumbing between them each leave a different signature. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the drinking-water quality context this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the signatures</h2>"
    "<ul>"
    "<li><b>Metallic taste with red staining.</b> Iron is the usual answer; it is unpleasant long before it is unsafe.</li>"
    "<li><b>Rotten-egg smell at the tap but not at the source.</b> That pattern points at the water heater or the plumbing, not the aquifer.</li>"
    "<li><b>White scale in the kettle.</b> Hardness; treatable, and worth testing before choosing a softener.</li>"
    "<li><b>Any sudden change.</b> A change is the signal to test the water, not to mask the taste.</li>"
    "</ul>"
    "<p>See <a href=\"/home/borehole-water-and-your-kettle/\">borehole water and your kettle</a>, <a href=\"/home/borehole-pump-no-water/\">borehole pump running with no water</a> and <a href=\"/home/best-water-softener-for-your-home/\">choosing a water softener</a>.</p>",

"tech/monitor-buying-specs":
    "<h2>Three numbers decide the monitor</h2>"
    "<p>Monitor marketing runs on dozens of specifications, but the purchase usually settles on three: the panel type, which decides how the picture behaves off-axis; the resolution against the screen size, which decides whether pixels are visible at your sitting distance; and the brightness and reflection handling, which decides whether the screen survives your actual room. Everything else refines a choice those three already made. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes the household energy guidance this desk follows on always-on display gear. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Buy for the room and the desk</h2>"
    "<ul>"
    "<li><b>Match resolution to size first.</b> High resolution on a small panel buys eye strain, not detail.</li>"
    "<li><b>Check the panel type against your viewing angle.</b> Shared desks and side seating punish the wrong panel choice.</li>"
    "<li><b>Measure the desk before the diagonal.</b> A monitor that fits the budget and not the desk is a return waiting to happen.</li>"
    "<li><b>Ignore most refresh-rate marketing.</b> For office and studio work, panel behaviour matters far more.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/4k-on-a-small-tv-when-its-invisible/\">when 4K on a small screen is invisible</a>, <a href=\"/tech/projector-vs-tv-compound-viewing/\">projector versus TV for compound viewing</a> and <a href=\"/tech/antenna-vs-satellite-vs-streaming-live-tv/\">antenna versus satellite versus streaming</a>.</p>",

"writers/learn/freelance-paid-writing/how-much-to-charge-for-an-article":
    "<h2>Price the work, not the words</h2>"
    "<p>Article pricing fails when it is derived purely from word count, because two eight-hundred-word pieces can differ by days of reporting. The honest method stacks the real inputs: the research the piece demands, the interviews it needs, the revisions a given client's process implies, and the rights being sold on top of the writing. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> publishes resources for writers structuring rates and client work. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The rate stack</h2>"
    "<ul>"
    "<li><b>Start from a day rate, then divide.</b> A floor derived from your working time survives bad estimates.</li>"
    "<li><b>Add for reporting.</b> Interviews, documents and travel are time the fee must carry.</li>"
    "<li><b>Add for process.</b> Endless-approval clients pay for that process, whether or not the rate card says so.</li>"
    "<li><b>Add for rights.</b> Exclusivity, reprint and corporate usage are separate goods from the writing itself.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/freelance-paid-writing/how-writing-retainers-work/\">how writing retainers work</a>, <a href=\"/writers/guides/how-to-check-a-freelance-writing-contract/\">how to check a freelance writing contract</a> and <a href=\"/writers/writing/longreads/\">Longreads</a>.</p>",

"writers/writing/poetry-wales-features":
    "<h2>A poetry magazine that publishes features too</h2>"
    "<p>Poetry Wales is a long-running magazine that pairs poetry with writing about poetry — reviews, essays and features on the Welsh and international scene. That mix matters to writers who do both: the magazine is a home for poems and for the criticism that surrounds them, which makes it one of the few places where a poet with a critical practice can publish both sides of the work. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the literary-magazine field it belongs to. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing about poetry credibly</h2>"
    "<ul>"
    "<li><b>Quote precisely and sparingly.</b> Poetry criticism rests on close reading, and the reading must be visible.</li>"
    "<li><b>Situate the book.</b> A review of one collection should place it, not just praise it.</li>"
    "<li><b>Write for readers of poetry, not only poets.</b> The best criticism opens the door rather than guarding it.</li>"
    "<li><b>Read the features, not just the poems.</b> The critical voice of a magazine shows there most clearly.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/modern-poetry-in-translation/\">Modern Poetry in Translation</a>, <a href=\"/writers/writing/fourteen-poems/\">Fourteen Poems</a> and <a href=\"/writers/writing/mslexia/\">Mslexia</a>.</p>",

"home/kitchen-hygiene-routine":
    "<h2>The kitchen is a workflow, not a list</h2>"
    "<p>Kitchen hygiene works when it is built into the order of cooking rather than added on top of it. The same few surfaces are touched during every meal preparation, the same few cloths carry everything around, and the same sink area returns to contamination hours after cleaning. Redesigning the flow beats scrubbing harder. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the food-safety principles this desk's kitchen guides follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Building the routine into the cooking</h2>"
    "<ul>"
    "<li><b>Wash at the transitions.</b> Hands and boards change state when raw food is finished with, not at the end.</li>"
    "<li><b>Colour-code or sequence boards.</b> Raw and ready-to-eat never share a surface at the same time.</li>"
    "<li><b>Change the cloth daily.</b> The kitchen cloth is the most mobile surface in the house.</li>"
    "<li><b>Finish at the sink.</b> Sponges and drains get their own weekly routine or they undo the rest.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ants-in-the-kitchen/\">ants in the kitchen</a>, <a href=\"/home/kitchen-ventilation-damp/\">kitchen ventilation and damp</a> and <a href=\"/home/washing-machine-mould-door-seal/\">washing-machine door seal mould</a>.</p>",

"writers/writing/slate":
    "<h2>A general-interest magazine that pays on schedule</h2>"
    "<p>Slate has run for decades as an online general-interest magazine with a strong voice section — politics, culture, advice, criticism — and a freelance pipeline that is unusually well documented. For writers it is significant as a pitch market: the editorial process is legible, the covers are public, and the piece-to-payment path is one of the better-known in digital magazines. The <a href=\"" + _w("Slate+(magazine)") + "\" rel=\"noopener\">magazine's history and format</a> are collected in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching a voice section</h2>"
    "<ul>"
    "<li><b>The argument arrives first.</b> Voice sections buy a claim the piece will defend, not a topic it will wander.</li>"
    "<li><b>News pegs have hours, not days.</b> Timely pitches are perishable goods.</li>"
    "<li><b>Read the section you are pitching.</b> Advice and criticism run on different editorial logic at the same magazine.</li>"
    "<li><b>Be specific about the evidence.</b> What you know, saw, or can obtain is the pitch's real subject line.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/business-insider/\">Business Insider</a>, <a href=\"/writers/writing/broadview/\">Broadview</a> and <a href=\"/writers/writing/the-offing/\">The Offing</a>.</p>",

"tech/dns-not-working-propagation":
    "<h2>Propagation is mostly a naming problem</h2>"
    "<p>The phrase DNS propagation suggests weather — something that arrives eventually — but the delays are specific: record time-to-live values still cached by resolvers, records not yet saved where they were edited, nameservers that have not been updated at the registrar, or the classic mismatch between the record types that different services need. Reference material sits under <a href=\"" + _w("Domain+Name+System") + "\" rel=\"noopener\">the Domain Name System</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Diagnose from the root downward</h2>"
    "<ul>"
    "<li><b>Ask the authoritative nameservers directly.</b> Their answer separates your records from the world's cache.</li>"
    "<li><b>Check the TTL before waiting.</b> The cache is obeying a timer someone set earlier, usually you.</li>"
    "<li><b>Verify every record type the service needs.</b> A correct A record with a missing TXT verification still fails.</li>"
    "<li><b>Leave it alone during the window.</b> Editing records resets the diagnosis without speeding the cache.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/dns-problems-diagnosed/\">DNS problems diagnosed</a>, <a href=\"/tech/custom-domain-dns-order/\">the order to set up a custom domain</a> and <a href=\"/tech/how-the-internet-works/\">how the internet works</a>.</p>",

"tech/how-much-ram-do-you-need":
    "<h2>RAM is a ceiling, not a speed boost</h2>"
    "<p>Memory does not make a computer faster; it decides how much the computer can hold at once before it starts trading speed for space. The right amount is therefore specific to what runs simultaneously — the browser tab count, the creative suite, the virtual machines — and once that amount is reached, spending on more buys nothing. Reference material sits under <a href=\"" + _w("random-access+memory") + "\" rel=\"noopener\">random-access memory</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Sizing it honestly</h2>"
    "<ul>"
    "<li><b>Count your real open set.</b> The working question is simultaneous usage, not installed software.</li>"
    "<li><b>Watch for swap during a normal day.</b> A drive light on constantly during light work is the memory ceiling showing.</li>"
    "<li><b>Match the machine's weak point.</b> Memory cannot rescue a slow storage drive or an old processor.</li>"
    "<li><b>Leave an upgrade slot when you can.</b> Soldered memory makes the first purchase the final one.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-buying-ram-storage/\">laptop buying: RAM and storage</a>, <a href=\"/tech/laptop-ram-vs-ssd-first/\">RAM or SSD: which upgrade first</a> and <a href=\"/tech/student-laptop-spec-floor-2026/\">student laptop spec floor</a>.</p>",

"writers/writing/earth-island-journal":
    "<h2>Environmental reporting with an argument</h2>"
    "<p>Earth Island Journal publishes environmental reporting, essays and interviews with an activist edge, and it has always favoured pieces that arrive with a finding rather than a feeling. For environmental writers it is a market where reporting depth shows directly in the acceptance rate. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the independent-magazine field it belongs to. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What environmental pitches need</h2>"
    "<ul>"
    "<li><b>A finding you can stand behind.</b> Investigations and documented trends pitch; general concern does not.</li>"
    "<li><b>Access described plainly.</b> Who you can reach and where you can go is part of the pitch.</li>"
    "<li><b>The local stakes.</b> The strongest environmental stories are about specific people and places.</li>"
    "<li><b>Form matched to the finding.</b> Dispatches, features and essays carry different evidence budgets.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/high-country-news/\">High Country News</a>, <a href=\"/writers/writing/ecotone/\">Ecotone</a> and <a href=\"/writers/writing/agni/\">AGNI</a>.</p>",

"home/fridge-not-cooling":
    "<h2>The fridge is failing at one of three jobs</h2>"
    "<p>A refrigerator that runs but does not cool is failing at airflow, at heat removal, or at the sealed system itself — and the first two are free to fix. Before calling anyone, work the ladder: door seals, the coils that shed heat, the vents that carry cold air inside, and the temperature dials that a household member may have moved. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes the household appliance energy guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The free checks, in order</h2>"
    "<ul>"
    "<li><b>Test the door seal with paper.</b> A seal that lets the paper slide out is leaking cold air continuously.</li>"
    "<li><b>Clean the coils at the back or underneath.</b> Dusty coils cannot shed heat; the cabinet warms up around them.</li>"
    "<li><b>Clear the vents inside.</b> Overpacked shelves block the cold air that keeps the lower box working.</li>"
    "<li><b>Check the dial and the ambient temperature.</b> Garages in hot seasons push fridges past their design range.</li>"
    "</ul>"
    "<p>See <a href=\"/home/fridge-not-cold-enough/\">fridge not cold enough</a>, <a href=\"/home/fridge-door-seal-test/\">the fridge door seal test</a> and <a href=\"/home/fridge-coils-twice-a-year/\">cleaning fridge coils twice a year</a>.</p>",

"home/condensation-vs-rising-vs-penetrating-damp":
    "<h2>Three damps, three fixes</h2>"
    "<p>The three kinds of damp look similar on a wall and demand opposite treatments. Condensation comes from indoor air meeting cold surfaces; rising damp comes from ground moisture breaching the masonry; penetrating damp comes from water getting through the building envelope. Misidentifying them is the expensive mistake — a dehumidifier cannot fix a failed damp course, and repainting cannot fix a leaking wall. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK Government</a> publishes housing damp guidance this desk's diagnosis pages follow. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The patterns that identify each</h2>"
    "<ul>"
    "<li><b>Condensation forms where air stalls.</b> Behind furniture, on glass, on cold corners — and it worsens in winter.</li>"
    "<li><b>Rising damp leaves a tide mark.</b> A distinct line above skirting height, salts in the plaster, ground-floor walls.</li>"
    "<li><b>Penetrating damp maps the leak.</b> It follows the wetting path — the roof slope, the gully, the window head.</li>"
    "<li><b>Test before treating.</b> A moisture meter tells you which damp you are holding, and the fix follows from it.</li>"
    "</ul>"
    "<p>See <a href=\"/home/condensation-ventilation-that-works/\">condensation ventilation that works</a>, <a href=\"/home/painting-over-damp/\">painting over damp</a> and <a href=\"/home/bathroom-fan-condensation/\">bathroom fans and condensation</a>.</p>",

"home/us-home-permits":
    "<h2>Permits are disclosure insurance</h2>"
    "<p>US building permits are the paperwork that says a change was inspected and met code when it was made. The value shows up later: at sale, at insurance claim, at inspection. Work done without a permit does not disappear — it waits, usually surfacing when a disclosure form asks the question directly. Reference material sits under <a href=\"" + _w("building+permit") + "\" rel=\"noopener\">building permits</a>. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Where owners get caught</h2>"
    "<ul>"
    "<li><b>Structural, electrical and plumbing changes pull permits almost everywhere.</b> The permit counter's list is the authority, not the contractor's opinion.</li>"
    "<li><b>The seller's disclosure asks directly.</b> Unpermitted work answered honestly is manageable; discovered later is not.</li>"
    "<li><b>Contractors should pull the permit in their name.</b> It ties their licence to the inspection record.</li>"
    "<li><b>Keep the final sign-off.</b> The closed permit is the document future buyers and insurers actually want.</li>"
    "</ul>"
    "<p>See <a href=\"/home/unpermitted-work-home-sale/\">unpermitted work when selling</a>, <a href=\"/home/unpermitted-work-insurance/\">unpermitted work and insurance</a> and <a href=\"/home/us-diy-electrical-rules/\">US DIY electrical rules</a>.</p>",

"home/wiring-red-flags-in-your-home":
    "<h2>The warning signs that justify a call</h2>"
    "<p>House wiring hides its condition behind paint, which is why the visible symptoms matter so much: flickering that follows load, outlets that run warm, breakers that trip on a pattern, or a burning smell with no source. Each one describes a specific fault, and each one is a reason to stop using the affected circuit until an electrician has seen it. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the home electrical fire-warning guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What each flag means</h2>"
    "<ul>"
    "<li><b>Lights dim when a motor starts.</b> That is voltage sag on a shared circuit — annoying first, unsafe as it accumulates.</li>"
    "<li><b>Warm outlets or discoloured faceplates.</b> Heat at a connection is the fault itself, not a side effect.</li>"
    "<li><b>One breaker that trips repeatedly.</b> The breaker is doing its job; something on the circuit is failing.</li>"
    "<li><b>Any burning or fishy smell with no source.</b> Cut power at the panel and call — heated insulation has that smell for a reason.</li>"
    "</ul>"
    "<p>See <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a>, <a href=\"/home/circuit-breaker-tripped-not-mystery/\">why the circuit breaker tripped</a> and <a href=\"/home/us-diy-electrical-rules/\">US DIY electrical rules</a>.</p>",

"tech/tool/uuid-generator":
    "<h2>What a UUID is for</h2>"
    "<p>A UUID is an identifier designed to be generated without asking anyone's permission — no central registry, no collision anxiety across systems, just 128 bits of structure that make duplicates vanishingly unlikely. That is why they show up as database keys, request identifiers and filenames across distributed systems. Reference material sits under <a href=\"" + _w("universally+unique+identifier") + "\" rel=\"noopener\">universally unique identifiers</a>. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Using them correctly</h2>"
    "<ul>"
    "<li><b>Choose the version deliberately.</b> Time-ordered UUIDs index well; random ones avoid leaking sequence information.</li>"
    "<li><b>Treat them as opaque.</b> Parsing meaning out of a v4 identifier is a mistake waiting to be made.</li>"
    "<li><b>Do not use them as secrets.</b> Uniqueness is not unguessability; pair them with real tokens where secrecy matters.</li>"
    "<li><b>Store and compare in one canonical form.</b> Case and brace styles are formatting, not identity.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/base64-encoder/\">the Base64 encoder</a>, <a href=\"/tech/tool/json-formatter/\">the JSON formatter</a> and <a href=\"/tech/tool/case-converter/\">the case converter</a>.</p>",

"writers/writing/clarkesworld-nonfiction":
    "<h2>The other half of a fiction magazine</h2>"
    "<p>Clarkesworld is known for its fiction, but its nonfiction — interviews, essays and commentary on the field — is a working market of its own. The nonfiction side shares the magazine's standards and its pay schedule while demanding a different toolkit: the ability to interview well, to read a career closely, or to argue about the state of a genre without repeating its commonplaces. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> maps the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing the field's nonfiction</h2>"
    "<ul>"
    "<li><b>Interviews are reporting.</b> Good ones are researched encounters, not question lists read aloud.</li>"
    "<li><b>Essays need a claim.</b> Genre commentary earns its place by arguing something the field has not settled.</li>"
    "<li><b>Know the canon and the present.</b> Credibility in this market is visible within two paragraphs.</li>"
    "<li><b>Match the word count to the argument.</b> Tight essays place better than padded ones, everywhere.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/clarkesworld-fiction/\">Clarkesworld fiction</a>, <a href=\"/writers/writing/strange-horizons-fiction/\">Strange Horizons fiction</a> and <a href=\"/writers/writing/diabolical-plots/\">Diabolical Plots</a>.</p>",

"writers/writing/kill-your-darlings":
    "<h2>An Australian magazine with a sharp voice</h2>"
    "<p>Kill Your Darlings built its readership on cultural criticism and essays with a distinctly Australian register — wry, well-read and unwilling to mistake enthusiasm for analysis. For writers it is a study in tone as a market position: the magazine commissions pieces that sound like someone specific is speaking. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the literary-magazine field it belongs to. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing criticism with a register</h2>"
    "<ul>"
    "<li><b>Voice is a stance, not adjectives.</b> The wryness follows from judgement about the subject.</li>"
    "<li><b>One argument per piece.</b> Cultural essays with two arguments review the writer, not the topic.</li>"
    "<li><b>Spend the opening on the claim.</b> Voice-led magazines still buy essays about something.</li>"
    "<li><b>Read the magazine's recent tone aloud.</b> Register is heard better than it is described.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/island-magazine/\">Island</a>, <a href=\"/writers/writing/australian-book-review/\">Australian Book Review</a> and <a href=\"/writers/writing/overland-fiction/\">Overland</a>.</p>",

"writers/writing/narratively":
    "<h2>Stories that do not fit the news cycle</h2>"
    "<p>Narratively made its name on deeply reported hidden-story journalism — the overlooked, the subcultural, the quietly extraordinary — and its essay strands continue the same logic. The pitch bar is not the topic but the discovery: what did the writer find that readers could not have reached on their own? The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> is the map of digital-first literary outlets of this kind. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The hidden-story pitch</h2>"
    "<ul>"
    "<li><b>Lead with the discovery.</b> If the pitch does not contain the surprise, the piece will not either.</li>"
    "<li><b>Prove access early.</b> Hidden stories live behind relationships the writer already has.</li>"
    "<li><b>Keep the stakes human.</b> The outlet's best work is about people, reported closely.</li>"
    "<li><b>Pitch the shape.</b> Reported feature, first-person essay and short memoir run different lengths here.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/electric-literature-essays/\">Electric Literature essays</a>, <a href=\"/writers/writing/litmag-online/\">LitMag Online</a> and <a href=\"/writers/writing/guernica/\">Guernica</a>.</p>",

"writers/writing/analog-fact":
    "<h2>The nonfiction side of a science-fiction institution</h2>"
    "<p>Analog's fact articles and columns have accompanied its fiction for generations, and the nonfiction slot remains one of the field's most durable writing markets: science written for readers who love speculation but demand accuracy. The requirement is expertise worn lightly — the writer must actually know the subject and must not talk down to a readership of engineers, biologists and enthusiasts. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing science for this readership</h2>"
    "<ul>"
    "<li><b>Anchor to the real science.</b> The column's standard is checked facts and honest uncertainty.</li>"
    "<li><b>Find the speculative hinge.</b> The best pieces show where current knowledge points at the unknown.</li>"
    "<li><b>Keep the maths loadable.</b> Equations serve the explanation; they do not replace it.</li>"
    "<li><b>Query before drafting at length.</b> Slots are thematic enough to shape the piece in advance.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/analog-fiction/\">Analog fiction</a>, <a href=\"/writers/writing/asimovs-fiction/\">Asimov's fiction</a> and <a href=\"/writers/writing/clarkesworld-nonfiction/\">Clarkesworld nonfiction</a>.</p>",

"writers/writing/overland-online":
    "<h2>The online magazine's working layer</h2>"
    "<p>Overland's online edition is where the magazine's daily voice lives — shorter essays, arguments, responses and reported pieces that run between the print issues. For writers it is the accessible entry point of the magazine: faster commissioning cycles, topical pitches, and a readership that argues back in the best sense. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> maps the independent field it sits within. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing for the online cadence</h2>"
    "<ul>"
    "<li><b>Timely pitches travel faster.</b> The online edition can publish a response while the question is still open.</li>"
    "<li><b>Shorter is a discipline, not a discount.</b> Online essays earn their length in argument per paragraph.</li>"
    "<li><b>Expect engagement.</b> The audience replies; pieces that survive scrutiny build a reputation here quickly.</li>"
    "<li><b>Use it as a route to print.</b> Writers who publish online regularly enter the longer commissions.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/overland-fiction/\">Overland fiction</a>, <a href=\"/writers/writing/griffith-review/\">Griffith Review</a> and <a href=\"/writers/writing/hinterland/\">Hinterland</a>.</p>",

"home/electrical-fire-warning-signs":
    "<h2>Electrical fires announce themselves first</h2>"
    "<p>Few house fires begin as surprises. The warning signs come days or weeks earlier: an outlet that has discoloured, a breaker that trips on a schedule, a faint buzzing at a switch, or a smell like hot plastic near one wall. Each is a connection or a conductor under stress, and each is fixable while the wall is still cold. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the home electrical fire guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What to do at each sign</h2>"
    "<ul>"
    "<li><b>Discolouration or scorch marks.</b> Stop using the outlet; the damage is at the connection behind it.</li>"
    "<li><b>Buzzing or crackling at a switch.</b> Cut the circuit — arcing is audible long before it is visible.</li>"
    "<li><b>Repeated breaker trips.</b> A pattern tied to one appliance is the appliance; a pattern without one is the wiring.</li>"
    "<li><b>Any smoke without flame.</b> Cut power at the panel first; water on an energised fire spreads it.</li>"
    "</ul>"
    "<p>See <a href=\"/home/wiring-red-flags-in-your-home/\">wiring red flags</a>, <a href=\"/home/dryer-vent-cleaning-fire-risk/\">dryer vents and fire risk</a> and <a href=\"/home/cooking-oil-fire-plan/\">the cooking-oil fire plan</a>.</p>",

"writers/learn/examples/example-of-a-press-release":
    "<h2>What the example demonstrates</h2>"
    "<p>A press release example earns its place when it shows the form's logic rather than decorating it: a headline that states the news, a dateline and a lead that answers who, what, when and where in two sentences, quotes that add a voice instead of adding adjectives, and boilerplate that describes the organisation without selling it. The <a href=\"" + _w("press+release") + "\" rel=\"noopener\">press release</a> is one of the most standardised forms in professional writing, and its standardisation is the point. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the example against your draft</h2>"
    "<ul>"
    "<li><b>Find the news in the first paragraph.</b> If it appears in paragraph three, the structure is inverted.</li>"
    "<li><b>Count the quotes.</b> Two purposeful quotes beat five ceremonial ones.</li>"
    "<li><b>Check the boilerplate length.</b> It describes the organisation; it does not carry the announcement.</li>"
    "<li><b>Include the contact line.</b> The release's real job is to make the next step easy for a journalist.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-blog-post/\">the blog post example</a>, <a href=\"/writers/learn/examples/example-of-a-book-review/\">the book review example</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-pitching-editors/\">the dos and don'ts of pitching editors</a>.</p>",

"home/ceiling-leak-11pm":
    "<h2>The night-of plan before anyone arrives</h2>"
    "<p>A ceiling leak discovered at night has three goals in order: keep people away from the bulge, keep electricity away from the water, and keep the water moving out rather than pooling in. Everything after that is diagnosis and repair, which can wait for daylight and a professional. What cannot wait is the ceiling itself — a sagging plaster ceiling is carrying water that keeps getting heavier. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes the household water-damage guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The night checklist</h2>"
    "<ul>"
    "<li><b>Clear the room under the leak.</b> Sagging plaster drops without warning and without asking.</li>"
    "<li><b>Move power away, then switch off if needed.</b> Water finds light fittings and ceiling roses first.</li>"
    "<li><b>Puncture the bulge at its edge, into a bucket.</b> A controlled drain beats an uncontrolled collapse.</li>"
    "<li><b>Find and stop the source if it is your water.</b> Your own shutoff valve turns an emergency into an inconvenience.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ceiling-water-stain-removal/\">ceiling water stain removal</a>, <a href=\"/home/flat-roof-ponding-and-leaks/\">flat roof ponding and leaks</a> and <a href=\"/home/hidden-water-leak-meter-test/\">the meter test for hidden leaks</a>.</p>",

}
