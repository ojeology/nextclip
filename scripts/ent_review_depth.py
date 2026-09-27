# -*- coding: utf-8 -*-
"""Per-review depth sections (Phase 3 tranche 4): context + verifiable-record links.
Every section is bespoke to the film; links are deterministic lookup URLs (IMDb find,
TMDb search, Wikipedia search) - never fabricated deep links."""

_IMDB = "https://www.imdb.com/find/?q=%s&s=tt"
_TMDB = "https://www.themoviedb.org/search?query=%s"
_WIKI = "https://en.wikipedia.org/wiki/Special:Search?search=%s"


def _lk(imdb_q, tmdb_q, wiki_q):
    return (_IMDB % imdb_q, _TMDB % tmdb_q, _WIKI % wiki_q)


def _sec(h2, angle, verify_label, links, extra=""):
    a, t, w = links
    return ('<h2>' + h2 + '</h2>'
            + '<p>' + angle + '</p>'
            + (('<p>' + extra + '</p>') if extra else '')
            + '<p>' + verify_label + ' the credits on <a href="' + a + '" rel="noopener">IMDb</a>, '
            + 'the cast and runtime on <a href="' + t + '" rel="noopener">TMDb</a>, and the '
            + 'production and reception history on <a href="' + w + '" rel="noopener">Wikipedia</a>.</p>')


