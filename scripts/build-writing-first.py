#!/usr/bin/env python3
"""Build the WRITING-FIRST BRYME main branch.

Reuses the existing focused-site shell (page(), esc(), schema(), write(), BASE,
SITE, cfg, TODAY) from build-focus-site.py so the infrastructure — site_config,
SITE_URL env handling, canonical/OG/twitter/schema head, server, discovery —
is shared rather than forked.

This builder emits the writing-first surface:
  /                       writing-first homepage
  /writing/               hub + all 55 publication cards
  /writing/<slug>/        one permanent page per publication (canonical)
  /guides/                writing-guide hub
  /guides/<slug>/         writing guide pages
  /tested/                BRYME Tested index
  /about/                 writing-first about page
  + trust/legal pages and 404/410.

Legacy multi-niche output is preserved on the `legacy-multiniche` branch and
archived in-tree under legacy-site/ — it is not generated here and not promoted.
"""
from __future__ import annotations
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))  # scripts import `bryme_config` by name

# Reuse the working focused-site shell (not a fork): page(), esc(), schema(),
# write(), BASE, SITE, cfg, TODAY, TODAY_HUMAN, footer().
_spec = importlib.util.spec_from_file_location("build_focus_site", ROOT / "scripts" / "build-focus-site.py")
_build_focus = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_build_focus)
ROOT = _build_focus.ROOT
BASE = _build_focus.BASE
TODAY = _build_focus.TODAY
TODAY_HUMAN = _build_focus.TODAY_HUMAN
SITE = _build_focus.SITE
cfg = _build_focus.cfg
esc = _build_focus.esc
schema = _build_focus.schema
write = _build_focus.write
footer = _build_focus.footer


def footer() -> str:
    """Writing-first footer: no jobs/opportunities/earn links."""
    return '''<footer class="site-foot"><div class="wrap foot-grid">
  <div class="foot-brand"><a class="logo" href="/"><span class="logo-mark" aria-hidden="true">B</span>BRYME</a><p>BRYME helps writers find legitimate opportunities to get published and paid — verified sources, honest limits.</p></div>
  <div class="foot-col"><b>Write</b><a href="/writing/">Writing opportunities</a><a href="/writing/afrolicious/">BRYME-tested example</a><a href="/guides/">Writing guides</a><a href="/tested/">BRYME Tested</a></div>
  <div class="foot-col"><b>Trust</b><a href="/about/">About</a><a href="/editorial-policy/">Editorial policy</a><a href="/corrections/">Corrections</a><a href="/privacy/">Privacy</a><a href="/contact/">Contact</a></div>
  <div class="foot-col"><b>Legal</b><a href="/terms/">Terms</a><a href="/disclaimer/">Disclaimer</a><a href="/copyright/">Copyright</a></div>
</div><div class="wrap foot-bottom">© 2026 BRYME · Independent editorial project · No acceptance, publication or payment is guaranteed.</div></footer>'''


WRITING = json.loads((ROOT / "content/opportunities.json").read_text(encoding="utf-8"))["opportunities"]

# ---------------------------------------------------------------------------
# Navigation — writing-first desktop + 4-item mobile bottom bar
# ---------------------------------------------------------------------------
def nav(current: str = "") -> str:
    links = [
        ("writing", "/writing/", "Writing Opportunities"),
        ("guides", "/guides/", "Writing Guides"),
        ("tested", "/tested/", "BRYME Tested"),
        ("about", "/about/", "About"),
    ]
    items = []
    for key, href, label in links:
        aria = ' aria-current="page"' if key == current else ""
        cls = ' class="nav-cta"' if key == "writing" else ""
        items.append(f'<a{cls}{aria} href="{href}">{label}</a>')
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap head-in">
  <a class="logo" href="/" aria-label="BRYME home"><span class="logo-mark" aria-hidden="true">B</span>BRYME</a>
  <nav class="main-nav" aria-label="Primary">{''.join(items)}</nav>
  <form class="nav-search-form" action="/writing/" method="get" role="search"><input type="search" name="q" placeholder="Search opportunities…" aria-label="Search writing opportunities" autocomplete="off"></form>
</div></header>'''


def mobile_nav(current: str = "") -> str:
    links = [
        ("writing", "/writing/", "📝", "Opportunities"),
        ("guides", "/guides/", "📚", "Guides"),
        ("tested", "/tested/", "🧪", "Tested"),
        ("about", "/about/", "👤", "About"),
    ]
    return '<nav class="bottom-nav bottom-nav--writing" aria-label="Primary mobile">' + ''.join(
        f'<a href="{href}"' + (' aria-current="page"' if key == current else '') +
        f'><span aria-hidden="true">{icon}</span>{label}</a>' for key, href, icon, label in links
    ) + '</nav>'


def page_wf(*, title: str, description: str, route: str, current: str, body: str,
            schema_data: object | None = None, robots: str = "index,follow") -> str:
    """Writing-first page: the shared shell with a writing-first graph + nav.

    (Copied from build_focus_site.page so the writing branch controls its own
    SearchAction/site graph and nav while keeping the same hardened head.)
    """
    canonical = BASE + route
    ca_id = str(cfg.publisher_config().get("caId") or "").strip()
    adsense_meta = f'<meta name="google-adsense-account" content="{esc(ca_id)}">' if ca_id else ""
    structured = schema_data or {
        "@context": "https://schema.org", "@type": "WebPage",
        "name": title.split(" | ")[0], "description": description, "url": canonical,
        "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
    }
    site_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": BASE + "/#org", "name": SITE["name"],
             "url": BASE + "/", "description": SITE["description"],
             "founder": {"@type": "Person", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/"}},
            {"@type": "WebSite", "@id": BASE + "/#site", "name": SITE["name"],
             "url": BASE + "/", "description": SITE["description"],
             "publisher": {"@id": BASE + "/#org"},
             "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint",
                                   "urlTemplate": BASE + "/writing/?q={search_term_string}"},
                                 "query-input": "required name=search_term_string"}},
        ],
    }
    return f'''<!doctype html>
