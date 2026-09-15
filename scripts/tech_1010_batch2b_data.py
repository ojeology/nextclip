# -*- coding: utf-8 -*-
"""BRYME Tech — 10/10 research brief, batch 2b (Tier 1 #5: hosting comparison).

Verification receipts (2026-09-15):
- ALL pricing figures taken from the platforms' own pricing pages on 15 Sep 2026:
  render.com/pricing (Hobby $0, 5GB bandwidth, 25 services; Pro $25, 25GB;
  free web service 512MB; paid compute from $7/mo), vercel.com/pricing (Hobby $0,
  100GB/mo fast data transfer, 1M edge requests, 4hrs fluid CPU, 1 seat;
  Pro $20/mo), netlify.com/pricing (Free 300 credit limit/mo; production deploy
  15 credits; bandwidth 20 credits/GB; Personal $9/mo 1,000 credits;
  Pro $20/mo unlimited members from 3,000 credits).
- The credit arithmetic (300 credits = ~15GB pure bandwidth OR ~20 production
  deploys) is stated AS arithmetic from Netlify's own per-unit credit table,
  not as a marketing claim.
- Vercel Hobby commercial-use restriction phrased as "personal, non-commercial
  projects" per Vercel's own positioning; readers pointed at the terms.
- First-hand claim is real: this site deploys on Render's free tier — the
  linked deploy post-mortems are the evidence.
- No "best platform" verdict. Decision conditions only.
"""

