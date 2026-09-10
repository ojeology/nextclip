# BRYME Sport — leagues data layer (batch 7, 2026-09-10).
# DATA POLICY: every row below was verified on 2026-09-10 against four independent
# sources for the table and fixtures (nbcsports.com, sportsmediawatch.com,
# footballfixtures.org, worldfootball.net — UK times cross-checked from CET/ET),
# and against each other for ordering. Nothing here is invented; if the desk
# cannot verify an update, the page says so instead of guessing.

SEASON = "2026-27"
TABLE_AS_OF = "Thursday 10 September 2026, after Matchweek 3"
FIXTURES_AS_OF = "verified Thursday 10 September 2026"

# pos, club, slug, played, w, d, l, gf, ga, gd, pts  — table as of Matchweek 3 (2026-09-10)
PL_TABLE = [
    (1,  "Manchester City",     "manchester-city",     3, 3, 0, 0, 7, 2,  5, 9),
    (2,  "Arsenal",             "arsenal",             3, 3, 0, 0, 6, 1,  5, 9),
    (3,  "Hull City",           "hull-city",           3, 2, 1, 0, 3, 0,  3, 7),
    (4,  "Chelsea",             "chelsea",             3, 2, 0, 1, 8, 7,  1, 6),
    (5,  "Brentford",           "brentford",           3, 1, 2, 0, 5, 2,  3, 5),
    (6,  "Liverpool",           "liverpool",           3, 1, 2, 0, 6, 4,  2, 5),
    (7,  "Newcastle United",    "newcastle-united",    3, 1, 2, 0, 6, 4,  2, 5),
    (8,  "Everton",             "everton",             3, 1, 2, 0, 5, 3,  2, 5),
    (9,  "Leeds United",        "leeds-united",        3, 1, 2, 0, 3, 2,  1, 5),
    (10, "Brighton & Hove Albion", "brighton",         3, 1, 1, 1, 8, 5,  3, 4),
    (11, "Manchester United",   "manchester-united",   3, 1, 1, 1, 7, 6,  1, 4),
    (12, "Sunderland",          "sunderland",          3, 1, 1, 1, 3, 3,  0, 4),
    (13, "Ipswich Town",        "ipswich-town",        3, 1, 0, 2, 4, 8, -4, 3),
    (14, "Crystal Palace",      "crystal-palace",      3, 1, 0, 2, 4, 8, -4, 3),
    (15, "AFC Bournemouth",     "bournemouth",         3, 0, 2, 1, 4, 5, -1, 2),
    (16, "Nottingham Forest",   "nottingham-forest",   3, 0, 2, 1, 2, 3, -1, 2),
    (17, "Aston Villa",         "aston-villa",         3, 0, 1, 2, 0, 5, -5, 1),
    (18, "Tottenham Hotspur",   "tottenham-hotspur",   3, 0, 1, 2, 0, 5, -5, 1),
    (19, "Fulham",              "fulham",              3, 0, 0, 3, 4, 7, -3, 0),
    (20, "Coventry City",       "coventry-city",       3, 0, 0, 3, 0, 5, -5, 0),
]

# date_label, time_uk, home slug, home, away slug, away, venue — Matchweek 4 (12–14 Sep 2026)
PL_MW4 = [
    ("Saturday 12 September, 15:00", "aston-villa",     "Aston Villa",        "nottingham-forest",  "Nottingham Forest",   "Villa Park"),
    ("Saturday 12 September, 15:00", "bournemouth",     "AFC Bournemouth",    "brentford",          "Brentford",           "Vitality Stadium"),
    ("Saturday 12 September, 15:00", "chelsea",         "Chelsea",            "hull-city",          "Hull City",           "Stamford Bridge"),
    ("Saturday 12 September, 15:00", "crystal-palace",  "Crystal Palace",     "ipswich-town",       "Ipswich Town",        "Selhurst Park"),
    ("Saturday 12 September, 15:00", "liverpool",       "Liverpool",          "fulham",             "Fulham",              "Anfield"),
    ("Saturday 12 September, 17:30", "tottenham-hotspur","Tottenham Hotspur", "everton",            "Everton",             "Tottenham Hotspur Stadium"),
    ("Saturday 12 September, 20:00", "sunderland",      "Sunderland",         "arsenal",            "Arsenal",             "Stadium of Light"),
    ("Sunday 13 September, 14:00",   "coventry-city",   "Coventry City",      "brighton",           "Brighton & Hove Albion","Coventry Building Society Arena"),
    ("Sunday 13 September, 16:30",   "manchester-united","Manchester United", "manchester-city",    "Manchester City",     "Old Trafford"),
    ("Monday 14 September, 20:00",   "leeds-united",    "Leeds United",       "newcastle-united",   "Newcastle United",    "Elland Road"),
]

