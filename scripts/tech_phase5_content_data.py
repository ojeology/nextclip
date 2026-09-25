# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 5 (2026-09-25).

Deepens the quantitative shelf from nine pieces toward a real section. These are
methodology and craft pieces about backtesting and research hygiene — educational
by design, never investment advice, and with no fabricated results, returns or
benchmarks. They cross-link to the existing QuantLab pieces and to each other.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE5_GUIDES = [

# ---------------------------------------------------------------- QUANT (build out the shelf)
("transaction-costs-slippage-backtest-reality", "quant", "guide",
"Transaction costs and slippage: the line that turns a paper edge into a real one",
"A strategy can be right about direction and still lose money once you subtract the cost of acting. Here is how to model that cost honestly before you trust any backtest.",
"""<p>Most backtests that look brilliant die the moment they meet reality, and the usual killer is not a wrong signal — it is the cost of acting on the signal. Every trade pays a spread, a commission, and a little extra because your own order moved the price. A strategy that trades often pays that toll often, and a thin edge that survives on paper can be entirely consumed by it.</p>
<h2>The three costs, named</h2>
<p>The <strong>spread</strong> is the gap between the price you can buy at and the price you can sell at; crossing it is a cost even before any fee. The <strong>commission</strong> is the explicit fee per order or per unit. <strong>Slippage</strong> is the difference between the price your backtest assumed and the price you actually got, because the market moved or your size ate into the available orders. The first two are knowable; the third is the one optimists forget.</p>
<h2>Model the cost you would really pay, not the advertised one</h2>
<p>Subtract a realistic per-trade cost from every simulated fill — not the best-case promotional commission, but the spread you would actually cross plus a slippage allowance that grows with how big and how fast you trade. A strategy that trades a hundred times a month needs a far more honest cost model than one that trades twice a year, because the toll is paid a hundred times. If your edge per trade is smaller than your cost per trade, no amount of winning direction saves you.</p>
<h2>Why turnover is the hidden variable</h2>
<p>Two strategies with the same gross signal can have opposite net results purely because one trades ten times more. That is why cost modelling and the overfitting question are linked: a hyperactive strategy is often both more overfit (see <a href="/tech/why-backtests-overfit-degrees-of-freedom/">degrees of freedom</a>) and more cost-sensitive. Stress-test the result by doubling your assumed cost — if the edge vanishes, it was never much of an edge, and the <a href="/tech/backtest-validation-checklist/">validation checklist</a> is where that stress test belongs.</p>""",
[],
["why-backtests-overfit-degrees-of-freedom", "backtest-validation-checklist"]),

("survivorship-bias-the-quiet-data-trap", "quant", "guide",
"Survivorship bias: why testing on today's list of names flatters every result",
"If your dataset only contains things that still exist, you have silently deleted every failure. Here is how that bias sneaks in and how to defend against it.",
"""<p>Survivorship bias is the error of studying only the survivors and concluding the odds were always good. In quantitative work it shows up whenever a dataset contains the things that exist <em>now</em> rather than the things that existed <em>then</em> — and it makes almost every backtest look better than it is.</p>
<h2>How it sneaks in</h2>
<p>The classic case is a universe of companies or assets taken from a current list. That list excludes everything that was delisted, acquired, or went to zero along the way — precisely the outcomes a strategy most needs to be tested against. Buying "the survivors of the last decade" and measuring their returns is not a strategy; it is reading the answer key. The same trap appears in any domain: studying only the apps still in the store, the funds still open, the websites still online.</p>
<h2>Point-in-time data is the defence</h2>
<p>The fix is to test against the universe as it actually was at each moment — a point-in-time snapshot that includes the names that later died. This is harder to obtain and easy to get wrong, which is exactly why it matters: if your data source quietly backfilled a current membership list into the past, every result built on it is inflated. Ask of any dataset: "does this include the failures, or only the things that made it?"</p>
<h2>It is a family of look-ahead errors</h2>
<p>Survivorship bias is really a cousin of <a href="/tech/lookahead-bias-explained/">look-ahead bias</a> — both let information from the future leak into a test of the past. The habit that catches both is the same: be paranoid about what your code "knows" at each simulated moment. The <a href="/tech/overfitting-detection-guide/">overfitting detection guide</a> treats this as one of the standard things to check before believing any result.</p>""",
[],
["lookahead-bias-explained", "overfitting-detection-guide"]),

("data-snooping-when-you-test-too-many-ideas", "quant", "guide",
"Data snooping: the more ideas you test, the more fake winners you find",
"Test a hundred random rules and a few will look great by pure luck. Here is why that happens and the discipline that keeps you from shipping a coincidence.",
"""<p>If you flip enough coins, one of them will land heads ten times in a row, and it would be a mistake to conclude that coin is special. Data snooping is exactly this, in research: test enough ideas against the same historical data and a handful will look excellent purely by chance. The danger is that the lucky ones look identical to the real ones.</p>
<h2>Why the winners are partly luck</h2>
<p>Every test you run is a chance to find a spurious pattern. Run one hypothesis and a strong result is meaningful; run two hundred and the best of them is mostly noise that happened to fit. The number of ideas you tried — including the ones you discarded — is part of the evidence, and it is the part people forget to count. This is the same intuition behind <a href="/tech/why-backtests-overfit-degrees-of-freedom/">degrees of freedom</a>: every knob you tuned is a way the result could be fitting the past rather than the future.</p>
<h2>The discipline that helps</h2>
<p>Decide your hypothesis before you look, not after. Keep an honest tally of how many variants you tried, and discount the result accordingly. Hold out data you have never tested against and only look at it once, at the end — the <a href="/tech/walk-forward-validation-explained/">walk-forward</a> pattern is one structured way to do this. And prefer a result that survives a simple, stable rule over one that needs five tuned parameters to shine; the simpler result has fewer places for luck to hide.</p>
<h2>The honest question</h2>
<p>Before believing any backtest, ask: "how many things did I try before I found this?" If the answer is large and untracked, the result is suspect no matter how good the chart looks. The <a href="/tech/backtest-validation-checklist/">validation checklist</a> is where that question gets written down instead of waved away.</p>""",
[],
["why-backtests-overfit-degrees-of-freedom", "walk-forward-validation-explained"]),

("regime-change-or-random-walk-telling-them-apart", "quant", "guide",
"Regime change or random walk? Telling a real shift from ordinary noise",
"Every series has streaks. The hard part is knowing when a bad run is just variance and when the underlying behaviour genuinely changed — and not overreacting to either.",
"""<p>When a strategy that worked stops working, two very different things could be happening: the world changed (a regime shift), or nothing changed and you are watching ordinary randomness (a drawdown inside a still-valid process). Reacting to noise as if it were a regime change is how people abandon good strategies; ignoring a real regime change is how people keep trading dead ones.</p>
<h2>Why it is genuinely hard to tell</h2>
<p>Random series produce streaks that look meaningful. A run of losses feels like a broken strategy the same way a run of wins feels like a discovered edge, and in both cases the feeling is unreliable. The honest position is that a short bad run is usually just variance, and declaring a regime change requires more evidence than discomfort — the same scepticism the <a href="/tech/why-backtests-fail/">why backtests fail</a> piece applies to good-looking results applies here to bad-looking ones.</p>
<h2>What actually helps you decide</h2>
<p>Define what "working" means in advance, with a threshold you set before the drawdown, so you are not negotiating with yourself mid-pain. Look at whether the <em>mechanism</em> still holds — has the reason the strategy worked changed, or only the recent outcome? And judge over enough samples that variance has room to even out; a regime call made on a handful of trades is almost always noise. The <a href="/tech/hundred-experiments-lessons/">lessons from a hundred experiments</a> are mostly lessons in not over-reading short runs.</p>
<h2>The asymmetry to respect</h2>
<p>False alarms and missed shifts are not equally costly. Switching strategies on every wobble guarantees you churn and never let an edge compound; never switching means a genuinely dead strategy bleeds slowly. Most people err toward the first. The discipline is to require real evidence — a mechanism story plus a sustained, pre-defined breach — before concluding the world moved.</p>""",
[],
["why-backtests-fail", "hundred-experiments-lessons"]),

("position-sizing-ruin-the-math-most-backtests-skip", "quant", "guide",
"Position sizing and the risk of ruin: the maths most backtests skip",
"Two strategies with identical signals can have opposite fates based only on how much they bet. Here is why sizing is a survival question, not an optimisation afterthought.",
"""<p>Backtests usually report a return and ignore the question that actually decides whether you live to collect it: how much was at risk on each bet. Position sizing is the part of a strategy that determines whether a normal run of bad luck knocks you out before the edge has time to show. It is a survival question dressed up as an optimisation detail.</p>
<h2>Why a good edge can still ruin you</h2>
<p>Bet too large and even a profitable strategy will, sooner or later, hit a streak of losses deep enough to wipe out the account — the risk of ruin. Bet too small and you leave most of the edge unused. The uncomfortable truth is that the size which maximises long-run growth is not the size that feels comfortable, and the size that feels exciting is usually past the point where ruin becomes a real probability rather than a tail story.</p>
<h2>Sizing is part of the strategy, not a layer on top</h2>
<p>A backtest that omits sizing is testing a signal, not a strategy, because the same signal at different sizes produces entirely different outcomes — including total loss. That means any result reported without a sizing rule is incomplete, and the <a href="/tech/backtest-validation-checklist/">validation checklist</a> should treat "what was the position size and the worst drawdown" as mandatory, not optional. Drawdown, not just return, is the number that tells you whether the sizing was survivable.</p>
<h2>The habits that keep you in the game</h2>
<p>Cap the fraction at risk on any single bet so that no realistic losing streak is fatal. Size down when uncertainty is higher rather than when conviction feels stronger — confidence is not the same as edge. And judge a strategy by its drawdown profile as much as its return, because a slightly lower return you can actually hold through beats a higher one that ruins you. This is the same "model the thing you are skipping" instinct as <a href="/tech/transaction-costs-slippage-backtest-reality/">transaction costs</a>: the omitted detail is usually where the real risk lives.</p>""",
[],
["backtest-validation-checklist", "transaction-costs-slippage-backtest-reality"]),

("reproducible-quant-research-why-it-matters", "quant", "guide",
"Reproducible research: why the result you cannot re-run is the one you cannot trust",
"A finding that depends on your machine, your seed, or your memory of which knobs you turned is not a finding. Here is the lightweight discipline that makes research you can rely on.",
"""<p>A result you cannot reproduce is a result you cannot trust, and in quantitative work reproduction fails constantly for boring reasons: a random seed that was not fixed, data that quietly changed underneath the analysis, a parameter tweaked by hand and never written down. None of these is dramatic; together they make most "it worked once" findings worthless.</p>
<h2>What makes research reproducible</h2>
<p>Three things, none of them heavy. Fix your randomness — set the seed so a stochastic run gives the same answer twice. Pin your inputs — know exactly which data, from when, fed the result, so a refresh does not silently change the conclusion. And record every choice — the parameters, the filters, the exclusions — in code or notes, not in memory. The <a href="/tech/quantlab-project-how-built/">QuantLab build</a> is built around exactly this: experiments you can re-run, not anecdotes you half-remember.</p>
<h2>Why it protects you from yourself</h2>
<p>Reproducibility is not just for other people checking your work; it is the main defence against your own <a href="/tech/data-snooping-when-you-test-too-many-ideas/">data snooping</a>. When every run is recorded and re-runnable, it is obvious how many variants you actually tried and how much the result moved when you nudged a parameter — which is precisely the information that tells you whether an edge is real or a tuned coincidence. The <a href="/tech/overfitting-detection-guide/">overfitting detection guide</a> assumes you can re-run the experiment; reproducibility is what makes that possible.</p>
<h2>The lightweight version that is worth doing</h2>
<p>You do not need elaborate tooling. A single script that goes from raw input to result, a fixed seed, a saved copy of the data snapshot, and a one-line note of what you changed is enough to turn "I think it worked" into "here, run it yourself." That gap — between a memory and a re-runnable artifact — is the whole difference between research and storytelling.</p>""",
[],
["quantlab-project-how-built", "data-snooping-when-you-test-too-many-ideas"]),

]
