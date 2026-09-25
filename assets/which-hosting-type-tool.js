/*!
 * which-hosting-type-tool.js — BRYME Tech decision tool (§16).
 * Mounts on #hosting-type-tool. Six questions -> one recommendation, with the
 * reasoning shown. Runs entirely on-device: no storage, no network calls, no
 * telemetry. External file because the site CSP is script-src 'self' https:
 * (no inline scripts). Cost bands mirror /tech/web-hosting-costs-explained/
 * (directional 2026 renewal rates; tax excluded — billing country decides).
 */
(function () {
  "use strict";
  var mount = document.getElementById("hosting-type-tool");
  if (!mount) return;

  var QUESTIONS = [
    {
      key: "build",
      q: "What are you building?",
      opts: [
        { id: "static", label: "A portfolio, landing page or docs site", note: "Static files, or a static generator like Hugo/Jekyll/Astro" },
        { id: "cms", label: "A blog or content site on WordPress (or similar CMS)", note: "Someone logs in and writes; the engine is standard" },
        { id: "store", label: "An online store", note: "Products, cart, checkout" },
        { id: "app", label: "A web app or API with my own code", note: "Node, Python, PHP, Go — anything custom" },
        { id: "lab", label: "Experiments / a hobby project", note: "Cost matters more than polish right now" }
      ]
    },
    {
      key: "traffic",
      q: "How much traffic do you realistically expect?",
      opts: [
        { id: "low", label: "Under ~5,000 visits/month", note: "Most small sites live here for years" },
        { id: "mid", label: "~5,000–50,000 visits/month", note: "A real audience, still modest" },
        { id: "high", label: "50,000+, or seriously spiky", note: "Launches, virality, seasonal peaks" },
        { id: "unknown", label: "No idea yet", note: "An honest answer — it changes the advice" }
      ]
    },
    {
      key: "server",
      q: "Does it need server-side code or a database?",
      opts: [
        { id: "none", label: "No — static files are enough", note: "Nothing executes on a server" },
        { id: "standard", label: "A standard engine only", note: "WordPress, WooCommerce, Ghost…" },
        { id: "custom", label: "Yes — my own backend", note: "You write the code that runs" }
      ]
    },
    {
      key: "admin",
      q: "Who maintains the server?",
      opts: [
        { id: "none", label: "Nobody — I want a panel and support", note: "Updates, backups and security are someone else's job" },
        { id: "guided", label: "Me, with a good guide", note: "You can follow documented steps" },
        { id: "comfy", label: "Me — terminal and all", note: "SSH doesn't scare you" }
      ]
    },
    {
      key: "budget",
      q: "Honest monthly budget — at renewal price, not the banner price?",
      opts: [
        { id: "zero", label: "$0", note: "Free tier or nothing" },
        { id: "under10", label: "Up to $10/month", note: "" },
        { id: "mid", label: "$10–30/month", note: "" },
        { id: "open", label: "$30+/month", note: "" }
      ]
    },
    {
      key: "data",
      q: "What will it hold?",
      opts: [
        { id: "none", label: "Nothing sensitive", note: "" },
        { id: "pii", label: "Payments or personal data", note: "Cards, customer records, emails" },
        { id: "strict", label: "Regulated data or residency rules", note: "Health, finance, government, data must stay in-country" }
      ]
    }
  ];

  var OUTCOMES = {
    "static-free": {
      name: "A static host's free tier",
      cost: "$0 + a domain (~$15/year). No renewal trap exists at $0.",
      links: [
        ["/tech/where-to-host-website-for-free/", "Where to host free — and what free means"],
        ["/tech/free-vs-paid-hosting/", "Free vs paid hosting, honestly"],
        ["/tech/web-hosting-costs-explained/", "The true 3-year cost of paid hosting"]
      ]
    },
    shared: {
      name: "Shared hosting",
      cost: "$9–$16/month at renewal (banner prices of $2–$6 are intro rates on long prepays).",
      links: [
        ["/tech/web-hosting-costs-explained/", "Price it with the 3-year calculator"],
        ["/tech/hosting-types-compared-shared-vps-cloud-dedicated/", "Shared vs VPS vs cloud vs dedicated"],
        ["/tech/free-vs-paid-hosting/", "Free vs paid hosting, honestly"]
      ]
    },
    "managed-wp": {
      name: "Managed WordPress hosting",
      cost: "$9–$20/month at renewal — the premium buys staging, updates and tuned caching.",
      links: [
        ["/tech/web-hosting-costs-explained/", "Price it with the 3-year calculator"],
        ["/tech/hosting-types-compared-shared-vps-cloud-dedicated/", "Hosting types compared"],
        ["/tech/free-vs-paid-hosting/", "Free vs paid hosting, honestly"]
      ]
    },
    vps: {
      name: "A VPS",
      cost: "$12–$60/month at renewal — guaranteed CPU/RAM, root access.",
      links: [
        ["/tech/what-is-a-vps-when-you-need-one/", "What a VPS is and when you need one"],
        ["/tech/web-hosting-costs-explained/", "Price it with the 3-year calculator"],
        ["/tech/hosting-types-compared-shared-vps-cloud-dedicated/", "Hosting types compared"]
      ]
    },
    cloud: {
      name: "Elastic cloud (with a hard autoscaling cap)",
      cost: "Usage-based. A small steady app often lands at $10–$50/month; an uncapped spike can land anywhere.",
      links: [
        ["/tech/cloud-bill-why-it-spikes/", "Why cloud bills spike (and how to cap them)"],
        ["/tech/web-hosting-costs-explained/", "Flat vs usage-based, priced honestly"],
        ["/tech/hosting-types-compared-shared-vps-cloud-dedicated/", "Hosting types compared"]
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

  /* The whole engine: deterministic rules, every branch adds a visible reason. */
  function decide(a) {
    var why = [];
    var out, move;

    why.push("You're building: " + labelFor("build", a.build) + ".");

    if (a.server === "none" && (a.build === "static" || a.build === "lab")) {
      out = "static-free";
      why.push("No server-side code means there is nothing to rent — static hosts serve files from edge caches, and their free tiers are genuinely usable (this very site runs on one).");
      if (a.traffic === "high") why.push("Even at serious traffic, static files stay cheap: caching at the edge absorbs the load.");
      if (a.budget === "zero") why.push("And $0 is exactly the budget you asked for.");
      move = "The day you need a CMS login or server-side code. That's an exit sign, not a failure — migrating a small static site is an afternoon.";
    } else if (a.server === "custom" || a.build === "app") {
      if (a.admin === "comfy") {
        if (a.traffic === "high") {
          out = "cloud";
          why.push("Custom backend + spiky or heavy traffic is exactly what elastic pricing was built for.");
          why.push("The rule that keeps it honest: cap autoscaling, or one spike becomes one invoice.");
          move = "If your load turns out to be steady month after month, a flat-cost VPS is usually far cheaper than elastic.";
        } else {
          out = "vps";
          why.push("You're comfortable running a server, and steady load is cheaper flat-rate than elastic — a VPS buys guaranteed resources for a fixed number.");
          if (a.traffic === "unknown") why.push("Traffic unknown: a VPS scales vertically without re-platforming, which suits uncertainty.");
          move = "When traffic gets spiky enough that you're paying for idle capacity — that's the elastic-cloud conversation.";
        }
      } else {
        out = "cloud";
        why.push("Custom code with no server admin is the expensive combination: a managed cloud platform (PaaS) removes the ops job — and charges for it, knowingly.");
        move = "If the app survives and stabilises, hiring the skills (or learning them) and moving to a VPS usually halves the bill.";
      }
    } else if (a.build === "store") {
      if (a.traffic === "high") {
        out = "vps";
        why.push("A store under real traffic needs guaranteed resources — checkout slowing during a campaign is the expensive kind of slow.");
      } else if (a.admin === "none") {
        out = "managed-wp";
        why.push("Stores run on standard engines (WooCommerce & co.), so you're paying for reliability and support, not raw power — that's the managed tier's whole pitch.");
      } else {
        out = "shared";
        why.push("A modest store is a standard engine on a small site: shared hosting at renewal rates handles it fine.");
      }
      why.push("Store rule that outranks all of this: use a hosted payment processor so card data never touches your server.");
      move = "When checkout slows under real traffic, or the catalogue outgrows the plan's inode/CPU limits.";
    } else {
      /* CMS / standard engine */
      if (a.admin === "none") {
        out = "managed-wp";
        why.push("A standard CMS with nobody maintaining a server: the managed tier deletes an entire job — updates, staging, backups, caching.");
      } else if (a.budget === "zero") {
        out = "shared";
        why.push("Hard truth: there is no honest $0 tier for a server-side site. The cheapest safe start is shared hosting at renewal rates — or rethink as a static site and genuinely pay $0.");
      } else {
        out = "shared";
        why.push("A standard CMS is shared hosting's home turf — at renewal prices, ignoring unlimited-everything badges.");
      }
      if (a.traffic === "high") why.push("At 50k+ visits/month, skip the bottom shared tier: start managed or on a small VPS instead.");
      move = "When plugins turn into custom code, or neighbours on the server start hurting you — that's the VPS conversation.";
    }

    if (a.data !== "none") {
      why.push("You said the site holds " + (a.data === "strict" ? "regulated data or has residency rules" : "payments or personal data") + " — verify the provider's own compliance docs (PCI DSS, GDPR, or Nigeria's NDPA). This tool flags it; it cannot audit it.");
    }
    if (a.traffic === "high" && a.server === "custom" && a.budget === "open" && a.data === "strict") {
      why.push("Only at your corner of the map does a dedicated machine ($129–$450/month) enter the conversation — it buys whole-machine isolation, not speed.");
    }

    return { out: out, why: why, move: move };
  }

  function render() {
    mount.innerHTML = "";
    var card = el("div", "htl-card");
    if (state.step < QUESTIONS.length) {
      var q = QUESTIONS[state.step];
      card.appendChild(el("p", "htl-step", "Question " + (state.step + 1) + " of " + QUESTIONS.length));
      card.appendChild(el("p", "htl-q", q.q));
      var opts = el("div", "htl-opts");
      q.opts.forEach(function (o) {
        var b = el("button", "htl-opt", o.label + (o.note ? "<small>" + o.note + "</small>" : ""));
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
        var nav = el("div", "htl-nav");
        var back = el("button", null, "← Back");
        back.type = "button";
        back.addEventListener("click", function () { state.step -= 1; render(); });
        nav.appendChild(back);
        nav.appendChild(el("span", "htl-progress", "Nothing is stored or sent — the tool lives in this tab."));
        card.appendChild(nav);
      }
    } else {
      var d = decide(state.answers);
      var o = OUTCOMES[d.out];
      card.setAttribute("aria-live", "polite");
      var res = el("div", "htl-result");
      res.appendChild(el("p", "htl-step", "Your recommendation"));
      res.appendChild(el("h3", null, o.name));
      var whyTitle = el("p", null, "<b>Why — your answers, in order:</b>");
      res.appendChild(whyTitle);
      var ul = el("ul", "htl-why");
      d.why.forEach(function (w) { ul.appendChild(el("li", null, w)); });
      res.appendChild(ul);
      res.appendChild(el("p", "htl-cost", "<b>Honest cost:</b> " + o.cost + " Tax is on top and follows your billing address — see <a href=\"/tech/web-hosting-costs-explained/#countries\">what changes by country</a>."));
      res.appendChild(el("p", null, "<b>Move on when:</b> " + d.move));
      var links = el("div", "htl-links");
      o.links.forEach(function (l) {
        var a = el("a", null, l[1]);
        a.href = l[0];
        links.appendChild(a);
      });
      res.appendChild(links);
      var nav2 = el("div", "htl-nav");
      var again = el("button", null, "↺ Start over");
      again.type = "button";
      again.addEventListener("click", function () { state = { step: 0, answers: {} }; render(); });
      nav2.appendChild(again);
      res.appendChild(nav2);
      res.appendChild(el("p", "htl-privacy", "Prices are directional 2026 renewal rates (sources on the costs page) — never a quote. The tool made no network calls and stored nothing."));
      card.appendChild(res);
    }
    mount.appendChild(card);
  }

  render();
})();
