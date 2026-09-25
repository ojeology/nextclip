# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 10 (2026-09-25).

Website security + networking cluster — finishes the security "ground zero" and
pairs with the cybersecurity cluster. Cannibalization check run first: CSP,
SSL/HTTPS, home-wifi-security-audit, public-wifi, router firmware and
port-forwarding already exist and are linked, not duplicated. These fill real
gaps: security headers beyond CSP, DDoS, WAF, vulnerability scanning, DNS
privacy, and segmenting a home network.

International rule honoured (Section 30): tier-1 US/UK/CA/AU/NZ/EU/Nigeria;
nothing fakes a jurisdiction-specific claim. Educational, no fabricated
benchmarks or prices, honest framing.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE10_GUIDES = [

# ---------------------------------------------------------------- WEBSITE SECURITY + NETWORKING
("website-security-headers-explained", "web-and-hosting", "guide",
"Website security headers explained: the few lines that block whole attack classes",
"A handful of HTTP response headers stop clickjacking, MIME sniffing and worse — and most small sites send none of them. Here is what each does and the sane starter set.",
"""<p>Most of website security is unglamorous configuration, and few things are as high-value-per-effort as HTTP security headers. They are a few lines your server adds to every response, and each one switches off a whole class of attack in the browser. The <a href="/tech/csp-safe-front-end/">CSP piece</a> covers the most powerful of them; this is the rest of the set and why each earns its place.</p>
<h2>The starter set worth sending</h2>
<p><strong>Strict-Transport-Security (HSTS)</strong> tells browsers to only ever use HTTPS for your site, closing the window where a first request could be intercepted — the natural partner to <a href="/tech/what-is-ssl-https/">what SSL/HTTPS is</a>. <strong>X-Content-Type-Options: nosniff</strong> stops the browser guessing a file's type, which blocks a classic way malicious uploads get executed. <strong>X-Frame-Options</strong> (or CSP's frame-ancestors) prevents your page being embedded in an invisible frame, which is how clickjacking tricks people into clicking things they did not mean to. <strong>Referrer-Policy</strong> limits how much of your URLs leak to other sites. Together they are a few lines and remove a surprising amount of attack surface.</p>
<h2>Why small sites skip them — and shouldn't</h2>
<p>They are invisible when working, so they are easy to forget, and they can break things if set carelessly (a strict CSP or HSTS applied too fast will lock you out or break a feature). So add them gradually, test each, and start with the safe ones. The payoff is disproportionate: these headers defend every visitor on every page for the cost of a configuration change, and they are a basic signal of a site that is maintained — which matters to the trust side of <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">data security compliance</a> too.</p>
<h2>How to check yours</h2>
<p>You do not need to guess: open your site's response headers in the browser's developer tools, or run a free header-scanning service, and see which of the set you actually send. Most small sites send none, which means adding them is almost always a pure improvement. Treat them as part of the same routine as <a href="/tech/patch-management-for-humans/">patch management</a> — quiet, boring, and the reason the dramatic breaches happen to someone else.</p>""",
[("MDN — HTTP security headers", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers#security")],
["csp-safe-front-end", "what-is-ssl-https"]),

("ddos-protection-for-small-sites", "web-and-hosting", "guide",
"DDoS protection for a small site: what actually helps and what is overkill",
"You probably do not need an enterprise scrubbing centre. Here is what a distributed flood actually is, what realistically protects a small site, and what to ignore.",
"""<p>"DDoS" sounds like something that only happens to banks and governments, but small sites get hit too — sometimes deliberately, often as collateral. The good news is that for almost every small site the defence is not an expensive appliance; it is mostly a matter of being on the right infrastructure and not panicking. Understanding what the attack is tells you what actually helps.</p>
<h2>What a DDoS attack actually is</h2>
<p>A distributed denial-of-service attack floods your site with more requests than it can handle, from many machines at once, so real visitors cannot get through. It is about <em>volume</em>, not intrusion — the attacker is not stealing data, they are trying to make the site unavailable. That distinction matters: the defences are about absorbing or filtering traffic, not about locks and keys.</p>
<h2>What realistically protects a small site</h2>
<p>The single most effective step is putting the site behind a CDN or reverse proxy, which absorbs and filters a huge amount of junk before it reaches your server — the same CDN that speeds up your site in <a href="/tech/what-is-a-cdn-why-your-site-needs-one/">what a CDN does</a> also hides your origin and soaks up floods. A web application firewall (<a href="/tech/what-is-a-waf-website-firewall/">what a WAF is</a>) adds request filtering on top. And being on hosted or cloud infrastructure that can scale helps, because a fixed single server is the easiest target. For most small sites, "behind a reputable CDN with its DDoS mitigation on" is 90% of the answer.</p>
<h2>What is overkill, and what to do during an attack</h2>
<p>Dedicated scrubbing services and enterprise contracts are for sites that are targeted repeatedly at scale — not for a blog or a small shop. If you are hit, the practical moves are boring: let the CDN absorb it, do not keep restarting your server (it will just be flooded again), and contact your host or provider, who often have mitigation you can enable. And keep the basics solid — <a href="/tech/website-security-headers-explained/">security headers</a>, <a href="/tech/patch-management-for-humans/">patches</a> — because the goal of most small attackers is disruption, and a site that is resilient and uninteresting is left alone.</p>""",
[("CISA — DDoS quick guide", "https://www.cisa.gov/topics/cyber-threats-and-advisories/denial-service")],
["what-is-a-cdn-why-your-site-needs-one", "what-is-a-waf-website-firewall"]),

("what-is-a-waf-website-firewall", "web-and-hosting", "guide",
"What a WAF (web application firewall) is, and whether a small site needs one",
"A WAF filters the requests your site actually receives, blocking the attacks that target your application rather than your network. Here is what it does and when it is worth turning on.",
"""<p>A regular firewall guards a network's edges; a web application firewall guards your website specifically. It sits in front of your site and inspects each incoming HTTP request, blocking the ones that look like attacks before they reach your application. For a small site the question is not whether a WAF is good — it is whether you need one separately, or whether the one bundled with your CDN and host already covers you.</p>
<h2>What it actually blocks</h2>
<p>A WAF filters application-layer attacks: SQL injection (tricking your database), cross-site scripting (injecting malicious script into your pages), malicious bots, and request patterns that no legitimate visitor would send. It is a different job from DDoS mitigation, which handles raw <em>volume</em> (<a href="/tech/ddos-protection-for-small-sites/">DDoS protection</a>); a WAF handles malicious <em>content</em>. Many small sites benefit from both, and both are usually features of the same product.</p>
<h2>You may already have one</h2>
<p>This is the key point for small sites: if your site is behind a major CDN or a managed host, a basic WAF is very often already there, sometimes just switched off. So before buying anything, check what your provider includes and enable it. A dedicated enterprise WAF with custom rule-tuning is for large or high-risk applications; a small site usually needs the bundled one turned on and left at sensible defaults, not a separate purchase.</p>
<h2>What a WAF is not</h2>
<p>It is not a substitute for a secure application. A WAF catches common patterns, but it cannot fix a fundamental vulnerability in your code, and a determined attacker may find a path around it. So it is one layer, not the whole defence — the layer that sits alongside <a href="/tech/website-security-headers-explained/">security headers</a>, keeping software patched (<a href="/tech/patch-management-for-humans/">patch management</a>), and the zero-trust mindset of verifying rather than assuming (<a href="/tech/zero-trust-explained-for-small-teams/">zero trust for small teams</a>). Turn on what your provider already gives you, and treat it as a net that catches the common case — not a reason to stop writing careful code.</p>""",
[("OWASP — web application security", "https://owasp.org/www-project-web-security-testing-guide/")],
["ddos-protection-for-small-sites", "website-security-headers-explained"]),

("vulnerability-scanning-explained", "web-and-hosting", "guide",
"Vulnerability scanning explained: finding the open door before someone else does",
"You do not need a red team to find the obvious holes. Here is what a vulnerability scan is, what it will and will not tell you, and the light version any small site can run.",
"""<p>Most successful attacks do not use a clever zero-day; they walk through a door that was left open and could have been found by anyone who looked. A vulnerability scan is exactly that act of looking at your own systems first — checking for the known, findable weaknesses before an attacker runs the same check against you.</p>
<h2>What a scan does</h2>
<p>A scanner probes your site, server or network and compares what it finds against a large database of known weaknesses: outdated software with published flaws, misconfigurations, missing <a href="/tech/website-security-headers-explained/">security headers</a>, exposed services, weak settings. It produces a prioritised list, which is far more useful than a vague worry. It is the diagnostic counterpart to <a href="/tech/patch-management-for-humans/">patch management</a>: patching fixes the holes, scanning tells you which ones you have.</p>
<h2>What it will not tell you</h2>
<p>A scan finds <em>known</em>, detectable issues — it is not a substitute for a human penetration test, and it will not catch a logic flaw unique to your application or a clever chained attack. So treat a clean scan as "no obvious open doors," not "secure." The honest expectation is that it catches the common, automatable problems that account for most real-world break-ins, which is precisely why running one is worth it.</p>
<h2>The light version any small site can run</h2>
<p>You do not need an enterprise platform. Free and low-cost scanners can check a website for headers, TLS problems and known vulnerabilities; your host may offer one; and the simplest version is a periodic check of your own dependencies and software versions against their security advisories. Scan on a schedule rather than once, because new weaknesses are found in software you already run — the same rhythm as the rest of this cluster. Find the door, close it, and check again; that loop is most of practical website security.</p>""",
[("OWASP — vulnerability scanning", "https://owasp.org/www-project-vulnerability-scanning-tools/")],
["patch-management-for-humans", "website-security-headers-explained"]),

("what-is-dns-over-https-private-dns", "web-and-hosting", "guide",
"DNS-over-HTTPS and private DNS: stopping the part of your browsing everyone can see",
"Even on HTTPS, the plain DNS lookup leaks every site you visit to whoever runs the network. Here is what encrypted DNS fixes, what it does not, and how to turn it on.",
"""<p>HTTPS encrypts what you send to a website, but it does not hide <em>which</em> websites you ask for. That lookup — turning a name like a bank into an address — traditionally happens in plain DNS, visible to your ISP, the café Wi-Fi, and anyone watching the network. Encrypted DNS closes that gap, and it is one of the easiest privacy wins available.</p>
<h2>The leak it fixes</h2>
<p>As explained in <a href="/tech/what-is-dns/">what DNS is</a>, every site you visit starts with a DNS query, and in the old model that query is unencrypted. So even though the contents of your banking session are private, the fact that you visited your bank is not — and on <a href="/tech/public-wifi-risks/">public Wi-Fi</a> that list is trivially readable. DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) wrap those lookups in encryption, so the network sees that you are using DNS but not the names.</p>
<h2>How to turn it on</h2>
<p>It is built into modern systems: browsers and operating systems now have a "secure DNS" or "private DNS" setting, and Android calls it Private DNS. Enable it and point at a reputable resolver. If it seems to break something, the cause is usually a network that expects to intercept DNS — the troubleshooting is the same ground as <a href="/tech/private-dns-not-working/">private DNS not working</a> and <a href="/tech/dns-problems-diagnosed/">DNS problems diagnosed</a>.</p>
<h2>What it does not do</h2>
<p>Be honest about the limits. Encrypted DNS hides your lookups from the <em>network</em>, but the resolver you choose can now see them — so you are moving trust from your ISP to your DNS provider; pick one with a clear no-logging policy. It does not hide your traffic from the websites themselves (that is what a <a href="/tech/vpn-what-it-protects/">VPN</a> is for), and it does not make you anonymous. It is one specific, worthwhile layer: stop the network reading your browsing list. Combined with <a href="/tech/browser-privacy-settings/">browser privacy settings</a>, it removes a surprising amount of casual surveillance for a two-minute change.</p>""",
[("Cloudflare — DNS over HTTPS", "https://www.cloudflare.com/learning/dns/dns-over-tls/")],
["what-is-dns", "public-wifi-risks"]),

("home-network-segmentation-vlans-guest", "web-and-hosting", "guide",
"Home network segmentation: the guest-network trick that protects your real devices",
"Your phone, your laptop and your cheap smart bulbs do not all need to be able to reach each other. Here is the practical, no-jargon version of separating them.",
"""<p>A typical home network puts everything on one flat layer: your work laptop, your phone, the family tablet, the TV, and a dozen cheap smart devices that rarely get updated — all able to see each other. That is convenient and quietly risky, because the least secure gadget becomes a path to the most important machine. Segmentation is simply putting things that do not need to talk onto separate parts of the network.</p>
<h2>The version you can do today: the guest network</h2>
<p>Almost every router offers a guest network — a separate Wi-Fi name that is isolated from your main one. The single most useful move is to put all your smart and untrusted devices on it, keeping phones and computers on the main network. The guest network usually blocks its clients from reaching the main network, so a compromised bulb cannot reach your laptop. This is the same idea as putting smart devices on <a href="/tech/smart-home-on-its-own-network/">their own network</a>, applied to the whole house, and it takes minutes.</p>
<h2>The fuller version: VLANs</h2>
<p>If you want to go further, VLANs let one router divide the network into several labelled segments — say one for personal devices, one for smart home, one for guests — with rules about what can cross between them. It is more setup and more fiddly, and it is genuinely optional; the guest-network move captures most of the benefit for almost no effort. The full audit of what to change is in <a href="/tech/home-wifi-security-audit/">the home Wi-Fi security audit</a>.</p>
<h2>Why it matters more now</h2>
<p>The reason segmentation has moved from "nice to have" to "worth doing" is that the average home now has many always-on, rarely-updated devices — the abandonment problem in <a href="/tech/smart-home-devices-stop-getting-updates/">devices that stop getting updates</a>. You cannot make a cheap gadget secure, but you can contain it, so that if it is ever compromised it hits a wall instead of your files. It is the home-scale version of the <a href="/tech/zero-trust-explained-for-small-teams/">zero-trust</a> principle: do not let one weak point become the whole network.</p>""",
[("CISA — secure home network", "https://www.cisa.gov/resources-tools/resources/securing-your-home-network")],
["home-wifi-security-audit", "smart-home-on-its-own-network"]),

]
