# -*- coding: utf-8 -*-
"""Editorial depth sections, part 5: money-desk pages in the 9.0-9.4 band.
Each is within 5-146 words of the 700-word full-content bar, so these blocks
are short by design. Every external URL curl-verified 200 at authoring time."""

INV = "https://www.investor.gov/"
CFPB = "https://www.consumerfinance.gov/"
FTC = "https://www.ftc.gov/"
FDIC = "https://www.fdic.gov/"
FRB = "https://www.federalreserve.gov/"
GOVUK = "https://www.gov.uk/"
NCUA = "https://www.mycreditunion.gov/"
IRS = "https://www.irs.gov/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS5 = {

"money/forex-spreads-and-pips":
    "<h2>The cost you pay before the trade moves</h2>"
    "<p>A spread is a cost taken at entry, which means every position starts negative by a known amount and has to move that far before it is level. That single fact changes how short-term strategies behave: a method tested without spreads can look profitable and lose money in execution. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on forex trading costs and risks that this desk's framing follows. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What actually moves the spread</h2>"
    "<ul>"
    "<li><b>Liquidity.</b> Major pairs quoted by many dealers stay tight; exotics widen because fewer parties will take the other side.</li>"
    "<li><b>Time of day.</b> Spreads widen outside the overlapping sessions, and widen sharply around major data releases.</li>"
    "<li><b>Volatility.</b> A dealer widens when it cannot price the next tick confidently, which is exactly when a breakout trade wants to enter.</li>"
    "<li><b>Account type.</b> Commission-plus-tight-spread and spread-only accounts can cost the same at different trade sizes, so compare at your own size.</li>"
    "</ul>"
    "<p>Related: <a href=\"/money/trading-fees-explained/\">trading fees explained</a>, <a href=\"/money/order-types-and-slippage/\">order types and slippage</a> and <a href=\"/money/zero-commission-trading-truth/\">the truth about zero-commission trading</a>.</p>",

"money/how-credit-scores-work":
    "<h2>One behaviour, several different scores</h2>"
    "<p>The part that surprises people is that there is no single credit score. Different bureaux compute differently and different lenders request different products, so two lenders can see meaningfully different numbers from the same history. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes the guidance on credit reporting and scoring this page follows. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What moves the number, and what does not</h2>"
    "<ul>"
    "<li><b>Payment history dominates.</b> A single late payment does more damage than several small balances.</li>"
    "<li><b>Utilisation matters at the snapshot.</b> What is reported on the statement date is what counts, not the balance you carry to the due date.</li>"
    "<li><b>Age of accounts is slow.</b> It improves on its own and degrades when old accounts are closed.</li>"
    "<li><b>Checking your own score does not hurt it.</b> Only lender-initiated hard inquiries affect the number.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-to-improve-your-credit-score/\">how to improve your credit score</a>, <a href=\"/money/how-credit-card-interest-works/\">how credit card interest works</a> and <a href=\"/money/money-scams-how-to-spot-and-recover/\">money scams</a> for the credit-repair fraud that targets this subject.</p>",

"money/what-is-escrow-explained":
    "<h2>Escrow is a trust mechanism, not a fee</h2>"
    "<p>An escrow puts money or documents with a party that has no interest in the outcome, so neither side has to trust the other to perform first. The same structure appears in property, in online transactions and in some lending arrangements, and the details differ considerably between them. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes the guidance on escrow accounts in mortgage lending. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The three forms worth distinguishing</h2>"
    "<ul>"
    "<li><b>Transaction escrow</b> holds funds until both sides confirm performance &mdash; common in high-value private sales.</li>"
    "<li><b>Mortgage escrow</b> collects tax and insurance into the monthly payment and pays them when due.</li>"
    "<li><b>Solicitor-held funds</b> in a property purchase, released on completion rather than on agreement.</li>"
    "</ul>"
    "<p>Escrow fraud is common enough to check for: a genuine escrow agent is verifiable independently, and instructions that arrive by email mid-transaction are the classic signal. See <a href=\"/money/mortgage-fees-and-closing-costs-explained/\">mortgage fees and closing costs</a>, <a href=\"/money/how-mortgages-work-explained/\">how mortgages work</a> and <a href=\"/money/money-scams-how-to-spot-and-recover/\">money scams</a>.</p>",

"money/student-loans-explained":
    "<h2>Student loans behave unlike other debt</h2>"
    "<p>Repayment is usually income-contingent rather than fixed, which makes the loan closer to a graduate tax in practice than to a conventional borrowing. That difference changes the arithmetic entirely: paying it off early is not automatically a saving, and for many borrowers the balance is never fully repaid. <a href=\"" + GOVUK + "\" rel=\"noopener\">GOV.UK</a> publishes the official terms for the UK system, and <a href=\"" + CFPB + "\" rel=\"noopener\">the CFPB</a> covers the US equivalent. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The questions that decide your approach</h2>"
    "<ul>"
    "<li><b>What is the repayment threshold?</b> Below it, nothing is deducted and the balance simply accrues.</li>"
    "<li><b>What is the write-off period?</b> If the balance is cancelled after a set number of years, overpaying can be a pure loss.</li>"
    "<li><b>How does interest compare with your likely earnings growth?</b> This determines whether early repayment helps at all.</li>"
    "<li><b>Does it affect other borrowing?</b> Lenders treat the monthly deduction as a committed outgoing when assessing a mortgage.</li>"
    "</ul>"
    "<p>See <a href=\"/money/good-debt-vs-bad-debt-explained/\">good debt versus bad debt</a>, <a href=\"/money/debt-snowball-vs-avalanche/\">snowball versus avalanche</a> and <a href=\"/money/how-mortgage-approval-works-explained/\">how mortgage approval works</a>.</p>",

