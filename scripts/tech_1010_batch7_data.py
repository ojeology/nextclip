# -*- coding: utf-8 -*-
"""Tech 10/10 brief batch 7 — Tier 1 #9: PayPal vs Wise vs Payoneer.

Why this piece exists
---------------------
Tier 1 #9 of the 10/10 content research brief, and the last open Tier 1 item.
The brief specifically warns that financial topics need jurisdiction-specific
sources and no global claims, because Wise and Payoneer fee schedules vary by
corridor and currency. That warning turned out to be the whole story: the three
products do not behave the same way at all once you ask where the recipient's
bank account is, and for a Nigeria-weighted audience the differences are not
marginal - one of the three cannot receive in naira at all.

Verification receipts (all checked live 2026-09-15)
---------------------------------------------------
- Wise Help Centre, "What currencies can I send to and from?"
  https://wise.com/help/articles/2571907/what-currencies-can-i-send-to-and-from
  Two lists. The first is "currencies you can send money to and from" and
  contains USD, GBP, EUR, CAD, AUD and 20-odd others. The second is "currencies
  you can only send money to (via local transfer)". NGN - Nigerian Naira - is in
  the SECOND list, annotated "Within Nigeria." That is the decisive fact in this
  whole comparison and it is first-party: you cannot hold, receive into, or pay
  out from an NGN balance with Wise. You can only send NGN to a Nigerian bank
  account.

- Wise Help Centre, "Guide to NGN transfers"
  https://wise.com/help/articles/2jVJxXsvpfBLkvb6RpOGk5/guide-to-ngn-transfers
  NGN can be sent to personal and business bank accounts in Nigeria; up to
  95,000,000 NGN per transfer; once Wise receives and converts the money it
  usually arrives the same working day; conversion can take up to 2 working
  days; NIBSS (Nigeria Inter-Bank Settlement System) may take up to 24 hours to
  confirm payment status.

- Payoneer, "Pricing" — page footer states "Last updated on 1 January 2026"
  https://www.payoneer.com/pricing/
  Full first-party fee schedule, quoted verbatim into the piece: receive from
  another Payoneer balance Free; marketplaces varies; receiving account in your
  local currency Free; receiving account in a non-local currency 1% (minimum
  1.00 USD); credit card up to 3.99% + 0.49 USD; ACH (US only) 1%; EU/UK bank
  account 1%; PayPal (US only) up to 3.99% + 0.49 USD. Withdrawal to a bank in
  the same country in local currency 1.50 USD — with a published list of
  supported countries in which NIGERIA DOES NOT APPEAR (Kenya does). Withdrawal
  in the recipient's local currency 1.2%-4% with, in some countries, a minimum
  fee of up to 20.00 USD; withdrawal with conversion 1.2%-4%. Moving funds
  between your own Payoneer balances 0.50%. Annual card fee 29.95 USD; card
  purchases with conversion up to 3.5%; ATM 3.15 USD + up to 1.8%/3.5%.
  Annual account fee 29.95 USD, applying ONLY if the account receives less than
  6,000.00 USD or equivalent in any 12 consecutive months, and not charged in
  the first year for paid annual plans.
  This resolved a live conflict in secondary coverage: several 2026 articles
  state the annual-fee threshold as $2,000 received per year, and one states the
  conversion fee as a flat 4.5% with a 3% withdrawal. Payoneer's own page says
  $6,000 and a 1.2%-4% band. Primary won; the secondary figures were dropped.

- Paga press release, "PayPal Goes Live in Nigeria Through Paga, Enabling
  Payments and Local Withdrawals", LAGOS, 27 January 2026
  https://paga.blog/2026-01-27/paypal-goes-live-in-nigeria-through-paga-enabling-payments-and-local-withdrawals/
  A joint announcement: it carries direct quotes from Tayo Oviosu (Founder and
  Group CEO, Paga) and Otto Williams (SVP, Regional Head and General Manager,
  PayPal Middle East and Africa), plus PayPal's PR contact at Edelman. Live
  account linking for customers in Nigeria; users link PayPal to a Paga wallet
  to receive cross-border payments from PayPal-supported markets, access PayPal
  balances, and withdraw locally - spend via card, transfer to local bank
  accounts, or pay bills and merchants inside the Paga ecosystem. Nigerian
  merchants can reach PayPal's 400m+ users. Access via the Paga app or
  www.paga.com. Paga founded 2009, 21m+ users, Paga Engine used by 400+
  businesses including Meta, LemFi, Qatar Airways and Verto; in 2025 Paga Group
  processed 169m transactions worth over 17 trillion naira (US$11 billion).
  Market context in the release: Nigerian digital payment values of 657.8
  trillion naira in 2023 and 30m+ active mobile wallet users (Novatia
  Consulting, 2024).

- PayPal, "Global | List of Countries and Currencies"
  https://www.paypal.com/ng/webapps/mpp/country-worldwide
  Confirms PayPal maintains a Nigeria-country surface (/ng/) and lists Nigeria
  among supported African countries. NOTE: I attempted to read whether Nigeria
  is hyperlinked to a local /home destination in that list, as a signal of full
  versus limited functionality. My extraction was ambiguous and I could not
  verify it reliably, so that detail is deliberately NOT used in the piece
  rather than guessed at.

- PayPal Community, staff answer, thread "Can I use PayPal to receive payments
  here in Nigeria" (2023-2024)
  https://www.paypal-community.com/t5/Transactions/Can-I-use-Paypal-to-receive-payments-here-in-Nigeria/td-p/3072173
  "When you open an account with PayPal, the country you register should be your
  current residence and where you will be operating the account from. If your
  country of registration is Nigeria, unfortunately you are unable to receive
  payments via PayPal regardless of where your business is registered." Also:
  "I can confirm there is not an option to receive funds through PayPal in
  Nigeria." Used ONLY to establish the pre-2026 position, and dated as such in
  the piece, because the Paga integration supersedes it.

Deliberately NOT claimed
------------------------
- No fees for the PayPal -> Paga -> naira route. The joint release announces the
  capability and quotes both executives but publishes no fee schedule, no
  exchange-rate basis and no withdrawal charge. Contemporaneous trade coverage
  describes conversion at "willing-buyer, willing-seller" rates, but that is
  secondary, so the piece says the capability exists and that the cost must be
  read in-app before you rely on it.
- No PayPal fee schedule for Nigeria. PayPal's Nigeria fee pages were not
  retrievable as first-party text, so the piece does not state PayPal
  percentages at all. Where it discusses cost on the PayPal route it says so
  qualitatively and points at the in-app quote.
- No single "cheapest" verdict, and no universal claim that any of the three
  works everywhere. Per the brief's factual-language rule the piece ranks by
  situation and by jurisdiction, and states that Payoneer's own page says fees
  depend on sender and recipient locations, payment method, currency corridor,
  account type, onboarding channel and agreement.
- The widely repeated claim that "Wise suspended USD transfers to Nigeria in
  November 2022" is NOT asserted. Wise's current help centre lists NGN as a
  supported send-to currency with a published per-transfer ceiling, which
  contradicts a blanket suspension. The piece handles this by stating what the
  current first-party page says, noting that corridor availability changes, and
  telling the reader to check the live route in-app - rather than picking a side
  between a 2022 news claim and a 2026 help page.
- Every worked cost figure is plain arithmetic on the providers' own published
  bands and prices, given as a RANGE wherever the provider publishes a range,
  and labelled as arithmetic in the text. No point estimates are invented from
  a band.
- Secondary fee tables (monito, cenoa, abokiforex, worldfirst, kachiplug) were
  read and are the reason I went to the primary pages: they disagree with each
  other by several percentage points and with Payoneer's own schedule. None are
  cited in the piece.
"""

