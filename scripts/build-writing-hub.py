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
nav = _bwf.nav
mobile_nav = _bwf.mobile_nav
howto_nav = _bwf.howto_nav
section_nav = _bwf.section_nav
TOOLS_NAV = [
    ("tools", "/tools/", "All tools"),
    ("templates", "/templates/", "Templates"),
    ("checklists", "/checklists/", "Checklists"),
    ("writing", "/writing/", "Paid opportunities"),
    ("guides", "/guides/", "Writing guides"),
    ("glossary", "/glossary/", "Glossary"),
]
LEARN_NAV = [
    ("learn", "/learn/", "All how-tos"),
    ("examples", "/learn/examples/", "Examples"),
    ("dos-and-donts", "/learn/dos-and-donts/", "Dos & don'ts"),
    ("types-of-writing", "/learn/types-of-writing/", "Writing types"),
    ("academic-writing", "/learn/academic-writing/", "Academic"),
    ("creative-writing", "/learn/creative-writing/", "Creative"),
    ("editing-proofreading", "/learn/editing-proofreading/", "Editing"),
    ("writing-for-publication", "/learn/writing-for-publication/", "Get published"),
]
WRITING = _bwf.WRITING


def load(name: str):
    return json.loads((ROOT / "content" / "hub" / name).read_text(encoding="utf-8"))


SECTIONS = load("sections.json")
TOOL_CONTENT = json.loads((ROOT / "content" / "hub" / "tool-content.json").read_text(encoding="utf-8"))
GROUPS = {g["id"]: g for g in SECTIONS["groups"]}
SECTIONS_BY_ID = {s["id"]: s for s in SECTIONS["sections"]}
TOOLS = load("tools.json")["tools"]
TOOLS_BY_ID = {t["id"]: t for t in TOOLS}
GLOSSARY = load("glossary.json")["terms"]
TEMPLATES = load("templates.json")["templates"]
PURPOSES = load("purposes.json")
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


LEVELS = {
    "beginner":     ("Beginner",     "Start here — assumes no prior knowledge."),
    "intermediate": ("Intermediate", "Assumes you can already draft and revise a piece."),
    "advanced":     ("Advanced",     "For longer or professional projects with higher stakes."),
}


def level_of(g: dict) -> str:
    lv = (g.get("level") or "intermediate").strip().lower()
    return lv if lv in LEVELS else "intermediate"


def level_badge(g: dict) -> str:
    """Skill-level tag. The word is always present, never colour alone."""
    lv = level_of(g)
    label, _ = LEVELS[lv]
    return f'<span class="level-badge level-{lv}">{esc(label)}</span>'


def guide_card(g: dict, heading: str = "h3") -> str:
    """Shared guide card carrying its skill level, so /learn/ can filter."""
    lv = level_of(g)
    return (f'<a class="guide-card" data-level="{lv}" href="/learn/{esc(g["section"])}/{esc(g["slug"])}/">'
            f'<span class="card-num">GUIDE</span>{level_badge(g)}'
            f'<{heading}>{esc(g["title"])}</{heading}>'
            f'<p>{esc(g.get("description", ""))}</p>'
            f'<span class="card-link">Open the guide →</span></a>')


