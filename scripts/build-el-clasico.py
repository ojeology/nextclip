#!/usr/bin/env python3
"""Build the single sourced Clásico guide. No network or third-party dependencies.
Run before build-routing.py; --stage also updates routed review artifacts.
"""
import argparse
import html
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'el-clasico-barcelona-real-madrid'
ROUTE = '/sports/' + SLUG + '/'
URL = 'https://thebryme.com' + ROUTE
TITLE = 'El Clásico: Barcelona vs Real Madrid Guide | BRYME'
DESC = 'Barcelona vs Real Madrid on 25 October 2026: Nigeria kickoff guidance, viewing checks, team news, title-race scenarios and El Clásico history.'
CSS = '''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}body{margin:0;background:#fafaf8;color:#14213d;font:18px/1.75 system-ui,sans-serif}a{color:#20573e;text-underline-offset:4px;overflow-wrap:anywhere}a:hover{color:#102e21}a:focus-visible,[tabindex]:focus-visible{outline:3px solid #a96015;outline-offset:5px}.skip{position:absolute;left:12px;top:-80px;background:white;padding:8px}.skip:focus{top:8px}.mast{max-width:1160px;margin:auto;padding:24px;display:flex;justify-content:space-between;border-bottom:1px solid #b9c5be;gap:20px;flex-wrap:wrap}.mast a{font-weight:750;text-decoration:none}.mast nav{display:flex;gap:22px;font-size:14px}main{max-width:920px;margin:auto;padding:48px 24px}h1,h2,h3{font-family:Georgia,serif;line-height:1.14;letter-spacing:-.025em}h1{font-size:clamp(2.5rem,6vw,4.5rem);max-width:850px;margin:20px 0}h2{font-size:clamp(1.8rem,4vw,2.6rem);margin-top:0}h3{font-size:1.4rem;margin:30px 0 12px}p,li{max-width:76ch}.eyebrow,.byline{font-size:13px;letter-spacing:.08em}.eyebrow{color:#20573e;font-weight:800}.dek{font-size:22px;color:#46576a}.fixture{background:#142d23;color:#fff;padding:28px;border-radius:3px;margin:30px 0}.fixture span{font-size:12px;letter-spacing:.16em}.fixture strong{display:block;font:700 clamp(1.6rem,4vw,2.6rem)/1.3 Georgia,serif;margin-top:12px}.fixture i{font-size:.65em;font-weight:400}.fixture p{font-size:16px;margin-bottom:0}.contents{background:#edf1eb;border:1px solid #bdcabc;padding:28px;margin:44px 0}.contents h2{font-size:1.4rem}.contents ol{columns:2;padding-left:22px}.contents li{padding:5px 12px 5px 0;break-inside:avoid}section{padding:40px 0;border-top:1px solid #bdcabc}.notice{border-left:4px solid #96661c;background:#f4efe3;padding:16px 24px;margin:24px 0}.notice h3{margin-top:0}.table-wrap{overflow-x:auto;margin:24px 0;max-width:100%}table{border-collapse:collapse;width:100%;font-size:15px;text-align:left}caption{text-align:left;font-size:13px;color:#46576a;margin-bottom:12px}td,th{padding:12px;border-bottom:1px solid #bdcabc;white-space:normal}thead{background:#edf1eb}footer{border-top:1px solid #bdcabc;max-width:920px;margin:auto;padding:30px 24px;font-size:14px}li{margin-bottom:10px}@media(max-width:600px){body{font-size:17px}main{padding-top:28px}.contents ol{columns:1}.fixture{padding:22px}.mast{padding:20px 24px}td,th{padding:8px}section{padding:30px 0}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'''

def build(stage=False):
    body = (ROOT/'content/sports-media/el-clasico-guide.html').read_text()
    # No fake publication date, author credentials or event state. This is a guide.
    schema = {'@context':'https://schema.org','@type':'Article','headline':'Barcelona vs Real Madrid: the El Clásico guide','description':DESC,'mainEntityOfPage':URL,'dateModified':'2026-10-09','inLanguage':'en','about':[{'@type':'SportsTeam','name':'FC Barcelona'},{'@type':'SportsTeam','name':'Real Madrid'}]}
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{TITLE}</title><meta name="description" content="{html.escape(DESC,quote=True)}"><meta name="robots" content="index,follow"><link rel="canonical" href="{URL}">
<meta property="og:type" content="article"><meta property="og:site_name" content="THE BRYME"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{html.escape(DESC,quote=True)}"><meta property="og:url" content="{URL}"><meta name="twitter:card" content="summary"><meta name="theme-color" content="#142d23"><style>{CSS}</style>
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body><a class="skip" href="#main">Skip to content</a><header class="mast"><a href="/sports/">THE BRYME <span> / SPORT</span></a><nav aria-label="Sport navigation"><a href="/sports/">The desk</a><a href="/sports/laliga-explained/">La Liga</a><a href="/sports/editorial-policy/">Our standards</a></nav></header><main id="main"><article>{body}</article></main><footer>THE BRYME · Independent football context, not betting advice. <a href="/sports/privacy/">Privacy</a> · <a href="/sports/corrections/">Corrections</a></footer></body></html>'''
    bases=[ROOT/'ecosystem/sports']
    if stage: bases += [ROOT/'sports',ROOT/'public/sports']
    for base in bases:
        dest=base/SLUG/'index.html'; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(page)
        sm=base/'sitemap.xml'; text=sm.read_text()
        if URL not in text:
            text=text.replace('</urlset>',f'<url><loc>{URL}</loc><lastmod>2026-10-09</lastmod></url>\n</urlset>')
            sm.write_text(text)
        hub=base/'index.html'; text=hub.read_text()
        marker='data-clasico-guide="true"'
        card=f'<section class="section" {marker}><div class="prose"><h2>El Clásico: the rivalry file</h2><p><a href="{ROUTE}">Barcelona vs Real Madrid: date, Nigeria viewing guidance, history and title-race scenarios</a>. Research edition checked 9 October 2026; availability and match-day details require updates.</p></div></section>'
        if marker not in text: hub.write_text(text.replace('</main>',card+'</main>',1))
    if stage:
        al=ROOT/'content/index-allowlist.routed.json'; data=json.loads(al.read_text()); data['routes']=sorted(set(data['routes'])|{ROUTE}); al.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    print(f'Clásico guide: built {len(bases)} copies; stable route {ROUTE}')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--stage',action='store_true');build(p.parse_args().stage)
