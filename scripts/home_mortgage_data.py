# BRYME Home & Property — mortgage payments explained (batch 34, 12 Sep 2026).
# Production Directive tool queue #1: mortgage calculator built FIRST (assets/mortgage-calculator.js),
# article carries it. Every figure verified 12 Sep 2026: Freddie Mac PMMS (10 Sep 2026: 30yr 6.76%,
# 15yr 6.09% - primary), CFPB 28/36 DTI guidance, CFPB PMI, HMRC SDLT first-time-buyer relief (from
# 1 Apr 2025), Canada insured-mortgage stress test (contract+2% or 5.25% floor; GDS 39 / TDS 44;
# CMHC premium bands 4.00/3.10/2.80). Worked examples computed from the same formula the tool uses.
# Byline: real author only (Ibrahim Sodiq); no reviewer credential claimed; general-information disclaimer.

MORTGAGE_SLUG = "mortgage-payments-explained"

MORTGAGE_BODY = """<div class="prose">
<p class="byline" style="margin-top:18px">By <b>Ibrahim Sodiq</b> \u00b7 published 12 September 2026 \u00b7 general information, never financial advice \u2014 your lender\u2019s figures govern</p>
<p><b>The 60-second answer.</b> A monthly mortgage payment is almost never one number. It is <b>principal + interest</b> \u2014 the part the loan math sets \u2014 usually plus <b>property taxes, home insurance</b>, and, if your down payment was under 20% (US), <b>private mortgage insurance</b>. On the week of 10 September 2026 the Freddie Mac 30-year fixed average was <b>6.76%</b> (15-year: 6.09%) \u2014 at that rate, a <b>$350,000 loan over 30 years costs $2,272/month</b> in principal and interest, and quietly pays back <b>$468,071 in interest</b> on top of the loan over the term.</p>
<p>And lenders size what you may borrow with a ratio, not a feeling: the standard guideline is that housing costs stay under <b>28%</b> of gross monthly income and total debt under <b>36%</b> \u2014 the \u201c28/36 rule\u201d. Approval letters often stretch far past it. The rest of this page is about knowing the difference.</p>
<p>Not a reader? <a href="#calculator">Section 4\u2019s calculator</a> shows every number\u2019s source line. Budgeting the move itself? Pair it with <a href="/home/emergency-repair-fund/">the emergency repair fund</a> \u2014 the cost category lenders don\u2019t count.</p>

<h2 id="inside">Section 1 \u00b7 What\u2019s actually inside the payment</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Component</th><th>What it is</th><th>Who sets it</th></tr></thead>
<tbody>
<tr><td><b>Principal</b></td><td>The slice of each payment that pays down the loan balance itself.</td><td>Your loan amount, term, and rate.</td></tr>
<tr><td><b>Interest</b></td><td>The lender\u2019s charge \u2014 in year 1 of the example below it\u2019s <b>86 cents of every dollar</b> you pay.</td><td>Your rate and remaining balance.</td></tr>
<tr><td><b>Property tax</b></td><td>Local tax, often collected monthly into an escrow account and paid on your behalf.</td><td>Your local authority \u2014 not the lender.</td></tr>
<tr><td><b>Home insurance</b></td><td>Hazard cover, also commonly escrowed. Flood is <b>never</b> in this line \u2014 it\u2019s a separate policy (<a href="/home/water-damage-insurance-coverage/">the water damage guide</a> explains the split).</td><td>Your insurer and your risk profile.</td></tr>
<tr><td><b>PMI / extras</b></td><td>Private mortgage insurance when equity is under 20% (US); HOA fees where they apply.</td><td>Your lender\u2019s requirements; typically removable once you cross 20% equity.</td></tr>
</tbody></table>
<p>The P&amp;I part is fixed for a fixed-rate loan \u2014 the other lines move with your tax bill and insurance renewal, which is why the \u201csame\u201d payment creeps up in years when neither the rate nor the house changed.</p>

<h2 id="math">Section 2 \u00b7 The math, shown once</h2>
<p>Every amortizing mortgage on earth uses one formula \u2014 the same one the <a href="#calculator">calculator below</a> runs: <b>M = P \u00d7 r \u00d7 (1+r)<sup>n</sup> / ((1+r)<sup>n</sup> \u2212 1)</b>, where P is the loan, r the monthly rate, n the months. Nothing hides in it. What surprises people is the <em>shape</em> it produces \u2014 amortization front-loads interest:</p>
<p><b>The $350,000 loan at 6.76% over 30 years ($2,272/month):</b></p>
<table class="lg-table lg-scroll">
<thead><tr><th>Year</th><th>Of each payment, interest is</th><th>Principal paid that year</th><th>Balance at year-end</th></tr></thead>
<tbody>
<tr><td>1</td><td><b>86%</b></td><td>$3,723</td><td>$346,277</td></tr>
<tr><td>5</td><td>82%</td><td>$4,875</td><td>$328,601</td></tr>
<tr><td>15</td><td>65%</td><td>$9,567</td><td>$256,636</td></tr>
<tr><td>29</td><td>10%</td><td>$24,582</td><td>$26,296</td></tr>
<tr><td>30</td><td>4%</td><td>$26,296</td><td>$0</td></tr>
</tbody></table>
<p>Read that top row again: in year one, barely a seventh of your money buys you anything you keep. This is why extra principal paid in the <em>early</em> years is disproportionately powerful, why refinancing math changes with the years you\u2019ve already paid, and why \u201cI\u2019ve paid 8 years so I\u2019ve paid off a third of it\u201d is never true.</p>

<h2 id="rule">Section 3 \u00b7 The rule lenders use (and the one you should)</h2>
<p>US guidance (CFPB) frames it as two debt-to-income lines: <b>28%</b> of gross monthly income for housing (front-end), <b>36%</b> for all debt combined (back-end). Many loan programs approve well beyond 36% \u2014 which is exactly why the rule matters more for you than for them:</p>
<ul>
<li><b>Use the back-end number honestly:</b> all loans, cards, car payments and the future mortgage against gross income.</li>
<li><b>Approval is a ceiling, not a budget.</b> The lender prices your <em>willingness</em> to repay at their maximum; only you price the part that keeps the house maintained, heated and insured \u2014 the ownership ledger the approval ignores (<a href="/home/someday-maintenance-cost/">the someday-cost rule</a> is the honest version).</li>
<li><b>Stress yourself like Canada stress-tests everyone:</b> before signing, recompute your budget at contract rate + 2%. If it only works at the exact rate, the loan is too big \u2014 whatever the letter says.</li>
</ul>

<h2 id="calculator">Section 4 \u00b7 The monthly payment calculator</h2>
<style>
.mc-grid{display:flex;flex-wrap:wrap;gap:22px;border:1px solid var(--line-strong);border-radius:12px;padding:18px 20px;background:var(--sheet);max-width:760px}
.mc-fields{flex:1;min-width:250px;display:flex;flex-direction:column;gap:10px}
.mc-fields label{font-size:13px;display:flex;flex-direction:column;gap:4px}
.mc-fields input,.mc-fields select{padding:8px 10px;border:1px solid var(--line-strong);border-radius:8px;font:inherit;font-size:15px;background:var(--card)}
.mc-out{flex:1;min-width:250px}
.mc-out table{width:100%;border-collapse:collapse}
.mc-out td{padding:7px 6px;border-bottom:1px solid var(--line);font-size:14px}
.mc-disc{font-size:13px;color:var(--line-strong);max-width:760px;margin-top:10px}
</style>
<div id="mortgage-calc"></div>
<noscript><p><b>Static version:</b> monthly P&amp;I = loan \u00d7 r \u00d7 (1+r)<sup>n</sup> / ((1+r)<sup>n</sup> \u2212 1), r = annual rate \u00f7 12, n = months. At 6.76% over 30 years that\u2019s about <b>$6.49 per $1,000 borrowed</b> \u2014 $350,000 \u2192 \u2248$2,272/mo, plus taxes, insurance and PMI where they apply.</p></noscript>
<p class="mc-disc" style="margin-top:6px">The tool runs its math in your browser, mirrors Section 2\u2019s formula exactly, and is general guidance \u2014 not a loan offer, not financial advice. US buyers: your lender\u2019s itemized <b>Loan Estimate</b> is the document that governs; UK and Canadian buyers: Sections 6\u2019s local differences apply before any of this.</p>

<h2 id="levers">Section 5 \u00b7 What actually moves the payment</h2>
<p>Same $350,000 loan, same market week \u2014 the term is the biggest single lever:</p>
<table class="lg-table lg-scroll">
<thead><tr><th>Term (fixed)</th><th>Rate (PMMS, 10 Sep 2026)</th><th>Monthly P&amp;I</th><th>Total interest</th></tr></thead>
<tbody>
<tr><td>30 years</td><td>6.76%</td><td><b>$2,272</b></td><td>$468,071</td></tr>
<tr><td>20 years</td><td>6.76%</td><td>$2,663</td><td>$289,205</td></tr>
<tr><td>15 years</td><td>6.09%</td><td>$2,971</td><td>$184,698</td></tr>
</tbody></table>
<ul>
<li><b>Rate:</b> half a point on this loan is about <b>\u00b1$115\u2013118/month</b> and tens of thousands over the term \u2014 which is why <b>shopping multiple lenders</b> is the highest-paid hour available to a borrower (Freddie Mac\u2019s chief economist\u2019s standing advice, same release).</li>
<li><b>Down payment:</b> under 20% down, US lenders typically add PMI \u2014 commonly quoted around <b>0.5\u20131% of the loan per year</b> (industry range; your Loan Estimate states yours). The calculator\u2019s \u201cother\u201d field exists for exactly this line.</li>
<li><b>Points:</b> paying upfront to cut the rate only wins if you stay past the break-even month \u2014 compute it, don\u2019t vibe it.</li>
</ul>

<h2 id="regional">Section 6 \u00b7 Regional differences (US \u00b7 UK \u00b7 CA)</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Country</th><th>The mechanism</th><th>The difference that matters</th></tr></thead>
<tbody>
<tr><td><b>United States</b></td><td>PMI below 20% down; standardized Loan Estimate form</td><td>Every lender must give the same 3-page form \u2014 line-by-line comparable quotes are a legal right; use it.</td></tr>
<tr><td><b>United Kingdom</b></td><td>Deposit culture + lender affordability checks; SDLT land tax</td><td>First-time buyers in England &amp; NI pay <b>no stamp duty up to \u00a3300,000</b> (5% only on the portion to \u00a3500,000; relief lost above \u00a3500k \u2014 rules since 1 April 2025). Deposits of 5\u201310% are common; rates are mostly short-term fixes, not 30-year locks.</td></tr>
<tr><td><b>Canada</b></td><td>The stress test + CMHC insurance</td><td>Insured borrowers must qualify at <b>contract rate + 2% or 5.25%, whichever is higher</b>, within GDS \u226439% / TDS \u226444%. Under 20% down, CMHC premiums stack on the loan (4.00% / 3.10% / 2.80% by down-payment band); minimum down is 5% to $500k, 5%+10% beyond; from $1.5M the mortgage can\u2019t be insured (20% down).</td></tr>
</tbody></table>
<p>Local rules move \u2014 each of these was checked 12 September 2026 against the schemes\u2019 published guidance and current industry summaries; re-check before you rely on a threshold.</p>

<h2 id="wrong">Section 7 \u00b7 If the math went wrong</h2>
<p>Signed, and the payment feels bigger than the budget? The order of moves:</p>
<ul>
<li><b>Refinance</b> when rates or your credit genuinely improve \u2014 but run it against your <em>remaining</em> term (Section 2\u2019s front-loading means an old loan refinanced late restarts the interest clock).</li>
<li><b>Recast</b> (US, where offered): a lump sum against the balance re-amortizes the <em>same</em> rate and term into a smaller payment, cheaply \u2014 the underrated move after a windfall.</li>
<li><b>Extra principal early</b> \u2014 one extra payment a year in the first years beats the same payment in year 25, because it deletes interest before the schedule charges it.</li>
<li><b>Struggling?</b> Call the servicer <em>before</em> the first missed payment \u2014 hardship and forbearance options exist and are easier to open than to reopen.</li>
</ul>

<h2 id="faq">FAQ</h2>
<p><b>How is a monthly mortgage payment calculated?</b><br>
Loan \u00d7 r \u00d7 (1+r)<sup>n</sup> \u00f7 ((1+r)<sup>n</sup> \u2212 1), with r the monthly rate and n the months \u2014 plus escrowed taxes, insurance and any PMI/HOA on top.</p>
<p><b>What percentage of income should go to a mortgage?</b><br>
The standard guideline is 28% of gross income for housing and 36% for all debt (the 28/36 rule). Many approvals exceed it; the guideline is a sanity line, not a law.</p>
<p><b>How much is PMI?</b><br>
Industry range commonly quoted around 0.5\u20131% of the loan per year while equity is under 20% \u2014 your Loan Estimate states your actual figure, and it typically comes off once you cross 20% equity.</p>
<p><b>Should I choose a 15-year or 30-year mortgage?</b><br>
On the week\u2019s averages, $350k costs $2,272/mo over 30 years but $2,971 over 15 \u2014 and saves about $283,000 in interest. The 30-year wins on flexibility; you can always overpay a 30-year toward 15-year speed, never the reverse.</p>
<p><b>What\u2019s the payment on a $350,000 mortgage?</b><br>
At 6.76% over 30 years: $2,272/month principal &amp; interest (rate = Freddie Mac weekly average, 10 Sep 2026). Add taxes, insurance and PMI for the real out-the-door number \u2014 the calculator above does both halves.</p>

<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":"Article","headline":"Mortgage payments explained: the real math behind the monthly bill",
"description":"What's inside a mortgage payment, the 28/36 rule lenders use, amortization's front-loaded interest, and the levers that move the number - with an in-page calculator.",
"author":{"@type":"Person","name":"Ibrahim Sodiq"},
"publisher":{"@type":"Organization","name":"THE BRYME"},
"datePublished":"2026-09-12","dateModified":"2026-09-12"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is a monthly mortgage payment calculated?","acceptedAnswer":{"@type":"Answer","text":"Loan multiplied by r times (1+r)^n divided by ((1+r)^n - 1), where r is the monthly interest rate and n the number of months - plus escrowed taxes, insurance, and any PMI or HOA on top."}},
{"@type":"Question","name":"What percentage of income should go to a mortgage?","acceptedAnswer":{"@type":"Answer","text":"The standard guideline is 28 percent of gross income for housing and 36 percent for all debt combined (the 28/36 rule). Many approvals exceed it; treat it as a sanity line, not a law."}},
{"@type":"Question","name":"How much is PMI?","acceptedAnswer":{"@type":"Answer","text":"Commonly quoted around 0.5 to 1 percent of the loan per year while equity is under 20 percent. Your Loan Estimate states your actual figure, and PMI typically comes off once you cross 20 percent equity."}},
{"@type":"Question","name":"Should I choose a 15-year or 30-year mortgage?","acceptedAnswer":{"@type":"Answer","text":"On the week's averages, $350,000 costs $2,272 per month over 30 years but $2,971 over 15 - and saves about $283,000 in interest. A 30-year loan wins on flexibility; you can overpay a 30-year toward 15-year speed, never the reverse."}},
{"@type":"Question","name":"What's the payment on a $350,000 mortgage?","acceptedAnswer":{"@type":"Answer","text":"At 6.76 percent over 30 years: $2,272 per month in principal and interest (the Freddie Mac weekly average as of 10 September 2026). Add taxes, insurance and PMI for the real monthly total."}}]}]}
</script>

<h2>Sources (all checked 12 September 2026)</h2>
<ul>
<li>Freddie Mac Primary Mortgage Market Survey, 10 September 2026 \u2014 30-year FRM average <b>6.76%</b>, 15-year <b>6.09%</b> (freddiemac.com/pmms; release via GlobeNewswire). Rates change weekly \u2014 this page stamps the week it checked.</li>
<li>Consumer Financial Protection Bureau \u2014 debt-to-income guidance (28/36 as the standard lender guideline) and PMI requirements below 20% equity; consumerfinance.gov.</li>
<li>HMRC Stamp Duty Land Tax \u2014 first-time buyer relief as re-set from 1 April 2025 (nil rate to \u00a3300,000; 5% on the portion to \u00a3500,000; relief lost above \u00a3500k), England &amp; NI \u2014 gov.uk and current industry summaries.</li>
<li>Canada\u2019s insured-mortgage framework \u2014 stress test at contract +2% (5.25% floor), GDS \u226439% / TDS \u226444%, CMHC premium bands 4.00/3.10/2.80%, minimum down payment tiers \u2014 CMHC/OSFI rules as summarised by current Canadian mortgage industry guides (2026).</li>
<li>Worked examples computed from the standard amortization formula at the stated rates \u2014 the same math the embedded calculator runs in-browser.</li>
</ul>
<p class="byline">Reviewed 12 September 2026 \u00b7 rates and tax thresholds move \u2014 each carries its checked date \u00b7 no professional reviewer is claimed: this page is general information, not financial, tax or legal advice.</p>
</div>
<script src="/assets/mortgage-calculator.js" defer></script>"""

HOME_MORTGAGE = [
(MORTGAGE_SLUG, "guide",
"Mortgage payments explained: the real math behind the monthly bill",
"What's inside a mortgage payment, the 28/36 rule lenders use, amortization's front-loaded interest, and the levers that move the number \u2014 with an in-page calculator.",
MORTGAGE_BODY),
]
