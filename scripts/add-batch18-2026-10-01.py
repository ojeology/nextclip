"""Add verified writing-market batch 18 (2026-10-01).

One NEW market, read off its own guidelines page on 2026-10-01. Raw text under
research/rebuild/raw/maine_review.txt.

WHY ONE
-------
The batch-17 queue has thinned: of the pages left unshipped after the slug
normalisation fix, the rest state no contributor rate at all. The newly fetched
names (Mania, MAP Literary, Maudlin House, Ranger, Marrow, Massachusetts Review,
Poetry Is Currency) carry no pay language on their pages as read, and three of
them are JavaScript walls of under 200 characters recorded as not established
rather than as unpaid.

WHAT THIS RECORD HAD TO AVOID
-----------------------------
  * The $3 submission fee is the writer's cost - "of which we receive $1.86" -
    and is kept out of the rate.
  * The free windows are real and are recorded, because a writer who can wait for
    one does not have to pay the fee at all.
  * The artwork call pays $50 on publication. That is a contributor rate for a
    different route, quoted in the conditions rather than averaged into a prose
    figure.
  * No sentence on the page states the review's country, so it is filed with no
    base country rather than guessed from the name.
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-10-01"
READ = "2026-10-01"


def rec(slug, publication, title, seo, excerpt, official, apply_url, apply_email,
        apply_method, sources, elig, types, type_label, pay, wc, response,
        status, deadline, ai, want, dont, reqs, rights, how, keywords,
        sim="not-stated", simnote=None):
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
        "simultaneousSubmissions": sim, "simultaneousNote": simnote,
    }


def src(name, url):
    return [{"name": name, "url": url}]


def pay(cur, lo, hi, display, conditions, timing):
    return {"currency": cur, "amountMin": lo, "amountMax": hi,
            "display": display, "conditions": conditions, "timing": timing}


def intl(summary="No stated country restriction on the guidelines page."):
    return {"summary": summary, "mode": "not-stated", "includesRegions": [],
            "allowsDiaspora": True, "notStated": True}


def worldwide(summary):
    return {"summary": summary, "mode": "worldwide", "includesGroups": [],
            "includesRegions": [], "allowsDiaspora": True, "notStated": False}


NEW = []
NEW.append(rec(
    "maine-review", "The Maine Review",
    "Prose: $25 per flash, $50 over 1,000 words; poetry $25 a poem",
    "The Maine Review: $25-$50 per piece, $3 to submit, free windows",
    "The Maine Review pays a $25 honorarium per published flash piece and per poem, and "
    "$50 for prose of 1,001 words or more; artwork is paid $50 on publication. It reads "
    "1 September to 30 November, alongside two other windows, and asks $3 per "
    "submission - the fee is the writer's cost. One prose piece of up to 3,000 words or "
    "three flashes, up to three poems, simultaneous work accepted with immediate "
    "withdrawal, and AI-generated writing refused.",
    "https://mainereview.submittable.com/submit",
    "https://mainereview.submittable.com/submit", None,
    "Online form through Submittable; one submission at a time.",
    src("The Maine Review - Submissions (official)",
        "https://mainereview.submittable.com/submit"),
    intl("Official page: no country restriction stated, and no sentence on the page "
         "states the review's country. Submitters are asked to wait a year after a "
         "publication before sending again."),
    ["fiction", "creative-nonfiction", "poetry", "translation"],
    "Fiction, nonfiction, poetry, translation and hybrid forms",
    pay("USD", 25, 50,
        "$25 per published flash piece or poem, $50 for prose of 1,001 words or more",
        "Official page, Writer Payment: \"Fiction and Nonfiction writers receive a $25 "
        "honorarium per published flash (1,000 words or fewer) and a $50 honorarium "
        "for work 1,001 words or more. Poets receive a $25 honorarium per published "
        "poem.\" On the artwork call: \"Contributors are paid $50 upon publication.\" "
        "The page also asks a $3 fee per submission - \"of which we receive $1.86\" - "
        "which is the writer's cost and is not part of the rate.",
        "On publication"),
    {"min": None, "max": 3000,
     "display": "Prose: one piece of 3,000 words or fewer, though longer works of "
                "exceptional merit are considered, or three flash pieces of no more "
                "than 1,000 words each. Poetry: up to three poems, five pages total."},
    {"label": "Six months or longer", "band": "3-plus-months", "official": True},
    "open",
    {"display": "Open 1 September to 30 November, one of three annual windows (1 "
                "January-31 March, 1 May-30 June, 1 September-30 November); free "
                "submissions also run 28 September to 5 October for Hispanic Heritage "
                "Month",
     "openingDate": "2026-09-01", "windowEnd": "2026-11-30", "recurring": True},
    "prohibited",
    ["Contemporary fiction, nonfiction and poetry, including work in translation and "
     "hybrid forms.",
     "New, emerging and established writers; the page states a commitment to "
     "representation, innovation and literary artistry.",
     "Artwork - photography, illustration and other forms - for the cover and section "
     "openings.",
     "The free submission windows the review runs to keep the magazine accessible."],
    ["AI-generated work: \"We do not publish AI-generated work. Such work will be "
     "automatically declined.\"",
     "Multiple submissions at a time - the page says it cannot refund them.",
     "Submitting again within a year of having work published in the review.",
     "Querying before six months have passed."],
    ["Read the general guidelines before submitting.",
     "Submit through Submittable, one submission at a time.",
     "Pay the $3 per-submission fee, or use a free window - 28 September to 5 October "
     "ran free for Hispanic Heritage Month.",
     "Prose: one piece up to 3,000 words or three flash pieces of no more than 1,000 "
     "words each; poetry: up to three poems and five pages.",
     "Format prose in 12-point Times New Roman, double-spaced, numbered pages, and "
     "include the word count in the cover letter.",
     "Address the cover letter to the genre editor, and allow six months before "
     "querying."],
    "Not stated on the guidelines page.",
    ["Read the general guidelines before sending.",
     "Submit through the Submittable form during a reading window - 1 September to 30 "
     "November is open.",
     "Check whether a free submission window is running before paying the $3 fee.",
     "Send one submission at a time, with the word count in the cover letter.",
     "Withdraw immediately if a simultaneous piece is accepted elsewhere, and wait a "
     "year after publication before sending again."],
    ["the maine review", "$25 per flash", "$50 honorarium", "$3 submission fee",
     "free submission window", "hispanic heritage month", "no ai",
     "simultaneous submissions", "submittable"],
    "accepted",
    "We encourage simultaneous submissions, but please withdraw your submission "
    "immediately if it is accepted elsewhere. "
    f"— https://mainereview.submittable.com/submit (read {READ})"))


BASE = {
    "maine-review": ("", "International"),
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
        # A zero is a figure that was never read off a page. Batch 4 shipped one
        # and it had to be found and removed; here it cannot be written.
        if p["amountMin"] == 0 or p["amountMax"] == 0:
            sys.exit(f"ERROR: {r['slug']} has a zero pay amount")
        if p["amountMin"] is not None and p["amountMax"] is not None \
                and p["amountMin"] > p["amountMax"]:
            sys.exit(f"ERROR: {r['slug']} pay range inverted")
        if p["amountMin"] is None and p["amountMax"] is not None:
            sys.exit(f"ERROR: {r['slug']} has a maximum but no minimum")
        for k in ("officialUrl", "excerpt", "seoTitle", "howToSubmit", "whatTheyWant"):
            if not r.get(k):
                sys.exit(f"ERROR: {r['slug']} missing {k}")
        # deadline is a structured object in this dataset (display/date/
        # openingDate/windowStart/windowEnd/recurring), never a bare string.
        # build-writing-first.py's deadline_passed() calls .get() on it, so a
        # string crashes the build. Batch 13 shipped three string deadlines and
        # the build caught them; this guard is why they cannot come back.
        dl = r["deadline"]
        if dl is not None:
            if not isinstance(dl, dict):
                sys.exit(f"ERROR: {r['slug']} deadline must be a dict or None, "
                         f"got {type(dl).__name__}")
            if not dl.get("display"):
                sys.exit(f"ERROR: {r['slug']} deadline has no display text")
            if not any(k in dl for k in ("date", "openingDate", "windowEnd")):
                sys.exit(f"ERROR: {r['slug']} deadline records no date of any kind")
        if r["simultaneousSubmissions"] not in ("accepted", "not-accepted", "not-stated"):
            sys.exit(f"ERROR: {r['slug']} bad simultaneous value")
        if r["simultaneousSubmissions"] == "not-stated" and r["simultaneousNote"]:
            sys.exit(f"ERROR: {r['slug']} has a note but says not-stated")
        if r["simultaneousSubmissions"] != "not-stated" and not r["simultaneousNote"]:
            sys.exit(f"ERROR: {r['slug']} states a policy with no sentence recorded")
        # Every policy note in this dataset is a verbatim sentence plus its source
        # and the date it was read. The date must be the desk date of THIS batch.
        if r["simultaneousNote"] and f"(read {READ})" not in r["simultaneousNote"]:
            sys.exit(f"ERROR: {r['slug']} simultaneous note carries no read date")
        # The pay display must never be a fee dressed as a rate.
        for word in ("fee", "entry", "Fast Pass"):
            if word.lower() in (p["display"] or "").lower():
                sys.exit(f"ERROR: {r['slug']} pay display mentions '{word}' - "
                         f"a writer's cost is not a rate")

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
# Read in this batch and HELD BACK, with the reason. Held is not the same as
# rejected: most of these are real markets that pay nothing, and the index policy
# for this desk is research-backed PAID opportunities.
#
#   apricity_press        "There is no submissions fee, nor is there any payment
#       for publishing your work (currently)." Unpaid. (The $5 option buys a
#       one-week response; it is a writer's cost, not a rate.)
#   amsterdam_review      "We are unable to offer paid compensation for accepted
#       submissions at present." Unpaid.
#   after_brunch_journal  "volunteer-based, so unfortunately we are not able to
#       offer payment to our contributors at this time". Unpaid.
#   appalachia            "We have a very limited budget and cannot pay for most
#       unsolicited material. Authors receive two contributor copies." Mostly
#       unpaid; the rest of the page's payment language is subscription billing.
#   aaduna                "aaduna does not provide publishing honorarium nor
#       charges any fee". Unpaid, as batch 13 already recorded.
#   atlantic_northeast    "right now we are unable to pay contributors for their
#       work." Unpaid.
#   autumn_sky_poetry_daily  "There is no payment for contributors." Unpaid.
#   acorn_review          $5 reading fee, no contributor rate stated on the page.
#   allium_a_journal_of_poetry_prose  $3.00 reading fee, window opens 13 November
#       2026; no contributor rate stated on the page.
#   alaska_quarterly_review  "The fee is $3." No contributor rate stated.
#   anomaly (ANMLY)       $3 submission fee with a hardship waiver; no contributor
#       rate stated.
#   arkana                The $50 figures are Editors' Choice Awards and an
#       Arkansas Writers prize. A prize is not a rate for published work - the
#       StoryQuarterly precedent from batch 12.
#   bacopa_literary_review  $2 submission fee and cash awards by category. Contest
#       money, not a contributor rate.
#   acdc_a_journal_for_the_bent  $5 tip jar buys a faster response. A writer's
#       cost, and no rate is stated.
#   antiphony             The only "$" strings on the page are Squarespace
#       newsletter-template boilerplate. No contributor rate found.
#   aura_literary_arts_review  The $10/$15/$25/$50 figures are donation buttons.
#
# Read later in the run and not yet classified when this batch shipped: the queue
# continues under research/rebuild/ with scripts/read-pw-candidates.py.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    raise SystemExit(main())
