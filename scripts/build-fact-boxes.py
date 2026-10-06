#!/usr/bin/env python3
"""B1: extractive fact boxes on the top-100 explainer pages (AI-answer surface).

Selection (deterministic): indexable pages under the 7 desks whose H1 reads like an
explainer (how/what/why/...), ranked by word count desc then route asc, top 100.
Policy pages (POLICY_SLUGS, i.e. each desk's /privacy/ page) never compete.

Box is EXTRACTIVE only: the page's own first lede sentence as "The short answer",
its own verified date string, and its own citation count. No new claims.
Idempotent via marker data-esrc="fb"; noindex pages excluded by selection.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
DESKS = ("writers", "tech", "sports", "entertainment", "fitness", "home", "money")
# Policy pages are not explainers, even when the H1 happens to open with a question
# word ("What we collect: almost nothing."). Candidates are ranked by raw word count
# and the whole top-100 is re-selected on every build (build-routing.py strips the old
# boxes), so a privacy page left in the pool lets any edit to its copy silently take a
# slot from a real explainer - which is what happened when the Monetag disclosure grew
# the Fitness privacy page. They never compete for a box.
POLICY_SLUGS = frozenset({"privacy"})
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


def first_lede(t):
    body = t[t.find("<main"):] if "<main" in t else t
    for pm in P_TAG.finditer(body):
        tag = pm.group(0)[:80]
        if re.search(r'class="[^"]*(byline|kicker|crumb|meta|tagline)', tag):
            continue
        s = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", pm.group(1))).strip()
        if len(s.split()) >= 8:
            return s
    return ""

def build_index():
    by_desk = {}
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
            if route.strip("/").rsplit("/", 1)[-1] in POLICY_SLUGS:
                continue
            if not first_lede(t):
                continue
            by_desk.setdefault(desk, []).append((words(t), route))
    # proportional allocation across desks (largest remainder), ranked in-desk
    total_pages = sum(len(v) for v in by_desk.values())
    quota = {d: len(v) * 100 / total_pages for d, v in by_desk.items()}
    alloc = {d: int(q) for d, q in quota.items()}
    for d in sorted(quota, key=lambda d: (-(quota[d] - alloc[d]), d))[:100 - sum(alloc.values())]:
        alloc[d] += 1
    top = set()
    for desk, items in by_desk.items():
        items.sort(key=lambda x: (-x[0], x[1]))
        top.update(route for _w, route in items[: alloc[desk]])
    return top

def apply_one(f, route):
    t = f.read_text(encoding="utf-8")
    if 'data-esrc="fb"' in t or "</main>" not in t:
        return "skip"
    m = H1.search(t)
    if not m:
        return "skip"
    h1 = strip(m.group(1))
    lede_src = first_lede(t)
    if not lede_src:
        return "skip"
    lede = first_sentence(lede_src)
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
