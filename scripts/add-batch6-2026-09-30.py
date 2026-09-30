#!/usr/bin/env python3
"""Add verified writing-market batch 6 (2026-09-30).

Ten NEW markets, read from the batch-4 backlog. No crawling: the 450 usable
guidelines pages from the Poets & Writers scrape are already on disk and ranked
in batch4_ranked.json. Batch 4 took the top twelve, batch 5 the tier below, this
takes the next.

Every figure was read off the publication's own guidelines page on 2026-09-30.
Raw page text is retained under research/batch4/<slug>.txt.

Three publish a figure of some kind - one guaranteed, two by award or
contingency. Seven publish no rate at all and are recorded as such.
None has been given a figure its publication did not publish.

Raising Mothers is the first record in this expansion to use
eligibility.mode = "restricted": it exclusively seeks work from self-identified
mothers and parents. That is a genuine gate, not a preference, so it is recorded
as one.
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

# ------------------------------------------- 1 Red River Review
NEW.append(rec(
    "red-river-review", "Red River Review", "Fiction and flash",
    "Red River Review: unpaid, $10 fee, stories to 3,000 words",
    "Red River Review states plainly that it does not currently offer "
    "contributor payment, and charges a $10 non-refundable submission fee that "
    "does not guarantee publication. It takes one story of up to 3,000 words or "
    "up to three flash pieces of 1,000 words each. It does not accept work "
    "created or meaningfully assisted by generative AI, and all rights revert to "
    "the author upon publication.",
    "https://redriverreview.org/submissions/",
    "https://redriverreview.org/submissions/", None, "DuoSuma — $10 non-refundable fee",
    src("Red River Review — Submissions (official)",
        "https://redriverreview.org/submissions/"),
    intl(),
    ["fiction"], "Fiction and flash",
    pay(None, None, None, "Unpaid — the magazine states it does not currently offer payment",
        "Official submissions page: Red River Review requires submitters to acknowledge that it "
        "does not currently offer contributor payment, and that the $10 submission fee is "
        "non-refundable and does not guarantee publication. BRYME records no figure because "
        "there is none. Note that this is an unpaid market that also charges to enter.",
        "Not applicable — unpaid"),
    {"min": None, "max": 3000,
     "display": "One story up to 3,000 words, or up to three flash pieces of 1,000 words each"},
    {"label": "All submitters notified before the connected issue is released",
     "band": "not-stated", "official": True},
    "open",
    {"date": None,
     "display": "Current submission dates are posted on the submissions page and through "
                "DuoSuma. Only one submission per genre is allowed during a reading period.",
     "recurring": True},
    "prohibited",
    ["One story of up to 3,000 words.",
     "Up to three flash pieces of 1,000 words each, in a single file."],
    ["Work created or meaningfully assisted by generative AI. The acknowledgment checkbox asks "
     "you to confirm your submission includes neither.",
     "More than one submission per genre in a reading period."],
    ["Check the current submission dates on the site or through DuoSuma.",
     "Pay the $10 non-refundable fee, understanding it does not guarantee publication.",
     "Submit once per genre per reading period.",
     "Every submitter is notified before the issue is released, so you will get an answer."],
    "All rights revert to the author upon publication. Accepted work may also be included in "
    "future Red River Review anthologies or special collections on a non-exclusive basis, with "
    "full author attribution.",
    ["Read https://redriverreview.org/submissions/ before paying anything.",
     "This is unpaid with a $10 entry fee — decide whether the credit is worth that.",
     "Rights revert on publication, so you can reprint immediately."],
    ["red river review", "fiction", "flash", "unpaid", "$10 fee", "3000 words", "duosuma",
     "rights revert", "no ai"]))

# ------------------------------------------- 2 Redivider
NEW.append(rec(
    "redivider", "Redivider", "Fiction, nonfiction, poetry and flash",
    "Redivider: 1,200–6,000 words, no AI even in part",
    "Redivider, published at Emerson College, takes prose of 1,200 to 6,000 "
    "words and routes anything shorter to its Flash Fiction category. It does "
    "not accept work that has been even partially created with AI. It requests "
    "first serial rights, all rights revert to the author upon publication, and "
    "authors retain copyright.",
    "https://redivider.emerson.edu/submissions/",
    "https://redivider.emerson.edu/submissions/", None, "Submittable only",
    src("Redivider — Submissions (official)",
        "https://redivider.emerson.edu/submissions/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Fiction, nonfiction, poetry and flash",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out word counts, the AI position and the rights "
        "position but publishes no payment rate, so BRYME records no figure. Confirm current "
        "terms before you submit.",
        "Not publicly stated"),
    {"min": 1200, "max": 6000,
     "display": "1,200–6,000 words; under 1,200 words goes to Flash Fiction"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Prose of 1,200 to 6,000 words.",
     "Flash fiction — anything shorter than 1,200 words, submitted under that category."],
    ["Work that has been even partially created with the use of AI. Redivider's wording is "
     "explicit that partial use counts.",
     "Prose under 1,200 words sent to the general category rather than Flash Fiction."],
    ["Submit through the Submittable page only.",
     "Keep prose between 1,200 and 6,000 words, or use Flash Fiction if it is shorter.",
     "Write without AI assistance of any degree."],
    "Redivider requests first serial rights and all rights revert to the author upon "
    "publication. Authors retain copyright to their work published in Redivider.",
    ["Read https://redivider.emerson.edu/submissions/ before sending.",
     "Submittable is the only route.",
     "Check the word count against the right category before you send."],
    ["redivider", "emerson college", "fiction", "nonfiction", "poetry", "flash",
     "1200-6000 words", "no ai", "submittable"]))

# ------------------------------------------- 3 West Trade Review
NEW.append(rec(
    "west-trade-review", "West Trade Review", "Prose and flash fiction",
    "West Trade Review: prose to 5,000 words, two reading periods",
    "West Trade Review takes one prose piece of up to 5,000 words for a $3 "
    "general submission fee, with paid expedited options at $10 for a quick "
    "decision and $25 for a quick decision with personalised editorial feedback. "
    "It runs two regular reading periods, 1 April to 1 August and 15 August to "
    "15 December, and does not publish anything written by or with the "
    "assistance of generative AI.",
    "https://www.westtradereview.com/submissionguidelines20.html",
    "https://www.westtradereview.com/submissionguidelines20.html", None,
    "Online submission — $3 fee, $10 or $25 expedited options",
    src("West Trade Review — Submission Guidelines (official)",
        "https://www.westtradereview.com/submissionguidelines20.html"),
    intl(),
    ["fiction", "creative-nonfiction"], "Prose and flash fiction",
    pay(None, None, None, "Not stated on the guidelines page; $3 fee with paid expedited options",
        "The guidelines page sets a $3 general submission fee to cover administrative costs of "
        "the online submissions system, plus $10 for an expedited decision and $25 for an "
        "expedited decision with personalised feedback from the editors. No payment rate for "
        "published work is stated, so BRYME records none. The review also runs the Phyllis "
        "Grant Zellmer Prize for Fiction and the 704 Prize for Flash Fiction.",
        "Not publicly stated"),
    {"min": None, "max": 5000, "display": "One prose piece of up to 5,000 words"},
    {"label": "Expedited options available; standard time not stated",
     "band": "not-stated", "official": True},
    "open",
    {"date": None,
     "display": "Two regular reading periods: 1 April to 1 August, and 15 August to 15 December. "
                "As of 30 September 2026 the second period is open.",
     "recurring": True},
    "prohibited",
    ["One prose piece of up to 5,000 words.",
     "Flash fiction, which has its own 704 Prize."],
    ["Any content written by or with the assistance of generative AI. The review states plainly "
     "that it does not publish it.",
     "Submissions outside the two reading periods."],
    ["Check that a reading period is open — 1 April to 1 August, or 15 August to 15 December.",
     "Pay the $3 general fee.",
     "Take the $10 expedited option for a quick decision, or $25 to add personalised editorial "
     "feedback.",
     "Keep prose to 5,000 words."],
    "Not stated on the official guidelines page.",
    ["Read https://www.westtradereview.com/submissionguidelines20.html and check the dates.",
     "The $25 tier buys real editorial feedback, which is unusual at this price.",
     "Work published in online editions is promoted across the review's social channels."],
    ["west trade review", "prose", "flash fiction", "5000 words", "$3 fee", "expedited",
     "reading periods", "no generative ai"]))

# ------------------------------------------- 4 Blue Bell Review
NEW.append(rec(
    "blue-bell-review", "The Blue Bell Review", "Prose, poetry and essays",
    "Blue Bell Review: 2 pieces under 2,500 words, Google Form",
    "The Blue Bell Review is a quarterly magazine that takes a maximum of two "
    "prose pieces of under 2,500 words each. It reserves First Serial Rights, "
    "expects a minimum 30-day response time, and asks that no AI-generated "
    "content be submitted. All submissions are accepted exclusively through its "
    "official Google Form.",
    "https://thebluebellreview.info/submit",
    "https://thebluebellreview.info/submit", None, "Google Form only",
    src("The Blue Bell Review — Submit (official)", "https://thebluebellreview.info/submit"),
    intl(),
    ["fiction", "creative-nonfiction", "essays", "poetry"],
    "Fiction, nonfiction, essays and poetry",
    pay(None, None, None, "Not stated on the public submit page",
        "The public submit page sets out the piece limits, the AI position, the rights position "
        "and the response time, but publishes no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": 2500,
     "display": "Prose: maximum of 2 pieces, under 2,500 words each"},
    {"label": "Minimum 30 days from the date of submission", "band": "1-3-months",
     "official": True},
    "open", None, "prohibited",
    ["Original prose — fiction, nonfiction or essays — a maximum of two pieces of under 2,500 "
     "words each.",
     "Poetry."],
    ["AI-generated content. The magazine asks for original work only.",
     "More than two prose pieces, or any piece over 2,500 words."],
    ["Submit exclusively through the official Google Form linked from the submit page.",
     "Send at most two prose pieces, each under 2,500 words.",
     "Expect at least 30 days before a response."],
    "The Blue Bell Review reserves First Serial Rights, which includes the right to publish the "
    "piece in its quarterly magazine.",
    ["Read https://thebluebellreview.info/submit and use the Google Form — it is the only route.",
     "Two pieces is the ceiling, so send your best two.",
     "Budget for a 30-day minimum wait."],
    ["blue bell review", "prose", "poetry", "essays", "2500 words", "google form",
     "first serial rights", "30 day response", "no ai"]))

# ------------------------------------------- 5 River Styx
NEW.append(rec(
    "river-styx-magazine", "River Styx Magazine",
    "Stories, essays, poetry and translation",
    "River Styx: paid by PayPal or Venmo only, stories to 1,500 words",
    "River Styx Magazine pays contributors but states no rate, and is explicit "
    "that it pays only by PayPal or Venmo — no paper checks, ACH transfers, "
    "Western Union or Cash App. It takes stories of 1,500 words or fewer in "
    "groups of up to three, and essays of 500 words or fewer in the same "
    "grouping. Copyright reverts to the author once the work is published.",
    "https://www.riverstyx.org/submit",
    "https://www.riverstyx.org/submit", None,
    "Submittable — portal closes when capacity is reached",
    src("River Styx Magazine — Submit (official)", "https://www.riverstyx.org/submit"),
    intl(),
    ["fiction", "essays", "poetry", "translation"],
    "Stories, essays, poetry and translation",
    pay(None, None, None, "Pays, but no rate is stated; PayPal or Venmo only",
        "Official submit page: River Styx states that it only pays contributors via PayPal or "
        "Venmo, and that it does not mail paper checks, do electronic (ACH) transfers, use "
        "Western Union or Cash App, or use any other means of payment. Contributors must include "
        "payment account details on the Contributor Form sent with the acceptance email. No "
        "rate is published, so BRYME records none.",
        "Not publicly stated"),
    {"min": None, "max": 1500,
     "display": "Stories of 1,500 words or fewer in groups of up to three; essays of 500 words "
                "or fewer in groups of up to three"},
    {"label": "Not stated; reading periods run until the issue is filled",
     "band": "not-stated", "official": True},
    "open",
    {"date": None,
     "display": "Reading periods run until River Styx has accepted enough work to complete the "
                "issue, and vary with submission volume and editorial need. If the Submittable "
                "portal is open, the magazine is still accepting work; it closes periodically at "
                "capacity.",
     "recurring": True},
    "not-stated",
    ["Stories of 1,500 words or fewer, sent in groups of up to three.",
     "Essays of 500 words or fewer, sent in groups of up to three.",
     "Translations, where permission has been granted by the copyright owner."],
    ["Translations without permission from the copyright owner."],
    ["Check whether the Submittable portal is open — if it is, the magazine is accepting work.",
     "Group up to three stories of 1,500 words or fewer, or three essays of 500 words or fewer.",
     "Have a PayPal or Venmo account; there is no other payment route.",
     "Include your payment details on the Contributor Form that arrives with an acceptance.",
     "For a translation, have the copyright owner's permission ready."],
    "Once the work has been published in River Styx, the copyright reverts back to the author.",
    ["Read https://www.riverstyx.org/submit and check the portal is open before preparing work.",
     "Short work is explicitly welcome — 500-word essays and 1,500-word stories.",
     "Set up PayPal or Venmo in advance; it is the only way to be paid."],
    ["river styx", "stories", "essays", "poetry", "translation", "paypal", "venmo",
     "1500 words", "500 words", "copyright reverts"]))

# ------------------------------------------- 6 New Letters
NEW.append(rec(
    "new-letters", "New Letters",
    "Poetry, fiction, nonfiction, essays and book reviews",
    "New Letters: $25 book reviews, three $2,000 annual awards",
    "New Letters pays $25 for book reviews, typically, and states that payment "
    "is not guaranteed but made as resources allow. It runs three annual awards "
    "of $2,000 each — the Patricia Cleary Miller Award for Poetry, the Robert "
    "Day Award for Fiction, and the Conger Beasley Jr. Award for nonfiction. "
    "Single-book reviews run 500 to 900 words, and all rights revert to the "
    "author upon publication.",
    "https://www.newletters.org/general-submissions/",
    "https://www.newletters.org/general-submissions/", None, "Submittable only",
    src("New Letters — General Submissions (official)",
        "https://www.newletters.org/general-submissions/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction", "essays", "reviews"],
    "Poetry, fiction, nonfiction, essays and book reviews",
    pay("USD", 25, 2000,
        "$25 for book reviews (not guaranteed); three $2,000 annual awards",
        "Official general submissions page: New Letters pays, typically, $25 for book reviews, "
        "and states that payment is not guaranteed but made as resources allow. Separately it "
        "runs the $2,000 Patricia Cleary Miller Award for Poetry, the $2,000 Robert Day Award "
        "for Fiction and the $2,000 Conger Beasley Jr. Award. The $2,000 figures are contest "
        "awards rather than a publication rate and are recorded as such.",
        "Not publicly stated"),
    {"min": 500, "max": 900,
     "display": "Single-book reviews 500–900 words; essay-reviews of groups of books run longer"},
    {"label": "Every effort to respond within six months; some categories in three to four weeks",
     "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Poetry, fiction, nonfiction and essays.",
     "Book reviews of 500 to 900 words for a single book; essay-reviews of groups of books run "
     "longer.",
     "Reviews of excellent books — including films and visual art — that are not receiving much "
     "attention in the national media, which is the magazine's stated review priority."],
    ["Reviews of books already well covered in the national media."],
    ["Submit only through Submittable, the magazine's online submission manager.",
     "Keep single-book reviews to 500–900 words.",
     "Aim review pitches at under-covered work — that is what New Letters wants.",
     "Expect six months, though some categories are answered in three or four weeks."],
    "All rights revert to the author upon publication.",
    ["Read https://www.newletters.org/general-submissions/ before sending.",
     "The $25 review payment is explicitly not guaranteed — do not budget on it.",
     "The three $2,000 awards are the real money here."],
    ["new letters", "poetry", "fiction", "nonfiction", "book reviews", "$25", "$2000 awards",
     "submittable", "rights revert"]))

# ------------------------------------------- 7 Pennsylvania Literary Journal
NEW.append(rec(
    "pennsylvania-literary-journal", "Pennsylvania Literary Journal",
    "Essays, fiction, poetry and book reviews",
    "Pennsylvania Literary Journal: unpaid, no fees, essays to 10,000 words",
    "Pennsylvania Literary Journal states there is no payment for publication, "
    "but equally that there are no reading fees or publication fees for "
    "contributors, and all authors receive free contributor PDF and epub copies. "
    "It takes essays of 4,000 to 10,000 words and book reviews of 1,200 to 1,600 "
    "words, and is listed in the MLA International Bibliography and the MLA "
    "Directory of Periodicals.",
    "https://anaphoraliterary.com/about/plj-cfp-and-guidelines/",
    "https://anaphoraliterary.com/about/plj-cfp-and-guidelines/", None,
    "See guidelines — no reading or publication fees",
    src("Pennsylvania Literary Journal — CFP and Guidelines (official)",
        "https://anaphoraliterary.com/about/plj-cfp-and-guidelines/"),
    intl(),
    ["essays", "fiction", "poetry", "reviews"],
    "Essays, fiction, poetry and book reviews",
    pay(None, None, None, "Unpaid — but no reading fees or publication fees either",
        "Official CFP and guidelines: there is no payment for publication, but also no reading "
        "fees or publication fees. All authors receive free contributor PDF and epub copies. "
        "BRYME records no figure because there is none. Unlike some unpaid markets this one "
        "charges nothing to enter.",
        "Not applicable — unpaid"),
    {"min": 4000, "max": 10000,
     "display": "Essays 4,000–10,000 words; book reviews 1,200–1,600 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Essays of 4,000 to 10,000 words.",
     "Book reviews of 1,200 to 1,600 words. Free books can be requested from major academic "
     "publishers on a reviewer's behalf, or a finished review may be submitted for "
     "consideration.",
     "Fiction and poetry."],
    ["An expectation of payment. The journal is explicit that there is none."],
    ["Read the CFP and guidelines page before sending.",
     "Keep essays between 4,000 and 10,000 words and reviews between 1,200 and 1,600.",
     "If you want to review, you can request a free book from an academic publisher through the "
     "journal.",
     "No fee either way — nothing to lose but the word count."],
    "Not stated on the official CFP and guidelines page.",
    ["Read https://anaphoraliterary.com/about/plj-cfp-and-guidelines/ before sending.",
     "This is unpaid but also fee-free, and it is MLA-indexed — worth the credit for academic "
     "work.",
     "The review route can come with a free book."],
    ["pennsylvania literary journal", "anaphora literary", "essays", "book reviews", "unpaid",
     "no fees", "4000-10000 words", "mla indexed"]))

# ------------------------------------------- 8 Pure in Heart Stories
NEW.append(rec(
    "pure-in-heart-stories", "Pure in Heart Stories", "Fiction, poetry and nonfiction",
    "Pure in Heart Stories: unpaid, no AI of any kind, 4–8 weeks",
    "Pure in Heart States it does not offer payment because it does not have the "
    "funds, and gives every contributor a free digital copy of the issue they "
    "appear in. It asks for one to five poems in a single attachment and takes "
    "no AI-generated work of any kind, including images. It takes first "
    "electronic rights and replies in about four to eight weeks.",
    "https://pureinheartstories.com/submissions/",
    "https://pureinheartstories.com/submissions/", None,
    "Online submission during reading periods",
    src("Pure in Heart Stories — Submissions (official)",
        "https://pureinheartstories.com/submissions/"),
    intl(),
    ["fiction", "poetry", "creative-nonfiction"], "Fiction, poetry and nonfiction",
    pay(None, None, None, "Unpaid — a free digital copy of the issue is offered instead",
        "Official submissions page: Pure in Heart Stories states it does not offer payment "
        "because it does not have the funds, and that all contributors will receive a free "
        "digital copy of the issue in which they appear. BRYME records no figure because there "
        "is none.",
        "Not applicable — unpaid"),
    {"min": None, "max": None, "display": "Poetry: 1–5 poems in one attachment"},
    {"label": "About 4–8 weeks", "band": "1-3-months", "official": True},
    "open",
    {"date": None,
     "display": "Submission reading periods are posted on the submissions page.",
     "recurring": True},
    "prohibited",
    ["Fiction, poetry and nonfiction that is humorous or adventurous, or both — that is the "
     "stated editorial preference.",
     "Poetry: one to five poems in one attachment."],
    ["AI-generated work of any kind, including AI images."],
    ["Check the reading periods on the submissions page.",
     "Send one to five poems in a single attachment.",
     "Aim for humorous or adventurous work.",
     "Expect a reply in four to eight weeks."],
    "Pure in Heart Stories takes first electronic rights, to be the first to publish the work "
    "online, and non-exclusive digital format rights to publish the work in its downloadable "
    "PDF.",
    ["Read https://pureinheartstories.com/submissions/ before sending.",
     "Unpaid — the free digital copy is the whole consideration.",
     "The turnaround is quick for a literary market."],
    ["pure in heart stories", "fiction", "poetry", "unpaid", "free copy", "1-5 poems",
     "4-8 weeks", "no ai"]))

# ------------------------------------------- 9 Raising Mothers
NEW.append(rec(
    "raising-mothers", "Raising Mothers",
    "Fiction, flash, creative nonfiction, interviews and graphic narrative by parents",
    "Raising Mothers: parents only, reader-funded, 3–6 month response",
    "Raising Mothers exclusively seeks work from self-identified mothers and "
    "parents — biological, non-biological, step, foster, grand or adoptive — who "
    "are often marginalised in literary space. It is reader-funded through "
    "subscription tiers rather than paying a rate, takes no AI-created work, and "
    "responds in three to six months.",
    "https://raisingmothers.substack.com/p/guidelines",
    "https://raisingmothers.substack.com/p/guidelines", None, "Online submission",
    src("Raising Mothers — Guidelines (official)",
        "https://raisingmothers.substack.com/p/guidelines"),
    {"summary": "Restricted to self-identified mothers and parents. Raising Mothers states it "
                "exclusively seeks out and supports submissions by self-identified mothers and "
                "parents — biological, non-biological, step, foster, grand or adoptive — who are "
                "often marginalised in literary space. Writers who are not parents are outside "
                "its remit.",
     "mode": "restricted", "includesGroups": ["mothers", "parents", "step-parents",
                                             "foster parents", "adoptive parents",
                                             "grandparents"],
     "includesRegions": [], "allowsDiaspora": True, "notStated": False},
    ["fiction", "creative-nonfiction", "interviews", "reviews"],
    "Fiction, flash, creative nonfiction, interviews, reviews and graphic narrative",
    pay(None, None, None, "No rate stated — the journal is reader-funded by subscription",
        "Official guidelines: Raising Mothers is funded by readers, with subscription tiers "
        "described in terms of what they cover — $6 a month covers the cost of one interview per "
        "year after twelve payments, $115 a year covers one essay, and $195 a year covers one "
        "essay plus one flash piece or interview. Those are supporter prices, not contributor "
        "rates, and BRYME does not record them as payment. No contributor rate is published.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No word limit stated; flash and micro forms are explicitly welcome"},
    {"label": "Three to six months", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Experimental and traditional fiction, micro and flash, creative nonfiction, interviews, "
     "book reviews, and comic or graphic narratives.",
     "Work by self-identified mothers and parents of any kind — biological, non-biological, "
     "step, foster, grand or adoptive."],
    ["Work created by AI.",
     "Work from writers who are not parents — the remit is explicit and exclusive."],
    ["Confirm you are a self-identified mother or parent; that is the entry condition.",
     "Check the reading periods before sending.",
     "Expect three to six months for a response."],
    "By submitting, you grant first electronic rights, exclusive for the first six months upon "
    "publication.",
    ["Read https://raisingmothers.substack.com/p/guidelines before sending.",
     "This is a parent-only market by design — that is the point of it, not an oversight.",
     "Graphic and comic narrative are welcome, which is unusual."],
    ["raising mothers", "parents", "motherhood", "fiction", "flash", "creative nonfiction",
     "interviews", "graphic narrative", "restricted eligibility", "no ai"]))

# ------------------------------------------- 10 New World Writing Quarterly
NEW.append(rec(
    "new-world-writing-quarterly", "New World Writing Quarterly",
    "Fiction, nonfiction, poetry and flash",
    "New World Writing Quarterly: 500–2,500 words for online reading",
    "New World Writing Quarterly prefers work of 500 to 2,500 words for online "
    "reading. All rights except the magazine's reprint rights revert to "
    "individual authors upon publication. No payment rate and no AI policy are "
    "stated on the public submissions page.",
    "https://newworldwriting.net/submissions/",
    "https://newworldwriting.net/submissions/", None, "Online submission",
    src("New World Writing Quarterly — Submissions (official)",
        "https://newworldwriting.net/submissions/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Fiction, nonfiction, poetry and flash",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page states a length preference and a rights position but "
        "publishes no payment rate, so BRYME records no figure. Confirm current terms before you "
        "submit.",
        "Not publicly stated"),
    {"min": 500, "max": 2500,
     "display": "500–2,500 words preferred for online reading"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Fiction, nonfiction, poetry and flash.",
     "Work of 500 to 2,500 words, which is the stated preference for online reading."],
    [],
    ["Read the submissions page before sending.",
     "Aim for 500 to 2,500 words if you are writing for the online edition.",
     "Note that the magazine keeps reprint rights after other rights revert."],
    "All rights except New World Writing's reprint rights revert to individual authors upon "
    "publication.",
    ["Read https://newworldwriting.net/submissions/ before sending.",
     "Short work is the stated preference for online publication.",
     "Neither a rate nor an AI policy is published, so ask before relying on either."],
    ["new world writing quarterly", "fiction", "nonfiction", "poetry", "flash",
     "500-2500 words", "rights revert"]))


BASE = {
    "red-river-review": ("", "International"),
    "redivider": ("", "International"),
    "west-trade-review": ("", "International"),
    "blue-bell-review": ("", "International"),
    "river-styx-magazine": ("", "International"),
    "new-letters": ("", "International"),
    "pennsylvania-literary-journal": ("", "International"),
    "pure-in-heart-stories": ("", "International"),
    "raising-mothers": ("", "International"),
    "new-world-writing-quarterly": ("", "International"),
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
#   thefictiondesk.com       ALREADY IN THE DATABASE as slug the-fiction-desk,
#       one of the original 147. Caught by the slug guard. The rate I had read
#       independently - GBP 25 per thousand words - matches its recorded figure
#       exactly, the second such cross-check.
#
#   sortes.co                Not a guidelines page - the fetch captured the whole
#       magazine site (39,669 words of published fiction). The "signals" that
#       passed the content filter were story text, not submission terms. This is
#       a false positive of the size-based filter and worth remembering.
#   newworldwriting.net      Included, but only because its length and rights
#       terms are genuinely stated. No rate and no AI policy.
#
# 415 usable guidelines pages remain unread. No further crawling required.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
