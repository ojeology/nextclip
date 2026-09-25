/*!
 * which-heating-tool.js — BRYME Home & DIY decision tool (§16).
 * Mounts on #which-heating-tool. Six questions -> one rung of the honest
 * heating ladder (cool-first / keep-and-tune / fabric-first / heat pump /
 * modern gas / modern electric), fabric-first rule enforced, reasoning shown.
 * On-device only: no storage, no network calls. External file: site CSP is
 * script-src 'self' https: (no inline scripts). Cost SHAPES, never quotes;
 * gas work always deferred to qualified professionals.
 */
(function () {
  "use strict";
  var mount = document.getElementById("which-heating-tool");
  if (!mount) return;

  var QUESTIONS = [
    {
      key: "climate",
      q: "What does the year actually demand?",
      opts: [
        { id: "coldgas", label: "Cold winters, gas grid available", note: "" },
        { id: "coldnogas", label: "Cold winters, no gas grid", note: "" },
        { id: "mild", label: "Mild — heating is occasional", note: "" },
        { id: "hot", label: "Hot — cooling is the real question", note: "The honest answer for much of Nigeria, and every summer somewhere else" }
      ]
    },
    {
      key: "current",
      q: "What's on the wall (or in the cupboard) now?",
      opts: [
        { id: "gas", label: "A gas boiler and radiators", note: "" },
        { id: "oldel", label: "Old electric — storage heaters or portable units", note: "" },
        { id: "newel", label: "Modern electric — panels, split AC, or a heat pump already", note: "" },
        { id: "none", label: "Nothing that works properly", note: "" }
      ]
    },
    {
      key: "fabric",
      q: "How tight is the building itself?",
      opts: [
        { id: "good", label: "Well insulated, no obvious draughts", note: "Recent insulation, good glazing" },
        { id: "medium", label: "Average — some insulation, some draughts", note: "" },
        { id: "poor", label: "Draughty, thin, or old", note: "" },
        { id: "unknown", label: "No idea", note: "An honest answer — and fixable with an evening's walk-round" }
      ]
    },
    {
      key: "budget",
      q: "What can you honestly spend now?",
      opts: [
        { id: "minimal", label: "Minimal — fixes only", note: "" },
        { id: "moderate", label: "A moderate project", note: "One real improvement" },
        { id: "replacement", label: "A full system replacement is on the table", note: "" }
      ]
    },
    {
      key: "driver",
      q: "What triggered this?",
      opts: [
        { id: "bills", label: "The bills hurt", note: "" },
        { id: "broken", label: "The system is failing or dead", note: "" },
        { id: "emissions", label: "Emissions — I want off gas if it's sensible", note: "" },
        { id: "comfort", label: "Some rooms never get warm", note: "" }
      ]
    },
    {
      key: "hometype",
      q: "What kind of home is it?",
      opts: [
        { id: "flat", label: "Flat or small home", note: "" },
        { id: "house", label: "Ordinary house", note: "" },
        { id: "bigold", label: "Large or period home", note: "High ceilings, solid walls" }
      ]
    }
  ];

  var OUTCOMES = {
    "keep-tune": {
      name: "Keep it and tune it — the $0-to-low rung",
      cost: "Near zero, cuts bills immediately: bleed radiators, correct boiler pressure, fresh filters, deliberate thermostat settings, closed draughts. A surprising share of 'heating problems' live on this rung.",
      links: [
        ["/home/how-to-bleed-a-radiator/", "How to bleed a radiator"],
        ["/home/boiler-pressure-low-or-high/", "Boiler pressure, honestly"],
        ["/home/thermostat-settings-that-save-money/", "Thermostat settings that save money"],
        ["/home/radiators-cold-top-or-bottom/", "Cold radiators, diagnosed"]
      ]
    },
    "fabric-first": {
      name: "Fabric first — insulate before you buy machinery",
      cost: "Moderate, permanent: every unit of heat you stop leaking lowers the price of EVERY system you could install afterwards. Payback is years, not months — it's an asset, not a trick.",
      links: [
        ["/home/attic-insulation-basics/", "Attic insulation basics"],
        ["/home/draught-proofing-mistakes/", "Draught-proofing mistakes"],
        ["/home/single-glazing-payback/", "Single glazing payback"],
        ["/home/epc-rating-explained/", "What the EPC rating means"]
      ]
    },
    heatpump: {
      name: "Heat pump — the efficiency winner in a tight house",
      cost: "High upfront, low running cost per unit of heat. Sizing and installer quality decide everything; a proper survey is non-negotiable — a tool that guesses kW is guessing.",
      links: [
        ["/home/heat-pump-vs-gas-furnace/", "Heat pump vs gas, honestly"],
        ["/home/attic-insulation-basics/", "Insulate before you install"],
        ["/home/epc-rating-explained/", "What the EPC rating means"]
      ]
    },
    "modern-gas": {
      name: "A modern condensing gas boiler — the pragmatic bridge",
      cost: "Moderate upfront, running cost follows gas prices. Where the grid exists, the fabric is poor, and the budget is now — installed and serviced by a qualified professional, always.",
      links: [
        ["/home/heat-pump-vs-gas-furnace/", "Heat pump vs gas, honestly"],
        ["/home/boiler-pressure-low-or-high/", "Boiler pressure, honestly"],
        ["/home/how-to-bleed-a-radiator/", "How to bleed a radiator"]
      ]
    },
    "modern-electric": {
      name: "Modern electric — efficient hardware, tariff discipline",
      cost: "Low-to-moderate upfront; per-kWh is the pricey part, so the TARIFF moves the bill more than the hardware does. Old storage heaters are the expensive version of electric.",
      links: [
        ["/home/storage-heaters-explained/", "Storage heaters explained"],
        ["/home/off-peak-electricity-tariffs-explained/", "Off-peak tariffs explained"],
        ["/home/why-is-my-electric-bill-so-high/", "Why the bill is high"]
      ]
    },
    "cool-first": {
      name: "Cooling is your heating question — shade, airflow, then AC",
      cost: "Cheap first: shade the glass, move the air, then a CORRECTLY SIZED unit. Oversized AC short-cycles, under-dehumidifies and wastes money — sizing beats brand, everywhere.",
      links: [
        ["/home/cost-to-run-air-conditioning/", "What AC actually costs to run"],
        ["/home/window-film-for-heat/", "Window film for heat"],
        ["/home/ceiling-fan-direction-summer-winter/", "Fan direction, summer vs winter"],
        ["/home/ac-outdoor-unit-care/", "Outdoor unit care"]
      ]
    }
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
    var out, move;

    why.push("Your year demands: " + labelFor("climate", a.climate) + ".");

    if (a.climate === "hot") {
      out = "cool-first";
      why.push("In a hot climate the 'heating' budget is really a cooling budget — and the cheapest cooling is the heat you never let in: shade, ventilation, then a correctly sized unit.");
      move = "When the home is well shaded and the unit still can't hold temperature — that's a sizing or fabric problem, not a brand problem.";
      return { out: out, why: why, move: move };
    }

    if (a.current === "newel") {
      out = "keep-tune";
      why.push("You already have modern hardware — the wins left are maintenance and settings, not a new machine. Service it, clean the filters, set schedules deliberately.");
      move = "When the fabric improves enough that a smaller/cheaper setup would do — or when the hardware itself fails.";
      return { out: out, why: why, move: move };
    }

    var leaky = (a.fabric === "poor" || a.fabric === "unknown");
    if (leaky) {
      why.push(a.fabric === "poor"
        ? "The building leaks heat — that fact outranks every machine on this page."
        : "Fabric unknown: an evening's walk-round (draughts at doors/windows, cold loft hatch, single glazing) will tell you more than any brochure. Assume leaky until proven otherwise.");
    }

    if (a.budget === "minimal") {
      out = "keep-tune";
      why.push("At a minimal budget the honest ladder starts at fixes: bleed, pressure, filters, draught tape, thermostat discipline — real bill cuts for near-zero spend.");
      move = "When fixes stop fixing: recurring failures mean the system itself is finished, and the fabric work should start before any replacement.";
      return { out: out, why: why, move: move };
    }

    if (leaky && a.budget === "moderate") {
      out = "fabric-first";
      why.push("One moderate project in a leaky house is worth more on the envelope than on machinery: insulation and draughts permanently lower what any future system costs to run.");
      move = "When the fabric is done — then choose the machine, one size smaller and cheaper than you'd have needed before.";
      return { out: out, why: why, move: move };
    }

    if (a.climate === "coldnogas" || a.current === "oldel") {
      if (a.driver === "emissions" && a.fabric === "good") {
        out = "heatpump";
        why.push("No gas grid, good fabric, emissions-driven: an air-source heat pump is the coherent answer — efficient, electric, and the fabric means it runs cheap.");
      } else {
        out = "modern-electric";
        why.push("No gas grid (or old electric): modern electric hardware plus a smart tariff is the realistic path — the tariff decision moves the bill more than the brand does.");
        if (a.current === "oldel") why.push("Old storage heaters are the expensive version of electric — replacing them pays back in comfort first, bills second.");
      }
      move = "If you later insulate deeply, revisit the heat-pump maths — fabric upgrades change the answer.";
      return { out: out, why: why, move: move };
    }

    /* gas-grid territory */
    if (a.current === "gas" && a.driver === "bills") {
      out = leaky ? "fabric-first" : "keep-tune";
      why.push(leaky
        ? "Bills hurting with a gas system in a leaky house: the leak is the bill. Envelope first — every degree you keep is cheaper than every degree you generate."
        : "Bills hurting with a gas system in a tight house: tune before you spend — schedules, thermostat discipline, serviced boiler, bled radiators.");
      move = leaky ? "After the fabric work, re-check the bills — if they still hurt, the system's efficiency is the next suspect."
                   : "If tuning doesn't move the bills, the boiler's age/modulation is the next suspect — a modern condensing unit is the bridge.";
      return { out: out, why: why, move: move };
    }

    if (a.driver === "emissions" && a.fabric === "good" && a.budget === "replacement") {
      out = "heatpump";
      why.push("Emissions-driven, tight house, replacement budget: this is the textbook heat-pump case — the only one where the green choice is also the cheap-to-run choice from day one.");
      move = "Rarely backwards — but if electricity tariffs spike permanently, revisit the running-cost maths annually.";
      return { out: out, why: why, move: move };
    }

    if (a.current === "gas" && a.driver === "broken" && leaky && a.budget === "replacement") {
      out = "modern-gas";
      why.push("A dead boiler in a leaky house with money to spend once: the honest sequence is a modern condensing boiler NOW (heat today) plus a staged fabric plan (insulation over the next years) that keeps a future heat pump viable.");
      why.push("Buying a heat pump into a leaky fabric is the expensive mistake this tool exists to prevent.");
      move = "When the fabric work is done — that's the heat-pump conversation, and this boiler becomes the backup or the exit.";
      return { out: out, why: why, move: move };
    }

    out = a.fabric === "good" ? "heatpump" : "modern-gas";
    why.push(a.fabric === "good"
      ? "Good fabric with a replacement decision: the heat pump's efficiency finally lands where it pays — sizing survey first, installer references second."
      : "Average fabric with the grid available: a modern condensing boiler is the pragmatic call now, with draught-proofing and insulation as the follow-through that shrinks every future bill.");
    move = a.fabric === "good"
      ? "If tariffs move dramatically, re-run the maths yearly — but the fabric means you're insulated from the worst of it."
      : "When the fabric work lands, revisit heat-pump viability before the boiler's next failure — plan the transition, don't inherit it.";
    return { out: out, why: why, move: move };
  }

  function render() {
    mount.innerHTML = "";
    var card = el("div", "ht-card");
    if (state.step < QUESTIONS.length) {
      var q = QUESTIONS[state.step];
      card.appendChild(el("p", "ht-step", "Question " + (state.step + 1) + " of " + QUESTIONS.length));
      card.appendChild(el("p", "ht-q", q.q));
      var opts = el("div", "ht-opts");
      q.opts.forEach(function (o) {
        var b = el("button", "ht-opt", o.label + (o.note ? "<small>" + o.note + "</small>" : ""));
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
        var nav = el("div", "ht-nav");
        var back = el("button", null, "← Back");
        back.type = "button";
        back.addEventListener("click", function () { state.step -= 1; render(); });
        nav.appendChild(back);
        nav.appendChild(el("span", "ht-progress", "Nothing is stored or sent — the tool lives in this tab."));
        card.appendChild(nav);
      }
    } else {
      var d = decide(state.answers);
      var o = OUTCOMES[d.out];
      card.setAttribute("aria-live", "polite");
      var res = el("div", "ht-result");
      res.appendChild(el("p", "ht-step", "Your rung"));
      res.appendChild(el("h3", null, o.name));
      res.appendChild(el("p", null, "<b>Why — your answers, in order:</b>"));
      var ul = el("ul", "ht-why");
      d.why.forEach(function (w) { ul.appendChild(el("li", null, w)); });
      res.appendChild(ul);
      res.appendChild(el("p", "ht-cost", "<b>Cost shape:</b> " + o.cost));
      res.appendChild(el("p", null, "<b>Move rungs when:</b> " + d.move));
      var links = el("div", "ht-links");
      o.links.forEach(function (l) {
        var a = el("a", null, l[1]);
        a.href = l[0];
        links.appendChild(a);
      });
      res.appendChild(links);
      var nav2 = el("div", "ht-nav");
      var again = el("button", null, "↺ Start over");
      again.type = "button";
      again.addEventListener("click", function () { state = { step: 0, answers: {} }; render(); });
      nav2.appendChild(again);
      res.appendChild(nav2);
      res.appendChild(el("p", "ht-privacy", "Cost shapes are directional, never quotes. Gas work belongs to qualified professionals. No network calls, nothing stored."));
      card.appendChild(res);
    }
    mount.appendChild(card);
  }

  render();
})();
