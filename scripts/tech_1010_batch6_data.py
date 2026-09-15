# -*- coding: utf-8 -*-
"""Tech 10/10 brief batch 6 — Tier 1 #7: ChatGPT Free vs Paid.

Why this piece exists
---------------------
Tier 1 #7 of the 10/10 content research brief, and the highest-volume
commercial-intent query in the AI cluster: people are not asking whether
ChatGPT works, they are asking whether to pay, and if so which tier. BRYME
already had `chatgpt-vs-claude-vs-gemini`, `free-ai-tools-worth-using`,
`ai-assistants-compared` and `deepseek-vs-chatgpt`, but nothing that walks
OpenAI's own plan ladder and says what each step actually buys.

Verification receipts (all checked live 2026-09-15)
---------------------------------------------------
Everything below was read off OpenAI's own pages on the date above. Six
first-party sources, five of them fetched directly:

- https://chatgpt.com/pricing/  (redirects from openai.com/chatgpt/pricing/)
  Full plan-by-plan comparison matrix for Free / Go / Plus / Pro: model access,
  context windows, feature availability, privacy, and the security/admin block
  that is "No" on all four individual plans. Also the FAQ: "Paid plans (Go,
  Plus, Business, and Enterprise) are priced per user per month. We offer
  monthly plans for Go, Plus and Business and annual plans for Business and
  Enterprise." NOTE: the dollar figures on the plan cards are rendered client
  side and are absent from the retrieved markup, so no price was read off this
  page. Prices came from the help-centre articles below instead.

- https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus
  "ChatGPT Plus is a subscription plan that provides enhanced access to the
  ChatGPT web app for $20/month"; "Price: $20/month (billed monthly)";
  "we do not support annual billing or the option to pay for multiple months in
  advance". Page showed "Updated: 30 minutes ago" at the time of checking.

- https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
  "Pro $100 unlocks 5x higher usage than Plus, while Pro $200 unlocks 20x usage
  than Plus." Carried a banner dated 10 September 2026 pausing new Pro $200
  sign-ups and upgrades. Page showed "Updated: 1 hour ago" at the time of
  checking.

- https://help.openai.com/en/articles/11989085-what-is-chatgpt-go
  Go's inclusions, "ChatGPT Go does not include GPT-5.6 Sol", "Access to legacy
  models is not included", voice "with the same usage limits as the Free tier",
  "All purchases are in USD", and "Subscription prices can be found in the
  ChatGPT pricing page" — i.e. OpenAI does not state Go's price in text.

- https://help.openai.com/en/articles/20001047-ads-in-chatgpt
  "Ads may appear for users on the Free and Go plans. Plus, Pro, Business,
  Enterprise, and Edu accounts will not have ads." US test began 9 February
  2026. Under-18 accounts excluded. No ads near personal health, mental health
  or politics; no political advertising. Controls in Settings > Ad Controls.
  Personalised ads not initially available in the EEA or Switzerland. Page
  showed "Updated: 18 hours ago".

- https://help.openai.com/en/articles/6825453-chatgpt-release-notes
  Dated, per-plan limits: 9 Sept 2026 voice allowances (Go 3h GPT-Live-1 mini,
  Plus 3h GPT-Live-1, Pro $100 15h, Pro $200 unlimited) — which also confirms
  the two Pro prices in OpenAI's own words; 14 May 2026 Library storage
  (Free 500 MB, Go 4 GB, Plus and Business 20 GB, Pro 100 GB); 3 Sept 2025
  project file uploads (Free 5, Plus/Go/Edu 25, Pro/Business/Enterprise 40);
  11 Sept 2026 planned custom-GPT retirement; 18 Aug 2025 Go's India launch at
  INR 399/month GST included; 22 Sept 2025 Indonesia at IDR 75,000/month.
  Page showed "Updated: 11 hours ago".

Deliberately NOT claimed
------------------------
- Go's US dollar price. Nine independent secondary sources converge on
  $8/month and several date their reading of OpenAI's pricing page, but OpenAI
  states no figure in text anywhere reachable, and the pricing page renders it
  in client-side JS that a plain fetch does not return. The piece therefore
  labels $8 as the widely reported US list price, says plainly that OpenAI's
  own help article defers to the pricing page, and notes the first-party
  evidence that Go is priced locally (INR 399 in India, IDR 75,000 in
  Indonesia) so no single figure is universal. Business and Enterprise per-seat
  prices are handled the same way: the first-party facts kept are "per user per
  month", "annual plans for Business and Enterprise" and "starting at 2 users".
- No claim about how many messages any plan allows. OpenAI publishes
  multipliers and context windows, not message counts, and states that
  allowances "may change dynamically" and differ per model. Where the piece
  uses "5x" and "20x" it is quoting OpenAI's own wording.
- No claim that ads are live outside the US. The help article describes a test
  that began in the US on 9 February 2026 and is expanding in phases, with a
  separate Ads Manager Availability page for country status.
- No "best plan" verdict. Per the brief's factual-language rule the piece ranks
  by situation. It also flags a live inconsistency between OpenAI's own pages:
  the Go help article still says ads "may" be tested in future, while the
  pricing card and the Ads article say ads may already appear on Go.
- Usage-per-dollar figures are plain division of OpenAI's own published
  multipliers and prices, labelled as arithmetic in the text, not sourced
  claims.
"""

