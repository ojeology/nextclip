# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch (2026-09-25).

First growth batch after the living-hub rebuild. Deliberately small and high-
quality, per the master brief's "do not mass-publish" rule: three cybersecurity
pieces (the brief's #1 priority, highest CPC-to-competition) and three pieces
for the two thinnest shelves the hub's self-read band advertises (streaming,
smart-home).

Discipline honoured throughout:
  * Evergreen mechanics, not volatile statistics. Nothing here prints a number
    that can go stale; where a fact could change, it carries a dated source.
  * No fabricated testing. Where we did not run hardware, we say so and frame
    the piece as documented mechanics / decision guidance.
  * Honest comparisons: "choose A if / choose B if", no fake winners.
  * Official, stable sources only.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE1_GUIDES = [

# ---------------------------------------------------------------- SAFETY (cyber)
("password-manager-migration-weekend", "safety", "guide",
"Move your whole life into a password manager in a weekend, without locking yourself out",
"The order that matters: vault first, master password and emergency kit second, then rotate the five accounts that actually hurt. No account left orphaned.",
"""<p>Most people never adopt a password manager because the migration looks like one giant, risky task. It is not. It is three small tasks done in the right order, and the order is what keeps you from ever being locked out.</p>
<h2>Day one: fill the vault before you change anything</h2>
<p>Install the manager and import what your browser already knows. Every major browser can export saved passwords, and every major manager can import them. Do not retype them by hand; you will skip the ones you barely remember, and those are exactly the accounts that will bite you later. After the import, log in to nothing. The vault is now a <em>record</em>, not yet a system.</p>
<p>Now audit the record. You will find duplicates: the same password reused across a forum, a shop and, worryingly, your email. Mark those. Reuse is the only thing that turns one leaked site into five compromised accounts, which is why the migration is worth doing at all. For the honest scenario-by-scenario picture of what a manager does and does not protect, see <a href="/tech/vpn-and-password-safety-table/">the VPN and password safety table</a>.</p>
<h2>Day one, evening: the two keys you must not lose</h2>
<p>A password manager concentrates risk into two secrets: the master password and the recovery path. Choose a master password that is long and memorable to you alone - a string of four or five unrelated words beats a short symbol soup, because length is what resists guessing and you will type it dozens of times a day. Write the recovery kit - the printed emergency code, the location of any key file - on paper, and put the paper somewhere you trust. A manager with no recovery path is a single point of failure; a manager with a paper kit is a belt with braces.</p>
<h2>Day two: rotate the five that hurt, in this order</h2>
<p>Do not try to change two hundred passwords in a weekend. Change the five that matter, then let the rest rotate naturally the next time you log in.</p>
<ul>
<li><b>Email first.</b> Your email is the master key to password resets everywhere else. Secure it before anything that depends on it.</li>
<li><b>Bank and payments.</b> Direct financial damage lives here.</li>
<li><b>The account that stores your identity documents or cloud backups.</b> Losing it is losing your paper trail.</li>
<li><b>Your primary shop and delivery accounts.</b> Less about money, more about the saved card and address an attacker inherits.</li>
<li><b>Work-adjacent accounts</b> that share any password with the above.</li>
</ul>
<p>For each, generate a long random password in the manager and enable two-factor while you are logged in. If you want the free-tier baseline for the manager itself, <a href="/tech/bitwarden-free-password-manager/">the Bitwarden free-plan piece</a> documents what unlimited devices officially includes.</p>
<h2>What this does not cover</h2>
<p>A manager fixes reuse and recall. It does not fix phishing - a perfect vault still hands your real password to a fake login page that looks right. That is a separate skill; <a href="/tech/how-to-spot-a-suspicious-link/">spotting a suspicious link</a> is the companion habit. And it does not replace having done <a href="/tech/your-security-checklist/">the two-minute security checklist</a>; do both.</p>""",
[("Bitwarden", "https://bitwarden.com/help/import-data/")],
["bitwarden-free-password-manager", "vpn-and-password-safety-table", "your-security-checklist"]),

("passkeys-what-they-stop-and-dont", "safety", "guide",
"Passkeys explained: what they actually stop, what they don't, and when to keep a password anyway",
"A passkey is a per-site key pair, not a secret you type. That kills phishing and reuse - and leaves a different set of problems you should plan for before you switch.",
"""<p>A passkey replaces "something you know" with "something you have, plus something you are." When you create a passkey for a site, your device generates a key pair: the private key never leaves your device's secure storage, and the site keeps only the public half. At login, the site sends a challenge your device signs with the private key, unlocked by your fingerprint, face or device PIN. There is no shared secret for a breached database to leak, and nothing to type into a lookalike page.</p>
<h2>What passkeys genuinely stop</h2>
<ul>
<li><b>Phishing, structurally.</b> The signature is bound to the site's real origin. A fake page on a fake domain cannot get a valid signature from your real passkey, so the attack that beats passwords simply does not compute. This is the big one.</li>
<li><b>Credential-stuffing and reuse.</b> Each site gets its own key pair, so one breach compromises nothing elsewhere. The reuse problem from <a href="/tech/password-manager-migration-weekend/">the migration guide</a> disappears by construction.</li>
<li><b>Leaked-password databases.</b> The site never stores a secret that can be stolen; a breached verifier list of public keys is useless to log in.</li>
</ul>
<h2>What they don't stop</h2>
<p>Passkeys authenticate the <em>device and its unlock</em>, not your judgement. They do nothing about malware on an already-compromised device that acts as you while you are logged in. They do not protect a session after login - cookie theft is still cookie theft. And they do not help if the site's own account-recovery flow is lax: an attacker who can convince support to move your account to their device bypasses the cryptography entirely, which is why recovery hygiene matters more, not less, with passkeys.</p>
<h2>The real problem: losing the thing that holds your keys</h2>
<p>A passkey lives in a device or a synced ecosystem. Lose the phone with no backup and no fallback, and you can be locked out of an account you provably own. So the discipline inverts from "remember many secrets" to "protect the few recovery paths": keep a password-manager fallback or a printed backup code on high-value accounts until you have confirmed the passkey syncs where you expect.</p>
<h2>When to keep a password anyway</h2>
<p>Keep a traditional password plus two-factor on accounts where you cannot tolerate a single-device dependency, on shared-family accounts, and anywhere you sign in from borrowed or public machines - a passkey is least comfortable on hardware you do not control. The honest reading is that passkeys and a good manager are complements, not rivals: passkeys where supported and low-risk to recover, manager-generated passwords everywhere else. For the broader picture of what each layer stops, see <a href="/tech/vpn-and-password-safety-table/">the safety table</a>.</p>""",
[("W3C WebAuthn Level 2", "https://www.w3.org/TR/webauthn-2/"), ("FIDO Alliance", "https://fidoalliance.org/passkeys/")],
["vpn-and-password-safety-table", "password-manager-migration-weekend", "your-security-checklist"]),

("phishing-drill-five-real-lures", "safety", "guide",
"The phishing drill: five real lures and the one tell that gives each away",
"Run the same ten-second check on every message and most lures collapse. Here are the five most common shapes, and the specific tell that breaks each one.",
"""<p>Phishing works by borrowing trust - your bank's logo, a colleague's name, a delivery you were half-expecting. You cannot defend against it by feeling; you defend against it with one mechanical check, applied every time. The check is: <em>who is the message actually from, and where does the action actually lead?</em> Everything below is that check applied to the five lures you will actually meet.</p>
<h2>1. The urgent delivery problem</h2>
<p>"Your parcel could not be delivered; pay a small fee." The tell: the sender domain and the link domain disagree with the courier's real one. Hover or long-press the link and read the address, not the blue text. A courier you never used is a certainty, not a suspicion. The mechanics of reading the address are covered in <a href="/tech/how-to-spot-a-suspicious-link/">how to spot a suspicious link</a>.</p>
<h2>2. The account problem that needs you now</h2>
<p>"Unusual sign-in; confirm your password." The tell: legitimate services ask you to sign in on their site; they never need your password inside a message or a linked form. The fix is to never follow the link - type the address you already know, or use a bookmark, and check for the alert there. If it is real, it will be waiting for you.</p>
<h2>3. The colleague in a hurry</h2>
<p>A short, slightly-off request from a familiar name - a gift-card or transfer ask. The tell: a new or lookalike address, and pressure that discourages a second channel. The defence is not cryptographic, it is social: confirm over a channel the message did not arrive on. Ten seconds of "did you send this?" ends the attack.</p>
<h2>4. The document or invoice you weren't expecting</h2>
<p>An attachment or shared file with a plausible name. The tell: you did not expect it, and the sender is vague. Unexpected attachments from real contacts usually mean their account is already compromised - so the message is being sent <em>by</em> someone you know, without them knowing. When in doubt, open nothing and ask them directly.</p>
<h2>5. The refund that owes you money</h2>
<p>"We owe you a refund; enter your card to receive it." The tell is inverted from the others: instead of fear it uses greed, and it asks for card details to <em>give</em> you money, which no real refund ever requires. Refunds go back to the card you paid with; nobody legitimate needs new card numbers to send you your own money.</p>
<h2>The one habit that covers all five</h2>
<p>Slow down exactly when the message tries to speed you up. Urgency is the payload; the link is just delivery. Keep <a href="/tech/your-security-checklist/">the checklist</a> handy, and treat two-factor as the seatbelt for the lure that still gets through: it turns a stolen password into a failed login.</p>""",
[("CISA", "https://www.cisa.gov/secure-our-world")],
["how-to-spot-a-suspicious-link", "your-security-checklist", "password-manager-migration-weekend"]),

# ---------------------------------------------------------------- STREAMING (thin shelf)
("why-streams-buffer-at-night", "streaming", "guide",
"Why your stream buffers at night and not at noon: the contention problem, diagnosed",
"It is not your plan's headline speed. It is shared capacity meeting everyone's evening at once. Here is the diagnosis order that finds which shared link is the bottleneck.",
"""<p>A stream that plays fine at noon and stalls at 8pm is almost never a "your internet is too slow" problem. It is a contention problem: several links in the chain are shared, and in the evening they are all busy at once. Diagnosis is the process of finding which shared link is the one that saturates.</p>
<h2>The chain, and where it gets shared</h2>
<ul>
<li><b>Your Wi-Fi.</b> Shared with every device in the home, and with neighbours on the same channels. Evening is when everyone's devices wake up. See <a href="/tech/wi-fi-standards-compared/">Wi-Fi standards compared</a> for why older radios collapse first under load.</li>
<li><b>Your router's uplink.</b> The single pipe from your home to your ISP, shared by every person and device you have. This is the link most people mean by "my speed," and it is genuinely shared.</li>
<li><b>The ISP's local aggregation.</b> Your street or cabinet shares capacity upstream. ISPs plan for average, not peak, usage - so peak evening is exactly when this link is busiest.</li>
<li><b>Interconnection and the streamer's edge.</b> Usually the least likely culprit for a single household, because big streamers cache popular video close to ISPs.</li>
</ul>
<h2>The diagnosis order</h2>
<p>Start at your end, because it is the only part you control and the most common failure. First, test over a cable at night. If the stall disappears on cable, your Wi-Fi was the saturated link and the fix is radio-side: channel, band, or placement - the same fixes as <a href="/tech/streaming-quality-settings/">streaming quality settings</a> discusses for the picture side. If it still stalls on cable, your uplink or the aggregation beyond it is saturated; then check whether the stall correlates with someone else in the home starting a big download or upload - uploads especially, because a saturated upload queue can starve your stream's acknowledgements.</p>
<h2>What actually helps, in order of cost</h2>
<p>Free first: schedule big uploads and backups for off-peak; move the streaming device to the 5&nbsp;GHz band or a cable; lower the stream's bitrate one notch at peak - a stable 1080p beats a stuttering 4K. Then cheap: a router that handles your home's device count, or a wired backhaul for the TV. Only last: paying for a bigger plan, which fixes the uplink link but does nothing for a saturated Wi-Fi or street-level aggregation. Buy the fix for the link you actually diagnosed.</p>""",
[],
["wi-fi-standards-compared", "streaming-quality-settings"]),

("4k-on-a-small-tv-when-its-invisible", "streaming", "guide",
"4K on a small TV: when the upgrade is genuinely invisible, and when it isn't",
"Resolution is a function of pixel density at your seating distance, not a badge. A simple distance rule tells you when 4K pays and when you are paying for pixels your eye cannot resolve.",
"""<p>The honest question about 4K on a small screen is not "is 4K better" - it always carries more pixels - but "at my seating distance, can my eye use those pixels." Resolution is perceived as density: the same 3840 pixels spread over 43 inches, viewed from three metres, may simply be finer than your vision can resolve. Past that point, the extra detail is real and invisible.</p>
<h2>The distance rule of thumb</h2>
<p>For a viewer with normal vision, the benefit of 4K over 1080p becomes hard to see once you sit farther than roughly one and a half times the screen's diagonal. On a 43-inch screen that is about 1.6 metres; sit at three metres and the two formats converge for most material. On a 65-inch screen the threshold moves out to about 2.5 metres, which is why the same person who sees nothing on a small 4K set sees a clear step on a large one. Measure your sofa-to-screen distance before you pay for resolution you cannot resolve.</p>
<h2>When small-screen 4K still pays</h2>
<p>Two cases make it worthwhile regardless. First, HDR: the wider brightness and colour range that usually travels with 4K streams is visible at any size and any distance, and for most people HDR is the upgrade they actually notice. Second, sitting close - a desk or kitchen screen used at arm's length resolves the extra detail readily. In both cases you are buying something 4K bundles, not the pixel count itself.</p>
<h2>The bandwidth honesty check</h2>
<p>A 4K stream wants several times the bitrate of 1080p. If your evening connection is the contended one described in <a href="/tech/why-streams-buffer-at-night/">why streams buffer at night</a>, choosing 4K on a small screen spends scarce bandwidth on pixels you cannot see and buys yourself the stall. On a small set with a busy link, capping at 1080p and letting the stream stay stable is the better trade - and the saved bitrate is a real, visible improvement in smoothness.</p>
<p>So: large screen or close seating, 4K pays. Small screen at sofa distance, the pixels are invisible - spend on HDR and stability instead.</p>""",
[],
["streaming-quality-settings", "why-streams-buffer-at-night"]),

# ---------------------------------------------------------------- SMART HOME (thin shelf)
("zigbee-wifi-thread-which-device", "smart-home", "guide",
"Zigbee vs Wi-Fi vs Thread: which radio belongs to which smart-home device",
"Three radios, three jobs. Wi-Fi for the heavy and few, Zigbee for the many and small, Thread for the mesh that must survive a hub dying. A simple assignment rule per device.",
"""<p>Smart-home flakiness is usually a radio-assignment problem: too many small devices on a radio built for few big ones, or a mesh that collapses when one device powers off. The three common radios - Wi-Fi, Zigbee and Thread - are not better or worse in the abstract; they are built for different jobs, and the fix is assigning each device to the radio that matches its job.</p>
<h2>Wi-Fi: few, heavy, mains-powered</h2>
<p>Wi-Fi gives every device a direct, high-bandwidth link to your network - perfect for cameras and anything streaming video, and for the handful of plugs near your router. But each Wi-Fi device is a full citizen of your network: it holds a connection, takes an address, and talks loudly. Dozens of battery sensors on Wi-Fi will crowd your router and drain their batteries, because Wi-Fi radios were never designed for tiny, infrequent, low-power messages.</p>
<h2>Zigbee: many, small, meshed</h2>
<p>Zigbee is built for exactly that crowd: lots of low-power sensors, bulbs and switches that pass messages for each other in a mesh, coordinated by a hub or coordinator. Battery life is measured in months to years, and adding devices makes the mesh stronger, not more crowded. The catch is the hub: a classic Zigbee mesh routes around a dead bulb, but if the coordinator itself dies, the network is down. It is a managed mesh.</p>
<h2>Thread: the self-healing mesh with no single point</h2>
<p>Thread is the newer answer to the same many-small-devices job, with one structural difference: there is no single coordinator whose death kills the network. Thread devices form a self-healing IPv6 mesh where any mains-powered device can route, and the "border router" role can be served by more than one device. That is why the modern smart-home standard (Matter) chose Thread for its low-power layer.</p>
<h2>The assignment rule</h2>
<ul>
<li><b>Cameras and anything with video:</b> Wi-Fi (or wired). They need the bandwidth only Wi-Fi offers.</li>
<li><b>Sensors, buttons, locks, bulbs - the many and small:</b> Zigbee or Thread, not Wi-Fi. Keep the crowd off your router.</li>
<li><b>If you are buying new and want resilience:</b> prefer Thread-capable devices, so the mesh survives any single device dying; see <a href="/tech/smart-home-worth-it/">smart-home devices worth it</a> for the worth-it framing.</li>
<li><b>Mix deliberately:</b> a home with Wi-Fi for the heavy and one mesh (Zigbee or Thread) for the small is the stable shape. Two competing meshes and a crowded Wi-Fi is the flaky shape.</li>
</ul>
<p>Radio choice is also why placement advice for Wi-Fi - like <a href="/tech/wi-fi-standards-compared/">the standards comparison</a> covers - does not transfer to a mesh: in a mesh you spread devices to extend it, rather than clustering them near one access point.</p>""",
[("Connectivity Standards Alliance", "https://csa-iot.org/"), ("Thread Group", "https://www.threadgroup.org/")],
["smart-home-worth-it", "wi-fi-standards-compared"]),

]
