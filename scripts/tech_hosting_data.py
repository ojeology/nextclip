# BRYME Tech — web hosting costs explained + the hosting decision tool.
# History: batch 47 (12 Sep 2026) built the costs guide + calculator
# (assets/hosting-cost-calculator.js). 25 Sep 2026 §2/§36 audit-first rework:
#   - SERP title reworked to the head query ("how much does web hosting cost")
#   - dead FAQPage + duplicate Article schema removed (brief §0.1 — dead since
#     May 2026); the template's single TechArticle remains, now with true dates
#     via GUIDE_DATES (published 12 Sep, updated 25 Sep 2026)
#   - duplicate body-level "Sources" H2 became "How these numbers were checked"
#   - new Section 6: what changes by country (brief §30 — UK VAT 20%, EU VAT
#     17–27% by country, AU GST 10%, Canada GST+province, Nigeria VAT 7.5%,
#     USD billing/FX reality; no invented prices)
#   - new §16 decision tool page /tech/which-hosting-type/ (quiz logic lives in
#     assets/which-hosting-type-tool.js — the site CSP blocks inline scripts)
# Figures are DIRECTIONAL 2026 rates from published pricing guides
# (ahosting.net Aug 2026; bearhost Hostinger tables Aug 2026;
# prestigetechnologies SMB guide Sep 2026) — labelled directional, editable in
# the tool, your cart decides. Desk byline (organizational, per convention).

HOSTING_SLUG = "web-hosting-costs-explained"
DECISION_SLUG = "which-hosting-type"

# Per-slug real dates (loop in build-ecosystem.py applies these to pub/upd so
# the TechArticle schema and byline stop disagreeing with each other).
GUIDE_DATES = {
    HOSTING_SLUG: ("2026-09-12", "2026-09-25"),
    DECISION_SLUG: ("2026-09-25", "2026-09-25"),
}

