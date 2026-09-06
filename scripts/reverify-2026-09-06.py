#!/usr/bin/env python3
"""Re-verify the four records flagged with a lapsed window (2026-09-06).

Each was re-read against the publication's own live guidelines page today.
Two are confirmed closed, one is closed for that call but its rate card has
improved, and one turned out to be MORE open than BRYME was showing.
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
P = ROOT / "content/opportunities.json"
V = "2026-09-06"

data = json.loads(P.read_text(encoding="utf-8"))
recs = {r["slug"]: r for r in data["opportunities"]}
for s in ("efiko", "uncanny-poetry", "griffith-review-bodies", "markaz-review"):
    if s not in recs:
        sys.exit(f"missing record: {s}")

# --- 1. Efiko -------------------------------------------------------------
# "The window for submissions is open for our 8th edition; it closes on
# 30 August." That date has passed, so the call is closed, not on-deadline.
# Rate card re-confirmed exactly, including the lower tier.
r = recs["efiko"]
r["submissionStatus"] = "closed"
r["deadline"] = {"display": "The 8th-edition window closed on 30 August 2026. "
                            "Efiko deletes work sent outside a submission window.",
                 "date": "2026-08-30", "recurring": True}
r["pay"]["conditions"] = ("Official: for contributors with a Nigerian bank account, \u20a630,000 for "
                          "2 or more poems and for prose over 2,500 published words. Accepted "
                          "submissions below those lengths attract \u20a620,000. Re-read on the "
                          "guidelines page 2026-09-06.")

# --- 2. Uncanny (poetry) --------------------------------------------------
# "Uncanny Magazine is OPEN to short story submissions from August 24 to
# September 7. Uncanny Magazine is CLOSED to all other submissions."
# Poetry is therefore closed; the $40 per poem rate is unchanged.
r = recs["uncanny-poetry"]
r["submissionStatus"] = "closed"
r["deadline"] = {"display": "Closed. As of 6 September 2026 Uncanny is open to short fiction only "
                            "(24 August \u2013 7 September); it states it is closed to all other "
                            "submissions, poetry included. Watch their newsletter for the next "
                            "poetry window.",
                 "recurring": True}
r["pay"]["conditions"] = ("Official: \u201cPayment is $40 per poem.\u201d Re-confirmed on the "
                          "submissions page 2026-09-06.")

# --- 3. Griffith Review ---------------------------------------------------
# The Bodies of Work call has closed, but the published rate card is richer
# than BRYME recorded: print prose per word, poetry per poem, online flat.
r = recs["griffith-review-bodies"]
r["submissionStatus"] = "closed"
r["deadline"] = {"display": "This call has closed. Griffith Review 95: Bodies of Work publishes "
                            "February 2027. Griffith Review announces new call-outs through its "
                            "news page and social channels rather than a fixed annual calendar.",
                 "date": "2026-08-23", "recurring": True}
r["pay"]["amountMin"] = 200
r["pay"]["amountMax"] = 500
r["pay"]["display"] = "AUD$0.75/word print \u00b7 AUD$200 poetry \u00b7 AUD$500 online"
r["pay"]["conditions"] = ("Official rate card, re-read 2026-09-06: fiction and non-fiction "
                          "commissioned for the print edition is paid at AUD$0.75 per word; poetry "
                          "at AUD$200 per poem; online pieces at a flat AUD$500. All online content "
                          "sits in front of the paywall.")

# --- 4. The Markaz Review -------------------------------------------------
# The 1 September date belonged to one themed call. The page says plainly:
# "we invite submissions all year-round". This record was UNDER-stating the
# opportunity, not over-stating it.
r = recs["markaz-review"]
r["submissionStatus"] = "rolling"
r["deadline"] = {"display": "Year-round. The Markaz Review runs six bimonthly themed issues plus "
                            "regular weekly pieces, and invites submissions all year round. "
                            "Individual themed calls carry their own deadlines \u2014 the humour "
                            "issue closed 1 September 2026."}
r["pay"]["conditions"] = ("Official: The Markaz Review is a nonprofit and pays all contributors an "
                          "honorarium within 30 days of publication. No figure is published, so "
                          "BRYME states none. Re-read 2026-09-06.")
r["pay"]["timing"] = "Within 30 days of publication"

for s in ("efiko", "uncanny-poetry", "griffith-review-bodies", "markaz-review"):
    recs[s]["lastVerified"] = V

data["updatedAt"] = V
P.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Re-verified 4 records against their live guidelines:")
for s in ("efiko", "uncanny-poetry", "griffith-review-bodies", "markaz-review"):
    print(f"  {s:<26} -> {recs[s]['submissionStatus']}")
