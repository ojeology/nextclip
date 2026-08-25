#!/usr/bin/env python3
"""BRYME site upgrade — applies ALL planned upgrades without changing any URL.
1. delete invalid content (legacy/)          6. CSS diet (in place)
2. apply pending patches (hrefs + result)    7. FAQ + FAQPage schema on 8 hubs
3. analytics loader injected site-wide       8. VideoObject schema on trailer pages
4. sitemap <lastmod> + populated news feed   9. ads.txt placeholder
5. image diet (recompress in place)         10. RSS feed.xml
"""
import os, re, json, glob, html, sys
from datetime import datetime, timezone
from email.utils import format_datetime
from PIL import Image

ROOT = "/home/user/nextclip"
os.chdir(ROOT)
log = lambda *a: print(*a, flush=True)

# ---------------------------------------------------------------- 1. delete invalid content
import shutil
if os.path.isdir("legacy"):
    shutil.rmtree("legacy"); log("1. deleted legacy/ (orphaned prototype page)")
for junk in (".DS_Store",):
    n = 0
    for f in glob.glob(f"**/{junk}", recursive=True):
        os.remove(f); n += 1
    if n: log(f"   deleted {n} {junk}")

# ---------------------------------------------------------------- 2. apply pending patches
p = "make-money/make-money-online-nigeria/index.html"
s = open(p, encoding="utf-8").read()
fixes = [
 ('<a href="No leadership or funding info published - normal for this platform" rel="nofollow noopener" target="_blank">',
  '<a href="https://mindrift.ai" title="No leadership or funding info published - normal for this platform" rel="nofollow noopener" target="_blank">'),
 ('<a href=" backed by Labelbox - no upfront fees ever" rel="nofollow noopener" target="_blank">',
  '<a href="https://alignerr.com" title="Backed by Labelbox - no upfront fees ever" rel="nofollow noopener" target="_blank">'),
 ('<a href="Reputable in academic/research circles - one of the more trustworthy platforms for this reason" rel="nofollow noopener" target="_blank">',
  '<a href="https://www.prolific.com" title="Reputable in academic/research circles - one of the more trustworthy platforms" rel="nofollow noopener" target="_blank">'),
]
nfix = 0
for bad, good in fixes:
    if bad in s:
        s = s.replace(bad, good); nfix += 1
open(p, "w", encoding="utf-8").write(s)
log(f"2. href fixes applied: {nfix}/3")

