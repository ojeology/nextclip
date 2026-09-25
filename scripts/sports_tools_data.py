# BRYME Sport — desk tools (2026-09-25).
# Same architecture as the tech/home desk tools: deterministic maths in an
# external JS asset (site CSP blocks inline scripts), a noscript framework in
# the page, the working shown in full, on-device only — no storage, no network,
# no betting content. The points race calculator is arithmetic, not prediction:
# it never invents a probability, and the page says so.

POINTS_RACE_SLUG = "points-race-calculator"

# Toolbox rows for the desk hub machine: (slug, name, dek, guide-slug)
SPO_TOOLS = [
    (POINTS_RACE_SLUG, "Points race calculator",
     "Points, games played and recent form in \u2014 projected finish, the minimum wins-and-draws route to any target, "
     "and every line of the working shown. Arithmetic, never a prediction.",
     "premier-league-prize-money-explained"),
]

POINTS_RACE_BODY = """
<main id="main"><div class="wrap">
<nav class="crumb"><a href="/sports/">Sport</a> / Points race calculator</nav>
<section class="cover"><p class="kicker">Tool &middot; desk</p>
<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">Points race calculator</h1>
<p class="byline">BRYME Sport desk &middot; published 2026-09-25 &middot; runs entirely in your browser &mdash; nothing is stored or sent &middot; arithmetic, not betting advice</p></section>
<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> put in the table numbers you can see &mdash; points, games played, recent form &mdash; and get the projected finish, the minimum wins-and-draws route to your target, and every step of the maths.</p></div></section>
<section class="section"><div class="prose">
<p>Every &ldquo;will they make it?&rdquo; argument is really two arithmetic questions: what does current form project to over the games left, and what is the cheapest combination of results that reaches the target? This tool answers both, shows the working line by line, and stops there. It does not model fixtures, injuries or luck &mdash; anything that claims to know those is selling you something.</p>
<style>
.pr-card{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:20px 22px;max-width:760px}
.pr-flds{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.pr-flds label{display:flex;flex-direction:column;gap:6px;font-weight:600;font-size:14px}
.pr-flds input,.pr-flds select{padding:10px 12px;border:1px solid var(--line-strong);border-radius:8px;font-size:16px;background:var(--paper);color:var(--ink)}
.pr-out{margin-top:16px;border-left:3px solid var(--accent);background:var(--paper);padding:12px 16px;border-radius:8px}
.pr-out h3{margin:0 0 8px;font-family:var(--serif)}
.pr-out ul{margin:0;padding-left:20px}
.pr-out li{margin:6px 0;font-size:14.5px}
.pr-warn{color:#a33;font-weight:700}
.pr-privacy{font-size:12.5px;color:var(--muted);margin-top:14px}
</style>
<div id="points-race-calculator"></div>
<noscript>
<p><b>The tool needs JavaScript. Here is the honest framework, statically:</b></p>
<ul>
<li><b>Projection:</b> remaining games = season length &minus; games played. Projected finish = current points + (remaining &times; points per game). Use last-five form for the run-in, or the season average if the squad has changed.</li>
<li><b>Minimum route to a target:</b> gap = target &minus; current points. Cheapest combination = as many wins as the gap allows (3 points each), leftover points as draws. If wins + draws exceeds the games left, the target is gone &mdash; the arithmetic says so, not the vibes.</li>
<li><b>Required rate:</b> gap &divide; games left = the points-per-game the run-in must average.</li>
<li><b>What the numbers don&rsquo;t know:</b> fixture difficulty, injuries, suspensions, European distraction. Two teams on identical projections can have very different run-ins &mdash; that is why this desk grades the table after matchdays, not before them.</li>
</ul>
</noscript>
<script src="/assets/points-race-tool.js" defer></script>

<h2 id="how">How the maths works</h2>
<p>Projection is one line: <b>points + (games left &times; points per game)</b>. The minimum route is a small division: <b>wins = gap &divide; 3 (rounded down)</b>, and the leftover one or two points become draws. Required rate is <b>gap &divide; games left</b>. That is the entire model &mdash; if a &ldquo;predictor&rdquo; hides its working, it is hiding the fact that there is no model.</p>
<p>Two folklore numbers deserve honesty: the <b>40-point safety line</b> is a habit, not a rule &mdash; recent seasons have seen safety secured well below it; and a <b>title-winning total</b> moves with how strong the top of the table is. Use the custom target and read the required rate, not the headline number.</p>

<h2 id="why">Why every place in the table is worth points</h2>
<p>The run-in maths changes meaning at both ends of the table because the money does: final position decides prize-money distribution, and the gaps between places are millions apart. The desk&rsquo;s explainer on <a href="/premier-league-prize-money-explained/">how prize money actually works</a> shows what a single place is worth &mdash; and <a href="/financial-fair-play-explained/">Financial Fair Play, explained</a> shows why those numbers govern what clubs can spend next.</p>

<p class="byline">This tool never places, suggests or prices a bet. It does arithmetic on numbers you enter, and it shows every line so you can check it.</p>
</div></section>
<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from the shelf.</h2></div>
<ul class="list">
<li><a href="/premier-league-prize-money-explained/"><span><b>Prize money, explained</b><small>What every position in the table is actually worth</small></span><span class="meta">Explainer</span></a></li>
<li><a href="/financial-fair-play-explained/"><span><b>Financial Fair Play and PSR, explained</b><small>The spending rules behind the points deductions</small></span><span class="meta">Explainer</span></a></li>
<li><a href="/how-the-transfer-window-works/"><span><b>How the transfer window really works</b><small>Registrations, deadlines and loans, after the noise</small></span><span class="meta">Explainer</span></a></li>
</ul>
<div class="actions"><a class="btn secondary" href="/sports/">All of BRYME Sport</a></div></section>
</div></main>"""
