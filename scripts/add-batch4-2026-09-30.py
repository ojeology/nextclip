#!/usr/bin/env python3
"""Add verified writing-market batch 4 (2026-09-30).

Twelve NEW markets. Every figure was read off the publication's own guidelines
page on 2026-09-30; raw page text is saved under research/batch4/<slug>.txt.

HOW THESE WERE FOUND, and why the method changed. Batches 1-3 guessed
submissions paths (/submissions/, /submit/) from a domain, which resolved to
the wrong site 54 times out of 160 in batch 2. Batch 4 instead scraped the
Poets & Writers Literary Magazines directory, which lists each magazine's OWN
submissions URL:

    35 listing pages -> 874 magazine names -> 827 not already known
    -> 613 with an official submissions URL -> 450 passed the content filter
    -> 12 shipped in this batch

pw.org was used ONLY for names and official URLs. It publishes pay notes of its
own; none were used. Every rate below comes from the publication's own page.

Note on base country: none of these twelve publishes its country on its
guidelines page, so pub-countries records "International" rather than a guess.
Peach is the exception - peach.gcsu.edu is a US .edu domain.

Rejects and holds are logged at the bottom.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-30"


def rec(slug, publication, title, seo, excerpt, official, apply_url, apply_email,
        apply_method, sources, elig, types, type_label, pay, wc, response,
        status, deadline, ai, want, dont, reqs, rights, how, keywords):
    return {
        "status": "published", "vertical": "writing",
        "lastVerified": V, "publishedAt": V,
        "experience": "not-stated",
        "editorExperience": {"status": "not-yet-submitted"},
        "id": slug, "slug": slug, "publication": publication,
        "title": title, "seoTitle": seo, "excerpt": excerpt,
        "officialUrl": official, "applyUrl": apply_url, "applyEmail": apply_email,
        "applyMethod": apply_method, "sources": sources,
        "eligibility": elig, "writingTypes": types, "writingTypeLabel": type_label,
        "pay": pay, "wordCount": wc, "response": response,
        "submissionStatus": status, "deadline": deadline, "aiPolicy": ai,
        "whatTheyWant": want, "whatTheyDontWant": dont, "requirements": reqs,
        "rights": rights, "howToSubmit": how, "keywords": keywords,
    }


def src(name, url):
    return [{"name": name, "url": url}]


def pay(cur, lo, hi, display, conditions, timing):
    return {"currency": cur, "amountMin": lo, "amountMax": hi,
            "display": display, "conditions": conditions, "timing": timing}


def intl():
    return {"summary": "No stated country restriction on the guidelines page.",
            "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True,
            "notStated": True}


NEW = []

# ------------------------------------------------------- 1 Litmosphere
NEW.append(rec(
    "litmosphere-charlotte-lit", "Litmosphere: Journal of Charlotte Lit",
    "Poetry, flash, short fiction and literary nonfiction",
    "Litmosphere: $25 per poem or flash, $50 per story, no AI",
    "Litmosphere, the journal of Charlotte Lit, pays $25 for each accepted poem "
    "or flash piece and $50 for each accepted short fiction or nonfiction piece, "
    "taking first electronic rights and non-exclusive archival rights while "
    "copyright stays with the author. It takes fiction and literary nonfiction "
    "of 1,500 to 5,000 words, flash of up to 500 words, and up to three poems. "
    "AI-generated or assisted work is prohibited.",
    "https://litmosphere.charlottelit.org/submissions/",
    "https://litmosphere.charlottelit.org/submissions/", None,
    "Submittable — open in January and July only",
    src("Litmosphere — Submissions (official)",
        "https://litmosphere.charlottelit.org/submissions/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, flash, short fiction and literary nonfiction",
    pay("USD", 25, 50, "$25 per poem or flash piece; $50 per short fiction or nonfiction piece",
        "Official submissions page: Litmosphere pays $25 for each accepted poem or flash piece "
        "and $50 for each accepted short fiction and nonfiction piece, for first electronic "
        "rights and non-exclusive archival rights.",
        "Not publicly stated"),
    {"min": 1500, "max": 5000,
     "display": "Fiction and literary nonfiction 1,500–5,000 words; flash up to 500 words each"},
    {"label": "Not stated; the queue closes at 300 submissions", "band": "not-stated",
     "official": False},
    "upcoming",
    {"date": None,
     "display": "Submissions open through Submittable during January for the Spring issue and "
                "during July for the Fall issue. The queue closes at 300 submissions and usually "
                "fills well before the end of the month.",
     "recurring": True},
    "prohibited",
    ["Short fiction and literary nonfiction of 1,500 to 5,000 words.",
     "Flash of up to 500 words each, up to three pieces, preferably stories or essays that "
     "speak to each other.",
     "Up to three poems, ideally related topically, thematically or stylistically — Litmosphere "
     "prefers to showcase multiple pieces as a set from each selected contributor."],
    ["AI-generated or AI-assisted work. Prohibited outright.",
     "Submissions outside the January and July windows.",
     "Prose longer than 5,000 words."],
    ["Submit through Charlotte Lit's Submittable page during January or July.",
     "Fiction and nonfiction: one piece, 1,500–5,000 words, in a readable font.",
     "Flash: up to three pieces of up to 500 words each.",
     "Poetry: up to three poems, up to ten pages total.",
     "If a piece is accepted elsewhere, withdraw through Submittable's Message function — not "
     "Notes.",
     "Expect the queue to close early; it caps at 300 submissions."],
    "Litmosphere takes first electronic rights and non-exclusive archival rights. Copyright "
    "remains with the author.",
    ["Check whether the January or July window is open before you prepare anything.",
     "Send related pieces together — the journal deliberately showcases sets.",
     "Do not submit by email; Submittable is the only route."],
    ["litmosphere", "charlotte lit", "poetry", "flash", "$25", "$50", "submittable", "no ai"]))

# ------------------------------------------------------- 2 Ninth Letter
NEW.append(rec(
    "ninth-letter", "Ninth Letter", "Poetry, fiction, creative nonfiction and flash",
    "Ninth Letter: $100 prose, $25 per poem, no generative AI",
    "Ninth Letter pays $25 per poem and $100 for prose in its print issues, plus "
    "two complimentary copies, and $25 per poem or $75 per piece of prose for "
    "its web issues. It takes one story or essay of up to 8,000 words, three to "
    "five poems, or flash, and acquires First North American Serial Rights. "
    "Work created, guided or revised with generative AI is not accepted, though "
    "assistive tools such as dictation and spell check are permitted.",
    "https://ninthletter.com/submit/",
    "https://ninthletter.com/submit/", None, "Submittable — $3 reading fee",
    src("Ninth Letter — Submit (official)", "https://ninthletter.com/submit/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, fiction, creative nonfiction and flash",
    pay("USD", 25, 100,
        "Print: $100 prose, $25 per poem + 2 copies. Web: $75 prose, $25 per poem",
        "Official submit page: Ninth Letter pays $25 per poem and $100 for prose upon "
        "publication plus two complimentary copies of the issue. Authors selected for a web "
        "issue are offered $25 per poem or $75 per piece of prose plus an exclusive discount on "
        "a one-year print subscription. A $3 reading fee applies.",
        "Upon publication"),
    {"min": None, "max": 8000,
     "display": "One story or essay up to 8,000 words; 3–5 poems; flash up to 3 pieces "
                "totalling 4,000 words"},
    {"label": "Within six months for print, four months for web issues",
     "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Fiction and creative nonfiction: one story or essay of up to 8,000 words at a time.",
     "Poetry: three to five poems.",
     "Flash: up to three pieces with a total word count of no more than 4,000 words.",
     "Unpublished work only — including work self-published on websites or blogs."],
    ["Work created, guided or revised using generative AI intervention or prompts. Ninth Letter "
     "states it is interested in human creativity and human writing processes, not the "
     "generative capabilities of AI or LLMs.",
     "Previously published work, including self-published work on websites and blogs.",
     "Submissions by email attachment — they will not be read.",
     "Note the distinction that does apply: assistive AI tools such as spell check, grammar "
     "check, dictation, speech-to-text and screen-reading software are permitted."],
    ["Submit electronically through Submittable; email submissions are not read.",
     "Pay the $3 reading fee.",
     "Keep prose to 8,000 words and poetry to three to five poems.",
     "Simultaneous submissions are welcome — send a withdrawal message immediately on acceptance "
     "elsewhere."],
    "Ninth Letter acquires First North American Serial Rights.",
    ["Read https://ninthletter.com/submit/ for the full guidelines before sending.",
     "Do not email your manuscript.",
     "Assistive accessibility tools are fine; generative AI is not."],
    ["ninth letter", "poetry", "fiction", "creative nonfiction", "$100", "$25", "fnasr",
     "no generative ai", "submittable"]))

# ------------------------------------------------------- 3 Star*Line
NEW.append(rec(
    "star-line-sfpa", "Star*Line", "Speculative poetry, essays and reviews",
    "Star*Line: 7 cents a word for poems, always open, no AI",
    "Star*Line, the journal of the Science Fiction & Fantasy Poetry Association, "
    "pays 7 cents a word for poems with a $7 minimum and $30 maximum, 5 cents a "
    "word for articles and essays, and a flat $7 for book or chapbook reviews. "
    "It is always open for submissions and typically responds within three "
    "weeks. It does not accept AI-generated content of any kind.",
    "https://sfpoetry.org/wp/starline/",
    "https://sfpoetry.org/wp/starline/", None, "Email submission — always open",
    src("Star*Line — Submission Guidelines (official)", "https://sfpoetry.org/wp/starline/"),
    intl(),
    ["poetry", "essays", "reviews"], "Speculative poetry, articles, essays and reviews",
    pay("USD", 7, 30,
        "7¢/word for poems ($7 minimum, $30 maximum); 5¢/word essays; $7 reviews",
        "Official guidelines: Star*Line pays 7 cents per word for poems with a minimum of $7 and "
        "a maximum of $30. Articles and essays are 5 cents per word. Book or chapbook reviews "
        "are a flat $7. Cover art is $30 plus five copies and interior art $8. Star*Line pays on "
        "publication and all contributors also receive one print copy.",
        "On publication"),
    {"min": None, "max": None, "display": "Up to five poems of any length in a single email"},
    {"label": "Typically up to three weeks; always open", "band": "2-4-weeks", "official": True},
    "open", None, "prohibited",
    ["Speculative poetry — up to five poems of any length in a single email.",
     "Articles and essays, paid at 5 cents a word.",
     "Book or chapbook reviews, paid at a flat $7.",
     "Cover and interior art."],
    ["AI-generated content of any kind. Star*Line does not accept it and points to the SFPA's "
     "Statement on Generative AI for detail."],
    ["Send up to five poems in a single email.",
     "Paste poetry into the body of the email unless the work has unusual formatting "
     "requirements.",
     "Check the guidelines for each submission type to see whether to attach or paste.",
     "Star*Line is always open, so there is no window to miss."],
    "Star*Line requires First North American Serial Rights and First Electronic Rights for "
    "poetry, reviews, non-fiction and essays. There is no exclusivity period on published "
    "content and all other rights remain with the author.",
    ["Read https://sfpoetry.org/wp/starline/ to pick the right submission type.",
     "Paste poems into the email body rather than attaching.",
     "No window to wait for — submissions are always open."],
    ["star*line", "sfpa", "speculative poetry", "7 cents per word", "science fiction poetry",
     "always open", "no ai"]))

# ------------------------------------------------------- 4 The Twin Bill
NEW.append(rec(
    "the-twin-bill", "The Twin Bill", "Baseball fiction and poetry",
    "The Twin Bill: $25 a story, $10 a poem, baseball only",
    "The Twin Bill is a baseball literary magazine that pays a $25 honorarium per "
    "accepted story, $15 per accepted piece and $10 per accepted poem, for a $3 "
    "submission fee. It wants short stories of roughly 3,000 words or fewer and "
    "up to five poems per issue, all connected to the game. It runs a "
    "zero-tolerance AI policy and writers retain all rights.",
    "https://thetwinbill.com/submissions/",
    "https://thetwinbill.com/submissions/", None, "Online submission — $3 fee",
    src("The Twin Bill — Submissions (official)", "https://thetwinbill.com/submissions/"),
    intl(),
    ["fiction", "poetry"], "Baseball fiction and poetry",
    pay("USD", 10, 25, "$25 per story, $15 per piece, $10 per poem; $3 submission fee",
        "Official submissions page: there is a $25 honorarium per accepted story, a $15 "
        "honorarium per accepted piece and a $10 honorarium per accepted poem, against a $3 "
        "submission fee. Contest winners receive $100, runners-up $50 and honorable mentions $25.",
        "Not publicly stated"),
    {"min": None, "max": 3000,
     "display": "Short stories up to roughly 3,000 words; up to five poems per issue"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Writing that displays a strong personal style and a connection to the game of baseball.",
     "Short stories up to roughly 3,000 words.",
     "Up to five poems per issue — baseball from all eras, though the editors particularly want "
     "poems of a more contemporary style or subject matter."],
    ["Anything written with AI. The magazine states a zero-tolerance AI policy.",
     "Previously published pieces.",
     "Writing with no connection to baseball."],
    ["Pay the $3 submission fee.",
     "Keep stories to about 3,000 words and send at most five poems.",
     "Simultaneous submissions are fine, but tell the magazine if the piece is accepted "
     "elsewhere."],
    "Writers retain all rights to their work.",
    ["Read https://thetwinbill.com/submissions/ before sending.",
     "This is a niche market — the baseball connection is the brief, not an afterthought.",
     "No previously published work."],
    ["the twin bill", "baseball", "fiction", "poetry", "$25", "$10", "3000 words",
     "rights retained", "no ai"]))

# ------------------------------------------------------- 5 NonBinary Review
NEW.append(rec(
    "nonbinary-review", "NonBinary Review", "Prose and poetry",
    "NonBinary Review: $15 a piece, no reading fee, prose to 1,500 words",
    "NonBinary Review, published by Zoetic Press, pays $15 per accepted piece for "
    "both prose and poetry, and charges no reading fee. Prose is limited to "
    "1,500 words and poetry to 50 lines. All submissions go through DuoSuma, "
    "and no paid Duotrope account is needed.",
    "https://www.zoeticpress.com/submit",
    "https://www.zoeticpress.com/submit", None, "DuoSuma — no reading fee",
    src("NonBinary Review — Submit (official)", "https://www.zoeticpress.com/submit"),
    intl(),
    ["fiction", "poetry", "creative-nonfiction"], "Prose and poetry",
    pay("USD", 15, 15, "$15 per accepted piece, prose and poetry alike",
        "Official submit page: prose pieces are limited to 1,500 words and poetry pieces to 50 "
        "lines, and both are paid at $15 per accepted piece. Zoetic Press states plainly that it "
        "does not charge a reading fee and does pay its authors.",
        "Not publicly stated"),
    {"min": None, "max": 1500, "display": "Prose to 1,500 words; poetry to 50 lines"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Prose of 1,500 words or fewer.",
     "Poetry of 50 lines or fewer. Note that the print trim is 5 by 8 inches, so lines wider "
     "than half a standard sheet will break to a new line in print."],
    ["Prose over 1,500 words or poems over 50 lines.",
     "An expectation of a fee — there is none."],
    ["Submit through DuoSuma. No paid Duotrope account is required.",
     "Keep to the 1,500-word and 50-line ceilings.",
     "For anything other than a submission, email the press directly."],
    "Not stated on the official submit page.",
    ["Read https://www.zoeticpress.com/submit before sending.",
     "Use DuoSuma, not email, for submissions.",
     "No fee, so there is nothing to lose but the formatting."],
    ["nonbinary review", "zoetic press", "prose", "poetry", "$15", "1500 words", "50 lines",
     "no reading fee", "duosuma"]))

# ------------------------------------------------------- 6 Variety Pack
NEW.append(rec(
    "variety-pack", "Variety Pack", "Short fiction, nonfiction, poetry and visual art",
    "Variety Pack: $23 prose, $13 poetry, rights back in 60 days",
    "Variety Pack is a paying market at $23 for prose and $13 for poetry and "
    "visual art, against a $3 DuoSuma fee that carries a financial hardship "
    "waiver. Short fiction and novellettes run 1,001 to 9,000 words, nonfiction "
    "up to 5,000 words. It takes first electronic and non-exclusive archival "
    "rights, with all rights reverting 60 days after publication.",
    "https://varietypack.net/submissions-2/",
    "https://varietypack.net/submissions-2/", None,
    "DuoSuma — $3 fee with a hardship waiver",
    src("Variety Pack — Submission Guidelines (official)",
        "https://varietypack.net/submissions-2/"),
    intl(),
    ["fiction", "poetry", "creative-nonfiction"],
    "Short fiction, novellettes, nonfiction, poetry and visual art",
    pay("USD", 13, 23, "$23 for prose; $13 for poetry and visual art",
        "Official guidelines: Variety Pack states it is now a paying market at $13 for poetry "
        "and visual art and $23 for prose, paid via PayPal, Cash App or Venmo. A $3 fee applies "
        "through DuoSuma and a financial hardship waiver is available on request.",
        "After the reading period closes"),
    {"min": 1001, "max": 9000,
     "display": "Short fiction and novellettes 1,001–9,000 words; nonfiction up to 3 pieces "
                "totalling 5,000 words; up to 4 poems"},
    {"label": "Between the end of the reading period and the week before release",
     "band": "not-stated", "official": True},
    "open",
    {"date": None,
     "display": "Submissions are open from 1 September to 15 October. Only one submission per "
                "reading period; anything sent outside the window is deleted unread.",
     "recurring": True},
    "prohibited",
    ["Short fiction and novellettes between 1,001 and 9,000 words.",
     "Nonfiction: up to three pieces, a maximum of 5,000 words in total.",
     "Poetry: up to four poems in one document. Ghazals, sonnets, haiku, senryu, diptychs, "
     "triptychs, prose poems, sestinas, pantoums, traditional forms, free verse and experimental "
     "forms are all welcome.",
     "Visual art, reviews and interviews."],
    ["Any written or visual work created through generative AI. The magazine will not accept it.",
     "Submissions sent before or after the reading period is open — they are deleted unread.",
     "More than one submission per reading period.",
     "Emails outside general inquiries, submission questions, review or interview submissions "
     "and fee waivers — returned unread and automatically rejected."],
    ["Submit through DuoSuma and pay the $3 fee. Email the submissions address with "
     "\"FEE WAIVER\" in the subject line if you need the hardship waiver.",
     "Keep prose between 1,001 and 9,000 words and nonfiction to 5,000 words across three "
     "pieces.",
     "Send only one submission per reading period.",
     "Reviews and interviews are the only categories still accepted by email."],
    "Variety Pack acquires first electronic rights and non-exclusive archival rights. All other "
    "rights remain with the author, and all rights revert to the author 60 days after "
    "publication.",
    ["Read https://varietypack.net/submissions-2/ and check the reading period is open.",
     "One submission per period — do not send two.",
     "Use the waiver if the fee is a barrier; it is offered freely."],
    ["variety pack", "short fiction", "novellette", "poetry", "visual art", "$23", "$13",
     "duosuma", "rights revert 60 days", "no ai"]))

# ------------------------------------------------------- 7 Grist
NEW.append(rec(
    "grist-journal", "Grist: A Journal of the Literary Arts",
    "Poetry, fiction and nonfiction",
    "Grist: $10 a poem, 1 cent a word for prose, 7,000-word cap",
    "Grist pays $10 per poem and 1 cent per word for prose up to $50, plus a "
    "contributor copy, for a $4 submission fee that is waived for subscribers. "
    "It takes one story or one essay of up to 7,000 words, or three to five "
    "poems, and its average response time is six months.",
    "https://gristjournal.com/submit/",
    "https://gristjournal.com/submit/", None, "Submittable — $4 fee, waived for subscribers",
    src("Grist — Submit (official)", "https://gristjournal.com/submit/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"], "Poetry, fiction and nonfiction",
    pay("USD", 10, 50, "$10 per poem; 1¢ per word for prose, up to $50",
        "Official submit page: payment is $10 per poem or 1 cent per word for prose up to $50, "
        "as well as a contributor copy. The submission fee is $4 for three to five poems, for "
        "one work of fiction up to 7,000 words, or for one work of non-fiction up to 7,000 "
        "words, and is waived for subscribers. The per-word rate means the prose total depends "
        "on length.",
        "Not publicly stated"),
    {"min": None, "max": 7000, "display": "One story or essay up to 7,000 words; 3–5 poems"},
    {"label": "Average six months; query after that", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Fiction: one story of up to 7,000 words.",
     "Nonfiction: one essay of up to 7,000 words.",
     "Poetry: three to five poems.",
     "Pitches, reviews and craft essays are handled under separate guidelines on the same page."],
    ["A second submission in the same genre before the first has been answered — wait for the "
     "response.",
     "Prose over 7,000 words."],
    ["Submit through Grist's Submittable manager after reading the guidelines.",
     "Pay the $4 fee unless you are a subscriber, in which case it is waived.",
     "Wait for a response before sending another piece in the same genre.",
     "If six months pass with no response, send a query email to the editor for that genre."],
    "Not stated on the official submit page.",
    ["Read https://gristjournal.com/submit/ — pitches, reviews and craft essays have their own "
     "rules.",
     "Subscribe if you plan to submit more than once; it waives the fee.",
     "Budget for a six-month wait before querying."],
    ["grist", "journal of the literary arts", "poetry", "fiction", "nonfiction", "$10",
     "1 cent per word", "7000 words", "submittable"]))

# ------------------------------------------------------- 8 IHRAM
NEW.append(rec(
    "ihram-literary-magazine", "IHRAM Literary Magazine",
    "Human rights short stories, essays, poetry and visual art",
    "IHRAM: $50 a piece, human rights focus, AI means instant rejection",
    "IHRAM Literary Magazine, published by the Human Rights Art Movement, pays "
    "$50 per accepted written piece and $25 per accepted artist. Short stories "
    "and essays run to 2,500 words and submissions take a maximum of five poems. "
    "Every submission needs a 300 to 500 word foreword explaining its "
    "inspiration. Any content written, assisted or edited using AI results in "
    "immediate rejection.",
    "https://humanrightsartmovement.org/ihram-submissions",
    "https://humanrightsartmovement.org/ihram-submissions", None,
    "Email — name the open call in the subject line",
    src("IHRAM — Submissions (official)",
        "https://humanrightsartmovement.org/ihram-submissions"),
    {"summary": "Open to writers worldwide, with a particular interest in creative activists at "
                "risk speaking about social-justice issues in their own environments. No country "
                "restriction is stated.",
     "mode": "worldwide", "includesRegions": [], "allowsDiaspora": True, "notStated": False},
    ["fiction", "essays", "poetry", "creative-nonfiction"],
    "Human rights short stories, essays, poetry and visual art",
    pay("USD", 25, 50, "$50 per accepted written piece; $25 per accepted artist",
        "Official submissions page: IHRAM Press pays $50 per accepted written piece and $25 per "
        "accepted artist. Writers whose submissions are accepted receive $50; accepted artists "
        "receive $25.",
        "Not publicly stated"),
    {"min": None, "max": 2500,
     "display": "Short stories and essays 2,500 words or less; maximum five poems"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Short stories and essays of 2,500 words or less on urgent human rights and social-justice "
     "issues.",
     "Up to five poems per submission.",
     "Visual art — mixed media and related forms. AI-generated art is not accepted.",
     "Work from creative activists at risk, giving readers perspectives from inside the "
     "situations described."],
    ["Any content written, assisted or edited using AI — including the submitted piece, the "
     "foreword and the author bio. This results in immediate rejection.",
     "AI-assisted or AI-written translations.",
     "AI-generated art of any kind."],
    ["Email your submission and name the open call you are responding to in the subject line.",
     "Keep stories and essays to 2,500 words; send at most five poems.",
     "Include a foreword of 300 to 500 words explaining your inspiration, background "
     "information, key characters and any other insight for the reader.",
     "Include a brief third-person bio of roughly 100 words.",
     "Write the piece, the foreword and the bio without any AI assistance."],
    "Not stated on the official submissions page.",
    ["Read https://humanrightsartmovement.org/ihram-submissions and identify the open call first.",
     "The foreword is mandatory and counts toward the no-AI rule.",
     "Subject line must name the call, or the submission may not be routed correctly."],
    ["ihram", "human rights art movement", "human rights", "social justice", "$50", "$25",
     "2500 words", "foreword required", "no ai"]))

# ------------------------------------------------------- 9 Copper Nickel
NEW.append(rec(
    "copper-nickel", "Copper Nickel", "Poetry, prose, flash and translation",
    "Copper Nickel: $30 a printed page, prose to $250, no generative AI",
    "Copper Nickel pays $30 per printed page for poetry and prose, with poetry "
    "payments between $50 and $150 and prose payments between $50 and $250, and "
    "a flat $150 for translation folios. It awards two $500 Editors' Prizes per "
    "issue. Submissions are four to six poems, one story, three flash pieces or "
    "one essay, and work produced via generative AI is not accepted.",
    "https://copper-nickel.org/submit/",
    "https://copper-nickel.org/submit/", None, "Submittable",
    src("Copper Nickel — Submit (official)", "https://copper-nickel.org/submit/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction", "translation"],
    "Poetry, prose, flash and translation folios",
    pay("USD", 30, 250, "$30 per printed page; poetry $50–$150; prose $50–$250; folios $150",
        "Official submit page: poetry and prose pay $30 per printed page. Poetry payments have a "
        "minimum of $50 and a maximum of $150; prose payments have a minimum of $50 and a "
        "maximum of $250. Translation folios are a flat $150. Two $500 Editors' Prizes in poetry "
        "and prose are awarded each issue. International writers should note that payments sent "
        "overseas are subject to a 30% tax withheld at source.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Four to six poems, one story, three flash pieces, or one essay per submission"},
    {"label": "Within twelve weeks, longer in spring; wait six months before resubmitting",
     "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Four to six poems, one story, three flash pieces, or one essay at a time, in a single "
     "submission.",
     "Translation folios. If accepted, Copper Nickel asks for a contextualizing introductory "
     "essay of 800 to 1,200 words."],
    ["Work produced via generative AI. The editors state that creative writing is rooted in the "
     "unique expression of the individual mind and that generative AI is the opposite of that.",
     "A further submission within six months of receiving a response."],
    ["Submit through Submittable: four to six poems, one story, three flash pieces, or one "
     "essay, in a single submission.",
     "Withdraw full submissions through Submittable; withdraw individual poems or flash pieces "
     "by messaging which pieces to remove.",
     "Expect a response within twelve weeks, longer in spring.",
     "Wait at least six months after a response before submitting again.",
     "Submitting adds you to the contact list for occasional emails about the book prize and "
     "subscription drives."],
    "Not stated on the official submit page.",
    ["Read https://copper-nickel.org/submit/ before sending.",
     "One submission at a time, and respect the six-month gap after a response.",
     "International writers should factor in the 30% withholding."],
    ["copper nickel", "poetry", "prose", "flash", "translation", "$30 per page", "$250",
     "no generative ai", "submittable"]))

# ------------------------------------------------------- 10 Peach
NEW.append(rec(
    "peach-gcsu", "Peach", "Fiction, nonfiction and poetry",
    "Peach: $10 a page for prose, $50 a poem, no AI in any amount",
    "Peach, the literary journal of Georgia College, pays $10 per printed page "
    "for prose capped at $150 and $50 per poem for up to four poems, against a "
    "$3 general submission fee. It takes one piece of fiction or nonfiction of "
    "up to 5,000 words and aims to respond within six weeks. It does not "
    "consider work produced in any amount by AI.",
    "https://peach.gcsu.edu/submission-guidelines/",
    "https://peach.gcsu.edu/submission-guidelines/", None,
    "Online submission — $3 general fee",
    src("Peach — Submission Guidelines (official)",
        "https://peach.gcsu.edu/submission-guidelines/"),
    {"summary": "No stated country restriction on the submission guidelines page. Peach is the "
                "literary journal of Georgia College in the United States.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction", "creative-nonfiction", "poetry"], "Fiction, nonfiction and poetry",
    pay("USD", 10, 150, "Prose $10 per printed page capped at $150; poetry $50 per poem",
        "Official submission guidelines: Peach offers a one-time honorarium on publication of "
        "$10 per printed page for prose, capped at $150 total for work up to 5,000 words, and "
        "$50 per poem for a maximum of four poems. A $3 general submission fee applies. The "
        "Susan Atefat Editor's Prize carries a separate $20 entry fee and a $4,000 award.",
        "On publication"),
    {"min": None, "max": 5000,
     "display": "One piece of fiction or nonfiction up to 5,000 words; maximum four poems"},
    {"label": "Aimed at within six weeks", "band": "1-3-months", "official": True},
    "open", None, "prohibited",
    ["One piece of fiction or nonfiction of up to 5,000 words.",
     "Poetry, up to four poems."],
    ["Work produced in any amount by AI. Peach states it does not consider work produced by AI "
     "and does not accept submissions created by artificial intelligence.",
     "Prose over 5,000 words or more than four poems."],
    ["Pay the $3 general submission fee.",
     "Send one prose piece of up to 5,000 words, or up to four poems.",
     "Expect a response within six weeks."],
    "Not stated on the official submission guidelines page.",
    ["Read https://peach.gcsu.edu/submission-guidelines/ — the page is dated, so check the "
     "version before sending.",
     "Keep to one prose piece or four poems.",
     "No AI assistance of any kind, including drafting."],
    ["peach", "georgia college", "fiction", "nonfiction", "poetry", "$10 per page", "$50",
     "5000 words", "no ai"]))

# ------------------------------------------------------- 11 Bellevue Literary Review
NEW.append(rec(
    "bellevue-literary-review", "Bellevue Literary Review",
    "Fiction, nonfiction and poetry on health and healing",
    "Bellevue Literary Review: $150 prose, $75 poetry, 5,000 words",
    "Bellevue Literary Review pays published authors $150 for prose and $75 for "
    "poetry, against a $5 general submission fee that is waived for current "
    "subscribers. Fiction and nonfiction run to 5,000 words, though most "
    "published prose is 2,000 to 4,000, and poets may send up to three poems of "
    "any length. It acquires First North American rights, with all other rights "
    "reverting after publication.",
    "https://blreview.org/submit/",
    "https://blreview.org/submit/", None,
    "Submittable — $5 fee, waived for subscribers",
    src("Bellevue Literary Review — Submit (official)", "https://blreview.org/submit/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Fiction, nonfiction and poetry on health, healing and the human body",
    pay("USD", 75, 150, "$150 for prose; $75 for poetry",
        "Official submit page: BLR pays published authors $150 for prose and $75 for poetry. "
        "There is a $5 fee per general submission, waived for current subscribers. The BLR "
        "Prizes carry a separate $20 entry fee per submission.",
        "On publication"),
    {"min": None, "max": 5000,
     "display": "Fiction and nonfiction up to 5,000 words (most published prose is 2,000–4,000); "
                "up to three poems of any length"},
    {"label": "Not stated; inquire after five months", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Fiction and nonfiction up to 5,000 words, though most published prose falls between 2,000 "
     "and 4,000 words.",
     "Up to three poems as one submission. Poems may be of any length, though shorter poems let "
     "BLR include more poets."],
    ["Work created or materially shaped by generative artificial intelligence tools. By "
     "submitting, authors affirm the work is their own original writing, has not been previously "
     "published, and was not created or materially shaped by generative AI.",
     "Previously published work.",
     "Submissions by email or hard copy mail, except where accessibility accommodations require "
     "it."],
    ["Submit electronically through Submittable; email and hard copy are not accepted except for "
     "accessibility accommodations.",
     "Pay the $5 general fee unless you are a current subscriber.",
     "Keep prose to 5,000 words and send at most three poems.",
     "If five months pass with no word, email to ask about the submission."],
    "BLR acquires First North American rights and the right to reprint in anthologies and "
    "online. After publication all other rights revert to the author, and the work may be "
    "reprinted as long as BLR is acknowledged.",
    ["Read https://blreview.org/submit/ before sending.",
     "Subscribe if you submit often — it waives the fee.",
     "Only query after five months."],
    ["bellevue literary review", "blr", "health", "medicine", "fiction", "nonfiction", "poetry",
     "$150", "$75", "5000 words", "no generative ai"]))

# ------------------------------------------------------- 12 Lady Churchill's Rosebud Wristlet
NEW.append(rec(
    "lady-churchills-rosebud-wristlet", "Lady Churchill's Rosebud Wristlet",
    "Fantasy and literary fiction",
    "Rosebud Wristlet: 3 cents a word, $25 minimum, no AI",
    "Lady Churchill's Rosebud Wristlet, published by Small Beer Press, pays 3 "
    "cents a word for fiction with a $25 minimum. It buys first North American "
    "serial rights, exclusive electronic rights for 90 days and a non-exclusive "
    "anthology right. It does not accept or publish anything written or assisted "
    "by AI, and it will not take gore, sword and sorcery, or pornography.",
    "https://smallbeerpress.com/about/submission-guidelines/",
    "https://smallbeerpress.com/about/submission-guidelines/", None,
    "See guidelines — international submissions answered by email",
    src("Small Beer Press — Submission Guidelines (official)",
        "https://smallbeerpress.com/about/submission-guidelines/"),
    intl(),
    ["fiction"], "Fantasy and literary fiction",
    pay("USD", 25, 25, "US$0.03 per word, $25 minimum",
        "Official submission guidelines: fiction pays US$0.03 per word with a $25 minimum. The "
        "minimum is recorded as the floor; the actual amount scales with length at three cents a "
        "word.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No word limit stated on the guidelines page; standard manuscript format"},
    {"label": "Not stated; the press replies to queries after six months",
     "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Fiction that has been through at least one round of revision — the press recommends this "
     "for both parties' sanity.",
     "Work in standard manuscript format: 12 point text in a font of your choice, "
     "double-spaced, numbered pages."],
    ["Anything written, assisted or otherwise produced by AI such as ChatGPT. Small Beer Press "
     "does not accept or publish it.",
     "Gore, sword and sorcery, or pornography. The press says there are places for all of them "
     "and this is not one of them."],
    ["Follow standard manuscript format: 12 point text, double-spaced, numbered pages.",
     "Revise at least once before sending.",
     "International submissions are answered by email.",
     "If six months pass, contact the press and they will try to reply with a decision."],
    "Small Beer Press buys first North American serial rights, exclusive electronic rights for "
    "90 days, and a non-exclusive anthology right. Reprints are only very occasionally "
    "solicited.",
    ["Read https://smallbeerpress.com/about/submission-guidelines/ before sending.",
     "Format properly — the press is explicit about 12 point, double-spaced, numbered pages.",
     "Do not send gore or sword and sorcery; it is out of scope, not a matter of taste."],
    ["lady churchill's rosebud wristlet", "small beer press", "fantasy", "fiction",
     "3 cents per word", "$25 minimum", "no ai", "90 days electronic"]))


BASE = {
    "litmosphere-charlotte-lit": ("", "International"),
    "ninth-letter": ("", "International"),
    "star-line-sfpa": ("", "International"),
    "the-twin-bill": ("", "International"),
    "nonbinary-review": ("", "International"),
    "variety-pack": ("", "International"),
    "grist-journal": ("", "International"),
    "ihram-literary-magazine": ("", "International"),
    "copper-nickel": ("", "International"),
    "peach-gcsu": ("US", "United States"),
    "bellevue-literary-review": ("", "International"),
    "lady-churchills-rosebud-wristlet": ("", "International"),
}


def main():
    data = json.loads(OPPS.read_text(encoding="utf-8"))
    opps = data["opportunities"]
    existing = {o["slug"] for o in opps}
    dupes = [r["slug"] for r in NEW if r["slug"] in existing]
    if dupes:
        sys.exit(f"ERROR: slug collision: {dupes}")
    seen = set()
    for r in NEW:
        if r["slug"] in seen:
            sys.exit(f"ERROR: duplicate slug inside batch: {r['slug']}")
        seen.add(r["slug"])
        p = r["pay"]
        if p["amountMin"] == 0 or p["amountMax"] == 0:
            sys.exit(f"ERROR: {r['slug']} has a zero pay amount")
        if p["amountMin"] is not None and p["amountMax"] is not None \
                and p["amountMin"] > p["amountMax"]:
            sys.exit(f"ERROR: {r['slug']} pay range inverted")
        for k in ("officialUrl", "excerpt", "seoTitle", "howToSubmit", "whatTheyWant"):
            if not r.get(k):
                sys.exit(f"ERROR: {r['slug']} missing {k}")

    opps.extend(NEW)
    data["opportunities"] = opps
    data["updatedAt"] = V
    OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if PUBC.exists():
        pc = json.loads(PUBC.read_text(encoding="utf-8"))
        for r in NEW:
            base, label = BASE[r["slug"]]
            pc[r["slug"]] = {"base": base, "label": label}
        PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Added {len(NEW)} verified records. Total opportunities: {len(opps)}")


# ---------------------------------------------------------------------------
# Held back from batch 4, and why:
#
#   skyislandjournal.com     $4.99 fee and a clear AI position, but states it
#       cannot provide monetary payment. Recordable, just not a paying market -
#       held for a later unpaid-market batch.
#   themetaworker.com        AI prohibited, copyright retained, 3-6 month
#       response, but no pay figure anywhere on the page.
#   globalmajoritypress.org  (The B'K) pays $10, but only to racially or
#       ethnically marginalised, gender-variant or disabled submitters. That is
#       an eligibility condition BRYME would have to record accurately, and it
#       needs a fuller read than this batch allowed.
#   pitheadchapel.com        Explicitly unpaid; under 4,000 words; no AI.
#   haiku shack / rawhead    Fee-and-prize models with no straightforward rate.
#   storyunlikely.com        Membership and contest model, $4,000 prize pool,
#       99-day response. Not a standard submissions market.
#   hootreview.com           Payment model described in a comment thread rather
#       than in the guidelines. Too unclear to record.
#   calyxpress.org, nereview.com, blreview.org (prizes), ubwali.com,
#   bloodtreeliterature.com, braidedway.org
#       Real markets with usable data; queued for batch 5 rather than rushed.
#
# The 450 usable pages are all retained under research/batch4/, so batches 5
# and beyond do not need to re-crawl pw.org or re-fetch anything.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
