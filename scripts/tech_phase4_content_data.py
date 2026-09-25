# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 4 (2026-09-25).

Closes the streaming shelf, the thinnest on the desk, from six pieces to twelve.
Same discipline as the earlier batches: evergreen mechanics and decision
guidance, no fabricated benchmarks or volatile statistics, dated official
sources only where a source is genuinely needed, and honest "choose A if /
choose B if" framing. Every internal link points at a page that already exists
on this desk.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE4_GUIDES = [

# ---------------------------------------------------------------- STREAMING (close to 12)
("download-vs-stream-when-each-wins", "streaming", "guide",
"Download vs stream: the decision is your data cap and your Wi-Fi, not the app",
"Streaming trades storage for a steady connection; downloading trades storage for certainty. Pick by whether your bottleneck is bandwidth, a data cap, or a shared network.",
"""<p>Every streaming app offers both a play button and a download button, and most people pick by habit. The honest way to choose is to name your actual bottleneck: is it a monthly data cap, an unreliable connection, a shared network that collapses at peak, or simply a lack of storage on the device? Each bottleneck points to a different answer.</p>
<h2>What streaming actually costs</h2>
<p>Streaming pulls data continuously while you watch, and the rate depends on the quality tier you select - the same ladder worked through in <a href="/tech/streaming-quality-settings/">the streaming quality settings that matter</a>. On an unmetered, steady connection that is the cheapest option in effort: nothing to manage, nothing stored, start instantly. The cost shows up only when the connection is not steady or not unmetered.</p>
<h2>What downloading actually costs</h2>
<p>A download pulls the whole file once, ahead of time, and then playback uses no network at all. That converts an uncertain, continuous demand into a single controlled one. It costs storage on the device and a little planning, and most apps expire downloads after a window or once you start them, so it is a "watch this soon" tool, not an archive. The data you spend is roughly the same as streaming the same title at the same quality - you are not saving bytes by downloading, you are moving when you spend them.</p>
<h2>Choose download if / choose stream if</h2>
<p>Download if you are on a metered connection and can fetch on unmetered hours (many carriers and routers can schedule this), if you are about to be somewhere with no or hostile Wi-Fi - a plane, a commute, a hotel - or if the household network falls over at peak, the same congestion that makes <a href="/tech/why-streams-buffer-at-night/">streams buffer at night</a>. Stream if you are on steady unmetered broadband, if device storage is tight, if you might not finish the title, or if you simply want to start now without waiting for a fetch. The middle case - a big title, a small cap, and no unmetered window - is the one to plan around, because that is where a single stream quietly eats the month's data.</p>""",
[("Netflix — downloads and smart downloads", "https://help.netflix.com/en/node/100624")],
["streaming-quality-settings", "why-streams-buffer-at-night"]),

("why-your-catalogue-differs-by-country", "streaming", "guide",
"Why your streaming catalogue looks nothing like your neighbour's",
"The library you see is set by licensing territory, not by your device, your plan tier, or a setting you can change. Here is what actually decides what appears.",
"""<p>Two people on the same service, same price, same app, can see completely different libraries. This is not a bug, a tier difference, or a setting buried in the app - it is licensing, and once you see the mechanism the surprises stop.</p>
<h2>Rights are sold territory by territory</h2>
<p>A studio does not usually sell a film or show to a streamer for the whole world in one deal. It sells rights territory by territory, often to different buyers, and often for fixed windows. A streamer can only show a title where it holds the rights, so the catalogue is the intersection of "what the service licensed" and "which country your account is billed in." The same contract logic is why a title can arrive on one service and leave another a year later.</p>
<h2>What decides "your" country</h2>
<p>Services infer your territory from your account's billing country and, for some, your connection. That is why travelling can change what you see, and why the country on the account - not the language of the app or the device's region - is usually what matters. It also explains the genuine grey market of region tricks: they are a violation of most terms of service and tend to break playback, payment, and subtitles in ways that are not worth the single title.</p>
<h2>What this means for your decisions</h2>
<p>Three practical reads. First, a service's value is local - judge it by your own catalogue, not by a global marketing list. Second, "leaving soon" carousels are a licensing clock, not a quality judgement; if a title you love is listed there, that is the reason to watch or buy it now. Third, owning a copy (buy or disc) is the only way to be unaffected by a licence expiring, which is the real trade behind the <a href="/tech/cord-cutting-math/">cord-cutting maths</a>: renting access versus owning the thing.</p>""",
[("Netflix — why titles leave", "https://help.netflix.com/en/node/100624")],
["cord-cutting-math"]),

("picture-settings-that-fix-the-soap-opera-look", "streaming", "guide",
"The picture settings that actually change what you see (and the one to turn off first)",
"Motion smoothing is the single biggest reason a film looks like a cheap video. Here is the short settings checklist that fixes it and the few that genuinely help.",
"""<p>Most "the picture looks wrong at home" complaints are not the stream, the cable, or the TV's quality - they are a handful of processing settings that are on by default and tuned for a showroom, not a living room. Fixing them costs nothing and takes two minutes.</p>
<h2>Turn off motion smoothing first</h2>
<p>The "soap opera effect" - where films look like cheap daytime video, oddly smooth and hyper-real - is motion interpolation. The TV invents extra frames between the real ones to raise the frame rate. It helps with sports and pans; it wrecks film, which is meant to be seen at its native 24 frames. Find the setting (each brand names it differently - something with "motion," "flow," or "smoothing") and turn it off for film and TV. This one change does more for how a movie looks than any other.</p>
<h2>Then fix the three that fight the source</h2>
<p>Turn down or off the sharpening/edge-enhancement - the stream already has detail, and added sharpening creates halos and grain. Switch the dynamic contrast and "vivid" energy-saving modes off; they crush darks and blow highlights, which is the opposite of what the <a href="/tech/hdr-formats-the-weakest-link/">HDR chain</a> is trying to do. And pick a colour temperature that reads slightly warm (often "Warm 2" or "Movie/Cinema") rather than the cool blue default - the cool look is a showroom trick, and it makes skin tones wrong.</p>
<h2>Use the right picture mode and let the source lead</h2>
<p>Almost every TV has a "Filmmaker," "Movie," or "Cinema" mode that disables most of the above in one go - start there and adjust brightness to the room. Make sure the HDMI input is in its enhanced/4K mode so HDR and higher frame rates pass through, and let the stream set quality rather than forcing the TV to upscale aggressively. If picture and sound drift apart after all this, that is a separate problem with its own fix order in <a href="/tech/audio-video-sync-drift-fix-order/">audio-video sync drift</a>.</p>""",
[("Rtings — TV learning library (motion interpolation / soap opera effect)", "https://www.rtings.com/tv/learn")],
["hdr-formats-the-weakest-link", "audio-video-sync-drift-fix-order"]),

("offline-streaming-what-actually-works-on-a-plane", "streaming", "guide",
"Offline streaming: what actually plays on a plane, and what silently fails",
"In-flight playback fails for boring, predictable reasons: DRM, expiring downloads, and HDCP. Do this before you board and it just works.",
"""<p>"I downloaded it, why won't it play at 35,000 feet" is one of the most common travel tech failures, and it is almost never the download itself. It is one of a few DRM and device protections that only reveal themselves offline. Knowing them turns a coin-flip into a checklist.</p>
<h2>Download inside the app, on the device you will watch on</h2>
<p>Downloads are encrypted and tied to the app and device that fetched them. A title downloaded on a phone will not appear on a laptop, and a file you copied yourself will not play - the app's own download is the only thing that carries the licence. Fetch it in the app, on the device you intend to watch on, while you still have real internet.</p>
<h2>Respect the expiry window and the "finish once started" clock</h2>
<p>Most services expire a download after a period, and some start a shorter clock (often 48 hours) the moment you press play. For a long trip, download close to departure, not weeks ahead, and avoid "starting" a title you will not finish before the flight. If the app offers a "refresh licence while online" step before boarding, take it.</p>
<h2>Why the second screen and the HDMI port go dark</h2>
<p>Two protections bite offline. HDCP stops protected video from playing over some HDMI connections and external displays, so the app may refuse to output to a monitor or capture device - watch on the built-in screen. And an external or second display that the app cannot verify can simply show black. The reliable setup is the device's own screen, in the app, with the download current.</p>
<h2>Pre-flight checklist</h2>
<p>Download in-app on the watching device shortly before you go; confirm the download shows as available offline (most apps have an offline filter); bring headphones that work with the jack or pair them before boarding; and put the device in aeroplane mode yourself before the crew asks, because some apps re-check the licence on launch and an active-but-captive connection can confuse that. If you will be streaming live instead at the gate, expect delay - covered in <a href="/tech/streaming-quality-settings/">the quality and latency settings</a> and the live-latency piece on this desk.</p>""",
[("Netflix — watch offline with downloads", "https://help.netflix.com/en/node/100624")],
["streaming-quality-settings", "hdr-formats-the-weakest-link"]),

("streaming-subscription-stacking-when-bundle-cheaper", "streaming", "guide",
"Subscription stacking: the honest maths of four services versus one bundle",
"Stacking looks cheap until you count the months you forget to cancel. Here is how to add up real cost, and when a bundle genuinely beats the sum of the parts.",
"""<p>One service feels reasonable. Three feels fine. Six - which is where a lot of households quietly land - is a number most people have never actually written down. The decision is not "is each one worth it" but "is the stack, as a whole, worth what it silently costs," and that is arithmetic, not taste.</p>
<h2>Add up the real monthly number, not the intro price</h2>
<p>Write down every recurring entertainment charge at its current, not promotional, price - the audit method in <a href="/tech/subscription-audit-that-actually-sticks/">a subscription audit that actually sticks</a> does this properly. Then multiply by twelve, because the annual figure is what you are actually committing to. Most people are surprised by the total, and the surprise is the point: stacking is affordable per-line and expensive in aggregate.</p>
<h2>When a bundle genuinely wins</h2>
<p>A bundle is worth it only when you would have paid for most of its parts separately anyway, and the bundle price is below that sum. A bundle that adds two services you would never buy to "save" on one you do is not saving; it is raising the floor. Check what the bundle actually includes against your real list, not against its marketing.</p>
<h2>The bigger lever: rotate instead of stack</h2>
<p>The most effective move for most households is not bundling but serialising - subscribe to one service, watch the thing you wanted, cancel before the next billing date, and rotate to the next. This works because the catalogue you want is a "leaving soon" clock anyway, and because the free-trial traps are avoidable if you calendar the cancel date the moment you sign up, exactly as <a href="/tech/free-trial-cancellation-traps/">free-trial cancellation traps</a> lays out. Stacking is for content you watch continuously; rotating is for content you watch in bursts, which is most of it.</p>
<p>Whichever way you go, the honest test is the same one the whole desk uses for recurring spend: would you buy this again today, knowing the annual total? If the answer for half the stack is no, the maths has already made the decision.</p>""",
[],
["subscription-audit-that-actually-sticks", "free-trial-cancellation-traps"]),

("why-live-streaming-lags-behind", "streaming", "guide",
"Why live streaming is always a few seconds behind (and how to shrink the gap)",
"The delay is not your connection's fault; it is the encode-pack-transcode chain every live stream passes through. Here is where the seconds go and what you can actually do.",
"""<p>Watch a live event on a stream next to someone on broadcast or a radio, and you will hear the goal land seconds apart. That gap is structural, not a malfunction - it is the cost of turning a live camera into internet packets and back into pictures - and knowing where the seconds go tells you how much of it you can claw back.</p>
<h2>Where the seconds go</h2>
<p>A live stream is captured, encoded, chopped into small segments, pushed to servers, repackaged for different connections, and reassembled by your player, which buffers a little before it dares to play. Each step adds latency, and the buffer - the few seconds the player holds in reserve so a hiccup does not stall playback - is usually the single biggest chunk. This is the same buffering trade-off, in its live form, that the on-demand side handles in <a href="/tech/streaming-quality-settings/">the quality and buffer settings</a>.</p>
<h2>What you can actually reduce</h2>
<p>Use a wired connection or strong Wi-Fi, because a player that keeps losing packets grows its buffer to stay smooth - a steady connection lets it run a smaller one. Lower the quality a notch if the connection is marginal; a stable lower-quality stream keeps a shorter buffer than a top-quality one that keeps rebuffering. Close competing traffic on the network, the congestion described in <a href="/tech/why-streams-buffer-at-night/">why streams buffer at night</a>. And if the app offers a "low latency" or "reduce live delay" toggle, turn it on - it trades a little extra stall risk for a shorter buffer.</p>
<h2>What you cannot fix, and why it is fine</h2>
<p>You will not get to true zero: the chain is real and the buffer is the price of not stalling. For watching alone, none of this matters. It only stings when you are syncing with someone else - a watch party across two streams, or a stream against a broadcast. For that, pick one source for everyone, count down together, and accept a few seconds; chasing perfect sync across two different services is the one problem here that has no clean answer.</p>""",
[("HLS / low-latency streaming overview", "https://developer.apple.com/streaming/")],
["streaming-quality-settings", "why-streams-buffer-at-night"]),

]
