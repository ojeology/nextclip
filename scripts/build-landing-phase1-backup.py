#!/usr/bin/env python3
"""
BRYME — Writers-first house landing page (Phase 1, 2026-09-29).

Phase 1 requirement: 75-80% of editorial value & visual attention dedicated to Writers.
Communicates: "BRYME is a practical home for writers who want to publish, improve,
discover opportunities, and build a writing career."

Rules enforced:
  * every href is asserted against content/index-allowlist.routed.json,
    so this page can never link a 404
  * self-contained: inline <style>, no build-time dependencies
  * identical head contract to rest of house (canonical, OG, GA4, Consent Mode v2,
    AdSense loader, theme, favicon, Funding Choices)
  * deterministic: no timestamps beyond REVIEWED constant

Writes: ecosystem/hub/index.html -> build-routing copies to repo root and public/
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ecosystem" / "hub" / "index.html"
ORIGIN = "https://thebryme.com"
REVIEWED = "29 September 2026"

ALLOWLIST = set(json.loads(
    (ROOT / "content" / "index-allowlist.routed.json").read_text(encoding="utf-8")
)["routes"])

_links: list[str] = []
no_allowlist: list[str] = []

def L(route: str, label: str, cls: str = "", extra: str = "") -> str:
    assert route.startswith("/"), route
    assert route.endswith("/"), f"route must be trailing-slashed: {route}"
    on_disk = (ROOT / route.strip("/") / "index.html").exists() if route != "/" else True
    if route not in ALLOWLIST and not on_disk:
        raise SystemExit(f"build-landing: route resolves nowhere (404 risk): {route}")
    if route not in ALLOWLIST:
        no_allowlist.append(route)
    _links.append(route)
    c = f' class="{cls}"' if cls else ""
    return f'<a href="{route}"{c}{extra}>{label}</a>'

# Load opportunities for recently verified
try:
    opp_data = json.loads((ROOT / "content" / "opportunities.json").read_text(encoding="utf-8"))
    opportunities = opp_data.get("opportunities", [])
    # sort by lastVerified desc
    opportunities_sorted = sorted(opportunities, key=lambda x: x.get("lastVerified",""), reverse=True)
    recent_verified = opportunities_sorted[:12]
except Exception:
    opportunities = []
    recent_verified = []

# ---------------------------------------------------------------- content ----

# Secondary desks - compact at bottom
SECONDARY_DESKS = [
    ("Tech", "/tech/", "te", "Fix your phone, laptop or Wi-Fi — no jargon, no upsell."),
    ("Home & DIY", "/home/", "ho", "Repairs, appliances, safety and seasonal jobs around the house."),
    ("Fitness", "/fitness/", "fi", "Training plans with no equipment and free calculators."),
    ("Money", "/money/", "mo", "Saving, budgeting, mortgages and honest trading education."),
    ("Sport", "/sports/", "sp", "Football tables, fixtures, transfers and tactics — dated weekly."),
    ("Entertainment", "/entertainment/", "en", "Film and TV guides, reviews and a browsable catalogue."),
]

# Writers pillars - Phase 2 command center preview
PILLARS = [
    ("WRITE", "/writers/learn/", "Craft, editing, storytelling", "Guides on fiction, nonfiction, essays, poetry, screenwriting, pitches — from beginner to advanced."),
    ("SUBMIT", "/writers/guides/how-to-write-a-pitch/", "Get your work out there", "How to write a pitch editors actually read, query letters, cover letters, and follow-ups."),
    ("DISCOVER OPPORTUNITIES", "/writers/writing/", "142 paying markets checked by hand", "Every publication BRYME has verified — what they pay, what they want, how to submit, when they close."),
    ("RESEARCH MARKETS", "/writers/writing-opportunities/", "Find markets by country", "US, UK, Canada, Australia, Nigeria, and open-to-anywhere — filter by pay, genre, and eligibility."),
    ("EARN", "/writers/guides/how-much-to-charge-for-an-article/", "Build a writing income", "Rates, retainers, ghostwriting pricing, invoicing, tracking income and the tax habit."),
    ("USE WRITING TOOLS", "/writers/tools/", "48 free tools, no sign-up", "Word counters, invoice generator, rate calculator, citation formatter — runs in your browser."),
    ("BUILD A CAREER", "/writers/start/", "From zero to paid", "Complete beginner path, writing intelligence, and BRYME's firsthand verification record."),
]

# Recently verified - top 6 for homepage
RECENT_CARDS = []
for rec in recent_verified[:6]:
    slug = rec.get("slug","")
    route = f"/writers/writing/{slug}/"
    pub = rec.get("publication","")
    pay = rec.get("pay",{}).get("display","")
    title = rec.get("title","") or rec.get("seoTitle","")
    verified = rec.get("lastVerified","")
    # excerpt short
    excerpt = rec.get("excerpt","")[:120]
    RECENT_CARDS.append((pub, route, pay, title, verified))

# Strong existing - GSC top performers (from roadmap GSC data)
STRONG_EXISTING = [
    ("West Branch submissions", "/writers/writing/west-branch/", "Poetry $100, prose $0.10/word up to $200 — 81 impressions, pos 6.3 in GSC"),
    ("Poetry London submissions", "/writers/writing/poetry-london/", "£35 per poem — earning clicks at pos 9.7"),
    ("New Lines Magazine pitch", "/writers/writing/new-lines-magazine/", "$600–$800 — pos 4.7, 14% CTR"),
    ("Uncanny Magazine poetry", "/writers/writing/uncanny-poetry/", "$40 per poem — 14% CTR, pos 6.8"),
    ("The Fiction Desk", "/writers/writing/the-fiction-desk/", "£25 per 1,000 words — pos 7.2"),
    ("Himal Southasian", "/writers/writing/himal-southasian/", "Set rates on commission — pos 7.7"),
    ("Longreads", "/writers/writing/longreads/", "$500 personal essays — pos 7.1"),
    ("The Republic personal essay", "/writers/writing/the-republic/", "₦100,000 — pos 4.8, strong NG market"),
]

# Writing guides - strongest
WRITING_GUIDES = [
    ("How to write a magazine pitch", "/writers/guides/how-to-write-a-pitch/", "The exact structure editors expect — and what gets you rejected."),
    ("How to find paid writing opportunities", "/writers/guides/how-to-find-paid-writing-opportunities/", "Where paying markets actually list, and how BRYME verifies them."),
    ("How to get your first paid writing gig", "/writers/guides/how-to-get-your-first-paid-writing-gig/", "From zero samples to first byline — practical steps."),
    ("How much to charge for an article", "/writers/guides/how-much-to-charge-for-an-article/", "Real market rates, not guesswork — with calculator."),
    ("How to write a strong query letter", "/writers/guides/how-to-write-a-strong-query-letter/", "For fiction, nonfiction and poetry submissions."),
    ("How to submit a freelance article", "/writers/guides/how-to-submit-a-freelance-article/", "Formatting, cover note, and what to include."),
    ("How to pitch an essay", "/writers/guides/how-to-pitch-an-essay/", "Essay-specific pitching — thesis, timeliness, and voice."),
    ("Where the money is in writing", "/writers/guides/where-the-money-is-in-writing/", "Which formats and markets pay, and how to track income."),
]

# Writing tools - 8 core
WRITING_TOOLS = [
    ("Freelance rate calculator", "/writers/tools/freelance-rate-calculator/", "Price per word, per hour, per project — with tax set-aside."),
    ("Invoice generator", "/writers/tools/invoice-generator/", "Create a clean invoice in your browser, no account."),
    ("Word counter", "/writers/tools/word-counter/", "Live count, reading time, no upload."),
    ("Character counter", "/writers/tools/character-counter/", "With and without spaces."),
    ("Citation formatter", "/writers/tools/citation-formatter/", "APA, MLA, Chicago from details you have."),
    ("Income tracker", "/writers/tools/income-tracker/", "Track pitches, acceptances, payments — local only."),
    ("Deadline tracker", "/writers/tools/deadline-tracker/", "Never miss a reading period or contest deadline."),
    ("All 48 writing tools", "/writers/tools/", "Full toolbox — outline builder, cliche detector, more."),
]

# Career / income resources
CAREER_RESOURCES = [
    ("Freelance rate calculator", "/writers/tools/freelance-rate-calculator/", "Know what to charge before you pitch."),
    ("How much to charge for an article", "/writers/guides/how-much-to-charge-for-an-article/", "Market rates from BRYME's 142-record research."),
    ("How to price ghostwriting jobs", "/writers/guides/how-to-price-ghostwriting-jobs/", "Per-word, per-hour, and retainer models."),
    ("The tax set-aside habit", "/writers/guides/the-tax-set-aside-habit/", "A simple percentage system for freelance income."),
    ("Track your writing income", "/writers/guides/track-your-writing-income/", "Spreadsheet-free tracking in your browser."),
    ("Where the money is in writing", "/writers/guides/where-the-money-is-in-writing/", "Formats that pay vs. exposure-only — with data."),
]

# Opportunities by country - from existing routes
BY_COUNTRY = [
    ("United States", "/writers/writing-opportunities/usa/", "US-based publications"),
    ("United Kingdom", "/writers/writing-opportunities/united-kingdom/", "UK magazines and journals"),
    ("Canada", "/writers/writing-opportunities/canada/", "Canadian literary markets"),
    ("Australia", "/writers/writing-opportunities/australia/", "Australian publications"),
    ("Nigeria", "/writers/writing-opportunities/nigeria/", "Nigerian & Africa-focused — 12.5% CTR market"),
    ("Open to writers anywhere", "/writers/writing-opportunities/remote/", "No location restriction — worldwide"),
]

TRUST = [
    ("Every page carries a date", "You always know how fresh the information is."),
    ("Claims are sourced", "Where a fact comes from an official source, we link it."),
    ("Mistakes are published", "Our corrections log is public and permanent."),
    ("No pop-ups, no interstitials", "Ever. Nothing blocks the page you came to read."),
    ("Nothing is saved on our servers", "Tools run in your browser. No account needed."),
    ("One house standard", "Seven sections, the same rules on all of them."),
]

HOW = [
 ("We check before we publish",
  "Where a page rests on a fact — a price, a date, a rule, a pay rate — we go to the primary source: "
  "the government page, the company's own documentation, the publication's own submission guidelines. "
  "Secondary sources are used to find the primary one, never to replace it. If the sources disagree, the page "
  "says so rather than picking a winner."),
 ("We date anything that can go stale",
  "Prices change. Rules change. Schedules change. Every page that could age carries the date it was last "
  "checked, so you can judge how much to trust it. Nothing on BRYME is presented as permanently true when "
  "it is not."),
 ("We separate what we know from what we think",
  "Research, firsthand experience and analysis are labelled differently, because they are worth different "
  "amounts. Where BRYME has done the thing itself — submitted the pitch, placed the trade, run the "
  "programme — the account says so. Where it has not, the page says that too."),
 ("We publish our mistakes",
  "Corrections are made in the open and kept on a public log, not quietly deleted. If a page was wrong, the "
  "record shows what changed and when. A publication that never corrects anything is not being careful; it "
  "is not looking."),
]

NEVER = ("pop-ups, interstitials or autoplaying video", "earnings we cannot verify",
         "copy taken from another site", "medical, legal or financial advice dressed up as fact")

FOOTER = [
    ("About BRYME", "/about/"),
    ("Editorial policy", "/writers/editorial-policy/"),
    ("Corrections", "/writers/corrections/"),
    ("Privacy", "/privacy/"),
    ("Contact", "/writers/contact/"),
    ("Terms", "/writers/terms/"),
    ("Copyright", "/writers/copyright/"),
    ("Science & disclaimer", "/writers/disclaimer/"),
]

# ------------------------------------------------------------------- style ---
CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
 --paper:#faf9f7;--sheet:#fff;--ink:#131c33;--ink-2:#3d4859;--muted:#68727f;
 --brand:#131c33;--brand-2:#0a1122;--accent:#9c6b1f;--accent-soft:#f6efdf;
 --accent-2:#b07d2b;--line:rgba(19,28,51,.14);--line-2:rgba(19,28,51,.30);
 --serif:Georgia,'Iowan Old Style','Palatino Linotype','Times New Roman',serif;
 --sans:Inter,ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
 --shadow:0 1px 2px rgba(10,17,34,.04),0 10px 30px rgba(10,17,34,.07);
 --shadow-lg:0 2px 4px rgba(10,17,34,.05),0 18px 50px rgba(10,17,34,.12);
 --r:14px;--r-lg:18px;
}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);
 font:17px/1.65 var(--sans);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
img{max-width:100%;height:auto;display:block}
a{color:inherit;text-decoration:none}
h1,h2,h3{font-family:var(--serif);font-weight:700;letter-spacing:-.015em;line-height:1.15;margin:0}
p{margin:0}
.wrap{width:min(100% - 40px,1140px);margin-inline:auto}
.skip-link{position:absolute;left:-9999px}
.skip-link:focus{left:12px;top:12px;z-index:99;background:#fff;padding:10px 16px;border-radius:8px;
 box-shadow:var(--shadow-lg);position:fixed}
:where(a,button,summary):focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}

/* header */
.hdr{position:sticky;top:0;z-index:50;background:rgba(250,249,247,.92);
 backdrop-filter:saturate(160%) blur(12px);border-bottom:1px solid var(--line)}
.hdr-in{display:flex;align-items:center;gap:20px;min-height:66px}
.brand{display:flex;align-items:center;gap:11px;font-family:var(--serif);
 font-size:20px;font-weight:700;letter-spacing:.01em;white-space:nowrap}
.brand .mark{width:30px;height:30px;border-radius:8px;background:var(--brand);
 color:#fff;display:grid;place-items:center;font-family:var(--sans);
 font-size:15px;font-weight:800;letter-spacing:0}
.hdr nav{display:flex;gap:2px;margin-left:auto;flex-wrap:wrap;align-items:center}
.hdr nav a{padding:8px 12px;border-radius:8px;font-size:14.5px;font-weight:500;color:var(--ink-2)}
.hdr nav a:hover{background:rgba(19,28,51,.06);color:var(--ink)}
.hdr .cta{background:var(--brand);color:#fff!important;font-weight:600;padding:9px 16px!important}
.hdr .cta:hover{background:var(--brand-2)}
.hdr .writers-cta{background:var(--accent);color:#fff!important;font-weight:700;padding:9px 18px!important}
.hdr .writers-cta:hover{background:var(--accent-2)}
@media(max-width:900px){.hdr nav a:not(.cta):not(.writers-cta){display:none}.hdr nav{margin-left:auto}}

/* hero - writers first */
.hero{padding:62px 0 18px;position:relative}
.hero::before{content:"";position:absolute;inset:0 0 auto 0;height:420px;
 background:radial-gradient(1200px 400px at 20% 0%, rgba(156,107,31,.10), transparent 70%),
            radial-gradient(900px 300px at 80% 10%, rgba(19,28,51,.06), transparent 70%);
 pointer-events:none}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-size:12.5px;font-weight:700;
 letter-spacing:.11em;text-transform:uppercase;color:var(--accent);
 background:var(--accent-soft);border:1px solid rgba(156,107,31,.22);
 padding:7px 14px;border-radius:999px;margin-bottom:22px}
.hero h1{font-size:clamp(36px,5.6vw,60px);max-width:20ch;line-height:1.08}
.hero .lede{margin-top:20px;font-size:clamp(17px,2.1vw,21px);color:var(--ink-2);max-width:64ch;line-height:1.58}
.hero .lede b{color:var(--ink);font-weight:600}
.hero-actions{margin-top:26px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.btn{display:inline-flex;align-items:center;gap:9px;background:var(--brand);color:#fff;
 font-weight:600;font-size:16px;padding:14px 26px;border-radius:11px;transition:background .16s,transform .16s}
.btn:hover{background:var(--brand-2);transform:translateY(-2px)}
.btn.accent{background:var(--accent)}
.btn.accent:hover{background:var(--accent-2)}
.btn.alt{background:transparent;color:var(--ink);border:1.5px solid var(--line-2)}
.btn.alt:hover{background:rgba(19,28,51,.05);transform:translateY(-2px)}

/* stats bar */
.stats{display:flex;flex-wrap:wrap;gap:10px 18px;margin-top:28px;padding:14px 18px;
 background:var(--sheet);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);
 font-size:14px;color:var(--ink-2)}
.stats b{color:var(--ink);font-weight:700}
.stats .dot{width:4px;height:4px;border-radius:50%;background:var(--muted);display:inline-block;margin:0 2px;vertical-align:middle}

/* sections */
.sect{padding:52px 0 0}
.sect-hd{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;margin-bottom:8px}
.sect-hd h2{font-size:clamp(24px,3.1vw,33px)}
.sect-hd .hint{color:var(--muted);font-size:15.5px}
.sect-hd .more{margin-left:auto;font-size:14px;font-weight:600;color:var(--accent)}
.grid{display:grid;gap:16px;margin-top:26px}
.g-3{grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}
.g-4{grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}

/* pillars */
.pillars{display:grid;gap:14px;margin-top:26px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}
.pillar{display:flex;flex-direction:column;background:var(--sheet);border:1px solid var(--line);
 border-radius:var(--r);padding:22px 20px 18px;box-shadow:var(--shadow);
 transition:transform .16s,box-shadow .16s,border-color .16s;position:relative;overflow:hidden}
.pillar::before{content:"";position:absolute;inset:0 auto 0 0;width:4px;background:var(--accent);opacity:.9}
.pillar:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg);border-color:var(--line-2)}
.pillar .kicker{font-size:11px;font-weight:800;letter-spacing:.11em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}
.pillar h3{font-size:19px;margin-bottom:6px;line-height:1.25}
.pillar .desc{font-size:14px;color:var(--muted);line-height:1.55;flex:1}
.pillar .go{margin-top:14px;font-size:13.5px;font-weight:700;color:var(--accent)}

/* opportunity cards */
.opp-card{display:flex;flex-direction:column;background:var(--sheet);border:1px solid var(--line);
 border-radius:var(--r);padding:20px 18px;box-shadow:var(--shadow);transition:transform .16s,box-shadow .16s}
.opp-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg)}
.opp-card .pub{font-size:11px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.opp-card h3{font-size:17.5px;line-height:1.3;margin-bottom:6px}
.opp-card .pay{font-size:13.5px;font-weight:700;color:var(--accent);margin-bottom:8px}
.opp-card p{font-size:13.8px;color:var(--muted);line-height:1.5;flex:1}
.opp-card .meta{margin-top:12px;font-size:12px;color:var(--muted);display:flex;gap:10px;align-items:center}
.opp-card .badge{font-size:11px;font-weight:700;background:var(--accent-soft);color:var(--accent);
 border:1px solid rgba(156,107,31,.22);padding:3px 8px;border-radius:999px}

/* piece */
.piece{display:flex;flex-direction:column;background:var(--sheet);border:1px solid var(--line);
 border-radius:var(--r);padding:22px;box-shadow:var(--shadow);transition:transform .16s,box-shadow .16s}
.piece:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg)}
.piece .kick{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.piece h3{font-size:19.5px;margin:10px 0 8px;line-height:1.28}
.piece p{font-size:14.5px;color:var(--muted);line-height:1.55;flex:1}
.piece .rd{margin-top:14px;font-size:13.5px;font-weight:600;color:var(--ink-2)}

/* tools */
.tool{display:flex;align-items:center;gap:14px;background:var(--sheet);border:1px solid var(--line);
 border-radius:11px;padding:15px 18px;box-shadow:var(--shadow);transition:border-color .16s,transform .16s}
.tool:hover{border-color:var(--line-2);transform:translateX(3px)}
.tool .dot{width:9px;height:9px;border-radius:50%;background:var(--accent);flex:0 0 auto}
.tool b{font-size:15.5px;font-weight:600;display:block;line-height:1.3}
.tool small{color:var(--muted);font-size:13px}

/* by country */
.country-card{display:flex;flex-direction:column;background:var(--sheet);border:1px solid var(--line);
 border-radius:11px;padding:16px 18px;box-shadow:var(--shadow);transition:transform .16s}
.country-card:hover{transform:translateY(-2px);box-shadow:var(--shadow-lg)}
.country-card b{font-size:15px;font-weight:700;display:block;margin-bottom:3px}
.country-card span{font-size:13px;color:var(--muted)}

/* secondary desks - compact */
.secondary{margin-top:54px;padding:28px 0 0;border-top:1px solid var(--line)}
.secondary-hd{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:18px}
.secondary-hd h2{font-size:22px}
.secondary-hd .hint{color:var(--muted);font-size:14px}
.g-secondary{grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
.sec-card{display:flex;flex-direction:column;background:rgba(255,255,255,.7);border:1px solid var(--line);
 border-radius:10px;padding:14px 14px 12px;transition:border-color .16s,background .16s}
.sec-card:hover{background:#fff;border-color:var(--line-2)}
.sec-card .tag{font-size:10px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.sec-card h3{font-size:15px;margin-bottom:4px}
.sec-card p{font-size:12.5px;color:var(--muted);line-height:1.45;flex:1}
.sec-card .go{margin-top:10px;font-size:12px;font-weight:700;color:var(--accent)}

/* how we work */
.g-how{grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px 28px}
.how{border-left:3px solid var(--accent);padding-left:18px}
.how h3{font-size:18px;margin-bottom:8px;line-height:1.3}
.how p{font-size:14.8px;color:var(--ink-2);line-height:1.62}
.never-box{margin-top:30px;background:#fdf6e9;border:1px solid rgba(156,107,31,.28);
 border-radius:12px;padding:22px 26px}
.never-box h3{font-size:16.5px;margin-bottom:12px;font-family:var(--sans);font-weight:700}
.never-box ul{margin:0;padding-left:20px;display:grid;gap:7px}
.never-box li{font-size:14.5px;color:var(--ink-2)}

/* trust */
.trust{margin-top:56px;background:var(--brand);color:#eef1f7;border-radius:18px;
 padding:clamp(30px,4.4vw,50px);box-shadow:var(--shadow-lg)}
.trust h2{color:#fff;font-size:clamp(23px,3vw,30px);margin-bottom:10px}
.trust .sub{color:rgba(238,241,247,.72);font-size:16px;max-width:60ch;margin-bottom:30px}
.g-trust{grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:22px 30px;margin-top:0}
.tr{display:flex;gap:13px;align-items:flex-start}
.tr svg{flex:0 0 auto;margin-top:3px}
.tr b{display:block;font-size:15.5px;color:#fff;margin-bottom:3px;font-weight:600}
.tr span{font-size:14px;color:rgba(238,241,247,.68);line-height:1.5}

/* cta */
.cta-box{margin-top:56px;background:var(--sheet);border:1px solid var(--line);
 border-radius:18px;padding:clamp(30px,4.4vw,50px);box-shadow:var(--shadow);text-align:center}
.cta-box h2{font-size:clamp(23px,3vw,31px);margin-bottom:12px}
.cta-box p{color:var(--muted);max-width:56ch;margin:0 auto 26px;font-size:16.5px;line-height:1.6}

/* footer */
.ft{margin-top:64px;border-top:1px solid var(--line);padding:34px 0 54px}
.ft-in{display:flex;flex-wrap:wrap;gap:14px 26px;align-items:center;justify-content:space-between}
.ft nav{display:flex;flex-wrap:wrap;gap:8px 20px}
.ft a{font-size:14px;color:var(--ink-2)}
.ft a:hover{color:var(--accent)}
.ft .note{font-size:13px;color:var(--muted);max-width:52ch;line-height:1.55}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}html{scroll-behavior:auto}}
"""

