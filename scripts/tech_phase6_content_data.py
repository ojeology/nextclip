# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 6 (2026-09-25).

Builds out the smart-home shelf from ten pieces toward a real section, with the
desk's cybersecurity-first, privacy-honest angle. Evergreen mechanics and
decision guidance, no fabricated benchmarks or volatile statistics, dated
official sources only where a source is genuinely needed. Every internal link
points at a page that already exists on this desk.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE6_GUIDES = [

# ---------------------------------------------------------------- SMART HOME (build out the shelf)
("smart-home-updates-the-security-habit-nobody-does", "smart-home", "guide",
"Smart-home updates: the security habit almost nobody keeps",
"The cheap camera and the smart plug are computers that never nag you to update. Here is why that matters more than for your phone, and the low-effort way to stay patched.",
"""<p>People are reasonably good at updating phones and laptops, because those devices insist. Smart-home gear does the opposite: a camera, a plug, a sensor sits there quietly, never prompts, and stays on the firmware it shipped with for years. That silence is the problem, because these are networked computers with cameras, microphones and door locks attached.</p>
<h2>Why the quiet devices are the risky ones</h2>
<p>A smart device usually has fewer defences than a phone, is reachable from your network at all hours, and often exposes a web interface or a cloud login. When a vulnerability is found, the fix arrives as a firmware update — and if the device never tells you, the update never happens. The devices you forget are exactly the ones an attacker hopes you forgot. The general reasoning is the same as <a href="/tech/patch-management-for-humans/">patch management for humans</a>, applied to the gadgets that will not remind you.</p>
<h2>The low-effort habit that covers most of it</h2>
<p>Turn on automatic firmware updates wherever the device offers them, and where it does not, put a recurring calendar note to open each device's app every couple of months and check. Group the checks: do all the cameras at once, all the plugs at once. The goal is not vigilance, it is a rhythm that does not rely on memory. When you add a device, add its update path to the same note so the list stays complete.</p>
<h2>The uncomfortable part: some never get fixed</h2>
<p>Cheap gear sometimes stops receiving updates entirely while still working, which is the subject of <a href="/tech/smart-home-devices-stop-getting-updates/">when devices stop getting updates</a>. That is a buying decision as much as a maintenance one: a device from a maker with a stated support period is a safer long-term buy than a no-name one that is cheaper today and unpatchable next year. Updates are the one habit that quietly decides whether a smart home stays safe or slowly becomes a liability.</p>""",
[],
["patch-management-for-humans", "smart-home-devices-stop-getting-updates"]),

("local-vs-cloud-smart-home-why-it-decides-everything", "smart-home", "guide",
"Local vs cloud control: the choice that decides privacy, reliability and whether it works when the internet doesn't",
"Two identical-looking smart switches can behave completely differently — one runs in your house, one phones home. Here is why that distinction outranks almost every feature.",
"""<p>When you compare two smart devices, the spec sheets look the same and the prices are close, so people choose on brand or looks. But the single most consequential difference is rarely listed prominently: does the device work <em>locally</em>, inside your home, or does every command route through the maker's <em>cloud</em>? That one choice decides privacy, speed, reliability, and whether your lights still work during an outage.</p>
<h2>What cloud control actually means</h2>
<p>With a cloud-only device, your app talks to the maker's server, which talks to the device. Your phone and your bulb may be in the same room and still communicate via a data centre. That adds latency, means the device depends on the internet and on the company staying online, and puts a record of your home's behaviour on someone else's servers. It is the reason a "smart" light can fail to turn on because a service across the ocean had a bad afternoon.</p>
<h2>What local control buys you</h2>
<p>A local device responds on your own network: faster, working without internet, and keeping your data in your house. For anything time-sensitive or private — locks, cameras, lighting — local control is the sturdier foundation. It also survives the company: a device that runs locally keeps working even if the maker's cloud shuts down, which is the resilience argument in <a href="/tech/smart-home-devices-stop-getting-updates/">devices that stop getting updates</a>.</p>
<h2>How this connects to the protocol choice</h2>
<p>Local capability is tied to the radio and standard a device uses, which is exactly what <a href="/tech/matter-vs-thread-vs-zigbee-vs-wifi/">Matter vs Thread vs Zigbee vs Wi-Fi</a> sorts out — some of those standards are designed to run locally, others lean on a cloud. And the privacy stakes for the always-listening devices are spelled out in <a href="/tech/smart-speaker-privacy/">smart-speaker privacy</a>. As a rule: prefer local for locks, cameras and lighting; accept cloud where convenience genuinely outweighs the dependency, and know which of your devices are which before the internet drops.</p>""",
[],
["matter-vs-thread-vs-zigbee-vs-wifi", "smart-speaker-privacy"]),

("smart-home-devices-stop-getting-updates", "smart-home", "guide",
"When the company stops updating your perfectly good device",
"End of support does not brick a gadget — it slowly makes it a risk. Here is what abandonment actually means, how to spot it coming, and what to do when it lands.",
"""<p>A smart device rarely dies. It gets abandoned: the company stops shipping firmware, the app stops being maintained, and one day it no longer works with a new phone or a new standard — while still sitting there, powered on, connected to your network. The hardware is fine; the support underneath it is gone.</p>
<h2>What end-of-support actually changes</h2>
<p>The device keeps doing its job for a while, but it stops getting security fixes, so any flaw found after that date is permanent. It may stop working with updated apps or assistants, and cloud-dependent features can simply switch off when the maker retires a server. This is the concrete downside of the cloud dependency described in <a href="/tech/local-vs-cloud-smart-home-why-it-decides-everything/">local vs cloud control</a>: a local device keeps working; a cloud-only one can be turned off from the other side of the world.</p>
<h2>How to see it coming before you buy</h2>
<p>Prefer makers who publish a support window or a track record of long updates, and be sceptical of very cheap gear from brands with no history — the low price often reflects a short support life you pay for later. Check whether the device runs on an open, durable standard rather than a proprietary cloud only that company operates. The buying logic mirrors <a href="/tech/smart-home-worth-it/">is a smart home worth it</a>: the real cost includes how long the thing stays supported, not just the sticker.</p>
<h2>What to do when a device you own is abandoned</h2>
<p>If it is local-only and still works, you can often keep using it while accepting it will not be patched — segment it on the network, as in <a href="/tech/smart-home-on-its-own-network/">putting smart devices on their own network</a>, so an unpatched gadget cannot reach the rest of your systems. If it is cloud-dependent and the cloud is gone, it may simply be dead, which is the strongest possible argument for buying local where you can. Abandonment is not dramatic; it is a slow leak, and the defence is choosing durable devices and isolating the ones that age.</p>""",
[],
["local-vs-cloud-smart-home-why-it-decides-everything", "smart-home-on-its-own-network"]),

("smart-home-on-its-own-network", "smart-home", "guide",
"Putting your smart devices on their own network (and why it is easier than it sounds)",
"A guest network or a second SSID keeps the cheap, unpatchable gadgets away from your laptop and your files. Here is the practical version most routers already support.",
"""<p>Smart-home gear is the least trustworthy computing you own: cheap, rarely updated, always connected, and made by companies you have never heard of. You would not let a stranger's laptop sit on the same network as your banking and your work files — but that is exactly where most smart bulbs and cameras live. Segmentation is the fix, and it is more accessible than the term suggests.</p>
<h2>What segmenting actually does</h2>
<p>It puts the smart devices on a separate network from your phones, laptops and storage, so that if one of them is compromised it cannot easily reach the devices that hold your data. It does not make any single device safer; it limits the blast radius. An attacker who gets into a camera should find a dead end, not a path to your NAS. It is the network equivalent of the update discipline in <a href="/tech/smart-home-updates-the-security-habit-nobody-does/">the updates habit</a> — neither prevents every problem, together they contain them.</p>
<h2>The practical version most people can do today</h2>
<p>Most routers already offer a guest network or a second SSID. Put the smart devices on it, keep your personal computers on the main one, and make sure the guest/secondary network is set to not allow access to the main network (often called client or AP isolation). That single setting is the whole idea. Devices that must talk to a hub can live together on the isolated side; only the controller bridges over.</p>
<h2>What it pairs with</h2>
<p>Segmentation matters most for the devices most likely to be abandoned and unpatched — the risk laid out in <a href="/tech/smart-home-devices-stop-getting-updates/">devices that stop getting updates</a>. It also limits what an always-listening device can reach, complementing the controls in <a href="/tech/smart-speaker-privacy/">smart-speaker privacy</a>. You do not need enterprise equipment; you need to stop treating a £8 plug as trusted just because it is convenient. One network for things, one for your life.</p>""",
[],
["smart-home-updates-the-security-habit-nobody-does", "smart-speaker-privacy"]),

("smart-home-automations-that-only-mostly-work", "smart-home", "guide",
"Automations that only mostly work: why the magic flickers, and how to make it boring-reliable",
"Automation that fails one time in twenty is worse than no automation, because you stop trusting it. Here is what actually breaks the flaky ones and how to fix the cause.",
"""<p>The complaint about smart homes is rarely "it does nothing" — it is "it works most of the time." A motion light that occasionally stays dark, a routine that fires late, a scene that needs a second tap. That intermittent failure is more corrosive than none at all, because you stop relying on it and start doing the thing manually anyway. The good news is the causes are few and fixable.</p>
<h2>The usual suspects</h2>
<p>Most flakiness traces to a handful of causes. The device drops off the network — the same connectivity loss behind <a href="/tech/smart-plug-going-offline/">a smart plug going offline</a> — so the trigger or the action silently misses. A cloud-dependent automation is delayed or dropped when the round trip through the maker's server hiccups, which is the reliability cost in <a href="/tech/local-vs-cloud-smart-home-why-it-decides-everything/">local vs cloud control</a>. A sensor is marginal on battery or range. Or two automations quietly contradict each other.</p>
<h2>Make the critical paths local and simple</h2>
<p>The single biggest reliability gain is keeping the automations you depend on local, so they do not wait on the internet, and keeping them simple — one clear trigger, one clear action. The more conditions chained together, the more ways for one marginal link to break the chain. For anything that must work every time (a lock, a light on a dark stair), prefer the boring local rule over the clever multi-condition one.</p>
<h2>Fix the connection underneath it</h2>
<p>Flaky automations are often a network problem wearing a costume. If devices drop or lag, the fix is the same as for any wireless trouble — placement and a clean channel, covered in <a href="/tech/wi-fi-router-placement/">router placement</a> and <a href="/tech/wi-fi-setup-mistakes/">common Wi-Fi setup mistakes</a>. A device that is reliably connected makes a reliable trigger. Chase the connection first and half the "random" failures stop being random.</p>""",
[],
["smart-plug-going-offline", "local-vs-cloud-smart-home-why-it-decides-everything"]),

("smart-home-features-behind-a-subscription", "smart-home", "guide",
"When the smart thing you bought needs a monthly fee to do the smart part",
"More devices ship working, then ask for a subscription to keep doing what you bought them for. Here is how to spot it before purchase and decide when it is genuinely worth it.",
"""<p>There is a pattern in smart-home buying now: the hardware works in the shop, and the feature you actually wanted — cloud video history, remote access, the clever detection — sits behind a monthly subscription you discover after setup. It is not always a scam, but it changes the real price of the device, and the honest move is to count that price before you buy, not after.</p>
<h2>What is usually paywalled, and why</h2>
<p>The recurring fee typically covers something that costs the company money every month: cloud storage for camera clips, a server that enables remote control away from home, or ongoing AI processing. That is a more defensible reason to charge than gating a feature that already runs on the device. The thing to distinguish is a subscription paying for real ongoing cost versus one renting back a capability the hardware does locally anyway — the same local-versus-cloud line drawn in <a href="/tech/local-vs-cloud-smart-home-why-it-decides-everything/">local vs cloud control</a>.</p>
<h2>Do the real maths before you buy</h2>
<p>Add the subscription to the hardware over the years you will actually own the device, and compare that total against a device that does the job locally with no fee. A cheaper camera with a £8 monthly cloud plan is often dearer over three years than a pricier one that records to a local card. This is the same arithmetic as the streaming stack in <a href="/tech/streaming-subscription-stacking-when-bundle-cheaper/">subscription stacking</a>: the monthly fee is small and the multi-year total is the number that matters.</p>
<h2>Decide, do not drift into it</h2>
<p>Some subscriptions are worth it — off-site camera backup genuinely protects against theft or fire in a way a local card cannot. The point is to choose deliberately rather than let a free trial silently become a charge, the trap covered in <a href="/tech/free-trial-cancellation-traps/">free-trial cancellation traps</a>. Buy knowing which features are one-time and which are rented, and the smart home stays an asset instead of a slow drip of small bills.</p>""",
[],
["local-vs-cloud-smart-home-why-it-decides-everything", "free-trial-cancellation-traps"]),

]