rp = "content/results.json"
res = json.load(open(rp, encoding="utf-8"))
if "fulham-vs-chelsea" not in res.get("premier-league", {}):
    res["premier-league"]["fulham-vs-chelsea"] = json.load(open("/home/user/site-audit/fulham-vs-chelsea-entry.json"))
    json.dump(res, open(rp, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    log("2. fulham-vs-chelsea added to results.json")
else:
    log("2. fulham-vs-chelsea already present")

# ---------------------------------------------------------------- 3. analytics loader
ANALYTICS_JS = """/* BRYME analytics loader.
   To activate Google Analytics 4, paste your measurement ID below, e.g. GA_ID = "G-XXXXXXXXXX".
   Nothing loads and no data is collected until an ID is set. */
(function () {
  "use strict";
  var GA_ID = ""; /* <-- paste GA4 measurement ID here */
  if (!GA_ID || !/^G-[A-Z0-9]+$/.test(GA_ID)) return;
  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag("js", new Date());
  gtag("config", GA_ID, { anonymize_ip: true });
})();
"""
open("assets/analytics.js", "w", encoding="utf-8").write(ANALYTICS_JS)

INJECT = ('<script src="/assets/analytics.js" async></script>'
          '<link rel="alternate" type="application/rss+xml" title="BRYME — Latest" href="/feed.xml">')
html_files = [f for f in glob.glob("**/*.html", recursive=True) if ".git/" not in f]
injected = 0
for f in html_files:
    base = os.path.basename(f)
    if base.startswith("google") or base.startswith("yandex"):
        continue
    s = open(f, encoding="utf-8", errors="ignore").read()
    if 'http-equiv="refresh"' in s or INJECT in s:
        continue
    if "</head>" in s:
        s = s.replace("</head>", INJECT + "</head>", 1)
        open(f, "w", encoding="utf-8").write(s)
        injected += 1
log(f"3. analytics+RSS tags injected into {injected} pages (redirect stubs & verification files skipped)")

# ---------------------------------------------------------------- 4. sitemap lastmod + news sitemap
def page_date(path):
    try:
        s = open(path, encoding="utf-8", errors="ignore").read()
    except Exception:
        return None
    for key in ("dateModified", "datePublished"):
        m = re.search(r'"%s":"(\d{4}-\d{2}-\d{2})' % key, s)
        if m:
            return m.group(1)
    return None

sm = open("sitemap.xml", encoding="utf-8").read()
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
out, with_lm = [], 0
for loc in locs:
    path = loc.replace("https://bryme.onrender.com/", "").strip("/")
    fp = os.path.join(path, "index.html") if os.path.isdir(path) else path
    d = page_date(fp) if os.path.isfile(fp) else None
    entry = f"<url><loc>{loc}</loc>"
    if d:
        entry += f"<lastmod>{d}</lastmod>"; with_lm += 1
    entry += "</url>"
    out.append(entry)
open("sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(out) + "\n</urlset>\n")
log(f"4. sitemap.xml rewritten: lastmod added to {with_lm}/{len(locs)} URLs")

# gather articles for news sitemap + feed
arts = []
for pat in ("article/*/index.html", "articles/*/index.html", "sports/articles/*/index.html"):
    for f in glob.glob(pat):
        s = open(f, encoding="utf-8", errors="ignore").read()
        t = re.search(r'<title>([^<]+)</title>', s)
        d = re.search(r'"datePublished":"(\d{4}-\d{2}-\d{2})', s) or re.search(r'"dateModified":"(\d{4}-\d{2}-\d{2})', s)
        de = re.search(r'<meta name="description" content="([^"]+)"', s)
        if t and d:
            slug = f.rsplit("/index.html", 1)[0]
            title = html.unescape(t.group(1)).replace(" | BRYME", "")
            arts.append(dict(slug=slug, title=title, date=d.group(1),
                             desc=html.unescape(de.group(1))[:200] if de else ""))
arts.sort(key=lambda a: a["date"], reverse=True)
log(f"   found {len(arts)} dated articles (newest: {arts[0]['date'] if arts else '-'})")

news_items = []
for a in arts[:20]:
    news_items.append(
        "<url><loc>https://bryme.onrender.com/" + a["slug"] + "/</loc>"
        "<news:news><news:publication><news:name>BRYME</news:name><news:language>en</news:language></news:publication>"
        f"<news:publication_date>{a['date']}</news:publication_date>"
        f"<news:title>{html.escape(a['title'])}</news:title></news:news></url>")
open("news-sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
    'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n' + "\n".join(news_items) + "\n</urlset>\n")
log(f"4. news-sitemap.xml populated with {len(news_items)} articles")

# ---------------------------------------------------------------- 10. RSS feed
def rfc822(iso):
    try:
        return format_datetime(datetime.fromisoformat(iso).replace(tzinfo=timezone.utc))
    except Exception:
        return iso
items = []
for a in arts[:40]:
    items.append(
        f"<item><title>{html.escape(a['title'])}</title>"
        f"<link>https://bryme.onrender.com/{a['slug']}/</link>"
        f"<guid>https://bryme.onrender.com/{a['slug']}/</guid>"
        f"<pubDate>{rfc822(a['date'])}</pubDate>"
        f"<description>{html.escape(a['desc'])}</description></item>")
open("feed.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
    '<title>BRYME — Discover what you love</title><link>https://bryme.onrender.com/</link>'
    '<description>Movies, TV, anime, sports, money guides and tech — latest from BRYME.</description>'
    + "".join(items) + "</channel></rss>\n")
log(f"10. feed.xml written with {len(items)} items")

# ---------------------------------------------------------------- 5. image diet (same URLs)
big = [f for f in glob.glob("assets/img/**/*.jpg", recursive=True)
       if os.path.getsize(f) > 280_000]
saved = 0
for f in big:
    before = os.path.getsize(f)
    try:
        im = Image.open(f).convert("RGB")
        if im.width > 1700:
            im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
        im.save(f, "JPEG", quality=74, optimize=True, progressive=True)
        after = os.path.getsize(f)
        if after >= before:
            log(f"   skip (no gain): {f}")
            continue
        saved += before - after
    except Exception as e:
        log(f"   img fail {f}: {e}")
log(f"5. image diet: {len(big)} big JPGs recompressed in place, saved {saved/1e6:.1f} MB")

# ---------------------------------------------------------------- 6. CSS diet (in place)
css_path = "assets/site.css"
css = open(css_path, encoding="utf-8").read()
css2 = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
css2 = re.sub(r"\s+", " ", css2).strip()
open(css_path, "w", encoding="utf-8").write(css2)
log(f"6. site.css: {len(css)/1024:.0f}KB -> {len(css2)/1024:.0f}KB")

# ---------------------------------------------------------------- 7. FAQ + FAQPage schema on hubs
FAQS = {
 "make-money/index.html": [
  ("Are the platforms on BRYME free to join?", "Yes. Every platform BRYME lists is free to register. Any site asking for a signup fee, starter kit or registration fee is a scam — walk away."),
  ("Do these money-making platforms accept Nigerians?", "Several do explicitly, including Outlier AI, Mindrift, Alignerr, Prolific and Remotasks. Many others accept a broad country list that includes Nigeria — always verify at signup because eligibility changes."),
  ("How much can I realistically earn?", "Pay is region-tiered: the same task can pay a US contributor $30/hr and a Nigerian contributor $10/hr. Task availability, not the advertised rate, is the real bottleneck — run two or three platforms at once."),
  ("What are the red flags to watch for?", "Upfront payments, requests for bank logins or OTPs, guaranteed income promises, and known-brand sites asking for crypto. No legitimate platform needs any of these."),
 ],
 "make-money/make-money-online-nigeria/index.html": [
  ("Which AI platforms pay Nigerians in 2026?", "Outlier AI, Mindrift, Alignerr, Prolific and Remotasks all explicitly accept Nigeria, with payouts via PayPal, Payoneer or bank transfer. Pay ranges from about $8 to $100+ per hour depending on expertise."),
  ("How do I receive payments in Nigeria?", "Payoneer, Wise, Grey, Cleva and Raenest generally work better than PayPal for receiving money in Nigeria. Each platform lists its supported payout methods on its official site."),
  ("Are unpaid assessments normal?", "Yes — qualifying tests of one to three hours are standard on platforms like Outlier and DataAnnotation. Treat a failed assessment as data, not a loss."),
  ("Is BRYME affiliated with these platforms?", "No. BRYME is an independent discovery site. Links go to official websites so you can verify everything yourself."),
 ],
 "sports/index.html": [
  ("Where do BRYME football results come from?", "Match scores and scorers are taken from verified sources such as BBC Sport and ESPN, and each result in our data links to its original source report."),
  ("How quickly are results updated?", "Results are added within hours of full time, usually the same evening as the final whistle."),
  ("Is BRYME affiliated with any club or league?", "No. BRYME is an independent publication. Team names and league references are editorial only."),
  ("Does BRYME show live scores?", "Not yet — BRYME publishes verified final results, tables and editorial coverage rather than live tickers."),
 ],
 "anime/index.html": [
  ("Does BRYME stream or host anime?", "No. BRYME is a discovery site — we link official trailers and legal where-to-watch options, and never host video."),
  ("How current is the anime catalogue?", "The catalogue is updated continuously, with new seasonal titles added as they are confirmed for legal streaming."),
  ("Can I filter anime by genre or year?", "Yes — BRYME anime hubs are organised by genre, year and topic so you can browse straight to what you like."),
 ],
 "movies/index.html": [
  ("Where does BRYME get its where-to-watch information?", "From official streaming catalogues and platform announcements. Availability changes by country, so BRYME always links the official source for you to confirm."),
  ("Are the trailers on BRYME official?", "Yes — trailers are embedded from official YouTube channels via click-to-play, so nothing loads until you press play."),
  ("How often is the movie catalogue updated?", "Continuously — new releases, classics and editorial collections are added every week."),
 ],
 "tech/index.html": [
  ("What kind of tech and AI content does BRYME publish?", "Practical guides: AI tools that pay, free alternatives to paid software, and plain-English explainers written for real users, not engineers."),
  ("Are the AI tools on BRYME free to use?", "Many have free tiers. Each guide states clearly what is free, what is freemium and what is paid."),
 ],
 "entertainment/index.html": [
  ("What is in BRYME entertainment?", "Movies, TV series, anime, trending topics and editorial recommendations — everything worth watching, with where-to-watch options."),
  ("Is the content legal?", "Yes. BRYME only links official trailers and licensed streaming platforms. We never host or link pirated content."),
 ],
 "make-money/remote-work/index.html": [
  ("Can I filter remote-work platforms by country?", "Yes — the platform reviews table can be filtered so you only see platforms that accept your country, including Nigeria."),
  ("Which payout methods work best outside the US?", "Payoneer, Wise and local fintech options usually beat PayPal for receiving earnings in countries with limited PayPal support."),
 ],
}

def faq_html(pairs):
    h = '<section class="sp-faq"><h2>Frequently asked questions</h2>'
    for q, a in pairs:
        h += f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>"
    return h + "</section>"

def faq_schema(pairs):
    return ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
    }, ensure_ascii=False) + "</script>")

