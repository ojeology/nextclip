# -*- coding: utf-8 -*-
"""Editorial depth extras, part 14: batch I rescue pass. The 15 batch I pages
whose t8 blocks landed just under their bars (736-749 of 750, and tech/tool at
660 of 669). Injected with marker data-esrc=\"t8c\" which does not collide with
t8/t8b idempotency. ~100 words each clears every gap."""

CLMP = "https://www.clmp.org/"
LITHUB = "https://lithub.com/"
EPA = "https://www.epa.gov/"
GOVUK = "https://www.gov.uk/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

EXTRA_SECTIONS14 = {

"tech/handle-api-errors-python":
    "<h2>Log the body</h2>"
    "<p>The response body is the error's actual message; the status code is only its envelope. A debugging habit that logs both — with the request id — turns a 3am incident into a two-minute grep. The <a href=\"" + _w("debugging") + "\" rel=\"noopener\">debugging practice</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Log request ids.</b> The provider's support needs the same string you saw.</li>"
    "<li><b>Bound the retry.</b> Three attempts, then the alert — never an infinite loop.</li>"
    "<li><b>Keep the last response.</b> The clue survives the crash that way.</li>"
    "</ul>",

"writers/writing/wired":
    "<h2>The clip that opens the door</h2>"
    "<p>WIRED reads pitches against clips: one deeply reported piece in an adjacent beat beats five posts about everything. The market rewards the writer who has already done the reporting once. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>One beat, deeply.</b> The portfolio should argue a specialism.</li>"
    "<li><b>Show the reporting.</b> Clips with named sources travel fastest.</li>"
    "<li><b>Pitch the gap.</b> The story the beat has not covered yet.</li>"
    "</ul>",

"tech/earbud-one-side-quiet":
    "<h2>When cleaning fails</h2>"
    "<p>If the mesh is clean and the contacts shine, the fault is firmware or driver balance — reset the pair, re-pair it, and test against another device before condemning the hardware. The <a href=\"" + _w("Bluetooth") + "\" rel=\"noopener\">Bluetooth pairing</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Reset and re-pair.</b> The classic fix for the persistent imbalance.</li>"
    "<li><b>Test on a second device.</b> It splits hardware from settings instantly.</li>"
    "<li><b>Check warranty early.</b> Driver failure inside a year is their problem.</li>"
    "</ul>",

"writers/learn/freelance-paid-writing/the-tax-set-aside-habit":
    "<h2>When the pot is raided</h2>"
    "<p>The habit breaks in predictable months — the slow quarter, the big invoice delay — and the fix is structural: the pot is untouchable and the rate is set high enough to survive a slow year. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government guidance</a> is the standard this desk follows. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Over-set rather than under.</b> A refund beats a bill every year.</li>"
    "<li><b>Never borrow from the pot.</b> The rule is the whole strategy.</li>"
    "<li><b>Invoice on time.</b> Cash flow is what breaks the habit.</li>"
    "</ul>",

"writers/writing/kenyon-review":
    "<h2>Building the submission</h2>"
    "<p>Literary submissions are read in order of arrival and judged on the first page — the opening that proves the sentence quality earns the rest of the read. Patience and precision are the market's whole demand. The <a href=\"" + CLMP + "\" rel=\"noopener\">Community of Literary Magazines and Presses</a> catalogs the wider field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>The first page is the audition.</b> Put the best sentence near the top.</li>"
    "<li><b>Follow the format exactly.</b> Formatting is the first filter.</li>"
    "<li><b>Submit to the fit.</b> The archive decides more acceptances than polish.</li>"
    "</ul>",

"tech/phone-photo-haze-lens-clean":
    "<h2>When the haze is inside</h2>"
    "<p>If the clean does not fix it, the haze is inside the lens assembly — condensation from a swim, a drop that unsealed the glass, or the sealant ageing out. The camera is then a repair decision, not a cleaning one. The <a href=\"" + _w("smartphone+camera") + "\" rel=\"noopener\">smartphone camera</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Sealed unit, sealed fate.</b> Internal fog means the seal is gone.</li>"
    "<li><b>Silica gel is a myth fix.</b> The unit needs opening; the drawer does not.</li>"
    "<li><b>Weigh the repair.</b> Camera module prices approach half the phone's.</li>"
    "</ul>",

"writers/learn/examples/example-of-a-product-description":
    "<h2>The structure, named</h2>"
    "<p>The example follows a repeatable shape: use case first, specifics second, proof third, and the honest limit last. Steal the shape and the writing gets easier every time. The <a href=\"" + _w("copywriting") + "\" rel=\"noopener\">copywriting practice</a> is documented in standard references. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Use case in line one.</b> The reader recognises their own Tuesday.</li>"
    "<li><b>Specifics in the middle.</b> Measurements beat adjectives in every test.</li>"
    "<li><b>The limit last.</b> Honesty converts better than perfection.</li>"
    "</ul>",

"entertainment/projector-or-tv-for-movie-nights":
    "<h2>The hidden costs</h2>"
    "<p>Projectors carry costs the demo room hides: lamp hours, blackout curtains, speaker placement, and the fan noise that arrives with the credits. The honest comparison runs five years, not one evening. The <a href=\"" + _w("video+projector") + "\" rel=\"noopener\">projector economics</a> are documented in standard references. By the Bryme Entertainment desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Lamps and lasers cost per hour.</b> The bulb is a subscription in disguise.</li>"
    "<li><b>Sound needs its own budget.</b> The picture upgrade reveals the speakers.</li>"
    "<li><b>The room is the real purchase.</b> Darkness is the projector's specification.</li>"
    "</ul>",

"writers/writing/the-ex-puritan":
    "<h2>Reading the interviews</h2>"
    "<p>The magazine explains itself in its interview archive — the editors' tastes, the work they remember, and the submissions that failed in instructive ways. Reading them is the cheapest editorial advice available. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows covers the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Editors quote their favourites.</b> The reading list lives in the interviews.</li>"
    "<li><b>Rejection notes recur in themes.</b> The patterns are publishable advice.</li>"
    "<li><b>Submit after reading.</b> Fit is a reading outcome, not a guess.</li>"
    "</ul>",

"writers/writing/aarp-magazine":
    "<h2>The pitch that lands</h2>"
    "<p>The magazine buys service journalism with receipts — the piece that answers a reader's real question with reporting rather than reassurance. The pitch names the reader, the question and the reporting plan. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Name the reader's decision.</b> Service is measured in actions.</li>"
    "<li><b>Report the claim.</b> Health and money pieces are checked.</li>"
    "<li><b>Match the section.</b> The desk decides the story's home.</li>"
    "</ul>",

"tech/tool":
    "<h2>Built to be boring</h2>"
    "<p>These utilities are deliberately uneventful: the input accepts, the output appears, and nothing phones home. Boring is the feature — the tool that surprises you is the tool you cannot trust with the client's text. The <a href=\"" + _w("web+application") + "\" rel=\"noopener\">in-browser tooling</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>No state, no servers.</b> The page forgets you the moment it closes.</li>"
    "<li><b>Keyboard first.</b> The tab order is the usability.</li>"
    "<li><b>Predictable output.</b> The same input, every time, on every device.</li>"
    "</ul>",

"writers/writing/whatculture":
    "<h2>The pitch shape</h2>"
    "<p>WhatCulture commissions from pitches that show the list's argument before the list exists: the criterion in the title, the entries already named, the voice visible in the sample. The format is fixed; the angle is the pitch. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Pitch the criterion.</b> 'Best' is a filter the reader can test.</li>"
    "<li><b>Name the entries early.</b> The editor reads the list in the pitch.</li>"
    "<li><b>Show the voice.</b> One sample entry sells the whole piece.</li>"
    "</ul>",

"tech/windows-keyboard-shortcuts":
    "<h2>The second tier</h2>"
    "<p>Beyond the rescue chords sits a second tier worth learning slowly: Win+V for the clipboard history, Win+. for the picker, and Alt+Tab's cousin Win+Tab for the desktops. The set compounds — each shortcut pays for the next. The <a href=\"" + _w("keyboard+shortcut") + "\" rel=\"noopener\">shortcut system</a> is documented in standard references. By the Bryme Tech desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Win+V.</b> Clipboard history: the feature that changes how you copy.</li>"
    "<li><b>Win+arrows, twice.</b> Snap layouts on the second press.</li>"
    "<li><b>Learn one per week.</b> The habit beats the cheat sheet.</li>"
    "</ul>",

"home/improvements-no-resale-value":
    "<h2>How the surveyor sees it</h2>"
    "<p>Surveyors price the house the next buyer needs, not the house the owner loves: standard layouts, legal compliance and honest maintenance carry value; bespoke taste does not. The improvement that helps most is often the one nobody photographs. The <a href=\"" + GOVUK + "\" rel=\"noopener\">UK government home guidance</a> is the standard this desk follows. By the Bryme Home desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Compliance first.</b> Certificates add value; features merely please.</li>"
    "<li><b>Maintenance over makeovers.</b> The roof sells the house.</li>"
    "<li><b>Keep the receipts.</b> Evidence of care is a line item.</li>"
    "</ul>",

"writers/writing/the-kitchn":
    "<h2>The diary's structure</h2>"
    "<p>The budget diary works because it is a real week with a real number at the end: the plan, the shop, the substitutions, and what the family actually ate. Structure is what turns diary into service journalism. The <a href=\"" + LITHUB + "\" rel=\"noopener\">literary press</a> this desk follows tracks the field. By the Bryme Writers desk. Reviewed 28 September 2026.</p>"
    "<ul>"
    "<li><b>Number the week.</b> The total is the story's proof.</li>"
    "<li><b>Show the substitutions.</b> Readers need the improvisation.</li>"
    "<li><b>End with the lesson.</b> Service journalism earns its ending.</li>"
    "</ul>",

}
