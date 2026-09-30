#!/usr/bin/env python3
"""Add verified writing-market batch 10 (2026-09-30).

Eight NEW markets, read from the batch-4 backlog. No crawling.

Every figure was read off the publication's own guidelines page on 2026-09-30.
Raw page text is retained under research/batch4/<slug>.txt.

Two enum values that this expansion has rarely needed:

  hanging-loose     eligibility.mode = restricted. Hanging Loose asks submitters
                    to identify themselves as high school age writers and give
                    their school and age. That is a gate, and it is recorded as
                    one rather than buried in the requirements.

  conjunctions      aiPolicy = limited. Generative AI may not be used to write,
                    draft or outline - but with a rare exception for pieces that
                    engage with the tool in an intentional, artistic and
                    transparent manner. That exception is the policy, so it is
                    recorded rather than flattened to "prohibited".
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

# ------------------------------------------- 1 Yellow Arrow Journal
NEW.append(rec(
    "yellow-arrow-journal", "Yellow Arrow Journal",
    "Poetry, prose and visual art",
    "Yellow Arrow Journal: $10 and a PDF, no AI outlining either",
    "Yellow Arrow Journal pays $10 USD and a PDF of the issue to selected "
    "contributors, by PayPal. Poetry runs to two poems per author per issue and "
    "may be any length. It bans AI outright and is specific about scope: do not "
    "use AI tools to write, outline or rewrite your text. Artists must own all "
    "rights to the work they submit.",
    "https://www.yellowarrowpublishing.com/submissions",
    "https://www.yellowarrowpublishing.com/submissions",
    "submissions@yellowarrowpublishing.com",
    "Email while submissions are open",
    src("Yellow Arrow Journal — Submissions (official)",
        "https://www.yellowarrowpublishing.com/submissions"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"], "Poetry, prose and visual art",
    pay("USD", 10, 10, "$10 USD plus a PDF of the journal issue",
        "Official submissions page: if selected you receive $10.00 USD and a PDF of the journal "
        "issue. Payments are through PayPal; the publisher tries to accommodate those without a "
        "PayPal account but says this is not always possible, especially for people outside the "
        "United States.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Poetry: up to 2 poems per author per issue, grouped in a single document, any "
                "length"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Poetry: up to two poems per author per issue, grouped into a single document, of any "
     "length.",
     "Prose and visual art."],
    ["Work created by artificial intelligence tools.",
     "Using AI tools to write, outline or rewrite your text. The ban covers outlining and "
     "rewriting, not just drafting.",
     "Work you do not own all rights to. If it was published or shown previously you must be "
     "able to list where and when."],
    ["Email submissions@yellowarrowpublishing.com while submissions are open for an issue.",
     "Group up to two poems into a single document.",
     "Have a PayPal account if you can — accommodation without one is not always possible, "
     "particularly outside the US.",
     "Be ready to say where and when previously shown work appeared."],
    "Artists must own all rights to the work submitted. No further rights transfer is stated on "
    "the submissions page.",
    ["Read https://www.yellowarrowpublishing.com/submissions and check an issue is open.",
     "The AI ban extends to outlining — plan your work without it.",
     "Flag early if you cannot use PayPal."],
    ["yellow arrow journal", "poetry", "prose", "visual art", "$10", "paypal", "2 poems",
     "no ai outlining"]))

# ------------------------------------------- 2 Modern Haiku
NEW.append(rec(
    "modern-haiku", "Modern Haiku", "Haiku, senryu and prose about haiku",
    "Modern Haiku: $5 per printed page for prose, paid on acceptance",
    "Modern Haiku pays a standard rate of $5 per printed page for prose, paid "
    "upon acceptance. It does not consider AI-generated work, asks for no more "
    "than one submission per reading period, and responds by email.",
    "https://modernhaiku.org/submissions.html",
    "https://modernhaiku.org/submissions.html", None, "See guidelines",
    src("Modern Haiku — Submissions (official)", "https://modernhaiku.org/submissions.html"),
    intl(),
    ["poetry", "essays", "reviews"], "Haiku, senryu and prose about haiku",
    pay("USD", 5, 5, "$5 per printed page for prose",
        "Official submissions page: the standard rate of payment for prose is $5 per printed "
        "page, paid upon acceptance. The rate is per printed page, so the total depends on how "
        "the prose is set.",
        "Upon acceptance"),
    {"min": None, "max": None, "display": "No prose length limit stated on the submissions page"},
    {"label": "By email; editors cannot correspond in depth about unaccepted work",
     "band": "not-stated", "official": True},
    "open", None, "prohibited",
    ["Haiku and senryu.",
     "Prose about haiku, paid at $5 per printed page."],
    ["AI-generated work. It will not be considered.",
     "More than one submission per reading period."],
    ["Send no more than one submission per reading period.",
     "Expect a response by email.",
     "Do not expect extended correspondence about work that is not accepted — the editors say "
     "time constraints prevent it."],
    "Submissions carry the author's copyright notice. No further rights transfer is stated on "
    "the submissions page.",
    ["Read https://modernhaiku.org/submissions.html before sending.",
     "One submission per reading period — respect it.",
     "Prose is paid per printed page, so length does affect the total."],
    ["modern haiku", "haiku", "senryu", "prose", "$5 per printed page", "paid on acceptance",
     "one submission per period", "no ai"]))

# ------------------------------------------- 3 Fantastic Other
NEW.append(rec(
    "fantastic-other", "Fantastic Other",
    "Fiction, flash fiction, poetry and art",
    "Fantastic Other: $5 token payment, rights revert on publication",
    "Fantastic Other offers a token payment of $5 USD for each accepted piece, "
    "paid through PayPal, and says it hopes to improve that in future. "
    "Submissions must be original, not AI-generated, and unpublished. On "
    "publication, rights revert back to the author.",
    "https://fantasticother.com/submissions/",
    "https://fantasticother.com/submissions/", None,
    "Email — genre in the subject line",
    src("Fantastic Other — Submissions (official)",
        "https://fantasticother.com/submissions/"),
    intl(),
    ["fiction", "poetry"], "Fiction, flash fiction, poetry and art",
    pay("USD", 5, 5, "$5 USD token payment per accepted piece, via PayPal",
        "Official submissions page: Fantastic Other is currently only able to offer a token "
        "payment of $5 USD for each accepted piece, paid through PayPal, and states it hopes to "
        "improve this payment in the future. BRYME records it as the token it is described as.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "No word limit stated on the submissions page"},
    {"label": "Not stated; feedback and quick-response routes exist", "band": "not-stated",
     "official": True},
    "open", None, "prohibited",
    ["Fiction, flash fiction, poetry and art.",
     "Both new and previously unpublished work from writers at any stage."],
    ["AI-generated work.",
     "Previously published work."],
    ["Email your submission with Fiction, Flash Fiction, Poetry or Art in the email title.",
     "If you are submitting in multiple genres, send separate emails for each.",
     "Write without AI assistance and send unpublished work only.",
     "Feedback Response and Quick Response submission routes are available if you want them."],
    "On publication, rights revert back to the author.",
    ["Read https://fantasticother.com/submissions/ before sending.",
     "Put the genre in the subject line — it is how submissions are routed.",
     "One genre per email."],
    ["fantastic other", "fiction", "flash fiction", "poetry", "art", "$5 token", "paypal",
     "rights revert", "no ai"]))

# ------------------------------------------- 4 Conjunctions
NEW.append(rec(
    "conjunctions", "Conjunctions", "Experimental fiction, nonfiction and poetry",
    "Conjunctions: AI banned, except where the work is about it",
    "Conjunctions accepts submissions electronically via Submittable twice a "
    "year, during its fall and winter reading periods. Generative AI tools may "
    "not be used to write, draft or outline submitted content — with a rare "
    "exception for pieces that engage with the tool in an intentional, artistic "
    "and transparent manner. Basic spell-checking and grammar tools are "
    "acceptable.",
    "https://conjunctions.com/about/submit/",
    "https://conjunctions.com/about/submit/", "info@conjunctions.com",
    "Submittable, twice a year — email only for accessibility",
    src("Conjunctions — Submit (official)", "https://conjunctions.com/about/submit/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Experimental fiction, nonfiction and poetry",
    pay(None, None, None, "Not stated on the public submit page",
        "The public submit page sets out the reading periods, the submission route and the AI "
        "policy but publishes no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "No length limit stated on the public submit page"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open",
    {"date": None,
     "display": "Submissions are accepted twice a year, during the fall and winter reading "
                "periods. Check the site, the newsletter or Conjunctions' Instagram, Facebook "
                "and Bluesky for the earliest news of each period.",
     "recurring": True},
    "limited",
    ["Experimental fiction, nonfiction and poetry.",
     "Pieces that engage with AI in an intentional, artistic and transparent manner — the one "
     "stated exception to the generative AI ban."],
    ["Using generative AI tools to write, draft or outline submitted content. Any submission "
     "found to be partially or wholly generated by AI is rejected.",
     "Submissions outside the fall and winter reading periods."],
    ["Submit electronically via Submittable during a fall or winter reading period.",
     "Basic spell-checking and grammar tools are acceptable; generative AI is not.",
     "If a disability prevents you from using Submittable, email info@conjunctions.com — that "
     "route exists specifically for accessibility.",
     "Check the site or newsletter for when each reading period opens."],
    "Not stated on the public submit page.",
    ["Read https://conjunctions.com/about/submit/ and wait for an open reading period.",
     "If your work is genuinely about AI, the exception may apply — but it has to be intentional, "
     "artistic and transparent.",
     "The email route is for accessibility, not convenience."],
    ["conjunctions", "bard college", "experimental", "fiction", "nonfiction", "poetry",
     "fall and winter reading periods", "ai exception", "submittable"]))

# ------------------------------------------- 5 WordSwell Journal
NEW.append(rec(
    "wordswell-journal", "WordSwell Journal", "Poetry and prose",
    "WordSwell Journal: prose 500–2,500 words, copyright stays yours",
    "WordSwell Journal takes up to three poems totalling nine pages or less, or "
    "one piece of prose between 500 and 2,500 words with the word count noted at "
    "the top of the document. Accepted writers retain copyright, reprints are "
    "welcome if you hold the rights, and the current response time is about six "
    "months to a year.",
    "https://www.wordswelljournal.org/submissions.html",
    "https://www.wordswelljournal.org/submissions.html", None,
    "Email — “Submission” plus genre and name in the subject line",
    src("WordSwell Journal — Submissions (official)",
        "https://www.wordswelljournal.org/submissions.html"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"], "Poetry and prose",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out piece limits, the copyright position and the "
        "response time but publishes no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": 500, "max": 2500,
     "display": "Prose 500–2,500 words, double spaced; poetry up to 3 poems totalling 9 pages "
                "or less in 12-point font"},
    {"label": "About six months to a year", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Prose of 500 to 2,500 words, double spaced, with the word count noted at the top of the "
     "document.",
     "Up to three poems totalling nine pages or less, in 12-point font.",
     "Reprints, provided you hold the copyright.",
     "Writers at any stage — the journal says explicitly that whether you are new or "
     "previously published, it wants to hear from you."],
    ["Prose outside the 500 to 2,500 word band.",
     "Reprints where you no longer hold the copyright."],
    ["Email your submission with \"Submission\" in the subject line plus your genre and name — "
     "for example \"Submission – Poetry – Jane Doe\".",
     "Double-space prose and put the word count at the top.",
     "Set poetry in 12-point font, three poems and nine pages at most.",
     "Simultaneous submissions are accepted, but notify the journal immediately if a piece is "
     "accepted elsewhere.",
     "After six months you may send an inquiry with \"Inquiry\" in the subject line."],
    "If your work is accepted, you retain the copyright.",
    ["Read https://www.wordswelljournal.org/submissions.html before sending.",
     "The subject line format is specific — follow it.",
     "Budget for six months to a year before inquiring."],
    ["wordswell journal", "poetry", "prose", "500-2500 words", "copyright retained",
     "reprints welcome", "6 month response"]))

# ------------------------------------------- 6 The Fictional Café
NEW.append(rec(
    "the-fictional-cafe", "The Fictional Café", "Poetry and prose",
    "The Fictional Café: unpaid non-profit, 4–8 poems minimum",
    "The Fictional Café describes itself as a non-profit labour of love and "
    "states it is unable to provide an honorarium for accepted submissions. "
    "Poets are asked to send a single document of four to eight poems or a "
    "minimum of 200 words; single poems or collections under 200 words are not "
    "considered.",
    "https://fictionalcafe.com/submit/",
    "https://fictionalcafe.com/submit/", "submissions@fictionalcafe.com",
    "Email — work as an attachment",
    src("The Fictional Café — Submit (official)", "https://fictionalcafe.com/submit/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"], "Poetry and prose",
    pay(None, None, None, "Unpaid — a non-profit labour of love with no honorarium",
        "Official submit page: The Fictional Café states it is a non-profit labour of love and is "
        "unable to provide an honorarium for accepted submissions. BRYME records no figure "
        "because there is none.",
        "Not applicable — unpaid"),
    {"min": 200, "max": None,
     "display": "Poetry: a single document of 4–8 poems, or a minimum of 200 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Poetry: a single document of four to eight poems, or a minimum of 200 words.",
     "Prose."],
    ["Single poems, or collections under 200 words — neither is considered.",
     "An expectation of payment. The café is explicit that there is none."],
    ["Send your work as an attachment to your email, in Word or a similar word processing "
     "format.",
     "Email submissions@fictionalcafe.com.",
     "Send four to eight poems in a single document, or at least 200 words."],
    "Not stated on the official submit page.",
    ["Read https://fictionalcafe.com/submit/ before sending.",
     "Do not send one short poem — the 200-word floor is enforced.",
     "Unpaid; submit for the publication."],
    ["the fictional cafe", "poetry", "prose", "unpaid", "non-profit", "4-8 poems",
     "200 words minimum"]))

# ------------------------------------------- 7 Five on the Fifth
NEW.append(rec(
    "five-on-the-fifth", "Five on the Fifth", "Fiction, nonfiction, poetry and art",
    "Five on the Fifth: FNAR, permanent archive, Submittable only",
    "Five on the Fifth asks for First North American Rights to publish. "
    "Following publication all rights revert to the author, but the magazine "
    "requires permission to archive your work permanently in its Previous Issues "
    "section. It accepts submissions exclusively through Submittable, where an "
    "optional $3 tip jar supports the magazine.",
    "https://www.fiveonthefifth.com/submit",
    "https://www.fiveonthefifth.com/submit", None, "Submittable only",
    src("Five on the Fifth — Submit (official)", "https://www.fiveonthefifth.com/submit"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"], "Fiction, nonfiction, poetry and art",
    pay(None, None, None, "Not stated; an optional $3 tip jar supports the magazine",
        "The public submit page describes an optional Fiction/Nonfiction Tip Jar on its "
        "Submittable page, where a $3 contribution leaves the magazine $1.86 after fees. That is "
        "a donation from writers, not payment to them, and BRYME does not record it as either. "
        "No contributor rate is published.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "No length limit stated on the public submit page"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Fiction, nonfiction, poetry and art.",
     "Writers reachable by email or a social media account."],
    ["Submissions sent anywhere other than Submittable."],
    ["Submit exclusively through Submittable.",
     "Make sure the magazine can reach you by email or a social media account.",
     "The $3 tip jar is optional support, not a fee — nothing is required."],
    "Five on the Fifth asks for First North American Rights to publish. Following publication "
    "all rights revert back to the author, but the magazine requires permission to permanently "
    "archive your work online in its Previous Issues section.",
    ["Read https://www.fiveonthefifth.com/submit before sending.",
     "Submittable is the only route.",
     "Note the permanent archive condition — rights revert, but the archive does not come down."],
    ["five on the fifth", "fiction", "nonfiction", "poetry", "fnar", "permanent archive",
     "submittable", "tip jar"]))

# ------------------------------------------- 8 Hanging Loose
NEW.append(rec(
    "hanging-loose", "Hanging Loose", "Poetry, flash fiction and short fiction",
    "Hanging Loose: for high school writers, up to six poems",
    "Hanging Loose asks high school age writers to send up to six poems, or "
    "flash fiction, or short fiction of up to 1,000 words, as an email "
    "attachment, with a note in the body of the email identifying yourself as a "
    "high school age writer and giving your school and age. That is a genuine "
    "eligibility gate, so it is recorded as one.",
    "https://www.hangingloosepress.com/submissions/",
    "https://www.hangingloosepress.com/submissions/", "HighSchool@hangingloosepress.com",
    "Email attachment — high school writers only",
    src("Hanging Loose — Submissions (official)",
        "https://www.hangingloosepress.com/submissions/"),
    {"summary": "Restricted to high school age writers. Hanging Loose asks submitters to include "
                "a note in the body of the email identifying themselves as a high school age "
                "writer and giving the name of their school and their age. Writers outside that "
                "group are not the intended submitters for this route.",
     "mode": "restricted", "includesGroups": ["high school age writers"],
     "includesRegions": [], "allowsDiaspora": True, "notStated": False},
    ["poetry", "fiction"], "Poetry, flash fiction and short fiction",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out the piece limits and the identification "
        "requirement but publishes no payment rate. The prices on the page are for ordering "
        "sample copies — $21.00 including postage in print, $18 digital — and are not "
        "contributor payment.",
        "Not publicly stated"),
    {"min": None, "max": 1000,
     "display": "Up to six poems, or flash fiction, or short fiction up to 1,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Up to six poems.",
     "Flash fiction.",
     "Short fiction of up to 1,000 words."],
    ["Submissions from writers who are not high school age, for this route.",
     "Submissions without the identifying note."],
    ["Send all work as an email attachment to HighSchool@hangingloosepress.com.",
     "Include a note in the body of the email identifying yourself as a high school age writer, "
     "and giving the name of your school and your age.",
     "Keep short fiction to 1,000 words and send at most six poems."],
    "Not stated on the public submissions page.",
    ["Read https://www.hangingloosepress.com/submissions/ before sending.",
     "This route is specifically for high school age writers — the note in the email is "
     "required.",
     "The prices on the site are for sample copies, not payment to contributors."],
    ["hanging loose", "hanging loose press", "high school writers", "poetry", "flash fiction",
     "short fiction", "1000 words", "restricted eligibility"]))


BASE = {
    "yellow-arrow-journal": ("", "International"),
    "modern-haiku": ("", "International"),
    "fantastic-other": ("", "International"),
    "conjunctions": ("", "International"),
    "wordswell-journal": ("", "International"),
    "the-fictional-cafe": ("", "International"),
    "five-on-the-fifth": ("", "International"),
    "hanging-loose": ("", "International"),
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
# 379 usable guidelines pages remain unread. No further crawling required.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
