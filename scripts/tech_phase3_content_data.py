# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 3 (2026-09-25).

Closes the buying and subscriptions shelves to ten and deepens the quantitative
shelf with two methodology pieces that are educational by design (never
investment advice, no fabricated results). Same discipline: evergreen mechanics
and decision guidance, no volatile statistics, dated official sources where a
source is needed, honest "choose A if / choose B if" framing.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE3_GUIDES = [

# ---------------------------------------------------------------- BUYING (close to 10)
("refurbished-vs-new-the-warranty-math", "buying", "guide",
"Refurbished vs new: the decision is the warranty, not the discount",
"A refurb is a good buy when the warranty and return window nearly match new, and a bad one when they don't. Read the two numbers before the price and the choice makes itself.",
"""<p>The honest question about refurbished hardware is not "is it as good as new" - a genuinely refurbished unit usually is - but "what happens if it isn't." That question is answered by exactly two numbers: the warranty length and the return window. The discount is only worth taking when those two numbers are close to what you'd get with new; when they aren't, you are not buying a cheaper laptop, you are buying a cheaper laptop plus all the risk the manufacturer declined to carry.</p>
<h2>Read the warranty before the price</h2>
<p>Manufacturer-certified refurbishment (the vendor's own refurbished store) typically ships with a warranty close to the new-product one - often a full year - and a normal return window. That is the good case: same testing, same parts discipline, nearly the same safety net, at a real discount. Third-party "refurbished" with a thirty- or ninety-day warranty is a different product: the discount now has to compensate you for the gap between ninety days and a year of cover, and for the fact that the unit's history is someone else's word.</p>
<h2>The return window is the real test drive</h2>
<p>Failures that matter usually show up in the first weeks - a weak battery, a flaky port, a fan that drones. A generous return window lets you discover them while it's still the seller's problem. A short or restocked-heavy return policy pushes that risk onto you. So compare return windows the way you compare warranties: a refurb with a fourteen-day window is asking you to accept a defect-discovery window a new purchase wouldn't.</p>
<h2>Choose refurbished if / choose new if</h2>
<p>Choose refurbished if the unit is manufacturer-certified, the warranty is a year or close to it, the return window is normal, and the part that ages fastest - the battery - is stated to be new or replaced. Choose new if the refurb's warranty or return window is materially worse and the discount is small, if you need the machine to be dependable for a fixed deadline, or if the only refurbs available are third-party with opaque history. The middle case - big discount, weak cover - is the one to slow down on: that is where the false economy lives.</p>
<p>The same logic applies to the machines students and small teams buy on tight budgets; the spec-floor question in <a href="/tech/student-laptop-spec-floor-2026/">the honest spec floor for a student laptop</a> tells you the minimum machine, and the warranty maths above tells you whether the cheap route to that machine is actually cheap. For a worked brand comparison in one market, see <a href="/tech/dell-vs-hp-refurbished-laptops-nigeria/">refurbished Dell vs HP</a>.</p>""",
[("Apple Certified Refurbished", "https://www.apple.com/shop/refurbished")],
["student-laptop-spec-floor-2026", "dell-vs-hp-refurbished-laptops-nigeria"]),

("monitor-buying-what-you-actually-see", "buying", "guide",
"Monitor buying: resolution, size and refresh, by what your eye can actually use",
"Same rule as the TV: density at your seating distance decides resolution value, and refresh rate only pays for the content that moves. Spend on the axis you can perceive.",
"""<p>Monitor marketing sells three numbers - resolution, size, refresh - as if each were independently better. In practice each is only worth paying for when your eye and your content can use it, and the deciding variable for two of the three is the same one as the living-room: your distance from the panel.</p>
<h2>Resolution is density at your distance</h2>
<p>At a normal desk distance (roughly an arm's length to a metre), a 27-inch 1440p panel is visibly sharper than 1080p, and 4K on 27 inches is finer than most people can resolve - the text-rendering gain tapers off. The honest read: 24-inch 1080p is fine for general work; 27-inch 1440p is the sweet spot where the extra pixels are plainly used at desk distance; 4K pays mainly when you sit closer, run a larger panel, or do detail work. Size and resolution move together - a 32-inch 4K is the same density as a 16-inch laptop, which is exactly the point: buy density, not a badge. The same logic is worked for the TV in <a href="/tech/4k-on-a-small-tv-when-its-invisible/">4K on a small screen</a>.</p>
<h2>Refresh rate pays only for motion</h2>
<p>A 120 or 144&nbsp;Hz panel shows more frames per second, which reads as smoother motion - valuable for fast games and, subtly, for scrolling. For static work, writing and video at 24-60fps, the benefit is small to none. So the question is what moves on your screen: if fast games do, refresh pays; if your day is text and spreadsheets, spend that money on resolution or size instead. Note the chain too: the panel's refresh is only useful if the source and cable deliver the frames, mirroring the weakest-link lesson from <a href="/tech/hdr-formats-the-weakest-link/">HDR chains</a>.</p>
<h2>The one axis everyone under-checks: the stand and the panel uniformity</h2>
<p>Two specs are lived with daily and rarely compared: height/tilt adjustment (a fixed stand is a daily tax) and panel uniformity/backlight bleed (visible in dark scenes). These are the reasons a "better" monitor feels worse. Check adjustment range before purchase, and treat reviews that photograph uniformity as more useful than the headline numbers.</p>
<p>So: fix density for your distance first, spend on refresh only if motion is your content, and let adjustability and uniformity break ties. That ordering keeps the money on the axes you can actually see.</p>""",
[],
["4k-on-a-small-tv-when-its-invisible", "hdr-formats-the-weakest-link", "student-laptop-spec-floor-2026"]),

# ---------------------------------------------------------------- SUBSCRIPTIONS (close to 10)
("subscription-audit-that-actually-sticks", "subscriptions", "guide",
"The subscription audit that sticks: list from the statement, rank by last use, kill by the official path",
"Most audits fail because they start from memory. Start from the bank statement, rank by when you last used each one, and cancel through the official path with a calendar note - then the audit survives the month.",
"""<p>A subscription audit that lasts is a method, not a mood. The mood version - "I'll cancel stuff this weekend" - fails because it starts from memory, and memory undercounts exactly the subscriptions that are quietly billing you. The method version starts from the one record that doesn't lie: the money leaving your account.</p>
<h2>Step one: list from the statement, not from memory</h2>
<p>Pull three months of statements and write down every recurring charge, including the small ones and the ones billed annually (annuals hide precisely because they don't appear monthly). The point is completeness: the audit acts on the list, and anything not on the list keeps billing you. This is also where you discover the price rises - the charge that crept up since you signed up, which is its own reason to re-decide.</p>
<h2>Step two: rank by last use, not by price</h2>
<p>For each line, answer one question: when did I last actually use it? The expensive service you use weekly is fine; the cheap one you haven't touched in two months is the leak - and twelve cheap untouched services are not cheap. Ranking by last use surfaces the true waste better than ranking by price, because waste is a function of non-use, and small recurring amounts are the hardest to notice individually.</p>
<h2>Step three: kill by the official path, and calendar the rest</h2>
<p>Cancel through the vendor's own cancellation flow, and keep the confirmation email - a cancellation that isn't confirmed is a cancellation that frequently didn't happen. For the ones you keep, put the renewal date in a calendar a few days ahead, especially annuals: the audit that sticks is the one that repeats automatically at each renewal instead of relying on you remembering to be vigilant.</p>
<h2>The keep-one rule</h2>
<p>Don't try to reach zero; reach deliberate. The goal is that every remaining line is one you would re-choose today at its current price. Anything you keep out of inertia gets one more billing cycle and then goes. The companion skills are knowing what the free tier already covers - the framing in <a href="/tech/cloud-storage-plans-compared/">cloud storage plans compared</a> - and knowing which recurring charges are actually worth it, as in <a href="/tech/which-vpn-subscription-is-worth-it/">which VPN subscription is worth it</a>.</p>""",
[],
["cloud-storage-plans-compared", "which-vpn-subscription-is-worth-it"]),

("free-trial-cancellation-traps", "subscriptions", "guide",
"Free-trial traps: the three mechanics that turn a trial into a charge, and the day-one defence",
"Pre-authorisation, the monthly-to-annual flip and the buried cancel path are the three mechanics. The defence is a day-one reminder and a noted cancel path - before the trial, not after the charge.",
"""<p>A free trial is a contract with a clock, and the traps are not tricks hidden in fine print so much as mechanics that work on forgetfulness. There are three, and knowing them converts a trial from a gamble into a scheduled decision.</p>
<h2>1. The pre-authorisation that becomes the charge</h2>
<p>Many trials take a card up front and pre-authorise a small or full amount. The trap is that when the trial ends, the switch to paid is automatic - the card is already authorised, so the first charge needs no new action from you. The defence is to treat "card required" as information: it means the default outcome is payment, and only your action prevents it. Set the reminder at sign-up, not when you remember.</p>
<h2>2. The monthly-to-annual flip</h2>
<p>Some offers present a low monthly figure but enrol you in an annual commitment, or convert the trial into a year at once - so the "small trial" becomes a large charge. Read, at sign-up, what the first charge will be and its period. If the first charge is annual and you wanted monthly, that is a decision to make before the trial, not a dispute after.</p>
<h2>3. The buried cancellation path</h2>
<p>The cancel flow is frequently longer and less visible than the sign-up flow - several screens, a retention offer at each, and a final confirm that is easy to miss. The trap is that people start cancelling, get interrupted at a retention screen, and never finish; the trial converts anyway. The defence is to finish to the confirmation email, and to note where the path was while you still remember it.</p>
<h2>The day-one defence</h2>
<p>Three habits, all done at sign-up: set a reminder a few days before the trial ends; screenshot or note the cancellation path and the stated first charge; and if you are unsure, decline trials that require a card when a no-card alternative exists. The reminder is the load-bearing one - every trap above only works if you forget, and a day-one reminder removes the forgetfulness the mechanics depend on. The wider discipline is the audit in <a href="/tech/subscription-audit-that-actually-sticks/">the subscription audit</a>; trials are just the subscriptions that sneak in.</p>""",
[],
["subscription-audit-that-actually-sticks"]),

# ---------------------------------------------------------------- QUANT (depth, educational)
("why-backtests-overfit-degrees-of-freedom", "quant", "guide",
"Why backtests overfit: the degrees-of-freedom problem, in plain terms",
"Every knob you tune is a question you ask the past, and the past always answers. The more knobs, the more the historical result flatters you - and the less it says about the future.",
"""<p>A backtest overfits for one underlying reason, and it has nothing to do with bad code: every parameter you tune is a question you put to history, and history will always produce an answer that sounds good. With enough questions, some answer will look excellent by chance alone - and that chance-looked-excellent answer is what you then mistake for a discovery.</p>
<h2>Knobs are questions, and the past always answers</h2>
<p>Suppose you test a rule and it loses, so you adjust a threshold and test again. Each adjustment uses the same historical data to pick the better-looking variant. After a dozen adjustments you have not discovered a rule that works; you have discovered the rule that, among the dozen you tried, happened to fit that particular past best. The fit is real - to the past. Its relevance to the future is what the tuning has quietly consumed.</p>
<h2>The multiple-testing intuition</h2>
<p>If you test one idea, a good historical result is meaningful. If you test a thousand, some will look good purely by luck - that is not skill, it is the arithmetic of many tries. The danger is that the researcher sees only the survivor: the one good line on the chart, not the nine hundred ninety-nine dead ones. Judging the survivor as if it were the only idea tested is the classic overfit.</p>
<h2>The defences, in order of power</h2>
<ul>
<li><b>Fewer knobs.</b> A rule with two parameters has far less freedom to bend to noise than one with ten. Simplicity is not aesthetic; it is statistical.</li>
<li><b>A holdout you never touch while tuning.</b> Reserve a slice of data the tuning never sees, and judge the final rule only there. If the holdout collapses, the fit was noise. See <a href="/tech/backtest-validation-checklist/">the backtest validation checklist</a> for the discipline.</li>
<li><b>Punish complexity when comparing.</b> Prefer the simpler rule that is nearly as good; the extra fit of the complex one is usually the noise you would otherwise carry forward.</li>
</ul>
<p>The companion failure modes - look-ahead and survivorship - are separate leaks and are covered in <a href="/tech/why-backtests-fail/">why backtests fail</a> and <a href="/tech/overfitting-detection-guide/">overfitting detection</a>. None of this is investment advice; it is the hygiene of not fooling yourself with your own historical data.</p>""",
[],
["backtest-validation-checklist", "why-backtests-fail", "overfitting-detection-guide"]),

("walk-forward-validation-explained", "quant", "guide",
"Walk-forward validation explained: train on the past, test on the next slice, roll",
"A static train/test split answers one question at one point in time. Walk-forward answers the real one: would this rule have kept working, month after month, as the world moved?",
"""<p>The honest question about any rule is not "did it work on the data I held out" but "would it have kept working as time moved." A single static split answers the first; walk-forward validation is built to answer the second, by replaying the way the rule would actually have been used: trained on the past, tested on the next slice, then rolled forward and repeated.</p>
<h2>The loop, plainly</h2>
<p>Take history up to some date, tune or fit the rule using only that window, then test it on the next slice - the period immediately after, which the fit never saw. Record that out-of-sample result. Now roll the window forward: add the tested slice to the training data, re-fit, and test the following slice. Repeat until history runs out. The final performance is the chain of those out-of-sample slices, each one a genuine "future" from the perspective of the fit that produced it.</p>
<h2>Why it beats one static split</h2>
<p>A single split gives you one out-of-sample verdict at one point in time - and a rule can pass it by fitting the particular regime that follows. Walk-forward gives many verdicts across many regimes: a rule that only works in one market condition shows it by collapsing on the slices where that condition is absent. You also get stability: if the rule's parameters jump wildly from window to window, that instability is itself a warning that you are fitting noise rather than finding structure - the same instinct as <a href="/tech/why-backtests-overfit-degrees-of-freedom/">the degrees-of-freedom problem</a>.</p>
<h2>The costs, honestly stated</h2>
<p>Walk-forward is expensive: every roll is a fresh fit, so it multiplies compute, and it demands enough history that each training window is meaningful. It also does not cure look-ahead or survivorship - if the data itself leaks the future, walk-forward merely repeats the leak many times. Those are separate hygiene items, covered in <a href="/tech/backtest-validation-checklist/">the validation checklist</a> and <a href="/tech/why-backtests-fail/">why backtests fail</a>.</p>
<p>Used well, walk-forward turns a single flattering backtest into a track record of out-of-sample slices - which is the closest a historical method gets to the truth that only live time can finally provide. This is educational methodology, not investment advice.</p>""",
[],
["backtest-validation-checklist", "why-backtests-overfit-degrees-of-freedom", "overfitting-detection-guide"]),

]
