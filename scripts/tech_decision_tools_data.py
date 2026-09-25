# BRYME Tech — §16 interactive decision tools, batch 2.
# 25 September 2026. Two more "shows its working" decision tools:
#   /tech/which-cloud-service-model/  — SaaS / PaaS / IaaS / serverless / self-hosted
#   /tech/which-security-solution/    — consumer basics -> business AV/EDR -> phishing-first
#                                       -> MDR -> MSSP/co-managed -> website hardening
# Both follow the which-hosting-type pattern: deterministic rules in an external
# JS asset (site CSP blocks inline scripts), noscript decision tree in the page,
# reasoning rendered per answer, on-device only. Prices are SHAPES not quotes —
# no fabricated numbers (brief §11): consumer $0, per-user list pricing "single
# digits", MDR "hundreds per month, quote-based", MSSP "contract quotes".
# Jet-word alignment (§0.4): the security tool feeds the MDR/MSSP/phishing
# cluster — the desk's highest-CPC topical graph.

CLOUD_MODEL_SLUG = "which-cloud-service-model"
SECURITY_SLUG = "which-security-solution"

GUIDE_DATES = {
    CLOUD_MODEL_SLUG: ("2026-09-25", "2026-09-25"),
    SECURITY_SLUG: ("2026-09-25", "2026-09-25"),
}

