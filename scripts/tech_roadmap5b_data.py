# -*- coding: utf-8 -*-
"""Tech roadmap batch T5 (finale, part B) — Email & Files (3) + Remote work (2) + Streaming (2).

Verification receipts (2026-09-10):
- cord-cutting-math [VERIFY pricing gate] — resolved with named, dated sources:
  * CNET six-city averages (Feb 2024): basic cable+internet $144/mo, premium $217/mo.
  * Cord Cutters News (Jun 2026): realistic cable bill $120-150+ vs promo prices $50-80;
    YouTube TV base $82.99/mo (also confirmed by fetv Mar 2026 and CableCompare Jul 2026).
  * CableCompare (Jul 2026): Hulu + Live TV $89.99/mo; 5-6 services + live TV = $165-185/mo,
    comparable to or above cable.
  * Deloitte 2025 Digital Media Trends (via T4-verified briefing): ~4 streaming services,
    ~$69/mo, +13% YoY.
  Piece pins NO single "average cable bill" figure; presents named-source ranges with years,
  flags pricing as volatile (UPDATE-class on republish).
- plain-text-passwords: cites NIST SP 800-63B FAQ (password managers acceptable; minimal
  composition rules) — same source verified live in T1 receipts; no new stats claimed.
- cloud-storage-mistakes: retention windows described qualitatively ("about a month, sometimes
  longer — check your provider's published policy"); no per-provider day counts pinned.
- inbox-zero, remote-work, video-call, streaming-quality: first-hand/protocol pieces; free-tier
  behaviours (Slack hiding older history, meeting-tier limits) described without pinned numbers
  because they change; no sources claimed where nothing external is asserted.
"""

