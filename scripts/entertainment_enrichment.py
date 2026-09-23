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
}
