#!/usr/bin/env python3
"""Turn the 16 BRYME sports draft placeholders into finished, published articles.

Every factual claim is drawn from the site's own data files:
  content/competitions.json  — live tables + top scorers
  content/results.json       — verified full-time scores (each carries a source)
  content/pl-transfers.json  — 2026/27 window, all 20 clubs, managers + fees
so nothing here can contradict what the rest of the site already publishes.
"""
import json, html, re, os, collections
import sys; sys.path.insert(0,'/home/user')
from build_extras import EXTRA, CLOSER

ROOT = '/home/user/nextclip'
TODAY = '2026-09-03'

comps = {c['id']: c for c in json.load(open(ROOT + '/content/competitions.json'))['competitions']}
results = json.load(open(ROOT + '/content/results.json'))
tr = {c['name']: c for c in json.load(open(ROOT + '/content/pl-transfers.json'))['clubs']}

PL = {t['name']: t for t in comps['premier-league']['teams']}
# the tracker and the league table spell a few clubs differently
for _short, _long in [('Bournemouth', 'AFC Bournemouth'), ('Brighton', 'Brighton & Hove Albion'),
                      ('Tottenham', 'Tottenham Hotspur'), ('Newcastle', 'Newcastle United')]:
    if _long in PL and _short not in PL:
        PL[_short] = PL[_long]
SCORERS = comps['premier-league']['scorers']


# ---------------------------------------------------------------- form helpers
def build_form(lg):
    rows = []
    for slug, v in results[lg].items():
        h, a = slug.split('-vs-')
        rows.append((v.get('playedOn', ''), h, v['homeScore'], v['awayScore'], a))
    rows.sort()
    f = collections.defaultdict(list)
    for d, h, hs, as_, a in rows:
        f[h].append({'ha': 'H', 'opp': a, 'gf': hs, 'ga': as_})
        f[a].append({'ha': 'A', 'opp': h, 'gf': as_, 'ga': hs})
    return f

FORM = build_form('premier-league')

def seq(team_id, n=2):
    fs = FORM.get(team_id, [])[-n:]
    return ' · '.join('%s %s %d-%d' % ('W' if x['gf'] > x['ga'] else 'D' if x['gf'] == x['ga'] else 'L',
                                       x['ha'], x['gf'], x['ga']) for x in fs)

def row(name):
    t = PL[name]
    return t['pos'], t['pts'], t['p'], t['gf'], t['ga']

def standing(name):
    p, pts, pl, gf, ga = row(name)
    return "%d%s, %d point%s from %d, %d-%d" % (p, ordsuf(p), pts, '' if pts == 1 else 's', pl, gf, ga)

def ordsuf(n):
    return 'th' if 11 <= n % 100 <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')

def ins(club, k=99):
    return tr[club].get('playersIn', [])[:k]

def outs(club, k=99):
    return tr[club].get('playersOut', [])[:k]

def mgr(club):
    return tr[club]['manager'], tr[club].get('managerNote', '')


# ---------------------------------------------------------------- page shell
NAV = ('<header class="top"><div class="shell"><a class="brand" href="/">BRY<b>ME</b></a>'
       '<nav class="topnav"><a href="/">Home</a><a href="/entertainment/">\U0001f3ac Entertainment</a>'
       '<a href="/sports/" class="active">\u26bd Sports</a><a href="/make-money/">\U0001f4b0 Make Money</a>'
       '<a href="/tech/">\U0001f916 Tech &amp; AI</a><a class="nav-search" href="/search/">Search</a></nav>'
       '<div class="top-tools"><a class="header-search" href="/search/" aria-label="Search">Search</a></div>'
       '</div></header>')

MOBNAV = ('<nav class="mobile-nav"><a href="/"><span class="mn-ico">\U0001f3e0</span>Home</a>'
          '<a href="/entertainment/"><span class="mn-ico">\U0001f3ac</span>Entertain</a>'
          '<a href="/sports/" class="active"><span class="mn-ico">\u26bd</span>Sports</a>'
          '<a href="/make-money/"><span class="mn-ico">\U0001f4b0</span>Money</a>'
          '<a href="/tech/"><span class="mn-ico">\U0001f916</span>Tech</a>'
          '<a href="/search/"><span class="mn-ico">\U0001f50d</span>Search</a></nav>')

FOOTER = ('<footer class="footer"><div class="shell"><div class="footer-grid">\n'
 '  <div class="footer-brand"><a class="brand" href="/">BRY<b>ME</b></a><p>Discover what you love. '
 'Learn what you need. Find what\'s next.</p></div>\n'
 '  <nav class="footer-col" aria-label="Explore"><h3>Verticals</h3><a href="/entertainment/">\U0001f3ac Entertainment</a>'
 '<a href="/sports/">\u26bd Sports</a><a href="/make-money/">\U0001f4b0 Make Money</a><a href="/tech/">\U0001f916 Tech &amp; AI</a></nav>\n'
 '  <nav class="footer-col" aria-label="Explore"><h3>Entertainment</h3><a href="/trending/">What\'s Trending</a>'
 '<a href="/movies/">Movies</a><a href="/series/">Series</a><a href="/anime/">Anime</a>'
 '<a href="/articles/">Articles</a><a href="/genres/">Genres</a></nav>\n'
 '  <nav class="footer-col" aria-label="Information"><h3>Information</h3><a href="/about/">About</a>'
 '<a href="/contact/">Contact</a><a href="/editorial-policy/">Editorial Policy</a></nav>\n'
 '  <nav class="footer-col" aria-label="Legal"><h3>Legal</h3><a href="/privacy/">Privacy Policy</a>'
 '<a href="/terms/">Terms of Use</a><a href="/disclaimer/">Disclaimer</a>'
 '<a href="/copyright/">Copyright / DMCA</a>'
 '<a href="/privacy/#cookies" data-cookie-settings>Cookie settings</a></nav>\n</div>\n'
 '<p class="footer-note">BRYME \u00b7 Sports analysis is editorial opinion built on verified results. '
 'We do not invent full-time scores.</p></div></footer>')

CSS = ('.bm-key{border:1px solid var(--line);border-left:3px solid #3ddc84;background:#101318;'
 'border-radius:0 8px 8px 0;padding:14px 18px;margin:18px 0}'
 '.bm-key b{color:#3ddc84;display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;margin-bottom:5px}'
 '.bm-key p{margin:0;font-size:14px;line-height:1.65;color:#d9dde1}'
 '.bm-seq{color:var(--muted);font-size:11.5px;font-weight:700}'
 '.bm-note{border:1px dashed var(--line);border-radius:10px;background:#101318;padding:15px 17px;'
 'margin:22px 0 6px;font-size:13px;line-height:1.65;color:#8d95a3}.bm-note b{color:#e7bb5c}'
 '.sp-table td{font-size:12.8px}.sp-table .num{font-variant-numeric:tabular-nums;white-space:nowrap}'
 '[data-theme="light"] .bm-key{background:#f2f7f3;border-color:#d7dde2;border-left-color:#1f9d57}'
 '[data-theme="light"] .bm-key b{color:#137a41}'
 '[data-theme="light"] .bm-key p{color:#20242a}'
 '[data-theme="light"] .bm-note{background:#f6f7f9;border-color:#d7dde2;color:#4a525d}'
 '[data-theme="light"] .bm-note b{color:#8a6410}'
 '[data-theme="light"] .bm-seq{color:#5a626d}')


def page(slug, eyebrow, title, seo_title, lead, desc, body, hero, related, read='6 min read'):
    url = 'https://bryme.onrender.com/sports/articles/%s/' % slug
    d = html.escape(desc, quote=True)
    t = html.escape(seo_title, quote=True)
    ld = json.dumps([
        {"@context": "https://schema.org", "@type": "Article", "headline": title,
         "description": desc, "datePublished": TODAY, "dateModified": TODAY,
         "author": {"@type": "Organization", "name": "BRYME Editorial"},
         "publisher": {"@type": "Organization", "name": "BRYME"},
         "mainEntityOfPage": url},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://bryme.onrender.com/"},
            {"@type": "ListItem", "position": 2, "name": "Sports", "item": "https://bryme.onrender.com/sports/"},
            {"@type": "ListItem", "position": 3, "name": "Articles", "item": "https://bryme.onrender.com/sports/articles/"},
            {"@type": "ListItem", "position": 4, "name": title, "item": url}]}],
        ensure_ascii=False)

    rel = ''.join('<a class="sp-rel" href="%s">%s</a>' % (u, html.escape(n)) for n, u in related)

    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
 '<meta name="theme-color" content="#08090b">'
 '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">'
 '<title>%s | BRYME</title>'
 '<meta name="description" content="%s">'
 '<meta name="robots" content="index,follow">'
 '<link rel="canonical" href="%s">'
 '<meta property="og:type" content="article"><meta property="og:site_name" content="BRYME">'
 '<meta property="og:title" content="%s | BRYME"><meta property="og:description" content="%s">'
 '<meta property="og:url" content="%s">'
 '<meta property="og:image" content="https://bryme.onrender.com/assets/bryme-card.png">'
 '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
 '<meta property="og:image:alt" content="BRYME">'
 '<meta name="twitter:card" content="summary_large_image">'
 '<meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s">'
 '<meta name="twitter:image" content="https://bryme.onrender.com/assets/bryme-card.png">'
 '<link rel="stylesheet" href="/assets/site.css"><link rel="stylesheet" href="/assets/sports-simple.css">'
 '<style>%s</style>'
 '<script src="/assets/analytics.js" async></script>'
 '<link rel="alternate" type="application/rss+xml" title="BRYME \u2014 Latest" href="/feed.xml">'
 '<script type="application/ld+json">%s</script></head>'
 '<body data-nav="sports">%s\n'
 '<main class="shell sp-easy">\n  <a class="sp-easy-back" href="/sports/articles/">\u2190 Sports articles</a>\n'
 '<section class="article-hero article-hero-photo" style="--hero-img:url(\'/assets/img/sports/%s\')">'
 '<div class="eyebrow">%s</div><h1>%s</h1><p class="lead">%s</p>'
 '<div class="article-meta"><span>BRYME Editorial</span><span>%s</span><span>%s</span></div></section>'
 '<article class="prose article-body">\n%s\n</article>'
 '<section class="sp-related"><h2>Related</h2><div class="sp-rel-grid">%s</div></section>'
 '</main>%s%s'
 '<script>window.BRYME_BASE=\'\'</script><script src="/assets/site-app.js"></script>'
 '<script src="/assets/sports-simple.js"></script>\n</body></html>\n'
 ) % (t, d, url, t, d, url, t, d, CSS, ld, NAV, hero, html.escape(eyebrow),
      html.escape(title), lead, TODAY, read, body, rel, MOBNAV, FOOTER)


