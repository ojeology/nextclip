#!/usr/bin/env python3
"""Additional depth sections for the 16 articles, keyed by slug.

Each block is inserted immediately before the methodology note. Everything here is
still grounded in content/competitions.json, content/results.json and
content/pl-transfers.json — the same sources the main bodies use.
"""

EXTRA = {

'arsenal-title-defence': """
<h2>The fixture list is about to get harder</h2>
<p>Arsenal's two wins came against Coventry (3\u20130 away) and Aston Villa (1\u20130 at home). Those are the sides currently 19th and 18th, with one goal scored between them all season. The clean sheets are real; the opposition has been the weakest available.</p>
<p>That is not a criticism of Arsenal so much as a warning against reading too much into two matches. Chelsea on Sunday is the first fixture that tells us something, and it is followed by a run in which Arteta's side face several of the teams currently above the bottom five.</p>

<h2>The Gabriel Jesus question</h2>
<p>Selling Gabriel Jesus to Barcelona for \u00a38.6m was the window's quietest decision and may prove its most consequential. Arsenal have scored four goals in two games \u2014 fewer than Chelsea, Brighton, Manchester United or Manchester City \u2014 and did not sign a replacement centre-forward. Christos Tzolis at ~\u20ac40m is a wide player.</p>
<p>Bukayo Saka has two of those four goals. A title race in which Arsenal keep clean sheets but rely on a winger for goals is a narrower path than the table currently suggests.</p>

<h2>How the last two title races were decided</h2>
<p>The pattern in recent seasons has been consistent: the champion is rarely the highest scorer, but almost always has the best defensive record. Arsenal currently have that record by definition \u2014 nobody else has kept two clean sheets and conceded nothing. Manchester City are next on two conceded.</p>
<p>If that holds through October, Arsenal are in a strong position regardless of what the attack does. If it does not, the absence of a recognised striker becomes the story of their season.</p>
""",

'five-biggest-transfer-winners': """
<h2>The clubs that lost the window</h2>
<p>A list of winners implies losers, and three stand out.</p>
<p><b>Aston Villa</b> sold Morgan Rogers for around \u20ac138m, Youri Tielemans for ~\u20ac41m and Donyell Malen for ~\u20ac25m, then bought Nicolas Jackson (\u00a365m), Johan Manzambi (~\u20ac60m) and Jo\u00e3o Gomes (~\u20ac40m). Enormous churn, and they have not scored a goal in two matches.</p>
<p><b>Newcastle United</b> sold Sandro Tonali (~\u00a3100m), Bruno Guimar\u00e3es (~\u20ac87.5m) and Anthony Gordon, and reinvested in four largely unproven signings. Matthias Jaissle has four points from two games, which makes this the loss that might not be a loss.</p>
<p><b>Crystal Palace</b> banked \u00a351m for Maxence Lacroix and up to \u00a322m for Daniel Mu\u00f1oz, and replaced them with free transfers and a swap deal. They are bottom four and have conceded six.</p>

<h2>Why headline fees mislead</h2>
<p>Tottenham spent \u00a3185m on two midfielders and are last. Hull City spent \u00a33m on a goalkeeper and are fourth. Over a full season the money usually wins, which is why our list is weighted towards clubs that spent well rather than clubs that spent least \u2014 but the first fortnight is a useful reminder that a squad is a system, not a sum.</p>
<p>The clearest evidence for that is Manchester City. They did not simply spend the most; they spent it on two players who fill the same structural hole in different ways, which is what allows a side to lose four senior defenders and still look coherent.</p>

<h2>What we will be checking in January</h2>
<p>Three questions decide whether this list ages well: does Enzo Fern\u00e1ndez make City better than Guardiola's final side; does Bruno Guimar\u00e3es keep Arsenal's midfield injury-free; and do Tottenham score enough goals to make \u00a3185m of midfield relevant. We will revisit all three when the next window opens.</p>
""",

'five-clubs-that-still-need-signings': """
<h2>The free agent market is still open</h2>
<p>One detail worth remembering: the transfer window closing does not stop clubs signing players without a contract. Every one of these five could add an unattached free agent tomorrow, and several will if injuries arrive.</p>
<p>It is an imperfect tool. The players available are, by definition, the ones nobody signed during the window. But Arsenal took Illan Meslier on a free, Brentford took Callum Wilson, Liverpool's rivals took Andy Robertson and Martin D\u00fabravka to Tottenham \u2014 useful players do move for nothing.</p>

<h2>What coaching can actually fix</h2>
<p>Of the five gaps we have identified, two are coachable and three are not.</p>
<p>Crystal Palace's defensive problem is largely structural: they lost two starters and are asking free signings to replicate them. A back line can be drilled into better shape, and Pierre Sage has four months to do it.</p>
<p>Fulham's lack of depth is similarly manageable if \u00c1lvaro Arbeloa rotates carefully and the squad stays healthy.</p>
<p>Tottenham, Aston Villa and Coventry all need goals, and goalscoring is the hardest thing to coach into a squad that does not have it. Spurs have the most talented squad of the three and the most obvious absence \u2014 no recognised number nine \u2014 which is why they are top of our list despite spending the most money.</p>

<h2>The January consequence</h2>
<p>Every one of these clubs will now pay a premium in January, because selling clubs know exactly how badly they need the position filled. A striker who cost \u00a340m in August costs \u00a355m in January to a side sitting in the relegation zone.</p>
<p>That is the real cost of an unfinished window, and it is why the sides on this list would have been better served by a less impressive summer that solved a duller problem.</p>
""",

'five-matches-we-cannot-wait-to-watch': """
<h2>How to watch from Nigeria</h2>
<p>Kick-off times in West Africa Time are the same as UK time during British Summer Time, so Arsenal v Chelsea at 16:30 UK is 16:30 in Lagos. Continental fixtures listed in CEST are one hour ahead of WAT \u2014 so Juventus v Milan at 20:45 CEST is 19:45 in Lagos.</p>
<p>That makes this a genuinely convenient weekend: the Friday night Ligue 1 game starts at 20:05 WAT and the biggest Sunday fixtures land in the early evening rather than late at night.</p>

<h2>The fixture we nearly included</h2>
<p>Hull City v Aston Villa on Saturday was the hardest omission. Hull are fourth with two wins and no goals conceded; Villa are 18th with no goals scored and five conceded. A promoted side and a club that finished in the European places last season, currently separated by fourteen places.</p>
<p>It missed the list because one-sided form lines rarely produce good matches, but it is the fixture most likely to produce a result nobody expects.</p>

<h2>What makes a good weekend fixture</h2>
<p>We pick these on three things: whether the two sides are close in the table, whether their styles genuinely conflict, and whether something is actually at stake this early in a season.</p>
<p>Arsenal v Chelsea satisfies all three \u2014 first against third, the best defence against a leaky attack, and an early marker in a title race. PSG v Monaco satisfies the second and third but not the first. Valencia v Barcelona satisfies none of them on paper and is included purely because the Mestalla has a habit of ignoring form.</p>
<p>That last one is the honest admission in any preview: some fixtures are worth watching because of where they are played rather than who is playing well.</p>
""",

'five-things-fans-will-talk-about-this-weekend': """
<h2>The argument nobody is having yet</h2>
<p>Aston Villa have played two Premier League matches and scored zero goals. They sold Morgan Rogers to Chelsea for around \u20ac138m, Youri Tielemans to Manchester United and Donyell Malen to Roma \u2014 where he has since scored five goals in two games.</p>
<p>Unai Emery brought in Nicolas Jackson for \u00a365m, Alejandro Garnacho on loan and Johan Manzambi for ~\u20ac60m. Villa are 18th with zero goals and five conceded, and almost nobody is talking about it because Tottenham are bottom and louder.</p>

<h2>Why September arguments are usually wrong</h2>
<p>Every point made above rests on two matches. Two matches is roughly five per cent of a season, and the sample is skewed by fixture difficulty: Arsenal have played the two lowest-scoring sides in the league, while Manchester United opened away at the division's only other unbeaten defence.</p>
<p>The useful way to hold these arguments is to name the thing that would change your mind. Ours: if Tottenham score twice in their next match, the \u00a3185m story dies. If Hull concede three, the clean-sheet story dies. If Liverpool win at Ipswich, the crisis framing dies.</p>

<h2>What we would actually bet on</h2>
<p>Of the five, the one most likely to still be true in December is the Liverpool point. Losing Salah, Robertson and Konat\u00e9 for nothing in a single summer is a structural problem, not a form problem, and no amount of coaching from Andoni Iraola replaces a decade of goals.</p>
<p>The one least likely to survive is Hull City's position. Fourth is not sustainable for a side that spent \u00a33m on its most expensive signing \u2014 but the clean sheets might be, and that is a different and more interesting claim.</p>
""",

'liverpools-next-chapter': """
<h2>What two 2\u20132 draws actually tell us</h2>
<p>Liverpool drew 2\u20132 at Newcastle and 2\u20132 at home with Nottingham Forest. In both, they scored twice \u2014 which is more than Arsenal have managed in either game \u2014 and conceded twice.</p>
<p>That is a meaningful distinction. This is not a side that has stopped creating chances; the goals are still arriving. The problem is at the other end, where a defence missing Ibrahima Konat\u00e9 has conceded in both matches against opponents currently sixth and fifteenth.</p>
<p>Ronald Ara\u00fajo's loan from Barcelona is therefore the most important piece of business Liverpool did. If he settles, the attacking output already looks sufficient for a top-four campaign.</p>

<h2>The financial reality of three frees</h2>
<p>Salah, Robertson and Konat\u00e9 left for nothing. Konat\u00e9 alone would have commanded a substantial fee twelve months earlier, and Real Madrid took him without paying one.</p>
<p>The consequence is visible in the incoming column: J\u00e9r\u00e9my Jacquet and V\u00edctor Mu\u00f1oz arrived for undisclosed fees and Ara\u00fajo on loan. Liverpool did not have transfer income to reinvest, which is why the rebuild looks modest next to Manchester City's \u00a3306m or Tottenham's \u00a3185m.</p>

<h2>The Iraola question</h2>
<p>Andoni Iraola built his reputation at Bournemouth on a high-intensity press and rapid transitions \u2014 a style that demands enormous running from the front three and disciplined defending behind it.</p>
<p>Liverpool's squad was assembled for a different manager. Adapting it takes a pre-season at minimum and realistically half a campaign. Two points from six is a poor return; it is also roughly what a stylistic transition looks like in its opening weeks.</p>
<p>The fixture at Ipswich on Friday is the sort Liverpool must win to keep the top four realistic, and our <a href="/sports/predictions/">predictions page</a> backs them to do it.</p>
""",

'managers-with-most-to-prove': """
<h2>The three who kept their jobs and still have something to prove</h2>
<p>Not every manager under pressure is a new appointment.</p>
<p><b>Roberto De Zerbi</b> was backed with \u00a3185m for Sandro Tonali and Mateus Fernandes and has Tottenham bottom of the table with zero goals scored. No manager in the division has a wider gap between investment and return.</p>
<p><b>Unai Emery</b> sold Morgan Rogers for around \u20ac138m and has Aston Villa 18th, also without a goal. Emery has credit in the bank at Villa Park; he will need some of it.</p>
<p><b>Frank Lampard</b> spent \u00a368.5m-plus getting promoted Coventry ready and they have not scored a Premier League goal. Manchester City visit on Saturday.</p>

<h2>How quickly these judgements change</h2>
<p>Matthias Jaissle is the instructive case. He replaced Eddie Howe, immediately lost Tonali, Bruno Guimar\u00e3es and Anthony Gordon, and by any reasonable pre-season assessment had the hardest job in the league. Newcastle then won 2\u20130 at Tottenham and sit sixth.</p>
<p>Two matches has moved him from most-pressure to least. It will move him back just as fast if the young signings need time, which most young signings do.</p>

<h2>What we are actually measuring</h2>
<p>The fair test for a new manager is not league position in September. It is whether the team looks like it is being coached towards something identifiable.</p>
<p>On that measure, Enzo Maresca and Oliver Glasner come out best \u2014 both have clear structures visible already. Xabi Alonso comes out worst, because a Chelsea side winning 4\u20133 and 3\u20132 does not resemble anything he has built before. Being top of the table buys him time to fix it, and the visit to Arsenal on Sunday will show whether he has started.</p>
""",

'manchester-city-without-guardiola': """
<h2>What the departures actually cost</h2>
<p>The incoming business has dominated coverage, but the outgoing column is where the risk sits. John Stones, Manuel Akanji and Nathan Ak\u00e9 all left without confirmed destinations, and Bernardo Silva joined Real Madrid on a free.</p>
<p>That is three senior centre-backs and the squad's most versatile creator, replaced by two central midfielders and a winger. City have conceded two goals in two matches, so nothing has broken \u2014 but the structural change is larger than the results so far suggest.</p>

<h2>The one thing Guardiola left behind</h2>
<p>Erling Haaland. Two goals in two games, and the single biggest reason a managerial transition at the Etihad is survivable. A side that changes philosophy, loses four defenders and rebuilds midfield can still win matches if the centre-forward converts what arrives.</p>
<p>Rayan Cherki's two goals matter for the same reason: City's attacking output has not depended on the new signings settling, which buys Maresca weeks he would not otherwise have.</p>

<h2>How other clubs have handled this</h2>
<p>Replacing a long-serving, era-defining manager usually costs a season. The clubs that avoid it tend to do one of two things: promote from within to preserve continuity, or spend heavily enough that the squad improves faster than the system degrades.</p>
<p>City have chosen the second, decisively. \u00a3306m on three players is not a hedge; it is a bet that quality covers transition. The first evidence is encouraging and the sample is tiny.</p>

<h2>The measurable test</h2>
<p>Watch the goals-conceded column rather than the points column between now and November. City finished the previous era as one of the meanest defences in Europe. If they are still conceding around one a game in three months with this personnel, the transition has worked. If it drifts towards two, the missing centre-backs will be the story.</p>
""",

'manchester-united-finally-their-season': """
<h2>The \u00a3150m midfield, examined</h2>
<p>Andrey Santos (~\u00a350m), Carlos Baleba (\u00a365\u201370m) and Youri Tielemans (~\u00a335m) is a lot of money for one area of the pitch. It is also a coherent plan: Santos and Baleba are ball-winners, Tielemans is a passer, and between them they replace Casemiro's role with players a decade younger.</p>
<p>The early evidence is mixed. United have scored five goals in two games, which suggests the midfield is supplying the attack. They have also conceded four, which suggests it is not yet protecting the defence. Both things are usually true of a midfield still learning each other.</p>

<h2>Why the Hull defeat matters more than the Ipswich win</h2>
<p>Beating Ipswich 5\u20132 at home is what a top-half side is supposed to do. Losing 2\u20130 at a promoted club in the opening week is what United have done repeatedly in recent seasons, and it is the pattern Michael Carrick was appointed to break.</p>
<p>Hull have since kept a second clean sheet and sit fourth, which softens the result considerably. It does not remove the point: United's problem for several years has been the away fixtures nobody circles, not the ones they lose to title rivals.</p>

<h2>The Bruno Fernandes dependency</h2>
<p>Three of United's five goals have come from their captain, from midfield. That is superb individual form and a structural warning. Rasmus H\u00f8jlund's loan to Napoli became permanent and no replacement centre-forward arrived.</p>
<p>If Fernandes stops scoring at this rate \u2014 and three in two is not a sustainable rate for a midfielder \u2014 the question becomes who does. That is the single number worth tracking through September.</p>

<h2>A realistic ceiling</h2>
<p>United are tenth with three points. The squad is deeper than last season's and younger in the areas that were oldest. Top four is plausible; a title challenge, with four goals conceded in two games and no recognised striker signed, is not the argument this season is about.</p>
""",

'marescas-second-attempt-in-england': """
<h2>What went wrong the first time</h2>
<p>Maresca's previous spell in English football ended with a reputation for control that his critics called caution. The complaint was consistent: patient build-up produced territory and possession but not enough clear chances, and matches that should have been won comfortably were drawn.</p>
<p>The reason it matters now is that Manchester City is the least forgiving environment in which to relearn that lesson. City draws are treated as defeats.</p>

<h2>Why this squad suits him better</h2>
<p>The criticism of his approach loses force when the squad contains Erling Haaland. Patient build-up producing few clear chances is a problem when nobody converts them; it is a strategy when the centre-forward scores from almost anything.</p>
<p>Haaland has two goals in two matches. Rayan Cherki has two more. The system's weakness \u2014 chance volume \u2014 is precisely the weakness this squad is built to absorb.</p>

<h2>The defensive gamble</h2>
<p>Losing John Stones, Manuel Akanji and Nathan Ak\u00e9 in one window leaves a thin back line, and Maresca's structure asks defenders to hold a high line and defend large spaces behind it. That combination \u2014 high line, fewer senior centre-backs \u2014 is the clearest risk in his plan.</p>
<p>G\u00e9r\u00f3nimo Rulli arrived from Marseille for around \u00a31.7m as goalkeeping cover, which is sensible but does not address the outfield issue.</p>

<h2>What success looks like by Christmas</h2>
<p>Not necessarily top of the table. A reasonable measure would be: City within three points of the leaders, conceding around a goal a game, and the Enzo Fern\u00e1ndez\u2013Elliot Anderson pairing established as the first-choice midfield.</p>
<p>Hit those three and Maresca has done the hard part, because the hard part was never winning matches against Coventry. It was replacing a manager whose ideas had defined the club for a decade without the squad losing its shape while he did it.</p>
""",

'newly-promoted-clubs-approach': """
<h2>What the historical pattern says</h2>
<p>Promoted clubs that survive tend to share two traits: they concede fewer than sixty goals, and they take points at home against the sides around them. Neither requires spending heavily; both require organisation.</p>
<p>That is why Hull's start is more encouraging than Coventry's, despite the gap in outlay. A promoted side that keeps clean sheets has found the harder half of the formula. A promoted side that spends \u00a368.5m and cannot score has found neither.</p>

<h2>Coventry's case for patience</h2>
<p>The counter-argument is straightforward: Coventry's two fixtures were away at Arsenal and at home to Hull \u2014 the division's two meanest defences, neither of which has conceded a goal to anyone. Failing to score against those two is not evidence of much.</p>
<p>Frank Lampard's signings also skew young and expensive, and Caleb Yirenkyi, Loum Tchaouna and Aur\u00e8le Amenda were bought for a season's development rather than an August impact. The \u00a368.5m looks alarming now and may look shrewd in April.</p>

<h2>Ipswich and the cost of changing manager</h2>
<p>Kieran McKenna stepping down after promotion was the most disruptive thing that happened to any of the three. Gary O'Neil inherited a squad built by someone else and then added seven players to it, which means Ipswich are simultaneously integrating a new manager and a new spine.</p>
<p>They beat Sunderland 2\u20131 and lost 5\u20132 at Manchester United. Conceding five is the number that should worry them; Kjell Scherpen (\u00a311m) arrived in goal and the defence in front of him is largely unchanged from the Championship.</p>

<h2>Our survival call</h2>
<p>Ipswich look the most likely of the three to stay up, because they have both spent money and retained the squad that won promotion. Hull's start is the best and their squad is the thinnest. Coventry have the best players and, at present, no way of scoring with them.</p>
""",

'players-to-watch-this-weekend': """
<h2>The names missing from these lists</h2>
<p>Two absences are worth noting. The most expensive signings of the window \u2014 Enzo Fern\u00e1ndez (\u00a3125m), Morgan Rogers (\u00a3117m), Elliot Anderson (~\u00a3116m) and Sandro Tonali (\u00a3100m) \u2014 appear nowhere in the Premier League scoring charts.</p>
<p>That is entirely normal for central midfielders in the opening fortnight, and it is also why goal charts are a poor way to judge a transfer window. Watch Fern\u00e1ndez and Anderson this weekend for how often City's midfield recovers the ball in the opposition half, not for goals.</p>
<p>The second absence is a Tottenham player, because Tottenham have not scored.</p>

<h2>Small samples, honestly labelled</h2>
<p>The Bundesliga has played one round. Younes Ebnoutalib and Yuito Suzuki have three goals each from a single appearance, which is a hat-trick and nothing more \u2014 no player sustains three goals per game.</p>
<p>The same caution applies to Jack Hinshelwood's two goals in one appearance for Brighton. These are worth watching precisely because they are extreme: the interesting question is not whether the rate continues but whether the player keeps starting once it stops.</p>

<h2>The most reliable indicator this early</h2>
<p>Minutes. A player scoring at a high rate off the bench tells you less than a player who has started every match for a side winning games. On that measure the names to trust are Raphinha (three starts, five goals, league leaders Barcelona), Kylian Mbapp\u00e9 (three starts, four goals, Real Madrid unbeaten) and Bruno Fernandes (two starts, three goals).</p>
<p>All three play for sides who will dominate possession this weekend, which is the simplest reason to expect the numbers to keep climbing.</p>
""",

'players-who-could-explode-this-season': """
<h2>What "exploding" actually requires</h2>
<p>Three conditions, in our experience: a guaranteed starting place, a side that creates chances, and a manager with a reason to be patient. Talent is the least reliable predictor \u2014 every squad in the Premier League is full of it.</p>
<p>That framework explains why Jack Hinshelwood tops our list ahead of more expensive names. Brighton have scored seven goals in two matches, Fabian H\u00fcrzeler is contracted through 2029 and has just rebuilt the squad around young players, and Hinshelwood is already scoring. All three boxes.</p>
<p>It also explains our caution about the \u00a3100m arrivals. Elliot Anderson and Enzo Fern\u00e1ndez have the starting place and the chance-creating side, but a new manager at Manchester City has every incentive to win immediately rather than develop patiently.</p>

<h2>The one nobody is discussing</h2>
<p>Ronald Ara\u00fajo, on loan at Liverpool from Barcelona with a reported option to buy. Defenders never appear on breakout lists because the evidence for them is invisible in the goal charts.</p>
<p>Liverpool have conceded in both matches and lost Ibrahima Konat\u00e9 on a free. If Ara\u00fajo settles, he transforms the season of a club that finished the summer looking diminished \u2014 and he does it in a shirt he may keep permanently.</p>

<h2>Where this list will look wrong</h2>
<p>Emersonn is the riskiest inclusion. \u00a326.6m is a club-record outlay for a promoted side and Ipswich have already conceded six goals in two games. A striker in a team defending that badly spends the season chasing matches rather than leading them.</p>
<p>Morgan Rogers is the safest, and therefore the least interesting: a \u00a3117m player at the league leaders is not a breakout, he is an established one. We included him because Aston Villa have not scored since selling him, which is the most emphatic case any player has for his own importance.</p>
""",

'premier-league-banter-table': """
<h2>The table if we ranked by money spent</h2>
<p>Reorder the division by outlay this summer and it looks nothing like the real thing. Manchester City (roughly \u00a3306m on three players) would lead, Tottenham (\u00a3185m on two) would be second, Chelsea third and Manchester United fourth.</p>
<p>Hull City would be last by a distance \u2014 \u00a33m on Jack Butland and three free transfers \u2014 and they are fourth in the table that counts. Coventry would be mid-table on spending and are 19th.</p>
<p>Two matchweeks is far too short a sample to draw a conclusion from that, but it is long enough to enjoy it.</p>

<h2>Five records that will not survive September</h2>
<p><b>Arsenal, Hull City and Monaco have conceded nothing.</b> Somebody will score against all three within a fortnight.</p>
<p><b>Tottenham and Aston Villa and Coventry have scored nothing.</b> All three will find a goal, probably in the most anticlimactic circumstances available.</p>
<p><b>Bruno Fernandes is the league's top scorer.</b> A midfielder leading the charts in May would be remarkable; leading it in September is a fortnight of good finishing.</p>
<p><b>Brighton have scored seven and conceded four in two games.</b> That is a rate of five and a half goals per match involving Brighton, which nobody should want to end.</p>
<p><b>Jack Hinshelwood has two goals in one appearance.</b> Enjoy the ratio while it lasts.</p>

<h2>In defence of the September table</h2>
<p>Everyone repeats that early tables mean nothing, and everyone checks them anyway. There is a reason: they are the only evidence that exists. Every argument about whether Tottenham wasted \u00a3185m or Hull are the story of the season rests on the same two matches, and pretending otherwise is just a slower way of having the same conversation.</p>
<p>So read this table, laugh at your rivals, and understand that in eight weeks it will be unrecognisable. That is the whole appeal.</p>
""",

'rodris-future': """
<h2>The cost of getting it wrong</h2>
<p>Manchester City committed roughly \u00a3241m to two central midfielders in a single window. If the pairing works, it is the most important structural fix any English club made this summer. If it does not, City have spent a British-record fee on a player who does not fit alongside the other British-record fee they had already agreed.</p>
<p>That is the genuine risk in the approach. Enzo Fern\u00e1ndez and Elliot Anderson are both progressive, ball-carrying midfielders. Neither is a natural defensive screen in the mould of the player they collectively replace.</p>

<h2>Who actually shields the defence?</h2>
<p>This is the unanswered question. With John Stones, Manuel Akanji and Nathan Ak\u00e9 all departed and no specialist holding midfielder signed, the protection in front of a rebuilt back line is being provided by two players whose strengths are in possession.</p>
<p>Ayyoub Bouaddi's arrival from Lille is the closest thing to an answer, and he is young enough that relying on him would be optimistic in a title season.</p>
<p>City have conceded two goals in two matches, against Crystal Palace and Bournemouth. Neither tested this.</p>

<h2>The wider lesson for other clubs</h2>
<p>Every side eventually faces the same problem: a player so specific to the system that no direct replacement exists. The conventional response is to search for a like-for-like signing, usually for years and usually unsuccessfully.</p>
<p>City's response \u2014 change the requirement rather than fill the gap \u2014 is the more interesting one, and if it works it will be copied. Liverpool are facing an equivalent problem after losing Mohamed Salah on a free, and they have not yet chosen an approach.</p>

<h2>When we will know</h2>
<p>By November. City's opening fixtures have been kind, and the structure will not be seriously examined until they face a side that presses their build-up and attacks the space behind their full-backs. Until then, six points from two games proves only that the plan has not failed yet.</p>
""",

'tactical-questions-ahead-of-matchweek-1': """
<h2>A sixth question: what happens to the promoted defences?</h2>
<p>Hull City have conceded nothing and sit fourth. Ipswich have conceded six and sit eleventh. Coventry have conceded four and scored none.</p>
<p>Promoted sides almost always concede more as the season progresses, for a simple reason \u2014 opponents build a video file on them. A deep block that nobody has analysed is far more effective in August than the same block in January. Whether Sergej Jakirovi\u0107 can adapt Hull's shape once teams solve it is a better question than whether the clean sheets continue.</p>

<h2>The pattern across Europe</h2>
<p>The same tension appears in every top-five league right now. In Spain, Barcelona have scored twelve in three and Real Madrid ten, while Valencia have scored one. In Italy, Roma have won 4\u20130 twice without conceding, and Fiorentina have conceded seven without scoring. In France, Monaco have won both without conceding.</p>
<p>Early seasons exaggerate. Attacking sides that are sharp look unstoppable, and defensive sides that are organised look impenetrable, because neither has yet met an opponent who has worked them out. Nearly all of these extremes regress by October.</p>

<h2>What we would watch in each match</h2>
<p>At Arsenal v Chelsea, watch where Chelsea lose the ball. Five goals conceded in two wins suggests turnovers in midfield, and Arsenal are built to punish exactly that.</p>
<p>At Manchester City v Coventry, watch City's full-backs. If they push high against a side with no attacking threat, that is Maresca committing to his structure regardless of the missing centre-backs.</p>
<p>At Hull v Aston Villa, watch how long Hull's block holds. Villa have not scored all season and Hull have not conceded; one of those runs ends on Saturday.</p>
""",
}