"money/how-deposit-insurance-works-explained":
    "<h2>What the guarantee actually covers</h2>"
    "<p>Deposit insurance protects cash in a failed institution up to a stated limit per depositor per institution. It does not protect against the institution's performance, and it does not cover investments held through that institution &mdash; a distinction that matters when a bank also sells funds. <a href=\"" + FDIC + "\" rel=\"noopener\">The FDIC</a> publishes the US scheme's rules, and <a href=\"" + NCUA + "\" rel=\"noopener\">mycreditunion.gov</a> covers credit unions. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The limits people get wrong</h2>"
    "<ul>"
    "<li><b>The limit is per institution, not per person.</b> Spreading cash across banks multiplies the cover; spreading it across accounts at one bank does not.</li>"
    "<li><b>Ownership categories can be separate.</b> Joint and individual accounts may be insured separately, which changes the total.</li>"
    "<li><b>Interest counts toward the limit.</b> An account sitting just below the cap can exceed it when interest posts.</li>"
    "<li><b>Brands are not always banks.</b> Some deposit-taking brands are subsidiaries, and the cover follows the licensed entity behind them.</li>"
    "</ul>"
    "<p>See <a href=\"/money/checking-and-savings-accounts-explained/\">checking and savings accounts</a>, <a href=\"/money/high-yield-savings-accounts-explained/\">high-yield savings accounts</a> and <a href=\"/money/joint-bank-accounts-explained/\">joint bank accounts</a>.</p>",

"money/renters-insurance-explained":
    "<h2>It covers your possessions, not the building</h2>"
    "<p>Renters insurance exists because a landlord's policy covers the structure and nothing belonging to the tenant. The most under-appreciated element is usually liability rather than contents: if a visitor is injured in the property, or the tenant causes damage to a neighbour's, the claim lands on the tenant. <a href=\"" + FTC + "\" rel=\"noopener\">The Federal Trade Commission</a> publishes consumer guidance on insurance purchasing. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What to check before buying</h2>"
    "<ul>"
    "<li><b>Replacement versus indemnity value.</b> Replacement cover pays what a new equivalent costs; indemnity pays the depreciated value, which can be far less.</li>"
    "<li><b>Single-item limits.</b> A total contents figure means little if an individual item cap is well below what you own.</li>"
    "<li><b>Accidental damage is often an add-on.</b> The most common real-world claim is frequently excluded from the base policy.</li>"
    "<li><b>Excess interacts with small claims.</b> If the excess is close to the value of typical losses, the policy only helps in serious cases.</li>"
    "</ul>"
    "<p>See <a href=\"/money/home-insurance-explained/\">home insurance explained</a>, <a href=\"/money/insurance-deductibles-and-excess-explained/\">deductibles and excess</a> and <a href=\"/money/how-insurance-claims-work-explained/\">how insurance claims work</a>.</p>",

"money/overdraft-fees-explained":
    "<h2>The most expensive credit most people use</h2>"
    "<p>An overdraft is borrowing, and priced per year it is usually the costliest credit a household holds &mdash; more expensive than a credit card and far more expensive than a personal loan. It survives because it is frictionless: there is no application at the moment of need. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes the guidance on overdraft practices and fees this page follows. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>How the charges actually accumulate</h2>"
    "<ul>"
    "<li><b>Interest accrues daily</b> on the outstanding amount, so a small balance held for months costs more than it appears to.</li>"
    "<li><b>Unarranged overdrafts cost more than arranged ones</b>, and going beyond an agreed limit can trigger a higher rate on the whole balance.</li>"
    "<li><b>Some schemes charge per item.</b> Multiple small transactions in one day can each attract a fee.</li>"
    "<li><b>A refusal can still cost money.</b> Declined-payment fees exist in some arrangements even when nothing is borrowed.</li>"
    "</ul>"
    "<p>If an overdraft is being used regularly rather than occasionally, it has become a loan and should be refinanced as one. See <a href=\"/money/how-to-negotiate-with-creditors-explained/\">negotiating with creditors</a>, <a href=\"/money/debt-consolidation-explained/\">debt consolidation</a> and <a href=\"/money/emergency-fund-guide/\">the emergency fund guide</a>.</p>",

