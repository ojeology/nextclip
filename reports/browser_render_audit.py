#!/usr/bin/env python3
"""Small rendered-DOM audit using system Chromium. Read-only against production."""
from __future__ import annotations
import json, re, time
from pathlib import Path
from urllib.parse import urlsplit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ROOT=Path(__file__).resolve().parents[1]
BASE='https://bryme.onrender.com'
OUT=ROOT/'reports'/'browser-render-audit.json'
WORD=re.compile(r"[\w’'\-]+",re.UNICODE)
URLS=[
 '/', '/movie/dune-part-two/', '/movie/thor/', '/series/shogun/', '/series/', '/anime/',
 '/movies/', '/year/1975/', '/channels/netflix/', '/sports/',
 '/sports/premier-league/fixtures/', '/sports/premier-league/table/',
 '/sports/premier-league/teams/arsenal/',
 '/sports/premier-league/reports/aston-villa-vs-arsenal/',
 '/sports/articles/arsenal-title-defence/',
 '/make-money/', '/make-money/microtasks/', '/tech/', '/tech/ai-tools/', '/search/',
 '/article/christopher-nolan-movies-order/', '/privacy/'
]

def wc(s): return len(WORD.findall(s or ''))

def options(width=390,height=844):
    o=Options(); o.binary_location='/usr/bin/chromium'
    for arg in ['--headless=new','--no-sandbox','--disable-dev-shm-usage','--disable-gpu',f'--window-size={width},{height}','--lang=en-GB']:
        o.add_argument(arg)
    o.page_load_strategy='eager'
    o.set_capability('goog:loggingPrefs', {'browser':'ALL'})
    return o

def audit(driver,path,settle=2.0):
    url=BASE+path
    driver.get(url)
    time.sleep(settle)
    data=driver.execute_script(r'''
const main=document.querySelector('main');
const txt=e=>e?(e.innerText||''):'';
const raw=e=>e?(e.textContent||''):'';
const vis=e=>{if(!e)return false;const s=getComputedStyle(e);const r=e.getBoundingClientRect();return !e.hidden&&s.display!=='none'&&s.visibility!=='hidden'&&s.visibility!=='collapse'&&parseFloat(s.opacity||'1')!==0&&r.width>0&&r.height>0};
const hiddenRoots=[];
if(main){for(const e of main.querySelectorAll('*')){const s=getComputedStyle(e);const h=e.hidden||s.display==='none'||s.visibility==='hidden'||s.visibility==='collapse'||parseFloat(s.opacity||'1')===0;if(!h)continue;let p=e.parentElement, parentHidden=false;while(p&&p!==main){const ps=getComputedStyle(p);if(p.hidden||ps.display==='none'||ps.visibility==='hidden'||ps.visibility==='collapse'||parseFloat(ps.opacity||'1')===0){parentHidden=true;break}p=p.parentElement}if(!parentHidden)hiddenRoots.push({tag:e.tagName.toLowerCase(),id:e.id||'',cls:e.className&&typeof e.className==='string'?e.className:'',text:raw(e).replace(/\s+/g,' ').trim().slice(0,1000)})}}
const entries=performance.getEntriesByType('resource').map(e=>({name:e.name,transfer:e.transferSize||0,duration:e.duration||0,initiator:e.initiatorType||''}));
return {
  url:location.href,
  status_title:document.title,
  body_inner:txt(document.body),
  main_inner:txt(main),
  main_raw:raw(main),
  main_html:main?main.innerHTML:'',
  hidden_roots:hiddenRoots,
  header_visible:vis(document.querySelector('header.top')),
  deskbar_visible:vis(document.querySelector('.desk-bar')),
  mobile_nav_visible:vis(document.querySelector('.mobile-nav')),
  h1:[...document.querySelectorAll('h1')].map(e=>({text:txt(e).trim(),visible:vis(e)})),
  links:[...(main||document).querySelectorAll('a[href]')].map(a=>({href:a.href,text:txt(a).replace(/\s+/g,' ').trim(),visible:vis(a)})),
  images:[...(main||document).querySelectorAll('img')].map(i=>({src:i.currentSrc||i.src||'',alt:i.alt||'',visible:vis(i),nw:i.naturalWidth||0,nh:i.naturalHeight||0,w:i.getBoundingClientRect().width,h:i.getBoundingClientRect().height})),
  frames:[...(main||document).querySelectorAll('iframe')].map(i=>({src:i.src||'',visible:vis(i)})),
  scripts:[...document.scripts].map(s=>s.src).filter(Boolean),
  resources:entries,
  ga_loaded:!![...document.scripts].find(s=>(s.src||'').includes('googletagmanager.com/gtag/js')),
  monetag_loaded:!![...document.scripts].find(s=>(s.src||'').includes('n6wxm.com')),
  data_layer_length:Array.isArray(window.dataLayer)?window.dataLayer.length:0
};
''')
    try: logs=driver.get_log('browser')
    except Exception: logs=[]
    hidden=' '.join(x['text'] for x in data.pop('hidden_roots'))
    resources=data.pop('resources')
    links=data.pop('links'); imgs=data.pop('images')
    data['path']=path
    data['body_visible_words']=wc(data.pop('body_inner'))
    data['main_visible_words']=wc(data.pop('main_inner'))
    data['main_dom_words']=wc(data.pop('main_raw'))
    data.pop('main_html',None)
    data['top_hidden_words']=wc(hidden)
    data['main_links']=len(links); data['visible_main_links']=sum(x['visible'] for x in links)
    data['empty_visible_main_links']=sum(x['visible'] and not x['text'] for x in links)
    data['main_images']=len(imgs); data['visible_main_images']=sum(x['visible'] for x in imgs)
    data['broken_visible_images']=sum(x['visible'] and not x['nw'] for x in imgs)
    data['resource_requests']=len(resources)
    data['resource_transfer_bytes']=sum(x['transfer'] for x in resources)
    data['resource_hosts']=dict(__import__('collections').Counter((urlsplit(x['name']).hostname or '') for x in resources))
    data['console_severe']=[x['message'][:1000] for x in logs if x.get('level')=='SEVERE']
    return data

def main():
    driver=webdriver.Chrome(service=Service('/usr/bin/chromedriver'),options=options())
    driver.set_page_load_timeout(25)
    rows=[]
    try:
        for p in URLS:
            try:
                row=audit(driver,p)
                rows.append(row)
                print(p,row['main_visible_words'],row['main_dom_words'],'hidden',row['top_hidden_words'],'GA',row['ga_loaded'],'errors',len(row['console_severe']))
            except Exception as e:
                rows.append({'path':p,'error':repr(e)})
                print('ERROR',p,repr(e))
    finally:
        driver.quit()

    # Desktop visibility check and deliberate 7-second observation of third-party scripts.
    d=webdriver.Chrome(service=Service('/usr/bin/chromedriver'),options=options(1440,1000))
    d.set_page_load_timeout(25)
    desktop=[]
    try:
        for p,settle in [('/',7.0),('/movie/dune-part-two/',2.0)]:
            try: desktop.append(audit(d,p,settle))
            except Exception as e: desktop.append({'path':p,'error':repr(e)})
    finally: d.quit()
    OUT.write_text(json.dumps({'generated_at':'2026-09-04','viewport':'390x844','pages':rows,'desktop_checks':desktop},ensure_ascii=False,indent=2)+'\n')
    print(OUT.relative_to(ROOT))

if __name__=='__main__': main()
