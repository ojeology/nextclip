"""Add verified writing-market batch 15 (2026-10-01).

Three NEW markets, read off each publication's OWN guidelines page on 2026-10-01.
The raw text of every page is kept under research/rebuild/raw/<slug>.txt so a
reading can be re-checked without re-fetching.

WHERE THESE CANDIDATES CAME FROM
--------------------------------
pw.org's Literary Magazines directory, for names and official submission URLs
only, exactly as in batches 4, 13 and 14:

    the batch-14 queue, resumed on the side branch
    -> candidates not already on this desk
    -> each publication's OWN guidelines page fetched and read

pw.org's own pay notes and reading-fee flags were not read and are not used. Every
figure below comes from the publication's own page.

WHAT WAS READ, AND WHAT WAS NOT FLATTENED
-----------------------------------------
All three pay a stated rate. Three of this batch's dollar figures are NOT rates,
and are recorded as what they are:

  * Colorado Review charges $3 on online submissions, and its own page never states
    when payment arrives. The $3 is the writer's cost. The same page lists
    advertising space at $150 a whole page and $75 a half page, under a "Deadlines"
    heading whose dates are advertising booking dates - a careless read turns an
    advertiser's cost into a contributor rate and an ad deadline into a submission
    deadline.
  * The Fairy Tale Magazine pays $25 USD a piece and runs a separate contest whose
    first prize is $100 USD. Contest prize money is context, never the rate, and
    the contest carries its own charges.
  * Gavialidae's page states its rates and nothing about rights, fees or AI. Those
    are recorded as not stated rather than filled in from the magazine's reputation.

WHY THIS BATCH IS SMALLER THAN BATCH 14
---------------------------------------
Batch 14 shipped six because that queue had been read hard before it. This batch
ships three and holds the rest: every other candidate read in the same pass is
either unpaid, fee-only, or states its rate only on a route this desk cannot yet
describe without flattening it. They are carried forward by name below rather than
forced in to make a round number.

HELD OPEN, NOT REJECTED
-----------------------
The queue continues under research/rebuild/ with scripts/read-pw-candidates.py.
Frontier Poetry pays $50 a poem but only on named routes ("partner poets", "New
Voices") alongside a separate $20-fee challenge; Half Mystic Journal states US$20
a piece with an April 2027 close; CutBank's $250 is for cover art. Each needs its
own careful reading before it is recorded.
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
    "colorado-review", "Colorado Review",
    "Short stories and essays: $300; poetry: $100 for each poet in the issue",
    "Colorado Review: $300 for stories and essays, $100 for poems",
    "Colorado Review pays $300 for short stories and nonfiction, a flat $100 to each "
    "poet featured, and $100 for cover photography. Fiction and poetry are read 1 "
    "August to 31 March and nonfiction year-round, with a $3 charge on online "
    "submissions. Simultaneous submissions are accepted with immediate notice, and "
    "first North American serial rights revert to the author on publication.",
    "https://coloradoreview.colostate.edu/colorado-review/#submission-guidelines",
    "https://coloradoreview.colostate.edu/colorado-review/#submission-guidelines",
    None, "Online form through Submittable. Paper submissions are no longer accepted.",
    src("Colorado Review - Submission guidelines (official)",
        "https://coloradoreview.colostate.edu/colorado-review/#submission-guidelines"),
    worldwide("Official page: \"Authors do NOT need to be residents of Colorado or the "
              "United States.\" Colorado State University faculty, staff and students "
              "are excluded, and alumni may submit three years after leaving."),
    ["fiction", "essays", "poetry", "creative-nonfiction", "reviews"],
    "Short fiction, personal essays, poetry, book reviews and cover photography",
    pay("USD", 100, 300,
        "$300 per short story or essay, $100 per poet, $100 for cover photography",
        "Official page: \"Colorado Review pays its writers and artists: $300 for short "
        "stories and nonfiction; $100 for poetry; and $100 for cover photography.\" "
        "And: \"We pay our poets a flat fee of $100 and we pay $300 for short stories "
        "and essays.\" The $3 charged on online submissions is the writer's cost and "
        "is not part of the rate.",
        "Not publicly stated"),
    {"min": None, "max": None,
     "display": "Stories and essays of 15-25 manuscript pages, one piece at a time; "
                "poetry up to 7 poems and 20 pages, with single long poems up to 10 pages"},
    {"label": "Not publicly stated", "band": "not-stated", "official": False},
    "open",
    {"display": "Fiction and poetry are read 1 August to 31 March; nonfiction is read "
                "year-round and photography for cover art is open now",
     "openingDate": "2026-08-01", "windowEnd": "2027-03-31", "recurring": True},
    "not-stated",
    ["Short fiction and personal essays with contemporary themes; the editors say they "
     "are equally interested in work by new and established writers.",
     "Poetry of any style - about fifteen poets are featured in each issue.",
     "Cover art photography, now open for submissions."],
    ["Flash fiction and flash nonfiction, which are not accepted.",
     "Scholarly essays and literary criticism.",
     "More than one story or essay at a time, or more than one group of poems.",
     "Lines longer than 65 characters, which the print page cannot fit.",
     "Work by current or emeritus CSU faculty, staff or students.",
     "A second submission while an earlier one is still awaiting a response.",
     "Work published in Colorado Review within the last two years."],
    ["Read the guidelines at "
     "https://coloradoreview.colostate.edu/colorado-review/#submission-guidelines "
     "before sending.",
     "Submit online through Submittable; paper submissions are no longer accepted.",
     "Fiction and poetry: send one piece at a time, from 1 August to 31 March. "
     "Nonfiction is read year-round.",
     "Poetry: up to 7 poems totalling no more than 20 pages; a single long poem may "
     "run to 10 pages.",
     "Translations need proof of permission to translate.",
     "Wait until you have a response before submitting again."],
    "Colorado Review purchases First North American Serial Rights, and all rights "
    "revert to the author upon publication in CR.",
    ["Read the guidelines page before sending.",
     "Submit through the Submittable portal linked from the guidelines; email and "
     "paper submissions are not accepted.",
     "Fiction and poetry are read 1 August to 31 March; nonfiction is read year-round.",
     "Book reviews go through Submittable and carry no charge.",
     "Simultaneous submissions are accepted - tell the editors immediately if the "
     "work is taken elsewhere."],
    ["colorado review", "$300 short stories", "$100 poetry", "colorado state university",
     "print journal", "submittable", "first north american serial rights",
     "simultaneous submissions", "no flash fiction"],
    "accepted",
    "Simultaneous submissions are accepted; writers must notify us immediately if the "
    "work is accepted elsewhere. "
    f"— https://coloradoreview.colostate.edu/colorado-review/ (read {READ})"))

NEW.append(rec(
    "gavialidae", "Gavialidae",
    "Poetry and flash fiction: $150; short stories and essays: $500",
    "Gavialidae: $150 per poem or flash, $500 per story or essay",
    "Gavialidae pays $150 per poem or flash fiction piece and $500 per short story or "
    "essay, reading unpublished work year-round through Duosuma. A submission carries "
    "no more than one story or essay, four flash fictions or ten poems, and nothing "
    "over 7,500 words. Simultaneous submissions are welcome, replies take about five "
    "months, and the page states no AI policy.",
    "https://gavialidae.com/submissions",
    "https://gavialidae.com/submissions",
    None, "Online form through Duosuma, with a brief biographical note.",
    src("Gavialidae - Submissions (official)", "https://gavialidae.com/submissions"),
    intl(),
    ["poetry", "fiction", "creative-nonfiction"],
    "Poetry, flash fiction, short stories and creative nonfiction",
    pay("USD", 150, 500,
        "$150 per poem or flash fiction piece, $500 per short story or essay",
        "Official page: \"Regarding work accepted for publication, we pay $150 per "
        "poem or flash fiction piece and $500 per short story or essay.\"",
        "Not publicly stated"),
    {"min": None, "max": 7500,
     "display": "No unsolicited submission longer than 7,500 words; up to 1 short "
                "story or essay, 4 flash fictions or 10 poems"},
    {"label": "Five months", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Unpublished fiction, poetry and creative nonfiction, read all year round.",
     "Shorter work: poems and flash fiction are paid per piece at the same rate.",
     "Pieces sent between 1 January and 31 July, which the page says are more likely "
     "to be considered for the current issue."],
    ["Anything longer than 7,500 words.",
     "More than one short story or essay, four flash fictions or ten poems in a "
     "single submission.",
     "Work sent to the contact email, which the page says will not be read."],
    ["Read https://gavialidae.com/submissions before sending.",
     "Submit through Duosuma, year-round.",
     "Include a brief biographical note.",
     "Keep to the stated limits: 1 story or essay, 4 flash fictions or 10 poems, and "
     "nothing over 7,500 words.",
     "Say so if a piece is also out elsewhere."],
    "Not stated on the guidelines page.",
    ["Read https://gavialidae.com/submissions before sending.",
     "Submit through Duosuma; the page notes that submissions sent to the contact "
     "email will not be read.",
     "Send no more than 1 short story or essay, 4 flash fictions or 10 poems, and "
     "nothing over 7,500 words.",
     "Include a brief biographical note.",
     "Expect a reply within five months, and note that pieces sent between 1 January "
     "and 31 July are likelier to be considered for the current issue.",
     "Tell the editors if a piece is submitted elsewhere."],
    ["gavialidae", "$150 per poem", "$500 per story", "flash fiction",
     "creative nonfiction", "duosuma", "simultaneous submissions",
     "7500 word limit"],
    "accepted",
    "Simultaneous submissions are welcome, but do inform us if a piece has been "
    "submitted elsewhere. "
    f"— https://gavialidae.com/submissions (read {READ})"))

NEW.append(rec(
    "fairy-tale-magazine", "The Fairy Tale Magazine",
    "Poetry and prose: $25 USD for every piece the magazine publishes",
    "The Fairy Tale Magazine: $25 USD per published poem or story",
    "The Fairy Tale Magazine pays $25 USD for each poem and prose piece it publishes, "
    "and its fall call is free to enter. Stories run 900-2,000 words and poems up to "
    "500 words, one piece per submission period, in a window that runs 15-21 August. "
    "Work from any country is welcome, the magazine does not read work made with AI, "
    "and simultaneous submissions are accepted with notice.",
    "https://fairytalemagazine.com/submissions",
    "https://fairytalemagazine.com/submissions",
    None, "Online Google Form only; the link appears on the page when submissions are open.",
    src("The Fairy Tale Magazine - Submissions (official)",
        "https://fairytalemagazine.com/submissions"),
    worldwide("Official page: \"We are happy to read and publish work from any "
              "country, and are open to work with a wide range of backgrounds and "
              "experiences.\""),
    ["poetry", "fiction"],
    "Fairy-tale short stories and poetry",
    pay("USD", 25, 25,
        "$25 USD per published poem or prose piece",
        "Official page: \"We pay $25USD for each poem and prose piece we publish.\" "
        "And: \"We pay $25 USD per piece (whether prose or poetry).\" The fall call "
        "is described as a \"Fall no-fee call for submissions\"; the contest's own "
        "charges and its $100 USD first prize are separate and are not the rate.",
        "Not publicly stated"),
    {"min": 900, "max": 2000,
     "display": "Short stories 900-2,000 words; poetry up to 500 words; one piece per "
                "submission period"},
    {"label": "About a month after the window closes", "band": "1-3-months",
     "official": True},
    "closed",
    {"display": "Submission window: 15-21 August (midnight to midnight EST), for the "
                "fall issue that launches 1 November; the 2026 window closed on 21 "
                "August and chosen authors were notified on or around 22 September 2026",
     "openingDate": "2026-08-15", "windowEnd": "2026-08-21"},
    "prohibited",
    ["Fairy-tale stories and poems on the announced theme - the fall call was Food in "
     "Fairy Tales.",
     "Work with an element of the supernatural and a transformation at its heart; "
     "mashups are welcomed.",
     "Previously unpublished stories of 900-2,000 words and poems of up to 500 words."],
    ["Work made with AI: the page says AI-generated submissions are equal to "
     "plagiarized work.",
     "Sci-fi, time travel, futuristic or space travel stories, high fantasy, erotica, "
     "stage magic, dystopian work, extreme horror or gore, westerns and lengthy "
     "gross-out description.",
     "Anything above PG - the page notes that children find the site.",
     "Previously published work, or more than one piece in a submission period.",
     "Work from anyone under 18."],
    ["Read https://fairytalemagazine.com/submissions before sending.",
     "Submit through the Google Form only; it appears on the page while the window "
     "is open.",
     "One piece per submission period: a story of 900-2,000 words or a poem of up to "
     "500 words.",
     "Include a third-person biography of 50 words or fewer.",
     "You must be 18 or older to submit.",
     "Email the magazine with WITHDRAW in the subject line if a simultaneous piece "
     "is accepted elsewhere."],
    "First and all electronic and digital rights are sought, along with rights to use "
    "the work to promote The Fairy Tale Magazine in perpetuity; electronic and "
    "digital rights revert to the author immediately after publication.",
    ["Read https://fairytalemagazine.com/submissions before sending.",
     "Submit through the Google Form; the link appears only while the submission "
     "window is open.",
     "Send one piece: a story of 900-2,000 words or a poem of up to 500 words.",
     "Include a 50-word third-person bio.",
     "The fall call is free - the page describes it as a no-fee call.",
     "Tell the editors if a simultaneous piece is taken elsewhere, using WITHDRAW in "
     "the subject line."],
    ["fairy tale magazine", "$25 per piece", "fairy tales", "no ai",
     "simultaneous submissions", "august submission window", "no-fee fall call",
     "short stories", "poetry submissions"],
    "accepted",
    "Simultaneous submissions are welcome. Please email "
    "thefairytalemagazine@gmail.com with WITHDRAW in the subject line to let us know "
    "if your work is accepted elsewhere. "
    f"— https://fairytalemagazine.com/submissions (read {READ})"))



BASE = {
    "colorado-review": ("US", "United States"),
    "gavialidae": ("", "International"),
    "fairy-tale-magazine": ("", "International"),
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
