/*!
 * which-cloud-model-tool.js — BRYME Tech decision tool (§16).
 * Mounts on #cloud-model-tool. Six questions -> one rung of the cloud ladder
 * (SaaS / static-free / PaaS / IaaS / serverless / self-hosted), reasoning
 * shown per answer. On-device only: no storage, no network calls. External
 * file because the site CSP is script-src 'self' https: (no inline scripts).
 * Cost SHAPES are directional — never quotes.
 */
(function () {
  "use strict";
  var mount = document.getElementById("cloud-model-tool");
  if (!mount) return;

  var QUESTIONS = [
    {
      key: "workload",
      q: "What do you actually need running?",
      opts: [
        { id: "existing", label: "A business problem existing software already solves", note: "CRM, email, accounting, chat — it's not your differentiator" },
        { id: "static", label: "A static site, docs or landing page", note: "Files, or a static generator" },
        { id: "app", label: "A web app or API", note: "Your code, or third-party code you deploy" },
        { id: "data", label: "Data processing or ML workloads", note: "Pipelines, training, big batch jobs" },
        { id: "tools", label: "Internal tools for my team", note: "Dashboards, admin panels, automations" }
      ]
    },
    {
      key: "ops",
      q: "Who can maintain servers?",
      opts: [
        { id: "none", label: "Nobody — servers are not happening", note: "" },
        { id: "guided", label: "Me, following a guide", note: "" },
        { id: "ops", label: "Someone comfortable with real ops", note: "Terminal, networking, patching — routine" }
      ]
    },
    {
      key: "load",
      q: "What shape is the load?",
      opts: [
        { id: "steady", label: "Steady, predictable", note: "Roughly the same every month" },
        { id: "spiky", label: "Spiky", note: "Launches, campaigns, time-of-day peaks" },
        { id: "quiet", label: "Mostly idle with occasional bursts", note: "Nights and weekends quiet" },
        { id: "unknown", label: "No idea yet", note: "" }
      ]
    },
    {
      key: "buybuild",
      q: "For the business logic itself: buy or build?",
      opts: [
        { id: "buy", label: "Buy — renting beats building here", note: "" },
        { id: "build", label: "Build — this is the product", note: "" },
        { id: "mixed", label: "Mixed — build the core, buy the boring parts", note: "The honest answer for most teams" }
      ]
    },
    {
      key: "budget",
      q: "Honest monthly budget?",
      opts: [
        { id: "zero", label: "$0", note: "" },
        { id: "under50", label: "Up to $50/month", note: "" },
        { id: "mid", label: "$50–500/month", note: "" },
        { id: "open", label: "$500+/month", note: "" }
      ]
    },
    {
      key: "data",
      q: "What will it hold?",
      opts: [
        { id: "none", label: "Nothing sensitive", note: "" },
        { id: "some", label: "Customer or business data", note: "" },
        { id: "strict", label: "Regulated data or residency rules", note: "It must stay in-country, or a regulator says how" }
      ]
    }
  ];

  var OUTCOMES = {
    saas: {
      name: "SaaS — buy the software, rent everything",
      cost: "Per-seat or per-month subscription. The real cost is the seats you forgot to cancel — audit them like any subscription.",
      links: [
        ["/tech/build-vs-buy-the-honest-decision/", "Build vs buy: the honest decision"],
        ["/tech/saas-pricing-models-explained/", "SaaS pricing models explained"],
        ["/tech/saas-lock-in-and-data-portability/", "Lock-in and data portability"]
      ]
    },
    "static-free": {
      name: "Static hosting — the $0 rung",
      cost: "$0 + a domain (~$15/year). Free tiers of static hosts are genuinely usable.",
      links: [
        ["/tech/where-to-host-website-for-free/", "Where to host free — and what free means"],
        ["/tech/which-hosting-type/", "Which hosting type do I need? (sister tool)"],
        ["/tech/free-vs-paid-hosting/", "Free vs paid hosting, honestly"]
      ]
    },
    paas: {
      name: "PaaS — you ship code, the platform runs it",
      cost: "Usage-based and usually modest for small apps — watch egress and build-minute meters, they're the quiet ones.",
      links: [
        ["/tech/aws-vs-azure-vs-gcp-choosing/", "AWS vs Azure vs GCP, choosing"],
        ["/tech/cloud-bill-why-it-spikes/", "Why cloud bills spike"],
        ["/tech/hosting-types-compared-shared-vps-cloud-dedicated/", "Hosting types compared"]
      ]
    },
    iaas: {
      name: "IaaS — rent the machine, run the stack",
      cost: "Hourly or monthly, predictable when the load is steady. You pay for idle capacity whether you use it or not.",
      links: [
        ["/tech/aws-vs-azure-vs-gcp-choosing/", "AWS vs Azure vs GCP, choosing"],
        ["/tech/what-is-a-vps-when-you-need-one/", "What a VPS is (IaaS's smaller cousin)"],
        ["/tech/cloud-bill-why-it-spikes/", "Why cloud bills spike"]
      ]
    },
    serverless: {
      name: "Serverless — pay per request, $0 when quiet",
      cost: "Per-invocation. Perfectly matched to spiky or mostly-idle work — until an uncapped burst writes the invoice.",
      links: [
        ["/tech/cloud-bill-why-it-spikes/", "Cap it: why cloud bills spike"],
        ["/tech/aws-vs-azure-vs-gcp-choosing/", "AWS vs Azure vs GCP, choosing"],
        ["/tech/cloud-hosting/", "The whole cloud & hosting cluster"]
      ]
    },
    "self-hosted": {
      name: "Self-hosted — the work (and control) stays home",
      cost: "Hardware up front + your labour forever. Underpricing your own time is the classic mistake.",
      links: [
        ["/tech/self-hosting-saas-when-its-worth-it/", "When self-hosting is actually worth it"],
        ["/tech/home-nas-vs-cloud-vs-drive/", "NAS vs cloud storage"],
        ["/tech/data-security-compliance-gdpr-ccpa-ndpr/", "GDPR, CCPA and NDPA side by side"]
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
    why.push("You need running: " + labelFor("workload", a.workload) + ".");

    if ((a.workload === "existing" || a.buybuild === "buy") && a.data !== "strict") {
      out = "saas";
      why.push("When the problem isn't your differentiator, renting the software beats building and running it — the ladder starts at 'the vendor does everything'.");
      move = "When the subscription's limits start bending your process instead of serving it — or when you outgrow per-seat maths.";
    } else if (a.workload === "static") {
      out = "static-free";
      why.push("Static files don't need a server — edge caches do. This is the only genuinely $0 rung and it's not a toy tier.");
      move = "The day you need server-side code or a CMS login.";
    } else if (a.data === "strict" && a.ops === "ops" && a.load === "steady") {
      out = "self-hosted";
      why.push("Strict residency rules + steady load + real ops skills is the one corner where self-hosting wins on cost AND compliance — the data never leaves your building.");
      why.push("The honest price: your labour is the subscription. Verify the regulation's actual requirement — some accept certified in-country clouds, which beats running your own rack.");
      move = "When uptime obligations outgrow one team's on-call rota — that's the certified-in-country-cloud conversation.";
    } else if (a.workload === "app" || a.workload === "tools") {
      if (a.ops === "ops") {
        if (a.load === "steady") {
          out = "iaas";
          why.push("Steady load + ops comfort = rent the machine. Flat cost beats per-request maths when the work never stops.");
          move = "When the load stops being steady, or the fleet of machines becomes its own project.";
        } else if (a.load === "spiky" || a.load === "quiet") {
          out = "serverless";
          why.push(labelFor("load", a.load) + " work is serverless's native shape: pay when requests arrive, $0 when they don't.");
          why.push("The rule that keeps it honest: cap concurrency and set a billing alarm before launch day.");
          move = "When steady baseline traffic makes per-invocation maths worse than a flat machine — run the numbers quarterly.";
        } else {
          out = "paas";
          why.push("Load unknown: start on the middle rung. A PaaS runs your code without an ops job, and moving up or down later is a config change, not a re-platform.");
          move = "Once you can measure the load shape — steady goes IaaS, spiky goes serverless.";
        }
      } else {
        out = "paas";
        why.push("No ops bench: a managed platform runs the servers while you keep the code. You're paying to not have a 2am pager — knowingly.");
        if (a.budget === "zero") why.push("At $0: free PaaS tiers genuinely cover hobby scale — with hard limits you'll feel before you outgrow them.");
        move = "When platform limits bend your architecture, or the bill exceeds what a small VPS would cost for the same steady work.";
      }
    } else {
      /* data workloads */
      if (a.ops === "ops") {
        out = "iaas";
        why.push("Data/ML work on a real ops bench: rent compute close to the data, keep the pipeline yours. Spot/preemptible capacity cuts batch costs sharply.");
        move = "When GPU scarcity or scheduling overhead dominates — managed ML services exist for exactly that.";
      } else {
        out = "paas";
        why.push("Data work without an ops bench: managed services (warehouses, notebooks, pipelines) — the meter is the trade for not running the cluster.");
        move = "When the meter exceeds a cluster's flat cost — that crossover is real and worth re-checking yearly.";
      }
    }

    if (a.data === "strict" && out !== "self-hosted") {
      why.push("Strict residency rules: verify the provider's in-country regions and compliance docs before signing — the tool flags it, it can't audit it.");
    }
    return { out: out, why: why, move: move };
  }

  function render() {
    mount.innerHTML = "";
    var card = el("div", "cm-card");
    if (state.step < QUESTIONS.length) {
      var q = QUESTIONS[state.step];
      card.appendChild(el("p", "cm-step", "Question " + (state.step + 1) + " of " + QUESTIONS.length));
      card.appendChild(el("p", "cm-q", q.q));
      var opts = el("div", "cm-opts");
      q.opts.forEach(function (o) {
        var b = el("button", "cm-opt", o.label + (o.note ? "<small>" + o.note + "</small>" : ""));
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
        var nav = el("div", "cm-nav");
        var back = el("button", null, "← Back");
        back.type = "button";
        back.addEventListener("click", function () { state.step -= 1; render(); });
        nav.appendChild(back);
        nav.appendChild(el("span", "cm-progress", "Nothing is stored or sent — the tool lives in this tab."));
        card.appendChild(nav);
      }
    } else {
      var d = decide(state.answers);
      var o = OUTCOMES[d.out];
      card.setAttribute("aria-live", "polite");
      var res = el("div", "cm-result");
      res.appendChild(el("p", "cm-step", "Your rung"));
      res.appendChild(el("h3", null, o.name));
      res.appendChild(el("p", null, "<b>Why — your answers, in order:</b>"));
      var ul = el("ul", "cm-why");
      d.why.forEach(function (w) { ul.appendChild(el("li", null, w)); });
      res.appendChild(ul);
      res.appendChild(el("p", "cm-cost", "<b>Cost shape:</b> " + o.cost + " Directional, not a quote — tax follows your billing address."));
      res.appendChild(el("p", null, "<b>Move rungs when:</b> " + d.move));
      var links = el("div", "cm-links");
      o.links.forEach(function (l) {
        var a = el("a", null, l[1]);
        a.href = l[0];
        links.appendChild(a);
      });
      res.appendChild(links);
      var nav2 = el("div", "cm-nav");
      var again = el("button", null, "↺ Start over");
      again.type = "button";
      again.addEventListener("click", function () { state = { step: 0, answers: {} }; render(); });
      nav2.appendChild(again);
      res.appendChild(nav2);
      res.appendChild(el("p", "cm-privacy", "The tool made no network calls and stored nothing. Provider choice comes after the rung — see the linked comparisons."));
      card.appendChild(res);
    }
    mount.appendChild(card);
  }

  render();
})();
