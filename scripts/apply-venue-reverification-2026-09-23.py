"""Apply the 2026-09-23 venue re-verification to content/opportunities.json.

Every field below was taken from the publication's own submissions page (or,
where the official page was unreachable, from clearly-labelled secondary
sources with the status downgraded to 'unknown'). Nothing is invented;
anything not confirmed stays empty or unchanged, per the desk's rules.

Run from the repo root: python3 scripts/apply-venue-reverification-2026-09-23.py
"""
import json
from pathlib import Path

P = Path(__file__).resolve().parents[1] / "content" / "opportunities.json"
TODAY = "2026-09-23"

raw = P.read_text(encoding="utf-8")
d = json.loads(raw)
assert raw == json.dumps(d, indent=2, ensure_ascii=False), "unexpected file formatting; aborting"
recs = {r["slug"]: r for r in d["opportunities"]}

def src(name, url):
    return {"name": name, "url": url}

U = {
    "narratively": [
        src("Narratively - Submissions: The Personals (official Submittable page)", "https://narratively.submittable.com/submit/321516/submissions-the-personals")],
    "longreads": [
        src("Longreads - Submissions (official)", "https://longreads.com/submissions/")],
    "wonderslist": [
        src("Wonderslist - Write For Us (official)", "https://www.wonderslist.com/write-us/")],
    "income-diary": [
        src("IncomeDiary - Write for IncomeDiary (official; page content dated 2024)", "https://www.incomediary.com/write-for-incomediary")],
    "communique": [
        src("Communique - How to pitch a Communique story (official)", "https://www.readcommunique.com/p/pitch-communique")],
    "the-offing": [
        src("The Offing - 2026 open calls (fee-free year; dept/length rates)", "https://theoffingmag.com/submit/"),
        src("Brittle Paper - The Offing open and free to submit (Apr 2026)", "https://brittlepaper.com/2026/04/call-for-submissions-literary-magazine-the-offing-is-open-and-free-to-submit/")],
    "griffith-review": [
        src("Griffith Review - submissions (official)", "https://www.griffithreview.com"),
        src("Duotrope - Griffith Review listing (poetry window to 20 Sep 2026)", "https://duotrope.com/magazine/griffith-review-1391")],
    "earth-island-journal": [
        src("Earth Island Journal - writer guidelines (official contact submissions@earthisland.org)", "https://www.earthisland.org")],
    "doek-literary-magazine": [
        src("Doek! Literary Magazine - Issues 17 & 18 call (official windows and limits)", "https://doek.africa/doek-literary-magazine/"),
        src("Brittle Paper - Doek! Issues 17/18 deadlines and eligibility (Feb 2026)", "https://brittlepaper.com/2026/02/doek-literary-magazine-opens-submissions-for-issues-17-and-18-deadlines-march-31-and-september-30-2026/")],
    "torch-literary-arts": [
        src("Torch Literary Arts - Torch Magazine rolling call (official)", "https://torchliteraryarts.org/torchmagazine"),
        src("NYCPlaywrights - Torch one-act plays call with manuscript format", "https://www.nycplaywrights.org/2026/07/torch-literary-arts-seeks-one-act-plays.html")],
    "chestnut-review": [
        src("Chestnut Review - submissions (official; current $120/piece guidelines)", "https://www.chestnutreview.com/submissions/"),
        src("Every Writer's Resource - Chestnut Review listing ($120, 30-day response)", "https://www.everywritersresource.com/literarymagazines/chestnut-review/")],
}

# ---------------------------------------------------------------- narratively
r = recs["narratively"]
r["lastVerified"] = TODAY
r["sources"] = U["narratively"]
r["wordCount"] = {"min": 1000, "max": 2200, "display": "1,000-1,500 words ideal; 2,200 hard max"}
r["whatTheyWant"] = [
    "First-person stories built on vivid, cinematic scenes - one moment, one day, one week, one summer",
    "A subject we have heard about before, but with a unique way in",
    "Active, dramatic narrative - not internal opinion pieces or essays worked out on the page",
    "Surprise: an upside-down view of something society is used to looking at head-on",
]
r["whatTheyDontWant"] = [
    "Pitches for this category - full drafts only",
    "Anything longer than 2,200 words (not considered)",
    "More than one essay in consideration at a time",
]
r["requirements"] = [
    "Full draft, 1,000-1,500 words ideal, 2,200 maximum",
    "Submit one essay at a time; wait for a response before sending another",
    "Rolling consideration - no deadline",
    "Rate: $300 flat per accepted Personals piece",
]
r["howToSubmit"] = [
    "Submit the full draft via Narratively's Submittable page (Submissions: The Personals)",
    "Wait to hear back before submitting another piece",
]

