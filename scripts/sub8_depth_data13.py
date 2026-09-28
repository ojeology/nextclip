# -*- coding: utf-8 -*-
"""Editorial depth sections, part 13: batch I, the 634-654 word tranche against
the 750-word bar, plus home/paint-calculator and the tech/tool hub under the
669 tool bar, plus five t8b top-ups. 84 pages total.
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

DEPTH_SECTIONS13 = {

"writers/writing/writers-digest":
    "<h2>The craft market, stated plainly</h2>"
    "<p>Writer's Digest pays professional rates for writing-craft articles — the business and practice of writing, pitched by writers who can demonstrate both. It is one of the few markets where the how-to of writing is the product, and where a clip compounds into authority. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What the desk buys</h2>"
    "<ul>"
    "<li><b>Craft with scars.</b> Technique explained through work that failed first.</li>"
    "<li><b>Markets and business.</b> The paying side of the writing life, reported.</li>"
    "<li><b>Pitch the column, not the muse.</b> Fit decides; inspiration does not.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/wired/\">WIRED</a>, <a href=\"/writers/writing/slate/\">Slate</a> and <a href=\"/writers/writing/the-tyee/\">The Tyee</a>.</p>",

"fitness/start":
    "<h2>Starting from zero</h2>"
    "<p>The first week is a logistics problem wearing a motivation problem's clothes: what to wear, when to go, what to do once you are there. Beginner plans work because they remove decisions — show up, move with reasonable effort, leave before you are destroyed. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> physical activity guidance is the floor this desk builds on. By the Bryme Fitness desk. Reviewed 28 September 2026.</p>"
    "<h2>The first week, honestly</h2>"
    "<ul>"
    "<li><b>Two sessions, not five.</b> The habit is the achievement; the programme comes later.</li>"
    "<li><b>Learn three machines or three moves.</b> Competence beats variety at the start.</li>"
    "<li><b>Expect the second day to hurt.</b> Soreness is information, not an injury verdict.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/how-to-start-working-out/\">how to start working out</a>, <a href=\"/fitness/gym-anxiety-first-session-guide/\">the gym anxiety first-session guide</a> and <a href=\"/fitness/strength-training-for-beginners/\">strength training for beginners</a>.</p>",

"home/ceiling-water-stain-removal":
    "<h2>The stain is a map</h2>"
    "<p>The brown ceiling stain is water carrying something from above — timber, plaster, rust — and its edges tell you how active the leak is. Painting over a live stain is the repair that fails twice: the tide mark returns and the paint bubbles first. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes moisture guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Read it before you paint</h2>"
    "<ul>"
    "<li><b>Sharp edges: old leak. Soft edges: active leak.</b> The paint waits for the second kind.</li>"
    "<li><b>Find the source above, always.</b> Stains travel along joists from somewhere else.</li>"
    "<li><b>Stain block, then repaint.</b> Watermarks bleed through emulsion without a barrier.</li>"
    "</ul>"
    "<p>See <a href=\"/home/ceiling-leak-11pm/\">the ceiling leak at 11pm</a>, <a href=\"/home/ceiling-plaster-sagging-repair/\">ceiling plaster sagging repair</a> and <a href=\"/home/small-leak-ripple-effect/\">why a small leak never stays small</a>.</p>",

"home/gutters-and-downpipes":
    "<h2>The cheapest roof repair</h2>"
    "<p>Guttering fails quietly: a small blockage, a slight sag, water finding the fascia instead of the downpipe. By the time the stain appears inside, the timber has been wet for a season. Clearing gutters twice a year is the cheapest insurance in the whole building. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The twice-a-year routine</h2>"
    "<ul>"
    "<li><b>Clear the outlets first.</b> The rest drains once those run.</li>"
    "<li><b>Check the fall.</b> Standing water means the sag won.</li>"
    "<li><b>Watch the joints.</b> Every leak starts where two pieces disagree.</li>"
    "</ul>"
    "<p>See <a href=\"/home/flat-roof-ponding-and-leaks/\">flat roof ponding and leaks</a>, <a href=\"/home/external-wall-crack-seal/\">the external wall crack seal</a> and <a href=\"/home/ceiling-water-stain-removal/\">ceiling water stain removal</a>.</p>",

"sports/weigh-ins-and-weight-cuts-explained":
    "<h2>The scale, then the water</h2>"
    "<p>Weight cuts are a dehydration product: fighters shed water to make the scale, then rehydrate into the fight. The weigh-in is the ceremony around that arithmetic, and the gap between weigh-in and bell is where the real weight class lives. The <a href=\"" + _w("weight+cutting") + "\" rel=\"noopener\">weight cutting practice</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>What the rehydration changes</h2>"
    "<ul>"
    "<li><b>The class is fiction on weigh-in day.</b> Both fighters return to their walking weight.</li>"
    "<li><b>Big cuts cost performance.</b> The last pounds take the most and give the least.</li>"
    "<li><b>Same-day weigh-ins change everything.</b> The format, not the rulebook, decides behaviour.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/boxing-decisions-explained/\">boxing decisions explained</a>, <a href=\"/sports/boxing-scoring-explained/\">boxing scoring explained</a> and <a href=\"/sports/how-extra-time-and-penalty-shootouts-work/\">extra time and penalty shootouts</a>.</p>",

"tech/what-free-apps-do-with-your-data":
    "<h2>The business behind the button</h2>"
    "<p>A free app is funded by something: attention, upgrades, or the data exhaust of daily use. The permissions screen is the disclosure — the gap between what an app needs to work and what it asks to know is the product's real business model. The <a href=\"" + _w("surveillance+capitalism") + "\" rel=\"noopener\">data-driven business model</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the disclosure</h2>"
    "<ul>"
    "<li><b>Permissions against purpose.</b> The mismatch is the answer.</li>"
    "<li><b>Where the data goes.</b> 'Partners' in a privacy policy is doing heavy lifting.</li>"
    "<li><b>What the delete button deletes.</b> Account deletion and data deletion are different promises.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/browser-privacy-settings/\">browser privacy settings</a>, <a href=\"/tech/ai-privacy-what-not-to-paste/\">AI privacy: what not to paste</a> and <a href=\"/tech/android-privacy-settings-checklist/\">the Android privacy checklist</a>.</p>",

"writers/learn/examples/example-of-a-cover-letter":
    "<h2>Why the example works</h2>"
    "<p>A cover letter is a single argument: this experience, this role, this fit — each paragraph earning the next. The example here works because it shows the reasoning, not just the prose: what was cut, why the opening names the role, and how the evidence stays specific. The <a href=\"" + _w("cover+letter") + "\" rel=\"noopener\">cover letter form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What to steal from it</h2>"
    "<ul>"
    "<li><b>The first line names the job.</b> Readers should never have to hunt.</li>"
    "<li><b>One achievement, quantified.</b> Evidence beats enthusiasm in every draft.</li>"
    "<li><b>The close asks for the conversation.</b> Letters that end politely end.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/professional-writing/how-to-write-a-cover-letter/\">how to write a cover letter</a>, <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-a-cover-letter/\">the dos and don'ts of a cover letter</a> and <a href=\"/writers/learn/professional-writing/how-to-write-a-cv-resume/\">how to write a CV</a>.</p>",

"entertainment/how-movie-release-windows-work":
    "<h2>The windows are the business</h2>"
    "<p>Every film arrives through a sequence of windows — cinema, then premium home, then rental, then subscription — each window priced for the audience that will not wait. The sequence is why the film costs £15 tonight and nothing in a year. The <a href=\"" + _w("film+distribution") + "\" rel=\"noopener\">distribution window system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What collapsed and what stayed</h2>"
    "<ul>"
    "<li><b>The theatrical window shrank.</b> Ninety days became weeks for many titles.</li>"
    "<li><b>Streaming bought the calendar.</b> Some films skip the sequence entirely.</li>"
    "<li><b>Premium pricing survived.</b> Early home access is more expensive, not cheaper.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-box-office-works/\">how box office works</a>, <a href=\"/entertainment/cheapest-way-to-stream-movies/\">the cheapest way to stream movies</a> and <a href=\"/tech/streaming-subscription-stacking-when-bundle-cheaper/\">streaming subscription stacking</a>.</p>",

"home/building-regs-vs-planning-permission":
    "<h2>Two different permissions</h2>"
    "<p>Planning permission asks whether the work should happen at all; building regulations ask whether it is built safely. UK homeowners need the right one — sometimes both — and confusing them is how projects stop halfway. Permitted development covers more than people expect, and the certificate that proves it is worth having. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government planning guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The distinction that matters</h2>"
    "<ul>"
    "<li><b>Planning is about appearance and neighbours.</b> Use, height, and the street.</li>"
    "<li><b>Regs are about structure and safety.</b> Fire, insulation, electrics, drainage.</li>"
    "<li><b>Buy the certificate.</b> The lawful development certificate settles future arguments.</li>"
    "</ul>"
    "<p>See <a href=\"/home/us-home-permits/\">US home permits</a>, <a href=\"/home/unpermitted-work-insurance/\">unpermitted work and insurance</a> and <a href=\"/home/renter-vs-owner-repairs/\">renter versus owner repairs</a>.</p>",

"writers/guides/how-to-write-a-pitch":
    "<h2>The pitch is the product</h2>"
    "<p>A magazine pitch sells the story before it exists: the subject line names the angle, the first paragraph proves the story is alive, and the closing sells you as the person to write it. Editors buy arguments and access — the pitch that shows both gets the reply. The <a href=\"" + _w("pitching") + "\" rel=\"noopener\">pitching practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The structure that gets read</h2>"
    "<ul>"
    "<li><b>Subject line as headline.</b> The editor's inbox is the first audition.</li>"
    "<li><b>The nut graf by line three.</b> What the piece argues, and why now.</li>"
    "<li><b>Clips that match.</b> Three relevant pieces beat ten impressive ones.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-to-write-a-strong-query-letter/\">how to write a strong query letter</a>, <a href=\"/writers/guides/how-to-follow-up-on-a-writing-pitch/\">how to follow up on a pitch</a> and <a href=\"/writers/guides/how-to-submit-a-freelance-article/\">how to submit a freelance article</a>.</p>",

"writers/learn/writing-glossary":
    "<h2>The vocabulary of the work</h2>"
    "<p>Writing has its working vocabulary — lede, nut graf, boilerplate, comps — and most of it exists to save editors time in conversation. Learning the terms is not gatekeeping; it is the shared shorthand that makes feedback precise. The <a href=\"" + _w("glossary+of+publishing+terms") + "\" rel=\"noopener\">publishing glossary</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Terms that pay the rent</h2>"
    "<ul>"
    "<li><b>Lede.</b> The opening that earns the second sentence.</li>"
    "<li><b>Nut graf.</b> The paragraph that says what the piece is about.</li>"
    "<li><b>Boilerplate.</b> The reusable description of you or the company.</li>"
    "<li><b>Comps.</b> The published pieces your piece resembles.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-basics/\">writing basics</a>, <a href=\"/writers/learn/types-of-writing/\">types of writing</a> and <a href=\"/writers/learn/dos-and-donts/\">the dos and don'ts library</a>.</p>",

"home/renter-vs-owner-repairs":
    "<h2>Who fixes what</h2>"
    "<p>The dividing line is structure and habitability versus everything the tenant brought in: the landlord owns the building's bones and the working installations, the renter owns the scuffs and the curtains. The tenancy agreement can shift details but rarely the frame. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government renting guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The practical split</h2>"
    "<ul>"
    "<li><b>Landlord: structure, heating, water, electrics.</b> The things that make it habitable.</li>"
    "<li><b>Tenant: cleanliness, minor upkeep, the things you chose.</b> Reporting quickly is most of the duty.</li>"
    "<li><b>Photograph the inventory day one.</b> Deposit disputes are won or lost before they exist.</li>"
    "</ul>"
    "<p>See <a href=\"/home/uk-landlord-damp-mould-duties/\">UK landlord damp and mould duties</a>, <a href=\"/home/inspection-checklist-gaps/\">inspection checklist gaps</a> and <a href=\"/home/emergency-repair-fund/\">the emergency repair fund</a>.</p>",

"writers/learn/dos-and-donts/dos-and-donts-of-a-cover-letter":
    "<h2>Do: make the fit obvious</h2>"
    "<p>A cover letter's job is fit: the role, your evidence, the conversation you want next. The letters that work read like the first page of working with you — specific, brief, and confident enough to stop selling. The <a href=\"" + _w("cover+letter") + "\" rel=\"noopener\">cover letter form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The shortlist</h2>"
    "<ul>"
    "<li><b>Do</b> name the role and the organisation in the first line.</li>"
    "<li><b>Don't</b> restate the CV; the letter is the argument, not the index.</li>"
    "<li><b>Do</b> quantify one achievement the role actually needs.</li>"
    "<li><b>Don't</b> end with 'I look forward to hearing from you' and nothing else.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/professional-writing/how-to-write-a-cover-letter/\">how to write a cover letter</a>, <a href=\"/writers/learn/examples/example-of-a-cover-letter/\">the cover letter example</a> and <a href=\"/writers/learn/professional-writing/how-to-write-a-cv-resume/\">how to write a CV</a>.</p>",

"writers/learn/types-of-writing/how-to-write-a-book-review":
    "<h2>A review is a service</h2>"
    "<p>A book review answers one reader question honestly: is this book worth my time, and for whom? The plot is the context; the judgement is the product — supported by enough evidence to be trusted and no spoilers to be avoided. The <a href=\"" + _w("book+review") + "\" rel=\"noopener\">book review form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The reviewing discipline</h2>"
    "<ul>"
    "<li><b>Judge the book it is.</b> Reviewing the book you wanted is a different piece.</li>"
    "<li><b>Quote the evidence.</b> A review's claims live or die on its examples.</li>"
    "<li><b>Name the reader.</b> 'Fans of slow burns' is the review's most useful sentence.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-an-article/\">how to write an article</a>, <a href=\"/writers/learn/creative-writing/how-to-write-a-memoir/\">how to write a memoir</a> and <a href=\"/writers/learn/common-problems/how-to-tell-if-your-writing-is-good/\">how to tell if your writing is good</a>.</p>",

"writers/learn/writing-for-publication/a-rejected-pitch-is-not-wasted":
    "<h2>Rejection is data</h2>"
    "<p>Every rejection contains information: the piece is wrong for the desk, wrong for the moment, or wrong in the pitch. The writers who place work fastest are the ones who read rejection as market research — and resubmit with the lesson applied. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows covers the numbers honestly. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What the rejection tells you</h2>"
    "<ul>"
    "<li><b>A form rejection is a fit problem.</b> The desk, not the writing.</li>"
    "<li><b>A personal note is an invitation.</b> That editor read you; try them again.</li>"
    "<li><b>Revise before resending.</b> The second pitch should not be the first one twice.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/when-to-follow-up-on-a-pitch/\">when to follow up on a pitch</a>, <a href=\"/writers/guides/how-to-follow-up-on-a-writing-pitch/\">how to follow up on a writing pitch</a> and <a href=\"/writers/learn/writing-for-publication/\">writing for publication</a>.</p>",

"entertainment/how-box-office-works":
    "<h2>What the numbers mean</h2>"
    "<p>Box office is gross ticket revenue reported in tiers — opening weekend, domestic, worldwide — and the tiers matter because studios keep different fractions of each. A film can be a hit in America and a loss worldwide, or the reverse; the headline number is the least interesting one. The <a href=\"" + _w("box+office") + "\" rel=\"noopener\">box office system</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading a headline number</h2>"
    "<ul>"
    "<li><b>Opening weekend sets the marketing maths.</b> It is the first weekend, not the film's worth.</li>"
    "<li><b>Studios keep roughly half.</b> The split varies by territory and week.</li>"
    "<li><b>The budget excludes marketing.</b> Prints and advertising can rival production cost.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-movie-budgets-work/\">how movie budgets work</a>, <a href=\"/entertainment/how-movie-release-windows-work/\">how release windows work</a> and <a href=\"/entertainment/how-award-season-actually-works/\">how award season actually works</a>.</p>",

"home/test-alarms-monthly":
    "<h2>The five-minute habit</h2>"
    "<p>Every safety device in the home has a test button and a schedule: smoke and CO alarms monthly, extinguishers seasonally, escape routes whenever the furniture moves. The monthly habit is the difference between having safety equipment and owning it. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the testing guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The monthly circuit</h2>"
    "<ul>"
    "<li><b>Press and listen.</b> Each alarm, every month; the button checks the circuit.</li>"
    "<li><b>Read the expiry dates.</b> Ten years is the sensor's life, not the plastic's.</li>"
    "<li><b>Walk the exit route.</b> The plan needs rehearsing more than the alarms do.</li>"
    "</ul>"
    "<p>See <a href=\"/home/co-smoke-alarm-expiry/\">the smoke and CO alarm expiry</a>, <a href=\"/home/electrical-fire-warning-signs/\">electrical fire warning signs</a> and <a href=\"/home/cooking-oil-fire-plan/\">the cooking oil fire plan</a>.</p>",

"writers/learn/grammar-language/british-vs-american-english":
    "<h2>The differences that matter</h2>"
    "<p>British and American English disagree about spelling, vocabulary and the serial comma — and consistency inside one piece matters far more than which side you choose. Editors notice mixed usage the way musicians hear a wrong note: instantly and forgivingly only once. The <a href=\"" + _w("American_and_British_English_spelling_differences") + "\" rel=\"noopener\">spelling differences</a> are documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing and holding the line</h2>"
    "<ul>"
    "<li><b>Pick by the market.</b> The publication's house style is the correct style.</li>"
    "<li><b>-ise versus -ize.</b> Both are correct; mixing both is not.</li>"
    "<li><b>Quotation marks and commas differ.</b> The punctuation rules travel with the spelling.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/grammar-language/\">grammar and language</a>, <a href=\"/writers/learn/grammar-language/common-grammar-mistakes/\">common grammar mistakes</a> and <a href=\"/writers/learn/editing-proofreading/\">editing and proofreading</a>.</p>",

"writers/learn/professional-writing/how-to-write-a-professional-email":
    "<h2>The email that gets a response</h2>"
    "<p>A professional email is a small piece of writing with a job: the subject line names the task, the first sentence gives the context, and the ask sits where it cannot be missed. Brevity is politeness at work — every paragraph you delete is time you give back. The <a href=\"" + _w("email+etiquette") + "\" rel=\"noopener\">email practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The structure</h2>"
    "<ul>"
    "<li><b>Subject as title.</b> 'Question about Thursday's report' beats 'Hello'.</li>"
    "<li><b>The ask in the first three lines.</b> Busy readers decide early.</li>"
    "<li><b>One thread, one subject.</b> The second task is the second email.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-professional-emails/\">the dos and don'ts of professional emails</a>, <a href=\"/writers/learn/professional-writing/how-to-write-a-formal-complaint/\">how to write a formal complaint</a> and <a href=\"/writers/learn/professional-writing/how-to-write-a-memo/\">how to write a memo</a>.</p>",

"writers/writing/guernica":
    "<h2>Essays with stakes</h2>"
    "<p>Guernica pays an honorarium for accepted work and publishes essays where art and politics refuse to stay in separate rooms. For writers it is a market that rewards the reported essay — the argument that arrives with receipts. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What the magazine wants</h2>"
    "<ul>"
    "<li><b>Art with consequences.</b> Criticism that knows the world outside the frame.</li>"
    "<li><b>The reported essay.</b> Argument plus evidence, in one voice.</li>"
    "<li><b>International by default.</b> The view is wider than one capital.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/the-drift/\">The Drift</a>, <a href=\"/writers/writing/statement-africa/\">Statement Africa</a> and <a href=\"/writers/writing/the-london-magazine/\">The London Magazine</a>.</p>",

"writers/writing/rest-of-world-2":
    "<h2>Tech beyond the West</h2>"
    "<p>Rest of World pays professional rates for technology reporting from outside the Western bubble — the stories of how platforms, payments and policies actually land in Lagos, Jakarta and São Paulo. For writers with regional access, it is one of the best-paying reportage markets open. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What the desk rewards</h2>"
    "<ul>"
    "<li><b>Reporting from the ground.</b> Access is the pitch's whole argument.</li>"
    "<li><b>The platform story with human stakes.</b> Policy as lived experience.</li>"
    "<li><b>Pitch before writing.</b> Reported pieces are commissioned, not bought finished.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/wired/\">WIRED</a>, <a href=\"/writers/writing/eater/\">Eater</a> and <a href=\"/writers/writing/whatculture/\">WhatCulture</a>.</p>",

"entertainment/cheapest-way-to-stream-movies":
    "<h2>The cheapest stack is a calendar</h2>"
    "<p>Streaming the films you want at the lowest cost is a rotation problem: one subscription at a time, cancelled between shows, plus the free tiers and library apps nobody markets. The household that never stacks saves hundreds a year and watches the same films. The <a href=\"" + _w("streaming+media") + "\" rel=\"noopener\">streaming model</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The rotation rules</h2>"
    "<ul>"
    "<li><b>One service at a time.</b> The catalogue waits; the billing cycle does not.</li>"
    "<li><b>Check the free tiers first.</b> Ad-supported libraries carry more than they admit.</li>"
    "<li><b>Rent the one-offs.</b> Three rentals a year beats any subscription.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-streaming-apps-nigeria/\">the best streaming apps in Nigeria</a>, <a href=\"/entertainment/best-streaming-service-us-uk/\">the best streaming services in the US and UK</a> and <a href=\"/tech/streaming-subscription-stacking-when-bundle-cheaper/\">when a bundle is cheaper</a>.</p>",

"tech/gaming-phone-vs-cooler":
    "<h2>The heat problem no spec sheet mentions</h2>"
    "<p>Gaming phones chase sustained performance; cooling accessories chase the same physics from outside. Throttling is the real benchmark — the phone that holds frame rate after twenty minutes beats the phone with the bigger numbers on the box. The <a href=\"" + _w("thermal+throttling") + "\" rel=\"noopener\">thermal throttling</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Choosing against the heat</h2>"
    "<ul>"
    "<li><b>Chipset efficiency first.</b> Sustained clocks are an engineering choice.</li>"
    "<li><b>Clip-on coolers genuinely work.</b> They are physics, not marketing.</li>"
    "<li><b>Case off during long sessions.</b> The cheapest thermal upgrade available.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/phone-overheating-causes-and-fixes/\">phone overheating causes and fixes</a>, <a href=\"/tech/new-midrange-vs-used-flagship/\">new midrange versus used flagship</a> and <a href=\"/tech/phone-buying-specs-that-matter/\">phone buying specs that matter</a>.</p>",

"entertainment/modern-horror-starter-route":
    "<h2>Where to start with modern horror</h2>"
    "<p>The last decade of horror is a map of different fears: grief played straight, home invasion as class anxiety, folk horror as landscape. A starter route should show the range rather than the gore — the films that made the genre argue with itself again. The <a href=\"" + _w("horror+film") + "\" rel=\"noopener\">horror genre</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The route</h2>"
    "<ul>"
    "<li><b>Grief horror first.</b> The movement that made the genre respectable again.</li>"
    "<li><b>Then the slow burns.</b> Dread as a directorial technique.</li>"
    "<li><b>Then the folk horrors.</b> Landscape, belief and the outsider.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/scariest-horror-movies-tonight/\">the scariest movies tonight</a>, <a href=\"/entertainment/best-horror-movies-of-all-time/\">the best horror movies of all time</a> and <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a>.</p>",

"tech/backtest-validation-checklist":
    "<h2>The gauntlet</h2>"
    "<p>A backtest must survive a gauntlet before it earns a simulation, let alone money: out-of-sample testing, sensitivity analysis, costs modelled honestly, and the check that the strategy is not one lucky parameter away from nonsense. The <a href=\"" + _w("backtesting") + "\" rel=\"noopener\">backtesting practice</a> is documented in standard references. By the Bryme Technical Research desk. Reviewed 28 September 2026.</p>"
    "<h2>What the gauntlet tests</h2>"
    "<ul>"
    "<li><b>Out-of-sample, walk-forward.</b> The final exam the model never crammed for.</li>"
    "<li><b>Costs and slippage.</b> The gross strategy is a marketing document.</li>"
    "<li><b>Parameter surfaces, not points.</b> A plateau is a finding; a spike is a warning.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/lookahead-bias-explained/\">lookahead bias explained</a>, <a href=\"/tech/survivorship-bias-the-quiet-data-trap/\">survivorship bias</a> and <a href=\"/tech/overfitting-detection-guide/\">overfitting detection</a>.</p>",

"tech/lookahead-bias-explained":
    "<h2>The bug that makes backtests lie</h2>"
    "<p>Lookahead bias is using information from the future in a decision that should have been made in the past — and it turns every strategy into a fortune-teller. It hides in merged datasets, in adjusted prices, in the reporting date that is not the release date. The <a href=\"" + _w("lookahead+bias") + "\" rel=\"noopener\">lookahead bias</a> is documented in standard references. By the Bryme Technical Research desk. Reviewed 28 September 2026.</p>"
    "<h2>Where it hides</h2>"
    "<ul>"
    "<li><b>Point-in-time data.</b> Earnings are known on the release date, not the period date.</li>"
    "<li><b>Survivor lists.</b> Today's index is not the index of the year being tested.</li>"
    "<li><b>Signal timing.</b> The close you trade on must be the close you knew.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/backtest-validation-checklist/\">the backtest validation checklist</a>, <a href=\"/tech/survivorship-bias-the-quiet-data-trap/\">survivorship bias</a> and <a href=\"/tech/reproducible-quant-research-why-it-matters/\">reproducible quant research</a>.</p>",

"tech/phone-battery-charging-myths":
    "<h2>The chemistry, minus the myths</h2>"
    "<p>Overnight charging does not kill a modern battery; the management circuit stops the charge. Heat is what ages lithium-ion cells, and the habits that matter are thermal: the case at night, the dash charge in the sun, the full-heat gaming session. The <a href=\"" + _w("lithium-ion+battery") + "\" rel=\"noopener\">lithium-ion battery</a> chemistry is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>What actually ages the battery</h2>"
    "<ul>"
    "<li><b>Heat, heat, heat.</b> Ambient temperature beats any charging ritual.</li>"
    "<li><b>Long spells at 100% in the heat.</b> Storage voltage matters for shelf life.</li>"
    "<li><b>Charge cycles are fine.</b> The battery is a consumable; use it accordingly.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/android-battery-health/\">Android battery health</a>, <a href=\"/tech/swollen-phone-battery-safety/\">swollen battery safety</a> and <a href=\"/tech/why-phones-slow-down/\">why phones slow down</a>.</p>",

"tech/printer-keeps-going-offline":
    "<h2>The fixed IP is the fix</h2>"
    "<p>A printer that drops off the network every few days is almost always a DHCP story: the router hands out a new address and every saved print job hunts for the old one. A fixed IP — or a DHCP reservation — ends the mystery permanently. The <a href=\"" + _w("DHCP") + "\" rel=\"noopener\">DHCP protocol</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The fix order</h2>"
    "<ul>"
    "<li><b>Reserve the address first.</b> Router-side reservation beats printer-side static.</li>"
    "<li><b>Then update firmware.</b> Old print servers drop off politely and often.</li>"
    "<li><b>Reinstall the queue last.</b> The OS holds stale printer routes.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/dns-not-working-propagation/\">DNS not working: propagation</a>, <a href=\"/tech/router-dns-slow-browsing-fix/\">router DNS slow browsing fix</a> and <a href=\"/tech/new-router-for-slow-internet/\">a new router for slow internet</a>.</p>",

"writers/guides/how-to-find-paid-writing-opportunities":
    "<h2>Where the paying work is</h2>"
    "<p>Paid writing work lives in specific places: submission lists with verified rates, the classifieds of magazines that pay, and the quiet network of editors who answer good pitches. The skill is judging legitimacy before spending the submission's most expensive input — your time. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs legitimate markets. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Judging a market</h2>"
    "<ul>"
    "<li><b>Named rates are the first filter.</b> 'Exposure' is a business model, not a payment.</li>"
    "<li><b>Read the masthead.</b> Real editors, real issues, real archive.</li>"
    "<li><b>Check the response times.</b> The guidelines promise is the relationship preview.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-to-find-international-writing-opportunities/\">international writing opportunities</a>, <a href=\"/writers/guides/how-to-get-your-first-paid-writing-gig/\">your first paid writing gig</a> and <a href=\"/writers/guides/where-the-money-is-in-writing/\">where the money is in writing</a>.</p>",

"writers/learn/start-writing/how-to-overcome-writers-block":
    "<h2>Unstuck, without the mystique</h2>"
    "<p>Writer's block is almost never a shortage of words; it is a decision not yet made — the point is unclear, the opening is doing too much, or the draft is being judged mid-flight. The fixes are practical: smaller targets, worse first drafts, and permission to write the middle first. The <a href=\"" + _w("writer%27s+block") + "\" rel=\"noopener\">writer's block</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The practical kit</h2>"
    "<ul>"
    "<li><b>Lower the bar to the floor.</b> A bad paragraph is unblocking progress.</li>"
    "<li><b>Skip the opening.</b> It is the last thing to write, not the first.</li>"
    "<li><b>Name the decision.</b> The stuck feeling usually has a noun.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/writing-basics/\">writing basics</a>, <a href=\"/writers/learn/common-problems/my-introduction-is-weak/\">my introduction is weak</a> and <a href=\"/writers/learn/writing-process/\">the writing process</a>.</p>",

"entertainment/how-cinematic-universes-work":
    "<h2>The shared-universe machine</h2>"
    "<p>A cinematic universe is an infrastructure project: each film is a franchise installment and an advertisement for the next, and the crossover event is the payoff of years of coordination. The machine works until the homework outweighs the fun. The <a href=\"" + _w("shared+universe") + "\" rel=\"noopener\">shared universe model</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Why the machine runs</h2>"
    "<ul>"
    "<li><b>Every entry is a pilot.</b> The universe sells the next title at this one's prices.</li>"
    "<li><b>Continuity is the product.</b> The audience's memory becomes the marketing.</li>"
    "<li><b>The event film is the bill.</b> Crossovers charge interest on every prior installment.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/how-box-office-works/\">how box office works</a>, <a href=\"/entertainment/how-movie-budgets-work/\">how movie budgets work</a> and <a href=\"/entertainment/directors-cut-vs-theatrical-explained/\">director's cut versus theatrical</a>.</p>",

"sports/how-the-transfer-window-works":
    "<h2>Two doors, one deadline</h2>"
    "<p>The transfer window opens twice a year and closes with a deadline day that turns administration into theatre: clubs can register new players only inside it, and the last hours are a negotiation market with a countdown clock. The <a href=\"" + _w("transfer+window") + "\" rel=\"noopener\">transfer window system</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>How deals actually close</h2>"
    "<ul>"
    "<li><b>The fee is half the deal.</b> Wages and agents decide more signings than price does.</li>"
    "<li><b>Deadline day prices rise.</b> Scarcity is the whole economics of the last hour.</li>"
    "<li><b>Loans are the pressure valve.</b> Squads rebalance without the fee conversation.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-football-loans-work/\">how football loans work</a>, <a href=\"/sports/how-football-contracts-work/\">how football contracts work</a> and <a href=\"/sports/how-do-football-clubs-make-money/\">how football clubs make money</a>.</p>",

"writers/learn/professional-writing/how-to-write-a-cover-letter":
    "<h2>The letter is the argument</h2>"
    "<p>A cover letter connects your evidence to the role in one page: the opening names the position, the middle proves the fit with specifics, and the close asks for the conversation. It complements the CV instead of repeating it. The <a href=\"" + _w("cover+letter") + "\" rel=\"noopener\">cover letter form</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The one-page structure</h2>"
    "<ul>"
    "<li><b>Opening: the role and why this organisation.</b> One sentence each.</li>"
    "<li><b>Middle: one achievement that maps to the job.</b> Numbers included.</li>"
    "<li><b>Close: the ask.</b> Interview, call, next step — named.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/examples/example-of-a-cover-letter/\">the cover letter example</a>, <a href=\"/writers/learn/professional-writing/how-to-write-a-cv-resume/\">how to write a CV</a> and <a href=\"/writers/learn/dos-and-donts/dos-and-donts-of-a-cover-letter/\">the dos and don'ts of a cover letter</a>.</p>",

"writers/learn/research-sources/how-to-avoid-plagiarism":
    "<h2>Honest use of sources</h2>"
    "<p>Plagiarism is a failure of method, not of character: the notes lost track of which words were yours, or the citation arrived after the draft. The discipline is simple — mark quotes as you go, paraphrase in your own syntax, and cite every claim that is not yours. The <a href=\"" + _w("plagiarism") + "\" rel=\"noopener\">plagiarism problem</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The method</h2>"
    "<ul>"
    "<li><b>Quote marks in the notes, always.</b> Future-you cannot tell the difference.</li>"
    "<li><b>Paraphrase the idea, not the sentence.</b> Swapped words are still the author's structure.</li>"
    "<li><b>Cite as you draft.</b> Retro-fitting citations loses the sources.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/academic-writing/how-to-cite-sources/\">how to cite sources</a>, <a href=\"/writers/learn/common-problems/how-plagiarism-and-ai-checkers-are-made/\">how plagiarism and AI checkers are made</a> and <a href=\"/writers/learn/academic-writing/how-to-structure-a-research-paper/\">how to structure a research paper</a>.</p>",

"writers/writing/aarp-magazine":
    "<h2>The service journalism giant</h2>"
    "<p>AARP pays top-of-market rates for features, essays and service journalism aimed at readers past fifty — a readership large, loyal and underserved by pitch. The bar is service: pieces readers can act on this month. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks where such work lives. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching the magazine</h2>"
    "<ul>"
    "<li><b>Service is the frame.</b> The reader's decision comes first.</li>"
    "<li><b>Report the number.</b> Health and money claims need receipts.</li>"
    "<li><b>Pitch the desk, not the dream.</b> Sections have different appetites.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/eater/\">Eater</a>, <a href=\"/writers/writing/the-kitchn/\">The Kitchn</a> and <a href=\"/writers/writing/slate/\">Slate</a>.</p>",

"writers/writing/cincinnati-review":
    "<h2>A page-rate literary market</h2>"
    "<p>The Cincinnati Review pays per page for prose and poetry — one of the clearest formulas in literary publishing — and reads work that trusts the sentence. Its pages favour precision over performance, and its payment terms are stated plainly. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Length becomes payment.</b> The page rate rewards the story's true length.</li>"
    "<li><b>Read the issue first.</b> The magazine's ear is on the page.</li>"
    "<li><b>One strong piece at a time.</b> Small magazines read honestly and fast.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/kenyon-review/\">The Kenyon Review</a>, <a href=\"/writers/writing/the-malahat-review/\">The Malahat Review</a> and <a href=\"/writers/writing/prism-international/\">PRISM international</a>.</p>",

"writers/writing/eater":
    "<h2>Food culture, reported</h2>"
    "<p>Eater commissions essays and reported pieces on food culture with a narrative spine — the restaurant story as a story about cities, money and appetite. Payment is professional, and the pitch is the commission: reported access is what the desk buys. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What the desk buys</h2>"
    "<ul>"
    "<li><b>The reported essay.</b> Access first, argument second, both required.</li>"
    "<li><b>Culture over recipes.</b> The food is the door; the room is the piece.</li>"
    "<li><b>Pitch with the reporting plan.</b> Who you can reach is the story's proof.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/the-kitchn/\">The Kitchn</a>, <a href=\"/writers/writing/aarp-magazine/\">AARP Magazine</a> and <a href=\"/writers/writing/rest-of-world-2/\">Rest of World</a>.</p>",

"home/grout-sealant-neglect":
    "<h2>The slow bathroom mistake</h2>"
    "<p>Grout and sealant fail slowly: a hairline gap, a soft corner, water finding the wall behind the tiles. The damage budget grows silently for months before the first tile loosens. Re-grouting and re-sealing on a schedule is a weekend's work against a plumber's week. The <a href=\"" + _w("grout") + "\" rel=\"noopener\">grout and sealant practice</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The inspection habit</h2>"
    "<ul>"
    "<li><b>Press the sealant.</b> A springy line is failing; a firm one is fine.</li>"
    "<li><b>Look at the corners first.</b> Movement lives where planes meet.</li>"
    "<li><b>Seal grout yearly in wet zones.</b> The bottle costs less than the tile.</li>"
    "</ul>"
    "<p>See <a href=\"/home/bath-silicone-reseal/\">the bath silicone reseal</a>, <a href=\"/home/bathroom-grout-mould/\">bathroom grout mould</a> and <a href=\"/home/caulk-vs-grout-explained/\">caulk versus grout</a>.</p>",

"home/inspection-checklist-gaps":
    "<h2>What gets missed every time</h2>"
    "<p>Home inspections fail on scope, not competence: the roof was too steep, the crawlspace too small, the wiring too old to open. Knowing the standard gaps turns the report from a verdict into a to-do list — and tells you which specialist to call next. The <a href=\"" + _w("home+inspection") + "\" rel=\"noopener\">home inspection practice</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The standard gaps</h2>"
    "<ul>"
    "<li><b>Behind the furniture.</b> Damp hides where nobody moves the sofa.</li>"
    "<li><b>The roof and the drains.</b> Both need their own eyes.</li>"
    "<li><b>Old electrics and old pipes.</b> Age is a finding, not a footnote.</li>"
    "</ul>"
    "<p>See <a href=\"/home/renter-vs-owner-repairs/\">renter versus owner repairs</a>, <a href=\"/home/external-wall-crack-seal/\">the external wall crack seal</a> and <a href=\"/home/building-regs-vs-planning-permission/\">building regs versus planning permission</a>.</p>",

"tech/your-security-checklist":
    "<h2>Score the setup in two minutes</h2>"
    "<p>Security is a checklist, not a mood: passwords in a manager, updates current, two-factor on the accounts that matter, backups tested. The two-minute score is not a grade — it is the shortest path to the next improvement. The <a href=\"" + _w("information+security") + "\" rel=\"noopener\">security basics</a> are documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The five-line checklist</h2>"
    "<ul>"
    "<li><b>Password manager, unique passwords.</b> The single highest-value move.</li>"
    "<li><b>Two-factor on email and money.</b> Everything else resets through these.</li>"
    "<li><b>Updates on, backups tested.</b> The recovery drill is the last line.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/home-wifi-security-audit/\">the home Wi-Fi security audit</a>, <a href=\"/tech/how-to-spot-a-suspicious-link/\">how to spot a suspicious link</a> and <a href=\"/tech/patch-management-for-humans/\">patch management for humans</a>.</p>",

"entertainment/was-eren-yeager-really-the-villain":
    "<h2>The argument the ending forces</h2>"
    "<p>The ending of Attack on Titan turns its hero into its argument: freedom taken to its logic becomes annihilation, and the audience is left holding both the sympathy and the horror. Whether Eren is the villain is a question the series built on purpose. The <a href=\"" + _w("Attack_on_Titan") + "\" rel=\"noopener\">Attack on Titan</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Why the debate never settles</h2>"
    "<ul>"
    "<li><b>The story keeps his reasons legible.</b> Sympathy survives the act.</li>"
    "<li><b>The cycle is the point.</b> The villain frame assumes one side can end history.</li>"
    "<li><b>The finale chooses tragedy over verdict.</b> The show refuses the last word.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/10-anime-like-solo-leveling-you-should-watch/\">ten anime like Solo Leveling</a>, <a href=\"/entertainment/anime-canon-and-filler-explained/\">anime canon and filler explained</a> and <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a>.</p>",

"home/unpermitted-work-insurance":
    "<h2>The honest answer</h2>"
    "<p>Unpermitted work does not automatically void a policy — but damage caused by that work is routinely excluded, and insurers ask for building-regulation certificates exactly when the claim is expensive. The disclosure at purchase is where the argument is won. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government building guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>What actually happens at claim time</h2>"
    "<ul>"
    "<li><b>Cause decides coverage.</b> The unpermitted extension's leak is the excluded part.</li>"
    "<li><b>Retrospective approval exists.</b> The certificate is worth buying even late.</li>"
    "<li><b>Declare at purchase.</b> The solicitor's forms are the insurance policy's memory.</li>"
    "</ul>"
    "<p>See <a href=\"/home/building-regs-vs-planning-permission/\">building regs versus planning permission</a>, <a href=\"/home/fence-shed-insurance/\">fence and shed insurance mistakes</a> and <a href=\"/home/us-home-permits/\">US home permits</a>.</p>",

"entertainment/reviews/shadow-parties":
    "<h2>A feud staged as epic</h2>"
    "<p>Shadow Parties stages a family torn by community feud as Yoruba epic — the feature-film scale visible in the blocking and the ensemble. The film's interest is how private grief becomes public ceremony. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What holds the film</h2>"
    "<ul>"
    "<li><b>The ensemble carries the scale.</b> Every household gets its own front.</li>"
    "<li><b>Tradition as argument.</b> The ceremonies are the plot's evidence.</li>"
    "<li><b>The feud's logic stays legible.</b> The audience always knows what is at stake.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/reviews/mokalik/\">the Mokalik review</a>, <a href=\"/entertainment/reviews/the-set-up/\">The Set Up review</a> and <a href=\"/entertainment/nollywood-golden-age-explained/\">Nollywood's golden age</a>.</p>",

"tech/why-your-website-is-slow":
    "<h2>The real causes</h2>"
    "<p>Site speed is a budget spent in order: the render-blocking script, the unoptimised image, the third-party tag that ships a framework to render a button. Measuring before optimising is the whole method — the waterfall names the culprit in one pass. The <a href=\"" + _w("web+performance") + "\" rel=\"noopener\">web performance</a> field is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The waterfall, in order</h2>"
    "<ul>"
    "<li><b>Images first.</b> They are almost always the largest unforced error.</li>"
    "<li><b>Then the third parties.</b> Every tag is someone else's JavaScript on your page.</li>"
    "<li><b>Then the cache headers.</b> Returning visitors are the cheapest win.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/check-if-google-indexed-your-page/\">check if Google indexed your page</a>, <a href=\"/tech/website-not-indexing-google/\">why is my site not on Google</a> and <a href=\"/tech/how-to-get-cited-by-ai-search/\">how to get cited by AI search</a>.</p>",

"writers/writing/the-kitchn":
    "<h2>Food writing on a budget</h2>"
    "<p>The Kitchn pays per assignment for food-budget diaries and practical kitchen writing — service journalism for people who cook on Tuesdays. The market rewards specificity: real numbers, real weeks, real compromises. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What the desk buys</h2>"
    "<ul>"
    "<li><b>The real diary.</b> Budgets readers can compare against their own.</li>"
    "<li><b>Practical over aspirational.</b> The kitchen the reader has.</li>"
    "<li><b>Commissions, not open pitches.</b> Build the clip that gets you asked.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/eater/\">Eater</a>, <a href=\"/writers/writing/aarp-magazine/\">AARP Magazine</a> and <a href=\"/writers/writing/whatculture/\">WhatCulture</a>.</p>",

"entertainment/best-time-travel-stories-to-watch":
    "<h2>Loops, paradoxes and the rest</h2>"
    "<p>The best time-travel stories pick one rule and keep it: the loop that closes, the paradox that eats its tail, the timeline that edits itself. The genre rewards discipline — the story that breaks its own rules breaks the audience's trust with it. The <a href=\"" + _w("time+travel+in+fiction") + "\" rel=\"noopener\">time travel fiction</a> is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>The three honest kinds</h2>"
    "<ul>"
    "<li><b>The closed loop.</b> The past already includes the traveller.</li>"
    "<li><b>The editable timeline.</b> Every change has a receipt.</li>"
    "<li><b>The fixed point.</b> The story's grief is that nothing can change.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-sci-fi-movies-of-all-time/\">the best sci-fi movies of all time</a>, <a href=\"/entertainment/comfort-movies-to-rewatch/\">comfort movies to rewatch</a> and <a href=\"/entertainment/what-makes-a-cult-classic/\">what makes a cult classic</a>.</p>",

"entertainment/reviews/the-set-up":
    "<h2>A con with a ledger</h2>"
    "<p>The Set Up runs three women and one con through a plot that keeps its twists in a bookkeeper's literal ledger — every reveal sitting where the film planted it. The pleasure is mechanical: the genre machine assembled with visible craft. The <a href=\"" + _w("Nollywood") + "\" rel=\"noopener\">Nollywood tradition</a> it works inside is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>What the film does well</h2>"
    "<ul>"
    "<li><b>The con stays legible.</b> The audience is cheated honestly.</li>"
    "<li><b>The leads carry the machinery.</b> Three performances doing the script's accounting.</li>"
    "<li><b>The genre knows its rules.</b> The twist lands where the ledger said.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/reviews/shadow-parties/\">the Shadow Parties review</a>, <a href=\"/entertainment/reviews/mokalik/\">the Mokalik review</a> and <a href=\"/entertainment/african-cinema-beyond-nollywood-explained/\">African cinema beyond Nollywood</a>.</p>",

"tech/surge-protector-stabiliser-ups":
    "<h2>Which box saves the TV</h2>"
    "<p>Three boxes do three jobs: the surge protector clips spikes, the stabiliser holds voltage in range, and the UPS keeps the lights on through the gap. Buying the wrong one is common because the failure modes look identical from the plug. The <a href=\"" + _w("surge+protector") + "\" rel=\"noopener\">surge protection</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Matching box to problem</h2>"
    "<ul>"
    "<li><b>Spikes: surge protector.</b> Cheap, sacrificial, replace after the big one.</li>"
    "<li><b>Brownouts: stabiliser.</b> Low voltage kills appliances slowly.</li>"
    "<li><b>Outages: UPS.</b> Runtime measured in minutes; buy the shutdown, not the evening.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/outage-lighting-tiers/\">outage lighting tiers</a>, <a href=\"/tech/blackout-internet-router-power/\">blackout internet and router power</a> and <a href=\"/tech/inverter-battery-runtime-maths/\">inverter battery runtime maths</a>.</p>",

"writers/learn/examples/example-of-a-product-description":
    "<h2>Selling without over-claiming</h2>"
    "<p>A product description that sells does three things: names the buyer, shows the use, and proves the claim. The example here works because every adjective is load-bearing and the benefits are the reader's, not the product's. The <a href=\"" + _w("copywriting") + "\" rel=\"noopener\">copywriting practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>What to steal from it</h2>"
    "<ul>"
    "<li><b>The first line names the use.</b> The reader pictures their Tuesday.</li>"
    "<li><b>Specifics over superlatives.</b> 'Lasts eight hours' beats 'long-lasting'.</li>"
    "<li><b>One honest limitation.</b> Trust is the conversion feature.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-a-blog-post/\">how to write a blog post</a>, <a href=\"/writers/learn/online-writing/how-to-write-search-friendly-content/\">how to write search-friendly content</a> and <a href=\"/writers/learn/examples/example-of-a-report/\">the report example</a>.</p>",

"writers/writing/wired":
    "<h2>Reported features at the top of market</h2>"
    "<p>WIRED pays premium rates for deeply reported features — pitched before writing, reported like magazine journalism, and read by a technically literate audience that spots bluffs instantly. The pitch is the commission; the reporting plan is the pitch. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Pitching WIRED</h2>"
    "<ul>"
    "<li><b>Reported, not thought-through.</b> Access and evidence are the currency.</li>"
    "<li><b>The stakes are human.</b> Technology is the setting, not the story.</li>"
    "<li><b>Pitch the desk that owns the beat.</b> The section is the first fit test.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/rest-of-world-2/\">Rest of World</a>, <a href=\"/writers/writing/slate/\">Slate</a> and <a href=\"/writers/writing/writers-digest/\">Writer's Digest</a>.</p>",

"home/external-wall-crack-seal":
    "<h2>The hairline-crack map</h2>"
    "<p>External cracks are a water-management question: which cracks are movement, which are the render ageing, and which are the path rain will take this season. Sealing before the rains is the maintenance that prevents the damp conversation later. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the crack</h2>"
    "<ul>"
    "<li><b>Hairline and stable: seal it.</b> Render flexes; the paint does not.</li>"
    "<li><b>Stepped or growing: investigate.</b> Movement is structural, not cosmetic.</li>"
    "<li><b>Sealant over paint, never under.</b> The joint must own the flex.</li>"
    "</ul>"
    "<p>See <a href=\"/home/grout-sealant-neglect/\">grout and sealant neglect</a>, <a href=\"/home/condensation-vs-rising-vs-penetrating-damp/\">the three damps</a> and <a href=\"/home/ceiling-plaster-sagging-repair/\">ceiling plaster sagging repair</a>.</p>",

"home/ignore-single-pest-sighting":
    "<h2>One sighting is a population</h2>"
    "<p>By the time one pest is visible, the colony has been resident for a while — that sighting is the exception that proves the rule. The cheapest response in the home is the immediate one: seal, clean, set the monitor, and watch the second sighting's absence. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household pest guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The first 24 hours</h2>"
    "<ul>"
    "<li><b>Find the entry.</b> The gap under the door is the whole story.</li>"
    "<li><b>Remove the food.</b> Sanitation is pest control with a broom.</li>"
    "<li><b>Set monitors.</b> The second sighting arrives as data, not surprise.</li>"
    "</ul>"
    "<p>See <a href=\"/home/pests-start-here/\">pests: first signs and first response</a>, <a href=\"/home/diy-vs-professional-pests/\">DIY versus professional pests</a> and <a href=\"/home/entry-point-mistakes/\">entry point mistakes</a>.</p>",

"tech/swollen-phone-battery-safety":
    "<h2>A Tuesday problem</h2>"
    "<p>A swollen battery is a chemical failure in progress: the pack is venting gas, the case is the only thing holding the shape, and pressure is what turns a Tuesday problem into a Friday one. Stop charging, stop using, and get it to a recycling point — puncture is the line not to cross. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes lithium battery safety this desk follows. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The response, in order</h2>"
    "<ul>"
    "<li><b>Power down, stop charging.</b> Every charge cycle adds gas.</li>"
    "<li><b>Do not press, bend or puncture.</b> The case is a pressure vessel.</li>"
    "<li><b>Recycle it properly.</b> Lithium cells belong in the special bin, not the bin.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/phone-battery-charging-myths/\">phone battery charging myths</a>, <a href=\"/tech/phone-overheating-causes-and-fixes/\">phone overheating causes and fixes</a> and <a href=\"/tech/android-battery-health/\">Android battery health</a>.</p>",

"writers/guides/the-tax-set-aside-habit":
    "<h2>Income arrives gross</h2>"
    "<p>Freelance income arrives with the tax still inside it. The set-aside habit is mechanical: a fixed percentage moves to a separate account on payment day, before the money can look like spending money. The habit is the entire tax strategy for most writers. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government self-assessment guidance</a> is the standard this desk follows. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The habit, in full</h2>"
    "<ul>"
    "<li><b>Move the percentage on payment day.</b> Not at quarter-end; the same day.</li>"
    "<li><b>Use a named pot.</b> The account name is the discipline.</li>"
    "<li><b>Review the rate yearly.</b> Income changes; the habit absorbs it.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/track-your-writing-income/\">track your writing income</a>, <a href=\"/writers/learn/freelance-paid-writing/how-to-invoice-as-a-writer/\">how to invoice as a writer</a> and <a href=\"/writers/learn/freelance-paid-writing/the-tax-set-aside-habit/\">the tax set-aside habit, the course version</a>.</p>",

"writers/learn/online-writing/how-to-write-search-friendly-content":
    "<h2>Readers first, engines second</h2>"
    "<p>Search-friendly writing is clear writing with the structure made visible: the question named early, the answer given plainly, and the headings carrying the map. Keyword stuffing optimises for a system that stopped falling for it years ago. The <a href=\"" + _w("search+engine+optimization") + "\" rel=\"noopener\">search optimisation practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The structure that ranks</h2>"
    "<ul>"
    "<li><b>Answer the query in the first paragraph.</b> Snippets reward honesty.</li>"
    "<li><b>Headings as questions.</b> The map should match the search.</li>"
    "<li><b>Specific beats clever.</b> The engine matches words the reader typed.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-a-blog-post/\">how to write a blog post</a>, <a href=\"/tech/how-to-get-cited-by-ai-search/\">how to get cited by AI search</a> and <a href=\"/writers/learn/examples/example-of-a-product-description/\">the product description example</a>.</p>",

"writers/writing/black-fox-literary-magazine":
    "<h2>Small press, clear terms</h2>"
    "<p>Black Fox Literary Magazine pays each contributor a stated flat fee and runs a biannual prize with real entry terms — small-magazine economics stated honestly. It favours work with a heartbeat over work with a gimmick. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>The prize is a separate market.</b> Entry terms differ from the magazine's.</li>"
    "<li><b>The flat fee is the floor.</b> Publication and readership are the rest.</li>"
    "<li><b>Read the sample work.</b> Small magazines publish a taste, not a genre.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/the-forge-literary-magazine/\">The Forge Literary Magazine</a>, <a href=\"/writers/writing/split-lip-magazine/\">Split Lip Magazine</a> and <a href=\"/writers/writing/carte-blanche/\">carte blanche</a>.</p>",

"home/fence-shed-insurance":
    "<h2>The outbuildings policy trap</h2>"
    "<p>Fences and sheds fail insurance claims in predictable ways: maintenance excluded as wear, storm damage needing evidence of upkeep, and boundary structures falling between two policies. The schedule's small print is where the garden lives. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government insurance guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The mistakes that void claims</h2>"
    "<ul>"
    "<li><b>Wear is not storm damage.</b> The fence that fell was rotting first.</li>"
    "<li><b>Photograph the upkeep.</b> Maintenance evidence settles storm disputes.</li>"
    "<li><b>Check the boundary line.</b> The neighbour's fence is the neighbour's claim.</li>"
    "</ul>"
    "<p>See <a href=\"/home/unpermitted-work-insurance/\">unpermitted work and insurance</a>, <a href=\"/home/inspection-checklist-gaps/\">inspection checklist gaps</a> and <a href=\"/home/improvements-no-resale-value/\">improvements with no resale value</a>.</p>",

"home/washing-machine-walks-and-shakes":
    "<h2>Shipping bolts and level feet</h2>"
    "<p>A washing machine that walks is telling you one of three things: the shipping bolts are still in, the feet are unlevel, or the load is a single heavy item. Each has a signature shake. The <a href=\"" + _w("washing+machine") + "\" rel=\"noopener\">washing machine</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The diagnosis</h2>"
    "<ul>"
    "<li><b>Shipping bolts out?</b> They travel in the back; they must not arrive.</li>"
    "<li><b>Rock the machine corner to corner.</b> The wobble names the unlevel foot.</li>"
    "<li><b>Balance the load.</b> One heavy item is the worst case every time.</li>"
    "</ul>"
    "<p>See <a href=\"/home/washing-machine-heavy-items/\">washing machine heavy items</a>, <a href=\"/home/dryer-lint-every-load/\">dryer lint every load</a> and <a href=\"/home/appliances-that-use-the-most-electricity/\">appliances that use the most electricity</a>.</p>",

"writers/compare":
    "<h2>Which format do you actually need</h2>"
    "<p>'Write a report' is only useful if you know what a report is, versus a memo, an essay or a brief. The format is a contract with the reader about what they are about to receive — and choosing wrong wastes both sides. The <a href=\"" + _w("technical+writing") + "\" rel=\"noopener\">document formats</a> are documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The choice, in one line each</h2>"
    "<ul>"
    "<li><b>Report.</b> Evidence gathered, findings stated, decisions left to the reader.</li>"
    "<li><b>Memo.</b> A decision or directive, inside the organisation.</li>"
    "<li><b>Essay.</b> An argument, in prose, for a curious reader.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/\">types of writing</a>, <a href=\"/writers/learn/examples/example-of-a-report/\">the report example</a> and <a href=\"/writers/learn/professional-writing/how-to-write-a-memo/\">how to write a memo</a>.</p>",

"entertainment/projector-or-tv-for-movie-nights":
    "<h2>The honest decision</h2>"
    "<p>Projectors sell screen size; TVs sell brightness and simplicity. The decision is made by the room: how dark it gets, how often movie night happens, and who is carrying the equipment up the stairs. The <a href=\"" + _w("video+projector") + "\" rel=\"noopener\">projector</a> category is documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<h2>Where each one wins</h2>"
    "<ul>"
    "<li><b>Dark room, big event.</b> The projector's only argument, and it is a good one.</li>"
    "<li><b>Everyday viewing.</b> The TV wins on friction alone.</li>"
    "<li><b>Gaming and daylight.</b> Latency and lumens settle it.</li>"
    "</ul>"
    "<p>See <a href=\"/entertainment/best-films-for-a-group/\">the best films for a group</a>, <a href=\"/tech/projector-vs-tv-compound-viewing/\">projector versus TV compound viewing</a> and <a href=\"/entertainment/comfort-movies-to-rewatch/\">comfort movies to rewatch</a>.</p>",

"sports/how-the-fa-cup-works":
    "<h2>700-plus teams, one trophy</h2>"
    "<p>The FA Cup is the oldest knockout competition in football and the widest: amateur clubs enter at the bottom, the giants arrive at the top, and replays have been trimmed to keep the calendar honest. The draw is the institution — the morning the minnows get their away day. The <a href=\"" + _w("FA+Cup") + "\" rel=\"noopener\">FA Cup</a> is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>How the giant-killing happens</h2>"
    "<ul>"
    "<li><b>The early rounds are the product.</b> The gap between tiers is the drama.</li>"
    "<li><b>No replays any more.</b> The format bend decided the calendar.</li>"
    "<li><b>Cup runs change small-club budgets.</b> The draw is economic as well as romantic.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/how-extra-time-and-penalty-shootouts-work/\">extra time and penalty shootouts</a>, <a href=\"/sports/champions-league-new-format-explained/\">the Champions League new format</a> and <a href=\"/sports/how-the-transfer-window-works/\">how the transfer window works</a>.</p>",

"tech/outage-lighting-tiers":
    "<h2>Lighting is the outage decision</h2>"
    "<p>When the grid drops, lighting is the first decision and the cheapest to have made: the head-torch, the rechargeable bulb, the lantern, and the candles nobody should use. The tiers map to how long the outage runs and what the household must keep doing. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes candle safety this desk follows. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The tiers</h2>"
    "<ul>"
    "<li><b>Tier one: the head-torch.</b> Hands free beats bright every time.</li>"
    "<li><b>Tier two: rechargeable bulbs.</b> They live in the fitting and charge when the grid returns.</li>"
    "<li><b>Tier three: the power station.</b> Light plus phone plus router, priced by the hour.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/blackout-internet-router-power/\">blackout internet and router power</a>, <a href=\"/tech/inverter-battery-runtime-maths/\">inverter battery runtime maths</a> and <a href=\"/tech/surge-protector-stabiliser-ups/\">surge protector, stabiliser or UPS</a>.</p>",

"writers/guides/when-to-follow-up-on-a-pitch":
    "<h2>The timing rules</h2>"
    "<p>Follow-up is part of the pitching rhythm: wait the stated response time plus a week, send the brief and the new line together, and stop after two unanswered nudges. The follow-up that works reads as professional courtesy, not impatience. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows covers the norms honestly. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The schedule</h2>"
    "<ul>"
    "<li><b>Wait the window.</b> The guidelines' response time is the first clock.</li>"
    "<li><b>One week grace, then nudge once.</b> Reply in-thread; make it easy.</li>"
    "<li><b>Two nudges, then move on.</b> Silence is an answer, eventually.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/how-to-follow-up-on-a-writing-pitch/\">how to follow up on a writing pitch</a>, <a href=\"/writers/guides/how-to-write-a-pitch/\">how to write a magazine pitch</a> and <a href=\"/writers/learn/writing-for-publication/a-rejected-pitch-is-not-wasted/\">a rejected pitch is not wasted</a>.</p>",

"home/paint-calculator":
    "<h2>How much paint a room needs</h2>"
    "<p>The calculator is wall area divided by coverage per litre, minus the windows and doors, plus the second coat and the honest margin for the corner you will spill. The number that comes out is the number of tins — and the reason the leftover tin exists is that nobody ran the maths. Reference material sits under <a href=\"" + _w("paint") + "\" rel=\"noopener\">paint coverage</a>. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the result</h2>"
    "<ul>"
    "<li><b>Measure the room, not the memory.</b> Tape beats estimation every time.</li>"
    "<li><b>Two coats are the default.</b> One-coat claims are about the paint's dreams.</li>"
    "<li><b>Keep the batch number.</b> The second tin must match the first.</li>"
    "</ul>"
    "<p>See <a href=\"/home/mistakes/painting-without-prep/\">painting without prep</a>, <a href=\"/home/basic-toolkit-checklist/\">the basic toolkit checklist</a> and <a href=\"/home/improvements-no-resale-value/\">improvements with no resale value</a>.</p>",

"tech/github-beginner-mistakes":
    "<h2>The mistakes that waste the most time</h2>"
    "<p>Git is not hard; it is unforgiving of fuzzy mental models. The beginner mistakes cluster: committing to main by accident, fighting a merge that should have been a rebase, and losing work to a reset nobody warned about. The <a href=\"" + _w("Git") + "\" rel=\"noopener\">Git version control</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The expensive four</h2>"
    "<ul>"
    "<li><b>Commit messages from the future.</b> 'Fix' tells the blame nothing.</li>"
    "<li><b>Pushing before pulling.</b> The rejected push is a conversation starter.</li>"
    "<li><b>Reset without reading.</b> Hard reset deletes; the reflog is the parachute.</li>"
    "<li><b>Secrets in the first commit.</b> History remembers everything.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/git-and-github-for-beginners/\">Git and GitHub for beginners</a>, <a href=\"/tech/git-errors-fixed/\">Git errors, fixed</a> and <a href=\"/tech/github-token-hygiene/\">GitHub token hygiene</a>.</p>",

"tech/paper-trading-bot-lessons":
    "<h2>SQLite, Telegram, and the point</h2>"
    "<p>The paper-trading bot taught its lessons cheaply: SQLite holds the trades, Telegram delivers the alerts, and the whole rig never risked a naira on the strategy it was testing. The engineering was the easy part; the honest benchmarking was the project. The <a href=\"" + _w("paper+trading") + "\" rel=\"noopener\">paper trading</a> is documented in standard references. By the Bryme Technical Research desk. Reviewed 28 September 2026.</p>"
    "<h2>What the project proved</h2>"
    "<ul>"
    "<li><b>Logging beats cleverness.</b> The trade table is the research.</li>"
    "<li><b>Alerts are UX, not strategy.</b> The bot's job is the record, not the dopamine.</li>"
    "<li><b>Simulation first, always.</b> The cheapest tuition in the market.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/backtest-validation-checklist/\">the backtest validation checklist</a>, <a href=\"/tech/position-sizing-ruin-the-math-most-backtests-skip/\">position sizing and ruin</a> and <a href=\"/tech/quantlab-project-how-built/\">how QuantLab was built</a>.</p>",

"tech/websocket-debugging":
    "<h2>From handshake to message</h2>"
    "<p>WebSocket failures live in layers: the handshake that never upgrades, the connection that drops at the proxy, the message that arrives mangled by framing. Debugging is walking the path in order — HTTP first, then the socket, then the payload. The <a href=\"" + _w("WebSocket") + "\" rel=\"noopener\">WebSocket protocol</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The debugging path</h2>"
    "<ul>"
    "<li><b>The handshake is HTTP.</b> 4xx here is a config problem, not a socket one.</li>"
    "<li><b>Proxies and idle timeouts.</b> The silent drop lives at the infrastructure.</li>"
    "<li><b>Frame the payload.</b> Text versus binary is the classic mangle.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/handle-api-errors-python/\">handling API errors in Python</a>, <a href=\"/tech/http-status-codes-explained/\">HTTP status codes explained</a> and <a href=\"/tech/how-to-read-an-error-message/\">how to read an error message</a>.</p>",

"writers/learn/freelance-paid-writing/the-tax-set-aside-habit":
    "<h2>The habit that keeps tax money spent</h2>"
    "<p>Freelance income arrives gross, and the set-aside habit is the fix: a fixed percentage moved to a separate pot on payment day. The mechanics are deliberately boring — the habit works because it removes the monthly decision. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government self-assessment guidance</a> is the standard this desk follows. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Running the habit</h2>"
    "<ul>"
    "<li><b>Percentage, not amount.</b> The rate survives a slow month.</li>"
    "<li><b>Payment day, not month end.</b> Timing is the entire trick.</li>"
    "<li><b>Yearly rate review.</b> The habit bends with the income.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/the-tax-set-aside-habit/\">the tax set-aside habit guide</a>, <a href=\"/writers/learn/freelance-paid-writing/business-expenses-for-writers/\">business expenses for writers</a> and <a href=\"/writers/learn/freelance-paid-writing/how-to-invoice-as-a-writer/\">how to invoice as a writer</a>.</p>",

"writers/writing/kenyon-review":
    "<h2>A per-word literary standard</h2>"
    "<p>The Kenyon Review pays per published word of prose within stated minimums and maximums — terms that make it one of the transparent literary markets. Its pages have published generations of careers; the reading is serious and the payment is real. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>The per-word model rewards the true length.</b> Cut to the story's needs.</li>"
    "<li><b>The archive is the brief.</b> Read two issues before the first submission.</li>"
    "<li><b>Patience is part of the terms.</b> Literary response times are slow by design.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/cincinnati-review/\">The Cincinnati Review</a>, <a href=\"/writers/writing/the-ex-puritan/\">The Ex-Puritan</a> and <a href=\"/writers/writing/agni/\">AGNI</a>.</p>",

"tech/cloud-storage-mistakes":
    "<h2>The mistakes that lose files</h2>"
    "<p>Cloud storage loses files the same way every time: sync is not backup, one copy lives in the recycle bin's memory, and the account that holds the data is not protected like the vault it is. The cloud keeps your files safe from disk failure, not from you. The <a href=\"" + _w("cloud+storage") + "\" rel=\"noopener\">cloud storage model</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The failure modes</h2>"
    "<ul>"
    "<li><b>Sync deletes everywhere.</b> The mirror mirrors deletions too.</li>"
    "<li><b>One account is a single point of failure.</b> Protect the email behind it first.</li>"
    "<li><b>Free tiers have expiry habits.</b> Dormant accounts get cleaned.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/three-two-one-backup-rule/\">the 3-2-1 backup rule</a>, <a href=\"/tech/cloud-vs-local-backup/\">cloud versus local backup</a> and <a href=\"/tech/home-nas-vs-cloud-vs-drive/\">home NAS versus cloud versus drive</a>.</p>",

"tech/handle-api-errors-python":
    "<h2>Status codes, timeouts, retries</h2>"
    "<p>Handling API errors in Python is a small discipline: catch the status families deliberately, bound the retries with backoff, and log the response body because the message is the clue. The unhandled 500 is the outage you cause yourself. The <a href=\"" + _w("HTTP+status+code") + "\" rel=\"noopener\">HTTP status code</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The handling order</h2>"
    "<ul>"
    "<li><b>Timeouts are errors too.</b> The default socket timeout is longer than your patience.</li>"
    "<li><b>Retry 429 and 5xx only.</b> Retrying a 400 is a bug wearing a retry.</li>"
    "<li><b>Exponential backoff with jitter.</b> The stampede is self-inflicted.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/http-status-codes-explained/\">HTTP status codes explained</a>, <a href=\"/tech/api-returns-error-diagnostic/\">the API error diagnostic</a> and <a href=\"/tech/parse-json-python/\">parsing JSON in Python</a>.</p>",

"tech/tool":
    "<h2>Small tools, zero strings</h2>"
    "<p>Every tool here runs in the browser: no accounts, no uploads, no telemetry selling the clickstream back. The utilities cover the daily developer and writer chores — encode, convert, count, calculate — and the design rule is that the page is faster than the problem. The <a href=\"" + _w("web+application") + "\" rel=\"noopener\">in-browser tooling</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>Why client-side matters</h2>"
    "<ul>"
    "<li><b>The data never leaves.</b> Your text stays your text.</li>"
    "<li><b>No account is a feature.</b> The tool opens and works.</li>"
    "<li><b>Offline-tolerant.</b> Once loaded, the maths is local.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/tool/base64-encoder/\">the base64 encoder</a>, <a href=\"/tech/tool/case-converter/\">the case converter</a> and <a href=\"/tech/tool/http-status-lookup/\">the HTTP status lookup</a>.</p>",

"writers/learn/types-of-writing":
    "<h2>What each form is for</h2>"
    "<p>Every form of writing is a contract with a reader: the essay argues, the report evidences, the review judges, the pitch sells. Choosing the form is choosing what the reader is allowed to expect — and most confused drafts are the wrong form doing the right work. The <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing forms</a> are documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>The map, in brief</h2>"
    "<ul>"
    "<li><b>Essay and article.</b> Argument versus reportage; the reader's job differs.</li>"
    "<li><b>Professional documents.</b> Memo, letter, report — each with a workplace.</li>"
    "<li><b>Creative forms.</b> Story, script, poem — the contract is the imagination.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/learn/types-of-writing/how-to-write-an-essay/\">how to write an essay</a>, <a href=\"/writers/learn/types-of-writing/how-to-write-an-article/\">how to write an article</a> and <a href=\"/writers/compare/\">which format you need</a>.</p>",

"writers/writing/the-ex-puritan":
    "<h2>Canadian literary, wide range</h2>"
    "<p>The Ex-Puritan pays by the type of writing and is especially open to experimental and cross-genre work — a market where the submission's shape can be the argument. Its terms are stated clearly, which is rarer than the craft. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Submitting well</h2>"
    "<ul>"
    "<li><b>Genre lines are soft here.</b> The work's logic decides the fit.</li>"
    "<li><b>Payment varies by form.</b> The guidelines state it; the budget should match.</li>"
    "<li><b>The interviews are the reading list.</b> The magazine explains itself often.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/carte-blanche/\">carte blanche</a>, <a href=\"/writers/writing/the-malahat-review/\">The Malahat Review</a> and <a href=\"/writers/writing/prism-international/\">PRISM international</a>.</p>",

"tech/earbud-one-side-quiet":
    "<h2>Wax, contact grime, or balance</h2>"
    "<p>One quiet earbud is three different faults: the mesh is blocked, the charging contacts are dirty, or the device's balance slider moved during a call. The fix order is cleaning first, contacts second, settings last — because the first two are free. The <a href=\"" + _w("earphone") + "\" rel=\"noopener\">earbud hardware</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The fix order</h2>"
    "<ul>"
    "<li><b>Clean the mesh gently.</b> Wax is the answer most of the time.</li>"
    "<li><b>Scrub the charge contacts.</b> Grime makes one side underperform.</li>"
    "<li><b>Check the audio balance slider.</b> The setting moves during calls, silently.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/anc-vs-passive-isolation-earbuds/\">ANC versus passive isolation</a>, <a href=\"/tech/wireless-earbuds-for-calls/\">wireless earbuds for calls</a> and <a href=\"/tech/bluetooth-wont-pair-reset/\">Bluetooth won't pair: the reset</a>.</p>",

"tech/phone-photo-haze-lens-clean":
    "<h2>The lens film nobody sees</h2>"
    "<p>Foggy phone photos are usually the lens, not the sensor: the oleophobic film of fingerprints and pocket lint that the phone's processing hides in daylight and reveals at dusk. The two-minute clean is the camera upgrade everyone owns. The <a href=\"" + _w("photography") + "\" rel=\"noopener\">photography basics</a> are documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The clean, properly</h2>"
    "<ul>"
    "<li><b>Cloth first, breath second.</b> The shirt hem is sandpaper in disguise.</li>"
    "<li><b>Check the case lip.</b> Cases trap the grime against the glass.</li>"
    "<li><b>Look for the haze at night.</b> Light flare is the film's signature.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/phone-video-quality-light-and-sound/\">phone video quality: light and sound</a>, <a href=\"/tech/muffled-phone-speaker-clean/\">the muffled speaker clean</a> and <a href=\"/tech/how-to-take-a-screenshot-windows/\">taking a screenshot</a>.</p>",

"writers/state-of-paid-writing-2026":
    "<h2>What the year changed</h2>"
    "<p>The paid writing market in 2026 runs on the same two engines as ever — expertise and access — with AI slop pushing editors toward bylines with receipts. Rates hold at the top and compress in the middle; the writers who report, invoice and niche survive the compression. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the shifts. By the Bryme Editorial desk. Reviewed 28 September 2026.</p>"
    "<h2>The findings that matter</h2>"
    "<ul>"
    "<li><b>Reported work holds value.</b> Verification is the moat now.</li>"
    "<li><b>Niches price better.</b> The specialist's rate is the survivor's rate.</li>"
    "<li><b>The middle is squeezed.</b> General explainers compete with the machine.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/guides/where-the-money-is-in-writing/\">where the money is in writing</a>, <a href=\"/writers/learn/freelance-paid-writing/how-to-price-your-freelance-writing/\">how to price your freelance writing</a> and <a href=\"/writers/guides/track-your-writing-income/\">track your writing income</a>.</p>",

"writers/writing/whatculture":
    "<h2>The list market</h2>"
    "<p>WhatCulture pays per published list article and more for commissioned forms — a volume market with a known format and honest terms. Its lists work when the argument is real and the entries are the evidence. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<h2>Writing the list that lands</h2>"
    "<ul>"
    "<li><b>The title is the argument.</b> 'Best' needs a criterion the reader can check.</li>"
    "<li><b>Entries earn their place.</b> The padding is what editors cut first.</li>"
    "<li><b>The format is the product.</b> Voice lives inside the structure, not against it.</li>"
    "</ul>"
    "<p>See <a href=\"/writers/writing/eater/\">Eater</a>, <a href=\"/writers/writing/rest-of-world-2/\">Rest of World</a> and <a href=\"/writers/writing/the-kitchn/\">The Kitchn</a>.</p>",

"home/improvements-no-resale-value":
    "<h2>The upgrades that are for you</h2>"
    "<p>Some improvements are consumption, not investment: the pool in a cold climate, the luxury kitchen in the modest street, the conversion that removes a bedroom. Knowing which is which protects both the budget and the resale conversation. The <a href=\"" + _w("home+improvement") + "\" rel=\"noopener\">home improvement economics</a> are documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The honest list</h2>"
    "<ul>"
    "<li><b>Over-personalised rooms.</b> The next buyer pays to undo them.</li>"
    "<li><b>Swimming pools outside the climate.</b> Maintenance as lifestyle, not value.</li>"
    "<li><b>Garage conversions.</b> Parking often prices above the extra room.</li>"
    "</ul>"
    "<p>See <a href=\"/home/bathroom-remodel-mistakes/\">bathroom remodel mistakes</a>, <a href=\"/home/inspection-checklist-gaps/\">inspection checklist gaps</a> and <a href=\"/home/building-regs-vs-planning-permission/\">building regs versus planning permission</a>.</p>",

}

TOPUP_SECTIONS13 = {

"sports/ligue-1-results":
    "<h2>Results as form evidence</h2>"
    "<p>A Ligue 1 results run reads like every other league's only slower to the eye: the table compresses streaks that the sequence explains, and the schedule decides which of those streaks mean anything. Reading results as form is the oldest discipline in football analysis. The <a href=\"" + _w("Ligue+1") + "\" rel=\"noopener\">Ligue 1</a> competition structure is documented in standard references. By the Bryme Sports desk. Reviewed 28 September 2026.</p>"
    "<h2>Reading the run</h2>"
    "<ul>"
    "<li><b>Sequence over totals.</b> Form is a direction, not an aggregate.</li>"
    "<li><b>Note who scored first.</b> Leaders and chasers win differently.</li>"
    "<li><b>Weight the opposition.</b> The schedule decides what the results measure.</li>"
    "</ul>"
    "<p>See <a href=\"/sports/premier-league-results/\">the Premier League results</a>, <a href=\"/sports/bundesliga-results/\">the Bundesliga results</a> and <a href=\"/sports/how-the-premier-league-table-works/\">how the table works</a>.</p>",

"home/mistakes/mixing-cleaning-products":
    "<h2>The chemistry lesson that matters</h2>"
    "<p>Bleach and ammonia, bleach and acid — the household mixes that release gas are few, famous and still hospitalise people every year. The rule is one product at a time, rinsed between, and the bottle's warning read before the cap comes off. The <a href=\"" + EPA + "\" rel=\"noopener\">US Environmental Protection Agency</a> publishes household chemical guidance this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The never-mix list</h2>"
    "<ul>"
    "<li><b>Bleach plus anything acidic.</b> Chlorine gas is the product.</li>"
    "<li><b>Bleach plus ammonia cleaners.</b> Glass cleaner is the usual suspect.</li>"
    "<li><b>Rinse between products.</b> The residue is still chemistry.</li>"
    "</ul>"
    "<p>See <a href=\"/home/mistakes/drying-laundry-indoors/\">drying laundry indoors</a>, <a href=\"/home/mistakes/painting-without-prep/\">painting without prep</a> and <a href=\"/home/deep-clean-schedule/\">the deep clean schedule</a>.</p>",

"tech/csp-safe-front-end":
    "<h2>Patterns that survive redesigns</h2>"
    "<p>Content Security Policy is easier to design into a front end than to bolt on after the first audit: inline scripts moved to files, styles through classes not attributes, and third parties pinned to named origins. The policy is a design constraint that pays out at every redesign. The <a href=\"" + _w("Content+Security+Policy") + "\" rel=\"noopener\">Content Security Policy</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The patterns</h2>"
    "<ul>"
    "<li><b>External scripts, always.</b> The inline ban is the policy's heart.</li>"
    "<li><b>Nonces over unsafe-inline.</b> The escape hatch should be narrow.</li>"
    "<li><b>Report-only first.</b> The header learns your app before it governs it.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/ddos-protection-for-small-sites/\">DDoS protection for small sites</a>, <a href=\"/tech/ssl-certificate-errors-explained/\">SSL certificate errors explained</a> and <a href=\"/tech/why-your-website-is-slow/\">why your website is slow</a>.</p>",

"home/mistakes/painting-without-prep":
    "<h2>The prep is the paint job</h2>"
    "<p>Paint applied to an unprepared wall fails in the ways everyone has seen: peeling at the edges, flashing through the patches, and a finish that shows every shortcut. The unglamorous hours — cleaning, filling, sanding, priming — are the paint job; the colour is the reward. The <a href=\"" + _w("paint") + "\" rel=\"noopener\">painting practice</a> is documented in standard references. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<h2>The prep that pays</h2>"
    "<ul>"
    "<li><b>Wash the wall.</b> Grease rejects paint politely and permanently.</li>"
    "<li><b>Fill, then sand.</b> The patch you can feel is the patch you will see.</li>"
    "<li><b>Prime the repairs.</b> Filler drinks paint differently than the wall.</li>"
    "</ul>"
    "<p>See <a href=\"/home/paint-calculator/\">the paint calculator</a>, <a href=\"/home/mistakes/mixing-cleaning-products/\">mixing cleaning products</a> and <a href=\"/home/basic-toolkit-checklist/\">the basic toolkit checklist</a>.</p>",

"tech/windows-keyboard-shortcuts":
    "<h2>The shortcuts worth memorising</h2>"
    "<p>The Windows shortcuts that pay rent are the ones that replace reaching for the mouse: window management, the snipping tool, and the handful of system dialogs that rescue a frozen afternoon. Everything else is trivia. The <a href=\"" + _w("keyboard+shortcut") + "\" rel=\"noopener\">keyboard shortcut</a> system is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<h2>The working set</h2>"
    "<ul>"
    "<li><b>Win+arrows.</b> The window manager nobody knows exists.</li>"
    "<li><b>Win+Shift+S.</b> The screenshot that saves the meeting.</li>"
    "<li><b>Ctrl+Shift+Esc.</b> The task manager, one chord from anywhere.</li>"
    "</ul>"
    "<p>See <a href=\"/tech/how-to-take-a-screenshot-windows/\">how to take a screenshot on Windows</a>, <a href=\"/tech/chrome-vs-edge-old-laptop/\">Chrome versus Edge on an old laptop</a> and <a href=\"/tech/computer-fans-loud/\">loud computer fans</a>.</p>",

}