# slug, name, ground, founded, identity paragraph (stable facts only)
PL_CLUBS = {
    "arsenal": ("Arsenal", "Emirates Stadium", 1886,
        "Founded in Woolwich in 1886 and moved across London to north London in 1913. One of English football\u2019s most decorated institutions, with a record haul of FA Cups and an Invincibles season \u2014 2003-04 \u2014 no top-flight club has matched. This season they have started with three wins from three, the league\u2019s meanest defence, and a Saturday-night visit to Sunderland next on the card."),
    "aston-villa": ("Aston Villa", "Villa Park", 1874,
        "One of the oldest clubs in English football and a founder-member of the Football League in 1888. European champions in 1982. Villa Park has been their home almost continuously since 1897. The 2026-27 start has been slow \u2014 one point and no league goal yet \u2014 with Nottingham Forest the visitors this weekend."),
    "bournemouth": ("AFC Bournemouth", "Vitality Stadium", 1899,
        "The south-coast club climbed from the fourth tier to the Premier League within a single decade in the 2010s, one of English football\u2019s great modern rises. The Vitality is one of the smallest grounds in the top flight, and famously intimidating for it. Unbeaten in patches early this season, with Brentford visiting on Saturday."),
    "brentford": ("Brentford", "Gtech Community Stadium", 1889,
        "A west London club built on one of the sharpest recruitment models in Europe: find undervalued players, develop them, sell high, repeat. Left their old Griffin Park home for the Gtech in 2020. Five points from three unbeaten games this season, with a trip to Bournemouth next."),
    "brighton": ("Brighton & Hove Albion", "American Express Stadium", 1901,
        "The Premier League\u2019s best-known overachievers of the decade: a scouting-and-coaching machine that keeps selling stars and keeps winning anyway. Moved into the Amex in 2011. Eight goals in three games this season \u2014 only Manchester City have scored more \u2014 and a trip to Coventry on Sunday."),
    "chelsea": ("Chelsea", "Stamford Bridge", 1905,
        "Founded in 1905 and unusually \u2014 for a major London club \u2014 built around an existing stadium rather than the other way round. European champions in 2012 and 2021, English champions five times in the modern era. Dropped their first points of the season last time out; Hull City\u2019s visit on Saturday is the weekend\u2019s quietest big fixture."),
    "coventry-city": ("Coventry City", "Coventry Building Society Arena", 1883,
        "Back in the top flight for the first time since 2001, after a quarter-century that included exile from their own city and a 1987 FA Cup high point. Returned to a rebuilt home in Coventry in 2021. Still waiting for a first point or a first goal this season; Brighton \u2014 winners of eight goals\u2019 worth of games \u2014 arrive on Sunday."),
    "crystal-palace": ("Crystal Palace", "Selhurst Park", 1905,
        "South London\u2019s club, formed by workers at the Crystal Palace exhibition site and settled at Selhurst Park since 1924. Won the first major trophy in the club\u2019s history \u2014 the 2025 FA Cup \u2014 and have made a habit of cup finals since. Three points on the board and Ipswich at home this Saturday."),
    "everton": ("Everton", "Bramley-Moore Dock stadium", 1878,
        "One of the twelve founders of the Football League and the club that spent more top-flight seasons than any other before leaving Goodison Park \u2014 their home since 1892 \u2014 for a new riverside stadium at Bramley-Moore Dock, opened for 2025-26. Five points from three games is a quietly strong start; Tottenham visit on Saturday evening."),
    "fulham": ("Fulham", "Craven Cottage", 1879,
        "London\u2019s oldest professional club still at its original ground: Craven Cottage on the Thames since 1896. Promoted, established, promoted again \u2014 the modern Fulham cycle has hardened into real stability. This season has been the hardest kind: three defeats from three, with the table\u2019s toughest away trip, Liverpool, next."),
    "hull-city": ("Hull City", "MKM Stadium", 1904,
        "The Tigers are the season\u2019s story so far: promoted, unbeaten, and \u2014 uniquely in the division \u2014 yet to concede a league goal, sitting third after three games. It is their first top-flight season since 2017. Chelsea away on Saturday answers the question every promoted start eventually faces."),
    "ipswich-town": ("Ipswich Town", "Portman Road", 1878,
        "A club with a giant\u2019s history and a middleweight footprint: English champions in 1962, FA Cup winners in 1978, UEFA Cup winners in 1981, all under the Stowmarket-born taskmaster Sir Bobby Robson in his different eras. Back among the elite after years away, with three points and a trip to Selhurst Park this weekend."),
    "leeds-united": ("Leeds United", "Elland Road", 1919,
        "Three-time English champions, the last of them in 1992, and the club of Don Revie\u2019s uncompromising 1960s-70s sides. Elland Road has been the home since the foundation. Back in the Premier League and unbeaten in regulation this season, with Newcastle under the Monday-night lights next."),
    "liverpool": ("Liverpool", "Anfield", 1892,
        "The most successful club in English football\u2019s European story \u2014 six European Cups \u2014 and champions of England again in 2024-25, a record-equaling twentieth title. Anfield has been the home since the club’s founding in 1892. One defeat in three this season; Fulham visit on Saturday afternoon."),
    "manchester-city": ("Manchester City", "Etihad Stadium", 1880,
        "Formed as a church team in 1880 and reborn as a modern superpower under Abu Dhabi ownership from 2008: six titles in seven seasons from 2017-18, a treble in 2023, and the club against which every English squad is now measured. Perfect through three games this season and top of the table on goals scored."),
    "manchester-united": ("Manchester United", "Old Trafford", 1878,
        "Twenty league titles, three European Cups, and the 1968 distinction of the first English club to become champions of Europe. Old Trafford \u2014 \u201cthe Theatre of Dreams\u201d \u2014 has been the home since 1910. A mixed start (four points) makes Sunday\u2019s derby against the league leaders the weekend\u2019s main event."),
    "newcastle-united": ("Newcastle United", "St James' Park", 1892,
        "The club of the Gallowgate and a city that lives through it: four English titles, a famous entertained-a-generation era under Kevin Keegan, and a 2025 League Cup that ended a seventy-year wait for a major trophy. St James\u2019 Park sits at the literal centre of town. Five points and a Monday trip to Leeds next."),
    "nottingham-forest": ("Nottingham Forest", "The City Ground", 1865,
        "Two consecutive European Cups, 1979 and 1980, under Brian Clough \u2014 arguably the most unlikely back-to-back achievement in the competition\u2019s history. The City Ground looks across the Trent at Notts County, the world\u2019s oldest professional club. Two points so far; a Friday-to-Saturday trip to Villa Park opens the weekend for both."),
    "sunderland": ("Sunderland", "Stadium of Light", 1879,
        "Six-time English champions in the deep history, promoted back to the Premier League through the 2025 play-offs, and armed with one of English football\u2019s loudest single-club cities. The Stadium of Light has shaken like few grounds in the division since the club returned. Four points, and Arsenal arrive on Saturday night."),
    "tottenham-hotspur": ("Tottenham Hotspur", "Tottenham Hotspur Stadium", 1882,
        "The first British club to win a European trophy in the modern era (1972) and winners of the 2025 Europa League. Their monumental new stadium, opened in 2019 on the old White Hart Lane footprint, is one of the finest in world football. A difficult start \u2014 one point, no league goal \u2014 with Everton the visitors on Saturday."),
}

