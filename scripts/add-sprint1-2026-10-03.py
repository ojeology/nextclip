#!/usr/bin/env python3
"""Add four NEW verified writing markets — sprint batch 1 (2026-10-03).

First batch of the records sprint agreed 2026-10-03 (desk roadmap: 300 -> 500
verified records). Same standard as the earlier batches: every figure below
was read off the publication's own live guidelines page on 2026-10-03. Official-source extracts
and verification notes are retained in the working archive outside the generated site tree.

Four NEW records:
  smokelong-quarterly   flash fiction/creative nonfiction, $100/$150 with audio
  khoreo                speculative fiction, $0.10/word SFWA pro rate, windowed
  dublin-review         fiction and nonfiction, fee scale from EUR 300
  the-dark-magazine     horror and dark fantasy, 5 cents/word originals

Fetched in the same pass but NOT added, and why (logged at the bottom):
  wigleaf.com           prestige flash market but pays nothing - outside the
                        paid-opportunity scope of this desk
  catapult.co           the magazine is now an archive; Catapult has pivoted
                        to book publishing and no longer takes story/essay
                        submissions
  lolwe.net             site unreachable on verification day - needs a retry
  nightmare-magazine.com submissions page 404s; market status unverifiable
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-10-03"


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

# ------------------------------------------------------- SmokeLong Quarterly
NEW.append(rec(
    "smokelong-quarterly", "SmokeLong Quarterly", "Flash fiction and flash creative nonfiction up to 1,000 words",
    "SmokeLong Quarterly submissions: $100–$150",
    "SmokeLong publishes flash up to 1,000 words and pays $100, or $150 if you grant audio "
    "rights. See reading windows and anonymous-submission rules.",
    "https://www.smokelong.com/guidelines/",
    "https://smokelong.submittable.com/Submit", None,
    "Online via Submittable during reading periods",
    src("SmokeLong Quarterly — Guidelines (official)", "https://www.smokelong.com/guidelines/"),
    {"summary": "No stated country restriction. SmokeLong reads internationally and assigns "
                "every submission to two editors anonymously.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction", "creative-nonfiction"], "Flash fiction and flash creative nonfiction",
    pay("USD", 100, 150, "$100 per story, or $150 with audio rights",
        "Official guidelines: payment is $100/$150 with audio, issued upon publication in the "
        "quarterly issue via PayPal or Zelle; the writer may bear any associated fees. The "
        "annual SmokeLong Quarterly Award for Flash Fiction is a separate paid competition "
        "with its own entry fees and prizes.",
        "Upon publication in the quarterly issue, via PayPal or Zelle"),
    {"min": 1, "max": 1000, "display": "Up to 1,000 words"},
    {"label": "Up to 4 weeks in free windows; usually sooner", "band": "2-4-weeks",
     "official": True},
    "open", None, "prohibited",
    ["Flash narratives up to 1,000 words — fiction and creative nonfiction — that are "
     "previously unpublished.",
     "Stories that stand up to rereading: the guidelines ask for something sincerely and "
     "uniquely yours, surprising and thrilling.",
     "Reviews of flash collections, essays on craft and articles on teaching flash are "
     "considered for the blog.",
     "Work previously published only on a personal blog or website is considered, if it is "
     "taken down before publication and flagged in the cover letter."],
    ["Previously published work, except in the annual Grand Micro Contest.",
     "Narratives created with the aid of AI — including AI translation or stylistic "
     "modification. Grammar tools are fine.",
     "Poetry — the magazine publishes prose flash only.",
     "Identifying information in the manuscript, filename or Submittable title; editors read "
     "anonymously."],
    ["Submit one unpublished piece at a time and wait for a decision, or use the "
     "multiple-submission option with up to three pieces in one document (paid windows, "
     "faster response).",
     "Include a print-ready, third-person bio in your cover letter.",
     "Keep the manuscript, filename and Submittable title free of your name.",
     "Watch for the free-submission window at the start of each reading period; after it "
     "closes a small fee applies, and the magazine always keeps a free window."],
    "Exclusive electronic rights for six months, then non-exclusive rights for the online "
    "archive; non-exclusive print rights for potential anthologies and promotion. All other "
    "rights remain with the writer.",
    ["Check the reading calendar on the guidelines page and submit inside a window — the "
     "December issue window runs roughly August 16 to November 15.",
     "Send your piece through the Submittable manager; one piece, or up to three via the "
     "multiple-submission option.",
     "If the piece is under consideration you will be told more time is needed; otherwise "
     "expect a decision within four weeks in free windows and about a week in paid windows.",
     "If your story is accepted elsewhere first, withdraw it through Submittable right away."],
    ["smokelong", "flash fiction", "flash nonfiction", "$100", "quarterly", "anonymous reading"]))


# ------------------------------------------------------- khōréō
NEW.append(rec(
    "khoreo", "khōréō", "Speculative fiction by immigrant and diaspora writers",
    "khōréō submissions: $0.10 per word",
    "khōréō pays $0.10 per word for speculative fiction by immigrant and diaspora writers. "
    "Its next fiction window is November 1–30, 2026.",
    "https://www.khoreomag.com/submissions-fiction/",
    "https://khoreo.moksha.io/publication/khoreo-magazine", "contact@khoreomag.com",
    "Online via Moksha during submission windows",
    src("khōréō — Submissions: Fiction (official)",
        "https://www.khoreomag.com/submissions-fiction/"),
    {"summary": "Restricted by identity: khōréō invites writers who identify as immigrants or "
                "members of a diaspora in the broadest sense — first- and second-generation "
                "immigrants, refugees, asylum seekers, undocumented migrants, diaspora "
                "communities, transnational and transracial adoptees, and anyone whose heritage "
                "includes 'here and elsewhere'. Nigerian and other African writers qualify "
                "where that identity applies. People outside those groups are asked to support "
                "the magazine by reading and subscribing instead.",
     "mode": "restricted", "includesGroups": ["immigrants", "diaspora"],
     "includesRegions": [], "allowsDiaspora": True, "notStated": False},
    ["fiction", "translation"], "Speculative short fiction and translated speculative fiction",
    pay("USD", None, None, "$0.10 per word (SFWA pro rate)",
        "Official fiction submissions page: payment at SFWA pro rates, listed as $0.10 per "
        "word (raised from $0.08). Translations earn the same rate for both the original "
        "author and the translator where applicable.",
        "Not publicly stated"),
    {"min": 1, "max": 5000, "display": "Under 5,000 words — flash queue ≤1,500, stories "
     "1,501–5,000; under 3,500 preferred"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "upcoming", {"display": "Next fiction window runs 1–30 November 2026 (themed submissions)",
              "openingDate": "2026-11-01", "recurring": True}, "prohibited",
    ["Short speculative fiction under 5,000 words with a speculative element — fantasy, "
     "sci-fi, horror and anything between or around the genres.",
     "Stories exploring migration in any form: immigration, diaspora, anti-colonialism, or "
     "more metaphorical readings of movement and displacement.",
     "One story per queue per window: you may submit one story to the flash queue (≤1,500 "
     "words) and one to the short story queue (1,501–5,000)."],
    ["Gratuitous gore or violence.",
     "Fridging — a character harmed purely to serve another character's development.",
     "Overwhelming racist, sexist, ableist, homophobic or xenophobic elements that the story "
     "does not subvert or challenge.",
     "Clichés and 'it was all a dream' endings.",
     "Stories where a person from a non-marginalized group experiences life as someone from a "
     "marginalized background.",
     "Novelettes, novellas, reprints, unsolicited resubmissions, multiple submissions within "
     "one category, and AI-generated work.",
     "Anything over 5,000 words — rejected unread."],
    ["Submit through Moksha during a window — fiction windows in 2026 are March (general), "
     "July (general) and November (themed); the next cycle runs 1–30 November 2026.",
     "Choose the right queue by length: flash (≤1,500) or short story (1,501–5,000).",
     "Format to the Shunn modern manuscript format; a mailing address is only needed after "
     "acceptance.",
     "If you are a previous contributor, wait until at least one year after your published "
     "issue before submitting again."],
    "First world English-language rights (digital, ebook and print), plus non-exclusive "
    "rights to include the story in an anthology within 24 months, archive it on the website "
    "for at least 36 months and record audio of it for at least 36 months.",
    ["Confirm the next window on the submissions page — windows are dated and submissions "
     "outside them are not read.",
     "Pick the queue by word count and submit one story per queue.",
     "Add a cover letter if you like: identity in your own words, genre, content warnings, "
     "and whether you want feedback.",
     "If the story is a simultaneous submission, say so in the cover letter and withdraw "
     "immediately if it is accepted elsewhere."],
    ["khoreo", "speculative fiction", "immigrant writers", "diaspora", "$0.10 per word",
     "science fiction", "fantasy", "migration"]))


# ------------------------------------------------------- The Dublin Review
NEW.append(rec(
    "dublin-review", "The Dublin Review", "Fiction and nonfiction — essays, reportage, criticism, memoir",
    "The Dublin Review submissions: from €300",
    "The Dublin Review welcomes unpublished fiction and nonfiction in English, with fees from "
    "€300 for pieces up to 2,500 words. Submit online.",
    "https://thedublinreview.com/submissions/",
    "https://thedublinreview.com/submissions/", None,
    "Online submission form (no postal submissions)",
    src("The Dublin Review — Submissions (official)",
        "https://thedublinreview.com/submissions/"),
    {"summary": "No stated country restriction. The magazine publishes writers from Ireland "
                "and elsewhere and says it especially encourages submissions from members of "
                "groups traditionally underrepresented in literary magazines and other "
                "cultural forums.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction", "essays", "creative-nonfiction"], "Fiction and long-form nonfiction",
    pay("EUR", 300, None, "From €300 for pieces up to 2,500 words; rises with length",
        "Official submissions page: the fee scale starts at €300 for pieces up to 2,500 words and "
        "increases with word count; it does not publish separate rates for commissioned and "
        "unsolicited work.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "No word limit stated on the current guidelines page"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Fiction and nonfiction previously unpublished in the English language.",
     "Essays of all kinds, reportage, criticism, travel writing, memoir and short stories.",
     "Work from writers anywhere; the magazine especially encourages submissions from groups "
     "traditionally underrepresented in literary magazines."],
    ["Poetry — the magazine does not accept poems.",
     "Work previously published in English."],
    ["Complete the online form on the submissions page with your name, email, a cover note "
     "and your submission document.",
     "Do not send submissions by post — the form is the only channel.",
     "Note the date you submitted: the form confirms on screen but sends no confirmation "
     "email.",
     "Expect a reply by email when the editors have read the piece; no timeframe is "
     "published."],
    "Not stated on the official submissions page.",
    ["Read a recent issue or two from the archive — full texts are free on the site — and "
     "make sure your piece sits in the magazine's register.",
     "Prepare your manuscript as a single document and send it through the form.",
     "Keep your own record of the submission date, since no confirmation email arrives.",
     "Longer pieces earn more on the published scale, but write to the piece, not the meter."],
    ["dublin review", "irish literary magazine", "essay", "reportage", "memoir",
     "short story", "€300"]))


# ------------------------------------------------------- The Dark Magazine
NEW.append(rec(
    "the-dark-magazine", "The Dark Magazine", "Horror and dark fantasy, 2,000–6,000 words",
    "The Dark Magazine: 5¢ per word",
    "The Dark pays 5¢ per word for original horror and dark fantasy up to 6,000 words. Submit "
    "by email; no simultaneous or AI-assisted work.",
    "https://www.thedarkmagazine.com/submission-guidelines/",
    "mailto:submissions@thedarkmagazine.com", "submissions@thedarkmagazine.com",
    "Email with the story attached (.doc, .docx or .rtf)",
    src("The Dark Magazine — Submission Guidelines (official)",
        "https://www.thedarkmagazine.com/submission-guidelines/"),
    {"summary": "No stated country restriction. The magazine's diversity statement welcomes "
                "submissions from all writers, of all nations, nationalities, ethnicities, "
                "backgrounds, faiths, genders, orientations, identities and experiences. "
                "Nigeria qualifies.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction"], "Horror and dark fantasy short fiction",
    pay("USD", None, None, "5¢/word originals; 1¢/word reprints",
        "Official guidelines: 5 cents per word for original fiction up to 6,000 words, paid on "
        "publication for first world rights; 1 cent per word for reprint fiction up to 6,000 "
        "words, paid on acceptance for non-exclusive reprint rights.",
        "On publication for originals; on acceptance for reprints"),
    {"min": 2000, "max": 6000, "display": "2,000–6,000 words"},
    {"label": "Minutes to 48 hours; query after one week", "band": "fast", "official": True},
    "unknown", None, "prohibited",
    ["Horror and dark fantasy between 2,000 and 6,000 words.",
     "Stories that experiment or deviate from the ordinary — the guidelines invite fiction "
     "that may fall outside regular categories.",
     "Reprints are considered if they first appeared in established print markets — "
     "magazines, collections, anthologies — within the past two years."],
    ["Graphic, violent horror — despite the name, this is not that market.",
     "Anything translated, written, developed or assisted by AI tools; attempting to submit "
     "AI work may mean a ban from future submissions.",
     "Simultaneous submissions and multiple submissions — violations result in a total ban.",
     "Stories embedded in the body of the email instead of attached as a document.",
     "Responses to rejection letters, for any reason."],
    ["Email submissions@thedarkmagazine.com with the story attached in .doc, .docx or .rtf.",
     "Use proper manuscript format — the modern Shunn format is preferred.",
     "Include your bio in a cover letter.",
     "For reprints, put REPRINT in the email header: SUBMISSION: [STORY TITLE] (REPRINT).",
     "Submit once and wait for a response before sending anything else; there is no wait "
     "period after a rejection."],
    "First world rights for original fiction, bought on publication; non-exclusive reprint "
    "rights for reprints, bought on acceptance.",
    ["The current guidelines list email submissions but do not explicitly state whether the reading period is open; check the official page before sending.",
     "Polish the story to manuscript format and attach it — never paste it into the email.",
     "Send it once, then wait: responses can arrive within minutes or take up to two days; "
     "query only after a full week, including the title and date submitted.",
     "Do not submit the same story anywhere else while The Dark considers it.",
     "If the story has appeared in a print market in the past two years, submit it as a "
     "reprint with REPRINT in the header."],
    ["the dark magazine", "horror", "dark fantasy", "5 cents per word", "monthly magazine",
     "no simultaneous submissions"]))


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
        BASE = {
            "smokelong-quarterly": ("US", "United States"),
            "khoreo": ("", "International"),
            "dublin-review": ("IE", "Ireland"),
            "the-dark-magazine": ("", "International"),
        }
        for r in NEW:
            base, label = BASE[r["slug"]]
            pc[r["slug"]] = {"base": base, "label": label}
        PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Added {len(NEW)} verified records. Total opportunities: {len(opps)}")


if __name__ == "__main__":
    main()
