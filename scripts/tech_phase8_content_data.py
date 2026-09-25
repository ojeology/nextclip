# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 8 (2026-09-25).

The cloud / hosting cluster — the brief's next-highest-leverage area (Section
0.4 cloud-infrastructure market context: real advertiser money chases this
content). Cannibalization check run first: free-vs-paid hosting, web-hosting
costs and render-vs-vercel-vs-netlify already exist and are linked, not
duplicated. These fill genuine gaps: hosting types, VPS, cloud bills, the big
three clouds, CDN, object storage.

International rule honoured (Section 30): tier-1 markets US/UK/CA/AU/NZ/EU/
Nigeria; where pricing, data-residency or availability differ by region the
piece says so and points to the dated official page rather than inventing a
number. Educational, no fabricated benchmarks or prices, honest framing.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE8_GUIDES = [

# ---------------------------------------------------------------- CLOUD / HOSTING CLUSTER
("hosting-types-compared-shared-vps-cloud-dedicated", "web-and-hosting", "guide",
"Shared vs VPS vs cloud vs dedicated: the hosting decision in plain terms",
"Four hosting types, four trade-offs. Here is the honest decision — what each really gives you, what it costs in effort, and the point where you should move up.",
"""<p>Every hosting decision reduces to one question: how much of the machine do you need, and how much work are you willing to do? Shared, VPS, cloud and dedicated sit on a line from "somebody else manages everything" to "you manage a physical server," and the right answer depends on your traffic, your tolerance for maintenance, and your budget. The <a href="/tech/free-vs-paid-hosting/">free vs paid hosting</a> piece covers the bottom of that line; this is the whole ladder.</p>
<h2>The four types, honestly</h2>
<p><strong>Shared hosting</strong> puts your site on a server with many others. It is cheap and hands-off, but noisy neighbours can slow you and you have little control — fine for a small brochure site, wrong for anything that spikes. <strong>A VPS</strong> (virtual private server) carves a guaranteed slice of a machine just for you: more power and control, still someone else's hardware. <strong>Cloud</strong> hosting spreads your workload across many machines that scale up and down — resilient and elastic, but the bill can surprise you (see <a href="/tech/cloud-bill-why-it-spikes/">why cloud bills spike</a>). <strong>Dedicated</strong> means a whole physical server: maximum control and performance, maximum cost and responsibility, and rarely worth it for a small site.</p>
<h2>The point where you move up</h2>
<p>Move from shared to a VPS when your site is consistently slow under load, when you need software shared hosting will not let you install, or when a neighbour's traffic keeps hurting you. Move toward cloud when your traffic is spiky or unpredictable and you would rather pay for what you use than provision for the peak. The <a href="/tech/web-hosting-costs-explained/">hosting costs</a> piece works through the money; the short version is that the cheapest tier is only cheap until it costs you uptime.</p>
<h2>The tier-1 caveat</h2>
<p>Pricing and what counts as "cheap" differ sharply by region and currency — a plan that is trivial in the US or UK is a real line item in Nigeria, and data-residency rules (covered in <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">data security compliance</a>) may require your server to sit in a specific jurisdiction. So treat any price as a starting point, check the provider's current page for your region, and choose the lowest tier that reliably handles your real load — not the one with the most impressive spec sheet.</p>""",
[],
["free-vs-paid-hosting", "web-hosting-costs-explained"]),

("what-is-a-vps-when-you-need-one", "web-and-hosting", "guide",
"What a VPS actually is, and the honest signs you have outgrown shared hosting",
"A VPS is a guaranteed slice of a server that is yours to control. Here is what that means in practice, when it is worth the step up, and when it is overkill.",
"""<p>"VPS" is thrown around as the obvious upgrade, but it is worth being clear about what you are actually buying. A virtual private server is one physical machine sliced by software into several isolated virtual servers; you rent one slice, with a guaranteed amount of CPU, memory and storage, and root access to do what you like with it. It sits between shared hosting (no control, shared resources) and a dedicated server (a whole machine, all the cost and admin).</p>
<h2>What the slice actually gives you</h2>
<p>Two things shared hosting does not: guaranteed resources and control. Your allocation is yours, so a noisy neighbour cannot starve your site. And you can install the software you need — a specific database version, a runtime, a tool — rather than living within a fixed panel. That control is the real reason to move; raw power is secondary. The mechanics of how a request reaches that server are in <a href="/tech/how-the-internet-works/">how the internet works</a> and <a href="/tech/what-is-dns/">what DNS is</a>.</p>
<h2>The honest signs you need one</h2>
<p>You have outgrown shared hosting when your site is reliably slow under normal traffic, when shared limits keep blocking software or connections you need, when you want to run something that is not just a website (a bot, an API, a self-hosted tool — including <a href="/tech/how-to-build-your-own-vpn-server/">your own VPN server</a>), or when you need consistent performance you can reason about. If none of those are true, a VPS is spending money and effort for headroom you will not use.</p>
<h2>The cost nobody mentions: it is yours to run</h2>
<p>A VPS hands you the keys, including the maintenance. You are responsible for updates and security — an unpatched, internet-facing server is a liability, which is exactly the discipline in <a href="/tech/patch-management-for-humans/">patch management</a>. Factor in that time, not just the monthly fee. For many small sites the saner answer is a managed platform that removes the server entirely, compared in <a href="/tech/render-vs-vercel-vs-netlify/">Render vs Vercel vs Netlify</a>; a VPS is the right call when you specifically need the control those platforms take away.</p>""",
[],
["free-vs-paid-hosting", "how-to-build-your-own-vpn-server"]),

("cloud-bill-why-it-spikes", "web-and-hosting", "guide",
"Why your cloud bill spiked (and the few settings that stop it)",
"Cloud bills rarely rise because you did more work — they rise because of egress, an orphaned resource, or a service left running. Here is how to find the cause fast.",
"""<p>The cloud bill that doubles overnight is a rite of passage, and it is almost never because your project got twice as busy. It is usually one of a few predictable culprits, and once you know them the bill becomes readable instead of frightening. This is the cost side of the hosting ladder in <a href="/tech/hosting-types-compared-shared-vps-cloud-dedicated/">hosting types compared</a>.</p>
<h2>The usual suspects</h2>
<p><strong>Egress</strong> — data leaving the cloud — is the classic surprise: storing data is cheap, but pulling it out (to users, to another provider, or a misconfigured sync) is metered and adds up fast. <strong>Orphaned resources</strong> are the next: a disk or IP left behind when you deleted the server it belonged to keeps billing. <strong>Something left running</strong> — a test instance, a database, a job that never stopped — accrues hours you forgot about. And <strong>autoscaling without a ceiling</strong> turns one traffic spike or one runaway loop into a very expensive day.</p>
<h2>How to find the cause quickly</h2>
<p>Every major provider breaks the bill down by service and by resource — go straight to that breakdown and sort by the largest month-on-month jump; the spike is almost always one line. Then look at egress specifically, list resources that are billed but idle, and check anything that scales automatically. The habit that prevents the next surprise is a budget alert set <em>before</em> the bill arrives, so a runaway is caught in hours rather than at month end.</p>
<h2>The structural fixes</h2>
<p>Cap autoscaling so a spike cannot become an open-ended charge. Tear down what you are not using, and automate the teardown of test environments. Keep an eye on egress by design — serve static assets through a CDN (the role explained in <a href="/tech/what-is-a-cdn-why-your-site-needs-one/">what a CDN does</a>) so repeated downloads do not bill as origin egress every time. And if the workload is steady rather than spiky, a flat-cost VPS is often far cheaper than elastic cloud — the trade-off worked through in <a href="/tech/web-hosting-costs-explained/">hosting costs</a>. The cloud is pay-for-what-you-use; the trick is making sure you are not paying for what you forgot.</p>""",
[],
["hosting-types-compared-shared-vps-cloud-dedicated", "web-hosting-costs-explained"]),

("aws-vs-azure-vs-gcp-choosing", "web-and-hosting", "guide",
"AWS vs Azure vs Google Cloud: choosing without the religion",
"The big three clouds are more alike than the fan camps admit. Here is the honest way to choose — by what you already use, what you are building, and the few real differences.",
"""<p>The "which cloud is best" argument is mostly tribal. AWS, Azure and Google Cloud together run the large majority of the world's cloud workloads, and for a typical project they can all do the job. The honest differences are not raw capability but fit: what you already depend on, what you are building, and a handful of genuine strengths. This is the comparison behind the market context in the brief — and the decision is calmer than the marketing suggests.</p>
<h2>Choose by what you already live in</h2>
<p>The strongest signal is your existing stack. A Microsoft shop — Windows Server, Active Directory, .NET — will find Azure integrates with what it already runs. A data-and-AI-heavy team often leans Google Cloud for its analytics and machine-learning heritage. AWS is the broadest and most mature, with the largest ecosystem of services, documentation and third-party tooling, which makes it the safe default when you do not have a strong pull the other way. For most small teams, "the one our tools and hiring pool already know" beats any benchmark.</p>
<h2>The real differences that matter</h2>
<p>Breadth and maturity (AWS leads), hybrid and enterprise-IT fit (Azure's strength), and data/AI tooling (Google's). Pricing is genuinely comparable at the headline level and genuinely complicated underneath — so do not choose on a list price; model your actual workload, and watch the egress trap covered in <a href="/tech/cloud-bill-why-it-spikes/">why cloud bills spike</a>, because data-transfer costs differ and can dominate.</p>
<h2>The tier-1 and the honest "do you even need one" caveat</h2>
<p>Region matters twice: latency and pricing vary by region, and data-residency law may require your data to stay in a jurisdiction — the GDPR/CCPA/NDPR map in <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">data security compliance</a> — so confirm the provider has a suitable region for your users, whether that is the US, UK/EU or Nigeria. And the most honest point: a huge number of projects do not need a hyperscale cloud at all. A simple site or small app is often cheaper and far simpler on a managed platform (<a href="/tech/render-vs-vercel-vs-netlify/">Render vs Vercel vs Netlify</a>) or a single <a href="/tech/what-is-a-vps-when-you-need-one/">VPS</a>. Reach for AWS, Azure or GCP when you need what only they offer — not because it sounds serious.</p>""",
[("AWS pricing", "https://aws.amazon.com/pricing/"), ("Azure pricing", "https://azure.microsoft.com/en-us/pricing/"), ("Google Cloud pricing", "https://cloud.google.com/pricing")],
["cloud-bill-why-it-spikes", "render-vs-vercel-vs-netlify"]),

("what-is-a-cdn-why-your-site-needs-one", "web-and-hosting", "guide",
"What a CDN actually does (and the small-site case for one)",
"A CDN serves copies of your site from servers near your visitors. Here is the plain mechanics, what it fixes, and why even a small or regional site benefits.",
"""<p>A CDN — content delivery network — is one of those terms that sounds like infrastructure only big sites need. It is not. At its simplest, a CDN keeps copies of your site's static files (images, scripts, styles, pages) on servers scattered around the world, and serves each visitor from the nearest one instead of from your single origin server. For a slow-loading or internationally-read site, it is often the cheapest large improvement available.</p>
<h2>The problem it solves</h2>
<p>Without a CDN, every visitor pulls from one place. A reader in Lagos hitting a server in Oregon waits for every request to cross the Atlantic — and the latency in <a href="/tech/why-your-website-is-slow/">why your website is slow</a> is often exactly this distance, not your code. A CDN puts a copy much closer to that reader, so the slow trans-oceanic trip happens once (origin to CDN) rather than once per visitor per file. It also takes load off your origin, which can lower your hosting tier and your egress bill — the cost link in <a href="/tech/cloud-bill-why-it-spikes/">why cloud bills spike</a>.</p>
<h2>What it fixes, and what it does not</h2>
<p>A CDN speeds up <em>static</em> content and absorbs traffic spikes; many also handle SSL and basic caching, complementing the HTTPS explained in <a href="/tech/what-is-ssl-https/">what SSL/HTTPS is</a>. It does not make a slow database query or a heavy server-rendered page fast — for that you fix the origin. So a CDN is a multiplier on an already-reasonable site, not a cure for a broken one.</p>
<h2>The small-site and tier-1 case</h2>
<p>For a small or regional site the case is strong and cheap: several CDNs have generous free tiers, and the win is largest exactly where the origin is far from the readers — a Nigerian or Indian audience served from a US or European origin sees the biggest gain. The one caveat is correctness: caching means you must handle invalidation when you update a file, or visitors see a stale version. Set sensible cache rules, purge on deploy, and a CDN becomes the simplest performance upgrade on this whole shelf.</p>""",
[],
["why-your-website-is-slow", "what-is-ssl-https"]),

("object-storage-explained-s3-r2", "web-and-hosting", "guide",
"Object storage explained: the cheap way to hold files (and the egress catch)",
"Object storage is where the internet keeps its files — S3, R2 and the rest. Here is what it is, what it is for, and the one cost difference that decides which you pick.",
"""<p>Object storage is the workhorse behind most of the files on the internet: the images, backups, videos and datasets that do not belong on a web server's disk. Instead of a folder tree on one machine, files are stored as flat "objects" in a "bucket," each with a unique key, served over HTTP and effectively unlimited in size. Amazon S3 defined the category; Cloudflare R2, Backblaze B2, Wasabi and others now compete on it.</p>
<h2>What it is good for</h2>
<p>Anything you write once and read many times, at scale: media for a website or app, user uploads, backups (the off-site copy in the <a href="/tech/three-two-one-backup-rule/">3-2-1 backup rule</a>), logs and datasets. It is durable — providers replicate objects across machines — and it costs a fraction of keeping that data on a server's disk. It is not a filesystem: there is no real folder hierarchy and no in-place editing, so it suits storage and delivery, not a working directory.</p>
<h2>The cost difference that actually decides it</h2>
<p>Storing data is cheap and similar across providers; the real differentiator is <strong>egress</strong> — what you pay to pull data back out. The incumbents charge meaningfully for egress, which is the same trap described in <a href="/tech/cloud-bill-why-it-spikes/">why cloud bills spike</a>; several newer providers built their whole pitch on cheap or zero egress. So the honest way to choose is to estimate how often the data will be read, not just how much you will store: a write-once archive and a hot, frequently-served media bucket have opposite economics.</p>
<h2>The practical pairing</h2>
<p>Object storage almost always pairs with a CDN — put the bucket behind a CDN and visitors pull from a nearby cache instead of billing origin egress every time, the mechanism in <a href="/tech/what-is-a-cdn-why-your-site-needs-one/">what a CDN does</a>. For the static half of a site this combination is cheap and fast; the hosting decision around it is the one in <a href="/tech/hosting-types-compared-shared-vps-cloud-dedicated/">hosting types compared</a>. As ever, prices differ by region and change often, so check the provider's current page for your jurisdiction rather than trusting a remembered number.</p>""",
[("Cloudflare R2 — zero egress fees", "https://www.cloudflare.com/developer-platform/r2/"), ("Amazon S3 pricing", "https://aws.amazon.com/s3/pricing/")],
["three-two-one-backup-rule", "what-is-a-cdn-why-your-site-needs-one"]),

]
