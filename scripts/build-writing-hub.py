#!/usr/bin/env python3
"""Build the BRYME Writing Hub — the expanded writing-education surface.

Content-driven (add a guide file in content/hub/guides, add a tool entry, and
rebuild — no generator change needed). Reuses the shared shell (page, esc,
schema, write, BASE) from the writing-first builder so the head/canonical/OG
handling and the hub navigation stay consistent.

Emits:
  /                       Hub homepage (overrides the writing-first home)
  /learn/                 all 20 sections grouped
  /learn/<section>/       one hub page per section (noindex while empty)
  /learn/<section>/<guide>/  one page per guide (canonical)
  /tools/ + /tools/<id>/  the in-browser tools
  /glossary/              searchable glossary
  /templates/             template library
  /checklists/            interactive checklists
  /problems/              common writing problems
  /search/                client-side site search
"""
from __future__ import annotations
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# Reuse the writing-first builder's shell (page_wf, esc, write, BASE, TODAY) so
# head/canonical/OG/schema + the (updated) hub navigation stay consistent.
_spec = importlib.util.spec_from_file_location(
    "build_writing_first", str(ROOT / "scripts" / "build-writing-first.py"))
_bwf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bwf)

esc = _bwf.esc
write = _bwf.write
BASE = _bwf.BASE
TODAY = _bwf.TODAY
page_wf = _bwf.page_wf
WRITING = _bwf.WRITING


def load(name: str):
    return json.loads((ROOT / "content" / "hub" / name).read_text(encoding="utf-8"))


SECTIONS = load("sections.json")
GROUPS = {g["id"]: g for g in SECTIONS["groups"]}
SECTIONS_BY_ID = {s["id"]: s for s in SECTIONS["sections"]}
TOOLS = load("tools.json")["tools"]
TOOLS_BY_ID = {t["id"]: t for t in TOOLS}
GLOSSARY = load("glossary.json")["terms"]
TEMPLATES = load("templates.json")["templates"]
CHECKLISTS = load("checklists.json")["checklists"]
PROBLEMS = load("problems.json")["problems"]

# --------------------------------------------------------------------------
# Markdown subset renderer for guide bodies
# --------------------------------------------------------------------------
def render_md(text: str) -> str:
    blocks = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        # heading
        if stripped.startswith("### "):
            blocks.append(f"<h3>{inline(stripped[4:])}</h3>")
            i += 1
            continue
        if stripped.startswith("## "):
            blocks.append(f"<h2>{inline(stripped[3:])}</h2>")
            i += 1
            continue
        if stripped.startswith("# "):
            blocks.append(f"<h2>{inline(stripped[2:])}</h2>")
            i += 1
            continue
        if stripped.startswith("---"):
            i += 1
            continue
        # blockquote
        if stripped.startswith("> "):
            q = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                q.append(lines[i].strip()[2:])
                i += 1
            blocks.append(f"<blockquote>{inline(' '.join(q))}</blockquote>")
            continue
        # task / bullet / number lists
        if stripped.startswith("- [ ] ") or stripped.startswith("- [x] "):
            items = []
            while i < len(lines) and (lines[i].strip().startswith("- [ ]") or lines[i].strip().startswith("- [x]")):
                s = lines[i].strip()
                checked = s.startswith("- [x]")
                body = s[6:].strip()
                items.append(f'<li><label class="tl"><input type="checkbox"{" checked" if checked else ""}> {inline(body)}</label></li>')
                i += 1
            blocks.append('<ul class="task-list">' + "".join(items) + "</ul>")
            continue
        if stripped.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(f"<li>{inline(lines[i].strip()[2:])}</li>")
                i += 1
            blocks.append("<ul>" + "".join(items) + "</ul>")
            continue
        m = re.match(r"^\d+\.\s+(.*)$", stripped)
        if m:
            items = []
            while i < len(lines):
                mm = re.match(r"^\d+\.\s+(.*)$", lines[i].strip())
                if not mm:
                    break
                items.append(f"<li>{inline(mm.group(1))}</li>")
                i += 1
            blocks.append("<ol>" + "".join(items) + "</ol>")
            continue
        # paragraph: gather until blank line
        para = []
        while i < len(lines):
            s = lines[i].strip()
            if not s or s.startswith(("## ", "# ", "### ", "- ", "> ", "---")):
                break
            if re.match(r"^\d+\.\s", s):
                break
            para.append(s)
            i += 1
        if para:
            blocks.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(blocks)