<html lang="en-NG"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#07100d">
<meta name="color-scheme" content="dark">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{esc(robots)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:site_name" content="BRYME">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}">
{adsense_meta}
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/bryme-v2.css">
{schema(site_graph)}
{schema(structured)}
</head><body>{nav(current)}<main id="main">{body}</main>{mobile_nav(current)}{footer()}</body></html>'''


# ---------------------------------------------------------------------------
# Status helpers
# ---------------------------------------------------------------------------
STATUS_ROBOTS = {
    "open":   ("🟢 Currently accepting",            "accepting",  "open"),
    "rolling":("🟢 Rolling submissions",            "rolling",    "open"),
    "upcoming":("🟡 Opens soon",                    "upcoming",   "unknown"),
    "deadline":("🟡 Limited window",                "limited",    "unknown"),
    "closed": ("🔴 Currently closed",               "closed",     "closed"),
    "unknown":("🟡 Information needs verification", "needs-verification", "unknown"),
}


def status_of(rec: dict) -> tuple[str, str, str]:
    by = {"open": "open", "rolling": "open", "upcoming": "unknown",
          "deadline": "unknown", "closed": "closed", "unknown": "unknown",
          None: "unknown"}
    from_status = rec.get("submissionStatus")
    label, cls, _ = STATUS_ROBOTS.get(from_status, STATUS_ROBOTS["unknown"])
    return label, cls, by.get(from_status, "unknown")


def status_badge(rec: dict) -> str:
    label, cls, _ = status_of(rec)
    return f'<span class="verify-badge {cls}">{esc(label)}</span>'


def verify_badge(rec: dict) -> str:
    """BRYME verification state for the publication card."""
    ex = rec.get("editorExperience") or {}
    st = ex.get("status")
    if not ex.get("applied"):
        return '<span class="verify-badge board-listed">🟡 Research only</span>'
    m = {"submitted": "🔵 Submitted", "accepted": "🟢 Accepted", "accepted-scheduled": "🟢 Accepted, scheduled",
         "published": "📖 Published", "paid": "💰 Paid", "rejected": "🔴 Rejected", "closed": "⚪ Closed"}
    return f'<span class="verify-badge verify">{m.get(st, st or "🔵 Submitted")}</span>'


def pub_card(rec: dict, heading: str = "h2") -> str:
    pay = (rec.get("pay") or {}).get("display") or "See page"
    wc = (rec.get("wordCount") or {}).get("display") or "—"
    el = (rec.get("eligibility") or {}).get("summary") or "See eligibility"
    url = f"/writing/{esc(rec['slug'])}/"
    return f'''<article class="job-card">
  <div class="job-card-badges">{status_badge(rec)}{verify_badge(rec)}</div>
  <{heading} class="job-card-title"><a href="{url}">{esc(rec['publication'])}</a></{heading}>
  <p class="job-card-sub">{esc(rec.get('writingTypeLabel') or rec.get('title') or '')}</p>
  <dl class="pub-facts">
    <dt>Pay</dt><dd>{esc(pay)}</dd>
    <dt>Words</dt><dd>{esc(wc)}</dd>
    <dt>Eligible</dt><dd>{esc(el.split('.')[0])}</dd>
    <dt>Verified</dt><dd>{esc((rec.get('lastVerified') or TODAY)[:7])}</dd>
  </dl>
  <div class="job-card-foot"><a class="card-link" href="{url}">View publication →</a></div>
</article>'''


# ---------------------------------------------------------------------------
# Homepage
# ---------------------------------------------------------------------------
def home() -> None:
    # Featured: the BRYME-tested record first, then a curated set of open ones.
    tested = [r for r in WRITING if (r.get("editorExperience") or {}).get("applied")]
    rest = [r for r in WRITING if not (r.get("editorExperience") or {}).get("applied")]
    def key(r):
        return 0 if r.get("submissionStatus") in ("open", "rolling") else 1
    rest.sort(key=key)
    featured = tested + rest[:5]
    cards = "".join(pub_card(r, "h3") for r in featured)
    n_open = sum(1 for r in WRITING if status_of(r)[2] == "open")
    body = f'''<section class="hero"><div class="wrap hero-grid"><div>
  <p class="kicker"><span class="kicker-dot"></span>Writing + research + trust</p>
  <h1>Find writing opportunities. Get published. Get <em>paid.</em></h1>
  <p class="hero-copy">BRYME researches legitimate writing opportunities — the publications, the pay, the word counts and who they're open to — and gives writers practical guides for pitching, submitting and getting published.</p>
  <div class="actions"><a class="btn" href="/writing/">Explore writing opportunities →</a><a class="btn secondary" href="/guides/">Browse writing guides</a><a class="btn secondary" href="/tested/">BRYME Tested</a></div>
</div><aside class="verify-card" aria-label="BRYME writing snapshot"><div class="verify-head"><h2 class="verify-title">Writing research snapshot</h2><span class="live-tag">Verified</span></div><p class="verify-date">{TODAY_HUMAN}</p><div class="metric-row"><div class="metric"><b>{len(WRITING)}</b><span>Publications</span></div><div class="metric"><b>{n_open}</b><span>Accepting now</span></div><div class="metric"><b>{len(tested)}</b><span>BRYME tested</span></div></div><p class="verify-note">Every publication page shows its last human-check date. "Open" is a timestamp, not a guarantee — always confirm the official guideline before pitching.</p></aside></div>
<div class="wrap location-picker"><p class="location-picker-label">Start with an opportunity <span class="location-picker-hint">— reviewed for pay, words and eligibility</span></p><div class="chip-grid">{''.join(f'<a class="chip-card" href="/writing/{esc(r["slug"])}/"><b>{esc((r.get("pay") or {}).get("display") or "—")}</b><span>{esc(r["publication"])}</span></a>' for r in WRITING[:6])}</div></div></section>
<section class="trust-strip"><div class="wrap trust-grid"><div class="trust-item"><span class="trust-icon">✓</span>Official submission guideline linked</div><div class="trust-item"><span class="trust-icon">✓</span>Pay and word count researched</div><div class="trust-item"><span class="trust-icon">✓</span>Eligibility and diaspora rules recorded</div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Featured opportunities</p><h2>Publications that pay writers.</h2></div><p>Each card links to a permanent BRYME page with the full detail and the official guideline.</p></div><div class="guide-grid">{cards}</div><div class="actions"><a class="btn" href="/writing/">See all {len(WRITING)} publications →</a></div></div></section>
<section class="section alt"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Guides</p><h2>From first pitch to first payment.</h2></div><p>Practical, writer-first resources that connect to the opportunities above.</p></div><div class="card-grid">
<a class="path-card" href="/guides/how-to-write-a-pitch/"><span class="card-num">01</span><h3>How to write a pitch</h3><p>The structure, subject line and clips that get a publication to say yes — explained plainly.</p><span class="card-link">Open the guide →</span></a>
<a class="path-card" href="/guides/how-to-find-paid-writing-opportunities/"><span class="card-num">02</span><h3>Find paid writing opportunities</h3><p>Where to look, how to judge legitimacy, and how to read a guidelines page.</p><span class="card-link">Open the guide →</span></a>
<a class="path-card" href="/guides/how-to-follow-up-on-a-writing-pitch/"><span class="card-num">03</span><h3>Follow up on a pitch</h3><p>When to wait, what to say, and how to treat silence without burning bridges.</p><span class="card-link">Open the guide →</span></a>
</div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Transparent by design</p><h2>What BRYME claims — and what it will not.</h2></div></div><div class="card-grid">
<div class="path-card"><span class="card-num">VERIFY</span><h3>Official guidelines first</h3><p>BRYME links to, and checks against, each publication's own guideline — not third-party reposts.</p></div>
<div class="path-card"><span class="card-num">TESTED</span><h3>Marked as it happens</h3><p>Where BRYME has personally pitched, the journey is shown step by step — accepted, published, paid — never assumed.</p></div>
<div class="path-card"><span class="card-num">LIMIT</span><h3>No guaranteed outcome</h3><p>An open submission window does not guarantee acceptance, publication or payment.</p></div>
</div></div></section>'''
    structured = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": "BRYME",
         "url": BASE + "/", "description": SITE["description"]},
        {"@context": "https://schema.org", "@type": "Organization", "name": "BRYME", "url": BASE + "/",
         "founder": {"@type": "Person", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/"}},
    ]
    write("/", page_wf(title="BRYME | Writing opportunities, guides and getting published",
                       description="BRYME researches legitimate paid writing opportunities for African and international writers, and gives practical guides for pitching, submitting and getting paid.",
                       route="/", current="writing", body=body, schema_data=structured))


# ---------------------------------------------------------------------------
# /writing/ hub
# ---------------------------------------------------------------------------
def writing_hub() -> None:
    n_open = sum(1 for r in WRITING if status_of(r)[2] == "open")
    cards = "".join(pub_card(r, "h2") for r in WRITING)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Writing opportunities</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Publications that pay writers</p>
<h1>Writing opportunities.</h1>
<p>{len(WRITING)} publications researched by BRYME. Each permanent page shows the type of writing, the published pay, word count, who it's open to, the submission method, and the official guideline to confirm before you pitch. A listing is an invitation to pitch — not a job offer or a promise of payment.</p>
<div class="source-line"><span><b>{len(WRITING)}</b> researched publications</span><span><b>{n_open}</b> currently accepting</span><span><b>{len([r for r in WRITING if (r.get("editorExperience") or {}).get("applied")])}</b> personally tested by BRYME</span></div></section>
<section class="section"><div class="how-steps"><h2 class="section-sub">How make-money writing works with BRYME</h2><ol class="steps">
<li><b>Pick an opportunity.</b> Each page names who it is open to — BRYME does not treat a missing country list as "open worldwide." Eligibility and diaspora rules are recorded where the publication states them.</li>
<li><b>Read the official guideline, not just the rate card.</b> Every page links to the publication's own guidelines and shows its last human-check date.</li>
<li><b>Understand the money before you pitch.</b> Payment is the published fee per accepted piece (or the real range), how and when it is paid, and whether it is per word, per piece or a variable honorarium. Rates are never invented.</li>
<li><b>Check the AI policy and rights.</b> Many publications reject AI-assisted work and take specific rights. BRYME records what each page says.</li>
<li><b>Pitch exactly as asked.</b> Send what the guideline requests through the official channel — a submission URL, form, or email.</li>
<li><b>Track it honestly.</b> Where BRYME has personally tested an opportunity, the journey is shown as it happens — pitch sent, response, accepted, scheduled, published, paid — and payment is only marked confirmed once it actually lands.</li>
</ol></div></section>
<section class="section alt"><div class="wrap">{cards}</div></section></div>'''
    write("/writing/", page_wf(title="Writing opportunities for African and international writers | BRYME",
                              description=f"{len(WRITING)} paid writing publications researched by BRYME — with published pay, word count, eligibility, submission method and the official guideline to confirm before pitching.",
                              route="/writing/", current="writing", body=body,
                              schema_data={"@context": "https://schema.org", "@type": "CollectionPage",
                                           "name": "BRYME writing opportunities", "url": BASE + "/writing/",
                                           "dateModified": TODAY, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


# ---------------------------------------------------------------------------
# /writing/<slug>/ publication page
# ---------------------------------------------------------------------------
def _facts(rec: dict) -> str:
    pay = rec.get("pay") or {}
    wc = rec.get("wordCount") or {}
    el = rec.get("eligibility") or {}
    resp = rec.get("response") or {}
    sub = rec.get("submissionStatus") or "unknown"
    rows = [
        ("Payment", pay.get("display") or "See official guideline"),
        ("Word count", wc.get("display") or "See official guideline"),
        ("Submission", (rec.get("applyMethod") or "See official guideline")),
        ("International writers", "Yes" if el.get("allowsDiaspora") or el.get("mode") != "restricted" else "No — see eligibility"),
        ("Status", status_of(rec)[0]),
        ("Last verified", (rec.get("lastVerified") or TODAY)[:7]),
    ]
    cells = "".join(f'<dt>{esc(k)}</dt><dd>{esc(v)}</dd>' for k, v in rows)
    return f'<div class="quick-facts"><h2 class="section-sub">Quick facts</h2><dl>{cells}</dl></div>'


def _list(label: str, items: list | None) -> str:
    if not items:
        return ""
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return f'<h3>{esc(label)}</h3><ul>{lis}</ul>'


def _prose_list(label: str, text: str | None) -> str:
    if not text:
        return ""
    return f'<h3>{esc(label)}</h3><p>{esc(text)}</p>'


def _timeline(rec: dict) -> str:
    ex = rec.get("editorExperience") or {}
    if not ex.get("applied"):
        return ('<section class="section"><div class="notice"><strong>🟡 Research only.</strong> '
                'BRYME has researched this opportunity but has not yet submitted to it. Nothing here should be read as '
                'a claim of acceptance, publication or payment.</div></section>')
    stages = ex.get("stages") or {}
    labels = [
        ("pitch_submitted", "Pitch submitted"), ("response_received", "Editor responded"),
        ("accepted", "Pitch accepted"), ("article_submitted", "Article submitted"),
        ("scheduled_for_publication", "Scheduled / published"), ("published", "Published"),
        ("payment_confirmed", "Payment confirmed"), ("payment_received", "Payment received"),
    ]
    dots = []
    for key, label in labels:
        if stages.get(key):
            dots.append(f'<li class="tl-on"><span class="tl-dot"></span>{esc(label)}</li>')
    paid = bool(stages.get("payment_confirmed") or stages.get("payment_received"))
    status = (ex.get("status") or "submitted").replace("-", " ")
    return f'''<div class="timebox"><h3>BRYME experience</h3>
<p class="tl-status">Status (as recorded): <b>{esc(status.capitalize())}</b> · Payment: <b>{'Confirmed' if paid else 'Pending / Not confirmed'}</b></p>
<p class="tl-note">This is BRYME's own firsthand record. Payment is only marked confirmed once it actually lands — never assumed. Dates, where shown, are when each step happened.</p>
<ul class="tl">{''.join(dots)}</ul></div>'''


def pub_page(rec: dict) -> None:
    slug = rec["slug"]
    pay = rec.get("pay") or {}
    wc = rec.get("wordCount") or {}
    el = rec.get("eligibility") or {}
    resp = rec.get("response") or {}
    label, cls, _state = status_of(rec)
    what = rec.get("whatTheyWant") or []
    dont = rec.get("whatTheyDontWant") or []
    reqs = rec.get("requirements") or []
    how = rec.get("howToSubmit") or []
    topics = (rec.get("writingTypes") or [])
    topic_display = ", ".join(t.replace("-", " ").capitalize() for t in topics) or rec.get("writingTypeLabel") or "—"
    official = rec.get("officialUrl") or ""
    apply_url = rec.get("applyUrl") or ""
    apply_email = rec.get("applyEmail") or ""
    method = rec.get("applyMethod") or ""
    rights = rec.get("rights") or ""
    ai = rec.get("aiPolicy") or "not-stated"
    ai_display = {"no-ai": "No / restricted (reported)", "not-stated": "Not stated in the guideline",
                  "unknown": "Unknown", "allowed": "Allowed (per guideline)"}.get(ai, ai.replace("-", " ").capitalize())

    # Guides that connect to this publication (by shared topic keywords).
    keywords = set(rec.get("keywords") or [])
    guide_links = []
    for g in GUIDES:
        gk = set(g.get("topics") or [])
        if keywords & gk:
            guide_links.append(g)
    guide_links = guide_links[:3]
    guide_html = "".join(f'<a class="chip-card" href="/guides/{esc(g["slug"])}/"><b>📚</b><span>{esc(g["title"])}</span></a>' for g in guide_links)

    submit_block = f'''<h3>How to submit</h3><p><b>{esc(method or "See official guideline")}</b></p>
<p>Apply through the <strong>official</strong> channel below. BRYME only records submission destinations it has verified.</p>
<ul>
<li>Official guideline: {f'<a href="{esc(official)}">opens the publication guideline (new tab)</a>' if official else 'Not recorded'}</li>
<li>Submission: {f'<a href="{esc(apply_url)}">{esc(method or "open the submission page (new tab)")}</a>' if apply_url else esc(method or "See official guideline")}</li>
{f'<li>Submission email: {esc(apply_email)}</li>' if apply_email else ''}
</ul>
{_list('What the guideline asks you to prepare', how) if how else ''}
{f'''<div class="notice"><strong>Safety note.</strong> Never pay to submit your work. A legitimate publication does not ask writers to pay a fee or provide identity documents to be considered. If you are asked to, do not proceed.</div>''' if True else ''}'''

    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / <a href="/writing/">Writing opportunities</a> / {esc(rec['publication'])}</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(topic_display)}</p>
<h1>{esc(rec['publication'])}</h1>
<p>{esc(rec.get('excerpt') or rec.get('title') or '')}</p>
<p class="source-line">{status_badge(rec)} <span class="verify-badge {cls}">Verified {esc((rec.get('lastVerified') or TODAY)[:7])}</span> <span class="byline">Researched by <a href="/author/ibrahim-sodiq/">BRYME Editorial Desk</a>.</span></p>
</section>
<div class="wrap two-col"><div>{_facts(rec)}</div><div>{_timeline(rec)}</div></div>
<section class="section"><div class="prose">
<h2>What this publication wants</h2>
<p>This is BRYME's summary of the publication's focus — not a copy of their website. <em>Type of writing:</em> {esc(topic_display)}. <em>Official guideline:</em> {f'<a href="{esc(official)}">{esc(rec['publication'])} guidelines</a>' if official else 'See the official site below'}.</p>
{_list('Topics, themes and styles they look for', what) if what else ''}
{_list('Subjects they avoid', dont) if dont else ''}
{_list('Key requirements', reqs) if reqs else ''}
<h3>Who can submit</h3>
<p>{esc(el.get('summary') or 'See the official guideline.')}</p>
{f'<h3>Rights</h3><p>{esc(rights)}</p>' if rights else ''}
<h3>AI policy</h3><p>{esc(ai_display)}</p>
<h2>How to write for them</h2>
<p><b>Official requirement:</b> always follow the publication's own guideline exactly.</p>
<p><b>BRYME's practical advice:</b> write for the publication's audience, use a clear structure, keep paragraphs short, lead with a specific angle, and confirm the word count before submitting. These are practical suggestions — they are <em>not</em> the publication's official rules.</p>
<h2>How to pitch</h2>
<p>Where a pitch is required, this is the general pattern BRYME recommends — always adapt it to the publication's guideline.</p>
<ol class="steps">
<li>Research the publication and read several recent pieces.</li>
<li>Choose a specific idea that fits their beat and audience.</li>
<li>Write a concise subject line naming your idea.</li>
<li>Introduce yourself in one or two lines (who you are, where you publish).</li>
<li>Explain the proposed piece in a short paragraph — angle, structure, length.</li>
<li>Say why it fits this publication.</li>
<li>Include 2–3 relevant clips or links.</li>
<li>Close professionally and thank them for their time.</li>
<li>Send through the official channel only.</li>
</ol>
{submit_block}
<h2>What happens after submission</h2>
<p><b>Expected response:</b> {esc(resp.get('label') or 'Not stated — BRYME does not invent a response time.')}</p>
<p>If the publication does not state a response time, BRYME records that it is unknown. A follow-up is generally reasonable after a couple of weeks; if there is still no response, treat that as a likely non-acceptance rather than a rejection. Acceptance is normally communicated by the publication. If they accept, they will tell you exactly how to submit the final piece and, for most, how and when payment is made.</p>
{f'<div class="guide-grid">{guide_html}</div>' if guide_html else ''}
</div></section>
<section class="section"><div class="card-grid">
<a class="path-card" href="{esc(rec.get('officialUrl') or '/writing/')}"><span class="card-num">OFFICIAL</span><h3>Read the official guideline</h3><p>Open the publication's own page and confirm everything on this record before you pitch.</p><span class="card-link">Open →</span></a>
<a class="path-card" href="/guides/how-to-write-a-pitch/"><span class="card-num">GUIDE</span><h3>How to write a pitch</h3><p>A step-by-step structure for a pitch that a busy editor can act on.</p><span class="card-link">Open the guide →</span></a>
</div></section></div>'''

    desc = (rec.get("seoTitle") or f"{rec['publication']} writing submissions — BRYME research").split(" | ")[0]
    title = f"{desc} | BRYME"
    schema_data = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": f"{rec['publication']}: {rec.get('writingTypeLabel') or rec.get('title') or 'writing opportunity'}",
        "description": desc, "url": f"{BASE}/writing/{slug}/",
        "datePublished": (rec.get("publishedAt") or rec.get("lastVerified") or TODAY) + "T00:00:00+01:00",
        "dateModified": (rec.get("lastVerified") or TODAY) + "T00:00:00+01:00",
        "author": {"@type": "Person", "name": "BRYME Editorial Desk", "url": BASE + "/author/ibrahim-sodiq/"},
        "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
        "mainEntityOfPage": f"{BASE}/writing/{slug}/",
    }
    write(f"/writing/{slug}/", page_wf(title=title, description=desc, route=f"/writing/{slug}/",
                                      current="writing", body=body, schema_data=schema_data))


# ---------------------------------------------------------------------------
# Guides
# ---------------------------------------------------------------------------
GUIDES = [
    {"slug": "how-to-write-a-pitch", "title": "How to write a magazine pitch",
     "description": "The structure, subject line and clips that get a publication to say yes.",
     "topics": ["pitch", "essay", "magazine"], "toc": ["Know the publication", "Choose a specific idea",
     "Write a tight subject line", "Introduce yourself", "State the angle and structure", "Show you fit", "Attach clips", "Close well"],
     "body": "A pitch is a short letter that sells an idea before you write it. The single biggest mistake is pitching a vague topic; the second is not saying why it fits the publication.\n\n**Know the publication first.** Read three or four recent pieces. Note the length, the tone, whether they use personal essays or reported features, and what they explicitly do not publish.\n\n**Choose a specific idea, not a topic.** \u201cAn essay about my mother\u201d is a topic. \u201cAn essay about the one phrase my mother said that I have never been able to hear the same way again\u201d is an idea.\n\n**Write a subject line that names the idea.** Editors skim. Make the line say what the piece is.\n\n**Introduce yourself in one or two lines.** Who you are, where you have published, and a reason to trust you with this idea.\n\n**State the angle and the structure.** In a short paragraph: the argument or story, how it develops, and a rough word count. Give them a reason to say yes.\n\n**Show that you fit.** Explain briefly why this is the right publication for this piece.\n\n**Attach two or three clips.** Links are fine; a couple of strong, relevant pieces beat a long list.\n\n**Close professionally.** Thank them, say you are happy to adjust, and send through the official channel."},
    {"slug": "how-to-pitch-an-essay", "title": "How to pitch an essay",
     "description": "Adapt a pitch for personal essay and nonfiction markets.",
     "topics": ["essay", "pitch"], "toc": ["Personal essays need a voice", "Find the universal", "Be honest", "Match the word count", "Send the whole essay if asked"],
     "body": "Personal essays are the most personal kind of pitch, and the most misunderstood.\n\n**The idea must carry a voice, not just a story.** Something happened to you; what matters is the perspective you bring to it and what it says about something larger.\n\n**Find the universal in the specific.** A personal essay works when a reader who is not you can still recognise themselves in it.\n\n**Be honest.** Do not invent events or feelings. If you are pitching a real experience, it must be real.\n\n**Match the word count.** Essay markets are often strict about length. Check the guideline before you claim a length.\n\n**Some markets want the full essay.** Where the guideline says to send the complete piece rather than a pitch, follow that. Sending a pitch to a market that expects the full essay wastes everyone's time."},
    {"slug": "how-to-find-paid-writing-opportunities", "title": "How to find publications that pay writers",
     "description": "Where to look, how to judge legitimacy, and how to read a guidelines page.",
     "topics": ["opportunities", "finding", "legitimate"], "toc": ["Start with the bibliography", "Judge the pay", "Check the guideline", "Confirm it is current", "Keep records"],
     "body": "Finding publications that genuinely pay writers is about knowing where to look and how to filter out the ones that do not.\n\n**Start with BRYME's own research.** The writing opportunities hub is built from checking publications' own guidelines — pay, words, eligibility and submission method.\n\n**Judge the pay, not the promise.** Does the publication state a fee per piece or per word? Many are honest about this; ones that say \u201cpayment varies\u201d with no range need more care. BRYME never invents a rate.\n\n**Read the guidelines page.** This is the single most important step. It tells you the type of writing, the length, whether they want a pitch or the full piece, and their rights and AI policy.\n\n**Confirm it is current.** Publications close and reopen. Check the date, or reach out. BRYME shows the last verified date on every page.\n\n**Keep records.** Note the date you checked, the official URL, and what the guideline said. That is what makes verification possible."},
    {"slug": "how-to-submit-a-freelance-article", "title": "How to submit a freelance article",
     "description": "From reading the guidelines to sending the finished piece the right way.",
     "topics": ["submit", "article", "freelance"], "toc": ["Read the submission instructions", "Formatting and files", "Attachments and clips", "The submission channel", "Track and confirm"],
     "body": "Submitting a freelance article is where many writers stumble over boring details, and details matter.\n\n**Read the submission instructions to the end.** The guideline tells you whether they want a pitch or the full article, the word count, the format and the channel.\n\n**Format it the way they asked.** Some want a docx; some want text in an email; some use a form. Do not guess when the answer is in the guideline.\n\n**Attach exactly what is required.** A cover note or clips if asked. Do not add a long cover letter if they did not ask for one.\n\n**Use the official channel.** An email, a form, or a submission portal from the publication — never an invented address.\n\n**Track and confirm.** Note the date you sent it and, if you can, confirm receipt. If there is no stated response time, it is reasonable to follow up after a couple of weeks."},
    {"slug": "how-to-build-writing-samples", "title": "How to build writing samples",
     "description": "Create a small portfolio that gets editors to say yes.",
     "topics": ["samples", "portfolio", "portfolio"], "toc": ["Quality over quantity", "Write a few strong pieces", "Match each sample to the publication", "Self-publish where allowed", "Keep them linkable"],
     "body": "You do not need dozens of clips to get published — you need a handful of strong, relevant ones.\n\n**Quality over quantity.** Two or three sharp pieces beat a long list of weak ones.\n\n**Write a few strong pieces in the style you want.** If you want to write essays, write essays. If you want features, write features.\n\n**Match each sample to the publication.** When you pitch, send the clips most like the piece you want to write.\n\n**Publish where you can.** A personal blog or a free platform counts, provided the work is genuinely yours and well done. (Check the guidelines — some publications will not consider previously self-published work.)\n\n**Keep them linkable.** Live links are easier for an editor than files they have to download."},
    {"slug": "how-to-write-a-strong-query-letter", "title": "How to write a strong query letter",
     "description": "A concise query that gets attention for nonfiction and journalism.",
     "topics": ["query", "pitch", "journalism"], "toc": ["Lead with the idea", "Show the reporting you will do", "Give a clear angle", "State the length and deadline", "End with your credibility"],
     "body": "A query letter sells a nonfiction piece before it exists. It should make the editor want the story.\n\n**Lead with the idea.** First line: what the article is, in one sentence.\n\n**Show what you will report.** Who you will talk to, what you will investigate, and why you are the one to do it.\n\n**Give a clear angle.** Not \u201cwe should talk about X\u201d but \u201cthis piece argues / reveals / shows Y.\u201d\n\n**State the length and any deadline.** Tell the editor what you are proposing and how long it will take.\n\n**End with credibility.** A line on your experience and any publication credits."},
    {"slug": "how-to-find-international-writing-opportunities", "title": "How to find international writing opportunities",
     "description": "Find paid markets beyond your home country without falling for scams.",
     "topics": ["international", "opportunities", "remote"], "toc": ["Look for markets that welcome you", "Check the eligibility", "Understand exchange and tax", "Use only official channels", "Beware of upfront fees"],
     "body": "International opportunities can pay better, but they come with extra things to check.\n\n**Look for markets that explicitly welcome writers where you live.** BRYME records which publications are open to African and diaspora writers, and which are not.\n\n**Check the eligibility carefully.** \u201cInternational submissions welcome\u201d is not the same as \u201copen to writers in every country.\u201d Some markets restrict who can apply, and some are region-specific.\n\n**Understand pay and exchange.** A rate in dollars or euros is not automatically better once conversion and transfer costs are considered. Note the currency and how payment is made.\n\n**Use only official channels.** International submissions go through the publication's own guideline, form or email — never through a third party promising to pitch on your behalf.\n\n**Beware of anything asking you to pay.** A legitimate publication does not charge writers to be considered, and it does not promise publication for a fee."},
    {"slug": "how-african-writers-can-find-paid-publications", "title": "How African writers find paid publications",
     "description": "Find paid, legitimate markets that welcome African and diaspora writers.",
     "topics": ["african", "opportunities", "international"], "toc": ["Look for markets that name you", "Know the diaspora rules", "Watch the currency and transfer", "Use guidelines, not reposts", "Protect your work"],
     "body": "African writers have genuine options — the key is finding markets that actually welcome you and that pay.\n\n**Look for publications that name African and diaspora writers.** BRYME records eligibility explicitly, including whether a market is restricted to Africans or to the African diaspora.\n\n**Understand the diaspora rules carefully.** Some markets welcome Black African diasporas; others are restricted to African residents. Read the eligibility line, and BRYME shows it.\n\n**Watch the currency and how you will be paid.** A fee quoted in a foreign currency may take a while to reach you or cost you fees. Note both.\n\n**Use the guidelines, not reposts.** A third-party repost can be outdated or wrong. Confirm against the publication's own page.\n\n**Protect your work.** Send to official channels, keep a record of every submission and its date, and never pay to be published."},
    {"slug": "how-to-follow-up-on-a-writing-pitch", "title": "How to follow up on a writing pitch",
     "description": "When to wait, what to say, and how to treat silence.",
     "topics": ["follow-up", "pitch", "response"], "toc": ["Wait a reasonable time", "Keep it short", "Confirm you can try elsewhere", "Treat silence as a sign", "Move on without burning bridges"],
     "body": "Following up is normal, but it has to be done well.\n\n**Wait a reasonable time.** If the publication states a response window, respect it. A short, polite follow-up after a couple of weeks is reasonable.\n\n**Keep it short.** One or two lines: reference your pitch, ask if they had a chance to consider it, and offer to adjust.\n\n**Confirm you can pitch elsewhere.** Many markets appreciate knowing you are holding the idea for them. Make it easy for them to say yes.\n\n**Treat silence as a sign.** If there is no response after a follow-up or two, that is usually a no. BRYME does not invent response times — it records when they are not stated.\n\n**Move on without burning bridges.** Publications have small teams and big inboxes. A later, better pitch to the same market is fine."},
    {"slug": "how-long-should-you-wait-for-an-editor", "title": "How long should you wait for an editor?",
     "description": "A realistic approach to editor response times and silence.",
     "topics": ["response", "follow-up", "pitch"], "toc": ["Read the stated window", "The default two-week rule", "What silence usually means", "When to move on", "Keep the relationship"],
     "body": "There is no universal answer, but good practices help.\n\n**Read the stated window first.** If the guideline says \u201cwe reply within two weeks,\u201d respect that. BRYME records stated response times and flags when they are not stated.\n\n**The default patience rule.** If nothing is stated, a couple of weeks before a short follow-up is reasonable.\n\n**Understand what silence usually means.** No response is rarely a personal rejection — it is usually just a busy editor. But it is also not acceptance.\n\n**When to move on.** After a follow-up or two with no reply, politely treat it as a pass and pitch elsewhere.\n\n**Keep the relationship.** A brief, gracious note leaves the door open for a future pitch."},
    {"slug": "how-to-find-remote-writing-work", "title": "How to find remote writing work",
     "description": "Legitimate remote and freelance writing opportunities you can do from anywhere.",
     "topics": ["remote", "freelance", "opportunities"], "toc": ["Separate jobs from gigs", "Use legitimate marketplaces", "Check who is hiring", "Beware of unpaid trials", "Verify before you commit"],
     "body": "Remote writing work spans two very different things: ongoing freelance contracts and one-off paid publications.\n\n**Separate jobs from gigs.** A paid publication call is not a job offer and not a promise of payment; a remote freelance contract is ongoing work. BRYME keeps them apart.\n\n**Use legitimate marketplaces and the publication's own channel.** For publication work, use the guideline. For freelance gigs, use reputable platforms — and read the terms carefully.\n\n**Check who is actually hiring.** A real remote role names a client or an agency. Vague \u201cwe need writers\u201d posts with no company need care.\n\n**Beware of unpaid trials.** A limited, clearly-scoped paid trial is one thing; a long \u201ctest\u201d you are expected to do for free is a red flag.\n\n**Verify before you commit.** Confirm the client, the pay, and how you will be paid. BRYME never invents a rate or a deadline."},
    {"slug": "how-to-get-your-first-paid-writing-gig", "title": "How to get your first paid writing gig",
     "description": "A starting path from writing samples to your first accepted, paid piece.",
     "topics": ["first", "gig", "paid"], "toc": ["Write first, publish somewhere", "Pick a small, reachable target", "Pitch one specific idea", "Send under the official channel", "Treat rejection as data"],
     "body": "The first paid gig is usually small — the point is to get on the board.\n\n**Write first.** You need something to show. Write a couple of strong pieces and publish them somewhere (a blog, a platform, or a publication that accepts your work).\n\n**Pick a small, reachable target.** Aim at a modest market that publishes work like yours and that you can genuinely match. BRYME lists many such markets with their pay and word counts.\n\n**Pitch one specific idea.** Not a general capability, but one angle for one publication.\n\n**Use the official channel.** An unfamiliar or invented submission address is how opportunities go wrong.\n\n**Treat rejection as data.** Editors are busy. A pass on one pitch is not a verdict on you as a writer. Note what the market wanted and keep going."},
]


def guides_hub() -> None:
    cards = "".join(f'<a class="guide-card" href="/guides/{esc(g["slug"])}/"><span class="card-num">GUIDE</span><h2>{esc(g["title"])}</h2><p>{esc(g["description"])}</p><span class="card-link">Open the guide →</span></a>' for g in GUIDES)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Writing guides</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Learn the craft</p>
<h1>Writing guides.</h1>
<p>Practical, writer-first resources on pitching, submitting, building samples and getting paid. Each guide connects to the relevant writing opportunities.</p></section>
<section class="section alt"><div class="guide-grid">{cards}</div></section></div>'''
    write("/guides/", page_wf(title="Writing guides for pitching, submitting and getting paid | BRYME",
                             description="Practical BRYME writing guides on pitching publications, submitting articles, building samples and getting paid for freelance work.",
                             route="/guides/", current="guides", body=body,
                             schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME writing guides", "url": BASE + "/guides/", "dateModified": TODAY, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


def guide_page(g: dict) -> None:
    toc = "".join(f'<li>{esc(t)}</li>' for t in g.get("toc", []))
    markdown = g["body"]
    # Render the small markdown subset used above (**bold**, blank-line paragraphs, - lists).
    paras = []
    for block in markdown.split("\n\n"):
        b = block.strip()
        if not b:
            continue
        if b.startswith("- "):
            lis = "".join(f"<li>{esc(x.strip())}</li>" for x in b.split("\n") if x.strip().startswith("- "))
            paras.append(f"<ul>{lis}</ul>")
        else:
            parts = b.split("\n")
            body_txt = " ".join(p.strip() for p in parts)
            # inline **bold**
            import re
            body_txt = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", body_txt)
            paras.append(f"<p>{body_txt}</p>")
    sections = "".join(paras)
    # Related publications by topic.
    gk = set(g.get("topics", []))
    related = [r for r in WRITING if gk & set(r.get("keywords", []))][:4]
    rel_cards = "".join(f'<a class="chip-card" href="/writing/{esc(r["slug"])}/"><b>✎</b><span>{esc(r["publication"])}</span></a>' for r in related)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / <a href="/guides/">Guides</a> / {esc(g["title"])}</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Writing guide</p>
<h1>{esc(g["title"])}</h1>
<p>{esc(g["description"])}</p>
<p class="byline">Researched and written by <a href="/author/ibrahim-sodiq/">BRYME Editorial Desk</a>.</p></section>
<section class="section"><div class="prose"><nav class="guide-toc"><b>In this guide</b><ol>{toc}</ol></nav>{sections}
{f'<h2>Related publications</h2><div class="guide-grid">{rel_cards}</div>' if rel_cards else ''}</div></section></div>'''
    write(f"/guides/{g['slug']}/", page_wf(title=f"{g['title']} | BRYME writing guides",
                                          description=g["description"], route=f"/guides/{g['slug']}/",
                                          current="guides", body=body,
                                          schema_data={"@context": "https://schema.org", "@type": "Article",
                                                       "headline": g["title"], "description": g["description"],
                                                       "url": f"{BASE}/guides/{g['slug']}/",
                                                       "datePublished": TODAY + "T00:00:00+01:00", "dateModified": TODAY + "T00:00:00+01:00",
                                                       "author": {"@type": "Person", "name": "BRYME Editorial Desk", "url": BASE + "/author/ibrahim-sodiq/"},
                                                       "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"},
                                                       "mainEntityOfPage": f"{BASE}/guides/{g['slug']}/"}))


# ---------------------------------------------------------------------------
# /tested/ index
# ---------------------------------------------------------------------------
def tested_page() -> None:
    tested = [r for r in WRITING if (r.get("editorExperience") or {}).get("applied")]
    rows = ""
    if tested:
        for r in tested:
            ex = r.get("editorExperience") or {}
            st = ex.get("status")
            rows += f'<tr><td>{esc(r["publication"])}</td><td><b>{esc((st or "submitted").replace("-", " ").capitalize())}</b></td><td>{"Confirmed" if (ex.get("stages") or {}).get("payment_confirmed") else "Pending"}</td><td><a href="/writing/{esc(r["slug"])}/">View →</a></td></tr>'
        table = f'<table class="pub-table"><thead><tr><th>Publication</th><th>BRYME status</th><th>Payment</th><th>Page</th></tr></thead><tbody>{rows}</tbody></table>'
    else:
        table = '<p>BRYME has not yet submitted to any opportunity. When it does, this page will show the complete, honest record.</p>'
    statuses = [("🟡", "Research only"), ("🔵", "Submitted"), ("🟢", "Accepted"),
                ("📖", "Published"), ("💰", "Paid"), ("🔴", "Rejected"), ("⚪", "Closed")]
    legend = "".join(f'<div class="trust-item"><span class="trust-icon">{e}</span>{lab}</div>' for e, lab in statuses)
    body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / BRYME Tested</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Firsthand verification</p>
<h1>BRYME Tested.</h1>
<p>Opportunities BRYME has personally researched, submitted to, been accepted by, published with, or been paid by. The record is shown as it happens — and payment is only ever marked confirmed once it actually lands.</p></section>
<section class="section"><div class="trust-grid">{legend}</div></section>
<section class="section alt"><div class="section-head"><div><p class="eyebrow">Current notes</p><h2>{len(tested)} opportunity·tested</h2></div></div>{table}</section></div>'''
    write("/tested/", page_wf(title="BRYME Tested — opportunities personally verified | BRYME",
                             description="Writing opportunities BRYME has personally submitted to, been accepted by, published with, or been paid by — shown as a staggered, honest record.",
                             route="/tested/", current="tested", body=body,
                             schema_data={"@context": "https://schema.org", "@type": "CollectionPage", "name": "BRYME Tested", "url": BASE + "/tested/", "dateModified": TODAY, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))


# ---------------------------------------------------------------------------
# About + trust pages
# ---------------------------------------------------------------------------
def about_page() -> None:
    body = '''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / About</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>About BRYME</p>
<h1>BRYME helps writers get published and paid.</h1>
<p>BRYME is an independent, Lagos-based editorial project led by Ibrahim Sodiq. It researches legitimate writing opportunities — the pay, the word count, who they are open to, and the official guideline — and gives writers practical guides for pitching, submitting and getting published.</p></section>
<section class="section"><div class="prose">
<h2>What BRYME publishes now</h2>
<ul>
<li>Permanent pages for every researched publication, with the official guideline linked.</li>
<li>Writing guides on pitching, submitting, building samples and getting paid.</li>
<li>BRYME Tested — a firsthand record where BRYME has personally submitted, been accepted, published or paid.</li>
</ul>
<h2>How opportunities are researched &amp; verified</h2>
<p>BRYME checks a publication's <strong>own</strong> guidelines page, records what it actually says about pay, word count, eligibility, submission method, rights and AI policy, and shows the date it was last verified. A listing is an invitation to pitch — it is not a job offer, and it is not a promise of payment.</p>
<h2>What BRYME will not do</h2>
<ul>
<li>It will not invent a rate, a deadline, an email or a submission URL.</li>
<li>It will not mark an opportunity as paid unless payment was actually confirmed.</li>
<li>It will not present BRYME's practical advice as an official publication requirement.</li>
</ul>
<h2>Who is accountable</h2>
<p>BRYME is created and edited by <a href="/author/ibrahim-sodiq/">Ibrahim Sodiq</a>. Report factual, link or status errors through the <a href="/contact/">Contact page</a>; material changes are recorded in <a href="/corrections/">Corrections</a>.</p>
</div></section></div>'''
    schema_data = {"@context": "https://schema.org", "@type": "AboutPage", "name": "About BRYME", "url": BASE + "/about/",
                   "dateModified": TODAY, "mainEntity": {"@type": "Organization", "name": "BRYME", "url": BASE + "/",
                   "founder": {"@type": "Person", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/"}}}
    write("/about/", page_wf(title="About BRYME | Writing research, guides and verification",
                             description="BRYME is an independent platform for writers — it researches legitimate paid writing opportunities and gives practical guides for getting published.",
                             route="/about/", current="about", body=body, schema_data=schema_data))


def empty_pages() -> None:
    trust = [
        ("/editorial-policy/", "Editorial policy", "Trust standard",
         "BRYME's rules for sources, authorship, dates, verification, automation, opinion, advertising and corrections."),
        ("/privacy/", "Privacy", "Privacy", "How BRYME handles personal information, analytics and third-party services."),
        ("/terms/", "Terms of use", "Terms of use", "Terms for using BRYME's editorial information and original content."),
        ("/disclaimer/", "Disclaimer", "Important limits", "BRYME's limits: no guarantee of acceptance, publication or payment; verify independently."),
        ("/corrections/", "Corrections", "Corrections", "BRYME's public record of material corrections to publications, sources and statuses."),
        ("/copyright/", "Copyright and source use", "Rights", "Copyright, attribution and rights-contact information for BRYME."),
        ("/contact/", "Contact BRYME", "Contact the desk", "Report a correction, a broken source link, or a rights concern with evidence."),
    ]
    for route, title, kicker, ds in trust:
        key = route.strip("/")
        body = f'''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / {esc(title)}</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>{esc(kicker)}</p><h1>{esc(title)}.</h1><p>{esc(ds)}</p></section>
<section class="section"><div class="prose"><p>This page will be published on the writing-first BRYME platform. For now, the editorial standard is: sources first, no invented facts, no fabricated experience, and payment only recorded once confirmed.</p></div></section></div>'''
        write(route, page_wf(title=f"{title} | BRYME", description=ds, route=route, current="about", body=body,
                             schema_data={"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": BASE + route, "publisher": {"@type": "Organization", "name": "BRYME", "url": BASE + "/"}}))

    author_body = '''<div class="wrap"><nav class="breadcrumb"><a href="/">Home</a> / Author / Ibrahim Sodiq</nav>
<section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>Founder and editor</p><h1>Ibrahim Sodiq.</h1>
<p>Ibrahim leads BRYME's source checks, opportunity research and editorial standards from Lagos, Nigeria.</p></section>
<section class="section"><div class="prose"><p>BRYME now focuses on writing: legitimate paid writing opportunities, practical guides, and a firsthand record where BRYME has personally pitched, been accepted, published or paid.</p></div></section></div>'''
    write("/author/ibrahim-sodiq/", page_wf(title="Ibrahim Sodiq | BRYME founder and editor",
                                            description="About Ibrahim Sodiq, founder and editor of BRYME's writing opportunities and guides platform.",
                                            route="/author/ibrahim-sodiq/", current="about", body=author_body,
                                            schema_data={"@context": "https://schema.org", "@type": "ProfilePage", "name": "Ibrahim Sodiq", "url": BASE + "/author/ibrahim-sodiq/", "mainEntity": {"@type": "Person", "name": "Ibrahim Sodiq", "jobTitle": "Founder and editor of BRYME"}}))

    not_found = '''<div class="wrap"><section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>404 · Page not found</p>
<h1>This page is not part of the BRYME writing platform.</h1>
<p>BRYME is now focused on writing opportunities, writing guides and getting published. Use the sections below.</p>
<div class="actions"><a class="btn" href="/writing/">Writing opportunities</a><a class="btn secondary" href="/guides/">Writing guides</a><a class="btn secondary" href="/tested/">BRYME Tested</a></div></section></div>'''
    (ROOT / "404.html").write_text(page_wf(title="Page not found | BRYME", description="The requested BRYME page was not found.",
                                           route="/404.html", current="", body=not_found, robots="noindex,follow"), encoding="utf-8")
    print("wrote 404.html")

    gone = '''<div class="wrap"><section class="page-hero"><p class="kicker"><span class="kicker-dot"></span>410 · Moved to legacy</p>
<h1>The multi-niche BRYME content moved to the legacy archive.</h1>
<p>The old jobs, sports, entertainment, make-money and technology site is preserved on the <b>legacy-multiniche</b> branch. BRYME's main branch now focuses entirely on writing opportunities and guides.</p>
<div class="actions"><a class="btn" href="/writing/">Writing opportunities</a><a class="btn secondary" href="/guides/">Writing guides</a></div></section></div>'''
    (ROOT / "410.html").write_text(page_wf(title="Content moved to legacy archive | BRYME", description="The former multi-niche BRYME content moved to the legacy-multiniche branch.",
                                           route="/410.html", current="", body=gone, robots="noindex,follow"), encoding="utf-8")
    print("wrote 410.html")


if __name__ == "__main__":
    home()
    writing_hub()
    for r in WRITING:
        pub_page(r)
    guides_hub()
    for g in GUIDES:
        guide_page(g)
    tested_page()
    about_page()
    empty_pages()
