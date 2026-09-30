#!/usr/bin/env python3
"""Add verified writing-market batch 12 (2026-09-30).

Six NEW markets read from the batch-4 backlog. No crawling.
Every figure read off the publication's own page on 2026-09-30.

StoryQuarterly's page carries a $500 figure. That is a contest prize for the
winner, first runner-up and second runner-up of a competition - not the rate
paid for published work. Per the precedent set by American Short Fiction,
Dogwood and The Nulla, it is recorded as context only, never as the market
rate. The $25 honorarium is the rate.

Jabberwock Review's $3 is charged to the writer and is not recorded as payment.

Two markets offer a choice rather than a sum, and both are recorded as such:
  farmer-ish      $25 honorarium OR a copy of the book
  pinhole-poetry  $5 CAD honorarium, which contributors may reinvest
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

# ------------------------------------------- 1 Farmer-ish
NEW.append(rec(
    "farmer-ish", "Farmer-ish", "Essays about farming, food and land",
    "Farmer-ish: $25 or a copy, copyright stays yours",
    "Farmer-ish offers a $25 honorarium or a copy of the book for its print "
    "annuals. General and how-to essays run to approximately 800 to 1,200 words. "
    "It does not accept work written in part by generative AI or edited heavily "
    "by AI, and authors retain copyright throughout.",
    "https://farmerish.net/submissions/",
    "https://farmerish.net/submissions/", None,
    "Email — work copied into the body",
    src("Farmer-ish — Submissions (official)", "https://farmerish.net/submissions/"),
    intl(),
    ["essays", "creative-nonfiction"], "Essays about farming, food and land",
    pay("USD", 25, 25, "$25 honorarium or a copy of the book",
        "Official submissions page: for its print annuals, Farmer-ish offers a $25 honorarium or "
        "a copy of the book. Contributors choose. BRYME records the cash figure and notes the "
        "alternative rather than assuming one.",
        "Not publicly stated"),
    {"min": 800, "max": 1200,
     "display": "General essays and how-to essays, approximately 800 to 1,200 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["General essays and how-to essays of roughly 800 to 1,200 words.",
     "Writing about farming, food and land — the magazine's subject."],
    ["Submissions written in part by generative AI.",
     "Submissions edited heavily by AI. Light editing assistance is not the same as heavy "
     "editing, but the line is the editor's to draw."],
    ["Send submissions by email.",
     "Copy your submission into the body of the email rather than attaching it.",
     "Keep essays to about 800 to 1,200 words."],
    "Authors retain copyright of their work.",
    ["Read https://farmerish.net/submissions/ before sending.",
     "Paste into the email body — do not attach.",
     "You can take $25 or a copy; say which you want."],
    ["farmer-ish", "farming", "food", "essays", "$25 honorarium", "800-1200 words",
     "copyright retained", "no generative ai"]))

# ------------------------------------------- 2 StoryQuarterly
NEW.append(rec(
    "story-quarterly", "StoryQuarterly",
    "Literary fiction and creative nonfiction",
    "StoryQuarterly: $25 honorarium, fiction up to 6,250 words",
    "StoryQuarterly, published at Rutgers University–Camden, offers a small "
    "honorarium of $25 and is interested in previously unpublished literary "
    "fiction — short stories, short shorts and novel excerpts up to 6,250 words "
    "— along with creative nonfiction. All work goes through Submittable.",
    "https://storyquarterly.camden.rutgers.edu/submissions",
    "https://storyquarterly.camden.rutgers.edu/submissions", None,
    "Submittable only",
    src("StoryQuarterly — Submissions (official)",
        "https://storyquarterly.camden.rutgers.edu/submissions"),
    intl(),
    ["fiction", "creative-nonfiction"], "Literary fiction and creative nonfiction",
    pay("USD", 25, 25, "$25 honorarium",
        "Official submissions page: StoryQuarterly offers a small honorarium of $25. The page "
        "also lists a $500 prize for the winner of a competition, with the winner, first "
        "runner-up and second runner-up published in the issue. That is a contest prize, not "
        "the rate paid for published work, so BRYME records the $25 as the market rate and "
        "notes the prize separately.",
        "Not publicly stated"),
    {"min": None, "max": 6250,
     "display": "Short stories, short shorts and novel excerpts up to 6,250 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Previously unpublished literary fiction — short stories, short shorts and novel excerpts "
     "up to 6,250 words.",
     "Creative nonfiction."],
    ["Previously published fiction.",
     "Fiction over 6,250 words."],
    ["Submit all work electronically through Submittable.",
     "Check the Submittable page for the current open or closed status before sending.",
     "Send previously unpublished work only."],
    "Not stated on the public submissions page.",
    ["Read https://storyquarterly.camden.rutgers.edu/submissions before sending.",
     "Submittable is the only route, and it also carries the open/closed status.",
     "The $500 on the page is a competition prize, not the standard rate."],
    ["storyquarterly", "rutgers camden", "literary fiction", "creative nonfiction",
     "$25 honorarium", "6250 words", "submittable"]))

# ------------------------------------------- 3 Pinhole Poetry
NEW.append(rec(
    "pinhole-poetry", "Pinhole Poetry", "Poetry and pinhole photography",
    "Pinhole Poetry: $5 CAD honorarium, 4–6 week response",
    "Pinhole Poetry pays each contributor a $5 CAD honorarium, and welcomes "
    "contributors who would rather reinvest it into the upkeep of its website "
    "and development projects. It asks that no work created with AI be sent, "
    "tries to respond within four to six weeks, and wants a short bio in the "
    "body of your email.",
    "https://pinholepoetry.ca/poetry-pinhole-photography-guidelines/",
    "https://pinholepoetry.ca/poetry-pinhole-photography-guidelines/", None,
    "Email — bio in the body",
    src("Pinhole Poetry — Guidelines (official)",
        "https://pinholepoetry.ca/poetry-pinhole-photography-guidelines/"),
    intl(),
    ["poetry"], "Poetry and pinhole photography",
    pay("CAD", 5, 5, "$5 CAD honorarium per contributor",
        "Official guidelines: Pinhole Poetry pays an honorarium of $5 CAD to each contributor, "
        "and says it is happy for contributors to reinvest that back into the upkeep of its "
        "website and development projects if they so desire. The choice is the contributor's; "
        "BRYME records the stated figure.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No length limit stated on the guidelines page; photography in jpeg only"},
    {"label": "Four to six weeks", "band": "2-4-weeks", "official": True},
    "open", None, "prohibited",
    ["Poetry.",
     "Pinhole photography, in jpeg format, for which you hold copyright.",
     "Reader responses to recently published poetry chapbooks — excluding Pinhole's own "
     "titles."],
    ["Work created with AI.",
     "Photography in any format other than jpeg.",
     "Work for which you do not hold copyright."],
    ["Send work by email with a short bio in the body, plus any social media accounts or "
     "personal websites you want shared.",
     "Send photography as jpeg only.",
     "Note any special formatting requirements in your submission email.",
     "Expect a response in four to six weeks."],
    "Send only work for which you hold copyright.",
    ["Read https://pinholepoetry.ca/poetry-pinhole-photography-guidelines/ before sending.",
     "Four to six weeks is one of the faster stated responses in this directory.",
     "You can decline the $5 CAD and reinvest it if you prefer."],
    ["pinhole poetry", "poetry", "pinhole photography", "$5 cad", "honorarium", "4-6 weeks",
     "jpeg", "no ai"]))

# ------------------------------------------- 4 Spellbinder Magazine
NEW.append(rec(
    "spellbinder-magazine", "Spellbinder Magazine", "Short fiction",
    "Spellbinder Magazine: first rights only, up to 3,000 words",
    "Spellbinder Magazine takes short stories of up to 3,000 words and acquires "
    "first publication rights only, with all rights reverting to the author "
    "after publication. It does not accept AI-generated or AI-assisted creative "
    "work, asks for one submission per reading period, and aims to respond "
    "within six weeks of the submission window closing.",
    "https://www.spellbindermag.com/submission-guidelines/",
    "https://www.spellbindermag.com/submission-guidelines/", None,
    "Online submission form — contact page for alternatives",
    src("Spellbinder Magazine — Submission Guidelines (official)",
        "https://www.spellbindermag.com/submission-guidelines/"),
    intl(),
    ["fiction"], "Short fiction",
    pay(None, None, None, "Not stated on the public guidelines page",
        "The public guidelines set out length limits, the rights position and the response time "
        "but publish no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": 3000, "display": "Short stories of up to 3,000 words"},
    {"label": "Within six weeks of the submission window closing", "band": "2-4-weeks",
     "official": True},
    "open", None, "prohibited",
    ["Short stories of up to 3,000 words.",
     "One submission per reading period."],
    ["AI-generated creative work.",
     "AI-assisted creative work. Assistance disqualifies the work, not just generation.",
     "More than one submission per reading period."],
    ["Read the guidelines first, then submit through the submission form.",
     "Keep stories to 3,000 words.",
     "Send one submission per reading period.",
     "If the form does not work for you, get in touch through the contact page and the "
     "magazine will arrange another way to send your work."],
    "Spellbinder acquires first publication rights only. All rights revert to the author after "
    "publication.",
    ["Read https://www.spellbindermag.com/submission-guidelines/ before sending.",
     "The six-week clock starts when the window closes, not when you submit.",
     "There is an accessibility route via the contact page if the form fails you."],
    ["spellbinder magazine", "short fiction", "3000 words", "first publication rights",
     "rights revert", "no ai-assisted", "six weeks"]))

# ------------------------------------------- 5 Decolonial Passage
NEW.append(rec(
    "decolonial-passage", "Decolonial Passage Literary Magazine",
    "Poetry, fiction and creative nonfiction",
    "Decolonial Passage: no AI processes, but spellcheckers are fine",
    "Decolonial Passage describes itself as a platform for human creative works "
    "and does not accept submissions containing AI processes — while stating "
    "plainly that spellcheckers and grammar tools are not AI. Publishing rights "
    "revert to the author upon initial publication, and the goal is a response "
    "within three to four months.",
    "https://thedecolonialpassage.net/submit-2/",
    "https://thedecolonialpassage.net/submit-2/", None, "See guidelines",
    src("Decolonial Passage — Submit (official)",
        "https://thedecolonialpassage.net/submit-2/"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, fiction and creative nonfiction",
    pay(None, None, None, "Not stated on the public submit page",
        "The public submit page sets out the AI position, the rights position and the response "
        "goal but publishes no payment rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "No length limit stated on the public submit page"},
    {"label": "Goal of three to four months", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Human creative work — poetry, fiction and creative nonfiction.",
     "Work that identifies and acknowledges any third-party material it contains."],
    ["Submissions containing AI processes. The magazine positions itself as a platform for "
     "human creative works.",
     "Third-party material that is not clearly identified and acknowledged in the text."],
    ["Check the submit page for the current route before sending.",
     "Identify and acknowledge any third-party material inside your submission.",
     "Spellcheckers and grammar tools are permitted — the magazine says explicitly they are "
     "not AI.",
     "Allow three to four months."],
    "Publishing rights revert to the author upon initial publication in the Decolonial Passage "
    "magazine.",
    ["Read https://thedecolonialpassage.net/submit-2/ before sending.",
     "Using a spellchecker does not breach this policy — the magazine says so.",
     "Rights revert on first publication."],
    ["decolonial passage", "poetry", "fiction", "creative nonfiction", "no ai processes",
     "spellcheckers allowed", "rights revert", "3-4 months"]))

# ------------------------------------------- 6 Jabberwock Review
NEW.append(rec(
    "jabberwock-review", "Jabberwock Review", "Fiction, poetry and creative nonfiction",
    "Jabberwock Review: rights revert, three-month response, Submittable only",
    "Jabberwock Review charges a small $3 submission fee, citing publication "
    "costs. Rights revert to the author upon publication, with a request to "
    "acknowledge the review in any future publications. It does not accept "
    "emailed submissions and tries to respond within three months.",
    "https://www.jabberwockreview.org/submit",
    "https://www.jabberwockreview.org/submit", None,
    "Submittable only — no emailed submissions",
    src("Jabberwock Review — Submit (official)",
        "https://www.jabberwockreview.org/submit"),
    intl(),
    ["fiction", "poetry", "creative-nonfiction"],
    "Fiction, poetry and creative nonfiction",
    pay(None, None, None, "No contributor rate published; $3 submission fee applies",
        "The public submit page publishes no payment to contributors. The $3.00 is a submission "
        "fee charged to the writer, which the review attributes to publication costs. BRYME "
        "records no contributor amount because none is published, and does not record the fee "
        "as payment.",
        "Not applicable — no published contributor rate"),
    {"min": None, "max": None, "display": "No length limit stated on the public submit page"},
    {"label": "Three months", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Fiction, poetry and creative nonfiction."],
    ["Emailed submissions — they are not accepted.",
     "Sending another submission before you have received a response on the first."],
    ["Submit through the Submission Manager on Submittable.",
     "Do not email work.",
     "Wait for a response before sending anything else.",
     "Pay the $3 submission fee."],
    "Rights revert to the author upon publication, but the review asks that it be acknowledged "
    "in any future publications of the work.",
    ["Read https://www.jabberwockreview.org/submit before sending.",
     "One submission at a time, and wait for the response.",
     "The $3 is to submit, not a charge against payment — there is no published contributor "
     "rate."],
    ["jabberwock review", "fiction", "poetry", "creative nonfiction", "$3 fee", "submittable",
     "rights revert", "three months"]))


BASE = {
    "farmer-ish": ("", "International"),
    "story-quarterly": ("", "International"),
    "pinhole-poetry": ("", "International"),
    "spellbinder-magazine": ("", "International"),
    "decolonial-passage": ("", "International"),
    "jabberwock-review": ("", "International"),
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
# 365 usable guidelines pages remain unread. No further crawling required.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
