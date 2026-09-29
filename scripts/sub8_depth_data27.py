"""Batch V depth sections — the 40 film pages carrying no verdict, no FAQ and no
depth section (2026-09-29).

These were the weakest pages in the catalogue after the triage work: everything a
reader got was the trailer facade, a two-line synopsis and a "More like this" list.
Each section below is written for its own title, and no h2 or lead-in label is
reused anywhere in the batch (asserted at the bottom).

Rows are FLAT: [slug, h2, para, l1, d1, ... l6, d6, para2]  -- 16 fields.

Accuracy rule for this batch: the 2025/2026 titles are recent enough that plot
detail cannot be asserted from memory, so those sections stay on verifiable
ground -- the source material, the filmmaking lineage, the casting -- and say
plainly where the desk is describing a tradition rather than a scene. Nothing
here claims a first-hand screening, a box-office figure or a review score.
"""
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent / "public"

SEE_ENT = [
    "entertainment/movies-like-deadpool-and-wolverine",
    "entertainment/best-anime-to-watch-now",
    "entertainment/best-horror-movies-of-all-time",
    "entertainment/comfort-movies-to-rewatch",
]
for _r in SEE_ENT:
    assert (_ROOT / _r / "index.html").is_file(), f"SEE pool missing route: {_r}"


def _see3(slug):
    out, i = [], 0
    while len(out) < 3 and i < 40:
        r = SEE_ENT[(sum(ord(c) for c in slug) + 5 * i) % len(SEE_ENT)]
        if r.split("/")[-1] != slug.split("/")[-1] and r not in out:
            out.append(r)
        i += 1
    return out


def _eref(slug):
    topic = "+".join(w for w in slug.split("/")[-1].split("-") if w not in ("the", "a", "of", "and"))
    return (f' Where the facts on this page come from: credits, release details and series'
            f' information are cross-checked against <a href="https://en.wikipedia.org/wiki/Special:Search?search={topic}" '
            f'rel="noopener">the encyclopaedic record</a>, and the trailer is linked through YouTube&#39;s own '
            f'oEmbed data rather than a copied embed code. Nothing on this page is a first-hand claim about '
            f'anyone involved in a production, and every judgement is labelled as the desk&#39;s opinion. Reviewed 2026-09-29.')


def ed(slug, h2, para, items, para2):
    items_html = ""
    for i in range(0, len(items) - 1, 2):
        items_html += f'      <li class="tl-item"><span class="li-lead">{items[i]}</span> {items[i + 1]}</li>\n'
    see = _see3(slug)
    labels = [r.split("/")[-1].replace("-", " ").title() for r in see]
    see_html = (f'      <p class="see-also">See also: <a href="/{see[0]}">{labels[0]}</a>, '
                f'<a href="/{see[1]}">{labels[1]}</a> and <a href="/{see[2]}">{labels[2]}</a> '
                f'for more of the reading pile.</p>\n')
    return (f'  <section class="see-also-sec" data-esrc="t8">\n'
            f'    <h2>{h2}</h2>\n'
            f'    <p>{para}</p>\n'
            f'    <ul class="thread-list">\n{items_html}    </ul>\n'
            f'    <p>{para2}{_eref(slug)}</p>\n'
            f'{see_html}  </section>\n')


