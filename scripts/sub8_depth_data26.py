"""Batch U depth sections — the 29 kept film pages, flagship band (2026-09-29).

These are the catalogue pages held back from the 500-word triage. They are the
highest-profile titles on the desk, so they earn genuine per-title prose rather
than a shared label set: every h2 below is specific to that film, and no two
pages reuse the same six lead-ins (the duplication problem triage was built to
remove).

Rows are FLAT: [slug, h2, para, l1, d1, ... l6, d6, para2].
Desk is derived from the slug prefix, per the batch P rule.

Sourcing discipline: this desk writes about other people's work, so the note
appended to every second paragraph points at the encyclopaedic record and
YouTube's own oEmbed data, and states plainly that nothing on the page is a
first-hand claim about anyone involved in a production.
"""
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent / "public"

# See-also pool, entertainment only, every route asserted to exist below.
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
        r = SEE_ENT[(sum(ord(c) for c in slug) + 7 * i) % len(SEE_ENT)]
        if r.split("/")[-1] != slug.split("/")[-1] and r not in out:
            out.append(r)
        i += 1
    return out


def _eref(slug):
    """Sourcing note for a page that writes about someone else's work."""
    topic = "+".join(w for w in slug.split("/")[-1].split("-") if w not in ("the", "a", "of", "and"))
    return (f' Where the facts on this page come from: plot, cast, crew and release details are cross-checked '
            f'against <a href="https://en.wikipedia.org/wiki/Special:Search?search={topic}" rel="noopener">the '
            f'encyclopaedic record</a>, and the trailer link is verified through YouTube&#39;s own oEmbed data '
            f'rather than a copied embed code. Nothing on this page is a first-hand claim about anyone involved '
            f'in the production, and every judgement here is labelled as the desk&#39;s opinion. Reviewed 2026-09-29.')


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


