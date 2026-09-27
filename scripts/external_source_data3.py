# -*- coding: utf-8 -*-
"""External source notes, part 3: BRYME Writers desk (batch 1 of 2).
Every URL curl-verified 200 at authoring time; where an authority blocked the
check (canada.ca, firs.gov.ng) the note uses a verified alternative instead."""

OWL = "https://owl.purdue.edu/owl/purdue_owl.html"
PW = "https://www.pw.org/"
PWMAGS = "https://www.pw.org/literary_magazines"
GRINDER = "https://thegrinder.diabolicalplots.com/"
GUARDIAN = "https://www.theguardian.com/guardian-observer-style-guide-a"
GUTENBERG = "https://www.gutenberg.org/"
JALADA = "https://jaladaafrica.org/"
CHICAGO = "https://www.chicagomanualofstyle.org/home.html"
FTC = "https://www.ftc.gov/"
IRS = "https://www.irs.gov/"
ASA = "https://www.asauthors.org/"
GRA = "https://gra.gov.gh/"
INCOMETAX = "https://www.incometax.gov.in/"
KRA = "https://www.kra.go.ke/"
SAFREA = "https://safrea.co.za/"
SARS = "https://www.sars.gov.za/"
HMRC = "https://www.gov.uk/government/organisations/hm-revenue-customs"
NUJ = "https://www.nuj.org.uk/"
AUTHGUILD = "https://authorsguild.org/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