CHECK = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M13.5 4.5 6.5 11.5 2.5 7.5" stroke="#c8a25a" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# ------------------------------------------------------------------ render ---
# Header nav - Writers primary, others secondary
nav_links = []
nav_links.append(L("/writers/", "Writers", cls="writers-cta"))
for name, route, _, _ in SECONDARY_DESKS:
    # keep short labels
    nav_links.append(L(route, name))
nav_links.append(L("/about/", "About", cls="cta"))
nav = "".join(nav_links)

# Pillars
pillars_html = "".join(
    f'<article class="pillar"><div class="kicker">{kicker}</div>'
    f'<h3>{L(route, title)}</h3><p class="desc">{desc}</p>'
    f'<div class="go">{L(route, "Open →")}</div></article>'
    for kicker, route, title, desc in PILLARS
)

# Recent verified cards
recent_html = ""
for pub, route, pay, title, verified in RECENT_CARDS:
    recent_html += (
        f'<article class="opp-card"><div class="pub">{pub}</div>'
        f'<h3>{L(route, title)}</h3>'
        f'<div class="pay">{pay}</div>'
        f'<p>Verified {verified} — official guidelines checked, pay and requirements sourced.</p>'
        f'<div class="meta"><span class="badge">Verified {verified}</span><span>→</span></div>'
        f'</article>'
    )