"money/debt-snowball-vs-avalanche":
    "<h2>Two methods, one arithmetic difference</h2>"
    "<p>The avalanche method clears the highest-interest debt first and is mathematically cheaper. The snowball method clears the smallest balance first and produces visible progress sooner. The comparison is usually presented as a choice between logic and psychology, but both are rational if the second one is what gets completed. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes the debt-repayment guidance behind this page. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>How to choose between them</h2>"
    "<ul>"
    "<li><b>Measure the actual gap.</b> Run both orders and compare the total interest; sometimes it is small enough to be irrelevant.</li>"
    "<li><b>Check whether one debt has consequences.</b> Secured debt and anything affecting housing or utilities should be prioritised regardless of rate.</li>"
    "<li><b>Count the balances.</b> Closing several accounts quickly reduces the number of payments to track, which lowers the chance of a missed one.</li>"
    "<li><b>Be honest about persistence.</b> A cheaper plan abandoned in month four costs more than an expensive plan finished.</li>"
    "</ul>"
    "<p>See <a href=\"/money/credit-card-payoff-calculator/\">the credit card payoff calculator</a>, <a href=\"/money/how-to-negotiate-with-creditors-explained/\">negotiating with creditors</a> and <a href=\"/money/debt-relief-options-explained/\">debt relief options</a>.</p>",

"money/good-debt-vs-bad-debt-explained":
    "<h2>The distinction is about the return, not the label</h2>"
    "<p>Calling debt good or bad is shorthand, and the shorthand misleads: what matters is whether the borrowing buys something whose return exceeds its cost. A loan is a rate. Everything else is a comparison against that rate. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on borrowing and investing decisions this page follows. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>Three tests worth applying</h2>"
    "<ul>"
    "<li><b>Does it buy an asset or an expense?</b> A loan against something that holds value behaves differently from one against consumption.</li>"
    "<li><b>What is the rate, honestly stated?</b> A loan's rate is a certain return working against you, and few investments reliably beat a high one.</li>"
    "<li><b>What happens if income stops?</b> The difference between manageable and dangerous debt is usually the payment's size relative to income, not the purpose.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-interest-rates-work-explained/\">how interest rates work</a>, <a href=\"/money/how-loan-amortisation-works-explained/\">how loan amortisation works</a> and <a href=\"/money/how-personal-loans-work-explained/\">how personal loans work</a>.</p>",

"money/income-protection-insurance-explained":
    "<h2>It replaces income, not health</h2>"
    "<p>Income protection pays a percentage of earnings when illness or injury prevents work, and the definitions inside the policy decide whether it pays at all. The most consequential is usually the distinction between own-occupation and any-occupation cover: the first pays if you cannot do your job, the second only if you cannot do any job you are suited to. <a href=\"" + GOVUK + "\" rel=\"noopener\">GOV.UK</a> publishes guidance on sick pay and statutory entitlements that sit alongside this cover. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The terms that decide the value</h2>"
    "<ul>"
    "<li><b>Deferred period.</b> The wait before payments start; longer deferral is cheaper and should match your sick pay and savings.</li>"
    "<li><b>Benefit period.</b> How long payments continue &mdash; to a fixed age, or for a limited number of years.</li>"
    "<li><b>Definition of incapacity.</b> Own-occupation costs more and is worth the difference for skilled professions.</li>"
    "<li><b>Exclusions.</b> Pre-existing conditions and some mental-health provisions vary widely between policies.</li>"
    "</ul>"
    "<p>See <a href=\"/money/critical-illness-insurance-explained/\">critical illness insurance</a>, <a href=\"/money/life-insurance-basics-explained/\">life insurance basics</a> and <a href=\"/money/emergency-fund-guide/\">the emergency fund guide</a>.</p>",

"money/trading-risk-checklist":
    "<h2>A checklist that assumes you will be wrong</h2>"
    "<p>Risk control is not about predicting correctly; it is about surviving the trades where the prediction fails. Every item here exists because a specific failure mode is common, documented and avoidable. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on trading risk and fraud that this desk's framing follows. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>Before every position</h2>"
    "<ul>"
    "<li><b>Know the exit before the entry.</b> A stop decided after the loss appears is not a stop.</li>"
    "<li><b>Size from the stop, not the conviction.</b> Position size should follow from how far the stop is and what you can lose, not from how confident you feel.</li>"
    "<li><b>Cap the day.</b> A daily loss limit is the only reliable defence against a bad session becoming a bad month.</li>"
    "<li><b>Include the costs.</b> Spread, commission and slippage belong in the calculation, not after it.</li>"
    "<li><b>Never add to a losing position to average down</b> without a rule written in advance.</li>"
    "</ul>"
    "<p>See <a href=\"/money/position-sizing-101/\">position sizing</a>, <a href=\"/money/risk-of-ruin-explained/\">risk of ruin explained</a> and <a href=\"/money/leverage-and-margin-explained/\">leverage and margin</a>.</p>",

