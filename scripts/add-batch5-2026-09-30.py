#!/usr/bin/env python3
"""Add verified writing-market batch 5 (2026-09-30).

Eleven NEW markets, read from the batch-4 backlog. No crawling was needed: all
450 usable guidelines pages from the Poets & Writers scrape were already on disk
and ranked by data richness in batch4_ranked.json. Batch 4 took the top twelve;
this batch takes the tier below it.

Every figure was read off the publication's own guidelines page on 2026-09-30.
Raw page text is retained under research/batch4/<slug>.txt.

Five of these eleven publish a firm rate. Two pay variably or by award and say
so. Three pay nothing and say so. One, PRISM International, was dropped at the
slug check because it already exists in the original 147 - and the rates I had
independently read off prismmagazine.ca matched its recorded figures exactly
($40 CAD a page prose, $45 poetry), which cross-checks that record. None has been given a number it did not
publish.

Note on base country: none of these eleven is verifiable from its own guidelines
page, so pub-countries records "International" rather than a guess.
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

# ------------------------------------------------------- 1 New England Review
NEW.append(rec(
    "new-england-review", "New England Review",
    "Poetry, fiction, nonfiction, translation and dramatic writing",
    "New England Review: $20 a page, $50 minimum, 12-week response",
    "New England Review pays $20 per page with a $50 minimum, plus two copies of "
    "the issue and a one-year subscription, and $50 for its Staging Style and "
    "other digital features. It takes one piece at a time — up to three if they "
    "are under 1,000 words — and dramatic writing up to 5,000 words. It expects "
    "contributors not to outsource their writing, translating or thinking to "
    "generative AI.",
    "https://nereview.com/submission-guidelines/",
    "https://nereview.com/submission-guidelines/", None,
    "Submittable — paper submissions accepted where Submittable is not usable",
    src("New England Review — Submission Guidelines (official)",
        "https://nereview.com/submission-guidelines/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction", "translation", "drama"],
    "Poetry, fiction, nonfiction, translation and dramatic writing",
    pay("USD", 20, 50, "$20 per page with a $50 minimum, plus 2 copies and a 1-year subscription",
        "Official submission guidelines: payment for work published in the journal is $20 per "
        "page with a $50 minimum, plus two copies of the issue in which the work appears and a "
        "one-year subscription to the print or e-book edition. For Staging Style and other "
        "digital features, payment is $50 and a one-year subscription. The $50 minimum is "
        "recorded as the floor because the per-page rate scales with length.",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "Dramatic writing up to 5,000 words; one piece at a time, or up to three if "
                "each is under 1,000 words"},
    {"label": "Attempted within twelve weeks, sometimes longer; every submission gets a response",
     "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Poetry, fiction, nonfiction, translation and dramatic writing.",
     "Dramatic writing: short plays, monologues and screenplays, up to 5,000 words.",
     "Very short pieces — if the work is under 1,000 words you may send up to three."],
    ["Outsourcing writing, translating or thinking to generative AI. The journal states it "
     "expects contributors to engage honestly with their own creative minds.",
     "More than one piece at a time, unless the pieces are each under 1,000 words."],
    ["Submit through Submittable.",
     "If you cannot use Submittable for any reason, paper submissions are allowed.",
     "Send one piece at a time, or up to three very short ones.",
     "Expect a response — New England Review responds to every submission, aiming for twelve "
     "weeks."],
    "Not stated on the official submission guidelines page.",
    ["Read https://nereview.com/submission-guidelines/ before sending.",
     "Do not bundle pieces unless each is under 1,000 words.",
     "Paper submission is a genuine accessibility route here, not a last resort."],
    ["new england review", "poetry", "fiction", "nonfiction", "translation", "dramatic writing",
     "$20 per page", "$50 minimum", "no generative ai"]))

# ------------------------------------------------------- 2 Ubwali Literary Magazine
NEW.append(rec(
    "ubwali-literary-magazine", "Ubwali Literary Magazine",
    "Fiction, essays, poetry and visual art",
    "Ubwali Literary Magazine: $10 a contributor, no reading fee",
    "Ubwali Literary Magazine offers a one-off $10 payment to each contributor "
    "whose work is accepted, paid per artist rather than per piece, and charges "
    "no reading fees. It takes fiction of 3,000 to 6,000 words, essays of up to "
    "3,000 words and one to three poems. It does not consider or accept "
    "AI-generated work, and all rights revert 90 days after publication.",
    "https://www.ubwali.com/submissions",
    "https://www.ubwali.com/submissions", None, "Online submission — no reading fee",
    src("Ubwali Literary Magazine — Submissions (official)",
        "https://www.ubwali.com/submissions"),
    intl(),
    ["fiction", "essays", "poetry"], "Fiction, essays, poetry and visual art",
    pay("USD", 10, 10, "$10 one-off per accepted contributor",
        "Official submissions page: a one-off $10 payment is offered to artists whose work is "
        "accepted for publication. Ubwali states explicitly that it pays per artist, not per "
        "piece, so submitting three poems earns the same $10 as one. It charges no reading fees.",
        "Not publicly stated"),
    {"min": 3000, "max": 6000,
     "display": "Fiction 3,000–6,000 words; essays up to 3,000 words; 1–3 poems in one document"},
    {"label": "Not stated; a slow reply means the work is still under consideration",
     "band": "not-stated", "official": True},
    "open", None, "prohibited",
    ["Fiction of 3,000 to 6,000 words.",
     "Essays of up to 3,000 words.",
     "One to three poems in a single document.",
     "Visual art."],
    ["AI-generated work. Ubwali states it does not consider or accept it.",
     "Fiction outside the 3,000 to 6,000 word band."],
    ["Send your work through the submissions page; there is no reading fee.",
     "Group poems into a single document, one to three of them.",
     "Keep fiction between 3,000 and 6,000 words and essays under 3,000.",
     "Do not chase a slow reply — Ubwali says a longer wait means the work is still being "
     "considered."],
    "Ubwali requests first serial rights for every piece it accepts. All rights revert to the "
    "author 90 days after publication.",
    ["Read https://www.ubwali.com/submissions before sending.",
     "The payment is per contributor, so send your best set rather than many singles.",
     "No fee, so there is no cost to submitting."],
    ["ubwali", "fiction", "essays", "poetry", "$10", "3000-6000 words", "no reading fee",
     "rights revert 90 days", "no ai"]))

# ------------------------------------------------------- 3 Blood Tree Literature
NEW.append(rec(
    "blood-tree-literature", "Blood Tree Literature",
    "Flash poetry, fiction, nonfiction and hybrid work",
    "Blood Tree Literature: $10 poetry, $15 prose, $20 hybrid",
    "Blood Tree Literature pays $10 for poetry, $15 for fiction and nonfiction "
    "and $20 for hybrid pieces, all in USD through PayPal, against a $3 "
    "submission fee. It leans flash. AI-generated work is strictly prohibited, "
    "and contributors retain copyright, free to republish elsewhere after six "
    "months with attribution.",
    "https://www.bloodtreeliterature.com/submit",
    "https://www.bloodtreeliterature.com/submit", None,
    "Submittable — $3 fee, optional $15 feedback tier",
    src("Blood Tree Literature — Submit (official)",
        "https://www.bloodtreeliterature.com/submit"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Flash poetry, fiction, nonfiction and hybrid pieces",
    pay("USD", 10, 20, "$10 poetry; $15 fiction and nonfiction; $20 hybrid pieces",
        "Official submit page: per piece accepted, Blood Tree Literature pays $10 for poetry, "
        "$15 for fiction and nonfiction, and $20 for hybrid pieces. All payments are in USD and "
        "processed through PayPal. A $3 submission fee applies, and a $15 tier buys detailed "
        "feedback and constructive notes. Fees go toward Submittable and domain costs, paying "
        "contributors and contest donations.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Flash-focused — the magazine states it likes to keep it flash-y"},
    {"label": "Query by email after three months", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Flash poetry, fiction, nonfiction and hybrid pieces.",
     "Mixed-media work, provided every image or audiovisual element is fully owned by the "
     "submitting author."],
    ["AI-generated work. Strictly prohibited. Blood Tree also states that any use of the "
     "publication to train generative AI technologies is expressly prohibited.",
     "Pieces using unlicensed images or audiovisual elements — rejected on copyright grounds."],
    ["Submit through Submittable and pay the $3 fee.",
     "Optionally take the $15 feedback tier if you want detailed notes.",
     "Write flash — that is the house preference.",
     "Query by email if three months pass with no response."],
    "Contributors retain copyright for their accepted work and may publish it elsewhere after "
    "six months have passed since the Blood Tree Literature publication date, with attribution "
    "to its first appearance.",
    ["Read https://www.bloodtreeliterature.com/submit before sending.",
     "Keep it short — flash is what the magazine wants.",
     "Only query after three months."],
    ["blood tree literature", "flash", "poetry", "fiction", "nonfiction", "hybrid", "$20",
     "paypal", "copyright retained", "no ai"]))

# ------------------------------------------------------- 4 Foglifter
NEW.append(rec(
    "foglifter", "Foglifter",
    "Fiction, nonfiction, poetry and translation",
    "Foglifter: $100 honorarium, author and translator both paid",
    "Foglifter pays a $100 honorarium by PayPal plus two copies of the issue, "
    "and where a translation is published both author and translator receive an "
    "honorarium. It takes up to 7,500 words of fiction or nonfiction and three "
    "to five poems, and accepts only first rights. AI-generated work is "
    "automatically disqualified. Its fiction and poetry submission caps for the "
    "current reading period were reached in August and September 2026.",
    "https://www.foglifterjournal.com/submit",
    "https://www.foglifterjournal.com/submit", None, "Submittable",
    src("Foglifter — Submit (official)", "https://www.foglifterjournal.com/submit"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry", "translation"],
    "Fiction, nonfiction, poetry and translation",
    pay("USD", 100, 100, "$100 honorarium plus two copies; translators paid separately",
        "Official submit page: contributors receive two copies of the issue in which they appear "
        "and a $100 honorarium via PayPal. For translated work, both author and translator "
        "receive an honorarium.",
        "Not publicly stated"),
    {"min": None, "max": 7500,
     "display": "Up to 7,500 words of fiction or nonfiction (up to three flash pieces); "
                "3–5 poems, one per page, max 5 pages"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "closed",
    {"date": None,
     "display": "Foglifter reached its submission cap for fiction on 26 August 2026 and for "
                "poetry on 12 September 2026, within the Foglifter 12 reading period. Poetry is "
                "capped at 500 submissions. Check the current call on its Submittable page "
                "before preparing work — other genres may still be open, and the next reading "
                "period will reopen them.",
     "recurring": True},
    "prohibited",
    ["Fiction or nonfiction of up to 7,500 words, including up to three flash fiction pieces.",
     "Poetry: three to five poems, one poem per page, maximum five pages.",
     "Translated work in all genres, provided rights were secured before submission.",
     "Art in all mediums except AI."],
    ["AI-generated work of any kind. It is automatically disqualified, and no AI art "
     "submissions are accepted.",
     "Multi-modal components where the submitting poet does not hold the copyright.",
     "Translations where rights were not secured before submission.",
     "More than one submission per genre in a reading period."],
    ["Check the current call on Foglifter's Submittable page first — caps are reached early.",
     "Only one submission per genre is permitted each reading period.",
     "Simultaneous submissions are accepted, but withdraw immediately on acceptance elsewhere, "
     "or message through Submittable for a partial withdrawal.",
     "Secure translation rights before you send."],
    "Foglifter accepts only first rights to publication.",
    ["Check https://www.foglifterjournal.com/submit and the Submittable call for what is "
     "currently open.",
     "Fiction and poetry were capped as of late September 2026 — wait for the next reading "
     "period rather than sending into a closed call.",
     "Translators are paid separately, so a translation is worth two honoraria."],
    ["foglifter", "fiction", "nonfiction", "poetry", "translation", "$100", "7500 words",
     "first rights", "submission cap", "no ai"]))

# ------------------------------------------------------- 5 The Dolomite Review
NEW.append(rec(
    "the-dolomite-review", "The Dolomite Review",
    "Fiction, poetry and first-person essays",
    "The Dolomite Review: $50 featured work, 2,500-word stories",
    "The Dolomite Review awards $50 each to one featured poem, one featured "
    "short story and one featured essay per issue from its Fall 2026 issue, "
    "against a $3.50 submission fee. Short stories run to 2,500 words. It asks "
    "submitters to confirm the work is original and human-authored with no "
    "AI-generated text or assistance, and all rights revert after publication.",
    "https://www.thedolomitereview.com/submit",
    "https://www.thedolomitereview.com/submit", None,
    "Online submission — $3.50 fee",
    src("The Dolomite Review — Submit (official)",
        "https://www.thedolomitereview.com/submit"),
    intl(),
    ["fiction", "poetry", "essays"], "Fiction, poetry and first-person essays",
    pay("USD", 50, 50, "$50 to one featured poem, one short story and one essay per issue",
        "Official submit page: beginning with the Fall 2026 issue, The Dolomite Review awards "
        "$50 each to one featured poem, one featured short story and one featured essay per "
        "issue. This is an award for featured work, not a rate paid to every accepted "
        "contributor, and BRYME records it as such. A $3.50 submission fee applies to all "
        "manuscripts.",
        "Not publicly stated"),
    {"min": None, "max": 2500, "display": "Short stories no more than 2,500 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Fiction, poetry and first-person essays that resonate with clarity, curiosity and depth.",
     "Short stories of no more than 2,500 words."],
    ["AI-generated text or assistance of any kind. The submission form requires an attestation "
     "that the work is original and human-authored and contains no AI-generated text or "
     "assistance. The magazine describes itself as open to all and not discriminating — except "
     "against artificial intelligence."],
    ["Submit through the submissions page and pay the $3.50 fee.",
     "Keep short stories to 2,500 words.",
     "Double-space everything except poetry.",
     "Tick the human-authorship attestation honestly — it is a condition of submission."],
    "The Dolomite Review requests first electronic rights and the right to archive the piece on "
    "its website. After publication all rights revert to the author, with the understanding "
    "that the magazine is credited as the original publisher if the work appears elsewhere.",
    ["Read https://www.thedolomitereview.com/submit before sending.",
     "The $50 is a featured-work award, so most accepted contributors are not paid — submit "
     "with that understood.",
     "Double-space prose; leave poetry single."],
    ["dolomite review", "fiction", "poetry", "essays", "$50", "2500 words", "human authored",
     "no ai"]))

# ------------------------------------------------------- 6 Hayden's Ferry Review
NEW.append(rec(
    "haydens-ferry-review", "Hayden's Ferry Review",
    "Poetry, micro-fiction, essays and stories",
    "Hayden's Ferry Review: contributor honorarium, no AI in part",
    "Hayden's Ferry Review pays each print contributor a modest honorarium from "
    "its contributor fund from fall 2026, with the amount depending on the funds "
    "available each semester and therefore no published figure. It takes up to "
    "six poems or micro-fictions, or one essay or story, for a $3 submission "
    "fee, and sets aside free submissions each reading period. It does not "
    "accept work produced wholly or in part by AI.",
    "https://haydensferryreview.com/submit",
    "https://haydensferryreview.com/submit", None,
    "Submittable — $3 fee, free slots set aside each period",
    src("Hayden's Ferry Review — Submit (official)",
        "https://haydensferryreview.com/submit"),
    intl(),
    ["poetry", "fiction", "essays"], "Poetry, micro-fiction, essays and stories",
    pay(None, None, None,
        "Modest honorarium from the contributor fund; amount varies by semester, no figure stated",
        "Official submit page: starting in fall 2026, Hayden's Ferry Review can pay each print "
        "contributor a modest honorarium from its contributor fund, but states that the amount "
        "will depend on the funds available each semester. Because no figure is published, "
        "BRYME records none. There is a $3 submission fee to the print journal in all genres "
        "except art, and a set number of free submissions during each open reading period.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Up to 6 poems or micro-fictions, or one essay or story"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Up to six poems or micro-fictions.",
     "One essay or one story.",
     "Art, which carries no submission fee."],
    ["Work produced wholly or in part by AI. The magazine does not accept it in any proportion.",
     "A second submission in the same genre before the first has been answered."],
    ["Submit through Submittable.",
     "Pay the $3 fee in any genre except art, or use one of the free submission slots set aside "
     "each reading period.",
     "Send one submission per genre at a time for print issues and wait for a response before "
     "sending more.",
     "If work is accepted elsewhere, notify the editors immediately by adding a message to the "
     "submission in Submittable."],
    "You or the copyright owner retain copyright and the right of reprint. After publication all "
    "rights except those stated by the magazine revert to the copyright owner.",
    ["Read https://haydensferryreview.com/submit before sending.",
     "Look for the free submission slots if the fee is a barrier.",
     "One genre at a time, and wait for the answer."],
    ["hayden's ferry review", "poetry", "micro-fiction", "essays", "honorarium", "6 poems",
     "free submissions", "no ai"]))

# ------------------------------------------------------- 7 Hemlock Journal
NEW.append(rec(
    "hemlock-journal", "The Hemlock Journal",
    "Poetry, fiction, nonfiction and visual art",
    "Hemlock Journal: $15 for print, fee refunded for digital",
    "The Hemlock Journal pays $15 for each piece selected for print and refunds "
    "the submission fee to contributors published digitally. Fiction and "
    "nonfiction run from 1,000 to 4,000 words, with anything shorter treated as "
    "flash, and each poetry submission may hold two poems across five pages. "
    "Rights remain with the author and the artist.",
    "https://thehemlockjournal.com/submissions/",
    "https://thehemlockjournal.com/submissions/", None,
    "Online submission — $3 expedited response option",
    src("The Hemlock Journal — Submissions (official)",
        "https://thehemlockjournal.com/submissions/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, fiction, nonfiction and visual art",
    pay("USD", 15, 15, "$15 per piece selected for print; fee refunded for digital publication",
        "Official submissions page: The Hemlock Journal pays $15 for each piece selected for "
        "print, and refunds the submission fee to contributors of digital versions. An expedited "
        "response of under two weeks is available for $3 per submission. The $15 applies to "
        "print selection only; a digital-only contributor receives a fee refund rather than a "
        "payment.",
        "Not publicly stated"),
    {"min": 1000, "max": 4000,
     "display": "Fiction and nonfiction 1,000–4,000 words; under 1,000 is flash; poetry max 2 "
                "poems and 5 pages"},
    {"label": "Not stated; expedited response under two weeks for $3",
     "band": "not-stated", "official": True},
    "open", None, "not-stated",
    ["Poetry, fiction, nonfiction and visual art.",
     "Fiction and nonfiction of 1,000 to 4,000 words, typed in Times New Roman or a similar "
     "font, single-spaced.",
     "Flash fiction — pieces shorter than 1,000 words, submitted under the same category with "
     "the submission noted.",
     "Poetry: a maximum of two poems and five pages in total, all poems in a single document.",
     "Previously published work, provided the author retains all the rights."],
    ["Fiction or nonfiction outside the 1,000 to 4,000 word band, unless it is flash.",
     "More than two poems or more than five pages in a poetry submission.",
     "Previously published work where the author no longer holds the rights."],
    ["Send one complete work of fiction or nonfiction per submission.",
     "Put all poems in one single document, maximum two poems and five pages.",
     "Take the $3 expedited option if you need an answer in under two weeks.",
     "Check the site and the magazine's Instagram for commencement dates and deadlines."],
    "The rights remain with the author and the artist. The Hemlock Journal retains the right to "
    "publish the submitted work, if selected, in its upcoming issues, whether in print or "
    "digitally.",
    ["Read https://thehemlockjournal.com/submissions/ before sending.",
     "Flash is a legitimate route here — under 1,000 words is welcome, just label it.",
     "Check the current submission window; dates are announced on the site and Instagram."],
    ["hemlock journal", "poetry", "fiction", "nonfiction", "$15", "1000-4000 words",
     "flash", "expedited response", "rights retained"]))

# ------------------------------------------------------- 8 Midway Journal
NEW.append(rec(
    "midway-journal", "Midway Journal",
    "Flash fiction, nonfiction, stories, essays and poetry",
    "Midway Journal: $40 for flash or one story, 2,000 words",
    "Midway Journal pays $40 for two works of flash fiction or nonfiction, or "
    "for one story or essay of up to eight double-spaced pages or 2,000 words. "
    "It takes three to five poems in a single document, each beginning on a new "
    "page, and asks for aesthetically ambitious work that invokes the colliding "
    "energies of the fairgrounds. Response time is three to six months.",
    "https://midwayjournal.com/submissions/",
    "https://midwayjournal.com/submissions/", None,
    "Online submission — $3 expedited reading option",
    src("Midway Journal — Submissions (official)",
        "https://midwayjournal.com/submissions/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"],
    "Flash fiction, nonfiction, stories, essays and poetry",
    pay("USD", 40, 40,
        "$40 for 2 flash works, or 1 story or essay up to 8 double-spaced pages / 2,000 words",
        "Official submissions page: fiction and nonfiction pay $40 for two works of flash "
        "fiction or nonfiction, or for one story or essay of up to eight double-spaced pages or "
        "2,000 words. A $3.00 tip jar buys a guaranteed careful, expedited reading. All funds "
        "from submissions go toward the rising costs of operating and maintaining the journal. "
        "No separate poetry rate is stated on the page.",
        "Not publicly stated"),
    {"min": None, "max": 2000,
     "display": "One story or essay up to 8 double-spaced pages / 2,000 words, or two flash "
                "works; 3–5 poems each on a new page"},
    {"label": "Three to six months; wait two weeks before inquiring",
     "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Aesthetically ambitious work that invokes the colliding and converging energies of the "
     "fairgrounds — that is the journal's stated theme.",
     "Two works of flash fiction or nonfiction, or one story or essay up to 2,000 words.",
     "Poetry: three to five poems in a single document, each poem beginning on a new page, "
     "single-spaced."],
    ["Work that ignores the fairgrounds conceit — it is the journal's organising idea, not a "
     "loose suggestion."],
    ["Send three to five poems in a single document with each poem starting on a new page.",
     "Single-space poetry manuscripts.",
     "Take the $3 tip jar option if you want a guaranteed expedited reading.",
     "Allow three to six months before inquiring, and wait at least two weeks before any status "
     "question."],
    "Not stated on the official submissions page.",
    ["Read https://midwayjournal.com/submissions/ and read the poetry preferences page too.",
     "Write to the fairgrounds theme.",
     "Do not query before two weeks, and expect three to six months."],
    ["midway journal", "flash fiction", "nonfiction", "poetry", "$40", "2000 words",
     "fairgrounds", "3-5 poems"]))

# ------------------------------------------------------- 9 MockingHeart Review
NEW.append(rec(
    "mockingheart-review", "MockingHeart Review",
    "Poetry, fiction and nonfiction",
    "MockingHeart Review: unpaid, no fee, rights revert on publication",
    "MockingHeart Review states plainly that it cannot pay contributors at this "
    "time, and equally that it charges no submission fee. Submitters whose work "
    "is accepted grant first North American serial rights, but rights revert to "
    "the creator upon publication. AI-generated work is not considered and "
    "senders are banned from submitting again.",
    "https://mockingheartreview.com/submit/",
    "https://mockingheartreview.com/submit/", None,
    "Online submission during reading periods only",
    src("MockingHeart Review — Submit (official)",
        "https://mockingheartreview.com/submit/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"], "Poetry, fiction and nonfiction",
    pay(None, None, None, "Unpaid — the magazine states it cannot pay contributors at this time",
        "Official submit page: MockingHeart Review states that it regrets it cannot pay "
        "contributors at this time, and that it does not charge a submission fee either. BRYME "
        "records no figure because there is none. Treat this as an unpaid market with no cost to "
        "enter.",
        "Not applicable — unpaid"),
    {"min": None, "max": None, "display": "No word limit stated on the submit page"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open",
    {"date": None,
     "display": "Submissions are only considered during the reading periods listed on the "
                "submit page. Submissions outside those periods are ignored unless solicited.",
     "recurring": True},
    "prohibited",
    ["Poetry, fiction and nonfiction submitted during an open reading period."],
    ["AI-generated work. It will not be considered, and the magazine states that senders of "
     "such work will be banned from submitting again.",
     "Defamatory, discriminatory or plagiarized work — same consequence.",
     "Submissions outside the listed reading periods, unless solicited."],
    ["Read the guidelines before submitting — the magazine asks for this explicitly.",
     "Check the listed reading periods; outside them your work is ignored.",
     "Send only original, human-made work."],
    "Submitters whose work is accepted grant MockingHeart Review first North American serial "
    "rights, but rights revert to the creator upon publication.",
    ["Read https://mockingheartreview.com/submit/ and check the reading period dates.",
     "This is unpaid and fee-free — submit for the credit, not the money.",
     "Rights revert immediately on publication, so you can reprint quickly."],
    ["mockingheart review", "poetry", "fiction", "nonfiction", "unpaid", "no fee", "fnasr",
     "rights revert", "reading periods", "no ai"]))

# ------------------------------------------------------- 10 Rawhead
NEW.append(rec(
    "rawhead", "Rawhead",
    "Poetry, fiction and nonfiction",
    "Rawhead: unpaid standard submissions, $100 award per issue",
    "Rawhead takes poetry of up to seven poems across fifteen pages and fiction "
    "or nonfiction of up to 3,000 words. Standard submissions are unpaid — the "
    "journal says it is actively seeking funding and hopes to pay all "
    "contributors one day — but it awards $100 each to one outstanding artist "
    "and one standout writer per standard issue, and $30 to each featured "
    "contributor in Rawhead: Point Blank. Submissions must be original, "
    "human-made and free of AI assistance.",
    "https://rawheadjournal.org/submit-to-rawhead/",
    "https://rawheadjournal.org/submit-to-rawhead/", None,
    "Submittable — paid expedited response options",
    src("Rawhead — Submit to Rawhead (official)",
        "https://rawheadjournal.org/submit-to-rawhead/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"], "Poetry, fiction and nonfiction",
    pay(None, None, None,
        "Standard submissions unpaid; $100 award to one writer and one artist per issue",
        "Official submit page: Rawhead states it is actively seeking funding and hopes to one "
        "day offer payment to all contributors, so standard submissions are currently unpaid. It "
        "does select one outstanding artist and one standout writer from each standard issue to "
        "receive a $100 award, and awards each featured contributor in Rawhead: Point Blank $30. "
        "Paid expedited responses are available: $5 and $10 for a guaranteed decision within two "
        "weeks, and $15 for a 72 business hour priority response. BRYME records no standard rate "
        "because there is none.",
        "Not applicable — standard submissions unpaid"),
    {"min": None, "max": 3000,
     "display": "Fiction and nonfiction up to 3,000 words; up to 7 poems totalling 15 pages"},
    {"label": "Not stated; two weeks guaranteed for a $5 or $10 expedited option",
     "band": "not-stated", "official": True},
    "open", None, "prohibited",
    ["Poetry: up to seven poems totalling no more than fifteen pages.",
     "Fiction and nonfiction of up to 3,000 words.",
     "Visual art — one artist per issue receives a $100 award."],
    ["AI-generated content. Submissions must be original, human-made and free of AI assistance."],
    ["Submit through Submittable.",
     "Keep prose to 3,000 words and poetry to seven poems across fifteen pages.",
     "Take a paid expedited option if you need a decision fast — $5 or $10 for two weeks, $15 "
     "for 72 business hours.",
     "Critique packages are available on Submittable if you want the work developed first."],
    "By accepting publication, authors grant Rawhead First Serial Rights, Non-Exclusive Reprint "
    "Rights, Electronic Rights, Archival Rights and Non-Exclusive Anthology Rights.",
    ["Read https://rawheadjournal.org/submit-to-rawhead/ before sending.",
     "Standard submissions are unpaid — the $100 is a per-issue award, not a rate.",
     "Pay for speed only if you need it; the standard queue is free."],
    ["rawhead", "poetry", "fiction", "nonfiction", "3000 words", "7 poems", "unpaid",
     "$100 award", "expedited response", "no ai"]))

# ------------------------------------------------------- 11 Braided Way
NEW.append(rec(
    "braided-way", "Braided Way: Faces & Voices of Spiritual Practice",
    "Personal essays, articles, fiction and poetry",
    "Braided Way: unpaid, 2,500 words, no AI-assisted work",
    "Braided Way states it is not yet a paying publication and invites "
    "contributors to promote their own publications, workshops or website in "
    "their bio instead. Personal essays, articles and fiction run to 2,500 words "
    "and it takes one to five poems. It asks for no AI-assisted work and for a "
    "line attesting that you are the originator of the work and own all rights.",
    "https://braidedway.org/submissions/",
    "https://braidedway.org/submissions/", None,
    "Online submission — unpaid, self-promotion invited in bio",
    src("Braided Way — Submissions (official)", "https://braidedway.org/submissions/"),
    intl(),
    ["personal-essays", "essays", "fiction", "poetry"],
    "Personal essays, articles, fiction and poetry on spiritual practice",
    pay(None, None, None, "Unpaid — the magazine states it is not yet a paying publication",
        "Official submissions page: Braided Way states it is not yet a paying publication, and "
        "welcomes contributors to promote their publications, workshops and website in their bio "
        "instead. BRYME records no figure because there is none. The trade here is exposure "
        "rather than money.",
        "Not applicable — unpaid"),
    {"min": None, "max": 2500,
     "display": "Personal essays, articles and fiction up to 2,500 words; one to five poems"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Personal essays of up to 2,500 words on spiritual practice.",
     "Articles of up to 2,500 words.",
     "Fiction of up to 2,500 words.",
     "Poetry: one to five poems.",
     "A third-person bio of no more than 300 words, with a website or social media link — "
     "Braided Way explicitly invites you to use it for self-promotion."],
    ["AI-assisted work. The magazine asks that none be sent.",
     "Prose over 2,500 words."],
    ["Include a line attesting that you are the originator of the work and own all rights.",
     "Include a third-person bio of 300 words or fewer plus a link.",
     "Keep prose to 2,500 words and send one to five poems.",
     "Use the bio to promote your own work — that is the offer being made in place of payment."],
    "Braided Way asks submitters to attest that they are the originator of the work and own all "
    "rights. No specific rights transfer is stated on the submissions page.",
    ["Read https://braidedway.org/submissions/ before sending.",
     "This is unpaid — the value is the bio link and the credit.",
     "Include the rights attestation or the submission is incomplete."],
    ["braided way", "spiritual practice", "personal essays", "articles", "fiction", "poetry",
     "unpaid", "2500 words", "no ai"]))


BASE = {
    "new-england-review": ("", "International"),
    "ubwali-literary-magazine": ("", "International"),
    "blood-tree-literature": ("", "International"),
    "foglifter": ("", "International"),
    "the-dolomite-review": ("", "International"),
    "haydens-ferry-review": ("", "International"),
    "hemlock-journal": ("", "International"),
    "midway-journal": ("", "International"),
    "mockingheart-review": ("", "International"),
    "rawhead": ("", "International"),
    "braided-way": ("", "International"),
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
#   prismmagazine.ca         ALREADY IN THE DATABASE as slug prism-international,
#       one of the original 147. Caught by the slug-collision guard. Its recorded
#       rates match what I read off the site today, so no correction is needed.
#
#   skyislandjournal.com     $4.99 fee, clear AI position, but states it cannot
#       provide monetary payment and argues publicity is worth more than a token
#       payment. Recordable; needs the argument stated fairly.
#   themetaworker.com        AI prohibited, copyright retained, 3-6 month
#       response, no pay figure anywhere.
#   globalmajoritypress.org  (The B'K) pays $10, but only to racially or
#       ethnically marginalised, gender-variant or disabled submitters. That
#       eligibility condition has to be recorded exactly, and still needs the
#       fuller read it did not get here.
#   pitheadchapel.com        Unpaid, under 4,000 words, no AI, caps at 300
#       submissions a month. Queued for the unpaid-market pass.
#   haiku shack / hootreview / storyunlikely
#       Fee, prize or membership models rather than a submissions rate.
#
# Remaining backlog: 426 usable guidelines pages still unread, of which the
# large majority state a pay figure. No further crawling is required.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
