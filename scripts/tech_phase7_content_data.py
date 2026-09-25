# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 7 (2026-09-25).

The cybersecurity "ground zero" cluster. Targets the brief's Section 0.4
high-CPC keywords that this desk does NOT already cover (cannibalization check
run first: MDR, patch management and phishing drills already exist and are
linked, not duplicated): data security compliance, phishing training, managed
security service provider, plus the VPN-infrastructure cluster and zero-trust /
incident-response for cluster depth.

International rule honoured (brief Section 30): tier-1 markets are US, UK,
Canada, Australia, New Zealand, Europe and Nigeria, and where law, pricing or
availability differ by jurisdiction the piece names it rather than pretending
one answer fits everywhere. Educational, no fabricated stats, honest framing.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE7_GUIDES = [

# ---------------------------------------------------------------- CYBERSECURITY CLUSTER (safety)
("data-security-compliance-gdpr-ccpa-ndpr", "safety", "guide",
"Data security compliance in plain terms: GDPR, CCPA and Nigeria's NDPA, and what each actually asks of you",
"Compliance is not one rule — it depends on whose data you hold and where they are. Here is the honest plain-language map for the US, UK/EU and Nigeria, and the basics that satisfy most of it.",
"""<p>"Are we compliant?" is the wrong first question, because there is no single thing called compliance. Which rules bind you depends on <em>whose</em> personal data you hold and <em>where those people are</em>, not where your company is registered. A small business in Lagos with customers in London answers to different law than one serving only Lagos. This is the plain-language map, and the reassuring part is that the core discipline overlaps heavily across all three regimes.</p>
<h2>The three regimes, and who they protect</h2>
<p>The <strong>GDPR</strong> (UK and EU) protects the data of people in those regions and follows the data wherever it goes — so a Nigerian or American firm serving UK/EU customers is in scope. The <strong>CCPA/CPRA</strong> (California, and a growing patchwork of other US states) is consumer-rights law: disclosure, opt-out of sale, deletion on request. Nigeria's <strong>NDPA 2023</strong> (with the NDPR that preceded it) is closer to the GDPR in shape — lawful basis, consent, data-subject rights — and applies to processing of Nigerian residents' data. The practical read: if you touch personal data of people in any of these places, assume that place's rules reach you.</p>
<h2>What all three actually ask (the overlap)</h2>
<p>Strip the jargon and the shared requirements are ordinary good practice: know what personal data you hold and why (a record of processing); have a lawful reason to hold it; keep it only as long as needed; secure it; let people see, correct or delete their data; and report a serious breach within the deadline (72 hours under GDPR, a defined window under the NDPA, and per-state rules in the US). None of that requires a legal team to start — it requires knowing your own data, which is the same hygiene as <a href="/tech/your-security-checklist/">the security checklist</a> applied to records rather than passwords.</p>
<h2>Where the jurisdictions genuinely differ</h2>
<p>Do not flatten these into one answer. Consent standards differ (GDPR's consent is stricter than much US practice). Breach-notification clocks and regulators differ. Cross-border transfer rules — moving EU/UK data to the US or Nigeria — carry extra conditions. Fines and enforcement differ sharply. So when a decision hinges on a specific obligation, name the jurisdiction and check the current text or a qualified adviser; this page is the map, not the legal advice. The security side of compliance — actually protecting the data — is the part this desk can help with directly, starting with <a href="/tech/patch-management-for-humans/">patch management</a> and the rest of this cluster.</p>""",
[("ICO — UK GDPR guide", "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/"), ("Nigeria Data Protection Act 2023 (NITDA)", "https://nitda.gov.ng/")],
["your-security-checklist", "patch-management-for-humans"]),

("phishing-training-that-actually-works", "safety", "guide",
"Phishing training that actually works (and the kind everyone ignores)",
"Annual slide decks and blame-the-victim simulations do not change behaviour. Here is what reduces clicks in the real world, for a team of any size.",
"""<p>Phishing remains the entry point for most breaches not because people are careless but because the attacks are good and most "training" is theatre. A yearly compliance slideshow and a punitive simulated-phishing programme feel like action and change almost nothing. The good news is that what actually works is well understood, cheap, and humane.</p>
<h2>Why the usual training fails</h2>
<p>Slides are forgotten in a week. Punitive simulations — trick staff, name and shame the clickers — teach people to fear the test, not to spot the trick, and they make people hide mistakes instead of reporting them. And generic "look for bad grammar" advice is useless against the polished, targeted lures that now dominate. The <a href="/tech/phishing-drill-five-real-lures/">five real lures</a> piece shows how specific and convincing modern phishing is; training has to meet that bar.</p>
<h2>What actually reduces clicks</h2>
<p>Short, frequent, relevant nudges beat one annual marathon — a two-minute example every month lands harder than an hour in January. Teach the <em>decision</em>, not trivia: verify unexpected requests through a second channel, slow down on urgency, treat links and attachments from outside as untrusted until checked. Make reporting frictionless and blame-free — a one-click "report phishing" button that gets a thank-you, not a lecture. And remove the need to be perfect: technical controls catch what people miss.</p>
<h2>The controls matter more than the training</h2>
<p>You cannot train your way out of a problem you can engineer away. Phishing-resistant authentication (passkeys, hardware keys — see <a href="/tech/passkeys-what-they-stop-and-dont/">what passkeys stop</a>) means a stolen password is useless. Email authentication (SPF, DKIM, DMARC) stops spoofed senders. Sensible defaults and least privilege limit the damage from the one click that gets through. Training plus controls is the honest answer; training alone is a comforting fiction. For the always-on personal version, the habits in <a href="/tech/how-to-spot-a-suspicious-link/">spotting a suspicious link</a> are the same lesson at individual scale.</p>""",
[("FTC — How to recognize and avoid phishing scams", "https://www.consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams")],
["phishing-drill-five-real-lures", "passkeys-what-they-stop-and-dont"]),

("managed-security-service-provider-vs-mdr", "safety", "guide",
"MSSP vs MDR: the security-services decision most small teams get backwards",
"MSSP and MDR overlap and vendors blur them on purpose. Here is the honest distinction, who each is for, and the questions that reveal what you are actually buying.",
"""<p>When a small organisation decides it needs security help, it meets an alphabet soup: MSSP, MDR, MSP, SOC-as-a-service. The two that matter most — MSSP and MDR — genuinely overlap, and vendors blur the line because it sells. The decision is not which acronym is better; it is what you actually need done, and whether you are buying tools-and-config or eyes-and-response.</p>
<h2>The honest distinction</h2>
<p>An <strong>MSSP</strong> (managed security service provider) traditionally manages security <em>tools</em> for you — it configures and runs your firewall, endpoint protection, VPN, and maybe a SIEM — and hands you alerts. An <strong>MDR</strong> (managed detection and response) goes further: it actively hunts for threats in your environment, triages the alerts, and responds — containing an incident, not just forwarding a notification. MSSP is "we run your kit"; MDR is "we watch for and fight intruders." The difference between an alert nobody reads and a threat somebody stops is the whole value.</p>
<h2>Who each is for</h2>
<p>An MSSP suits an organisation that has tools but no staff to run them. MDR suits one that fears the intrusion it would not notice — which is most small teams, because they have no security analyst watching at 3am. Many providers now sell a blend, which is fine, but it means you must ask what is actually included rather than trusting the label. This builds directly on <a href="/tech/mdr-what-managed-detection-actually-buys/">what MDR actually buys</a>, which goes deeper on the detection-and-response side.</p>
<h2>The questions that reveal what you are buying</h2>
<p>Ask, in writing: who watches the alerts, and when — 24/7 or business hours in one time zone? When something is found, do you contain it or just tell me? What is the guaranteed response time? What do you need from me to do your job? And what happens to my visibility if I leave? Vendors answering crisply are a good sign; vendors who cannot say who is watching at 3am are selling a dashboard, not a service. For tier-1 buyers, also confirm where the analysts and the data sit — US, UK/EU or Nigeria — because that affects latency, language and the data-location rules covered in <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">data security compliance</a>.</p>""",
[("CISA — small business cybersecurity guidance (MDR recommendations)", "https://www.cisa.gov/small-business")],
["mdr-what-managed-detection-actually-buys", "data-security-compliance-gdpr-ccpa-ndpr"]),

("zero-trust-explained-for-small-teams", "safety", "guide",
"Zero trust explained for small teams (without the enterprise price tag)",
"Zero trust is a principle, not a product: never trust by default, always verify. Here is what it means at small scale and the cheap steps that deliver most of the benefit.",
"""<p>"Zero trust" is marketed as a sprawling enterprise platform, which makes small teams assume it is not for them. It is not a product at all — it is a principle: stop trusting anything just because it is inside the network perimeter, and verify every access every time. The old castle-and-moat model assumed everything inside the wall was safe; zero trust assumes the wall has already been crossed.</p>
<h2>The principle in one line</h2>
<p>Never trust, always verify, assume breach. A request to reach a system is granted based on who is asking, from where, on what device, and only for as much as they need — not because the request came from "inside." That single shift defeats a huge class of attack, because an attacker who phishes one password does not automatically inherit the whole network.</p>
<h2>What small teams can actually do</h2>
<p>Most of the benefit comes from a few unglamorous steps, all cheap. Require strong authentication everywhere, ideally phishing-resistant — the passkeys and hardware keys in <a href="/tech/passkeys-what-they-stop-and-dont/">what passkeys stop</a>. Apply least privilege: give people and services the minimum access they need, so a compromise is contained. Segment, so one foothold is not the whole building — the same instinct as putting smart devices on <a href="/tech/smart-home-on-its-own-network/">their own network</a>, applied to servers and admin access. Keep systems patched (<a href="/tech/patch-management-for-humans/">patch management</a>) because verification means little if the verified path leads to an unpatched box. And log access, so you can see what was reached.</p>
<h2>Why it is the frame that ties this cluster together</h2>
<p>Zero trust is less a project than a way of making the other decisions: it is why you choose MDR that can respond, why compliance asks you to know and limit your data, and why a breach is survivable when access is narrow. It is the architecture behind the rest of this cluster, and you can start it today with authentication, least privilege and segmentation — no platform purchase required.</p>""",
[("CISA — zero trust maturity model", "https://www.cisa.gov/zero-trust-maturity-model")],
["passkeys-what-they-stop-and-dont", "patch-management-for-humans"]),

("incident-response-plan-for-small-business", "safety", "guide",
"The incident-response plan a small business can actually run at 2am",
"You will not remember the right steps during a real breach. A one-page plan, written now, is the difference between a contained incident and a catastrophe.",
"""<p>Small organisations assume incident response is for companies with a SOC. The truth is the opposite: with no security team, the difference between a survivable incident and a disaster is almost entirely whether someone wrote down, in advance, what to do. Under stress nobody improvises well. A one-page plan, agreed beforehand, is the whole game.</p>
<h2>The four moves, in order</h2>
<p>Every response reduces to contain, assess, notify, recover. <strong>Contain</strong> first — stop the bleeding: isolate the affected machine or account, revoke the compromised credential, take the exposed service offline. Containment beats forensics when they conflict. <strong>Assess</strong> what was reached and what data was involved, because that drives everything legal. <strong>Notify</strong> who must be told and on what clock. <strong>Recover</strong> from a known-clean state and close the hole that let it in.</p>
<h2>Notification is where jurisdiction bites</h2>
<p>Who you must tell, and how fast, depends on where the affected people are — this is the part you cannot guess. A breach touching UK/EU residents can trigger a 72-hour GDPR notification to the regulator; Nigerian residents' data engages the NDPA's notification duties; US obligations vary by state and by sector. The <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">compliance map</a> lays out who each regime protects; your plan should name your regulator and the deadline before you need it, not during the panic.</p>
<h2>What to write on the one page, now</h2>
<p>Who is in charge of an incident and their contact. The containment steps for your most likely scenarios (a compromised email account, ransomware on one machine, a leaked token — the risk behind <a href="/tech/github-token-hygiene/">token hygiene</a>). Who you call: your MDR or provider if you have one (<a href="/tech/managed-security-service-provider-vs-mdr/">MSSP vs MDR</a>), your insurer, your regulator, your customers. Where your clean backups live and how to restore — the <a href="/tech/three-two-one-backup-rule/">3-2-1 rule</a> is what makes "recover" real instead of theoretical. Write it before you need it, test it once a year, and the worst night of the business becomes a checklist instead of a catastrophe.</p>""",
[("CISA — incident response for small businesses", "https://www.cisa.gov/small-business")],
["data-security-compliance-gdpr-ccpa-ndpr", "three-two-one-backup-rule"]),

("how-to-build-your-own-vpn-server", "safety", "guide",
"How to build your own VPN server (and the honest case for not bothering)",
"Self-hosting a VPN is genuinely useful for one specific job and a downgrade for another. Here is what it is good for, what it costs, and when a commercial VPN is the better buy.",
"""<p>"Build your own VPN" is a popular project, and for good reason: it is cheap, private, and teaches you a lot. It is also frequently recommended for the wrong reason. A self-hosted VPN and a commercial VPN service solve different problems, and knowing which one you have stops you building the wrong thing.</p>
<h2>What a self-hosted VPN is actually for</h2>
<p>Its real job is <em>getting back into your own network</em> securely from elsewhere — reaching your files, a home server, or a service that should never be exposed to the internet, over an encrypted tunnel. For that, it is excellent and private: the traffic lands at your machine, not a stranger's. Think of it as a private door home, not a cloak of invisibility. This is the use the brief's VPN-infrastructure cluster ("host a VPN", "build a VPN server") is really about.</p>
<h2>What it is not for</h2>
<p>It does not hide you from the internet the way a commercial VPN does. When you tunnel to your own server, your traffic then exits from <em>your</em> connection with <em>your</em> IP — so for "browse from another country" or "stop my ISP seeing my traffic," a self-hosted VPN on your own line does little. That is the job of a commercial provider, and choosing one is a different decision, covered in <a href="/tech/vpn-what-it-protects/">what a VPN protects</a> and <a href="/tech/which-vpn-subscription-is-worth-it/">which VPN is worth it</a>. Build your own to get home; buy one to change where you appear to be.</p>
<h2>The honest cost of running it</h2>
<p>A self-hosted VPN is a server you now secure and maintain: it is internet-facing, so it must be patched — the discipline in <a href="/tech/patch-management-for-humans/">patch management</a> applies with full force, because an unpatched VPN is a front door with the key in it. You own the uptime, the keys, and the configuration. For most people a maintained tool (WireGuard, Tailscale, or a router's built-in option) is the sane route rather than hand-rolling. And if any of this is for a small business rather than personal use, the zero-trust framing in <a href="/tech/zero-trust-explained-for-small-teams/">zero trust for small teams</a> is the better mental model — verify every connection, including your own way in.</p>""",
[("WireGuard — documentation", "https://www.wireguard.com/"), ("Tailscale — self-hosted access", "https://tailscale.com/")],
["vpn-what-it-protects", "which-vpn-subscription-is-worth-it"]),

]