# ------------------------------------------------------------------ longreads
r = recs["longreads"]
r["lastVerified"] = TODAY
r["sources"] = U["longreads"]
r["wordCount"] = {"min": 2000, "max": 6000, "display": "Most features 2,000-6,000 words (guideline, not a rule)"}
r["whatTheyWant"] = [
    "Original nonfiction that sustains a reader's curiosity for the duration",
    "Researched and critical essays (pitches welcome) - rate starts at $500 depending on reporting and length",
    "Personal essays: $500 flat, accepted as full polished drafts only (not commissioned from pitches)",
    "Curated reading lists: $350 - essay-style introduction plus links to free longform web stories; timely or offbeat angles, diverse publications and writers",
]
r["whatTheyDontWant"] = [
    "Fiction of any kind",
    "Reading lists that feature books exclusively",
]
r["requirements"] = [
    "Pitches must state the gist (story and shape), the context (why now, why Longreads) and the length (why the piece needs its word count)",
    "Personal essays: attach the completed draft (PDF, Google Docs or Word) to the email",
    "Essays are fact-checked as necessary",
]
r["howToSubmit"] = [
    "Email essay submissions, pitches, reading-list ideas and queries to hello@longreads.com",
    "Editor's-pick nominations: send the link via Bluesky/X DM or the same email address",
]
r["applyMethod"] = "Email (hello@longreads.com)"
r["applyUrl"] = "https://longreads.com/submissions/"
r["applyEmail"] = "hello@longreads.com"

# -------------------------------------------------------------------- cracked
r = recs["cracked"]
r["lastVerified"] = TODAY
r["submissionStatus"] = "unknown"
r["response"] = {"label": "Official submissions page returned 404 at check (23 Sep 2026); status unconfirmed - treat rates as historical", "band": "unknown", "official": False}
r["sources"] = [src("Cracked - write-for-us page (404 at 23 Sep 2026 check)", "https://www.cracked.com/write-for-cracked"),
                src("Secondary guide: contributor portal via Literally Media; ~$50-250 per piece, paid on publication (2024-2026 reports)", "https://askfoodie.blog/can-you-still-write-for-cracked")]
r["whatTheyWant"] = [
    "High-concept humour, weird history and pop-culture deep dives in the Cracked list style (per secondary reports - unconfirmed by an official page)",
]
r["howToSubmit"] = []

# ---------------------------------------------------------------- whatculture
r = recs["whatculture"]
r["lastVerified"] = TODAY
r["submissionStatus"] = "unknown"
r["response"] = {"label": "Write-for-us page unreachable at check (23 Sep 2026); status unconfirmed", "band": "unknown", "official": False}
r["sources"] = [src("WhatCulture - write for us page (unreachable at 23 Sep 2026 check)", "https://whatculture.com/write-for-us")]
r["howToSubmit"] = []

# ---------------------------------------------------------------- wonderslist
r = recs["wonderslist"]
r["lastVerified"] = TODAY
r["sources"] = U["wonderslist"]
r["wordCount"] = {"min": 1500, "max": None, "display": "Minimum 1,500 words"}
r["whatTheyWant"] = [
    "List articles: exactly 10 items, presented in descending order from #10 to #1",
    "Genuine, factual content - statistics and claims referenced",
    "Informative, engaging lists relevant to the site's topics",
]
r["whatTheyDontWant"] = [
    "Spinned (article-spinner) content - strongly discouraged and ignored",
    "Casinos/gambling, adult content, drugs/alcohol/tobacco, hacking, weapons, violence, content attacking individuals or groups, copyright material",
    "Previously published articles",
]
r["requirements"] = [
    "Minimum 1,500 words, list of 10 in descending order",
    "Include your bio, headshot and any links you want in the post",
    "Good English, free of grammatical and formatting errors",
    "Payment $5 per article via PayPal - include payment details with your submission",
    "On publication Wonderslist becomes the owner of the article (no further copyright)",
]
r["howToSubmit"] = [
    "Email the article to admin@wonderslist.com with payment details",
    "For guest blogging, mention 'Guest Blogging' in the subject line",
    "Expect a reply within about 48 hours",
]
r["response"] = {"label": "Notification within ~48 hours (per guidelines)", "band": "fast", "official": True}
r["rights"] = "On publication, Wonderslist becomes the owner of the article; no further copyright is acceptable."
r["applyMethod"] = "Email (admin@wonderslist.com)"
r["applyEmail"] = "admin@wonderslist.com"