BATCH_1010_B7 = [

    # ------------------------------------------------------------------ #
    # Tier 1 #9: PayPal vs Wise vs Payoneer
    # ------------------------------------------------------------------ #
    ("paypal-vs-wise-vs-payoneer", "subscriptions", "guide",
     "PayPal vs Wise vs Payoneer: which one actually gets you paid, and where each stops working",
     "The three are not interchangeable, and the deciding factor is not fee percentage but which country your bank account is in. Wise cannot receive in naira at all; PayPal gained a Nigerian receiving route only in January 2026; Payoneer works, with the most fee surfaces.",
     """<p>These three get compared constantly and the comparison is usually wrong, because it treats them as three versions of the same product. They are not. PayPal is a consumer wallet and checkout network. Wise is a transfer service that moves money between bank accounts. Payoneer is a business receivables platform that gives you receiving account details, marketplace integrations, a card and withdrawals.</p>

<p><strong>In one line:</strong> the question is not "which is cheapest". It is "which one can actually receive money in the country where my bank account is". For a recipient in Nigeria the answers diverge sharply — Wise cannot receive in naira at all, PayPal only gained a Nigerian receiving route on 27 January 2026 through a partnership with Paga, and Payoneer is the one that issues you receiving account details and pays out to a Nigerian bank, at the cost of the most fee surfaces of the three.</p>

<p>Everything below was read from the providers' own pages on <strong>15 September 2026</strong>: Wise's help centre, Payoneer's pricing page (which states it was last updated 1 January 2026), and the joint Paga/PayPal press release of 27 January 2026. Where a figure could not be confirmed first-party, that is stated instead of estimated.</p>

<h2>Wise: the restriction that decides everything</h2>
<p>Wise's help centre publishes two lists under "What currencies can I send to and from?" The first is currencies you can send to <em>and from</em> — USD, GBP, EUR, CAD, AUD and about twenty others. The second is currencies you can <strong>only send to</strong>, via local transfer.</p>

<p><strong>NGN, the Nigerian naira, is in the second list</strong>, annotated "Within Nigeria."</p>

<p>That single placement settles most of the comparison for anyone banking in Nigeria. It means with Wise you cannot hold a naira balance, you cannot receive a payment into naira, and you cannot pay out from naira. What you can do is have money <em>sent</em> into naira, from another currency, landing in a Nigerian bank account.</p>

<p>Wise's NGN transfer guide gives the mechanics: you can send NGN to personal and business bank accounts in Nigeria; the ceiling is <strong>95,000,000 NGN per transfer</strong>; once Wise has received and converted the money it usually arrives in the recipient's bank account the same working day; conversion itself can take up to two working days; and NIBSS, the Nigeria Inter-Bank Settlement System, may take up to 24 hours to confirm payment status.</p>

<p>So the correct way to think about Wise in Nigeria is a reframe rather than a comparison: <strong>Wise is a tool your client uses to pay you, not a wallet you receive into.</strong> If someone abroad owes you money and can pay by bank transfer, asking them to send naira to your Nigerian account via Wise is often the strongest option available — Wise charges a visible fee and converts at the mid-market rate, and the cost sits with the sender rather than being buried in a spread you never see.</p>

<p>One caution on currency here. You may find older articles claiming Wise suspended transfers to Nigeria. Wise's current help centre lists NGN as a supported send-to currency with a published per-transfer ceiling, which is not consistent with a blanket suspension. Corridor availability does change, and providers adjust routes without press releases, so the reliable move is to start a transfer in the app and read the live route, fee and rate it offers before you promise a client a method.</p>

<h2>PayPal in Nigeria: what actually changed on 27 January 2026</h2>
<p>For roughly two decades the position was simple and bleak. PayPal Community staff put it plainly in a 2023 answer: "When you open an account with PayPal, the country you register should be your current residence and where you will be operating the account from. If your country of registration is Nigeria, unfortunately you are unable to receive payments via PayPal regardless of where your business is registered." Another answer in the same thread: "I can confirm there is not an option to receive funds through PayPal in Nigeria."</p>

<p>That changed. On <strong>27 January 2026</strong>, Paga and PayPal issued a joint announcement from Lagos confirming "the availability of live account linking for customers in Nigeria."</p>

<p>What the release says the integration does:</p>
<ul>
<li>Users in Nigeria can <strong>link their PayPal accounts directly to their Paga wallets</strong> to receive cross-border payments from PayPal-supported markets.</li>
<li>They can <strong>access their PayPal balances</strong> and withdraw funds for everyday needs — spending via card, transferring to local bank accounts, or paying bills and merchants within the Paga ecosystem.</li>
<li>They can <strong>shop with global PayPal merchants</strong>.</li>
<li>Nigerian merchants and entrepreneurs can reach <strong>PayPal's global network of over 400 million users</strong>.</li>
<li>Access is through the <strong>Paga app or www.paga.com</strong>: log in, link the PayPal account, start receiving.</li>
</ul>

<p>The release is genuinely joint rather than a partner claiming a relationship — it carries quotes from Tayo Oviosu, Founder and Group CEO of Paga, and from Otto Williams, Senior Vice President, Regional Head and General Manager of PayPal Middle East and Africa, and lists PayPal's public-relations contact at Edelman. Paga was founded in 2009, has over 21 million users, runs Paga Engine infrastructure used by more than 400 businesses including Meta, LemFi, Qatar Airways and Verto, and processed 169 million transactions worth over ₦17 trillion (about US$11 billion) in 2025.</p>

<p><strong>What the release does not say is what it costs.</strong> There is no fee schedule, no exchange-rate basis and no withdrawal charge published for the PayPal-to-Paga-to-naira route. That is a real gap, and the honest reading is that the capability now exists while the price of using it has to be read on screen before you commit. If PayPal is your only option because that is how a client pays, link the accounts, run one small payment through, and record exactly what arrived versus what was sent before you quote that method to anyone else.</p>

<p>It is also worth being precise about what this is: account linking through a regulated local partner. It is not the same thing as a Nigerian PayPal account having the full feature set of a US or UK one, and the release does not claim that it is.</p>

<h2>Payoneer: the published fee schedule, and the country list that matters</h2>
<p>Payoneer's pricing page is the most transparent of the three for Nigeria, and it states it was last updated on 1 January 2026. These are its own figures.</p>

<p><strong>Receiving money into your Payoneer account:</strong></p>
<ul>
<li>From another customer's Payoneer balance — <strong>free</strong>.</li>
<li>From marketplaces and integrated platforms — <strong>varies by marketplace</strong>.</li>
<li>Via a receiving account in your local currency — <strong>free</strong>.</li>
<li>Via a receiving account in a currency that is not your local currency — <strong>1%</strong>, minimum fee 1.00 USD or equivalent.</li>
<li>From a payer using a credit card — <strong>up to 3.99% + 0.49 USD</strong>.</li>
<li>From a payer using ACH bank debit (US only) — <strong>1%</strong>.</li>
<li>From a payer using an EU or UK bank account — <strong>1%</strong>.</li>
<li>From a payer using PayPal (US only) — <strong>up to 3.99% + 0.49 USD</strong>.</li>
</ul>

<p><strong>Withdrawing to a bank account:</strong></p>
<ul>
<li>To a bank account in the same country as yours, in local currency, in supported countries — <strong>1.50 USD</strong>. Payoneer publishes the supported list, and it is worth reading carefully: all EU countries, USA, Australia, Bulgaria, Canada, China, Czech Republic, Japan, Kenya, South Korea, Mexico, Malaysia, Norway, New Zealand, Philippines, Poland, Romania, Saudi Arabia, Sweden, Singapore, Thailand, Vietnam, the UK and a handful of territories. <strong>Nigeria is not on that list.</strong></li>
<li>To a bank account in the recipient's local currency with no conversion — <strong>1.2% to 4%</strong>, and in some countries a minimum fee of up to 20.00 USD or equivalent may apply.</li>
<li>To a bank account in the recipient's non-local currency, with conversion — <strong>1.2% to 4%</strong>.</li>
</ul>

<p><strong>Other fees that catch people out:</strong></p>
<ul>
<li>Moving funds between your own Payoneer balances — <strong>0.50%</strong>. This is separate from the withdrawal fee, so converting inside the platform and then withdrawing can stack two charges.</li>
<li><strong>Annual account fee of 29.95 USD</strong>, which applies only if the account receives less than <strong>6,000.00 USD</strong> or equivalent in any 12 consecutive months, and is not charged in the first year for paid annual plans.</li>
<li>Annual card fee <strong>29.95 USD</strong>; standard card delivery free; additional virtual cards free; replacing a card 12.95 USD.</li>
<li>Card purchases without currency conversion up to <strong>1.8%</strong>, free where the merchant country matches the card issuing country; card transactions with conversion up to <strong>3.5%</strong>.</li>
<li>ATM cash withdrawals 3.15 USD plus up to 1.8% in the same currency, or plus up to 3.5% with conversion; checking an ATM balance or an ATM decline costs 1.00 USD.</li>
</ul>

<p>Payoneer is explicit that these are ranges and that the real number depends on the corridor: fees depend on sender and recipient locations, payment method, currency, account type, onboarding channel and agreement, certain account types in specific regions require an Annual Plan, a registration fee may apply in certain countries, and the exact fee is always displayed before you confirm a payment inside your account. Full details live on the fees page once signed in.</p>

<p>If you see a Payoneer fee table elsewhere quoting a flat 4.5% conversion, a 3% withdrawal, or a $2,000 annual-fee threshold, it disagrees with Payoneer's own page. Check the page rather than the article.</p>

<h2>What a $1,000 invoice actually costs on each route</h2>
<p>This is plain arithmetic on the providers' own published figures, and it is given as a range wherever the provider publishes a range, because pretending to more precision than they do would be fabrication.</p>

<p><strong>Payoneer, client pays into your USD receiving account, you withdraw to a Nigerian bank in naira.</strong> For a Nigerian recipient a USD receiving account is not the local currency, so receiving costs 1% = <strong>$10</strong>. Withdrawing with conversion falls in the 1.2%–4% band = <strong>$12 to $40</strong>, and in some countries a minimum fee of up to $20 can apply instead, which matters most on small invoices. If you moved money between balances first, add 0.50% = <strong>$5</strong>. Total roughly <strong>$22 to $55</strong>, or about <strong>2.2% to 5.5%</strong> of the invoice. If you receive under $6,000 in a rolling 12 months, add the <strong>$29.95</strong> annual account fee — across six $1,000 invoices in a year that is another half a percentage point.</p>

<p><strong>Wise, client sends naira to your Nigerian bank account.</strong> Your cost as the recipient is normally nothing at your end, because the sender pays Wise's visible fee and the conversion happens at the mid-market rate. The number that matters is the one your client sees before they confirm, and it is corridor-specific. The structural point is that the cost is disclosed to the person paying it rather than deducted invisibly from you — which is why, where a client is willing to pay by bank transfer, this route frequently beats the alternatives.</p>

<p><strong>PayPal, via the Paga link.</strong> Not calculable from published data, because the joint release publishes no fees for the route. Treat any percentage you read online for this corridor as unverified until you have seen it in the app.</p>

<h2>The decision framework</h2>
<p>Work down and stop at the first that matches your situation.</p>

<p><strong>1. A client says "I'll PayPal you" and you bank in Nigeria.</strong> Link your PayPal account to a Paga wallet. That route went live on 27 January 2026 and is the only sanctioned way to receive PayPal funds into naira. Run one small payment first and record what was sent versus what arrived, because the fee is not published.</p>

<p><strong>2. You are paid by a marketplace — Upwork, Fiverr, Amazon and similar.</strong> Payoneer, because its receiving accounts and platform integrations are built for exactly this. Note that Payoneer states marketplace fees vary by platform, and the marketplace's own commission is separate from anything Payoneer charges.</p>

<p><strong>3. A client can pay by bank transfer and you want naira in a Nigerian bank.</strong> Ask them to send NGN via Wise to your account. Ceiling 95,000,000 NGN per transfer, usually same working day once converted, and the cost sits with the sender as a visible fee at the mid-market rate. This is the route most people overlook because they assume Wise is a wallet they should open themselves.</p>

<p><strong>4. You need to hold USD, GBP or EUR and spend internationally without converting each time.</strong> Payoneer's receiving accounts plus its card. Budget for the $29.95 annual card fee and up to 3.5% on card transactions involving conversion — card spend is where a receiving platform quietly becomes expensive.</p>

<p><strong>5. You receive less than $6,000 a year through Payoneer.</strong> The $29.95 annual account fee applies. On low volumes that is a meaningful percentage, so either factor it into your pricing or prefer a route without it. It is waived in the first year for paid annual plans, and it does not apply at all once you cross the threshold in any 12 consecutive months.</p>

<p><strong>6. You bank outside Nigeria.</strong> All three can receive, and the comparison changes completely: Wise gives you local account details in the currencies it supports both ways, Payoneer competes on marketplace reach, and PayPal competes on how many buyers already have an account. Compare on the specific corridor you actually use, not on headline claims — Payoneer's own page says fees depend on sender and recipient locations, and Wise's own pages split currencies into those it can both send to and from versus those it can only send to.</p>

<h2>What to check before you commit to a platform</h2>
<ul>
<li><strong>Which country your account is registered in.</strong> This determines your capabilities more than any other variable. PayPal's own guidance is that the country you register should be your current residence and where you operate the account from. Registering in a jurisdiction you do not live in to unlock features breaches the provider's terms and puts the balance at risk.</li>
<li><strong>Receiving, holding and withdrawing are three separate features.</strong> Confirm each one individually. Wise can send to naira but cannot hold it. PayPal in Nigeria can now receive via Paga but the release makes no claim about holding foreign-currency balances locally.</li>
<li><strong>Whether the provider publishes fees for your corridor.</strong> Payoneer publishes bands and shows the exact fee before you confirm. Wise shows the fee and rate before you send. The PayPal/Paga release publishes nothing, so ask in-app.</li>
<li><strong>The currency you will actually be settled in, and at which rate.</strong> In naira especially, the difference between an official rate and a market rate can exceed the entire fee. Ask which rate applies and compare the amount that lands, not the percentage quoted.</li>
<li><strong>Whether you want foreign currency to stay foreign.</strong> Withdrawing USD to a domiciliary account avoids a conversion you may not want; converting to naira is convenient but final. Decide before you withdraw, because the fee differs by route.</li>
<li><strong>Threshold fees.</strong> Payoneer's $29.95 annual account fee below $6,000 received, and its separate $29.95 annual card fee, are the two that surprise people. Both are on the public pricing page.</li>
<li><strong>Minimum fees on small invoices.</strong> Payoneer's 1% receiving fee carries a 1.00 USD minimum, and some withdrawal corridors carry a minimum of up to 20.00 USD. On a $50 payment a minimum fee is a far larger percentage than on a $5,000 one.</li>
<li><strong>KYC requirements before you need the money urgently.</strong> Verification for Nigeria-routed services involves identity and address checks and is not instant. Set the account up before the first invoice is due, not after.</li>
</ul>

<p>Whichever route you choose, the money arriving is income with a recurring cost attached, and those costs compound quietly. This desk has a worked method for finding every recurring charge in <a href="/tech/subscription-creep-audit/">how to audit every subscription you are actually paying for</a>, and the same discipline applies to platform fees: write down what was sent and what landed, every time, and you will see the real percentage within a month. If you are also carrying tool costs for the work itself, <a href="/tech/web-hosting-costs-explained/">what a small website actually costs per year</a> puts the platform fee in proportion, and <a href="/tech/free-trial-traps/">how free trials convert into paid subscriptions</a> covers the billing pattern that catches most people at least once.</p>

<p><em>Everything on this page was read from Wise's help centre, Payoneer's own pricing page (last updated 1 January 2026) and the joint Paga/PayPal press release of 27 January 2026, all checked on 15 September 2026. Fee bands are ranges the providers publish; your actual fee depends on corridor, currency, payment method, account type, onboarding channel and agreement, and is shown before you confirm. PayPal/Paga route fees are not published and are not estimated here. Nothing on this page is a claim that one provider is universally cheapest or works everywhere — capability is jurisdiction-specific, and the right answer changes with where your bank account is.</em>""",
     [("Wise Help Centre — What currencies can I send to and from?", "https://wise.com/help/articles/2571907/what-currencies-can-i-send-to-and-from"),
      ("Wise Help Centre — Guide to NGN transfers", "https://wise.com/help/articles/2jVJxXsvpfBLkvb6RpOGk5/guide-to-ngn-transfers"),
      ("Payoneer — Pricing (last updated 1 January 2026)", "https://www.payoneer.com/pricing/"),
      ("Paga — PayPal goes live in Nigeria through Paga (joint press release, 27 January 2026)", "https://paga.blog/2026-01-27/paypal-goes-live-in-nigeria-through-paga-enabling-payments-and-local-withdrawals/"),
      ("PayPal — Global list of countries and currencies", "https://www.paypal.com/ng/webapps/mpp/country-worldwide"),
      ("PayPal Community — staff answer on receiving payments in Nigeria (2023, pre-dates the Paga integration)", "https://www.paypal-community.com/t5/Transactions/Can-I-use-Paypal-to-receive-payments-here-in-Nigeria/td-p/3072173")],
     [("subscription-creep-audit", "How to audit every subscription you actually pay for"),
      ("web-hosting-costs-explained", "What a small website really costs per year"),
      ("free-trial-traps", "How free trials quietly become paid subscriptions"),
      ("remote-work-free-tools", "Free tools for working remotely"),
      ("cloud-storage-plans-compared", "Cloud storage compared, plan by plan")]),
]