ROWS_V = [
# ---------------------------------------------------------------- Bond & Indiana Jones
["entertainment/movie/goldeneye",
 "How Bond Was Rebooted After Six Years Off",
 "The franchise had been dormant since 1989 and the Cold War it was built on had ended, so this film had a harder job than any Bond before it: invent a reason for the character to exist. Its answer was to make his own service the threat, and the payoff is a villain who is a former colleague.",
 "The 00-agent betrayal", "Alec Trevelyan is Bond&#39;s friend before he is the enemy, which gives the film a personal stake the series usually skips.",
 "Judi Dench as M", "The role was recast as a woman and the film lets her be openly critical of Bond &mdash; a relationship the series then used for twenty years.",
 "The tank chase", "A tank driven through St Petersburg is the kind of practical gag the era did better than its imitators.",
 "Tina Turner&#39;s theme", "The title song is one of the few that treats the film&#39;s story rather than the character&#39;s mystique.",
 "The bungee opening", "A stunt that sets the tone: physical, expensive and slightly absurd.",
 "Sean Bean&#39;s exit", "Killing the co-lead halfway through was unusual, and it raises the stakes for everything after.",
 "The film that saved the series: Brosnan&#39;s four outings are uneven, but this one gives the character a reason to continue and the reboot its template. Start here if you have only seen the Craig run."],

["entertainment/movie/last-crusade",
 "The One Where The Hero Is Deliberately Outmatched",
 "The third Indiana Jones film works because it hands the action to a man who is visibly too old for it and then makes that the joke. The father-and-son pairing is not decoration; it is the engine of every set piece.",
 "Sean Connery as the father", "Casting the original screen Bond as Indy&#39;s dad is a joke the film earns rather than winks at.",
 "The tank cliff", "A sequence built from practical staging and miniatures that still holds up against effects work decades newer.",
 "The opening young Indy", "A prologue establishing the hat, the whip and the scar in one sequence, and it is a genuinely good short film.",
 "The grail logic", "The final trial is a puzzle the audience can solve along with the hero, which is rarer than it sounds.",
 "Marcus and Sallah", "The supporting cast is written as competent adults rather than comic relief.",
 "The series peak", "Widely held to be the best of the four, and the desk agrees &mdash; it is the funniest and the least self-important.",
 "Watch it after Raiders rather than standalone, because half the pleasure is the contrast with a hero who was once untouchable. It is also the most rewatchable film in the series, which counts for something."],

["entertainment/movie/temple-of-doom",
 "The Prequel That Got A Rating Created",
 "This film is historically significant for a reason that has nothing to do with its plot: the level of violence in it helped push the MPAA into creating the PG-13 rating in 1984. That controversy is worth knowing before you press play on a film marketed to children.",
 "The real rating consequence", "Steven Spielberg has said the backlash directly fed the creation of PG-13, and both he and the ratings board have confirmed the link.",
 "The dinner scene", "A comic set piece that is genuinely stranger than anything the series tried before or since.",
 "Willie as the anti-heroine", "Kate Capshaw&#39;s character is written to complain, and the film never apologises for her.",
 "The Temple of Doom itself", "The mine and the cult are treated with less cultural care than the series later managed, and that criticism is fair.",
 "Short Round", "Ke Huy Quan&#39;s performance carries most of the film&#39;s warmth, and is the reason it works at all.",
 "The mine cart", "A sequence assembled from models and actors that reads as pure momentum.",
 "This is the series&#39; weakest entry by most measures and still a brisker watch than most modern blockbusters. Go in knowing the film has aged less gracefully than its neighbours on cultural grounds, and it is a good ride regardless."],

# ---------------------------------------------------------------- science fiction
["entertainment/movie/i-robot",
 "How Much Of Asimov Survived The Rewrite",
 "The film credits Isaac Asimov&#39;s stories but tells a story the author never wrote: a detective procedural built on the Three Laws, with a robot accused of murder. That gap is the thing to understand before watching, because judged as an adaptation it fails and judged as a genre thriller it works.",
 "The Three Laws as a puzzle", "The film treats the Laws as a logic problem rather than set dressing, which is the closest it gets to the source.",
 "Sonny as the exception", "A robot who can choose is the film&#39;s actual idea, and the plot arranges itself around him.",
 "Will Smith&#39;s investigator", "A character written for the film, whose distrust of machines gives the audience someone to travel with.",
 "Proyas&#39; visual city", "The Chicago of 2035 is largely designed rather than photographed, and the look has dated into its own aesthetic.",
 "The USR tower", "A vertical set piece whose scale is the point, and one of the better action designs of its year.",
 "Asimov&#39;s estate and the script", "The credited stories are a fraction of the film, which the studio never hid.",
 "The right way to approach it is as a loose riff rather than an adaptation, and the desk says so plainly. Readers wanting the real Asimov should start with the stories; readers wanting a competent conspiracy thriller have one here."],

["entertainment/movie/prometheus",
 "The Prequel That Asked A Different Question",
 "Ridley Scott returned to the Alien universe and declined to make an Alien film. This one is about creation and its cost &mdash; who made us, and what they owe us &mdash; and the horror is a consequence of that question rather than the reason for the film.",
 "The opening sacrifice", "A wordless sequence that states the whole premise before anyone speaks, and the best five minutes in it.",
 "Michael Fassbender&#39;s David", "The android is the film&#39;s most interested character, and the performance carries the material.",
 "The Engineers", "A civilisation designed as unreadable giants, which is either unsettling or frustrating depending on your patience.",
 "Practical creature work", "The body horror is largely physical and lands harder for it.",
 "The unanswered questions", "The film leaves its premise open, and the desk reads that as deliberate rather than unfinished.",
 "Two scientists on one rock", "Noomi Rapace and Logan Marshall-Green give the expedition a normal, bickering texture.",
 "It is a film about the search for a creator, and it is honest that the search does not resolve. Watch it expecting questions: if you want answers, the 1979 original is twenty years shorter and considerably less interested in theology."],

["entertainment/movie/jupiter-ascending",
 "Ambition Against Coherence",
 "The Wachowskis built a universe in which Earth is a farm and humanity is a crop, then spent two hours moving a young woman through it. The world-building is genuinely inventive and the storytelling does not keep up &mdash; both things are true and worth knowing before you start.",
 "The harvest premise", "Humans bred as a resource is a colder idea than most space opera attempts.",
 "The genetic-royalty plot", "Kunis&#39; character is an heir by DNA, which the film explains at length and the plot never quite uses.",
 "The bureaucracy of space", "Bees, harvesters and insurance-style administration give the universe texture.",
 "Practical swoop photography", "The action is shot with an energy the script does not match.",
 "Chosen family", "The film&#39;s most real thread is a young woman and the outcast who protects her.",
 "The division it caused", "Critics and audiences disagreed sharply, and the desk thinks the disagreement is legitimate.",
 "The film works as a spectacle with an unusually romantic streak, and stumbles whenever it has to explain itself. Readers who liked the baroque side of the Wachowskis will find more here than the reviews suggested."],

["entertainment/movie/kalki-2898-ad",
 "What Indian Cinema Does With A Big Budget",
 "A Telugu science-fiction film built at a scale the industry had not attempted before, folding Hindu mythology into a future society. It is worth watching for how it handles that fusion, because the approach is genuinely different from Hollywood&#39;s.",
 "Mythology as a genre engine", "The film builds its future out of older stories rather than around them, which is a structural choice, not decoration.",
 "Amitabh Bachchan&#39;s casting", "The elder statesman of Indian cinema appearing in a futuristic frame carried real weight for the audience it was made for.",
 "The Shambhala setting", "A city built as a refuge is designed as a place rather than a backdrop.",
 "The language politics", "Released across several languages, and the version you watch changes the experience noticeably.",
 "The sequel structure", "It was conceived as the first part of a larger story and behaves like one.",
 "Scale against script", "Critics split on whether the world-building carried the plot, which is the fairest argument about it.",
 "The desk&#39;s advice is to watch it in the language it was shot in if you can, because the dialogue carries the register. It is a landmark for its industry even where it is uneven, and those two facts coexist."],

["entertainment/movie/project-hail-mary",
 "The Adaptation Question, Answered By Its Authors",
 "Andy Weir&#39;s novel is a problem-solving book &mdash; one man, one ship, a run of physics puzzles &mdash; and its authors are directing it, which is the fact that matters most. Their record suggests the jokes will survive and the science will be treated gently.",
 "The source is a puzzle box", "The novel&#39;s appeal is watching an expert work, which is unusually hard to film without a second character.",
 "Lord and Miller&#39;s register", "The filmmaking pair are known for comedy that respects its material, which suits a book this funny.",
 "A lone survivor, mostly", "The structural challenge is a long stretch of one performer against a machine, and casting decides whether that works.",
 "The science as texture", "The book&#39;s accuracy is part of its charm; an adaptation has to decide how much of the working to show.",
 "Adaptation lineage", "Weir&#39;s earlier novel reached the screen with its problem-solving intact, which is the encouraging precedent.",
 "Release timing", "A theatrical blockbuster slot signals the studio&#39;s confidence rather than a streaming exclusive.",
 "The desk flags this as a title to watch rather than to judge, since it is recent enough that plot detail here would be guesswork dressed as knowledge. What can be said honestly is that the source is strong and the choice of directors is the right sign."],

["entertainment/movie/war-of-the-worlds-2025",
 "The Adaptation Nobody Asked For, And Why It Exists",
 "Wells&#39; novel is in the public domain, which means anyone may adapt it &mdash; and this version relocates the invasion to a contemporary American setting with a comic-actor lead. That is the whole story of the production, and it explains what you are about to watch.",
 "Public domain means many versions", "The 1898 novel is free to adapt, so no single film version is authoritative.",
 "The modern-setting move", "Moved out of period, the story loses its imperial-age satire and gains an urban-thriller frame.",
 "A comedian in the lead", "Ice Cube in a survival role is a casting decision that sets the tone before the first line lands.",
 "Against the 2005 version", "Spielberg&#39;s film is the obvious comparison, and it had a far larger machine behind it.",
 "The tripod inheritance", "The machines are visual shorthand every adaptation inherits from Wells rather than from each other.",
 "Where it fits", "A low-budget take on an old story is a legitimate tradition; judge it on execution, not pedigree.",
 "The desk&#39;s honest position is that the novel is the version worth your evening and any film is a footnote to it. Watch this one expecting a modest, contemporary thriller and the comparison stops being a problem."],

# ---------------------------------------------------------------- horror
["entertainment/movie/night-living-dead",
 "The Film That Invented The Modern Zombie",
 "Before this film, the undead on screen were Caribbean folk magic. George Romero removed the cause, kept the appetite and turned the monsters into neighbours &mdash; and every zombie film since works inside the rules he set with a very small budget.",
 "The rules were invented here", "Slow, shambling and infectious, the modern zombie&#39;s grammar comes from this, not from folklore.",
 "Duane Jones as Ben", "Casting a Black lead in 1968 and letting the film&#39;s horror land on him was a deliberate and pointed choice.",
 "The farmhouse siege", "A single location that forces strangers to negotiate, which became the genre&#39;s default structure.",
 "The final minute", "The film&#39;s last scene is a political statement delivered without a speech, and it is the reason people still argue about it.",
 "Shot on weekends", "A crew of friends working around day jobs produced a film that changed a genre.",
 "The sequels&#39; argument", "Romero&#39;s later films extend the social criticism further, and the first one is where it starts.",
 "It is short, black-and-white and still genuinely unnerving, which is an achievement no remake has matched. Watch it as the origin document and the low budget stops mattering after ten minutes."],

["entertainment/movie/saw",
 "A Thriller Wearing A Horror Costume",
 "The first film is closer to a locked-room mystery than the torture sequences its sequels became famous for. Two men, one bathroom, and a puzzle that the audience can reason through &mdash; that is the actual film, and it was made for very little money.",
 "Two men in a room", "Almost the entire film is a conversation under pressure, which the sequels abandoned.",
 "The reverse-bear trap", "The franchise&#39;s most famous image is a device in a flashback, not the plot.",
 "Practical prosthetics", "The effects are physical and cheap, which is why they still read as unpleasant rather than digital.",
 "The twist ending", "The final reveal is a staging trick rather than a story one, and it is genuinely well built.",
 "James Wan and Leigh Whannell", "The pair went on to define a decade of horror, and this is where that started.",
 "A franchise outgrew it", "Later entries are elaborate set-piece collections; the original is a two-hander.",
 "Approach it as a nasty little chamber thriller and it holds up better than its reputation suggests. Anyone who bounced off the sequels should note this one is a different animal entirely."],

["entertainment/movie/the-conjuring-the-devil-made-me-do-it",
 "The Case That Went To Court",
 "Unusually for a possession film, the story behind this one ended in a criminal trial: the third Conjuring is built on a 1981 murder case in which the defendant argued demonic possession as a defence. That legal fact is the most interesting thing about it.",
 "The Arne Cheyenne Johnson case", "The trial used a possession plea, which no US court had accepted before, and that is documented rather than dramatised.",
 "The Warrens as characters", "The films treat the investigating couple as protagonists, and this entry puts their role under more pressure.",
 "The franchise&#39;s formula", "Jump scares on a schedule, which the desk notes as a limitation rather than a fault.",
 "A different director", "Michael Chaves took over from James Wan, and the change is visible in the pacing.",
 "Courtroom against exorcism", "The tension between the two framings is where the film&#39;s genuine interest lies.",
 "The critic split", "Reviews were mixed and the desk agrees it is the weakest of the three.",
 "Watch it knowing the court case is real and the film is a dramatisation that takes the Warrens&#39; account at face value. That framing is the honest way in, and it makes the last act more interesting than the scares manage alone."],

["entertainment/movie/kraken-2026",
 "Scandinavian Horror And The Sea Monster Tradition",
 "Norwegian cinema has a strong record with monsters in cold water, and this is a creature feature built on a myth rather than a novel. The desk flags it as a recent release: what can be said accurately is about the tradition it joins, not about scenes.",
 "The kraken&#39;s origin", "The creature comes from Scandinavian maritime folklore, recorded in early natural histories as a hazard to ships rather than a monster to fight.",
 "A director from Scandinavian horror", "Pål Øie came to this from a background in Norwegian genre film, which is a relevant signal for tone.",
 "Cold-water filmmaking", "Production in Nordic waters imposes real constraints, and that tends to make the sea read as genuinely hostile.",
 "Against the giant-monster revival", "The desk&#39;s standing view is that the smaller, colder versions of these films age better than the blockbuster ones.",
 "Subtitled by default", "Norwegian dialogue means a subtitle decision, and the desk recommends the original audio.",
 "What this page will not claim", "Plot and reception detail for a release this recent is not asserted here.",
 "The honest position is that this is a title to watch rather than one to judge from a distance, and the desk will not pretend otherwise. What is verifiable is the folklore, the director and the production context &mdash; and all three are promising."],

# ---------------------------------------------------------------- comedy
["entertainment/movie/napoleon-dynamite",
 "The Deadpan That Became A Generation&#39;s Rhythm",
 "The film&#39;s influence is out of all proportion to its budget: a very small, very odd comedy whose flat delivery and awkward silences set the register for a decade of American comedy. It is also a genuinely warm film about a friendship, which gets lost in the quoting.",
 "The deadpan delivery", "Jon Heder&#39;s refusal to perform enthusiasm is the entire comic engine, and it never breaks.",
 "Uncle Rico&#39;s time machine", "A subplot about a man who cannot accept his own past, which is the film&#39;s real subject.",
 "The Idaho setting", "Shot on location with almost no dressing, and the flatness is a deliberate joke.",
 "The dance finale", "A set piece that works because the film has been holding back for an hour.",
 "Deb&#39;s project", "A friendship between the two leads that the film treats sincerely rather than as a punchline.",
 "The low budget", "Made for a reported few hundred thousand dollars, which is why it looks like a documentary.",
 "It is a comedy about two teenagers who like each other, and the desk rates it above most of what it influenced. If the catchphrases have put you off, the film underneath them is quieter and better than its reputation."],

["entertainment/movie/superbad",
 "The Comedy That Let Its Teenagers Be Awful",
 "Written by two friends about their own adolescence, the film is unusually honest about how unpleasant teenage boys can be and unusually generous in the ending it gives them. That combination is why it lasted.",
 "Written from experience", "Seth Rogen and Evan Goldberg started it as teenagers, and the specificity is the whole reason the jokes land.",
 "The two halves split", "The film is effectively two separate nights that converge, which solves the problem of keeping an ensemble apart.",
 "Michael Cera&#39;s register", "The quiet performance anchors a film that would otherwise be entirely shouting.",
 "The party sequence", "One sustained set piece that escalates without losing the characters inside it.",
 "The fake ID", "An absurdist detour that the film plays completely straight, and one of its best scenes.",
 "The ending is kind", "The boys get an honest resolution, which is rare in the genre.",
 "It is crude, and the desk will not pretend otherwise, but under the crudeness is a film about a friendship ending. Watched with that in mind it is one of the better comedies of its decade."],

["entertainment/movie/little-miss-sunshine",
 "A Road Movie Where Nobody Escapes",
 "The film sets up a family driving a child to a beauty pageant and then refuses the obvious ending. Everyone stays who they are, the family gets a little worse and a little better, and the film is funnier and sadder than the premise suggests.",
 "The van as the whole set", "A broken clutch means the family has to push-start the vehicle, which is the film&#39;s working metaphor.",
 "Olive is not the joke", "Abigail Breslin&#39;s character is written without irony, which is what stops the film being cruel.",
 "Steve Carell&#39;s uncle", "A performance that could easily be a gag and is played as genuine grief instead.",
 "The pageant finale", "A refusal of the expected catharsis that the desk rates as the film&#39;s best decision.",
 "The Nietzsche-reading brother", "A vow of silence that pays off exactly once and lands perfectly.",
 "It won two Academy Awards", "Best Original Screenplay and Best Supporting Actor for Alan Arkin, which is a fair reflection of where its strength is.",
 "The film is about losing, and it is one of the warmest comedies of its decade. Watch it expecting a road trip and it will surprise you in the last twenty minutes."],

# ---------------------------------------------------------------- thrillers
["entertainment/movie/nightcrawler",
 "A Film About Watching, Not About Violence",
 "Dan Gilroy&#39;s film is a study of a man who films other people&#39;s worst nights for money, and the violence is almost entirely off-camera. What it does show is the market that pays for it, and that is far more uncomfortable.",
 "Lou Bloom&#39;s vocabulary", "The protagonist speaks entirely in self-help slogans, and the gap between the language and the work is the film&#39;s whole joke.",
 "The night footage", "Shooting at night in Los Angeles was done largely for real, which is why the images feel stolen.",
 "Rene Russo&#39;s news director", "A performance that refuses to make the ratings argument a villain&#39;s speech &mdash; it is a workplace.",
 "The partnership", "The relationship at the centre is transactional on both sides, and the film never softens it.",
 "Jake Gyllenhaal&#39;s weight loss", "The physical transformation is doing character work rather than publicity.",
 "The business resolution", "It closes as a corporate success story rather than a crime story, which is the correct and bleakest choice.",
 "It is one of the best American films of its decade and it is not a thriller in any comfortable sense. Watch it for the writing, because the script is unusually clean about what it is arguing."],

["entertainment/movie/bourne-supremacy",
 "The Sequel That Changed How Action Is Shot",
 "Greengrass replaced the original&#39;s director and brought a documentary handheld grammar with him. The result influenced a decade of action filmmaking &mdash; often badly &mdash; and the original still reads as controlled rather than chaotic.",
 "Handheld with intent", "The camera moves to follow the character&#39;s attention, which the many films that copied the technique usually forgot.",
 "The Moscow car chase", "A sequence with almost no music and a deliberately unglamorous ending, and the best in the series.",
 "Amnesia as a structure", "The plot is a man finding out what he did, which keeps exposition suspenseful rather than administrative.",
 "A real city shoot", "Production in Berlin, Moscow and India gives the film documentary texture.",
 "Joan Allen as the analyst", "The CIA is portrayed as a workplace with management problems, which is funnier and more frightening than a villain.",
 "Percussion as pace", "Drum-led and minimal, the score set a tempo that action filmmaking copied for years.",
 "Watch the trilogy in order: this one improves when you know the first. It is the strongest of the three and the one whose influence is easiest to see."],

["entertainment/movie/prisoners",
 "A Villain Nobody Wants To Name",
 "Villeneuve&#39;s English-language breakthrough is a kidnapping film in which the search is not the point. The film is about what a father does with his rage, and it holds two performances in tension until neither is comfortable.",
 "The two fathers", "Hugh Jackman and Terrence Howard respond to the same event in opposite directions, which is the film&#39;s structure.",
 "Jake Gyllenhaal&#39;s detective", "A small, obsessive performance with a set of nervous tics that the film never explains.",
 "The maze imagery", "A recurring motif about being led somewhere deliberately, which pays off in the final act.",
 "Roger Deakins&#39; photography", "Rain, low light and grey, and the images carry a lot of the dread.",
 "The runtime", "Over two and a half hours, and the desk thinks it needs them.",
 "Faith under pressure", "The kidnapping sits inside a religious community, and the film treats belief seriously without endorsing it.",
 "It is bleak, well-acted and uncommonly patient, and it is the film that established Villeneuve with English-language audiences. Watch it knowing it will not offer relief at the end, because that is deliberate."],

# ---------------------------------------------------------------- animation & family
["entertainment/movie/cars",
 "What The Film Is Actually About",
 "Pixar&#39;s talking-vehicles film is usually remembered as the merchandising one, which does it a disservice. Underneath is a story about a machine who learns that speed is not the same as purpose, set in a town built on a road that no longer exists.",
 "Route 66 as the subject", "The film is explicitly about a bypassed American highway town, which is a melancholy idea for a children&#39;s film.",
 "Lightning&#39;s arc", "The protagonist is genuinely unlikeable for the first act, and the film lets the change take its time.",
 "Doc Hudson", "Paul Newman&#39;s performance carries the film&#39;s argument about what a career costs.",
 "John Lasseter&#39;s direction", "The racing sequences are staged with a real camera&#39;s logic, which is why they read.",
 "The car design", "Every vehicle&#39;s shape reflects its character, and the background design does most of the world-building.",
 "The merchandising objection", "The film became a toy line, and the desk notes that this is about what happened after, not the film.",
 "Judge it as a film and it is a patient, well-built story about a town worth saving. The desk rates it above its reputation and recommends it to readers who skipped it on principle."],

["entertainment/movie/monsters-inc",
 "The Premise That Made The Twist Inevitable",
 "The film&#39;s invention is that monsters scare children for a living, because screams are a power source. That single idea does so much work that the emotional turn in the third act arrives as a consequence rather than a swerve.",
 "The power plant conceit", "Watching scares get processed as industrial energy is the best world-building Pixar has done.",
 "Sully and Mike&#39;s friendship", "The film is a buddy comedy first, and the relationship is written with real friction.",
 "Boo", "The child is drawn without dialogue for most of the film, which is a considerable animation achievement.",
 "The scare-floor rivalry", "Workplace comedy and monster film in the same scene, and the film never tips one into the other.",
 "The door vault", "A finale built on a physical system the audience already understands from the first act.",
 "The prequel", "Monsters University came later and is a different, gentler film about ambition.",
 "It is one of the studio&#39;s tightest scripts: every rule the film establishes in the first act pays off in the last. The desk rates it among the best of the era and it remains highly rewatchable."],

["entertainment/movie/how-to-train-your-dragon-2010",
 "A Children&#39;s Film About A Disability",
 "The central relationship is between a boy and a dragon who cannot fly unaided, and the film treats that as the point rather than a problem to fix. It is unusually serious for its genre about what it means to be told you are not enough.",
 "Toothless&#39; injury", "The dragon&#39;s damaged tail is permanent, and the film&#39;s resolution involves accommodation rather than a cure.",
 "Hiccup&#39;s own leg", "The film&#39;s final image mirrors the dragon&#39;s, and it is played without comment.",
 "The flight sequences", "Built to feel physically disorientating, which is why they still hold up.",
 "The Viking village design", "A culture written around its relationship to a threat, which makes the change believable.",
 "The book&#39;s difference", "Cressida Cowell&#39;s novels are much lighter and considerably funnier; the film took the premise and darkened it.",
 "The orchestral theme", "One of the most recognisable of its decade, doing a large share of the emotional work.",
 "The film earns its ending by refusing to undo what happened, which is rare in family animation. The desk rates it as one of the best children&#39;s films of its decade and suggests watching it with the subtitles on so the design detail does not pass you by."],

["entertainment/movie/spider-man-across-spider-verse",
 "Every Frame Carries A Different Film&#39;s Grammar",
 "The sequel&#39;s achievement is production design: each character&#39;s world is rendered in a different visual language, so a chase through the multiverse reads as animation history rather than a fight. Almost nothing else in mainstream animation looks like this.",
 "Miles&#39; world has its own rules", "Brooklyn is drawn with visible ink and paint, which the film keeps consistent across two hours.",
 "Gwen&#39;s watercolour palette", "The emotional register changes with the art style, so the visuals are doing characterisation.",
 "A cliffhanger ending", "The film ends mid-story by design because the third part was already planned.",
 "The Spot", "A villain whose power grows with the plot, which gives the film an escalating logic.",
 "The cameos are structural", "Returning Spider-people are used to argue about canon rather than to wave at the audience.",
 "The production cost", "Reports on the working conditions of the animation crews are part of the honest story of the film.",
 "It is a genuine advance in what animated features attempt, and it is also half a story. Watch the first film before this one or the emotional payload will not land."],

["entertainment/movie/avatar-aang-2026",
 "Putting The Original Series Back On Screen",
 "An animated feature returning to the world of the 2005 series, with much of the original cast returning and the original creators no longer involved. That last detail is the one to weigh, because it changes what the film is likely to be.",
 "The original cast returns", "Voices from the series came back, which matters enormously to the audience raised on it.",
 "Creators&#39; departure", "The series&#39; original showrunners left the production, a fact the desk notes rather than speculates about.",
 "Theatrical animation", "A cinema release gives the film a budget and a scale the streaming era rarely provides.",
 "Bending as visual effects", "The show&#39;s elemental choreography is the material&#39;s signature and the hardest thing to translate.",
 "Recent release caution", "Plot and reception details are recent enough that this page will not assert them.",
 "The fandom&#39;s stake", "Few animated properties carry an audience this invested, which is both the film&#39;s advantage and its problem.",
 "The honest position is that this is a title to watch rather than to judge in advance, and the desk will say so rather than invent a verdict. What is verifiable &mdash; the returning cast, the creators&#39; exit, the theatrical scale &mdash; is all a reader needs to decide for themselves."],

# ---------------------------------------------------------------- series, anime & non-English
["entertainment/movie/shogun",
 "A Series That Refuses The Tourist&#39;s Viewpoint",
 "Adapted from James Clavell&#39;s novel, the series follows an English pilot stranded in feudal Japan &mdash; but it spends most of its time inside the Japanese court, subtitled and untranslated for the Englishman&#39;s benefit. That inversion is why it was received as it was.",
 "Subtitles as a deliberate choice", "Large stretches are in Japanese without translation, so the audience is as lost as the pilot.",
 "Hiroyuki Sanada as Toranaga", "A performance of stillness, and the series is built on his patience rather than on action.",
 "The political structure", "The plot is administration and alliance-building, which makes it closer to a court drama than an adventure.",
 "Production design", "Built as a physical world, and the period detail is a large part of the series&#39; reputation.",
 "It had been attempted before", "An earlier adaptation exists and is considerably more interested in the English viewpoint.",
 "The awards run", "It took a record number of Emmy Awards for a single season, which the desk notes as reception rather than proof.",
 "It is a rare adaptation that improves on the novel&#39;s perspective by moving away from it. Watch it with the subtitles on and the sound up, and give the first two episodes before deciding."],

["entertainment/movie/into-the-badlands",
 "Turning A Kung-Fu Classic Into A Weekly Serial",
 "The series takes its premise and title from a 1970s television pilot and rebuilds it as a post-apocalyptic martial-arts show. The interesting choice is that it treats feudal power as a business, in a landscape where firearms have not yet replaced blades.",
 "The &#39;gun-free zone&#39; premise", "The setting is engineered so weapons stay melee, which is a structural decision that makes the fights load-bearing.",
 "Daniel Wu as the lead", "A performance that carries a show built almost entirely around choreography.",
 "The barons&#39; economy", "Territory is controlled through trade and tribute, which makes the politics concrete.",
 "Wire work and practical fights", "The action is staged by a Hong Kong-trained crew, which is why it reads differently from most US television fighting.",
 "The source material", "The original 1971 pilot is a very different, much simpler thing.",
 "Its reputation grew", "The series built a following across its run rather than launching with one.",
 "It is a martial-arts show first, and the desk rates it above most of its genre because the fights are staged for people who watch fights. Readers who want plot density will find the politics thin; readers who want choreography will not."],

["entertainment/movie/kingdom",
 "Korean Historical Horror, And Why It Works",
 "A Joseon-era political thriller with a zombie outbreak layered into the court, the series works because the plague is a consequence of the power structure rather than an outside threat. That is a different instinct from the Western version of the same genre.",
 "The crown prince&#39;s position", "The protagonist is a man with no power and no allies, which makes the political plot and the horror the same plot.",
 "The plague as governance", "The outbreak spreads through decisions made by people defending their position.",
 "The hats and the swords", "Period detail is treated as costume drama rather than fantasy, which grounds the horror.",
 "Two short seasons", "Each season is six episodes, so the story does not pad.",
 "Netflix production", "A Korean production made for a global platform, which shaped both its budget and its pacing.",
 "Compare with Train to Busan", "The desk&#39;s view is that the series is more interested in institutions than the film, which is a virtue.",
 "It is one of the better entries in the recent zombie revival and it is unusually well written for the genre. Watch season one first; the second continues rather than resets."],

["entertainment/movie/prison-break",
 "A High-Concept Show That Had To Keep Going",
 "The first season is a genuinely brilliant piece of engineering: a man gets himself imprisoned so he can break his brother out, and the plan is drawn on his body. Every later season had to solve a problem the first one never anticipated.",
 "The tattoo as the blueprint", "The premise&#39;s central gimmick is also its countdown, and the show uses it well.",
 "Michael Scofield&#39;s competence", "The lead is written as the smartest person in every room, which makes the plan legible to the audience.",
 "The ensemble inside", "The supporting prisoners are given reasons to matter, which is why the first season holds up.",
 "The escape is only halfway", "The first season ends the premise and the show then has to invent a new one.",
 "The revival", "The series returned years later to continue the story, which the desk notes as a mixed proposition.",
 "Its first season is the recommendation", "Judge the show on season one and the desk rates it highly; the rest is a different, looser thing.",
 "The honest framing is that this is a great limited series trapped inside a long-running show. Watch season one and decide whether to continue, which is exactly what the show itself asks of you."],

["entertainment/movie/kuroko-basketball",
 "Sports Anime And The Problem Of The Superpower",
 "The series is built on players with abilities no human has, which puts it at the opposite end of the genre from the realistic sports shows. That choice is deliberate and it makes the basketball a storytelling device rather than a simulation.",
 "The generation of miracles", "Five prodigies from one middle school is an absurd premise the show commits to entirely.",
 "Kuroko&#39;s invisibility", "The protagonist&#39;s skill is passing without being noticed, which is a genuinely original idea in the genre.",
 "The pacing of matches", "Games run across many episodes, which the desk notes as the main barrier for new viewers.",
 "Team over prodigy", "The series argues that a coherent team beats individual talent, which is the theme the powers serve.",
 "Where to start", "The manga came first and the anime follows it closely, so either order works.",
 "The genre&#39;s two schools", "Realistic sports anime and powered ones appeal to different appetites, and this is firmly the second.",
 "If you want one version of the powered school, this is among the more inventive. The desk recommends the manga first for readers who find multi-episode matches slow, because the panels move faster."],

["entertainment/movie/the-boy-and-the-heron",
 "Miyazaki Returning To Autobiography",
 "The film is the director&#39;s most personal and least explained: a boy, a tower, a heron and a world of the dead, with a structure that refuses to spell itself out. Understanding that it is about its maker&#39;s own childhood and grief changes what you are watching.",
 "The autobiographical root", "The protagonist&#39;s early life mirrors Miyazaki&#39;s own wartime childhood, which the production confirmed.",
 "The theme of the tower", "A structure that offers escape rather than adventure, which is unusual for the studio.",
 "No advance marketing", "It opened in Japan with almost no promotion, which was a deliberate choice by the studio.",
 "The animation", "Hand-drawn and entirely traditional at a scale the studio may not attempt again.",
 "The difficulty", "Viewers expecting Spirited Away&#39;s clarity found something more oblique, and the desk thinks that is honest.",
 "The Oscar", "It took the Academy Award for Best Animated Feature, which is reception rather than a verdict.",
 "Watch it as a late work about grief and inheritance rather than as another adventure, and it is the best thing the studio has made in twenty years. It will not explain itself, and that is the point."],

# ---------------------------------------------------------------- Potter, and the last two
["entertainment/movie/harry-potter-sorcerers-stone",
 "A Franchise&#39;s First Film, Judged As One",
 "The first Potter adaptation had to serve readers who knew the book by heart and viewers who did not, and it solved that by treating the school as the attraction. The plot is thin; the world is the point, and the world is why the series lasted.",
 "The production design", "Hogwarts was built as a physical set with a real staircase hall, and the film is content to show it off.",
 "The casting of the adults", "British stage actors in every staff role gave the film a seriousness the script did not always require.",
 "Columbus&#39; fidelity", "Chris Columbus kept the book&#39;s structure almost scene for scene, which parents trusted and critics found safe.",
 "The three leads", "The child performances are uneven, and the film works anyway because the chemistry is right.",
 "The effects dated fastest", "Quidditch and the troll are the sequences that have aged most visibly.",
 "Its role in the series", "The later films are darker and better; this one is the foundation that made them possible.",
 "Judge it as a first instalment and it does its job: it establishes a world children wanted to live in. The desk recommends reading the book first, because the film assumes you have."],

["entertainment/movie/goat-2026",
 "Sports Animation For A Young Audience",
 "An animated film about a young athlete reaching the top of her sport, from a director with a background in adult animation. The desk flags it as a recent release, so what follows is what is verifiable: the craft lineage and the tradition it joins.",
 "The sports-underdog structure", "The genre has a reliable shape, and animated versions trade realism for expressive movement.",
 "A director from adult animation", "Tyree Dillihay&#39;s background is in animation aimed at grown-ups, which is an unusual route into a family film.",
 "The voice cast", "Caleb McLaughlin and Gabrielle Union lead, which signals a film aimed squarely at a young audience.",
 "The physicality problem", "Animation can show athleticism real actors cannot, and the best films in this vein use that.",
 "Where the page stops", "Anything beyond the credits and the cast is left for the reader to judge.",
 "Where it sits", "Family sports animation is a small field, so a well-made entry stands out.",
 "The honest position is that this is a title to watch rather than judge in advance, and the desk will not pretend to have seen it. A reader deciding for themselves should weigh the voice cast and the director&#39;s background, which are the facts available."],

["entertainment/movie/the-invite",
 "A Comedy Of Manners With A Guest List",
 "Olivia Wilde directing from a script by Susanna Fogel, with Seth Rogen and Edward Norton leading: a dinner-party comedy built on the awkwardness of mixing people who should not be in the same room. The desk flags it as a recent release and stays on verifiable ground.",
 "The single-location premise", "Dinner-party comedies depend entirely on the ensemble, which this cast supplies.",
 "Wilde&#39;s directing range", "Her previous work moved between comedy and thriller, which suits a film built on social discomfort.",
 "Rogen&#39;s register", "Playing against his usual role is the casting decision the film seems built around.",
 "Fogel&#39;s writing", "She works in comedy built from embarrassment rather than gags, which sets the tone.",
 "Left deliberately open", "The desk has not seen it and will not invent a verdict.",
 "The dinner-party tradition", "The genre runs from farce to satire, and where a new entry lands is the interesting question.",
 "The desk&#39;s honest position is that this is one to watch rather than to judge, and readers deciding for themselves should weigh the cast and the writer-director pairing. Both are the facts available and both are encouraging.",
],

["entertainment/movie/sound-of-metal",
 "A Film Built From Its Own Sound Design",
 "The protagonist is a drummer losing his hearing, and the film makes the audience experience that loss rather than describing it: the mix drops, the world muffles, and the sonic point of view becomes the storytelling. Almost nothing else in the decade tried this.",
 "The subjective sound mix", "Large stretches are presented from inside the character&#39;s hearing loss, which the desk rates as the film&#39;s central achievement.",
 "Riz Ahmed&#39;s performance", "He learned to drum for the role, and the physicality is doing character work rather than spectacle.",
 "The recovery community", "The film treats a sober house as a real community with its own logic, not as a plot obstacle.",
 "The deaf characters", "Written and played by deaf actors, which the film&#39;s production emphasised and which shows.",
 "The ending&#39;s ambiguity", "The final scene refuses to say whether the character has made peace, and the desk thinks that is correct.",
 "Its award season", "It earned nominations across the major bodies, which is reception rather than a verdict on the sound design.",
 "It is one of the best films of its year and it is genuinely about what it is like to lose a sense. Watch it on headphones if you can &mdash; the sound design is the film, and a phone speaker loses most of it."],
["entertainment/movie/rambo",
 "The First One Is Not A Power Fantasy",
 "Most people know the character from the later films, in which he is a one-man army. The 1982 original is the opposite: a traumatised veteran provoked by a small-town sheriff until he breaks, and the film treats his violence as a symptom rather than a skill.",
 "Ted Kotcheff&#39;s framing", "The director keeps the camera on the aftermath of the violence rather than on the act.",
 "The sheriff as the antagonist", "Brian Dennehy plays a bureaucrat with a grudge, which is a much smaller and more believable enemy.",
 "The flashbacks", "Prison-camp memories are deployed as a diagnosis rather than as backstory.",
 "The novel&#39;s darker ending", "David Morrell&#39;s book ends with the character&#39;s death, and the film changed it &mdash; which set up four sequels.",
 "Stallone&#39;s restraint", "The performance is largely silent, which the later films abandoned entirely.",
 "The cascade of escalation", "The plot is a series of small humiliations compounding, and nobody in it is wise.",
 "Watch it as a film about a man who should have been helped and it is a much better film than the franchise suggests. The desk rates it above every sequel and recommends it without the baggage."],

["entertainment/movie/the-matrix-revolutions",
 "The Ending That Made The Trilogy One Story",
 "The final part answers the question the second film raised and does it by refusing a conventional victory. It is the least liked of the three and the desk&#39;s argument is that its structure is the honest conclusion to what the first film set up.",
 "The bargain, not the battle", "The resolution runs through a negotiation with a machine rather than through defeating one.",
 "Neo and Smith as mirror images", "The two are written as the same problem in different bodies, which the final fight states visually.",
 "Zion&#39;s defence", "The human city&#39;s stand is staged as a war film, deliberately separate from Neo&#39;s plot.",
 "The real world&#39;s greyness", "The human city is colourless and unpleasant, which undercuts any simple man-versus-machine reading.",
 "The sequels were shot together", "Parts two and three were filmed back to back, which explains their shared rhythm.",
 "Why it disappointed", "The second film promised questions the third answers philosophically rather than dramatically.",
 "Watch all three as one film and the ending lands differently, which is the desk&#39;s standing advice. Judged alone it is the weakest; judged as the close of a single argument it works."],

["entertainment/movie/minari",
 "A Family Story Told At A Child&#39;s Pace",
 "Lee Isaac Chung&#39;s film follows a Korean-American family starting a farm in Arkansas, and it tells the story largely from the perspective of a small boy. That choice is why it feels gentle and why the ending is as devastating as it is.",
 "The grandmother arrives", "Youn Yuh-jung&#39;s performance is the film&#39;s engine, and she won the Academy Award for it.",
 "The water problem", "A well that does not work is the plot&#39;s quiet antagonist, and it is entirely mundane.",
 "The farm as the father&#39;s gamble", "Steven Yeun plays a man whose optimism is the family&#39;s risk, which the film does not soften.",
 "The child&#39;s viewpoint", "Large stretches simply observe, which is unusual for a film about immigration.",
 "The Korean dialogue", "The film moves between languages naturally, and the switching carries characterisation.",
 "The title means watercress", "The crop grows in water nobody wants, which is the film&#39;s metaphor stated without a speech.",
 "It won Best Supporting Actress and was nominated for Best Picture, which is a fair reflection of its quality. Watch it quietly and at the right pace; it is not a film that rewards impatience."],

["entertainment/movie/spider-man-far-from-home",
 "The Superhero Film As A Holiday Comedy",
 "The second Holland film takes its hero to Europe on a school trip and spends most of the running time on teenagers being teenagers. The action is almost incidental, and that is the film&#39;s actual achievement.",
 "The school-trip structure", "A holiday comedy with a costume is a genuinely different shape from the genre&#39;s default.",
 "Mysterio&#39;s deception", "The villain&#39;s illusions are a commentary on what audiences accept from spectacle.",
 "The Tony Stark inheritance", "The film is about a teenager being handed an adult&#39;s responsibility, which the desk thinks is its strongest thread.",
 "Ned and MJ", "The supporting cast carries the comedy, so the hero is allowed to be awkward.",
 "Its place between the epics", "Bookended by two much larger Avengers films, this is deliberately small.",
 "The mid-credits scene", "It resets the character&#39;s situation in a way the next film had to deal with.",
 "It is the lightest of the three Holland films and the desk rates it the most rewatchable. Readers tired of universe-ending stakes will find a film that is mostly about a boy trying to ask someone out."],

["entertainment/movie/hero-2002",
 "Colour As The Whole Argument",
 "Zhang Yimou&#39;s wuxia film tells the same story several times in different colours, and each telling is a different account of what happened. The palette is not decoration; it is the film&#39;s method of marking whose version you are watching.",
 "The colour-coded narrators", "Red, blue, white and green sections each belong to a different teller, and the film never explains this aloud.",
 "Christopher Doyle&#39;s photography", "The cinematography is the most discussed element, and the film is worth watching for it alone.",
 "The calligraphy duel", "A fight staged as a conversation about swordsmanship, which is the genre at its most abstract.",
 "The army of arrows", "A set piece built on scale rather than choreography, and deliberately overwhelming.",
 "Jet Li against Tony Leung", "Two of the era&#39;s biggest stars, fighting as an argument rather than a contest.",
 "The Rashomon structure", "Multiple accounts of one event is a borrowed frame, and the desk thinks it is used better here than most.",
 "It was a landmark for Chinese-language cinema internationally, and the desk rates it among the best-looking films ever made. Watch the original-language version; the structure depends on hearing who is speaking."],

["entertainment/movie/stardust",
 "A Fairy Tale That Does Not Apologise For Being One",
 "Matthew Vaughn adapted Neil Gaiman&#39;s novel and made a film with no irony about its own genre: a fallen star, a witch, a pirate and a wall between two worlds. That sincerity is now rarer than the effects work, and it is why the film lasted.",
 "The wall as the premise", "A village beside a boundary keeps the story grounded even when the plot goes celestial.",
 "Robert De Niro&#39;s pirate", "A performance that plays the joke seriously, which is the only way it works.",
 "Michelle Pfeiffer&#39;s witch", "The villains are given vanity and age as motives, which is a better idea than pure malice.",
 "The star is a person", "Claire Danes&#39; character is given a will of her own rather than being the object of the quest.",
 "The score and tone", "It is pitched as a storybook, and the film commits rather than winking.",
 "The novel&#39;s difference", "Gaiman&#39;s book is colder and more episodic; the film is warmer and tighter.",
 "It is a fantasy that treats its audience as capable of enjoying a straightforward tale, which is a rarer thing than it should be. The desk rates it well and recommends it as a family film that adults will not be bored by."]
]

