#!/usr/bin/env python3
"""Add three NEW verified writing markets found in batch 1 (2026-09-30).

Same standard as the AU/UK/CA/IN/US batches: every figure below was read off
the publication's own live guidelines page on 2026-09-30. Raw page text is
saved under research/batch1/*.txt in the working directory.

Three NEW records. Eight further outlets fetched in the same pass turned out to
be already in the database under different slugs (longreads, new-lines-magazine,
the-republic, himal-southasian, african-arguments, aurealis, brevity-essays,
hobart); their fresh 2026-09-30 verification goes into
reverify-batch1-2026-09-30.py instead. Nine more were fetched and NOT added
because the page did not support a record - reasons logged at the bottom.
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


NEW = []

# ------------------------------------------------------- The Elephant
NEW.append(rec(
    "the-elephant", "The Elephant", "Analysis, opinion, reflections and investigations",
    "The Elephant: features of 1,500–3,500 words, pitch under 500 words",
    "The Elephant, the Kenyan platform for politics, society and long-form analysis, takes "
    "pitches of no more than 500 words for features running between 1,500 and 3,500 words. "
    "Payment is discussed with each writer after a pitch is approved for commissioning rather "
    "than published as a rate card. Articles published in a month are paid within the first ten "
    "days of the following month.",
    "https://www.theelephant.info/write-for-us/",
    "mailto:info@theelephant.info", "info@theelephant.info",
    "Email pitch to the relevant section",
    src("The Elephant — Write for us (official)",
        "https://www.theelephant.info/write-for-us/"),
    {"summary": "No stated country restriction. The Elephant's coverage is centred on Kenya and "
                "the region, and the write-for-us page does not restrict who may pitch.",
     "mode": "not-stated", "includesRegions": ["kenya", "east-africa"],
     "allowsDiaspora": True, "notStated": True},
    ["analysis", "opinion", "essays", "journalism"],
    "Analysis, opinion, reflections and investigations",
    pay(None, None, None, "Discussed per commission — no published rate",
        "Official write-for-us page: payments discussion is done with each writer after a pitch "
        "has been approved for commissioning. There is therefore no public rate for BRYME to "
        "record. Agree the fee in writing before you file. Articles published in a given month "
        "are paid within the first ten days of the following month.",
        "Within the first ten days of the month following publication"),
    {"min": 1500, "max": 3500, "display": "Features run 1,500–3,500 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["A pitch of no more than 500 words, sent to the section that best suits it — Analysis, "
     "Opinion, Reflections or Investigations.",
     "Features between 1,500 and 3,500 words."],
    ["The write-for-us page does not publish a list of exclusions. Read the section you are "
     "pitching before you send, since the four sections have different registers."],
    ["Email info@theelephant.info with a pitch document of no more than 500 words.",
     "Address the pitch to the section of The Elephant that best suits it.",
     "Agree the payment with your editor after the pitch is approved for commissioning, before "
     "you file.",
     "Expect payment within the first ten days of the month after publication."],
    "Not stated on the official write-for-us page.",
    ["Read https://www.theelephant.info/write-for-us/ and pick the right section.",
     "Keep the pitch document under 500 words.",
     "Get the fee agreed before you write the piece."],
    ["the elephant", "kenya", "east africa", "analysis", "opinion", "investigations", "pitch"]))

# ------------------------------------------------------- Africa Is a Country
NEW.append(rec(
    "africa-is-a-country", "Africa Is a Country", "Commentary, criticism and reviews on Africa and its diaspora",
    "Africa Is a Country: 700–800 words, no pay for unsolicited posts",
    "Africa Is a Country usually takes posts of 700 to 800 words, occasionally up to 900 or a "
    "little more when the content warrants it. Its guidelines are blunt about payment: it does "
    "not pay for unsolicited submissions, though it offers incentives for consistent "
    "contributors. Submissions are complete drafts sent as a .doc attachment, not pitches in the "
    "body of an email.",
    "https://africasacountry.com/submission-guidelines/",
    "mailto:ideas@africasacountry.com", "ideas@africasacountry.com",
    "Email a completed draft as a Word attachment",
    src("Africa Is a Country — Submission guidelines (official)",
        "https://africasacountry.com/submission-guidelines/"),
    {"summary": "No stated country restriction. The subject matter is Africa and its diaspora, "
                "but the guidelines do not restrict who may submit.",
     "mode": "not-stated", "includesRegions": ["africa"],
     "allowsDiaspora": True, "notStated": True},
    ["opinion", "reviews", "essays", "analysis"],
    "Commentary, criticism, music video and film reviews",
    pay(None, None, None, "No pay for unsolicited submissions; incentives for consistent contributors",
        "Official guidelines, quoted: 'Short answer is that we don't pay people for unsolicited "
        "submissions. We do, however, offer incentives for consistent contributors.' BRYME "
        "records no figure because none is published. Treat this as a byline-and-audience market "
        "rather than a paid one until you have an editor relationship.",
        "Not publicly stated"),
    {"min": 700, "max": 800,
     "display": "Usually 700–800 words; occasionally 900 or a little more"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["A timely, compelling issue that keeps the reader's interest.",
     "Detail, backed up with hyperlinks — not footnotes or citations.",
     "Music videos and film reviews with strong introductions and critiques, which can be short "
     "and sweet.",
     "Relevant non-copyrighted images, videos or audio. Wikimedia, Flickr Creative Commons or "
     "another photo-sharing source is preferred."],
    ["Submissions pasted into the body of the email. The guidelines ask for a Word attachment "
     "and are explicit that the text should not go in the email itself."],
    ["Attach a Word document — .doc is preferred over .docx — in Times New Roman.",
     "Include a suggested title, your name, and a one to two sentence bio with your email or web "
     "address and any social handles.",
     "Attach images as JPEGs or list the URLs, and keep image files around 120 KB.",
     "Email everything to ideas@africasacountry.com.",
     "If published elsewhere afterwards, credit and link Africa Is a Country."],
    "Not stated in detail. The guidelines say they are happy for you to sell the work elsewhere, "
    "provided Africa Is a Country is credited and linked to.",
    ["Read https://africasacountry.com/submission-guidelines/ — it is short and specific.",
     "Send a finished draft, not a pitch.",
     "Do not expect payment for an unsolicited first submission."],
    ["africa is a country", "africa", "diaspora", "commentary", "criticism", "film review",
     "unpaid"]))

# ------------------------------------------------------- 100 Word Story
NEW.append(rec(
    "100-word-story", "100 Word Story", "Stories of exactly 100 words",
    "100 Word Story: exactly 100 words, $2 fee, opens the first week of each month",
    "100 Word Story publishes stories of exactly 100 words — no more and no less, counted by "
    "Microsoft Word's tally, with the title not included in the count. Submissions open the "
    "first week of every month and carry a $2 fee. The magazine particularly encourages Black, "
    "Indigenous and People of Colour, writers from economically disadvantaged backgrounds, and "
    "LGBTQIA+ and disability communities to submit.",
    "https://100wordstory.org/submit/",
    "https://100wordstory.org/submit/", None, "Online submission, first week of each month",
    src("100 Word Story — Submit (official)", "https://100wordstory.org/submit/"),
    {"summary": "No stated country restriction. 100 Word Story states that among the types of "
                "underrepresentation in literature it particularly encourages Black, Indigenous "
                "and People of Colour, those from economically disadvantaged backgrounds, and "
                "those belonging to LGBTQIA+ and disability communities to submit.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction"], "Stories of exactly 100 words",
    pay(None, None, None, "Payment not stated on the submit page; $2 submission fee applies",
        "The official submit page sets out the form, the monthly window and the $2 submission "
        "fee, but does not state a payment rate for published stories, so BRYME records no "
        "figure. The $2 fee is described as the minimum needed to cover the costs of the "
        "submission system. Confirm the current rate for published work before you submit.",
        "Not publicly stated"),
    {"min": 100, "max": 100, "display": "Exactly 100 words (title not counted)"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["A complete story in exactly 100 words — the whole story, holding together, not a fragment.",
     "A short bio of 25 words maximum.",
     "Word count verified against Microsoft Word's tally; the title sits outside the 100 words."],
    ["Anything that is not exactly 100 words. The page repeats the point: exactly 100 words, no "
     "more or no less.",
     "A bio longer than 25 words.",
     "Multiple stories in a single submission — each story must be submitted separately."],
    ["Submit during the first week of a month, when submissions are open.",
     "Pay the $2 submission fee per story.",
     "Submit each story separately; you may submit as many as you like.",
     "Include a bio of 25 words or fewer.",
     "Count your words in Microsoft Word."],
    "Not stated on the official submit page.",
    ["Check https://100wordstory.org/submit/ for the current monthly window.",
     "Count in Microsoft Word, not in another tool — the tallies differ.",
     "Your title is free; the 100 words are the story."],
    ["100 word story", "flash fiction", "exactly 100 words", "micro fiction", "$2 fee"]))


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
        BASE = {
            "the-elephant": ("KE", "Kenya"),
            "africa-is-a-country": ("", "International"),
            "100-word-story": ("US", "United States"),
        }
        for r in NEW:
            base, label = BASE[r["slug"]]
            pc[r["slug"]] = {"base": base, "label": label}
        PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Added {len(NEW)} verified records. Total opportunities: {len(opps)}")


# ---------------------------------------------------------------------------
# Fetched on 2026-09-30 in the same pass but deliberately NOT added, and why:
#
#   guernicamag.com/about/submissions/  Page says only that Guernica considers
#       completed manuscripts, no pitches, through Submittable, and that the
#       current editorial guidelines live there. No rate, word count or AI
#       policy on the page. Needs the Submittable listing read before a record
#       can be written.
#   electricliterature.com              The submissions post that resolves is
#       dated 2 January 2018 with a window that closed 16 January. The $50 rate
#       and 1,500-4,000 word range on it are eight years old. Stale - do not
#       publish as current.
#   opendemocracy.net/en/submit/        Resolves to an ourNHS contribute page
#       from 2013, not the house submissions guide. Wrong page.
#   wordswithoutborders.org/submissions/ Nav and events only in the server HTML;
#       the rate table is rendered client-side. Needs a browser pass.
#   passblue.com/contributors/          Fetch failed (no response).
#   caravanmagazine.in/contribute       20 words of text; the page is
#       client-rendered. Needs a browser pass.
#   globalpressjournal.com/submissions/ Page is a topic/country archive index,
#       not submission guidelines. Needs the correct URL.
#   inkstickmedia.com/contribute/       Resolves to the article index. Needs the
#       correct URL.
#   clarkesworldmagazine.com            Already in the database as
#       clarkesworld-fiction and clarkesworld-nonfiction. Not duplicated.
#   uncannymagazine.com                 Already in the database as
#       uncanny-fiction and uncanny-poetry. Not duplicated.
#   strangehorizons.com/submit/         States that each department has separate
#       guidelines. Needs per-department records, not one.
#   griffithreview.com                  Already in the database as
#       griffith-review. Not duplicated.
# ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------
# Fetched on 2026-09-30 in the same pass but deliberately NOT added, and why:
#
#   guernicamag.com/about/submissions/  Page says only that Guernica considers
#       completed manuscripts, no pitches, through Submittable, and that the
#       current editorial guidelines live there. No rate, word count or AI
#       policy on the page. Needs the Submittable listing read before a record
#       can be written.
#   electricliterature.com              The submissions post that resolves is
#       dated 2 January 2018 with a window that closed 16 January. The $50 rate
#       and 1,500-4,000 word range on it are eight years old. Stale - do not
#       publish as current.
#   opendemocracy.net/en/submit/        Resolves to an ourNHS contribute page
#       from 2013, not the house submissions guide. Wrong page.
#   wordswithoutborders.org/submissions/ Nav and events only in the server HTML;
#       the rate table is rendered client-side. Needs a browser pass.
#   passblue.com/contributors/          Fetch failed (no response).
#   caravanmagazine.in/contribute       20 words of text; the page is
#       client-rendered. Needs a browser pass.
#   globalpressjournal.com/submissions/ Page is a topic/country archive index,
#       not submission guidelines. Needs the correct URL.
#   inkstickmedia.com/contribute/       Resolves to the article index. Needs the
#       correct URL.
#   clarkesworldmagazine.com            Already in the database as
#       clarkesworld-fiction and clarkesworld-nonfiction. Not duplicated.
#   uncannymagazine.com                 Already in the database as
#       uncanny-fiction and uncanny-poetry. Not duplicated.
#   strangehorizons.com/submit/         States that each department has separate
#       guidelines. Needs per-department records, not one.
#   griffithreview.com                  Already in the database as
#       griffith-review. Not duplicated.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
