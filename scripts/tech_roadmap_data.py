# BRYME Tech — roadmap batch T1: Coding & Dev (priority cluster) + Passwords & Accounts remainder.
# The roadmap's [VERIFY] tags resolved 2026-09-10: Verizon 2025 DBIR (stolen creds 22% of
# breaches / 88% of basic web-app attacks); Cybernews 19bn-password analysis (94% reused);
# NIST SP 800-63B FAQ (KBA no longer acceptable; random answers in a manager recommended).

TECH_ROADMAP_T1 = [
("learning-python-free-resources", "coding", "guide",
"Free resources to learn Python that are actually good",
"A self-taught programmer's shortlist — ranked by what survives contact with a real learner, written by someone who learned on a phone.",
"""<p>Most "best resources to learn Python" lists are affiliate farms that have never run the code they recommend. This one is written from the other direction: I taught myself Python without a laptop, on a phone, and every resource below earned its place by surviving actual use. None of them paid for inclusion, none of them are affiliate links, and all of them are free.</p>
<h2>The spine: the official tutorial, eventually</h2>
<p><a href="https://docs.python.org/3/tutorial/">The official Python tutorial</a> is better than its reputation and drier than its competition — which is exactly why it belongs on the list twice: once as a reference you grow into, and once as the graduation exercise. Don't start there if dry documentation has killed your motivation before; do start there the day a tutorial leaves you asking "but how does it <em>actually</em> work", because it always answers that question. Reading it after a month of practice is a different experience from reading it on day one.</p>
<h2>The start: Automate the Boring Stuff</h2>
<p>Al Sweigart's <a href="https://automatetheboringstuff.com/">Automate the Boring Stuff with Python</a> is free to read in full online, and it wins the motivation war because every chapter does something real — renaming files, scraping a page, filling a form. For learners who quit tutorials because nothing <em>happens</em>, this is the antidote. It teaches enough to automate your own boredom, which is the honest core of why most people should learn Python at all.</p>
<h2>The depth: CS50P</h2>
<p>Harvard's <a href="https://cs50.harvard.edu/python/">CS50's Introduction to Programming with Python</a> is free, rigorous, and the best bridge from "I can follow a tutorial" to "I can solve a problem nobody has pre-solved for me". The problem sets are genuinely hard in the right way — hard like exercise, not hard like hazing. If you only keep one item from this list, keep this one: it's the resource that turns tutorial-knowledge into programmer-judgment.</p>
<h2>The practice: Exercism and freeCodeCamp</h2>
<p><a href="https://exercism.org/">Exercism</a> gives you small problems, a mentor who reviews your code for free, and the experience of being told your working code could be better — which is the lesson tutorials never give you. freeCodeCamp's Python curriculum is broader, video-light, and good for the stretch where you want volume. Use one as your main practice floor and the other as a side dish; both are free all the way down.</p>
<h2>The phone clause: Termux changes the calculus</h2>
<p>If your only computer is a phone, the resources above all still work — a browser renders every one of them, and <a href="/tech/learning-to-code-on-a-phone-termux/">Termux gives you a real Python interpreter and a real Linux toolchain on Android</a>, which is how this list was originally written. The phone is a worse keyboard and a perfectly good brain-extension; don't let anyone tell you the laptop is the prerequisite. When you're ready for the next layer — projects, version control, the errors that teach — <a href="/tech/git-and-github-for-beginners/">Git and GitHub come next</a>, and <a href="/tech/how-to-read-an-error-message/">learning to read error messages</a> is the skill that quietly does most of the teaching.</p>
<h2>What to skip</h2>
<p>Paid bootcamps before free fundamentals (you don't know what you don't know yet — pay when you can evaluate what you're buying); "Python in 30 days" content farms that measure progress in days; and any resource whose first lesson is installing an IDE you don't understand. The order that works: something real (<i>Automate</i>), something hard (<i>CS50P</i>), something referential (the official docs), forever: small problems (Exercism). That's the whole stack, and it costs nothing but the months it takes.</p>
<p><em>Reviewed September 2026 · all listed resources free at time of writing; availability checked but course contents evolve — verify the syllabus still suits you before committing months.</em></p>""",
[("Automate the Boring Stuff — free online", "https://automatetheboringstuff.com/"),
 ("CS50's Introduction to Programming with Python", "https://cs50.harvard.edu/python/"),
 ("Exercism", "https://exercism.org/")],
[("learning-to-code-on-a-phone-termux", "Termux: coding on a phone"),
 ("git-and-github-for-beginners", "Git and GitHub, concept-first"),
 ("how-to-read-an-error-message", "Reading error messages")]),

("github-beginner-mistakes", "coding", "guide",
"GitHub for beginners: the mistakes that waste the most time",
"Not the scary mistakes — the slow ones. The habits that quietly cost beginners their first year, collected from experience.",
"""<p>Git's learning curve is mostly made of self-inflicted detours. The commands are learnable in an afternoon; the <em>habits</em> — the ones that either compound into fluency or compound into fear — take a year. These are the time-wasting mistakes, roughly in order of how much time each one wastes. The conceptual groundwork lives in <a href="/tech/git-and-github-for-beginners/">the concept-first Git guide</a>; this page is the field notes.</p>
<h2>Mistake one: waiting for the perfect first commit</h2>
<p>Beginners treat their first commit like a diploma — the project must be ready, the code must be clean, the README must exist. So nothing gets committed for weeks, and the safety net Git exists to provide never gets built. Commit broken, commit ugly, commit often: the entire value of version control is <em>save points</em>, and a save point only exists if you save. The habit that works: commit at every moment you'd be annoyed to lose your work.</p>
<h2>Mistake two: committing secrets</h2>
<p>An API key or token pasted into code and committed is compromised the moment it's pushed — automated scanners find credentials in public repos within minutes, not hypothetically; it's how this desk's own <a href="/tech/github-token-hygiene/">token-hygiene guide</a> earned its scars. The recovery is genuinely annoying (revoke, rotate, purge history), and prevention is trivially cheap: secrets live in environment variables and ignored files, from day one. Related beginner trap: <code>node_modules</code>, virtual environments and other rebuildable folders committed wholesale — a missing <code>.gitignore</code> at project start is the gift that keeps costing.</p>
<h2>Mistake three: doing everything on main</h2>
<p>Every experiment happens directly on <code>main</code>, until one breaks the working version and there's no way back except memory. Branches are Git's answer to "what if" — and beginners avoid them because merging looks scarier than not branching. The fear is backwards: a small branch merged often teaches you merging in five-minute lessons; a year of main-only development teaches it in an afternoon-long crisis.</p>
<h2>Mistake four: reading commands as incantations</h2>
<p>Copy-pasting commands from a forum without reading them is how beginners end up in the situations the commands were warning about — <code>force push</code> and <code>reset --hard</code> are the classic two. The wasted time isn't the damage (everything in Git is usually recoverable); it's the <em>confidence</em> damage — one scary incantation incident and weeks of paranoid committing follow. Read every command, one flag at a time; <a href="/tech/how-to-read-an-error-message/">the error-message habit</a> applies to Git output too, and Git's messages are unusually helpful once you let them talk.</p>
<h2>Mistake five: fighting merge conflicts with fear</h2>
<p>A merge conflict is not an error — it's Git <em>asking you a question</em>: two versions of a line exist; which should survive? Beginners read the wall of <<<<<<< markers as failure, close the editor, and delete things. The fix is seeing the markers as what they are: a diff you're invited to resolve, with the two versions labelled. Ten minutes of deliberate practice on a self-made conflict (edit the same line on two branches, merge) is a permanent vaccine.</p>
<h2>Mistake six: the README that never comes</h2>
<p>"I'll write it later" — and six months later the project can't be reinstalled by its own author. The five-minute README at project start (what this is, how to run it) pays for itself the first time you return after a break, which is also exactly how future collaborators and employers will meet the work. Good enough now beats perfect never — the same lesson as mistake one, wearing documentation.</p>
<p><em>Sources: GitHub's own beginner documentation and Pro Git; the scars are first-hand. Reviewed September 2026.</em></p>""",
[("Pro Git — the free book", "https://git-scm.com/book/en/v2"),
 ("GitHub — Get started docs", "https://docs.github.com/en/get-started")],
[("git-and-github-for-beginners", "Git and GitHub, concept-first"),
 ("github-token-hygiene", "Token hygiene, first-hand"),
 ("learning-python-free-resources", "Free Python resources that are good")]),

("reusing-passwords-risk", "safety", "guide",
"Reusing the same password everywhere is the easiest way to lose everything",
"The mechanism is called credential stuffing, the numbers are in the industry's own breach reports, and the fix takes one evening.",
"""<p>The reason password reuse is dangerous isn't that hackers guess your passwords one site at a time — it's that they never guess at all. When any one service is breached and its password file leaks, that email-and-password pair gets replayed automatically against every other major service on Earth. It's called <strong>credential stuffing</strong>, it's industrial-scale, and it works precisely because reuse works.</p>
<h2>What the breach data actually says</h2>
<p>Verizon's Data Breach Investigations Report — the industry's annual breach census — found <strong>stolen credentials were the initial access vector in 22% of breaches</strong> in its 2025 edition, and that <strong>88% of basic web-application attacks involved stolen credentials</strong>. The reuse that feeds those numbers is measurable too: Cybernews researchers analysed <strong>over 19 billion leaked passwords and found 94% were reused or duplicated</strong> across accounts. Read those together and the pattern is stark: your password is only as strong as the least-secure forum you ever used it on — and attackers know people reuse, because they're watching the stuffing succeed.</p>
<h2>Why "but my accounts are boring" doesn't protect you</h2>
<p>The stuffed account isn't necessarily your email or your bank on day one. The classic escalation starts somewhere forgettable — a forum, a shopping site — because the goal is <em>information</em>: your password patterns, the email you reuse, the security answers you recycle. From there, attackers assemble the picture that opens the valuable accounts. And password resets themselves become the attack: whoever controls your email inbox controls every "forgot password" link sent to it, which is why the email account is the crown jewel and the one account that must have a unique password and <a href="/tech/two-factor-authentication-setup/">a second factor</a> above all others.</p>
<h2>The fix, one evening, in order</h2>
<p><strong>First the crown jewels:</strong> email, bank, phone account, primary social — unique passwords today, 2FA tonight. <strong>Then a password manager:</strong> it remembers the rest so you don't have to — <a href="/tech/password-manager-or-browser/">browser-built-in or dedicated, honestly compared</a>, with <a href="/tech/bitwarden-free-password-manager/">Bitwarden's free tier as the default recommendation</a>. Let it generate unmemorable random strings per site; memorising is the machine's job now. <strong>Then the backfill:</strong> when you log into any old site over the coming weeks, that's the trigger to give it a fresh unique password. You don't have to fix all of them in one sitting — you have to stop the reuse from here forward, and let the backfill happen naturally.</p>
<h2>The upgrade past passwords</h2>
<p>Passkeys — the newer standard that replaces the password with a device-bound credential — are quietly rolling out across major services and are immune to stuffing by design. Where a service offers them, they're worth five minutes to set up. Until then: unique, generated, managed, with 2FA on anything that matters. That combination doesn't make you unhackable; it removes you from the <em>easy</em> pile — and the easy pile is where the stuffing machines eat.</p>
<p><em>Sources: Verizon Data Breach Investigations Report 2025 (22% initial access via stolen credentials; 88% of basic web-app attacks); Cybernews research team analysis of 19bn leaked passwords (94% reused/duplicated). Reviewed September 2026.</em></p>""",
[("Verizon DBIR 2025", "https://www.verizon.com/business/resources/reports/dbir/"),
 ("NIST SP 800-63B — Digital Identity Guidelines", "https://pages.nist.gov/800-63-3/sp800-63b.html")],
[("password-manager-or-browser", "Password manager or browser?"),
 ("two-factor-authentication-setup", "Two-factor authentication, done right"),
 ("bitwarden-free-password-manager", "Bitwarden, honestly reviewed")]),

("security-questions-are-insecure", "safety", "guide",
"The security-question trap: why your mother's maiden name protects nobody",
"America's digital-identity standards body says security questions shouldn't be used for authentication at all — and the reasons are older than the internet.",
"""<p>Security questions survive everywhere — the bank, the email provider, the government portal — which makes them look like protection. They're closer to a spare key buried under a doormat you announced the location of. The US National Institute of Standards and Technology (NIST), whose digital identity guidelines are the reference point for authentication worldwide, now states it plainly: knowledge-based authentication — security questions — is <strong>"no longer recognized as an acceptable authenticator"</strong>, and verifiers <strong>shall not</strong> use it. The standards body that shapes how banks and governments authenticate people has formally retired the mother's maiden name.</p>
<h2>Why the answers were never secret</h2>
<p>Three structural problems, all older than the practice itself. <strong>Researchability:</strong> maiden names, first schools, first cars, the street you grew up on — a surprising amount is one social-media scroll away, and data brokers assemble the rest. <strong>Leakability:</strong> when any site using the same questions is breached, the answers leak with it — and people recycle answers as readily as passwords. <strong>Smallness:</strong> even private answers have tiny possibility spaces — how many first-pet names are there, really? A question with twelve plausible answers isn't a lock; it's a twelve-sided die an attacker gets to roll forever.</p>
<h2>What NIST says to do instead</h2>
<p>The standard's guidance for the sites that still ask: <strong>generate random answers and store them in a password manager</strong> — not the actual answer, a random string. NIST's own FAQ suggests exactly this. Your mother's maiden name becomes <code>7-trXq!2mpL-vase-2</code>, the manager remembers it, and the "security question" quietly becomes a second random password — which is the only version of it that ever protected anyone. The <a href="/tech/password-manager-or-browser/">password-manager guide</a> covers the setup, and <a href="/tech/reusing-passwords-risk/">the reuse guide explains why recycled answers leak sideways</a> just like recycled passwords.</p>
<h2>If you're locked out instead: the recovery honest path</h2>
<p>Sometimes the trap has already sprung — the account demands the question, the answer's long gone. That's an account-recovery problem, not a security one: <a href="/tech/how-to-reset-forgotten-passwords/">the forgotten-password guide walks the honest recovery routes</a>, and the lesson afterwards is the random-answers-in-a-manager setup, so the next lockout never depends on remembering which street you lived on in 2009.</p>
<h2>The wider pattern worth naming</h2>
<p>Security questions are the clearest example of a general rule: <em>authentication that depends on facts about you was never authentication — it was trivia.</em> The modern replacements — generated passwords in a manager, app-based second factors, and passkeys that bind sign-in to a device — all share one property: they don't ask what you know that others might also know. They verify something you <em>have</em> or something unique you <em>hold</em>. Where a service offers those, prefer them; where it still asks for your first school, feed it a random string and sleep better.</p>
<p><em>Sources: NIST SP 800-63 Digital Identity Guidelines FAQ (KBA no longer recognized; random answers via password manager recommended); NIST SP 800-63B. Reviewed September 2026.</em></p>""",
[("NIST SP 800-63 FAQ — knowledge-based authentication", "https://pages.nist.gov/800-63-FAQ/"),
 ("NIST SP 800-63B", "https://pages.nist.gov/800-63-3/sp800-63b.html")],
[("reusing-passwords-risk", "The reuse mechanism"),
 ("password-manager-or-browser", "Password manager or browser?"),
 ("how-to-reset-forgotten-passwords", "Forgotten-password recovery, honestly")]),
]
