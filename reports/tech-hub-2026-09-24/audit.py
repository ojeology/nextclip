#!/usr/bin/env python3
"""Tech-desk audit: URL inventory + content-quality census (read-only)."""
import json, re, sys, collections
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path("/home/user/nextclip")
TECH = ROOT / "tech"

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hrefs=[]; self.scripts=[]; self.inline_script=False; self.text=[]
        self.instyle=0; self.inhead=0; self.instyleflag=False
        self.imgs=0; self.alts=0; self.h2=0; self.tables=0; self.links_internal=0
        self.schemas=[]; self.robots=""; self.canonical=""; self.title=""; self.desc=""
        self._cap=False; self.jsonld=[]; self._injson=False; self._buf=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="a" and a.get("href","").startswith("/tech/"): self.links_internal+=1
        if tag=="link" and a.get("rel")=="canonical": self.canonical=a.get("href","")
        if tag=="meta" and a.get("name")=="robots": self.robots=a.get("content","")
        if tag=="meta" and a.get("name")=="description": self.desc=a.get("content","")
        if tag=="img": self.imgs+=1; self.alts+= 1 if a.get("alt") not in (None,"") else 0
        if tag=="script":
            if a.get("type")=="application/ld+json": self._injson=True; self._buf=[]
            elif a.get("src"): self.scripts.append(a["src"])
            else: self.inline_script=True
            self.instyleflag=False
        if tag=="style": self.instyle+=1
        if tag=="title": self._cap=True
    def handle_endtag(self,tag):
        if tag=="title": self._cap=False
        if tag=="script":
            if self._injson:
                try: self.schemas.append(json.loads("".join(self._buf)))
                except Exception: self.schemas.append({"_unparsed":True})
                self._injson=False
    def handle_data(self,d):
        if self._cap: self.title+=d
        if self._injson: self._buf.append(d)
        self.text.append(d)

rows=[]
for d in sorted(p for p in TECH.iterdir() if p.is_dir()):
    f=d/"index.html"
    if not f.is_file():
        rows.append(dict(slug=d.name,file=False)); continue
    raw=f.read_text(encoding="utf-8",errors="replace")
    pr=P(); pr.feed(raw)
    # body text only: strip head, tags
    body=re.sub(r"<head.*?</head>","",raw,flags=re.S|re.I)
    for pat in (r"<script.*?</script>",r"<style.*?</style>"):
        body=re.sub(pat,"",body,flags=re.S|re.I)
    txt=re.sub(r"<[^>]+>"," ",body)
    txt=re.sub(r"\s+"," ",txt).strip()
    words=len(txt.split())
    rows.append(dict(slug=d.name,file=True,words=words,
        h2=len(re.findall(r"<h2",body)),tables=len(re.findall(r"<table",body)),
        code=len(re.findall(r"<pre",body)),
        links=pr.links_internal, imgs=pr.imgs, alts=pr.alts,
        inline_script=pr.inline_script, scripts=sorted(set(pr.scripts)),
        robots=pr.robots.strip(), canonical=pr.canonical,
        schemas=sorted({s.get("@type","?") for s in pr.schemas if isinstance(s,dict)}),
        title=pr.title.strip()[:90], desc_len=len(pr.desc), bytes=len(raw)))

hub=TECH/"index.html"
hp=P(); hp.feed(hub.read_text(encoding="utf-8"))
out=dict(
  total_dirs=len([p for p in TECH.iterdir() if p.is_dir()]),
  pages=len(rows), missing=[r["slug"] for r in rows if not r["file"]],
  words=[r["words"] for r in rows if r["file"]],
  thin=sorted([(r["words"],r["slug"]) for r in rows if r["file"]])[:18],
  thick=sorted([(r["words"],r["slug"]) for r in rows if r["file"]],reverse=True)[:10],
  no_robots=[r["slug"] for r in rows if r["file"] and not r["robots"]],
  nonindex=[r["slug"] for r in rows if r["file"] and "noindex" in r["robots"].lower()],
  inline=[r["slug"] for r in rows if r["file"] and r["inline_script"]],
  schemas=collections.Counter(s for r in rows if r["file"] for s in r["schemas"]),
  scripts=collections.Counter(s for r in rows if r["file"] for s in r["scripts"]),
  hub_bytes=hub.stat().st_size,
)
w=out["words"]
w_sorted=sorted(w)
out["word_stats"]=dict(n=len(w), min=w_sorted[0], p25=w_sorted[len(w)//4], median=w_sorted[len(w)//2], p75=w_sorted[(3*len(w))//4], max=w_sorted[-1],
                      mean=round(sum(w)/len(w),1), under400=sum(1 for x in w if x<400), under800=sum(1 for x in w if x<800), over1200=sum(1 for x in w if x>=1200))
out["no_alt"]=sum(1 for r in rows if r["file"] and r["imgs"]>r["alts"])
out["zero_internal_links"]=[r["slug"] for r in rows if r["file"] and r["links"]==0]
json.dump(out,open("/home/user/nextclip/reports/tech-hub-2026-09-24/audit.json","w"),indent=1)
# URL inventory: every href/src referencing /tech/ across all tech pages
urls=set(); ext=set()
for f in list(TECH.rglob("index.html")):
    raw=f.read_text(encoding="utf-8",errors="replace")
    for m in re.finditer(r'href="(/tech/[^"#?]*)"',raw): urls.add(m.group(1))
    for m in re.finditer(r'href="(https?://[^"]+)"',raw): ext.add(m.group(1))
inv=sorted(urls)
open("/home/user/nextclip/reports/tech-hub-2026-09-24/url-inventory.txt","w").write("\n".join(inv)+"\n")
print("tech dirs:",out["total_dirs"],"pages:",out["pages"])
print("word stats:",out["word_stats"])
print("schemas:",dict(out["schemas"]))
print("scripts:",dict(list(out["scripts"].items())[:8]))
print("inline script pages:",len(out["inline"]))
print("nonindex:",out["nonindex"][:12],"count",len(out["nonindex"]))
print("no robots meta:",len(out["no_robots"]))
print("URL inventory refs:",len(inv),"external links:",len(ext))
print("thin (18):",out["thin"])
print("zero-link pages:",len(out["zero_internal_links"]))
print("hub bytes:",out["hub_bytes"])
