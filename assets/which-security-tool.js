/*!
 * which-security-tool.js — BRYME Tech decision tool (§16, cybersecurity cluster).
 * Mounts on #security-solution-tool. Six questions -> one rung of the honest
 * security ladder (consumer basics / business AV-EDR / training-first / MDR /
 * co-managed MSSP / website hardening), reasoning shown per answer.
 * On-device only: no storage, no network calls. External file because the site
 * CSP is script-src 'self' https: (no inline scripts). Prices are SHAPES, not
 * quotes: MDR/MSSP pricing is genuinely quote-based and we won't invent it.
 */
(function () {
  "use strict";
  var mount = document.getElementById("security-solution-tool");
  if (!mount) return;

  var QUESTIONS = [
    {
      key: "scope",
      q: "What are you protecting?",
      opts: [
        { id: "personal", label: "Personal and family devices", note: "Phones, laptops, the household" },
        { id: "smallbiz", label: "A small business (under ~25 people)", note: "" },
        { id: "org", label: "A larger organisation", note: "Multiple sites, staff, or systems" },
        { id: "website", label: "A website or web app", note: "The public-facing thing" }
      ]
    },
    {
      key: "owner",
      q: "Who owns security day to day?",
      opts: [
        { id: "nobody", label: "Nobody — it keeps getting skipped", note: "The most honest answer in most small businesses" },
        { id: "parttime", label: "Someone, part-time, alongside everything else", note: "" },
        { id: "dedicated", label: "A dedicated person or team", note: "" }
      ]
    },
    {
      key: "fear",
      q: "What are you actually most afraid of?",
      opts: [
        { id: "ransomware", label: "Ransomware / malware", note: "Everything encrypted or down" },
        { id: "phishing", label: "Phishing / someone clicking the wrong thing", note: "" },
        { id: "breach", label: "Customer data leaking", note: "" },
        { id: "compliance", label: "Failing a compliance obligation", note: "Questionnaires, audits, regulators" },
        { id: "downtime", label: "Downtime", note: "The site or systems just being down" }
      ]
    },
    {
      key: "twa",
      q: "When something happens at 2am, who notices?",
      opts: [
        { id: "unknown", label: "Honestly? Nobody knows", note: "" },
        { id: "nice", label: "Nice if someone did", note: "" },
        { id: "yes", label: "Someone must — downtime or breach is expensive", note: "" },
        { id: "no", label: "We'd handle it in the morning", note: "" }
      ]
    },
    {
      key: "compliance",
      q: "What compliance pressure do you carry?",
      opts: [
        { id: "none", label: "None", note: "" },
        { id: "questionnaires", label: "Customer security questionnaires", note: "The occasional spreadsheet from a client" },
        { id: "regulated", label: "Real obligations", note: "GDPR / NDPA / payment data / sector rules" }
      ]
    },
    {
      key: "budget",
      q: "Honest monthly budget?",
      opts: [
        { id: "zero", label: "$0", note: "" },
        { id: "under50", label: "Up to $50/month", note: "" },
        { id: "mid", label: "$50–500/month", note: "" },
        { id: "quote", label: "$500+/month or quote-based", note: "" }
      ]
    }
  ];

  var OUTCOMES = {
    "consumer-basics": {
      name: "Consumer basics — $0, and not the weak option",
      cost: "$0: your OS's built-in protection is genuinely good now, plus a real password manager and 2FA everywhere. Paid suites mostly add support, not safety.",
      links: [
        ["/tech/your-security-checklist/", "Your security checklist"],
        ["/tech/bitwarden-free-password-manager/", "The free password manager worth using"],
        ["/tech/two-factor-authentication-setup/", "Two-factor authentication, set up properly"]
      ]
    },
    "business-av-edr": {
      name: "Business-grade AV/EDR on every endpoint",
      cost: "Per user per month at list — commonly single digits. The fleet-wide view is the upgrade over consumer AV: one dashboard, remote isolation.",
      links: [
        ["/tech/mdr-what-managed-detection-actually-buys/", "What detection actually buys (EDR vs MDR)"],
        ["/tech/three-two-one-backup-rule/", "The 3-2-1 backup rule"],
        ["/tech/your-security-checklist/", "Your security checklist"]
      ]
    },
    "training-first": {
      name: "Training-first: drills + business AV",
      cost: "Training platforms price per user per month at list; free drills go a long way. The software half is business AV at single-digit list per user.",
      links: [
        ["/tech/phishing-training-that-actually-works/", "Phishing training that actually works"],
        ["/tech/phishing-drill-five-real-lures/", "Five real lures for your first drill"],
        ["/tech/how-to-spot-a-suspicious-link/", "How to spot a suspicious link"]
      ]
    },
    mdr: {
      name: "MDR — a team that watches and responds",
      cost: "Hundreds per month and up, scaling with endpoints — genuinely quote-based. Anyone quoting exact figures without your endpoint count is guessing.",
      links: [
        ["/tech/mdr-what-managed-detection-actually-buys/", "What MDR actually buys"],
        ["/tech/managed-security-service-provider-vs-mdr/", "MSSP vs MDR — the honest difference"],
        ["/tech/incident-response-plan-for-small-business/", "Your one-page incident response plan"]
      ]
    },
    mssp: {
      name: "Co-managed MSSP — their SOC scales your person",
      cost: "Contract quotes. You're buying breadth (firewalls, email, monitoring, compliance reporting) around the dedicated person you already have.",
      links: [
        ["/tech/managed-security-service-provider-vs-mdr/", "MSSP vs MDR — the honest difference"],
        ["/tech/zero-trust-explained-for-small-teams/", "Zero trust, explained for small teams"],
        ["/tech/vulnerability-scanning-explained/", "Vulnerability scanning explained"]
      ]
    },
    "website-hardening": {
      name: "Website hardening — headers, WAF, absorption, backups",
      cost: "$0 to low: DNS-based protection has real free tiers; paid adds WAF tuning, bot management and support. Backups are the non-negotiable part.",
      links: [
        ["/tech/website-security-headers-explained/", "Security headers explained"],
        ["/tech/what-is-a-waf-website-firewall/", "What a WAF actually does"],
        ["/tech/ddos-protection-for-small-sites/", "DDoS protection for small sites"]
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
    why.push("You're protecting: " + labelFor("scope", a.scope) + ".");

    if (a.scope === "personal") {
      out = "consumer-basics";
      why.push("For households the winning stack is free and boring: built-in OS protection, one real password manager, 2FA on every account that matters, updates on. Habits beat products here.");
      if (a.budget !== "zero") why.push("If you'd pay anyway: a reputable suite adds convenience and support — not a different level of safety.");
      move = "Never, honestly — unless you start a business, at which point the fleet question changes everything.";
    } else if (a.scope === "website") {
      out = "website-hardening";
      why.push("A public website's threat model is different: it can't hide, so it hardens — correct headers, a WAF in front, DNS-level DDoS absorption, and backups that survive the site itself.");
      move = "When the site starts holding customer accounts or payments — that's when the business ladder below applies too.";
    } else if (a.owner === "dedicated") {
      if (a.budget === "quote") {
        out = "mssp";
        why.push("A dedicated person + real budget = co-management, not replacement: an MSSP wraps their SOC around your admin so 2am has a bench, not a single name.");
        move = "Rarely backwards — the failure mode is an MSSP contract that quietly becomes the only institutional knowledge. Keep your own runbooks.";
      } else {
        out = "business-av-edr";
        why.push("A dedicated person with a normal budget runs the stack in-house: EDR-class protection on every endpoint, and your team is the responder.");
        why.push("Which makes the written incident plan non-optional — the person IS the process otherwise.");
        move = "When on-call rota or alert volume outgrows one desk — that's the co-managed conversation.";
      }
    } else if (a.owner === "parttime") {
      if ((a.budget === "quote" || a.budget === "mid") && (a.twa === "yes" || a.twa === "unknown")) {
        out = "mdr";
        why.push("Part-time ownership can't be 2am ownership. MDR supplies the team your part-timer can't be: they monitor, triage, and respond with you.");
        why.push("And 'honestly, nobody knows' is the most common answer we see — treat it as 'nobody is watching' until a service says otherwise.");
        move = "When security becomes a full-time remit in-house — renegotiate to co-management instead of cancelling cold.";
      } else {
        out = "business-av-edr";
        why.push("With a tight budget, the highest-leverage spend is fleet-wide EDR-class protection your part-timer can actually read — plus the backup rule that survives everything.");
        if (a.fear === "breach") why.push("Data-leak fear: add regular vulnerability scanning — most breaches walk through unpatched doors.");
        move = "When the dashboard keeps showing things nobody has time to chase — that's the signal to buy the watching, not more software.";
      }
    } else {
      /* nobody owns it */
      if (a.fear === "compliance" || a.compliance === "regulated") {
        out = "mdr";
        why.push("Real obligations need a documented detection-and-response trail — MDR provides the logs, the alerts and the humans that satisfy 'show me you'd notice'.");
      } else if (a.fear === "phishing") {
        out = "training-first";
        why.push("Phishing fear with nobody owning security: the perimeter is your people's inboxes. Drills plus business AV beats any product bought in panic.");
      } else if (a.twa === "yes" || ((a.twa === "unknown") && (a.budget === "mid" || a.budget === "quote"))) {
        out = "mdr";
        why.push("Nobody owns it AND 2am matters: that gap is exactly what MDR sells — a team that watches so ownership stops being a vacancy.");
      } else if (a.budget === "zero" || a.budget === "under50") {
        out = "business-av-edr";
        why.push("At this budget the honest start is business-grade AV/EDR on every endpoint plus free phishing drills — the two cheapest rungs that actually reduce risk.");
        why.push("Set the tripwire now: when the fleet or the fear outgrows the dashboard, MDR is the next rung, not another product.");
      } else {
        out = "mdr";
        why.push("Budget without an owner: buy the watching. MDR converts money into the ownership you don't have in-house.");
      }
      move = "When you hire the dedicated person — most rungs get cheaper and better that day.";
    }

    if ((a.compliance !== "none" || a.fear === "compliance") && a.scope !== "personal" && a.scope !== "website") {
      why.push("Compliance note: a tool never makes you compliant — documented process does. Start with the regulation's actual text (GDPR, Nigeria's NDPA, your sector's rules), not a vendor's summary.");
    }
    if (a.scope !== "personal" && a.scope !== "website") {
      why.push("Whatever rung you land on: a one-page incident response plan is the cheapest security purchase that exists — linked below.");
    }
    return { out: out, why: why, move: move };
  }

  function render() {
    mount.innerHTML = "";
    var card = el("div", "sec-card");
    if (state.step < QUESTIONS.length) {
      var q = QUESTIONS[state.step];
      card.appendChild(el("p", "sec-step", "Question " + (state.step + 1) + " of " + QUESTIONS.length));
      card.appendChild(el("p", "sec-q", q.q));
      var opts = el("div", "sec-opts");
      q.opts.forEach(function (o) {
        var b = el("button", "sec-opt", o.label + (o.note ? "<small>" + o.note + "</small>" : ""));
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
        var nav = el("div", "sec-nav");
        var back = el("button", null, "← Back");
        back.type = "button";
        back.addEventListener("click", function () { state.step -= 1; render(); });
        nav.appendChild(back);
        nav.appendChild(el("span", "sec-progress", "Nothing is stored or sent — the tool lives in this tab."));
        card.appendChild(nav);
      }
    } else {
      var d = decide(state.answers);
      var o = OUTCOMES[d.out];
      card.setAttribute("aria-live", "polite");
      var res = el("div", "sec-result");
      res.appendChild(el("p", "sec-step", "Your rung"));
      res.appendChild(el("h3", null, o.name));
      res.appendChild(el("p", null, "<b>Why — your answers, in order:</b>"));
      var ul = el("ul", "sec-why");
      d.why.forEach(function (w) { ul.appendChild(el("li", null, w)); });
      res.appendChild(ul);
      res.appendChild(el("p", "sec-cost", "<b>Price shape:</b> " + o.cost));
      res.appendChild(el("p", null, "<b>Move rungs when:</b> " + d.move));
      var links = el("div", "sec-links");
      o.links.forEach(function (l) {
        var a = el("a", null, l[1]);
        a.href = l[0];
        links.appendChild(a);
      });
      res.appendChild(links);
      var nav2 = el("div", "sec-nav");
      var again = el("button", null, "↺ Start over");
      again.type = "button";
      again.addEventListener("click", function () { state = { step: 0, answers: {} }; render(); });
      nav2.appendChild(again);
      res.appendChild(nav2);
      res.appendChild(el("p", "sec-privacy", "The tool made no network calls and stored nothing. It flags compliance; it cannot audit it."));
      card.appendChild(res);
    }
    mount.appendChild(card);
  }

  render();
})();
