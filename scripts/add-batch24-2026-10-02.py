"""Add verified writing-market batch 24 (2026-10-02).

Ten NEW markets, each read off its own page (saved text under
research/rebuild/raw/, crawl of 2026-09-30; the desk read them on 2026-10-02).

THE FIGURE THAT IS THE RATE, AND THE FIGURES THAT ARE NOT
---------------------------------------------------------
Four of these pages mix money of different kinds, and the record separates them:

  * Nimrod's $2,000/$1,000 Literary Awards are contest outcomes behind a $25
    entry; the RATE is "We pay $20 per poem and page of prose, with a $300
    maximum". General submissions are free.
  * Pangyrus and Palette Poetry both have paid options (a $3 submission charge;
    Fast Response and Editorial Feedback) that are the writer's costs. The rates
    are $30 per accepted piece and $50 per poem up to $150.
  * Mulberry Literary's two July windows are free (Early Bird) and
    pay-what-you-can (Last Minute) - writer's costs, not pay.
  * Kweli states "Payment is after publication." and publishes no amount. It is
    recorded in the same shape as Black Warrior Review: payment stated, amount
    not published. Nothing is invented for it.

The First Line, Overtime, Blackbird, Booth, Consequence, First Line and
Gavialidae were also re-read from their saved pages while working this batch;
all five existing records already match what their pages say, so none of them
needed a field changed.

CLOSED LEADS FROM THE PREVIOUS SWEEPS
-------------------------------------
  * action_spectacle - no rate for general publication. All the money on the
    page is fee-backed contests ($20 Editors' Prize entry, $25 book and
    chapbook entries, $1,000 prizes). Contest prizes are context, a fee is
    never a rate.
  * anacapa_review - Anacapa Review states no payment for publication and
    charges $3 an entry; the $500 with 10 author copies is the John Ridland
    Poetry Prize, behind a $30/$25 entry and open to poets 55 and older.
  * blue_earth_review - "Payment is two contributor's copies."
  * chicago_quarterly_review - "PAYMENT FOR PUBLICATION: Two copies of the
    Chicago Quarterly Review."
  * dunes_review - "Payment comes in the form of two copies of the journal, or
    one digital copy for international contributors."
    Copies are not money, so these three are unpaid markets by their own words
    and stay out of a paid-opportunities index.

A DUPLICATE, RESOLVED RATHER THAN RE-ADDED
------------------------------------------
The long pw.org slug after_dinner_conversation_philosophy_ethics_short_story_
magazine turned out to be the same market as the existing record
after-dinner-conversation. Its page was re-fetched on the desk date, the $75
rate and the AI ban are still on it, and the record's lastVerified was bumped
to 2026-10-02 by scripts/refresh-after-dinner-conversation-2026-10-02.py. No
second record was created.
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-10-02"
READ = "2026-10-02"


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
    "exposition-review", "Exposition Review",
    "Fiction, poetry and more: $50.00 USD for accepted work",
    "Exposition Review: $50 per accepted piece, 1 October to 15 December",
    "Exposition Review pays $50.00 USD for accepted work and leaves copyright with "
    "the author, asking only that a later reprint cites the magazine. It reads "
    "fiction and nonfiction up to 5,000 words, flash up to three pieces of 1,000 "
    "words each, up to three poems, stage and screen up to 15 pages, comics and "
    "short film. The annual issue window runs 1 October to 15 December, "
    "simultaneous submissions are accepted with a note in the cover letter, and "
    "only previously unpublished work is considered.",
    "https://expositionreview.com/submission-guidelines",
    "https://expositionreview.com/submission-guidelines", None,
    "Submittable only; one piece per genre at a time, and previously unpublished "
    "work only.",
    src("Exposition Review - Submission Guidelines (official)",
        "https://expositionreview.com/submission-guidelines"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry", "drama", "other"],
    "Fiction, flash fiction, nonfiction, poetry, stage and screen, comics, film "
    "and visual art",
    pay("USD", 50, 50, "$50.00 USD for accepted work",
        "Official page: \"Author receives $50.00 USD for accepted work. Author "
        "retains copyright, but is asked to cite appearance in Exposition Review "
        "if the work is republished elsewhere.\"",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "Fiction and nonfiction up to 5,000 words; flash up to three "
                "pieces of 1,000 words each; up to three poems; stage and screen "
                "up to 15 pages; comics up to three pages per piece; film up to "
                "15 minutes."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Annual issue window 1 October to 15 December; the Flash 405 "
                "short-form contests run in February, April, June and August",
     "openingDate": "2026-10-01", "windowEnd": "2026-12-15", "recurring": True},
    "not-stated",
    ["Work that fits or rethinks the annual theme, told in a strong voice and a "
     "strong sense of place.",
     "Boundary-blurring, risk-taking pieces; the page asks to be surprised.",
     "Genre work across fiction, flash, nonfiction, poetry, stage and screen, "
     "comics, film and experimental narrative."],
    ["Previously published work, including anything already published online.",
     "Pieces over the stated limits - the page says over-length work will not be "
     "read.",
     "More than one piece of the same genre at a time, or a new piece before the "
     "previous one has been answered."],
    ["Read the guidelines at "
     "https://expositionreview.com/submission-guidelines before sending.",
     "Submit through Submittable only; there is no fee stated on the guidelines "
     "page.",
     "Send one piece per genre, previously unpublished, within the stated limits.",
     "Note simultaneous submissions in the cover letter and withdraw promptly if "
     "the work is accepted elsewhere.",
     "The annual issue window runs 1 October to 15 December."],
    "The author retains copyright, and is asked to cite appearance in Exposition "
    "Review if the work is republished elsewhere.",
    ["Read the guidelines page before sending.",
     "Submit via Submittable; one piece per genre at a time.",
     "Follow the genre limits: fiction and nonfiction up to 5,000 words, flash up "
     "to 1,000 words a piece, up to three poems.",
     "Note simultaneous submissions in the cover letter and notify the editors on "
     "acceptance elsewhere.",
     "Expect the annual issue window to run 1 October to 15 December."],
    ["exposition review", "$50 usd", "accepted work", "flash 405",
     "stage and screen", "comics", "short film", "author retains copyright",
     "october to december"],
    "accepted",
    "Simultaneous submissions are accepted, but make note of this in your cover "
    "letter and notify us immediately if your submission is accepted elsewhere. "
    f"— https://expositionreview.com/submission-guidelines (read {READ})"))

NEW.append(rec(
    "mulberry-literary", "Mulberry Literary",
    "Flat $25 USD a piece, and a pay-what-you-can window",
    "Mulberry Literary: $25 USD per accepted piece, July windows, closed now",
    "Mulberry Literary pays a flat $25 USD for each piece accepted, through "
    "PayPal, and sends contributors the issue their work appears in. The journal "
    "is closed between cycles: its annual windows run 1-14 July, free, and 15-31 "
    "July as pay-what-you-can. It takes fiction, nonfiction, poetry, plays, "
    "screenplays, film, ballet and art, refuses AI-generated or AI-assisted work "
    "and previously published work, accepts simultaneous submissions with prompt "
    "notice, and answers within about three months.",
    "https://mulberryliterary.com/submit",
    "https://mulberryliterary.com/submit", None,
    "Submittable forms only, one category per cycle; email submissions are no "
    "longer read.",
    src("Mulberry Literary - Submissions (official)",
        "https://mulberryliterary.com/submit"),
    intl("No country restriction is stated; the journal particularly encourages "
         "work from LGBTQIA+, women, international and BIPOC writers and "
         "artists."),
    ["fiction", "creative-nonfiction", "poetry", "drama", "other"],
    "Fiction, nonfiction, poetry, plays, screenplays, film, ballet and art",
    pay("USD", 25, 25, "Flat $25 USD for each piece accepted",
        "Official page: \"Contributors featured in our issues will receive a flat "
        "rate of $25 USD for each piece accepted. At this time, payments to our "
        "contributors can and will only be distributed through PayPal.\" The "
        "annual Early Bird window (1-14 July) requires no donation, while the "
        "Last Minute window (15-31 July) asks for a pay-what-you-can donation "
        "that is the writer's cost, not part of the rate.",
        "On publication"),
    {"min": None, "max": None,
     "display": "Word counts are not stated on the guidelines page; genre "
                "guidelines sit inside each submission form."},
    {"label": "Up to three months", "band": "3-months", "official": True},
    "closed",
    None,
    "prohibited",
    ["Best work in any theme or genre, including experimental and genre work.",
     "Fiction, nonfiction, poetry, plays, screenplays, film, ballet and art.",
     "Work from LGBTQIA+, women, international and BIPOC writers and artists, "
     "whom the journal particularly encourages."],
    ["AI-generated, AI-prompted or AI-assisted work.",
     "Previously published material, including work posted to public social "
     "media, Substack or other blog platforms.",
     "Manuscripts, novels or chapbooks, or submissions to more than one category "
     "in a single cycle.",
     "Copyright-infringing material, including fanart and fanfiction."],
    ["Read the guidelines at https://mulberryliterary.com/submit before the next "
     "window; submissions are closed at present and reopen next year.",
     "Choose one category per cycle; more than one category in a cycle is "
     "automatically rejected.",
     "Note the two July windows: 1-14 July is free, 15-31 July asks for a "
     "pay-what-you-can donation.",
     "Simultaneous submissions are considered, but tell the editors immediately "
     "if a piece is accepted elsewhere.",
     "Expect a response within up to three months, and do not send a new entry "
     "within the same period after a decision."],
    "Mulberry Literary receives first North American serial publication rights "
    "(FNASR); after publication in print and online, contributors may republish "
    "their piece elsewhere so long as they state Mulberry Literary as its first "
    "appearance.",
    ["Read the submission guidelines before the next window opens.",
     "Pick one category per cycle and submit through the Submittable form.",
     "Simultaneous submissions are fine; notify the editors on acceptance "
     "elsewhere.",
     "Expect up to three months for a decision.",
     "Watch for the July windows: free 1-14 July, pay-what-you-can 15-31 July."],
    ["mulberry literary", "$25 usd per piece", "paypal", "no ai",
     "fnasr", "july windows", "pay-what-you-can", "closed"],
    "accepted",
    "Simultaneous submissions will be considered, but please inform us "
    "immediately if your piece has been accepted elsewhere. "
    f"— https://mulberryliterary.com/submit (read {READ})"))

NEW.append(rec(
    "claudine-a-literary-magazine", "Claudine: A Literary Magazine",
    "Micros: $25 on publication for up to 400 words",
    "Claudine: $25 per micro on publication, 400 words, free to submit",
    "Claudine pays $25 on publication for microfiction and micro creative "
    "nonfiction of up to 400 words, a firm limit, and never charges a submission "
    "fee. It reads January through November, one submission with up to two micros "
    "per calendar month, accepts simultaneous submissions with prompt "
    "withdrawal, and answers most submissions within ten days. Rights are first "
    "serial rights worldwide in English plus non-exclusive anthology rights, with "
    "copyright kept by the writer, and AI-generated or AI-assisted work is "
    "refused.",
    "https://claudineliterary.net/general-5",
    "https://claudineliterary.net/general-5",
    "submissions@claudineliterary.com",
    "Email the submission to submissions@claudineliterary.com with the genre and "
    "title in the subject line, a brief cover letter and a 50-word bio.",
    src("Claudine: A Literary Magazine - Submissions (official)",
        "https://claudineliterary.net/general-5"),
    intl(),
    ["fiction", "creative-nonfiction"],
    "Microfiction and micro creative nonfiction",
    pay("USD", 25, 25, "$25 upon publication for each micro",
        "Official page, under all three micro categories: \"Pay is $25 upon "
        "publication.\" And on cost: \"Fee. Submissions are always FREE.\"",
        "On publication"),
    {"min": None, "max": 400,
     "display": "Up to 400 words, all categories, a firm count: microfiction, "
                "micro creative nonfiction and New Writer micros."},
    {"label": "About ten days for most submissions", "band": "10-days",
     "official": True},
    "open",
    {"display": "Open January through November; the journal does not read "
                "submissions in December",
     "windowStart": "2026-01-01", "windowEnd": "2026-11-30", "recurring": True},
    "prohibited",
    ["Pieces that move and surprise, with intentional language and specificity.",
     "Myths, fairy tales, fabulism, slipstream and haunting vibes; prose that "
     "makes the reader ache.",
     "Notably, the New Writer category for writers with three or fewer published "
     "literary pieces."],
    ["Horror, or fantasy and science fiction that leans more genre than literary.",
     "Op-eds, rants and heavy-handed issue pieces.",
     "Pieces over 400 words, or more than one submission a month.",
     "AI-generated or AI-assisted work - the journal runs submissions through a "
     "third-party authenticator."],
    ["Read the guidelines at https://claudineliterary.net/general-5 before "
     "sending.",
     "Email submissions@claudineliterary.com with genre and title in the subject "
     "line.",
     "Keep the piece to 400 words or fewer, and send one submission with up to "
     "two micros per calendar month.",
     "Include a brief cover letter, the word count, and a 50-word bio.",
     "There is no fee; expect a response in about ten days."],
    "First serial rights worldwide in English and non-exclusive anthology "
    "rights; the journal asks for the right to display the work for the duration "
    "of the journal, and copyright remains with the writer in all cases, with an "
    "acknowledgement asked for if the work is reprinted elsewhere.",
    ["Read the guidelines page before sending.",
     "Email the piece to submissions@claudineliterary.com with genre and title "
     "in the subject line.",
     "Keep it to 400 words; one submission with up to two micros per calendar "
     "month.",
     "Note simultaneous submissions and withdraw promptly on acceptance "
     "elsewhere.",
     "Expect a response in about ten days, and note the journal is closed in "
     "December."],
    ["claudine", "$25 on publication", "microfiction", "400 words",
     "no fee", "free submissions", "january to november", "new writer micros",
     "no ai"],
    "accepted",
    "We accept simultaneous submissions; please withdraw your piece promptly if "
    "it's accepted elsewhere. "
    f"— https://claudineliterary.net/general-5 (read {READ})"))

NEW.append(rec(
    "nimrod-international-journal", "Nimrod International Journal",
    "October window: $20 a poem or prose page, $300 maximum",
    "Nimrod International Journal: $20 per poem or prose page, open 1-31 October",
    "Nimrod pays $20 per poem and per page of prose, with a $300 maximum, and "
    "its general submission window is open this October, 1-31, free online or by "
    "post. It takes fiction up to 5,000 words and up to seven pages of poetry, "
    "all previously unpublished, and asks for first North American rights. "
    "Simultaneous submissions are accepted when noted, responses take one to "
    "five months, and the separate Literary Awards - a $2,000 first prize and "
    "$1,000 second in fiction and poetry - charge $25 an entry.",
    "https://nimrodjournal.utulsa.edu/submissions-guidelines/",
    "https://nimrodjournal.utulsa.edu/submissions-guidelines", None,
    "Online submission manager or post; email only for writers overseas who "
    "cannot use the manager.",
    src("Nimrod International Journal - Submissions Guidelines (official)",
        "https://nimrodjournal.utulsa.edu/submissions-guidelines/"),
    intl("No country restriction is stated; the journal notes that writers "
         "living overseas may email if they cannot use the online submission "
         "manager."),
    ["fiction", "poetry"],
    "Fiction and poetry",
    pay("USD", 20, 300, "$20 per poem and per page of prose, $300 maximum",
        "Official page: \"We pay $20 per poem and page of prose, with a $300 "
        "maximum.\" General submissions are free online and by post; the "
        "separate Nimrod Literary Awards charge $25 an entry with publication "
        "and $2,000 and $1,000 prizes, which are contest outcomes, not the rate.",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "Fiction up to 5,000 words; poetry up to seven pages, no more "
                "than one poem per page."},
    {"label": "One to five months", "band": "1-5-months", "official": True},
    "open",
    {"display": "General submissions open 1-31 October each year; the Literary "
                "Awards take entries 1-31 January",
     "openingDate": "2026-10-01", "windowEnd": "2026-10-31", "recurring": True},
    "not-stated",
    ["Previously unpublished fiction and poetry in any style or subject.",
     "Work that would sit well beside a century-old international journal; "
     "reading a sample issue first is recommended.",
     "Writers anywhere: overseas writers who cannot use the submission manager "
     "may email their work."],
    ["Previously published work of any kind.",
     "Fiction over 5,000 words, or poetry over seven pages or more than one poem "
     "a page.",
     "Email submissions from writers who can use the online submission manager."],
    ["Note the window: general submissions are open 1-31 October each year.",
     "Submit free through the online submission manager, or post to Nimrod "
     "International Journal, University of Tulsa, 800 S. Tucker Dr., Tulsa, OK "
     "74104.",
     "Send fiction double-spaced and poetry no more than one poem a page; only "
     "previously unpublished work.",
     "Note simultaneous submissions and withdraw immediately if accepted "
     "elsewhere.",
     "Writers overseas who cannot use the manager may paste work into an email."],
    "Nimrod takes first North American rights for work published in the journal.",
    ["Read the guidelines page before sending.",
     "Submit in the October window, 1-31, free online or by post.",
     "Send previously unpublished fiction up to 5,000 words or up to seven pages "
     "of poetry.",
     "Mark simultaneous submissions and withdraw them promptly on acceptance "
     "elsewhere.",
     "Expect one to five months for a response."],
    ["nimrod", "$20 per poem", "$300 maximum", "october 1-31", "tulsa",
     "first north american rights", "university of tulsa", "literary awards"],
    "accepted",
    "Simultaneous submissions are accepted as long as they are noted and "
    "withdrawn immediately if accepted elsewhere. "
    f"— https://nimrodjournal.utulsa.edu/submissions-guidelines/ (read {READ})"))

NEW.append(rec(
    "old-pal", "Old Pal",
    "Literature and art: $50 upon publication",
    "Old Pal: $50 on publication, poetry, prose, art; currently closed",
    "Old Pal compensates contributors $50 upon publication for poetry, fiction, "
    "criticism, excerpts, audio, mixed media and art, with all rights reverting "
    "to the author on publication. It asks for up to 10 pages of poetry, 15 "
    "pages of prose, 10 images, or five minutes of audio or video, and charges "
    "no submission fee. Simultaneous submissions are welcome with notice, "
    "previously published work is refused while work posted to social media is "
    "still considered. Submissions are closed at present; reading periods run in "
    "spring and fall.",
    "https://www.oldpalmagazine.com/submissions",
    "https://www.oldpalmagazine.com/submissions", None,
    "Online submissions through the magazine's form during its spring and fall "
    "reading periods.",
    src("Old Pal - Submissions (official)",
        "https://www.oldpalmagazine.com/submissions"),
    intl("No country restriction is stated; the magazine encourages artists "
         "from all experience levels and communities."),
    ["poetry", "fiction", "essays", "other"],
    "Poetry, fiction, criticism, excerpts, audio, mixed media and art",
    pay("USD", 50, 50, "$50 upon publication",
        "Official page: \"Contributors are compensated $50 upon publication.\" "
        "And on cost: \"There is no submission fee or subscription required to "
        "submit.\"",
        "On publication"),
    {"min": None, "max": None,
     "display": "Up to 10 pages of poetry, up to 15 pages of prose, up to 10 "
                "images or visual artworks, and up to five minutes of audio or "
                "video."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "closed",
    None,
    "not-stated",
    ["Poetry, fiction, criticism, excerpts, audio, mixed media and various "
     "mediums of art.",
     "Artists from all experience levels and communities; the magazine says it "
     "encourages them.",
     "Work already posted to social media, which the magazine says will still be "
     "considered."],
    ["Previously published work in the traditional sense, beyond social media "
     "posts.",
     "Submissions over the stated limits: 10 pages of poetry, 15 of prose, 10 "
     "images or five minutes of media.",
     "Sending outside the spring and fall reading periods."],
    ["Note that submissions are closed at present; reading periods run in spring "
     "and fall.",
     "Respect the limits: up to 10 pages of poetry, 15 pages of prose, 10 images, "
     "five minutes of audio or video.",
     "There is no submission fee and no subscription required.",
     "Simultaneous submissions are welcome - notify the magazine to withdraw "
     "works accepted elsewhere.",
     "Know that all rights revert on publication, with a first-publication "
     "acknowledgement requested for later reprints."],
    "All rights revert to authors and artists upon publication; the magazine "
    "requests first publication acknowledgement if the work is published "
    "elsewhere in future, and asks permission to post brief excerpts to social "
    "media for promotion.",
    ["Wait for the spring or fall reading period; submissions are closed now.",
     "Send poetry, prose, criticism, excerpts, audio, mixed media or art within "
     "the stated limits.",
     "There is no fee to submit.",
     "Mark simultaneous submissions and withdraw on acceptance elsewhere.",
     "Expect all rights to revert to you on publication."],
    ["old pal", "$50 upon publication", "no fee", "spring and fall",
     "rights revert", "social media posts considered", "poetry and art",
     "closed"],
    "accepted",
    "Simultaneous submissions are welcome; we just ask that you notify us to "
    "withdraw works if accepted elsewhere. "
    f"— https://www.oldpalmagazine.com/submissions (read {READ})"))

NEW.append(rec(
    "overtime", "Overtime (Workers Write!)",
    "Workplace stories: $40 to $60 a story",
    "Overtime: $40-$60 per story, 5,000-10,000 words, work as the theme",
    "Overtime, the one-story chapbook series from Workers Write!, pays $40 to "
    "$60 per story, depending on length and rights available. It wants stories "
    "of 5,000 to 10,000 words with work as a central theme, and will consider "
    "serialising novels about the workplace by query first. Send a query or the "
    "full story to overtime@workerswritejournal.com or by post; the page "
    "refuses work generated or co-written by AI, and states no submission fee.",
    "https://www.workerswritejournal.com/overtime.html",
    "https://www.workerswritejournal.com/overtime.html",
    "overtime@workerswritejournal.com",
    "Email a query or the full story to overtime@workerswritejournal.com, or "
    "post it to P.O. Box 250382, Plano, TX 75025-0382.",
    src("Overtime (Workers Write!) - Submissions (official)",
        "https://www.workerswritejournal.com/overtime.html"),
    intl(),
    ["fiction"],
    "Short stories",
    pay("USD", 40, 60, "$40-$60 per story, depending on length and rights available",
        "Official page: \"We publish 3 hours a year. We pay $40-$60 per story, "
        "depending on length and rights available.\"",
        "Not publicly stated"),
    {"min": 5000, "max": 10000,
     "display": "Stories of 5,000 to 10,000 words with work as a central theme; "
                "novels about the workplace by query first."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    None,
    "prohibited",
    ["Stories of 5,000 to 10,000 words where work is a central theme.",
     "Stories too long for the Workers Write! series but worthy of publication.",
     "Queries about serialising novels about the workplace."],
    ["Pieces shorter than 5,000 words or longer than 10,000, unless querying "
     "about a novel serialisation.",
     "Stories in which work is not central to the plot.",
     "Work generated or co-written by artificial intelligence."],
    ["Read the Overtime page at "
     "https://www.workerswritejournal.com/overtime.html before sending.",
     "Email a query or the full story to overtime@workerswritejournal.com, or "
     "post it to P.O. Box 250382, Plano, TX 75025-0382.",
     "Keep the story between 5,000 and 10,000 words with work as a central "
     "theme.",
     "No fee is stated on the page; subscriptions listed there are for readers."],
    "Not publicly stated beyond the note that the rate depends on \"length and "
    "rights available\".",
    ["Read the Overtime page before sending.",
     "Email a query or full story to overtime@workerswritejournal.com, or send "
     "by post.",
     "Keep the story between 5,000 and 10,000 words, with work as a central "
     "theme.",
     "Query first if you want to serialise a novel about the workplace.",
     "Note the page refuses writing generated or co-written by AI."],
    ["overtime", "workers write", "$40-$60 per story", "work theme",
     "5,000-10,000 words", "chapbook series", "query first", "no ai"],
    "not-stated", None))

NEW.append(rec(
    "pacifica-literary-review", "Pacifica Literary Review",
    "Poetry, prose and flash: $25 per piece published",
    "Pacifica Literary Review: $25 per published piece, open year-round",
    "Pacifica Literary Review pays $25 per piece published and reads poetry, "
    "fiction, creative nonfiction, flash and folios year-round, with periodic "
    "closures in September, January and May while it puts an issue together. "
    "Prose runs under 5,000 words, flash to three pieces of no more than 1,000 "
    "words each, and up to three poems. Simultaneous submissions are fine with "
    "immediate notice, responses take one to four months, and the magazine will "
    "not consider work involving AI processes of any description.",
    "https://pacificalitreview.com/submissions/",
    "https://pacificalitreview.com/submissions/", None,
    "Submittable; title each submission with the name of the work and wait for "
    "a decision before sending more.",
    src("Pacifica Literary Review - Submissions (official)",
        "https://pacificalitreview.com/submissions/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, fiction, creative nonfiction and flash fiction",
    pay("USD", 25, 25, "$25 per piece published",
        "Official page: \"Authors will be paid $25/piece published. We know it's "
        "not much, but it's the best we can do currently.\"",
        "On publication"),
    {"min": None, "max": 5000,
     "display": "Prose under 5,000 words; flash fiction up to three pieces of no "
                "more than 1,000 words each; up to three poems in one document."},
    {"label": "One to four months", "band": "1-4-months", "official": True},
    "open",
    None,
    "prohibited",
    ["Poetry, fiction, creative nonfiction, flash fiction and folios.",
     "Stand-alone novel excerpts that hold up on their own.",
     "Work that follows the genre limits, titled with the name of the work."],
    ["Prose of 5,000 words or more, flash over 1,000 words a piece, or more than "
     "three poems.",
     "Work involving AI processes of any description, including prompt, "
     "structure or text generation.",
     "Sending new work before receiving a decision on what is already under "
     "consideration, or resubmitting a piece already considered."],
    ["Read the submissions page at "
     "https://pacificalitreview.com/submissions/ before sending.",
     "Submit through Submittable during an open period; the magazine closes "
     "periodically in September, January and May.",
     "Keep prose under 5,000 words, flash to 1,000 words a piece, and poetry to "
     "three poems.",
     "Title submissions with the name of the work and wait for a decision before "
     "sending more.",
     "Simultaneous submissions are fine; notify the magazine immediately on "
     "acceptance elsewhere and withdraw through Submittable."],
    "Pacifica Literary Review reserves first North American publishing rights, "
    "and non-exclusive rights to reproduce, display and distribute the work in "
    "print or other media platforms.",
    ["Read the submissions page before sending.",
     "Submit via Submittable; the magazine reads year-round with closures in "
     "September, January and May.",
     "Keep prose under 5,000 words, flash to three pieces of 1,000 words, poetry "
     "to three poems.",
     "Notify the magazine immediately if a piece is accepted elsewhere and "
     "withdraw it.",
     "Expect one to four months for a decision."],
    ["pacifica literary review", "$25 per piece", "flash fiction",
     "novel excerpts", "folios", "year-round", "no ai", "submittable"],
    "accepted",
    "Simultaneous submissions are fine, as long as Pacifica Literary Review is "
    "notified immediately if the work is accepted elsewhere. "
    f"— https://pacificalitreview.com/submissions/ (read {READ})"))

NEW.append(rec(
    "palette-poetry", "Palette Poetry",
    "$50 a poem, up to $150, and always free to submit",
    "Palette Poetry: $50 per poem up to $150, open year-round",
    "Palette Poetry pays $50 per poem, up to $150, for Featured Poetry, which is "
    "free to submit and open year-round to poets at any stage, including "
    "internationally. It reads up to five poems totalling no more than ten "
    "pages, previously unpublished, in one document, and accepts simultaneous "
    "submissions. It refuses AI-generated work, holds first publication rights "
    "for three months after publication before rights revert to the author, and "
    "expects about twelve weeks for a response. Paid Fast Response and "
    "Editorial Feedback options exist but are the writer's cost.",
    "https://palettepoetry.com/submit/",
    "https://palettepoetry.com/submit/", None,
    "Submittable, with all poems for Featured Poetry in one document; the paid "
    "Fast Response and Editorial Feedback options are optional.",
    src("Palette Poetry - Submit (official)",
        "https://palettepoetry.com/submit/"),
    intl("Submissions are open internationally to any poet writing in English; "
         "translated work is not accepted unless the submitter is also the "
         "author of the original."),
    ["poetry"],
    "Poetry",
    pay("USD", 50, 150, "$50 per poem, up to $150",
        "Official page: \"We are thrilled to offer significant payment to our "
        "poets: $50 per poem, up to $150.\" The paid Fast Response and "
        "Editorial Feedback options are the writer's cost and are not part of "
        "the rate; the $60,000 Discover New Art Prize is a separate contest.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Up to five poems totalling no more than ten pages, in one "
                "document for Featured Poetry."},
    {"label": "About twelve weeks, with a two-to-four-week response in the "
              "historically marginalized voices category",
     "band": "12-weeks", "official": True},
    "open",
    None,
    "prohibited",
    ["Poets at any stage of their careers; emerging authors are highly "
     "encouraged.",
     "Poems in English from anywhere in the world, with other languages welcome "
     "alongside.",
     "Under-represented and marginalized voices, who have a dedicated category "
     "answered within two to four weeks."],
    ["Previously published poems, including work posted to a journal, blog or "
     "social media.",
     "Translated work unless the submitter is also the author of the original "
     "poem.",
     "Multiple submissions to Featured Poetry, or more than five poems or ten "
     "pages.",
     "AI-generated work, which Palette does not consider or review."],
    ["Read the submission page at https://palettepoetry.com/submit/ before "
     "sending.",
     "Note that Featured Poetry is always free and open year-round.",
     "Send up to five poems totalling no more than ten pages in one document, "
     "previously unpublished.",
     "Put identifying information and any publication history in the cover "
     "letter, not in the poem file, and include content warnings if relevant.",
     "Simultaneous submissions are accepted; message the editors via "
     "Submittable if a poem is picked up elsewhere."],
    "Palette Poetry holds first publication rights for three months after "
    "publication, after which rights revert to the author.",
    ["Read the submission page before sending.",
     "Submit up to five poems in one document through Submittable.",
     "Keep the poems previously unpublished, and put your details in the cover "
     "letter.",
     "Mark simultaneous submissions and message the editors on acceptance "
     "elsewhere.",
     "Expect about twelve weeks for a response, or two to four weeks in the "
     "historically marginalized voices category."],
    ["palette poetry", "$50 per poem", "up to $150", "featured poetry",
     "always free", "year-round", "rights revert after three months",
     "no ai", "international"],
    "accepted",
    "We accept simultaneous submissions, but please send us a message via "
    "Submittable if your work is picked up elsewhere—we want to say congrats! "
    f"— https://palettepoetry.com/submit/ (read {READ})"))

NEW.append(rec(
    "pangyrus", "Pangyrus",
    "$30 for every accepted piece, in an open reading period now",
    "Pangyrus: $30 per accepted piece, reading 15 September to 15 November",
    "Pangyrus pays all its authors, at a current rate of $30 per accepted piece, "
    "by PayPal, and is reading now through 15 November as part of its 15 "
    "September to 15 November period. It publishes fiction, poetry, nonfiction, "
    "memoir, comics and art online twice a week and in an annual print "
    "anthology, with essay pitches of 600-1,500 words, reported features up to "
    "7,500 words, and a maximum of 5,000 words for a short story. Simultaneous "
    "submissions are accepted with immediate notice, a $3 charge applies per "
    "submission, and work created with AI software is refused.",
    "https://pangyrus.submittable.com/submit",
    "https://pangyrus.submittable.com/submit", None,
    "Submittable; note the $3.00 charge per submission category, which is the "
    "writer's cost.",
    src("Pangyrus - Submissions Guidelines (official)",
        "https://pangyrus.submittable.com/submit"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry", "other"],
    "Fiction, nonfiction, memoir, poetry, comics, art, opinion and reviews",
    pay("USD", 30, 30, "$30 per accepted piece",
        "Official page: \"We pay all our authors, with a current rate of $30 per "
        "accepted piece. (We only use PayPal for payments.)\" Each submission "
        "category carries a $3.00 charge, which is the writer's cost, not part "
        "of the rate.",
        "Not publicly stated"),
    {"min": None, "max": 7500,
     "display": "Short stories up to 5,000 words or three micro/flash pieces; "
                "essays of 600-1,500 words or reported features up to 7,500 "
                "words; up to three poems in one document; pitches of 1,500 "
                "words or less."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Two reading periods a year: 15 February to 15 April, and 15 "
                "September to 15 November",
     "openingDate": "2026-09-15", "windowEnd": "2026-11-15", "recurring": True},
    "prohibited",
    ["Work with a strong point of view that takes the reader into surprising "
     "spaces.",
     "Fiction, poetry, nonfiction, memoir, comics, art, opinion pieces and "
     "reviews - the 2027 print issue's theme is Undercurrents.",
     "Established and new voices alike; the magazine edits for writing that will "
     "stand the test of time."],
    ["Work created with AI software.",
     "Previously published work - everything must be wholly original and "
     "unpublished.",
     "Sending revisions after the submission, or work to categories that are "
     "closed."],
    ["Read the guidelines at https://pangyrus.submittable.com/submit before "
     "sending.",
     "Submit through Submittable during the 15 February to 15 April or 15 "
     "September to 15 November reading periods.",
     "Respect the limits: short story up to 5,000 words or flash pieces, essays "
     "600-1,500 words, features up to 7,500 words, up to three poems.",
     "Note the $3.00 charge per submission category, which is the writer's cost.",
     "Simultaneous submissions are accepted; notify the magazine immediately on "
     "acceptance elsewhere."],
    "A contract is sent on acceptance; all accepted work appears online and "
    "selected work also appears in the print editions.",
    ["Read the guidelines page before sending.",
     "Submit via Submittable in one of the two reading periods.",
     "Keep within the word limits for the category, and send no revisions after "
     "submitting.",
     "Mark simultaneous submissions and tell the magazine immediately if a work "
     "is accepted elsewhere.",
     "Note the $3.00 charge per category, paid to the submission platform."],
    ["pangyrus", "$30 per piece", "paypal", "reading periods", "undercurrents",
     "comics", "no ai", "boston literary magazine"],
    "accepted",
    "We accept simultaneous submissions, asking that you notify us immediately "
    "if a work is accepted elsewhere. "
    f"— https://pangyrus.submittable.com/submit (read {READ})"))

NEW.append(rec(
    "kweli-journal", "Kweli Journal",
    "Payment stated, but no amount published",
    "Kweli Journal: pays contributors, amount not published, reading to 30 May",
    "Kweli Journal states that payment for published work is made after "
    "publication, but does not publish an amount. It reads fiction, nonfiction "
    "and poetry from 1 September to 30 May each year, asking for one prose piece "
    "of up to 6,000 words or up to three poems totalling six pages, previously "
    "unpublished, and refuses work that endorses discrimination or features "
    "gratuitous violence or sexual content. Simultaneous submissions are "
    "accepted when indicated, all published work is archived online, and "
    "submissions go through Submittable.",
    "https://www.kwelijournal.org/submit",
    "http://kwelijournal.submittable.com/", None,
    "Submittable during the reading period; send prose in one file and up to "
    "three poems in one file, in doc, rtf or pdf.",
    src("Kweli Journal - Submit (official)",
        "https://www.kwelijournal.org/submit"),
    intl("No country restriction is stated; the journal is named for \"truth\" "
         "in Swahili and describes itself as truth from the diaspora's boldest "
         "voices."),
    ["fiction", "creative-nonfiction", "poetry"],
    "Fiction, nonfiction and poetry",
    pay(None, None, None, "Payment stated, amount not published",
        "Official page: \"Payment is after publication.\" The page does not "
        "state an amount, so none is recorded here - the rate is not published.",
        "After publication"),
    {"min": None, "max": 6000,
     "display": "One short story, self-contained novel excerpt or creative "
                "nonfiction piece of up to 6,000 words; up to three poems "
                "totalling no more than six pages."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Reading period 1 September to 30 May; work received outside it "
                "is not read",
     "windowStart": "2026-09-01", "windowEnd": "2027-05-30", "recurring": True},
    "not-stated",
    ["Fiction, nonfiction and poetry from the African diaspora and beyond, in "
     "the journal's words truth from the boldest voices.",
     "One prose piece up to 6,000 words, or up to three poems totalling six "
     "pages.",
     "Reading a few issues of the journal first, which the guidelines strongly "
     "encourage."],
    ["Previously published work.",
     "Work that endorses discrimination including racism, homophobia, sexism "
     "and xenophobia.",
     "Work featuring gratuitous violence or sexual content.",
     "Submissions sent outside the 1 September to 30 May reading period, which "
     "remain unread."],
    ["Read the guidelines at https://www.kwelijournal.org/submit before "
     "sending.",
     "Submit through Submittable between 1 September and 30 May.",
     "Send prose in one file up to 6,000 words, or up to three poems in one "
     "file, in doc, rtf or pdf.",
     "Work must be previously unpublished, and simultaneous submissions should "
     "be indicated.",
     "Know that the page states payment is made after publication but does not "
     "publish an amount."],
    "Not stated beyond archiving: \"All published work will be archived "
    "online.\"",
    ["Read the guidelines page before sending.",
     "Submit via Submittable during the 1 September to 30 May reading period.",
     "Send one prose piece up to 6,000 words, or up to three poems of six pages "
     "in total.",
     "Indicate simultaneous submissions and notify the editors immediately on "
     "acceptance elsewhere.",
     "Note that the journal states payment after publication but publishes no "
     "amount."],
    ["kweli journal", "payment after publication", "amount not published",
     "diaspora", "september to may", "swahili", "submittable",
     "unpublished work only"],
    "accepted",
    "Simultaneous submissions are acceptable as long as they are indicated as "
    "such. Authors must immediately notify the editors if said work has been "
    "selected for publication in another periodical, either in print or online. "
    f"— https://www.kwelijournal.org/submit (read {READ})"))


BASE = {
    "exposition-review": ("", "International"),
    "mulberry-literary": ("", "International"),
    "claudine-a-literary-magazine": ("", "International"),
    "nimrod-international-journal": ("US", "United States"),
    "old-pal": ("", "International"),
    "overtime": ("US", "United States"),
    "pacifica-literary-review": ("", "International"),
    "palette-poetry": ("", "International"),
    "pangyrus": ("", "International"),
    "kweli-journal": ("", "International"),
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