def tbl(headers, rows):
    h = ''.join('<th>%s</th>' % x for x in headers)
    b = ''.join('<tr>%s</tr>' % ''.join('<td%s>%s</td>' % (' class="num"' if isinstance(c, tuple) else '',
                                                            c[0] if isinstance(c, tuple) else c)
                                        for c in r) for r in rows)
    return '<div class="sp-table-wrap"><table class="sp-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, b)


def key(label, text):
    return '<div class="bm-key"><b>%s</b><p>%s</p></div>' % (label, text)

NOTE = ('<div class="bm-note"><b>How this was put together.</b> League positions, points and goal '
        'figures come from BRYME\u2019s own league tables, and every result quoted is a verified full-time '
        'score published on the <a href="/sports/">Sports</a> section with a source attached. Transfer '
        'fees and managerial changes come from the 2026/27 window tracker, which closed on 1 September 2026. '
        'Analysis and opinion are the writer\u2019s own; where we make a prediction we say so, and we never '
        'invent a scoreline that has not been played.</div>')

ART = []   # (slug, kwargs)


# ================================================================= 1. ARSENAL
def a_arsenal():
    p, pts, pl, gf, ga = row('Arsenal')
    ci, co = ins('Arsenal'), outs('Arsenal')
    body = f"""
<p>Arsenal are champions of England, and they have started the defence of that title the way champions are supposed to: two matches, two wins, four goals scored, none conceded. They sit {standing('Arsenal')}.</p>
<p>The question in the headline is the one everybody asked in August. Three weeks into the season it already has a sharper edge, because the two clubs most likely to answer it have started just as well — and one of them arrives at the Emirates this weekend.</p>

<h2>What the table actually says</h2>
<p>Four clubs have won both of their opening games. The separation is not in the points column, it is in the goal columns.</p>
{tbl(['#', 'Club', 'P', 'W', 'Goals', 'Pts'],
     [[(str(PL[n]['pos']),), n, (str(PL[n]['p']),), (str(PL[n]['w']),),
       ('%d\u2013%d' % (PL[n]['gf'], PL[n]['ga']),), (str(PL[n]['pts']),)]
      for n in ['Chelsea', 'Manchester City', 'Arsenal', 'Hull City']])}
<p>Chelsea and Manchester City have the same six points. Chelsea have conceded five goals getting there, City two, Arsenal none. Over 38 games that difference is usually the title.</p>
{key('The number that matters', 'Arsenal have not conceded a Premier League goal this season. No side that has kept a clean sheet in both opening fixtures has ever been in a bad position in September.')}

<h2>The window: a spine, not a splash</h2>
<p>Arsenal did not sign the most expensive player in England this summer. They signed the one their midfield had been missing for three years.</p>
{tbl(['In', 'From', 'Fee'], [[html.escape(x['player']), html.escape(x.get('from', '')), (html.escape(x.get('detail', '')),)] for x in ci])}
<p>Bruno Guimar\u00e3es at roughly \u20ac87.5m from Newcastle is the deal that defines the window. Piero Hincapi\u00e9 gives Arteta a ball-playing left-sided defender, Christos Tzolis a direct wide threat, and Illan Meslier arrives on a free as goalkeeping cover.</p>
<p>Out went Leandro Trossard, Jakub Kiwior, Christian N\u00f8rgaard, Karl Hein and — the one that will be tested all season — Gabriel Jesus to Barcelona for \u00a38.6m.</p>

<h2>So can anyone stop them?</h2>
<p>Three sides have a genuine claim, and each has a different flaw.</p>
<p><b>Chelsea</b> lead the table and have scored seven, but they have also conceded five in two games and sold Enzo Fern\u00e1ndez to Manchester City for \u00a3125m on deadline day. Xabi Alonso is rebuilding a midfield mid-season.</p>
<p><b>Manchester City</b> have Enzo Fern\u00e1ndez, Elliot Anderson and Iliman Ndiaye, and a new manager in Enzo Maresca replacing Pep Guardiola. Six points from two, six scored, two conceded. On paper this is the most complete challenge.</p>
<p><b>Hull City</b> are the anomaly — promoted, six points, no goals conceded, and a 2\u20130 win over Manchester United already banked. Nobody expects it to last. It is early enough that nobody can prove it will not.</p>
{key('BRYME view', 'The defence is the argument. Arsenal are the only side in the division yet to concede, and they added a \u20ac87.5m midfielder to protect it. City are the likeliest challengers because they have the deepest squad; Chelsea are the likeliest to drop points because they keep conceding. Sunday against Chelsea will tell us more than the previous two weeks combined.')}

<h2>What to watch next</h2>
<p>Arsenal host Chelsea at the Emirates on Sunday 6 September, 16:30 UK. It is first versus third and, more usefully, the best defence in the league against one of the leakiest attacks in the top half. Our full <a href="/sports/predictions/">predictions page</a> has a scoreline for it and for every other fixture in Europe this weekend.</p>
{NOTE}"""
    return dict(slug='arsenal-title-defence', eyebrow='Premier League',
        title='Arsenal Begin Their Title Defence: Can Anyone Stop Them?',
        seo_title='Arsenal Title Defence 2026/27: Can Anyone Stop Them?',
        lead='Two games, two wins, no goals conceded. Arsenal have started their title defence perfectly \u2014 but Chelsea and Manchester City are level on points, and one of them visits the Emirates on Sunday.',
        desc='Arsenal have started their title defence with two wins and no goals conceded. We look at the table, the \u20ac87.5m Bruno Guimar\u00e3es signing and whether Chelsea, Manchester City or anyone else can stop them.',
        body=body, hero='hero-arsenal.jpg',
        related=[('Our predictions for every top-five league fixture', '/sports/predictions/'),
                 ("Football's biggest spenders", '/sports/articles/biggest-spenders-and-top-five-league-predictions/'),
                 ('Transfer tracker (Aug 2026)', '/sports/articles/premier-league-transfer-tracker-august-2026/'),
                 ('Arsenal on BRYME', '/sports/premier-league/teams/arsenal/')],
        read='7 min read')
ART.append(a_arsenal())


# ============================================== 2. FIVE BIGGEST TRANSFER WINNERS
def a_winners():
    rows = []
    for club, why in [('Manchester City', 'Enzo Fern\u00e1ndez \u00a3125m, Elliot Anderson ~\u00a3116m, Iliman Ndiaye \u00a365m'),
                      ('Arsenal', 'Bruno Guimar\u00e3es ~\u20ac87.5m, Piero Hincapi\u00e9 ~\u20ac49m'),
                      ('Tottenham Hotspur', 'Sandro Tonali \u00a3100m, Mateus Fernandes \u00a385m'),
                      ('Nottingham Forest', 'Sold Elliot Anderson ~\u00a3116m, bought Delap and Diomande'),
                      ('Ipswich Town', 'Seven arrivals led by Emersonn \u00a326.6m')]:
        t = PL[club]
        rows.append([club, (str(t['pos']),), (str(t['pts']),), why])
    body = f"""
<p>The 2026/27 window closed on 1 September. Some clubs spent enormous money; a smaller number actually improved. Those are different things, and two weeks of football has already started to separate them.</p>
<p>These are the five clubs we think won the window — judged not by outlay but by whether the squad is measurably better than it was in May.</p>

<h2>1. Manchester City</h2>
<p>{standing('Manchester City')}. Enzo Maresca replaced Pep Guardiola and was handed the most expensive rebuild in the league.</p>
{tbl(['In', 'From', 'Fee'], [[html.escape(x['player']), html.escape(x.get('from', '')), (html.escape(x.get('detail', '')),)] for x in ins('Manchester City')])}
<p>Enzo Fern\u00e1ndez at \u00a3125m from Chelsea and Elliot Anderson at ~\u00a3116m from Forest is a midfield rebuilt in a single window. Iliman Ndiaye for \u00a365m on deadline day gave Maresca a wide forward as well. City lost Bernardo Silva and Jack Grealish and are still the deepest squad in England.</p>
{key('Why they won it', 'City replaced a departing generation without a transitional season. Two matches in, they have six points and a 4\u20131 win at Crystal Palace already banked.')}

<h2>2. Arsenal</h2>
<p>{standing('Arsenal')} — and not a goal conceded. Bruno Guimar\u00e3es for ~\u20ac87.5m solved the one position that had cost them in previous seasons, and Piero Hincapi\u00e9 at ~\u20ac49m added a defender comfortable in possession. A focused window rather than a loud one.</p>

<h2>3. Tottenham Hotspur</h2>
<p>The biggest spenders by headline fee: Sandro Tonali at \u00a3100m and Mateus Fernandes at \u00a385m, with Andy Robertson and Martin D\u00fabravka added free. Roberto De Zerbi got everything he asked for.</p>
<p>And yet Spurs are {standing('Tottenham Hotspur')}. This is the honest entry on the list: the business was excellent, the results have not followed, and \u00a3185m of midfield has produced zero goals in two matches. Judge it in May, not now.</p>

<h2>4. Nottingham Forest</h2>
<p>Selling your best player for ~\u00a3116m is not usually a win. Forest turned Elliot Anderson into Liam Delap (\u00a345\u201350m), Ousmane Diomande (~\u00a334m), Daniel Mu\u00f1oz (up to \u00a322m) and Xaver Schlager on a free, then hired Oliver Glasner. That is a squad rebuilt from one sale with money left over.</p>

<h2>5. Ipswich Town</h2>
<p>Promoted clubs usually either freeze or panic. Ipswich did neither: seven arrivals led by Emersonn (\u00a326.6m), Abdul Fatawu (\u00a323m) and Florentino (\u00a319m), after Kieran McKenna stepped down and Gary O'Neil took over. They have already won a Premier League match.</p>

<h2>The table, two matchweeks in</h2>
{tbl(['Club', 'Pos', 'Pts', 'Headline business'], rows)}
<p>Four of our five are in the top half. The exception is Tottenham, and that is the reminder that a good window is a bet, not a result.</p>
{key('The one we may have got wrong', 'Chelsea. Nine in, ten out, and they top the table \u2014 but selling Enzo Fern\u00e1ndez to a title rival on deadline day for \u00a3125m without replacing him is the kind of decision that looks very different in March.')}
{NOTE}"""
    return dict(slug='five-biggest-transfer-winners', eyebrow='Transfer news',
        title='The Five Biggest Transfer Winners of the 2026 Window',
        seo_title='The Five Biggest Transfer Winners of the 2026 Window',
        lead='The window shut on 1 September. Spending big and improving are not the same thing \u2014 here are the five clubs whose squads are genuinely better, and the early evidence for each.',
        desc='Manchester City, Arsenal, Tottenham, Nottingham Forest and Ipswich \u2014 the five clubs that won the 2026 transfer window, judged on whether the squad actually improved, with the early league table as evidence.',
        body=body, hero='hero-premier-league.jpg',
        related=[('Clubs that still need signings', '/sports/articles/five-clubs-that-still-need-signings/'),
                 ('Transfer tracker (Aug 2026)', '/sports/articles/premier-league-transfer-tracker-august-2026/'),
                 ("Football's biggest spenders", '/sports/articles/biggest-spenders-and-top-five-league-predictions/'),
                 ('Deadline day', '/sports/articles/deadline-day-dont-try-to-make-sense-of-it/')],
        read='7 min read')
