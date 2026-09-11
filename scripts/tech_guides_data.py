"""BRYME Tech — batch 2 original guides (Sept 2026). Plain HTML bodies, house voice."""

NEW_TECH_GUIDES = [

# ============================================================ SAFETY
("how-to-spot-a-suspicious-link", "safety", "guide",
"How to spot a suspicious link before you tap it",
"The checklist that catches most phishing links in ten seconds — and what to do if you already tapped.",
"""<p>Phishing links do not look dangerous — that is the entire point. They look like your bank, your delivery company, your boss. What gives them away is not the words around them but the address itself, and ten seconds of checking catches most of them.</p>
<h2>The ten-second check</h2>
<p>On a computer, rest your pointer on the link and read the address that appears at the corner of the browser — the real destination, not the underlined words. On a phone, press and hold the link until a preview pops up. Then read the domain from right to left: the part immediately before the first single slash is the only part that matters. <b>secure.bryme.example.com</b> belongs to example.com. <b>bryme.example.secure-login.ru</b> does not belong to anyone you trust.</p>
<h2>The patterns that repeat</h2>
<p>Lookalike spellings — rn for m, 0 for o, a dot slipped into a famous name. Rushed domains — a real bank does not register netflix-billing-alert.xyz this morning. Emotion before thought — the message needs you to act now, worry later; urgent language is the product. And the wrong channel: your parcel company does not text you a payment link for a fee you never owed.</p>
<h2>Shorteners and buttons</h2>
<p>A shortened link (bit.ly and friends) hides its destination by design. That is legitimate in a presentation and suspicious in a payment text. Do not visit to find out — most shortener sites offer a preview mode by adding a plus sign to the address, and messaging apps increasingly show destination previews on long-press.</p>
<h2>If you already tapped</h2>
<p>Tapping alone rarely causes harm; the damage starts when you type. If you entered a password on a fake page, change it on the real site now, and anywhere you reused it — which is exactly why the <a href="/tech/password-manager-or-browser/">password-manager habit</a> matters. If you entered card details, call the bank. If nothing was typed, close the page and move on; drive-by phone attacks at consumer scale are rare and target specific flaws, but keep the phone updated anyway.</p>
<h2>The habit that beats the checklist</h2>
<p>Go to sites, do not arrive at them. For anything involving money or logins, open the app or type the address yourself — the message can be a notification, never the front door. For assistants that summarise or rewrite text, our <a href="/tech/ai-assistant-data-training-settings/">data-training settings guide</a> covers a different leak: what your pasted text teaches the model.</p>""",
[("FTC — How to recognize and avoid phishing scams", "https://consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams")],
[("two-factor-authentication-setup", "2FA done right"),
 ("public-wifi-risks", "The honest public Wi-Fi guide"),
 ("bitwarden-free-password-manager", "Bitwarden's free plan, checked")]),

("two-factor-authentication-setup", "safety", "guide",
"Two-factor authentication, done right",
"Why 2FA beats any password, the three ways to get it (SMS, app, passkey) ranked honestly, and the backup codes that save you.",
"""<p>Two-factor authentication means a login needs something you know (your password) and something you have (your phone, an app, a security key). Its value is blunt: a stolen password alone stops working. Accounts with 2FA are dramatically harder to take over — which is why every serious security body pushes it, and why enabling it on your email first matters more than anywhere else, because email is the reset door to everything else.</p>
<h2>The three ways, ranked honestly</h2>
<p><b>SMS codes</b> are the weakest but still worthwhile — better than nothing, vulnerable to SIM-swap attacks where a fraudster moves your number to their SIM. <b>Authenticator apps</b> (Google Authenticator, Authy, Aegis and similar) generate codes on the device itself; no network, nothing to intercept — the sensible default. <b>Passkeys</b> are the newest: a cryptographic key stored on your device, unlocked with fingerprint or PIN, with nothing typeable to phish. Where a service offers passkeys, they are the best option for most people.</p>
<h2>Set it up in five minutes</h2>
<p>Go to the account's security settings — look for "two-step verification", "2FA" or "security". Choose an authenticator app, scan the QR code it shows, and type back the six-digit code to prove the pairing worked. Do this for email first, then banking, then social.</p>
<h2>The step everyone skips</h2>
<p>The service will show you backup codes — a list of one-time codes for when your phone is lost, dead or reset. Save them somewhere that is not the phone doing the authenticating: printed, or in the <a href="/tech/bitwarden-free-password-manager/">password manager</a> itself. Skipping this is how people lock themselves out, and lockouts teach the wrong lesson.</p>
<h2>What 2FA does not fix</h2>
<p>It protects logins, not judgement. A payment you authorise yourself, or a conversation you paste into a tool — see <a href="/tech/ai-assistant-data-training-settings/">what assistants do with your data</a> — is outside its reach. And if a service offers to send a login link by email instead, that is fine too: possession of your inbox is the factor.</p>
<h2>The ten-minute shortlist</h2>
<p>Email, bank, password manager, primary social, cloud storage. Five accounts tonight beats a perfect plan for next month.</p>""",
[("CISA — Turn on MFA", "https://www.cisa.gov/secure-our-world/turn-mfa")],
[("how-to-spot-a-suspicious-link", "Spotting suspicious links"),
 ("bitwarden-free-password-manager", "Bitwarden's free plan, checked"),
 ("ai-assistant-data-training-settings", "What assistants do with your data")]),

("public-wifi-risks", "safety", "guide",
"Public Wi-Fi: the honest risks (they are not the ones you were told)",
"Modern encryption fixed most of the coffee-shop threat. What actually remains: fake hotspots, captive portals and your own habits.",
"""<p>Old security advice treats every airport network as a sniper's nest where anyone reads your traffic. That advice is a decade out of date, and knowing why makes you both calmer and correctly paranoid about the threats that remain.</p>
<h2>What changed</h2>
<p>Most of the web now encrypts the connection itself — the padlock in the address bar means the coffee shop, the network and anyone on it see that you talked to your bank, not what was said. HTTPS arrived near-universally, so the classic "sniffing passwords from the air" attack mostly died with it. If a site would accept a password over plain unencrypted HTTP today, the site is the emergency, not the Wi-Fi.</p>
<h2>The three real risks</h2>
<p><b>The evil twin:</b> a hotspot named "Airport_Free_WiFi" that is actually someone's laptop collecting whatever you send before encryption, or simply positioned to phish a login portal. <b>The fake captive portal:</b> the "sign in to continue" page that asks for an email and password — real portals almost never need a password, only an email or room number. <b>You:</b> shoulder-surfing in a crowded terminal, and the habit of doing banking where a camera over your shoulder works harder than any hacker.</p>
<h2>What actually helps</h2>
<p>Prefer a phone's personal hotspot when you have one — you control that network. Verify the exact network name with staff, not with the strongest signal. If a portal demands a password a real portal would not want, walk away. Keep the device updated; browser and OS updates patch the genuine drive-by flaws. A VPN adds a tunnel for unencrypted traffic and hides your activity from the network — honest but narrow: it protects you from the café, not from the VPN company, and it does not make a fake login page real.</p>
<h2>The one-line version</h2>
<p>Encryption made public Wi-Fi mostly fine; humans remain the exploit. The same judgement applies to messages — see <a href="/tech/how-to-spot-a-suspicious-link/">how to read a link before tapping it</a>, and for messaging privacy specifically, our <a href="/tech/signal-vs-whatsapp/">Signal and WhatsApp comparison</a> covers what each app encrypts and what metadata stays.</p>""",
[],
[("how-to-spot-a-suspicious-link", "Spotting suspicious links"),
 ("signal-vs-whatsapp", "Signal vs WhatsApp, honestly"),
 ("two-factor-authentication-setup", "2FA done right")]),

("password-manager-or-browser", "safety", "guide",
"Password manager or browser? An honest comparison",
"Chrome, Safari and Edge save passwords well now. Here is what a dedicated manager still does better — and when the browser is genuinely enough.",
"""<p>The honest headline: built-in browser password saving got good. Chrome, Safari, Edge and Firefox now generate strong passwords, sync them across your devices and warn about breaches. For many people, that is already a vast upgrade over reusing one password — and it is fine to start there tonight.</p>
<h2>What a dedicated manager still does better</h2>
<p><b>It is not chained to one browser.</b> Browser vaults work best inside their own browser; switch from Chrome to Safari on a whim and your vault does not follow. A dedicated manager — Bitwarden, 1Password, Proton Pass and similar — fills any app on any platform from one encrypted vault. <b>It holds more than logins:</b> secure notes, Wi-Fi passwords, bank card details, identity fields for forms. <b>It passes the household test:</b> proper sharing of a handful of logins with a partner or family, without texting passwords. <b>It survives the browser's own account:</b> your Chrome vault is only as safe as the Google password protecting it — which is exactly why that account deserves <a href="/tech/two-factor-authentication-setup/">two-factor authentication</a>.</p>
<h2>What the browser does better</h2>
<p>Zero setup, zero new habits, passkeys built in, and it is already watching for breached passwords. If the alternative is "nothing", the browser wins. The comparison only matters once you are ready for the extra it provides — our <a href="/tech/bitwarden-free-password-manager/">Bitwarden free-plan review</a> checked what the best-known free manager includes across unlimited devices.</p>
<h2>The honest recommendation</h2>
<p>Start with the browser vault today; it takes two minutes. Graduate to a dedicated manager when you feel the friction: a second browser, a phone app that needs logins, a family asking for the Wi-Fi password again. Move the bank and email first, then let the rest migrate as you log in to things.</p>
<h2>Whichever you pick</h2>
<p>The vault is only as strong as its front door: a long unique master password, 2FA on the account, and the backup codes stored somewhere that is not the phone doing the approving.</p>""",
[],
[("bitwarden-free-password-manager", "Bitwarden's free plan, checked"),
 ("two-factor-authentication-setup", "2FA done right"),
 ("how-to-spot-a-suspicious-link", "Spotting suspicious links")]),

# ============================================================ ANDROID
("free-up-storage-android", "android", "guide",
"Free up storage on Android without deleting your life",
"The order that works: what to check first, what apps quietly hoard, and the difference between clearing cache and clearing data.",
"""<p>"Storage almost full" on Android is rarely about how much you have and usually about five specific hoarders. Clear them in this order and most phones recover gigabytes without losing a single photo.</p>
<h2>1. See where it actually went</h2>
<p>Settings → Storage (your maker may file it under "Battery and device care"). The breakdown matters: photos, apps, "other" or "system". Guessing skips the step that pays.</p>
<h2>2. Files by Google does the boring work</h2>
<p>Google's free <b>Files</b> app has a Clean tab that finds duplicates, memes, old screenshots and large files with previews, so you delete in batches with your eyes open. On many phones it is preinstalled; otherwise it is a small official install from the Play Store.</p>
<h2>3. The messaging-app mountain</h2>
<p>On phones used for family groups, WhatsApp and its cousins are usually the largest app in the list. Inside the app's own storage settings you can review and delete large files, forwards and long-forgotten videos — chat text stays, media goes. This single sweep often beats everything else combined.</p>
<h2>4. Cache: helpful, and often misunderstood</h2>
<p>Apps cache images and files to feel fast. Clearing an app's cache (Settings → Apps → [app] → Storage → Clear cache) frees space safely — the app re-downloads what it needs. <b>Clear data</b> is the neighbouring button that signs you out and resets the app; that is the one that deletes your preferences, not the cache.</p>
<h2>5. Photos without loss</h2>
<p>Back up to Google Photos (15 GB free) or your maker's cloud, then use the app's "free up space" action, which removes on-device copies that are already safely uploaded. Check the backup badge before trusting it.</p>
<h2>6. When it is genuinely full</h2>
<p>Android needs some free space to function; below a few percent everything from the camera to messaging starts misbehaving. If the hoarders are cleared and you are still packed, a microSD slot (if your phone has one) moves photos and media across cheaply — apps generally cannot live there on modern Android. And if the phone itself is old and small, our <a href="/tech/android-battery-health/">battery-health guide</a> will help you decide whether it is also time for hardware.</p>""",
[("Android Help — Free up space", "https://support.google.com/android/answer/7431795")],
[("android-app-permissions", "The permission audit"),
 ("android-battery-health", "Battery health, honestly"),
 ("android-notifications", "Notification control")]),

("android-app-permissions", "android", "guide",
"Android app permissions: the ten-minute audit that matters",
"What each scary-sounding permission actually grants, which apps deserve it, and the settings that answer “only while using the app”.",
"""<p>Permission prompts train you to tap Allow without reading — an app asks for location at the exact moment you are trying to do something else. A ten-minute audit reverses that. You will not find spies behind every icon, but you will find apps holding more than their job requires, and taking back the excess costs nothing.</p>
<h2>The audit path</h2>
<p>Settings → Privacy (or Security & privacy) → Permission manager. It groups permissions by what they access — location, camera, microphone, contacts, storage — and shows which apps hold each. Work down the big four: location, camera, microphone, contacts. For each app ask one question: does its core job need this? A torch app with location is not suspicious so much as unemployed.</p>
<h2>The three levels, and the one to prefer</h2>
<p>Modern Android offers "Allow all the time", "Allow only while using the app", "Ask every time" and "Don't allow". Almost nothing honest needs all-the-time location — maps should get while-using. Microphone and camera should be while-using for nearly everything. If an option surprises you, Android's newer versions also ask where photos are concerned: you can grant access to just the items you pick instead of the whole library.</p>
<h2>The honest caveats</h2>
<p>Menus differ by maker and version — Samsung, Xiaomi and others reshape Settings, so the names above are landmarks, not street addresses. Some revokes have consequences: revoking an alarm app's notifications silences your alarm. And permission lists do not map cleanly to badness — a scanner app genuinely needs the camera. The audit is about least privilege, not suspicion of every icon.</p>
<h2>When you install next</h2>
<p>Read the prompt at install time instead of tapping through — it takes the same two seconds. And for the accounts behind the apps, the same least-privilege logic applies to what data training on assistant apps receives: see <a href="/tech/ai-assistant-data-training-settings/">the data-settings guide</a>. Storage pressure from those same apps is its own guide: <a href="/tech/free-up-storage-android/">freeing space without deleting your life</a>.</p>""",
[],
[("free-up-storage-android", "Freeing phone storage"),
 ("ai-assistant-data-training-settings", "What assistants do with your data"),
 ("two-factor-authentication-setup", "2FA done right")]),

("android-battery-health", "android", "guide",
"Android battery health: what actually drains it, and what is just myth",
"How to read the battery screen, the three real drains, the charging myths worth retiring, and how to tell a tired battery from a tired phone.",
"""<p>Battery advice online is mostly folklore with confidence. The useful version starts with the one screen that measures instead of guessing: Settings → Battery (often Battery → Battery usage), which ranks what consumed your charge since the last full one. Read that list before buying anything a blog post sells.</p>
<h2>The three drains that are usually real</h2>
<p><b>The screen</b> — biggest single consumer for most people; a shorter screen timeout and a less blinding brightness do more than any killer app. <b>Poor-signal radio strain</b> — a phone hunting for signal in a weak-coverage area burns charge aggressively; if your workday sits in one, that is the mystery solved. <b>An app misbehaving after an update</b> — one app topping the usage list that does not match how much you used it is the honest suspect; update or, if it persists, replace it.</p>
<h2>Charging myths, retired</h2>
<p>Modern phones manage their own charging: they slow near full and stop at full, so leaving them plugged in overnight is largely handled. Heat is the genuine enemy — a phone charging under a pillow or on a sunlit dashboard ages its battery far faster than any charging habit. Fast charging generates more warmth; that is a real trade-off, not a deal-breaker. The old "drain it to zero monthly" ritual belongs to battery chemistry your phone no longer uses.</p>
<h2>Tired battery or tired phone?</h2>
<p>Two honest tests. Time: a phone that went three years of daily cycles has genuinely worn — lithium batteries are consumables, and many makers design around a few hundred full cycles before capacity visibly drops. Behaviour: sudden percentage drops, shutdowns at 20–30%, or swelling (which is a stop-using-it safety issue, not a maintenance item) point at the battery itself. Samsung and others surface battery diagnostics in their settings or members apps; otherwise a repair shop reads the cycle count in minutes.</p>
<h2>If the battery is the problem</h2>
<p>A battery replacement costs a fraction of a new phone and often restores it completely — worth pricing before shopping. And when you do shop, the same discipline applies as in our <a href="/tech/free-up-storage-android/">storage guide</a>: check what you actually need first.</p>""",
[],
[("free-up-storage-android", "Freeing phone storage"),
 ("android-notifications", "Notification control"),
 ("android-app-permissions", "The permission audit")]),

("android-notifications", "android", "guide",
"Android notifications: silence the noise, keep the signal",
"Channels, priority and Do Not Disturb done properly — so the phone only interrupts for things you actually care about.",
"""<p>A phone that buzzes for everything trains you to ignore it — including the messages that mattered. The fix is not silence-everything; it is giving the few important senders a lane and making everyone else wait politely.</p>
<h2>Start with the big lever</h2>
<p>Do Not Disturb (Settings → Sound → Do Not Disturb, or quick settings) blocks calls, sounds and visual interruptions on schedule or on demand. The power move is its exceptions: allow starred contacts and repeat calls through, so DND becomes quiet by default but never deaf to family. Pair it with a bedtime schedule and the phone stops being the last thing you see at night.</p>
<h2>Then fix it per app, the Android way</h2>
<p>Android apps deliver notifications through <b>channels</b> — categories the app itself defines (for a chat app: messages, group mentions, marketing). Long-press any notification to switch that channel off instantly, or open Settings → Apps → [app] → Notifications for the full list. This is the feature that makes Android good at this: you can keep a shopping app's order updates and kill its "deals", without losing the app.</p>
<h2>Priority, honestly</h2>
<p>Buzzing is for people, not pixels. Calls, messages from actual humans, calendar alarms: keep sound. News, social likes, "you have a new follower": silent — they still appear in the shade for when you look. If your maker's software buries these controls (some do), the per-app long-press still works everywhere Android runs.</p>
<h2>The habit that keeps it working</h2>
<p>Every time an interruption annoys you, fix it in that moment — three seconds now, permanent peace. And if what is draining you is a phone that feels generally overloaded, storage and battery hygiene are the other two levers: <a href="/tech/free-up-storage-android/">space</a> and <a href="/tech/android-battery-health/">battery health</a>.</p>""",
[],
[("android-battery-health", "Battery health, honestly"),
 ("free-up-storage-android", "Freeing phone storage"),
 ("android-app-permissions", "The permission audit")]),

# ============================================================ WINDOWS
("why-is-my-computer-slow", "windows", "guide",
"Why is my computer slow? Triage in the order that finds the cause",
"The five checks that explain most slow Windows PCs — in the order that rules causes out fastest, and the point where you stop tuning and decide.",
"""<p>Computers are rarely slow for mysterious reasons. They are slow for five common ones, and checking them in the right order finds the culprit in under half an hour. Work top to bottom; stop when the machine feels fast again.</p>
<h2>1. Is the drive full?</h2>
<p>Windows wants breathing room on the system drive (usually C:) to work at all. Under about 10% free and everything — updates, browsing, startup — stutters. Settings → System → Storage shows the truth and offers cleanup of temporary files. A full drive is the single most common cause of "my computer got old".</p>
<h2>2. What launches at startup?</h2>
<p>Task Manager (Ctrl+Shift+Esc) → Startup apps: everything here runs every boot. Disable what you do not need at login — the messaging apps, updaters and helpers that appointed themselves. This is free speed on machines that have been lived in for a year or two.</p>
<h2>3. Updates pending or mid-install?</h2>
<p>A machine that is suddenly slow often is working: Windows Update installing, or an antivirus scan running. Give it an hour on power before diagnosing deeper. Check Settings → Windows Update for anything stuck in a loop — that is its own guide: <a href="/tech/windows-update-problems/">when updates get stuck</a>.</p>
<h2>4. What is using the RAM and CPU right now?</h2>
<p>Task Manager's Processes tab, sorted by Memory or CPU: anything pinning a core or eating RAM while idle is a name and a decision — uninstall, replace or reconfigure. A browser with forty tabs is a legitimate workload, not a mystery: the <a href="/tech/browser-problems/">browser guide</a> covers taming it.</p>
<h2>5. The honest hardware conversation</h2>
<p>If the drive is a hard disk (HDD) rather than a solid-state drive (SSD), that alone explains most of what you feel: an SSD swap is the single biggest upgrade an old machine can receive, and it is cheaper than you fear. Beyond that: 8 GB of RAM is a workable floor today, and security software beyond the built-in Windows Security rarely adds protection worth the drag.</p>
<h2>When to stop tuning</h2>
<p>If storage is healthy, startup is lean, updates are current and the machine is still slow for your work, the decision is between the SSD/RAM upgrade and replacement — and that is a shopping decision, not a tuning one.</p>""",
[],
[("windows-update-problems", "When updates get stuck"),
 ("browser-problems", "Browser problems, tamed"),
 ("custom-domain-dns-order", "Our desk's own first-hand builds")]),

("browser-problems", "windows", "guide",
"Browser slow, crashing or behaving strangely? The honest fix list",
"Extensions are the usual suspect. The cache is usually innocent. The order that actually sorts a misbehaving browser.",
"""<p>The browser is where your computer actually lives, so when it slows, crashes or starts behaving strangely, everything feels broken. Most browser trouble is caused by one of three things — extensions, an overloaded session, or a profile that has accumulated years of state. Check them in that order.</p>
<h2>1. Extensions first, always</h2>
<p>Every extension runs code on every page. The ad-blocker, the coupon finder, the three productivity helpers — combined, they are a second browser's worth of work, and one badly updated extension can slow or break every site. Disable all of them, restart the browser, and feel the difference. Re-enable the two or three you truly use; lose the rest. That is not a compromise, it is the fix.</p>
<h2>2. The session itself</h2>
<p>Forty open tabs each hold memory and keep scripts running. The honest test: bookmark the pile (all tabs to a bookmarks folder), close everything, and reopen only what this week needs. If the browser is suddenly fast, the session was the workload.</p>
<h3>The cache question</h3>
<p>Clearing cache is the folk remedy for everything, and it is mostly theatre for slowness — the cache exists to make things faster. Where it genuinely helps is a site misbehaving specifically for you: a broken layout or stale login state. Clear the <em>site's</em> data (site settings → delete data) rather than nuking every cookie and getting logged out of your life.</p>
<h2>3. The profile, tested honestly</h2>
<p>Years of history, cookies and settings can rot a profile. Every major browser lets you create a fresh second profile in its menu; sign in to nothing, visit your problem sites. Fast and clean means the old profile is the patient — migrate what matters (passwords and bookmarks sync over) rather than performing surgery.</p>
<h2>4. When it is not the browser</h2>
<p>If a clean profile on a lean machine still crawls, the computer is the slow party, not the browser — run the <a href="/tech/why-is-my-computer-slow/">PC triage list</a>. And if "strange behaviour" means search results you did not ask for or a homepage you cannot change, that is not maintenance, that is an unwanted extension or hijacker: remove everything from the extensions list and treat any prompt that offered it as a <a href="/tech/how-to-spot-a-suspicious-link/">suspicious link lesson</a>.</p>""",
[],
[("why-is-my-computer-slow", "The PC triage list"),
 ("windows-update-problems", "When updates get stuck"),
 ("how-to-spot-a-suspicious-link", "Spotting suspicious links")]),

("windows-update-problems", "windows", "guide",
"Windows Update is stuck, failing or looping — what actually works",
"The patience timeline first, the built-in troubleshooter second, the manual fix third — and the line where a repair shop earns its fee.",
"""<p>A stuck update feels like a broken computer, but the sequence has more patience than most people give it. Windows Update failures have a short list of real causes — a interrupted download, a full drive, a driver disagreement, or the update service itself hiccuping — and they are fixable in that order.</p>
<h2>Step zero: patience with a deadline</h2>
<p>Updates install in stages and restart themselves; an hour of "working on updates" on a slow drive is normal. The honest deadline is two to three hours with no disk activity (listen, or watch the drive light). Past that, a hard restart is safe — the installer is designed to roll back and retry.</p>
<h2>1. The boring causes first</h2>
<p>Free storage (updates need real room — see the <a href="/tech/why-is-my-computer-slow/">triage list</a> if the drive is packed), a stable power connection, and no pending restart ignored for weeks. A surprising share of "stuck" updates are three queued restarts deep.</p>
<h2>2. The built-in troubleshooter</h2>
<p>Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run. It resets the update components that genuinely get stuck and knows the common failure patterns. Microsoft also ships a standalone version for repeated failures. Run it, restart, try again.</p>
<h2>3. Read the error, then the manual path</h2>
<p>The failure code (something like 0x800f0922) is a name, not noise — searching the exact code finds the specific fix. The general-purpose manual path is well-supported: stop the update services, rename the SoftwareDistribution folder so Windows rebuilds its download cache cleanly, restart the services, and let it fetch fresh. Microsoft's own support pages document this for current versions; follow the steps for your exact edition.</p>
<h2>4. The professional line</h2>
<p>Updates that fail repeatedly after a clean retry, fail in safe mode too, or arrive with boot problems belong to a repair shop — so do any fix involving system files you are not certain about. Updates matter (they carry the security fixes), but a bricked weekend costs more than an hour of professional time.</p>
<h2>While it heals</h2>
<p>Pause is not failure: Settings lets you pause updates for up to a few weeks while you sort the machine calmly — just do not let the pause become the permanent state, because the browser and <a href="/tech/two-factor-authentication-setup/">2FA</a> can only protect an updated system so much.</p>""",
[],
[("why-is-my-computer-slow", "The PC triage list"),
 ("browser-problems", "Browser problems, tamed"),
 ("two-factor-authentication-setup", "2FA done right")]),

# ============================================================ CODING
("how-to-read-an-error-message", "coding", "guide",
"How to read an error message (the skill that makes coding possible)",
"Errors are instructions in disguise: read them bottom-up, trust the first one, copy the exact text, and search like a professional.",
"""<p>Beginners treat error messages as failure. Programmers treat them as the program telling them exactly where to look — because that is what they are. Learning to read them is the single skill that turns coding from guessing into engineering.</p>
<h2>Read the last error first</h2>
<p>Long error output (a "stack trace") is read bottom-up: the final line is what actually went wrong, and the lines above are the path the program took to get there. When there are multiple errors, the first one is usually the real one — later errors are often dominoes. Fix from the top error, rerun, and watch the list shrink.</p>
<h2>The vocabulary that pays for itself</h2>
<p>A handful of messages cover most beginner pain. SyntaxError: you typed something the language cannot parse — a missing bracket, colon or quote, usually on or just before the named line. NameError / ReferenceError: you used a name nothing has defined — a typo, or code running before the thing it needs exists. TypeError: a value is not the type the operation needs — adding a number to text, calling something that is not a function. IndexError / out of range: you asked a list for a position it does not have; check its length. Permission denied: the file or port belongs to someone else — a rights problem, not a code problem.</p>
<h2>Copy the exact text</h2>
<p>Not a paraphrase — the exact message, including the code if there is one. Searching the precise string finds the forum post; paraphrasing finds vibes. This is the same discipline as our <a href="/home/why-does-my-circuit-breaker-keep-tripping/">breaker-tripping guide</a>: the error is a clue with a name, and the name narrows the world.</p>
<h2>Then reproduce it small</h2>
<p>The fastest fixes come from the smallest failing example. Comment out half the program; does the error survive? Keep halving until five lines produce it. The bug in five lines is visible; the same bug in five hundred is a haystack.</p>
<h2>On a phone, the same skill applies</h2>
<p>Our <a href="/tech/learning-to-code-on-a-phone-termux/">Termux diary</a> is this skill in practice — what broke on a phone, and what reading the errors fixed. And once your program talks to another service, <a href="/tech/what-is-an-api/">knowing what an API is</a> explains a whole species of error messages.</p>""",
[],
[("learning-to-code-on-a-phone-termux", "Coding on a phone: what broke"),
 ("what-is-an-api", "What is an API?"),
 ("git-and-github-for-beginners", "Git and GitHub for beginners")]),

("git-and-github-for-beginners", "coding", "guide",
"Git and GitHub for beginners, explained by a site that runs on them",
"Version control without the jargon: what Git remembers, what GitHub is for, and the four commands that carry most real work.",
"""<p>Git has a reputation for difficulty that it mostly earns from being taught backwards — commands before concepts. Start with the idea instead: <b>Git is a time machine for a folder of files.</b> Every commit is a save point with a label, and you can walk back to any of them. That is the entire product.</p>
<h2>Git vs GitHub, in one paragraph</h2>
<p>Git is the tool that runs on your computer and records history. GitHub is a website that hosts a copy of that history so a team (or you, on another machine) can share it, review it and collaborate. This very site — every guide on this desk — lives in a GitHub repository and deploys from it; when we rotate credentials, it is <a href="/tech/github-token-hygiene/">token hygiene</a> we practised on it, and when we documented deployment, it was <a href="/tech/render-static-deploy/">Render from that repository</a>.</p>
<h2>The mental model that makes commands make sense</h2>
<p>Your folder has three states. <b>Working directory:</b> the files you are editing. <b>Staging area:</b> the basket of changes you have chosen to include in the next save. <b>History:</b> the committed save points. You move edits into the basket deliberately, then save the basket as one named moment. That is why there are two steps — it lets a commit tell one story ("fix the mobile menu") instead of ten.</p>
<h2>The four commands that carry most work</h2>
<p>git status — what state am I in? (run it constantly; it is the dashboard). git add filename — put this change in the basket (or git add . for everything). git commit -m "what and why" — save the basket as a moment. git push — upload your new moments to GitHub. Later, git pull brings a collaborator's moments down. Clone once at the start of a project to fetch the whole history to a new machine; everything else is the same four moves.</p>
<h2>The beginner mistakes, pre-lived</h2>
<p>Commits the size of a week ("misc changes") waste the time machine — small, story-shaped commits are what make history worth having. Merge conflicts look terrifying and are just Git showing two people edited the same lines; pick the text you want, remove the markers, commit. And commit messages addressed to your future self beat clever ones addressed to nobody.</p>
<h2>Where to learn by doing</h2>
<p>The Pro Git book is free online and definitive for the deep end; GitHub's own start-here docs walk the first repository in minutes. Pair it with our <a href="/tech/how-to-read-an-error-message/">error-reading skill</a> — Git's occasional refusals are just messages with names.</p>""",
[("Pro Git — the free book", "https://git-scm.com/book/en/v2"),
 ("GitHub — Get started docs", "https://docs.github.com/en/get-started")],
[("how-to-read-an-error-message", "Reading error messages"),
 ("github-token-hygiene", "Token hygiene, first-hand"),
 ("what-is-an-api", "What is an API?")]),

("what-is-an-api", "coding", "guide",
"What is an API? The explainer that finally makes it click",
"The restaurant menu, the weather app, and why “API” is less mysterious than the people using the word want it to sound.",
"""<p>API is three words — Application Programming Interface — that describe a simple idea: <b>a defined way for one program to ask another program for something, without knowing how it works inside.</b> You have used dozens today. Every app on your phone that shows weather, maps, or payments is asking another service through an API.</p>
<h2>The menu, used properly</h2>
<p>A restaurant API would be its menu. You do not enter the kitchen and cook; you order from a fixed list of dishes, described in fixed terms, and the kitchen brings food. The menu is the interface: it promises what you can ask for and what you will get. Change the kitchen's chef, ovens or suppliers — the menu survives, and your order still works. Programs hide their insides the same way, which is why the insides can be rewritten without breaking yours.</p>
<h2>The weather app, end to end</h2>
<p>Your weather app does not own satellites. It asks a weather service's API: "give me today's forecast for Lagos" — a request to a web address with parameters — and gets back structured data (temperatures, times, codes), not a designed webpage. The app's job is presenting that data well. The service's job is being right. The API is the contract between them: named fields, agreed formats, rules about how often you may ask.</p>
<h2>Why APIs explain a lot of errors</h2>
<p>When an app "can't connect", the conversation between programs failed — the request was malformed, the answer came back in an unexpected shape, or the contract changed. Our <a href="/tech/how-to-read-an-error-message/">error-reading guide</a> applies directly: the message names which side of the contract broke. And pricing models follow contracts too — AI services charge per tokens of text through their APIs, which is why our <a href="/tech/deepseek-vs-chatgpt/">DeepSeek comparison</a> keeps insisting the free chat and the paid API are different products.</p>
<h2>The one-line version to keep</h2>
<p>An API is a menu: a promise about what you can ask for and what you will get back — so programs can work together without peeking into each other's kitchens.</p>""",
[],
[("how-to-read-an-error-message", "Reading error messages"),
 ("deepseek-vs-chatgpt", "DeepSeek vs ChatGPT, honestly"),
 ("git-and-github-for-beginners", "Git and GitHub for beginners")]),

("phone-wont-connect-to-wifi", "android", "guide",
"Phone won't connect to Wi-Fi? The checklist, in the order that works",
"From the thirty-second fixes to the network reset, with the one setting almost nobody checks.",
"""<p>A phone that refuses a network it used to join happily is following a short list of failure modes: the radio got stuck, the saved credentials went stale, the router moved on without it, or the phone itself drifted out of sync. Work down this list in order — the first three steps fix most cases.</p>
<h2>1. The thirty-second pair</h2>
<p>Toggle airplane mode on, wait ten seconds, off. Then toggle Wi-Fi off and on. This resets the radio stack, which genuinely gets wedged — especially after a day of hopping between networks. It feels too simple; it works too often to skip.</p>
<h2>2. Forget the network, then rejoin</h2>
<p>Tap the network's name → Forget (long-press it in the Wi-Fi list if there is no button), then rejoin from scratch, typing the password carefully. Saved networks go stale: the password was changed on the router, or the phone is holding a corrupted credential from months ago. Case matters; a trailing space from autocomplete happens more than you would think.</p>
<h2>3. Restart the phone, then the router</h2>
<p>Phone off and on clears its network stack properly. If that is not it, unplug the router for thirty seconds and let it fully come back — routers accumulate their own cruft, and a restart re-does their addresses and channels. Most "the Wi-Fi is broken" household emergencies end here.</p>
<h2>4. The setting almost nobody checks: date and time</h2>
<p>Wi-Fi security involves certificates, and certificates are date-sensitive. A phone with the wrong date — dead battery, manual clock, travel — will refuse networks that are perfectly fine, with errors that never mention time. Set the clock to automatic (Settings → System → Date & time) and try again.</p>
<h2>5. "Connected, no internet" — whose fault is it?</h2>
<p>If the phone says connected but nothing loads, test another device on the same network. Nobody else works either: it is the router or the line from your provider — restart the router, then call them. Only your phone fails: the problem is local, and the next step is yours.</p>
<h2>6. The reset with a warning label</h2>
<p>Settings → System → Reset options → Reset Wi-Fi & Bluetooth (naming varies by maker) returns all network settings to factory state: every saved network, every Bluetooth pairing, gone. It is the honest last resort before suspecting hardware — and after it, you will re-pair your earbuds too, which is fair warning to read the <a href="/tech/bluetooth-not-pairing/">Bluetooth pairing guide</a> as well.</p>
<h2>If none of it works</h2>
<p>Try the phone on a different network (a friend's hotspot works). If it joins fine, your router is the patient — its manual or your provider takes it from there. If it fails everywhere, the phone's Wi-Fi hardware or software is the patient: a support visit beats a new phone in almost every case. And for the networks you do join away from home, our <a href="/tech/public-wifi-risks/">public Wi-Fi guide</a> covers what is and is not worth worrying about once you are connected.</p>""",
[],
[("bluetooth-not-pairing", "Bluetooth not pairing?"),
 ("public-wifi-risks", "The honest public Wi-Fi guide"),
 ("android-battery-health", "Battery health, honestly")]),

("bluetooth-not-pairing", "android", "guide",
"Bluetooth won't pair? The ritual, done in the right order",
"Pairing is a first-meeting protocol with rules. Most failures are one of five things — and the fix is almost always sequence, not hardware.",
"""<p>Bluetooth pairing fails for boring reasons, which is good news: boring reasons have boring fixes. The mistake most people share is treating the accessory's power button as the whole story — power is not pairing mode, and the difference is where nearly every "my phone can't find it" begins.</p>
<h2>1. Pairing mode, not just power</h2>
<p>Earbuds, speakers and car kits do not advertise themselves forever — discoverability is a window, usually opened by holding the button for five-plus seconds until the light flashes (often blue-and-white, but read your model's cue). Powering on is not enough; if the phone cannot see the device, put the device back into pairing mode first, then scan.</p>
<h2>2. One bond at a time</h2>
<p>Most Bluetooth devices hold a handful of pairings, and older ones hold two. An accessory that quietly connects itself to a laptop across the room will ignore your phone. Turn Bluetooth off on every other device that has ever been paired with it — then try again. Multipoint devices (that advertise two-device connection) still choose one active stream; knowing which is the quirk of your model matters.</p>
<h2>3. The stale-bond fix: unpair, then re-pair</h2>
<p>A bond that broke mid-handshake — firmware updated on the accessory, phone updated, or the accessory factory reset — leaves both sides holding half a conversation. In the phone's Bluetooth settings, tap the device → Unpair/Forget. Re-enter pairing mode on the accessory and pair from scratch. This is Bluetooth's equivalent of the Wi-Fi "forget network" move, and it settles most stubborn cases.</p>
<h2>4. Range and interference, honestly</h2>
<p>Bluetooth is a ten-metre technology at best, and walls, bodies and crowded 2.4 GHz air (Wi-Fi routers, microwaves, the neighbour's earbuds) chew into that. Pair in the same room, once; afterwards the bond holds across the whole flat. If audio stutters after pairing succeeds, that is interference or distance — not a failed pairing.</p>
<h2>5. Connected but no sound</h2>
<p>That is usually not a Bluetooth failure at all: check the phone's media-audio toggle for that device (Settings → Bluetooth → gear icon), and the accessory's own buttons — many earbuds have a "music only" or one-ear mode that mutes the call channel. Read the pairing prompt carefully too: contacts and call-history permissions are normal for car kits and unnecessary for earbuds — our <a href="/tech/android-app-permissions/">permission-audit logic</a> applies to accessories just as it does to apps.</p>
<h2>6. When it is genuinely the hardware</h2>
<p>Try pairing the accessory with a different phone. If it refuses everywhere, the accessory is the patient — its factory reset (every maker documents the button combo) is the last self-service step before support. If it pairs fine elsewhere, run the phone's <a href="/tech/phone-wont-connect-to-wifi/">network-reset step</a> from the Wi-Fi guide — it clears Bluetooth bonds along with Wi-Fi, and rebuilds both cleanly.</p>""",
[],
[("phone-wont-connect-to-wifi", "Wi-Fi connection checklist"),
 ("android-app-permissions", "The permission audit"),
 ("android-battery-health", "Battery health, honestly")]),

("how-to-reset-forgotten-passwords", "safety", "guide",
"Forgot your password? The recovery playbook, done safely",
"The order that avoids lockouts and traps: email first, official flows only, and the post-reset cleanup most people skip.",
"""<p>Everyone forgets passwords; the systems exist for exactly this. What turns a five-minute recovery into a bad week is doing the steps in the wrong order, or through the wrong door. This is the safe sequence.</p>
<h2>Rule zero: arrive at the door yourself</h2>
<p>Never reset through a link in a message you did not request. "Your password was changed, click here to secure your account" is the classic phishing shape — see <a href="/tech/how-to-spot-a-suspicious-link/">how to read a link before tapping</a>. Open the service's own site or app and use its Forgot-password flow there. A real reset email, to be clear, is fine to act on — if you requested it. Unsolicited reset emails mean someone else is trying your door; ignore the link and change the password directly instead.</p>
<h2>1. Email first, always</h2>
<p>Your email address is the recovery key to everything else — every "reset password" flow ends in your inbox. If the forgotten account is your email itself, recover it before touching anything else, and check its recovery settings (phone number, backup address) are current while you are in there. Recovering a bank login is trivial when your email is solid, and impossible when it is not.</p>
<h2>2. The reset itself</h2>
<p>Use the official flow, prove identity the way the service asks, and choose a new password that is long and not reused anywhere — let a generator do it. Put it straight into your <a href="/tech/bitwarden-free-password-manager/">password manager</a> before you close the tab; "I'll write it down later" is where passwords die. If the manager itself is the forgotten account, recover it with its master-password recovery options or its emergency kit — services like Bitwarden document this precisely because it cannot be done socially.</p>
<h2>3. The cleanup most people skip</h2>
<p>For any account that may have been accessed by someone else — not just forgotten — the reset is step one of three. First: sign out all other sessions (most services have exactly this button in security settings). Second: check for attacker persistence — unknown forward rules in email, unknown linked devices, unknown app passwords, a changed recovery phone. Third: re-enable or refresh <a href="/tech/two-factor-authentication-setup/">two-factor authentication</a>, and regenerate backup codes if there is any chance the old list was seen.</p>
<h2>4. Recovery codes are the spare tyre</h2>
<p>If you enabled 2FA and have your backup codes, a lost password with a lost phone is still a five-minute recovery: use one code at the 2FA prompt, then regenerate the list (a used code is a spent code) and put the fresh list somewhere that is not the phone doing the approving.</p>
<h2>5. When recovery simply fails</h2>
<p>The honest limit: with no working email, no recovery codes and no 2FA fallback, some accounts cannot be recovered — and that is the system working, because the same door is open to strangers. Services with account-recovery forms (the big email providers among them) ask questions only the real owner would survive; answer them patiently from a usual device and location. Prevention beats recovery every time this happens: 2FA on the email, current recovery details, and the manager holding the rest.</p>""",
[],
[("two-factor-authentication-setup", "2FA done right"),
 ("bitwarden-free-password-manager", "Bitwarden's free plan, checked"),
 ("how-to-spot-a-suspicious-link", "Spotting suspicious links")]),
("what-is-dns", "web-and-hosting", "guide",
"What is DNS? The internet's phonebook, explained properly",
"Names into numbers, records into pages: what actually happens when you type an address — and why changes take time to appear.",
"""<p>DNS &mdash; the Domain Name System &mdash; is the internet's phonebook. Computers find each other by numeric address; humans remember names. DNS is the service that translates one into the other, every single time you visit anything.</p>
<h2>The lookup, step by step</h2>
<p>Type a name and four quiet things happen. Your device asks a <b>resolver</b> (usually your ISP's, or a public one) to find the address. The resolver, if it does not already know, asks the <b>root servers</b>, which point it at the <b>TLD servers</b> for the ending (.com, .ng, .org), which point it at the domain's <b>nameservers</b> &mdash; the ones the domain's owner chose. The nameserver answers with the <b>record</b>: an A record holding the IPv4 address, AAAA for IPv6, CNAME for &ldquo;same as that other name&rdquo;, MX for where email goes, TXT for verification strings. The resolver caches the answer for as long as the record's <b>TTL</b> (time to live) allows, and hands it to your browser, which connects to the number.</p>
<h2>Why this matters to you</h2>
<p><b>Propagation is caching.</b> When you change a DNS record, the change spreads as resolvers' caches expire &mdash; usually fast, occasionally hours, depending on the old TTL. &ldquo;DNS propagation&rdquo; is not a global switch flipping; it is cached answers politely dying at different times. We lived this exact sequence moving this very site: <a href="/tech/custom-domain-dns-order/">the DNS order that avoids downtime</a> is our first-hand walkthrough. <b>Email breaks by DNS</b> &mdash; MX records are why mail stops when nameservers go wrong. And <b>&ldquo;site not found&rdquo; errors are usually DNS</b>, not the website being down.</p>
<h2>The security angle, briefly</h2>
<p>Because DNS is old and trusting, the industry has been adding verification: DNSSEC signs answers so they cannot be forged in transit, and browsers increasingly prefer encrypted DNS. You do not need to configure any of it to benefit &mdash; but knowing the phonebook can be tampered with explains a certain species of &ldquo;why am I on the wrong site?&rdquo; attack, the kind our <a href="/tech/how-to-spot-a-suspicious-link/">link-reading guide</a> teaches you to catch at the other end.</p>""",
[("Cloudflare Learning — What is DNS?", "https://www.cloudflare.com/learning/dns/what-is-dns/")],
[("custom-domain-dns-order", "The DNS order that avoids downtime"),
 ("what-is-ssl-https", "What HTTPS actually means"),
 ("how-the-internet-works", "How the internet works, plainly")]),

("what-is-ssl-https", "web-and-hosting", "guide",
"What the padlock really means: HTTPS and SSL, honestly",
"Encryption, identity, and the thing the padlock does NOT tell you — which is exactly what phishers exploit.",
"""<p>HTTPS is the encrypted version of the web's own language. The padlock in the address bar means two things: the connection between you and the site is <b>encrypted</b> (nobody on the network can read or tamper with what passes), and the site presented a <b>certificate</b> proving that the server answering is the one the address belongs to. SSL is the old name for the technology &mdash; the modern version is called TLS &mdash; but &ldquo;SSL certificate&rdquo; stuck as the everyday phrase.</p>
<h2>How the handshake works, without maths</h2>
<p>On connecting, the server shows its certificate &mdash; a document signed by a <b>certificate authority</b>, an organisation browsers already trust. Your browser checks the signature, the name match, and the dates. If all pass, both sides perform a key exchange and everything afterwards travels encrypted. The whole performance takes a fraction of a second, and certificate authorities such as Let's Encrypt issue the certificates free of charge, which is why the whole web finally went encrypted.</p>
<h2>The honest warning: the padlock is not a trust badge</h2>
<p>Here is the part most people get wrong, and phishers rely on: <b>HTTPS means the connection is private, not that the site is honest.</b> Any scammer can get a free certificate for a lookalike domain in minutes, and their fake bank page will show the same padlock as the real one. Read the <em>name</em>, not the lock &mdash; our <a href="/tech/how-to-spot-a-suspicious-link/">suspicious-link guide</a> is built around exactly that. The padlock tells you nobody is eavesdropping; it cannot tell you who is on the other end.</p>
<h2>What HTTPS protects, in practice</h2>
<p>Passwords, card details, messages and everything else in transit &mdash; from the coffee-shop network to the backbone. What it does not cover: a compromised device, a site that mishandles what you send it, or the fact of your visit (the network still sees you talked to that domain). For public networks specifically, our <a href="/tech/public-wifi-risks/">public Wi-Fi guide</a> separates the solved threats from the live ones.</p>""",
[("Mozilla — What is TLS?", "https://developer.mozilla.org/en-US/docs/Glossary/TLS")],
[("how-to-spot-a-suspicious-link", "Spotting suspicious links"),
 ("what-is-dns", "What is DNS?"),
 ("public-wifi-risks", "The honest public Wi-Fi guide")]),

("how-the-internet-works", "web-and-hosting", "guide",
"How the internet works, plainly",
"Packets, addresses, protocols and one world-wide agreement on shapes: the whole machine in five minutes, no jargon held back.",
"""<p>Strip away the mystique and the internet is one idea: <b>computers sending each other envelopes.</b> Everything else &mdash; cables, Wi-Fi, apps, this page &mdash; is agreement about how the envelopes are addressed, carried and opened.</p>
<h2>The envelopes: packets</h2>
<p>When you load a page, the data is chopped into small packets. Each packet carries the destination address (an <b>IP address</b> &mdash; the postal system of the network) and a fragment of the payload. Routers are the sorting offices: each one reads the address and forwards the packet one hop closer. Packets from the same page may take different routes and arrive out of order; your device reassembles them by number. If one is lost, it is re-requested. That is the internet's quiet genius: no central office, just millions of routers cooperating on a shared addressing scheme.</p>
<h2>The three agreements that make it feel like magic</h2>
<p><b>IP</b> is the addressing agreement &mdash; every device gets a location. <b>TCP</b> is the delivery agreement &mdash; ordered, checked, re-sent when lost. <b>HTTP/HTTPS</b> is the conversation agreement &mdash; browsers ask (&ldquo;GET me this page&rdquo;), servers answer. Names never travel; before any of this, <a href="/tech/what-is-dns/">DNS</a> translated the name you typed into the address the envelopes need. Then the server sends the page's files, your browser renders them, and &mdash; if the connection is <a href="/tech/what-is-ssl-https/">HTTPS</a> &mdash; every envelope was sealed in transit.</p>
<h2>Where &ldquo;the cloud&rdquo; actually is</h2>
<p>Websites live on servers &mdash; computers that stay on and answer requests &mdash; owned by hosting companies and platform providers. This very site is a static site on such a platform: when you requested this page, a server handed back the files that a build process prepared, over exactly the envelope system above. Our <a href="/tech/render-static-deploy/">Render deployment walkthrough</a> and <a href="/tech/where-to-host-website-for-free/">free-hosting comparison</a> are first-hand tours of that half of the story.</p>
<h2>Why this is worth knowing</h2>
<p>Because every troubleshooting decision gets easier when you know the path: no page at all is usually DNS; slow is the route or the server; broken-looking is the page itself; &ldquo;your connection is not private&rdquo; is the handshake. Diagnose by stage, not by vibes.</p>""",
[],
[("what-is-dns", "What is DNS?"),
 ("what-is-ssl-https", "What HTTPS actually means"),
 ("render-static-deploy", "Deploying a static site, first-hand")]),

("what-is-a-database", "coding", "guide",
"What is a database? From spreadsheet to system",
"Tables, rows and the questions that make databases different from files &mdash; the mental model every beginner actually needs.",
"""<p>A database is a program whose entire job is remembering structured data and answering questions about it quickly. The beginner's bridge to the concept: a spreadsheet. Tables with columns you define, rows you add, and the ability to sort and filter. Databases do that &mdash; at scales and with safety guarantees a spreadsheet cannot touch.</p>
<h2>The vocabulary that unlocks everything</h2>
<p>A <b>table</b> holds one kind of thing (users, orders, articles). Each <b>row</b> is one item; each <b>column</b> is one attribute, with a fixed type. Rows are found by <b>keys</b> &mdash; a unique ID per row (the primary key), and columns that point at rows in other tables (foreign keys), which is how &ldquo;this order belongs to that user&rdquo; is expressed. Asking questions is <b>querying</b>, most often in SQL, a language that reads almost like the question: which rows from orders where the date is this month, sorted by total.</p>
<h2>Why not just use files?</h2>
<p>Because files fall over exactly where apps live: two people writing at once, a crash mid-write, a question across a million rows. Databases solve those as their core competence &mdash; controlled concurrent access, transactions (a change that either fully happens or fully does not), and indexes that keep lookups fast as data grows. That is the honest one-line answer to &ldquo;why is this so complicated?&rdquo;</p>
<h2>The SQL / NoSQL fork, honestly brief</h2>
<p>SQL databases (PostgreSQL, MySQL, SQLite) are the classic: structured tables, strict types, powerful joins. The &ldquo;NoSQL&rdquo; family (document stores, key-value stores and friends) trades some of that structure for flexibility and different scaling shapes. Beginners should not agonise: learn one SQL database properly and the concepts &mdash; tables, keys, queries, transactions &mdash; transfer to everything.</p>
<h2>Where this sits in an app</h2>
<p>Apps talk to their database behind the scenes; everything you submit through an interface lands in one. The conversation between programs at scale is the <a href="/tech/what-is-an-api/">API</a> &mdash; and when that conversation misfires, it is the <a href="/tech/how-to-read-an-error-message/">error messages</a> that name which side broke. Database first, API second, interface third: that is the honest architecture of almost everything you use.</p>""",
[],
[("what-is-an-api", "What is an API?"),
 ("how-to-read-an-error-message", "Reading error messages"),
 ("git-and-github-for-beginners", "Git and GitHub for beginners")]),

("how-to-take-a-screenshot-windows", "windows", "guide",
"How to take a screenshot on Windows (all the ways, and when to use each)",
"Win+Shift+S is the one to learn. The others, honestly ranked — including the key nobody explains.",
"""<p>Windows has half a dozen screenshot methods; you need one for daily life and two for special occasions. Learn <b>Windows key + Shift + S</b> and you have the daily one: the screen dims, you drag a rectangle, and the capture lands on your clipboard &mdash; paste it straight into a message or document with Ctrl+V. A notification pops the image too, in case you want to mark it up first.</p>
<h2>The full honest roster</h2>
<p><b>Win + Shift + S</b> &mdash; region, window or full screen via the little toolbar; clipboard; the modern default. <b>Win + Print Screen</b> &mdash; grabs the whole screen and silently saves a file into Pictures → Screenshots; the move when you need the file, not the clipboard. <b>Print Screen alone</b> &mdash; whole screen to clipboard only (old school; pair with paste). <b>Alt + Print Screen</b> &mdash; only the active window, to clipboard: the politest way to screenshot without your twenty other tabs. <b>The Snipping Tool</b> &mdash; the app behind Win+Shift+S; open it directly when you want its extras, such as a delay timer for capturing menus that only appear after a hover.</p>
<h2>Two honest tips</h2>
<p>Screenshots of an error message are how you ask for help properly &mdash; capture the whole message, including any code, exactly as printed (our <a href="/tech/how-to-read-an-error-message/">error-reading guide</a> explains why the exact text matters). And before you paste a screenshot into a chat, glance at what else is in the frame: notification previews, open inboxes and visible passwords have embarrassed more people than any hacker.</p>
<h2>If the keys do nothing</h2>
<p>On some laptops Print Screen hides behind an Fn key, and a few systems route the key elsewhere &mdash; if Win+Shift+S dims nothing, search &ldquo;Snipping Tool&rdquo; from the Start menu and use it directly; the result is identical. Nothing here needs installing: it is all built into Windows 10 and 11.</p>""",
[],
[("why-is-my-computer-slow", "The PC triage list"),
 ("browser-problems", "Browser problems, tamed"),
 ("windows-keyboard-shortcuts", "Shortcuts worth knowing")]),

("windows-keyboard-shortcuts", "windows", "guide",
"The Windows shortcuts actually worth memorising",
"Twelve keystrokes that quietly buy back hours — chosen for being durable, not exotic.",
"""<p>Keyboard shortcuts are compound interest: each saves seconds, and you press them hundreds of times a month. This is not the exhaustive list &mdash; it is the twelve that survive every Windows version and pay for themselves in a week.</p>
<h2>The everyday six</h2>
<p><b>Alt + Tab</b> &mdash; hop between open windows; hold Alt and tap Tab to walk them. <b>Win + D</b> &mdash; show the desktop and back, when the window pile needs parting. <b>Win + L</b> &mdash; lock the computer, the two seconds of hygiene every desk away from your desk deserves. <b>Ctrl + Shift + Esc</b> &mdash; Task Manager, straight up, no menu journey (the <a href="/tech/why-is-my-computer-slow/">slow-PC triage</a> lives here). <b>Ctrl + Z</b> &mdash; undo, nearly everywhere, several steps deep; its partner Ctrl + Y or Ctrl + Shift + Z redoes. <b>Win + V</b> &mdash; clipboard history: the last many things you copied, ready to paste again. Enable it once and copying becomes a memory instead of a single slot.</p>
<h2>The window-wranglers</h2>
<p><b>Win + Left/Right arrow</b> &mdash; snap the window to half the screen; the two-document setup without a second monitor. <b>Win + Up/Down</b> &mdash; maximise, or shrink to taskbar. <b>Win + E</b> &mdash; File Explorer, instantly. <b>Win + .</b> (the full stop) &mdash; the emoji and symbols panel; genuinely useful in messages, secretly delightful.</p>
<h2>How to actually learn them</h2>
<p>Pick two. Use them deliberately for three days &mdash; say the keys' names in your head as you press &mdash; then add two more. Shortcuts learned in bulk evaporate; shortcuts learned as habits stay. And when a shortcut leads somewhere you do not recognise (Task Manager, say), that is a doorway into the machine's own diaries &mdash; the same reason <a href="/tech/how-to-take-a-screenshot-windows/">screenshots</a> and this list are the desk's first two recommendations for anyone settling into a Windows machine.</p>""",
[],
[("how-to-take-a-screenshot-windows", "Screenshots, all the ways"),
 ("why-is-my-computer-slow", "The PC triage list"),
 ("browser-problems", "Browser problems, tamed")]),
]
from tech_roadmap_data import TECH_ROADMAP_T1 as _TECH_ROADMAP_T1
from tech_roadmap2_data import TECH_ROADMAP_T2 as _TECH_ROADMAP_T2
from tech_roadmap2_data import TECH_ROADMAP_T2B as _TECH_ROADMAP_T2B
from tech_roadmap3_data import TECH_ROADMAP_T3 as _TECH_ROADMAP_T3
NEW_TECH_GUIDES.extend(_TECH_ROADMAP_T3)
from tech_roadmap4_data import TECH_ROADMAP_T4 as _TECH_ROADMAP_T4
NEW_TECH_GUIDES.extend(_TECH_ROADMAP_T4)
from tech_roadmap5_data import TECH_ROADMAP_T5 as _TECH_ROADMAP_T5
NEW_TECH_GUIDES.extend(_TECH_ROADMAP_T5)
from tech_roadmap5b_data import TECH_ROADMAP_T5B as _TECH_ROADMAP_T5B
NEW_TECH_GUIDES.extend(_TECH_ROADMAP_T5B)
from tech_master_m2_data import TECH_MASTER_M2 as _TECH_MASTER_M2
NEW_TECH_GUIDES.extend(_TECH_MASTER_M2)
from tech_master_m3_data import TECH_MASTER_M3 as _TECH_MASTER_M3
NEW_TECH_GUIDES.extend(_TECH_MASTER_M3)
from tech_master_m4_data import TECH_MASTER_M4 as _TECH_MASTER_M4
NEW_TECH_GUIDES.extend(_TECH_MASTER_M4)
from tech_master_m5_data import TECH_MASTER_M5 as _TECH_MASTER_M5
NEW_TECH_GUIDES.extend(_TECH_MASTER_M5)
from tech_master_m6_data import TECH_MASTER_M6 as _TECH_MASTER_M6
NEW_TECH_GUIDES.extend(_TECH_MASTER_M6)
NEW_TECH_GUIDES.extend(_TECH_ROADMAP_T2B)
NEW_TECH_GUIDES.extend(_TECH_ROADMAP_T2)
NEW_TECH_GUIDES.extend(_TECH_ROADMAP_T1)

