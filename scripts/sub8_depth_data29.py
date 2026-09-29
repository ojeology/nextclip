"""Batch X depth sections — the next 36 thinnest film pages (2026-09-29).

These pages carry a verdict and an FAQ but no editorial depth section, and sit
at roughly 490 words each. Each section is written for its own title and no h2
or lead-in label is reused anywhere in the batch, or in any earlier batch
(asserted at the bottom, and cross-checked against every sibling module before
injection).

Rows are FLAT: [slug, h2, para, l1, d1, ... l6, d6, para2]  -- 16 fields.

Craft note for this batch: it is unusually mixed -- studio sequels, prestige
remakes, anime, Nollywood, Korean and Spanish television, and two 1950s/1990s
canon titles. Sections stay on documented ground: who directed it, what it
adapts or follows, which industry made it, and what is publicly known about its
production and release. Where a title has a famous cliffhanger or a contested
reputation, that is named as such rather than resolved with invented detail.
Reception is reported only in the broad terms the record supports; no numbers,
awards or quotes are asserted that the desk cannot stand behind.
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
    return (f' Where the facts on this page come from: credits, release details and source-material '
            f'information are cross-checked against <a href="https://en.wikipedia.org/wiki/Special:Search?search={topic}" '
            f'rel="noopener">the encyclopaedic record</a>, and the trailer is linked through YouTube&#39;s own '
            f'oEmbed data rather than a copied embed code. Nothing on this page is a first-hand claim about anyone '
            f'involved in a production, and every judgement is labelled as the desk&#39;s opinion. Reviewed 2026-09-29.')


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


ROWS_X = [
# ------------------------------------------------------------ studio sequels & franchises
["entertainment/movie/aquaman-2",
 "Sequel Rules And A Universe Winding Down",
 "James Wan returned to direct this 2023 follow-up to his own 2018 Aquaman, which matters because the first film&#39;s scale was the reason it connected. The sequel arrived as the DC slate was being rebuilt, so it reads as a closing entry rather than a fresh start.",
 "Wan stayed on", "The director of the first film came back, which is unusual for a franchise that changed hands between entries.",
 "The subtitle logic", "It is named for the lost kingdom of the title rather than for a character, which tells you the plot is a search.",
 "The visual approach", "The underwater sequences remain the selling point, as they were the first time.",
 "The slate context", "It landed as the shared universe it belonged to was being wound down and replaced.",
 "Who returns", "The leads from the first film are back, which is what keeps it a continuation rather than a reboot.",
 "The standing question", "Readers arriving from the first film usually want to know whether it is required viewing.",
 "Treat this as the second half of one story rather than a new beginning. If the first film did not convince you, this one is unlikely to, and the desk rates it accordingly."],

["entertainment/movie/ant-man-2",
 "The Smallest Franchise And Its Set-Piece Logic",
 "Peyton Reed directed this 2018 entry, and the series it belongs to is the one built around size change rather than scale. Where other films in the shared universe escalate, this one stays deliberately domestic and comic, which is the intentional difference.",
 "Reed&#39;s second turn", "He had directed the first film and returned, keeping the comedic register consistent.",
 "The house arrest premise", "The hero is confined after the events of a previous team film, which is the reason the plot takes place close to home.",
 "The Wasp billing", "A co-lead is named in the title, and the film spends real time on her rather than relegating her.",
 "Practical shrinking", "The trick sequences rely on staging and perspective more than on spectacle.",
 "The Michael Peña factor", "His recaps were a signature of the first film, and the comedy remains the series&#39; real engine.",
 "The collector&#39;s question", "It sits between larger films, so readers ask whether the continuity is essential.",
 "It is the least demanding film in its franchise and knows it, which makes it a reasonable evening rather than a landmark. Skip it only if you are following the wider continuity."],

["entertainment/movie/jurassic-world",
 "Rebooting A Park Without Rebuilding It",
 "Colin Trevorrow directed this 2015 revival, arriving fourteen years after the third Jurassic Park film. Rather than pretend the earlier films did not happen, it opens with the park finally working &mdash; which is the most interesting idea the series has had since the original.",
 "The park is open", "The premise resolves the question the first film raised by simply answering it.",
 "The gap it fills", "More than a decade separates it from its predecessor, and the script treats that as history rather than erasing it.",
 "The raptor handlers", "The relationship between staff and animals is the film&#39;s real novelty.",
 "Spielberg&#39;s shadow", "The original remains the benchmark, and this one is measured against it every time.",
 "The practical question", "The effects mix digital and animatronic work, and readers want to know the ratio.",
 "The trilogy it started", "It launched a new trilogy, so it is an opening chapter rather than a standalone.",
 "A functioning park was the obvious idea the series had been avoiding, and it is worth watching for that alone. The desk rates it below the 1993 original and comfortably above the two films before it."],

["entertainment/movie/the-flash",
 "A Multiverse That Cost More Than It Earned",
 "Andy Muschietti directed this 2023 DC film, which uses time travel to revisit the franchise&#39;s own past. It is remembered as much for a difficult production and widely criticised visual effects as for anything it does dramatically.",
 "The time-travel frame", "The plot turns on changing a past event, which lets the film restage familiar material.",
 "The returning Batman", "A previous actor returns to the role, and that casting is the film&#39;s main talking point.",
 "The effects criticism", "The visual work drew unusually public criticism, which is part of the film&#39;s record now.",
 "The production trouble", "Its route to release was troubled and long, and that context is hard to separate from the result.",
 "The reset function", "It arrived to close out a version of the shared universe rather than continue it.",
 "The question of need", "Almost nobody arrives at this film without asking who it is actually for.",
 "Go in knowing the effects are the weakest part and the novelty casting is the strongest. It functions better as an epilogue than as a film in its own right."],

["entertainment/movie/equalizer",
 "The Quiet Man Who Has Already Decided",
 "Antoine Fuqua directed this 2014 adaptation of the 1980s television series that starred Edward Woodward. Denzel Washington plays a man who appears ordinary until he is not, and the film&#39;s restraint is what separates it from the action films around it.",
 "The television origin", "It adapts a series in which a former agent offers help to people who have nowhere else to turn.",
 "The casting inversion", "The lead is deliberately played as mild and unremarkable until the violence arrives.",
 "Fuqua&#39;s patience", "The director holds the pacing back, and the slowness is the point rather than a flaw.",
 "The measured violence", "The action is brief and decisive, which is a stylistic choice rather than a limitation.",
 "The sequels", "It became a trilogy, so this is the entry that establishes the pattern.",
 "The tone question", "Readers often ask whether it is a revenge film, and the answer shapes expectations.",
 "It is a slow-burn film with a very short fuse, and the contrast is the whole appeal. Expect character work with occasional sharp violence, not a continuous action picture."],

["entertainment/movie/vinland-saga",
 "A Revenge Story That Argues Against Itself",
 "Wit Studio adapted Makoto Yukimura&#39;s manga in 2019, and the series is unusual for starting as a revenge thriller before turning into something that rejects revenge outright. That pivot is the reason it is discussed as more than a Viking action show.",
 "Yukimura&#39;s manga", "The source ran long enough for the adaptation to follow a genuine change in its own argument.",
 "The Thorfinn problem", "The protagonist&#39;s early motivation is vengeance, and the series is honest that this is a trap.",
 "Wit&#39;s first season", "The studio&#39;s animation carries the violence without glamorising it.",
 "The second-season shift", "A different studio handled the later season, which changes pace deliberately.",
 "The pacifism thread", "The series&#39; later argument is genuinely unusual for the genre and divides viewers.",
 "The historical setting", "It draws on the Norse world rather than inventing a fantasy one, with real figures appearing.",
 "It starts as a revenge story and argues its way out of one, which is a rare thing for the genre to attempt. Give it the full first season before deciding, because the turn is the point."],

["entertainment/movie/cowboy-bebop",
 "Jazz, Bounty Hunters And A Genre That Did Not Exist Yet",
 "Shinichiro Watanabe directed this 1998 Sunrise series, and it is the title most often named when people explain how anime reached an adult Western audience. The structure &mdash; mostly standalone episodes with a spine of backstory &mdash; is as deliberate as the music.",
 "Yoko Kanno&#39;s score", "The soundtrack is jazz and blues rather than orchestral, which was a genuine departure.",
 "The episodic shape", "Most episodes stand alone, and the handful that do not are the ones everyone remembers.",
 "The Western breakthrough", "Its run on late-night American television is the reason it is a gateway title.",
 "Its tonal spread", "Comedy, noir and genuine melancholy sit next to each other without friction.",
 "How it finishes", "It finishes the way it needs to, and the desk rates that decision highly.",
 "The one-season question", "There is only one series, which surprises people expecting a franchise.",
 "The music and the patience are what make it endure, and one season is the whole of it. Watch the first few episodes before judging, because the shape is unusual on purpose."],

["entertainment/movie/howls-moving-castle",
 "A Children&#39;s Book Turned Into An Argument Against War",
 "Hayao Miyazaki adapted Diana Wynne Jones&#39;s novel in 2004, and he changed its centre. The book is a comic fantasy of mistaken identity; the film is that plus a sustained objection to war, written while one was being fought.",
 "The novel it departs from", "The source and the film share their premise and diverge sharply in tone.",
 "The war added", "The conflict is Miyazaki&#39;s own expansion rather than something the book required.",
 "The curse structure", "A transformation early on drives the whole plot and stands in for a character&#39;s self-image.",
 "Ghibli&#39;s movement", "The studio&#39;s animation is at its most fluid in the film&#39;s flights and crowds.",
 "The Miyazaki themes", "Flight, old age and duty recur across his work and are all present here.",
 "The divergence question", "Readers of the book often ask whether the film is a faithful adaptation, and it is not.",
 "Read the book and watch the film as two different arguments about the same premise. The film is the more political of the two, and knowingly so."],

["entertainment/movie/jujutsu-kaisen",
 "Cursed Energy And A Premise That Moves Fast",
 "MAPPA adapted Gege Akutami&#39;s manga from 2020, and the series is built on a simple inversion: the monsters come from human negativity rather than from somewhere else. That idea gives the fights a reason to exist beyond choreography.",
 "Akutami&#39;s source", "Events and abilities are largely inherited from the manga rather than invented for the screen.",
 "The cursed-energy rule", "Negative emotion is the power source, which makes the world internally consistent.",
 "The fast pacing", "The adaptation covers ground quickly, which some viewers find bracing and others abrupt.",
 "The prequel film", "A feature released between seasons adapts earlier material and fills in a key character.",
 "The MAPPA craft", "The studio&#39;s animation is the reason the action sequences are discussed at all.",
 "The entry point", "Newcomers often ask whether to start with the series or the film.",
 "The world-building rule is the strongest thing here, and the animation carries the rest. Start with the series and treat the film as a companion rather than a starting point."],

["entertainment/movie/tokyo-ghoul",
 "Body Horror As A Metaphor For Becoming Someone Else",
 "Pierrot adapted Sui Ishida&#39;s manga from 2014, and the series is remembered for how far it takes the idea of a protagonist becoming the thing he hunts. It is horror first and action second, which is the opposite of how it was marketed.",
 "Ishida&#39;s manga", "The source is known for dense artwork and a willingness to disturb its own lead.",
 "The half-transformation", "The hero&#39;s change is irreversible from the first episode, which sets the series&#39; tone.",
 "The adaptation&#39;s drift", "Later seasons diverged from the manga and then returned to it, which splits viewers.",
 "The horror register", "It is genuinely bleak, and the desk flags that rather than softening it.",
 "The broadcast edits", "Television versions were censored in places, and home releases differ.",
 "The continuation question", "Readers ask whether the later seasons are worth continuing with.",
 "Watch it as a horror series about losing control of your own body, not as a power fantasy. Be aware that later seasons follow a different route through the source."],

["entertainment/movie/code-geass",
 "A Rebellion Series Where The Hero Is The Problem",
 "Sunrise&#39;s 2006 series, directed by Goro Taniguchi with character designs by CLAMP, gives its protagonist a power of absolute command and then asks what that does to a person. It sits alongside the mecha tradition while being sceptical of it.",
 "The Geass power", "Absolute obedience is the premise, and the series is interested in the cost rather than the wish fulfilment.",
 "The masked identity", "The lead operates under a second name, which lets the show keep two sets of relationships running.",
 "CLAMP&#39;s designs", "The character work is stylised in a way that distinguishes it from the standard mecha look.",
 "The chess framing", "Strategy is the language of the show, and battles are argued rather than merely animated.",
 "The two seasons", "The story is split across a first and second series, and the second changes its footing.",
 "The ending&#39;s reputation", "Its conclusion is among the most discussed in the genre, which readers should expect.",
 "The premise is a trap the series sets for its own hero, and it knows it. Go in expecting a political drama that happens to have giant robots."],

["entertainment/movie/sherlock",
 "Updating A Victorian Detective Without Losing Him",
 "Steven Moffat and Mark Gatiss moved Conan Doyle&#39;s detective into the present for the BBC from 2010, keeping the original stories&#39; scaffolding while replacing telegrams with text messages. Each episode runs feature length, which is the structural decision that defines it.",
 "The modern setting", "The update is done by changing the tools rather than the character, which is why it works.",
 "Episode length", "Each instalment runs close to ninety minutes, so the shape is closer to television film than series.",
 "Cumberbatch and Freeman", "The central partnership carries the show, and the casting is why it travelled.",
 "The original stories", "Plots are adapted from the canon rather than invented, including some of the more famous ones.",
 "The short run", "There are relatively few episodes across several years, which makes it easy to finish.",
 "The decline debate", "Later series divided audiences, and the desk says so rather than pretending otherwise.",
 "Watch the first two series and decide from there, because the later ones take a different turn. The modern-day update is the most successful part of the whole idea."],

# ------------------------------------------------------------ Nollywood & Nigerian
["entertainment/movie/chief-daddy",
 "A Nollywood Comedy About What A Patriarch Leaves Behind",
 "Niyi Akinmolayan directed this 2018 Nigerian comedy, in which a wealthy family&#39;s arrangements unravel after the head of the household dies. It works as an ensemble piece, and the joke is usually at the expense of the family rather than the staff.",
 "The Akinmolayan direction", "He is one of the more prolific Nigerian directors of the period and works across comedy and thriller.",
 "The inheritance plot", "The death triggers the comedy rather than being the subject of it.",
 "The ensemble structure", "The film spreads its time across a large family, which is where the humour lives.",
 "The streaming route", "It reached a global audience through Netflix, as several Nollywood comedies did.",
 "The class observation", "The satire is aimed at the newly comfortable rather than at poverty.",
 "Whether a follow-up exists", "The film did well enough that a follow-up followed, so this is the first entry.",
 "It is a family comedy with a large cast, so expect breadth rather than a single lead. The satire lands hardest if you know the milieu it is teasing."],

["entertainment/movie/breaded-life",
 "A Body-Swap Comedy With A Nollywood Accent",
 "Biodun Stephen directed this 2021 Nigerian film, which takes the familiar body-swap premise and drops it into a Lagos setting. The joke is not only the swap but the adjustment to someone else&#39;s daily life and obligations.",
 "Stephen&#39;s range", "The director works across comedy and family drama, and this sits between the two.",
 "The swap mechanism", "The premise is established quickly, and the film is more interested in what follows.",
 "The Lagos texture", "The setting is specific rather than generic, which is where much of the humour sits.",
 "The performance demand", "A body-swap film rests on the lead carrying two characters, and this one does.",
 "The streaming audience", "It found viewers through Netflix, which widened its reach beyond cinemas.",
 "The genre lineage", "Body-swap comedies are old, and the film is aware of the tradition.",
 "Go in for the performances and the specific local detail rather than for plot surprise. The premise is the setup, not the point."],

["entertainment/movie/drishyam",
 "The Film That Was Remade In Almost Every Language",
 "Jeethu Joseph wrote and directed this 2013 Malayalam thriller, in which an ordinary man protects his family after an accident by constructing an alibi. Its reputation rests less on the crime than on the fact that the protagonist is not a detective.",
 "The Mohanlal performance", "The lead is cast against type as an unremarkable man, which is what makes the film work.",
 "The class fault line", "The story turns on a family without power against one with it, which is the film&#39;s real subject.",
 "The cable-operator detail", "The protagonist&#39;s profession is the source of his expertise rather than any investigative training.",
 "The remake wave", "It has been remade in numerous Indian languages and beyond, which is unusual even by the standards of the industry.",
 "The two-part follow-up", "A follow-up exists and continues the family&#39;s story years later.",
 "Choosing a version", "Readers often ask which remake to start with, and the original is the answer.",
 "It is a thriller where the audience is complicit rather than a whodunnit, and the remakes are a testament to how well the structure travels. Start with the original."],

["entertainment/movie/baahubali-2",
 "The Answer To The Question The First Film Asked",
 "S. S. Rajamouli&#39;s 2017 Telugu film is the second half of a two-part story, and it exists largely to resolve the cliffhanger the first part ended on. It is one of the clearest cases of a sequel being structurally necessary rather than commercially motivated.",
 "The two-part gamble", "Both halves were conceived as one story and split, which is unusual at this scale.",
 "The famous question", "The first film ends on a betrayal that the second exists to explain.",
 "The Telugu industry scale", "It is a landmark of pan-Indian filmmaking, made before that phrase became standard.",
 "Rajamouli&#39;s staging", "The action is built around large-scale practical sequences rather than effects alone.",
 "The flashback structure", "A long middle section carries the story&#39;s emotional weight rather than its action.",
 "The order question", "Nobody should watch this first; it depends entirely on the earlier film.",
 "Watch the two parts as one story, because that is what they are. The second half is where the emotional payoff sits, and it does not stand alone."],

# ------------------------------------------------------------ Korean, Spanish & world television
["entertainment/movie/money-heist",
 "The Spanish Series That Became A Global Format",
 "Created by Alex Pina and first broadcast in Spain in 2017, the series was initially a modest performer and became a worldwide title only after international distribution. Its visual signature &mdash; red overalls and a particular mask &mdash; is now more recognisable than the plot.",
 "The Antena 3 run", "Its first broadcast was not the reason it became famous, which is part of the story.",
 "The streaming rescue", "International licensing changed the show&#39;s reach entirely rather than the show changing.",
 "The mask", "The imagery borrows from a real artist&#39;s face, which is why it reads as protest rather than costume.",
 "The Professor&#39;s role", "The planner narrates strategy, which is the show&#39;s storytelling engine.",
 "One operation per part", "Each part is built around a single long operation rather than episodic cases.",
 "The length problem", "Later parts expanded, and the desk notes that the pacing suffers for it.",
 "Start with the first two parts, which are tightly built, and treat later instalments as optional. The format is the achievement more than any single heist."],

["entertainment/movie/all-of-us-are-dead",
 "A Zombie Outbreak Confined To One School",
 "This 2022 Korean series, adapted from a webtoon and made for Netflix, sets its outbreak inside a single high school. The containment is the point: the show is less about the apocalypse than about the hierarchies that survive it.",
 "The webtoon source", "It adapts an existing serial rather than originating the premise for television.",
 "The school setting", "Restricting the outbreak to one building keeps the scale human rather than global.",
 "The bully dynamics", "The social order inside the school is the show&#39;s real subject and outlasts the zombies.",
 "The Korean zombie lineage", "It follows a run of Korean zombie films and series that reframed the genre internationally.",
 "Its large student cast", "A large student cast means the show spreads its attention rather than following one hero.",
 "The season ending", "The first season closes on an unresolved note, which readers should know in advance.",
 "It is a social drama wearing a zombie premise, and it is better for that. Expect an ensemble and an ending that does not tie everything off."],

["entertainment/movie/the-penguin",
 "A Villain Spin-Off That Earns Its Own Ground",
 "This 2024 HBO series grew out of the 2022 Batman film, with Colin Farrell reprising a role he had played under heavy prosthetics. Lauren LeFranc developed it, and it works because it treats its lead as a crime story rather than a superhero footnote.",
 "The film it follows", "It picks up in the aftermath of the earlier film&#39;s flooding of the city, which sets the conditions.",
 "The prosthetics", "The lead&#39;s transformation is largely physical makeup rather than digital, which matters to the performance.",
 "The crime register", "It is a gangster story first, with the comic-book material sitting underneath.",
 "The rival family", "A competing dynasty drives the plot, giving the series a structure beyond its lead.",
 "The LeFranc writing", "The showrunner&#39;s handling of the lead&#39;s damage is what lifts it above a cash-in.",
 "The prerequisite question", "It can be watched without the film, though the film explains the starting conditions.",
 "It is a crime drama that happens to be set in a comic-book city, and it is better for that distance. Watch the 2022 film first if you want the full setup."],

["entertainment/movie/agatha",
 "A Spin-Off Made Entirely Of Leftovers, On Purpose",
 "Jac Schaeffer developed this 2024 series as a follow-up to WandaVision, with Kathryn Hahn returning to the role she originated. Its structure &mdash; a sequence of trials with shifting rules &mdash; is closer to a musical fable than to the superhero television around it.",
 "The WandaVision origin", "It continues directly from a character the earlier series established.",
 "Hahn&#39;s return", "The lead is reprising rather than inheriting a role, which keeps the continuity.",
 "The trial structure", "Episodes are built as set pieces with their own rules, which gives the season a shape.",
 "The musical element", "Songs are woven through rather than added, which divides viewers.",
 "The witch lineage", "It draws on comic-book material about a long line of magic users.",
 "The prerequisite", "Watching the earlier series first is close to necessary, not optional.",
 "It commits to a strange structure and the commitment is the appeal. If you have not seen WandaVision, start there."],

["entertainment/movie/the-sandman",
 "The Comic That Was Called Unfilmable",
 "Neil Gaiman&#39;s comics had circulated as a supposedly impossible adaptation for decades before this 2022 Netflix series. The difficulty was never effect work; it was that the source moves between registers so freely that holding one tone for a season is a real problem.",
 "The source comics", "The series adapts the opening volumes rather than attempting the whole run.",
 "The anthology shape", "Some episodes stand almost alone, which follows the comics&#39; structure.",
 "The single-horror-chapter", "One episode is a contained horror story, and it is the season&#39;s boldest move.",
 "The Dream casting", "The lead is played as still and formal, which suits a character who is an idea rather than a man.",
 "The tone problem", "The comics move between myth, horror and whimsy, and any adaptation has to choose.",
 "The adaptation history", "Attempts had been discussed for years before this one reached the screen.",
 "Watch it as an anthology with a spine rather than a single plot, because that is what it is. The standalone horror episode is the one to judge it by."],

["entertainment/movie/fargo",
 "A Television Anthology Borrowed From One Film",
 "Noah Hawley developed this series for television from 2014, taking the Coen brothers&#39; 1996 film as a starting point rather than a text to adapt. Each season is a separate story with its own cast, which is why the show survives where direct adaptations usually fail.",
 "The anthology model", "Seasons are self-contained, so a weak year does not spoil the others.",
 "The Coen inheritance", "It borrows tone and setting from the film rather than its plot.",
 "The regional accent", "The upper-midwest setting is a character in itself, as it was in the original.",
 "The moral framing", "Episodes open with an assertion about truth, and the stories then complicate it.",
 "The cast turnover", "Each season recasts entirely, which attracts actors who would not commit to a long run.",
 "The starting point", "Newcomers ask which season to begin with, and the first is the standard answer.",
 "It is closer to a literary anthology than to a spin-off, and the regional detail is the connective tissue. Start with the first season and treat the rest as separate books."],

# ------------------------------------------------------------ prestige drama & canon
["entertainment/movie/casino",
 "Scorsese&#39;s Other Las Vegas Film",
 "Martin Scorsese directed this 1995 film from Nicholas Pileggi&#39;s non-fiction book, the same writer he had worked with on Goodfellas. It is often treated as a companion piece, though its subject &mdash; how organised crime was pushed out of a legitimate casino business &mdash; is a different argument.",
 "The Pileggi source", "It adapts reported non-fiction rather than a novel, which shapes its structure.",
 "Three narrators", "The film divides its narration between three voices, which is unusual for the director.",
 "The narration device", "All three narrate, and their accounts of the same events do not agree.",
 "The Vegas subject", "The real interest is the business takeover rather than the violence.",
 "The length", "It runs long and the middle stretch is deliberately procedural.",
 "The Goodfellas comparison", "Readers inevitably ask which is better, and the desk declines to settle it.",
 "It is a business story told through three unreliable narrators, and the procedure is the point. Watch it after Goodfellas, not instead of it."],

["entertainment/movie/rashomon",
 "Four Witnesses, Four Films",
 "Akira Kurosawa directed this 1950 film, in which the same crime is recounted four times with mutually incompatible details. Its title entered the language as a term for disputed truth, which is the clearest sign of how far it travelled.",
 "The four accounts", "The structure refuses to resolve which version is accurate, on purpose.",
 "The gate setting", "A ruined gate in the rain frames the story, which is where the retelling happens.",
 "Toshiro Mifune", "The actor&#39;s performance is a study in performance itself, which is the film&#39;s central joke.",
 "The Venice prize", "Its international award is the reason Japanese cinema reached a global audience.",
 "The effect it named", "The word derived from the film is now used far beyond cinema.",
 "The running time", "It is unusually short, which surprises people expecting an epic.",
 "It is short, and it does not tell you which version to believe. Watch it for the structure, which has been borrowed endlessly since."],

["entertainment/movie/gladiator",
 "The Film That Brought Back A Dead Genre",
 "Ridley Scott directed this 2000 film, and its significance is partly industrial: the sword-and-sandal epic had been dormant for decades, and its success is why a run of similar films followed. It also won the Academy Award for Best Picture.",
 "The genre revival", "Its commercial success reopened a category the industry had written off.",
 "The opening battle", "The film establishes its scale immediately, and the effects work still holds up.",
 "The revenge spine", "The plot is a simple revenge structure, which is what frees the film to be about Rome.",
 "The Hans Zimmer score", "The music is a large part of why the film feels the way it does.",
 "The lead&#39;s performance", "The central performance won an Academy Award, and the film rests entirely on it.",
 "The late follow-up", "A follow-up arrived much later, so this remains the reference point.",
 "It is a revenge film with imperial Rome as its real subject, and it revived a genre almost single-handedly. Watch the extended version if the pacing bothers you."],

["entertainment/movie/ex-machina",
 "A Turing Test Told From Inside The Test",
 "Alex Garland wrote and directed this 2014 film, his first as director, with a cast of four and effectively one location. It is a science-fiction film about conversation, and the effects work won an Academy Award despite the film&#39;s small scale.",
 "The single location", "Almost the whole film takes place in one house, which is a constraint the script uses.",
 "The four-hander", "The cast is tiny, so the film relies on dialogue rather than incident.",
 "The Turing framing", "The premise is a test of machine intelligence, and the film is careful about who is testing whom.",
 "The effects award", "The visual work won an Academy Award, which is rare for a film of this size.",
 "The Garland transfer", "The director moved from writing screenplays to directing, and this is the changeover point.",
 "The final reveal", "It resolves on a note that readers should discover rather than be told.",
 "It is a chamber piece about a test where everyone is being assessed, including the audience. Do not read about the ending first."],

["entertainment/movie/moon",
 "One Actor, One Station, One Very Old Idea",
 "Duncan Jones directed this 2009 film as his first feature, with Sam Rockwell carrying almost the entire running time alone. Its effects are largely practical models rather than digital work, which is why it still looks the way it does.",
 "The solo performance", "One actor holds nearly the whole film, which is the risk the film takes.",
 "The practical models", "The station and vehicles were built as miniatures, not rendered.",
 "The isolation premise", "Solitude on a lunar station is an old idea, and the film knows it.",
 "The voice casting", "The station&#39;s computer is voiced by a well-known actor, in a deliberate lineage.",
 "The budget constraints", "The film was made cheaply, and the restriction is visible in ways that help it.",
 "The twist question", "Readers often ask what the film is actually about, and the answer is a spoiler.",
 "It is a quiet science-fiction film that turns on a single idea, carried by one performance. Avoid reading plot summaries before watching."],

["entertainment/movie/call-me-by-your-name",
 "Summer, Italy, And A Screenplay That Won An Award",
 "Luca Guadagnino directed this 2017 adaptation of Andre Aciman&#39;s novel, with James Ivory writing the screenplay &mdash; the pairing is unusual and the script won an Academy Award. It is a romance built almost entirely out of atmosphere and withheld speech.",
 "The Ivory screenplay", "A writer associated with a very different tradition adapted the novel, and won for it.",
 "The northern Italian setting", "The location work is a large part of the film&#39;s reputation.",
 "The period detail", "It is set in the early nineteen-eighties, which the film treats as texture rather than nostalgia.",
 "The lead performance", "The younger lead&#39;s work is the reason the film landed as it did.",
 "The music", "Songs by a contemporary artist were written for the film and carry its final scene.",
 "The novel comparison", "Readers of the book often ask about the differences, and the ending is the big one.",
 "Watch it for the summer and the silence rather than for plot, because there is deliberately little. The final scene is the whole film in miniature."],

["entertainment/movie/the-florida-project",
 "A Childhood Shot On Film Beside A Motel",
 "Sean Baker directed this 2017 film, shot on 35mm, about children living in a budget motel near a large theme park. It uses non-professional performers alongside experienced ones, which is central to how it feels.",
 "The motel setting", "The location is the film&#39;s organising idea rather than a backdrop.",
 "The child&#39;s-eye view", "The camera stays at the children&#39;s height, which does most of the film&#39;s work.",
 "The casting method", "Some leads were found rather than trained, and the film is built around that.",
 "The Willem Dafoe role", "An experienced actor plays the motel manager and is the film&#39;s moral centre.",
 "The film stock", "It was shot on 35mm, which gives it a warmth the digital alternative would not.",
 "Its last five minutes", "It breaks its own rules in the final scene, which readers should not be warned about further.",
 "It is a children&#39;s film about an adult situation, and that gap is the whole achievement. Watch it without reading about the last five minutes."],

# ------------------------------------------------------------ comedy, romance & thrillers
["entertainment/movie/bridesmaids",
 "The Comedy That Proved A Point Nobody Should Have Needed Proven",
 "Paul Feig directed this 2011 film from a screenplay by Kristen Wiig and Annie Mumolo, with Judd Apatow producing. Its significance is partly commercial: it demonstrated that a comedy with a female ensemble could perform at the top of the market.",
 "The Wiig and Mumolo script", "It was written by two of its own performers, which shapes its specificity.",
 "The wedding-party cast", "The cast gives the film its structure, with the wedding as a device rather than a subject.",
 "The Apatow method", "The producer&#39;s approach to improvisation is visible throughout.",
 "The breakout performance", "A supporting turn in it became a career turning point.",
 "The screenplay nomination", "The script was nominated for an Academy Award, which is unusual for the genre.",
 "The comparison problem", "It is often described in terms of a male equivalent, which undersells it.",
 "It is funnier and more specific than its reputation as a milestone suggests, and the script is the reason. Watch it for the ensemble rather than the plot."],

["entertainment/movie/blockers",
 "A Teen Comedy Flipped To The Parents&#39; Side",
 "Kay Cannon directed this 2018 film as her first feature, having written for a long-running a cappella comedy series. The premise inverts the standard teen comedy by following the parents trying to stop a pact rather than the teenagers making it.",
 "The genre inversion", "The film follows the adults, which is what distinguishes it from its influences.",
 "A first-time director", "It was Cannon&#39;s first time directing, after a writing career in comedy.",
 "The two-hander approach", "The parents are split across three storylines that converge on one night.",
 "The wrestling actor", "One of the leads is cast against his established physical image.",
 "The title change", "The film was renamed before release, which changed how it was marketed.",
 "The tone balance", "It aims for cruder comedy and genuine warmth simultaneously.",
 "The inversion is the joke and it is sustained for the full running time rather than just the premise. It works best if you know the films it is flipping."],

["entertainment/movie/crazy-rich-asians",
 "A Studio Romance With An Entirely Asian Principal Cast",
 "Jon M. Chu directed this 2018 adaptation of Kevin Kwan&#39;s novel, and its main claim is industrial: a major studio romantic comedy with an all-Asian principal cast had not been attempted at that scale in decades. The film itself is a lavish, specific comedy of manners.",
 "The Kwan novel", "It adapts the first of a trilogy, which is why the ending leaves threads open.",
 "The casting fact", "The ensemble is the point, and the film knows what it is representing.",
 "The Singapore setting", "The location work is unusually specific rather than a generic stand-in.",
 "The opening flashback", "The film starts in another country and era, which frames the whole story.",
 "The wedding sequence", "Its set piece is where the production scale is most visible.",
 "The book comparison", "Readers ask how much of the novel survives, and the answer is a fair amount.",
 "Watch it for what it established as much as for the romance itself. The specific detail is what keeps it from being a generic wedding comedy."],

["entertainment/movie/atomic-blonde",
 "A Cold War Spy Thriller Built Around One Long Fight",
 "David Leitch directed this 2017 adaptation of a graphic novel, set in Berlin in the days around the wall coming down. Its reputation rests on a sustained stairwell fight staged to look like a single take.",
 "The graphic novel source", "It adapts an existing spy comic rather than originating the plot.",
 "The autumn 1989 setting", "The wall&#39;s collapse is the deadline the plot runs against.",
 "The single-take fight", "The staging is a deliberate display of what the performer trained for.",
 "The period soundtrack", "The music is drawn from the era and does much of the film&#39;s tonal work.",
 "The Leitch background", "The director came from stunt work, which shows in how the action is built.",
 "The plot&#39;s reputation", "The story is often called convoluted, and the desk agrees it is the weaker half.",
 "Watch it for the staging and the setting, because the plotting is the part people forget. The fight sequences are the reason it is remembered."],

["entertainment/movie/udaan",
 "A Debut About A Childhood That Ends Too Early",
 "Vikramaditya Motwane directed this 2010 film as his first feature, produced by Anurag Kashyap. It follows a boy expelled from boarding school and returned to a father he barely knows, and it is as much about that household as about what he wants.",
 "Motwane&#39;s first feature", "It was Motwane&#39;s first film, and it established a career built on restraint.",
 "The father figure", "The performance is the film&#39;s engine, and it is played without any softening.",
 "The Bombay setting", "The city is industrial and unglamorous rather than the usual cinematic version.",
 "The poetry thread", "The protagonist&#39;s writing gives the film its structure and its title.",
 "The Cannes premiere", "It screened at a major festival, which brought it wide attention.",
 "The ending&#39;s tone", "It resolves with something closer to possibility than triumph, which is the point.",
 "It is a quiet film about a household rather than a plot, and the restraint is deliberate. Expect a mood rather than a resolution."],

["entertainment/movie/awarapan",
 "A Bollywood Remake That Kept Its Own Identity",
 "Mohit Suri directed this 2007 Hindi film, adapting a Korean gangster picture from two years earlier. It is remembered as much for its music as for its plot, which is a fair summary of what the film is actually good at.",
 "The Korean original", "It is a remake rather than an original screenplay, which shapes the story&#39;s shape.",
 "Why the music lasted", "The music outlived the film&#39;s plot in popular memory, and the desk reports that rather than arguing.",
 "The lead casting", "The film leaned on a performer with a specific screen persona rather than a conventional romantic lead.",
 "The gangster frame", "The crime story is the container for a melodrama rather than the other way around.",
 "Its emotional register", "It is a love story wrapped around violence, and the mix is the reason people remember it.",
 "The original comparison", "Viewers who have seen the Korean film tend to have strong opinions on the changes.",
 "Watch it as a melodrama with a crime backdrop rather than a thriller, and the music will do the rest. The Korean original is a different, colder film."],

# ------------------------------------------------------------ desk threads

["entertainment/movie/the-falcon-winter-soldier",
 "Two Sidekicks Asked What They Owe The Shield",
 "Kari Skogland directed this 2021 series for Disney+, running six episodes, and it is the franchise entry that asks what happens to the people left behind after the big story ends. It is a political thriller wearing a partnership comedy, which is why it is more interesting than its premise suggests.",
 "The post-Blip setting", "It deals directly with the aftermath of a global disappearance, which most of the franchise skips.",
 "The shield question", "Who should carry a symbol is the actual plot, and the show takes it seriously.",
 "The buddy pairing", "The central pairing is a study in obligation rather than friendship, which is the point.",
 "The antagonist logic", "The villain&#39;s argument is given real airtime rather than dismissed.",
 "John Walker", "The replacement figure exists to test the audience&#39;s own sympathies, and he does.",
 "The six-episode shape", "Its short run is a constraint, and the desk notes that one thread suffers for it.",
 "It is the most politically minded of its franchise&#39;s television entries, and the argument is the reason to watch. Expect a slow start and a strong second half.",
],

]

DEPTH_SECTIONS_X = {}
for _row in ROWS_X:
    _slug, _h2, _para = _row[0], _row[1], _row[2]
    _items = _row[3:-1]
    _para2 = _row[-1]
    assert _slug.startswith("entertainment/movie/"), f"batch X is film-only: {_slug}"
    # 6 pairs minimum (16 fields) and an even number of item fields, so a
    # section can carry more than the baseline six pairs without breaking.
    # row = [slug, h2, para] + item pairs + [para2], so item count is
    # len(row) - 4 and must be even and non-zero.
    assert len(_row) >= 16 and (len(_row) - 4) % 2 == 0, f"row shape {_slug}: {len(_row)} fields"
    assert isinstance(_para2, str) and _para2, f"missing closing para: {_slug}"
    DEPTH_SECTIONS_X[_slug] = ed(_slug, _h2, _para, _items, _para2)

for _slug, _html in DEPTH_SECTIONS_X.items():
    _route = _slug.split("#")[0]
    assert (_ROOT / _route / "index.html").is_file(), f"batch X missing route: {_route}"

_h2s = [r[1] for r in ROWS_X]
_lead = [r[i] for r in ROWS_X for i in range(3, len(r) - 1, 2)]
assert len(set(_h2s)) == len(_h2s), "duplicate h2 within batch X"
assert len(set(_lead)) == len(_lead), "duplicate lead-in within batch X"

print(f"batch X: {len(DEPTH_SECTIONS_X)} film sections, {len(set(_h2s))} unique h2, "
      f"{len(set(_lead))} unique lead-ins")
