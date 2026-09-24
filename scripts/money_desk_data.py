# BRYME Money desk - phase 1 content (2026-09-24).
# House rules for this desk, mirroring fitness discipline:
#   - General information and education. NEVER financial advice.
#   - No profit promises, no signals, no "guaranteed" anything.
#   - Trading involves substantial risk of loss; say so plainly.
#   - The desk's credibility is the founder's public research:
#     QUANTLAB + mean-reversion-vwap-lab (github.com/ojeology).

MONEY_TAGLINE = "Risk-first trading research, tools and education."

MONEY_EDITION = "SEPTEMBER 2026 \u00b7 THE RISK-FIRST DESK"

RESEARCH_HTML = (
    '<section class="section" id="research"><div class="section-head"><p class="kicker">Open research</p>'
    '<h2>Built on research we publish</h2></div><div class="prose">'
    "<p>Most trading content on the internet is written by people who have never tested "
    "anything. This desk is the opposite: the systems we discuss come from the founder's "
    "open-source quantitative research, published in full on GitHub.</p>"
    '<ul class="list">'
    '<li><a href="https://github.com/ojeology/QUANTLAB" rel="noopener">QUANTLAB</a> '
    "\u2014 a systematic research framework for discovering and stress-testing trading "
    "strategies: the engine behind everything this desk publishes.</li>"
    '<li><a href="https://github.com/ojeology/mean-reversion-vwap-lab" rel="noopener">Mean-Reversion VWAP Lab</a> '
    "\u2014 a VWAP \u00b12\u03c3 mean-reversion crypto strategy developed across fourteen days "
    "of testing, with the methodology left open for anyone to check or reproduce.</li>"
    "</ul>"
    "<p>Reading the research first is the honest way to read anything else on this desk: "
    "you can see exactly how the conclusions were reached.</p>"
    "</div></section>"
)

DISCLAIMER_HTML = (
    '<section class="section"><div class="prose">'
    '<p style="background:rgba(127,127,127,.08);border:1px solid var(--line-strong);padding:13px 15px">'
    "<b>General information, not financial advice.</b> Everything on BRYME Money is "
    "educational. Trading forex, crypto and derivatives involves substantial risk of loss "
    "and is not suitable for everyone. Past performance \u2014 including any published "
    "research \u2014 does not guarantee future results. Never trade money you cannot "
    "afford to lose.</p>"
    "</div></section>"
)

HUB_BODY = (
    '<div class="wrap"><section class="cover"><p class="kicker">BRYME Money</p>'
    "<h1 class=\"cover-title\">Risk comes first. Everything else is arithmetic.</h1>"
    "<p class=\"cover-dek\">Trading tools, education and open research \u2014 built by people "
    "who test systems in public, for readers who want the discipline without the drama.</p></section>"
    '<section class="section"><div class="prose">'
    "<p>BRYME Money exists because most trading education skips the only variable a "
    "trader actually controls: how much is at risk on the next trade. Strategy gets the "
    "headlines; position sizing decides who survives long enough to have a strategy. "
    "So this desk starts where survival starts.</p>"
    '<ul class="list">'
    '<li><a href="/money/position-size-calculator/"><b>The position size calculator</b></a> '
    "\u2014 account balance, risk percent, entry and stop in; exact position size out. "
    "Works for forex lots and any market in units.</li>"
    '<li><a href="/money/position-sizing-101/"><b>Position sizing, the 1% rule, explained</b></a> '
    "\u2014 the formula behind the calculator, worked examples in forex and crypto, and "
    "why risking 1\u20132% per trade is the whole game.</li>"
    '<li><a href="/money/quantlab-explained/"><b>QUANTLAB, explained</b></a> '
    "\u2014 every step of the open trading-research project: 95 runs, 34 blind tests and one "
    "honest retraction.</li>"
    '<li><a href="/money/backtesting-101/"><b>How to test a strategy honestly</b></a> '
    "\u2014 the seven ways a backtest lies, and the discipline that catches each one.</li>"
    '<li><a href="/money/expectancy-calculator/"><b>The expectancy calculator</b></a> '
    "\u2014 win rate and risk-reward in; edge per trade, breakeven win rate and dollars out.</li>"
    "</ul>"
    "<p>New tools and research notes are added as they are finished \u2014 never on a "
    "schedule, always with the working open for inspection.</p>"
    "</div></section>"
    + RESEARCH_HTML
    + DISCLAIMER_HTML
    + "</div>"
)

