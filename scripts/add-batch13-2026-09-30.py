#!/usr/bin/env python3
"""Add verified writing-market batch 13 (2026-09-30).

Seven NEW markets. Every figure below was read off the publication's own
guidelines page on 2026-09-30; the raw text of each page is kept under
research/rebuild/raw/<slug>.txt so the reading can be re-checked without
re-fetching.

WHY THIS BATCH NEEDED A REBUILD FIRST
-------------------------------------
Batches 5-12 all say "read from the batch-4 backlog. No crawling." That
backlog lived at research/batch4/ - 450 saved guidelines pages - and it was
never committed on any branch (git log --all -- 'research/*' returns nothing;
it is not gitignored, just absent). A fresh clone therefore has no backlog and
batches 5-12 cannot be continued by the method they describe.

The backlog was rebuilt the same way batch 4 built it: the Poets & Writers
Literary Magazines directory was scraped for magazine names and each
magazine's OWN submissions URL.

    pw.org 35 listing pages -> 849 magazine slugs
    -> 849 detail pages -> 84 had a submission-guidelines URL at read time
    -> 62 not already on this desk -> 52 pages fetched -> 7 shipped here

That is 12 fewer than batch 4's yield of 450 usable pages. The difference is
not a shortage of markets: pw.org began rate-limiting the detail pages, and
the remaining 765 were still queued when this batch shipped. The queued pages
are the backlog for batch 14 and are kept under research/rebuild/.

pw.org was used ONLY for names and official URLs, exactly as in batch 4. It
publishes pay notes and reading-fee flags of its own; none were used, and none
were copied. Every rate, length, right, fee and AI statement below comes from
the publication's own page.

WHAT WAS READ, AND ONE THING THAT WAS NOT FLATTENED
---------------------------------------------------
Epiphany's public page carries the sentence "No writing that is plagiarized or
created with the use of AI will be accepted." It appears twice, and both times
inside a DIFFERENT application: once in the Fresh Voices Fellowship section and
once in the art-submissions section. It is not attached to the general writing
submissions, whose own block states windows and pay and nothing about AI.
The record therefore says aiPolicy "not-stated" for writing. Flattening a
fellowship condition into a magazine-wide policy would have invented a rule
the magazine has not published for the work this record is about.

Two windows open the day after this batch was read, and both are recorded as
upcoming rather than open:
  brick             October 1 - October 31
  bracken           October 1 - November 30
32 Poems' window closes ON the verification date (August 1 - September 30), so
the record is "open" with deadline 2026-09-30 and the next window named in the
submission steps. It is accurate for the date it was read and no further.

A Velvet Giant, Brick and 32 Poems publish no response time and no rights
line on the pages read; those fields say so rather than borrowing a figure.

Simultaneous submissions are recorded in the shape main's Phase 4 established:
a three-value field plus, where the publication actually states a policy, the
sentence it was read from with its URL and date. Nine-tenths of the mistake
Phase 4 documented was substring matching, so nothing here is classified by
keyword. Brick's "We will read simultaneous submissions", Bracken's
"Simultaneous submissions are considered" and Metphrastics' "Absolutely fine"
were each read as sentences before being recorded; the other four say nothing
and are left as not-stated.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-30"


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

# ------------------------------------------- 1 Brick
NEW.append(rec(
    "brick-a-literary-journal", "Brick", "Literary non-fiction: essays, reviews and memoir",
    "Brick: $65-720 by length, opens October 1 and April 1",
    "Brick pays $65 to $720 depending on the length of accepted work, on publication, "
    "plus two copies of the issue and a one-year subscription. It publishes literary "
    "non-fiction only and tends toward 1,000 to 5,000 words. Submissions open twice a "
    "year, October 1 to 31 and April 1 to 30, through Submittable only.",
    "https://brickmag.com/submissions/",
    "https://brickmag.com/submissions/", None,
    "Submittable only - mailed or emailed submissions are not read, returned or answered",
    src("Brick - Submissions (official)", "https://brickmag.com/submissions/"),
    intl(),
    ["essays", "creative-nonfiction", "reviews", "interviews"],
    "Literary non-fiction - essays, reviews, interviews and memoir",
    pay("USD", 65, 720, "$65-720 depending on the length of accepted work",
        "Official submissions page: Brick pays its contributors upon publication and "
        "offers $65-720, depending on the length of accepted work, plus two copies of the "
        "issue the work appears in and a one-year subscription to the magazine. The "
        "figure is a range set by length, so both ends are recorded rather than a single "
        "headline number.",
        "Upon publication"),
    {"min": 1000, "max": 5000,
     "display": "No formal word limit; the magazine tends toward 1,000-5,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "upcoming", {"display": "The October window runs 1 October 2026 to 31 October "
                 "2026; Brick also opens 1 April", "openingDate": "2026-10-01",
                 "recurring": True}, "prohibited",
    ["Literary non-fiction - essays, reviews, interviews, belle lettres, memoir and "
     "translations.",
     "Finished, polished work with formal integrity that takes a creative approach to "
     "rich ideas.",
     "Writers of underrepresented identities - including but not limited to writers who "
     "are Black, Indigenous, people of colour, queer, non-binary, Deaf and/or disabled - "
     "are especially encouraged to submit."],
    ["Submissions that make use of AI-generated content.",
     "Pieces previously submitted to Brick, including revisions.",
     "More than one piece at a time - multiple submissions are automatically rejected.",
     "Mailed or emailed submissions."],
    ["Submissions open October 1 to 31 and April 1 to 30 only.",
     "Submit through Submittable.",
     "Send one piece at a time and wait for a response before sending more.",
     "Pieces run toward 1,000-5,000 words, though no limit is set.",
     "Read a recent issue before submitting - the magazine asks for it."],
    "Not stated on the submissions page.",
    ["Read https://brickmag.com/submissions/ before sending.",
     "Brick opens twice a year: October 1-31 and April 1-30. This record was read on "
     "2026-09-30, the day before the October window opened.",
     "Submit through Submittable only. Mailed or emailed work is not read.",
     "One piece at a time. Wait for the answer before sending the next.",
     "Free submissions reach their cap well before the window ends; the paid "
     "submit-and-subscribe options stay open, and the magazine asks you to get in touch "
     "if that is a barrier."],
    ["brick", "literary non-fiction", "$65-720", "1000-5000 words",
     "two submission windows", "submittable only", "no ai-generated content"],
    sim="accepted",
    simnote=("We will read simultaneous submissions, but let us know if your manuscript "
             "is accepted for publication elsewhere, and you can withdraw the piece via "
             "Submittable. - https://brickmag.com/submissions/ (read 2026-09-30)"),
))

# ------------------------------------------- 2 Epiphany
NEW.append(rec(
    "epiphany-magazine", "Epiphany", "Fiction, poetry and essays",
    "Epiphany: $75 per poem, $175 per essay or story in print",
    "Epiphany pays $75 per poem and $175 per essay or story in print, and $50 per poem "
    "and $150 per essay or story for online-only publication. Print submissions run in "
    "two windows, May 1 to June 15 and November 1 to December 15, and the magazine "
    "typically responds within five to six months.",
    "https://epiphanymagazine.org/submit",
    "https://epiphanymagazine.org/submit", None,
    "Submission manager - see the submit page",
    src("Epiphany - Submit (official)", "https://epiphanymagazine.org/submit"),
    intl(),
    ["fiction", "poetry", "essays", "creative-nonfiction"],
    "Fiction, poetry and essays",
    pay("USD", 50, 175,
        "Print: $75 per poem, $175 per essay or story. Online only: $50 per poem, "
        "$150 per essay or story",
        "Official submit page: in print, Epiphany pays $75 per poem and $175 per essay or "
        "story. All print submissions are also considered for online-only publication, "
        "which pays $50 per poem and $150 per essay or story. Art is paid on a sliding "
        "scale starting at $75 for interior art and $300 for cover art. The recorded "
        "minimum and maximum are the across-the-board low and high of the writing rates; "
        "the display text carries the full breakdown so the two venues are not confused.",
        "Not stated"),
    {"min": None, "max": None,
     "display": "No length limit stated on the public submit page"},
    {"label": "Five to six months", "band": "3-plus-months", "official": True},
    "closed", None, "not-stated",
    ["Stories, poems, essays and genre-bending work.",
     "Writing that fits the range of work the magazine has already published."],
    ["Sending before reading recent work - the magazine asks you to familiarize yourself "
     "with it first."],
    ["Submissions for the Fall/Winter print issue run May 1 to June 15.",
     "Submissions for the Spring/Summer print issue run November 1 to December 15.",
     "Submit through the magazine's submission manager.",
     "Those facing financial hardship may request a fee waiver through the contact form "
     "on the website."],
    "Not stated on the public submit page.",
    ["Read https://epiphanymagazine.org/submit before sending.",
     "Both print windows were closed on the date this record was read (2026-09-30). The "
     "Spring/Summer window opens November 1 and closes December 15.",
     "Print submissions are considered for online-only publication automatically, at the "
     "lower online rate.",
     "Expect five to six months for a response.",
     "If a fee is a barrier, ask for a waiver through the contact form."],
    ["epiphany", "$75 per poem", "$175 per essay", "print and online rates",
     "two submission windows", "five to six months", "fee waiver"],
    sim="not-stated",
    simnote=None,
))

# ------------------------------------------- 3 Bracken
NEW.append(rec(
    "bracken", "Bracken", "Poetry and art",
    "Bracken: $30 per piece, $3 to submit, opens October 1",
    "Bracken pays $30 for each previously unpublished piece of writing and $30 per art "
    "feature, with a negotiated rate for cover art. Poetry submissions cost $3, waived "
    "on request if the fee is prohibitive. It reads twice a year, March 1 to April 30 "
    "and October 1 to November 30, and replies to all submitters within four months.",
    "https://brackenmagazine.com/submit",
    "https://brackenmagazine.com/submit", None,
    "Submittable only - emailed submissions are deleted unread",
    src("Bracken - Submit (official)", "https://brackenmagazine.com/submit"),
    intl(),
    ["poetry", "translation", "other"],
    "Poetry and art",
    pay("USD", 30, 30,
        "$30 per piece of writing; $30 per art feature; cover art negotiated",
        "Official submit page: Bracken pays $30 for each previously unpublished piece of "
        "writing, $30 per art feature (which may be a single image or several), and a "
        "negotiated rate for cover art. The poetry rate is a flat $30 per accepted piece, "
        "not per poem in a packet.",
        "Not stated"),
    {"min": None, "max": None,
     "display": "Up to 5 poems in a single document; no length limit stated"},
    {"label": "Four months", "band": "3-plus-months", "official": True},
    "upcoming", {"display": "The October window runs 1 October 2026 to 30 November "
                 "2026", "openingDate": "2026-10-01", "recurring": True}, "prohibited",
    ["Poetry and art that correspond to the aesthetic of the journal.",
     "Creative work that helps the reader feel an underlying oneness with all of nature.",
     "Previously unpublished work.",
     "Poetry in translation, with the originals included and permission from the poet or "
     "rights holder confirmed in the cover letter."],
    ["AI-generated or AI-assisted work - Bracken does not consider it.",
     "Emailed submissions - they are deleted unread.",
     "More than one submission during the same submission window.",
     "For translations, sending work without permission from the poet or copyright "
     "holder."],
    ["Submissions run March 1 to April 30 and October 1 to November 30.",
     "Submit through Submittable only. Email is not read.",
     "Send once per submission window.",
     "Poetry: up to 5 poems in one document. A Word document is preferred; PDF is "
     "accepted.",
     "The $3 poetry submission fee can be waived - email info@brackenmagazine.com if it "
     "is prohibitive. Do not send work to that address."],
    "Bracken purchases first worldwide English-language serial and electronic rights for "
    "written work. The author retains all other rights. Art is featured on the site and "
    "promoted on social media; no other rights are requested.",
    ["Read https://brackenmagazine.com/submit before sending.",
     "The October window runs October 1 to November 30; this record was read on "
     "2026-09-30, the day before it opened.",
     "Submit through Submittable. Emailed work is deleted unread.",
     "Send up to 5 poems in a single document.",
     "If $3 is prohibitive, ask for the fee to be waived rather than not submitting."],
    ["bracken", "$30 per piece", "$3 submission fee", "poetry", "art",
     "first serial rights", "no ai-assisted work", "four months"],
    sim="accepted",
    simnote=("We seek work that is previously unpublished. Simultaneous submissions are "
             "considered. We ask that you let us know promptly via Submittable if your "
             "piece has been accepted elsewhere. - https://brackenmagazine.com/submit "
             "(read 2026-09-30)"),
))

# ------------------------------------------- 4 32 Poems
NEW.append(rec(
    "32-poems", "32 Poems", "Poetry",
    "32 Poems: $25 per poem plus two copies, $3 to submit online",
    "32 Poems pays $25 per poem and two copies of the issue. Electronic submissions cost "
    "$3, waived for current subscribers, and fee-free postal submissions are still "
    "accepted. It reads February 1 to March 31 and August 1 to September 30, publishes "
    "shorter poems that fit on a single page, and considers no more than five poems at a "
    "time.",
    "https://32poems.com/submission-guidelines",
    "https://32poems.com/submission-guidelines", None,
    "Submittable or Duosuma; fee-free postal submissions also accepted",
    src("32 Poems - Poetry Guidelines (official)",
        "https://32poems.com/submission-guidelines"),
    intl(),
    ["poetry"], "Poetry",
    pay("USD", 25, 25, "$25 per poem plus two copies of the issue",
        "Official guidelines page: contributors receive $25 per poem and two copies of "
        "the issue in which their writing appears. The rate is per poem, so a packet of "
        "five accepted poems is five payments, not one.",
        "Not stated"),
    {"min": None, "max": None,
     "display": "Shorter poems that fit on a single page; up to 5 poems per submission"},
    {"label": "Often within a few weeks; query after 90 days",
     "band": "2-4-weeks", "official": True},
    "open", {"display": "The August-September window runs 1 August 2026 to "
             "30 September 2026", "windowStart": "2026-08-01",
             "windowEnd": "2026-09-30", "recurring": True}, "not-stated",
    ["Poems that fit on a single page as a rule, though longer work is occasionally "
     "accepted.",
     "Remarkable work - the magazine makes exceptions for it."],
    ["Translations.",
     "Work previously published in print or online.",
     "More than five poems in one submission.",
     "More than one active submission at a time."],
    ["Read the guidelines at https://32poems.com/submission-guidelines first.",
     "The reading window runs February 1 to March 31 and August 1 to September 30.",
     "Send no more than five poems in a single document.",
     "Keep one active submission at a time.",
     "Electronic submissions carry a $3 processing fee, waived for current subscribers. "
     "Fee-free postal submissions remain available."],
    "Not stated on the guidelines page.",
    ["Read https://32poems.com/submission-guidelines before sending.",
     "This record was read on 2026-09-30, the closing day of the August 1 to September 30 "
     "window. The next window opens February 1.",
     "Send up to five poems in one document, one active submission at a time.",
     "Poets with no answer after 90 days are encouraged to query.",
     "Subscribers do not pay the $3 electronic fee, and postal submissions are free."],
    ["32 poems", "$25 per poem", "two contributor copies", "$3 processing fee",
     "single page poems", "five poems maximum", "no translations"],
    sim="not-stated",
    simnote=None,
))

# ------------------------------------------- 5 Metphrastics
NEW.append(rec(
    "metphrastics", "Metphrastics", "Ekphrastic poetry about works in the Met",
    "Metphrastics: $10 per poem, no fee, open year-round, worldwide",
    "Metphrastics pays $10 per poem and charges no submission fee. It publishes "
    "ekphrastic poems responding to works in the Metropolitan Museum of Art's permanent "
    "collection and special exhibitions, welcomes submissions year-round from poets "
    "around the world, and does not accept AI-generated work.",
    "https://metphrastics.com/submit",
    "mailto:metphrastics@gmail.com", "metphrastics@gmail.com",
    "Email - up to three poems with a note on the works referenced",
    src("Metphrastics - Submit (official)", "https://metphrastics.com/submit"),
    worldwide("Poets around the world are explicitly welcome: the submit page states "
              "that all styles are welcome from poets around the world."),
    ["poetry"], "Ekphrastic poetry",
    pay("USD", 10, 10, "$10 per poem",
        "Official submit page: payment is $10 per poem. There is no fee to submit, so "
        "the $10 is a rate paid to the poet rather than a fee charged to them.",
        "Not stated"),
    {"min": None, "max": None,
     "display": "No length limit stated; up to 3 poems per submission"},
    {"label": "Two to three weeks after the deadline",
     "band": "2-4-weeks", "official": True},
    "rolling", None, "prohibited",
    ["Ekphrastic poems responding to works in the Metropolitan Museum of Art's permanent "
     "collection or special exhibitions - painting, drawing, sculpture, photography, "
     "costume, musical instruments, and the Met building itself.",
     "Poems about works currently on display are favoured, though it is not required "
     "unless a call says so.",
     "Poems that engage with the artwork rather than choosing an artwork to fit a "
     "finished poem.",
     "Work about regions and genres the journal has covered least - it names Latin "
     "America, Ancient America and Africa as gaps."],
    ["AI-generated work.",
     "Poems about works in other museums - only ekphrastic poems about artwork at the Met "
     "are considered and responded to.",
     "Submissions without a note identifying the artwork referenced."],
    ["Read https://metphrastics.com/submit before sending.",
     "Email up to three poems to metphrastics@gmail.com.",
     "Include a note about the work or works the poems reference and a 2-3 line bio.",
     "Name the artwork in the cover letter.",
     "Reprints are occasionally considered - say where the poem first appeared."],
    "Not stated on the submit page.",
    ["Read https://metphrastics.com/submit before sending.",
     "Submissions are welcome year-round, so there is no window to wait for. The Fall "
     "2026 call on the theme of Wounds asked for poems by September 15.",
     "Email up to three poems with a note on the artworks and a short bio.",
     "Only poems about works at the Met are answered, so a poem about another museum's "
     "collection will not get a reply.",
     "Simultaneous submissions are welcome - say so if a poem is taken elsewhere."],
    ["metphrastics", "$10 per poem", "no fee", "ekphrastic", "met museum",
     "poetry", "year-round", "no ai-generated work"],
    sim="accepted",
    simnote=("Simultaneous Submissions: Absolutely fine. Just let us know if a piece is "
             "accepted elsewhere. - https://metphrastics.com/submit (read 2026-09-30)"),
))

# ------------------------------------------- 6 A Velvet Giant
NEW.append(rec(
    "a-velvet-giant", "A Velvet Giant", "Genreless literary work",
    "A Velvet Giant: $20 per author on publication, six-month response",
    "A Velvet Giant is a genreless literary journal that pays $20 per author on "
    "publication from donated funds. It asks for first serial rights, asks that future "
    "publication of the work acknowledge the journal, and says to expect a response "
    "within no more than six months. Submissions were closed when this record was read.",
    "https://avelvetgiant.com/submit",
    "https://avelvetgiant.com/submit", None,
    "Submissions portal - see the submit page",
    src("A Velvet Giant - Submission guidelines (official)",
        "https://avelvetgiant.com/submit"),
    intl(),
    ["fiction", "poetry", "essays", "creative-nonfiction", "other"],
    "Genreless literary work",
    pay("USD", 20, 20, "$20 per author on publication",
        "Official submission guidelines: A Velvet Giant pays its contributors $20 per "
        "author upon publication. The page states that donated funds are used to pay the "
        "illustrator and all contributors and to maintain the website - so the rate "
        "depends on donations, which is worth knowing before submitting.",
        "Upon publication"),
    {"min": None, "max": None,
     "display": "No length limit stated on the submission guidelines"},
    {"label": "No more than six months", "band": "3-plus-months", "official": True},
    "closed", None, "not-stated",
    ["Genreless literary work - the journal describes itself as a genreless literary "
     "journal and points writers to its archive to see what it publishes.",
     "Work by genderqueer and LGBTQIA+ people, women, people of color, global writers, "
     "people living with disability and/or chronic pain or illness, and survivors of "
     "domestic violence and sexual assault - the journal says it is especially "
     "interested in these writers."],
    ["Work that is misogynistic, racist, homophobic, transphobic, antisemitic, or "
     "otherwise oppressive or exploitative. The journal's words: if you're not sure, "
     "don't send it."],
    ["Read the about page and the archive before submitting.",
     "Submissions were closed on the date this record was read (2026-09-30).",
     "Expect a response within no more than six months.",
     "Acknowledge A Velvet Giant in any future publication of accepted work."],
    "The journal asks for first serial rights, and asks that any future publications of "
    "accepted work acknowledge A Velvet Giant.",
    ["Read https://avelvetgiant.com/submit before sending.",
     "Submissions were CLOSED on the date this record was read; check the page before "
     "preparing a submission.",
     "Read the about page and a previous issue first - the journal tells you to.",
     "Expect up to six months for a response.",
     "Payment is $20 per author on publication and is funded by donations."],
    ["a velvet giant", "$20 per author", "genreless", "first serial rights",
     "six months", "donation funded", "submissions closed"],
    sim="not-stated",
    simnote=None,
))

# ------------------------------------------- 7 Thriller Magazine
NEW.append(rec(
    "thriller-magazine", "Thriller Magazine", "Short crime and thriller fiction",
    "Thriller Magazine: $15 per story, 1,000-7,000 words, feedback on every submission",
    "Thriller Magazine pays $15 for accepted short stories of 1,000 to 7,000 words. "
    "Submissions carry a non-refundable $4.49 fee and every submission receives detailed "
    "editorial feedback, which is unusual at this price. It was reading for its December "
    "2026 issue when this record was checked.",
    "https://thrillermagazine.org/submissions",
    "https://thrillermagazine.org/submissions", None,
    "Online submission form",
    src("Thriller Magazine - Submissions (official)",
        "https://thrillermagazine.org/submissions"),
    intl(),
    ["fiction"], "Short crime and thriller fiction",
    pay("USD", 15, 15, "$15 per accepted short story",
        "Official submissions page: pay is $15 for accepted short stories. The page also "
        "states a submission fee: $4.49, non-refundable. The fee is charged to the writer "
        "and is not recorded as payment - at $15 for an accepted story against $4.49 to "
        "submit, a writer needs the fee to be worth the feedback as well as the rate.",
        "Not stated"),
    {"min": 1000, "max": 7000, "display": "1,000-7,000 words"},
    {"label": "Four to five weeks", "band": "1-3-months", "official": True},
    "open", None, "not-stated",
    ["Short stories in the crime and thriller space, 1,000 to 7,000 words.",
     "Finished stories - the magazine reads everything and returns editorial feedback."],
    ["Stories outside the 1,000 to 7,000 word range.",
     "Previously published work, unless declared honestly in the submission form."],
    ["Read https://thrillermagazine.org/submissions before sending.",
     "Submit through the online form.",
     "Keep stories to 1,000-7,000 words.",
     "Pay the non-refundable $4.49 submission fee.",
     "Declare honestly whether the story has been previously published."],
    "Not stated on the submissions page.",
    ["Read https://thrillermagazine.org/submissions before sending.",
     "Submissions were open for the December 2026 issue on the date this record was read.",
     "Stories run 1,000 to 7,000 words.",
     "The $4.49 submission fee is non-refundable and applies whether or not the story is "
     "accepted - count it against the $15 rate.",
     "Every submission receives detailed editorial feedback, which is the main thing "
     "beyond the fee that separates this from most $15 markets."],
    ["thriller magazine", "$15 per story", "$4.49 submission fee", "1000-7000 words",
     "crime fiction", "thriller", "editorial feedback", "four to five weeks"],
    sim="not-stated",
    simnote=None,
))


BASE = {
    "brick-a-literary-journal": ("", "International"),
    "epiphany-magazine": ("", "International"),
    "bracken": ("", "International"),
    "32-poems": ("", "International"),
    "metphrastics": ("", "International"),
    "a-velvet-giant": ("", "International"),
    "thriller-magazine": ("", "International"),
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
        # deadline is a structured object in this dataset (display/date/windowEnd/
        # openingDate/recurring), never a bare string. build-writing-first.py's
        # deadline_passed() calls .get() on it, so a string crashes the build.
        # Batch 13 shipped three string deadlines and the build caught them; this
        # guard is why they cannot come back.
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
# Held back from batch 13, and why:
#
#   hootreview.com      batch 4 already held this for the same reason and it has
#       not changed: the payout is described in a comment thread ("average
#       around $25", "30% of the whole $2") rather than in the guidelines. It
#       still cannot be recorded as a rate.
#   i70review           $15 entry fee and a $1,000 cash prize. That is a
#       competition, not a rate for published work - the StoryQuarterly
#       precedent from batch 12. The page states no contributor rate.
#   tadpolepress        $5 to enter, $50 to one winner every other month. Same
#       contest-prize problem, and the page mixes a contest with a $1,000
#       first prize.
#   humanaobscura       States plainly that it is not able to offer payment at
#       this time. Held for an unpaid-market batch, as batch 4 did with
#       skyislandjournal and pitheadchapel.
#   passagesnorth       "does not pay contributors at this time". Same hold.
#   mid-american-review No fee, copies only - "Contributing authors receive two
#       complimentary copies". Unpaid. Same hold.
#   2river, aaduna, tinge, boomerlitmag, thin-skin
#       All state clearly that they do not pay. Recordable, but not paying
#       markets, and the index policy for this desk is research-backed PAID
#       opportunities. Batch 4 set the precedent of holding them.
#   reliefjournal       $3 submission fee, contributor copy, no stated cash
#       rate. Fee-and-copy model; verify in a later pass before recording.
#
# 765 pw.org detail pages were still queued for fetching when this batch
# shipped (pw.org rate-limited the run). They are the backlog for batch 14.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
