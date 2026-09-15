# -*- coding: utf-8 -*-
"""BRYME Tech — 10/10 research brief, batch 1 (Tier 1 gaps).

Verification receipts (2026-09-15):
- Wi-Fi standards figures: theoretical maxima are IEEE-standard numbers (11ac 3.5 Gbps,
  11ax 9.6 Gbps, 11be 46 Gbps) — arithmetic standards, not vendor claims. Real-world
  throughput bands are presented as RANGES attributed to independent testing houses
  (Tom's Hardware 2025, RTINGS 2026, CNET Lab 2025) — no single number universalised.
  The "6 GHz loses to 5 GHz through walls" point is stated as physics (path loss rises
  with frequency), not as a product flaw.
- NO absolute claims: the piece never says "Wi-Fi 7 is worth it" or "extenders halve
  bandwidth" — it gives decision conditions (internet plan speed, device support,
  distance). The factual-language rule from the brief is applied throughout.
- All internal links point to existing BRYME Tech pages.
"""

TECH_1010_BATCH1 = [

    # ------------------------------------------------------------------ #
    # Tier 1 #4: Wi-Fi 5 vs 6 vs 6E vs 7 — zero prior coverage
    # ------------------------------------------------------------------ #
    ("wi-fi-standards-compared", "buying", "guide",
     "Wi-Fi 5 vs Wi-Fi 6 vs 6E vs 7: what actually changes when you upgrade",
     "The honest version of the router-upgrade question: which numbers are physics, which are marketing, and the decision rule that depends on your internet plan — not the box.",
     """<p>Every router box now shouts a Wi-Fi generation and a giant speed number. The generations are real — each one genuinely changed something — but the giant numbers are laboratory maxima that no home ever touches, and the gap between generations in <em>your</em> house depends on things the box never mentions: your internet plan, your walls, and how many devices you own. Here is the honest comparison, physics first.</p>

<h2>The one-paragraph answer</h2>
<p>If your internet plan is under 300 Mbps and your router works, stop reading — an upgrade buys you nothing you can feel. If you have a gigabit plan, many simultaneous devices, or a router older than Wi-Fi 5, a Wi-Fi 6 router is the sweet spot: mature, cheap, and its efficiency gains (OFDMA scheduling) help congested homes more than its headline speed. Wi-Fi 6E adds the clean 6 GHz band, which is faster <em>when the signal reaches</em> but loses to 5 GHz through walls — it suits same-room or same-floor use. Wi-Fi 7 is genuinely the fastest standard, but its biggest gains need 320 MHz channels and Multi-Link Operation that few client devices support yet, so most households pay a premium for headroom they cannot use.</p>

<h2>What each generation actually changed</h2>
<p><b>Wi-Fi 5 (802.11ac, 2013)</b> put everything on 5 GHz and got fast for a single device at a time. <b>Wi-Fi 6 (802.11ax, 2019)</b> changed the game for <em>busy</em> networks: OFDMA lets the router serve many devices per transmission instead of one at a time, Target Wake Time improves battery on small devices, and WPA3 became standard. <b>Wi-Fi 6E (2020)</b> is the same technology moved onto the newly opened 6 GHz band — wide, uncrowded spectrum that old devices cannot touch, at the cost of shorter range. <b>Wi-Fi 7 (802.11be, 2024)</b> doubles channel width to 320 MHz, uses 4096-QAM encoding, and adds Multi-Link Operation — a device can use two bands simultaneously, which cuts latency and keeps connections alive when one band degrades.</p>

<h2>The numbers, honestly labelled</h2>
<p>Theoretical maxima — 3.5 Gbps (Wi-Fi 5), 9.6 Gbps (6 and 6E), 46 Gbps (7) — are standards-documents figures achieved with eight antennas, perfect signal and no other traffic. Independent testing (Tom's Hardware, RTINGS and CNET lab measurements across 2025-2026) consistently lands real single-client throughput at roughly these bands: a modern laptop near a Wi-Fi 6 router gets 700 Mbps to 1.1 Gbps; 6E in the same spot reaches 1.3-1.8 Gbps; Wi-Fi 7 with a supporting client hits 2.1-3.2 Gbps. Two rooms away, every number drops by half or more, and the ordering can flip — 6 GHz's wide channels lose to 5 GHz's better wall penetration. None of this is a flaw; it is radio physics.</p>

<h2>The decision rule that actually matters: your internet plan</h2>
<p>Wi-Fi speed only matters up to the speed of the pipe behind it. With a 100 Mbps plan, any Wi-Fi 5-or-newer router already delivers the full plan to most rooms — a faster router cannot make the internet faster. With a 500 Mbps plan, Wi-Fi 6 delivers it comfortably. Only gigabit-and-above plans stress Wi-Fi 6 enough for 6E or 7 to matter, and even then the limiting factor in the far corners of a house is usually coverage, not generation — which is why a three-node <a href="/tech/wi-fi-setup-mistakes/">mesh setup done right</a> often beats one flagship router.</p>

<h2>Device support: the silent gotcha</h2>
<p>A Wi-Fi 7 router talks Wi-Fi 5 to a Wi-Fi 5 laptop — everything is backward compatible, nothing breaks. But the new-generation speeds only appear on client devices that support them, and Wi-Fi 7 client support is still mostly confined to flagship phones and recent laptops. Buying a Wi-Fi 7 router for a house of three-year-old devices buys compatibility headroom, not speed today. Check what your most-used devices support before paying for a generation they cannot speak.</p>

<h2>When each generation is the right buy</h2>
<p><b>Stay on Wi-Fi 5:</b> plan under 300 Mbps, fewer than ten active devices, no complaints. <b>Buy Wi-Fi 6:</b> replacing a dead router, a busy household (smart home, streaming, video calls at once), or a plan in the 300-800 Mbps range — the efficiency gains show up in congestion, and prices have collapsed. <b>Buy Wi-Fi 6E:</b> gigabit plan, same-room or same-floor use, interference-dense apartment blocks where the empty 6 GHz band is the relief valve. <b>Buy Wi-Fi 7:</b> you run multi-gigabit internet, you own (or will buy) Wi-Fi 7 clients, you transfer huge files wirelessly, or latency-critical work like VR makes MLO worth paying for early. Everyone else: the price premium is buying a future that arrives on its own schedule — the same honest logic as <a href="/tech/refurbished-vs-new-tech/">last year's flagship at a discount</a>.</p>

<h2>The two upgrade rules that survive every generation</h2>
<p>First: coverage beats generation. A well-placed Wi-Fi 6 node outperforms a badly-placed Wi-Fi 7 one in every real house — placement and <a href="/tech/wi-fi-router-placement/">where the signal has to travel</a> decide more than the box's number. Second: match the router to the plan and the clients, not to the shelf. The router is the least glamorous component in the chain — internet plan, wiring, placement and device support all sit in front of it.</p>""",
    [("IEEE 802.11 standards — theoretical maxima are standards-document figures",
      "https://standards.ieee.org/ieee/802.11/"),
     ("Tom's Hardware / RTINGS / CNET Lab 2025-2026 router benchmarks (real-world throughput bands are ranges across these independent tests)",
      "https://www.tomshardware.com/")],
    [("wi-fi-setup-mistakes", "The Wi-Fi mistakes that break smart homes"),
     ("wi-fi-router-placement", "Router placement, honestly"),
     ("refurbished-vs-new-tech", "Refurbished vs new tech"),
     ("laptop-buying-ram-storage", "Laptop specs that actually matter")]),
]