CALC_PAGE = {
    "route": "/position-size-calculator/",
    "title": "Position Size Calculator - forex lots & any-market units | BRYME Money",
    "desc": "Free position size calculator: balance, risk %, entry and stop in - exact lot or unit size out. Forex pip mode and any-market mode. Educational tool, not advice.",
    "h1": "Position size calculator",
    "dek": "The one calculation that decides whether a trading account survives: how big should this trade be?",
}

CALC_BODY_TOP = (
    '<div class="wrap"><section class="cover"><p class="kicker">BRYME Money \u00b7 Tool</p>'
    "<h1 class=\"cover-title\">Position size calculator</h1>"
    "<p class=\"cover-dek\">Balance, risk percent, entry and stop in \u2014 exact position size out. "
    "For forex (in lots) and any market (in units).</p></section>"
    '<section class="section"><div class="prose">'
    "<p>Choose a mode, fill in four numbers, read the answer. The maths and its "
    "reasoning are explained in <a href=\"/money/position-sizing-101/\">position sizing, "
    "explained</a>; nothing is stored or sent anywhere \u2014 the calculation runs entirely "
    "in your browser.</p>"
    "</div></section>"
    '<section class="section"><div class="prose money-calc">'
    '<style>'
    '.money-calc .fld{display:flex;flex-direction:column;gap:6px;margin:14px 0}'
    '.money-calc label{font-weight:600;font-size:14px}'
    '.money-calc input,.money-calc select{padding:10px 12px;border:1px solid var(--line-strong);border-radius:8px;font-size:16px;max-width:340px;background:var(--sheet);color:var(--ink)}'
    '.money-calc fieldset{border:1px solid var(--line-strong);border-radius:10px;padding:6px 16px 16px;max-width:520px}'
    '.money-calc legend{font-weight:700;padding:0 8px}'
    '.money-calc .out{background:rgba(127,127,127,.08);border:1px solid var(--line-strong);border-radius:10px;padding:14px 16px;max-width:520px;margin:16px 0}'
    '.money-calc .out b{font-size:18px}'
    '.money-calc .warn{color:#a33;font-weight:600}'
    '</style>'
    '<fieldset><legend>Trade details</legend>'
    '<div class="fld"><label for="mc-mode">Market type</label>'
    '<select id="mc-mode"><option value="fx">Forex pair (answer in lots)</option>'
    '<option value="units">Any market \u2014 crypto, indices, stocks (answer in units)</option></select></div>'
    '<div class="fld" id="mc-pair-row"><label for="mc-pair">Forex pair</label>'
    '<select id="mc-pair">'
    '<option value="0.0001" data-name="EUR/USD">EUR/USD</option>'
    '<option value="0.0001" data-name="GBP/USD">GBP/USD</option>'
    '<option value="0.0001" data-name="AUD/USD">AUD/USD</option>'
    '<option value="0.0001" data-name="NZD/USD">NZD/USD</option>'
    '<option value="0.0001" data-name="EUR/GBP">EUR/GBP</option>'
    '<option value="0.0001" data-name="USD/CAD">USD/CAD</option>'
    '<option value="0.0001" data-name="USD/CHF">USD/CHF</option>'
    '<option value="0.01" data-name="USD/JPY">USD/JPY</option>'
    '<option value="0.01" data-name="EUR/JPY">EUR/JPY</option>'
    '<option value="0.01" data-name="GBP/JPY">GBP/JPY</option>'
    '</select></div>'
    '<div class="fld"><label for="mc-balance">Account balance</label>'
    '<input id="mc-balance" type="number" min="0" step="any" placeholder="e.g. 5000"></div>'
    '<div class="fld"><label for="mc-risk">Risk per trade (% of balance)</label>'
    '<input id="mc-risk" type="number" min="0" max="100" step="any" value="1"></div>'
    '<div class="fld"><label for="mc-entry">Entry price</label>'
    '<input id="mc-entry" type="number" min="0" step="any" placeholder="e.g. 1.0850"></div>'
    '<div class="fld"><label for="mc-stop">Stop-loss price</label>'
    '<input id="mc-stop" type="number" min="0" step="any" placeholder="e.g. 1.0825"></div>'
    '</fieldset>'
    '<div class="out" id="mc-out" aria-live="polite">Fill in the fields to see your position size.</div>'
    '<p id="mc-warn" class="warn" aria-live="polite"></p>'
    "</div></section>"
)

