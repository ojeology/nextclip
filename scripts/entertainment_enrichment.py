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
}
