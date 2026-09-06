#!/usr/bin/env python3
"""Add the verified Australia publication batch (2026-09-06).

Same standard as the UK and Canada batches: every figure read off the
publication's own live guidelines page on 2026-09-06 (raw text saved in
/home/user/research/au/*.txt).
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-06"


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

# ------------------------------------------------------------------ 1 Island
NEW.append(rec(
    "island-magazine", "Island", "Poetry, fiction, nonfiction and graphic narratives",
    "Island: submissions close 18 September 2026",
    "Island, a Tasmanian literary and arts magazine, has three calls closing 18 September 2026 — print poetry for Island 180, and nonfiction and fiction for Island Online. It pays contributor fees and explicitly refuses AI-written work. Open to Australia, New Zealand and Australians abroad.",
    "https://islandmag.com/submit",
    "https://island.submittable.com/submit", "jane@islandmag.com",
    "Submittable; pitches by email to the editor",
    src("Island — Submissions and prizes (official)", "https://islandmag.com/submit"),
    {"summary": "Official and restrictive: \"Island welcomes submissions from Australia, New Zealand and Australians living abroad.\" Writers based elsewhere are outside the stated eligibility.",
     "mode": "restricted", "includesRegions": ["australia", "new-zealand"], "allowsDiaspora": True, "notStated": False},
    ["poetry", "fiction", "creative-nonfiction", "essays"], "Poetry, fiction, nonfiction and graphic narratives",
    pay("AUD", None, None, "Pays contributor fees — schedule not on the public page",
        "Island states it pays contributor fees, but the fee schedule sits behind the link to its Submittable portal rather than on the public submissions page, so BRYME states no figure. Check the current rate on the Submittable listing before you submit.",
        "Not publicly stated"),
    {"min": None, "max": 4000, "display": "Online nonfiction ~1,500 words; print nonfiction rarely over 4,000"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "deadline",
    {"date": "2026-09-18",
     "display": "Print poetry (Island 180), Island Online nonfiction and Island Online fiction all close 18 September 2026. Print nonfiction is currently closed. Graphic narrative pitches for 2027 are open with no formal cut-off.",
     "windowEnd": "2026-09-18", "recurring": True},
    "prohibited",
    ["Print poetry for Island 180: a maximum of three poems in any form.",
     "Island Online nonfiction: new nonfiction of approximately 1,500 words.",
     "Writing about what fascinates, excites or enrages you — it does not have to be zeitgeisty.",
     "Graphic narrative pitches for 8-page works, with specialist editor Joshua Santospirito."],
    ["Anything you have written, rewritten or otherwise created using AI. Their stated reason: \"AI is destroying writers' income.\"",
     "Print nonfiction while that door is closed, and work much over 4,000 words for print."],
    ["Submittable", "Australia, NZ or Australians abroad", "Max 3 poems", "No AI"],
    "Not stated on the submissions page.",
    ["Read https://islandmag.com/submit and pick the right call — several close 18 September 2026.",
     "Check the contributor fee on the linked Submittable listing before submitting.",
     "For graphic narratives, pitch jane@islandmag.com directly."],
    ["island", "australia", "tasmania", "poetry", "nonfiction", "aud", "no ai"]))

# ---------------------------------------------------------------- 2 Westerly
NEW.append(rec(
    "westerly", "Westerly", "Poetry, fiction, creative non-fiction and reviews",
    "Westerly: $250 per poem, $500 for prose, $620 for comics",
    "Westerly, published twice a year out of the University of Western Australia, pays $250 for one poem, $300 for a poetic sequence, $500 for prose, $620 for visual art, photo essays and comics, and $250 for online publication. It aims to pay Australian Society of Authors rates.",
    "https://westerlymag.com.au/submit/",
    "https://westerlymag.com.au/submit/", None,
    "Online submission during an open window",
    src("Westerly — Submit (official)", "https://westerlymag.com.au/submit/"),
    {"summary": "No nationality restriction stated on the submit page. Westerly is based at the University of Western Australia.",
     "mode": "not-stated", "notStated": True},
    ["poetry", "fiction", "creative-nonfiction", "reviews"], "Poetry, fiction, creative non-fiction and reviews",
    pay("AUD", 250, 620, "$250–$620 depending on form",
        "Official payment rates. Print work — Poems: $250 for one poem or $300 for a poetic sequence; Prose (including scholarly work): $500; Visual art, photo essays and comics: $620. Online publication (including reviews): $250; online special issues are paid as per print. Westerly states it aspires to pay Australian Society of Authors (ASA) rates when possible, depending on its funding, and that it is bound by policy to pay minimum set fees for all work. Non-subscribers whose work is accepted are offered a discounted year's subscription as part-payment.",
        "Not publicly stated"),
    {"min": None, "max": 5000, "display": "Fiction/CNF max 3,500 words; scholarly max 5,000; reviews ~800"},
    {"label": "Not stated; they endeavour to give brief feedback on request", "band": "not-stated", "official": True},
    "upcoming",
    {"display": "Westerly is published twice a year, in June and November. Submission windows open for each issue as advertised. Scholarly articles may be submitted at any time.",
     "recurring": True},
    "not-stated",
    ["Poetry: a maximum of five poems, each a maximum of 50 lines.",
     "Fiction and creative non-fiction: maximum 3,500 words. Scholarly articles: maximum 5,000 words.",
     "Reviews of approximately 800 words, for online or print. Comics of up to four A5 pages.",
     "Manuscripts 1.5-spaced in Times New Roman 12, with a cover letter carrying a two-line bio and email."],
    ["More than one short story at any one time — wait for a response before submitting again.",
     "Separate files when submitting online: collate poems and material into a single document."],
    ["Open window (scholarly articles anytime)", "1.5-spaced Times New Roman 12", "Two-line bio in cover letter"],
    "Not fully stated on the submit page.",
    ["Check https://westerlymag.com.au/submit/ — the open window is advertised at the bottom of the page.",
     "Collate your work into a single 1.5-spaced document with a two-line bio.",
     "Submit online, and wait for a response before sending anything else."],
    ["westerly", "australia", "perth", "poetry", "fiction", "aud"]))

# --------------------------------------------------------- 3 Kill Your Darlings
NEW.append(rec(
    "kill-your-darlings", "Kill Your Darlings", "Short fiction",
    "Kill Your Darlings: minimum $1,000 for short fiction — members only",
    "Kill Your Darlings pays a minimum of $1,000 for short fiction of 2,000–5,000 words, and reads year-round from established and emerging writers. The catch is real: only KYD Members may submit fiction, and membership is a paid subscription.",
    "https://www.killyourdarlings.com.au/write-for-us/",
    "https://www.killyourdarlings.com.au/write-for-us/", None,
    "Submission portal, members only",
    [{"name": "Kill Your Darlings — Write For Us (official)", "url": "https://www.killyourdarlings.com.au/write-for-us/"},
     {"name": "Kill Your Darlings — Submission guidelines (official)", "url": "https://www.killyourdarlings.com.au/submission-guidelines/"}],
    {"summary": "Official and restrictive in a way that costs money: \"We only accept fiction submissions from KYD Members.\" Membership is a paid subscription (advertised at under $5 a month) which also gives free entry to their writing prizes. No nationality restriction is stated.",
     "mode": "restricted", "includesGroups": ["kyd-members"], "notStated": False},
    ["fiction"], "Short fiction",
    pay("AUD", 1000, None, "Minimum $1,000",
        "Official: \"Minimum payment is $1000\" for short fiction of 2,000–5,000 words. This is a floor, not a ceiling, and no maximum is published. Weigh it against the cost of the KYD membership that is required to submit at all.",
        "Not publicly stated"),
    {"min": 2000, "max": 5000, "display": "2,000–5,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Short fiction between 2,000 and 5,000 words, previously unpublished.",
     "Submissions from established and emerging writers alike, year-round.",
     "A current KYD membership — fiction submissions are members-only."],
    ["Previously published work.",
     "Fiction submissions from non-members — they are not accepted."],
    ["KYD membership required", "2,000–5,000 words", "Previously unpublished"],
    "Not stated on the write-for-us page.",
    ["Read https://www.killyourdarlings.com.au/submission-guidelines/ in full.",
     "Become a KYD Member — fiction submissions are members-only.",
     "Submit your 2,000–5,000 word story through the members' portal."],
    ["kill your darlings", "australia", "melbourne", "short fiction", "aud"]))

# ---------------------------------------------------------------- 4 Aurealis
NEW.append(rec(
    "aurealis", "Aurealis", "Science fiction, fantasy and horror",
    "Aurealis: AUD 6c a word for all stories published in 2027",
    "Aurealis, Australia's long-running science fiction and fantasy magazine, pays AUD 2–6 cents a word for stories of 2,000–8,000 words, rising to a flat 6 cents a word for everything published in 2027. Non-fiction pays A$40. It has a no-AI policy.",
    "https://aurealis.com.au/submissions/",
    "https://aurealis.com.au/submissions/", "nonfiction@aurealis.com.au",
    "Online submission during an open reading period",
    src("Aurealis — Submissions (official)", "https://aurealis.com.au/submissions/"),
    {"summary": "Official and window-dependent: Australian writers and subscribers from anywhere may submit 1 February – 30 September. Everyone else, anywhere in the world, may submit only during 1–14 March. Subscribers are fast-tracked through assessment, though stories are selected anonymously on merit regardless of subscriber status.",
     "mode": "restricted", "includesRegions": ["australia"], "allowsDiaspora": True, "notStated": False},
    ["fiction", "articles"], "Science fiction, fantasy and horror",
    pay("AUD", 40, None, "AUD 2–6c a word; 6c a word for 2027; A$40 non-fiction",
        "Official: \"Aurealis pays between AUD2c to AUD6c a word, but assume the lower rate for unsolicited submissions. For all stories published in 2027, Aurealis will be paying AUD6c a word.\" Non-fiction: \"Our payment is A$40.\" Black and white story illustrations: A$25. Contributors also receive a free electronic copy of the issue. The A$40 non-fiction fee is the only flat piece figure published; the fiction rate is per word.",
        "Soon after publication of the issue containing your story"),
    {"min": 2000, "max": 8000, "display": "2,000–8,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Australian writers and subscribers from anywhere: 1 February – 30 September. Anyone anywhere: 1–14 March only.",
     "windowEnd": "2026-09-30", "recurring": True},
    "prohibited",
    ["Science fiction, fantasy or horror short stories between 2,000 and 8,000 words.",
     "All types of science fiction, fantasy and horror of a genuinely speculative nature.",
     "Non-fiction articles and queries by email to nonfiction@aurealis.com.au — these must stay unpublished for 12 months after appearing in Aurealis."],
    ["Derivative work, or horror without a supernatural element.",
     "Reprints, poetry, novel extracts or serials — none of these are published.",
     "AI-generated work: they state a no-AI policy."],
    ["Open reading period", "2,000–8,000 words", "No reprints", "No AI"],
    "They buy first digital rights for publication in the magazine, plus non-exclusive online, audio and print rights, with a twelve-month exclusivity window after electronic publication (apart from 'Best of' anthologies).",
    ["Check which window applies to you at https://aurealis.com.au/submissions/ — non-Australians outside 1–14 March must be subscribers.",
     "Submit a 2,000–8,000 word speculative story through their form.",
     "For non-fiction, email nonfiction@aurealis.com.au instead."],
    ["aurealis", "australia", "science fiction", "fantasy", "horror", "aud", "no ai"]))

# ------------------------------------------------- 5 Australian Book Review
NEW.append(rec(
    "australian-book-review", "Australian Book Review", "Commentary essays and criticism",
    "Australian Book Review: pays for everything it publishes",
    "Australian Book Review welcomes pitches for commentary essays on topics of political and cultural moment. It states it pays for everything it publishes and is publicly committed to increasing its rates, though it does not name a figure.",
    "https://www.australianbookreview.com.au/submissions",
    "https://www.australianbookreview.com.au/submissions", None,
    "Email pitch to the Editor",
    src("Australian Book Review — Submissions (official)", "https://www.australianbookreview.com.au/submissions"),
    {"summary": "No nationality restriction stated on the submissions page. ABR is Australia's leading review of books and arts.",
     "mode": "not-stated", "notStated": True},
    ["essays", "reviews", "opinion", "analysis"], "Commentary essays and criticism",
    pay("AUD", None, None, "Pays for everything published — rate not stated",
        "Official: \"We pay for everything we publish, and we are publicly committed to increasing our rates when we can.\" No figure is published, so BRYME states none rather than guessing.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Not stated"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Succinct pitches for commentary essays on topics of political and cultural moment.",
     "Ideas that complement ABR's increased focus in its areas of interest and expertise.",
     "Pitches sent to the Editor by email."],
    ["Long, unfocused pitches — they ask for succinct ones."],
    ["Email pitch", "Succinct"],
    "Not stated on the submissions page.",
    ["Read https://www.australianbookreview.com.au/submissions.",
     "Read recent commentary essays to judge the fit.",
     "Send a succinct pitch to the Editor at the address on that page."],
    ["australian book review", "abr", "australia", "essays", "criticism", "aud"]))


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

    pc = json.loads(PUBC.read_text(encoding="utf-8"))
    for r in NEW:
        pc[r["slug"]] = {"base": "AU", "label": "Australia"}
    PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {len(NEW)} Australia records. Total opportunities: {len(opps)}")


if __name__ == "__main__":
    main()
