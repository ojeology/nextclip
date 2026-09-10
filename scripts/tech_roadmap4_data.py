# -*- coding: utf-8 -*-
"""Tech roadmap batch T4 — Smart Home (3) + Subscriptions & Digital Declutter (3).

Verification receipts (2026-09-10):
- Smart-speaker policies [VERIFY gate]: 2019 human-review revelations documented by BBC
  ("extremely small sample" — Amazon statement) and Wired (opt-out flows, Siri opt-in from
  iOS 13.2). Amazon's March 28, 2025 removal of the 'Do Not Send Voice Recordings' option
  (US English: Echo Dot 4th gen, Echo Show 10/15) double-sourced via Malwarebytes (quoting
  Amazon's customer email) and Business Today (citing Ars Technica).
- Subscription spend [VERIFY gate]: C+R Research 2022 (n=1,004 US adults) $86 estimated vs
  $219 itemised — corroborated across independent writeups; West Monroe 89% underestimate
  (year conflicting across aggregators, so no year pinned); Deloitte 2025 Digital Media
  Trends ~4 streaming services / ~$69 per month / +13% YoY (two independent summaries).
  The $273 figure was DROPPED — aggregators attribute it to both C+R and West Monroe.
- FTC click-to-cancel status (added gate for free-trial-traps): rule vacated by the 8th
  Circuit July 8, 2025 before taking effect; ROSCA + state auto-renewal laws + FTC
  enforcement (Sept 2025 $2.5B Amazon Prime settlement) still in force. Sources: Goodwin
  alert (Feb 2026), getuptocode guide (Jul 2026).
- wi-fi-setup-mistakes and subscription-creep-audit are first-hand pieces; no external
  stats claimed, sources left empty on purpose.
"""

