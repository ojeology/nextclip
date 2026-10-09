#!/usr/bin/env python3
"""Focused static + optional browser tests; python3 scripts/test-el-clasico.py --browser.
Browser test requires Python playwright and installed Chromium, preview on port 8000.
"""
import hashlib
import json
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
SLUG='el-clasico-barcelona-real-madrid'; ROUTE='/sports/'+SLUG+'/'
class Parser(HTMLParser):
    def __init__(self): super().__init__(); self.tags=[]
    def handle_starttag(self,tag,attrs): self.tags.append((tag,dict(attrs)))
p=ROOT/'public'/ROUTE.strip('/')/'index.html'
text=p.read_text(); parser=Parser();parser.feed(text)
assert sum(t=='h1' for t,a in parser.tags)==1
assert [a['href'] for t,a in parser.tags if t=='link' and a.get('rel')=='canonical']==['https://thebryme.com'+ROUTE]
assert any(t=='meta' and a.get('name')=='robots' and a.get('content')=='index,follow' for t,a in parser.tags)
ids=[a['id'] for t,a in parser.tags if 'id' in a];assert len(ids)==len(set(ids))
for tag,a in parser.tags:
    if tag!='a':continue
    link=a.get('href','')
    if link.startswith('#'):assert link[1:] in ids,link
    elif link.startswith('/'):
        dest=ROOT/'public'/link.strip('/')
        assert dest.is_file() or (dest/'index.html').is_file(),link
for base in [ROOT/'ecosystem/sports',ROOT/'sports',ROOT/'public/sports']:
    assert (base/SLUG/'index.html').read_text()==text
    tree=ET.parse(base/'sitemap.xml')
    locs=[n.text for n in tree.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert locs.count('https://thebryme.com'+ROUTE)==1
    assert (base/'index.html').read_text().count('data-clasico-guide="true"')==1
assert ROUTE in json.loads((ROOT/'content/index-allowlist.routed.json').read_text())['routes']
files=[ROOT/'content/index-allowlist.routed.json']+[base/name for base in [ROOT/'ecosystem/sports',ROOT/'sports',ROOT/'public/sports'] for name in ['index.html','sitemap.xml',SLUG+'/index.html']]
def hashes():return [hashlib.sha256(f.read_bytes()).hexdigest() for f in files]
before=hashes();subprocess.run([sys.executable,str(ROOT/'scripts/build-el-clasico.py'),'--stage'],check=True);assert hashes()==before
print('PASS: one H1, canonical, robots, unique anchors, all internal links, three copies, sitemap, incoming links, allowlist, idempotence')
if '--browser' in sys.argv:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        browser=pw.chromium.launch()
        for width in [360,390,768,1440]:
            page=browser.new_page(viewport={'width':width,'height':900});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
            response=page.goto('http://127.0.0.1:8000'+ROUTE);assert response.status==200
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),width
            assert not errors,errors
            schema=json.loads(page.locator('script[type="application/ld+json"]').inner_text());assert schema['@type']=='Article'
            page.locator('.contents a[href="#records"]').click();assert page.evaluate('location.hash')=='#records'
            if width==390:
                page.evaluate('scrollTo(0,0)');page.screenshot(path=str(ROOT/'reports/el-clasico/mobile.png'),full_page=False)
            print(f'PASS browser: {width}px, HTTP 200, no document overflow, no JS exceptions, JSON-LD, contents navigation')
            page.close()
        browser.close()
print('HTML bytes:',len(p.read_bytes()))
