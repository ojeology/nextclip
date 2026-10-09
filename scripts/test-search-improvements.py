#!/usr/bin/env python3
"""Focused regression checks for the five audited pages.
Requires beautifulsoup4; --browser additionally needs Playwright/Chromium and
PREVIEW_URL (default http://127.0.0.1:8001). No third-party ads run in tests.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
PAGES=json.loads((ROOT/'content/search-improvements/pages.json').read_text())
paths=[]
for rec in PAGES:
    path=ROOT/'public'/rec['route'].strip('/')/'index.html';paths.append(path)
    s=BeautifulSoup(path.read_text(),'html.parser');article=s.select_one('article.si-article');assert article
    assert len(s.select('h1'))==1
    assert s.title.get_text()==rec['title']
    assert s.select_one('meta[name=description]')['content']==rec['description']
    assert len(s.select('link[rel=canonical]'))==1
    assert s.select_one('link[rel=canonical]')['href']=='https://thebryme.com'+rec['route']
    assert all('noindex' not in m.get('content','') for m in s.select('meta[name=robots]'))
    ids=[x['id'] for x in s.select('[id]')];assert len(ids)==len(set(ids)),rec['route']
    for a in article.select('a[href]'):
        u=a['href']
        if u.startswith('#'):assert u[1:] in ids,u
        if u.startswith('/'):
            dest=ROOT/'public'/u.strip('/')/'index.html';assert dest.exists(),u
    jsons=[json.loads(x.string) for x in s.select('script[type="application/ld+json"]')]
    articles=[x for x in jsons if x.get('@type')=='Article'];assert len(articles)==1,rec['route']
    assert articles[0]['dateModified']=='2026-10-09'
    assert articles[0]['headline']==s.h1.get_text()
    desk=rec['route'].split('/')[1];tree=ET.parse(ROOT/'public'/desk/'sitemap.xml');ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    nodes=[n for n in tree.findall('s:url',ns) if n.find('s:loc',ns).text=='https://thebryme.com'+rec['route']]
    assert len(nodes)==1;assert nodes[0].find('s:lastmod',ns).text=='2026-10-09'
    headings=[h.get_text() for h in article.select('h2')]
    if rec['fragment']=='alice.html':assert len([h for h in headings if re.match(r'^\d+\.',h)])==10
    if rec['fragment']=='deadpool.html':assert len([h for h in headings if re.match(r'^\d+\.',h)])==12
    if rec['fragment']=='the-drift.html':assert 'anything written by AI' in article.get_text()
    if rec['fragment']=='noema.html':assert 'not blanket permission' in article.get_text()
    assert len(s.select('main aside[data-adband]'))==1
    print('PASS static:',rec['route'])
before=[hashlib.sha256(p.read_bytes()).hexdigest() for p in paths]
subprocess.run([sys.executable,str(ROOT/'scripts/build-search-improvements.py')],check=True)
assert before==[hashlib.sha256(p.read_bytes()).hexdigest() for p in paths]
print('PASS: idempotent renderer; metadata, sources, section counts, links, schemas and sitemap checks')
if '--browser' in sys.argv:
    from playwright.sync_api import sync_playwright
    origin=os.environ.get('PREVIEW_URL','http://127.0.0.1:8001')
    with sync_playwright() as pw:
        browser=pw.chromium.launch()
        for rec in PAGES:
            for width in [360,768,1440]:
                page=browser.new_page(viewport={'width':width,'height':900})
                page.route('**/*',lambda r:r.continue_() if urlsplit(r.request.url).netloc==urlsplit(origin).netloc else r.abort())
                response=page.goto(origin+rec['route'],wait_until='domcontentloaded');assert response.status==200
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),(rec['route'],width)
                first=page.locator('.si-article a[href^="#"]').first
                if first.count():
                    target=first.get_attribute('href');first.click();assert page.evaluate('location.hash')==target
                print('PASS browser:',width,rec['route'])
                if width==360:
                    page.evaluate('scrollTo(0,0)');page.screenshot(path=str(ROOT/'reports/search-sprint-oct9'/rec['fragment'].replace('.html','-mobile.png')))
                page.close()
        browser.close()
