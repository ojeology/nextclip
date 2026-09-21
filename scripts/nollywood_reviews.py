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