CALC_BODY_TAIL = (
    '<section class="section"><div class="prose">'
    "<h2>How the calculation works</h2>"
    "<p>The calculator answers one question: <i>if my stop is hit, do I lose exactly the "
    "amount I chose to risk?</i></p>"
    '<ul class="list">'
    "<li><b>Any-market mode:</b> units = money at risk \u00f7 (entry \u2212 stop). A $0.40 "
    "stop distance risking $100 means 250 units.</li>"
    "<li><b>Forex mode:</b> one standard lot is 100,000 units of the base currency, and "
    "a pip is 0.0001 (0.01 on JPY pairs). Lots = money at risk \u00f7 (stop in pips \u00d7 "
    "pip value per lot).</li></ul>"
    "<p>Pip values are shown in the pair's <i>quote</i> currency. If your account is in a "
    "different currency the exact figure shifts with the exchange rate \u2014 the position "
    "size moves the same direction, so treat the answer as the honest starting point and "
    "round <i>down</i>.</p>"
    "<p>Read the full reasoning in <a href=\"/money/position-sizing-101/\">position "
    "sizing, explained</a>.</p>"
    "</div></section>"
    + DISCLAIMER_HTML
    + "</div>"
)

SIZING_101 = {
    "route": "/position-sizing-101/",
    "title": "Position sizing explained - the 1% rule that keeps traders alive | BRYME Money",
    "desc": "Why position sizing - not strategy - decides which trading accounts survive. The 1-2% rule, the formula, worked forex and crypto examples. General information, not advice.",
    "h1": "Position sizing, explained honestly",
    "dek": "The 1-2% rule is the least glamorous idea in trading and the only one that reliably separates accounts that survive from accounts that don't.",
}

