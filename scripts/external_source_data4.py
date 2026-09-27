# -*- coding: utf-8 -*-
"""External source notes, part 4: BRYME Writers desk (batch 2 of 2) - the learn
guides and the desk's index/hub pages. Every URL curl-verified 200 at authoring
time."""

OWL = "https://owl.purdue.edu/owl/purdue_owl.html"
PW = "https://www.pw.org/"
PWMAGS = "https://www.pw.org/literary_magazines"
GRINDER = "https://thegrinder.diabolicalplots.com/"
GUARDIAN = "https://www.theguardian.com/guardian-observer-style-guide-a"
GUTENBERG = "https://www.gutenberg.org/"
CHICAGO = "https://www.chicagomanualofstyle.org/home.html"
ASA = "https://www.asauthors.org/"
NUJ = "https://www.nuj.org.uk/"
AUTHGUILD = "https://authorsguild.org/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

EXTERNAL_SOURCES4 = {

# --------------------- learn/academic-writing (6) ---------------------------

"writers/learn/academic-writing/how-to-write-a-lab-report":
    "<p><b>The genre has fixed conventions.</b> Method reproducibility and results separation are requirements, not preferences, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's lab-report guidance</a> sets out the sections and their expectations. The desk's template follows the standard order, because a reader looking for the method needs to find it where the method always is.</p>",

"writers/learn/academic-writing/how-to-write-a-literature-review":
    "<p><b>Synthesis, not a list.</b> A review argues about the state of a field, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's literature-review guidance</a> describes how to organise sources by theme rather than chronology. The <a href=\"" + _w("literature+review") + "\" rel=\"noopener\">literature-review reference material on Wikipedia</a> covers the forms and their purposes across disciplines.</p>",

"writers/learn/academic-writing/how-to-write-a-peer-review":
    "<p><b>Reviewing is a documented practice.</b> What a reviewer is asked to assess — originality, method, validity — is set out in the <a href=\"" + _w("scholarly+peer+review") + "\" rel=\"noopener\">peer-review reference material on Wikipedia</a>, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL</a> covers the feedback conventions the desk's template uses. The page is written for the reviewer who has never done it, which is most of them the first time.</p>",

"writers/learn/academic-writing/how-to-write-a-personal-statement":
    "<p><b>A genre with a specific reader.</b> Admissions readers assess evidence of fit and capability, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's personal-statement guidance</a> describes the structure that serves that reader. The desk's advice is concrete: specific episodes beat adjectives, because the reader has already read fifty claims of passion.</p>",

"writers/learn/academic-writing/how-to-write-an-annotated-bibliography":
    "<p><b>Two jobs per entry.</b> Cite correctly, then evaluate honestly, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's annotated-bibliography guidance</a> sets out both halves with examples in each citation style. The <a href=\"" + _w("annotated+bibliography") + "\" rel=\"noopener\">annotated-bibliography reference material on Wikipedia</a> covers the variants your course may specify.</p>",

"writers/learn/academic-writing/how-to-write-an-exam-essay":
    "<p><b>Exam conditions change the craft.</b> Planning time, structure and the discipline of answering the question set are covered by the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's essay-writing resources</a>, which the desk compresses into a timed method. The difference between a good essay and a good exam essay is the clock, and the page is organised around it.</p>",

# -------------------- learn/common-problems (1) -----------------------------

"writers/learn/common-problems/how-plagiarism-and-ai-checkers-are-made":
    "<p><b>How the detectors actually work.</b> Similarity tools compare text against indexed corpora using established techniques, and the <a href=\"" + _w("plagiarism+detection") + "\" rel=\"noopener\">plagiarism-detection reference material on Wikipedia</a> explains the methods and their failure modes. The <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's plagiarism guidance</a> covers the citation practice that makes the question moot — which is the desk's actual recommendation.</p>",

# -------------------- learn/creative-writing (2) ----------------------------

"writers/learn/creative-writing/how-to-plan-a-novel":
    "<p><b>Structure is a craft with a literature.</b> Narrative structure, scene sequencing and the planning methods writers use are described in the <a href=\"" + _w("plot+(narrative)") + "\" rel=\"noopener\">narrative-plot reference material on Wikipedia</a>. The desk's method is deliberately non-prescriptive: plan enough to know the next scene, not so much that discovery becomes impossible.</p>",

"writers/learn/creative-writing/how-to-write-flash-fiction":
    "<p><b>A form with real constraints.</b> Flash fiction compresses a complete story into very few words, and the <a href=\"" + _w("flash+fiction") + "\" rel=\"noopener\">flash-fiction reference material on Wikipedia</a> covers its conventions and history. The public-domain shelves at <a href=\"" + GUTENBERG + "\" rel=\"noopener\">Project Gutenberg</a> hold short models worth dissecting, which the desk recommends over reading about the form.</p>",

# ------------------ learn/editing-proofreading (2) --------------------------

"writers/learn/editing-proofreading/how-to-build-a-personal-style-guide":
    "<p><b>Build it the way the professionals do.</b> A style guide records decisions so they stay consistent, and two public ones are worth reading in full: the <a href=\"" + GUARDIAN + "\" rel=\"noopener\">Guardian's published style guide</a> and the <a href=\"" + CHICAGO + "\" rel=\"noopener\">Chicago Manual of Style</a>. Your own needs twenty entries, not two hundred — the desk's starter list is on the page.</p>",

"writers/learn/editing-proofreading/how-to-write-in-plain-language":
    "<p><b>Plain language is a measurable standard.</b> Readability, word choice and sentence length have documented effects on comprehension, and the <a href=\"" + _w("plain+language") + "\" rel=\"noopener\">plain-language reference material on Wikipedia</a> covers the principles and their history in public administration. The desk's tests are practical: read it aloud, then read it to someone outside the subject.</p>",

# ----------------------- learn/examples (6) ---------------------------------

"writers/learn/examples/example-blog-post":
    "<p><b>An annotated model, not a template.</b> The example is dissected move by move on the page; for structure in the wild, the <a href=\"" + GUTENBERG + "\" rel=\"noopener\">Project Gutenberg</a> archive offers a century of prose free to study. The desk's point in publishing worked examples is that craft is easier to see than to describe.</p>",

"writers/learn/examples/example-of-a-short-story":
    "<p><b>Read it, then take it apart.</b> The example here is annotated for want, obstacle and turn; for comparison, <a href=\"" + GUTENBERG + "\" rel=\"noopener\">Project Gutenberg</a> holds thousands of public-domain stories whose seams are visible in a way modern prose often hides. The <a href=\"" + _w("short+story") + "\" rel=\"noopener\">short-story reference material on Wikipedia</a> covers the form's conventions.</p>",

"writers/learn/examples/example-of-a-speech":
    "<p><b>Speeches are written to be heard.</b> Rhythm, repetition and the placement of the close are covered by the <a href=\"" + _w("public+speaking") + "\" rel=\"noopener\">public-speaking reference material on Wikipedia</a>, and the desk's annotated example marks where each device does its work. The timing note matters: spoken delivery runs near 140 words a minute.</p>",

"writers/learn/examples/example-of-an-essay":
    "<p><b>A worked argument, annotated.</b> The example is marked for thesis, evidence and turn; the <a href=\"" + _w("essay") + "\" rel=\"noopener\">essay reference material on Wikipedia</a> covers the form's history and variants, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL</a> carries the academic conventions. The desk publishes examples because reading one closely teaches more than reading five guides.</p>",

"writers/learn/examples/example-personal-essay":
    "<p><b>Voice is the subject.</b> The annotated example shows where the piece earns its intimacy and where it resists sentimentality; the <a href=\"" + _w("personal+essay") + "\" rel=\"noopener\">personal-essay reference material on Wikipedia</a> describes the form. The <a href=\"" + GUTENBERG + "\" rel=\"noopener\">Project Gutenberg</a> archive is a good place to read the essay's ancestors — Montaigne onward — free.</p>",

"writers/learn/examples/example-query-letter":
    "<p><b>A model, with its reasoning exposed.</b> The example is annotated line by line, and the form's anatomy is described in the <a href=\"" + _w("query+letter") + "\" rel=\"noopener\">query-letter reference material on Wikipedia</a> plus the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's professional-correspondence pages</a>. The desk's note on the page is the one that matters: match the length the market asks for, not the length the classic form suggests.</p>",

# --------------------- learn/grammar-language (4) ---------------------------

"writers/learn/grammar-language/australian-and-canadian-english-for-writers":
    "<p><b>Two varieties with documented conventions.</b> Spelling, punctuation and idiom differ from both British and American usage, and the reference material for <a href=\"" + _w("Australian+English") + "\" rel=\"noopener\">Australian</a> and <a href=\"" + _w("Canadian+English") + "\" rel=\"noopener\">Canadian English</a> sets out the patterns. The desk's practical advice: pick one variety per piece and let a style sheet enforce it.</p>",

"writers/learn/grammar-language/punctuation-and-date-conventions-by-country":
    "<p><b>Conventions that cause real errors.</b> Date order, decimal separators and quotation style differ by market, and the <a href=\"" + _w("date+format+by+country") + "\" rel=\"noopener\">date-format reference material on Wikipedia</a> documents the national patterns. The <a href=\"" + GUARDIAN + "\" rel=\"noopener\">Guardian's public style guide</a> shows one publication resolving these calls consistently, which is the habit worth copying.</p>",

"writers/learn/grammar-language/words-that-change-meaning-across-english":
    "<p><b>False friends between varieties.</b> Words that mean different things in British and American English are documented in the <a href=\"" + _w("comparison+of+American+and+British+English") + "\" rel=\"noopener\">American-and-British-English comparison on Wikipedia</a>. The desk's list concentrates on the ones that cause embarrassment rather than mere oddity — the words that change an argument rather than a spelling.</p>",

"writers/learn/grammar-language/writing-in-english-as-a-second-language":
    "<p><b>Strengths worth keeping, errors worth fixing.</b> The field has a literature of its own, described in the <a href=\"" + _w("English+as+a+second+or+foreign+language") + "\" rel=\"noopener\">ESL reference material on Wikipedia</a>, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL</a> carries extensive guidance for multilingual writers. The desk's position: your first language is an asset in voice; the fixable surface errors are a separate, solvable problem.</p>",

# ---------------------- learn/online-writing (4) ----------------------------

"writers/learn/online-writing/how-to-write-a-linkedin-post":
    "<p><b>A platform with its own conventions.</b> Format, length and the professional register the audience expects are described in the <a href=\"" + _w("LinkedIn") + "\" rel=\"noopener\">LinkedIn reference material on Wikipedia</a>. The desk's advice is the anti-engagement-bait version: a specific lesson, honestly told, outperforms the manufactured-hook format within a month.</p>",

"writers/learn/online-writing/how-to-write-a-thread":
    "<p><b>Serial writing is a form with rules.</b> The microblogging conventions — one idea per post, a first line that earns the rest — come from the platform's constraints, described in the <a href=\"" + _w("microblogging") + "\" rel=\"noopener\">microblogging reference material on Wikipedia</a>. The desk's method: draft the thread as one piece, then cut along its joints.</p>",

"writers/learn/online-writing/how-to-write-a-video-script":
    "<p><b>Scripts are timed documents.</b> The two-column and narration conventions used in video work are described in the <a href=\"" + _w("video+production") + "\" rel=\"noopener\">video-production reference material on Wikipedia</a>, and the desk's template is built around the constraint that drives everything else: roughly 140 spoken words a minute.</p>",

"writers/learn/online-writing/how-to-write-an-faq-page":
    "<p><b>An FAQ is a service document.</b> Its conventions — real questions, short answers, no marketing — are described in the <a href=\"" + _w("FAQ") + "\" rel=\"noopener\">FAQ reference material on Wikipedia</a>. The desk's test for a good one is blunt: would a reader who did not work for you have asked that question?</p>",

# ------------------- learn/professional-writing (7) -------------------------

"writers/learn/professional-writing/how-to-write-a-formal-appeal":
    "<p><b>Structure decides outcomes.</b> A formal appeal states the decision, the grounds and the remedy sought, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's business-correspondence guidance</a> covers the register. The <a href=\"" + _w("appeal") + "\" rel=\"noopener\">appeal reference material on Wikipedia</a> explains why procedure matters as much as argument in a formal process.</p>",

"writers/learn/professional-writing/how-to-write-a-formal-complaint":
    "<p><b>A complaint that gets action has a shape.</b> Facts, impact, remedy and deadline — and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's professional-writing resources</a> cover the register that keeps it taken seriously. Where consumer rights apply, the desk notes that the relevant authority's published process is worth reading before writing, because it defines what must be said.</p>",

"writers/learn/professional-writing/how-to-write-a-performance-review":
    "<p><b>Evidence, not adjectives.</b> The convention is specific examples tied to stated expectations, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's professional-writing guidance</a> covers the register for evaluative documents. The desk's rule for both directions of a review: every claim names an observable event, which is the difference between feedback and a verdict.</p>",

"writers/learn/professional-writing/how-to-write-a-reference-letter":
    "<p><b>A letter with legal and ethical edges.</b> What a referee can honestly claim, and what to do when they cannot, is covered by the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's reference-letter guidance</a>. The desk's advice includes the part most templates skip: if you cannot write a supportive letter, decline promptly rather than write a cold one.</p>",

"writers/learn/professional-writing/how-to-write-a-standard-operating-procedure":
    "<p><b>SOPs have a documented purpose and format.</b> The <a href=\"" + _w("standard+operating+procedure") + "\" rel=\"noopener\">SOP reference material on Wikipedia</a> describes why organisations use them and the structures that work, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's technical-writing resources</a> cover the task-oriented prose. The desk's test: can someone who was not in the meeting follow it?</p>",

"writers/learn/professional-writing/how-to-write-an-apology":
    "<p><b>The research on apologies is unusually clear.</b> A complete apology names the offence, accepts responsibility, and offers repair — and the <a href=\"" + _w("apology") + "\" rel=\"noopener\">apology reference material on Wikipedia</a> covers the components studied in the field. The desk's list of what to leave out is as long as the list of what to include, which is why most corporate apologies fail.</p>",

"writers/learn/professional-writing/how-to-write-meeting-minutes":
    "<p><b>Minutes are a record, not a transcript.</b> Decisions, actions and owners are the content that matters, and the <a href=\"" + _w("minutes") + "\" rel=\"noopener\">minutes reference material on Wikipedia</a> covers the formal requirements in governance contexts. The <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's professional-writing pages</a> supply the register; the desk's template supplies the columns.</p>",

# -------------------- learn/types-of-writing (5) ----------------------------

"writers/learn/types-of-writing/all-types-of-writing":
    "<p><b>The categories, mapped.</b> Writing types are classified by purpose and audience, and the <a href=\"" + _w("writing") + "\" rel=\"noopener\">writing reference material on Wikipedia</a> covers the major divisions this page organises. The desk's practical note: most paid work sits between categories, so learn the four purposes rather than memorising the twenty labels.</p>",

"writers/learn/types-of-writing/how-to-write-a-condolence-message":
    "<p><b>Short, specific, and about them.</b> The conventions of condolence writing are covered in the <a href=\"" + _w("condolences") + "\" rel=\"noopener\">condolence reference material on Wikipedia</a>, and the desk's guidance follows the bereavement literature's consistent finding: naming the person and offering something concrete beats expressing sympathy in the abstract.</p>",

"writers/learn/types-of-writing/how-to-write-a-eulogy":
    "<p><b>A speech with a hard brief.</b> The form's conventions — one through-line, specific memories, a close that releases the room — are described in the <a href=\"" + _w("eulogy") + "\" rel=\"noopener\">eulogy reference material on Wikipedia</a>. The desk's timing note is practical: three to five minutes, roughly 140 words a minute, which is fewer words than most people write.</p>",

"writers/learn/types-of-writing/how-to-write-a-thank-you-note":
    "<p><b>Specificity is the whole content.</b> A note that names what was given and what it changed takes four sentences, and the <a href=\"" + _w("thank-you+note") + "\" rel=\"noopener\">thank-you-note reference material on Wikipedia</a> covers the conventions and their history. The desk's rule: never mention what you want next in the same note, because it converts gratitude into a transaction.</p>",

"writers/learn/types-of-writing/how-to-write-a-wedding-speech":
    "<p><b>Structure protects the room.</b> The best man's and maid of honour's conventions — who to thank, what to leave out, how to close — are described in the <a href=\"" + _w("wedding+speech") + "\" rel=\"noopener\">wedding-speech reference material on Wikipedia</a>. The desk's timing advice is the part that gets repeated back: five minutes maximum, one story per person named.</p>",

# ----------------- learn/writing-for-publication (6) ------------------------

"writers/learn/writing-for-publication/how-to-pitch-australian-editors":
    "<p><b>The market has a professional body.</b> The <a href=\"" + ASA + "\" rel=\"noopener\">Australian Society of Authors</a> publishes rate guidance and contract advice that shapes what Australian editors expect, and the desk records each publication's submission route from its own guideline. The <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers magazine database</a> widens the search beyond the desk's listings.</p>",

"writers/learn/writing-for-publication/how-to-pitch-canadian-editors":
    "<p><b>Commissioning routes, recorded.</b> Each market on this page is listed with its own submission route and the date the desk last read it; the <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers magazine database</a> and <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a>'s response-time data cover markets beyond the list. The pitching mechanics are the same everywhere — the fit is what differs.</p>",

"writers/learn/writing-for-publication/how-to-pitch-uk-editors":
    "<p><b>A market with strong professional conventions.</b> The <a href=\"" + NUJ + "\" rel=\"noopener\">National Union of Journalists</a> publishes rate and contract guidance that UK commissioning editors work against, and the <a href=\"" + GUARDIAN + "\" rel=\"noopener\">Guardian's public style guide</a> is a useful read for the register these desks expect. Routes here are recorded from each publication's own page, dated.</p>",

"writers/learn/writing-for-publication/how-to-pitch-us-editors":
    "<p><b>The largest market, and the most documented.</b> <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a> lists US markets with submission details, the <a href=\"" + AUTHGUILD + "\" rel=\"noopener\">Authors Guild</a> publishes contract guidance, and <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a> records response times writers have reported. The desk's listings add the verification date, which is the part databases do not carry.</p>",

"writers/learn/writing-for-publication/how-to-write-a-query-letter":
    "<p><b>The form's anatomy, documented.</b> The <a href=\"" + _w("query+letter") + "\" rel=\"noopener\">query-letter reference material on Wikipedia</a> describes the structure and its history, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's professional-correspondence pages</a> supply the register. The desk's version is shorter than the classic form because most markets now read queries as emails, and the page says which to send where.</p>",

"writers/learn/writing-for-publication/why-your-first-pitch-may-be-rejected":
    "<p><b>Rejection is mostly arithmetic.</b> Response-time and acceptance data aggregated from writers' reports sits at <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a>, which turns &ldquo;no reply&rdquo; into a statistic rather than a verdict. The <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers magazine database</a> is where the desk sends writers looking for a better-matched market.</p>",

# --------------------- learn/writing-process (4) ----------------------------

"writers/learn/writing-process/how-to-get-and-use-feedback":
    "<p><b>Feedback has a method.</b> Structured critique — separating observation from preference, and revision from defence — is covered by the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's revision and peer-review resources</a>. The <a href=\"" + _w("peer+review") + "\" rel=\"noopener\">peer-review reference material on Wikipedia</a> describes the formal version of the same discipline.</p>",

"writers/learn/writing-process/how-to-manage-a-long-writing-project":
    "<p><b>Project discipline, applied to prose.</b> Milestones, buffers and the risk of a single unmovable deadline are standard project-management concerns, described in the <a href=\"" + _w("project+management") + "\" rel=\"noopener\">project-management reference material on Wikipedia</a>. The desk's translation for writers: schedule the revision, because the draft is the part that announces its own progress.</p>",

"writers/learn/writing-process/how-to-write-under-deadline-pressure":
    "<p><b>The method is boring and it works.</b> Outline, draft, verify, cut — in that order, with verification never compressed — and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's writing-process resources</a> formalise the stages. The desk's rule for deadline work: the fact-check pass is the one thing that cannot be shortened, which is what the <a href=\"/writers/corrections/\">corrections policy</a> exists to enforce.</p>",

"writers/learn/writing-process/how-to-write-with-ai":
    "<p><b>Know what the tool is, and what markets allow.</b> The technology's behaviour and limits are described in the <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large-language-model reference material on Wikipedia</a>, and several publications now state an AI position in their guidelines, which the desk records verbatim. The craft guidance here assumes you keep the voice; the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL</a> covers the citation side.</p>",

# ------------------------- desk hubs (13) -----------------------------------

"writers/find":
    "<p><b>Choosing a form is choosing a reader.</b> The major writing types are classified by purpose and audience, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's purpose-and-audience material</a> is the free standard on that question. This desk's routes below are built around the same distinction, because the practical question is always what the reader needs from the page.</p>",

"writers/intelligence":
    "<p><b>How the desk's facts are held.</b> Every time-sensitive claim carries a check date, and the market data behind the listings is cross-referenced against public sources: <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a> and <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a>'s writer-reported response times. Where the desk cannot verify something, the label says so rather than leaving it implied.</p>",

"writers/learn":
    "<p><b>The library's spine.</b> The shelves here follow the standard stages of the craft, and the free reference behind most of them is the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL</a> — encyclopaedic, maintained, and the closest thing the field has to a neutral authority. The desk's guides compress what it formalises into sequences you can run in an afternoon.</p>",

"writers/regional":
    "<p><b>Conventions that cross borders badly.</b> Spelling, punctuation, dates and register differ by variety, and the <a href=\"" + _w("comparison+of+American+and+British+English") + "\" rel=\"noopener\">American-and-British-English comparison on Wikipedia</a> documents the main divergences. The <a href=\"" + GUARDIAN + "\" rel=\"noopener\">Guardian's public style guide</a> shows one publication resolving them consistently, which is the practice worth copying.</p>",

"writers/templates":
    "<p><b>Templates encode conventions.</b> The business-letter, proposal and correspondence structures these templates follow are documented by the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's professional-writing resources</a>, and each template on this page states which convention it implements. The <a href=\"" + _w("query+letter") + "\" rel=\"noopener\">query-letter reference material on Wikipedia</a> covers the form most often templated badly.</p>",

"writers/today":
    "<p><b>Fresh listings, dated.</b> Opportunities appearing here are taken from each publication's own guideline with the date the desk read it; the wider market is searchable at <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a>. The desk records pay, eligibility and window rather than promising availability, because those three fields change without announcement.</p>",

"writers/writing-calendar":
    "<p><b>Windows, with their sources.</b> Submission windows are recorded from each publication's guideline with a check date, and the desk cross-references the wider market through <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a>. Where a window is stated as rolling rather than dated, the entry says so — an undated window is a different kind of deadline.</p>",

"writers/writing-opportunities/australia":
    "<p><b>How this page is kept honest.</b> Each listing is re-read from the publication's own guideline at every sweep, with pay, eligibility and last-verified date recorded. The professional context for Australian markets is published by the <a href=\"" + ASA + "\" rel=\"noopener\">Australian Society of Authors</a>, and the <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers database</a> covers markets between sweeps.</p>",

"writers/writing-opportunities/canada":
    "<p><b>Dated listings, not promises.</b> The desk re-reads each publication's guideline at every sweep and records pay, eligibility and the verification date. The wider market is searchable at <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a>, with response-time data at <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a>; the guideline page always outranks this page.</p>",

"writers/writing-opportunities/united-kingdom":
    "<p><b>Sourced from the publications themselves.</b> Every entry is re-read from the publication's own guideline, dated, and the professional context for UK rates and contracts is published by the <a href=\"" + NUJ + "\" rel=\"noopener\">National Union of Journalists</a>. The <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers database</a> widens the search; where a listing says nothing about pay, this page says nothing either.</p>",

"writers/writing-opportunities/usa":
    "<p><b>Verified listings, dated.</b> Pay, eligibility and submission route are re-read from each publication's guideline at every sweep. The <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers magazine database</a> is the desk's recommended complement for markets between sweeps, and <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a> adds writer-reported response times.</p>",

"writers/writing":
    "<p><b>The desk's core record, and how it is kept.</b> Every listing here carries pay, eligibility and the date the desk last read the publication's guideline; nothing is included on a promise. The public reference layer is <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a> and <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a>, both free, and the desk says plainly where its data and theirs differ.</p>",

}