TECH_ROADMAP_T4 = [

    # ------------------------------------------------------------------ #
    # 1. Smart home — worth it vs gimmicks
    # ------------------------------------------------------------------ #
    (
        "smart-home-worth-it",
        "smart-home",
        "guide",
        "Smart home devices that are worth it vs. the gimmicks",
        "Most smart home purchases are a solution looking for a problem. A few genuinely earn their socket. Here's the honest sorting, device by device.",
        '''<p>Walk into the smart home aisle and everything promises a life upgrade. Walk out with half of it and you'll spend a weekend babysitting gadgets that mostly re-invent a wall switch. The difference between the devices people keep and the ones that end up in a drawer isn't brand or price — it's whether the device solves a problem you already had.</p>

<h2>The one-question triage</h2>
<p>Before any smart device goes in the basket, ask: <strong>what does this do that the dumb version couldn't, and would I still want that done in a blackout?</strong> Three follow-ups separate the keepers from the clutter:</p>
<p><strong>Does it fail gracefully?</strong> A good smart device still works like its dumb ancestor when the internet drops — a smart bulb stays a bulb from the wall switch, a smart plug stays an on/off socket. A device that bricks without Wi-Fi has made your home <em>less</em> reliable than before you bought it.</p>
<p><strong>Does anything rent back what you bought?</strong> Some devices ship with features locked behind a monthly plan — richer camera history, full-speed modes, "premium" automations. That's not a purchase, it's a lease. Check what the subscription costs and what it guards <em>before</em> buying, because the box never makes it obvious. Subscription sprawl deserves its own audit — <a href="/tech/subscription-creep/">it's how small monthly charges become real money</a>.</p>
<p><strong>Who else lives with it?</strong> A household where one person configures and everyone else suffers is the most common smart home failure mode. If the rest of the family has to learn an app to turn on a lamp, the device loses.</p>

<h2>The boring devices that earn their keep</h2>
<p><strong>Smart plugs.</strong> The best entry point, full stop. Ten-ish units of currency, and suddenly the lamp, the fan and the iron (which you <em>will</em> otherwise drive back home to check) are schedulable and remote. The killer feature isn't automation, it's the answer to "did I leave it on?" from anywhere.</p>
<p><strong>Water leak detectors.</strong> Unsung heroes. A cheap puck under the sink, the water heater or the washing machine that screams at your phone the moment it touches water pays for itself the one time a hose lets go while you're out. No camera, no microphone, no subscription in most cases — pure problem-solving.</p>
<p><strong>Smart bulbs — one room at a time.</strong> Worth it where light has <em>jobs</em>: a warm wind-down routine in the bedroom, lights that come on before you're home. Not worth it as a whole-house swap on day one; a five-unit starter pack of bulbs you control from a phone gets old faster than three scenes you actually use.</p>
<p><strong>Video doorbells.</strong> Genuinely useful — parcel thieves and awkward "were you even home" moments are real problems. But this is the category where the subscription trap lives: the doorbell may be a one-time buy while the recordings cost monthly. Decide the true price including the plan, or accept a doorbell that only shows you live video.</p>
<p><strong>Smart thermostats.</strong> The most honest of the "savings" claims — but the savings depend on your climate, insulation and heating type. Buy it for comfort and scheduling that you'll feel weekly; treat the bill reduction as a bonus, not a promise. No honest review can promise you a specific percentage back.</p>

<h2>The gimmick zone</h2>
<p><strong>Smart kitchen everything.</strong> The kettle, toaster and coffee machine you still walk to the kitchen to fill are not meaningfully improved by pre-heating from the sofa. The walk is not the hard part of making tea.</p>
<p><strong>Voice control as the only interface.</strong> A button is faster than a sentence for most tasks. Voice is a supplement, and if you're weighing privacy alongside convenience, <a href="/tech/smart-speaker-privacy/">it's worth knowing what smart speakers actually listen for</a>.</p>
<p><strong>Mirrors, jars, egg trays.</strong> Categories that exist mostly to demo at trade shows. If the pitch is "now the object you never think about can send notifications", the honest answer is that you never think about it for a reason.</p>
<p><strong>Anything whose demo needs a presenter.</strong> At a friend's house or a store display, if the wow moment requires someone to explain the setup, the thing doesn't sell itself — and it won't run itself either.</p>

<h2>The failure nobody plans for</h2>
<p>Smart home devices outlive their servers. Companies fold, apps get deprecated, accounts get merged into someone else's. The devices that age well are the ones that degrade back to dumb hardware instead of becoming e-waste with a battery. Before buying, a two-minute search for the brand's track record — did past devices keep working after the app changed? — tells you more than any spec sheet.</p>
<p>And almost every "my smart home doesn't work" story is really a network story: the router, the bands, the guest network. <a href="/tech/wi-fi-setup-mistakes/">The Wi-Fi mistakes that quietly break these setups</a> are worth reading before your first purchase, not after your third evening of factory resets.</p>

<p><em>Start with two smart plugs and one leak detector. If six weeks later you want more, you'll know exactly which problem you're buying a solution for — which is more than most smart home owners ever get to say.</em></p>''',
        [],
        [
            ("smart-speaker-privacy", "Smart speaker privacy, honestly"),
            ("wi-fi-setup-mistakes", "The Wi-Fi mistakes that break smart homes"),
            ("subscription-creep", "The subscription creep nobody notices"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 2. Smart speaker privacy — [VERIFY] gate resolved
    # ------------------------------------------------------------------ #
    (
        "smart-speaker-privacy",
        "smart-home",
        "guide",
        "Smart speaker privacy: what they're actually listening for",
        "The microphone isn't the scary part. Retention, human review and a quiet 2025 policy change are — and all three have settings you should check today.",
        '''<p>Every smart speaker conversation eventually hits the same question: is it <em>always listening</em>? The honest answer has two parts — one reassuring, one that deserves your attention. The microphone is designed to wait locally for a wake word ("Alexa", "Hey Google") and only starts sending audio anywhere <em>after</em> it hears one. That part is the standard design and it's the reassuring part. The attention-deserving part is what happens to the audio after the wake word: where it goes, how long it stays, and who else can hear it.</p>

<h2>The part people didn't know about</h2>
<p>In 2019 it emerged that all the major assistants — Amazon, Google, Apple — had human reviewers listening to some fraction of recorded voice commands, to grade how well the software handled them. The BBC reported Amazon's response at the time: reviewers annotated what Amazon called "an extremely small sample of Alexa voice recordings", with safeguards and a "zero tolerance policy" for abuse. The scandal wasn't only that humans listened — it was that <strong>the terms never clearly said so</strong>, and opting out wasn't obvious. Every major vendor then shipped real controls: opt-outs from human grading, deletion tools, auto-deletion timers. Apple went furthest and made human grading opt-in with iOS 13.2 later that year.</p>

<h2>What quietly changed in 2025</h2>
<p>Here's the development most owners missed. Until spring 2025, Alexa offered a setting called <strong>"Do Not Send Voice Recordings"</strong> — device-side processing, your audio never leaving the speaker. Amazon emailed customers in March 2025 that this option would stop working on March 28, 2025. Amazon's stated reason, quoted by Malwarebytes: "As we continue to expand Alexa's capabilities with generative AI features that rely on the processing power of Amazon's secure cloud, we have decided to no longer support this feature." The change applies to US customers on certain newer devices (the fourth-generation Echo Dot, Echo Show 10 and Echo Show 15, set to English); Amazon says voice recordings are now deleted after processing and that you can still stop recordings from being <em>saved</em>. The practical takeaway stands regardless of device: <strong>cloud processing of your voice is now the default path on newer hardware, and the choice left to you is about storage and improvement programs, not transmission.</strong></p>

<h2>The settings that actually matter</h2>
<p><strong>On Alexa</strong> (in the app: Settings, then Alexa Privacy, then Manage Your Alexa Data): turn off the option to help improve Amazon services using your voice recordings; set recordings to auto-delete after three or eighteen months — or choose "don't save recordings"; and enable voice deletion so you can say "Alexa, delete what I just said" or "delete everything I said today".</p>
<p><strong>On Google</strong> (myactivity.google.com, under Web &amp; App Activity): the key switch is "include voice and audio recordings" — unchecking it means your audio isn't retained for review at all. Set auto-delete to three or eighteen months while you're there, and review what's already stored.</p>
<p><strong>On Apple</strong> (Settings, Privacy &amp; Security, Analytics &amp; Improvements): "Improve Siri &amp; Dictation" is the human-grading toggle — off means your recordings aren't used for grading. Since it's opt-in by default, this one mostly matters to confirm it stayed off.</p>
<p>And the most reliable control ever shipped: the <strong>physical mute button</strong> on the device itself. When company is over, or the conversation isn't the speaker's business, a hardware mute beats every software promise.</p>

<h2>What the settings don't fix</h2>
<p><strong>Third-party skills and apps</strong> are governed by their own developers, not by your assistant's privacy dashboard — a setting that limits Amazon's retention says nothing about what a quiz skill does with your answers. Treat skills like phone apps: <a href="/tech/android-app-permissions/">check what permissions they actually need</a>, and delete the ones you don't use.</p>
<p><strong>Shared spaces</strong> are the under-discussed risk. A speaker in a kitchen hears everyone who visits, including people who never agreed to Amazon's terms. Guest mode (on Google) and hardware mute are the polite-host answers; the bedroom is a defensible no-speaker zone.</p>
<p><strong>Your voice data is data.</strong> The same logic that applies to free apps applies here — <a href="/tech/what-free-apps-do-with-your-data/">the data a service collects is part of the price</a>, and it's worth deciding consciously what you're paying.</p>

<p><em>None of this makes smart speakers indefensible. It makes them a trade: convenience for data, with the terms set by the vendor and adjustable — within limits — by you. Five minutes in the privacy settings is the difference between accepting that trade knowingly and accepting it by default.</em></p>''',
        [
            ("Malwarebytes — Amazon disables the option to keep Echo recordings on-device (Mar 2025, quoting Amazon's customer email)", "https://www.malwarebytes.com/blog/news/2025/03/amazon-disables-option-to-store-echo-voice-recordings-on-your-device"),
            ("BBC — Smart speaker recordings reviewed by humans (2019, incl. Amazon's 'extremely small sample' statement)", "https://www.bbc.com/news/technology-47893082"),
            ("Wired — How to keep Siri, Alexa and Google Assistant recordings private (2019, opt-out flows; Siri grading opt-in from iOS 13.2)", "https://www.wired.com/story/keep-siri-alexa-google-assistant-recordings-private/"),
        ],
        [
            ("smart-home-worth-it", "Smart home: worth it vs gimmicks"),
            ("what-free-apps-do-with-your-data", "What free apps do with your data"),
            ("android-app-permissions", "Android app permissions, explained"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 3. Wi-Fi setup mistakes that break smart homes
    # ------------------------------------------------------------------ #
    (
        "wi-fi-setup-mistakes",
        "smart-home",
        "guide",
        "Why smart home setups fail: the Wi-Fi mistakes nobody warns you about",
        "The smart device is almost never the problem. The 2.4 GHz band, the guest network and one silent phone setting are — and every one of them is fixable in minutes.",
        '''<p>Nobody returns a smart bulb because the bulb was bad. They return it because it paired, worked for an evening, and then vanished from the app forever. After watching enough of these failures up close, a pattern holds: the device is rarely the problem — the network setup is. Here are the mistakes that cause most of it, in the order they tend to strike.</p>

<h2>The 2.4 GHz wall</h2>
<p>The single biggest one. Most smart home devices speak only <strong>2.4 GHz Wi-Fi</strong> — the older, slower, longer-range band — because their radios are tiny and cheap. Modern routers broadcast two bands, often merged under <strong>one network name</strong> so your phone hops to whichever is faster. The result is a setup ritual that fails in a way nobody explains: your phone (on 5 GHz) tries to hand the bulb credentials for a network name the bulb can technically see but can't complete setup on, and the app reports "setup failed" with no hint why.</p>
<p>The fix: when a device refuses to pair, <strong>split the bands</strong> in your router settings — name the 2.4 GHz network separately, join it with your phone, set the device up, then switch your phone back. Some routers offer a "smart connect" or IoT band toggle that does this more gracefully. Either way, "it only joins the slow network" is a feature for these devices, not a defect.</p>

<h2>Guest networks that quietly isolate</h2>
<p>Putting smart devices on the guest network feels tidy — until nothing can talk to anything. Most guest networks run <strong>client isolation</strong>: every connected device is blocked from seeing the others, including your phone. That's a privacy feature for visitors and a hard wall for smart home control, because your phone can't reach the bulb it's supposed to control. Devices can end up online-but-unreachable, which looks exactly like a broken product. Smart devices belong on the main network (or a dedicated IoT network you've deliberately configured to allow device-to-phone traffic).</p>

<h2>Your phone is the problem sometimes</h2>
<p>Two phone-side settings ruin onboarding in ways that look like router problems:</p>
<p><strong>VPN.</strong> A phone VPN can block the local network discovery step that smart home apps rely on — the app can't find the new device because its traffic is tunneled somewhere else. If pairing fails and you run a VPN, turn it off for five minutes and try again.</p>
<p><strong>MAC randomisation.</strong> Modern phones use a different fake hardware address per network as a privacy measure — a good feature that becomes a trap when a router has MAC filtering or device limits: the random address gets refused. If your router filters addresses, add the device's real one, or suspend filtering during setup.</p>
<p>And the universal default, because it genuinely is the most common fix: <a href="/tech/why-restarting-fixes-problems/">power-cycle the router and the device</a> before anything clever. It's not superstition — it clears stale network state.</p>

<h2>The password change that orphans everything</h2>
<p>Rotating your Wi-Fi password is good security hygiene with a hidden cost: every smart device holding the old credentials dies silently, one per evening, for weeks — often after the router itself, so the failure looks random. Before changing the password, list what's connected (routers show this), and re-run each device's Wi-Fi setup right after the change. Better: give smart devices their own 2.4 GHz network with its own name and password. Rotating <em>that</em> password stays a ten-minute job instead of a weekend.</p>

<h2>Capacity, placement and the ISP box</h2>
<p>The free router from your internet provider is designed for a household of laptops and phones — not forty always-connected things that wake up at once. If devices drop off in the evenings or in the room farthest from the router, you're likely past the router's comfort zone. Keep placement simple: central, elevated, out of the closed media cabinet. (A metal TV, thick walls and aquariums are all signal enemies.) If the box is old, a modest dedicated router for the smart home — even a second-hand one — is often the cheapest fix there is; the same first-hand logic as <a href="/tech/refurbished-vs-new-tech/">buying refurbished instead of new</a> applies.</p>

<h2>When it still fails</h2>
<p>Work the ladder in order: restart everything, split the 2.4 GHz band, drop the VPN, get off the guest network. If a specific device still won't pair while others do, check whether your phone connects at all on that band — <a href="/tech/phone-wont-connect-to-wifi/">the phone-won't-join-Wi-Fi checklist</a> covers the phone-side causes. Ninety times out of a hundred, the smart device was fine all along.</p>''',
        [],
        [
            ("phone-wont-connect-to-wifi", "Phone won't connect to Wi-Fi"),
            ("smart-home-worth-it", "Smart home: worth it vs gimmicks"),
            ("smart-speaker-privacy", "Smart speaker privacy, honestly"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 4. Subscription creep — [VERIFY] gate resolved
    # ------------------------------------------------------------------ #
    (
        "subscription-creep",
        "subscriptions",
        "guide",
        "The subscription creep nobody notices until the bank statement",
        "Not one big charge — thirty small ones, each defensible, together the size of a utility bill. How the gap between what you think you spend and what you spend gets so wide.",
        '''<p>Subscription creep doesn't announce itself. It's never one big charge — it's a video plan here, a storage tier there, an app that quietly finished its trial, a news site from that one week you followed a story. Each one is defensible. Together, they're the size of a utility bill that never arrives as a single line item.</p>

<h2>The numbers behind the feeling</h2>
<p>This isn't just a vibe — researchers keep measuring the same gap. When C+R Research surveyed US adults in 2022, people estimated their monthly subscription spending at about <strong>$86</strong>. Asked to then go category by category and itemise what they actually pay, the total averaged <strong>$219</strong> a month — roughly two and a half times the guess. A West Monroe survey found <strong>89% of consumers</strong> underestimate their subscription spending. Deloitte's 2025 Digital Media Trends survey put US spending on <em>streaming video alone</em> at about $69 a month across roughly four services, up 13% year over year.</p>
<p>Treat the exact figures as a range rather than a promise — different surveys count different things, and the trackers that promise a precise average disagree with each other. The finding that survives every version of the research is simpler and more useful: <strong>almost everyone underestimates, and the underestimation is not small.</strong> Which means your own number is worse than your guess, whatever it is.</p>

<h2>Why your brain keeps missing it</h2>
<p><strong>The monthly anchor.</strong> Subscription prices are quoted per month because per-month sounds small — and $9.99 does sound small. Run the arithmetic once and it stops: $9.99 a month is about <strong>$120 a year</strong> for one service; a "cheap" $4.99 app tier is $60. Twelve mid-priced subscriptions is a four-figure year. Nobody would hand over $1,200 in one transaction for this bundle. The pricing is designed so you never have to see that transaction.</p>
<p><strong>The dormant charge.</strong> Creep isn't only services you use at a worse price — it's services you don't use at any price. The gym app from January, the meditation app you opened twice, the cloud tier sized for a phone you've replaced. These keep billing precisely because they demand nothing of you.</p>
<p><strong>The odd-month annual.</strong> Annual plans convert the problem: instead of one visible monthly line, a $74.99 charge lands in some random month for a service you barely remember renewing. Many people audit their monthly statement, see nothing suspicious, and never meet the annual lines at all.</p>
<p><strong>The ratchet.</strong> Prices on existing subscriptions rise — and the rise is charged to a card that's already on file, with a receipt email as the only announcement. Staying subscribed through three quiet increases is the default outcome of doing nothing at all.</p>

<h2>The accelerators</h2>
<p>Bundling blurs the lines further: the music plan that came with the phone deal, the storage that came with the laptop, the streaming bundle that seemed cheaper than its parts (until you wanted two of the four parts). Family plans multiply seats nobody uses. And free-to-paid conversions are the classic on-ramp — <a href="/tech/free-trial-traps/">the trial ends, the first real charge lands, and the service was designed so you wouldn't notice</a>.</p>
<p>There's an escape hatch worth knowing here too: whole categories that used to be rent-only have one-time-purchase or genuinely free options now — <a href="/tech/affinity-now-free/">professional-grade creative software with no subscription at all</a>, or <a href="/tech/free-software-alternatives/">the free canon for everyday software</a>.</p>

<h2>Signs it's already you</h2>
<p>Any one of these is a diagnosis: four or more streaming services and you still "can't find anything"; a free trial older than a month that you can't name; statement lines you have to look up; subscriptions in a currency or an app store you'd forgotten you used; and the quiet one — you can't say, from memory, what your total comes to. If that landed, don't guilt-spiral: creep is the designed outcome of a business model, not a personal failing.</p>

<h2>The fix is an afternoon, not a lifestyle</h2>
<p>You don't need to live subscription-free. You need to see the list once, keep what earns its place, and put a mechanism in place so the list can't silently regrow. That mechanism is a proper audit — every recurring line, every app store, every annual renewal date pinned to a calendar. <a href="/tech/subscription-creep-audit/">The full audit, step by step, is here</a>; it takes about an hour the first time and twenty minutes a season after that.</p>''',
        [
            ("C+R Research 2022 figures ($86 estimated vs $219 itemised) — summary table via Substract", "https://www.substract.co/blog/average-subscription-spending"),
            ("Deloitte 2025 Digital Media Trends (streaming spend) and West Monroe 89% — summary briefing", "https://visionarynetwork.co.uk/2026/04/06/subscription-spending-household-budgets-and-consumer-behaviour/"),
        ],
        [
            ("subscription-creep-audit", "The full subscription audit"),
            ("free-trial-traps", "Free trial traps"),
            ("what-free-apps-do-with-your-data", "What free apps do with your data"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 5. The actual subscription audit
    # ------------------------------------------------------------------ #
    (
        "subscription-creep-audit",
        "subscriptions",
        "guide",
        "How to actually audit every subscription you're paying for",
        "One hour, one statement walk, one app-store pass, four questions per service. The audit that finds the charges your memory dropped — and keeps them from coming back.",
        '''<p>Most "cancel your subscriptions" advice fails at step one, because memory is exactly the tool subscriptions are built to bypass. An audit that works doesn't start with what you <em>think</em> you pay. It starts with what your money actually does. Here's the full pass — about an hour the first time, twenty minutes a season after that.</p>

<h2>Step 1: the statement walk</h2>
<p>Open your bank and card statements — every account and every card, because subscriptions love the backup card — and walk the last <strong>three months</strong>, writing down every recurring or recurring-shaped line: the obvious ones, the renamed ones (billing descriptors are often a company's legal name, not the brand you know), and the small ones you'd wave past. The three-month window catches monthly plans; then scroll <strong>twelve</strong> looking for the annuals — the single larger charges that only appear once a year, landing in whatever month you first signed up.</p>
<p>Parallel path, same pass: search your email for "receipt", "invoice", "renewed", "your subscription" and "thank you for your payment". Receipt mail catches services billed through methods your statement walk might miss, and the dates in those emails tell you each service's renewal rhythm.</p>

<h2>Step 2: the app-store and platform pass</h2>
<p>Subscriptions bought through an app store never appear the way you expect on a card statement — they're bundled under the store's name. Both major phone platforms have a subscriptions screen (search "subscriptions" in the phone's settings, or in the store app's account section) that lists every active plan, the price and the next charge date. Check it even if you believe you have nothing there. Do the same for any payment platform you use — PayPal and similar services list "automatic payments" or pre-approved merchants, a classic resting place for half-forgotten plans.</p>

<h2>Step 3: four questions per service</h2>
<p>With the full list in front of you, each subscription gets the same four questions, in order:</p>
<p><strong>When did I last use it — honestly?</strong> Not "could I use it", not "I might need it". Opened, deliberately, in the last month? If the honest answer is no, it's on the shortlist regardless of price.</p>
<p><strong>Would I start it again today, at today's price?</strong> This reframes the decision. A service you'd re-buy today at full price is earning its keep. One you'd only keep because cancelling is a hassle has just told you the hassle is the product.</p>
<p><strong>Is there a cheaper version of the same thing?</strong> Before cancelling anything you <em>do</em> use: downgrades are under-used. Individual instead of family, one streaming service at a time instead of four stacked, the annual plan only for the keepers. When a cheaper rival does the same job, that's a swap worth testing — this desk keeps one as a case study: <a href="/tech/lyra-vs-spotify/">a cheaper music service held up against the default</a>.</p>
<p><strong>Does a one-time-purchase or free option exist?</strong> Some categories have genuinely escaped the rent model — <a href="/tech/affinity-now-free/">professional creative software you buy once</a>, <a href="/tech/notion-free-plan/">a free plan that's actually usable</a>, <a href="/tech/free-software-alternatives/">the free canon for the everyday tools</a>. Swapping one $12-a-month habit for a one-time buy is a raise you pay yourself.</p>

<h2>Step 4: the cancellation mechanics</h2>
<p>Two facts people learn the hard way. First, <strong>cancelling is not deleting</strong> — in most services your account and data survive cancellation, so "I'll lose my photos" is almost never a reason to keep paying. Second, check what cancellation does to your remaining access: many services keep you active until the end of the period you've paid for; some cut you off immediately. It changes <em>when</em> to cancel, not whether. And a practical trick for the borderline cases: cancel, then wait. If you genuinely miss the service in a month, resubscribing takes ninety seconds — that's the entire strength of their business model, working for you this time.</p>

<h2>Step 5: make the list unable to regrow</h2>
<p>The audit fails if creep restarts next month. Three cheap mechanisms close the loop. <strong>Calendar the annuals:</strong> for every plan that renews yearly, a calendar entry three days before the charge, titled with the price — "Renews: X, $74.99". Deciding <em>before</em> the charge beats noticing after. <strong>Trials get a calendar entry too,</strong> set the day you sign up, before the first charge — <a href="/tech/free-trial-traps/">the trial-to-paid conversion is the whole trap, and a dated reminder defuses it</a>. <strong>Re-run the walk seasonally:</strong> a twenty-minute statement skim at the change of each season catches the new lines while they're still young.</p>

<p><em>The end state isn't zero subscriptions. It's a list where every line would survive the four questions — which is exactly what the subscription business model is built to stop you from ever finding out.</em></p>''',
        [],
        [
            ("subscription-creep", "Why the creep happens"),
            ("free-trial-traps", "Free trial traps"),
            ("affinity-now-free", "One-time-purchase software, tested"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 6. Free trial traps
    # ------------------------------------------------------------------ #
    (
        "free-trial-traps",
        "subscriptions",
        "guide",
        "Free trial traps: the cancellation mistakes that cost real money",
        "The trial is free. The conversion is automatic. The only variable is whether the charge lands on someone who wrote it down — here's how to be that person.",
        '''<p>Free trials are one of the internet's best deals and one of its most reliable money leaks — often in the same week. The leak isn't the trial itself; it's the <strong>conversion</strong>, and the fact that it's automatic by design. The subscription business calls this "negative option": you're charged unless you act. Knowing that, the entire defence fits in one habit — never let a trial's end date live only in your memory.</p>

<h2>Why the charge always surprises someone</h2>
<p>The mechanics are simple: you enter a card, you get 7 or 14 or 30 days, and on day 8 or 15 or 31 the card is charged the full price unless you cancelled first. The system is legal almost everywhere precisely because you agreed — the consent was in the terms you accepted, and the reminder (if any) is the seller's choice, not your right. Five mistakes do most of the damage:</p>
<p><strong>1. No record of the date.</strong> The trial starts on a busy Tuesday; day 14 arrives the way all days arrive. If the end date exists nowhere except in your head, consider it already forgotten.</p>
<p><strong>2. The main card.</strong> Trials signed up with your everyday card are invisible — one more line among groceries and fuel. Charges on a card you check weekly blend in; charges on a dedicated card stand out immediately.</p>
<p><strong>3. Cancelling on the last day.</strong> The deadline logic is backwards: the safe move is to cancel on <em>day one</em>, not the final afternoon. The forgotten trial at 11pm on expiry day is how a free month becomes a year — the first real charge is the cheapest moment to have prevented it.</p>
<p><strong>4. Assuming cancel means lose it now.</strong> Many services keep your access until the trial's end even if you cancel early; some cut you off instantly, and a few don't say clearly which they do. It takes ten seconds to check the cancellation page — and knowing which kind you're in tells you whether to cancel today or set the reminder instead.</p>
<p><strong>5. The long-con trial.</strong> "Three months free with your new device." "A year of the premium tier included." Long trials convert at <em>annual</em> prices — often $50–100+ — and no calendar entry you made this month will still be alive when they land. The longer the trial, the more the reminder matters, and the more it should be set for the conversion date, not the signup date.</p>

<h2>The defence stack</h2>
<p><strong>The calendar entry, with the price in the title.</strong> Same day you sign up: entry on the day <em>before</em> expiry, titled "If ignored, card charged $X — cancel or keep". The price in the title is what turns a nag into a decision; the day-before buffer absorbs timezone and processing quirks. For long-con trials, set the reminder for the conversion date and let it live in the calendar for a year — that's exactly what calendars are for.</p>
<p><strong>A dedicated card for trials.</strong> A virtual or prepaid card — where the service accepts one, and some refuse prepaid, which is itself informative — turns every conversion into a declined charge you'll actually see. No dedicated card? At minimum use one card for <em>all</em> trials so the statement walk has a single place to look. (This pairs directly with the audit habit: <a href="/tech/subscription-creep-audit/">the statement walk catches what the reminders miss</a>.)</p>
<p><strong>An email rule for receipts.</strong> Any email containing "receipt", "invoice" or "your subscription renews" auto-filed into one folder. Conversions always send mail; the problem is only that it arrives among two hundred others. The rule makes every charge knock loudly.</p>
<p><strong>Prefer store-managed trials where possible.</strong> Trials through your phone's app store can be reviewed and cancelled from one subscriptions screen, and the store's receipt emails are consistent — a small structural advantage over trusting each website's cancellation page.</p>

<h2>What the law does and doesn't do for you</h2>
<p><em>(United States, current as of September 2026 — general information, not legal advice.)</em> US federal law — the Restore Online Shoppers' Confidence Act (ROSCA) — already requires subscription sellers to clearly disclose the terms before charging, obtain your express informed consent, and provide a <strong>simple mechanism to stop the recurring charges</strong>. The stronger-sounding "click-to-cancel" rule the FTC finalised in 2024 — which would have added explicit requirements like cancelling as easily as signing up — was <strong>vacated by a federal appeals court on July 8, 2025, before it ever took effect</strong>, on procedural grounds; states including California have since tightened their own auto-renewal laws. Enforcement didn't stop with the rule: the FTC's actions over difficult cancellations continue — its September 2025 settlement with Amazon over Prime enrolment and cancellation was reported at about $2.5 billion. Outside the US, the practical toolkit above doesn't depend on any of this: your calendar entries work under every legal system, and if a charge lands unfairly, your card's <strong>dispute/chargeback process</strong> exists precisely for it.</p>

<p><em>Free trials are worth taking — the genuinely free month is real value, and the free plans that stay free are worth knowing too. The whole game is refusing to hold the expiry date in your head. Write it down once, and the trap doesn't spring.</em></p>''',
        [
            ("Goodwin — FTC 'click-to-cancel' rule status after the 8th Circuit vacatur; ROSCA duties and enforcement (Feb 2026)", "https://www.goodwinlaw.com/en/insights/publications/2026/02/alerts-practices-ba-ftcs-click-to-cancel-rule-gets-new-life"),
            ("Up To Code — FTC auto-renewal rules: what still applies in 2026 (ROSCA, California ARL, Amazon settlement)", "https://getuptocode.com/guides/ftc-auto-renewal-click-to-cancel"),
        ],
        [
            ("subscription-creep-audit", "The subscription audit"),
            ("notion-free-plan", "Free plans vs free trials"),
            ("subscription-creep", "Subscription creep"),
        ],
    ),
]
