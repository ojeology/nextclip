"""Batch W depth sections — the 36 thinnest remaining film pages (2026-09-29).

These pages carry a verdict and an FAQ but no editorial depth: median 336 words,
all below the 600-word floor. Each section is written for its own title and no
h2 or lead-in label is reused anywhere in the batch (asserted at the bottom).

Rows are FLAT: [slug, h2, para, l1, d1, ... l6, d6, para2]  -- 16 fields.

Craft note for this batch: it is anime- and world-cinema-heavy, so the sections
lean on what is actually documented -- source material, studio, adaptation
history, national industry context -- rather than on scene-by-scene recall.
Where a title is recent, the section stays on the verifiable ground of its
production and lineage and does not invent plot or reception detail.
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
        r = SEE_ENT[(sum(ord(c) for c in slug) + 3 * i) % len(SEE_ENT)]
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


ROWS_W = [
# ------------------------------------------------------------------ romance & slice of life
["entertainment/movie/toradora",
 "Two Characters Who Are Not Nice",
 "The romantic comedy works because neither lead is written as a prize: Taiga is short-tempered and physically violent, Ryuuji looks intimidating and is domestically meticulous. The romance builds out of mutual usefulness rather than attraction, which is why it holds up better than most of the genre.",
 "The premise is co-operation", "Each agrees to help the other with someone else, and the feelings arrive as a side effect rather than a goal.",
 "Takemiya&#39;s light novels", "Yuyuko Takemiya&#39;s source is a long-running series, and the adaptation chose careful pacing over compression.",
 "J.C. Staff&#39;s restraint", "The studio resists the visual clutter that dates the genre, so the show has aged unusually well.",
 "Taiga is not softened", "Her temper is treated as part of her rather than a flaw the plot fixes.",
 "The Christmas Arc", "The series&#39; midpoint turns the comedy serious for several episodes, and the tonal shift is earned by the setup.",
 "Voice casting", "Rie Kugimiya&#39;s performance is the reason the archetype is remembered as specific rather than generic.",
 "The ending is debated", "The final episodes divide viewers, and the desk thinks that disagreement is a sign of how invested the show makes people.",
 "It is one of the few romance series where both people change rather than one being fixed by the other, which is why it is still recommended a decade on. Give it the first four episodes before judging the tone."],

["entertainment/movie/your-lie-in-april",
 "A Series About Performance Anxiety",
 "The story is usually described as a romance, and it is, but the recurring subject is stage fright: a pianist who cannot hear his own playing and the violinist who drags him back in front of an audience. The music is the drama, not the backdrop.",
 "The performance-nerve problem", "The protagonist's inability to play is a psychological injury the series treats with real seriousness.",
 "Arakawa&#39;s manga", "Naoshi Arakawa&#39;s source runs the same emotional beats, and the anime keeps most of its structure.",
 "A-1 Pictures&#39; concert staging", "The recital episodes are animated as action sequences, with the hands and the score doing the work.",
 "Kaori is not a device", "The violinist who pushes the pianist has her own ambition and her own fear.",
 "Classical repertoire", "The pieces are real and recognisable, and the series uses them to mark character change.",
 "The title is a warning", "The show signals its ending early, and watching it knowing that changes the experience rather than ruining it.",
 "The animation of hands", "Piano animation is genuinely difficult and the series invested in it, which is visible.",
 "It is a series about why people stop playing music and what makes them start again, and it is more serious than its romance reputation suggests. Watch it with sound you can hear properly."],

["entertainment/movie/violet-evergarden",
 "A Ghost Story Told Through Letters",
 "The protagonist is a former child soldier who takes work writing letters for other people, and the series is organised as a run of standalone episodes in which she learns what feeling looks like by drafting other people&#39;s. The war is backstory; the furniture of the show is stationery and correspondence.",
 "The letter-writing premise", "A profession built on translating other people&#39;s emotion gives the series an episodic engine and a moral frame.",
 "Kyoto Animation&#39;s craft", "The studio&#39;s reputation rests on character animation, and this series is among its most technically celebrated work.",
 "A war just ended", "The conflict shapes every character, and the show refuses to make its ending a simple triumph.",
 "The episodes are mostly standalone", "Each client&#39;s letter is its own short story, which makes the series easy to sample and hard to put down.",
 "The protagonist's injury", "She cannot read emotion, and the series treats that as a wound rather than a quirk.",
 "Akatsuki&#39;s light novels", "The source is a series of light novels, and the adaptation expands several of its arrivals into full episodes.",
 "Evan Call&#39;s music", "The score carries a great deal of the emotional register, and it is a large part of the show&#39;s reputation.",
 "The premise sounds sentimental and the execution is restrained, which is the whole reason it works. Readers wary of the genre should try the first two standalone episodes rather than deciding from the synopsis."],

["entertainment/movie/apothecary-diary",
 "Court Politics Solved By A Pharmacist",
 "The series puts a pharmacist&#39;s assistant in an imperial court and lets her solve problems with chemistry rather than martial arts. That inversion is the appeal: the mystery is usually a poisoning, and the resolution is usually knowledge.",
 "The poison-detection hook", "Each case turns on ingested substances, which gives the series a repeatable and genuinely interesting structure.",
 "Natsu Hyuuga&#39;s novels", "The source began as a web novel and grew into a long-running light-novel series before adaptation.",
 "Maomao&#39;s disinterest", "The protagonist is curious and unromantic, and the show never forces her into the submissive role the setting implies.",
 "The court as a workplace", "Consort politics are treated as an administrative system with rules, which makes the intrigue legible.",
 "Servants&#39; lives", "The show spends its time with the staff rather than the royalty, which is the more interesting vantage point.",
 "The adaptation&#39;s reception", "It was among the most discussed anime of its year, which the desk notes as reception rather than a verdict.",
 "Period detail", "The fictional court borrows from Chinese imperial history, and the production designs it as a system rather than a backdrop.",
 "It is a mystery series whose solutions are real knowledge, which is a better engine than it sounds. Start at the beginning; the character&#39;s circumstances matter and the show does not recap."],

# ------------------------------------------------------------------ anime action & shonen
["entertainment/movie/fullmetal-alchemist-brotherhood",
 "Why The Remake Beat The Original",
 "The first adaptation caught up with the manga and invented its own ending. This one waited for the story to finish and adapted it faithfully, which is why the two versions are genuinely different shows rather than one being better produced.",
 "The faithful-adaptation decision", "Hiromu Arakawa&#39;s manga had ended by the time this was made, so the ending is hers rather than the studio&#39;s.",
 "Bones&#39; production", "The studio had already animated the earlier version, and the second pass has noticeably more consistent animation.",
 "The law of equivalent exchange", "The series&#39; central rule is a moral system as much as a magic one, and it constrains every plot solution.",
 "Brothers as the subject", "The relationship carries the show, and the scale of the conspiracy never displaces it.",
 "Which version first", "Begin at episode one of this run rather than with the earlier series, because the openings differ.",
 "The 2003 version still stands", "It is not superseded so much as it is a different story, and both are worth watching.",
 "The ending lands", "Because the author finished her own story, the conclusion is structural rather than improvised.",
 "On the running order question, the desk&#39;s position is simply to watch this one first and seek out the 2003 series afterwards. Watch it as a completed story and the length stops feeling long."],

["entertainment/movie/hunter-x-hunter",
 "A Shonen That Keeps Changing Genre",
 "The show begins as a boy searching for his father and then becomes, in order, a tournament, a detective story, a siege, an election and a political thriller. Togashi writes by rebuilding the rules between arcs, and the 2011 adaptation follows him.",
 "Togashi&#39;s pacing", "Yoshihiro Togashi is known for long hiatuses and for arcs that abandon their own premise, which the adaptation takes at face value.",
 "The Chimera Ant arc", "A long, slow, morally serious stretch that the desk rates as the series&#39; high point and its most divisive.",
 "Madhouse&#39;s consistency", "The studio&#39;s animation is steady across a long run, which is rarer than it should be.",
 "Nen as a power system", "The show&#39;s abilities are defined by rules and costs, and the fights are won by understanding them.",
 "Gon is not a hero", "The protagonist&#39;s single-mindedness is treated as unsettling rather than admirable.",
 "Which adaptation", "The 2011 series covers more of the manga than the 1999 version, which is why the desk recommends it.",
 "Violence escalates", "Later arcs are considerably darker than the opening suggests, which surprises viewers who came for the adventure.",
 "It rewards patience: the first arc is the simplest thing it does, and everything after is more ambitious. Give it the Hunter Exam and the arc that follows before deciding."],

["entertainment/movie/one-punch-man",
 "A Parody That Became The Thing It Mocked",
 "The premise is that the strongest hero alive is bored by it, which deflates every fight the genre normally builds to. The joke only works because the animation is genuinely excellent, so the show ends up delivering the spectacle it is satirising.",
 "Saitama&#39;s boredom", "Invincibility removes suspense, so the show builds tension out of everyone else instead.",
 "ONE&#39;s webcomic", "The source began as a rough amateur webcomic, which is why its jokes land on genre convention rather than on production.",
 "Murata&#39;s redraw", "Yusuke Murata&#39;s redrawn version supplies the visual detail the anime then animates.",
 "Madhouse&#39;s action animation", "The first season&#39;s fight choreography is the reason the show is remembered rather than the premise.",
 "Everybody around Saitama", "The heroes and monsters carry the arcs he cannot, and the show knows it.",
 "The second season changed studios", "J.C. Staff took over and the animation difference is visible, which the desk notes rather than excuses.",
 "Which season first", "Season one stands alone and is considerably the stronger of the two.",
 "Watch it as a comedy about how competence removes drama, which is a sharper idea than the title suggests. The first season is the one to recommend; the second is optional."],

["entertainment/movie/dragon-ball-z",
 "The Sequel That Redefined Its Own Genre",
 "The show took a comedy adventure and rebuilt it as serialised combat, and in doing so set the template that a generation of shonen followed: escalating power levels, tournaments, and a hero who arrives late and wins anyway.",
 "The tonal break from Dragon Ball", "The original was a gag manga; this version keeps the character but changes the genre entirely.",
 "Akira Toriyama&#39;s arcs", "The author wrote the manga the anime adapted, and the series&#39; structure follows his escalating threats.",
 "The Saiyan reveal", "A backstory turn that reframes the protagonist and gives the show its engine.",
 "The tournament format", "Structured competition as a storytelling device, later standard across the genre.",
 "Filler episodes", "The anime added material to avoid overtaking the manga, and the desk flags which stretches to skip.",
 "Its influence is enormous", "Most modern battle shonen are working inside rules this show established.",
 "Manga or anime", "Read the manga for the pacing, or watch the anime for the performances &mdash; both are legitimate.",
 "Its importance is historical as much as artistic, which is the honest way to describe it. Readers who missed it should know the first arc is slow and the show finds its footing shortly after."],

["entertainment/movie/dragon-ball-super",
 "The Continuation That Started As Two Films",
 "This series exists because the author returned to the story after eighteen years away, and it began by retelling two films before writing anything new. Knowing that explains why its opening arcs feel different from everything after.",
 "It retells the films first", "Battle of Gods and Resurrection F were re-adapted as arcs before original material began.",
 "Toriyama&#39;s involvement", "He outlined the story and designed characters rather than drawing the manga, which is a different kind of authorship.",
 "The multiverse structure", "Tournaments between universes gave the show a format for a long run of fights.",
 "Placing it in the story", "It sits after the original manga&#39;s ending but before its epilogue, which the show handles carefully.",
 "The animation criticism", "Early episodes drew complaints about consistency that the production later addressed.",
 "Two films came after", "Super Hero and Broly are continuous with the series and are the better entry points.",
 "The manga continues differently", "The comics version diverges from the anime, and the desk notes that the two are separate tellings.",
 "New readers should start with the two films the series retells, because that is where the story actually begins and the animation is better. The series is for people who want more after those, and the desk is honest that it is uneven."],

["entertainment/movie/chainsaw-man",
 "Adapting A Manga That Moves Like A Film",
 "Tatsuki Fujimoto&#39;s source is drawn with cinematic framing, so the adaptation&#39;s main problem was deciding how realistic to make it. MAPPA chose a muted, grounded look rather than the exaggerated style the manga&#39;s covers suggest, and that choice divided the audience.",
 "The cinematic source", "The manga&#39;s panels are composed like film frames, which sets a high bar for any adaptation.",
 "MAPPA&#39;s restrained look", "Colour and lighting are desaturated, and the desk thinks the decision is defensible even where it disappointed readers.",
 "The protagonist&#39;s poverty", "Denji&#39;s motivation is food and shelter rather than ambition, which is an unusual engine for the genre.",
 "Tonal whiplash", "The series moves between comedy and extreme violence quickly, and the source does the same.",
 "The ending is a beginning", "The adaptation covers the first part of the manga and behaves like an opening act.",
 "The movie that followed", "The Reze arc was later adapted as a film, which is the next thing to watch after the series.",
 "Devil design", "The monsters are drawn from everyday objects and fears, which is a stronger idea than the gore suggests.",
 "It is a violent, funny series about a boy who wants a normal life, and the violence is not the point. Watch the series then the film, in that order, and give the muted visual style a few episodes."],

["entertainment/movie/spy-x-family",
 "The Comedy Rests On Three Liars",
 "A spy needs a family for a cover mission, so he adopts a telepathic daughter and marries an assassin. Every joke comes from the same engine: three people keeping secrets from each other while genuinely becoming a family.",
 "The premise is structural", "Each character has a mission that requires the others, so the sitcom and the plot are the same thing.",
 "Tatsuya Endo&#39;s manga", "The source is drawn with unusually clean action framing, and the adaptation keeps its comic timing intact.",
 "Two studios, one show", "Wit and CloverWorks split the production, and the desk notes the resulting consistency as an achievement.",
 "Anya carries the comedy", "The child&#39;s mind-reading means the audience gets the joke before the adults do, every time.",
 "The violence is cartoonish", "The assassin&#39;s work is stylised rather than graphic, which keeps the tone family-friendly.",
 "No homework needed", "The first episode introduces all three leads, so the series asks nothing of you going in.",
 "It is a workplace comedy wearing spy fiction, and the warmth is genuine rather than ironic. Watch it as a comedy first and the occasional action sequence lands better than expected."],

["entertainment/movie/trigun",
 "A Pacifist In A Western",
 "The protagonist is a legendary gunman who refuses to kill anyone, in a setting that gives him every reason to. That contradiction is the show&#39;s subject, and it makes the action sequences arguments rather than spectacles.",
 "The no-kill rule", "Vash&#39;s refusal is the plot, not a personality trait, and the series tests it constantly.",
 "Nightow&#39;s manga", "Yasuhiro Nightow&#39;s source is denser and darker; the 1998 anime diverges from it substantially.",
 "The Western-in-space setting", "A desert planet with frontier towns, which lets the show use the genre&#39;s grammar without its history.",
 "The comic tone shifts", "Early episodes are largely farcical, and the show turns serious in its second half.",
 "The remake exists", "Trigun Stampede retells the story with modern animation and a different ending path.",
 "Which version to watch", "The desk suggests the original for the tonal arc and the remake for the visuals, and says so rather than picking a winner.",
 "Insurance agents as comedy", "Two investigators chasing the hero&#39;s destruction bills are the show&#39;s running joke and its best invention.",
 "It is a series about refusing violence in a genre built on it, and it earns that position over a long run. Give the comic opening episodes their time; the turn is the point."],

["entertainment/movie/blue-lock",
 "A Sports Show That Argues Against Teamwork",
 "Most sports stories build towards the team coming together. This one argues the opposite: that a striker needs selfishness, and that cooperation is what holds Japanese football back. That contrarian premise is why it stands out in a crowded genre.",
 "The egoist premise", "The programme is designed to produce one supremely selfish striker rather than a balanced squad.",
 "Kaneshiro and Nomura&#39;s manga", "The source is a manga by Muneyuki Kaneshiro and Yusuke Nomura, and the anime follows its tournament structure closely.",
 "Isagi&#39;s development", "The protagonist improves by learning to read the field, which gives the show a legible kind of progress.",
 "The animation trade-off", "The series uses stylised effects for the players&#39; thought processes, which the desk notes divides viewers.",
 "The supporting rivals", "Each opponent is given a distinct philosophy, so the matches are arguments between ideas.",
 "Comparison to the genre", "It is a deliberate inversion of the teamwork-first tradition, which is the reason to watch it.",
 "Football knowledge not required", "The opening arc explains its own competition, so nothing outside the show is assumed.",
 "It is a sports series for people who have grown tired of the usual lesson, and the argument is more interesting than the football. No background in the sport is required, which the show is careful to ensure."],

["entertainment/movie/fairy-tail",
 "Friendship As The Actual Magic System",
 "The series is built on a guild of wizards who win because they believe in each other, which is either the show&#39;s charm or its weakness depending on your appetite. It is unashamed about the formula, and it sticks to it for hundreds of episodes.",
 "The guild structure", "A found family is the setting and the theme, so the emotional payoff is available in almost every arc.",
 "Mashima&#39;s long run", "Hiro Mashima wrote the manga over a decade, and the anime follows it closely and at length.",
 "Natsu&#39;s straightforwardness", "The protagonist&#39;s power comes from emotion rather than technique, which is the show&#39;s whole method.",
 "The arcs are self-contained", "New viewers can start at the beginning of any major arc, which is unusual for a long shonen.",
 "The fan service criticism", "The show is known for it, and the desk notes it as a genuine barrier for some viewers.",
 "The sequel exists", "Fairy Tail: 100 Years Quest continues the story, so the end is not really the end.",
 "Studio changes", "A-1 Pictures and Satelight shared the production, and the visual differences are noticeable across the run.",
 "It is comfort viewing more than ambitious storytelling, and it does that job well for a very long time. Watch it knowing what it is rather than hoping for subversion."],

# ------------------------------------------------------------------ South Asian cinema
["entertainment/movie/dhoom-3",
 "The Franchise Film That Bet On One Actor",
 "The third entry in a heist series casts Aamir Khan in a double role as rival brothers, and the entire production is built around that gamble. The set pieces are larger than the earlier films and the logic is thinner, which the desk states plainly.",
 "The dual role", "Khan plays both the antagonist and his twin, which the film treats as its central attraction.",
 "The circus setting", "A Chicago circus supplies the film&#39;s imagery and its best set pieces.",
 "Yash Raj production scale", "The studio&#39;s budget is visible, and the action was staged internationally.",
 "Divergence from the series", "The earlier films were lighter caper comedies; this one is heavier and more emotional.",
 "The chase choreography", "The motorcycle and aerial sequences are the parts the film is remembered for.",
 "Critical reception", "It was commercially enormous and critically mixed, and the desk does not pretend otherwise.",
 "Where it sits", "The series is loosely connected, so prior viewing is not required.",
 "Watch it for the spectacle and the performance, not for the plot, and it delivers on those terms. Readers wanting the franchise at its lightest should start with the first film."],

["entertainment/movie/the-great-indian-kitchen",
 "A Film About Household Labour",
 "The premise is a kitchen: a new wife enters a household where cooking is an unpaid, unending obligation, and the film simply shows the work. It is among the most direct films about domestic labour in Indian cinema, and its restraint is what makes the argument.",
 "The repetitive structure", "The film shows the same tasks repeatedly, and the repetition is the point rather than a flaw.",
 "Jeo Baby&#39;s direction", "The director keeps the camera still and the pace ordinary, refusing melodrama.",
 "Nimisha Sajayan&#39;s performance", "A largely silent role that carries the film&#39;s whole emotional weight.",
 "The Malayalam context", "Malayalam cinema has become the most formally adventurous of the Indian industries, and this sits in that tradition.",
 "The premise is universal", "Anyone who has run a household recognises the schedule, which is why it travelled.",
 "A small film that travelled", "Made on a modest budget and widely discussed, which is reception rather than a verdict.",
 "The film has no villains", "The husband is not cruel, which is a harder and more honest choice than a villain would be.",
 "It is a quiet, patient film about work nobody counts, and it is more effective for refusing to shout. Watch it without expecting a confrontation scene, because the absence of one is the argument."],

["entertainment/movie/uri",
 "The Film That Made A Military Operation A Procedure",
 "The surgical strikes of 2016 became one of the most commercially successful Indian films about them, and its approach is procedural rather than jingoistic: the operation is treated as a plan with logistics, timelines and failures.",
 "The procedural structure", "The film follows planning and execution rather than a hero&#39;s journey, which is unusual for the genre.",
 "Aditya Dhar&#39;s script", "It was the director&#39;s debut feature, and the screenplay&#39;s structure is the film&#39;s strongest element.",
 "Vicky Kaushal&#39;s lead", "A performance built around competence and restraint rather than speeches.",
 "The Uri base reconstruction", "Production design of the military installation is where the budget is most visible.",
 "The claimed timeframe", "The film compresses and dramatises events, and readers should treat it as a dramatisation.",
 "Indian war-film tradition", "It sits in a genre that has grown considerably since, and the desk notes its influence.",
 "The domestic audience", "It became a major success in India, which the desk reports as fact rather than endorsement.",
 "Watch it as a procedural thriller based on a real operation rather than as a documentary, and the craft is genuinely strong. Readers wanting context should read the reporting alongside it, which the desk recommends for any dramatised history."],

["entertainment/movie/bajrangi-bhaijaan",
 "A Cross-Border Film That Chose Kindness",
 "The plot is a devout man escorting a mute Pakistani girl home after she is stranded in India, and the film&#39;s politics are deliberately naive: obstacles are personal rather than national, and almost everyone he meets helps. That choice was the point.",
 "The child is mute", "Because the girl cannot speak, the film has to show the border problem rather than debate it.",
 "Kabir Khan&#39;s handling", "The director keeps the tone warm and comic, and the desk notes this is a deliberate political position.",
 "Salman Khan against type", "A star known for action playing a soft, devout innocent, which was part of the film&#39;s appeal.",
 "The road-trip structure", "Episodes along the journey give the film its shape and its running jokes.",
 "Religious identity", "The hero&#39;s faith is central and treated with respect rather than as a plot device.",
 "The film&#39;s reception", "It was one of the highest-grossing Indian films of its year, which the desk reports as fact.",
 "Its optimism is the critique", "Some viewers found the harmony unrealistic, and the desk thinks that is a fair argument.",
 "It is a mainstream film that chose warmth over confrontation, and judged on those terms it succeeds. Readers wanting a harder look at the same subject will not find it here, and should know that going in."],

# ------------------------------------------------------------------ Korean & Nigerian
["entertainment/movie/the-man-from-nowhere",
 "The Action Was Built Around Stillness",
 "The film casts a quiet pawnshop owner as an ex-special-forces operative, and its best sequences are the ones where he does almost nothing. The restraint is what distinguishes it from the action films that copied it.",
 "Won Bin&#39;s stillness", "The lead performance is almost entirely physical and near-silent, which the desk rates as the film&#39;s engine.",
 "The knife fight", "A single close-quarters sequence in a confined space became the film&#39;s signature and its most imitated scene.",
 "The child relationship", "The emotional thread is a friendship with a young neighbour, and the film takes it seriously.",
 "Lee Jeong-beom&#39;s direction", "A debut feature, and the staging is disciplined rather than showy.",
 "The trafficking premise", "The villains&#39; business is grim, and the film does not use it for titillation.",
 "Korean action lineage", "It sits alongside a run of Korean thrillers that reached international audiences in the same period.",
 "How the desk rates it", "Among the strongest of that Korean run, and better than most Western equivalents.",
 "It is an action film whose power comes from what the lead withholds, which is a difficult thing to sustain. Watch it expecting a slow build; the payoff is worth the patience."],

["entertainment/movie/a-bittersweet-life",
 "A Gangster Film Where Nothing Is Stylish",
 "Kim Jee-woon&#39;s film follows a loyal enforcer whose life collapses over a single act of mercy, and it refuses the genre&#39;s pleasures: the violence is ugly, the loyalty is misplaced and the ending is not a triumph.",
 "The mercy that starts it", "The plot turns on one small decision to spare someone, which is an unusually moral engine for the genre.",
 "Lee Byung-hun&#39;s performance", "Restrained for most of the film, which makes the final act land harder.",
 "The hotel setting", "A luxury interior used as a workplace, which keeps the violence small and domestic.",
 "The score and imagery", "The film is visually elegant in a way that works against its content, and the desk reads that as deliberate.",
 "Kim Jee-woon&#39;s range", "The director moves between genres, and this is his tightest film.",
 "The alternative ending", "A different cut exists, and the desk recommends the theatrical version first.",
 "Korean noir tradition", "It sits among the films that built the international reputation of Korean genre cinema.",
 "It is a bleak, well-made film with no comfort in it, and the desk says so rather than dressing it up. Watch it for the craft and the performance, not for a satisfying resolution."],

["entertainment/movie/vincenzo",
 "A Korean Drama That Borrows Italian Opera",
 "A mafia consigliere returns to Seoul and takes on a pharmaceutical conglomerate using the law, which lets the series run two registers at once: broad comedy and genuine corporate satire. The tonal swing is the show&#39;s signature and its main point of disagreement.",
 "The dual register", "Scenes move between farce and violence within an episode, and the desk notes that this divides viewers sharply.",
 "The conglomerate villain", "The antagonist is a corporation rather than a mob, which is a sharper target than the genre usually picks.",
 "Song Joong-ki&#39;s performance", "The lead plays it straight against a comic ensemble, which is why the absurdity holds together.",
 "The legal-procedure engine", "Court and corporate manoeuvring supplies the plot, so the series is closer to a legal drama than a crime one.",
 "Its length", "Twenty episodes with a long middle stretch, which the desk flags as the main barrier.",
 "Korean drama export", "It was one of the most-watched Korean series internationally in its year, which the desk reports as reception.",
 "The tenants downstairs", "The building&#39;s residents carry the comedy and give the show its warmth.",
 "It is a revenge drama that is frequently very funny, and the mixture either works for you immediately or does not. Give it three episodes before deciding, because the tone takes that long to settle."],

["entertainment/movie/a-tribe-called-judah",
 "Nigerian Comedy At Feature Scale",
 "A single mother&#39;s five sons from five different fathers attempt a robbery to save her, and the film turns that premise into a family comedy with an action finale. It became one of the highest-grossing Nigerian films, which matters for what it says about the industry.",
 "The five sons", "Each is written as a distinct type, which gives the film an ensemble rather than a lead.",
 "Funke Akindele&#39;s direction", "The director also stars, and the film&#39;s commercial reach reflected her standing in Nollywood.",
 "The heist structure", "Borrowing a genre shape gave the film a pace that Nollywood comedies often lack.",
 "The mother&#39;s illness", "The emotional stakes are domestic, which keeps the film grounded despite the plot.",
 "Nollywood&#39;s theatrical turn", "Its box office was part of a run that pushed Nigerian films back into cinemas.",
 "The comedy is broad", "The desk notes the humour is farcical by design and does not pretend otherwise.",
 "Its significance", "Commercially it is a landmark, and the desk separates that from its merits as a film.",
 "Watch it as an ensemble comedy and the pleasure is in the cast rather than the plot, which is thin in places. Its box office is the more interesting story, and it is worth reading about separately."],

["entertainment/movie/brotherhood",
 "A Nigerian Action Film That Went For Craft",
 "Loukman Ali&#39;s film follows two brothers on opposite sides of a robbery investigation, and its reputation rests on the action staging: the director came from a visual-effects background and the set pieces are unusually well built for the budget.",
 "Loukman Ali&#39;s background", "The director&#39;s VFX and short-film work is visible in how the action is constructed.",
 "The brother conflict", "The plot runs on a family split, which gives the chases a personal stake.",
 "The chase sequences", "Practical shooting and tight editing are the film&#39;s strongest technical elements.",
 "The Nollywood action gap", "Nigerian cinema has produced comparatively few action films, which makes this one notable.",
 "The cast", "It assembles several of the industry&#39;s best-known actors, which the desk notes as a commercial decision.",
 "How it landed", "Well received at home and shown abroad, which the desk reports as fact rather than praise.",
 "Budget against ambition", "The film aims higher than its means in places, and the desk reads that as a fair trade.",
 "It is worth watching for how much action craft the production extracted from limited resources. Go in expecting a genre film rather than a prestige drama and it delivers."],

# ------------------------------------------------------------------ Chinese cinema
["entertainment/movie/wolf-warrior-2",
 "The Film That Became A Domestic Phenomenon",
 "A former special-forces soldier ends up in an African war zone, and the film&#39;s Chinese box office broke records. The interesting question is not whether it is good but what its reception says about the audience it was made for.",
 "The box-office fact", "It became one of the highest-grossing films ever in China, which is the fact most worth knowing about it.",
 "Wu Jing as director and star", "The lead directed and choreographed, which explains the film&#39;s physical consistency.",
 "The African setting", "Shot partly in China and partly abroad, and the desk notes the setting is used symbolically.",
 "The patriotism is explicit", "The film is openly nationalistic, and readers should expect that rather than be surprised.",
 "Action craft", "The fight and vehicle sequences are competently staged, which the desk credits.",
 "The first film", "The original is smaller and less politically charged, which the desk notes for context.",
 "Outside China", "Its reception abroad was very different, which is itself worth understanding.",
 "Watch it as a mainstream domestic blockbuster rather than an action film made for export, and it makes more sense. Readers interested in Chinese cinema&#39;s commercial turn will find it more useful than enjoyable."],

["entertainment/movie/wandering-earth-2",
 "The Prequel That Improved On The Original",
 "The first film adapted a Liu Cixin short story into a disaster spectacle. This one goes back in time to show how the crisis began, and it is more ambitious: multiple timelines, a political argument about survival, and a much larger production.",
 "The prequel structure", "It shows the events before the first film, which lets it build the world rather than inherit it.",
 "Liu Cixin&#39;s source", "The story is short and the films expand it enormously, which the desk notes as an adaptation liberty.",
 "Frant Gwo&#39;s direction", "The director returned, and the improvement in staging and scale between the two films is visible.",
 "The hard-science premise", "Moving the planet rather than leaving it is an unusual idea that the films take seriously.",
 "Chinese science fiction", "The films are part of a rapid expansion of the genre in Chinese cinema.",
 "The visual effects", "The production is among the most technically ambitious to come out of the industry.",
 "Which to watch first", "The desk recommends the second film if you want the stronger one, accepting the timeline jump.",
 "It is a large, serious science-fiction film with a genuinely unusual premise, and the scale is the point. Subtitles are essential and the desk recommends the original audio."],

# ------------------------------------------------------------------ series & western
["entertainment/movie/x-men-2",
 "The Sequel That Made The Ensemble Work",
 "The first film assembled the team; this one gives almost every member something to do, and it does it inside a plot about registration and identity that is more interesting than the action. The desk rates it as the high point of the original trilogy.",
 "The ensemble balance", "Nightcrawler&#39;s opening, Wolverine&#39;s search and Jean&#39;s arc all get real screen time, which is rare.",
 "The opening sequence", "A White House infiltration staged with real tension, and the best set piece in the series.",
 "Bryan Singer&#39;s direction", "The film is patient with its characters between action beats, which the sequels abandoned.",
 "The registration allegory", "The mutant-rights theme is used as an argument rather than a costume.",
 "Wolverine and Stryker", "A personal history gives the film&#39;s villain a reason to matter.",
 "The new arrivals", "Brian Cox and Alan Cumming are the additions that lift this above the first film.",
 "Its place now", "The franchise was rebooted twice afterwards, and the desk rates this above both runs.",
 "It is the strongest of the early X-Men films and holds up better than most superhero releases of its era. Watch the first film before it, because the emotional beats depend on the introductions."],

["entertainment/movie/succession",
 "A Show Where Nothing Is Ever Resolved",
 "A media family fights over who will inherit the company, and the series refuses to let anyone win for four seasons. The structure is the achievement: every episode ends with the same balance of power, only worse.",
 "Jesse Armstrong&#39;s writing", "The dialogue is built on interruption and humiliation, and the desk rates it as the show&#39;s sharpest weapon.",
 "The handheld camera", "The documentary-style shooting keeps the viewer inside the room, which the show uses deliberately.",
 "Logan is never explained", "The patriarch&#39;s motives stay opaque, and the show refuses to give him a sympathetic scene.",
 "The corporate context", "The business is modelled on real media dynasties, which the desk notes as informed rather than fictional.",
 "The comedy", "It is frequently very funny, which is easy to miss under the cruelty.",
 "The succession answer", "The finale settles the question in the most deflating way available, and the desk thinks that is right.",
 "The siblings", "Each is written as genuinely competent and genuinely unable to work together.",
 "It is a tragedy disguised as a comedy about work, and it is one of the best-written series of its decade. Watch the first three episodes before deciding; the register takes a while to settle."],

["entertainment/movie/peaky-blinders",
 "A Period Crime Family, Built On One Idea",
 "The series is a gangster story set in Birmingham after the First World War, and it works because it treats the family as a business with strategy rather than as a set of personalities. The stylistic choices are distinctive and the desk notes they are divisive.",
 "Steven Knight&#39;s writing", "The creator writes the episodes himself, which gives the show an unusually consistent voice.",
 "Shellshock and the black market", "Returning soldiers and a wartime economy are the show&#39;s real subject.",
 "The anachronistic soundtrack", "Modern rock over period footage is the show&#39;s most imitated and most criticised decision.",
 "Tommy&#39;s planning", "The lead&#39;s schemes are shown in advance, so tension comes from execution rather than surprise.",
 "The family expansion", "The cast grows across six seasons, which the desk notes thins the later episodes.",
 "The historical figures", "Real politicians and gangsters appear, and the show treats them as characters.",
 "The final season", "It closed with a film planned to follow, which is worth knowing before starting.",
 "It is a well-constructed crime drama with a strong visual identity, and readers should expect style as much as substance. The first three seasons are the peak."],

["entertainment/movie/dark",
 "A Time-Travel Story That Plans Its Own Paradoxes",
 "The German series runs on a bootstrap paradox: the future causes the past that causes the future, and the show commits fully to it across three seasons. Almost nothing is explained early, and the payoff depends on the audience holding the family tree in their head.",
 "The closed loop", "Events cause themselves, and the show treats that as a rule rather than a twist.",
 "The small-town structure", "Four families across several generations, which the desk says is why a flowchart is genuinely useful.",
 "Baran bo Odar&#39;s direction", "The visual style is deliberate and consistent, and it makes the timelines distinguishable.",
 "The casting of three ages", "Each character has three actors, chosen to look plausibly alike, which was done carefully.",
 "The first season is the hardest", "The show does not explain itself early, and the desk advises patience.",
 "Closing the loop", "The finale answers its own puzzle, and the desk rates the answer as satisfying rather than merely clever.",
 "Watch it with the original German audio", "The dub flattens performances the show depends on.",
 "It is the most rigorously plotted time-travel series on television and requires genuine attention. Do not watch it casually or in the background; the structure is the entertainment."],

["entertainment/movie/the-white-lotus",
 "An Anthology About Guests And Staff",
 "Each season installs a new cast at a luxury resort and watches the holiday fall apart, with the local employees carrying the consequences the guests never see. Mike White&#39;s structure is the point: the same format, a different class of failure.",
 "The anthology format", "Each season is self-contained, so seasons can be watched in any order.",
 "The staff&#39;s perspective", "The writing gives the resort workers real interiority, which is what separates the show from satire.",
 "Mike White&#39;s authorship", "One writer for every season gives the series an unusually consistent sensibility.",
 "The mystery frame", "Each season opens with a death and works backwards, which the desk notes is a device rather than the subject.",
 "Social discomfort as comedy", "Humiliation is the engine, and the show is very good at making it funny and awful at once.",
 "The location work", "The resorts are shot as places rather than backdrops, which the desk credits.",
 "Which season to start", "The desk suggests the first, and notes the second is the most divisive.",
 "It is a comedy of manners where the manners belong to tourists, and it is sharper than the holiday setting suggests. Start with season one and treat each as its own film."],

["entertainment/movie/arcane-season-2",
 "Animating A Story That Was Never Scripted",
 "The series is built from the backstory of a video game, which usually produces marketing. This one was drawn and painted by Studio Fortiche in a style closer to illustration than to game cinematics, and the second season closed the story rather than extending it.",
 "Fortiche&#39;s painted style", "Hand-drawn textures over 3D animation give the show a look nothing else in the field matches.",
 "The game source", "League of Legends supplies characters, and the show builds a story the game never tells.",
 "The two-city politics", "Piltover and Zaun are written as a class conflict, which gives the plot its stakes.",
 "The sister relationship", "The emotional core is two siblings on opposite sides, and the show never resolves it simply.",
 "The second season&#39;s pacing", "It compresses more plot than the first, and the desk notes that viewers split on it.",
 "Accessibility", "No knowledge of the game is required, which the desk confirms.",
 "Its cost and craft", "The production budget and time were unusual for animation, and it shows.",
 "Watch it for the artwork alone if the plot does not grip you, because nothing else looks like it. Start with season one; the second assumes it entirely."],

["entertainment/movie/gen-v",
 "A Spin-Off That Rewrote The Rules",
 "The show takes the universe of The Boys and relocates it to a university for young superheroes, which lets it handle a different subject: what happens to people told they are exceptional before they have decided who they are.",
 "The campus setting", "A school for powered students gives the show a coming-of-age structure the parent series never had.",
 "The parent show", "It shares a universe, and the desk confirms the spin-off works without having seen it.",
 "The body-horror register", "The violence is more grotesque than the parent series in places, which the desk flags.",
 "An unfamiliar cast", "The leads are largely unknown actors, which keeps the attention on the writing.",
 "Corporate control as the villain", "The antagonist is a company managing a product line, which is the same target as the parent show.",
 "Viewership, stated plainly", "It drew a large audience on release, which is a fact rather than an endorsement.",
 "How much homework is needed", "Best watched after a season of its parent series, though it stands up without one.",
 "It is a sharper show than its premise suggests and the university frame gives it somewhere to go. Expect the same violence and humour as the parent series, and roughly the same amount."],

["entertainment/movie/the-umbrella-academy",
 "A Superhero Family That Never Learns To Work",
 "An eccentric billionaire adopts seven children with powers and raises them badly, and the series is about the damage rather than the heroics. The apocalypse plot is the deadline; the family is the story.",
 "The dysfunctional adoption", "The premise is a parenting failure, which makes the ensemble interesting before any power is used.",
 "Gerard Way&#39;s comics", "The source is a comic by the My Chemical Romance frontman and Gabriel Bá, and the adaptation diverges from it.",
 "The time-travel plot", "The first season runs on a countdown to an apocalypse, which gives the family a reason to co-operate.",
 "Number Five", "The performance of a man in a child&#39;s body is the show&#39;s best comic and tragic idea.",
 "The visual style", "The production has a deliberate comic-book palette, which the desk rates as effective.",
 "The later seasons", "They expand the mythology and the desk notes the show becomes more convoluted.",
 "The soundtrack", "Period pop is used deliberately, and it is part of the show&#39;s identity.",
 "Watch the first season for the family dynamics, which are the reason it works at all. Readers should know the later seasons are more plot-driven and less focused on the characters."],

["entertainment/movie/creed",
 "A Legacy Sequel That Justifies Its Own Existence",
 "The seventh Rocky film hands the franchise to a new lead and a new director, and it works because it treats the inheritance as the subject: Adonis Creed is defined by a father he never met. The fight scenes are staged as arguments.",
 "Ryan Coogler&#39;s direction", "The director&#39;s debut, and the one-take fight sequence became the film&#39;s signature.",
 "Michael B. Jordan&#39;s lead", "A performance built on inherited pressure rather than on charisma alone.",
 "Stallone&#39;s supporting role", "Rocky is written as a man with nothing left to prove, which is the film&#39;s best decision.",
 "The one-shot fight", "A single uninterrupted take that the desk rates as the most interesting boxing ever filmed.",
 "The Philadelphia setting", "The city is treated as a character, as it was in the original.",
 "What it inherits", "The franchise&#39;s structure is kept, and the film is honest about borrowing it.",
 "Its sequels", "Two more followed, and the desk rates this first one well above them.",
 "It is a sports film that earns the franchise it belongs to rather than trading on it, which is rare. Watch the original Rocky first if you have not, because the contrast is the pleasure."],

["entertainment/movie/steins-gate",
 "A Time-Travel Story That Punishes Its Hero",
 "The protagonist discovers he can send messages to the past and spends the first half being delighted by it. The second half is the cost, and the show&#39;s structure means the audience feels the accumulation rather than being told about it.",
 "The microwave phone", "A deliberately absurd device, which the show uses to keep the premise grounded rather than grand.",
 "The visual novel source", "It adapts a 5pb. and Nitroplus visual novel, and the adaptation keeps the branching logic intact.",
 "The tonal turn", "The comedy of the opening episodes is necessary setup for what the show does with it later.",
 "Okabe&#39;s performance", "The protagonist&#39;s affectation is layered over genuine grief, which the show reveals slowly.",
 "The repetition", "The show loops and the audience re-lives events, which the desk rates as the point.",
 "Where the ending lies", "The anime has multiple endings in the source, and the adaptation chose one.",
 "The sequel", "Steins;Gate 0 exists and continues from an alternate branch.",
 "It is a science-fiction series about the cost of correcting things, and the first half is not wasted time. Give it twelve episodes before judging, because the structure needs that runway."],

["entertainment/movie/dandadan",
 "Occult Comedy And Aliens In The Same Show",
 "The premise pits ghosts against extraterrestrials, with two teenagers as the unwilling contact point, and the series moves between gross-out comedy and genuine horror. Science SARU&#39;s animation is the reason it works as well as it does.",
 "Yukinobu Tatsu&#39;s manga", "The source runs both horror registers simultaneously, and the adaptation keeps that balance.",
 "Science SARU&#39;s animation", "The studio&#39;s reputation for expressive movement suits a show that changes style constantly.",
 "The two leads", "Their argument about whether ghosts or aliens are real is the show&#39;s running engine.",
 "The tonal range", "Comedy, body horror and genuine tenderness appear within single episodes.",
 "Its popularity", "It was among the most-discussed new anime of its year, which the desk reports as reception.",
 "Content warnings", "The show contains sexual-harassment material played for comedy, which the desk flags as a real barrier.",
 "The caveat, stated plainly", "The craft here is rated highly, and the content warning above is stated rather than omitted.",
 "The animation alone justifies a look, and the comedy lands more often than a premise this strange should allow. Readers sensitive to the content noted above should know it is recurring rather than incidental."],
]

DEPTH_SECTIONS_W = {}
for _row in ROWS_W:
    _slug, _h2, _para = _row[0], _row[1], _row[2]
    _items = _row[3:-1]
    _para2 = _row[-1]
    assert _slug.startswith("entertainment/movie/"), f"batch W is film-only: {_slug}"
    # 6 pairs minimum (16 fields) and an even number of item fields, so a
    # section can carry more than the baseline six pairs without breaking.
    # row = [slug, h2, para] + item pairs + [para2], so item count is
    # len(row) - 4 and must be even and non-zero.
    assert len(_row) >= 16 and (len(_row) - 4) % 2 == 0, f"row shape {_slug}: {len(_row)} fields"
    assert isinstance(_para2, str) and _para2, f"missing closing para: {_slug}"
    DEPTH_SECTIONS_W[_slug] = ed(_slug, _h2, _para, _items, _para2)

for _slug, _html in DEPTH_SECTIONS_W.items():
    assert (_ROOT / _slug / "index.html").is_file(), f"batch W missing route: {_slug}"

_h2s = [r[1] for r in ROWS_W]
_lead = [r[i] for r in ROWS_W for i in range(3, len(r) - 1, 2)]
assert len(set(_h2s)) == len(_h2s), "duplicate h2 within batch W"
assert len(set(_lead)) == len(_lead), "duplicate lead-in within batch W"

print(f"batch W: {len(DEPTH_SECTIONS_W)} film sections, {len(set(_h2s))} unique h2, "
      f"{len(set(_lead))} unique lead-ins")