CLOUD_BODY = """<div class="prose">
<p class="byline">BRYME Tech desk \u00b7 published 25 September 2026 \u00b7 the tool runs entirely in your browser \u2014 no answers are stored or sent anywhere</p>
<p><b>SaaS, PaaS, IaaS, serverless, or self-hosted \u2014 five words that decide who does the work.</b> The cloud isn\u2019t one thing; it\u2019s a ladder of \u201chow much do you want to run yourself.\u201d Climb it one rung too high and you\u2019re paying a provider to do a job you\u2019d never notice; one rung too low and you\u2019re the on-call sysadmin for a server you didn\u2019t want. Six questions place you on the right rung \u2014 and show which answers drove the call.</p>
<style>
.cm-card{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:20px 22px;max-width:760px}
.cm-step{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);margin:0 0 6px}
.cm-q{font-size:19px;font-weight:700;margin:0 0 14px;font-family:var(--serif)}
.cm-opts{display:flex;flex-direction:column;gap:8px}
.cm-opt{text-align:left;padding:11px 14px;border:1px solid var(--line-strong);border-radius:10px;background:var(--card);font:inherit;font-size:14.5px;cursor:pointer}
.cm-opt:hover,.cm-opt:focus-visible{border-color:var(--accent);background:var(--paper)}
.cm-opt small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.cm-nav{display:flex;gap:10px;margin-top:16px;align-items:center}
.cm-nav button{padding:8px 16px;border-radius:9px;border:1px solid var(--line-strong);background:var(--card);font:inherit;font-size:14px;cursor:pointer}
.cm-nav .cm-progress{font-size:12.5px;color:var(--dim);margin-left:auto}
.cm-result h3{margin:0 0 8px;font-family:var(--serif);font-size:22px}
.cm-why{margin:0 0 14px;padding-left:20px;font-size:14.5px}
.cm-why li{margin-bottom:6px}
.cm-cost{font-size:14px;border-left:3px solid var(--accent);padding:8px 12px;background:var(--paper);margin:0 0 14px}
.cm-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.cm-links a{font-size:13.5px;border:1px solid var(--line-strong);border-radius:999px;padding:6px 13px}
.cm-links a:hover,.cm-links a:focus-visible{border-color:var(--accent)}
.cm-privacy{font-size:12.5px;color:var(--dim);margin-top:14px}
</style>
<div id="cloud-model-tool"></div>
<noscript>
<p><b>The tool needs JavaScript. Here is the whole decision tree, statically:</b></p>
<ul>
<li><b>Someone already sells it as software</b> \u2192 <b>SaaS</b>. Buying beats building whenever the problem isn\u2019t your differentiator \u2014 <a href="/tech/build-vs-buy-the-honest-decision/">the honest build-vs-buy decision</a>.</li>
<li><b>Static site or docs</b> \u2192 <b>static hosting / free tiers</b> ($0 + domain).</li>
<li><b>Standard app, nobody wants to run servers</b> \u2192 <b>PaaS</b> (managed platform: you ship code, it runs it).</li>
<li><b>Custom infra needs, steady load, someone can run a server</b> \u2192 <b>IaaS</b> (virtual machines, flat cost) \u2014 <a href="/tech/aws-vs-azure-vs-gcp-choosing/">choosing between the big three</a>.</li>
<li><b>Spiky, event-shaped work</b> \u2192 <b>serverless</b> \u2014 but <a href="/tech/cloud-bill-why-it-spikes/">cap it, or a spike becomes an invoice</a>.</li>
<li><b>Strict data sovereignty, or the workload is steady and local anyway</b> \u2192 <b>self-hosted</b> \u2014 <a href="/tech/self-hosting-saas-when-its-worth-it/">when self-hosting is actually worth it</a>.</li>
</ul>
</noscript>
<script src="/assets/which-cloud-model-tool.js" defer></script>

<h2 id="why-six">Why the questions are shaped this way</h2>
<p>The whole ladder is one question repeated: <b>who does the work?</b> SaaS means the vendor runs everything including the software; PaaS runs the servers while you keep the code; IaaS rents raw machines; serverless rents outcomes per request; self-hosting keeps the work (and the control) in your building. So the tool asks what you\u2019re running, who can maintain it, how the load behaves, whether buying beats building, what it may hold, and what you can actually spend. Budget moves you along the rung you\u2019re on \u2014 it never changes which rung is honest.</p>

<h2 id="outcomes">The five rungs, and the shape of their cost</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Rung</th><th>Who does the work</th><th>Cost shape (directional)</th><th>The classic mistake</th></tr></thead>
<tbody>
<tr><td>SaaS</td><td>The vendor, all of it</td><td>Per-seat or per-month subscription</td><td>Building what you could rent \u2014 <a href="/tech/saas-pricing-models-explained/">pricing models explained</a></td></tr>
<tr><td>PaaS</td><td>Platform runs servers; you ship code</td><td>Usage-based, usually modest for small apps</td><td>Ignoring egress and build-minute meters</td></tr>
<tr><td>IaaS</td><td>You run the OS and up</td><td>Hourly/monthly, predictable if steady</td><td>Paying for idle capacity month after month</td></tr>
<tr><td>Serverless</td><td>Nobody, until a request arrives</td><td>Per-invocation; $0 when quiet</td><td>Uncapped concurrency \u2014 <a href="/tech/cloud-bill-why-it-spikes/">why cloud bills spike</a></td></tr>
<tr><td>Self-hosted</td><td>You, entirely</td><td>Hardware up front + your time forever</td><td>Underpricing your own labour \u2014 <a href="/tech/self-hosting-saas-when-its-worth-it/">when it\u2019s worth it</a></td></tr>
</tbody></table>
<p>Provider choice comes after the rung: <a href="/tech/aws-vs-azure-vs-gcp-choosing/">AWS vs Azure vs GCP, choosing honestly</a>. If the rung is SaaS, read <a href="/tech/saas-lock-in-and-data-portability/">lock-in and data portability</a> before signing, and keep the <a href="/tech/cloud-hosting/">whole cloud &amp; hosting cluster</a> one click away.</p>

<h2 id="limits">What this tool deliberately does not do</h2>
<ul>
<li><b>It doesn\u2019t pick a provider.</b> Rung first, provider second \u2014 every \u201cbest cloud\u201d list online skips that order.</li>
<li><b>It doesn\u2019t quote prices.</b> The shapes above are directional; your workload\u2019s maths decides. The <a href="/tech/web-hosting-costs-explained/">3-year cost method</a> applies to cloud too.</li>
<li><b>It doesn\u2019t phone home.</b> No analytics on your answers, no storage, no network calls.</li>
</ul>
</div>"""

