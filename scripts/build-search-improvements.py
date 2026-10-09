#!/usr/bin/env python3
"""Final, deterministic editorial overrides for five audited search-priority pages.
Run LAST: legacy depth injectors must not append unsourced filler after the reviewed
copy. Existing site shells, consent, analytics and ad wiring stay intact. Inputs
live in content/search-improvements; no network, clock or package dependency.
"""
import html
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'content/search-improvements'
PAGES=json.loads((DATA/'pages.json').read_text())
DATE='2026-10-09'
STYLE='''<style id="search-improvements-style">.si-article{max-width:850px;margin:0 auto;padding:32px 24px 56px;font-size:18px;line-height:1.75;overflow-wrap:anywhere}.si-article h1{font-size:clamp(2rem,5vw,3.3rem);line-height:1.16;margin:18px 0 24px}.si-article h2{font-size:clamp(1.5rem,3vw,2rem);line-height:1.25;margin:42px 0 16px;scroll-margin-top:100px}.si-article h3{font-size:1.2rem;margin:24px 0 12px}.si-article p{margin:16px 0}.si-article nav{padding:18px 24px;border:1px solid #89978e;border-radius:4px;margin:28px 0}.si-article li{margin:10px 0}.si-article .byline{font-size:14px;line-height:1.6}.si-article a{text-decoration:underline;text-underline-offset:3px}.si-article a:focus-visible,.si-table:focus-visible{outline:3px solid #8d651b;outline-offset:4px}.si-table{max-width:100%;overflow-x:auto}.si-table table{width:100%;border-collapse:collapse;font-size:15px}.si-table caption{text-align:left;font-size:13px;margin-bottom:12px}.si-table td,.si-table th{text-align:left;padding:10px;border-bottom:1px solid #89978e}.si-article code{overflow-wrap:anywhere}@media(max-width:500px){.si-article{padding:24px 18px 40px;font-size:17px}.si-article nav{padding:12px 16px}.si-table td,.si-table th{padding:8px}} </style>'''

def patch_html(text,record):
    fragment=(DATA/record['fragment']).read_text()
    heading=html.unescape(re.search(r'<h1>(.*?)</h1>',fragment,re.S).group(1))
    match=re.search(r'<main\b([^>]*)>(.*?)</main>',text,re.S)
    if not match:raise RuntimeError('Missing main: '+record['route'])
    ads=re.findall(r'<aside\b[^>]*\bdata-adband=["\'][^"\']+["\'][^>]*>.*?</aside>',match.group(2),re.S)
    desk='writers' if record['route'].startswith('/writers/') else 'entertainment'
    nav=f'<nav aria-label="Breadcrumb"><a href="/{desk}/">{desk.title()}</a> / '+ ('<a href="/writers/writing/">Writing opportunities</a>' if desk=='writers' else '<a href="/entertainment/recommendations/">Recommendations</a>')+'</nav>'
    body=''.join(ads)+'<article class="si-article" data-search-improved="2026-10-09">'+nav+fragment+'</article>'
    text=text[:match.start()]+f'<main{match.group(1)}>'+body+'</main>'+text[match.end():]
    text=re.sub(r'<title>.*?</title>',lambda m:'<title>'+html.escape(record['title'])+'</title>',text,count=1,flags=re.S)
    def meta(m):
        tag=m.group(0)
        key=re.search(r'(?:name|property)=["\']([^"\']+)',tag,re.I)
        if not key:return tag
        value=record['description'] if key.group(1) in ['description','og:description','twitter:description'] else record['title'] if key.group(1) in ['og:title','twitter:title'] else DATE if key.group(1)=='article:modified_time' else None
        if value is not None:tag=re.sub(r'content=["\'][^"\']*["\']',lambda m:'content="'+html.escape(value,quote=True)+'"',tag)
        return tag
    text=re.sub(r'<meta\b[^>]*>',meta,text,flags=re.I)
    def schema(m):
        data=json.loads(m.group(2))
        def walk(obj):
            if isinstance(obj,list):
                for v in obj:walk(v)
            elif isinstance(obj,dict):
                if obj.get('@type') in ['Article','NewsArticle','BlogPosting','WebPage']:
                    obj['headline']=heading;obj['description']=record['description'];obj['dateModified']=DATE
                if obj.get('@type')=='ListItem' and obj.get('item')=='https://thebryme.com'+record['route']:obj['name']=heading
                for value in list(obj.values()):
                    if isinstance(value,(dict,list)):walk(value)
        walk(data)
        return m.group(1)+json.dumps(data,ensure_ascii=False)+m.group(3)
    text=re.sub(r'(<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',schema,text,flags=re.S)
    # Entertainment's legacy Article lived inside main, which was replaced.
    # Restore one accurate Article in head, not an invisible duplicate body.
    if desk=='entertainment' and not re.search(r'"@type"\s*:\s*"Article"',text):
        article={'@context':'https://schema.org','@type':'Article','headline':heading,'description':record['description'],'datePublished':'2026-09-09','dateModified':DATE,'mainEntityOfPage':'https://thebryme.com'+record['route'],'author':{'@type':'Organization','name':'BRYME Entertainment desk'},'publisher':{'@type':'Organization','name':'THE BRYME'}}
        text=text.replace('</head>','<script type="application/ld+json">'+json.dumps(article,ensure_ascii=False)+'</script></head>',1)
    text=re.sub(r'<style id="search-improvements-style">.*?</style>','',text,flags=re.S)
    text=text.replace('</head>',STYLE+'</head>',1)
    return text

def main():
    count=0
    for record in PAGES:
        rel=record['route'].strip('/')+'/index.html'
        paths=[ROOT/rel,ROOT/'public'/rel]
        if rel.startswith('entertainment/'):paths.append(ROOT/'ecosystem'/rel)
        for path in paths:
            if not path.is_file():raise RuntimeError('Expected generated page: '+str(path))
            old=path.read_text();new=patch_html(old,record)
            if old!=new:path.write_text(new);count+=1
        desk=record['route'].split('/')[1]
        maps=[ROOT/desk/'sitemap.xml',ROOT/'public'/desk/'sitemap.xml']
        if desk=='entertainment':maps.append(ROOT/'ecosystem'/desk/'sitemap.xml')
        for path in maps:
            old=path.read_text();url='https://thebryme.com'+record['route']
            def patch_url(m):
                block=m.group(0)
                if '<loc>'+url+'</loc>' not in block:return block
                if '<lastmod>' in block:return re.sub(r'<lastmod>.*?</lastmod>','<lastmod>'+DATE+'</lastmod>',block)
                return block.replace('</url>','<lastmod>'+DATE+'</lastmod></url>')
            new=re.sub(r'<url\b[^>]*>.*?</url>',patch_url,old,flags=re.S)
            if old!=new:path.write_text(new)
    print(f'Search improvements: {len(PAGES)} routes, {count} page writes; canonical URLs unchanged')
if __name__=='__main__':main()