"money/how-insurance-premiums-are-calculated-explained":
    "<h2>Premiums price a probability, plus costs</h2>"
    "<p>A premium is an expected loss, plus the insurer's expenses and margin, spread across a pool. Understanding the structure explains why premiums behave counter-intuitively: they rise for the whole pool after a bad claims year even when an individual has not claimed. <a href=\"" + FTC + "\" rel=\"noopener\">The Federal Trade Commission</a> publishes consumer guidance on insurance purchasing and comparison. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The inputs that move your price</h2>"
    "<ul>"
    "<li><b>Exposure.</b> Value at risk, location and usage are the primary drivers and the ones you can sometimes change.</li>"
    "<li><b>Claims history.</b> Individual history matters, but pool experience matters too.</li>"
    "<li><b>Excess selected.</b> A higher excess lowers the premium because the insurer's expected payout falls.</li>"
    "<li><b>Cover scope.</b> Add-ons are priced individually and are the easiest part of a premium to reduce.</li>"
    "</ul>"
    "<p>See <a href=\"/money/insurance-deductibles-and-excess-explained/\">deductibles and excess</a>, <a href=\"/money/how-insurance-claims-work-explained/\">how claims work</a> and <a href=\"/money/how-car-insurance-works/\">how car insurance works</a>.</p>",

"money/checking-and-savings-accounts-explained":
    "<h2>Two accounts with different jobs</h2>"
    "<p>A transactional account exists for movement and a savings account for accumulation, and using one for the other costs something in each direction. The practical benefit of separating them is less about interest than about visibility: money you cannot see is money you do not spend. <a href=\"" + FDIC + "\" rel=\"noopener\">The FDIC</a> publishes the deposit insurance rules that apply to both, and <a href=\"" + NCUA + "\" rel=\"noopener\">mycreditunion.gov</a> covers the credit union equivalent. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What to compare</h2>"
    "<ul>"
    "<li><b>Fees and their triggers.</b> Minimum-balance and maintenance fees can exceed the interest earned on a small balance.</li>"
    "<li><b>Access limits.</b> Some savings products restrict withdrawals, which is a feature if the goal is accumulation.</li>"
    "<li><b>Rate type.</b> A teaser rate that reverts after a few months is a different product from a standing one.</li>"
    "<li><b>The entity behind the brand.</b> Cover follows the licensed institution, not the trading name.</li>"
    "</ul>"
    "<p>See <a href=\"/money/high-yield-savings-accounts-explained/\">high-yield savings accounts</a>, <a href=\"/money/how-deposit-insurance-works-explained/\">how deposit insurance works</a> and <a href=\"/money/emergency-fund-guide/\">the emergency fund guide</a>.</p>",

"money/budget-50-30-20-explained":
    "<h2>A starting frame, not a rule</h2>"
    "<p>The 50/30/20 split allocates after-tax income across needs, wants and saving. Its value is that it forces the three categories apart, which is the part most budgeting fails at. Its weakness is that it assumes the split is achievable, and in high-cost housing markets the needs category alone can exceed half. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes budgeting guidance for households. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>Making it work with real numbers</h2>"
    "<ul>"
    "<li><b>Classify honestly.</b> The category errors matter more than the percentages &mdash; a car payment is a need, a larger car is not.</li>"
    "<li><b>Adjust the ratios to your costs.</b> If needs are 65%, the useful move is to find the saving elsewhere rather than to pretend.</li>"
    "<li><b>Treat saving as the first allocation.</b> What is left after spending is never 20%.</li>"
    "<li><b>Review the wants category, not the needs.</b> Needs are largely fixed in the short run; wants are where the flexibility is.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-to-budget-with-irregular-income/\">budgeting with irregular income</a>, <a href=\"/money/sinking-funds-explained/\">sinking funds</a> and <a href=\"/money/savings-goal-calculator/\">the savings goal calculator</a>.</p>",

"money/critical-illness-insurance-explained":
    "<h2>It pays on diagnosis, not on need</h2>"
    "<p>Critical illness cover pays a lump sum when a condition listed in the policy is diagnosed to the stated severity. The gap between a clinical diagnosis and the policy's definition is where most disputes arise, so the schedule of conditions is the document to read rather than the summary. <a href=\"" + GOVUK + "\" rel=\"noopener\">GOV.UK</a> publishes guidance on the state support available alongside private cover. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What to read before buying</h2>"
    "<ul>"
    "<li><b>The condition list and its severity thresholds.</b> Early-stage conditions are frequently excluded or paid at a reduced percentage.</li>"
    "<li><b>Survival period.</b> Some policies require surviving a set number of days after diagnosis before payment.</li>"
    "<li><b>Whether it is combined with life cover.</b> A combined policy pays once, not twice, which is often misunderstood.</li>"
    "<li><b>Exclusions and pre-existing conditions.</b> These are declared at application and revisited at claim.</li>"
    "</ul>"
    "<p>See <a href=\"/money/income-protection-insurance-explained/\">income protection insurance</a>, <a href=\"/money/life-insurance-basics-explained/\">life insurance basics</a> and <a href=\"/money/health-insurance-basics-explained/\">health insurance basics</a>.</p>",