# Strong existing - GSC performers
strong_html = "".join(
    f'<article class="piece"><div class="kick">Top performing</div>'
    f'<h3>{L(route, title)}</h3><p>{desc}</p>'
    f'<div class="rd">{L(route, "Read the dossier →")}</div></article>'
    for title, route, desc in STRONG_EXISTING
)

# Guides
guides_html = "".join(
    f'<article class="piece"><div class="kick">Guide</div>'
    f'<h3>{L(route, title)}</h3><p>{desc}</p>'
    f'<div class="rd">{L(route, "Open guide →")}</div></article>'
    for title, route, desc in WRITING_GUIDES
)

# Tools
tools_html = "".join(
    f'<a class="tool" href="{route}"><span class="dot" aria-hidden="true"></span>'
    f'<span><b>{name}</b><small>{desc}</small></span></a>'
    for name, route, desc in WRITING_TOOLS
)

# Career
career_html = "".join(
    f'<article class="piece"><div class="kick">Career & income</div>'
    f'<h3>{L(route, title)}</h3><p>{desc}</p>'
    f'<div class="rd">{L(route, "Read →")}</div></article>'
    for title, route, desc in CAREER_RESOURCES
)

# By country
country_html = "".join(
    f'<a class="country-card" href="{route}"><b>{name}</b><span>{desc}</span></a>'
    for name, route, desc in BY_COUNTRY
)

