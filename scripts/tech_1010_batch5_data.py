# -*- coding: utf-8 -*-
"""Tech 10/10 brief batch 5 — Tier 1 #2: the cloud storage comparison.

Why this piece exists
---------------------
Tier 1 #2 of the 10/10 content research brief. BRYME had cloud-storage
*adjacent* coverage (`cloud-storage-mistakes`, `cloud-vs-local-backup`) but no
plan-by-plan comparison of the four services people actually choose between,
which is the commercial-intent query the brief prioritises.

Verification receipts (all prices checked live 2026-09-15, US storefronts)
-------------------------------------------------------------------------
Every number below was read off the vendor's own pricing page on the date
above, not from a review site. Secondary coverage disagreed sharply — one
aggregator still listed Google AI Pro at 2 TB, another showed euro prices as
if they were dollars — so the primary pages were fetched directly:

- Google One   https://one.google.com/about/plans
  Free 15 GB shared across Photos/Drive/Gmail; Basic 100 GB $1.99/mo;
  Google AI Plus 2 TB $9.99/mo; Google AI Pro 5 TB $19.99/mo. Annual toggle
  advertised as "Save up to 16%". All paid tiers share with up to 5 others.
  NOTE the 2026 restructure: AI Pro is now 5 TB, not the 2 TB older articles
  describe, and the mid tier is branded "Google AI Plus".

- Microsoft    https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products
               https://www.microsoft.com/en-us/microsoft-365/onedrive/onedrive-plans-and-pricing
  Basic $1.99/mo or $19.99/yr, 100 GB, no desktop Office apps;
  Personal $9.99/mo or $99.99/yr, 1 TB, 5 devices signed in at once;
  Family $12.99/mo or $129.99/yr, 1-6 people, up to 6 TB (1 TB per person),
  AI for the subscription owner only; Premium $19.99/mo or $199.99/yr.
  Cross-check: Microsoft states yearly savings of $19.89 / $25.89 / $39.89
  for Personal / Family / Premium. Those equal 12x monthly minus the annual
  price exactly ($119.88-$99.99, $155.88-$129.99, $239.88-$199.99), so the
  monthly and annual figures are mutually consistent.

- Dropbox      https://www.dropbox.com/plans
  Basic free 2 GB; Plus $9.99/mo, 2 TB ("2,000 GB"), 1 person, 30-day version
  history and deleted-file restore, transfers up to 50 GB, 3 eSignature
  requests/month; Standard $15/user/mo from 3 TB pooled, 180-day history;
  Advanced $24/user/mo from 15 TB pooled, 1-year history, E2E encryption,
  advanced key management, SSO. Page carries a monthly/yearly billing toggle;
  the figures above are what the page showed on the default state.

- Apple        https://www.apple.com/icloud/
  iCloud+ 50 GB $0.99/mo; 200 GB $2.99/mo; 2 TB $9.99/mo; 6 TB $29.99/mo;
  12 TB $59.99/mo. Plan shareable with up to five other family members at no
  extra cost. Includes Private Relay, Hide My Email, HomeKit Secure Video.

Deliberately NOT claimed
------------------------
- No free-tier quota is asserted for OneDrive or iCloud: the pages fetched did
  not state one in the retrieved markup, so the piece compares paid tiers and
  leaves the free allowances to Google (15 GB, stated) and Dropbox (2 GB,
  stated) where they were actually on the page.
- Dropbox's yearly prices were not captured (toggle state), so the piece says
  the yearly option exists and is worth checking rather than inventing a
  figure. Google's annual figures likewise: only the "up to 16%" claim was on
  the page, so that is what is quoted.
- Cost-per-TB figures are plain division of the vendor's own prices, labelled
  as arithmetic in the text, not sourced claims.
- No "best overall" verdict. Per the brief's factual-language rule the piece
  ranks by situation, and states that prices are US-listed, volatile and
  frequently promoted.
"""