"money/moving-averages-sma-vs-ema":
    "<h2>Both smooth; they differ in what they weight</h2>"
    "<p>A simple moving average weights every bar equally across the window; an exponential average weights recent bars more heavily and therefore responds faster. Neither is more accurate &mdash; the EMA simply trades lag for noise, and the choice is a choice about which error you prefer. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on technical analysis and its limits. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>Choosing between them</h2>"
    "<ul>"
    "<li><b>SMA for slower, cleaner signals.</b> It ignores old bars abruptly, which can produce a visible step when a large bar leaves the window.</li>"
    "<li><b>EMA for responsiveness.</b> Useful where reaction time matters more than smoothness, at the cost of more false signals.</li>"
    "<li><b>Period matters more than type.</b> A 10-bar SMA and a 10-bar EMA differ less than either differs from a 50-bar version.</li>"
    "<li><b>Both lag by construction.</b> A moving average is derived from past prices and cannot anticipate a turn.</li>"
    "</ul>"
    "<p>See <a href=\"/money/technical-indicators-explained/\">technical indicators explained</a>, <a href=\"/money/atr-indicator-guide/\">the ATR indicator guide</a> and <a href=\"/money/backtesting-101/\">backtesting 101</a>.</p>",

"money/employer-pension-matching-explained":
    "<h2>The match is free money with conditions</h2>"
    "<p>An employer match is a return no investment can promise: contributing enough to earn a 50% match is an instant 50% on that money before markets do anything. The conditions are what people miss &mdash; vesting schedules, contribution caps and eligibility waiting periods all determine how much of it is actually yours. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on workplace retirement plans and matching. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What to check in your scheme</h2>"
    "<ul>"
    "<li><b>The match formula.</b> Percentage matched, up to what contribution, and whether it is tiered.</li>"
    "<li><b>Vesting.</b> Employer contributions may belong to you only after a set period of service.</li>"
    "<li><b>The cap.</b> Contributing above the match threshold earns no immediate return, which changes the priority order.</li>"
    "<li><b>Default fund choice.</b> The default is usually conservative and worth reviewing rather than accepting.</li>"
    "</ul>"
    "<p>See <a href=\"/money/retirement-savings-basics-explained/\">retirement savings basics</a>, <a href=\"/money/salary-sacrifice-explained/\">salary sacrifice explained</a> and <a href=\"/money/how-much-to-save-for-retirement-explained/\">how much to save for retirement</a>.</p>",

"money/mortgage-fees-and-closing-costs-explained":
    "<h2>The fee total is larger than the rate comparison</h2>"
    "<p>Borrowers compare rates closely and fees loosely, which inverts their importance on a short-held mortgage: over a few years, arrangement and closing costs can outweigh the difference between two rates. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes the disclosure rules and guidance on mortgage closing costs. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The costs to itemise</h2>"
    "<ul>"
    "<li><b>Arrangement and application fees</b>, sometimes addable to the loan, which means paying interest on them.</li>"
    "<li><b>Valuation and legal fees</b>, which are payable whether or not the purchase completes.</li>"
    "<li><b>Broker fees</b>, which may be charged to you, by the lender, or both.</li>"
    "<li><b>Early repayment charges</b>, which determine the real cost of leaving early and are the most commonly overlooked figure.</li>"
    "</ul>"
    "<p>Compare total cost over the period you expect to hold, not the headline rate. See <a href=\"/money/mortgage-types-explained/\">mortgage types explained</a>, <a href=\"/money/how-to-remortgage-explained/\">how to remortgage</a> and <a href=\"/money/how-mortgage-approval-works-explained/\">how mortgage approval works</a>.</p>",

"money/atr-indicator-guide":
    "<h2>ATR measures movement, not direction</h2>"
    "<p>Average True Range quantifies how much an instrument typically moves over a period, including gaps, which is what makes it useful for stops: a stop set at a fixed distance ignores that different instruments move different amounts. ATR is descriptive, and treating it as predictive is the common misuse. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes guidance on trading tools and their limitations. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>Using it properly</h2>"
    "<ul>"
    "<li><b>Size stops in multiples of ATR</b> rather than in fixed price distance, so the stop reflects the instrument's own behaviour.</li>"
    "<li><b>Compare ATR across instruments</b> to see which is genuinely more volatile, rather than judging by price.</li>"
    "<li><b>Watch for regime change.</b> A rising ATR means widening ranges, which affects position size as well as stops.</li>"
    "<li><b>Do not read direction from it.</b> ATR rises on large moves in either direction.</li>"
    "</ul>"
    "<p>See <a href=\"/money/position-sizing-101/\">position sizing</a>, <a href=\"/money/technical-indicators-explained/\">technical indicators explained</a> and <a href=\"/money/moving-averages-sma-vs-ema/\">moving averages</a>.</p>",

"money/mortgage-types-explained":
    "<h2>The type determines what you are exposed to</h2>"
    "<p>Mortgage products differ mainly in who carries interest-rate risk and for how long. A fixed rate transfers it to the lender for a term; a variable rate keeps it with the borrower; and the choice between them is a view about rates combined with a statement about how much payment variability you can absorb. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes guidance comparing mortgage product types. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>Comparing them on the right basis</h2>"
    "<ul>"
    "<li><b>Fix the period you are judging.</b> A rate is only comparable over the same timeframe, including what happens after the initial period ends.</li>"
    "<li><b>Read the reversion rate.</b> The rate after the deal ends is often the most expensive part of the product.</li>"
    "<li><b>Check portability and overpayment.</b> These determine whether the product survives a move or a windfall.</li>"
    "<li><b>Interest-only needs a repayment plan</b>, not an intention; lenders increasingly require evidence of one.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-mortgages-work-explained/\">how mortgages work</a>, <a href=\"/money/mortgage-ltv-and-deposits-explained/\">LTV and deposits</a> and <a href=\"/money/mortgage-payment-calculator/\">the mortgage payment calculator</a>.</p>",

