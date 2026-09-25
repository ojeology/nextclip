/*!
 * rent-or-buy-tool.js — BRYME Home & DIY decision tool (§16).
 * Mounts on #rent-or-buy-tool. Six questions -> an honest call for the
 * reader's MARKET (UK/US/CA/AU-NZ/EU/Nigeria/other): mechanics named,
 * no price predictions, no invented figures. On-device only: no storage,
 * no network calls. External file: site CSP is script-src 'self' https:.
 */
(function () {
  "use strict";
  var mount = document.getElementById("rent-or-buy-tool");
  if (!mount) return;

  var QUESTIONS = [
    {
      key: "market",
      q: "Where is the home — which market's rules apply?",
      opts: [
        { id: "uk", label: "United Kingdom", note: "Stamp duty, tenure, first-time relief" },
        { id: "us", label: "United States", note: "Closing costs, property tax, deductions" },
        { id: "ca", label: "Canada", note: "Land transfer tax, FHSA, mortgage insurance" },
        { id: "anz", label: "Australia or New Zealand", note: "State-by-state duty and grants" },
        { id: "eu", label: "Europe (EU/EEA)", note: "Notary fees, transfer taxes by country" },
        { id: "ng", label: "Nigeria", note: "Upfront-rent norms, title verification" },
        { id: "other", label: "Somewhere else", note: "The universal framework applies" }
      ]
    },
    {
      key: "horizon",
      q: "Realistically, how long will you stay in this city?",
      opts: [
        { id: "lt2", label: "Under 2 years", note: "Work or life is likely to move you" },
        { id: "y2_5", label: "2–5 years", note: "" },
        { id: "y5_10", label: "5–10 years", note: "" },
        { id: "y10p", label: "10+ years — roots", note: "This is the long haul" }
      ]
    },
    {
      key: "deposit",
      q: "What deposit/down-payment savings do you actually have (after your emergency fund)?",
      opts: [
        { id: "none", label: "None yet", note: "The emergency fund comes first — that order matters" },
        { id: "small", label: "A small deposit", note: "Scheme territory in several markets" },
        { id: "standard", label: "A standard deposit (~10–20%)", note: "" },
        { id: "large", label: "20%+ comfortably", note: "" }
      ]
    },
    {
      key: "income",
      q: "How stable is the income that would carry it?",
      opts: [
        { id: "stable", label: "Stable salary", note: "" },
        { id: "variable", label: "Variable — freelance, business, commissions", note: "" },
        { id: "growing", label: "Early career — smaller now, growing", note: "" }
      ]
    },
    {
      key: "rentcost",
      q: "Locally, what does renting a similar place do against the monthly cost of owning?",
      opts: [
        { id: "rentcheap", label: "Rent is clearly cheaper", note: "" },
        { id: "rentsimilar", label: "Roughly the same", note: "" },
        { id: "renthigh", label: "Rent is high and climbing", note: "" },
        { id: "unknown", label: "Haven't done that maths yet", note: "The tool will tell you to do it" }
      ]
    },
    {
      key: "priority",
      q: "What matters most to you here?",
      opts: [
        { id: "flexibility", label: "Freedom to move", note: "" },
        { id: "equity", label: "Building equity instead of a landlord's", note: "" },
        { id: "predictable", label: "Predictable monthly costs", note: "" },
        { id: "control", label: "A place that's genuinely mine", note: "Paint, pets, renovations — the rules are yours" }
      ]
    }
  ];

  var OUTCOMES = {
    "rent-flexibility": {
      name: "Rent — without the guilt",
      cost: "Renting under ~2–5 years is not 'throwing money away' — it's buying flexibility, and the entry costs you skip (taxes, fees, agent costs) are the receipt.",
      links: [
        ["/home/rent-vs-buy-explained/", "Rent vs buy, explained"],
        ["/home/renter-vs-owner-repairs/", "Which repairs are whose"],
        ["/home/renter-friendly-fixes/", "Renter-friendly fixes"]
      ]
    },
    "rent-save": {
      name: "Rent deliberately — and bank the difference",
      cost: "The winning move at your horizon: rent with intent, automate the difference into savings, and check first-home schemes NOW even if you buy years from now.",
      links: [
        ["/home/rent-vs-buy-explained/", "Rent vs buy, explained"],
        ["/home/mortgage-payments-explained/", "What mortgage payments really are"],
        ["/home/emergency-repair-fund/", "The repair fund (owners need it too)"]
      ]
    },
    "buy-schemes": {
      name: "Buying — with scheme support, checked first",
      cost: "A small deposit isn't a verdict; several markets subsidise the entry. Scheme thresholds change — the official calculator for your jurisdiction is the authority, not any website.",
      links: [
        ["/home/mortgage-payments-explained/", "What mortgage payments really are"],
        ["/home/rent-vs-buy-explained/", "Rent vs buy, explained"],
        ["/home/moving-costs-explained/", "What moving really costs"]
      ]
    },
    "buy-ready": {
      name: "Buying is the realistic call — do the diligence",
      cost: "At your horizon with your deposit, entry costs amortise and cost-predictability starts working for you. Budget the boring trio too: maintenance, tax/charges, insurance.",
      links: [
        ["/home/mortgage-payments-explained/", "What mortgage payments really are"],
        ["/home/moving-costs-explained/", "What moving really costs"],
        ["/home/renter-vs-owner-repairs/", "Every repair just became yours"],
        ["/home/improvements-no-resale-value/", "Improvements that don't pay back"]
      ]
    }
  };

  var DILIGENCE = {
    uk: "UK diligence: run the official stamp-duty (SDLT) calculator including first-time-buyer relief; check TENURE (leasehold vs freehold) and service charges before falling in love; a proper survey, not just the lender's valuation.",
    us: "US diligence: get closing-cost estimates in writing (they vary by state and county); find the property's annual tax bill — it never ends; the mortgage-interest deduction only helps if you itemise.",
    ca: "Canada diligence: land transfer tax (first-time rebates exist in some provinces — check yours); below 20% down means mandatory mortgage default insurance; the FHSA is the tax-advantaged way to save the deposit.",
    anz: "AU/NZ diligence: stamp duty and first-home grants are STATE matters — your state revenue office's calculator is the only authority; check foreign-buyer rules if any apply to you.",
    eu: "EU diligence: notary fees and transfer taxes swing hugely by country (and region) — get local figures, never averages; mortgage markets are national, so shop domestically.",
    ng: "Nigeria diligence: rent is commonly demanded 1–2 YEARS upfront — price the cash-flow, not just the monthly equivalent. If buying: verify title properly (Certificate of Occupancy, governor's consent, a registered survey) through a lawyer — the title, not the fence, is the protection. Lagos State's tenancy law governs notice and ejection.",
    other: "Universal diligence: get the real entry/exit costs (transfer taxes, legal, agent fees) in writing before deciding; add the boring trio — maintenance, property charges, insurance — to any monthly comparison."
  };

  var state = { step: 0, answers: {} };

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  function labelFor(key, id) {
    var qs = QUESTIONS.filter(function (q) { return q.key === key; })[0];
    var o = qs.opts.filter(function (o) { return o.id === id; })[0];
    return o ? o.label : id;
  }

  function decide(a) {
    var why = [];
    var out, dil = DILIGENCE[a.market] || DILIGENCE.other;

    why.push("Your market: " + labelFor("market", a.market) + " — its entry costs and schemes shape everything below.");

    if (a.horizon === "lt2") {
      out = "rent-flexibility";
      why.push("Under two years: transaction costs almost never round-trip that fast, in any market. This is the rare universal in this question.");
    } else if (a.horizon === "y2_5") {
      out = "rent-save";
      why.push("At 2–5 years, entry costs still dominate the maths — rent deliberately and bank the difference so the deposit (and the schemes) are ready when the horizon lengthens.");
      if (a.rentcost === "renthigh") why.push("High local rent tilts the scale toward buying SOONER — run the five-year test with real numbers before dismissing it.");
    } else if (a.deposit === "none") {
      out = "rent-save";
      why.push("No deposit yet means the decision makes itself for now: the emergency fund comes first, the deposit second, the house third — in that order, the maths always wins.");
    } else if ((a.deposit === "small") && (a.income === "stable" || a.income === "growing") && (a.rentcost !== "rentcheap")) {
      out = "buy-schemes";
      why.push("A small deposit with stable income is exactly the profile first-home schemes are built for in your market — check eligibility and thresholds before anything else.");
    } else if ((a.deposit === "standard" || a.deposit === "large") && (a.income === "stable" || a.income === "growing")) {
      out = "buy-ready";
      why.push("A real deposit, serviceable income, and a " + (a.horizon === "y10p" ? "10+ year" : "5–10 year") + " horizon: entry costs amortise and predictability starts working for you.");
    } else {
      out = "rent-save";
      why.push("Something in the stack isn't ready — deposit, income shape, or local rent maths. Renting deliberately while you fix that beats buying under pressure.");
    }

    if (a.income === "variable" && (out === "buy-ready" || out === "buy-schemes")) {
      why.push("Variable income caveat: stress-test the payment against your WORST year, not your average — the mortgage doesn't flex when clients pay late.");
    }
    if (a.rentcost === "renthigh" && (out === "rent-save" || out === "rent-flexibility")) {
      why.push("Because local rent is high: every rented year buys flexibility you may not need — re-run this maths yearly, the answer can flip.");
    }
    if (a.rentcost === "unknown") {
      why.push("You haven't compared local rent against the monthly cost of owning (payment + tax/charges + maintenance + insurance). That comparison is the homework — the tool's call is provisional until it's done.");
    }
    if (a.priority === "flexibility" && (out === "buy-ready" || out === "buy-schemes")) {
      why.push("You ranked freedom to move first — weigh it before signing: selling is the most expensive move in the whole decision.");
    }
    if ((a.priority === "control" || a.priority === "equity") && (out === "rent-save" || out === "rent-flexibility")) {
      why.push("You ranked ownership itself highly — that's a real value, not a number. If it keeps pulling, shorten the savings runway (schemes, longer horizon) rather than ignore it.");

    return { out: out, why: why, dil: dil };
  }

  function render() {
    mount.innerHTML = "";
    var card = el("div", "rb-card");
    if (state.step < QUESTIONS.length) {
      var q = QUESTIONS[state.step];
      card.appendChild(el("p", "rb-step", "Question " + (state.step + 1) + " of " + QUESTIONS.length));
      card.appendChild(el("p", "rb-q", q.q));
      var opts = el("div", "rb-opts");
      q.opts.forEach(function (o) {
        var b = el("button", "rb-opt", o.label + (o.note ? "<small>" + o.note + "</small>" : ""));
        b.type = "button";
        b.addEventListener("click", function () {
          state.answers[q.key] = o.id;
          state.step += 1;
          render();
        });
        opts.appendChild(b);
      });
      card.appendChild(opts);
      if (state.step > 0) {
        var nav = el("div", "rb-nav");
        var back = el("button", null, "← Back");
        back.type = "button";
        back.addEventListener("click", function () { state.step -= 1; render(); });
        nav.appendChild(back);
        nav.appendChild(el("span", "rb-progress", "Nothing is stored or sent — the tool lives in this tab."));
        card.appendChild(nav);
      }
    } else {
      var d = decide(state.answers);
      var o = OUTCOMES[d.out];
      card.setAttribute("aria-live", "polite");
      var res = el("div", "rb-result");
      res.appendChild(el("p", "rb-step", "The honest call"));
      res.appendChild(el("h3", null, o.name));
      res.appendChild(el("p", null, "<b>Why — your answers, in order:</b>"));
      var ul = el("ul", "rb-why");
      d.why.forEach(function (w) { ul.appendChild(el("li", null, w)); });
      res.appendChild(ul);
      res.appendChild(el("p", "rb-cost", "<b>The money shape:</b> " + o.cost));
      res.appendChild(el("p", "rb-dilig", "<b>Before you act:</b> " + d.dil));
      var links = el("div", "rb-links");
      o.links.forEach(function (l) {
        var a = el("a", null, l[1]);
        a.href = l[0];
        links.appendChild(a);
      });
      res.appendChild(links);
      var nav2 = el("div", "rb-nav");
      var again = el("button", null, "↺ Start over");
      again.type = "button";
      again.addEventListener("click", function () { state = { step: 0, answers: {} }; render(); });
      nav2.appendChild(again);
      res.appendChild(nav2);
      res.appendChild(el("p", "rb-privacy", "No price predictions, no invented figures, no network calls, nothing stored. General information — never financial advice."));
      card.appendChild(res);
    }
    mount.appendChild(card);
  }

  render();
})();
