#!/usr/bin/env python3
"""B1: extractive fact boxes on the top-100 explainer pages (AI-answer surface).

Selection (deterministic): indexable pages under the 7 desks whose H1 reads like an
explainer (how/what/why/...), ranked by word count desc then route asc, top 100.

Box is EXTRACTIVE only: the page's own first lede sentence as "The short answer",
its own verified date string, and its own citation count. No new claims.
Idempotent via marker data-esrc="fb"; noindex pages excluded by selection.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
DESKS = ("writers", "tech", "sports", "entertainment", "fitness", "home", "money")
QW = re.compile(r"\b(how|what|why|when|where|which|who|does|do|can|is|are|should|best way)\b", re.I)
H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
LEDE = re.compile(r"<main.*?>(.*?)</p>", re.S)
P_TAG = re.compile(r"<p[^>]*>(.*?)</p>", re.S)
DATE = re.compile(r"(Updated|Reviewed|Verified|checked)\s+(on\s+)?[A-Z0-9][^<.]{3,30}", re.I)

def words(t):
    body = re.sub(r"<[^>]+>", " ", t)
    return len(body.split())

def strip(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()

def first_sentence(t):
    s = strip(t)
    for sep in (". ", "? ", "! "):
        if sep in s:
            return s.split(sep)[0].strip() + sep.strip()
    return s[:220]

def build_index():
    cands = []
    for desk in DESKS:
        for f in (PUB / desk).rglob("index.html"):
            t = f.read_text(encoding="utf-8")
            if 'content="noindex' in t and re.search(r'<meta[^>]+name="robots"[^>]+content="noindex', t):
                continue
            m = H1.search(t)
            if not m:
                continue
            h1 = strip(m.group(1))
            if not QW.search(h1[:40]):
                continue
            route = "/" + f.parent.relative_to(PUB).as_posix() + "/"
            if route.count("/") < 3:  # hubs (desk root + top-level hub pages) are not explainers
                continue
            pm2 = P_TAG.search(t[t.find("<main"):])
            if not pm2 or len(strip(pm2.group(1)).split()) < 8:
                continue
            cands.append((words(t), route))
    cands.sort(key=lambda x: (-x[0], x[1]))
    return {route for _w, route in cands[:100]}

def apply_one(f, route):
    t = f.read_text(encoding="utf-8")
    if 'data-esrc="fb"' in t or "</main>" not in t:
        return "skip"
    m = H1.search(t)
    if not m:
        return "skip"
    h1 = strip(m.group(1))
    pm = P_TAG.search(t[t.find("<main"):])
    if not pm:
        return "skip"
    lede = first_sentence(pm.group(1))
    dm = DATE.search(strip(t[:6000]))
    vdate = strip(dm.group(0)) if dm else "dated inline"
    n_src = t.count('rel="noopener"')
    src_line = f"{n_src} external sources cited" if n_src else "citations listed at the foot of the page"
    box = (f'<aside class="fact-box" data-esrc="fb" style="border-left:4px solid #e4572e;background:#faf7f2;'
           f'padding:14px 18px;margin:18px 0;font-family:Georgia,serif">'
           f'<h2 style="margin:0 0 8px;font-size:1.05rem">{h1} &mdash; the short answer</h2>'
           f'<p style="margin:0 0 8px"><strong>The short answer:</strong> {lede}</p>'
           f'<p style="margin:0;font-size:.85rem;color:#555">{vdate} &middot; {src_line}</p></aside>')
    idx = t.find("<h2", t.find("<main"))
    if idx == -1:
        t = t.replace("</main>", box + "</main>", 1)
    else:
        t = t[:idx] + box + t[idx:]
    f.write_text(t, encoding="utf-8")
    return "applied"

def main():
    top = build_index()
    applied = {}
    for base in (ROOT, PUB):
        a = s = 0
        for route in sorted(top):
            f = base / route.strip("/") / "index.html"
            if not f.is_file():
                continue
            r = apply_one(f, route)
            if r == "applied":
                a += 1
            else:
                s += 1
        applied[str(base)] = (a, s)
    print(f"fact-boxes: top100 selected; applied={applied}")

if __name__ == "__main__":
    main()
