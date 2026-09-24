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
