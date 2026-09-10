# -*- coding: utf-8 -*-
"""BRYME Sport batch 3 — the analysis shelf (Sept 2026). No fixtures, no data rights, no betting.

Receipts:
- xG history verified 2026-09-10: first implemented by Sam Green at Opta, April 2012
  (adapting American-sport analytics); mainstreamed by BBC Match of the Day from the
  2017-18 season; providers (Opta, StatsBomb, others) run different models, hence
  differing values per shot. Sources cited in-piece; no win-percentage stats used.
- Back-pass law verified 2026-09-10: introduced 1992 after the 1990 World Cup's
  time-wasting problem; keeper may not handle a team-mate's deliberate foot pass or a
  direct team-mate throw-in — indirect free kick; headed/chested/kneed returns fine;
  deliberate circumvention tricks banned. Sporting Chronicle (history) + Footymetrics
  (Law 12 mechanics) cited; the 1990 goal-per-match figure deliberately NOT pinned.
- pressing / shirt-numbers / possession / offside-trap are pure concept pieces — no
  external stats claimed, sources[] left empty on purpose (house precedent).
"""

SPORT_ANALYSIS = [

("xg-explained", "Expected goals: what the number actually tells you",
"Chance quality as a probability: where xG came from, what the model eats, why every site shows a different number, and the honest limits of football's most quoted stat.",
"""<p>Every broadcast graphic now carries it, every pundit leans on it, and most arguments about it start from a misunderstanding. Expected goals (xG) is not a prediction and not a rating of teams. It is one number per shot: <strong>the probability that an average shot from that situation becomes a goal</strong>, between 0 and 1. A chance rated 0.3 should score roughly three times in ten. Over a season, those probabilities tell you more about a team than the scoreboard does — which is exactly why it also gets misused every single week.</p>
<h2>Where it came from</h2>
<p>The modern model was first implemented in April 2012 by Sam Green, then an analyst at the sports data company Opta, adapting ideas that American sports analytics had been using for years. It stayed a niche tool until BBC's <em>Match of the Day</em> began building it into its coverage from the 2017-18 season, and it has been part of football's everyday language since. That history matters, because it explains the metric's shape: it was built to compare chance quality, not to settle bar arguments about who deserved a single result.</p>
<h2>What the model actually eats</h2>
<p>A shot's xG is estimated from the things that make shots miss: distance and angle to goal, the body part used, how the chance was built (a through ball versus a scramble), the position of defenders and keeper, and pattern of play. Two honest consequences follow. First, the number is a model's opinion, built from historical shots of the same type. Second, <strong>different providers run different models</strong> — Opta, StatsBomb and the rest weigh the ingredients differently, which is why the same goal gets 0.34 on one site and 0.41 on another. Both are doing their job; the differences are usually smaller than the arguments about them.</p>
<h2>What it is good for</h2>
<p>Over months, not minutes. Chance creation and chance suppression are among the most stable signals of how good a team actually is — results wobble around them. xG separates a striker in a finishing hot streak from one getting genuinely better chances, shows when a defence is conceding dangerous opportunities rather than surviving on luck, and gives recruitment departments a shared language for &ldquo;does this player get into good positions?&rdquo;</p>
<h2>The honest limits</h2>
<p><strong>Small samples lie.</strong> A single match is noise; a team that &ldquo;won the xG&rdquo; has not won an argument, it has taken one shot-quality snapshot. <strong>Game state bends everything:</strong> a leading team stops shooting and a chasing one piles forward, so the numbers describe the situation as much as the quality. <strong>The goalkeeper is invisible to it</strong> — xG rates the chance, and the save is the other half of the story (a keeper who concedes above his chances' rating is facing, or failing, his own column). And a 0.95 chance that stays out is not a scandal: probability is not a promise, which is the sentence most xG arguments forget first.</p>
<p><em>The fair summary: xG measures chances, not football. Used over a season it is the most honest number in the game; used to pronounce on one Saturday it is astrology with decimal points. This desk uses it the first way — the same rule applied to every number we publish: know what it measures, then say so.</em></p>""",
[("Sport Performance Analysis — the xG model's origin (Sam Green, Opta, April 2012; Match of the Day adoption from 2017-18)", "https://www.sportperformanceanalysis.com/article/what-are-expected-goals-xg")],
[("pressing-explained", "Pressing, blocks and the line"),
 ("possession-explained", "Possession: what it tells you"),
 ("how-var-works", "How VAR actually works")]),

("pressing-explained", "Pressing, blocks and the line: how modern teams defend",
"Defending used to start 40 yards from goal. Now the first question is where the block sits — and the second is what sets the hunt off.",
"""<p>Ask an older fan to define defending and you will hear about heading, tackling and getting men behind the ball. Ask a modern coach and the answer is one word: <strong>space</strong>. Everything in contemporary defending — the press, the block, the line — is a decision about which space to occupy and which to concede. Once you see that, the tactical diagrams on television stop being abstract art.</p>
<h2>The block: where your team lives without the ball</h2>
<p>Every team picks a neighbourhood to defend in. The <strong>high block</strong> defends from the opposition's half: it suffocates build-up at source and wins the ball where a turnover hurts most — but it needs pace behind and legs everywhere. The <strong>mid block</strong> crouches around the halfway line, funnelling play wide and waiting for a bad pass. The <strong>low block</strong> packs the final third, accepting territory to deny the box — the classic shape of the underdog, and of any team protecting a lead. None of the three is superior. The choice is set by personnel (speed, stamina, aerial strength), by the opponent, and by the score. Teams that can hold two or three shapes and switch between them are the hardest to play against; teams married to one block are pattern-matched within weeks.</p>
<h2>The press: a hunt with rules</h2>
<p>Pressing is not running at the ball enthusiastically. It is a coordinated trap with <strong>triggers</strong>: the bad first touch, the pass played inside to a crowded area, the ball played back to a defender facing his own goal, the isolated full-back. When a trigger fires, three or four players converge on the ball carrier while teammates cut the escape routes — pressing is chess played at sprint speed, and the passing lanes matter more than the man. Good pressing teams hunt in packs by design; bad pressing teams chase in ones and get sliced apart.</p>
<h2>Gegenpressing and the counter-press</h2>
<p>The most influential defensive idea of the last fifteen years has a German name: <em>gegenpressing</em> — counter-pressing, the idea associated above all with J&uuml;rgen Klopp's teams. The insight: <strong>the moment you lose the ball is the perfect time to win it back</strong>, because the opponent is organised to attack, not to keep it. Win it high and their defence is facing the wrong way; fail, and drop into your block and reset. It is aggressive, exhausting, and honest about its trade — it bets legs against chances.</p>
<h2>The cost nobody hides</h2>
<p>Every yard a defence pushes up is a yard of grass behind it. The high press concedes the space that the fastest attackers want; the whole defensive line moves as one or not at all — which is why the high line and the offside trap are the press's Siamese twins, and why one mistimed stride is the most expensive mistake in football (<a href="/the-offside-trap/">the offside trap, explained</a>). And the reverse duel matters too: what a pressing team does, a build-up team exists to break — <a href="/playing-out-from-the-back/">playing out from the back is the move invented to beat the press</a>.</p>
<p><em>Watch one match with only this question — where does the defending team put its block, and what triggers its hunt? — and a season of tactical television punditry starts making sense at once.</em></p>""",
[],
[("playing-out-from-the-back", "Why teams play out from the back"),
 ("the-offside-trap", "The offside trap"),
 ("possession-explained", "Possession: what it tells you")]),

("what-shirt-numbers-mean", "What shirt numbers actually mean (and what they used to mean)",
"Once they were positions on a teamsheet; now they are identities. The story of 1 to 11, the jobs behind 6, 8 and 10, and why the false 9 is not wearing what it used to.",
"""<p>Shirt numbers look like identity — Ronaldo's 7, Messi's 10 — but they began as paperwork. For most of football's history, teams numbered their starting eleven from 1 to 11 in a fixed order that mapped straight onto positions, and if you knew the list you knew the team's shape before the first whistle.</p>
<h2>When the numbers were positions</h2>
<p>The old English layout said it all: 1 the goalkeeper; 2 and 3 the full-backs; 4, 5 and 6 the half-back line; 7 through 11 the forwards, with 9 the centre-forward and 10 and 11 the inside men beside him. Numbers described roles so precisely that a teamsheet was a formation diagram. Football then spent decades bending the map: formations evolved, the fixed order dissolved, and the numbers drifted into tradition — but the key numbers never lost their meaning, they just stopped being coordinates and became vocabulary.</p>
<h2>The numbers that became words</h2>
<p>When commentators say &ldquo;a classic 10&rdquo; or &ldquo;a proper 6&rdquo;, this is the vocabulary: <strong>the 6</strong> is the holding midfielder — the screen in front of the defence who collects the ball, sets the tempo and covers for everyone else's adventure. <strong>The 8</strong> is the connector, the box-to-box midfielder doing both halves of the game. <strong>The 10</strong> is the creator who lives between the opposition's lines, the position so associated with genius that &ldquo;the No. 10 role&rdquo; outgrew the number itself. <strong>The 9</strong> remains the centre-forward, the finisher, the man the crosses were always for. These roles are real jobs with real responsibilities; the number on the back is just the shorthand.</p>
<h2>The modern drift</h2>
<p>Once squad numbers became permanent personal brands, any pretence that numbers described positions ended — the teamsheet stopped being a diagram forever. Roles kept mutating anyway. The <strong>false 9</strong> is a centre-forward who keeps dropping into midfield, dragging the opposing defenders with him and leaving the lane they abandoned free for midfield runners; the idea's most famous practitioner made the position a laboratory experiment that won everything, and now it is simply part of the language. The <strong>inverted winger</strong> is a wide attacker stationed on his weaker-looking foot so he can cut inside and shoot — the modern default on both flanks, and the reason &ldquo;winger&rdquo; no longer implies crossing.</p>
<p><em>The rule of thumb this desk uses: ignore the number, watch the job. The teamsheet tells you who is playing; the first ten minutes tell you what the numbers are doing.</em></p>""",
[],
[("pressing-explained", "Pressing, blocks and the line"),
 ("possession-explained", "Possession: what it tells you"),
 ("the-offside-rule-explained", "The offside rule, explained")]),

("possession-explained", "Possession: what it tells you, and what it doesn't",
"Having the ball is a choice, not a scoreboard. Why 70% possession can mean control or cowardice — and what to watch instead of the stat.",
"""<p>Possession is the most quoted number in football and the least examined. It answers a simple question — who has the ball, how much of the time — and then people quietly add a second claim that does not follow: that the team with more of it is the better team. Sometimes. The honest version: <strong>possession is a plan, not a prize</strong>, and the plan it reveals matters more than the percentage.</p>
<h2>Two kinds of having the ball</h2>
<p><strong>Live possession</strong> moves a team up the pitch: the ball travels with purpose, defenders are dragged out of their block, and every pass threatens something. <strong>Sterile possession</strong> circulates side to side in front of a settled defence — safe, patient and going nowhere. Both can produce 68% on the graphic. The eye test separates them in ten minutes: watch whether the ball possession forces the defending team to move, or lets them stand still. A team can dominate the ball all afternoon and never once make the opposition's shape turn.</p>
<h2>The plan you are actually watching</h2>
<p>Possession share is mostly a statement of intent. A coach who wants the ball is buying control: fewer transitions, the game played far from his own goal, tired opponents chasing shadows. A coach who accepts 35% is buying space: the opponent must commit players forward, and every committed player is one less defender against the counter — the whole strategy is the grass the other team abandons. Neither is braver; both can be executed well or badly. What possession cannot tell you is which plan you are watching — the stat counts the ball, not the idea behind who has it.</p>
<h2>What to watch instead</h2>
<p><strong>Where the ball is won and lost</strong> — territory matters as much as ownership; a team that wins the ball 40 yards higher up the pitch needs fewer passes to score. <strong>Chance quality</strong> — the metric built for that job is expected goals, and this desk has <a href="/xg-explained/">explained what xG does and doesn't measure</a>; two minutes of chances tell you more than ninety of passing. <strong>What happens in transitions</strong> — the five seconds after the ball changes hands are where modern matches are decided, and no possession stat sees them at all.</p>
<p><em>The scoreboard is the only number that counts, and it counts ends, not means. Possession is one means among several — the teams that win trophies are the ones whose means match their players, whatever the graphic says at half-time.</em></p>""",
[],
[("xg-explained", "Expected goals, explained"),
 ("pressing-explained", "Pressing, blocks and the line"),
 ("what-shirt-numbers-mean", "What shirt numbers mean")]),

("playing-out-from-the-back", "Why teams play out from the back — and why it keeps going wrong",
"The riskiest habit in modern football started with a law change in 1992. Inside the short build-up: the idea, the danger, and why some squads simply should not try it.",
"""<p>Few things make a stadium hold its breath like a goalkeeper taking a touch with an attacker sprinting at him. Playing out from the back — building every attack with short passes from the keeper — is modern football's most confident habit and its most expensive failure mode. Both halves of that sentence trace back to one law change.</p>
<h2>The law that made keepers footballers</h2>
<p>Until 1992 a goalkeeper could pick the ball up from any teammate and launch it. Late in tight games, that meant a defender would calmly knock the ball back to his keeper, who would cradle it, eat thirty seconds, and punt — time-wasting so endemic that the game's lawmakers intervened. The 1992 amendment to Law 12: <strong>a goalkeeper may not handle the ball after a team-mate has deliberately kicked it to him</strong> (nor straight from a team-mate's throw-in); the punishment is an indirect free kick. Headed, chested or kneed returns stayed legal; deliberate trickery to dodge the rule was itself banned. The tactical earthquake followed within a generation: keepers had to learn to play, defenders learned to build under pressure, and the short pass back to the keeper became a loaded weapon instead of a fire escape.</p>
<h2>The idea, stated fairly</h2>
<p>The short build-up is not stubbornness — it is arithmetic. When the opponent presses high, they commit players forward, and every committed player is someone else now unmarked. Invite the press, survive the first pass or two, and the team that pressed has left holes behind itself; the keeper is effectively the spare man, and the first completed escape turns a siege into a counter-attack opportunity. Teams that play out well are not risking the ball for aesthetics — they are spending risk to buy the most valuable commodity in the modern game: an opponent caught on the wrong side of the ball.</p>
<h2>The cost, stated honestly</h2>
<p>The same geometry runs in reverse. A lost ball in your own third arrives with your whole team facing the wrong way, your defence scattered, and the nearest opposition player one pass from your goal — <strong>it is the most dangerous turnover in football by a distance</strong>. The variable is never the idea, it is the execution: first touches, passing range, the keeper's composure under a close press. A squad with the technicians should play this way; a squad without them is buying disaster at a discount. When it goes wrong on your screen on a Saturday, it is worth remembering there are two possibilities — a coach's plan beaten by a better press, or a squad attempting football it cannot actually play. Both exist; the second is the one that ends up on highlight reels.</p>
<p><em>And the duel at the heart of it: the press exists to break this (<a href="/pressing-explained/">how pressing actually works</a>), the build-up exists to beat the press. Most tactical evolution of the last decade is just these two ideas taking turns winning.</em></p>""",
[("Sporting Chronicle — the 1992 back-pass rule: origin and conditions", "https://sportingchronicle.com/back-pass-rule-explained"),
 ("Footymetrics — the back-pass rule under Law 12: mechanics, exceptions, the trick ban", "https://www.footymetrics.com/learn/back-pass-rule-explained")],
[("pressing-explained", "Pressing, blocks and the line"),
 ("how-var-works", "How VAR actually works"),
 ("possession-explained", "Possession: what it tells you")]),

("the-offside-trap", "The offside trap: the highest-wire act in defending",
"Step up in unison and you kill every through ball. Miss by half a stride and you have gift-wrapped a one-on-one. Why teams still take the bet.",
"""<p>It is the most elegant collective manoeuvre in football and the most humiliating when it fails: the entire defensive line stepping up together, on purpose, at the exact moment the opponent wants to play the ball forward — leaving the striker standing offside with his arm raised in complaint. Done right, the offside trap erases the most dangerous passes in the game without a single tackle. Done wrong, it is a clean run at goal for the opponent. This is the trade.</p>
<h2>The mechanic</h2>
<p>The trap exploits the law's timing rule: offside is judged at the moment the pass is <em>played</em> (<a href="/the-offside-rule-explained/">the full rule, explained</a>). So the defending line advances as a unit just before a through ball arrives, dropping the attackers beyond the last defender at the crucial freeze-frame. The reward is structural: with the line high, the space behind is shrunk, the midfield is compressed into a smaller area to defend, and the through ball — the most efficient pass in football — is switched off at source. Teams defend high not because they love risk but because the alternative concedes half the pitch.</p>
<h2>Why it fails</h2>
<p>The trap is a bet on <strong>unison</strong>, and unison is fragile. One defender slow off the mark — half a stride of doubt, a glance at the ball instead of the line — and everyone else's timing is undone; the attacker who was being trapped is now clean through with only the keeper left. That asymmetry is the whole drama: the reward for getting it right is modest (a free kick, a restart), and the price of getting it wrong is the single most valuable situation in the sport. It also asks defenders to do the unnatural thing — turn and sprint toward their own goal while the ball is played the other way — and asks the goalkeeper to sweep the grass behind the line like an extra defender.</p>
<h2>The modern twist: millimetres, measured</h2>
<p>Semi-automated offside technology at the top competitions now draws the freeze-frame lines from tracking data, and attackers have adapted in kind: timed runs with the trailing boot level with the last defender, goals decided by a toe's width measured to the centimetre. The trap has not died — it has got thinner. Every marginal advantage the technology strips from defenders raises the price of one lazy step, and the <a href="/how-var-works/">video review system</a> means even the misses get audited after the fact.</p>
<p><em>Watch a high defensive line for one half and count the bets: every through ball declined is the trap winning quietly, every ball over the top is the bill arriving. The best defending pairs in the world are the ones who step together for a decade — because the alternative to trust out there is a one-on-one.</em></p>""",
[],
[("the-offside-rule-explained", "The offside rule, explained"),
 ("pressing-explained", "Pressing, blocks and the line"),
 ("how-var-works", "How VAR actually works")]),
]
