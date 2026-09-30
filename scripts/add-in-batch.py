#!/usr/bin/env python3
"""Add the verified India batch (Phase 19 Wave 1), 2026-09-30.

Verification standard, same as the US/UK/CA/AU batches: every figure below was
read off the publication's OWN live guidelines or pitch page on 2026-09-30.
Nothing is copied from a third-party "paying markets" list.

That standard earned its keep on this batch. The Bombay Literary Magazine is
already in the catalogue with ₹5,000, sourced from its old domain
(bombayliterarymagazine.com). The publication's current official page
(bombaylitmag.com/submit) states INR 10,000, and every third-party list still
quotes the old figure - so reading the source doubled a rate the desk had been
publishing as current. The correction is applied here as well as the additions.

Honest scope note: India's literary magazine ecosystem is largely unpaid. Of the
India-based magazines surveyed, most state no compensation at all, and several
charge reading fees. The paying capacity sits in the digital newsrooms. So this
batch is deliberately split - one paying literary market, one paying literary
market with conditional pay, and three newsrooms that state they pay but do not
publish a figure. Where a publication does not state a rate, the record says so
rather than guessing.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-30"
UA = "https://bombaylitmag.com/submit/"


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


NB = pay(None, None, None,
         "Not publicly stated on the official submission page",
         "The official page sets out eligibility, genres, word counts, rights and response times, but states no fee. BRYME records that as unstated rather than guessing. Assume unpaid unless you confirm otherwise with the editor.",
         "Not publicly stated")

NEW = []

# ------------------------------------------------------------- 1 Wire Science
NEW.append(rec(
    "wire-science", "The Wire Science",
    "Science journalism, cited and under 1,100 words",
    "The Wire Science submissions: paid per piece, 1,000 words, cite everything",
    "The Wire Science, the science desk of India's The Wire, pays per piece rather than per word and publishes its full 18-point house style publicly. Hard cap 1,100 words, every claim hyperlinked to a primary source, and a stated preference for quoting scientists working outside the West. The rate is not published.",
    "https://science.thewire.in/science/our-submission-guidelines/",
    "mailto:mukunth@thewire.in", "mukunth@thewire.in",
    "Email the science editor; pitches discussed case by case",
    src("The Wire Science - Submission Guidelines (official)",
        "https://science.thewire.in/science/our-submission-guidelines/"),
    {"summary": "The guidelines state no geographic restriction on who may write for the desk. India-based.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": None, "notStated": True},
    ["journalism", "analysis", "articles", "reviews"],
    "Reported science and environment pieces, analysis, reviews",
    pay(None, None, None,
        "Paid per piece - figure not published",
        "Official, verbatim: \u201cWe don\u2019t pay per word. We pay per piece, with each piece valued according to usefulness, length, amount of work required to produce it, newsiness and quality of writing.\u201d The page tells writers to contact the editor for the figure. Because no number is published, BRYME states none.",
        "Not stated"),
    {"min": None, "max": 1100, "display": "Up to 1,000 words; hard cap 1,100"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Science, health, environment, technology and education stories with a real reporting base.",
     "Pieces built from primary sources - papers, filings, datasets - not from other coverage.",
     "Independent experts, and explicit encouragement to quote scientists working outside the West and women scientists.",
     "Descriptive writing that shows rather than announces its structure.",
     "Conflict-of-interest disclosure where you have any link to the work you are writing about."],
    ["Plagiarism - warned once, banned on the second offence, and self-plagiarism is treated as plagiarism too.",
     "Citations in footnotes. They want hyperlinks inline instead.",
     "Papers in predatory journals or unreliable preprint servers.",
     "Charts without the underlying data in a separate spreadsheet.",
     "Pieces over 1,100 words without clearing it with the editor first."],
    ["Average sentence length of 18 words or fewer.",
     "A .doc or .docx file; a PDF may accompany it, not replace it.",
     "Every source cited as an inline hyperlink.",
     "Charts supplied with their data in a separate spreadsheet and the source named.",
     "Suggested images under Creative Commons Attribution or Zero, with the uploader's username and licence version.",
     "A conflict-of-interest disclosure where relevant."],
    "Not stated on the guidelines page. Ask the editor before you write.",
    ["Pitch the idea first: the desk discusses story ideas case by case, and points 4, 5, 7, 12 and 15 of the guidelines apply to pitches as well.",
     "Write to the science editor, Vasudevan Mukunth.",
     "Send the piece as .doc or .docx with sources hyperlinked inline.",
     "Check the average sentence length with their suggested tool before sending - it is an explicit house rule."],
    ["the wire science", "science journalism india", "paid science writing", "india",
     "health reporting", "environment reporting", "pitched science writing"]))

# --------------------------------------------------------------- 2 ThePrint
NEW.append(rec(
    "theprint", "ThePrint",
    "News, opinion and ground reportage from an Indian newsroom",
    "ThePrint freelance pitches: ideas@theprint.in, paid on publication",
    "ThePrint, the Indian news platform founded by Shekhar Gupta, takes freelance story ideas at a dedicated address and states plainly that it pays for commissioned work. It does not publish a rate card, so BRYME states none. Strongest fit for India-context politics, policy, defence, economy and ground reporting.",
    "https://theprint.in/about-us/",
    "mailto:ideas@theprint.in", "ideas@theprint.in",
    "Email a story idea; clear the pitch before writing",
    src("ThePrint - About Us (official, freelancer paragraph)",
        "https://theprint.in/about-us/"),
    {"summary": "The page states no geographic restriction. India-based newsroom writing for an Indian readership.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": None, "notStated": True},
    ["journalism", "opinion", "analysis", "articles"],
    "News, opinion, ground reports, policy and defence analysis",
    pay(None, None, None,
        "Paid for commissioned work - figure not published",
        "Official, verbatim: \u201cWe\u2019d prefer that you send us contributions after clearing the pitches with us. We pay fairly and on time for contributions we commission and publish.\u201d That is a stated commitment to pay, with no figure attached. BRYME does not invent one.",
        "Not stated"),
    {"min": None, "max": None, "display": "Not publicly stated"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["India-context politics, policy, governance, defence, diplomacy and the economy.",
     "Ground reporting from a specific place - the desk's stated strength.",
     "Opinion with a clear argument, for the National Interest and PoV sections.",
     "Pitches cleared with the desk before the piece is written."],
    ["The page does not set out a public list of exclusions. Read the published sections before pitching - the desk is explicitly non-doctrinaire, and says it is neither doctrinaire Left nor Right.",
     "No rate is published, so do not treat a pitch as a commission."],
    ["A story idea emailed to the freelance address.",
     "Pitch first; the desk asks that contributions be sent after the idea is cleared.",
     "Familiarity with the relevant section, since pitches are routed by section."],
    "Not stated on the page. Commissioning terms are agreed with the desk.",
    ["Email the story idea to the freelance address given on the About page.",
     "Wait for the desk to clear the pitch before writing the piece.",
     "Follow the house sections - politics, ground reports, opinion, defence, diplomacy, economy, health, science and tech."],
    ["theprint", "india news freelance", "indian newsroom pitch", "paid journalism india",
     "policy writing india", "ground reporting", "opinion pitch india"]))

# ------------------------------------------------------------- 3 The Caravan
NEW.append(rec(
    "the-caravan", "The Caravan",
    "Long-form narrative journalism - pitch in 400 words",
    "The Caravan pitches: 400-word pitch, long-form narrative journalism",
    "The Caravan, India's long-form narrative journalism magazine, takes story pitches of no more than 400 words alongside a résumé and publication list - and has closed its fiction and poetry desks entirely. No pay figure is published and the desk says it cannot reply to every pitch, so treat silence as silence.",
    "https://caravanmagazine.in/pages/submit-to-us",
    "mailto:editor.thecaravan@delhipress.in", "editor.thecaravan@delhipress.in",
    "Email a pitch of no more than 400 words, with a résumé and published-work list",
    src("The Caravan - Submit to Us (official)",
        "https://caravanmagazine.in/pages/submit-to-us"),
    {"summary": "The submission page states no geographic restriction. India-based, publishing on Indian politics and culture.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": None, "notStated": True},
    ["journalism", "reported-feature", "analysis"],
    "Long-form reportage, politics, culture and photo essays",
    NB, {"min": None, "max": None, "display": "Not publicly stated"},
    {"label": "The desk says it cannot respond to every pitch", "band": "not-stated", "official": True},
    "open", None, "not-stated",
    ["Long-form narrative journalism on Indian politics, culture and society.",
     "Photo essays that offer a narrative rather than straight news coverage.",
     "A familiarity with the archive and its approach, which the page asks for explicitly."],
    ["Fiction and poetry. The desk states it no longer accepts either.",
     "Pitches longer than 400 words.",
     "Zipped folders of high-resolution images with a photo-essay proposal.",
     "Photo essays of fewer than twenty images, or without the 200-300 word description."],
    ["A pitch of no more than 400 words.",
     "A résumé.",
     "A list of your published work.",
     "For photo essays: at least twenty images plus a 200-300 word description, all in one PDF."],
    "Not stated on the submission page.",
    ["Send the pitch, your résumé and your published-work list by email in one message.",
     "Keep the pitch inside the 400-word limit the page sets.",
     "Read the archive first - the page asks for it, and the desk commissions on fit with its established approach."],
    ["the caravan", "india longform", "narrative journalism india", "pitch india",
     "photo essay pitch", "delhi press", "indian magazine pitch"]))

# ------------------------------------------------------------ 4 Goya Journal
NEW.append(rec(
    "goya-journal", "The Goya Journal",
    "Food writing with a regional and cultural frame",
    "The Goya Journal pitches: food stories, 7-10 day reply, AI screened",
    "The Goya Journal publishes Indian food journalism - ingredient-led essays, home kitchens, food businesses and the places food meets politics or history. It states a 7-10 day response window and screens every draft for AI. It publishes no fee, so BRYME states none.",
    "https://www.goya.in/how-to-pitch",
    "mailto:hello@goyamedia.in", "hello@goyamedia.in",
    "Email a pitch with a headline, blurb and 1-2 paragraphs",
    src("The Goya Journal - Guidelines on sending a story pitch (official)",
        "https://www.goya.in/how-to-pitch"),
    {"summary": "The pitch page states no geographic restriction. India-based, and it says it values regional inflections of English - so writers outside the West are not a special case here.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": None, "notStated": True},
    ["articles", "essays", "personal-essays", "other"],
    "Food writing, essays, photo essays, recipes with a backstory",
    pay(None, None, None,
        "Not publicly stated on the official pitch page",
        "The pitch page is unusually detailed about what to send and how long a reply takes, but states no fee. Third-party write-ups describe Goya as paying; BRYME does not copy third-party descriptions, and records the official position as unstated.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Not publicly stated"},
    {"label": "7-10 days (their stated window)", "band": "under-2-weeks", "official": True},
    "open", None, "prohibited",
    ["Stories about people doing meaningful work in food - farmers, bakers, bartenders, home cooks, writers.",
     "Recipes with a compelling backstory, especially from lesser-known cuisines or communities.",
     "How people actually eat now: the shops, spice mixes and street carts that make up a real pantry.",
     "Ingredient-led essays, and stories where food meets politics, history, sociology, economics or environment.",
     "Photo essays, home-kitchen stories, and travel writing that reads culture through cuisine."],
    ["AI-generated editorial text. The page says every draft is screened, so a generated draft does not merely weaken a pitch - it fails the screen.",
     "Pitches without a clear headline.",
     "Pitches that leave out whether the piece is time-sensitive or whether you have photographs."],
    ["A clear headline, used as the email subject line.",
     "An intro or blurb.",
     "A 1-2 paragraph outline of the story.",
     "A note on whether the piece is time-sensitive.",
     "Confirmation of whether you have photographs.",
     "A note if you have video clips."],
    "Not stated on the pitch page.",
    ["Email the pitch to the address on the pitch page.",
     "Put the headline in the subject line.",
     "State whether it is time-sensitive and whether you have photographs.",
     "Expect a reply within 7-10 days."],
    ["goya journal", "india food writing", "food journalism pitch", "indian food essay",
     "recipe backstory", "food culture writing", "paid food writing india"]))

# ----------------------------------------------------------- 5 Mithila Review
NEW.append(rec(
    "mithila-review", "Mithila Review",
    "Speculative writing, with a stated commitment to Dalit, Bahujan and Adivasi voices",
    "Mithila Review: speculative non-fiction open, pay conditional on Patreon",
    "Mithila Review publishes speculative fiction, poetry and criticism from around the world and says explicitly that it wants voices from Dalit, Bahujan, Adivasi and other under-represented communities. Fiction and poetry are currently closed; non-fiction and pitches are open. Pay is conditional on the magazine's Patreon income and has not been restated since 2016, which BRYME records rather than smooths over.",
    "https://mithilareview.com/submission-guidelines/",
    "mailto:submissions@mithilareview.com", "submissions@mithilareview.com",
    "Non-fiction by email; fiction and poetry through the submission form when open",
    src("Mithila Review - Submission Guidelines (official)",
        "https://mithilareview.com/submission-guidelines/"),
    {"summary": "Open to writers from around the world. The magazine states it encourages first-time writers from anywhere, and says it is especially committed to publishing BIPOC creators, LGBTQIA+ writers, people with disabilities, and voices from Dalit, Bahujan, Adivasi and other subaltern communities.",
     "mode": "open", "includesRegions": [], "includesGroups": ["dalit", "bahujan", "adivasi", "bipoc", "lgbtqia", "disabled-writers"], "allowsDiaspora": True, "notStated": False},
    ["fiction", "poetry", "essays", "reviews", "interviews", "analysis"],
    "Speculative fiction, poetry, reviews, essays and criticism",
    pay("USD", 10, 50,
        "$10-$50, only when Patreon funds permit",
        "Official, verbatim: \u201cIf/when our Patreon funds permit, we pay $10 for original poetry, essays, flash stories (under 2500 words), and reprints and $10-$50 for original stories between 4000-8000 words or longer.\u201d That sentence is dated 24 October 2016 on the page and has not been restated since. The magazine also says it is underfunded and run by volunteers, and asks readers to donate so it can become a professional market. Treat any figure as conditional.",
        "Only stated as conditional on Patreon income; no schedule published"),
    {"min": None, "max": 8000, "display": "Stories up to 8,000 words; the $10 tier is under 2,500"},
    {"label": "2-8 weeks; average 2+ weeks (their figure)", "band": "2-4-weeks", "official": True},
    "open", None, "not-stated",
    ["Speculative work that explores politics, identity and culture - the guidelines ask for fiction that makes the reader feel and think.",
     "Stories and poetry from under-represented and marginalised writers, named explicitly in the guidelines.",
     "Non-fiction: reviews, essays, listicles, reaction pieces and critical articles about SFF media and pop culture that get little mainstream attention.",
     "First-time writers. The page says it happily encourages them, and asks you not to self-reject."],
    ["More than one story and three poems before you hear back. Pitches and non-fiction may be sent separately.",
     "Submissions outside the .doc or .docx formats the page names.",
     "Assuming fiction or poetry is open - both have been closed since 18 September 2021, and non-fiction is the live window."],
    ["One story, one non-fiction piece or pitch, and up to three poems, in a single document.",
     "Standard manuscript format, which the page strongly prefers and links a template for.",
     "A cover letter with a short background and your pronouns - preferred, not required.",
     "A note in the cover letter if the piece is simultaneously submitted, and immediate notice if it is accepted elsewhere."],
    "First world electronic rights, plus non-exclusive audio and anthology rights for the planned annual anthology.",
    ["Check the current status before sending: fiction and poetry are closed, non-fiction is open.",
     "For non-fiction, email the pitch with a detailed outline or a completed article.",
     "For fiction and poetry, use the submission form when the window reopens.",
     "Say in the cover letter if you are submitting elsewhere at the same time."],
    ["mithila review", "speculative fiction india", "dalit writers", "bahujan writers",
     "adivasi writers", "sff magazine submissions", "south asian speculative fiction"]))

# ------------------------------------------------------------------ main


def main():
    data = json.loads(OPPS.read_text(encoding="utf-8"))
    opps = data["opportunities"]
    existing = {o["slug"]: o for o in opps}

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

    # --- correction of an existing stale record ---------------------------
    # Verified against the publication's current official page on 2026-09-30.
    b = existing.get("bombay-literary-magazine")
    if b is None:
        sys.exit("ERROR: bombay-literary-magazine missing; correction cannot be applied")
    b["pay"] = pay("INR", 104, 104,
                   "\u20b910,000 (about $104)",
                   "Official, verbatim: \u201cWe offer an honorarium of INR 10,000 (ten thousand Indian rupees, approximately $104 USD, \u20ac90) per published contribution, contingent on such financial transfers being feasible.\u201d The old record carried \u20b95,000 from the magazine's previous domain; the current official page states \u20b910,000. Settled by PayPal or to an Indian bank account - the page warns that international bank transfers are not always feasible, so ask before you write.",
                   "After publication; contingent on a feasible transfer route")
    b["wordCount"] = {"min": 2000, "max": 5000,
                      "display": "2,000-5,000 words; or five poems"}
    b["aiPolicy"] = "prohibited"
    b["response"] = {"label": "Within six weeks (their figure)",
                     "band": "1-3-months", "official": True}
    b["lastVerified"] = V
    b["officialUrl"] = "https://bombaylitmag.com/submit/"
    b["applyUrl"] = "https://bombaylitmag.com/submit/"
    b["sources"] = src("The Bombay Literary Magazine - Sending Us Your Work (official)",
                       "https://bombaylitmag.com/submit/")
    b["rights"] = ("Minimum rights needed to publish: exclusive for one year, non-exclusive "
                   "thereafter. The magazine asks you to tell it if a further opportunity comes "
                   "up inside that year, and says it will try to cooperate.")
    b["eligibility"] = {
        "summary": "Open worldwide - the page states no nationality restriction, and English-language translations from other languages are welcome. India-based, publishing three times a year.",
        "mode": "open", "includesRegions": [], "allowsDiaspora": True, "notStated": False}
    b["excerpt"] = ("The Bombay Literary Magazine pays \u20b910,000 (about $104) per published "
                    "contribution - doubled from the \u20b95,000 the desk previously recorded - and "
                    "takes fiction, poetry, essays and translated fiction worldwide. Fiction and "
                    "poetry are currently capped and closed; essays, translated fiction and graphic "
                    "fiction are open. No AI-generated work.")
    b["howToSubmit"] = [
        "Check which categories are open first: the magazine closes each one when it reaches a cap of 400 submissions.",
        "Submit through the form on the page. Email submissions are not considered.",
        "Fiction and essays run 2,000-5,000 words; poetry is five poems in one document.",
        "Simultaneous submissions are allowed - tell them if the work is accepted elsewhere.",
    ]

    opps.extend(NEW)
    data["opportunities"] = opps
    data["updatedAt"] = V
    OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    pc = json.loads(PUBC.read_text(encoding="utf-8"))
    for r in NEW:
        pc[r["slug"]] = {"base": "IN", "label": "India"}
    PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Added {len(NEW)} India records and corrected 1 stale record. "
          f"Total opportunities: {len(opps)}")
    print("India-based markets now:", sum(1 for v in pc.values() if (v or {}).get("base") == "IN"))


if __name__ == "__main__":
    main()