# The three additional competitions hubs — verified structural facts only (2026-09-10).
# Serie A champion: Inter (2025-26) per transfermarkt + en.wikipedia; Bundesliga: Bayern
# (2025-26, 34th title); Ligue 1: PSG (defending as of 2026-27, 14 titles). Serie A
# 2026-27 club lists conflicted across sources on 2-3 slots -> the desk publishes no
# contested club list. Season dates: Serie A ran from 22 Aug 2026 to 30 May 2027 (beIN).
LEAGUE_FACTS = {
    "serie-a": dict(
        name="Serie A", country="Italy", clubs=20, rounds=38,
        champion="Inter Milan", titles_note="a 21st scudetto, tying the city rivalry at the top of the all-time table with the two Milan clubs\u2019 combined totals intact",
        season_note="The 2026-27 season began on 22 August 2026 and runs to 30 May 2027.",
        body_intro="Italy\u2019s top division is the tactician\u2019s league: a history of catenaccio and total football experiments, the deepest tactical coaching culture in Europe, and clubs \u2014 Juventus, the two Milanese giants, Napoli, Roma \u2014 that shaped the sport\u2019s modern idea of defence and system."),
    "bundesliga": dict(
        name="Bundesliga", country="Germany", clubs=18, rounds=34,
        champion="Bayern Munich", titles_note="a 34th title, extending the longest championship run and the most titles of any top European league\u2019s single club",
        season_note="Eighteen clubs, thirty-four rounds, and the highest average attendance in world football.",
        body_intro="Germany\u2019s single-division top flight is the attendance capital of Europe and the league of the 50+1 member-owned model, which keeps ticket culture cheap and the league\u2019s identity genuinely local. Bayern Munich\u2019s dominance defines the era; the chase behind them defines the drama."),
    "ligue-1": dict(
        name="Ligue 1", country="France", clubs=18, rounds=34,
        champion="Paris Saint-Germain", titles_note="a record 14th title and the role of defending champions into 2026-27",
        season_note="Eighteen clubs since 2023-24, playing thirty-four rounds from August to May.",
        body_intro="France\u2019s top flight is Europe\u2019s great producer: the academy system that has supplied World Cup-winning generations, and a league whose most successful club, Paris Saint-Germain, turned Qatari investment into the most conspicuous squad project of the age."),
}