# --------------------------------------------------------------- income-diary
r = recs["income-diary"]
r["lastVerified"] = TODAY
r["sources"] = U["income-diary"]
r["wordCount"] = {"min": 1500, "max": None, "display": "Minimum 1,500 words; listed assignments 2,000+"}
r["whatTheyWant"] = [
    "Expert articles on websites, SEO, traffic, content creation, entrepreneurship and making money online",
    "Interviews with experts; buying/selling websites; affiliate marketing; success-mindset pieces",
    "Professional writers who state their fee on submission (budget quoted at $150-$300 for SEO articles; pay up to $200 for worthy articles)",
]
r["whatTheyDontWant"] = [
    "Republishing anywhere else, including your own blog (copyright transfers to IncomeDiary)",
    "Spun or non-original content",
]
r["requirements"] = [
    "Articles must exceed 1,500 words (2,000+ for the site's listed assignment requests)",
    "Confirm you have read the site's three flagship content/SEO articles in your request",
    "Include examples of previous writing (portfolio) and your fee",
    "Application form asks for target word length, title, description and completion date",
]
r["howToSubmit"] = [
    "Submit your article idea via the form on the Write for IncomeDiary page (or contact page with a quote)",
    "If accepted, full instructions follow by email",
]
r["submissionStatus"] = "unknown"
r["response"] = {"label": "Page is live but its example assignment list is dated 2024 - current demand unconfirmed", "band": "unknown", "official": True}
r["rights"] = "Submitting a post grants IncomeDiary.com copyright ownership; the content may not be published elsewhere."

# ----------------------------------------------------------------- communique
r = recs["communique"]
r["lastVerified"] = TODAY
r["sources"] = U["communique"]
r["wordCount"] = {"min": 1000, "max": 1500, "display": "1,000-1,500 words"}
r["whatTheyWant"] = [
    "Insightful, rigorously reported stories on Africa's media and creative industries - music, film & TV, creator economy, cultural heritage, gaming",
    "Fresh angles, underreported trends, bold investigations",
    "African and diasporic voices centred: creators, entrepreneurs, industry insiders",
    "Hard data: statistics, financial records or original surveys backing the claims",
    "A timely hook - event, policy shift or cultural moment",
]
r["whatTheyDontWant"] = [
    "Surface-level trend pieces without original analysis or data",
]
r["requirements"] = [
    "1,000-1,500 words, beyond-surface analysis with data",
    "You must be subscribed to Communique before submitting",
    "Pay: 150,000 naira per story, or $100 for writers outside Nigeria",
    "Audience of 40,000+ readers; editorial support provided",
]
r["howToSubmit"] = [
    "Subscribe to Communique (free/paid tiers on Substack)",
    "Fill in the submissions Google Form linked from the pitch page",
]
r["applyMethod"] = "Submittable-style form (Google Form; subscription required)"

# ------------------------------------------------------------ statement-africa
r = recs["statement-africa"]
r["lastVerified"] = TODAY
r["submissionStatus"] = "unknown"
r["response"] = {"label": "No active pitch page linked from the current site (last checks 2023-2024 via secondary sources); status unconfirmed", "band": "unknown", "official": False}
r["sources"] = [src("STATEMENT Africa - official site (no pitch page linked at 23 Sep 2026 check)", "https://statementafrica.com"),
                src("Creative Writing News - STATEMENT Africa pitch guidelines (pay up to $1/word; Nov 2023)", "https://www.creativewritingnews.com/statement-africa-is-accepting-pitches-how-to-submit-pay-1-word/")]
r["whatTheyWant"] = [
    "Stories about Africa's creative industries - entertainment (TV/film), music, art, fashion (per 2023-24 guidelines; unconfirmed currently)",
    "Creative challenges, trends, interviews/profiles and industry influences",
    "Features with a strong data component (e.g. a box-office dataset); research support offered",
]
r["howToSubmit"] = []

