# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 11 (2026-09-25).

The SaaS / software cluster — the last of the brief's named cluster heads.
Cannibalization check run first: the tools shelf is product-vs-product
comparisons (Canva/Photoshop/Grammarly alternatives) and subscriptions already
covers audit/trials, so this batch is the software-DECISION layer those assume —
how to choose SaaS, how pricing works, lock-in and exit, build-vs-buy, open
source, and self-hosting. No new product comparison, no duplicated trial piece.

International rule honoured (Section 30): tier-1 US/UK/CA/AU/NZ/EU/Nigeria;
where pricing or data-residency differ by jurisdiction the piece says so and
points at the dated official page rather than inventing a number. Educational,
no fabricated benchmarks or prices, honest framing.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE11_GUIDES = [

# ---------------------------------------------------------------- SAAS / SOFTWARE CLUSTER
("saas-free-vs-paid-how-to-choose", "tools", "guide",
"Choosing software: the honest way to decide between the free tier and paying",
"Free tiers are not charity — they are a funnel with a designed limit. Here is how to read that limit, and a repeatable way to decide whether paying is actually worth it.",
"""<p>Almost every piece of software now has a free tier and a paid one, and the choice between them is usually made on feeling. It can be made on evidence instead, once you understand that a free tier is not a gift — it is a deliberately limited sample designed to make you hit a wall and reach for your card. Reading where that wall is tells you whether you will ever hit it.</p>
<h2>Read the limit, not the feature list</h2>
<p>Free tiers restrict along a few predictable axes: number of users, volume (projects, files, requests), features held back, or support. Before anything else, find which axis the free tier limits and ask whether your real usage crosses it. A free tier that caps at three projects is fine if you run two; one that caps at a thousand requests is useless if you make a million. The honest question is not "is the paid version better" but "does the free version's specific limit actually bind me."</p>
<h2>Count the real cost of paying</h2>
<p>If the limit does bind, the decision becomes a cost one, and it is rarely the sticker price. Per-seat software multiplies by your team; annual billing is cheaper but locks you in; and the multi-year total is the number that matters, the same arithmetic as <a href="/tech/streaming-subscription-stacking-when-bundle-cheaper/">subscription stacking</a>. Add the cost of switching later — the lock-in explored in <a href="/tech/saas-lock-in-and-data-portability/">lock-in and data portability</a> — because a cheap tool you cannot leave is not cheap.</p>
<h2>The decision, in order</h2>
<p>First, does a genuinely free or open tool already do the job? The desk's <a href="/tech/free-software-alternatives/">free software alternatives</a> exist precisely because the paid default is often not the only option. Second, if you do need the paid tier, choose the lowest one that removes the limit that binds you — not the one with the most impressive feature list. And third, prefer tools that let you get your data out, so the decision is reversible. For recurring software spend specifically, the audit discipline in <a href="/tech/subscription-audit-that-actually-sticks/">a subscription audit that sticks</a> is how you stop the small paid tiers from quietly becoming the big line item.</p>""",
[],
["free-software-alternatives", "saas-lock-in-and-data-portability"]),

("saas-pricing-models-explained", "tools", "guide",
"SaaS pricing models explained: per seat, usage, flat and the traps in each",
"The pricing page is engineered, not neutral. Here is what per-seat, usage-based and flat pricing actually optimise for, and how to pick the model that suits how you really use the tool.",
"""<p>Software pricing feels like a menu but it is a set of incentives. Whether a tool charges per seat, by usage, or flat is not arbitrary — each model is chosen to maximise revenue from a particular kind of customer, and choosing the wrong one for your usage can quietly double your bill. Understanding the models lets you predict the cost instead of being surprised by it.</p>
<h2>The three common models</h2>
<p><strong>Per-seat</strong> charges for each person who can log in. It is predictable and suits teams where everyone genuinely uses the tool, but it punishes broad, occasional access — paying for fifty seats when ten people are active is waste. <strong>Usage-based</strong> charges for what you consume (requests, storage, compute). It aligns cost with value and is cheap when you are small, but it scales with success and can spike — the same dynamic as <a href="/tech/cloud-bill-why-it-spikes/">why cloud bills spike</a>, because it often <em>is</em> cloud underneath. <strong>Flat-rate</strong> charges one price regardless, which is simple and predictable but means light users subsidise heavy ones.</p>
<h2>The traps in each</h2>
<p>Per-seat hides cost in "viewer" and "admin" tiers and in minimums. Usage-based hides it in the metered unit — read what exactly is counted, because the thing that grows may not be the thing you expected. Flat-rate hides it in the ceiling: the plan is cheap until you cross into the next tier, where the price often jumps sharply. In every case the pricing page is optimised to make the common path look cheap; the honest move is to estimate your real usage on each axis and price that, not the headline.</p>
<h2>How to choose</h2>
<p>Match the model to your usage shape. A small team with steady, uniform use is usually cheapest per-seat. Spiky or fast-growing usage may be cheaper flat-rate until it is not. Variable, scale-driven usage suits usage-based — if you watch the meter. Whichever you pick, the multi-year total is the number to compare, the discipline in <a href="/tech/saas-free-vs-paid-how-to-choose/">choosing free vs paid</a>, and you should already know how hard it is to leave before you sign, which is the subject of <a href="/tech/saas-lock-in-and-data-portability/">lock-in and data portability</a>.</p>""",
[],
["cloud-bill-why-it-spikes", "saas-lock-in-and-data-portability"]),

("saas-lock-in-and-data-portability", "tools", "guide",
"Vendor lock-in and data portability: knowing your exit before you sign up",
"The most overlooked question in choosing software is how you leave. Here is what creates lock-in, why your data is the real asset, and the checks to run before committing.",
"""<p>People choose software by its features and its price, and almost never by how hard it is to leave. That is backwards, because the cost of a tool is not just what it charges while you stay — it is what it costs to get out. Lock-in is the gap between those two, and it is decided long before you ever want to switch.</p>
<h2>What actually creates lock-in</h2>
<p>Three things, in increasing severity. The mild kind is inconvenience — your team's habits and integrations are built around the tool. The real kind is your <em>data</em>: if your work lives in a proprietary format with no clean export, leaving means losing or painstakingly converting it. The severe kind is architectural — the software is so woven into your processes that removing it is a project, not a switch. The first is survivable; the last two are what turn a reasonable tool into a trap.</p>
<h2>The checks to run before you commit</h2>
<p>Ask, in writing, before you sign: can I export all my data, in an open or documented format, at any time? Is there an API so I am not dependent on the vendor's export button? What happens to my data if I cancel — is it deleted, retained, or held hostage? And how portable is the format — could another tool import it? A vendor that answers these crisply is confident; one that is vague about export is telling you something. These are the same questions behind the right-to-portability idea in <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">data security compliance</a>, applied commercially.</p>
<h2>Why it matters more than the monthly price</h2>
<p>Software changes: prices rise, features get cut, companies get acquired or shut down. The subscription creep that quietly raises costs is covered in <a href="/tech/subscription-audit-that-actually-sticks/">the subscription audit</a>; lock-in is what stops you acting on it. A slightly dearer tool you can walk away from is often the cheaper choice, because it keeps the decision reversible — the same logic as preferring local control in <a href="/tech/local-vs-cloud-smart-home-why-it-decides-everything/">the smart-home local-vs-cloud piece</a>. Choose for the exit as much as the entrance, and no single vendor ever owns you.</p>""",
[],
["data-security-compliance-gdpr-ccpa-ndpr", "subscription-audit-that-actually-sticks"]),

("build-vs-buy-the-honest-decision", "tools", "guide",
"Build it or buy it: the honest decision most teams get wrong in both directions",
"Building feels like control and buying feels like compromise, but the real cost of building is the years of maintenance nobody budgets for. Here is how to decide soberly.",
"""<p>Every team faces it: there is a tool you need, and you could buy it or build your own. The debate gets heated because both camps are half right. Building gives control and a perfect fit; buying gives speed and someone else's maintenance. The mistake is deciding on ideology instead of counting the real, long-term cost — which is almost always dominated by maintenance, not creation.</p>
<h2>The cost nobody budgets: keeping it alive</h2>
<p>Building the first version is the cheap part. The expensive part is every year after: fixing bugs, patching security holes (<a href="/tech/patch-management-for-humans/">patch management</a> now applies to software you own), keeping up with the platforms it runs on, adding the features users assume, and being on call when it breaks. A bought tool spreads that cost across all its customers; a self-built one concentrates it on you, forever. Most build-vs-buy decisions go wrong because the team priced the build and forgot the decade of upkeep.</p>
<h2>When building genuinely wins</h2>
<p>Build when the thing is core to what makes you different — your actual competitive edge, not a generic need. Build when nothing on the market fits a genuine, specific requirement and the fit is worth owning. Build when the data or logic is so sensitive it cannot leave your control, the same reasoning as <a href="/tech/local-vs-cloud-ai-running-models-on-your-own-hardware/">running AI locally</a>. For everything that is a commodity — auth, billing, analytics, a CRM — buying is almost always right, because you would be paying to reinvent something maintained by people who do nothing else.</p>
<h2>The sober test</h2>
<p>Ask: is this our secret sauce or our plumbing? Plumbing should be bought. And before building, price the maintenance honestly — who owns it in two years, when the person who wrote it has moved on? The middle path is often best: buy the commodity, build only the thin layer that is genuinely yours. Whichever way you go, know your exit — the lock-in question in <a href="/tech/saas-lock-in-and-data-portability/">lock-in and data portability</a> applies whether you build or buy, and the cost discipline is the same one as <a href="/tech/saas-pricing-models-explained/">reading SaaS pricing</a>.</p>""",
[],
["patch-management-for-humans", "saas-lock-in-and-data-portability"]),

("open-source-software-what-free-really-means", "tools", "guide",
"Open source: what 'free' actually means, and how the companies behind it make money",
"Open source is free as in freedom and often free as in price — but not free as in no-cost-to-run, and the projects are businesses. Here is the honest picture before you rely on one.",
"""<p>"Open source" is widely used and widely misunderstood. It does not simply mean free, and the projects you depend on are usually sustained by companies with real business models. Understanding both makes you a better user — you will rely on the right projects, support the ones worth supporting, and not be blindsided when a licence changes.</p>
<h2>What open source actually guarantees</h2>
<p>Open source means the source code is available under a licence that lets you inspect, use, modify and share it. That is freedom, and it brings real benefits: you can audit what the software does (a genuine security and privacy plus), you are not locked to one vendor, and the project can outlive any single company. It does not guarantee the software is free of charge, free of support cost, or free of the effort to run it — "free as in speech," not necessarily "free as in beer."</p>
<h2>How the projects make money</h2>
<p>Most substantial open source is backed by a company that monetises around the free core: paid enterprise support, hosted versions (the SaaS form of the same tool), premium features, or dual licensing. This matters to you because it explains the incentives — and the risk. A project can change its licence to pull features behind a paywall, or a company can shut down and the hosted version with it. The healthy ones are transparent about this; the sustainability question is the same one behind <a href="/tech/saas-lock-in-and-data-portability/">lock-in and portability</a>, because open code you can fork is the ultimate portability.</p>
<h2>When to choose it</h2>
<p>Open source is often the right call for infrastructure and tools where inspection and freedom matter, and where a free, well-maintained project beats a paid black box — the desk's <a href="/tech/free-software-alternatives/">free software alternatives</a> lean on exactly this. But apply the same sobriety as any software choice: check the project is actively maintained (an abandoned project is a security liability, per <a href="/tech/vulnerability-scanning-explained/">vulnerability scanning</a>), understand who sustains it, and know what running it will cost you in time. Free to download is not free to own — and the honest version of that trade is the whole decision.</p>""",
[],
["free-software-alternatives", "vulnerability-scanning-explained"]),

("self-hosting-saas-when-its-worth-it", "tools", "guide",
"Self-hosting your software: when owning the server beats paying the subscription",
"You can run many SaaS tools yourself, privately, for the cost of a small server. Here is the honest case for it, the real cost people forget, and when the cloud still wins.",
"""<p>For a growing list of tools — note apps, file sync, project boards, password managers, media servers — there is a self-hosted version you can run on your own hardware instead of paying a monthly fee. It is genuinely appealing: private, no subscription, no vendor deciding your price. It is also genuinely work, and the decision is the same local-versus-cloud trade-off that runs through this whole desk.</p>
<h2>What self-hosting buys you</h2>
<p>Control and privacy first: your data stays on your machine, which solves the exposure described in <a href="/tech/saas-lock-in-and-data-portability/">lock-in and portability</a> at a stroke — there is no vendor to be locked into. No recurring fee, no price rises, no service shutting down and taking your data with it. For sensitive data or for a tool you would otherwise rent forever, the economics can strongly favour owning it, the same reasoning as <a href="/tech/local-vs-cloud-ai-running-models-on-your-own-hardware/">running models locally</a>.</p>
<h2>The cost people forget: you become the IT department</h2>
<p>Self-hosting trades a subscription for responsibility. You run the server, so you own its uptime, its backups (the <a href="/tech/three-two-one-backup-rule/">3-2-1 rule</a> is now your problem), and above all its security — an internet-facing self-hosted app is a target, and keeping it patched is the discipline in <a href="/tech/patch-management-for-humans/">patch management</a> with real consequences. The honest cost is not the hardware; it is your time and the risk of running something unattended. For many people that is a bad trade; for the technically comfortable it is a good one.</p>
<h2>When the cloud still wins</h2>
<p>Use the hosted version when reliability just works and matters more than control, when you do not want to maintain a server, or when the tool needs to be reachable from everywhere without you opening ports and hardening a box. The decision mirrors <a href="/tech/what-is-a-vps-when-you-need-one/">when you need a VPS</a>: self-host when you specifically value the control and will do the upkeep; otherwise let someone else run it. There is no virtue in self-hosting for its own sake — only in matching the effort to how much the privacy and control are worth to you.</p>""",
[],
["saas-lock-in-and-data-portability", "three-two-one-backup-rule"]),

]