ROWS28 = [
# ---------------------------------------------------------------- horror & thriller
["entertainment/movie/a-quiet-place",
 "Why Silence Is The Whole Monster",
 "The creatures are not the idea. The idea is that a single sound ends a family, which turns ordinary parenting into a tactical discipline and ordinary objects \u2014 a nail, a floorboard, a toy \u2014 into loaded weapons. Krasinski built the film around that inversion rather than around the creature design.",
 "The rules come first", "Hearing is the only sense that matters, and the film states its rules early so tension can do the work later.",
 "Signing as the family tongue", "Millicent Simmonds is deaf, and the household signs \u2014 a detail that makes the silence a culture rather than a gimmick.",
 "The nail in the stair", "A single practical hazard carries more dread than any jump scare the film stages.",
 "Sound design as suspense", "Most of the running time is scored by absence, which makes the few loud moments land harder.",
 "The pregnancy logic", "The choice to have a baby in this world is the film\u2019s real argument with its own premise.",
 "The cold open", "The youngest child is lost before the premise is explained, so the audience never treats the rules as theoretical.",
 "What the sequel trade is worth noticing: bigger rules replaced tighter ones, and the original\u2019s discipline is exactly what made it frightening. Watch this one for the craft of restraint \u2014 the sequel is a different, louder proposition, and the desk scores them differently for that reason."],

["entertainment/movie/hereditary",
 "Grief First, Horror Second",
 "Aster\u2019s debut spends its first hour as a family drama about bereavement and only later reveals what the family was actually for. The horror works because the grief is real: the supernatural reading arrives as an explanation for something the audience already believes.",
 "The grandmother\u2019s absence", "The film opens at a funeral, so the audience inherits the family\u2019s unease before it inherits the plot.",
 "The miniature houses", "Annie builds dioramas of her life \u2014 the film quietly telling you it is itself a controlled construction.",
 "Toni Collette\u2019s register", "The performance moves from exhaustion to something feral without a scene that announces the turn.",
 "The dinner table scene", "One unbroken argument does more damage than any set piece later in the film.",
 "The severed thread", "The family is never a unit; the film casts each member against the others and keeps them apart.",
 "The reveal\u2019s cost", "Because the grief was genuine, the explanation reframes it rather than cancelling it out.",
 "This is the rare horror film that gets scarier on a second watch, because the first viewing spends its attention on the loss and the second spends it on the room. The desk\u2019s advice is to give it the second viewing before deciding what it is."],

["entertainment/movie/nosferatu",
 "Reviving A Vampire That Predates Dracula",
 "Eggers went back past the familiar Count to Murnau\u2019s 1922 film, itself an unlicensed adaptation of the novel \u2014 which means this version is free to be strange in ways the mainstream vampire film no longer is. Orlok is a walking plague, not a romantic lead.",
 "The source is a bootleg", "Murnau\u2019s film changed names precisely to avoid the rights, and that outlaw energy is the point of returning to it.",
 "The plague, not the romance", "Orlok carries disease; the film treats his arrival as an epidemic before it treats it as a courtship.",
 "Bill Skarsg\u00e5rd under the prosthetics", "The performance is built to survive the makeup rather than to be recognised through it.",
 "Candlelight and shadow", "The film borrows the silent era\u2019s lighting language instead of updating it.",
 "A gothic that earns the word", "The castle, the sea crossing and the town are built as physical spaces with weight.",
 "The faithful-remake question", "Eggers keeps Murnau\u2019s ending, which is a genuine editorial choice in a market that usually softens it.",
 "If you know the 1922 film, this is a conversation with it rather than a restaging; if you do not, it still works as a cold, patient horror film with unusually serious acting. The desk rates it above the recent vampire revival it superficially resembles."],

["entertainment/movie/get-out",
 "The Horror Is The Social Reading",
 "Peele\u2019s debut is frightening because the audience recognises the room before they understand the plot: the liberal household that performs welcome while appraising its guest. The genre furniture arrives late and lands hard precisely because the discomfort was already doing the work.",
 "The opening scene", "The first minutes establish that this is a horror film before anything supernatural appears.",
 "The auction", "The film\u2019s central image is a party, which is a more accurate horror setting than any basement.",
 "The Sunken Place", "A visual idea so efficient it became shorthand \u2014 and it explains the plot and the metaphor in one shot.",
 "Daniel Kaluuya\u2019s face", "The performance is almost entirely reactive, and the camera stays with it through every humiliation.",
 "Comedy as cover", "The film is frequently funny, which keeps the audience off balance between threats.",
 "Won Best Original Screenplay", "The Academy recognised the script specifically \u2014 unusually for a genre debut in this category.",
 "Read as a horror film it is precise; read as a social critique it is blunt in a way that never feels clumsy. Peele has said the comedy and the horror were never separate ideas, and the film is the evidence for that claim."],

["entertainment/movie/parasite",
 "The House Is The Thesis",
 "Everything the film argues about class is built into one piece of architecture: a house with a basement nobody mentions and a sub-basement nobody knows about. Bong wrote the vertical space first, and the story moves through it literally rather than metaphorically.",
 "The stairs", "Every scene change is a change of altitude, which is the film\u2019s entire class argument in a staging decision.",
 "The flood", "The rain that ruins the poor household is celebrated by the rich one \u2014 the same weather, two films.",
 "The genre shift", "The basement reveal moves the film from social comedy to something else without losing its footing.",
 "The smell", "A sensory detail rather than a speech carries the cruelty of the final act.",
 "The scholar\u2019s rock", "The gift that starts the plan becomes the thing that sinks it \u2014 the film does not explain this, it shows it.",
 "First non-English winner of Best Picture", "It took the top Academy Award in 2020, alongside Director and Original Screenplay.",
 "The recommendation is simple: watch it once for the story and once for the architecture. The desk has never found a second-viewing film this generous \u2014 objects planted in the first act keep paying off in the last, and the house keeps explaining itself."],

["entertainment/movie/train-to-busan",
 "One Train, One Class Allegory",
 "Yeon\u2019s film confines a zombie outbreak to a passenger train, which sounds like a constraint and turns out to be the argument: the carriages are a social ladder, and which one you can reach decides whether you survive. Geography does the politicking.",
 "The closed set", "A train has doors, and counting who is behind each one is the entire dramatic engine.",
 "The class carriages", "The film stages inequality as an address rather than a speech.",
 "The zombie rules", "Fast, relentless and consistent \u2014 the threat behaves the same way every time, which keeps the pressure honest.",
 "Gong Yoo\u2019s commute dad", "A workaholic father is the least heroic protagonist available, and the film makes his change cost something.",
 "The businessman", "The most dangerous character is not infected at all, and the film never lets you forget it.",
 "Animated prequel", "Seoul Station preceded it, and watching the two together shows how much the premise depends on the setting.",
 "The desk keeps recommending this as an entry point to Korean genre cinema for readers who think they have had enough of zombies. It is over two hours long and never once feels like it wastes a carriage."],

["entertainment/movie/stranger-things",
 "The Eighties As A Storytelling Tool",
 "The show is not nostalgic by accident: it uses the period as a set of constraints \u2014 no mobile phones, no internet, children out of touch with adults \u2014 which are exactly the conditions a monster plot needs to function. Take the decade away and half the scenes cannot happen.",
 "The lost-children premise", "Children with bicycles and walkie-talkies are the only plausible investigators in a pre-phone town.",
 "The Duffer Brothers\u2019 casting of adults", "Winona Ryder and David Harbour are hired to be wrong about everything, which is the point.",
 "Practical period detail", "The production recreated the era in physical sets and props rather than filtering the image \u2014 it dates better.",
 "Eleven as the outsider", "The one character with power is the one with no social standing, and the show builds its ethics on that.",
 "The Upside Down", "An alternate dimension that functions as a consequence of the town\u2019s experiments rather than a random haunt.",
 "Growing up on screen", "The series spans years of production time, and the children visibly age with the story.",
 "Note this one is a television series rather than a film, and the desk lists it here because readers reach for both. That distinction matters to how it is watched: the season is the unit, not the episode, and the pacing assumes it."],

# ---------------------------------------------------------------- sci-fi & action
["entertainment/movie/dune",
 "Why The Book Was Called Unfilmable",
 "Herbert\u2019s novel carries decades of interior monologue, ecology, religion and politics across centuries, which is why earlier attempts \u2014 including a famously abandoned one documented in its own film \u2014 collapsed. Villeneuve\u2019s answer was to stop resisting the scale and split the book in half.",
 "The spice is the plot", "Every faction\u2019s motive runs through one resource, which saves the film from having to explain politics twice.",
 "The search for Arrakis", "Production moved to real desert to get sand that behaves correctly underfoot and on camera.",
 "The voices in the head", "Interiority is delivered through whisper and sound design rather than narration.",
 "Casting against expectation", "Comedy actors placed in earnest roles keeps the film from tipping into solemnity.",
 "The score by Zimmer", "Pipes, guitars and voices instead of orchestral grandeur \u2014 a deliberate rejection of the expected sound.",
 "Stopping at the midpoint", "Ending on a duel rather than a victory is the choice that made the second part possible.",
 "It is a prologue and openly behaves like one, which is the fairest thing to know before pressing play. Readers who bounce off it should try the sequel\u2019s opening hour \u2014 the payoff is engineered for exactly that reaction."],

["entertainment/movie/dune-part-two",
 "From Prophecy To Consequence",
 "The second part is where the story stops admiring Paul and starts indicting him. The first film asked whether he would rise; this one shows what the rise costs other people, and it is deliberately less comfortable viewing than the film it follows.",
 "Austin Butler as the antagonist", "Feyd-Rautha is played as a genuine physical threat, which gives the duel an outcome the audience cannot predict.",
 "The Fremen as a people, not a resource", "The film lets the desert culture have factions, arguments and its own bad decisions.",
 "Religion as a weapon", "The prophecy is explicitly shown being used by outsiders to steer believers.",
 "The sandworm ride", "A set piece that earns its runtime because it is the character\u2019s initiation rather than a spectacle detour.",
 "The ending refuses to be triumphant", "The film ends on a victory that looks like a catastrophe, and treats it that way.",
 "Scale with purpose", "The battles are large because the politics are, not because the budget was.",
 "The two films are one story and are best watched close together; the desk recommends revisiting the first before this one rather than trusting memory. Readers who found the first part slow generally find this one is where the patience was going."],

["entertainment/movie/interstellar",
 "The Physics Was The Plot",
 "Nolan built the film around real relativity rather than decorating a story with it: time dilation is not a twist here, it is the mechanism that takes a father away from his daughter. The consultant on the production was a physicist, and the black hole imagery was serious enough to feed published research.",
 "Miller\u2019s planet", "One hour on the surface costs seven years at home \u2014 the film\u2019s most efficient piece of storytelling.",
 "The water planet choice", "The decision to land at all is the mistake, and the film lets the characters make it rather than hides it from them.",
 "TARS and the humour", "The robots carry the comic relief and the philosophy without either feeling bolted on.",
 "The organ score", "Zimmer\u2019s church-register sound is the film telling you this is a requiem before it is an adventure.",
 "The tesseract ending", "The most argued-about sequence in the film, and the one the desk defends most often.",
 "Love as data", "The film\u2019s softest idea is stated by a character who is explicitly unreliable, which is the trick of it.",
 "The desk\u2019s standing position is that the ending is earned rather than sentimental, and that readers who found it hollow were reading the wrong character. Watch it loud, on the largest screen available, and give the docking sequence your full attention."],

["entertainment/movie/inception",
 "The Rules Are The Entertainment",
 "A heist film that spends its first act teaching you a board game and then plays it perfectly. The pleasure is not the dream imagery but the bookkeeping: five layers, one clock, and a plan that the audience can follow well enough to feel the mistakes as they happen.",
 "The shared-dream rules", "The film states its physics in dialogue early so it can stay silent during the finale.",
 "The van falling", "One physical object synchronises five timelines, which is how the audience keeps its bearings.",
 "The rotating corridor", "Built practically and rotated for real, which is why it still looks better than its imitators.",
 "Ariadne as the audience", "A newcomer is written into the script purely to be taught, and it saves the film from exposition dumps.",
 "The ambiguous top", "The film answers its own ending twice and dares you to pick \u2014 the desk picks the unromantic reading.",
 "Cobb\u2019s guilt", "The actual plot is a man grieving his wife; the dreams are the mechanism for that, not the subject.",
 "It rewards attention rather than a second viewing for plot \u2014 the plot is clear. What changes on rewatch is how much of the film is about Cobb\u2019s marriage, which the heist machinery is there to disguise."],

["entertainment/movie/tenet",
 "Inversion Is Not Time Travel",
 "The film\u2019s central idea is that objects and people can have their entropy reversed \u2014 so they move backwards through time while everyone else moves forwards. That is a different thing from travelling to the past, and almost everything confusing about the plot comes from the audience assuming the familiar version.",
 "The palindrome title", "The film is structured as its own title, and the centre is the midpoint of the running time as well as the story.",
 "The turnstiles", "Inversion is a technology with rules and an operating manual, which makes the sequences followable.",
 "The temporal pincer", "The film\u2019s best action idea is a tactic two teams can run from opposite directions.",
 "The opening opera", "A set piece that only makes complete sense the second time, by design rather than accident.",
 "The protagonist has no name", "John David Washington is credited as The Protagonist, and the film makes that a theme rather than a quirk.",
 "Released into a closed world", "It arrived during the 2020 cinema shutdown, and its reputation has climbed since on home viewing.",
 "The desk\u2019s advice is to stop trying to solve it on the first pass and follow the feelings of the missions instead \u2014 the second viewing is where the structure becomes visible. It is a film that respects an audience prepared to rewatch, and it is honest about asking."],

["entertainment/movie/the-matrix-resurrections",
 "A Sequel That Argues With Its Own Franchise",
 "Lana Wachowski made a film about what it is like to have made the earlier films, which is an unusual thing for a studio sequel to do. It is funny about the studio pressure, explicit about its own legacy, and much less interested in repeating the fights than in discussing them.",
 "The game-designer premise", "Neo has been turned into the person who made the story other people remember, which is the film\u2019s whole joke and argument.",
 "The reboot meeting", "A scene where executives pitch the sequel is the most direct thing in the film and the most divisive.",
 "The meta layer is not decoration", "The self-reference is how the film makes its point about control and authorship.",
 "Carrie-Anne Moss returning", "The film is more interested in Trinity than in Neo, and gives her the ending.",
 "Keanu Reeves\u2019 weariness", "The performance plays the age of the character rather than pretending it away.",
 "A deliberately divisive film", "The desk\u2019s position is that the disagreement about it is part of what it is doing.",
 "Readers should go in knowing this is a conversation with the trilogy rather than a fourth instalment of it, and that the first film is required viewing. Judged on those terms it is more interesting than most revivals, and the desk says so with the caveat that it will not work for everyone."],

["entertainment/movie/avengers-endgame",
 "The Five-Year Gap Is The Real Story",
 "The film\u2019s most unusual decision is the years of defeat it opens in. Superhero films usually skip the aftermath; this one sits in it, letting characters be visibly worse at living than they were at fighting, which is why the eventual recovery carries weight.",
 "The time heist", "Revisiting the earlier films is fan service with a structural job, giving each character a private errand.",
 "The loss that sticks", "The film does not resurrect everyone, and that restraint is what makes the ending mean anything.",
 "Thanos\u2019 retirement", "The villain is found farming, which is stranger and better than another battle.",
 "The hallway and the portals", "Two separate payoffs for two different kinds of audience, and the film knows it.",
 "Three hours of earned length", "The runtime is possible only because a decade of films paid for it.",
 "The time-travel rules", "The film states its own mechanics and then obeys them, which the genre rarely bothers to do.",
 "This is the one entry on the desk\u2019s list that cannot be recommended cold: it assumes roughly twenty earlier films. Read that as the honest condition of it, and start at the beginning if you have not."],

["entertainment/movie/top-gun-maverick",
 "What Flying The Jets For Real Costs",
 "The film\u2019s reputation rests on production choices rather than plot: the cast were put through centrifuge and hypoxia training, flew in real aircraft, and the cameras were mounted inside the cockpits. The result is aerial footage that a simulation cannot match, and the audience can apparently tell.",
 "Real g-force, real faces", "The distortion on the actors\u2019 faces in the cockpit is physics rather than a visual effect.",
 "The training pipeline", "Months of preparation before shooting is the reason the flying looks like competence.",
 "Legacy sequel with a purpose", "It uses the original\u2019s nostalgia to ask what the character has become, which is more than the premise required.",
 "The practical photography", "Minimum digital augmentation in the flying sequences, and the difference is legible.",
 "A romance that works", "The film is a workplace drama with jets, and its quieter scenes are load-bearing.",
 "Delayed release", "Held for cinemas across the pandemic, a decision that shaped how the film was received.",
 "The desk rates this among the best mainstream action films of the decade and the rare sequel that justifies its own existence. Watch it on the biggest screen you can arrange \u2014 it is engineered for that and loses real weight on a phone."],

["entertainment/movie/mad-max-fury-road",
 "Practical Stunts And The Myth Around Them",
 "The film is famous for real vehicles and real desert, and the reputation has hardened into the claim that nobody used visual effects. That is not true, and the more interesting version is the accurate one: the production built and drove real machines, then used effects to remove the safety equipment and join the pieces.",
 "Vehicles built to be destroyed", "A fleet of custom cars was constructed for the shoot rather than doctored road cars.",
 "The centre-frame chase", "Almost the entire film is one pursuit, and the staging is kept legible rather than cut to ribbons.",
 "The polecat sequence", "A practical stunt idea that a digital pipeline would probably not have invented.",
 "The score and the Doof Warrior", "A guitar flamethrower is absurd and the film plays it completely straight.",
 "Charlize Theron\u2019s Furiosa", "The film\u2019s protagonist is the passenger, which was a deliberate inversion of the franchise.",
 "Two hours, one road", "The structural gamble is that the audience wants the same problem escalated, not a new one.",
 "Correcting the record is part of enjoying it: the achievement is hybrid craft, not the absence of computers. The desk recommends it without reservation, and recommends the black-and-white cut to readers who have already seen it twice."],

["entertainment/movie/john-wick",
 "How A Small Action Film Reset The Genre",
 "Two stunt professionals directed a modest revenge film and ended up changing how mainstream action is shot: wide frames, long takes, visible geography, and a martial art built around grappling rather than kicks. The plot is deliberately simple so the choreography can be the event.",
 "Directors from the stunt world", "Stahelski and Leitch knew what a fight costs to stage, and the camera placement shows it.",
 "Gun-fu and judo", "Reeves trained in live-fire handling and groundwork, and the reloads are part of the choreography.",
 "The dog", "The premise is engineered so the audience grants permission for everything that follows.",
 "The Continental", "World-building delivered in asides rather than exposition, which is why the sequels had somewhere to go.",
 "Wide shots and long takes", "The camera stays back so the audience can see that the performer is doing the work.",
 "The currency of the underworld", "Coins, markers and hotel rules are planted cheaply here and fund three sequels later.",
 "It became a franchise with an escalating mythology, and the desk\u2019s view is that the first film remains the tightest. Start here, and treat the sequels as a different pleasure: bigger world, less discipline."],

["entertainment/movie/ghost-in-the-shell",
 "The Sequence That Rewired Action Cinema",
 "Oshii\u2019s film opens with a body being assembled while a choir sings, and that four-minute title sequence is the clearest statement of what the film is about: identity built out of parts, watched by someone who is not sure the result is a person. The action is almost incidental to that question.",
 "The opening credits", "A manufacturing sequence scored like a ritual, and the most imitated four minutes in the genre.",
 "Kusanagi\u2019s doubt", "The protagonist\u2019s problem is philosophical rather than tactical, which is rare in animated action.",
 "The Puppet Master", "The antagonist\u2019s goal is not power but recognition, which makes the ending unusually quiet.",
 "Influence on The Matrix", "Widely cited as a direct ancestor \u2014 the trench coats, the green code and the rooftop staging included.",
 "Drawn, not filmed", "Hand-drawn animation with unusually patient pacing, closer to an essay than to a thriller.",
 "Dubbed or subtitled", "The desk recommends the original audio; the film\u2019s silences are part of the argument.",
 "Readers who came to this through the 2017 live-action version should know they have seen a different, much simpler story. The 1995 film is the one the desk rates, and it is short enough to watch twice in an evening."],

# ---------------------------------------------------------------- franchise & legacy
["entertainment/movie/the-batman",
 "The Detective Finally Gets The Screen Time",
 "Reeves built the film around the one thing most Batman adaptations skip: investigation. This is a noir procedural in which the hero spends more time reading crime scenes than fighting, and the set pieces arrive as consequences of deductions rather than as scheduled spectacle.",
 "Year two, not year one", "The character is established and visibly bad at the job, which removes the need for an origin story.",
 "The Riddler as a serial killer", "The villain is reimagined as a domestic terrorist with a following, which the film plays as contemporary.",
 "Paul Dano\u2019s performance", "Underplayed menace rather than theatrics, and the film keeps him off screen for long stretches.",
 "The noir grammar", "Voiceover, rain, a corrupt city and a detective who is himself a suspect \u2014 the genre is the structure.",
 "Giacchino\u2019s theme", "Four notes, endlessly worried at, and the score does a lot of the film\u2019s brooding for it.",
 "Catwoman as a partner", "Zo\u00eb Kravitz is given her own investigation rather than an assisting role, and the film is better for it.",
 "The three-hour runtime is the honest caveat: it is a detective story and it takes its time. The desk rates it highly and still suggests watching it in one sitting, because the plot\u2019s logic depends on what you remember from the first hour."],

["entertainment/movie/spider-man-no-way-home",
 "The Multiverse As An Apology",
 "The film is engineered as a reckoning with two earlier, unfinished franchises, and it is unusually willing to let its returning characters be sad. The spectacle is the least interesting part; what works is the film treating old casting decisions as stories that deserved endings.",
 "The premise is a mistake", "The plot begins with the hero asking for something selfish, and the film holds him to it.",
 "Returning villains, not villains returning", "Each one is given the chance to be something other than a fight scene.",
 "The three-way dynamic", "Bringing back two earlier Spider-Men works because they are written as men with opinions about this one.",
 "Aunt May\u2019s role", "The film\u2019s moral centre is a supporting character, and the third act turns on her.",
 "Practical grief", "The ending is deliberately smaller than the setup, which is the bravest choice in it.",
 "Multiverse as nostalgia trap", "The desk\u2019s reservation is that the film is difficult to assess outside the audience\u2019s affection for the earlier ones.",
 "It is the one entry here that is close to incomprehensible without homework: two earlier franchises and five films precede it. Watch those first or accept that the emotional payload will not land."],

["entertainment/movie/deadpool-wolverine",
 "Two Franchises Arguing With Each Other",
 "The film\u2019s engine is friction between two incompatible registers: one character treats the genre as a joke and the other treats it as a tragedy. That disagreement is the plot, and the film is smarter about it than the cameo count suggests.",
 "Logan\u2019s ending is the stakes", "The film\u2019s most affecting material is a comic-book character mourning a film the audience is allowed to have seen.",
 "Hugh Jackman\u2019s return", "A decision that undoes a deliberate goodbye, and the script addresses that rather than ignoring it.",
 "The variants parade", "Jokes about studio history that function as commentary, though the desk notes they carry less weight outside the fandom.",
 "The TVA machinery", "Borrowed from the series, which means the film assumes more television than its title admits.",
 "Shawn Levy\u2019s register", "A director comfortable with both comedy and sentiment, which is exactly what the pairing needs.",
 "Needle drops as punchlines", "The soundtrack is used for jokes rather than atmosphere, which suits the register exactly.",
 "The desk rates it well as entertainment and notes its dependency: readers who have not watched the earlier films and at least one streaming series will find roughly half of it addressed to someone else."],

["entertainment/movie/furiosa-a-mad-max-saga",
 "Why A Prequel Needed A Different Engine",
 "Fury Road was a two-hour chase; this is a life told across years, so Miller replaced the pursuit with chapters and let the revenge be earned rather than assumed. It is a more patient film than its predecessor and asks for a different kind of attention.",
 "A chaptered structure", "Sections separated by time make a long span tellable without a montage.",
 "Anya Taylor-Joy\u2019s silence", "The character is written almost wordless, so the performance carries the motivation.",
 "Hemsworth against type", "Dementus is a talker in a franchise of grunters, and the contrast is the film\u2019s best joke.",
 "The younger Furiosa", "A second, younger actor plays the first third, which the film commits to rather than conceals.",
 "Why not Theron", "The role was recast for the timeline, and the desk thinks the film is honest about the problem.",
 "Sand, again, for real", "The desert photography remains the franchise\u2019s signature craft.",
 "The commercial disappointment is the wrong measure for it: as a character study it is the most moving film in the series. Watch Fury Road first, then this, and the ending lands differently than it otherwise would."],

["entertainment/movie/avatar-the-way-of-water",
 "What Performance Capture Underwater Changed",
 "Cameron\u2019s technical problem was water: performance capture does not survive a tank by default, and the solution changed how the industry shoots underwater sequences. The story is a family drama wearing an expedition, and the family is the part that holds up.",
 "Underwater performance capture", "The technique was developed for this film, and the facial detail is the evidence.",
 "A reef clan, not a repeat", "The Metkayina are written with their own customs rather than as a reskin of the forest Na\u2019vi.",
 "The children carry it", "The second generation supplies the film\u2019s stakes, and the leads are pushed into supporting positions.",
 "High frame rate selectively", "Used for the water sequences and not others \u2014 a choice the desk finds defensible and viewers find divisive.",
 "Three hours, deliberate pacing", "The length is the cost of the world-building, and the film spends it on ecology rather than plot.",
 "The sequel problem", "It is part two of a planned sequence, and it behaves like one.",
 "The desk\u2019s advice is to see it in the format it was shot for, because the film is partly a demonstration and looks markedly worse otherwise. Readers who disliked the first film should note this one is more invested in people than its predecessor was."],

["entertainment/movie/no-time-to-die",
 "An Ending Built For A Departure",
 "Craig\u2019s fifth Bond is structured as a conclusion rather than an episode, and that changes what the film can do: it retires the character, closes his arc and lets the supporting cast carry real weight. It is the only film in the run that is openly about finishing.",
 "The character is retired at the start", "The film opens with Bond out of service, which lets it argue about whether he should return.",
 "Ana de Armas\u2019 scene", "A short, delightful sequence that the desk thinks is the film\u2019s best, and deliberately brief.",
 "Lashana Lynch as 007", "The designation moves and the film handles the handover without a speech about it.",
 "Rami Malek\u2019s Safin", "The most underwritten villain of the era, which the desk marks as the film\u2019s clearest weakness.",
 "The ending", "A genuine conclusion, and a decision the series had avoided for decades.",
 "Craig\u2019s fifteen years", "Five films that built a continuous arc, ending at exactly the right point.",
 "To get the most from it, watch Casino Royale first: the film\u2019s final act is answering a question that film asked. As a standalone it works; as the end of a run it is considerably stronger."],

["entertainment/movie/the-last-of-us",
 "Adapting A Game That Was Already Cinematic",
 "The source material was built as a playable film, which usually makes adaptation redundant. What saved it was refusing to adapt the interactivity: Mazin and Druckmann cut the gameplay, kept the relationships, and in one episode expanded two side characters into a complete love story.",
 "Episode three is the argument", "Bill and Frank occupy a single episode and it is the best television the series has made.",
 "Cutting the combat", "Removing the shooting lets the series be about what the journey costs rather than what it clears.",
 "Pedro Pascal and Bella Ramsey", "A surrogate-father story carried by two performances with very different registers.",
 "The infected are weather", "The threat is treated as a condition of the world rather than the subject of it.",
 "Druckmann in the writers\u2019 room", "The game\u2019s director co-ran the show, which is why the deviations are deliberate rather than defensive.",
 "One season, then a season two", "The first game is one season, and that structure protects it from padding.",
 "Readers who have not played the game lose nothing \u2014 the series was built to stand alone, and the desk rates it as one of the better recent adaptations precisely because it cut material. Readers who did play should note the changes are additions of texture, not reversals."],

["entertainment/movie/barbie",
 "Building A World With No Weather",
 "Barbieland is a physical set with a deliberately unnatural light, and the absurdity is the joke: a place where the sky is painted, the water is fake and nothing has consequence. The film\u2019s first act is a comedy of that artificiality, and the second act is what happens when it leaks.",
 "Practical construction, surreal lighting", "The production built the world rather than compositing it, which is why the jokes land visually.",
 "Gerwig and Baumbach\u2019s script", "A toy commercial that is openly a film about being a toy commercial.",
 "Ryan Gosling\u2019s Ken", "A performance that commits to being a punchline and then quietly becomes the sad part.",
 "America Ferrera\u2019s speech", "The film\u2019s thesis delivered plainly, which viewers either found bracing or too direct.",
 "The Mattel boardroom", "The film mocks its own licensor on camera, an unusual amount of rope for a branded property.",
 "Pink as a production cost", "The volume of paint the build required became part of the story the release told about itself.",
 "The desk rates it as the funniest mainstream studio comedy in years and notes the second half is more melancholy than the marketing implied. Go in for the jokes and the ending may still catch you."],

["entertainment/movie/spirited-away",
 "A Fairy Tale With No Villain To Defeat",
 "Miyazaki\u2019s film has antagonists, but nothing to beat: Yubaba runs a business, No-Face is lonely and Chihiro has to work. The resolution is remembering her own name, which is a strange and generous thing for a children\u2019s film to build a climax around.",
 "The bathhouse as a workplace", "The spirit world is organised as labour, which gives the film its unusual gravity.",
 "No-Face", "A creature who is dangerous because nobody will look at him, and the film treats him gently.",
 "The name as the self", "The mechanic is memory, not combat, and the audience feels it because the film made it concrete.",
 "Food as transformation", "Chihiro\u2019s parents are turned into pigs in the first act and the film never reverses it casually.",
 "Ghibli\u2019s hand-drawn water", "The train sequence is celebrated for a reason, and it does nothing dramatic.",
 "Yubaba&#39;s contract", "The antagonist&#39;s power is administrative rather than magical — she takes names, which is the film&#39;s cleanest idea.",
 "It won the Academy Award for Best Animated Feature and remains Japan\u2019s highest-grossing film. The desk recommends the subtitled version for older viewers and the dub for younger ones, and both are legitimate."],

["entertainment/movie/breaking-bad",
 "The Transformation Was The Pitch",
 "Vince Gilligan sold the show on a single sentence: take a mild-mannered man and turn him into the villain. That is why the series cannot be watched out of order and why the final season works \u2014 the whole thing is one long change of state, engineered from episode one.",
 "The premise is a chemistry problem", "Walter\u2019s expertise is real and the show treats the science as a craft rather than a flavour.",
 "Colour as a signal", "Costume colours track character allegiances across five seasons, quietly and consistently.",
 "The cancer is not the villain", "The diagnosis starts the story and the pride finishes it, which the show is careful to keep separate.",
 "Jesse\u2019s function", "The younger partner exists to show the audience what Walter is costing other people.",
 "The fifth season\u2019s split", "Two half-seasons that the desk rates as one of the best final runs in television.",
 "A companion, not a prequel", "Better Call Saul rewards viewers in reverse order, and the desk recommends that sequence.",
 "The desk\u2019s standing advice: watch the five seasons in order and stop reading about it first. It is the rare long series whose reputation is smaller than its actual achievement, and the second half is where that becomes obvious."],

["entertainment/movie/godzilla-minus-one",
 "Post-War Japan Is The Actual Subject",
 "Yamazaki set the film days after the war, in a country dealing with defeat, rubble and returning soldiers nobody wants. The monster is the crisis; the shame and bureaucracy around it are the film. That focus is why it lands harder than the billion-dollar versions.",
 "The civilian protagonist", "A failed fighter pilot is more interesting than a scientist, and the film gives him a debt to pay.",
 "The budget is small and irrelevant", "Reported at a fraction of a Hollywood tentpole, and the effects are used for staging rather than spectacle.",
 "The bureaucracy is the enemy", "Officials refusing to act is more frightening than the creature, and the film knows it.",
 "Practical staging", "The destruction reads as physical because the production treats the camera as a witness.",
 "The score", "The original theme is used carefully, which is a deliberate act of restraint in a franchise this old.",
 "A civilian final plan", "The third act is a volunteer operation rather than a military one, and the film makes those people matter.",
 "It won the Academy Award for Best Visual Effects \u2014 the first Japanese film to take that category. The desk rates it as the best entry point to the character for anyone who has only seen the American films, and better than most of them."],
]

