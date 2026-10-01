"""Add verified writing-market batch 20 (2026-10-01).

One NEW market, read off its own guidelines page on 2026-10-01. Raw text under
research/rebuild/raw/missouri_review.txt.

THE TWO RATES ARE IN DIFFERENT UNITS, AND ARE KEPT APART
--------------------------------------------------------
The page states a page rate for the print journal - "Authors are paid $25 per
printed page" - and a per-piece rate for its online exclusive feature - "BLAST
authors are paid $100 per story." Averaging those into one number would misstate
both. The range runs 25 to 100 because that is the honest span of the two stated
figures, and the display names each one.

WHAT ELSE THE PAGE DID NOT SAY
------------------------------
No submission fee, no rights position and no payment timing are stated, so none
is recorded. Contest prizes on the same page ($5,000 Editors' Prize, $1,000 Poem
of the Year, $1,000 William Peden Prize, $250 runners-up) are outcomes, not rates,
and stay context. The AI position is unusual and is recorded as such: the magazine
does not ban AI, it requires detailed disclosure.

FEE-ONLY MARKETS READ IN THE SAME PASS, AND NOT RECORDED
--------------------------------------------------------
Beloit Fiction Journal ("we charge a ser[ial]" submission cost), Breakwater Review
($3 reading fee), Cola Literary Review (paid reading period, $3 fee), Flyway (a
nominal $3 per submission), Hole in the Head Review ($20 submission fee) and
Harpur Palate ($19 entry fee) all state a writer's cost and no contributor rate.
A fee is never a rate, and none of them states payment.
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
    "missouri-review", "The Missouri Review",
    "Fiction, poetry and essays: $25 per printed page; BLAST pays $100 a piece",
    "The Missouri Review: $25 a printed page, $100 for BLAST online exclusives",
    "The Missouri Review pays $25 per printed page for poetry, fiction and nonfiction, "
    "and $100 per story or essay accepted for BLAST, its online exclusive feature. It "
    "reads year-round with a 10-12 week response, accepts simultaneous submissions with "
    "notice, takes work by post as well as online, and requires any use of AI to be "
    "disclosed in detail rather than banning it. Its $5,000 Editors' Prize is a contest "
    "outcome, not the rate.",
    "https://missourireview.com/submissions/",
    "https://missourireview.com/submissions/", None,
    "Online through the submission manager, or by post with a cover letter and a "
    "self-addressed stamped envelope.",
    src("The Missouri Review - Submissions (official)",
        "https://missourireview.com/submissions/"),
    worldwide("Official page: no country restriction stated, and submissions by post "
              "are accepted. The page carries the University of Missouri's copyright "
              "line, which is where the US filing comes from."),
    ["fiction", "poetry", "essays", "creative-nonfiction", "reviews", "interviews"],
    "Poetry, fiction, nonfiction, interviews and omnibus reviews",
    pay("USD", 25, 100,
        "$25 per printed page for regular submissions; $100 per story or essay for "
        "BLAST online exclusives",
        "Official page: \"Authors are paid $25 per printed page.\" And, for the online "
        "feature: \"BLAST authors are paid $100 per story.\" and \"BLAST authors are "
        "paid $100 per essay.\" The two figures are different units - a page rate and "
        "a per-piece rate - and are kept apart here rather than averaged. Prize money "
        "($5,000 Editors' Prize, $1,000 Poem of the Year, $1,000 William Peden Prize) "
        "is a contest outcome and is not part of the rate.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "No length restrictions stated for fiction and nonfiction, though the "
                "editors suggest reading back issues; poetry features run 6-14 pages "
                "of poems from each of three poets per issue; interviews and omnibus "
                "reviews cover 3-6 recently published books"},
    {"label": "Ten to twelve weeks", "band": "1-3-months", "official": True},
    "open",
    {"display": "Open for submissions year-round, with no closing date stated; the "
                "2026 Jeffrey E. Smith Editors' Prize has a deadline of 1 October",
     "windowEnd": "2026-10-01", "recurring": True},
    "disclosure-required",
    ["Poetry, fiction and nonfiction of general interest; the page does not consider "
     "literary criticism.",
     "Interviews, and omnibus reviews of three to six recently published books that "
     "share a common feature or subject.",
     "Fiction and essays that do not fit a given issue may still be considered for "
     "BLAST, the online exclusive feature, which pays per piece.",
     "Work by post as well as online, if sent with a cover letter and a stamped, "
     "self-addressed envelope."],
    ["Literary criticism, which the page excludes.",
     "Work that has appeared elsewhere: only original, previously unpublished "
     "material is considered.",
     "Generative AI use that is not disclosed - the page requires specific detail in "
     "both the piece and the cover letter rather than banning AI outright.",
     "Mixing genres in one submission.",
     "Physical manuscripts sent without a self-addressed stamped envelope, which the "
     "page says are recycled without a response."],
    ["Read https://missourireview.com/submissions/ before sending.",
     "Submit through the submission manager, or by post with a cover letter and a "
     "self-addressed stamped envelope.",
     "Do not mix genres in the same submission.",
     "Disclose any use of artificial intelligence in detail, in the piece and in the "
     "cover letter.",
     "Allow 10-12 weeks for a standard response.",
     "Contest entries for the Editors' Prize close 1 October."],
    "Not stated on the submissions page.",
    ["Read https://missourireview.com/submissions/ before sending.",
     "Submit through the submission manager year-round, or post a manuscript with a "
     "cover letter and a self-addressed stamped envelope.",
     "Say in the cover letter if you want the work considered for BLAST, the online "
     "feature that pays $100 a piece.",
     "Keep each submission to one genre, and disclose any AI use in detail.",
     "Expect a reply in 10-12 weeks; contest entries close 1 October."],
    ["missouri review", "$25 per printed page", "$100 blast", "editors prize",
     "university of missouri", "no literary criticism", "disclose ai use",
     "simultaneous submissions", "postal submissions"],
    "accepted",
    "Simultaneous submissions are OK as long as you notify us if accepted elsewhere. "
    f"— https://missourireview.com/submissions/ (read {READ})"))


BASE = {
    "missouri-review": ("US", "United States"),
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
