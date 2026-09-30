#!/usr/bin/env python3
"""Add verified writing-market batch 3 (2026-09-30).

Six NEW markets. Every figure was read off the publication's own guidelines
page on 2026-09-30; raw page text is saved under research/batch3/*.txt.

These names were surfaced by a web search rather than by the candidate CSV.
The aggregator pages that surfaced them publish their own pay figures; NONE of
those figures are used here. Each one was fetched from the publication's own
site and recorded from that. Where a publication's page states no rate, the
field says so.

Probed 45 searched names; 10 yielded a usable guidelines page; 6 supported a
record. Rejects are logged at the bottom.
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

# ------------------------------------------------------- 1 Pseudopod
NEW.append(rec(
    "pseudopod", "Pseudopod", "Horror short fiction, published as audio",
    "Pseudopod: 8 cents a word original, $100 reprints, no AI",
    "Pseudopod, the Escape Artists horror podcast, pays the professional rate of 8 cents a word "
    "for original fiction, $100 flat for short story reprints and $20 flat for flash fiction "
    "reprints under 1,500 words. It does not accept any AI or LLM-generated work, including the "
    "cover letter. Submissions go through its Moksha portal during open general submission "
    "periods, which usually consider one original and one reprint per author.",
    "https://pseudopod.org/submissions/",
    "https://pseudopod.org/submissions/", None,
    "Moksha portal — during an open general submission period",
    src("Pseudopod — Submissions (official)", "https://pseudopod.org/submissions/"),
    {"summary": "No stated country restriction. The guidelines place no limits on genre "
                "definitions or on content, and describe no taboos about what may appear in a "
                "story.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction"], "Horror short fiction, original and reprint",
    pay("USD", 20, 100, "8¢/word original; $100 short story reprint; $20 flash reprint",
        "Official submissions page: Pseudopod pays the pro rate of $0.08 per word for original "
        "fiction, a $100 flat rate for short story reprints, and a $20 flat rate for flash "
        "fiction reprints (stories below 1,500 words). The 8¢ rate applies per word, so the "
        "actual total depends on length; the flat reprint rates are recorded here.",
        "Not publicly stated"),
    {"min": None, "max": 1500,
     "display": "Flash reprints defined as under 1,500 words; no maximum stated for originals"},
    {"label": "Query if no automated confirmation within 24 hours; after 60 days, query",
     "band": "1-3-months", "official": True},
    "rolling",
    {"date": None,
     "display": "Submissions are only accepted during an open general submission period; check "
                "the schedule at pseudopod.org before sending.",
     "recurring": True},
    "prohibited",
    ["Short horror fiction, original or reprint, that would work narrated aloud by a performer.",
     "Any kind of content. Pseudopod states it does not split hairs about genre definitions and "
     "observes no taboos about what can appear in stories.",
     "One original and one reprint per author during a general submission period.",
     "A different original or reprint if you already have a submission under consideration "
     "through a separate portal — each call is treated separately."],
    ["AI or LLM-generated work of any kind. Basic spelling and grammar checking tools are "
     "acceptable, but Pseudopod recommends steering clear of all generative AI at every stage of "
     "the writing process.",
     "AI or LLM tools used to write the cover letter — explicitly asked against.",
     "Submitting the same story to multiple Escape Artists podcasts at once (Escape Pod, "
     "PodCastle, Cast of Wonders, CatsCast and PseudoPod). Wait for a decision on one before "
     "sending it to another."],
    ["Check the schedule first — submissions are only accepted when Pseudopod is open.",
     "Submit through the Moksha portal; you will get an automated email confirmation.",
     "Query if the confirmation has not arrived within 24 hours, and again after 60 days if you "
     "have heard nothing.",
     "Simultaneous submissions are acceptable with disclosure — say that you are submitting "
     "elsewhere.",
     "Do not use AI for the story or for the cover letter."],
    "Not stated on the official submissions page.",
    ["Check https://pseudopod.org/submissions/ and the schedule before writing anything — the "
     "portal is only open during general submission periods.",
     "Write for the ear; this is an audio market.",
     "Reprints are paid, so a strong back catalogue is worth money here."],
    ["pseudopod", "horror", "audio fiction", "podcast", "escape artists", "8 cents per word",
     "reprints", "moksha", "no ai"]))

# ------------------------------------------------------- 2 Gulf Coast
NEW.append(rec(
    "gulf-coast", "Gulf Coast", "Poetry, fiction, nonfiction and translation",
    "Gulf Coast: $50 per page in print, $75–$100 online exclusives",
    "Gulf Coast, the literary journal housed in the University of Houston English Department, "
    "pays $50 per .doc or PDF page for poetry, fiction and nonfiction in its print issues, and "
    "guarantees $75 for poetry and $100 for prose in its Online Exclusives. Regular submissions "
    "carry a $3 reading fee that goes entirely toward author honorariums. Work over 7,000 words "
    "cannot be read.",
    "https://gulfcoastmag.org/submit/",
    "https://gulfcoastmag.org/submit/", None, "Submittable — $3 reading fee",
    src("Gulf Coast — Submit (official)", "https://gulfcoastmag.org/submit/"),
    {"summary": "No stated country restriction on the submissions page.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["poetry", "fiction", "creative-nonfiction", "translation"],
    "Poetry, fiction, nonfiction and translation",
    pay("USD", 50, 100, "$50 per page in print; $75 poetry / $100 prose online exclusives",
        "Official submit page: Gulf Coast pays $50 per .doc or PDF page for poetry, fiction and "
        "nonfiction in its print issues. In its Online Exclusives it guarantees $75 for poetry "
        "and $100 for prose. A $3 reading fee applies to regular submissions and is stated to go "
        "100% toward increasing author honorariums. The rate is per page, so the total depends "
        "on the length of the piece.",
        "Not publicly stated"),
    {"min": None, "max": 7000, "display": "Up to 7,000 words; longer work cannot be read"},
    {"label": "Not stated; wait for a response before submitting again",
     "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Poetry, fiction, nonfiction and translation, under 7,000 words.",
     "Work that has not appeared in Gulf Coast within the last two years — accepted authors are "
     "asked to wait two years from the date of publication before submitting again."],
    ["General submissions by email or post. Neither is accepted; Submittable is the only route.",
     "Anything over 7,000 words.",
     "A further submission before you have had a response on the one already under "
     "consideration."],
    ["Submit through Submittable via the link on the submit page.",
     "Pay the $3 reading fee for regular submissions.",
     "Put your name, address, phone number and email on the first page, and the title on "
     "subsequent pages.",
     "Keep prose under 7,000 words.",
     "Simultaneous submissions are allowed, but tell Gulf Coast promptly if the piece is "
     "accepted elsewhere.",
     "If accepted, wait two years from publication before submitting again."],
    "Not stated on the official submit page.",
    ["Read https://gulfcoastmag.org/submit/ and use the Submittable link.",
     "Format as asked — contact details on page one, title on the pages after.",
     "Do not email or post the work; it will not be read."],
    ["gulf coast", "university of houston", "poetry", "fiction", "nonfiction", "$50 per page",
     "submittable", "7000 words"]))

# ------------------------------------------------------- 3 Nachtljocht
NEW.append(rec(
    "nachtljocht", "Nachtljocht", "Fiction and short plays",
    "Nachtljocht: $15, fiction 3,000–12,000 words, opens 1 October 2026",
    "Nachtljocht accepts previously unpublished fiction and short plays between 3,000 and 12,000 "
    "words, and pays accepted writers $15 plus a print contributor copy and digital copies. Its "
    "2026–27 reading period runs from 1 October 2026 to 31 March 2027, with responses aimed at "
    "within 60 days. There is a $3 submission fee that includes a digital copy of the most recent "
    "issue.",
    "https://nachtljocht.com/",
    "https://nachtljocht.com/", None, "Online submission form — $3 fee",
    src("Nachtljocht — official site", "https://nachtljocht.com/"),
    {"summary": "Eligibility requirements are published on the submission form rather than on "
                "the public page, so BRYME records no restriction and no confirmation of "
                "openness. Check the form before you submit.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction", "drama"], "Fiction and short plays",
    pay("USD", 15, 15, "$15 plus a print contributor copy and digital copies",
        "Official site: accepted writers receive $15 USD, one complimentary print contributor "
        "copy, and digital copies of the issue. A $3 USD submission fee applies and includes a "
        "digital copy of the most recent issue.",
        "Not publicly stated"),
    {"min": 3000, "max": 12000, "display": "3,000–12,000 words"},
    {"label": "Aimed at within 60 days", "band": "1-3-months", "official": True},
    "upcoming",
    {"date": "2026-10-01",
     "display": "The 2026–27 reading period runs from 1 October 2026 to 31 March 2027.",
     "windowEnd": "2027-03-31", "recurring": True},
    "prohibited",
    ["Previously unpublished fiction and short plays between 3,000 and 12,000 words.",
     "Work that is emotionally precise, formally confident and unafraid of strangeness — the "
     "stated editorial emphasis.",
     "Writers at any stage; each issue brings together emerging and established writers across "
     "genres, forms and styles."],
    ["Work written by large language models. Nachtljocht states it does not publish it, and "
     "separately states that it does not use AI to evaluate submissions and will never upload "
     "your work to an AI detector.",
     "Previously published work."],
    ["Submit through the submission form on https://nachtljocht.com/ during the reading period.",
     "Pay the $3 fee, which includes a digital copy of the most recent issue.",
     "Stay between 3,000 and 12,000 words and send unpublished work only.",
     "Simultaneous submissions are welcome.",
     "Once you have a decision you may submit another piece while the reading period is still "
     "open.",
     "Read the full formatting requirements, rights information and eligibility requirements on "
     "the submission form — they are not on the public page."],
    "Full rights information is published on the submission form rather than on the public page.",
    ["The 2026–27 reading period opens 1 October 2026 and closes 31 March 2027 — submit inside "
     "that window.",
     "Read the eligibility requirements on the submission form before you write; they are not on "
     "the public page.",
     "Nachtljocht has no social media. Any account claiming to represent it is unauthorised."],
    ["nachtljocht", "fiction", "short plays", "$15", "3000-12000 words", "reading period",
     "no ai", "no ai detector"]))

# ------------------------------------------------------- 4 The Lisbon Literary Review
NEW.append(rec(
    "lisbon-literary-review", "The Lisbon Literary Review",
    "Poetry, short fiction, translation, essay and nonfiction in Portuguese and English",
    "The Lisbon Literary Review: bilingual poetry and fiction, no AI",
    "The Lisbon Literary Review is a new bilingual journal emphasising Portuguese- and "
    "English-language poetry and translations between the two. It accepts poetry, short fiction, "
    "literary translation, photography, drawing, essay and nonfiction prose including chronicle "
    "and reflective writing. It does not consider or publish work generated wholly or "
    "substantially by AI, aims to respond within four to six weeks, and pays no stated rate.",
    "https://www.lisbonliteraryreview.com/submissions/",
    "https://www.lisbonliteraryreview.com/submissions/", None, "Online submission form",
    src("The Lisbon Literary Review — Submissions (official)",
        "https://www.lisbonliteraryreview.com/submissions/"),
    {"summary": "Open internationally to authors writing primarily in Portuguese or English. The "
                "journal states it is calling all creative writers, translators and artists.",
     "mode": "worldwide", "includesRegions": [], "allowsDiaspora": True, "notStated": False},
    ["poetry", "fiction", "translation", "essays", "creative-nonfiction"],
    "Poetry, short fiction, translation, photography, drawing, essay and nonfiction prose",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out the formats, the AI policy, the response time and "
        "the rights position, but publishes no payment rate, so BRYME records no figure. As a "
        "new journal its terms may still be settling — confirm before you submit.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No word limit stated on the public page; one text per page"},
    {"label": "Four to six weeks, occasionally longer", "band": "1-3-months", "official": True},
    "open", None, "prohibited",
    ["Work demonstrating originality, artistic merit and a distinctive voice.",
     "Poetry in Portuguese or English, and translations of poems between the two languages.",
     "Short fiction, literary translation, photography, drawing, essay, and nonfiction prose "
     "including chronicle and personal or reflective writing.",
     "One text per page, with your email address included."],
    ["Work generated wholly or substantially by artificial intelligence. AI-generated "
     "submissions are declined.",
     "Translations where you do not hold the necessary rights — by submitting a translation the "
     "author confirms that they do."],
    ["Read the terms and conditions on the submissions page before submitting.",
     "Format with no more than one text per page and include your email address.",
     "Simultaneous submissions are accepted, but tell the journal immediately if the text is "
     "accepted elsewhere.",
     "Expect a response in four to six weeks, sometimes longer."],
    "Authors retain copyright. By accepting publication the author grants the journal first "
    "publication rights.",
    ["Read https://www.lisbonliteraryreview.com/submissions/ in full — the terms and conditions "
     "sit on that page.",
     "If you are submitting a translation, be certain you hold the rights.",
     "This is a new journal; confirm current terms before you send."],
    ["lisbon literary review", "portuguese", "english", "bilingual", "poetry", "translation",
     "no ai", "copyright retained"]))

# ------------------------------------------------------- 5 Stygian Lepus
NEW.append(rec(
    "stygian-lepus", "Stygian Lepus", "Fiction, poetry and art",
    "Stygian Lepus: $5 token payment, up to 5,000 words",
    "Stygian Lepus offers a token payment of $5 USD for each accepted submission and takes work "
    "up to 5,000 words. All copyright remains with the author and reprints are allowed, though "
    "the magazine asks for three months' exclusivity from publication. Simultaneous submissions "
    "are disqualified.",
    "https://www.stygianlepus.com/submissions/",
    "https://www.stygianlepus.com/submissions/", None, "Email submission — one email per piece",
    src("Stygian Lepus — Submissions (official)",
        "https://www.stygianlepus.com/submissions/"),
    {"summary": "No stated country restriction on the submissions page.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction", "poetry"], "Fiction, poetry and art",
    pay("USD", 5, 5, "$5 USD token payment per accepted submission",
        "Official submissions page: Stygian Lepus offers a small token payment of $5 USD for each "
        "accepted submission. It describes the payment as a token, so treat this as a credit "
        "market rather than a professional-rate one.",
        "Not publicly stated"),
    {"min": None, "max": 5000, "display": "Up to 5,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Fiction, poetry and art up to 5,000 words.",
     "A short bio of no more than 100 words with one link."],
    ["Simultaneous submissions. The page states plainly that they will be disqualified — "
     "simultaneous means sending the same piece to two publishers at the same time.",
     "Work over 5,000 words.",
     "More than one submission per email."],
    ["Send one email per submission.",
     "Include a bio of 100 words or fewer with one link.",
     "Do not submit the same piece anywhere else at the same time.",
     "Be aware that submitting implies consent to be added to the newsletter, which is how "
     "approval drafts are sent. Marking those emails as spam prevents the approval request and "
     "means Stygian Lepus can no longer accept submissions from you."],
    "All copyright remains with the author and reprints are allowed, provided Stygian Lepus has "
    "exclusivity for three months from the publication date.",
    ["Read https://www.stygianlepus.com/submissions/ before sending.",
     "One piece per email — do not bundle.",
     "Do not whitelist-block the newsletter if you want to be able to submit again."],
    ["stygian lepus", "fiction", "poetry", "art", "$5", "5000 words", "copyright retained",
     "no simultaneous"]))

# ------------------------------------------------------- 6 In Short
NEW.append(rec(
    "in-short-journal", "In Short: A Journal of Flash Nonfiction",
    "Flash nonfiction, micros and short-shorts",
    "In Short: flash nonfiction to 1,000 words — unpaid, rights revert in 3 months",
    "In Short publishes flash nonfiction of 1,000 words or fewer, including memoir, lyric essays, "
    "experimental pieces and straightforward narrative. Micros run to 400 words and short-shorts "
    "to 100. It cannot yet pay writers and says so openly, and it asks only for first serial "
    "rights, with all rights reverting to the author three months after publication.",
    "https://inshortjournal.com/in-short-home-page/submissions/",
    "https://inshortjournal.com/in-short-home-page/submissions/", None,
    "Online submission — see submissions page",
    src("In Short — Submissions (official)",
        "https://inshortjournal.com/in-short-home-page/submissions/"),
    {"summary": "No stated country restriction on the submissions page.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["creative-nonfiction", "personal-essays", "essays"],
    "Flash nonfiction, micros and short-shorts",
    pay(None, None, None, "Unpaid — the journal states it cannot yet pay writers",
        "Official submissions page: In Short states that because creative nonfiction often "
        "contains sensitive material it cannot yet pay writers, and that it hopes to change that "
        "through grants, tip jar donations and paid feedback options. BRYME records no figure "
        "because there is none. Treat this as an unpaid credit market.",
        "Not applicable — unpaid"),
    {"min": None, "max": 1000,
     "display": "Flash nonfiction to 1,000 words; micros to 400; short-shorts to 100"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Flash nonfiction of 1,000 words or fewer.",
     "Memoir, lyric essays, experimental pieces, straightforward narratives, and everything in "
     "between — the page names hermit crabs among the things it loves.",
     "Micros: flash nonfiction of 400 words or fewer.",
     "Short-shorts: flash of 100 words or fewer."],
    ["Anything over 1,000 words for the main category.",
     "An expectation of payment. The journal is explicit that it cannot pay yet."],
    ["Submit through the route on the submissions page.",
     "Pick the right category — flash nonfiction, micro or short-short each has its own word "
     "ceiling.",
     "Do not expect payment; do expect a fast turnaround on rights."],
    "In Short asks for first serial rights only. All rights revert to the author three months "
    "after publication, after which work may be reprinted, with an acknowledgement of In Short "
    "as the place of initial publication.",
    ["Read https://inshortjournal.com/in-short-home-page/submissions/ before sending.",
     "This is unpaid — submit for the credit and the fast rights reversion, not the money.",
     "Keep to the ceiling for your category: 1,000, 400 or 100 words."],
    ["in short", "flash nonfiction", "creative nonfiction", "micro", "1000 words", "unpaid",
     "rights revert"]))


BASE = {
    "pseudopod": ("", "International"),
    "gulf-coast": ("US", "United States"),
    "nachtljocht": ("", "International"),
    "lisbon-literary-review": ("PT", "Portugal"),
    "stygian-lepus": ("", "International"),
    "in-short-journal": ("", "International"),
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
# Probed in batch 3 but NOT added, and why:
#
#   newfeathers.com            The domain resolves to a HugeDomains sale page.
#       The magazine is gone or moved. Do not add.
#   smallbeerpress.com         Resolved to the publisher's homepage, not the
#       Lady Churchill's Rosebud Wristlet submissions route.
#   litromagazine.com          Homepage only; the submissions terms are not in
#       the server HTML.
#   sunspotlit.com             Real submissions terms (Submittable or Duotrope,
#       simultaneous welcome, nonfiction up to 49,000 words) but no payment
#       figure and no fiction word limit on the public page. Held back rather
#       than published with two blank core fields.
#   35 further searched names  No guidelines page found at the guessed paths.
#       Several are real magazines whose submissions route is a Submittable or
#       Moksha portal rather than a page on their own domain, which path-based
#       discovery cannot reach.
#
# Sourcing note: the aggregator pages that surfaced these names publish pay
# figures of their own. None were used. Pseudopod's 8c/word and Gulf Coast's
# $50/page were both read off the publications' own pages, which is the only
# source BRYME's standard allows.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
