#!/usr/bin/env python3
"""Add the verified Canada publication batch (2026-09-06).

Same standard as the UK batch: every figure was read off the publication's
own live guidelines page on 2026-09-06 (raw text saved in
/home/user/research/ca/*.txt). Aggregator listings were used only to find
candidate URLs and were contradicted by source in several cases -- PRISM was
listed by third parties as $30/page (actual: $40 prose / $45 poetry), EVENT as
$25 or $30/page (actual: $35 prose / $40 poetry).

Per-word rates follow the existing repo convention: amountMin/amountMax stay
None unless the publication states a per-piece floor or cap, because a
per-word rate is not a piece amount and must not sort as one.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPPS = ROOT / "content/opportunities.json"
PUBC = ROOT / "content/hub/pub-countries.json"
V = "2026-09-06"


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

# -------------------------------------------------------------- 1 Briarpatch
NEW.append(rec(
    "briarpatch", "Briarpatch Magazine", "Non-fiction pitches",
    "Briarpatch: $150–$350 per article, pitch deadline 18 September 2026",
    "Briarpatch pays $150 for profiles, short essays and reviews, $250 for features and photo essays, and $350 for research-based and investigative reporting. The pitch deadline for the Winter 2027 'AI Resistance' issue is 18 September 2026.",
    "https://briarpatchmagazine.com/submissions",
    "mailto:pitch@briarpatchmagazine.com", "pitch@briarpatchmagazine.com",
    "Email pitch",
    src("Briarpatch — Submissions (official)", "https://briarpatchmagazine.com/submissions"),
    {"summary": "No nationality restriction stated on the submissions page. Briarpatch is a Saskatchewan-based magazine of grassroots politics, labour, ecology and social justice.",
     "mode": "not-stated", "notStated": True},
    ["journalism", "essays", "reviews", "analysis"], "Reported features, essays, reviews and investigations",
    pay("CAD", 150, 350, "$150–$350 per article",
        "Official standard rates: $150 for profiles, short essays, reviews, reading lists, online-only articles and parting shots (generally 1,500 words or less); $250 for feature stories (generally 1,500–2,000 words) and photo essays; $350 for research-based articles and investigative reporting with extensive primary research (generally 2,000–2,500 words). Online-only stories pay $150. Illustration is paid separately: $100 spot, $150 feature, $300 cover.",
        "Not publicly stated"),
    {"min": 700, "max": 2500, "display": "700–2,500 words depending on section"},
    {"label": "Within a week or two after the pitch deadline; assume no after three weeks", "band": "2-4-weeks", "official": True},
    "deadline",
    {"date": "2026-09-18", "display": "Winter 2027 'AI Resistance' issue — pitch deadline 18 September 2026. Spring 2027 (unthemed) deadline TBA.",
     "windowEnd": "2026-09-18", "recurring": True},
    "not-stated",
    ["Pitches on grassroots activism, current events, electoral politics, economic justice, ecology, labour, food security, gender equity, Indigenous struggles and international solidarity.",
     "Your contact information, an estimated word count, a list of recent publications if applicable, and a short writing sample.",
     "Back-page opinion: 700–800 word thoughtful pieces and well-aimed jabs that challenge readers.",
     "Be prepared to take your piece through two or three rewrites over the course of a month."],
    ["Features much beyond 2,500 words — they occasionally accept longer only when the topic and skill warrant it.",
     "An assumption that they will chase you. If you do not hear back within three weeks of the pitch deadline, assume it is a no."],
    ["Email pitch", "Estimated word count", "Short writing sample", "Expect 2–3 rewrites"],
    "Not stated on the submissions page.",
    ["Read https://briarpatchmagazine.com/submissions and their guide to pitching Briarpatch.",
     "Check the editorial schedule for the issue theme you want to write for.",
     "Email your pitch to pitch@briarpatchmagazine.com before the 18 September 2026 deadline."],
    ["briarpatch", "canada", "saskatchewan", "investigative", "social justice", "cad"]))

# --------------------------------------------------------------- 2 Broadview
NEW.append(rec(
    "broadview", "Broadview", "Opinion and reported features",
    "Broadview: 40¢ a word for opinion, 65¢ a word for reported pieces",
    "Broadview, an award-winning Canadian magazine on faith, ethics and justice, pays 40 cents a word for opinion pieces and 65 cents a word for reported ones. Pitches go by email to the editor and payment lands within 30 days of invoice.",
    "https://broadview.org/submission-guidelines/",
    "mailto:j.bell@broadview.org", "j.bell@broadview.org",
    "Email query or manuscript to the Editor",
    src("Broadview — Submission guidelines (official)", "https://broadview.org/submission-guidelines/"),
    {"summary": "No nationality restriction stated. Broadview is Canadian and follows Canadian Press style and the Canadian Oxford Dictionary, so stories are pitched to a Canadian readership.",
     "mode": "not-stated", "notStated": True},
    ["journalism", "opinion", "essays", "analysis"], "Opinion and reported features",
    pay("CAD", None, None, "40¢ a word (opinion), 65¢ a word (reported)",
        "Official: \"We pay $.40 a word for opinion pieces and $.65 a word for reported ones.\" Digital and print pieces are both paid by the word. You are paid only for the words you were assigned, unless a revised length is agreed with your handling editor. The guidelines write the rate as $ without naming the currency; Broadview is a Canadian publication following Canadian Press style, so it is recorded here as CAD. Per repo convention a per-word rate carries no piece amount.",
        "Within 30 days of receipt of an invoice"),
    {"min": None, "max": None, "display": "Assigned per commission"},
    {"label": "Print issues are planned about six months ahead; online stories days to weeks ahead", "band": "not-stated", "official": True},
    "open", None, "not-stated",
    ["Crisp perspectives on faith, ethics and justice — human rights and social issues, spirituality, inspiring human interest stories, the environment, culture and mental health.",
     "A query or manuscript by email to the Editor.",
     "Time-sensitive ideas pitched with their lead times in mind: about six months for print, days to weeks for online."],
    ["Missing your assigned deadline without telling them — they can often extend, but they get nervous in silence.",
     "Work that is not original and unpublished."],
    ["Email pitch to the Editor", "Canadian Press style", "Invoice required for payment"],
    "Broadview buys first North American rights in English and French, plus the right to archive the story and post it on Broadview.org.",
    ["Read the full guidelines at https://broadview.org/submission-guidelines/.",
     "Email your query or manuscript to Jocelyn Bell, Editor, at j.bell@broadview.org.",
     "Invoice after publication — payment follows within 30 days."],
    ["broadview", "canada", "faith", "ethics", "justice", "cad"]))

# --------------------------------------------------------- 3 Malahat Review
NEW.append(rec(
    "the-malahat-review", "The Malahat Review", "Fiction, poetry and creative non-fiction",
    "The Malahat Review: CAD$70 per published page",
    "The Malahat Review, based at the University of Victoria, pays CAD$70 per published page plus a one-year subscription and two copies. Submissions go through Submittable only. International submitters, including from the US, pay a CAD$7 fee.",
    "https://malahatreview.ca/submission_guidelines.html",
    "https://malahatreview.submittable.com/submit", None,
    "Submittable only",
    src("The Malahat Review — Submission guidelines (official)", "https://malahatreview.ca/submission_guidelines.html"),
    {"summary": "Open internationally. Their four annual contests are explicitly open to Canadian and international writers alike. They note that writers of certain backgrounds and religions have been historically under-represented in Canadian literary contexts and welcome that work.",
     "mode": "open", "notStated": False},
    ["fiction", "poetry", "creative-nonfiction"], "Fiction, poetry and creative non-fiction",
    pay("CAD", 70, 70, "CAD$70 per published page",
        "Official: \"We pay CAD$70 per published page plus a one-year print subscription and two copies of the issue in which your work appears.\" Note a CAD$7 fee (approximately USD$5) per regular submission for international submitters, including from the US. Their four annual contests have separate guidelines and their own entry fees.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "Paid per published page"},
    {"label": "One to six months for poetry; up to nine months for fiction and creative non-fiction", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Fiction, poetry and creative non-fiction submitted through Submittable as a single .doc, .docx or .pdf.",
     "A word count for prose, or a line count for poetry, listed at the beginning of each piece.",
     "Your name and contact info included for regular submissions."],
    ["Work excerpted elsewhere, or any work revised since its original publication — neither is eligible.",
     "Simultaneous submissions to their contests.",
     "AI-generated work — their Editorial Boards state they are not interested in it."],
    ["Submittable only", "CAD$7 fee for international submitters", "Word or line count at the start"],
    "Not fully stated on the guidelines page.",
    ["Order or read an issue first to see what they publish.",
     "Read https://malahatreview.ca/submission_guidelines.html and check the reading period.",
     "Submit via Submittable, paying the CAD$7 fee if you are outside Canada."],
    ["malahat review", "canada", "victoria", "fiction", "poetry", "cad"]))

# ------------------------------------------------------- 4 The New Quarterly
NEW.append(rec(
    "the-new-quarterly", "The New Quarterly", "Fiction, poetry and non-fiction",
    "The New Quarterly: $400 for prose, $100 for poetry — Canadian writers only",
    "The New Quarterly pays $400 for fiction and non-fiction pieces and $100 per poem. It publishes exclusively Canadian writers and actively nurtures emerging writers who have not yet published a full book. Submission periods are fixed and responses take 6–7 months.",
    "https://tnq.ca/submit/",
    "https://tnq.ca/submit/", None,
    "Genre-specific submission forms during an open period",
    src("The New Quarterly — Submit (official)", "https://tnq.ca/submit/"),
    {"summary": "Official and strict: The New Quarterly publishes fiction, poetry and creative non-fiction exclusively by Canadian writers. They particularly seek to nurture emerging writers — those who have not yet published a full book — alongside established names.",
     "mode": "restricted", "includesRegions": ["canada"], "allowsDiaspora": False, "notStated": False},
    ["fiction", "poetry", "creative-nonfiction"], "Fiction, poetry and non-fiction",
    pay("CAD", 100, 400, "$400 prose / $100 poetry",
        "Official payment rates: \"For Fiction and Nonfiction pieces, we pay $400. For Poetry and Postscripts, we pay $100 per piece.\" Contributors also get a complimentary copy of the issue their piece appears in and a contributor discount on TNQ subscriptions.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "One piece per submission period"},
    {"label": "6–7 months from the time the submission period opened", "band": "3-plus-months", "official": True},
    "upcoming",
    {"display": "Fiction and poetry: 1 February–30 April (response by end of June) and 1 July–30 September (response by end of January). Non-fiction runs to its own periods — check the page.",
     "windowEnd": "2026-09-30", "recurring": True},
    "not-stated",
    ["Writing that questions, challenges and responds.",
     "Work by Canadian writers only — with an active interest in emerging writers who have not yet published a full book.",
     "Double-spaced work with a word count at the end, page numbers on prose or multi-page poems, and your name on every page.",
     "One piece per submission period. They recommend submitting in the first couple of months of a period."],
    ["Submissions from writers who are not Canadian.",
     "More than one piece per period."],
    ["Genre-specific form", "Canadian writers only", "One piece per period", "Name on every page"],
    "Not stated on the submit page.",
    ["Confirm you are eligible — TNQ publishes Canadian writers exclusively.",
     "Check the submission periods at https://tnq.ca/submit/ for your genre.",
     "Submit early in the window through the genre-specific form."],
    ["the new quarterly", "canada", "canadian writers", "emerging writers", "cad"]))

# ---------------------------------------------------- 5 PRISM international
NEW.append(rec(
    "prism-international", "PRISM international", "Fiction, non-fiction, poetry and translation",
    "PRISM international: $40 per page for prose, $45 for poetry",
    "PRISM international, run out of UBC, pays $40 CAD per printed page for prose and $45 CAD per printed page for poetry, plus two contributor copies. It publishes writing and translation from Canada and around the world. Reply times run six to twelve months.",
    "https://prismmagazine.ca/submit/",
    "https://prism.submittable.com/submit", None,
    "Submittable",
    src("PRISM international — Submit (official)", "https://prismmagazine.ca/submit/"),
    {"summary": "Open internationally — their mandate is to publish \"the best in contemporary writing and translation from Canada and around the world.\" They ask for a bio of 50 words or fewer that references where you live.",
     "mode": "open", "notStated": False},
    ["fiction", "creative-nonfiction", "poetry", "translation"], "Fiction, non-fiction, poetry and translation",
    pay("CAD", 40, 45, "$40 CAD/page prose, $45 CAD/page poetry",
        "Official: \"We purchase first North American serial rights and pay $40 CAD per printed page for prose and $45 CAD per printed page for poetry.\" Contributors also receive two copies. Translations: $45 CAD/page for poetry translation plus $30 CAD/page to the original author; $40 CAD/page for prose translation plus $25 CAD/page to the original author up to $200 CAD. Art: $300 CAD for a cover, $50 CAD per interior page up to $250 CAD. Third-party directories list $30/page — that is out of date; this is the figure on PRISM's own page.",
        "Not publicly stated"),
    {"min": None, "max": 4000, "display": "Preferred length 4,000 words or less"},
    {"label": "Six to twelve months; they may not be able to respond to everyone", "band": "3-plus-months", "official": True},
    "open", None, "not-stated",
    ["Fiction and creative non-fiction up to about 4,000 words, including flash.",
     "Up to four poems for a maximum of six pages.",
     "A cover letter with your contact information and a bio of 50 words or fewer referencing where you live.",
     "For translations: a copy of the original work, plus confirmed permission from the original author or rights holder."],
    ["More than one piece at a time, unless submitting for a specific call.",
     "Translations without permission from the rights holder — they will ask to see it before publishing."],
    ["Submittable", "Bio of 50 words or fewer", "One piece at a time", "Preferred length 4,000 words"],
    "PRISM purchases first North American serial rights.",
    ["Read https://prismmagazine.ca/submit/ and check which category is open.",
     "Prepare a cover letter with a 50-word bio that says where you live.",
     "Submit through Submittable."],
    ["prism international", "canada", "ubc", "translation", "fiction", "poetry", "cad"]))

# ------------------------------------------------------------------ 6 EVENT
NEW.append(rec(
    "event-magazine", "EVENT", "Fiction, poetry and reviews",
    "EVENT: $40 per page for poetry, $35 for prose, up to $500",
    "EVENT pays $40 per page for poetry and book reviews and $35 per page for prose, up to a maximum of $500, plus two copies. Fiction and poetry windows open in January, July, August and December only, and each closes early once the submission cap is hit.",
    "https://www.eventmagazine.ca/submit/",
    "https://eventmagazine.submittable.com/submit", None,
    "Submittable during an open month",
    src("EVENT — Submit (official)", "https://www.eventmagazine.ca/submit/"),
    {"summary": "No nationality restriction stated for general submissions, though some categories carry their own eligibility requirements on Submittable — the August 2026 fiction and poetry calls were flagged as Canadian.",
     "mode": "not-stated", "notStated": True},
    ["fiction", "poetry", "reviews", "creative-nonfiction"], "Fiction, poetry and reviews",
    pay("CAD", 35, 40, "$40/page poetry and reviews, $35/page prose (max $500)",
        "Official: \"We pay $40/page for poetry and book reviews, and $35/page for prose, up to a maximum of $500.\" All contributors receive 2 copies of the issue. Third-party directories list $25 or $30 per page — both are out of date; this is the figure on EVENT's own page.",
        "Issued upon publication"),
    {"min": None, "max": 5000, "display": "Up to six poems, or one short story to 5,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "upcoming",
    {"display": "Fiction and poetry are accepted in January, July, August and December only. Canadian Fiction and Canadian Poetry (August 2026) hit their caps and closed. Non-fiction comes mainly through the annual Non-Fiction Contest, deadline 15 October.",
     "openingDate": "2026-12-01", "recurring": True},
    "prohibited",
    ["Fiction: stories, moments and narratives that move them.",
     "Poetry: arresting imagery, polished language, emotional impact, and lyricism without pretension.",
     "Up to six poems, or one short story of maximum 5,000 words, at a time — in one genre only.",
     "Each poem or story saved as its own separate .doc, .docx, .rtf or .txt file."],
    ["Work produced with artificial intelligence tools such as ChatGPT.",
     "PDFs.",
     "Submissions in more than one genre at a time, or another piece before you have had a response.",
     "Submissions after the monthly cap is reached — windows close early."],
    ["Submittable", "Open months only", "One genre at a time", "No PDFs"],
    "See their Editorial Policy for rights and payment policies.",
    ["Check https://www.eventmagazine.ca/submit/ — windows are January, July, August and December, and close early when capped.",
     "Save each poem or story as its own file, not a PDF.",
     "Submit via Submittable in one genre only."],
    ["event magazine", "canada", "british columbia", "fiction", "poetry", "cad"]))

# ------------------------------------------------------------ 7 Prairie Fire
NEW.append(rec(
    "prairie-fire", "Prairie Fire", "Fiction, poetry and creative non-fiction",
    "Prairie Fire: 10¢ per word for prose, $40 per poem",
    "Prairie Fire, a Winnipeg quarterly, pays 10 cents per word for prose to a maximum of $250 per piece, and $40 per poem, plus a contributor's copy. AI-generated text of any kind is refused. Response takes three to six months.",
    "https://prairiefire.ca/submissions/",
    "https://prairiefire.submittable.com/submit", None,
    "Submittable",
    src("Prairie Fire — Rates of Payment and Submissions (official)", "https://prairiefire.ca/rates-of-payment/"),
    {"summary": "No nationality restriction stated on the submissions page.", "mode": "not-stated", "notStated": True},
    ["fiction", "poetry", "creative-nonfiction", "interviews"], "Fiction, poetry and creative non-fiction",
    pay("CAD", 40, 250, "10¢ per word prose (max $250), $40 per poem",
        "Official print rates: Prose $0.10 per word; Poetry $40 per poem. Maximum fee $250 for short fiction and excerpts from longer works, and $250 for articles, creative non-fiction, editorials, essays and memoirs. Interviews and profiles: subject $75. Payment includes one free contributor's copy. Anything not covered by the rate sheet is negotiated separately, and rates are subject to change without notice.",
        "Following publication"),
    {"min": None, "max": None, "display": "Maximum 5 poems per submission"},
    {"label": "Generally three to six months", "band": "3-plus-months", "official": True},
    "open", None, "prohibited",
    ["Fiction, poetry and creative non-fiction, with a word count at the top right of the first page and your address at the top left.",
     "Numbered pages, a maximum of 5 poems per submission.",
     "A twelve-month gap between submissions — once you submit, wait a year before submitting again."],
    ["Work that uses AI, algorithmic, machine-learning or computer-generated text of any sort.",
     "Work that promotes intolerance.",
     "Revisions, replacements or substitutions once you have submitted.",
     "Previously published work, including work published with a digital publication."],
    ["Submittable", "Word count on page one", "Max 5 poems", "Twelve-month gap between submissions"],
    "Prairie Fire buys First North American Serial Rights and First Digital Publication Rights only. Rights are reassigned to the author upon publication.",
    ["Read the rate sheet at https://prairiefire.ca/rates-of-payment/ and the guidelines at /submissions/.",
     "Format with word count top-right and address top-left of page one, pages numbered.",
     "Submit via Submittable, then wait twelve months before submitting again."],
    ["prairie fire", "canada", "winnipeg", "fiction", "poetry", "cad", "no ai"]))

# ------------------------------------------------------------------ 8 Augur
NEW.append(rec(
    "augur-magazine", "Augur Magazine", "Speculative fiction and poetry",
    "Augur Magazine: CAD $0.14 per word for fiction, $100 per poem",
    "Augur Magazine pays CAD $0.14 per word for short fiction over 800 words, a flat $112 for flash fiction, and $100 CAD per poem. It publishes dreamy, speculative and surreal work, prohibits AI-generated submissions, and tracks Canadian and international quotas for its funders.",
    "https://augurmag.com/submissions/",
    "https://augur.moksha.io/publication/augur", None,
    "Moksha submissions portal",
    src("Augur Magazine — Submissions (official)", "https://augurmag.com/submissions/"),
    {"summary": "Open internationally. Canadian granting bodies require Augur to track quotas, so submitters are asked to identify as from Canada/Turtle Island or as International — but they explicitly allow you to exempt yourself from that requirement. They invite Indigenous creators to self-identify their citizenship however feels most accurate.",
     "mode": "open", "notStated": False},
    ["fiction", "poetry"], "Speculative fiction and poetry",
    pay("CAD", 100, 112, "CAD $0.14/word fiction, $112 flash, $100 per poem",
        "Official: \"We pay $0.14 cents (CAD) per word for short fiction (800+ words), and a flat fee of $112.00 per flash fiction piece (800 words and under).\" For poetry: \"We pay $100.00 CAD per poem.\" The piece figures recorded here are the two flat fees; the per-word fiction rate is not a piece amount and so carries no separate figure, per repo convention.",
        "Not publicly stated"),
    {"min": None, "max": 5000, "display": "Fiction to 5,000 words; up to 5 poems / 10 pages"},
    {"label": "Query if you have not heard by the end of October 2026", "band": "1-3-months", "official": True},
    "closed",
    {"display": "Submissions are currently closed. Translation submissions are closed for both Augur and Tales & Feathers; Tales & Feathers is closed for all of 2026.", "recurring": True},
    "prohibited",
    ["Speculative, dreamlike and surreal fiction and poetry.",
     "Fiction in standard manuscript format as a .doc or .docx, with no identifying information, maximum one story per call.",
     "Poetry: up to 5 poems to a maximum of 10 pages, all in one package.",
     "Optionally, an indication of your intersections — not required, and treated as confidential."],
    ["AI-generated submissions. The text must be ideated and written by a human; an AI-written piece is a breach of contract if accepted.",
     "Reprints, or pieces you have submitted before unless significantly revised.",
     "Stories longer than 5,000 words for Augur.",
     "Submissions if they have published you two years running in the same market — take a break."],
    ["Moksha portal", "No identifying information on fiction", "Max 1 story or 5 poems", "Human-written only"],
    "Not stated on the submissions page.",
    ["Read https://augurmag.com/submissions/ and their published work to check the fit.",
     "Wait for a submissions call — they are currently closed.",
     "Submit via Moksha; you should get a verification email."],
    ["augur", "canada", "speculative fiction", "poetry", "cad", "no ai"]))

# ------------------------------------------------------------------ 9 Geist
NEW.append(rec(
    "geist", "Geist", "Non-fiction, fiction, poetry and comics",
    "Geist: up to $650 for features, $100 per page for poetry",
    "Geist, a Canadian magazine of ideas and culture, pays up to $650 for longform essays, fiction and comics, $100 per page for poetry, and $100–300 for short non-fiction in Notes & Dispatches. It prioritises Canadians and permanent residents, or work with a strong Canadian connection.",
    "https://www.geist.com/submit/",
    "https://www.geist.com/submit/", "submit@geist.com",
    "Submission form on their site",
    src("Geist — Submission Guidelines (official)", "https://www.geist.com/submit/"),
    {"summary": "Official: their priority is work from emerging and established writers and artists who are Canadian or permanent residents of Canada, or whose work has a strong connection to Canada or would be relevant to a Canadian audience. They encourage submissions from Black writers, Indigenous writers, writers of colour, writers with disabilities and LGBTQIA2S+ writers.",
     "mode": "restricted", "includesRegions": ["canada"], "allowsDiaspora": True, "notStated": False},
    ["creative-nonfiction", "fiction", "poetry", "essays"], "Non-fiction, fiction, poetry and comics",
    pay("CAD", 100, 650, "Up to $650; $100/page poetry",
        "Official rates by section: Longform essays up to 5,000 words, published as Features — up to $650. Fiction (short stories up to 5,000 words) — up to $650. Comics — up to $650. Poetry — $100 per page. Short non-fiction under 2,000 words for Notes & Dispatches — pay is commensurate with length, usually $100–300. Art and photography — between $50 and $120.",
        "Not publicly stated"),
    {"min": None, "max": 5000, "display": "Notes & Dispatches under 2,000 words; Features up to 5,000"},
    {"label": "Not stated; due to volume you may not hear back", "band": "not-stated", "official": True},
    "open", None, "not-stated",
    ["Short non-fiction under 2,000 words, typically personal narrative, for Notes & Dispatches — they are always seeking this.",
     "Longform essays up to 5,000 words: innovative, thoughtfully researched and emotionally resonant narrative non-fiction.",
     "Work that takes the shape of lists, letters, instructions or other unconventional structures, matching creativity with intellectual rigour.",
     "Comics that are weird, funny, unexpected or experimental. Poetry: a maximum of 5 poems."],
    ["Work with no connection to Canada or relevance to a Canadian audience.",
     "More than your best single short story — they usually publish one per issue."],
    ["Submission form", "Canadian connection", "Read several issues first"],
    "Geist purchases first North American Serial Rights and non-exclusive electronic rights. Copyright reverts to the author after publication. They may use part of the work for promotional purposes.",
    ["Read several issues of Geist, or the archives at geist.com, before submitting.",
     "Pick the right section — Notes & Dispatches is the most open door at under 2,000 words.",
     "Submit through the form at https://www.geist.com/submit/."],
    ["geist", "canada", "ideas", "culture", "essays", "cad"]))

# -------------------------------------------------------------- 10 FreeFall
NEW.append(rec(
    "freefall-magazine", "FreeFall Magazine", "Prose, poetry, interviews and reviews",
    "FreeFall Magazine: $10 per page for prose, $25 per poem, $50 for reviews",
    "FreeFall Magazine, based in Calgary, pays $10 per published page for prose to a maximum of $100, $25 per poem, and $50 for interviews and book reviews, plus a contributor copy. Prose runs to 4,000 words and responses take two weeks to six months.",
    "https://freefallmagazine.ca/submissions/",
    "https://freefallmagazine.ca/submissions/", None,
    "Online submission form",
    src("FreeFall Magazine — Submissions (official)", "https://freefallmagazine.ca/submissions/"),
    {"summary": "No nationality restriction stated on the submissions page.", "mode": "not-stated", "notStated": True},
    ["fiction", "poetry", "creative-nonfiction", "reviews", "interviews"], "Prose, poetry, interviews and reviews",
    pay("CAD", 10, 50, "$10/page prose (max $100), $25/poem, $50 reviews",
        "Official: Prose — \"Payment is $10 per page in the magazine (to a maximum of $100) and one copy of the issue.\" Poetry — \"Payment is $25 per poem and one copy of the issue.\" Interviews and book reviews — \"Payment is $50 and one copy of the issue.\" All payments are made upon publication.",
        "Upon publication"),
    {"min": None, "max": 4000, "display": "Prose to 4,000 words; poems max 6 pages each"},
    {"label": "Anywhere from 2 weeks to 6 months", "band": "1-3-months", "official": True},
    "open", None, "not-stated",
    ["Prose up to 4,000 words: short stories and novel excerpts, non-fiction on writing-related or general-audience topics, creative non-fiction, plays and postcard stories.",
     "Poetry: 1–3 poems of any style, with no individual poem exceeding 6 pages.",
     "Interviews and book reviews: send a proposal query only — guidelines follow once the proposal is approved."],
    ["Previously published work, online or digital.",
     "Interviews or reviews submitted in full without an approved proposal first."],
    ["Online form", "Prose max 4,000 words", "Proposal query for interviews and reviews"],
    "FreeFall buys First North American Serial Rights and First Digital Publication Rights only. Copyright returns to the author after publication.",
    ["Read https://freefallmagazine.ca/submissions/ and pick your category.",
     "For interviews or reviews, send a proposal query first.",
     "Submit through the online form and expect anywhere from 2 weeks to 6 months."],
    ["freefall", "canada", "calgary", "prose", "poetry", "cad"]))

# ------------------------------------------------------- 11 The /tEmz/ Review
NEW.append(rec(
    "the-temz-review", "The /tEmz/ Review", "Fiction, creative non-fiction and poetry",
    "The /tEmz/ Review: $20 per piece, open 1 September–31 October",
    "The /tEmz/ Review pays $20 per prose piece and $20 per batch of poems. It is open for journal submissions from 1 September to 31 October 2026 and takes prose up to 10,000 words. AI use is allowed only where fully disclosed.",
    "https://thetemzreview.com/submissions",
    "https://thetemzreview.moksha.io/publication/the-temz-review", None,
    "Moksha submissions manager",
    src("The /tEmz/ Review — Submit (official)", "https://thetemzreview.com/submissions"),
    {"summary": "No nationality restriction stated. They are looking for innovative short fiction from diverse voices and a wide range of styles and voices.",
     "mode": "not-stated", "notStated": True},
    ["fiction", "creative-nonfiction", "poetry"], "Fiction, creative non-fiction and poetry",
    pay("CAD", 20, 20, "$20 per piece",
        "Official: \"We pay $20 per piece\" for prose, and \"We pay $20 per batch of poems we publish.\" Reviews and interviews are handled separately and are not submitted through Moksha — contact them if you want to write one.",
        "Not publicly stated"),
    {"min": None, "max": 10000, "display": "Prose up to 10,000 words"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "deadline",
    {"date": "2026-10-31", "display": "Open for journal submissions 1 September – 31 October 2026",
     "windowStart": "2026-09-01", "windowEnd": "2026-10-31", "recurring": True},
    "disclosure-required",
    ["Innovative short fiction from diverse voices, and a wide range of styles and voices.",
     "Prose (fiction and creative non-fiction) up to 10,000 words. They will consider longer, but it needs to earn its length.",
     "Several short pieces at once if each is under 1,000 words — otherwise only one piece.",
     "Full disclosure of any AI use in your cover letter: the extent of it, and the reasons for it."],
    ["Undisclosed AI-generated material. They accept that there are legitimate artistic reasons to use AI, but submitting it without accurately disclosing the nature and extent will be treated seriously.",
     "More than one submission per reading period.",
     "Reviews or interviews through Moksha — contact them directly instead."],
    ["Moksha", "Open window only", "One submission per reading period", "AI use must be disclosed"],
    "Not stated on the submit page.",
    ["Read https://thetemzreview.com/submissions and the policies in full.",
     "If you used AI in any way, state the extent and the reasons in your cover message.",
     "Submit through Moksha before 31 October 2026."],
    ["temz review", "canada", "ontario", "fiction", "poetry", "cad"]))

# ------------------------------------------------------------ 12 carte blanche
NEW.append(rec(
    "carte-blanche", "carte blanche", "Fiction, non-fiction, poetry and translation",
    "carte blanche: pays an honorarium per published submission",
    "carte blanche, published by the Quebec Writers' Federation, pays a modest honorarium per submission. It publishes fiction, non-fiction, poetry and translation, with spring and fall reading periods and no submission fee.",
    "https://carte-blanche.org/submissions/",
    "https://carte-blanche.org/submissions/", None,
    "Submittable",
    src("carte blanche — Submissions (official)", "https://carte-blanche.org/submissions/"),
    {"summary": "No nationality restriction stated. carte blanche is published by the Quebec Writers' Federation.",
     "mode": "not-stated", "notStated": True},
    ["fiction", "creative-nonfiction", "poetry", "translation"], "Fiction, non-fiction, poetry and translation",
    pay("CAD", None, None, "Modest honorarium — amount not stated",
        "Official: \"carte blanche pays a modest honorarium per submission.\" No figure is published, so BRYME states none rather than guessing.",
        "Not publicly stated"),
    {"min": None, "max": None, "display": "See the guidelines for each genre"},
    {"label": "Not stated", "band": "not-stated", "official": False},
    "upcoming",
    {"display": "Spring and Fall reading periods. Check the submissions page for the current window.", "recurring": True},
    "not-stated",
    ["Fiction, creative non-fiction, poetry and translation submitted through Submittable.",
     "Work that fits a magazine published by the Quebec Writers' Federation."],
    ["Submissions outside an open reading period."],
    ["Submittable", "Open reading period"],
    "Not stated on the submissions page.",
    ["Check https://carte-blanche.org/submissions/ for the current reading period.",
     "Read recent issues to see the range they publish.",
     "Submit via Submittable."],
    ["carte blanche", "canada", "quebec", "translation", "cad"]))


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

    pc = json.loads(PUBC.read_text(encoding="utf-8"))
    for r in NEW:
        pc[r["slug"]] = {"base": "CA", "label": "Canada"}
    PUBC.write_text(json.dumps(pc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Added {len(NEW)} Canada records. Total opportunities: {len(opps)}")
    stated = [r for r in NEW if r["pay"]["amountMin"] is not None]
    print(f"  with a stated piece figure: {len(stated)}")
    print(f"  per-word or unstated: {len(NEW) - len(stated)}")


if __name__ == "__main__":
    main()
