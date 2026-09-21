# -*- coding: utf-8 -*-
"""BRYME Entertainment desk — the review shelf (Phase 1 engine, batch 1).

One dict per reviewed film. The four axes are the published method at
/entertainment/scoring/ : story, craft (performance), vision (direction &
technical), weight (cultural meaning). Score is the axis average to one
decimal, half-points allowed, rounded to the nearest half on the film card.
Reviews are desk opinion, written and signed by the editorial desk; they are
never sold, never previewed to rights-holders, and a revision is recorded by
changing `date` — the page prints it.

To add a review: append one dict below, run the build. It renders, joins the
shelf index, links itself into the matching catalogue card (if the film has
one), carries Review schema, and enters the sitemap automatically.
"""

REVIEWED_BY = "The BRYME Entertainment desk"

REVIEWS = [
dict(
    slug="living-in-bondage", title="Living in Bondage", year=1992,
    director="Chris Obi Rapu", country="Nigeria", language="English / Igbo",
    runtime=None, axes=dict(story=7.0, craft=5.0, vision=5.0, weight=10.0),
    score=6.5, date="2026-09-21",
    verdict="Crude, grieving, unforgettable: the film that proved Nigerian stories could carry a video economy on their own shoulders.",
    body=[
     "There is no reviewing Living in Bondage on the terms of the films that came after it — because almost every Nigerian film that came after it exists because of this one. A man in debt, a friend's offer no one should take, a ritual that costs the one thing money cannot buy back: the architecture is a folktale warning, assembled with the budget of a trade ministry and the reach of a market stall, and it changed how an entire continent made movies.",
     "What survives on screen is the mess. The production values are brutal by any fair standard — sound that arrives late, blocking that waits for the camera to remember where it is, a cutting rhythm that feels like necessity rather than style. But the story's moral engineering is real. Richard's downward turn earns its dread because the film keeps showing the ledger: each ritual payment is also an emotional amputation. When the price finally presents itself in the film's most infamous sequence, the shock lands not because of what is on screen but because of everything the story quietly subtracted from the man.",
     "The performances belong to conviction rather than craft. They shout where a director with more resources would have whispered, and there are scenes that run ten minutes too long because someone believed the speech was the point. Watch anyway, because these are actors performing for an audience that had never seen themselves on tape before, and the seriousness of the room is legible in every frame.",
     "Its cultural weight is not arguable and this desk does not argue it: a home-video industry estimated in the thousands of titles traces its business model — market-distributed VHS made fast, made local, made for the diaspora — to this film's demonstration that the audience was waiting. Judged as cinema it is rough; judged as history it is required. The honest BRYME score leans on both: technically weak, structurally sound, civilisationally load-bearing.",
     "New viewers should approach it the way one approaches a carved lintel in a museum: the aesthetics are not the point. Watch for the moment Nigerian storytelling stopped asking permission.",
    ],
),
dict(
    slug="glamour-girls", title="Glamour Girls", year=1994,
    director="Frank Rajah Arase", country="Nigeria", language="English",
    runtime=None, axes=dict(story=6.0, craft=6.0, vision=5.0, weight=9.0),
    score=6.5, date="2026-09-21",
    verdict="The video era's great moral panic — a campus-to-city cautionary tale whose notoriety still outdrives its craft.",
    body=[
     "Two classmates arrive in Lagos with the same start and opposite ends: one studies, the other sells. Glamour Girls built that simple fork into the most talked-about Nigerian video of its era, and you can still feel why. It understood that a moral fable is only worth telling if the wrong road looks genuinely tempting — the film films the glamour before it judges it, and the judging has to fight for the frame.",
     "The craft is that of a production learning its grammar in public. There is a recurring shot — faces held slightly too long, mid-speech — that reads like budget discipline mistaken for emphasis, and sometimes it accidentally is. The soundtrack works overtime. The editing follows dialogue rather than geography, so Lagos changes shape between cuts like a rumour does.",
     "What gives the film its grip in 2026 is its nerve about money. It draws the economy of survival without euphemism: rent, feeding, the arithmetic a young woman runs every time she looks in a mirror. Its conservatism is real — the ending collects its debts in the fashion of the decade — but the social observation inside the cautionary shell is sharper than its reputation allows.",
     "The weight is the reason to watch. Few Nigerian films of any era have provoked comparable argument — parents' associations, church bulletins, a national conversation about what women on screen were allowed to want. That argument is part of Nigerian cinema's coming-of-age, and this is the tape it happened on. Scored as craft it sits in the middle; scored as a document of what the industry was willing to risk, it rises well above the year of its making.",
    ],
),
dict(
    slug="the-wedding-party", title="The Wedding Party", year=2016,
    director="Kemi Adetiba", country="Nigeria", language="English",
    runtime=None, axes=dict(story=7.0, craft=7.0, vision=7.0, weight=7.0),
    score=7.0, date="2026-09-21",
    verdict="Slick, warm, four-couples busy: the film that made the industry believe in its own box office — and mostly earns it.",
    body=[
     "Kemi Adetiba's feature debut arrives with an advertisement's polish and an ensemble's chaos, chasing four weddings' worth of secrets through a single Lagos weekend. Duncan and Toniki's big day corrals an ex on each side, a family grudge, a hair-week from hell, and a city that will not keep its phone calls short. The shape is borrowed — this is the franchise-era ensemble rom-com formula worn with Nigerian tailoring — but the tailoring is genuinely excellent.",
     "The film's smartest instinct is balance. Adunni's subplot could have played as villain scenery; it plays as the story's hardest question — who do you become when the room full of your past expects your worst. Ayoola Smart sells Toniki's composure cracking in close-ups the editing is respectful enough to hold. The comedy knows its register: wedding-industry satire that never punches down at the clients it films.",
     "The seams show where the formula demands them: a third act of simultaneous revelations that resolve faster than they detonated, and at least one subplot that exists for the sequel it would eventually feed. There are minutes where you can feel the calendar — the film was built to be the biggest day of the year, and its business model is briefly louder than its story.",
     "Its weight is industrial. The Wedding Party proved, in money the industry could count, that a Nigerian film could open like a global one — the highest-grossing local release of its time and the proof that pushed distribution, marketing budgets and cinema chains to take the industry at its word. Half a decade on, the ensemble comedies filling those cinemas are still its children. Judged alone it is a very good genre film; judged as the pivot of a market, it is essential.",
    ],
),
dict(
    slug="half-of-a-yellow-sun", title="Half of a Yellow Sun", year=2013,
    director="Biyi Bandele", country="Nigeria / UK", language="English",
    runtime=None, axes=dict(story=5.0, craft=7.0, vision=6.0, weight=7.0),
    score=6.25, date="2026-09-21",
    verdict="The novel's war, the film's surface: beautiful performances stranded by an adaptation that keeps the plot and loses the time machine.",
    body=[
     "Chimamanda Ngozi Adichie's Biafra novel was the obvious prize and the obvious trap: a love story on a sliding scale toward atrocity, told in two registers — the heady Nsukka campus years and the refugee aftermath. Biyi Bandele's film keeps the characters and, crucially, keeps the cast capable of them: Thandiwe Newton's Olanna carries grief in her posture before the script admits it, and Chiwetel Ejiofor gives Odenigbo's decline the discipline of a man arguing with himself.",
     "What the film cannot survive is its own pacing. The university years — where the novel earns every later loss — are compressed to scenes that announce rather than inhabit; the political education that makes the war unbearable is reported in newsreel asides. When violence arrives it is significant without being felt, because the cinema of happiness it interrupts was only summarised.",
     "The craft is respectable and the ambition honest: shooting in Ghana, rebuilding the period with real care, trusting faces over exposition. But a war epic that hedges its chronology — that fears its audience will not follow two timelines — becomes one long, sad trailer for a better book.",
     "Its weight, this desk insists, is real: whatever the adaptation's flaws, it carried one of the defining Nigerian novels of the century to audiences who would not have met it otherwise, and its reception in Nigeria — impatient, exacting, loving the source more than the film — is itself a document of how seriously this industry's audience now takes its own stories on screen. Scored as film: below its cast. Scored as a chapter in the industry's story: worth your evening, followed by the book.",
    ],
),
dict(
    slug="king-of-boys", title="King of Boys", year=2018,
    director="Kemi Adetiba", country="Nigeria", language="English / Yoruba",
    runtime=None, axes=dict(story=8.0, craft=8.0, vision=7.0, weight=9.0),
    score=8.0, date="2026-09-21",
    verdict="A godmother tragedy in Lagos colours: stage-bound, operatic, and anchored by a lead performance that simply dares the camera not to blink.",
    body=[
     "Eniola Salami runs a political machine the way a Shakespearean house runs a grudge: publicly generous, privately absolute. Kemi Lala Akindoju plays her as a woman whose smile has a filing system, and the film's best idea is structural — telling the rise in flashbacks with the apparatus of theatre, as if power itself were a series of acts performed for different rooms.",
     "That theatrical decision is both the film's strength and its ceiling. Staged confrontations, monologues delivered at the edge of a set, a chorus of market women narrating like a Greek agora on duty: it is a choice, it mostly works, and you can feel its budget in every wide shot that wisely stays still. The language moves between English and Yoruba with political precision — who is addressed in which tongue is the film's second script.",
     "The story's true subject is not crime but succession: what a self-made empire costs the women who build it, and what it becomes when the heir wants out. The son's resistance gives the second hour its gravity — a mother who can command anyone except the one person she actually wants to reach, which is the oldest tragedy in the book and still earns its dividends here.",
     "King of Boys is a commercial proof-of-concept in its own right: a Nigerian release that toured like an event, with subtitles treated as an asset rather than an apology, and a follow-up series that tested whether this universe could sustain television weight. Its score sits with the performances and the nerve; its minor league is restraint — a two-and-a-half-hour cut that flatters some scenes it should be merciless about. Essential for anyone taking Nigerian cinema seriously, and the rare local epic that argues — mostly winningly — that it deserves the comparison to the genre's greats.",
    ],
),
dict(
    slug="anikulapo", title="Aníkúlápó", year=2022,
    director="Kunle Afolayan", country="Nigeria", language="Yoruba",
    runtime=None, axes=dict(story=7.0, craft=7.0, vision=8.0, weight=8.0),
    score=7.5, date="2026-09-21",
    verdict="A Yoruba-language epic that out-produced its doubts: gorgeous, stubborn, and a market turning point wearing ceremonial cloth.",
    body=[
     "A prince sold into slavery who will not die — the title names the promise — and Kunle Afolayan builds Aníkúlápó as a myth in period dress: pre-colonial court intrigue, a kingdom of ritual law, and a man whose curse is surviving every punishment a ruler invents. The premise is folklorically absurd exactly as folklore intends; a realist script would kill it, and the film wisely never apologises.",
     "The vision is the headline. The costume design alone — the woven patterning, the brass, the horse trappings — is a statement that a Nigerian production can dress a historical epic with conviction; Kunle Remi, in the title role, moves like a man the camera keeps deciding to fear. The sound mix and the grading choose dusk so often you will wonder if a second colourist exists — one mood per film is a style; the discipline deserves the score it gets.",
     "The story, correspondingly, is where the desk argues with the film. Aníkúlápó's middle third repeats its trial-and-resurrection mechanic until the audience learns the trick, and some court politics play like spectacle notes rather than narrative logic — characters explain what they will do before doing it, twice. A tighter cut by twenty minutes would trade some grandeur for momentum and lose nothing a legend requires.",
     "Its weight is commercial history with cultural teeth: a Yoruba-language production that a global platform funded and the world streamed, demonstrating that the audience for indigenous-language Nigerian cinema is not a niche but a continent with subtitles. For the Oyo-era material itself — the name, the pouch, the kingdom's texture — this is how most of that audience first met it. Flawed epic, essential milestone.",
    ],
),
dict(
    slug="mami-wata", title="MamiWata", year=2023,
    director="C.J. 'Fiyo' Obasi", country="Nigeria", language="Yoruba / English",
    runtime=None, axes=dict(story=6.0, craft=7.0, vision=9.0, weight=9.0),
    score=7.75, date="2026-09-21",
    verdict="A water myth shot in black and white like a fever that refuses colour: the most formally audited Nigerian film in a generation.",
    body=[
     "A lakeside village angers a goddess by taking her favourite singer — the bargain is struck, the water starts collecting — and C.J. Obasi tells it as myth rather than monster movie: people speak in proverbs, decisions are communal, and dread arrives like weather. The choice to shoot luminous monochrome in a colour-obsessed market is the film's first argument, and Jonathan Kovel's photography wins it — water, skin and ash rendered with a gravity colour could only have decorated.",
     "The craft runs in two registers: the formal setpieces — a flood staged as a slow choreography of bodies and cloth, a bar sequence with actual musical dramaturgy — and a looser folk cadence between them, where scenes keep their full, unhurried, village-runtime length. Some audiences will find the second register a patience test. It is also the point: the film refuses to edit indigenous storytelling into a trailer.",
     "The story is the honest weakness: a fable's logic means the pieces click into place only at the watery end, and a subplot's payoff arrives thinner than its setup promised. Its Sundance recognition for editing was earned by rhythm the writing does not quite match — a beautiful vessel with a simple liquid in it.",
     "The weight, though, is enormous. A Nigerian studio-backed feature choosing myth, monochrome and Yoruba as its mainstream gambit — and touring the festival circuit on those terms rather than in spite of them — redraws what local blockbusters are allowed to be. Half of its audience this year met a water spirit for the first time without a horror filter; that is cultural work. High marks for vision, fair marks for story, and the desk expects to be arguing about its influence for a decade.",
    ],
),
dict(
    slug="the-figure", title="The Figure", year=2023,
    director="Anebkara", country="Nigeria", language="English",
    runtime=None, axes=dict(story=6.0, craft=6.0, vision=6.0, weight=7.0),
    score=6.25, date="2026-09-21",
    verdict="A party-girl-accused thriller with a genuine subject — viral evidence — and a third act that blinks before its premise does.",
    body=[
     "A viral video makes a young woman the public's accused killer; she has days to prove the footage lied. The Figure's smartest element is its time design: a countdown structure that keeps the city in permanent motion, the accused moving through Lagos districts the way rumour moves through it. The film understands, correctly and uncomfortably, that its real villain is the verdict of an audience that has already pressed share.",
     "As thriller mechanics go, it is serviceable: clean wides, a synth-forward score that knows when to shut up, and a lead who can hold a frame while lying with her face. The craft wobbles where money and time ran out — an action sequence that cuts precisely to avoid what it cannot afford, and an antagonist whose reveal arrives with more costume than motive.",
     "The problem is the resolution's courage. A premise about how fast the internet destroys the innocent deserves a final turn that indicts the system that watched; this one, like many films of its size, individualises the guilt and hands the crowd an amnesty. The writing's instinct in the first two acts — everyone with a phone is on the jury — is the better film.",
     "Its weight rests partly outside the frame — a much-publicised rights dispute kept the title in the trade columns until release — but inside it, the film marks a genuine step: a Nigerian youth-culture thriller staged like a genre picture on a genre budget-line, aimed at the audience that grew up on streaming. Uneven, alive, and the kind of middle that a film industry needs more of: the movies between the masterpieces and the mistakes.",
    ],
),
dict(
    slug="atlantics", title="Atlantics", year=2019,
    director="Mati Diop", country="Senegal / France / Belgium", language="Wolof / French",
    runtime=None, axes=dict(story=7.0, craft=7.0, vision=9.0, weight=9.0),
    score=8.0, date="2026-09-21",
    verdict="The crossing told from the shore it left: migration cinema rebuilt as a ghost story, with the sea as both monster and archive.",
    body=[
     "Young workers on a Dakar construction site are owed wages and promised Europe; when their boat vanishes, the film does not follow the sea — it follows the women left in it, and then lets the dead return to collect. Mati Diop's feature debut is built on that reversal, and it is the whole argument: who gets to be the haunting.",
     "The vision is almost embarrassingly assured for a first film — the fire scenes glow like fever charts, the water moves through interiors with a photographer's patience, and the final possession sequence plays a boardroom as a tribunal. Diop hires non-actors and shoots them like scripture; Mama Sané's Ada carries the film's grief with a face that edits the frame around her. Cannes' Grand Prix arrived with, and deserved.",
     "The story asks patience: its middle holds long, quiet scenes that some viewers will read as drift — but the drift is the subject, the suspended time of waiting for news that will not come. Where it can fairly be struck is structure; a late act's mechanism explains more than the film's early mystery needed, and the documentary coda belongs to a different, less risky movie.",
     "Its weight is historic twice over: the first Senegal-directed feature in the Cannes competition in decades, and the work that reset what African migration cinema could be — no smuggler POV, no European shore, ghosts instead of statistics. The desk's only argument is with its reputation's ceiling, not its floor: this is required viewing for anyone in BRYME's francophone audience, and for everyone else, it is how the Atlantic should have been filmed all along.",
    ],
),
dict(
    slug="timbuktu", title="Timbuktu", year=2014,
    director="Abderrahmane Sissako", country="Mali / Mauritania", language="French / Arabic / Bambara / English",
    runtime=None, axes=dict(story=8.0, craft=8.0, vision=9.0, weight=10.0),
    score=8.75, date="2026-09-21",
    verdict="Occupation filmed as elegy: cowherds, banned music and a football match played without a ball — the gentlest fury in modern African cinema.",
    body=[
     "A herder family outside Timbuktu lives under a proclamation regime that bans music, cigarettes, football, and the way women's ankles look; the film watches, with unbearable patience, until the edicts come for Kinikou's cow — the famous milk-selling cow whose death sentence the audience somehow knows is also somebody's death sentence. Sissako assembles occupation not as war but as house rules.",
     "The vision does the arguing. A football match played in empty shorts, chasing a ball that cannot be kicked, is the single best scene about cultural prohibition of its decade — funny, athletic, and devastated. A rooftop radio plays hymns of music into the night while speakers announce its ban. Camera moves are slow enough that beauty keeps happening against the regime's schedule, and Sofian El Fani's light gives the desert the moral clarity of a parable.",
     "The craft is actors choosing restraint: the parents' stillness is the film's loudest instrument; the imam, debating a young jihadist in the town square, wins the movie's thesis with one raised finger — 'God does not need your war.' The regime's recruits are played with a documentarian's pity: boys in over-sized authority, terrifying and ridiculous at once.",
     "The weight is hard to overstate. Made when the occupation was fresh and the world's cameras had moved on, Timbuktu returned Mali to the world's screen — Oscar-nominated, festival-sweeping — and gave every later African film about extremism its method: refuse spectacle, keep the ledger of small kindnesses, let the audience do the sentencing. The third act earns its grief and loses a whisper of its patience to explicitness; nothing else here is improvable.",
    ],
),
dict(
    slug="tsotsi", title="Tsotsi", year=2005,
    director="Gavin Hood", country="South Africa", language="Zulu / Xhosa / Sotho / English",
    runtime=None, axes=dict(story=6.0, craft=8.0, vision=7.0, weight=8.0),
    score=7.25, date="2026-09-21",
    verdict="A township gangster finds a baby, and the film finds its thesis: tenderness as theft in a city built to make it impossible.",
    body=[
     "After a job, Tsotsi drives off with a passenger in his back seat — and the passenger is an infant. Gavin Hood's adaptation of Athol Fugard's novel keeps that spine and lets everything else bend around it: a crime thriller in the first reel, a man learning to heat a bottle in the second, an apology as long as a city block by the end.",
     "Presley Chweneyagae makes the transformation legible without softening the face — the same jaw that ordered a killing now argues with a baby's cry; the desk's vote for craft lives or dies on how long the film trusts that face, and mostly it does. Terry Pheto's Miriam, the mother he coerces into helping, gets the film's best speech and its only present tense.",
     "The honest criticism: Fugard's township picaresque gets smoothed into three-act morality — coincidences stack where the novel accumulated history, and the flashback mechanism arrives precisely when a thriller needs its tear-socket oil. Darryl Whetter's photography chooses golden where the story sometimes needed grey.",
     "The weight is a country's mood piece: post-apartheid cinema's biggest international handshake — the Foreign Language Film Oscar, a continent's story told with genre fluency, for better and for trade-offs the sequels to its success kept making. Watch it as performance study and watch the film around it more sceptically. Tsotsi remains the desk's entrance ramp to South African cinema: not its best, permanently its loudest.",
    ],
),
dict(
    slug="moolaade", title="Moolaadé", year=2004,
    director="Ousmane Sembène", country="Senegal / Burkina Faso", language="French / Dioula / Wolof",
    runtime=None, axes=dict(story=8.0, craft=8.0, vision=8.0, weight=10.0),
    score=8.5, date="2026-09-21",
    verdict="Asylum as a verb: the last Sembène turns a village dispute into a courtroom drama about who owns tradition — and lets the women hold the gavel.",
    body=[
     "A girl flees the knife; Collé shelters her and two others inside the compound, drawing the line of asylum — moolaadé — that tradition itself makes sacred, and the village spends a film's length discovering that the same custom it invokes can be turned against it. Sembène, in his eighties and working by his own design, builds a final-feature-calibre film as a legal thriller with no lawyers.",
     "The craft is deliberate plain-speak: compositions like testimony, radio as the village's parliament, a broadcast phone-in that lets the whole country argue about what the compound is doing. The performances are courtroom-calm — Maimouna Coulibaly's Collé does not emote, she cites; the men's outrage is played as stage-manageable in a way the film's argument is about: authority that needs noise is already losing.",
     "The story's architecture is its genius and its one visible seam: each act opens with an indictment delivered straight to camera — 'here is what a radio station does to you, here is what a tradition does to you' — as if the parable needed signposts. It does not mind; the signposts are the thesis, the film trusting an audience it is also convening.",
     "The weight: a film about female self-determination that ban-happers in its own country tried to strangle at the festival stage — and that won Cannes' Un Certain Regard prize anyway, then changed the vocabulary of a real legislative argument. No African film of its era does more with less; no review shelf on this desk may skip it.",
    ],
),

dict(
    slug="yeelen", title="Yeelen (Brightness)", year=1987,
    director="Souleymane Cissé", country="Mali", language="Bambara",
    runtime=None, axes=dict(story=7.0, craft=8.0, vision=10.0, weight=10.0),
    score=8.75, date="2026-09-22",
    verdict="The film that made world cinema treat African cinema as cinema: Cissé's creation-epic duel is a masterclass in severity, light and refusal to explain itself.",
    body=[
     "A sorcerer father hunts his son to death across the Bambara world to forestall a prophecy; the son, raised in exile, gathers the knowledge to return and finish the duel. Yeelen takes the creation mythology Malian audiences inherited orally and refuses every tourist accommodation: names are not glossed, rituals are not subtitled into meaning, the camera keeps its distance and lets the light do the argument. Four decades on, that refusal remains the most radical choice an African epic has made - the film trusts you to arrive at its level.",
     "The vision is untouchable. Cissé and his photographers compose the desert, the river and the final cave confrontation like scripture painted in hard sun and ember-dark; the restored print - the film's second life in the 2020s - proved how deliberate the palette always was: sand, indigo, copper, blood at the edges. Sound design works the same severity: chants placed like stones, silence where a festival crowd would expect a score.",
     "The craft walks a knife-edge a Western cast would fail: ritual acting risks ethnographic blankness in unfamiliar hands; Issiagu Barry and the company find instead a controlled grandeur, faces doing exposition the dialogue refuses. The final duel is staged as physics and fate at once - two men collapsing the world's balance with their own hands.",
     "Its weight is the entire shelf this desk sits on: the first sub-Saharan African feature to win Cannes' jury prize, the film that moved a continent's cinema from ethnography to art history. Every later Malian, Burkinabè and Nigerian epic negotiating budgets in Europe's offices cites the year Yeelen made it a line item. Watch it the way it demands: undistracted, unbothered by what you miss on the first pass - the balance reveals itself on the second, and it is brightness either way.",
    ],
),
dict(
    slug="supa-modo", title="Supa Modo", year=2018,
    director="Likarion Wainaina", country="Kenya", language="Swahili / Kikuyu / English",
    runtime=None, axes=dict(story=6.0, craft=8.0, vision=7.0, weight=9.0),
    score=7.5, date="2026-09-22",
    verdict="A village becomes a film school so a dying girl can become a superhero: sentimental in its premise, incorruptible in its practice.",
    body=[
     "Nine-year-old Jo is sent from the city hospital back to her grandmother's village - the family cannot afford the treatment, and everyone speaks around the fact by talking about a film instead. Jo, who has never stopped watching matatu-poster heroes, declares she is a superhero, and the village plays along so completely that it makes a movie for her before the ending comes. Supa Modo has the most dangerous premise in commercial cinema - childhood illness plus community warmth - and it survives only because its method is the opposite of exploitation.",
     "The method is the review: this was shot in the Kikuyu community that performs it, with non-professional neighbours who were trained on set as the story they tell is exactly that of neighbours building a film together. That double frame - a family acting out their own story while the film credits them as the collaborators they are - is what keeps the tears honest. The village's tin-roof cinematography glows by accident and by hour; the flying sequences, staged with rope, dust and total conviction, are the best child's-eye spectacle since the bicycle in E.T. - the whole movie is a make-believe that never asks you to stop believing.",
     "The story's concession is its third act: the disease's paperwork arrives when the film needs it, and a scene of hospital machinery explains a loss the film had earned the right to leave in grace. It is the only stretch where Supa Modo behaves like a campaign instead of a community - and it still has the nerve to end on flight.",
     "The weight: Kenya's Oscar submission in the Foreign Language Film year it won an audience prize circuit across two continents, and proof that a national film industry can be built from a village outward, with the skills left behind on set as the real export. For this desk's shelf, it sits where the canon needed a corner: cinema that treats its own audience's children as the crew.",
    ],
),
    dict(slug="october-1", title="October 1", year=2014,
         director="Kunle Afolayan", country="Nigeria", language="English", runtime=None,
         axes=dict(story=7.5, craft=8.0, vision=8.0, weight=8.5), score=8.0,
         date="2026-09-22",
         verdict="A murder in a colonial hotel becomes a nation holding its breath - period Nollywood with the nerve to be ambiguous",
         body=[
"Northern Nigeria, on the eve of independence, and the whole film happens in and around a hotel where the empire's last party is being arranged. A body appears; a constable from the village - honest, out of his depth - has to hold the line until the British hand over. It is a whodunit only in the way the best of them are: the mystery is a doorway into who gets to define order when the people defining it are leaving.",
"The period work is not decoration; it is the argument. Afolayan builds 1960 with the patience of someone who knows that independence is being staged as a hotel's menu, uniform and dance floor, and the cinematography lets the emptiness of those props speak. The constable's dilemma - law as an imported instrument he has genuinely come to respect - is the kind of paradox Nollywood thrillers had barely touched before, and still rarely touch as well.",
"What it risks, it mostly wins: the ending refuses the tidy case, the suspect list outlives its novelty deliberately, and the film trusts an audience to sit with an unresolved question about who the new nation is actually for. Where it drifts is in the middle - the hotel's subplots need the tightening the first and last acts have.",
"Weight, on this desk's scale, means what a film changed or proved possible: October 1 proved the industry's biggest budgets could aim at history and ambiguity instead of present-day spectacle, and it remains the standard the period-Nollywood attempts since have been measured against. Stream it for the craft, argue about the ending, keep the date in mind - the 1st of October is the joke and the thesis.",
         ]),
    dict(slug="gangs-of-lagos", title="Gangs of Lagos", year=2023,
         director="Jade Osiberu", country="Nigeria", language="English", runtime=None,
         axes=dict(story=7.5, craft=7.5, vision=7.5, weight=8.5), score=7.75,
         date="2026-09-23",
         verdict="Four friends, one campus and the cult of the 'arean' - the film that made the street epic fashionable again, and earned it",
         body=[
"The 1990s Lagos campus as the industry has never quite filmed it: not the comedic hustle, not the village morality play, but a period gang epic with a Greek tragedy's engine - boys in love with their own legend, a city that needs the legend more than they need it. Osiberu adapted Jikena Jones's novel with a producer's instinct for spectacle and a writer's patience for the slow turn from brotherhood to blood feud, and the result is the closest Nollywood has come to a genre crowd-film for a multiplex generation.",
"The craft is the argument: the '68-era costumes and yellow Mazda menace, the choreography of a crowd where every fist has a reason, and a cast - most of them new - who are directed to the frame rather than to the camera. The desk notes for the record that the period Lagos of this film is a stylised Lagos, a music-video memory of the streets; what the film does with the stylisation is the argument, not whether the paint was that bright.",
"The story pays for its spectacle unevenly: the middle loses a thread between the boys, the female characters exist mostly as consequence rather than cause, and the ending earns its grief while rushing the step that caused it. What it does at full power is the cult itself - the way a campus becomes a recruiting ground because nobody offers the boys a better story about themselves.",
"Weight is where this shelf keeps its scorecards honest, and here the ledger is simple: this film minted the 'street epic' cycle the industry chased for two years, proved the period-action genre could fill cinemas outside the comedy lane, and launched a cast whose names now headline slate announcements. A flawed genre piece that changed the slate is exactly what a five-axis scale exists to score - craft and weight up, story's loose middle down.",
         ]),
    dict(slug="93-days", title="93 Days", year=2016,
         director="Steve Gukas", country="Nigeria", language="English", runtime=None,
         axes=dict(story=7.0, craft=7.0, vision=7.5, weight=8.5), score=7.5,
         date="2026-09-23",
         verdict="The Ebola outbreak thriller that Nigeria needed before it knew it needed it - procedural, unshowy and all the braver for it",
         body=[
"July 2014: a traveller arrives in Lagos from Abidjan, already dying of Ebola, and the film follows the 93 days the city's containment took - not through a hero's arc but through contact lists, quarantines, a doctor who knew first and the machinery of a state deciding not to collapse. Gukas made the rare Nigerian film whose subject is competence, and made it thrilling by insisting on the paperwork.",
"The craft is procedural-clean: an ensemble pulled between the heroic and the bureaucratic, a script that trusts the timeline, and an honesty about Lagos's density that turns the city itself into the infection's best ally. What it cannot fully escape is the docudrama's pull - speeches arrive where scenes could have carried the same truth, and the villains are the ones the newsreels already provided.",
"The story's weakness is also its thesis: the drama here is that nobody gets a movie moment, because the outbreak was stopped by ordinary people doing the unglamorous thing at the right hour. The desk will take that trade once a year, at least; a Nigerian film that argues for public health systems instead of individual great men is doing something genre cinema rarely attempts.",
"Weight, unambiguously: 93 Days is the film Nigeria's Ebola response produced against all forecasts - the containment Lagos achieved became the WHO's case study, and this film is the country's own record of it, released while the memory was still a policy argument. Every subsequent outbreak film in the industry borrows its premise: that the thriller is in the contact list. That is a shelf entry for life.",
         ]),
    dict(slug="the-figurine", title="The Figurine", year=2009,
         director="Kunle Afolayan", country="Nigeria", language="English", runtime=None,
         axes=dict(story=7.5, craft=8.0, vision=8.0, weight=8.0), score=7.875,
         date="2026-09-24",
         verdict="The supernatural thriller that told the industry a Nigerian film could be dread - and dressed the dread like a museum piece",
         body=[
"A statue with an appetite, a village's curse, and a decade of grudges arriving in Lagos wearing European tailoring: The Figurine is what Nollywood's theatrical era sounded like when it decided to compete on atmosphere instead of exposition. Two couples, one archaeological crime, and a horror logic that the script trusts the audience to keep up with - a trust the industry spent years being denied.",
"The craft is where the landmark sits: the lighting treats shadow as a character, the Osun-state location work gives the curse geography, and the score - genuinely scored, with motifs - does the dread-doing that most contemporary videos left to jump-cut and scream. For a desk that catalogues this industry's production values like wine lists, 2009 is a vintage year because of this film's existence.",
"Held honestly to account: the mystery front-loads its clues and then asks for patience mid-film while the couples' subplots dilute the case, and the resolution prefers the supernatural's word over the detective's - a choice that reads as bold or as a dodge depending on the night. Neither charge ruins the rewatch; the dread keeps its appointment.",
"Weight decides this shelf's finals, and it is simple: every serious genre budget the industry has mounted since traces its green light to what The Figurine proved about cinemas taking a Nigerian supernatural film seriously, and about international platforms paying for one. It is not the best horror this desk has reviewed; it is the one that made the next ten possible, which on this scale is worth more.",
         ]),
    dict(slug="phone-swap", title="Phone Swap", year=2012,
         director="Kunle Afolayan", country="Nigeria", language="English", runtime=None,
         axes=dict(story=7.0, craft=6.5, vision=7.0, weight=7.0), score=6.875,
         date="2026-09-24",
         verdict="A princess, a mechanic and a swapped handset - the rom-com this industry needed before it needed awards",
         body=[
"The setup is a device from silent comedy - a spoiled influencer loses her phone, a village-adjacent mechanic finds it, and the identity swap that follows forces both to live one week in the other's SIM slot - and the film earns it by taking both lives seriously. The Lagos-versus-the-road contrast is the actual subject; the phone is the courier.",
"The craft is warm rather than showy: location sound that occasionally loses fights, a cut that trusts its comedy pairs, and a lead performance (Omotola as the princess forced to competence) that the desk would happily teach as the moment Nollywood rom-coms started being acted rather than delivered. The screenplay itself - a craft Nollywood rarely let be discussed before this film - is the desk's early, loud argument for treating writers as the production's first star.",
"What ages it, honestly: the middle's moral arithmetic - suffering as character education - resolves a privilege gap with a handshake, and the film would rather charm you than argue. It charms you anyway, which is the rom-com contract, and this one honours it better than most with bigger budgets did.",
"Weight, on this desk's ledger: Phone Swap is the proof that the comedy-of-class engine could fill cinemas outside the Yoruba-comedy lane, and its writer's next film - the one about a wedding - ran the playbook the industry still copies. Two shelf entries, one lineage; that is a film changing its market by being watchable, which is how taste moves.",
         ]),
    dict(slug="the-ceo", title="The CEO", year=2016,
         director="Kunle Afolayan", country="Nigeria", language="English", runtime=None,
         axes=dict(story=6.5, craft=7.0, vision=7.5, weight=6.0), score=6.75,
         date="2026-09-25",
         verdict="Lagos luxury as genre: the most commercial Afolayan is also the most contested - production design looking for a spine",
         body=[
"Six women at the top of a city, one fashion house as the hinge, and a camera budget that never once admits it is Nigerian cinema trying: The CEO is what the industry's theatrical era commissioned when a director with the figurine-and-swap pedigree decided glamour itself was a subject worth the price of the frame. It is a film about competence under scrutiny, dressed so beautifully that the argument about whether it has a script almost misses the point - almost.",
"The craft is the thesis. The lighting design treats Victoria Island at night like a set built for desire rather than a location endured, the wardrobe department is doing actual character work, and the ensemble is directed to talk over each other the way boardrooms do - the desk files this among the first Nigerian films where the rich scenes feel observed rather than aspirational. Where the machinery strains is in the connective tissue: four or five mini-arcs competing for two hours means grief arrives by memo in places where the film should have sat down and let it happen.",
"Held honestly to account: the brand weight is real - this is a film that flirts with being a long advertisement for a lifestyle, and one subplot in particular resolves on a handshake and a sunset where the writing owed an accounting. The desk also refuses to pretend the third act's sudden legal-thread convenience is anything but a shortcut. And yet the ambition is its own evidence: a Nigerian film that could only exist because its director's last two had proven cinemas would pay for polish, and the polish is here even when the plot is not.",
"Weight, on this shelf's ledger, is measured in what a film makes possible rather than what it achieves, and The CEO's entry is double-edged: it proved the luxury multi-hander could be financed and exported to streaming shelves worldwide, and it also showed exactly how far an ensemble can be designed before it is dramatised. The desk's number is generous to the first fact and stern to the second; the streaming afterlife belongs to the first. Watch it as the industry's costume fitting for the premium era - and grade it, kindly, on whether the play arrived after.",
         ]),
    dict(slug="76", title="76", year=2016,
         director="Izu Ojukwu", country="Nigeria", language="English / Hausa / Igbo", runtime=None,
         axes=dict(story=7.5, craft=7.5, vision=7.5, weight=9.0), score=7.875,
         date="2026-09-25",
         verdict="The coup the classrooms skipped, restored as a love story under arrest - and Nigerian cinema's first honest argument with its own history",
         body=[
"A young soldier home on leave two days before his wedding, a headmaster's daughter with a teaching post and a mind of her own, and the January night in 1966 when the country's first republic ended in gunfire and every file since became political: 76 takes the event Nigerian history teaching handled in whispers and tells it from inside a household, from the end of the queue where the accusation lands on whoever happens to be standing nearest. It is a love story that the state keeps interrupting, and the interruptions are the point.",
"The craft is period-obliged, and the film pays the obligation seriously - the costumes carry creases instead of prestige, the radios, the barracks, the hand-written detention orders all read researched rather than rented, and the editing keeps the dread at walking pace where a lesser film would have run. The desk's standing praise is for restraint: the accused gets no speech for the jury, the investigator gets no cartoon, and the girl at the gate waiting for a visitor's pass is given scenes that trust silence to carry what dialogue would cheapen.",
"The film's central bargain - history through a romance, politics through paperwork - is also where the desk enters its caveat: a mid-film stretch of procedure wants a second edit, and the final act asks the audience to accept an intervention that the earlier scene-work had carefully ruled out. Neither flaw breaks the spell; both are visible enough that this desk will not pretend otherwise. What the film never lets go is its nerve about archives - the sense that a nation's story is mostly what the surviving documents refuse to say.",
"Weight decides the finals on this shelf and 76's is simple to state: before it, the first republic's end was a topic Nigerian cinema handled through allegory or ignored; after it, a whole generation's entry point to 1966 is a film two of them cried in, and the historiography argument it started has not finished running in the country's newspapers. Judged as cinema it is very good; judged as the moment a film industry agreed its own past was worth the research, it is a landmark - which is exactly the arithmetic that puts it on this shelf at this number.",
         ]),

    dict(slug="isoken", title="Isoken", year=2017,
         director="Jadesola Osiberu", country="Nigeria", language="English", runtime=None,
         axes=dict(story=7.0, craft=7.0, vision=7.0, weight=6.5), score=6.875,
         date="2026-09-26",
         verdict="The rom-com that made a title a thesis: a princess who refuses the crown of the wedding industry, played at a full human tempo",
         body=[
"A young Edo woman who has spent a lifetime being addressed as royalty by strangers and being scheduled for marriage by relatives goes home for a family wedding with one refusal on her lips - the desk calls this the most quietly radical premise the Nigerian rom-com produced in its streaming decade: the rebellion is not against the groom candidates, it is against the noun. The princess problem is that the title is a leash, and the film takes the leash seriously while keeping its comedy light.",
"The craft is warm precision: the family compound scenes are blocked like actual families - everyone talking, nobody waiting their turn - the dialogue carries the bilingual music of Benin City drawing-room English, and the leads sell romance as negotiation rather than destiny, which is the harder trick. The direction's signature is restraint at the moments a lesser film would swell the score; this desk files the funerals and the family conferences among the best-directed scenes in the shelf's modern wing.",
"Entered honestly against the ledger: the third act buys the convention it spent two hours dodging - the grand gesture arrives on schedule, and the family subplots resolve a little faster than their messes allowed. The film's Lagos-side fashion gloss also thins its texture next to the Benin sequences, where it is most itself. None of this is fatal; a rom-com is judged by whether the couple earns the close, and these two mostly do.",
"Weight on this shelf is the industry's own memory, and Isoken's entry is real in two directions: it proved the mid-budget romantic comedy could travel the world through streaming shelves and carry a specifically Nigerian - specifically Edo - cultural argument doing it, and it made 'the princess' a running phrase in the country's comedy about what families do to their successful daughters. Judged as a film, a good one with a rushed ending; judged as a moment, the one that let a hundred lighter films argue with nouns after it.",
         ]),
    dict(slug="the-black-book", title="The Black Book", year=2023,
         director="Editi Effiong", country="Nigeria", language="English", runtime=None,
         axes=dict(story=6.5, craft=7.0, vision=7.5, weight=6.0), score=6.75,
         date="2026-09-26",
         verdict="A grief thriller with a thesis stapled to it: the system is not broken, it was built this way - and the film trusts its working-class ensemble more than its own plot does",
         body=[
"A teenager's life ends in a compound with gates, money moves through the machinery of police files and court papers, and a mother with money and a father with access discover the difference between grieving and prosecuting. The Black Book opens as a revenge thriller and keeps interrupting itself with the quieter, angrier observation that revenge would require a system capable of being satisfied - the desk's shorthand for the whole film: a heist plot in service of an audit of who the country's laws protect.",
"The craft is the film's strongest argument. The camera treats Lagos as architecture - power corridors photographed as corridors, the courts as a building where cruelty is procedural rather than personal - and the direction's best decision is the tonal casting of the ensemble: the fixers, drivers and beauticians who carry the second half are played with a working-day realism that keeps the thriller from becoming cosplay. The writing around them - the film's actual engine room - is where this desk would put the grade: the plan is assembled like a community, and the community is shot like it means it.",
"The ledger's debits belong to the first half: the thriller scaffolding leans on reveals the audience is allowed to see coming, and the pivot from procedural grief to vigilante operation asks more coincidence than the story's realism can afford. There is also a temptation, in a film about bought justice, to let its own villains be bought too cheaply - a few cardboard turns that its leads' committed faces cannot quite sell. The film survives its shortcuts because it never sells the mother's grief as a genre beat; that spine is straight even when the plot bends.",
"Weight, measured as what a film moved: The Black Book became the country's loudest argument that its crime thrillers are one long case file on impunity - critics, lawyers and the phrase 'black book' entered the street's vocabulary for the ledger of purchased files, and its global streaming debut made that vocabulary everyone's. Judged as cinema, a gripping second-half film; as a document of a national mood in 2023, the shelf's most quotable entry in years, which is precisely the kind of weight this desk keeps a column for.",
         ]),

    dict(slug="lionheart", title="Lionheart", year=2018,
         director="Genevieve Nnaji", country="Nigeria", language="English / Igbo", runtime=None,
         axes=dict(story=6.5, craft=6.5, vision=6.0, weight=7.5), score=6.625,
         date="2026-09-27",
         verdict="A corporate succession comedy shot in family colours: the film's real plot was the argument it started about what a foreign-language film is",
         body=[
"The eldest daughter of a shipping magnate, a stroke that hands her the company mid-fight, a brother waiting in the wings and a father who conducts half of his life in Igbo: on paper Lionheart is a comedy of corporate succession dressed in Lagos tailoring, and it plays that way - competently, warmly, a little safely. Its actual historical subject was waiting outside the frame, in the fine print of an awards rulebook.",
"The craft is solid television-grade raised a class by its lead: blocking that keeps family scenes in the same room instead of cross-cutting them, an office comedy rhythm that mostly trusts its silences, and a physical, lived-in warehouse world that the desk files as the film's best design choice - a shipping company shot as a working body, not a set. The score and cut never embarrass themselves; nor do they reach for the one register, risk, that would make the middle hour unforgettable rather than agreeable.",
"The ledger's debits are the script's: the antagonist is a scheduling problem, the resolution arrives wearing a family-unity speech, and the business-logic of the succession would not survive a board meeting. Held honestly: this is a film that likes its characters more than it challenges them, which is a valid genre contract - the desk simply refuses to grade it as if the contract were bold.",
"Weight is where Lionheart vaults its own shelf position. As the first Netflix original from its country's industry it changed what a platform deal meant for the slate economics here, and its exclusion from a foreign-language race on the technicality of its English submission rules had the industry, the diaspora and the rulebook's owners arguing in public about what a 'foreign-language' film from a multilingual country even is. Films are judged by what they do on screen; this one is also remembered for what it did to a form - and on this desk's ledger, that Igbo argument at the edge of the frame outlived most of the plot inside it.",
         ]),
    dict(slug="eyimofe", title="Eyimofe (This Is My Desire)", year=2020,
         director="Arie & Chuko Esiri", country="Nigeria", language="English / Igbo", runtime=None,
         axes=dict(story=7.5, craft=8.5, vision=8.0, weight=7.5), score=7.875,
         date="2026-09-27",
         verdict="Two lives, one departure economy, and a Lagos shot like evidence: the self-financed debut that out-classed the industry's funded productions on their own turf",
         body=[
"A welder keeping two women's households alive across a city he cannot afford; a hairdresser whose passport queue is the only door she can see - Eyimofe follows the economics of going anywhere else as a day-by-day grind rather than a montage, and its title's desire is priced in ferry tickets, hospital bills and funeral money. The desk has reviewed this industry's migration stories for years; almost none of them had a script this patient or a camera this unwilling to look away.",
"The craft is the debut that embarrassed budgets twice its size: framing that composes Lagos like a witness statement rather than a postcard, sound design that keeps the city at working distance, and performances conducted at the volume of people who cannot afford drama in public. The decision to shoot on film stock in a market that had digitised everything reads on screen as seriousness - grain as a moral choice, a period the industry was not asked to look at this closely before.",
"Entered honestly: the two strands share a city and a theme but not equal gravity - the desk finds the second movement slightly the stronger, and a final image or two reaches for poetry where the film's own evidence had already made the point. The film also asks patience of audiences trained on the industry's faster emotional commerce; that patience is some of its argument, but this page does not pretend it is free.",
"Weight: a self-financed first feature that premiered at a major international festival in early 2020, then swept that season's national industry awards, and rewrote what debut financing could mean - the desk's shorthand is the sentence producers now hear in every pitch meeting: if the Esiri brothers could do it with their own money, whose money is the excuse? As a document of the departure economy it joins the shelf's essential pair with 76 - one film recovering a nation's buried past, this one recording its present leaving by sea.",
         ]),

]

REVIEWS_BY_SLUG = {r["slug"]: r for r in REVIEWS}


def review_score_str(rv):
    return str(rv["score"]) if rv["score"] % 1 else str(int(rv["score"]))


def backfill_card(movies):
    """Give catalogue cards a score when a real desk review supplies one."""
    fixed = 0
    for m in movies:
        if m.get("score") is None and m.get("slug") in REVIEWS_BY_SLUG:
            _sc0 = REVIEWS_BY_SLUG[m["slug"]]["score"]
            m["score"] = int(_sc0) if _sc0 % 1 == 0 else _sc0
            fixed += 1
    return fixed