SIZING_BODY = (
    '<div class="wrap"><section class="cover"><p class="kicker">BRYME Money \u00b7 Education</p>'
    "<h1 class=\"cover-title\">Position sizing, explained honestly</h1>"
    "<p class=\"cover-dek\">Nobody blows an account with one bad idea. They blow it with "
    "one badly sized trade \u2014 repeated.</p></section>"
    '<section class="section"><div class="prose">'
    "<p>Ask a losing trader what went wrong and you will hear about strategy: the wrong "
    "indicator, the fake breakout, the news. Ask a surviving trader and you will hear a "
    "number: <i>how much</i> they were willing to lose on any single trade. That number "
    "is position sizing, and it is the only input in trading you fully control.</p>"
    "<p>You cannot control whether the next trade wins. You cannot control the spread, "
    "the slippage or the news. You control exactly one thing \u2014 how much is at risk "
    "before you click the button. Get that one thing right and losing streaks become "
    "survivable. Get it wrong and no strategy on earth saves the account.</p>"
    "<h2>The 1\u20132% rule</h2>"
    "<p>The working convention among professional risk managers is simple: <b>never risk "
    "more than 1\u20132% of the account on a single trade</b>. Not 1\u20132% of the "
    "account <i>in</i> the trade \u2014 1\u20132% of the account <i>lost if the stop is "
    "hit</i>. On a $5,000 account, one percent is $50. Every position you take is built "
    "backwards from that fifty dollars, never forwards from \u201chow much can I "
    "buy?\u201d.</p>"
    "<p>Why so small? Because losing streaks are not a possibility, they are a "
    "statistical certainty. A strategy with a genuine 50% win rate will still hand you "
    "eight losses in a row sooner or later \u2014 the streak is inside the maths, not a "
    "sign the strategy broke. At 1% risk, eight straight losses is a 7.7% drawdown: "
    "painful, survivable. At 20% risk it is an 83% drawdown, which needs a 578% gain "
    "just to get back to even. That is not a recovery plan; it is an obituary.</p>"
    "<h2>The formula</h2>"
    "<p>Position size is one division:</p>"
    '<p style="background:rgba(127,127,127,.08);border:1px solid var(--line-strong);padding:13px 15px">'
    "<b>Position size = (account \u00d7 risk %) \u00f7 stop distance</b></p>"
    "<p>Everything else is unit conversion \u2014 which is what the "
    "<a href=\"/money/position-size-calculator/\">position size calculator</a> is for. "
    "The work worth doing by hand is deciding the two honest inputs: the account figure "
    "(what you actually have, not what you wish you had) and the stop (where the trade "
    "idea is <i>objectively wrong</i>, not where it \u201cfeels safe\u201d).</p>"
    "<h2>Worked example \u2014 forex</h2>"
    "<p>Account: $5,000. Risk: 1% = $50. Trade: long EUR/USD at 1.0850, stop at 1.0825 "
    "\u2014 a 25-pip stop. A standard lot (100,000 units) makes each pip worth $10 in "
    "quote-currency terms, so 25 pips risks $250 per standard lot. $50 \u00f7 $250 = "
    "<b>0.2 lots</b>. Take the trade at 0.2 lots and a full stop-out costs exactly the "
    "fifty dollars you chose \u2014 nothing more.</p>"
    "<h2>Worked example \u2014 crypto</h2>"
    "<p>Account: $5,000. Risk: 1% = $50. Trade: long BTC at 60,000 with the idea invalid "
    "below 58,800 \u2014 a $1,200 stop distance. $50 \u00f7 $1,200 = <b>0.0417 BTC</b> "
    "(about $2,500 of exposure). The same calculation, run in reverse, is why leveraged "
    "\u201cI\u2019ll just size up\u201d trades end accounts: the position grew, the stop "
    "distance did not, and the loss per trade quietly tripled.</p>"
    "<h2>Where traders cheat themselves</h2>"
    '<ul class="list">'
    "<li><b>Widening the stop to keep the size.</b> If the stop moves to fit a bigger "
    "position, the trade idea changed and the sizing maths is now theatre.</li>"
    "<li><b>Risking \u201cjust this once\u201d more.</b> The 1% rule only compounds if it "
    "is actually a rule. The account does not care about your conviction.</li>"
    "<li><b>Counting pips, not percent.</b> Fifty pips means nothing without position "
    "size attached; the only universal unit is the percent of the account at risk.</li>"
    "<li><b>Forgetting leverage is sizing, not capital.</b> Leverage multiplies exposure, "
    "never the balance. The risk maths above is identical at 1:30 or 1:500 \u2014 only "
    "the margin required changes.</li>"
    "</ul>"
    "<h2>The part research can and cannot do</h2>"
    "<p>Position sizing cannot make a losing strategy win \u2014 it makes a losing "
    "strategy <i>affordable to keep testing</i>, which is how every strategy in our "
    "<a href=\"/#research\">open research</a> survived long enough to be judged. That is "
    "the honest scope of the tool: sizing keeps you in the game; the edge has to come "
    "from tested method. Our "
    '<a href="https://github.com/ojeology/QUANTLAB" rel="noopener">QUANTLAB</a> framework '
    "and the "
    '<a href="https://github.com/ojeology/mean-reversion-vwap-lab" rel="noopener">VWAP '
    "mean-reversion lab</a> exist because that second part deserves the same discipline "
    "as the first.</p>"
    "</div></section>"
    + DISCLAIMER_HTML
    + "</div>"
)

# ---- Money desk phase 2 (2026-09-24): QUANTLAB explained + backtesting 101 + expectancy tool ----
# Every factual claim in these pages is drawn from the public research repos:
#   github.com/ojeology/QUANTLAB (README, 2026-09 state) and
#   github.com/ojeology/mean-reversion-vwap-lab (README, E1-E14 journal).
# House rules unchanged: general information, never advice; no profit promises;
# research numbers are presented as the project's own logged results, with caveats.

