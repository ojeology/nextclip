#!/usr/bin/env python3
"""Add the verified UK publication batch (2026-09-06).

Every field below was read off the publication's own live guidelines page on
2026-09-06 and saved to /home/user/research/uk/*.txt. Nothing is inferred from
an aggregator or directory. Publications verified as NOT paying (Acumen,
The Learned Pig, Elsewhere) were deliberately excluded, not listed with a
guessed rate. Publications that pay but do not state a figure carry
pay.amountMin = None so they resolve to null, never 0.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-06"


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


NEW = []

# ---------------------------------------------------------------- 1 Pellicle
NEW.append(rec(
    "pellicle", "Pellicle", "Drinks, pubs and food features",
    "Pellicle pitching: £375–£675 per commissioned feature",
    "Pellicle is a UK drinks magazine paying fixed commission fees — £375 for a 1,500–2,000 word feature, £525 for a long read, £675 for a photo essay. Rates are based on a working rate of £0.25 per word. Pitches are accepted year-round by email.",
    "https://www.pelliclemag.com/pitching",
    "mailto:matthew@pelliclemag.com", "matthew@pelliclemag.com",
    "Email pitch to a named editor",
    src("Pellicle — Pitching, Rate and Style Guide (official)", "https://www.pelliclemag.com/pitching"),
    {"summary": "No nationality restriction stated. Pellicle is UK-based and mainly wants UK drinks and hospitality stories; international stories are taken but must have an angle relevant to the UK audience. International invoices are paid via Wise.",
     "mode": "open", "notStated": False},
    ["journalism", "articles", "creative-nonfiction"], "Feature, long read or photo essay",
    pay("GBP", 375, 675, "£375–£675 per commission",
        "Official rate card, based on a rough working rate of £0.25 per word: Features (1,500–2,000 words) £375; Long Reads (2,500 words and over) £525; Photo Essays (2,000 words and over, plus photography) £675. Photography (30–40 stills) £250 and illustration £250 are paid separately. Pellicle commissions to a fixed fee agreed in writing at commissioning, not to a per-word count.",
        "Invoices paid in GBP after submission of the first draft; international invoices processed via Wise"),
    {"min": 1500, "max": 2500, "display": "1,500–2,500+ words depending on format"},
    {"label": "Not stated on the pitching guide", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Narrative-driven stories about beer, pubs, cider, wine, spirits, sake, coffee and non-alcoholic drinks.",
     "Stories about the people, places, history and culture of drink — above all, what people are drinking and why.",
     "A fully fleshed-out pitch including your angle, your sources, and why the idea is relevant to Pellicle's audience specifically.",
     "Examples of previous work if you have not pitched them before — including self-published work on a blog or newsletter."],
    ["Stories based on press releases, or on press trips you were sent on.",
     "Guides, listicles, or anything that is or feels like advertorial.",
     "Topics already covered extensively by other publications.",
     "Travel stories with no link to food or drink.",
     "A quick \"are you interested in this\" or a collection of rough ideas — that will not earn a commission.",
     "Pitches sent by DM or phone. Email only."],
    ["Email pitch", "Previous work samples for first-time pitchers", "Fixed fee agreed in writing at commissioning"],
    "Agreed at commissioning; the written commission terms are legally binding on acceptance.",
    ["Read the full pitching guide at https://www.pelliclemag.com/pitching.",
     "Read several recent features from their back catalogue first.",
     "Email your pitch to one of the named editors listed on the guide."],
    ["pellicle", "drinks", "beer", "food writing", "uk", "gbp"]))

# ------------------------------------------------------------- 2 Extra Teeth
NEW.append(rec(
    "extra-teeth", "Extra Teeth", "Fiction and nonfiction",
    "Extra Teeth: £200 per piece, next window 1–14 December 2026",
    "Extra Teeth is a Scottish magazine paying £200 for each piece selected for the print magazine and £150 for its Substack. Pieces run 800–4,000 words. AI-generated work is explicitly prohibited. The next open call is 1–14 December 2026.",
    "https://extrateeth.co.uk/submissions",
    "mailto:submissions@extrateeth.co.uk", "submissions@extrateeth.co.uk",
    "Email during an open window",
    src("Extra Teeth — Submissions (official)", "https://extrateeth.co.uk/submissions"),
    {"summary": "Official: a Scottish magazine with an international outlook. They champion Scottish writing but also publish writers located elsewhere, and especially welcome submissions from underrepresented groups. Work in translation is accepted with the necessary permissions.",
     "mode": "open", "notStated": False},
    ["fiction", "creative-nonfiction", "essays"], "Fiction and nonfiction",
    pay("GBP", 150, 200, "£200 print / £150 Substack",
        "Official: £200 for each piece selected for the magazine, plus two contributor copies. Four further pieces are selected for their Substack, With Bite, paid at £150 per piece. There are 16 spots per issue — 12 in print, 4 on Substack. Extra Teeth charges no submission fee.",
        "Bank transfer within 30 days of receipt of a signed publishing agreement"),
    {"min": 800, "max": 4000, "display": "800–4,000 words"},
    {"label": "Do not chase before eight weeks from the end of the submission period", "band": "1-3-months", "official": True},
    "upcoming",
    {"display": "Submissions closed. Next open call 1–14 December 2026.",
     "openingDate": "2026-12-01", "windowEnd": "2026-12-14", "recurring": True},
    "prohibited",
    ["Short stories that stick with you, lingering in the memory long after reading.",
     "Essays that explore specific interests or issues from a new perspective.",
     "Work that is strange, bold and experimental — they offer space for writers to express their unique style.",
     "One piece only per submission period, 800–4,000 words, double-spaced size 12 in a Word document.",
     "A title sheet with your name, address, the word count and a bio under 100 words."],
    ["Any work written using artificial intelligence — it will not be considered.",
     "Secondary submissions in the same window; they will be deleted.",
     "Poetry, scripts or artwork — they do not currently publish these.",
     "Previously published work."],
    ["Email with F: TITLE or NF: TITLE in the subject line", "800–4,000 words", "Title sheet with bio under 100 words"],
    "Copyright remains with the author.",
    ["Wait for the window to open on 1 December 2026.",
     "Email one piece only to submissions@extrateeth.co.uk with F: TITLE (fiction) or NF: TITLE (nonfiction) in the subject line.",
     "Label your document F: YOUR NAME or NF: YOUR NAME and attach a title sheet."],
    ["extra teeth", "scotland", "fiction", "nonfiction", "gbp", "no ai"]))

# --------------------------------------------------- 3 Poetry Wales features
NEW.append(rec(
    "poetry-wales-features", "Poetry Wales", "Features, articles and interviews",
    "Poetry Wales features: £150 per 3,000 words, rolling pitches",
    "Poetry Wales has a rolling submissions window for features, articles and interviews, paid at £150 per 3,000 words or in that proportion. Send a 300-word pitch via Submittable at any time. Features usually run 2,000–3,000 words.",
    "https://www.poetrywales.co.uk/submissions/",
    "https://poetrywales.submittable.com/submit", None,
    "300-word pitch via Submittable",
    src("Poetry Wales — Submitting Your Work (official)", "https://www.poetrywales.co.uk/submissions/"),
    {"summary": "No nationality restriction stated on the submissions page.", "mode": "not-stated", "notStated": True},
    ["articles", "essays", "interviews"], "Feature, article or interview",
    pay("GBP", 150, 150, "£150 per 3,000 words",
        "Official payment rates: Articles £150/3,000 words, or in that proportion depending on the number of published words. Reviews are £67.50/1,500 words and poems are £20 each — those are listed separately on the same page. Payment is by PayPal only; if you cannot accept PayPal you forfeit the fee.",
        "On publication of the issue the work appears in"),
    {"min": 2000, "max": 3000, "display": "2,000–3,000 words as a rule"},
    {"label": "Not stated for features", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["A 300-word pitch via Submittable — you can send one at any time, the features window is rolling.",
     "Features, essays and interviews connected to poetry.",
     "Pitches connected to the slant of a current issue when those windows are open."],
    ["Submissions sent by email or social media, unless previously agreed.",
     "Poetry outside the 2–3 poetry windows a year — work sent when the window is closed is not read."],
    ["Submittable", "300-word pitch", "PayPal required to be paid"],
    "Copyright remains with the author. Poetry Wales Press Ltd retains the right to reproduce the piece digitally and in print for the magazine's own purposes.",
    ["Read https://www.poetrywales.co.uk/submissions/.",
     "Send a 300-word pitch through Submittable.",
     "Note that payment is by PayPal only."],
    ["poetry wales", "wales", "features", "interviews", "gbp"]))

# ----------------------------------------------------- 4 Poetry Wales poetry
NEW.append(rec(
    "poetry-wales-poetry", "Poetry Wales", "Poetry",
    "Poetry Wales poetry: £20 per poem, 2–3 windows a year",
    "Poetry Wales pays £20 per poem. The poetry window opens 2–3 times a year and is capped at 550 submissions per issue. They publish under 3% of the poems they receive. Submissions are currently closed.",
    "https://www.poetrywales.co.uk/submissions/",
    "https://poetrywales.submittable.com/submit", None,
    "Submittable during an open window",
    src("Poetry Wales — Submitting Your Work (official)", "https://www.poetrywales.co.uk/submissions/"),
    {"summary": "No nationality restriction stated on the submissions page.", "mode": "not-stated", "notStated": True},
    ["poetry"], "Poetry",
    pay("GBP", 20, 20, "£20 per poem",
        "Official payment rates: Poems £20 each. Contributors also receive one complimentary copy of their issue. Payment is by PayPal only; if you cannot accept PayPal you forfeit the fee.",
        "On publication of the issue the work appears in"),
    {"min": None, "max": None, "display": "Not stated"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "upcoming",
    {"display": "Poetry submissions are currently closed. The window opens 2–3 times a year.", "recurring": True},
    "not-stated",
    ["Poetry, submitted through Submittable during an open window.",
     "They cap the portal at 550 submissions per issue so that each poem gets proper attention."],
    ["Submissions sent when the window is closed — they will not be read.",
     "Email or social-media submissions, unless previously agreed."],
    ["Submittable", "Open window only", "PayPal required to be paid"],
    "Copyright remains with the author. Poetry Wales Press Ltd retains the right to reproduce the piece digitally and in print for the magazine's own purposes.",
    ["Check https://www.poetrywales.co.uk/submissions/ for the next window.",
     "Sign up to their newsletter — they announce openings there and on social media.",
     "Submit through Submittable when open."],
    ["poetry wales", "wales", "poetry", "gbp"]))

# --------------------------------------------------------- 5 Poetry London
NEW.append(rec(
    "poetry-london", "Poetry London", "Poetry, reviews and interviews",
    "Poetry London: £35 per poem, general submissions reopen 1 October",
    "Poetry London pays £35 per poem, with review and interview fees benchmarked at £50 per 1,000 words. General submissions are currently closed and reopen on 1 October. Send up to six poems; reading can take up to four months.",
    "https://poetrylondon.co.uk/submissions/",
    "https://poetrylondon.submittable.com/submit", None,
    "Submittable, or by post",
    src("Poetry London — Submissions (official)", "https://poetrylondon.co.uk/submissions/"),
    {"summary": "Open internationally — they will reply by email to work sent from abroad, though they cannot return manuscripts from outside the UK.",
     "mode": "open", "notStated": False},
    ["poetry", "reviews", "interviews"], "Poetry, reviews and interviews",
    pay("GBP", 35, 35, "£35 per poem",
        "Official: £35 per poem, though appropriate adjustments may be made for very long poems. Review and interview fees are agreed in advance with the Reviews Editor and benchmarked at £50 per 1,000 words. Contributors also receive one complimentary copy.",
        "Within 30 days following publication of the print issue, on receipt of an invoice"),
    {"min": None, "max": None, "display": "Maximum six poems per submission"},
    {"label": "Reading can take up to four months; no reply within 3 months means no", "band": "3-plus-months", "official": True},
    "upcoming",
    {"display": "General submissions are currently closed and reopen on 1 October.",
     "openingDate": "2026-10-01", "recurring": True},
    "not-stated",
    ["The best, most exciting poetry being written now — they are always interested in work by unpublished poets as well as celebrated ones.",
     "A maximum of six poems per submission, electronic or postal.",
     "An invoice after publication — they only pay on receipt of one."],
    ["Previously published work, except in exceptional circumstances.",
     "Postal submissions without correct postage — as a small charity they cannot collect underpaid post."],
    ["Submittable or post", "Maximum six poems", "Invoice required for payment"],
    "They take the first non-exclusive right to publish in the next issue in print and verbatim digital form, in English, plus a non-exclusive archive right. Contributors are encouraged to republish afterwards, with no permissions fee, crediting Poetry London.",
    ["Wait for general submissions to reopen on 1 October.",
     "Submit up to six poems via Submittable, or by post to Niall Campbell at Goldsmiths.",
     "Send an invoice after publication to be paid."],
    ["poetry london", "poetry", "reviews", "london", "gbp"]))

# ------------------------------------------------ 6 Shoreline of Infinity
NEW.append(rec(
    "shoreline-of-infinity", "Shoreline of Infinity", "Science fiction short stories",
    "Shoreline of Infinity: £20 per 1,000 words for science fiction",
    "Shoreline of Infinity is a Scottish science fiction magazine paying £20 per 1,000 words for stories up to 6,000 words. The submission window is currently closed. They particularly want authors from backgrounds underrepresented in the Western SF canon.",
    "https://shorelineofinfinity.com/submissions/",
    "https://shorelineofinfinity.com/submissions/", None,
    "Online submission form during an open window",
    src("Shoreline of Infinity — Submissions, fiction (official)", "https://shorelineofinfinity.com/submissions/"),
    {"summary": "Official: they are particularly interested in work from authors of backgrounds underrepresented in the Western science fiction canon, and authors from outside the anglophone West. If English is not your first language, tell them and they will keep it in mind while reading.",
     "mode": "open", "notStated": False},
    ["fiction"], "Science fiction short story",
    pay("GBP", 20, 20, "£20 per 1,000 words",
        "Official: they offer £20/1000 words. A reprint fee is paid for republishing in collections. Rates are stated per thousand words, so a 6,000-word story at the maximum length is £120.",
        "Not publicly stated"),
    {"min": None, "max": 6000, "display": "Maximum 6,000 words"},
    {"label": "Contact them if you have not heard within 3 months", "band": "3-plus-months", "official": True},
    "closed",
    {"display": "Submission window currently closed. No next opening date stated.", "recurring": True},
    "not-stated",
    ["Engaging science fiction — stories that give reality a tweak on the nose, an idea that makes them stop and think.",
     "Everything from high-concept literary SF to pulp-style adventure, sometimes at once.",
     "Work that pushes the boundaries of the genre while keeping a link to its rich and global history.",
     "A note if an acceptance would be your first fiction publication — they are keen to publish new voices."],
    ["Stories with no discernible science fictional element — they love fantasy, but this is an SF magazine.",
     "Unchallenged bigotry. They want fiction that actually interrogates social issues.",
     "Violent revenge fantasies, especially from the POV of a male character.",
     "Emailed manuscripts — these will be ignored."],
    ["Online submission form", "Maximum 6,000 words", "Times 12pt double spaced, .doc/.docx", "One story per call"],
    "They buy first digital, print and audio world rights in English, plus audio rights. After 9 months from original publication you are free to publish it however and wherever you like. They retain the right to keep selling back issues and anthologies.",
    ["Read a copy of Shoreline of Infinity first to see the kind of stories they publish.",
     "Watch the submissions page for the next window.",
     "Submit through the form on the page — not by email."],
    ["shoreline of infinity", "science fiction", "scotland", "gbp"]))

# ----------------------------------------------------------------- 7 Propel
NEW.append(rec(
    "propel-magazine", "Propel Magazine", "Poetry from emerging poets",
    "Propel Magazine: £20 honorarium, UK and Ireland poets only",
    "Propel Magazine publishes poets based in the UK or Ireland who have not yet published a first full-length collection, paying a £20 honorarium. Submissions run in six one-month windows a year and are currently closed.",
    "https://propelmagazine.co.uk/submissions",
    "https://propelmagazine.submittable.com/submit", "info@propelmagazine.co.uk",
    "Submittable during an open window",
    src("Propel Magazine — Submit (official)", "https://propelmagazine.co.uk/submissions"),
    {"summary": "Official and strict: poets must be based in the UK or Ireland, and must not have published a full-length poetry collection in English or be under contract for one. Due to the nature of their funding they cannot accept submissions from writers based overseas. Pamphlets and self-published collections are fine.",
     "mode": "restricted", "includesRegions": ["uk", "ireland"], "allowsDiaspora": False, "notStated": False},
    ["poetry"], "Poetry",
    pay("GBP", 20, 20, "£20 honorarium",
        "Official, from their FAQ: \"We offer an honorarium of £20 to each contributor.\"",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Maximum six poems per submission"},
    {"label": "Within six weeks of the end of the submission period", "band": "1-3-months", "official": True},
    "upcoming",
    {"display": "Submissions are currently closed. They run six one-month windows a year.", "recurring": True},
    "not-stated",
    ["Poetry from poets based in the UK or Ireland who have not published a first full-length collection.",
     "A maximum of six poems in a single document, one submission per window.",
     "An audio recording of you reading the poem if your work is accepted — they can help you make it."],
    ["Poems previously published online or in print, including on social media or your own blog.",
     "Submissions from poets based outside the UK and Ireland.",
     "Poets who have published a full collection in English, or are under contract for one.",
     "Postal submissions.",
     "Translations — they are not currently publishing these."],
    ["Submittable", "Based in UK or Ireland", "No full collection published", "Maximum six poems"],
    "All copyright remains with the author. Propel retains the right to publish the submission in any subsequent digital and print issues or anthologies.",
    ["Check https://propelmagazine.co.uk/submissions for the next window.",
     "Submit up to six poems in a single document via Submittable.",
     "Email info@propelmagazine.co.uk if you cannot access Submittable."],
    ["propel", "poetry", "emerging poets", "uk", "ireland", "gbp"]))

# ------------------------------------------------------------ 8 Fiction Desk
NEW.append(rec(
    "the-fiction-desk", "The Fiction Desk", "Short stories for print anthologies",
    "The Fiction Desk: £25 per 1,000 words, deadline 30 September 2026",
    "The Fiction Desk pays £25 per thousand words for short stories of 1,000–15,000 words in its print anthologies — £150 for a 6,000 word story. The current call closes at midnight UK time on 30 September 2026. There is a £5 submission fee and AI-written work is prohibited.",
    "https://www.thefictiondesk.com/submissions/short-story-submission-guidelines.php",
    "https://www.thefictiondesk.com/submissions/", None,
    "Online submission form",
    src("The Fiction Desk — Short Story Submission Guidelines (official)",
        "https://www.thefictiondesk.com/submissions/short-story-submission-guidelines.php"),
    {"summary": "Official: they are based in the UK and are happy to consider short story submissions from authors all over the world. All submissions must be in English; if submitting a translation, note who is submitting and who owns the rights.",
     "mode": "worldwide", "notStated": False},
    ["fiction"], "Short story",
    pay("GBP", 25, 25, "£25 per 1,000 words",
        "Official: The Fiction Desk and Uncertain Stories both pay £25 per thousand words — for example £100 for a 4,000 word story, or £150 for a 6,000 word story. Contributors also receive six printed copies. Published stories are eligible for the Writer's Award, a £100 cash prize for the best story in each volume, judged by the contributors. Note the £5 submission fee per story.",
        "Not publicly stated"),
    {"min": 1000, "max": 15000, "display": "1,000–15,000 words"},
    {"label": "Within six weeks, often much less", "band": "1-3-months", "official": True},
    "deadline",
    {"date": "2026-09-30", "display": "Current call closes midnight UK time, Wednesday 30 September 2026",
     "windowEnd": "2026-09-30", "recurring": True},
    "prohibited",
    ["Short stories on any of the themes and genres featured in Fiction Desk anthologies.",
     "Stories between 1,000 and 15,000 words — most published stories run 2,000–7,000 words.",
     "Submissions through their online form; stories are considered for both The Fiction Desk and partner publisher Uncertain Stories."],
    ["Novel excerpts, non-fiction, poetry, or anything with illustrations or photographs.",
     "Any writing generated using AI tools. Their submission form and publishing contract both require authors to confirm no AI was used — including tools that standardise or 'correct' grammar and punctuation.",
     "Postal submissions — these will not reach the right people.",
     "PDF or Microsoft Works documents."],
    ["Online submission form", "£5 submission fee per story", "1,000–15,000 words", "English only"],
    "They ask for first serial rights, a brief period of exclusivity (usually six months), and the right to keep the story in print as part of the anthology. They place no limits on what you do with the story after the exclusivity period.",
    ["Read the guidelines at https://www.thefictiondesk.com/submissions/short-story-submission-guidelines.php.",
     "Look at one of their anthologies to check the fit.",
     "Submit through the online form before midnight UK time on 30 September 2026, paying the £5 fee by card or PayPal."],
    ["fiction desk", "short story", "anthology", "uk", "gbp", "no ai"]))

# -------------------------------------------------------------- 9 The Rialto
NEW.append(rec(
    "the-rialto", "The Rialto", "Poetry",
    "The Rialto: £20 per poem on publication",
    "The Rialto, a Norwich-based poetry magazine, pays £20 per poem on publication. Send up to six poems through Submittable when the window is open, or by post at any time. They aim to reply within three months.",
    "https://www.therialto.co.uk/pages/about/the-magazine/submissions/",
    "https://therialto.submittable.com/submit", "info@therialto.co.uk",
    "Submittable when open, or by post at any time",
    src("The Rialto — Poetry Submissions (official)", "https://www.therialto.co.uk/pages/about/the-magazine/submissions/"),
    {"summary": "No nationality restriction stated on the submissions page.", "mode": "not-stated", "notStated": True},
    ["poetry"], "Poetry",
    pay("GBP", 20, 20, "£20 per poem",
        "Official: \"We currently pay £20 per poem on publication.\" Articles and reviews are commissioned rather than submitted, and no rate is stated for them.",
        "On publication"),
    {"min": None, "max": None, "display": "Up to six poems per submission"},
    {"label": "They aim to reply within three months", "band": "3-plus-months", "official": True},
    "unknown",
    {"display": "Window-based. Check their Submittable portal to see whether online submissions are open — postal submissions are accepted at any time.", "recurring": True},
    "not-stated",
    ["New poets and new poems — they are always looking for both.",
     "Up to six poems in a single Word document, each poem starting on a new page with your name or email on each page.",
     "A cover letter with your postal address, phone number and email."],
    ["Multiple simultaneous submissions to them.",
     "Poems published anywhere before, in print or online.",
     "Email submissions or links to work via social media — neither will be accepted."],
    ["Submittable or post", "Up to six poems", "Single Word document", "SAE for a postal reply"],
    "Not stated on the submissions page.",
    ["Check the Submittable portal at https://www.therialto.co.uk/pages/about/the-magazine/submissions/ to see if the window is open.",
     "Send up to six poems in one Word document with a cover letter.",
     "Or post to The Editor, The Rialto, 74 Britannia Road, Norwich NR1 4HS with an SAE."],
    ["the rialto", "poetry", "norwich", "uk", "gbp"]))

# ---------------------------------------------------------------- 10 Gutter
NEW.append(rec(
    "gutter-magazine", "Gutter", "Fiction, poetry and essays",
    "Gutter: flat £50 per piece, Scottish and international writing",
    "Gutter is a magazine of new Scottish and international writing paying a flat £50 per published piece regardless of length or style. Fiction, poetry and essay windows run twice a year and are currently closed; reviews are commissioned on a rolling, paid basis.",
    "https://www.guttermag.co.uk/submit",
    "https://guttermagazine.submittable.com/submit", None,
    "Submittable during an open window",
    src("Gutter — Submit (official)", "https://www.guttermag.co.uk/submit"),
    {"summary": "Official: during their two annual windows they accept poetry, fiction and essays from writers in Scotland and beyond. Reviews are commissioned on newly published books with a clear Scottish connection. Scots and Gaelic guidelines are provided on the same page.",
     "mode": "open", "notStated": False},
    ["fiction", "poetry", "essays", "reviews"], "Fiction, poetry, essays and reviews",
    pay("GBP", 50, 50, "Flat £50 per piece",
        "Official: \"Successful contributors will be paid a flat fee of £50 for work published in the magazine, regardless of length or style.\" Published authors also receive a complimentary copy. Reviews and critical essays are separately described as paid opportunities, with no rate stated.",
        "Not publicly stated"),
    {"min": None, "max": 2500, "display": "Prose to 2,500 words; up to 3 poems totalling 100 lines"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "closed",
    {"display": "Fiction, poetry and essay submissions are currently closed. Windows run twice a year, in Spring and Autumn.", "recurring": True},
    "not-stated",
    ["Work that challenges, re-imagines or undermines the status quo, and pushes at the boundaries of form and function.",
     "They reject any distinction between literary and genre, high art and popular culture.",
     "Poetry: up to three poems totalling no more than 100 lines, in a single document.",
     "Fiction and essays: a maximum of 2,500 words, one prose submission per issue.",
     "Review pitches at any time — they will ask for examples of previous work before commissioning."],
    ["Work that does not conform to the guidelines — it will not be considered.",
     "More than one prose submission per issue."],
    ["Submittable", "Prose max 2,500 words", "Poetry max 3 poems / 100 lines", ".docx or .rtf"],
    "Not stated on the submit page.",
    ["Watch https://www.guttermag.co.uk/submit or their newsletter for the Spring or Autumn window.",
     "Submit via Submittable as .docx or .rtf.",
     "For reviews, get in touch at any time with examples of previous work."],
    ["gutter", "scotland", "fiction", "poetry", "essays", "gbp"]))

# -------------------------------------------------------- 11 fourteen poems
NEW.append(rec(
    "fourteen-poems", "fourteen poems", "LGBTQ+ poetry",
    "fourteen poems: £30 per poem, open for Issue 21",
    "fourteen poems publishes an anthology of LGBTQ+ poetry around three times a year and pays £30 for each poem published. Submissions are open for Issue 21. Submission is free, you keep your copyright, and they welcome poets who have never been published.",
    "https://www.fourteenpoems.com/submit",
    "https://www.fourteenpoems.com/submit", None,
    "Submissions platform linked from their submit page",
    src("fourteen poems — Submit (official)", "https://www.fourteenpoems.com/submit"),
    {"summary": "Official: for LGBTQ+ poets. They are based in London but publish poets from all over the world, and want to read your work even if you have never been published before.",
     "mode": "open", "notStated": False},
    ["poetry"], "Poetry",
    pay("GBP", 30, 30, "£30 per poem",
        "Official: \"We pay £30 for each poem published.\" Submission is free. Solo pamphlets are a separate programme and are currently closed.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Not stated"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["New queer poetry — they want to represent all that is thrilling about the new wave of LGBTQ+ poets.",
     "A single Word or PDF document containing your work, plus a short paragraph about yourself.",
     "In that paragraph: a little about you, how you identify, whether you have been published elsewhere, and what your work is like."],
    ["Your name on the poetry document itself — poems are judged blind.",
     "Graphics or images in the bio or the submission.",
     "Work already published online or in print.",
     "Submissions by email — they are not accepted."],
    ["Submissions platform, not email", "Single Word or PDF document", "Short bio paragraph", "Free to submit"],
    "You retain your copyright with their anthologies.",
    ["Read the guidelines at https://www.fourteenpoems.com/submit.",
     "Prepare one Word or PDF document with your poems and a short bio paragraph, keeping your name off the poems.",
     "Submit for Issue 21 through the platform linked on the page."],
    ["fourteen poems", "lgbtq", "queer", "poetry", "london", "gbp"]))

# ---------------------------------------------------------------- 12 Granta
NEW.append(rec(
    "granta", "Granta", "Fiction and non-fiction",
    "Granta submissions: open 1–30 September 2026",
    "Granta is open to unsolicited fiction and non-fiction during four month-long windows a year — the current one closes 30 September 2026. Granta pays contributors but does not state a rate publicly. There is a £3.50 submission fee, with 200 free places per window for low-income writers.",
    "https://granta.com/submissions/",
    "https://granta.submittable.com/submit", None,
    "Submittable during an open window",
    src("Granta — Submissions (official)", "https://granta.com/submissions/"),
    {"summary": "Official: committed to offering a home to writing by those who are marginalised or underrepresented — writers of colour, working class or low-income writers, queer, transgender, non-binary and gender-nonconforming writers, and writers with disabilities. No nationality restriction. Work must be in English.",
     "mode": "open", "notStated": False},
    ["fiction", "creative-nonfiction", "essays"], "Fiction and non-fiction",
    pay("GBP", None, None, "Pays contributors — rate not stated",
        "Granta does not publish a rate on its submissions page. BRYME does not guess: this record carries no figure rather than an invented one. Note the cost in the other direction — a £3.50 fee for full-length prose submissions, equivalent to printing and postage, claimable against a new subscription. During every opening period they offer 200 free submissions to authors on low incomes.",
        "Not publicly stated"),
    {"min": 3000, "max": 6000, "display": "No set maximum or minimum; most submissions run 3,000–6,000 words"},
    {"label": "Not stated. They cannot comment on your work.", "band": "not-stated", "official": False},
    "deadline",
    {"date": "2026-09-30", "display": "Open 1–30 September 2026. Further 2026 windows: 1–31 December. Poetry is closed.",
     "windowStart": "2026-09-01", "windowEnd": "2026-09-30", "recurring": True},
    "not-stated",
    ["One complete story or essay at a time, or one document of no more than four poems when poetry is open.",
     "Original material only — first-ever publication. An original translation is fine if the work has never appeared in English.",
     "A cover letter stating where your work has been published before, if relevant.",
     "Double-spaced prose; for poetry, whatever spacing best represents the work."],
    ["Academic essays or reviews.",
     "Book manuscripts or unsolicited book proposals — Granta Books does not accept these.",
     "Work that has already appeared on the web or elsewhere in print.",
     "Multiple submissions in a single genre.",
     "Work not written in English."],
    ["Submittable", "£3.50 fee for full-length prose (200 free low-income places per window)", "English only", "Original material only"],
    "Not stated on the submissions page.",
    ["Read https://granta.com/submissions/ and their FAQ page.",
     "If you are a low-income writer, read the low-income entry guidelines first — there are 200 free places each window.",
     "Submit through Submittable before midnight UK time on 30 September 2026."],
    ["granta", "fiction", "non-fiction", "literary", "uk", "prestige"]))

# ------------------------------------------------------- 13 London Magazine
NEW.append(rec(
    "the-london-magazine", "The London Magazine", "Poetry, short fiction and non-fiction",
    "The London Magazine: pays for everything published in print",
    "The London Magazine, the UK's oldest literary magazine, pays a fee for everything it publishes in print but cannot currently pay for pieces published on the website. It takes poetry up to 40 lines, fiction to 4,000 words and non-fiction of 800–2,000 words.",
    "https://thelondonmagazine.org/submission-guidelines/",
    "https://thelondonmagazine.submittable.com/submit", "submissions@thelondonmagazine.org",
    "Submittable portal, email to the portal, or post",
    [{"name": "The London Magazine — Submission Guidelines (official)", "url": "https://thelondonmagazine.org/submission-guidelines/"},
     {"name": "The London Magazine — Submissions (official)", "url": "https://www.thelondonmagazine.org/submissions/"}],
    {"summary": "No nationality restriction stated. They are interested in writing with a London focus but not exclusively, since London is a world city with international concerns.",
     "mode": "not-stated", "notStated": True},
    ["poetry", "fiction", "essays", "reviews"], "Poetry, short fiction, non-fiction and reviews",
    pay("GBP", None, None, "Pays for print — rate not stated",
        "Official: \"We pay a fee for everything we publish in print. We are currently unable to pay for pieces published on the website.\" No figure is published, so BRYME states none. They charge a £3.50 fee for submissions made outside their free windows — they advise submitting near the start of the month, before the portal's free quota is used up.",
        "Not publicly stated"),
    {"min": 800, "max": 4000, "display": "Poetry to 40 lines; fiction to 4,000 words; non-fiction 800–2,000 words"},
    {"label": "Not stated; the portal is intended to be faster than the old email system", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Poetry with a commitment to the ultra specificities of language and a refined sense of simile and metaphor — tight, exact structure, no longer than 40 lines, maximum six poems.",
     "Short fiction addressing mature and sophisticated themes with elegance of style, up to 4,000 words.",
     "Non-fiction — reviews, essays, memoir and features that are erudite, lucid and incisive, 800–2,000 words."],
    ["Abstraction — \"the enemy of good poetry\". Long, loose poems.",
     "Science fiction, fantasy or erotica — not normally published.",
     "Work published anywhere before, including a website, blog or online forum, broadcast, or placed in any competition."],
    ["Submittable portal", "£3.50 fee outside the free monthly quota", "Genre-specific word limits", "Previously unpublished"],
    "Publication includes the print issue, the eBook (Kindle) edition, The London Magazine App and thelondonmagazine.org.",
    ["Read https://thelondonmagazine.org/submission-guidelines/.",
     "Submit near the start of the month, before the free quota is used, to avoid the £3.50 fee.",
     "Use the Submittable portal, or email the genre-specific portal address with your work attached."],
    ["london magazine", "poetry", "fiction", "non-fiction", "london", "oldest"]))

# ------------------------------------------------------------ 14 Hinterland
NEW.append(rec(
    "hinterland", "Hinterland", "Creative non-fiction",
    "Hinterland: pays for all published creative non-fiction",
    "Hinterland publishes creative non-fiction of 500–5,000 words and pays for all the work it publishes, though it does not state a rate. It runs 2–3 windows a year via Submittable; subscribers can submit year-round. There is a £3 readers' fee, waived for subscribers.",
    "https://www.hinterlandnonfiction.com/submissions",
    "https://hinterland.submittable.com/submit", None,
    "Submittable only",
    src("Hinterland — Nonfiction submissions (official)", "https://www.hinterlandnonfiction.com/submissions"),
    {"summary": "Official: they publish the best in creative non-fiction from around the globe. No nationality restriction stated.",
     "mode": "open", "notStated": False},
    ["creative-nonfiction", "essays"], "Creative non-fiction",
    pay("GBP", None, None, "Pays for all published work — rate not stated",
        "Official: \"We pay for all the work that we publish.\" No figure is given, so BRYME states none rather than guessing. Note the cost in the other direction — a £3 readers' fee on all submissions, redeemable as a discount against a subscription. Subscribers submit free, all year round.",
        "Not publicly stated"),
    {"min": 500, "max": 5000, "display": "500–5,000 words"},
    {"label": "They aim to read all submissions within 5–6 months", "band": "3-plus-months", "official": True},
    "upcoming",
    {"display": "They operate 2–3 submission windows a year. Subscribers can submit all year round.", "recurring": True},
    "not-stated",
    ["Creative non-fiction on any topic or from any genre — they ask only that it is non-fiction.",
     "A particular interest in discovering new voices and in pieces that sit outside the usual categories.",
     "Anything from 500–5,000 words, including self-contained extracts from longer or in-progress works."],
    ["Submissions made by any means other than Submittable — they will be returned unopened.",
     "Previously published material."],
    ["Submittable only", "£3 readers' fee (free for subscribers)", "500–5,000 words", "Previously unpublished"],
    "Not stated on the submissions page.",
    ["Follow them or join their newsletter to be notified when a window opens.",
     "Submit only via Submittable — anything else is returned unopened.",
     "Subscribers can skip the window and the fee, and submit year-round."],
    ["hinterland", "creative nonfiction", "essays", "uk"]))

# -------------------------------------------------------------- 15 Mslexia
NEW.append(rec(
    "mslexia", "Mslexia", "Poetry and short fiction for women writers",
    "Mslexia: pays for every piece published, women writers only",
    "Mslexia is a magazine for women's writing that pays for every piece it publishes. The Showcase section takes stories up to 2,200 words and poems up to 40 lines on a set theme, judged by a guest curator. Several current slots close on 5 October 2026.",
    "https://mslexia.co.uk/submit-your-work/poetry/",
    "https://mslexia.co.uk/submit-your-work/", None,
    "Online form on the relevant submissions page",
    [{"name": "Mslexia — Poetry submissions (official)", "url": "https://mslexia.co.uk/submit-your-work/poetry/"},
     {"name": "Mslexia — Submit your work (official)", "url": "https://mslexia.co.uk/submit-your-work/"}],
    {"summary": "Mslexia is a magazine for women's writing and its submission routes are for women writers. Some individual slots (Salon Showcase, Poems for the Planet) are restricted further to subscribers or Salon members — check the specific slot before submitting.",
     "mode": "restricted", "includesGroups": ["women"], "notStated": False},
    ["poetry", "fiction"], "Poetry and short fiction",
    pay("GBP", None, None, "Pays for every piece published — rate not stated",
        "Official: \"we pay for every piece we publish.\" Mslexia does not put a figure on the Showcase submissions page itself, so BRYME states none. Their competitions publish separate, specific prize amounts, but those are contests with entry fees, not submissions.",
        "Not publicly stated"),
    {"min": None, "max": 2200, "display": "Stories to 2,200 words; poems to 40 lines"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "deadline",
    {"date": "2026-10-05", "display": "Several current slots close 5 October 2026 — check each slot, they run to their own dates",
     "windowEnd": "2026-10-05", "recurring": True},
    "not-stated",
    ["Poetry and short fiction on the announced theme for the Showcase section, chosen by a guest curator-judge — past judges include Hilary Mantel, Carol Ann Duffy, Val McDermid, Jackie Kay and Kate Mosse.",
     "Up to four poems and/or up to two stories on any one theme.",
     "Stories no longer than 2,200 words and poems up to 40 lines. There is no lower word or line limit."],
    ["Your name anywhere on the work itself — submissions are read anonymously.",
     "Submissions to subscriber-only slots if you are not a subscriber or Salon member."],
    ["Online form", "Women writers", "Theme-specific", "Name must not appear on the work"],
    "See their Submissions Policy page.",
    ["Read https://mslexia.co.uk/submit-your-work/ and pick the right slot — there are five separate poetry routes.",
     "Check that slot's own deadline and whether it is subscriber-only.",
     "Submit through the form on the page, with your name off the work itself."],
    ["mslexia", "women writers", "poetry", "fiction", "uk"]))

# ------------------------------------------ 16 Modern Poetry in Translation
NEW.append(rec(
    "modern-poetry-in-translation", "Modern Poetry in Translation", "Poetry in translation",
    "Modern Poetry in Translation: pays a fee for translated poetry",
    "Modern Poetry in Translation is the only UK magazine dedicated solely to poetry in translation. It pays a fee to contributors, takes up to six poems per submission through Submittable during announced windows, and aims to respond within four months.",
    "https://modernpoetryintranslation.com/submit/",
    "https://modernpoetryintranslation.submittable.com/submit", None,
    "Submittable during an announced window",
    src("Modern Poetry in Translation — Submissions guidelines (official)", "https://modernpoetryintranslation.com/submit/"),
    {"summary": "Official: they welcome work from any age and accept translations from any language, with a preference for contemporary work. You must state which languages you are fluent in on the submission form. No nationality restriction.",
     "mode": "open", "notStated": False},
    ["translation", "poetry"], "Poetry in translation",
    pay("GBP", None, None, "Pays a fee — amount not stated",
        "Official: \"We pay a fee to our contributors.\" No figure is published, so BRYME states none. Note that responsibility for clearing rights and permissions for translated works — and paying any related fees — lies with the translator.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Up to six poems per submission"},
    {"label": "They endeavour to respond within four months", "band": "3-plus-months", "official": True},
    "unknown",
    {"display": "Window-based. They publicise submissions windows on their website, newsletter and social media.", "recurring": True},
    "not-stated",
    ["Translations of poetry only — not original English-language poetry — and the translations must be previously unpublished.",
     "Up to six poems per submission, with a preference for contemporary work.",
     "A statement of which languages you are fluent in, on the submissions form.",
     "Confirmation that you can obtain reproduction rights for the translations, in print and online."],
    ["Original English-language poetry.",
     "Speculative email submissions outside a dedicated submissions period.",
     "Work previously published elsewhere."],
    ["Submittable only", "Translations only", "Up to six poems", "Translator clears permissions"],
    "Copyright for work appearing in MPT rests with the contributor and with MPT. Work will be accessible online to digital subscribers, made available as an e-book, and may appear on their website — permissions must cover electronic and print versions and digital reproduction.",
    ["Browse the poems archive first to see which translated authors have featured recently.",
     "Clear permissions for your translations — this is the translator's responsibility and can take time.",
     "Submit up to six poems via Submittable during an announced window."],
    ["modern poetry in translation", "translation", "poetry", "uk", "mpt"]))


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
        # Contract checks: never let an unstated rate become 0.
        p = r["pay"]
        if p["amountMin"] == 0 or p["amountMax"] == 0:
            sys.exit(f"ERROR: {r['slug']} has a zero pay amount")
        if (p["amountMin"] is None) != (p["amountMax"] is None):
            sys.exit(f"ERROR: {r['slug']} has a half-stated pay range")
        for k in ("officialUrl", "excerpt", "seoTitle", "howToSubmit", "whatTheyWant"):
            if not r.get(k):
                sys.exit(f"ERROR: {r['slug']} missing {k}")

    opps.extend(NEW)
    data["opportunities"] = opps
    data["updatedAt"] = V
    OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    pc = json.loads(PUBC.read_text(encoding="utf-8"))
    for r in NEW:
        pc[r["slug"]] = {"base": "UK", "label": "United Kingdom"}
    PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Added {len(NEW)} UK records. Total opportunities: {len(opps)}")
    stated = [r for r in NEW if r["pay"]["amountMin"] is not None]
    print(f"  with a stated rate: {len(stated)}")
    print(f"  pays but no public rate: {len(NEW) - len(stated)}")


if __name__ == "__main__":
    main()
