# BRYME Tech — AI assistant comparison matrix (batch 48, 12 Sep 2026).
# Directive Tech tool queue #3: AI comparison matrix built FIRST (assets/ai-matrix.js).
# Market table checked 12 Sep 2026 against three comparison guides (axis-intelligence
# Apr 2026; omidsaffari Aug 2026; toolradar May 2026) — AI products change MONTHLY;
# every figure is a dated directional. Desk byline (organizational, tech convention);
# no invented reviewer; links only to existing desk articles.

AI_SLUG = "ai-assistants-compared"

AI_BODY = """<div class="prose">
<p class="byline">BRYME Tech desk \u00b7 published 12 September 2026 \u00b7 market table checked 12 September 2026 \u2014 AI products change monthly; re-verify before you pay</p>
<p><b>The 60-second answer.</b> Every major AI assistant has a genuinely usable <b>free tier</b> in 2026 \u2014 what the \u00b1$20/month tiers actually buy you is <b>relief from caps</b>, not secret features. The honest map (checked 12 Sep 2026): <b>Claude</b> for writing and code ($20/mo, $17 annual), <b>Perplexity</b> for research with visible sources ($20/mo, 5 free Pro searches/day), <b>Copilot</b> if you live in Microsoft 365 (free in Windows; Pro $20), <b>Mistral Le Chat</b> when EU data residency matters ($14.99), <b>Grok</b> free with an X account, <b>DeepSeek</b> and <b>Meta AI</b> free outright \u2014 and the cheapest paid step in the industry is <b>Gemini\u2019s AI Plus at $4.99/mo</b>. ChatGPT remains the broadest generalist (free, ad-supported in the US; Plus $20).</p>
<p>Use the chooser to rank them by <em>your</em> needs, then read the full matrix \u2014 and the caps table, because caps are what you\u2019re really buying.</p>

<h2 id="chooser">The chooser: rank by your needs</h2>
<style>
.am-note{font-size:13px;color:var(--dim);margin:6px 0}
.am-needs{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0;max-width:760px}
.am-chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line-strong);border-radius:999px;padding:7px 13px;font-size:13.5px;cursor:pointer;background:var(--card)}
.am-chip:hover{border-color:var(--accent)}
#am-out ol{margin:8px 0;padding-left:22px;font-size:15px}
#am-out li{margin:5px 0}
#am-out small{color:var(--dim)}
.am-disc{font-size:13px;color:var(--dim);max-width:760px;margin-top:10px}
</style>
<div id="ai-matrix-calc"></div>
<noscript><p><b>Static version:</b> pick by primary job \u2014 writing/code \u2192 Claude; sourced research \u2192 Perplexity; Google-centric \u2192 Gemini; Microsoft 365 \u2192 Copilot; EU residency \u2192 Mistral Le Chat; free-only \u2192 ChatGPT free, Gemini free, DeepSeek, Meta AI. Full table below.</p></noscript>

<h2 id="matrix">The full matrix (checked 12 Sep 2026)</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Assistant</th><th>Free tier</th><th>Paid from</th><th>Best known for</th><th>The cap you\u2019ll hit</th></tr></thead>
<tbody>
<tr><td><b>ChatGPT</b></td><td>Yes \u2014 broad, ad-supported in the US</td><td>$8\u201320/mo</td><td>The generalist: files, images, data analysis, projects</td><td>Message caps resetting every ~3 hours</td></tr>
<tr><td><b>Claude</b></td><td>Yes \u2014 daily caps</td><td>$17\u201320/mo</td><td>Writing, long documents, code</td><td>Per-5-hour window; Pro Max tiers $100\u2013$200</td></tr>
<tr><td><b>Gemini</b></td><td>Yes</td><td><b>$4.99/mo</b></td><td>Google Workspace natives; cheapest paid step; AI Pro adds 2TB</td><td>Deep Research caps on paid tiers</td></tr>
<tr><td><b>Perplexity</b></td><td>Yes \u2014 5 Pro searches/day</td><td>$16.67\u201320/mo</td><td>Research with inline sources; student plan $4.99</td><td>Pro search count (300/day on Pro)</td></tr>
<tr><td><b>Microsoft Copilot</b></td><td>Yes \u2014 in Windows/M365 chat</td><td>$20/mo</td><td>Microsoft 365 documents and workflows</td><td>Full power needs a qualifying M365 licence</td></tr>
<tr><td><b>Mistral Le Chat</b></td><td>Yes \u2014 rate-limited</td><td>$14.99/mo</td><td>EU data residency</td><td>Free-tier rate limits</td></tr>
<tr><td><b>Grok</b></td><td>Yes \u2014 with an X account</td><td>$30/mo</td><td>X-integrated answers</td><td>Account/platform-tied</td></tr>
<tr><td><b>DeepSeek</b></td><td>Yes \u2014 with caps</td><td>API only</td><td>Coding; free chat</td><td>Free-chat caps; consumers pay via API</td></tr>
<tr><td><b>Meta AI</b></td><td>Yes \u2014 inside Meta apps</td><td>\u2014</td><td>Free assistant in WhatsApp/IG/etc.</td><td>Meta-account-tied; no paid tier</td></tr>
</tbody></table>
<p class="lede" style="font-size:14px">Compiled 12 September 2026 from three independent comparison guides (axis-intelligence, Apr 2026; omidsaffari, Aug 2026; toolradar, May 2026). Prices are the cheapest credible paid step; annual billing is often ~15% under monthly. This market moves monthly \u2014 treat every cell as \u201cas of the checked date\u201d.</p>

<h2 id="job">Which assistant for which job</h2>
<ul>
<li><b>Writing and code:</b> Claude\u2019s editorial quality and long-document handling keep winning comparisons; ChatGPT is the broader all-rounder if you also want images and data analysis in one place.</li>
<li><b>Research where sources matter:</b> Perplexity \u2014 the citations are the product. For getting <em>your</em> site into those answers, that\u2019s a different game (<a href="/tech/how-to-get-cited-by-ai-search/">getting cited by AI search</a>).</li>
<li><b>Google-centric work:</b> Gemini \u2014 and its $4.99 AI Plus is the sensible first paid experiment for anyone.</li>
<li><b>Microsoft 365 shops:</b> Copilot \u2014 but check the licence requirement before assuming the $20 buys everything.</li>
<li><b>Privacy-sensitive / EU:</b> Mistral Le Chat\u2019s EU residency is the differentiator.</li>
<li><b>Zero budget:</b> ChatGPT free, Gemini free, DeepSeek, Meta AI \u2014 genuinely usable, capped (<a href="/tech/free-ai-tools-worth-using/">where free tiers really hold up</a>).</li>
</ul>

<h2 id="caps">Caps: what you\u2019re actually buying at $20</h2>
<p>The honest read of 2026\u2019s pricing: <b>free = capable but rationed; $20 = the caps stop hurting; $100\u2013$200 = more caps gone</b> (ChatGPT Pro $200, Claude Max $100/$200, Perplexity Max $200). Power tiers mostly buy higher limits \u2014 pay for one only after you\u2019ve hit the $20 tier\u2019s ceiling repeatedly, not because a feature list whispered.</p>
<ul>
<li><b>ChatGPT:</b> caps reset roughly every 3 hours \u2014 heavy mornings can burn through them.</li>
<li><b>Claude:</b> per-5-hour windows \u2014 plan long sessions, not bursts.</li>
<li><b>Perplexity:</b> the free 5 Pro searches/day is generous for occasional research; daily researchers hit it by noon.</li>
</ul>

<h2 id="pay">When to actually pay</h2>
<ul>
<li>You\u2019ve hit free caps <b>repeatedly</b> (a week of real work, not one busy Sunday).</li>
<li>The paid capability is <em>load-bearing</em>: long documents on Claude, sourced research on Perplexity, Workspace integration on Gemini.</li>
<li>Annual billing: typically ~15% under monthly if the choice is already made ($17 effective Claude annual, $200/yr Perplexity).</li>
<li>Not yet: if you can\u2019t name the task that hit the cap, stay free another month \u2014 <a href="/tech/ai-useful-vs-hype/">useful vs hype applies to subscriptions too</a>.</li>
</ul>

<h2 id="faq">FAQ</h2>
<p><b>Which AI assistant is completely free?</b><br>
All of the major ones have usable free tiers: ChatGPT (ad-supported in the US), Gemini, Claude (daily caps), Perplexity (5 Pro searches/day), Copilot in Windows, Grok via X, DeepSeek and Meta AI. Free means capped, not crippled.</p>
<p><b>Which AI is best for writing and coding?</b><br>
On the checked-date comparisons, Claude leads for writing quality and long documents, with ChatGPT the broader generalist. Both are $20/mo paid (Claude $17 annual) with usable free tiers.</p>
<p><b>What\u2019s the cheapest paid AI plan?</b><br>
Google\u2019s Gemini AI Plus at $4.99/mo is the cheapest sensible paid step in the industry as of 12 Sep 2026; Perplexity\u2019s student plan ($4.99 with verification) matches it for students.</p>
<p><b>Is the $20/month AI tier worth it?</b><br>
If you\u2019ve hit the free caps repeatedly in real work \u2014 yes, it buys cap relief where the work happens. If you can\u2019t name the task that ran out, stay free another month.</p>
<p><b>Which AI shows its sources?</b><br>
Perplexity is built around inline citations; that\u2019s its core differentiator at $20/mo (or $200/yr).</p>

<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":"Article","headline":"AI assistants compared: the 2026 matrix (free tiers, prices, caps)",
"description":"The 2026 AI assistant market as a matrix: what's actually free, what the $20 tier buys, cheapest paid steps, and a needs-based chooser. Checked 12 Sep 2026.",
"author":{"@type":"Organization","name":"BRYME Tech desk"},
"publisher":{"@type":"Organization","name":"THE BRYME"},
"datePublished":"2026-09-12","dateModified":"2026-09-12"},
{"@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Which AI assistant is completely free?","acceptedAnswer":{"@type":"Answer","text":"All major assistants have usable free tiers: ChatGPT (ad-supported in the US), Gemini, Claude with daily caps, Perplexity with 5 Pro searches a day, Copilot in Windows, Grok via X, DeepSeek and Meta AI. Free means capped, not crippled."}},
{"@type":"Question","name":"Which AI is best for writing and coding?","acceptedAnswer":{"@type":"Answer","text":"On comparisons checked 12 September 2026, Claude leads for writing quality and long documents, with ChatGPT the broader generalist. Both cost $20 monthly paid (Claude $17 annual) with usable free tiers."}},
{"@type":"Question","name":"What is the cheapest paid AI plan?","acceptedAnswer":{"@type":"Answer","text":"Google's Gemini AI Plus at $4.99 per month is the cheapest sensible paid step as of 12 September 2026; Perplexity's student plan ($4.99 with verification) matches it for students."}},
{"@type":"Question","name":"Is the $20 per month AI tier worth it?","acceptedAnswer":{"@type":"Answer","text":"If you have hit the free caps repeatedly in real work, yes - it buys cap relief where the work happens. If you cannot name the task that ran out, stay free another month."}},
{"@type":"Question","name":"Which AI shows its sources?","acceptedAnswer":{"@type":"Answer","text":"Perplexity is built around inline citations - that is its core differentiator at $20 per month (or $200 per year)."}}]}]}
</script>

<h2>Sources (all checked 12 September 2026 \u2014 this market changes monthly)</h2>
<ul>
<li>axis-intelligence.com \u2014 Best AI Chatbots 2026, tested by use case: pricing table incl. ChatGPT GPT-5.3 free/Plus $20/Pro $200; Claude Sonnet 4.6 free/Pro $20/Max $100\u2013$200; Gemini 3 Flash free/AI Pro $19.99+2TB/Ultra $249.99; Perplexity free/Pro $20/Max $200 + $4.99 student; Copilot free-in-Windows/$20/$30 enterprise (Apr 2026).</li>
<li>omidsaffari.com \u2014 Best AI chatbot 2026: Claude for documents/code, Perplexity for sourced research, Gemini\u2019s $4.99 AI Plus cheapest step-up, ChatGPT broadest (Aug 2026).</li>
<li>toolradar.com \u2014 AI chatbots for business 2026: cap styles (3h resets, 5-hour windows, 5 Pro searches/day), Mistral $14.99 EU residency, Grok $30, DeepSeek API-only, Meta AI free (May 2026).</li>
</ul>
<p class="byline">Reviewed 12 September 2026 \u00b7 models, caps and prices in this market change monthly \u2014 every cell is \u201cas of the checked date\u201d \u00b7 no professional reviewer is claimed: general information, not purchase advice.</p>
</div>
<script src="/assets/ai-matrix.js" defer></script>"""

NEW_AI_GUIDES = [
(AI_SLUG, "ai", "guide",
"AI assistants compared: the 2026 matrix (free tiers, prices, caps)",
"What's actually free across ChatGPT, Claude, Gemini, Perplexity, Copilot and more, what the $20 tier buys, and a needs-based chooser. Checked 12 Sep 2026.",
AI_BODY,
[("axis-intelligence - Best AI Chatbots 2026", "https://axis-intelligence.com/best-ai-chatbots-2026-tested-complete-guide/"),
 ("omidsaffari - Best AI chatbot 2026", "https://omidsaffari.com/blog/best-ai-chatbot"),
 ("toolradar - AI chatbots for business 2026", "https://toolradar.com/guides/best-ai-chatbots")],
[("chatgpt-vs-claude-vs-gemini", "The head-to-head comparison"),
 ("free-ai-tools-worth-using", "Free AI tools worth using"),
 ("ai-useful-vs-hype", "Useful AI vs hype")]),
]
