#!/usr/bin/env python3
"""Add the verified US batch (2026-09-06). Same standard as UK/CA/AU:
every figure read off the publication's own live guidelines page today."""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-06"


def rec(slug, publication, title, seo, excerpt, official, apply_url, apply_email,
        apply_method, sources, elig, types, type_label, pay, wc, response,
        status, deadline, ai, want, dont, reqs, rights, how, keywords):
    return {"status": "published", "vertical": "writing", "lastVerified": V,
            "publishedAt": V, "experience": "not-stated",
            "editorExperience": {"status": "not-yet-submitted"},
            "id": slug, "slug": slug, "publication": publication, "title": title,
            "seoTitle": seo, "excerpt": excerpt, "officialUrl": official,
            "applyUrl": apply_url, "applyEmail": apply_email, "applyMethod": apply_method,
            "sources": sources, "eligibility": elig, "writingTypes": types,
            "writingTypeLabel": type_label, "pay": pay, "wordCount": wc,
            "response": response, "submissionStatus": status, "deadline": deadline,
            "aiPolicy": ai, "whatTheyWant": want, "whatTheyDontWant": dont,
            "requirements": reqs, "rights": rights, "howToSubmit": how, "keywords": keywords}


def src(n, u): return [{"name": n, "url": u}]
def pay(c, lo, hi, d, cond, t):
    return {"currency": c, "amountMin": lo, "amountMax": hi, "display": d,
            "conditions": cond, "timing": t}


