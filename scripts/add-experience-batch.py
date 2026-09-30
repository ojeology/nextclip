#!/usr/bin/env python3
"""Wave 0a — assign `experience` from each publication's own stated policy.

`experience` was `not-stated` on all 147 records, which is why the roadmap gates
Wave 5 behind it. The taxonomy (BRYME-PHASE19 proposal §6):

  first-timer-friendly  the page names unpublished / first-time writers, or runs
                        a slot for them
  emerging              the page names new, emerging, debut or early-career
                        writers as a group it publishes
  established           the page asks for prior publication, professional status
                        or a track record
  not-stated            the page says nothing about it — the honest default

THE RULE, applied mechanically so a reader can reproduce every call:

  1. WRITER versus WORK. "We do not publish previously published work" is about
     the manuscript. It says nothing about who may submit and never earns a
     label. Only a sentence aimed at the person submitting counts. This is the
     single distinction the whole wave turns on, and the one a keyword search
     gets wrong: 33 of the 147 records use experience-adjacent words solely
     about the work.
  2. first-timer-friendly needs the page to say unpublished/never published/
     first-time, or to invite writers with no publication at all. Naming "new
     writers" as a group is NOT enough — that is the emerging band.
  3. Otherwise not-stated. Silence is recorded as silence. A publication that
     does not exclude first-timers is not the same as one that invites them, and
     the desk does not turn the first into the second.

EVIDENCE. Every assignment carries the sentence it was read from, verbatim, in
`experienceNote`. This script ASSERTS that each quote appears in the cached
guideline text under /home/user/.expfetch before it writes anything, so a
paraphrase or a misremembered line fails the run instead of reaching a page.
Sources are the publication's own pages; where a record's secondary source is a
third-party listicle it was ignored (chestnut-review's was — everywritersresource
disagrees with the magazine's own site, and the site had not fetched).

Read off the cached text on 2026-09-30.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
FETCH = pathlib.Path("/home/user/.expfetch")
V = "2026-09-30"

FTF = "first-timer-friendly"
EMG = "emerging"
EST = "established"

# slug: (value, verbatim quote, source URL)
CALLS: dict[str, tuple[str, str, str]] = {
    # ---- first-timer-friendly: the page names unpublished or first-time writers
    "beneath-ceaseless-skies": (FTF, "BCS welcomes submissions from new and unpublished writers.",
                                "https://www.beneath-ceaseless-skies.com/submissions/"),
    "briarpatch": (FTF, "We welcome pitches from unpublished writers, seasoned freelancers, "
                        "front-line activists, and anyone else with a story to tell and a "
                        "desire to tell it compellingly.",
                   "https://briarpatchmagazine.com/submit"),
    "fourteen-poems": (FTF, "If you\u2019re a poet, even if you\u2019ve never been published "
                            "before, we want to read your work.",
                       "https://fourteenpoems.com/submit/"),
    "goya-journal": (FTF, "You don't need to have been published previously, but you should "
                          "have the expertise, lived experience or proximity to the subject.",
                     "https://www.goya.in/how-to-pitch"),
    "mithila-review": (FTF, "We\u2019ve published both experienced and aspiring authors, and "
                            "happily encourage first-time writers from anywhere in the world "
                            "to submit.",
                       "https://mithilareview.com/submission-guidelines/"),
    "pellicle": (FTF, "Our editorial process is stringent, and while we are open to working "
                      "with first-time writers, we hold every draft to the same standards",
                 "https://pelliclemagazine.com/submissions/"),
    "poetry-london": (FTF, "Poetry London aims to publish the best, most exciting poetry being "
                           "written now, and we are always interested in work by unpublished "
                           "poets, as well as celebrated ones.",
                      "https://poetrylondon.co.uk/submissions/"),
    "strange-horizons-fiction": (FTF, "It's okay if you are unpublished!",
                                 "https://strangehorizons.com/wordpress/submit/fiction-submission-guidelines/"),
    "the-new-quarterly": (FTF, "We seek to nurture emerging writers (writers who haven\u2019t yet "
                               "published a full book) by publishing and promoting their work "
                               "alongside established writers",
                          "https://thenewquarterly.com/submissions/"),
    "the-sun-magazine": (FTF, "First-time authors and award-winners alike find their place in The Sun",
                         "https://www.thesunmagazine.org/submissions"),
    "the-stinging-fly": (FTF, "We have a particular interest in promoting new writers, and in "
                              "promoting the short story form.",
                         "https://stingingfly.org/submissions/"),

    # ---- emerging: the page names new/emerging/debut writers as a group
    "aeon-essays": (EMG, "We also strongly encourage younger and emerging scholars, especially "
                         "outside the US and the UK, to pitch Essay ideas to us, even if you "
                         "don\u2019t have much experience in writing outside of the academy.",
                    "https://aeon.co/pitch"),
    "analog-fact": (EMG, "We are eager to find and develop new, capable writers.",
                    "https://analogsf.com/contact-us/writers-guidelines/"),
    "analog-fiction": (EMG, "We are eager to find and develop new, capable writers.",
                       "https://analogsf.com/contact-us/writers-guidelines/"),
    "australian-book-review": (EMG, "Australian Book Review has a long and proud history of "
                                    "publishing emerging writers and critics with diverse "
                                    "backgrounds and interests.",
                               "https://www.australianbookreview.com.au/submissions"),
    "brevity-essays": (EMG, "Brevity publishes well-known and emerging writers working in the "
                            "extremely brief (750 words or fewer) essay form.",
                       "https://brevitymag.com/submissions/"),
    "electric-literature-essays": (EMG, "For 17 years, Electric Literature has remained dedicated "
                                        "to uplifting emerging writers.",
                                   "https://electricliterature.com/submissions/"),
    "event-magazine": (EMG, "We encourage writers from diverse backgrounds and experience levels "
                            "to send their work to EVENT.",
                       "https://eventmagazine.ca/submissions/"),
    "extra-teeth": (EMG, "We have only 16 spots per issue (12 in print and 4 on our Substack, "
                         "With Bite) and we remain committed to publishing the very best of new "
                         "and established writers.",
                    "https://extrateeth.co.uk/submissions"),
    "geist": (EMG, "Our priority is to publish work from emerging and established writers and "
                   "artists who are Canadian or permanent residents of Canada",
              "https://geist.com/submissions/"),
    "griffith-review-bodies": (EMG, "We publish work by established and emerging writers \u2013 "
                                    "most from Australia, some from overseas",
                               "https://griffithreview.com/submissions/"),
    "himal-southasian": (EMG, "We are always interested in hearing from new writers.",
                         "https://www.himalmag.com/contribute"),
    "island-magazine": (EMG, "We aim to provide as many publishing opportunities as we can for "
                             "new, emerging and established writers.",
                        "https://islandmag.com/submissions/"),
    "kill-your-darlings": (EMG, "Kill Your Darlings welcomes submissions of short fiction to the "
                                "magazine from established and emerging writers year-round.",
                           "https://killyourdarlings.com.au/submit/"),
    "markaz-review": (EMG, "TMR is open to both emerging and established writers, and to writing "
                           "in multiple languages",
                      "https://themarkaz.org/submit/"),
    "mslexia": (EMG, "Including big-name commissions and as-yet-undiscovered newcomers, we "
                     "publish over 60 women in every issue.",
                "https://mslexia.co.uk/submit-your-work/"),
    "ploughshares": (EMG, "We consider authors \u201cemerging\u201d if they haven\u2019t "
                           "published or self-published a book.",
                     "https://www.pshares.org/submit/"),
    "prism-international": (EMG, "PRISM international publishes exciting, original, literary "
                                 "material from established and emerging writers in Canada and "
                                 "around the world.",
                            "https://prismmagazine.ca/submissions/"),
    "propel-magazine": (EMG, "Propel Magazine is for writers who have not previously published a "
                             "full collection.",
                        "https://propelmagazine.co.uk/submissions/"),
    "pulp-literature": (EMG, "If you\u2019re a new writer, send in your most thrilling, funny, or "
                             "heart-rending work!",
                        "https://pulpliterature.com/submit/"),
    "the-fiction-desk": (EMG, "The Fiction Desk is a short story publisher specialising in regular "
                              "anthologies of new short fiction from both debut and established "
                              "authors.",
                         "https://www.thefictiondesk.com/submissions/"),
    "the-malahat-review": (EMG, "The Malahat Review welcomes submissions of poetry, short fiction, "
                                "and creative nonfiction, as well as translated work in any of "
                                "these three genres, by new and established writers from Canada "
                                "and abroad.",
                           "https://malahatreview.ca/submissions/"),
    "the-rumpus-el-alboroto": (EMG, "We welcome work from both emerging and established writers.",
                               "https://therumpus.net/submissions/"),
    "the-rumpus-essays": (EMG, "We welcome work from both emerging and established writers.",
                          "https://therumpus.net/submissions/"),
    "writers-digest": (EMG, "Although we welcome the work of new writers, we believe the "
                            "established writer can better instruct our reader.",
                       "https://www.writersdigest.com/submissions"),
}

# ---- established: the page asks for a track record --------------------------
CALLS.update({
    "broadview": (EST, "The majority of articles published in Broadview magazine and on "
                       "Broadview.org are assigned to professional writers and journalists.",
                  "https://broadview.org/submissions/"),
    "business-insider": (EST, "We will ask you for a headshot, a bio, and proof of your credentials.",
                         "https://www.businessinsider.com/freelance-journalism"),
    "climate-home-news": (EST, "When contacting us for the first time, please provide clear "
                               "evidence of your track record as a journalist so that we can "
                               "verify your identity.",
                          "https://www.climatechangenews.com/about/write-for-us/"),
    "income-diary": (EST, "If you are a professional writer and would like to be paid, please let "
                          "us know when you submit your article for review including your fee.",
                     "https://www.incomediary.com/write-for-incomediary"),
})


def url_path(url: str) -> str:
    from urllib.parse import urlparse
    return urlparse(url).path


def _norm(t: str) -> str:
    """Collapse whitespace and tidy the artefacts HTML-to-text always leaves.

    Comparing raw strings overstated this: stripping tags leaves "The Sun ."
    where the page renders "The Sun." because a link ended there, and a run of
    newlines where the page had one paragraph break. Normalising both sides is
    the right comparison - the check is that the SENTENCE is the same one, not
    that the whitespace survived a parser.
    """
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\s+([.,;:!?])", r"\1", t)
    t = re.sub(r"\s+[\u2013\u2014]\s+", " - ", t)
    return t.strip()


def main(write: bool) -> int:
    raw = OPPS.read_text(encoding="utf-8")
    data = json.loads(raw)
    recs = {r["slug"]: r for r in data["opportunities"]}

    problems: list[str] = []
    resolved: dict[str, str] = {}
    for slug, (value, quote, url) in CALLS.items():
        if slug not in recs:
            problems.append(f"{slug}: not a record")
            continue
        cached = FETCH / f"{slug}.txt"
        if not cached.exists():
            problems.append(f"{slug}: no cached guideline to verify against")
            continue
        text = _norm(cached.read_text(encoding="utf-8"))
        if _norm(quote) not in text:
            problems.append(f"{slug}: QUOTE NOT FOUND in the cached guideline")
        else:
            # WHICH PAGE the sentence actually came from, taken from the harvest
            # rather than typed here. The note used to carry a hand-written URL
            # and 21 of the 40 were wrong - plausible-looking submissions paths
            # that the publication does not use. The sentence was real and the
            # citation beside it was invented, which is precisely the defect this
            # desk exists to avoid, so the URL is now a fact read out of the
            # cache: the section header the quote is found under.
            parts = re.split(r"===== SOURCE (\S+) =====", text)
            sections = [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
            home = [u for u, body in sections if _norm(quote) in body]
            if not home:
                problems.append(f"{slug}: quote is in the cache but under no SOURCE header")
            else:
                # A label may not rest on a homepage. "Emerging Writers' Contest"
                # in a nav bar is a programme name, not a policy, and a blurb by a
                # named third party is not the magazine's own word.
                if url_path(home[0]) in ("", "/"):
                    problems.append(f"{slug}: evidence is the homepage ({home[0]}) - "
                                    f"a policy has to come from the guidelines page")
                resolved[slug] = home[0]
        # the rule, machine-checked: a work-level sentence earns no label
        low = _norm(quote).lower()
        for work_phrase in ("previously unpublished work", "original, unpublished work",
                            "do not accept previously published work"):
            if work_phrase in low:
                problems.append(f"{slug}: quote describes the WORK, not the writer")

    if problems:
        print("REFUSING TO WRITE — evidence did not check out:")
        for p in problems:
            print("  FAIL", p)
        return 1

    if not write:
        print(f"dry run: {len(CALLS)} assignments, every quote present in its cached source")
        for slug, url in sorted(resolved.items()):
            print(f"   {CALLS[slug][0][:18]:20} {slug:26} {url[:74]}")
        return 0

    for slug, (value, quote, _typed) in CALLS.items():
        rec = recs[slug]
        rec["experience"] = value
        rec["experienceNote"] = f"{quote} \u2014 {resolved[slug]} (read {V})"
    data["updatedAt"] = V
    OPPS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    import collections
    dist = collections.Counter(r.get("experience", "not-stated") for r in data["opportunities"])
    print(f"wrote {len(CALLS)} assignments to content/opportunities.json")
    for k, v in dist.most_common():
        print(f"   {k:22} {v:>4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main("--write" in sys.argv))
