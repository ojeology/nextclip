#!/usr/bin/env python3
"""Add verified writing-market batch 11 (2026-09-30).

Eight NEW markets read from the batch-4 backlog. No crawling.
Every figure read off the publication's own page on 2026-09-30.

One correction worth recording: the ranking extractor flagged Lowestoft
Chronicle as mentioning AI. Grepping the page shows those hits are an author's
name in a credits line - there is no AI sentence on the page at all. The record
therefore carries aiPolicy = not-stated. Recording "prohibited" would have been
a fabrication invented from a false positive.

Two fee-not-payment markets are recorded with no contributor rate, because the
money flows from the writer:
  blank-spaces  $6 fiction feature / $3 everything else is a SUBMISSION fee;
                contributors are invited to BUY a print copy at a discount.
  milk-press    $5 reading fee funds the Poetry Society of New York's free
                programmes.
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

# ------------------------------------------- 1 River Teeth
NEW.append(rec(
    "river-teeth", "River Teeth: A Journal of Nonfiction Narrative",
    "Nonfiction narrative and reviews",
    "River Teeth: $100 plus two issues and a year's subscription",
    "River Teeth pays $100 for published work, plus two complimentary issues, a "
    "one-year subscription, and the option to buy further copies at a "
    "discounted contributor's rate. It takes submissions through Submittable "
    "with a $3 processing fee, asks for one piece at a time, and does not "
    "accept work created with the assistance of generative AI.",
    "https://riverteethjournal.com/submission-guidelines/",
    "https://riverteethjournal.com/submission-guidelines/", None,
    "Submittable — $3 processing fee",
    src("River Teeth — Submission Guidelines (official)",
        "https://riverteethjournal.com/submission-guidelines/"),
    intl(),
    ["creative-nonfiction", "reviews", "essays"],
    "Nonfiction narrative and reviews",
    pay("USD", 100, 100,
        "$100, plus two complimentary issues, a one-year subscription and "
        "discounted further copies",
        "Official submission guidelines: if published, the writer receives $100, two "
        "complimentary issues of the journal, a one-year subscription, and the option to "
        "purchase additional copies at a discounted contributor's rate. Submissions carry a "
        "$3 processing fee.",
        "Not publicly stated"),
    {"min": 1000, "max": 1200,
     "display": "Reviews 1,000–1,200 words; no limit stated for nonfiction narrative"},
    {"label": "Three to six months", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Nonfiction narrative.",
     "Reviews, in the neighbourhood of 1,000 to 1,200 words.",
     "One piece at a time — the journal asks you to submit one beautiful thing at a time."],
    ["Submissions created with the assistance of generative AI.",
     "Multiple simultaneous submissions."],
    ["Submit through Submittable with the $3 processing fee.",
     "Send one piece at a time.",
     "Keep reviews to about 1,000 to 1,200 words.",
     "Allow three to six months, though the team says it works to return submissions sooner "
     "while giving each a fair read."],
    "Not stated in detail on the guidelines page.",
    ["Read https://riverteethjournal.com/submission-guidelines/ before sending.",
     "The $3 fee is per submission, so send your best single piece.",
     "Reviews have their own length band — do not send a narrative at review length."],
    ["river teeth", "nonfiction narrative", "reviews", "$100", "submittable", "$3 fee",
     "1000-1200 words", "no generative ai"]))

# ------------------------------------------- 2 The Baltimore Review
NEW.append(rec(
    "the-baltimore-review", "The Baltimore Review",
    "Poetry, short fiction and creative nonfiction",
    "The Baltimore Review: $75, rights revert, no AI at all",
    "The Baltimore Review pays $75 for non-contest work — as an Amazon gift "
    "certificate, or through PayPal if preferred — plus a copy of the annual "
    "print compilation in which the work appears. It does not accept work "
    "generated in whole or in part by AI, declines prose over 5,000 words, and "
    "notifies you within four months. All rights revert to the author.",
    "https://baltimorereview.org/submit",
    "https://baltimorereview.org/submit", None,
    "Submittable only — no email or post",
    src("The Baltimore Review — Submit (official)", "https://baltimorereview.org/submit"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, short fiction and creative nonfiction",
    pay("USD", 75, 75,
        "$75 as an Amazon gift certificate or via PayPal, plus a copy of the annual print "
        "compilation",
        "Official submit page: payment for non-contest submissions is $75 via Amazon gift "
        "certificate, or $75 through PayPal if preferred, as well as a copy of the annual print "
        "compilation in which the author's work appears. Contest submissions carry a separate "
        "$8 fee, and contest prizes are not recorded here as a market rate.",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "Prose up to 5,000 words; no more than three poems"},
    {"label": "Within four months", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Poetry, short fiction and creative nonfiction, selected from the Submittable queue on "
     "merit and the needs of the journal.",
     "Submissions in more than one category."],
    ["Work generated in whole or in part by artificial intelligence. The review states it wants "
     "to provide a space for human expression and believes human voices and ideas are powerful.",
     "Prose exceeding 5,000 words.",
     "More than three poems in a submission.",
     "A book review, or other work that is clearly not creative nonfiction.",
     "Multiple submissions during one submission period.",
     "Emailed submissions or submissions sent by post — neither is considered."],
    ["Submit through Submittable. Email and postal submissions are not considered.",
     "Keep prose under 5,000 words and send at most three poems.",
     "Submit once per category per reading period.",
     "Expect a decision within four months.",
     "Confirm in the agreement that you are the sole author and own all rights to your work."],
    "All rights revert to the author after publication. In the agreement for accepted work, "
    "authors must confirm they are the sole author and own all rights to their work.",
    ["Read https://baltimorereview.org/submit before sending.",
     "The $75 applies to non-contest work — the $8 fee is for contests.",
     "Submittable is the only route in."],
    ["the baltimore review", "poetry", "short fiction", "creative nonfiction", "$75",
     "paypal", "amazon gift certificate", "submittable", "rights revert", "no ai"]))

# ------------------------------------------- 3 Cholla Needles
NEW.append(rec(
    "cholla-needles", "Cholla Needles", "Poetry, stories and essays",
    "Cholla Needles: two copies, copyright returns on publication",
    "Cholla Needles pays two copies of the printed magazine to US authors. "
    "Poets send six to twelve original poems by email, in the body or as an "
    "attachment. Stories and essays run to approximately 3,000 words, and "
    "copyright returns to the original author upon publication.",
    "https://www.chollaneedles.com/p/submissions.html",
    "https://www.chollaneedles.com/p/submissions.html", "editor@chollaneedles.com",
    "Email — poems in the body or attached",
    src("Cholla Needles — Submissions (official)",
        "https://www.chollaneedles.com/p/submissions.html"),
    intl(),
    ["poetry", "fiction", "essays"], "Poetry, stories and essays",
    pay(None, None, None, "Two copies of the printed magazine, to US authors",
        "Official submissions page: payment is two copies of the printed magazine to US "
        "authors. BRYME records no currency amount because the magazine states its "
        "compensation in copies, not money. Authors outside the US are not covered by the "
        "stated payment terms.",
        "Not publicly stated"),
    {"min": None, "max": 3000,
     "display": "Stories and essays approx 3,000 words; 6–12 poems; online essays any length"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Six to twelve original poems.",
     "Stories and essays of approximately 3,000 words.",
     "Online essays, which can be any length."],
    ["Fewer than six or more than twelve poems.",
     "Previously published work presented as original."],
    ["Email editor@chollaneedles.com with six to twelve original poems.",
     "Poems may go in the body of the email or be attached.",
     "Keep stories and essays to roughly 3,000 words."],
    "Copyright returns to the original author upon publication.",
    ["Read https://www.chollaneedles.com/p/submissions.html before sending.",
     "The six-to-twelve poem range is a requirement, not a suggestion.",
     "Payment is in copies and is specified for US authors."],
    ["cholla needles", "poetry", "stories", "essays", "two copies", "6-12 poems",
     "3000 words", "copyright returns"]))

# ------------------------------------------- 4 Lowestoft Chronicle
NEW.append(rec(
    "lowestoft-chronicle", "Lowestoft Chronicle", "Fiction, creative nonfiction and poetry",
    "Lowestoft Chronicle: unpaid, 3,000 words, rights revert after 30 days",
    "Lowestoft Chronicle states plainly that it cannot pay contributors at "
    "present. It takes fiction of any genre up to 3,000 words, warns that "
    "submissions under 100 words are likely too slight unless they are poetry, "
    "and assumes first publication rights for 30 days before all rights revert. "
    "Allow 30 days for a reply.",
    "https://lowestoftchronicle.com/submissions/",
    "https://lowestoftchronicle.com/submissions/", None,
    "Email — plain text in the body, or attached",
    src("Lowestoft Chronicle — Submissions (official)",
        "https://lowestoftchronicle.com/submissions/"),
    intl(),
    ["fiction", "creative-nonfiction", "poetry"], "Fiction, creative nonfiction and poetry",
    pay(None, None, None, "Unpaid — the journal states it cannot provide payment at present",
        "Official submissions page: Lowestoft Chronicle states that at present it cannot "
        "provide payment to contributors, giving an elaborate and humorous reason involving its "
        "bank manager claiming dibs on all profits. BRYME records no figure because there is "
        "none.",
        "Not applicable — unpaid"),
    {"min": None, "max": 3000,
     "display": "Fiction of any genre up to 3,000 words; under 100 words likely too slight "
                "unless poetry"},
    {"label": "Allow 30 days for a reply", "band": "2-4-weeks", "official": True},
    "open", None, "not-stated",
    ["Fiction of any genre, up to 3,000 words.",
     "Creative nonfiction.",
     "Poetry in all forms — but only one or two of your very best poems per reading period.",
     "Work that is not too slight. Under 100 words will likely be rejected unless it is poetry."],
    ["Submissions under 100 words that are not poetry — likely rejected as too slight.",
     "More than one or two poems per reading period.",
     "Work generated by AI is not addressed: the submissions page states no AI policy at all, "
     "so nothing is promised either way."],
    ["Email your work as plain text in the body of an email, or as an attachment.",
     "Include your name, your pseudonym if you use one, the title of your work, and a brief "
     "bio.",
     "Keep fiction to 3,000 words.",
     "Allow 30 days for a reply."],
    "Upon acceptance, Lowestoft Chronicle assumes first publication rights for 30 days from "
    "publication, after which all rights revert back to the author.",
    ["Read https://lowestoftchronicle.com/submissions/ before sending.",
     "Send plain text in the email body if you can — it is the first option offered.",
     "Unpaid; submit for the publication and the 30-day reversion."],
    ["lowestoft chronicle", "fiction", "creative nonfiction", "poetry", "unpaid",
     "3000 words", "first publication rights 30 days", "100 words minimum"]))

# ------------------------------------------- 5 Blank Spaces
NEW.append(rec(
    "blank-spaces", "Blank Spaces", "Flash fiction and longer fiction",
    "Blank Spaces: flash under 1,000 words, fiction features to 3,500",
    "Blank Spaces takes flash fiction of any topic and genre under 1,000 words, "
    "and fiction features up to 3,500 words. Submissions carry a fee of $6 for a "
    "fiction feature or $3 for everything else outside free submission months, "
    "and are not opened until payment clears. It publishes no contributor rate; "
    "contributors are instead invited to buy print copies at a discount.",
    "https://www.blankspaces.ca/submit",
    "https://www.blankspaces.ca/submit", None, "Submittable-style portal",
    src("Blank Spaces — Submit (official)", "https://www.blankspaces.ca/submit"),
    intl(),
    ["fiction"], "Flash fiction and longer fiction",
    pay(None, None, None, "No contributor rate published; submissions carry a fee",
        "The official submit page states no payment to contributors. The money runs the other "
        "way: $6 for a fiction feature or $3 for everything else, charged outside free "
        "submission months, and submissions are not opened until payment has cleared. "
        "Contributors are invited to purchase print copies at a discounted rate. BRYME records "
        "no contributor amount because none is published, and does not record the fee as "
        "payment.",
        "Not applicable — no published contributor rate"),
    {"min": None, "max": 3500,
     "display": "Flash fiction under 1,000 words; fiction features up to 3,500 words"},
    {"label": "Not stated; you will hear back only if they publish your piece",
     "band": "not-stated", "official": True},
    "open", None, "not-stated",
    ["Flash fiction — any topic, any genre, under 1,000 words.",
     "Fiction features — longer fiction, any topic, any genre, up to 3,500 words.",
     "Multiple submissions, each in its own separate submission package."],
    ["Expecting a rejection notice. Blank Spaces says it will contact you if it decides to "
     "publish your piece, and asks you not to email asking whether your submission has been "
     "read or accepted.",
     "Combining multiple submissions into one package — each is charged separately."],
    ["Choose the right tier: under 1,000 words is flash fiction, up to 3,500 is a fiction "
     "feature.",
     "Pay the submission fee unless a free submission month is running — $6 for a fiction "
     "feature, $3 for everything else.",
     "Do not pay until you are ready to send; submissions are not opened until payment clears.",
     "Send multiple submissions in separate packages."],
    "Not stated on the official submit page.",
    ["Read https://www.blankspaces.ca/submit before sending.",
     "The fee is to submit, not a charge against payment — there is no published contributor "
     "rate.",
     "Do not email about status; only accepted writers are contacted."],
    ["blank spaces", "flash fiction", "fiction feature", "1000 words", "3500 words",
     "submission fee", "no contributor rate"]))

# ------------------------------------------- 6 Milk Press
NEW.append(rec(
    "milk-press", "Milk Press", "Poetry and hybrid work",
    "Milk Press: no AI-derived work either, rights revert on publication",
    "Milk Press, run by the Poetry Society of New York, will not consider "
    "AI-generated work, or work that has been derived from or partially composed "
    "by AI. All submissions go through the Society's Submittable page with a $5 "
    "reading fee that funds its free and accessible programmes. On publication, "
    "all rights revert to the contributor.",
    "https://poetrysocietyny.org/milk-press-guidelines",
    "https://poetrysocietyny.org/milk-press-guidelines", None,
    "Submittable — $5 reading fee",
    src("Milk Press — Guidelines (official)",
        "https://poetrysocietyny.org/milk-press-guidelines"),
    intl(),
    ["poetry"], "Poetry and hybrid work",
    pay(None, None, None, "No contributor rate published; $5 reading fee applies",
        "The guidelines publish no payment rate. The $5 reading fee is charged to submitters "
        "and is put towards the free and accessible programmes the Poetry Society of New York "
        "offers. BRYME records no contributor amount because none is published.",
        "Not applicable — no published contributor rate"),
    {"min": None, "max": None, "display": "No length limit stated on the guidelines page"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Poetry and hybrid work.",
     "Work composed entirely by a human — the only kind considered."],
    ["AI-generated work.",
     "Work derived from, or partially composed by, AI. The ban reaches past drafting into "
     "derivation and partial composition."],
    ["Submit through the Poetry Society of New York's Submittable page.",
     "Pay the $5 reading fee, which funds the Society's free programmes.",
     "Ensure nothing in your work was derived from or partially composed by AI."],
    "Upon publication, all rights revert back to the contributor.",
    ["Read https://poetrysocietyny.org/milk-press-guidelines before sending.",
     "The AI ban covers derivation and partial composition, not just drafting — that is broader "
     "than most.",
     "Rights revert on publication."],
    ["milk press", "poetry society of new york", "poetry", "hybrid", "$5 reading fee",
     "submittable", "rights revert", "no ai derived"]))

# ------------------------------------------- 7 Literary Veganism
NEW.append(rec(
    "literary-veganism", "Literary Veganism: An Online Journal",
    "Poetry, fiction and creative nonfiction",
    "Literary Veganism: pitch first, prose preferably well under 3,000 words",
    "Literary Veganism is an online journal looking for original, not "
    "AI-generated poetry, fiction and perhaps creative nonfiction. It prefers "
    "shorter prose of no more than 3,000 words and much less where possible, "
    "since that is easier to read online. It asks writers to make contact first: "
    "unsolicited attachments are never opened and suspicious emails are deleted.",
    "https://www.litvegan.net/p/submissions.html",
    "https://www.litvegan.net/p/submissions.html", None,
    "Pitch by email first — no unsolicited attachments",
    src("Literary Veganism — Submissions (official)",
        "https://www.litvegan.net/p/submissions.html"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, fiction and creative nonfiction",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out the pitch-first route, the prose length "
        "preference and the AI position but publishes no payment rate, so BRYME records no "
        "figure.",
        "Not publicly stated"),
    {"min": None, "max": 3000,
     "display": "Prose preferably shorter, no more than 3,000 words and much less if possible"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Original poetry, fiction and perhaps creative nonfiction.",
     "Shorter prose — no more than 3,000 words, and much less if possible, since it is easier "
     "for online reading.",
     "Work with a vegan or animal-ethics thread, which is the journal's subject."],
    ["AI-generated work.",
     "Unsolicited attachments — they are never opened and are automatically deleted.",
     "Suspicious emails, which are deleted."],
    ["Write first and pitch. The journal prefers to hear from you before you send anything.",
     "Do not attach unsolicited files.",
     "Put Lit Vegan in the subject line.",
     "Keep prose well under 3,000 words if you can."],
    "Not stated on the public submissions page; the journal raises copyright only to say it "
    "will address any question about it.",
    ["Read https://www.litvegan.net/p/submissions.html before sending.",
     "Pitch first — attaching a manuscript cold will get it deleted unread.",
     "Shorter prose is explicitly preferred over longer."],
    ["literary veganism", "lit vegan", "poetry", "fiction", "creative nonfiction",
     "3000 words", "pitch first", "no ai", "vegan"]))

# ------------------------------------------- 8 Poetry South
NEW.append(rec(
    "poetry-south", "Poetry South", "Poetry",
    "Poetry South: no AI-assisted poetry, Southern writers given priority",
    "Poetry South, published at Mississippi University for Women, does not "
    "consider AI-generated or AI-assisted poetry as the writer's original work. "
    "It pays particular attention to writers from the South — born, raised or "
    "living there — while holding that all poetry within its covers has a claim "
    "to the South because it is published there. Submissions go through "
    "Submittable.",
    "https://www.muw.edu/poetrysouth/submit/",
    "https://www.muw.edu/poetrysouth/submit/", "poetrysouth01@gmail.com",
    "Submittable — email for queries only",
    src("Poetry South — Submit (official)", "https://www.muw.edu/poetrysouth/submit/"),
    {"summary": "Open to all poets, with stated priority for writers from the South. Poetry "
                "South says it pays particular attention to writers from the South — born, "
                "raised, or living there — while holding that all poetry within its covers has "
                "a claim to the South because it is published there. BRYME records this as an "
                "editorial emphasis rather than a restriction, because the magazine does not "
                "exclude writers from elsewhere.",
     "mode": "not-stated", "includesRegions": ["the American South"],
     "allowsDiaspora": True, "notStated": True},
    ["poetry"], "Poetry",
    pay(None, None, None, "Not stated on the public submit page",
        "The public submit page sets out the submission route, the AI position and the "
        "editorial emphasis on Southern writers but publishes no payment rate, so BRYME records "
        "no figure.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Submit a file of poems; individual poems can be withdrawn via a Submittable "
                "message"},
    {"label": "Not stated; longer if submitted after the issue deadline", "band": "not-stated",
     "official": True},
    "open",
    {"date": None,
     "display": "Submissions made after the stated date are considered for the following "
                "year's issue, though response times may be longer.",
     "recurring": True},
    "prohibited",
    ["Poetry. The magazine pays particular attention to writers from the South — born, raised "
     "or living there."],
    ["AI-generated or AI-assisted poetry. Neither is considered the writer's original work.",
     "Resubmitting to the current issue after a decline, or while your submission is still "
     "unread."],
    ["Submit through Submittable.",
     "Send a file of poems — the page describes withdrawing one or two poems from a file of "
     "four via a Submittable message.",
     "Email poetrysouth01@gmail.com for queries only.",
     "If you must withdraw, you may resubmit new poems, but not to the current issue."],
    "Not stated on the public submit page.",
    ["Read https://www.muw.edu/poetrysouth/submit/ before sending.",
     "AI assistance disqualifies work as original here, not just AI drafting.",
     "Being from the South helps but is not required."],
    ["poetry south", "mississippi university for women", "poetry", "southern writers",
     "submittable", "no ai-assisted"]))


BASE = {
    "river-teeth": ("", "International"),
    "the-baltimore-review": ("", "International"),
    "cholla-needles": ("", "International"),
    "lowestoft-chronicle": ("", "International"),
    "blank-spaces": ("", "International"),
    "milk-press": ("", "International"),
    "literary-veganism": ("", "International"),
    "poetry-south": ("", "International"),
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
# 371 usable guidelines pages remain unread. No further crawling required.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