# ----------------------------------------------------------------- the-offing
r = recs["the-offing"]
r["lastVerified"] = TODAY
r["sources"] = U["the-offing"]
r["whatTheyWant"] = [
    "Work at the edges of genre and form across departments (fiction, nonfiction, poetry; art windows vary)",
    "2026 open calls include Back of the Envelope, Insight, and Translation: Poetry (translations due June 1, 2026 - up to 6 poems, with permission from rights holders)",
    "Original, unpublished-in-English work",
]
r["whatTheyDontWant"] = [
    "Previously published work",
    "Email submissions - Submittable only",
    "More than one submission per department at a time",
]
r["requirements"] = [
    "Free to submit in 2026 (no submission fees, donor-supported); tip-jar option exists",
    "Pay: $25-$100 depending on department and length",
    "Simultaneous submissions allowed",
    "Response can take up to six months",
]
r["howToSubmit"] = [
    "Submit via The Offing's Submittable (check which departments are open before sending)",
    "Translated poetry: include both original language and English, bios for author and translator, rights permission and context notes",
]
r["response"] = {"label": "Up to six months (per guidelines)", "band": "slow", "official": True}
r["rights"] = "Original work, unpublished in English; translated work requires secured permission from the original author or rights holder."

# ------------------------------------------------------------ griffith-review
r = recs["griffith-review"]
r["lastVerified"] = TODAY
r["sources"] = U["griffith-review"]
r["wordCount"] = {"min": 2000, "max": 5000, "display": "~2,000-5,000 words (essays, fiction, features)"}
r["whatTheyWant"] = [
    "Literary essays, reported features, narrative nonfiction and short fiction - 2,000-5,000 words, AUD $0.75 per word",
    "Poetry: open window (per trackers, through 20 September 2026), up to 4 pieces",
    "Emerging Voices programme for early-career writers (recent edition: 3,500-5,000 words; Australian and New Zealand citizens/permanent residents only)",
]
r["whatTheyDontWant"] = [
    "Multiple simultaneous submissions (trackers list the market as no-simultaneous)",
    "Excerpts of longer works",
]
r["requirements"] = [
    "AUD $0.75 per word for accepted essays and fiction",
    "Submissions run to themed editions - check the current call before pitching",
    "Fiction and nonfiction windows have recently opened and closed between editions; poetry may stay open when prose is closed",
]
r["howToSubmit"] = [
    "Submit via Submittable during an open window (the general journal is not open to pitches year-round)",
    "Watch the Emerging Voices call-out for the annual early-career window",
]
r["response"] = {"label": "Not publicly stated; windows open and close by edition", "band": "unknown", "official": False}

# ------------------------------------------------------- earth-island-journal
r = recs["earth-island-journal"]
r["lastVerified"] = TODAY
r["sources"] = U["earth-island-journal"]
r["wordCount"] = {"min": 1200, "max": 3000, "display": "Dispatches 1,200-1,500; features 2,500-3,000 (print ~2,800 common)"}
r["whatTheyWant"] = [
    "Investigative journalism and essays connecting the environment to other contemporary issues",
    "Environmental justice, climate, wildlife and land conservation - especially intersections with social and human rights",
    "On-the-ground reports from outside the US actively welcomed (quarterly print journal)",
    "Personal essays, reflections and think pieces of various lengths for themed editions",
]
r["requirements"] = [
    "Pay: $500 flat for shorter pieces under 1,000 words; $750-$1,500 for longer reports/essays (1,500-3,000 words); $500 for interviews; $400 for book reviews",
    "Print features historically 20-50 cents per word depending on the call",
    "Pitch with clips; accepted features are fact-checked",
]
r["howToSubmit"] = [
    "Email pitches to submissions@earthisland.org",
    "Reference the current edition theme if pitching into a call",
]
r["applyMethod"] = "Email (submissions@earthisland.org)"
r["applyEmail"] = "submissions@earthisland.org"
r["response"] = {"label": "Not publicly stated", "band": "unknown", "official": False}

