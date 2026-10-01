"""Add verified writing-market batch 19 (2026-10-01).

One NEW market, read off its own guidelines page on 2026-10-01. Raw text under
research/rebuild/raw/menagerie_magazine.txt.

WHY THIS ONE, AND NOT MIDNIGHT & INDIGO
---------------------------------------
Menagerie states a rate in its own words: "$50 per acceptance (e.g. one piece of
prose or one to three poems)". Midnight & indigo surfaced in the same pass on
"we pay for all accepted work", but the only pay figure on the page it points to
is a per-hour rate for a Writing Program teaching role - a job, not a contributor
rate. It is not recorded, because recording it would turn employment terms into a
rate for published work.

CLOSED, AND SAID SO WITHOUT A DATE
----------------------------------
Menagerie's status line reads: "Status: Menagerie is TEMPORARILY CLOSED for
submissions to catch up on our backlog. We will reopen as soon as we can." There
is no reopening date, so the record carries no deadline at all rather than a
placeholder, and the closure is stated in the requirements and how-to-submit text
where a writer will actually read it.
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
    "menagerie-magazine", "Menagerie",
    "Fiction, essays and poetry: $50 per acceptance, first serial rights",
    "Menagerie: $50 per acceptance, no reprints, 60-90 day reply",
    "Menagerie pays $50 per acceptance - one piece of prose or one to three poems - and "
    "acquires first serial rights. It publishes fictions, essays and poems that the "
    "editors describe as strange, wild and uncanny, takes stories and essays up to "
    "5,000 words, and allows simultaneous submissions with withdrawal. It refuses "
    "AI-written work outright, and is temporarily closed to catch up on its backlog.",
    "https://menageriemagazine.com/submissions",
    "https://menageriemagazine.com/submissions", None,
    "Online form through Submittable; submissions are temporarily closed while the "
    "magazine catches up on its backlog.",
    src("Menagerie - Submissions (official)",
        "https://menageriemagazine.com/submissions"),
    intl(),
    ["fiction", "essays", "poetry", "creative-nonfiction"],
    "Fiction, essays and poetry",
    pay("USD", 50, 50,
        "$50 per acceptance - one piece of prose or one to three poems",
        "Official page: \"We pay $50 per acceptance (e.g. one piece of prose or one to "
        "three poems) and acquire first serial rights. We do not republish work that "
        "has already appeared el[sewhere].\"",
        "Not publicly stated"),
    {"min": None, "max": 5000,
     "display": "Stories and essays up to 5,000 words, with 1,000-3,000 words "
                "published more often; poetry: three to five poems per submission"},
    {"label": "60-90 days", "band": "1-3-months", "official": True},
    "closed", None, "prohibited",
    ["Sentences \"so sharp they draw blood\" - fictions in the register of Borges, "
     "Link, Calvino and Sparks.",
     "Weird lyric essays, and writing engaged with the environment and natural world.",
     "Poems that explode form.",
     "Work the editors call strange, wild and uncanny, including pieces the writer "
     "is not sure what to call."],
    ["AI-written work: \"Absolutely no AI. We're interested in writing that reflects "
     "real, lived experience, not the hallucinations of LLMs.\"",
     "Work that has already appeared elsewhere - the magazine does not republish.",
     "Lukewarm prose, formulaic attempts at being on trend, conformity, pat endings "
     "and sentiment-drenched rhyming poems.",
     "Submissions to more than one category at a time.",
     "Stories or essays over 5,000 words."],
    ["Read https://menageriemagazine.com/submissions before sending.",
     "The magazine is temporarily closed to catch up on its backlog and says it will "
     "reopen as soon as it can; no reopening date is stated.",
     "Submit to one category at a time.",
     "Poetry: three to five poems in one submission, and tell the editors if one "
     "poem is taken elsewhere so the rest stay in consideration.",
     "Prose: up to 5,000 words.",
     "Expect a response within 60-90 days."],
    "Menagerie acquires first serial rights and does not republish work that has "
    "already appeared elsewhere.",
    ["Read https://menageriemagazine.com/submissions before sending.",
     "Check the status line first: submissions are temporarily closed while the "
     "magazine works through its backlog, with no reopening date stated.",
     "When it reopens, submit through the form on the page, to one category only.",
     "Send three to five poems, or a story or essay of up to 5,000 words.",
     "Withdraw a simultaneous piece immediately if it is accepted elsewhere."],
    ["menagerie", "$50 per acceptance", "first serial rights", "no ai",
     "no reprints", "weird fiction", "lyric essay", "simultaneous submissions",
     "60-90 day response"],
    "accepted",
    "Simultaneous submissions are allowed. If your work is accepted elsewhere, please "
    "withdraw it. "
    f"— https://menageriemagazine.com/submissions (read {READ})"))


BASE = {
    "menagerie-magazine": ("", "International"),
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