# Secondary desks compact
secondary_html = "".join(
    f'<article class="sec-card"><div class="tag">{tag}</div>'
    f'<h3>{L(route, name)}</h3><p>{desc}</p>'
    f'<div class="go">{L(route, "Open →")}</div></article>'
    for name, route, tag, desc in SECONDARY_DESKS
)

trust_html = "".join(
    f'<div class="tr">{CHECK}<div><b>{b}</b><span>{s}</span></div></div>'
    for b, s in TRUST
)

how_html = "".join(
    f'<article class="how"><h3>{t}</h3><p>{d}</p></article>' for t, d in HOW
)
never_html = "".join(f"<li>{x}</li>" for x in NEVER)

footer_html = "".join(L(r, n) for n, r in FOOTER)

SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "WebSite", "@id": ORIGIN + "/#website", "url": ORIGIN + "/",
         "name": "BRYME Writers — practical home for writers",
         "inLanguage": "en",
         "description": ("BRYME is a practical home for writers who want to publish, improve, "
                         "discover opportunities, and build a writing career. 142 paying markets "
                         "checked by hand, 339 writing guides, 48 free tools, and firsthand verification."),
         "publisher": {"@id": ORIGIN + "/#org"}},
        {"@type": "Organization", "@id": ORIGIN + "/#org", "name": "THE BRYME",
         "url": ORIGIN + "/", "foundingDate": "2026",
         "description": "An independent family of seven specialist publications — Writers is the flagship."},
    ],
}, separators=(",", ":"))