"money/insurance-deductibles-and-excess-explained":
    "<h2>The excess is a price you choose</h2>"
    "<p>An excess is the amount you pay on every claim before the insurer pays anything, and selecting it is a real financial decision rather than a formality. A higher excess lowers the premium because the insurer's expected payout falls &mdash; but only helps if you can actually meet the excess when the claim happens. <a href=\"" + FTC + "\" rel=\"noopener\">The Federal Trade Commission</a> publishes consumer guidance on choosing insurance cover. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>How to set it</h2>"
    "<ul>"
    "<li><b>Compare premium saving against exposure.</b> The saving is certain and small; the excess is contingent and large.</li>"
    "<li><b>Check the typical claim size.</b> If most losses are below the excess, the policy only responds to serious events.</li>"
    "<li><b>Look for compulsory and voluntary excesses.</b> They stack, so the amount you actually pay can exceed the figure you selected.</li>"
    "<li><b>Consider claim frequency.</b> Multiple claims each attract the excess, which matters for policies covering frequent small losses.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-insurance-premiums-are-calculated-explained/\">how premiums are calculated</a>, <a href=\"/money/how-insurance-claims-work-explained/\">how claims work</a> and <a href=\"/money/home-insurance-explained/\">home insurance explained</a>.</p>",

"money/travel-insurance-explained":
    "<h2>Medical cover is the part that matters</h2>"
    "<p>Travel insurance is usually bought for lost luggage and used for medical emergencies, which inverts how people compare policies. Cancellation and medical limits differ by an order of magnitude in their potential financial impact, and the exclusions around pre-existing conditions are the most common source of refused claims. <a href=\"" + FTC + "\" rel=\"noopener\">The Federal Trade Commission</a> publishes consumer guidance on travel insurance purchasing. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What to check</h2>"
    "<ul>"
    "<li><b>Medical limit and repatriation.</b> The headline figure should be large enough for the destination's healthcare costs, including evacuation.</li>"
    "<li><b>Pre-existing condition declaration.</b> Undeclared conditions commonly void the medical element entirely.</li>"
    "<li><b>Cancellation triggers.</b> What counts as a covered reason is narrower than travellers assume.</li>"
    "<li><b>Activity exclusions.</b> Many policies exclude specific activities unless declared, and the list is not intuitive.</li>"
    "</ul>"
    "<p>See <a href=\"/money/health-insurance-basics-explained/\">health insurance basics</a>, <a href=\"/money/how-insurance-claims-work-explained/\">how claims work</a> and <a href=\"/money/insurance-deductibles-and-excess-explained/\">deductibles and excess</a>.</p>",

"money/how-insurance-claims-work-explained":
    "<h2>A claim is an assessment, not a request</h2>"
    "<p>When a claim is filed, the insurer assesses whether the loss falls within the policy's terms before it calculates any payment. That sequence explains most claim friction: disagreements are usually about coverage rather than about amount, and they are settled by the policy wording rather than by the size of the loss. <a href=\"" + FTC + "\" rel=\"noopener\">The Federal Trade Commission</a> publishes consumer guidance on the claims process. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What improves the outcome</h2>"
    "<ul>"
    "<li><b>Notify promptly.</b> Most policies set a reporting window, and late notification is a common ground for refusal.</li>"
    "<li><b>Document before repairing.</b> Photographs and records taken before any remedial work are difficult to reconstruct afterwards.</li>"
    "<li><b>Read the wording, not the summary.</b> The schedule defines the cover; the marketing does not.</li>"
    "<li><b>Keep the correspondence.</b> A claim that is refused on one basis can be reassessed on another if the record is complete.</li>"
    "</ul>"
    "<p>See <a href=\"/money/insurance-deductibles-and-excess-explained/\">deductibles and excess</a>, <a href=\"/money/how-insurance-premiums-are-calculated-explained/\">how premiums are calculated</a> and <a href=\"/money/home-insurance-explained/\">home insurance explained</a>.</p>",

"money/how-to-remortgage-explained":
    "<h2>Remortgaging is a comparison, not a switch</h2>"
    "<p>The decision is whether a new product costs less over the period you will hold it than staying on the current one &mdash; and the current deal's exit charges belong inside that comparison rather than outside it. Borrowers who compare rates without including early repayment charges routinely reach the wrong conclusion. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes guidance on refinancing costs. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The calculation, in order</h2>"
    "<ul>"
    "<li><b>Establish the current exit cost.</b> Early repayment charges plus any exit fees, which can be substantial early in a deal.</li>"
    "<li><b>Total the new product's fees.</b> Arrangement, valuation and legal costs, including anything added to the loan.</li>"
    "<li><b>Compare over the intended holding period.</b> A lower rate that takes four years to recover its fees is a poor trade on a two-year plan.</li>"
    "<li><b>Check whether the timing can be prepared.</b> Many lenders allow a new deal to be arranged ahead of the current one ending.</li>"
    "</ul>"
    "<p>See <a href=\"/money/mortgage-fees-and-closing-costs-explained/\">mortgage fees and closing costs</a>, <a href=\"/money/mortgage-types-explained/\">mortgage types explained</a> and <a href=\"/money/mortgage-ltv-and-deposits-explained/\">LTV and deposits</a>.</p>",

