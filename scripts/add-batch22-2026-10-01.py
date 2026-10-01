"""Add verified writing-market batch 22 (2026-10-01).

One NEW market, read off its own guidelines page on 2026-10-01. Raw text under
research/rebuild/raw/black_warrior_review.txt.

A PAYING MARKET WITH NO PUBLISHED FIGURE
----------------------------------------
Black Warrior Review says it pays - twice, in as many words: "Black Warrior Review
is a paying market" and "We always pay our contributors" - and then explains why
no number can be quoted: "The amount per contributor or piece is dependent on our
overall number of contributors for a given issue, and the budget allocated to us
by our presiding office at the University of Alabama, the Office of Student
Media." The record therefore carries null amounts and a display that says the
amount is not published, which is the same shape used for American Short Fiction
("Payment is competitive") in batch 14. Inventing a figure, or leaving the market
out because there is no figure, would both be wrong: the page is unambiguous that
contributors are paid.

THE FEE IS MENTIONED AND NOT QUANTIFIED
---------------------------------------
The page refers to a submission fee with waivers, including free submissions for
incarcerated writers, but publishes no fee amount in the text as read. No fee
figure is recorded. The $15 and $25 figures on the page are subscription prices,
not submission costs.
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
    "black-warrior-review", "Black Warrior Review",
    "Poetry, prose and comics from a paying market - amount not published",
    "Black Warrior Review: a paying market with the amount left unpublished",
    "Black Warrior Review states plainly that it pays contributors, and equally "
    "plainly that the amount depends on how many contributors an issue carries and "
    "the budget its university office allocates - so no figure can be quoted and none "
    "is. It reads poetry, prose, comics and hybrid work in winter and summer windows, "
    "takes prose up to 6,000 words, notes simultaneous submissions, reverts rights on "
    "publication, and will not consider AI-assisted work.",
    "https://bwr.submittable.com/submit", "https://bwr.submittable.com/submit",
    None, "Online through the submission manager; fee waivers are available on request.",
    src("Black Warrior Review - General submissions (official)",
        "https://bwr.submittable.com/submit"),
    intl("Official page: no country restriction stated. The magazine is staffed by "
         "graduate students at the University of Alabama and carries the university's "
         "copyright line, which is where the US filing comes from."),
    ["poetry", "fiction", "creative-nonfiction", "other"],
    "Poetry, prose, comics, art, nonfiction and hybrid work",
    pay(None, None, None, "Payment stated, amount not published",
        "Official page: \"Black Warrior Review is a paying market. The amount per "
        "contributor or piece is dependent on our overall number of contributors for "
        "a given issue, and the budget allocated to us by our presiding office at the "
        "University of Alabama, the Office of Student Media.\" Also: \"We always pay "
        "our contributors.\" The page also mentions a submission fee with waivers but "
        "publishes no fee amount, so none is recorded.",
        "Not publicly stated"),
    {"min": None, "max": 6000,
     "display": "Prose up to 6,000 words, with nonfiction limited to 4,000 words; "
                "poetry, comics, art and hybrid work also read"},
    {"label": "Three to six months", "band": "3-plus-months", "official": True},
    "closed",
    {"display": "Reads in two windows a year, predominantly 15 December to 1 March "
                "and 1 June to 30 September - so the summer window closed on 30 "
                "September 2026 and the winter window opens 15 December 2026. The "
                "page warns the dates are liable to change as the masthead turns over",
     "openingDate": "2026-12-15", "windowEnd": "2027-03-01", "recurring": True},
    "prohibited",
    ["Poetry - the page says it believes poetry is the history of words.",
     "Fiction the editors describe as unreal, nonfiction that can be uncertain of "
     "itself, comics, art and hybrid work.",
     "Work of up to 6,000 words for prose, and 4,000 words for nonfiction.",
     "Simultaneous submissions, if noted as such."],
    ["Work translated, written, developed or assisted by AI writing tools: the page "
     "names ChatGPT and states it will consider none.",
     "Previously published work.",
     "Prose beyond the stated limits - the journal is print and the page notes its "
     "physical space is limited.",
     "Simultaneous work that is accepted elsewhere without withdrawal."],
    ["Read the general guidelines at https://bwr.submittable.com/submit before "
     "sending.",
     "Submit through the submission manager only.",
     "Send during a reading window: predominantly 15 December to 1 March and 1 June "
     "to 30 September, though the page warns the dates can shift.",
     "Note simultaneous submissions as such, and withdraw immediately on acceptance "
     "elsewhere.",
     "Request a fee waiver if the submission fee is a hardship; free submissions are "
     "available for incarcerated writers.",
     "Allow three to six months for a response."],
    "Rights revert to the author upon publication.",
    ["Read https://bwr.submittable.com/submit before sending.",
     "Submit through the submission manager during a window - general submissions "
     "are between windows now, with the winter period opening 15 December 2026.",
     "Keep prose within 6,000 words and nonfiction within 4,000.",
     "Note simultaneous submissions and withdraw on acceptance elsewhere.",
     "Ask for a fee waiver if the fee is a barrier; the page says it grants them."],
    ["black warrior review", "paying market", "university of alabama",
     "no ai", "simultaneous submissions", "rights revert",
     "winter and summer reading periods", "submittable", "comics"],
    "accepted",
    "Simultaneous submissions are welcome, if noted, and please notify us immediately "
    "if the work is accepted somewhere else. "
    f"— https://bwr.submittable.com/submit (read {READ})"))


BASE = {
    "black-warrior-review": ("US", "United States"),
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
