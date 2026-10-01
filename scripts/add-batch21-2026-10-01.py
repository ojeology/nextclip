"""Add verified writing-market batch 21 (2026-10-01).

Seven NEW markets, read off each publication's OWN guidelines page on 2026-10-01.
Raw text under research/rebuild/raw/<slug>.txt.

WHY THIS BATCH EXISTS AFTER BATCH 20 SAID THE PASS WAS FINISHED
--------------------------------------------------------------
Batch 20 concluded the queue was read out. It was not - the triage net was too
narrow. It looked for "we pay", "pays $", "payment of $", "honorarium" and unit
rates, and missed every market that states pay in another shape:

    Idaho Review      "we ... pay contributors $300 for short stories"
    Berkeley Fiction  "we now offer a $25 payment for accepted stories"
    Blue Marble       "Contributors ... will receive $30 per published piece"
    Claudine          "Pay is $25 upon publication"
    HEART             "PAY: $25 upon publication"
    Ink In Thirds     "Our current payment is $5 USD per contributor"
    F(r)iction        "Payment / $25 per final printed page"

A looser pass - any dollar figure in a sentence that also mentions paying,
contributors, writers or publication - found 21 pages, of which these seven
state a contributor rate and the rest are prizes, fees or revenue shares. The
lesson is recorded in the commit that added this batch: a payment filter that
matches only one grammatical shape will report an empty queue long before the
queue is empty.

THE FIGURES THAT ARE NOT RATES
------------------------------
  * Idaho Review's "There is no entry fee" is a cost statement, not pay - and
    the rate for creative nonfiction is not stated, so no figure is recorded
    for it even though the story and poem rates are.
  * F(r)iction charges $2.50 a submission and says the reading fees fund
    contributor payment. The fee is the writer's cost.
  * HEART's $500 is the HEART Poetry Award - an outcome.
  * Blue Marble pays $75 for cover art against $30 a published piece: two
    routes, both quoted.
  * Ink In Thirds pays per contributor, not per piece, with a stated $3 floor.

ELIGIBILITY THAT IS AN AGE LIMIT, NOT A COUNTRY ONE
---------------------------------------------------
Blue Marble Review states "We welcome submissions from students ages 13-22."
That is recorded as mode "restricted" with the reason spelled out in the
summary, so it is not mistaken for a nationality bar.
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
    "idaho-review", "The Idaho Review",
    "Short stories: $300; poems: $75 each - plus two copies, no entry fee",
    "The Idaho Review: $300 a story, $75 a poem, no entry fee",
    "The Idaho Review pays $300 for a short story and $75 for each accepted poem, "
    "sends two copies of the print issue, and charges no entry fee. It reads 8 "
    "September to 15 November, most stories run under 25 double-spaced pages, and "
    "simultaneous submissions are accepted with immediate withdrawal. It buys first "
    "worldwide serial rights and states nothing about AI; the nonfiction rate is not "
    "stated on the page.",
    "https://idahoreview.org/submit", "https://idahoreview.org/submit",
    None, "Online through Submittable; post is accepted only from incarcerated "
          "writers or writers with accessibility needs.",
    src("The Idaho Review - Submissions (official)", "https://idahoreview.org/submit"),
    intl(),
    ["fiction", "poetry", "creative-nonfiction"],
    "Short fiction, poetry and creative nonfiction",
    pay("USD", 75, 300,
        "$300 per short story, $75 per accepted poem, plus two contributor copies",
        "Official page: \"We buy first worldwide serial rights and pay contributors "
        "$300 for short stories and $75 for each accepted poem. In addition, we send "
        "two copies of the print publication to contributing authors.\" The page's "
        "FAQ states \"There is no entry fee.\" The rate for creative nonfiction is "
        "not stated, so no figure is recorded for it.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No designated page limit, though most stories published run under "
                "25 double-spaced pages; the page asks for one submission per "
                "reading period"},
    {"label": "Six months or less", "band": "3-plus-months", "official": True},
    "open",
    {"display": "Reading period 8 September to 15 November; the journal may close "
                "early on volume or reopen in winter or spring",
     "openingDate": "2026-09-08", "windowEnd": "2026-11-15", "recurring": True},
    "not-stated",
    ["Short stories, with most published pieces running under 25 double-spaced pages.",
     "Poetry, paid per accepted poem.",
     "Creative nonfiction of all kinds - the page says it is open to publishing all "
     "different kinds.",
     "Work sent during the 8 September to 15 November reading period."],
    ["More than one submission per reading period, unless the editors ask for more.",
     "Mailed submissions, except from incarcerated writers or writers with "
     "accessibility needs that require post.",
     "Simultaneous work that is accepted elsewhere without immediate withdrawal."],
    ["Read https://idahoreview.org/submit before sending.",
     "Submit through Submittable during the reading period that runs 8 September to "
     "15 November; the journal may close early on volume.",
     "Indicate the genre in the cover letter, and send one submission per reading "
     "period.",
     "Withdraw immediately if a simultaneous piece is accepted elsewhere.",
     "There is no entry fee."],
    "First worldwide serial rights are bought on acceptance; the page states no "
    "other rights position.",
    ["Read https://idahoreview.org/submit before sending.",
     "Submit once during the 8 September to 15 November window, through Submittable.",
     "Say which genre the piece is in, in the cover letter.",
     "Note the pay: $300 a story and $75 a poem, with two copies and no fee."],
    ["idaho review", "$300 per story", "$75 per poem", "no entry fee",
     "boise state university", "first worldwide serial rights",
     "simultaneous submissions", "september reading period", "submittable"],
    "accepted",
    "Yes. If your submission is accepted elsewhere, please immediately withdraw it "
    "from consideration for publication in Idaho Review. "
    f"— https://idahoreview.org/submit (read {READ})"))

NEW.append(rec(
    "friction", "F(r)iction",
    "Fiction, nonfiction and poetry: $25 per final printed page plus copies",
    "F(r)iction: $25 per printed page, $2.50 to submit, no AI",
    "F(r)iction pays $25 per final printed page and sends two free contributor copies, "
    "with a $2.50 charge per submission that the magazine says goes toward paying its "
    "contributors. It takes short fiction of 1,001-7,500 words, creative nonfiction up "
    "to 6,500, flash of 1,000 words or fewer, poetry, and reviews of 500-1,000 words. "
    "Simultaneous submissions are accepted with withdrawal, AI work is refused, and "
    "rights revert to the author on publication.",
    "https://frictionlit.org/about/submit", "https://frictionlit.org/about/submit",
    None, "Online form through Submittable; separate portals for the journal, the "
          "Log and contests.",
    src("F(r)iction - Submit (official)", "https://frictionlit.org/about/submit"),
    intl("Official page: no country restriction stated. The magazine is published by "
         "Brink Literacy Project, which the page names without stating where it is "
         "based."),
    ["fiction", "creative-nonfiction", "poetry", "reviews"],
    "Short fiction, creative nonfiction, flash, poetry and reviews",
    pay("USD", 25, 25,
        "$25 per final printed page, plus two free contributor copies",
        "Official page, F(r)iction Series: \"Payment / $25 per final printed page and "
        "two free contributor's copies.\" The same card states \"Price / $2.50 per "
        "submission\", and the page explains: \"100% of our reading fees go toward "
        "paying the contributors who are printed in our[ magazine]\". The fee is the "
        "writer's cost and is not part of the rate.",
        "Not publicly stated"),
    {"min": None, "max": 7500,
     "display": "Short fiction 1,001-7,500 words; creative nonfiction up to 6,500 "
                "words; flash fiction 1,000 words or fewer, up to three pieces in a "
                "three-pack; reviews 500 words preferred, up to 1,000"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Short fiction, creative nonfiction, flash fiction and poetry, regardless of "
     "genre, style or origin.",
     "Reviews of books and literary journals of 500-1,000 words.",
     "Work by writers who opt in to having their details shared with the magazine's "
     "partner literary agents.",
     "As many pieces as a writer likes - the page says to submit as many as you would "
     "like."],
    ["Work from artificial intelligence generators or similar: \"No AI submissions\".",
     "Prose outside the stated limits - fiction under 1,001 words belongs in flash, "
     "and nonfiction over 6,500 words is out of scope.",
     "Simultaneous work that is selected elsewhere without withdrawing it."],
    ["Read https://frictionlit.org/about/submit and the formatting guidelines before "
     "sending.",
     "Submit through the correct portal: the F(r)iction Series portal is for journal "
     "submissions only, and contests have their own.",
     "Pay the $2.50 per-submission charge, which the magazine says funds contributor "
     "payment.",
     "Keep to the genre limits, and choose the three-pack for up to three flash "
     "pieces.",
     "Withdraw immediately through Submittable if a simultaneous piece is selected "
     "elsewhere."],
    "F(r)iction retains first publishing rights on works published in print or online, "
    "and publishing rights revert to the author upon publication.",
    ["Read https://frictionlit.org/about/submit before sending.",
     "Submit through the F(r)iction Series portal; contests and the Log use their own.",
     "Keep fiction between 1,001 and 7,500 words, nonfiction under 6,500, and flash "
     "under 1,000 - three to a three-pack.",
     "Withdraw at once if a simultaneous piece is selected elsewhere.",
     "Note the $2.50 submission charge and the $25 per printed page rate."],
    ["friction", "f(r)iction", "$25 per printed page", "$2.50 submission fee",
     "brink literacy project", "no ai", "flash fiction",
     "simultaneous submissions", "submittable"],
    "accepted",
    "Simultaneous submissions are accepted, but please notify us immediately by "
    "choosing \"withdraw\" in Submittable if your work is selected for publication "
    "elsewhere. "
    f"— https://frictionlit.org/about/submit (read {READ})"))

NEW.append(rec(
    "berkeley-fiction-review", "Berkeley Fiction Review",
    "Short fiction: $25 per accepted story, and no submission fees ever",
    "Berkeley Fiction Review: $25 a story, free to submit, worldwide",
    "Berkeley Fiction Review pays $25 for each accepted story and sends a "
    "complimentary copy of the issue, and states that it does not charge submission "
    "fees. It reads previously unpublished short fiction from around the world "
    "year-round, publishes annually, encourages simultaneous submissions, and asks "
    "for content warnings where they apply. Responses take eight months to a year, "
    "and the page states no AI policy.",
    "https://berkeleyfictionreview.org/submit/short-fiction",
    "https://berkeleyfictionreview.org/submit/short-fiction", None,
    "Online through the review's submission manager.",
    src("Berkeley Fiction Review - Short fiction submissions (official)",
        "https://berkeleyfictionreview.org/submit/short-fiction"),
    worldwide("Official page: \"We invite submissions of previously unpublished short "
              "stories from around the country and the world year-round.\""),
    ["fiction"],
    "Short fiction",
    pay("USD", 25, 25,
        "$25 per accepted story, plus a complimentary copy of the issue",
        "Official page: \"On that note, we now offer a $25 payment for accepted "
        "stories and continue to offer a complimentary copy of the Issue in which "
        "your story appears.\" And on cost: \"Unlike the majority of literary "
        "journals, we do not charge submission fees in the hopes that we can provide "
        "an opportunity for all authors, regardless of economic circumstances.\"",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No word limit stated; the review publishes one annual issue of "
                "short fiction"},
    {"label": "Eight months to a year", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Previously unpublished short fiction of any kind.",
     "Stories that provoke a visceral reaction in the reader - the page names joy, "
     "fear, and the solace of being seen and understood.",
     "Work from anywhere in the world; there is no country restriction."],
    ["Previously published stories.",
     "Work without a content warning where the material demands one - warnings do not "
     "affect the review process, but the page asks for them."],
    ["Read https://berkeleyfictionreview.org/submit/short-fiction before sending.",
     "Submit through the review's submission manager; there is no fee.",
     "Include content warnings where the story contains particularly sensitive "
     "material.",
     "Expect eight months to a year for a response, and note that the journal runs as "
     "a class, so submissions can sit between semesters."],
    "Not stated on the submissions page.",
    ["Read https://berkeleyfictionreview.org/submit/short-fiction before sending.",
     "Submit year-round through the submission manager - submissions are free.",
     "Send one previously unpublished story, with content warnings where needed.",
     "Expect a long wait: eight months to a year, with the journal's schedule set by "
     "the academic calendar."],
    ["berkeley fiction review", "$25 per story", "no submission fees",
     "university of california", "short fiction", "worldwide",
     "simultaneous submissions", "annual issue"],
    "accepted",
    "Simultaneous submissions are encouraged. "
    f"— https://berkeleyfictionreview.org/submit/short-fiction (read {READ})"))

NEW.append(rec(
    "blue-marble-review", "Blue Marble Review",
    "Poetry, prose and art: $30 per published piece, $75 for cover art",
    "Blue Marble Review: $30 a piece, $75 cover art, students 13-22",
    "Blue Marble Review pays $30 for each piece published online and $75 for cover "
    "art, and is open to students aged 13 to 22 - an age limit, not a country one. It "
    "publishes poetry, fiction, nonfiction, essays, opinion and travel writing up to "
    "1,500 words, up to three pieces per submission, on a rolling basis four times a "
    "year. It takes First Serial Rights and the right to archive; it states nothing "
    "on fees, AI or response times.",
    "https://bluemarblereview.com/submit", "https://bluemarblereview.com/submit",
    None, "Online through the review's submission form.",
    src("Blue Marble Review - Submit (official)", "https://bluemarblereview.com/submit"),
    {"summary": "Official page: \"We welcome submissions from students ages 13-22.\" "
                "The limit is age, not nationality - no country restriction is "
                "stated.",
     "mode": "restricted", "includesGroups": ["students-13-to-22"],
     "includesRegions": [], "allowsDiaspora": True, "notStated": False},
    ["poetry", "fiction", "creative-nonfiction", "essays", "articles", "reviews"],
    "Poetry, fiction, nonfiction, essays, opinion and travel writing, plus art",
    pay("USD", 30, 75,
        "$30 per published piece; $75 for cover art",
        "Official page, Payment: \"Contributors published online in Blue Marble "
        "Review will receive $30 per published piece, $75 for cover art.\"",
        "Not publicly stated"),
    {"min": None, "max": 1500,
     "display": "Poetry, fiction and all prose forms up to 1,500 words; up to three "
                "pieces per submission; one to two pieces for nonfiction and essays"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Flash fiction, short stories and hybrid forms of 1,500 words or fewer.",
     "Memoir, personal essays, travel adventures, and occasionally a research paper "
     "or book review.",
     "Poetry, with one poem per page.",
     "Photography and art, including cover art, which is paid at a higher rate."],
    ["Prose over 1,500 words.",
     "More than three pieces in one submission.",
     "Submissions from writers outside the stated age range of 13 to 22."],
    ["Read https://bluemarblereview.com/submit before sending.",
     "Submit up to three pieces, each within 1,500 words.",
     "Attach prose as a single double-spaced Word document; poetry may be "
     "single-spaced with one poem per page.",
     "Include page numbers on fiction and nonfiction.",
     "Note the age range: submissions are welcome from students aged 13 to 22."],
    "Submitting grants Blue Marble Review First Serial Rights and the right to "
    "archive the work on its site; copyright stays with the contributor.",
    ["Read https://bluemarblereview.com/submit before sending.",
     "Submit through the form; the review reads on a rolling basis four times a year.",
     "Send up to three pieces of 1,500 words or fewer, in a double-spaced Word "
     "document for prose.",
     "Confirm you are within the stated age range of 13 to 22."],
    ["blue marble review", "$30 per piece", "$75 cover art", "students 13-22",
     "young writers", "flash fiction", "first serial rights",
     "rolling submissions"],
    "not-stated", None))

NEW.append(rec(
    "claudine", "Claudine",
    "Microfiction and micro nonfiction: $25 on publication, free to submit",
    "Claudine: $25 per micro, 400 words max, free and no AI",
    "Claudine pays $25 on publication for microfiction and micro creative nonfiction "
    "of up to 400 words, and submissions are always free. It reads January through "
    "November, welcomes simultaneous submissions with prompt withdrawal, acquires "
    "first serial rights worldwide in English and non-exclusive anthology rights, and "
    "refuses AI-generated or AI-assisted work, which it runs through a third-party "
    "checker.",
    "https://claudineliterary.net/general-5",
    "https://claudineliterary.net/general-5", None,
    "Email; the cover letter and bio go in the body and the piece is attached as a "
    "Word document.",
    src("Claudine - General submissions (official)",
        "https://claudineliterary.net/general-5"),
    intl(),
    ["fiction", "creative-nonfiction"],
    "Microfiction and micro creative nonfiction",
    pay("USD", 25, 25, "$25 upon publication, per micro piece",
        "Official page, by category: microfiction - \"Pay is $25 upon publication.\"; "
        "micro creative nonfiction - \"Pay is $25 upon publication.\" And on cost: "
        "\"Submissions are always FREE.\"",
        "On publication"),
    {"min": None, "max": 400,
     "display": "Up to 400 words for all categories - a firm count"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Submissions are open January through November; the magazine does not "
                "read in December",
     "windowEnd": "2026-11-30", "recurring": True},
    "prohibited",
    ["Pieces that move and surprise, with stunning prose, thoughtful punctuation "
     "over strict grammar, and innovative form.",
     "Microfiction, which the page marks as mostly made up.",
     "Micro creative nonfiction that stays true to an experience or topic.",
     "New Writer Micros, open to writers with three or fewer published literary "
     "pieces."],
    ["AI-generated or AI-assisted work: \"We want to read what your human self has "
     "written.\" Submissions are run through a third-party checker.",
     "Anything over 400 words - the page calls the count firm.",
     "Submissions during December, when the magazine does not read."],
    ["Read https://claudineliterary.net/general-5 before sending.",
     "Email the piece as a Word document, with the cover letter and bio typed in the "
     "body.",
     "Keep the piece to 400 words or fewer - the count is firm.",
     "Name the piece, the word count and the category in the cover letter.",
     "Withdraw promptly if a simultaneous piece is accepted elsewhere.",
     "There is no submission fee."],
    "Claudine acquires first serial rights worldwide in English and non-exclusive "
    "anthology rights, and asks for the right to display the work.",
    ["Read https://claudineliterary.net/general-5 before sending.",
     "Email the submission with the cover letter and bio in the body of the message.",
     "Send one piece per category of up to 400 words - microfiction, micro creative "
     "nonfiction, or a New Writer Micro if you have three or fewer published pieces.",
     "Send between January and November; December is closed."],
    ["claudine", "$25 upon publication", "400 words", "microfiction",
     "micro creative nonfiction", "free submissions", "no ai",
     "first serial rights", "new writer micros"],
    "accepted",
    "We accept simultaneous submissions; please withdraw your piece promptly if it's "
    "accepted elsewhere. "
    f"— https://claudineliterary.net/general-5 (read {READ})"))

NEW.append(rec(
    "heart", "HEART",
    "Poetry and short prose: $25 on publication",
    "HEART: $25 on publication for poems and short prose",
    "HEART pays $25 on publication, whether the work appears on the site or in the "
    "digital issue, and runs a separate annual HEART Poetry Award of $500. It prefers "
    "modern prose no longer than one page and asks for no more than three poems at a "
    "time. Its submissions page states nothing about fees, rights, windows or AI, and "
    "none is recorded.",
    "https://nostalgiapress.com/submissions/",
    "https://nostalgiapress.com/submissions/", None,
    "Online through the site's contact or submission route as described on the page.",
    src("HEART - General submissions (official)",
        "https://nostalgiapress.com/submissions/"),
    intl("Official page: no country restriction stated; published by Nostalgia Press, "
         "which the page names without stating where it is based."),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry and short prose",
    pay("USD", 25, 25, "$25 upon publication",
        "Official page: \"PAY: $25 upon publication on website and digital copy if "
        "published in issue.\" The HEART Poetry Award is a separate $500 award - an "
        "outcome, not a rate - and is not part of the pay figure.",
        "On publication"),
    {"min": None, "max": None,
     "display": "Prose of no more than one page; no more than three poems at a time"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Modern prose of no longer than one page.",
     "Poetry, up to three poems in a submission.",
     "Work in the register the journal publishes - the page suggests reviewing an "
     "issue or reading the poets featured on the site first.",
     "Submissions for the annual HEART Poetry Award, which carries its own $500."],
    ["Prose longer than one page.",
     "More than three poems in one submission."],
    ["Read https://nostalgiapress.com/submissions/ before sending.",
     "Send no more than three poems at a time, or prose of no more than one page.",
     "Read an issue or the featured poets first - the page says it helps.",
     "Note that payment is $25 on publication, whether on the site or in the digital "
     "issue."],
    "Not stated on the submissions page.",
    ["Read https://nostalgiapress.com/submissions/ before sending.",
     "Send up to three poems, or one page of prose.",
     "Check the current HEART Poetry Award page if entering the award, which is "
     "separate from general submissions."],
    ["heart", "$25 on publication", "heart poetry award", "nostalgia press",
     "short prose", "poetry submissions", "three poems"],
    "not-stated", None))

NEW.append(rec(
    "ink-in-thirds", "Ink In Thirds",
    "Poetry and prose: $5 per contributor, no fees, two reading periods",
    "Ink In Thirds: $5 per contributor, free to submit, no AI",
    "Ink In Thirds pays $5 per contributor, with a floor of $3 should donations fall, "
    "and charges no fees. It takes prose up to 600 words - drabbles, microfiction, "
    "flash - alongside poetry and art, reading 1 April to 31 July and 1 October to 31 "
    "January, with art always open. It acquires exclusive first rights and "
    "non-exclusive archival rights, accepts simultaneous submissions, and refuses AI "
    "created content and previously published work.",
    "https://inkinthirds.org/submissions", "https://inkinthirds.org/submissions",
    None, "Online through the magazine's submission manager.",
    src("Ink In Thirds - Submissions (official)",
        "https://inkinthirds.org/submissions"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, short prose and visual art",
    pay("USD", 5, 5,
        "$5 per contributor, with a stated floor of $3 depending on donations",
        "Official page, Compensation: \"As of 2025, we have now become a paying "
        "market! Our current payment is $5 USD per contributor (it can vary based on "
        "yearly donations but will not be less than $3 per contributor).\" And on "
        "cost: \"No Fees\". Payment is per contributor, not per piece.",
        "Not publicly stated"),
    {"min": None, "max": 600,
     "display": "Prose up to 600 words, one piece per form - including 3-word "
                "stories, 100-word stories, drabbles, microfiction and flash "
                "fiction; poetry and art also accepted"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Two reading periods for poetry and prose: 1 April to 31 July for the "
                "fall/winter issues, and 1 October to 31 January; photography and "
                "visual art are always open",
     "openingDate": "2026-10-01", "windowEnd": "2027-01-31", "recurring": True},
    "prohibited",
    ["Short prose up to 600 words: 3-word stories, 100-word stories, drabbles, "
     "microfiction and flash fiction.",
     "Poetry, in the magazine's stated register of work that makes the reader feel "
     "something.",
     "Photography and visual art, which are read year-round.",
     "Work for either reading period - 1 April to 31 July, or 1 October to 31 "
     "January."],
    ["AI created content.",
     "Previously published work: the page treats anything posted or otherwise made "
     "publicly available online as previously published.",
     "Lewd or graphic images, excessive profanity, or overtly disturbing mental "
     "images in art submissions.",
     "Prose over 600 words."],
    ["Read https://inkinthirds.org/submissions before sending.",
     "Submit during a reading period: 1 April to 31 July or 1 October to 31 January, "
     "with art always open.",
     "Keep prose within 600 words, one piece per form.",
     "There is no fee to submit.",
     "Note the compensation is $5 per contributor, with a $3 floor."],
    "Ink in Thirds acquires exclusive first rights, and maintains non-exclusive "
    "archival rights.",
    ["Read https://inkinthirds.org/submissions before sending.",
     "Submit through the manager during a reading period - the 1 October to 31 "
     "January window is open; art can be sent at any time.",
     "Send up to 600 words of prose, or poetry, and note that the payment is per "
     "contributor rather than per piece.",
     "Do not send anything previously published online, and no AI created content."],
    ["ink in thirds", "$5 per contributor", "no fees", "paying market",
     "600 words", "drabble", "no ai", "exclusive first rights",
     "simultaneous submissions"],
    "accepted",
    "We DO ACCEPT simultaneous submissions. "
    f"— https://inkinthirds.org/submissions (read {READ})"))


BASE = {
    "idaho-review": ("US", "United States"),
    "friction": ("", "International"),
    "berkeley-fiction-review": ("US", "United States"),
    "blue-marble-review": ("", "International"),
    "claudine": ("", "International"),
    "heart": ("", "International"),
    "ink-in-thirds": ("", "International"),
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
