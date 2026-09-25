# -*- coding: utf-8 -*-
"""BRYME Tech — Phase 1 content batch 9 (2026-09-25).

The AI fundamentals cluster. Cannibalization check run first: the AI shelf is
already heavy on comparisons (chatgpt-vs-claude, gemini-vs-chatgpt, free-vs-paid,
alternatives, useful-vs-hype) so this batch deliberately fills the evergreen
FOUNDATION those comparisons assume — how the models work, why they hallucinate,
how to prompt, how to spot fakes, and privacy. No new head-to-head comparison.

International rule honoured (Section 30): tier-1 US/UK/CA/AU/NZ/EU/Nigeria; the
privacy piece points at the GDPR/CCPA/NDPR map rather than repeating it, and
nothing here fakes a jurisdiction-specific claim. Educational, no fabricated
benchmarks, scores or prices, honest framing.

Shape matches tech_guides_data.NEW_TECH_GUIDES:
  (slug, cat, kind, title, dek, body_html, sources, related)
"""

PHASE9_GUIDES = [

# ---------------------------------------------------------------- AI FUNDAMENTALS CLUSTER
("how-large-language-models-actually-work", "ai", "guide",
"How large language models actually work (in plain English, no maths)",
"They are not databases and not minds — they are extremely good guessers of the next word. Understanding that one idea explains both their brilliance and their nonsense.",
"""<p>Most confusion about AI — both the fear and the overselling — comes from not knowing what the thing actually is. A large language model is not a database it looks things up in, and not a mind that understands you. It is a system trained to do one thing extraordinarily well: given the words so far, predict the most likely next word. Everything it does, good and bad, follows from that single mechanic.</p>
<h2>Next-word prediction, at enormous scale</h2>
<p>During training the model reads a vast amount of text and learns statistical patterns — which words tend to follow which, in which contexts. Ask it something and it generates an answer one token at a time, each chosen because it is likely to follow the last. There is no lookup table of facts and no belief underneath; there is a deeply learned sense of what plausible text looks like. That is why it can write a poem it has never seen and also state a falsehood with total confidence — both are just "what would likely come next."</p>
<h2>Why this explains the brilliance and the nonsense</h2>
<p>The same mechanic that makes a model fluent and useful makes it unreliable as a source of fact. It is optimised for plausibility, not truth, so when it does not "know" something it will still produce something that fits the pattern — the failure explored in <a href="/tech/why-ai-hallucinates-and-how-to-fact-check/">why AI hallucinates</a>. It also explains why phrasing matters so much: you are steering a predictor, which is the whole subject of <a href="/tech/writing-better-prompts-plain-english/">writing better prompts</a>.</p>
<h2>What it is genuinely good at, and what it is not</h2>
<p>Because it models language, it excels at anything linguistic: drafting, summarising, rephrasing, explaining, brainstorming, translating, and turning messy text into structure. It is weak at precise recall of specific facts, arithmetic it cannot reason through, and knowing the limits of its own knowledge. Judging a tool against what it actually is — a powerful language engine, not an oracle — is the same scepticism the desk applies in <a href="/tech/ai-useful-vs-hype/">useful vs hype</a>, and it is what lets you use these tools well instead of being impressed or burned by them.</p>""",
[],
["why-ai-hallucinates-and-how-to-fact-check", "ai-useful-vs-hype"]),

("why-ai-hallucinates-and-how-to-fact-check", "ai", "guide",
"Why AI hallucinates, and the fact-checking habit that keeps you safe",
"A confident, fluent, completely wrong answer is a feature of how these models work, not a glitch. Here is why it happens and the discipline for never being caught out by it.",
"""<p>Sooner or later everyone using an AI assistant gets handed a fact that is stated beautifully and is simply not true — an invented quote, a case that does not exist, a statistic that sounds right. This is not a rare bug. It is the predictable consequence of how the models are built, and the only defence is a habit, not trust.</p>
<h2>Why it happens</h2>
<p>As explained in <a href="/tech/how-large-language-models-actually-work/">how these models work</a>, a model predicts plausible next words; it is optimised for text that fits, not text that is true. When it lacks a real answer, the gap does not produce silence — it produces the most plausible-looking fill. Fluency and confidence are by-products of the mechanism, not signals of accuracy, which is exactly why a hallucination is so hard to spot: it reads like everything around it.</p>
<h2>The fact-checking habit</h2>
<p>Treat specific, checkable claims — names, dates, numbers, quotes, citations, legal or medical specifics — as unverified until you confirm them against a primary source. The model is excellent at <em>finding the shape</em> of an answer and at explaining a topic; it is unreliable as the <em>authority</em> for a fact. So use it to draft, summarise and explain, then verify the load-bearing details yourself. If it cites a source, open the source — invented references are common precisely because a plausible-looking citation is what the predictor would produce.</p>
<h2>Where the stakes are highest</h2>
<p>The cost of a hallucination scales with the decision it feeds. For a casual summary, low stakes; for something legal, medical, financial, or published under your name, a confident falsehood can do real damage — which is why this desk's own rule is no claim without a dated, checkable source, the standard in the methodology. Pair the habit with the privacy discipline in <a href="/tech/ai-privacy-what-not-to-paste/">what not to paste into AI</a>: verify what comes out, and be careful what goes in. Used that way, the model is a superb thinking partner; trusted as an oracle, it is a liability.</p>""",
[],
["how-large-language-models-actually-work", "ai-privacy-what-not-to-paste"]),

("writing-better-prompts-plain-english", "ai", "guide",
"Writing better prompts in plain English (no incantations, no magic phrases)",
"You do not need secret wording — you need to give context, say what good looks like, and iterate. Here is the practical craft that reliably gets more out of any assistant.",
"""<p>Prompt "engineering" is often sold as a set of magic phrases. It is not. A model is a next-word predictor responding to the text you give it, so better prompts are not incantations — they are clearer communication. The same things that would help a capable human help a model: context, a clear ask, and feedback. None of this requires jargon.</p>
<h2>The four moves that do most of the work</h2>
<p><strong>Give context</strong> — who you are, who the audience is, what it is for; the model cannot guess what you have not said. <strong>Be specific about the output</strong> — length, format, tone, what to include and leave out; "a 150-word email, warm but brief, no jargon" beats "write an email." <strong>Show an example</strong> when you can — one sample of the style or structure you want is worth a paragraph of description. And <strong>iterate</strong> — treat the first answer as a draft and refine, because a conversation narrows in on what you mean far faster than one perfect instruction.</p>
<h2>Why this works (it is the mechanism)</h2>
<p>Because the model predicts what should come next, the more precisely you describe the situation and the desired result, the more the plausible continuation <em>is</em> your desired result. Vague in, generic out; specific in, useful out. This is a direct consequence of <a href="/tech/how-large-language-models-actually-work/">how the models work</a> — you are steering a predictor with context, not unlocking it with a code word.</p>
<h2>What actually limits the result</h2>
<p>No prompt fixes a model's blind spots: it will still not reliably know specific facts (<a href="/tech/why-ai-hallucinates-and-how-to-fact-check/">why it hallucinates</a>) and cannot verify its own claims, so prompt well <em>and</em> check the load-bearing details. Be careful what you put in the prompt too — the privacy rules in <a href="/tech/ai-privacy-what-not-to-paste/">what not to paste</a> apply to every prompt you write. And remember the tool underneath matters: which assistant you use is a separate question, worked through in <a href="/tech/ai-assistants-compared/">AI assistants compared</a>. Clear thinking in, useful work out — that is the whole craft.</p>""",
[],
["how-large-language-models-actually-work", "ai-assistants-compared"]),

("spotting-ai-fakes-and-deepfakes", "ai", "guide",
"Spotting AI fakes and deepfakes: the practical checks before you believe it",
"Generated images, cloned voices and fabricated text are now good enough to fool a first glance. Here are the concrete tells and the habits that stop you being taken in.",
"""<p>Generated media has crossed the line where a quick look is no longer enough — a convincing face, a familiar voice on a call, a plausible news quote. The defence is not paranoia or expertise; it is a few concrete checks and a habit of pausing before you believe or share something that was clearly designed to provoke a reaction.</p>
<h2>The tells in images and video</h2>
<p>Generated images still leak signs, though fewer each year: implausible hands and teeth, garbled text in the background, mismatched reflections or shadows, eerily smooth skin, and jewellery or glasses that melt into the face. Reverse-image-search a picture — if a "real" event photo exists nowhere else, treat it as suspect. And check the source before the pixels: a genuine news image appears on reputable outlets; a fabrication usually appears first on one account with no original.</p>
<h2>The tells in voice and text</h2>
<p>Cloned voice is the one that catches people, especially in a stressful "it's me, I need help" call. The defence is procedural, not perceptual: agree a safe word or call the person back on a known number, because a real person can verify and a scammer cannot. For text, be suspicious of writing that is fluent but factually hollow, or that arrives with unusual urgency — the same instincts as <a href="/tech/how-to-spot-a-suspicious-link/">spotting a suspicious link</a>, because AI is now used to make phishing more convincing, the risk covered in <a href="/tech/phishing-training-that-actually-works/">phishing training</a>.</p>
<h2>The habit that matters most</h2>
<p>Slow down on anything engineered to make you act fast — outrage, fear, urgency, a too-good deal. Verify against a primary or independent source before sharing, because sharing is how fakes travel. None of this requires spotting every artefact; it requires refusing to let a convincing surface bypass the question "where did this actually come from?" That scepticism is the same one the desk applies to AI answers in <a href="/tech/why-ai-hallucinates-and-how-to-fact-check/">why AI hallucinates</a> — applied now to what you see and hear.</p>""",
[],
["how-to-spot-a-suspicious-link", "why-ai-hallucinates-and-how-to-fact-check"]),

("ai-privacy-what-not-to-paste", "ai", "guide",
"AI privacy: what not to paste into a chatbot, and how to check where your data goes",
"Most assistants learn from what you type by default. Here is the plain rule for what never to paste, and how to find and change the data settings on the tools you use.",
"""<p>People type things into AI assistants that they would never email to a stranger — work documents, personal details, code, anything. The uncomfortable truth is that, by default, many consumer assistants may retain and use your conversations to improve their models. That is fine for a casual question and a serious problem for anything confidential. The fix is a simple rule plus knowing where the settings live.</p>
<h2>The rule for what not to paste</h2>
<p>Do not put anything into a consumer AI tool that you would not be comfortable becoming part of its training data or being reviewed: secrets and passwords, personal data about other people, confidential work or client material, anything covered by an NDA, and proprietary code you do not own outright. If it is sensitive, it does not go in — or it goes only into a tool with a clear no-training, enterprise, or local guarantee.</p>
<h2>Where your data actually goes</h2>
<p>It differs by tool and by plan, and it changes, so check rather than assume. Most major assistants have a setting that controls whether your conversations are used for training, and many exclude paid or business tiers from training by default. This desk already walks through turning that off in <a href="/tech/ai-assistant-data-training-settings/">AI assistant data-training settings</a> — the single most useful five minutes for anyone using these tools. The broader principle is the same as <a href="/tech/what-free-apps-do-with-your-data/">what free apps do with your data</a>: if the tool is free, your input is plausibly part of the deal.</p>
<h2>The jurisdiction angle, and the local option</h2>
<p>If the data you handle belongs to people in the UK/EU, the US or Nigeria, pasting it into a tool that trains on it or stores it abroad can have legal consequences — the GDPR/CCPA/NDPR map in <a href="/tech/data-security-compliance-gdpr-ccpa-ndpr/">data security compliance</a> explains whose rules reach you. For genuinely sensitive work the answer is sometimes to keep it on your own machine, which is the privacy-and-control case in <a href="/tech/local-vs-cloud-ai-running-models-on-your-own-hardware/">running models on your own hardware</a>. Know what you are typing, know where it goes, and the tools stay useful without becoming a leak.</p>""",
[],
["ai-assistant-data-training-settings", "data-security-compliance-gdpr-ccpa-ndpr"]),

("local-vs-cloud-ai-running-models-on-your-own-hardware", "ai", "guide",
"Running AI on your own hardware vs the cloud: the honest trade-off",
"You can now run capable models locally, privately, for free — with real limits. Here is when local AI is the right call and when the cloud is still the better tool.",
"""<p>For a few years "use AI" meant "send your prompt to someone else's server." That is no longer the only option: open models can run on your own machine, privately and at no per-use cost. Local AI is genuinely useful and genuinely limited, and the honest choice between it and the cloud comes down to privacy, capability and hardware — not ideology.</p>
<h2>What local AI gives you</h2>
<p>Privacy is the big one: nothing you type leaves your machine, which solves at a stroke the problem in <a href="/tech/ai-privacy-what-not-to-paste/">what not to paste into AI</a> — sensitive work, client data, anything confidential can be processed without it touching a third party. It also means no per-use cost, no rate limits, and no dependency on a service staying up or staying free. For repetitive or private tasks on data you cannot share, that is a decisive advantage.</p>
<h2>What it costs you</h2>
<p>Capability and convenience. The best local models you can run on a normal computer are typically behind the largest cloud models on hard reasoning, and quality scales sharply with hardware — a serious local setup wants a lot of memory and, ideally, a capable GPU. There is setup and fiddling, and the model is fixed rather than silently improving. So local trades raw capability and ease for privacy and control.</p>
<h2>How to choose</h2>
<p>Choose local when the data is sensitive, the task is well within a smaller model's ability, and you value privacy and zero marginal cost over peak capability. Choose the cloud when you need the strongest reasoning, the latest features, or you simply want it to work without managing hardware — accepting the data trade-offs, which you can reduce via the settings in <a href="/tech/ai-assistant-data-training-settings/">data-training settings</a>. Many people sensibly do both: local for private or routine work, cloud for the hard problems. It is the same local-versus-cloud reasoning as <a href="/tech/local-vs-cloud-smart-home-why-it-decides-everything/">the smart-home version</a> — decide what must stay in your house and what is worth sending out.</p>""",
[],
["ai-privacy-what-not-to-paste", "ai-assistant-data-training-settings"]),

]
