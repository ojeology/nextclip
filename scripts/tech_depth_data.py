# -*- coding: utf-8 -*-
"""BRYME Tech desk depth sections (Phase 3 tranche 6). Applied post-build by
scripts/inject-tech-depth.py into both the tech/ source tree and public/tech/.

Every entry is desk-written guidance: how the tool actually works, where its
numbers are approximations, what it cannot tell you, and what to do instead.
External references are restricted to URLs verified live at authoring time."""

MDN_HTTP = "https://developer.mozilla.org/en-US/docs/Web/HTTP"
MDN_B64 = "https://developer.mozilla.org/en-US/docs/Glossary/Base64"
RFC3986 = "https://datatracker.ietf.org/doc/html/rfc3986"
RFC4122 = "https://www.rfc-editor.org/rfc/rfc4122"
RFC8446 = "https://datatracker.ietf.org/doc/html/rfc8446"
JSON_ORG = "https://www.json.org/json-en.html"
OWASP = "https://owasp.org/www-project-top-ten/"
NIST = "https://csrc.nist.gov/"
EFF = "https://www.eff.org/"
HIBP = "https://haveibeenpwned.com/"
WEBDEV = "https://web.dev/"
CANIUSE = "https://caniuse.com/"
IANA_MT = "https://www.iana.org/assignments/media-types/media-types.xhtml"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

