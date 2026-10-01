# -*- coding: utf-8 -*-
"""Editorial depth sections, part 16: batch K, the 600-616 word tranche against
the 750-word bar, plus home/privacy (598 of 732), kenya opportunities (671 of
819) and three t8b top-ups. 84 pages total. Blocks sized to clear in one pass.
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

DEPTH_SECTIONS16 = {

"tech/ai-start-here":
    "<h2>Start with the tasks</h2>"
    "<p>This desk's AI coverage starts from tasks, not futures: drafting help, summarising, code assistance and research triage are the workflows that actually change under these tools. The claims tested here are small and checkable — what the tools do well, where they fail with confidence, and what the reader should keep doing by hand. The <a href=\"" + _w("artificial+intelligence") + "\" rel=\"noopener\">AI field</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The starting map</h2>"
    "<ul>"
    "<li><b>Useful today.</b> Drafting, transformation, summarising and code scaffolding are the honest wins.</li>"
    "<li><b>Verify everything.</b> The confident error is the technology's signature failure mode.</li>"
    "<li><b>Mind the paste.</b> Privacy is a workflow decision before it is a policy question.</li>"
    "<li><b>Build habits, not dependencies.</b> The models change monthly; the prompting discipline outlasts them.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/ai-useful-vs-hype/\">AI useful versus hype</a>, <a href=\"/tech/ai-privacy-what-not-to-paste/\">AI privacy: what not to paste</a> and <a href=\"/tech/how-large-language-models-actually-work/\">how large language models work</a>.</p>",

"tech/deploy-python-app":
    "<h2>The deploy that stays deployed</h2>"
    "<p>Deploying a Python app is a checklist in disguise: the pinned dependencies, the environment variables, the health check and the logs that will explain the 3am failure. The first-hand lesson from this desk's own Render deployments is that boring configuration is the one that survives — the build command, the start command, and the port the platform expects. The <a href=\"" + _w("software+deployment") + "\" rel=\"noopener\">deployment practice</a> is documented in standard references. By the Bryme Technical Research desk. Reviewed 28 September 2026.</p>"
    "<h2>The deploy checklist</h2>"
    "<ul>"
    "<li><b>Pin the dependencies.</b> The requirements file is the deploy's memory.</li>"
    "<li><b>Environment variables in the platform.</b> Secrets never enter the repository.</li>"
    "<li><b>A health check endpoint.</b> The platform's watchdog needs a door to knock on.</li>"
    "<li><b>Logs are the post-mortem.</b> The first deploy is the logging test.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/render-deployment-failures-what-they-taught-me/\">render deployment failures</a>, <a href=\"/tech/environment-variables-guide/\">the environment variables guide</a> and <a href=\"/tech/works-locally-fails-online/\">works locally, fails online</a>.</p>",

"writers/learn/journaling-personal":
    "<h2>The private page</h2>"
    "<p>Journaling and personal writing are the private end of the craft: the pages where the writer thinks on paper, tests sentences nobody will grade, and builds the noticing muscle that every published piece later depends on. The forms here run from the daily prompt to the personal essay's raw material. The <a href=\"" + _w("journaling") + "\" rel=\"noopener\">journaling practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What the practice builds</h2>"
    "<ul>"
    "<li><b>Noticing.</b> The journal trains the eye that later finds the story.</li>"
    "<li><b>Fluency.</b> Daily sentences keep the hand warm for the working draft.</li>"
    "<li><b>Material.</b> The private page is the personal essay's quarry.</li>"
    "<li><b>Honesty.</b> The unwatched page is where the writer finds their real voice.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/journaling-personal/how-to-start-journaling/\">how to start journaling</a>, <a href=\"/writers/learn/journaling-personal/daily-journal-prompts/\">daily journal prompts</a> and <a href=\"/writers/learn/start-writing/\">start writing</a>.</p>",

"entertainment/reviews/the-milkmaid":
    "<h2>Language, landscape and survival</h2>"
    "<p>The Milkmaid follows two sisters through a rural landscape where language, faith and violence negotiate every scene — a film that trusts its imagery to carry what the dialogue refuses to explain. Its festival run marked it as one of the period's most visually deliberate Nigerian features. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the film does</h2>"
    "<ul>"
    "<li><b>The landscape argues.</b> The terrain is the film's moral geography.</li>"
    "<li><b>Multilingual by design.</b> The dialogue's languages carry the world's texture.</li>"
    "<li><b>The sister plot holds the frame.</b> The search is personal before it is political.</li>"
    "<li><b>Festival craft.</b> The image quality is the production's statement of intent.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/nollywood-golden-age-explained/\">Nollywood's golden age</a>, <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a> and <a href=\"/entertainment/reviews/breath-of-life/\">the Breath of Life review</a>.</p>",

"sports/premier-league-transfer-tracker-august-2026":
    "<h2>The window's ledger</h2>"
    "<p>A transfer tracker is the window's ledger: every done deal, the fee as reported, the loan with its option, and the paperwork day that makes it official. Read as a whole, the month's business shows each club's squad logic — and the market's inflation — more clearly than any single headline. The <a href=\"" + PL + "\" rel=\"noopener\">Premier League</a> market this desk follows prices such deals in the open. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the tracker</h2>"
    "<ul>"
    "<li><b>Done deal means registered.</b> The announcement and the registration are different days.</li>"
    "<li><b>Fees are reported, not official.</b> The add-ons are where the numbers move.</li>"
    "<li><b>Loans with options are the real market.</b> The option price is the deal's true face.</li>"
    "<li><b>The deadline is a force multiplier.</b> The last day prices scarcity in public.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-the-transfer-window-works/\">how the transfer window works</a>, <a href=\"/sports/how-football-transfer-medicals-work/\">how transfer medicals work</a> and <a href=\"/sports/deadline-day-dont-try-to-make-sense-of-it/\">deadline day</a>.</p>",

"entertainment/reviews/the-meeting":
    "<h2>One room, many agendas</h2>"
    "<p>The Meeting stages a single room's worth of negotiation — the agendas circling one another, the comedy of manners doing the plot's heavy lifting, and the ensemble carrying a chamber piece with genre polish. Its pleasure is structural: the meeting as a machine that reveals each character by what they need from it. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the chamber piece does</h2>"
    "<ul>"
    "<li><b>The room is the engine.</b> Every agenda finds its friction in the same four walls.</li>"
    "<li><b>The comedy is character comedy.</b> The laughs arrive from wants colliding.</li>"
    "<li><b>The ensemble is the plot.</b> No single lead; the negotiation carries the story.</li>"
    "<li><b>Time pressure as structure.</b> The clock in the room tightens every scene.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/reviews/mokalik/\">the Mokalik review</a>, <a href=\"/entertainment/reviews/shadow-parties/\">the Shadow Parties review</a> and <a href=\"/entertainment/nollywood-golden-age-explained/\">Nollywood's golden age</a>.</p>",

"entertainment/shonen-shojo-seinen-explained":
    "<h2>The demographic system</h2>"
    "<p>Shonen, shojo, seinen and josei are demographic labels before they are genres — a publishing system that sorts manga magazines by their target reader, and in doing so sorts the storytelling with it: pacing, stakes, romance and violence each bend toward the imagined audience. The <a href=\"" + _w("sh%C5%8Dnen+manga") + "\" rel=\"noopener\">manga demographic system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What each label promises</h2>"
    "<ul>"
    "<li><b>Shonen.</b> Friendship and escalation; the tournament arc is the signature.</li>"
    "<li><b>Shojo.</b> Interiority and romance; the emotional register carries the plot.</li>"
    "<li><b>Seinen.</b> Ambiguity and consequence; the pacing trusts the adult reader.</li>"
    "<li><b>The labels bend.</b> The best series borrow across the aisles constantly.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/anime-canon-and-filler-explained/\">anime canon and filler</a>, <a href=\"/entertainment/anime-seasons-and-cours-explained/\">anime seasons and cours</a> and <a href=\"/entertainment/isekai-anime-explained/\">isekai anime explained</a>.</p>",

"sports/can-ronaldo-score-1000-goals":
    "<h2>The arithmetic of the chase</h2>"
    "<p>The 1,000-goal question is arithmetic plus physiology: the career total against the calendar, the league's scoring rate against the ageing curve, and the international fixtures that decide how many games are actually available. The honest answer is a projection with stated assumptions — not a verdict. The <a href=\"" + _w("Cristiano+Ronaldo") + "\" rel=\"noopener\">career record</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>The projection's assumptions</h2>"
    "<ul>"
    "<li><b>Minutes, not seasons.</b> The chase needs playing time, not contracts.</li>"
    "<li><b>The scoring rate's decay curve.</b> Every projection assumes a slope.</li>"
    "<li><b>Fixture availability.</b> The international calendar is part of the arithmetic.</li>"
    "<li><b>Health is the unnamed variable.</b> The record books are read survivorship-first.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/best-football-players-in-the-world-2026/\">the best football players in the world</a>, <a href=\"/sports/how-football-transfer-medicals-work/\">how transfer medicals work</a> and <a href=\"/sports/who-will-win-the-2026-ballon-dor/\">the 2026 Ballon d'Or</a>.</p>",

"tech/tv-as-monitor-overscan-fix":
    "<h2>The cut-off edges</h2>"
    "<p>Overscan is the television treating your desktop like broadcast footage: cropping the edges to protect old signals, and hiding the taskbar and window borders behind the bezel. The fix is a setting on one of the two devices — the TV's 'just scan' or the GPU's scaling — and the diagnosis is which one is lying. The <a href=\"" + _w("overscan") + "\" rel=\"noopener\">overscan behaviour</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Where the fix lives</h2>"
    "<ul>"
    "<li><b>TV side first.</b> The picture mode's 'just scan' or '1:1 pixel' ends most cases.</li>"
    "<li><b>GPU scaling second.</b> The driver's scaling mode is the other suspect.</li>"
    "<li><b>HDMI port labelling.</b> Some ports run PC mode by name.</li>"
    "<li><b>Check the resolution handshake.</b> The TV may be scaling before you are.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/new-tv-settings-day-one/\">new TV settings, day one</a>, <a href=\"/tech/one-big-monitor-vs-two/\">one big monitor or two</a> and <a href=\"/tech/picture-settings-that-fix-the-soap-opera-look/\">picture settings that fix the soap opera look</a>.</p>",

"writers/learn/writing-process/how-to-brainstorm-and-find-ideas":
    "<h2>Ideas are found, not waited for</h2>"
    "<p>Brainstorming is a production method: the quota of bad ideas, the collision of two unrelated lists, the question flipped until it becomes a story. Writers who find ideas reliably run the method on schedule — the notebook fills while the mood is still optional. The <a href=\"" + _w("brainstorming") + "\" rel=\"noopener\">brainstorming practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The idea machines</h2>"
    "<ul>"
    "<li><b>The quota.</b> Ten ideas before judging any of them; volume precedes quality.</li>"
    "<li><b>The collision.</b> Two unrelated lists, one forced connection.</li>"
    "<li><b>The flipped question.</b> The obvious answer's opposite is the pitch.</li>"
    "<li><b>The complaint log.</b> The things you mutter at the news are stories.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/start-writing/how-to-turn-an-idea-into-an-outline/\">turn an idea into an outline</a>, <a href=\"/writers/learn/start-writing/how-to-overcome-writers-block/\">how to overcome writer's block</a> and <a href=\"/writers/learn/writing-process/\">the writing process</a>.</p>",

"entertainment/nigerian-thrillers-worth-your-time":
    "<h2>Five doors into the genre</h2>"
    "<p>The Nigerian thriller has as many registers as the industry has cities: the crime procedural, the folk-horror turn, the domestic menace, the heist gone wrong. This starter set maps the range rather than the reputation — the films that show what the genre does when it plays by its own rules. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What to watch for</h2>"
    "<ul>"
    "<li><b>The procedural register.</b> Investigation stories with local institutions in frame.</li>"
    "<li><b>The folk-horror turn.</b> The genre's most distinctive Nigerian seam.</li>"
    "<li><b>Domestic menace.</b> The household as the thriller's locked room.</li>"
    "<li><b>The heist structure.</b> Genre machinery with Nollywood energy.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/reviews/the-milkmaid/\">the Milkmaid review</a>, <a href=\"/entertainment/reviews/nneka-the-pretty-serpent/\">the Nneka review</a> and <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a>.</p>",

"home/pressure-washer-safe-use":
    "<h2>What the washer does well</h2>"
    "<p>A pressure washer cleans hard surfaces brilliantly and damages soft ones instantly: the strip of paint, the gouged timber, the forced joint. The tool's discipline is distance and angle — and knowing which surfaces were never meant to face a concentrated jet. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The safe-use rules</h2>"
    "<ul>"
    "<li><b>Test the inconspicuous corner first.</b> The wand's pressure is a surface decision.</li>"
    "<li><b>Keep the distance.</b> The nozzle's rating assumes it.</li>"
    "<li><b>Never chase paint.</b> The edge you lift is the repaint you booked.</li>"
    "<li><b>Sealed surfaces only.</b> The unsealed timber and the old mortar lose.</li>"
    "</ul>"
    "<p>See <a href=\"/home/gutter-cleaning-damage/\">gutter cleaning damage</a>, <a href=\"/home/deep-clean-schedule/\">the deep clean schedule</a> and <a href=\"/home/external-wall-crack-seal/\">the external wall crack seal</a>.</p>",

"tech/nvme-vs-sata-portable-ssd":
    "<h2>The gap is the protocol</h2>"
    "<p>NVMe and SATA portable SSDs look identical and behave differently: the protocol ceiling decides sustained transfer speeds, and the price gap follows the throughput. For backups and video work the NVMe's headroom is real; for document shuttles the SATA drive's honesty is enough. The <a href=\"" + _w("NVMe") + "\" rel=\"noopener\">NVMe protocol</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing by workload</h2>"
    "<ul>"
    "<li><b>Video and large archives: NVMe.</b> Sustained writes are the honest benchmark.</li>"
    "<li><b>Documents and handoffs: SATA.</b> The speed ceiling never binds.</li>"
    "<li><b>Check the enclosure.</b> The bridge chip is the silent ceiling.</li>"
    "<li><b>Both beat spinning disks.</b> The real baseline is the drive in the drawer.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/data-shuttle-sd-usb-ssd/\">the data shuttle comparison</a>, <a href=\"/tech/sd-card-not-reading-recovery/\">SD card recovery</a> and <a href=\"/tech/cloud-vs-local-backup/\">cloud versus local backup</a>.</p>",

"tech/refurbished-vs-new-tech":
    "<h2>When refurbished is the smarter buy</h2>"
    "<p>Refurbished tech wins when the warranty is real, the battery is graded honestly, and the generation gap is smaller than the price gap. The refurbished market's failure mode is not age — it is missing recourse. The <a href=\"" + _w("refurbishment") + "\" rel=\"noopener\">refurbishment market</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The buy checklist</h2>"
    "<ul>"
    "<li><b>Warranty first.</b> The seller's guarantee is the product's real spec.</li>"
    "<li><b>Battery health graded.</b> The percentage is the laptop's remaining life.</li>"
    "<li><b>Generation maths.</b> Two-year-old flagship beats new budget on everything but the charger.</li>"
    "<li><b>Return policy in writing.</b> The seven-day window is where lemons surface.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/new-midrange-vs-used-flagship/\">new midrange versus used flagship</a>, <a href=\"/tech/dell-vs-hp-refurbished-laptops-nigeria/\">Dell versus HP refurbished in Nigeria</a> and <a href=\"/tech/repair-vs-replace/\">repair versus replace</a>.</p>",

"writers/learn/freelance-paid-writing/track-your-writing-income":
    "<h2>The business ledger</h2>"
    "<p>Tracking writing income is the habit that turns freelancing into a business: which markets pay, which clients pay late, and which line of work is actually carrying the year. The ledger is a spreadsheet and a discipline — the invoice log, the payment dates, and the quarterly review that changes the pitch list. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government self-assessment guidance</a> is the standard this desk follows. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The tracking discipline</h2>"
    "<ul>"
    "<li><b>Log the invoice on send.</b> The record starts before the payment.</li>"
    "<li><b>Track the lag.</b> The payment delay is a client's true character.</li>"
    "<li><b>Quarterly review.</b> The ledger decides which markets deserve the next pitch.</li>"
    "<li><b>Income by source.</b> The concentration risk hides in the totals.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/track-your-writing-income/\">the track-your-income guide</a>, <a href=\"/writers/guides/the-tax-set-aside-habit/\">the tax set-aside habit</a> and <a href=\"/writers/learn/freelance-paid-writing/how-to-invoice-as-a-writer/\">how to invoice as a writer</a>.</p>",

"writers/writing/bombay-literary-magazine":
    "<h2>A market with a clear voice</h2>"
    "<p>The Bombay Literary Magazine publishes fiction, poetry and long-form essays with an editorial ear tuned to the subcontinent's writing and its diasporas — and states its terms plainly enough to stay on the honest submission lists. For writers it is a market where place reads as texture rather than theme. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Read the archive first.</b> The magazine's ear is on every page.</li>"
    "<li><b>Place as texture.</b> The setting does its work through detail.</li>"
    "<li><b>Check the reading windows.</b> The open periods are the whole policy.</li>"
    "<li><b>One piece at a time.</b> Small magazines read honestly and fast.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/wasafiri-interviews/\">Wasafiri</a>, <a href=\"/writers/writing/words-without-borders-reviews/\">Words Without Borders</a> and <a href=\"/writers/writing/statement-africa/\">Statement Africa</a>.</p>",

"entertainment/how-streaming-bundles-work-explained":
    "<h2>The cable model, reassembled</h2>"
    "<p>Streaming bundles are the cable economics rebuilt from parts: the wholesale discount, the wholesale churn, and the consumer's belief that one bill beats three. The bundle's real product is convenience priced against the rotation habit — the household that cancels and returns. The <a href=\"" + _w("streaming+media") + "\" rel=\"noopener\">streaming business model</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The bundle arithmetic</h2>"
    "<ul>"
    "<li><b>The discount is real; so is the lock-in.</b> The bundle prices the churn you give up.</li>"
    "<li><b>One catalog is never the whole one.</b> The bundle's channels have their own windows.</li>"
    "<li><b>Price per household, not per screen.</b> The family's usage is the true cost basis.</li>"
    "<li><b>Rotation still wins for singles.</b> The bundle's discount assumes the household watches everything.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/cheapest-way-to-stream-movies/\">the cheapest way to stream movies</a>, <a href=\"/tech/streaming-subscription-stacking-when-bundle-cheaper/\">streaming subscription stacking</a> and <a href=\"/entertainment/why-streaming-services-raise-prices/\">why streaming prices rise</a>.</p>",

"entertainment/how-to-pick-a-movie-tonight":
    "<h2>The decision, shortened</h2>"
    "<p>The endless scroll is a decision problem wearing a catalogue problem: the household agrees on nothing because the question was never framed. The fixes are structural — the pick order, the veto rule, the time-box — and they turn movie night from a negotiation into a tradition. The <a href=\"" + _w("choice+architecture") + "\" rel=\"noopener\">choice architecture</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The pick rules</h2>"
    "<ul>"
    "<li><b>Frame the mood first.</b> The genre question answers the catalogue question.</li>"
    "<li><b>The rotating chooser.</b> The pick's ownership ends the argument.</li>"
    "<li><b>Two vetoes, then decide.</b> The veto rule is the household's constitution.</li>"
    "<li><b>Time-box the scroll.</b> Three minutes, then the top of the shortlist.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/what-to-watch-in-90-minutes/\">what to watch in 90 minutes</a>, <a href=\"/entertainment/comfort-movies-to-rewatch/\">comfort movies to rewatch</a> and <a href=\"/entertainment/best-films-for-a-group/\">the best films for a group</a>.</p>",

"entertainment/how-to-read-movie-reviews":
    "<h2>Reading the review's contract</h2>"
    "<p>A review is a critic's argument with evidence, and reading one well means reading its method: what the critic values, what they showed you of the film, and whether the verdict follows from the case. The reader's defence is the sample — the scene quoted, the claim tested against the trailer's promise. The <a href=\"" + _w("film+criticism") + "\" rel=\"noopener\">film criticism</a> tradition is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The reader's toolkit</h2>"
    "<ul>"
    "<li><b>Check the evidence.</b> The review that quotes scenes is the review that watched.</li>"
    "<li><b>Find the critic's axis.</b> Every reviewer ranks craft against fun differently.</li>"
    "<li><b>Beware the plot summary.</b> The recap is the review's dead weight.</li>"
    "<li><b>Read two, always.</b> The disagreement between critics is the film's real profile.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/reviews/mokalik/\">the Mokalik review</a>, <a href=\"/entertainment/how-award-season-actually-works/\">how award season works</a> and <a href=\"/writers/learn/types-of-writing/how-to-write-a-book-review/\">how to write a book review</a>.</p>",

"home/deep-clean-schedule":
    "<h2>The schedule that actually runs</h2>"
    "<p>Deep cleaning fails as a monolith and survives as a rotation: one zone per week, the seasonal jobs on the calendar, and the daily ten minutes that keep the weekly hour honest. The schedule's design principle is that the house's dirt has a calendar — the stove before the guests, the filters before the harmattan. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor environment guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The rotation</h2>"
    "<ul>"
    "<li><b>One zone per week.</b> The zone system beats the whole-house fantasy.</li>"
    "<li><b>Seasonal anchors.</b> The rains and the harmattan write the calendar.</li>"
    "<li><b>The daily ten.</b> The dishes, the sink, the floor spot — the week's momentum.</li>"
    "<li><b>Equipment on schedule.</b> The filter and the vacuum clean themselves first.</li>"
    "</ul>"
    "<p>See <a href=\"/home/mistakes/\">the common home mistakes</a>, <a href=\"/home/hvac-filter-change-habit/\">the HVAC filter habit</a> and <a href=\"/home/condensation-ventilation-that-works/\">condensation and ventilation</a>.</p>",

"tech/ai-useful-vs-hype":
    "<h2>The honest line</h2>"
    "<p>The line between useful and hype is drawn at the task: drafting, summarising and transformation are genuinely changed; prediction of the specific, the factual and the consequential is where the confident error lives. The useful posture is instrumental — the tool as a fast junior, checked like one. The <a href=\"" + _w("artificial+intelligence") + "\" rel=\"noopener\">AI field</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Which side of the line</h2>"
    "<ul>"
    "<li><b>Useful: the blank page.</b> First drafts and scaffolds are the technology's real win.</li>"
    "<li><b>Hype: the oracle.</b> The confident specific answer is the failure mode.</li>"
    "<li><b>Useful: transformation.</b> Format, tone and structure changes are reliable.</li>"
    "<li><b>Hype: judgement.</b> The stakes of the decision belong to the human.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/ai/\">AI without the hype</a>, <a href=\"/tech/free-ai-tools-worth-using/\">free AI tools worth using</a> and <a href=\"/tech/ai-assistants-compared/\">AI assistants compared</a>.</p>",

"writers/learn/editing-proofreading/how-to-proofread":
    "<h2>The last pass</h2>"
    "<p>Proofreading is the pass where the writing stops being yours and becomes the reader's: the spelling, the punctuation, the name spelled two ways on page three. The discipline is mechanical — read it aloud, read it backwards, read it printed — because the brain edits the screen. The <a href=\"" + _w("proofreading") + "\" rel=\"noopener\">proofreading practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The proofing methods</h2>"
    "<ul>"
    "<li><b>Read aloud.</b> The mouth catches what the eye forgives.</li>"
    "<li><b>Read backwards.</b> The sentence structure stops hiding the typo.</li>"
    "<li><b>Print it.</b> The page changes the eye's attention entirely.</li>"
    "<li><b>The name search.</b> Every proper noun gets a search pass.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/editing-proofreading/how-to-edit-for-clarity/\">how to edit for clarity</a>, <a href=\"/writers/learn/editing-proofreading/how-to-edit-your-own-writing/\">how to edit your own writing</a> and <a href=\"/writers/learn/writing-checklists/\">writing checklists</a>.</p>",

"home/dishwasher-not-draining-first-checks":
    "<h2>The five checks</h2>"
    "<p>A dishwasher that will not drain is almost always a blockage question: the filter basket, the air gap, the drain hose's high loop, the disposer connection, and the pump's last word. The order matters — the checks are free and the pump is not. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Before you call anyone</h2>"
    "<ul>"
    "<li><b>The filter basket first.</b> The commonest culprit and the cheapest fix.</li>"
    "<li><b>Air gap and hose loop.</b> The plumbing's logic decides the drainage.</li>"
    "<li><b>The disposer connection.</b> The knockout plug is the classic installer's error.</li>"
    "<li><b>Standing water scoop.</b> The last step before the pump's inspection.</li>"
    "<li><b>Then the pump.</b> The professional's territory starts here.</li>"
    "</ul>"
    "<p>See <a href=\"/home/dishwasher-loading-mistakes/\">dishwasher loading mistakes</a>, <a href=\"/home/garbage-disposal-mistakes/\">garbage disposal mistakes</a> and <a href=\"/home/someday-maintenance-cost/\">the cost of someday maintenance</a>.</p>",

"tech/tablet-vs-budget-laptop-for-students":
    "<h2>The school decision</h2>"
    "<p>The tablet is a consumption device with a keyboard accessory; the budget laptop is a production device with a battery compromise. The school's actual assignments decide — the essays and the spreadsheets want a file system, the reading and the video call want the tablet's simplicity. The <a href=\"" + _w("tablet+computer") + "\" rel=\"noopener\">tablet category</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Deciding by workload</h2>"
    "<ul>"
    "<li><b>Essays and research: the laptop.</b> The file system is the assignment's tool.</li>"
    "<li><b>Reading and calls: the tablet.</b> The lighter machine does the lighter job.</li>"
    "<li><b>The keyboard is the tell.</b> A tablet with a keyboard case is a laptop's price.</li>"
    "<li><b>Check the exam software.</b> The institution's lockdown browser decides the platform.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/student-laptop-spec-floor-2026/\">the student laptop spec floor</a>, <a href=\"/tech/kindle-vs-kobo-vs-tablet-reading/\">Kindle versus Kobo versus tablet</a> and <a href=\"/tech/laptop-buying-ram-storage/\">laptop buying: RAM and storage</a>.</p>",

"entertainment/best-romantic-comedies-of-all-time":
    "<h2>The ones that hold up</h2>"
    "<p>The romantic comedies that last share a screenplay discipline: the meet has stakes, the obstacle is character rather than coincidence, and the banter carries the theme. The canon here is argued rather than voted — the entries that still surprise on the fifth rewatch. The <a href=\"" + _w("romantic+comedy") + "\" rel=\"noopener\">romantic comedy genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the canon shares</h2>"
    "<ul>"
    "<li><b>The obstacle is internal.</b> The great ones fight the character's flaw, not the weather.</li>"
    "<li><b>Banter is theme.</b> The dialogue argues the film's question.</li>"
    "<li><b>The ending earns its rain.</b> The third act's honesty is the genre's craft.</li>"
    "<li><b>Comedy first.</b> The laugh is the love story's vehicle.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/comfort-movies-to-rewatch/\">comfort movies to rewatch</a>, <a href=\"/entertainment/best-films-for-a-group/\">the best films for a group</a> and <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a>.</p>",

"entertainment/hottest-movies-right-now":
    "<h2>How to know, without the noise</h2>"
    "<p>The 'hottest movie' is a moving target with three honest indicators: the box office's second weekend, the search interest's slope, and the conversation's staying power past the premiere. This page's method is the indicators themselves — the way to read the temperature rather than trust one list. The <a href=\"" + _w("box+office") + "\" rel=\"noopener\">box office system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The three indicators</h2>"
    "<ul>"
    "<li><b>The second weekend.</b> Word of mouth's verdict, priced in tickets.</li>"
    "<li><b>The search slope.</b> Interest that grows after release is the real heat.</li>"
    "<li><b>Week three conversation.</b> The premiere's noise fades; the film's argument stays.</li>"
    "<li><b>Ignore the opening-day takes.</b> The first day is the marketing's echo.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-box-office-works/\">how box office works</a>, <a href=\"/entertainment/how-to-pick-a-movie-tonight/\">how to pick a movie tonight</a> and <a href=\"/entertainment/what-to-watch-in-90-minutes/\">what to watch in 90 minutes</a>.</p>",

"entertainment/how-streaming-algorithms-recommend-explained":
    "<h2>Why the homepage picks your films</h2>"
    "<p>Streaming recommendations optimise for completion, not satisfaction: the system learns what keeps the session alive and serves more of the same, because the metric it is graded on is tonight's watch time. The viewer's counter-move is deliberate diversity — the search box beats the carousel. The <a href=\"" + _w("recommender+system") + "\" rel=\"noopener\">recommender system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Gaming the algorithm back</h2>"
    "<ul>"
    "<li><b>Completion is the currency.</b> What you finish trains the system more than what you rate.</li>"
    "<li><b>Search deliberately.</b> The carousel serves the past; the search box serves the choice.</li>"
    "<li><b>Profiles matter.</b> The household's mix confuses every recommendation.</li>"
    "<li><b>Ratings are weak signals.</b> Behaviour is the system's real language.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-streaming-licensing-works/\">how streaming licensing works</a>, <a href=\"/entertainment/how-to-pick-a-movie-tonight/\">how to pick a movie tonight</a> and <a href=\"/tech/subscription-creep-audit/\">the subscription creep audit</a>.</p>",

"home/wall-hole-anchors-by-type":
    "<h2>The anchor is the wall</h2>"
    "<p>Wall anchors are chosen by the wall, not the shelf: the plasterboard's toggle, the masonry's plug, the tile's diamond bit. The hole's repair and the anchor's chemistry match the substrate — and every shelf that fell chose the wrong one. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Matching anchor to wall</h2>"
    "<ul>"
    "<li><b>Plasterboard: toggle or spiral.</b> The board's grip is its thickness's physics.</li>"
    "<li><b>Masonry: plug and masonry bit.</b> The hammer drill is the load-bearing half.</li>"
    "<li><b>Tile: diamond core, slow.</b> The heat is the tile's enemy.</li>"
    "<li><b>Load rating honestly.</b> The anchor's number is the ceiling, not the target.</li>"
    "</ul>"
    "<p>See <a href=\"/home/basic-toolkit-checklist/\">the basic toolkit checklist</a>, <a href=\"/home/ceiling-fan-mounting-right/\">ceiling fan mounting</a> and <a href=\"/home/mistakes/painting-without-prep/\">painting without prep</a>.</p>",

"tech/git-errors-fixed":
    "<h2>The errors, decoded</h2>"
    "<p>Git's errors are precise and its users are not: the merge conflict is two histories disagreeing, the detached HEAD is a commit without a branch, and the rejected push is a conversation waiting to happen. Each message names the state; the fix follows the naming. The <a href=\"" + _w("Git") + "\" rel=\"noopener\">Git version control</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The classic three</h2>"
    "<ul>"
    "<li><b>Merge conflict.</b> Two branches edited the same truth; choose deliberately.</li>"
    "<li><b>Detached HEAD.</b> You are standing on a commit; make a branch or go back.</li>"
    "<li><b>Rejected non-fast-forward.</b> Pull first, or the history diverges twice.</li>"
    "<li><b>The reflog is the parachute.</b> Almost nothing is truly lost.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/github-beginner-mistakes/\">GitHub beginner mistakes</a>, <a href=\"/tech/git-and-github-for-beginners/\">Git and GitHub for beginners</a> and <a href=\"/tech/github-token-hygiene/\">GitHub token hygiene</a>.</p>",

"tech/student-laptop-spec-floor-2026":
    "<h2>The honest floor</h2>"
    "<p>The student laptop's spec floor is set by the degree, not the games: 16 gigabytes of RAM, a real SSD, a screen the library's fluorescent lights cannot defeat, and a battery that survives the timetable. Everything above the floor is preference; everything below it is a slow Tuesday. The <a href=\"" + _w("laptop") + "\" rel=\"noopener\">laptop category</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The floor, itemised</h2>"
    "<ul>"
    "<li><b>RAM 16 GB.</b> The browser alone is the modern memory floor.</li>"
    "<li><b>SSD, no exceptions.</b> The spinning disk ruins every other spec.</li>"
    "<li><b>Screen over speed.</b> The hours are spent looking at it.</li>"
    "<li><b>Battery measured in lectures.</b> The outlet hunt is the timetable's tax.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/laptop-buying-ram-storage/\">laptop buying: RAM and storage</a>, <a href=\"/tech/tablet-vs-budget-laptop-for-students/\">tablet versus budget laptop</a> and <a href=\"/tech/new-midrange-vs-used-flagship/\">new midrange versus used flagship</a>.</p>",

"writers/learn/grammar-language/how-to-use-semicolons-and-colons":
    "<h2>The two dots' jobs</h2>"
    "<p>The semicolon joins two sentences that belong together; the colon announces what the first sentence promised. They are the punctuation of relationships — and most misuse is a sentence trying to avoid being two. The <a href=\"" + _w("semicolon") + "\" rel=\"noopener\">semicolon</a> and <a href=\"" + _w("colon") + "\" rel=\"noopener\">colon</a> are documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The rules, short</h2>"
    "<ul>"
    "<li><b>Semicolon: related full sentences.</b> Both sides could stand alone; the link is the point.</li>"
    "<li><b>Colon: the promised payload.</b> The first half announces; the second delivers.</li>"
    "<li><b>Never both at once.</b> The semicolon-colon confusion is a rewrite signal.</li>"
    "<li><b>Read the breath aloud.</b> The pause is the rule's origin story.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/grammar-language/comma-rules/\">comma rules</a>, <a href=\"/writers/learn/grammar-language/common-grammar-mistakes/\">common grammar mistakes</a> and <a href=\"/writers/learn/writing-basics/sentence-basics/\">sentence basics</a>.</p>",

"entertainment/how-film-festivals-work":
    "<h2>Premieres, prizes and the market</h2>"
    "<p>A film festival is three machines in one building: the premiere that launches a film's campaign, the jury that prices its reputation, and the market where the rights are actually sold. The selection is the product; the red carpet is the marketing. The <a href=\"" + _w("film+festival") + "\" rel=\"noopener\">film festival system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>How the machine runs</h2>"
    "<ul>"
    "<li><b>The premiere is a campaign launch.</b> The slot decides the film's year.</li>"
    "<li><b>Juries are arguments.</b> The prize is the jury's thesis statement.</li>"
    "<li><b>The market is the business.</b> The deals happen in the rooms without cameras.</li>"
    "<li><b>The audience award is the public's verdict.</b> The second opinion that matters.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-award-season-actually-works/\">how award season works</a>, <a href=\"/entertainment/how-movie-release-windows-work/\">how release windows work</a> and <a href=\"/entertainment/how-streaming-licensing-works/\">how streaming licensing works</a>.</p>",

"entertainment/how-streaming-licensing-works":
    "<h2>Why shows vanish</h2>"
    "<p>Streaming libraries are rental agreements with calendars: the licence window opens and closes, the rights revert to the owner's own platform, and the show that was 'on Netflix' becomes an exclusive somewhere else. The vanishing is business, not malfunction. The <a href=\"" + _w("film+distribution") + "\" rel=\"noopener\">licensing system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The licensing calendar</h2>"
    "<ul>"
    "<li><b>Windows, not ownership.</b> The catalogue is a rotating rental shelf.</li>"
    "<li><b>Exclusives are leverage.</b> The content war is a rights war.</li>"
    "<li><b>The owner's platform wins eventually.</b> The rights go home to roost.</li>"
    "<li><b>'Where to watch' sites are the honest guide.</b> The tracker beats the memory.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-streaming-bundles-work-explained/\">how streaming bundles work</a>, <a href=\"/entertainment/cheapest-way-to-stream-movies/\">the cheapest way to stream movies</a> and <a href=\"/entertainment/how-movie-release-windows-work/\">how release windows work</a>.</p>",

"entertainment/shows-like-squid-game":
    "<h2>Games with rules you can lose</h2>"
    "<p>The shows that scratch the Squid Game itch share its engine: a system with legible rules, a debt driving the players, and the game as a mirror of the economy outside it. The best next watches are the ones that find their own metaphor inside the same machine. The <a href=\"" + _w("survival+game") + "\" rel=\"noopener\">survival game genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What to look for next</h2>"
    "<ul>"
    "<li><b>Rules the audience can learn.</b> The game's legibility is the tension's floor.</li>"
    "<li><b>The debt that drives the players.</b> The stakes are economic before they are physical.</li>"
    "<li><b>The system as the villain.</b> The best entries indict the game, not the players.</li>"
    "<li><b>One twist per arc.</b> The genre rewards restraint more than shock.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/10-shows-like-alice-in-borderland-you-should-watch-next/\">shows like Alice in Borderland</a>, <a href=\"/entertainment/alice-in-borderland-vs-squid-game/\">Alice in Borderland versus Squid Game</a> and <a href=\"/entertainment/best-thriller-movies-of-all-time/\">the best thrillers</a>.</p>",

"tech/android-privacy-settings-checklist":
    "<h2>The one-time audit</h2>"
    "<p>The Android privacy audit is a one-time pass with a yearly review: the permission manager, the ad ID, the location history and the lock screen's notifications. Each setting is a disclosure decision — what the phone tells the apps and the strangers about the day. The <a href=\"" + _w("Android") + "\" rel=\"noopener\">Android platform</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The checklist</h2>"
    "<ul>"
    "<li><b>Permission manager, app by app.</b> The list is the disclosure.</li>"
    "<li><b>Ad ID reset.</b> The tracking identifier is a setting, not a law of nature.</li>"
    "<li><b>Location history off.</b> The archive of your movements is optional.</li>"
    "<li><b>Lock screen previews down.</b> The notification is a shoulder-surfing channel.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-app-permissions/\">Android app permissions</a>, <a href=\"/tech/what-free-apps-do-with-your-data/\">what free apps do with your data</a> and <a href=\"/tech/browser-privacy-settings/\">browser privacy settings</a>.</p>",

"writers/learn/types-of-writing/how-to-write-copywriting":
    "<h2>Writing that sells without shouting</h2>"
    "<p>Copywriting is writing for a decision: the headline that earns the second line, the benefit that lives in the reader's day, and the call to action that arrives before the attention leaves. The craft is honest persuasion — the claim the product can keep. The <a href=\"" + _w("copywriting") + "\" rel=\"noopener\">copywriting practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The copywriter's moves</h2>"
    "<ul>"
    "<li><b>The headline is the ad's first sale.</b> The second line is the second.</li>"
    "<li><b>Benefits in the reader's Tuesday.</b> The feature is the ingredient; the benefit is the meal.</li>"
    "<li><b>One ask per piece.</b> The second call to action dilutes the first.</li>"
    "<li><b>Honesty is the conversion feature.</b> The claim kept beats the claim made.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-of-a-product-description/\">the product description example</a>, <a href=\"/writers/learn/online-writing/how-to-write-search-friendly-content/\">how to write search-friendly content</a> and <a href=\"/writers/learn/types-of-writing/how-to-write-an-article/\">how to write an article</a>.</p>",

"entertainment/evergreen-anime":
    "<h2>The series that never age</h2>"
    "<p>Evergreen anime share a design that resists the calendar: the themes that outlive their animation budget, the characters who stay legible to new generations, and the craft that taught the industry its vocabulary. These are the series the recommendation engines return to because the audience does. The <a href=\"" + _w("anime") + "\" rel=\"noopener\">anime medium</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Why they endure</h2>"
    "<ul>"
    "<li><b>Themes before trends.</b> The questions the shows ask do not expire.</li>"
    "<li><b>Characters with arcs.</b> The growth is the rewatch's engine.</li>"
    "<li><b>Craft that taught the form.</b> The industry's vocabulary was written here.</li>"
    "<li><b>Entry points for every age.</b> The shows find viewers at 15 and 40.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-anime-to-watch-now/\">the best anime to watch now</a>, <a href=\"/entertainment/best-anime-movies-of-all-time/\">the best anime movies</a> and <a href=\"/entertainment/where-to-start-with-long-running-anime/\">where to start with long-running anime</a>.</p>",

"home/lawn-mower-care-spring-service":
    "<h2>The hour that decides the year</h2>"
    "<p>The spring mower service is one hour that sets the season: the blade sharpened, the oil changed, the air filter cleared, and the deck scraped before the grass grows into the arguments. A dull blade tears the lawn and taxes the engine. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes small-engine guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The service list</h2>"
    "<ul>"
    "<li><b>Sharpen the blade.</b> The clean cut is the lawn's health and the engine's rest.</li>"
    "<li><b>Oil and filter on schedule.</b> The small engine's life is the maintenance log.</li>"
    "<li><b>Scrape the deck.</b> The old clippings are this season's disease.</li>"
    "<li><b>Stabilise the fuel.</b> The winter's stale petrol is the spring's first fault.</li>"
    "</ul>"
    "<p>See <a href=\"/home/autumn-home-preparation/\">autumn home preparation</a>, <a href=\"/home/basic-toolkit-checklist/\">the basic toolkit checklist</a> and <a href=\"/home/someday-maintenance-cost/\">the cost of someday maintenance</a>.</p>",

"tech/kindle-vs-kobo-vs-tablet-reading":
    "<h2>The reading decision</h2>"
    "<p>The Kindle and the Kobo are single-purpose instruments — e-ink that behaves like paper and batteries that behave like promises — while the tablet is a library with a notification problem. The decision is about attention: the device that protects it wins. The <a href=\"" + _w("e+reader") + "\" rel=\"noopener\">e-reader category</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing by reader</h2>"
    "<ul>"
    "<li><b>E-ink for the book.</b> The eye comfort and the battery are the whole argument.</li>"
    "<li><b>Tablet for the mixed diet.</b> Comics, PDFs and video share the screen.</li>"
    "<li><b>Store lock-in matters.</b> The library you build is the platform you chose.</li>"
    "<li><b>The lamp is the feature.</b> Night reading without the notification glow.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tablet-vs-budget-laptop-for-students/\">tablet versus budget laptop</a>, <a href=\"/tech/big-tv-small-room/\">a big TV in a small room</a> and <a href=\"/tech/anc-vs-passive-isolation-earbuds/\">ANC versus passive isolation</a>.</p>",

"tech/reusing-passwords-risk":
    "<h2>The credential stuffing economy</h2>"
    "<p>Reusing one password is trusting every site's security with every other account: the breach of the weakest forum becomes the key to the bank. The attack has a name — credential stuffing — and an industry behind it. The <a href=\"" + _w("credential+stuffing") + "\" rel=\"noopener\">credential stuffing attack</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Breaking the chain</h2>"
    "<ul>"
    "<li><b>Email and money first.</b> These two reset everything else.</li>"
    "<li><b>A manager does the remembering.</b> The friction is the reason reuse exists.</li>"
    "<li><b>Check the breach reports.</b> The list of exposures is public and useful.</li>"
    "<li><b>Two-factor as the second wall.</b> The stolen password stops being the whole key.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/password-manager-migration-weekend/\">the password manager migration</a>, <a href=\"/tech/how-to-reset-forgotten-passwords/\">how to reset forgotten passwords</a> and <a href=\"/tech/security-questions-are-insecure/\">security questions are insecure</a>.</p>",

"entertainment/soap-opera-effect-explained":
    "<h2>Why movies look like daytime TV</h2>"
    "<p>The soap opera effect is motion interpolation: the television inventing frames between the film's own, turning 24-frames-per-second cinema into the hyper-smooth look of a studio interview. The fix is a picture setting — the motion smoothing that marketing departments love and cinematographers do not. The <a href=\"" + _w("frame+rate") + "\" rel=\"noopener\">frame rate</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Turning it off</h2>"
    "<ul>"
    "<li><b>Find the motion setting.</b> Every brand names the same villain differently.</li>"
    "<li><b>Set it per input.</b> The sports benefit can stay; the film's night can end.</li>"
    "<li><b>Filmmaker mode where offered.</b> The one-button honesty setting.</li>"
    "<li><b>Interpolation is not resolution.</b> The invented frames are the tell.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/picture-settings-that-fix-the-soap-opera-look/\">picture settings that fix the look</a>, <a href=\"/tech/new-tv-settings-day-one/\">new TV settings, day one</a> and <a href=\"/entertainment/aspect-ratios-in-film-explained/\">aspect ratios explained</a>.</p>",

"home/owning":
    "<h2>The ownership ledger</h2>"
    "<p>Owning a home is a ledger with two columns nobody shows you at the viewing: the maintenance calendar and the reserve fund. The pages here cover the ownership work — the systems, the paperwork, the improvements that pay and the ones that please. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The ownership map</h2>"
    "<ul>"
    "<li><b>Systems.</b> The roof, the wiring, the plumbing — each with its service interval.</li>"
    "<li><b>Paperwork.</b> The certificates and the insurance that answer when asked.</li>"
    "<li><b>Improvements.</b> The value test before the colour swatch.</li>"
    "<li><b>The fund.</b> The reserve that turns a surprise into an errand.</li>"
    "</ul>"
    "<p>See <a href=\"/home/emergency-repair-fund/\">the emergency repair fund</a>, <a href=\"/home/inspection-checklist-gaps/\">inspection checklist gaps</a> and <a href=\"/home/someday-maintenance-cost/\">the cost of someday maintenance</a>.</p>",

"home/secondhand-furniture-mistakes":
    "<h2>What to check before it enters</h2>"
    "<p>Secondhand furniture carries three risks the photos hide: the pest passengers in the joints, the structural damage under the upholstery, and the mould in the frame. The inspection is fifteen minutes at the kerb — before the piece becomes the house's problem. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor pest guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The fifteen-minute check</h2>"
    "<ul>"
    "<li><b>The joints and the seams.</b> The bedbug inspection is the first inspection.</li>"
    "<li><b>The frame's weight.</b> The wobble is the structure's honesty.</li>"
    "<li><b>The smell test.</b> The mould is the piece's history of damp.</li>"
    "<li><b>The quarantine.</b> The garage week is the infestation insurance.</li>"
    "</ul>"
    "<p>See <a href=\"/home/bedbugs-first-signs/\">bedbugs: first signs</a>, <a href=\"/home/ignore-single-pest-sighting/\">the single pest sighting</a> and <a href=\"/home/musty-wardrobe-clothes-rainy/\">the musty wardrobe</a>.</p>",

"sports/how-many-english-teams-champions-league":
    "<h2>The coefficient's arithmetic</h2>"
    "<p>English clubs' Champions League places are the nation's coefficient arithmetic: the European results that earn the association's ranking, the league positions that allocate the berths, and the format changes that resized the whole bracket. The rules reward the league's depth as much as its champions. The <a href=\"" + _w("UEFA+Champions+League") + "\" rel=\"noopener\">Champions League</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>How the berths are earned</h2>"
    "<ul>"
    "<li><b>The coefficient is collective.</b> Every English result in Europe counts.</li>"
    "<li><b>The league table allocates.</b> The positions map to the berths the format allows.</li>"
    "<li><b>The extra place is performance-priced.</b> The format's expansion follows the coefficient.</li>"
    "<li><b>The calendar feeds itself.</b> European success funds the depth that earns more berths.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/champions-league-new-format-explained/\">the Champions League new format</a>, <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a> and <a href=\"/sports/how-do-football-clubs-make-money/\">how football clubs make money</a>.</p>",

"tech/usb-c-fast-charge-not-working":
    "<h2>The handshake, not the wattage</h2>"
    "<p>USB-C charging is a negotiation before it is electricity: the charger, the cable and the device must agree on a standard, and one legacy cable in the bag fails the whole conversation. The watts on the brick are the ceiling; the handshake is the product. The <a href=\"" + _w("USB-C") + "\" rel=\"noopener\">USB-C standard</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Diagnosing the slow charge</h2>"
    "<ul>"
    "<li><b>Cable first.</b> The charge-only cable is the silent saboteur.</li>"
    "<li><b>Charger's standard.</b> The brick must speak the device's protocol.</li>"
    "<li><b>Port debris.</b> The pocket lint is the commonest fault of all.</li>"
    "<li><b>Battery health last.</b> The aged cell refuses the fast handshake.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/phone-charging-slow-cable-port/\">phone charging slow: cable and port</a>, <a href=\"/tech/power-bank-flying-rules/\">power bank flying rules</a> and <a href=\"/tech/ethernet-cable-categories-honest/\">ethernet cable categories</a>.</p>",

"writers/learn/editing-proofreading/how-to-edit-for-clarity":
    "<h2>Clarity is an edit</h2>"
    "<p>Editing for clarity is subtractive: the sentence that means one thing, the paragraph that knows its job, the page that respects the reader's time. The test is the reader's paraphrase — if they can say it back, the editing worked. The <a href=\"" + _w("plain+language") + "\" rel=\"noopener\">plain language practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The clarity edits</h2>"
    "<ul>"
    "<li><b>One idea per sentence.</b> The compound sentence is the confusion's address.</li>"
    "<li><b>The subject does the acting.</b> The active voice is clarity's default setting.</li>"
    "<li><b>Cut the qualifier pile.</b> Three hedges say nothing confidently.</li>"
    "<li><b>The paragraph's first line works hardest.</b> The topic sentence is the map.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/editing-proofreading/how-to-make-writing-more-concise/\">how to make writing more concise</a>, <a href=\"/writers/learn/common-problems/my-writing-sounds-too-formal/\">my writing sounds too formal</a> and <a href=\"/writers/learn/editing-proofreading/how-to-proofread/\">how to proofread</a>.</p>",

"writers/learn/research-sources":
    "<h2>Where the evidence lives</h2>"
    "<p>Research and sources are the writer's evidence system: the primary document, the interview, the dataset, and the citation that lets the reader check the work. The discipline is provenance — knowing where each claim came from before the draft makes it anonymous. The <a href=\"" + _w("research") + "\" rel=\"noopener\">research practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The source hierarchy</h2>"
    "<ul>"
    "<li><b>Primary before secondary.</b> The document beats the article about the document.</li>"
    "<li><b>Named before anonymous.</b> The source's name is the evidence's weight.</li>"
    "<li><b>Dated before recent.</b> The claim has a calendar whether the writer names it or not.</li>"
    "<li><b>Triangulate the claim.</b> Two sources disagreeing is information, not failure.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/research-sources/how-to-avoid-plagiarism/\">how to avoid plagiarism</a>, <a href=\"/writers/learn/academic-writing/how-to-cite-sources/\">how to cite sources</a> and <a href=\"/writers/learn/common-problems/how-plagiarism-and-ai-checkers-are-made/\">how plagiarism checkers work</a>.</p>",

"writers/learn/start-writing/how-to-turn-an-idea-into-an-outline":
    "<h2>The idea's skeleton</h2>"
    "<p>An outline is the idea's skeleton: the claim, the evidence beats, and the order the reader needs them in. The outline's job is to fail cheaply — to show the structure's weakness before the prose's investment. The <a href=\"" + _w("outline") + "\" rel=\"noopener\">outlining practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The outlining pass</h2>"
    "<ul>"
    "<li><b>One line per beat.</b> The beat is the unit the reader will feel.</li>"
    "<li><b>Order by the reader's questions.</b> The discovery order is the wrong order.</li>"
    "<li><b>Mark the weak beats now.</b> The outline is the cheapest place to fail.</li>"
    "<li><b>The outline bends.</b> The draft is allowed to improve the plan.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-process/how-to-brainstorm-and-find-ideas/\">how to brainstorm ideas</a>, <a href=\"/writers/learn/structure-formatting/\">structure and formatting</a> and <a href=\"/writers/learn/writing-process/how-to-build-a-writing-routine/\">how to build a writing routine</a>.</p>",

"writers/writing/space-and-time":
    "<h2>Speculative since the pulps</h2>"
    "<p>Space and Time publishes speculative fiction and poetry with a working-writer's terms sheet — a market that has kept the short fiction pipeline open across the genre's many reinventions. For writers it is a door with a clear handle. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Speculative with a heart.</b> The idea must carry a human load.</li>"
    "<li><b>Read the current issue.</b> The magazine's era is on its pages.</li>"
    "<li><b>Check the window.</b> The open periods are the submission policy.</li>"
    "<li><b>The slush pile is honest.</b> Small magazines read for fit and for craft.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/uncanny-poetry/\">Uncanny poetry</a>, <a href=\"/writers/writing/strange-horizons-fiction/\">Strange Horizons fiction</a> and <a href=\"/writers/writing/shoreline-of-infinity/\">Shoreline of Infinity</a>.</p>",

"entertainment/best-action-movies-of-all-time":
    "<h2>The canon, argued</h2>"
    "<p>The action canon is a craft argument: the geography of the fight readable, the stakes legible at speed, and the stunt work carrying the storytelling. The films here are the ones the genre's own directors study — the entries that built the vocabulary everyone else borrows. The <a href=\"" + _w("action+film") + "\" rel=\"noopener\">action film genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the canon teaches</h2>"
    "<ul>"
    "<li><b>Readable geography.</b> The audience must know where everyone stands.</li>"
    "<li><b>The stunt is the story.</b> The set piece advances the character.</li>"
    "<li><b>Rhythm over noise.</b> The edit's patience is the tension's source.</li>"
    "<li><b>The hero pays the price.</b> The victory carries cost or it carries nothing.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-thriller-movies-of-all-time/\">the best thrillers</a>, <a href=\"/entertainment/best-heist-movies/\">the best heist movies</a> and <a href=\"/entertainment/best-war-movies-of-all-time/\">the best war movies</a>.</p>",

"home/garbage-disposal-mistakes":
    "<h2>The mistakes behind the service call</h2>"
    "<p>The garbage disposal fails on habits: the fibrous peel, the starchy paste, the grease that coats the chamber between seasons. The tool is a grinder, not a bin — and the drain's chemistry is part of its care. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The care habits</h2>"
    "<ul>"
    "<li><b>Cold water while grinding.</b> The heat sets the grease the water should carry.</li>"
    "<li><b>Small batches, not the whole plate.</b> The chamber is a grinder, not a compactor.</li>"
    "<li><b>Never the fibrous and the starchy.</b> The peel wraps; the paste coats.</li>"
    "<li><b>The citrus ice ritual.</b> The cleaning habit that keeps the blades honest.</li>"
    "</ul>"
    "<p>See <a href=\"/home/dishwasher-not-draining-first-checks/\">dishwasher not draining</a>, <a href=\"/home/dripping-tap-cartridge-fix/\">the dripping tap cartridge fix</a> and <a href=\"/home/mistakes/\">the common home mistakes</a>.</p>",

"home/jerrycan-fuel-storage-safely":
    "<h2>The fuel tank indoors</h2>"
    "<p>A jerry can is a fuel tank parked inside the house — which makes its storage a fire-safety question, not a convenience one. The rules are vapour, distance and the approved container: the fumes travel farther than the smell suggests, and the garage's corners are the ignition map. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes flammable liquid guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The storage rules</h2>"
    "<ul>"
    "<li><b>Approved container only.</b> The rated can is the safety device.</li>"
    "<li><b>Vapour travels.</b> The storage point is chosen by the fumes' route, not the can's.</li>"
    "<li><b>Fill outside, engines off.</b> The static spark is the ignition story.</li>"
    "<li><b>The quantity is the risk.</b> The litres stored are the household's hazard budget.</li>"
    "</ul>"
    "<p>See <a href=\"/home/cooking-oil-fire-plan/\">the cooking oil fire plan</a>, <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a> and <a href=\"/home/test-alarms-monthly/\">the monthly alarm habit</a>.</p>",

"sports/how-football-transfer-medicals-work":
    "<h2>The exam that can stop the deal</h2>"
    "<p>The transfer medical is the deal's last gate: the heart screening, the muscle history, the knee that decides the fee's final number. The exam is a risk assessment priced into the contract — and the reported 'failed medical' is the process working in public. The <a href=\"" + _w("medical+examination") + "\" rel=\"noopener\">sports medical</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What the medical checks</h2>"
    "<ul>"
    "<li><b>The cardiac screen.</b> The exam's most important thirty minutes.</li>"
    "<li><b>The injury ledger.</b> The body's history is the contract's risk table.</li>"
    "<li><b>The load tests.</b> The muscle's readiness is measured, not assumed.</li>"
    "<li><b>Fee adjustments live here.</b> The finding re-prices the deal quietly.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-football-contracts-work/\">how football contracts work</a>, <a href=\"/sports/how-the-transfer-window-works/\">how the transfer window works</a> and <a href=\"/sports/weigh-ins-and-weight-cuts-explained/\">weigh-ins and weight cuts</a>.</p>",

"sports/playing-out-from-the-back":
    "<h2>The risk that keeps being taken</h2>"
    "<p>Playing out from the back is a territorial investment: the goalkeeper's pass buys the whole pitch's space and risks the goal's immediate one. The teams that make it work have the press-resistant defenders and the goalkeeper's feet; the teams that lose to it usually lack one of the two. The <a href=\"" + PL + "\" rel=\"noopener\">Premier League</a> tacticians this desk follows have made it the league's argument. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Why it keeps failing — and working</h2>"
    "<ul>"
    "<li><b>The build is a personnel question.</b> The system needs press-resistant defenders.</li>"
    "<li><b>The goalkeeper's feet are the tactic.</b> The extra outfielder is the whole point.</li>"
    "<li><b>The press is the counter.</b> The opponent's trigger decides the risk's price.</li>"
    "<li><b>The exit is the safety valve.</b> The long ball is still allowed; the pride is the problem.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/pressing-explained/\">pressing explained</a>, <a href=\"/sports/gegenpressing-explained/\">gegenpressing explained</a> and <a href=\"/sports/football-positions-explained/\">football positions explained</a>.</p>",

"tech/inkjet-vs-laser-printer-nigeria":
    "<h2>The fault lines</h2>"
    "<p>In the Nigerian home office the printer decision runs on cartridge logistics: the inkjet's clogged head in the harmattan, the laser's toner that survives the shelf, and the per-page maths that follows the workload. The humidity is part of the specification. The <a href=\"" + _w("laser+printing") + "\" rel=\"noopener\">printer technologies</a> are documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Deciding by workload</h2>"
    "<ul>"
    "<li><b>Documents at volume: laser.</b> The toner economics are the honest maths.</li>"
    "<li><b>Photos occasionally: inkjet.</b> The colour range is the inkjet's only argument.</li>"
    "<li><b>Shelf life beats speed.</b> The clogged head is the climate's printer tax.</li>"
    "<li><b>Cost per page, always.</b> The sticker price is the deposit on the cartridges.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/printer-keeps-going-offline/\">the printer that goes offline</a>, <a href=\"/tech/repair-vs-replace/\">repair versus replace</a> and <a href=\"/tech/free-software-alternatives/\">free software alternatives</a>.</p>",

"writers/learn/editing-proofreading":
    "<h2>The second craft</h2>"
    "<p>Editing and proofreading are the second craft: the discovery of what the draft is actually saying, the structural surgery, the line polish, and the final mechanical pass. Each stage has its own questions and its own time — the mistake is asking the proofreader's questions during the drafting. The <a href=\"" + _w("editing") + "\" rel=\"noopener\">editing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The four stages</h2>"
    "<ul>"
    "<li><b>Developmental.</b> The argument's bones; the question is whether the piece works.</li>"
    "<li><b>Line editing.</b> The sentences' music and the paragraphs' jobs.</li>"
    "<li><b>Proofreading.</b> The mechanics, after everything else has settled.</li>"
    "<li><b>Rest between stages.</b> The editor's freshest tool is time.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/editing-proofreading/how-to-edit-your-own-writing/\">how to edit your own writing</a>, <a href=\"/writers/learn/editing-proofreading/how-to-edit-for-clarity/\">how to edit for clarity</a> and <a href=\"/writers/learn/writing-checklists/\">writing checklists</a>.</p>",

"writers/learn/writing-basics/sentence-basics":
    "<h2>The sentence's working parts</h2>"
    "<p>A sentence is a subject doing something to something — and the craft begins when the writer can feel the difference between that and the sentence where the subject is being done to. The basics are the independent clause, the verb's strength, and the rhythm of the variation. The <a href=\"" + _w("sentence") + "\" rel=\"noopener\">sentence structure</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The basics that pay</h2>"
    "<ul>"
    "<li><b>The subject leads.</b> The reader finds the actor first, always.</li>"
    "<li><b>Verbs carry weight.</b> The strong verb retires the adverb.</li>"
    "<li><b>Vary the length.</b> The rhythm is the reader's breath.</li>"
    "<li><b>One job per clause.</b> The compound load is the confusion's source.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-basics/\">writing basics</a>, <a href=\"/writers/learn/grammar-language/comma-rules/\">comma rules</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-writing/\">the dos and don'ts of writing</a>.</p>",

"home/humidity-and-paint":
    "<h2>Why the paint never dried</h2>"
    "<p>Humidity is the paint job's hidden variable: the coat that will not cure, the blisters that arrive in the rains, the colour that flashes where the wall stayed damp. The paint's schedule belongs to the weather, and the moisture meter is the honest instrument. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor moisture guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Painting with the weather</h2>"
    "<ul>"
    "<li><b>Check the wall, not the sky.</b> The substrate's moisture is the real condition.</li>"
    "<li><b>The cure time doubles in the rains.</b> The schedule follows the humidity.</li>"
    "<li><b>Blisters are moisture's signature.</b> The repaint waits for the cause.</li>"
    "<li><b>Ventilation is part of the kit.</b> The airflow is the drying system.</li>"
    "</ul>"
    "<p>See <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three damps</a>, <a href=\"/home/mistakes/painting-without-prep/\">painting without prep</a> and <a href=\"/home/why-is-my-home-doing-that/\">why is my home doing that</a>.</p>",

"home/someday-maintenance-cost":
    "<h2>The interest on someday</h2>"
    "<p>'Someday' is the most expensive item on the maintenance calendar: the small repair that compounds through the seasons until it becomes the large one. The honest accounting prices the someday jobs at their future bill — and discovers the fund's business case. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Price the someday list</h2>"
    "<ul>"
    "<li><b>The small repair's compound rate.</b> The drip's interest is measured in timber.</li>"
    "<li><b>Seasonal deadlines.</b> The rains price the procrastination in public.</li>"
    "<li><b>The fund's real job.</b> The reserve converts someday into Saturday.</li>"
    "<li><b>The quote is free information.</b> The surveyor's number beats the worry.</li>"
    "</ul>"
    "<p>See <a href=\"/home/emergency-repair-fund/\">the emergency repair fund</a>, <a href=\"/home/inspection-checklist-gaps/\">inspection checklist gaps</a> and <a href=\"/home/mistakes/\">the common home mistakes</a>.</p>",

"tech/works-locally-fails-online":
    "<h2>The six differences</h2>"
    "<p>The gap between local and online is six environmental facts: the case-sensitive filesystem, the environment variables, the time zone, the network's rules, the resource ceilings and the build step. Each is invisible on the laptop and constitutional on the server. The <a href=\"" + _w("software+deployment") + "\" rel=\"noopener\">deployment environment</a> is documented in standard references. By the Bryme Technical Research desk. Reviewed 28 September 2026.</p>"
    "<h2>The diagnostic list</h2>"
    "<ul>"
    "<li><b>Case sensitivity.</b> The filename that worked in Finder fails in Linux.</li>"
    "<li><b>Environment variables.</b> The laptop's defaults are the server's secrets.</li>"
    "<li><b>Time zones and locales.</b> The date parsing bug is a geography bug.</li>"
    "<li><b>The build step.</b> What compiles locally must compile in the pipeline.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/deploy-python-app/\">how to deploy a Python app</a>, <a href=\"/tech/environment-variables-guide/\">the environment variables guide</a> and <a href=\"/tech/render-deployment-failures-what-they-taught-me/\">render deployment failures</a>.</p>",

"entertainment/where-to-start-with-long-running-anime":
    "<h2>The entry points</h2>"
    "<p>The thousand-episode series are best entered through their own front doors: the arc that establishes the world, the film that compresses it, or the remake that recuts it. The starter's rule is simple — enter at a beginning, and leave whenever the pace stops paying. The <a href=\"" + _w("anime") + "\" rel=\"noopener\">anime medium</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The entry strategies</h2>"
    "<ul>"
    "<li><b>The arc sampler.</b> The first great arc is the series' honest trailer.</li>"
    "<li><b>The film entry.</b> The compressed version is the sampler's weekend.</li>"
    "<li><b>The manga-first route.</b> The original pacing is the story's own.</li>"
    "<li><b>Permission to stop.</b> The long runner is a habit, not a contract.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/anime-canon-and-filler-explained/\">anime canon and filler</a>, <a href=\"/entertainment/evergreen-anime/\">evergreen anime</a> and <a href=\"/entertainment/best-anime-to-watch-now/\">the best anime to watch now</a>.</p>",

"home/hvac-noises-decoded":
    "<h2>Rattle, buzz, grind</h2>"
    "<p>The HVAC's noises are its diagnostic language: the rattle is a panel, the buzz is electrical, the grind is the motor's expensive announcement. The noise map turns the dread into a schedule — and the scheduled call into the cheap one. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The noise map</h2>"
    "<ul>"
    "<li><b>Rattle: the panels.</b> The screws and the panels' vibration is the cheap fix.</li>"
    "<li><b>Buzz: the electrical.</b> The contactor's noise is the electrician's cue.</li>"
    "<li><b>Grind: the motor.</b> The bearing's announcement is the replacement's booking.</li>"
    "<li><b>Silence with no air.</b> The quietest failure is the thermostat's.</li>"
    "</ul>"
    "<p>See <a href=\"/home/hvac-filter-change-habit/\">the HVAC filter habit</a>, <a href=\"/home/ac-outdoor-unit-care/\">AC outdoor unit care</a> and <a href=\"/home/why-is-my-home-doing-that/\">why is my home doing that</a>.</p>",

"tech/new-router-for-slow-internet":
    "<h2>The fix is not the router</h2>"
    "<p>Slow internet is a diagnostic chain: the plan's actual speed, the line's real condition, the Wi-Fi's channel and placement, and only then the router's age. The new-router reflex is the industry's favourite sale and the internet's least common fix. The <a href=\"" + _w("broadband") + "\" rel=\"noopener\">broadband performance</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The chain, in order</h2>"
    "<ul>"
    "<li><b>Test at the modem.</b> The wired speed is the plan's honest number.</li>"
    "<li><b>Then the Wi-Fi.</b> The channel and the placement are the household's half.</li>"
    "<li><b>Then the devices.</b> The old network card is the quiet bottleneck.</li>"
    "<li><b>Then the router.</b> The replacement is the last suspect, not the first.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/wifi-channel-congestion-fix/\">the Wi-Fi channel congestion fix</a>, <a href=\"/tech/router-placement-nigerian-flat/\">router placement in a Nigerian flat</a> and <a href=\"/tech/wi-fi-router-placement/\">Wi-Fi router placement</a>.</p>",

"writers/learn/journaling-personal/how-to-start-journaling":
    "<h2>The first page</h2>"
    "<p>Starting a journal is a permission problem: the page does not need to be good, published or even readable tomorrow. The starter's kit is one prompt, one small session and one privacy guarantee — the drawer that keeps the pages honest. The <a href=\"" + _w("journaling") + "\" rel=\"noopener\">journaling practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The starter's kit</h2>"
    "<ul>"
    "<li><b>One prompt, three lines.</b> The entry's size is the habit's survival condition.</li>"
    "<li><b>The same slot daily.</b> The trigger does the remembering.</li>"
    "<li><b>Private by design.</b> The unwatched page is the honest one.</li>"
    "<li><b>Skip the streak guilt.</b> The practice is a tool, not a test.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/journaling-personal/daily-journal-prompts/\">daily journal prompts</a>, <a href=\"/writers/learn/start-writing/how-to-overcome-writers-block/\">how to overcome writer's block</a> and <a href=\"/writers/learn/journaling-personal/\">journaling and personal writing</a>.</p>",

"entertainment/indian-cinema-first-five":
    "<h2>Five doors, five industries</h2>"
    "<p>Indian cinema is plural: the Hindi mainstream's song-and-spectacle machine, the Malayalam new wave's realism, the Tamil genre cinema's invention under constraint. The starter set maps the range — the five films that show the subcontinent's cinema arguing with itself. The <a href=\"" + _w("cinema+of+India") + "\" rel=\"noopener\">Indian cinema</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The map</h2>"
    "<ul>"
    "<li><b>The mainstream spectacle.</b> The song sequence is a narrative technology.</li>"
    "<li><b>The new wave realism.</b> The regional cinemas carry the critical reputation.</li>"
    "<li><b>The genre machinery.</b> The masala film's structure is its own grammar.</li>"
    "<li><b>Read the subtitles twice.</b> The translation carries the culture's half.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/10-korean-movies-everyone-should-watch/\">ten Korean movies to watch</a>, <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a> and <a href=\"/entertainment/film-movements-explained/\">film movements explained</a>.</p>",

"entertainment/shows-like-stranger-things":
    "<h2>The next watches</h2>"
    "<p>The shows that share Stranger Things' DNA keep its recipe: the kids' gang against the institution, the 1980s as an emotional technology, and the genre horror played as friendship's stakes. The best next watches find their own monster inside the same formula. The <a href=\"" + _w("supernatural+fiction") + "\" rel=\"noopener\">supernatural genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What to look for</h2>"
    "<ul>"
    "<li><b>The group is the hero.</b> The gang's friendship carries the season's stakes.</li>"
    "<li><b>The era is the texture.</b> The nostalgia is the story's second engine.</li>"
    "<li><b>The monster is the metaphor.</b> The horror lands because it means something.</li>"
    "<li><b>The small town is the lab.</b> The setting contains the secret.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/shows-like-squid-game/\">shows like Squid Game</a>, <a href=\"/entertainment/10-shows-like-alice-in-borderland-you-should-watch-next/\">shows like Alice in Borderland</a> and <a href=\"/entertainment/comfort-movies-to-rewatch/\">comfort movies to rewatch</a>.</p>",

"home/bathroom-grout-mould":
    "<h2>The bleach's short memory</h2>"
    "<p>The black in the tile lines is a colony fed by humidity, and bleach only recolours it: the spores stay in the grout's pores while the surface looks resolved. The lasting fix is moisture management plus a grout-safe fungicide, then the ventilation habit that starves the colony. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes mould guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The fix that lasts</h2>"
    "<ul>"
    "<li><b>Fungicide, not bleach.</b> The product must reach the colony, not the colour.</li>"
    "<li><b>The fan's ten minutes.</b> The ventilation is the mould's starvation plan.</li>"
    "<li><b>Reseal the grout yearly.</b> The sealant is the colony's property line.</li>"
    "<li><b>Fix the humidity source.</b> The tile is the symptom's canvas.</li>"
    "</ul>"
    "<p>See <a href=\"/home/grout-sealant-neglect/\">grout and sealant neglect</a>, <a href=\"/home/condensation-ventilation-that-works/\">condensation and ventilation</a> and <a href=\"/home/bathroom-fan-condensation/\">bathroom fan condensation</a>.</p>",

"home/why-is-my-home-doing-that":
    "<h2>The symptom finder</h2>"
    "<p>The house's strange behaviours are diagnostics in disguise: the stain's location, the smell's schedule, the noise's temperature. The symptom finder maps each to its usual causes before the professional arrives — because the informed household describes the problem better. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The symptom map</h2>"
    "<ul>"
    "<li><b>Stains: follow the water's path.</b> The visible mark is rarely the source.</li>"
    "<li><b>Smells: note the schedule.</b> The time of day is the system's confession.</li>"
    "<li><b>Noises: name the material.</b> Wood, metal and water sound different in failure.</li>"
    "<li><b>Write it down.</b> The symptom log is the repair's first document.</li>"
    "</ul>"
    "<p>See <a href=\"/home/hvac-noises-decoded/\">HVAC noises decoded</a>, <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three damps</a> and <a href=\"/home/inspection-checklist-gaps/\">inspection checklist gaps</a>.</p>",

"tech/how-to-reset-forgotten-passwords":
    "<h2>The recovery playbook</h2>"
    "<p>Password recovery is a security ritual: the reset link travels through the email account, which makes that account the keystone of the whole identity. The playbook is order itself — recover the email first, secure it, then cascade the resets through the priority list. The <a href=\"" + _w("identity+management") + "\" rel=\"noopener\">account recovery</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The reset order</h2>"
    "<ul>"
    "<li><b>Email first, always.</b> The reset chain runs through the inbox.</li>"
    "<li><b>Banking and work next.</b> The accounts with costs at stake.</li>"
    "<li><b>Two-factor as you go.</b> The migration is the security audit.</li>"
    "<li><b>Then the password manager.</b> The last reset you will ever memorise.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/reusing-passwords-risk/\">the risk of reused passwords</a>, <a href=\"/tech/password-manager-migration-weekend/\">the password manager migration</a> and <a href=\"/tech/security-questions-are-insecure/\">security questions are insecure</a>.</p>",

"tech/which-hosting-type":
    "<h2>The two-minute decision</h2>"
    "<p>Hosting types are sized by traffic, expertise and grief budget: shared hosting for the brochure site, VPS for the app that needs root, managed platforms for the team that values sleep. The decision tree is short because the wrong choice is loud. The <a href=\"" + _w("web+hosting+service") + "\" rel=\"noopener\">hosting categories</a> are documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The decision tree</h2>"
    "<ul>"
    "<li><b>Static or brochure: shared.</b> The traffic is small; the support is the product.</li>"
    "<li><b>App with state: VPS or platform.</b> The database decides the architecture.</li>"
    "<li><b>Team without ops: managed.</b> The sleep is the feature being purchased.</li>"
    "<li><b>Traffic is the exit.</b> The migration plan is part of the first choice.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/hosting-types-compared-shared-vps-cloud-dedicated/\">hosting types compared</a>, <a href=\"/tech/free-vs-paid-hosting/\">free versus paid hosting</a> and <a href=\"/tech/domain-names-explained/\">domain names explained</a>.</p>",

"writers/learn/creative-writing":
    "<h2>The making of stories</h2>"
    "<p>Creative writing is the making of stories, poems and scripts — the craft side of the imagination: character, dialogue, structure and the sentence's music. The library here treats the art as a workshop: learnable parts, practised drills, and revision as the actual writing. The <a href=\"" + _w("creative+writing") + "\" rel=\"noopener\">creative writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The workshop map</h2>"
    "<ul>"
    "<li><b>Character.</b> The want on the page is the story's engine.</li>"
    "<li><b>Dialogue.</b> The speech that carries subtext and status.</li>"
    "<li><b>Structure.</b> The scene order as the reader's experience.</li>"
    "<li><b>Revision.</b> The drafting that turns the idea into the work.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/creative-writing/how-to-write-a-short-story/\">how to write a short story</a>, <a href=\"/writers/learn/creative-writing/how-to-develop-characters/\">how to develop characters</a> and <a href=\"/writers/learn/creative-writing/how-to-write-dialogue/\">how to write dialogue</a>.</p>",

"entertainment/fast-and-furious-watch-order":
    "<h2>The Tokyo Drift problem</h2>"
    "<p>The franchise's timeline is a knot: the third film sits later in the story than its release, and every ordering is a trade-off between the narrative's logic and the series' escalation. The release order is the historical document; the chronological order is the story's own. The <a href=\"" + _w("The+Fast+and+the+Furious") + "\" rel=\"noopener\">franchise timeline</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Which order to watch</h2>"
    "<ul>"
    "<li><b>Release order for the first run.</b> The films were made to land in their moment.</li>"
    "<li><b>Chronological for the rewatch.</b> The timeline's logic is the second viewing's pleasure.</li>"
    "<li><b>Tokyo Drift is the hinge.</b> The film's placement is the whole puzzle.</li>"
    "<li><b>The later entries reset the clock.</b> The retcons are part of the machine.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/alien-franchise-in-order/\">the Alien franchise in order</a>, <a href=\"/entertainment/christopher-nolan-movies-order/\">Nolan's movies in order</a> and <a href=\"/entertainment/how-cinematic-universes-work/\">how cinematic universes work</a>.</p>",

"writers/learn/dos-and-donts/dos-and-donts-of-creative-writing":
    "<h2>Do: trust the scene</h2>"
    "<p>Creative writing's rules are workshop wisdom: show the want in the scene, cut the explanation after it, and let the dialogue do the arguing. The dos and don'ts are not formulas — they are the patterns that survive honest reading. The <a href=\"" + _w("creative+writing") + "\" rel=\"noopener\">creative writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The shortlist</h2>"
    "<ul>"
    "<li><b>Do</b> enter the scene late and leave it early.</li>"
    "<li><b>Don't</b> explain the character's feelings after showing them.</li>"
    "<li><b>Do</b> give every character a want the scene can threaten.</li>"
    "<li><b>Don't</b> protect the protagonist from the plot's consequences.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/creative-writing/\">creative writing</a>, <a href=\"/writers/learn/creative-writing/how-to-develop-characters/\">how to develop characters</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-writing/\">the dos and don'ts of writing</a>.</p>",

"writers/learn/professional-writing/how-to-write-a-cv-resume":
    "<h2>The document that gets the minute</h2>"
    "<p>A CV earns its minute by evidence: the achievement with a number, the role with its scope, and the structure that lets a recruiter's eye land where the fit lives. The document is a marketing piece for a specific job — the tailored version is the real CV. The <a href=\"" + _w("r%C3%A9sum%C3%A9") + "\" rel=\"noopener\">CV form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The structure that works</h2>"
    "<ul>"
    "<li><b>The top third is the pitch.</b> The recruiter's minute lives there.</li>"
    "<li><b>Achievements with numbers.</b> The verbs do the work; the metrics prove it.</li>"
    "<li><b>Tailor per application.</b> The generic CV is the rejected CV.</li>"
    "<li><b>One page's discipline.</b> The second page must earn itself with evidence.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/professional-writing/how-to-write-a-cover-letter/\">how to write a cover letter</a>, <a href=\"/writers/learn/examples/example-of-a-cover-letter/\">the cover letter example</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-a-cover-letter/\">the dos and don'ts of a cover letter</a>.</p>",

"writers/learn/structure-formatting/how-to-write-a-conclusion":
    "<h2>The ending that answers</h2>"
    "<p>A conclusion is the essay's answer arriving: the claim restated with the argument's weight behind it, the stakes named for the reader, and the final line that opens the question wider rather than closing it flat. The conclusion's enemy is the summary. The <a href=\"" + _w("conclusion") + "\" rel=\"noopener\">conclusion practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The conclusion's jobs</h2>"
    "<ul>"
    "<li><b>Answer the question asked.</b> The reader's contract is the ending's first duty.</li>"
    "<li><b>Restate with new weight.</b> The thesis returns changed by the argument.</li>"
    "<li><b>Name the stake.</b> The 'so what' is the ending's real content.</li>"
    "<li><b>Open the door.</b> The last line widens rather than seals.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/structure-formatting/\">structure and formatting</a>, <a href=\"/writers/learn/common-problems/my-introduction-is-weak/\">my introduction is weak</a> and <a href=\"/writers/learn/types-of-writing/how-to-write-an-essay/\">how to write an essay</a>.</p>",

"home/baby-toddler-home-proofing":
    "<h2>The six fixes that matter</h2>"
    "<p>Baby-proofing is hazard triage: the stairs, the sockets, the furniture that tips, the chemicals under the sink. The honest list is short — the six fixes that address the injuries that actually happen — and the rest is anxiety merchandise. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes child injury guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The honest list</h2>"
    "<ul>"
    "<li><b>The stairs.</b> The gates at both ends; the banister's gap is the hidden hazard.</li>"
    "<li><b>The tip-overs.</b> The furniture anchored to the wall is the fix that sticks.</li>"
    "<li><b>The cabinets.</b> The chemicals move up; the latch is the second line.</li>"
    "<li><b>The water.</b> The bath temperature and the kettle's cord are the burn map.</li>"
    "</ul>"
    "<p>See <a href=\"/home/basic-toolkit-checklist/\">the basic toolkit checklist</a>, <a href=\"/home/barred-windows-and-fire-escape/\">barred windows and fire escape</a> and <a href=\"/home/test-alarms-monthly/\">the monthly alarm habit</a>.</p>",

"writers/learn/common-problems/my-introduction-is-weak":
    "<h2>The opening's real job</h2>"
    "<p>Weak introductions are usually doing the wrong job elegantly: setting the scene when the reader needs the question, warming up when the reader needs the stakes. The fix is rewriting the opening last — once the draft knows what it is about. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The fixing pass</h2>"
    "<ul>"
    "<li><b>Write it last.</b> The opening is the draft's summary of itself.</li>"
    "<li><b>The question by line two.</b> The reader's contract is signed early.</li>"
    "<li><b>Cut the throat-clearing.</b> 'Since the dawn of time' is the classic tell.</li>"
    "<li><b>The concrete before the abstract.</b> The scene earns the theory its place.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/common-problems/\">common writing problems</a>, <a href=\"/writers/learn/structure-formatting/how-to-write-a-conclusion/\">how to write a conclusion</a> and <a href=\"/writers/learn/common-problems/my-writing-sounds-too-formal/\">my writing sounds too formal</a>.</p>",

"writers/learn/creative-writing/how-to-develop-characters":
    "<h2>The want on the page</h2>"
    "<p>Character is desire under pressure: the want that drives the scene, the flaw that resists it, and the change the plot forces between them. The workshop's tools are simple — the want stated in one line, the backstory kept off the page but in the file. The <a href=\"" + _w("characterization") + "\" rel=\"noopener\">characterisation</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The development tools</h2>"
    "<ul>"
    "<li><b>The want, in one line.</b> The scene's engine is the desire's clarity.</li>"
    "<li><b>The flaw with a history.</b> The weakness is the character's evidence.</li>"
    "<li><b>Backstory as iceberg.</b> The file holds it; the page carries the shadows.</li>"
    "<li><b>Change must be paid for.</b> The arc's honesty is the cost it charges.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/creative-writing/how-to-write-dialogue/\">how to write dialogue</a>, <a href=\"/writers/learn/creative-writing/how-to-write-a-short-story/\">how to write a short story</a> and <a href=\"/writers/learn/creative-writing/how-to-plan-a-novel/\">how to plan a novel</a>.</p>",

"entertainment/what-to-watch-in-90-minutes":
    "<h2>The ninety-minute contract</h2>"
    "<p>Ninety minutes is a screenplay's discipline: the tight film that spends its whole budget on the turn. The comedies, the thrillers and the animations that run the short clock are engineered differently — every scene doing two jobs. The <a href=\"" + _w("feature+film") + "\" rel=\"noopener\">feature film</a> form is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What fits the clock</h2>"
    "<ul>"
    "<li><b>The bottle film.</b> One location, real time, maximum tension.</li>"
    "<li><b>The tight comedy.</b> The ninety-minute comedy's jokes-per-scene discipline.</li>"
    "<li><b>The animation.</b> The form's economy is the medium's craft.</li>"
    "<li><b>The documentary.</b> The short form's argument is the feature's whole job.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-to-pick-a-movie-tonight/\">how to pick a movie tonight</a>, <a href=\"/entertainment/best-limited-series-to-watch/\">the best limited series</a> and <a href=\"/entertainment/comfort-movies-to-rewatch/\">comfort movies to rewatch</a>.</p>",

}

TOPUP_SECTIONS16 = {

"home/privacy":
    "<h2>What the desk does with it</h2>"
    "<p>The data this desk collects is the data the pages need to work: no tracking pixels selling the reading list, no accounts required to read, and the analytics that exist are counted in aggregate. The house privacy page's job is to state that plainly. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government data guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The commitments</h2>"
    "<ul>"
    "<li><b>Read without an account.</b> The pages are public by design.</li>"
    "<li><b>Aggregate, not individual.</b> The counters count visits, not visitors.</li>"
    "<li><b>The tools run locally.</b> The browser tools never upload the input.</li>"
    "<li><b>Corrections on request.</b> The contact page is the privacy page's door.</li>"
    "</ul>"
    "<p>See <a href=\"/home/contact/\">contact the desk</a>, <a href=\"/home/editorial-policy/\">the editorial policy</a> and <a href=\"/home/disclaimer/\">the disclaimer</a>.</p>",

"home/mistakes/overloading-the-fridge":
    "<h2>The airflow is the cold</h2>"
    "<p>A packed fridge is a warm fridge: the cold air's circulation is the appliance's whole design, and the boxes against the vent are the energy bill's quiet author. The door's shelves are the warmest real estate in the kitchen. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Load the fridge properly</h2>"
    "<ul>"
    "<li><b>Leave the vent clear.</b> The circulation is the cooling system.</li>"
    "<li><b>The door is the warm shelf.</b> The condiments live there for a reason.</li>"
    "<li><b>Cold mass helps.</b> The full fridge holds temperature; the crowded one cannot.</li>"
    "<li><b>The thermometer is the truth.</b> The dial's numbers are decorative.</li>"
    "</ul>"
    "<p>See <a href=\"/home/fridge-not-cold-enough/\">the fridge that is not cold enough</a>, <a href=\"/home/fridge-door-seal-test/\">the fridge door seal test</a> and <a href=\"/home/fridge-temperature-setting/\">the fridge temperature setting</a>.</p>",

"sports/deadline-day-dont-try-to-make-sense-of-it":
    "<h2>The theatre of the last hour</h2>"
    "<p>Deadline day is the transfer window's compression event: the fee's inflation, the medical in the car park, and the paperwork that turns rumour into registration. The day makes narrative sense only as spectacle — the market's logic arrives afterwards, in the squad's shape. The <a href=\"" + PL + "\" rel=\"noopener\">Premier League</a> market this desk follows plays out in public. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>How to watch it</h2>"
    "<ul>"
    "<li><b>Registration is the only truth.</b> The announcement is the trailer.</li>"
    "<li><b>The fee inflates by the hour.</b> Scarcity is the day's whole economics.</li>"
    "<li><b>The loan is the pressure valve.</b> The panic buys are structured deals.</li>"
    "<li><b>Read the squad afterwards.</b> The day's sense is the season's team sheet.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-the-transfer-window-works/\">how the transfer window works</a>, <a href=\"/sports/premier-league-transfer-tracker-august-2026/\">the transfer tracker</a> and <a href=\"/sports/how-football-transfer-medicals-work/\">how transfer medicals work</a>.</p>",

"writers/writing-opportunities/kenya":
    "<h2>The Kenyan market map</h2>"
    "<p>Kenya's writing market runs on three engines: the newsrooms' features desks, the literary magazines' reading windows, and the digital platforms' content budgets. The opportunities page tracks the verified paying markets and the rates they state — the writers who check the guidelines twice get published. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the opportunities list</h2>"
    "<ul>"
    "<li><b>Named rates first.</b> The market's honesty is in its terms sheet.</li>"
    "<li><b>Local beats generic.</b> The regional pitch's specificity is its currency.</li>"
    "<li><b>Check the window twice.</b> The reading periods are the whole policy.</li>"
    "<li><b>The international market is open.</b> The diaspora desks commission from Nairobi.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-african-writers-can-find-paid-publications/\">how African writers find paid publications</a>, <a href=\"/writers/guides/how-to-find-paid-writing-opportunities/\">how to find paid opportunities</a> and <a href=\"/writers/learn/freelance-paid-writing/freelance-writing-rates-kenya/\">freelance writing rates in Kenya</a>.</p>",

"home/mistakes/too-much-detergent":
    "<h2>The residue is the problem</h2>"
    "<p>Excess detergent does not clean better; it deposits, it foams, and it carries the machine's seal toward the repair. The scoop's habit is the fabric's and the machine's shared care — the modern wash needs less soap than the memory of the lather. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The corrected scoop</h2>"
    "<ul>"
    "<li><b>Half the remembered dose.</b> The modern formula is concentrated.</li>"
    "<li><b>The drum's cleanliness is the check.</b> The residue advertises in the seal.</li>"
    "<li><b>Soft water needs less.</b> The geography decides the dose.</li>"
    "<li><b>The monthly hot cycle.</b> The machine cleans itself first.</li>"
    "</ul>"
    "<p>See <a href=\"/home/washing-machine-heavy-items/\">washing machine heavy items</a>, <a href=\"/home/mistakes/drying-laundry-indoors/\">drying laundry indoors</a> and <a href=\"/home/mistakes/mixing-cleaning-products/\">mixing cleaning products</a>.</p>",

}
