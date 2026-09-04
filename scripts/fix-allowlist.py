import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
al=json.load(open(ROOT/"content/index-allowlist.json"))
routes=al["routes"] if isinstance(al,dict) and "routes" in al else al
data=json.load(open(ROOT/"content/jobs.json"))
jobs=data["jobs"] if isinstance(data,dict) and "jobs" in data else data
need=[f"/jobs/{j['id']}/" for j in jobs]
add=[r for r in need if r not in routes]
routes=sorted(set(routes)|set(need))
if isinstance(al,dict) and "routes" in al:
    al["routes"]=routes
    out=al
else:
    out=routes
json.dump(out,open(ROOT/"content/index-allowlist.json","w"),ensure_ascii=False,indent=2)
print("added",len(add),"-- allowlist now",len(routes))