"money/mortgage-vs-renting-explained":
    "<h2>The comparison usually omits the costs of owning</h2>"
    "<p>Rent-versus-buy is commonly reduced to mortgage payment against rent, which leaves out maintenance, transaction costs, insurance, and the fact that a mortgage payment contains two different things: interest, which is a cost, and principal, which is a transfer to savings. Once all of it is included, the answer depends heavily on how long the property is held. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes guidance on the costs of homeownership. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What belongs in the comparison</h2>"
    "<ul>"
    "<li><b>Total cost of ownership.</b> Interest, maintenance, insurance, taxes and transaction costs &mdash; not the monthly payment alone.</li>"
    "<li><b>The holding period.</b> Transaction costs are recovered over years, so a short hold rarely works.</li>"
    "<li><b>The alternative use of the deposit.</b> Money tied up in equity is money not invested elsewhere, and that comparison should be explicit.</li>"
    "<li><b>Mobility.</b> Renting prices flexibility; owning prices stability. Neither is free.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-to-save-for-a-house-deposit/\">saving for a house deposit</a>, <a href=\"/money/mortgage-fees-and-closing-costs-explained/\">mortgage fees and closing costs</a> and <a href=\"/money/how-mortgages-work-explained/\">how mortgages work</a>.</p>",

"money/mortgage-ltv-and-deposits-explained":
    "<h2>LTV drives the price more than the rate shopping does</h2>"
    "<p>Loan-to-value expresses the loan as a proportion of the property value, and lenders price risk in bands: crossing from one band to the next usually changes the available rate more than any amount of comparison shopping within a band. This makes the deposit decision a rate decision. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes guidance on down payments and mortgage terms. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The practical implications</h2>"
    "<ul>"
    "<li><b>Band thresholds matter more than increments.</b> An extra few percent of deposit only helps if it crosses a band boundary.</li>"
    "<li><b>Valuation can move the LTV.</b> If the lender's valuation is below the agreed price, the effective LTV rises.</li>"
    "<li><b>Equity changes the position later.</b> Rising value or capital repayment lowers LTV, which can unlock better rates on remortgage.</li>"
    "<li><b>High LTV products carry other conditions</b>, including mortgage insurance in some markets, which adds to the monthly cost.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-to-save-for-a-house-deposit/\">saving for a house deposit</a>, <a href=\"/money/mortgage-types-explained/\">mortgage types explained</a> and <a href=\"/money/how-mortgage-approval-works-explained/\">how mortgage approval works</a>.</p>",

"money/how-mortgage-approval-works-explained":
    "<h2>Approval is an assessment of repayment, not of affordability</h2>"
    "<p>A lender assesses whether the loan can be repaid under stress, which is a stricter test than whether the current payment fits the current budget. This is why an applicant can be comfortably affording their rent and still be approved for less than expected: the assessment applies a higher rate and adds committed outgoings. <a href=\"" + CFPB + "\" rel=\"noopener\">The Consumer Financial Protection Bureau</a> publishes guidance on mortgage qualification and the application process. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>What the assessment looks at</h2>"
    "<ul>"
    "<li><b>Income, verified.</b> Payslips, and for self-employed applicants usually several years of accounts.</li>"
    "<li><b>Committed outgoings.</b> Existing credit, loan repayments and dependant costs are all deducted before the mortgage figure.</li>"
    "<li><b>Conduct.</b> Credit history and any missed payments, which affect both approval and rate.</li>"
    "<li><b>The property itself.</b> Valuation and, in some cases, construction type influence the decision as well as the LTV.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-credit-scores-work/\">how credit scores work</a>, <a href=\"/money/mortgage-ltv-and-deposits-explained/\">LTV and deposits</a> and <a href=\"/money/how-payslips-work-explained/\">how payslips work</a>.</p>",

"money/risk":
    "<h2>Risk is measurable, and usually underestimated</h2>"
    "<p>Risk in trading is not the possibility of loss but the size of loss relative to the account, which makes it a quantity that can be set before a trade rather than discovered during it. Most account failures come from a small number of positions sized too large, not from a low win rate. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on trading risk this section follows. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The sequence that controls it</h2>"
    "<ul>"
    "<li><b>Decide the loss first.</b> What the trade costs if it is wrong, stated in currency before entry.</li>"
    "<li><b>Derive the size from the loss.</b> Position size follows from the stop distance and the risk amount, never from conviction.</li>"
    "<li><b>Cap the aggregate.</b> Total open risk across positions matters more than any single one.</li>"
    "<li><b>Set a daily and monthly limit.</b> These are the controls that stop a bad session becoming a bad quarter.</li>"
    "</ul>"
    "<p>See <a href=\"/money/risk-of-ruin-explained/\">risk of ruin explained</a>, <a href=\"/money/position-sizing-101/\">position sizing</a> and <a href=\"/money/leverage-and-margin-explained/\">leverage and margin</a>.</p>",