def inline(t: str) -> str:
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    data = {}
    for line in fm.split("\n"):
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip().strip("\"'")
        if v.startswith("[") and v.endswith("]"):
            if v == "[]":
                data[k] = []
            else:
                data[k] = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
        else:
            data[k] = v
    return data, body


# --------------------------------------------------------------------------
# Page helpers
# --------------------------------------------------------------------------
def load_guides() -> list[dict]:
    guides = []
    for p in sorted((ROOT / "content" / "hub" / "guides").glob("*.md")):
        fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        fm["slug"] = p.stem
        fm["body"] = body
        fm["section"] = fm.get("section", "")
        guides.append(fm)
    return guides


GUIDES = load_guides()
GUIDES_BY_SLUG = {g["slug"]: g for g in GUIDES}
GUIDES_BY_SECTION: dict[str, list[dict]] = {}
for g in GUIDES:
    GUIDES_BY_SECTION.setdefault(g["section"], []).append(g)
for sec in GUIDES_BY_SECTION:
    GUIDES_BY_SECTION[sec].sort(key=lambda g: g.get("updated", ""), reverse=True)


def breadcrumb(*parts: list[str]) -> str:
    links = ['<a href="/">Home</a>']
    for label, href in parts:
        links.append(f'<a href="{esc(href)}">{esc(label)}</a>')
    return '<nav class="breadcrumb">' + " / ".join(links) + "</nav>"


def tool_links(items: list[str]) -> str:
    if not items:
        return ""
    cards = "".join(
        f'<a class="chip-card" href="/tools/{esc(t)}/"><b>🛠</b><span>{esc(TOOLS_BY_ID[t]["title"])}</span></a>'
        for t in items if t in TOOLS_BY_ID)
    return f'<div class="wrap"><section class="section"><div class="section-head"><div><p class="eyebrow">Tools that can help</p><h2>Try a free BRYME tool</h2></div><p>No account needed — these run right in your browser.</p></div><div class="guide-grid">{cards}</div></section></div>' if cards else ""


def related_links(items: list[str]) -> str:
    if not items:
        return ""
    cards = "".join(
        f'<a class="path-card" href="/learn/{esc(g["section"])}/{esc(g["slug"])}/"><span class="card-num">GUIDE</span><h3>{esc(g["title"])}</h3><p>{esc(g.get("description", ""))}</p><span class="card-link">Open the guide →</span></a>'
        for g in (GUIDES_BY_SLUG.get(s) for s in items) if g)
    return f'<div class="wrap"><section class="section alt"><div class="section-head"><div><p class="eyebrow">Related guides</p><h2>Go deeper</h2></div></div><div class="guide-grid">{cards}</div></section></div>' if cards else ""


def guide_page(g: dict) -> None:
    section = SECTIONS_BY_ID.get(g["section"])
    tool_items = g.get("tools", [])
    # Where the guide's tools live inline in prose, we render a section at the end.
    prose = render_md(g["body"])
    body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"), (section["title"], f"/learn/{section['id']}/"), (g["title"], ""))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(section['title'])}</p>
