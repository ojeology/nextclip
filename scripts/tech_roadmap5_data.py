# -*- coding: utf-8 -*-
"""Tech roadmap batch T5 (finale, part A) — Buying (2) + Troubleshooting (2) + Privacy (2).

Verification receipts (2026-09-10):
- No external statistics claimed in these six pieces; they are engineering-reasoning and
  first-hand protocol pieces. Pixel-density and screen-size figures are plain arithmetic
  (e.g. 1920x1080 at 24 inches is about 92 ppi), not sourced claims.
- vpn-what-it-protects deliberately avoids VPN market sizing and "hack" anecdotes; it
  describes what the technology does and does not do. Free-VPN danger framed behaviourally.
- browser-privacy-settings describes settings by concept (menu names drift between browser
  versions on purpose) and makes no per-browser version claims.
"""

TECH_ROADMAP_T5 = [

    # ------------------------------------------------------------------ #
    # 1. Phone buying: specs that matter vs marketing numbers
    # ------------------------------------------------------------------ #
    (
        "phone-buying-specs-that-matter",
        "buying",
        "guide",
        "Phone buying mistakes: specs that matter vs. marketing numbers",
        "Launch events argue about megapixels and gigahertz because they're easy to say out loud. The specs that decide whether a phone is still pleasant in year three get a slide at most.",
        '''<p>Phone marketing has a stable shape: the biggest number in the room gets the keynote. But three years into ownership, the specs that decided your experience are rarely the ones that got the applause. Here's the honest sorting — what to weigh, what to glance at, and what to ignore.</p>

<h2>The spec you can't undo: storage</h2>
<p>Start with the only purchase you can't reverse later. Phones can't take storage cards any more, and cloud storage is a rental, not a fix — <a href="/tech/storage-full-breaking-apps/">a full phone breaks apps in ways that look like bugs</a>. The base storage tier exists to make the launch price look better; it's the marketing number doing the most damage. Buy one tier above what you use today, because photo libraries only grow — the same reasoning as <a href="/tech/laptop-buying-ram-storage/">buying a laptop you can't upgrade later</a>, which this desk has written about before. RAM is similar but gentler: a mid-tier amount is fine, the absolute floor tier ages fastest.</p>

<h2>The chip: one tier of headroom beats a flagship logo</h2>
<p>The processor decides how long the phone stays pleasant, because software grows heavier every year while silicon stays fixed. You don't need the flagship chip — you need <em>enough</em> chip that the OS updates of years two and three don't hurt. A last-generation flagship chip or a good current mid-range chip both clear that bar; last year's budget chip does not. Practical proxy: reviews that test the phone <em>after updating it</em>, not at launch. And the slowdown you're buying headroom against is real and explained here — <a href="/tech/why-phones-slow-down/">why phones slow down isn't always age</a>.</p>

<h2>The camera: ignore the megapixel count almost entirely</h2>
<p>Megapixels measure size, not quality. A 200-megapixel sensor behind a tiny lens produces worse photos than a 12-megapixel one with good optics and stabilization, and phone makers know it — which is why the number survives in ads. What actually predicts photos: optical image stabilization (a mechanical feature, genuinely scarce below the mid tier), sensor size, and how good the processing is in <em>low light</em>, because that's where phones differentiate. The honest shortcut: skip the spec sheet, look at same-scene comparison shots in reviews — especially night shots.</p>

<h2>The screen: two numbers, only one matters</h2>
<p>Resolution stopped being a differentiator years ago — beyond a certain pixel density, human eyes at phone distance can't tell, which is why every phone says "HD-class" in a different way. What you <em>can</em> see daily is refresh rate: a 120 Hz screen makes scrolling visibly smoother than 60 Hz on day one and every day after. If a launch event spends two minutes on resolution and one on refresh rate, it's spent them backwards.</p>

<h2>Battery: capacity plus habits, not wattage theatre</h2>
<p>Battery capacity (the milliamp-hour number) is worth comparing within the same phone size class. Charging wattage is marketed hard, but the honest version: fast charging is about convenience top-ups, and running a battery at its thermal limit all the time trades long-term health for speed. A phone that charges somewhat slower and charges <em>wirelessly</em> too may age better than the wattage champion. What kills daily battery life in practice is software — bad apps, full storage, old background cruft — more than the spec sheet.</p>

<h2>The numbers that are pure theatre</h2>
<p><strong>Gigahertz.</strong> A clock speed in isolation compares nothing — chip design matters more than the frequency, which is why a "slower" modern chip beats an older "faster" one. <strong>Zoom digits.</strong> "100x zoom" is mostly software guessing; the useful number is the optical zoom range, which is small and honest. <strong>8K video.</strong> You have no 8K screen and the files are enormous; this checkbox exists because it photographs well on a slide. <strong>AI acronyms.</strong> Every phone now has an AI story; the features that matter work offline, and the rest deserve <a href="/tech/ai-useful-vs-hype/">the useful-versus-hype test</a> like any other AI pitch.</p>

<p><em>The pattern across all of it: marketing numbers are the ones you can say loudly in a sentence; the specs that matter are ratios, sizes and tiers that need context. If a launch price feels too good, it's the storage tier. If a camera sounds magical, check night shots. And if the deal is on last year's flagship, that's often genuinely the sweet spot — <a href="/tech/refurbished-vs-new-tech/">refurbished or discounted prior-gen</a> is where the spec-per-unit-currency peaks.</em></p>''',
        [],
        [
            ("laptop-buying-ram-storage", "Laptop RAM and storage, honestly"),
            ("refurbished-vs-new-tech", "Refurbished vs new tech"),
            ("why-phones-slow-down", "Why phones slow down"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 2. Monitor buying: resolution and refresh rate, simply
    # ------------------------------------------------------------------ #
    (
        "monitor-buying-specs",
        "buying",
        "guide",
        "Monitor buying mistakes: resolution and refresh rate, explained simply",
        "Two numbers dominate monitor boxes and most buyers overpay for the wrong one. Which you need depends on one question: documents or motion?",
        '''<p>Monitor shopping collapses into two headline numbers — resolution and refresh rate — and most confusion comes from treating them as rivals. They answer different questions. Resolution is <em>how much fits on the screen and how sharp it looks</em>. Refresh rate is <em>how smooth motion looks</em>. Buy the one that matches what your eyes actually do all day, and you can stop thinking about the rest.</p>

<h2>Resolution: sharpness is about pixel density, not the label</h2>
<p>"4K" sounds like a quality tier, but sharpness depends on pixels per inch — resolution divided by screen size. The arithmetic is simple and worth doing once: a 24-inch 1080p monitor is about 92 pixels per inch (perfectly crisp at a desk); a 27-inch 1080p is about 82 (noticeably softer); a 27-inch 1440p is about 109; a 27-inch 4K is about 163 (sharper than most eyes need at arm's length). This is why a small "lesser" monitor can look better than a big "premium" one: a 4K label on a huge panel can still end up modestly dense.</p>
<p>Practical tiers, no theatre: <strong>1080p is fine up to 24 inches</strong>. <strong>1440p is the sweet spot at 27 inches</strong> — sharp enough, and easier for a modest computer to drive than 4K. <strong>4K earns its cost at 27 inches and up</strong> if you read and write text all day or work with fine detail. And note what resolution demands: pushing four times the pixels needs a real GPU. A 4K monitor on a weak laptop can feel <em>slower</em> than 1440p — the same false-economy trap as <a href="/tech/laptop-buying-ram-storage/">buying spec labels without the hardware to feed them</a>.</p>

<h2>Refresh rate: the number you feel before you notice</h2>
<p>A 60 Hz screen redraws 60 times a second; 144 Hz redraws 144. The effect on a static document is invisible. The effect on <em>motion</em> — scrolling, dragging windows, cursor movement, games — is immediate and a little spoiled-forever: most people who move to a high-refresh display can't go back without complaining. So the rule: <strong>if you play games or scroll all day, refresh rate is the money spec</strong>; a 1440p 144 Hz panel beats a 4K 60 Hz one for feel. <strong>If you read, write and browse, 60 Hz costs you nothing</strong> — spend the budget on resolution or panel quality instead.</p>

<h2>The number nobody markets: what your device can output</h2>
<p>A monitor can't display what the computer won't send. Before buying, check two boring things: your device's video output (a laptop's USB-C port may carry display signal or only power — the manual, not the marketing) and the cable standard. A gorgeous 144 Hz panel connected with an old cable quietly runs at 60 Hz, and nothing warns you. This is the monitor equivalent of <a href="/tech/phone-buying-specs-that-matter/">buying a phone for numbers the hardware can't actually use</a> — the port is the spec that gates everything else.</p>

<h2>Panel type and the honest extras</h2>
<p>Three letters describe the panel and they matter more than HDR stickers: <strong>IPS</strong> (accurate colour, wide viewing angles — the default for most people), <strong>VA</strong> (deeper contrast, slightly slower feel), <strong>TN</strong> (fast and cheap, washed-out from an angle — now mostly for competitive gaming on a budget). On HDR: budget-monitor "HDR" is usually a compliance label — real HDR needs brightness and dimming that cheap panels don't have. Treat sub-premium HDR as marketing until proven otherwise. Curved screens are preference, not performance; ultrawide is a workflow choice that 1080p-era marketing has nothing to do with.</p>

<p><em>Decision in three lines: desk work up to 24 inches — 1080p 60 Hz, spend on the panel. Everything-round at 27 — 1440p 144 Hz, the modern default. Text-heavy professional at 27-plus — 4K, and check your ports first. And if the budget is tight, a previous-year model in the right tier beats this year's sticker — the same logic as <a href="/tech/refurbished-vs-new-tech/">buying refurbished tech</a> everywhere else.</em></p>''',
        [],
        [
            ("phone-buying-specs-that-matter", "Phone specs that matter"),
            ("laptop-buying-ram-storage", "Laptop RAM and storage, honestly"),
            ("refurbished-vs-new-tech", "Refurbished vs new tech"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 3. Wi-Fi router placement
    # ------------------------------------------------------------------ #
    (
        "wi-fi-router-placement",
        "smart-home",
        "guide",
        "Wi-Fi router placement mistakes that are quietly killing your speed",
        "Same internet, same plan, half the speed — because the router lives in a corner, inside a cabinet, behind a television. Placement is the free upgrade nobody claims.",
        '''<p>Before you pay for a faster plan or a new router, there's a free upgrade available in most homes: move the one you already have. Router placement is the difference between a signal that reaches the far bedroom at half strength and one that doesn't — and the bad placements are bad for reasons that are pure physics, not brand rivalry.</p>

<h2>Central, elevated, in the open</h2>
<p>Wi-Fi is radio. It spreads out from the antenna in every direction, which means the router's job is to sit roughly in the middle of the space it serves — not where the internet <em>enters</em> the home, which is usually the worst corner. Two adjustments do most of the work: get it <strong>off the floor</strong> (tables and shelves, high furniture is better — floor-level signals fight furniture and feet) and get it <strong>out of the cabinet</strong> (closed wooden or metal furniture is a box around your antenna). The installers put the connection point by the front door; the cables can usually reach further than you think, or be extended for pocket change.</p>

<h2>The enemy list</h2>
<p>In rough order of guilt: <strong>metal</strong> (the TV is a metal slab — a router behind it broadcasts into the wall; mirrors and fridges similar), <strong>water</strong> (aquariums are signal black holes), <strong>thick masonry</strong> (concrete and brick eat signal; drywall barely notices), <strong>the microwave</strong> (it shouts on the same 2.4 GHz band — if video calls stutter when someone cooks, that's why), and <strong>other electronics stacked on it</strong> (a router shelf shared with speakers and a set-top box is interference soup). None of this needs expert diagnosis: walk the house with your phone's Wi-Fi speed while someone watches the router — the dead spots tell you the story.</p>

<h2>Antennas, distance and the band split</h2>
<p>If your router has adjustable antennas, don't point them all straight up: mixing orientations (one vertical, one horizontal) matches real-world device positions better. And distance hits the two bands differently — 2.4 GHz travels farther through walls but is slower and crowded; 5 GHz is fast but fades fast. This is why the far bedroom "has Wi-Fi but it's useless": it's clinging to the far edge of one band. Placement fixes what placement broke; the deeper band mechanics — and the setup traps they cause — are in <a href="/tech/wi-fi-setup-mistakes/">the Wi-Fi mistakes piece</a>.</p>

<h2>When moving it isn't enough</h2>
<p>Big homes, thick walls and multiple floors genuinely exceed one router's reach. The honest ladder, cheapest first: <strong>move the router</strong> (free), <strong>reposition once more with the dead-spot walk</strong> (free), <strong>a wired access point</strong> if an ethernet path exists (the gold standard — a cable to the far zone beats any wireless trick), <strong>a mesh system</strong> for whole-home coverage without cables, and <strong>extenders</strong> only with realistic expectations — they halve throughput by design and add a second network name to manage. An extender at the edge of the good signal repeating a weak signal is money spent twice for the same disappointment.</p>
<p>One more honest note: placement also decides how well everything <em>on</em> the network behaves — the same physics that makes your laptop's video stutter is what makes smart devices drop off, which is why <a href="/tech/smart-home-worth-it/">smart home failures</a> and this piece share a root cause. And if devices simply won't stay connected at all, that's usually setup rather than placement — <a href="/tech/phone-wont-connect-to-wifi/">the phone-won't-join checklist</a> covers the phone side.</p>

<p><em>Do the free things first: central, elevated, open air, antennas mixed, dead-spot walk once a year or after any furniture change. Half of "our internet is slow" is actually "our router is decorative."</em></p>''',
        [],
        [
            ("wi-fi-setup-mistakes", "The Wi-Fi mistakes that break smart homes"),
            ("phone-wont-connect-to-wifi", "Phone won't connect to Wi-Fi"),
            ("smart-home-worth-it", "Smart home: worth it vs gimmicks"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 4. Computer fans loud — and when it's a warning
    # ------------------------------------------------------------------ #
    (
        "computer-fans-loud",
        "windows",
        "guide",
        "Why your computer fans are loud — and when that's actually a warning sign",
        "Fans are the machine's only cooling, and they get loud for honest reasons: dust, heat, or a runaway process. Sometimes the roar is a symptom, though — here's how to tell which.",
        '''<p>A computer's fans are its lungs and its cooling system in one: everything inside that computes also heats, and the only thing carrying that heat out is air moved by those fans. So noise is usually information, not malfunction. The skill worth having is telling <em>working-as-designed noise</em> from <em>something's-wrong noise</em> — and the diagnosis is mostly common sense once you know what the fan is reacting to.</p>

<h2>Normal: burst, then calm</h2>
<p>Fans are supposed to spin up under load and settle when the load passes. Opening forty tabs, starting a video call, launching a game or installing an update all spike heat; the fans respond within seconds and drop back within minutes. That's the system working. What's <em>not</em> normal is the same roar at <strong>idle</strong> — machine untouched, nothing open, fans at takeoff. That means heat is trapped or something is silently consuming the processor, and both are fixable.</p>

<h2>Cause one: dust (the most common by far)</h2>
<p>Dust is insulation where insulation is the enemy: a fuzzy blanket on the heatsinks and fans that stops heat leaving. Machines used on floors, on carpet, or in pet households clog fastest — often within a year to the point of constant fan noise. The fix is mechanical: power off, unplug, take it (or a laptop, carefully) somewhere ventilated, and use short bursts of <strong>compressed air</strong> through the vents and intakes until the dust stops flying. Hold fans still while blowing if you can reach them — spinning them with compressed air can over-speed them. Laptops used on beds and blankets inhale their own bedding fibres; a hard surface is not a stylistic preference, it's the intake path.</p>

<h2>Cause two: a runaway process</h2>
<p>Sometimes the processor is pinned at idle-temperature-defying load by software, not dust. Your operating system's activity monitor (Task Manager on Windows, Activity Monitor on macOS) sorts by processor use — the culprit is usually at the top: a browser tab running away, a stalled updater, a sync client looping, or malware in the worst case. Close it; the fans answer within seconds. If the machine is <em>also</em> generally sluggish, that's the same investigation with a wider net — <a href="/tech/why-is-my-computer-slow/">the slow-computer triage order</a> covers it, and <a href="/tech/why-restarting-fixes-problems/">a restart clears the most common variant outright</a>.</p>

<h2>Cause three: failing hardware — the actual warnings</h2>
<p>Three fan behaviours deserve real urgency. <strong>New rhythms</strong> — grinding, clicking or rattling from the case mean a bearing is dying; a fan is a cheap part, but one that stops entirely means a machine that overheats and shuts down. <strong>Shutdowns under load</strong> — the machine turning itself off during games, video calls or heavy work is thermal protection tripping; treat it as the computer's fire alarm, not a fluke to restart through. <strong>Maxed fans at true idle after a cleanup</strong> — dust removed, processes clear, still roaring: that's a cooling system (or sensor) failing, and the machine needs service. Laptops that run hot and throttle to slowness under modest load are in the same family — the cooling path is compromised.</p>

<h2>The prevention that's boring and works</h2>
<p>Vents need inches of clearance, not upholstery. Intakes collect dust on a schedule, so the compressed-air ritual — every six months or so, more with pets — keeps fans quiet for the machine's whole life. Storage pressure isn't a fan issue, but overall system health reading is the same discipline as <a href="/tech/storage-full-breaking-apps/">keeping storage from silently breaking things</a>: cheap maintenance, catastrophic neglect.</p>

<p><em>Fans are the one component that announces every problem out loud. Listen for the change in the noise, not the noise itself: bursts are normal, sustained idle roar is dust or a process, and new mechanical sounds or heat shutdowns are service calls.</em></p>''',
        [],
        [
            ("why-is-my-computer-slow", "Why your computer is slow"),
            ("why-restarting-fixes-problems", "Why restarting fixes things"),
            ("windows-update-problems", "Windows update problems, triaged"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 5. VPNs: what they protect and what they don't
    # ------------------------------------------------------------------ #
    (
        "vpn-what-it-protects",
        "safety",
        "guide",
        "VPNs explained: what they protect and what they don't",
        "A VPN is a useful, narrow tool sold as a magical wide one. It encrypts your traffic up to a point and hides your address — and the list of things it doesn't do is longer than the ads admit.",
        '''<p>VPN advertising promises anonymity, safety and invisibility in one subscription. The technology underneath is genuinely useful — and much narrower than the ads. A VPN does exactly one structural thing: it builds an encrypted tunnel from your device to a server operated by the VPN company, and your traffic exits to the internet from there. Everything it does and doesn't do follows from that one sentence.</p>

<h2>What the tunnel actually buys you</h2>
<p><strong>Protection from the local network.</strong> On café, hotel or airport Wi-Fi, everyone's traffic shares the same air and the same router. With a VPN, an eavesdropper on that network sees encrypted tunnel traffic to one address — not which sites you visit or what you send. This is the original, legitimate use case, and it pairs with the judgement calls in <a href="/tech/public-wifi-risks/">why public Wi-Fi is riskier than people think</a>.</p>
<p><strong>Shrinking what your internet provider can see.</strong> Without a VPN your provider can log every destination you contact; with one, it sees a single encrypted stream to the VPN server. Note the honest phrasing: the <em>observation</em> moves, it doesn't vanish — the VPN company now sits where the provider was, which is why the provider's own logging policy and jurisdiction matter more than its speed claims.</p>
<p><strong>Address swap.</strong> Sites see the VPN server's address instead of yours. That's how region switching works, and it also quietly removes one small tracking signal.</p>
<p><strong>Safer roads for work.</strong> The "corporate VPN" many people already use is the same technology: a private path into an office network. If your employer offers one for its systems, that's the tool doing a real job.</p>

<h2>What it does NOT do (the list the ads skip)</h2>
<p><strong>It doesn't make you anonymous.</strong> You log into accounts — mail, shopping, social — with your name attached. Sites know exactly who you are; they just see a different address. Anonymity would require changing behaviour, not just the tunnel.</p>
<p><strong>It doesn't stop ads or tracking.</strong> The tracking industry runs on cookies, browser fingerprinting and logins — none of which care what your IP address is. A VPN doesn't touch them; <a href="/tech/browser-privacy-settings/">browser privacy settings</a> address that layer far more directly.</p>
<p><strong>It doesn't scan for malware or phishing.</strong> Some products bundle blockers, but the tunnel itself happily carries you to a fake banking site at encrypted speed. The defence there remains <a href="/tech/how-to-spot-a-suspicious-link/">link scepticism</a>, not routing.</p>
<p><strong>It doesn't fix a compromised device.</strong> Malware running on your machine watches your screen and keyboard from inside the tunnel — encrypting the road outside the computer helps nothing once the passenger is compromised.</p>
<p><strong>It doesn't make anything legal.</strong> Local law still applies, to you and to the service; a tunnel is not a jurisdiction change.</p>

<h2>The free-VPN warning, stated once and plainly</h2>
<p>Running a VPN network costs real money in bandwidth. A free service has to earn that back somehow, and the currency available is you: injected ads, harvested data, sold traffic profiles. The same rule as everywhere else on this site — <a href="/tech/what-free-apps-do-with-your-data/">if you can't tell what the product is, the product is your data</a> — applies double to a service whose entire job is handling your traffic. If you use a VPN at all, use one whose business model you can explain in a sentence.</p>

<p><em>The honest summary: a VPN is worth having for public Wi-Fi, worth considering for provider-visibility reasons, and worth skipping the day you catch yourself calling it "anonymous browsing". It moves trust from one operator to another — so the decision worth making is whether you trust the operator, not whether the technology sounds powerful.</em></p>''',
        [],
        [
            ("public-wifi-risks", "Public Wi-Fi risks, honestly"),
            ("browser-privacy-settings", "Browser privacy settings"),
            ("what-free-apps-do-with-your-data", "What free apps do with your data"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 6. Browser privacy settings most people never touch
    # ------------------------------------------------------------------ #
    (
        "browser-privacy-settings",
        "safety",
        "guide",
        "Browser privacy settings most people never touch",
        "The tracking industry runs on defaults. One focused pass through your browser's settings — fifteen quiet minutes — removes most of the passive collection without breaking the web.",
        '''<p>Your browser is where the tracking economy actually lives — not in dramatic hacks, but in defaults: third-party cookies on, permissions granted and forgotten, sign-in sync quietly bundling your history with your account. None of this requires genius to fix, and none of it requires extensions either. One pass through the settings below takes about fifteen minutes. Menu names drift between browsers and versions on purpose, so these are organized by concept — every major browser has a settings page for each.</p>

<h2>Third-party cookies and tracking protection</h2>
<p>The big one. Third-party cookies are how a shop's ad follows you to a news site; blocking them is a single toggle in the privacy section. Set tracking protection to its <strong>strict</strong> level — the standard level deliberately leaves exemptions that advertisers pay for, and strict rarely breaks anything you can't fix by a single sign-in. Do not nuke all cookies wholesale: deleting first-party cookies signs you out of everything and achieves little, since the trackers you care about are the third-party ones. While you're there, decline the "pre-load pages for speed" nicety if your browser offers it — it visits links before you click them, which is exactly what it sounds like.</p>

<h2>Permissions, revoked like app permissions</h2>
<p>Browsers grant sites camera, microphone and location access the same way phones grant apps — and collect the same forgotten grants. The site-permissions page lists everything with access; revoke anything you can't explain, and set location and notifications to "ask" rather than remembering a yes from 2023. This is the browser chapter of the same discipline as <a href="/tech/android-app-permissions/">phone app permissions</a>: access you forgot about is access you're still giving.</p>

<h2>Sign-in sync: the trade nobody reads</h2>
<p>Being signed into the browser itself (for bookmarks, tabs, passwords) is genuinely convenient — and it hands your full browsing history to that company's account profile, tied to your name. Decide deliberately: either keep the convenience and review the activity controls on that account (the same dashboards as <a href="/tech/smart-speaker-privacy/">the smart-speaker privacy piece</a> — same companies, same controls), or use the browser signed out and accept manual bookmarks. What you shouldn't be is signed in without knowing it.</p>

<h2>Private windows, demystified</h2>
<p>Private mode clears local traces — history and cookies <em>on your machine</em> after the window closes. It does not hide activity from the sites you visit, your workplace network, or your provider; it's a shared-computer and gift-shopping tool, not anonymity. Expecting anonymity from it is the same category error as expecting it from <a href="/tech/vpn-what-it-protects/">a VPN</a> — different layer, same illusion.</p>

<h2>The rest of the pass, quickly</h2>
<p><strong>Search engine:</strong> switch to one that doesn't build an ad profile on queries — it's one dropdown and it changes what your search bar leaks daily. <strong>Autofill:</strong> browser-stored cards and addresses are convenient; know that they're there and protect the browser accordingly. <strong>Do Not Track:</strong> the toggle is honest but nearly toothless — it's a request most trackers ignore; enable it, don't rely on it. <strong>Extensions:</strong> every extension can read most of what you browse; keep the few you'd defend out loud, delete the rest — the logic is identical to <a href="/tech/what-free-apps-do-with-your-data/">what free apps do with your data</a>. <strong>Profiles:</strong> if work and life share a computer, separate browser profiles contain the cookies, history and sign-ins apart — cleaner than any cleanup ritual.</p>

<p><em>Do the pass today, then forget about it: cookie settings, strict protection, permissions revoked, sync decision made, search engine switched. The tracking economy assumes you'll never open that settings page; the entire advantage is that you did.</em></p>''',
        [],
        [
            ("vpn-what-it-protects", "What a VPN actually protects"),
            ("android-app-permissions", "Android app permissions, explained"),
            ("what-free-apps-do-with-your-data", "What free apps do with your data"),
        ],
    ),
]