HOSTING_BODY = """<div class="prose">
<p class="byline">BRYME Tech desk \u00b7 published 12 September 2026 \u00b7 updated 25 September 2026 \u00b7 general information and directional rates \u2014 never a quote; your cart and invoice govern</p>
<p><b>The 60-second answer.</b> The price on a hosting homepage is almost never the price you\u2019ll pay. That <b>$2.79\u2013$3.99/month</b> banner is an <b>intro rate</b>, conditioned on prepaying 36\u201348 months up front \u2014 and it renews at <b>2\u20135\u00d7</b> (Hostinger\u2019s own tables: $2.99 intro \u2192 $10.99 renewal). The honest 2026 bands: shared hosting really costs <b>$9\u2013$16/month at renewal</b> (standard rates $9.79\u2013$13.79 are common), managed WordPress <b>$9\u2013$20</b>, VPS <b>$12\u2013$60</b>, dedicated <b>$129\u2013$450</b>. Add a domain at ~<b>$15/year</b> after year-one promos and email at <b>$0.39\u2013$1.99 per mailbox/month</b>, and a \u201c$3 a month\u201d website is really a <b>$150\u2013$300/year</b> commitment \u2014 priced honestly over three years, not from the banner. Tax is on top and follows your billing address (Section 6). Not sure which type of hosting you need in the first place? The <a href="/tech/which-hosting-type/">2-minute decision tool</a> narrows it down before you price anything.</p>
<p>The calculator below turns any plan into its true 3-year cost \u2014 the only number worth comparing between hosts.</p>

<h2 id="table">Section 1 \u00b7 What hosting really costs (2026 \u2014 directional)</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Type</th><th>Advertised (intro)</th><th>Renewal (the real price)</th><th>What you\u2019re buying</th></tr></thead>
<tbody>
<tr><td>Shared</td><td>$2\u2013$6/mo</td><td><b>$9\u2013$16/mo</b></td><td>A slice of a managed server; fine for most small sites</td></tr>
<tr><td>Managed WordPress</td><td>$2\u2013$8/mo</td><td><b>$9\u2013$20/mo</b></td><td>Shared resources + staging, auto-updates, tuned caching</td></tr>
<tr><td>VPS</td><td>$6\u2013$45/mo</td><td><b>$12\u2013$60/mo</b></td><td>Guaranteed CPU/RAM, root access; the jump happens at guaranteed resources, not a traffic number</td></tr>
<tr><td>Dedicated</td><td>$95\u2013$415/mo</td><td><b>$129\u2013$450/mo</b></td><td>A whole machine \u2014 rarely needed by small sites</td></tr>
</tbody></table>
<p class="lede" style="font-size:14px">Ranges from 2026 published pricing guides (ahosting.net, Aug 2026; bearhost\u2019s Hostinger tables, Aug 2026; prestigetechnologies SMB guide, Sep 2026) \u2014 directional, they change with sales and regions. Intro prices sit 50\u201370% below renewals by design. The side-by-side version lives in <a href="/tech/hosting-types-compared-shared-vps-cloud-dedicated/">hosting types compared: shared vs VPS vs cloud vs dedicated</a>.</p>

<h2 id="calculator">Section 2 \u00b7 The true-cost calculator (3-year view)</h2>
<style>
.hc-note{font-size:13px;color:var(--dim);margin:6px 0}
.hc-grid{display:flex;flex-wrap:wrap;gap:22px;border:1px solid var(--line-strong);border-radius:12px;padding:18px 20px;background:var(--sheet);max-width:760px}
.hc-fields{flex:1;min-width:250px;display:flex;flex-direction:column;gap:9px;font-size:14px}
.hc-fields label{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}
.hc-fields input,.hc-fields select{padding:7px 9px;border:1px solid var(--line-strong);border-radius:8px;font:inherit;font-size:14px;background:var(--card);width:110px}
.hc-fields select{width:auto}
.hc-out{flex:1;min-width:250px;overflow-x:auto}
.hc-out table{width:100%;border-collapse:collapse}
.hc-out td{padding:7px 6px;border-bottom:1px solid var(--line);font-size:14px}
.hc-out td.hc-trap-note{font-size:12.5px;color:var(--dim);text-align:left;white-space:normal;overflow-wrap:break-word;padding-top:2px}
.hc-disc{font-size:13px;color:var(--dim);max-width:760px;margin-top:10px}
</style>
<div id="hosting-cost-calc"></div>
<noscript><p><b>Static version:</b> true cost = (intro \u00d7 intro term) + (renewal \u00d7 remaining months) + domain \u00d7 years + (mailboxes \u00d7 mailbox price \u00d7 12) + one-offs. Compare hosts on that 3-year total, never on the banner.</p></noscript>

<h2 id="trap">Section 3 \u00b7 Why the renewal trap exists (and is legal)</h2>
<p>You\u2019re not being scammed \u2014 you\u2019re being given a <b>cash-flow discount</b>: prepay three or four years and the host funds today\u2019s server from tomorrow\u2019s money. The marketing problem is that the intro rate is the only number on the homepage. Three habits neutralise it:</p>
<ul>
<li><b>Price the renewal first.</b> If year 2+ isn\u2019t acceptable, the intro is irrelevant \u2014 no matter how big the percentage-off badge.</li>
<li><b>Match term to confidence.</b> The 48-month prepay is only a bargain if you\u2019d genuinely stay four years; 12-month terms cost a little more and keep you free.</li>
<li><b>Set the exit reminder now.</b> Calendar reminder two weeks before renewal: either negotiate (see Section 5) or migrate while the site is small.</li>
</ul>

<h2 id="sizing">Section 4 \u00b7 How much hosting do you actually need?</h2>
<ul>
<li><b>A static site or portfolio:</b> possibly <b>$0</b> \u2014 static hosts\u2019 free tiers are real (this very site runs on one; <a href="/tech/free-vs-paid-hosting/">free vs paid, honestly</a>).</li>
<li><b>A blog or small business site:</b> shared at renewal rates \u2014 ignore unlimited-everything badges; disk and \u201cunlimited traffic\u201d are rarely the constraint at this size.</li>
<li><b>A growing store or app:</b> the VPS jump buys <em>guaranteed</em> resources, not speed alone \u2014 pay it when neighbours-on-your-server actually hurt (<a href="/tech/what-is-a-vps-when-you-need-one/">what a VPS is and when you need one</a>).</li>
<li><b>Anything else:</b> upgrade when measured pain appears (<a href="/tech/why-your-website-is-slow/">measure slowness properly first</a>), not when a headline scares you.</li>
</ul>
<p>Prefer it the other way round? <a href="/tech/which-hosting-type/">Which hosting type do I need?</a> asks six questions, recommends one of five paths, and shows the reasoning \u2014 it runs entirely in your browser.</p>

<h2 id="hidden">Section 5 \u00b7 The add-ons that move the bill</h2>
<ul>
<li><b>Domain renewal:</b> ~$1 first-year promos reprice to ~<b>$15/year</b> \u2014 and transferring away can have its own fees (<a href="/tech/domain-names-explained/">what a domain name really is</a>).</li>
<li><b>Email mailboxes:</b> $0.39\u2013$1.99 per mailbox/month \u2014 five staff mailboxes can out-cost the hosting.</li>
<li><b>Backups and SSL:</b> many entry plans now include basic SSL (<a href="/tech/what-is-ssl-https/">what the padlock really means</a>); daily-backup add-ons are worth it only if you\u2019d pay a human to recreate the site without them.</li>
<li><b>Migration:</b> \u201cfree migration\u201d deals exist \u2014 price it if you\u2019re switching, and get the old host\u2019s exit terms in writing.</li>
</ul>
<p><b>Renewal-day negotiation, honestly:</b> the retention chat can offer real discounts to stop you leaving \u2014 it works more often than not, and costs five minutes. The credible alternative in your other tab is what makes it work.</p>

<h2 id="countries">Section 6 \u00b7 What changes by country (tax, currency, domains)</h2>
<p>The bands above are the global list-price reality, but three things follow your <b>billing address</b>, not the banner:</p>
<ul>
<li><b>Tax on the invoice.</b> Hosting is usually quoted tax-excluded, and sales tax is applied where you are billed: the <b>UK</b> adds 20% VAT; <b>EU</b> member states add their own VAT (currently 17\u201327% depending on country); <b>Australia</b> adds 10% GST; <b>Canada</b> adds 5% GST plus the provincial part (13\u201315% combined HST in participating provinces); <b>Nigeria</b> adds 7.5% VAT; <b>US</b> sales tax on digital services varies by state. A $10.99/mo plan is $13.19 at a UK checkout. Rates as of September 2026 \u2014 the checkout page is the authority.</li>
<li><b>Currency and card reality.</b> Most global hosts bill in <b>USD</b> wherever you live. If your bank account isn\u2019t in USD, expect conversion \u2014 and many cards add a foreign-transaction fee (commonly ~1\u20133%; check your card\u2019s terms). Nigerian cards face a second layer: banks apply their own naira exchange rate, with a spread. Where a host runs a local-currency storefront, it can beat the USD price after fees \u2014 compare at checkout, never at the banner.</li>
<li><b>The domain line.</b> Country domains price differently: .com renews around $15/year; .co.uk typically less; .ng and .com.ng register through Nigeria\u2019s NiRA-accredited registrars, in naira, with different renewal economics (<a href="/tech/domain-names-explained/">what a domain name really is</a>).</li>
</ul>
<p>Promos are regional and change constantly; the renewal maths is the same everywhere. Whatever your country, the honest comparison number is still the 3-year total \u2014 tax included, in the currency your card actually pays.</p>

<h2 id="faq">FAQ \u00b7 the questions that decide the bill</h2>
<p><b>How much does website hosting really cost per month?</b><br>
At renewal in 2026: shared $9\u2013$16, managed WordPress $9\u2013$20, VPS $12\u2013$60, dedicated $129\u2013$450. The $2\u2013$6 numbers you see advertised are intro rates on long prepays.</p>
<p><b>Why is renewal so much more expensive?</b><br>
The intro is a cash-flow discount for prepaying years ahead. Hosts publish renewal rates in their pricing tables \u2014 the 2\u20135\u00d7 jump is standard across the industry, not one company\u2019s trick.</p>
<p><b>How do I avoid the hosting renewal trap?</b><br>
Budget from the renewal price, choose the shortest term you\u2019d happily commit to, set a reminder two weeks before renewal, and negotiate or migrate at that point.</p>
<p><b>Is a VPS worth it over shared hosting?</b><br>
When you need guaranteed resources (real traffic spikes, background jobs, strict neighbours) \u2014 the renewal gap between upper shared and entry VPS is smaller than the ad gap suggests, so the decision is about predictability, not price.</p>
<p><b>What\u2019s the cheapest way to host a small website?</b><br>
A static site on a free-tier static host ($0), plus a domain at ~$15/year. Add paid hosting only when the site needs a server-side engine.</p>

<h2 id="method">How these numbers were checked</h2>
<p>Every band on this page comes from a published 2026 pricing guide, read in full \u2014 not from a search snippet, and not invented. The linked list under <b>Sources</b> below is the same three, clickable:</p>
<ul>
<li>ahosting.net \u2014 Website Hosting Cost Per Month 2026: intro from $2.79 (long prepay), standard shared $9.79\u2013$13.79; honest bands by plan type; VPS entry/renewal example (checked Aug 2026).</li>
<li>bearhost \u2014 Hostinger pricing 2026 tables: $2.99\u2192$10.99 web, $3.99\u2192$16.99 business, $6.49\u2192$11.99 VPS, $7.99\u2192$25.99 cloud; domain ~$14.99/yr renewal; email $0.39\u2013$1.99/mailbox (checked Aug 2026).</li>
<li>prestigetechnologies.com \u2014 SMB hosting 2026 guide: $3\u2013$15 intro / $10\u2013$20 renewal shared; VPS $20\u2013$100; dedicated $80\u2013$500+; intro 50\u201370% below renewal (checked Sep 2026).</li>
</ul>
<p class="byline">Reviewed 12 September 2026 \u00b7 updated 25 September 2026 \u00b7 prices are directional and promo-dependent \u00b7 no professional reviewer is claimed: general information, not a quote or purchase advice.</p>
</div>
<script src="/assets/hosting-cost-calculator.js" defer></script>"""

