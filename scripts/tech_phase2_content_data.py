# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 2 (2026-09-25).

Second growth batch. Closes the smart-home shelf to ten, deepens the
cybersecurity cluster with the two highest-leverage B2B-adjacent topics the
master brief's verified CPC data flags (patch management, managed detection),
and adds two streaming mechanics pieces. Same discipline as batch 1: evergreen
mechanics and decision guidance, no volatile statistics, no fabricated pricing
or testing, dated official sources where a source is needed.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE2_GUIDES = [

# ---------------------------------------------------------------- SMART HOME (close to 10)
("smart-lock-when-the-battery-dies", "smart-home", "guide",
"Plan for the day your smart lock's battery dies: override, alerts and the failure order",
"A smart lock is only as good as its failure plan. The mechanical override, the battery-warning window and the offline behaviour are the three things to verify before you trust it with your door.",
"""<p>The honest way to evaluate a smart lock is not how it works on a good day - every smart lock opens when the app is up and the battery is full - but what happens on the bad days. Three failure modes cover almost all of them: the battery dies, the network is down, and the phone is not in your hand. A lock with a good answer to all three is fine; a lock with a bad answer to any one is a liability you have bolted to your door.</p>
<h2>The mechanical override is the product, not the app</h2>
<p>Every trustworthy smart lock keeps a physical key path - a hidden cylinder, a key cap, or an external terminal - that opens it with zero power and zero network. Before you install, find that override and actually use it, twice, from outside, in the dark. If the override is fiddly, concealed so well you cannot find it under stress, or - worst - absent, the lock has made you less secure, because you now depend on electronics for a door that used to open with a key. Keep the key somewhere that is not inside the locked house.</p>
<h2>Battery warnings are a window, not an event</h2>
<p>Good locks warn weeks ahead and repeat the warning. The failure is not the battery dying; it is ignoring the first warning and discovering the lock at zero. Treat the first low-battery notice as a calendar item for this week. Use the battery type the manual names - mixing a weaker cell to save money is exactly the false economy that shortens the warning window. And know your lock's behaviour at zero: some hold the last state, some fail open-able only by key; that difference matters if the battery dies while you are away.</p>
<h2>Offline behaviour: the lock should still lock</h2>
<p>A network outage should never stop the door from locking and unlocking locally. The app being unreachable is an inconvenience; the lock refusing a keypad code or key because it cannot phone home is a design failure. Verify, with the Wi-Fi off, that keypad, key and any local credential still work. This is the same principle as the radio-assignment piece: the security-relevant path should not depend on the part that fails most - see <a href="/tech/zigbee-wifi-thread-which-device/">which radio belongs to which device</a> for why locks generally belong on a mesh, not on crowded Wi-Fi.</p>
<h2>The failure order to check before you trust it</h2>
<ul>
<li>Key override, from outside, in the dark - twice.</li>
<li>Keypad or local credential with the network off.</li>
<li>What the lock does at a fully dead battery.</li>
<li>How and how often it warns before that happens.</li>
</ul>
<p>If a lock passes those four, it is a convenience that degrades gracefully to an ordinary lock. If it fails any, it is an ordinary lock that sometimes refuses to be one - and the worth-it question in <a href="/tech/smart-home-worth-it/">smart-home devices worth it</a> turns against it.</p>""",
[],
["smart-home-worth-it", "zigbee-wifi-thread-which-device"]),

("smart-bulb-flicker-the-real-causes", "smart-home", "guide",
"Smart bulbs flickering? The three real causes, and the fix order that finds yours",
"Nearly all smart-bulb flicker is power or grouping, not a broken bulb. Check the dimmer, the minimum-load problem and the mesh grouping in this order and you will find the cause without replacing hardware.",
"""<p>Smart bulbs flicker for a short list of reasons, and almost none of them is "the bulb is broken." The LED and its driver are being asked to do something the electrical side cannot support. Work the list in order, because the first cause is by far the most common and the cheapest to fix.</p>
<h2>1. A dimmer that was never meant for LEDs</h2>
<p>Leading-edge dimmers built for incandescent loads chop the waveform in a way an LED driver misreads, producing shimmer at low brightness or a strobe at high. If the flickering bulb is on a dimmer switch, this is your first suspect. The test is brutal and free: put the bulb on a plain on/off circuit. If it stops flickering, the dimmer was the cause - replace it with a trailing-edge (LED-rated) dimmer, or set the bulb's minimum level above the range where the dimmer misbehaves.</p>
<h2>2. The minimum-load problem on "dumb" switches and circuits</h2>
<p>Some circuits and smart switches leak a tiny current or expect a minimum load. A single low-watt LED on such a circuit can glow, pulse or flicker because the driver is being fed crumbs of power. This shows up as flicker or ghost-glow when the switch is off, or a pulse every few seconds. Adding load (a second bulb on the same fitting) or fitting a bypass at the switch usually ends it. If it only happens when "off," it is almost certainly this.</p>
<h2>3. Grouping and mesh chatter</h2>
<p>Smart bulbs that flicker in a brief, synchronised pulse across a group are usually showing you network behaviour, not electrical failure: a group command re-sent, or a bulb re-joining the mesh. If your bulbs ride a crowded Wi-Fi rather than a proper mesh, re-joins and retries become visible as flicker - the same contention described in <a href="/tech/zigbee-wifi-thread-which-device/">the radio-assignment guide</a>. Move the bulbs to the mesh they were designed for, or reduce group sizes, and the pulses stop.</p>
<h2>The fix order</h2>
<p>Dimmer first (test on plain power), then minimum-load (check off-state glow and single-bulb circuits), then network (mesh vs Wi-Fi, group size). Only after all three do you suspect the bulb itself - and even then, a bulb that flickers on a known-good plain circuit is the one you replace, not the first one you replaced.</p>""",
[],
["zigbee-wifi-thread-which-device", "smart-home-worth-it"]),

# ---------------------------------------------------------------- SAFETY / CYBER (depth)
("patch-management-for-humans", "safety", "guide",
"Patch management for one person: the update order that matters, and what can wait",
"You do not need an enterprise process to patch well. You need an order: the software that touches the internet updates first, the rest on a rhythm. Here is the order and the reasoning.",
"""<p>Patch management sounds like an enterprise discipline, but its core insight applies to a single laptop: not all software is equally exposed, so not all updates are equally urgent. The order below ranks software by how directly it faces the internet, because that exposure is what turns an unpatched bug into a remote compromise.</p>
<h2>Update first: the software that meets strangers</h2>
<ul>
<li><b>Browsers.</b> Your browser executes code from every site you visit. It is the single most-exposed program you run, and browser updates are the highest-value patches on a personal machine. Set it to update automatically and restart it when asked.</li>
<li><b>The operating system.</b> The OS handles network traffic before any app does. OS security updates close the holes that need no click at all. Auto-update for security patches is the right default.</li>
<li><b>Anything that opens files from others: PDF readers, office suites, archive tools.</b> A malicious document is a delivery mechanism, and these are the decoders.</li>
<li><b>Your router's firmware.</b> The router is the one computer you never think about that faces the internet continuously. Check the vendor page a couple of times a year; a patched router is a quietly large win.</li>
</ul>
<h2>Update on a rhythm: everything else</h2>
<p>Editors, games, media tools and local utilities face the internet rarely or not at all; their updates matter, but on a monthly rhythm rather than immediately. A monthly sweep - one sitting, everything current - covers them without your attention being the scheduler. This is the personal version of the discipline the pros call patch management: exposure-ranked urgency plus a standing cadence, which is also what keeps <a href="/tech/windows-update-problems/">Windows update problems</a> from becoming a surprise.</p>
<h2>What can wait, and the one rule about waiting</h2>
<p>It is reasonable to wait a few days on a brand-new major version of a big OS or app to let early bugs surface - that is caution, not neglect. The rule is that waiting applies to <em>feature</em> releases, never to <em>security</em> patches. A security patch that sits unapplied for weeks is a known open door: attackers scan for the exact versions a patch fixed. So: feature updates on your schedule, security updates on the vendor's.</p>
<h2>The reboot honesty</h2>
<p>Many patches only take effect after a restart. An update that has been downloaded for a fortnight behind an un-rebooted machine is not applied. Fold the reboot into the rhythm - one predictable restart a week beats a month of pending ones. That single habit, plus auto-update for the exposed layer, is most of personal patch management.</p>""",
[("CISA", "https://www.cisa.gov/secure-our-world")],
["windows-update-problems", "your-security-checklist", "password-manager-migration-weekend"]),

("mdr-what-managed-detection-actually-buys", "safety", "guide",
"Managed detection and response, honestly: what you are actually buying, and when DIY is the right call",
"MDR is not antivirus with a pricier logo. It is staffing and coverage you do not have. This is the honest trade-off: what the service buys, what it cannot buy, and the choose-A-if / choose-B-if line.",
"""<p>The core question about managed detection and response (MDR) is not "is it good" but "what scarcity does it relieve." What MDR buys is the thing most organisations genuinely lack: people watching, around the clock, who have seen enough real incidents to tell an attack from a backup job. If you understand exactly what is being bought, the decision makes itself.</p>
<h2>What you are actually buying</h2>
<ul>
<li><b>Coverage you cannot staff.</b> Alerts do not keep office hours. A solo admin or a small team covers perhaps the working day; MDR's value is the 2am alert that a human actually triages. That is the headline purchase.</li>
<li><b>Analyst judgement at volume.</b> The hard part of detection is not collecting logs - tools do that - it is the judgement call on thousands of ambiguous events. MDR vendors amortise that judgement across many customers.</li>
<li><b>A defined response path.</b> Good MDR includes the playbooks and authority to contain - isolate a machine, disable an account - fast, instead of after a meeting.</li>
</ul>
<h2>What it cannot buy</h2>
<p>MDR does not remove the need for the basics: if your estate is unpatched, unbacked-up and full of admin-everything accounts, a managed team is watching a burning building. It also does not remove your accountability - you still own the risk and the decisions; the service changes how fast and how well they are made. And quality varies: "we monitor your antivirus dashboard" is not MDR, so the contract's specifics (what telemetry, what response authority, what hours) are the whole ballgame.</p>
<h2>The choose-A-if / choose-B-if line</h2>
<p>Choose managed detection if you have no person whose job is security triage today, you hold data you would pay to keep, and you cannot staff 24/7 coverage yourself - that combination is exactly the scarcity MDR is priced to relieve. Choose the do-it-yourself path if you have the people and the hours, your footprint is small and simple, and you can honestly say someone sober is reading the alerts; in that case the money is better spent on the basics - patching, backups, MFA - which is the framing in <a href="/tech/your-security-checklist/">the security checklist</a>.</p>
<p>Pricing varies too widely to print: it tracks device count and telemetry volume, and the honest move is to price the same scope with two or three vendors and read what response authority each contract actually grants. The number matters less than whether the 2am alert reaches a human who can act.</p>""",
[("NIST SP 800-61 Rev. 2", "https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final")],
["your-security-checklist", "patch-management-for-humans"]),

# ---------------------------------------------------------------- STREAMING (depth)
("hdr-formats-the-weakest-link", "streaming", "guide",
"HDR10 vs Dolby Vision vs HLG: your chain is only as good as its weakest link",
"HDR is an end-to-end contract: source, player, cable, port and panel must all speak the same dialect. Find the one link that doesn't and you know exactly why the picture falls back to SDR.",
"""<p>HDR fails in a very specific way: the whole chain silently falls back to standard dynamic range, and you are left with a washed-out picture and no explanation. That is because HDR is a contract between five links - the content, the player or app, the cable, the TV's port, and the panel - and every link must support the dialect being spoken. Diagnosis is therefore the process of finding the one link that doesn't.</p>
<h2>The three dialects, plainly</h2>
<ul>
<li><b>HDR10</b> is the baseline every HDR device must speak. If anything in your chain does HDR at all, it does HDR10.</li>
<li><b>Dolby Vision</b> adds dynamic metadata - scene-by-scene instructions - and needs licensed support at both ends. A Vision disc on an HDR10-only TV plays as HDR10: fine, but not what the disc intended.</li>
<li><b>HLG</b> is the broadcast flavour, designed to degrade gracefully on SDR screens. It is what live TV generally uses, and the least fussy of the three.</li>
</ul>
<h2>Where the chain breaks, in practice</h2>
<p>The panel is rarely the weakest link on a modern TV; the breaks are upstream. The streaming app must carry the dialect (an app that only outputs HDR10 will never show Vision). The player or console must have HDR enabled <em>and</em> the format toggled on. The HDMI port matters: on many TVs only specific ports handle the full bandwidth, and a port set to a compatibility mode caps the signal. The cable must be a certified high-speed one; an old cable is a classic invisible break. And any soundbar or receiver passed through must itself pass HDR metadata - an AVR that strips metadata is a single link that downgrades everything behind it.</p>
<h2>Finding your weakest link</h2>
<p>Work from the screen backwards with one known-good source: play a title you know is Dolby Vision on a device you trust, straight into the TV's best port with a certified cable. If Vision appears, the panel and that path are fine; then reintroduce one link at a time - the soundbar, the other port, the other app - and the link whose reintroduction drops you to SDR or HDR10 is your weakest one. Label the good port and cable so the chain is never accidentally rebuilt wrong.</p>
<p>The payoff for doing this once is that the expensive pixels you paid for - and the distance maths from <a href="/tech/4k-on-a-small-tv-when-its-invisible/">the 4K-on-a-small-TV piece</a> - are finally showing the dynamic range that was the real upgrade all along.</p>""",
[],
["4k-on-a-small-tv-when-its-invisible", "streaming-quality-settings"]),

("audio-video-sync-drift-fix-order", "streaming", "guide",
"Lips out of sync? The real causes of audio drift and the fix order that ends it",
"Sync drift is almost always one device re-clocking the stream differently from another. The fix order - TV processing first, then the audio path, then the app - isolates which device is the liar.",
"""<p>When lips and sound disagree, something in the chain is adding latency to one stream and not the other. Video processing and audio decoding each take time, and when they take different amounts of time the two arrive apart. The fix is not a setting you guess at; it is isolating which device is the slow one, in an order that starts with the biggest usual offender.</p>
<h2>1. The TV's own processing (the usual liar)</h2>
<p>A TV applying heavy motion smoothing and noise reduction can lag the picture by tens to over a hundred milliseconds while the audio passes through. The test is the TV's game or PC mode, which strips most processing: if sync snaps right in that mode, the TV's processing was the drift, and you either keep that mode for the source or use the TV's audio-delay setting to re-align the sound to the processed picture.</p>
<h2>2. The audio path: passthrough versus decode</h2>
<p>Every box that re-decodes audio adds its own latency. A soundbar receiving a raw bitstream (passthrough) and decoding it once typically lags differently than the TV decoding and sending PCM. Mixing the two - TV speakers and soundbar, or an AVR decoding while the TV processes - is the classic recipe for drift. Pick one decoder: set the source or TV to pass the original format to the soundbar and let nothing else touch it. When a device offers an audio-delay or lip-sync number, small corrections here fix the residue.</p>
<h2>3. The app or box itself</h2>
<p>Only after the TV and audio path are settled do you suspect the source: an overloaded streaming stick, or an app whose own A/V clocks disagree. Rebooting the stick is legitimately first among these; a device at its memory limit stutters video while audio keeps time. If one app drifts and others do not, the app is the liar and its in-app sync offset (where offered) is the repair.</p>
<h2>The order, and why it works</h2>
<p>TV processing, then audio-path decoding, then the source - because each step down the list is a smaller and rarer contributor, and fixing a big one first often makes the small ones invisible. The same discipline of isolating one device at a time applies to buffering problems, where the shared link is the liar instead - see <a href="/tech/why-streams-buffer-at-night/">why streams buffer at night</a>.</p>""",
[],
["why-streams-buffer-at-night", "streaming-quality-settings"]),

]