"money/costs":
    "<h2>Costs compound against you, silently</h2>"
    "<p>Every trading cost is subtracted before any return is earned, and because costs recur while returns are uncertain, they dominate the outcome for anyone trading frequently. A strategy can be correct about direction and still lose money once spread, commission and slippage are applied. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on investment costs and fees this section follows. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The costs to account for</h2>"
    "<ul>"
    "<li><b>Spread.</b> Paid on entry, before the position can move in your favour.</li>"
    "<li><b>Commission.</b> Per trade or per unit, and often structured so that small trades pay proportionally more.</li>"
    "<li><b>Slippage.</b> The difference between the expected fill and the actual one, which grows in fast markets.</li>"
    "<li><b>Financing.</b> Overnight funding on leveraged positions, which can exceed the trading result on a long hold.</li>"
    "<li><b>Withdrawal and currency fees.</b> Small individually, meaningful across a year.</li>"
    "</ul>"
    "<p>See <a href=\"/money/trading-fees-explained/\">trading fees explained</a>, <a href=\"/money/forex-spreads-and-pips/\">spreads and pips</a> and <a href=\"/money/zero-commission-trading-truth/\">the truth about zero-commission trading</a>.</p>",

"money/start":
    "<h2>An order that avoids the expensive mistakes</h2>"
    "<p>Most people begin trading by opening an account and choosing an instrument, which puts the two decisions with the least long-term consequence first. The order that matters runs the other way: capital you can lose, then risk per trade, then instrument, then method. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes the guidance on getting started and on avoiding fraud, which is worth reading before depositing anything. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The sequence</h2>"
    "<ul>"
    "<li><b>Set the capital.</b> An amount whose total loss would not change your circumstances, separated from savings and emergency funds.</li>"
    "<li><b>Set the risk per trade.</b> A small fixed percentage, decided once and applied uniformly.</li>"
    "<li><b>Choose one market.</b> Depth in one instrument beats familiarity with five.</li>"
    "<li><b>Verify the broker.</b> Regulation, fee schedule and withdrawal process, checked before the first deposit rather than after.</li>"
    "<li><b>Keep records from the first trade.</b> A journal started later is missing the trades that taught the lessons.</li>"
    "</ul>"
    "<p>See <a href=\"/money/how-to-check-a-trading-broker/\">how to check a trading broker</a>, <a href=\"/money/trading-for-beginners/\">trading for beginners</a> and <a href=\"/money/demo-accounts-what-they-cant-teach/\">what demo accounts cannot teach</a>.</p>",

"money/charts":
    "<h2>What a chart can and cannot show</h2>"
    "<p>A chart is a record of transactions, not a forecast. It reliably shows what happened and when, and it is widely asked to show what happens next, which it cannot do &mdash; though it can show where previous participants reacted, which is a different and more defensible claim. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes guidance on technical analysis and its limits. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>Reading one sensibly</h2>"
    "<ul>"
    "<li><b>Timeframe changes the message.</b> The same instrument looks different on five minutes and on a day, and neither is more true.</li>"
    "<li><b>Volume gives the price context.</b> A move on low participation means less than the same move on high participation.</li>"
    "<li><b>Support and resistance describe memory.</b> They mark where orders previously clustered, which is a tendency rather than a rule.</li>"
    "<li><b>Indicators are derived.</b> Every one is computed from past price, so none can lead it.</li>"
    "</ul>"
    "<p>See <a href=\"/money/technical-indicators-explained/\">technical indicators explained</a>, <a href=\"/money/moving-averages-sma-vs-ema/\">moving averages</a> and <a href=\"/money/backtesting-101/\">backtesting 101</a>.</p>",

"money/method":
    "<h2>A method is a set of rules you can audit</h2>"
    "<p>The difference between a method and an intuition is that a method states its entry, exit, size and invalidation in advance, which makes it possible to evaluate afterwards. Without those four stated, there is nothing to review and no way to know whether results came from the approach or from the market. <a href=\"" + INV + "\" rel=\"noopener\">Investor.gov</a> publishes guidance on evaluating trading claims. By the Bryme Money desk. Reviewed 27 September 2026.</p>"
    "<h2>The four parts, and why each is needed</h2>"
    "<ul>"
    "<li><b>Entry.</b> Specific enough that two people would identify the same setup.</li>"
    "<li><b>Exit.</b> Both the profit target and the stop, since an approach with only one is incomplete.</li>"
    "<li><b>Size.</b> Derived from the stop distance and the risk per trade.</li>"
    "<li><b>Invalidation.</b> The condition under which the approach is abandoned rather than adjusted &mdash; the part almost always missing.</li>"
    "</ul>"
    "<p>A method also needs a sample. Ten trades cannot distinguish skill from chance, which is why records matter more than results in the early period. See <a href=\"/money/backtesting-101/\">backtesting 101</a>, <a href=\"/money/trading-risk-checklist/\">the trading risk checklist</a> and <a href=\"/money/expectancy-calculator/\">the expectancy calculator</a>.</p>",

}
