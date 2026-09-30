#!/usr/bin/env python3
"""Add verified writing-market batch 9 (2026-09-30).

Eight NEW markets, read from the batch-4 backlog. No crawling.

Every figure was read off the publication's own guidelines page on 2026-09-30.
Raw page text is retained under research/batch4/<slug>.txt.

Two more AI policies that are neither prohibited nor silent:

  four-way-review        AI may be used, but if any element was developed using
                         found materials or written in collaboration with others
                         - whether human or through AI - it must be disclosed in
                         your cover letter. disclosure-required.

  metachrosis-literary   Bans AI-generated and stolen art, but states that art
                         using computer simulations based on first-hand data
                         collected by the artist, or where the AI was designed
                         by the artist, is fine - and that it has several such
                         pieces in its catalogue. limited.

A note on a near-miss: STATEMENT Africa, one of the original 147, was briefly
suspected dead because statement-africa.com does not resolve. It does not - but
that is not the record's URL. The record points at statementafrica.com, which
returns HTTP 200. The record was fine and the suspicion was wrong.
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

# ------------------------------------------- 1 Eye to the Telescope
NEW.append(rec(
    "eye-to-the-telescope", "Eye to the Telescope", "Speculative poetry",
    "Eye to the Telescope: 7 cents a word for speculative poetry",
    "Eye to the Telescope, published by the Science Fiction & Fantasy Poetry "
    "Association, pays 7 cents a word rounded up to the nearest dollar, with a "
    "$7 minimum and $30 maximum, within a month of publication. It seeks First "
    "Electronic Rights for original unpublished poems and asks for no "
    "AI-generated works or AI-human collaborations.",
    "https://eyetothetelescope.com/submit.html",
    "https://eyetothetelescope.com/submit.html", None, "Online submission",
    src("Eye to the Telescope — Submit (official)",
        "https://eyetothetelescope.com/submit.html"),
    intl(),
    ["poetry"], "Speculative poetry",
    pay("USD", 7, 30, "7¢ per word rounded up to the nearest dollar; $7 minimum, $30 maximum",
        "Official submit page: accepted poems are paid at 7 cents per word rounded up to the "
        "nearest dollar, with a minimum of US$7 and a maximum of US$30. The per-word rate means "
        "the total depends on length, and the rounding-up convention is the publisher's own.",
        "Within a month of publication"),
    {"min": None, "max": None, "display": "No length limit stated on the submit page"},
    {"label": "Not stated; payment lands within a month of publication", "band": "not-stated",
     "official": True},
    "open", None, "prohibited",
    ["Original unpublished speculative poetry.",
     "Themed issues — recent calls have included faeries of any kind and faerie-like creatures "
     "from any culture, approached with reverence and respect."],
    ["AI-generated works, or AI-human collaborations. Both are excluded.",
     "Previously published poems, for which First Electronic Rights would not apply."],
    ["Check the current themed call before writing.",
     "Send original unpublished work.",
     "Write without AI assistance or collaboration.",
     "Payment arrives within a month of publication."],
    "First Electronic Rights are sought for original unpublished poems.",
    ["Read https://eyetothetelescope.com/submit.html and check the current theme.",
     "The rate scales with length and rounds up — longer poems earn more.",
     "Also see the SFPA's AI policy, which the submit page links to."],
    ["eye to the telescope", "sfpa", "speculative poetry", "7 cents per word", "$7 minimum",
     "$30 maximum", "first electronic rights", "no ai"]))

# ------------------------------------------- 2 Four Way Review
NEW.append(rec(
    "four-way-review", "Four Way Review", "Poetry and short shorts",
    "Four Way Review: honorarium funded by a $3 fee, AI must be disclosed",
    "Four Way Review charges a $3 submission fee for part of the year "
    "specifically so it can offer its writers a small honorarium, though it "
    "publishes no figure. Short shorts run under 1,000 words and poetry "
    "submissions hold three to five poems. Its AI position requires disclosure: "
    "if any element was developed using found materials or written in "
    "collaboration with others, whether human or through artificial "
    "intelligence, that must be stated in the cover letter.",
    "https://fourwayreview.com/submit/",
    "https://fourwayreview.com/submit/", None,
    "Online submission — $3 fee for part of the year",
    src("Four Way Review — Submit (official)", "https://fourwayreview.com/submit/"),
    intl(),
    ["poetry", "fiction"], "Poetry and short shorts",
    pay(None, None, None, "A small honorarium, funded by a $3 fee; no figure published",
        "Official submit page: in order to offer writers a small honorarium, Four Way Review "
        "charges a small submission fee of $3 for part of the year. No honorarium figure is "
        "published, so BRYME records none. The fee exists to fund the payment rather than to "
        "cover costs alone.",
        "Not publicly stated"),
    {"min": None, "max": 1000,
     "display": "Short shorts under 1,000 words; poetry 3–5 poems per submission"},
    {"label": "Not stated; wait to hear back before submitting again", "band": "not-stated",
     "official": True},
    "open", None, "disclosure-required",
    ["Poetry: three to five poems in a single submission, with no more than three poetry "
     "submissions per year.",
     "Short shorts under 1,000 words."],
    ["Using any part of the website, magazine or books to train artificial intelligence "
     "technologies or systems — expressly forbidden.",
     "Undisclosed collaboration. If any element was developed using found materials or written "
     "in collaboration with others, whether human or through AI, it must be disclosed in the "
     "cover letter."],
    ["Pay the $3 fee when it applies — it funds the honorarium.",
     "Send three to five poems per poetry submission, at most three times a year.",
     "Disclose any collaboration, human or AI, in your cover letter.",
     "Email to withdraw individual poems; withdrawal requests are not individually answered."],
    "All rights revert to the author upon publication, with a request that you acknowledge Four "
    "Way Review if the work is published elsewhere.",
    ["Read https://fourwayreview.com/submit/ before sending.",
     "Disclose collaboration in the cover letter — it is required, not optional.",
     "Three poetry submissions a year is the ceiling."],
    ["four way review", "poetry", "short shorts", "honorarium", "$3 fee", "1000 words",
     "ai disclosure required", "rights revert"]))

# ------------------------------------------- 3 Metachrosis Literary
NEW.append(rec(
    "metachrosis-literary", "Metachrosis Literary", "Poetry, prose and visual art",
    "Metachrosis Literary: artist-designed AI is welcome, generated art is not",
    "Metachrosis Literary takes a maximum of three poems under 40 lines each, or "
    "one piece of up to 1,000 words, and reads only during its stated reading "
    "periods. Its art policy is unusually precise: AI-generated and stolen art "
    "are refused, but art using computer simulations based on first-hand data "
    "collected by the artist, or where the AI was designed by the artist, is "
    "accepted — and the magazine has several such pieces in its catalogue.",
    "https://metachrosislitmag.com/submission-guidelines/",
    "https://metachrosislitmag.com/submission-guidelines/", None,
    "Email during reading periods",
    src("Metachrosis Literary — Submission Guidelines (official)",
        "https://metachrosislitmag.com/submission-guidelines/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"], "Poetry, prose and visual art",
    pay(None, None, None, "Not stated on the public guidelines page",
        "The public guidelines set out piece limits, the reading periods and the art policy but "
        "publish no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": 1000,
     "display": "Up to 3 poems under 40 lines each, or 1 piece of up to 1,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open",
    {"date": None,
     "display": "Reading periods are announced by the magazine. Submissions sent outside them "
                "are not read.",
     "recurring": True},
    "limited",
    ["Up to three poems, each under 40 lines.",
     "One piece of prose of up to 1,000 words.",
     "Visual art, including work using computer simulations based on first-hand data the artist "
     "collected, or where the artist designed the AI. The magazine states it has several such "
     "pieces in its catalogue.",
     "Mentions of sex and violence are acceptable; the magazine invites an email if you are "
     "unsure whether a piece is suitable."],
    ["AI-generated art, and stolen art.",
     "Submissions sent outside the reading periods — they are not read."],
    ["Check that a reading period is open before sending.",
     "Send at most three poems under 40 lines each, or one piece under 1,000 words.",
     "If you use an experimental or visual layout, say so in the email and send both a PDF and a "
     "doc or docx copy.",
     "Email first if you are unsure whether a piece is suitable."],
    "Not stated on the public guidelines page.",
    ["Read https://metachrosislitmag.com/submission-guidelines/ and check the reading period.",
     "Artist-designed AI and data-driven simulation work is genuinely welcome here — that is "
     "rare.",
     "Send both PDF and doc for experimental layouts."],
    ["metachrosis literary", "poetry", "prose", "visual art", "40 lines", "1000 words",
     "artist designed ai", "reading periods"]))

# ------------------------------------------- 4 SoFloPoJo
NEW.append(rec(
    "soflopojo", "SoFloPoJo — South Florida Poetry Journal",
    "Poetry, essays, flash fiction and video",
    "SoFloPoJo: no fee, no pay, no paywall; $500 contest",
    "SoFloPoJo describes itself as a no fee, no pay, no paywall, self-funded "
    "publication. Its contest carries a $500 prize. It retains First Serial "
    "Rights plus the right to archive and reprint in a SoFloPoJo anthology, with "
    "all rights reverting to the author after publication, and asks for one "
    "submission per quarterly reading period.",
    "https://www.southfloridapoetryjournal.com/submission-guidelines.html",
    "https://www.southfloridapoetryjournal.com/submission-guidelines.html", None,
    "Submittable — no reading fees",
    src("SoFloPoJo — Submission Guidelines (official)",
        "https://www.southfloridapoetryjournal.com/submission-guidelines.html"),
    intl(),
    ["poetry", "essays", "fiction"], "Poetry, essays, flash fiction and video",
    pay(None, None, None, "Unpaid and fee-free; the contest prize is $500",
        "Official submission guidelines: SoFloPoJo is a no fee, no pay, no paywall, self-funded "
        "publication, and states there are no reading fees. Its contest prize is five hundred "
        "dollars. BRYME records no contributor rate because there is none; the $500 is a contest "
        "award.",
        "Not applicable — unpaid"),
    {"min": None, "max": None, "display": "No word or line limit stated on the guidelines page"},
    {"label": "Wait six months after any decision before submitting again",
     "band": "3-plus-months", "official": True},
    "open",
    {"date": None,
     "display": "Quarterly reading periods: January to March, April to June, July to September, "
                "and October to December. Essays or Flash may close for two weeks at the end of "
                "a period so the editors can clear their backlog.",
     "recurring": True},
    "not-stated",
    ["Poetry, essays, flash fiction and video.",
     "Contest entries, for the $500 prize."],
    ["More than one submission per reading period.",
     "A further submission within six months of a decision, whether accepted or rejected."],
    ["Submit through the Submittable page.",
     "One submission per quarterly reading period.",
     "Wait six months after any decision before sending again.",
     "SoFloPoJo may add your email to its contact list; say so if you would rather it did not."],
    "SoFloPoJo retains First Serial Rights and the right to electronically archive and reprint "
    "your work in a SoFloPoJo anthology. Following publication, all rights revert back to the "
    "author.",
    ["Read https://www.southfloridapoetryjournal.com/submission-guidelines.html before sending.",
     "Unpaid and fee-free — the $500 contest is the only money.",
     "Respect the six-month gap; it is enforced."],
    ["soflopojo", "south florida poetry journal", "poetry", "essays", "flash fiction", "video",
     "unpaid", "no fee", "$500 contest", "submittable"]))

# ------------------------------------------- 5 Poetry Super Highway
NEW.append(rec(
    "poetry-super-highway", "Poetry Super Highway", "Poetry",
    "Poetry Super Highway: poems stay yours, no email submissions",
    "Poetry Super Highway states that all poems are copyright and owned by the "
    "author. It has not accepted submissions by email since January 2019, and if "
    "you have not heard within six months of your submission date it means "
    "nothing from that submission could be used.",
    "https://www.poetrysuperhighway.com/psh/poetry/submission-guidelines/",
    "https://www.poetrysuperhighway.com/psh/poetry/submission-guidelines/", None,
    "Online submission — not by email",
    src("Poetry Super Highway — Submission Guidelines (official)",
        "https://www.poetrysuperhighway.com/psh/poetry/submission-guidelines/"),
    intl(),
    ["poetry"], "Poetry",
    pay(None, None, None, "Not stated on the public guidelines page",
        "The public guidelines set out the rights position, the submission route and the "
        "response convention but publish no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "No limit stated on the public guidelines page"},
    {"label": "Six months of silence means nothing could be used", "band": "3-plus-months",
     "official": True},
    "open", None, "not-stated",
    ["Poetry."],
    ["Email submissions. The magazine has not accepted them since January 2019."],
    ["Submit through the online route on the guidelines page, not by email.",
     "If six months pass with no reply, treat the submission as closed.",
     "Your copyright is unaffected either way."],
    "All poems are copyright and owned by the author.",
    ["Read https://www.poetrysuperhighway.com/psh/poetry/submission-guidelines/ before sending.",
     "Do not email — that route closed in 2019.",
     "Rights stay with you throughout."],
    ["poetry super highway", "poetry", "copyright retained", "no email submissions",
     "6 month response"]))

# ------------------------------------------- 6 Poetry Pacific
NEW.append(rec(
    "poetry-pacific", "Poetry Pacific", "Poetry",
    "Poetry Pacific: unpaid by design, 3-month response",
    "Poetry Pacific says openly that it is not a paying market but a literary "
    "project presented as a labour of love for lovers of words and wisdom. Its "
    "response time is three months, usually shorter, and only accepted "
    "submitters receive a reply. By submitting, you warrant that you alone "
    "created the work and own all rights to it.",
    "https://poetrypacific.blogspot.com/2026/05/pp-call-for-subs-guidelines.html",
    "https://poetrypacific.blogspot.com/2026/05/pp-call-for-subs-guidelines.html", None,
    "Email — editorial submissions only",
    src("Poetry Pacific — Call for Submissions and Guidelines (official)",
        "https://poetrypacific.blogspot.com/2026/05/pp-call-for-subs-guidelines.html"),
    intl(),
    ["poetry"], "Poetry",
    pay(None, None, None, "Unpaid — the magazine states it is not a paying market",
        "Official guidelines: Poetry Pacific states it is not a paying market but a literary "
        "project as a labour of love, presented to true lovers of words and wisdom. BRYME "
        "records no figure because there is none.",
        "Not applicable — unpaid"),
    {"min": None, "max": None, "display": "No limit stated on the public guidelines page"},
    {"label": "Three months, usually shorter; only accepted submitters get a reply",
     "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Poetry."],
    ["Personal solicitations, or requests to move the conversation to third-party messaging apps.",
     "Work you did not create alone or do not own the rights to — the submission warranty covers "
     "both."],
    ["Send your submission to the editorial email given in the guidelines. That address is for "
     "editorial submissions only.",
     "Warrant that you alone created the work and own all rights to it.",
     "Expect three months at most, and a reply only if you are accepted."],
    "By submitting, the submitter warrants that they alone created the work and own all rights "
    "to it. No specific rights transfer is stated on the guidelines page.",
    ["Read the guidelines at "
     "https://poetrypacific.blogspot.com/2026/05/pp-call-for-subs-guidelines.html first.",
     "Unpaid by design — submit for the readership.",
     "Silence means declined; only acceptances get a reply."],
    ["poetry pacific", "poetry", "unpaid", "labor of love", "3 month response",
     "no reply if declined"]))

# ------------------------------------------- 7 Brilliant Flash Fiction
NEW.append(rec(
    "brilliant-flash-fiction", "Brilliant Flash Fiction", "Flash fiction",
    "Brilliant Flash Fiction: unpaid, rights stay yours, no AI",
    "Brilliant Flash Fiction is run by an editorial board and board of directors "
    "who receive no payment for their services, and it does not pay "
    "contributors. It asks for no AI-generated material, and authors whose "
    "submissions are accepted retain all rights to their work after "
    "publication.",
    "https://brilliantflashfiction.com/submissions/",
    "https://brilliantflashfiction.com/submissions/",
    "brilliantflashfiction@gmail.com",
    "Email — paste in the body and attach",
    src("Brilliant Flash Fiction — Submissions (official)",
        "https://brilliantflashfiction.com/submissions/"),
    intl(),
    ["fiction"], "Flash fiction",
    pay(None, None, None, "Unpaid — the editorial board itself is unpaid",
        "Official submissions page: Brilliant Flash Fiction states that no one on its editorial "
        "board or board of directors receives payment for their services, and no contributor "
        "rate is published. BRYME records no figure because there is none.",
        "Not applicable — unpaid"),
    {"min": None, "max": None,
     "display": "Flash fiction; no word limit stated on the public submissions page"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Flash fiction."],
    ["AI-generated material."],
    ["Email your story to brilliantflashfiction@gmail.com.",
     "Paste the story into the body of the email and also attach it — both are required.",
     "Write without AI assistance."],
    "Authors whose submissions are accepted retain all rights to their work after publication.",
    ["Read https://brilliantflashfiction.com/submissions/ before sending.",
     "Both paste and attach — the page asks for both.",
     "Unpaid, but you keep every right."],
    ["brilliant flash fiction", "flash fiction", "unpaid", "rights retained", "email submission",
     "no ai"]))

# ------------------------------------------- 8 The Journal
NEW.append(rec(
    "the-journal", "The Journal", "Fiction, nonfiction, poetry, reviews and artwork",
    "The Journal: unpaid, no AI, work under 8,000 words",
    "The Journal, based in the Department of English at The Ohio State "
    "University, states it is unable to offer monetary payment to its "
    "contributors at this time. It does not accept work generated by AI, "
    "generally does not publish work over 8,000 words, and keeps reviews to "
    "1,200 words. It does not publish academic writing or straight reportage.",
    "https://thejournalmag.org/submit",
    "https://thejournalmag.org/submit", None, "Submittable",
    src("The Journal — Submit (official)", "https://thejournalmag.org/submit"),
    {"summary": "Open internationally. No country restriction is stated on the submit page. The "
                "Journal is published from the Department of English at The Ohio State "
                "University, Columbus, Ohio, United States.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction", "creative-nonfiction", "poetry", "reviews"],
    "Fiction, nonfiction, poetry, reviews and artwork",
    pay(None, None, None, "Unpaid — the journal states it cannot offer monetary payment",
        "Official submit page: at this time The Journal is unable to offer monetary payment to "
        "its contributors. BRYME records no figure because there is none.",
        "Not applicable — unpaid"),
    {"min": None, "max": 8000,
     "display": "Generally not over 8,000 words; reviews no more than 1,200 words"},
    {"label": "Not stated; the journal asks for patience", "band": "not-stated",
     "official": True},
    "open",
    {"date": None,
     "display": "The Journal accepts general submissions during its current reading period.",
     "recurring": True},
    "prohibited",
    ["Fiction and nonfiction, generally under 8,000 words.",
     "Self-contained excerpts of novels and long stories, though the journal notes that "
     "historically it is unusual for it to publish submissions longer than 8,000 words.",
     "Reviews of no more than 1,200 words.",
     "Poetry and artwork."],
    ["Work generated by AI. Submissions including AI-generated work are rejected.",
     "Academic writing or straight reportage — neither is published.",
     "Multiple submissions. They are not accepted and will not be read or responded to."],
    ["Submit your writing and artwork on Submittable.",
     "Keep prose under 8,000 words and reviews to 1,200.",
     "Send one submission at a time and wait for the response.",
     "Address correspondence to The Journal, Department of English, The Ohio State University, "
     "Columbus, Ohio."],
    "Not stated on the official submit page.",
    ["Read https://thejournalmag.org/submit before sending.",
     "No academic writing or reportage — literary work only.",
     "One submission at a time; multiples are not read."],
    ["the journal", "ohio state university", "fiction", "nonfiction", "poetry", "reviews",
     "unpaid", "8000 words", "no ai", "submittable"]))


BASE = {
    "eye-to-the-telescope": ("", "International"),
    "four-way-review": ("", "International"),
    "metachrosis-literary": ("", "International"),
    "soflopojo": ("", "International"),
    "poetry-super-highway": ("", "International"),
    "poetry-pacific": ("", "International"),
    "brilliant-flash-fiction": ("", "International"),
    "the-journal": ("US", "United States"),
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
#   thenulla.com        A prize. Its $500 goes to contest winners with
#       publication in the Fall 2026 issue, behind a fee and an online form.
#       Same call as Dogwood in batch 8 and American Short Fiction in batch 2.
#
# The extractor now matches on the name before any subtitle, which is what let
# Gulf Coast slip through in batch 8. Re-run against the 450-page backlog it
# correctly identifies 51 pages that match a record already in the database.
#
# 387 usable guidelines pages remain unread. No further crawling required.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
