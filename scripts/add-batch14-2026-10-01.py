#!/usr/bin/env python3
"""Add verified writing-market batch 14 (2026-10-01).

Six NEW markets, read off each publication's OWN guidelines page on 2026-10-01.
The raw text of every page is kept under research/rebuild/raw/<slug>.txt so a
reading can be re-checked without re-fetching.

WHY THIS BATCH IS DATED 2026-10-01 AND NOT 2026-09-30
-----------------------------------------------------
The crawl runs on a UTC clock; the desk is in Lagos. The reads happened between
2026-09-30 23:18 UTC and 2026-10-01 00:5x UTC, which is 2026-10-01 00:18-01:5x
West Africa Time - already the next day at the desk. The desk's own local date is
the check date, so every record here carries 2026-10-01, and each raw file is
stamped with both clocks so the evidence cannot look a day stale beside it.

WHERE THESE CANDIDATES CAME FROM
--------------------------------
pw.org's Literary Magazines directory, for names and official submission URLs
only, exactly as in batches 4 and 13:

    detail pages resumed from the batch-13 queue
    -> candidates not already on this desk
    -> each publication's OWN guidelines page fetched and read

pw.org's own pay notes and reading-fee flags were not read and are not used. Every
figure below comes from the publication's own page.

WHAT WAS READ, AND WHAT WAS NOT FLATTENED
-----------------------------------------
Two of the six pay a stated rate for prose and poetry; one pays by length; one
states payment exists but publishes no amount; and every dollar figure that is a
FEE is recorded as a fee, never as pay:

  * American Poetry Journal charges $3.00 to submit - and its own page says the
    fee helps "pay contributors and poet staff". A careless read turns that
    sentence into a rate. It is the writer's money and is recorded as a fee.
  * Bayou Magazine pays $150/$100 for FICTION by length and "one contributor's
    copy unless otherwise specified by genre" for everything else. The general
    payment line and the genre-specific rate are both kept, because they differ.
  * After Dinner Conversation pays $75 one-time; its $25 Fast Pass and $80
    feedback service are the writer's costs.
  * American Short Fiction states "Payment is competitive and upon publication"
    and publishes no figure. That is recorded as paid-not-published, not as a
    number and not as "not stated".

Markets read and HELD BACK are listed at the foot of this file with the reason.

WHAT WAS REJECTED BY READING, NOT BY REGEX
------------------------------------------
A money-word scan is a triage aid, never a source. Two traps caught in this batch:
Appalachia's page is full of "payment" language that is all subscription billing,
and antiphony's carries Squarespace template boilerplate ("From $107.50/mo").
Both would have been recorded as paying markets by a keyword classifier. Neither
pays writers for unsolicited work on the evidence read.
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

# ------------------------------------------- 1 American Poetry Journal
NEW.append(rec(
    "american-poetry-journal", "American Poetry Journal",
    "Poetry and cover art: $25 paid to every published poet and artist",
    "American Poetry Journal: $25 honorarium, $3 to submit, opens 1 November 2026",
    "American Poetry Journal pays a $25 honorarium to each poet and artist it "
    "publishes. Submissions carry a $3 fee and are read in windows: the next opens "
    "1 November 2026 for the February 2027 issue. Simultaneous submissions are "
    "fine if you say so. Open to contributors globally; no translations.",
    "https://apjpoetry.org/submit", "https://apjpoetry.org/submit", None,
    "Online form through Duosuma - a free Duotrope account is required. No email "
    "and no postal submissions.",
    src("American Poetry Journal - Submissions (official)", "https://apjpoetry.org/submit"),
    worldwide("Official page: poetry and art in most styles, forms or genres "
              "\"from all contributors globally\", with no country restriction stated."),
    ["poetry"], "Poetry and cover art",
    pay("USD", 25, 25, "$25 honorarium per published poet or artist",
        "Official submissions page: \"Poets and artists will each get paid a $25 "
        "honorarium for publication.\" Each issue reading period also carries a "
        "$3.00 fee, which the page says helps \"pay contributors and poet staff\" - "
        "that fee is the writer's cost and is not part of the rate.",
        "On publication"),
    {"min": None, "max": None,
     "display": "Poetry: up to 3 poems in one file, 7 pages total. Cover art: up to 5 pieces"},
    {"label": "One to two months", "band": "1-3-months", "official": True},
    "upcoming",
    {"display": "The February 2027 issue window runs 1 November 2026 to 30 November "
                "2026; the October 2027 window opens 1 July 2027",
     "openingDate": "2026-11-01", "windowEnd": "2026-11-30", "recurring": True},
    "prohibited",
    ["Poems that are \"unique and honest\", with distinctive imagery and a mastery of "
     "craft; the editors say they want bold metaphors and sonics they have not heard "
     "before.",
     "Poems that question humanity and engage contemporary as well as age-old "
     "concepts.",
     "Cover art, black and white or colour, up to 5 pieces at high resolution."],
    ["Work drafted or composed with generative AI (Natural Language Processing "
     "tools used only to check spelling and grammar are explicitly allowed).",
     "Translations - not considered at this time.",
     "Book reviews - no longer published.",
     "Easy rhymes and \"light\" verse, which the page says are less likely to place.",
     "A second file of poems: the first file is read and the rest are lost, and the "
     "fee is not refunded.",
     "More than one submission per reading period - multiple submissions stopped "
     "being considered on 19 June 2026."],
    ["Read https://apjpoetry.org/submit before sending.",
     "Pay the $3.00 submission fee. One day per reading period is free for a DEI "
     "tribute, capped at 55 submissions - 13 November 2026 for the February 2027 "
     "issue.",
     "Poetry: send no more than 3 previously unpublished poems in ONE file of no "
     "more than 7 pages. A second file is discarded without refund.",
     "Cover art: up to 5 previously unpublished pieces as high-resolution .jpeg "
     "(.jpg) or .png.",
     "Include a 50-word third-person bio with a short cover note.",
     "Submit through Duosuma; a free Duotrope account is required.",
     "The reading period is capped at 400 submissions and may be extended.",
     "If previously published in APJ, wait one year from acceptance before "
     "submitting again."],
    "The creator retains copyright on publication and grants APJ first "
    "serial/electronic rights as well as electronic archival rights, agreeing that "
    "any later publication of the work credits APJ.",
    ["Read https://apjpoetry.org/submit before sending.",
     "Submit through the Duosuma button on the page. A free Duotrope account is "
     "required; APJ does not accept email or postal submissions.",
     "The February 2027 issue window is open 1 November 2026 to 30 November 2026, "
     "with 13 November 2026 free for DEI submissions.",
     "Poetry goes in a single .doc, .docx or PDF file - not a OneDrive or Google "
     "Docs link. Art goes as attached high-resolution image files."],
    ["american poetry journal", "apj poetry", "$25 honorarium", "$3 submission fee",
     "poetry submissions", "cover art", "duosuma", "free submission day",
     "simultaneous submissions allowed", "no generative ai"],
    "accepted",
    "Simultaneous submissions are fine, but please mention it in your email. "
    f"— https://apjpoetry.org/submit (read {READ})"))

# ------------------------------------------- 2 After Dinner Conversation
NEW.append(rec(
    "after-dinner-conversation", "After Dinner Conversation",
    "Short stories: $75 one-time payment, no future royalties",
    "After Dinner Conversation: $75 per story, 1,500-7,000 words, no web-published reprints",
    "After Dinner Conversation pays $75 one-time for accepted unsolicited short "
    "stories, with no future royalties. Adult stories run 1,500-7,000 words. It "
    "will not consider stories already readable on the open web, and it does not "
    "accept AI-generated writing.",
    "https://afterdinnerconversation.com/submissions",
    "https://afterdinnerconversation.com/submissions", None,
    "Online submission form; a $25 Fast Pass gives priority reading",
    src("After Dinner Conversation - Submissions (official)",
        "https://afterdinnerconversation.com/submissions"),
    intl(),
    ["fiction"], "Short fiction (philosophy and ethics)",
    pay("USD", 75, 75,
        "$75 one-time payment per accepted short story, with no future royalties",
        "Official FAQ and submissions page: \"Accepted short stories from "
        "unsolicited submissions are paid a one-time amount of $75 with no future "
        "royalties.\" The $25 Fast Pass and the $80 story-feedback service are the "
        "writer's costs, not pay.",
        "Not publicly stated"),
    {"min": 1500, "max": 7000,
     "display": "Adult stories 1,500-7,000 words (2,500-4,500 tend to fare best); "
                "young adult under 3,500; children's under 1,500"},
    {"label": "A few sentences of reader feedback with each rejection; no timeframe stated",
     "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Short stories that raise a philosophical or ethical question and carry it "
     "through, which is the magazine's stated remit.",
     "Stories that present both sides of an ethical dilemma rather than a position.",
     "Shorter work: the page says 2,500-4,500 words tend to do best."],
    ["Writing generated with AI software.",
     "Stories that are already freely readable online - if a Google search finds "
     "the text on a website, the magazine is not interested.",
     "Reprints that would breach another agreement the writer has signed.",
     "Very long work: the page warns that past 5,000 words readers may skim, and "
     "long stories are rarely published."],
    ["Read the submissions page and FAQ at "
     "https://afterdinnerconversation.com/submissions before sending.",
     "Word counts: adult 1,500-7,000, young adult under 3,500, children's under 1,500.",
     "Optional costs: a $25 Fast Pass buys priority reading and a response in 3-5 "
     "business days; an $80 service buys developed feedback from the story editor.",
     "Check the author agreement linked from the page; the page tells writers not "
     "to submit if they are not comfortable with its terms.",
     "Quotes from copyrighted work need written permission and attribution."],
    "Accepted stories are published under an author agreement that grants the "
    "magazine the right to publish the story. Payment is a one-time $75 with no "
    "future royalties.",
    ["Read the submissions page and FAQ at "
     "https://afterdinnerconversation.com/submissions before sending.",
     "Submit through the online form on that page.",
     "Stories are also considered for the magazine's themed anthologies."],
    ["after dinner conversation", "$75 per story", "short story submissions",
     "philosophy fiction", "ethics fiction", "1500-7000 words",
     "no future royalties", "fast pass", "no ai submissions"],
    "accepted",
    "Do you accept reprints and/or simultaneous submissions? Yes, but... It is one "
    "thing for your story to be behind a paywall or in a print magazine, it's "
    "another thing for it to be freely available on a website. If it is on a "
    "website and can be found and read online via a google search we are not "
    "interested in it. "
    f"— https://afterdinnerconversation.com/submissions (read {READ})"))

# ------------------------------------------- 3 American Short Fiction
NEW.append(rec(
    "american-short-fiction", "American Short Fiction",
    "Short fiction: paid on publication, $3 to submit",
    "American Short Fiction: competitive payment on publication, $3 fee, September-December",
    "American Short Fiction pays for accepted stories, though it publishes no "
    "figure, and buys first serial rights with all rights reverting to the author "
    "on publication. Unsolicited submissions run September through December, cost "
    "$3, and are read alongside two annual contests.",
    "https://americanshortfiction.org/submityourwork",
    "https://americanshortfiction.org/submityourwork", None,
    "Online form through Submittable",
    src("American Short Fiction - Submit Your Work (official)",
        "https://americanshortfiction.org/submityourwork"),
    intl(),
    ["fiction"], "Short fiction",
    pay(None, None, None, "Payment is competitive - amount not published",
        "Official submissions page: \"Payment is competitive and upon publication. "
        "American Short Fiction purchases first serial rights. All rights revert to "
        "the author upon publication.\" The $3 submission fee is the writer's cost "
        "and is not pay.",
        "On publication"),
    {"min": None, "max": None,
     "display": "No set guidelines as to the content or length of regular submissions"},
    {"label": "No stated timeframe; the page asks writers to wait at least eight "
              "months before following up",
     "band": "3-plus-months", "official": True},
    "open",
    {"display": "Unsolicited submissions are accepted September through December "
                "each year; contests run at other times",
     "windowEnd": "2026-12-31", "recurring": True},
    "not-stated",
    ["Original, previously unpublished short fiction - the magazine says its "
     "standards are extremely high and asks writers to read the magazine first.",
     "Work from established, new and lesser-known writers alike.",
     "Translations, provided a copy of the original text accompanies them."],
    ["Work that has appeared online, including on blogs or Facebook - the page "
     "counts that as previously published.",
     "Poetry, plays, nonfiction, reviews and other non-fiction forms.",
     "Paper submissions - they are recycled on receipt.",
     "More than one story at a time.",
     "Manuscripts not written in English."],
    ["Read https://americanshortfiction.org/submityourwork before sending.",
     "Pay the $3 submission fee, then submit.",
     "Send one story at a time, typed and double-spaced, with the author's name, "
     "address, phone number and approximate word count on the first page and pages "
     "numbered throughout.",
     "Unsolicited submissions are read September through December only; contests "
     "run outside that window.",
     "Wait at least eight months before sending a follow-up inquiry, to "
     "editors@americanshortfiction.org with \"Submissions Inquiry\" in the subject."],
    "American Short Fiction purchases first serial rights for accepted work, and "
    "all rights revert to the author upon publication.",
    ["Read https://americanshortfiction.org/submityourwork before sending.",
     "Regular (non-contest) submissions are accepted September through December.",
     "Submit through Submittable and pay the $3 fee before the work is sent.",
     "Contest guidelines are separate and are announced on the magazine's homepage."],
    ["american short fiction", "short story submissions", "$3 submission fee",
     "competitive payment", "first serial rights", "september to december",
     "short fiction", "submittable"],
    "accepted",
    "We will read and consider simultaneous submissions on the condition that if "
    "the manuscript is accepted for publication elsewhere, the author immediately "
    "withdraw the submission through the Submittable site. "
    f"— https://americanshortfiction.org/submityourwork (read {READ})"))

# ------------------------------------------- 4 Bayou Magazine
NEW.append(rec(
    "bayou-magazine", "Bayou Magazine",
    "Fiction: $150 for stories of 3,000 words or more, $100 under",
    "Bayou Magazine: $150 or $100 per story by length, open to 15 December 2026",
    "Bayou Magazine pays $150 for fiction of 3,000 words or more and $100 for "
    "shorter stories, and pays other genres in contributor copies. It reads poetry "
    "and fiction from 15 September to 15 December, publishes no work touched by AI, "
    "and excludes University of New Orleans students, faculty and alumni.",
    "https://bayoumagazine.org/submissions",
    "https://bayoumagazine.submittable.com/submit", None,
    "Online form through Submittable only - mailed and emailed work is discarded",
    src("Bayou Magazine - Submissions (official)",
        "https://bayoumagazine.org/submissions"),
    intl("No stated country restriction. Students, faculty and alumni of the "
         "University of New Orleans are not eligible to submit."),
    ["fiction", "poetry"], "Fiction and poetry",
    pay("USD", 100, 150,
        "Fiction: $150 for stories of 3,000 words or more, $100 for stories under "
        "3,000 words",
        "Official submissions page: \"Payment for fiction of >3000 words is $150, "
        "<3000 words is $100.\" The same page's general payment line reads \"Payment "
        "is one contributor's copy unless otherwise specified by genre\", so the "
        "cash rate is the fiction rate and other genres are paid in copies.",
        "Not publicly stated"),
    {"min": None, "max": 7500,
     "display": "Fiction up to 7,500 words, double spaced, 12pt Times New Roman"},
    {"label": "Contact the magazine if five months pass without a response",
     "band": "3-plus-months", "official": True},
    "open",
    {"display": "The reading period runs 15 September 2026 to 15 December 2026",
     "windowStart": "2026-09-15", "windowEnd": "2026-12-15", "recurring": True},
    "prohibited",
    ["Original, previously unpublished poetry and fiction.",
     "Flash fiction and short-shorts, though only one story per submission.",
     "Work from both established and emerging writers."],
    ["Work composed, revised or edited by AI - the magazine states it will not "
     "publish it and reserves the right to check between acceptance and publication.",
     "Work already published in print or online.",
     "Submissions from University of New Orleans students, faculty and alumni.",
     "More than one story per submission, or more than 5 poems at a time.",
     "Work sent by mail or email - Submittable only."],
    ["Read https://bayoumagazine.org/submissions before sending.",
     "Submit through Submittable only; mailed and emailed work is discarded without "
     "review.",
     "Fiction: one story per submission, up to 7,500 words, double spaced in 12pt "
     "Times New Roman.",
     "Poetry: one submission of up to 5 poems at a time.",
     "Include a cover page with title, author and contact details, plus a "
     "third-person bio - that bio is what the magazine will use.",
     "After a rejection, wait three months before submitting again.",
     "There is no submission fee stated on the page."],
    "After publication in Bayou Magazine, all rights revert to the author. Payment "
    "is one contributor's copy unless otherwise specified by genre, which for "
    "fiction means the stated cash rate.",
    ["Read https://bayoumagazine.org/submissions before sending.",
     "Submit through Submittable - the only channel the magazine accepts.",
     "The reading period runs 15 September to 15 December.",
     "Send one story, or up to 5 poems, at a time and wait for the decision before "
     "sending more."],
    ["bayou magazine", "$150 per story", "$100 per story", "fiction submissions",
     "poetry submissions", "3000 words", "7500 words", "no ai",
     "university of new orleans", "submittable"],
    "accepted",
    "We accept simultaneous submissions. If your work is accepted elsewhere, we ask "
    "that you immediately add a note to your submission specifying the piece/s are "
    "no longer available. "
    f"— https://bayoumagazine.org/submissions (read {READ})"))

# ------------------------------------------- 5 Bennington Review
NEW.append(rec(
    "bennington-review", "Bennington Review",
    "Prose and poetry: $120-$250 for prose, $25 per poem",
    "Bennington Review: $120-$250 per prose piece, $25 per poem, opens 4 January 2027",
    "Bennington Review pays $120 for prose up to six typeset pages and $250 beyond "
    "that, plus $25 per poem, along with copies of the issue. It acquires first "
    "North American serial rights and takes simultaneous submissions if told about "
    "an acceptance elsewhere. The next reading period opens 4 January 2027.",
    "https://benningtonreview.org/submit", "https://benningtonreview.org/submit", None,
    "Online form through Submittable",
    src("Bennington Review - Submit (official)", "https://benningtonreview.org/submit"),
    intl("No stated country restriction. Current or recent Bennington College "
         "students, faculty and staff may not submit; alumni and past employees "
         "must wait three years."),
    ["poetry", "creative-nonfiction", "fiction", "translation"],
    "Poetry, fiction, creative nonfiction and translation",
    pay("USD", 25, 250,
        "$120-$250 for prose by length and $25 per poem, plus two copies of the issue",
        "Official submissions page: \"We pay contributors $120 for prose of six "
        "typeset pages and under, $250 for prose of over six typeset pages, and $25 "
        "per poem, in addition to two copies of the issue in which the piece is "
        "published and a copy of the subsequent issue.\"",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Prose up to 30 pages; 3-5 poems per submission"},
    {"label": "Five to eight months", "band": "3-plus-months", "official": True},
    "upcoming",
    {"display": "The next reading period runs 4 January 2027 to 5 March 2027",
     "openingDate": "2027-01-04", "windowEnd": "2027-03-05", "recurring": True},
    "not-stated",
    ["Innovative, intelligent and moving fiction, creative nonfiction, poetry, film "
     "writing and cross-genre work.",
     "Writing in the spirit of the poet Dean Young's dictum that poets should be "
     "\"making birds, not birdcages\".",
     "Translations, where the translator holds permission from the copyright holder "
     "and supplies the work in its original language."],
    ["Work previously published in print or online, including on personal blogs.",
     "Reviews and interviews, which are not accepted unsolicited.",
     "Film writing as its own category - it now goes through nonfiction.",
     "Paper and unsolicited email submissions, which the magazine cannot answer.",
     "Submissions from current or recent Bennington College students, faculty and "
     "staff."],
    ["Read https://benningtonreview.org/submit before sending.",
     "Submit through Submittable only.",
     "Poetry: no fewer than three and no more than five poems per submission.",
     "Fiction and creative nonfiction: no more than thirty pages per submission; "
     "excerpts from longer projects must stand alone.",
     "Prose must be double-spaced and paginated, with a cover letter.",
     "The next reading period opens 4 January 2027 and closes 5 March 2027.",
     "No submission fee is stated on the page."],
    "Bennington Review acquires first North American serial rights for all accepted "
    "work. Some accepted work is also featured on the magazine's website.",
    ["Read https://benningtonreview.org/submit before sending.",
     "Submit through Submittable during the reading period that runs 4 January 2027 "
     "to 5 March 2027.",
     "Send 3-5 poems, or up to 30 pages of prose.",
     "Questions go to benningtonreview@bennington.edu."],
    ["bennington review", "$25 per poem", "$120 prose", "$250 prose",
     "first north american serial rights", "poetry submissions",
     "creative nonfiction", "translation", "january 2027 reading period"],
    "accepted",
    "We welcome simultaneous submissions, as long as you notify us immediately when "
    "work has been accepted elsewhere. "
    f"— https://benningtonreview.org/submit (read {READ})"))

# ------------------------------------------- 6 Blackbird
NEW.append(rec(
    "blackbird", "Blackbird",
    "Poetry, fiction and essays: $40 per poem, $200 per story",
    "Blackbird: $40 per poem, $200 per story or essay, $100 per review",
    "Blackbird pays $40 per poem, $200 per story or essay, and $100 for book "
    "reviews, craft essays and interviews. It reads submissions year-round, takes "
    "simultaneous work if flagged, and will not accept work produced or altered by "
    "AI in any way.",
    "https://blackbird.vcu.edu/submissions", "https://blackbird.vcu.edu/submissions",
    None, "Online form through Submittable",
    src("Blackbird - Submissions (official)",
        "https://blackbird.vcu.edu/submissions"),
    intl(),
    ["poetry", "fiction", "essays", "creative-nonfiction", "reviews", "interviews"],
    "Poetry, fiction, essays, reviews and interviews",
    pay("USD", 40, 200,
        "$40 per poem, $200 per story or essay, $100 per book review, craft essay or "
        "interview",
        "Official submissions page, by genre: \"We pay $40/poem.\" / \"We pay "
        "$200/story.\" / \"We pay $200/essay.\" / \"We pay $100/book review, craft "
        "essay, and interview.\"",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Poetry: 2-6 poems per submission; prose guidelines are on the page"},
    {"label": "Six months or longer", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Short stories, novel excerpts that stand alone, personal essays and memoir "
     "excerpts.",
     "Poetry: send up to six poems, but no fewer than two.",
     "Book reviews, craft essays and interviews.",
     "Bodies of work whose individual pieces have appeared elsewhere, provided the "
     "majority is unpublished."],
    ["Work produced or altered by AI in any way.",
     "Unsolicited book reviews and criticism outside the stated categories.",
     "Work that has not been indicated as a simultaneous submission when it is one."],
    ["Read https://blackbird.vcu.edu/submissions before sending.",
     "Submit through Submittable.",
     "Poetry: 2-6 poems in a single document, set as they should appear in print.",
     "Prose: double-spaced.",
     "Flag simultaneous submissions as such, and notify the magazine immediately on "
     "acceptance elsewhere.",
     "Withdraw individual poems by message through Submittable, not by resubmitting.",
     "Expect six months or more for a response, and wait for a decision before "
     "sending more."],
    "Not stated on the guidelines page.",
    ["Read https://blackbird.vcu.edu/submissions before sending.",
     "Submit through Submittable; submissions for Blackbird 2.0 are open.",
     "Send 2-6 poems, or prose in the stated categories.",
     "Indicate simultaneous submissions and withdraw immediately on acceptance "
     "elsewhere."],
    ["blackbird", "$40 per poem", "$200 per story", "$200 per essay",
     "vc university", "poetry submissions", "fiction submissions",
     "no ai", "simultaneous submissions", "submittable"],
    "accepted",
    "Simultaneous submissions are acceptable so long as they are indicated as such "
    "and we are immediately notified upon acceptance elsewhere. "
    f"— https://blackbird.vcu.edu/submissions (read {READ})"))


BASE = {
    "american-poetry-journal": ("", "International"),
    "after-dinner-conversation": ("", "International"),
    "american-short-fiction": ("", "International"),
    "bayou-magazine": ("", "International"),
    "bennington-review": ("", "International"),
    "blackbird": ("", "International"),
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