def level_filter(guides: list[dict], label: str = "guides") -> str:
    """Static skill-level filter. Radio buttons, so it works without JS and is
    keyboard/screen-reader native; JS only hides cards."""
    counts = {k: sum(1 for g in guides if level_of(g) == k) for k in LEVELS}
    opts = [f'<label class="level-opt"><input type="radio" name="level" value="all" checked>'
            f'<span>All levels <b>{len(guides)}</b></span></label>']
    for key, (lab, _desc) in LEVELS.items():
        if not counts[key]:
            continue
        opts.append(f'<label class="level-opt level-opt-{key}"><input type="radio" name="level" value="{key}">'
                    f'<span>{esc(lab)} <b>{counts[key]}</b></span></label>')
    return (f'<form id="level-filter" class="level-filter" aria-label="Filter {esc(label)} by skill level">'
            f'<span class="level-filter-label">Your level</span>'
            f'<div class="level-opts">{"".join(opts)}</div>'
            f'<p id="level-note" class="level-note" aria-live="polite">Showing all {len(guides)} {esc(label)}.</p>'
            f'</form>')


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
    body = f'''{howto_nav(g['section'])}<div class="wrap">{breadcrumb(("Learn", "/learn/"), (section["title"], f"/learn/{section['id']}/"), (g["title"], ""))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(section['title'])}</p>
<h1>{esc(g['title'])}</h1>
<p>{esc(g.get('description', ''))}</p>
<p class="level-line">{level_badge(g)} <span class="level-desc">{esc(LEVELS[level_of(g)][1])}</span></p>
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
        body = f'''{howto_nav(sec['id'])}<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
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
        cards = "".join(guide_card(g, "h2") for g in guides)
        content = (f'<section class="section">{level_filter(guides)}'
                   f'<div class="guide-grid">{cards}</div></section>')
        robots = "index,follow"
    else:
        content = '<section class="section"><div class="prose"><p>This section is being written. Check back soon — BRYME adds new guides steadily. In the meantime, browse the <a href="/learn/">full library</a> or the <a href="/writing/">paid writing opportunities</a>.</p></div></section>'
        robots = "noindex,follow"
    body = f'''{howto_nav(sec['id'])}<div class="wrap">{breadcrumb(("Learn", "/learn/"))}
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
{section_nav(TOOLS_NAV, "Writing resources", "tools")}
<section class="section"><div class="guide-grid">{''.join(grid)}</div></section></div>'''
    write("/tools/", page_wf(title="Writing tools — free word counter, character counter and more | BRYME",
                            description=f"{len(TOOLS)} free in-browser writing tools: word counter, character counter, reading time, readability score, case converter, text cleaner, outline generator and more. No account needed.",
                            route="/tools/", current="tools", body=body,
                            schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME writing tools", "url": BASE + "/tools/"}))


def tool_page(t: dict) -> None:
    # Substantive per-tool SEO content (how/what/why) so tool pages aren't thin.
    tc = TOOL_CONTENT.get(t["id"], {})
    about = ""
    if tc:
        about = f'''<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">About this tool</p><h2>How to use the {esc(t['title'].lower())}.</h2></div></div>
<div class="prose">
<p><b>What it does.</b> {esc(tc.get('what', t.get('description', '')))}</p>
<p><b>How to use it.</b> {esc(tc.get('howto', ''))}</p>
<p><b>Why it matters.</b> {esc(tc.get('why', ''))}</p>
</div>
<div class="related-cta"><a class="btn secondary" href="/tools/">← All writing tools</a></div>
</div></section>'''
    body = f'''<div class="wrap">{breadcrumb(("Writing tools", "/tools/"))}
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Free tool</p>
<h1>{esc(t['title'])}.</h1>
<p>{esc(t['description'])}</p>
<a class="btn secondary" href="/tools/">← All tools</a></section>
<section class="section">{render_tool(t)}</section></div>
{about}'''
    st = t.get("seo_title") or f"{t['title']} — free online writing tool | BRYME"
    sd = t.get("seo_desc") or f"Free {t['title'].lower()} from BRYME. It works instantly in your browser — no account, no upload, no download."
    write(f"/tools/{t['id']}/", page_wf(
        title=st,
        description=sd,
        route=f"/tools/{t['id']}/", current="tools", body=body,
        schema_data={"@context": "https://schema.org", "@type": "WebApplication", "name": t["title"], "applicationCategory": "Utility", "url": f"{BASE}/tools/{t['id']}/", "operatingSystem": "Any", "description": t["description"], "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


def pdf_render(i: str) -> str:
    """Markup for the in-browser PDF tools (fully client-side)."""
    if i == "pdf-editor":
        return '''<div class="tool-prose"><p>Open a PDF and <b>rotate, delete, reorder or merge</b> its pages, then export a new PDF. Runs entirely in your browser — nothing is uploaded.</p>
<label for="pdf-file">Choose a PDF</label><input id="pdf-file" type="file" accept="application/pdf">
<input id="pdf-file-src" type="file" accept="application/pdf" style="display:none">
<div class="tool-actions"><button id="editor-export" class="btn">Export edited PDF</button></div>
<div class="tool-note" id="editor-status"></div>
<span class="tool-note" id="editor-count"></span>
<div class="pdf-pages" id="pages-list"></div></div>'''
    if i == "pdf-to-text":
        return '''<div class="tool-prose"><p>Extract the text from a PDF so you can copy, edit or reuse it. Runs in your browser.</p>
<label for="pdft-text-file">Choose a PDF</label><input id="pdft-text-file" type="file" accept="application/pdf">
<textarea id="pdft-out" readonly placeholder="Extracted text appears here…"></textarea>
<div class="tool-actions"><button id="pdft-copy" class="btn">Copy text</button></div>
<span class="tool-note" id="pdft-count"></span>
<div class="tool-note" id="pdft-status"></div></div>'''
    if i == "text-to-pdf":
        return '''<div class="tool-prose"><p>Turn plain text into a clean, downloadable PDF. Great for a first draft or a simple document. Runs in your browser.</p>
<label>Your text</label><textarea id="txt2pdf-in" placeholder="Type or paste your text here…"></textarea>
<div class="tool-actions"><button id="txt2pdf-go" class="btn">Create PDF</button></div>
<div class="tool-note" id="txt2pdf-status"></div></div>'''
    if i == "images-to-pdf":
        return '''<div class="tool-prose"><p>Turn one or more JPG/PNG images into a single PDF, each on its own page. Runs in your browser.</p>
<label for="img2pdf-file">Choose images</label><input id="img2pdf-file" type="file" accept="image/*" multiple>
<div class="tool-actions"><button id="img2pdf-add" class="btn">Add images</button></div>
<div class="tool-note" id="img2pdf-status"></div></div>'''
    return ""


def render_tool(t: dict) -> str:
    i = t["id"]
    if i == "tone-checker":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Paste a paragraph or a full draft. BRYME estimates how formal it sounds and shows you which signals produced that estimate.</p>
<label for="ta">Your text</label><textarea id="ta" placeholder="Paste your draft here…"></textarea><div class="tool-result" id="out" aria-live="polite"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="tone-checker"></script>'''
    if i == "citation-formatter":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Fill in what you have. The reference updates as you type.</p>
<div class="tool-grid"><div class="tool-input"><label for="style">Style</label><select id="style"><option value="apa">APA (7th)</option><option value="mla">MLA (9th)</option><option value="chicago">Chicago</option></select></div>
<div class="tool-input"><label for="ctype">Source type</label><select id="ctype"><option value="web">Web page or article</option><option value="book">Book</option></select></div></div>
<div class="tool-grid"><div class="tool-input"><label for="author">Author</label><input id="author" type="text" placeholder="Chinua Achebe" autocomplete="off"></div>
<div class="tool-input"><label for="year">Year</label><input id="year" type="text" placeholder="2024" autocomplete="off"></div></div>
<label for="title">Title</label><input id="title" type="text" placeholder="Title of the book, article or page" autocomplete="off">
<div class="tool-grid"><div class="tool-input"><label for="container">Journal, site or newspaper</label><input id="container" type="text" placeholder="The Guardian" autocomplete="off"></div>
<div class="tool-input"><label for="publisher">Publisher</label><input id="publisher" type="text" placeholder="Heinemann" autocomplete="off"></div></div>
<div class="tool-grid"><div class="tool-input"><label for="url">URL</label><input id="url" type="text" placeholder="https://…" autocomplete="off"></div>
<div class="tool-input"><label for="accessed">Date accessed (MLA)</label><input id="accessed" type="text" placeholder="4 Sept. 2026" autocomplete="off"></div></div>
<div class="tool-result" id="out" aria-live="polite"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="citation-formatter"></script>'''
    if i == "word-alternatives":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Type one overused word or phrase to see stronger options — and to be told when deleting it is the better move.</p>
<label for="w">Word or phrase</label><input id="w" type="text" placeholder="e.g. said, very, important, in order to" autocomplete="off">
<div class="tool-result" id="out" aria-live="polite"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="word-alternatives"></script>'''
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
    if i == "title-generator":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Type your topic and get a fresh bank of headlines.</p>
<label>Topic</label><input id="topic" type="text" placeholder="e.g. write a strong introduction" autocomplete="off"><label>Audience (optional)</label><input id="audience" type="text" placeholder="e.g. busy beginners" autocomplete="off"><div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="title-generator"></script>'''
    if i == "meta-description-generator":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Draft a search-friendly description under the character limit.</p>
<label>Page topic</label><input id="topic" type="text" placeholder="e.g. how to proofread" autocomplete="off"><label>Reader benefit</label><input id="benefit" type="text" placeholder="e.g. catch typos before you submit" autocomplete="off"><div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="meta-description-generator"></script>'''
    if i == "random-writing-prompt":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Click for a fresh prompt to beat the blank page.</p>
<div class="tool-actions"><button class="btn" id="new">New prompt</button></div><div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="random-writing-prompt"></script>'''
    if i == "word-document-converter":
        return f'''<div class="tool-box"><div class="tool-prose"><p>Paste or write your text, then download it as a Word-compatible file. Everything happens in your browser — nothing is uploaded.</p>
<label>Your text</label><textarea id="ta" placeholder="Paste or write your document here…"></textarea>
<div class="tool-actions"><label class="tool-select">Format <select id="format"><option value="doc">Word (.doc)</option><option value="txt">Plain text (.txt)</option></select></label><button id="download" class="btn">Download document</button></div>
<div class="tool-result" id="out"></div></div></div>
<script src="/assets/hub-tools.js" data-hub-tool="word-document-converter"></script>'''
    if i == "pdf-editor":
        # editor uses pdf.js for thumbnails and pdf-lib to rebuild the file
        return f'''<div class="tool-box">{pdf_render(i)}</div>
<script src="/assets/vendor/pdfjs.min.js"></script>
<script src="/assets/vendor/pdf-lib.min.js"></script>
<script src="/assets/pdf-tools.js" data-hub-tool="{i}"></script>'''
    if i in ("text-to-pdf", "images-to-pdf"):
        return f'''<div class="tool-box">{pdf_render(i)}</div>
<script src="/assets/vendor/pdf-lib.min.js"></script>
<script src="/assets/pdf-tools.js" data-hub-tool="{i}"></script>'''
    if i == "pdf-to-text":
        return f'''<div class="tool-box">{pdf_render(i)}</div>
<script src="/assets/vendor/pdfjs.min.js"></script>
<script src="/assets/pdf-tools.js" data-hub-tool="{i}"></script>'''
    if i in ("self-plagiarism-checker",):
        return f'''<div class="tool-box"><div class="tool-prose"><p>Check your text for repeated or near-identical sentences <em>within itself</em> — a self-plagiarism and internal-duplication check. Everything runs locally in your browser.</p>
<textarea id="plag-in" placeholder="Paste your text here…"></textarea>
<div class="tool-actions"><button id="plag-run" class="btn">Check for repetition</button></div>
<div class="tool-result" id="plag-out"></div></div></div>
<script src="/assets/pdf-tools.js" data-hub-tool="self-plagiarism-checker"></script>'''
    if i in ("ai-writing-checker",):
        return f'''<div class="tool-box"><div class="tool-prose"><p>A <b>rule-based heuristic</b> look for formulaic phrases and AI-favoured words in your text. It is an honest nudge to sound more natural — not a real AI detector (no tool can reliably do that).</p>
<textarea id="ai-in" placeholder="Paste your text here…"></textarea>
<div class="tool-actions"><button id="ai-run" class="btn">Analyse style</button></div>
<div class="tool-result" id="ai-out"></div></div></div>
<script src="/assets/pdf-tools.js" data-hub-tool="ai-writing-checker"></script>'''
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
{section_nav(TOOLS_NAV, "Writing resources", "templates")}
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
{section_nav(TOOLS_NAV, "Writing resources", "checklists")}
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
    body = f'''{howto_nav('learn')}<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / How to write</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>The BRYME Writing Hub</p>
<h1>How to write.</h1>
<p>Everything you need to write better — from the very first sentence to getting published and paid. Start where you are and follow the journey: learn, plan, write, check, improve, finish.</p>
<div class="searchbar"><form action="/search/" method="get"><input type="search" name="q" placeholder="What do you want to learn about writing? (e.g. essay, comma, email)" aria-label="Search guides"></form></div></section>
<div class="journey-strip"><ol class="steps-journey"><li>Learn</li><li>Plan</li><li>Write</li><li>Check</li><li>Improve</li><li>Finish</li></ol></div>
{sections_html}
<section class="section alt" id="all-guides"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Every guide</p><h2>Browse all {len(GUIDES)} guides by your level.</h2></div>
<p>Not sure where to start? Filter by how much writing experience you already have.</p></div>
{level_filter(sorted(GUIDES, key=lambda x: x["title"]), "guides")}
<div class="guide-grid">{"".join(guide_card(g) for g in sorted(GUIDES, key=lambda x: x["title"]))}</div>
</div></section>'''
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


def prune_stale_guides() -> None:
    """Remove guide pages that no longer exist (e.g. after a guide's section
    changes) so no stale/duplicate routes remain on disk."""
    import shutil
    current = {f"/learn/{g['section']}/{g['slug']}" for g in GUIDES}
    root = ROOT / "learn"
    if not root.is_dir():
        return
    for section_dir in root.iterdir():
        if not section_dir.is_dir():
            continue
        for slug_dir in section_dir.iterdir():
            if not slug_dir.is_dir():
                continue
            route = f"/learn/{section_dir.name}/{slug_dir.name}"
            if route not in current:
                shutil.rmtree(slug_dir, ignore_errors=True)


# --------------------------------------------------------------------------
# "Writing by purpose" finder + the complete beginner path
# --------------------------------------------------------------------------
TEMPLATES_BY_ID = {t["id"]: t for t in TEMPLATES}


def _validate_purposes() -> None:
    """Fail the build rather than ship a finder that routes to a 404."""
    bad = []
    for item in PURPOSES["purposes"]:
        for key in ("guide", "also"):
            slug = item.get(key)
            if slug and slug not in GUIDES_BY_SLUG:
                bad.append(f'{item["q"]}: {key}="{slug}" is not a guide')
        t = item.get("template")
        if t and t not in TEMPLATES_BY_ID:
            bad.append(f'{item["q"]}: template="{t}" is not a template')
        tl = item.get("tool")
        if tl and tl not in TOOLS_BY_ID:
            bad.append(f'{item["q"]}: tool="{tl}" is not a tool')
        if not item.get("guide") and not item.get("template"):
            bad.append(f'{item["q"]}: routes nowhere')
    if bad:
        raise SystemExit("purposes.json has broken routes:\n  - " + "\n  - ".join(bad))


def purpose_finder_page() -> None:
    _validate_purposes()
    cats = {c["id"]: c for c in PURPOSES["categories"]}
    by_cat: dict[str, list[dict]] = {}
    for item in PURPOSES["purposes"]:
        by_cat.setdefault(item["cat"], []).append(item)

    blocks = []
    for c in PURPOSES["categories"]:
        items = by_cat.get(c["id"], [])
        if not items:
            continue
        rows = []
        for it in items:
            links = []
            g = GUIDES_BY_SLUG.get(it.get("guide", ""))
            if g:
                links.append(f'<a class="purpose-go" href="/learn/{esc(g["section"])}/{esc(g["slug"])}/">Read the guide →</a>')
            a = GUIDES_BY_SLUG.get(it.get("also", ""))
            if a:
                links.append(f'<a class="purpose-alt" href="/learn/{esc(a["section"])}/{esc(a["slug"])}/">{esc(a["title"])}</a>')
            t = TEMPLATES_BY_ID.get(it.get("template", ""))
            if t:
                links.append(f'<a class="purpose-alt" href="/templates/#{esc(t["id"])}">{esc(t["title"])} template</a>')
            tl = TOOLS_BY_ID.get(it.get("tool", ""))
            if tl:
                links.append(f'<a class="purpose-alt" href="/tools/{esc(tl["id"])}/">{esc(tl["title"])}</a>')
            lvl = f'{level_badge(g)}' if g else ""
            note = f'<p class="purpose-note">{esc(it["note"])}</p>' if it.get("note") else ""
            rows.append(
                f'<li class="purpose-row" data-purpose="{esc(it["q"].lower())} {esc(c["title"].lower())}">'
                f'<div class="purpose-q"><b>I need to write {esc(it["q"])}</b>{lvl}</div>'
                f'{note}<div class="purpose-links">{"".join(links)}</div></li>')
        blocks.append(
            f'<section class="section" data-cat-block><div class="wrap">'
            f'<div class="section-head"><div><p class="eyebrow">{esc(c["icon"])} {esc(c["title"])}</p>'
            f'<h2>{esc(c["blurb"])}</h2></div></div>'
            f'<ul class="purpose-list">{"".join(rows)}</ul></div></section>')

    total = len(PURPOSES["purposes"])
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / What do you want to write?</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Find the right guide</p>
<h1>What are you trying to write?</h1>
<p>You do not need to know the name of the format to find help with it. Say what you are trying to write and BRYME points you at the guide, the template and the tool for it — {total} starting points across {len(PURPOSES["categories"])} situations.</p>
<div class="purpose-search"><label for="purpose-q" class="sr-only">Search what you want to write</label>
<input id="purpose-q" type="search" placeholder="Type what you need — e.g. email, essay, speech, pitch" autocomplete="off">
<p id="purpose-count" class="purpose-count" aria-live="polite">{total} things to write</p>
<p id="purpose-empty" class="purpose-count empty" hidden>Nothing matches that yet. Try a simpler word — “letter”, “story”, “report” — or <a href="/learn/">browse every guide</a>.</p></div>
</section></div>
{"".join(blocks)}
<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Not listed?</p><h2>Still not sure what you need.</h2></div></div>
<div class="card-grid">
<a class="path-card" href="/start/"><span class="card-num">PATH</span><h3>Start from the beginning</h3><p>A guided track through the essentials, in order, for anyone starting from zero.</p><span class="card-link">Open the beginner path →</span></a>
<a class="path-card" href="/learn/"><span class="card-num">ALL</span><h3>Browse every guide</h3><p>All {len(GUIDES)} guides, filterable by your skill level.</p><span class="card-link">Browse the library →</span></a>
<a class="path-card" href="/contact/"><span class="card-num">ASK</span><h3>Ask BRYME</h3><p>No guide for your problem? Tell the desk and it may become one.</p><span class="card-link">Contact the desk →</span></a>
</div></div></section>'''
    write("/find/", page_wf(
        title="What do you want to write? Find the right guide | BRYME",
        description=f"Say what you are trying to write — an email, an essay, a speech, a pitch — and BRYME routes you to the right guide, template and tool. {total} starting points.",
        route="/find/", current="learn", body=body,
        schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                     "name": "What do you want to write?", "url": BASE + "/find/"}))


BEGINNER_PATH = [
    ("what-is-writing", "Understand what writing actually is before worrying about doing it well."),
    ("how-to-start-writing", "Get words on the page for the first time, without a plan or confidence."),
    ("sentence-basics", "The unit everything else is built from."),
    ("paragraph-basics", "Group sentences so a reader can follow you."),
    ("tone-voice-audience", "Decide who you are writing for — this changes every other choice."),
    ("how-to-brainstorm-and-find-ideas", "Find something worth saying."),
    ("how-to-turn-an-idea-into-an-outline", "Turn a vague idea into a shape you can write."),
    ("the-writing-process", "See the whole journey so you know which stage you are in."),
    ("how-to-write-an-introduction", "Open in a way that makes someone keep reading."),
    ("how-to-write-a-conclusion", "End on purpose instead of just stopping."),
    ("how-to-use-headings-effectively", "Make a longer piece navigable."),
    ("common-grammar-mistakes", "Fix the errors that cost you credibility fastest."),
    ("comma-rules", "The single most misused mark in English."),
    ("active-vs-passive-voice", "Make sentences direct."),
    ("how-to-make-writing-more-concise", "Cut what is not earning its place."),
    ("how-to-edit-your-own-writing", "Become your own first editor."),
    ("how-to-proofread", "Catch what editing missed, before anyone else sees it."),
    ("how-to-overcome-writers-block", "Keep going when it stops being fun."),
    ("how-to-build-a-writing-routine", "Turn writing into something you do, not something you plan to do."),
    ("how-to-tell-if-your-writing-is-good", "Judge your own work honestly and know what to fix next."),
]


def beginner_path_page() -> None:
    missing = [s for s, _ in BEGINNER_PATH if s not in GUIDES_BY_SLUG]
    if missing:
        raise SystemExit(f"beginner path references missing guides: {missing}")
    steps = []
    for i, (slug, why) in enumerate(BEGINNER_PATH, 1):
        g = GUIDES_BY_SLUG[slug]
        steps.append(
            f'<li class="path-step"><span class="path-num">{i:02d}</span>'
            f'<div class="path-step-body"><h3><a href="/learn/{esc(g["section"])}/{esc(g["slug"])}/">{esc(g["title"])}</a></h3>'
            f'<p class="path-why">{esc(why)}</p>'
            f'<p class="path-meta">{level_badge(g)}</p></div></li>')
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Complete beginner path</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Structured learning</p>
<h1>The complete beginner path.</h1>
<p>{len(BEGINNER_PATH)} guides in a deliberate order, for anyone who would rather be taught than browse. Each one assumes only what came before it. Work through them at any pace — nothing here expires, and there is nothing to sign up for.</p>
<div class="source-line"><span><b>{len(BEGINNER_PATH)}</b> guides</span><span>Free, no account</span><span><a href="/find/">Or jump to a specific thing you need to write →</a></span></div></section>
<section class="section"><ol class="path-list">{"".join(steps)}</ol></section>
<section class="section alt"><div class="section-head"><div><p class="eyebrow">After the path</p><h2>Where to go next.</h2></div></div>
<div class="card-grid">
<a class="path-card" href="/learn/?level=intermediate"><span class="card-num">NEXT</span><h3>Intermediate guides</h3><p>Formats and craft that assume you can already draft and revise.</p><span class="card-link">Browse intermediate →</span></a>
<a class="path-card" href="/find/"><span class="card-num">FIND</span><h3>Write a specific thing</h3><p>Jump straight to the guide for the document in front of you.</p><span class="card-link">Open the finder →</span></a>
<a class="path-card" href="/writing/"><span class="card-num">PAID</span><h3>Get published and paid</h3><p>Researched publications that pay writers, with the pay and rules recorded.</p><span class="card-link">See opportunities →</span></a>
</div></section></div>'''
    write("/start/", page_wf(
        title=f"The complete beginner path — {len(BEGINNER_PATH)} writing guides in order | BRYME",
        description=f"A guided track through the {len(BEGINNER_PATH)} most essential BRYME writing guides, in order, for complete beginners. Free, no account needed.",
        route="/start/", current="learn", body=body,
        schema_data={"@context": "https://schema.org", "@type": "Course",
                     "name": "The complete beginner writing path", "url": BASE + "/start/",
                     "description": "A structured, ordered track through BRYME's essential writing guides for complete beginners.",
                     "provider": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
                     "isAccessibleForFree": True}))


def build() -> None:
    prune_stale_guides()
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
    purpose_finder_page()
    beginner_path_page()
    print(f"wrote hub: {len(GUIDES)} guides, {len(TOOLS)} tools, {len(SECTIONS['sections'])} sections, /search/ + /glossary/ + /templates/ + /checklists/ + /problems/")


if __name__ == "__main__":
    build()
