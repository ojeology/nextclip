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
]