REVIEW_DEPTH = {

"tsotsi": _sec("Athol Fugard, the townships, and an Oscar",
 "Gavin Hood adapted the only novel Athol Fugard ever wrote, moved it to a Johannesburg that feels both specific and placeless, and let Presley Chweneyagae carry nearly the whole film in his face. In 2006 it became the first South African film to win the Academy Award for Best Foreign Language Film \u2014 the fact most international viewers know it by, and the least interesting thing about it. The desk\u2019s 7.25 reflects a film whose craft is undeniable and whose arc is, arguably, a touch too neat for the world it depicts.",
 "The desk\u2019s facts can be checked against",
 _lk("Tsotsi%202005", "Tsotsi", "Tsotsi")),

"phone-swap": _sec("A high-concept comedy that Nollywood rarely attempts",
 "Single-concept comedies live or die on execution, and Kunle Afolayan\u2019s Phone Swap hangs everything on one switched phone and two lives that refuse to untangle. It is the lightest film on the director\u2019s shelf \u2014 no colonial mysteries, no figurines \u2014 which is exactly why it is a useful data point: it shows the same craftsman\u2019s discipline applied to farce rather than dread. The 6.875 is the sound of solid craft serving modest material.",
 "Cross-check the details against",
 _lk("Phone%20Swap%202012", "Phone%20Swap", "Phone%20Swap")),

"moolaade": _sec("Semb\u00e8ne\u2019s last statement, and a bell that still rings",
 "Ousmane Semb\u00e8ne, the father of African cinema, ended his feature career with this 2004 film about women in a Bambara village using a ancient shelter custom \u2014 the moolaad\u00e9 \u2014 to protect girls from ritual purification. It won the top prize at Cannes\u2019 Un Certain Regard, and its final image may be the most hopeful in the director\u2019s whole body of work. The desk\u2019s 8.5 puts it in the company of the best films any continent produced that decade.",
 "Check the record at",
 _lk("Moolaad%C3%A9", "Moolaad%C3%A9", "Moolaad%C3%A9")),

"the-figurine": _sec("The film that reset the conversation",
 "Before The Figurine, the industry story was that ambitious, cinema-grade Nollywood was a rumour. Kunle Afolayan\u2019s 2009 folk-horror-tinged drama about friendship, a covenant and a wooden figure that grants fortune at a price became the argument-settler, touring festivals and putting its director\u2019s name on the map. Nearly every ambitious Nigerian film since has been measured against it \u2014 the desk\u2019s 7.875 measures it on its own axes.",
 "Verify the credits at",
 _lk("The%20Figurine", "The%20Figurine", "The%20Figurine%20(film)")),

"the-figure": _sec("A new director\u2019s name worth learning",
 "The Figure arrived in 2023 with little of the marketing machinery behind the year\u2019s big titles, which is precisely why the desk picked it up: the shelf exists to judge films on craft, not on campaign budgets. The entry credits are sparse across databases too \u2014 one more reason to check them directly rather than trust aggregator summaries. On the desk\u2019s axes it lands at 6.25: real intention, uneven execution.",
 "The sparse credits can be checked at",
 _lk("The%20Figure%202023", "The%20Figure%202023", "The%20Figure%202023")),

"timbuktu": _sec("Occupation without a single wasted frame",
 "Abderrahmane Sissako\u2019s Timbuktu is that rare film about jihadists that refuses them the movie: the camera keeps drifting to the ordinary people living absurd, defiant lives under an occupation \u2014 the herder, the singer, the boy footballing without a ball. It was Mauritania\u2019s first Academy Award nominee and competed at Cannes in 2014. The desk\u2019s 8.75, the joint-highest on this shelf, is the review the editor still rereads when the news makes the film feel more documentary than drama.",
 "Every fact here is checkable at",
 _lk("Timbuktu%202014", "Timbuktu%202014", "Timbuktu%20(film)")),

"atlantics": _sec("A debut that changed what a first film could be",
 "Mati Diop became the first Black woman to direct a film in Cannes\u2019 main competition, and Atlantics left the 2019 festival with the Grand Prix: a Dakar love story told through the girls and the women left behind, with a supernatural turn that feels less like a genre move than a tide coming in. The desk\u2019s 8.0 argues the film\u2019s patience is its power, not its flaw.",
 "Check the festival record at",
 _lk("Atlantics%202019", "Atlantics%202019", "Atlantics%20(film)")),

"glamour-girls": _sec("The early video era\u2019s sharpest mirror",
 "Glamour Girls (1994) belongs to the stretch when Nollywood was inventing itself on home video, and few films from that wave look at money, respectability and women\u2019s options in Lagos with this much unblinking directness. Watching it now is a double experience: the craft of the era (feasible schedules, direct sound, daylight lighting) and a social argument that mainstream capitalism-glamour cinema still mostly avoids. The desk\u2019s 6.5 prices in the era\u2019s limits; the writing has aged better than its production values.",
 "The era\u2019s credits are checkable at",
 _lk("Glamour%20Girls%201994", "Glamour%20Girls", "Glamour%20Girls%20film")),

"half-of-a-yellow-sun": _sec("From page to screen, with the war intact",
 "Biyi Bandele\u2019s adaptation of Chimamanda Ngozi Adichie\u2019s novel took on the Biafran story through a family that history keeps interrupting, and the production\u2019s very existence \u2014 a Biafra narrative with this budget and these faces \u2014 mattered as much as its execution. The desk\u2019s 6.25 records where the compression of a 450-page novel into feature length bites hardest; the novel remains the deeper cut, and the film is a companion, not a replacement.",
 "Compare book and film records at",
 _lk("Half%20of%20a%20Yellow%20Sun%20film", "Half%20of%20a%20Yellow%20Sun", "Half%20of%20a%20Yellow%20Sun%20(film)")),

"anikulapo": _sec("Folklore, a ram\u2019s folly, and Netflix\u2019s biggest Nollywood bet",
 "Kunle Afolayan\u2019s An\u00edk\u00fal\u00e1p\u00f3 adapts Yoruba folk material \u2014 a dying man, a mystical bird, an affair that topples a household \u2014 into the kind of epic the streaming era made possible at scale: hundreds of extras, real locations, a language-first cast. It became one of Netflix\u2019s most-watched Nigerian titles, and its proverb-heavy script rewards viewers who let the Yoruba land without hurrying to the subtitles. The desk\u2019s 7.5 balances spectacle against a second act that repeats its lesson.",
 "Verify language and credits at",
 _lk("An%C3%ADk%C3%BAl%C3%A1p%C3%B3", "An%C3%ADk%C3%BAl%C3%A1p%C3%B3", "An%C3%ADk\u00fal\u00e1p\u00f3")),

"october-1": _sec("Colonial Nigeria as a crime scene",
 "October 1 sets a murder investigation in the September days before Nigerian independence in 1960, and uses the countdown the way thrillers use ticking clocks: every flag being sewn, every oath being rehearsed, sits one room away from something rotten. Kunle Afolayan\u2019s craft-first approach \u2014 period design, restrained performances \u2014 earns the desk\u2019s 8.0, one of the shelf\u2019s highest marks and a standing recommendation for viewers who think period Nollywood begins and ends with costume parties.",
 "The 1960 context and credits at",
 _lk("October%201%20film", "October%201%20movie", "October%201%20(film)")),

"mami-wata": _sec("Black-and-white folklore on the festival route",
 "C.J. \u2019Fiyo\u2019 Obasi shot MamiWata in striking monochrome, built a village fable around the water-spirit myth, and took it to Sundance\u2019s World Cinema competition \u2014 a Nigerian genre film travelling that route on its own visual terms. The desk\u2019s 7.75 rewards the boldness of the images and the folk-tale economy of the storytelling, while noting where the allegory announces itself.",
 "Check the festival run at",
 _lk("Mami%20Wata%202023", "Mami%20Wata", "Mami%20Wata%20(film)")),

"the-wedding-party": _sec("The record-breaking party, revisited",
 "The Wedding Party is the film the industry measures box-office eras by: a 2016 ensemble comedy from the ELFIKE collective\u2019s producing partnership that turned Lagos wedding chaos into historic ticket sales. What the desk\u2019s 7.0 argues is that its craft case rests on one genuinely excellent thing \u2014 an ensemble comedy rhythm that Nollywood studio comedy still copies \u2014 while the script coasts on charm in its final act.",
 "Verify the box-office era at",
 _lk("The%20Wedding%20Party%202016", "The%20Wedding%20Party%202016", "The%20Wedding%20Party%20(film)")),

"king-of-boys": _sec("Eniola Salami and the grammar of Nigerian power",
 "Kemi Adetiba\u2019s King of Boys gave Nollywood its proper crime epic: three hours of electoral muscle, generational grief and Sola Sobowale\u2019s towering performance as Eniola Salami. It spawned a Netflix-cut sequel and cemented the director as the shelf\u2019s most-watched working filmmaker. The desk\u2019s 8.0 still holds: the ambition is fully earned, the middle hour fully subscribed to genre conventions the first and last hours transcend.",
 "Check the franchise record at",
 _lk("King%20of%20Boys%202018", "King%20of%20Boys", "King%20of%20Boys")),

"yeelen": _sec("The Mand\u00e9 epic that opened Cannes\u2019 doors",
 "Souleymane Ciss\u00e9\u2019s Yeelen (1987) \u2014 a father-son sorcery odyssey drawn from Mand\u00e9 oral tradition \u2014 was the first African film to compete for the Palme d\u2019Or, and it won the Cannes Jury Prize. Everything the festival world later celebrated in African fantasy cinema has a ancestor frame somewhere in this film. The desk\u2019s 8.75 scores it as the timeless object it is; the restoration-era prints now circulating are the best argument for film preservation there is.",
 "Check the 1987 record at",
 _lk("Yeelen", "Yeelen", "Yeelen")),

"gangs-of-lagos": _sec("Streaming-era Lagos, with history in the wardrobe",
 "Jade Osiberu\u2019s Gangs of Lagos arrived as a Prime Video original and gave the streaming era its first big Nollywood crime saga \u2014 Eyo masquerade regalia, Onîdo gang lore and all. The desk\u2019s 7.75 notes what the streaming budget fixed (production value, night scenes, crowd work) and what it did not (a third act that mistakes volume for escalation).",
 "The Lagos lore is checkable at",
 _lk("Gangs%20of%20Lagos", "Gangs%20of%20Lagos", "Gangs%20of%20Lagos")),

"oloture": _sec("Undercover journalism, honestly ugly",
 "Kenneth Gyang\u2019s \u00d2l\u00f2t\u016br\u00e9 follows a Lagos reporter into the trafficking economy she is investigating, and it keeps faith with how grim that terrain actually is \u2014 no rescue-arc comfort, an ending that refuses to wave. Produced by EbonyLife for Netflix, it announced the streamer era\u2019s appetite for Nigerian social realism. The desk\u2019s 7.375 credits the film\u2019s nerve and Sharon Ooja\u2019s lead performance while flagging the side characters the script leaves as furniture.",
 "Check the credits (director, writers, year) at",
 _lk("Oloture", "Oloture", "Oloture")),
"supa-modo": _sec("A Kenya superhero story with small stakes and a huge heart",
 "Likarion Wainaina\u2019s Supa Modo gives a terminally ill Kenyan girl the superhero movie her village stages around her \u2014 and finds the rare register where the fantasy never lies to the child or the audience. It premiered in the Berlinale\u2019s Generation strand and travelled the festival circuit collecting audience awards. The desk\u2019s 7.5 holds that its restraint is the craft: the film earns every tear it never begs for.",
 "Check the Berlinale record at",
 _lk("Supa%20Modo", "Supa%20Modo", "Supa%20Modo")),
"isoken": _sec("The wedding-movie family, minus the wedding",
 "Jade Osiberu\u2019s Isoken takes the Nollywood family-gathering machine and points it at a single question \u2014 what a 34-year-old Lagos woman is allowed to want \u2014 with Dakore Akande holding the centre. The desk\u2019s 6.875 prices the film as classy convention: polished, warm, and a touch afraid of the sharper ending its own premise points toward.",
 "Cast and credits are checkable at",
 _lk("Isoken", "Isoken", "Isoken")),
"citation": _sec("The campus trial film Nollywood had not made",
 "Kunle Afolayan\u2019s Citation takes a university sexual-harassment case through a formal academic hearing, which is both its subject and its method: procedure as drama. Moremi Ojudu\u2019s performance carries the silence the story is about. The desk\u2019s 6.875 notes where the film\u2019s gloss softens its own sharpest edges \u2014 and why it remains a useful film to assign, not just watch.",
 "Verify the production details at",
 _lk("Citation%202020", "Citation%202020", "Citation%20(film)")),
"lionheart": _sec("The first submission, and the rule that disqualified it",
 "Genevieve Nnaji\u2019s directorial debut Lionheart became Nigeria\u2019s first Academy Award submission \u2014 and then the case study in the Academy\u2019s language rules, disqualified for an English-heavy soundtrack in the International category. The film itself is a gentler boardroom inheritance drama than its reputation: the desk\u2019s 6.625 separates the milestone (real, historic) from the movie (solid, modest).",
 "The Academy saga is documented at",
 _lk("Lionheart%202018", "Lionheart%202018", "Lionheart%20(film)")),
"namaste-wahala": _sec("The Nigeria-India rom-com experiment",
 "Hamisha Daryani Ahuja\u2019s Namaste Wahala braided Nigerian and Indian family comedy into one Lagos wedding plot for Netflix, and its global streaming numbers outpaced its reviews everywhere. The desk\u2019s 6.5 is kind about the swing and firm about the miss: the cultures deserve a better bridge than the script builds \u2014 and the film\u2019s success guarantees someone will build it.",
 "Check the credits and reception at",
 _lk("Namaste%20Wahala", "Namaste%20Wahala", "Namaste%20Wahala")),
"eyimofe": _sec("35mm, two dreams, one bus fare",
 "The Esiri brothers\u2019 Eyimofe (This Is My Desire) is Lagos neorealism: two working people, one Spain-shaped dream each, and a city that charges them for every step. Shot on 35mm and premiered at the Berlinale in 2020, it looks like nothing else in the contemporary Nigerian field \u2014 the desk\u2019s 7.875 argues it is the shelf\u2019s quiet masterclass in patience.",
 "Check the Berlinale credits at",
 _lk("Eyimofe", "Eyimofe", "Eyimofe")),
"jagun-jagun": _sec("The warrior epic, correctly credited",
 "Jagun Jagun (The Warrior) was produced by Femi Adebayo\u2019s Euphoria360 and directed by Adebayo Tijani and Tope Adebayo Salami \u2014 a credit line worth stating precisely, because the film\u2019s scale (a warlord\u2019s army, digital battlefields, Netflix reach) invited plenty of loose talk. It followed the same team\u2019s King of Thieves and took AMVCA and AMAA honours for costume, makeup and visual effects. The desk\u2019s 7.0 weighs the ambition against a villain whose menace does more work than the script does.",
 "The correct credit chain is verifiable at",
 _lk("Jagun%20Jagun", "Jagun%20Jagun", "Jagun%20Jagun")),
"living-in-bondage": _sec("Where the home-video era begins",
 "Living in Bondage (1992) is the industry\u2019s big bang: the Igbo-language video film whose success \u2014 and whose ritual-wealth morality tale \u2014 turned a Lagos idlers\u2019 market into an industry. The desk reviews it as history that still plays: every Nollywood occult thriller since is negotiating with this film\u2019s grammar. The 6.5 is a score for the craft of 1992, judged with 1992\u2019s means in view.",
 "Check the founding record at",
 _lk("Living%20in%20Bondage", "Living%20in%20Bondage", "Living%20in%20Bondage%3A%20Setting%20Free")),
"felcite": _sec("Music as survival, priced in Congolese francs",
 "Alain Gomis\u2019s F\u00e9licit\u00e9 follows a Kinshasa bar singer through a son\u2019s accident and the economy of getting him fixed, cutting between the blues of the everyday and sudden dream sequences that rearrange the film\u2019s logic. It won the Jury Grand Prix at the Berlinale in 2017. The desk\u2019s 7.75 scores its energy honestly: exhilitating, and knowingly rough at the seams.",
 "Check the Berlinale record at",
 _lk("F%C3%A9licit%C3%A9", "F%C3%A9licit%C3%A9", "F%C3%A9licit%C3%A9%20(film)")),
"something-necessary": _sec("Kenya after the violence, at kitchen-table range",
 "Judy Kibinge\u2019s Something Necessary pairs a woman rebuilding after the 2007-08 post-election violence with the young man whose choices broke her home, and lets national trauma play out entirely at personal scale. The desk\u2019s 7.25 values the film as one of the clearest statements of Kenya\u2019s one-film-one-wound school of filmmaking.",
 "The context is checkable at",
 _lk("Something%20Necessary", "Something%20Necessary", "Something%20Necessary")),
"the-ceo": _sec("A boardroom thriller at 30,000 feet",
 "The CEO assembles five corporate candidates on a flight and lets Kunle Afolayan run a locked-room premise at altitude \u2014 a Nollywood first for the setup, and a film whose idea still outruns its execution. The desk\u2019s 6.75 is the honest ledger: a genuinely clever frame, characters introduced by job title, and a twist the film undercuts itself.",
 "Credits and cast are at",
 _lk("The%20CEO%202016", "The%20CEO%202016", "The%20CEO%20(film)")),
"76": _sec("The coup year, remembered from the wives\u2019 side",
 "Izu Ojukwu\u2019s 76 builds its military-coup drama around a soldier\u2019s wife waiting, which keeps the 1976 DG-episode history at human scale: checkpoints, rumours, a photograph that becomes evidence. The desk\u2019s 7.875 places it among the shelf\u2019s best-directed period work, and its patience is the point.",
 "The 1976 context and credits at",
 _lk("76%20film%202016", "76%20movie", "76%20(film)")),
"the-black-book": _sec("Netflix\u2019s Nigerian thriller record-setter",
 "Editi Effiong\u2019s The Black Book put a grieving professor against the machinery of the state and briefly became the most-watched Nigerian title of its season on Netflix globally \u2014 a distribution milestone the desk records without letting it inflate the review. The 6.75 splits the difference: action-first craft, a conspiracy plot that explains less than it shows.",
 "Check the release record at",
 _lk("The%20Black%20Book%202023", "The%20Black%20Book%202023", "The%20Black%20Book%20(film)")),
"nneka-the-pretty-serpent": _sec("A remake\u2019s debt to 1994",
 "This 2020 Nneka the Pretty Serpent reworks the video-era cult favourite for the streaming age, with Tosin Igho\u2019s production moving the witchcraft office from Lagos socialites to a glossier conspiracy register. The desk\u2019s 6.0 \u2014 among the shelf\u2019s lowest recent marks \u2014 argues the remake borrows the title\u2019s power before earning its own.",
 "Compare with the original\u2019s record at",
 _lk("Nneka%20the%20Pretty%20Serpent", "Nneka%20the%20Pretty%20Serpent", "Nneka%20the%20Pretty%20Serpent")),
"shadow-parties": _sec("Politics as blood sport, in miniature",
 "Shadow Parties (2021) takes the local-government war film \u2014 political thugs, patron networks, a town that pays \u2014 and tells it at a budget that shows. The desk\u2019s 6.25 is a fair price for conviction: the film\u2019s anger is real, its staging modest, and its best scenes come from actors outrunning the production around them.",
 "Check the credits at",
 _lk("Shadow%20Parties", "Shadow%20Parties", "Shadow%20Parties")),
"mokalik": _sec("A day among the mechanics, seen low to the ground",
 "Kunle Afolayan\u2019s Mokalik hides its premise in plain sight: an eleven-year-old spends a day as an apprentice in a Lagos motor workshop, and the film studies the informal economy\u2019s whole curriculum \u2014 hierarchy, hustle, expertise \u2014 from a child\u2019s eye line. The desk\u2019s 7.0 calls it the director\u2019s quietest film and, scene for scene, his most observant.",
 "Credits and language details at",
 _lk("Mokalik", "Mokalik", "Mokalik")),
"the-set-up": _sec("Heist mechanics, Lagos paperwork",
 "Niyi Akinmolayan\u2019s The Set Up runs a con at business-class altitude \u2014 forged signatures, inheritance plots, executives who deserve each other \u2014 and dresses the genre in genuine Lagos specificity. The desk\u2019s 6.25 finds the pieces better than the pattern: style to spare, plot to spare, and a reveal the first act already spent.",
 "Verify the production record at",
 _lk("The%20Set%20Up%202019", "The%20Set%20Up%202019", "The%20Set%20Up%20(film)")),
"the-meeting": _sec("Abuja bureaucracy as romantic obstacle",
 "Mildred Okwo\u2019s The Meeting sends a junior executive into the ministry waiting room from hell and lets Rita Dominic\u2019s receptionist run the satire \u2014 a near-perfect single-location comedy of Nigerian officialdom with a romance folded quietly inside. The desk\u2019s 7.75 has aged well: a decade on, the queue has only grown funnier and sadder.",
 "Cast and credits checkable at",
 _lk("The%20Meeting%202012", "The%20Meeting%202012", "The%20Meeting%20(film)")),
"thirty-days-in-atlanta": _sec("The comedy whose numbers started the argument",
 "30 Days in Atlanta (2014), AY Makun\u2019s transatlantic culture-clash comedy, became one of the highest-grossing Nollywood films of its moment \u2014 a box-office fact that says more about the market than the movie, as the desk\u2019s 6.0 argues at length. As cinema: broad, game, occasionally very funny; as a data point in Nollywood\u2019s commercial history: essential.",
 "Check the box-office era at",
 _lk("30%20Days%20in%20Atlanta", "30%20Days%20in%20Atlanta", "30%20Days%20in%20Atlanta")),

}