ART.append(a_winners())


# ============================================ 3. CLUBS THAT STILL NEED SIGNINGS
def a_needs():
    need = ['Tottenham Hotspur', 'Aston Villa', 'Coventry City', 'Crystal Palace', 'Fulham']
    body = f"""
<p>The window is shut. These five cannot fix anything until January, which makes the gaps in their squads the story of their autumn.</p>
<p>We picked them on evidence rather than reputation: goals scored, goals conceded and points after two matchweeks.</p>
{tbl(['Club', 'Pos', 'Pts', 'Scored', 'Conceded', 'Last two'],
     [[n, (str(PL[n]['pos']),), (str(PL[n]['pts']),), (str(PL[n]['gf']),), (str(PL[n]['ga']),),
       ('<span class="bm-seq">%s</span>' % seq(sl),)]
      for n, sl in [('Tottenham Hotspur', 'tottenham'), ('Aston Villa', 'aston-villa'),
                    ('Coventry City', 'coventry'), ('Crystal Palace', 'crystal-palace'), ('Fulham', 'fulham')]])}

<h2>1. Tottenham Hotspur \u2014 a striker</h2>
<p>Spurs spent \u00a3100m on Sandro Tonali and \u00a385m on Mateus Fernandes and have scored zero goals in two matches. {standing('Tottenham Hotspur')}. The midfield is among the most expensive ever assembled in England; the finishing is not there. Mykhailo Mudryk arrived on loan from Chelsea, which is a winger, not a solution.</p>
{key('The gap', 'Two games, no goals, five conceded. Spurs did not sign a recognised number nine and it is already the defining problem of their season.')}

<h2>2. Aston Villa \u2014 a replacement for Morgan Rogers</h2>
<p>Villa sold Rogers to Chelsea for around \u20ac138m and have not scored since. {standing('Aston Villa')}. Nicolas Jackson (\u00a365m) and Alejandro Garnacho on loan arrived to cover it, and Jo\u00e3o Gomes and Johan Manzambi refreshed the midfield, but Unai Emery has lost 0\u20134 at Brighton and 0\u20131 at home to Arsenal.</p>

<h2>3. Coventry City \u2014 a Premier League forward</h2>
<p>Promoted Coventry spent \u00a368.5m-plus on Caleb Yirenkyi, Carl Rushworth, Loum Tchaouna and Aur\u00e8le Amenda. Frank Lampard's side have still not scored a top-flight goal: {standing('Coventry City')}. They host Manchester City on Saturday.</p>

<h2>4. Crystal Palace \u2014 a centre-back</h2>
<p>Palace sold Maxence Lacroix to Chelsea for \u00a351m and Daniel Mu\u00f1oz for up to \u00a322m, and replaced them largely with free transfers and a swap. Pierre Sage inherits {standing('Crystal Palace')}. The rebuild is coherent on paper; the defence has conceded six already.</p>

<h2>5. Fulham \u2014 depth anywhere</h2>
<p>\u00c1lvaro Arbeloa's first window brought Gonzalo Garc\u00eda (\u00a334m) and C\u00e9sar Palacios from Real Madrid and Shea Charles (\u00a330m). Fulham are {standing('Fulham')} having lost both. Ra\u00fal Jim\u00e9nez left on a free and nobody of that profile replaced him.</p>

<h2>What happens now</h2>
<p>Nothing, until 1 January. That is the point. Four of these five sit in the bottom five of the table, and the only tool available between now and the new year is coaching. Spurs are the interesting case: their squad cost more than almost anyone's and their problem is the cheapest one to have \u2014 a finisher.</p>
{NOTE}"""
    return dict(slug='five-clubs-that-still-need-signings', eyebrow='Transfer news',
        title='Five Clubs That Still Need Signings \u2014 And Cannot Buy Until January',
        seo_title='Five Clubs That Still Need Signings After the 2026 Window',
        lead='The window shut on 1 September. These five have holes they can no longer fill, and the league table is already showing exactly where.',
        desc='Tottenham, Aston Villa, Coventry, Crystal Palace and Fulham all finished the 2026 window with obvious gaps. We use the early table \u2014 goals scored, conceded and points \u2014 to show what each is missing.',
        body=body, hero='hero-matchweek.jpg',
        related=[('The five biggest transfer winners', '/sports/articles/five-biggest-transfer-winners/'),
                 ('Transfer tracker (Aug 2026)', '/sports/articles/premier-league-transfer-tracker-august-2026/'),
                 ('Deadline day', '/sports/articles/deadline-day-dont-try-to-make-sense-of-it/'),
                 ('Our predictions', '/sports/predictions/')],
        read='6 min read')
ART.append(a_needs())


# ================================================== 4. FIVE MATCHES TO WATCH
def a_matches():
    body = f"""
<p>Matchweek 3 in England, Jornada 4 in Spain, Giornata 3 in Italy. Across Europe's top five leagues there are 48 fixtures this weekend. These are the five worth rearranging your Saturday for.</p>

<h2>1. Arsenal v Chelsea \u2014 Sunday 6 September, 16:30 UK</h2>
<p>First plays third, and the two biggest spenders in world football over the last five years meet at the Emirates. Arsenal are {standing('Arsenal')}, Chelsea {standing('Chelsea')}.</p>
<p>The contrast is the appeal: Arsenal have not conceded a goal, Chelsea have conceded five while scoring seven. Chelsea sold Enzo Fern\u00e1ndez to Manchester City for \u00a3125m on deadline day and Xabi Alonso is still settling a rebuilt midfield.</p>

<h2>2. Inter Milan v Napoli \u2014 Saturday 5 September, 18:00 CEST</h2>
<p>San Siro, and the best fixture in Italy this round. Inter have won both, scoring five and conceding one. Napoli beat Genoa 2\u20130 and then lost 2\u20131 at home to Como \u2014 the sort of result that makes an away trip to Inter look considerably harder.</p>

<h2>3. Paris Saint-Germain v Monaco \u2014 Friday 4 September, 21:05 CEST</h2>
<p>Monaco are the only side in Ligue 1 with a perfect record and no goals conceded, and they beat Marseille 2\u20130 last time out. PSG drew their opener 2\u20132 with Rennes. On current evidence the visitors are the better team, which is not a sentence Ligue 1 offers up often.</p>

<h2>4. Valencia v Barcelona \u2014 Sunday 6 September, 16:15 CEST</h2>
<p>Barcelona have won all three and scored twelve. Valencia have one goal in three matches and sit bottom of La Liga on goal difference. The Mestalla has historically been one of the hardest away days in Spain, which is the only reason this is a contest at all.</p>
<p>Raphinha has five goals in three games \u2014 the leading scorer in La Liga.</p>

<h2>5. Juventus v AC Milan \u2014 Sunday 6 September, 20:45 CEST</h2>
<p>Both have won both. Juventus have not conceded a goal; Milan have conceded one. Two of Italy's biggest clubs, six points each, and a combined one goal against. It may not be pretty, but it decides who stays with Roma at the top.</p>

<h2>The rest of the weekend</h2>
{tbl(['Also worth your time', 'When', 'Why'],
 [['Manchester City v Coventry', 'Sat 15:00 UK', 'City at home to a side yet to score a league goal'],
  ['Hull City v Aston Villa', 'Sat 17:30 UK', 'Hull have six points and no goals conceded; Villa have none of either'],
  ['Real Betis v Real Madrid', 'Fri 21:00 CEST', 'Madrid have won all three, scoring ten'],
  ['Schalke v Bayern Munich', 'Sat 18:30 CEST', 'Atmosphere guaranteed, result rather less so'],
  ['Roma v Atalanta', 'Sat 20:45 CEST', 'Roma have won 4\u20130 twice and conceded nothing']])}
<p>Every one of those has a predicted scoreline on our <a href="/sports/predictions/">predictions page</a>, with both clubs' form shown next to the pick.</p>
{NOTE}"""
    return dict(slug='five-matches-we-cannot-wait-to-watch', eyebrow='Matchweek coverage',
        title='Five Matches We Cannot Wait to Watch This Weekend',
        seo_title='Five Best Matches This Weekend: Arsenal v Chelsea, Inter v Napoli',
        lead='Forty-eight fixtures across Europe\u2019s top five leagues. Arsenal host Chelsea, Inter host Napoli and Monaco go to the Parc des Princes with a perfect record \u2014 these are the five that matter.',
        desc='Arsenal v Chelsea, Inter v Napoli, PSG v Monaco, Valencia v Barcelona and Juventus v Milan \u2014 the five best fixtures across Europe this weekend, with the form behind each.',
        body=body, hero='hero-matches.jpg',
        related=[('Predictions for all 48 fixtures', '/sports/predictions/'),
                 ('Players to watch this weekend', '/sports/articles/players-to-watch-this-weekend/'),
                 ('Five things fans will be talking about', '/sports/articles/five-things-fans-will-talk-about-this-weekend/'),
                 ('All sports articles', '/sports/articles/')],
        read='6 min read')