# ----------------------------------------------------------------------- doek
r = recs["doek-literary-magazine"]
r["lastVerified"] = TODAY
r["pay"] = {"amountMin": None, "amountMax": None, "currency": None, "display": "Unpaid (token payments when funding allows)", "conditions": "No remuneration as of January 2025; Namibian contributors may receive token payments or book vouchers when funding becomes available."}
r["wordCount"] = {"min": 1500, "max": 4500, "display": "Fiction 1,500-4,500; nonfiction 1,500-4,500; poetry no minimum (up to 5 poems per document)"}
r["whatTheyWant"] = [
    "Original, exciting short fiction, nonfiction, poetry and visual art from Namibia and the African diaspora",
    "Strictly pan-African perspectives - work not directed at the white gaze",
    "Themed calls: Issue 18 window runs June 1 - September 30, 2026 (two issues per year)",
]
r["whatTheyDontWant"] = [
    "More than one piece per window (poets may submit up to five poems in one document)",
]
r["requirements"] = [
    "Fiction and poetry eligibility: Namibian citizens (at home or in the diaspora) and foreign nationals permanently residing in Namibia",
    "Nonfiction and visual art eligibility: African writers and artists of African descent, continent-wide or diaspora",
    "Fiction minimum 1,500 words; fiction and nonfiction maximum 4,500 words",
    "No submission fee; submissions via the online form",
]
r["howToSubmit"] = [
    "Send one piece per window via the Doek! submission form during an open window",
    "Poets: up to five poems in a single document",
]
r["rights"] = "Copyright remains with contributors, who license the work exclusively to Doek! for three months from publication."
r["response"] = {"label": "Decisions after each window closes (issues publish June/July and November/December)", "band": "unknown", "official": False}

# ------------------------------------------------------- torch-literary-arts
r = recs["torch-literary-arts"]
r["lastVerified"] = TODAY
r["officialUrl"] = "https://torchliteraryarts.org"
r["applyUrl"] = "https://torchliteraryarts.org/torchmagazine"
r["sources"] = U["torch-literary-arts"]
r["whatTheyWant"] = [
    "Original creative work by Black women writers: poetry, fiction, creative nonfiction, plays and screenplays",
    "Work that challenges and disrupts preconceived notions of what contemporary writing by Black women should be",
    "Selected pieces are published as the Friday Feature - rolling, year-round, no deadline",
]
r["whatTheyDontWant"] = [
    "Submissions without a cover letter (may not be read)",
]
r["requirements"] = [
    "$150 flat for every accepted Friday Feature",
    "One-page cover letter with title(s) and a brief bio (does not count toward page count)",
    "Word/PDF, typed, double-spaced (poetry may be single-spaced), numbered pages, 1-1.5 inch margins",
    "Drama/screenwriting: one act or short scene collection, max 15 pages; self-contained excerpts welcome",
]
r["howToSubmit"] = [
    "Submit via Submittable at torchliteraryarts.org/torchmagazine",
    "Indicate if a performance video or audio reading is available if selected (for scripts)",
]
r["applyMethod"] = "Submittable"
r["response"] = {"label": "Rolling - features selected weekly (Fridays)", "band": "fast", "official": True}

# ------------------------------------------------------------ chestnut-review
r = recs["chestnut-review"]
r["lastVerified"] = TODAY
r["sources"] = U["chestnut-review"]
r["whatTheyWant"] = [
    "Poetry (up to six poems; three for the free tier), flash fiction and creative nonfiction under 1,000 words, prose 1,000-5,000 words, visual art and photography",
    "Work showing persistence and creative tenacity - 'for stubborn artists'",
    "Primarily English work, including work engaging with other languages and cultures",
]
r["whatTheyDontWant"] = [
    "Previously published work (online or print)",
    "AI-generated content",
    "Translations",
    "Excerpts of longer works (prose)",
]
r["requirements"] = [
    "$120 per accepted piece, every writer and artist paid",
    "Flash submissions free; minimal fees for longer prose categories; optional paid staff-reader feedback",
    "Simultaneous submissions considered",
    "Contributors receive a copy of the annual print anthology; quarterly online, annually in print",
]
r["howToSubmit"] = [
    "Submit via the Submittable page for your genre (see chestnutreview.com/submissions)",
    "Poems single-spaced, each starting on a new page; one flash piece at a time",
]
r["response"] = {"label": "About 30 days", "band": "fast", "official": True}
r["aiPolicy"] = "no-ai"
r["rights"] = "Unpublished work only; contributors receive the annual anthology copy."

# ------------------------------------------------------------------- finalize
d["updatedAt"] = TODAY
out = json.dumps(d, indent=2, ensure_ascii=False)
assert out != raw, "nothing changed?"
P.write_text(out, encoding="utf-8")
changed = sum(1 for r in d["opportunities"] if r.get("lastVerified") == TODAY)
print(f"updated {changed} venue records; updatedAt -> {TODAY}")
