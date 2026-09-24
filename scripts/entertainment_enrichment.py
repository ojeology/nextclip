"""Desk enrichment for BRYME Entertainment film pages (batch 1, 2026-09-23).

What this is: the per-title editorial layer the generator template renders on
top of the factual record in entertainment_platform_data.py - a verdict (why
this film is or isn't worth your night, in the desk's own voice) and a short
FAQ built only from facts the desk keeps (director, year, runtime, language,
awards, order in a series). No time-sensitive claims: where-to-stream is
deliberately NOT stated here, because catalogues rotate by country and month
- the film pages link platform *searches*, labelled as searches.

How to extend: add a slug that exists in entertainment_platform_data.MOVIES
with the same spelling. Anything missing renders nothing - the template
degrades gracefully, so partial batches are safe to ship.

Verified: every key below matches a MOVIES slug; build-ecosystem.py fails
loudly (enrichment-audit print) if a key stops matching after a rename.
"""

ENRICH = {
    "dune-part-two": {
        "verdict": "The rare sequel that out-builds its predecessor. Villeneuve shoots "
            "desert warfare as physical, sun-scoured spectacle - no green-screen mush - "
            "and lets the political trap under the prophecy stay ugly. If the first "
            "Dune felt like a prologue, this is the film it was prologue to. Watch it "
            "biggest and loudest you can.",
        "faqs": [
            ("Is Dune: Part Two the end of the story?",
             "No. It adapts the second half of Frank Herbert's 1965 novel, but the book "
             "series continues - and a third film, Dune Messiah, is the planned next chapter."),
            ("Do I need to see the first Dune (2021) first?",
             "Yes. Part Two begins moments after Part One ends and assumes you know who "
             "Paul, the Fremen and the Harkonnens are. It is one story in two parts."),
            ("How long is Dune: Part Two?",
             "166 minutes. Go easy on the super-sized drink."),
        ],
    },
    "oppenheimer": {
        "verdict": "A three-hour talky biopic that plays like a horror film. Nolan strands "
            "you in the head of the man who built the bomb and makes the committee rooms "
            "feel as tense as any battlefield. Cillian Murphy holds the centre for every "
            "minute. Demands attention, not snacks - and rewards it.",
        "faqs": [
            ("Did Oppenheimer win the Oscars?",
             "Yes - seven at the 2024 ceremony, including Best Picture, Best Director "
             "(Christopher Nolan) and Best Actor (Cillian Murphy)."),
            ("Is Oppenheimer based on a book?",
             "Yes - American Prometheus, the 2005 Pulitzer-winning biography by Kai Bird "
             "and Martin J. Sherwin."),
            ("Why is it three hours long, and is it slow?",
             "It runs 180 minutes across three timelines, but the pacing is the point: "
             "the hearings and the Trinity test feed each other. It is dense, not slow."),
        ],
    },
    "interstellar": {
        "verdict": "Nolan's most emotional film, and still his most divisive. The physics "
            "is real, the score is enormous, and the father-daughter story lands because "
            "the film commits to it completely. The docking scene and the tesseract remain "
            "two of the great big-screen sequences. Melodrama? Sometimes. Worth it? Every time.",
        "faqs": [
            ("Is the science in Interstellar real?",
             "The relativity, wormhole and black-hole visuals were guided by physicist Kip "
             "Thorne (Nobel laureate) - the black hole Gargantua was rendered from actual "
             "equations. The later plot leans into speculation, not textbook physics."),
            ("What is the runtime of Interstellar?",
             "169 minutes, including the ending that splits audiences. Stay for the score."),
            ("Is Interstellar connected to the Dune films?",
             "No - different studios, directors and universes. The link people remember is "
             "Hans Zimmer, who scored both."),
        ],
    },
    "godzilla-minus-one": {
        "verdict": "The best Godzilla film in decades, and the best argument that spectacle "
            "does not need a Hollywood budget. Post-war Japan is the real subject - grief, "
            "shame, and a country deciding to live again - with the monster as the test. "
            "The visuals would shame films at ten times the cost.",
        "faqs": [
            ("Did Godzilla Minus One really win an Oscar?",
             "Yes - Best Visual Effects at the 2024 ceremony, the first Oscar in the "
             "franchise's seventy-year history, on a reported budget around 15 million dollars."),
            ("Do I need to watch other Godzilla films first?",
             "No. Minus One is a standalone restart, set just after World War Two, with no "
             "connection to the Monsterverse or any earlier continuity."),
            ("Is it subtitled?",
             "Yes - it is a Japanese production, shot in Japanese. The 2024 black-and-white "
             " theatrical re-cut, Minus One/Minus Color, is the same film."),
        ],
    },
    "top-gun-maverick": {
        "verdict": "The legacy sequel that solved the format: honour the original, add one "
            "impossible mission, and film every G-force for real. Tom Cruise carries it with "
            "total sincerity, the aerial sequences are the genuine article, and the film "
            "knows exactly what a crowd wants and delivers it without irony.",
        "faqs": [
            ("Did the actors really fly the jets in Top Gun: Maverick?",
             "The actors flew in real F/A-18s as passengers with Navy pilots - up to about "
             "7.5 Gs - with cameras mounted in the cockpits. Actors cannot legally fly the "
             "fighter themselves; the dogfights are stitched from real footage."),
            ("Do I need to see the 1986 Top Gun first?",
             "It helps but is not required. The film recaps who Maverick is within minutes; "
             "the returning characters land harder if you know the original."),
            ("What is the runtime of Top Gun: Maverick?",
             "130 minutes - lean by modern blockbuster standards."),
        ],
    },
    "avengers-endgame": {
        "verdict": "A three-hour payoff that shouldn't work as well as it does. It is less "
            "a film than a structural magic trick - twenty-two movies folded into one "
            "farewell - and the time heist gives it a lightness the genre usually forgets. "
            "As spectacle it is enormous; as an ending for Captain America and Iron Man, "
            "it earns its tears.",
        "faqs": [
            ("How many Marvel films do I need before Endgame?",
             "The essential run is roughly Infinity War first - Endgame is its direct "
             "sequel. Deeper cuts (Civil War, Winter Soldier, Ragnarok) enrich the payoffs, "
             "but the film assumes Infinity War above all."),
            ("How long is Avengers: Endgame?",
             "181 minutes - the longest film in the Infinity Saga."),
            ("Was Endgame really the highest-grossing film ever?",
             "It set the record on release in 2019, passing 2.7 billion dollars, and held "
             "the top spot until Avatar retook it after a re-release."),
        ],
    },
    "spider-man-no-way-home": {
        "verdict": "A fan-service engine with a genuine heart. The multiverse premise could "
            "have been a catalogue cameo parade; instead the film makes returning villains "
            "carry themes of redemption and consequence. Holland's best Spider-Man film "
            "because it is finally about something: what it costs to be known.",
        "faqs": [
            ("Which Spider-Man films should I watch before No Way Home?",
             "At minimum: Far From Home (2019), which it directly follows, and the previous "
             "five live-action Spider-Man films from the other two franchises for the cameos "
             "to land. It is built as a finale to all of them."),
            ("How long is No Way Home?",
             "148 minutes, with a credits scene that sets up the next chapter."),
            ("Did No Way Home break box-office records?",
             "It became the biggest film of 2021 and one of the highest-grossing films ever, "
             "remarkable for a release that arrived mid-pandemic."),
        ],
    },
    "everything-everywhere-all-at-once": {
        "verdict": "Maximum chaos, minimum cynicism. The Daniels hurl multiverse gags, "
            "hot-dog fingers and bagel nihilism at a story about an immigrant family that "
            "cannot say it loves itself - and somehow the silly and the sincere fuse. "
            "Ke Huy Quan and Jamie Lee Curtis are glorious. The year's most alive film.",
        "faqs": [
            ("What did Everything Everywhere All at Once win at the Oscars?",
             "Seven awards at the 2023 ceremony, including Best Picture, Best Director, "
             "Best Actress (Michelle Yeoh), and Best Supporting Actor for Ke Huy Quan."),
            ("Is it confusing to follow?",
             "It moves fast and jumps freely between universes, but the emotional throughline "
             "- a failing laundromat family at tax time - is always on screen. Trust the film."),
            ("Why is it rated R?",
             "For some violence, language and sexual references - it is an absurdist adult "
             "comedy, not a family superhero film, despite the multiverse trappings."),
        ],
    },
    "the-grand-budapest-hotel": {
        "verdict": "Wes Anderson's most perfectly tuned machine: a confectionery-coloured "
            "caper about civilisation losing to brutality, told with total formal control. "
            "Fiennes' M. Gustave is the performance of Anderson's career. Funny, precise, "
            "and quietly heartbroken underneath the symmetry.",
        "faqs": [
            ("What are the different aspect ratios in The Grand Budapest Hotel for?",
             "Time layers: the 1930s story plays in the old Academy ratio, the 1960s scenes "
             "in widescreen, and the 1980s frame in modern widescreen. The format ages with "
             "the storytelling."),
            ("Is The Grand Budapest Hotel based on a real hotel?",
             "No - the hotel and Zubrowka are invented, inspired by the works of novelist "
             "Stefan Zweig rather than any single real place."),
            ("How long is it?",
             "99 minutes - one of Anderson's tightest."),
        ],
    },
    "1917": {
        "verdict": "Mendes builds the First World War as one continuous tracked shot, and "
            "the gimmick is the point: no cuts means no escape. You trudge every yard with "
            "two messengers carrying a deadline. Roger Deakins' camerawork won the Oscar "
            "and deserved it. An experience more than a story - and a staggering one.",
        "faqs": [
            ("Is 1917 really one continuous shot?",
             "It is edited to appear as one unbroken take - hidden cuts hide in darkness "
             "and crossings. The longest true on-set takes ran roughly eight to nine minutes."),
            ("Is 1917 based on a true story?",
             "Not on specific soldiers, but on Operation Alberich-style strategic German "
             "retreats in 1917 and real messenger-runner accounts the director heard from "
             "his great-grandfather."),
            ("How long is 1917?",
             "119 minutes, built to feel like roughly two hours of real time."),
        ],
    },
    "300": {
        "verdict": "Zack Snyder's comic-panel colosseum - history as gym playlist. As "
            "history it is propaganda; as pure stylised combat it is still unmatched two "
            "decades on, all bronze and blood and bellowing. Take it on those terms and "
            "it delivers exactly what it sells. THIS. IS. SPARTA remains a great time.",
        "faqs": [
            ("Is 300 historically accurate?",
             "Heavily stylised, no. It adapts Frank Miller's comic, itself loose legend: "
             "the real Thermopylae stand was a few days, with roughly 7,000 Greeks holding "
             "the pass before the famous 300 Spartans' last stand."),
            ("What is the runtime of 300?",
             "117 minutes - it does not outstay its welcome."),
            ("Is there a sequel?",
             "Yes - 300: Rise of an Empire (2014), which runs parallel to the first film's "
             "events at sea. Most viewers find the original the stronger picture."),
        ],
    },
    "2001-space-odyssey": {
        "verdict": "The monolith of science-fiction cinema. Kubrick's 1968 epic still "
            "out-imagines films made this century: the bone-cut, the rotating station, "
            "HAL's quiet murder, the star-child. It is slow, cold and deliberately "
            "unknowable - and absolutely essential. The best possible screen for it is "
            "the biggest one you can find, lights off, phone in another room.",
        "faqs": [
            ("What does the ending of 2001: A Space Odyssey mean?",
             "Kubrick refused to explain it. The standard reading: the Star Child is "
             "humanity's next evolutionary step after Bowman's journey through the "
             "monolith's star gate - a rebirth the film shows rather than states."),
            ("Is 2001 based on a book?",
             "In parallel - Arthur C. Clarke wrote the novel and the screenplay alongside "
             "the film's production, both loosely expanding his 1951 short story The Sentinel."),
            ("Why does 2001 look so good for its age?",
             "Practical front-projection, enormous sets and slit-scan photography - no "
             "digital effects existed. The craft still holds up against modern CGI."),
        ],
    },
    "baahubali-the-beginning": {
        "verdict": "Indian grande spectacle at full power: a mythic revenge epic staged "
            "with waterfall rescues, bull-ramp charges and absolute conviction. S.S. "
            "Rajamouli treats scale as a promise, not a tease, and the intermission twist "
            "is one of Indian cinema's great curtain-drops. The beginning half of one "
            "enormous story - part two pays everything off.",
        "faqs": [
            ("Do I watch Baahubali: The Beginning or The Conclusion first?",
             "The Beginning (2015) first, always - The Conclusion (2017) is its direct "
             "sequel and resolves the cliffhanger the first film famously ends on."),
            ("What language is Baahubali in?",
             "Shot simultaneously in Telugu and Tamil, with dubbed releases in Hindi and "
             "many other languages - the Hindi version made it a pan-India phenomenon."),
            ("Is Baahubali based on mythology?",
             "It is original fiction built from Mahabharata-style mythic architecture - "
             "not a retelling of any single epic."),
        ],
    },
    "half-of-a-yellow-sun": {
        "verdict": "Chimamanda Ngozi Adichie's Biafran saga on screen, carried by "
            "Chiwetel Ejiofor and Thandiwe Newton through love, class and civil war. The "
            "novel's scope resists two hours and the film occasionally hurries its years - "
            "but the history matters, the performances hold, and Nigerian cinema of this "
            "ambition deserves the audience.",
        "faqs": [
            ("Is Half of a Yellow Sun based on a book?",
             "Yes - Chimamanda Ngozi Adichie's 2006 Orange Prize-winning novel about the "
             "Biafran war. The film adaptation arrived in 2013, directed by Biyi Bandele."),
            ("What is the film about?",
             "Twin sisters from a wealthy Nigerian family, their loves and losses across "
             "the 1960s, as the breakaway state of Biafra descends into war and famine."),
            ("Where can I watch Half of a Yellow Sun?",
             "Availability rotates by country - the film page's platform links above are "
             "labelled searches precisely so you check your own region's catalogue."),
        ],
    },
    "living-in-bondage-breaking-free": {
        "verdict": "The 1992 classic that effectively launched Nollywood home video, "
            "reborn as a 2019 prestige sequel about the children of the original's cult. "
            "It works as both a thriller and a hand-over-of-history - money, faith and "
            "the price both exact. Watch the original first for the full weight.",
        "faqs": [
            ("Do I need the 1992 Living in Bondage first?",
             "Strongly recommended - the sequel is built on the original's cult story and "
             "its consequences a generation later, and Nollywood history gives it weight."),
            ("What is Living in Bondage: Breaking Free about?",
             "A young Lagosian chasing wealth is pulled into his father's old secret cult - "
             "the same path that destroyed his family decades before - and must find his "
             "way out."),
            ("Is it a Nollywood film?",
             "Yes - a landmark one: the original 1992 film is widely credited with "
             "igniting Nigeria's home-video industry, and this 2019 sequel was one of "
             "the country's biggest theatrical releases."),
        ],
    },
    "mission-impossible-the-final-reckoning": {
        "verdict": "Cruise closes the account with the series' most deliberate entry - "
            "slower, talkier, then detonating into set pieces (the biplane is the one "
            "you've heard about) that no younger franchise would attempt for real. Not "
            "the pure adrenaline of Fallout; the victory lap of the greatest stunt "
            "franchise ever built. Stay for the plane.",
        "faqs": [
            ("Is The Final Reckoning a direct sequel?",
             "Yes - it continues Dead Reckoning (2023) immediately, same villain, same "
             "key, Hunt's past catching up wholesale. Watch Dead Reckoning first."),
            ("Did Tom Cruise really fly the biplane?",
             "He performed the aerial stunt work strapped to a real 1930s biplane after "
             "extensive flight training; the most dangerous shots are genuinely him in "
             "the air, per the production's released footage."),
            ("How long is it?",
             "169 minutes - the longest entry in the series."),
        ],
    },
    "the-batman": {
        "verdict": "A detective story that actually detects. Reeves plays Batman as a "
            "noir investigator locked in a city-wide riddle, with Pattinson finding the "
            "grief and obsession under the cowl and Paul Dano's Riddler genuinely "
            "unsettling. Three hours of rain, corruption and mood - the moodiest "
            "mainstream superhero film ever green-lit, and a better crime film than "
            "most actual crime films.",
        "faqs": [
            ("Is The Batman connected to the DC films with Ben Affleck's Batman?",
             "No. It is a standalone reboot with its own younger Batman, separate from "
             "both the old DCEU and the newer DCU films."),
            ("Is The Batman based on a comic storyline?",
             "It is an original mystery built from noir comics DNA - Year One, The Long "
             "Halloween and Ego are the clear touchstones rather than any single "
             "adaptation."),
            ("Is there a sequel?",
             "Yes - The Batman Part II is in development, and the HBO series The "
             "Penguin (2024) continues this version of Gotham in the meantime."),
        ],
    },
    "avatar-the-way-of-water": {
        "verdict": "Cameron builds the ocean of Pandora as a place you can live in, and "
            "the middle hour - learning to swim, ride, and breathe with the reef people "
            "- is the film's secret best part. Story-wise it is a familiar family-on-"
            "the-run tale; visually it is the new benchmark. The third act is one of "
            "the great sustained action sequences. See it on the biggest screen that "
            "exists near you.",
        "faqs": [
            ("Do I need to see the first Avatar before The Way of Water?",
             "Yes - it continues Jake and Neytiri's story thirteen years on, and the "
             "returning villain only lands if you know how the first film ended."),
            ("Was it really filmed underwater?",
             "The performers trained in free-diving and performed much of the water "
             "work in a massive tank, with genuine breath-holds of several minutes - "
             "Cameron refused dry-for-wet for the swimming scenes."),
            ("How long is The Way of Water?",
             "192 minutes - bring patience and skip the large soda."),
        ],
    },
    "barbie": {
        "verdict": "The rare four-quadrant blockbuster with an actual argument. Gerwig "
            "turns an IP joke into a funny, satirical and disarmingly sincere look at "
            "womanhood, branding and death - yes, death. Gosling's Ken is a comedic "
            "avalanche, Robbie holds the heart, and the film keeps its intelligence "
            "even while selling it. Hollywood's most surprising hit of the decade.",
        "faqs": [
            ("Is Barbie suitable for children?",
             "Mostly - it is PG-13 for suggestion and language. Younger kids enjoy the "
             " visuals and gags; the themes about identity and patriarchy fly past them, "
             "which is fine, the film plays on two levels on purpose."),
            ("Did Barbie really out-gross a billion dollars?",
             "It became the highest-grossing film of 2023, passing 1.4 billion dollars "
             "worldwide - the first film directed solely by a woman to cross a billion."),
            ("What is the song from Barbie?",
             "Two took over 2023: What Was I Made For? by Billie Eilish (which won the "
             "Oscar) and I'm Just Ken, sung by Ryan Gosling."),
        ],
    },
    "dune": {
        "verdict": "Part One is the prologue, and Villeneuve knows it - a slow, "
            "awe-drenched establishment of world, ecology and dread that trusts you to "
            "wait for the story. Not a complete film on its own; a magnificent one. "
            "Watch it back-to-back with Part Two if you can - together they are the "
            "best big-screen science fiction of this century so far.",
        "faqs": [
            ("Why does Dune (2021) end so abruptly?",
             "The novel's first half simply does not resolve, and Villeneuve refused to "
             "compress it. The studio greenlit Part Two after release, so the story "
             "continues exactly where this stops."),
            ("Is Dune hard to follow for newcomers?",
             "Keep two things in mind - the spice is everything, and Paul's visions are "
             "not flashbacks - and the rest unfolds clearly. It is slower than typical "
             "blockbusters, not more complicated."),
            ("Is the 2021 Dune a remake of the 1984 film?",
             "It is a new adaptation of Frank Herbert's 1965 novel, covering roughly "
             "the same ground as David Lynch's 1984 version but in far more depth."),
        ],
    },
    "no-time-to-die": {
        "verdict": "Craig's goodbye is the longest Bond and the most emotional - a "
            "retirement-that-won't-stick story that finally admits this Bond has been "
            "one continuous tragedy. Safin is a thin villain; the film around him is "
            "lavish, funny when it needs to be, and genuinely moving at the end. The "
            "send-off the era earned.",
        "faqs": [
            ("Do I need to have seen the other Daniel Craig Bond films?",
             "Yes for full effect - No Time to Die closes the story that began in Casino "
             "Royale and directly references SPECTRE and Vesper. It is an ending, not a "
             "standalone mission."),
            ("How did No Time to Die end Craig's era?",
             "Without spoiling it: definitively. It is the first Bond film to end the "
             "lead actor's run by story choice rather than recasting, and the finale is "
             "the reason to have watched all five."),
            ("How long is it?",
             "163 minutes - the longest film in the franchise."),
        ],
    },
    "tenet": {
        "verdict": "Nolan's most forbidding puzzle: time-inverted combat staged with "
            "real planes, real ships and zero explanation pauses. Watch it once for the "
            "spectacle, once for the structure - it is built to be re-watched, and it "
            "knows it. Cold characters, dazzling craft. If Inception is Nolan "
            "explaining his trick, Tenet is him refusing to.",
        "faqs": [
            ("Do I need to understand every plot point to enjoy Tenet?",
             "No - the film is designed so the mission logic stays ahead of you and the "
             "physical spectacle stays legible. The palindrome structure rewards a "
             "second viewing more than a paused first one."),
            ("Was the plane crash in Tenet real?",
             "Yes - Nolan bought a real Boeing 747 and crashed it into a hangar on "
             "camera rather than building the sequence with miniatures or CGI."),
            ("Is Tenet a sequel to Inception?",
             "No connection - different rules, cast and studio characters. What they "
             "share is a director fascinated by time and practical scale."),
        ],
    },
    "mad-max-fury-road": {
        "verdict": "Two hours of diesel and chrome that redefined what an action film "
            "could be: one long chase, edited like a drum solo, with a feminist "
            "escape story hiding in plain sight. Miller shot real cars in a real "
            "desert and it shows in every frame. Furiosa is the soul; the Doof "
            "Warrior is the culture. A perfect film wearing a grill.",
        "faqs": [
            ("Do I need to watch the older Mad Max films first?",
             "No - Fury Road is a self-contained story set after the originals, and it "
             "recaps what matters in the first ten minutes. Knowing Road Warrior adds "
             "flavour, not plot."),
            ("Was Fury Road really shot with practical effects?",
             "Over 95 percent of the stunts and vehicles are real - the fleet actually "
             "drove through the Namib desert. CGI was used to stitch and enhance, not "
             "to invent."),
            ("Which comes first, Fury Road or Furiosa?",
             "Furiosa (2024) is a prequel about the younger Furiosa. Watch Fury Road "
             "first - it is the better film and the prequel lands harder with the "
             "character already mythic."),
        ],
    },
    "deadpool-wolverine": {
        "verdict": "The MCU's contractually obligated good time: Reynolds' motor mouth "
            "and Jackman's claws spending three hours insulting corporate synergy while "
            "delivering exactly the fan-service carnival it promises. The plot is a "
            "clothesline for gags, cameos and one genuinely great Needle-in-the-haystack "
            "soundtrack. As a multiverse apology tour, it is shockingly fun.",
        "faqs": [
            ("Is Deadpool & Wolverine suitable for kids?",
             "No - it is R-rated for extreme gore and language, the first R-rated film "
             "in the MCU. It is also the highest-grossing R-rated film ever, so the "
             "adults turned out."),
            ("Do I need to watch the old Fox Marvel films?",
             "Not strictly - but the joke lands far harder if you have seen at least "
             "the earlier X-Men films and the two previous Deadpools. It is a farewell "
             "to that entire era."),
            ("Is Hugh Jackman's Wolverine the same one from the X-Men films?",
             "A variant of him - the yellow suit is new, the grumpiness is not. The "
             "film leans fully into Jackman having played the role for a quarter century."),
        ],
    },
    "furiosa-a-mad-max-saga": {
        "verdict": "Miller trades Fury Road's two-hour engine for a five-chapter revenge "
            "epic, and the gamble mostly pays: Anya Taylor-Joy rebuilds the character "
            "from the wound up, Chris Hemsworth's warlord is all theatre and teeth, and "
            "the counterpart/stolen-vehicle set pieces are among the saga's best. It is "
            "slower, longer and sadder - a western in the wasteland, and a worthy one.",
        "faqs": [
            ("Is Furiosa a sequel or a prequel?",
             "A prequel - it tells the origin of Imperator Furiosa years before Fury "
             "Road, from her childhood in the Green Place to her rise among Immortan "
             "Joe's war boys."),
            ("Why did Charlize Theron not play Furiosa again?",
             "The story begins with the character as a child, and the decade between "
             "the films made de-ageing impractical; Anya Taylor-Joy takes the role, "
             "with Alyla Browne playing the young Furiosa."),
            ("Do I need Fury Road first?",
             "It works either way, but Fury Road first is the better experience - the "
             "prequel keeps answering questions you have not yet asked."),
        ],
    },
    "mission-impossible-fallout": {
        "verdict": "The series' high-water mark and arguably the best pure action film "
            "of its decade: a broken-glass plot (Cruise broke his ankle filming the "
            "roof jump and the take is in the movie) strung between a real HALO jump, "
            "a real helicopter chase and Cavill reloading his arms like steam pistons. "
            "Every action film since has been graded against it.",
        "faqs": [
            ("Did Tom Cruise really break his ankle in Fallout?",
             "Yes - jumping between buildings in London; he finishes the take, and the "
             "injury pushed the release date. The shot made the final cut."),
            ("Do I need to see the earlier Mission: Impossible films first?",
             "Fallout is the only entry that is a true direct sequel (to Rogue Nation), "
             "so seeing that one first helps. Everything else you need is restated."),
            ("Is Henry Cavill's character the villain?",
             "Without spoiling the twist: his August Walker is the story's agent of "
             "chaos, and the bathroom fight is one of the great two-hander brawls."),
        ],
    },
    "mission-impossible-dead-reckoning": {
        "verdict": "The setting-of-the-table half of the finale, and better than its "
            "reputation: a genuinely clever AI-era espionage plot, the runaway-train "
            "set piece as a nine-minute masterclass, and a Pompeii of practical "
            "motorcycle stunting that Cruise jumped off a Norwegian cliff to earn. "
            "It ends mid-sentence - by design - so watch it as Act One of one film.",
        "faqs": [
            ("Does Dead Reckoning have an ending?",
             "It resolves this film's mission but ends with the larger story open - the "
             "conclusion arrives in The Final Reckoning (2025). Think of them as one "
             "epic split in two."),
            ("Did Tom Cruise really jump the motorcycle off the cliff?",
             "Yes - after a year of base-jump and motocross training he performed the "
             "cliff jump on camera for real; the production documented the training "
             "extensively. It is the film's centrepiece for a reason."),
            ("What is The Entity in Dead Reckoning?",
             "The villain is a rogue artificial intelligence the world's spies are "
             "fighting to control - the series' most contemporary antagonist, and the "
             "reason everyone wants the same key."),
        ],
    },
    "fast-x": {
        "verdict": "The franchise's Late Roman phase: everyone returns, physics has "
            "formally resigned, and Jason Momoa's Dante chewishes his way into the "
            "all-time villain ranks. As cinema it is ridiculous; as the first half of "
            "a two-part ending it does its job - big family stakes, big set pieces, "
            "one cliffhanger to end them all. The hell of it is: it works.",
        "faqs": [
            ("Is Fast X the last Fast & Furious film?",
             "Not quite - it is part one of the planned finale, ending on a major "
             "cliffhanger the concluding film resolves."),
            ("Who is Dante in Fast X?",
             "Jason Momoa plays Dante Reyes, the son of Fast Five's drug lord, taking "
             "his revenge on Dom's family a decade on - the franchise's most theatrical "
             "villain since Decker."),
            ("Do I need to have seen Fast Five?",
             "Fast Five (2011) is essential - Fast X is a direct revenge sequel to it, "
             "and the vault run everyone remembers is the debt being repaid."),
        ],
    },
    "blade-runner-2049": {
        "verdict": "The sequel nobody asked for that arrived as one of the most "
            "beautiful science-fiction films ever made. Villeneuve and Deakins build "
            "Villeneuve's Los Angeles out of orange fog and ruin, Gosling plays the "
            "hollow man finding a soul, and it has the nerve to be slow, sad and "
            "three hours long. A box-office misfire and a future classic - time has "
            "already voted.",
        "faqs": [
            ("Do I need to see the original Blade Runner (1982) first?",
             "Yes - 2049's entire plot rests on the first film's central mystery, and "
             "one returning character means nothing without the original. It is a "
             "direct sequel set thirty years on."),
            ("Why did Blade Runner 2049 flop at the box office?",
             "A three-hour, austere art film sold as a blockbuster - audiences stayed "
             "away despite acclaim. Its reputation has only grown since, and it won "
             "two Oscars including cinematography."),
            ("How long is Blade Runner 2049?",
             "164 minutes. Clear the evening; the film earns every minute."),
        ],
    },
    "the-martian": {
        "verdict": "The cheeriest survival story ever filmed about a man alone on "
            "Mars - Scott plays the science as triumph, Damon plays botanist-as-"
            "MacGyver with exactly enough gallows humour, and the world-cooperation "
            "backbone gives it a warmth genre rarely attempts. 'Science the s--- out "
            "of this' remains the most useful life advice in modern cinema.",
        "faqs": [
            ("Is The Martian scientifically accurate?",
             "Largely, by design - Andy Weir's novel built the survival problems from "
             "real chemistry and orbital mechanics, and the film keeps them. The big "
             "liberty is the storm: Mars' atmosphere is far too thin for that wind."),
            ("Is The Martian based on a book?",
             "Yes - Andy Weir's self-published 2011 novel, which became a bestseller "
             "and then this film; the book's maths and humour both survive the move."),
            ("Is The Martian funny?",
             "Surprisingly, yes - Damon's stranded botanist narrates his own possible "
             "death with sitcom timing. It is a comedy about not dying."),
        ],
    },
    "arrival": {
        "verdict": "A first-contact film where the weapon is linguistics. Villeneuve "
            "turns deciphering an alien grammar into an emotional mystery, Adams "
            "gives one of the decade's great performances, and the twist - about time, "
            "grief and choosing it anyway - re-frames everything you have watched. "
            "Cerebral, humane, quietly devastating.",
        "faqs": [
            ("Is Arrival based on a book?",
             "Yes - Ted Chiang's acclaimed 1998 novella Story of Your Life, which the "
             "film follows remarkably closely, including its central idea."),
            ("What are the aliens in Arrival actually asking?",
             "Without spoiling: the film is less about why they came than about what "
             "learning their language does to the person studying it. The question "
             "and the answer are the same thing - watch for it."),
            ("Does Arrival have a twist ending?",
             "It has a structural revelation rather than a twist - a fact about the "
             "story's timeline that re-casts the whole film as a different, sadder, "
             "braver story than it first appeared."),
        ],
    },
    "a-quiet-place": {
        "verdict": "Krasinski's high-concept pressure cooker: monsters that hunt by "
            "sound, a family surviving in silence, and a film that makes a cinema "
            "audience hold its own breath. It runs lean, it trusts gesture over "
            "dialogue, and Blunt gives the genre its best scream-queen mother in "
            "decades. The bathtub sequence alone earns classic status.",
        "faqs": [
            ("Why can't they talk in A Quiet Place?",
             "The creatures are blind and hunt exclusively by sound, so any noise "
             "brings a lethal response within seconds. The film's rule is total: the "
             "family communicates in sign language and bare feet."),
            ("Is A Quiet Place very scary?",
             "It is a tension film more than a gore film - relentless, jumpy and "
             "very loud in exactly the moments you are holding your breath. Suitable "
             "for teen horror fans; tough for younger kids."),
            ("Is there a sequel?",
             "Yes - A Quiet Place Part II (2021) continues the family's story the "
             "morning after, and Day One (2024) is a prequel about the first day of "
             "the invasion in New York."),
        ],
    },
    "hereditary": {
        "verdict": "The scariest film of its decade, and the least interested in "
            "scaring you cheaply. Aster builds grief, inheritance and family "
            "dysfunction into a slow occult nightmare where the horror is structural "
            "- you dread what the film is becoming. Collette's performance is a "
            "career peak. You will not sleep; you will not forget it either.",
        "faqs": [
            ("How scary is Hereditary compared to other horror films?",
             "It trades jump-scare volume for accumulating dread - most viewers find "
             "it deeply unsettling rather than constantly startled, with a handful "
             "of images (the telephone pole, the garage) that rank among the genre's "
             "worst nightmares."),
            ("Is Hereditary part of a series?",
             "It is the first of Ari Aster's unrelated 'family trauma as horror' "
             "films - Midsommar follows as a standalone, sharing themes but no "
             "story."),
            ("What is actually happening in Hereditary?",
             "On rewatch the film is unusually explicit: a family is a chosen "
             "vessel for a cult's summoning, and every tragedy doubles as ritual. "
             "The horror is that the grief was scheduled."),
        ],
    },
    "get-out": {
        "verdict": "Peele's debut remains a perfect machine: a satire of liberal "
            "racism wrapped in a stepford-servants thriller, funnier and angrier "
            "than its awards reputation suggests. Kaluuya's teacup hypnosis scene "
            "is the decade's great performance-under-duress. The sunken place "
            "entered the language; the film earned it. Mandatory.",
        "faqs": [
            ("Is Get Out a horror film or a comedy?",
             "Both, deliberately - Peele calls it a social thriller, and the comedy "
             "(Lil Rel Howery's TSA agent) is the pressure valve that makes the "
             "horror land harder. It won the Oscar for Best Original Screenplay."),
            ("Is Get Out based on a true story or a book?",
             "It is an original screenplay - its ideas come from American racial "
             "history rather than any novel, which is why the metaphors feel so "
             "precise."),
            ("What does the sunken place mean?",
             "It is the film's image of being paralysed inside yourself while "
             "someone else steers - read by audiences as a metaphor for Black "
             "experience in white spaces. Peele built it to be felt first, "
             "interpreted after."),
        ],
    },
    "nosferatu": {
        "verdict": "Eggers remakes the 1922 Dracula unauthorised classic as a dark "
            "fairy-tale fever dream - candlelight compositions, plague-rat texture, "
            "and Skarsgård's Orlok buried so deep in voice and prosthetic it is a "
            "haunting, not a performance. Depp carries the possession arc with real "
            "conviction. Slow-burn gothic for people who want atmosphere over "
            "scares.",
        "faqs": [
            ("Is Nosferatu (2024) a remake?",
             "It is Robert Eggers' new adaptation of the same 1897 Dracula material "
             "the forbidden 1922 German silent adapted - the second official "
             "unauthorised nod to the film that survived a court order to be "
             "destroyed."),
            ("How scary is Nosferatu compared to Eggers' other films?",
             "It is his most conventionally frightening - The Lighthouse and The "
             "VVitch are stranger and slower, while Nosferatu deploys full gothic "
             "horror machinery alongside the historical texture."),
            ("Who plays Count Orlok?",
             "Bill Skarsgård, near-unrecognisable under prosthetics and a "
             "manipulated voice - the same actor behind the modern Pennywise."),
        ],
    },
    "parasite": {
        "verdict": "The perfect film? A comedy of manners that climbs a staircase "
            "into a horror film without changing key, Bong's architecture is the "
            "screenplay - every level of Seoul is a class argument you can draw. "
            "Funny, furious, and cruelly precise, it became the first non-English "
            "language Best Picture winner and deserved that and more. Everyone "
            "should see it once a year.",
        "faqs": [
            ("What language is Parasite in?",
             "Korean, with the official English title Parasite; the original title "
             "is Gisaengchung. Subtitles did not stop it becoming a global "
             "phenomenon."),
            ("Why did Parasite win Best Picture?",
             "It swept the 2020 Oscars - Best Picture, Director, Original "
             "Screenplay and International Film - the first non-English language "
             "film ever to win the top prize, on the strength of a screenplay that "
             "works as thriller, comedy and class essay at once."),
            ("Is Parasite based on a true story?",
             "No - it is an original screenplay. Its power comes from how ordinary "
             "its premise is: one family conning its way into another's home, and "
             "what the arrangement exposes."),
        ],
    },
    "train-to-busan": {
        "verdict": "The zombie film reinvented as a class-conscious express train - "
            "gorgeous, relentless choreography where every car of the train is a "
            "new social experiment, and Gong Yoo's hedge-fund dad gives it a soul "
            "worth saving. It does in 118 minutes what most zombie shows cannot in "
            "seasons: make you care who lives. The best gateway into Korean genre "
            "cinema.",
        "faqs": [
            ("Is Train to Busan in Korean with subtitles?",
             "Yes - a Korean production (Busanhaeng), and the 2016 animated "
             "prequel Seoul Station is its companion piece."),
            ("Is Train to Busan very gory?",
             "It is intense and occasionally bloody, but its fame rests on speed "
             "and emotion rather than gore - the set pieces are choreographed like "
             "action cinema, not torture horror."),
            ("Is there a sequel?",
             "Yes - Peninsula (2020) continues the outbreak four years later with a "
             "new cast; most fans rate the original the stronger film."),
        ],
    },
    "squid-game": {
        "verdict": "The global phenomenon earned it: childhood games restaged as "
            "debtors' roulette, with production design so seductive the violence "
            "lands like betrayal. It is sharpest as economics by other means - "
            "every game is a loan contract - and its giant doll is already "
            "folklore. Bleak, propulsive, impossible to stop watching.",
        "faqs": [
            ("How many seasons of Squid Game are there?",
             "The story continues past the first season - the follow-up seasons "
             "extend the games and the rebellion behind them, with the front man "
             "and Gi-hun's revenge carrying the plot."),
            ("Is Squid Game suitable for teenagers?",
             "No - it is 16+ territory: heavy graphic violence and adult themes, "
             "despite the playground packaging that made it famous."),
            ("Is Squid Game based on real games?",
             "The games are real Korean children's games (red light green light, "
             "ddakji, the honeycomb dalgona) - the death-tournament framing is "
             "fiction, which is exactly what makes it sting."),
        ],
    },
    "the-last-of-us": {
        "verdict": "The best video-game adaptation ever made, full stop. The third "
            "episode alone (Bill and Frank) is some of the finest television of "
            "the decade, Pascal and Ramsey recreate the game's found-family "
            "chemistry, and the Clickers are as frightening as the game made "
            "them. It respects the source and stands beside it - a feat nobody "
            "had managed before.",
        "faqs": [
            ("Do I need to play the game before The Last of Us?",
             "No - the series retells the story completely for newcomers, and "
             "players get the deeper pleasure of watching scenes they love "
             "re-staged with new detail. Both orders work."),
            ("Is The Last of Us a zombie show?",
             "Not technically - the infected are cordyceps fungal mutations, which "
             "is why the biology (and the real-science framing device) feels "
             "fresher than standard zombies."),
            ("How many seasons will The Last of Us run?",
             "The plan is a multi-season adaptation - the first season covers the "
             "first game, with the second game's sprawling story mapped across "
             "the seasons that follow."),
        ],
    },
    "stranger-things": {
        "verdict": "The show that made Netflix a noun. Season one is a near-perfect "
            "spell - Speilberg kids, King monsters, an indelible synth score - and "
            "the series has grown bigger, louder and more comic-book with every "
            "season while keeping its true engine: the kids. Uneven in the middle "
            "stretch, unmissable at its peaks, and still the streaming era's "
            "defining adventure.",
        "faqs": [
            ("How many seasons of Stranger Things are there?",
             "The story builds across multiple seasons toward a final chapter - "
             "each season escalates the Upside Down threat while the cast "
             "famously grew up on screen."),
            ("Is Stranger Things too scary for kids?",
             "It is pitched at teenagers and up - monsters, body horror and "
             "genuine peril, wrapped in 1980s nostalgia. Younger kids love the "
             "kids but the Demogorgon disagrees."),
            ("Where is Stranger Things set?",
             "The fictional town of Hawkins, Indiana, in the 1980s - the era is "
             "so precisely built it functions as the show's second villain and "
             "second love letter."),
        ],
    },
    "black-panther": {
        "verdict": "The superhero film as cultural event, and it holds up as both: "
            "Coogler builds Wakanda into a real place with real arguments - "
            "isolation versus duty, Killmonger's grievance versus T'Challa's grace "
            "- and Boseman carries it all with regal quiet. The best MCU villain "
            "until then and since. What a loss he was; what a film he left.",
        "faqs": [
            ("Why is Black Panther so important?",
             "It was the first Black-led superhero blockbuster, one of the "
             "highest-grossing films ever, and the first Marvel film nominated "
             "for Best Picture at the Oscars - winning three, including costume "
             "design and score."),
            ("Who is the villain in Black Panther?",
             "Erik Killmonger, played by Michael B. Jordan - a warped product of "
             "the same system T'Challa inherits, written well enough that his "
             "argument still gets quoted as politics."),
            ("Do I need other Marvel films before Black Panther?",
             "Only Civil War really matters - it introduces T'Challa and sets his "
             "backstory. The film stands alone beyond that."),
        ],
    },
    "joker": {
        "verdict": "A character study doing an impression of a comic-book film: "
            "Phoenix's Arthur Fleck disintegrates through a 1970s-New-York "
            "hellscape with total commitment, and Phillips gives the comic origin "
            "a Taxi Driver transplant. As social commentary it is muddy; as a "
            "performance and a piece of craft it is riveting. The Oscar was "
            "earned; the argument it started was the point.",
        "faqs": [
            ("Is Joker connected to the other Batman films?",
             "It is a standalone origin story in its own universe - no Batman "
             "franchise attachment, deliberately separate from every previous "
             "screen Joker."),
            ("Did Joaquin Phoenix win the Oscar for Joker?",
             "Yes - Best Actor at the 2020 ceremony, for a performance built on "
             "a lost 52 pounds, a researched 'laughing condition', and dance "
             "rehearsals that turned the character into a tragedy in motion."),
            ("Is Joker very violent?",
             "It is violent in sudden, realistic bursts rather than action-movie "
             "volume, and the film's real subject - humiliation and mental "
             "illness untreated - is heavier than its body count."),
        ],
    },
    "spider-man-into-the-spider-verse": {
        "verdict": "The Spider-Man film others will be measured against forever: a "
            "comic book that learned to move - halftone dots, on-panel thought "
            "bubbles, and action rendered at animation's absolute frontier. "
            "Miles Morales is the hero the era needed, and the film treats that "
            "responsibility with joy instead of homework. Rewatchable to the "
            "frame.",
        "faqs": [
            ("Do I need to know Spider-Man to watch Into the Spider-Verse?",
             "No - it introduces Miles Morales from zero and hands him the "
             "mythology as he learns it. Newcomers and lifelong fans get the "
             "same film."),
            ("Is Into the Spider-Verse suitable for young kids?",
             "Yes - it is one of the great all-ages action films, with the "
             "fastest cutting and most inventive animation most children will "
             "ever see. Nothing in it exists to frighten."),
            ("Are there sequels?",
             "Yes - Across the Spider-Verse (2023) continues Miles' story and "
             "ends on a cliffhanger for the third film."),
        ],
    },
    "thor-ragnarok": {
        "verdict": "The reboot-by-comedy that saved Thor from dignity: Waititi "
            "shreds the mythology into a gladiator cartoon with Led Zeppelin, a "
            "Blink-182 joke, and Blanchett's Hela chewing the rainbow bridge. "
            "Purists mourn the Shakespeare; everyone else got the most "
            "re-watchable film in the Thor trilogy and Hulk's best MCU hours.",
        "faqs": [
            ("Is Thor: Ragnarok a comedy or a superhero film?",
             "Both, with the comedy in the driver's seat - Waititi rebuilt the "
             "franchise around improvisation and colour. The stakes survive; "
             "the self-seriousness does not."),
            ("Do I need Thor 1 and 2 before Ragnarok?",
             "It helps for exactly three things: Loki, Asgard, and how much "
             "tone has changed. The film re-introduces everything else - many "
             "viewers start here."),
            ("Is the Hulk in Ragnarok?",
             "Yes - a large chunk of the film is Planet-Hulk-style gladiator "
             "material, with Banner and the big guy negotiating screen time in "
             "the funniest subplot of the MCU's phase."),
        ],
    },
    "soul": {
        "verdict": "Pixar's most adult film wearing a kid's animation: a jazz "
            "pianist's near-death rewires into a meditation on purpose, "
            "ordinary joy and the crime of treating life as a waiting room. "
            "The jazz is genuinely played, the Great Before is design at its "
            "most inventive, and the ending chooses gentleness over twist. "
            "Bring tissues; leave with plans.",
        "faqs": [
            ("Is Soul too philosophical for kids?",
             "Younger viewers ride the visuals and the cat; adults get the "
             "existential question. It is Pixar's gentlest-looking big idea "
             "film - and one of its most quietly devastating endings."),
            ("Is the jazz in Soul real?",
             "Yes - the piano performances belong to Jon Batiste, who recorded "
             "Joe's playing, with the animation keyed to actual sessions. Trent "
             "Reznor and Atticus Ross scored the rest."),
            ("Where is Soul set?",
             "New York City, mostly - it is the studio's most location-specific "
             "love letter since Ratatouille's Paris, right down to the subway "
             "and the barbershop."),
        ],
    },
    "the-lion-king": {
        "verdict": "The 2019 'live-action' remake is a photoreal nature "
            "documentary that keeps pausing for a 1994 masterpiece. The craft "
            "is genuinely staggering and the songs still detonate - but where "
            "the animated originals had faces, these lions have fur physics. "
            "As a technical milestone, essential; as storytelling, a very "
            "well-sung memory of a better film.",
        "faqs": [
            ("Is The Lion King (2019) animated or live-action?",
             "Neither, exactly - it is photoreal computer animation so exact "
             "that no real animal appears on screen; director Jon Favreau has "
             "called it 'live-action in a virtual world'."),
            ("How does the 2019 Lion King compare to the 1994 original?",
             "The story and songs are the same, scene for scene. The original's "
             "expressive animation is widely judged the stronger telling; the "
             "remake's argument is immersion - it looks like a nature "
             "documentary that learned to grieve."),
            ("Is the 2019 Lion King suitable for little kids?",
             "The wildebeest stampede and Scar's villainy hit as hard as 1994's "
             "did - it is as 'dark' as the original, just rendered in "
             "documentary realism that can unsettle very young children more."),
        ],
    },
    "avatar": {
        "verdict": "The film that dragged cinema into modern 3D, and still the "
            "highest-grossing film ever made. Cameron builds Pandora with such "
            "total ecological conviction that the hour of flying and bioluminescent "
            "wonder justifies the familiar plot on its own. Fifteen years of "
            "imitators have matched its box office and not its immersion. The "
            "big screen exists for films like this.",
        "faqs": [
            ("Why was Avatar so expensive, and did it pay off?",
             "Its production and marketing ran somewhere north of 400 million "
             "dollars - much of it spent inventing the performance-capture and "
             "3D pipeline. It repaid that with roughly 2.9 billion dollars "
             "worldwide, the record it has held across two release runs."),
            ("Do I need to watch Avatar before The Way of Water?",
             "Yes - the sequel continues Jake and Neytiri's family story "
             "directly, and its emotional stakes are built on the first film's "
             "ending."),
            ("Is Avatar based on a book?",
             "No - Cameron wrote the original screenplay and famously sat on it "
             "for over a decade waiting for the technology to catch up to his "
             "vision of Pandora. The idea predates most of its visual toolbox."),
        ],
    },
    "gravity": {
        "verdict": "Ninety lean minutes of pure orbital terror. Cuaron opens "
            "with a thirteen-minute unbroken shot and never lets you breathe: "
            "debris, silence, and Bullock fighting physics and panic in equal "
            "measure. The science bends where drama needs it to, but the feeling "
            "of weightless dread is unmatched. Watch it loud, in the dark, and "
            "hold on.",
        "faqs": [
            ("Did Gravity win the Best Picture Oscar?",
             "No - it won seven Academy Awards, including Best Director for "
             "Alfonso Cuaron, but lost Best Picture to 12 Years a Slave at the "
             "2014 ceremony."),
            ("How realistic is the science in Gravity?",
             "The visuals are meticulous, but the film compresses geography for "
             "story - the Hubble, the ISS and China's station are not reachable "
             "by short spacewalks, and orbital debris does not behave like a "
             "chain-reaction traffic jam. The emotion is accurate; the map is "
             "not."),
            ("Is Gravity scary?",
             "It is terror rather than horror - relentless survival pressure "
             "with one of the great sustained opening sequences in cinema. "
             "Claustrophobes should buckle in and breathe on schedule."),
        ],
    },
    "edge-of-tomorrow": {
        "verdict": "The cleverest action film of its decade: a cowardly "
            "publicist forced to live the same losing battle on loop, dying "
            "badly hundreds of times until repetition becomes skill. Cruise "
            "plays against type brilliantly, Blunt's Full Metal Valkyrie is the "
            "badass the genre owes women, and the editing turns repetition into "
            "comedy and dread at once. Live, die, repeat - then repeat the "
            "film.",
        "faqs": [
            ("Is Edge of Tomorrow based on a book?",
             "Yes - Hiroshi Sakurazaka's Japanese light novel All You Need Is "
             "Kill (2004); the film keeps the loop mechanics and resets the "
             "story into a European beach invasion."),
            ("Does Edge of Tomorrow have a different title?",
             "It was marketed in some territories as Live Die Repeat, which is "
             "also the tagline on the poster - home media even re-titled it "
             "Live Die Repeat: Edge of Tomorrow. Same film either way."),
            ("Is the ending a time paradox?",
             "The final act plays a deliberate sleight of hand with the loop's "
             "rules - watch the logistics of the Louvre finale closely and the "
             "film's internal logic does hold together on rewatch."),
        ],
    },
    "oblivion": {
        "verdict": "Kosinski's moodiest blueprint: a drone repairman on an "
            "evacuated Earth starts asking the questions his orders forbid. The "
            "sky-tower aesthetic, M83's score and the rotting landmarks are "
            "genuinely gorgeous; the plot is a bundle of familiar twists "
            "executed with total sincerity. A film for people who miss when "
            "science fiction looked like architecture.",
        "faqs": [
            ("Is Oblivion based on a book?",
             "It grew from director Joseph Kosinski's own unproduced graphic "
             "novel concept, developed into a screenplay - a rare case of a "
             "director adapting his own comic before his first feature even "
             "shipped."),
            ("Where was Oblivion filmed?",
             "Mostly Iceland - the black landscapes double as the scarred, "
             "evacuated Earth, which is why the film's emptiness feels real "
             "rather than digital."),
            ("Is Oblivion connected to the video game of the same name?",
             "No relation to the Oblivion role-playing game or any other "
             "property - the name overlap is a coincidence that still confuses "
             "streaming searches."),
        ],
    },
    "ready-player-one": {
        "verdict": "Spielberg riffing on pop-culture hoarding: a treasure hunt "
            "through a virtual universe stuffed with everything from the "
            "DeLorean to King Kong. As spectacle it is a pixel-perfect "
            "amusement park; as satire of fandom and corporate VR it is lighter "
            "than the book. Turn your brain to arcade settings and the craft "
            "carries you - the opening race sequence is pure joy.",
        "faqs": [
            ("Is Ready Player One based on a book?",
             "Yes - Ernest Cline's 2011 novel stuffed with 1980s references. "
             "Spielberg swapped many of the book's pop-culture markers for "
             "sequences he could actually clear rights on."),
            ("Do I need to know the 1980s references to enjoy it?",
             "No - the references are decoration on a straightforward adventure "
             "race. Half the fun is spotting them; none of the plot depends on "
             "it."),
            ("Is Ready Player One suitable for kids?",
             "Generally yes for tweens and up - PG-13 for action violence and "
             "some language, with the virtual setting keeping the mayhem "
             "consequence-light."),
        ],
    },
    "warcraft": {
        "verdict": "The video-game movie that actually built the world: Duncan "
            "Jones plays the orc-human war with genuine tragic structure, "
            "motion-captured orcs more expressive than most human co-stars, and "
            "a fandom's lore treated with respect. As a critic's film it is "
            "clunky; as a translation of Azeroth it has never been matched - "
            "which is why it earned half a billion despite the reviews.",
        "faqs": [
            ("Do I need to play World of Warcraft to follow Warcraft?",
             "It helps, but the film reconstructs the first orc-human war from "
             "scratch and explains its factions as it goes. Players get the "
             "deep-cut joy; newcomers get a complete fantasy war film."),
            ("Was Warcraft a flop?",
             "Critics were harsh, but it grossed over 430 million dollars "
             "worldwide - most of it in China, where it set records and became "
             "the most successful video-game adaptation at the box office at "
             "the time."),
            ("Will there be a Warcraft sequel?",
             "The planned sequels never materialised, though Duncan Jones has "
             "spoken openly about where he wanted to take them - the first "
             "film ends clearly pitched for more."),
        ],
    },
    "the-revenant": {
        "verdict": "Survival as ordeal: Inarritu and cinematographer Deakins "
            "shot only in natural light across frozen wilderness, and the "
            "result feels less watched than endured. DiCaprio's bear-mauled "
            "frontiersman crawls through two and a half hours of revenge-"
            "driven silence to the Oscar he had been denied for twenty years. "
            "Brutal, beautiful, and absolutely not a casual watch.",
        "faqs": [
            ("Did The Revenant win DiCaprio his Oscar?",
             "Yes - Best Actor at the 2016 ceremony, after five previous "
             "nominations. The film won three Oscars total, including Best "
             "Director for Inarritu, his second in a row."),
            ("Is The Revenant based on a true story?",
             "Loosely - frontiersman Hugh Glass really was mauled by a bear and "
             "abandoned by companions in 1823, and really did survive hundreds "
             "of miles to reach them. Everything beyond that is legend and "
             "fiction."),
            ("How graphic is the bear attack?",
             "It is one of the most visceral sequences in modern cinema - long, "
             "loud and convincing, with no cut to spare. Most viewers find it "
             "harder to sit through than the film's human violence."),
        ],
    },
    "dunkirk": {
        "verdict": "Nolan's shortest film and his most abstract: three "
            "timelines - one week on the beach, one day on the water, one hour "
            "in the air - braided into a 106-minute war film with almost no "
            "dialogue and no villain on screen. Zimmer's Shepard-tone score and "
            "the ticking watch make pure suspense out of evacuation. War as "
            "structure, not speeches.",
        "faqs": [
            ("Is Dunkirk based on a true event?",
             "Yes - the 1940 Dunkirk evacuation, in which some 338,000 Allied "
             "soldiers were rescued from the beaches by navy ships and hundreds "
             "of civilian 'little ships'. Nolan tells it through fictional "
             "characters inside the real event."),
            ("Why is there so little dialogue in Dunkirk?",
             "By design - Nolan built the film as suspense mechanics rather "
             "than character drama, with the three timelines supplying the "
             "structure conversations usually would. The silence is the "
             "point."),
            ("Is Dunkirk suitable for younger viewers?",
             "It is one of the least bloody war films of its scale - rated "
             "PG-13, with tension rather than gore as its weapon. History-"
             "curious teenagers are exactly the right audience."),
        ],
    },
    "hacksaw-ridge": {
        "verdict": "Gibson's comeback is old-school battle filmmaking with one "
            "genuinely great true story: Desmond Doss, the army medic who "
            "refused to touch a rifle and saved dozens of wounded men under "
            "fire on Okinawa. Garfield plays the conviction without smugness, "
            "the second-half battle is hell rendered honestly, and the "
            "sincerity that makes eyes roll elsewhere lands here. Faith, blood "
            "and nerve.",
        "faqs": [
            ("Is Desmond Doss a real person?",
             "Yes - the first conscientious objector awarded the Medal of "
             "Honor, for saving wounded soldiers at Hacksaw Ridge during the "
             "Battle of Okinawa in 1945. The film's most incredible details are "
             "the documented ones."),
            ("How violent is Hacksaw Ridge?",
             "Very - the battle sequences are among the most graphic of the "
             "decade, unflinching by intent. The first half is a gentle "
             "biopic; the second half is war without varnish. Not for the "
             "squeamish."),
            ("Did Hacksaw Ridge win any Oscars?",
             "It was nominated for six, winning two - Best Film Editing and "
             "Best Sound Mixing - with Garfield nominated for Best Actor."),
        ],
    },
    "pacific-rim": {
        "verdict": "Del Toro builds monsters the size of buildings and then "
            "has the audacity to make you care about the people inside the "
            "robots. Weight is the whole trick - every punch moves tons of "
            "water, every city block breaks like real masonry - and the film "
            "treats its giant-robot premise with the gravity of a war picture. "
            "Idris Elba's 'cancelling the apocalypse' speech still raises "
            "hairs.",
        "faqs": [
            ("Is Pacific Rim connected to Godzilla or King Kong?",
             "No - it is an original universe, separate from Legendary's "
             "Monsterverse. The kaiju genre debt is openly Japanese, but the "
             "story stands alone."),
            ("Do I need to watch the Pacific Rim sequel?",
             "No - Uprising (2018) continues the timeline with a mostly new "
             "cast and is widely considered the weaker film. The first stands "
             "alone beautifully."),
            ("Was Pacific Rim a success?",
             "It underperformed in the US but found its audience internationally "
             "and on home video, grossing over 400 million dollars and earning "
             "a devoted following for its craft."),
        ],
    },
    "alita-battle-angel": {
        "verdict": "Cameron's pet project, handed to Robert Rodriguez to "
            "direct: a cyborg girl rebuilt in a scrapyard junk city, with the "
            "biggest eyes in motion-capture history and a motorball chase that "
            "justifies the whole film. The world-building is dense and "
            "sincere, the story is half a saga, and none of it quite adds up - "
            "and it is still the most alive manga adaptation Hollywood has "
            "made.",
        "faqs": [
            ("Is Alita based on an anime?",
             "Yes - Yukito Kishiro's manga Battle Angel Alita (1990), which "
             "also inspired a 1993 OVA. Cameron spent two decades trying to "
             "make it before technology and schedules let him produce it under "
             "Rodriguez."),
            ("Does Alita have an ending?",
             "It ends mid-saga, resolving this chapter but pointing straight up "
             "at the sky city for a sequel that fans have been campaigning for "
             "ever since."),
            ("Why are Alita's eyes so big?",
             "A deliberate nod to the manga's art style - the performance-"
             "capture scales Rosa Salazar's features to anime proportions. Ten "
             "minutes in, your brain accepts it; that is the 200-million-dollar "
             "trick."),
        ],
    },
    "ghost-in-the-shell": {
        "verdict": "Hollywood's 2017 remake of the most important cyberpunk "
            "anime ever made: a gorgeous, faithful-in-images, hollow-in-spirit "
            "copy. The production design steals from the 1995 original with "
            "reverence, Johansson commits fully, and the casting controversy "
            "became the film's real legacy. Watch it as an appetiser - then "
            "watch the anime it feeds on.",
        "faqs": [
            ("Do I need to watch the 1995 anime first?",
             "Not required - but the 1995 Ghost in the Shell is the masterwork "
             "this remixes, and the comparison is instructive: every image the "
             "remake borrows carried more argument in the original."),
            ("What was the casting controversy about?",
             "A white American actress was cast as Major Motoko Kusanagi, a "
             "Japanese character - and the film then wrote a plot explanation "
             "for it, which most critics found worse than the casting "
             "itself."),
            ("Is Ghost in the Shell (2017) suitable for teens?",
             "PG-13, and thematically heavy rather than gory - older teenagers "
             "interested in AI and identity questions are exactly its audience, "
             "ideally followed by the anime."),
        ],
    },
    "deadpool": {
        "verdict": "The R-rated counter-attack on sanitised superhero cinema: "
            "Reynolds' mercenary with a mouth spends two hours insulting the "
            "genre that fired him, breaking the fourth wall, and - the film's "
            "secret - telling a genuinely sweet love story. Funnier, sharper "
            "and more romantic than it has any right to be. The proof that "
            "rating and craft are unrelated.",
        "faqs": [
            ("Is Deadpool suitable for teenagers?",
             "No - hard R for graphic violence, language and sexual content. It "
             "is a superhero film built specifically for adults, which was the "
             "entire point of its existence."),
            ("Do I need to watch X-Men films before Deadpool?",
             "No - the film mocks the idea of continuity as much as anything "
             "else. Knowing Reynolds' first Deadpool turn in X-Men Origins "
             "earns you one extra joke, nothing more."),
            ("Is Deadpool a Marvel or Fox film?",
             "It was made by Fox (the character's film rights predated the "
             "MCU) and joined Marvel Studios' canon after Disney's acquisition "
             "- which is exactly the joke the third film is built on."),
        ],
    },
    "deadpool-2": {
        "verdict": "The sequel doubles everything - gags, gore, heart - and "
            "mostly gets away with it. Brolin's Cable is the straight man the "
            "jokes need, Domino's luck powers are the best new superhero power "
            "in years, and the X-Force parachute sequence is the hardest any "
            "superhero film has ever laughed at itself. The found-family theme "
            "is real, which is why the punchlines hit harder.",
        "faqs": [
            ("Is Deadpool 2 better than the first?",
             "Opinions split cleanly: the first is the purer origin, the second "
             "is bigger, funnier in more scenes and more emotionally open. "
             "Watch the first first - the sequel assumes you love these "
             "idiots."),
            ("Who is the kid in Deadpool 2?",
             "Russell, a young mutant in a brutal reform facility whose future "
             "turns him into a killer Cable is hunting - the film's actual "
             "emotional plot, and the reason the jokes land harder."),
            ("Are there different cuts of Deadpool 2?",
             "Yes - the theatrical cut, a Super Duper extended cut, and a "
             "deliberately family-friendly PG-13 re-edit (Once Upon a Deadpool) "
             "framed as a holiday special."),
        ],
    },
    "aquaman": {
        "verdict": "Wan plays Atlantis as an underwater theme park with total "
            "commitment: seven kingdoms, tunnel-shark leviathans, Momoa surfing "
            "a tidal wave of crabs into battle. It is the highest-grossing film "
            "of DC's extended-universe era because it never apologises for "
            "being ridiculous. Come for the octopus playing the drums, stay "
            "for the genuinely epic final act.",
        "faqs": [
            ("Do I need other DC films before Aquaman?",
             "No - everything from the team-up film is recapped in a scene, "
             "and the story stands entirely alone. It is the most newcomer-"
             "friendly film of the DCEU."),
            ("Is Aquaman the highest-grossing DC film?",
             "It grossed about 1.15 billion dollars, making it the highest-"
             "grossing film of the DCEU era and one of the few DC films to "
             "cross a billion."),
            ("Did Julie Andrews really voice the sea monster?",
             "Yes - the Karathen, the colossal creature guarding the Trident, "
             "is voiced by Julie Andrews, a piece of casting so delightful it "
             "refuses to stay buried in the credits."),
        ],
    },
    "shang-chi-and-the-legend-of-the-ten-rings": {
        "verdict": "The MCU's best pure martial-arts film: a bus fight staged "
            "in one legible, escalating take, Tony Leung playing grief as a "
            "villain, and a family drama about fathers and shadows that earns "
            "its dragon. Liu Simu arrived as a movie star fully formed. When "
            "the MCU keeps its feet on the ground, it is this good.",
        "faqs": [
            ("Is Shang-Chi based on existing comics?",
             "Yes - Marvel's Shang-Chi, Master of Kung Fu, created in 1973 "
             "during the kung-fu cinema boom; the film rewrites the character's "
             "problematic comics origin into something centred on Chinese "
             "family and legend."),
            ("Do I need other Marvel films first?",
             "No - it is designed as a clean entry point, with a couple of "
             "cameos (and one very good Wong scene) as seasoning rather than "
             "homework."),
            ("Is the bus fight really one shot?",
             "It is edited to play as extended takes, with the camera moving "
             "through the chaos - stunt choreography from Brad Allan's team, "
             "and widely praised as the MCU's best hand-to-hand sequence."),
        ],
    },
    "eternals": {
        "verdict": "The MCU's most divisive film is also its most interesting "
            "experiment: an Oscar-winning director shoots seven immortals "
            "across seven thousand years with natural light, ancient-epic "
            "pacing and a plot about whether humanity deserves to exist. It "
            "swings at genuine themes, misses as often as it connects, and "
            "never once feels stamped from the mould. Judge it for trying.",
        "faqs": [
            ("Why is Eternals so different from other Marvel films?",
             "Chloe Zhao's approach - naturalistic performances, real "
             "landscapes, long takes - met a cosmic mythology that spans "
             "millennia. The studio let her keep the textures, and the result "
             "is the franchise's slowest, strangest, most philosophical "
             "entry."),
            ("Do I need to watch Eternals before other Marvel films?",
             "No - its events matter mainly to its own corner of the universe, "
             "which makes it one of the safest jumping-in points in the modern "
             "MCU."),
            ("Is Eternals boring?",
             "If you need constant momentum, honestly, probably - it runs 157 "
             "minutes of mythology and doubt. If you want the MCU attempting "
             "cosmic scale and a love story across centuries, it is the only "
             "one of its kind."),
        ],
    },
    "captain-marvel": {
        "verdict": "A 1990s blockbuster dressed as a 2019 one: video stores, "
            "dial-up internet, and Larson's Kree warrior slowly remembering "
            "the Earth life she was told to forget. The amnesia mystery keeps "
            "the first half honest, the Skrull twist reframes the war, and the "
            "film's whole thesis - get up, again - lands clean. Not the MCU's "
            "boldest; one of its most confident.",
        "faqs": [
            ("Why is Captain Marvel set in the 1990s?",
             "To place it before the earlier MCU films, making it a prequel "
             "that explains the pager from the Infinity War post-credits - and "
             "to dress an entire blockbuster in video-store-era nostalgia "
             "while it is at it."),
            ("Do I need Captain Marvel before Endgame?",
             "It helps - her arrival is a plot point in Endgame, and her "
             "powers recalibrate the films' power scales. Watch it before "
             "Avengers: Endgame if you are marathoning."),
            ("Is Captain Marvel the strongest Avenger?",
             "In-universe, she is repeatedly positioned in the top tier - able "
             "to move spaceships. Power-scaling debates aside, the films treat "
             "her as the emergency button, not the regular line-up."),
        ],
    },
    "wonder-woman": {
        "verdict": "The DCEU's one unqualified success story: Gadot's Amazon "
            "walks into the mud of the First World War and the film finds the "
            "exact register of sincerity the franchise had been missing. The "
            "No Man's Land crossing remains one of the great superhero scenes "
            "- a character becoming herself in real time. The third act "
            "collapses into smoke and noise; everything before it soars.",
        "faqs": [
            ("Is Wonder Woman set in World War One or Two?",
             "The First World War - 1918 - a deliberate choice that keeps the "
             "era's cynicism specific (gas, trenches, generals in rooms) rather "
             "than blending into generic WWII iconography."),
            ("Is the No Man's Land scene in the comics?",
             "The scene is original to the film - it instantly became the "
             "character's defining screen moment and one of the most analysed "
             "superhero sequences ever shot."),
            ("Do I need Justice League before Wonder Woman?",
             "No - watch this first, chronologically and in quality. The film "
             "stands entirely alone and is the recommended entry to Gadot's "
             "Diana."),
        ],
    },
    "wonder-woman-1984": {
        "verdict": "The follow-up swung for an era-specific fable about greed "
            "and wish-thinking - and the film is at its best exactly there, in "
            "Pedro Pascal's unraveling TV salesman and a cold-open Olympics "
            "sequence for the ages. The plot machinery around it creaks, and "
            "the ending argues with itself. A noble misfire with two "
            "unforgettable scenes.",
        "faqs": [
            ("Why is Wonder Woman 1984 set in 1984?",
             "To drop Diana into the decade of excess - Wall Street greed, "
             "television shopping channels, nuclear brinkmanship - the exact "
             "soil for a story about wishes and their costs."),
            ("Should I watch Wonder Woman 1984 or skip it?",
             "Watch it after the first film if you are completing the arc; "
             "Pascal's villain and the opening sequence justify the time even "
             "though the film around them wobbles."),
            ("Why did WW84 release on streaming?",
             "December 2020, mid-pandemic - it launched day-and-date on HBO "
             "Max, the first blockbuster to do so, and its reception was "
             "forever tangled in that experiment."),
        ],
    },
    "black-adam": {
        "verdict": "The Rock's decade-long passion project arrives as a DC "
            "origin with an antihero smirk: a five-thousand-year slave-turned-"
            "god wakes up, declines the hero speech, and levels things. The "
            "Justice Society members are the fun part, the hierarchy-changing "
            "promise was mostly marketing, and the film now reads as the "
            "DCEU's last grand swing before the reset. Big, loud, oddly "
            "likable.",
        "faqs": [
            ("Is Black Adam a villain or a hero?",
             "The film's whole argument is that he is neither - an antihero "
             "whose idea of justice predates modern morality. In the comics he "
             "is Shazam's dark mirror; here he is a nation's wrath given a "
             "body."),
            ("Is Superman really in Black Adam?",
             "Yes - Henry Cavill's Superman appears in the mid-credits scene, "
             "a cameo that made headlines and led nowhere: the studio reset "
             "followed within weeks."),
            ("Do I need other DC films before Black Adam?",
             "No - it introduces its own corner (Kahndaq) and its own team, "
             "the Justice Society, from scratch. Zero homework required."),
        ],
    },
    "venom": {
        "verdict": "A studio contract walked into a bar and ordered a buddy "
            "comedy: Hardy plays a disgraced journalist and the symbiote "
            "voices the id, and the two of them squabble their way through a "
            "limp corporate plot with total commitment to the bit. The critics "
            "were right and the 800-million-dollar box office was also right - "
            "junk food executed with real charm, and Hardy's dual performance "
            "is the whole meal.",
        "faqs": [
            ("Is Venom connected to Spider-Man?",
             "In the comics, inseparably - the suit is born from Spider-Man's "
             "storyline. The 2018 film builds its own universe without "
             "Spider-Man, saving the connection for post-credits teases."),
            ("Do I need the post-credits scenes for Venom?",
             "The first film's credits scenes set up the sequel; the sequel's "
             "credits scene winks at another universe entirely. They are "
             "seasoning, not homework."),
            ("Is Venom scary or funny?",
             "Both by design - body-horror imagery played for comedy, with "
             "Hardy's wet-voiced double act as the engine. Teenagers are its "
             "core audience; horror fans should calibrate accordingly."),
        ],
    },
    "venom-let-there-be-carnage": {
        "verdict": "Ninety-seven minutes of Hardy arguing with himself while "
            "Harrelson's Carnage turns a prison transfer into a red-"
            "splattered rock concert. The first film's charm, concentrated: "
            "less plot, more symbiote relationship drama, played as the "
            "world's strangest breakup movie. It knows exactly what it is - a "
            "midnight movie with a blockbuster budget - and never pretends "
            "otherwise.",
        "faqs": [
            ("Do I need to watch Venom (2018) first?",
             "Yes - the sequel is the second act of Eddie and Venom's "
             "relationship, and its whole emotional vocabulary assumes you "
             "watched them move in together."),
            ("Who is Carnage?",
             "Cletus Kasady, a serial killer whose cellmate moment with the "
             "red symbiote creates Venom's psychotic offspring - Harrelson "
             "playing it as heavy-metal crazy, which is either the film's "
             "problem or its energy source."),
            ("What is the Venom 2 post-credits scene?",
             "Without spoiling the mechanics: Eddie and Venom glimpse another "
             "universe's world - the clearest on-screen bridge between the "
             "Sony Marvel films and the MCU to date."),
        ],
    },
    "the-matrix-resurrections": {
        "verdict": "Lana Wachowski's sequel is a trapdoor: a film about being "
            "forced to make a sequel, in which the Matrix itself has become a "
            "franchise factory and Neo is literally re-enslaved by his own "
            "story. The first hour is the sharpest metafiction Hollywood has "
            "dared; the second retreats into homage. Flawed, fascinating, and "
            "the only recent blockbuster arguing with its own studio on "
            "screen.",
        "faqs": [
            ("Do I need to rewatch the original Matrix trilogy?",
             "At minimum the first film - Resurrections recaps constantly, but "
             "its entire argument (and its jokes) only land if you remember "
             "what the original meant to you."),
            ("Why did only Lana Wachowski direct Resurrections?",
             "Lilly Wachowski chose not to return, and Lana's script reframes "
             "the whole film around grief and creation, which most critics "
             "read as the honest answer on screen."),
            ("Is The Matrix Resurrections a reboot or a sequel?",
             "Both, deliberately - it is a direct sequel that begins by "
             "parodying the idea of its own reboot, with studio executives "
             "appearing as characters in the film's opening argument."),
        ],
    },
    "inside-out": {
        "verdict": "Pixar's thesis statement: the emotions inside an eleven-"
            "year-old's head argue through a family move, and the film quietly "
            "hands every viewer the healthiest model of sadness ever put on "
            "screen. Bing Bong is the hardest cry in the studio's catalogue. "
            "Concept, craft and compassion in perfect formation - the best "
            "original film Pixar has made this century.",
        "faqs": [
            ("Is Inside Out scientifically accurate?",
             "Consulting psychologists shaped the five-emotion core, so the "
             "architecture is real psychology dressed as whimsy - right down "
             "to sadness being the mechanism that asks for help."),
            ("Do I need Inside Out 2 before the first?",
             "No - the 2015 original is complete on its own; the 2024 sequel "
             "(puberty, new emotions) builds on it. Watch this first, "
             "always."),
            ("Why does everyone cry at Inside Out?",
             "Because Bing Bong's sacrifice and the film's central idea - "
             "sadness is not a malfunction, it is connection - arrive "
             "together. Pixar built a machine for empathy and ran it at full "
             "power."),
        ],
    },
    "finding-dory": {
        "verdict": "The rare legacy sequel built as a character study: Dory's "
            "short-term memory loss reframed as origin, adoption and the "
            "invention of a family that fits. The octopus Hank steals the "
            "film, the loopy whales steal two scenes, and the marine-institute "
            "set pieces are Pixar doing pure comedy. Lighter than Nemo by "
            "design - and just as kind.",
        "faqs": [
            ("Do I need to watch Finding Nemo before Finding Dory?",
             "Yes, ideally - Dory is Nemo's comic relief, and the sequel hands "
             "her the lead by finally explaining the wound behind the joke. "
             "The payoff lands because you know her."),
            ("Is Finding Dory suitable for very young kids?",
             "It is one of Pixar's gentlest - sea creatures, bright tanks and "
             "a short runtime suit young children, with themes (memory, "
             "belonging) that fly harmlessly over the smallest heads."),
            ("Was Finding Dory a bigger hit than Finding Nemo?",
             "It crossed a billion dollars worldwide, making it one of the "
             "highest-grossing animated films ever at the time - the "
             "thirteen-year wait paid off."),
        ],
    },
    "moana": {
        "verdict": "The best of Disney's modern musicals: a Polynesian "
            "wayfinder, a demigod played by The Rock at maximum charm, a "
            "companion chicken for comic relief, and songs - How Far I'll Go "
            "especially - that earn their anthemic status. The ocean is a "
            "character, the grandmother is the secret hero, and the volcano "
            "finale chooses argument over swordfight. Total conviction, start "
            "to finish.",
        "faqs": [
            ("Is Moana based on a real legend?",
             "It is original fiction built from real Polynesian voyaging "
             "tradition - filmmakers consulted navigators and elders across "
             "the Pacific, and Maui is drawn from mythology rather than any "
             "single tale."),
            ("Is Moana called Vaiana in some countries?",
             "Yes - a trademark clash over the name forced the title Vaiana "
             "or Oceania in much of Europe; the film itself is identical."),
            ("Which is better, Moana or Encanto?",
             "Both are modern Disney peaks with different engines - Moana has "
             "the stronger adventure spine and anthem, Encanto the richer "
             "family ensemble. Households have voted for both, endlessly."),
        ],
    },
    "raya-and-the-last-dragon": {
        "verdict": "Kumandra's five lands and a sword-wielding heroine hunting "
            "the last dragon to heal a shattered world - Southeast Asian "
            "design traditions rendered gorgeously, with Awkwafina's Sisu "
            "supplying the comedy. The trust-versus-armor theme is genuinely "
            "argued, the action is fluid, and a pandemic-era release buried a "
            "film that deserved a theatrical audience.",
        "faqs": [
            ("What cultures inspire Raya and the Last Dragon?",
             "Southeast Asia broadly - Vietnam, Thailand, Laos, Indonesia, "
             "Malaysia, the Philippines and Cambodia all fed the design, "
             "costume, food and martial arts through the studio's cultural "
             "consultants."),
            ("Why did Raya skip cinemas?",
             "It released in March 2021, deep in the pandemic - day-and-date "
             "on Disney+ with paid early access and a limited theatrical "
             "rollout. Its modest box office reflects timing, not quality."),
            ("Is Raya too scary for little kids?",
             "The Druun - dust-plague monsters that petrify people - are "
             "genuinely unsettling to under-fives; older children ride it "
             "fine. The trust theme lands best with school age and up."),
        ],
    },
    "mulan": {
        "verdict": "The 2020 remake swaps the animation's songs and dragon for "
            "wuxia sweep: real armies, real locations, genuine battle "
            "choreography, and Liu Yifei carrying the warrior arc with steel. "
            "What it gains in spectacle it loses in warmth - the 1998 film's "
            "comedy and music were the soul, and this version knows it. "
            "Honourable, handsome, slightly hollow.",
        "faqs": [
            ("Does the live-action Mulan have songs?",
             "Not as performances - the 1998 numbers survive as instrumental "
             "reprises and one end-credits cover, a choice that divided "
             "audiences as much as any casting."),
            ("How different is the 2020 Mulan from the animation?",
             "The skeleton is the same - daughter takes father's place, truth "
             "revealed in war - but the witch is new, the dragon and the love "
             "interest are gone, and the tone is straight epic rather than "
             "musical adventure."),
            ("Why did Mulan (2020) struggle?",
             "A 200-million-dollar budget released mid-pandemic as a premium "
             "streaming rental, plus a boycott movement over filming "
             "locations - the film's reception was never purely about the "
             "film."),
        ],
    },
    "toy-story-4": {
        "verdict": "Nobody asked for a fourth film, and then it broke your "
            "heart anyway. Forky - a spork in existential crisis - is a comic "
            "genius creation, the antique-shop second act is genuinely eerie, "
            "and Bo Peep's return turns the whole franchise into a "
            "conversation about purpose after purpose. It ends the saga with "
            "grace where Toy Story 3 ended it with tears. Oscar well earned.",
        "faqs": [
            ("Is Toy Story 4 a sequel or an epilogue?",
             "Both - it follows Woody after Andy's chapters close, and its "
             "ending redefines the toys' world so completely that many fans "
             "consider it the truer finale than the beloved third film."),
            ("Do I need to rewatch Toy Story 3 first?",
             "Not strictly - the handover is restated elegantly - but the "
             "emotional continuity is the whole engine, and the third film's "
             "ending is the launchpad for this one's questions."),
            ("Is Toy Story 4 the last one?",
             "It closes Woody's arc completely; a fifth film exists in "
             "development at Pixar, but this one was made as an ending - and "
             "plays as one."),
        ],
    },
    "zootopia": {
        "verdict": "The cop-buddy comedy that smuggles a course in prejudice "
            "into a bunny-cop mystery: Judy Hopps and con-artist Nick Wilde "
            "chase a missing-mammals case through a city built as a bias "
            "machine. The DMV sloth gag is eternal, and the message never "
            "lectures past the story. Disney's smartest modern original.",
        "faqs": [
            ("Is Zootopia about racism?",
             "It is an allegory about bias and stereotyping built with "
             "predator/prey dynamics - deliberately broader than any single "
             "real-world analogy, which is why it works in classrooms on "
             "every continent."),
            ("Is there a Zootopia sequel?",
             "Yes - Zootopia 2 is in the works at Disney, reuniting the "
             "leads; the 2016 original also spawned a Disney+ series of "
             "shorts."),
            ("Did Zootopia win the Oscar?",
             "Yes - Best Animated Feature at the 2017 ceremony, on the "
             "strength of writing that works as mystery, comedy and social "
             "essay at once."),
        ],
    },
    "minions": {
        "verdict": "The sidekicks got a prequel and proved they can carry a "
            "film - barely, gloriously, at 90 minutes exactly. 1968 New York, "
            "a villain convention, and Sandra Bullock's Scarlet Overkill "
            "giving the performance of her career; the Minions themselves "
            "operate on pure slapstick logic in a language everyone pretends "
            "to understand. Foolishness, perfectly engineered.",
        "faqs": [
            ("What language do the Minions speak?",
             "Minionese - a constructed gibberish blending English, Spanish, "
             "French, Italian and food words, voiced largely by co-director "
             "Pierre Coffin. Every audience believes they understood more "
             "than they did; that is the trick."),
            ("Do I need the Despicable Me films before Minions?",
             "No - it is a prequel set decades before, explaining how the "
             "Minions found their villain. The viewing order between this "
             "and Despicable Me barely matters."),
            ("Is Minions suitable for very young children?",
             "It is engineered for them - slapstick, bright colours, short "
             "runtime, no real peril that sticks. Parents may emerge needing "
             "coffee and a thesaurus for 'banana'."),
        ],
    },
    "despicable-me-3": {
        "verdict": "The franchise's most divided entry: Gru meets a twin "
            "brother with hair and a turtleneck, a villain reviews his own "
            "80s nostalgia in shoulder pads, and the Minions take a detour "
            "to prison variety night. The long-lost-siblings plot is cotton "
            "candy, Trey Parker's Bratt is a gift, and the whole thing runs "
            "on the series' unbeatable engine - evil reformed by "
            "parenting.",
        "faqs": [
            ("Do I need to watch Despicable Me 1 and 2 first?",
             "It helps - the family (the girls, Lucy, the Minions) carries "
             "over, and this one's whole premise leans on Gru having become "
             "a contented dad. Watch the second at minimum."),
            ("Who voices the villain in Despicable Me 3?",
             "Trey Parker, co-creator of South Park, as Balthazar Bratt, a "
             "former child star turned 80s-obsessed supervillain - the "
             "casting explains every single joke in his scenes."),
            ("Why are the Minions barely in Despicable Me 3?",
             "They are - but the film splits them off early (the prison "
             "sequence) so Gru's twin-brother plot can breathe, a structure "
             "choice that split audiences down the middle."),
        ],
    },
    "kung-fu-panda-3": {
        "verdict": "The trilogy's gentlest chapter: Po meets his birth "
            "father, a secret panda village learns to be terrible at kung fu "
            "on purpose, and J.K. Simmons' Kai steals chi with jade blades. "
            "The film's big idea - you win by being more yourself, not less - "
            "is the series' thesis distilled. Gorgeous, funny, and quietly a "
            "landmark US-China co-production.",
        "faqs": [
            ("Do I need Kung Fu Panda 1 and 2 first?",
             "Yes - the third pays off both (Po's origin, the inner-peace "
             "lesson, the Furious Five) and assumes you love this world. The "
             "trilogy is designed as one story."),
            ("Where does Kung Fu Panda 3 take place?",
             "The secret panda village high in the mountains - a snow-dusted, "
             "scroll-softened world built for the film - plus the spirit "
             "realm where Kai fights, rendered in jade-and-ink style."),
            ("Is Kung Fu Panda 3 the last one?",
             "It closed the original trilogy's arc, but Po returned in a "
             "2024 fourth film - the third remains the fan-favourite ending "
             "of the original story."),
        ],
    },
    "the-lord-of-the-rings-the-fellowship-of-the-ring": {
        "verdict": "The foundation of modern fantasy cinema: Jackson took a "
            "book declared unfilmable and built New Zealand into Middle-earth "
            "with models, mud and total faith. The Shire's warmth, Moria's "
            "dread, Boromir's death - the trilogy's emotional peak is right "
            "here in film one. A complete story, a perfect promise, and the "
            "standard every fantasy film still measures itself against.",
        "faqs": [
            ("Do I need to watch Lord of the Rings in order?",
             "Yes - the trilogy is one story in three parts, and Fellowship "
             "establishes everything: the Ring, the Fellowship, the stakes. "
             "For the original trilogy, release order and story order are "
             "the same."),
            ("How many Oscars did Fellowship of the Ring win?",
             "Four from thirteen nominations - including cinematography and "
             "Howard Shore's score - with the trilogy's big haul (eleven "
             "wins) reserved for The Return of the King."),
            ("Theatrical or Extended cut for first-time viewers?",
             "The theatrical cut first - it is the film as released, 178 "
             "minutes; the Extended Editions are magnificent for the devoted "
             "but add roughly two hours across the trilogy."),
        ],
    },
    "the-hobbit-an-unexpected-journey": {
        "verdict": "The overture to a trilogy that should have been one "
            "film: Jackson returns to Middle-earth with love and unlimited "
            "runtime, and the results are exactly that - Gollum's riddle "
            "duel is among the best scenes in all six films, while "
            "everything around it breathes slower than the story needs. "
            "Comfort-viewing Middle-earth, first-course pacing. Watch it for "
            "the dwarf song and Bilbo's choice.",
        "faqs": [
            ("Should I watch The Hobbit before Lord of the Rings?",
             "Never on a first visit - The Lord of the Rings first, always. "
             "The Hobbit films assume you know and love Middle-earth, and "
             "their pleasures only fully read that way."),
            ("Why is one short book three long films?",
             "Studio economics and expanded lore - the planned two films "
             "became three, padded with appendix material and new "
             "characters, a decision debated by fans longer than the "
             "trilogy runs."),
            ("What is the high frame rate version of The Hobbit?",
             "48 frames per second - double cinema standard, offered in some "
             "screenings. It made motion hyper-smooth and sets look like "
             "sets; audiences split hard, and most home versions default to "
             "the classic 24fps look."),
        ],
    },
    "fantastic-beasts-and-where-to-find-them": {
        "verdict": "The Wizarding World's spin-off gamble at its best: 1926 "
            "New York, Redmayne's hunched magizoologist and his case of "
            "runaway wonders, the Niffler's jewellery heist, and a genuinely "
            "sad mystery underneath. As franchise-launch it over-reaches - "
            "the dark-wizard reveal belongs to a different film - but as a "
            "creature-feature romance it is a warm, winsome detour.",
        "faqs": [
            ("Do I need the Harry Potter films before Fantastic Beasts?",
             "No - it is set seventy years earlier, and the few connections "
             "are easter eggs, not prerequisites. Newcomers start clean."),
            ("Is Fantastic Beasts connected to the Harry Potter books?",
             "Through lore, yes - the film adapts Rowling's 2001 companion "
             "'textbook' about magical creatures into an original screenplay "
             "expanding the era before Harry's story."),
            ("How many Fantastic Beasts films were planned?",
             "Five, once upon a time - the series was later trimmed after "
             "the third film's reception, leaving the saga's future "
             "officially undecided."),
        ],
    },
    "inception": {
        "verdict": "The heist film rebuilt inside the skull, and the "
            "blockbuster that proved original ideas could still carry nine "
            "figures. Nolan layers dream on dream with lucid, legible "
            "physics - the hallway fight and the folding Paris street "
            "remain touchstones - while Zimmer's Édith Piaf detour gives "
            "the whole thing a heartbeat. Demands attention, pays it back "
            "tenfold.",
        "faqs": [
            ("Does the spinning top fall at the end of Inception?",
             "Nolan cuts away on purpose - the film's point is that Cobb "
             "stops waiting for the totem and chooses his children. Nolan "
             "has said the ambiguity is the intended ending; Michael Caine "
             "(whose character only appears in reality) has his own "
             "answer."),
            ("How does dream time work in Inception?",
             "Roughly five times deeper per level under sedation - minutes "
             "above become hours below, which is what lets the van, the "
             "hotel and the snow fortress run as three simultaneous "
             "timeframes in the climax."),
            ("Is Inception based on a book?",
             "No - Nolan wrote the original screenplay over about a decade, "
             "building it around the idea of stealing and planting ideas "
             "(extraction and inception) inside shared dream space."),
        ],
    },
    "la-la-land": {
        "verdict": "A sun-drunk musical about the price of the dream, and "
            "the rare original Hollywood romance that earns its bittersweet "
            "epilogue. Chazelle shoots Los Angeles in CinemaScope candy, "
            "Gosling and Stone sell the fallbacks as romance, and the "
            "final fantasy - the life they did not choose - is one of "
            "modern cinema's great endings. City of stars, indeed.",
        "faqs": [
            ("What happened with the La La Land / Moonlight Best Picture "
             "Oscar?",
             "At the 2017 ceremony the presenters were wrongly given La La "
             "Land's envelope; the producers were mid-speech when the "
             "error was corrected and Moonlight was announced as the real "
             "Best Picture winner - the most famous mix-up in Oscars "
             "history. La La Land still won six awards that night, "
             "including Best Director."),
            ("Did Ryan Gosling really play the piano in La La Land?",
             "Yes - he learned to play the film's jazz pieces by "
             "practising daily for months, and the performance shots are "
             "him, no hand double. Emma Stone also sings live."),
            ("What is the meaning of the La La Land ending?",
             "The epilogue imagines the life Mia and Sebastian would have "
             "had if he had come to Paris - then returns them to the "
             "successful but separate lives they actually chose. The "
             "argument: some loves are right and still not forever."),
        ],
    },
    "knives-out": {
        "verdict": "The whodunit resurrected with total showmanship: "
            "Johnson builds a donut of a mystery - a hole at the centre "
            "you can see straight through - and lets Craig's Benoit "
            "Blanc twang his way through a family of vultures with "
            "gusto. De Armas is the heart the satire needs. Cozy, "
            "vicious, and rewatchable every single holiday.",
        "faqs": [
            ("Is Knives Out connected to Murder on the Orient Express?",
             "No - it is an original whodunit in the Agatha Christie "
             "tradition, with Daniel Craig's detective Benoit Blanc as an "
             "original Poirot-flavoured creation, not an adaptation of any "
             "existing novel."),
            ("What is the donut metaphor in Knives Out?",
             "Blanc describes the case as a donut hole within a donut "
             "hole - layers of truth with gaps at the centre - and the "
             "film literally hands him a doughnut to hold while he says "
             "it."),
            ("Are there Knives Out sequels?",
             "Yes - Glass Onion (2022) and a third case, Wake Up Dead Man "
             "(2025), with Craig's Blanc solving a new mystery each time "
             "around a new ensemble."),
        ],
    },
    "gone-girl": {
        "verdict": "Fincher at his iciest, and the rare adaptation that "
            "improves a twist you already know: Flynn adapts her own "
            "novel and Pike plays the year's great ice-bath performance, "
            "turning the 'Cool Girl' speech into a mission statement. A "
            "marriage autopsy, a media satire, and the most uncomfortable "
            "ending thriller audiences have cheerfully applauded.",
        "faqs": [
            ("Is Gone Girl based on a book?",
             "Yes - Gillian Flynn's 2012 blockbuster novel, with a "
             "screenplay by Flynn herself (she changed the ending's "
             "texture, not its teeth). Fincher signed on partly because "
             "he wanted the author to keep control."),
            ("Was Rosamund Pike nominated for an Oscar for Gone Girl?",
             "Yes - Best Actress at the 2015 ceremony, for a performance "
             "that spends the film's second half doing something almost "
             "unplayable. The film's only nomination, oddly."),
            ("Why does Gone Girl end the way it does?",
             "The ending is the thesis: Amy wins by weaponising the "
             "narrative, and Nick chooses to stay inside the story she "
             "has written. The film calls marriage a performance and "
             "then makes it literal."),
        ],
    },
    "jaws": {
        "verdict": "The film that invented the summer blockbuster and "
            "still out-thrills its descendants: a malfunctioning robot "
            "shark forced Spielberg into suggestion, and absence became "
            "the scariest special effect ever. Three men, one boat, "
            "Shaw's USS Indianapolis monologue, and two notes of score "
            "that turned a beach into a threat. Perfect in every way "
            "that matters.",
        "faqs": [
            ("Why do you barely see the shark in Jaws?",
             "'Bruce' the mechanical shark barely functioned in salt "
             "water, so Spielberg withheld it - dread built on music, "
             "bathing legs and that yellow barrel. The accident created "
             "the suspense blueprint half a century of films copied."),
            ("How much money did Jaws make?",
             "It grossed around 476 million dollars worldwide on a "
             "roughly 9-million-dollar budget and became the "
             "highest-grossing film ever at the time - the birth of the "
             "wide summer release."),
            ("Did Jaws win any Oscars?",
             "Three, from Best Picture nomination: Editing, Sound and "
             "John Williams' score - possibly the most famous two notes "
             "in film history."),
        ],
    },
    "jurassic-park": {
        "verdict": "The theme park as perfection: Spielberg balances awe "
            "and appetite better than any film since, the brachiosaurus "
            "reveal still lands like religion, and the practical "
            "animatronics mean the T. rex kitchen scene has aged better "
            "than most modern CGI. Goldblum's chaos theorist, Newman's "
            "barbasol can, Williams' hymn - every piece is the right "
            "piece.",
        "faqs": [
            ("How did Jurassic Park make its dinosaurs look real?",
             "A blend Stan Winston's full-scale animatronics (the rain-"
             "soaked T. rex is largely mechanical) and ILM's digital "
             "breakthroughs - the first fully convincing CGI creatures "
             "in a feature, which reset the entire industry."),
            ("Did Jurassic Park win the Oscar for visual effects?",
             "Yes - at the 1994 ceremony, alongside Sound and Sound "
             "Effects Editing. Its Best Picture nomination went to "
             "Schindler's List territory the next year for Spielberg "
             "instead."),
            ("Is Jurassic Park scarier than Jurassic World?",
             "Most viewers find the 1993 original the tenser film - it "
             "builds dread in daylight and trusts silence, while the "
             "World entries lean louder and faster. Age-appropriate "
             "teens handle both; under-tens start with the original's "
             "fences, not its raptors."),
        ],
    },
    "logan": {
        "verdict": "The superhero film as elegy: a worn-out Wolverine "
            "escorting a dying Professor X across a desert that wants "
            "them both dead, with Mangold playing it as a western "
            "(Shane, openly, on the motel TV). Jackman and Stewart give "
            "the performances the franchise never let them give, and "
            "Dafne Keen's Laura says nothing and breaks everything. The "
            "rarest thing: a farewell with no reservations.",
        "faqs": [
            ("Do I need to watch the X-Men films before Logan?",
             "You need the relationship - Jackman's seventeen years as "
             "Wolverine and Stewart's Xavier - more than any specific "
             "plot. The film burns the continuity down and works as a "
             "standalone elegy for everything it references."),
            ("Is Logan based on a comic?",
             "Yes - Mark Millar and Steve McNiven's Old Man Logan arcs "
             "and Death of Wolverine, loosely combined; Mangold shot a "
             "black-and-white 'Noir' version that mirrors the source's "
             "grit."),
            ("Was Logan nominated for an Oscar?",
             "Yes - Best Adapted Screenplay at the 2018 ceremony, the "
             "first live-action superhero film nominated in a writing "
             "category."),
        ],
    },
    "john-wick": {
        "verdict": "The action film rebuilt on craft: long takes, real "
            "driving, and geometry you can read - Stahelski was Reeves' "
            "stunt double, and it shows in every fall. The dog is the "
            "hook, the Continental is the world, and the pencil is the "
            "legend. What could have been a forgettable revenge "
            "thriller became the genre's load-bearing pillar.",
        "faqs": [
            ("Is John Wick based on a book or comic?",
             "No - an original screenplay by Derek Kolstad. The world "
             "(the High Table, gold coins, the Continental's rules) was "
             "built across the films as the first one's success "
             "demanded more mythology."),
            ("How many John Wick films are there?",
             "Four theatrical chapters so far (2014-2023), with Ballerina, "
             "an Ana de Armas spin-off, extending the world - and the "
             "franchise famously ends each entry with Wick in worse "
             "shape and higher stakes."),
            ("Did Keanu Reeves do his own stunts in John Wick?",
             "A large share of them - he trained in judo, jiu-jitsu and "
             "tactical shooting for months per film and performs much of "
             "the driving and fighting on camera, with Stahelski's stunt "
             "team handling the truly lethal work."),
        ],
    },
    "godzilla-kong": {
        "verdict": "The title is the promise and the film keeps it: two "
            "titans, one Hong King neon brawl, and a mech-Godzilla third "
            "act that gives the kids what the 1962 crossover only "
            "dreamed of. Wingard shoots scale with genuine spectacle "
            "logic, Hollow Earth is beautiful nonsense, and the human "
            "plot wisely stays out of the punching. Monster-movie "
            "comfort food, perfectly done.",
        "faqs": [
            ("Do I need Godzilla (2014) and King of the Monsters before "
             "Godzilla vs. Kong?",
             "The essentials: Titans are real, Godzilla defends the "
             "surface, and Monarch is the agency studying them. The "
             "Skull Island link matters for Kong; everything else is "
             "recapped by the screaming."),
            ("Who wins, Godzilla or Kong?",
             "Watch the film - it lands the match on points with a "
             "twist, then needs both titans for the real fight. The "
             "sequel (The New Empire, 2024) settles them as reluctant "
             "teammates."),
            ("Was Godzilla vs. Kong a streaming success?",
             "Yes - released mid-pandemic in cinemas and on HBO Max "
             "simultaneously, it became the service's biggest launch "
             "and grossed around 470 million dollars, reviving the "
             "Monsterverse."),
        ],
    },
    "iron-man": {
        "verdict": "The cornerstone: a risky star, a B-list hero, and a "
            "tonally confident origin story that treats genius as "
            "charisma. Downey plays Tony's reckoning with total wit, "
            "Favreau grounds the spectacle in a cave and a toolbox, and "
            "the improvised 'I am Iron Man' button rewrote franchise "
            "grammar. Everything after exists because this worked.",
        "faqs": [
            ("Do I need Iron Man to start the Marvel films?",
             "It is the recommended starting point - 2008's Iron Man is "
             "the first MCU film and its DNA (wit, legacy, the "
             "post-credits promise) runs through everything that "
             "follows."),
            ("Was the 'I am Iron Man' line improvised?",
             "Yes - the final press-conference line was Downey's "
             "improvisation, kept in the cut; it replaced a scripted "
             "non-answer and became the MCU's founding gesture."),
            ("How much did Iron Man make?",
             "About 585 million dollars worldwide on a "
             "then-risky 140-million-dollar budget - the hit that "
             "justified Marvel Studios' entire ten-year plan."),
        ],
    },
    "kung-fu-panda": {
        "verdict": "The parody that became the real thing: DreamWorks "
            "winks at kung-fu cinema for ten minutes, then plays the "
            "chosen-one story with complete sincerity - and lands the "
            "genre's actual philosophy, 'there is no secret "
            "ingredient', as its punchline and thesis. Black's Po, "
            "Hong's Shifu, and a snow-mountain training sequence that "
            "still teaches real structure. The studio's best film.",
        "faqs": [
            ("What is the secret ingredient in Kung Fu Panda?",
             "Nothing - Shifu and Po realise the Secret Ingredient Soup "
             "has no special ingredient: 'It is just you.' Belief, not "
             "props, is the film's whole martial arts lesson."),
            ("Was Kung Fu Panda nominated for an Oscar?",
             "Yes - Best Animated Feature at the 2009 ceremony (WALL-E "
             "won), plus a long afterlife as one of the most "
             "rewatched animated trilogies ever."),
            ("Do I need to watch Kung Fu Panda in order?",
             "Yes for the full arc - one makes Po the Dragon Warrior, "
             "two gives him inner peace and an origin, three completes "
             "the teacher's journey. The stand-alone jokes work "
             "anywhere; the story does not."),
        ],
    },
    "kpop-demon-hunters": {
        "verdict": "2025's word-of-mouth monster: a K-pop girl group "
            "hunting demons with a honmoon to protect, Sony animation "
            "firing on every cylinder - concert-beam battles, fan-cam "
            "cuts, and an earworm arsenal ('Golden' topping the actual "
            "Hot 100). It treats idol culture and demon lore with "
            "equal sincerity, and the Saja Boys may be animation's "
            "best villain-boyband. Netflix's biggest animated event "
            "ever, and it earns it.",
        "faqs": [
            ("Is KPop Demon Hunters getting a sequel?",
             "Netflix and Sony have moved forward with more stories in "
             "the world after it became the platform's most-watched "
             "original animated film; a sequel and a short film were "
             "confirmed in 2025-2026 coverage."),
            ("Did the KPop Demon Hunters songs really chart?",
             "Yes - 'Golden' by the fictional group HUNTR/X reached "
             "No. 1 on the Billboard Hot 100, and multiple songs from "
             "the film charted simultaneously - the soundtrack became "
             "a genuine pop event, not a novelty."),
            ("Is KPop Demon Hunters suitable for kids?",
             "Very - it is a crowd-pleaser for ages roughly six and "
             "up: bright, funny, musical, with demon-fighting action "
             "on the spooky-fun side rather than the scary side."),
        ],
    },
    "jawan": {
        "verdict": "Shah Rukh Khan's mass-cinema victory lap: a "
            "father-son vigilante double act aimed straight at systemic "
            "corruption, with Atlee staging action set pieces at "
            "maximum scale and SRK doing both ages with total command. "
            "Vijay Sethupathi relishes the villainy, Anirudh's score "
            "detonates on cue, and the crowd-pleasing is calibrated "
            "like artillery. One of Indian cinema's biggest hits, "
            "earned honestly.",
        "faqs": [
            ("Is Jawan streaming, and in which languages?",
             "It streams on Netflix in its original Hindi plus dubbed "
             "Tamil and Telugu - the film released theatrically in "
             "all three languages, standard practice for Atlee's "
             "pan-Indian productions."),
            ("Who does Shah Rukh Khan play in Jawan?",
             "A dual role: father Vikram Rathore and son Azad - a "
             "prison warden leading a masked crusade to hold the "
             "system accountable, the film's engine and its biggest "
             "surprise structure-wise."),
            ("How big a hit was Jawan?",
             "Among the highest-grossing Indian films ever - over "
             "1,100 crore rupees worldwide (well past $130 million) "
             "in 2023, shortly after Khan's Pathaan had already "
             "rewritten the year's record books."),
        ],
    },
    "lagaan": {
        "verdict": "The four-hour epic that makes you care "
            "passionately about a colonial-era cricket match: Aamir "
            "Khan's villagers bet their land tax on a game they have "
            "never played, and Gowariker builds the rules, the "
            "training, the last wicket with the patience of a master. "
            "Rahman's songs carry the hope; the monsoon finale is "
            "Indian cinema at full force. India's great crowd-pleaser "
            "with an Oscar stamp.",
        "faqs": [
            ("Did Lagaan win an Oscar?",
             "It was nominated - Best Foreign Language Film at the "
             "2002 ceremony, India's third nomination in the category "
             "(it lost to No Man's Land). It swept India's National "
             "and Filmfare awards."),
            ("Do I need to understand cricket to enjoy Lagaan?",
             "No - the film teaches the game's rules to its heroes "
             "and its audience simultaneously, and by the final "
             "innings you will be shouting at a match that ended "
             "140 years ago."),
            ("How long is Lagaan?",
             "About 224 minutes including intermission - the length "
             "is the point: songs, subplots and the full arc of a "
             "village learning to believe."),
        ],
    },
    "king-of-boys": {
        "verdict": "Nollywood's gangster epic, with Sola Sobowale "
            "giving one of the performances of the decade: Eniola "
            "Salami, businesswoman, kingmaker, monster, mother - "
            "Adetiba shoots Lagos power politics as opera, and the "
            "film's ambition (three hours of it) is the point. "
            "Brutal, theatrical, and completely gripping; the 2021 "
            "Netflix cut extends the reckoning into a seven-part "
            "saga.",
        "faqs": [
            ("Do I need to watch King of Boys before Return of the "
             "King?",
             "Yes - the 2018 film is the foundation; the Netflix "
             "sequel/series Return of the King (2021) continues "
             "Eniola Salami's story in exile and in power, and "
             "assumes every scar from the first."),
            ("Is King of Boys based on a true story?",
             "No - it is fiction, though its world of Nigerian "
             "political godfathers, kingmakers and street power is "
             "played with a realism that fuels the speculation."),
            ("Is King of Boys in English?",
             "Primarily English with substantial Yoruba, Hausa and "
             "Pidgin - part of what makes Sobowale's performance "
             "legendary is the language-switching range of the "
             "role."),
        ],
    },
    "the-black-book": {
        "verdict": "The Nollywood thriller that went global: a grieving "
            "professor and a corrupt-system conspiracy, shot with real "
            "action-film discipline - car chases that read, shootouts "
            "that sting - and RMD carrying the grief like a weight in "
            "his coat. Effiong's direction announced a new commercial "
            "ceiling for Nigerian cinema. Imperfect, propulsive, "
            "historic.",
        "faqs": [
            ("Why is The Black Book historically significant?",
             "It became the first Nigerian film to reach No. 1 on "
             "Netflix's global English-language top 10 (September "
             "2023), charting in dozens of countries and proving "
             "Nollywood's worldwide streaming audience."),
            ("Is The Black Book based on true events?",
             "It is fiction - a revenge thriller about military-era "
             "framing, police violence and elite impunity - but its "
             "anger is drawn from recognisably real Nigerian "
             "history."),
            ("Who stars in The Black Book?",
             "Richard Mofe-Damijo (RMD) as Professor Craig, with a "
             "supporting turn from Ade Laoye; written and directed "
             "by Editi Effiong for Netflix."),
        ],
    },
    "lionheart": {
        "verdict": "Genevieve Nnaji's directorial debut is Nigerian "
            "cinema at its warmest and most confident: a family "
            "business succession comedy about a daughter the men "
            "underestimate, played with total charm by Nnaji and "
            "veteran gravitas by Pete Edochie and Kanayo O. Kanayo. "
            "Gentle, funny, quietly feminist - and historically "
            "significant twice over.",
        "faqs": [
            ("Why was Lionheart disqualified from the Oscars?",
             "Nigeria's first Best International Feature submission "
             "was ruled ineligible because most of its dialogue is "
             "English - the academy's language rule, which many "
             "observers pointed out is itself a legacy of "
             "colonialism. The ruling caused international debate."),
            ("Is Lionheart a Netflix film?",
             "Yes - it was acquired as a Netflix Original, the first "
             "Nigerian film to premiere that way (2018), which is "
             "part of why its international audience is so large."),
            ("Is Lionheart suitable for family viewing?",
             "Ideal for it - a multigenerational comedy about "
             "family, business and respect, with no content flags "
             "beyond brief business tension. A perfect first "
             "Nollywood film for mixed audiences."),
        ],
    },

    "the-godfather": {
        "verdict": "The blueprint every gangster epic since has been measured against. Coppola plays "
            "family tragedy on opera-scale sets, and the film is patient the way great novels are - "
            "nothing rushes, everything lands. Unhurried, formally flawless, endlessly quoted.",
        "faqs": [
            ("Who directed The Godfather?",
             "Francis Ford Coppola, co-writing the screenplay with novelist Mario Puzo from Puzo's 1969 bestseller."),
            ("Do I need to watch the sequels?",
             "The 1972 original stands alone; Part II (1974) continues Michael's story and is widely ranked "
             "among the greatest sequels ever made."),
            ("How long is The Godfather?",
             "It runs just under three hours - a full evening, and the pacing rarely feels it."),
        ],
    },
    "the-dark-knight": {
        "verdict": "The comic-book film that argued with itself about chaos, and won. Nolan builds a crime "
            "epic first and a superhero film second, and Ledger's Joker remains the benchmark the genre "
            "keeps failing to beat. Bigger and darker than its predecessor in every department.",
        "faqs": [
            ("Is this a sequel?",
             "Yes - the second film of Christopher Nolan's Dark Knight trilogy, following Batman Begins (2005)."),
            ("Why is the Joker performance so famous?",
             "Heath Ledger's take on the character became one of cinema's most acclaimed villains, and earned "
             "a posthumous Academy Award for Best Supporting Actor."),
            ("Which order should I watch the trilogy in?",
             "Release order: Batman Begins, The Dark Knight, The Dark Knight Rises."),
        ],
    },
    "the-matrix": {
        "verdict": "The 1999 film that rewired action cinema - leather, bullet-time and a philosophy seminar "
            "fired at full speed. Two decades on it remains the cleanest 'reality is a lie' blockbuster ever "
            "built: propulsive, stylish, and smarter than it needed to be.",
        "faqs": [
            ("Who made The Matrix?",
             "The Wachowskis wrote and directed it; the film made their careers and changed action choreography industry-wide."),
            ("Is the story self-contained?",
             "Largely, yes - the 1999 film has a complete arc. The sequels expand (and divide audiences), with "
             "The Matrix Resurrections arriving decades later."),
            ("Why is it still so influential?",
             "Its mix of wire-fu action, digital-age paranoia and iconic visual language - the falling green code, "
             "the sunglasses, the red pill - has been quoted ever since."),
        ],
    },
    "whiplash": {
        "verdict": "A jazz film with the pulse rate of a thriller. Chazelle turns a music-school practice room "
            "into a battleground, and J.K. Simmons' Fletcher is one of the great screen monsters - terrifying "
            "because he might be right. The final performance is the most stressful ten minutes on this desk.",
        "faqs": [
            ("Is Whiplash based on something?",
             "Yes - Damien Chazelle's own 2013 short film of the same name, expanded into this feature."),
            ("What did it win?",
             "Three Academy Awards, including Best Supporting Actor for J.K. Simmons."),
            ("Do I need to like jazz?",
             "No - it helps to like tension. The music is the battlefield, not the homework."),
        ],
    },
    "casino-royale": {
        "verdict": "The reboot that rebuilt Bond from cold steel. Craig's debut strips the gimmicks, plays the "
            "brutality and the vulnerability honestly, and the free-running chase remains the franchise's best "
            "cold open. The film that made 007 matter again.",
        "faqs": [
            ("Who plays Bond here?",
             "Daniel Craig, in his first appearance as 007 - a grounded reboot of the character."),
            ("Is Casino Royale the first Bond story?",
             "It was Ian Fleming's first Bond novel, yes - though not the first Bond film, which is why multiple "
             "versions exist."),
            ("Does the story continue?",
             "Directly - Quantum of Solace picks up where this one ends, the only true immediate sequel in the "
             "Craig era."),
        ],
    },
    "die-hard": {
        "verdict": "The template for every one-location action film since: an ordinary cop, a tower full of "
            "hostages, and bare feet on glass. McClane gets tired, bleeds and cracks jokes - which is exactly "
            "why it still plays. And yes, it is a Christmas film; the argument is settled.",
        "faqs": [
            ("Is Die Hard really a Christmas movie?",
             "It is set at a Christmas party and watched every December - treat the debate as part of the fun."),
            ("Who directed it?",
             "John McTiernan, at the peak of his action run; the film is adapted from Roderick Thorp's novel "
             "Nothing Lasts Forever."),
            ("Are the sequels worth it?",
             "Opinions sharpen quickly after the first two - the 1988 original is the one to see first and most."),
        ],
    },
    "coco": {
        "verdict": "Pixar's Dia de Muertos masterpiece - a colour-drenched land of the dead, a family mystery, "
            "and a final act engineered with tissues in mind. The 'Remember Me' turn is a trap and you will "
            "walk into it willingly.",
        "faqs": [
            ("What is the film about?",
             "A boy who dreams of music in a family that bans it, accidentally crossing into the land of the "
             "dead during Dia de Muertos - the Mexican holiday honouring departed family."),
            ("Did Coco win awards?",
             "Yes - two Academy Awards, including Best Animated Feature."),
            ("Is it too sad for kids?",
             "It deals with loss head-on, but with warmth and humour - the ending is emotional, not frightening."),
        ],
    },
    "toy-story": {
        "verdict": "The 1995 film that started computer-animated features - and still one of the best scripts "
            "Pixar ever shipped. The toys' jealousy plot is airtight, the jokes hold, and the buddy arc became "
            "the studio's template for two decades.",
        "faqs": [
            ("Why is Toy Story historically important?",
             "It was the first feature-length film made entirely with computer animation - the shot that changed "
             "the industry."),
            ("Who voices the leads?",
             "Tom Hanks as Woody and Tim Allen as Buzz - the pairing the whole series is built on."),
            ("How many sequels are there?",
             "Three more Toy Story films followed, with the fourth (2019) widely praised as a worthy coda."),
        ],
    },
    "wall-e": {
        "verdict": "Pixar at its boldest and quietest: a near-wordless opening act on a trashed Earth, then a "
            "space romance that earns its big ideas without a lecture. The little robot's binocular heart is "
            "one of animation's great character designs.",
        "faqs": [
            ("Is it true there's barely any dialogue?",
             "Much of the opening plays almost wordlessly - the storytelling is visual, and that restraint is "
             "the point."),
            ("Who directed WALL-E?",
             "Andrew Stanton, the Pixar veteran behind Finding Nemo; the film won the Best Animated Feature Oscar."),
            ("Is it too slow for small kids?",
             "The first act is patient - but the robot physical comedy carries younger viewers through it."),
        ],
    },
    "back-to-the-future": {
        "verdict": "The perfect blockbuster machine: Zemeckis at full speed, an airtight script where every "
            "setup pays off, and the 1955 sequence as plotting taught through pure joy. Thirty-plus years of "
            "imitators and it still runs like a Swiss watch.",
        "faqs": [
            ("Who directed Back to the Future?",
             "Robert Zemeckis, with Steven Spielberg producing - the team that turned the famously rejected "
             "script into a phenomenon."),
            ("What order do the trilogy films go in?",
             "Release order: Back to the Future (1985), Part II (1989), Part III (1990)."),
            ("Is the trilogy worth continuing?",
             "Yes - Part II doubles the plotting games and Part III swaps genre entirely; the finale lands the "
             "story properly."),
        ],
    },
    "alien": {
        "verdict": "Ridley Scott's haunted house in space - pure dread, industrial set design that still "
            "out-ages most modern sci-fi, and the single greatest dinner-party disaster in cinema. The "
            "slowest-burn thriller on this desk and worth every cold minute.",
        "faqs": [
            ("Who directed Alien?",
             "Ridley Scott; the 1979 original launched a franchise that spans decades."),
            ("Alien or Aliens first?",
             "Release order: Alien (1979) is the horror template; Aliens (1986) shifts to full-throttle action "
             "under James Cameron."),
            ("Do the later prequels change the story?",
             "Prometheus and Covenant add backstory decades later - watch the originals first; they stand alone."),
        ],
    },
    "the-shining": {
        "verdict": "Kubrick's overhead-horror machine: a hotel with impossible geography, a slow descent, and "
            "Nicholson unwinding one calm-crazy scene at a time. The rare horror film where the stillness is "
            "the scary part.",
        "faqs": [
            ("Is The Shining based on a book?",
             "Yes - Stephen King's 1977 novel; King famously disagreed with Kubrick's colder take, and wrote "
             "his own 1997 miniseries in response."),
            ("Is there a sequel?",
             "Doctor Sleep (2019), based on King's 2013 sequel novel, follows Danny as an adult."),
            ("Where does 'Here's Johnny!' come from?",
             "Nicholson improvised the line from a TV catchphrase of the era - and it stayed in the film."),
        ],
    },
    "zodiac": {
        "verdict": "Fincher's procedural about the case that would not close: no jump scares, just mounting "
            "dread across years of newspaper ink and obsession. The scariest film on this desk because it "
            "stays closest to the documented record - and still ends unresolved.",
        "faqs": [
            ("Is Zodiac a true story?",
             "It is based on the real Zodiac killer case in late-1960s California - parts of which remain "
             "officially unsolved."),
            ("Who directed it?",
             "David Fincher, between his thrillers and The Social Network - his most restrained and most "
             "unsettling film."),
            ("Is it too slow?",
             "It is deliberately long and procedural - if you want a slasher, this is not that; if you want "
             "dread, it is unmatched."),
        ],
    },
    "your-name": {
        "verdict": "Shinkai's body-swap romance that became a global phenomenon - comet-lit animation gorgeous "
            "frame by frame, comedy front-loaded, and an ending that lands like first love. The gateway anime "
            "film for people who think they don't like anime.",
        "faqs": [
            ("Who made Your Name?",
             "Makoto Shinkai, writer-director and animator; the 2016 film made him a household name far beyond Japan."),
            ("What language is it in?",
             "Japanese - subtitled or dubbed both work; the visual storytelling carries either."),
            ("Is it connected to other Shinkai films?",
             "It stands alone; his later Weathering with You and Suzame are separate stories in a similar register."),
        ],
    },
    "3-idiots": {
        "verdict": "Bollywood's great campus comedy with a life philosophy smuggled inside - three hours that "
            "pass like forty minutes, a soundtrack a whole generation hums, and 'All izz well' as a survival "
            "mantra. The friendliest possible front door to Hindi cinema.",
        "faqs": [
            ("What language is 3 Idiots in?",
             "Hindi - it is one of Indian cinema's most-watched and most-subtitled films worldwide."),
            ("Is it based on a book?",
             "Loosely on Chetan Bhagat's novel Five Point Someone, with substantial changes - a detail the "
             "credits acknowledged after some public debate."),
            ("Where should I start with Indian films?",
             "This, or the desk's Indian cinema starter route - Lagaan is the other standing recommendation."),
        ],
    },
    "dangal": {
        "verdict": "The true-story wrestling drama that became one of Indian cinema's biggest ever: a stubborn "
            "father training daughters against a village's worth of odds. Aamir Khan plays the patriarch hard "
            "to like and harder to dismiss - and the bouts are shot better than most sports films manage.",
        "faqs": [
            ("Is Dangal a true story?",
             "Yes - wrestler Mahavir Singh Phogat training his daughters Geeta and Babita to national and "
             "international victory."),
            ("What language is it in?",
             "Hindi, with the Haryanvi flavour of its setting; the wrestling storytelling translates universally."),
            ("Why is it such a big deal?",
             "Beyond the box office, it landed squarely in India's conversation about daughters and sport - "
             "rare for a mainstream entertainer."),
        ],
    },
    "anikulapo": {
        "verdict": "Kunle Afolayan gives Nollywood its folklore epic: a tale of desire, jealousy and a "
            "mythical second chance, wrapped in gorgeous Yoruba-language production design. The film that "
            "made 'Akala' a household name far beyond its opening weekend.",
        "faqs": [
            ("What language is Anikulapo in?",
             "Primarily Yoruba - subtitled, and deeply rooted in Yoruba folklore and storytelling tradition."),
            ("Who made it?",
             "Kunle Afolayan, one of Nollywood's most prominent directors, with a cast led by Kunle Remi and "
             "Bimbo Ademoye."),
            ("Is it a good first Nollywood film?",
             "Yes - the myth structure is universal and the craft is a showcase; the desk's Nigerian thrillers "
             "route pairs well with it."),
        ],
    },

    "akira": {
        "verdict": "The 1988 animation that proved the medium could carry adult spectacle - Neo-Tokyo "
            "biker gang warfare with body horror and a satellite weapon, hand-drawn frame by glorious "
            "frame. Thirty-plus years on, it still out-animates most of what it inspired.",
        "faqs": [
            ("Is Akira based on a manga?",
             "Yes - Katsuhiro Otomo's own landmark manga, which he wrote and drew; he also directed the film."),
            ("Why is Akira so influential?",
             "Its detailed animation and cyberpunk vision shaped decades of sci-fi in and far outside Japan - "
             "the film is a standing reference point in global pop culture."),
            ("Is it suitable for younger viewers?",
             "No - it is violent and intense, and intended for adults and older teens."),
        ],
    },
    "alien-romulus": {
        "verdict": "The 2024 entry that understands the assignment: practical creatures, blue-collar "
            "space horror, set-piece dread between the original two films. It borrows boldly from its "
            "elders - sometimes too boldly - but the corridor terror is real again.",
        "faqs": [
            ("Where does Alien: Romulus fit in the timeline?",
             "Between Alien (1979) and Aliens (1986) - it works as a standalone survival story too."),
            ("Who directed it?",
             "Fede Alvarez, the director of the 2013 Evil Dead remake, with a largely young ensemble cast."),
            ("Do I need to have seen the originals?",
             "It helps - the film is in conversation with them - but newcomers can follow the plot fine."),
        ],
    },
    "amelie": {
        "verdict": "Jean-Pierre Jeunet's 2001 confection - a shy Montmartre waitress secretly rearranging "
            "the lives of her neighbours, rendered in colours you want to live inside. The rare feel-good "
            "film that earns its sweetness with craft.",
        "faqs": [
            ("What language is Amelie in?",
             "French - Audrey Tautou's breakout role launched on it, and the film became a worldwide phenomenon."),
            ("Did it win Oscars?",
             "It received multiple Academy Award nominations, including Best Foreign Language Film, and won "
             "audiences everywhere - awards count aside, its influence on 'quirky cinema' is enormous."),
            ("Is it a romance?",
             "Partly - it is more a portrait of a neighbourhood, with a shy love story threaded through it."),
        ],
    },
    "blade-runner": {
        "verdict": "Ridley Scott's 1982 neo-noir - rain-soaked megacity, Vangelis on the synthesiser, and "
            "the sci-fi question that outlives every effect shot: what makes a person? Deliberately slow, "
            "endlessly imitated, never equalled.",
        "faqs": [
            ("Which cut of Blade Runner should I watch?",
             "The Final Cut (2007) - Ridley Scott's preferred version; the film famously exists in several cuts."),
            ("Is it based on a book?",
             "Yes - Philip K. Dick's novel Do Androids Dream of Electric Sheep?"),
            ("Is it slow?",
             "By modern blockbuster standards, deliberately so - it is atmosphere-first noir; patience is the ticket price."),
        ],
    },
    "eternal-sunshine": {
        "verdict": "The best breakup film ever disguised as sci-fi - a couple erasing each other from "
            "memory, and a film that keeps rearranging itself as the deletion catches up. Wildly inventive, "
            "and quietly devastating about why people love badly.",
        "faqs": [
            ("Who made Eternal Sunshine of the Spotless Mind?",
             "Director Michel Gondry with writer Charlie Kaufman - the screenplay won the Academy Award for "
             "Best Original Screenplay."),
            ("Is it a romance or sci-fi?",
             "Both, inseparably - the memory-erasure premise is the mechanism, the relationship is the story."),
            ("Do Jim Carrey and Kate Winslet play against type?",
             "Yes - Carrey is restrained and melancholy, Winslet chaotic and volatile; both castings are the point."),
        ],
    },
    "ex-machina": {
        "verdict": "Alex Garland's 2014 directorial debut - a chamber piece about a programmer, his boss, "
            "and the android who may be testing them both. Three actors, one location, and more ideas per "
            "frame than most trilogies manage.",
        "faqs": [
            ("Is Ex Machina someone's first film?",
             "Yes - it was novelist Alex Garland's directorial debut; he went on to Annihilation and more."),
            ("Did it win awards?",
             "It won the Academy Award for Best Visual Effects - remarkable for a film built on restrained, "
             "intimate effects work."),
            ("Is it scary?",
             "It is unsettling rather than gory - the tension is psychological, and it builds like a trap."),
        ],
    },
    "the-prestige": {
        "verdict": "Christopher Nolan's 2006 duelling-magicians film - obsession as a magic trick told in "
            "three acts, with Bale and Jackman escalating past sanity. The twist is famous; the craft is "
            "what survives the rewatch.",
        "faqs": [
            ("Is The Prestige based on a book?",
             "Yes - Christopher Priest's 1995 novel, adapted by Jonathan and Christopher Nolan."),
            ("Who directed it?",
             "Christopher Nolan, between Batman Begins and The Dark Knight, with his regular behind-camera crew."),
            ("Should I avoid spoilers?",
             "Absolutely - the film is engineered around its reveals; go in clean and let it lie to you."),
        ],
    },
    "the-social-network": {
        "verdict": "Fincher and Sorkin turn a founding dispute into the sharpest dialogue duel of the "
            "decade - ambition, betrayal and a fortune accruing in the background of every deposition. "
            "Not a documentary; a myth with excellent lawyers.",
        "faqs": [
            ("Is The Social Network a true story?",
             "It is a dramatisation based on Ben Mezrich's book The Accidental Billionaires - several depicted "
             "events are disputed by the people involved."),
            ("Did it win Oscars?",
             "Yes - including Best Adapted Screenplay for Aaron Sorkin and Best Original Score for Trent "
             "Reznor and Atticus Ross."),
            ("Who directed it?",
             "David Fincher, at full formal precision; the film plays as a thriller with no thriller plot."),
        ],
    },
    "totoro": {
        "verdict": "Studio Ghibli's 1988 gentle giant - two sisters, a forest spirit, and the gentlest "
            "ghost story ever animated. No villain, no danger worth the name; just childhood rendered with "
            "a patience grown-up films rarely afford.",
        "faqs": [
            ("Who made My Neighbor Totoro?",
             "Hayao Miyazaki and Studio Ghibli - the creature became the studio's official logo."),
            ("Is it suitable for small children?",
             "Yes - it is one of the gentlest films in animation; the sweet spot is roughly ages four and up."),
            ("Do I need to watch other Ghibli films first?",
             "No - it stands alone; it is also the classic first step into the studio's catalogue."),
        ],
    },
    "forrest-gump": {
        "verdict": "Zemeckis and Hanks ride one man's decency through thirty years of American history - "
            "technically audacious, emotionally shameless, and still sweeping. The effects-driven historical "
            "cameos were the era's magic trick; the sincerity is why it endures.",
        "faqs": [
            ("Did Forrest Gump win the Best Picture Oscar?",
             "Yes - it won six Academy Awards including Best Picture, Best Director (Robert Zemeckis) and "
             "Best Actor (Tom Hanks)."),
            ("Is it based on a book?",
             "Yes - Winston Groom's 1986 novel; the film softens the book's edges considerably."),
            ("Why is it still so popular?",
             "The fusion of personal story with national history - and a lead performance that never winks."),
        ],
    },
    "fight-club": {
        "verdict": "Fincher's 1999 adaptation that bombed, then conquered the DVD era to become a "
            "generational argument. Shot like a cigarette burn on the print - and still the most "
            "misquoted satire in cinema.",
        "faqs": [
            ("Is Fight Club based on a book?",
             "Yes - Chuck Palahniuk's 1996 novel; the film's ending famously diverges from it."),
            ("Why is it called a cult classic?",
             "It underperformed in theatres, then found a massive second life on home video - and its "
             "central twist became one of pop culture's most referenced."),
            ("What's actually in it beyond the twist?",
             "A satire of consumer masculinity that the decade took at face value - the joke, and the "
             "reason it rewards rewatching."),
        ],
    },
    "gladiator": {
        "verdict": "Ridley Scott resurrects the Roman epic with mud, grit and Maximus - Crowe's vengeance "
            "arc is as clean as blockbuster storytelling gets, and the Colosseum sequences still roar. "
            "'Are you not entertained' became the genre's thesis statement.",
        "faqs": [
            ("Did Gladiator win Best Picture?",
             "Yes - five Academy Awards including Best Picture and Best Actor for Russell Crowe."),
            ("Is it historically accurate?",
             "It compresses and invents freely around real figures (Marcus Aurelius, Commodus) - it is "
             "historical spectacle, not history."),
            ("Is there a sequel?",
             "Yes - Gladiator II arrived in 2024, continuing the story decades later."),
        ],
    },
    "se7en": {
        "verdict": "Fincher's 1995 descent - two detectives, seven deadly sins, and a city where the rain "
            "never stops. The bleakest procedural on this desk and one of the most controlled: every frame "
            "is evidence of something.",
        "faqs": [
            ("What is Se7en about?",
             "A serial killer structuring murders around the seven deadly sins, and the two detectives "
             "hunting him - the investigation is the horror."),
            ("Why is the ending so famous?",
             "Because it completes the killer's design rather than defeating it - a twist that re-frames "
             "the whole film without cheating."),
            ("How dark is it?",
             "Very - grim, violent and cynical; this is the film to watch when you want to be shaken, not comforted."),
        ],
    },
    "andhadhun": {
        "verdict": "Sriram Raghavan's 2018 black-comedy thriller - a 'blind' pianist, a murder he maybe "
            "witnessed, and a plot that keeps selling you a new genre every fifteen minutes. Twisting "
            "cinema at its most confident, and India's National Award-winning Best Hindi film.",
        "faqs": [
            ("What language is Andhadhun in?",
             "Hindi - Ayushmann Khurrana stars as the pianist; the film also became a favourite of world "
             "cinema audiences far beyond India."),
            ("Did it win awards?",
             "Yes - it won the National Film Award for Best Feature Film in Hindi, among others."),
            ("Is it really that twisty?",
             "Yes - and the pleasure is that every twist feels fair; it has inspired remakes in multiple languages."),
        ],
    },
    "tumbbad": {
        "verdict": "Folk horror about greed as inheritance - a cursed ancestral treasure guarded by a "
            "hungry god, drenched in rain and dread. The most visually distinctive Hindi horror of its "
            "decade, and a film whose audience keeps growing with every re-release.",
        "faqs": [
            ("What language is Tumbbad in?",
             "Primarily Hindi, set in Maharashtra of the 1920s - Sohum Shah leads a small, committed cast."),
            ("Who directed it?",
             "Rahi Anil Barve, over a famously long production - the craft shows in every rain-soaked frame."),
            ("Is it too scary for casual viewers?",
             "It is atmospheric horror rather than jump-scare horror - dread and myth, with moments of real horror."),
        ],
    },
    "a-tribe-called-judah": {
        "verdict": "Funke Akindele's 2023 heist-with-heart - five brothers robbing their own mother's "
            "debtor, and a Nollywood crowd-pleaser that became the country's highest-grossing film at "
            "the time. Family comedy, real stakes, and a third act that lands hard.",
        "faqs": [
            ("Who made A Tribe Called Judah?",
             "Funke Akindele, one of Nollywood's most commercially successful filmmaker-actors, leading "
             "the ensemble."),
            ("Was it a box-office record?",
             "Yes - it became Nigeria's highest-grossing film on release, a record since surpassed by later "
             "Nollywood hits."),
            ("What language is it in?",
             "English with Yoruba and Pidgin woven through - subtitled releases travel well."),
        ],
    },
    "the-wedding-party": {
        "verdict": "Kemi Adetiba's 2016 ensemble rom-com - one Lagos wedding, every relative a detonator, "
            "and the film that reset Nollywood's box-office ceiling. Glossy, chaotic and proudly Eko; the "
            "comedy of errors structure travels perfectly.",
        "faqs": [
            ("Who directed The Wedding Party?",
             "Kemi Adetiba, who went on to direct the desk's other Nollywood recommendation, King of Boys."),
            ("Was it a record-breaker?",
             "Yes - it became the highest-grossing Nigerian film at the time of its release."),
            ("Is there a sequel?",
             "Yes - The Wedding Party 2 arrived the following year, moving the chaos abroad."),
        ],
    },
    "citation": {
        "verdict": "Kunle Afolayan's 2020 campus drama - a bright student pushing a sexual-harassment "
            "complaint against a star lecturer, and the machinery that closes ranks. Sober, necessary "
            "Nollywood with a breakout lead performance from Temi Otedola.",
        "faqs": [
            ("Who directed Citation?",
             "Kunle Afolayan, one of Nollywood's most prominent directors; Temi Otedola leads the cast."),
            ("What is it about?",
             "A university student's fight to be heard after reporting a professor - inspired by real "
             "conversations around harassment in Nigerian institutions."),
            ("Where did it premiere?",
             "It released as a Netflix original film in 2020, reaching a global audience."),
        ],
    },
    "chief-daddy": {
        "verdict": "Niyi Akinmolayan's 2018 farce - a wealthy patriarch dies, and an army of relatives "
            "descends on the estate with receipts. Broad, fast and very funny, carried by one of "
            "Nollywood's deepest ensemble casts.",
        "faqs": [
            ("Who directed Chief Daddy?",
             "Niyi Akinmolayan, one of Nollywood's most technically accomplished directors."),
            ("Is it connected to other films?",
             "It spawned a sequel, Chief Daddy 2 - the first film stands alone and is the one to see."),
            ("What's the tone?",
             "Pure family farce - escalating squabbles, punchlines per minute, and a warm heart under the chaos."),
        ],
    },
    # ---- film batch 7 (2026-09-24): 30 evergreen classics/anime/K-drama/MCU ----
    "aliens": {
        "verdict": "The rare sequel that swaps dread for adrenaline and somehow deepens the "
            "nightmare. Cameron takes Ridley Scott's haunted house to space-marine scale - "
            "pulse rifles, power loaders, and a queen - while keeping the corridors mean. "
            "One of the greatest action films ever made, and still the blueprint.",
        "faqs": [
            ("Do I need to see Alien (1979) before Aliens?",
             "Yes. Aliens is a direct sequel - it opens on Ripley decades after the Nostromo "
             "and assumes you know what the xenomorph is and what it cost her."),
            ("Is Aliens a horror film or an action film?",
             "Both, deliberately: the first hour rebuilds the dread, then the marines arrive "
             "and it becomes full-contact war. The transition is the trick that made it famous."),
            ("Did Aliens win Oscars?",
             "It was nominated for seven Academy Awards and won two - Visual Effects and Sound "
             "Effects Editing - with Sigourney Weaver nominated for Best Actress, almost unheard "
             "of for this genre."),
        ],
    },
    "apocalypse-now": {
        "verdict": "War as a hallucination you cannot wake from. Coppola's Vietnam odyssey "
            "took a legendary toll on everyone who made it, and the madness is on screen - "
            "the jungle, the doors, the bull. Not an entertainment; an experience that "
            "changed what films could be. See the 1979 cut first.",
        "faqs": [
            ("Is Apocalypse Now based on a book?",
             "Loosely on Joseph Conrad's 1899 novella Heart of Darkness, transplanted from "
             "colonial Africa to the Vietnam War - the river journey up to confront Kurtz "
             "is the spine of both."),
            ("Did Apocalypse Now win anything major?",
             "Yes - the Palme d'Or at Cannes in 1979, plus two Academy Awards, and it is a "
             "fixture of greatest-films lists."),
            ("Which version should I watch?",
             "Start with the 147-minute 1979 theatrical cut. The longer Apocalypse Now "
             "Redux and Final Cut are for people who already loved it once."),
        ],
    },
    "airplane": {
        "verdict": "The densest joke-per-minute film ever made, and the grandfather of every "
            "spoof comedy since. The gags fly past at airline-food speed - half are absurd, "
            "a quarter are all-timers, and the certainty is you cannot breathe. Watch it "
            "with people who quote it, or become one.",
        "faqs": [
            ("Is Airplane! a parody of a specific film?",
             "Yes - it is a near shot-for-shot parody of the 1957 drama Zero Hour!, plus the "
             "whole Airport disaster-movie genre. The deadpan borrowing of old dialogue is "
             "half the joke."),
            ("Is it suitable for kids?",
             "Broadly yes for teens - the humor is relentless innuendo and sight gags rather "
             "than anything graphic, though parents should expect questions about the "
             "scenery-chewing drag gags and one very odd drug sequence."),
            ("Why is it so quotable?",
             "Because every line is either a setup or a punchline - 'surely you can't be "
             "serious' being the most famous straight-man handoff in comedy."),
        ],
    },
    "back-to-the-future-2": {
        "verdict": "The middle chapter that swings for the fences: 2015, alternate 1985, "
            "and 1955 running simultaneously in a plot that should not work and does. "
            "The hoverboards and self-tying shoes are the postcard; the real fun is the "
            "impossible origami of the script.",
        "faqs": [
            ("What year does Back to the Future II travel to?",
             "The 'future' is 21 October 2015 - the film's 2015 predictions (hoverboards, "
             "video calls, wearable tech) became the internet's favourite scoreboard once "
             "the actual year arrived."),
            ("Why does Part II revisit the first film?",
             "Doc and Marty's trouble with the timeline forces a return to 1955 - the same "
             "week of the original, seen from new angles. Watch Parts I and II close together; "
             "they interlock."),
            ("Do I need to watch them in order?",
             "Yes - Part II ends on a cliffhanger that Part III resolves directly."),
        ],
    },
    "back-to-the-future-3": {
        "verdict": "The gentlest of the trilogy - a Western with a DeLorean. Trading 2015's "
            "gadgetry for 1885 campfires and a train chase, it gives Doc the love story the "
            "character deserved and the series a warm, unhurried goodbye. Cheered on by "
            "generations who watched it as kids, and it holds.",
        "faqs": [
            ("When is Back to the Future III set?",
             "Mostly 1885 - the Old West - with bookends in 1955. It is a full Western, "
             "stagecoach hold-ups and all, with the time machine out of fuel."),
            ("Is Part III the last one?",
             "Yes. The trilogy ends here by design, and cleanly - the 'Doc's adventures "
             "continue' coda is inside the film itself, not a sequel hook."),
            ("How long is it?",
             "118 minutes, the longest of the three."),
        ],
    },
    "all-quiet-on-the-western-front": {
        "verdict": "The Great War without glory: mud, machinery and boys fed into both. "
            "Edward Berger's German adaptation is austere where Hollywood versions were "
            "poetic, and the armistice-as-bureaucracy ending lands like a slap. Devastating, "
            "craft-perfect, and impossible to shake.",
        "faqs": [
            ("Is this the one that won the Oscars?",
             "Yes - four Academy Awards at the 2023 ceremony, including Best International "
             "Feature, plus its cinematography, production design and score."),
            ("Is it based on a true story?",
             "It adapts Erich Maria Remarque's 1929 novel, itself drawn from his experiences "
             "as a German soldier in the First World War - fiction built on living memory."),
            ("Is it very violent?",
             "Yes, and deliberately unspectacular about it: the violence is industrial and "
             "numbing rather than thrilling. That is the point, but go in warned."),
        ],
    },
    "annihilation": {
        "verdict": "Sci-fi as a slow fever dream. Garland sends five scientists into a zone "
            "where the rules of biology have gone strange, and lets the dread accumulate "
            "rather than explode. The ending divides rooms; nobody forgets it. For viewers "
            "who want ideas with their shivers.",
        "faqs": [
            ("Is Annihilation based on a book?",
             "Yes - the first of Jeff VanderMeer's Southern Reach trilogy. The film keeps the "
             "premise and the dread and takes its own path through them."),
            ("What is the Shimmer?",
             "The film's central mystery: a growing zone where DNA refracts and recombines - "
             "flora, fauna and eventually people. Explaining more would spoil the point."),
            ("Is it scary or just strange?",
             "Both - there are two sequences of pure horror (the bear will stay with you), "
             "wrapped in a meditation on self-destruction that is stranger than any monster."),
        ],
    },
    "ant-man": {
        "verdict": "The Marvel formula at its lightest and most likeable - a heist comedy "
            "that shrunk the stakes on purpose and got to keep the fun. Rudd's everyman charm "
            "does the lifting, Michael Pena's stories do the laughing. Not top-tier MCU; "
            "top-tier palate cleanser.",
        "faqs": [
            ("Do I need to see Ant-Man before other Marvel films?",
             "No - it is a standalone origin story that only lightly touches the wider "
             "Avengers continuity. A good entry point if the franchise feels heavy."),
            ("Is Ant-Man a comedy?",
             "Genuinely, yes - a heist comedy first, a superhero film second, and better for it."),
            ("How long is it?",
             "117 minutes, one of the shorter MCU entries."),
        ],
    },
    "avengers-age-of-ultron": {
        "verdict": "The busiest middle child in the MCU: a villain with a genuine argument, "
            "a farm-house detour the franchise has never repeated, and more setup per frame "
            "than payoff. Uneven but full of life - and the party scene alone earns its seat.",
        "faqs": [
            ("Who is Ultron?",
             "An AI peace program Tony Stark builds that concludes the best way to save the "
             "world is to end the Avengers - James Spader gives the machine real menace and "
             "worse, charm."),
            ("Is Age of Ultron essential viewing?",
             "For the Infinity Saga, yes - it introduces key characters and fractures that "
             "pay off in Civil War and beyond."),
            ("How long is it?",
             "141 minutes."),
        ],
    },
    "avengers-infinity-war": {
        "verdict": "Ten years of franchise converging into a villain's victory lap. Thanos "
            "is the protagonist and the film has the nerve to act like it - a two-and-a-half "
            "hour chase that keeps handing him wins. Ends on the boldest cliffhanger blockbusters "
            "have dared.",
        "faqs": [
            ("Do I need to have seen the earlier Marvel films?",
             "Ideally twenty of them. Infinity War assumes you know the Avengers, the "
             "Guardians, Thanos and the Infinity Stones - it is a finale, not an entry point."),
            ("Which film resolves the ending?",
             "Avengers: Endgame (2019) is the direct continuation - watch them back to back "
             "if you can."),
            ("How long is it?",
             "149 minutes, and it uses every one."),
        ],
    },
    "a-silent-voice": {
        "verdict": "An anime about bullying, deafness and the long cost of cruelty - handled "
            "with a tenderness most live-action never reaches. Kyoto Animation's craft is "
            "extraordinary: half the story is told in where people look. Bring patience for "
            "quiet; it earns every ounce of its catharsis.",
        "faqs": [
            ("Is A Silent Voice about deafness?",
             "Partly: a deaf girl, Shoko, and the boy who tormented her at school, years later "
             "seeking to make amends. It is really about whether people can change and who "
             "gets to forgive them."),
            ("Is it based on a manga?",
             "Yes - Yoshitoki Oima's manga, adapted by Kyoto Animation with Naoko Yamada "
             "directing."),
            ("Is it sad?",
             "Often, and it deals with depression and suicidal thoughts directly - moving, "
             "not merciless, but go in knowing the weight."),
        ],
    },
    "alice-in-borderland": {
        "verdict": "Squid Game's death-game cousin from Japan, with better puzzle design and "
            "a sci-fi undertow. Arisu the gamer nerd is a great survival lead precisely because "
            "he thinks rather than punches. Blink-and-you-miss-it brutality, cliffhanger "
            "engineering of the highest order.",
        "faqs": [
            ("What is Alice in Borderland based on?",
             "Haro Aso's manga: an aimless young gamer and his friends hide from the police "
             "in a public toilet and emerge into an empty Tokyo where survival games run on "
             "playing cards."),
            ("Is it like Squid Game?",
             "Similar premise family - deadly games, desperate players - but Alice leans "
             "sci-fi and puzzle-box, with each game having a logic the characters must solve."),
            ("Is it finished?",
             "No - the story has continued beyond the first two seasons, and each season "
             "closes on new questions. Binge with that in mind."),
        ],
    },
    "all-of-us-are-dead": {
        "verdict": "K-drama zombie escalation at full sprint: a school outbreak, kids with "
            "no way out, and adults who are frequently the second-biggest threat. The first "
            "episodes are the best pure zombie TV of its decade - what follows trades some "
            "focus for scale, and stays gripping.",
        "faqs": [
            ("Is All of Us Are Dead based on a webtoon?",
             "Yes - Joo Dong-geun's Korean webtoon, adapted with the school-as-quarantine "
             "premise intact."),
            ("How gory is it?",
             "Very - this is full-scale zombie violence plus some human cruelty. Brilliantly "
             "choreographed, not for the squeamish."),
            ("Is it a limited series?",
             "No - the first season ends with the outbreak unresolved and further story "
             "continues. Expect cliffhangers, not closure."),
        ],
    },
    "arcane": {
        "verdict": "The video-game adaptation that shamed an entire genre. Fortiche's "
            "painterly animation alone would justify it; the sibling tragedy of Vi and Jinx "
            "makes it one of this century's great shows. Every frame is a poster, every "
            "episode earns its songs.",
        "faqs": [
            ("Do I need to play League of Legends to follow Arcane?",
             "Not at all - it is a self-contained origin story about two sisters on opposite "
             "sides of a class war between the city of Progress and its underground. Knowing "
             "the game adds Easter eggs, nothing more."),
            ("Did Arcane win awards?",
             "Yes - the Emmy for Outstanding Animated Program in 2022, the first streaming "
             "series to win it, and it took the award again for season two."),
            ("What is the animation style?",
             "Hand-finished 3D - painterly textures over CG, music-video energy in the "
             "action, watercolour in the memories. Nothing else looks like it."),
        ],
    },
    "attack-on-titan": {
        "verdict": "The anime that spent ten years telling you it was a zombie-siege show "
            "while quietly building one of the great war tragedies. The animation peaks "
            "(that first season's titans remain unmatched nightmare fuel) and the plot pays "
            "off every brutal coin it banks. All-time tier, and now complete.",
        "faqs": [
            ("Is Attack on Titan finished?",
             "Yes - the manga ended in 2021 and the anime concluded in 2023 across four "
             "seasons. You can binge it complete, which is a luxury its weekly audience "
             "never had."),
            ("What is it actually about?",
             "The last human city behind enormous walls, man-eating titans outside them, "
             "and the boy who swears to kill them all - before the story keeps unfolding "
             "into politics, war and moral ruin."),
            ("How violent is it?",
             "Extremely, and unflinching from episode one. It is one of the great action "
             "tragedies, not a casual watch."),
        ],
    },
    "babadook": {
        "verdict": "The rare horror film that is really about something - grief as a "
            "houseguest that never leaves. Jennifer Kent's debut builds dread from a "
            "pop-up book and a mother-son relationship fraying to threads. Scary, sad, "
            "and the reason a thousand 'elevated horror' pitches got funded.",
        "faqs": [
            ("What is the Babadook meant to be?",
             "The film keeps it deliberately unresolved: a monster from a children's book "
             "and a stand-in for grief and resentment that cannot be evicted, only managed. "
             "Both readings are correct."),
            ("Is it very scary?",
             "Atmospherically, extremely - the dread outperforms the jump count. Sensitive "
             "viewers should know a child is in peril throughout."),
            ("How long is it?",
             "94 minutes, and it wastes none."),
        ],
    },
    "barry-lyndon": {
        "verdict": "Kubrick's most beautiful and most mischievous film: an 18th-century "
            "con-man's rise and fall, shot in candlelight with lenses built for NASA, "
            "narrated like a bedtime story that keeps leaving the room. Slow as molasses "
            "and exactly as rich. Give it a big screen and your full evening.",
        "faqs": [
            ("Why is Barry Lyndon famous for its cinematography?",
             "Kubrick shot entire interior scenes by actual candlelight using ultra-fast "
             "Zeiss lenses developed for NASA - images no film had achieved. It won the "
             "Oscar for cinematography, one of four the film took."),
            ("Is it based on a book?",
             "Yes - Thackeray's 1844 novel The Luck of Barry Lyndon, an Irish fortune-hunter's "
             "memoir of gambling, marriage and self-destruction."),
            ("Is it boring?",
             "It is three hours at 18th-century pace, and it is not for everyone - but the "
             "wit is dry and constant, and the craft is one of one."),
        ],
    },
    "battle-royale": {
        "verdict": "The original last-one-standing death game, two decades before it became "
            "a genre. Fukasaku's thriller is wilder and sadder than its imitators - a "
            "cartoon-cruel premise played for genuine heartbreak about generational betrayal. "
            "Every battle-royale since owes it rent.",
        "faqs": [
            ("What is Battle Royale about?",
             "A near-future Japan where a school class is randomly selected, collared, and "
             "dropped on an island with one rule: last survivor lives. The Hunger Games "
             "comparisons are fair; this came first and plays darker."),
            ("Is it very violent?",
             "Yes - that is its reputation and its point, though the satire of adult failure "
             "is the actual subject."),
            ("Was it controversial in Japan?",
             "Massively - government debates and a refused distribution deal at the time. "
             "It has since been reappraised as a classic of Japanese cinema."),
        ],
    },
    "before-sunrise": {
        "verdict": "Two strangers, one night, one city, and the best conversation in modern "
            "cinema. Linklater's film is almost nothing happening - and it is everything: "
            "charm, risk, and the specific ache of a connection with a deadline. The first "
            "third of one of the great romances.",
        "faqs": [
            ("Do I need to watch the Before trilogy in order?",
             "Yes ideally - Sunrise (1995), Sunset (2004), Midnight (2013), each nine years "
             "later in both fiction and reality. Each stands alone, but they gain enormously "
             "from sequence."),
            ("Is it just two people talking?",
             "Essentially yes - a walk through Vienna, wine, a record booth, a poet on a "
             "bridge. Whether that sounds like heaven or torture tells you if it is your film."),
            ("How long is it?",
             "A mere 97 minutes, one night long."),
        ],
    },
    "band-of-brothers": {
        "verdict": "Still the summit of the war miniseries. Ten hours with Easy Company "
            "from D-Day training to Germany's collapse - expensive, humane, and merciless "
            "about cost. The veteran interviews bookending each episode do more heavy lifting "
            "than any battle scene. Clear your calendar and your eyes.",
        "faqs": [
            ("Is Band of Brothers a true story?",
             "Yes - it follows the real Easy Company, 506th Parachute Infantry Regiment, "
             "through the Second World War, adapted from Stephen Ambrose's oral-history book."),
            ("Who made it?",
             "Executive-produced by Tom Hanks and Steven Spielberg for HBO, with different "
             "directors per episode - including Hanks himself - which gives each hour its "
             "own character."),
            ("How long is it?",
             "Ten episodes, roughly ten hours. Watch it as it aired: slowly, one war at a time."),
        ],
    },
    "big-hero-6": {
        "verdict": "The Disney film whose robot became a global mascot. Baymax the inflatable "
            "healthcare companion is a perfect character - gentle, literal, quietly hilarious "
            "- and the grief-and-healing story around him is better than the superhero plot "
            "it rides in on. Huggable with real feelings attached.",
        "faqs": [
            ("Is Big Hero 6 a Marvel film?",
             "It is Disney Animation's loose adaptation of a little-known Marvel comic - the "
             "names are Marvel, the tone is pure house-of-mouse. No MCU connection."),
            ("Did it win an Oscar?",
             "Yes - Best Animated Feature at the 2015 ceremony."),
            ("Who is Baymax?",
             "A vinyl, pill-shaped healthcare robot built to treat the sick - and one of "
             "animation's greats: the balloon that learns to grieve."),
        ],
    },
    "black-panther-2": {
        "verdict": "A sequel made in mourning that chooses to say so. Wakanda Forever buries "
            "its king, its actor, and a fair amount of its pace under grief - and earns real "
            "poetry anyway, with a stunning Namor and one of the MCU's most human final acts. "
            "Longer and sadder than you expect: let it be.",
        "faqs": [
            ("Do I need to see the first Black Panther?",
             "Yes - the sequel is a direct continuation, and its entire emotional weight comes "
             "from the loss the first film's king represents, on screen and off."),
            ("Why is the film about grief?",
             "Chadwick Boseman, who played T'Challa, died in 2020 before filming. Coogler "
             "reshaped the story around the loss rather than recasting - the film is the "
             "tribute."),
            ("How long is it?",
             "161 minutes."),
        ],
    },
    "blazing-saddles": {
        "verdict": "The Western that burned the genre down laughing - and took studio "
            "racism, Hollywood fakery and good taste with it. Fifty years on, Brooks's "
            "satire is still the boldest thing in the room precisely because its target is "
            "the bigotry, never the victims. Deliberately silly; secretly razor-edged.",
        "faqs": [
            ("Is Blazing Saddles offensive?",
             "It trades in the slurs and stereotypes of the Westerns it is mocking, pointed "
             "squarely at racists - a distinction some viewers still debate. It is a satire "
             "of bigotry, made with genuine anger underneath the gags."),
            ("Is that really the ending?",
             "Yes - the film literally breaks its own set, crashes through the studio wall "
             "into another genre, and ends in a canteen. It could not be more on purpose."),
            ("How long is it?",
             "93 minutes of pure 1974 anarchy."),
        ],
    },
    "anchorman": {
        "verdict": "A film with no interest in being good and every interest in being "
            "legendary. Ron Burgundy is a magnificent idiot in a leather suit, the news-team "
            "street brawl remains the funniest set piece of its decade, and the quotes have "
            "outlived several careers. Improv capital-C Comedy.",
        "faqs": [
            ("Is Anchorman based on a real newsman?",
             "No - it is a 1970s San Diego news-desk satire built entirely for silliness, "
             "loosely nodding to the era's first female anchors through Christina Applegate's "
             "Veronica Corningstone."),
            ("Which cut should I watch?",
             "The theatrical cut is the classic. The 'unrated' extended versions add hours "
             "of alternate improv that fans will love and first-timers should skip."),
            ("How long is it?",
             "94 minutes in cinemas."),
        ],
    },
    "21-jump-street": {
        "verdict": "The reboot that taught Hollywood the trick: admit the premise is ridiculous "
            "and weaponise it. Lord and Miller turn a stale TV cop show into a laugh-a-minute "
            "buddy movie with real chemistry, real action and a self-awareness that never "
            "winks itself to death. The rare comedy with actual craft under the chaos.",
        "faqs": [
            ("Do I need to know the original TV show?",
             "No - the film is built on mocking its own source premise (undercover cops in "
             "high school), and explains the joke in the first act."),
            ("Is it very crude?",
             "Yes - R-rated language, drugs and violence played for laughs, with a genuinely "
             "sweet friendship underneath."),
            ("Is there a sequel?",
             "Yes - 22 Jump Street (2014), which turns the sequel itself into the joke, and "
             "is nearly as funny."),
        ],
    },
    "a-taxi-driver": {
        "verdict": "The Korean hit that turns a cab ride into a nation's awakening. Based on "
            "the true story of a German reporter and the Seoul taxi driver who smuggled him "
            "into 1980 Gwangju, it balances humour, terror and decency with total control. "
            "The history is harrowing; the film is humane.",
        "faqs": [
            ("Is A Taxi Driver based on a true story?",
             "Yes - German journalist Jurgen Hinzpeter really did ride into the 1980 Gwangju "
             "uprising thanks to a local driver; the film honours both men and the city that "
             "fed them."),
            ("Do I need to know Korean history first?",
             "No - the film gives you enough context as it goes. Knowing Gwangju was violently "
             "suppressed by the military makes it land harder, not necessary."),
            ("How long is it?",
             "137 minutes, Korean with English subtitles."),
        ],
    },
    "avatar-fire-and-ash": {
        "verdict": "Cameron's third Pandora epic goes darker: new Na'vi clans, a fire-lit "
            "tone shift, and 197 minutes of the most expensive world-building in cinema "
            "history. If you bought a ticket to the ocean two films ago, this is the winter "
            "event it promised.",
        "faqs": [
            ("Do I need to see the first two Avatar films?",
             "Yes - Fire and Ash continues the Sully family story directly from The Way of "
             "Water (2022), which ends on unresolved conflict."),
            ("Who are the Ash People?",
             "The new Na'vi clan introduced in this film - a volcanic, fire-associated culture "
             "that breaks the franchise's 'naive good vs colonising evil' symmetry, according "
             "to Cameron's own promotion of the film."),
            ("How long is it?",
             "197 minutes - three hours and 17 minutes. Plan the bathroom run accordingly."),
        ],
    },
    "avengers-doomsday": {
        "verdict": "The MCU's big reset button: the next Avengers event, with the Russo "
            "brothers back at the wheel and Robert Downey Jr returning to the franchise - "
            "as Doctor Doom. Whether the multiverse gambit pays off arrives with the film; "
            "the casting gamble alone already rewrote the conversation.",
        "faqs": [
            ("When is Avengers: Doomsday releasing?",
             "It is dated for late 2026, the next flagship Avengers film after Endgame's era "
             "wound down - check current listings near release for exact dates."),
            ("Is Robert Downey Jr playing Iron Man again?",
             "No - Marvel announced him as Doctor Doom, a different character entirely. The "
             "meta-frisson of Tony Stark's actor as the new big bad is the whole conversation."),
            ("Do I need to watch everything since Endgame first?",
             "It helps - the multiverse arc across recent films feeds in - but the Avengers "
             "films remain designed as convergence points you can enter from the trailers."),
        ],
    },
    "alien-3": {
        "verdict": "The franchise's beautiful failure: Fincher's debut, shot in production "
            "hell, opening by destroying what you loved - and still full of furnace-light "
            "beauty and genuine dread. Flawed, mournful, twice recut into better versions. "
            "Not the film anyone wanted; weirdly worth your time anyway.",
        "faqs": [
            ("Is Alien 3 really that bad?",
             "It is the series' black sheep and a genuine mess of a production - yet Fincher's "
             "style bleeds through, and the Assembly Cut is regarded by many fans as a dark "
             "minor classic."),
            ("Do I need to watch Alien and Aliens first?",
             "Yes - its opening directly follows Aliens' ending, and the loss it deals is the "
             "whole film's engine. Which is also why it angers people."),
            ("Which version exists?",
             "Several: the 1992 theatrical cut (114 minutes) and the longer 2003 Assembly Cut "
             "are the main two - the latter is Fincher-adjacent, unfinished, and preferred by "
             "devotees."),
        ],
    },
    "animal": {
        "verdict": "Bollywood's most polarising blockbuster in years: a father-son saga "
            "drenched in blood, slow-motion and unfiltered misogyny, made with total conviction "
            "and a 200-minute runtime. As craft, frequently electrifying; as politics, exactly "
            "as divisive as the discourse says. You will not be bored - that is the warning.",
        "faqs": [
            ("What is Animal about?",
             "The violent, obsessive devotion of a son (Ranbir Kapoor) to his industrialist "
             "father, and what that love does to everyone around it - a gangster family epic "
             "in the vein of the director Sandeep Reddy Vanga's earlier hits."),
            ("Why is it controversial?",
             "Its treatment of women and glorification-of-violence debates dominated the "
             "internet on release - it is a film explicitly about masculine rage that many "
             "viewers felt wallowed in it. Expect to argue afterwards."),
            ("How long is it?",
             "201 minutes - one of the longest mainstream Hindi films ever released. Eat first."),
        ],
    },
    # ---- film batch 8 (2026-09-24): 30 titles - classics, Ghibli, K-drama, prestige TV, Nollywood ----
    "pulp-fiction": {
        "verdict": "The film that broke the nineties open and reassembled it out of order. "
            "Hitmen discussing burgers, a glow-in-the-dark briefcase, a gold watch with a "
            "very specific history - every scene became culture. Still electric, still "
            "funny, still the reason half of modern cinema owes Tarantino rent.",
        "faqs": [
            ("Why is Pulp Fiction told out of order?",
             "Its three main stories interlock but are shown shuffled - the structure is the "
             "point: chance, consequence and a circular ending that only lands out of sequence."),
            ("Did Pulp Fiction win the Oscar?",
             "It won Best Original Screenplay (Tarantino and Roger Avary) at the 1995 "
             "ceremony, and lost Best Picture to Forrest Gump - still the era's most argued result."),
            ("Is it very violent?",
             "Yes, abruptly and unsentimentally - plus heavy language and one needle-drop "
             "scene people never forget. A classic, not a comfy one."),
        ],
    },
    "the-shawshank-redemption": {
        "verdict": "The most beloved film on the internet, and for once the consensus is "
            "right. Two decades inside Shawshank prison, one friendship, and a final ten "
            "minutes that have repaired more bad days than modern medicine. It streams, "
            "it endures, it hits every time.",
        "faqs": [
            ("Was Shawshank a flop at first?",
             "Genuinely yes - it underperformed in 1994 cinemas and won zero of its seven "
             "Oscar nominations, then became one of the most-watched films ever through "
             "home video and television."),
            ("Is it based on a book?",
             "A Stephen King novella - Rita Hayworth and Shawshank Redemption, from the "
             "collection Different Seasons."),
            ("Why is it rated so highly?",
             "Because it earns its hope honestly: patience, friendship and dignity against "
             "an institution built to grind them away. The payoff is one of cinema's great "
             "releases."),
        ],
    },
    "godfather-part-ii": {
        "verdict": "The sequel that out-mastered the masterpiece: Michael's soul in the "
            "present, his father's rise in the past, cut against each other like two halves "
            "of a tragedy sharing one spine. De Niro's young Vito is iconic; Pacino's eyes "
            "do the actual storytelling. The arguable peak of the American film.",
        "faqs": [
            ("Do I need to see the first Godfather?",
             "Absolutely - Part II continues Michael's story directly and its flashback half "
             "only resonates because you know where Vito ends up."),
            ("Did it win Best Picture?",
             "Yes - the first sequel ever to win the Academy Award for Best Picture (1975), "
             "with De Niro taking Best Supporting Actor for his Italian-language performance."),
            ("How long is it?",
             "165 minutes - and treat it as an event, not background viewing."),
        ],
    },
    "empire-strikes-back": {
        "verdict": "The Star Wars that grew up: the heroes lose, the villain tells the "
            "truth that rewired a generation, and the ending leaves everything hanging on "
            "purpose. Still the franchise's peak for most who love it - darker, deeper, "
            "and with the saga's best third act.",
        "faqs": [
            ("Which Star Wars film is 'I am your father' from?",
             "The Empire Strikes Back (1980) - the duel revelation is among the most famous "
             "scenes ever filmed, and the line is often misquoted."),
            ("Do I need to watch A New Hope first?",
             "Yes - Empire is the middle chapter of the original trilogy and assumes everything "
             "the first film set up."),
            ("Who directed it?",
             "Irvin Kershner, from a story by George Lucas - the hand-off that gave the saga "
             "its darkest, most personal chapter."),
        ],
    },
    "raiders": {
        "verdict": "The perfect adventure film, full stop. Spielberg at maximum velocity, "
            "Ford at maximum charm, a boulder, a whip, and Nazis getting what was coming - "
            "every set piece a masterclass in momentum. Eighty years of blockbusters have "
            "been chasing this high.",
        "faqs": [
            ("Is Raiders of the Lost Ark the first Indiana Jones?",
             "Yes - 1981, the start of the series and still its benchmark (the later "
             "prequel, Temple of Doom, is actually set earlier in time)."),
            ("Did it win any Oscars?",
             "Five, at the 1982 ceremony - art direction, cinematography, editing, sound "
             "and visual effects. It lost Best Picture to Chariots of Fire."),
            ("Is it suitable for kids?",
             "Broadly - it is PG in the old, bold sense: spooky faces melting and skeletons, "
             "thrilling rather than gruesome. A rite of passage at about eight."),
        ],
    },
    "terminator-2-judgment-day": {
        "verdict": "The sequel that swallowed its genre whole: the terrifying assassin "
            "returns as protector, and Cameron turns a B-movie premise into opera - liquid "
            "metal, oil-truck chases, and 'hasta la vista' entering the language. Groundbreaking "
            "effects that somehow never age.",
        "faqs": [
            ("Do I need to see The Terminator (1984) first?",
             "Yes - T2's entire premise (who the guardian is, why Sarah knows too much) depends "
             "on it, and it is a classic in its own right."),
            ("Did T2 win Oscars?",
             "Four at the 1992 ceremony - makeup, sound, sound effects editing and visual "
             "effects, for effects that still hold up three decades later."),
            ("Why is it considered better than the original?",
             "It is not better so much as bigger in every dimension - the action scaled up, "
             "the heart scaled up. Which one is supreme remains the bar-room argument."),
        ],
    },
    "the-departed": {
        "verdict": "Scorsese's Boston powder keg: a cop inside the mob, a mobster inside "
            "the police, and nobody - on screen or in the audience - safe for a second. "
            "Rat-a-tat dialogue, genuine dread, and an ending that lands like a slap. "
            "The Best Picture the director had waited decades for.",
        "faqs": [
            ("Is The Departed based on another film?",
             "Yes - a remake of Hong Kong's Infernal Affairs (2002), transplanted to Boston "
             "with Scorsese's crime-family DNA all over it."),
            ("Did it win Best Picture?",
             "Yes - the 2007 Academy Awards, plus Best Director for Scorsese, his first "
             "win after decades of masterpieces."),
            ("Is it very violent?",
             "Frequently and suddenly - the film's tension depends on the sense that anyone "
             "can go at any moment. That is not an idle promise."),
        ],
    },
    "goodfellas": {
        "verdict": "The greatest gangster film about being a gangster - not the throne, the "
            "job: the perks, the paranoia, the petty treacheries and the slow rot. Scorsese's "
            "kinetic genius is at full blast - the Copacabana tracking shot alone is film-school "
            "gospel. Funny until it very suddenly is not.",
        "faqs": [
            ("Is Goodfellas based on a true story?",
             "Yes - Nicholas Pileggi's book Wiseguy, the documented life of mob associate "
             "Henry Hill; the Lufthansa heist at its centre really happened."),
            ("Why is the restaurant tracking shot famous?",
             "One unbroken glide takes Henry and Karen through the back door, corridors and "
             "kitchen to a front-row table - half a decade of status conveyed in a single move."),
            ("Is it better than The Godfather?",
             "Different animals: Coppola's is Shakespearean tragedy, Scorsese's is kinetic "
             "documentary energy. The eternal argument has no wrong answer."),
        ],
    },
    "casablanca": {
        "verdict": "Eighty years of imitations and still the standard: a gin joint, a "
            "bitter expat, a woman walking in with the war behind her. Every line lands, "
            "every glance means two things, and the ending remains the most mature in "
            "Hollywood history. They genuinely do not make them like this.",
        "faqs": [
            ("What is Casablanca about?",
             "Morocco during the Second World War: cynical club owner Rick must choose "
             "between the woman he loves and helping her resistance husband escape - "
             "sacrifice over desire, duty over the heart."),
            ("Did it win Best Picture?",
             "Yes - three Academy Awards in 1944, including Best Picture and Best Director."),
            ("Is it black and white, and is that a problem?",
             "It is, and it is not - the shadows and smoke are half the romance. Even "
             "first-time classic-haters tend to surrender by the twenty-minute mark."),
        ],
    },
    "memento": {
        "verdict": "The puzzle-box that made Nolan's name: a man who cannot form new "
            "memories hunts his wife's killer backwards, and the film runs the same trick "
            "on you. Genuinely clever rather than pretending to be - and underneath the "
            "gimmick, a real story about the stories we tell ourselves.",
        "faqs": [
            ("Does Memento play backwards?",
             "Alternating: one thread runs in reverse scene by scene, intercut with a "
             "forward-moving thread - the two collide at the ending, which is also the "
             "beginning of the truth."),
            ("Is it based on a book?",
             "No - on a short story by Nolan's brother Jonathan (Memento Mori), written "
             "while the film was being pitched."),
            ("Should I watch the chronological version?",
             "Not first. The disorientation is the design; the re-ordered cut exists for "
             "rewatchers who want to see the trick from the other side."),
        ],
    },
    "children-of-men": {
        "verdict": "The dystopia that ages into prophecy: no children for eighteen years, "
            "a Britain of cages and camps, and one escort mission through it all. Cuarón's "
            "camera refuses to blink - those long battle takes are legendary - and the film "
            "is more relevant every single year. Devastating craft.",
        "faqs": [
            ("Is Children of Men based on a book?",
             "On P. D. James's 1992 novel, though the film transposes its mystery into an "
             "immigrant-refugee frame all its own."),
            ("Why is it famous for its camera work?",
             "Several sequences play as single unbroken shots - the car ambush and the "
             "final war-zone walk especially - stitching chaos into terrifying continuity."),
            ("Is it very bleak?",
             "Yes - and it ends on the exact honest note of hope the genre usually fakes."),
        ],
    },
    "predator": {
        "verdict": "The eighties action film that wanders into a horror film and never "
            "comes back: Schwarzenegger's commandos meet something that hunts them for "
            "sport, and the jungle closes in. Muscles, one-liners, dread and the single "
            "greatest creature design of its decade. Perfect popcorn with teeth.",
        "faqs": [
            ("Is Predator a horror film or an action film?",
             "It starts as the latter and becomes the former - the switch from buddy-war "
             "movie to stalk-and-slash is the whole architecture of its genius."),
            ("Who is in the cast?",
             "Arnold Schwarzenegger leads, with a pre-governor future mind - Carl Weathers, "
             "and two future US state governors sharing a screen."),
            ("How does it connect to the Alien films?",
             "It does not, on screen - the famous crossover (Alien vs Predator) is a comics "
             "and later-film affair. This stands alone."),
        ],
    },
    "heat": {
        "verdict": "The crime epic of the nineties: cop and criminal orbiting each other "
            "with monastic discipline until the streets pay for it. The downtown shootout "
            "rewrote how films sound, the diner scene is two legends sharing coffee like "
            "duellists, and the whole thing hums at three hours. Michael Mann's masterpiece.",
        "faqs": [
            ("Is Heat based on a true story?",
             "Loosely on Chicago cop Chuck Adamson's pursuit of thief Neil McCauley - the "
             "diner meeting between De Niro and Pacino mirrors a real conversation the two "
             "men once had."),
            ("Is this the first Pacino-De Niro film together?",
             "They shared The Godfather Part II without sharing scenes; Heat's diner scene "
             "is their first true on-screen face-off."),
            ("How long is it?",
             "171 minutes - clear the evening; the payoff is worth every one."),
        ],
    },
    "looper": {
        "verdict": "The rare time-travel film that solves its own paradoxes and then finds "
            "the human story hiding inside them: a hitman killing targets sent from the "
            "future, until the next target is himself. Smart, scrappy, Willis and Gordon-"
            "Levitt doing career-best work. Sci-fi with a bruise.",
        "faqs": [
            ("Do I need to follow every time-travel rule?",
             "No - Johnson states the rules clearly, then keeps the focus on choices rather "
             "than mechanics. It rewards attention without requiring a diagram."),
            ("Is Bruce Willis the villain?",
             "He is the complication: the older version of the main character arriving into "
             "his own past with a mission of his own. Whether that makes him villain or "
             "saviour is the film's real question."),
            ("How long is it?",
             "119 minutes, tight as a drum."),
        ],
    },
    "oldboy": {
        "verdict": "Park Chan-wook's revenge odyssey - imprisoned for fifteen years without "
            "explanation, released with five days to find out why. Style and savagery in "
            "perfect balance: the corridor hammer fight, the octopus, and a final revelation "
            "that remains cinema's cruellest gut-punch. Not for the squeamish; unmissable "
            "for everyone else.",
        "faqs": [
            ("Is Oldboy based on a manga?",
             "Yes - Nobuaki Minegishi and Garon Tsuchiya's Japanese manga, though Park's film "
             "takes its own road to an even darker destination."),
            ("How violent is it?",
             "Brutally - torture, self-harm and one revelation whose impact outdoes any "
             "violence. This is a hard-18 experience and a masterpiece of that register."),
            ("Is it part of a series?",
             "It is the middle film of Park's informal Vengeance trilogy - each stands alone."),
        ],
    },
    "memories-of-murder": {
        "verdict": "Bong Joon-ho's true-crime masterwork: rural detectives chasing Korea's "
            "first serial killer in the rain, with procedures that keep failing and a "
            "final look into the camera that still haunts. Funny, furious, and quietly "
            "one of the finest films of its century.",
        "faqs": [
            ("Is Memories of Murder a true story?",
             "Yes - it dramatises the real Hwaseong serial murders of 1986-91; the killer "
             "was identified only after the film was made, which makes its ending look "
             "prophetic."),
            ("Is it like Memories of a Murderer on other platforms?",
             "Different works exist about the case - Bong's 2003 feature is the acclaimed "
             "one, based on the play Come to See Me."),
            ("Do I need to like crime dramas to love it?",
             "It helps, but the film is really about incompetence, dictatorship-era Korea "
             "and the guilt of not knowing - it transcends its genre on purpose."),
        ],
    },
    "crash-landing-on-you": {
        "verdict": "The K-drama that made the world cry over a paragliding accident: a "
            "South Korean heiress blown over the border into North Korea, and the officer "
            "who hides her. Sixteen hours of warmth, absurdity, genuine peril and the "
            "best found-family on television. The gateway K-drama for a reason.",
        "faqs": [
            ("Is Crash Landing on You based on real events?",
             "Only loosely - the premise echoes the real case of a South Korean woman whose "
             "boat drifted north; the romance and comedy are pure drama."),
            ("How long is it?",
             "Sixteen episodes at about seventy minutes each - a full, generous commitment."),
            ("Is it funny or sad?",
             "Both, constantly - the fish-out-of-water comedy carries real danger and a "
             "bittersweet core. Keep tissues within reach from episode eight."),
        ],
    },
    "extraordinary-attorney-woo": {
        "verdict": "The gentlest phenomenon on television: a brilliant autistic attorney "
            "navigating courtrooms, whales, and colleagues learning to deserve her. Park "
            "Eun-bin's performance is a marvel of specificity and dignity. Kind, clever, "
            "casewise - comfort viewing with substance.",
        "faqs": [
            ("Is Extraordinary Attorney Woo based on a book?",
             "No - an original drama, though each case draws on real Korean legal and social "
             "questions."),
            ("What makes it different from other legal dramas?",
             "Its protagonist's autism is neither superpower nor tragedy - the show works "
             "through how environments, colleagues and courts adapt to a mind like hers, "
             "case by case."),
            ("How long is it?",
             "Sixteen episodes of about seventy minutes; most cases resolve within an episode, "
             "with the relationships carrying the series."),
        ],
    },
    "vincenzo": {
        "verdict": "The K-drama that threw everything at the wall - mafia consigliere, "
            "corporate villains, tenant-cooperative comedy, romance, fountain of gold - and "
            "somehow conducted it into a hit. Song Joong-ki's antihero is deliciously cold "
            "until he very much is not. Gloriously excessive.",
        "faqs": [
            ("What is Vincenzo about?",
             "A Korean-Italian mafia lawyer returns to Seoul to recover hidden gold beneath "
             "a condemned building - and goes to war with the conglomerate squatting on it, "
             "armed with nothing but legal process and mob craft."),
            ("Is it a comedy or a thriller?",
             "A machete-cut hybrid: broad slapstick one scene, chilling revenge the next - "
             "its tonal confidence is the whole appeal."),
            ("How long is it?",
             "Twenty episodes - a big, satisfying commitment."),
        ],
    },
    "one-piece": {
        "verdict": "Twenty-five years and still sailing: the shonen epic about a rubber "
            "pirate chasing the world's greatest treasure that quietly became the story of "
            "freedom, found family and every kind of oppression. The pacing punishes, the "
            "payoff redeems - there is a reason it is the best-selling manga ever.",
        "faqs": [
            ("Is One Piece still ongoing?",
             "Yes - the manga entered its final saga, while the anime continues adapting it; "
             "there has literally never been a better time to start than after the arcs that "
             "recently concluded."),
            ("Do I need to read the manga first?",
             "No - the anime is the canonical experience for most, and the pacing issues "
             "that used to plague it have been reined in for the modern arcs."),
            ("How long is it?",
             "Over a thousand episodes - begin with the East Blue arc and let the world "
             "argue about fillers once you are hooked."),
        ],
    },
    "death-note": {
        "verdict": "The thriller that made a generation of non-anime viewers into anime "
            "viewers: a student finds a notebook that kills anyone whose name is written "
            "in it, and the world's greatest detective arrives to stop him. A high-wire "
            "game of moral vanity, in thirty-seven tight episodes.",
        "faqs": [
            ("Is Death Note based on a manga?",
             "Yes - Tsugumi Ohba and Takeshi Obata's mega-selling manga; the 2006 anime "
             "adapts it in 37 episodes."),
            ("Should I stop watching after a certain point?",
             "You will meet this opinion online: many fans consider the story's natural "
             "climax to arrive late in the series. Watch the whole thing and form your own "
             "verdict - the ending is more divisive than broken."),
            ("Is it scary?",
             "It is tense, gothic and morally unsettling rather than gory - a psychological "
             "duel, not a horror."),
        ],
    },
    "fullmetal-alchemist-brotherhood": {
        "verdict": "The most complete anime ever made: two brothers break alchemy's one "
            "taboo and spend sixty-four episodes paying for it across a plot that weaves "
            "war, faith, family and every character's story into one flawless braid. Start "
            "to finish, zero filler - the genre's high-water mark.",
        "faqs": [
            ("Do I need to watch the 2003 Fullmetal Alchemist first?",
             "No - Brotherhood (2009) follows the manga's complete story; the 2003 series "
             "branched off on its own path when the manga was unfinished. Start with Brotherhood."),
            ("Is it dubbed well?",
             "Yes - the English dub is widely regarded as excellent, which is rare air for anime."),
            ("Is it suitable for teens?",
             "Mature themes and some genuinely dark body horror - best for older teens and "
             "up, and rewarding at every age above that."),
        ],
    },
    "spirited-away": {
        "verdict": "Miyazaki's masterpiece and the greatest animated film ever made, if you "
            "believe the Academy (it won the Oscar) or the box office (it ruled Japan for "
            "two decades). A girl lost in a bathhouse for spirits - and a film about courage, "
            "greed and names, drawn by hand at an altitude nobody else breathes.",
        "faqs": [
            ("Did Spirited Away win an Oscar?",
             "Yes - Best Animated Feature at the 2003 ceremony, the first hand-drawn and "
             "non-English-language film to win it."),
            ("Is it scary for children?",
             "Mildly - some transformations and a temperamental river spirit startle younger "
             "viewers, though the film was made for and beloved by children. About eight and "
             "up is the classic starting age."),
            ("Do Miyazaki films connect?",
             "No - each Studio Ghibli film stands alone; start here or with My Neighbour "
             "Totoro and work outwards."),
        ],
    },
    "princess-mononoke": {
        "verdict": "Miyazaki's wildest, most adult fable: gods of the forest against the "
            "humans of Iron Town, with no villains and no easy side. The ecological rage, "
            "the muscular hand-drawn action, and a moral seriousness most live-action never "
            "reaches. Ghibli at its most fierce.",
        "faqs": [
            ("Is Princess Mononoke suitable for kids?",
             "Older kids and up - it is Ghibli's most violent film by some distance, with "
             "dismemberments and curses; teenagers are the natural audience."),
            ("Is it connected to Spirited Away?",
             "No - a separate story, released four years earlier. Both are Miyazaki, nothing more."),
            ("What is it really about?",
             "The irreconcilable: civilisation's needs against nature's, told through humans "
             "who are each right and each guilty. Nobody wins cleanly, which is the point."),
        ],
    },
    "suzume": {
        "verdict": "Shinkai's disaster-fable road movie: a girl, a boy turned into a chair, "
            "and doors across Japan that must be closed before what is behind them gets out. "
            "Breathtaking backdrops, an emotional core about grief and growing up, and the "
            "most gorgeous catastrophe animation going.",
        "faqs": [
            ("Is Suzume connected to Your Name or Weathering With You?",
             "No - Shinkai's films share themes (love, weather, catastrophe) but stand alone; "
             "this one is inspired in part by Japan's 2011 earthquake and tsunami."),
            ("Is it based on a book?",
             "It received a novelisation and manga alongside release, but the film is the "
             "original work."),
            ("Is it good for family viewing?",
             "Yes for older children - the peril is real but kind, and the talking chair is "
             "exactly as delightful as it sounds."),
        ],
    },
    "breaking-bad": {
        "verdict": "The complete crime tragedy: a dying chemistry teacher chooses pride over "
            "protection and becomes the thing he feared, one impeccable episode at a time. "
            "The most controlled five-season arc television has produced - no filler, no "
            "false steps, and an ending that sticks the landing.",
        "faqs": [
            ("Is Breaking Bad based on a true story?",
             "No - Vince Gilligan's invention, though its descent is so precise it feels "
             "documented."),
            ("How many seasons and how long is an episode?",
             "Five seasons, 62 episodes, roughly 47 minutes each - about two months of "
             "evenings, and worth every one."),
            ("Do I need Better Call Saul first?",
             "No - Breaking Bad first; the prequel then deepens in ways its own right. "
             "The intended order is the publication order."),
        ],
    },
    "true-detective": {
        "verdict": "Season one remains a high-water mark of the prestige-crime era: two "
            "Louisiana detectives, seventeen years, and a ritual murder that curdles everything "
            "it touches. McConaughey and Harrelson are magnetic, Fukunaga's direction is "
            "hypnotic, and the show is genuinely about something - time, guilt, light against "
            "the dark. Anthology: each season stands alone.",
        "faqs": [
            ("Do the True Detective seasons connect?",
             "No - it is an anthology: each season is a new case, cast and era. Season one "
             "(2014) is the acclaimed landmark most people mean."),
            ("Is it horror or crime?",
             "Crime first, with cosmic-horror dread woven through - the occult atmosphere "
             "is real, the explanation is human."),
            ("Is it very dark?",
             "Yes - violence, nihilism and some truly disturbing imagery. It earns its "
             "darkness with ideas, not shock alone."),
        ],
    },
    "sholay": {
        "verdict": "The Indian film that defined 'blockbuster' for a billion people: two "
            "buddies, a vengeful thakur, a dacoit with a voice like gravel, and every song "
            "a national memory. Fifty years on, its lines are still quoted at weddings and "
            "in parliament. The Western, the friendship film and the festival all at once.",
        "faqs": [
            ("Why is Sholay so famous?",
             "It is the template - the biggest hit of classic Hindi cinema, running in some "
             "theatres for years, and the source of a disproportionate share of Indian "
             "pop-culture's most quoted dialogue."),
            ("Is it a Western?",
             "An Indian one - the grammar of Seven Samurai and Spaghetti Westerns transposed "
             "to village India, with the bromance and the songs that make it pure Bollywood."),
            ("How long is it?",
             "About 204 minutes in its restored form - an event, as intended."),
        ],
    },
    "rrr": {
        "verdict": "The most aerobic action epic ever made: two revolutionaries, one "
            "explosive friendship, and action sequences staged with such conviction they "
            "briefly suspend disbelief worldwide. Rajamouli does not choreograph scenes; "
            "he launches them. Watch it loudest, with the biggest crowd you can assemble.",
        "faqs": [
            ("Is RRR a true story?",
             "It borrows two real Indian revolutionaries (Komaram Bheem and Alluri Sitarama "
             "Raju) and then invents - gloriously - the friendship and fireworks between them."),
            ("Did RRR really win an Oscar?",
             "Yes - Best Original Song for 'Naatu Naatu' at the 2023 ceremony, following that "
             "viral dance number around the world."),
            ("Is it in Hindi?",
             "It is a Telugu-language film (with dubs) - part of what made its global success "
             "a landmark for Indian cinema beyond Bollywood."),
        ],
    },
    "oloture": {
        "verdict": "Nollywood's hardest look in the mirror: a reporter goes undercover in "
            "Lagos's sex trade and finds a world the city prefers unseen. Kenneth Gyang's "
            "film is humane, unsensational and quietly furious - the rare exposé that trusts "
            "its people more than its plot. Essential Nigerian cinema.",
        "faqs": [
            ("Is Oloture based on a true story?",
             "It is fiction inspired by real reporting on trafficking and prostitution rings "
             "in Nigeria - the conditions depicted are documented, the characters are crafted."),
            ("Is it connected to the series?",
             "A follow-up series continued the story on streaming - the film stands alone "
             "but leaves the door open."),
            ("Is it difficult to watch?",
             "Emotionally, yes - exploitation and violence against women are its subject "
             "matter, handled seriously rather than for spectacle."),
        ],
    },
    # ---- film batch 9 (2026-09-24): 30 titles - Kurosawa, Star Wars, horror, anime, TV landmarks ----
    "scarface": {
        "verdict": "The rise-and-fall fable at maximum volume: Tony Montana claws from raft-"
            "arrival to Miami kingpin to a staircase of bullets, and De Palma shoots every "
            "rung like it's the last. Excess is the subject and the method - 'say hello' "
            "entered the language. Three hours of opera for gangsters.",
        "faqs": [
            ("Is Scarface based on a true story?",
             "It is a loose remake of Howard Hawks' 1932 Scarface, inspired by Al Capone - "
             "Pacino's Montana is fiction, but the prohibition-era skeleton shows through."),
            ("Why is it rated so high in culture?",
             "Its lines, its look and its soundtrack saturated hip-hop and video games for "
             "decades - it is as much a style manual as a film."),
            ("How long is it?",
             "165 minutes, and the last act earns every one."),
        ],
    },
    "reservoir-dogs": {
        "verdict": "The debut that announced Tarantino: a heist film with no heist, just "
            "the paranoid aftermath, colour-coded strangers and a ear and a razor. Talk "
            "as violence, violence as punchline - ninety-nine minutes of pure nerve. Indie "
            "cinema's big bang.",
        "faqs": [
            ("Is Reservoir Dogs the first Tarantino film?",
             "Yes - his 1992 debut, funded on a shoestring, and the seedbed of everything "
             "from the timelines to the needle-drops that came after."),
            ("Why don't we see the heist?",
             "The film is the before-and-after: the robbery failed off-screen, and the "
             "mystery of who tipped off the police is the plot. Withholding it is the trick."),
            ("How long is it?",
             "A lean 99 minutes."),
        ],
    },
    "casino": {
        "verdict": "Goodfellas' colder, grander sibling: Las Vegas as a machine for skimming, "
            "run with mechanical brilliance and dismantled by ego, drugs and betrayal. De "
            "Niro precise, Pesci unhinged, Sharon Stone heartbreaking - and Scorsese's "
            "montages turn greed into choreography. Long, glittering, pitiless.",
        "faqs": [
            ("Is Casino based on a true story?",
             "Yes - Nicholas Pileggi's book on Frank 'Lefty' Rosenthal and Tony Spilotro, "
             "the real mob enforcer's run over Las Vegas in the 1970s-80s."),
            ("Is it a sequel to Goodfellas?",
             "No - a companion piece by the same director and co-writer, different true "
             "story, same DNA."),
            ("How long is it?",
             "178 minutes."),
        ],
    },
    "seven-samurai": {
        "verdict": "The blueprint for every team-assembles adventure ever made: a starving "
            "village hires seven swordsmen, and Kurosawa spends three and a half hours "
            "turning archetypes into people before the rain-soaked final battle. Three "
            "hours and twenty-seven minutes, and not one wasted frame - the honourable "
            "granddaddy of heists, Westerns and superhero lineups alike.",
        "faqs": [
            ("What did Seven Samurai inspire?",
             "Directly, The Magnificent Seven; structurally, nearly everything from Star "
             "Wars to any 'gather the team' film - the recruiting-the-experts structure "
             "is Kurosawa's gift to cinema."),
            ("Is it really over three hours?",
             "207 minutes in the complete cut. It plays faster than films half its length."),
            ("Is it silent-era style?",
             "No - a sound film, 1954, with battle sequences whose camerawork still looks "
             "modern; the criterion is patience rewarded."),
        ],
    },
    "rashomon": {
        "verdict": "The film that taught the world that truth has versions: a bandit, a "
            "wife, a samurai and a woodcutter recount one crime four ways, and Kurosawa "
            "refuses to referee. Eighty-eight minutes that gave psychology a term - the "
            "'Rashomon effect' - and cinema its modern grammar of doubt.",
        "faqs": [
            ("What is the Rashomon effect?",
             "The term for contradictory interpretations of the same event by different "
             "witnesses - named directly for this film's structure."),
            ("Is the truth ever revealed?",
             "The film withholds a definitive version on purpose; what settles is not the "
             "fact but the choice to act decently despite doubt."),
            ("How long is it?",
             "A tight 88 minutes."),
        ],
    },
    "dr-strangelove": {
        "verdict": "The funniest film ever made about the end of the world: Kubrick's "
            "cold-war satire flies a B-52 over squabbling generals, mangled phone calls "
            "and Peter Sellers in three roles, straight into doomsday. Fifty years of "
            "nuclear anxiety distilled into ninety-three minutes of perfect farce.",
        "faqs": [
            ("Why is it black and white?",
             "By design - 1964's satirical bite lands harder in austere monochrome, and "
             "the war-room set became iconic in it."),
            ("Did Peter Sellers really play three roles?",
             "Yes - the president, the RAF officer and the title scientist; a fourth part "
             "was abandoned after an injury on set."),
            ("Is the ending really like that?",
             "Yes - 'We'll meet again' over mushroom clouds remains the boldest final "
             "joke in cinema."),
        ],
    },
    "star-wars-a-new-hope": {
        "verdict": "The film that made the modern blockbuster: a farm boy, a smuggler, a "
            "princess and a death star, shot with a serial-serial heart and a brand-new "
            "kind of spectacle. Whatever the saga became, it starts here - and the binary "
            "sunset still works on everyone.",
        "faqs": [
            ("What is the correct order to watch Star Wars?",
             "Fans debate eternal: release order (this film first) preserves the saga's "
             "reveals; chronological order starts with the prequels. Most veterans say: "
             "release order, always."),
            ("Did it win any Oscars?",
             "Six at the 1978 ceremony - art direction, costumes, effects, music, editing "
             "and sound - plus a special award for the sound design."),
            ("Is it worth watching after all the newer films?",
             "More than ever - every later film is in conversation with it, and its "
             "economy of storytelling is the lesson blockbusters keep relearning."),
        ],
    },
    "return-of-the-jedi": {
        "verdict": "The trilogy's victory lap: Ewoks, the sail barge, and Luke's final "
            "refusal to strike - the saga's moral payoff dressed in the brightest colours. "
            "Leia's gold bikini and the teddy bears divide fans forever; the throne-room "
            "duel unites them. The circle completes.",
        "faqs": [
            ("Is Return of the Jedi the last in the original trilogy?",
             "Yes - following A New Hope and The Empire Strikes Back, it closes the "
             "Skywalker story as it stood from 1977-83."),
            ("Why do people argue about the Ewoks?",
             "Some find the teddy-bear warriors cute merch-bait; others the proof the "
             "series remembered children exist. Both are allowed; the film sails anyway."),
            ("How long is it?",
             "132 minutes."),
        ],
    },
    "rogue-one-a-star-wars-story": {
        "verdict": "The war film Star Wars always implied but never showed: expendable "
            "spies stealing the Death Star plans, no chosen ones, no escapes guaranteed. "
            "Third-act space combat of rare grandeur, a Vader moment fans scream about, "
            "and the saga's best ending-for-its-beginnings logic.",
        "faqs": [
            ("Do I need other Star Wars films before Rogue One?",
             "It helps enormously - it is a direct prequel to A New Hope, and its final "
             "scene connects frame-for-frame."),
            ("Does everyone die?",
             "The film's reputation for wartime honesty precedes it; expect sacrifice, "
             "delivered seriously."),
            ("How long is it?",
             "133 minutes."),
        ],
    },
    "the-mandalorian": {
        "verdict": "The show that returned Star Wars to its campfire roots: a bounty "
            "hunter, a mysterious child, and episodic frontier adventures with blockbuster "
            "craft. Early seasons are the franchise's warmest embrace in decades - Western "
            "cadence, zero homework required.",
        "faqs": [
            ("Do I need to have seen the Star Wars films first?",
             "No - it is designed as a doorway: knowing the films adds flavour, knowing "
             "nothing blocks nothing. 'This is the way' works on its own."),
            ("Is that baby Yoda?",
             "The child the internet adopted is Grogu - of the same species as Yoda, "
             "narratively his own small person, and the engine of the show's heart."),
            ("How many seasons?",
             "Three seasons so far, with the story continuing into film plans - check "
             "current listings for where it stands today."),
        ],
    },
    "the-avengers": {
        "verdict": "The team-up that proved the experiment: four franchises, one "
            "shwarma-fuelled ensemble, and Whedon's dialogue doing the impossible - making "
            "an event film feel like banter. The Battle of New York rewrote the scale of "
            "superhero cinema, and it has not stopped since.",
        "faqs": [
            ("Do I need to see the films before The Avengers?",
             "Ideally the five that precede it (Iron Man, Thor, Captain America, Hulk "
             "continuity) - the payoff is assembly itself. But the film hands you enough "
             "to enjoy the ride cold."),
            ("Who is the villain?",
             "Loki, Thor's adopted brother, playing conqueror with genuine relish - Hiddleston's "
             "breakout and the MCU's best early antagonist."),
            ("How long is it?",
             "142 minutes."),
        ],
    },
    "the-dark-knight-rises": {
        "verdict": "Nolan's trilogy coda swings operatic: a broken Batman against Bane's "
            "occupation of Gotham, with revolution as set piece and a finale that aims "
            "for catharsis and mostly lands it. Imperfect and enormous - the rare "
            "blockbuster with an ending it means.",
        "faqs": [
            ("Do I need the first two Dark Knight films?",
             "Yes - it concludes a direct trilogy, and its plot leans on debts the first "
             "two films opened."),
            ("Is Bane's voice understandable?",
             "A famous talking point - the muffled megaphone delivery was adjusted between "
             "trailer and film; most viewers adapt within minutes."),
            ("How long is it?",
             "164 minutes."),
        ],
    },
    "guardians-of-the-galaxy": {
        "verdict": "The risk that paid for a decade: a comedy of space losers with a "
            "mixtape, a talking tree and a raccoon - and suddenly the MCU had a soul to "
            "match its spectacle. The soundtrack is a character, the found family is the "
            "point, and the jokes actually land. Marvel's most rewatchable gamble.",
        "faqs": [
            ("Do I need Marvel knowledge for Guardians?",
             "Almost none - it introduces its whole corner from zero, which is why it "
             "became the franchise's favourite entry point."),
            ("Is it more comedy than the other MCU films?",
             "Yes, unapologetically - though the third act smuggles in real grief, and "
             "the sequels deepen that blend."),
            ("How long is it?",
             "121 minutes."),
        ],
    },
    "captain-america-the-winter-soldier": {
        "verdict": "The MCU's stealth political thriller: Captain America versus a "
            "surveillance state infiltrating his own side, played as seventies paranoia "
            "with shield throws. The Russo brothers' breakout - tight action, real "
            "consequences, and the twist that reshaped the whole franchise.",
        "faqs": [
            ("Is The Winter Soldier a spy thriller or a superhero film?",
             "Both, deliberately - the conspiracy structure is straight out of the "
             "seventies paranoid-thriller tradition, with super-soldiers."),
            ("Do I need to see the first Captain America?",
             "It helps - the emotional weight of the title character depends entirely on "
             "the 2011 origin story."),
            ("How long is it?",
             "136 minutes."),
        ],
    },
    "the-conjuring": {
        "verdict": "The haunted-house film that relaunched a genre: old farmhouse, dark "
            "cellar, hands in the dark - and Wan's camera doing the scaring with pure "
            "craft. Loosely built on the Warrens' case files, it plays classical rather "
            "than gross. The gateway modern horror, and the start of a universe.",
        "faqs": [
            ("Is The Conjuring based on a true story?",
             "It dramatises paranormal investigators Ed and Lorraine Warren's claimed 1971 "
             "Perron family case - 'based on the case files', with everything that implies "
             "about artistic licence."),
            ("How scary is it really?",
             "Very, by construction rather than gore - jump scares orchestrated with "
             "genuine skill. It is the film people watch with cushions and then recommend."),
            ("How long is it?",
             "112 minutes."),
        ],
    },
    "the-exorcist": {
        "verdict": "Still the heavyweight champion of horror: a mother, a possessed child, "
            "and two priests walking into the most infamous room in cinema. Friedkin plays "
            "possession as medical crisis and faith crisis at once - the craft is so "
            "straight-faced it remains terrifying fifty years on. The one that started "
            "the headlines.",
        "faqs": [
            ("Why is The Exorcist so famous?",
             "It turned horror into an event - Oscar-nominated for Best Picture, lines "
             "around the block, faintings reported - and its practical effects still "
             "outclass most modern attempts."),
            ("Is it really that scary?",
             "It is disturbing more than jumpy: the dread is theological and the imagery "
             "has never left the culture. First-time viewers consistently report it hits "
             "harder than expected."),
            ("How long is it?",
             "122 minutes."),
        ],
    },
    "halloween": {
        "verdict": "The blueprint slasher, still the purest: one night, one masked shape, "
            "a suburb full of unlocked doors, and Carpenter's synth score doing half the "
            "killing. Made for almost nothing, terrifying forever - every October "
            "franchise since is living in its shadow.",
        "faqs": [
            ("Is Michael Myers supernatural?",
             "The film keeps it deliberately unexplained - pure shape, pure force. The "
             "sequels explain; this one understands that explaining is the mistake."),
            ("Is the 2018 Halloween connected?",
             "Yes - the later films reboot from the original, ignoring every sequel in "
             "between. This 1978 film is the only required viewing."),
            ("How long is it?",
             "A knife-clean 92 minutes."),
        ],
    },
    "the-thing": {
        "verdict": "Carpenter's Antarctic masterpiece: research station, shape-shifting "
            "invader, and the total collapse of trust between men snowed in with it. "
            "Practical effects that remain the peak of the form, an ending of perfect "
            "despair, and the best 'who is still human?' game in film. A flop that became "
            "a religion.",
        "faqs": [
            ("Is The Thing a remake?",
             "It remakes 1951's The Thing from Another World, returning to the original "
             "novella's shape-shifter - and outgrowing both predecessors."),
            ("Why do fans revere the effects?",
             "Rob Bottin's in-camera creature work - splitting faces, dogs, tables of "
             "meat - predates CGI and has never been surpassed; every frame is a craftsman "
             "at the top of a doomed art."),
            ("How long is it?",
             "109 minutes of paranoia."),
        ],
    },
    "midsommar": {
        "verdict": "The break-up horror bathed in daylight: grief, a toxic relationship "
            "and a Swedish midsummer festival that flowers into ritual horror under a sun "
            "that never sets. Aster makes dread from flowers and white linen - beautiful, "
            "unhurried, and quietly one of the most upsetting films of its decade.",
        "faqs": [
            ("Is Midsommar as scary as Hereditary?",
             "Differently - Hereditary is claustrophobic night-terror; Midsommar is "
             "daylight dread, its horrors visible from far away and inevitable."),
            ("Is there a director's cut?",
             "Yes - Aster's preferred cut runs about 24 minutes longer, deepening the "
             "relationship decay; the theatrical cut is the standard entry."),
            ("How long is it?",
             "147 minutes theatrically."),
        ],
    },
    "jujutsu-kaisen": {
        "verdict": "Modern shonen's darkest star: cursed spirits fed by human negativity, "
            "a sorcerer school, and MAPPA's animation turning every fight into a "
            "wet-bloodied ballet. Yuji Itadori swallowing a finger starts a story that "
            "keeps choosing cruelty and craft in equal measure - the genre's current peak.",
        "faqs": [
            ("Is Jujutsu Kaisen finished?",
             "No - the manga ran to its conclusion, while the anime continues adapting "
             "with new seasons; the story it tells is complete on the page."),
            ("Is it as gory as people say?",
             "Yes - this is dark supernatural action with real violence and real deaths; "
             "it earns its 16+ reputation."),
            ("Where should I start?",
             "Season one, episode one - the story is built to be watched in order."),
        ],
    },
    "demon-slayer": {
        "verdict": "The phenomenon that broke records: a boy joins the demon-slaying "
            "corps to cure his sister, and ufotable's water-and-flame animation turned "
            "each sword stroke into a national event. The Mugen Train arc alone made it "
            "Japan's biggest film ever. Spectacle first, heart underneath, tears guaranteed.",
        "faqs": [
            ("Is Demon Slayer finished?",
             "No - the manga completed its story, and the anime continues through the "
             "final arcs; check current listings for where the adaptation stands."),
            ("Is it good for younger viewers?",
             "Older kids and teens - the demons and violence are real, though the series "
             "is famously sincere rather than cruel."),
            ("Do I start with the series or the film?",
             "With season one - the record-breaking film lands mid-story and means nothing "
             "without it."),
        ],
    },
    "howls-moving-castle": {
        "verdict": "Miyazaki's anti-war fairytale on legs: a hatmaker cursed into old age, "
            "a wizard who is mostly birds, and a castle that struts across meadows "
            "screaming with steam. Gorgeous, gentle, and stranger than its reputation - "
            "Sophie's quiet courage is one of animation's great protagonists.",
        "faqs": [
            ("Is Howl's Moving Castle based on a book?",
             "Yes - Diana Wynne Jones's 1986 novel; Miyazaki keeps the premise and takes "
             "his own flight path with the war storyline."),
            ("Do the Ghibli films need watching in order?",
             "No - every film stands alone; this one pairs nicely with any rainy Sunday."),
            ("How long is it?",
             "119 minutes."),
        ],
    },
    "grave-fireflies": {
        "verdict": "The saddest film ever made, by common consent: two orphans scavenging "
            "through the firebombed end of the Second World War, drawn with tenderness "
            "and absolute honesty by Isao Takahata. Everyone should see it once; nobody "
            "watches it twice lightly. Bring tissues, then sit quietly afterwards.",
        "faqs": [
            ("Is Grave of the Fireflies based on a true story?",
             "It adapts Akiyuki Nosaka's semi-autobiographical short story - his own "
             "experience of losing his sister in wartime Japan."),
            ("Why is it paired with My Neighbour Totoro?",
             "They were released together in 1988 as a double bill - light and shadow "
             "from the same studio, a programming choice still discussed today."),
            ("Is it suitable for children?",
             "Mature children and up - the war's effects on children are its whole "
             "subject; most viewers say teens and older."),
        ],
    },
    "cowboy-bebop": {
        "verdict": "The coolest anime ever aired: bounty hunters drifting between jazz "
            "clubs and gunfights, tragedies nipping their heels. Twenty-six episodes of "
            "genre-hopping style - noir, western, comedy - welded to a story about "
            "runaways and the past that collects. See you, space cowboy.",
        "faqs": [
            ("Do I need to like anime to enjoy Cowboy Bebop?",
             "No - it converts newcomers constantly; the jazz, the P.I. melancholy and "
             "the episode-of-the-week freedom play like a great American TV series drawn "
             "in ink."),
            ("What order should I watch it in?",
             "Broadcast order, roughly episode one onwards - the standalone adventures "
             "slowly braid into the backstory."),
            ("Is the Netflix live-action version worth it?",
             "Fans largely prefer the animated original - it remains the definitive form."),
        ],
    },
    "drishyam": {
        "verdict": "The original that launched a thousand remakes: a Malayalam family man "
            "with a cinema addiction commits the perfect cover-up to protect his daughter, "
            "and Jeethu Joseph plays every move like chess while the police close in. "
            "Razor-tight, humane, and one of Indian cinema's cleverest thrillers.",
        "faqs": [
            ("Is Drishyam the Malayalam original?",
             "Yes - this is the 2013 Malayalam film with Mohanlal; its celebrated 2015 "
             "Hindi remake with Ajay Devgn follows it closely, and both have sequels."),
            ("What does 'Drishyam' mean?",
             "Visuals or scenery - a nod to the hero's cinephilia, which becomes the "
             "mechanism of his alibi."),
            ("How long is it?",
             "160 minutes of escalating pressure."),
        ],
    },
    "gangs-of-wasseypur": {
        "verdict": "Anurag Kashyap's generational gangster epic - coal-mine feuds, "
            "elections, Bollywood quotes and betrayal across two families and five hours "
            "of anarchic energy. Vulgar, hilarious, savage and ceaselessly alive: the "
            "Indian crime saga that rewrote what mainstream Indian film could say.",
        "faqs": [
            ("Is Gangs of Wasseypur one film or two?",
             "Two parts, released weeks apart in 2012, together telling one story across "
             "generations - Part One sets the feud, Part Two collects every debt."),
            ("Is it based on real events?",
             "It fictionalises the real gang wars of the Wasseypur area of Dhanbad, "
             "compressing decades of coal-mafia history into family saga."),
            ("How long is it?",
             "About 160 minutes per part - clear a weekend; it is a world, not a film."),
        ],
    },
    "game-of-thrones": {
        "verdict": "The phenomenon that redefined what TV could be - and then taught the "
            "world's biggest lesson in how to end one. Seasons one to four remain "
            "all-time television: politics, dragons, and nobody safe. The later descent "
            "is real; the mountain it fell from is still worth climbing.",
        "faqs": [
            ("Is Game of Thrones worth starting despite the ending?",
             "Most veterans say yes - the early seasons are among TV's finest, and the "
             "show's cultural references run through everything. Go in knowing the final "
             "season divides everyone."),
            ("Is it based on books?",
             "On George R. R. Martin's A Song of Ice and Fire; the show outpaced the "
             "unfinished novels around its final seasons."),
            ("How long is it?",
             "Eight seasons, 73 episodes - a genuine commitment, and a rite of passage."),
        ],
    },
    "chernobyl": {
        "verdict": "Five hours of dread, done perfectly: the 1986 nuclear disaster played "
            "as a horror story about lies - what it costs to lie, and what it costs to "
            "hear the truth. Jared Harris anchors, the rooftop scenes burn in memory, "
            "and 'what is the cost of lies?' is the century's best cold open. Haunting "
            "and essential.",
        "faqs": [
            ("Is Chernobyl a true story?",
             "It dramatises the real 1986 disaster and cleanup, compressed and "
             "dramatised in places (the visible open-air radiation burns are an artistic "
             "heightening) - the substance is documented history."),
            ("Do I need to understand nuclear physics?",
             "No - the show explains exactly as much as you need, through characters "
             "demanding the same answers you would."),
            ("How long is it?",
             "Five episodes of about an hour. Watch it slowly; it lingers."),
        ],
    },
    "the-wire": {
        "verdict": "Television's great novel: a city - Baltimore - examined one "
            "institution at a time, from the drug war up through the docks, city hall, "
            "schools and press. Slow, patient, furious and ultimately the most complete "
            "picture American TV ever painted. The first season hooks; the whole thing "
            "changes how you see streets you have never walked.",
        "faqs": [
            ("Why do people say The Wire is the best show ever?",
             "Because it treats a whole city as its protagonist - every season widens "
             "the lens, and the writing trusts you with systems, not heroes. Its rate of "
             "all-time lists speaks for itself."),
            ("Do the seasons connect?",
             "Yes - one continuing story across five seasons, each focused on a "
             "different institution. Watch in order, give it three episodes to grip."),
            ("How long is it?",
             "Sixty episodes, about an hour each - the most rewarding long commitment "
             "in the crime genre."),
        ],
    },
    "the-host": {
        "verdict": "Bong Joon-ho's monster movie with a family of losers at its heart: "
            "a creature from the Han River, a snack-bar owner's daughter taken, and the "
            "most dysfunctional rescue squad ever assembled. Scares, satire and tears "
            "in one seamless package - proof monster films can be about something and "
            "still be thrill rides.",
        "faqs": [
            ("Is The Host based on a true story?",
             "Its premise satirises a real incident - a Seoul mortuary dumping formaldehyde "
             "into the Han River - while the creature itself is pure invention."),
            ("Is it scary or funny?",
             "Both, expertly - the monster attacks are genuinely frightening and the "
             "family comedy keeps breaking in. That tonal blend is Bong's signature."),
            ("How long is it?",
             "119 minutes."),
        ],
    },
    # ---- film batch 10 (2026-09-24): 30 titles - family animation, action staples, smart sci-fi ----
    "shrek": {
        "verdict": "The fairy tale that mocked fairy tales and outlived them all: an ogre, "
            "a talking donkey and a screenplay with something for every age in the room. "
            "Mike Myers' accent alone is a comedy instrument. Two decades of sequels and "
            "memes later, the original's jokes still land - which is more than the "
            "fairy-tales it skewered can say.",
        "faqs": [
            ("Is Shrek based on a book?",
             "Loosely on William Steig's 1990 picture book Shrek! - the film keeps the "
             "grumpy ogre and invents nearly everything else, including the entire tone."),
            ("Did Shrek win an Oscar?",
             "Yes - the first ever Best Animated Feature at the 2002 ceremony, beating "
             "both Monsters, Inc. and Pixar's own hopes that year."),
            ("Is it suitable for young kids?",
             "Yes, with a few innuendos aimed over their heads - the joke design is "
             "two-tier by intent."),
        ],
    },
    "finding-nemo": {
        "verdict": "Pixar's ocean-crossing masterpiece: one clownfish father crossing an "
            "ocean, one forgettable fish holding the whole film together, and an opening "
            "ten minutes that still ambush parents everywhere. Gorgeous, funny and "
            "quietly about letting go - the studio near its untouchable peak.",
        "faqs": [
            ("Did Finding Nemo win the Oscar?",
             "Yes - Best Animated Feature at the 2004 ceremony, Pixar's second win in "
             "the category's history."),
            ("Is the sequel needed?",
             "Finding Dory (2016) is a warm continuation centred on Dory - the original "
             "stands perfectly alone."),
            ("Is the opening too sad for kids?",
             "It is the famous warning: the first minutes involve loss, handled directly. "
             "Most families survive it and treasure the film forever after."),
        ],
    },
    "the-incredibles": {
        "verdict": "The superhero film that out-thought the genre by making it a midlife "
            "crisis: a family of powers in witness protection, dying of normality. Brad "
            "Bird's action choreography still sings, and underneath the gags is a real "
            "argument about talent, purpose and family dinner. Cake, and who deserves it.",
        "faqs": [
            ("Is The Incredibles a Pixar film about Marvel-style heroes?",
             "Original characters - not Marvel - though it lovingly riffs on the entire "
             "superhero tradition while telling its own story."),
            ("Did it win the Oscar?",
             "Yes - Best Animated Feature at the 2005 ceremony, plus Sound Editing."),
            ("Is the sequel worth watching?",
             "Incredibles 2 (2018) is a strong continuation - the original remains the "
             "entry point and the classic."),
        ],
    },
    "ratatouille": {
        "verdict": "The food film for people who think with their hearts: a rat with a "
            "chef's soul pilots a garbage boy through Paris kitchens, and the result is "
            "Pixar's most grown-up pleasure - about taste, critics and who is allowed "
            "to create. The final-act food flashback remains an all-timer of pure cinema.",
        "faqs": [
            ("Did Ratatouille win an Oscar?",
             "Yes - Best Animated Feature at the 2008 ceremony."),
            ("Is it based on a book?",
             "No - an original screenplay; Parisian kitchens and chef culture were "
             "researched extensively for it."),
            ("What is 'Anyone can cook' really about?",
             "The film's whole thesis: talent comes from unexpected places, and the "
             "critic's job is to recognise it - a defence of artists disguised as a "
             "comedy about a rat."),
        ],
    },
    "frozen": {
        "verdict": "The snowstorm that swallowed pop culture: two sisters, one ice curse, "
            "and 'Let It Go' redrawing the Disney princess playbook. Underneath the "
            "phenomenon is a genuinely subversive story - true love turns out not to be "
            "the kind songs promised. Kids wore it out; parents secretly admired the craft.",
        "faqs": [
            ("Did Frozen win Oscars?",
             "Yes - two at the 2014 ceremony: Best Animated Feature and Best Original "
             "Song for 'Let It Go'."),
            ("Is Frozen based on a fairy tale?",
             "Loosely on Hans Christian Andersen's The Snow Queen - the sister story is "
             "Disney's own invention."),
            ("Is the sequel worth it?",
             "Frozen II (2019) goes bigger and stranger - a worthy continuation once "
             "the first has done its work."),
        ],
    },
    "tangled": {
        "verdict": "The Rapunzel film that quietly reignited Disney's animation: lantern "
            "scene alone justifies the ticket, the chameleon steals every scene he is "
            "in, and the humour has real snap. Arriving between the studio's wilder "
            "experiments, it is the polished crowd-pleaser that set up the modern renaissance.",
        "faqs": [
            ("Is Tangled the same story as Frozen's team?",
             "Different film - but it was the proving ground for the modern Disney "
             "revival that Frozen completed."),
            ("Why was it named Tangled, not Rapunzel?",
             "A marketing pivot away from 'princess' branding of that era - and a joke "
             "the film itself acknowledges."),
            ("How long is it?",
             "100 minutes."),
        ],
    },
    "encanto": {
        "verdict": "The family-magic musical that turned 'We Don't Talk About Bruno' into "
            "a household weather system: a Colombian family where every gift matters "
            "except the one girl without one. Generational-pressure themes wrapped in "
            "Lin-Manuel Miranda's earworms - and the loudest kitchen sing-along of the decade.",
        "faqs": [
            ("Did Encanto win an Oscar?",
             "Yes - Best Animated Feature at the 2022 ceremony."),
            ("What is the song everyone knows?",
             "'We Don't Talk About Bruno' - it reached number one on the Billboard Hot "
             "100, a first for a Disney song in decades."),
            ("What is the gift metaphor about?",
             "Family roles, inherited expectations and the pressure of being 'the gifted "
             "one' - the film's core is about being valued for existing, not achieving."),
        ],
    },
    "wicked": {
        "verdict": "The stage phenomenon finally on film, and the staging is the point: "
            "Oz before Dorothy, told through the green girl and the golden one. Erivo "
            "and Grande sing the roof off, Jon Chu shoots spectacle like a musical "
            "lover, and 'Defying Gravity' earns its place in the sky. Part one of two - "
            "plan accordingly.",
        "faqs": [
            ("Do I need to know The Wizard of Oz or the stage show?",
             "Neither - the film assumes Oz's outline and rebuilds everything else; "
             "stage fans get the bonus of hearing the score done full-orchestra."),
            ("Is it the whole musical?",
             "No - it adapts Act One of the stage show; Part Two completes the story "
             "the following year."),
            ("How long is it?",
             "160 minutes, Interval included."),
        ],
    },
    "titanic": {
        "verdict": "The blockbuster that married spectacle to melodrama and ruled the "
            "world: James Cameron's ship, Leonardo's gaze, and a love story placed "
            "directly in the path of history. Long, swooning, technically astonishing - "
            "and the ending debate has fuelled dinner tables for decades. The last "
            "great old-school epic.",
        "faqs": [
            ("Did Titanic win Best Picture?",
             "Yes - eleven Academy Awards at the 1998 ceremony, tying the all-time record, "
             "including Best Director for Cameron."),
            ("Is the door scene physically accurate?",
             "The film says the space fit one; the internet has run the buoyancy maths "
             "ever since. Cameron has weighed in repeatedly - the debate is the legacy."),
            ("How long is it?",
             "195 minutes - an event, then and now."),
        ],
    },
    "gladiator-ii": {
        "verdict": "Ridley Scott returns to the arena sixteen years later: Rome under "
            "twin corrupt emperors, a young hero with Maximus's old anger, and set "
            "pieces - rhino included - built at full imperial scale. Not the original's "
            "thunder, but a proper Roman epic with DenzelWashington relishing every "
            "venal minute.",
        "faqs": [
            ("Do I need to see Gladiator (2000) first?",
             "It helps deeply - the sequel's whole meaning runs on what the first film "
             "built and buried."),
            ("Who does Denzel Washington play?",
             "Macrinus, a former-slave-turned-powerbroker who owns gladiators and plays "
             "Rome's long game - the film's most watchable predator."),
            ("How long is it?",
             "148 minutes."),
        ],
    },
    "mad-max": {
        "verdict": "The scrappy 1979 original that started a myth: an Australian highway "
            "cop, a chrome gang, and the birth of George Miller's wasteland. Rougher and "
            "smaller than Fury Road - and fascinating precisely because you can watch "
            "the whole legend hatch here.",
        "faqs": [
            ("Do I need to watch Mad Max before Fury Road?",
             "No - Fury Road stands alone. But the original is where the vocabulary "
             "(the Interceptor, the recklessness) was invented."),
            ("Why does the dub sound odd to some viewers?",
             "The original Australian voices were partly redubbed with American accents "
             "for early international releases - modern releases restore the original track."),
            ("How long is it?",
             "A lean 88 minutes."),
        ],
    },
    "die-hard-2": {
        "verdict": "The sequels-before-sequels-were-cool entry: same cop, worse night, "
            "an airport seized on Christmas Eve. It cannot match the tower's claustrophobia, "
            "but the snowmobile chase and the runway fire landing keep the franchise "
            "honest. Solid Yippee-ki-yay continuation, no more, no less.",
        "faqs": [
            ("Do I need to see the first Die Hard?",
             "Yes - the whole premise leans on John McClane's luck being legendary and "
             "his marriage being on the line."),
            ("Is it as good as the original?",
             "It trades the tower's intimacy for scale - most fans rank it below the "
             "first and third films, above what follows."),
            ("How long is it?",
             "124 minutes."),
        ],
    },
    "speed": {
        "verdict": "The purest high-concept thriller of the nineties: a bomb on a bus, "
            "armed at fifty miles per hour, and a cop with a bad knee riding shotgun. "
            "Jan de Bont stages gridlock as opera; Reeves and Bullock generate real "
            "chemistry at illegal velocities. The elevator prelude alone outclasses "
            "most whole films.",
        "faqs": [
            ("What is the premise of Speed?",
             "A bomber rigs a city bus to explode if it drops below 50 mph - and a "
             "young LAPD officer has to keep it flying through LA traffic."),
            ("Is there a sequel?",
             "Yes - Speed 2: Cruise Control (1997), famously without Reeves and famously "
             "not needed; the original is complete."),
            ("How long is it?",
             "116 minutes, most of it at speed."),
        ],
    },
    "the-fugitive": {
        "verdict": "The gold standard of the wrong-man thriller: a surgeon framed for his "
            "wife's murder, a marshal who will not quit, and a dam-jump that defined "
            "nineties cinema. Tommy Lee Jones' dry pursuit earned an Oscar; the film "
            "still plays like a watched kettle. Efficiency as entertainment.",
        "faqs": [
            ("Is The Fugitive based on a series?",
             "On the 1960s TV series with David Janssen, itself echoing classic wrong-man "
             "stories - the film version became the definitive one."),
            ("Did anyone win Oscars?",
             "Tommy Lee Jones won Best Supporting Actor at the 1994 ceremony; the film "
             "was nominated for Best Picture."),
            ("How long is it?",
             "130 minutes, without a wasted beat."),
        ],
    },
    "total-recall": {
        "verdict": "Verhoeven's Martian mind-bender: Schwarzenegger, implanted memories, "
            "and three tits' worth of proper sci-fi sleaze. Is any of it real? The film "
            "refuses to say, the action never pauses long enough to care, and the "
            "practical effects still embarrass the remake. Big, dumb and secretly clever.",
        "faqs": [
            ("Is Total Recall based on a book?",
             "On Philip K. Dick's short story 'We Can Remember It for You Wholesale' - "
             "the memory-implant premise is pure Dick."),
            ("Is the dream interpretation ever settled?",
             "No - the film plants evidence both ways on purpose; every viewer picks a "
             "side and defends it forever."),
            ("How long is it?",
             "113 minutes."),
        ],
    },
    "robocop": {
        "verdict": "The satire hiding inside the action figure: a murdered cop rebuilt "
            "as product, a Detroit owned by corporations, and Verhoeven smuggling "
            "genuine tragedy into the violence. Funnier and angrier than its reputation "
            "suggests - the media breaks are still razor-sharp. One of the eighties' "
            "smartest films in dumb clothing.",
        "faqs": [
            ("Is RoboCop a satire?",
             "Completely - corporate capture, privatised policing and TV desensitisation "
             "are the real subjects; the shootouts are the sugar."),
            ("How violent is it?",
             "Extremely - the unrated reputation is earned; the original cut was initially "
             "refused certification in several territories."),
            ("How long is it?",
             "102 minutes."),
        ],
    },
    "taken": {
        "verdict": "The film that gave cinema its most quoted phone call and Liam Neeson "
            "a second career: ninety minutes of driven, economical father-rage through "
            "Paris. The trafficking backdrop is handled with action-movie simplicity - "
            "this is a revenge machine, not a documentary, and as one it purrs.",
        "faqs": [
            ("What is the famous line?",
             "'I will find you and I will kill you' - the phone speech, delivered with "
             "such calm it became the internet's favourite threat template."),
            ("Are the sequels worth it?",
             "Diminishing returns, honestly - the original's premise closes cleanly; "
             "the follow-ups re-open it for payroll."),
            ("How long is it?",
             "A ruthless 90 minutes."),
        ],
    },
    "john-wick-4": {
        "verdict": "Action cinema at its absolute ceiling: Stahelski conducts gun-fu "
            "through Berlin, Osaka and a sunrise staircase of Parisian doom, with Donnie "
            "Yen as the equal-and-opposite force. Nearly three hours and it earns every "
            "minute - the series' best since the first, and the genre's current champion.",
        "faqs": [
            ("Do I need the earlier John Wick films?",
             "Yes - Chapter 4 collects debts and characters from all three predecessors; "
             "start at the beginning for the dog, stay for the world."),
            ("Is it really that long for an action film?",
             "169 minutes - unusually epic, and paced like three great action films "
             "stitched into one saga."),
            ("Is it the last one?",
             "It closes a chapter emphatically while leaving doors ajar - the franchise "
             "has continued expanding around it."),
        ],
    },
    "the-fifth-element": {
        "verdict": "Luc Besson's operatic space circus: a cab driver, a perfect being, "
            "a villain with a head like a squids daydream, and Chris Tucker at maximum "
            "frequency. Sloppy, sincere and spectacular - the Diva dance sequence alone "
            "is worth the ticket. The most French thing ever to save the universe.",
        "faqs": [
            ("Is The Fifth Element based on a comic?",
             "On stories Besson began inventing as a teenager; the visual design came "
             "from comics artists Moebius and Jean-Claude Mezieres."),
            ("Why do people love it so much?",
             "Total commitment to its own nonsense - the costume design, Gary Oldman's "
             "lisp and the opera scene add up to a film with zero cynicism."),
            ("How long is it?",
             "121 minutes."),
        ],
    },
    "district-9": {
        "verdict": "The alien-arrival film with the nerve to land them over Johannesburg: "
            "mockumentary becomes action tragedy becomes one man's crawl toward decency. "
            "Blomkamp's debut is rough, furious and unforgettable - apartheid allegory "
            "wearing a mech suit. The prawn-pawn wordplay is the least of its cleverness.",
        "faqs": [
            ("Is District 9 based on a true event?",
             "No - but it is built directly on South Africa's real forced-removal history "
             "(District Six, Cape Town), which is the source of its anger."),
            ("Why is it shot like a documentary at first?",
             "The news-crew framing is the satire's delivery system - the film starts as "
             "the media the society deserves, then breaks form as its hero does."),
            ("How long is it?",
             "112 minutes."),
        ],
    },
    "her": {
        "verdict": "The romance about loneliness in the digital age that keeps becoming "
            "more relevant: a letter-writer falls for his operating system, and Spike "
            "Jonze plays it completely straight - tender, specific and quietly "
            "devastating about how we live now. Phoenix and Johanson make the impossible "
            "relationship feel real.",
        "faqs": [
            ("Is Her about AI?",
             "It is about connection - the AI is the vehicle for questions about intimacy, "
             "growth and what happens when a relationship changes at different speeds."),
            ("Did it win an Oscar?",
             "Yes - Best Original Screenplay at the 2014 ceremony."),
            ("Is it sad?",
             "Melancholy rather than bleak - a film about the beautiful, temporary nature "
             "of every connection."),
        ],
    },
    "moon": {
        "verdict": "Duncan Jones' debut is the loneliness mic-drop: one man, a lunar base, "
            "a taciturn robot and a countdown that stops adding up. Rockwell gives a "
            "one-man masterclass; the budget is tiny and the ideas are enormous. The "
            "smart little sci-fi film that launched a director.",
        "faqs": [
            ("Is Moon connected to other films?",
             "It is the first of Jones' self-described universe with Mute - but it stands "
             "perfectly alone."),
            ("Who voices the robot?",
             "Kevin Spacey as GERTY - a deliberately ambiguous machine whose loyalty is "
             "the film's quiet subplot."),
            ("How long is it?",
             "A taut 96 minutes."),
        ],
    },
    "minority-report": {
        "verdict": "Spielberg's fog-drenched precognition thriller: murders stopped before "
            "they happen, until the cop tasked with the system becomes its target. "
            "Peak-era blockbuster ideas - free will, surveillance, the tyranny of "
            "certainty - wrapped in rain-slick chase craft. The touchscreen future it "
            "invented mostly arrived.",
        "faqs": [
            ("Is Minority Report based on a book?",
             "On Philip K. Dick's short story, expanded into a full-throated thriller by "
             "Spielberg and a dream team of futurist consultants."),
            ("How does it hold up as a prediction?",
             "Embarrassingly well - gesture interfaces, personalised advertising and "
             "predictive-policing debates all play out on screen."),
            ("How long is it?",
             "145 minutes."),
        ],
    },
    "iron-man-3": {
        "verdict": "The post-Avengers anxiety attack: Tony Stark, sleepless after New "
            "York, meets a terrorist of pure theatre - and Shane Black directs the "
            "Christmas-set fallout with the series' sharpest wit. The third-act twist "
            "divides fandom forever; the script's smarts are not up for debate.",
        "faqs": [
            ("Why is Iron Man 3 set at Christmas?",
             "Shane Black's signature - the writer-director of Kiss Kiss Bang Bang sets "
             "nearly everything he touches in the festive season, for ironic counterpoint."),
            ("What is the controversial twist?",
             "The Mandarin's true identity reframed the MCU's first real terrorist as "
             "performance - fans still argue whether it is clever or a cheat."),
            ("How long is it?",
             "130 minutes."),
        ],
    },
    "thor": {
        "verdict": "The MCU's Shakespeare pivot: Kenneth Branagh plays the god of thunder "
            "as dynastic family drama - banishment, a brother's envy, and a fish-out-of-"
            "water detour through New Mexico. Hemsworth arrives fully formed, Hiddleston's "
            "Loki becomes an instant all-timer. Wobbly in places, essential for what it seeds.",
        "faqs": [
            ("Do I need Thor before The Avengers?",
             "Yes - it introduces Thor and Loki, whose brother act powers the ensemble "
             "era's first two films."),
            ("Is it fantasy or superhero?",
             "Both by design - Asgard plays as full mythology while Earth plays fish-out-"
             "of-water comedy, and the film alternates by intent."),
            ("How long is it?",
             "114 minutes."),
        ],
    },
    "spider-man-homecoming": {
        "verdict": "The reboot that finally got the age right: a fifteen-year-old Spidey "
            "who is happy, awkward and grounded - with Keaton's Vulture as the franchise's "
            "best-kept villain secret. Small stakes by design, big charm by execution. "
            "The friendly neighbourhood reset the character needed.",
        "faqs": [
            ("How does this Spider-Man connect to the MCU?",
             "It is the Sony-Marvel shared era - Tom Holland's Peter Parker enters having "
             "already fought in Civil War, with Tony Stark as mentor."),
            ("Do I need the earlier Spider-Man films?",
             "No - this is a fresh start that skips the origin story entirely, on purpose."),
            ("How long is it?",
             "133 minutes."),
        ],
    },
    "batman-v-superman-dawn-of-justice": {
        "verdict": "The most divisive superhero film of its decade: Snyder's mythic, "
            "mopey colossus - gods arguing about power while a city pays. Martha saves "
            "it or sinks it depending on your faith, but Affleck's broken Batman and the "
            " sheer ambition of the thing keep it fascinating. A failure worth arguing about.",
        "faqs": [
            ("Do I need Man of Steel first?",
             "Yes - the film is a direct sequel, and its whole argument is about the "
             "consequences of that film's ending."),
            ("What is the 'Martha' moment?",
             "The mothers' shared name that halts the title fight - the internet's "
             "favourite shorthand for the film's operatic logic. Watch it and join the "
             "eternal debate."),
            ("Which cut exists?",
             "The theatrical cut and the longer Ultimate Edition (about 30 minutes more, "
             "coherently violent) - the latter is generally the preferred version."),
        ],
    },
    "godzilla-2014": {
        "verdict": "Gareth Edwards' patience play: a monster film that hides its titans "
            "like horror mysteries until the parachute drop and the stadium reveal pay "
            "off everything. The human story divides viewers; the final harbour "
            "sequence - the atomic breath glow - is pure cinema. The American Godzilla "
            "finally done with awe.",
        "faqs": [
            ("Do I need earlier Godzilla films?",
             "No - this is a fresh American reboot that honours the original's dread-first "
             "philosophy."),
            ("Why is Godzilla off-screen so long?",
             "Deliberate - Edwards rations the monster like a horror villain; those who "
             "want constant kaiju brawling are served better by the sequels."),
            ("How long is it?",
             "123 minutes."),
        ],
    },
    "jurassic-world": {
        "verdict": "The park finally open, and the film knows exactly what that means: "
            "a self-aware blockbuster about the appetite for bigger, louder, more - "
            "starring Pratt, a raptor whisperer, and one very indignant hybrid. Not "
            "Spielberg's wonder; a fun machine with real craft in the paddock scenes.",
        "faqs": [
            ("Do I need the original Jurassic Park films?",
             "It helps - the sequel runs on nostalgia for the 1993 original and literally "
             "revisits its locations."),
            ("Is the Indominus rex the point?",
             "Yes - a dinosaur designed by marketing committee, which is the film's whole "
             "joke about its own existence."),
            ("How long is it?",
             "124 minutes."),
        ],
    },
    "kingsman-the-secret-service": {
        "verdict": "Vaughn's tailor-shop spy romp: a chav done good, amentor with an "
            "umbrella, and action choreography so clean the church sequence became "
            "legendary - and controversial. Rude, funny, impeccably tailored; a Bond "
            "film that read Bond's manual and decided to enjoy itself.",
        "faqs": [
            ("Is Kingsman a parody of Bond?",
             "A loving remix - it riffs on every spy convention while staging action "
             "sequences most Bond films would envy."),
            ("How violent is it?",
             "Very, and stylishly so - the church sequence is the famous one; the film "
             "is R-rated throughout by choice."),
            ("How long is it?",
             "129 minutes."),
        ],
    },
    # ---- film batch 11 (2026-09-24): 30 titles - cult classics, mega-TV, anime, world cinema ----
    "clockwork-orange": {
        "verdict": "Kubrick's most dangerous film: Beethoven, bowler hats and ultraviolence "
            "as ballet, wrapped around a question societies still avoid - what is it worth "
            "to cure a monster by turning him into a machine? Fifty-plus years on it "
            "remains electric, repulsive and impossible to shake. Not for everyone; "
            "unavoidable for cinema.",
        "faqs": [
            ("Why was A Clockwork Orange banned in the UK?",
             "It was not officially banned - Kubrick himself withdrew it from British "
             "release after death threats and copycat-crime moral panic, and it stayed "
             "unavailable there until after his death."),
            ("What is the strange slang?",
             "Nadsat - an invented teen dialect mixing Russian and English, from Anthony "
             "Burgess's novel; it makes you complicit in learning the violence's language."),
            ("How long is it?",
             "136 minutes."),
        ],
    },
    "full-metal-jacket": {
        "verdict": "Kubrick's Vietnam, in two half-films that make one great whole: a drill "
            "sergeant who rebuilds men into killers, then the war itself as absurd, "
            "claustrophobic geometry. The boot-camp hour is the most quoted acting "
            "showcase ever filmed; the Hue City scenes are the quietest horror in the "
            "war genre. The duality of man, indeed.",
        "faqs": [
            ("Is the drill sergeant real?",
             "R. Lee Ermey was a real Marine drill instructor hired as advisor who talked "
             "his way into the role - his improvised insults earned a Golden Globe "
             "nomination."),
            ("Why does the film feel like two movies?",
             "Deliberate - boot camp dehumanises, Vietnam institutionalises; the structure "
             "mirrors the soldier's journey from one machine-room to another."),
            ("How long is it?",
             "116 minutes."),
        ],
    },
    "the-truman-show": {
        "verdict": "The gentlest dystopia ever filmed: a man discovers his entire life is "
            "a television set, and Jim Carrey plays the awakening with heartbreaking "
            "sincerity. Prescient about surveillance and reality TV before either "
            "swallowed the world - and somehow still sunny about the human need to walk "
            "through the exit. 'In case I don't see you...'",
        "faqs": [
            ("Was The Truman Show ahead of its time?",
             "Famously so - written in the mid-nineties, it anticipated reality TV, "
             "livestreamed lives and curated identity; academics coined 'Truman Show "
             "delusion' after it."),
            ("Is it a comedy or a drama?",
             "Both, in perfect balance - Carrey's comic timing sells the set-up while "
             "the story lands as sincere drama about free will."),
            ("How long is it?",
             "99 minutes."),
        ],
    },
    "the-princess-bride": {
        "verdict": "The swashbuckling fairy tale that perfected the form by making fun of "
            "it: fencing, revenge, giants, miracles and true love, all delivered with "
            "quote-perfect wit. Thirty-nine years of endearment, half a century of "
            "quotability - 'inconceivable' - and still the ultimate family film that "
            "adults love more. As you wish.",
        "faqs": [
            ("Is The Princess Bride a kids' film?",
             "Yes and no by design - William Goldman's script plays fairy tale for "
             "children and satire for adults, which is why it never ages."),
            ("Is it based on a book?",
             "On Goldman's own 1973 novel - he adapted it himself, keeping the "
             "grandfather-frame and the best lines."),
            ("How long is it?",
             "98 minutes."),
        ],
    },
    "do-the-right-thing": {
        "verdict": "Spike Lee's hottest day and sharpest film: one block in Bed-Stuy, one "
            "pizzeria, and pressure that builds all day toward a night everyone will "
            "argue about forever. Vibrant, funny, furious and still the clearest lens "
            "on American racial politics cinema has produced. The heat you feel is the "
            "point.",
        "faqs": [
            ("Is Do the Right Thing based on true events?",
             "It is fiction, but drawn from real tensions - the 1986 Howard Beach attack "
             "and years of Brooklyn racial incidents feed its background."),
            ("Who does 'the right thing' refer to?",
             "The film deliberately refuses to say - every character's choice is "
             "defensible and damning, which is why debates outlived the century."),
            ("Is it considered a classic?",
             "Fully - it competed at Cannes, earned an Original Screenplay Oscar "
             "nomination, and joined the US National Film Registry in 1999."),
        ],
    },
    "the-iron-giant": {
        "verdict": "The great box-office failure that became a sacred text: a boy, a "
            "giant metal alien, and a Cold War parable about choosing what you are "
            "instead of what you are built for. Brad Bird's debut is gorgeous, funny "
            "and armed with one of animation's great endings. 'Superman.' Bring "
            "tissues, again.",
        "faqs": [
            ("Why was The Iron Giant a flop?",
             "1999 release with almost no marketing support - Warner Bros barely opened "
             "it; reputation rebuilt it over home video and TV into a beloved classic."),
            ("Is it based on a book?",
             "Loosely on Ted Hughes's 1968 children's novel The Iron Man - the Cold War "
             "setting and gun-metal design are the film's own."),
            ("How long is it?",
             "86 minutes."),
        ],
    },
    "top-gun-1986": {
        "verdict": "Tony Scott's sunlight-and-jetfuel adrenaline machine: sunglasses, "
            "beach volleyball, and F-14s screamed into myth by the greatest fighter-pilot "
            "photography ever shot. The plot is a delivery system for speed - and 'Take "
            "My Breath Away' did the rest. Thirty-six years later the sequel proved the "
            "myth still had altitude.",
        "faqs": [
            ("Did Top Gun win an Oscar?",
             "Yes - 'Take My Breath Away' won Best Original Song at the 1987 ceremony."),
            ("Do I need it before Maverick (2022)?",
             "Strongly - Maverick is a direct sequel that runs on the original's "
             "relationships and ghosts; watch the 1986 film first."),
            ("How long is it?",
             "105 minutes."),
        ],
    },
    "drive": {
        "verdict": "The coolest film of the 2010s: Gosling's stunt driver says almost "
            "nothing, the synth score does the talking, and Refn shoots LA at night "
            "like a neon sacrament - then detonates violence you do not see coming. "
            "Slow-burn romance, elevator carnage, an icon born. 'A real hero.'",
        "faqs": [
            ("Is Drive a quiet film?",
             "Famously - long silences, synthwave soundtrack, sparse dialogue; the "
             "violence erupts in short shocking bursts. The rhythm is the aesthetic."),
            ("Is it based on a book?",
             "On James Sallis's 2005 novel; Refn kept the driver's laconic code and "
             "reimagined the rest."),
            ("How long is it?",
             "100 minutes."),
        ],
    },
    "the-notebook": {
        "verdict": "The weepie that defined the genre for a generation: a summer romance, "
            "a class divide, and a devotion that outlasts memory itself. Gosling and "
            "McAdams' chemistry - stormy on and off screen - makes the old-fashioned "
            "machinery genuinely move. Cynics arrive, sobers Leave. It works.",
        "faqs": [
            ("Is The Notebook based on a book?",
             "On Nicholas Sparks's 1996 debut novel - his first and still his most "
             "beloved adaptation."),
            ("Why is the rain scene famous?",
             "The dock reunion in the storm became the romance blueprint of the 2000s - "
             "and the couple's real-life off-screen relationship added legend to it."),
            ("How long is it?",
             "123 minutes."),
        ],
    },
    "bourne-identity": {
        "verdict": "The spy thriller that rewired the genre: a man fished from the sea "
            "with amnesia, deadly skills and no name, hunted across Europe while "
            "reassembling himself. Doug Liman's grounded, handheld kineticism plus "
            "Damon's wounded intelligence killed the martini era overnight. The "
            "blueprint every action franchise studied after.",
        "faqs": [
            ("Is The Bourne Identity based on a book?",
             "On Robert Ludlum's 1980 novel - the film keeps the amnesiac-assassin core "
             "and updates the Cold War frame to post-9/11 Europe."),
            ("Do the sequels keep the quality?",
             "The next two (Supremacy, Ultimatum, with Paul Greengrass) are widely rated "
             "equal or better - the trilogy is complete at three; later entries vary."),
            ("How long is it?",
             "119 minutes."),
        ],
    },
    "the-rock": {
        "verdict": "Michael Bay's best film, by wide consent: a chemical-weapons siege of "
            "Alcatraz, Sean Connery having the time of his life as a captured spy, "
            "Nicolas Cage twitching brilliantly through the flames. Peaks of pure "
            "nineties action craft - the car chase, the shower-room ambush - and a "
            "buddy chemistry for the ages. A spectacle with a soul.",
        "faqs": [
            ("Is The Rock based on a true story?",
             "No - the conspiracy backstory (Connery's imprisoned agent) is pure "
             "invention, though Alcatraz's real history is woven in lovingly."),
            ("Why is Connery's character in The Rock so iconic?",
             "A lifetime-British-legend playing an American secret forgotten in prison - "
             "the film treats him as the most dangerous man alive, and he plays it as "
             "pure amusement."),
            ("How long is it?",
             "127 minutes."),
        ],
    },
    "die-hard-3": {
        "verdict": "The franchise's comeback: Simon says, and New York pays - a "
            "phone-book bomber forces McClane and a foul-mouthed shop owner (Samuel L. "
            "Jackson) through riddles across the city. McTiernan returns and finds the "
            "first film's wit again; the taxi chase and the aqueduct run are top-drawer "
            "McClane. The best of the sequels, many say.",
        "faqs": [
            ("Do I need the first two Die Hard films?",
             "Yes - the villain is direct revenge for the first film's events, and the "
             "revelation lands best if you know it."),
            ("Why is it called With a Vengeance?",
             "Because it is - Simon Gruber's entire game is payback for the tower, "
             "delivered as a city-sized riddle."),
            ("How long is it?",
             "128 minutes."),
        ],
    },
    "x-men-days-of-future-past": {
        "verdict": "The X-Men's high-water mark: a dark future, a mind sent into the past, "
            "and two generations of mutants in one film - Stewart and McKellen with "
            "McAvoy and Fassbender, Wolverine bridging them. Big ideas, big set pieces, "
            "Quicksilver's kitchen scene alone rewrote superhero cinema. The saga's "
            "best since X2.",
        "faqs": [
            ("Do I need to see the earlier X-Men films first?",
             "Ideally X-Men (2000), X2 and First Class - the time-travel premise pays "
             "off decades of continuity."),
            ("What is the Rogue Cut?",
             "An extended version restoring Rogue's deleted storyline (about 17 minutes "
             "more) - fans debate which cut is better; the theatrical version is the "
             "standard edit."),
            ("How long is it?",
             "131 minutes theatrically."),
        ],
    },
    "up": {
        "verdict": "Pixar's most lopsided masterpiece: four minutes of married life that "
            "reduce whole cinemas to tears, then a house flown by balloons into an "
            "adventure about grief, patience and saying yes to life again. Dug the dog "
            "is perfect, the principals are perfect, the craft is Pixar at full power. "
            "Adventure is out there - so is this.",
        "faqs": [
            ("Did Up win the Oscar?",
             "Yes - Best Animated Feature and Best Original Score at the 2010 ceremony, "
             "plus nominations including Best Picture."),
            ("Is the opening too sad for children?",
             "The Carl-and-Ellie montage is the famous tearjerker; children feel it and "
             "understand it - most families call it essential, not excessive."),
            ("How long is it?",
             "96 minutes."),
        ],
    },
    "coraline": {
        "verdict": "The stop-motion door to the other mother: Henry Selick turns Neil "
            "Gaiman's novella into handmade nightmare - button eyes, a too-perfect "
            "mirror world and dread stitched into every frame. Gorgeous, creepy and "
            "courageous enough to trust children with real fear. The cult classic that "
            "keeps finding new generations.",
        "faqs": [
            ("Is Coraline too scary for kids?",
             "For very young ones, yes - it is a genuine nightmare vehicle; for older "
             "children it is a rite of passage, beloved by the brave."),
            ("Is it based on a book?",
             "On Neil Gaiman's 2002 novella, adapted by director Henry Selick (The "
             "Nightmare Before Christmas)."),
            ("Is there a sequel?",
             "No sequel exists - Gaiman has resisted direct continuations; the film "
             "stands as a complete world."),
        ],
    },
    "castle-in-sky": {
        "verdict": "The film that launched Studio Ghibli: Miyazaki's sky-pirate adventure "
            "of a floating castle, a crystal pendant and two kids outpacing an entire "
            "armada. Pure adventure with Ghibli's gentleness underneath - robots, "
            "clouds and a final ten minutes of pure wonder. Where the whole studio's "
            "magic began.",
        "faqs": [
            ("Is Castle in the Sky a Ghibli film?",
             "Yes - the studio's very first release (1986), which makes its quality all "
             "the more remarkable."),
            ("Is it connected to other Miyazaki films?",
             "No - completely standalone; the shared DNA is tone and wonder, not story."),
            ("How long is it?",
             "124 minutes."),
        ],
    },
    "the-wild-robot": {
        "verdict": "The 2024 surprise that melted everyone: a shipwrecked service robot "
            "adopts a gosling on a wild island, and DreamWorks paints it in gorgeous "
            "storybook brushstrokes. Funny, tender and genuinely wise about "
            "parenthood - 'kindness can be a survival skill'. The rare modern family "
            "film adults recommend to each other.",
        "faqs": [
            ("Is The Wild Robot based on a book?",
             "On Peter Brown's 2016 illustrated novel - the film keeps the Roz-Brightbill "
             "heart and adds a fuller island cast."),
            ("Did it win the Oscar?",
             "It was nominated for Best Animated Feature at the 2025 ceremony (Flow took "
             "the award) - and won hearts regardless."),
            ("How long is it?",
             "102 minutes."),
        ],
    },
    "friends": {
        "verdict": "The comfort-watch colossus: six twenty-somethings in Greenwich Village, "
            "a coffee house, and ten seasons of will-they-won't-they that became the "
            "shared language of sitcoms. The jokes are furniture in half the world's "
            "homes - 'PIVOT', 'we were on a break' - and the warmth has not leaked out "
            "of the episodes yet. Streaming's great re-discovery.",
        "faqs": [
            ("Is Friends still worth watching?",
             "Its numbers say yes - decades after it ended it remains one of the most "
             "watched series on streaming, and new viewers keep adopting it."),
            ("How many seasons are there?",
             "Ten seasons, 236 episodes, airing 1994 to 2004 - plus the 2021 reunion "
             "special where the cast returned as themselves."),
            ("Do I start at season one?",
             "Yes - it is an ensemble sitcom built to be watched in order, and the "
             "relationships only compound."),
        ],
    },
    "better-call-saul": {
        "verdict": "The prequel that outgrew its source: Jimmy McGill's slow, tragic "
            "slouch toward becoming Saul Goodman, told with Breaking Bad's precision "
            "and a heartbreak all its own. Bob Odenkirk and Rhea Seehorn give the "
            "prestige-TV decade its finest performances. The rare spin-off that "
            "argues - successfully - it was the point all along.",
        "faqs": [
            ("Do I need Breaking Bad first?",
             "Strongly recommended - it is a direct prequel, and every shadow (Gus, the "
             "cartel, Mike's line of work) lands harder for knowing where it leads."),
            ("How many seasons?",
             "Six seasons, 2015 to 2022, widely acclaimed as one of the best-reviewed "
             "dramas of its era."),
            ("Is it as violent as Breaking Bad?",
             "It is quieter and more legal-drama-driven early on - the tension is "
             "moral rather than explosive, until it isn't."),
        ],
    },
    "black-mirror": {
        "verdict": "The anthology that watches us back: standalone near-futures where "
            "technology strips a little more humanity away, each episode a fresh "
            "glass pane cracking. Uneven by nature, occasionally masterpiece ('San "
            "Junipero', 'White Christmas') and always conversation-starting. The "
            "sci-fi mirror of its decade.",
        "faqs": [
            ("Do Black Mirror episodes connect?",
             "Mostly standalone by design - tiny Easter eggs and shared brands wink "
             "across episodes, but you can watch any single one cold."),
            ("Which episode should I start with?",
             "Fan consensus starts newcomers on 'San Junipero' (warm) or 'Fifteen "
             "Million Merits' (dark) depending on taste - anthology means no wrong door."),
            ("Is it all bleak?",
             "Predominantly cautionary, with celebrated exceptions - 'San Junipero' is "
             "the famous happy one."),
        ],
    },
    "dark": {
        "verdict": "The German time-twister that out-Netflixed everything: four families, "
            "one missing child, and a cave that folds 1953, 1986, 2019 and beyond into "
            "a single knot. Demanding, meticulously plotted and visually stunning - "
            "the rare puzzle-box that actually solves. Pay attention; it rewards you "
            "like nothing else.",
        "faqs": [
            ("Is Dark hard to follow?",
             "Gloriously yes - four time periods and four families; watch with the "
             "show's own family-tree diagram handy and never on a phone screen."),
            ("Is Dark subtitled or dubbed?",
             "It is a German production - subtitled viewing is the widely preferred way; "
             "dubs exist including English."),
            ("How many seasons?",
             "Three seasons, 2017 to 2020, ending on a planned, complete conclusion."),
        ],
    },
    "the-sopranos": {
        "verdict": "The big bang of prestige television: a New Jersey mob boss with "
            "panic attacks walks into a therapist's office, and TV grows up. James "
            "Gandolfini's performance remains the medium's gold standard - tender, "
            "monstrous, human. Twenty-five years of great drama live in its shadow. "
            "Woke up this morning, got yourself a show.",
        "faqs": [
            ("Does The Sopranos hold up today?",
             "Overwhelmingly - critics regularly rank it the greatest TV series ever "
             "made, and the family-psychology core has not aged a day."),
            ("What about the famous ending?",
             "The cut-to-black at Holsten's divided the planet in 2007 and still "
             "generates essays - intentionally ambiguous, defended by its own creator."),
            ("How many seasons?",
             "Six seasons, 86 episodes, 1999 to 2007."),
        ],
    },
    "dragon-ball-z": {
        "verdict": "The series that globalised shonen: Saiyan invasions, namekian legends, "
            "screaming power-ups and friendships forged in orbital combat. Nearly 300 "
            "episodes of escalating spectacle that raised a generation on four "
            "continents. Slow by modern pacing, monumental by influence - the bedrock "
            "of anime's worldwide era.",
        "faqs": [
            ("Do I watch Dragon Ball before DBZ?",
             "Ideally - the original series establishes Goku's childhood and friends; "
             "DBZ starts with him grown. Many jump straight in and backfill later."),
            ("Why is DBZ so slow?",
             "The anime was produced against an ongoing manga, stretching moments into "
             "episodes - the Kai recut condenses it significantly if pacing frustrates."),
            ("How long is it?",
             "291 episodes across roughly a decade of airing - a marathon, and a "
             "foundational one."),
        ],
    },
    "frieren": {
        "verdict": "The fantasy anime about after the adventure: an elf mage who outlived "
            "her party sets out to understand the humans she loved too late. Gentle, "
            "gorgeous and quietly devastating about time, memory and small kindnesses "
            "- it became one of the highest-rated series of its decade almost "
            "overnight. For everyone who ever finished something and felt the silence.",
        "faqs": [
            ("Why is Frieren rated so highly?",
             "It trades shonen combat-rush for reflection - critics and audiences "
             "placed it among the highest-rated anime ever within a year of airing."),
            ("Do I need fantasy anime experience?",
             "None - it assumes nothing and teaches its world as it goes; newcomers "
             "and veterans both start at episode one."),
            ("How long is it?",
             "Season one ran 28 episodes, with the story continuing in new seasons."),
        ],
    },
    "chainsaw-man": {
        "verdict": "Devils born from fear, a boy with a chainsaw for a heart, and MAPPA "
            "giving the whole thing cinematic grime and glory. Denji's starved, honest "
            "desires make him shonen's most human protagonist; the tone swings from "
            "stupid-funny to soul-crushing without warning. The most exciting new-gen "
            "series of its moment.",
        "faqs": [
            ("Is Chainsaw Man finished?",
             "No - the manga continues its second part, and the anime adapts onward; "
             "the 2025 Reze film continues the story cinematically."),
            ("Is it as violent as people say?",
             "Yes - gore is the genre furniture, but the real shock is how much "
             "feeling hides under the blood."),
            ("Where should I start?",
             "Season one, in order - the Reze arc lands after it."),
        ],
    },
    "the-handmaiden": {
        "verdict": "Park Chan-wook's erotic con-artist masterpiece: 1930s Korea under "
            "Japanese rule, a pickpocket hired as a maid, and a plot that turns over "
            "on itself three times with opulent, wicked grace. Sumptuous, transgressive "
            "and perfectly constructed - the twists are the jewellery. Adults only, "
            "and worth every minute.",
        "faqs": [
            ("Is The Handmaiden based on a book?",
             "On Sarah Waters's Victorian novel Fingersmith, transplanted to "
             "Japanese-occupied Korea - a relocation that gives it its own politics "
             "and texture."),
            ("Why is it rated so highly?",
             "It swept critics' lists on release, won the BAFTA for best film not in "
             "the English language, and is widely called Park's most complete film."),
            ("How long is it?",
             "145 minutes."),
        ],
    },
    "the-wailing": {
        "verdict": "Na Hong-jin's six-year build of pure dread: a village sickness, a "
            "policeman whose family falls ill, and a shaman's ritual that may save or "
            "damn them. Two and a half hours of escalating, unexplainable horror - "
            "the most debated ending in Korean cinema. Not a scare machine; a "
            "haunting.",
        "faqs": [
            ("Is The Wailing scarier than typical Korean horror?",
             "It trades jump-scares for accumulating dread - most viewers call it one "
             "of the most unsettling films of its decade rather than a gorefest."),
            ("Does the ending explain everything?",
             "No - it is famously debated; theories flourish precisely because the "
             "film withholds a final verdict."),
            ("How long is it?",
             "156 minutes."),
        ],
    },
    "baahubali-2": {
        "verdict": "Rajamouli's mythic answer to cinema's biggest 'why': how Kattappa killed "
            "Baahubali - and the revelation detonates exactly as the nation demanded. "
            "Larger-than-life battles, impossible stunts, a mother's oath and a "
            "coronation: Indian myth-making at full scale, and among the highest-"
            "grossing Indian films ever made. See part one first; then this rewards "
            "everything.",
        "faqs": [
            ("Do I need Baahubali: The Beginning first?",
             "Absolutely - part two is the second half of one story, and its power is "
             "answering part one's cliffhanger."),
            ("Why is 'Why did Kattappa kill Baahubali' so famous?",
             "The first film ended on that single unanswered question and an entire "
             "country spent two years theorising - a genuine national conversation."),
            ("How long is it?",
             "167 minutes of spectacle."),
        ],
    },
    "bajrangi-bhaijaan": {
        "verdict": "The Salman Khan film with a soul the size of a subcontinent: a "
            "devout simpleton smuggles a mute Pakistani girl home across the border, "
            "and the road movie becomes a case for human decency over every division "
            "on the map. Funny, shamelessly moving and carried by the little girl's "
            "silence. The feel-good giant of modern Bollywood.",
        "faqs": [
            ("Is Bajrangi Bhaijaan based on a true story?",
             "No - it is fiction, though it channels real India-Pakistan border "
             "tragedies and custody cases that give it its charge."),
            ("Why is it called Bhaijaan?",
             "'Bhaijaan' is Salman Khan's real-world nickname and his character's "
             "honorific - the film is built entirely around his persona's warmth."),
            ("How long is it?",
             "159 minutes."),
        ],
    },
    "93-days": {
        "verdict": "The true story of when Lagos stopped an epidemic: Patrick Sawyer "
            "lands at Murtala Muhammed carrying Ebola, and the doctors, nurses and "
            "officials of First Consultant Hospital hold the line for the ninety-three "
            "days that kept Nigeria safe. Tense, respectful and rooted in real "
            "sacrifice - Nigerian thriller craft serving a genuinely important memory.",
        "faqs": [
            ("Is 93 Days based on a true story?",
             "Yes - the real 2014 Ebola emergency in Lagos, when the virus arrived via "
             "an infected traveller and was contained by contact-tracing and the staff "
             "who paid the highest price."),
            ("Where is it set?",
             "Lagos, Nigeria - largely at the real First Consultant Hospital in Obalende, "
             "the outbreak's ground zero."),
            ("How long is it?",
             "118 minutes."),
        ],
    },
    # ---- film batch 12 (2026-09-24): 30 titles - TV giants, MCU backfill, horror landmarks, world cinema ----
    "the-office-us": {
        "verdict": "The mundane miracle of American sitcom: a paper company in Scranton, "
            "filmed like a documentary, staffed by the most uncomfortably lovable idiots "
            "on television. Carell's Michael Scott is a tragedy of needing to be loved, "
            "Jim-and-Pam is the slow burn by which all slow burns are judged, and the "
            "rewatch economy it built may be unmatched. Nothing happens; everything lands.",
        "faqs": [
            ("Is the US Office based on the UK one?",
             "Yes - it adapts Ricky Gervais and Stephen Merchant's British original, then "
             "finds its own voice by season two and never looks back."),
            ("How many seasons?",
             "Nine seasons, 2005 to 2013 - Steve Carell leads the first seven, and the "
             "ensemble carries it home."),
            ("Is it still worth watching?",
             "It remains one of the most rewatched shows on streaming - a comfort-watch "
             "default for two decades of viewers, which answers the question empirically."),
        ],
    },
    "downton-abbey": {
        "verdict": "The upstairs-downstairs colossus: a Yorkshire estate, an heir problem, "
            "and a servants' hall full of schemes, all conducted with Julian Fellowes' "
            "impeachable manners. Maggie Smith's Dowager alone justifies the admission "
            "fee. It soothed a decade of audiences on two continents and spun off into "
            "films - comfort television at its most exportable.",
        "faqs": [
            ("Do I need to watch Downton Abbey in order?",
             "Yes - it is one long serial story across six seasons (2010-2015), and the "
             "payoffs depend on the long game."),
            ("Is it historically accurate?",
             "It is meticulous about period texture (electricity, telephones, a world war) "
             "while being open fiction - accuracy of feel more than of event."),
            ("Are the films worth it after the series?",
             "They continue the story properly - made for devotees, and devotees are "
             "consistently rewarded."),
        ],
    },
    "vikings": {
        "verdict": "The saga that made raiders philosophers: Ragnar Lothbrok's climb from "
            "farmer to legend, and then his sons' wars over the wreckage. Michael "
            "Hirst's writing gives the Norse world weight - faith, fate and farm - and "
            "Lagertha remains one of TV's great warriors. Rougher and more soulful than "
            "its spectacle reputation suggests.",
        "faqs": [
            ("Is Vikings historically accurate?",
             "It weaves real figures (Ragnar, his sons, the raids on Lindisfarne and "
             "Paris) into legend - the texture is researched, the events are drama."),
            ("How many seasons?",
             "Six, airing 2013 to 2020, with the sequel series Vikings: Valhalla "
             "continuing the world a century later."),
            ("Do I watch Valhalla first?",
             "No - the original first; Valhalla assumes its history."),
        ],
    },
    "the-walking-dead": {
        "verdict": "The zombie drama that proved the walkers were never the point: "
            "eleven seasons of survivors learning that people are the apocalypse. The "
            "early seasons are genre-defining television; the long middle tests "
            "loyalty; the character payoffs (hello, Negan) still generate heat. A "
            "universe-builder whose influence on TV horror is total.",
        "faqs": [
            ("Is The Walking Dead based on a comic?",
             "Yes - Robert Kirkman's black-and-white comic series; the show follows it "
             "lovingly at first, then diverges freely."),
            ("How many seasons?",
             "Eleven, 2010 to 2022, 177 episodes - plus a small universe of spin-offs "
             "for favourite survivors."),
            ("When can I stop watching?",
             "The honest fan answer: season six is the classic peak - but the finale "
             "still rewards those who stay the course."),
        ],
    },
    "the-witcher": {
        "verdict": "Sword-and-sorcery with a grumpy heart: Geralt of Rivia, monster-for-hire, "
            "bound by destiny to a runaway princess and a bard who won't stop singing. "
            "Cavill's two seasons of weary charisma and one unforgettable 'Toss a Coin' "
            "made it a phenomenon. Messy timelines, generous monsters, and a recast "
            "that keeps the conversation alive.",
        "faqs": [
            ("Is The Witcher based on games or books?",
             "The books - Andrzej Sapkowski's Polish short stories and novels; the "
             "games came later and the series draws from the page."),
            ("Why is there a new Geralt?",
             "Henry Cavill departed after season three; Liam Hemsworth took over the "
             "medallion from the next season - one of TV's most debated recasts."),
            ("Do I need to have played the games?",
             "No - the story is built from the books and explains its own world."),
        ],
    },
    "wednesday": {
        "verdict": "The Addams daughter gets her noir: Jenna Ortega's deadpan Wednesday "
            "investigates a monster at Nevermore Academy, Tim Burton directs with "
            "gothic glee, and one viral dance later the show was a record-setting "
            "phenomenon. Wry, spooky-sweet, and built to binge - the rare family "
            "gothic that satisfies teens and their parents at once.",
        "faqs": [
            ("Do I need to know The Addams Family?",
             "No - Wednesday spins its own mystery-school story; knowing the family "
             "adds seasoning, not requirements."),
            ("Is it coming back?",
             "Yes - the second season arrived in 2025, keeping Ortega's deadpan and "
             "adding star turns."),
            ("Is it scary?",
             "Mildly and stylishly - monsters and mystery more than dread; younger "
             "teens are the sweet spot."),
        ],
    },
    "yellowjackets": {
        "verdict": "Lord of the Flies with a paper trail: a championship soccer team "
            "survives a plane crash in 1996 - and the show cuts between the wilderness "
            "and the damaged adults they became. Cannibalism lurks, cults bloom, and "
            "the dual-timeline structure never blinks. The best pure mystery-box on "
            "television, anchored by fearless performances.",
        "faqs": [
            ("Is Yellowjackets based on a true story?",
             "No - it echoes real survival-at-any-cost cases (the Andes flight disaster "
             "most famously) but its team, cult and cover-ups are invention."),
            ("How scary is it?",
             "Psychologically very - the horror is what people choose, not what hunts "
             "them; gore is present and purposeful."),
            ("Do the mysteries get answered?",
             "Slowly and deliberately - each season widens the 1996 timeline; patience "
             "is part of the pact."),
        ],
    },
    "captain-america": {
        "verdict": "The MCU's earnest heart, wearing stars and stripes in 1942: a "
            "skinny kid from Brooklyn gets the super-soldier serum and proves the "
            "serum was the least of it. Joe Johnston plays it as a wartime adventure "
            "poster come to life - Red Skull, Hydra, and a sacrifice that defines the "
            "man before the franchise redefines time itself.",
        "faqs": [
            ("Do I watch this before The Avengers?",
             "Yes - it introduces Steve Rogers and sets up both his sacrifice and the "
             "Tesseract plot that threads the early MCU."),
            ("Is the skinny-Steve effect real acting?",
             "Partly digital shrinking, partly Chris Evans' motion - groundbreaking "
             "for its time and still convincing."),
            ("How long is it?",
             "124 minutes."),
        ],
    },
    "doctor-strange": {
        "verdict": "The MCU hires a sorcerer: Cumberbatch's arrogant surgeon loses the "
            "use of his hands and finds the multiverse instead. The kaleidoscope city-"
            "folding third act is the franchise's most purely psychedelic set piece, "
            "and 'Dormammu, I've come to bargain' remains its cleverest beat. The "
            "gateway to everything magical that followed.",
        "faqs": [
            ("Do I need Doctor Strange before Infinity War?",
             "Yes - his Time Stone and his foresight are load-bearing for the entire "
             "Infinity Saga climax."),
            ("Is it based on a comic?",
             "On Steve Ditko and Stan Lee's 1963 creation - the eye, the cloak and the "
             "sanctums all predate the film by fifty years."),
            ("How long is it?",
             "115 minutes."),
        ],
    },
    "black-widow": {
        "verdict": "Natasha Romanoff's belated solo send-off: a Cold War family "
            "reunion in which the Red Room's ghosts are literal. Johansson hands the "
            "baton gracefully to Florence Pugh's Yelena (an instant fan favourite), "
            "the Taskmaster concept divides, and the heart - chosen family over "
            "programmed loyalty - lands. A finale by way of a handover.",
        "faqs": [
            ("When is Black Widow set in the MCU timeline?",
             "Between Civil War and Infinity War - after Natasha's fall-out with Tony, "
             "before Thanos looms."),
            ("Do I need to have seen the Avengers films?",
             "Yes - it is a coda to a decade of Natasha, and the grief lands only if "
             "you know her arc."),
            ("How long is it?",
             "133 minutes."),
        ],
    },
    "the-flash": {
        "verdict": "The multiverse movie as cautionary tale: Barry Allen runs back time "
            "to save his mother and breaks the DC multiverse open - Keaton's Batman "
            "returns to general jubilation, and the film's reach wildly exceeds its "
            "effects. A fascinating, flawed swing that became the era's most discussed "
            "underperformance. Ambition, caught mid-stumble.",
        "faqs": [
            ("Do I need other DC films before The Flash?",
             "No - it resets its own context; familiarity with the 1989 Batman adds "
             "the biggest emotional charge."),
            ("Why was it so talked about?",
             "A combination: Keaton's return, the multiverse cameos, visual-effect "
             "debates and a box-office collapse that reshaped DC's plans."),
            ("How long is it?",
             "144 minutes."),
        ],
    },
    "the-penguin": {
        "verdict": "The crime saga hiding inside a comic-book spin-off: Colin Farrell, "
            "unrecognisable in prosthetics, climbs Gotham's underworld one betrayal at "
            "a time in the wake of The Batman. Cristin Milioti's Sofia is the "
            "revelation, the tone is pure seventies gangster drama, and the "
            "performances collected awards attention everywhere. Prestige TV in "
            "villain clothing.",
        "faqs": [
            ("Do I need The Batman (2022) first?",
             "Yes - it is a direct continuation of that film's flood-wrecked Gotham, "
             "and its power depends on the setup."),
            ("Is it a superhero show?",
             "Not really - it is a gangster series set in a comic universe; expect "
             "crime politics, not capes."),
            ("How many episodes?",
             "Eight - a tight limited-series arc that feeds directly into the next "
             "Batman film."),
        ],
    },
    "the-ring": {
        "verdict": "The film that cursed a generation's VCRs: a videotape that kills in "
            "seven days, a reporter descending into its mystery, and Gore Verbinski's "
            "rain-slick, sepia dread remaking Japan's Ringu for the West. The "
            "television crawl remains one of horror's greatest reveals. The gateway "
            "drug of the entire J-horror remake wave.",
        "faqs": [
            ("Is The Ring based on a Japanese film?",
             "Yes - Hideo Nakata's 1998 Ringu, itself from Koji Suzuki's novel; the "
             "remake honours the mythology while re-staging it in the Pacific Northwest."),
            ("How scary is it really?",
             "Dread-first and image-led rather than gory - but the imagery is permanent: "
             "this is the film people cite as their formative scare."),
            ("How long is it?",
             "116 minutes."),
        ],
    },
    "the-witch": {
        "verdict": "Robert Eggers' debut is a Puritan nightmare played straight: a 1630s "
            "family exiled to the wood's edge, and the devil arrives as a goat, a "
            "raven and a smile. Anya Taylor-Joy erupts into cinema; the period "
            "language and candlelight are so exact the film feels excavated. Horror "
            "as history lesson - 'Wouldst thou like to live deliciously?'",
        "faqs": [
            ("Is The Witch historically accurate?",
             "Obsessively - Eggers built the dialogue from period pamphlets and "
             "recorded folk belief, making the horror a documentary of superstition."),
            ("Why is it so slow?",
             "The dread is cumulative by design - a family disintegrating long before "
             "the supernatural confirmations; patience is repaid."),
            ("How long is it?",
             "92 minutes."),
        ],
    },
    "us": {
        "verdict": "Jordan Peele's doppelganger nightmare: a family's beach day "
            "interrupted by their own taped-mouth doubles, and a national reckoning "
            "in red jumpsuits. Lupita Nyong'o gives two career performances in one "
            "film; the imagery (scissors, rabbits, Hands Across America) is "
            "engineered for years of decoding. Horror with ideas and box office to "
            "spare.",
        "faqs": [
            ("Is Us a sequel to Get Out?",
             "No - Peele framed it as a new nightmare in the same social-horror spirit; "
             "the connections are thematic, not plot."),
            ("What is the twist about?",
             "The reveal reframes the whole film as an argument about the underclass "
             "America forgot - interpretations abound, which is the design."),
            ("How long is it?",
             "112 minutes."),
        ],
    },
    "the-lighthouse": {
        "verdict": "Two men, one lamp, total madness: Eggers' black-and-white, "
            "tobacco-stained fever dream strands Pattinson and Dafoe on a storm-bound "
            "rock and lets the mermaids and gin do the rest. Dafoe's seaman's "
            "confession is a monologue for the ages. A film that smells like a "
            "barrel - and a critics' darling precisely because of it.",
        "faqs": [
            ("Is The Lighthouse a horror film?",
             "Partly - it is psychological isolation horror wrapped in black comedy; "
             "the scares are madness and the jokes are bleaker."),
            ("Why is it black and white?",
             "Period immersion and claustrophobia - the old-fashioned 4:3 frame and "
             "monochrome make the lighthouse feel a century older than cinema."),
            ("How long is it?",
             "109 minutes."),
        ],
    },
    "28-years-later": {
        "verdict": "Boyle and Garland return to the rage virus with the boldest zombie "
            "film in decades: a boy's first mainland trip becomes a pilgrimage through "
            "a Britain gone feral - part horror, part folk elegy, shot largely on "
            "iPhone and riotously alive. Ralph Fiennes' bone-temple cult gives the "
            "genre a line it has never had before. A trilogy opener with teeth.",
        "faqs": [
            ("Do I need the earlier 28 films first?",
             "28 Days Later helps enormously - it establishes the rage virus; 28 Weeks "
             "Later is optional context."),
            ("Is it connected to the 2026 sequel?",
             "Yes - The Bone Temple continues the story as the next part of a planned "
             "trilogy."),
            ("Is it really shot on iPhone?",
             "Largely, yes - Boyle used iPhone rigs for its raw, jagged intimacy; you "
             "would never guess the budget from the frame."),
        ],
    },
    "the-hangover": {
        "verdict": "The night nobody can remember, made unforgettable: a Vegas bachelor "
            "party, a missing groom, a baby in a closet and a tiger in the bathroom. "
            "Todd Phillips structures the film as a detective story told in "
            "hangover-emerging fragments, and it became one of the highest-grossing "
            "comedies of its era. The wolfpack at full howl.",
        "faqs": [
            ("Is The Hangover appropriate for kids?",
             "No - hard R throughout; the chaos is adult in every sense."),
            ("Are the sequels worth it?",
             "Part two repeats the formula scene-for-scene (some love it); part three "
             "changes genre entirely. The first is the classic."),
            ("How long is it?",
             "100 minutes."),
        ],
    },
    "bridesmaids": {
        "verdict": "The wedding comedy that smuggled in a real study of friendship and "
            "self-sabotage: Kristen Wiig's maid of honour unravels against Rose "
            "Byrne's perfect rival, and the airplane and dress-fitting scenes became "
            "instant comedy landmarks. Melissa McCarthy earned an Oscar nomination "
            "from it. Funnier and sadder than its genre promised.",
        "faqs": [
            ("Did Bridesmaids get Oscar attention?",
             "Yes - Melissa McCarthy was nominated for Best Supporting Actress at the "
             "2012 ceremony, a rare comedy turn to break through."),
            ("Is it more comedy or drama?",
             "It pivots honestly to drama in the middle - the baking-scene breakdown "
             "is the film's real centre."),
            ("How long is it?",
             "125 minutes."),
        ],
    },
    "the-nice-guys": {
        "verdict": "Shane Black's sunshine-noir valentine: a heav-for-hire (Crowe) and "
            "a hapless PI (Gosling, doing peak comic panic) stumble through 1977 Los "
            "Angeles, missing persons and porn-industry rot. Nobody saw it in "
            "cinemas; everyone who did quotes it forever. The great cult buddy "
            "detective film of its decade.",
        "faqs": [
            ("Why did The Nice Guys flop?",
             "Crowded summer release and marketing that never found its tone - the "
             "audience found it on home video and streaming instead."),
            ("Is it connected to Kiss Kiss Bang Bang?",
             "Same writer-director's voice - private eyes, Los Angeles, rapid-fire "
             "banter - but a separate story."),
            ("How long is it?",
             "116 minutes."),
        ],
    },
    "tokyo-story": {
        "verdict": "The quietest masterpiece in cinema: an elderly couple travel to "
            "Tokyo to visit their grown children, and are lovingly neglected. Ozu's "
            "low camera and patient frames find the whole of life in politeness and "
            "its failures - and in 2022 the world's film directors poll ranked it "
            "among the greatest films ever made. Everyone should sit with it once; "
            "many never recover.",
        "faqs": [
            ("Why do filmmakers revere Tokyo Story?",
             "Its restraint is the summit - no camera moves, no music cues, and yet "
             "it devastates; directors in the Sight and Sound 2022 poll placed it at "
             "the very top."),
            ("Is it slow?",
             "It is patient, not slow - 136 minutes that pass like an evening; the "
             "final act lands like weather."),
            ("Do I need subtitles knowledge of Japan?",
             "None - the family story is universal; the setting is specific and the "
             "grief is everyone's."),
        ],
    },
    "drive-my-car": {
        "verdict": "Three hours of grief, theatre and red Saab therapy: a stage "
            "director stages Chekhov while a quiet chauffeur drives him toward the "
            "truth about his marriage. Hamaguchi turns Murakami's short story into a "
            "meditation on talking as survival - and won the Oscar for Adapted "
            "Screenplay plus Best International Feature. Long, quiet, and somehow "
            "over before you want it to be.",
        "faqs": [
            ("Is Drive My Car based on a book?",
             "On Haruki Murakami's short story - Hamaguchi expands it into a full "
             "Chekhov-inflected drama."),
            ("Did it win Oscars?",
             "Two at the 2022 ceremony - Best Adapted Screenplay and Best "
             "International Feature, alongside a Best Picture nomination."),
            ("Is the three-hour runtime worth it?",
             "It plays far shorter than its length - and the multilingual final play "
             "justifies every minute."),
        ],
    },
    "the-intouchables": {
        "verdict": "The French phenomenon built on a true friendship: a wealthy "
            "quadriplegic aristocrat hires a caregiver from the projects, and the "
            "film rides their banter from blunt honesty to genuine tenderness. "
            "Omar Sy's star turn won the César and launched him international. "
            "Sentimental? Enormously. Effective? One of the most-watched French "
            "films anywhere, ever.",
        "faqs": [
            ("Is The Intouchables a true story?",
             "Yes - adapted from Philippe Pozzo di Borgo's real friendship with his "
             "carer Abdel Sellou; both consulted on the film."),
            ("Why was it so popular worldwide?",
             "Universal comedy of opposites - it crossed borders on word of mouth and "
             "became a fixture of international 'favourite films' lists."),
            ("Is there an American remake?",
             "Yes - The Upside (2017) with Bryan Cranston and Kevin Hart; the original "
             "remains the preferred version for most viewers."),
        ],
    },
    "a-bittersweet-life": {
        "verdict": "Kim Jee-woon's crystalline gangster ballet: a loyal enforcer "
            "commits the one sin his boss cannot forgive - mercy - and the film turns "
            "his punishment into a symmetrical, almost musical revenge piece. Lee "
            "Byung-hun gives Korean noir its coolest, saddest face. Violence as "
            "composition; melancholy as style.",
        "faqs": [
            ("Is A Bittersweet Life based on a book?",
             "No - an original screenplay by Kim Jee-woon, conceived as a fusion of "
             "Korean revenge drama with formal, European art-cinema elegance."),
            ("Why is it a cult favourite?",
             "Its immaculate framing and tragic cool - every shootout is composed like "
             "a painting, and the ending refuses consolation."),
            ("How long is it?",
             "120 minutes."),
        ],
    },
    "vikram": {
        "verdict": "Lokesh Kanagaraj hands Tamil cinema its adrenaline shot: a masked "
            "vigilante cell, an alcoholic investigator (Fahadh Faasil, gloriously "
            "unhinged) and Kamal Haasan returning to the title role he made iconic "
            "in 1986 - all colliding in a sprawling, twist-heavy crime universe. "
            "Relentless set pieces, fan-service done right, one of Tamil cinema's "
            "biggest hits.",
        "faqs": [
            ("Is Vikram connected to other films?",
             "Yes - it anchors Lokesh's shared universe, directly tied to Kaithi, with "
             "the threads continuing in later films."),
            ("Do I need to know the 1986 Vikram?",
             "No - the title and star are the homage; this is a fresh story built for "
             "newcomers too."),
            ("How long is it?",
             "174 minutes of chase."),
        ],
    },
    "uri": {
        "verdict": "The Indian war film that became a phenomenon: dramatising the 2016 "
            "surgical strikes after the Uri attack, with Vicky Kaushal's major "
            "leading a covert operation across the Line of Control. Taut military "
            "craft, a country's collective emotion in the audience, and a catchphrase "
            "('How's the josh?') that escaped the cinema entirely. Kaushal won the "
            "National Award for it.",
        "faqs": [
            ("Is Uri based on true events?",
             "Yes - it dramatises the real 2016 attack on an Indian army brigade at "
             "Uri and the cross-border strikes India reported days later, with "
             "cinematic liberties."),
            ("Is it propaganda or a film?",
             "It is unambiguously a patriotic action film made from one nation's "
             "perspective - judged best as drama, not documentary."),
            ("How long is it?",
             "138 minutes."),
        ],
    },
    "the-lunchbox": {
        "verdict": "Mumbai's famous dabbawalas deliver a wrong lunchbox, and a lonely "
            "widower and an overlooked wife begin exchanging notes through it. "
            "Irrfan Khan at his gentlest, a romance conducted entirely in food and "
            "handwriting, and an ending that trusts you. Small, perfect, bittersweet "
            "- one of Indian cinema's warmest exports.",
        "faqs": [
            ("Is The Lunchbox a romance?",
             "An epistolary almost-romance - the beauty is in restraint; whether they "
             "ever meet is the film's famous grace note."),
            ("What is a dabba?",
             "A tiffin lunchbox - Mumbai's dabbawala network famously delivers hot "
             "home lunches across the city with near-perfect accuracy; one 'wrong' "
             "delivery starts this story."),
            ("How long is it?",
             "105 minutes."),
        ],
    },
    "vinland-saga": {
        "verdict": "Vikings with a soul in open wound: Thorfinn grows up inside a "
            "revenge quest, gets it, and discovers the emptiness on the other side - "
            "then spends the second season farming his way toward becoming a man "
            "who refuses violence. Rare anime that treats pacifism as the hardest "
            "fight. Brutal first season, transcendent second.",
        "faqs": [
            ("Is Vinland Saga historically based?",
             "It weaves real saga-era figures into fiction - Thorfinn and the "
             "expeditions to Vinland draw on the Norse sagas as Makoto Yukimura "
             "reimagines them."),
            ("Do the two seasons connect?",
             "Yes - one continuing story; the acclaimed second season is the "
             "aftermath that redefines the first."),
            ("Is it very violent?",
             "The first season is full-on Viking warfare; the second trades battle "
             "for moral struggle - the harder watch, in a way."),
        ],
    },
    "weathering-with-you": {
        "verdict": "Shinkai's rain-soaked follow-up to Your Name: a runaway meets a "
            "girl who can summon sunshine, and Tokyo slowly drowns in exchange for "
            "their love. The skies are borderline pornographic in their beauty, "
            "RADWIMPS does the emotional lifting, and the ending chooses the "
            "personal over the planet. Gorgeous weather for feeling things.",
        "faqs": [
            ("Is Weathering with You a sequel to Your Name?",
             "No - a standalone story in the same emotional universe, with sly "
             "connections fans love spotting; watch either order."),
            ("Did it do well in Japan?",
             "Immensely - among Japan's highest-grossing domestic films of its year, "
             "and Japan's awards season favourite."),
            ("How long is it?",
             "112 minutes."),
        ],
    },
    "gangs-of-lagos": {
        "verdict": "Lagos is the main character: a young man raised in Isale Eko's "
            "gang culture wants out, and Osiberu's film gives Nigeria's biggest "
            "city a real crime saga - masquerades, loyalty, inheritance of violence "
            "- shot with blockbuster energy. One of the first Nigerian originals "
            "to stream globally on Prime Video, and a landmark for Nollywood "
            "thrillers reaching the world.",
        "faqs": [
            ("Is Gangs of Lagos based on a true story?",
             "It is fiction rooted in the real lore of Lagos Island - Isale Eko's "
            "street-gang history and Eyo masquerade tradition give the drama its "
            "authentic backdrop."),
            ("Where can the cultural conversation about it be found?",
             "Its release sparked wide Nigerian debate about its portrayal of the "
             "Eyo masquerade - evidence of how closely the film was watched."),
            ("How long is it?",
             "124 minutes."),
        ],
    },
    # ---- film batch 13 (2026-09-24): 30 titles - prestige cinema, K-cinema deep cuts, Oscar winners ----
    "con-air": {
        "verdict": "The nineties action blockbuster at its most gloriously Extra: a "
            "plane full of career psychopaths hijacked mid-transfer, and Nicolas Cage's "
            "just-paroled ranger caught in the middle with his bunny plush. Cusack and "
            "Malkovich chew scenery at 30,000 feet; the crash-landing onto the Strip "
            "is pure spectacle. Dumb as a rock, cut like a diamond.",
        "faqs": [
            ("What is the famous Con Air line?",
             "'Put the bunny back in the box' - Cage's deadpan through-line in a film "
             "built from quotable nonsense."),
            ("Did the theme song get Oscar attention?",
             "Yes - 'How Do I Live' (Trisha Yearwood) was nominated for Best Original "
             "Song at the 1998 ceremony."),
            ("How long is it?",
             "115 minutes."),
        ],
    },
    "face-off": {
        "verdict": "John Woo's apex of beautiful absurdity: an FBI agent and the "
            "terrorist who killed his son surgically swap faces, and Cage and Travolta "
            "proceed to give dual masterclasses in playing each other. Opera, doves, "
            "knife fights and the most committed high-concept acting of the nineties. "
            "Once you accept the face surgery, it is perfect.",
        "faqs": [
            ("Is Face/Off scientifically plausible?",
             "Absolutely not - and the film knows it; the face-swap is a grand opéra "
             "premise, and Woo stages everything else with total sincerity."),
            ("Who is the better impression - Cage or Travolta?",
             "The film's greatest pleasure: both actors study each other and swap "
             "mannerisms mid-film - a genuine double-performance showcase."),
            ("How long is it?",
             "133 minutes."),
        ],
    },
    "the-transporter": {
        "verdict": "The film that made Jason Statham a star: a courier with three rules, "
            "a package that moves, and Corey Yuen staging car chases and warehouse "
            "brawls with French-Lucerne precision. The shirtless hose-fight remains a "
            "genre landmark. Lean, fast, unpretentious - the definitive mid-2000s "
            "action machine.",
        "faqs": [
            ("What are the Transporter's three rules?",
             "Never change the deal, no names, never open the package - the plot exists "
             "to break all three, gloriously."),
            ("Is it connected to Luc Besson?",
             "Yes - Besson co-wrote and produced, pairing his Euro-action polish with "
             "Hong Kong choreography."),
            ("How long is it?",
             "92 minutes."),
        ],
    },
    "equalizer": {
        "verdict": "Denzel Washington's hardware-store terminator: a quiet Home Depot "
            "employee with a very particular set of skills dismantles a Russian mob "
            "one improvised weapon at a time. Fuqua shoots slow-burn dread and "
            "clockwork violence; Denzel makes righteous rage feel almost gentle. The "
            "start of a whole franchise of calm, efficient revenge.",
        "faqs": [
            ("Is The Equalizer based on a TV series?",
             "Yes - the 1980s series with Edward Woodward; the films (and the Queen "
             "Latifah series) all descend from it."),
            ("Is it very violent?",
             "Yes - the finale's hardware-aisle sequence is ingeniously brutal; expect "
             "R-rated precision rather than gore-splatter."),
            ("How long is it?",
             "132 minutes."),
        ],
    },
    "creed": {
        "verdict": "The revival nobody expected to matter this much: Rocky as the "
            "Mickey to a new underdog, Adonis Creed, son of Apollo. Ryan Coogler's "
            "breakout directs the franchise's inheritance themes with genuine fire - "
            "the one-take sparring scene is the series' best-shot sequence. Legacy "
            "sequels, done properly.",
        "faqs": [
            ("Do I need the Rocky films first?",
             "Rocky (1976) is the real prerequisite - the whole film is a conversation "
             "with it; the other sequels are bonus depth."),
            ("Did Stallone win anything for it?",
             "He won the Golden Globe and was Oscar-nominated for Supporting Actor at "
             "the 2016 ceremony - Rocky himself, finally honoured."),
            ("How long is it?",
             "133 minutes."),
        ],
    },
    "crouching-tiger": {
        "verdict": "The wuxia poem that conquered the West: Ang Lee balances gravity-"
            "defying bamboo-top duels with a tragedy of suppressed love and duty. "
            "Michelle Yeoh and Zhang Ziyi give the genre its beating heart; the "
            "fights are choreographed poetry. Four Oscars and the highest-grossing "
            "foreign-language film in American history - and it earned every bit of it.",
        "faqs": [
            ("Did Crouching Tiger win the Oscar?",
             "Yes - Best Foreign Language Film at the 2001 ceremony, plus three more "
             "(cinematography, art direction, score)."),
            ("Is it the first of a story?",
             "It is a standalone adaptation from the Wang Dulu Crane-Iron pentalogy - "
             "later sequels recast parts; this film is complete in itself."),
            ("Why is it so influential?",
             "It carried wire-fu artistry to global audiences and proved subtitled "
             "spectacle could top the American box office."),
        ],
    },
    "crazy-rich-asians": {
        "verdict": "The rom-com event of its decade: a NYU professor discovers her "
            "boyfriend is Singapore's most eligible billionaire heir, and meets the "
            "glittering, scheming family from hell. Constance Wu, Henry Golding and "
            "Michelle Yeoh rule a wedding-set spectacle of mahjong and money - the "
            "first Hollywood studio rom-com with an all-Asian cast in a generation.",
        "faqs": [
            ("Is Crazy Rich Asians based on a book?",
             "On Kevin Kwan's 2013 bestseller, itself drawn from his Singapore "
             "high-society observations."),
            ("Why was its release culturally significant?",
             "It was the first major studio film with an all-Asian lead cast since "
             "The Joy Luck Club in 1993 - and its box-office success reshaped "
             "Hollywood's casting assumptions."),
            ("How long is it?",
             "116 minutes."),
        ],
    },
    "call-me-by-your-name": {
        "verdict": "A northern Italian summer, a scholarly family, and first love "
            "arriving with devastating specificity: Guadagnino's sun-drenched "
            "adaptation plays desire, dread and memory like a season changing. "
            "Chalamet's monologue by the fireplace is the decade's great acting "
            "reveal. Every frame aches beautifully.",
        "faqs": [
            ("Is Call Me by Your Name based on a book?",
             "On André Aciman's 2007 novel, adapted by James Ivory."),
            ("Did it win an Oscar?",
             "Yes - James Ivory won Best Adapted Screenplay at the 2018 ceremony, "
             "becoming the oldest competitive Oscar winner ever."),
            ("Is it explicit?",
             "There is mature content and full-frontal context, but the film's real "
             "intimacy is emotional - longing more than anatomy."),
        ],
    },
    "burning": {
        "verdict": "The murkiest, most hypnotic mystery of its decade: a delivery boy, "
            "a girl who disappears, and a wealthy stranger who burns greenhouses - or "
            "does he? Lee Chang-dong's adaptation of a Murakami short builds unbearable "
            "ambiguity over nearly two and a half hours, and the final ten minutes "
            "detonate like a long-held breath. A film that argues with you afterwards.",
        "faqs": [
            ("Is Burning based on a book?",
             "On Haruki Murakami's short story 'Barn Burning', transplanted to South "
             "Korea and expanded with class-anger themes."),
            ("What actually happens in the ending?",
             "Deliberately unresolved - the film withholds the final fact; every "
             "reading (literal or metaphor) has defenders."),
            ("How long is it?",
             "148 minutes of slow-burn ambiguity."),
        ],
    },
    "decision-to-leave": {
        "verdict": "Park Chan-wook's most tender puzzle: an insomniac detective "
            "investigating a climber's death and falls for the elegant, unreadable "
            "widow - through phone screens, altitudes and a fog of withheld motives. "
            "It won Best Director at Cannes 2022 and plays like a love story told in "
            "police procedure. Exquisite, melancholy, quietly devastating.",
        "faqs": [
            ("Did Decision to Leave win at Cannes?",
             "Yes - Park Chan-wook won Best Director at the 2022 festival."),
            ("Do I need to know Park's earlier films?",
             "No - it is completely standalone, though fans will recognise his "
             "fascination with guilt and desire."),
            ("How long is it?",
             "138 minutes."),
        ],
    },
    "extreme-job": {
        "verdict": "The police-comedy formula perfected: an under-surveillance drug "
            "squad takes over a fried chicken restaurant as a stakeout cover, and the "
            "chicken is so good they become businessmen instead of cops. One of the "
            "highest-grossing Korean comedies ever - and it earns it: escalation "
            "choreography, deadpan Captain Yoo, and a climax that weaponises both "
            "drugs and drumsticks.",
        "faqs": [
            ("Is Extreme Job available with subtitles?",
             "Yes - international releases carry English subtitles; the humour is "
             "physical enough to travel well."),
            ("Why is fried chicken central?",
             "The stakeout cover becomes the squad's accidental second career - the "
             "joke is that they are better entrepreneurs than detectives."),
            ("How long is it?",
             "111 minutes."),
        ],
    },
    "the-man-from-nowhere": {
        "verdict": "Won Bin's pawnshop loner dismantles an entire criminal underworld "
            "for the little girl next door - Korean action's gold standard of the "
            "quiet-man-who-is-death template. Visceral, tightly plotted, and carried "
            "by a genuinely touching bond at its centre. One of the most beloved "
            "Korean thrillers of its era.",
        "faqs": [
            ("Is The Man from Nowhere in English?",
             "No - Korean with subtitles; the sparse dialogue makes it very "
             "subtitle-friendly."),
            ("Is it connected to The Man from Nowhere sequels?",
             "There are no sequels - it is a complete, standalone story."),
            ("How long is it?",
             "119 minutes."),
        ],
    },
    "departures": {
        "verdict": "The Japanese film about death that makes you fall in love with "
            "life: a failed cellist becomes a nokanshi - one who prepares the dead - "
            "and finds dignity, humour and grace in the ritual of farewell. Winner of "
            "the Best Foreign Language Film Oscar at the 2009 ceremony, and one of the "
            "gentlest films ever made about mortality.",
        "faqs": [
            ("Did Departures win the Oscar?",
             "Yes - Best Foreign Language Film at the 2009 ceremony."),
            ("What is a nokanshi?",
             "An encoffiner - a professional who washes and prepares bodies for "
             "cremation with ceremonial care; the film treats the work as an art of "
             "compassion."),
            ("Is it sad?",
             "Profoundly, and consoling at once - most viewers finish it moved rather "
             "than crushed."),
        ],
    },
    "cloud-atlas": {
        "verdict": "The most ambitious novel adaptation of its decade: six stories "
            "across five centuries - composer, journalist, clone, sailor, publisher, "
            "post-apocalyptic shepherd - cut into one another by three directors and "
            "one philosophy: everything is connected. Messy, magnificent, mocked and "
            "beloved; a film that attempts everything cinema can do.",
        "faqs": [
            ("Is Cloud Atlas based on a book?",
             "On David Mitchell's acclaimed 2004 novel, which told the six tales in "
             "mirrored halves; the film interleaves them continuously instead."),
            ("Why do actors play multiple roles?",
             "Recurring actors across timelines embody the film's reincarnation theme - "
             "including some notorious (debated) prosthetic and cross-ethnic casting."),
            ("How long is it?",
             "172 minutes - a true commitment, best watched in one sitting."),
        ],
    },
    "eyes-wide-shut": {
        "verdict": "Kubrick's final dream: Tom and Nicole, a Manhattan Christmas that "
            "never existed, and a masked ritual glimpsed at the edge of the world's "
            "richest city. Shot over a famously record-setting continuous schedule, "
            "it plays like hypnosis - jealousy, desire and class rendered as one long "
            "sleepwalk. The strangest studio film by a giant, and a fitting last riddle.",
        "faqs": [
            ("Is Eyes Wide Shut really Kubrick's last film?",
             "Yes - he finished the edit days before his death in 1999; it premiered "
             "after."),
            ("Why did it take so long to film?",
             "Kubrick's perfectionism produced one of the longest continuous shoots "
             "ever recorded - well over a year of production."),
            ("Is the ritual real or a dream?",
             "The film refuses to say - the whole picture is constructed like a "
             "nocturnal hallucination, ending on 'fuck'."),
        ],
    },
    "the-farewell": {
        "verdict": "A family lies to their grandmother about her terminal diagnosis - "
            "a real Chinese practice the film frames, as its tagline says, 'based on "
            "an actual lie'. Lulu Wang directs with perfect tonal control; Awkwafina "
            "(against type, dramatic) and Zhao Shuzhen anchor the wedding-as-goodbye "
            "structure. Laughing and sobbing in the same scene, guaranteed.",
        "faqs": [
            ("Is The Farewell a true story?",
             "Essentially - Lulu Wang first told it on her podcast; the film's tagline "
             "'based on an actual lie' refers to its real family roots."),
            ("Did Awkwafina win awards for it?",
             "Yes - she won the Golden Globe for Best Actress in a Musical or Comedy "
             "(2020), a landmark for Asian-American performers."),
            ("Why hide a diagnosis from the patient?",
             "The film explores the East-West divide over 'who owns the truth' about "
             "family illness - its central, respectful debate."),
        ],
    },
    "the-florida-project": {
        "verdict": "Childhood at the edge of Disney World: six-year-old Moonee spends "
            "a violet-scented summer in a budget motel while her mother's finances "
            "collapse just off-screen. Sean Baker shoots poverty in candy colours; "
            "Willem Dafoe's motel manager (Oscar-nominated) is one of cinema's great "
            "quiet decent men. The ending will hollow you out kindly.",
        "faqs": [
            ("Why is it called The Florida Project?",
             "Disney World's original construction name - the film lives in its "
             "tourism shadow, in the motels the magic forgot."),
            ("Is it sad?",
             "It is joyful on the surface and devastating underneath - the children "
             "play while the adults quietly fail them."),
            ("How long is it?",
             "115 minutes."),
        ],
    },
    "the-holdovers": {
        "verdict": "A 1970s New England Christmas capsule: a bitter boarding-school "
            "teacher, a brainy troublemaker and a grieving cook hold over the holidays "
            "together. Alexander Payne in monochrome-snow mode; Paul Giamatti is "
            "perfect, Da'Vine Joy Randolph won the Oscar for Supporting Actress. The "
            "warmest scowl in modern cinema - an instant seasonal classic.",
        "faqs": [
            ("Did The Holdovers win an Oscar?",
             "Yes - Da'Vine Joy Randolph won Best Supporting Actress at the 2024 "
             "ceremony; the film was also nominated for Best Picture."),
            ("Is it set in the past?",
             "Yes - deliberately a 1970 film in feel, shot with period titles, grain "
             "and mono-style sound."),
            ("Is it a Christmas film?",
             "Set at Christmas, yes - but its melancholy-warm blend works in any "
             "season."),
        ],
    },
    "the-shape-of-water": {
        "verdict": "Del Toro's fairy tale for the misfits: a mute janitor, an amphibian "
            "god in a government tank, and a love that speaks in eggs, music and "
            "bathtubs flooded with green light. Sally Hawkins performs a whole "
            "soundtrack without a word; the film took Best Picture and Best Director "
            "at the 2018 Oscars. Monster movies, grown tender.",
        "faqs": [
            ("Did The Shape of Water win Best Picture?",
             "Yes - four Oscars at the 2018 ceremony including Best Picture and Best "
             "Director for Guillermo del Toro."),
            ("Is it a Creature from the Black Lagoon remake?",
             "Inspired-by rather than remake - del Toro reframes the gill-man story "
             "as a romance about the hunted outsider."),
            ("Is it suitable for teens?",
             "Older teens - nudity and adult themes; otherwise a gentle, painterly "
             "fantasy."),
        ],
    },
    "the-zone-of-interest": {
        "verdict": "The Holocaust film without a single image of it: the commandant of "
            "Auschwitz and his wife cultivate their garden, their children, their "
            "beautiful domestic life - while beyond the wall, the camp's machinery "
            "hums on the soundtrack. Glazer's formal rigour won the Oscar for "
            "International Feature and upended what cinema can show by refusing to "
            "show it. Unbearable, essential, formally perfect.",
        "faqs": [
            ("Is The Zone of Interest based on a true story?",
             "It dramatises the real household of Auschwitz commandant Rudolf Hoss, "
             "loosely drawing on Martin Amis's novel of the same name - the domestic "
             "detail is the documented horror."),
            ("Why is the camp never shown?",
             "The point exactly - the film keeps the horror at the edge of frame and "
             "sound, indicting the wilful blindness of ordinary life beside atrocity."),
            ("How long is it?",
             "105 minutes that sit very heavy."),
        ],
    },
    "the-substance": {
        "verdict": "Body horror as celebrity-culture autopsy: Demi Moore's fading star "
            "takes a black-market serum that births a younger, better self - and the "
            "sharing arrangement goes operatically, explosively wrong. Margaret "
            "Qualley is heartbreaking, the final act is legendary gross-out, and the "
            "film won the Oscar for its transformative makeup. Rage, jelly and "
            "sequins - Coralie Fargeat's scream.",
        "faqs": [
            ("How extreme is The Substance?",
             "Extremely - the third act is among the most graphic of recent mainstream "
             "horror; it is designed to test the room."),
            ("Did it win the Oscar?",
             "Yes - Best Makeup and Hairstyling at the 2025 ceremony; Demi Moore was "
             "nominated for Best Actress."),
            ("Is it feminist or exploitative?",
             "The debate is the point - it weaponises the male gaze to indict it, and "
             "viewers split on the ethics of the weapon."),
        ],
    },
    "the-menu": {
        "verdict": "Eat the rich, plated course by course: twelve diners arrive at a "
            "celebrity island restaurant, and Ralph Fiennes' chef serves a tasting "
            "menu with murder in the mise en place. Anya Taylor-Joy's cheeseburger "
            "counter-strike is the film's genius move. Wicked, controlled satire with "
            "a correct wine pairing.",
        "faqs": [
            ("Is The Menu a horror film?",
             "Thriller-horror hybrid - dark comedy first, with genuine menace and a "
             "few late jolts."),
            ("What is the cheeseburger scene about?",
             "The film's whole thesis: an uncomplicated comfort food breaks the "
             "haute-cuisine spell - taste as honesty."),
            ("How long is it?",
             "106 minutes, course by course."),
        ],
    },
    "the-green-knight": {
        "verdict": "Arthurian legend as fevered art film: Dev Patel's Sir Gawain "
            "rides into a year-long appointment with his own beheading, through "
            "Lowery's mist, giants, ghosts and mushroom-lit cathedrals. Gorgeous, "
            "patient, strange - a medieval poem reimagined as an odyssey toward "
            "honour. Not for the impatient; transcendent for the willing.",
        "faqs": [
            ("Is The Green Knight based on a poem?",
             "Yes - the 14th-century Middle English 'Sir Gawain and the Green "
             "Knight', one of the great Arthurian romances."),
            ("What does the ending mean?",
             "It offers a vision, a choice, then a final image - widely read as the "
             "moment courage becomes character; interpretations abound."),
            ("How long is it?",
             "130 minutes of pilgrimage."),
        ],
    },
    "the-lives-of-others": {
        "verdict": "The Stasi officer who listens himself human: a surveillance expert "
            "monitors a playwright and his actress lover in 1984 East Berlin, and the "
            "file he writes becomes a confession. Debut-direction perfection; the "
            "Best Foreign Language Film Oscar of 2007; an ending (a single line in a "
            "bookshop) that lands like a lifetime. One of the great films about "
            "conscience.",
        "faqs": [
            ("Did The Lives of Others win the Oscar?",
             "Yes - Best Foreign Language Film at the 2007 ceremony."),
            ("Is it historically accurate?",
             "It compresses history for drama (real Stasi surveillance was even "
             "larger), but the apparatus, fear and compromises are faithfully drawn."),
            ("What is the famous final line?",
             "'It is for me' - the bookshop moment that redeems a career of betrayal; "
             "one of cinema's great quiet endings."),
        ],
    },
    "article-15": {
        "verdict": "Anubhav Sinha's angriest, cleanest film: an idealised IPS officer "
            "arrives in a small town and finds two Dalit girls hanged - and the "
            "caste machinery that explains it. Named for the constitutional article "
            "banning caste discrimination, it made mainstream Hindi cinema say the "
            "quiet parts loudly. Fire, delivered as procedure.",
        "faqs": [
            ("What is Article 15?",
             "The article of India's Constitution that prohibits discrimination on "
             "grounds of religion, race, caste, sex or birthplace - the film's title "
             "and its verdict."),
            ("Is it based on real cases?",
             "It draws on real 2014-2016 incidents of caste violence (including the "
             "Badaun and Una cases), fictionalised into one town."),
            ("How long is it?",
             "130 minutes."),
        ],
    },
    "the-great-indian-kitchen": {
        "verdict": "A marriage, a kitchen, and a slow revolution: a new wife grinds "
            "through endless cooking, cleaning and submission while the men of the "
            "house eat, argue politics and never enter her world. Jeo Baby's Malayalam "
            "phenomenon turned domestic labour into an indictment heard across India - "
            "quiet until it is not, then thunderous.",
        "faqs": [
            ("Why is The Great Indian Kitchen considered important?",
             "It made the invisible labour of the household the entire subject - and "
             "its ending (the woman walking out as sabarimala drums beat) became a "
             "cultural talking point."),
            ("Is it slow?",
             "Deliberately - the repetition IS the argument; the film makes you feel "
             "the days she cannot escape."),
            ("How long is it?",
             "About 100 minutes; a remade Hindi version exists, but the original is "
             "the one that started the conversation."),
        ],
    },
    "the-fall-guy": {
        "verdict": "David Leitch's love letter to stunt people: Ryan Gosling's battered "
            "stuntman is pulled back onto a blockbuster and into a missing-person "
            "mystery, with Blunt supplying the romance and a barfights-and-helicopters "
            "third act supplying the spectacle. Funny, savvy, and genuinely moving "
            "about the unheralded artists who take the hits.",
        "faqs": [
            ("Is The Fall Guy based on a TV series?",
             "Yes - the 1980s series starring Lee Majors, rebooted as a rom-com action "
             "vehicle."),
            ("Did it really showcase real stunts?",
             "Proudly - it broke a Guinness record for cannon rolls in a car and "
             "champions the stunt community throughout."),
            ("How long is it?",
             "126 minutes."),
        ],
    },
    "anora": {
        "verdict": "The year's wildest Best Picture: a Brooklyn sex worker's Cinderella "
            "marriage to a Russian oligarch's son collapses into a blackout-comic "
            "search across Coney Island, with Mikey Madison's Ani refusing to be a "
            "joke. Sean Baker's film swept five Oscars at the 2025 ceremony - picture, "
            "director, actress, screenplay, editing - and its final frame may be the "
            "saddest of the decade.",
        "faqs": [
            ("Did Anora win Best Picture?",
             "Yes - one of five Oscars at the 2025 ceremony (also Director, Actress, "
             "Original Screenplay and Editing)."),
            ("Is it a comedy or a drama?",
             "Both - chaotic screwball energy for two thirds, then a gutting dramatic "
             "slide; the tonal shift is the design."),
            ("How long is it?",
             "139 minutes."),
        ],
    },
    "aftersun": {
        "verdict": "A father-daughter holiday remembered in dying light: karaoke, "
            "calculus and calamari at a Turkish resort, while Sophie's adult memory "
            "reassembles the melancholy her father hid. Charlotte Wells' debut is a "
            "masterclass in what films can leave unsaid; Paul Mescal earned an Oscar "
            "nomination; the LCD-final-act still is cinema's most quietly devastating "
            "dance scene.",
        "faqs": [
            ("Is Aftersun based on a true story?",
             "Wells calls it deeply personal but fiction - built from memories of her "
             "own childhood holidays; the film keeps the autobiography discreet."),
            ("What do the final scenes mean?",
             "The film drifts from memory into imagined, speculative space - the last "
             "sequence is widely read as the daughter's goodbye she never got to give."),
            ("How long is it?",
             "101 minutes."),
        ],
    },
    "the-figurine": {
        "verdict": "The film that announced the New Nollywood: Kunle Afolayan's "
            "supernatural thriller follows two friends who find the Araromire "
            "figurine - seven years of good fortune, then seven of misfortune - and "
            "trade friendship for greed. Yoruba-inflected myth, gorgeous forest "
            "cinematography and genuine dread; a multiple Africa Movie Academy Awards "
            "winner that changed what Nigerian cinema could look like.",
        "faqs": [
            ("Is The Figurine based on Yoruba mythology?",
             "It builds on the lore of Araromire, a goddess-figure whose idol blesses "
             "then curses - an original screenplay rooted in that mythic texture."),
            ("Why is it a Nollywood landmark?",
             "Its cinema-grade production values and awards sweep (Africa Movie "
             "Academy Awards) signalled the New Nollywood wave of prestige Nigerian "
             "features."),
            ("How long is it?",
             "122 minutes."),
        ],
    },
    # ---- film batch 14 (2026-09-24): 30 titles - milestone batch, crosses 50% enriched ----
    "euphoria": {
        "verdict": "High school as Technicolor fever dream: Rue, a teenage addict relapsing "
            "through love and recovery, anchors HBO's most visually intoxicated series. "
            "Zendaya's Emmy-winning work is revelatory and raw, the make-up and "
            "cinematography rewired a generation's aesthetic, and the show's honesty "
            "about drugs, identity and phones keeps it a cultural reference point.",
        "faqs": [
            ("Did Zendaya win awards for Euphoria?",
             "Yes - two Primetime Emmys for Outstanding Lead Actress in a Drama Series "
             "(2020 and 2022), among the youngest winners ever in the category."),
            ("Is Euphoria suitable for teenagers?",
             "It is made about teens, not for them - explicit drug use, nudity and "
             "violence throughout; adults deciding for older teens should preview first."),
            ("Is it based on anything?",
             "On an Israeli series of the same name - the US version transformed it "
             "into its own neon-lit animal."),
        ],
    },
    "gen-v": {
        "verdict": "The Boys goes to college: Godolkin University trains supes for "
            "fame and sponsorships, and the campus rot underneath is exactly as dark "
            "as you would expect. A grisly mystery, a ferocious young cast, and "
            "crossover threads that feed straight into The Boys itself. The spin-off "
            "that earned its compound-V.",
        "faqs": [
            ("Do I need to watch The Boys first?",
             "Strongly - Gen V assumes its world, its satire and its characters; the "
             "events feed directly into later seasons of The Boys."),
            ("Is it as gory as The Boys?",
             "Yes - the hemocraft fights and the finale keep the franchise's "
             "splatter-by-satire standard."),
            ("Is it continuing?",
             "Yes - new seasons continue the story alongside The Boys."),
        ],
    },
    "fallout": {
        "verdict": "The rare video-game adaptation that players and newcomers both "
            "adopted: a vault dweller, a cowboy ghoul and a brotherhood knight cross "
            "a nuclear-blasted America with dark comic joy. Walton Goggins' Ghoul is "
            "an instant icon, the production honours the games' lore religiously, "
            "and the show treats nuclear holocaust with a wink and a shotgun. "
            "Emmy-nominated and renewed - the wasteland is open for business.",
        "faqs": [
            ("Do I need to play the Fallout games first?",
             "No - the show explains its world cleanly; players get extra delight "
             "from the lore treats, newcomers lose nothing essential."),
            ("Is it connected to the games' story?",
             "Yes - it continues the timeline of the games (particularly the "
             "west-coast lore), carefully so."),
            ("How many episodes?",
             "Eight in the first season, hour-long each."),
        ],
    },
    "arcane-season-2": {
        "verdict": "The conclusion of the century's most beautiful show: Piltover and "
            "Zaun go to war, sisters Vi and Jinx collide with the city between them, "
            "and Fortiche's painterly mayhem peaks with battle sequences no live "
            "action could afford. The story lands its ending while the animation "
            "industry simply watches and takes notes. A masterpiece, finished.",
        "faqs": [
            ("Do I need season one first?",
             "Absolutely - season two is the direct second half, and its power runs "
             "on everything season one set up."),
            ("Is it really the final season?",
             "Yes - the story of Vi and Jinx concludes here, though the world of "
             "League of Legends offers more regions for future tales."),
            ("Does the show need game knowledge?",
             "None - it uses the game's characters and city, then tells a complete "
             "story of class, family and sacrifice on its own terms."),
        ],
    },
    "what-we-do-in-shadows": {
        "verdict": "The funniest vampire flat-share ever documented: four immortals in "
            "a Wellington house, filmed mockumentary-style as they argue about "
            "dishes, nightclubs and not transforming in the living room. Clement and "
            "Waititi play it deadpan to perfection, and the gentlest gore jokes "
            "land endlessly. The film that spawned a whole TV dynasty.",
        "faqs": [
            ("Is the film connected to the TV series?",
             "The FX series continues the concept with new vampires in Staten Island, "
             "with cameos from the film's cast - the film is the origin."),
            ("Where is it set?",
             "Wellington, New Zealand - the deadpan local backdrop is half the joke."),
            ("How long is it?",
             "86 minutes."),
        ],
    },
    "dandadan": {
        "verdict": "The loudest, fastest anime of its moment: occult-obsessed Ken "
            "and spirit-sighted Momo battle aliens and yokai in Science SARU's "
            "fire-hydrant-of-ideas animation. Romance, body horror, slapstick and "
            "genuine tenderness at forty frames a second. The show that made "
            "everyone ask 'how is this animated by humans?'",
        "faqs": [
            ("What is Dandadan about?",
             "A boy who believes in aliens and a girl who does not believe in ghosts "
             "- both proven wrong in the same episode, binding them into a war on "
             "everything uncanny."),
            ("Is it still ongoing?",
             "Yes - new seasons continue adapting the red-hot manga."),
            ("Is it very weird?",
             "Gloriously - expect the strangest character designs of the decade "
             "wrapped around a sincere first-love story."),
        ],
    },
    "blue-lock": {
        "verdict": "Football as battle royale: Japan's federation imprisons 300 "
            "strikers in a facility designed to manufacture the world's most "
            "selfish goal-scorer. Ego is the theme, the training puzzles are "
            "genuinely tense, and the sports genre gets a supervillain grin. For "
            "everyone who ever wanted Diamond no Ace to draw blood.",
        "faqs": [
            ("Is Blue Lock like other sports anime?",
             "It turns the genre's teamwork gospel upside down - cooperation is "
             "suspect and individuality is weapon; that inversion is the thrill."),
            ("Is the manga ahead of the anime?",
             "Yes - the manga continues well beyond; the anime adapts in its wake."),
            ("Where should I start?",
             "Season one, episode one - the selection tournament explains itself as "
             "it goes."),
        ],
    },
    "black-clover": {
        "verdict": "The classic shonen underdog, executed with total commitment: "
            "Asta is born without magic in a world where magic is everything - so "
            "he screams louder, trains harder and swings anti-magic swords at "
            "destiny itself. 170 episodes of escalating tournaments, knights and "
            "devils, with one of anime's most loved-no-matter-what protagonists.",
        "faqs": [
            ("Is Black Clover finished?",
             "The TV series ran 170 episodes (2017-2021); the story continued with "
             "the 2023 film and further plans, while the manga advances toward its "
             "finale."),
            ("Why do people say it gets good?",
             "Early episodes lean on tired gags, then the Royal Knights arc onward "
             "delivers the payoff - the fandom's 'push past episode 20' advice."),
            ("Where do I start?",
             "Episode one, or the movie after the series if pacing is a concern."),
        ],
    },
    "code-geass": {
        "verdict": "The mecha-chess tragedy that defined an era: an exiled prince "
            "gains the power of absolute obedience and declares war on his own "
            "empire as the masked terrorist Zero. Every episode is gambits within "
            "gambits; the ending remains one of anime's most audacious, tear-jerking "
            "final acts. Twenty-five years of 'peak anime' arguments, and it keeps "
            "winning them.",
        "faqs": [
            ("How many seasons does Code Geass have?",
             "Two - Code Geass (2006) and Code Geass R2 (2008), fifty episodes total, "
             "one complete story."),
            ("Do I watch the movies?",
             "The compilation films retell the series with changes; the 2019 film "
             "Lelouch of the Re;surrection continues after. Series first, always."),
            ("Why is the ending so praised?",
             "It commits completely to its hero's monstrous, self-sacrificing plan - "
             "a finale that recontextualises all fifty episodes."),
        ],
    },
    "toradora": {
        "verdict": "The tsundere gold standard: gentle delinquent Ryuji and "
            "pocket-sized tiger Taiga scheme to help each other woo their best "
            "friends, and accidentally find the real thing. Twenty-five episodes "
            "of comedy that quietly assemble one of anime's most sincere romances, "
            "topped by the Christmas arc that still tops emotional-damage lists.",
        "faqs": [
            ("Is Toradora the best romance anime?",
             "It is perennially on the shortlist - the character growth across its "
             "single season is the benchmark newer shows chase."),
            ("Do I read the light novels?",
             "Optional - the anime adapts the full story arc; the novels add "
             "epilogue depth."),
            ("How long is it?",
             "25 episodes - one clean season."),
        ],
    },
    "ant-man-2": {
        "verdict": "The MCU's breeziest heist gets its sequel: Scott Lang, Hope and "
            "Hank race Ghost and black-market buyers into the quantum realm - and "
            "the family banter carries the film straight into a post-credits gut-"
            "punch that recontextualises it forever. Light as fog, important as a "
            "snap.",
        "faqs": [
            ("Why is Ant-Man and the Wasp important to the MCU?",
             "Its final moments run parallel to Infinity War's snap - the cliffhanger "
             "makes it essential Endgame context."),
            ("Do I need the first Ant-Man?",
             "Yes - the cast, the quantum realm rules and the tone all build on it."),
            ("How long is it?",
             "118 minutes."),
        ],
    },
    "aquaman-2": {
        "verdict": "James Wan's underwater opera takes its final swim: Arthur, "
            "Mera and a resentful brother unite against an ancient deep-state "
            "kingdom, with bigger creatures and a lighter heart than its dour "
            "reputation suggests. Divisive at the box office, sincere on screen - "
            "the DCEU's aquatic send-off with real charm in the margins.",
        "faqs": [
            ("Do I need the first Aquaman?",
             "Yes - the brother dynamic and the throne politics continue directly."),
            ("Is it the last Aquaman film?",
             "It closed the DC films of that era; the character's screen future was "
             "reset with the new DC universe."),
            ("How long is it?",
             "124 minutes."),
        ],
    },
    "blue-beetle": {
        "verdict": "The warmest superhero film of its year: Jaime Reyes comes home "
            "from college to find an alien scarab welded to his spine - and his "
            "delightful, fully realised Latino family along for every minute. "
            "Xolo Mariduena is a star, the humour is organic, and the film's "
            "modest box office hid one of DC's most liked entries. Familia over "
            "franchise.",
        "faqs": [
            ("Why is Blue Beetle significant?",
             "It is DC's first feature headlined by a Latino superhero - and the "
             "family-centred storytelling is the point, not an afterthought."),
            ("Is it connected to other DC films?",
             "It stands alone - and the character has been carried forward in DC's "
             "new era plans."),
            ("How long is it?",
             "127 minutes."),
        ],
    },
    "x-men": {
        "verdict": "The film that proved the team could work after a decade of "
            "superhero failures: a brand called mutant, a school for the gifted, "
            "and one snarling unknown named Hugh Jackman changing franchises "
            "forever. Tight, scrappy and sincere where later films got loud - "
            "the foundation stone of the modern Marvel age of cinema.",
        "faqs": [
            ("Did X-Men start the modern superhero era?",
             "It is widely credited (with Blade the year before) as the film that "
             "made studios trust comic-book cinema again - two years before "
             "Spider-Man and eight before the MCU."),
            ("Do I watch it before the prequels?",
             "Either order works, but release order (X-Men, X2, then First Class "
             "and the rest) preserves the reveals best."),
            ("How long is it?",
             "104 minutes."),
        ],
    },
    "x-men-2": {
        "verdict": "The sequel that outgrew the original: Nightcrawler's White "
            "House attack opens the best action sequence of the pre-MCU era, and "
            "the film never looks back - Stryker's purge, Logans memory-lab, and "
            "an ending that still has weight. Regularly cited among the greatest "
            "superhero sequels ever made. The high-water mark of the original "
            "trilogy.",
        "faqs": [
            ("Is X2 one of the best superhero sequels?",
             "It is on nearly every such list - the Nightcrawler opening alone is "
             "taught as action-filmmaking craft."),
            ("Do I need the first film?",
             "Yes - character arcs (Wolverine, Rogue, Magneto) continue directly."),
            ("How long is it?",
             "133 minutes."),
        ],
    },
    "agatha": {
        "verdict": "The WandaVision scene-stealer gets her own coven: Agatha Harkness, "
            "powerless and petty, walks the treacherous Witches' Road with a band "
            "of delightfully odd spellcasters. Kathryn Hahn devours every scene, "
            "the finale recontextualises the road itself, and the whole thing is "
            "far smarter about grief than its camp reputation admits. Disney+'s "
            "best-reviewed Marvel showing of its year.",
        "faqs": [
            ("Do I need WandaVision first?",
             "Yes - Agatha's history, her song and her punishment all come from it; "
             "the payoff depends on it."),
            ("Is it related to the WandaVision song?",
             "The viral 'Agatha All Along' tune was born in WandaVision and named "
             "this series."),
            ("How many episodes?",
             "Nine - a complete, contained season."),
        ],
    },
    "deep-water": {
        "verdict": "Adrian Lyne's return after two decades: Ben Affleck and Ana de "
            "Armas play a married couple whose open-marriage games curdle into "
            "something much worse, adapted from Patricia Highsmith's icy novel. "
            "Slow-burn dread, garden snails and a final shot people argue about - "
            "the erotic thriller's old master signing off in style.",
        "faqs": [
            ("Is Deep Water based on a book?",
             "On Patricia Highsmith's 1957 novel - her first, from the author of "
             "The Talented Mr. Ripley."),
            ("Why was it so anticipated?",
             "It marked Adrian Lyne's first film in twenty years (the director of "
             "Fatal Attraction and Unfaithful)."),
            ("Is it slow?",
             "Deliberately - the dread accrues in domestic details before the "
             "thriller mechanics engage."),
        ],
    },
    "the-grudge": {
        "verdict": "The remake that imported dread wholesale: Takashi Shimizu "
            "re-stages his own Ju-On for America - a Tokyo house where the dead "
            "cling like damp, and a chain of residents learn the curse is not a "
            "haunting, it is an infection. Told in shards, quiet as a held breath. "
            "The film that made an entire generation afraid of attic spaces.",
        "faqs": [
            ("Is The Grudge a remake?",
             "Of the director's own Ju-On: The Grudge (2002) - Shimizu directed "
             "both, keeping the mythology and reframing it through new characters."),
            ("Why does the story jump around in time?",
             "The curse is nonlinear by nature - the fractured timeline mirrors "
             "how the grudge traps everyone it touches."),
            ("How long is it?",
             "88 minutes."),
        ],
    },
    "the-road": {
        "verdict": "The grimmest, most sincere apocalypse in mainstream cinema: a "
            "father and son push a shopping cart through a dead, grey America, "
            "guarding the fire of being 'the good guys'. Cormac McCarthy's novel "
            "rendered with total fidelity - ash, hunger, love without limit. Not "
            "survival horror; a prayer with teeth.",
        "faqs": [
            ("Is The Road based on a book?",
             "On Cormac McCarthy's 2006 Pulitzer-winning novel - one of the most "
             "respected American novels of its era."),
            ("What caused the apocalypse?",
             "Never explained - in the book or the film; the absence of "
             "explanation is the point."),
            ("How depressing is it?",
             "Very - and endurable because of the father-son love at its centre; "
             "viewers leave shaken but not empty."),
        ],
    },
    "the-gorge": {
        "verdict": "Two snipers on opposite cliffs, ordered never to look down - "
            "and the gorge between them hides something ancient that wants out. "
            "Miles Teller and Anya Taylor-Joy fall in love across the void via "
            "handwritten signs while the horror escalates below. Sincere genre "
            "fun: half romance, half creature chasm, fully committed.",
        "faqs": [
            ("Where can The Gorge be watched?",
             "It was released as a major streaming original - check current "
             "platform listings in your region."),
            ("Is it a romance or a horror film?",
             "Both halves, earnestly - the long-distance courtship plays straight "
             "before the monsters claim the film."),
            ("How long is it?",
             "127 minutes."),
        ],
    },
    "atomic-blonde": {
        "verdict": "Cold-War candy with knuckles: Charlize Theron's MI6 blade "
            "smashes through 1989 Berlin for a list of double agents, and David "
            "Leitch shoots it like a music video that lifts weights. The "
            "stairwell fight - one unbroken, exhausting take - is among the "
            "great modern action sequences. Style with real bruise.",
        "faqs": [
            ("Is Atomic Blonde based on a comic?",
             "On Antony Johnston's graphic novel The Coldest City."),
            ("Is the stairwell fight really one take?",
             "It is presented as an extended single take (with hidden stitches) - "
             "Theron trained extensively and the stunt team earned every bruise "
             "in it."),
            ("How long is it?",
             "115 minutes."),
        ],
    },
    "booksmart": {
        "verdict": "The graduation-night revolution: two straight-A best friends "
            "realise they studied through high school and now have one night to "
            "make up for it. Olivia Wilde's directing debut is fast, filthy and "
            "secretly one of the warmest friendship films of the decade. Superbad "
            "with straight As and a bigger heart.",
        "faqs": [
            ("Is Booksmart suitable for teens?",
             "Older teens - R-rated language and party content, but its values "
             "(friendship, identity, kindness) are exemplary."),
            ("Was it a hit?",
             "Modestly at the box office, hugely with critics - it immediately "
             "made Wilde a sought-after director."),
            ("How long is it?",
             "102 minutes."),
        ],
    },
    "blockers": {
        "verdict": "The sex-comedy with the parents' seat flipped: three mums and "
            "dads try to sabotage their daughters' prom-night pact, and the film "
            "lands the harder joke - the kids are right, the parents are the "
            "chaos. Leslie Mann at full flight, John Cena's nervous breakdown in "
            "a prom dress for the win. Honest, hilarious, sneakily wise.",
        "faqs": [
            ("Is Blockers appropriate for family viewing?",
             "With older teens, weirdly ideal - it is R-rated but its message "
             "about trust and consent is the healthiest in the genre."),
            ("Is it the director's first film?",
             "Yes - Kay Cannon (writer of the Pitch Perfect films) directed it as "
             "her debut."),
            ("How long is it?",
             "102 minutes."),
        ],
    },
    "elemental": {
        "verdict": "Fire meets water in Element City: a fiery temp with a temper "
            "and a go-with-the-flow water guy fall for each other across a city "
            "of elements. A slow starter that word of mouth turned into a "
            "genuine phenomenon - underneath the gas-flame puns is Pixar's most "
            "personal immigrant-family story yet.",
        "faqs": [
            ("Did Elemental do well?",
             "A famous slow-burn: a quiet opening, then weeks of word-of-mouth "
             "growth into one of the year's biggest animated hits."),
            ("What is it really about?",
             "Immigrant families and inherited expectation - director Peter Sohn "
             "built it from his own Korean-American upbringing."),
            ("How long is it?",
             "102 minutes."),
        ],
    },
    "wonka": {
        "verdict": "Paul King (Paddington) does the impossible politely: a "
            "young Wonka pre-factory, all optimism and chocolate, sung through "
            "with genuine warmth and Timothee Chalamet's twinkling con-man charm. "
            "It should be cynical brand extension; it is instead the coziest "
            "family film of its year. Pure imagination, tidily justified.",
        "faqs": [
            ("Do I need the older Wonka films?",
             "No - it is an origin-flavoured tale that stands alone and plays "
             "gently alongside them."),
            ("Is it a musical?",
             "Yes - original songs plus a few classics, in Paddington-style "
             "warmth rather than spectacle.",
             ),
            ("How long is it?",
             "116 minutes."),
        ],
    },
    "wreck-it-ralph": {
        "verdict": "The villain support group that launched a franchise: an arcade "
            "bad-guy sneaks into other games to win a medal and finds a glitchy "
            "little friend instead. Disney's video-game love letter - sugar-rush "
            "worldbuilding, a great villain reveal, and real feeling under the "
            "coin-op nostalgia. 'I'm gonna wreck it!' remains a perfect catchphrase.",
        "faqs": [
            ("Did Wreck-It Ralph win the Oscar?",
             "It was nominated for Best Animated Feature at the 2013 ceremony "
             "(Brave won) - and its sequel followed in 2018."),
            ("Do I need to know arcade games?",
             "No - the cameos (Bowser, Sonic, Q*bert) are garnish; the story runs "
             "on its own characters."),
            ("How long is it?",
             "101 minutes."),
        ],
    },
    "blood-sisters": {
        "verdict": "Nigeria's first Netflix original drama series, and it swings: "
            "a bride's perfect engagement collapses into a death, and two best "
            "friends go on the run through Lagos - money, family secrets and a "
            "hunter who will not stop. Glossy Nollywood thriller craft with "
            "genuine momentum, built to binge.",
        "faqs": [
            ("Is Blood Sisters a film or a series?",
             "A limited series - four 50-minute episodes telling one continuous "
             "story."),
            ("Why is it called Nigeria's first Netflix original?",
             "It was widely described as the first Nigerian Netflix Original "
             "drama series - a milestone for Nollywood on the global stage."),
            ("Is it subtitled?",
             "It plays in English with Nigerian languages woven in - subtitles "
             "helpfully provided throughout."),
        ],
    },
    "the-set-up": {
        "verdict": "EbonyLife's slick heist con: a businesswoman is drawn into a "
            "collar-meets-double-cross plot that keeps flipping the mark, with "
            "Niyi Akinmolayan directing Lagos gloss and Ramsey Nouah relishing "
            "the long game. Twisty, stylish, unapologetically commercial - "
            "Nollywood's answer to the casino con genre.",
        "faqs": [
            ("Is there a sequel?",
             "Yes - The Set Up 2 (2022) continued the con world with new marks."),
            ("Who directed it?",
             "Niyi Akinmolayan, one of Nollywood's most technically ambitious "
             "directors."),
            ("How long is it?",
             "103 minutes."),
        ],
    },
    "eyimofe": {
        "verdict": "The Nollywood art film that went to Berlin: two Lagos lives - "
            "a nurse saving every naira to reach Spain, a young man paying his "
            "sister's debts - told in patient, beautiful 16mm by the Esiri "
            "brothers. Eyimofe ('This Is My Desire') is migration's dream and "
            "cost, observed with documentary stillness. Nigerian cinema at its "
            "quietest and most international.",
        "faqs": [
            ("What does Eyimofe mean?",
             "'This Is My Desire' - the film was released with that subtitle."),
            ("Is it one story or two?",
             "Two mirrored halves - Mofe's story then Rosa's - that share a city, "
             "a dream of Europe and its price."),
            ("Was it recognised internationally?",
             "Yes - it premiered at the Berlin International Film Festival and "
             "travelled the festival circuit widely."),
        ],
    },
    "wandering-earth": {
        "verdict": "China's sci-fi arriving at blockbuster scale: when the sun "
            "dies, humanity does not flee - it installs giant engines and moves "
            "the planet itself out of the solar system. Adapted from Liu Cixin, "
            "spectacular and stubbornly collective in its heroism, and one of "
            "the highest-grossing Chinese films ever. The day Earth stood still, "
            "and then walked.",
        "faqs": [
            ("Is The Wandering Earth based on a book?",
             "On Liu Cixin's novella (author of The Three-Body Problem) - the film "
             "expands a fragment into a full disaster epic."),
            ("Why is the premise unusual?",
             "Most stories abandon Earth; this one takes it along - engines, "
             "underground cities and all."),
            ("Is there a sequel?",
             "Yes - The Wandering Earth II (2023), a prequel that many rate even "
             "higher."),
        ],
    },
    # ---- film batch 15 (2026-09-24): 30 titles - prestige TV, MCU completion, classics, anime arc ----
    "andor": {
        "verdict": "The Star Wars show for people who do not like Star Wars shows: "
            "Cassian Andor's road from petty thief to rebel, told as adult espionage "
            "drama - corporate offices, prison labour, radicalisation, bureaucracy as "
            "villain. Tony Gilroy's writing made it one of the best-reviewed series of "
            "its decade, and the ending lands you at the first frame of Rogue One. "
            "Went out on top, deliberately.",
        "faqs": [
            ("Do I need Rogue One or other Star Wars first?",
             "Rogue One is the real prerequisite - the series ends exactly where the "
             "film begins, and knowing the destination makes the journey devastating."),
            ("Is it slow or political?",
             "Deliberately paced and unapologetically political - radicalisation, "
             "empire and compromise are the subjects; the prison arc alone justifies "
             "every minute."),
            ("Is the story complete?",
             "Yes - two seasons (2022 and 2025), planned and executed as one arc."),
        ],
    },
    "the-last-kingdom": {
        "verdict": "Vikings' grittier, truer cousin: Uhtred of Bebbanburg - Saxon born, "
            "Dane raised - fights for Alfred the Great's England while his own "
            "birthright stays stolen. Bernard Cornwell's novels give it real historical "
            "spine, and five seasons of battles, bargains and stubborn honour earn the "
            "big-screen send-off. The most under-watch epic of its era.",
        "faqs": [
            ("Is The Last Kingdom based on books?",
             "On Bernard Cornwell's Saxon Stories - thirteen novels of real 9th-century "
             "history woven around a fictional hero."),
            ("Do I watch the movie after the series?",
             "Yes - Seven Kings Must Die (2023) continues directly after season five "
             "and closes Uhtred's tale."),
            ("How true is the history?",
             "Alfred, Aethelflaed and the Dane wars are real; Uhtred's personal story "
             "is invented - the texture is researched, the plot is drama."),
        ],
    },
    "the-white-lotus": {
        "verdict": "Mike White's luxury-resort autopsy: gorgeous location, terrible "
            "guests, one body too many by checkout. Each season is a self-contained "
            "satire of wealth and service - Hawaii, Sicily, Thailand - stitched "
            "together by tone and Jennifer Coolidge's immortal Tanya. The rare "
            "anthology where the destination is the company, not the corpse.",
        "faqs": [
            ("Are the seasons connected?",
             "Mostly standalone - new location and cast each season, with light "
             "connective threads; start with season one or jump anywhere."),
            ("Is it based on true events?",
             "No - pure satire, aimed at wealthy tourists and the people paid to "
             "endure them."),
            ("Did it win awards?",
             "Generously - multiple Emmys across its seasons, including Jennifer "
             "Coolidge's supporting-actress win."),
        ],
    },
    "wandavision": {
        "verdict": "The MCU's boldest swing: grief as a sitcom - Wanda's captured town "
            "replays decades of American television while two nosy detectives close "
            "in. Elizabeth Olsen and Paul Bettany play it beautifully straight, "
            "Kathryn Hahn's witch reveal detonates the format, and the whole thing "
            "lands as Marvel's saddest, strangest experiment. Nothing else like it "
            "before or since.",
        "faqs": [
            ("How much MCU do I need?",
             "The Wanda and Vision arcs from the Avengers films are the baseline - "
             "the show assumes you know what Wanda lost."),
            ("Is it really a sitcom all the way through?",
             "No - the format is the mystery; it curdles into a full Marvel drama as "
             "the truth leaks in."),
            ("Where does it lead?",
             "Directly into Doctor Strange in the Multiverse of Madness, and its "
             "villain's song launched a whole spin-off."),
        ],
    },
    "the-falcon-winter-soldier": {
        "verdict": "The MCU's buddy-espionage reckoning: Sam Wilson refusing the "
            "shield, Bucky working through his ledger, and America's reaction to a "
            "Black Captain America made explicitly the subject. Zemo's stylish return, "
            "Wyatt Russell's catastrophic US Agent, and a finale that hands the "
            "franchise its new Cap with real weight.",
        "faqs": [
            ("Do I need it before Brave New World?",
             "Yes - it is the direct setup for Sam Wilson's Captain America era."),
            ("Is it heavy on MCU homework?",
             "The Blip aftermath is the engine, so Endgame context matters - beyond "
             "that it explains itself."),
            ("How many episodes?",
             "Six - a tight limited series."),
        ],
    },
    "thunderbolts": {
        "verdict": "The MCU's misfit mirror: a depressed ex-assassin, a washed-up "
            "super soldier, a paranoid Centurion of a Red Guardian and friends - "
            "assembled to die, choosing instead to matter. Florence Pugh anchors "
            "the bleakest, funniest Marvel ensemble in years, and the asterisk in "
            "the title hides the film's cheekiest reveal. Group therapy with "
            "explosions.",
        "faqs": [
            ("Why the asterisk in Thunderbolts*?",
             "It is a running joke with an in-film payoff - the team's marketing "
             "versus its reality; the film explains itself."),
            ("Do I need deep MCU knowledge?",
             "Less than most - the film reintroduces its ragtag cast from zero and "
             "runs on character chemistry more than lore."),
            ("Does it set up future films?",
             "Yes - its status-quo wink feeds directly into the next phase."),
        ],
    },
    "the-fantastic-four-first-steps": {
        "verdict": "The family, finally right: Marvel's first family on a retro-"
            "futurist 1960s Earth, facing a god that eats planets. Pedro Pascal, "
            "Vanessa Kirby, Joseph Quinn and Ebon Moss-Bachrach click as a household "
            "before they click as heroes, and Shakman shoots it like a vintage "
            "space-age postcard. The friendliest door into the MCU in years.",
        "faqs": [
            ("Do I need other Marvel films first?",
             "No - it is deliberately self-contained on its own alternate Earth; "
             "newcomers welcome."),
            ("Is it suitable for kids?",
             "Among the most family-friendly MCU entries - cosmic menace without "
             "gratuitous darkness."),
            ("Is it the best Fantastic Four film?",
             "By wide consent, yes - the first to treat the family dynamic as the "
             "point rather than the setup."),
        ],
    },
    "alien-resurrection": {
        "verdict": "The Alien franchise's strangest animal: Ripley cloned two "
            "centuries on, part alien by design, aboard a Jeunet-directed funhouse "
            "of body horror and gallows humour. Divisive, perverse, visually "
            "brilliant - the series' cult entry, and proof the property never "
            "repeated itself. Newborn monster included.",
        "faqs": [
            ("Do I need the earlier Alien films?",
             "Yes - at minimum Alien, Aliens and Alien 3; the whole premise is a "
             "response to Ripley's sacrifice."),
            ("Is it really that weird?",
             "Deliberately - Jean-Pierre Jeunet's dark-fairy-tale instincts plus a "
             "Joss Whedon script make it the franchise's oddest curve."),
            ("How long is it?",
             "109 minutes."),
        ],
    },
    "carrie": {
        "verdict": "Stephen King's first novel became the definitive prom-night "
            "tragedy: Sissy Spacek's telekinetic outcast, Piper Laurie's fanatic "
            "mother, and De Palma's split-screen descent into pig's blood and "
            "flames. Both women earned Oscar nominations - horror royalty - and the "
            "final shot still jerks fifty years of audiences out of their seats. "
            "Puberty as horror film, perfected.",
        "faqs": [
            ("Is Carrie based on a book?",
             "On Stephen King's 1974 debut novel - his first published, and still "
             "one of his most adapted."),
            ("How scary is it?",
             "Slow-burn tragedy first, notorious shock finale second - the horror "
             "is cruelty as much as telekinesis."),
            ("Is the 2013 remake worth it?",
             "It exists and is respectful; the 1976 original remains the definitive "
             "version by wide consent."),
        ],
    },
    "ghostbusters": {
        "verdict": "The 1984 original, still the perfect comedy machine: three "
            "disgraced academics, a New York crawling with the undead, and Bill "
            "Murray deadpanning through the apocalypse. Aykroyd and Ramis' script "
            "treats the supernatural as bureaucracy, the effects hold up, and the "
            "theme song ruled the planet. Forty years of sequels, cartoons and "
            "legacyquels - all of them walk in this one's footprints.",
        "faqs": [
            ("Do I start with the 1984 film or the newer ones?",
             "The 1984 original, always - everything after (1989's sequel, the 2021 "
             "and 2024 legacy films) builds on it."),
            ("Did the theme song top the charts?",
             "Yes - Ray Parker Jr.'s 'Ghostbusters' spent weeks at number one and "
             "earned an Oscar nomination."),
            ("How long is it?",
             "105 minutes."),
        ],
    },
    "willow": {
        "verdict": "George Lucas's story, Ron Howard's direction, Warwick Davis' "
            "farmer-hero: a reluctant Nelwyn conjurer escorts a chosen-one princess "
            "through a Val Kilmer-shaped sword-and-sorcery romp. Its early digital "
            "morphing sequence is a landmark in effects history, and its heart has "
            "kept the cult growing for decades. Fantasy comfort food with a "
            "groundbreaking streak.",
        "faqs": [
            ("Is Willow connected to Star Wars?",
             "Spiritually - from a George Lucas story with Lucasfilm production "
             "craft; fans call it fantasy Star Wars with good reason."),
            ("Is there a sequel series?",
             "Yes - the 2022 Disney+ continuation; this 1988 film is the required "
             "starting point."),
            ("Why do effects people love it?",
             "Its morphing sequence was pioneering early digital imagery - a genuine "
             "milestone between practical eras."),
        ],
    },
    "the-labyrinth": {
        "verdict": "Jim Henson's puppet odyssey, produced by George Lucas and "
            "crowned by David Bowie's Goblin King: a teenager's baby brother is "
            "stolen into a maze of Muppets, riddles and danger, and Sarah must wish "
            "him back properly. A flop that became a religion - Bowie's songs, "
            "Henson's workshop at full power, and the strangest ballroom in cinema. "
            "'You have no power over me' - the line every misfit keeps.",
        "faqs": [
            ("Does David Bowie sing in Labyrinth?",
             "Yes - several original songs, including 'Magic Dance' and 'As the "
             "World Falls Down'."),
            ("Is it too scary for young kids?",
             "It has genuinely eerie stretches - the Helping Hands and the Fireys - "
             "best for older children and up."),
            ("Why is it a cult classic?",
             "A box-office flop on release, then decades of VHS devotion: Henson's "
             "craft and Bowie's performance age like wine."),
        ],
    },
    "twisters": {
        "verdict": "The disaster movie reborn with manners: a storm-chaser haunted "
            "by loss and a swaggering wrangler-turned-tornado-tourist face a record "
            "outbreak across Oklahoma. Lee Isaac Chung shoots storms with awe "
            "instead of green-screen slop, Daisy Edgar-Jones and Glen Powell spark "
            "cleanly, and the film trusts spectacle without irony. Old-school "
            "summer, done right.",
        "faqs": [
            ("Do I need the 1996 Twister first?",
             "No - it is a standalone story in the same storm country."),
            ("Is the storm science real?",
             "The storm-chaser culture is authentic; the tech is amped up - the "
             "film keeps its feet mostly on the ground."),
            ("How long is it?",
             "122 minutes."),
        ],
    },
    "the-super-mario-bros-movie": {
        "verdict": "The video-game adaptation curse, shattered: Mario, Luigi and a "
            "Kong kingdom rendered in Illumination candy, with Jack Black's Bowser "
            "stealing the film and the charts. Over 1.3 billion dollars later, it "
            "stands as one of the highest-grossing animated films ever - a pure "
            "homage machine that plays like two hours of fan service done with "
            "affection.",
        "faqs": [
            ("Do I need to know the games?",
             "No - it plays as a bright adventure; players just collect far more "
             "cameos per minute."),
            ("What is the Bowser song?",
             "'Peaches' - Jack Black's piano ballad, the film's breakout earworm."),
            ("Is there a sequel?",
             "Yes - a Galaxy-set follow-up is in the works."),
        ],
    },
    "zootopia-2": {
        "verdict": "The mammal metropolis adds reptiles: Judy and Nick go undercover "
            "through Zootopia's cold-blooded underbelly in a sequel with bigger "
            "conspiracy and sharper worldbuilding. The 2016 original won the Best "
            "Animated Feature Oscar; the follow-up became one of 2025's biggest "
            "releases worldwide - the rare franchise where the satire grows up with "
            "its audience.",
        "faqs": [
            ("Do I need the first Zootopia?",
             "Yes - the buddy dynamic and the city's premise are the engine; watch "
             "the 2016 Oscar winner first."),
            ("Is it as good as the original?",
             "It was warmly reviewed and a blockbuster - most fans rate it a worthy "
             "continuation rather than a repeat."),
            ("How long is it?",
             "108 minutes."),
        ],
    },
    "frozen-2": {
        "verdict": "The rare sequel that outgrossed a phenomenon: Elsa hears a voice, "
            "the sisters ride north, and Arendelle's founding sin surfaces in "
            "myth-heavy, autumn-toned spectacle. Darker than the first film, "
            "genuinely moving about change and loss, with 'Into the Unknown' and an "
            "Olaf who has learned to talk about death. The kids' film that quietly "
            "processes grief.",
        "faqs": [
            ("Is Frozen 2 better than the first?",
             "It goes deeper and stranger - critics split, audiences made it the "
             "bigger earner worldwide; both belong in any family rotation."),
            ("Do I need the first film?",
             "Yes - the character stakes are all inherited."),
            ("How long is it?",
             "103 minutes."),
        ],
    },
    "demon-slayer-mugen-train": {
        "verdict": "The film that rewrote the record books in Japan: the Mugen Train "
            "arc - Tanjiro and the flame Hashira Rengoku aboard a demon-haunted "
            "locomotive - became Japan's all-time box-office champion and the first "
            "non-Hollywood film to lead the worldwide yearly chart. ufotable at "
            "full fire, and an emotional gut-punch the entire fandom still carries. "
            "Watch season one first; bring tissues.",
        "faqs": [
            ("Can I watch the film without the series?",
             "No - it is a direct sequel to season one and will spoil itself into "
             "noise; watch the series first."),
            ("Where does it fit?",
             "Between seasons one and two - the TV version re-adapts it as the "
             "opening arc of the Entertainment District season."),
            ("Why does everyone cry about it?",
             "Rengoku. That is the whole answer."),
        ],
    },
    "demon-slayer-infinity-castle": {
        "verdict": "The final-arc begins: Tanjiro and the surviving Hashira fall "
            "into Muzan's shifting fortress, and ufotable delivers 155 minutes of "
            "the most ambitious animation of the decade. It smashed Japan's box-"
            "office records upon release and opens a planned trilogy - the Demon "
            "Slayer saga's endgame has arrived, and it is staggering.",
        "faqs": [
            ("What do I watch first?",
             "Everything: seasons one through four plus Mugen Train - this film is "
             "pure endgame."),
            ("Is it the last Demon Slayer film?",
             "It is the first of a planned trilogy adapting the final arc."),
            ("How long is it?",
             "155 minutes of escalating spectacle."),
        ],
    },
    "chainsaw-man-reze": {
        "verdict": "Denji's first love arrives holding a lit fuse: the Reze arc - "
            "the manga's most beloved stretch - arrives on film as a romance that "
            "keeps detonating into set pieces. Typhoon-lit schoolyards, a cafe that "
            "feels like a memory, and violence choreographed like dance. The "
            "perfect continuation for anyone the series hooked.",
        "faqs": [
            ("Do I watch the series first?",
             "Yes - season one sets up Denji's heart and the world that breaks it; "
             "the film follows directly."),
            ("What is the Reze arc?",
             "The fan-favourite storyline introducing the girl of Denji's dreams - "
             "and the chaos attached to her; no spoilers past that."),
            ("How long is it?",
             "100 minutes."),
        ],
    },
    "tokyo-ghoul": {
        "verdict": "The dark-fantasy landmark of its era: bookish Kaneki's date "
            "turns out to be a ghoul, his survival makes him half-monster, and "
            "Tokyo's hidden flesh-eater society opens like a wound. Body horror as "
            "identity tragedy, an iconic opening theme, and a tone that defined "
            "dark anime for a generation of newcomers.",
        "faqs": [
            ("What order do I watch Tokyo Ghoul in?",
             "Season one, then Root A, then re - and note the anime diverges from "
             "the manga, which remains the fuller story."),
            ("Why is it so popular?",
             "It arrived at the perfect moment: accessible dark fantasy with real "
             "horror teeth and a protagonist whose transformation is the point."),
            ("Is it very gory?",
             "Yes - flesh-eating is the premise; it is stylish but unflinching."),
        ],
    },
    "trigun": {
        "verdict": "The space-western with the biggest tonal gearshift of its era: "
            "Vash the Stampede is a 60-billion-double-dollar legend who cannot stop "
            "saving people - until his past forces the comedy to collapse into "
            "tragedy. Episodic charm front-loading a moral core that still lands; "
            "the blueprint for every lovable-idiot-with-a-burden protagonist since.",
        "faqs": [
            ("Original Trigun or Trigun Stampede?",
             "The 1998 original is the classic entry; Stampede (2023) retells the "
             "story closer to the manga's order - fans argue happily, start anywhere."),
            ("Is it really a comedy?",
             "It starts as one - the pivot to tragedy is the series' whole legend."),
            ("Is it finished?",
             "The 1998 run is a complete story; the manga continued for decades."),
        ],
    },
    "your-lie-in-april": {
        "verdict": "The piano prodigy who cannot hear his own playing, the "
            "free-spirit violinist who drags him back into the light - twenty-two "
            "episodes of classical music, trauma and the most organised emotional "
            "devastation in anime. 'Your Lie in April' is less a title than a "
            "warning label. Bring the whole box of tissues.",
        "faqs": [
            ("Will I actually cry?",
             "It is one of the most reliably tearful anime ever made - plan "
             "accordingly."),
            ("Do I need to like classical music?",
             "No - the performances are emotional set pieces first; the music "
             "carries even non-fans."),
            ("Is the story complete?",
             "Yes - it adapts the full manga."),
        ],
    },
    "violet-evergarden": {
        "verdict": "Kyoto Animation's most beautiful ache: a child soldier of "
            "terrible efficiency becomes a writer of other people's love letters, "
            "learning what feelings are one commission at a time. The craft is "
            "legendary, episode ten is a rite of passage, and the 2020 film closes "
            "her arc with devastating grace. Letters that outlive their writers.",
        "faqs": [
            ("What order do I watch?",
             "The series, then the 2020 film - the film is the true conclusion."),
            ("Which episode is the famous one?",
             "Episode ten - the dying mother's fifty letters - is the one people "
             "warn each other about."),
            ("Is it sad throughout?",
             "Melancholy-warm: every episode touches loss, and the cumulative effect "
             "is catharsis, not misery."),
        ],
    },
    "apothecary-diary": {
        "verdict": "The court-mystery phenomenon: Maomao, a pharmacy-obsessed "
            "apothecary sold into the imperial rear palace, solves poisonings and "
            "politics with the same deadpan brilliance - while a beautiful, "
            "dangerous eunuch keeps buying her experiments. Sharp heroine, "
            "meticulous period detail, and the coziest slow-burn dynamic in recent "
            "anime. Mystery comfort food with real teeth.",
        "faqs": [
            ("What kind of show is it?",
             "Historical mystery first - poison cases and palace intrigue - with a "
             "deliberately restrained romance thread."),
            ("Is it still ongoing?",
             "Yes - new seasons continue adapting the light novels."),
            ("Why is Maomao so loved?",
             "She is brilliant, prickly, poison-curious and entirely her own person - "
             "a protagonist the genre had been missing."),
        ],
    },
    "fargo": {
        "verdict": "The anthology that earned the Coen name: each season a standalone "
            "Midwestern crime tragedy - snow, nerves, catastrophic politeness - "
            "plotted with brutal elegance and sprinkled with dark comedy. Billy Bob "
            "Thornton's chilling first season won the Emmy, season two is a "
            "perennial all-timer, and every new cycle is an event. 'This is a true "
            "story' - the nicest lie on television.",
        "faqs": [
            ("Do the seasons connect?",
             "Each is standalone with its own cast and era - you can start with "
             "season one or the consensus masterpiece, season two."),
            ("Do I need the 1996 film?",
             "No - it shares the tone and universe flavor, not the plot."),
            ("How many seasons so far?",
             "Five so far, with more possible - check current listings."),
        ],
    },
    "the-sandman": {
        "verdict": "Neil Gaiman's dreams finally on screen: Morpheus, King of "
            "Dreams, escapes a century of captivity and rebuilds his kingdom across "
            "anthological wonders - a diner in Hell, a cat's sermon, a 19th-century "
            "gentleman's serial. Tom Sturridge plays eternity beautifully; the "
            "craft honours the comic panel by panel. The story wrapped with its "
            "second season - complete, as dreamed.",
        "faqs": [
            ("Can I watch episodes standalone?",
             "Largely yes - several are self-contained gems; the through-line "
             "rewards order."),
            ("Do I need the comics?",
             "No - the adaptation stands alone while fans spot the faithful panels."),
            ("Is the story finished?",
             "Yes - the second season (2025) concluded the adaptation."),
        ],
    },
    "the-umbrella-academy": {
        "verdict": "Seven adopted super-siblings, one dreadful father, and an "
            "apocalypse per season: Gerard Way's comic became TV's most watchable "
            "dysfunction - time travel, sibling therapy and needle-drop choreography "
            "of the highest order. Aidan Gallagher's Number Five is a scene-stealing "
            "icon, and the ensemble ran four seasons to a proper ending.",
        "faqs": [
            ("Is the story finished?",
             "Yes - four seasons, concluding properly in 2024."),
            ("Do I need the comic?",
             "No - the show remixes it freely; reading is optional homework."),
            ("What is it best known for?",
             "The family chemistry and its music-driven sequences - some of the "
             "best needle-drops of the streaming era."),
        ],
    },
    "the-glory": {
        "verdict": "Revenge served cold, over years: a woman with nothing left "
            "carefully dismantles the lives of the schoolmates who tortured her - "
            "and Kim Eun-sook (of Descendants of the Sun fame) writes it with "
            "icy, meticulous patience. Song Hye-kyo's career-peak performance "
            "anchors one of Netflix Korea's most talked-about dramas. Hard to "
            "watch, impossible to drop.",
        "faqs": [
            ("How brutal is the bullying content?",
             "Genuinely hard - the violence is a plot engine, not decoration; "
             "sensitive viewers should brace."),
            ("Is it one season or two?",
             "A two-part story - the first part in late 2022, the conclusion in "
             "March 2023."),
            ("Is it based on real events?",
             "It is fiction, channelling South Korea's real reckoning with school "
             "violence - which is why it hit the national nerve."),
        ],
    },
    "vikram-vedha": {
        "verdict": "The Tamil neo-noir that riddles its way into legend: a cop "
            "(Madhavan) interrogates a gangster (Vijay Sethupathi) who answers "
            "every question with a folk-tale that reframes the cop's own life - "
            "Vikram-and-Betaal morality as an action thriller. Twist after twist, "
            "two stars sparring at their peak, and a Hindi remake that proves how "
            "strong the original is. Kya kahtha hai Vedha? See it.",
        "faqs": [
            ("Original or the 2022 Hindi remake?",
             "The Tamil original is the consensus watch - the Hrithik-Saif remake "
             "is faithful, the original is sharper."),
            ("What is the Vikram-Vedha story frame?",
             "A king-and-sage riddle cycle from Indian folklore - every tale the "
             "gangster tells forces the cop to rethink right and wrong."),
            ("How long is it?",
             "147 minutes."),
        ],
    },
    "conclave": {
        "verdict": "The papal election as political thriller: Ralph Fiennes' "
            "cardinal-dean must steer a locked-room conclave of ambitious princes "
            "of the church while secrets surface with every ballot. Edward Berger "
            "follows All Quiet with immaculate tension - bargaining, scheming, "
            "Isabella Rossellini - and an ending that detonates the whole film's "
            "argument. The Adapted Screenplay Oscar was earned.",
        "faqs": [
            ("Do I need Catholic knowledge?",
             "No - it explains the ritual machinery as it goes; the engine is pure "
             "institutional politics."),
            ("Is it based on a book?",
             "On Robert Harris's 2016 novel."),
            ("What about the ending?",
             "A genuine twist - widely debated, thematically loaded; worth the "
             "blind watch."),
        ],
    },
    # ---- film batch 16 (2026-09-24): 30 titles - TV giants, anime staples, Bollywood/Nollywood, Chinese blockbusters ----
    "house-of-the-dragon": {
        "verdict": "The prequel that saved the franchise's reputation: House Targaryen "
            "two centuries before Daenerys, tearing itself apart in the Dance of the "
            "Dragons. Fire, blood and succession politics with genuine tragedy at the "
            "centre - Team Black versus Team Green split households worldwide. The "
            "throne is the same; the dragons are many.",
        "faqs": [
            ("Do I need Game of Thrones first?",
             "No - it stands alone 200 years earlier; knowing the later saga only adds "
             "dramatic irony."),
            ("Is it as explicit as Game of Thrones?",
             "Slightly tamer but still adult - political marriages, violence and "
             "succession blood-letting throughout."),
            ("Is the story finished?",
             "No - the Dance of the Dragons continues across new seasons."),
        ],
    },
    "succession": {
        "verdict": "The richest, cruellest family on television: a media titan's "
            "decline sets his children fencing for the throne, and the dialogue is "
            "the sharpest weapon on the network. Four seasons of corporate savagery, "
            "hilarious humiliation and genuine pathos - one of the most awarded "
            "dramas of its era. 'I love you, but you are not serious people.'",
        "faqs": [
            ("How many seasons?",
             "Four (2018-2023), ending deliberately at its peak."),
            ("Did it win the top Emmy?",
             "Yes - Outstanding Drama Series multiple times, plus writing and "
             "acting awards across its run."),
            ("Is it really that profane?",
             "Famously - the insults are legendary; it is as funny as it is brutal."),
        ],
    },
    "severance": {
        "verdict": "The workplace thriller as existential horror: employees surgically "
            "split work-memory from home-memory, and the 'innies' begin asking who "
            "chose this for them. Ben Stiller directs with icy retro elegance - "
            "fluorescent corridors, impossible geometry, and Adam Scott giving the "
            "performance of his career. The most debated cliffhanger of the decade.",
        "faqs": [
            ("Is Severance scary?",
             "It is unsettling rather than gory - corporate dread, mystery-box "
             "revelations and one very wrong hallway."),
            ("Do seasons connect?",
             "Yes - one continuing mystery; the acclaimed second season deepens it."),
            ("Who is behind it?",
             "Ben Stiller directs much of it - his prestige-TV turn surprised "
             "everyone."),
        ],
    },
    "peaky-blinders": {
        "verdict": "Birmingham's finest: a post-war gang family climbs from racecourses "
            "to empire under Tommy Shelby's flat cap and thousand-yard stare. Cillian "
            "Murphy's career-defining cool, a needle-drop soundtrack that shouldn't "
            "work and absolutely does, and six seasons of stylish ambition. 'By order "
            "of the Peaky Blinders.'",
        "faqs": [
            ("Is it based on a real gang?",
             "Loosely - the real Peaky Blinders were a Birmingham urban youth gang; "
             "the Shelby family saga is fiction built on that seed."),
            ("How many seasons?",
             "Six, ending in 2022, with a film continuing the story."),
            ("When does it get good?",
             "Most viewers are hooked within the first two episodes - the pilot is "
             "the template."),
        ],
    },
    "sherlock": {
        "verdict": "The update that made deduction appointment television again: "
            "Cumberbatch's high-functioning sociopath and Freeman's long-suffering "
            "Watson, solving crimes through London's smartphones and blogs. Three "
            "90-minute films per season, all wit and speed - peak-era television "
            "whose final series still divides the fandom.",
        "faqs": [
            ("How many episodes are there?",
             "Thirteen across four seasons, each 90 minutes, plus the Victorian-era "
             "special The Abominable Bride."),
            ("Do I need to watch in order?",
             "Yes - the arcs build; start at A Study in Pink."),
            ("Why do fans argue about the ending?",
             "Season four's tonal swings split viewers - the earlier seasons are the "
             "consensus gold."),
        ],
    },
    "money-heist": {
        "verdict": "The Spanish heist that conquered the world: the Professor's "
            "impossibly intricate plan, eight robbers named after cities, and 'Bella "
            "Ciao' echoing through the Royal Mint. Started as a modest Spanish "
            "series, became Netflix's global phenomenon - pure antihero catnip with "
            "twists by the truckload.",
        "faqs": [
            ("What order do I watch Money Heist?",
             "Parts 1-5 in order - one continuous story; the Berlin prequel spin-off "
             "comes after."),
            ("Is it as good as the hype?",
             "It is melodramatic, ridiculous and utterly moreish - the most-watched "
             "non-English series of its era for a reason."),
            ("Is it subtitled?",
             "Spanish audio with subtitles (dubs available) - the original voices "
             "are the preferred experience."),
        ],
    },
    "my-hero-academia": {
        "verdict": "The superhero shonen of its generation: a quirkless boy inherits "
            "the greatest power of all and enrols in hero school - and the genre's "
            "brightest franchise balances tournament spectacle with genuine moral "
            "weight. Deku's journey, All Might's legacy, and a class of characters "
            "the internet adopted wholesale.",
        "faqs": [
            ("Is My Hero Academia finished?",
             "The manga has concluded; the anime adapts the final arcs in its later "
             "seasons."),
            ("How many seasons?",
             "Seven-plus and counting to the finale - long-haul shonen."),
            ("Do I start at episode one?",
             "Yes - the origin is the emotional engine."),
        ],
    },
    "one-punch-man": {
        "verdict": "The superhero parody that out-heroed its heroes: Saitama trains "
            "until he can end any fight with one punch - and finds existence "
            "devastatingly boring. Season one's animation became legend; the joke "
            "hides a genuinely sharp satire of power and recognition.",
        "faqs": [
            ("Which season is the famous one?",
             "Season one - its fight animation is still a benchmark; later seasons "
             "trade studios and polish."),
            ("Is it a comedy?",
             "Primarily, with real action chops - the parody is the engine."),
            ("Is it still ongoing?",
             "Yes - new seasons continue adapting the webcomic-turned-manga."),
        ],
    },
    "spy-x-family": {
        "verdict": "The found-family phenomenon: a master spy builds a fake family "
            "for a mission - not knowing his wife is an assassin and his daughter "
            "reads minds. Anya steals the planet, the comedy is warm and constant, "
            "and the world's most dysfunctional functional household became anime's "
            "coziest hit.",
        "faqs": [
            ("Is Spy x Family good for kids?",
             "Largely yes - it is one of the most family-friendly hit anime; mild "
             "violence only."),
            ("Is the story finished?",
             "No - new seasons continue the manga's missions."),
            ("Who is the fan favourite?",
             "Anya - the telepathic child whose reactions became a global meme "
             "library."),
        ],
    },
    "hunter-x-hunter": {
        "verdict": "The shonen that plays chess while others play checkers: Gon's "
            "quest to find his father builds a world of Nen abilities so logically "
            "rigorous that its battles feel like duels of ideas. The 2011 series is "
            "the definitive version - and the Chimera Ant arc is one of the "
            "medium's greatest achievements.",
        "faqs": [
            ("2011 or the 1999 version?",
             "The 2011 adaptation - it covers the full story arc and is the "
             "consensus entry point."),
            ("Why do fans consider it a masterpiece?",
             "Its power system and arcs - especially Chimera Ant - trade formulas "
             "for genuine moral complexity."),
            ("Is the manga still going?",
             "Infamously on-and-off - long hiatuses between comeback runs."),
        ],
    },
    "steins-gate": {
        "verdict": "The time-travel tragedy that earns every feeling: a self-styled "
            "mad scientist's microwave starts texting the past, and each 'correction' "
            "pulls his friends deeper into catastrophe. Slow-burn first half, "
            "devastating second - the gold standard of puzzle-box anime, with an "
            "ending that pays off everything. El Psy Kongroo.",
        "faqs": [
            ("Does the slow start matter?",
             "Completely - the early episodes plant every payoff; push through and "
             "the back half detonates."),
            ("What do I watch after?",
             "The OVA and movie, then Steins;Gate 0 - the darker alternate route."),
            ("Is it based on a game?",
             "Yes - the acclaimed visual novel; the anime is the popular entry."),
        ],
    },
    "fairy-tail": {
        "verdict": "The guild-as-family shonen: dragon-slayer Natsu and the loudest "
            "wizard guild in fiction smash their way through quests, tournaments and "
            "dark guilds with friendship as literal power source. Nearly 300 "
            "episodes of comfort-food magic - predictable, warm and proud of it.",
        "faqs": [
            ("How long is Fairy Tail?",
             "278 episodes across its run, plus the 100 Years Quest continuation "
             "series."),
            ("Is it good for younger viewers?",
             "Teens and up - fanservice and battle violence keep it out of the "
             "young-kids slot."),
            ("Do I need anything before it?",
             "No - it stands alone; Hiro Mashima's earlier Rave Master is a bonus "
             "for completionists."),
        ],
    },
    "dragon-ball-super": {
        "verdict": "The legend's next chapter: gods of destruction, universes at "
            "stake, and Goku reaching divinity while staying gloriously Goku. "
            "Super modernised the franchise for a new generation - its tournaments "
            "(Universe 6, Tournament of Power) delivered the freshest fights since "
            "the Cell Games.",
        "faqs": [
            ("Do I watch DBZ first?",
             "Yes - Super continues after the Buu saga; the Battle of Gods and "
             "Resurrection F films are folded into its early episodes."),
            ("How many episodes?",
             "131, plus the Broly and Super Hero films continuing the story in "
             "cinema."),
            ("Is the story finished?",
             "The anime paused after the Tournament of Power; the manga continues "
             "new arcs."),
        ],
    },
    "the-housemaid-2025": {
        "verdict": "The bestseller thriller done as star-powered cinema: a young "
            "woman with a record takes a live-in housekeeping job for a wealthy "
            "family whose perfect home is a locked box of secrets. Paul Feig swaps "
            "comedy for tension and delivers the domestic-gone-wrong escalation "
            "readers loved on the page. Convenience, closets and very bad employers.",
        "faqs": [
            ("Is The Housemaid based on a book?",
             "Yes - Freida McFadden's bestselling thriller novel; the adaptation "
             "was a major 2025 release."),
            ("Is it a horror film?",
             "Psychological thriller - menace and twists rather than the "
             "supernatural."),
            ("How long is it?",
             "131 minutes."),
        ],
    },
    "fifty-shades-of-grey": {
        "verdict": "The literary phenomenon that became a cinematic one: a naive "
            "student and a billionaire with a very specific contract. As culture, "
            "enormous; as film, a fascinating artifact of its moment - the trilogy "
            "grossed over a billion dollars worldwide and owned the 2015-18 "
            "conversation. Whatever the reviews said, everyone watched.",
        "faqs": [
            ("Is Fifty Shades based on a book?",
             "Yes - E L James's novel, which began life as fan fiction and became "
             "one of the fastest-selling books of its decade."),
            ("How many films are there?",
             "Three - Fifty Shades of Grey, Darker and Freed."),
            ("Is it explicit?",
             "Yes - the adult content is the franchise's whole billing; R-rated "
             "throughout."),
        ],
    },
    "freakier-friday": {
        "verdict": "The body-swap classic, generations later: Tess and Anna return - "
            "and the swap goes sideways again with a new generation in the mix. "
            "Jamie Lee Curtis and Lindsay Lohan's reunion gives the film its heart, "
            "and the nostalgia math adds up to one of 2025's warmest crowd-pleasers.",
        "faqs": [
            ("Do I need the 2003 film first?",
             "Yes - the whole point is the reunion; watch Freaky Friday (2003) "
             "first."),
            ("Is it good for family viewing?",
             "Yes - that is the assignment, and it lands."),
            ("How long is it?",
             "111 minutes."),
        ],
    },
    "devara-part-1": {
        "verdict": "Telugu spectacle at full sail: a coastal chieftain who forbids "
            "the sea-trade violence his people ran on, a son raised in his shadow, "
            "and Jr NTR carrying both weight and myth through mass-action "
            "choreography of the biggest kind. Part one of a planned saga - and a "
            "box-office storm on release.",
        "faqs": [
            ("Is Devara connected to RRR?",
             "Different film - but the same school of maximalist Telugu action, and "
             "the same superstar anchor in Jr NTR."),
            ("Do I need it before part two?",
             "It is part one of the story - the sequel continues it."),
            ("How long is it?",
             "178 minutes."),
        ],
    },
    "bhool-bhulaiyaa-3": {
        "verdict": "The horror-comedy franchise's biggest swing: Rooh Baba returns "
            "to a haunted palace where the original's legendary Manjulika presides - "
            "and the film gleefully mixes jumpscares, dance numbers and genuine "
            "lore. The Diwali blockbuster slot does not miss twice; this one "
            "delivered the goods for the fandom.",
        "faqs": [
            ("Do I need the earlier films?",
             "It helps - the 2007 original and Bhool Bhulaiyaa 2 seed the mythology "
             "and the jokes."),
            ("Is it scary or funny?",
             "Both by design - the franchise's signature blend of horror beats and "
             "comedy relief."),
            ("How long is it?",
             "158 minutes."),
        ],
    },
    "dhoom-3": {
        "verdict": "India's motorcycle-franchise goes operatic: Aamir Khan's "
            "circus-performer thief turns Chicago into a stage for revenge, and the "
            "YRF machine delivers stunts, twists and twin-led spectacle. One of the "
            "highest-grossing Indian films of its era - the popcorn event that "
            "defined the franchise's peak scale.",
        "faqs": [
            ("Do I need Dhoom 1 and 2 first?",
             "Not strictly - the villain plots are standalone; the franchise "
             "formula is the connective tissue."),
            ("Is it the best Dhoom?",
             "Fans split between this and Dhoom 2 - this one has the scale and the "
             "twist."),
            ("How long is it?",
             "172 minutes."),
        ],
    },
    "awarapan": {
        "verdict": "The cult gangster tragedy that grew into a religion: Emraan "
            "Hashmi's mob enforcer - hollowed out by loss - finds one last chance "
            "at grace protecting a woman he cannot save. Mohit Suri's most soulful "
            "film; dismissed in 2007, revered a decade later. 'Jabse tere naina' "
            "still stops rooms.",
        "faqs": [
            ("Why is Awarapan a cult classic?",
             "Its sincerity - a gangster film about redemption that plays like a "
             "spiritual tragedy; word of mouth made it beloved years on."),
            ("Is there a sequel?",
             "A follow-up has been long discussed; this 2007 film stands complete "
             "on its own."),
            ("What is it rated?",
             "Adult-themed crime drama - violence and tragedy throughout."),
        ],
    },
    "udaan": {
        "verdict": "The coming-of-age that cut Hindi cinema's nerve: a teenager "
            "expelled from boarding school returns to the father who owns him - and "
            "slowly, quietly plans his flight. Vikramaditya Motwane's debut premiered "
            "at Cannes and remains one of Indian cinema's finest films about young "
            "men and their fathers. Restraint as thunder.",
        "faqs": [
            ("Is Udaan based on a true story?",
             "It is fiction, drawn from recognisable middle-India family dynamics - "
             "which is why it feels documentary-true."),
            ("Why is it so highly rated?",
             "Cannes recognition plus a generational performance from Rajat "
             "Barmecha - the film that announced Motwane."),
            ("How long is it?",
             "138 minutes."),
        ],
    },
    "bad-newz": {
        "verdict": "The wildest high-concept comedy of its year: a woman discovers "
            "her pregnancy is twins - by two different fathers - and the two "
            "would-be dads move in to compete. Vicky Kaushal's comic timing is a "
            "revelation, and the film rides its absurd premise with actual heart. "
            "Heteropaternal superfecundation has never been this funny.",
        "faqs": [
            ("Is Bad Newz a sequel?",
             "It follows the spirit of Good Newwz (2019) with a new story and cast - "
             "no prior viewing needed."),
            ("Is the twin premise medically real?",
             "Yes - heteropaternal superfecundation exists; the film just takes it "
             "to comedy court."),
            ("How long is it?",
             "140 minutes."),
        ],
    },
    "dhurandhar": {
        "verdict": "The event film of its moment: Aditya Dhar's sprawling spy-action "
            "epic runs three and a half hours - 214 minutes - of undercover warfare "
            "and star power, and audiences showed up in force. Divisive in tone, "
            "immense in scale, impossible to ignore: the conversation-piece Hindi "
            "blockbuster of its year.",
        "faqs": [
            ("Is Dhurandhar really 214 minutes?",
             "Yes - one of the longest mainstream Hindi action films ever released; "
             "clear the evening."),
            ("Who made it?",
             "Aditya Dhar, following his Uri: The Surgical Strike phenomenon."),
            ("Is it based on true events?",
             "It borrows the texture of real covert operations while playing as "
             "heightened fiction."),
        ],
    },
    "breaded-life": {
        "verdict": "The Lagos comedy with a soul: a spoiled bakery heir's life "
            "collapses until he wakes up invisible to everyone except the woman he "
            "cheated - and the redemption run becomes a genuine spiritual comedy. "
            "Biodun Stephen's warmest, most rewatchable film - Nollywood "
            "comfort-food with real feeling underneath.",
        "faqs": [
            ("Is Breaded Life a comedy or a drama?",
             "Both - the fantasy premise plays funny while the redemption arc plays "
             "sincere."),
            ("Is it connected to other Biodun Stephen films?",
             "It shares her universe's warmth and Lagos texture; it stands alone."),
            ("How long is it?",
             "120 minutes."),
        ],
    },
    "brotherhood": {
        "verdict": "Lagos crime saga at blockbuster scale: twin brothers end up on "
            "opposite sides of the law, and the city's underworld collects its "
            "debts. Glossy, gun-heavy and emotionally blunt - one of the films that "
            "proved Nigerian cinema could do the big-scale crime thriller "
            "confidently.",
        "faqs": [
            ("Who made Brotherhood?",
             "It was directed by Loukman Ali - part of the wave of ambitious "
             "big-canvas Nollywood crime films."),
            ("Is there a sequel?",
             "Yes - Brotherhood 2 continued the story."),
            ("How long is it?",
             "A feature-length crime epic - check the page details for the exact "
             "runtime."),
        ],
    },
    "the-milkmaid": {
        "verdict": "Nigeria's prestige entry to the world stage: a Hausa-language "
            "drama of abduction, radicalisation and the sister who walks into the "
            "wilderness to bring her home. Desmond Ovbiagele's film was selected as "
            "Nigeria's submission for the Oscars' international category - stark, "
            "beautiful and quietly furious.",
        "faqs": [
            ("What language is The Milkmaid in?",
             "Primarily Hausa - a landmark for northern Nigerian stories on the "
             "international stage."),
            ("Was it really an Oscar submission?",
             "Yes - Nigeria selected it as its entry for the international feature "
             "film category."),
            ("Is it heavy?",
             "Yes - it deals with insurgency and its victims with seriousness; "
             "worth the weight."),
        ],
    },
    "citizen-vigilante": {
        "verdict": "A compact vigilante thriller from an unexpected corner: Uwe "
            "Boll - the German director famous for his video-game adaptations - "
            "delivers an 89-minute tale of one person deciding the courts are too "
            "slow. Lean, mean, and built for the direct-to-audience action crowd.",
        "faqs": [
            ("Who directed Citizen Vigilante?",
             "Uwe Boll - a surprise genre entry from the notorious German "
             "filmmaker."),
            ("How long is it?",
             "89 minutes - a tight single-sitting thriller."),
            ("Is it connected to any franchise?",
             "No - a standalone vigilante story."),
        ],
    },
    "wandering-earth-2": {
        "verdict": "The prequel that out-grew its giant: how humanity decided to "
            "move the planet - the politics, the moon crisis, the digital-life "
            "debate - staged at jaw-dropping scale. Frant Gwo's prequel became one "
            "of the biggest Chinese films ever and a landmark of the country's "
            "sci-fi cinema. The plan, the sacrifice, the engines.",
        "faqs": [
            ("Prequel or sequel - what order?",
             "Watch this first if you want chronology - it is a prequel to The "
             "Wandering Earth (2019); either order works."),
            ("Is it as good as the first?",
             "Many rate it higher - bigger ideas, bigger set pieces, longer "
             "runtime."),
            ("How long is it?",
             "173 minutes."),
        ],
    },
    "wolf-warrior-2": {
        "verdict": "The film that redefined Chinese box office: a retired special "
            "forces soldier defends African civilians from mercenaries, and Wu "
            "Jing's patriotic action epic became the highest-grossing Chinese film "
            "in history - a record it held for years. Tank vs shark-duel energy; "
            "pure national-cinema muscle.",
        "faqs": [
            ("Do I need the first Wolf Warrior?",
             "No - this one restarts the hero's story in Africa; it stands alone."),
            ("Is it really that big a deal in China?",
             "Enormous - it topped China's all-time box office for years and became "
             "a cultural phenomenon."),
            ("How long is it?",
             "126 minutes."),
        ],
    },
    "28-years-later-the-bone-temple": {
        "verdict": "The rage saga continues: Nia DaCosta takes the baton from Danny "
            "Boyle for the second chapter of the new trilogy, following the "
            "bone-temple cult and the warlord world growing in the infected wilds. "
            "Where 28 Years Later was pilgrimage, this is aftermath - and the "
            "trilogy's dark middle book.",
        "faqs": [
            ("Do I need 28 Years Later (2025) first?",
             "Yes - it is a direct continuation; start with 28 Days Later if "
             "you are brand new."),
            ("Is Danny Boyle involved?",
             "He directed the first film of the trilogy; Nia DaCosta directs this "
             "chapter."),
            ("Is the trilogy complete?",
             "No - a third film is planned to close the arc."),
        ],
    },
}