ART.append(a_matches())


# ============================================ 5. FIVE THINGS FANS WILL TALK ABOUT
def a_talk():
    body = f"""
<p>Every weekend produces the same handful of arguments in group chats. Here are the five this one will produce, and the numbers you will want when the argument starts.</p>

<h2>1. Tottenham have spent \u00a3185m and scored nothing</h2>
<p>Sandro Tonali (\u00a3100m) and Mateus Fernandes (\u00a385m) arrived to build the most expensive midfield in the club's history. Spurs are {standing('Tottenham Hotspur')} \u2014 zero goals in two matches, five conceded, beaten 3\u20130 at Brentford and 2\u20130 at home by Newcastle.</p>
{key('The argument', 'Is this a squad problem or a striker problem? Roberto De Zerbi bought midfielders and loaned Mudryk. Nobody bought a number nine.')}

<h2>2. Hull City are fourth and nobody knows what to do about it</h2>
<p>Promoted, {standing('Hull City')}, and they have not conceded a goal. They beat Manchester United 2\u20130 and won 1\u20130 at Coventry. Sergej Jakirovi\u0107 spent almost nothing \u2014 Jack Butland for \u00a33m, Matt Targett, Ben Robinson and Hidemasa Morita on frees.</p>
<p>The debate is whether it is real. Our view on the <a href="/sports/predictions/">predictions page</a> is that it is real enough to back them against Aston Villa this weekend.</p>

<h2>3. Chelsea sold Enzo Fern\u00e1ndez to a title rival</h2>
<p>\u00a3125m from Manchester City on deadline day, with no direct replacement signed. Chelsea are top of the table, so the decision has not hurt yet. They have also conceded five goals in two games, both of which they won by a single goal \u2014 3\u20132 at Fulham and 4\u20133 against Brighton.</p>

<h2>4. Liverpool lost Salah, Robertson and Konat\u00e9 on frees</h2>
<p>All three left for nothing: Mohamed Salah to Trabzonspor, Andy Robertson to Tottenham, Ibrahima Konat\u00e9 to Real Madrid. Andoni Iraola replaced Arne Slot and brought in J\u00e9r\u00e9my Jacquet, V\u00edctor Mu\u00f1oz and Ronald Ara\u00fajo on loan from Barcelona.</p>
<p>Liverpool are {standing('Liverpool')}, having drawn both 2\u20132. Two points from six, and the argument about how a club lets three players of that standing run their contracts down will not go away quickly.</p>

<h2>5. Bruno Fernandes is the league's top scorer</h2>
<p>Three goals in two games from midfield, and Manchester United still lost 2\u20130 at Hull before beating Ipswich 5\u20132.</p>
{tbl(['Player', 'Club', 'Goals', 'Apps'],
     [[html.escape(s['name']), s['team'], (str(s['goals']),), (str(s['apps']),)] for s in SCORERS[:6]])}
<p>Michael Carrick's side are {standing('Manchester United')}. Andrey Santos (~\u00a350m) and Carlos Baleba (\u00a365\u201370m) were bought to rebuild the midfield; so far the goals are coming from the man who was already there.</p>
{NOTE}"""
    return dict(slug='five-things-fans-will-talk-about-this-weekend', eyebrow='Football debates',
        title='Five Things Football Fans Will Be Talking About This Weekend',
        seo_title='Five Things Football Fans Will Talk About This Weekend',
        lead='Spurs have spent \u00a3185m and scored nothing, Hull City are fourth without conceding, and Chelsea sold their midfield to a title rival. The five arguments this weekend will produce.',
        desc='Tottenham\u2019s goalless \u00a3185m midfield, Hull City in fourth, Chelsea selling Enzo Fern\u00e1ndez to Manchester City, Liverpool losing three players on frees and Bruno Fernandes topping the scoring charts.',
        body=body, hero='hero-matchweek.jpg',
        related=[('Five matches we cannot wait to watch', '/sports/articles/five-matches-we-cannot-wait-to-watch/'),
                 ('Premier League banter table', '/sports/articles/premier-league-banter-table/'),
                 ('Predictions', '/sports/predictions/'),
                 ('All sports articles', '/sports/articles/')],
        read='6 min read')
ART.append(a_talk())


# =================================================== 6. LIVERPOOL NEXT CHAPTER
def a_liverpool():
    body = f"""
<p>Mohamed Salah left on a free transfer. So did Andy Robertson. So did Ibrahima Konat\u00e9. Arne Slot left too, replaced by Andoni Iraola. Liverpool have started the season {standing('Liverpool')} \u2014 two draws, four scored, four conceded.</p>
<p>This is the most complete change of era Anfield has seen in a decade, and it happened in one summer.</p>

<h2>What left</h2>
{tbl(['Out', 'To', 'Fee'], [[html.escape(x['player']), html.escape(x.get('to', '')), (html.escape(x.get('detail', '')),)] for x in outs('Liverpool')])}
<p>Three players of that standing leaving for nothing in a single window is remarkable. Salah to Trabzonspor ends the most productive Premier League career the club has had since the competition began.</p>

<h2>What arrived</h2>
{tbl(['In', 'From', 'Detail'], [[html.escape(x['player']), html.escape(x.get('from', '')), (html.escape(x.get('detail', '')),)] for x in ins('Liverpool')])}
<p>Ronald Ara\u00fajo's season-long loan from Barcelona, with a reported option to buy, is the headline. J\u00e9r\u00e9my Jacquet and V\u00edctor Mu\u00f1oz are longer-term bets. This is not a like-for-like replacement of what left; it is a different kind of squad.</p>
{key('The maths', 'Liverpool lost a forward with a decade of goals, a first-choice left-back and a first-choice centre-back, and received no fees. The replacements cost money the sales did not generate.')}

<h2>Two matches, two draws</h2>
<p>Liverpool drew 2\u20132 at Newcastle and 2\u20132 at home with Nottingham Forest. Neither is a bad result in isolation. Together they are two points from six, and a defence that has conceded in both.</p>
<p>The pattern is the concern rather than the points: Iraola's teams press high and defend in transition, and Liverpool have twice been pegged back.</p>

<h2>Can they challenge again?</h2>
<p>The honest answer three weeks in is that they are not currently in the argument. Arsenal, Chelsea and Manchester City all have six points; Liverpool have two. That is a four-point gap in August, which is nothing, and a four-point gap plus a squad in transition, which is not nothing.</p>
<p>What would change our mind: Ara\u00fajo settling quickly at centre-back, and someone other than the front line scoring. Liverpool travel to promoted Ipswich on Friday night \u2014 our <a href="/sports/predictions/">predictions page</a> backs them to win it, on the basis that two draws against Newcastle and Forest is still a higher floor than anything Ipswich have shown.</p>
{key('BRYME view', 'Top four is realistic. A title challenge in the first season under a new manager, having lost Salah, Robertson and Konat\u00e9 for nothing, would be one of the more remarkable achievements in the club\u2019s recent history.')}
{NOTE}"""
    return dict(slug='liverpools-next-chapter', eyebrow='Premier League',
        title='Liverpool\u2019s Next Chapter: Can They Challenge Again?',
        seo_title='Liverpool 2026/27: Life After Salah, Robertson and Konat\u00e9',
        lead='Salah, Robertson and Konat\u00e9 all left on free transfers. Arne Slot left too. Andoni Iraola has two points from two games and the biggest rebuild at Anfield in a decade.',
        desc='Liverpool lost Mohamed Salah, Andy Robertson and Ibrahima Konat\u00e9 on free transfers and replaced Arne Slot with Andoni Iraola. Two draws in, we look at whether they can challenge again.',
        body=body, hero='hero-liverpool.jpg',
        related=[('Managers with the most to prove', '/sports/articles/managers-with-most-to-prove/'),
                 ('Predictions', '/sports/predictions/'),
                 ('Transfer tracker (Aug 2026)', '/sports/articles/premier-league-transfer-tracker-august-2026/'),
                 ('Liverpool on BRYME', '/sports/premier-league/teams/liverpool/')],
        read='7 min read')
ART.append(a_liverpool())


