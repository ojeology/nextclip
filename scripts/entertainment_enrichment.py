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
}