<h1>{esc(g['title'])}</h1>
<p>{esc(g.get('description', ''))}</p>
<p class="byline">Researched and written by <a href="/author/ibrahim-sodiq/">BRYME Editorial Desk</a>.</p>
<a class="btn secondary" href="/learn/{esc(section['id'])}/">← All {esc(section['title'])} guides</a></section>
<section class="section"><div class="prose">{prose}</div></section></div>
{tool_links(tool_items)}{related_links(g.get('related', []))}'''
    write(f"/learn/{g['section']}/{g['slug']}/", page_wf(
        title=f"{g['title']} | BRYME writing guides",
        description=g.get("description", ""),
        route=f"/learn/{g['section']}/{g['slug']}/",
        current="learn", body=body,
        schema_data={"@context": "https://schema.org", "@type": "Article",
                     "headline": g["title"], "description": g.get("description", ""),
                     "url": f"{BASE}/learn/{g['section']}/{g['slug']}/",
                     "datePublished": TODAY + "T00:00:00+01:00", "dateModified": (g.get("updated") or TODAY).replace("-", "-") + "T00:00:00+01:00",
                     "author": {"@type": "Person", "name": "BRYME Editorial Desk", "url": BASE + "/author/ibrahim-sodiq/"},
                     "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
                     "mainEntityOfPage": f"{BASE}/learn/{g['section']}/{g['slug']}/"}))


def section_hub(sec: dict) -> None:
    guides = GUIDES_BY_SECTION.get(sec["id"], [])
    # The four "utility" sections (tools, templates, checklists, glossary) are
    # served by their own dedicated hub pages rather than guides. Render them as
    # an indexable landing that links to the hub.
    utility = {
        "writing-tools": ("/tools/", len(TOOLS), "free tools", "Open the tool library"),
        "writing-templates": ("/templates/", len(TEMPLATES), "templates", "Open the template library"),
        "writing-checklists": ("/checklists/", len(CHECKLISTS), "checklists", "Open the checklists"),
        "writing-glossary": ("/glossary/", len(GLOSSARY), "terms", "Open the glossary"),
    }
    if sec["id"] in utility:
        href, n, noun, label = utility[sec["id"]]
        cards = f'<a class="path-card" href="{href}"><span class="card-num">OPEN</span><h3>{esc(sec["title"])}</h3><p>{esc(sec.get("tagline", sec.get("description", "")))}</p><span class="card-link">{label} →</span></a>'
        content = f'<section class="section"><div class="guide-grid">{cards}</div></section>'
        # also show a few representative items
        extra = ""
        if sec["id"] == "writing-tools":
            extra = '<section class="section alt"><div class="section-head"><div><p class="eyebrow">Popular</p><h2>Start with these tools.</h2></div></div><div class="guide-grid">' + "".join(f'<a class="chip-card" href="/tools/{esc(t["id"])}/"><b>🛠</b><span>{esc(t["title"])}</span></a>' for t in TOOLS[:8]) + '</div></section>'
        elif sec["id"] == "writing-templates":
            extra = '<section class="section alt"><div class="section-head"><div><p class="eyebrow">Popular</p><h2>Most-used templates.</h2></div></div><div class="guide-grid">' + "".join(f'<a class="guide-card" href="/templates/#{esc(t["id"])}"><span class="card-num">{esc(t["title"][:8].upper())}</span><h3>{esc(t["title"])}</h3><p>{esc(t["use"])}</p><span class="card-link">View →</span></a>' for t in TEMPLATES[:6]) + '</div></section>'
        body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(sec['icon'])} Writing Hub</p>
<h1>{esc(sec['title'])}.</h1>
<p>{esc(sec.get('tagline', sec.get('description', '')))}</p>
<div class="source-line"><span><b>{n}</b> {noun}</span></div></section>
{content}{extra}</div>'''
        write(f"/learn/{sec['id']}/", page_wf(
            title=f"{sec['title']} | BRYME", description=sec.get("description", "").replace("\n", " "),
            route=f"/learn/{sec['id']}/", current="learn", body=body, robots="index,follow"))
        return
    if guides:
        cards = "".join(f'<a class="guide-card" href="/learn/{esc(sec["id"])}/{esc(g["slug"])}/"><span class="card-num">GUIDE</span><h2>{esc(g["title"])}</h2><p>{esc(g.get("description", ""))}</p><span class="card-link">Open the guide →</span></a>' for g in guides)
        content = f'<section class="section"><div class="guide-grid">{cards}</div></section>'
        robots = "index,follow"
    else:
        content = '<section class="section"><div class="prose"><p>This section is being written. Check back soon — BRYME adds new guides steadily. In the meantime, browse the <a href="/learn/">full library</a> or the <a href="/writing/">paid writing opportunities</a>.</p></div></section>'
        robots = "noindex,follow"
    body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(sec['icon'])} Writing Hub</p>