QL_BODY = (
    '<div class="wrap"><section class="cover"><p class="kicker">BRYME Money \u00b7 Open research</p>'
    "<h1 class=\"cover-title\">QUANTLAB, explained: every step of a real trading research project</h1>"
    "<p class=\"cover-dek\">95 crypto runs, 9 forex runs, 34 blind tests, one strategy freeze and one "
    "self-audit that retracted its own best result. This is what honest strategy research looks like, "
    "step by step.</p></section>"
    '<section class="section"><div class="prose">'
    "<p>Most trading content shows you a winning backtest and asks for your email. "
    '<a href="https://github.com/ojeology/QUANTLAB" rel="noopener">QUANTLAB</a> is the opposite: a public '
    "research laboratory where every experiment \u2014 including the embarrassing ones \u2014 is numbered, "
    "logged and open for inspection. This page walks through exactly how the project works, in order, "
    "using nothing but its own published record. It is general information about a research "
    "<i>process</i>, not advice to trade anything.</p>"
    "<h2>Step 0 \u2014 the premise: a lab, not a strategy dump</h2>"
    "<p>QUANTLAB's founding rule is that a failed experiment is still a finding. Across its two research "
    "arcs it logged roughly <b>95 numbered crypto iterations (R001\u2013R095)</b> over twelve days in "
    "July\u2013August 2026, <b>9 forex iterations (F001\u2013F009)</b>, and then \u2014 after a deliberate "
    "<b>strategy freeze</b> on 9 August 2026 \u2014 a <b>blind out-of-sample campaign of 34 tests "
    "(T1\u2013T34)</b> on a separate branch. Nothing was quietly deleted. The journal, the scripts, the "
    "reports and the charts are all in the repository.</p>"
    "<h2>Step 1 \u2014 every run asks one falsifiable question</h2>"
    "<p>Each numbered run is built around a single claim that data can prove wrong: <i>does strategy X, "
    "on market Y, survive costs on data it was not designed on?</i> If the answer is no, the run is "
    "written down as a no. There is no third outcome where a losing idea gets a softer name.</p>"
    "<h2>Step 2 \u2014 the data rules</h2>"
    "<p>The crypto research worked on hourly candles across a broad symbol universe, with 2023\u20132026 "
    "split into <b>per-year holdouts</b> \u2014 years kept untouched until a verdict, so no result could "
    "quietly lean on the data it would later be judged by. Forex ran on 1-hour spot. Five-minute crypto "
    "was tested too \u2014 and it is one of the project's proudest results that it proved <b>no "
    "cost-surviving edge exists there, seven independent ways (runs R089\u2013R095)</b>.</p>"
    "<h2>Step 3 \u2014 the validation battery every idea must survive</h2>"
    '<ul class="list">'
    "<li><b>Walk-forward optimisation</b> \u2014 train only on the past, never on the future.</li>"
    "<li><b>Out-of-sample holdouts</b> \u2014 a period kept untouched until the verdict.</li>"
    "<li><b>Cost gates</b> \u2014 0.05% per side on crypto, retail spread and swap on forex. An edge "
    "that dies at cost is not an edge.</li>"
    "<li><b>A causal (lookahead) audit</b> \u2014 made mandatory after run R090's result was retracted "
    "as a proxy artefact.</li>"
    "<li><b>Bootstrap confidence intervals</b> on profit-factor estimates, <b>Monte Carlo</b> "
    "simulation for P(profit) and drawdown distributions, <b>leave-one-out</b> checks across symbols "
    "and folds, <b>monthly stability</b> and <b>parameter robustness grids</b>.</li></ul>"
    "<p>Each verdict uses a fixed vocabulary so results cannot be talked up: <b>VALIDATED</b>, "
    "<b>WATCHLIST</b> (promising, sample too thin), <b>REJECT</b>, <b>RETRACTED</b>, <b>OVERFIT</b>.</p>"
    "<h2>Step 4 \u2014 what the hunt actually found</h2>"
    "<p>The honest map, from the log: five-minute crypto \u2014 no edge; Deriv synthetic indices \u2014 "
    "indistinguishable from a random walk in that sandbox; forex 1-hour \u2014 the crypto trend pipeline "
    "transferred at roughly break-even (profit factor \u22481.10, no real edge); most discovered edges "
    "proved <b>universe-specific</b>, failing on symbols they had never seen. What survived: a "
    "<b>1-hour crypto mean-reversion family</b> \u2014 an SVM-filtered setup with a volatility-ceiling "
    "regime gate \u2014 plus a VWAP-band lab explored separately.</p>"
    "<h2>Step 5 \u2014 the freeze, and why freezing was the point</h2>"
    "<p>On 9 August 2026 the project froze its best configuration \u2014 and then did the thing almost "
    "nobody does: it re-tested the frozen champion <b>blind</b>, on untouched per-year data, with "
    "costs. The frozen config <b>failed</b>. Its backtest profit factor of 1.94 collapsed to about "
    "1.25 after costs on the blind re-test, and one static variant lost outright. The freeze did its "
    "job: it stopped a fragile result from being trusted.</p>"
    "<h2>Step 6 \u2014 the audit that retracted its own best number</h2>"
    "<p>In September 2026 a test (T34) auditing whether the results were implementable found something "
    "uncomfortable: the trend strategy's filter had been reading data from the <i>exit</i> bar of each "
    "trade \u2014 information that does not exist at entry. That is textbook lookahead bias. Re-anchored "
    "honestly to the entry bar, the trend edge fell to roughly break-even (profit factor \u22481.03). "
    "The project's response was to publish the retraction, mark the old claims superseded, and make "
    "causal audits mandatory for every future run. The framework caught its own error \u2014 which is "
    "the entire point of having a framework.</p>"
    "<h2>Step 7 \u2014 where the research stands now</h2>"
    "<p>As of its September 2026 log, the surviving verdict is deliberately modest: the "
    "<b>mean-reversion leg only</b>, at a 2R-target / 1R-stop exit and 1% risk per trade, was the "
    "configuration the small-account study could defend \u2014 the project's own simulation logged "
    "roughly +104% on a $100 account across 2024 to mid-2026 with a realised max drawdown near "
    "<b>\u221237%</b>, while risking 2% per trade produced simulated drawdowns of \u221250% to \u221280%. "
    "Note what those numbers include: a losing year (2024) inside the winning period. And note the "
    "protocol attached: the study re-runs its full validation battery on fresh data at year-end and "
    "<b>green-lights 2027 only if the post-cost profit factor holds at roughly 1.2 or better</b>. "
    "These are the project's logged research results on historical data \u2014 not a promise, not a "
    "forecast, and not advice.</p>"
    "<h2>What any trader can steal from this</h2>"
    '<ul class="list">'
    "<li>Write the question down before the test; let the data answer, not the hope.</li>"
    "<li>Costs are part of the strategy. So is the year the market hated you.</li>"
    "<li>A retraction is a strength, not a scandal \u2014 the alternative is trading a bug.</li>"
    "<li>If you cannot audit it, you cannot trust it. That is why the lab is public.</li></ul>"
    "<p>Do the maths your own research deserves: the "
    "<a href=\"/money/expectancy-calculator/\">expectancy calculator</a> and the "
    "<a href=\"/money/position-size-calculator/\">position size calculator</a> cover the two numbers "
    "every system lives or dies by, and <a href=\"/money/backtesting-101/\">backtesting 101</a> "
    "explains the testing logic in full.</p>"
    "</div></section>"
    + DISCLAIMER_HTML
    + "</div>"
)