TECH_DEPTH = {

"tool/word-counter": """
<h2>How this counter counts, and why other counters disagree</h2>
<p>Word counting looks like arithmetic and behaves like a policy decision. This tool splits on whitespace and punctuation boundaries, so "state-of-the-art" counts as one word and "don't" counts as one — the same convention most word processors use. Other tools make different choices: some split hyphenated compounds into two, some count each contraction as two, and most count CJK text by character rather than by word, which changes the figure for Japanese or Chinese by an order of magnitude. If a submission limit matters (a competition entry, a journal abstract, a 280-character post), check the organiser's own counter rather than trusting any tool, including this one.</p>
<p>The reading-time figure deserves the same scepticism. It divides your word count by a fixed pace — 200 words per minute here, which is a deliberate middle setting. Silent reading of dense technical prose runs slower, often 150 wpm; skimming a listicle runs faster. So the number is a planning estimate, not a promise: a 1,200-word explainer is roughly six minutes for an engaged reader and ninety seconds for a scanner, and both are correct.</p>
<h3>What the counts are genuinely useful for</h3>
<ul>
<li><b>Length discipline.</b> The fastest editorial use is not the total but the delta: paste a draft, cut until the number drops 20 percent, and read what you removed. Most writers discover the cut version is the better piece.</li>
<li><b>Format limits.</b> Meta descriptions, ad copy, subject lines and social posts all have hard limits. Check the actual character limit with the counter rather than guessing from a word count.</li>
<li><b>Billing and quoting.</b> Freelancers paid by the word need a documented count. Note that publishers count their own way, so quote ranges and confirm in writing.</li>
<li><b>Speaking time.</b> Spoken delivery is slower than reading — roughly 130–150 words per minute for a talk. Divide by 140 for a script, not by 200.</li>
</ul>
<p>Two honest limitations. First, nothing here analyses quality: a page can hit every length target and still be unreadable, which is why the desk's editorial guidance lives in the guides rather than the toolbox. Second, this tool runs entirely in your browser — text is never sent anywhere, which matters more than it sounds when the draft in the box is a client's unreleased material. If you want to understand how browsers handle text and input in the first place, the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP" rel="noopener">MDN web documentation</a> is the reference layer, and the <a href="https://en.wikipedia.org/wiki/Special:Search?search=word+count" rel="noopener">word-count reference material on Wikipedia</a> explains why the counting conventions differ across languages.</p>
<p>Related desk tools: the <a href="/tech/tool/case-converter/">case converter</a> for cleaning pasted text, the <a href="/tech/tool/json-formatter/">JSON formatter</a> when the text is data, and the <a href="/tech/browser-problems/">browser troubleshooting guide</a> if a paste behaves oddly.</p>""",

"tool/case-converter": """
<h2>Case conversion: what each mode is actually for</h2>
<p>Changing letter case looks trivial until a title goes wrong in production. The modes here map to real conventions, and knowing which convention you are targeting is the whole skill.</p>
<ul>
<li><b>Sentence case</b> — first word capitalised, the rest lower. The default for headings on the web, and the style most style guides now prefer because it reads faster and avoids the "Which Words Are Proper?" trap.</li>
<li><b>Title Case</b> — major words capitalised, short function words (of, the, and, to) usually lower. Used by many publications and by bibliographic styles; the rules differ between guides, which is why two publications can title-case the same sentence differently and both be right.</li>
<li><b>lowercase / UPPERCASE</b> — lowercase for identifiers, tags and slugs; uppercase only for genuine emphasis or acronyms. Entire sentences in caps read as shouting and are measurably harder to scan.</li>
<li><b>camelCase, snake_case, kebab-case</b> — these are code conventions, not typography. camelCase for JavaScript identifiers, snake_case for Python and database columns, kebab-case for URLs and CSS custom properties. Pasting prose into these modes produces garbage; use them on identifiers.</li>
</ul>
<p>The failure mode worth naming: automated case conversion cannot know your proper nouns. It will happily produce "the eiffel tower" or "IBM" as "Ibm", and it has no way to know that "iOS" and "eBay" begin with a deliberate lowercase letter. Treat any bulk conversion as a first pass that needs one human read, especially before the text goes into a title tag or a printed document.</p>
<p>Two technical notes. Case folding is not purely cosmetic in software: string comparisons, file names on case-sensitive systems and database lookups all depend on it, and the formal rules live in the Unicode standard rather than in any one language — the <a href="https://en.wikipedia.org/wiki/Special:Search?search=letter+case" rel="noopener">letter-case reference material on Wikipedia</a> covers the historical and technical background. Second, this tool works on the text in your browser and sends nothing anywhere, so client names and unpublished copy stay where they started.</p>
<p>Practical pairings: convert first, then count with the <a href="/tech/tool/word-counter/">word counter</a> (some length limits are case-sensitive), and if the text is a URL, use the <a href="/tech/tool/url-encoder/">URL encoder</a> rather than case tools — URLs have their own rules, specified in <a href="https://datatracker.ietf.org/doc/html/rfc3986" rel="noopener">RFC 3986</a>, and case is only one of several things that can break a link.</p>""",

"tool/uuid-generator": """
<h2>What a UUID is, and when you actually want one</h2>
<p>A UUID (universally unique identifier) is a 128-bit value written as 32 hexadecimal digits in five groups, defined in <a href="https://www.rfc-editor.org/rfc/rfc4122" rel="noopener">RFC 4122</a>. The point is not that it is random — it is that the space is so large that two systems generating them independently will not collide in practice, which lets you create identifiers without a central authority. That single property is why they appear everywhere: database primary keys, session tokens, file names in object storage, log correlation IDs, and the device identifiers that advertisers argue about.</p>
<p>The version matters more than most people realise. Version 4 is random — the common default, and what this tool generates. Versions 1 and 6 embed a timestamp and a node identifier, which means they sort chronologically (useful for database indexes) but leak the time and machine they were created on. Version 5 is name-based: the same namespace and name always produce the same UUID, which makes it a deterministic key rather than an identifier you can hand out freely. If you are choosing one for a system, the question is whether you need randomness, sortability, or reproducibility — those pull in different directions.</p>
<h3>Where UUIDs are the wrong tool</h3>
<ul>
<li><b>Sequential public identifiers.</b> Invoice numbers, ticket numbers and anything a human types are better short and sequential. A UUID in a support email is an accessibility problem as much as a design one.</li>
<li><b>Passwords and secrets.</b> A v4 UUID has 122 bits of entropy, which is respectable, but it was not designed as a credential and cannot be rotated or revoked like a real secret. Use a proper password manager instead — see the desk's <a href="/tech/tool/password-strength-checker/">strength checker</a> for why length beats cleverness.</li>
<li><b>Anonymous tracking.</b> UUIDs are pseudonymous, not anonymous: the same ID attached to a person's activity over time identifies them as reliably as a name does. The <a href="https://www.eff.org/" rel="noopener">Electronic Frontier Foundation</a> tracks exactly this class of surveillance.</li>
</ul>
<p>Two practical notes. First, uniqueness is a property of the generator, not of the string: a UUID produced by a broken random source (a predictable seed, a virtual machine cloned mid-boot) is only as unique as that source, which is a real class of production incident. Use your platform's cryptographic random function, never a hand-rolled one. Second, this tool generates values in your browser using the browser's own random source and sends nothing anywhere — so identifiers you generate here are not logged, and you can use it for throwaway test data without leaking your schema.</p>
<p>If you are picking identifiers for a real system, the background on how the versions differ is summarised in the <a href="https://en.wikipedia.org/wiki/Special:Search?search=universally+unique+identifier" rel="noopener">UUID reference material on Wikipedia</a>, and the desk's <a href="/tech/ai-privacy-what-not-to-paste/">privacy guide</a> covers what to avoid pasting into any online tool.</p>""",

"tool/base64-encoder": """
<h2>What Base64 does, and the trap it sets</h2>
<p>Base64 is an encoding, not encryption — and the confusion between those two words causes real security incidents. Base64 takes binary data and rewrites it as 64 printable characters (A–Z, a–z, 0–9, plus and slash) so it can survive systems that only handle text: email attachments, JSON payloads, data URLs in web pages, HTTP headers. Anyone can decode it in one step, with no key, which is exactly what the <a href="https://developer.mozilla.org/en-US/docs/Glossary/Base64" rel="noopener">MDN Base64 entry</a> stresses. If you are protecting something, Base64 is the wrong instrument; the standard for encrypted transport is TLS, specified in <a href="https://datatracker.ietf.org/doc/html/rfc8446" rel="noopener">RFC 8446</a>.</p>
<p>The practical cost worth knowing: Base64 makes data about 33 percent larger. Three bytes become four characters, which is why embedding images as Base64 in a web page can quietly inflate it — a technique that used to save HTTP requests and now usually loses to plain caching. If you are debugging a slow page and find a wall of Base64 in the HTML, that is your answer.</p>
<h3>Where Base64 legitimately shows up</h3>
<ul>
<li><b>Data URLs</b> — small inline images and fonts, where the request overhead genuinely exceeds the size penalty.</li>
<li><b>API payloads</b> — binary blobs (PDFs, images, signatures) carried inside JSON, which has no binary type. The format itself is defined at <a href="https://www.json.org/json-en.html" rel="noopener">json.org</a>.</li>
<li><b>Email attachments</b> — the original reason the encoding exists, since SMTP was designed for seven-bit text.</li>
<li><b>Debugging</b> — decoding an opaque string in a config file or a cookie to see whether it is text underneath. Most "mysterious encrypted token" strings turn out to be plain Base64.</li>
</ul>
<p>Two warnings from the desk. First, decoding an untrusted Base64 string is fine; <em>executing</em> whatever it contains is not — malicious payloads are routinely shipped as Base64 precisely because it looks like noise, which is why the <a href="https://owasp.org/www-project-top-ten/" rel="noopener">OWASP Top Ten</a> treats unvalidated input as a first-class risk. Second, never paste a live credential, private key or customer record into any web tool. This encoder runs entirely in your browser and transmits nothing, which is the point of keeping it here rather than sending you to a third-party site — but the habit matters more than the tool, and the desk's <a href="/tech/ai-privacy-what-not-to-paste/">guide on what not to paste</a> is the longer version of that argument.</p>
<p>Related: the <a href="/tech/tool/url-encoder/">URL encoder</a> for text going into a query string (a different job — URL encoding is about reserved characters, not binary), and the <a href="/tech/tool/json-formatter/">JSON formatter</a> when the Base64 is a field inside a payload.</p>""",

"tool/timestamp-converter": """
<h2>Unix time, and why it bites people in 2038 and 2001</h2>
<p>A Unix timestamp counts the seconds since 00:00:00 UTC on 1 January 1970 — the "epoch." It is a single number, so it stores compactly, compares cheaply, and carries no time-zone ambiguity: the same number means the same instant everywhere on Earth. That last property is the whole reason the format exists, and it is also why converting it back to a human-readable date requires you to say which zone you want. "1700000000" is one instant and 24 different wall-clock readings.</p>
<p>Three conventions cause most conversion errors. First, seconds versus milliseconds: JavaScript's <code>Date.now()</code> returns milliseconds, most Unix tools return seconds, and mixing them puts you in 1970 or the year 55,000. If a converted date looks absurd, divide or multiply by 1,000 before investigating anything else. Second, the zone: this tool converts to UTC and to your local zone, but a date written as "2026-03-15" without a zone is genuinely ambiguous — databases and logs disagree about it constantly. Third, daylight saving: a timestamp is unambiguous, but the local time derived from it can repeat or skip an hour twice a year, which is why "one hour off" bugs cluster around March and October.</p>
<h3>The 2038 problem, in one paragraph</h3>
<p>Timestamps stored in a signed 32-bit integer overflow at 03:14:07 UTC on 19 January 2038, wrapping to 1901. This is a real deadline for embedded devices, old file formats and any database column defined as a 32-bit int. Systems that moved to 64-bit integers are unaffected for billions of years. If you maintain anything with a date column, check its type now rather than in 2037 — the background is in the <a href="https://en.wikipedia.org/wiki/Special:Search?search=year+2038+problem" rel="noopener">Year 2038 problem reference material on Wikipedia</a>, and it is the same class of bug as the Y2K panic, only smaller and easier to fix.</p>
<p>Practical uses on this desk: reading log files (most server logs are timestamps plus an IP and a status — the status codes come from <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP" rel="noopener">the HTTP specification</a>), verifying that a scheduled job ran when you think it did, comparing two systems' clocks when one appears to be "wrong," and decoding JWT tokens and certificate validity windows, which are timestamp pairs. The <a href="/tech/tool/data-usage-estimator/">data-usage estimator</a> and the <a href="/tech/tool/upload-time-calculator/">upload calculator</a> solve the adjacent problem of turning a rate and a size into a duration.</p>
<p>One privacy note, because it applies to every tool on this desk: conversions run in your browser. Timestamps from a client's logs stay in your browser.</p>""",

"tool/json-formatter": """
<h2>Formatting JSON, and reading the errors it reveals</h2>
<p>JSON is a small, strict format — the whole grammar fits on one page at <a href="https://www.json.org/json-en.html" rel="noopener">json.org</a> — and its strictness is why formatting tools earn their place. Two rules cause most failures: no trailing comma after the last item in an object or array, and strings must use double quotes (single quotes are invalid, which trips up anyone coming from JavaScript object literals). A payload that fails to parse is almost always one of those two, or an unescaped quote inside a string.</p>
<p>Pretty-printing is not cosmetic. Indentation turns a 4,000-character single line into something you can scan, and it makes the nesting depth visible — which is usually where the actual bug lives. When an API returns something unexpected, the first diagnostic step is not reading the documentation but reformatting the response and looking at its shape: is the data where you expected it, is it a string where you expected an array, is a field simply missing? Those three questions resolve most integration bugs before any code changes.</p>
<h3>What formatting cannot fix</h3>
<ul>
<li><b>Semantic errors.</b> Valid JSON can be completely wrong data — a null where a number belongs, an ISO date as a plain string, an ID as a float that has already lost precision. Parsing success tells you nothing about correctness.</li>
<li><b>Truncated payloads.</b> A response cut off mid-stream is invalid JSON no matter how you format it. If the end of the document is missing, check the network layer, not the syntax.</li>
<li><b>Size problems.</b> Pretty-printing multiplies the byte count. Format for reading, send minified.</li>
</ul>
<p>A precision note that catches experienced developers: JSON numbers are commonly parsed as IEEE-754 doubles, so integers beyond about 2^53 lose exactness. Large IDs (snowflake IDs, some database keys) should travel as strings, and if you see a large ID ending in zeros after a round trip, that is why. The formal behaviour of the underlying number type is documented in the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP" rel="noopener">MDN web documentation</a> and the JSON specification itself.</p>
<p>How this desk uses it: decoding API responses while verifying a service's claims, inspecting a website's structured data (the JSON-LD blocks that power rich search results), and checking that a form's payload contains what the privacy policy says it does — the last of which is the practical side of the <a href="/tech/ai-privacy-what-not-to-paste/">what-not-to-paste guide</a>. Everything runs in your browser; nothing is uploaded, which matters when the payload contains real customer records.</p>
<p>Adjacent tools: the <a href="/tech/tool/base64-encoder/">Base64 encoder</a> when a field inside the JSON is an encoded blob, and the <a href="/tech/tool/timestamp-converter/">timestamp converter</a> for the epoch values JSON APIs love to return.</p>""",

"tool/url-encoder": """
<h2>URL encoding: the reserved characters that break links</h2>
<p>A URL is a formal grammar, specified in <a href="https://datatracker.ietf.org/doc/html/rfc3986" rel="noopener">RFC 3986</a>, and only a limited set of characters may appear unencoded. Everything else — spaces, non-ASCII letters, and the characters that already mean something in a URL (<code>? &amp; = # / %</code> and friends) — must be percent-encoded: a percent sign followed by two hex digits. A space becomes <code>%20</code>, an ampersand becomes <code>%26</code>. Skipping this is why a search query containing "AT&amp;T" or "Côte d'Ivoire" arrives at the server truncated or mangled.</p>
<p>The trap worth knowing: encoding applies to the <em>value</em>, not the whole URL. Percent-encode the query parameter and you get a working link; percent-encode the entire URL and you get <code>https%3A%2F%2Fexample.com</code>, which is a string, not a link. The distinction between "encode the component" and "encode the string" is the difference between the two functions most languages expose (<code>encodeURIComponent</code> versus <code>encodeURI</code> in JavaScript), and confusing them is a perennial source of broken deep links.</p>
<h3>The common real-world cases</h3>
<ul>
<li><b>Spaces.</b> Legal in a search box, illegal in a URL. Depending on the context they become <code>%20</code> or <code>+</code> — form submissions traditionally use <code>+</code>, path components require <code>%20</code>. Servers usually accept both in queries; do not rely on it in paths.</li>
<li><b>Non-English text.</b> Encoded as UTF-8 bytes, each byte percent-encoded. A URL with raw accented characters often "works" in one browser and fails in a crawler, a messaging app or an email client.</li>
<li><b>Ampersands inside a value.</b> The single most common breakage: <code>?name=AT&amp;T</code> reads as two parameters. Encode it and the value survives.</li>
<li><b>Hashes.</b> A literal <code>#</code> in a value truncates the URL at that point, because <code>#</code> begins the fragment identifier.</li>
</ul>
<p>Two desk notes. First, encoding is not a security measure: percent-encoding is trivially reversible and attackers use double-encoding to slip payloads past naive filters, which is why the <a href="https://owasp.org/www-project-top-ten/" rel="noopener">OWASP Top Ten</a> insists on validating decoded input rather than filtering the encoded form. Second, over-encoding is as broken as under-encoding — a URL that arrives as <code>%2520</code> has been encoded twice, and the fix is upstream, not in another decode pass.</p>
<p>Related: the <a href="/tech/tool/base64-encoder/">Base64 encoder</a> (a different job — binary to text, not text to URL-safe text), the <a href="/tech/tool/json-formatter/">JSON formatter</a> when the query carries a serialised object, and the desk's <a href="/tech/browser-problems/">browser troubleshooting guide</a>, where malformed URLs show up as mystery redirects.</p>""",

}