SECURITY_BODY = """<div class="prose">
<p class="byline">BRYME Tech desk \u00b7 published 25 September 2026 \u00b7 the tool runs entirely in your browser \u2014 no answers are stored or sent anywhere</p>
<p><b>From free consumer basics to MDR \u2014 the honest ladder of \u201cwho\u2019s watching.\u201d</b> The security market sells acronyms: AV, EDR, MDR, MSSP, SIEM, zero trust. Underneath, every product answers one question \u2014 <b>when something goes wrong at 2am, who notices, and who responds?</b> Six questions place you on the right rung of that ladder, name what it actually buys, and show the price <em>shape</em> (real numbers are quote territory, and we won\u2019t invent them).</p>
<style>
.sec-card{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:20px 22px;max-width:760px}
.sec-step{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);margin:0 0 6px}
.sec-q{font-size:19px;font-weight:700;margin:0 0 14px;font-family:var(--serif)}
.sec-opts{display:flex;flex-direction:column;gap:8px}
.sec-opt{text-align:left;padding:11px 14px;border:1px solid var(--line-strong);border-radius:10px;background:var(--card);font:inherit;font-size:14.5px;cursor:pointer}
.sec-opt:hover,.sec-opt:focus-visible{border-color:var(--accent);background:var(--paper)}
.sec-opt small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.sec-nav{display:flex;gap:10px;margin-top:16px;align-items:center}
.sec-nav button{padding:8px 16px;border-radius:9px;border:1px solid var(--line-strong);background:var(--card);font:inherit;font-size:14px;cursor:pointer}
.sec-nav .sec-progress{font-size:12.5px;color:var(--dim);margin-left:auto}
.sec-result h3{margin:0 0 8px;font-family:var(--serif);font-size:22px}
.sec-why{margin:0 0 14px;padding-left:20px;font-size:14.5px}
.sec-why li{margin-bottom:6px}
.sec-cost{font-size:14px;border-left:3px solid var(--accent);padding:8px 12px;background:var(--paper);margin:0 0 14px}
.sec-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.sec-links a{font-size:13.5px;border:1px solid var(--line-strong);border-radius:999px;padding:6px 13px}
.sec-links a:hover,.sec-links a:focus-visible{border-color:var(--accent)}
.sec-privacy{font-size:12.5px;color:var(--dim);margin-top:14px}
</style>
<div id="security-solution-tool"></div>
<noscript>
<p><b>The tool needs JavaScript. Here is the whole decision tree, statically:</b></p>
<ul>
<li><b>Personal devices and household</b> \u2192 <b>consumer basics, $0</b>: built-in OS protection, a real password manager, 2FA everywhere, updated software. Paid suites mostly add support, not safety \u2014 <a href="/tech/your-security-checklist/">the checklist</a>.</li>
<li><b>Small business, nobody owns security, phishing is the fear</b> \u2192 <b>training-first</b>: business-grade antivirus plus a phishing-drill habit \u2014 <a href="/tech/phishing-training-that-actually-works/">training that actually works</a>.</li>
<li><b>Small business, nobody owns security, ransomware is the fear</b> \u2192 <b>business AV/EDR</b> on every endpoint, offline backups \u2014 <a href="/tech/three-two-one-backup-rule/">3-2-1 backups</a>.</li>
<li><b>You can\u2019t answer \u201cwho\u2019s watching at 2am?\u201d</b> \u2192 <b>MDR</b>: a team monitors, triages and responds for you \u2014 <a href="/tech/mdr-what-managed-detection-actually-buys/">what MDR actually buys</a>.</li>
<li><b>You have a dedicated security person</b> \u2192 <b>co-managed MSSP or in-house EDR/SIEM</b> \u2014 <a href="/tech/managed-security-service-provider-vs-mdr/">MSSP vs MDR</a>.</li>
<li><b>It\u2019s a website you\u2019re protecting</b> \u2192 <b>website hardening</b>: headers, WAF, DDoS absorption, backups \u2014 <a href="/tech/website-security-headers-explained/">security headers</a>, <a href="/tech/what-is-a-waf-website-firewall/">what a WAF does</a>.</li>
</ul>
</noscript>
<script src="/assets/which-security-tool.js" defer></script>

<h2 id="why-six">The one question every product answers</h2>
<p><b>Who notices, and who responds?</b> Consumer antivirus notices on one machine and tells a human. EDR notices across a fleet and can isolate a machine. MDR adds people: a team watches the alerts around the clock and responds with you. An MSSP wraps that in a broader managed service \u2014 firewalls, email, compliance reporting. Zero trust isn\u2019t a product at all; it\u2019s the direction of travel (<a href="/tech/zero-trust-explained-for-small-teams/">explained for small teams</a>). The tool asks what you\u2019re protecting, who owns security day-to-day, what you\u2019re most afraid of, whether 2am coverage matters, what compliance you carry, and your budget \u2014 because those six answers <em>are</em> the procurement decision, whatever the brochure says.</p>

<h2 id="outcomes">The rungs, and the shape of their price</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Rung</th><th>Who notices at 2am</th><th>Price shape (directional)</th><th>Start here</th></tr></thead>
<tbody>
<tr><td>Consumer basics</td><td>You, on one machine</td><td>$0 \u2014 built-in tools + free password manager</td><td><a href="/tech/your-security-checklist/">Security checklist</a></td></tr>
<tr><td>Business AV / EDR</td><td>Software, fleet-wide; a human reads the dashboard</td><td>Per user/month at list \u2014 commonly single digits</td><td><a href="/tech/mdr-what-managed-detection-actually-buys/">EDR vs MDR, explained</a></td></tr>
<tr><td>Training-first</td><td>Your people, drilled</td><td>Per user/month at list; free drills go far</td><td><a href="/tech/phishing-drill-five-real-lures/">Five real lures</a></td></tr>
<tr><td>MDR</td><td>A provider\u2019s team, around the clock</td><td>Hundreds per month, scales with endpoints \u2014 quote-based</td><td><a href="/tech/mdr-what-managed-detection-actually-buys/">What MDR buys</a></td></tr>
<tr><td>MSSP / co-managed</td><td>Shared: their SOC + your admin</td><td>Contract quotes</td><td><a href="/tech/managed-security-service-provider-vs-mdr/">MSSP vs MDR</a></td></tr>
<tr><td>Website hardening</td><td>Your host/CDN absorbs; you configure</td><td>$0\u2013low; free tiers are real</td><td><a href="/tech/ddos-protection-for-small-sites/">DDoS protection for small sites</a></td></tr>
</tbody></table>
<p>Compliance changes the paperwork, not the physics: <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">GDPR, CCPA and Nigeria\u2019s NDPA side by side</a>. And whatever rung you land on, assume breach: <a href="/tech/incident-response-plan-for-small-business/">a one-page incident response plan</a> is the cheapest security purchase that exists. The whole ladder lives in the <a href="/tech/cybersecurity/">cybersecurity cluster</a>.</p>

<h2 id="limits">What this tool deliberately does not do</h2>
<ul>
<li><b>It doesn\u2019t rank vendors.</b> Quote two or three providers at your rung; the difference between rungs dwarfs the difference between brands.</li>
<li><b>It doesn\u2019t invent prices.</b> MDR and MSSP pricing is genuinely quote-based; anyone quoting you exact figures without your endpoint count is guessing.</li>
<li><b>It doesn\u2019t certify compliance.</b> It flags obligations; documented process (not a product) is what satisfies a regulator.</li>
<li><b>It doesn\u2019t phone home.</b> No analytics on your answers, no storage, no network calls.</li>
</ul>
</div>"""