QL_PAGE = {
    "route": "/quantlab-explained/",
    "title": "QUANTLAB explained - real trading research, step by step | BRYME Money",
    "desc": "Inside QUANTLAB: 95 crypto runs, 34 blind tests, one honest retraction. Every step of a systematic trading research project, explained from its public record. Not advice.",
    "body": QL_BODY,
}

BT_BODY = (
    '<div class="wrap"><section class="cover"><p class="kicker">BRYME Money \u00b7 Education</p>'
    "<h1 class=\"cover-title\">How to test a trading strategy honestly</h1>"
    "<p class=\"cover-dek\">Backtesting 101: the seven ways a backtest lies, and the discipline that "
    "catches every one of them \u2014 with real examples from a public research lab.</p></section>"
    '<section class="section"><div class="prose">'
    "<p>A backtest is a story a strategy tells about the past. Told carelessly, it is a story "
    "designed to flatter. The discipline of honest testing is mostly a list of ways to catch "
    "yourself flattering yourself. Every example below comes from "
    '<a href="https://github.com/ojeology/QUANTLAB" rel="noopener">QUANTLAB</a> and the '
    '<a href="https://github.com/ojeology/mean-reversion-vwap-lab" rel="noopener">VWAP mean-reversion '
    "lab</a> \u2014 public projects whose failed runs are documented alongside the good ones.</p>"
    "<h2>1. In-sample flattery</h2>"
    "<p>Test a strategy on the data you designed it on and it will look brilliant \u2014 it has, in "
    "effect, memorised the answers. The VWAP lab's final experiment made the gap explicit: about "
    "<b>+$262 profit in-sample</b> over its test month versus about <b>+$18 out-of-sample</b>, with a "
    "win rate of 54% in-sample falling to 44\u201347% outside it. Same strategy, same rules \u2014 the "
    "only thing that changed was whether the data had been seen before. Any backtest that does not "
    "show you this split is hiding its most important number.</p>"
    "<h2>2. The future leaking in</h2>"
    "<p>Lookahead bias means letting the strategy read information that would not exist yet in live "
    "trading. It is rarely deliberate and almost always fatal. QUANTLAB's September 2026 audit is the "
    "textbook case: its best trend result was gated by a filter reading the <i>exit</i> bar of each "
    "trade \u2014 future information \u2014 and re-anchoring the filter to the true entry bar erased the "
    "edge (profit factor \u22481.03, roughly break-even). The fix is a standing rule: audit every "
    "feature for when it was actually knowable.</p>"
    "<h2>3. Costs that only exist in theory</h2>"
    "<p>Fees, spread and slippage do not care about your equity curve. QUANTLAB gates every result at "
    "0.05% per side on crypto and retail spread plus swap on forex \u2014 and its five-minute crypto "
    "research concluded <b>no cost-surviving edge existed at all, proven seven independent ways</b>. "
    "An edge that cannot pay its own transaction costs is not an edge; it is a donation schedule.</p>"
    "<h2>4. The universe you quietly chose</h2>"
    "<p>Results depend on which symbols you test \u2014 and testing only the ones that worked is "
    "survivorship bias. Two lessons from the log: edges that worked on the discovery universe failed "
    "on unseen symbols, and a drawdown measured on 30 favourable symbols read \u22129.4% while the "
    "full 50-symbol universe \u2014 including a hostile 2024 \u2014 read <b>\u221228.2%</b> on the same "
    "strategy. Same rules, different honesty.</p>"
    "<h2>5. One lucky backtest</h2>"
    "<p>A single profitable run proves almost nothing. Robustness comes from multiple independent "
    "checks: walk-forward optimisation (train on the past only), bootstrap confidence intervals on "
    "the profit factor, Monte Carlo simulation for the range of drawdowns, leave-one-out tests "
    "across symbols and time folds, monthly stability counts. If the result only survives one "
    "configuration of one test on one universe, it is not a result \u2014 it is a coincidence with "
    "a chart.</p>"
    "<h2>6. Drawdowns you have not felt yet</h2>"
    "<p>Paper drawdowns are abstract; lived drawdowns end accounts. The same research that logged a "
    "winning period also logged that risking 2% per trade instead of 1% turned simulated drawdowns "
    "from painful (\u2248\u221228%) to account-ending (\u221250% to \u221280%). Sizing, not strategy, "
    "decides whether a normal losing streak is survivable \u2014 which is what the "
    "<a href=\"/money/position-size-calculator/\">position size calculator</a> and "
    "<a href=\"/money/position-sizing-101/\">the 1% rule</a> are for.</p>"
    "<h2>7. Words that mean nothing</h2>"
    "<p>'Works great', 'proven system', '9/10 traders' \u2014 vague praise is how overfit results "
    "travel. QUANTLAB forces every verdict through a fixed vocabulary: <b>VALIDATED</b>, "
    "<b>WATCHLIST</b> (promising, sample too thin), <b>REJECT</b>, <b>RETRACTED</b>, <b>OVERFIT</b>. "
    "Borrow the habit: give your own results names that cannot be negotiated with.</p>"
    "<h2>The honest-testing checklist</h2>"
    '<ul class="list">'
    "<li>Split your data: design in-sample, judge out-of-sample, keep at least one period fully "
    "untouched until the end.</li>"
    "<li>Audit every input for lookahead \u2014 know the timestamp of every number the strategy reads.</li>"
    "<li>Apply real costs, then re-check whether the edge still exists.</li>"
    "<li>Test on symbols and years the design never saw.</li>"
    "<li>Run the robustness battery: walk-forward, bootstrap, Monte Carlo, leave-one-out.</li>"
    "<li>Report the drawdown and the losing year, not just the return.</li>"
    "<li>Log failures with the same care as wins \u2014 they are the tuition.</li></ul>"
    "<p>When you have an honest edge estimate, the <a href=\"/money/expectancy-calculator/\">expectancy "
    "calculator</a> turns it into the only two numbers that matter per trade, and "
    "<a href=\"/money/quantlab-explained/\">QUANTLAB, explained</a> shows the whole discipline applied "
    "end to end.</p>"
    "</div></section>"
    + DISCLAIMER_HTML
    + "</div>"
)