TECH_ROADMAP_T5B = [

    # ------------------------------------------------------------------ #
    # 1. Inbox zero is a myth — a realistic system
    # ------------------------------------------------------------------ #
    (
        "inbox-zero-myth",
        "tools",
        "guide",
        "Email inbox zero is a myth: a realistic system that actually works",
        "Inbox zero as a permanent state is a productivity myth that makes people feel behind. As a daily practice it's the only part worth keeping — here's the system that survives real life.",
        '''<p>Inbox zero began as a reasonable idea — decide something about every message — and curdled into an aesthetic: an empty inbox as a sign of order, held up by people whose job is email in a way nobody else's is. For everyone else, the inbox refills by lunch, and the gap between the aesthetic and reality becomes one more guilt generator. The honest version: <strong>zero is a daily checkpoint, not a permanent state</strong>. The system below takes minutes a day and survives holidays, projects and toddlers.</p>

<h2>The one decision that matters: the inbox is not a to-do list</h2>
<p>Every inbox-zero failure traces to the same root: messages arrive and get left there as reminders of things to handle. But an inbox has no order, no priorities, no due dates — it's the world's worst task manager, and treating it as one means the important items drown under the loud ones. The fix isn't discipline, it's moving the <em>tasks</em> to a real list (any app or notebook) and letting the inbox return to what it is: a delivery entrance. Mail arrives, gets decided, and moves on — the entrance stays clear because nothing lives there.</p>

<h2>The four-way sort</h2>
<p>Every message gets one of four decisions, taken once, in order of speed. <strong>Delete or archive</strong> — the correct answer for most mail; if it might matter someday, search will find it in the archive, which is why folders are optional (see below). <strong>Two-minute replies</strong> — answer now if it takes less than two minutes; the scheduling cost of "later" exceeds the reply. <strong>Convert to task</strong> — if a message needs real work, the work goes on the task list with a date; the message gets archived, because the task references it and search retrieves it. <strong>Delegate or defer</strong> — forward it with a nudge, or use the snooze function, which is the inbox's one genuinely magical feature: the message vanishes and returns exactly when it becomes relevant. A return-Thursday button kills more inbox anxiety than any folder scheme.</p>

<h2>Stop the inflow, not the backlog</h2>
<p>The system fails if two hundred newsletter arrive daily. Unsubscribing is unglamorous and it is <em>the</em> highest-leverage habit in email: every list you leave is a permanent daily deduction. Be ruthless — a newsletter you haven't opened in a month is dead weight, and the guilt-unsubscribe rule is simple: keep what you'd re-subscribe to. This is the attention version of <a href="/tech/subscription-creep/">subscription creep</a> — small recurring costs, individually defensible, collectively the problem — and the same audit instinct from <a href="/tech/subscription-creep-audit/">the subscription audit</a> works on it directly. Notifications go off entirely; email should be a place you visit, not one that taps your shoulder.</p>

<h2>Folders are overrated; search is not</h2>
<p>Elaborate folder hierarchies are the tax people pay for not trusting search. Modern mail search finds a message from a fragment of a name, a phrase, or a month — filing dozens of folders costs minutes daily to save seconds monthly. Keep at most a handful of coarse buckets (finance, travel, receipts — things you genuinely retrieve by category), archive everything else, and lean on search. The archive button deserves to be your most-pressed.</p>

<p><em>The realistic promise: not a permanently empty inbox, but an inbox you process to empty (or near it) once a day in ten-odd minutes, where nothing important can silently rot, and where the inflow is mostly mail you chose. That's the achievable version of the myth — and it's better than the myth, because it survives Tuesday.</em></p>''',
        [],
        [
            ("subscription-creep", "The subscription creep nobody notices"),
            ("subscription-creep-audit", "The full subscription audit"),
            ("remote-work-free-tools", "Free tools that rival paid ones"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 2. Cloud storage mistakes that lose files forever
    # ------------------------------------------------------------------ #
    (
        "cloud-storage-mistakes",
        "safety",
        "guide",
        "Cloud storage mistakes that lead to losing files 'forever'",
        "The cloud is not a backup — and the ways people discover that are all avoidable. Sync propagation, deletion windows, shared-folder revocation and single-account risk, explained.",
        '''<p>"It was in the cloud" is the most heartbreaking phrase in data loss, because the speaker did try to be careful — they just trusted a system that does something subtly different from what they assumed. Cloud storage is excellent. The mistakes are in what people believe it does. All of them are avoidable in minutes.</p>

<h2>Mistake one: believing sync is backup</h2>
<p>The core confusion. Sync services keep every device's copy matching; backup keeps a second, independent copy. The difference is what happens on <strong>deletion</strong>: delete a synced file — accidentally, or via ransomware that quietly scrambles everything it can reach — and the deletion itself <em>syncs</em>, propagating to every device and sometimes to the cloud copy too. A perfectly synced system can be perfectly synced at zero files. This isn't hypothetical; it's the mechanism behind most "the cloud ate my thesis" stories, and it's why <a href="/tech/cloud-vs-local-backup/">cloud storage and backup are both, not either</a> — and why the oldest rule in the field still stands: <a href="/tech/three-two-one-backup-rule/">three copies, two media, one off-site</a>.</p>

<h2>Mistake two: assuming deleted means recoverable forever</h2>
<p>Every major service keeps deleted files for a grace period — often about a month, sometimes longer, sometimes shorter on older plans — and keeps version history for edited files on some tiers. The mistake is treating "some window exists" as "recovery is guaranteed": the windows are published policies that vary by service and plan, they expire silently, and past them the file is genuinely gone. Spend five minutes on your provider's help page today: how long are deletions kept, how far back do versions go on <em>your</em> plan. Knowing the answer before you need it is the difference between an inconvenient undo and a funeral.</p>

<h2>Mistake three: shared folders that outlive the team</h2>
<p>Shared folders have an asymmetry almost nobody thinks through: files <em>you</em> added to a folder someone else owns may leave with you when you leave the org, the plan, or the partnership — while files in folders <em>you</em> own can silently keep consuming your quota years after the collaboration ended. The losing-file variant: contributing years of work into someone else's folder, then departing. The audit: list folders you own (revoke ex-collaborators), list folders you're in that others own (copy out anything whose loss would sting), and check what happens to shared links when a plan lapses.</p>

<h2>Mistake four: one account, one key, one point of failure</h2>
<p>Your cloud account is a single lock on every file you've delegated to it. Account takeover — a phished password, a reused password from someone else's breach (<a href="/tech/reusing-passwords-risk/">the math on reuse is ugly</a>) — can mean the attacker deletes everything precisely <em>because</em> there's no offline copy to fall back to. Two moves close most of the gap: proper two-factor authentication (<a href="/tech/two-factor-authentication-setup/">the setup that stops the common attacks</a>), and remembering that the account holds the only copy — which loops back to mistake one. And if you've ever lost the recovery path to an account, <a href="/tech/how-to-reset-forgotten-passwords/">the reset options are worth knowing before the lockout</a>.</p>

<p><em>Cloud storage is genuinely one of the best tools of the last two decades — the failures in this piece are all belief failures, not technology failures. Sync is a convenience; backup is insurance; and the people who never lose files are simply the ones who never confused the two.</em></p>''',
        [],
        [
            ("cloud-vs-local-backup", "Cloud storage vs local backup"),
            ("three-two-one-backup-rule", "The 3-2-1 backup rule"),
            ("phone-died-no-backup", "Phone died with no backup"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 3. Plain-text passwords
    # ------------------------------------------------------------------ #
    (
        "plain-text-passwords",
        "safety",
        "guide",
        "Why you should never store passwords in a plain text file or notes app",
        "It feels safer than trusting a password manager. It's actually the same single-point-of-failure risk with none of the engineering — and one sync away from every device you own.",
        '''<p>The reasoning is always sympathetic: password managers feel like a black box, and "at least a text file is mine" feels like control. Some people graduate to a note in the default notes app, which feels like a step up — it syncs, it's searchable, it's got a lock icon maybe. This piece is the honest case for why that file is the worst of both worlds: all of the single-point-of-failure risk of a password manager, none of the engineering that manages it away.</p>

<h2>The failure mode, stated precisely</h2>
<p>A passwords-in-a-notes-file setup has one property that matters: <strong>everything, readable, in one place, replicated</strong>. The note syncs to a cloud account — so it exists on every device signed into that account, on the provider's servers, and in that provider's own backups. Anyone with access to any one of those — a borrowed phone, a shared family plan, a phished account, a compromised device — holds every credential you own, with no second factor between them and the file. The lock icon on a note, where present, is a speed bump, not a safe: it protects against a casual glance, not against account access.</p>
<p>Compare the threat model of the file against the threat model of <em>not</em> storing anything: a person with no list must remember, and memory pushes people toward <a href="/tech/reusing-passwords-risk/">reusing the same password everywhere</a> — the single most exploited habit in account takeover. The file usually begins as a cure for reuse and ends as its own catastrophe. Both failure modes live at the same address: convenience without engineering.</p>

<h2>"But a manager is also one basket"</h2>
<p>The standard objection deserves a straight answer, because it's half right: yes, a password manager is also a single point of failure. The difference is what surrounds the failure. A reputable manager is built for exactly this job — strong encryption where the data is unreadable without your master password, no plaintext copies on servers, and your master password as the only key. The people who built it anticipated the attacks; the notes app wasn't built for this job at all. And the security establishment treats the two as opposites: NIST's digital-identity guidance (SP 800-63B) — the same standard that killed security questions — is built around password managers being the <em>recommended</em> way to hold credentials, not a risk to avoid. The basket isn't the problem; an unbasketed basket is.</p>

<h2>The migration, in one sitting</h2>
<p>Move today, in under an hour. Choose a reputable manager — the free tiers are genuinely sufficient for most people, as <a href="/tech/bitwarden-free-password-manager/">the Bitwarden free-plan review</a> and <a href="/tech/password-manager-or-browser/">the manager-versus-browser comparison</a> cover in detail. Install it, set a master password you'll actually remember (long, memorable, unique — this one password is the only one you'll ever type). Import the list: every manager accepts imported entries, so the text file's contents paste straight in. Then <strong>delete the file everywhere it synced</strong> — every device, the trash, the version history if the app keeps one — and change the two or three most important passwords first (email, banking, primary social) so the list that ever existed in plaintext is retired fastest where it hurts most.</p>

<p><em>The text file felt safe because it was simple. Simple and safe are different properties — and for secrets, safety comes from engineering you don't have to do yourself. One hour of migration retires the most dangerous file on your devices.</em></p>''',
        [
            ("NIST SP 800-63B FAQ — digital identity guidelines (password managers recommended; the same standard cited for security questions)", "https://pages.nist.gov/800-63-FAQ/"),
        ],
        [
            ("password-manager-or-browser", "Password manager or browser?"),
            ("bitwarden-free-password-manager", "Bitwarden free plan, reviewed"),
            ("reusing-passwords-risk", "The real cost of password reuse"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 4. Free remote work tools that rival paid ones
    # ------------------------------------------------------------------ #
    (
        "remote-work-free-tools",
        "tools",
        "guide",
        "Free tools for remote work that rival paid ones",
        "The remote stack used to be the expensive part of a job. In 2026 the free tier of almost every category is genuinely good — if you know where the free tiers actually end.",
        '''<p>Remote work software had a golden paradox: the tools got excellent while the free tiers got generous, and most people still pay out of habit or office tradition. The honest map below is by category — what the free tier covers, where it genuinely ends, and when paying is actually worth it. The through-line: for individuals and small teams, free now rivals paid; the paid versions mostly earn their price on administration, compliance and scale, not on the core experience.</p>

<h2>Writing and documents</h2>
<p>This is the most settled category: the free tiers here are not consolation prizes. Google Docs is a complete collaborative word processor — comments, suggestions, version history, real-time co-editing — free, and the choice between the big three is about workflow, not money: <a href="/tech/google-docs-vs-word-vs-notion/">the Docs-versus-Word-versus-Notion breakdown</a>. Notion's free plan is generous enough that individuals rarely outgrow it, as <a href="/tech/notion-free-plan/">its honest free-plan review</a> covers. If a job needs a paid office suite, it needs it for formats and compliance, not capability.</p>

<h2>Tasks and projects</h2>
<p>Kanban boards became commodity years ago — the free tiers of the major boards (Trello, Notion, GitHub Projects for technical teams) cover personal and small-team use with the real limits landing on automation counts, views and admin controls rather than the core experience. The honest gap at free: cross-team reporting, dependencies at scale, permissioning. A freelancer or a five-person team hits none of those walls for years.</p>

<h2>Meetings and calls</h2>
<p>Free meeting tiers cover the actual daily work — video, screen share, recording on some tiers — with the usual free-tier ceilings on group-call duration and extras that change often enough that this piece won't pin numbers; check the current limits before committing to a platform. What matters more than the platform: being <a href="/tech/video-call-mistakes/">good at the call itself</a> — lighting, sound and camera discipline beat any software upgrade on the market.</p>

<h2>Chat and async communication</h2>
<p>Slack's free tier is fully usable with one behavioural caveat that shapes everything: on the free plan, older message history eventually becomes hidden, which means free Slack works only for teams whose decisions also live somewhere durable. Treat that not as a flaw but as architecture — decisions go in docs (free), chat stays ephemeral. The same behavioural lens applies to every "free vs paid" chat choice: the question is never "does it work" but "what does the free tier make your team forget".</p>

<h2>The rest of the stack, quickly</h2>
<p><strong>Whiteboarding:</strong> Excalidraw is free, open-source and the fastest shared sketch tool going. <strong>File sync:</strong> free storage tiers from the major clouds cover documents easily, though the sync-is-not-backup caveat in <a href="/tech/cloud-storage-mistakes/">the cloud-storage mistakes piece</a> applies to every one of them. <strong>Software generally:</strong> the free canon keeps expanding — <a href="/tech/free-software-alternatives/">the reviewed free alternatives piece</a> maps which paid categories have genuinely free escapes. <strong>Time zones:</strong> every calendar app does this now; nobody needs a tool for it.</p>

<h2>When paying is genuinely worth it</h2>
<p>Three cases survive honest scrutiny. <strong>Admin and compliance</strong> — central billing, user provisioning, audit logs: real products, priced for companies, irrelevant to individuals. <strong>Scale ceilings</strong> — when the team outgrows free-tier structure (history, storage, seats), paying beats contorting. <strong>Time</strong> — if a paid tool's automation saves an hour a month, the subscription has already paid for itself; otherwise the <a href="/tech/subscription-creep-audit/">subscription audit</a> applies to work software too.</p>

<p><em>The 2026 reality: the free remote stack is not a compromise — it's what the paid stack was five years ago. Spend the evaluation time on where each free tier ends, and pay only when you actually meet the wall.</em></p>''',
        [],
        [
            ("google-docs-vs-word-vs-notion", "Docs vs Word vs Notion"),
            ("notion-free-plan", "Notion free plan, honestly"),
            ("video-call-mistakes", "Video call mistakes"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 5. Video call mistakes
    # ------------------------------------------------------------------ #
    (
        "video-call-mistakes",
        "tools",
        "guide",
        "Video call mistakes that make you look unprepared (and the 10-minute fix)",
        "Nobody remembers what software the meeting used. Everyone remembers the ceiling cam, the echo and the silhouette against a window. Ten minutes of setup fixes all of it, permanently.",
        '''<p>Video calls flattened one advantage the polished had in physical rooms: preparation used to mean a commute. Now it means ten minutes of setup — and most people still skip it, which makes it the cheapest professional edge available. Every fix below is free and permanent. The theme throughout: your equipment is already fine; the arrangement is what's broken.</p>

<h2>Lighting: the single biggest upgrade</h2>
<p>The classic mistake is sitting with a window <em>behind</em> you — the camera exposes for the bright background and renders you as a silhouette with a name label. The fix costs nothing: <strong>face the light</strong>. Sit so a window is in front of you, slightly off to one side; if the room's windowless, put a lamp behind the laptop, pointing at your face, and turn off the overhead alone-in-a-lift light. One light source in front, none strong behind — that's the entire discipline, and it changes how you look more than any camera purchase could.</p>

<h2>Camera height and the eyeline lie</h2>
<p>Laptop-on-the-desk means the camera is below your chin, shooting up your nostrils at a ceiling-corner angle that reads as unprepared even when you aren't. Stack books or a box under it so the <strong>lens sits at eye level</strong> — the difference between "gaming streamer" and "colleague" is three textbooks of altitude. Then the awkward one: when speaking, look at the <strong>lens</strong>, not at the faces. It feels unnatural because every instinct points at the people; but on their screen, lens-eye-contact is exactly what looking-at-them looks like. Use it for your key moments — openings, asks, closings — and glance at faces the rest of the time.</p>

<h2>Sound beats camera, always</h2>
<p>Viewers forgive mediocre video; they endure bad audio only while planning their exit. In order of what actually helps: <strong>proximity</strong> — being close to any microphone beats owning an expensive one far away; <strong>headphones</strong> — any wired earbuds kill the echo problem instantly, because echo is your speakers' sound re-entering your mic, and headphones remove the source; <strong>the room</strong> — soft furnishings absorb, empty rooms with hard walls bounce, so a bedroom beats a kitchen. The professional trick nobody mentions: mute is a courtesy you extend to others, and a discipline you owe yourself — unmute-then-speak beats live-keyboard-noise every call.</p>

<h2>Background, frame and the etiquette layer</h2>
<p>The background question has a simple answer: a real, slightly-tidy space reads as more trustworthy than any virtual replacement — virtual backgrounds shimmer at the edges and steal attention, which is the one thing you can't afford. Frame yourself with a little headroom and your eyes roughly on the top-third line. Before any high-stakes call, do the ten-second dry run: open the call app's own preview, check what's <em>in frame</em> (laundry counts), check the light, check the mic. And the connection rule that outperforms every other fix on bad days: distance from the router is distance from quality — the physics is in <a href="/tech/wi-fi-router-placement/">the router placement piece</a>, and it applies to your call quality directly.</p>

<h2>The mistakes that are pure habit</h2>
<p>Joining exactly on the minute (join two early; the small talk before the call is where reputations are quietly built). Talking over the lag (calls have latency; count to one before responding — the pause reads as thoughtful, not slow). Sharing the wrong window (close everything you'd hate to share <em>before</em> the call, not during the scramble). And the classic: reading your own face in the self-view the entire call — hide it in the settings; you'll suddenly appear twice as engaged.</p>

<p><em>Ten minutes, once: light in front, lens at eye level, earbuds in, background real, notifications off, self-view hidden. Every call after that runs on the dividend.</em></p>''',
        [],
        [
            ("wi-fi-router-placement", "Router placement mistakes"),
            ("remote-work-free-tools", "Free remote work stack"),
            ("bluetooth-not-pairing", "Bluetooth won't pair?"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 6. Cord-cutting math [VERIFY pricing — resolved, see file header]
    # ------------------------------------------------------------------ #
    (
        "cord-cutting-math",
        "streaming",
        "guide",
        "Cord-cutting math: when streaming actually costs more than cable",
        "Cutting the cord saved everyone money in 2015. In 2026 the honest math says: light viewers still win big — and live-TV replacements with a stacked bundle can quietly cost as much as, or more than, the cable bill they replaced.",
        '''<p>Cord-cutting began as arithmetic: cable cost a small fortune, one or two streaming services cost pocket change, cancel the former and keep watching. A decade later the streaming industry has reassembled everything people fled — price hikes, bundles, ads — and the honest answer to "does cutting the cord still save money" is: <strong>it depends entirely on what you watch, and the worst case loses to cable.</strong> Here's the math, with sources, so you can run your own numbers.</p>

<h2>What cable actually costs</h2>
<p>Cable pricing is a two-tier system: the advertised promo and the bill you actually pay. CNET's six-city US comparison put basic cable-plus-internet at an average of about <strong>$144 a month</strong> and premium packages around <strong>$217</strong> (2024 figures, excluding taxes and fees). 2026 guides describe the same gap live: advertised packages from roughly $50–80 with realistic bills of <strong>$120–150+ once equipment rentals and mandatory surcharges land</strong> (Cord Cutters News, June 2026). Treat "the promo price" as marketing everywhere in this piece — it's the number the industry leads with on both sides of the fence.</p>

<h2>What streaming costs — by viewer type</h2>
<p><strong>The light viewer wins big.</strong> One or two on-demand services plus an antenna is the setup cord-cutting was invented for: CNET's comparison put a basic four-service with-ads streaming stack at about <strong>$33 a month</strong> before internet (2024). Deloitte's 2025 Digital Media Trends survey found US households averaging about four services at roughly <strong>$69 a month</strong> — already up 13% year over year, which is its own warning. Against a realistic $144–157 cable bill, a modest stack saves real money, on the order of $60–90 a month.</p>
<p><strong>The live-TV replacement breaks even.</strong> Sports, news and local channels are what keep people paying cable, and the streaming substitutes for them have climbed to cable prices: <strong>YouTube TV's base plan is $82.99 a month</strong> and Hulu + Live TV runs <strong>$89.99</strong> (both confirmed across 2026 comparisons by Cord Cutters News and CableCompare). Add the internet connection you still need, and a live-TV streamer lands within a few notes of the cable bundle it replaced — CNET's table had YouTube TV's total within a dollar or two of average cable.</p>
<p><strong>The super-stack loses.</strong> Here's the case the title promises: a household keeping five or six on-demand services <em>plus</em> a live-TV service spends roughly <strong>$165–185 a month</strong> — comparable to, or above, the cable bundle it left (CableCompare, July 2026). Fragmentation did this: the shows you want now live across more services, each with its own price that only ratchets upward — the same quiet accumulation documented in <a href="/tech/subscription-creep/">the subscription-creep piece</a>, wearing a different logo.</p>

<h2>The four honest rules of the math</h2>
<p><strong>One: internet is paid either way</strong> — so compare TV-portion to TV-portion, or the whole exercise flatters whichever answer you wanted. <strong>Two: count what you keep, not what you can get</strong> — the stack's price only counts services you'd genuinely miss; the audit from <a href="/tech/subscription-creep-audit/">the subscription audit</a> decides which those are. <strong>Three: rotate instead of stack</strong> — subscribing to one service at a time, watching its show, cancelling, moving on, converts a $100+ stack into $15–25 a month; the catalogues barely notice. <strong>Four: free and legal exists</strong> — free ad-supported services, library apps and an antenna cover more than people assume, and every paid trial should enter your calendar the day it starts (<a href="/tech/free-trial-traps/">the trial-trap defence</a> applies double when there are six services).</p>

<p><em>Pricing here was checked September 2026 and will be stale within a year — the industry reprices constantly, which is precisely point four. The structure of the math, though, barely moves: cut the cord for two services and an antenna and you'll save; rebuild cable out of streaming subscriptions and you'll pay cable prices plus the inconvenience.</em></p>''',
        [
            ("CNET — Streaming vs cable six-city cost comparison (Feb 2024; $144 basic / $217 premium averages)", "https://www.cnet.com/tech/home-entertainment/streaming-services-vs-cable-battle-budget-which-one-saves-you-more-money/"),
            ("Cord Cutters News — YouTube TV vs cable, realistic monthly bills (Jun 2026; YouTube TV $82.99, cable $120-150+)", "https://cordcuttersnews.com/youtube-tv-vs-cable-tv-can-youtube-tv-really-save-you-money/"),
            ("CableCompare — Why cord-cutters are returning to cable (Jul 2026; Hulu+Live $89.99, super-stack $165-185)", "https://www.cablecompare.com/blog/cord-cutters-return-cable-satellite-tv-subscriptions"),
            ("Deloitte 2025 Digital Media Trends summary (4 streaming services, ~$69/mo, +13% YoY)", "https://visionarynetwork.co.uk/2026/04/06/subscription-spending-household-budgets-and-consumer-behaviour/"),
        ],
        [
            ("subscription-creep", "The subscription creep nobody notices"),
            ("streaming-quality-settings", "Streaming quality settings"),
            ("free-trial-traps", "Free trial traps"),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 7. Streaming quality settings
    # ------------------------------------------------------------------ #
    (
        "streaming-quality-settings",
        "streaming",
        "guide",
        "Streaming quality settings most people get wrong",
        "Soft picture, sudden drops to mush, data bills at the end of the month — almost all of it traces to one setting nobody opened and one knob nobody knew existed.",
        '''<p>When a stream looks wrong, the instinct is to blame the internet plan or the television. It's almost never either. Streaming apps ship on auto-pilot — an algorithm silently decides your picture quality moment to moment, weighing your connection, their server costs and your data budget in ways that suit the service. Understanding that one fact explains most quality complaints, and the fixes are all settings you can change in a minute.</p>

<h2>Why the picture quietly drops: adaptive bitrate</h2>
<p>Streaming isn't one quality — it's a ladder of qualities, and the player climbs up and down it in real time based on your connection speed. That's why the film starts crisp, turns soft during the family's evening crunch (everyone's on the network at 8pm), and sharpens again at midnight. The mechanism is called adaptive bitrate, and it's why "my internet is bad" is often wrong: the internet is fine, but at that hour it's <em>contested</em> — someone's gaming, someone's on a call, three devices are updating. The fix is scheduling or contention-triage, not a faster plan you may not need.</p>

<h2>The settings that are actually yours</h2>
<p><strong>Per-service quality lock:</strong> inside each major app's playback settings there's a quality selector — auto, and then named tiers. Setting it to a fixed tier stops the silent downgrades, at the cost of buffering when the connection dips; a stable medium tier often beats an auto setting that's eternally cautious. <strong>Data saver:</strong> the same selector on mobile — data-saver modes cut usage dramatically and are the difference between streaming on a mobile plan and regretting it; on phone screens the quality cost is smaller than you fear. <strong>Downloads:</strong> over cellular, downloading on Wi-Fi first is the highest-quality, zero-data-risk option the app offers, and almost nobody uses it.</p>

<h2>The checks before you blame the app</h2>
<p>When the picture looks persistently soft, work this order: <strong>one — the in-app quality setting</strong> (it may be pinned low from a hotel trip years ago). <strong>two — the source</strong>: some content is old or broadcast at modest quality and no setting rescues it; compare the same scene across two shows. <strong>three — the TV's picture processing</strong>: the most common "why does everything look weird" culprit is <em>motion smoothing</em> (soap-opera effect), a TV feature that makes 24-frame film look like a daytime soap — it lives in the TV's picture settings under names like "motionflow" or "trumotion", and turning it off restores the film look instantly. <strong>four — the HDMI cable and port</strong> on external devices: a stale cable quietly caps the signal, the same port-ceiling trap as <a href="/tech/monitor-buying-specs/">monitor buying</a>.</p>

<h2>Data: the invisible cost of "max quality"</h2>
<p>Resolution settings are really data settings. Streaming at the top tier moves far more data per hour than most households track — roughly speaking, an hour at standard definition is a fraction of a gigabyte while top-tier 4K can run to several gigabytes, and exact figures vary by service, so check the provider's own data-usage help page rather than trusting a forum. Two practical consequences: capped or metered connections should pin quality deliberately rather than letting "auto" climb to 4K; and households that hit data caps while "nobody changed anything" usually have a 4K default plus a new TV doing the changing. If cost is the concern, the bigger lever is still the count of services — <a href="/tech/cord-cutting-math/">the cord-cutting math</a> covers why stacking is the expensive part, and rotation beats resolution-tinkering every time (<a href="/tech/subscription-creep/">same audit mindset</a>).</p>

<p><em>Quality issues resolve in this order: the app's own setting, the household's contention, the TV's processing, the plan. Ninety percent of "our streaming looks bad" is the first two — and both are free to fix tonight.</em></p>''',
        [],
        [
            ("cord-cutting-math", "The cord-cutting math"),
            ("subscription-creep", "The subscription creep nobody notices"),
            ("monitor-buying-specs", "Monitor specs, explained simply"),
        ],
    ),
]
