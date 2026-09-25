# -*- coding: utf-8 -*-
"""BRYME Tech — 10/10 brief, Tier 2 batch B: SSD vs HDD, RAM guide, Microsoft 365.

Verification receipts (2026-09-15):
- SSD/HDD performance and TBW figures: manufacturer-datasheet conventions
  (Samsung 870 EVO 1TB = 600 TBW, Crucial MX500 1TB = 360 TBW, etc. — the DSET
  manufacturer-TWB table) + interface arithmetic (SATA III ~600 MB/s ceiling,
  PCIe gens per standard). Real-world speeds stated as RANGES, attributed to
  independent testing; no single-number claims.
- Backblaze: the honest treatment — their SSD AFR sample is small and their
  comparison caveat is stated rather than buried; HDD AFR ranges (0.4-1.5%)
  attributed to Backblaze fleet data.
- RAM: Microsoft's Windows 11 4 GB minimum is the official number, framed as
  install-minimum not comfortable-use. The 2026 workload tiers (8/16/32/64)
  presented as consensus bands across multiple independent guides, not as
  Microsoft's recommendation. No invented "Microsoft recommends 32GB" claim.
- Microsoft 365: plan structure and storage numbers from Microsoft's own
  support comparison page (free web apps = 5 GB OneDrive, web only;
  Basic = 100 GB, web only; Personal/Family = desktop apps + 1 TB/person,
  Family up to 6 people). Prices NOT pinned in the article — readers pointed
  at the official pricing page with a "prices move; check the day you decide"
  note, per the first-party rule. The "Classic" plan existence (older pricing
  without AI) noted as a real option per Microsoft Q&A.
"""