BT_PAGE = {
    "route": "/backtesting-101/",
    "title": "Backtesting 101 - how to test a trading strategy honestly | BRYME Money",
    "desc": "The seven ways a backtest lies - in-sample flattery, lookahead, costs, survivorship - and the discipline that catches them, with real public-research examples. Not advice.",
    "body": BT_BODY,
}

EXP_BODY = (
    '<div class="wrap"><section class="cover"><p class="kicker">BRYME Money \u00b7 Tool</p>'
    "<h1 class=\"cover-title\">Trading expectancy calculator</h1>"
    "<p class=\"cover-dek\">Win rate and risk-reward in \u2014 the only two numbers your system is "
    "built on, out.</p></section>"
    '<section class="section"><div class="prose">'
    "<p>Expectancy answers one question: <i>on average, what does one trade earn or lose?</i> Enter "
    "your win rate and your average winner and loser measured in R \u2014 where 1R is the amount "
    "risked. The calculation runs entirely in your browser; nothing is stored or sent anywhere.</p>"
    "</div></section>"
    '<section class="section"><div class="prose money-calc">'
    '<fieldset><legend>System stats</legend>'
    '<div class="fld"><label for="mcx-win">Win rate (%)</label>'
    '<input id="mcx-win" type="number" min="0" max="100" step="any" placeholder="e.g. 45"></div>'
    '<div class="fld"><label for="mcx-winr">Average winner (in R)</label>'
    '<input id="mcx-winr" type="number" min="0" step="any" value="2"></div>'
    '<div class="fld"><label for="mcx-losr">Average loser (in R)</label>'
    '<input id="mcx-losr" type="number" min="0" step="any" value="1"></div>'
    '<div class="fld"><label for="mcx-bal">Account balance (optional, for $)</label>'
    '<input id="mcx-bal" type="number" min="0" step="any" placeholder="e.g. 5000"></div>'
    '<div class="fld"><label for="mcx-risk">Risk per trade (% \u2014 optional, for $)</label>'
    '<input id="mcx-risk" type="number" min="0" max="100" step="any" value="1"></div>'
    '</fieldset>'
    '<div class="out" id="mcx-out" aria-live="polite">Fill in a win rate and reward numbers to see expectancy.</div>'
    '<p id="mcx-warn" class="warn" aria-live="polite"></p>'
    "</div></section>"
    '<section class="section"><div class="prose">'
    "<h2>How to read the result</h2>"
    '<ul class="list">'
    "<li><b>Expectancy per trade</b> is (win% \u00d7 avg win) \u2212 (loss% \u00d7 avg loser), in R. "
    "Positive means the system makes money <i>per trade on average</i>; negative means it bleeds, no "
    "matter how good it feels.</li>"
    "<li><b>Breakeven win rate</b> is loser \u00f7 (winner + loser). At a 2R winner the system only "
    "needs ~33% winners to break even; at a 1R winner it needs over 50%.</li>"
    "<li><b>Dollars per trade</b> apply expectancy to your risk amount: balance \u00d7 risk% = 1R.</li></ul>"
    "<p>The catch, and it is the whole game: these numbers are only as honest as the testing behind "
    "them. A win rate measured in-sample flatters; one measured out-of-sample tells the truth \u2014 "
    "see <a href=\"/money/backtesting-101/\">backtesting 101</a> for how to get numbers you can "
    "actually trust, and <a href=\"/money/position-size-calculator/\">the position size calculator</a> "
    "to convert risk into lots or units. Research context: "
    "<a href=\"/money/quantlab-explained/\">QUANTLAB, explained</a>.</p>"
    "</div></section>"
    + DISCLAIMER_HTML
    + '<script src="/assets/money-expectancy.js" defer></script></div>'
)

EXP_PAGE = {
    "route": "/expectancy-calculator/",
    "title": "Trading expectancy calculator - win rate & risk-reward | BRYME Money",
    "desc": "Free expectancy calculator: win rate and R-multiples in - expectancy per trade, breakeven win rate and dollar expectancy out. Runs in your browser. Educational, not advice.",
    "body": EXP_BODY,
}