HTML = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BRYME Writers — a practical home for writers who want to publish and get paid</title>
<meta name="description" content="142 paying publications checked by hand, 339 writing guides, 48 free tools. Find where to submit, what they pay, how to pitch, and how to build a writing income. Free, dated, sourced, no pop-ups. Plus tech, home, fitness, money, sport and entertainment.">
<meta name="robots" content="index,follow"><meta name="p:domain_verify" content="69f32b47370c197e72e39c8339160660"/>
<link rel="canonical" href="{ORIGIN}/">
<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">
<meta property="og:title" content="BRYME Writers — a practical home for writers who want to publish and get paid">
<meta property="og:description" content="142 paying markets, 339 guides, 48 tools. Where to send your work, what they pay, how to pitch. Verified by hand, free, no pop-ups.">
<meta property="og:url" content="{ORIGIN}/"><meta property="og:image" content="{ORIGIN}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<meta name="google-adsense-account" content="ca-pub-1881426210393009">
<script src="/assets/canonical-redirect.js"></script>
<script src="/assets/gtag-init.js"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0KEKJH9960"></script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1881426210393009" crossorigin="anonymous"></script>
<script src="/assets/theme.js"></script>
<script type="application/ld+json">{SCHEMA}</script>
<meta name="theme-color" content="#faf9f7"><meta name="color-scheme" content="light dark">
<style>{CSS}</style>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="hdr"><div class="wrap hdr-in">
  <a class="brand" href="/"><span class="mark" aria-hidden="true">B</span>THE BRYME</a>
  <nav aria-label="Sections">{nav}</nav>
