# BRYME Money desk — taxonomy for the living-machine hub (batch 1).
# Mirrors fitness_hub_data.py: CATS drive the section shelves and section
# pages; MAP assigns every content page a (section, need); TOOLS are the
# on-device calculators; NEEDS are the job tiles; CADENCE sets per-section
# re-verification windows in days (fees/brokers move fastest).

MONEY_CATS = {
    "start": ("Start here",
              "What trading actually is, which market suits you, the trade types and the market environments — the map before the money."),
    "risk": ("Risk and sizing",
             "Position sizing, pre-trade checklists, leverage and order mechanics — the survival layer that comes before any strategy."),
    "charts": ("Charts and indicators",
               "What indicators measure and what they cannot: RSI, ATR, moving averages — with the marketing claims stripped out."),
    "costs": ("Costs, brokers and platforms",
              "The maths of fees, spreads, swaps and pips, plus how to verify a broker and choose a platform in your own country."),
    "method": ("Method and evidence",
               "How to test an idea honestly before risking money: backtesting discipline and the public QUANTLAB research record."),
}

# slug -> (section, need)
MONEY_MAP = {
    "trading-for-beginners": ("start", "start"),
    "stocks-forex-futures-and-cfds": ("start", "start"),
    "trade-types-explained": ("start", "start"),
    "trading-environments-explained": ("start", "read"),
    "position-sizing-101": ("risk", "size"),
    "trading-risk-checklist": ("risk", "size"),
    "leverage-and-margin-explained": ("risk", "size"),
    "order-types-and-slippage": ("risk", "size"),
    "technical-indicators-explained": ("charts", "read"),
    "rsi-indicator-guide": ("charts", "read"),
    "atr-indicator-guide": ("charts", "read"),
    "moving-averages-sma-vs-ema": ("charts", "read"),
    "trading-fees-explained": ("costs", "vet"),
    "forex-spreads-and-pips": ("costs", "vet"),
    "how-to-check-a-trading-broker": ("costs", "vet"),
    "how-to-choose-a-trading-platform": ("costs", "vet"),
    "backtesting-101": ("method", "test"),
    "quantlab-explained": ("method", "test"),
}

# (slug, title, blurb, related_slug)
MONEY_TOOLS = [
    ("position-size-calculator", "Position size calculator",
     "Account, risk % and stop distance in — lot or unit size out. Any market, any account currency, the working shown.",
     "position-sizing-101"),
    ("expectancy-calculator", "Trading expectancy calculator",
     "Win rate and average win/loss in — expectancy per trade out. See why the ratio matters more than being right.",
     "backtesting-101"),
]

# (key, label, blurb)
MONEY_NEEDS = [
    ("start", "Start from zero",
     "New to markets. What trading is, what the instruments are, and the risk-first way in."),
    ("size", "Size the trade",
     "How big should this position be? Sizing, leverage, checklists and the maths that keeps one loss survivable."),
    ("read", "Read the chart",
     "Indicators and market environments — what the lines actually measure, and the claims they cannot support."),
    ("vet", "Vet the broker",
     "Before you deposit: verifying a broker in your country, and the true cost of spreads, fees and swaps."),
    ("test", "Test the method",
     "An idea is not a strategy until it survives an honest test. Backtesting discipline and public research."),
]

# days between re-verifications per section
MONEY_CADENCE = {"start": 365, "risk": 365, "charts": 365, "costs": 180, "method": 365}