CLOSER = {
'five-things-fans-will-talk-about-this-weekend': """
<h2>One prediction to settle an argument with</h2>
<p>Tottenham score at least twice in their next match. They have created chances in both games without converting, the squad is far too expensive to keep producing zeroes, and negative runs this extreme almost always break suddenly rather than gradually.</p>
<p>If we are wrong, the \u00a3185m story becomes the defining one of the Premier League season and De Zerbi's position starts being discussed seriously before October.</p>
""",
'liverpools-next-chapter': """
<h2>The three numbers that decide their season</h2>
<p><b>Goals conceded.</b> Two in two so far. Liverpool need this closer to one a game, and that depends almost entirely on Ronald Ara\u00fajo settling at centre-back.</p>
<p><b>Goals from outside the front line.</b> With Salah gone, a decade of guaranteed output has left the squad. Midfield and wide players have to replace roughly twenty goals between them.</p>
<p><b>Points by the end of October.</b> Two from six is a slow start, not a crisis. Liverpool's fixture list is navigable through the autumn; if they are still averaging a point a game when the clocks change, the top four becomes genuinely difficult.</p>
""",
'manchester-united-finally-their-season': """
<h2>The verdict</h2>
<p>No \u2014 not this season, on the evidence available. But the direction is finally right, which is more than could be said twelve months ago.</p>
<p>United have a young midfield that cost \u00a3150m, a captain in the best scoring form of his career and a manager whose appointment has been made permanent rather than provisional. Those are the foundations of a good side.</p>
<p>What they do not have is a centre-forward or a defence that keeps clean sheets, and no team wins a Premier League title without at least one of the two. Top four is the honest target, and beating Everton on Sunday would be a reasonable place to start.</p>
""",
'marescas-second-attempt-in-england': """
<h2>The verdict</h2>
<p>Yes, with one condition. Maresca has the striker his system has always needed, a midfield rebuilt to his specification and a squad deep enough to absorb a poor month.</p>
<p>The condition is the back line. Three senior centre-backs left and none were replaced, and a high defensive line without established defenders behind it is the one way this plan fails quickly.</p>
<p>City host Coventry on Saturday and will win comfortably. The season starts properly the first time somebody runs at that defence.</p>
""",
'players-to-watch-this-weekend': """
<h2>Our three picks, in order</h2>
<p><b>Donyell Malen (Roma v Atalanta).</b> Five goals in two matches for a side that has won 4\u20130 twice without conceding. The best form of any forward in Europe, against a defence good enough to make it a genuine contest.</p>
<p><b>Raphinha (Valencia v Barcelona).</b> Five in three, and Valencia have conceded four while scoring one. The most favourable matchup on the board for a player already leading his league.</p>
<p><b>Bruno Fernandes (Everton v Manchester United).</b> Three goals in two from midfield, away at an unbeaten side. If United are to win, he almost certainly decides it.</p>
<p>Predicted scorelines for all three, and for the other 45 fixtures across Europe, are on our <a href="/sports/predictions/">predictions page</a>.</p>
""",
'tactical-questions-ahead-of-matchweek-1': """
<h2>The one we most want answered</h2>
<p>Tottenham's. The other four questions are about whether something good continues; this one is about whether something broken can be fixed without a transfer market.</p>
<p>Roberto De Zerbi has £185m of midfield, no recognised centre-forward and four months until he can sign one. Everything he tries between now and January — a false nine, a winger through the middle, Mudryk central — will be a coaching solution to a recruitment problem, and those are the most interesting experiments in football to watch.</p>
""",
'rodris-future': """
<h2>The verdict</h2>
<p>City have given the most convincing answer available to a question that had no clean solution. Buying two elite midfielders instead of hunting for one irreplaceable profile is expensive, imaginative and \u2014 on two matches of evidence \u2014 working.</p>
<p>It is also unfinished. The pairing solves possession and progression; it does not obviously solve protection, and City removed three senior centre-backs in the same window. That combination is the reason to withhold judgement until the fixtures get harder.</p>
<p>Ask again in November, after City have played someone who presses them.</p>
""",
}
