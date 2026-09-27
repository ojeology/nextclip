# -*- coding: utf-8 -*-
"""External source notes, part 5: tech desk (77) + sports desk (7).
Every URL curl-verified 200 at authoring time; jumia.com.ng blocked the check
(403) and is therefore not cited."""

IETF = "https://www.ietf.org/"
W3C = "https://www.w3.org/"
MDN = "https://developer.mozilla.org/en-US/docs/Learn"
MDNHTTP = "https://developer.mozilla.org/en-US/docs/Web/HTTP"
KERNEL = "https://www.kernel.org/"
NIST = "https://www.nist.gov/"
CISA = "https://www.cisa.gov/"
NCSC = "https://www.ncsc.gov.uk/"
EFF = "https://www.eff.org/"
HIBP = "https://haveibeenpwned.com/"
FTC = "https://www.ftc.gov/"
USB = "https://www.usb.org/"
HDMI = "https://www.hdmi.org/"
BT = "https://www.bluetooth.com/specifications/specs/"
WIFI = "https://www.wi-fi.org/discover-wi-fi/security"
LETSENCRYPT = "https://letsencrypt.org/"
OPENSOURCE = "https://opensource.org/"
SITEMAPS = "https://www.sitemaps.org/"
INDEXNOW = "https://www.indexnow.org/"
UBUNTU = "https://ubuntu.com/"
DEBIAN = "https://www.debian.org/"
RENDER = "https://render.com/"
KONGA = "https://www.konga.com/"
GANDROID = "https://support.google.com/android/"
ANDDEV = "https://developer.android.com/"
MSWIN = "https://learn.microsoft.com/en-us/windows/"
IANA = "https://www.iana.org/assignments/media-types/media-types.xhtml"
NCC = "https://www.ncc.gov.ng/"
INVESTOR = "https://www.investor.gov/"
LALIGA = "https://www.laliga.com/"
LIGUE1 = "https://www.ligue1.com/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

