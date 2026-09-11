# BRYME Entertainment — the catalogue (batch 22, 11 Sep 2026).
# House rule: every entry links ONLY to pages that genuinely discuss the title
# (verified against page text at build time — the build fails if a link lies).
# Shelf order follows the desk's request: fantasy, anime, kdrama — then more.

CATALOGUE_SHELVES = [
("fantasy", "Fantasy &amp; Sci-Fi",
"Big worlds, bigger ideas — every film here is argued about somewhere on this desk.",
[
 ("Interstellar", "2014", "Film", "Time, gravity and the price of a promise — the ending the desk keeps defending.", ["movies-like-interstellar-guide", "7-movies-we-wished-never-ended"]),
 ("Arrival", "2016", "Film", "First contact as a language puzzle — the patient sibling of the Interstellar picks.", ["movies-like-interstellar-guide", "dune-sci-fi-epics-guide"]),
 ("Dune: Part Two", "2024", "Film", "Villeneuve's sandworm epic, and why the scale finally feels earned.", ["dune-sci-fi-epics-guide", "7-movies-we-wished-never-ended"]),
 ("Blade Runner 2049", "2017", "Film", "The same patient, enormous-screen visual language as the modern Dune films.", ["dune-sci-fi-epics-guide", "movies-like-interstellar-guide"]),
 ("Alien", "1979", "Film", "The haunted house in space — the franchise in viewing order on the desk.", ["alien-franchise-in-order"]),
]),
("anime", "Anime",
"From entry points to the long-runners — with the vocabulary to argue about them properly.",
[
 ("Solo Leveling", "2024", "Anime", "From E-rank joke to system-wielder — the rise that spawned a wave.", ["solo-leveling-e-rank-to-s-rank", "10-anime-like-solo-leveling-you-should-watch", "solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences"]),
 ("Frieren: Beyond Journey's End", "2023", "Anime", "The quiet masterpiece about what happens after the quest.", ["best-anime-to-watch-now"]),
 ("One Piece", "1999", "Anime", "The longest voyage in shonen — does the journey justify the runtime?", ["one-piece-vs-naruto", "best-anime-to-watch-now"]),
 ("Naruto", "2002", "Anime", "The ninja epic on the other side of the desk's biggest head-to-head.", ["one-piece-vs-naruto", "best-anime-to-watch-now"]),
 ("Hunter x Hunter", "2011", "Anime", "Gon's journey and the Chimera Ant peak — the other half of the Solo Leveling comparison.", ["solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences", "10-anime-like-solo-leveling-you-should-watch"]),
 ("Attack on Titan", "2013", "Anime", "Was Eren really the villain? The desk takes the question seriously.", ["was-eren-yeager-really-the-villain"]),
 ("Jujutsu Kaisen", "2020", "Anime", "Cursed energy, style to spare — a modern shonen benchmark.", ["10-anime-like-solo-leveling-you-should-watch", "best-anime-to-watch-now"]),
 ("Demon Slayer", "2019", "Anime", "One of animation's prettiest sword systems, and a brother to save.", ["10-anime-like-solo-leveling-you-should-watch"]),
 ("Spirited Away", "2001", "Anime film", "Miyazaki's spirit-world bathhouse — one more scene, forever.", ["7-movies-we-wished-never-ended", "how-to-pick-a-movie-tonight"]),
 ("Your Name", "2016", "Anime film", "The comet, the stairs, the question — the film that converts non-anime viewers.", ["7-movies-we-wished-never-ended"]),
]),
("kdrama", "K-Drama &amp; Korean screen",
"Series and cinema from the desk's deepest shelf — gateway route included.",
[
 ("Squid Game", "2021", "K-drama", "Why season 1 became a global phenomenon — and Agent Kim's season-3 file.", ["squid-game-season-1-why-it-became-a-global-phenomenon", "10-facts-about-agent-kim-squid-game-season-3", "alice-in-borderland-vs-squid-game"]),
 ("Parasite", "2019", "Korean film", "Bong Joon-ho's staircase comedy-thriller that rewrote the Oscar conversation.", ["10-korean-movies-everyone-should-watch", "korean-cinema-starter-guide-rebuilt", "movies-like-parasite"]),
 ("Memories of Murder", "2003", "Korean film", "The serial-killer procedural that started the Bong dynasty argument.", ["10-korean-movies-everyone-should-watch", "korean-cinema-starter-guide-rebuilt"]),
 ("Oldboy", "2003", "Korean film", "The revenge landmark — corridor fight included.", ["10-korean-movies-everyone-should-watch", "korean-cinema-starter-guide-rebuilt"]),
 ("The Handmaiden", "2016", "Korean film", "Park Chan-wook's most beautiful con, in three acts.", ["10-korean-movies-everyone-should-watch", "korean-cinema-starter-guide-rebuilt"]),
 ("Burning", "2018", "Korean film", "The slow-burn mystery that ends on cinema's great unanswered question.", ["10-korean-movies-everyone-should-watch", "korean-cinema-starter-guide-rebuilt"]),
 ("Train to Busan", "2016", "Korean film", "The zombie train that outruns its own genre.", ["10-korean-movies-everyone-should-watch", "korean-cinema-starter-guide-rebuilt"]),
 ("Snowpiercer", "2013", "Korean film", "Class war on rails, in carriage order.", ["10-korean-movies-everyone-should-watch"]),
 ("The Host", "2006", "Korean film", "The creature feature that is really about a family — and a river.", ["10-korean-movies-everyone-should-watch", "korean-cinema-starter-guide-rebuilt"]),
]),
("more", "Thrillers, horror &amp; everything else",
"The rest of the covered catalogue — box-set television, modern horror, world cinema.",
[
 ("Breaking Bad", "2008", "Series", "Two seasons in, still the best argument on television.", ["breaking-bad-two-seasons-opinion"]),
 ("Prison Break", "2005", "Series", "Season one in one sitting — and why it still holds.", ["why-prison-break-season-1-is-still-one-of-the-best-tv-seasons"]),
 ("Alice in Borderland", "2020", "J-drama", "The death-game cousin of Squid Game — and how they really compare.", ["10-shows-like-alice-in-borderland-you-should-watch-next", "alice-in-borderland-vs-squid-game"]),
 ("Into the Badlands", "2015", "Series", "The underrated martial-arts western the desk defends without irony.", ["into-the-badlands-was-underrated"]),
 ("Deadpool &amp; Wolverine", "2024", "Film", "The cameo carnival that broke the internet's rules on purpose.", ["movies-like-deadpool-and-wolverine", "5-movies-that-broke-the-internet"]),
 ("Oppenheimer", "2023", "Film", "Nolan's three-hour dialogue bomb — where it sits in the viewing order.", ["christopher-nolan-movies-order", "5-movies-that-broke-the-internet"]),
 ("The Dark Knight", "2008", "Film", "Not science fiction, but pure Nolan craft — the character entry in the order.", ["christopher-nolan-movies-order"]),
 ("Get Out", "2017", "Horror", "A smart first door into modern horror — thriller bones, social teeth.", ["modern-horror-starter-route"]),
 ("A Quiet Place", "2018", "Horror", "Silence and attention turned into the main source of pressure.", ["modern-horror-starter-route"]),
 ("Hereditary", "2018", "Horror", "Grief as horror — the route's heavy lift, and worth it.", ["modern-horror-starter-route"]),
 ("Midsommar", "2019", "Horror", "Daylight horror — the breakup film wearing a flower crown.", ["modern-horror-starter-route"]),
 ("Let the Right One In", "2008", "Horror", "The Swedish masterpiece that made vampires lonely again.", ["modern-horror-starter-route"]),
 ("Interview with the Vampire", "1994", "Horror", "Vampires as tragic, gorgeous rock stars — the gothic romance era begins here.", ["modern-horror-starter-route"]),
 ("RRR", "2022", "Indian cinema", "The maximalist action anthem — the Indian starter five begins with scale.", ["indian-cinema-first-five"]),
 ("Dangal", "2016", "Indian cinema", "Wrestling, daughters, and grounded pressure over spectacle.", ["indian-cinema-first-five"]),
]),
]

# per-shelf desk guides, listed under the tiles
CATALOGUE_SHELF_FOOTERS = {
 "fantasy": [("dune-sci-fi-epics-guide", "The Dune & sci-fi epics guide"), ("christopher-nolan-movies-order", "Nolan in order"), ("alien-franchise-in-order", "Alien in order")],
 "anime": [("best-anime-to-watch-now", "The best anime to watch now"), ("anime-canon-and-filler-explained", "Canon & filler, explained"), ("anime-seasons-and-cours-explained", "Seasons & cours, explained")],
 "kdrama": [("best-kdramas-to-start-with", "The K-drama starter route"), ("korean-cinema-starter-guide-rebuilt", "Korean cinema starter guide"), ("10-korean-movies-everyone-should-watch", "Ten Korean films")],
 "more": [("modern-horror-starter-route", "The modern horror starter route"), ("nigerian-thrillers-worth-your-time", "Nigerian thrillers worth your time"), ("5-movies-that-broke-the-internet", "Five movies that broke the internet")],
}