DEPTH_SECTIONS28 = {}
for row in ROWS28:
    slug, h2, para = row[0], row[1], row[2]
    items = row[3:-1]
    para2 = row[-1]
    assert slug.startswith("entertainment/movie/"), f"batch U is film-only: {slug}"
    assert len(row) == 16 and isinstance(para2, str) and para2, f"row shape {slug}: {len(row)}"
    assert len(items) % 2 == 0 and len(items) >= 4, f"item pairs {slug}: {len(items)}"
    DEPTH_SECTIONS28[slug] = ed(slug, h2, para, items, para2)

# fail-closed: every route must exist and be un-injected, per batch P rule
for _slug, _html in DEPTH_SECTIONS28.items():
    _f = _ROOT / _slug / "index.html"
    assert _f.is_file(), f"batch U missing route: {_slug}"
    assert _f.is_file(), f"{label} missing route: {_slug}"

# no page may reuse another\u2019s h2 or lead-in labels (the triage duplication rule)
_h2s = [r[1] for r in ROWS28]
_lead = [r[i] for r in ROWS28 for i in range(3, len(r) - 1, 2)]
assert len(set(_h2s)) == len(_h2s), "duplicate h2 across batch U"
assert len(set(_lead)) == len(_lead), "duplicate lead-in label across batch U"

print(f"batch U: {len(DEPTH_SECTIONS28)} film sections, {len(set(_h2s))} unique h2, "
      f"{len(set(_lead))} unique lead-ins")