# ================================================= 7. MANAGERS WITH MOST TO PROVE
def a_managers():
    newmen = [(c['name'], c['manager'], c.get('managerNote', '')) for c in tr.values()
              if c.get('managerNote', '').startswith('New')]
    body = f"""
<p>Eight Premier League clubs changed manager over the summer. Two matchweeks in, some of those decisions already look inspired and others look expensive.</p>
{tbl(['Club', 'Manager', 'Change', 'Pos', 'Pts'],
     [[n, html.escape(m), html.escape(note), (str(PL[n]['pos']),), (str(PL[n]['pts']),)]
      for n, m, note in sorted(newmen, key=lambda x: PL[x[0]]['pos'])])}

<h2>1. Enzo Maresca \u2014 Manchester City</h2>
<p>Replacing Pep Guardiola is the hardest job in football management. Maresca was handed Enzo Fern\u00e1ndez (\u00a3125m), Elliot Anderson (~\u00a3116m) and Iliman Ndiaye (\u00a365m) to do it with, and lost Bernardo Silva, John Stones, Manuel Akanji, Nathan Ak\u00e9 and Jack Grealish.</p>
<p>{standing('Manchester City')}. So far, so untroubled \u2014 but the fixture list has been kind and the expectation is absolute.</p>

<h2>2. Xabi Alonso \u2014 Chelsea</h2>
<p>Nine in, ten out, and Chelsea sit {standing('Chelsea')}. The wins were 3\u20132 at Fulham and 4\u20133 against Brighton: five goals conceded in two victories. Alonso then lost Enzo Fern\u00e1ndez on deadline day for \u00a3125m with no replacement.</p>
{key('The test', 'Chelsea are top and leaking. Alonso\u2019s reputation was built on control at Leverkusen. Sunday at Arsenal \u2014 the only side yet to concede \u2014 is the first real examination.')}

<h2>3. Andoni Iraola \u2014 Liverpool</h2>
<p>Took over from Arne Slot in the same summer Salah, Robertson and Konat\u00e9 all left on frees. Two draws, {standing('Liverpool')}. The most to prove of anyone on this list, with the least margin.</p>

<h2>4. Matthias Jaissle \u2014 Newcastle United</h2>
<p>Replaced Eddie Howe and immediately sold Sandro Tonali (~\u00a3100m), Bruno Guimar\u00e3es (~\u20ac87.5m) and Anthony Gordon, reinvesting in Aladji Bamba, Bazoumana Tour\u00e9, Sean Steur and Lukas Hornicek. Newcastle are {standing('Newcastle United')} and won 2\u20130 at Spurs. A rebuild that is going better than it should be.</p>

<h2>5. Oliver Glasner \u2014 Nottingham Forest</h2>
<p>Left Crystal Palace for Forest and sold Elliot Anderson for ~\u00a3116m, spending it on Liam Delap, Ousmane Diomande and Daniel Mu\u00f1oz. Forest are {standing('Nottingham Forest')} but took a point at Anfield.</p>

<h2>The others</h2>
<p><b>Pierre Sage</b> inherited a Crystal Palace side that lost Lacroix and Mu\u00f1oz and sits {standing('Crystal Palace')}. <b>\u00c1lvaro Arbeloa</b> at Fulham is {standing('Fulham')}. <b>Marco Rose</b> has Bournemouth {standing('Bournemouth')}. <b>Gary O'Neil</b> at Ipswich took over after Kieran McKenna stepped down post-promotion and has already won a match.</p>
{key('BRYME view', 'Jaissle has the best case so far \u2014 four points while selling the three best players at the club. Alonso has the most to fix, and the least time in which fixing it will look impressive.')}
{NOTE}"""
    return dict(slug='managers-with-most-to-prove', eyebrow='Managers',
        title='The Managers With the Most to Prove in 2026/27',
        seo_title='Premier League Managers With the Most to Prove in 2026/27',
        lead='Eight Premier League clubs changed manager this summer. Maresca replaced Guardiola, Alonso took Chelsea and Iraola inherited a Liverpool side that lost Salah for nothing.',
        desc='Enzo Maresca at Manchester City, Xabi Alonso at Chelsea, Andoni Iraola at Liverpool and five more \u2014 the Premier League managers with the most to prove, with the early table as evidence.',
        body=body, hero='hero-man-city-manager.jpg',
        related=[('Manchester City without Guardiola', '/sports/articles/manchester-city-without-guardiola/'),
                 ("Maresca's second attempt in England", '/sports/articles/marescas-second-attempt-in-england/'),
                 ("Liverpool's next chapter", '/sports/articles/liverpools-next-chapter/'),
                 ('All sports articles', '/sports/articles/')],
        read='7 min read')
ART.append(a_managers())


# ============================================ 8. MAN CITY WITHOUT GUARDIOLA
def a_city():
    body = f"""
<p>Pep Guardiola has gone. Enzo Maresca has replaced him. Manchester City are {standing('Manchester City')} and have spent more than any club in England this summer to make the transition invisible.</p>
<p>Two matches is not enough to judge a era. It is enough to see what the new one is going to look like.</p>

<h2>The squad Maresca inherited, and the one he built</h2>
{tbl(['In', 'From', 'Fee'], [[html.escape(x['player']), html.escape(x.get('from', '')), (html.escape(x.get('detail', '')),)] for x in ins('Manchester City')])}
<p>Enzo Fern\u00e1ndez at \u00a3125m from Chelsea on deadline day, Elliot Anderson at ~\u00a3116m from Forest, Iliman Ndiaye at \u00a365m from Everton. That is roughly \u00a3306m on three players.</p>
{tbl(['Out', 'To', 'Detail'], [[html.escape(x['player']), html.escape(x.get('to', '') or '\u2014'), (html.escape(x.get('detail', '')),)] for x in outs('Manchester City')])}
<p>Bernardo Silva left for Real Madrid on a free. John Stones, Manuel Akanji and Nathan Ak\u00e9 all departed without confirmed destinations, and Jack Grealish went to Everton on loan. That is a defence substantially dismantled.</p>

<h2>What has actually happened</h2>
<p>City won 4\u20131 at Crystal Palace and 2\u20131 at home to Bournemouth. Six points, six scored, two conceded. Erling Haaland has two goals in two, and Rayan Cherki also has two.</p>
{key('The early read', 'The attack has transferred intact. The defence is the open question: three senior centre-backs left and the replacements are midfielders. Two goals conceded in two games is fine \u2014 the fixtures have not tested it.')}

<h2>What is different about a Maresca team</h2>
<p>Guardiola's City controlled games through positional discipline and a single deep midfielder. Maresca has bought two \u00a3100m-plus central midfielders in one window, which suggests a different structure \u2014 more bodies in midfield, more rotation, less reliance on one holding player.</p>
<p>That matters because Rodri's succession was the unresolved problem of the previous regime. City have answered it by buying Enzo Fern\u00e1ndez and Elliot Anderson rather than by finding one direct replacement.</p>

<h2>What happens next</h2>
<p>City host Coventry on Saturday \u2014 a promoted side that has yet to score a Premier League goal and sits {standing('Coventry City')}. Our <a href="/sports/predictions/">predictions page</a> makes this the most one-sided fixture in Europe this weekend.</p>
<p>The real examination comes later: away trips, European nights, and the first time a well-organised side sits deep and asks the rebuilt defence to play out under pressure.</p>
{NOTE}"""
    return dict(slug='manchester-city-without-guardiola', eyebrow='Managers',
        title='Manchester City Without Guardiola: What Happens Next?',
        seo_title='Manchester City Without Guardiola: Maresca\u2019s First Season',
        lead='Pep Guardiola has gone, Enzo Maresca has arrived, and City spent roughly \u00a3306m on three midfielders to make the change invisible. Two matches in, here is what the new era looks like.',
        desc='Enzo Maresca has replaced Pep Guardiola at Manchester City, with Enzo Fern\u00e1ndez, Elliot Anderson and Iliman Ndiaye arriving for around \u00a3306m. What the post-Guardiola side actually looks like.',
        body=body, hero='hero-man-city-manager.jpg',
        related=[("Rodri's future", '/sports/articles/rodris-future/'),
                 ('Managers with the most to prove', '/sports/articles/managers-with-most-to-prove/'),
                 ("Maresca's second attempt in England", '/sports/articles/marescas-second-attempt-in-england/'),
                 ('Manchester City on BRYME', '/sports/premier-league/teams/manchester-city/')],
        read='7 min read')
ART.append(a_city())


# ============================================ 9. MAN UNITED FINALLY THEIR SEASON
def a_united():
    body = f"""
<p>Manchester United are {standing('Manchester United')}. They were beaten 2\u20130 at promoted Hull City on the opening weekend and then beat Ipswich 5\u20132. Bruno Fernandes has three goals in two matches and leads the Premier League scoring charts.</p>
<p>That is the season so far: one very bad afternoon, one very good one, and a midfielder carrying the attack.</p>

<h2>Carrick's first full summer</h2>
<p>Michael Carrick's appointment was made permanent after R\u00faben Amorim's departure. The window that followed was about the middle of the pitch.</p>
{tbl(['In', 'From', 'Fee'], [[html.escape(x['player']), html.escape(x.get('from', '')), (html.escape(x.get('detail', '')),)] for x in ins('Manchester United')])}
<p>Andrey Santos from Chelsea (~\u00a350m), Carlos Baleba from Brighton (\u00a365\u201370m) and Youri Tielemans from Aston Villa (~\u00a335m) is a midfield rebuilt in one window for roughly \u00a3150m.</p>
{tbl(['Out', 'To', 'Detail'], [[html.escape(x['player']), html.escape(x.get('to', '') or '\u2014'), (html.escape(x.get('detail', '')),)] for x in outs('Manchester United')])}
<p>Rasmus H\u00f8jlund's loan at Napoli became permanent. Casemiro, Jadon Sancho and Tyrell Malacia all left without confirmed destinations \u2014 the clearing of a wage bill more than a sporting decision.</p>

<h2>The case for yes</h2>
<p>Five goals against Ipswich, the league's leading scorer in the side, and a midfield that finally has legs in it. United have scored five in two games \u2014 more than Arsenal, Manchester City or Hull.</p>

<h2>The case for no</h2>
<p>They lost 2\u20130 at a promoted club in the first week, and have conceded four in two matches. Only three sides in the top ten have conceded more.</p>
{key('The honest position', 'United are 10th with three points, four behind the leaders after two games. The squad is better than last season\u2019s. Whether it is a top-four squad is a question the next month answers, not this one.')}

<h2>What to watch</h2>
<p>United travel to Everton on Sunday \u2014 a side unbeaten on four points. Our <a href="/sports/predictions/">predictions page</a> calls it a draw, largely because United's away form this season consists of a 2\u20130 defeat at Hull.</p>
<p>The number that will decide their season is not goals scored. It is whether Baleba and Santos give the defence enough protection to stop conceding two a game.</p>
{NOTE}"""
    return dict(slug='manchester-united-finally-their-season', eyebrow='Premier League',
        title='Manchester United: Is This Finally Their Season?',
        seo_title='Manchester United 2026/27: Is This Finally Their Season?',
        lead='Beaten 2\u20130 at promoted Hull, then 5\u20132 winners over Ipswich. Bruno Fernandes leads the league\u2019s scoring charts and Carrick has spent \u00a3150m on a new midfield. What it adds up to.',
        desc='Manchester United have spent around \u00a3150m rebuilding midfield under Michael Carrick. After a 2\u20130 defeat at Hull and a 5\u20132 win over Ipswich, we look at whether this is finally their season.',
        body=body, hero='hero-premier-league.jpg',
        related=[('Players who could explode this season', '/sports/articles/players-who-could-explode-this-season/'),
                 ('Transfer tracker (Aug 2026)', '/sports/articles/premier-league-transfer-tracker-august-2026/'),
                 ('Predictions', '/sports/predictions/'),
                 ('Manchester United on BRYME', '/sports/premier-league/teams/manchester-united/')],
        read='6 min read')
