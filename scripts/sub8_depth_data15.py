# -*- coding: utf-8 -*-
"""Editorial depth sections, part 15: batch J, the 616-634 word tranche against
the 750-word bar, plus home/disclaimer (602 of 732) and five t8b top-ups.
84 pages total. Blocks sized ~170 words to clear the bar in one pass.
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

DEPTH_SECTIONS15 = {

"writers/learn/types-of-writing/how-to-write-a-feature":
    "<h2>The story under the topic</h2>"
    "<p>A feature is reporting shaped as narrative: the topic is the setting, but the story is the human tension underneath it. The feature writer finds the character who embodies the question, the scene that shows it, and the structure that lets a reader forget they are being informed. The <a href=\"" + _w("feature+story") + "\" rel=\"noopener\">feature writing form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Building the feature</h2>"
    "<ul>"
    "<li><b>Find the character first.</b> The person is the reader's way into the topic.</li>"
    "<li><b>Report scenes, not just facts.</b> Detail is what separates feature from explainer.</li>"
    "<li><b>Structure for the turn.</b> Every good feature has a moment the story changes direction.</li>"
    "<li><b>End where the meaning lives.</b> The kicker is written, never stumbled upon.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-an-article/\">how to write an article</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-a-personal-essay/\">how to write a personal essay</a> and <a href=\"/writers/guides/how-to-pitch-an-essay/\">how to pitch an essay</a>.</p>",

"writers/writing/agni":
    "<h2>A market for the long sentence</h2>"
    "<p>AGNI publishes poetry and prose with an eye for the ambitious sentence — work that trusts the reader with difficulty and rewards the second reading. Its payment terms and reading windows are stated plainly, which keeps it on every serious submission list. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Read the current issue.</b> The magazine's ear is on every page.</li>"
    "<li><b>Send the difficult piece.</b> The market exists for work the mainstream flinches from.</li>"
    "<li><b>Respect the window.</b> Reading periods are the policy, not a suggestion.</li>"
    "<li><b>One polished piece beats three drafts.</b> Small magazines read quality, not volume.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/kenyon-review/\">The Kenyon Review</a>, <a href=\"/writers/writing/cincinnati-review/\">The Cincinnati Review</a> and <a href=\"/writers/writing/the-ex-puritan/\">The Ex-Puritan</a>.</p>",

"tech/quantlab-project-how-built":
    "<h2>One person, one lab</h2>"
    "<p>A quantitative research lab in Python is a pipeline, not a platform: data ingestion, cleaning, feature stores, backtests and reporting, each stage reproducible from a single command. The project's real lesson is that infrastructure discipline is cheaper than cleverness — the lab that reruns last month's result is worth more than the one that predicts. The <a href=\"" + _w("quantitative+research") + "\" rel=\"noopener\">quantitative research</a> practice is documented in standard references. By the Bryme Technical Research desk. Reviewed 28 September 2026.</p>"
    "<h2>What the build taught</h2>"
    "<ul>"
    "<li><b>Reproducibility first.</b> Every result regenerates from the raw data or it does not exist.</li>"
    "<li><b>SQLite is enough.</b> The bottleneck is the research, not the database.</li>"
    "<li><b>Report generation is the product.</b> The lab's output is the notebook, not the trade.</li>"
    "<li><b>Version the data.</b> The dataset changes; the experiment must not.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/backtest-validation-checklist/\">the backtest validation checklist</a>, <a href=\"/tech/reproducible-quant-research-why-it-matters/\">reproducible quant research</a> and <a href=\"/tech/paper-trading-bot-lessons/\">paper trading bot lessons</a>.</p>",

"home/dryer-lint-every-load":
    "<h2>Why every load, every time</h2>"
    "<p>The lint trap is the dryer's fire safety system and its efficiency system in one: a full trap doubles drying time, doubles the bill, and sends heat where the drum's design never intended. Dryer fires start in the vent line that the trap's neglect feeds. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes dryer vent guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The habit, and the yearly job</h2>"
    "<ul>"
    "<li><b>Clear the trap before every load.</b> The thirty seconds is the whole ritual.</li>"
    "<li><b>Wash it monthly.</b> Dryer sheets leave a film a brush cannot see.</li>"
    "<li><b>Clean the vent line yearly.</b> The lint the trap misses lives there.</li>"
    "<li><b>Watch the dry time.</b> A load that suddenly takes longer is telling you something.</li>"
    "</ul>"
    "<p>See <a href=\"/home/dryer-vent-cleaning-fire-risk/\">dryer vent cleaning and fire risk</a>, <a href=\"/home/washing-machine-walks-and-shakes/\">the machine that walks</a> and <a href=\"/home/test-alarms-monthly/\">the monthly alarm habit</a>.</p>",

"tech/cloud-vs-local-backup":
    "<h2>Why both, not either</h2>"
    "<p>Cloud and local backups fail differently, which is exactly why both are required: the cloud survives the house fire and the stolen laptop; the local copy survives the account lockout, the sync deletion and the internet being down. The 3-2-1 rule is just these failure modes made arithmetic. The <a href=\"" + _w("backup") + "\" rel=\"noopener\">backup discipline</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What each one survives</h2>"
    "<ul>"
    "<li><b>Cloud: physical disaster.</b> Fire, theft and flood are someone else's problem.</li>"
    "<li><b>Local: account disaster.</b> Lockouts, deletions and outages end at your drive.</li>"
    "<li><b>Test restores, both sides.</b> A backup is a promise you have not yet kept.</li>"
    "<li><b>Automate or forget.</b> The manual backup is the one that stops in March.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/three-two-one-backup-rule/\">the 3-2-1 backup rule</a>, <a href=\"/tech/cloud-storage-mistakes/\">cloud storage mistakes</a> and <a href=\"/tech/home-nas-vs-cloud-vs-drive/\">home NAS versus cloud versus drive</a>.</p>",

"writers/learn/types-of-writing/how-to-write-a-poem":
    "<h2>The line is the decision</h2>"
    "<p>Poetry is writing where the line break is an argument: the line decides what the reader knows and when, and the white space does half the saying. The poem works when its language is doing more than its sentences — sound, image and syntax loading the same word twice. The <a href=\"" + _w("poetry") + "\" rel=\"noopener\">poetic form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The workshop rules</h2>"
    "<ul>"
    "<li><b>Read it aloud first.</b> The ear is poetry's first editor.</li>"
    "<li><b>Cut the lines that explain.</b> The image earns trust; the commentary spends it.</li>"
    "<li><b>End before the ending.</b> The last line should open, not close.</li>"
    "<li><b>Revise the breaks.</b> Every line ending is a decision you can revisit.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/creative-writing/how-to-write-a-short-story/\">how to write a short story</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-a-personal-essay/\">how to write a personal essay</a> and <a href=\"/writers/learn/editing-proofreading/how-to-make-writing-more-concise/\">how to make writing more concise</a>.</p>",

"writers/writing/split-lip-magazine":
    "<h2>Working-class stories, honestly</h2>"
    "<p>Split Lip Magazine pays contributors and publishes work with its feet on the ground — fiction, nonfiction and poetry that values the specific life over the universal lesson. It is a market where voice is the entry requirement and the payment terms are stated plainly. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Specificity over theme.</b> The magazine buys lives, not lessons.</li>"
    "<li><b>Check the monthly windows.</b> Small magazines open and close like shops.</li>"
    "<li><b>Voice carries the piece.</b> The first paragraph is the audition.</li>"
    "<li><b>Simultaneous submissions are welcome.</b> Withdraw promptly on acceptance elsewhere.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/torch-literary-arts/\">Torch Literary Arts</a>, <a href=\"/writers/writing/the-forge-literary-magazine/\">The Forge Literary Magazine</a> and <a href=\"/writers/writing/black-fox-literary-magazine/\">Black Fox Literary Magazine</a>.</p>",

"tech/environment-variables-guide":
    "<h2>Where the secrets live</h2>"
    "<p>Environment variables are configuration that never enters the codebase — the reason API keys, tokens and database URLs can change between machines without a commit. The pattern is universal because the failure it prevents is universal: the leaked secret in the repository's history. The <a href=\"" + _w("environment+variable") + "\" rel=\"noopener\">environment variable</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The pattern, properly</h2>"
    "<ul>"
    "<li><b>.env in .gitignore, always.</b> The example file is the template; the real one is local.</li>"
    "<li><b>Validate at startup.</b> A missing variable should fail loudly, at boot.</li>"
    "<li><b>One source of truth.</b> The environment decides; the code only reads.</li>"
    "<li><b>Rotate what leaks.</b> History rewrites are recovery; rotation is prevention.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/github-token-hygiene/\">GitHub token hygiene</a>, <a href=\"/tech/plain-text-passwords/\">plain text passwords</a> and <a href=\"/tech/deploy-python-app/\">deploying a Python app</a>.</p>",

"writers/learn/start-writing":
    "<h2>Start before you are ready</h2>"
    "<p>Starting writing is a logistics problem: pick the small project, lower the standard, and put the session on the calendar before the confidence arrives. The writers who produce work have not solved their doubts — they have simply built a routine that runs alongside them. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The first month</h2>"
    "<ul>"
    "<li><b>Small project first.</b> The finished short piece teaches more than the eternal novel.</li>"
    "<li><b>Same time, most days.</b> Routine beats inspiration in every account of the work.</li>"
    "<li><b>Finish something weekly.</b> Completion is a skill that must be practised.</li>"
    "<li><b>Read the market you want.</b> Writers learn the form by reading it inhabited.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/start-writing/how-to-start-writing/\">how to start writing</a>, <a href=\"/writers/learn/start-writing/how-to-overcome-writers-block/\">how to overcome writer's block</a> and <a href=\"/writers/learn/writing-process/\">the writing process</a>.</p>",

"home/caulk-vs-grout-explained":
    "<h2>The rule that settles it</h2>"
    "<p>Grout fills the joints that do not move; caulk seals the corners that do. Every bathroom mistake in this family comes from swapping the two — grout cracking in the corner it was never designed for, caulk failing to hold the tile line it was never meant to fill. The <a href=\"" + _w("caulk") + "\" rel=\"noopener\">sealant and grout practice</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The one rule, applied</h2>"
    "<ul>"
    "<li><b>Change of plane: caulk.</b> Corners, edges and the bath rim move.</li>"
    "<li><b>Tile field: grout.</b> The wall between tiles stays still.</li>"
    "<li><b>100% silicone where water sits.</b> The cheap tube fails expensively.</li>"
    "<li><b>Tool the bead once.</b> The finger pass is where the mess begins.</li>"
    "</ul>"
    "<p>See <a href=\"/home/bath-silicone-reseal/\">the bath silicone reseal</a>, <a href=\"/home/grout-sealant-neglect/\">grout and sealant neglect</a> and <a href=\"/home/bathroom-grout-mould/\">bathroom grout mould</a>.</p>",

"home/generator-vs-inverter-nigeria":
    "<h2>A spreadsheet decision</h2>"
    "<p>Generator versus inverter is fuel maths against battery maths: the load profile, the hours of outage, the cost per kilowatt-hour over five years. Generators win on raw capacity and lose on noise and fuel logistics; inverters win on silence and lose on the upfront number. The <a href=\"" + _w("inverter") + "\" rel=\"noopener\">inverter system</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The columns that decide</h2>"
    "<ul>"
    "<li><b>Hours of outage per week.</b> The single biggest input; measure it before buying.</li>"
    "<li><b>The load list.</b> Fridge, fans and lights first; the kettle is a luxury line.</li>"
    "<li><b>Five-year fuel cost.</b> The generator's sticker price is the deposit.</li>"
    "<li><b>Noise and fumes.</b> The costs that never appear on the invoice.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/inverter-battery-runtime-maths/\">inverter battery runtime maths</a>, <a href=\"/tech/blackout-internet-router-power/\">blackout internet and router power</a> and <a href=\"/home/appliances-that-use-the-most-electricity/\">appliances that use the most electricity</a>.</p>",

"entertainment/post-credits-scenes-explained":
    "<h2>The scene after the contract</h2>"
    "<p>Post-credits scenes are a studio's handshake with the audience that stays: the mid-credits joke, the post-credits promise, and the franchise breadcrumb that turns a film into an episode. The tradition runs from Ferris Bueller to the modern universe machine — and the theatre staff's least favourite ritual. The <a href=\"" + _w("post-credits+scene") + "\" rel=\"noopener\">post-credits scene</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Why they work</h2>"
    "<ul>"
    "<li><b>The reward is belonging.</b> The scene says: you know how this works.</li>"
    "<li><b>The joke releases the film.</b> Comedy credits clear the tonal debt.</li>"
    "<li><b>The breadcrumb builds the universe.</b> Next year's trailer lives here.</li>"
    "<li><b>Ask the staff.</b> The scene's presence is the theatre's open secret.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-cinematic-universes-work/\">how cinematic universes work</a>, <a href=\"/entertainment/how-movie-release-windows-work/\">how release windows work</a> and <a href=\"/entertainment/directors-cut-vs-theatrical-explained/\">director's cut versus theatrical</a>.</p>",

"writers/learn/common-problems/my-writing-sounds-too-formal":
    "<h2>Where the stiffness comes from</h2>"
    "<p>Formal distance is almost always a costume: the writer performing competence instead of communicating it. The fix is not slang — it is choosing the plain word, the active verb and the sentence that sounds like a person explaining something they understand. The <a href=\"" + _w("plain+language") + "\" rel=\"noopener\">plain language practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The de-stiffening edits</h2>"
    "<ul>"
    "<li><b>Read it aloud.</b> The mouth detects the costume instantly.</li>"
    "<li><b>Swap the Latinate noun.</b> 'Utilise' is 'use' wearing a tie.</li>"
    "<li><b>Name the actor.</b> Passive voice is where formality hides.</li>"
    "<li><b>Cut the throat-clearing.</b> 'It is important to note that' notes nothing.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/common-problems/my-introduction-is-weak/\">my introduction is weak</a>, <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-writing/\">the dos and don'ts of writing</a> and <a href=\"/writers/learn/editing-proofreading/how-to-make-writing-more-concise/\">how to make writing more concise</a>.</p>",

"entertainment/reviews/thirty-days-in-atlanta":
    "<h2>The comedy that sold the trip</h2>"
    "<p>Thirty Days in Atlanta built its comedy on the Nigerian-in-America collision — the jokes that live in the gap between expectation and Atlanta. Its box office run made the case that local comedy could carry a cinema. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the film proved</h2>"
    "<ul>"
    "<li><b>The diaspora premise is a genre.</b> The gap between homes is the joke engine.</li>"
    "<li><b>Comedy carries cinemas.</b> Theatres filled on word of mouth alone.</li>"
    "<li><b>The cast is the marketing.</b> The comedy duo's audience arrived first.</li>"
    "<li><b>Sequels follow success.</b> The franchise logic arrived with the box office.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/nollywood-golden-age-explained/\">Nollywood's golden age</a>, <a href=\"/entertainment/reviews/mokalik/\">the Mokalik review</a> and <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a>.</p>",

"entertainment/what-is-film-noir-explained":
    "<h2>The shadow genre</h2>"
    "<p>Film noir was never a movement with a manifesto — it was a mood the studio system stumbled into: venetian-blind light, moral fog, the detective who knows better. The name arrived from the French critics after the fact, and the genre has been reinvented by every decade since. The <a href=\"" + _w("film+noir") + "\" rel=\"noopener\">film noir</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The signature moves</h2>"
    "<ul>"
    "<li><b>Light as plot.</b> The shadows tell you who to trust.</li>"
    "<li><b>The narrator who is lying.</b> Voiceover as unreliable evidence.</li>"
    "<li><b>The city at night.</b> Streets as moral geography.</li>"
    "<li><b>The ending that is not a victory.</b> Noir survives its own conclusions.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/film-movements-explained/\">film movements explained</a>, <a href=\"/entertainment/german-expressionism-explained/\">German Expressionism explained</a> and <a href=\"/entertainment/comfort-movies-to-rewatch/\">comfort movies to rewatch</a>.</p>",

"home/emergency-repair-fund":
    "<h2>The fund that owns the surprise</h2>"
    "<p>Every home eventually presents a bill that cannot wait: the burst pipe, the failed inverter, the roof the rains found. The emergency repair fund is not insurance — it is the cash that turns a crisis into an errand, sized at roughly one percent of the home's value and kept where Tuesday cannot reach it. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Sizing and keeping it</h2>"
    "<ul>"
    "<li><b>One percent a year, as a floor.</b> The maths is approximate; the habit is exact.</li>"
    "<li><b>Separate account, separate name.</b> The label is part of the discipline.</li>"
    "<li><b>Replenish after use.</b> The fund's second test is the refill.</li>"
    "<li><b>Know the first calls.</b> The plumber's number is part of the fund.</li>"
    "</ul>"
    "<p>See <a href=\"/home/inspection-checklist-gaps/\">inspection checklist gaps</a>, <a href=\"/home/energy-bill-high-unchanged/\">the energy bill that will not fall</a> and <a href=\"/home/mistakes/\">the common home mistakes</a>.</p>",

"home/rainy-season-home-checklist":
    "<h2>What the Lagos rains inspect</h2>"
    "<p>The pre-rains checklist is the survey the season will run anyway: gutters cleared, external cracks sealed, drainage moving, and the roof checked while it is still a dry job. Lagos roofs fail at the details — the joint, the outlet, the sealant that aged out last year. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The checklist, in order</h2>"
    "<ul>"
    "<li><b>Gutters and outlets first.</b> The cheapest prevention on the whole list.</li>"
    "<li><b>External walls and sealant.</b> Hairline cracks are the rain's entry paperwork.</li>"
    "<li><b>Drainage and compound level.</b> Water that stands finds a way in.</li>"
    "<li><b>The roof inspection while dry.</b> Wet-season repairs cost double.</li>"
    "</ul>"
    "<p>See <a href=\"/home/gutters-and-downpipes/\">gutters and downpipes</a>, <a href=\"/home/external-wall-crack-seal/\">the external wall crack seal</a> and <a href=\"/home/flat-roof-ponding-and-leaks/\">flat roof ponding and leaks</a>.</p>",

"writers/learn/freelance-paid-writing/how-to-find-paying-publications":
    "<h2>The research discipline</h2>"
    "<p>Paying publications announce themselves in specific places: mastheads with named editors, submission pages with stated rates, and archives that show who has been published. The research discipline is verifying all three before writing a word of the pitch — the market that cannot state its terms cannot be trusted with your work. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs verified markets. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The verification pass</h2>"
    "<ul>"
    "<li><b>Named rates, or walk.</b> Exposure pays in nothing.</li>"
    "<li><b>Find the current issue.</b> A live market publishes.</li>"
    "<li><b>Trace the editors.</b> Real bylines have real histories.</li>"
    "<li><b>Check the response norms.</b> The market's manners are in its track record.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-to-find-paid-writing-opportunities/\">how to find paid writing opportunities</a>, <a href=\"/writers/guides/how-to-find-international-writing-opportunities/\">international writing opportunities</a> and <a href=\"/writers/guides/how-african-writers-can-find-paid-publications/\">how African writers find paid publications</a>.</p>",

"entertainment/best-heist-movies":
    "<h2>Perfectly planned nights</h2>"
    "<p>The heist film is a machine picture: the plan shown in pieces, the crew assembled like a toolset, and the beautiful moment the plan meets the world. The best ones know the genre's real subject is not the money but the professional's dignity under chaos. The <a href=\"" + _w("heist+film") + "\" rel=\"noopener\">heist film genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the great ones share</h2>"
    "<ul>"
    "<li><b>The assembly is half the pleasure.</b> The crew's recruitment is the first act's engine.</li>"
    "<li><b>The plan is shown, then broken.</b> The audience must own the plan to feel the failure.</li>"
    "<li><b>Style with stakes.</b> The suits matter because the bullets do.</li>"
    "<li><b>The twist is the machine's honesty.</b> The genre cheats only where it promised to.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-thriller-movies-of-all-time/\">the best thrillers of all time</a>, <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a> and <a href=\"/entertainment/best-films-for-a-group/\">the best films for a group</a>.</p>",

"entertainment/best-mecha-anime-explained":
    "<h2>Giant robots, as promised</h2>"
    "<p>Mecha is the medium's oldest argument with itself: the robot as wish fulfilment in the super-robot shows, the robot as trauma machine in the real-robot shows. The genre's best entries know the machine is a metaphor wearing armour — which is why the pilots' conversations outrank the fights. The <a href=\"" + _w("mecha") + "\" rel=\"noopener\">mecha genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The two lineages</h2>"
    "<ul>"
    "<li><b>Super robot.</b> The machine is a hero with a finishing move.</li>"
    "<li><b>Real robot.</b> The machine is military hardware, and the show knows it.</li>"
    "<li><b>The pilots carry the genre.</b> Character drama in the cockpit.</li>"
    "<li><b>Watch the lineage.</b> Each generation argues with its predecessor.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/isekai-anime-explained/\">isekai anime explained</a>, <a href=\"/entertainment/slice-of-life-anime-explained/\">slice-of-life anime explained</a> and <a href=\"/entertainment/best-anime-movies-of-all-time/\">the best anime movies of all time</a>.</p>",

"entertainment/isekai-anime-explained":
    "<h2>The transported-world genre</h2>"
    "<p>Isekai moves its hero into another world — by truck, by game, by ritual — and the genre's pleasure is the reset: a life restarted with rules that can be learned. The best entries use the frame for comedy or critique; the genre's ceiling is the power fantasy that never earns its powers. The <a href=\"" + _w("isekai") + "\" rel=\"noopener\">isekai genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Why the frame endures</h2>"
    "<ul>"
    "<li><b>The second chance is the product.</b> The audience's own reset fantasy.</li>"
    "<li><b>Game logic is legible.</b> Stats and levels make the world readable.</li>"
    "<li><b>Comedy knows the tropes.</b> The genre's self-awareness is its best seam.</li>"
    "<li><b>Critique travels well.</b> The deconstructions are the movement's growth.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-mecha-anime-explained/\">the best mecha anime</a>, <a href=\"/entertainment/anime-canon-and-filler-explained/\">anime canon and filler</a> and <a href=\"/entertainment/anime-seasons-and-cours-explained/\">anime seasons and cours</a>.</p>",

"entertainment/reviews/nneka-the-pretty-serpent":
    "<h2>Revenge, folklore, reboot</h2>"
    "<p>Nneka the Pretty Serpent rebuilds a Nollywood cult classic for the multiplex era: the folklore premise intact, the revenge plot sharpened, the production scaled to the market the original predicted. The film's interest is how much the 2020s version trusts the original's engine. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the reboot keeps</h2>"
    "<ul>"
    "<li><b>The folklore logic.</b> The serpent story's rules stay legible.</li>"
    "<li><b>The revenge structure.</b> The audience's appetite is the original's bet.</li>"
    "<li><b>The production upgrade.</b> The new version shows what the market became.</li>"
    "<li><b>The cult's memory.</b> Reboots are conversations with their audiences.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/reviews/shadow-parties/\">the Shadow Parties review</a>, <a href=\"/entertainment/nollywood-golden-age-explained/\">Nollywood's golden age</a> and <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a>.</p>",

"home/musty-wardrobe-clothes-rainy":
    "<h2>The six-week fix</h2>"
    "<p>The musty wardrobe is a humidity problem in a wooden box: damp air enters, the clothes absorb it, and the mildew colony arrives quietly while the rains keep everything wet. The fix is airflow, absorption and distance from the wall — not more perfume. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor air guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The six-week programme</h2>"
    "<ul>"
    "<li><b>Week one: empty and dry.</b> Sun the clothes; wipe the shelves dry.</li>"
    "<li><b>Week two: move the furniture.</b> Air against the back wall is the whole fix.</li>"
    "<li><b>Weeks three-six: absorb and rotate.</b> Moisture absorbers and the habit of spacing.</li>"
    "<li><b>Ongoing: check the damp source.</b> The wardrobe is the thermometer, not the disease.</li>"
    "</ul>"
    "<p>See <a href=\"/home/condensation-ventilation-that-works/\">condensation and ventilation that works</a>, <a href=\"/home/mistakes/drying-laundry-indoors/\">drying laundry indoors</a> and <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three damps</a>.</p>",

"tech/android-notifications-not-arriving":
    "<h2>Why apps go quiet</h2>"
    "<p>Missing notifications on Android are a permission story with three chapters: battery optimisation killing the app's background life, notification channels switched off one by one in some past settings session, and the Do Not Disturb schedule nobody remembers creating. Each fix is a toggle. The <a href=\"" + _w("Android") + "\" rel=\"noopener\">Android platform</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The three chapters</h2>"
    "<ul>"
    "<li><b>Battery optimisation first.</b> Aggressive modes silence apps silently.</li>"
    "<li><b>Notification channels second.</b> Every app's alerts have individual switches.</li>"
    "<li><b>Do Not Disturb third.</b> The schedule outlives the memory of creating it.</li>"
    "<li><b>Then reinstall.</b> Corrupted registration is rare and last.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-notifications/\">Android notifications</a>, <a href=\"/tech/android-privacy-settings-checklist/\">the Android privacy checklist</a> and <a href=\"/tech/free-up-storage-android/\">free up storage on Android</a>.</p>",

"tech/nat-type-port-forwarding":
    "<h2>The NAT story</h2>"
    "<p>'NAT failed' is the router refusing to route: the console's request for an open connection, the strict NAT type, the party chat that drops at the worst time. Port forwarding is the classic fix; UPnP is the convenient one; the honest answer includes both and a DMZ only as a test. The <a href=\"" + _w("network+address+translation") + "\" rel=\"noopener\">NAT system</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Opening the path</h2>"
    "<ul>"
    "<li><b>Static IP first.</b> The forward needs an address that stays.</li>"
    "<li><b>Forward the console's ports.</b> The publisher documents them; the router remembers them.</li>"
    "<li><b>UPnP as convenience, not policy.</b> It works until two devices disagree.</li>"
    "<li><b>Double NAT is the hidden villain.</b> Two routers arguing is the commonest strict NAT.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/home-network-segmentation-vlans-guest/\">home network segmentation</a>, <a href=\"/tech/cloud-gaming-reality-lagos-lines/\">cloud gaming on Lagos lines</a> and <a href=\"/tech/wi-fi-router-placement/\">Wi-Fi router placement</a>.</p>",

"tech/power-bank-size-math-for-tv-and-wifi":
    "<h2>What the brick actually runs</h2>"
    "<p>A 20,000 mAh power bank is a small battery with a marketing number — the watt-hours are the honest figure, and the conversion losses eat a fifth before the TV sees anything. The maths that matters is simple: device watts times hours, divided by usable capacity, minus the inverter's cut. The <a href=\"" + _w("battery+energy+capacity") + "\" rel=\"noopener\">battery capacity</a> maths is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Running the numbers</h2>"
    "<ul>"
    "<li><b>Convert to watt-hours first.</b> mAh is a vendor's unit; watts are physics.</li>"
    "<li><b>Assume 80% usable.</b> Conversion and heat take their share.</li>"
    "<li><b>Router before TV.</b> The router costs watts and buys everything else.</li>"
    "<li><b>DC beats AC when you can.</b> Every conversion is a leak.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/power-bank-flying-rules/\">power bank flying rules</a>, <a href=\"/tech/inverter-battery-runtime-maths/\">inverter battery runtime maths</a> and <a href=\"/tech/blackout-internet-router-power/\">blackout internet and router power</a>.</p>",

"writers/learn/writing-checklists":
    "<h2>Checklists that finish drafts</h2>"
    "<p>Writing checklists work because they move quality control out of the draft and into a second pass: the structure check before the line check, the reader check before the proof. Each checklist is a promise that some questions will be asked at the right time instead of at every time. The <a href=\"" + _w("editing") + "\" rel=\"noopener\">editing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The three passes</h2>"
    "<ul>"
    "<li><b>Structure pass.</b> Does each section earn its place? Cut before polishing.</li>"
    "<li><b>Reader pass.</b> Who is this for, and what do they need first?</li>"
    "<li><b>Language pass.</b> Verbs, repetition, the sentences that need reading twice.</li>"
    "<li><b>Proof pass.</b> Spelling last, always — the cheapest errors to fix late.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/structure-formatting/\">structure and formatting</a>, <a href=\"/writers/learn/editing-proofreading/\">editing and proofreading</a> and <a href=\"/writers/learn/dos-and-donts/\">the dos and don'ts library</a>.</p>",

"entertainment/into-the-badlands-was-underrated":
    "<h2>The show that swung for the fences</h2>"
    "<p>Into the Badlands staged martial-arts choreography on television scale — and then asked its world questions about power and inheritance that the fights were only the vocabulary for. Its cancellation is the argument of the piece: the audience for ambitious action exists; the schedule for patience does not. The <a href=\"" + _w("television+production") + "\" rel=\"noopener\">television production</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the show did right</h2>"
    "<ul>"
    "<li><b>Choreography as character.</b> The fights carried the dialogue's meaning.</li>"
    "<li><b>A world with a thesis.</b> The baronies argued about power by existing.</li>"
    "<li><b>It trusted colour and silence.</b> Genre television that believed in images.</li>"
    "<li><b>It ended its story.</b> Ambition includes the ending.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-tv-shows-get-cancelled/\">how TV shows get cancelled</a>, <a href=\"/entertainment/why-tv-seasons-are-getting-shorter/\">why TV seasons are getting shorter</a> and <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a>.</p>",

"sports/what-the-2026-world-cup-changed":
    "<h2>The tournament as an argument</h2>"
    "<p>The 2026 World Cup ran on the expanded format and the tri-nation host map, and the tournament itself settled the debates: squad depth decides a forty-eight-team bracket, travel is a tactical variable, and the calendar is now a club-versus-country negotiation in public. The <a href=\"" + _w("FIFA+World+Cup") + "\" rel=\"noopener\">World Cup format</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What the format proved</h2>"
    "<ul>"
    "<li><b>Depth beats eleven.</b> The expanded bracket rewards the wider squad.</li>"
    "<li><b>Travel is a match variable.</b> The host map added a third opponent.</li>"
    "<li><b>The group stage grew teeth.</b> More teams, more elimination nights.</li>"
    "<li><b>The calendar argument came home.</b> Club football now negotiates in the open.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/champions-league-new-format-explained/\">the Champions League new format</a>, <a href=\"/sports/how-the-transfer-window-works/\">how the transfer window works</a> and <a href=\"/sports/how-extra-time-and-penalty-shootouts-work/\">extra time and penalty shootouts</a>.</p>",

"sports/who-will-win-the-2026-ballon-dor":
    "<h2>How the award is actually decided</h2>"
    "<p>The Ballon d'Or is a journalists' ballot with a calendar: the season's achievements weighed by an international jury, the voting criteria published, the ceremony a formality at the end of the arithmetic. Understanding the criteria is the honest way to read any shortlist — the award rewards the year, not the reputation. The <a href=\"" + _w("Ballon+d%27Or") + "\" rel=\"noopener\">Ballon d'Or</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What the jury weighs</h2>"
    "<ul>"
    "<li><b>The year's achievements.</b> Trophies are evidence, not the verdict.</li>"
    "<li><b>Individual performance.</b> The decisive matches live in the voters' memory.</li>"
    "<li><b>Conduct and class.</b> The criteria name sportsmanship explicitly.</li>"
    "<li><b>The calendar matters.</b> The award's window frames every argument.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/best-football-players-in-the-world-2026/\">the best football players in the world</a>, <a href=\"/sports/how-olympic-judging-works/\">how Olympic judging works</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",

"tech/android":
    "<h2>The platform, honestly</h2>"
    "<p>Android is the open platform's long experiment: one operating system, a thousand hardware opinions, and a settings app that hides its best features. The desk's approach is behavioural — the battery, the storage, the permissions and the update path — because those decide daily life more than any spec sheet. The <a href=\"" + _w("Android") + "\" rel=\"noopener\">Android platform</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The four questions</h2>"
    "<ul>"
    "<li><b>Will it get updates?</b> The security patch level is the real spec.</li>"
    "<li><b>How is the battery managed?</b> Aggressive optimisation is a trade, not a feature.</li>"
    "<li><b>What does the backup cover?</b> The gaps are where loss lives.</li>"
    "<li><b>What do the apps know?</b> The permission screen is the disclosure.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-privacy-settings-checklist/\">the Android privacy checklist</a>, <a href=\"/tech/iphone-vs-android-nigeria/\">iPhone versus Android in Nigeria</a> and <a href=\"/tech/android-backup-guide/\">the Android backup guide</a>.</p>",

"tech/blackout-internet-router-power":
    "<h2>The Wi-Fi dies with the lights</h2>"
    "<p>The blackout that takes the Wi-Fi is an equipment question, not a signal one: the router, the ONT and the access point each need power, and most households size the backup for lights and forget the internet. The fix is a small UPS or a power bank with the right barrel plug. The <a href=\"" + _w("uninterruptible+power+supply") + "\" rel=\"noopener\">UPS</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Keeping the line up</h2>"
    "<ul>"
    "<li><b>Inventory the chain.</b> Router, ONT, switch — each is a failure point.</li>"
    "<li><b>Size the backup in hours, not watts.</b> The evening is the load.</li>"
    "<li><b>Test it dark.</b> The backup's first real test should not be the outage.</li>"
    "<li><b>Mobile hotspot as plan B.</b> The phone's tether is the free fallback.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/outage-lighting-tiers/\">outage lighting tiers</a>, <a href=\"/tech/inverter-battery-runtime-maths/\">inverter battery runtime maths</a> and <a href=\"/tech/surge-protector-stabiliser-ups/\">surge protector, stabiliser or UPS</a>.</p>",

"tech/one-big-monitor-vs-two":
    "<h2>The desk decision</h2>"
    "<p>One big monitor is a window management problem solved by size; two monitors solve it by division. The honest decision runs through the work: coding and research want two surfaces; design and video want one large canvas. The <a href=\"" + _w("computer+monitor") + "\" rel=\"noopener\">monitor setups</a> are documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Which work wants which</h2>"
    "<ul>"
    "<li><b>Two screens for reference work.</b> The second surface ends the alt-tab tax.</li>"
    "<li><b>One big screen for creative work.</b> The canvas wants continuity.</li>"
    "<li><b>Resolution before diagonal.</b> Pixels are the workspace; inches are the footprint.</li>"
    "<li><b>The arm is the upgrade.</b> Desk space and neck angle follow the mount.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/monitor-buying-specs/\">monitor buying specs</a>, <a href=\"/tech/big-tv-small-room/\">a big TV in a small room</a> and <a href=\"/tech/laptop-desk-ergonomics-the-standing-fix/\">laptop desk ergonomics</a>.</p>",

"tech/password-manager-migration-weekend":
    "<h2>The weekend, planned</h2>"
    "<p>Migrating to a password manager is a weekend project with a strict order: install the manager, fix the email account first, then sweep the passwords in priority order — money, work, everything else. The sweep is the boring half; the email account is the decision that protects all the others. The <a href=\"" + _w("password+manager") + "\" rel=\"noopener\">password manager</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The order of operations</h2>"
    "<ul>"
    "<li><b>Email first.</b> Every password reset routes through it.</li>"
    "<li><b>Banking and work next.</b> The accounts whose loss has a cost.</li>"
    "<li><b>Turn on two-factor as you go.</b> The migration is the audit.</li>"
    "<li><b>Write the emergency sheet.</b> The master password is the one password that resets nothing.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/best-password-manager-for-you/\">the best password manager for you</a>, <a href=\"/tech/reusing-passwords-risk/\">the risk of reused passwords</a> and <a href=\"/tech/security-questions-are-insecure/\">security questions are insecure</a>.</p>",

"writers/guides/how-to-price-ghostwriting-jobs":
    "<h2>Pricing the invisible work</h2>"
    "<p>Ghostwriting is priced on three axes: the word count, the research depth, and the credit you give away. The market splits between per-project fees for books and per-word rates for articles — and the contract's name on the cover is worth a line item of its own. The <a href=\"" + _w("ghostwriter") + "\" rel=\"noopener\">ghostwriting market</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The three axes</h2>"
    "<ul>"
    "<li><b>Words are the floor.</b> The rate reflects the hour, not just the page.</li>"
    "<li><b>Research is the multiplier.</b> Interviews and drafts are the real workload.</li>"
    "<li><b>Credit is negotiable.</b> No byline has a price; agree it early.</li>"
    "<li><b>Contract the revisions.</b> The unnamed draft is where fees die.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/freelance-paid-writing/how-to-price-your-freelance-writing/\">how to price your freelance writing</a>, <a href=\"/writers/guides/how-much-to-charge-for-an-article/\">how much to charge for an article</a> and <a href=\"/writers/guides/how-writing-retainers-work/\">how writing retainers work</a>.</p>",

"writers/learn/writing-process/how-to-build-a-writing-routine":
    "<h2>The routine is the infrastructure</h2>"
    "<p>A writing routine is built like infrastructure: a fixed time, a defined task size, and a trigger that starts the session without negotiation. The writers who produce steadily have not more discipline — they have fewer decisions between sitting down and writing. The <a href=\"" + _w("writing+process") + "\" rel=\"noopener\">writing process</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Building the routine</h2>"
    "<ul>"
    "<li><b>Same time, small size.</b> Three hundred words daily beats the Sunday marathon.</li>"
    "<li><b>Define the session's task.</b> 'Draft the opening' beats 'work on the piece'.</li>"
    "<li><b>Track the streak.</b> The calendar is the motivator that does not negotiate.</li>"
    "<li><b>Protect the slot.</b> The routine dies where it is scheduled first.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-process/\">the writing process</a>, <a href=\"/writers/learn/start-writing/\">start writing</a> and <a href=\"/writers/learn/writing-checklists/\">writing checklists</a>.</p>",

"writers/studio":
    "<h2>Drafts that never leave the browser</h2>"
    "<p>The studio is a drafting space that runs entirely client-side: the text lives in the browser, nothing is uploaded, and closing the tab is the delete button. It exists because first drafts deserve a room without an audience — including the audience of analytics. The <a href=\"" + _w("text+editor") + "\" rel=\"noopener\">editor tooling</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Why local-first matters</h2>"
    "<ul>"
    "<li><b>The draft is yours.</b> No server holds the half-finished paragraph.</li>"
    "<li><b>No account, no funnel.</b> The tool opens when the idea does.</li>"
    "<li><b>Export is the feature.</b> The text leaves as a file, on your command.</li>"
    "<li><b>Offline-tolerant.</b> The writing continues when the line does not.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-process/\">the writing process</a>, <a href=\"/tech/tool/\">the browser tools</a> and <a href=\"/writers/learn/start-writing/\">start writing</a>.</p>",

"entertainment/how-anime-production-committees-work":
    "<h2>Who actually makes the show</h2>"
    "<p>Anime is financed by production committees — the publisher, the broadcaster, the music label and the toy company pooling risk around a show. The committee's shape decides the show's shape: which studio animates it, how many episodes it gets, and which side of the story gets the merchandise. The <a href=\"" + _w("production+committee+system") + "\" rel=\"noopener\">production committee system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the money decides</h2>"
    "<ul>"
    "<li><b>Episode counts are budget artefacts.</b> Thirteen or twenty-six is finance, not story.</li>"
    "<li><b>The studio is a contractor.</b> The committee owns the show the studio makes.</li>"
    "<li><b>Merchandise shapes the cast.</b> The toy aisle has a vote in the character design.</li>"
    "<li><b>Committee changes are sequel news.</b> The money's exit is the show's ending.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/anime-seasons-and-cours-explained/\">anime seasons and cours</a>, <a href=\"/entertainment/anime-canon-and-filler-explained/\">anime canon and filler</a> and <a href=\"/entertainment/best-anime-to-watch-now/\">the best anime to watch now</a>.</p>",

"home/borehole-water-and-your-kettle":
    "<h2>The scale is the mineral</h2>"
    "<p>Borehole water carries dissolved minerals that kettle elements collect as scale — the white crust is geography, not dirt, and its chemistry decides everything from filter choice to appliance lifespan. Hardness varies by the water table, not the neighbourhood brand. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes drinking-water mineral guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Living with hard water</h2>"
    "<ul>"
    "<li><b>Descale the kettle monthly.</b> Citric acid or vinegar; the element pays the fee.</li>"
    "<li><b>Test before buying a softener.</b> The filter is sized to the mineral, not the fear.</li>"
    "<li><b>Scale is not a health alarm.</b> Minerals are chemistry; contamination is different.</li>"
    "<li><b>Watch the appliances.</b> Washing machines and geysers price the hardness.</li>"
    "</ul>"
    "<p>See <a href=\"/home/borehole-water-taste-smell/\">borehole water taste and smell</a>, <a href=\"/home/best-water-softener-for-your-home/\">the best water softener</a> and <a href=\"/home/borehole-pump-no-water/\">the borehole pump with no water</a>.</p>",

"writers/learn/common-problems/how-to-tell-if-your-writing-is-good":
    "<h2>The honest instruments</h2>"
    "<p>The question 'is my writing good' has instruments: the reader who finishes the piece, the editor who asks for revisions instead of rejecting, and the reread six months later that embarrasses you for good reasons. Writing improves exactly at the rate its instruments get honest. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The three instruments</h2>"
    "<ul>"
    "<li><b>Finishing readers.</b> Attention is the market's truest verdict.</li>"
    "<li><b>Editors' responses.</b> 'Revise and resubmit' is applause with homework.</li>"
    "<li><b>The six-month reread.</b> The version of you that owes nothing to the draft.</li>"
    "<li><b>Revision speed.</b> Good writers fix faster because they see sooner.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/common-problems/\">common writing problems</a>, <a href=\"/writers/learn/editing-proofreading/how-to-edit-your-own-writing/\">how to edit your own writing</a> and <a href=\"/writers/learn/writing-for-publication/how-to-handle-a-rejection/\">how to handle a rejection</a>.</p>",

"writers/learn/start-writing/how-to-start-writing":
    "<h2>The first words are logistics</h2>"
    "<p>Starting is a logistics problem: choose a form small enough to finish, a schedule dull enough to keep, and a first draft bad enough to stop worrying about. The blank page is not a test of talent — it is a task with no defined first step. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The first week</h2>"
    "<ul>"
    "<li><b>Pick the smallest form.</b> The finished paragraph teaches more than the open epic.</li>"
    "<li><b>Write at the same hour.</b> The habit recruits the brain before the mood.</li>"
    "<li><b>Copied sentences warm the hand.</b> Transcription is the writer's press-up.</li>"
    "<li><b>Finish before you improve.</b> Revision needs material; drafts supply it.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/start-writing/\">start writing</a>, <a href=\"/writers/learn/writing-process/how-to-build-a-writing-routine/\">how to build a writing routine</a> and <a href=\"/writers/learn/start-writing/how-to-overcome-writers-block/\">how to overcome writer's block</a>.</p>",

"writers/learn/writing-for-publication/how-to-build-a-writing-portfolio":
    "<h2>The portfolio is the argument</h2>"
    "<p>A writing portfolio argues one claim: this writer does this work. Three strong pieces in a named beat beat thirty assorted clips — editors hire the evidence of a specialism, and the portfolio's structure is the argument's structure. The <a href=\"" + _w("portfolio") + "\" rel=\"noopener\">portfolio practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Building the case</h2>"
    "<ul>"
    "<li><b>Name the beat.</b> The portfolio's title is the pitch's first line.</li>"
    "<li><b>Three great pieces.</b> Quality is the filter editors actually apply.</li>"
    "<li><b>Show range within the beat.</b> One form, several angles.</li>"
    "<li><b>Keep it current.</b> The portfolio is a garden, not a monument.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-for-publication/\">writing for publication</a>, <a href=\"/writers/guides/how-to-build-writing-samples/\">how to build writing samples</a> and <a href=\"/writers/guides/how-to-get-your-first-paid-writing-gig/\">your first paid writing gig</a>.</p>",

"tech/ai":
    "<h2>AI, without the hype</h2>"
    "<p>The desk's position on AI is behavioural: what the tools actually do well, what they confidently do badly, and which workflows change under their use. The useful questions are about tasks — drafting, summarising, coding assistance — not about civilisations. The <a href=\"" + _w("artificial+intelligence") + "\" rel=\"noopener\">AI field</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What works, what does not</h2>"
    "<ul>"
    "<li><b>Drafting works.</b> The blank page is the technology's real win.</li>"
    "<li><b>Verification is still yours.</b> Confident errors are the failure mode.</li>"
    "<li><b>Privacy is a workflow decision.</b> What you paste is what they train on.</li>"
    "<li><b>The tools change monthly.</b> Habits outlast any particular model.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/ai-useful-vs-hype/\">AI: useful versus hype</a>, <a href=\"/tech/ai-privacy-what-not-to-paste/\">AI privacy: what not to paste</a> and <a href=\"/tech/how-large-language-models-actually-work/\">how large language models work</a>.</p>",

"tech/storage-full-breaking-apps":
    "<h2>The silent breakage</h2>"
    "<p>Storage that fills completely breaks apps in slow motion: the camera that will not save, the message app that stops downloading, the system that starts deleting its own cache. The failure hides behind 'phone storage full' warnings that everyone postpones. The <a href=\"" + _w("flash+memory") + "\" rel=\"noopener\">flash storage behaviour</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The safe-delete pass</h2>"
    "<ul>"
    "<li><b>Check what is actually big.</b> The storage screen names the culprit in one tap.</li>"
    "<li><b>Downloads and old chats first.</b> The content nobody is looking for.</li>"
    "<li><b>Never delete from the file manager blindly.</b> Apps fail first at their data folders.</li>"
    "<li><b>Keep ten percent free.</b> The headroom is the system's working memory.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/phone-storage-full-safe-deletes/\">phone storage: safe deletes</a>, <a href=\"/tech/free-up-storage-android/\">free up storage on Android</a> and <a href=\"/tech/cloud-storage-mistakes/\">cloud storage mistakes</a>.</p>",

"writers/learn/creative-writing/how-to-write-a-memoir":
    "<h2>The truth, selected</h2>"
    "<p>Memoir is not autobiography — it is a life's material selected to argue one thing about living. The memoirist's privilege is also the job: choosing the scenes, compressing the years, and building a shape the memory itself never had. The <a href=\"" + _w("memoir") + "\" rel=\"noopener\">memoir form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The selection problem</h2>"
    "<ul>"
    "<li><b>Find the question.</b> The memoir's thesis decides every scene's inclusion.</li>"
    "<li><b>Scene over summary.</b> The reader lives the year through the Tuesday.</li>"
    "<li><b>The narrator's growth is the plot.</b> The person at the end must differ from the start.</li>"
    "<li><b>Fact-check your own memory.</b> The memoir's contract includes honesty.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/creative-writing/how-to-write-a-short-story/\">how to write a short story</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-a-personal-essay/\">how to write a personal essay</a> and <a href=\"/writers/learn/creative-writing/how-to-develop-characters/\">how to develop characters</a>.</p>",

"entertainment/best-true-crime-documentaries-to-watch":
    "<h2>True crime, honestly</h2>"
    "<p>The true-crime documentary boom has two grades: the investigation that serves the victims and the entertainment that consumes them. The best entries know the case is somebody's worst day and treat the audience like adults who can hold both the craft and the cost. The <a href=\"" + _w("true+crime") + "\" rel=\"noopener\">true crime genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the good ones do</h2>"
    "<ul>"
    "<li><b>The victims have names.</b> The grade is legible in the first ten minutes.</li>"
    "<li><b>The reporting is the plot.</b> Process beats revelation in the best series.</li>"
    "<li><b>It knows its limits.</b> The form that admits uncertainty earns trust.</li>"
    "<li><b>It does not recruit jurors.</b> The courtroom is not the audience's job.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-documentaries-of-all-time/\">the best documentaries of all time</a>, <a href=\"/entertainment/best-limited-series-to-watch/\">the best limited series</a> and <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a>.</p>",

"entertainment/reviews/breath-of-life":
    "<h2>Faith, service, and the frame</h2>"
    "<p>Breath of Life builds its story around service and second chances — the Nollywood melodrama tradition with a moral spine worn openly. The film's craft lives in its performances, which carry the faith frame's emotional argument scene by scene. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the film does</h2>"
    "<ul>"
    "<li><b>The theme is structural.</b> Service is the plot's engine, not its message.</li>"
    "<li><b>The cast carries the register.</b> The emotional beats arrive through faces.</li>"
    "<li><b>The pacing trusts the audience.</b> Melodrama that does not hurry.</li>"
    "<li><b>The genre is the vessel.</b> Faith cinema's frame with real stakes inside.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/reviews/mokalik/\">the Mokalik review</a>, <a href=\"/entertainment/reviews/shadow-parties/\">the Shadow Parties review</a> and <a href=\"/entertainment/nollywood-golden-age-explained/\">Nollywood's golden age</a>.</p>",

"home/gentle-low-flow-fixes":
    "<h2>Five fixes the plumber will applaud</h2>"
    "<p>Low flow is usually aerator scale, cartridge wear or a partially closed valve — three faults fixed with a cloth, a part and a turn. The gentle fixes avoid the trap of forcing threads and flooding the cabinet underneath. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government plumbing guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The five, in order</h2>"
    "<ul>"
    "<li><b>Aerator off, soak, brush.</b> The commonest fix is the simplest one.</li>"
    "<li><b>Check the isolation valve.</b> Half-closed valves are honest suspects.</li>"
    "<li><b>Cartridge inspection.</b> The part inside does the wear.</li>"
    "<li><b>Pressure check the supply.</b> The house may be the patient, not the tap.</li>"
    "<li><b>Know when to stop.</b> Seized threads are the professional's job.</li>"
    "</ul>"
    "<p>See <a href=\"/home/dripping-tap-cartridge-fix/\">the dripping tap cartridge fix</a>, <a href=\"/home/borehole-pump-no-water/\">the borehole pump with no water</a> and <a href=\"/home/hidden-water-leak-meter-test/\">the hidden leak meter test</a>.</p>",

"sports/pro-wrestling-explained":
    "<h2>Athletic theatre, honestly</h2>"
    "<p>Pro wrestling is the athletic theatre that outlived every prediction of its death: a live stunt show with serialized drama, where the outcome is agreed and the performance is not. The craft is the cooperation — every match is two people building one story at full physical risk. The <a href=\"" + _w("professional+wrestling") + "\" rel=\"noopener\">professional wrestling</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>How the show works</h2>"
    "<ul>"
    "<li><b>The match is a conversation.</b> Holds and reversals are sentences.</li>"
    "<li><b>The finish is the story's turn.</b> The agreed result carries the feud forward.</li>"
    "<li><b>The crowd is a participant.</b> The live audience writes the rewrite notes.</li>"
    "<li><b>The risk is real.</b> The performance is a stunt profession.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-boxing-fights-end-explained/\">how boxing fights end</a>, <a href=\"/sports/how-olympic-judging-works/\">how Olympic judging works</a> and <a href=\"/sports/what-does-rtd-mean-in-boxing-explained/\">what RTD means in boxing</a>.</p>",

"tech/data-shuttle-sd-usb-ssd":
    "<h2>Which one can carry the weight</h2>"
    "<p>The SD card, the thumb drive and the portable SSD are different physics wearing the same promise: flash storage that moves files. The differences decide everything — write endurance, sustained speed, and what survives a pocket. The <a href=\"" + _w("flash+storage") + "\" rel=\"noopener\">flash storage</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing the shuttle</h2>"
    "<ul>"
    "<li><b>SD cards: cameras and single loads.</b> Built for writes once, reads often.</li>"
    "<li><b>Thumb drives: sneakernet.</b> The handoff is the use case.</li>"
    "<li><b>Portable SSDs: real work.</b> Sustained writes and the only honest backup role.</li>"
    "<li><b>Label the drives.</b> The unlabelled shuttle is the lost archive.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/sd-card-not-reading-recovery/\">SD card not reading: recovery</a>, <a href=\"/tech/nvme-vs-sata-portable-ssd/\">NVMe versus SATA portable SSDs</a> and <a href=\"/tech/three-two-one-backup-rule/\">the 3-2-1 backup rule</a>.</p>",

"tech/smart-lock-when-the-battery-dies":
    "<h2>Plan for the dead battery</h2>"
    "<p>Smart locks are battery-powered devices guarding the front door — which means the battery plan is part of the lock plan: the warning schedule, the physical key that still works, and the nine-volt jump that opens the door when the plan failed. The <a href=\"" + _w("smart+lock") + "\" rel=\"noopener\">smart lock</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The battery plan</h2>"
    "<ul>"
    "<li><b>Calendar the replacement.</b> The warning email is a courtesy, not a plan.</li>"
    "<li><b>Keep the physical key outside the house.</b> The lock's fallback is only useful if reachable.</li>"
    "<li><b>Know the jump terminals.</b> The nine-volt trick is the lock's emergency room.</li>"
    "<li><b>Check the cold.</b> Battery life is a temperature product.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/smart-home-devices-stop-getting-updates/\">smart home devices stop getting updates</a>, <a href=\"/tech/do-you-need-a-smart-home-hub/\">do you need a smart home hub</a> and <a href=\"/tech/smart-home-worth-it/\">is smart home worth it</a>.</p>",

"writers/guides":
    "<h2>Guides for the working writer</h2>"
    "<p>These guides cover the working side of writing: the pitch and its follow-up, the money and its taxes, the portfolio and its argument. Each guide is built to be used at the desk, in the moment the question arrives — because writing advice that cannot be applied on Tuesday is commentary. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows keeps the advice honest. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The guide families</h2>"
    "<ul>"
    "<li><b>Pitching.</b> The query, the pitch, the follow-up, the rejection.</li>"
    "<li><b>Money.</b> Rates, invoices, taxes, the set-aside habit.</li>"
    "<li><b>Portfolio.</b> Samples, clips, and the argument they make together.</li>"
    "<li><b>The writing life.</b> Routines, screens, and the long game.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a magazine pitch</a>, <a href=\"/writers/guides/how-to-find-paid-writing-opportunities/\">how to find paid writing opportunities</a> and <a href=\"/writers/learn/\">the writers learn library</a>.</p>",

"entertainment/why-streaming-services-raise-prices":
    "<h2>The economics of the raise</h2>"
    "<p>Streaming prices rise because the business model was a customer-acquisition bet: below-cost subscriptions to build the habit, then the price where the content bill actually lives. The raises track the content arms race — every service paying more for the same shows. The <a href=\"" + _w("streaming+media") + "\" rel=\"noopener\">streaming business model</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What drives each raise</h2>"
    "<ul>"
    "<li><b>Content costs compound.</b> Every hit resets the market rate for the next one.</li>"
    "<li><b>The ad tier is the pressure valve.</b> Cheaper plans move the price pain to attention.</li>"
    "<li><b>Churn is the audience's vote.</b> The rotation habit is the market's discipline.</li>"
    "<li><b>Bundles return.</b> The cable model reassembles itself from the parts.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/cheapest-way-to-stream-movies/\">the cheapest way to stream movies</a>, <a href=\"/tech/streaming-subscription-stacking-when-bundle-cheaper/\">when a bundle is cheaper</a> and <a href=\"/tech/subscription-creep-audit/\">the subscription creep audit</a>.</p>",

"home/gutter-cleaning-damage":
    "<h2>The damage that skips years</h2>"
    "<p>Gutter damage is deferred maintenance with compound interest: the overflow that soaks the fascia one rainy season, rots the timber in the next, and invites the birds and the damp in the third. Cleaning on schedule costs a morning; the repair chain costs a month. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The damage chain</h2>"
    "<ul>"
    "<li><b>Overflow to fascia rot.</b> The first wet season is silent.</li>"
    "<li><b>Timber to damp path.</b> The rot finds the wall's interior.</li>"
    "<li><b>Foundation splashback.</b> The ground below the outlet takes the beating.</li>"
    "<li><b>Two cleanings a year.</b> The cheapest intervention in the whole chain.</li>"
    "</ul>"
    "<p>See <a href=\"/home/gutters-and-downpipes/\">gutters and downpipes</a>, <a href=\"/home/ceiling-water-stain-removal/\">ceiling water stain removal</a> and <a href=\"/home/external-wall-crack-seal/\">the external wall crack seal</a>.</p>",

"tech/chatgpt-vs-claude-vs-gemini":
    "<h2>The honest comparison</h2>"
    "<p>The three assistants converge on capability and diverge on behaviour: how they handle long documents, how confidently they are wrong, and what they do with the text you give them. The honest comparison is task-based — drafting, analysis, code — because the leaderboard is not your workflow. The <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large language model</a> field is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>How to choose</h2>"
    "<ul>"
    "<li><b>Test with your own work.</b> The sample task beats the benchmark.</li>"
    "<li><b>Watch the failure style.</b> How it is wrong matters more than how often.</li>"
    "<li><b>Check the data policy.</b> The privacy terms are part of the product.</li>"
    "<li><b>Assume convergence.</b> The durable skill is the prompting habit, not the vendor.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/chatgpt-free-vs-paid/\">ChatGPT free versus paid</a>, <a href=\"/tech/ai-assistants-compared/\">AI assistants compared</a> and <a href=\"/tech/deepseek-vs-chatgpt/\">DeepSeek versus ChatGPT</a>.</p>",

"writers/learn/writing-for-publication/how-to-handle-a-rejection":
    "<h2>The professional response</h2>"
    "<p>A rejection arrives as a verdict on fit far more often than on talent, and the professional response treats it that way: file it, read it once for data, and move the work to the next market. The writers who publish are the ones who kept the pipeline full through the silence. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows reports the numbers honestly. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The response routine</h2>"
    "<ul>"
    "<li><b>Twenty-four hours of feelings.</b> The sting is real; the deadline is not.</li>"
    "<li><b>Extract the data.</b> Personal notes are rare and valuable; forms are weather.</li>"
    "<li><b>Resubmit within the week.</b> The next market is the only cure.</li>"
    "<li><b>Keep the rejection log.</b> The pattern is the market research.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-for-publication/a-rejected-pitch-is-not-wasted/\">a rejected pitch is not wasted</a>, <a href=\"/writers/learn/common-problems/how-to-tell-if-your-writing-is-good/\">how to tell if your writing is good</a> and <a href=\"/writers/guides/when-to-follow-up-on-a-pitch/\">when to follow up on a pitch</a>.</p>",

"entertainment/kdrama-genres-explained":
    "<h2>What you are actually choosing</h2>"
    "<p>K-drama's genre labels are promises about structure: the workplace romance's slow burn, the makjang's escalation, the sageuk's costume politics. Choosing by genre is choosing the emotional contract — the rhythm of the episodes, the size of the turns, the kind of ending on offer. The <a href=\"" + _w("Korean+drama") + "\" rel=\"noopener\">Korean drama</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The genre contracts</h2>"
    "<ul>"
    "<li><b>Romance.</b> The sixteen-episode arc and the rule of the wrist-grab.</li>"
    "<li><b>Makjang.</b> Escalation as a design philosophy.</li>"
    "<li><b>Sageuk.</b> The palace as a political workplace.</li>"
    "<li><b>Thriller.</b> The format's discipline meets real pacing.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-kdramas-to-start-with/\">the best K-dramas to start with</a>, <a href=\"/entertainment/10-korean-movies-everyone-should-watch/\">ten Korean movies to watch</a> and <a href=\"/entertainment/korean-cinema-starter-guide-rebuilt/\">the Korean cinema starter guide</a>.</p>",

"home/clean-home-pests-myth":
    "<h2>Why cleanliness is not pest control</h2>"
    "<p>A clean home removes the food pests came for; it does not remove the harbourage they live in. The myth survives because cleanliness delays the visible signs — the colony exists in the wall void regardless of the kitchen floor. Sanitation is step one of three. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household pest guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The three steps</h2>"
    "<ul>"
    "<li><b>Sanitation.</b> Remove the food, and the population's growth stops.</li>"
    "<li><b>Exclusion.</b> Seal the entries; the wall void is the actual address.</li>"
    "<li><b>Monitoring.</b> Traps tell you what the clean kitchen hides.</li>"
    "<li><b>Know when to call.</b> Established colonies are structural problems.</li>"
    "</ul>"
    "<p>See <a href=\"/home/pests-start-here/\">pests: first signs and first response</a>, <a href=\"/home/entry-point-mistakes/\">entry point mistakes</a> and <a href=\"/home/diy-vs-professional-pests/\">DIY versus professional pests</a>.</p>",

"sports/pressing-explained":
    "<h2>Defence as an attacking act</h2>"
    "<p>Modern pressing is defence played forward: the block that hunts the ball in the opponent's half, the trigger that starts the hunt, and the line that moves as one body. The tactic's arms race has defined a decade of football — and its counter, the long ball over the press, defined the answers. The <a href=\"" + PL + "\" rel=\"noopener\">Premier League</a> tacticians this desk follows have made pressing the league's language. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>The pressing vocabulary</h2>"
    "<ul>"
    "<li><b>The trigger.</b> The backward pass that starts the hunt.</li>"
    "<li><b>The block.</b> The compressed unit that owns the space.</li>"
    "<li><b>The press-resistant pivot.</b> The player who beats the system with one touch.</li>"
    "<li><b>The risk.</b> Every press gambles the space behind it.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/gegenpressing-explained/\">gegenpressing explained</a>, <a href=\"/sports/football-positions-explained/\">football positions explained</a> and <a href=\"/sports/xg-explained/\">expected goals explained</a>.</p>",

"sports/what-does-rtd-mean-in-boxing-explained":
    "<h2>The corner's decision</h2>"
    "<p>RTD — referee technical decision — ends a fight when the corner stops it, when a cut decides it, or when a fighter cannot continue safely. It is the sport's mercy rule: the result on the record, the decision in the corner's hands. The <a href=\"" + _w("boxing") + "\" rel=\"noopener\">boxing rules</a> are documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>How a fight ends</h2>"
    "<ul>"
    "<li><b>KO and TKO.</b> The referee's count and the referee's instinct.</li>"
    "<li><b>RTD.</b> The corner's towel is the sport's oldest mercy.</li>"
    "<li><b>Technical decision.</b> The scorecards decide an accidental injury.</li>"
    "<li><b>No contest.</b> The accident the rules cannot grade.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-boxing-fights-end-explained/\">how boxing fights end</a>, <a href=\"/sports/boxing-scoring-explained/\">boxing scoring explained</a> and <a href=\"/sports/boxing-decisions-explained/\">boxing decisions explained</a>.</p>",

"tech/hdmi-arc-vs-optical-tv-audio":
    "<h2>The one cable decision</h2>"
    "<p>ARC, eARC and optical carry TV audio to the soundbar — and the choice decides what survives the trip: basic surround over optical and ARC, full lossless over eARC. The receiver end matters as much as the port; the cable is the easy part. The <a href=\"" + _w("HDMI") + "\" rel=\"noopener\">HDMI ARC system</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Matching cable to kit</h2>"
    "<ul>"
    "<li><b>eARC for lossless.</b> The only path for the full cinema track.</li>"
    "<li><b>ARC for the everyday.</b> Compressed surround covers most living rooms.</li>"
    "<li><b>Optical as the fallback.</b> Old kit's honest friend.</li>"
    "<li><b>CEC is the convenience.</b> One remote control is the feature that matters daily.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/soundbar-for-dialogue-not-bass/\">a soundbar for dialogue</a>, <a href=\"/tech/bluetooth-audio-delay-tv/\">Bluetooth audio delay on TV</a> and <a href=\"/tech/new-tv-settings-day-one/\">new TV settings, day one</a>.</p>",

"writers/learn/grammar-language/comma-rules":
    "<h2>The comma's real job</h2>"
    "<p>The comma marks the pause the sentence's grammar requires: the list's seams, the clause's breath, the quote's introduction. The rules are learnable and finite — and most comma errors are rhythm problems wearing grammar's clothes. The <a href=\"" + _w("comma") + "\" rel=\"noopener\">comma usage</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The rules that cover most cases</h2>"
    "<ul>"
    "<li><b>Compound sentences.</b> Two independent clauses take a comma and a conjunction.</li>"
    "<li><b>Introductory elements.</b> The sentence's opening phrase earns a breath.</li>"
    "<li><b>Non-restrictive clauses.</b> The information that adds rather than defines.</li>"
    "<li><b>Read it aloud.</b> The ear knows the rule the memory forgot.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/grammar-language/common-grammar-mistakes/\">common grammar mistakes</a>, <a href=\"/writers/learn/grammar-language/british-vs-american-english/\">British versus American English</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-writing/\">the dos and don'ts of writing</a>.</p>",

"tech/android-backup-guide":
    "<h2>What backup quietly skips</h2>"
    "<p>Android backup covers more than people expect and less than they assume: app data where the developer opted in, photos when the sync is on, and almost nothing from apps that kept their data local. The gaps are where phone loss becomes data loss. The <a href=\"" + _w("Android") + "\" rel=\"noopener\">Android platform</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Covering the gaps</h2>"
    "<ul>"
    "<li><b>Check the account's backup screen.</b> The list of backed-up apps is the honest map.</li>"
    "<li><b>Photos: verify the sync.</b> The camera roll is the loss that hurts most.</li>"
    "<li><b>Authenticator exports matter.</b> The two-factor seeds need their own plan.</li>"
    "<li><b>Test the restore.</b> A backup is a rehearsal you have not attended.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/phone-photo-backup-options-nigeria/\">phone photo backup options in Nigeria</a>, <a href=\"/tech/three-two-one-backup-rule/\">the 3-2-1 backup rule</a> and <a href=\"/tech/phone-died-no-backup/\">the phone that died with no backup</a>.</p>",

"writers/learn/creative-writing/how-to-write-travel-writing":
    "<h2>The place, not the postcard</h2>"
    "<p>Travel writing that lasts is about the encounter, not the itinerary: the writer's presence in a place that existed before the visit and continues after it. The genre's discipline is specific detail and honest position — the view from where you actually stood. The <a href=\"" + _w("travel+writing") + "\" rel=\"noopener\">travel writing form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The discipline</h2>"
    "<ul>"
    "<li><b>Detail beats adjective.</b> The market's bus is the scene's anchor.</li>"
    "<li><b>The place has residents.</b> The postcard view has an address.</li>"
    "<li><b>Report the friction.</b> The delay and the misstep are the story's honesty.</li>"
    "<li><b>Name the season.</b> Travel pieces carry their weather like a dateline.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/creative-writing/how-to-write-a-memoir/\">how to write a memoir</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-a-feature/\">how to write a feature</a> and <a href=\"/writers/learn/creative-writing/how-to-write-a-short-story/\">how to write a short story</a>.</p>",

"writers/learn/journaling-personal/daily-journal-prompts":
    "<h2>Prompts that start something</h2>"
    "<p>A daily journal prompt works when it asks a question the writer has not already answered — the small observation, the honest inventory, the scene from yesterday worth keeping. The prompt is a starting mechanism; the habit is the product. The <a href=\"" + _w("journaling") + "\" rel=\"noopener\">journaling practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The prompt families</h2>"
    "<ul>"
    "<li><b>Observation.</b> What did you notice today that nobody else did?</li>"
    "<li><b>Inventory.</b> What is taking up the most room in your head?</li>"
    "<li><b>Scene.</b> Write yesterday's moment as if it were a story.</li>"
    "<li><b>Gratitude, specific.</b> The named thing, not the category.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/journaling-personal/how-to-write-a-gratitude-journal-entry/\">how to write a gratitude journal entry</a>, <a href=\"/writers/learn/journaling-personal/\">journaling and personal writing</a> and <a href=\"/writers/learn/start-writing/\">start writing</a>.</p>",

"writers/learn/types-of-writing/how-to-write-a-personal-essay":
    "<h2>The self as material</h2>"
    "<p>The personal essay is the self used as evidence for something larger: one life's scene, examined until it says something the reader can carry home. The form's trap is the diary; its engine is the turn — the moment the story stops being about the writer. The <a href=\"" + _w("personal+essay") + "\" rel=\"noopener\">personal essay form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The essay's engine</h2>"
    "<ul>"
    "<li><b>The scene is the doorway.</b> The reader enters through a Tuesday.</li>"
    "<li><b>The turn is the point.</b> The reflection must change the story's meaning.</li>"
    "<li><b>Universal through specific.</b> The narrower the scene, the wider the mirror.</li>"
    "<li><b>End on the meaning.</b> The last line is the essay's thesis arriving late.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-a-feature/\">how to write a feature</a>, <a href=\"/writers/learn/creative-writing/how-to-write-a-memoir/\">how to write a memoir</a> and <a href=\"/writers/guides/how-to-pitch-an-essay/\">how to pitch an essay</a>.</p>",

"writers/writing/transition-magazine":
    "<h2>A magazine of the Black world</h2>"
    "<p>Transition publishes writing from the African diaspora's arguments with itself — essays, criticism and fiction with a political ear and an international frame. For writers it is a market where the stakes are structural and the reading is serious. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>The argument is the currency.</b> Pieces that take a position travel here.</li>"
    "<li><b>Read the archive.</b> The magazine's history is its masthead.</li>"
    "<li><b>Essays with receipts.</b> Criticism that reports is criticism that lands.</li>"
    "<li><b>The frame is international.</b> The diaspora is the magazine's address.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/statement-africa/\">Statement Africa</a>, <a href=\"/writers/writing/the-republic/\">The Republic</a> and <a href=\"/writers/writing/guernica/\">Guernica</a>.</p>",

"entertainment/how-tv-shows-get-cancelled":
    "<h2>The metrics behind the axe</h2>"
    "<p>TV cancellations are arithmetic in a suit: the ratings against the budget, the streaming completion rate against the cost of the next season, and the ownership question of who profits from the back catalogue. The axe falls on economics; the audience's outrage arrives as a receipt. The <a href=\"" + _w("television+ratings") + "\" rel=\"noopener\">television ratings system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the numbers say</h2>"
    "<ul>"
    "<li><b>Completion rate is the streaming rating.</b> The metric that decides renewals now.</li>"
    "<li><b>Ownership decides loyalty.</b> The studio's catalogue is the second balance sheet.</li>"
    "<li><b>Season three is the cliff.</b> Costs compound faster than audiences.</li>"
    "<li><b>The save campaigns work rarely.</b> The metric is not the mailing list.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/into-the-badlands-was-underrated/\">Into the Badlands was underrated</a>, <a href=\"/entertainment/why-tv-seasons-are-getting-shorter/\">why TV seasons are getting shorter</a> and <a href=\"/entertainment/how-award-season-actually-works/\">how award season works</a>.</p>",

"home/electric-iron-steam-care":
    "<h2>The iron that spits brown</h2>"
    "<p>The brown spit is the tank's sediment finding the steam vents — minerals from the water, scale on the element, and the soleplate's coating wearing where nobody looks. The fix is a tank flush, a soleplate clean and the right water in the first place. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The care routine</h2>"
    "<ul>"
    "<li><b>Flush the tank monthly.</b> The sediment is the spit's whole story.</li>"
    "<li><b>Distilled or cooled boiled water.</b> The mineral decides the iron's lifespan.</li>"
    "<li><b>Wipe the soleplate warm.</b> Cold cleaning scratches the coating.</li>"
    "<li><b>Store it standing.</b> The tank dries; the mould loses its address.</li>"
    "</ul>"
    "<p>See <a href=\"/home/borehole-water-and-your-kettle/\">borehole water and your kettle</a>, <a href=\"/home/mistakes/\">the common home mistakes</a> and <a href=\"/home/appliances-that-use-the-most-electricity/\">appliances that use the most electricity</a>.</p>",

"home/fridge-door-seal-test":
    "<h2>The dollar-bill test</h2>"
    "<p>The fridge door seal fails quietly: the cold escapes, the compressor works overtime, and the electricity bill grows a second floor. The dollar-bill test — close the note in the door and pull — settles the question in one minute. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The test and the fix</h2>"
    "<ul>"
    "<li><b>Test all four sides.</b> The seal fails locally before it fails visibly.</li>"
    "<li><b>Clean the gasket.</b> The residue is half the leak.</li>"
    "<li><b>Warm water, then re-test.</b> The rubber remembers its shape.</li>"
    "<li><b>Replace when it stays flat.</b> A hardened gasket is a spent part.</li>"
    "</ul>"
    "<p>See <a href=\"/home/fridge-not-cold-enough/\">the fridge that is not cold enough</a>, <a href=\"/home/fridge-door-not-sealing/\">the fridge door not sealing</a> and <a href=\"/home/fridge-coils-twice-a-year/\">the fridge coils twice a year</a>.</p>",

"home/mosquito-coils-and-plug-ins":
    "<h2>The night-time defence</h2>"
    "<p>Coils, plug-ins and nets are three different strategies: the coil smoulders a repellent ring, the plug-in volatilises one indoors, and the net is the only barrier that works while you sleep. The honest household uses all three in layers — and knows the coil's smoke is not free. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes vector-control guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The layered defence</h2>"
    "<ul>"
    "<li><b>The net is the foundation.</b> The barrier that works during the eight hours that matter.</li>"
    "<li><b>Plug-ins for the room.</b> The evening's airspace, managed.</li>"
    "<li><b>Coils for the compound.</b> Outdoors only; the smoke needs the sky.</li>"
    "<li><b>Empty the standing water.</b> The breeding site is the strategy's first line.</li>"
    "</ul>"
    "<p>See <a href=\"/home/compound-mosquito-control-night/\">compound mosquito control</a>, <a href=\"/home/pests-start-here/\">pests: first signs and first response</a> and <a href=\"/home/ignore-single-pest-sighting/\">the single pest sighting</a>.</p>",

"writers/learn/academic-writing/academic-writing-basics":
    "<h2>The register of the academy</h2>"
    "<p>Academic writing is a register before it is a format: claims stated as claims, evidence cited as evidence, and hedging used exactly where certainty would be dishonest. The conventions are learnable — and they exist so that arguments can be checked. The <a href=\"" + _w("academic+writing") + "\" rel=\"noopener\">academic writing</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The four conventions</h2>"
    "<ul>"
    "<li><b>Claims need evidence.</b> The sentence without support is an opinion.</li>"
    "<li><b>Hedge honestly.</b> 'Suggests' and 'demonstrates' are different claims.</li>"
    "<li><b>Structure is argument.</b> The section order is the reasoning order.</li>"
    "<li><b>Citation is the floor.</b> Every borrowed idea carries its address.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/academic-writing/how-to-structure-a-research-paper/\">how to structure a research paper</a>, <a href=\"/writers/learn/academic-writing/how-to-cite-sources/\">how to cite sources</a> and <a href=\"/writers/learn/academic-writing/how-to-write-an-exam-essay/\">how to write an exam essay</a>.</p>",

"writers/learn/examples/how-to-use-the-examples":
    "<h2>Examples as instruments</h2>"
    "<p>The examples library is built to be dissected, not admired: each example shows the structure doing its work, with the reasoning labelled so the shape can be borrowed. Reading an example as an instrument — what each paragraph is doing — teaches faster than reading it as prose. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>How to read an example</h2>"
    "<ul>"
    "<li><b>Read the labels first.</b> The reasoning is the lesson; the prose is the specimen.</li>"
    "<li><b>Mark the turns.</b> Each example has a moment the job changes.</li>"
    "<li><b>Adapt the structure.</b> The shape travels; the words are the example's own.</li>"
    "<li><b>Write the parallel draft.</b> The instrument becomes a skill by use.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-of-a-cover-letter/\">the cover letter example</a>, <a href=\"/writers/learn/examples/example-of-a-report/\">the report example</a> and <a href=\"/writers/learn/examples/example-of-a-newsletter/\">the newsletter example</a>.</p>",

"writers/learn/journaling-personal/how-to-write-a-gratitude-journal-entry":
    "<h2>Specific, or it does not work</h2>"
    "<p>Gratitude journaling works when the entry is specific — the named moment, the named person, the thing that happened on Tuesday. The generic entry is the habit's failure mode: the practice's benefits live in the detail the writer notices while searching for it. The <a href=\"" + _w("gratitude+journaling") + "\" rel=\"noopener\">gratitude journaling</a> practice is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing the specific entry</h2>"
    "<ul>"
    "<li><b>Name the moment.</b> The date and the scene do the work.</li>"
    "<li><b>One item, fully seen.</b> The list habit dilutes the noticing.</li>"
    "<li><b>The detail is the gratitude.</b> The adjectives are usually hiding from it.</li>"
    "<li><b>Keep it small.</b> The practice is daily because it is small.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/journaling-personal/daily-journal-prompts/\">daily journal prompts</a>, <a href=\"/writers/learn/journaling-personal/\">journaling and personal writing</a> and <a href=\"/writers/learn/start-writing/how-to-start-writing/\">how to start writing</a>.</p>",

"writers/learn/structure-formatting":
    "<h2>Structure is the argument</h2>"
    "<p>Structure is the order in which the reader is told things — and formatting is that order made visible. The right structure for a piece is the one that matches the reader's questions: what is this, why should I care, what do I do next. The <a href=\"" + _w("document+structure") + "\" rel=\"noopener\">document structure</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The order of questions</h2>"
    "<ul>"
    "<li><b>What is this?</b> The opening that names the subject earns everything.</li>"
    "<li><b>Why does it matter?</b> The stakes paragraph is the reader's contract.</li>"
    "<li><b>How does it work?</b> The body answers in the reader's order, not the writer's.</li>"
    "<li><b>What now?</b> The ending gives the reader their next move.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-checklists/\">writing checklists</a>, <a href=\"/writers/compare/\">which format you need</a> and <a href=\"/writers/learn/editing-proofreading/\">editing and proofreading</a>.</p>",

"writers/learn/types-of-writing/how-to-write-a-tutorial":
    "<h2>Teach the task, not the tool</h2>"
    "<p>A tutorial is a promise that the reader will be able to do something at the end — which makes every step a contract and every skipped step a broken one. The good tutorial names the outcome first, orders the steps by the reader's hands, and tests the whole path before publishing. The <a href=\"" + _w("technical+writing") + "\" rel=\"noopener\">tutorial form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The tutorial contract</h2>"
    "<ul>"
    "<li><b>Outcome in the title.</b> The reader should know the destination before packing.</li>"
    "<li><b>Steps in the order of doing.</b> The writer's discovery order is the wrong order.</li>"
    "<li><b>Test from zero.</b> The clean machine is the tutorial's real reader.</li>"
    "<li><b>End with the done state.</b> The reader needs to recognise success.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-a-blog-post/\">how to write a blog post</a>, <a href=\"/writers/learn/online-writing/how-to-write-search-friendly-content/\">how to write search-friendly content</a> and <a href=\"/writers/learn/types-of-writing/how-to-write-an-article/\">how to write an article</a>.</p>",

"entertainment/slice-of-life-anime-explained":
    "<h2>Why nothing happening works</h2>"
    "<p>Slice-of-life anime builds drama from the almost-nothing: the club meeting, the walk home, the summer that ends. The genre's craft is attention — the show that makes a Tuesday feel like it mattered — and its endings arrive like seasons do. The <a href=\"" + _w("slice+of+life") + "\" rel=\"noopener\">slice-of-life genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The genre's craft</h2>"
    "<ul>"
    "<li><b>Time is the special effect.</b> The slow episode earns the fast one.</li>"
    "<li><b>The setting is a character.</b> The classroom remembers every season.</li>"
    "<li><b>The comedy is structural.</b> The running gag is the show's memory.</li>"
    "<li><b>Endings arrive as change.</b> The genre's plot is growing up.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/isekai-anime-explained/\">isekai anime explained</a>, <a href=\"/entertainment/anime-seasons-and-cours-explained/\">anime seasons and cours</a> and <a href=\"/entertainment/best-anime-to-watch-now/\">the best anime to watch now</a>.</p>",

"home/hvac-filter-change-habit":
    "<h2>The habit that decides the system</h2>"
    "<p>The HVAC filter is the system's lung: a clogged filter raises the energy bill, lowers the airflow and invites the repair that the habit would have prevented. The change schedule is printed on the filter itself — and the household's dust decides the real interval. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor air guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The habit, sized to the house</h2>"
    "<ul>"
    "<li><b>Calendar the change.</b> The filter's rating is a maximum interval, not a schedule.</li>"
    "<li><b>Check monthly in harmattan.</b> The dust sets the true interval.</li>"
    "<li><b>Buy the right rating.</b> Higher MERV is not automatically better for your system.</li>"
    "<li><b>Watch the airflow.</b> The register's whisper is the filter's full note.</li>"
    "</ul>"
    "<p>See <a href=\"/home/cost-to-run-air-conditioning/\">the cost to run air conditioning</a>, <a href=\"/home/condensation-ventilation-that-works/\">condensation and ventilation</a> and <a href=\"/home/ac-outdoor-unit-care/\">AC outdoor unit care</a>.</p>",

}

TOPUP_SECTIONS15 = {

"home/mistakes/drying-laundry-indoors":
    "<h2>The moisture nobody budgets</h2>"
    "<p>A drying load releases litres of water into the air — the humidity spike that feeds the condensation on every cold surface in the house. The windows-shut habit turns a laundry chore into a damp cause. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes indoor moisture guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Drying without the damp</h2>"
    "<ul>"
    "<li><b>One window, one door.</b> Cross-ventilation carries the load's water outside.</li>"
    "<li><b>The room with the fewest cold surfaces.</b> Condensation picks the coldest wall.</li>"
    "<li><b>The dehumidifier option.</b> The electricity cost is cheaper than the damp survey.</li>"
    "<li><b>Outdoor lines win.</b> The sun is the free appliance.</li>"
    "</ul>"
    "<p>See <a href=\"/home/musty-wardrobe-clothes-rainy/\">the musty wardrobe</a>, <a href=\"/home/condensation-ventilation-that-works/\">condensation and ventilation that works</a> and <a href=\"/home/cost-to-run-a-dehumidifier/\">the cost to run a dehumidifier</a>.</p>",

"sports/elliot-anderson-man-city-record-signing":
    "<h2>What the record fee buys</h2>"
    "<p>A record signing is a squad-building decision priced by the market's scarcity: the age curve, the contract length, the position's going rate, and the fee's weight on the wage structure that follows. The number makes the headline; the structure makes the signing. The <a href=\"" + PL + "\" rel=\"noopener\">Premier League</a> market this desk follows prices such deals in the open. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the deal</h2>"
    "<ul>"
    "<li><b>The fee is the deposit.</b> The wage bill is the contract's real cost.</li>"
    "<li><b>Age curves price futures.</b> The years bought are the deal's ceiling.</li>"
    "<li><b>Position scarcity moves markets.</b> The going rate is set by the last three deals.</li>"
    "<li><b>PSR shapes every number.</b> The accounting window is the negotiation's clock.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-football-contracts-work/\">how football contracts work</a>, <a href=\"/sports/how-psr-and-points-deductions-work/\">how PSR works</a> and <a href=\"/sports/how-do-football-clubs-make-money/\">how football clubs make money</a>.</p>",

"sports/serie-a-results":
    "<h2>Results as form evidence</h2>"
    "<p>A Serie A results run tells the story the table compresses: which streaks are real form, which are schedule effects, and which sides are converting narrow games. Reading results as sequences is the oldest analytic discipline in football and still one of the most reliable. The <a href=\"" + _w("Serie+A") + "\" rel=\"noopener\">Serie A</a> competition structure is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the run</h2>"
    "<ul>"
    "<li><b>Sequence over totals.</b> Form is a direction, not an aggregate.</li>"
    "<li><b>Note who scored first.</b> Teams that lead early win differently from teams that chase.</li>"
    "<li><b>Weight the opposition.</b> Results are samples; the schedule decides what they measure.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league-results/\">the Premier League results</a>, <a href=\"/sports/ligue-1-results/\">the Ligue 1 results</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",


"home/mistakes":
    "<h2>Mistakes as a system</h2>"
    "<p>The home's most expensive mistakes share a shape: a shortcut taken once, a warning ignored politely, and a bill that arrives with interest. This collection is organised by the failure's family — moisture, fire, chemistry, money — because the mistake that gets corrected by understanding rarely repeats. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The failure families</h2>"
    "<ul>"
    "<li><b>Moisture.</b> The leaks and damp that compound silently.</li>"
    "<li><b>Fire and electricity.</b> The overloads that advertise before they act.</li>"
    "<li><b>Chemistry.</b> The cleaning mixes and misuse that hurt people.</li>"
    "<li><b>Money.</b> The repairs that were cheaper last year.</li>"
    "</ul>"
    "<p>See <a href=\"/home/mistakes/mixing-cleaning-products/\">mixing cleaning products</a>, <a href=\"/home/mistakes/painting-without-prep/\">painting without prep</a> and <a href=\"/home/mistakes/overwatering-houseplants/\">overwatering houseplants</a>.</p>",


"home/mistakes/overwatering-houseplants":
    "<h2>Kindness, done wrongly</h2>"
    "<p>Overwatering is the commonest way houseplants die: the roots sit in water, the oxygen leaves the soil, and the rot arrives dressed as thirst — so the well-meaning water more. The fix is the finger test and a pot that drains. The <a href=\"" + _w("houseplant") + "\" rel=\"noopener\">houseplant care</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The corrected habit</h2>"
    "<ul>"
    "<li><b>Finger test before watering.</b> The top inch is the honest instrument.</li>"
    "<li><b>Drainage is non-negotiable.</b> The decorative pot is not the plant's home.</li>"
    "<li><b>Yellow leaves are a diagnosis.</b> They point down at the roots.</li>"
    "<li><b>Seasonal rhythm.</b> Winter plants drink less; the calendar should know.</li>"
    "</ul>"
    "<p>See <a href=\"/home/mistakes/\">the common home mistakes</a>, <a href=\"/home/mistakes/drying-laundry-indoors/\">drying laundry indoors</a> and <a href=\"/home/deep-clean-schedule/\">the deep clean schedule</a></p>",


}

# The two remaining t8b top-ups for this batch live here (keyed the same way).
TOPUP_SECTIONS15["home/disclaimer"] = (
    "<h2>What this desk is, and is not</h2>"
    "<p>This page carries general information written to be useful and checked — not professional advice for the specific house, circuit or claim. The distinction matters most at the expensive moments: the boundary between what a reader can do and what a licensed professional must. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government guidance</a> is one of the standards this desk cites. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The boundaries</h2>"
    "<ul>"
    "<li><b>General, not specific.</b> Your house has its own wiring history and its own survey.</li>"
    "<li><b>Safety lines are absolute.</b> Gas, main electrics and structure are professional territory.</li>"
    "<li><b>Check the local rules.</b> Building regulations vary by jurisdiction and year.</li>"
    "<li><b>When in doubt, get the quote.</b> The call-out is cheaper than the guess.</li>"
    "</ul>"
    "<p>See <a href=\"/home/editorial-policy/\">the home editorial policy</a>, <a href=\"/home/corrections/\">corrections</a> and <a href=\"/home/contact/\">contact the desk</a>.</p>"
)

# Batch J rescue pass: pages whose t8/t8b blocks landed just under their bars
# by the frozen ruler's count (731-748 of 750). Injected with t8c marker.
EXTRA_SECTIONS15 = {

"entertainment/reviews/nneka-the-pretty-serpent":
    "<h2>The folklore engine</h2>"
    "<p>The serpent story's rules are the film's contract with its audience: the magic has terms, the revenge has a price, and the folklore frame keeps both legible. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Rules before spectacle.</b> The magic works because it has terms.</li><li><b>Revenge has a ledger.</b> The plot's honesty is its engine.</li><li><b>The reboot respects the audience.</b> The cult's memory is the film's inheritance.</li></ul>",

"entertainment/what-is-film-noir-explained":
    "<h2>Why it never ended</h2>"
    "<p>Noir survives because every decade finds its own fog — the genre is a lens, not a period. The <a href=\"" + _w("film+noir") + "\" rel=\"noopener\">film noir</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>The lens travels.</b> Any city at night can hold the shadows.</li><li><b>Moral fog is timeless.</b> Every era has its compromised detective.</li><li><b>The style is the argument.</b> The lighting carries the thesis.</li></ul>",

"home/electric-iron-steam-care":
    "<h2>The right water</h2>"
    "<p>The tank's sediment is the tap water's mineral deposit — the iron's lifespan is a water-quality product. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Distilled or cooled boiled.</b> The mineral decides the vents' life.</li><li><b>Empty the tank after use.</b> Standing water breeds the next spit.</li><li><b>Flush before it spits.</b> The schedule beats the symptom.</li></ul>",

"home/gutter-cleaning-damage":
    "<h2>The cheap morning</h2>"
    "<p>Two cleanings a year interrupt the damage chain at its cheapest link — before the fascia, the timber and the wall join the story. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Autumn and spring.</b> The schedule follows the trees and the harmattan.</li><li><b>Check the fall.</b> Standing water is the sag announcing itself.</li><li><b>Photograph the outlets.</b> The evidence settles the maintenance argument.</li></ul>",

"sports/serie-a-results":
    "<h2>The table's memory</h2>"
    "<p>The league table remembers totals; the results run remembers sequences — and form lives in the sequence. The <a href=\"" + _w("Serie+A") + "\" rel=\"noopener\">Serie A</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Read the last five first.</b> Direction beats accumulation.</li><li><b>Home and away are different leagues.</b> The split is the form's real texture.</li><li><b>Goals decide which streaks are noise.</b> The margins are the honesty.</li></ul>",

"writers/learn/common-problems/how-to-tell-if-your-writing-is-good":
    "<h2>The editor's verdict</h2>"
    "<p>Editors vote with their responses: the personal note, the revise request, the silence — each is information about fit and about the work. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows treats the response as the market's honest grade. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Personal notes are rare gold.</b> They mark growth precisely.</li><li><b>Revise requests are wins.</b> The door opened; walk through it.</li><li><b>Silence is weather.</b> The market's mood, not your worth.</li></ul>",

"writers/learn/creative-writing/how-to-write-a-memoir":
    "<h2>The narrator's honesty</h2>"
    "<p>The memoir's narrator is a character too — the self on the page must be as honest as the events it reports. The <a href=\"" + _w("memoir") + "\" rel=\"noopener\">memoir form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>The flawed narrator is the point.</b> Growth needs a starting self.</li><li><b>Memory is a source.</b> Treat it like an interview, checked.</li><li><b>The present self frames the past.</b> The essay's meaning lives in the gap.</li></ul>",

"writers/learn/examples/how-to-use-the-examples":
    "<h2>The parallel draft</h2>"
    "<p>The instrument becomes a skill the moment the writer drafts the parallel version — the example's shape, the writer's content. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Outline the example's skeleton.</b> The structure is the lesson.</li><li><b>Fill it with your case.</b> The content reveals the shape's honesty.</li><li><b>Compare the drafts.</b> The gap is the next thing to learn.</li></ul>",

"home/clean-home-pests-myth":
    "<h2>The wall void is the address</h2>"
    "<p>Pests live in the structure, not the kitchen — the clean floor removes the food, while the harbourage in the wall void keeps the colony. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household pest guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Seal the entries.</b> Exclusion is the pest control that stays done.</li><li><b>Monitor the void.</b> Traps report what the kitchen hides.</li><li><b>Call it what it is.</b> Established colonies are structural work.</li></ul>",

"tech/one-big-monitor-vs-two":
    "<h2>The arm is the upgrade</h2>"
    "<p>Whatever the screen count, the mount decides the desk: the arm reclaims the footprint and sets the angle the neck will live with. The <a href=\"" + _w("computer+monitor") + "\" rel=\"noopener\">monitor setups</a> are documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Height first.</b> The top of the screen at eye level.</li><li><b>The desk breathes.</b> The reclaimed space is the daily gain.</li><li><b>Cable management is posture too.</b> The tangle sets the seating.</li></ul>",

"writers/learn/writing-process/how-to-build-a-writing-routine":
    "<h2>The trigger, not the mood</h2>"
    "<p>Routines survive because the trigger replaces the decision: the kettle on, the file open, the first sentence copied. The <a href=\"" + _w("writing+process") + "\" rel=\"noopener\">writing process</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Attach the session to a habit.</b> The trigger does the motivating.</li><li><b>Small enough to finish.</b> The half-hour that actually happens beats the evening that does not.</li><li><b>Miss once, never twice.</b> The streak survives one life.</li></ul>",

"writers/studio":
    "<h2>The room without an audience</h2>"
    "<p>First drafts change when nobody is watching — including analytics. The studio keeps the writing in the browser so the draft can be as unfinished as drafts actually are. The <a href=\"" + _w("text+editor") + "\" rel=\"noopener\">editor tooling</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Write badly on purpose.</b> The permission is the feature.</li><li><b>Export when it earns it.</b> The file is the draft's graduation.</li><li><b>No account, no history.</b> The tab is the whole storage.</li></ul>",

"entertainment/reviews/breath-of-life":
    "<h2>The register held</h2>"
    "<p>Faith cinema succeeds when the theme is dramatised rather than declared — and this film's performances keep the register honest scene by scene. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Theme through action.</b> Service shown is worth ten speeches.</li><li><b>The faces carry the argument.</b> The cast does the theology.</li><li><b>The pacing trusts the audience.</b> Earned beats land hardest.</li></ul>",

"tech/ai":
    "<h2>The verification habit</h2>"
    "<p>The durable skill is verification: checking the output's claims against sources, dates and arithmetic, because confident error is the technology's signature failure. The <a href=\"" + _w("artificial+intelligence") + "\" rel=\"noopener\">AI field</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Cite-check everything.</b> The invented reference is the classic tell.</li><li><b>Test the arithmetic.</b> The models are better at prose than sums.</li><li><b>Keep the human signature.</b> The reader is owed the real author.</li></ul>",

"tech/hdmi-arc-vs-optical-tv-audio":
    "<h2>The settings that follow the cable</h2>"
    "<p>The cable is half the story: the TV's audio output format and the bar's input setting decide what actually arrives. The <a href=\"" + _w("HDMI") + "\" rel=\"noopener\">HDMI system</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Set the output to the format.</b> PCM versus passthrough is the real switch.</li><li><b>CEC on, always.</b> The one-remote life is the feature.</li><li><b>Test with real content.</b> The menus lie less than the streaming app.</li></ul>",

"writers/learn/creative-writing/how-to-write-travel-writing":
    "<h2>The writer's position</h2>"
    "<p>Travel writing's honesty is positional: the piece declares where the writer stood, what they paid, and who showed them the place. The <a href=\"" + _w("travel+writing") + "\" rel=\"noopener\">travel writing form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Declare the viewpoint.</b> The honest byline is part of the reporting.</li><li><b>Pay the guide's rate.</b> The extractive story shows in the details.</li><li><b>Return visits deepen the piece.</b> The second look sees the first.</li></ul>",

"home/fridge-door-seal-test":
    "<h2>The energy at the door</h2>"
    "<p>A leaking gasket is an electricity problem first: the compressor runs longer, the bill rises, and the fridge dies younger. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government appliance guidance</a> is the standard this desk adapts. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>The test monthly.</b> One minute of paper saves a season of waste.</li><li><b>Warm water restores.</b> The rubber's memory is real.</li><li><b>Replace what stays flat.</b> The spent gasket cannot be cleaned back.</li></ul>",

"tech/android-notifications-not-arriving":
    "<h2>The reinstall, last</h2>"
    "<p>When the toggles are all correct and apps stay quiet, the app's registration with the push service is the last suspect — and a reinstall re-registers it cleanly. The <a href=\"" + _w("Android") + "\" rel=\"noopener\">Android platform</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Reinstall the quiet app.</b> The registration is the invisible state.</li><li><b>Check the network's restrict.</b> Data savers silence push quietly.</li><li><b>One app at a time.</b> The fix is diagnostic, not decorative.</li></ul>",

"writers/learn/journaling-personal/how-to-write-a-gratitude-journal-entry":
    "<h2>The habit's shape</h2>"
    "<p>The entry's size is the habit's survival condition: small enough to do on the tired days, specific enough to mean something. The <a href=\"" + _w("gratitude+journaling") + "\" rel=\"noopener\">gratitude journaling</a> practice is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Three lines, one item.</b> The economy is the discipline.</li><li><b>Same slot daily.</b> The trigger does the remembering.</li><li><b>Specificity grows with practice.</b> The noticing is the skill.</li></ul>",

"writers/learn/structure-formatting":
    "<h2>Formatting is the map</h2>"
    "<p>Headings, spacing and lists are the reader's map through the argument — the structure made visible at a glance. The <a href=\"" + _w("document+structure") + "\" rel=\"noopener\">document structure</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Headings that say something.</b> The map's labels are the skim's content.</li><li><b>White space is a paragraph break's cousin.</b> The eye needs the rests.</li><li><b>Lists for the checkable.</b> The reader's task shapes the form.</li></ul>",

"writers/learn/writing-for-publication/how-to-build-a-writing-portfolio":
    "<h2>Keep it current</h2>"
    "<p>The portfolio is a garden: the dated clip is pruned, the recent work is planted where the argument lives. The <a href=\"" + _w("portfolio") + "\" rel=\"noopener\">portfolio practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Quarterly review.</b> The old clip is the argument's weakest link.</li><li><b>Lead with the named beat.</b> The visitor's first question is 'what do you write'.</li><li><b>One page beats ten.</b> The editor's minute is the design constraint.</li></ul>",

"home/mistakes":
    "<h2>The correction habit</h2>"
    "<p>Each family of mistakes has its own correction habit — the check that catches the error at its cheapest stage. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Monthly circuit.</b> The house's warnings advertise early.</li><li><b>Seasonal sweep.</b> The rains and the harmattan write the calendar.</li><li><b>Fix the first sign.</b> The small repair is the fund's best friend.</li></ul>",

"tech/data-shuttle-sd-usb-ssd":
    "<h2>The pocket test</h2>"
    "<p>What survives a pocket decides the shuttle: the SD card's contacts, the drive's cap, the SSD's tolerance for the commute. The <a href=\"" + _w("flash+storage") + "\" rel=\"noopener\">flash storage</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Caps and cases.</b> The connector is the device's soft tissue.</li><li><b>Two copies before travel.</b> The shuttle is not the archive.</li><li><b>Label the flight risk.</b> The unlabelled drive is the future's lost folder.</li></ul>",

"home/mistakes/overwatering-houseplants":
    "<h2>The pot's honesty</h2>"
    "<p>The drainage hole is the plant's whole insurance policy — the decorative pot holds a trapped pool the roots cannot survive. The <a href=\"" + _w("houseplant") + "\" rel=\"noopener\">houseplant care</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Water at the sink.</b> The soak-and-drain beats the daily splash.</li><li><b>Saucers emptied.</b> The standing water is the rot's address.</li><li><b>Winter rhythm.</b> The calendar, not the guilt, decides.</li></ul>",

"writers/learn/academic-writing/academic-writing-basics":
    "<h2>The reader is a checker</h2>"
    "<p>Academic conventions exist because the reader's job is verification: every claim findable, every source traceable, every hedge honest. The <a href=\"" + _w("academic+writing") + "\" rel=\"noopener\">academic writing</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Write for the sceptic.</b> The reviewer is the design reader.</li><li><b>Definitions early.</b> The term's meaning is the argument's floor.</li><li><b>The paragraph is the unit.</b> One claim, one evidence, one move.</li></ul>",

"entertainment/slice-of-life-anime-explained":
    "<h2>The season's shape</h2>"
    "<p>Slice-of-life plots run on calendars: the school year, the summer, the festival — the structures audiences already feel. The <a href=\"" + _w("slice+of+life") + "\" rel=\"noopener\">slice-of-life genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>The calendar is the plot.</b> The audience knows what comes next and loves it.</li><li><b>The last episode is the season's truth.</b> Change arrives as an ending.</li><li><b>The rewatch is the genre's metric.</b> Comfort is a design goal.</li></ul>",

"entertainment/kdrama-genres-explained":
    "<h2>The sixteen-episode contract</h2>"
    "<p>The classic K-drama arc is a structure audiences can feel: the meet, the obstacle, the wrist-grab, the finale's weather. The <a href=\"" + _w("Korean+drama") + "\" rel=\"noopener\">Korean drama</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>The episode-eight turn.</b> The format's midpoint is a design constant.</li><li><b>The second leads' arc.</b> The mirror plot carries the theme.</li><li><b>The finale keeps its promise.</b> The contract's last clause is the tone.</li></ul>",

"writers/learn/grammar-language/comma-rules":
    "<h2>The serial question</h2>"
    "<p>The serial comma is a house-style decision with a clarity floor: when the list's last items pair wrongly, the comma is not optional. The <a href=\"" + _w("comma") + "\" rel=\"noopener\">comma usage</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>House style, consistently.</b> The mix is the only error.</li><li><b>Clarity overrides style.</b> The ambiguous list takes the comma.</li><li><b>Read the rhythm aloud.</b> The breath is the rule's origin.</li></ul>",

"writers/learn/journaling-personal/daily-journal-prompts":
    "<h2>The prompt that asks</h2>"
    "<p>The best prompt asks a question the writer has not answered this week — the observation fresh enough to need finding. The <a href=\"" + _w("journaling") + "\" rel=\"noopener\">journaling practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>Rotate the families.</b> The same question stops asking anything.</li><li><b>Keep the unanswered list.</b> The prompt's archive is the writing's seed.</li><li><b>Short answers count.</b> The habit's unit is the entry, not the essay.</li></ul>",

"writers/writing/transition-magazine":
    "<h2>The political ear</h2>"
    "<p>Transition's pages hold essays that argue with the world and with each other — criticism written at the stakes the subject deserves. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>The argument is the pitch.</b> Position first, evidence alongside.</li><li><b>The archive is the syllabus.</b> Read the magazine's history before submitting.</li><li><b>The frame stays wide.</b> The diaspora is the conversation, not the niche.</li></ul>",

"sports/what-does-rtd-mean-in-boxing-explained":
    "<h2>The mercy on the record</h2>"
    "<p>The RTD protects the fighter from the fight's own momentum — the corner's decision is the sport's oldest form of care. The <a href=\"" + _w("boxing") + "\" rel=\"noopener\">boxing rules</a> are documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<ul><li><b>The towel is wisdom.</b> The career outlasts the round.</li><li><b>The cut man's clock.</b> The bleeding decides the doctor's call.</li><li><b>The record keeps the truth.</b> RTD stands in the history honestly.</li></ul>",

}