CLOUD_SOURCES = [
    ("NIST SP 800-145 - The NIST Definition of Cloud Computing", "https://csrc.nist.gov/pubs/sp/800/145/final"),
    ("BRYME Tech - AWS vs Azure vs GCP, choosing", "/tech/aws-vs-azure-vs-gcp-choosing/"),
    ("BRYME Tech - Why cloud bills spike", "/tech/cloud-bill-why-it-spikes/"),
]

SECURITY_SOURCES = [
    ("CISA - Zero Trust Maturity Model", "https://www.cisa.gov/zero-trust-maturity-model"),
    ("CISA - Small business cybersecurity", "https://www.cisa.gov/small-business"),
    ("BRYME Tech - What MDR actually buys", "/tech/mdr-what-managed-detection-actually-buys/"),
]

DECISION_TOOLS = [
(CLOUD_MODEL_SLUG, "web-and-hosting", "guide",
"Which cloud service model fits me? \u2014 SaaS, PaaS, IaaS, serverless or self-hosted",
"SaaS, PaaS, IaaS, serverless or self-hosted: six questions, one recommendation, reasoning shown \u2014 with the real cost shape of each rung. Runs on-device.",
CLOUD_BODY,
CLOUD_SOURCES,
[("aws-vs-azure-vs-gcp-choosing", "AWS vs Azure vs GCP, choosing honestly"),
 ("self-hosting-saas-when-its-worth-it", "Self-hosting SaaS: when it's worth it"),
 ("build-vs-buy-the-honest-decision", "Build vs buy: the honest decision"),
 ("cloud-bill-why-it-spikes", "Why cloud bills spike")]),
(SECURITY_SLUG, "safety", "guide",
"Which security solution do I need? \u2014 a decision tool for people, not procurement",
"From free consumer basics to MDR and MSSP: six questions, one rung of the ladder, reasoning shown, honest price shapes. Runs on-device, nothing stored.",
SECURITY_BODY,
SECURITY_SOURCES,
[("mdr-what-managed-detection-actually-buys", "What MDR actually buys"),
 ("managed-security-service-provider-vs-mdr", "MSSP vs MDR"),
 ("phishing-training-that-actually-works", "Phishing training that actually works"),
 ("your-security-checklist", "Your security checklist"),
 ("zero-trust-explained-for-small-teams", "Zero trust for small teams")]),
]