BATCH_1010_B5 = [

    # ------------------------------------------------------------------ #
    # Tier 1 #2: Cloud storage comparison
    # ------------------------------------------------------------------ #
    ("cloud-storage-plans-compared", "subscriptions", "guide",
     "Cloud storage compared: Google One, OneDrive, Dropbox and iCloud+, plan by plan",
     "Four services, three of which charge $9.99 a month for 2 TB. The real differences are not storage — they are what comes bundled, who can share it, and how fast the price moves when a promotion ends.",
     """<p>Cloud storage pricing looks confusing because four companies are selling four different products under the same headline number. Google and Microsoft are selling AI subscriptions that happen to include storage. Apple is selling a privacy and device-backup layer. Dropbox is selling file workflow for people who move documents around all day. Once you sort by <em>what the subscription is actually for</em>, the price table stops being confusing and starts being obvious.</p>

<p><strong>In one line:</strong> if you only need space, buy the cheapest tier that fits and stop reading. If you are paying $9.99 or more a month, you are almost certainly paying for AI features, Office apps or family sharing — so decide which of those you want first, and treat the storage as the side effect.</p>

<p>All prices below are the US figures published on each vendor's own pricing page, checked 15 September 2026. They are list prices, they change, and all four run frequent promotions — the last section explains why the promotional price is the one that misleads people.</p>

<h2>The four price tables, side by side</h2>
<p><strong>Google One</strong> (from one.google.com/about/plans). Every Google account includes up to 15 GB shared across Photos, Drive and Gmail; paid storage replaces that allowance rather than adding to it.</p>
<ul>
<li><strong>Basic — 100 GB, $1.99/month.</strong> Storage plus sharing with up to five others. No Gemini AI uplift.</li>
<li><strong>Google AI Plus — 2 TB, $9.99/month.</strong> Gemini app usage limits 2x higher than without an AI plan, the Flash Thinking model, Google Flow, Gemini in Gmail, more Gemini Notebook access.</li>
<li><strong>Google AI Pro — 5 TB, $19.99/month.</strong> Gemini limits 4x higher, the Pro model and Deep Research, Gemini in Gmail, Docs and Vids, YouTube Premium Lite (Individual) and Google Home Premium Standard.</li>
</ul>
<p>An annual option is offered and advertised as saving up to 16%. All three paid tiers share storage with up to five other people.</p>

<p><strong>Microsoft 365 / OneDrive</strong> (from microsoft.com's plan comparison and OneDrive pricing pages).</p>
<ul>
<li><strong>Basic — 100 GB, $1.99/month or $19.99/year.</strong> One person. Cloud storage plus a 100 GB mailbox, ransomware protection for files and photos, ad-free Outlook. <em>No desktop Office apps</em> — this is the tier people misread.</li>
<li><strong>Personal — 1 TB, $9.99/month or $99.99/year.</strong> One person, signed in on up to five devices at once. Word, Excel, PowerPoint, Outlook and OneNote desktop apps with Copilot, Microsoft Defender, Teams with Copilot.</li>
<li><strong>Family — up to 6 TB, $12.99/month or $129.99/year.</strong> One to six people, 1 TB each, each person on up to five devices simultaneously. AI features are for the subscription owner only.</li>
<li><strong>Premium — $19.99/month or $199.99/year.</strong> Everything in Family with extensive rather than higher Copilot usage.</li>
</ul>

<p><strong>Dropbox</strong> (from dropbox.com/plans).</p>
<ul>
<li><strong>Basic — 2 GB, free.</strong></li>
<li><strong>Plus — 2 TB, $9.99/month.</strong> One person. 30-day version history and deleted-file restore, transfers up to 50 GB, three eSignature requests a month with unlimited self-signing, PDF editing.</li>
<li><strong>Standard — from 3 TB pooled, $15 per user/month.</strong> One or more people, 180-day history, 100 GB transfers, advanced PDF editing, team folders, admin console.</li>
<li><strong>Advanced — from 15 TB pooled, $24 per user/month.</strong> Three or more people, one-year history, end-to-end encryption, advanced key management, single sign-on.</li>
</ul>
<p>A yearly billing option exists on the same page; the monthly figures are the ones quoted here.</p>

<p><strong>iCloud+</strong> (from apple.com/icloud). Every plan can be shared with up to five other family members at no extra cost, and every plan includes Private Relay, Hide My Email and HomeKit Secure Video.</p>
<ul>
<li><strong>50 GB — $0.99/month</strong></li>
<li><strong>200 GB — $2.99/month</strong></li>
<li><strong>2 TB — $9.99/month</strong></li>
<li><strong>6 TB — $29.99/month</strong></li>
<li><strong>12 TB — $59.99/month</strong></li>
</ul>

<h2>The one pattern worth memorising: the $9.99 plateau</h2>
<p>Three of the four services charge <strong>exactly $9.99 a month for 2 TB</strong> — Google AI Plus, Dropbox Plus and iCloud+. Microsoft is the outlier at that price point: $9.99 buys 1 TB in Microsoft 365 Personal, half the space, because you are paying for the Office desktop apps rather than the gigabytes.</p>
<p>Divide the price by the terabytes and the shape appears (plain arithmetic on the vendors' own numbers, not a sourced claim):</p>
<ul>
<li>100 GB tiers — Google Basic and Microsoft 365 Basic, both $1.99/month — work out around <strong>$19.90 per TB per month</strong>.</li>
<li>The 2 TB plateau works out at <strong>$5.00 per TB per month</strong>.</li>
<li>Google AI Pro at 5 TB for $19.99 works out at <strong>$4.00 per TB per month</strong>.</li>
<li>Microsoft 365 Family at 6 TB for $12.99 works out at about <strong>$2.17 per TB per month</strong> — the cheapest large-pool storage in this comparison, by a wide margin.</li>
</ul>
<p>So the per-gigabyte price falls roughly tenfold between the 100 GB tier and the family tier. That is the entire economics of cloud storage in one observation: <strong>small plans are expensive per byte, and the discount is bought with either AI features or extra people.</strong> If you need 200 GB and nothing else, you will pay a bad rate — that is the price of not wanting the bundle.</p>

<h2>What you are actually paying for at each price point</h2>
<p><strong>At $0.99-$2.99 (Apple's small tiers).</strong> Pure storage, and the cheapest entry in the comparison. Worth it only if you are inside Apple's ecosystem, because the value is in iCloud Backup and Photos working invisibly across devices you already own.</p>

<p><strong>At $1.99 (Google Basic, Microsoft Basic).</strong> Same price, different products. Google's 100 GB is storage plus family sharing. Microsoft's 100 GB is storage plus a 100 GB mailbox, ad-free Outlook and ransomware protection — but explicitly <em>without</em> the Word, Excel and PowerPoint desktop apps. People who buy Microsoft 365 Basic expecting installed Office apps are the most common mistake in this whole category.</p>

<p><strong>At $9.99.</strong> Four completely different purchases. Google: 2 TB and a real Gemini uplift. Apple: 2 TB and the privacy features. Dropbox: 2 TB and file workflow — version history, large transfers, eSignature. Microsoft: 1 TB and the actual Office desktop suite with Copilot. This is the price point where comparing storage alone is actively misleading.</p>

<p><strong>At $12.99-$19.99.</strong> Households and heavy AI users. Microsoft Family is the value play for a household that wants Office apps on six accounts. Google AI Pro is the play if the Gemini limits, Deep Research, YouTube Premium Lite and Google Home Premium are worth more to you than the storage.</p>

<h2>Sync versus backup: the distinction that decides whether you need Dropbox</h2>
<p>All four services synchronise files and all four offer some form of backup, but they are not the same job and the difference matters before you pay.</p>
<p><strong>Sync</strong> means a folder that stays identical across your devices. <strong>Backup</strong> means a copy that survives your devices entirely — including deletion, corruption and ransomware. The version-history numbers in the tables above are the practical measure of backup quality: Dropbox Plus restores 30 days, Standard 180 days, Advanced a year. Apple's iCloud Backup covers iPhone and iPad data automatically when the device is on power and Wi-Fi. Google's 15 GB and paid allowances are shared across Photos, Drive and Gmail, which means a heavy Gmail user can consume the storage they bought for photos.</p>
<p>If your real fear is losing everything, cloud storage alone is not the answer — a synced folder happily synchronises a deleted or encrypted file across every device you own. This desk has written about the failure mode where <a href="/tech/cloud-storage-mistakes/">the mistakes people make with cloud storage</a> cost them files, and separately about <a href="/tech/cloud-vs-local-backup/">why cloud sync and a local backup are two different purchases</a>. The honest setup for anything irreplaceable is both.</p>

<h2>The decision framework</h2>
<p>Answer these in order and stop at the first one that applies.</p>
<p><strong>1. Do you already pay for Microsoft 365 or use Office desktop apps?</strong> Then your storage question is already answered — check whether you are on Basic (no desktop apps, 100 GB) or Personal (apps, 1 TB), because upgrading tiers may be cheaper than adding a second cloud service. If your household has more than one person needing Office, Family at 6 TB is where the maths collapses in your favour.</p>
<p><strong>2. Is your problem photos and phone backup on an iPhone?</strong> iCloud+. It is the cheapest large tier at $0.99 and $2.99, family sharing costs nothing extra, and no third-party service integrates with iOS backup as cleanly.</p>
<p><strong>3. Do you move documents with other people for work?</strong> Dropbox Plus. The transfers, version history and eSignature allowances are the product; the 2 TB is incidental. If you need more than one person, Standard's pooled 3 TB at $15 per user is the entry point, and it is a per-user cost, not a flat one.</p>
<p><strong>4. Are you actually trying to buy AI, with storage as the bonus?</strong> Google AI Plus or AI Pro. Be honest about which: AI Plus doubles Gemini limits and adds Flash Thinking; AI Pro quadruples them and adds the Pro model, Deep Research, YouTube Premium Lite and Google Home Premium. If you cannot name two features from the AI Pro list that you use, you want AI Plus.</p>
<p><strong>5. None of the above — you just need space?</strong> Buy the smallest tier that fits with headroom, from whichever service your devices already integrate with. Do not pay for a bundle you will not open. And read <a href="/tech/subscription-creep-audit/">the subscription audit</a> first, because the most common outcome of this decision is that people keep two of these services and use one.</p>

<h2>The promotional-price trap</h2>
<p>Every vendor in this comparison advertises a discount, and the discount is the least informative number on the page. Google's plans page sells annual billing as saving up to 16%; Microsoft states yearly savings of $19.89, $25.89 and $39.89 for Personal, Family and Premium — figures that are exactly twelve months of the monthly price minus the annual price, so they describe the billing cycle rather than a special offer. Separately, both companies run genuine limited-time promotions that halve the first year.</p>
<p>The number that decides your cost is the <strong>renewal</strong> price, because that is the one you pay in years two, three and four. A first-year offer that halves a $199.99 subscription is worth about $100 once; the renewal is worth $199.99 every year after. Before buying any annual plan on promotion, write down what the page says the price becomes on renewal, and decide whether you would pay that. If you would not, you are renting a discount, not buying a plan.</p>
<p>The same logic applies to the free trial attached to most of these tiers. Trials convert automatically, which is precisely the mechanism described in <a href="/tech/subscription-creep/">how subscription creep quietly rebuilds your monthly spending</a>.</p>

<h2>What to check before you pay, in order</h2>
<ul>
<li><strong>How much space you use today</strong>, from each service's own storage page — not a guess. Buy one tier above it, because photo libraries only grow.</li>
<li><strong>Whether the tier includes the apps you think it includes.</strong> Microsoft 365 Basic does not install Office. Google Basic does not include the Gemini uplift.</li>
<li><strong>Who can share the plan</strong>, and whether AI features follow the share. Microsoft explicitly limits AI to the subscription owner on Family; Google shares storage with up to five others.</li>
<li><strong>The renewal price</strong>, written down before you click buy.</li>
<li><strong>Whether you can export everything.</strong> Before committing years of files, confirm you can download the lot. This is a five-minute test now and a hostage negotiation later.</li>
</ul>

<p><em>Prices on this page are US list prices read from each vendor's own pricing page on 15 September 2026. Cloud storage pricing is volatile and heavily promoted; treat every figure as a snapshot and re-check the vendor page before buying. Nothing here is a claim that one service is universally best — they are selling different products at similar prices, and the right one depends on which product you actually want.</em></p>""",
     [("Google One — Plans & pricing", "https://one.google.com/about/plans"),
      ("Microsoft — Compare all Microsoft 365 products", "https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products"),
      ("Microsoft — OneDrive plans and pricing", "https://www.microsoft.com/en-us/microsoft-365/onedrive/onedrive-plans-and-pricing"),
      ("Dropbox — Plans", "https://www.dropbox.com/plans"),
      ("Apple — iCloud+", "https://www.apple.com/icloud/")],
     [("cloud-storage-mistakes", "The cloud storage mistakes that cost people files"),
      ("cloud-vs-local-backup", "Cloud sync vs a local backup: two different purchases"),
      ("subscription-creep-audit", "The subscription audit: find every recurring charge"),
      ("microsoft-365-free-vs-paid", "Microsoft 365: free vs paid, tier by tier"),
      ("subscription-creep", "How subscription creep rebuilds your monthly spending")]),
]
