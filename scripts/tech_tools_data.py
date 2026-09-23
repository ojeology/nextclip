# -*- coding: utf-8 -*-
"""BRYME Tools (master build M3) — 8 client-side browser tools, CSP-safe.

Pattern: UI markup here; behaviour in assets/tool-<name>.js (script-src 'self'; no inline
JS anywhere); styles in assets/tech-tools.css. Every tool: runs entirely in the visitor's
browser, no network calls, no data collection. Each links its companion article + siblings.
"""

# (slug, short name, title, dek, article_slug_or_None, what_html, tool_html)
TOOLS = [

("json-formatter", "JSON formatter & validator",
"JSON formatter & validator",
"Paste JSON, format it, minify it, or find out exactly where it breaks. Runs entirely in your browser.",
"what-is-json",
"""<h2>What this does</h2>
<p>Paste JSON into the box and press <b>Format</b>: valid JSON comes back indented and readable, with a confirmation message. <b>Minify</b> strips all the whitespace back out (handy for configs and payloads). If the JSON is invalid, the tool shows the parser's actual error message &mdash; which usually names the exact character position that broke it.</p>
<h2>Notes</h2>
<p>The formatter is strict, as the standard demands: double-quoted keys, no trailing commas, no comments. For why those rules exist, read <a href="/tech/what-is-json/">what JSON actually is</a>. Nothing you paste leaves this page &mdash; the tool runs in your browser and your text never touches a server.</p>""",
"""<label class="tt-label" for="tt-in">Paste JSON</label>
<textarea id="tt-in" class="tt-box" rows="8" spellcheck="false" placeholder='{"hello": "world", "working": true, "notes": ["paste", "anything"]}'></textarea>
<div class="tt-btnrow"><button type="button" id="tt-format" class="btn">Format</button>
<button type="button" id="tt-minify" class="btn secondary">Minify</button>
<button type="button" id="tt-clear" class="btn secondary">Clear</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("base64-encoder", "Base64 encoder / decoder",
"Base64 encoder / decoder",
"Encode text to Base64 or decode it back, with proper UTF-8 handling. Client-side only.",
"base64-explained",
"""<h2>What this does</h2>
<p>Type or paste text, then <b>Encode</b> to get its Base64 form, or paste Base64 and <b>Decode</b> to get the original back. The tool handles non-Latin characters correctly (emoji, accents, other scripts) by encoding through UTF-8 &mdash; many quick converters mangle anything beyond plain ASCII.</p>
<h2>Notes</h2>
<p>Two reminders worth repeating: decoding is the inverse of encoding, so <b>Base64 is not security</b> &mdash; anything encoded can be decoded by anyone (see <a href="/tech/plain-text-passwords/">why encoding is not protection</a>). And as with every tool on this page, your text is processed on your device and never sent anywhere.</p>""",
"""<label class="tt-label" for="tt-in">Text or Base64</label>
<textarea id="tt-in" class="tt-box" rows="6" spellcheck="false" placeholder="Hello, world — or paste Base64 to decode"></textarea>
<div class="tt-btnrow"><button type="button" id="tt-enc" class="btn">Encode &rarr;</button>
<button type="button" id="tt-dec" class="btn">&larr; Decode</button>
<button type="button" id="tt-clear" class="btn secondary">Clear</button></div>
<label class="tt-label">Result</label>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("url-encoder", "URL encoder / decoder",
"URL encoder / decoder",
"Percent-encode text or full URLs, or decode %20-style sequences back to readable text.",
None,
"""<h2>What this does</h2>
<p>URLs can only carry a limited set of characters; everything else gets percent-encoded (a space becomes <code>%20</code>). Paste text or a URL, choose a mode, and encode or decode:</p>
<p><b>Component mode</b> encodes everything special &mdash; use it for query-parameter values, the part after <code>?q=</code>. <b>Full URL mode</b> leaves URL structure characters (<code>:&#47;&#47;</code>, <code>&amp;</code>, <code>=</code>) intact so a whole link stays a working link.</p>
<h2>Notes</h2>
<p>Decoding fails loudly on malformed input (a stray <code>%</code> that isn't a valid sequence), which is the correct behaviour &mdash; better than silently mangling data. One classic gotcha the tool won't hide: in <em>form</em> submissions a space is sometimes written as <code>+</code>; decode those with component mode after replacing <code>+</code> with <code>%20</code> if the result keeps literal pluses.</p>""",
"""<label class="tt-label" for="tt-in">Text or URL</label>
<textarea id="tt-in" class="tt-box" rows="5" spellcheck="false" placeholder="hello world &amp; more / or a whole https://link"></textarea>
<div class="tt-btnrow"><label style="font-size:14px"><input type="checkbox" id="tt-component" checked> component mode (query values)</label></div>
<div class="tt-btnrow"><button type="button" id="tt-enc" class="btn">Encode &rarr;</button>
<button type="button" id="tt-dec" class="btn">&larr; Decode</button>
<button type="button" id="tt-clear" class="btn secondary">Clear</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("uuid-generator", "UUID generator (v4)",
"UUID generator (version 4)",
"Generate cryptographically random version-4 UUIDs, one at a time or in batches, with one-tap copy.",
"uuid-guide",
"""<h2>What this does</h2>
<p>Press <b>Generate</b> for fresh version-4 UUIDs &mdash; 128-bit identifiers drawn from your browser's cryptographic random source (<code>crypto.getRandomValues</code>), the proper way, not <code>Math.random</code>. Choose a batch of 1, 5 or 10, and <b>Copy</b> puts the whole list on your clipboard.</p>
<h2>Notes</h2>
<p>Version 4 is the random flavour: 122 of its 128 bits are random, which is why two generated UUIDs are, for practical purposes, never the same &mdash; the reasoning (and when <em>not</em> to use a random UUID) is in <a href="/tech/uuid-guide/">the UUID guide</a>. Generated on your device, transmitted nowhere.</p>""",
"""<div class="tt-btnrow"><label class="tt-label" for="tt-count" style="margin:0 8px 0 0">How many:</label>
<select id="tt-count" class="tt-input" style="max-width:90px"><option>1</option><option>5</option><option>10</option></select></div>
<div class="tt-btnrow"><button type="button" id="tt-gen" class="btn">Generate</button>
<button type="button" id="tt-copy" class="btn secondary">Copy</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("timestamp-converter", "Unix timestamp converter",
"Unix timestamp converter",
"Convert Unix seconds or milliseconds to readable dates, and dates back to timestamps. Both directions, local and UTC.",
"unix-time-explained",
"""<h2>What this does</h2>
<p><b>Timestamp &rarr; date:</b> paste a Unix timestamp (seconds <em>or</em> milliseconds &mdash; the tool detects which by size), or press <b>Now</b> for the current moment. You get the local time and UTC side by side. <b>Date &rarr; timestamp:</b> pick a date and time, press convert, and get both the seconds and milliseconds forms.</p>
<h2>Notes</h2>
<p>The seconds-versus-milliseconds mix-up is the most common timestamp bug in web development &mdash; the auto-detection here exists because of how often it bites (the full story in <a href="/tech/unix-time-explained/">what Unix time is</a>). Your device's timezone settings drive the "local" line; UTC never changes.</p>""",
"""<label class="tt-label" for="tt-stamp">Timestamp (seconds or milliseconds)</label>
<div class="tt-btnrow"><input type="input" id="tt-stamp" class="tt-input" inputmode="numeric" placeholder="1726000000">
<button type="button" id="tt-now" class="btn secondary">Now</button>
<button type="button" id="tt-conv" class="btn">Convert &rarr;</button></div>
<label class="tt-label" for="tt-date">…or pick a date</label>
<div class="tt-btnrow"><input type="datetime-local" id="tt-date" class="tt-input">
<button type="button" id="tt-dconv" class="btn">Convert &rarr;</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("word-counter", "Word & character counter",
"Word & character counter",
"Live word, character, sentence and paragraph counts plus reading time, as you type.",
None,
"""<h2>What this does</h2>
<p>Start typing or paste text: the counts update as you go. You get words, characters (with and without spaces), an approximate sentence count, paragraph count, and estimated reading time at a calm 200-words-a-minute pace.</p>
<h2>Notes</h2>
<p>The sentence and reading-time figures are honest approximations &mdash; sentence-splitting on punctuation is a heuristic, and reading speed varies by reader and material. The character counts are exact, which is what forms, meta descriptions and bios actually constrain. Everything is counted on your device; nothing is uploaded.</p>""",
"""<label class="tt-label" for="tt-in">Your text</label>
<textarea id="tt-in" class="tt-box" rows="10" spellcheck="false" placeholder="Type or paste — the counts update as you go."></textarea>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>"""),

("case-converter", "Text case converter",
"Text case converter",
"UPPERCASE, lowercase, Title Case, Sentence case, camelCase, PascalCase, snake_case and kebab-case — one click each.",
None,
"""<h2>What this does</h2>
<p>Paste text and press a button: the converted result appears below. The programmer cases (<b>camelCase</b>, <b>PascalCase</b>, <b>snake_case</b>, <b>kebab-case</b>) split your text on any non-alphanumeric characters, so "quarterly report draft" becomes <code>quarterlyReportDraft</code>, <code>quarterly_report_draft</code> or <code>quarterly-report-draft</code> as needed.</p>
<h2>Notes</h2>
<p>Sentence case re-capitalises after <code>.</code>, <code>!</code> and <code>?</code>; Title Case capitalises every word (headlines that need small-word rules are better done by eye). Proper nouns get lowercased by the machine conversions &mdash; give them a final human pass.</p>""",
"""<label class="tt-label" for="tt-in">Your text</label>
<textarea id="tt-in" class="tt-box" rows="5" spellcheck="false" placeholder="the quarterly report draft"></textarea>
<div class="tt-btnrow">
<button type="button" id="tt-upper" class="btn secondary">UPPERCASE</button>
<button type="button" id="tt-lower" class="btn secondary">lowercase</button>
<button type="button" id="tt-title" class="btn secondary">Title Case</button>
<button type="button" id="tt-sentence" class="btn secondary">Sentence case</button></div>
<div class="tt-btnrow">
<button type="button" id="tt-camel" class="btn">camelCase</button>
<button type="button" id="tt-pascal" class="btn">PascalCase</button>
<button type="button" id="tt-snake" class="btn">snake_case</button>
<button type="button" id="tt-kebab" class="btn">kebab-case</button></div>
<label class="tt-label">Result</label>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>"""),

("http-status-lookup", "HTTP status code lookup",
"HTTP status code lookup",
"The HTTP status codes that actually matter, grouped by class, with plain-language meanings. Type to filter.",
"http-status-codes-explained",
"""<h2>What this does</h2>
<p>A filterable table of the HTTP response codes you meet in real work, grouped by class: <code>1xx</code> informational, <code>2xx</code> success, <code>3xx</code> redirects, <code>4xx</code> the client's problem, <code>5xx</code> the server's problem. Type a code (<code>404</code>) or a word (<code>timeout</code>) and the table narrows as you type.</p>
<h2>Notes</h2>
<p>The descriptions are deliberately plain rather than quotable-spec: what the code <em>means in practice</em> and what usually caused it. The formal definitions live in the IANA registry linked from <a href="/tech/http-status-codes-explained/">the full guide to HTTP status codes</a>. This table is static and complete in the page &mdash; it works with JavaScript disabled too (the typing filter is the only dynamic part).</p>""",
"""<label class="tt-label" for="tt-q">Filter — a code (404) or a word (timeout)</label>
<div class="tt-btnrow"><input type="input" id="tt-q" class="tt-input" placeholder="404" aria-label="Filter status codes">
<button type="button" id="tt-look" class="btn">Filter</button></div>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>
<div style="overflow-x:auto"><table class="tt-table" id="tt-table">
<thead><tr><th>Code</th><th>Name</th><th>What it means in practice</th></tr></thead>
<tbody>
<tr data-code="100 continue"><td>100</td><td>Continue</td><td>The client can go ahead and send the request body.</td></tr>
<tr data-code="101 switching protocols websocket"><td>101</td><td>Switching Protocols</td><td>Agreed to switch — this is how a WebSocket connection upgrades.</td></tr>
<tr data-code="103 early hints"><td>103</td><td>Early Hints</td><td>Preliminary headers before the real response; a performance trick.</td></tr>
<tr data-code="200 ok success"><td>200</td><td>OK</td><td>Worked. The body holds what you asked for.</td></tr>
<tr data-code="201 created post"><td>201</td><td>Created</td><td>Success that made something new — the classic POST response.</td></tr>
<tr data-code="202 accepted queued"><td>202</td><td>Accepted</td><td>Received and queued, not finished yet.</td></tr>
<tr data-code="204 no content delete"><td>204</td><td>No Content</td><td>Success with an empty body — common after DELETE or a save.</td></tr>
<tr data-code="206 partial content range video"><td>206</td><td>Partial Content</td><td>A range was served — video scrubbing and resumable downloads.</td></tr>
<tr data-code="301 moved permanently redirect seo"><td>301</td><td>Moved Permanently</td><td>The address changed for good; update links — search engines transfer rankings.</td></tr>
<tr data-code="302 found temporary redirect"><td>302</td><td>Found</td><td>A temporary redirect; the original URL remains the real one.</td></tr>
<tr data-code="304 not modified cache"><td>304</td><td>Not Modified</td><td>The cached copy is still fresh — the quiet workhorse of fast browsing.</td></tr>
<tr data-code="307 temporary redirect method"><td>307</td><td>Temporary Redirect</td><td>Temporary, but the HTTP method must not change.</td></tr>
<tr data-code="308 permanent redirect method"><td>308</td><td>Permanent Redirect</td><td>Permanent, but the HTTP method must not change.</td></tr>
<tr data-code="400 bad request malformed"><td>400</td><td>Bad Request</td><td>The request itself is malformed; the server refuses to parse it.</td></tr>
<tr data-code="401 unauthorized authentication login"><td>401</td><td>Unauthorized</td><td>"Who are you?" — credentials missing or failed. Log in properly and retry.</td></tr>
<tr data-code="403 forbidden permission"><td>403</td><td>Forbidden</td><td>"I know who you are — still no." A permissions problem, not a login one.</td></tr>
<tr data-code="404 not found"><td>404</td><td>Not Found</td><td>No resource at this URL. The most famous error on the web.</td></tr>
<tr data-code="405 method not allowed"><td>405</td><td>Method Not Allowed</td><td>A GET where only POST is accepted, and similar mismatches.</td></tr>
<tr data-code="409 conflict duplicate"><td>409</td><td>Conflict</td><td>The request fights the resource's current state — often a duplicate.</td></tr>
<tr data-code="410 gone permanently removed"><td>410</td><td>Gone</td><td>Removed on purpose, permanently. Tell search engines it's final.</td></tr>
<tr data-code="413 content too large payload"><td>413</td><td>Content Too Large</td><td>The request body exceeds the server's limit.</td></tr>
<tr data-code="414 uri too long url"><td>414</td><td>URI Too Long</td><td>The URL exceeds limits — usually a query string gone rogue.</td></tr>
<tr data-code="415 unsupported media type content-type"><td>415</td><td>Unsupported Media Type</td><td>Wrong payload format for this endpoint (check Content-Type).</td></tr>
<tr data-code="429 too many requests rate limit"><td>429</td><td>Too Many Requests</td><td>Rate limit hit — slow down; the response often says when to retry.</td></tr>
<tr data-code="431 request header fields too large cookies"><td>431</td><td>Request Header Fields Too Large</td><td>Headers too big — an oversized cookie is the usual suspect.</td></tr>
<tr data-code="451 unavailable legal reasons"><td>451</td><td>Unavailable For Legal Reasons</td><td>Blocked by a legal demand rather than a technical one.</td></tr>
<tr data-code="500 internal server error crash"><td>500</td><td>Internal Server Error</td><td>The server's own code crashed. The cause lives in its logs.</td></tr>
<tr data-code="501 not implemented"><td>501</td><td>Not Implemented</td><td>The server doesn't support this action at all.</td></tr>
<tr data-code="502 bad gateway upstream proxy"><td>502</td><td>Bad Gateway</td><td>A middleman server got garbage from the server behind it.</td></tr>
<tr data-code="503 service unavailable maintenance overloaded"><td>503</td><td>Service Unavailable</td><td>Overloaded or down for maintenance — often temporary.</td></tr>
<tr data-code="504 gateway timeout upstream"><td>504</td><td>Gateway Timeout</td><td>The server behind the middleman took too long to answer.</td></tr>
<tr data-code="511 network authentication required captive portal wifi"><td>511</td><td>Network Authentication Required</td><td>The Wi-Fi wants a login page first — a captive portal.</td></tr>
</tbody></table></div>"""),
("data-usage-estimator", "Data usage estimator", "Will my mobile data last the month?",
 "Bundle size, your daily video, music and social hours - get the pace, the projected month, and an honest verdict. Runs entirely in your browser.",
 "use-less-mobile-data",
 """<h2>What this does</h2>
<p>Most data bundles die on a predictable pattern: video on the commute, a hotspot left on, auto-updates over mobile. Enter your bundle and an honest day's usage and this tool projects the whole cycle - pace, whether the bundle lasts, and how many days short it falls if it does not. The rates are the streaming industry's usual rough averages (standard-definition video around 0.7 GB an hour, high definition around 3, music 50-150 MB, social feeds 100-200 MB) - approximations, not quotations.</p>
<h2>Notes</h2>
<p>The honest inputs are the ones from your phone's own data-usage screen, not your intentions. If the verdict comes back tight, the fixes are on <a href="/tech/use-less-mobile-data/">use less mobile data</a> - and when data refuses to work at all, that is a different problem with its own fix list. Nothing you enter leaves this page: the tool runs entirely in your browser.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label" for="tt-bundle">Bundle size (GB)</label><input id="tt-bundle" type="number" inputmode="decimal" min="1" max="2000" step="0.5" placeholder="10"></div>
<div class="tt-field"><label class="tt-label" for="tt-cycle">Cycle length (days)</label><input id="tt-cycle" type="number" inputmode="numeric" min="1" max="120" step="1" placeholder="30"></div>
<div class="tt-field"><label class="tt-label" for="tt-used">Days already used</label><input id="tt-used" type="number" inputmode="numeric" min="0" max="119" step="1" placeholder="10"></div>
<div class="tt-field"><label class="tt-label" for="tt-quality">Video quality</label><select id="tt-quality"><option value="sd" selected="selected">Standard (SD)</option><option value="hd">High (HD)</option></select></div>
<div class="tt-field"><label class="tt-label" for="tt-video">Video hours per day</label><input id="tt-video" type="number" inputmode="decimal" min="0" max="24" step="0.5" placeholder="1"></div>
<div class="tt-field"><label class="tt-label" for="tt-music">Music hours per day</label><input id="tt-music" type="number" inputmode="decimal" min="0" max="24" step="0.5" placeholder="1"></div>
<div class="tt-field"><label class="tt-label" for="tt-social">Social hours per day</label><input id="tt-social" type="number" inputmode="decimal" min="0" max="24" step="0.5" placeholder="1"></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-est" class="btn">Estimate my month</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>"""),

("vpn-cost-calculator", "VPN true-cost calculator", "What will this VPN deal really cost?",
 "Intro lump sum, months it buys, annual renewal, how long you'll keep it: the 36-month truth, the effective monthly rate and the renewal jump. Runs entirely in your browser.",
 "which-vpn-subscription-is-worth-it",
 """<h2>What this does</h2>
<p>VPN pricing pages advertise an instalment figure (&ldquo;$2.99/mo&rdquo;) that is really a lump sum divided by a long first term, followed by a higher renewal. Enter the four numbers from the checkout page &mdash; the introductory charge, how many months it covers, the annual renewal price, and how long you realistically expect to keep the service &mdash; and the tool returns the total cost over that period, the effective monthly rate, the renewal jump as a multiple of the introductory rate, and, if you supply the provider's month-to-month price, the point at which paying monthly would have been cheaper. Add the optional monthly price to see the break-even for short needs such as a single trip.</p>
<h2>Notes</h2>
<p>Renewals are prorated across the months you keep the service after the introductory term ends; providers bill them annually in advance, so your actual invoice lands in yearly chunks rather than the smoothed figure shown here. Taxes, currency conversion and bank markups are excluded &mdash; for a Nigerian card paying a USD charge, your bank's conversion rate on the day is part of the real price. The companion read is <a href="/tech/which-vpn-subscription-is-worth-it/">Which VPN subscription is worth paying for?</a>, where the five current contracts are compared on their own published terms.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label" for="tt-intro">Introductory charge (total, e.g. 83.72)</label><input id="tt-intro" type="number" inputmode="decimal" min="0" max="2000" step="0.01" placeholder="83.72"></div>
<div class="tt-field"><label class="tt-label" for="tt-introm">Months the intro charge covers</label><input id="tt-introm" type="number" inputmode="numeric" min="1" max="60" step="1" placeholder="28"></div>
<div class="tt-field"><label class="tt-label" for="tt-renew">Renewal price per year</label><input id="tt-renew" type="number" inputmode="decimal" min="0" max="2000" step="0.01" placeholder="99.95"></div>
<div class="tt-field"><label class="tt-label" for="tt-keep">Months you expect to keep it</label><input id="tt-keep" type="number" inputmode="numeric" min="1" max="120" step="1" placeholder="36"></div>
<div class="tt-field"><label class="tt-label" for="tt-monthly">Month-to-month price (optional)</label><input id="tt-monthly" type="number" inputmode="decimal" min="0" max="200" step="0.01" placeholder="14.99"></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-calc" class="btn">Calculate the true cost</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>"""),

("internet-speed-calculator", "Internet speed calculator", "What internet speed do you actually need?",
 "Count the 4K streams, video calls, gamers and smart gadgets in the house - get the download and upload numbers worth paying for, headroom included. Runs entirely in your browser.",
 "new-router-for-slow-internet",
 """<h2>What this does</h2>
<p>Internet plans are sold by big numbers, and most households either overpay for speed they never use or underbuy and blame the Wi-Fi. Count the simultaneous activity in your home and this tool adds the published bandwidth each activity actually consumes, applies a 25% headroom for surges, and maps the result onto the plan tiers providers commonly sell. It also works out the upload figure separately - the number video calls live and die on, and the one providers advertise least.</p>
<h2>The rates behind the numbers</h2>
<p>4K streaming about 25 Mbps, HD streaming 8, HD video calls 4 each, online gaming 5 (latency matters more than bandwidth there), music 1, a heavy work-from-home user 10 (cloud syncs and big files), and each smart-home device roughly half a megabit. These are the usual published per-activity figures - approximations, not quotations: services compress differently, and nobody streams six 4K films at once for long. For a data-cap question instead of a speed question, the <a href="/tech/tool/data-usage-estimator/">data usage estimator</a> is the sibling tool.</p>
<h2>Notes</h2>
<p>Two honest caveats live in the result: everything shares one connection, and real-world speeds over Wi-Fi land well below the advertised figure - walls, distance and router age each take their cut. If the number says you have plenty of speed and pages still crawl, the fix is usually the router, not the plan: <a href="/tech/new-router-for-slow-internet/">new router for slow internet</a> walks that diagnosis. Nothing you enter leaves this page - the tool runs entirely in your browser.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label" for="tt-4k">4K streams at once</label><input id="tt-4k" type="number" inputmode="numeric" min="0" max="10" step="1" placeholder="1"></div>
<div class="tt-field"><label class="tt-label" for="tt-hd">HD streams at once</label><input id="tt-hd" type="number" inputmode="numeric" min="0" max="10" step="1" placeholder="1"></div>
<div class="tt-field"><label class="tt-label" for="tt-calls">Video calls at once</label><input id="tt-calls" type="number" inputmode="numeric" min="0" max="10" step="1" placeholder="1"></div>
<div class="tt-field"><label class="tt-label" for="tt-gamers">Online gamers</label><input id="tt-gamers" type="number" inputmode="numeric" min="0" max="6" step="1" placeholder="0"></div>
<div class="tt-field"><label class="tt-label" for="tt-music">Music streams</label><input id="tt-music" type="number" inputmode="numeric" min="0" max="10" step="1" placeholder="1"></div>
<div class="tt-field"><label class="tt-label" for="tt-wfh">Heavy work-from-home users</label><input id="tt-wfh" type="number" inputmode="numeric" min="0" max="6" step="1" placeholder="0"></div>
<div class="tt-field"><label class="tt-label" for="tt-smart">Smart-home devices</label><input id="tt-smart" type="number" inputmode="numeric" min="0" max="60" step="1" placeholder="5"></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-speed" class="btn">Calculate the speed I need</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>"""),

("electricity-cost-calculator", "Electricity cost calculator", "Electricity cost calculator: what any appliance really costs to run",
 "Pick an appliance, add your rate from the bill, and see the cost per hour, day, month and year in your currency. Runs entirely in your browser.",
 None,
 """<h2>What this does</h2>
<p>Every appliance has a wattage on its label. Multiply that by the hours it runs and your electricity rate, and you get what it truly costs - not the vague "a few dollars a month" utilities imply. This tool does that arithmetic instantly: pick a common appliance or enter a custom wattage, set how many hours a day it runs, and read off the hourly, daily, monthly and yearly cost.</p>
<h2>The default rates</h2>
<p>The region picker pre-fills a national reference rate so the numbers work before you touch anything: the United States average residential rate of about 18.4&cent; per kWh (US Energy Information Administration, September 2026), the UK Ofgem price-cap unit rate of 26.11p per kWh (July-September 2026), Canada at about C$0.14 and Australia at about A$0.33. These are averages and caps, not quotations - rates vary by state, region and tariff, and they change several times a year. The rate printed on <b>your</b> bill or prepaid meter always wins: overwrite the rate box with your own figure and every result updates.</p>
<h2>Notes</h2>
<p>Appliance wattages are typical figures - a space heater near 1,500 W and a tumble dryer near 3,000 W are the common values, but your model's nameplate is the truth. Appliances that cycle on and off (fridge-freezers, air conditioners) are listed at a realistic average draw, not their peak. For the data-plan side of the same question, the <a href="/tech/tool/data-usage-estimator/">data usage estimator</a> is the sibling tool. Nothing you enter leaves this page - the tool runs entirely in your browser.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label" for="tt-appliance">Appliance</label><select id="tt-appliance">
<option value="1500">Space heater - 1500 W</option>
<option value="1000">Portable air conditioner - 1000 W</option>
<option value="3500">Central air conditioning - 3500 W</option>
<option value="3000">Tumble dryer - 3000 W</option>
<option value="500">Washing machine - 500 W</option>
<option value="150">Fridge-freezer (average draw) - 150 W</option>
<option value="400">Gaming PC - 400 W</option>
<option value="100">Television - 100 W</option>
<option value="7200">EV charger (Level 2) - 7200 W</option>
<option value="custom">Custom wattage</option>
</select></div>
<div class="tt-field"><label class="tt-label" for="tt-watts">Custom wattage (W)</label><input id="tt-watts" type="number" inputmode="numeric" min="1" max="50000" step="1" placeholder="1200"></div>
<div class="tt-field"><label class="tt-label" for="tt-hours">Hours running per day</label><input id="tt-hours" type="number" inputmode="decimal" min="0.1" max="24" step="0.5" placeholder="4"></div>
<div class="tt-field"><label class="tt-label" for="tt-region">Region (pre-fills the rate)</label><select id="tt-region">
<option value="0.184|$">United States - about $0.184/kWh (EIA average)</option>
<option value="0.2611|&pound;">United Kingdom - &pound;0.2611/kWh (Ofgem cap)</option>
<option value="0.14|C$">Canada - about C$0.14/kWh</option>
<option value="0.33|A$">Australia - about A$0.33/kWh</option>
<option value="custom">My own rate</option>
</select></div>
<div class="tt-field"><label class="tt-label" for="tt-rate">Your rate per kWh</label><input id="tt-rate" type="number" inputmode="decimal" min="0.01" max="5" step="0.001" placeholder="0.184"></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-calc" class="btn">Calculate running cost</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("ai-subscription-cost-comparer", "AI subscription comparer", "AI subscription cost comparer: what your stack really adds up to",
 "Tick the AI subscriptions you pay for, correct any price, and see the monthly, yearly and per-day cost - biggest line first. Runs entirely in your browser.",
 None,
 """<h2>What this does</h2>
<p>AI subscriptions stack quietly: a chat assistant here, an image tool there, a search upgrade nobody remembers approving. Tick what you pay for, correct any price that has changed (prices move often - the defaults were right in September 2026), and the tool totals the stack per month, per year and per day, biggest line first.</p>
<h2>The defaults and the honest caveats</h2>
<p>The pre-filled prices are the standard paid tiers as of September 2026: ChatGPT Plus 20, Claude Pro 20, Google AI Pro 19.99, Perplexity Pro 20, Microsoft Copilot Pro 20, SuperGrok 30, Midjourney from 10. Plans, names and prices change frequently, annual billing usually knocks roughly two months off the effective yearly price (enter the annual price divided by twelve), and free tiers are everywhere - the tool only totals what you tick. The interesting question it answers is not "can I afford it" but "do I still use the second and third one": the usual saving is cancelling the tool that overlaps the biggest one, for a month, as an experiment.</p>
<h2>Notes</h2>
<p>Everything runs on this page - your list of subscriptions never leaves the browser, and there is nothing to sign into. If you are weighing a first paid AI subscription rather than a stack, the honest starting point is one general assistant at 20 a month for three months before adding anything narrower.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-chatgpt"> ChatGPT Plus</label><input id="tt-chatgpt-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" value="20"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-claude"> Claude Pro</label><input id="tt-claude-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" value="20"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-gemini"> Google AI Pro</label><input id="tt-gemini-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" value="19.99"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-perplexity"> Perplexity Pro</label><input id="tt-perplexity-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" value="20"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-copilot"> Microsoft Copilot Pro</label><input id="tt-copilot-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" value="20"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-grok"> SuperGrok</label><input id="tt-grok-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" value="30"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-midjourney"> Midjourney</label><input id="tt-midjourney-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" value="10"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-custom"> Another subscription</label>
<input id="tt-custom-p" type="number" inputmode="decimal" min="0" max="250" step="0.01" placeholder="price per month"></div>
<div class="tt-field"><label class="tt-label" for="tt-months">Months you will keep them this year</label><input id="tt-months" type="number" inputmode="numeric" min="1" max="12" step="1" value="12"></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-calc" class="btn">Add up the stack</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("video-file-size-estimator", "Video file size estimator", "Video file size estimator",
 "Pick resolution, frame rate, codec and length - get the file size before you record, or before that upload fails. Runs entirely in your browser.",
 None,
 """<h2>What this does</h2>
<p>Video files are just bitrates wearing a stopwatch: bits per second, times seconds. Pick the resolution, frame rate, codec and length, and the tool multiplies the typical bitrate for that combination into a file size - useful before a recording, before a platform upload that has a limit, or before blaming the internet for what is simply a heavy file.</p>
<h2>The bitrate table behind the numbers</h2>
<p>The estimates use typical mid-quality H.264 bitrates at 30 frames per second: about 40 Mbps for 4K, 20 for 1440p, 10 for 1080p, 5 for 720p and 2.5 for 480p - close to the figures platforms publish for uploads. Frame rate scales from there (24fps slightly lighter, 60fps roughly 1.7 times), and newer codecs cut the bitrate for the same visible quality: HEVC/H.265 lands around half the H.264 figure, AV1 a little lower again. These are shapes, not quotes - real encoders, scene complexity and camera settings move results by a fifth or more either way. Many phones record 4K in HEVC by default; if your files look small for 4K, that is why.</p>
<h2>Notes</h2>
<p>The estimate is deliberately conservative-middle: fast action and grain (rain, crowds, sensor noise) inflate size; static scenes shrink it. Platforms re-encode everything on upload anyway, so the file you send is not the file viewers get - it just has to survive the trip. For that trip's length, the <a href="/tech/tool/upload-time-calculator/">upload time calculator</a> is the sibling tool; for what the editing PC costs to run, the <a href="/tech/tool/electricity-cost-calculator/">electricity cost calculator</a> prices any wattage. Nothing you pick here leaves the page.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label" for="tt-res">Resolution</label><select id="tt-res">
<option value="40|4K (2160p)">4K (2160p) - about 40 Mbps H.264</option>
<option value="20|2K (1440p)">2K (1440p) - about 20 Mbps</option>
<option value="10|Full HD (1080p)" selected>Full HD (1080p) - about 10 Mbps</option>
<option value="5|HD (720p)">HD (720p) - about 5 Mbps</option>
<option value="2.5|SD (480p)">SD (480p) - about 2.5 Mbps</option>
</select></div>
<div class="tt-field"><label class="tt-label" for="tt-fps">Frame rate</label><select id="tt-fps">
<option value="0.85|24 fps">24 fps (cinematic)</option>
<option value="1|30 fps" selected>30 fps</option>
<option value="1.7|60 fps">60 fps (smooth/sports/gaming)</option>
</select></div>
<div class="tt-field"><label class="tt-label" for="tt-codec">Codec / efficiency</label><select id="tt-codec">
<option value="1|H.264">H.264 (most common)</option>
<option value="0.55|HEVC / H.265">HEVC / H.265 (about half the size)</option>
<option value="0.45|AV1">AV1 (newest, smallest)</option>
</select></div>
<div class="tt-field"><label class="tt-label" for="tt-audio">Audio</label><select id="tt-audio">
<option value="0.128|standard stereo">Standard stereo (128 kbps)</option>
<option value="0.256|high-quality stereo">High-quality stereo (256 kbps)</option>
<option value="0.448|surround 5.1">Surround 5.1 (448 kbps)</option>
<option value="0|no audio">No audio</option>
</select></div>
<div class="tt-field"><label class="tt-label" for="tt-min">Length in minutes</label><input id="tt-min" type="number" inputmode="numeric" min="0.5" max="100000" step="0.5" placeholder="10"></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-calc" class="btn">Estimate the file size</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("upload-time-calculator", "Upload time calculator", "Upload time calculator",
 "File size in, upload speed in - get the realistic transfer time, plus what your connection actually moves per hour. Runs entirely in your browser.",
 None,
 """<h2>What this does</h2>
<p>Enter a file size and your measured upload speed, and the calculator converts the marketing units into time: hours and minutes for that video backup, that course recording, that photo library. It also translates the speed into what it means per hour, which is usually the more honest number - a "fast" connection that uploads at 20 Mbps moves under 9 GB an hour.</p>
<h2>Use a measured speed, not the plan's number</h2>
<p>The speed that matters is the <b>upload</b> figure from a speed test run on the machine and connection you will actually upload from - not the headline plan speed, which is usually the download. Advertised upload speeds are "up to" figures; cable connections are typically much slower upward than downward, while fibre is often symmetrical. Wi-Fi, an older router, and anything else using the network during the transfer all take a cut, which is why the result includes a plan-for-it figure about fifteen percent above the ideal.</p>
<h2>Notes</h2>
<p>Sizes use decimal units (1 GB = 1,000 MB), matching how internet speeds are quoted. If the file in question is a video you have not made yet, the <a href="/tech/tool/video-file-size-estimator/">video file size estimator</a> sizes it first - the two tools in sequence answer "can I get this there tonight". Nothing you enter leaves this page.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label" for="tt-size">File size</label><input id="tt-size" type="number" inputmode="decimal" min="0.1" max="1000000" step="any" placeholder="2.5"></div>
<div class="tt-field"><label class="tt-label" for="tt-unit">Unit</label><select id="tt-unit">
<option value="1">MB</option>
<option value="1000">GB</option>
</select></div>
<div class="tt-field"><label class="tt-label" for="tt-speed">Your upload speed (Mbps)</label><input id="tt-speed" type="number" inputmode="decimal" min="0.1" max="10000" step="any" placeholder="20"></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-calc" class="btn">Calculate the upload time</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),

("password-strength-checker", "Password strength checker", "Password strength checker",
 "Check how a password holds up against real cracking methods - length, dictionary, patterns, reuse risks - with honest verdicts and fixes. Runs entirely in your browser.",
 None,
 """<h2>What this does</h2>
<p>Type a password and the checker scores it the way a cracking rig would: length first, then character variety, then the dictionary - because attacks start with lists of leaked passwords, not with every possible combination. The verdict comes with the reasoning: which weaknesses were found, how long the password would typically survive against a stolen-database attack versus a website's throttled login form, and what specifically would strengthen it.</p>
<h2>What it knows about</h2>
<p>The usual weaknesses: world-class common passwords (it is not a coincidence detector - swapped letters like @ for a are checked too), embedded dictionary words, keyboard runs (qwerty and friends), sequences, repeated characters, all-digit passwords, and years bolted onto names. What it can never know: whether you reuse this password elsewhere - which is the single risk it cannot measure and the one that causes the most real damage.</p>
<h2>Notes</h2>
<p>The maths is honest entropy estimation with human-shaped penalties - conservative, not optimistic. Nothing you type is stored, logged or transmitted; the page holds no network connection and the checker cannot phone home even if it wanted to. The output teaches the pattern worth learning: length beats complexity, uniqueness beats everything, and a password manager turns the whole problem off.</p>""",
 """<div class="tt-grid">
<div class="tt-field"><label class="tt-label" for="tt-pw">Password to check</label><input id="tt-pw" type="password" autocomplete="off" spellcheck="false" placeholder="type or paste"></div>
<div class="tt-field"><label class="tt-label"><input type="checkbox" id="tt-show"> show what I typed</label></div>
</div>
<div class="tt-btnrow"><button type="button" id="tt-calc" class="btn">Check the strength</button></div>
<pre id="tt-out" class="tt-out" aria-live="polite"></pre>
<p id="tt-msg" class="tt-msg" aria-live="polite"></p>"""),
]