<h1>{esc(sec['title'])}.</h1>
<p>{esc(sec.get('tagline', sec.get('description', '')))}</p>
<div class="source-line"><span><b>{len(guides)}</b> guides published</span><span><b>{len(WRITING)}</b> paid opportunities</span></div></section>
{content}</div>'''
    write(f"/learn/{sec['id']}/", page_wf(
        title=f"{sec['title']} | BRYME writing guides",
        description=sec.get("description", ""),
        route=f"/learn/{sec['id']}/", current="learn", body=body, robots=robots))


def tools_index() -> None:
    cats = {"count": "Count and measure", "analyze": "Analyse your writing", "format": "Format and clean text", "work": "Work and plan"}
    grid = []
    for t in TOOLS:
        grid.append(f'<a class="path-card" href="/tools/{esc(t["id"])}/"><span class="card-num">TOOL</span><h3>{esc(t["title"])}</h3><p>{esc(t["short"])}</p><span class="card-link">Use the tool →</span></a>')
    body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Free, in-browser</p>
<h1>Writing tools.</h1>
<p>{len(TOOLS)} free utilities that run right in your browser. No account, no download — type and get instant answers for counting, checking, formatting and planning your writing.</p></section>
<section class="section"><div class="guide-grid">{''.join(grid)}</div></section></div>'''
    write("/tools/", page_wf(title="Writing tools — free word counter, character counter and more | BRYME",
                            description=f"{len(TOOLS)} free in-browser writing tools: word counter, character counter, reading time, readability score, case converter, text cleaner, outline generator and more. No account needed.",
                            route="/tools/", current="tools", body=body,
                            schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME writing tools", "url": BASE + "/tools/"}))


def tool_page(t: dict) -> None:
    body = f'''<div class="wrap">{breadcrumb(("Writing tools", "/tools/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Free tool</p>
<h1>{esc(t['title'])}.</h1>
<p>{esc(t['description'])}</p>
<a class="btn secondary" href="/tools/">← All tools</a></section>
<section class="section">{render_tool(t)}</section></div>'''
    write(f"/tools/{t['id']}/", page_wf(
        title=f"{t['title']} — free writing tool | BRYME",
        description=f"Free {t['title'].lower()} from BRYME. Works in your browser, no account or download needed.",
        route=f"/tools/{t['id']}/", current="tools", body=body,
        schema_data={"@context": "https://schema.org", "@type": "WebApplication", "name": t["title"], "applicationCategory": "Utility", "url": f"{BASE}/tools/{t['id']}/", "operatingSystem": "Any", "description": t["description"], "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


def render_tool(t: dict) -> str:
    i = t["id"]
    if i in ("writing-timer",):
        return f'''<div class="tool-box"><div class="tool-prose"><p>Set a goal and write for a focused stretch. BRYME's timer keeps you honest without nagging you.</p>
<div class="tool-grid"><div class="tool-input"><label for="goal">Goal (minutes)</label><input id="goal" type="number" value="25" min="1"></div><div class="tool-input"><button id="setgoal" class="btn">Set goal</button></div></div>
<div class="timer-display" id="time" aria-live="polite">25:00</div>
<div class="tool-actions"><button id="start" class="btn">Start</button><button id="reset" class="btn secondary">Reset</button></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="writing-timer"></script>'''
    if i in ("case-converter", "text-sorter"):
        extra = '<div class="tool-grid"><div class="tool-input"><label>Input</label><textarea id="ta" placeholder="Type or paste your text…"></textarea></div><div class="tool-input"><label>Output</label><textarea id="out" readonly placeholder="Result appears here…"></textarea></div></div>'
        ctl = '<div class="tool-grid"><div class="tool-input"><label for="mode">Mode</label>' + ('<select id="mode"><option value="title">Title Case</option><option value="lower">lowercase</option><option value="upper">UPPERCASE</option><option value="sentence">Sentence case</option><option value="camel">camelCase</option></select>' if i == "case-converter" else '<select id="dir"><option value="asc">A–Z</option><option value="desc">Z–A</option></select>') + '</div></div>' if i == "case-converter" else ''
        if i == "text-sorter":
            ctl = '<div class="tool-grid"><div class="tool-input"><label for="dir">Direction</label><select id="dir"><option value="asc">A–Z</option><option value="desc">Z–A</option></select></div></div>'
        return f'''<div class="tool-box"><div class="tool-prose"><p>Type or paste your text below — the result updates as you go.</p>{ctl}{extra}</div></div>
<script src="/assets/hub-tools.js" data-hub-tool="{i}"></script>'''
    if i in ("text-cleaner", "remove-extra-spaces", "line-break-cleaner", "duplicate-line-remover"):
        return f'''<div class="tool-box"><div class="tool-prose"><p>Paste messy text and get clean text back.</p>
<div class="tool-grid"><div class="tool-input"><label>Input</label><textarea id="ta" placeholder="Paste your text…"></textarea></div><div class="tool-input"><label>Output</label><textarea id="out" readonly placeholder="Cleaned text…"></textarea></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="{i}"></script>'''
    if i == "word-density":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Paste your text to see the words you use most.</p><label>Your text</label><textarea id="ta" placeholder="Type or paste…"></textarea><div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="word-density"></script>'''
    if i == "article-outline-generator":
        return f'''<div class="tool-box"><div class="tool-prose"><label>Working title</label><input id="t" type="text" placeholder="e.g. How to write a strong introduction"><label>Your key points (one per line)</label><textarea id="p" placeholder="The hook&#10;Who it's for&#10;The proof"></textarea><button class="btn" id="go">Generate outline</button><div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="article-outline-generator"></script>'''
    if i == "writing-checklist-generator":
        return f'''<div class="tool-box"><div class="tool-prose"><label>Checklist items (one per line)</label><textarea id="ta" placeholder="I checked the facts&#10;I proofread once&#10;I added a clear next step"></textarea><div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="writing-checklist-generator"></script>'''
    # default: single textarea with live count
    return f'''<div class="tool-box"><div class="tool-prose"><label>Your text</label><textarea id="ta" placeholder="Type or paste your text…"></textarea><div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="{i}"></script>'''


def glossary_page() -> None:
    items = "".join(f'<dt>{esc(x["term"])}</dt><dd>{esc(x["definition"])}</dd>' for x in GLOSSARY)
    body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Reference</p>
<h1>Writing glossary.</h1>
<p>{len(GLOSSARY)} writing terms explained in plain language, with examples. Use the search box to find a term.</p>
<div class="searchbar"><input id="gsearch" type="search" placeholder="Search the glossary… (e.g. pitch, thesis, tone)" aria-label="Search the glossary"></div></section>
<section class="section"><dl class="glossary" id="glossary">{items}</dl></section></div>
<script src="/assets/hub-tools.js" data-hub-glossary></script>'''
    write("/glossary/", page_wf(title="Writing glossary — every writing term explained | BRYME",
                                description="A plain-language glossary of writing terms: pitch, thesis, tone, voice, draft, paraphrase and more, with simple examples.",
                                route="/glossary/", current="learn", body=body,
                                schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME writing glossary", "url": BASE + "/glossary/"}))


def templates_page() -> None:
    cards = "".join(
        f'<article class="card-block"><h3>{esc(t["title"])}</h3><p class="muted">{esc(t["use"])}</p><ol>{"".join("<li>" + esc(s) + "</li>" for s in t["structure"])}</ol></article>'
        for t in TEMPLATES)
    body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Blueprints</p>
<h1>Writing templates.</h1>
<p>{len(TEMPLATES)} reusable structures for the most common kinds of writing. Use them to see how a piece is built — then make the structure your own.</p></section>
<section class="section"><div class="template-grid">{cards}</div></section></div>'''
    write("/templates/", page_wf(title="Writing templates — structures for every kind of writing | BRYME",
                                 description="Reusable writing templates for articles, essays, emails, cover letters, reports, stories and more — each teaches the structure, not just copy.",
                                 route="/templates/", current="learn", body=body))


def checklists_page() -> None:
    def card(c: dict) -> str:
        items = "".join('<li><label class="tl"><input type="checkbox"> ' + esc(x) + '</label></li>' for x in c["items"])
        return ('<details class="card-block checklist-block"><summary><h3>' + esc(c["title"]) +
                '</h3><p class="muted">Tap to open</p></summary><ul class="task-list">' + items + '</ul></details>')
    cards = "".join(card(c) for c in CHECKLISTS)
    body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Before you finish</p>
<h1>Writing checklists.</h1>
<p>{len(CHECKLISTS)} checklists to run through at each stage — research, drafting, editing, proofreading, and submission. Open one and tick it off as you go.</p></section>
<section class="section"><div class="template-grid">{cards}</div></section></div>'''
    write("/checklists/", page_wf(title="Writing checklists — research, editing, proofreading and submission | BRYME",
                                  description="Practical writing checklists to run before, during and after you write: research, article, essay, email, editing, proofreading, submission and publication.",
                                  route="/checklists/", current="learn", body=body))


def problems_page() -> None:
    cards = "".join(f'<article class="card-block"><h3>{esc(p["q"])}</h3><p>{esc(p["fix"])}</p></article>' for p in PROBLEMS)
    body = f'''<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Troubleshooting</p>
<h1>Common writing problems.</h1>
<p>The problems writers actually face — and the practical fix for each one.</p></section>
<section class="section"><div class="template-grid">{cards}</div></section></div>'''
    write("/problems/", page_wf(title="Common writing problems and how to fix them | BRYME",
                                description="Fix the writing problems that trip up most writers: can't start, weak intro, boring, repeating yourself, confusing sentences, and more.",
                                route="/problems/", current="learn", body=body))


def search_page() -> None:
    index = []
    for g in GUIDES:
        sec = SECTIONS_BY_ID.get(g["section"])
        index.append({"t": g["title"], "d": g.get("description", ""), "u": f"/learn/{g['section']}/{g['slug']}/", "s": sec["title"] if sec else ""})
    for t in TOOLS:
        index.append({"t": t["title"], "d": t["short"], "u": f"/tools/{t['id']}/", "s": "Tools"})
    for p in PROBLEMS:
        index.append({"t": p["q"], "d": p["fix"][:120], "u": "/problems/", "s": "Problems"})
    for x in GLOSSARY:
        index.append({"t": "Glossary: " + x["term"], "d": x["definition"], "u": "/glossary/", "s": "Glossary"})
    search_index = json.dumps(index, ensure_ascii=False).replace("</", "<\\/")
    (ROOT / "assets" / "search-index.js").write_text("window.__INDEX=" + search_index + ";\n", encoding="utf-8")
    body = f'''<div class="wrap">{breadcrumb(("Home", "/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Search</p>
<h1>Search BRYME.</h1>
<p>Search all our writing guides and tools. Try "how to write an essay", "comma rules", "word counter", or "how to submit an article".</p>
<div class="searchbar"><input id="q" type="search" placeholder="What do you want to learn about writing?" aria-label="Search" autocomplete="off"></div></section>
<section class="section"><div class="guide-grid" id="results"></div></section></div>
<script src="/assets/search-index.js"></script><script src="/assets/hub-tools.js" data-hub-search></script>'''
    write("/search/", page_wf(title="Search BRYME — writing guides and tools | BRYME",
                              description="Search BRYME's writing guides, tools and resources. Find how to write an essay, comma rules, how to write a work email, how to write a short story and more.",
                              route="/search/", current="learn", body=body))


def learn_index() -> None:
    by_group = {g["id"]: [] for g in SECTIONS["groups"]}
    for s in SECTIONS["sections"]:
        by_group.setdefault(s["group"], []).append(s)
    for gid in by_group:
        by_group[gid].sort(key=lambda s: s["order"])
    sections_html = ""
    for g in SECTIONS["groups"]:
        cards = "".join(
            f'<a class="path-card" href="/learn/{esc(s["id"])}/"><span class="card-num">{esc(s["icon"])}</span><h3>{esc(s["title"])}</h3><p>{esc(s.get("tagline", s.get("description", "")))}</p><span class="card-link">Explore →</span></a>'
            for s in by_group[g["id"]])
        sections_html += f'<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">{esc(g["title"])}</p><h2>{esc(g["subtitle"])}</h2></div></div><div class="card-grid">{cards}</div></div></section>'
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Learn to write</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>The BRYME Writing Hub</p>
<h1>Learn to write.</h1>
<p>Everything you need to write better — from the very first sentence to getting published and paid. Start where you are and follow the journey: learn, plan, write, check, improve, finish.</p>
<div class="searchbar"><form action="/search/" method="get"><input type="search" name="q" placeholder="What do you want to learn about writing? (e.g. essay, comma, email)" aria-label="Search guides"></form></div></section>
<div class="journey-strip"><ol class="steps-journey"><li>Learn</li><li>Plan</li><li>Write</li><li>Check</li><li>Improve</li><li>Finish</li></ol></div>
{sections_html}'''
    write("/learn/", page_wf(title="Learn to write — writing guides for every level | BRYME",
                             description="BRYME's Writing Hub: beginner-friendly guides on starting to write, writing basics, types of writing, grammar, editing, research, and getting published and paid.",
                             route="/learn/", current="learn", body=body,
                             schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME writing guides", "url": BASE + "/learn/", "about": "Writing"}))


def homepage() -> None:
    popular = [g for g in GUIDES if g.get("popular")][:6]
    latest = sorted(GUIDES, key=lambda g: g.get("updated", ""), reverse=True)[:6]
    pop_cards = "".join(
        f'<a class="path-card" href="/learn/{esc(g["section"])}/{esc(g["slug"])}/"><span class="card-num">GUIDE</span><h3>{esc(g["title"])}</h3><p>{esc(g.get("description", ""))}</p><span class="card-link">Open →</span></a>'
        for g in popular)
    qtools = [t for t in TOOLS if t["id"] in ("word-counter", "character-counter", "reading-time", "case-converter", "text-cleaner")][:5]
    qtool_cards = "".join(f'<a class="chip-card" href="/tools/{esc(t["id"])}/"><b>🛠</b><span>{esc(t["title"])}</span></a>' for t in qtools)
    latest_cards = "".join(
        f'<a class="path-card" href="/learn/{esc(g["section"])}/{esc(g["slug"])}/"><span class="card-num">NEW</span><h3>{esc(g["title"])}</h3><p>{esc(g.get("description", ""))}</p><span class="card-link">Open →</span></a>'
        for g in latest)
    featured_pubs = "".join(_bwf.pub_card(r, "h3") for r in WRITING[:4])
    body = f'''<section class="hero"><div class="wrap hero-grid"><div>
  <p class="kicker"><span class="kicker-dot"></span>Learn · Plan · Write · Check · Improve · Finish</p>
  <h1>Learn to write. Write with <em>confidence.</em></h1>
  <p class="hero-copy">BRYME is a complete writing resource — free guides, in-browser tools, and verified opportunities to get published and paid. Come as a beginner; leave with finished work.</p>
  <div class="actions"><a class="btn" href="/learn/">Start learning →</a><a class="btn secondary" href="/tools/">Open the tools</a><a class="btn secondary" href="/writing/">Write &amp; get paid</a></div>
</div><aside class="verify-card" aria-label="BRYME writing snapshot"><div class="verify-head"><h2 class="verify-title">BRYME snapshot</h2><span class="live-tag">Free</span></div><p class="verify-date">{TODAY}</p><div class="metric-row"><div class="metric"><b>{len(GUIDES)}</b><span>Writing guides</span></div><div class="metric"><b>{len(TOOLS)}</b><span>Free tools</span></div><div class="metric"><b>{len(WRITING)}</b><span>Opportunities</span></div></div><p class="verify-note">Guides and tools are free. Opportunities are researched and verified — a listing is an invitation to pitch, not a promise of payment.</p></aside></div>
<div class="wrap location-picker"><p class="location-picker-label">Quick tools <span class="location-picker-hint">— no account, run in your browser</span></p><div class="chip-grid">{qtool_cards}</div></div></section>
<section class="trust-strip"><div class="wrap trust-grid"><div class="trust-item"><span class="trust-icon">📚</span>Beginner-friendly guides</div><div class="trust-item"><span class="trust-icon">🛠</span>Free in-browser tools</div><div class="trust-item"><span class="trust-icon">✓</span>Verified opportunities</div></div></section>

<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Learn writing</p><h2>Start from the beginning.</h2></div><a class="card-link" href="/learn/">All {len(GUIDES)} guides →</a></div><div class="guide-grid">{pop_cards}</div></div></section>

<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Write differently</p><h2>Match the form to the job.</h2></div></div><div class="card-grid">
<a class="path-card" href="/learn/academic-writing/"><span class="card-num">🎓</span><h3>Academic</h3><p>Essays, research papers, citations — done your own way.</p></a>
<a class="path-card" href="/learn/professional-writing/"><span class="card-num">💼</span><h3>Professional</h3><p>Emails, reports, proposals and clear workplace writing.</p></a>
<a class="path-card" href="/learn/creative-writing/"><span class="card-num">✎</span><h3>Creative</h3><p>Stories, characters, dialogue and voice.</p></a>
<a class="path-card" href="/learn/online-writing/"><span class="card-num">🌐</span><h3>Online</h3><p>Blogs, SEO and content that gets read.</p></a>
<a class="path-card" href="/learn/journaling-personal/"><span class="card-num">☕</span><h3>Personal</h3><p>Journaling and writing for yourself.</p></a>
</div></div></section>

<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Improve your writing</p><h2>Getting better on purpose.</h2></div></div><div class="guide-grid">
<a class="path-card" href="/learn/grammar-language/"><span class="card-num">Aa</span><h3>Grammar &amp; language</h3><p>The rules, explained simply with examples.</p></a>
<a class="path-card" href="/learn/editing-proofreading/"><span class="card-num">✓</span><h3>Editing &amp; proofreading</h3><p>From rough draft to error-clean piece.</p></a>
<a class="path-card" href="/learn/research-sources/"><span class="card-num">⌕</span><h3>Research &amp; sources</h3><p>Find reliable sources and use them honestly.</p></a>
<a class="path-card" href="/learn/common-problems/"><span class="card-num">⚑</span><h3>Common problems</h3><p>Fix the things that actually trip you up.</p></a>
</div></div></section>

<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Write &amp; publish</p><h2>Turn finished work into published, paid work.</h2></div></div><div class="guide-grid">{featured_pubs}</div><div class="actions"><a class="btn" href="/writing/">See all {len(WRITING)} opportunities →</a><a class="btn secondary" href="/templates/">Templates</a><a class="btn secondary" href="/checklists/">Checklists</a></div></div></section>

<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Latest guides</p><h2>Newest from the Writing Hub.</h2></div></div><div class="guide-grid">{latest_cards}</div></div></section>'''
    structured = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": "BRYME", "url": BASE + "/", "description": "Learn to write, use free writing tools, and find verified paid writing opportunities."},
        {"@context": "https://schema.org", "@type": "Organization", "name": "BRYME", "url": BASE + "/", "founder": {"@type": "Person", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/"}},
    ]
    write("/", page_wf(title="BRYME — learn to write, tools, and paid writing opportunities",
                       description="BRYME is a complete writing resource: free beginner-friendly guides, in-browser writing tools, and verified opportunities to get published and paid.",
                       route="/", current="", body=body, schema_data=structured))


def build() -> None:
    homepage()
    learn_index()
    for sec in SECTIONS["sections"]:
        section_hub(sec)
    for g in GUIDES:
        guide_page(g)
    tools_index()
    for t in TOOLS:
        tool_page(t)
    glossary_page()
    templates_page()
    checklists_page()
    problems_page()
    search_page()
    print(f"wrote hub: {len(GUIDES)} guides, {len(TOOLS)} tools, {len(SECTIONS['sections'])} sections, /search/ + /glossary/ + /templates/ + /checklists/ + /problems/")


if __name__ == "__main__":
    build()