DECISION_BODY = """<div class="prose">
<p class="byline">BRYME Tech desk \u00b7 published 25 September 2026 \u00b7 the tool runs entirely in your browser \u2014 no answers are stored or sent anywhere</p>
<p><b>Six questions, one recommendation, and the reasoning shown.</b> Most \u201cwhich hosting\u201d content is a ranked list of sponsors. This is a decision tool: it asks what you\u2019re building, how it will be used, and what you\u2019re comfortable running \u2014 then names one of five paths (static free tier, shared, managed WordPress, VPS, or cloud), tells you <em>which of your answers</em> drove the call, and prices it at honest renewal rates instead of banner rates. If the answers change, the recommendation changes \u2014 that\u2019s the point.</p>
<style>
.htl-card{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:20px 22px;max-width:760px}
.htl-step{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);margin:0 0 6px}
.htl-q{font-size:19px;font-weight:700;margin:0 0 14px;font-family:var(--serif)}
.htl-opts{display:flex;flex-direction:column;gap:8px}
.htl-opt{text-align:left;padding:11px 14px;border:1px solid var(--line-strong);border-radius:10px;background:var(--card);font:inherit;font-size:14.5px;cursor:pointer}
.htl-opt:hover,.htl-opt:focus-visible{border-color:var(--accent);background:var(--paper)}
.htl-opt small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.htl-nav{display:flex;gap:10px;margin-top:16px;align-items:center}
.htl-nav button{padding:8px 16px;border-radius:9px;border:1px solid var(--line-strong);background:var(--card);font:inherit;font-size:14px;cursor:pointer}
.htl-nav .htl-progress{font-size:12.5px;color:var(--dim);margin-left:auto}
.htl-result h3{margin:0 0 8px;font-family:var(--serif);font-size:22px}
.htl-verdict{font-size:15.5px;margin:0 0 14px}
.htl-why{margin:0 0 14px;padding-left:20px;font-size:14.5px}
.htl-why li{margin-bottom:6px}
.htl-cost{font-size:14px;border-left:3px solid var(--accent);padding:8px 12px;background:var(--paper);margin:0 0 14px}
.htl-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.htl-links a{font-size:13.5px;border:1px solid var(--line-strong);border-radius:999px;padding:6px 13px}
.htl-links a:hover,.htl-links a:focus-visible{border-color:var(--accent)}
.htl-privacy{font-size:12.5px;color:var(--dim);margin-top:14px}
</style>
<div id="hosting-type-tool"></div>
<noscript>
<p><b>The tool needs JavaScript. Here is the whole decision tree, statically:</b></p>
<ul>
<li><b>No server-side code</b> (portfolio, landing page, docs, static blog generator) \u2192 <b>static free tier</b> \u2014 $0 + domain. Move when you need a CMS or server code.</li>
<li><b>WordPress or another standard CMS, no server admin</b> \u2192 <b>managed WordPress</b> ($9\u2013$20/mo renewal). Comfortable following setup guides and budget under $10 \u2192 plain <b>shared</b> ($9\u2013$16/mo renewal) works too.</li>
<li><b>Small store, modest traffic</b> \u2192 shared or managed, then a <b>VPS</b> when checkout slows under real traffic.</li>
<li><b>Custom server-side app, you can run a server</b> \u2192 <b>VPS</b> ($12\u2013$60/mo renewal) for steady load; <b>cloud</b> for spiky load \u2014 with an autoscaling cap, or a spike becomes an invoice (<a href="/tech/cloud-bill-why-it-spikes/">why cloud bills spike</a>).</li>
<li><b>Custom app, no server skills</b> \u2192 managed cloud/PaaS, and pay for the comfort knowingly.</li>
<li><b>Dedicated servers</b> ($129\u2013$450/mo) are rarely the right answer for a small site \u2014 they buy whole-machine isolation, not speed.</li>
</ul>
</noscript>
<script src="/assets/which-hosting-type-tool.js" defer></script>

<h2 id="why-six">Why these six questions (and not ten)</h2>
<p>Every hosting decision reduces to four facts \u2014 <b>what runs</b> (static files, a standard CMS, or custom server code), <b>how hard it works</b> (steady, spiky, or unknown traffic), <b>who maintains it</b> (your comfort with servers), and <b>what it may hold</b> (payments, personal data, residency rules). Budget decides which version of the answer you can afford, not which answer is true \u2014 so it\u2019s asked last, and it changes the tier, never the type. Anything beyond those is marketing.</p>

<h2 id="outcomes">The five outcomes, at honest prices</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Outcome</th><th>True cost (renewal)</th><th>Who it\u2019s for</th><th>Move on when</th></tr></thead>
<tbody>
<tr><td>Static free tier</td><td>$0 + domain ~$15/yr</td><td>Portfolios, landing pages, docs, static generators</td><td>You need a CMS or server-side code \u2014 <a href="/tech/where-to-host-website-for-free/">where to host free, and what free means</a></td></tr>
<tr><td>Shared</td><td>$9\u2013$16/mo</td><td>Blogs, small business sites, first stores</td><td>Neighbours slow you down, or you need software the panel won\u2019t install</td></tr>
<tr><td>Managed WordPress</td><td>$9\u2013$20/mo</td><td>CMS sites with no server admin in the house</td><td>Outgrowing plugins into custom code</td></tr>
<tr><td>VPS</td><td>$12\u2013$60/mo</td><td>Custom apps, steady load, guaranteed resources \u2014 <a href="/tech/what-is-a-vps-when-you-need-one/">what a VPS really is</a></td><td>Traffic gets spiky enough that flat provisioning wastes money</td></tr>
<tr><td>Cloud (elastic)</td><td>Usage-based; a small steady app often lands $10\u2013$50/mo</td><td>Spiky or growing workloads, autoscaling needs</td><td>Never, if you cap it \u2014 <a href="/tech/cloud-bill-why-it-spikes/">uncapped autoscaling is the exit</a></td></tr>
</tbody></table>
<p>All bands are renewal-rate reality, sourced on <a href="/tech/web-hosting-costs-explained/">the hosting costs page</a> \u2014 including the 3-year calculator and <a href="/tech/web-hosting-costs-explained/#countries">what changes by country</a> (tax, currency, domains). The full side-by-side lives in <a href="/tech/hosting-types-compared-shared-vps-cloud-dedicated/">hosting types compared</a>, and the honest starting point for $0 sites is <a href="/tech/free-vs-paid-hosting/">free vs paid hosting</a>. More paths through the money: the <a href="/tech/cloud-hosting/">cloud &amp; hosting cluster</a>.</p>

<h2 id="limits">What this tool deliberately does not do</h2>
<ul>
<li><b>It doesn\u2019t rank providers.</b> The right host depends on your region, stack and support needs \u2014 a six-question tool that pretends otherwise is an affiliate funnel.</li>
<li><b>It doesn\u2019t certify compliance.</b> If you handle payments or personal data, the tool flags it and points you to verify the provider\u2019s own compliance docs (PCI DSS, GDPR, NDPA) \u2014 it cannot audit them.</li>
<li><b>It doesn\u2019t phone home.</b> No analytics on your answers, no localStorage, no network calls \u2014 the whole thing is one script running in your tab.</li>
</ul>
</div>"""