HOSTING_1010_B2 = [

    ("render-vs-vercel-vs-netlify", "web-and-hosting", "guide",
     "Render vs Vercel vs Netlify in 2026: the comparison that starts with your project",
     "Every number here was read off the three platforms' own pricing pages on 15 September 2026 — and the honest answer is a decision tree, not a winner. From a desk whose site actually runs on Render.",
     """<p>Comparisons of these three platforms usually fail in the same way: they recycle last year's free-tier numbers (the numbers have moved a lot), then crown a winner that depends entirely on a project the reader doesn't have. So here are the ground rules for this one: every figure below comes from the platform's own pricing page, checked 15 September 2026; free tiers are compared because that's where the real differences live; and the conclusion is a decision tree, because the right answer genuinely depends on what you're deploying. One more disclosure that matters: <em>this site runs on Render's free tier</em> — <a href="/tech/render-static-deploy/">the deploy is documented here</a>, including what broke — so our first-hand experience is deepest on that platform, and we've said so wherever it shows.</p>

<h2>The 2026 numbers, first-party and dated</h2>
<p><b>Render</b> — Hobby plan, $0/month: up to 25 services, <b>5 GB of bandwidth included</b> per workspace (then metered), global CDN, custom domains, single-service previews. Pro is $25/month with 25 GB included and unlimited seats. Compute is separate: free web services exist (512 MB RAM, with spin-down after inactivity), paid instances start at $7/month, and managed Postgres/Redis/cron run in the same workspace.</p>
<p><b>Vercel</b> — Hobby plan, $0/month, positioned for personal, non-commercial projects: <b>100 GB/month of fast data transfer included</b>, 1M edge requests, 4 hours of Fluid compute, 1M function invocations, unlimited deployments, one developer seat. Pro is $20/month/seat with $20 of included usage credit and the flat-rate CDN. Commercial use on the free tier isn't what the Hobby plan is for — check the terms before putting a business on it.</p>
<p><b>Netlify</b> — Free plan, $0/month, <b>300 usage credits per month</b>. The credit math from their own table: a production deploy costs 15 credits, bandwidth costs 20 credits per GB, web requests 2 credits per 10k. So the whole free pool is <em>either</em> about 20 production deploys, <em>or</em> about 15 GB of bandwidth, <em>or</em> a mix — one shared pool for everything. Personal ($9/month) includes 1,000 credits; Pro ($20/month, unlimited members) starts at 3,000.</p>
<p>Notice what changed over the years: Netlify moved from generous separate quotas to the shared credit pool, and Render's free bandwidth tightened from earlier eras. If you read a comparison citing 100 GB free on all three, it's recycling 2024. The numbers above will drift too — <a href="/tech/free-vs-paid-hosting/">that drift is exactly why the free-vs-paid question needs re-checking</a>, and why we date every figure.</p>

<h2>What each platform is actually built around</h2>
<p><b>Vercel</b> is built around frontend frameworks — Next.js above all. If your project <em>is</em> a Next.js app, the integration (ISR, image optimisation, edge middleware, preview deploys per pull request) is the deepest of the three, and the free compute allowance is real. The trade: the free tier's seat count, commercial restrictions and the overage-pricing model mean the moment the project grows up, it becomes a paid conversation.</p>
<p><b>Netlify</b> is built around the Jamstack workflow — deploy previews, branch deploys, forms, functions, instant cache invalidation. The workflow polish is excellent; the credit pool is the discipline. For a site that deploys often and serves moderate traffic, the arithmetic above is the whole story: it's easy to compute exactly when the free tier runs out, which is honest but unforgiving.</p>
<p><b>Render</b> is built around running <em>everything together</em>: static sites, web services, workers, managed Postgres, Redis and cron in one workspace. The static-site free tier is simple (static sites are free; bandwidth is the 5 GB pool), and the superpower is that the backend your frontend needs is a sibling service, not a separate platform. The trade: free web services spin down after inactivity and take a moment to wake, the free bandwidth pool is the smallest of the three, and the frontend-framework niceties (per-PR preview ecosystems, image pipelines) are leaner than Vercel's.</p>

<h2>The decision tree</h2>
<p><b>Pure static site, modest traffic, simple needs?</b> Honestly, all three work — and so do the options we've compared separately: <a href="/tech/where-to-host-website-for-free/">GitHub Pages and Cloudflare Pages</a>, where unmetered static bandwidth can beat all three free tiers at once. Start there if the site is just files.</p>
<p><b>A Next.js (or heavy React) app?</b> Vercel's framework integration is the reason it exists; the free tier's 100 GB covers a lot of traffic. Have the commercial-use conversation before the project earns money.</p>
<p><b>A Jamstack site with functions, forms, lots of PR previews?</b> Netlify's workflow is the most polished. Budget the credits: multiply your deploys-per-month by 15, your expected GB by 20, and see whether free is realistic or whether $9 Personal is the honest plan.</p>
<p><b>A real backend — API server, database, background jobs?</b> Render is the only one of the three where the static frontend and the long-running backend (with managed Postgres and cron) live as first-class siblings. This site's own architecture — static pages served alongside a Node server with security headers and routing — is exactly that shape, and <a href="/tech/render-deployment-failures-what-they-taught-me/">the failures we documented</a> taught us the platform's sharp edges honestly.</p>
<p><b>Watching bandwidth above all?</b> The 2026 free-tier order for included transfer is Vercel 100 GB &gt; Netlify ~15 GB-equivalent &gt; Render 5 GB. If a static site is your shape and traffic is your constraint, Cloudflare Pages' unmetered static bandwidth changes the question entirely — that's a <a href="/tech/web-hosting-costs-explained/">hosting-costs conversation</a>, not a loyalty one.</p>

<h2>The migration tax nobody prices in</h2>
<p>Whichever you pick, the cost of switching later is real but survivable: DNS is the piece that takes patience — <a href="/tech/custom-domain-dns-order/">the order you move records in matters</a> — and the deploy pipeline is usually a re-connect-the-repo afternoon. What doesn't transfer cleanly is platform-specific glue (Netlify function shims, Vercel rewrites, Render's blueprint). Keep the build framework-native and the platform config thin, and you keep the exit cheap. That discipline is why this site could move hosts if the bandwidth math ever demanded it — the build is plain HTML and a Node server, no platform lock-in to speak of.</p>

<h2>The honest closing</h2>
<p>There is no winner here. There are three well-run platforms with sharply different free-tier shapes: Vercel's is the most generous for non-commercial frontends, Netlify's is the most predictable and the most finite, Render's is the narrowest on bandwidth but the only one that treats your backend as a first-class citizen. Pick by project shape, check the pricing page on the day you decide — not this article, not a forum — and re-check it whenever your traffic changes by an order of magnitude. Checked figures age; the decision tree doesn't.</p>

<p><b>Official sources (checked 15 September 2026):</b> render.com/pricing · vercel.com/pricing · netlify.com/pricing. Free-tier behaviour (spin-down, credit metering) per each platform's documentation pages.</p>""",
    [("Render — official pricing (checked 15 Sep 2026)", "https://render.com/pricing"),
     ("Vercel — official pricing (checked 15 Sep 2026)", "https://vercel.com/pricing"),
     ("Netlify — official pricing and credit table (checked 15 Sep 2026)", "https://www.netlify.com/pricing/")],
    [("render-static-deploy", "The Render static deploy walkthrough"),
     ("render-deployment-failures-what-they-taught-me", "What Render failures taught us"),
     ("free-vs-paid-hosting", "Free vs paid hosting"),
     ("where-to-host-website-for-free", "Where to host for free"),
     ("web-hosting-costs-explained", "Web hosting costs explained")]),
]