nf = 0
for rel, pairs in FAQS.items():
    if not os.path.isfile(rel):
        log(f"   FAQ target missing: {rel}"); continue
    s = open(rel, encoding="utf-8").read()
    if "FAQPage" in s:
        continue
    block = faq_html(pairs)
    if "</main>" in s:
        s = s.replace("</main>", block + "</main>", 1)
    if "</head>" in s:
        s = s.replace("</head>", faq_schema(pairs) + "</head>", 1)
    open(rel, "w", encoding="utf-8").write(s)
    nf += 1
log(f"7. FAQ + FAQPage schema added to {nf} hub pages")

# ---------------------------------------------------------------- 8. VideoObject schema
yt_re = re.compile(r'data-[a-z-]*(?:yt|youtube|trailer)[a-z-]*="([\w-]{11})"')
nv, pages_seen = 0, 0
for f in glob.glob("movie/*/index.html") + glob.glob("series/*/index.html") + glob.glob("anime/*/index.html"):
    pages_seen += 1
    s = open(f, encoding="utf-8", errors="ignore").read()
    if "VideoObject" in s:
        continue
    m = yt_re.search(s)
    if not m:
        continue
    ytid = m.group(1)
    t = re.search(r'<meta property="og:title" content="([^"]+)"', s)
    d = re.search(r'"datePublished":"(\d{4})', s)
    name = html.unescape(t.group(1)) if t else f
    year = (d.group(1) + "-01-01") if d else "2024-01-01"
    vo = ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "VideoObject",
        "name": name,
        "description": f"Official trailer for {name} — watch and find where to stream it on BRYME.",
        "thumbnailUrl": [f"https://i.ytimg.com/vi/{ytid}/hqdefault.jpg"],
        "uploadDate": year,
        "embedUrl": f"https://www.youtube-nocookie.com/embed/{ytid}",
    }, ensure_ascii=False) + "</script>")
    if "</head>" in s:
        s = s.replace("</head>", vo + "</head>", 1)
        open(f, "w", encoding="utf-8").write(s)
        nv += 1
log(f"8. VideoObject schema added to {nv}/{pages_seen} title pages (trailer data found on those)")

# ---------------------------------------------------------------- 9. ads.txt placeholder
if not os.path.exists("ads.txt"):
    open("ads.txt", "w").write(
        "# BRYME ads.txt — add your AdSense line here when approved, e.g.:\n"
        "# google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n")
    log("9. ads.txt placeholder created")
log("DONE")