HOSTING_SOURCES = [
    ("ahosting.net - Website Hosting Cost Per Month 2026", "https://www.ahosting.net/blog/website-hosting-cost-per-month-2026/"),
    ("bearhost - Hostinger pricing 2026", "https://bearhost.com/blogs/hostinger-pricing"),
    ("Prestige Technologies - SMB hosting 2026", "https://www.prestigetechnologies.com/blog/website-hosting-cost-for-small-business/"),
]

NEW_HOSTING_GUIDES = [
(HOSTING_SLUG, "web-and-hosting", "guide",
"How much does web hosting cost in 2026? \u2014 true prices, the renewal trap, and a 3-year calculator",
"Shared hosting really costs $9\u2013$16/mo at renewal, not the $3 banner. True 3-year costs by plan type, the renewal trap, hidden add-ons + a calculator.",
HOSTING_BODY,
HOSTING_SOURCES,
[("free-vs-paid-hosting", "Free vs paid hosting"),
 ("domain-names-explained", "Domain names, explained"),
 ("why-your-website-is-slow", "Why websites are slow"),
 ("which-hosting-type", "Which hosting type do I need?")]),
(DECISION_SLUG, "web-and-hosting", "guide",
"Which hosting type do I need? \u2014 a 2-minute decision tool that shows its working",
"Six questions, one hosting recommendation \u2014 with the reasoning shown: static free tier, shared, managed WordPress, VPS, or cloud, at honest renewal prices.",
DECISION_BODY,
HOSTING_SOURCES,
[("web-hosting-costs-explained", "How much does web hosting cost in 2026?"),
 ("hosting-types-compared-shared-vps-cloud-dedicated", "Hosting types compared"),
 ("free-vs-paid-hosting", "Free vs paid hosting"),
 ("what-is-a-vps-when-you-need-one", "What a VPS is and when you need one")]),
]