EXTERNAL_SOURCES3 = {

# ---------------- learn/freelance-paid-writing (40) -------------------------

"writers/learn/freelance-paid-writing":
    "<p><b>The reference layer behind this shelf.</b> Market and rate questions are checked against the trade's public record: <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> for market data and surveys, and <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a> for response times reported by writers themselves. Where the desk states a rate, it states the source and the date it was read.</p>",

"writers/learn/freelance-paid-writing/accounting-software-for-writers":
    "<p><b>What the software is actually doing.</b> Double-entry bookkeeping, multi-currency handling and tax categorisation are standardised functions, and the <a href=\"" + _w("accounting+software") + "\" rel=\"noopener\">accounting-software reference material on Wikipedia</a> explains what each category of tool is built for. The desk's comparison is about workflow fit, not features nobody uses.</p>",

"writers/learn/freelance-paid-writing/african-writers-international-markets":
    "<p><b>Markets and eligibility, from the source.</b> Which publications accept African and diaspora writers is recorded from each publication's own guideline, and the desk's reference layer is <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a> plus continental platforms such as <a href=\"" + JALADA + "\" rel=\"noopener\">Jalada Africa</a>. Payment and tax mechanics are the reader's to confirm with their own authority.</p>",

"writers/learn/freelance-paid-writing/b2b-content-writing":
    "<p><b>The discipline has a literature.</b> Business-to-business content is a defined practice with its own conventions, and the <a href=\"" + _w("content+marketing") + "\" rel=\"noopener\">content-marketing reference material on Wikipedia</a> covers the formats and measurement approaches behind the briefs. The desk's advice on specialising follows the market logic: depth in one vertical beats range across ten.</p>",

"writers/learn/freelance-paid-writing/canada-tax-for-freelance-writers":
    "<p><b>Filing dates come from the revenue authority.</b> Canadian self-employment filing and payment deadlines are published by the Canada Revenue Agency — summarised in the <a href=\"" + _w("Canada+Revenue+Agency") + "\" rel=\"noopener\">encyclopaedic record</a> where the desk needs a citable reference — and the desk prints them with their check date rather than paraphrasing them from memory. This page is general information, not tax advice for your situation.</p>",

"writers/learn/freelance-paid-writing/choosing-a-grammar-checker":
    "<p><b>What these tools can and cannot detect.</b> Rule-based and statistical checkers fail differently, and the <a href=\"" + _w("grammar+checker") + "\" rel=\"noopener\">grammar-checker reference material on Wikipedia</a> explains the two approaches and their limits. The desk's position follows from that: a checker catches surface errors, not meaning, and no tool should be the last reader.</p>",

"writers/learn/freelance-paid-writing/choosing-ai-writing-tools":
    "<p><b>The technology, described honestly.</b> What these systems generate and how they are trained is documented in the <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large-language-model reference material on Wikipedia</a>, which is the desk's baseline for claims about output and attribution. Market policy is the practical half: several publications now state an AI position in their guidelines, and the desk records it verbatim.</p>",

"writers/learn/freelance-paid-writing/choosing-long-form-writing-software":
    "<p><b>Choose by file format, not by interface.</b> The long-term question is whether your manuscript is readable in ten years, and the <a href=\"" + _w("word+processor") + "\" rel=\"noopener\">word-processor reference material on Wikipedia</a> covers the format families and their longevity. The desk's rule is plain: an open or well-documented format beats a proprietary one with nicer typography.</p>",

"writers/learn/freelance-paid-writing/choosing-note-taking-apps":
    "<p><b>Ownership is the deciding question.</b> Whether your notes are exportable and locally readable is a property of the format, and the <a href=\"" + _w("note-taking") + "\" rel=\"noopener\">note-taking reference material on Wikipedia</a> covers the approaches and their trade-offs. The desk's test is the exit test: if the app disappeared tomorrow, could you read your own notes?</p>",

"writers/learn/freelance-paid-writing/choosing-pdf-and-document-tools":
    "<p><b>PDF is a published standard, which is why it survives.</b> The format is specified openly (ISO 32000), and the <a href=\"" + _w("PDF") + "\" rel=\"noopener\">PDF reference material on Wikipedia</a> explains the variants that matter to a writer submitting work — flattened text, embedded fonts, tagged structure for accessibility. Most tool choice is downstream of getting those right.</p>",

"writers/learn/freelance-paid-writing/choosing-research-tools":
    "<p><b>Citation management is a solved problem.</b> Reference managers store sources and emit citations in any required style, and the <a href=\"" + _w("reference+management+software") + "\" rel=\"noopener\">reference-management reference material on Wikipedia</a> compares the categories. The desk's emphasis is on the capture habit rather than the software, because a tool cannot find a source you did not save.</p>",

"writers/learn/freelance-paid-writing/do-writers-need-business-insurance":
    "<p><b>The exposure has a name.</b> Professional indemnity and media liability cover the mistakes a writer can actually make, and the <a href=\"" + _w("professional+liability+insurance") + "\" rel=\"noopener\">professional-liability reference material on Wikipedia</a> explains what such policies respond to. The desk's answer is conditional and says so: it depends on your contracts, your clients and your jurisdiction.</p>",

"writers/learn/freelance-paid-writing/emerging-writing-platforms-polymemo":
    "<p><b>Judging a platform means reading its economics.</b> The categories of self-publishing and reader-funded writing have documented histories, and the <a href=\"" + _w("self-publishing") + "\" rel=\"noopener\">self-publishing reference material on Wikipedia</a> covers them. The desk's method for any new platform is the same: read the fee schedule, the payout terms and the exit path before writing a word for it.</p>",

"writers/learn/freelance-paid-writing/finance-and-insurance-copywriting":
    "<p><b>Regulated subjects pay for precision.</b> Financial and insurance copy is written under disclosure rules, and the <a href=\"" + _w("copywriting") + "\" rel=\"noopener\">copywriting reference material on Wikipedia</a> covers the commercial forms. The desk's rate observation follows from the compliance burden: the premium is for accuracy and audit trail, not for creativity.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-australia":
    "<p><b>The rate card is published by the profession.</b> The <a href=\"" + ASA + "\" rel=\"noopener\">Australian Society of Authors</a> publishes recommended rates that this page quotes with its check date, which is why the desk can discuss a market floor rather than guess at one. Individual contracts vary, and the ASA's figures are recommendations rather than rules.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-canada":
    "<p><b>Rates and the tax side, kept separate.</b> Market rates here are drawn from published surveys and the desk's own recorded listings, with the self-employment tax framework summarised in the <a href=\"" + _w("Canada+Revenue+Agency") + "\" rel=\"noopener\">encyclopaedic record</a> for reference. The desk states which figure came from where, and dates it — rates move faster than any page can.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-ghana":
    "<p><b>A thin market, described honestly.</b> Where published rate data is scarce, the desk says so rather than inventing a benchmark; the tax side of self-employment is overseen by the <a href=\"" + GRA + "\" rel=\"noopener\">Ghana Revenue Authority</a>, whose published guidance is the correct reference for filing obligations. Figures here are labelled as observed ranges, not official rates.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-india":
    "<p><b>Wide range, documented causes.</b> The spread between content-mill and specialist rates is a market structure, and the desk records both ends with sources. The tax framework for self-employed writers is administered by the <a href=\"" + INCOMETAX + "\" rel=\"noopener\">Income Tax Department</a>, whose published rules are the reference for the filing points on this page.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-kenya":
    "<p><b>Rates and obligations, sourced.</b> Market figures here come from the desk's recorded listings and published surveys, each with a check date; the tax side sits with the <a href=\"" + KRA + "\" rel=\"noopener\">Kenya Revenue Authority</a>, whose guidance governs how freelance income is declared. This page is general information, not tax advice.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-nigeria":
    "<p><b>Two currencies, one ledger.</b> The desk records Nigerian rates in the currency they were quoted and dates each figure, because a naira rate and a dollar rate are not comparable without the conversion of the day. Tax obligations for self-employed writers are administered by the federal revenue service, described in the <a href=\"" + _w("Federal+Inland+Revenue+Service") + "\" rel=\"noopener\">encyclopaedic record</a> where the desk needs a citable reference.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-south-africa":
    "<p><b>The profession publishes its own rates.</b> <a href=\"" + SAFREA + "\" rel=\"noopener\">SAFREA</a>, the South African freelance editorial association, publishes rate guidance that this page quotes with its check date; the tax framework sits with the <a href=\"" + SARS + "\" rel=\"noopener\">South African Revenue Service</a>. The desk prints both because a rate without its obligations is half a number.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-uk":
    "<p><b>Day rates and the tax position.</b> The <a href=\"" + NUJ + "\" rel=\"noopener\">National Union of Journalists</a> publishes rate guidance for freelance journalists, which is the desk's anchor for the UK figures; the self-employment tax framework is administered by <a href=\"" + HMRC + "\" rel=\"noopener\">HM Revenue &amp; Customs</a>. Both are cited with check dates, and neither is tax advice.</p>",

"writers/learn/freelance-paid-writing/freelance-writing-rates-us":
    "<p><b>Survey data, named and dated.</b> US rate figures on this page come from published industry surveys and the desk's own recorded listings, each labelled with its source and check date. The self-employment tax side is administered by the <a href=\"" + IRS + "\" rel=\"noopener\">Internal Revenue Service</a>, and the <a href=\"" + AUTHGUILD + "\" rel=\"noopener\">Authors Guild</a> publishes contract and rate guidance for writers.</p>",

"writers/learn/freelance-paid-writing/high-paying-writing-niches":
    "<p><b>Survey figures, with their limits stated.</b> The rate data here comes from published industry surveys — the kind aggregated by <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> — and the desk states each figure's source and date. The honest caveat the page keeps repeating: survey averages describe markets, not what any individual writer will be offered.</p>",

"writers/learn/freelance-paid-writing/how-to-become-a-medical-writer":
    "<p><b>A field with defined standards.</b> Medical writing has formal conventions for accuracy and citation, and the <a href=\"" + _w("medical+writing") + "\" rel=\"noopener\">medical-writing reference material on Wikipedia</a> describes the roles and their requirements. The desk's entry route is portfolio-first: regulated writing is learned on supervised work, not from a certificate.</p>",

"writers/learn/freelance-paid-writing/how-to-become-a-technical-writer":
    "<p><b>The craft is documented, and the portfolio decides.</b> Technical communication has established conventions — task orientation, audience analysis, structured authoring — described in the <a href=\"" + _w("technical+writing") + "\" rel=\"noopener\">technical-writing reference material on Wikipedia</a>. The desk's argument is the practical one: employers hire on samples, so write documentation for something real.</p>",

"writers/learn/freelance-paid-writing/how-to-invoice-as-a-writer":
    "<p><b>An invoice is a legal document.</b> Its required contents and payment terms are governed by contract and consumer law, and the <a href=\"" + _w("invoice") + "\" rel=\"noopener\">invoice reference material on Wikipedia</a> covers the components and conventions. The desk's template follows the professional standard: dated, numbered, specific about the work, with payment terms stated rather than assumed.</p>",

"writers/learn/freelance-paid-writing/how-to-raise-your-freelance-rates":
    "<p><b>Raise against the market, not against your nerves.</b> The desk anchors rate conversations in published guidance — the <a href=\"" + AUTHGUILD + "\" rel=\"noopener\">Authors Guild</a> and <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> both publish rate and contract material — plus the writer's own realised hourly. A rise justified by evidence survives; one justified by need usually does not.</p>",

"writers/learn/freelance-paid-writing/invoicing-software-for-writers":
    "<p><b>The software is bookkeeping with a sender.</b> What matters is that the records satisfy whichever tax authority reads them, and the <a href=\"" + _w("invoice") + "\" rel=\"noopener\">invoice reference material on Wikipedia</a> covers the required components. The desk's comparison concentrates on the parts that cost a writer time: multi-currency handling, reminders, and export to an accountant's format.</p>",

"writers/learn/freelance-paid-writing/legal-writing-for-freelancers":
    "<p><b>A niche with its own conventions.</b> Legal writing prizes precision over elegance, and the <a href=\"" + _w("legal+writing") + "\" rel=\"noopener\">legal-writing reference material on Wikipedia</a> describes the forms and their expectations. The desk's boundary is stated plainly: writing about the law for a client is not practising it, and the page says which tasks cross that line.</p>",

"writers/learn/freelance-paid-writing/medical-writing-rates":
    "<p><b>Why this niche pays what it pays.</b> Regulatory and publication writing carries verification responsibility, and the <a href=\"" + _w("medical+writing") + "\" rel=\"noopener\">medical-writing reference material on Wikipedia</a> describes the roles that carry it. Rate figures here are labelled with their source and date, because the spread between agency and direct work is wide.</p>",

"writers/learn/freelance-paid-writing/payment-platforms-for-writers":
    "<p><b>Cross-border payment is a fee structure, not a service.</b> The mechanics — settlement time, intermediary banks, conversion margin — are described in the <a href=\"" + _w("payment+processor") + "\" rel=\"noopener\">payment-processor reference material on Wikipedia</a>. The desk's advice is arithmetic: compare the total cost of receiving a real payment, not the advertised fee.</p>",

"writers/learn/freelance-paid-writing/per-word-day-rate-or-project-fee":
    "<p><b>Three pricing models, three different risks.</b> The trade's published guidance — <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a> among the sources — discusses rate structures, and the desk's comparison follows the risk allocation: per-word protects the writer from scope, project fees protect the client from slowness. The page states which model suits which kind of work.</p>",

"writers/learn/freelance-paid-writing/project-and-client-tools-for-writers":
    "<p><b>Tools serve a workflow that already exists.</b> The categories of project and client management software are described in the <a href=\"" + _w("project+management+software") + "\" rel=\"noopener\">project-management-software reference material on Wikipedia</a>, and the desk's shortlist is deliberately small. A writer's needs are a pipeline, a calendar and a record — not an enterprise suite.</p>",

"writers/learn/freelance-paid-writing/reader-supported-writing":
    "<p><b>Reader funding has a documented history.</b> Subscription and patronage models are described in the <a href=\"" + _w("crowdfunding") + "\" rel=\"noopener\">crowdfunding reference material on Wikipedia</a>, including their failure modes. The desk's comparisons quote each platform's published fee and payout terms with a check date, because those are the numbers that decide what the work is worth to you.</p>",

"writers/learn/freelance-paid-writing/real-estate-writing":
    "<p><b>A niche priced by market, not by skill alone.</b> Listing copy and market commentary sit at opposite ends of the range, and the <a href=\"" + _w("real+estate") + "\" rel=\"noopener\">real-estate reference material on Wikipedia</a> covers the transaction context that explains the spread. The desk records both ends of the range with sources rather than quoting an average that describes nobody.</p>",

"writers/learn/freelance-paid-writing/should-writers-form-an-llc":
    "<p><b>A structure question with a published answer.</b> What limited-liability formation does and does not protect is described in the <a href=\"" + _w("limited+liability+company") + "\" rel=\"noopener\">LLC reference material on Wikipedia</a>, and the <a href=\"" + IRS + "\" rel=\"noopener\">Internal Revenue Service</a> publishes how such entities are treated for US federal tax. The desk's answer is conditional: it depends on your contracts, your income and your jurisdiction.</p>",

"writers/learn/freelance-paid-writing/technical-writing-rates":
    "<p><b>Documented roles, documented ranges.</b> Technical communication roles differ enough to pay differently, and the <a href=\"" + _w("technical+writing") + "\" rel=\"noopener\">technical-writing reference material on Wikipedia</a> describes them. Every rate on this page carries its source and check date; where the desk could not verify a figure, it says the range is unverified rather than printing a number.</p>",

"writers/learn/freelance-paid-writing/ux-writing-for-writers":
    "<p><b>A discipline with its own conventions.</b> Interface copy is written to be scanned, tested and localised, and the <a href=\"" + _w("user+experience+design") + "\" rel=\"noopener\">user-experience-design reference material on Wikipedia</a> describes the practice it sits inside. The desk's transition advice is portfolio-shaped: rewrite a real product's flows and show the reasoning.</p>",

"writers/learn/freelance-paid-writing/writing-contracts-what-to-check":
    "<p><b>Clause language has published meanings.</b> Rights terms — first rights, exclusive, work for hire — are described in the <a href=\"" + _w("publishing+contract") + "\" rel=\"noopener\">publishing-contract reference material on Wikipedia</a>, and the <a href=\"" + AUTHGUILD + "\" rel=\"noopener\">Authors Guild</a> publishes model contract guidance for writers. The desk's standing boundary applies: this page explains terms, it does not give legal advice.</p>",

# ---------------------------- compare (12) ----------------------------------

"writers/compare/chatgpt-alternatives-for-writers":
    "<p><b>What the category actually contains.</b> These systems differ in training, context handling and output control, and the <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large-language-model reference material on Wikipedia</a> explains the differences that matter. The desk's comparison concentrates on the practical questions: what each tool costs, what it keeps, and which markets will accept the output.</p>",

"writers/compare/cover-letter-vs-personal-statement":
    "<p><b>Three documents with different readers.</b> The conventions behind each are covered by the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's professional-writing resources</a>, which carry worked examples of application and admission letters. The desk's comparison turns on one question: who reads it, and what decision are they making?</p>",

"writers/compare/cv-vs-resume":
    "<p><b>A regional difference, documented.</b> Length, content and expectation differ by country, and the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's résumé and CV guidance</a> sets out the US conventions while the desk's comparison covers the UK and continental expectations. The <a href=\"" + _w("curriculum+vitae") + "\" rel=\"noopener\">curriculum-vitae reference material on Wikipedia</a> explains how the two documents diverged.</p>",

"writers/compare/essay-vs-article-vs-blog-post":
    "<p><b>Forms defined by their contract with the reader.</b> The essay's history and conventions are described in the <a href=\"" + _w("essay") + "\" rel=\"noopener\">essay reference material on Wikipedia</a>, which is the desk's starting point for distinguishing an argument-driven form from an information-driven one. The comparison table on this page follows from those definitions rather than from publishing fashion.</p>",

"writers/compare/google-docs-alternatives":
    "<p><b>Choose on format and ownership.</b> The word-processor categories and their file formats are described in the <a href=\"" + _w("word+processor") + "\" rel=\"noopener\">word-processor reference material on Wikipedia</a>, which is the desk's basis for the longevity question: can someone open this manuscript in ten years without your account?</p>",

"writers/compare/grammarly-alternatives":
    "<p><b>Different engines, different blind spots.</b> Rule-based and statistical checkers fail in different places, and the <a href=\"" + _w("grammar+checker") + "\" rel=\"noopener\">grammar-checker reference material on Wikipedia</a> explains the two approaches. The desk's comparison reports what each tool misses as well as what it catches, because that is the part that costs a writer a publication.</p>",

"writers/compare/hemingway-editor-alternatives":
    "<p><b>Readability tools measure proxies.</b> Formula-based scores estimate difficulty from sentence and syllable counts, and the <a href=\"" + _w("readability") + "\" rel=\"noopener\">readability reference material on Wikipedia</a> explains how those formulas work and where they mislead. The desk's comparison says plainly what a score can and cannot tell you about a sentence.</p>",

"writers/compare/memoir-vs-autobiography-vs-biography":
    "<p><b>Three forms, three different contracts.</b> The distinctions are documented in the <a href=\"" + _w("memoir") + "\" rel=\"noopener\">memoir reference material on Wikipedia</a>, which sets out scope, voice and the author's standing. The desk's comparison adds the practical layer: what a publisher expects from each, and what the reader is promised.</p>",

"writers/compare/press-release-vs-news-article":
    "<p><b>One announces, one reports.</b> The press release's structure and purpose are described in the <a href=\"" + _w("press+release") + "\" rel=\"noopener\">press-release reference material on Wikipedia</a>, and the difference from reported journalism is the reason the desk keeps them on separate shelves. The comparison is about who the writing serves.</p>",

"writers/compare/proposal-vs-pitch":
    "<p><b>Length is not the only difference.</b> A proposal argues feasibility; a pitch argues interest. The <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's proposal-writing resources</a> cover the formal proposal's components, which the desk sets beside the two-hundred-word pitch the market actually reads. Both appear here because writers are asked for both, often in the same week.</p>",

"writers/compare/report-vs-essay":
    "<p><b>Structure versus argument.</b> The report's conventions — findings first, evidence after, recommendations explicit — are covered by the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's academic and professional writing resources</a>. The desk's comparison turns on the reader's job: a report is read for decisions, an essay for understanding.</p>",

"writers/compare/summary-vs-abstract-vs-executive-summary":
    "<p><b>Three compressions, three audiences.</b> The academic abstract's conventions are set out in the <a href=\"" + OWL + "\" rel=\"noopener\">Purdue OWL's abstract-writing guidance</a>, and the desk's comparison adds the business variant and the plain summary beside it. The distinguishing test is what the reader does next, which is why the page includes a length column.</p>",

# ----------------------------- essays (7) -----------------------------------

"writers/essays/most-magazines-wont-tell-you-what-they-pay":
    "<p><b>The argument, with its evidence named.</b> Pay-transparency data is aggregated publicly by <a href=\"" + PWMAGS + "\" rel=\"noopener\">Poets &amp; Writers' magazine database</a> and by <a href=\"" + GRINDER + "\" rel=\"noopener\">The Submission Grinder</a>, both of which the desk cites where figures appear. Everything else here is the desk's position, stated as a position — and open to challenge through the <a href=\"/writers/contact/\">contact door</a>.</p>",

"writers/essays/onchain-publishing-for-writers-is-over":
    "<p><b>An argument about a technology, sourced.</b> The underlying mechanics are described in the <a href=\"" + _w("blockchain") + "\" rel=\"noopener\">blockchain reference material on Wikipedia</a>, which is the desk's baseline for what such platforms can technically do. The claim that the publishing use case has faded is the desk's reading of the evidence, dated and labelled as opinion.</p>",

"writers/essays/polymemo-review-the-49-percent":
    "<p><b>A review with its arithmetic shown.</b> The platform's published fee schedule is quoted with the date it was read, and the categories of self-publishing it competes in are described in the <a href=\"" + _w("self-publishing") + "\" rel=\"noopener\">self-publishing reference material on Wikipedia</a>. The 49 percent is the desk's own calculation from the platform's terms, and the working is printed on the page.</p>",

"writers/essays/ream-stories-review":
    "<p><b>Fees quoted, not paraphrased.</b> The platform's published terms are cited with their check date, and the wider category is described in the <a href=\"" + _w("self-publishing") + "\" rel=\"noopener\">self-publishing reference material on Wikipedia</a>. Where the desk judges the platform, it says so — the review separates the published terms from the desk's opinion of them.</p>",

"writers/essays/stacker-news-review":
    "<p><b>Bitcoin payments, described accurately.</b> The mechanics of bitcoin tipping and the lightning network are documented in the <a href=\"" + _w("Lightning+Network") + "\" rel=\"noopener\">encyclopaedic record</a>, which is the desk's baseline for the claims here. The review's verdict is opinion, dated, and the earnings figures on the page are the desk's own recorded numbers.</p>",

"writers/essays/the-ai-ban-is-spreading":
    "<p><b>Policy claims, quoted from the policies.</b> Where this essay says a publication restricts AI-generated work, it quotes the guideline and dates the reading. The technology being legislated about is described in the <a href=\"" + _w("generative+artificial+intelligence") + "\" rel=\"noopener\">generative-AI reference material on Wikipedia</a>; the argument about where the trend is going is the desk's, and it is labelled as such.</p>",

"writers/essays/what-writing-platforms-actually-pay":
    "<p><b>Numbers with their sources attached.</b> Platform fees and payout terms are quoted from each platform's published schedule with a check date, and the categories are described in the <a href=\"" + _w("self-publishing") + "\" rel=\"noopener\">self-publishing reference material on Wikipedia</a>. Market context comes from <a href=\"" + PW + "\" rel=\"noopener\">Poets &amp; Writers</a>; the ranking is the desk's judgement, clearly marked.</p>",

}