# ---- batch 16: the IdeaWave steals - two evergreen search-visibility guides ----
NEW_TECH_GUIDES.extend([
("check-if-google-indexed-your-page", "web-and-hosting", "guide",
"How to check if Google has indexed a page",
"The ten-second test, the definitive test, and the five reasons a page stays out of Google even when everything looks fine.",
"""<p>Every site owner eventually plays this game: you publish a page, search a phrase from it, and nothing comes back. Before assuming the worst, work down this list &mdash; it is ordered by speed, and it is the same order we use on this very site.</p>
<h2>The ten-second test: the <code>site:</code> operator</h2>
<p>Search <code>site:yourdomain.com/your-page/</code>. If the URL appears, the page <b>is indexed</b>. Two honest caveats: the number of results <code>site:</code> reports is a fuzzy filter, not a reliable count, and appearing under <code>site:</code> says nothing about <i>where</i> the page ranks. It answers "is it in?", never "is it visible?"</p>
<h2>The definitive test: URL Inspection</h2>
<p>Google Search Console's URL Inspection tool is the only authoritative answer. Paste the full URL and read the verdict: <b>"URL is on Google"</b> means indexed; <b>"URL is not on Google"</b> comes with a reason &mdash; noindex, crawl blocked, duplicate (Google chose another canonical), or simply not crawled/processed yet. That reason field is the whole game; it converts guessing into a todo.</p>
<h2>The five usual suspects</h2>
<p><b>1. The page says noindex.</b> Check the <code>&lt;meta name="robots"&gt;</code> tag and the <code>X-Robots-Tag</code> HTTP header &mdash; either can block indexing, and a staging-to-production slip is the classic cause. <b>2. robots.txt blocks crawling.</b> Subtle but real: a blocked page can still appear in Google "without content" because a link gave Google the URL; blocking is not noindexing, and combining both is a well-known trap. <b>3. The canonical points elsewhere.</b> If the page declares (or Google infers) a preferred version, duplicates get consolidated &mdash; Search Console says "Google chose a different canonical". <b>4. It is simply new.</b> Crawling and processing take time on young sites; patience plus a submitted sitemap beats frantic republishing. <b>5. Google saw it and declined.</b> "Crawled &mdash; currently not indexed" and "Discovered &mdash; currently not indexed" in the Pages report usually mean quality/thinness signals, not a penalty. The fix is honest: make the page substantially useful and linked from your own navigation.</p>
<h2>Indexed is not ranked</h2>
<p>Indexing is entry to the library, not a seat at the front. Once a page is "on Google", ranking is a separate, slower contest &mdash; which is why we track indexing in batches on this site rather than refreshing hourly, and why our <a href="/tech/sitemap-indexnow/">sitemap and IndexNow routine</a> is about speed of discovery, not about rank.</p>
<h2>Quick hygiene that prevents the mystery</h2>
<p>Keep one canonical domain (decide www vs non-www and redirects once); never ship noindex on templates; submit sitemaps and read the Pages report monthly; and check that staging subdomains are blocked <i>at the server</i>, not just unlinked. For how the domain and DNS layer underneath works, see <a href="/tech/custom-domain-dns-order/">custom domains and DNS order</a> &mdash; and if your pages are fine in Google but invisible in AI answers, that is a different (newer) problem: <a href="/how-to-get-cited-by-ai-search/">how to get cited by AI search tools</a>.</p>""",
[("Google Search Central: block indexing (noindex)", "https://developers.google.com/search/docs/crawling-indexing/block-indexing"),
 ("Google Search Central: URL Inspection", "https://support.google.com/webmasters/answer/9012289")],
[("sitemap-indexnow", "Sitemaps and IndexNow"), ("custom-domain-dns-order", "Custom domains, DNS order"), ("how-to-get-cited-by-ai-search", "Cited by AI search")]),
("how-to-get-cited-by-ai-search", "ai", "guide",
"How to get your site cited by AI search tools",
"What is actually known about being quoted by chatbots and AI search &mdash; and the honesty to spot what nobody can guarantee.",
"""<p>A growing share of answers now comes from AI tools that fetch, read and summarise the web. Publishers naturally want to be the source being quoted. Here is the desk's honest brief &mdash; including which parts are evidence and which are practice.</p>
<h2>How the tools actually find answers</h2>
<p>Most AI answers that reference the web work in two steps: retrieve (search or fetch live pages) then summarise. That means the first gate is not "AI optimisation" &mdash; it is boring crawlability: your pages must be fetchable, fast, and not blocked from the crawlers you choose to allow. Each vendor runs its own crawler with a name in robots.txt (OpenAI's GPTBot, Anthropic's ClaudeBot, Google-Extended for Gemini training among others); allowing or blocking them is a publisher decision, not a technical default. If you block them, do not expect to be cited by them.</p>
<h2>What genuinely helps (the evidence-backed part)</h2>
<p><b>Answer-shaped writing.</b> Tools lift passages that directly answer a question &mdash; a clear heading, a definition or number early in the section, and a date. <b>Entity clarity.</b> Say what a thing is, plainly, on the page; consistent naming across your site helps machines know what your pages are about. <b>Freshness you can prove.</b> Visible last-updated stamps and dated corrections &mdash; the practice this whole desk runs on &mdash; make a page safer to quote than an undated one. <b>Being referenced elsewhere.</b> Retrieval favours sources the wider web already trusts; citations in your niche flow to pages that earn ordinary links and mentions. <b>Technical health.</b> The checks in <a href="/tech/check-if-google-indexed-your-page/">how to check if Google indexed a page</a> matter here too: a page that is confused about its own canonical or blocked by accident will not be anyone's source.</p>
<h2>What nobody can guarantee (the honest part)</h2>
<p>There is no submission form, no paid inclusion, and no known trick that forces a citation &mdash; anyone selling "guaranteed AI rankings" is selling. The <code>llms.txt</code> file convention exists but is not a documented requirement of any major assistant; treat it as optional, unproven, and harmless at best. And measurement is genuinely hard: many chatbot visits arrive without usable referral data, so expect small, manual checks (ask the tools the questions your pages answer and note what gets quoted) rather than precise dashboards.</p>
<h2>The boring conclusion</h2>
<p>Everything that reliably improves AI citations overlaps almost perfectly with good publishing: be clear, be sourced, be dated, be crawlable, be genuinely useful. That is why this desk treats AI visibility as an <i>outcome</i> of the editorial standard, not a separate channel &mdash; the same discipline behind our <a href="/tech/sitemap-indexnow/">sitemap and IndexNow routine</a> and our correction policies. Do those well, keep the robots decisions deliberate, and check manually now and then. Anything more precise being promised to you is theatre.</p>""",
[("OpenAI: crawlers and bots documentation", "https://platform.openai.com/docs/bots"),
 ("Google Search Central: Google crawlers (incl. Google-Extended)", "https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers")],
[("check-if-google-indexed-your-page", "Check if Google indexed a page"), ("sitemap-indexnow", "Sitemaps and IndexNow"), ("github-token-hygiene", "Token hygiene")]),
])
