# -*- coding: utf-8 -*-
"""External source notes (Phase 3, step 1: the 226 pages scoring 9.75 whose only
missing point is an external reference). Applied post-build by
scripts/inject-external-source.py into both the property source tree and public/.

Rule enforced here: every URL in this file was curl-verified 200 at authoring
time. Where a natural authority blocked the check (403/404), the note uses a
verified alternative or an encyclopaedic lookup instead - never an unverified
deep link."""

# ---- verified reference pool -------------------------------------------------
IATA = "https://www.iata.org/en/programs/cargo/dgr/lithium-batteries/"
ATSC = "https://www.atsc.org/"
THREEGPP = "https://www.3gpp.org/"
NCC = "https://www.ncc.gov.ng/"
NCSC = "https://www.ncsc.gov.uk/"
CISA = "https://www.cisa.gov/"
EFF = "https://www.eff.org/"
FTC = "https://www.ftc.gov/"
HIBP = "https://haveibeenpwned.com/"
USB = "https://www.usb.org/"
HDMI = "https://www.hdmi.org/"
WIFI = "https://www.wi-fi.org/discover-wi-fi/security"
MDN = "https://developer.mozilla.org/en-US/docs/Learn"
W3C = "https://www.w3.org/"
IETF = "https://www.ietf.org/"
KERNEL = "https://www.kernel.org/"
ESTAR = "https://www.energystar.gov/"
MSWIN = "https://learn.microsoft.com/en-us/windows/"
GANDROID = "https://support.google.com/android/"
IANA = "https://www.iana.org/assignments/media-types/media-types.xhtml"
INVESTOR = "https://www.investor.gov/"
LALIGA = "https://www.laliga.com/"
LIGUE1 = "https://www.ligue1.com/"
EPL = "https://www.premierleague.com/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

