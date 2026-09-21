# -*- coding: utf-8 -*-
"""BRYME Tech desk — the comparison shelf, batch 2 (Phase 1 T10, 21 Sep 2026).

House rules these entries obey: no invented prices or specs; anything that can
change ships with a "check the official page" nudge; verdicts are frameworks,
not advertising; first-hand voice only where the desk has actually run the thing.
Tuple shape matches TECH_ARTICLES: (slug, title, blurb, body-html).
"""

TECH_COMPARE = [
 ("zoom-vs-google-meet-low-bandwidth",
  "Zoom vs Google Meet when your connection is bad: which one survives?",
  "Audio-only fallbacks, noise suppression, local recording and calendar gravity - the differences that matter when the uplink is holding on for its life.",
  """<p>Every video-call comparison is written by someone with fibre. This one is for the rest of us: the meeting that has to happen on a mobile hotspot, in a storm, with two bars. Both apps are good; they fail differently, and the failure modes are the whole buying decision.</p>
<h2>What each does when bandwidth drops</h2>
<p>Zoom's heritage is audio-first - it grew up dialling people in over telephone lines, and that instinct shows: it keeps a call alive on a lower-quality uplink by degrading video gradually and keeps screen-share legibility prioritised over face-cam. Meet, born inside Google Workspace, leans on the browser and on aggressive codecs; its newer plans sell software noise suppression as a headline feature, which is genuinely valuable when everyone is on laptop mics in Lagos traffic. For raw survival on a weak uplink, Zoom still has the edge the moment the network starts flapping; for a call where the noise, not the bandwidth, is the enemy, Meet's suppression is excellent - verify which plan you need on Google's own page, because these features move between tiers without warning.</p>
<h2>The fallbacks you will actually use</h2>
<ul><li><b>Dial-in audio.</b> Both offer PSTN numbers. When video dies, "I'll ring in" saves the meeting; check the current call-rate page for the number you will actually dial - rates change.</li>
<li><b>Local recording.</b> Zoom records to your machine by default, which means no upload time and a file you control. Meet records to the cloud, which means it keeps working when your disk is full but needs Workspace entitlements most personal accounts don't have.</li>
<li><b>No-install guests.</b> Meet opens in a browser tab politely; Zoom's web client works but pushes the app. If your participants are clients' assistants and in-law phones, that friction is a feature decision.</li>
<li><b>Calendar gravity.</b> If your org lives on Google Calendar, Meet links are one click and the room hardware understands them. Zoom wins when meetings are cross-org and ad-hoc.</li></ul>
<h2>The verdict, as a rule</h2>
<p>If the meeting is <em>yours</em> and the network is the variable: Zoom, video off by default, record locally, dial-in numbers in the invite. If the meeting is <em>inside Google Workspace</em> and the problem is a noisy room: Meet, noise suppression on, record to the cloud, never fight your admin about it. Whatever you choose, hold one habit above all features - send the agenda as a text message too, because the message that survives a dead call is the one that isn't in the call.</p>
<h2>Check before you commit</h2>
<p>Tier names, minute limits and which plan holds which suppression feature have changed more than once across both services in recent years. Both companies publish current limits plainly: Zoom's plans page and Google's Workspace editions page. Read those, not this page, before paying.</p>"""),

 ("canva-vs-adobe-express",
  "Canva vs Adobe Express: which one should actually be your design tool?",
  "Template depth, background removal lineage, brand kits and the one accounting question that decides it: are you already paying for Creative Cloud?",
  """<p>Canva is the default answer to "can you design something quick"; Adobe Express is Photoshop's company trying to make quick respectable. They want the same three minutes of your day, and the honest differences live in what happens after those three minutes.</p>
<h2>Where each one is genuinely stronger</h2>
<ul><li><b>Starting points.</b> Canva's template library is larger by a wide margin and organised like a search engine - type "fundraiser poster, Nigeria" and you get usable, non-boring results. Express's library is smaller and skews corporate-clean; if you want a style to borrow, Canva finds it faster.</li>
<li><b>Cut-outs and photo work.</b> Express inherits Adobe's object selection - subject isolation on a busy background is the one task where its AI feels like a Photoshop-grade hand, not a magic-wand demo. Canva's background remover is fine for portraits and unreliable for hair, fur and transparent edges.</li>
<li><b>Brand consistency.</b> Canva's brand kit locks fonts, palettes and logos across a team with per-user controls that just work. Express does the same via Creative Cloud libraries, which are more powerful - if someone has already built the library; if not, the setup tax is real.</li>
<li><b>Video and motion.</b> Express has the video-editor DNA (it shares a lineage with Premiere's templates); Canva's animation is presentation-cute, not edit-tight. Short clips with captions and clean typography: Express. Slideshow-with-music for a WhatsApp broadcast: Canva.</li>
<li><b>Free-plan reality.</b> Both free tiers are usable and both gate their best assets behind paid rows, in slightly different places each year. Check the current free-vs-paid pages before deciding - the honest summary is: free Canva gets you further on design volume, free Express on one good cut-out.</li></ul>
<h2>The accounting question</h2>
<p>If you already pay for Creative Cloud - for Photoshop, for Lightroom, for a student deal - Express is in the box. Its "free" cost is a lie and a true one: you own it, and Adobe's ecosystem (fonts via Typekit, stock via the stock tiers) clicks together. If you don't, Canva's single subscription usually buys more practical capability per naira - templates, brand kit, presentation, social scheduler - as one product.</p>
<h2>The verdict, as a rule</h2>
<p>Volume design work for a small team with one competent volunteer: Canva, no argument. Photo-first social clips, cut-outs, and anyone with a Creative Cloud subscription: Express. If you find yourself fighting Express's editor on a deck, or Canva's cut-out on a hair edge, that fight <em>is</em> the answer.</p>"""),

 ("showmax-vs-netflix-nigeria",
  "Showmax vs Netflix in Nigeria: what is each actually for?",
  "Local-first library versus global volume, the sports tier question, download discipline on metered data - the honest split for streaming from here.",
  """<p>This is not a quality comparison; Netflix and Showmax both stream beautifully when your bandwidth allows it. It is a question of which habit you want funded. Pick by what you'll watch, not what the library size says.</p>
<h2>The library identities</h2>
<p>Showmax built itself on proximity: Nollywood and African originals at real budgets, South African and Nigerian soaps with current episodes (the soaps are the retention engine - people do not cancel mid-story), plus the live-sports tiers that carry Premier League football. Netflix built itself on volume and depth: a global catalogue, kids' programming that is its own argument, and a growing - still small relative to the whole - slate of Nigerian originals that increasingly arrive with international co-production money behind them.</p>
<h2>The mechanics that matter from here</h2>
<ul><li><b>Sports.</b> If you want league football included, Showmax's sports-bearing tiers are the only streaming-in-Nigeria answer that consistently carries it; verify the current tier and add-on on Showmax's own plan page - sports rights move every season, and a subscription bought on an old page is a cancelled subscription within three months.</li>
<li><b>Downloads and data.</b> Both apps save to phone; both throttle on metered connections. On capped mobile data, download caps per tier matter more than bitrate - check which plan limits simultaneous devices and download counts before you commit a month's allowance to one.</li>
<li><b>Kids and household profiles.</b> Netflix's per-profile controls and junior catalogue are still the industry reference. Showmax profiles are functional; its kids tier is narrower.</li>
<li><b>Subtitling.</b> Showmax's local-language subtitle culture has improved steadily; Netflix's subtitle quality is uniform and searchable by language. If subtitles are non-negotiable for a household, test both free weekends with your own content rather than trusting anyone's claim - including this page's.</li></ul>
<h2>The verdict, as a rule</h2>
<p>Football plus Naija-soap habit: Showmax, bought at the right tier. Volume, variety and a household that argues about what to watch: Netflix. And the honest financial line, the one no review gives you: whichever you buy, rotate with the seasons - both services make leaving easy by design, and the catalogue that justified the sub in January will not be the one in July. Read the current pricing and tier pages for your region at signup; this page deliberately prints no numbers because numbers like these go stale faster than this desk re-verifies them.</p>"""),

 ("jumia-vs-konga-electronics",
  "Buying electronics on Jumia vs Konga: which marketplace protects you better?",
  "Seller ratings, protection programmes, warranty routing and the four habits that matter more than which logo is on the checkout page.",
  """<p>Nigerian electronics e-commerce has been won by process, not platform. Both Jumia and Konga sell genuine, excellent products next to mediocre ones, because most listings come from third-party sellers. The buying skill that actually protects you transfers between them - so this comparison is half platform, half procedure.</p>
<h2>How the platforms differ</h2>
<ul><li><b>Official brand stores.</b> Jumia's mall-style official stores (brand-operated or authorised-distributor listings) are the closest thing online to a warranty-backed shop counter. Konga's own stock - the era that made its name - is smaller now; when a high-value item is "sold by Konga" and in their warehouse, its handling of returns and inspection is often calmer than a third-party storefront.</li>
<li><b>Buyer protection.</b> Both publish protection programmes with money-back conditions; the devil is in the current wording (what "not as described" covers, who pays return shipping, inspection timelines). Read the live policy at checkout, not an old screenshot - these documents get quietly tightened.</li>
<li><b>Logistics honesty.</b> Delivery windows for Lagos-mainland are similar; the differences appear in second-city fulfilment and at pickup stations. Whichever platform has a station you can reach in one ride is the one that can absorb a failed delivery without drama - for you.</li>
<li><b>Warranty routing.</b> Local warranty lives in the distributor sticker in the box, not the marketplace receipt. A listing that names the authorised distributor is worth more than any platform badge; a listing that doesn't is worth exactly what an unboxed phone is worth at a repair counter.</li></ul>
<h2>The four habits</h2>
<p>One: sort to seller rating and years on platform, then open the store's own review pages - a 100-item electronics store with 4.2 stars is a safer room than a fresh one with five perfect reviews. Two: prefer "official store" or warehouse-stock listings for anything above a mid-range phone price. Three: film the unboxing, every time, in one take including the shipping label - the protection programmes all reference evidence and mean it. Four: test before the return window closes, with the box: pixels, battery, IMEI check, speaker grille - you are inspecting, not reviewing, and the clock is the clock.</p>
<h2>The verdict</h2>
<p>For laptops, phones and screens sold with local warranty: Jumia's official stores first, seller-graded listings second, never the cheapest new-store listing. For second-life, refurbished and warehouse-stock deals: watch Konga's own inventory and read the condition grade like a contract. If either platform's current protection page contradicts this paragraph, the platform page wins - that is the point of the habit.</p>"""),

 ("iphone-vs-android-nigeria",
  "iPhone vs Android in Nigeria: the decision is repair economics, not brand",
  "Screen-part availability, resale curves, banking-app reality and the file-transfer habits that decide which phone is cheaper over four years.",
  """<p>Almost every iPhone-vs-Android argument is a lifestyle argument pretending to be an economics one. In Nigeria specifically, the economics are unusual and decisive: what happens to this phone when it breaks in month thirty, and what it sells for in month forty-eight.</p>
<h2>Repair reality</h2>
<p>Android supports a vast grey-market repair economy - screens, batteries, charging ports for popular mid-range models are stocked everywhere from Alaba to Wuse at prices that don't feel like a new-phone purchase. iPhones repair well too, but parts are serialised and pairing matters: an "aftermarket screen" trade on an iPhone comes with a settings-menu warning and a degraded True-Tone/ Face-ID story depending on the board swap. Translation: on most Android mid-rangers, a repair shop conversation is about price; on iPhones it is about authenticity, and the premium is structural.</p>
<h2>Resale as a refund</h2>
<p>iPhone resale value holds - the second-hand market trusts the battery-health readout as a spec sheet, and two-generation-old iPhones remain sellable at percentages Android rarely matches. If you buy expensive and sell once, the iPhone's curve pays part of the premium back. If you buy mid-range and never sell, the Android's lower entry price is the better deal and the resale talk is decoration.</p>
<h2>The daily-work differences that matter here</h2>
<ul><li><b>File freedom.</b> Android behaves like a USB drive - moving video projects, a card from a camera, sharing folders with a print shop. iOS is a walled garden that works perfectly if your whole workflow lives in cloud apps; it is friction the moment it doesn't.</li>
<li><b>Banking and SIM life.</b> Both ecosystems carry every Nigerian bank app, authenticator and mobile-money tool; USSD works identically. The one practical note: eSIM-first iPhones abroad can mean a paperwork visit for a local SIM swap - keep your old plan's SIM details wherever you buy.</li>
<li><b>Charging infrastructure.</b> Lightning-era spare cables are still everywhere and USB-C iPhones share the world's most common cable; Android's advantage here has quietly evaporated - the cable in any Lagos drawer fits both now.</li></ul>
<h2>The verdict, as a rule</h2>
<p>You keep phones four years and sell things when you move apartments: iPhone - the repair premium is amortised by the resale refund. You want capability per naira, file freedom, or a second device that just works for work: a solid Android mid-ranger with a wide local parts footprint (before buying any model, search "[model] screen price" with a local marketplace open - that number is the review everyone skips). Whatever the badge: buy the case and the tempered glass, because the second-most expensive moment in phone ownership is the first fall.</p>"""),

 ("ubuntu-vs-debian-home-server",
  "Ubuntu vs Debian for the home server: the family feud, settled by hardware",
  "Same lineage, opposite temperaments: release cadence, the Snap question, hardware enablement, and which one lets you forget it exists.",
  """<p>This is a family argument: Ubuntu is built on Debian, and every choice Ubuntu makes is a choice Debian declined. For a home server, "which is better" is the wrong question; the right one is "which will I still be able to fix at 11 p.m. on the Sunday I actually attempt maintenance."</p>
<h2>Where Ubuntu earns its opinionated choices</h2>
<ul><li><b>Hardware freshness.</b> Newer NICs, Wi-Fi cards and CPU microcode arrive in Ubuntu's HWE kernels without surgery. Debian stable ships what it has tested for age - rock-solid and occasionally too old to drive last year's laptop. Buy a mini-PC with recent silicon: Ubuntu makes the first hour friendly.</li>
<li><b>Documentation gravity.</b> Every home-server tutorial on the internet is written against Ubuntu or its derivatives. When you search an error at 11 p.m., the answer is written for this box. That's a real feature; don't let anyone tell you otherwise.</li>
<li><b>The managed bits.</b> Landscape, unattended-upgrades configured by default, and a free personal Ubuntu Pro token (home-lab tier - verify the current machine allowance on Canonical's own page) that patches universe packages too.</li></ul>
<h2>Where Debian is the better answer</h2>
<ul><li><b>No Snap tax.</b> Ubuntu's Snap-first habits - notably the loopback interface it creates for Docker's benefit - will bite you the day a DNS container refuses to bind port 53, because systemd-resolved already lives there. Debian's plain apt has none of these surprises; what you install is what is running.</li>
<li><b>Stability as personality.</b> Debian stable's release cadence is "when it's ready," and its upgrade path is the smoothest in Linux because everything moves at once, rarely. If your server hosts a family archive and a media shelf, boring is correct.</li>
<li><b>Resource humility.</b> A Debian netinst with the few packages you choose genuinely idles smaller, boots on older RAM, and stays that way - no first-boot package flood.</li></ul>
<h2>The verdict, as a rule</h2>
<p>New hardware, want Docker/Kubernetes/play-it-from-tutorials life: Ubuntu Server LTS, and disable what you don't use the day it annoys you. Old hardware, static services, "install and forget": Debian netinst. If you'd rather learn one system forever than argue, learn Debian proper - Ubuntu is Debian with a personality, and the personality is a subscription to its choices. Whatever you pick: name the machine, snapshot before upgrades (Timeshift or plain LVM state), and test your restore while the thing you're protecting still exists.</p>"""),

 ("chrome-vs-edge-old-laptop",
  "Chrome vs Edge on an old laptop: which one actually breathes easier?",
  "Same engine, different manners - memory discipline, battery drain, phone handoff and the one Edge setting Chrome has never copied for slower machines.",
  """<p>Both browsers are built on the same Chromium engine, so the honest question is not which is faster - it is which wastes less of the two things an old laptop has: RAM and battery. The answers are settings, not badges, and one of them genuinely ships off by default in Edge's favour.</p>
<h2>Where Edge quietly wins for older hardware</h2>
<p>Edge has a built-in sleeping-tabs system that suspends background tabs after minutes of no use and hands their memory back - and a "efficiency mode" that does the same for the whole browser while a laptop runs on battery. Chrome added tab freezing later and still keeps every open tab's extensions awake; on a four-gigabyte machine the difference is real and measurable in fan noise. The second Edge advantage is Windows-level integration: the best performance gains on an old laptop come from what the browser lets the OS do, not how fast its JS engine benchmarks.</p>
<h2>Where Chrome still earns its weight</h2>
<ul><li><b>Extension survival.</b> Every extension you rely on exists for Chrome first; Edge's store is growing but thin at the long tail. An ad-blocker is the single biggest speed upgrade any old laptop can buy, so whichever browser runs <em>your</em> blocker wins.</li>
<li><b>Sync and password continuity.</b> If your phone is Android, Chrome keeps the password vault honest. Edge does the same for Microsoft accounts - pick the browser that matches the account you already trust with your passwords, because switching vaults is the actual migration cost.</li>
<li><b>Memory hog reputation, fairly:</b> Chrome's number-one drain is not the tabs, it's the tabs that keep extensions, casting and full-res video alive. Close what you are not reading and the gap narrows; the same is true of Edge.</li></ul>
<h2>The old-laptop checklist that beats either choice</h2>
<p>Whatever logo you keep: cap open tabs at ten, put the streaming site in its own window so its DRM machinery runs alone, check the task manager's memory sort once to find which extension is the leak (it is always one), and run the browser while the laptop is plugged in when possible - batteries past three years throttle hard on charge, and no browser choice fixes physics. For a genuinely tired four-gigabyte Windows machine, the best-performing free software is a lighter operating-system install, not a lighter browser - say so, as this desk does about everything.</p>
<h2>The verdict</h2>
<p>Old laptop, Windows, no extension dependencies: Edge with efficiency mode switched on, and stop pretending it is a compromise. Android-phone household with must-have Chrome-only extensions: stay on Chrome and manage it like fuel - tabs are the consumption. Both free in every sense: try both for a week with the task manager open, and let the memory graph, not this page, decide.</p>"""),

 ("wifi-extender-vs-second-router-nigerian-house",
  "Wi-Fi extender vs a second router vs a cable to the ceiling: fixing a Nigerian two-storey signal dead spot",
  "Why extenders usually halve what they extend, when a cheap second router beats them, and the two-storey truth about cables in the ceiling.",
  """<p>The Nigerian double-storey house has a physics problem the marketing solves badly: the ground floor router broadcasts through a concrete slab with steel mesh inside, and concrete-and-steel is the champion of Wi-Fi assassination. The box of hope sitting on the shelf - the plug-in extender - usually makes it worse before dinner. Here is why, and the order of fixes that works.</p>
<h2>Why the extender disappoints</h2>
<p>A single-band extender receives the signal and re-sends it on the same radio - it talks twice so it goes half as far, and everything behind it shares one breath. Dual-band extenders do better (receive on one band, rebroadcast on the other), but they still sit in the dead zone <em>receiving</em> the very signal that is already struggling. The honest rule: extenders amplify a bad situation; they do not fix it, and each one added to the house is another neighbour's channel to fight over at night.</p>
<h2>The three real fixes, in cost order</h2>
<ul><li><b>The second-router-as-access-point trick.</b> Any cheap router with an Ethernet port can be an access point: run one cable - even an ugly external one clipped along the wall - from the main router to the second floor, plug it into the second router's LAN port, turn <em>off</em> that router's DHCP, and give it the same network name and password on a different channel. Now devices roam to whichever is louder. This is the same job a mesh kit does for many times the money.</li>
<li><b>Powerline adapters, with an if.</b> In houses on stable wiring - one meter, clean connections - powerline carries the network through the electrical copper to another room's socket. The if: Nigerian homes often have separate circuits, old joints and stabiliser-heavy wiring; a good kit on one ring beats a bad one across two meters. Buy from a shop that lets you test on your own circuit before the week is out.</li>
<li><b>The ceiling-cable endgame.</b> One Cat6 run in the ceiling - through the roof space if you have one, clipped externally if you don't, with proper conduit where the sun hits - turns every future fix into plug-and-play. It is the one installation a competent electrician can do on the same visit as the wiring repairs, which is how the labour cost stays civilised.</li></ul>
<h2>What to do tonight, free</h2>
<p>Move the router: central, high - top of a wardrobe, not behind the TV where the metal panel eats it - and change the control-channel to the one your phone's Wi-Fi scanner shows as empty, because on a street of thirty networks, the least-crowded channel is worth more than any box. Then decide from the signal you actually measure - a phone's Wi-Fi reading at the dead spot is the instrument this whole page rests on, and it is in your pocket.</p>"""),

 ("dell-vs-hp-refurbished-laptops-nigeria",
  "Dell vs HP refurbished laptops: which brand survives Nigerian second-hand life better?",
  "Parts supply, keyboard ratings, the battery grading honesty test, and the two model families that keep this desk buying one brand with eyes open.",
  """<p>In the second-hand market, the brand badge on the lid is actually a supply chain: which spare parts will still exist in three years, and whether any technician in the city can fit them with tools from one drawer. Dell and HP both pass that test; the differences are in the habits their business lines left behind.</p>
<h2>The parts story</h2>
<p>Both brands flooded Nigerian offices with the same class of machine - corporate fleets renewed every three years - so the streets are carpeted with their parts: screens, hinges, keyboards, chargers. Dell's Latitude/Precision families share charger barrels and BIOS habits so deeply that a repair often becomes swap-and-go; HP's EliteBook/ProBook lines lean on ubiquitous USB-C charging now, which future-proofs the purchase. Either brand, the one question that predicts your next five years: "do they stock the keyboard for this model here?" If the answer at your shop is "we can import it, two weeks," a keyboard death becomes a funeral.</p>
<h2>Where each tends to land</h2>
<ul><li><b>Dell (Latitude/Precision):</b> thick, hinge-heavy business builds that survive the "carried everywhere in a backpack" life; BIOS menus that a technician can reset with nothing but a screwdriver; docking legacy that turns a used laptop into a desktop on a second-hand stand.</li>
<li><b>HP (EliteBook/ProBook):</b> often the nicer keyboard and the better screen for the same money; the EliteBook aluminium shells resist flex; and the one practical edge that matters - their recent mid-range all keep memory in ordinary slots rather than soldered, which is how a four-gigabyte find becomes sixteen gigabytes cheaply. Check the exact generation: HP has soldered more, and "usually" buys nothing.</li></ul>
<h2>The grading honesty test (works on any brand)</h2>
<p>Grade-A / Grade-B listings are a shop's vocabulary, not a standard - so ignore the word and run the five-minute interrogation on the actual machine: charge port - does the socket wiggle? Battery - health report from the OS, not the shop's promise; hinges - open and close it ten times, slowly; screen - full white and full black pages at max brightness for backlight bleed and dead pixels; screws - stripped heads mean a second repair, which means a first repair the shop will not warranty.</p>
<h2>The verdict, as a rule</h2>
<p>Whichever brand your specific shop can actually service is the right brand: the used-laptop market is local by nature, and a warranty you can walk to beats any model preference. Between two same-shop machines of equal grade and price: the one with the upgradeable RAM and the USB-C charge - that is where used-life economics live. And refuse any laptop whose battery "report" is a shopkeeper's memory: the operating system prints the number, and the number is the whole battery section of this article.</p>"""),

 ("kindle-vs-kobo-vs-tablet-reading",
  "Kindle vs Kobo vs your tablet for reading: the decision is the store, not the screen",
  "E-paper versus a glass screen at night, the library-loan card neither advertises, and the format wars settled by the one file type both e-readers eat.",
  """<p>Every specs comparison of e-readers misses the decision. The real question is where your books come from, because each device is a shop window with a screen attached - and if you buy the wrong window, the glass is still lovely while your library sits in the other ecosystem's file format.</p>
<h2>The screen, since it must be covered</h2>
<p>E-paper is not technology you watch, it is technology you ignore: ambient light on ink, no blue at bedtime, and a battery counted in weeks precisely because the page does not refresh itself like a video. A tablet does the same job on a good evening with dark mode - and makes the sleep you needed worse. If reading is how you fall asleep, the e-ink device is the only honest answer; the tablet is a reading lamp with a notification habit.</p>
<h2>The libraries nobody puts on the box</h2>
<ul><li><b>Kobo's quiet superpower:</b> it accepts the free library-loan format the public libraries built their lending systems around, so a Kobo and a library card can be the whole subscription - and in a country where most library delivery is not part of the deal, its openness to any file you can move from a folder still matters: it reads the standard unprotected book file; the shops' DRM formats are the ones it will not.</li>
<li><b>Kindle's gravity:</b> the store is the world's largest used-and-cheapest book machine; Whispersync moves your place between phone and reader, and the ecosystem's sale culture is genuinely the cheapest way to build a library in English. Its walls are walls - the proprietary file type is why sideloading guides exist - but they are walls around the biggest yard.</li>
<li><b>Tablet plus apps:</b> free library apps, PDFs that e-ink butchers (the real answer for a student with lecture packets is a ten-inch tablet and a stylus), audio-book support without a phone by the ear - the "one device for everything" argument is honest for exactly these jobs.</li></ul>
<h2>What the spec sheets get wrong</h2>
<p>Brightness: both e-readers light the page sideways so the screen surface stays matte - the numbers in their ads are marketing, not sunlight; test at dusk with the light off, which is when it matters. Storage: a thousand books fit in less than a phone's photo app wastes. Waterproofing: real now on the premium tier - if you read in a bath or a rainy compound veranda, it is worth money; if you read in bed, it is not.</p>
<h2>The verdict, as a rule</h2>
<p>Buying books in English, one store for life: Kindle, accept the walls, enjoy the yard. Owning your files and wanting zero subscription: Kobo. A student, a PDF reader, a commuter with three apps: keep the tablet, buy the reading light separately and sleep better on purpose. No one in the history of this desk has regretted the e-ink purchase; the regret is always the ecosystem, so choose the shop, not the screen.</p>"""),

 ("streaming-stick-vs-android-box",
  "Streaming stick vs Android TV box for a dumb TV: what each box cannot do for you",
  "The one app your stick will never install, the update cliff every box seller hides, and the honest cast-versus-native verdict for a Nigerian living room.",
  """<p>Both fix the same problem - a television with no apps - from opposite philosophies: the stick is a remote with ambition, the box is a phone you point at a wall. The differences decide in about eighteen months of ownership, not in the shop.</p>
<h2>The stick's case</h2>
<p>Interface polish and app certainty. A Chromecast-class stick brings a curated front page, an update stream that lasts years from a manufacturer with a platform to feed, and one trick the box never reproduces cleanly: casting - the phone is the remote <em>and</em> the content buffer, which on a shaky home connection outperforms the box downloading alone. It is smaller, uses the TV's own USB port for power (watch the port's amperage - some TVs sag; the supplied wall plug exists for a reason), and it survives the landlord change because it moves in a pocket.</p>
<h2>The box's case</h2>
<p>Freedom and the answer to "what about the app that isn't on the store" - when a service exists as an APK, the box is the TV that runs it: regional sports apps, local IPTV interfaces used <em>legitimately</em> (this desk will not walk you toward pirated anything - a subscription that costs less than a bottle of Fanta per month is not a deal, it's an eviction notice with a logo), sideloaded file players that eat every codec in a shared folder, and full keyboard-and-gamepad support. RAM and storage are real, and matter if you want the box to be more than a streamer.</p>
<h2>The two things sellers bury</h2>
<ul><li><b>The update cliff.</b> A no-name Android box gets its Android version and its security patches once, from a factory, on the day it ships. Two years later the bank app refuses the OS level and the store app stops updating. Branded TV boxes (the name-brand Android TV lines) are the middle ground - real update promises - which is precisely why they cost more than the grey import.</li>
<li><b>The interface tax.</b> Phone apps on a TV need a Leanback interface or you live in a remote-control maze; the stick's whole job is that interface, so the "limited app list" that reads like a weakness on the spec sheet is the product.</li></ul>
<h2>The verdict, as a rule</h2>
<p>One streaming habit, living room, family remote: a name-brand stick - the polish is the purchase. Tinkerer, sports-bundle collector, or the app you actually watch lives outside the store: a branded Android TV box with real update commitments, and if the grey import tempts you, budget for it to become a media player in two years and the price math changes. Either way, the HDMI port and the TV's own volume control will do the rest; the dumb TV, as always, is the second-best thing in the room after you fixed it.</p>"""),

 ("student-laptop-spec-floor-2026",
  "The honest spec floor for a student laptop in 2026: five numbers, no prices",
  "The minimum configuration that will still work in year three of a degree - and the two spec traps that make a cheap laptop expensive by second semester.",
  """<p>A student laptop is bought once and judged for four years, so the only sensible purchase question is: which numbers make it survive year three? This desk will not quote prices - they move - but the floor below which any laptop becomes coursework with a lid is stable and small enough to memorise.</p>
<h2>The five numbers</h2>
<ul><li><b>16 GB of RAM, or 8 that is upgradeable.</b> Browser tabs are the student's real workload, and each one is a small office. Four gigabytes is a 2020 laptop; eight is the 2026 minimum with a hard floor, sixteen is the one that stops you managing tabs for the last time.</li>
<li><b>A real SSD, any size you can grow.</b> Hard-disk laptops are still sold as "new" behind some counters; they are slow, they die from backpack life, and they teach you to hate computers. If the machine says HDD, walk - the secondhand SSD swap later is cheap; the lost project is not.</li>
<li><b>A screen you can read at 100 percent zoom.</b> 1920x1080 on 14 inches, matte, and - the trap - not the 1366x768 panels still shipping as "HD." Zoom once in the shop and look at the letter edges; your eyes are the lab.</li>
<li><b>Modern-ish CPU: any current four-core, generation not older than about three years.</b> For lecture-hall work, the processor is almost never the bottleneck - <em>except</em> in the one spec trap below.</li>
<li><b>Weight under 1.6 kg with the charger, measured in the shop, not the listing.</b> A lecture hall is a five-minute walk; a campus is a twenty-minute one, every day, for four years, and a 2.4 kg machine is a decision you make again each morning by not making it.</li></ul>
<h2>The two traps</h2>
<p>One: the Pentium/Celeron/"4-core feel" chips that carry modern RAM and SSD while being the bottleneck the whole specification exists to remove - the processor is where a "great value" laptop hides its crime. Two: soldered-everything thin-and-lights - the ultrabook shape at the student budget means no RAM path up, no battery swap without glue, and one deep scar from the repair shop that follows the machine like a debt. Both traps are visible in five minutes: open the back panel image, or ask the seller which slots are empty.</p>
<h2>The floor, as a card</h2>
<p>Sixteen gigabytes or a free slot. Solid-state storage. Full-HD matte screen. A four-core CPU no one has to hype. Under 1.6 kilos. Warranty you can <em>walk to</em> - in the second-hand market a shop's reputation is the manufacturer's warranty, so buy the dealer as much as the laptop. Every spec argument after those five is preference; a seller who argues they are "nice to have" is telling you which side of the till they are on. For engineering students running genuinely heavy software - check the department's published requirement before you buy anything, because that page, not this one, is your real floor.</p>"""),
]
