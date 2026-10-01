"""Add verified writing-market batch 17 (2026-10-01).

Five NEW markets, read off each publication's OWN guidelines page on 2026-10-01.
The raw text of every page is kept under research/rebuild/raw/<slug>.txt.

WHAT THIS BATCH HAD TO KEEP APART
---------------------------------
Four of the five pay a small flat sum, and two of those pay only *on one route*.
The route matters more than the number here:

  * Frontier Poetry pays $50 per poem on New Voices - "Always open. Always free."
    The same page runs a challenge that charges $20 to enter and pays prizes. A
    record that quotes "$50 per poem" without the route, or that folds in the $20,
    is wrong twice over: it invents a fee-free rate that is route-specific and it
    turns a writer's cost into a payout.
  * Infrarrealista Review pays $100 for reviews and essays but $50 for interviews
    and $50 for a poem or story in its newspaper section. The range is real.
  * Half Mystic pays US$20 a piece in the journal and royalties on manuscripts.
    A royalty is not a rate per accepted piece, so only the journal figure is
    recorded as pay and the manuscript model is named in the conditions.
  * The Literary Fantasy Magazine pays $10 on the web and says print pays more -
    without publishing the print figure. Only the stated rate is recorded.

TWO MONTH-LEVEL DEADLINES, RECORDED AS SUCH
-------------------------------------------
Half Mystic says submissions "close in April 2027" and The Literary Fantasy
Magazine announces "a special submission window in October" (2026). Neither page
gives a day. The display text repeats the page's own wording - "the page states
the month, not a day" - and the sort key uses the last day of that month purely
so the record can be ordered. No day is claimed to be the publication's.

A FALSE POSITIVE WORTH NAMING
-----------------------------
Emerald City Ghosts matched the payment filter with "Do We Pay? Unfortunately,
no." It is unpaid and stays out of the batch.
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
    "frontier-poetry", "Frontier Poetry",
    "New Voices: $50 per poem, always free to submit, open to emerging poets",
    "Frontier Poetry: $50 per poem on the free New Voices route",
    "Frontier Poetry pays $50 for every poem selected on its New Voices route, which is "
    "always open and always free to enter, for poets with no more than one full-length "
    "collection. Submissions run to five poems and ten pages, are open internationally, "
    "take eight to twelve weeks for a reply, and AI-generated work is refused. The "
    "separate Discover New Art Prize charges $20 to enter and is not recorded as the rate.",
    "https://frontierpoetry.com/submit", "https://frontierpoetry.com/submit",
    None, "Online form through Submittable; the New Voices route is free.",
    src("Frontier Poetry - Submissions (official)", "https://frontierpoetry.com/submit"),
    worldwide("Official page: \"Submissions are open internationally, to any poet "
              "writing primarily in English. Code-switching/meshing is warmly "
              "welcomed.\""),
    ["poetry"],
    "Poetry, on the New Voices route",
    pay("USD", 50, 50, "$50 per poem selected on the New Voices route",
        "Official page, New Voices: \"We are thrilled to offer significant payment to "
        "our partner poets: $50 per poem.\" And: \"New Voices Free - Always a free "
        "way to submit and we always pay for the work. We pay new poets $50 per poem "
        "selected.\" The Discover New Art Prize is a separate challenge with a $20 "
        "entry charge and prize money, and neither is the rate for published work.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No more than ten pages and no more than five poems, all in one "
                "document; a cover letter with publication history is required"},
    {"label": "Eight to twelve weeks", "band": "1-3-months", "official": True},
    "open", None, "prohibited",
    ["Poets the page calls new and emerging - no more than one full-length published "
     "or forthcoming collection at the time of submission.",
     "Poets from historically under-represented and marginalised groups, whom the "
     "New Voices route is designed to reach.",
     "Work in English by poets anywhere, with code-switching and meshing welcomed.",
     "Up to five poems and ten pages, submitted together, with a cover letter."],
    ["AI-generated work: \"Frontier Poetry does not consider or review AI-generated "
     "work. Submissions utilizing AI tools will be automatically declined.\"",
     "Multiple submissions - all poems must go in one document.",
     "More than five poems or more than ten pages.",
     "Poets with more than one full-length collection published or forthcoming."],
    ["Read https://frontierpoetry.com/submit before sending.",
     "Submit through the New Voices route, which is free; other routes and the "
     "Discover New Art Prize carry their own charges.",
     "Send no more than five poems and no more than ten pages, all in one document.",
     "Include a cover letter with your publication history.",
     "Allow eight to twelve weeks for a response."],
    "Frontier Poetry holds first publication rights for three months after "
    "publication, after which rights revert to the author.",
    ["Read https://frontierpoetry.com/submit before sending.",
     "Use the New Voices Free option: always open, always free, and paid.",
     "Send up to five poems in a single document with a cover letter.",
     "Note the eligibility line: new and emerging poets, with no more than one "
     "full-length collection out or forthcoming.",
     "Expect eight to twelve weeks for a reply."],
    ["frontier poetry", "$50 per poem", "new voices", "free to submit",
     "emerging poets", "no ai", "simultaneous submissions",
     "poetry submissions", "international"],
    "accepted",
    "We accept simultaneous submissions—just please send us a note if your work is "
    "picked up elsewhere (we want to say congrats)! "
    f"— https://frontierpoetry.com/submit (read {READ})"))

NEW.append(rec(
    "half-mystic-journal", "Half Mystic Journal",
    "Journal contributors: US$20 per accepted piece, closing April 2027",
    "Half Mystic Journal: US$20 per piece, submissions close April 2027",
    "Half Mystic Journal pays US$20 for each piece it accepts into its Fioritura issue, "
    "with submissions closing in April 2027. The journal takes poetry, essays, fiction "
    "and art on a themed call, alongside a separate full-length manuscript route paying "
    "royalties rather than a flat rate. It states nothing on its page about fees, "
    "response times, simultaneous submissions or AI.",
    "https://halfmystic.com/guidelines", "https://halfmystic.com/guidelines",
    None, "Online form through Submittable.",
    src("Half Mystic Journal - Guidelines (official)",
        "https://halfmystic.com/guidelines"),
    intl(),
    ["poetry", "essays", "fiction", "creative-nonfiction"],
    "Poetry, essays, fiction and art for the journal; full-length manuscripts separately",
    pay("USD", 20, 20, "US$20 per accepted piece in the journal",
        "Official page, journal submissions: \"We pay US$20 per accepted piece, and "
        "submissions close in April 2027.\" The separate manuscript route is paid in "
        "royalties - \"We pay competitive royalties\" - and is a different model, not "
        "a rate for an accepted piece.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No word or page limit stated for journal submissions; manuscript "
                "submissions are full-length works of at least 60 pages"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Submissions for the Fioritura issue close in April 2027 (the page "
                "states the month, not a day)",
     "windowEnd": "2027-04-30", "recurring": False},
    "not-stated",
    ["Journal work on the announced theme - Fioritura, described as devotion wearing "
     "the voice of decoration.",
     "Poetry, essays, fiction and art, sent with a cover letter and a description of "
     "what music means to you.",
     "Full-length manuscripts of at least 60 pages, submitted on the separate press "
     "route."],
    ["Chapbooks on the manuscript route: the page says it publishes only full-length "
     "manuscripts.",
     "Work that ignores the announced theme for the journal issue."],
    ["Read https://halfmystic.com/guidelines before sending.",
     "Submit through Submittable; the journal, press and blog all use it.",
     "Include a cover letter with a biographical note, acknowledgements of previous "
     "publications, and a description of what music means to you.",
     "Journal submissions close in April 2027.",
     "Manuscript submissions need at least 60 pages; no chapbooks."],
    "Not stated on the guidelines page.",
    ["Read https://halfmystic.com/guidelines before sending.",
     "Submit through Submittable.",
     "Write to the Fioritura theme for the journal, and send the cover letter the "
     "page asks for.",
     "Send before the April 2027 close; the page gives no day within the month."],
    ["half mystic journal", "us$20 per piece", "fioritura", "submittable",
     "april 2027", "royalties for manuscripts", "art submissions"],
    "not-stated", None))

NEW.append(rec(
    "infrarrealista-review", "Infrarrealista Review",
    "$100 per review or essay, $50 per interview or newspaper piece",
    "Infrarrealista Review: $100 reviews and essays, $50 interviews and poems",
    "Infrarrealista Review pays $100 per book review or cultural-criticism essay and "
    "$50 per interview, and pays $50 a publication for poems and short fiction in its "
    "Letras y Disparates section in the Caldwell-Hays Examiner. It runs open calls, "
    "asks for no rights to contributors' work, and states no policy on fees, "
    "simultaneous submissions, AI or response times.",
    "https://infrarrealistas.org/submission",
    "https://infrarrealistas.org/submission", None,
    "Online form through the site; the page lists its calls as currently open.",
    src("Infrarrealista Review - Submission (official)",
        "https://infrarrealistas.org/submission"),
    intl("Official page: the review prioritises \"radical writers from Texas, "
         "especially those from the central Texas area\", and states no country "
         "restriction on submitting."),
    ["reviews", "interviews", "essays", "poetry", "fiction"],
    "Book reviews, interviews, cultural criticism, poetry and fiction",
    pay("USD", 50, 100,
        "$100 per review or essay, $50 per interview, $50 per newspaper publication "
        "of a poem or short story",
        "Official page, by section: reviews - \"We pay $100 per review.\" / interviews "
        "- \"We pay $50 per interview.\" / nonfiction and cultural criticism - \"We "
        "pay $100 per essay.\" / Letras y Disparates in the Caldwell-Hays Examiner - "
        "\"CHE pays $50 per publication.\"",
        "Not publicly stated"),
    {"min": None, "max": 1500,
     "display": "Fiction in the Letras y Disparates section: 1,500-word limit. Poems "
                "in that section: up to three sent. No limit stated for reviews or "
                "essays."},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Reviews of books from small presses, books by Texan writers, and out-of-print "
     "books from Texas presses and writers.",
     "Interviews with Texan authors, or about books published by Texas presses.",
     "Essays about cultura, including responses to new films, music and writing.",
     "Poetry and short fiction for the Letras y Disparates section of the "
     "Caldwell-Hays Examiner newspaper."],
    ["Reviews outside the three Texas-linked categories the page names.",
     "Fiction over 1,500 words in the newspaper section."],
    ["Read https://infrarrealistas.org/submission before sending.",
     "Submit through the form on the page; its calls are listed as currently open.",
     "Check which section fits: reviews, interviews, essays, or Letras y Disparates.",
     "Send up to three poems for the newspaper section, or fiction within 1,500 words.",
     "Expect Texas subjects and small-press books to be prioritised, especially from "
     "central Texas."],
    "The page states the review asks for no rights: \"Creatives owning their work. We "
    "do not ask for your rights to your work.\"",
    ["Read https://infrarrealistas.org/submission before sending.",
     "Submit through the site's form, which is open.",
     "Pitch or send a review, interview or essay - or a poem or short story for the "
     "newspaper section.",
     "Keep newspaper fiction within 1,500 words and send no more than three poems."],
    ["infrarrealista review", "$100 per review", "$50 per interview",
     "texas writers", "caldwell-hays examiner", "cultural criticism",
     "no rights requested", "book reviews"],
    "not-stated", None))

NEW.append(rec(
    "interrobanglit", "InterrobangLit",
    "Prose: a $3 token payment per accepted story, 3,000-word limit",
    "InterrobangLit: $3 token payment per accepted story, free to submit",
    "InterrobangLit pays a $3 token payment by PayPal for each accepted prose piece, "
    "and its submission windows are free. It takes prose up to 3,000 words, never "
    "reprints, and asks for first electronic, 30-day exclusive electronic and archival "
    "rights. The windows open on the first of every other month and close on the 8th "
    "or when the cap is reached; the September window has closed and the page does not "
    "name the next.",
    "https://interrobanglit.com/submit", "https://interrobanglit.com/submit",
    None, "Online form; windows open on the first of every other month.",
    src("InterrobangLit - Submit (official)", "https://interrobanglit.com/submit"),
    intl(),
    ["fiction", "creative-nonfiction"],
    "Prose, scored against a published rubric",
    pay("USD", 3, 3, "$3 token payment per accepted prose piece",
        "Official page: \"As of February 2026, we offer a token payment of $3 through "
        "PayPal. Unfortunately, we will not be able to use another payment processor.\"",
        "Not publicly stated"),
    {"min": None, "max": 3000,
     "display": "Prose up to 3,000 words - a hard limit, with anything longer "
                "automatically rejected"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "closed",
    {"display": "Windows open on the first of every other month and close on the 8th "
                "or when the submission cap is reached; the window that ran 1-8 "
                "September 2026 has closed and the page does not name the next",
     "openingDate": "2026-09-01", "windowEnd": "2026-09-08", "recurring": True},
    "prohibited",
    ["Prose written to the character prompt posted with each window.",
     "Stories that score 13 or more points on the magazine's published rubric, which "
     "is why the page tells writers to read it before submitting.",
     "Unpublished work, in English."],
    ["AI-written content: \"We do not accept AI written content.\"",
     "Reprints - the magazine considers only unpublished work.",
     "Prose over 3,000 words, which is rejected automatically.",
     "A piece still under consideration elsewhere without immediate withdrawal."],
    ["Read https://interrobanglit.com/submit and the scoring rubric before sending.",
     "Submit during a window: they open on the first of every other month and close "
     "on the 8th or at the cap.",
     "Keep prose within 3,000 words - the limit is hard.",
     "Withdraw immediately if a simultaneous piece is accepted elsewhere.",
     "Give a PayPal address, since that is the only payment route the magazine uses."],
    "If accepted, InterrobangLit asks for First Electronic Publishing Rights, "
    "Exclusive Electronic Rights for 30 days after publication, and Archival Rights "
    "unless removal is requested.",
    ["Read https://interrobanglit.com/submit before sending.",
     "Wait for a window: they open on the first of every other month and close on the "
     "8th or when the cap is reached.",
     "Check the character prompt for the window and the published scoring rubric.",
     "Send prose within 3,000 words, previously unpublished, and not under "
     "consideration elsewhere without withdrawal."],
    ["interrobanglit", "$3 token payment", "3000 word limit", "free to submit",
     "submission window", "scoring rubric", "no ai", "paypal"],
    "accepted",
    "We do not consider reprints, only unpublished work, please. We do accept "
    "simultaneous submissions but ask for immediate withdrawal if your story is "
    "accepted elsewhere. "
    f"— https://interrobanglit.com/submit (read {READ})"))

NEW.append(rec(
    "literary-fantasy-magazine", "The Literary Fantasy Magazine",
    "Arcanist Online: a $10 token payment per story, print pays more",
    "The Literary Fantasy Magazine: $10 token payment for stories on the web",
    "The Literary Fantasy Magazine pays a $10 token payment for fiction accepted for "
    "Arcanist Online, its web publication, and says its print magazines pay more. "
    "Stories run 4,000 to 10,000 words, serials 20,000 to 50,000, and creative "
    "nonfiction 700 to 5,000. General submissions are closed after a 376-submission "
    "window; only a special October window for Short Story September participants is "
    "announced. It asks for first printing and internet archival rights.",
    "https://www.thearcanist.net/submissions",
    "https://www.thearcanist.net/submissions", None,
    "Online submission form; contact support@thearcanist.net only if the form fails.",
    src("The Literary Fantasy Magazine - Submissions (official)",
        "https://www.thearcanist.net/submissions"),
    intl(),
    ["fiction", "creative-nonfiction"],
    "Fantasy short fiction, serial fiction and creative nonfiction",
    pay("USD", 10, 10, "$10 token payment per story published on the web",
        "Official page: \"We offer a token payment of $10 for submissions accepted "
        "for publication on the web. Our print magazines offer higher pay, as do many "
        "other publicatio[ns]...\" Print rates are not stated as figures, so only the "
        "web rate is recorded.",
        "Not publicly stated"),
    {"min": 4000, "max": 10000,
     "display": "Short fiction 4,000-10,000 words (6,000-10,000 preferred); serial "
                "fiction 20,000-50,000 words in one document; creative nonfiction "
                "700-5,000 words"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "closed",
    {"display": "General submissions closed after the June 2026 window drew 376 "
                "submissions; a special window in October 2026 runs for Storytelling "
                "Collective's Short Story September participants only",
     "windowEnd": "2026-10-31", "recurring": False},
    "prohibited",
    ["Fantasy of any flavour, preferably from emerging authors at the start of their "
     "journey.",
     "Short fiction of 4,000-10,000 words, with 6,000-10,000 preferred.",
     "Serial fiction of 20,000-50,000 words, submitted whole in one document.",
     "Creative nonfiction of 700-5,000 words."],
    ["Anything touched by AI: \"Anything touched by AI. Grammarly and ProWritingAid is "
     "allowed, but highly discouraged.\"",
     "Curse words that would not fly on television.",
     "PDF files - the page accepts .docx, .doc or .odt only.",
     "General submissions at present: the window is closed until the backlog is read."],
    ["Read https://www.thearcanist.net/submissions before sending.",
     "Submit through the online form; the general window is closed and only the "
     "October 2026 Storytelling Collective window is announced.",
     "Keep to the word counts: 4,000-10,000 short fiction, 20,000-50,000 serial in "
     "one document, 700-5,000 creative nonfiction.",
     "Send .docx, .doc or .odt files - no PDFs.",
     "Check the site for the Writer Circle and future window announcements."],
    "The magazine asks for first printing rights and internet archival rights; work "
    "may be republished six months after the release date with credit.",
    ["Read https://www.thearcanist.net/submissions before sending.",
     "Wait for a window to open - general submissions are closed and the announced "
     "October 2026 window is limited to Short Story September participants.",
     "Send .docx, .doc or .odt files within the stated word counts.",
     "Note the $10 web rate applies to Arcanist Online; print rates are not published."],
    ["literary fantasy magazine", "$10 token payment", "arcanist online",
     "fantasy short fiction", "serial fiction", "no ai", "storytelling collective",
     "first printing rights"],
    "accepted",
    "Simultaneous submissions are allowed. Please inform us immediately if it is "
    "accepted elsewhere and accept our sincere congratulations. "
    f"— https://www.thearcanist.net/submissions (read {READ})"))


BASE = {
    "frontier-poetry": ("", "International"),
    "half-mystic-journal": ("", "International"),
    "infrarrealista-review": ("US", "United States"),
    "interrobanglit": ("", "International"),
    "literary-fantasy-magazine": ("", "International"),
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