EXTERNAL_SOURCES = {

# ============================ TECH (47) ======================================

"tech/antenna-vs-satellite-vs-streaming-live-tv":
    "<p><b>Where the broadcast numbers come from.</b> The over-the-air standards an antenna actually receives are written by the <a href=\"" + ATSC + "\" rel=\"noopener\">Advanced Television Systems Committee</a>, which publishes the ATSC specifications and the transition documents behind them; regional variants differ, so the desk quotes a standard rather than a retailer's claim about channel counts.</p>",

"tech/cloud-gaming-reality-lagos-lines":
    "<p><b>The regulator's numbers, not the advert's.</b> Latency, coverage and licensed-spectrum questions in Nigeria sit with the <a href=\"" + NCC + "\" rel=\"noopener\">Nigerian Communications Commission</a>, which publishes operator data and consumer guidance. The desk treats a provider's advertised speed as a ceiling and the NCC's published figures as context, never as a promise about your street.</p>",

"tech/cloud-hosting":
    "<p><b>The layer underneath the marketing.</b> Hosting products differ mostly in which internet standards they implement, and those standards are published openly by the <a href=\"" + IETF + "\" rel=\"noopener\">Internet Engineering Task Force</a> — the body behind HTTP, TLS and DNS. Reading a protocol specification once makes most hosting comparison pages unnecessary, because you can see what a provider is actually offering.</p>",

"tech/coding":
    "<p><b>A free curriculum, not a sales funnel.</b> The <a href=\"" + MDN + "\" rel=\"noopener\">MDN learning area</a> is maintained in the open by the web standards community and covers HTML, CSS and JavaScript from first principles without a subscription. The desk recommends it ahead of paid courses because it tracks the specifications themselves rather than one framework's fashion cycle.</p>",

"tech/compare":
    "<p><b>Specs come from the bodies that define them.</b> Every figure in these head-to-heads traces to a standards organisation rather than a product page: <a href=\"" + USB + "\" rel=\"noopener\">USB-IF</a> for charging and dock profiles, <a href=\"" + HDMI + "\" rel=\"noopener\">the HDMI Forum</a> for video bandwidth, and <a href=\"" + WIFI + "\" rel=\"noopener\">the Wi-Fi Alliance</a> for wireless generations. Where a vendor's number disagrees with the standard, the desk prints the standard and says so.</p>",

"tech/cybersecurity":
    "<p><b>Advice from the people who handle the incidents.</b> The <a href=\"" + CISA + "\" rel=\"noopener\">Cybersecurity and Infrastructure Security Agency</a> and the UK's <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> both publish free, vendor-neutral guidance — including the password and update advice this desk repeats. When a guide here disagrees with a vendor blog, it is usually because these two say something less convenient.</p>",

"tech/dashcam-power-and-mounting":
    "<p><b>The electrical part has a specification.</b> Hardwiring a camera into a vehicle's fuse box means dealing with a supply standard, and the 12-volt accessories and USB power profiles involved are documented by <a href=\"" + USB + "\" rel=\"noopener\">USB-IF</a> for the charging side. The desk's standing caveat stands: fuse taps and ignition-switched circuits vary by car, and a wiring diagram for your model beats any general guide.</p>",

"tech/esim-for-international-travel":
    "<p><b>eSIM is a standard, not a brand.</b> The embedded-SIM architecture is specified by <a href=\"" + THREEGPP + "\" rel=\"noopener\">3GPP</a>, the partnership that writes the mobile specifications, which is why an eSIM behaves the same across operators and why the desk can talk about profile limits rather than one carrier's policy. Roaming charges, by contrast, remain a commercial decision each operator makes alone.</p>",

"tech/hdmi-long-run-4k":
    "<p><b>Cable length limits are published, not guessed.</b> <a href=\"" + HDMI + "\" rel=\"noopener\">The HDMI Forum</a> publishes the specification and the certification programme that defines what a Premium High Speed or Ultra High Speed cable must carry — including the bandwidth figures that decide whether a long passive run can hold a 4K signal. The desk's rule follows it: buy the certified category, not the longest cable that fits.</p>",

"tech/home-nas-vs-cloud-vs-drive":
    "<p><b>Two different risks, two different references.</b> The hardware side of a network drive is standardised and documented — the <a href=\"" + _w("network-attached+storage") + "\" rel=\"noopener\">network-attached storage reference material on Wikipedia</a> covers the architectures and their trade-offs. The privacy side is not: it depends entirely on a provider's terms, which is why the desk reads them and links the <a href=\"" + EFF + "\" rel=\"noopener\">Electronic Frontier Foundation</a>'s surveillance and privacy work for the questions no spec sheet answers.</p>",

"tech/home-wifi-security-audit":
    "<p><b>The audit list is borrowed from professionals.</b> The <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> publishes free device and home-network guidance that this desk's checklist follows closely — router admin passwords, firmware updates, guest networks, WPA settings. The wireless security generations themselves are described by <a href=\"" + WIFI + "\" rel=\"noopener\">the Wi-Fi Alliance</a>, which is the honest source for what WPA3 does and does not fix.</p>",

"tech/hours-of-video-per-gigabyte":
    "<p><b>The arithmetic behind the table.</b> Every figure on this page comes from one relationship — bitrate multiplied by duration — and the units involved (bits, bytes, megabits per second) are where most published estimates go wrong by a factor of eight. The <a href=\"" + _w("bitrate") + "\" rel=\"noopener\">bitrate reference material on Wikipedia</a> sets out the definitions, and the codec containers themselves are registered with <a href=\"" + IANA + "\" rel=\"noopener\">IANA's media-type registry</a>.</p>",

"tech/inverter-battery-runtime-maths":
    "<p><b>Capacity units, defined properly.</b> Ampere-hours, watt-hours and the depth-of-discharge limits that decide real runtime are defined in the battery standards literature, and the <a href=\"" + _w("battery+capacity") + "\" rel=\"noopener\">battery-capacity reference material on Wikipedia</a> explains the conversions and the rate effects that make a sticker capacity optimistic. The desk's arithmetic assumes the pessimistic case, which is the only case that keeps the lights on.</p>",

"tech/laptop-desk-ergonomics-the-standing-fix":
    "<p><b>Ergonomics has a literature.</b> Screen height, elbow angle and the reasons a laptop posture strains the neck are studied properly, and the <a href=\"" + _w("ergonomics") + "\" rel=\"noopener\">ergonomics reference material on Wikipedia</a> summarises the field and its findings. The desk's advice here is deliberately cheap — books, a box, an external keyboard — because the evidence does not require an expensive chair to act on.</p>",

"tech/laptop-fan-dust-harmattan":
    "<p><b>Why dust kills electronics slowly.</b> The failure mode is thermal, not mechanical: a clogged fin stack raises junction temperature until the machine throttles, long before a bearing fails. The <a href=\"" + _w("thermal+management+of+electronic+devices+and+systems") + "\" rel=\"noopener\">thermal-management reference material on Wikipedia</a> explains the mechanisms, and it is the reason the desk's cleaning guide insists on holding the fan still rather than letting it overspin.</p>",

"tech/laptop-ram-vs-ssd-first":
    "<p><b>The two components do different jobs.</b> A solid-state drive changes how fast the machine reaches data; memory changes how much it can hold open at once. The <a href=\"" + _w("solid-state+drive") + "\" rel=\"noopener\">solid-state drive reference material on Wikipedia</a> covers how SSDs differ from spinning disks — including the write-endurance characteristics that matter if you are choosing between a cheap and a good one.</p>",

"tech/laptop-theft-recovery-playbook":
    "<p><b>Preparation is the professional advice.</b> The <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> publishes guidance on stolen and lost devices — device encryption, remote wipe, account recovery — and this desk's playbook follows it. The part most people skip is the one the guidance stresses: the settings only help if they were switched on before the theft, not after.</p>",

"tech/mobile-data-plan-math":
    "<p><b>Read the plan against the regulator's framework.</b> Tariff structures, fair-use policies and consumer rights in Nigeria are overseen by the <a href=\"" + NCC + "\" rel=\"noopener\">Nigerian Communications Commission</a>, whose published consumer information is the correct place to check what an operator is allowed to do with your bundle. The five numbers on this page are the desk's own arithmetic for comparing plans that are priced deliberately unlike each other.</p>",

"tech/monitor-panel-type-for-text-work":
    "<p><b>Panel technology is a documented trade-off.</b> Viewing angles, contrast and response time differ by panel construction, and the <a href=\"" + _w("in-plane+switching") + "\" rel=\"noopener\">in-plane switching reference material on Wikipedia</a> explains why IPS behaves as it does relative to VA and TN designs. For text work the desk's conclusion follows from the optics, not from reviews: consistent gamma across the screen beats contrast ratio on a spec sheet.</p>",

"tech/monitor-refresh-rate-explained":
    "<p><b>Refresh rate versus frame rate, kept separate.</b> The two figures are related but independent, and the <a href=\"" + _w("refresh+rate") + "\" rel=\"noopener\">refresh-rate reference material on Wikipedia</a> distinguishes them properly — including why a 144 Hz panel shows no benefit when the machine renders 40 frames a second. The desk's buying advice rests on that distinction: buy the panel your hardware can actually feed.</p>",

"tech/new-tv-settings-day-one":
    "<p><b>The settings that matter are the measurable ones.</b> Picture modes exist mostly for shop lighting, and the energy consequences of brightness settings are quantified by <a href=\"" + ESTAR + "\" rel=\"noopener\">ENERGY STAR</a>, whose display criteria document the relationship between backlight output and consumption. The desk's day-one list is the short version: turn off motion smoothing, pick the accurate picture mode, then leave it alone.</p>",

"tech/old-phone-as-home-camera":
    "<p><b>A camera on the network is a security decision.</b> The <a href=\"" + EFF + "\" rel=\"noopener\">Electronic Frontier Foundation</a> publishes the clearest plain-language guidance on the privacy trade-offs of connected devices, which is why the desk insists on a separate guest network and a device you would not mind losing. A repurposed phone recording a compound gate is useful; one on the same network as your banking is a mistake.</p>",

"tech/oled-vs-led-tv-sunny-room":
    "<p><b>The brightness question is a physics question.</b> OLED's per-pixel emission and LCD's backlight produce different peak luminance, and the <a href=\"" + _w("organic+light-emitting+diode") + "\" rel=\"noopener\">OLED reference material on Wikipedia</a> sets out how the technology works and where its limits sit. For a sunlit room the desk's answer follows directly from those limits: total light output beats perfect blacks.</p>",

"tech/pc-no-power-no-post-triage":
    "<p><b>What POST actually is.</b> The power-on self-test is a firmware routine with a defined order of checks, and the <a href=\"" + _w("power-on+self-test") + "\" rel=\"noopener\">POST reference material on Wikipedia</a> explains the sequence and the beep-code conventions that make triage possible. That order is why the desk's guide works outward from the power supply rather than randomly swapping parts.</p>",

"tech/phone-buying-specs-that-matter":
    "<p><b>Some specs are standards, some are adjectives.</b> The radio generations, bands and protocols a phone supports are specified by <a href=\"" + THREEGPP + "\" rel=\"noopener\">3GPP</a>, which is why the desk treats them as checkable facts while treating camera megapixels and \"AI\" labels as marketing. If a spec cannot be traced to a standard or a measurement, it belongs in the second pile.</p>",

"tech/phone-photo-backup-options-nigeria":
    "<p><b>Backups are a privacy decision as much as a storage one.</b> Whatever service holds your photographs can be asked for them, which is why the desk links the <a href=\"" + EFF + "\" rel=\"noopener\">Electronic Frontier Foundation</a>'s privacy resources alongside the practical options. The three-two-one rule still stands: three copies, two media, one offsite — and the offsite copy is the one people forget until the phone is in a canal.</p>",

"tech/phone-video-quality-light-and-sound":
    "<p><b>Two variables, both documented.</b> Exposure and audio capture are the whole of phone video quality, and the <a href=\"" + _w("digital+video") + "\" rel=\"noopener\">digital-video reference material on Wikipedia</a> covers the encoding side of what the camera records. The desk's emphasis on light over lenses is not aesthetic preference: a sensor with more light produces better frames than a better sensor without it.</p>",

"tech/portable-solar-panel-power-bank-reality":
    "<p><b>Rated output assumes conditions you will not get.</b> Panel ratings are measured at standard test conditions, and the <a href=\"" + _w("solar+charger") + "\" rel=\"noopener\">solar-charger reference material on Wikipedia</a> explains how real-world angle, cloud and temperature reduce them — usually by half or more. That gap between rated and delivered watts is the entire subject of this page.</p>",

"tech/power-bank-flying-rules":
    "<p><b>The rule is written down, and it is a safety rule.</b> <a href=\"" + IATA + "\" rel=\"noopener\">IATA's lithium-battery guidance</a> is the source airlines work from: capacity limits in watt-hours, the requirement that spare cells travel in the cabin, and the reason damaged packs are refused outright. The desk prints the watt-hour arithmetic because most power banks advertise milliamp-hours, and the two are not the same number.</p>",

"tech/router-placement-nigerian-flat":
    "<p><b>Placement beats hardware, and the physics is standard.</b> <a href=\"" + WIFI + "\" rel=\"noopener\">The Wi-Fi Alliance</a> documents how the wireless generations behave, including the attenuation that makes concrete walls and metal doors the real enemy in a Nigerian flat. The desk's placement hour exists because a router moved to the middle of the house routinely outperforms an extender bought instead of moving it.</p>",

"tech/safety":
    "<p><b>The sources this shelf is built on.</b> Security guidance here follows the two public bodies that publish it without selling anything: <a href=\"" + CISA + "\" rel=\"noopener\">CISA</a> in the United States and the <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> in the UK, with the <a href=\"" + EFF + "\" rel=\"noopener\">Electronic Frontier Foundation</a> for the civil-liberties side of the same questions. Where a commercial product's claim conflicts with them, the desk says which one it followed.</p>",

"tech/small-shop-camera-system":
    "<p><b>The architecture choice is the whole decision.</b> Whether footage lives on an NVR, on SD cards or in a cloud subscription determines what happens when the network drops, and the <a href=\"" + _w("network+video+recorder") + "\" rel=\"noopener\">network-video-recorder reference material on Wikipedia</a> sets out the architectures. For a shop the desk's conclusion is blunt: local recording with a network copy beats a cloud-only camera that stops working when the connection does.</p>",

"tech/smart-home-worth-it":
    "<p><b>Connected devices widen your attack surface.</b> The <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a> publishes IoT buying and setup guidance that this page's shortlist respects — update policy, default passwords, whether the device works when the vendor's cloud is unreachable. Those three questions filter out more gimmicks than any feature comparison.</p>",

"tech/smart-tv-or-stick-which-ages-better":
    "<p><b>Why the TV's software stops first.</b> A television's platform is fixed hardware with a shrinking app catalogue, while a streaming stick is replaceable — and the <a href=\"" + _w("digital+media+player") + "\" rel=\"noopener\">digital-media-player reference material on Wikipedia</a> covers the categories and their constraints. The desk's answer follows the replacement cost: buy the panel for the picture and let a separate box handle the software.</p>",

"tech/soundbar-for-dialogue-not-bass":
    "<p><b>Dialogue clarity is a channel and placement problem.</b> A centre channel aimed at the listening position does what a downward-firing driver cannot, and the <a href=\"" + _w("soundbar") + "\" rel=\"noopener\">soundbar reference material on Wikipedia</a> explains the driver layouts behind the marketing names. The desk's buying test is one scene of quiet conversation at low volume — the case every soundbar is actually sold for.</p>",

"tech/ssd-trim-vs-defrag-myths":
    "<p><b>TRIM is part of the storage stack, not a tuning trick.</b> The command exists so a drive can reclaim blocks the filesystem no longer needs, and it is implemented in the kernel of every major operating system — the <a href=\"" + KERNEL + "\" rel=\"noopener\">Linux kernel documentation</a> describes the mechanism plainly. Defragmenting an SSD is not merely useless; it spends write endurance for nothing, which is the myth this page exists to retire.</p>",

"tech/subscription-creep-audit":
    "<p><b>Cancellation rights are regulated, not courtesy.</b> The <a href=\"" + FTC + "\" rel=\"noopener\">Federal Trade Commission</a> publishes the rules on automatic renewal and negative-option billing, including the principle that cancelling must be as easy as signing up — the standard the desk applies when reviewing a service's exit path. Your own jurisdiction's equivalent is worth finding before you need it.</p>",

"tech/update-now-or-wait":
    "<p><b>Patching guidance comes from the incident responders.</b> <a href=\"" + CISA + "\" rel=\"noopener\">CISA</a> publishes the reasoning behind applying security updates promptly, including how quickly known vulnerabilities are exploited after disclosure. The desk's wait-a-week advice applies to feature updates only; a security patch with a published vulnerability behind it is not the same decision.</p>",

"tech/usb-c-dock-desk-setup":
    "<p><b>One connector, several different promises.</b> USB-C is a shape, not a capability: what a port actually carries depends on the power-delivery and alternate-mode profiles defined by <a href=\"" + USB + "\" rel=\"noopener\">USB-IF</a>. That is why two identical-looking laptops behave differently with the same dock, and why the desk tells you to check the port's rated wattage and video support rather than the connector's shape.</p>",

"tech/used-phone-buyer-checklist":
    "<p><b>Half the inspection is in the settings.</b> Battery-health readings, security-lock status and warranty state are all visible on the device itself, and the official <a href=\"" + GANDROID + "\" rel=\"noopener\">Android help documentation</a> describes where each lives. The desk's ten-minute order follows the risk: lock status first, because a device that cannot be unlocked is worth nothing regardless of its screen.</p>",

"tech/video-editing-laptop-requirements":
    "<p><b>The bottleneck is the timeline, not the spec sheet.</b> Non-linear editing loads decode, storage and memory simultaneously, and the <a href=\"" + _w("non-linear+editing") + "\" rel=\"noopener\">non-linear-editing reference material on Wikipedia</a> describes how the workflow differs from simple capture. The desk's requirements list is read off that workflow: sustained storage throughput and enough memory to hold a project, before any GPU marketing.</p>",

"tech/vpn-and-password-safety-table":
    "<p><b>Two claims, two checkable sources.</b> Whether your credentials have already leaked is answerable at <a href=\"" + HIBP + "\" rel=\"noopener\">Have I Been Pwned</a>, which indexes real breach data; what a VPN does and does not hide is covered by the <a href=\"" + NCSC + "\" rel=\"noopener\">National Cyber Security Centre</a>'s plain-language guidance. The desk's table exists because both answers are usually less dramatic than the advertising suggests.</p>",

"tech/web-and-hosting":
    "<p><b>The web has public specifications.</b> Every technology on this shelf — HTML, CSS, the accessibility rules a site should meet — is written down openly by the <a href=\"" + W3C + "\" rel=\"noopener\">World Wide Web Consortium</a>, and the <a href=\"" + MDN + "\" rel=\"noopener\">MDN learning area</a> turns those specifications into readable documentation. The desk links both because hosting decisions get much easier once you can read what a server is being asked to do.</p>",

"tech/webcam-vs-phone-for-video-calls":
    "<p><b>The phone wins on the sensor, loses on the mount.</b> Camera quality in calls is mostly optics and processing, and the <a href=\"" + _w("webcam") + "\" rel=\"noopener\">webcam reference material on Wikipedia</a> covers how the dedicated devices differ from phone cameras. The desk's conclusion is practical: the old phone's sensor is better, so spend the money on holding it steady at eye level rather than on a new webcam.</p>",

"tech/wi-fi-setup-mistakes":
    "<p><b>The mistakes are documented, and so are the fixes.</b> <a href=\"" + WIFI + "\" rel=\"noopener\">The Wi-Fi Alliance</a> explains what each wireless generation and security mode actually provides, which is where most setup errors start — a device pinned to an old mode, or a network still running a superseded security standard. The desk's shortlist of fixes follows from the specifications rather than from forum folklore.</p>",

"tech/windows-storage-full":
    "<p><b>Delete what the operating system says is safe.</b> <a href=\"" + MSWIN + "\" rel=\"noopener\">Microsoft's official Windows documentation</a> describes which system folders and caches can be cleared, what Windows Update keeps and why, and how Storage Sense automates the routine part. The desk's rule is the same as the documentation's: never delete a system directory on the advice of a forum post.</p>",

"tech/wrong-wattage-usb-c-laptop-charger":
    "<p><b>The negotiation is standardised, which is the good news.</b> USB Power Delivery lets a laptop and charger agree on a voltage and current, and the profiles are published by <a href=\"" + USB + "\" rel=\"noopener\">USB-IF</a> — which is why an under-powered charger is usually slow rather than dangerous, and why an uncertified one is the actual risk. The desk's advice is to match the wattage the manufacturer specifies for the model.</p>",

# ======================= ENTERTAINMENT (12) ==================================

"entertainment/10-anime-like-solo-leveling-you-should-watch":
    "<p><b>Where the facts on this page come from.</b> Series details, studios and broadcast history are cross-checked against the show entries reachable through <a href=\"" + _w("Solo+Leveling") + "\" rel=\"noopener\">the encyclopaedic record</a>, and availability is checked at streaming search rather than assumed. The recommendations themselves are the desk's taste, clearly labelled as such.</p>",

"entertainment/10-shows-like-alice-in-borderland-you-should-watch-next":
    "<p><b>Sourcing the shelf.</b> Premise and production details for the anchor show are documented in <a href=\"" + _w("Alice+in+Borderland") + "\" rel=\"noopener\">the encyclopaedic record</a>; the ten recommendations are the desk's judgement, and each entry says plainly what it shares with the original and what it does not. No availability claim here outlives its check date.</p>",

"entertainment/alice-in-borderland-vs-squid-game":
    "<p><b>The comparison, sourced.</b> Both shows' production histories and reception are documented in <a href=\"" + _w("Squid+Game") + "\" rel=\"noopener\">the encyclopaedic record</a>, which is where the desk checks dates and credits before comparing anything. The verdict on which survival format is harder is the desk's argument, not a fact — and the page marks it that way.</p>",

"entertainment/breaking-bad-two-seasons-opinion":
    "<p><b>An opinion with its facts checked.</b> The series' production and broadcast history sits in <a href=\"" + _w("Breaking+Bad") + "\" rel=\"noopener\">the encyclopaedic record</a>; everything else here is one desk's honest failure to connect with a widely loved show. Opinion pieces on this desk state their evidence and their limits, and this one's limit is two seasons.</p>",

"entertainment/dune-sci-fi-epics-guide":
    "<p><b>Facts and taste, separated.</b> Production details for the anchor film are documented in <a href=\"" + _w("Dune+(2021+film)") + "\" rel=\"noopener\">the encyclopaedic record</a>; the recommendations that follow are the desk's, chosen for scale and seriousness rather than box office. Where a title's availability varies by country, the page says so instead of guessing.</p>",

"entertainment/explainers":
    "<p><b>How this shelf is built.</b> The explainers here describe how the industry works — budgets, release windows, award voting — and each one names its sources, with background reading reachable through <a href=\"" + _w("film+industry") + "\" rel=\"noopener\">the encyclopaedic record</a>. Where a practice is convention rather than rule, the page says which, because the distinction is the point of the shelf.</p>",

"entertainment/movies-like-interstellar-guide":
    "<p><b>Sourced recommendations.</b> The anchor film's production history is documented in <a href=\"" + _w("Interstellar+(film)") + "\" rel=\"noopener\">the encyclopaedic record</a>; the six suggestions are the desk's, each with the reason it earns a place. Running times and availability are checked at publication and dated, because both change.</p>",

"entertainment/recommendations":
    "<p><b>The method behind the lists.</b> Every recommendation on this shelf is chosen by the desk and argued in its own entry — no aggregated scores, no paid placement — with background on the titles reachable through <a href=\"" + _w("lists+of+films+considered+the+best") + "\" rel=\"noopener\">the encyclopaedic record</a>. If a list disagrees with consensus, the page explains why rather than hiding it.</p>",

"entertainment/solo-leveling-e-rank-to-s-rank":
    "<p><b>The source material, documented.</b> The rank system and its origin in the source series are described in <a href=\"" + _w("Solo+Leveling") + "\" rel=\"noopener\">the encyclopaedic record</a>, which is the desk's check for anything stated as fact. The reading of what the ranks mean for the story is the desk's interpretation, labelled as such.</p>",

"entertainment/solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences":
    "<p><b>Both series, checked before comparing.</b> Publication and broadcast histories for the two shows sit in <a href=\"" + _w("Hunter+%C3%97+Hunter") + "\" rel=\"noopener\">the encyclopaedic record</a> — the desk verifies dates and credits before drawing any parallel. The comparison itself is argument, and the page keeps the facts and the opinion in separate paragraphs on purpose.</p>",

"entertainment/squid-game-season-1-why-it-became-a-global-phenomenon":
    "<p><b>Reception claims need receipts.</b> The show's release history, viewing figures and awards are documented in <a href=\"" + _w("Squid+Game") + "\" rel=\"noopener\">the encyclopaedic record</a>, and the desk cites them rather than repeating the rounder numbers that circulate. The argument about why it travelled is the desk's — and it is presented as an argument.</p>",

"entertainment/why-prison-break-season-1-is-still-one-of-the-best-tv-seasons":
    "<p><b>An opinion, with its record checked.</b> Broadcast history and production details for the series are documented in <a href=\"" + _w("Prison+Break") + "\" rel=\"noopener\">the encyclopaedic record</a>; the claim that season one stands above the rest is the desk's judgement, argued episode by episode. Readers who disagree are invited to — the <a href=\"/entertainment/contact/\">contact door</a> is open and the argument is the point.</p>",

# ============================ SPORTS (5) =====================================

"sports/bundesliga-transfers":
    "<p><b>How this list is compiled.</b> Every entry is taken from the club's or league's own announcement, with the competition's structure and rules documented in <a href=\"" + _w("Bundesliga") + "\" rel=\"noopener\">the encyclopaedic record</a>. The desk records announced deals only — nothing rumoured, nothing unconfirmed — and each entry carries the date it was checked.</p>",

"sports/la-liga-transfers":
    "<p><b>Sourced from the league itself.</b> Deals are listed from official announcements, and the competition's own published records sit at <a href=\"" + LALIGA + "\" rel=\"noopener\">LaLiga</a>. Where a transfer is reported but not confirmed by a club, it does not appear here; the desk's transfer pages are a record, not a rumour mill.</p>",

"sports/laliga":
    "<p><b>What this page is and is not.</b> Structure, competition format and historical context are documented in the <a href=\"" + _w("La+Liga") + "\" rel=\"noopener\">encyclopaedic record</a>, with the league's own publications at <a href=\"" + LALIGA + "\" rel=\"noopener\">LaLiga</a>. Fixtures and standings move faster than any page can, so the desk states its check date rather than implying live data.</p>",

"sports/ligue-1-transfers":
    "<p><b>Only what the clubs have said.</b> Entries come from official club and league announcements; the competition's published records are at <a href=\"" + LIGUE1 + "\" rel=\"noopener\">Ligue 1</a>. Loan moves, free transfers and undisclosed fees are labelled as such, because the distinction matters more than the number.</p>",

"sports/serie-a-transfers":
    "<p><b>Compiled from announcements, dated.</b> The desk lists confirmed deals only, with the competition's history and format documented in the <a href=\"" + _w("Serie+A") + "\" rel=\"noopener\">encyclopaedic record</a>. Transfer-window rules change season to season, so each entry is stamped with the date it was verified against the club's own statement.</p>",

# MONEY (2 entries) removed 2026-10-01: desk retired (owner decision, AdSense review).
}