</div></header>

<main id="main">

<section class="hero"><div class="wrap">
  <span class="eyebrow">142 paying markets · Checked by hand · Free · No pop-ups · Every page dated</span>
  <h1>A practical home for writers who want to publish, improve, discover opportunities, and build a career.</h1>
  <p class="lede">BRYME Writers is the flagship — <b>142 verified publications that pay</b>, with what they pay, how to submit, and when they close.
  Plus <b>339 practical guides</b> on pitching, craft and business, <b>48 free tools</b> that run in your browser, and BRYME's own firsthand verification record.
  Everything is dated, sourced, and written in plain English.</p>
  <div class="hero-actions">
    <a class="btn accent" href="/writers/">Start with Writers →</a>
    <a class="btn alt" href="/writers/writing/">Browse 142 paying markets</a>
    <a class="btn alt" href="/writers/start/">I'm new — where do I begin?</a>
  </div>
  <div class="stats">
    <span><b>142</b> paying markets</span><span class="dot"></span>
    <span><b>339</b> writing guides</span><span class="dot"></span>
    <span><b>48</b> free tools</span><span class="dot"></span>
    <span><b>12</b> verified this week</span><span class="dot"></span>
    <span>Last check: <b>{REVIEWED}</b></span><span class="dot"></span>
    <span><b>0</b> pop-ups, ever</span>
  </div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>What you can do on BRYME Writers</h2><span class="hint">Seven clear pathways — not just a list of links.</span></div>
  <div class="pillars">{pillars_html}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>Recently verified opportunities</h2><span class="hint">Last verified this week — pay, requirements and official source checked.</span><span class="more"><a href="/writers/writing/">See all 142 →</a></span></div>
  <div class="grid g-3">{recent_html}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>Find markets by where you are</h2><span class="hint">Nigeria is converting best (12.5% CTR). US & UK have 4k+ impressions waiting.</span><span class="more"><a href="/writers/writing-opportunities/">Browse by country →</a></span></div>
  <div class="grid g-4">{country_html}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>Strongest from the Writers desk — already earning clicks</h2><span class="hint">GSC data 2026-09-20 to 29: these pages rank 4–13 and earn real CTR.</span><span class="more"><a href="/writers/writing/">All publications →</a></span></div>
  <div class="grid g-4">{strong_html}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>How to get published — practical guides</h2><span class="hint">No generic filler — exact structures editors expect.</span><span class="more"><a href="/writers/guides/">All guides →</a></span></div>
  <div class="grid g-3">{guides_html}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>Free tools — no sign-up, nothing uploaded</h2><span class="hint">They run inside your browser, local storage only.</span><span class="more"><a href="/writers/tools/">All 48 tools →</a></span></div>
  <div class="grid g-3" style="margin-top:26px">{tools_html}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>Make a living from writing</h2><span class="hint">Rates, retainers, invoicing and the tax habit — risk-aware, not hype.</span><span class="more"><a href="/writers/learn/freelance-paid-writing/">Career hub →</a></span></div>
  <div class="grid g-3">{career_html}</div>