EXTERNAL_SOURCES5 = {

# ============================== TECH (77) ====================================

"tech/4k-on-a-small-tv-when-its-invisible":
    "<p><b>The limit is angular resolution.</b> Whether extra pixels are visible depends on screen size and viewing distance, and the <a href=\"" + _w("display+resolution") + "\" rel=\"noopener\">display-resolution reference material on Wikipedia</a> sets out the arithmetic. The desk's conclusion follows from it rather than from reviews: at typical distances, small panels stop benefiting long before large ones do.</p>",

"tech/ai-privacy-what-not-to-paste":
    "<p><b>What these systems do with input, documented.</b> Training and retention behaviour is described in the <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large-language-model reference material on Wikipedia</a>, and the <a href=\"" + EFF + "\" rel=\"noopener\">Electronic Frontier Foundation</a> publishes the privacy guidance behind the desk's do-not-paste list. The rule is simple enough to survive a busy day: if it would be a problem in a screenshot, it does not go in the box.</p>",

"tech/android-app-permissions":
    "<p><b>The permission model is published.</b> What each Android permission grants is documented in the official <a href=\"" + ANDDEV + "\" rel=\"noopener\">Android developer documentation</a>, and the <a href=\"" + GANDROID + "\" rel=\"noopener\">Android help centre</a> describes the user-facing controls. The desk's ten-minute audit follows the model rather than the marketing: location, microphone, camera and contacts first.</p>",

"tech/android-battery-health":
    "<p><b>Chemistry, not settings, decides lifespan.</b> Lithium-ion cells degrade with charge cycles, temperature and time at full charge, and the <a href=\"" + _w("battery+life") + "\" rel=\"noopener\">battery-life reference material on Wikipedia</a> explains the mechanisms. The <a href=\"" + GANDROID + "\" rel=\"noopener\">official Android guidance</a> covers the software side; the desk's advice separates what settings can change from what they cannot.</p>",

"tech/audio-video-sync-drift-fix-order":
    "<p><b>Sync drift has a small set of causes.</b> Buffering, processing latency and wireless delay are the usual three, and the <a href=\"" + _w("audio-to-video+synchronization") + "\" rel=\"noopener\">audio-to-video synchronisation reference material on Wikipedia</a> describes the tolerances involved. The desk's fix order runs from the cheapest cause to the most expensive, which is the opposite of how people usually troubleshoot it.</p>",

"tech/bluetooth-wont-pair-reset":
    "<p><b>Pairing is a defined handshake.</b> The procedures and profiles are published by the <a href=\"" + BT + "\" rel=\"noopener\">Bluetooth Special Interest Group</a>, which is why clearing a stale pairing record usually fixes what restarting does not. The desk's order follows the protocol: forget, restart, re-pair, then suspect the hardware.</p>",

"tech/browser-problems":
    "<p><b>The web has public specifications, which is why browsers are debuggable.</b> The <a href=\"" + MDN + "\" rel=\"noopener\">MDN documentation</a> describes the platform a browser implements, and the <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> publishes the browser hygiene guidance the desk's checklist follows — updates, extensions, and the cost of each one you install.</p>",

"tech/build-vs-buy-the-honest-decision":
    "<p><b>Total cost, not licence price.</b> The comparison that matters includes maintenance and the cost of the team's attention, and the <a href=\"" + _w("total+cost+of+ownership") + "\" rel=\"noopener\">total-cost-of-ownership reference material on Wikipedia</a> sets out the method. The desk's rule of thumb comes from that arithmetic: buy the boring parts, build the part that is actually your business.</p>",

"tech/buying":
    "<p><b>Buying advice, with its standards named.</b> Specifications quoted on this shelf trace to the bodies that define them — <a href=\"" + USB + "\" rel=\"noopener\">USB-IF</a>, <a href=\"" + HDMI + "\" rel=\"noopener\">the HDMI Forum</a>, <a href=\"" + WIFI + "\" rel=\"noopener\">the Wi-Fi Alliance</a> — rather than to product marketing. Where a vendor's figure and the standard disagree, the desk prints the standard.</p>",

"tech/canva-vs-adobe-express":
    "<p><b>Compare on the file you end up with.</b> Design tools differ most in export fidelity and template lock-in, and the <a href=\"" + _w("graphic+design+software") + "\" rel=\"noopener\">graphic-design-software reference material on Wikipedia</a> covers the categories. The desk's test is the practical one: can you finish the job without a subscription you did not plan to keep?</p>",

"tech/cloud-bill-why-it-spikes":
    "<p><b>Bills spike for a few predictable reasons.</b> Orphaned resources, egress charges and autoscaling are the usual three, and the <a href=\"" + _w("cloud+computing") + "\" rel=\"noopener\">cloud-computing reference material on Wikipedia</a> describes the billing models behind them. The desk's audit order follows cost visibility: look at the largest line first, not the newest one.</p>",

"tech/data-snooping-when-you-test-too-many-ideas":
    "<p><b>A documented statistical trap.</b> Testing many hypotheses inflates false positives, and the <a href=\"" + _w("data+dredging") + "\" rel=\"noopener\">data-dredging reference material on Wikipedia</a> explains the mechanism and the corrections available. The desk applies it to backtesting because the failure mode is identical: the more strategies you try, the more winners you invent.</p>",

"tech/earbuds-buying-checklist":
    "<p><b>Codec and fit decide the outcome.</b> The wireless audio profiles are published by the <a href=\"" + BT + "\" rel=\"noopener\">Bluetooth SIG</a>, which is why two earbuds with identical drivers can sound different on the same phone. The desk's checklist starts there and ends with fit, because neither is fixable after purchase.</p>",

"tech/free-trial-cancellation-traps":
    "<p><b>The mechanics are regulated, not accidental.</b> Automatic-renewal and negative-option practices are the subject of <a href=\"" + FTC + "\" rel=\"noopener\">Federal Trade Commission</a> rules, including the requirement that cancelling be as easy as subscribing. The desk's three mechanics are those rules inverted — and the page names your jurisdiction's equivalent as the place to complain.</p>",

"tech/hdr-formats-the-weakest-link":
    "<p><b>Formats have published specifications.</b> <a href=\"" + HDMI + "\" rel=\"noopener\">The HDMI Forum</a> documents the video transport behind HDR delivery, and the <a href=\"" + _w("high-dynamic-range+video") + "\" rel=\"noopener\">HDR-video reference material on Wikipedia</a> compares the formats. The desk's point is the chain: source, player, cable and panel must all support the same format, and the weakest one decides.</p>",

"tech/hosting-types-compared-shared-vps-cloud-dedicated":
    "<p><b>The categories differ in isolation, not in name.</b> What a virtual private server actually guarantees is a technical question, and the <a href=\"" + _w("virtual+private+server") + "\" rel=\"noopener\">VPS reference material on Wikipedia</a> describes the virtualisation behind it. The <a href=\"" + IETF + "\" rel=\"noopener\">IETF</a> publishes the protocols all four types implement, which is where most real differences hide.</p>",

"tech/how-large-language-models-actually-work":
    "<p><b>The architecture is published research.</b> Tokenisation, attention and training are documented in the <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large-language-model reference material on Wikipedia</a>, and the <a href=\"" + MDN + "\" rel=\"noopener\">MDN documentation</a> covers the browser-side APIs that now expose them. The desk explains the mechanics plainly because the mystique is doing commercial work.</p>",

"tech/how-the-internet-works":
    "<p><b>It works because the standards are public.</b> The protocols behind routing, naming and transport are published by the <a href=\"" + IETF + "\" rel=\"noopener\">Internet Engineering Task Force</a>, and domain-name administration sits with <a href=\"" + IANA + "\" rel=\"noopener\">IANA</a>. The desk's plain-English version cites them throughout, because a reader who wants the formal text should be one click away.</p>",

"tech/how-to-read-an-error-message":
    "<p><b>Messages follow conventions worth learning.</b> HTTP status codes are defined in the <a href=\"" + MDNHTTP + "\" rel=\"noopener\">HTTP specification documentation</a>, and the <a href=\"" + _w("error+message") + "\" rel=\"noopener\">error-message reference material on Wikipedia</a> covers design practice. The desk's method is transferable: read the last line first, note what changed, then reproduce it deliberately.</p>",

"tech/how-to-take-a-screenshot-windows":
    "<p><b>The methods are documented by the vendor.</b> <a href=\"" + MSWIN + "\" rel=\"noopener\">Microsoft's official Windows documentation</a> describes each capture route — full screen, active window, region, clipboard versus file — and the differences that decide which to use. The desk's guide adds the part the documentation skips: where the files land and how to change it.</p>",

"tech/iphone-vs-android-nigeria":
    "<p><b>A repair-economy question, not a spec question.</b> Parts availability and technician density decide the real cost of ownership, and the desk records what it observes in the market rather than quoting a global average. Where connectivity or spectrum is at issue, the <a href=\"" + NCC + "\" rel=\"noopener\">Nigerian Communications Commission</a> publishes the regulatory context.</p>",

"tech/jumia-vs-konga-electronics":
    "<p><b>Marketplace rules are published.</b> Buyer protection, returns and seller terms are set out by each platform, and <a href=\"" + KONGA + "\" rel=\"noopener\">Konga</a>'s own policy pages are the desk's reference for one side of this comparison. The <a href=\"" + FTC + "\" rel=\"noopener\">FTC's consumer guidance</a> describes the protections a marketplace should provide, which is the standard the desk measures both against.</p>",

"tech/local-vs-cloud-ai-running-models-on-your-own-hardware":
    "<p><b>The trade-off is documented.</b> What local inference costs in hardware and what cloud inference costs in data exposure are described in the <a href=\"" + _w("large+language+model") + "\" rel=\"noopener\">large-language-model reference material on Wikipedia</a>, and the <a href=\"" + EFF + "\" rel=\"noopener\">EFF</a> covers the privacy half. The desk's answer depends on one question: does the data leave the building?</p>",

"tech/local-vs-cloud-smart-home-why-it-decides-everything":
    "<p><b>Local control is a privacy and reliability decision.</b> What a device does when the vendor's cloud is unreachable is the test, and the <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a>'s IoT guidance is the desk's reference for setup and update practice. The <a href=\"" + _w("home+automation") + "\" rel=\"noopener\">home-automation reference material on Wikipedia</a> describes the architectures.</p>",

"tech/methodology":
    "<p><b>How this desk decides what is true.</b> Specifications come from the bodies that publish them — the <a href=\"" + IETF + "\" rel=\"noopener\">IETF</a>, <a href=\"" + W3C + "\" rel=\"noopener\">W3C</a> and the standards organisations named on each page — and safety guidance from <a href=\"" + CISA + "\" rel=\"noopener\">CISA</a> and the <a href=\"" + NCSC + "\" rel=\"noopener\">NCSC</a>. Where the desk relies on its own testing, the page says so and dates it.</p>",

"tech/monitor-buying-what-you-actually-see":
    "<p><b>Three numbers, one viewing distance.</b> Pixel density, refresh rate and panel type interact, and the reference material for <a href=\"" + _w("display+resolution") + "\" rel=\"noopener\">resolution</a> and <a href=\"" + _w("refresh+rate") + "\" rel=\"noopener\">refresh rate</a> on Wikipedia explains the arithmetic. The desk's advice is to buy for the distance you actually sit at, which is the variable spec sheets never mention.</p>",

"tech/open-source-software-what-free-really-means":
    "<p><b>\"Free\" is a defined term.</b> The <a href=\"" + OPENSOURCE + "\" rel=\"noopener\">Open Source Initiative</a> publishes the definition that licences are measured against, and the <a href=\"" + _w("open-source+software") + "\" rel=\"noopener\">open-source reference material on Wikipedia</a> covers the licence families. The desk's distinction matters commercially: open source means you may inspect and modify, not that support is included.</p>",

"tech/password-manager-or-browser":
    "<p><b>The comparison has published guidance.</b> The <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> publishes password-manager advice, and <a href=\"" + HIBP + "\" rel=\"noopener\">Have I Been Pwned</a> lets you check whether a credential has already leaked. The desk's conclusion is narrower than either camp claims: the deciding factor is sync and export, not encryption.</p>",

"tech/phone-acting-up-symptom-finder":
    "<p><b>Symptoms map to a short list of causes.</b> Storage pressure, thermal throttling and background load explain most of them, and the official <a href=\"" + GANDROID + "\" rel=\"noopener\">Android help documentation</a> describes the diagnostics built into the platform. The desk's finder is ordered by likelihood, so the common causes are checked before the expensive ones.</p>",

"tech/phone-overheating-causes-and-fixes":
    "<p><b>Heat is a design limit, not a fault.</b> Devices throttle deliberately to protect the silicon, and the <a href=\"" + _w("thermal+management+of+electronic+devices+and+systems") + "\" rel=\"noopener\">thermal-management reference material on Wikipedia</a> explains the mechanisms. The desk's fixes are ordered by effect: shade and case first, background load second, because the first is free.</p>",

"tech/position-sizing-ruin-the-math-most-backtests-skip":
    "<p><b>Risk of ruin is calculable.</b> The mathematics of drawdown and bet sizing is standard, and the <a href=\"" + _w("risk+of+ruin") + "\" rel=\"noopener\">risk-of-ruin reference material on Wikipedia</a> sets it out. The desk's framing follows the investor-education line taken by <a href=\"" + INVESTOR + "\" rel=\"noopener\">investor.gov</a>: position sizing is a risk decision, and this page is education rather than advice.</p>",

"tech/public-wifi-risks":
    "<p><b>The real risk is narrower than advertised.</b> Encrypted transport has removed most of the classic threat, and the <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> publishes guidance on public networks; the transport itself is specified in <a href=\"" + IETF + "\" rel=\"noopener\">IETF</a> documents. The desk's advice concentrates on what remains: captive portals, rogue networks and unpatched devices.</p>",

"tech/quant":
    "<p><b>Methods, with their limits stated.</b> The statistical machinery here is documented in the <a href=\"" + _w("quantitative+analysis+(finance)") + "\" rel=\"noopener\">quantitative-analysis reference material on Wikipedia</a>, and the desk follows the <a href=\"" + INVESTOR + "\" rel=\"noopener\">investor.gov</a> line on what such methods cannot promise. Nothing on this shelf is investment advice, and every page says so.</p>",

"tech/regime-change-or-random-walk-telling-them-apart":
    "<p><b>A statistical question with a literature.</b> Distinguishing a structural break from noise is a studied problem, and the <a href=\"" + _w("structural+break") + "\" rel=\"noopener\">structural-break reference material on Wikipedia</a> covers the tests. The desk's caution follows the random-walk evidence: most apparent shifts are not, which is why the page insists on out-of-sample confirmation.</p>",

"tech/render-static-deploy":
    "<p><b>Platform behaviour, from the platform.</b> Build, deploy and routing behaviour are documented by <a href=\"" + RENDER + "\" rel=\"noopener\">Render's own documentation</a>, which the desk cites for anything version-specific and dates the reading. The underlying web standards come from the <a href=\"" + W3C + "\" rel=\"noopener\">W3C</a>, which is why the same static site moves between hosts with so little change.</p>",

"tech/reproducible-quant-research-why-it-matters":
    "<p><b>Reproducibility is a method, not a virtue.</b> The practices — pinned data, versioned code, recorded parameters — come from the wider scientific literature summarised in the <a href=\"" + _w("reproducibility") + "\" rel=\"noopener\">reproducibility reference material on Wikipedia</a>. The desk's version is blunt: a result you cannot re-run is an anecdote with a chart attached.</p>",

"tech/router-dns-slow-browsing-fix":
    "<p><b>Name resolution has a documented failure mode.</b> DNS lookups precede every connection, and the <a href=\"" + IETF + "\" rel=\"noopener\">IETF</a> publishes the protocol while <a href=\"" + IANA + "\" rel=\"noopener\">IANA</a> administers the root zone. The desk's test separates the two cases properly: fast downloads with slow page loads is a resolver problem, not a bandwidth one.</p>",

"tech/router-firmware-backdoor":
    "<p><b>Respond to the disclosure, not the headline.</b> The <a href=\"" + CISA + "\" rel=\"noopener\">Cybersecurity and Infrastructure Security Agency</a> publishes vulnerability advisories, and the <a href=\"" + NCSC + "\" rel=\"noopener\">NCSC</a> covers the home-device side. The desk's twenty-minute routine is the standard response: identify the model, check the advisory, update or isolate — in that order.</p>",

"tech/saas-free-vs-paid-how-to-choose":
    "<p><b>The free tier is a business model.</b> What it costs you in limits, lock-in and support is the real comparison, and the <a href=\"" + _w("software+as+a+service") + "\" rel=\"noopener\">SaaS reference material on Wikipedia</a> describes the model. The desk's decision rule: pay when the free tier's limit is on your work, not on your convenience.</p>",

"tech/saas-lock-in-and-data-portability":
    "<p><b>Exit is a format question.</b> Whether you can leave depends on export fidelity, and the <a href=\"" + _w("vendor+lock-in") + "\" rel=\"noopener\">vendor-lock-in reference material on Wikipedia</a> describes the mechanisms. The <a href=\"" + W3C + "\" rel=\"noopener\">W3C</a>'s open standards are the practical antidote: an open format is the cheapest insurance a small team can buy.</p>",

"tech/saas-pricing-models-explained":
    "<p><b>Four models, four risk allocations.</b> Per-seat, usage, flat and hybrid pricing shift cost risk differently, and the <a href=\"" + _w("software+as+a+service") + "\" rel=\"noopener\">SaaS reference material on Wikipedia</a> covers the model's economics. The desk's comparison adds the line most pricing pages omit: what happens to your data and workflow when you stop paying.</p>",

"tech/sd-card-not-reading-recovery":
    "<p><b>Stop writing to the card immediately.</b> File systems keep data after a directory entry is lost, and the <a href=\"" + _w("file+system") + "\" rel=\"noopener\">file-system reference material on Wikipedia</a> explains why an overwrite is the only irreversible step. The desk's order follows from that: test the reader, test the card elsewhere, image it, then attempt recovery.</p>",

"tech/self-hosting-saas-when-its-worth-it":
    "<p><b>Owning the server is an operations commitment.</b> What administration actually involves is described in the <a href=\"" + _w("self-hosting+(web+services)") + "\" rel=\"noopener\">self-hosting reference material on Wikipedia</a>, and the security baseline comes from <a href=\"" + CISA + "\" rel=\"noopener\">CISA</a> and the <a href=\"" + NCSC + "\" rel=\"noopener\">NCSC</a>. The desk's honest test: do you want a hobby, or do you want the software?</p>",

"tech/sitemap-indexnow":
    "<p><b>Both formats are published specifications.</b> The <a href=\"" + SITEMAPS + "\" rel=\"noopener\">sitemaps.org protocol</a> and the <a href=\"" + INDEXNOW + "\" rel=\"noopener\">IndexNow specification</a> define what these files and pings may contain. The desk's advice is to treat them as declarations rather than persuasion: they tell a crawler what exists, and nothing in them makes a page worth ranking.</p>",

"tech/smart-bulb-flicker-the-real-causes":
    "<p><b>Three causes, all electrical or firmware.</b> Dimmer compatibility, minimum load and update loops explain most flicker, and the <a href=\"" + _w("light-emitting+diode") + "\" rel=\"noopener\">LED reference material on Wikipedia</a> covers the driver behaviour behind it. The desk's order tests the cheapest cause first: remove the bulb from any dimmer circuit and see what happens.</p>",

"tech/smart-home-automations-that-only-mostly-work":
    "<p><b>Reliability is an architecture property.</b> Automations that depend on a distant cloud inherit its latency and its outages, and the <a href=\"" + _w("home+automation") + "\" rel=\"noopener\">home-automation reference material on Wikipedia</a> describes the local and cloud architectures. The <a href=\"" + NCSC + "\" rel=\"noopener\">NCSC's IoT guidance</a> is the desk's reference for the update habits that keep either working.</p>",

"tech/smart-home-devices-stop-getting-updates":
    "<p><b>An unpatched device is a network risk.</b> The <a href=\"" + CISA + "\" rel=\"noopener\">Cybersecurity and Infrastructure Security Agency</a> publishes guidance on end-of-support devices and the vulnerabilities that follow, and the <a href=\"" + NCSC + "\" rel=\"noopener\">NCSC</a> covers the household version. The desk's advice is the same as theirs: isolate what you cannot update.</p>",

"tech/smart-home-features-behind-a-subscription":
    "<p><b>The practice has a name, and a regulator's attention.</b> Feature removal after purchase and subscription-gated capabilities are the subject of <a href=\"" + FTC + "\" rel=\"noopener\">Federal Trade Commission</a> consumer guidance, and the <a href=\"" + _w("subscription+business+model") + "\" rel=\"noopener\">subscription-model reference material on Wikipedia</a> describes the economics. The desk's buying test: does the device work fully with no account at all?</p>",

"tech/smart-home-on-its-own-network":
    "<p><b>Segmentation is standard security practice.</b> Guest networks and VLANs limit what a compromised device can reach, and the <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> publishes the guidance behind this desk's setup. The wireless generations and their security modes are documented by <a href=\"" + WIFI + "\" rel=\"noopener\">the Wi-Fi Alliance</a>.</p>",

"tech/smart-home-updates-the-security-habit-nobody-does":
    "<p><b>Updating is the highest-value habit there is.</b> <a href=\"" + CISA + "\" rel=\"noopener\">CISA</a> publishes the reasoning behind prompt patching, including how quickly disclosed vulnerabilities are exploited, and the <a href=\"" + NCSC + "\" rel=\"noopener\">NCSC</a> covers the device-update side. The desk's routine is deliberately small: one monthly pass, automatic where it is safe.</p>",

"tech/smart-tv-app-freezes-cache":
    "<p><b>A cache is a stored copy, and stale copies misbehave.</b> The mechanism is standard across platforms, and the <a href=\"" + _w("cache+(computing)") + "\" rel=\"noopener\">cache reference material on Wikipedia</a> explains why clearing it helps and what it costs. The desk's order — cold restart, cache, update, reinstall — is arranged so each step preserves your settings as long as possible.</p>",

"tech/smr-vs-cmr-hard-drives":
    "<p><b>The recording method changes the behaviour.</b> Shingled and conventional recording differ in how tracks are written, and the <a href=\"" + _w("shingled+magnetic+recording") + "\" rel=\"noopener\">SMR reference material on Wikipedia</a> explains why one stutters under sustained writes. The desk's advice is to check the specification rather than the price, because the difference is invisible until it matters.</p>",

"tech/spotting-ai-fakes-and-deepfakes":
    "<p><b>Detection is an arms race, and the checks are humble.</b> The generation techniques are described in the <a href=\"" + _w("deepfake") + "\" rel=\"noopener\">deepfake reference material on Wikipedia</a>, and the <a href=\"" + EFF + "\" rel=\"noopener\">Electronic Frontier Foundation</a> covers the policy side. The desk's practical advice is verification by provenance — find the original — rather than trusting your eye.</p>",

"tech/ssl-certificate-errors-explained":
    "<p><b>Each warning means something specific.</b> Certificate validation is specified in <a href=\"" + IETF + "\" rel=\"noopener\">IETF</a> documents and the transport in <a href=\"" + _w("transport+layer+security") + "\" rel=\"noopener\">the TLS reference material on Wikipedia</a>; <a href=\"" + LETSENCRYPT + "\" rel=\"noopener\">Let's Encrypt</a> documents the free issuance path most sites use. The desk's rule: a certificate warning is never something to click through.</p>",

"tech/streaming":
    "<p><b>How the delivery works, and what it costs.</b> Adaptive streaming and content delivery are described in the <a href=\"" + _w("streaming+media") + "\" rel=\"noopener\">streaming-media reference material on Wikipedia</a>, and the transport standards come from the <a href=\"" + IETF + "\" rel=\"noopener\">IETF</a>. The desk's shelves separate the technical questions from the commercial ones, because they have different answers.</p>",

"tech/streaming-subscription-stacking-when-bundle-cheaper":
    "<p><b>Bundle arithmetic, done honestly.</b> The comparison that matters is what you actually watch, and the desk's method records viewing rather than assuming it. Cancellation and renewal practices are the subject of <a href=\"" + FTC + "\" rel=\"noopener\">FTC</a> consumer guidance, which is where the page sends readers when a bundle becomes hard to leave.</p>",

"tech/subscription-audit-that-actually-sticks":
    "<p><b>Start from the statement, not from memory.</b> The audit method here is arithmetic, and the consumer-protection context — including how automatic renewals must be disclosed — is published by the <a href=\"" + FTC + "\" rel=\"noopener\">Federal Trade Commission</a>. The <a href=\"" + _w("subscription+business+model") + "\" rel=\"noopener\">subscription-model reference material on Wikipedia</a> explains why the model is so sticky by design.</p>",

"tech/subscriptions":
    "<p><b>The model, and the exits.</b> Subscription economics are described in the <a href=\"" + _w("subscription+business+model") + "\" rel=\"noopener\">subscription-model reference material on Wikipedia</a>, and the <a href=\"" + FTC + "\" rel=\"noopener\">FTC's consumer guidance</a> covers the renewal and cancellation rules that decide how hard leaving is. The desk's shelves are written for the second question as much as the first.</p>",

"tech/survivorship-bias-the-quiet-data-trap":
    "<p><b>A classic bias with a standard remedy.</b> Testing on today's survivors inflates results, and the <a href=\"" + _w("survivorship+bias") + "\" rel=\"noopener\">survivorship-bias reference material on Wikipedia</a> explains the mechanism with its canonical examples. The desk applies it to market data, where the bias is worst because the delisted names disappear from the dataset entirely.</p>",

"tech/tool/internet-speed-calculator":
    "<p><b>Requirements depend on the activity, not the headline number.</b> Bitrate needs for video calls, streaming and uploads are documented in the <a href=\"" + _w("bitrate") + "\" rel=\"noopener\">bitrate reference material on Wikipedia</a>, and the codec containers are registered with <a href=\"" + IANA + "\" rel=\"noopener\">IANA's media-type registry</a>. This tool runs in your browser and sends nothing anywhere.</p>",

"tech/tool/video-file-size-estimator":
    "<p><b>One relationship: bitrate times duration.</b> The units behind it are where estimates go wrong by a factor of eight, and the <a href=\"" + _w("bitrate") + "\" rel=\"noopener\">bitrate reference material on Wikipedia</a> sets out the definitions. Codec and container choices change the result, which is why this tool states its assumptions rather than hiding them.</p>",

"tech/transaction-costs-slippage-backtest-reality":
    "<p><b>Costs are what turn a paper result into a real one.</b> Spread, commission and market impact are standard transaction-cost concepts, described in the <a href=\"" + _w("transaction+cost") + "\" rel=\"noopener\">transaction-cost reference material on Wikipedia</a>. The desk follows the <a href=\"" + INVESTOR + "\" rel=\"noopener\">investor.gov</a> approach of naming costs plainly; nothing here is investment advice.</p>",

"tech/ubuntu-vs-debian-home-server":
    "<p><b>Two distributions, one lineage.</b> Both publish their own release and support documentation — <a href=\"" + DEBIAN + "\" rel=\"noopener\">Debian</a> and <a href=\"" + UBUNTU + "\" rel=\"noopener\">Ubuntu</a> — and the <a href=\"" + KERNEL + "\" rel=\"noopener\">Linux kernel documentation</a> covers the layer beneath both. The desk's recommendation turns on one question: do you want the newest packages or the longest support window?</p>",

"tech/unix-time-explained":
    "<p><b>A single number, and one famous deadline.</b> Counting seconds from the epoch removes time-zone ambiguity, and the <a href=\"" + _w("unix+time") + "\" rel=\"noopener\">Unix-time reference material on Wikipedia</a> covers the convention and the 2038 overflow. The desk's companion <a href=\"/tech/tool/timestamp-converter/\">converter</a> handles seconds-versus-milliseconds, the error that catches most people first.</p>",

"tech/use-less-mobile-data":
    "<p><b>Most savings come from a few settings.</b> Video resolution, background sync and app updates account for the bulk of consumption, and the official <a href=\"" + GANDROID + "\" rel=\"noopener\">Android help documentation</a> describes the controls. Where network conditions are the real constraint, the <a href=\"" + NCC + "\" rel=\"noopener\">Nigerian Communications Commission</a> publishes the regulatory and coverage context.</p>",

"tech/walk-forward-validation-explained":
    "<p><b>Test on data the model has not seen.</b> The technique is a form of out-of-sample validation, and the <a href=\"" + _w("cross-validation+(statistics)") + "\" rel=\"noopener\">cross-validation reference material on Wikipedia</a> explains the family it belongs to. The desk's caution is the usual one: walk-forward reduces overfitting, but it cannot rescue a strategy with no edge.</p>",

"tech/what-is-a-cdn-why-your-site-needs-one":
    "<p><b>Caching closer to the reader.</b> The mechanism is documented in the <a href=\"" + _w("content+delivery+network") + "\" rel=\"noopener\">CDN reference material on Wikipedia</a>, and the transport standards it relies on are published by the <a href=\"" + IETF + "\" rel=\"noopener\">IETF</a>. The desk's small-site case is honest: a CDN helps latency and resilience, and it does not fix slow content.</p>",

"tech/what-is-a-database":
    "<p><b>From spreadsheet to system, in steps.</b> The concepts — tables, keys, queries, transactions — are described in the <a href=\"" + _w("database") + "\" rel=\"noopener\">database reference material on Wikipedia</a>, and the query language most beginners meet is documented in the <a href=\"" + MDN + "\" rel=\"noopener\">MDN documentation</a>'s wider platform guides. The desk's framing is practical: a database is a spreadsheet that never loses its shape.</p>",

"tech/what-is-a-vps-when-you-need-one":
    "<p><b>Virtualisation, and what it guarantees.</b> The technology behind a virtual private server is described in the <a href=\"" + _w("virtual+private+server") + "\" rel=\"noopener\">VPS reference material on Wikipedia</a>, and the <a href=\"" + KERNEL + "\" rel=\"noopener\">Linux kernel documentation</a> covers the isolation features underneath. The desk's signs you have outgrown shared hosting are behavioural, not technical.</p>",

"tech/what-is-an-api":
    "<p><b>An interface with a contract.</b> The general concept is described in the <a href=\"" + _w("API") + "\" rel=\"noopener\">API reference material on Wikipedia</a>, and the web conventions most readers meet are documented by <a href=\"" + MDNHTTP + "\" rel=\"noopener\">MDN's HTTP documentation</a>. The desk's explanation uses the restaurant analogy once and then drops it, because the contract is the part that matters.</p>",

"tech/why-ai-hallucinates-and-how-to-fact-check":
    "<p><b>Confident error is a property of the design.</b> Why these systems produce plausible falsehoods is explained in the <a href=\"" + _w("hallucination+(artificial+intelligence)") + "\" rel=\"noopener\">AI-hallucination reference material on Wikipedia</a>. The desk's checking habit is the same one it applies to itself: every claim traced to a source you could produce in a minute.</p>",

"tech/why-backtests-overfit-degrees-of-freedom":
    "<p><b>Flexibility buys false confidence.</b> Each parameter fitted is a degree of freedom spent, and the <a href=\"" + _w("overfitting") + "\" rel=\"noopener\">overfitting reference material on Wikipedia</a> explains the mechanism. The desk's practical rule is the one professionals use: fewer parameters, longer history, and a result that survives a period it was never tuned on.</p>",

"tech/why-is-my-computer-slow":
    "<p><b>Triage in the order that finds the cause.</b> Storage pressure, memory exhaustion, thermal throttling and startup load are the usual four, and the <a href=\"" + MSWIN + "\" rel=\"noopener\">official Windows documentation</a> describes the built-in diagnostics. The desk's order is deliberate: check the free space and the temperatures before reinstalling anything.</p>",

"tech/why-streams-buffer-at-night":
    "<p><b>Shared capacity, predictable peaks.</b> Evening congestion on access networks is a documented pattern, and the <a href=\"" + _w("network+congestion") + "\" rel=\"noopener\">network-congestion reference material on Wikipedia</a> explains the mechanisms. Where local conditions dominate, the <a href=\"" + NCC + "\" rel=\"noopener\">Nigerian Communications Commission</a> publishes the operator and coverage context the desk cites for Nigerian readers.</p>",

"tech/windows":
    "<p><b>The platform's own documentation, linked.</b> <a href=\"" + MSWIN + "\" rel=\"noopener\">Microsoft's official Windows documentation</a> is the desk's reference for settings, updates and recovery — the fastest route to an answer that will still be true next year. Where a fix involves the registry or system files, the page says so and links the vendor's warning alongside it.</p>",

"tech/windows-update-problems":
    "<p><b>Stuck updates have a documented recovery path.</b> <a href=\"" + MSWIN + "\" rel=\"noopener\">Microsoft's official Windows documentation</a> describes the troubleshooting steps and the components involved, which is why the desk's guide starts there rather than with forum fixes. The security case for updating promptly is published by <a href=\"" + CISA + "\" rel=\"noopener\">CISA</a>.</p>",

"tech/writing-better-prompts-plain-english":
    "<p><b>Clarity works because of how these systems are trained.</b> The behaviour behind prompt phrasing is described in the <a href=\"" + _w("prompt+engineering") + "\" rel=\"noopener\">prompt-engineering reference material on Wikipedia</a>. The desk's argument is the unfashionable one: there are no incantations, only clear instructions — and the <a href=\"" + MDN + "\" rel=\"noopener\">MDN documentation</a> is a good model of the precision worth copying.</p>",

# ============================= SPORTS (7) ====================================

"sports/bundesliga-table":
    "<p><b>Standings, with their source named.</b> The competition's structure and rules are documented in the <a href=\"" + _w("Bundesliga") + "\" rel=\"noopener\">encyclopaedic record</a>, and the desk records the table with the date it was checked rather than implying a live feed. Where a column needs explaining — goal difference, head-to-head tiebreaks — the page explains it.</p>",

"sports/la-liga-table":
    "<p><b>Checked, dated, and explained.</b> The league's own published records sit at <a href=\"" + LALIGA + "\" rel=\"noopener\">LaLiga</a>, and the desk states when this table was last verified. Tiebreak rules are set out on the page because they decide more seasons than points do, and readers should not have to look them up mid-argument.</p>",

"sports/ligue-1-table":
    "<p><b>A snapshot, not a live service.</b> The competition's published records are at <a href=\"" + LIGUE1 + "\" rel=\"noopener\">Ligue 1</a>, and this page carries the date it was checked. The desk's rule for every standings page is the same: state the check date, explain the tiebreaks, and never imply a fixture result that has not been confirmed.</p>",

"sports/serie-a-table":
    "<p><b>Table, rules and check date.</b> The competition's format and history are documented in the <a href=\"" + _w("Serie+A") + "\" rel=\"noopener\">encyclopaedic record</a>, and the desk records the standings with the date of verification. Where the tiebreak order decides a place, the page prints it — because that is usually the part a reader actually came for.</p>",

"sports/possession-explained":
    "<p><b>A statistic with a known limitation.</b> How possession is measured and what it correlates with is described in the <a href=\"" + _w("possession+(football)") + "\" rel=\"noopener\">football-possession reference material on Wikipedia</a>. The desk's position is the honest one: it measures where the ball was, not how dangerous anything was, and the page says which questions it cannot answer.</p>",

"sports/what-does-a-sporting-director-do":
    "<p><b>A role with a documented history.</b> Responsibilities vary by club and league, and the <a href=\"" + _w("sporting+director") + "\" rel=\"noopener\">sporting-director reference material on Wikipedia</a> sets out how the role developed and differs across countries. The desk separates what the title means on paper from what it means at a club with an active owner.</p>",

"sports/why-football-transfers-collapse":
    "<p><b>The mechanics, documented.</b> How transfers actually complete — agreement, personal terms, medical, registration — is described in the <a href=\"" + _w("transfer+(association+football)") + "\" rel=\"noopener\">transfer reference material on Wikipedia</a>, and the window rules sit with each competition. The desk's argument is the one the fee column hides: most collapses happen after the number is agreed.</p>",

}