BATCH_1010_B4 = [

    # ------------------------------------------------------------------ #
    # Tier 2 #14: SSD vs HDD
    # ------------------------------------------------------------------ #
    ("ssd-vs-hdd", "buying", "guide",
     "SSD vs HDD in 2026: what each is actually for now",
     "The speed gap is enormous and mostly irrelevant to the buying question. The honest decision now runs on cost-per-terabyte, endurance maths, and what happens when each type fails.",
     """<p>The SSD vs HDD question used to be "which is faster?" — and the answer was so one-sided it stopped being interesting. The 2026 question is sharper: <em>what is each type actually for now?</em> because both survive in modern machines for completely different reasons. Here's the honest sorting.</p>

<h2>The speed gap, honestly labelled</h2>
<p>Interface numbers first, because they're arithmetic rather than marketing: a spinning drive moves data at roughly 100-200 MB/s (mechanical limit); a SATA SSD saturates its ~600 MB/s interface; NVMe drives range from ~3,000 MB/s (PCIe 3.0) to well past 10,000 MB/s on the newest PCIe 5.0 hardware. Independent testing consistently lands there. But the number that changes daily <em>feel</em> isn't sequential speed — it's random access latency: a hard drive's head physically travels (milliseconds); flash doesn't (~tens of microseconds). That's why an SSD boot or app launch feels instant in a way no HDD spec improvement ever replicates. If a machine still boots from a spinning drive, moving to an SSD is <a href="/tech/laptop-buying-ram-storage/">the single most felt upgrade most people can make</a>.</p>

<h2>What HDD is still for: the cost-per-terabyte wall</h2>
<p>Flash is cheap per gigabyte now, but the physics of mass storage still favours spinning platters at scale: large-capacity HDDs sell for a fraction of the price per terabyte of equivalent SSD capacity, which is why backups, archives, surveillance footage and media servers still run on HDDs. The 3-2-1 backup rule's "two different media" is naturally satisfied by keeping your working copies on SSD and your cold archive on HDD — <a href="/tech/three-two-one-backup-rule/">the backup rule is its own piece</a>. The honest summary: HDD is no longer a performance choice; it's a capacity-per-currency choice, and a good one.</p>

<h2>Endurance: the TBW maths people skip</h2>
<p>SSDs wear out by total bytes written — the manufacturer's TBW rating. The honest scale, from manufacturer datasheets: a typical 1 TB consumer drive carries roughly 300-600 TBW; high-capacity premium drives run higher. What that means in practice: writing 100 GB <em>every single day</em> exhausts a 600 TBW rating in about sixteen years. Normal users write a fraction of that, so for typical use, endurance is a specification, not a worry. The exceptions: constant video recording, database work, heavy scratch-disk use — workloads where you check the TBW rating instead of assuming. HDDs wear mechanically instead (moving parts, rated in power-on hours); both types report health via S.M.A.R.T. data — <a href="/tech/computer-fans-loud/">when a drive starts failing, the machine usually tells you other ways first</a>.</p>

<h2>Reliability: what the field data actually says</h2>
<p>Backblaze publishes annualised failure rates for their drive fleets — the best public field data that exists. The honest reading: their HDD fleets show annualised failure rates in the low single digits percentage-wise (varying by model and age), and their SSD comparison sample is much smaller — small enough that Backblaze itself flags the comparison as not statistically settled. What's uncontroversial: SSDs have no moving parts to shock-damage (the laptop-drop scenario), HDDs fail mechanical deaths that are often preceded by audible warnings, and <em>both</em> fail eventually. Anyone who tells you one type "just doesn't fail" is selling something. The rule that matters: a drive is a component, not a vault — <a href="/tech/cloud-vs-local-backup/">important data lives in more than one place</a> or it doesn't really live anywhere.</p>

<h2>The failure modes nobody prices in</h2>
<p>SSD failure tends toward sudden (controller death takes everything at once); HDD failure is often gradual (bad sectors spread, sounds change, files corrupt one at a time). Neither is kinder — sudden loss with no warning versus slow loss with warning. And there's an archival quirk worth knowing: unpowered flash slowly loses charge over years (spec'd in JEDEC standards at typical consumer temperatures), so a USB SSD in a drawer for a decade is not the archival medium people assume. For cold archives, HDD and a periodic power-on check remain reasonable practice. Backup strategy beats media loyalty, every time.</p>

<h2>The 2026 buying answer</h2>
<p><b>System drive:</b> SSD, non-negotiable — the machine's responsiveness lives there. <b>Games and big working files:</b> SSD while the budget allows; load times and asset streaming are real. <b>Bulk archive and backup target:</b> HDD, where terabytes are cheapest and speed doesn't matter. <b>Portable/rough use:</b> SSD (shock resistance is structural). That's the whole modern map — speed where you feel it, capacity where you store it, and <a href="/tech/refurbished-vs-new-tech/">the refurb market</a> for drives is worth the usual caution (check warranty and health reports before trusting used storage of either type).</p>""",
    [("Backblaze — Drive Stats (annualised failure-rate reports)", "https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data"),
     ("JEDEC — SSD endurance and retention standards", "https://www.jedec.org/")],
    [("three-two-one-backup-rule", "The 3-2-1 backup rule"),
     ("laptop-buying-ram-storage", "Laptop RAM and storage, honestly"),
     ("cloud-vs-local-backup", "Cloud vs local backup"),
     ("refurbished-vs-new-tech", "Refurbished vs new tech")]),

    # ------------------------------------------------------------------ #
    # Tier 2 #15: How much RAM do you actually need
    # ------------------------------------------------------------------ #
    ("how-much-ram-do-you-need", "buying", "guide",
     "How much RAM do you actually need in 2026? 8, 16, 32 or 64 GB",
     "The honest tiering by what you actually do: why 16 GB is the default answer, when 8 GB genuinely still works, and the two workloads that legitimately eat 32 GB and beyond.",
     """<p>RAM advice usually fails in one direction: a number without a workload attached. Microsoft's official Windows 11 minimum is 4 GB — the number that lets it <em>install</em>, not the number that makes it pleasant — and everything above that floor is a workload decision. So: tiers by what you actually do.</p>

<h2>8 GB: works, honestly, for one thing at a time</h2>
<p>Email, documents, a handful of browser tabs, video calls, streaming — 8 GB handles these fine <em>individually</em>. What it can't handle is them simultaneously: a modern browser alone can take multiple GB with a busy tab session, and once RAM fills, Windows starts paging to storage, which is the slowdown people mistake for "the computer getting old." 8 GB is right for a genuinely light-use machine — a student writing machine, a kitchen laptop — and wrong the moment serious multitasking or a heavy app joins. If you're buying, treat it as the floor tier to upgrade from, not the target.</p>

<h2>16 GB: the default answer for a reason</h2>
<p>For most people in 2026, 16 GB is the tier that removes RAM from the list of things to think about: heavy browsing, office suite, video calls, photo management, and mainstream gaming all fit with headroom. Every current consensus guide lands here for general use, and so do we. The buying translation: on a desktop where RAM is upgradeable, 16 GB now and more later is fine. On a laptop — especially one with soldered memory — buy the tier you'll want in year three, not the tier that's enough today; <a href="/tech/laptop-buying-ram-storage/">that laptop-buying piece</a> covers the upgradeability trap in full.</p>

<h2>32 GB: the two legitimate eaters</h2>
<p>Two workloads genuinely consume 32 GB: <b>video editing</b> (4K timelines and colour work) and <b>local AI workloads</b> — running models on-device is memory-hungry in a way nothing else consumer-grade is, and it's the reason the 32 GB tier went from "enthusiast" to "mainstream question" in two years. Add heavy virtual machines, big-codebase development with containers, and 3D work. For everyone else, 32 GB is comfort, not necessity — buy it if the price gap is small, don't stretch for it.</p>

<h2>64 GB and beyond: professional territory</h2>
<p>8K/multicam editing, large 3D scenes, VM farms, serious data work — the professional tier. The honest advice: people who need 64 GB almost always already know, because their current machine is telling them (Task Manager's memory pressure at peak load is the real spec sheet). Nobody should buy 64 GB "to be safe"; they should buy it because their measured workload demands it.</p>

<h2>The reading-the-machine skill</h2>
<p>High RAM usage by itself is not a problem — Windows deliberately fills free RAM as cache, because empty memory does nothing. The signals that matter: sustained high <em>committed</em> usage, frequent paging (disk activity during ordinary app switches), and stutter that vanishes when you close the biggest app. Task Manager (Ctrl+Shift+Esc → Performance → Memory) shows all three. That's how you answer "is my machine's problem actually RAM?" instead of guessing — and if the answer is paging on a machine with an old spinning drive, the SSD upgrade fixes more than RAM would; <a href="/tech/ssd-vs-hdd/">those two upgrades trade places as the best value depending on which one you still need</a>.</p>

<h2>The one-paragraph answer</h2>
<p>8 GB for genuinely light single-task use; 16 GB for everyone normal — the tier that stops the question mattering; 32 GB for video editors and local-AI users; 64 GB+ when your measured workload demands it. And on non-upgradeable machines, buy one tier above what today needs. General guidance, not a rule — the Task Manager check is the honest answer for any specific machine.</p>""",
    [("Microsoft — Windows 11 system requirements (official 4 GB minimum)", "https://www.microsoft.com/windows/windows-11-specifications")],
    [("laptop-buying-ram-storage", "Laptop RAM and storage, honestly"),
     ("ssd-vs-hdd", "SSD vs HDD in 2026"),
     ("why-is-my-computer-slow", "Why is my computer slow"),
     ("phone-buying-specs-that-matter", "Phone specs that matter vs marketing")]),

    # ------------------------------------------------------------------ #
    # Tier 2 #18: Microsoft 365 free vs paid
    # ------------------------------------------------------------------ #
    ("microsoft-365-free-vs-paid", "subscriptions", "guide",
     "Microsoft 365 free vs paid: what the free tier actually includes in 2026",
     "Word, Excel and PowerPoint in your browser cost nothing — the official comparison, the storage math that decides most upgrades, and who the paid tiers are genuinely for.",
     """<p>The most common misconception in this space is that Office costs money, full stop. It hasn't for years: sign into Microsoft365.com with any Microsoft account and you get <b>Word, Excel, PowerPoint, OneNote and Outlook as web apps, free</b>, with 5 GB of OneDrive storage. That free tier is the correct answer for a large share of home users — the paid question is about three specific gaps.</p>

<h2>The official comparison, plainly stated</h2>
<p>Per Microsoft's own support comparison: the <b>free web apps</b> run in a browser, receive security updates but no new features, include 5 GB of OneDrive, and include no technical support. <b>Microsoft 365 Basic</b> (the cheapest paid tier) keeps the web apps but adds 100 GB of storage and ad-free email — it's a storage plan, not an apps plan. <b>Personal and Family</b> add the <em>desktop</em> apps for PC and Mac (installable on multiple devices, five signed in at once), 1 TB of OneDrive per person (Family covers up to six people, each with their own terabyte), ongoing feature updates, and support. Family's per-person arithmetic — six terabytes and six app installs for the household — is the quiet best-value move in the lineup if even two people use it. The top <b>Premium</b> tier layers the AI features; note Microsoft's own caveat that AI benefits stay with the subscription owner and don't share to Family members.</p>

<h2>The three gaps that actually decide it</h2>
<p><b>1. Web vs desktop apps.</b> The web versions cover writing, spreadsheets and slides well for everyday work; the desktop versions matter when you need offline access, heavy files that strain browser limits, or specific power features. Most home users never hit this gap; power users hit it in week one.</p>
<p><b>2. The storage wall.</b> 5 GB fills fast — one phone's photo backup alone can break it. This is the most common real reason people upgrade, and the honest comparison is against standalone cloud storage: price the Basic tier against <a href="/tech/cloud-storage-mistakes/">what 100 GB costs elsewhere</a> before assuming it's a bargain, and the Personal/Family tiers against whether your household actually uses the desktop apps.</p>
<p><b>3. Feature motion.</b> Free tier gets security updates only; paid tiers get the new features as they ship. If your work depends on the latest Office capabilities, that's the paid signal.</p>

<h2>The alternatives question, honestly</h2>
<p>The free tier isn't the only free option: Google's web apps and LibreOffice (free desktop suite) both exist, and the honest comparison is its own piece — <a href="/tech/google-docs-vs-word-vs-notion/">we've written the Docs vs Word vs Notion comparison separately</a>. The lock-in angle matters too: documents saved in OneDrive's native formats move between these worlds better than they used to, but formatting fidelity on complex documents still favours staying put. The subscription-creep question is real here — Office is one of the line items worth an audit: <a href="/tech/subscription-creep-audit/">our subscription audit piece</a> walks the full habit — and note Microsoft has also kept lower-priced "Classic" plan variants (without the newer AI features) available in several markets, which their own support threads confirm. Check the pricing page the day you decide; prices have moved more than once recently.</p>

<h2>The decision, in one line each</h2>
<p><b>Light home use, online, documents and spreadsheets:</b> the free web apps — genuinely enough. <b>Need storage more than apps:</b> Basic, priced against standalone storage rivals. <b>Want desktop apps or 1 TB:</b> Personal. <b>Two or more people in the household:</b> Family, the arithmetic winner. <b>AI features that matter to your workflow:</b> Premium, with the no-family-sharing caveat understood. Prices change — <a href="https://www.microsoft.com/microsoft-365/buy/compare-all-microsoft-365-products">Microsoft's official comparison page</a> is the first-party source of the day.</p>""",
    [("Microsoft Support — Free web apps vs paid subscription (official comparison)", "https://support.microsoft.com/en-us/microsoft-365-activation-licensing/manage-microsoft-365/what-s-the-difference-between-a-paid-microsoft-365-subscription-and-the-free-web-apps"),
     ("Microsoft — Compare Microsoft 365 plans (official pricing page)", "https://www.microsoft.com/microsoft-365/buy/compare-all-microsoft-365-products")],
    [("google-docs-vs-word-vs-notion", "Google Docs vs Word vs Notion"),
     ("subscription-creep-audit", "The subscription audit"),
     ("cloud-storage-mistakes", "Cloud storage mistakes"),
     ("free-software-alternatives", "Free software alternatives")]),
]
