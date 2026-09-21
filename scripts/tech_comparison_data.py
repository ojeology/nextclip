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
]