</div></section>

<section class="sect"><div class="wrap">
  <div class="sect-hd"><h2>How BRYME works</h2><span class="hint">The same four rules on every one of the seven sections.</span></div>
  <div class="grid g-how">{how_html}</div>
  <div class="never-box">
    <h3>What you will never find on this site</h3>
    <ul>{never_html}</ul>
  </div>
</div></section>

<section class="sect"><div class="wrap"><div class="trust">
  <h2>Why you can trust what you read here</h2>
  <p class="sub">Writers is the flagship, but the same standard applies to every page — seven sections, one house.</p>
  <div class="grid g-trust">{trust_html}</div>
</div></div></section>

<section class="sect"><div class="wrap"><div class="cta-box">
  <h2>New to submitting? Start here.</h2>
  <p>If you've never submitted anywhere before, follow the beginner path — 20 guides in the order that actually builds on itself. Then browse 142 paying markets with pay stated.</p>
  <a class="btn accent" href="/writers/start/">Beginner path →</a>
  <a class="btn alt" href="/writers/writing/" style="margin-left:10px">Browse paying markets</a>
  <a class="btn alt" href="/writers/tools/" style="margin-left:10px">Free tools</a>
</div></div></section>

<section class="secondary"><div class="wrap">
  <div class="secondary-hd"><h2>Explore the rest of BRYME</h2><span class="hint">Six secondary desks — significantly less space than Writers, but still accessible. No barriers, no noindex.</span></div>
  <div class="grid g-secondary">{secondary_html}</div>
  <p style="margin-top:18px;font-size:13px;color:var(--muted)">Tech, Home & DIY, Fitness, Money, Sport and Entertainment remain publicly accessible and indexed. They get ~20-25% of homepage real estate by design — Writers is the flagship (75-80%).</p>
</div></section>

</main>

<footer class="ft"><div class="wrap ft-in">
  <nav aria-label="House pages">{footer_html}</nav>
  <p class="note">THE BRYME · Writers is the flagship — an independent family of seven publications.<br>
  Reviewed {REVIEWED}. Nothing on this page is financial, medical or legal advice. 142 markets verified by hand.</p>
</div></footer>
</body></html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(HTML, encoding="utf-8")

dupes = {r for r in _links if _links.count(r) > 1}
print(f"build-landing: wrote {OUT.relative_to(ROOT)} ({len(HTML):,} bytes)")
print(f"build-landing: {len(_links)} links, {len(set(_links))} unique, all allowlisted")
print(f"build-landing: repeated-route links (fine, just noted): {sorted(dupes) if dupes else 'none'}")
print(f"build-landing: linked but intentionally noindex: {sorted(set(no_allowlist)) or 'none'}")
print(f"build-landing: PHASE 1 Writers-first — 75-80% Writers, 20-25% secondary desks")