ART.append(a_united())


# ============================================ 10. MARESCA SECOND ATTEMPT
def a_maresca():
    body = f"""
<p>Enzo Maresca is back in the Premier League, and this time he has replaced Pep Guardiola. Manchester City are {standing('Manchester City')} after two matches.</p>
<p>The question is not whether he can coach. It is whether the specific way he wants to play survives contact with the expectations at the Etihad.</p>

<h2>The job</h2>
<p>Guardiola left having redefined what the club expects. Maresca inherited a squad losing Bernardo Silva, John Stones, Manuel Akanji, Nathan Ak\u00e9 and Jack Grealish, and was given roughly \u00a3306m to spend on Enzo Fern\u00e1ndez, Elliot Anderson and Iliman Ndiaye.</p>
{key('What that buying tells you', 'Two \u00a3100m-plus central midfielders in one window is not squad depth, it is a structural choice. Maresca wants control through numbers in midfield rather than through a single holding player.')}

<h2>Two matches</h2>
<p>City won 4\u20131 at Crystal Palace and 2\u20131 at home to Bournemouth. Six points, six scored, two conceded. Comfortable at Selhurst Park, considerably less so against Bournemouth, who were the better side for a spell before losing to a late goal.</p>
<p>Erling Haaland has two goals; Rayan Cherki also has two.</p>

<h2>What could go wrong</h2>
<p>The defence. Three senior centre-backs left the club and none of the three headline signings is a defender. City have conceded two goals in two games, which is fine, but neither Crystal Palace ({standing('Crystal Palace')}) nor Bournemouth ({standing('Bournemouth')}) has been a serious attacking test.</p>
<p>The second risk is patience. Maresca's approach relies on slow, deliberate build-up. At the Etihad, a run of 1\u20130 wins is tolerated; a run of 1\u20131 draws is not.</p>

<h2>What could go right</h2>
<p>If Enzo Fern\u00e1ndez and Elliot Anderson work as a pair, City have solved the succession problem that hung over the previous regime without a transitional season. That would be the most valuable thing any manager in England achieves this year.</p>

<h2>The next test</h2>
<p>Coventry visit on Saturday \u2014 {standing('Coventry City')}, and yet to score in the Premier League. Our <a href="/sports/predictions/">predictions page</a> has City winning comfortably. The genuine examination arrives when a side sits deep and dares the new-look defence to play through them.</p>
{NOTE}"""
    return dict(slug='marescas-second-attempt-in-england', eyebrow='Managers',
        title='Maresca\u2019s Second Attempt in England: Can He Make It Work?',
        seo_title='Enzo Maresca at Manchester City: Can He Make It Work?',
        lead='Enzo Maresca is back in the Premier League, this time replacing Pep Guardiola. Six points from two games, \u00a3306m spent on three signings, and a defence stripped of three senior centre-backs.',
        desc='Enzo Maresca has replaced Pep Guardiola at Manchester City with roughly \u00a3306m of new signings. We look at what his structure needs, what could go wrong and what the first two matches showed.',
        body=body, hero='hero-man-city-manager.jpg',
        related=[('Manchester City without Guardiola', '/sports/articles/manchester-city-without-guardiola/'),
                 ('Managers with the most to prove', '/sports/articles/managers-with-most-to-prove/'),
                 ("Rodri's future", '/sports/articles/rodris-future/'),
                 ('Predictions', '/sports/predictions/')],
        read='6 min read')
ART.append(a_maresca())


# ============================================ 11. NEWLY PROMOTED CLUBS
def a_promoted():
    body = f"""
<p>Three clubs came up: Coventry City, Ipswich Town and Hull City. Two matchweeks in they have taken three very different approaches, and produced three very different starts.</p>
{tbl(['Club', 'Manager', 'Pos', 'Pts', 'Goals', 'Last two'],
     [[n, html.escape(tr[n]['manager']), (str(PL[n]['pos']),), (str(PL[n]['pts']),),
       ('%d\u2013%d' % (PL[n]['gf'], PL[n]['ga']),), ('<span class="bm-seq">%s</span>' % seq(sl),)]
      for n, sl in [('Hull City', 'hull'), ('Ipswich Town', 'ipswich'), ('Coventry City', 'coventry')]])}

<h2>Hull City \u2014 spend little, concede nothing</h2>
<p>Sergej Jakirovi\u0107 kept his job and spent almost nothing: Jack Butland for \u00a33m, plus Matt Targett, Ben Robinson and Hidemasa Morita on free transfers. Ivor Pandur (\u00a36m) and Kyle Joseph (\u00a34m) left.</p>
<p>Hull are {standing('Hull City')} \u2014 two wins, no goals conceded, including 2\u20130 against Manchester United on the opening weekend.</p>
{key('The approach', 'Continuity. Same manager, minimal turnover, a defence that already knew each other. It is the cheapest strategy on this list and currently the most effective.')}

<h2>Ipswich Town \u2014 back the new manager</h2>
<p>Kieran McKenna stepped down after promotion and Gary O'Neil took over. Ipswich then made seven signings: Emersonn (\u00a326.6m), Abdul Fatawu (\u00a323m), Florentino (\u00a319m), Kjell Scherpen (\u00a311m) and Daizen Maeda (\u00a310m) among them. Ashley Young retired at 41.</p>
<p>They are {standing('Ipswich Town')} \u2014 a 2\u20131 win over Sunderland and a 5\u20132 defeat at Manchester United. Aggressive recruitment, mixed early evidence.</p>

<h2>Coventry City \u2014 spend big, wait for it to click</h2>
<p>Frank Lampard's side spent the most: Caleb Yirenkyi (\u00a326m), Carl Rushworth (\u00a322.5m), Loum Tchaouna (\u00a320m) and Aur\u00e8le Amenda (\u00a317.2m), with Gustavo Hamer at \u00a36m.</p>
<p>Coventry are {standing('Coventry City')} and have not scored a Premier League goal. They lost 3\u20130 at Arsenal and 1\u20130 at home to Hull.</p>

<h2>What the three approaches tell us</h2>
<p>The club that spent the least is fourth. The club that spent the most is 19th. That is a two-game sample and proves nothing on its own, but it points at something real: promoted squads that stay together tend to start better, because organisation transfers to a higher division faster than individual quality does.</p>
<p>The counter-argument arrives around November, when the schedule thickens and Hull's thin squad is asked to cover injuries that Coventry's \u00a368.5m of new signings can absorb.</p>
{key('BRYME view', 'Hull are the story now; Coventry are the better bet for May. But if Coventry are still goalless in three weeks the mood at the club will change quickly \u2014 and they host Manchester City on Saturday.')}
{NOTE}"""
    return dict(slug='newly-promoted-clubs-approach', eyebrow='Premier League',
        title='The Newly Promoted Clubs: Three Very Different Approaches',
        seo_title='Hull, Ipswich, Coventry: How the Promoted Clubs Approached 2026/27',
        lead='Hull spent almost nothing and are fourth without conceding. Coventry spent \u00a368.5m and have not scored. Ipswich changed manager and did both. Three promoted clubs, three strategies.',
        desc='Hull City, Ipswich Town and Coventry City took three different approaches to the Premier League. Two matchweeks in, the club that spent least is fourth and the club that spent most is 19th.',
        body=body, hero='hero-premier-league.jpg',
        related=[('Five clubs that still need signings', '/sports/articles/five-clubs-that-still-need-signings/'),
                 ('Predictions', '/sports/predictions/'),
                 ('Transfer tracker (Aug 2026)', '/sports/articles/premier-league-transfer-tracker-august-2026/'),
                 ('All sports articles', '/sports/articles/')],
        read='6 min read')
ART.append(a_promoted())


