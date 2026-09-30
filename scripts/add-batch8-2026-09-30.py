#!/usr/bin/env python3
"""Add verified writing-market batch 8 (2026-09-30).

Ten NEW markets, read from the batch-4 backlog. No crawling.

Every figure was read off the publication's own guidelines page on 2026-09-30.
Raw page text is retained under research/batch4/<slug>.txt.

THIS BATCH IS MOSTLY UNPAID, and that is recorded rather than papered over.
Only Wallstrait publishes a firm rate. Tusculum Review pays in copies. Six
publish no rate at all. The point of including them is that a writer filtering
for paying work needs these marked honestly as much as they need the paying ones
marked with a figure.

Two AI policies here are NOT simple prohibitions, and are the reason this batch
was worth reading carefully:

  teach-write       AI may be used for editing or research, but not for
                    generating creative content - and if AI assisted your
                    process you must disclose how in your cover letter.
                    Recorded as disclosure-required.

  the-pasticheur    Recognises AI as part of contemporary creative practice,
                    says AI may be used as a form of conversation, and that an
                    author may accept, reject, alter or respond to suggestions
                    from an editor, another person, or an AI system.
                    Recorded as limited, not prohibited.

Flattening either to "prohibited" would have been wrong, and flattening them to
"not-stated" would have thrown away a real policy.

Base country is verifiable for one: Tusculum Review at ttr.tusculum.edu, a US
.edu domain. The rest record "International" rather than a guess.
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


def intl(summary="No stated country restriction on the guidelines page."):
    return {"summary": summary, "mode": "not-stated", "includesRegions": [],
            "allowsDiaspora": True, "notStated": True}


NEW = []

# ------------------------------------------- 1 Wallstrait
NEW.append(rec(
    "wallstrait", "Wallstrait", "Fiction and nonfiction",
    "Wallstrait: $100 on publication, one of the fastest responses",
    "Wallstrait pays $100 upon publication, by PayPal only, against a $3 "
    "submission fee that is waived between 1 and 8 October. It prefers work of "
    "500 to 3,000 words with a 5,000-word maximum, aims to be one of the "
    "fastest-responding literary journals in the industry, and reverts all "
    "other rights to the author on publication.",
    "https://www.wallstrait.com/submissions",
    "https://www.wallstrait.com/submissions", None,
    "Online submission — $3 fee, waived 1–8 October",
    src("Wallstrait — Submissions (official)", "https://www.wallstrait.com/submissions"),
    intl(),
    ["fiction", "creative-nonfiction"], "Fiction and nonfiction",
    pay("USD", 100, 100, "$100 upon publication, PayPal only",
        "Official submissions page: Wallstrait pays $100 upon publication, PayPal only. A $3 "
        "submission fee applies, with no fee between 1 and 8 October.",
        "Upon publication"),
    {"min": 500, "max": 5000,
     "display": "500–3,000 words preferred, 5,000 words maximum"},
    {"label": "Very quickly — the journal aims to be one of the fastest-responding in the "
               "industry", "band": "not-stated", "official": True},
    "open", None, "not-stated",
    ["Fiction and nonfiction, preferably 500 to 3,000 words.",
     "Work up to 5,000 words."],
    ["Prose over 5,000 words."],
    ["Pay the $3 fee, or submit between 1 and 8 October when there is none.",
     "Keep work between 500 and 3,000 words if you can.",
     "Have a PayPal account — it is the only payment route.",
     "If they pass, you are welcome to submit again quickly."],
    "All other rights revert back to the author upon publication.",
    ["Read https://www.wallstrait.com/submissions before sending.",
     "Submit in the first week of October to avoid the fee.",
     "Fast responses mean fast turnaround on resubmission too."],
    ["wallstrait", "fiction", "nonfiction", "$100", "paypal", "500-3000 words",
     "fast response", "rights revert"]))

# ------------------------------------------- 2 Tusculum Review
NEW.append(rec(
    "tusculum-review", "Tusculum Review", "Prose and poetry",
    "Tusculum Review: paid in copies, prose under 7,000 words",
    "Tusculum Review would pay in money but says its current budget only allows "
    "payment in two copies. It takes prose under 7,000 words — about 24 "
    "double-spaced pages — and poetry of five pages or less, reads year round, "
    "and does not publish AI-generated or AI-assisted pieces. Rights revert to "
    "the individual authors after publication.",
    "https://ttr.tusculum.edu/submit-5/",
    "https://ttr.tusculum.edu/submit-5/", None, "Submittable — cover letter required",
    src("Tusculum Review — Submit (official)", "https://ttr.tusculum.edu/submit-5/"),
    {"summary": "Open internationally. No country restriction is stated on the submissions "
                "page. Tusculum Review is the journal of Tusculum University in the United "
                "States.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction", "creative-nonfiction", "poetry"], "Prose and poetry",
    pay(None, None, None, "Paid in two copies — the journal states it cannot pay money",
        "Official submit page: Tusculum Review states it would love to pay with money, but its "
        "current budget only allows for payment in copies (2). BRYME records no monetary figure "
        "because there is none. The consideration is two copies of the issue.",
        "Not applicable — paid in copies"),
    {"min": None, "max": 7000,
     "display": "Prose under 7,000 words (about 24 double-spaced pages); poetry five pages or "
                "less"},
    {"label": "Not stated; reads year round", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Prose under 7,000 words, roughly 24 double-spaced pages.",
     "Poetry of five pages or less."],
    ["AI-generated or AI-assisted pieces. Tusculum Review considers original writing by humans."],
    ["Submit through Submittable.",
     "Include a cover letter with your name, address, phone number, email address and the "
     "titles of your submissions.",
     "Keep prose under 7,000 words and poetry to five pages.",
     "Simultaneous submissions are accepted, but alert the journal through Submittable if the "
     "work is accepted elsewhere.",
     "It reads year round, so there is no window to wait for."],
    "Except for second printings of the journal due to demand, all rights to material in the "
    "Tusculum Review and its chapbooks revert to the individual authors and artists after "
    "publication.",
    ["Read https://ttr.tusculum.edu/submit-5/ before sending.",
     "Paid in copies, not cash — decide if that suits you before submitting.",
     "The cover letter is mandatory, not optional."],
    ["tusculum review", "tusculum university", "prose", "poetry", "paid in copies",
     "7000 words", "year round", "no ai"]))

# ------------------------------------------- 3 Oyster River Pages
NEW.append(rec(
    "oyster-river-pages", "Oyster River Pages",
    "Fiction, creative nonfiction and poetry",
    "Oyster River Pages: prose to 7,500 words, no AI in part or full",
    "Oyster River Pages takes one story of up to 7,500 words and one creative "
    "nonfiction essay of no more than 6,000 words, plus up to three poems for "
    "its Emerging Voices Poetry category. It will not publish anything created "
    "in part or in full with generative AI, and reserves the right to remove "
    "such work and rescind publication if it is found later. All rights revert "
    "to the author or artist.",
    "https://www.oysterriverpages.com/submit",
    "https://www.oysterriverpages.com/submit", None, "Online submission — 60-word bio required",
    src("Oyster River Pages — Submit (official)", "https://www.oysterriverpages.com/submit"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Fiction, creative nonfiction and poetry",
    pay(None, None, None, "Not stated on the public submit page",
        "The public submit page sets length limits, the AI policy and the rights position but "
        "publishes no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": 7500,
     "display": "Fiction up to 7,500 words; creative nonfiction up to 6,000 words; up to 3 "
                "poems in one document of no more than 10 pages"},
    {"label": "Six months, after which a decline is assumed", "band": "3-plus-months",
     "official": True},
    "open", None, "prohibited",
    ["Fiction: one story of up to 7,500 words.",
     "Creative nonfiction: one essay of no more than 6,000 words, in Word Doc or PDF format.",
     "Emerging Voices Poetry: up to three poems in one document, no longer than 10 pages total."],
    ["Work created in part or in full, or in collaboration with, generative artificial "
     "intelligence. If such work is published and later found, Oyster River Pages reserves the "
     "right to remove it and rescind publication."],
    ["Put the exact word count, your full name or chosen pen name, and your preferred email at "
     "the top of the first page.",
     "Include a 60-word bio, and a photo if you want one.",
     "Read recent issues first to get a sense of the preferences.",
     "If six months pass with no reply, treat it as a decline."],
    "Oyster River Pages requests first serial rights, after which all rights revert to the "
    "author or artist.",
    ["Read https://www.oysterriverpages.com/submit and skim recent issues before sending.",
     "Word count goes on page one — it is a stated requirement.",
     "Six months is the outer limit; plan around it."],
    ["oyster river pages", "fiction", "creative nonfiction", "poetry", "emerging voices",
     "7500 words", "6000 words", "no generative ai"]))

# ------------------------------------------- 4 Teach. Write.
NEW.append(rec(
    "teach-write", "Teach. Write.: A Literary Journal for Writing Teachers",
    "Short fiction and creative nonfiction by and for writing teachers",
    "Teach. Write.: AI for editing allowed if disclosed",
    "Teach. Write. is a literary journal for writing teachers, run as a "
    "one-woman operation on a retirement income. Its editor cannot pay much but "
    "believes writers should be paid. Its AI policy is unusually precise: AI "
    "tools may be used for editing or research but not for generating creative "
    "content, and if AI assisted your process you must disclose how in your "
    "cover letter.",
    "https://teachwritejournal.com/submission-guidelines/",
    "https://teachwritejournal.com/submission-guidelines/", "teachwritejournal@gmail.com",
    "Email submission",
    src("Teach. Write. — Submission Guidelines (official)",
        "https://teachwritejournal.com/submission-guidelines/"),
    intl(),
    ["fiction", "creative-nonfiction"],
    "Short fiction and creative nonfiction by and for writing teachers",
    pay(None, None, None, "Cannot pay much; donations of honorariums support the journal",
        "Official submission guidelines: the editor states this is a one-woman show and she is "
        "now living on a retirement income, so she cannot pay much, but believes writers should "
        "be paid for their work. She cannot provide any alternate form of payment, and any "
        "donations of honorariums go to support Teach. Write. BRYME records no figure because "
        "none is published.",
        "Not publicly stated"),
    {"min": 1000, "max": 3000,
     "display": "Short fiction 1,000–3,000 words; creative nonfiction up to 2,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "disclosure-required",
    ["Short fiction of 1,000 to 3,000 words, any theme or genre.",
     "Creative nonfiction of up to 2,000 words, on the same exceptions.",
     "Work by and for writing teachers — that is the journal's remit."],
    ["AI used to generate creative content. AI tools may be used for editing or research only.",
     "Undisclosed AI assistance. If AI assisted your process you must say how."],
    ["Email your submission to teachwritejournal@gmail.com.",
     "Keep fiction to 1,000–3,000 words and nonfiction to 2,000.",
     "If AI assisted your process in any permitted way, disclose how in your cover letter — "
     "this is a condition, not a courtesy.",
     "Writing teachers are the intended contributors."],
    "Copyright remains with the author.",
    ["Read https://teachwritejournal.com/submission-guidelines/ before sending.",
     "Disclose any AI assistance — the policy is explicit that it is required.",
     "This is a low-pay market run by one person on a retirement income; submit accordingly."],
    ["teach write", "writing teachers", "short fiction", "creative nonfiction",
     "1000-3000 words", "ai disclosure required", "copyright retained"]))

# ------------------------------------------- 5 The Pasticheur
NEW.append(rec(
    "the-pasticheur", "The Pasticheur",
    "Short fiction, creative nonfiction and film writing",
    "The Pasticheur: AI treated as a tool, authors keep copyright",
    "The Pasticheur takes one piece of short fiction or creative nonfiction of "
    "up to 3,000 words, and film writing with a 150 to 200 word synopsis plus "
    "one still. Authors retain full copyright, and the magazine asks only for "
    "first publication rights and the right to archive permanently. Its AI "
    "position is permissive rather than prohibitive: it recognises AI as part of "
    "contemporary creative practice and that an author may accept, reject, alter "
    "or respond to suggestions from an editor, another person, or an AI system.",
    "https://the-pasticheur.com/submit-your-work-1",
    "https://the-pasticheur.com/submit-your-work-1", "editor@the-pasticheur.com",
    "Email with a cover letter addressed to the editors",
    src("The Pasticheur — Submit Your Work (official)",
        "https://the-pasticheur.com/submit-your-work-1"),
    intl(),
    ["fiction", "creative-nonfiction", "reviews"],
    "Short fiction, creative nonfiction and film writing",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out formats, the rights position and the AI position "
        "but publishes no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": 3000,
     "display": "Short fiction or creative nonfiction: 1 piece up to 3,000 words; film writing: "
                "synopsis of 150–200 words plus one still"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "limited",
    ["Short fiction or creative nonfiction: one piece of up to 3,000 words.",
     "Film writing: a brief synopsis of 150 to 200 words and one film still or promotional "
     "image.",
     "A cover letter addressed to the editors.",
     "Work responding to a special call, indicated clearly in the email subject line or body."],
    ["Submissions without a cover letter addressed to the editors."],
    ["Email your submission with a cover letter addressed to the editors.",
     "Keep fiction and nonfiction to one piece of up to 3,000 words.",
     "For film writing, include the 150–200 word synopsis and one still.",
     "If your work responds to a special call, say so in the subject line or body.",
     "For any adapted or source-based work, include proof of copyright permission and the right "
     "to publish both versions."],
    "Authors retain full copyright. The Pasticheur requests only first publication rights and "
    "the right to archive the work permanently.",
    ["Read the 'On Authorship and the Use of AI' section at "
     "https://the-pasticheur.com/submit-your-work-1 before sending.",
     "This is one of the few markets that treats AI as a legitimate tool rather than banning it "
     "— but authorship still rests with you.",
     "The cover letter is required."],
    ["the pasticheur", "short fiction", "creative nonfiction", "film writing", "3000 words",
     "authors retain copyright", "ai permitted", "cover letter"]))

# ------------------------------------------- 6 Long River Review
NEW.append(rec(
    "long-river-review", "Long River Review",
    "Poetry, prose, art and literary criticism",
    "Long River Review: unpaid, and no AI even for grammar",
    "Long River Review states it is not in a position to offer payment to its "
    "writers. It takes five poems or one prose piece under 4,000 words, and is "
    "now seeking literary criticism. Its AI policy goes further than most: it "
    "will not publish writing or art featuring AI-generated sections, and "
    "because it standardises grammar during copyediting it prohibits AI grammar "
    "checking too.",
    "https://longriverreview.com/submit-2/",
    "https://longriverreview.com/submit-2/", None, "Online submission",
    src("Long River Review — Submit (official)", "https://longriverreview.com/submit-2/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction", "essays"],
    "Poetry, prose, art and literary criticism",
    pay(None, None, None, "Unpaid — the review states it cannot offer payment",
        "Official submit page: Long River Review states that unfortunately it is not in the "
        "position to offer payment to its writers. BRYME records no figure because there is "
        "none.",
        "Not applicable — unpaid"),
    {"min": None, "max": 4000, "display": "5 poems, or 1 prose piece under 4,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Five poems, or one prose piece under 4,000 words.",
     "Literary criticism that responds to a recent text, or that recontextualises older "
     "literature in modern literary discourse — a category the review is actively seeking."],
    ["Any submission of writing or art featuring sections that are, or are entirely, "
     "AI-generated text or visual content.",
     "AI tools used for grammar checking. Because Long River Review standardises grammar during "
     "copyediting, this is prohibited as well — a stricter position than most journals take."],
    ["Send five poems or one prose piece under 4,000 words.",
     "Do not run your work through an AI grammar checker — it is explicitly against the rules "
     "here.",
     "Literary criticism is being actively sought, so pitch it."],
    "Long River Review takes first North American rights, to be the first publication in North "
    "America to publish the work, after which the rights revert back to the author.",
    ["Read https://longriverreview.com/submit-2/ before sending.",
     "Unpaid — submit for the credit.",
     "The no-AI-grammar-check rule is unusual; proofread by hand."],
    ["long river review", "poetry", "prose", "literary criticism", "unpaid", "4000 words",
     "no ai grammar check", "rights revert"]))

# ------------------------------------------- 7 KUDU
NEW.append(rec(
    "kudu", "KUDU", "Poetry",
    "KUDU: unpaid, 1–3 poems of 40 lines, no AI",
    "KUDU states plainly that it is not a paying market. It takes one to three "
    "poems of no more than 40 lines each, sent attached to an email in a single "
    "document with each poem on a separate page. It does not accept work "
    "generated by AI, contributors retain copyright on publication, and no "
    "notification of rejection is sent.",
    "https://kudujournal.wordpress.com/submissions/",
    "https://kudujournal.wordpress.com/submissions/", None,
    "Email — poems in one document, each on its own page",
    src("KUDU — Submissions (official)", "https://kudujournal.wordpress.com/submissions/"),
    intl(),
    ["poetry"], "Poetry",
    pay(None, None, None, "Unpaid — KUDU states it is not a paying market",
        "Official submissions page: KUDU states that it is not a paying market. BRYME records no "
        "figure because there is none.",
        "Not applicable — unpaid"),
    {"min": None, "max": None, "display": "1–3 poems, 40 lines maximum per poem"},
    {"label": "Not stated; no rejection notifications are sent", "band": "not-stated",
     "official": True},
    "open", None, "prohibited",
    ["One to three poems of no more than 40 lines each.",
     "Each poem on a separate page, in a single document attached to your email."],
    ["Work generated by AI.",
     "Poems over 40 lines, or more than three per submission."],
    ["Send the poems attached to your email in a single document, each poem on a separate page.",
     "Keep each poem to 40 lines and send at most three.",
     "Do not expect a rejection notice — silence is the answer.",
     "Check the interviews at Six Questions For and New Pages for a summary of what KUDU wants."],
    "Upon publication, contributors retain the copyright of their work.",
    ["Read https://kudujournal.wordpress.com/submissions/ and the linked interviews before "
     "sending.",
     "Unpaid, and no rejection emails — set your expectations accordingly.",
     "Format matters here: one document, one poem per page."],
    ["kudu", "poetry", "unpaid", "1-3 poems", "40 lines", "no rejection notice",
     "copyright retained", "no ai"]))

# ------------------------------------------- 8 Litbop
NEW.append(rec(
    "litbop", "Litbop: Art and Literature in the Groove",
    "Poetry, prose and visual art with a musical bent",
    "Litbop: unpaid, no fee, up to 5 poems",
    "Litbop states there is currently no money to pay contributors, and charges "
    "no submission fee, though tips toward production costs are accepted through "
    "DuoSuma. It takes up to five poems with a maximum of ten pages in one "
    "document, and is candid that its response time is currently up in the air.",
    "https://www.thrillingtales.com/litbop/",
    "https://www.thrillingtales.com/litbop/", None,
    "DuoSuma — no fee, tips optional",
    src("Litbop — Submissions (official)", "https://www.thrillingtales.com/litbop/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, prose and visual art with a musical bent",
    pay(None, None, None, "Unpaid — there is currently no money to pay contributors",
        "Official submissions page: Litbop states that there is currently no money to pay "
        "contributors, and that there is no fee to submit, though tips to help with production "
        "costs are gratefully accepted through DuoSuma. BRYME records no figure because there is "
        "none.",
        "Not applicable — unpaid"),
    {"min": None, "max": None,
     "display": "Up to 5 poems with a maximum of 10 pages in one document"},
    {"label": "Currently up in the air, per the journal's own wording", "band": "not-stated",
     "official": True},
    "open",
    {"date": None,
     "display": "Litbop runs a reading period each year, announced on its submissions page.",
     "recurring": True},
    "not-stated",
    ["Up to five poems with a maximum of ten pages, in one document.",
     "Art and literature in the groove — the musical connection is the journal's theme."],
    ["An expectation of payment, or of a predictable response time. Both are stated to be "
     "unavailable at present."],
    ["Submit through DuoSuma; there is no fee.",
     "Keep poetry to five poems and ten pages in a single document.",
     "Check the reading period before sending.",
     "Tips are optional and go to production costs."],
    "Not stated on the official submissions page.",
    ["Read https://www.thrillingtales.com/litbop/ and check the current reading period.",
     "Unpaid with an uncertain response time — submit for the fit, not the turnaround.",
     "No fee, so there is nothing to lose."],
    ["litbop", "art and literature in the groove", "poetry", "music", "unpaid", "no fee",
     "5 poems", "duosuma"]))

# ------------------------------------------- 9 Unwashed
NEW.append(rec(
    "unwashed", "Unwashed",
    "Fiction, flash, experimental writing, creative nonfiction and poetry",
    "Unwashed: 1,500-word prose, no AI or LLM in part",
    "Unwashed takes creative writing including fiction, flash fiction, "
    "experimental fiction and creative nonfiction to a 1,500-word maximum, and "
    "poetry to 1,000 words, all previously unpublished with no restrictions as "
    "to type, form or content. No AI or LLM tools may be used wholly or in part "
    "in the creation of any submission.",
    "https://unwashedmke.com/",
    "https://unwashedmke.com/", None, "Email submission",
    src("Unwashed — official site", "https://unwashedmke.com/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Fiction, flash, experimental writing, creative nonfiction and poetry",
    pay(None, None, None, "Not stated on the public page",
        "The public page sets out the word limits, the originality requirement and the AI policy "
        "but publishes no payment rate for contributors. The prices shown on the page are for "
        "buying copies of the magazine, not payment to writers, and BRYME does not record them "
        "as such.",
        "Not publicly stated"),
    {"min": None, "max": 1500,
     "display": "Prose 1,500 words maximum; poetry 1,000 words maximum"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Fiction, flash fiction, experimental fiction and creative nonfiction to 1,500 words, "
     "previously unpublished.",
     "Poetry to 1,000 words, previously unpublished.",
     "No restrictions as to type, form or content — the magazine is explicit about that, and "
     "says it wants to hear from writers with the courage to put their work out there."],
    ["Any use of AI or LLM tools, wholly or in part, in the creation of a submission.",
     "Previously published work."],
    ["Email your submission to the address on the site.",
     "Keep prose to 1,500 words and poetry to 1,000.",
     "Send unpublished work only.",
     "Write without AI or LLM assistance of any degree."],
    "Not stated on the public page.",
    ["Read https://unwashedmke.com/ before sending.",
     "Form and content are genuinely open here — that is the brief.",
     "Note that the prices on the site are copy prices, not contributor payment."],
    ["unwashed", "fiction", "flash fiction", "experimental", "creative nonfiction", "poetry",
     "1500 words", "no restrictions", "no ai"]))

# ------------------------------------------- 10 Men Matters Online Journal
NEW.append(rec(
    "men-matters-online-journal", "Men Matters Online Journal",
    "Fiction, creative nonfiction, poetry and academic work on men and masculinities",
    "Men Matters Online Journal: 5,000 words, 2 weeks to 3 months",
    "Men Matters Online Journal takes a single work of fiction or creative "
    "nonfiction to a maximum of 5,000 words, and asks for a brief abstract of "
    "150 to 200 words with academic submissions. It does not accept AI-generated "
    "submissions and its response period runs from two weeks to three months.",
    "https://menmattersonlinejournal.com/call-for-submissions/",
    "https://menmattersonlinejournal.com/call-for-submissions/", None,
    "See call for submissions",
    src("Men Matters Online Journal — Call for Submissions (official)",
        "https://menmattersonlinejournal.com/call-for-submissions/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Fiction, creative nonfiction, poetry and academic work on men and masculinities",
    pay(None, None, None, "Not stated on the public call for submissions",
        "The public call for submissions sets out formats, the abstract requirement and the AI "
        "policy but publishes no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "A single work of fiction or creative nonfiction, maximum 5,000 words"},
    {"label": "Between two weeks and three months", "band": "1-3-months", "official": True},
    "open", None, "prohibited",
    ["A single work of fiction or creative nonfiction to a maximum of 5,000 words.",
     "Poetry.",
     "Academic work, with a brief abstract of 150 to 200 words."],
    ["AI-generated submissions."],
    ["Read the call for submissions and send a single work to 5,000 words.",
     "Include a 150 to 200 word abstract for academic submissions.",
     "Expect an answer somewhere between two weeks and three months."],
    "Not stated on the public call for submissions.",
    ["Read https://menmattersonlinejournal.com/call-for-submissions/ before sending.",
     "The abstract is required for academic work.",
     "The response window is wide — two weeks to three months."],
    ["men matters online journal", "men", "masculinities", "fiction", "creative nonfiction",
     "5000 words", "abstract required", "no ai"]))


BASE = {
    "wallstrait": ("", "International"),
    "tusculum-review": ("US", "United States"),
    "oyster-river-pages": ("", "International"),
    "teach-write": ("", "International"),
    "the-pasticheur": ("", "International"),
    "long-river-review": ("", "International"),
    "kudu": ("", "International"),
    "litbop": ("", "International"),
    "unwashed": ("", "International"),
    "men-matters-online-journal": ("", "International"),
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
# Read this pass but not added:
#
#   dogwoodliterary.wordpress.com   A prize, not a submissions market. Its $1,000
#       awards go to the best essay, story and poem in an annual contest, and the
#       reading period ran 1 July to 5 September. Batch 2 rejected American Short
#       Fiction on the same grounds and this follows that precedent.
#   antiphonypress.com              False positive. The URL resolved to an
#       Indonesian e-commerce product page for a refrigerator. Not a magazine.
#   gulfcoastmag.org/submit/        Already added in batch 3 as slug gulf-coast.
#       The extractor missed it because pw.org lists the long form "Gulf Coast: A
#       Journal of Literature and Fine Arts" while the database records
#       "Gulf Coast" - name-normalised matching needs to handle subtitles.
#
# 395 usable guidelines pages remain unread. No further crawling required.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
