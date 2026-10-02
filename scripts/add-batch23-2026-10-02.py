"""Add verified writing-market batch 23 (2026-10-02).

Two NEW markets, read off each publication's OWN page. Raw text under
research/rebuild/raw/<slug>.txt.

WHY THE DESK DATE IS 2026-10-02 AND THE RAW FILES SAY 2026-09-30
----------------------------------------------------------------
The crawl that fetched these two pages ran on 2026-09-30; the desk read them on
2026-10-02 and re-read both against the saved text before recording anything. The
figures are the ones on the pages as fetched, and the read date on the records is
the desk date of the batch.

THE FIGURE THAT IS A PRIZE, AND THE ONE THAT IS A FEE
------------------------------------------------------
The Lemonwood Quarterly is the awkward one. Its windows are branded as contests
with a $4.00 charge, and each published piece advances to a December final round
for the $1,000 and $500 prizes. But the payment for PUBLICATION is stated
separately and plainly: "Every three months, ten stories or plays are selected for
publication ... The authors are awarded $200 payment". So $200 is the rate, the
$4.00 is the writer's cost, and the two prizes are outcomes kept as context.

NO CLOSING DATE IS INVENTED
---------------------------
The Lemonwood page's listing carries a closing date that the text as read does not
capture - it renders as "Ends on $4.00". Rather than guess a date, the record
carries no deadline object at all and the requirements say the closing date is not
in the text as read.

Let me tell you a story ran a summer 2026 window, 15 July to 15 August, which had
closed by the read date; the record is closed and does not announce a next window
the page does not announce.
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-10-02"
READ = "2026-10-02"


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
    "let-me-tell-you-a-story", "Let me tell you a story",
    "Flash fiction: $10 CAD per accepted story, and they never charge a fee",
    "Let me tell you a story: $10 CAD per story, no fees, under 1,000 words",
    "Let me tell you a story pays $10 CAD for each accepted flash fiction piece and "
    "states that it never charges fees. Stories run under 1,000 words, one per writer, "
    "with the title required to begin \"Let me tell you a story...\", sent by email as "
    "a Google Doc or PDF. It asks for first electronic rights and the non-exclusive "
    "right to archive, leaves all other rights with the author, and replies in one to "
    "three months. The summer 2026 window ran 15 July to 15 August.",
    "https://letmetellthisstory.substack.com/p/submission-guidelines",
    "https://letmetellthisstory.substack.com/p/submission-guidelines",
    "lyw.write@gmail.com",
    "Email lyw.write@gmail.com with a brief message in the body; there is no "
    "submission form.",
    src("Let me tell you a story - Submission guidelines (official)",
        "https://letmetellthisstory.substack.com/p/submission-guidelines"),
    intl(),
    ["fiction"],
    "Flash fiction",
    pay("CAD", 10, 10, "$10 CAD per accepted story",
        "Official page: \"For our upcoming reading season, we offer $10 CAD per "
        "accepted story.\" And on cost: \"We never charge fees and we give each story "
        "careful attention.\"",
        "Not publicly stated"),
    {"min": None, "max": 1000,
     "display": "Flash fiction under 1,000 words, one story per writer, title must "
                "begin \"Let me tell you a story...\""},
    {"label": "One to three months", "band": "1-3-months", "official": True},
    "closed",
    {"display": "The summer 2026 call ran 15 July to 15 August 2026; the page "
                "describes the reading season as upcoming and does not announce the "
                "next window",
     "openingDate": "2026-07-15", "windowEnd": "2026-08-15", "recurring": False},
    "not-stated",
    ["Flash fiction across genres, subjects and perspectives; the guidelines are "
     "deliberately minimal.",
     "Writers both emerging and established, bringing new angles, experiences and "
     "styles.",
     "Work that brings something fresh to its genre and avoids predictable or "
     "clichéd approaches."],
    ["Predictable, generic or clichéd approaches - the page asks for something fresh.",
     "More than one story per writer.",
     "Pieces of 1,000 words or more - the limit is under 1,000.",
     "A title that does not begin with \"Let me tell you a story...\"."],
    ["Read the guidelines at "
     "https://letmetellthisstory.substack.com/p/submission-guidelines before sending.",
     "Send to lyw.write@gmail.com - there is no submission form, so include a brief "
     "message in the email body with your name and a short introduction.",
     "Attach the story as a Google Doc or PDF.",
     "Keep it under 1,000 words, one story per writer, with the title beginning "
     "\"Let me tell you a story...\".",
     "There is no fee."],
    "First electronic rights and the non-exclusive right to archive the story on the "
    "site are requested; all other rights remain with the author, and the writer is "
    "free to republish after publication with a credit.",
    ["Read the guidelines page before sending.",
     "Email the story to lyw.write@gmail.com with a short introduction in the body.",
     "Attach a Google Doc or PDF, under 1,000 words, one story per writer.",
     "Use the required title opening: \"Let me tell you a story...\"",
     "Expect one to three months for a response, and note the summer window ran 15 "
     "July to 15 August."],
    ["let me tell you a story", "$10 cad per story", "flash fiction",
     "under 1000 words", "no fees", "substack", "first electronic rights",
     "required title opening"],
    "not-stated", None))

NEW.append(rec(
    "lemonwood-quarterly", "The Lemonwood Quarterly",
    "Fiction and plays: $200 paid per published piece, $4 to enter",
    "The Lemonwood Quarterly: $200 on publication, $4 entry, 2,000-10,000 words",
    "The Lemonwood Quarterly pays $200 for each story or play it selects for "
    "publication, ten per quarterly issue, with a $4.00 charge per submission that is "
    "the writer's cost. Published pieces also advance to a December final round for "
    "the $1,000 and $500 prizes. It takes fiction and plays of 2,000 to 10,000 words, "
    "welcomes writers of every nationality, refuses machine-generated text, and "
    "answers within thirty days of each window.",
    "https://thelemonwoodquarterly.submittable.com/submit",
    "https://thelemonwoodquarterly.submittable.com/submit", None,
    "Online form through Submittable; Word or PDF only.",
    src("The Lemonwood Quarterly - Submissions (official)",
        "https://thelemonwoodquarterly.submittable.com/submit"),
    worldwide("Official page: \"We welcome and encourage submissions from writers of "
              "every gender, age, race, ethnicity, sexuality, and nationality - "
              "including writers without MFA degrees or previously published work.\""),
    ["fiction", "drama"],
    "Short stories and plays",
    pay("USD", 200, 200,
        "$200 payment per story or play selected for publication",
        "Official page: \"Every three months, ten stories or plays are selected for "
        "publication in that season's issue of The Lemonwood Quarterly. The authors "
        "are awarded $200 payment, and their short story advances to the final round "
        "in December for consideration for the $1000 Charlotte Ann Porter Prize for "
        "Fiction.\" Each submission window charges $4.00, which is the writer's cost "
        "and is not part of the rate. The $1,000 fiction prize and the $500 play "
        "prize are contest outcomes, not rates.",
        "On publication"),
    {"min": 2000, "max": 10000,
     "display": "Stories and plays of 2,000 to 10,000 words; no poetry, flash "
                "fiction, nonfiction or other prose; up to four submissions a year, "
                "one per quarterly issue"},
    {"label": "Within thirty days of the window deadline", "band": "1-3-months",
     "official": True},
    "open", None, "prohibited",
    ["Superbly written short stories and plays; the magazine looks for English-language "
     "work of 2,000 to 10,000 words.",
     "Stories with female protagonists well into adulthood, which the page says it "
     "especially seeks.",
     "Writers of every gender, age, race, ethnicity, sexuality and nationality, "
     "including writers without MFA degrees or prior publications."],
    ["Work that includes machine-generated or AI text.",
     "Poetry, flash fiction, nonfiction prose and other forms - the page excludes them "
     "by name.",
     "Work previously published in any form, including online, in blogs or in print.",
     "More than one submission per quarterly issue, or more than four a year.",
     "A simultaneous submission accepted elsewhere without immediate withdrawal."],
    ["Read https://thelemonwoodquarterly.submittable.com/submit before sending.",
     "Submit through the quarterly contest window on Submittable; Word document or PDF.",
     "Keep the piece between 2,000 and 10,000 words, and submit only fiction or a "
     "play.",
     "Pay the $4.00 charge per submission, or check the page for any free window.",
     "Withdraw immediately if a simultaneous piece is accepted elsewhere.",
     "Note that the page's own listing does not show the window's closing date in the "
     "text as read, so no closing date is recorded here."],
    "The publishing agreement grants The Lemonwood Quarterly first worldwide "
    "electronic publication rights and non-exclusive online rights, with copyright "
    "retained by the author.",
    ["Read the submissions page and its guidelines before sending.",
     "Submit through the current quarterly window on Submittable - the page lists "
     "Fall 2026 fiction and playscript windows, and its listing does not show a "
     "closing date in the text as read.",
     "Send fiction or a play of 2,000 to 10,000 words as a Word document or PDF.",
     "Note the $4.00 charge per submission and the $200 payment on publication."],
    ["lemonwood quarterly", "$200 payment", "$4.00 entry", "short stories",
     "plays", "charlotte ann porter prize", "no ai", "submit table",
     "simultaneous submissions"],
    "accepted",
    "Simultaneous Submissions to other publications are fine, but please withdraw "
    "your submission immediately if your work is accepted elsewhere. "
    f"— https://thelemonwoodquarterly.submittable.com/submit (read {READ})"))


BASE = {
    "let-me-tell-you-a-story": ("", "International"),
    "lemonwood-quarterly": ("", "International"),
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