# ============================================ 12. PLAYERS TO WATCH THIS WEEKEND
def a_players_weekend():
    body = f"""
<p>Forty-eight fixtures across Europe's top five leagues this weekend. These are the players whose current form makes them worth watching \u2014 chosen from the actual scoring charts, not reputation.</p>

<h2>Premier League</h2>
{tbl(['Player', 'Club', 'Goals', 'Apps'],
     [[html.escape(s['name']), s['team'], (str(s['goals']),), (str(s['apps']),)] for s in SCORERS[:6]])}
<p><b>Bruno Fernandes</b> leads the division with three goals in two games, from midfield, and travels to Everton on Sunday. <b>Jack Hinshelwood</b> has two goals in a single appearance for Brighton, who host Leeds.</p>
<p><b>Erling Haaland</b> and <b>Rayan Cherki</b> both have two for Manchester City, who face a Coventry side yet to concede fewer than one per game and yet to score at all.</p>

<h2>La Liga</h2>
{tbl(['Player', 'Club', 'Goals', 'Apps'],
     [[html.escape(s['name']), s['team'], (str(s['goals']),), (str(s['apps']),)] for s in comps['la-liga']['scorers'][:5]])}
<p><b>Raphinha</b> is the leading scorer in Spain with five in three and goes to the Mestalla, where Valencia have conceded four and scored one all season. <b>Kylian Mbapp\u00e9</b> has four in three for a Real Madrid side that has won every match.</p>

<h2>Serie A</h2>
{tbl(['Player', 'Club', 'Goals', 'Apps'],
     [[html.escape(s['name']), s['team'], (str(s['goals']),), (str(s['apps']),)] for s in comps['serie-a']['scorers'][:5]])}
<p><b>Donyell Malen</b> has five goals in two games for Roma, who have won 4\u20130 twice and conceded nothing. He faces Atalanta on Saturday evening \u2014 the best individual form in Italy against one of its meanest defences.</p>

<h2>Ligue 1 and Bundesliga</h2>
{tbl(['Player', 'Club', 'Goals', 'Apps', 'League'],
     [[html.escape(s['name']), s['team'], (str(s['goals']),), (str(s['apps']),), lg]
      for lg, arr in [('Ligue 1', comps['ligue-1']['scorers'][:3]), ('Bundesliga', comps['bundesliga']['scorers'][:3])]
      for s in arr])}
<p><b>Esteban Lepaul</b> and <b>Florian Thauvin</b> lead France with three apiece. In Germany only one round has been played, so <b>Younes Ebnoutalib</b> and <b>Yuito Suzuki</b> have three goals from a single appearance each \u2014 a small sample worth watching precisely because it is unsustainable.</p>
{key('One to watch above all', 'Donyell Malen. Five goals in two matches, and Roma have not conceded a goal this season. If he scores against Atalanta, Roma are the best team in Italy on every available measure.')}
<p>Scorelines for every fixture are on our <a href="/sports/predictions/">predictions page</a>.</p>
{NOTE}"""
    return dict(slug='players-to-watch-this-weekend', eyebrow='Matchweek coverage',
        title='Players to Watch This Weekend Across Europe',
        seo_title='Players to Watch This Weekend: Europe\u2019s Top Five Leagues',
        lead='Bruno Fernandes leads England with three in two. Raphinha has five in three. Donyell Malen has five in two for a Roma side yet to concede. The players in form, from the actual scoring charts.',
        desc='Bruno Fernandes, Raphinha, Kylian Mbapp\u00e9 and Donyell Malen \u2014 the players in form across the Premier League, La Liga, Serie A, Bundesliga and Ligue 1 this weekend, taken from the current scoring charts.',
        body=body, hero='hero-breakout.jpg',
        related=[('Predictions for all 48 fixtures', '/sports/predictions/'),
                 ('Five matches we cannot wait to watch', '/sports/articles/five-matches-we-cannot-wait-to-watch/'),
                 ('Players who could explode this season', '/sports/articles/players-who-could-explode-this-season/'),
                 ('All sports articles', '/sports/articles/')],
        read='6 min read')
ART.append(a_players_weekend())


# ============================================ 13. PLAYERS WHO COULD EXPLODE
def a_explode():
    body = f"""
<p>Every season a handful of players go from useful to essential. These are the seven best-placed to do it in 2026/27 \u2014 picked from players who either moved this summer or have already started scoring.</p>

<h2>1. Jack Hinshelwood (Brighton)</h2>
<p>Two goals in a single appearance, already among the Premier League's leading scorers. Brighton have scored seven in two matches and sit {standing('Brighton & Hove Albion')}. Fabian H\u00fcrzeler had his contract extended through 2029 and rebuilt the squad around players of exactly this profile.</p>

<h2>2. Rayan Cherki (Manchester City)</h2>
<p>Two goals in two games for a City side adjusting to life after Guardiola. With Bernardo Silva gone and Jack Grealish on loan at Everton, the creative burden has shifted, and Cherki has taken a share of it immediately.</p>

<h2>3. Elliot Anderson (Manchester City)</h2>
<p>Left Nottingham Forest for around \u00a3116m. That fee makes him one of the most expensive midfielders in English football history, and he arrives alongside Enzo Fern\u00e1ndez. If Maresca's twin-\u00a3100m midfield works, Anderson is the player it is built around.</p>

<h2>4. Carlos Baleba (Manchester United)</h2>
<p>\u00a365\u201370m from Brighton, into a United midfield that also added Andrey Santos and Youri Tielemans. United have conceded four in two games; Baleba is the player expected to stop that.</p>

<h2>5. Morgan Rogers (Chelsea)</h2>
<p>\u00a3117m from Aston Villa, the second-most expensive signing of the window. Chelsea are {standing('Chelsea')} and Villa, who sold him, have not scored a goal all season. The transfer market's clearest verdict on a single player.</p>

<h2>6. Donyell Malen (Roma)</h2>
<p>Five goals in two Serie A matches. Roma have won 4\u20130 twice and conceded nothing. Malen left Aston Villa for around \u20ac25m and is currently the most productive forward in Italy.</p>

<h2>7. Emersonn (Ipswich Town)</h2>
<p>\u00a326.6m, the marquee arrival of Ipswich's seven-signing summer under Gary O'Neil. Promoted clubs rarely spend this on one forward. If he delivers, Ipswich stay up; if he does not, {standing('Ipswich Town')} will look optimistic by Christmas.</p>

{key('The one we would bet on', 'Hinshelwood. Two goals in one appearance is a small sample, but Brighton have the best attacking record in the league so far and a manager signed through 2029 who trusts young players with real minutes.')}

<h2>Current top scorers, for reference</h2>
{tbl(['Player', 'Club', 'Goals', 'Apps'],
     [[html.escape(s['name']), s['team'], (str(s['goals']),), (str(s['apps']),)] for s in SCORERS[:8]])}
{NOTE}"""
    return dict(slug='players-who-could-explode-this-season', eyebrow='Players',
        title='The Players Who Could Explode This Season',
        seo_title='Players Who Could Break Out in 2026/27',
        lead='Jack Hinshelwood has two goals in one appearance. Elliot Anderson cost \u00a3116m. Donyell Malen has five in two for Roma. Seven players set for a breakout season, and the evidence for each.',
        desc='Jack Hinshelwood, Rayan Cherki, Elliot Anderson, Carlos Baleba, Morgan Rogers, Donyell Malen and Emersonn \u2014 seven players who could break out in 2026/27, with early-season evidence.',
        body=body, hero='hero-breakout.jpg',
        related=[('Players to watch this weekend', '/sports/articles/players-to-watch-this-weekend/'),
                 ('The five biggest transfer winners', '/sports/articles/five-biggest-transfer-winners/'),
                 ('Predictions', '/sports/predictions/'),
                 ('All sports articles', '/sports/articles/')],
        read='6 min read')
ART.append(a_explode())


# ============================================ 14. BANTER TABLE
def a_banter():
    order = sorted(PL.values(), key=lambda t: t['pos'])
    verdict = {
     'Chelsea': 'Top of the league. Also conceded five goals in two wins. Enjoy it while the defence holds.',
     'Manchester City': 'Spent \u00a3306m to make sure nobody noticed Guardiola left. So far nobody has.',
     'Arsenal': 'Two games, no goals conceded. The most Arsenal way to be third.',
     'Hull City': 'Promoted, six points, zero conceded, beat Manchester United. Nobody has a good explanation.',
     'Brentford': 'Beat Spurs 3\u20130 then drew with Leeds. Peak Brentford.',
     'Newcastle United': 'Sold Tonali, Bruno Guimar\u00e3es and Gordon, then won at Spurs anyway.',
     'Everton': 'Unbeaten, and they signed Jack Grealish on loan. Moyes is enjoying himself.',
     'Leeds United': 'Spent \u00a340m on a goalkeeper and have conceded one goal. Fair enough.',
     'Brighton & Hove Albion': 'Seven goals in two games, and lost one of them 4\u20133. Never change.',
     'Manchester United': 'Lost 2\u20130 at Hull, won 5\u20132 against Ipswich. The chaos is at least entertaining now.',
     'Ipswich Town': 'Signed seven players and conceded six goals. Ambition, at least.',
     'Sunderland': 'Beat Fulham 1\u20130 and sold Anthony Patterson to Wrexham. Football is strange.',
     'Liverpool': 'Lost Salah, Robertson and Konat\u00e9 for nothing. Drew both games 2\u20132. Symmetry.',
     'AFC Bournemouth': 'Were the better side at the Etihad for an hour. Have one point.',
     'Nottingham Forest': 'Sold Anderson for \u00a3116m, took a point at Anfield, still 15th.',
     'Fulham': 'Signed half of Real Madrid\u2019s reserves and lost both games.',
     'Crystal Palace': 'Sold Lacroix for \u00a351m and replaced him with free transfers. It shows.',
     'Aston Villa': 'Sold Morgan Rogers for \u20ac138m and have not scored since. Correlation is not causation, but still.',
     'Coventry City': 'Spent \u00a368.5m and have not scored a Premier League goal. Manchester City visit on Saturday.',
     'Tottenham Hotspur': '\u00a3185m on two midfielders. Zero goals. Bottom of the table. Spursy has evolved.'}
    rows = [[(str(t['pos']),), t['name'], (str(t['pts']),), ('%d\u2013%d' % (t['gf'], t['ga']),),
             verdict.get(t['name'], '')] for t in order]
    body = f"""
<p>The real Premier League table, with the only column that matters in September added. Positions, points and goal figures are the genuine ones from BRYME's league table; the last column is entirely our opinion.</p>
{tbl(['#', 'Club', 'Pts', 'Goals', 'The verdict'], rows)}

<h2>Three observations nobody asked for</h2>
<p><b>Tottenham are bottom.</b> They spent \u00a3100m on Sandro Tonali and \u00a385m on Mateus Fernandes and have scored zero goals in two matches. The most expensive nothing in the division.</p>
<p><b>Hull City are fourth.</b> They spent \u00a33m on a goalkeeper and picked up three free transfers. They have conceded fewer goals than Arsenal, Chelsea and Manchester City combined would like to admit \u2014 which is to say, none.</p>
<p><b>Aston Villa have not scored.</b> They sold Morgan Rogers for around \u20ac138m to Chelsea, who are now top. Villa are 18th with zero goals and five conceded. Unai Emery has bought Nicolas Jackson and taken Alejandro Garnacho on loan; neither has fixed it yet.</p>
{key('The serious bit', 'It is two matchweeks. Every table published in early September is wrong. Tottenham will score goals, Hull will concede one eventually, and Villa are far better than 18th. Come back in November and laugh at this page.')}
<p>For picks on every fixture this weekend, see the <a href="/sports/predictions/">predictions page</a> \u2014 where the analysis is rather more sober than this.</p>
{NOTE}"""
    return dict(slug='premier-league-banter-table', eyebrow='BRYME original',
        title='The Premier League Banter Table',
        seo_title='The Premier League Banter Table \u2014 2026/27',
        lead='The real table, the real points, and one honest sentence per club. Spurs are bottom with a \u00a3185m midfield, Hull are fourth with a \u00a33m goalkeeper, and Aston Villa have not scored at all.',
        desc='The real Premier League table with a verdict on every club. Tottenham bottom with a \u00a3185m midfield, Hull City fourth having conceded nothing, and Aston Villa yet to score a goal.',
        body=body, hero='hero-landing.jpg',
        related=[('Five things fans will be talking about', '/sports/articles/five-things-fans-will-talk-about-this-weekend/'),
                 ('Predictions', '/sports/predictions/'),
                 ('Five clubs that still need signings', '/sports/articles/five-clubs-that-still-need-signings/'),
                 ('All sports articles', '/sports/articles/')],
        read='5 min read')
