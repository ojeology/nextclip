"""Add verified writing-market batch 16 (2026-10-01).

Eight NEW markets, read off each publication's OWN guidelines page on 2026-10-01.
The raw text of every page is kept under research/rebuild/raw/<slug>.txt so a
reading can be re-checked without re-fetching.

WHERE THESE CANDIDATES CAME FROM
--------------------------------
pw.org's Literary Magazines directory, for names and official submission URLs
only, as in batches 4 and 13-15:

    the batch-15 queue, resumed on the side branch
    -> candidates not already on this desk, matched after normalising the raw
       crawl's underscores against the records' hyphens (colorado_review vs
       colorado-review) - without that step a shipped market looks unshipped
    -> each publication's OWN guidelines page fetched and read

pw.org's own pay notes and reading-fee flags were not read and are not used.
Every figure below comes from the publication's own page.

WHAT WAS READ, AND WHAT WAS NOT FLATTENED
-----------------------------------------
This batch is mostly cheap-rate small presses, so the danger is not missing a
zero - it is inflating one. The distinctions kept apart:

  * The First Line REFUSES simultaneous submissions outright ("we do not accept
    simultaneous submissions"). It is one of eight records in the whole dataset
    that says no, and the temptation is to record it as not-stated because
    saying no is unusual.
  * Booth pays a flat $50 whatever the length, and charges $3 to submit. The fee
    is the writer's cost.
  * Consequence pays by printing route and by page count: $20 a poem in print,
    $30-$50 a prose piece by length, $150 for an eight-page art spread, with
    different figures again online and on Substack. Collapsing that to one
    number would misstate every rate in it.
  * Fahmidan pays $35 a piece and points to Submittable for its prices: the page
    states no fee amount, so none is recorded.
  * Free the Verse pays $10 for an issue poem and $20 for Marginalia. Two
    routes, two rates, both quoted.
  * Fairy Tale Review's only window on its page ran 15 March to 15 July 2025 and
    Volume 22 is already published. The record is closed and says no later window
    is stated rather than inventing the next one.

BASE COUNTRIES
--------------
Recorded only where the page itself places the publication. Consequence, The
First Line and Fairy Tale Review name no location, so all three are filed
International rather than guessed from a familiar masthead. Booth says "Butler",
Chicago Review of Books says Chicago, Fahmidan says London and the United
Kingdom, Invisible City says the University of San Francisco.
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-10-01"
READ = "2026-10-01"


def rec(slug, publication, title, seo, excerpt, official, apply_url, apply_email,
        apply_method, sources, elig, types, type_label, pay, wc, response,
        status, deadline, ai, want, dont, reqs, rights, how, keywords,
        sim="not-stated", simnote=None):
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
        "simultaneousSubmissions": sim, "simultaneousNote": simnote,
    }


def src(name, url):
    return [{"name": name, "url": url}]


def pay(cur, lo, hi, display, conditions, timing):
    return {"currency": cur, "amountMin": lo, "amountMax": hi,
            "display": display, "conditions": conditions, "timing": timing}


def intl(summary="No stated country restriction on the guidelines page."):
    return {"summary": summary, "mode": "not-stated", "includesRegions": [],
            "allowsDiaspora": True, "notStated": True}


def worldwide(summary):
    return {"summary": summary, "mode": "worldwide", "includesGroups": [],
            "includesRegions": [], "allowsDiaspora": True, "notStated": False}


NEW = []
NEW.append(rec(
    "booth", "Booth",
    "Fiction, poetry and nonfiction: $50 flat, regardless of length",
    "Booth: $50 for every published piece, open 1 September",
    "Booth pays $50 for every piece it publishes, whatever the length, sent by PayPal "
    "after online publication. It reads 1 September to 30 November and 1 January to 31 "
    "March, taking up to three poems or micro essays, two flashes, or one prose piece "
    "of up to 7,500 words, and charges $3 to submit. Simultaneous work is fine if you "
    "withdraw it, and AI-assisted writing is refused.",
    "https://booth.submittable.com/submit", "https://booth.submittable.com/submit",
    None, "Online form through Submittable; one submission at a time.",
    src("Booth - Submissions (official)", "https://booth.submittable.com/submit"),
    intl("Official page: \"Anyone can submit to Booth except for Butler employees, "
         "current Butler students, or anyone with affiliations to Butler's MFA "
         "program.\" No country restriction stated."),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, fiction, flash and creative nonfiction",
    pay("USD", 50, 50, "$50 per published piece, regardless of length",
        "Official page: \"We pay $50, regardless of length. This will be issued via "
        "PayPal after the online publication of your work.\" The Submittable form "
        "carries a $3.00 charge per submission, which is the writer's cost and is not "
        "part of the rate.",
        "After online publication, by PayPal"),
    {"min": None, "max": 7500,
     "display": "Poetry or micro essays: up to 3 pieces, micro meaning 300 words or "
                "fewer. Flash: up to 2 pieces of 500 words or fewer. Fiction or "
                "creative nonfiction: up to 7,500 words in a single document."},
    {"label": "By the end of May", "band": "3-plus-months", "official": True},
    "open",
    {"display": "Reads 1 September to 30 November, then 1 January to 31 March; "
                "responses usually go out by the end of May",
     "openingDate": "2026-09-01", "windowEnd": "2026-11-30", "recurring": True},
    "prohibited",
    ["Fiction, poetry, flash and micro work - the magazine says it publishes writing "
     "it loves and is not prescriptive about genre.",
     "Creative nonfiction alongside fiction.",
     "Themed calls, announced from time to time on the page."],
    ["Work made with generative AI: \"We do not accept submissions aided by "
     "generative AI.\"",
     "More than one submission at a time.",
     "Prose over 7,500 words, or more pieces than the category allows.",
     "Work from Butler employees, current Butler students, or anyone affiliated with "
     "Butler's MFA program."],
    ["Read https://booth.submittable.com/submit before sending.",
     "Submit through Submittable, where each submission carries a $3.00 charge.",
     "Poetry or micro essays: up to 3 pieces, micro being 300 words or fewer.",
     "Flash: up to 2 pieces of 500 words or fewer.",
     "Fiction or creative nonfiction: one piece, up to 7,500 words, in a single "
     "document.",
     "Withdraw accepted simultaneous work from the submission manager."],
    "Not stated on the guidelines page.",
    ["Read https://booth.submittable.com/submit before sending.",
     "Submit through the Submittable form; the form asks you to confirm the work was "
     "not made with AI.",
     "Send no more than the category allows - one prose piece, two flashes, or three "
     "poems or micro essays.",
     "If a simultaneous submission is taken elsewhere, withdraw it through the "
     "submission manager."],
    ["booth", "$50 per piece", "butler university", "submittable",
     "no generative ai", "simultaneous submissions", "flash fiction",
     "micro essays", "september reading period"],
    "accepted",
    "Simultaneous submissions okay? You bet. But you should know that if your work is "
    "accepted elsewhere and you don't bother to withdraw it from our submission "
    "manager, your name goes on the Secret List of writers who did not withdraw their "
    "simultaneous submissions. "
    f"— https://booth.submittable.com/submit (read {READ})"))

NEW.append(rec(
    "chicago-review-of-books", "Chicago Review of Books",
    "Reviews and interviews: $25; features and essays: $75",
    "Chicago Review of Books: $25 for reviews, $75 for features",
    "The Chicago Review of Books pays $25 for reviews and interviews and $75 for "
    "features, taking pitches by email two to three months ahead of a book's "
    "publication. Reviews run about 600 to 800 words. It states nothing about "
    "simultaneous pitches, fees, rights or AI on its writer page.",
    "https://chireviewofbooks.com/faq", "https://chireviewofbooks.com/faq",
    "chireviewofbooks@gmail.com",
    "Pitch by email to chireviewofbooks@gmail.com; no form is used.",
    src("Chicago Review of Books - Write for us and FAQ (official)",
        "https://chireviewofbooks.com/faq"),
    intl(),
    ["reviews", "interviews", "essays", "articles"],
    "Book reviews, author interviews, features and essays",
    pay("USD", 25, 75, "$25 for reviews and interviews, $75 for features",
        "Official page: \"We are! Currently, we are able to pay $25 for reviews and "
        "interviews and $75 for features.\"",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Reviews run about 600-800 words; length for features and essays is "
                "settled at commissioning"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "rolling", None, "not-stated",
    ["Book reviews, author interviews, features and author-written essays.",
     "Book lists that gather significant or underappreciated books around a theme.",
     "Essays that put books in conversation with culture.",
     "Pitches with a clear reason why this book and why you."],
    ["A pitch that does not say why this book and why you - the page's short answer "
     "to what it wants.",
     "A pitch for a review sent later than about two months before the book's "
     "publication date."],
    ["Read https://chireviewofbooks.com/faq before pitching.",
     "Pitch by email to chireviewofbooks@gmail.com - the page does not use a "
     "submission form.",
     "Pitch reviews and interviews about two to three months ahead of the book's "
     "publication date.",
     "Say why this book and why you."],
    "Not stated on the page.",
    ["Read https://chireviewofbooks.com/faq before pitching.",
     "Email the pitch to chireviewofbooks@gmail.com.",
     "Pitch reviews and interviews two to three months before publication, and "
     "features or essays at any time.",
     "Wait to be commissioned before writing the piece."],
    ["chicago review of books", "$25 reviews", "$75 features", "book reviews",
     "author interviews", "pitch by email", "stories matter foundation",
     "chicago"],
    "not-stated", None))

NEW.append(rec(
    "consequence", "Consequence",
    "Poetry from $20, prose from $30, art spread $150 - print, online and Substack",
    "Consequence: $20-$150, paying print, online and Substack rates",
    "Consequence pays for everything it prints: $20 a poem, $30-$50 a prose piece by "
    "length, $150 for an eight-page art spread in print, $50 online and $30 on "
    "Substack. Fiction and nonfiction run under 4,000 to 5,000 words and reviews "
    "1,500 to 3,000. It reads 15 January to 15 April and 15 July to 15 October, takes "
    "up to three poems, and refuses work made with AI.",
    "https://consequenceforum.org/submissions",
    "https://consequenceforum.org/submissions", None,
    "Online form through Submittable; reviews may instead be pitched to "
    "reviews@consequenceforum.org.",
    src("Consequence - Submissions (official)",
        "https://consequenceforum.org/submissions"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction", "essays", "reviews", "articles"],
    "Poetry, fiction, nonfiction, reviews and visual art",
    pay("USD", 20, 150,
        "$20 per poem in print, $30-$50 per prose piece in print by length, $150 for "
        "an eight-page art spread, $50 online, $30 on Substack",
        "Official submissions page, by section: Poetry - \"Print: $20 per piece / "
        "Online Feature: $50 / Substack: $30\"; Fiction and Nonfiction - \"Print 1-4 "
        "pp: $30 / Print 5-10 pp: $40 / Print 11+ pp: $50 / Online Feature: $50 / "
        "Substack: $30\"; Visual Art - \"Print: $150 for eight-page spread\". Reviews "
        "\"primarily\" come from solicitations but the page pays for them.",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "Nonfiction under 4,000 words; fiction shorts and excerpts under "
                "5,000 words; flash under 1,000 words; reviews 1,500-3,000 words; "
                "poetry up to three poems"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Spring reading period 15 January to 15 April; fall reading period 15 "
                "July to 15 October; translations and visual art are read year-round",
     "openingDate": "2026-07-15", "windowEnd": "2026-10-15", "recurring": True},
    "prohibited",
    ["Poetry in any form, with up to three poems per submission.",
     "Fiction and nonfiction: critical and personal essays, narrative nonfiction, "
     "interviews, shorts, flash and excerpts.",
     "Reviews of books, films and plays, by pitch to reviews@consequenceforum.org.",
     "Visual art in all forms and mediums, read year-round.",
     "Translations, read year-round, at the pay scale of the genre translated."],
    ["Work created by AI, even partially: the page states a zero-tolerance policy.",
     "More than three poems in one submission.",
     "Nonfiction over 4,000 words, fiction shorts or excerpts over 5,000 words, or "
     "flash over 1,000 words."],
    ["Read https://consequenceforum.org/submissions before sending.",
     "Submit through the online form; translations and visual art are read year-round.",
     "Send during the spring (15 January to 15 April) or fall (15 July to 15 October) "
     "reading period.",
     "Poetry: up to three poems per submission.",
     "Reviews: pitch first to reviews@consequenceforum.org.",
     "Translations carry additional requirements on the submission platform."],
    "Not stated on the guidelines page.",
    ["Read https://consequenceforum.org/submissions before sending.",
     "Submit through the portal during a reading period - the fall window runs 15 "
     "July to 15 October and the spring window 15 January to 15 April.",
     "Translations and visual art can be sent at any time of year.",
     "Pitch reviews to reviews@consequenceforum.org.",
     "Do not send work made with AI in any part."],
    ["consequence", "$20 per poem", "$150 art spread", "print and online rates",
     "substack", "war and culture", "no ai", "submittable",
     "january and july reading periods"],
    "not-stated", None))

NEW.append(rec(
    "fahmidan-journal", "Fahmidan Journal",
    "Poetry, prose and flash: $35 per piece, paid on publication",
    "Fahmidan Journal: $35 per piece, four reading windows a year",
    "Fahmidan Journal pays $35 for every piece it publishes, delivered on publication, "
    "and has paid that since Issue 24 in September 2025. It reads in four seasonal "
    "windows and offers free submission slots alongside paid ones. It buys first "
    "British serial, anthology and audio rights, encourages simultaneous work, and "
    "refuses AI-generated writing.",
    "https://fahmidan.net/journal-submissions",
    "https://fahmidan.net/journal-submissions", None,
    "Online form through Submittable only; email submissions are ignored.",
    src("Fahmidan Journal - Submissions (official)",
        "https://fahmidan.net/journal-submissions"),
    intl("Official page: no country restriction stated. Submitters must be at least "
         "18 years old, and present or past staff of Fahmidan Journal or its parent "
         "are barred from submitting."),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, prose and flash",
    pay("USD", 35, 35, "$35 per published piece",
        "Official page: \"Payment is $35 per piece, delivered on publication.\" And: "
        "\"Fahmidan has increased Contributor pay to $35 from Issue 24 (as of Sept "
        "2025).\" The page points to Submittable for submission and feedback prices; "
        "no fee amount is stated here.",
        "On publication"),
    {"min": None, "max": 2500,
     "display": "Poetry: up to 7 poems (3 on a free submission) of no more than 3 A4 "
                "pages each. Prose: one piece of 1,000-2,500 words. Flash: up to 5 "
                "pieces (2 free) of no more than 800 words each."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Four reading windows a year: 16 December to 14 March for the summer "
                "issue, 15 March to 15 June for autumn, 16 June to 14 September for "
                "winter, and 15 September to 15 December for spring",
     "openingDate": "2026-09-15", "windowEnd": "2026-12-15", "recurring": True},
    "prohibited",
    ["Thought-provoking work on existentialism, phobias and dark moments, in whatever "
     "form suits it.",
     "Poetry, prose and flash, with free submission slots in each category.",
     "Work that takes risks: the page asks for writing that entrances it."],
    ["AI-generated work: \"We do not accept submissions of AI-generated work.\"",
     "Any identifying information on the document itself.",
     "Email submissions, which are ignored.",
     "Work that is offensive or presents hatred or prejudice against a race, "
     "sexuality, gender, ethnicity, ability or socioeconomic group.",
     "More than one submission per category at a time.",
     "Submissions from present or past staff of Fahmidan Journal or its parent."],
    ["Read https://fahmidan.net/journal-submissions before sending.",
     "Submit through Submittable only; email submissions are ignored.",
     "Send Word documents with no name or identifying information in the document.",
     "Poetry: up to 7 poems on a paid submission, 3 on a free one.",
     "Prose: one piece of 1,000-2,500 words; flash: up to 5 pieces of 800 words or "
     "fewer, 2 on a free submission.",
     "You must be at least 18 to submit.",
     "Send an updated document through Submittable messages rather than withdrawing "
     "and resubmitting."],
    "Fahmidan purchases First British Serial Rights, First Anthology and First Audio "
    "rights, and the right to archive the work on its open-access platforms after "
    "publication.",
    ["Read https://fahmidan.net/journal-submissions before sending.",
     "Submit through Submittable during a reading window or a themed call.",
     "Keep identifying information off the document itself.",
     "Check the Submittable page for the current submission prices and the free "
     "slots.",
     "Stay within the category limits: 7 poems, one 1,000-2,500 word prose piece, or "
     "5 flashes."],
    ["fahmidan journal", "$35 per piece", "paid on publication",
     "first british serial rights", "no ai", "submittable", "18 plus",
     "seasonal reading windows", "simultaneous submissions"],
    "accepted",
    "Simultaneous submissions are encouraged! Just message us on Submittable if you "
    "need to withdraw a piece at any point! "
    f"— https://fahmidan.net/journal-submissions (read {READ})"))

NEW.append(rec(
    "first-line", "The First Line",
    "Fiction $25-$50, nonfiction $25 and poetry $10 - and no fee, ever",
    "The First Line: $25-$50 fiction, $10-$25 other, no submission fee",
    "The First Line pays $10 for a poem, $25 for a nonfiction essay and $25 to $50 for "
    "a story, plus a copy of the issue, and states flatly that it will never charge a "
    "submission fee. Every piece must begin with the first line the magazine supplies, "
    "stories run 300 to 5,000 words, and it does not accept simultaneous submissions - "
    "one of the few markets on this desk that says so outright.",
    "https://thefirstline.com/submission.htm",
    "https://thefirstline.com/submission.htm", None,
    "Email or postal submission; the page asks for MS Word or WordPerfect attachments.",
    src("The First Line - Submissions (official)",
        "https://thefirstline.com/submission.htm"),
    intl(),
    ["fiction", "poetry", "essays", "creative-nonfiction"],
    "Short fiction, poetry and critical essays",
    pay("USD", 10, 50,
        "$10 per poem, $25 per nonfiction essay, $25-$50 per story, plus a copy of "
        "the issue",
        "Official page: \"We pay on publication: $25.00 - $50.00 for fiction, $10.00 "
        "for poetry, and $25.00 for nonfiction (all U.S. dollars). We also send you a "
        "copy of the issue in which your piece appears.\" And on fees: \"We do not - "
        "nor will we ever - charge a submission fee.\"",
        "On publication, with the contributor copy"),
    {"min": 300, "max": 5000,
     "display": "Fiction: 300-5,000 words. Nonfiction: critical essays of 500-800 "
                "words. Poetry: no line limit, but rare."},
    {"label": "Four to five weeks after the deadline", "band": "1-3-months",
     "official": True},
    "open",
    {"display": "Quarterly deadlines on 1 February, 1 May, 1 August and 1 November; "
                "the next is 1 November 2026",
     "openingDate": "2026-08-01", "windowEnd": "2026-11-01", "recurring": True},
    "prohibited",
    ["Stories written to the first line supplied for the coming issue, in any genre.",
     "Critical essays of 500-800 words on a favourite first line from a literary work.",
     "Poetry, rarely, with no restriction on form or line count.",
     "Work that cannot be taken out of context and dropped into another magazine."],
    ["Simultaneous submissions: \"just to be clear, we do not accept simultaneous "
     "submissions.\"",
     "Previously published work, including a story that already ran with a new first "
     "line added.",
     "Work generated or co-written by AI: submissions found to be AI-generated are "
     "disqualified.",
     "Altering the supplied first line in any way.",
     "More than one story or poem in the same issue."],
    ["Read https://thefirstline.com/submission.htm before sending.",
     "Write to the first line supplied for the issue you are entering; it cannot be "
     "altered.",
     "Fiction runs 300-5,000 words; nonfiction essays run 500-800 words.",
     "Include a two- to three-sentence biography.",
     "Send by email or post as an MS Word or WordPerfect document; there is no "
     "submission fee.",
     "Submit once per issue against the 1 February, 1 May, 1 August or 1 November "
     "deadline."],
    "Not stated on the guidelines page.",
    ["Read https://thefirstline.com/submission.htm for the current issue's first "
     "line - every piece must start with it.",
     "Send the piece by the quarterly deadline: 1 February, 1 May, 1 August or 1 "
     "November.",
     "Use the first line unchanged, and do not send simultaneous submissions.",
     "Include a two- to three-sentence biography.",
     "There is no submission fee to pay."],
    ["the first line", "$25 to $50 fiction", "$10 poetry", "no submission fee",
     "first line prompt", "quarterly deadlines", "no simultaneous submissions",
     "blue cubicle"],
    "not-accepted",
    "There are, however, literary magazines that run traditional contests, where they "
    "charge entry fees and rank the winners. We do not - nor will we ever - charge a "
    "submission fee, nor do we rank our stories in order of importance. And, just to "
    "be clear, we do not accept simultaneous submissions. "
    f"— https://thefirstline.com/submission.htm (read {READ})"))

NEW.append(rec(
    "free-the-verse", "Free the Verse",
    "Poetry: $10 for issue poems, $20 for annotated Marginalia drafts",
    "Free the Verse: $10 a poem, $20 for Marginalia, free to submit",
    "Free the Verse pays $10 for a poem in its themed quarterly issue and $20 for a "
    "Marginalia piece that annotates a poem's first and final drafts. Both routes are "
    "free to submit, and the issue deadline is 25 November 2026 while Marginalia is "
    "always open. The page states no policy on rights, AI or eligibility.",
    "https://free-the-verse.com/poetry-submissions",
    "https://free-the-verse.com/poetry-submissions", None,
    "Online form linked from the submissions page.",
    src("Free the Verse - Poetry submissions (official)",
        "https://free-the-verse.com/poetry-submissions"),
    intl(),
    ["poetry"],
    "Poetry, including annotated draft essays",
    pay("USD", 10, 20,
        "$10 per poem for the themed quarterly issue; $20 for a Marginalia piece",
        "Official page, by route: issue submissions - \"What we pay / USD $10 / Free "
        "submissions / Yes / Deadline / 25 November 2026\"; Marginalia - \"What we "
        "pay / USD $20 / Free submissions / Yes / Deadline / Always open\".",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No word or line limit stated. Each issue publishes 10-12 poems "
                "around a theme; Marginalia takes a first and final draft with "
                "annotations."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Issue submissions close 25 November 2026 for the next themed "
                "quarterly issue; Marginalia is always open",
     "windowEnd": "2026-11-25", "recurring": True},
    "not-stated",
    ["Poems on the theme announced for the coming quarterly issue - 10 to 12 poems "
     "are published each quarter.",
     "Marginalia pieces: a first and final draft of one poem with annotations "
     "explaining the edits.",
     "Poems that work with the annotation format, which the magazine shapes into an "
     "article."],
    ["Work outside the announced theme for an issue submission.",
     "An unannotated draft for Marginalia, which exists to show the editing."],
    ["Read https://free-the-verse.com/poetry-submissions before sending.",
     "Choose the route: a themed issue poem by 25 November 2026, or a Marginalia "
     "piece at any time.",
     "For Marginalia, send the first and final drafts with annotations on the edits.",
     "No submission fee applies on either route."],
    "Not stated on the guidelines page.",
    ["Read https://free-the-verse.com/poetry-submissions before sending.",
     "Submit through the form linked on the page - there is no charge.",
     "Send a poem to the next quarterly issue before 25 November 2026, or a "
     "Marginalia draft pair at any time.",
     "Check the theme for the issue you are entering."],
    ["free the verse", "$10 per poem", "$20 marginalia", "free submissions",
     "themed quarterly issue", "poetry submissions", "annotated drafts"],
    "not-stated", None))

NEW.append(rec(
    "invisible-city", "Invisible City",
    "Poetry, prose and flash: $20 per published piece",
    "Invisible City: $20 per piece, open now, 5,000-word prose limit",
    "Invisible City pays a $20 honorarium for every published piece, with international "
    "contributors paid by wire transfer. Submissions are open: up to three poems, three "
    "flash pieces under 1,000 words each, or prose up to 5,000 words. Only unpublished "
    "work is considered, simultaneous submissions are accepted with notice, and current "
    "University of San Francisco students are excluded.",
    "https://invisiblecitylit.com/submissions",
    "https://invisiblecitylit.com/submissions", None,
    "Online submission manager only; email and postal submissions are not accepted.",
    src("Invisible City - Submissions (official)",
        "https://invisiblecitylit.com/submissions"),
    worldwide("Official page: honorariums to an international address are paid by "
              "wire transfer, and the page sets out no country restriction. Current "
              "University of San Francisco students are excluded; alumni may submit."),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, prose, flash and visual art",
    pay("USD", 20, 20, "$20 honorarium per published piece",
        "Official page: \"We compensate our contributors with a $20 honorarium per "
        "published piece.\" And, on paying from abroad: \"All honorariums associated "
        "with an international address will be made by wire transfer.\"",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "Prose up to 5,000 words; flash under 1,000 words, up to three pieces; "
                "poetry up to three poems. No novel excerpts unless they stand alone."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Writing and visual art that asks readers to see the world from a new "
     "perspective or angle.",
     "Poetry: up to three poems.",
     "Prose up to 5,000 words, or up to three flash pieces of under 1,000 words each.",
     "Art in PDF or PNG, scanned rather than photographed, on a rolling basis."],
    ["Previously published work - \"No exceptions.\"",
     "Novel excerpts, unless they function as stand-alone stories.",
     "Email or postal submissions, which are not accepted.",
     "Art photographed on a smartphone rather than scanned.",
     "Work from current University of San Francisco students; alumni may submit.",
     "A new writing submission within three reading cycles of a publication."],
    ["Read https://invisiblecitylit.com/submissions before sending.",
     "Submit through the submission manager; email and post are not accepted.",
     "Poetry: no more than three poems. Prose: one piece up to 5,000 words, or up to "
     "three flash pieces under 1,000 words.",
     "Include content warnings where they apply.",
     "Art goes as a PDF or PNG, or a ZIP of multiple pieces; scan physical work "
     "rather than photographing it.",
     "If published, wait three reading cycles before submitting writing again."],
    "Not stated on the guidelines page.",
    ["Read https://invisiblecitylit.com/submissions before sending.",
     "Submit through the submission manager, which is open now.",
     "Send up to three poems, up to three flashes, or one prose piece of up to 5,000 "
     "words.",
     "Include content warnings where they apply.",
     "Tell the editors promptly if a simultaneous piece is accepted elsewhere."],
    ["invisible city", "$20 honorarium", "university of san francisco",
     "flash fiction", "poetry submissions", "simultaneous submissions",
     "wire transfer for international writers"],
    "accepted",
    "We do accept simultaneous submissions. However, we ask that you notify us as "
    "soon as possible if your work is accepted elsewhere. "
    f"— https://invisiblecitylit.com/submissions (read {READ})"))

NEW.append(rec(
    "fairy-tale-review", "Fairy Tale Review",
    "Poetry, fiction and nonfiction: $50 honorarium and two copies",
    "Fairy Tale Review: $50 honorarium and two copies per contributor",
    "Fairy Tale Review pays a $50 honorarium and sends two copies of the issue to each "
    "contributor. It reads 15 March to 15 July - the Volume 22 window ran in 2025 and "
    "no future window is stated - and welcomes simultaneous submissions. It publishes "
    "unpublished fiction, nonfiction, poetry, translation and up to five artwork "
    "images per portfolio.",
    "https://fairytalereview.com/submit", "https://fairytalereview.com/submit",
    None, "Online form linked from the submissions page.",
    src("Fairy Tale Review - Submissions (official)",
        "https://fairytalereview.com/submit"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction", "translation"],
    "Fiction, nonfiction, poetry, translation and artwork",
    pay("USD", 50, 50, "$50 honorarium and two copies of the issue per contributor",
        "Official page: \"Contributors will receive two (2) copies of the issue and a "
        "$50 honorarium upon publication.\"",
        "On publication"),
    {"min": None, "max": None,
     "display": "No word limit stated. Artwork: up to five high-resolution images in "
                "a single portfolio."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "closed",
    {"display": "Submissions for Volume 22 were accepted 15 March 2025 to 15 July "
                "2025; Volume 22 was published in Spring 2026 and no later window is "
                "stated on the page",
     "openingDate": "2025-03-15", "windowEnd": "2025-07-15"},
    "not-stated",
    ["Unpublished manuscripts in all forms and styles, guided by the writer's own "
     "artistic direction.",
     "Fiction, nonfiction and poetry.",
     "Translations into English of fiction, nonfiction and poetry, with the "
     "translator's note and permissions.",
     "Up to five high-resolution artwork images in a single portfolio."],
    ["Previously published work: the page invites \"unpublished manuscripts\".",
     "Artwork that does not convey the fairy-tale register the journal describes."],
    ["Read https://fairytalereview.com/submit before sending.",
     "Submit through the form on the page during a reading window; the Volume 22 "
     "window ran 15 March to 15 July 2025.",
     "Translations must include the translator's note and any permissions.",
     "Artwork: up to five high-resolution images in one portfolio."],
    "Not stated on the guidelines page.",
    ["Read https://fairytalereview.com/submit before sending.",
     "Watch for the next reading window: the last one ran 15 March to 15 July, and "
     "no later window is announced on the page.",
     "Send unpublished fiction, nonfiction or poetry, or a translation with its "
     "permissions.",
     "Artwork goes as up to five high-resolution images in a single portfolio."],
    ["fairy tale review", "$50 honorarium", "two contributor copies",
     "kate bernheimer", "fairy tales", "university of alabama press",
     "simultaneous submissions", "translation"],
    "accepted",
    "Simultaneous submissions are welcome (and we welcome your disclosure if you are "
    "sending your work out simultaneously). "
    f"— https://fairytalereview.com/submit (read {READ})"))


BASE = {
    "booth": ("US", "United States"),
    "chicago-review-of-books": ("US", "United States"),
    "consequence": ("", "International"),
    "fahmidan-journal": ("UK", "United Kingdom"),
    "first-line": ("", "International"),
    "free-the-verse": ("", "International"),
    "invisible-city": ("US", "United States"),
    "fairy-tale-review": ("", "International"),
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
        # A zero is a figure that was never read off a page. Batch 4 shipped one
        # and it had to be found and removed; here it cannot be written.
        if p["amountMin"] == 0 or p["amountMax"] == 0:
            sys.exit(f"ERROR: {r['slug']} has a zero pay amount")
        if p["amountMin"] is not None and p["amountMax"] is not None \
                and p["amountMin"] > p["amountMax"]:
            sys.exit(f"ERROR: {r['slug']} pay range inverted")
        if p["amountMin"] is None and p["amountMax"] is not None:
            sys.exit(f"ERROR: {r['slug']} has a maximum but no minimum")
        for k in ("officialUrl", "excerpt", "seoTitle", "howToSubmit", "whatTheyWant"):
            if not r.get(k):
                sys.exit(f"ERROR: {r['slug']} missing {k}")
        # deadline is a structured object in this dataset (display/date/
        # openingDate/windowStart/windowEnd/recurring), never a bare string.
        # build-writing-first.py's deadline_passed() calls .get() on it, so a
        # string crashes the build. Batch 13 shipped three string deadlines and
        # the build caught them; this guard is why they cannot come back.
        dl = r["deadline"]
        if dl is not None:
            if not isinstance(dl, dict):
                sys.exit(f"ERROR: {r['slug']} deadline must be a dict or None, "
                         f"got {type(dl).__name__}")
            if not dl.get("display"):
                sys.exit(f"ERROR: {r['slug']} deadline has no display text")
            if not any(k in dl for k in ("date", "openingDate", "windowEnd")):
                sys.exit(f"ERROR: {r['slug']} deadline records no date of any kind")
        if r["simultaneousSubmissions"] not in ("accepted", "not-accepted", "not-stated"):
            sys.exit(f"ERROR: {r['slug']} bad simultaneous value")
        if r["simultaneousSubmissions"] == "not-stated" and r["simultaneousNote"]:
            sys.exit(f"ERROR: {r['slug']} has a note but says not-stated")
        if r["simultaneousSubmissions"] != "not-stated" and not r["simultaneousNote"]:
            sys.exit(f"ERROR: {r['slug']} states a policy with no sentence recorded")
        # Every policy note in this dataset is a verbatim sentence plus its source
        # and the date it was read. The date must be the desk date of THIS batch.
        if r["simultaneousNote"] and f"(read {READ})" not in r["simultaneousNote"]:
            sys.exit(f"ERROR: {r['slug']} simultaneous note carries no read date")
        # The pay display must never be a fee dressed as a rate.
        for word in ("fee", "entry", "Fast Pass"):
            if word.lower() in (p["display"] or "").lower():
                sys.exit(f"ERROR: {r['slug']} pay display mentions '{word}' - "
                         f"a writer's cost is not a rate")

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
# Read in this batch and HELD BACK, with the reason. Held is not the same as
# rejected: most of these are real markets that pay nothing, and the index policy
# for this desk is research-backed PAID opportunities.
#
#   apricity_press        "There is no submissions fee, nor is there any payment
#       for publishing your work (currently)." Unpaid. (The $5 option buys a
#       one-week response; it is a writer's cost, not a rate.)
#   amsterdam_review      "We are unable to offer paid compensation for accepted
#       submissions at present." Unpaid.
#   after_brunch_journal  "volunteer-based, so unfortunately we are not able to
#       offer payment to our contributors at this time". Unpaid.
#   appalachia            "We have a very limited budget and cannot pay for most
#       unsolicited material. Authors receive two contributor copies." Mostly
#       unpaid; the rest of the page's payment language is subscription billing.
#   aaduna                "aaduna does not provide publishing honorarium nor
#       charges any fee". Unpaid, as batch 13 already recorded.
#   atlantic_northeast    "right now we are unable to pay contributors for their
#       work." Unpaid.
#   autumn_sky_poetry_daily  "There is no payment for contributors." Unpaid.
#   acorn_review          $5 reading fee, no contributor rate stated on the page.
#   allium_a_journal_of_poetry_prose  $3.00 reading fee, window opens 13 November
#       2026; no contributor rate stated on the page.
#   alaska_quarterly_review  "The fee is $3." No contributor rate stated.
#   anomaly (ANMLY)       $3 submission fee with a hardship waiver; no contributor
#       rate stated.
#   arkana                The $50 figures are Editors' Choice Awards and an
#       Arkansas Writers prize. A prize is not a rate for published work - the
#       StoryQuarterly precedent from batch 12.
#   bacopa_literary_review  $2 submission fee and cash awards by category. Contest
#       money, not a contributor rate.
#   acdc_a_journal_for_the_bent  $5 tip jar buys a faster response. A writer's
#       cost, and no rate is stated.
#   antiphony             The only "$" strings on the page are Squarespace
#       newsletter-template boilerplate. No contributor rate found.
#   aura_literary_arts_review  The $10/$15/$25/$50 figures are donation buttons.
#
# Read later in the run and not yet classified when this batch shipped: the queue
# continues under research/rebuild/ with scripts/read-pw-candidates.py.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    raise SystemExit(main())