BATCH_1010_B6 = [

    # ------------------------------------------------------------------ #
    # Tier 1 #7: ChatGPT Free vs Paid
    # ------------------------------------------------------------------ #
    ("chatgpt-free-vs-paid", "ai", "guide",
     "ChatGPT free vs paid: what Go, Plus and Pro actually change, plan by plan",
     "The free tier is genuinely usable and the $20 tier is the one that changes what ChatGPT can do. The $8 tier mostly changes how often you can do it — and it does not remove the ads.",
     """<p>OpenAI now sells four individual plans, and the gaps between them are not where most comparison articles put them. The question is not "free versus paid". It is <em>which</em> paid, because the cheapest paid tier and the standard paid tier buy two completely different things: one buys volume, the other buys capability.</p>

<p><strong>In one line:</strong> if you use ChatGPT a few times a week, stay on Free — it is not a crippled demo. If you are hitting limits and want the stronger models and no ads, Plus at $20 a month is the tier that changes what the tool can do. Go at $8 raises your allowances but keeps you on the same model family as Free and, on OpenAI's own account, may still show you ads. Pro is for people who reliably exhaust Plus, and as of 10 September 2026 the $200 Pro tier is paused for new purchases.</p>

<p>Everything below was read from OpenAI's own pricing page and help centre on <strong>15 September 2026</strong>. Where a figure could not be confirmed first-party, that is stated rather than papered over.</p>

<h2>The four plans and what they cost</h2>
<p><strong>Free — $0.</strong> Unlimited everyday text chats with GPT-5.6 Luna, subject to what OpenAI calls abuse guardrails. Limited messages with uploads, limited and slower image generation, limited voice chats, limited deep research, limited memory and context, limited Codex access.</p>

<p><strong>Go — widely reported at $8 a month in the US.</strong> Everything in Free plus more messages with tools, more uploads, more image creation, more voice chats and longer memory. Billed monthly, cancel anytime. OpenAI's pricing card for Go carries the line "This plan may include ads."</p>

<p><strong>Plus — $20 a month, billed monthly.</strong> This one is stated in plain text by OpenAI's own help article: "ChatGPT Plus is a subscription plan that provides enhanced access to the ChatGPT web app for $20/month." Adds the advanced reasoning models, expanded messages and uploads, more accurate image creation, expanded deep research, expanded memory and context, projects, scheduled tasks, custom GPTs, expanded Codex usage and early access to new features.</p>

<p><strong>Pro — $100 or $200 a month.</strong> OpenAI's Pro article states the distinction directly: "Pro $100 unlocks 5x higher usage than Plus, while Pro $200 unlocks 20x usage than Plus." Same core capabilities on both; the difference is allowance.</p>

<p><strong>There is no annual discount on any of them.</strong> Three separate OpenAI help articles repeat the same sentence: "we do not support annual billing or the option to pay for multiple months in advance for ChatGPT Go, Plus, or Pro subscriptions." Annual billing exists on Business and Enterprise, which are priced per user per month and, per the pricing FAQ, start at two users.</p>

<p>Two first-party routes to free or reduced access are worth knowing about before you pay anything: <strong>ChatGPT for Teachers</strong> is free for verified US K-12 educators through June 2027, and <strong>OpenAI for Nonprofits</strong> offers up to a 75% discount on Business or Enterprise.</p>

<h2>The gap that actually decides it: model access, not message count</h2>
<p>Most people compare plans on how much they can send. That is the wrong axis, because OpenAI gates the <em>models</em> by tier, and the model determines what the tool is capable of rather than how often you can use it.</p>

<p>From OpenAI's own plan comparison table:</p>
<ul>
<li><strong>GPT-5.6 Luna</strong> — available on all four plans. This is what Free runs, and it is what Go's Think mode uses.</li>
<li><strong>GPT-5.6 Terra</strong> — Free and Go get "limited access in Work and Codex on desktop". Plus gets it, Pro gets it unlimited.</li>
<li><strong>GPT-5.6 Sol</strong> — Free: no. Go: no. Plus: yes. Pro: unlimited.</li>
<li><strong>GPT-6 Astra</strong> — Free: no. Go: no. Plus: yes. Pro: expanded.</li>
<li><strong>GPT-5.6 Sol Pro</strong> — Pro only. Not on Free, Go or Plus at any price below $100.</li>
<li><strong>Legacy models</strong> — Free: no. Go: no. Plus and Pro: yes.</li>
</ul>

<p>OpenAI's Go article says this explicitly, in case the table is skimmed: "Think uses GPT-5.6 Luna. ChatGPT Go does not include GPT-5.6 Sol." And separately, "Access to legacy models is not included with the ChatGPT Go subscription."</p>

<p>So the $8 tier and the free tier are running the same headline model. <strong>The step from Go to Plus is the step that changes what ChatGPT can reason with.</strong> If your reason for paying is better answers on hard problems — code, analysis, multi-step planning — Go does not buy that. Plus does.</p>

<p>Response times follow the same split: Free and Go are listed as "limited on bandwidth &amp; availability", Plus and Pro as "fast".</p>

<h2>The ads line: the clearest reason to pay $20 rather than $8</h2>
<p>This is the fact most comparison articles miss, and OpenAI states it without hedging in its ads help article: <strong>"Ads may appear for users on the Free and Go plans. Plus, Pro, Business, Enterprise, and Edu accounts will not have ads."</strong></p>

<p>Paying $8 does not make the advertising go away. Paying $20 does.</p>

<p>The details, all first-party, matter if you are deciding how much this bothers you:</p>
<ul>
<li>The test began in the US on <strong>9 February 2026</strong> and is expanding in phases; OpenAI maintains a separate Ads Manager Availability page for country status.</li>
<li>Ads appear <strong>below the end of a response</strong>, labelled as sponsored and visually separated from the answer.</li>
<li>OpenAI states ads <strong>do not influence ChatGPT's answers</strong>, run on separate systems from the chat model, and that advertisers cannot shape, rank or alter responses.</li>
<li>Conversations are <strong>not shared with advertisers</strong> and data is never sold to them; advertisers receive only aggregated, non-identifying performance figures such as total views or clicks.</li>
<li>No ads are shown to accounts identified as belonging to people <strong>under 18</strong>.</li>
<li>Ads are not eligible near sensitive or regulated topics including <strong>personal health, mental health and politics</strong>, and political advertising is not allowed.</li>
<li>During the test, ads do <strong>not</strong> appear in the ChatGPT Atlas browser.</li>
<li>Controls live in <strong>Settings &gt; Ad Controls</strong>: turn off personalisation, dismiss an ad and give feedback, see why you were shown it, and clear the data used for ads. Turning off personalisation still leaves context-based ads from the current thread.</li>
<li>Personalised ads were <strong>not initially available in the EEA or Switzerland</strong>, and ad controls are only offered to Free and Go users in regions where ads are available or arriving.</li>
</ul>

<p>One honest wrinkle: OpenAI's pages currently disagree with each other. The Go help article, last updated about four weeks before this was checked, still says "We may start testing ads in ChatGPT Go in the future", while the pricing page's Go card says "This plan may include ads" and the ads article says ads may appear on Go today. Read together, the safe assumption for a buyer is that <strong>Go is inside the ad-supported group</strong>, and that this is exactly the sort of detail worth re-checking on the day you subscribe.</p>

<h2>The concrete numbers, plan by plan</h2>
<p>OpenAI publishes context windows and dated per-feature allowances rather than message counts. These are the figures that let you compare the tiers on something measurable.</p>

<p><strong>Context window</strong> (from the pricing comparison table):</p>
<ul>
<li>GPT Instant total context — Free <strong>27K</strong>, Go <strong>54K</strong>, Plus <strong>54K</strong>, Pro <strong>128K</strong>.</li>
<li>GPT Instant input maximum — Free <strong>about 12 pages</strong> of text, Go and Plus <strong>about 40 pages</strong>, Pro <strong>about 250 pages</strong>.</li>
<li>GPT Reasoning total context — Free <strong>varies</strong>, Go and Plus <strong>256K</strong>, Pro <strong>400K</strong>.</li>
<li>GPT Reasoning input maximum — Free <strong>varies</strong>, Go and Plus <strong>about 320 pages</strong>, Pro <strong>about 680 pages</strong>.</li>
</ul>
<p>Notice what that does to the Go-versus-Plus comparison: <strong>the context window is identical.</strong> Go doubles Free's instant context and matches Plus on it. OpenAI's own footnote explains that the space available for your input is smaller than the total window, because system instructions, memories and internal processing also consume it, and that the reported figure is an approximation that may change dynamically.</p>

<p><strong>Voice</strong> (OpenAI release notes, 9 September 2026):</p>
<ul>
<li>Go — up to <strong>3 hours</strong> with GPT-Live-1 mini, replacing its earlier GPT-Live-1 access.</li>
<li>Plus — up to <strong>3 hours</strong> with GPT-Live-1.</li>
<li>Pro $100 — up to <strong>15 hours</strong> with GPT-Live-1.</li>
<li>Pro $200 — <strong>unlimited</strong> GPT-Live-1.</li>
</ul>
<p>Same hour allowance for Go and Plus; the difference is which model speaks. Plus and Pro also no longer drop to GPT-Live mini once the limit is reached.</p>

<p><strong>Library storage</strong> (release notes, 14 May 2026): Free <strong>500 MB</strong>, Go <strong>4 GB</strong>, Plus and Business <strong>20 GB</strong>, Pro <strong>100 GB</strong>.</p>

<p><strong>File uploads per project</strong> (release notes, 3 September 2025): Free up to <strong>5</strong>, Plus, Go and Edu up to <strong>25</strong>, Pro, Business and Enterprise up to <strong>40</strong>.</p>

<p><strong>Deep research in ChatGPT Work and Codex</strong> (release notes, 9 September 2026): available to Plus, Pro, Business, Enterprise and Edu. Not Free, not Go. In ordinary chat, deep research is listed as "limited" on Free and Go and full on Plus and Pro.</p>

<h2>Features that surprise people, in both directions</h2>
<p><strong>Free is more capable than its reputation.</strong> Per OpenAI's comparison table, the free tier includes projects, shared projects, the plugins directory, interactive apps, Skills (beta), search, the built-in browser, study mode, memory sources, code edits on macOS, and regular quality and speed updates as models improve. Free and Go both get unlimited everyday text chats, subject to abuse guardrails.</p>

<p><strong>Go genuinely adds things Free lacks.</strong> Scheduled tasks and the ability to create and share GPTs are both "No" on Free and "Yes" on Go. Data analysis, vision and file uploads move from "limited" on Free to full on Go. Memory moves from "limited" to "yes", and memory with past chats likewise.</p>

<p><strong>Some things you might assume are paid are not available at any individual price.</strong> Sites is Plus and Pro only — Free and Go both get "No". Workspace agents, company knowledge, SAML SSO, an admin console, SOC 2 Type 2 compliance, SCIM, role-based access controls, data residency and every other entry in the security and administration block are "No" across all four individual plans. Those are Business and Enterprise features. If you are buying for a company, no consumer tier will satisfy a security questionnaire, and this is the point where the comparison stops being about price.</p>

<p><strong>One thing is only on the top tier:</strong> sharing GPTs with your workspace is Pro-only — not even Plus gets it.</p>

<p><strong>And one selling point is being withdrawn.</strong> On 11 September 2026 OpenAI announced it is planning to retire custom GPTs across ChatGPT plans and provide a migration path to plugins, which combine reusable instructions with connected apps. Existing GPTs keep working until a retirement date that varies by plan and workspace. If "custom GPTs" is your reason for paying, that reason has a shelf life — check the current status before you subscribe on the strength of it.</p>

<h2>Pro: the tier you may not be able to buy</h2>
<p>This is the most time-sensitive fact on the page. OpenAI's Pro article carries a banner dated <strong>10 September 2026</strong>:</p>

<p><em>"As of September 10, 2026, we're temporarily pausing new sign-ups and upgrades to the ChatGPT Pro $200 plan (Pro 20X). This includes sign-ups and upgrades from Free, Go, Plus, or Pro $100. Existing ChatGPT Pro $200 subscriptions and new or existing ChatGPT Pro $100 subscriptions are not affected by this pause."</em></p>

<p>The consequences are unusually sharp, and they are the kind of thing that costs real money if you do not read them:</p>
<ul>
<li>You <strong>can</strong> still upgrade to Pro $100, from the pricing page or Settings &rarr; My Plan. New limits apply immediately.</li>
<li>You <strong>cannot</strong> move to Pro $200 from Free, Go, Plus or Pro $100 until the pause is lifted. OpenAI gives no end date.</li>
<li>If you are already on Pro $200 it keeps renewing as usual, and remains the highest usage tier.</li>
<li>If you cancel or schedule a downgrade, you keep Pro $200 until the end of the current billing cycle and can undo the change in billing settings before the cycle ends. <strong>Once that subscription ends you cannot buy it back</strong> until the pause lifts — the same applies if a refund cancels it, if a promotion ends it, or if a renewal payment fails and the subscription is cancelled.</li>
<li>New Pro $200 promo redemptions are paused too. Usage-credit promotions are separate and still run under their own terms.</li>
</ul>

<p>Practically: if you hold Pro $200 and were considering dropping to Pro $100 to save $100 a month, that door currently closes behind you. And if you were planning to work up to Pro $200, the plan is not available at any price today.</p>

<h2>The arithmetic of usage per dollar</h2>
<p>OpenAI describes Pro as a multiplier of Plus: 5x at $100, 20x at $200. Divide those against the $20 Plus price and a pattern appears. This is plain arithmetic on OpenAI's own published numbers, not a claim about any individual feature:</p>
<ul>
<li><strong>Plus, $20</strong> — the baseline, 1x.</li>
<li><strong>Pro $100</strong> — 5x the usage for 5x the price. Usage per dollar is <strong>flat</strong> against Plus. You are not getting a bulk discount; you are buying headroom at the same rate.</li>
<li><strong>Pro $200</strong> — 20x the usage for 10x the price. Usage per dollar is <strong>roughly double</strong> Plus, and double Pro $100.</li>
</ul>
<p>So the $200 tier is the efficient one <em>if and only if</em> you actually consume something approaching 20x. For most people that is not a real workload, and the honest framing is that Pro $100 costs the same per unit of allowance as Plus while removing the ceiling you were hitting. It is also the tier currently on pause, which makes Pro $100 the only Pro anyone can newly buy.</p>

<p>Two cautions on the multipliers. First, OpenAI says allowances differ per model and per Pro tier, and that some models have separate usage allowances — so "20x" is not a uniform 20x across every feature. Second, when you hit an allowance the model becomes temporarily unavailable until it resets; ChatGPT displays a reset time where one exists, there is no setting to raise or bypass an allowance, and OpenAI states plainly that <strong>Support does not reset ChatGPT or Codex usage limits</strong>.</p>

<p>For scale, monthly-only billing turns into these annual figures (arithmetic on the prices above): Go about <strong>$96</strong> a year, Plus <strong>$240</strong>, Pro $100 <strong>$1,200</strong>, Pro $200 <strong>$2,400</strong>. Across roughly 250 working days that is about $0.38, $0.96, $4.80 and $9.60 a working day. The gap between Go and Plus is $144 a year — $12 a month — which is the entire price of the model access, ad removal, Sites, full deep research and fast response times described above.</p>

<h2>The decision framework</h2>
<p>Work down and stop at the first one that describes you.</p>

<p><strong>1. Do you use ChatGPT a handful of times a week for ordinary questions?</strong> Stay on Free. Unlimited everyday text chats with Luna, plus projects, search, plugins and the built-in browser, is a real product. The limits that bite are uploads, image generation, deep research and memory — if none of those are your use, there is nothing to buy.</p>

<p><strong>2. Are you hitting limits, but your work is ordinary — drafting, summarising, analysing a file, a few images?</strong> Go. It doubles Free's instant context to 54K, lifts uploads, image creation and data analysis from limited to full, adds scheduled tasks and custom GPTs, and quadruples Library storage to 4 GB. Understand what you are <em>not</em> buying: no GPT-5.6 Sol, no GPT-6 Astra, no legacy models, no Sites, limited deep research, and ads may still appear.</p>

<p><strong>3. Do you want better answers, not just more of them?</strong> Plus. This is the tier that unlocks GPT-6 Astra and GPT-5.6 Sol, fast response times, full deep research, Sites, interactive tables and charts, developer mode, record mode, apps connecting to internal tools, and 20 GB of Library storage. It is also the tier that removes ads. At $20 a month with no annual option, the honest test is whether you would use it on most working days — at about $0.96 a working day, the answer for daily users is usually yes.</p>

<p><strong>4. Do you reliably exhaust Plus, especially in Codex or long research sessions?</strong> Pro $100. It is the only Pro tier currently purchasable, it gives 5x Plus usage, GPT-5.6 Sol Pro, 128K instant context and about 250 pages of input, 400K reasoning context, 15 hours of GPT-Live-1 voice and 100 GB of Library storage. Budget $1,200 a year.</p>

<p><strong>5. Were you planning to buy Pro $200?</strong> You cannot, as of 10 September 2026. New sign-ups and upgrades are paused with no published end date. If you already have it, treat the subscription as non-replaceable until the pause lifts — do not cancel or downgrade on the assumption you can return.</p>

<p><strong>6. Is this for a team, or does anyone need to answer a security questionnaire?</strong> Stop looking at consumer tiers. SSO, admin console, SOC 2 Type 2, SCIM, data residency and role-based access are "No" on Free, Go, Plus <em>and</em> Pro. That is Business or Enterprise, priced per user per month, from two users, and the only place annual billing exists. Nonprofits can get up to 75% off; verified US K-12 educators can get ChatGPT for Teachers free through June 2027.</p>

<h2>What to check before you pay, in order</h2>
<ul>
<li><strong>Which model you actually need.</strong> Open the model picker on your current account and see what is there. If Luna is answering your questions adequately, no tier change will improve your results — only your allowances.</li>
<li><strong>Whether the limit you hit is a message limit or a model limit.</strong> They have different fixes. A message limit is solved by Go. A model limit is only solved by Plus or above.</li>
<li><strong>Whether ads bother you enough to be worth $12 a month.</strong> That is the precise Go-to-Plus delta, and ad removal is one of the things it buys. Check Settings &gt; Ad Controls first; you may be able to reduce personalisation for free.</li>
<li><strong>The billing mechanics of changing your mind.</strong> Upgrades take effect immediately and restart your billing cycle. Downgrades take effect at your next renewal, and you keep the current plan until then. Cancelling keeps access to the end of the paid period. Switching down from Plus or Pro to Go is <strong>not refunded</strong>.</li>
<li><strong>That you are not about to pay twice.</strong> Subscribing through the iOS App Store, Google Play and chatgpt.com are separate billing paths. OpenAI has a dedicated help article on avoiding duplicate charges; check Account and Billing in each place before you buy, and note that API usage is separate and billed independently on every plan.</li>
<li><strong>Whether a feature you are paying for is being retired.</strong> Custom GPTs are planned for retirement with migration to plugins, and automatic Instant-to-Thinking switching was retired for Plus and Pro on 14 September 2026. Release notes are the place to check, and they are updated most days.</li>
<li><strong>Your training-data setting.</strong> Content is used to train models on Free, Go, Plus and Pro alike, with an opt-out available on all four. Paying more does not change this — it is a setting, not a tier benefit.</li>
</ul>

<p>Before adding another recurring charge, it is worth running the numbers across everything you already pay for. This desk has a worked method for that in <a href="/tech/subscription-creep-audit/">how to audit every subscription you are actually paying for</a>, and an $8 or $20 monthly line is exactly the kind of charge that survives unnoticed. If you are choosing between AI assistants rather than between tiers, <a href="/tech/chatgpt-vs-claude-vs-gemini/">ChatGPT versus Claude versus Gemini</a> compares the three, and <a href="/tech/free-ai-tools-worth-using/">the free AI tools worth using</a> covers what you can get without paying at all.</p>

<p><em>Prices and plan details on this page are US figures read from OpenAI's own pricing page and help centre on 15 September 2026. Go's dollar price could not be confirmed first-party and is labelled accordingly; OpenAI states that Go purchases are in USD with local-currency billing in a limited set of countries, that prices may be adjusted over time, and that model availability and limits change during rollouts. Individual plans are monthly-only. Nothing here is a claim that one plan is universally best — the right tier depends on whether your bottleneck is volume, model access or administration.</em>""",
     [("ChatGPT — Pricing (plan comparison matrix)", "https://chatgpt.com/pricing/"),
      ("OpenAI Help Center — What is ChatGPT Plus?", "https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus"),
      ("OpenAI Help Center — About ChatGPT Pro tiers", "https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers"),
      ("OpenAI Help Center — What is ChatGPT Go?", "https://help.openai.com/en/articles/11989085-what-is-chatgpt-go"),
      ("OpenAI Help Center — Ads in ChatGPT", "https://help.openai.com/en/articles/20001047-ads-in-chatgpt"),
      ("OpenAI Help Center — ChatGPT Release Notes", "https://help.openai.com/en/articles/6825453-chatgpt-release-notes")],
     [("chatgpt-vs-claude-vs-gemini", "ChatGPT vs Claude vs Gemini: which one to use"),
      ("free-ai-tools-worth-using", "The free AI tools actually worth using"),
      ("subscription-creep-audit", "How to audit every subscription you pay for"),
      ("microsoft-365-free-vs-paid", "Microsoft 365: free vs paid, tier by tier"),
      ("ai-useful-vs-hype", "Where AI is genuinely useful, and where it is hype")]),
]