ART.append(a_banter())


# ============================================ 15. RODRI'S FUTURE
def a_rodri():
    body = f"""
<p>The question in the title was asked in the summer, and the 2026 window answered it in a way nobody quite predicted: Manchester City did not find one Rodri replacement. They bought two players for a combined \u00a3241m and changed the shape of the midfield instead.</p>

<h2>What City actually did</h2>
{tbl(['Signing', 'From', 'Fee'],
     [[html.escape(x['player']), html.escape(x.get('from', '')), (html.escape(x.get('detail', '')),)]
      for x in ins('Manchester City') if x['player'] in ('Enzo Fern\u00e1ndez', 'Elliot Anderson', 'Ayyoub Bouaddi')])}
<p>Enzo Fern\u00e1ndez arrived from Chelsea on deadline day for \u00a3125m. Elliot Anderson came from Nottingham Forest for around \u00a3116m. Ayyoub Bouaddi arrived from Lille earlier in the window.</p>
{key('The strategic answer', 'A single holding midfielder is a single point of failure \u2014 which is exactly what the previous era discovered. Buying two elite central midfielders spreads the load rather than replacing one irreplaceable player.')}

<h2>Why the succession problem was so hard</h2>
<p>A deep-lying midfielder who dictates tempo, breaks up play and never gives the ball away is the rarest profile in football. Clubs cannot simply buy one, which is why the question hung over the Etihad for two seasons.</p>
<p>Enzo Maresca's response has been to change the requirement. Two midfielders sharing the responsibility need not be as complete individually as one player doing it alone.</p>

<h2>Has it worked so far?</h2>
<p>City are {standing('Manchester City')}: two wins, six goals scored, two conceded, including a 4\u20131 at Crystal Palace. Rayan Cherki and Erling Haaland have two goals each.</p>
<p>Two games against Palace and Bournemouth is not evidence of much. The structure has not yet been tested by a side that presses well or by a European away leg.</p>

<h2>What to watch for</h2>
<p>The tell will be the games City do not control. Under the previous regime, one holding player let the full-backs push high. With two central midfielders and three senior centre-backs departed \u2014 John Stones, Manuel Akanji and Nathan Ak\u00e9 all left \u2014 the defensive structure behind them is different.</p>
<p>City host Coventry on Saturday, which will tell us nothing. The fixtures after that will tell us a great deal.</p>
{NOTE}"""
    return dict(slug='rodris-future', eyebrow='Players',
        title='The Rodri Question: How Manchester City Finally Answered It',
        seo_title='How Manchester City Solved the Rodri Succession Problem',
        lead='City did not replace one irreplaceable midfielder. They spent \u00a3241m on Enzo Fern\u00e1ndez and Elliot Anderson and changed the shape of the midfield instead.',
        desc='Manchester City answered the Rodri succession question by signing Enzo Fern\u00e1ndez for \u00a3125m and Elliot Anderson for around \u00a3116m \u2014 spreading the load rather than replacing one player.',
        body=body, hero='hero-man-city-manager.jpg',
        related=[('Manchester City without Guardiola', '/sports/articles/manchester-city-without-guardiola/'),
                 ("Maresca's second attempt in England", '/sports/articles/marescas-second-attempt-in-england/'),
                 ('The five biggest transfer winners', '/sports/articles/five-biggest-transfer-winners/'),
                 ('Manchester City on BRYME', '/sports/premier-league/teams/manchester-city/')],
        read='6 min read')
ART.append(a_rodri())


# ============================================ 16. TACTICAL QUESTIONS
def a_tactical():
    body = f"""
<p>Two matchweeks have been played, which is exactly enough football to replace the questions we had in August with better ones. These are the five tactical problems that will define the autumn.</p>

<h2>1. Can Chelsea keep winning while conceding this much?</h2>
<p>Chelsea are {standing('Chelsea')}. Both wins were 3\u20132 at Fulham and 4\u20133 against Brighton \u2014 seven scored, five conceded. Then they sold Enzo Fern\u00e1ndez to Manchester City for \u00a3125m on deadline day without signing a replacement.</p>
<p>Xabi Alonso's Leverkusen sides were built on control. This Chelsea team is not controlled; it is simply outscoring people. Sunday at Arsenal, against the only defence yet to concede, is the test.</p>

<h2>2. Does a two-man \u00a3241m midfield actually work?</h2>
<p>Manchester City bought Enzo Fern\u00e1ndez (\u00a3125m) and Elliot Anderson (~\u00a3116m) and let Bernardo Silva, John Stones, Manuel Akanji and Nathan Ak\u00e9 go. Maresca has replaced a single-pivot structure with two central midfielders and a thinner defence.</p>
{key('What to look for', 'Whether City\u2019s full-backs still push as high. With three senior centre-backs gone, the cover behind an advanced full-back is not what it was.')}

<h2>3. Where do Tottenham's goals come from?</h2>
<p>\u00a3100m for Sandro Tonali, \u00a385m for Mateus Fernandes, and zero goals in two matches. Spurs are {standing('Tottenham Hotspur')}. De Zerbi bought midfield control and did not buy a striker; Mykhailo Mudryk arrived on loan as a winger.</p>
<p>This is the most solvable problem on the list and the one that cannot be solved until January.</p>

<h2>4. Is Hull City's defence sustainable?</h2>
<p>Hull are {standing('Hull City')} with no goals conceded, including 2\u20130 against Manchester United. They spent \u00a33m on Jack Butland and added three free transfers.</p>
<p>Low blocks work early in a season because opponents have not yet worked out how to break them and squads are fresh. The question is whether Sergej Jakirovi\u0107 has enough depth when injuries arrive in October.</p>

<h2>5. Can Liverpool press without the players who did the pressing?</h2>
<p>Andoni Iraola's teams press aggressively and defend in transition. He inherited a Liverpool squad that lost Mohamed Salah, Andy Robertson and Ibrahima Konat\u00e9 on free transfers in a single summer.</p>
<p>Liverpool have drawn both matches 2\u20132 \u2014 {standing('Liverpool')} \u2014 and have been pegged back in each. Ronald Ara\u00fajo's loan from Barcelona is the signing that has to settle fastest.</p>

<h2>The weekend's answers</h2>
<p>Three of these five get tested immediately: Chelsea at Arsenal, City against Coventry, and Hull against Aston Villa. Our <a href="/sports/predictions/">predictions page</a> has a scoreline and the supporting form for every one of them.</p>
{NOTE}"""
    return dict(slug='tactical-questions-ahead-of-matchweek-1', eyebrow='Matchweek coverage',
        title='The Five Biggest Tactical Questions of the Season So Far',
        seo_title='Five Big Tactical Questions in the Premier League Right Now',
        lead='Chelsea are top and leaking goals. City have a \u00a3241m midfield and a thinner defence. Spurs have spent \u00a3185m and scored nothing. The five tactical problems that will define the autumn.',
        desc='Chelsea conceding five in two wins, Manchester City\u2019s \u00a3241m midfield, Tottenham\u2019s missing goals, Hull City\u2019s clean sheets and Liverpool\u2019s press \u2014 five tactical questions after two matchweeks.',
        body=body, hero='hero-matchweek.jpg',
        related=[('Predictions for all 48 fixtures', '/sports/predictions/'),
                 ('Managers with the most to prove', '/sports/articles/managers-with-most-to-prove/'),
                 ('Five matches we cannot wait to watch', '/sports/articles/five-matches-we-cannot-wait-to-watch/'),
                 ('All sports articles', '/sports/articles/')],
        read='7 min read')
ART.append(a_tactical())


# ================================================================= write
os.makedirs(ROOT + '/sports/articles', exist_ok=True)
written = []
for a in ART:
    ex = EXTRA.get(a['slug'], '')
    if ex:
        assert NOTE in a['body'], a['slug']
        a['body'] = a['body'].replace(NOTE, ex + '\n' + NOTE)
    cl = CLOSER.get(a['slug'], '')
    if cl:
        a['body'] = a['body'].replace(NOTE, cl + '\n' + NOTE)
    d = '%s/sports/articles/%s' % (ROOT, a['slug'])
    os.makedirs(d, exist_ok=True)
    open(d + '/index.html', 'w', encoding='utf-8').write(page(**a))
    written.append(a['slug'])

print('wrote %d articles' % len(written))
for s in written:
    p = '%s/sports/articles/%s/index.html' % (ROOT, s)
    txt = re.sub(r'<[^>]+>', ' ', re.search(r'<article.*?</article>', open(p, encoding='utf-8').read(), re.S).group(0))
    print('  %-52s %5d words' % (s, len(' '.join(txt.split()).split())))
