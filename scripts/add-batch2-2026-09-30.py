#!/usr/bin/env python3
"""Add verified writing-market batch 2 (2026-09-30).

Nine NEW markets, each read off the publication's own guidelines page on
2026-09-30. Raw page text saved under research/batch2/*.txt.

Probed 160 reachable candidates; 74 yielded a guidelines-shaped URL; 20 of
those survived the content filter; 9 supported a record. The rest are logged
at the bottom of this file with the reason, including the ones where the
"guidelines" URL was actually an article, an image or a parked domain.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-30"


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

# ------------------------------------------------------- 1 Balkan Insight
NEW.append(rec(
    "balkan-insight", "Balkan Insight / Reporting Democracy",
    "Commentary, features, news analysis, interviews and investigations",
    "Balkan Insight: €100 for a commentary piece, grants to €5,000",
    "Balkan Insight's Reporting Democracy pays a standard rate of 100 euros for a commentary "
    "piece and competitive rates for features, news analysis, interviews, videos and "
    "investigations on democracy in Central, Eastern and Southeastern Europe. Most analyses, "
    "features and interviews run 800 to 1,200 words. A limited number of grants of up to 5,000 "
    "euros are available to teams or individuals.",
    "https://balkaninsight.com/reporting-democracy/contribute/",
    "https://balkaninsight.com/reporting-democracy/contribute/", None,
    "Email pitch — see the contribute page for the addresses",
    src("Balkan Insight / Reporting Democracy — Contribute (official)",
        "https://balkaninsight.com/reporting-democracy/contribute/"),
    {"summary": "No stated country restriction on contributors. The coverage focus is a named "
                "list of countries: Albania, Bosnia and Herzegovina, Bulgaria, Croatia, Czech "
                "Republic, Hungary, Kosovo, Moldova, Montenegro, North Macedonia, Poland, "
                "Serbia, Romania and Slovakia.",
     "mode": "not-stated", "includesRegions": ["europe"], "allowsDiaspora": True,
     "notStated": True},
    ["opinion", "analysis", "journalism", "interviews"],
    "Commentary, features, news analysis, interviews, videos and investigations",
    pay("EUR", 100, 100, "€100 standard for a commentary piece; competitive rates for features",
        "Official contribute page: the standard rate for a commentary piece is 100 euros. "
        "Reporting Democracy separately pays competitive rates for feature stories, news "
        "analysis, interviews, videos and investigations, but publishes no figure for those, so "
        "BRYME records only the one stated rate. A limited number of grants of up to 5,000 euros "
        "are available for teams or individuals.",
        "Not publicly stated"),
    {"min": 800, "max": 1200,
     "display": "Most analyses, features and interviews run 800–1,200 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Work on issues affecting the state of democracy in Central, Eastern and Southeastern "
     "Europe.",
     "A pitch that summarises the story idea in three or four paragraphs and clearly explains "
     "why the proposed piece is important.",
     "Commentary, features, news analysis, interviews, video and investigations."],
    ["The contribute page does not publish a list of exclusions. Note that the length of a "
     "commissioned piece is outlined when it is commissioned, so do not assume 800–1,200 words "
     "applies to your pitch."],
    ["Email your pitch to the address on the contribute page — the page renders addresses "
     "through Cloudflare email protection, so read them there rather than copying from a "
     "summary.",
     "Op-ed proposals go to a separate address from story pitches; the page lists both.",
     "Summarise the idea in three or four paragraphs and say why it matters.",
     "Expect to work one-on-one with an editor, often by email or Skype.",
     "If you need reporting funding, ask about the grants of up to 5,000 euros."],
    "Not stated on the official contribute page.",
    ["Read https://balkaninsight.com/reporting-democracy/contribute/ for the two addresses and "
     "the grant terms.",
     "Check that your country is on the focus list before pitching a domestic story.",
     "Pitch a story, not a topic — and say why it matters now."],
    ["balkan insight", "reporting democracy", "europe", "democracy", "commentary",
     "investigation", "eur", "grant"]))

# ------------------------------------------------------- 2 Boston Review
NEW.append(rec(
    "boston-review", "Boston Review", "Long-form essays on politics and ideas",
    "Boston Review: around $500 for web essays of 2,500–5,000 words",
    "Boston Review publishes long-form essays on politics and ideas, book review essays, "
    "interviews, in-depth analysis of current affairs and occasional reporting. Most essays run "
    "2,500 to 5,000 words and all go through intensive editing. For web pieces it typically pays "
    "around $500 depending on length, for writers whose main source of income is their writing; "
    "other writers are offered a modest honorarium.",
    "https://www.bostonreview.net/about/submissions/",
    "https://www.bostonreview.net/about/submissions/", None,
    "Submittable — no email submissions",
    src("Boston Review — Submissions (official)",
        "https://www.bostonreview.net/about/submissions/"),
    {"summary": "No stated country restriction. The pay terms distinguish writers by whether "
                "writing is their main source of income, not by where they live.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["essays", "reviews", "interviews", "analysis"],
    "Long-form essays, book review essays, interviews, analysis and occasional reporting",
    pay("USD", 500, 500, "Around $500 for web pieces; modest honorarium for other writers",
        "Official submissions page: for web pieces Boston Review typically pays around $500, "
        "depending on length, for writers whose main source of income derives from their "
        "writing. For all other writers it can offer a modest honorarium, but states no figure. "
        "BRYME records the stated web rate; the honorarium for other writers is undefined on the "
        "page.",
        "Not publicly stated"),
    {"min": 2500, "max": 5000, "display": "Most essays run 2,500–5,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Long-form essays on politics and ideas, feature book review essays, interviews, in-depth "
     "analysis of current affairs, and occasional reporting.",
     "A special interest in democracy, inequality and matters of injustice — including war, "
     "poverty and violations of human rights.",
     "Submissions on any subject of broad public concern, not only the priority themes.",
     "Work that can survive intensive editing; every essay goes through it."],
    ["The submissions page does not publish a list of exclusions. Note that the special interest "
     "in democracy, inequality and injustice describes priority, not a boundary."],
    ["Submit through the Submittable portal linked from the submissions page.",
     "Do not email submissions — the portal is the only route.",
     "Expect intensive editing; the page says all essays go through it.",
     "Be ready to say whether writing is your main source of income, since the rate depends on "
     "it."],
    "Not stated on the official submissions page.",
    ["Read https://www.bostonreview.net/about/submissions/ and use the Submittable link.",
     "Pitch long. Most essays are 2,500–5,000 words and a short piece is unlikely to fit.",
     "Tell them about your income situation up front — it determines whether you are offered the "
     "$500 web rate or the honorarium."],
    ["boston review", "essays", "politics", "ideas", "book review", "$500", "submittable"]))

# ------------------------------------------------------- 3 East Asia Forum
NEW.append(rec(
    "east-asia-forum", "East Asia Forum", "Analytic op-eds on East Asian economics and politics",
    "East Asia Forum: ~800-word op-eds, double-blind peer review",
    "East Asia Forum invites original analytic op-eds of around 800 words, accessible to a "
    "general audience and written in crisp, clear language. Every original submission goes "
    "through double-blind peer review, so it will not match the mainstream press for speed. It "
    "does not publish submissions where the substance of the argument or analysis is generated "
    "by AI, but AI may be used for research and clarity provided it is disclosed.",
    "https://eastasiaforum.org/submissions/",
    "https://eastasiaforum.org/submissions/", None, "Online submission — see submissions page",
    src("East Asia Forum — Submissions (official)", "https://eastasiaforum.org/submissions/"),
    {"summary": "No stated country restriction. The page explicitly invites writers who are not "
                "completely confident in their English to submit, and describes a well-informed "
                "international readership.",
     "mode": "not-stated", "includesRegions": ["east-asia"], "allowsDiaspora": True,
     "notStated": True},
    ["opinion", "analysis"], "Analytic op-eds",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out the format, the length and the peer-review process "
        "but publishes no rate, so BRYME records no figure. Ask about payment when you submit.",
        "Not publicly stated"),
    {"min": None, "max": 800, "display": "Around 800 words"},
    {"label": "Not stated; double-blind peer review means it is not fast",
     "band": "not-stated", "official": False},
    "open", None, "disclosure-required",
    ["An original analytic op-ed of around 800 words, accessible to a general audience.",
     "Crisp, clear language.",
     "An argument. The page is emphatic that the takeaway argument, not the facts and figures "
     "behind it, is what readers remember.",
     "Writers who are not completely confident in their English — the page says plainly not to "
     "hesitate."],
    ["Submissions in which the substance of the arguments or analysis is generated by AI. AI "
     "must not generate arguments, analysis or substantive content, including paragraphs, data, "
     "findings, citations or summaries of longer texts.",
     "Undisclosed AI use. Authors must disclose any use of AI at the time of submission, and "
     "submissions that appear to rely on AI-generated content will be rejected.",
     "Breaking-news reaction. The double-blind peer review process means EAF cannot match the "
     "mainstream press on pace."],
    ["Submit through the route on https://eastasiaforum.org/submissions/.",
     "Write to about 800 words and make a single clear argument.",
     "Disclose any AI use at the time of submission.",
     "Independently verify everything — the page warns that AI tools generate inaccurate and "
     "misleading information and holds the author responsible for accuracy."],
    "Not stated on the official submissions page.",
    ["Read https://eastasiaforum.org/submissions/ — it carries the full AI policy, which is more "
     "nuanced than a flat ban.",
     "Do not pitch breaking news.",
     "Disclose AI use up front; the penalty for being caught relying on it is rejection."],
    ["east asia forum", "op-ed", "analysis", "east asia", "800 words", "peer review",
     "ai disclosure"]))

# ------------------------------------------------------- 4 Foreign Affairs
NEW.append(rec(
    "foreign-affairs", "Foreign Affairs", "Analysis of international affairs and US foreign policy",
    "Foreign Affairs: rolling submissions, no AI-generated text",
    "Foreign Affairs welcomes pitches and unsolicited manuscripts and considers them on a "
    "rolling basis rather than to a fixed editorial calendar. It assumes any piece submitted is "
    "offered exclusively, and requires authors to affirm that none of the text in their articles "
    "was generated by an artificial-intelligence tool. The page publishes no rate.",
    "https://www.foreignaffairs.com/submissions",
    "https://www.foreignaffairs.com/submissions", None, "Online submission — rolling",
    src("Foreign Affairs — Submissions (official)", "https://www.foreignaffairs.com/submissions"),
    {"summary": "No stated country restriction. Foreign Affairs describes its standard as clear "
                "thinking by knowledgeable observers, written in English that can be read with "
                "ease by both professionals and a broad general audience.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["analysis", "essays", "opinion"], "International affairs analysis",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out the rolling process, the exclusivity assumption and "
        "the AI affirmation, but publishes no rate, so BRYME records no figure.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Not stated on the submissions page"},
    {"label": "Not stated; considered on a rolling basis", "band": "not-stated",
     "official": False},
    "open", None, "prohibited",
    ["Clear thinking by knowledgeable observers on important issues.",
     "English that can be read with ease and pleasure by both professionals and a broad general "
     "audience.",
     "Pitches and unsolicited manuscripts alike — both are considered, on a rolling basis."],
    ["Text generated by an artificial-intelligence tool. Authors are required to affirm that "
     "none of the text in their articles was AI-generated.",
     "Simultaneous publication. Unless told otherwise, Foreign Affairs assumes any piece "
     "submitted is offered exclusively and that nothing accepted will be published elsewhere at "
     "the same time without its knowledge."],
    ["Submit through https://www.foreignaffairs.com/submissions.",
     "Be prepared to affirm that none of your text was AI-generated.",
     "Do not submit elsewhere simultaneously unless you have told them.",
     "There is no editorial calendar to time yourself against — submissions are considered as "
     "they arrive."],
    "Not stated on the official submissions page.",
    ["Read https://www.foreignaffairs.com/submissions before you send.",
     "Assume exclusivity is expected.",
     "Do not pitch on a deadline; the process is rolling, not scheduled."],
    ["foreign affairs", "international affairs", "foreign policy", "analysis", "rolling",
     "no ai"]))

# ------------------------------------------------------- 5 Dialogue Earth
NEW.append(rec(
    "dialogue-earth", "Dialogue Earth (China Dialogue)",
    "Environmental journalism from local voices",
    "Dialogue Earth: 1,000–1,500 word environmental stories, 300-word pitches",
    "Dialogue Earth, the independent non-profit behind China Dialogue, welcomes pitches for "
    "articles of 1,000 to 1,500 words from journalists and experts. Pitches are a brief outline "
    "of no more than 300 words, sent to a named editor. Fees for journalism are based on "
    "competitive market rates in the author's region; expert opinion pieces are not normally "
    "paid.",
    "https://dialogue.earth/en/pitch/",
    "https://dialogue.earth/en/pitch/", None, "Email pitch to a named editor",
    src("Dialogue Earth — Pitch (official)", "https://dialogue.earth/en/pitch/"),
    {"summary": "Open worldwide, with regional commissioning. Dialogue Earth is commissioning "
                "content in English from creators based in Southeast Asia, South Asia and "
                "Africa, and in Spanish or Portuguese from creators in Latin America.",
     "mode": "worldwide", "includesRegions": ["asia", "africa", "latin-america"],
     "allowsDiaspora": True, "notStated": False},
    ["journalism", "analysis", "opinion"],
    "Environmental journalism, expert commentary and social video",
    pay(None, None, None, "Competitive market rates in the author's region — no figure published",
        "Official pitch page: fees for journalism are based on competitive market rates in the "
        "author's region, so the rate varies by where you are based and no single figure exists "
        "for BRYME to record. Expert opinion pieces are not normally paid. Agree the fee with "
        "your editor before you write.",
        "Not publicly stated"),
    {"min": 1000, "max": 1500, "display": "Articles of 1,000–1,500 words; pitch outline 300 words"},
    {"label": "Allow two weeks before following up", "band": "2-4-weeks", "official": True},
    "open", None, "not-stated",
    ["Articles of 1,000 to 1,500 words from journalists and experts.",
     "A specific pitch for a story rather than a broad idea or a topic, in an outline of no more "
     "than 300 words.",
     "Urban heat solutions, Indigenous environmental issues, and climate and energy justice "
     "reported from the ground — named as current priorities.",
     "Suggestions for multimedia elements including photographs, illustrations and infographics.",
     "Pitches for cross-publication, collaboration and partnership with other outlets.",
     "Social video from independent creators in Southeast Asia, South Asia and Africa in "
     "English, or in Latin America in Spanish or Portuguese."],
    ["Expectation of payment for expert opinion pieces. Dialogue Earth states it does not "
     "normally pay for them.",
     "Broad ideas or topics in place of a specific story pitch."],
    ["Send a brief outline of no more than 300 words to one of the editors listed on the pitch "
     "page.",
     "Choose an editor from your region; if they are not the right person they will forward it.",
     "Mark time-sensitive pitches in the subject line.",
     "Allow two weeks before sending a follow-up."],
    "Not stated on the official pitch page.",
    ["Read https://dialogue.earth/en/pitch/ and pick the right editor for your region.",
     "Keep the outline under 300 words and make it a story, not a topic.",
     "If you are pitching expert commentary, do not assume it will be paid."],
    ["dialogue earth", "china dialogue", "environment", "climate", "journalism", "global south",
     "pitch"]))

# ------------------------------------------------------- 6 Brittle Paper
NEW.append(rec(
    "brittle-paper", "Brittle Paper", "African fiction, essays, commentary and book reviews",
    "Brittle Paper: fiction to 2,500 words, essays and reviews to 1,500",
    "Brittle Paper, the magazine of African literature, takes fiction of no more than 2,500 "
    "words and book reviews, literary commentary, think pieces and essays of no more than 1,500 "
    "words. Writers retain copyright. The submissions page does not publish a payment rate.",
    "https://brittlepaper.com/submissions/",
    "mailto:brittlesubmissions@gmail.com", "brittlesubmissions@gmail.com", "Email submission",
    src("Brittle Paper — Submissions (official)", "https://brittlepaper.com/submissions/"),
    {"summary": "No stated country restriction on the submissions page. The magazine's subject "
                "is African literature.",
     "mode": "not-stated", "includesRegions": ["africa"], "allowsDiaspora": True,
     "notStated": True},
    ["fiction", "reviews", "essays", "analysis"],
    "Fiction, book reviews, literary commentary, think pieces and essays",
    pay(None, None, None, "Not stated on the submissions page",
        "The public submissions page sets out the word limits by format and the copyright "
        "position but publishes no payment rate, so BRYME records no figure. Ask about payment "
        "when you submit.",
        "Not publicly stated"),
    {"min": None, "max": 2500,
     "display": "Fiction up to 2,500 words; reviews, commentary and essays up to 1,500"},
    {"label": "Not stated; rejection emails are not sent", "band": "not-stated",
     "official": False},
    "open", None, "not-stated",
    ["Fiction of no more than 2,500 words.",
     "Book reviews of no more than 1,500 words.",
     "Literary commentary, think pieces and essays of no more than 1,500 words.",
     "Work responding to immediate events on the literary scene."],
    ["Fiction over 2,500 words, or reviews, commentary and essays over 1,500.",
     "Expecting an acknowledgement. Brittle Paper states it usually does not acknowledge "
     "reception unless emailed separately, and that it is unable to send rejection emails."],
    ["Email your submission to brittlesubmissions@gmail.com.",
     "If the piece responds to immediate events on the literary scene, email it to the same "
     "address and say so.",
     "Keep to the word limit for your format.",
     "Email separately if you want an acknowledgement of receipt, because one is not automatic."],
    "Writers retain the copyright to their work.",
    ["Read https://brittlepaper.com/submissions/ for the current word limits.",
     "Do not wait for a rejection email — the page says they are not sent.",
     "Keep fiction under 2,500 words and everything else under 1,500."],
    ["brittle paper", "africa", "african literature", "fiction", "book review", "essay",
     "copyright retained"]))

# ------------------------------------------------------- 7 Boulevard
NEW.append(rec(
    "boulevard", "Boulevard", "Poetry, fiction and nonfiction",
    "Boulevard: up to 8,000 words, $3 fee, four-month response",
    "Boulevard accepts poetry, fiction and nonfiction of up to 8,000 words through Submittable "
    "for a $3 fee. Work must be previously unpublished in print and online, no more than five "
    "poems may be submitted at a time, and authors retain rights to their work from the time of "
    "publication. The average response time is four months.",
    "https://www.boulevardmagazine.org/guidelines/",
    "https://www.boulevardmagazine.org/guidelines/", None, "Submittable — $3 fee",
    src("Boulevard — Guidelines (official)", "https://www.boulevardmagazine.org/guidelines/"),
    {"summary": "No stated country restriction on the guidelines page.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["poetry", "fiction", "creative-nonfiction"], "Poetry, fiction and nonfiction",
    pay(None, None, None, "Not stated on the guidelines page; $3 submission fee applies",
        "The public guidelines page sets out the word limit, the $3 online submission fee, the "
        "response time and the rights position, but publishes no payment rate, so BRYME records "
        "no figure. Confirm the current rate before you submit.",
        "Not publicly stated"),
    {"min": None, "max": 8000, "display": "Up to 8,000 words; no more than five poems at a time"},
    {"label": "Average four months", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Poetry, fiction and nonfiction up to 8,000 words.",
     "No more than five poems at a time.",
     "Work that has not previously been published, in print or online."],
    ["Previously published work, in print or online.",
     "More than five poems in a single submission.",
     "Anything over 8,000 words."],
    ["Submit online through Submittable via the link on the guidelines page.",
     "Pay the $3 online submission fee.",
     "Keep prose under 8,000 words and poems to five per submission.",
     "Confirm the work is unpublished in both print and online before submitting."],
    "Authors retain rights to their work from the time of publication in Boulevard.",
    ["Read https://www.boulevardmagazine.org/guidelines/ and use the Submittable link.",
     "Budget for a four-month response before submitting elsewhere.",
     "Do not submit previously published work in any form."],
    ["boulevard", "poetry", "fiction", "nonfiction", "8000 words", "$3 fee", "submittable",
     "rights retained"]))

# ------------------------------------------------------- 8 Cast of Wonders
NEW.append(rec(
    "cast-of-wonders", "Cast of Wonders", "Young adult speculative short fiction, published as audio",
    "Cast of Wonders: YA speculative fiction up to 6,000 words, read blind",
    "Cast of Wonders is a young adult speculative short fiction market publishing stories up to "
    "6,000 words as audio. Manuscripts are read anonymously and non-anonymous submissions are "
    "rejected unread with no permission to resubmit. It wants science fiction accessible to a "
    "young adult audience, with a minimum of technical jargon.",
    "https://www.castofwonders.org/submissions/",
    "https://www.castofwonders.org/submissions/", None,
    "Online submission — anonymous, read blind",
    src("Cast of Wonders — Submissions (official)",
        "https://www.castofwonders.org/submissions/"),
    {"summary": "No stated country restriction. Writers under 18 may submit but must state their "
                "age, and a parent or legal guardian must sign the contract on their behalf.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["fiction"], "Young adult speculative short fiction",
    pay(None, None, None, "Not stated on the public submissions page",
        "The public submissions page sets out the format, the length and the anonymity rule but "
        "publishes no payment rate, so BRYME records no figure. Confirm the rate before you "
        "submit.",
        "Not publicly stated"),
    {"min": None, "max": 6000, "display": "Up to 6,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "not-stated",
    ["Young adult speculative short fiction up to 6,000 words.",
     "All forms of science fiction — far-future, near future, space opera, hard sci-fi — provided "
     "it is accessible to the target audience with a minimum of technical jargon.",
     "Stories that hold up as audio. The audience listens rather than reads, so they rarely skim "
     "past boring sections.",
     "'Off-cut' stories drawn from a longer work, flagged as such so the biography can carry "
     "purchase links to the related novel.",
     "Translations of non-English fiction, named as a growing area the market wants to support.",
     "Well-researched, respectful and conscientious work."],
    ["Non-anonymous manuscripts, which are rejected unread with no permission to resubmit.",
     "Fiction that denigrates any culture or perpetuates stereotypes.",
     "Heavy technical jargon, which does not survive audio for a young adult audience."],
    ["Submit anonymously — strip identifying information from the manuscript.",
     "Stay under 6,000 words.",
     "If you are under 18, state your age when you submit; a parent or guardian will need to "
     "sign the contract.",
     "Flag off-cut stories so the biography can link to the longer work.",
     "Complete any sensitivity review before submitting — Cast of Wonders cannot fund reviews but "
     "will work with you to incorporate the feedback.",
     "Query first if the guidelines do not answer your question."],
    "Not stated on the official submissions page.",
    ["Read https://www.castofwonders.org/submissions/ — the anonymity rule is strict and the "
     "penalty is rejection unread with no resubmission.",
     "Write for the ear, not the eye.",
     "Do the sensitivity read before you submit, not after."],
    ["cast of wonders", "young adult", "ya", "speculative fiction", "science fiction",
     "audio fiction", "6000 words", "anonymous"]))

# ------------------------------------------------------- 9 Collider
NEW.append(rec(
    "collider", "Collider", "Entertainment news and features",
    "Collider: remote freelance, 2 years' experience, no AI",
    "Collider, the Valnet-owned entertainment site, recruits experienced freelance contributors "
    "for news and features on film, television, video games, comics, music and wider "
    "entertainment. The role is remote, requires two years of experience producing entertainment "
    "content, and Valnet's editorial standards prohibit the use of artificial intelligence. No "
    "rate is published.",
    "https://collider.com/work-with-us/",
    "https://collider.com/work-with-us/", None, "Online application — freelance contributor role",
    src("Collider — Work with us (official)", "https://collider.com/work-with-us/"),
    {"summary": "No stated country restriction. The role is remote and location is the "
                "contributor's choice.",
     "mode": "not-stated", "includesRegions": [], "allowsDiaspora": True, "notStated": True},
    ["journalism", "articles", "reviews"], "Entertainment news and features",
    pay(None, None, None, "Not published; described as consistent and timely payments",
        "The work-with-us page describes consistent and timely payments but publishes no rate, "
        "so BRYME records no figure. The related Valnet brands describe freelance rates as "
        "competitive and negotiable; negotiate yours before you commit.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Not stated on the work-with-us page"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "open", None, "prohibited",
    ["Original, high-quality entertainment content produced in a timely manner.",
     "A dedicated and consistent contributor with quick-response availability for breaking news "
     "and viral trends.",
     "Two years of experience producing entertainment and related content."],
    ["Artificial intelligence. Valnet's editorial standards, which all contributors must follow, "
     "include a prohibition on using AI."],
    ["Apply through https://collider.com/work-with-us/.",
     "Be ready to evidence two years of entertainment content.",
     "Adhere to Valnet's editorial standards, including the AI prohibition.",
     "Treat it as an ongoing contributor role rather than a one-off pitch — consistency and "
     "quick response are stated requirements."],
    "Not stated on the official work-with-us page.",
    ["Read https://collider.com/work-with-us/ and Valnet's editorial standards before applying.",
     "This is a contributor role, not a single-commission pitch.",
     "Negotiate your rate; nothing is published."],
    ["collider", "valnet", "entertainment", "film", "tv", "freelance", "remote", "no ai"]))


BASE = {
    "balkan-insight": ("", "International"),
    "boston-review": ("US", "United States"),
    "east-asia-forum": ("AU", "Australia"),
    "foreign-affairs": ("US", "United States"),
    "dialogue-earth": ("", "International"),
    "brittle-paper": ("", "International"),
    "boulevard": ("US", "United States"),
    "cast-of-wonders": ("", "International"),
    "collider": ("CA", "Canada"),
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
        for r in NEW:
            base, label = BASE[r["slug"]]
            pc[r["slug"]] = {"base": base, "label": label}
        PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Added {len(NEW)} verified records. Total opportunities: {len(opps)}")


# ---------------------------------------------------------------------------
# Probed in batch 2 but NOT added, and why:
#
#   bellingcat.com/about/meet-our-team/  The "guidelines" URL was the staff
#       page, not a submissions route.
#   cnet.com/pictures/submissions-for-...  A photo contest article, not a
#       writing market.
#   care2.com                            Homepage, not a submissions page.
#   entrepreneur.com                     Homepage; no contributor terms in HTML.
#   communication-arts.com/submissions/  Design and illustration submission
#       specs (JPG, RGB, 2300x1200). Not a writing market.
#   americanshortfiction.org             The page that resolved is a prize call
#       ($1,000 first, $250 runner-up, $17 entry, under 1,000 words) - a
#       competition, not the general reading market. Needs the submissions page.
#   autostraddle.com/submissions/        Says only that email pitches are not
#       accepted and points at a form; no rate, length or AI policy in HTML.
#   canadaland.com/pitch-us-your-podcast/ Podcast pitching, not writing.
#   android-police.com/work-with-us/     Real freelance terms (rates
#       "competitive and negotiable") but no rate and no length; held back
#       rather than published thin.
#   boulevard/cast-of-wonders pay        Neither page publishes a rate. Both are
#       included because format, length, fee, rights and response time are all
#       stated; the pay field says "not stated" rather than carrying a guess.
#
#   URL-shape rejects (54 of 160 probed) - the path matched /submissions|
#   /contribute|/guidelines but resolved to a dated article permalink, an image
#   file, a parked domain or an unrelated site. Examples: cv2.ca resolved to a
#   domain auction at whc.ca; engadget resolved to wp.looper.com; folio:
#   resolved to eddie-ozzie.com; book riot and digiday resolved to .jpg files;
#   bella caledonia, bellanaija, chicago tribune, clickhole, crikey, extra.ie,
#   fact magazine and foreign policy all resolved to article permalinks.
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