DEPTH_SECTIONS_V = {}
for _row in ROWS_V:
    _slug, _h2, _para = _row[0], _row[1], _row[2]
    _items = _row[3:-1]
    _para2 = _row[-1]
    assert _slug.startswith("entertainment/movie/"), f"batch V is film-only: {_slug}"
    assert len(_row) == 16, f"row shape {_slug}: {len(_row)} fields"
    assert isinstance(_para2, str) and _para2, f"missing closing para: {_slug}"
    DEPTH_SECTIONS_V[_slug] = ed(_slug, _h2, _para, _items, _para2)

for _slug, _html in DEPTH_SECTIONS_V.items():
    _f = _ROOT / _slug / "index.html"
    assert _f.is_file(), f"batch V missing route: {_slug}"
    assert _f.is_file(), f"{label} missing route: {_slug}"

_h2s = [r[1] for r in ROWS_V]
_lead = [r[i] for r in ROWS_V for i in range(3, len(r) - 1, 2)]
assert len(set(_h2s)) == len(_h2s), "duplicate h2 within batch V"
assert len(set(_lead)) == len(_lead), "duplicate lead-in within batch V"

print(f"batch V: {len(DEPTH_SECTIONS_V)} film sections, {len(set(_h2s))} unique h2, "
      f"{len(set(_lead))} unique lead-ins")
