# -*- coding: utf-8 -*-
"""BRYME Tech — 10/10 brief, Tier 2 batch A: the smart-home protocol cluster.

Verification receipts (2026-09-15):
- Protocol layer model (Matter = application standard over Thread/Wi-Fi/Ethernet;
  Thread = IPv6 mesh on 802.15.4; Zigbee = 2.4 GHz mesh needing a coordinator):
  per Connectivity Standards Alliance / Thread Group positioning, corroborated
  across independent 2026 explainers. No vendor superiority claims.
- "Matter does not run over Zigbee; bridges translate" — stated per CSA docs.
- Thread border router requirement and the bridge-vs-border-router distinction:
  the piece most guides miss, stated explicitly with what fails without it.
- Battery-life and latency numbers deliberately NOT pinned (the brief's rule):
  described qualitatively (months-to-years, low latency) — aggregator tables
  disagree, so no number is universalised.
- No absolute claims. Everything framed as conditions ("battery device → Thread
  suits", "mains-powered → Wi-Fi is fine").
"""

SMARTHOME_1010_A = [

    # ------------------------------------------------------------------ #
    # Tier 2 #11: Matter vs Thread vs Zigbee vs Wi-Fi
    # ------------------------------------------------------------------ #
    ("matter-vs-thread-vs-zigbee-vs-wifi", "smart-home", "guide",
     "Matter vs Thread vs Zigbee vs Wi-Fi: the layer mistake most guides make",
     "Matter is a language, Thread is a radio — they're not competitors. The four-way comparison that finally sorts which layer does what, and what to buy for each device.",
     """<p>Almost every smart-home buying mistake traces to one confusion: treating Matter, Thread, Zigbee and Wi-Fi as rival products on the same shelf. They are not. Two of them are <em>languages</em> and two are <em>radios</em> — different layers of the same stack — and once you can name the layer, the whole landscape stops being confusing.</p>

<h2>The one-sentence version</h2>
<p><b>Matter is what a device speaks; Thread, Zigbee and Wi-Fi are how it transmits.</b> Matter is an application standard — it defines how a light, lock or sensor describes itself and takes commands, so any certified device works across Apple Home, Google Home, Alexa, SmartThings and friends. Thread, Zigbee and Wi-Fi are network layers — the radio the device uses to actually move those words. A single device can be Matter over Wi-Fi, Matter over Thread, or Matter over Ethernet. All three are valid Matter devices.</p>

<h2>The four, one layer at a time</h2>
<p><b>Wi-Fi (radio).</b> Your existing network. Plenty of bandwidth, no extra hardware, and the natural fit for mains-powered devices — plugs, displays, cameras, appliances — because the radio draws power constantly. The honest downsides: battery devices on Wi-Fi chew through cells, every device adds load to a network built for laptops and phones, and 2.4 GHz congestion is real in apartment blocks. If a device is plugged into the wall and doesn't need a hub, Wi-Fi is simply fine — <a href="/tech/wi-fi-setup-mistakes/">provided your network is set up for it</a>.</p>
<p><b>Zigbee (radio).</b> A mature 2.4 GHz low-power mesh that's been in smart homes for over a decade — the reason there are mountains of affordable Zigbee bulbs and sensors. Devices relay for each other (the mesh self-heals around a dead node), battery devices last a long time, and it needs a <em>coordinator</em> — usually a hub — to join your network. The catch in 2026: Zigbee devices reach modern ecosystems only through a bridge that translates. Existing Zigbee setups keep working fine; new buyers are choosing Thread for the same role.</p>
<p><b>Thread (radio).</b> The modern successor to Zigbee's role: a low-power, self-healing mesh on the same 802.15.4 radio, but IP-native — every Thread device speaks IPv6 directly, which is exactly why it pairs so cleanly with Matter: no translation layer, the Matter language rides straight on top. Battery sensors, buttons, locks and some bulbs are Thread's natural territory. The requirement most guides skip: a Thread mesh needs a <b>Thread border router</b> to connect to your network — without one, Thread devices can talk to each other but never reach your phone. Border routers now ship inside hardware you might already own: smart speakers, hubs, some Wi-Fi routers and Apple TV.</p>
<p><b>Matter (language).</b> The Connectivity Standards Alliance's answer to ecosystem lock-in: one certification, one pairing flow, multi-admin support (a device can be shared across ecosystems), and local control by design rather than cloud-dependence. Matter does <em>not</em> run over Zigbee — a Zigbee device joins a Matter home through a <b>bridge</b>, which translates between the two. And a bridge is not the same thing as a border router: a bridge translates languages, a border router connects a Thread mesh to your network. Confusing those two is the second-most-common way a smart-home plan goes wrong.</p>

<h2>The compatibility table people actually need</h2>
<p>Read it by layer: <b>Wi-Fi device</b> → talks to your router directly, pairs to an app, no hub. <b>Thread device</b> → needs a Thread border router somewhere in the house. <b>Zigbee device</b> → needs a Zigbee coordinator (hub), or a Matter bridge to appear inside a modern ecosystem. <b>Matter-certified device</b> → works across ecosystems, regardless of which radio is underneath. The buying translation: prefer Matter certification for anything new; choose Thread underneath for battery devices and Wi-Fi underneath for plugged-in ones; let existing Zigbee gear keep running and bridge it rather than replacing it.</p>

<h2>Does Matter replace Thread — or need a hub?</h2>
<p>Neither, and the questions themselves are the layer mistake. Matter doesn't replace Thread; it <em>uses</em> it (and Wi-Fi, and Ethernet). Does Matter need a hub? Matter over Wi-Fi devices pair straight to your phone and ecosystem app — no hub. Matter over Thread devices need exactly one Thread border router on the network, which increasingly lives in a speaker or router you'd own anyway. That's the whole answer, and it's why the honest future is layered: Matter for interoperability, Thread under battery devices, Wi-Fi under hungry ones, and Zigbee bridged where it already exists. If a seller tells you one protocol "wins", they're selling, not explaining.</p>

<h2>What this means when you're actually shopping</h2>
<p>For each device you're considering, ask two questions — <em>is it Matter-certified?</em> and <em>which radio is underneath?</em> A Matter-over-Wi-Fi plug for a lamp: buy freely, no hub. A Matter-over-Thread door sensor: confirm you have (or buy) a border router first — that's the piece whose absence breaks setups. And if you're starting from zero with a chosen ecosystem, the fastest path is one device that wears several hats — <a href="/tech/smart-home-worth-it/">the hub question is its own decision</a>, covered separately. The layered stack isn't marketing; it's how the pieces genuinely fit.</p>""",
    [("Connectivity Standards Alliance — Matter overview", "https://csa-iot.org/all-solutions/matter/"),
     ("Thread Group — Thread protocol and border router role", "https://www.threadgroup.org/")],
    [("smart-home-worth-it", "Smart home: what's worth it vs gimmicks"),
     ("smart-plug-going-offline", "Why smart plugs go offline"),
     ("wi-fi-setup-mistakes", "The Wi-Fi mistakes that break smart homes"),
     ("wi-fi-router-placement", "Router placement, honestly")]),

    # ------------------------------------------------------------------ #
    # Tier 2 #12: Do you actually need a smart home hub?
    # ------------------------------------------------------------------ #
    ("do-you-need-a-smart-home-hub", "smart-home", "guide",
     "Do you actually need a smart home hub? The honest answer by device type",
     "Hub, controller, bridge, border router — four different jobs wearing similar boxes. What each one does, which devices need which, and the misconception costing people money.",
     """<p>The hub question is really four questions wearing one word, because "hub" gets used for devices doing completely different jobs. Sort the jobs, and the answer to <em>do I need one?</em> becomes obvious per device — not as a lifestyle decision.</p>

<h2>The four jobs, disentangled</h2>
<p>A <b>Thread border router</b> connects a Thread mesh to your Wi-Fi network. A <b>Zigbee coordinator</b> does the same for Zigbee devices. A <b>Matter bridge</b> translates non-Matter devices (like Zigbee bulbs) into Matter so ecosystems can control them. A <b>Matter controller</b> is the software brain — the app or device that pairs and commands Matter devices; your phone's home app is one, and so are smart speakers and hubs. The reason this matters: a box can be all four at once (the best "hubs" are), or just one. When a setup fails, it's usually because someone bought a box that does three of the four jobs and needed the fourth.</p>

<h2>Devices that need nothing but your Wi-Fi</h2>
<p>Matter-over-Wi-Fi and plain Wi-Fi devices — smart plugs, most bulbs, displays, appliances — connect to your router directly and pair to an app. No hub of any kind. This is most people's first tier of smart home, and it needs zero extra hardware — just <a href="/tech/wi-fi-setup-mistakes/">a network set up to handle it</a>. If everything you own is plugged into the wall and Wi-Fi, the hub market has nothing to sell you.</p>

<h2>Devices that need exactly one thing</h2>
<p>Battery-powered Thread devices (sensors, buttons, locks) need one Thread border router somewhere in the house. Zigbee devices need one Zigbee coordinator. That's the whole requirement — not a hub per room, not a hub per brand, one. And because border routers now live inside smart speakers, Apple TVs and some Wi-Fi routers, you may already own one without knowing. Check your ecosystem's app before buying any box: the "add Thread device" flow will tell you whether a border router is present.</p>

<h2>The misconceptions, priced</h2>
<p><b>"Matter means no hub."</b> True for Matter over Wi-Fi; false for Matter over Thread (border router needed) and for bridged Zigbee (bridge needed) — the <a href="/tech/matter-vs-thread-vs-zigbee-vs-wifi/">layer model explains why</a>. <b>"I need Brand X's hub for Brand X devices."</b> Increasingly no: Matter certification is exactly the end of that requirement, within the limits of each platform's support. <b>"A hub makes everything faster."</b> A local controller can beat cloud round-trips, but a badly-placed or overloaded hub makes things worse — placement and radio channels matter more than the logo. The honest shopping order: decide your devices first, then buy the smallest box that covers the missing job — never the other way round. The full worth-it-vs-gimmick pass on devices themselves lives <a href="/tech/smart-home-worth-it/">in the smart home buying guide</a>.</p>""",
    [("Connectivity Standards Alliance — Matter controllers and bridges", "https://csa-iot.org/all-solutions/matter/"),
     ("Thread Group — border routers", "https://www.threadgroup.org/")],
    [("matter-vs-thread-vs-zigbee-vs-wifi", "Matter vs Thread vs Zigbee vs Wi-Fi"),
     ("smart-home-worth-it", "Smart home: worth it vs gimmicks"),
     ("wi-fi-setup-mistakes", "The Wi-Fi mistakes that break smart homes")]),

    # ------------------------------------------------------------------ #
    # Tier 2 #13: Why smart plugs keep going offline
    # ------------------------------------------------------------------ #
    ("smart-plug-going-offline", "smart-home", "troubleshooting",
     "Why smart plugs keep going offline (and the fix order that works)",
     "The 2.4 GHz requirement, the DHCP timeout, the cloud dependency nobody mentions — the diagnostic order for the most-complained-about smart home device, symptom by symptom.",
     """<p><b>The symptom:</b> a smart plug that paired fine, worked for weeks, then shows "offline" in the app — sometimes daily, sometimes after a power cut, sometimes for no reason you can name. The plug is rarely broken. The causes have an order, and testing in that order finds the culprit fastest.</p>

<h2>Cause 1: the 2.4 GHz requirement (check first)</h2>
<p>Most smart plugs are 2.4 GHz-only, and this is the single most common cause. Your router broadcasts both 2.4 and 5 GHz; phones prefer 5 GHz (faster), plugs <em>require</em> 2.4 GHz. Two failure shapes: a <em>band-steering</em> router that moves the plug or its setup traffic onto 5 GHz, or a setup done on a phone that wouldn't drop to 2.4 GHz during pairing. The fixes: give the bands separate names (my-network and my-network-5G) so nothing can be steered, or temporarily disable 5 GHz during pairing. This is also why plugs work fine at the far end of the house where 5 GHz doesn't reach — 2.4 GHz penetrates walls better; <a href="/tech/wi-fi-setup-mistakes/">the band anatomy is worth knowing</a>.</p>

<h2>Cause 2: DHCP address expiry (the weekly-offline signature)</h2>
<p>The router loans each device an IP address for a lease period. When the lease expires, a well-behaved plug renews silently; a poorly-implemented one drops offline instead. The tell: the plug disappears on a regular cadence — every few days, same pattern. The fix: in your router's settings, reserve a static IP for the plug (usually listed under DHCP reservations or address reservations). Two minutes of setup, and the failure mode is gone permanently. This single fix resolves a large share of "randomly offline" plugs.</p>

<h2>Cause 3: router distance and congestion</h2>
<p>2.4 GHz is the crowded band — neighbours' Wi-Fi, microwaves, Bluetooth, other IoT devices. A plug at the edge of range works until congestion peaks, then drops. Diagnose: does it go offline at consistent times (evenings, when every network is busy)? Fix: move the plug one socket closer to the router, or reduce 2.4 GHz congestion — fewer devices on that band, a <a href="/tech/wi-fi-router-placement/">better router position</a>, or channel selection away from the crowd.</p>

<h2>Cause 4: power interruptions (the after-a-storm signature)</h2>
<p>A brief outage is a race: when power returns, the router takes 30-90 seconds to boot; the plug reconnects in 5-10 seconds, finds no router, and some plugs give up instead of retrying patiently. The fix is a firmware-behaviour question — update the plug's firmware (makers have progressively improved reconnect logic), and accept that a power-cycle of the plug (10 seconds off, on again) after an outage is normal behaviour, not a defect. A plug on a surge protector also survives the voltage transients that occasionally scramble cheap electronics.</p>

<h2>Cause 5: the cloud dependency (the honest limitation)</h2>
<p>Many budget plugs route every command through the maker's cloud: your phone → their server → the plug. When their cloud has an outage, your plug is "offline" even though your Wi-Fi is perfect — and this one is not fixable from your side. Diagnose: check the maker's status page or community forums when it happens; if thousands report it simultaneously, it's them, not you. The long-term fix is buying habits: Matter-certified plugs controlled locally don't have this failure mode — <a href="/tech/matter-vs-thread-vs-zigbee-vs-wifi/">local control is one of Matter's actual promises</a>. This is also why a house full of cloud-dependent devices feels flakier than the individual specs suggest.</p>

<h2>The fix order, in one line</h2>
<p>Confirm 2.4 GHz → reserve the IP → improve signal/congestion → update firmware → check the maker's cloud status. In that order, fastest-test first. And if the plug is offline <em>right now</em>: the 10-second power cycle before anything else — it re-runs the whole connection sequence and clears causes 1, 2 and 4 in one move.</p>""",
    [("Thread Group / CSA — local control and Matter certification", "https://csa-iot.org/all-solutions/matter/")],
    [("matter-vs-thread-vs-zigbee-vs-wifi", "Matter vs Thread vs Zigbee vs Wi-Fi"),
     ("wi-fi-setup-mistakes", "The Wi-Fi mistakes that break smart homes"),
     ("smart-home-worth-it", "Smart home: worth it vs gimmicks")]),
]
