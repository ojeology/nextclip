# -*- coding: utf-8 -*-
"""Tech master build M4 — Python practicals (6 pieces, Sept 2026).

HARD GATE honoured: every executable code block in these articles was extracted and run
in a real Python 3.13 sandbox before publishing (parse/JSON against fixture files, the API
calls live against api.github.com, the retry ladder against a local 429-then-200 server,
sqlite in a temp dir, the sched job to completion, the Flask app via test_client, gunicorn
version-checked). Cron lines / requirements.txt / start commands are config, marked as such.
Sources: official Python docs + primary product docs only.
"""

TECH_MASTER_M4 = [

("parse-json-python", "coding", "guide",
"How to parse JSON in Python (and fix the errors everyone hits)",
"json.loads vs json.load, safe access to nested data, the datetime gotcha, and how to read a JSONDecodeError by line and column.",
"""<p>Python ships the whole JSON toolchain in its standard library &mdash; no installation, one import. The entire skill is four functions and a handful of habits, so here is the practical version: parsing, safe access, the error that starts every debugging session, and the type error that ambushes everyone once.</p>
<h2>Parsing: loads vs load</h2>
<p>The one-letter distinction confuses people forever: <code>loads</code> parses a <em>string</em>, <code>load</code> (no s) reads from an <em>open file</em>. In practice:</p>
<pre><code>import json

raw = '{"city": "Lagos", "temp_c": 27.5, "days": ["Mon", "Tue"]}'
data = json.loads(raw)

print(data["city"])
print(data["days"][0])
print(data.get("humidity", "not reported"))</code></pre>
<p>JSON objects become Python dictionaries, arrays become lists, and the value types map cleanly (string, number, boolean, null &rarr; <code>None</code>). The <code>.get()</code> line is the habit worth stealing: missing keys raise <code>KeyError</code> with square brackets, and API responses omit fields all the time &mdash; <code>.get("key", default)</code> turns that into a non-event.</p>
<p>Reading from a file is the same idea with <code>load</code>:</p>
<pre><code>import json

with open("weather.json", encoding="utf-8") as f:
    data = json.load(f)

clean = json.dumps(data, indent=2, sort_keys=True)
print(clean[:200])</code></pre>
<p><code>dumps</code> is the reverse (Python &rarr; JSON string), and <code>indent=2</code> is what makes it readable &mdash; the same transformation the <a href="/tech/tool/json-formatter/">JSON formatter tool</a> does in your browser.</p>
<h2>Reading the error instead of fearing it</h2>
<p>Invalid JSON raises <code>json.JSONDecodeError</code>, and it is a genuinely helpful exception &mdash; it tells you exactly where the parse died:</p>
<pre><code>import json

broken = '{"city": "Lagos", "temp_c": }'

try:
    json.loads(broken)
except json.JSONDecodeError as e:
    print(f"Line {e.lineno}, column {e.colno}: {e.msg}")</code></pre>
<p>Ninety percent of real-world JSON errors are one of the format's three strictness rules &mdash; single quotes instead of double, a trailing comma, or a comment where comments aren't allowed (the reasons live in <a href="/tech/what-is-json/">what JSON actually is</a>). Run the parse, read the line and column, look there first.</p>
<h2>The one ambush: non-JSON types</h2>
<p><code>dumps</code> happily serialises dicts, lists, strings, numbers, booleans and <code>None</code> &mdash; and raises <code>TypeError</code> on everything else, most often <code>datetime</code> objects. The standard fix is to convert to a string yourself before serialising (<code>dt.isoformat()</code> is the conventional choice) rather than teaching the serialiser tricks. If a script reads timestamps from an API, they arrive as <em>strings</em>; converting them with <code>datetime.fromisoformat()</code> beats arithmetic on text every time. What to do with parsed data next &mdash; storing it properly &mdash; is the follow-up: <a href="/tech/store-api-data-python/">SQLite, in a few honest lines</a>.</p>""",
[("Python docs \u2014 the json module (loads, load, dumps, JSONDecodeError)", "https://docs.python.org/3/library/json.html"),
 ("IETF RFC 8259 \u2014 the JSON format these functions implement", "https://www.rfc-editor.org/rfc/rfc8259")],
[("what-is-json", "What JSON actually is"),
 ("store-api-data-python", "Storing API data in SQLite")]),

("call-api-python", "coding", "guide",
"How to call an API with Python (standard library only)",
"urllib.request from first principles: headers that matter, timeouts that save you, query parameters that don't get mangled, and where the requests library fits.",
"""<p>You do not need a third-party library to call an API from Python &mdash; the standard library's <code>urllib.request</code> does the whole job, and learning it first means you understand what every fancier library is doing for you. This piece is the working pattern: build a request, set the headers that matter, always set a timeout, read the response.</p>
<h2>The minimal real call</h2>
<pre><code>import json
import urllib.request

url = "https://api.github.com/zen"
req = urllib.request.Request(url, headers={"User-Agent": "bryme-demo/1.0"})

with urllib.request.urlopen(req, timeout=10) as resp:
    print("Status:", resp.status)
    body = resp.read().decode("utf-8")

print(body)</code></pre>
<p>Three deliberate details. The <strong>User-Agent header</strong>: many APIs reject or throttle default Python clients, and a named, honest identifier is both polite and required by some providers. The <strong>timeout</strong>: without it, a stuck server can hang your program indefinitely &mdash; ten seconds is a sane default for most APIs. And the <strong>context manager</strong> (<code>with</code>): it closes the connection deterministically instead of leaving cleanup to luck. The response body arrives as bytes; <code>.decode("utf-8")</code> turns it into text, and if the endpoint promises JSON, <code>json.loads</code> on that text gives you data structures &mdash; the full move is in <a href="/tech/parse-json-python/">parsing JSON in Python</a>.</p>
<h2>Query parameters without the string surgery</h2>
<p>Hand-building URLs with f-strings breaks the first time a value contains a space or an ampersand. <code>urlencode</code> does the escaping correctly:</p>
<pre><code>from urllib.parse import urlencode
import json
import urllib.request

params = urlencode({"q": "json parsing", "per_page": "3"})
url = "https://api.github.com/search/repositories?" + params
req = urllib.request.Request(url, headers={"User-Agent": "bryme-demo/1.0"})

with urllib.request.urlopen(req, timeout=10) as resp:
    results = json.loads(resp.read().decode("utf-8"))

for item in results["items"]:
    print(item["full_name"])</code></pre>
<p>This is also where URL-encoding stops being trivia: <code>urlencode</code> percent-encodes every value the way the server expects &mdash; the same transformation as the <a href="/tech/tool/url-encoder/">URL encoder tool</a>.</p>
<h2>Where requests fits</h2>
<p>The third-party <a href="https://requests.readthedocs.io/" rel="noopener">requests</a> library is the community favourite, and for good reason: <code>requests.get(url, params=..., timeout=10)</code> compresses the ceremony while keeping the same shape &mdash; headers, parameters, timeouts, then <code>.json()</code> on the response. Install it with <code>pip install requests</code> when a project justifies a dependency. Everything you learned with urllib transfers directly, including the part that matters most when calls go wrong: <a href="/tech/handle-api-errors-python/">the error-handling ladder</a>.</p>""",
[("Python docs \u2014 urllib.request", "https://docs.python.org/3/library/urllib.request.html"),
 ("Python docs \u2014 urllib.parse (urlencode)", "https://docs.python.org/3/library/urllib.parse.html"),
 ("requests \u2014 the third-party library, for comparison", "https://requests.readthedocs.io/")],
[("parse-json-python", "Parsing JSON in Python"),
 ("handle-api-errors-python", "Handling API errors properly")]),

("handle-api-errors-python", "coding", "guide",
"How to handle API errors in Python (status codes, timeouts, retries)",
"The exception ladder that keeps an API client alive: HTTPError first (and read its body), URLError for the network, and a polite retry for 429 and 5xx.",
"""<p>A demo API call works on the good day it was written. A useful one works on every other day too &mdash; which means handling the two failure classes separately: the server answered with an error (an <code>HTTPError</code>), and the server effectively didn't answer at all (a <code>URLError</code> or a timeout). urllib keeps the ladder short, but the order matters.</p>
<h2>The ladder, and why the order matters</h2>
<p><code>HTTPError</code> is a <em>subclass</em> of <code>URLError</code>. Catch HTTPError first or the generic parent swallows every meaningful status code and you learn nothing. Here is the pattern worth copying &mdash; a retry wrapper that handles the two retryable cases politely (rate limits and server hiccups) and fails fast on everything else:</p>
<pre><code>import json
import time
import urllib.error
import urllib.request

def fetch_with_retry(url, retries=3):
    req = urllib.request.Request(url, headers={"User-Agent": "bryme-demo/1.0"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            print(f"HTTP {e.code}: {detail[:120]}")
            if e.code == 429:
                wait = e.headers.get("Retry-After", "2")
                time.sleep(int(wait) if wait.isdigit() else 2)
                continue
            if e.code &gt;= 500 and attempt &lt; retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
        except urllib.error.URLError as e:
            print(f"Network problem: {e.reason}")
            raise
    raise RuntimeError("retries exhausted")</code></pre>
<p>Four habits are embedded in those lines. <strong>Read the error body:</strong> <code>e.read()</code> &mdash; good APIs put the actual explanation in the error response ("rate limit exceeded, key quota"), and printing it turns mystery into diagnosis. <strong>Respect 429:</strong> a rate-limit response with a <code>Retry-After</code> header is the server telling you exactly when to come back; sleeping that long (with a sane fallback) is the difference between a client and a nuisance &mdash; <a href="/tech/http-status-codes-explained/">the status-code field guide</a> covers what each code means. <strong>Back off on 5xx:</strong> a server that just errored needs seconds, not an immediate retry; <code>2 ** attempt</code> is exponential backoff in one expression. <strong>Re-raise the rest:</strong> a 403 or 404 will not fix itself &mdash; crash loudly with the detail instead of retrying into a wall (<a href="/tech/call-api-python/">the base calling pattern</a> is in the previous piece).</p>
<h2>Timeouts are errors too</h2>
<p>The <code>timeout=10</code> from the calling pattern raises when a server stalls &mdash; in current Python, a <code>TimeoutError</code> (which, like HTTPError, sits under URLError's family tree in older versions; catching <code>URLError</code> plus <code>TimeoutError</code> covers both across versions). Treat it like a network failure: one retry with backoff is reasonable for a flaky cell link; a loop is not.</p>
<h2>The trap after the status code</h2>
<p>One last habit separates professionals: some APIs return <strong>200 OK with an error in the body</strong> (<code>{"error": "..."}</code>). The transport succeeded; the request didn't. After parsing, check for the API's own error key before celebrating &mdash; the status code says the pipe works, the payload says whether the answer is real. Log both whenever something puzzles you; the combination of status, body and attempt number is what you'll want in the bug report.</p>""",
[("Python docs \u2014 urllib.error (HTTPError, URLError)", "https://docs.python.org/3/library/urllib.error.html"),
 ("IETF RFC 9110 \u2014 HTTP semantics, incl. Retry-After", "https://datatracker.ietf.org/doc/html/rfc9110")],
[("call-api-python", "Calling an API with Python"),
 ("http-status-codes-explained", "HTTP status codes, explained")]),

("store-api-data-python", "coding", "guide",
"How to store API data in Python: SQLite in a few honest lines",
"Skip the CSV files: the standard library's sqlite3 gives your API data indexes, queries and safe writes — with parameterised queries from line one.",
"""<p>The default fate of API data in a script is a CSV that grows until it stops being useful. Python's standard library carries a better answer: <code>sqlite3</code>, a real database in a single file &mdash; queryable, indexed, safe under interruptions, zero setup. For anything a personal project will collect more than once, SQLite is the honest default.</p>
<h2>The working pattern</h2>
<pre><code>import sqlite3

conn = sqlite3.connect("inventory.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS items ("
    " id INTEGER PRIMARY KEY,"
    " name TEXT NOT NULL,"
    " price REAL,"
    " updated_at TEXT)"
)
sample = [
    ("desk lamp", 19.99, "2026-09-10"),
    ("usb-c cable", 8.5, "2026-09-10"),
]
conn.executemany(
    "INSERT OR REPLACE INTO items (name, price, updated_at) VALUES (?, ?, ?)",
    sample,
)
conn.commit()

for row in conn.execute(
    "SELECT name, price FROM items WHERE price &gt; ? ORDER BY price", (9.0,)
):
    print(row)

conn.close()</code></pre>
<p>Six details carry the whole skill. <strong><code>CREATE TABLE IF NOT EXISTS</code></strong> makes the script re-runnable &mdash; the first run creates, every later run reuses. <strong><code>INSERT OR REPLACE</code></strong> is the simplest upsert: re-fetching the same item updates instead of duplicating (as long as a unique key &mdash; here <code>name</code> could be one via a <code>UNIQUE</code> constraint &mdash; defines "the same"). <strong>Question-mark placeholders, always:</strong> values go in as parameters (<code>?, (9.0,)</code>), never formatted into the SQL string &mdash; string-formatting SQL is how injection bugs and quote-crashes are born, and the parameterised form is both safe and faster. <strong><code>executemany</code></strong> for batches: one round-trip for a hundred rows. <strong><code>commit()</code></strong> makes writes real; without it, closing the connection discards them. And <strong>dates as ISO-8601 text</strong> (<code>2026-09-10</code>) sort correctly as strings &mdash; which is the same convention <a href="/tech/unix-time-explained/">Unix timestamps</a> exist to simplify on the numerical side.</p>
<h2>What you get for the ceremony</h2>
<p>Once the data is in SQLite, the queries that were reasons to open the file become one-liners: latest price per item (<code>ORDER BY updated_at DESC</code>), weekly totals (<code>SUM</code> with a <code>WHERE</code> on the date), deduplication (<code>SELECT DISTINCT</code>). A CSV gives you none of that without rewriting the program each time. SQLite also writes atomically &mdash; a laptop dying mid-<code>commit()</code> leaves the file valid, which no hand-rolled file format promises.</p>
<h2>When to graduate</h2>
<p>The honest ceilings: SQLite is one file on one machine &mdash; perfect for a personal data pipeline, wrong for a multi-server application (that's PostgreSQL's job, and the SQL you wrote transfers almost unchanged), and wrong for data volumes where the file outgrows your disk or backup habits. For everything between "a list" and "a datacentre", it is the sweet spot &mdash; including as the storage layer under <a href="/tech/paper-trading-bot-lessons/">the paper-trading bot</a>, which uses it for exactly these reasons.</p>""",
[("Python docs \u2014 sqlite3", "https://docs.python.org/3/library/sqlite3.html"),
 ("SQLite \u2014 the official documentation", "https://www.sqlite.org/docs.html")],
[("parse-json-python", "Parsing JSON in Python"),
 ("paper-trading-bot-lessons", "The paper-trading bot, first-hand")]),

("schedule-python-scripts", "coding", "guide",
"How to schedule Python scripts (cron, and the honest case against sleep loops)",
"cron for real schedules, the environment gotchas that break scheduled scripts, and why your script's own while-loop is usually the wrong tool.",
"""<p>Sooner or later every useful script earns a schedule: the report that should run at 6:30, the poller that should check every fifteen minutes. The reliable answers live outside Python &mdash; in the operating system's scheduler &mdash; and the unreliable answer is the one most people write first. Start with the right one.</p>
<h2>cron: the workhorse (Linux and macOS)</h2>
<p>Open your user's crontab with <code>crontab -e</code> and add a line: five time fields, then the command.</p>
<pre><code># every day at 06:30
30 6 * * * /usr/bin/python3 /home/you/jobs/report.py &gt;&gt; /home/you/jobs/report.log 2&gt;&amp;1
# every 15 minutes
*/15 * * * * /usr/bin/python3 /home/you/jobs/poll.py</code></pre>
<p>The fields are minute, hour, day-of-month, month, day-of-week; <code>*</code> means "every", <code>*/15</code> means "every fifteenth". Three gotchas break most first attempts, so embed the fixes: <strong>use the absolute Python path</strong> (<code>which python3</code> tells you yours) because cron's <code>PATH</code> is not your shell's; <strong>use absolute script paths</strong> because cron runs from a different working directory than your terminal; and <strong>redirect output</strong> (<code>&gt;&gt; log 2&gt;&amp;1</code>) because a scheduled script that fails silently is invisible &mdash; the log line turns every failure into evidence. One subtlety worth knowing before it costs an evening: <code>%</code> is special in crontab commands (it starts a stdin block), so any command that needs a literal percent sign must escape it as <code>\\%</code>. On Windows, the Task Scheduler is the equivalent &mdash; point a task at <code>python.exe</code> with the script as its argument, on your trigger schedule.</p>
<h2>The sleep-loop trap</h2>
<p>The instinctive alternative &mdash; a <code>while True</code> loop with <code>time.sleep(900)</code> &mdash; has three failure modes that only show up in week three: the script drifts (sleep time <em>plus</em> work time per cycle), a crash takes the schedule down with it (nothing restarts the process), and a deploy silently orphans the old copy. The OS scheduler solves all three: it starts fresh, logs, and survives reboots. Reserve in-process repetition for genuinely in-process jobs &mdash; and if you need one, the standard library's <code>sched</code> module shows the correct pattern (a scheduler queue, not a sleep guess):</p>
<pre><code>import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def job(n):
    print("job", n, "ran at", time.strftime("%H:%M:%S"))
    if n &lt; 3:
        scheduler.enter(2, priority=1, action=job, argument=(n + 1,))

scheduler.enter(1, priority=1, action=job, argument=(1,))
scheduler.run()
print("all runs complete")</code></pre>
<p>Drop the guard on <code>n</code> and the job reschedules itself forever. For heavier needs &mdash; persistent jobs, missed-run handling, distributed workers &mdash; dedicated schedulers exist (APScheduler in-process, Celery for task queues); adopt them when a cron line genuinely stops being enough, not before. And whatever runs on a schedule needs what every unattended script needs: the error handling of <a href="/tech/handle-api-errors-python/">a proper API ladder</a> and a storage layer that survives crashes &mdash; <a href="/tech/store-api-data-python/">SQLite over CSV</a>, every time.</p>""",
[("Python docs \u2014 sched (the event scheduler)", "https://docs.python.org/3/library/sched.html"),
 ("Python docs \u2014 time.time and time.sleep", "https://docs.python.org/3/library/time.html")],
[("handle-api-errors-python", "Handling API errors"),
 ("store-api-data-python", "Storing API data in SQLite")]),

("deploy-python-app", "coding", "firsthand",
"How to deploy a Python app (the first-hand Render version)",
"A minimal Flask app, the three files that matter, secrets as environment variables, and the deploy pattern this very site uses in production — written by the person who runs it.",
"""<p>This site runs on Render, deployed by pushing a repository &mdash; and the same push-to-deploy pattern carries a Python app with almost no ceremony. This is the first-hand version: the three files that matter, the mistakes that cost time, and the config that works. (The static-site sibling of this story &mdash; how this very publication deploys &mdash; is in <a href="/tech/render-static-deploy/">the Render static deploy walkthrough</a>.)</p>
<h2>The smallest honest app</h2>
<p>A Python web app needs a framework entry point. Flask is the conventional first one &mdash; small, readable, installable in one line (<code>pip install flask</code>):</p>
<pre><code>from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "ok", "service": "bryme-demo"}</code></pre>
<p>Run it locally with <code>flask --app app run</code> and visit the printed address &mdash; you should see the JSON. That round-trip is the whole loop you are automating: code, run, check.</p>
<h2>The three files that matter</h2>
<p><strong>One:</strong> <code>requirements.txt</code> &mdash; every import your app needs, pinned to the versions you actually tested with (<code>flask==3.1.3</code> at the time of writing; pin what <em>you</em> tested, because unpinned dependencies are how a working app breaks months later without a single edit). <strong>Two:</strong> the code itself, in a repo. <strong>Three:</strong> the two commands your host will run &mdash; on Render, a build command (<code>pip install -r requirements.txt</code>) and a start command. The production-grade start command uses a real WSGI server rather than Flask's development server:</p>
<pre><code>gunicorn -w 2 -b 0.0.0.0:$PORT app:app</code></pre>
<p><code>app:app</code> means "the variable <code>app</code> inside <code>app.py</code>"; <code>-b 0.0.0.0:$PORT</code> binds to every interface on the port the platform assigns &mdash; binding to <code>127.0.0.1</code> is the classic reason a deploy "succeeds" and serves nothing. Flask's own server prints a warning for a reason: it is single-purpose and unsuitable for production traffic; gunicorn (install with <code>pip install gunicorn</code>) is the boring, correct answer.</p>
<h2>Secrets are environment variables</h2>
<p>API keys never go in code or in the repo &mdash; the host's environment-variable settings inject them at runtime, and your code reads them as the first thing it does:</p>
<pre><code>import os

API_KEY = os.environ["API_KEY"]</code></pre>
<p>Using <code>os.environ["KEY"]</code> (rather than <code>.get</code>) is deliberate: the app should refuse to start without its secrets rather than run broken and discover it at 3am. The full discipline &mdash; scoping, rotation, never committing tokens &mdash; is in <a href="/tech/github-token-hygiene/">the token-hygiene guide</a>.</p>
<h2>The first-hand warnings</h2>
<p>Trust the deploy log, not the homepage &mdash; a host can serve the last good build while today's build quietly failed, which is the number-one "why is my change not live" mystery (<a href="/tech/render-deployment-failures-what-they-taught-me/">our deployment-failure field notes</a>). Expect free-tier web services to sleep between requests and wake slowly on the first hit (static hosting doesn't sleep; app services do &mdash; different products, despite the same dashboard). And after the first deploy, verify with curl, not vibes: hit the URL, check the status code, confirm the JSON &mdash; the same rule as every piece on this desk.</p>""",
[("Flask \u2014 official documentation", "https://flask.palletsprojects.com/"),
 ("gunicorn \u2014 the WSGI server used in the start command", "https://gunicorn.org/"),
 ("Render \u2014 deployment documentation", "https://render.com/docs")],
[("render-static-deploy", "Render static deploys, first-hand"),
 ("github-token-hygiene", "Token hygiene"),
 ("render-deployment-failures-what-they-taught-me", "Deployment failures, documented")]),
]