NEW = [
rec("high-country-news", "High Country News", "Reported stories and essays about the American West",
    "High Country News: $1 a word for reported content",
    "High Country News pays $1 per word for reported content and 50 cents per word for essays and reviews, at the same rate whether the work runs in print, online or both. It covers the American West and takes pitches year-round.",
    "https://www.hcn.org/submissions/", "mailto:pitches@hcn.org", "pitches@hcn.org",
    "Email pitch to pitches@hcn.org",
    src("High Country News — Submission Guidelines (official)", "https://www.hcn.org/submissions/"),
    {"summary": "No nationality restriction stated. The subject matter is the American West, so the work needs a genuine connection to the region rather than the writer needing one.",
     "mode": "not-stated", "notStated": True},
    ["journalism", "essays", "reviews", "analysis", "interviews"], "Reported stories, essays and reviews",
    pay("USD", None, None, "$1/word reported · 50¢/word essays and reviews",
        "Official: \"HCN pays $1/word for reported content and .50/word for essays and reviews. Our rates are the same whether the material is published in print, online or both.\" Per repo convention a per-word rate carries no piece figure. For story forms other than straight text, rates are set case by case.",
        "Not publicly stated"),
    {"min": 600, "max": 8000, "display": "Short-form reported 650–2,500 · essays 600–2,500 · features 2,500–8,000"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Short-form reported stories of 650–2,500 words on conservation, housing, wildfire, transportation, recreation, climate change and Indigenous affairs.",
     "Essays about life in the West, 600–2,500 words. They prefer to read a full draft of an essay rather than a pitch, because essays are hard to judge from a pitch.",
     "Features of 2,500–8,000 words that are deeply reported, with a well-researched pitch and a realistic reporting plan."],
    ["Phone calls — the guidelines ask for none.",
     "Pitches with no reporting plan behind them."],
    ["Email pitches@hcn.org", "Reporting plan for features", "Full draft preferred for essays"],
    "Not stated on the submissions page.",
    ["Read https://www.hcn.org/submissions/ and recent coverage to find the section you fit.",
     "For essays, write the draft — they would rather read it than a pitch.",
     "Email pitches@hcn.org. No phone calls."],
    ["high country news", "american west", "reported", "essays", "environment", "usd"]),

rec("one-story", "One Story", "Literary short fiction",
    "One Story: $500 for a single short story",
    "One Story publishes exactly one story per issue and pays $500 plus 25 contributor copies. It takes literary fiction of 3,000–8,000 words. The spring 2026 window hit its submission cap; the guidelines say submissions reopen in fall 2026.",
    "https://one-story.com/write/submit-a-story/", "https://one-story.submittable.com/submit", None,
    "Submittable",
    src("One Story — Submission Guidelines (official)", "https://one-story.com/write/submit-a-story/"),
    {"summary": "No nationality restriction stated on the guidelines page.", "mode": "not-stated", "notStated": True},
    ["fiction"], "Literary short fiction",
    pay("USD", 500, 500, "$500 plus 25 contributor copies",
        "Official: \"One Story pays $500 and 25 contributors copies for First Serial North American rights. All rights will revert to the author following publication.\"",
        "Not publicly stated"),
    {"min": 3000, "max": 8000, "display": "3,000–8,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "upcoming",
    {"display": "The guidelines state the spring 2026 submission cap was reached and that submissions reopen in fall 2026. Check their Submittable before preparing anything — caps close windows early.",
     "recurring": True},
    "not-stated",
    ["Literary fiction of 3,000–8,000 words, any style, any subject.",
     "Stories that leave a reader satisfied and are strong enough to stand alone — the whole issue is your story.",
     "A cover letter with the word count and a short biographical statement, and the story as a PDF."],
    ["Work previously published online anywhere — blogs, personal sites, online magazines or forums. Work published in print outside North America will be considered.",
     "A second story before your first has had a response.",
     "An expectation of feedback: they state plainly that they do not send comments."],
    ["Submittable", "PDF preferred", "Word count in the cover letter", "One story at a time"],
    "First Serial North American rights. All rights revert to the author following publication.",
    ["Wait for an open window — the cap closes it early.",
     "Prepare a 3,000–8,000 word story as a PDF with a cover letter stating the word count.",
     "Submit through Submittable."],
    ["one story", "literary fiction", "short story", "500", "usa", "usd"]),

rec("ecotone", "Ecotone", "Fiction, non-fiction and poetry about place",
    "Ecotone: honorarium with a $100 minimum",
    "Ecotone, published at UNC Wilmington, pays an honorarium with a $100 minimum plus two copies and a year's subscription. Its writing is about \"reimagining place.\" The general fall 2026 window has closed, but current subscribers can submit fee-free through September.",
    "https://ecotonemagazine.org/submissions/", "https://ecotone.submittable.com/submit", None,
    "Submittable, or by post during a reading period",
    src("Ecotone — Submissions (official)", "https://ecotonemagazine.org/submissions/"),
    {"summary": "No nationality restriction stated. Postal submissions are accepted from within the United States only; everyone else uses Submittable.",
     "mode": "not-stated", "notStated": True},
    ["fiction", "creative-nonfiction", "poetry"], "Fiction, non-fiction and poetry about place",
    pay("USD", 100, None, "Honorarium, $100 minimum",
        "Official: \"Contributors receive an honorarium upon publication, with a $100 minimum; two copies of the issue in which their work appears; and a one-year subscription beginning with the subsequent issue.\" No maximum is published.",
        "Upon publication"),
    {"min": None, "max": None, "display": "Up to 30 pages"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "deadline",
    {"display": "The general fall 2026 window closed early due to overwhelming response. Ecotone is open to fee-free submissions from current subscribers for the month of September 2026. Two general reading periods a year begin in January/February and August/September, plus a Valentine's Day window.",
     "windowEnd": "2026-09-30", "recurring": True},
    "not-stated",
    ["Writing that reimagines place — fiction, creative non-fiction and poetry rooted in the natural world.",
     "One submission per reading period: one in fall, one in spring, one in the Valentine's Day window.",
     "Postal submissions, which they keep open deliberately as a fee-free route during general reading periods."],
    ["More than one submission in a reading period.",
     "Postal submissions from outside the United States, or outside a reading period."],
    ["Submittable or post", "September 2026 is subscribers only", "One submission per reading period"],
    "Not stated on the submissions page.",
    ["Check the current window — Ecotone closes early when response is heavy.",
     "If you subscribe, September 2026 is open to you fee-free.",
     "Submit through Submittable, or by post from within the US during a reading period."],
    ["ecotone", "place", "nature writing", "unc wilmington", "usa", "usd"]),

rec("orion-magazine", "Orion Magazine", "Nonfiction pitches and poetry on nature, culture and place",
    "Orion Magazine: $200 per poem, poetry call 10–15 September 2026",
    "Orion pays $200 for poems accepted into its Spring 2027 Memory and Place issue, with the call open 10–15 September 2026 or until 800 submissions arrive. It also opens twice a year for digital nonfiction pitches, and refuses AI-assisted work outright.",
    "https://orionmagazine.org/submission-guidelines/", "https://orion.submittable.com/submit", "dearorion@orionmagazine.org",
    "Submittable during an open call",
    src("Orion Magazine — Submission Guidelines (official)", "https://orionmagazine.org/submission-guidelines/"),
    {"summary": "No nationality restriction stated on the guidelines page.", "mode": "not-stated", "notStated": True},
    ["poetry", "essays", "creative-nonfiction"], "Nonfiction pitches and poetry",
    pay("USD", 200, 200, "$200 per poem",
        "Official, for the 2026 poetry call: \"We will pay $200 for accepted works.\" Orion does not publish a rate for its digital or print nonfiction on this page, so BRYME states none for those.",
        "Not publicly stated"),
    {"min": None, "max": 2000, "display": "Poems max 2 pages · digital pieces unlikely over 2,000 words"},
    {"label": "Within three months; poetry responses by early 2027", "band": "3-plus-months", "official": True},
    "deadline",
    {"date": "2026-09-15",
     "display": "Poetry call open 10–15 September 2026, or until 800 submissions are received — whichever comes first. Digital nonfiction pitches open 1 September and 1 February each year for two weeks.",
     "windowStart": "2026-09-10", "windowEnd": "2026-09-15", "recurring": True},
    "prohibited",
    ["One poem per poet for the Spring 2027 Memory and Place issue, no longer than two single-spaced pages, guest-edited by Pádraig Ó Tuama with poetry editor Roger Reeves.",
     "Digital nonfiction pitches of up to 400 words — short essays, food pieces, enumerations, conversations, graphic stories and art portfolios.",
     "Full drafts for short digital pieces under 1,000 words, where a pitch is harder than just reading it.",
     "Work that expands or challenges an understanding of nature, culture and place."],
    ["AI-assisted work of any kind. Orion states this three separate times on the page, for print, digital and poetry alike.",
     "Straight exposés of environmental catastrophe, or conceptual work stretched to fit a nature theme.",
     "Submissions outside an open window — they state they have no capacity to consider them.",
     "Fiction, book reviews, op-eds or press releases."],
    ["Submittable", "Open window only", "One poem, max 2 pages", "No AI-assisted work"],
    "Not stated on the guidelines page.",
    ["Read https://orionmagazine.org/submission-guidelines/ and recent issues.",
     "For the poetry call, submit one poem between 10 and 15 September 2026 — it closes at 800 submissions.",
     "For digital nonfiction, watch the 1 September and 1 February two-week windows."],
    ["orion", "nature", "place", "poetry", "environment", "usa", "usd", "no ai"]),
]


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
            sys.exit(f"ERROR: duplicate slug in batch: {r['slug']}")
        seen.add(r["slug"])
        p = r["pay"]
        if p["amountMin"] == 0 or p["amountMax"] == 0:
            sys.exit(f"ERROR: {r['slug']} zero pay")
        if p["amountMin"] is not None and p["amountMax"] is not None and p["amountMin"] > p["amountMax"]:
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
        pc[r["slug"]] = {"base": "US", "label": "United States"}
    PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {len(NEW)} US records. Total: {len(opps)}")


if __name__ == "__main__":
    main()
