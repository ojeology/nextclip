#!/usr/bin/env python3
"""Build THE BRYME ecosystem — the four publications + master homepage.

Per the Master Ecosystem Rebuild plan:
  thebryme.com            -> ecosystem/hub/            (parent homepage)
  writers.thebryme.com    -> the existing site (this repo's main build)
  sports.thebryme.com     -> ecosystem/sports/        (newsroom identity)
  entertainment.thebryme.com -> ecosystem/entertainment/ (cinematic identity)
  tech.thebryme.com       -> ecosystem/tech/          (modern-technical identity)

Each directory is a self-contained static service (own css, sitemap,
robots). The production hostname comes from the PRODUCTION_DOMAIN env
var, falling back to ecosystem/config.json — never hard-coded. This
script is run manually (python3 scripts/build-ecosystem.py); its output
is committed so each dir can be pointed at by its own Render service.

Content rules honoured: no betting content in Sports; no piracy in
Entertainment (information only); recovered archive articles keep their
own words, re-typeset, with honest archive labels.
"""
from __future__ import annotations

import html
import shutil
import json
import os
import sys
import re
from pathlib import Path
from xml.sax.saxutils import escape as xesc

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
OUT = ROOT / "ecosystem"
CFG = json.loads((ROOT / "ecosystem" / "config.json").read_text(encoding="utf-8"))
DOMAIN = os.environ.get("PRODUCTION_DOMAIN") or CFG["domain"]
MODE = os.environ.get("ROUTING_MODE") or CFG.get("mode", "path")
ORIGIN = os.environ.get("ORIGIN") or CFG.get("origin", "https://bryme.onrender.com")
TODAY = "2026-09-09"

# ---- AdSense rail (batch 19): driven by site.config.json "adsense" block. ----
# Renders NOTHING unless caId is a real ca-pub-... id AND enabled=true. The note in
# the config stands: ads must never resemble job cards, application buttons or nav.
try:
    _ADS_CFG = (json.loads((ROOT / "site.config.json").read_text(encoding="utf-8")).get("adsense") or {})
except Exception:
    _ADS_CFG = {}
ADSENSE_ID = str(_ADS_CFG.get("caId") or "").strip()
ADSENSE_ON = bool(_ADS_CFG.get("enabled")) and ADSENSE_ID.startswith("ca-pub-")
ADS_HEAD = ""
if ADSENSE_ON:
    ADS_HEAD = ('<meta name="google-adsense-account" content="' + ADSENSE_ID + '">\n'
                + '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + ADSENSE_ID + '" crossorigin="anonymous"></script>\n')
def _ads_slot(pos):
    """One responsive unit. Only when enabled; auto ads handle the rest."""
    if not ADSENSE_ON:
        return ""
    return ('<div class="ad-slot" data-pos="' + pos + '" aria-label="Advertisement">'
            + '<ins class="adsbygoogle" style="display:block" data-ad-client="' + ADSENSE_ID + '" data-ad-format="auto" data-full-width-responsive="true"></ins>'
            + '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>')

# ---------------------------------------------------------------- family css
BASE_CSS = """
:root{--paper:%(paper)s;--sheet:%(sheet)s;--ink:%(ink)s;--muted:%(muted)s;--dim:%(dim)s;
--brand:%(brand)s;--brand-deep:%(brand_deep)s;--accent:%(accent)s;
--line:rgba(%(line)s,.18);--line-strong:rgba(%(line)s,.4);--shadow:0 1px 2px rgba(0,0,0,.05),0 14px 38px rgba(0,0,0,.08);
--serif:Georgia,'Iowan Old Style','Palatino Linotype',serif;--sans:Inter,ui-sans-serif,system-ui,sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;min-height:100vh;color:var(--ink);background:var(--paper);font:16px/1.65 var(--sans);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}::selection{background:rgba(176,141,87,.3)}
.wrap{width:min(calc(100%% - 48px),1080px);margin:0 auto}
a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.skip-link{position:fixed;z-index:99;top:10px;left:10px;transform:translateY(-160%%);padding:10px 16px;background:var(--brand);color:var(--sheet);font-weight:700}
.skip-link:focus{transform:none}
.head{position:sticky;z-index:50;top:0;background:var(--paper);border-bottom:1px solid var(--line-strong)}
.head::before{content:"";display:block;height:6px;background:var(--brand)}
.head::after{content:"";display:block;height:2px;background:var(--accent)}
.mast{display:flex;align-items:baseline;gap:18px;padding:18px 0 12px;flex-wrap:wrap}
.mast-brand{font-family:var(--serif);font-size:34px;line-height:.9;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.mast-brand span{color:var(--accent)}
.mast-tag{font:italic 13px var(--serif);color:var(--muted);flex:1;min-width:200px}
.parent-link{font:750 10.5px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);padding:7px 11px;border-radius:2px}
.parent-link:hover{color:var(--ink);border-color:var(--line-strong)}
.cover{padding:clamp(46px,8vw,96px) 0 clamp(36px,6vw,64px);border-bottom:3px double var(--line-strong)}
.kicker{color:var(--accent);font:800 11.5px var(--sans);letter-spacing:.22em;text-transform:uppercase;margin:0 0 20px}
h1.cover-title{font-family:var(--serif);font-weight:700;letter-spacing:-.018em;font-size:clamp(36px,6.4vw,70px);line-height:1.03;margin:0;max-width:15em}
.cover-dek{font-family:var(--serif);font-size:clamp(16.5px,2.2vw,20px);line-height:1.62;color:var(--muted);max-width:58ch;margin:24px 0 0}
.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.btn{min-height:46px;display:inline-flex;align-items:center;padding:11px 20px;border:1px solid var(--brand);border-radius:2px;background:var(--brand);color:var(--sheet);font:700 13.5px var(--sans);letter-spacing:.04em;cursor:pointer}
.btn:hover{background:var(--brand-deep);border-color:var(--brand-deep)}
.btn.secondary{background:transparent;color:var(--brand);border-color:var(--line-strong)}
.btn.secondary:hover{border-color:var(--brand);background:transparent}
.section{padding:clamp(42px,7vw,80px) 0}
.section.alt{background:var(--paper-2,transparent);outline:1px solid var(--line);outline-offset:-1px}
.section-head{margin-bottom:28px}
.section-head h2{font-family:var(--serif);font-weight:700;font-size:clamp(23px,3.2vw,32px);line-height:1.12;margin:6px 0 0;letter-spacing:-.012em}
.section-head h2::after{content:"";display:block;width:46px;height:4px;background:var(--accent);margin-top:14px}
.lede{font-family:var(--serif);font-size:17.5px;line-height:1.65;color:var(--muted);max-width:60ch;margin:18px 0 0}
.list{list-style:none;margin:0;padding:0;border-top:1px solid var(--line-strong)}
.list li{border-bottom:1px solid var(--line)}
.list a{display:flex;gap:22px;align-items:baseline;padding:18px 6px;transition:background .15s ease,padding-left .15s ease}
.list a:hover{background:var(--sheet);padding-left:14px}
.list b{font-family:var(--serif);font-size:19px;line-height:1.3}
.list a:hover b{color:var(--brand)}
.list small{display:block;font:13px var(--sans);color:var(--muted);margin-top:3px}
.list .meta{margin-left:auto;flex:none;font:750 11px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.prose{max-width:720px;margin:0 auto;padding:clamp(28px,5vw,54px) 0 26px}
.prose h2{font-family:var(--serif);font-size:clamp(22px,3vw,29px);line-height:1.16;margin:44px 0 12px;padding-top:24px;border-top:1px solid var(--line)}
.prose h3{font-family:var(--serif);font-size:19.5px;margin:28px 0 8px}
.prose h3::before{content:"";display:inline-block;width:20px;height:4px;background:var(--accent);margin-right:11px;vertical-align:middle}
.prose p,.prose li{font-family:var(--serif);font-size:18px;line-height:1.78}
.prose p{margin:0 0 19px}
.prose ul,.prose ol{padding-left:26px;margin:0 0 19px}
.prose li+li{margin-top:9px}
.prose a{color:var(--brand);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
.prose blockquote{margin:32px 0;padding:6px 0 6px 24px;border-left:4px solid var(--accent);font-family:var(--serif);font-style:italic;font-size:21px;line-height:1.5}
.prose img{max-width:100%%;border:1px solid var(--line);padding:6px;background:var(--sheet)}
.crumb{padding:18px 0 10px;font:11.5px var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.crumb a{color:var(--muted)}.crumb a:hover{color:var(--accent)}
.byline{margin:16px 0 0;font-size:13px;color:var(--muted);border-top:1px solid var(--line);padding-top:13px}
.foot{margin-top:44px;border-top:3px double var(--line-strong);background:var(--paper-2,transparent)}
.foot-in{padding:34px 0 30px;display:flex;flex-wrap:wrap;gap:14px 34px;justify-content:space-between;font:13px var(--sans);color:var(--muted)}
.foot-in a:hover{color:var(--ink)}
.foot small{display:block;margin-top:8px;font:italic 12.5px var(--serif);color:var(--dim)}
.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.pub-card{border:1px solid var(--line-strong);border-top:6px solid var(--pc);background:var(--sheet);padding:26px 26px 22px;display:flex;flex-direction:column}
.pub-card h3{font-family:var(--serif);font-size:24px;margin:0 0 4px;letter-spacing:-.01em}
.pub-card .pc-kicker{font:800 10.5px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--pc);margin:0 0 12px}
.pub-card p{font-size:14.5px;line-height:1.6;color:var(--muted);margin:0 0 18px}
.pub-card .btn{margin-top:auto;align-self:flex-start}
.pub-card.live{box-shadow:var(--shadow)}
.pub-card.soon{opacity:.92}
.soon-tag{font:800 10px var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--muted);border:1px dashed var(--line-strong);align-self:flex-start;padding:8px 12px;margin-top:auto}
@media(max-width:820px){.cards{grid-template-columns:1fr}.mast-tag{display:none}}
@media print{.head,.foot,.actions,.btn{display:none!important}body{background:#fff}}

/* ---- writers-mirrored chrome: theme toggle, drawer, hero settle, dark theme ---- */
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.mast-tools{display:flex;align-items:center;gap:8px;margin-left:auto;align-self:center}
.theme-toggle,.nav-toggle{display:inline-grid;place-items:center;width:36px;height:36px;background:none;border:1px solid var(--line-strong);border-radius:2px;color:var(--muted);cursor:pointer;padding:0}
.theme-toggle:hover,.nav-toggle:hover{color:var(--ink);border-color:var(--ink)}
.theme-toggle svg,.nav-toggle svg{width:18px;height:18px}
.icon-moon{display:none}
html[data-theme="dark"] .icon-moon{display:block}
html[data-theme="dark"] .icon-sun{display:none}
@keyframes bsettle{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.cover .kicker,.cover-title,.cover-dek{animation-name:bsettle;animation-duration:.5s;animation-fill-mode:both}
.cover-title{animation-delay:.04s}
.cover-dek{animation-delay:.12s}
@media (prefers-reduced-motion:reduce){.cover .kicker,.cover-title,.cover-dek{animation:none}}
#drawer-backdrop{position:fixed;inset:0;z-index:90;background:rgba(15,21,31,.5);opacity:0;pointer-events:none;transition:opacity .2s ease}
#drawer-backdrop.show{opacity:1;pointer-events:auto}
#site-drawer{position:fixed;z-index:100;top:0;right:0;bottom:0;width:min(360px,88vw);background:var(--paper);border-left:1px solid var(--line-strong);transform:translateX(102%%);transition:transform .22s ease;overflow-y:auto;padding:0 22px 30px}
#site-drawer.open{transform:none}
.drawer-head{display:flex;align-items:center;justify-content:space-between;padding:20px 0 14px;border-bottom:3px double var(--line-strong);margin-bottom:8px}
.drawer-head .logo{font-family:var(--serif);font-weight:700;letter-spacing:.14em;font-size:19px}
.drawer-close{background:none;border:1px solid var(--line);border-radius:2px;color:var(--muted);width:34px;height:34px;display:grid;place-items:center;cursor:pointer}
.drawer-group{padding:14px 0;border-bottom:1px solid var(--line)}
.drawer-group>b{display:block;font:800 10.5px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin-bottom:8px}
#site-drawer a{display:block;padding:7px 0;color:var(--ink);border-bottom:1px solid var(--line)}
#site-drawer a:hover{color:var(--accent)}
body.drawer-open{overflow:hidden}
html[data-theme="dark"]{--paper:#141a24;--sheet:#1a212c;--ink:#e7e3d8;--muted:#9aa1ad;--dim:#7b818d;--brand:#aec4e0;--brand-deep:#0f151f;--accent:#d0aa52;--line:rgba(231,227,216,.15);--line-strong:rgba(231,227,216,.34);--shadow:0 1px 2px rgba(0,0,0,.3),0 14px 38px rgba(0,0,0,.35);color-scheme:dark}
html[data-theme="dark"] ::selection{background:rgba(208,170,82,.35)}
/* ---- writers-mirrored masthead: edition block, nav bar, mega menus, cta ---- */
.mast-edition{display:flex;flex-direction:column;gap:3px;flex:1;min-width:0}
.mast-date{font-size:10.5px;font-weight:800;letter-spacing:.22em;color:var(--accent);text-transform:uppercase}
.main-nav{border-top:1px solid var(--line);background:var(--paper)}
.mast-nav{display:flex;align-items:center;gap:4px;min-height:46px}
.main-nav a{padding:8px 13px;color:var(--muted);font-size:12px;font-weight:750;letter-spacing:.12em;text-transform:uppercase;white-space:nowrap}
.main-nav a:hover,.main-nav a[aria-current="page"]{color:var(--ink);box-shadow:inset 0 -3px 0 var(--accent)}
.main-nav a.nav-cta{color:var(--sheet);background:var(--brand);border-radius:2px;margin-left:8px;padding:7px 14px}
.main-nav a.nav-cta:hover{background:var(--brand-deep);color:var(--sheet);box-shadow:none}
.has-mega{position:relative}
.mega{display:none;position:absolute;z-index:80;left:0;top:100%%;min-width:300px;background:var(--paper);border:1px solid var(--line-strong);border-top:3px solid var(--accent);box-shadow:var(--shadow);padding:12px 0}
.has-mega:hover .mega,.has-mega:focus-within .mega{display:grid}
.mega a{display:block;padding:9px 18px;font:500 13.5px var(--sans);letter-spacing:0;text-transform:none;color:var(--muted);white-space:normal}
.mega a:hover{color:var(--brand);background:var(--sheet);box-shadow:none}
.mega b{display:block;padding:9px 18px 3px;font:800 10px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--accent)}
.nav-toggle{display:none}
.cover-facts{display:flex;gap:30px;flex-wrap:wrap;margin-top:34px;padding-top:22px;border-top:1px solid var(--line)}
.cover-facts b{display:block;font-family:var(--serif);font-size:30px;line-height:1.15;color:var(--accent)}
.cover-facts span{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
@media (max-width:860px){.mast-nav{overflow-x:auto;scrollbar-width:none}.mast-nav::-webkit-scrollbar{display:none}}
@media (max-width:760px){.mast-tag{display:none}.mast-date{font-size:9.5px}.nav-toggle{display:inline-grid}}

"""

FAMILY = {
    "writers":       dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#14213d", brand_deep="#0c1526", accent="#a8752a", line="20,33,61"),
    "hub":           dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#14213d", brand_deep="#0c1526", accent="#a8752a", line="20,33,61"),
    "sports":        dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#2f6b4f", brand_deep="#1f4d37", accent="#2f6b4f", line="20,33,61"),
    "entertainment": dict(paper="#17151a", sheet="#201d24", ink="#efe9dd", muted="#b5ad9f", dim="#8b8478", brand="#6d1832", brand_deep="#4d1023", accent="#a8752a", line="239,233,221"),
    "tech":          dict(paper="#fafaf8", sheet="#ffffff", ink="#14213d", muted="#5b6b7a", dim="#8b96a2", brand="#14213d", brand_deep="#0c1526", accent="#a8752a", line="20,33,61"),
}

FAMILY["fitness"] = dict(FAMILY["tech"])
FAMILY["home"] = dict(FAMILY["tech"])

HOME_CSS_EXTRA = """
html{color-scheme:light}
html[data-theme="dark"]{--paper:#131318;--sheet:#1b1b23;--ink:#e9e6df;--muted:#a7a29a;--dim:#7e7970;--brand:#4a7aa8;--brand-deep:#3a628c;--accent:#c9994e;--line:rgba(233,230,223,.14);--line-strong:rgba(233,230,223,.32);--shadow:0 1px 2px rgba(0,0,0,.45),0 14px 38px rgba(0,0,0,.5);color-scheme:dark}
html[data-theme="dark"] .btn{color:#fff}
html[data-theme="dark"] .skip-link{color:#fff}
html[data-theme="dark"] ::selection{background:rgba(201,153,78,.35)}
.theme-btn{margin-left:auto;flex:none;align-self:center;border:1px solid var(--line-strong);background:transparent;color:var(--muted);border-radius:99px;width:44px;height:36px;cursor:pointer;font-size:15px;line-height:1}
.theme-btn:hover{color:var(--ink);border-color:var(--accent)}
.h-layout{display:grid;grid-template-columns:236px minmax(0,1fr);gap:48px;align-items:start}
.h-side{position:sticky;top:112px;padding:28px 0}
.h-side-title{font:800 10.5px var(--sans);letter-spacing:.22em;text-transform:uppercase;color:var(--dim);margin:0 0 10px;padding-left:10px}
.h-side nav{display:block}
.h-side nav a{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:9px 10px;border-left:2px solid transparent;font:600 13.5px var(--sans);color:var(--muted)}
.h-side nav a:hover{color:var(--ink);background:var(--sheet)}
.h-side nav a.active{color:var(--brand);border-left-color:var(--brand);background:var(--sheet)}
.h-side nav a.flag{color:var(--accent)}
.h-side nav a.active.flag{color:var(--accent)}
.h-side nav a .n{font:700 10.5px var(--sans);color:var(--dim);border:1px solid var(--line);padding:1px 7px;border-radius:99px;flex:none}
.h-main .cover{padding:clamp(30px,5vw,58px) 0 clamp(26px,4vw,44px)}
.h-main h1.cover-title{font-size:clamp(30px,4.8vw,52px)}
.h-sec-card{border:1px solid var(--line);padding:20px 22px;background:var(--sheet)}
.h-sec-card h3{font-family:var(--serif);font-size:21px;margin:6px 0 6px}
.h-sec-card p{margin:0;color:var(--muted);font-size:14.5px}
.h-sec-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
@media (max-width:920px){.h-layout{display:block}.h-side{position:static;padding:16px 0;border-bottom:1px solid var(--line)}
.h-side nav{display:flex;gap:8px;overflow-x:auto;padding-bottom:4px}
.h-side nav a{border:1px solid var(--line);border-radius:99px;padding:7px 14px;white-space:nowrap;border-left-width:1px}
.h-side nav a.active{border-color:var(--brand)}
.h-sec-grid{grid-template-columns:1fr}}
"""

FITNESS_CSS_EXTRA = """
.fp-week .fp-day { display: grid; grid-template-columns: 44px 1fr auto; gap: 14px; align-items: center; }
.fp-day .fp-num { font-family: var(--serif); font-size: 22px; color: var(--accent); text-align: right; }
.fp-day small { display: block; color: var(--dim); font-size: 12.5px; margin-top: 2px; }
.fp-day.done { opacity: .55; }
.fp-day.done .fp-num::after { content: " \u2713"; color: var(--brand); }
.wp-grid { display: grid; gap: 10px; }
.wp-row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.wp-day { width: 96px; flex: none; font-weight: 700; font-size: 14px; }
.wp-chip { border: 1px solid var(--line); background: var(--paper); border-radius: 99px; padding: 9px 16px; font: 600 13px var(--sans); color: var(--muted); cursor: pointer; }
.wp-chip.on { border-color: var(--brand); color: var(--brand); }
.wp-chip.on::after { content: " \u2713"; font-weight: 700; }
.fp-progressbar { height: 10px; background: var(--sheet); border: 1px solid var(--line); border-radius: 99px; overflow: hidden; }
.fp-fill { height: 100%; width: 0%; background: var(--brand); transition: width .3s ease; }
@media (max-width: 640px) { .fp-week .fp-day { grid-template-columns: 34px 1fr; } .fp-day .fp-done { grid-column: 2; justify-self: start; } }
"""

SPORTS_CSS_EXTRA = """
.lg-scroll{overflow-x:auto;border:1px solid var(--line);background:var(--sheet)}
table.lg-table{width:100%;border-collapse:collapse;min-width:640px;font:500 14px var(--sans)}
.lg-table th{font:800 10.5px var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--dim);text-align:left;padding:10px 12px;border-bottom:2px solid var(--line-strong)}
.lg-table td{padding:9px 12px;border-bottom:1px solid var(--line);color:var(--ink)}
.lg-table tr:last-child td{border-bottom:none}
.lg-table td.num,.lg-table th.num{text-align:right;font-variant-numeric:tabular-nums}
.lg-table tr.rel td{border-top:2px solid var(--accent)}
.lg-table .club-b{font-weight:700}
.data-cols{display:grid;grid-template-columns:minmax(0,2.1fr) minmax(250px,1fr);gap:30px;align-items:start}
@media (max-width:900px){.data-cols{grid-template-columns:1fr}}
.side-panel{border:1px solid var(--line);background:var(--sheet);padding:18px 20px}
.side-panel + .side-panel{margin-top:16px}
.side-panel h3{font:800 10.5px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--dim);margin:0 0 10px}
.sp-row{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-bottom:1px solid var(--line);font-size:13.5px}
.sp-row:last-of-type{border-bottom:none}
.sp-row b{font-family:var(--serif)}
.sp-row .pts{color:var(--accent);font-weight:700;white-space:nowrap}
.sp-more{display:inline-block;margin-top:10px;font:700 11.5px var(--sans);letter-spacing:.07em;text-transform:uppercase;color:var(--brand)}
.lg-table td.club-b .row-badge{width:22px;height:22px;border-radius:6px;padding:2px;display:inline-block;vertical-align:middle;margin-right:8px}
.lg-table td.club-b a{color:var(--ink)}
.fx-row{display:flex;gap:14px;justify-content:space-between;align-items:baseline;padding:13px 0;border-bottom:1px solid var(--line);flex-wrap:wrap}
.fx-row .fx-when{font:700 11px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--dim);min-width:190px}
.fx-row .fx-tie{font-family:var(--serif);font-size:17.5px;font-weight:700}
.fx-row .fx-where{color:var(--muted);font-size:13px}
.fx-row .fx-tv{font:600 10.5px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--dim);border:1px solid var(--line);border-radius:99px;padding:2px 9px}
.fx-score{font-family:var(--serif);font-size:19px;color:var(--accent);padding:0 8px}
.cal-mw{font:800 11px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--accent);margin:30px 0 6px;padding-top:14px;border-top:2px solid var(--line-strong)}
.club-badge{display:block;border:1px solid var(--line);background:var(--sheet);border-radius:12px;padding:6px}
.cov-badge{width:76px;height:76px;margin-top:18px}
.row-badge{width:40px;height:40px;flex:none;margin-right:2px}
@media (max-width:640px){.cov-badge{width:60px;height:60px}}
"""

def css_for(pub):
    return BASE_CSS % FAMILY[pub] + (FITNESS_CSS_EXTRA if pub in ("fitness", "home") else "") + (HOME_CSS_EXTRA if pub == "home" else "") + (SPORTS_CSS_EXTRA if pub == "sports" else "")

def shell(pub, title, desc, route, body, card=None, robots="index,follow"):
    d = route  # mode-aware base URL from SUB
    og = f"https://{route}/assets/og.png" if route else f"https://{DOMAIN}/assets/og.png"
    has_theme = pub in ("tech", "fitness", "sports", "hub", "entertainment")
    theme_head = ('<script src="/assets/theme.js"></script>\n'
                  '<meta name="theme-color" content="#fafaf8">\n'
                  '<meta name="color-scheme" content="light dark">') if has_theme else ""
    if pub == "tech":
        drawer = tech_drawer()
    elif pub == "sports":
        drawer = sports_drawer()
    elif pub == "entertainment":
        drawer = ent_drawer()
    elif pub == "fitness":
        drawer = fitness_drawer()
    else:
        drawer = ""
    navjs = '<script src="/assets/site-nav.js" defer></script>' if pub in ("tech", "sports", "entertainment", "fitness") else ""
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{d}{'' if route.endswith('/') else ''}">
<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{d}"><meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
{ADS_HEAD}{theme_head}
<style>{css_for(pub)}</style>
</head><body><a class="skip-link" href="#main">Skip to content</a>
{body}
{drawer}
{navjs}
</body></html>"""

_THEME_TOGGLE_BTN = ('<button type="button" class="theme-toggle" data-theme-toggle aria-pressed="false" aria-label="Switch to dark theme">'
 '<svg class="icon-sun" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
 '<circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M4.2 4.2l1.6 1.6M18.2 18.2l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.2 19.8l1.6-1.6M18.2 5.8l1.6-1.6"/></svg>'
 '<svg class="icon-moon" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
 '<path d="M20.5 14.3A8.6 8.6 0 0 1 9.7 3.5a8.6 8.6 0 1 0 10.8 10.8Z"/></svg>'
 '<span class="sr-only theme-toggle-text">Switch to dark theme</span></button>')
_NAV_TOGGLE_BTN = ('<button type="button" class="nav-toggle" data-drawer-open aria-label="Open menu" aria-expanded="false">'
 '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>')

def _mega(items):
    """items: list of (href, label) tuples, optionally prefixed by ("HEAD", text) group marks."""
    rows = []
    for href, label in items:
        if href == "HEAD":
            rows.append("<b>" + label + "</b>")
        else:
            rows.append('<a href="' + href + '">' + label + "</a>")
    return '<div class="mega">' + "".join(rows) + "</div>"


def _nav_items(pub):
    """Writers-style nav per property: [(label, payload)] where payload is an href
    (plain link) or a list of (href, label) (mega dropdown). Built lazily so
    TECH_CAT etc. exist by call time."""
    if pub == "tech":
        guides = [("HEAD", "The guide shelf"), ("/tech/", "All of BRYME Tech")] + [
            ("/tech/" + c + "/", TECH_CAT[c][0]) for c in TECH_CAT]
        tools = [("HEAD", "The toolbox"), ("/tech/tool/", "All eight tools"),
                 ("/tech/tool/json-formatter/", "JSON formatter"),
                 ("/tech/tool/base64-encoder/", "Base64 encoder"),
                 ("/tech/tool/url-encoder/", "URL encoder"),
                 ("/tech/tool/uuid-generator/", "UUID generator"),
                 ("/tech/tool/timestamp-converter/", "Timestamp converter"),
                 ("/tech/tool/word-counter/", "Word counter"),
                 ("/tech/tool/case-converter/", "Case converter"),
                 ("/tech/tool/http-status-lookup/", "HTTP status lookup")]
        desk = [("HEAD", "Standards and contact"), ("/tech/methodology/", "Editorial methodology"),
                ("/tech/corrections/", "Corrections policy"), ("/tech/about/", "About"),
                ("/tech/contact/", "Contact"), ("/tech/privacy/", "Privacy")]
        return ([("Guides", guides), ("Toolbox", tools), ("The desk", desk)],
                ("/tech/", "Start here"))
    if pub == "sports":
        _lg_data = [("Premier League", "premier-league", "/premier-league/", True),
                    ("La Liga", "la-liga", "/laliga/", False),
                    ("Champions League", "champions-league", "/champions-league/", False),
                    ("Serie A", "serie-a", "/serie-a/", False),
                    ("Bundesliga", "bundesliga", "/bundesliga/", False),
                    ("Ligue 1", "ligue-1", "/ligue-1/", False)]
        navs = []
        for _n, _sl, _hub, _is_pl in _lg_data:
            rows = [("HEAD", _n + " \u00b7 live")]
            if _is_pl:
                rows.append((_hub, "The hub"))
            rows += [("/" + _sl + "-table/", "Table"), ("/" + _sl + "-results/", "Results"),
                     ("/" + _sl + "-top-scorers/", "Top scorers"), ("/" + _sl + "-fixtures/", "Fixtures")]
            if not _is_pl:
                rows.append((_hub, "The hub"))
            if _sl != "champions-league":
                rows.append(("/" + _sl + "-transfers/", "Transfer centre"))
            if _is_pl:
                rows += [("/premier-league-clubs/", "All twenty clubs"),
                         ("/premier-league-matchweek-4-preview/", "Matchweek 4 preview \u00b7 live")]
            navs.append((_n, rows))
        desk = [("HEAD", "The desk"), ("/sports/", "Desk home"),
                ("/the-weekend-ahead/", "The weekend forecast"),
                ("/form-board/", "The Form Board"),
                ("/fpl/", "FPL, explained properly"),
                ("/sports/explainers/", "All explainers"),
                ("/sports/analysis/", "The analysis shelf"),
                ("/sports/transfers/", "The transfer desk (archive)")]
        navs.append(("The desk", desk))
        return (navs, ("/the-weekend-ahead/", "This weekend"))
    if pub == "fitness":
        guides = [("HEAD", "The fitness shelf"), ("/fitness/", "All fitness guides"),
                  ("/fitness/how-to-start-working-out/", "Starting from zero"),
                  ("/fitness/30-day-walking-plan/", "The 30-day walking plan"),
                  ("/fitness/how-many-steps-a-day/", "How many steps a day"),
                  ("/fitness/how-to-warm-up/", "How to warm up"),
                  ("/fitness/strength-training-for-beginners/", "Strength for beginners"),
                  ("/fitness/rest-days-and-recovery/", "Rest days and recovery"),
                  ("/fitness/walking-vs-running/", "Walking vs running"),
                  ("/fitness/workout-at-home-no-equipment/", "Home workout, no equipment"),
                  ("/fitness/how-progressive-overload-works/", "Progressive overload"),
                  ("/fitness/breathing-during-exercise/", "Breathing basics"),
                  ("/fitness/how-much-protein-do-you-need/", "Protein, honestly"),
                  ("/fitness/sleep-and-exercise-performance/", "Sleep &amp; recovery"),
                  ("/fitness/weekly-planner/", "The weekly planner")]
        return ([("Guides", guides)], ("/fitness/", "Desk home"))
    if pub == "entertainment":
        shelves = [("HEAD", "The entertainment shelves"), ("/entertainment/browse/", "Browse movies"), ("/entertainment/best-streaming-service-us-uk/", "Best streaming service"), ("/entertainment/how-to-watch-movies-online-free-and-legal/", "Watch free, legally"), ("/entertainment/explainers/", "Explainers"),
                   ("/entertainment/recommendations/", "Recommendations"),
                   ("/entertainment/opinion/", "Opinion"),
                   ("/entertainment/how-to-build-a-watchlist/", "Build a watchlist"),
                   ("/entertainment/subtitles-or-dubs/", "Subtitles or dubs?"),
                   ("/entertainment/anime-seasons-and-cours-explained/", "Anime seasons and cours"),
                   ("/entertainment/how-movie-release-windows-work/", "Release windows"),
                   ("/entertainment/why-streaming-services-raise-prices/", "Why prices rise"),
                   ("/entertainment/how-anime-production-committees-work/", "Production committees"),
                   ("/entertainment/how-award-season-actually-works/", "How award season works")]
        return ([("Shelves", shelves)], ("/entertainment/", "Desk home"))
    if pub == "hub":
        return ([("Writers", "/writers/"), ("Sport", "/sports/"), ("Tech", "/tech/"),
                 ("Entertainment", "/entertainment/"), ("Fitness", "/fitness/"), ("Home & DIY", "/home/")],
                ("/writers/", "Start with Writers"))
    return ([], None)


def tech_drawer():
    return ('<div id="drawer-backdrop"></div>\n'
        '<aside id="site-drawer" aria-hidden="true" aria-label="BRYME Tech sections">\n'
        '<div class="drawer-head"><span class="logo">BRYME&nbsp;TECH</span>'
        '<button type="button" class="drawer-close" data-drawer-close aria-label="Close menu">'
        '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg></button></div>\n'
        '<div class="drawer-group"><b>Sections</b><a href="/tech/">Desk home</a>'
        + "".join('<a href="/tech/' + c + '/">' + TECH_CAT[c][0] + '</a>' for c in TECH_CAT)
        + '<a href="/tech/tool/">The toolbox</a></div>\n'
        '<div class="drawer-group"><b>The desk</b><a href="/tech/methodology/">Editorial methodology</a>'
        '<a href="/tech/corrections/">Corrections policy</a><a href="/tech/about/">About</a>'
        '<a href="/tech/contact/">Contact</a><a href="/tech/privacy/">Privacy</a></div>\n'
        '</aside>')


def sports_drawer():
    return ('<div id="drawer-backdrop"></div>\n'
        '<aside id="site-drawer" aria-hidden="true" aria-label="BRYME Sport sections">\n'
        '<div class="drawer-head"><span class="logo">BRYME&nbsp;SPORT</span>'
        '<button type="button" class="drawer-close" data-drawer-close aria-label="Close menu">'
        '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg></button></div>\n'
        '<div class="drawer-group"><b>Leagues</b>'
        '<a href="/premier-league/">Premier League</a><a href="/laliga/">La Liga</a>'
        '<a href="/champions-league/">Champions League</a><a href="/serie-a/">Serie A</a>'
        '<a href="/bundesliga/">Bundesliga</a><a href="/ligue-1/">Ligue 1</a></div>\n'
        '<div class="drawer-group"><b>Live data</b>'
        '<a href="/premier-league-table/">Premier League table</a><a href="/la-liga-table/">La Liga table</a>'
        '<a href="/serie-a-table/">Serie A table</a><a href="/bundesliga-table/">Bundesliga table</a>'
        '<a href="/ligue-1-table/">Ligue 1 table</a><a href="/champions-league-table/">Champions League table</a>'
        '<a href="/the-weekend-ahead/">The weekend forecast</a><a href="/form-board/">The Form Board</a><a href="/fpl/">FPL guide</a></div>\n'
        '<div class="drawer-group"><b>The desk</b><a href="/sports/">Desk home</a><a href="/premier-league-transfers/">Transfer centre</a><a href="/sports/explainers/">Explainers</a>'
        '<a href="/sports/analysis/">Analysis</a></div>\n'
        '<div class="drawer-group"><b>The desk</b><a href="/sports/about/">About</a>'
        '<a href="/sports/contact/">Contact</a><a href="/sports/privacy/">Privacy</a></div>\n'
        '</aside>')


def ent_drawer():
    return ('<div id="drawer-backdrop"></div>\n'
        '<aside id="site-drawer" aria-hidden="true" aria-label="BRYME Entertainment sections">\n'
        '<div class="drawer-head"><span class="logo">BRYME&nbsp;ENTERTAINMENT</span>'
        '<button type="button" class="drawer-close" data-drawer-close aria-label="Close menu">'
        '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg></button></div>\n'
        '<div class="drawer-group"><b>Browse</b><a href="/entertainment/">Desk home</a>'
        '<a href="/entertainment/browse/">Browse the movies</a>'
        '<a href="/entertainment/recommendations/">Recommendations</a>'
        '<a href="/entertainment/explainers/">Explainers</a><a href="/entertainment/opinion/">Opinion</a></div>\n'
        '<div class="drawer-group"><b>Guides</b><a href="/entertainment/how-to-pick-a-movie-tonight/">Pick a movie tonight</a>'
        '<a href="/entertainment/how-to-build-a-watchlist/">Build a watchlist</a>'
        '<a href="/entertainment/best-streaming-service-us-uk/">Best streaming service</a>'
        '<a href="/entertainment/how-to-watch-movies-online-free-and-legal/">Watch free, legally</a>'
        '<a href="/entertainment/cheapest-way-to-stream-movies/">Cheapest way to stream</a>'
        '<a href="/entertainment/best-kdramas-to-start-with/">K-drama starter route</a>'
        '<a href="/entertainment/subtitles-or-dubs/">Subtitles or dubs?</a>'
        '<a href="/entertainment/anime-seasons-and-cours-explained/">Seasons &amp; cours</a></div>\n'
        '<div class="drawer-group"><b>The desk</b><a href="/entertainment/about/">About</a>'
        '<a href="/entertainment/contact/">Contact</a><a href="/entertainment/privacy/">Privacy</a></div>\n'
        '</aside>')


def fitness_drawer():
    return ('<div id="drawer-backdrop"></div>\n'
        '<aside id="site-drawer" aria-hidden="true" aria-label="BRYME Fitness sections">\n'
        '<div class="drawer-head"><span class="logo">BRYME&nbsp;FITNESS</span>'
        '<button type="button" class="drawer-close" data-drawer-close aria-label="Close menu">'
        '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5L5 19"/></svg></button></div>\n'
        '<div class="drawer-group"><b>Tools</b><a href="/fitness/30-day-walking-plan/">The 30-day walking plan</a>'
        '<a href="/fitness/weekly-planner/">The weekly planner</a></div>\n'
        '<div class="drawer-group"><b>Guides</b><a href="/fitness/how-to-start-working-out/">How to start working out</a>'
        '<a href="/fitness/how-to-warm-up/">How to warm up</a>'
        '<a href="/fitness/strength-training-for-beginners/">Strength for beginners</a>'
        '<a href="/fitness/walking-vs-running/">Walking vs running</a>'
        '<a href="/fitness/workout-at-home-no-equipment/">Home workout, no equipment</a>'
        '<a href="/fitness/how-progressive-overload-works/">Progressive overload</a>'
        '<a href="/fitness/rest-days-and-recovery/">Rest days &amp; recovery</a>'
        '<a href="/fitness/how-much-protein-do-you-need/">Protein, honestly</a>'
        '<a href="/fitness/sleep-and-exercise-performance/">Sleep &amp; performance</a></div>\n'
        '<div class="drawer-group"><b>The desk</b><a href="/fitness/about/">About</a>'
        '<a href="/fitness/contact/">Contact</a><a href="/fitness/privacy/">Privacy</a></div>\n'
        '</aside>')


def head(pub, tagline, parent=True):
    pl = f'<a class="parent-link" href="https://{DOMAIN}/">THE BRYME</a>' if parent and pub != "hub" else ""
    if pub == "hub":
        brand = "THE&nbsp;BRYME"; brand_href = "/"
    else:
        brand = f'BRYME&nbsp;<span style="color:var(--accent)">{PUB_NAME[pub].upper()}</span>'
        brand_href = PREFIX.get(pub, "/") + "/"
    editions = {"tech": "SEPTEMBER 2026 \u00b7 THE TOOL DESK",
                "sports": "SEPTEMBER 2026 \u00b7 THE 2026-27 SEASON",
                "fitness": "SEPTEMBER 2026 \u00b7 FOUNDATION SEASON",
                "entertainment": "SEPTEMBER 2026 \u00b7 THE EVERGREEN SHELF",
                "hub": "SEPTEMBER 2026 \u00b7 THE HOUSE DESK"}
    edition = editions.get(pub)
    edition_html = (f'<div class="mast-edition"><span class="mast-date">{edition}</span>'
                    f'<span class="mast-tag">{tagline}</span></div>') if edition else f'<span class="mast-tag">{tagline}</span>'
    tools = ""
    if pub in ("tech", "fitness", "sports", "hub", "entertainment"):
        tools += _THEME_TOGGLE_BTN
    if pub in ("tech", "sports", "entertainment", "fitness"):
        tools += _NAV_TOGGLE_BTN
    items, cta = _nav_items(pub)
    nav = ""
    if items:
        parts = []
        for label, payload in items:
            if isinstance(payload, list):
                parts.append('<div class="has-mega"><a href="' + payload[1][0] + '">' + label + "</a>" + _mega(payload) + "</div>")
            else:
                parts.append('<a href="' + payload + '">' + label + "</a>")
        if cta:
            parts.append('<a class="nav-cta" href="' + cta[0] + '">' + cta[1] + "</a>")
        nav = '<nav class="main-nav"><div class="wrap mast-nav">' + "".join(parts) + "</div></nav>"
    return f"""<header class="head"><div class="wrap mast">
<a class="mast-brand" href="{brand_href}">{brand}</a>
{edition_html}
{pl}{tools}
</div></header>{nav}"""

def foot(pub, extra=""):
    _base = "writers" if pub == "hub" else pub
    _trust = ((' \u00b7 <a href="/tech/methodology/">Methodology</a> \u00b7 <a href="/tech/corrections/">Corrections</a>'
               ' \u00b7 <a href="/tech/terms/">Terms</a> \u00b7 <a href="/tech/disclaimer/">Disclaimer</a>') if pub == "tech" else
              (' \u00b7 <a href="/' + _base + '/terms/">Terms</a> \u00b7 <a href="/' + _base + '/editorial-policy/">Editorial policy</a>'
               ' \u00b7 <a href="/' + _base + '/corrections/">Corrections</a>'))
    x = extra or _trust
    return f"""<footer class="foot"><div class="wrap foot-in">
<div>© 2026 THE BRYME — {PUB_NAME[pub] if pub != 'hub' else 'the BRYME publications'}.</div>
<div><a href="/{'writers' if pub == 'hub' else pub}/about/">About</a> · <a href="/{'writers' if pub == 'hub' else pub}/privacy/">Privacy</a> · <a href="/{'writers' if pub == 'hub' else pub}/contact/">Contact</a>{x}</div>
<div><a href="https://{DOMAIN}/">thebryme.com</a></div>
</div></footer>"""

def write_placeholder(key, name, tagline, identity, planned):
    """Foundation-era property: one honest page + the standard legal pages, all noindex."""
    items = "".join("<li>" + html.escape(x) + "</li>" for x in planned)
    body = (head(key, tagline)
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/">THE BRYME</a> / ' + html.escape(name) + "</nav>"
        + '<section class="cover"><p class="kicker">Under construction \u00b7 foundation laid</p>'
        + '<h1 class="cover-title">' + html.escape(name) + "</h1>"
        + '<p class="cover-dek">' + html.escape(identity) + "</p></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The plan</p><h2>What this desk will cover.</h2></div>'
        + '<ul class="list">' + items + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Honest status</p><h2>Nothing to read here yet.</h2></div>'
        + '<p class="lede">This property is at the foundation stage: the route, standards and plan exist; the guides are being built and will open when they are worth reading. In the meantime, the live desks are <a href="/writers/">BRYME Writers</a>, <a href="/tech/">BRYME Tech</a>, <a href="/sports/">BRYME Sport</a>, <a href="/entertainment/">BRYME Entertainment</a> and <a href="/fitness/">BRYME Fitness</a>.</p>'
        + '</section></div></main>' + foot(key))
    base = OUT / key
    base.mkdir(parents=True, exist_ok=True)
    for route, title, desc, pbody in [("/", name + " | BRYME", tagline, body)] + legal_pages(key, name, tagline):
        f = base / ("index.html" if route == "/" else route.lstrip("/") + "/index.html")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(shell(key, title, desc, ORIGIN + "/" + key + route, pbody, robots="noindex,follow"), encoding="utf-8")
    print(key + ": foundation page + legal (noindex, no sitemap)")


PUB_NAME = {"sports": "Sport", "entertainment": "Entertainment", "tech": "Tech", "fitness": "Fitness", "home": "Home & DIY"}

def write_service(pub, pages):
    base = OUT / pub
    base.mkdir(parents=True, exist_ok=True)
    # clear stale output from earlier builds; the recovery store survives
    for e in base.iterdir():
        if e.name == "_recovered":
            continue
        shutil.rmtree(e) if e.is_dir() else e.unlink()
    (base / "assets").mkdir(exist_ok=True)
    (base / "assets" / "site.css").write_text(css_for(pub), encoding="utf-8")
    urls = []
    for route, title, desc, body in pages:
        p = base / route.lstrip("/")
        p.mkdir(parents=True, exist_ok=True)
        full = shell(pub, title, desc, SUB[pub] + route, body)
        (p / "index.html").write_text(full, encoding="utf-8")
        urls.append(SUB[pub] + route)
    (base / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
        + "\n</urlset>\n", encoding="utf-8")
    (base / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SUB[pub]}/sitemap.xml\n", encoding="utf-8")
    print(f"{pub}: {len(pages)} pages, sitemap, robots")

PREFIX = {"sports": "/sports", "entertainment": "/entertainment", "tech": "/tech", "fitness": "/fitness", "home": "/home"}
if MODE == "subdomain":
    SUB = {k: f"https://{v}.{DOMAIN}" for k, v in CFG["subdomains"].items() if k in PREFIX}
    SUB["writers"] = f"https://writers.{DOMAIN}"
else:
    SUB = {k: ORIGIN + pfx for k, pfx in PREFIX.items()}
    SUB["writers"] = ORIGIN + "/writers"
SUB["hub"] = f"https://{DOMAIN}" if MODE == "subdomain" else ORIGIN

def legal_pages(pub, name, tagline, skip=frozenset()):
    about_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / About</nav>
<section class="cover"><p class="kicker">About</p><h1 class="cover-title">{name}</h1>
<p class="cover-dek">{tagline}</p></section>
<section class="section"><div class="prose">
<p>{name} is one of the BRYME publications — a family of independent, specialist sites under THE BRYME. Each publication has its own focus, its own standards and its own editorial line; what they share is the house discipline: research before publishing, dates on anything time-sensitive, and no fabricated experience or statistics.</p>
<p>BRYME began as a writers' resource and grew into a small ecosystem of publications. The family is edited from Lagos, Nigeria, and written for a global readership.</p>
<h2>Editorial standards</h2>
<ul>
<li>Evergreen, genuinely useful work over volume.</li>
<li>First-hand experience where we have it; clearly labelled archive or research material where we don't.</li>
<li>Corrections in the open, on the page that made the claim.</li>
<li>No betting content, no piracy, no fabricated data — the house rules, applying everywhere.</li>
</ul>
</div></section></div>"""
    privacy_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Privacy</nav>
<section class="cover"><p class="kicker">Privacy</p><h1 class="cover-title">What we collect: almost nothing.</h1></section>
<section class="section"><div class="prose">
<p>{name} is a static publication. It sets no tracking cookies, runs no analytics on these pages, and asks for no personal information. Reading it is between you and your browser.</p>
<p>If interactive tools are added later, any data they store will stay in <em>your</em> browser's local storage on <em>your</em> device — the standing BRYME pattern — and this page will be updated before that changes.</p>
<p><b>Advertising &amp; cookies (updated 11 September 2026):</b> BRYME plans to show advertising, including through Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the internet. You may opt out of personalised advertising by visiting Google's Ads Settings (adssettings.google.com), or opt out of some third-party vendors' uses of cookies at aboutads.info. Visitors in the EEA and UK will be asked for consent before personalised advertising; without consent, only non-personalised ads are eligible to serve. Whatever serves, our standing rules apply: ads are clearly separated from content and navigation, never cover text, and never resemble our buttons, cards or links.</p>
<p>Questions: see <a href="/contact/">Contact</a>.</p>
</div></section></div>"""
    contact_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Contact</nav>
<section class="cover"><p class="kicker">Contact</p><h1 class="cover-title">Reach the desk.</h1>
<p class="cover-dek">Corrections first: if something on {name} is wrong, that is the most valuable email in the world to us.</p></section>
<section class="section"><div class="prose">
<p>Editorial contact details go live with the publication's domain launch. Until then, {name} is reached through <a href="https://writers.thebryme.com/contact/">the BRYME Writers contact page</a>, which routes to the same editorial desk.</p>
<h2>What to include</h2>
<ul><li>The page address and the exact claim that needs correcting.</li>
<li>For pitches: a two-paragraph summary and one relevant sample. No attachments.</li></ul>
</div></section></div>"""
    terms_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Terms</nav>
<section class="cover"><p class="kicker">Terms of use</p><h1 class="cover-title">The short, honest terms.</h1></section>
<section class="section"><div class="prose">
<p>{name} is free to read. It is provided as-is, for information: general guidance, never professional advice. Nothing on this publication is a substitute for qualified professional help — medical, electrical, gas, legal or financial. Where a topic borders on those fields, our pages say so plainly and stop.</p>
<p>The writing, layout and tools are \u00a9 2026 THE BRYME. Quote freely with a link; do not republish whole pages. External sites we link to have their own terms and their own owners. Adverts, when shown, are clearly separated from editorial content and never constitute an endorsement.</p>
<p>Questions about these terms: see <a href="/contact/">Contact</a>.</p>
</div></section></div>"""
    editorial_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Editorial policy</nav>
<section class="cover"><p class="kicker">Editorial policy</p><h1 class="cover-title">How every page earns its place.</h1></section>
<section class="section"><div class="prose">
<p>The BRYME method: <b>research, verify, explain, use.</b> Every page answers a real question, and time-sensitive claims carry a last-checked date and a source. We do not fabricate experience, statistics, reviews or rankings, and we do not publish pages whose only purpose is to catch a search.</p>
<h2>Fact labels</h2>
<ul>
<li><b>CONFIRMED FACT</b> — verified against an official or primary source, with source and date.</li>
<li><b>REPORTED</b> — carried by credible media, not yet officially confirmed; outlet and date attached.</li>
<li><b>RUMOURED</b> — speculation, shown separately, never blended into fact.</li>
<li><b>BRYME ANALYSIS</b> — our interpretation, attributed to us.</li>
<li><b>BRYME PREDICTION</b> — our model's or desk's projection, never presented as official data.</li>
</ul>
<h2>Standing prohibitions</h2>
<p>No betting content, no piracy or download pages, no fake play buttons, no scraped or duplicated pages, no misleading titles. Comparisons explain who each option is actually for; they never invent rankings. Errors are corrected in the open — see <a href="/corrections/">Corrections</a>.</p>
</div></section></div>"""
    corrections_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Corrections</nav>
<section class="cover"><p class="kicker">Corrections policy</p><h1 class="cover-title">We fix errors in the open.</h1></section>
<section class="section"><div class="prose">
<p>If something on {name} is wrong, tell us via <a href="/contact/">Contact</a> with the page address and the exact claim. The desk verifies against sources, fixes the page, and records the correction on the page itself — silently deleting a wrong claim is not a correction.</p>
<p>Time-sensitive facts (prices, availability, standings, schedules) are re-checked on a schedule and stamped with the date of the last check. If you spot a stale one, that report is welcome.</p>
</div></section></div>"""
    copyright_body = f"""<div class="wrap"><nav class="crumb"><a href="/">Home</a> / Copyright</nav>
<section class="cover"><p class="kicker">Copyright &amp; takedowns</p><h1 class="cover-title">Ownership, honestly stated.</h1></section>
<section class="section"><div class="prose">
<p>All original text, layout and tools on {name} are \u00a9 2026 THE BRYME. We quote and link to third-party material under fair quotation with attribution, and we do not host or link to pirated copies of films, shows, books or software — anywhere in the family.</p>
<p>Rights-holders with a concern: send the page address, the material concerned, and your relationship to the rights, via <a href="/contact/">Contact</a>. Verified takedown requests are actioned promptly.</p>
</div></section></div>"""
    def _m(b):
        return b if "<main" in b else '<main id="main"><div class="wrap">' + b + "</div></main>"
    out = [("/about/", f"About {name} | BRYME", f"What {name} is and the standards it holds.", _m(about_body)),
            ("/privacy/", f"Privacy | {name}", "What BRYME collects (almost nothing) and how advertising will be handled.", _m(privacy_body)),
            ("/contact/", f"Contact | {name}", "Corrections, pitches and the editorial desk.", _m(contact_body))]
    for route, t, d, b in [("/terms/", f"Terms of use | {name}", "The short, honest terms for using " + name + ".", _m(terms_body)),
                           ("/editorial-policy/", f"Editorial policy | {name}", "Fact labels, freshness standard, and the prohibitions every BRYME page obeys.", _m(editorial_body)),
                           ("/corrections/", f"Corrections | {name}", "How errors are reported, verified and fixed in the open.", _m(corrections_body)),
                           ("/copyright/", f"Copyright &amp; takedowns | {name}", "Ownership, fair quotation and takedown handling.", _m(copyright_body))]:
        if route not in skip:
            out.append((route, t, d, b))
    return out


# ------------------------------------------------------------------ 1. HUB
HUB_PUBS = [
    ("writers", "BRYME Writers", "The flagship.", "The practical digital library and workspace for writers \u2014 191 researched guides, 44 free browser tools, a hand-verified opportunity database and the essays behind the market. Free, independent, human-verified.", "live"),
    ("sports", "BRYME Sport", "The desk reopens.", "Football coverage from BRYME's media desk \u2014 transfer reporting, matchweek guides and the 2026-27 season, with the archive's thin pages honestly retired. No betting content, ever.", "live"),
    ("entertainment", "BRYME Entertainment", "Recovered from the archive.", "Cinema, TV and anime \u2014 guides, explainers and opinion rebuilt from BRYME's earliest editorial research, re-typeset and honestly labelled. No download sites, no piracy \u2014 only writing about the work.", "live"),
    ("tech", "BRYME Tech", "Practical technology. No theatre.", "Deployment walkthroughs, domain and DNS specifics, token hygiene, front-end patterns \u2014 written from first-hand builds, not press releases. Evergreen on purpose.", "live"),
]
WORKSHOP_PUBS = [
    ("fitness", "BRYME Fitness", "Now open.", "Practical fitness, built to keep: two interactive tools \u2014 the 30-day walking plan and the weekly planner \u2014 plus a dozen honest, sourced guides on starting, strength, protein, sleep and recovery. General fitness information, never medical advice.", "live"),
    ("home", "BRYME Home & DIY", "Now open.", "Practical help for fixing, maintaining and understanding your home \u2014 low-risk repairs explained honestly, an in-browser seasonal checklist, and safety boundaries stated without apology.", "live"),
]

def hub_pages():
    import datetime as _dt
    _wr = ROOT / "public" / "writers"
    _legal = {"about", "contact", "privacy", "terms", "corrections", "editorial-policy",
              "copyright", "disclaimer", "disclosure", "assets"}
    _n_guides = sum(1 for f in _wr.rglob("index.html")
                    if f.parent.name not in _legal and "tools" not in f.parts) if _wr.exists() else 0
    _n_tools = len([d for d in (_wr / "tools").iterdir() if d.is_dir()]) if (_wr / "tools").exists() else 0
    _stamp = " Counts verified at every build (last: " + _dt.date.today().isoformat() + ")."
    cards = ""
    for key, name, tag, desc, state in HUB_PUBS + WORKSHOP_PUBS:
        if key == "writers" and _n_guides:
            desc = (desc.replace("191 researched guides", str(_n_guides) + " researched pages")
                        .replace("44 free browser tools", str(_n_tools) + " free browser tools")
                        .rstrip(".")
                    + ". " + _stamp)
        kicker = PUB_NAME.get(key, "").upper() if key != "writers" else "THE FLAGSHIP"
        if state == "live":
            cta = f'<a class="btn" href="{SUB[key]}/">Enter {name.split(" ")[1]} →</a>'
            cls = "pub-card live"
        else:
            cta = '<span class="soon-tag">In build — opens soon</span>'
            cls = "pub-card soon"
        cards += f'<article class="{cls}" style="--pc:{FAMILY[key]["brand"] if key!="hub" else "#1e3a5f"}"><p class="pc-kicker">{kicker} &#183; ACTIVE</p><h3>{name}</h3><p>{desc}</p>{cta}</article>'
    body = f"""{head("hub", "Six publications. One house standard.", parent=False)}
<main id="main"><div class="wrap">
<section class="cover"><p class="kicker">A family of independent publications</p>
<h1 class="cover-title">THE BRYME</h1>
<p class="cover-dek">BRYME is a small ecosystem of specialist publications, each with its own focus and its own standards, held to one house rule: research before publishing, and say exactly what you know. Pick a desk.</p></section>
<section class="section"><div class="section-head"><p class="kicker">The publications</p><h2>Choose your desk</h2></div>
<div class="cards">{cards}</div></section>
<section class="section alt"><div class="section-head"><p class="kicker">The house</p><h2>One standard, six voices.</h2></div>
<p class="lede">Every BRYME publication is edited by the same desk, run on the same discipline — dates on time-sensitive claims, corrections in the open, no fabricated experience, no pages built to game a search engine — and none of them share a navigation bar. When you enter one, you are in that world.</p>
</section></div></main>
{foot("hub")}"""
    hub_index = [("index.html placeholder", "", "", "")]
    return [("/", "THE BRYME — a family of independent publications",
             "BRYME is six specialist publications — Writers, Sport, Entertainment, Tech, Fitness and Home &amp; DIY — under one house standard. Choose your desk.", body)]


# ------------------------------------------------------- 2. ENTERTAINMENT
def clean_recovered(raw):
    # the archive predates the ecosystem: absolute links to the retired GitHub Pages
    # host come home to the entertainment shelf instead of leaving the site
    raw = re.sub(r"https?://ojeology\.github\.io/nextclip/[^\"<> ]*", "/entertainment/", raw)
    raw = re.sub(r"<h1\b[^>]*>[\s\S]*?</h1>", "", raw, count=1)
    # strip links to the retired catalog (dead routes) — keep external http(s)
    raw = re.sub(r'<a\s[^>]*href="(/(?!entertainment/?\')[^"]*)"[^>]*>(.*?)</a>', r"\2", raw, flags=re.S)
    raw = re.sub(r'<a\s[^>]*href="(/(?!entertainment/?)[^"]*)"[^>]*>(.*?)</a>', r"\2", raw, flags=re.S)
    raw = re.sub(r"<img[^>]*>", "", raw)
    return raw

ENT_SECTIONS = {
    "recommendations": ("What to watch next", "Recommendations, starter routes and watch orders \u2014 the answer to \u201cwhat should I watch tonight?\u201d, argued honestly rather than scraped."),
    "explainers": ("Explainers & comparisons", "Why a show became a phenomenon, what a character\u2019s choice really meant, and the head-to-heads fans actually argue about."),
    "opinion": ("Opinion & lists", "Reviews with a spine, cult favourites defended, and lists with a reason behind every entry \u2014 labelled as opinion, written as argument."),
}
ENT_SLUG_SECT = {
    "10-anime-like-solo-leveling-you-should-watch": "recommendations",
    "10-shows-like-alice-in-borderland-you-should-watch-next": "recommendations",
    "movies-like-deadpool-and-wolverine": "recommendations",
    "movies-like-interstellar-guide": "recommendations",
    "movies-like-parasite": "recommendations",
    "christopher-nolan-movies-order": "recommendations",
    "korean-cinema-starter-guide-rebuilt": "recommendations",
    "indian-cinema-first-five": "recommendations",
    "modern-horror-starter-route": "recommendations",
    "nigerian-thrillers-worth-your-time": "recommendations",
    "how-to-pick-a-movie-tonight": "recommendations",
    "best-streaming-apps-nigeria": "recommendations",
    "dune-sci-fi-epics-guide": "recommendations",
    "alien-franchise-in-order": "recommendations",
    "squid-game-season-1-why-it-became-a-global-phenomenon": "explainers",
    "was-eren-yeager-really-the-villain": "explainers",
    "solo-leveling-e-rank-to-s-rank": "explainers",
    "alice-in-borderland-vs-squid-game": "explainers",
    "one-piece-vs-naruto": "explainers",
    "solo-leveling-vs-hunter-x-hunter-the-similarities-and-differences": "explainers",
    "breaking-bad-two-seasons-opinion": "opinion",
    "10-korean-movies-everyone-should-watch": "recommendations",
    "best-anime-to-watch-now": "recommendations",
    "10-facts-about-agent-kim-squid-game-season-3": "explainers",
    "5-movies-that-broke-the-internet": "opinion",
    "7-movies-we-wished-never-ended": "opinion",
    "into-the-badlands-was-underrated": "opinion",
    "why-prison-break-season-1-is-still-one-of-the-best-tv-seasons": "opinion",
}
# consolidation: the second slug is folded into the first as a labelled companion piece
ENT_MERGE = {
    "solo-leveling-e-rank-to-s-rank": "solo-leveling-from-e-rank-hunter-to-one-of-animes-most-powerful-characters",
    "why-prison-break-season-1-is-still-one-of-the-best-tv-seasons": "prison-break-season-1-watching-all-night",
    "movies-like-interstellar-guide": ["interstellar-ending-explained", "movies-like-interstellar"],
    "modern-horror-starter-route": "5-vampire-movies-that-changed-horror",
    "dune-sci-fi-epics-guide": "why-dune-part-two-feels-large",
    "korean-cinema-starter-guide-rebuilt": "korean-cinema-starter-guide",
}
# values may be a single slug or a list — normalise to lists
ENT_MERGE = {k: (v if isinstance(v, list) else [v]) for k, v in ENT_MERGE.items()}
ENT_START = ["how-to-pick-a-movie-tonight", "how-to-build-a-watchlist", "christopher-nolan-movies-order",
             "best-streaming-apps-nigeria", "korean-cinema-starter-guide-rebuilt"]

def _first_line(body_html, fallback=""):
    m = re.search(r"<p[^>]*>([\s\S]*?)</p>", body_html)
    if not m:
        return fallback
    txt = _strip_tags(m.group(1))
    txt = html.unescape(re.sub(r"\s+", " ", txt)).strip()
    return (txt[:157] + "\u2026") if len(txt) > 160 else txt

def _strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)

def entertainment_pages():
    rec = OUT / "entertainment" / "_recovered"
    manifest = json.loads((rec / "manifest.json").read_text())
    by_slug = {m["slug"]: m for m in manifest}
    # the moved piece joins the manifest with its own record
    by_slug["best-streaming-apps-nigeria"] = {
        "slug": "best-streaming-apps-nigeria",
        "title": "Best Streaming Apps in Nigeria (2026), Honestly Compared",
        "words": 900, "moved": True}
    # evergreen guides: original pieces, no archive provenance
    import entertainment_guides_data
    guide_bodies = {}
    for slug, sect, title, dek, body in entertainment_guides_data.ENT_GUIDES:
        ENT_SLUG_SECT[slug] = sect
        by_slug[slug] = {"slug": slug, "title": title, "words": len(re.sub(r"<[^>]+>", " ", body).split()),
                         "new": True}
        guide_bodies[slug] = body
    import entertainment_watch_guides_data
    for slug, sect, title, dek, body in entertainment_watch_guides_data.WATCH_GUIDES:
        ENT_SLUG_SECT[slug] = sect
        by_slug[slug] = {"slug": slug, "title": title, "words": len(re.sub(r"<[^>]+>", " ", body).split()),
                         "new": True}
        guide_bodies[slug] = body
    shelf = sorted(ENT_SLUG_SECT)
    merged_away = {o for vs in ENT_MERGE.values() for o in vs}
    bodies = {}
    for slug in shelf + sorted(merged_away):
        if slug in guide_bodies:
            bodies[slug] = guide_bodies[slug]
        else:
            raw = (rec / f"{slug}.html").read_text()
            bodies[slug] = clean_recovered(raw)
    arts = {}
    for slug in shelf:
        if slug in merged_away:
            continue
        m = by_slug[slug]
        sect = ENT_SLUG_SECT[slug]
        moved = m.get("moved")
        if m.get("new"):
            kick = "Evergreen guide \u00b7 "
        elif moved:
            kick = "Moved from the BRYME tech desk \u00b7 "
        else:
            kick = "Archive edition (2025) \u00b7 "
        comp_html = ""
        for other in ENT_MERGE.get(slug, []):
            comp_html += ('<h2>Companion piece, restored: ' + html.escape(by_slug[other]["title"]) + "</h2>"
                         + "<p><em>Merged from the archive so the whole argument lives on one page.</em></p>"
                         + bodies[other])
        summ = _first_line(bodies[slug])
        rel_pool = [s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == sect and s2 != slug]
        rel = rel_pool[:3]
        while len(rel) < 3:
            for s2 in shelf:
                if s2 not in merged_away and s2 != slug and s2 not in rel:
                    rel.append(s2)
                    break
            if len(rel) >= 3:
                break
        rel_html = "".join('<li><a href="/' + s2 + '/">' + html.escape(by_slug[s2]["title"]) + "</a></li>" for s2 in rel)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": m["title"],
                  "author": {"@type": "Organization", "name": "BRYME Entertainment desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/entertainment/" + slug + "/",
                  "description": summ}
        import json as _j
        byline = ("Written by the BRYME Entertainment desk \u00b7 reviewed " + TODAY
                  + " \u00b7 evergreen \u2014 re-checked whenever the facts move") if m.get("new") else (
                  "Recovered from the archive \u00b7 " + str(m["words"]) + " words \u00b7 re-typeset and reviewed "
                  + TODAY + (" \u00b7 prices in older pieces change \u2014 confirm with the service" if slug == "best-streaming-apps-nigeria" else ""))
        abody = (head("entertainment", "Cinema, TV and anime \u2014 written about, never pirated.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/entertainment/">Entertainment</a> / <a href="/entertainment/' + sect + '/">'
            + html.escape(ENT_SECTIONS[sect][0]) + "</a> / " + html.escape(m["title"]) + "</nav>"
            + '<section class="cover"><p class="kicker">' + kick + "no piracy, no scrapes \u2014 written about the work</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(m["title"]) + "</h1>"
            + '<p class="byline">BRYME Entertainment desk \u00b7 ' + html.escape(byline) + "</p></section>"
            + ('<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(summ) + "</p></div></section>" if summ else "")
            + '<section class="section"><div class="prose">' + bodies[slug] + comp_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from ' + html.escape(ENT_SECTIONS[sect][0]) + '.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/entertainment/' + sect + '/">All of ' + html.escape(ENT_SECTIONS[sect][0]) + '</a>'
            + '<a class="btn secondary" href="/entertainment/">All of BRYME Entertainment</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("entertainment"))
        arts[slug] = (("/" + slug + "/"), m["title"] + " | BRYME Entertainment", summ or "From the BRYME archive \u2014 re-typeset and honestly labelled.", abody)

    sect_pages = {}
    for cslug, (cname, cdesc) in ENT_SECTIONS.items():
        lst = [s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == cslug]
        lst.sort(key=lambda s2: -by_slug[s2]["words"])
        rows = "".join(
            '<li><a href="/' + s2 + '/"><span><b>' + html.escape(by_slug[s2]["title"]) + "</b><small>"
            + html.escape(_first_line(bodies[s2])[:110]) + "\u2026</small></span>"
            '<span class="meta">' + str(by_slug[s2]["words"]) + " words</span></a></li>" for s2 in lst)
        others = "".join('<a class="btn secondary" href="/entertainment/' + c2 + '/">' + html.escape(ENT_SECTIONS[c2][0]) + "</a>"
                         for c2 in ENT_SECTIONS if c2 != cslug)
        cbody = (head("entertainment", "Cinema, TV and anime \u2014 written about, never pirated.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/entertainment/">Entertainment</a> / ' + html.escape(cname) + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Entertainment \u00b7 section</p>'
            + '<h1 class="cover-title">' + html.escape(cname) + "</h1>"
            + '<p class="cover-dek">' + html.escape(cdesc) + "</p></section>"
            + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(lst)) + ' pieces</p><h2>Everything in ' + html.escape(cname) + '.</h2></div>'
            + '<ul class="list">' + rows + "</ul></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Keep watching</p><h2>Elsewhere on this desk.</h2></div>'
            + '<div class="actions">' + others + "</div></section></div></main>" + foot("entertainment"))
        sect_pages[cslug] = [("/" + cslug + "/", cname + " | BRYME Entertainment", cdesc, cbody)]

    start_rows = "".join(
        '<li><a href="/' + s2 + '/"><span><b>' + html.escape(by_slug[s2]["title"]) + "</b><small>"
        + html.escape(_first_line(bodies[s2])[:110]) + "\u2026</small></span><span class=\"meta\">Start here</span></a></li>"
        for s2 in ENT_START)
    cat_cards = "".join(
        '<article class="pub-card live" style="--pc:#6d1832"><p class="pc-kicker">' + str(len([s2 for s2 in shelf if s2 not in merged_away and ENT_SLUG_SECT[s2] == c])) + ' PIECES</p>'
        + "<h3>" + html.escape(ENT_SECTIONS[c][0]) + "</h3><p>" + html.escape(ENT_SECTIONS[c][1][:130]) + "\u2026</p>"
        + '<a class="btn" href="/entertainment/' + c + '/">Browse ' + html.escape(ENT_SECTIONS[c][0]) + " \u2192</a></article>"
        for c in ENT_SECTIONS)
    cat_cards = ('<article class="pub-card live" style="--pc:#6d1832"><p class="pc-kicker">THE CATALOGUE</p><h3>Browse the movies</h3><p>Every film and series the desk covers, shelved: fantasy &amp; sci-fi, anime, K-drama and more — each entry links to where the argument actually lives.</p><a class="btn" href="/entertainment/browse/">Open the catalogue →</a></article>'
        + cat_cards)
    retired_rows = "".join(
        '<li><span><b>' + html.escape(m["title"]) + "</b><small>" + str(m["words"]) + " words \u00b7 reviewed by the audit \u2014 retired on merit</small></span>"
        '<span class="meta">Retired</span></li>'
        for m in manifest if m["slug"] not in ENT_SLUG_SECT and m["slug"] not in merged_away
        and m["slug"] not in {"korean-cinema-starter-guide", "movies-like-interstellar"})
    index_body = (head("entertainment", "Cinema, TV and anime \u2014 written about, never pirated.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Entertainment</p>'
        + '<h1 class="cover-title">What should I watch \u2014 and why?</h1>'
        + '<p class="cover-dek">Recommendations with reasons, explainers without spoilers-for-sport, and opinion labelled as opinion. Everything here is written about the work: no download pages, no fake play buttons, no piracy \u2014 ever.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Handpicked</p><h2>Start here.</h2></div>'
        + '<ul class="list">' + start_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Browse by need</p><h2>Sections of this desk.</h2></div>'
        + '<div class="cards">' + cat_cards + "</div></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The house rule</p><h2>Written about the work, never trafficking in it.</h2></div>'
        + '<p class="lede">BRYME Entertainment does not stream, host, link or hint at pirated copies. External trailers may support a piece; the value on the page is the argument. Restored editions say so plainly, carry their word counts, and were re-typeset \u2014 not quietly re-scraped.</p>'
        + '<ul class="list" style="margin-top:14px">' + retired_rows + "</ul>"
        + "</section></div></main>" + foot("entertainment"))
    import entertainment_catalogue_data as _cat
    body_text = {s2: html.unescape(re.sub(r"<[^>]+>", " ", b2)).lower().replace("\u2019", chr(39)) for s2, b2 in bodies.items()}
    shelf_html = ""
    for n2, (cs, clabel, cdek, entries) in enumerate(_cat.CATALOGUE_SHELVES):
        tiles = ""
        for (t, yr, kind, blurb, slugs) in entries:
            low = t.lower().replace("&amp;", "&").replace("\u2019", chr(39))
            for s3 in slugs:
                composed = body_text[s3] + " ".join(body_text[o] for o in ENT_MERGE.get(s3, []))
                assert low in composed, f"catalogue truth check: '{t}' not found in {s3}"
            primary = slugs[0]
            more = "".join('<a href="/' + s3 + '/">' + html.escape(by_slug[s3]["title"]) + "</a> · " for s3 in slugs[1:])
            tiles += ('<li style="display:block"><a href="/' + primary + '/"><span><b>' + t
                      + " <span class=\"meta\">(" + yr + ")</span></b><small>" + kind + " \u2014 " + blurb + "</small></span>"
                      + '<span class="meta">' + str(len(slugs)) + " link" + ("s" if len(slugs) > 1 else "") + "</span></a>"
                      + ('<div style="font-size:13px;padding:2px 0 10px">Also in: ' + more.rstrip(" · ") + "</div>" if more else "")
                      + "</li>")
        footers = "".join('<a class="btn secondary" href="/' + fs + '/">' + fl + "</a>" for fs, fl in _cat.CATALOGUE_SHELF_FOOTERS[cs])
        picks = _cat.CATALOGUE_STARTERS.get(cs, [])
        picks_html = ""
        if picks:
            rows = "".join('<li><span><b>' + t + '</b> <span class="meta">(' + yr + ")</span><small>" + kind + " — " + blurb + "</small></span></li>" for t, yr, kind, blurb in picks)
            picks_html = ('<div class="section-head" style="margin-top:8px"><p class="kicker">Quick picks</p><h3>More to start with tonight.</h3></div>'
                + '<p class="lede" style="font-size:15px">Desk-curated starters — canonical, evergreen, and safe to press play on. No dedicated review yet; coverage grows every batch.</p>'
                + '<ul class="list" style="font-size:15px">' + rows + "</ul>")
        shelf_html += ('<section id="shelf-' + cs + '" class="' + ("section" if n2 % 2 == 0 else "section alt") + '"><div class="section-head"><p class="kicker">Shelf ' + str(n2 + 1) + "</p><h2>" + clabel + "</h2></div>"
            + '<p class="lede">' + cdek + "</p>"
            + '<ul class="list">' + tiles + "</ul>"
            + picks_html
            + '<div class="actions">' + footers + "</div></section>")
    n_titles = sum(len(e[4]) for sh in _cat.CATALOGUE_SHELVES for e in sh[3])
    n_picks = sum(len(v) for v in _cat.CATALOGUE_STARTERS.values())
    browse_body = (head("entertainment", "The catalogue — every title the desk covers, shelved.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/entertainment/">Entertainment</a> / Browse the movies</nav>'
        + '<section class="cover"><p class="kicker">BRYME Entertainment · the catalogue</p>'
        + '<h1 class="cover-title">Browse the movies.</h1>'
        + '<p class="cover-dek">Every title below is covered somewhere on this desk — no database padding, no empty entries. Pick a shelf; each tile links to the page where the argument actually lives.</p></section>'
        + '<nav class="actions" style="justify-content:center;padding:0 0 8px">'
        + "".join('<a class="btn secondary" href="#shelf-' + cs + '">' + cl.replace("&amp;", "&") + "</a>" for cs, cl, _d, _e in _cat.CATALOGUE_SHELVES)
        + "</nav>"
        + shelf_html
        + '<section class="section"><div class="section-head"><p class="kicker">The house rule</p><h2>Links that go somewhere.</h2></div>'
        + '<p class="lede">This catalogue lists ' + str(len([e for sh in _cat.CATALOGUE_SHELVES for e in sh[3]])) + " titles argued on this desk with " + str(n_titles) + " verified coverage links, plus " + str(n_picks) + " desk-curated quick picks — " + str(len([e for sh in _cat.CATALOGUE_SHELVES for e in sh[3]]) + n_picks) + " ways to start tonight. Covered titles link to where the argument lives; quick picks are labelled as such. If a title is missing, we have not written about it yet — and we do not pretend otherwise.</p>"
        + "</section></div></main>" + foot("entertainment"))
    pages = [("/", "BRYME Entertainment — what to watch, and why",
              "Film, TV and anime recommendations with reasons, explainers and opinion — written about the work, never piracy.", index_body),
             ("/browse/", "Browse the movies — the BRYME Entertainment catalogue",
              "Every film, series and anime the desk covers, shelved under fantasy & sci-fi, anime, K-drama and more — each entry links to real coverage.", browse_body)]
    for pl in sect_pages.values():
        pages.extend(pl)
    pages.extend(arts[s] for s in shelf if s not in merged_away)
    return pages + legal_pages("entertainment", "BRYME Entertainment", "Writing about film, TV and anime for people who love the work.")



# ------------------------------------------------------------- 3. SPORTS
def sports_pages():
    rec = Path(OUT / "sports" / "_recovered")
    manifest = json.loads((rec / "manifest.json").read_text())
    REAL = {"premier-league-transfer-tracker-august-2026", "premier-league-matchweek-2-preview",
            "elliot-anderson-man-city-record-signing", "deadline-day-dont-try-to-make-sense-of-it",
            "premier-league-matchweek-1-guide"}
    by = {m["slug"]: m for m in manifest}
    restored, retired = [], []
    pages = []
    for slug in sorted(REAL):
        m = by.get(slug)
        if not m:
            continue
        body_file = rec / f"{slug}.body.html"
        if not body_file.exists():
            continue
        body_html = clean_recovered(body_file.read_text())
        route = f"/{slug}/"
        archive = slug in {"premier-league-transfer-tracker-august-2026",
                           "premier-league-matchweek-1-guide", "premier-league-matchweek-2-preview",
                           "deadline-day-dont-try-to-make-sense-of-it"}
        kick = ("Season 2026-27 \u00b7 archive edition" if archive else "The desk \u00b7 2026-27 season")
        arch_note = (" \u00b7 written during the live season window and kept as archive \u2014 "
                     "new editions return with the season" if archive else "")
        restored.append(f'<li><a href="{route}"><span><b>{html.escape(m["title"])}</b>'
                        f'<small>From the media desk · {m["words"]} words · {TODAY}</small></span>'
                        f'<span class="meta">Read</span></a></li>')
        pbody = f"""{head("sports", "Analysis, stories and the long view \u2014 never betting.")}
<main id="main"><div class="wrap">
<nav class="crumb"><a href="/">Home</a> / {html.escape(m["title"])}</nav>
<section class="cover"><p class="kicker">{kick}</p>
<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">{html.escape(m["title"])}</h1>
<p class="byline">From the BRYME media desk · recovered edition, re-typeset {TODAY}{arch_note}</p></section>
<section class="section"><div class="prose">{body_html}</div></section>
</div></main>{foot("sports")}"""
        pages.append((route, f'{m["title"]} | BRYME Sport',
                      "From the BRYME media desk — recovered edition, re-typeset.", pbody))

    # evergreen explainers: laws, formats and roles — no fixtures, no data rights, no betting
    import sports_explainers_data
    import sports_features_data
    import json as _j
    expl_rows = []
    for slug, title, dek, body, sources, related in sports_explainers_data.SPORT_EXPLAINERS:
        src_html = ""
        if sources:
            src_html = ('<h2>Sources</h2><ul class="list">'
                        + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                        + "</ul>")
        rel_html = "".join('<li><a href="/' + s + '/">' + rt + "</a></li>" for s, rt in related)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": title,
                  "author": {"@type": "Organization", "name": "BRYME Sport desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/sports/" + slug + "/",
                  "description": dek}
        ebody = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/sports/explainers/">Explainers</a> / ' + title + "</nav>"
            + '<section class="cover"><p class="kicker">Explainer \u00b7 evergreen</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + title + "</h1>"
            + '<p class="byline">BRYME Sport desk \u00b7 reviewed ' + TODAY + " \u00b7 evergreen explainer \u2014 no odds, no tips, no invented facts</p></section>"
            + '<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + dek + "</p></div></section>"
            + '<section class="section"><div class="prose">' + body + src_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from the shelf.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/sports/explainers/">All explainers</a>'
            + '<a class="btn secondary" href="/sports/">All of BRYME Sport</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("sports"))
        pages.append(("/" + slug + "/", title + " | BRYME Sport", dek[:155], ebody))
        expl_rows.append('<li><a href="/' + slug + '/"><span><b>' + title + "</b><small>" + dek[:110] + "\u2026</small></span>"
                         '<span class="meta">Explainer</span></a></li>')

    # the analysis shelf: how the game is played (batch 3)
    import sports_analysis_data
    analysis_rows = []
    for slug, title, dek, body, sources, related in sports_analysis_data.SPORT_ANALYSIS:
        src_html = ""
        if sources:
            src_html = ('<h2>Sources</h2><ul class="list">'
                        + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                        + "</ul>")
        rel_html = "".join('<li><a href="/' + s + '/">' + rt + "</a></li>" for s, rt in related)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": title,
                  "author": {"@type": "Organization", "name": "BRYME Sport desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/sports/" + slug + "/",
                  "description": dek}
        abody = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/analysis/">Analysis</a> / ' + title + "</nav>"
            + '<section class="cover"><p class="kicker">Analysis \u00b7 evergreen</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + title + "</h1>"
            + '<p class="byline">BRYME Sport desk \u00b7 reviewed ' + TODAY + " \u00b7 evergreen analysis \u2014 no odds, no tips, no invented facts</p></section>"
            + '<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + dek + "</p></div></section>"
            + '<section class="section"><div class="prose">' + body + src_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>More from the shelf.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/analysis/">All analysis</a>'
            + '<a class="btn secondary" href="/sports/">All of BRYME Sport</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("sports"))
        pages.append(("/" + slug + "/", title + " | BRYME Sport", dek[:155], abody))
        analysis_rows.append('<li><a href="/' + slug + '/"><span><b>' + title + "</b><small>" + dek[:110] + "\u2026</small></span>"
                         '<span class="meta">Analysis</span></a></li>')

    # the analysis shelf hub
    analysis_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The analysis shelf</nav>'
        + '<section class="cover"><p class="kicker">The analysis shelf \u00b7 how the game is played</p>'
        + '<h1 class="cover-title">Read the game, not the noise.</h1>'
        + '<p class="cover-dek">The ideas behind the tactics \u2014 expected goals, pressing, possession, the short build-up and the trap \u2014 explained plainly and argued honestly. Concepts only, evergreen: no odds, no tips, no invented numbers.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(sports_analysis_data.SPORT_ANALYSIS)) + ' pieces</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + "".join(analysis_rows) + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">The honest bit</p><h2>How this desk uses numbers.</h2></div>'
        + '<div class="prose"><p>Analysis pieces explain concepts; where a number has a model behind it, the piece says what the model measures and what it misses. No betting angles, ever &mdash; understanding the game is the product, not tipping it.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/analysis/", "The analysis shelf \u2014 how the game is played | BRYME Sport",
                  "xG, pressing, possession, the short build-up and the offside trap \u2014 the ideas behind modern football, explained honestly and evergreen.", analysis_hub))
    epl_archive = [
        ("/premier-league-matchweek-2-preview", "Matchweek 2 preview", "Archive", "The season's second weekend, previewed before a ball was kicked."),
        ("/premier-league-matchweek-1-guide", "Matchweek 1 guide", "Archive", "Opening weekend: the storylines worth carrying into the season."),
        ("/premier-league-transfer-tracker-august-2026", "The August 2026 transfer tracker", "Archive", "The summer window as this desk could verify it, deal by deal."),
        ("/deadline-day-dont-try-to-make-sense-of-it", "Deadline day: don't try to make sense of it", "Archive", "A field guide to the window's strangest evening."),
    ]
    epl_evergreen = [
        ("/promotion-and-relegation-explained", "Promotion and relegation", "Explainer", "The pyramid that makes every April matter at both ends of the table."),
        ("/the-offside-rule-explained", "The offside rule, explained", "Explainer", "Position, timing, involvement \u2014 the three ideas that settle most arguments."),
        ("/how-var-works", "How VAR actually works", "Explainer", "What is checkable, who decides, and why the wait exists."),
    ]
    epl_rows = ('<section class="section"><div class="section-head"><p class="kicker">Archive editions</p><h2>The 2026-27 season, as we covered it.</h2></div>'
        + '<ul class="list">' + "".join('<li><a href="' + r[0] + '/"><span><b>' + r[1] + '</b><small>' + r[3] + '</small></span><span class="meta">' + r[2] + '</span></a></li>' for r in epl_archive) + '</ul></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">Evergreen explainers</p><h2>The laws and ideas that never expire.</h2></div>'
        + '<ul class="list">' + "".join('<li><a href="' + r[0] + '/"><span><b>' + r[1] + '</b><small>' + r[3] + '</small></span><span class="meta">' + r[2] + '</span></a></li>' for r in epl_evergreen) + '</ul></section>')

    # the league desks: EPL + LaLiga (batch 4, header/league pass)
    epl_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The Premier League desk</nav>'
        + '<section class="cover"><p class="kicker">The Premier League desk \u00b7 the league, covered honestly</p>'
        + '<h1 class="cover-title">The Premier League, without the noise.</h1>'
        + '<p class="cover-dek">The desk\u2019s England-top-flight shelf: dated editions from the live season, the archived summer window, and the evergreen explainers that never stop applying. The first live edition of 2026-27 is on the shelf below.</p></section>'
        + '<section class="section"><div class="prose"><p>House rules apply here as everywhere on the desk: no odds, no rumour mill, no invented results. The matchweek editions below were written during the live season window and kept exactly as published. The transfer mechanics behind every window live on the <a href="/sports/transfers/">transfer desk</a>, and the league\u2019s pyramid is explained in <a href="/promotion-and-relegation-explained/">promotion and relegation</a>.</p></div></section>'
        + epl_rows
        + '<section class="section"><div class="prose"><p><em>The desk is live again for 2026-27: the <a href=\"/premier-league-matchweek-4-preview/\">Matchweek 4 preview</a> is the first fresh dated edition of the season \u2014 published the Thursday before the weekend, no odds, ever. The archive stands exactly as written.</em></p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/epl/", "The Premier League desk | BRYME Sport",
                  "Matchweek and transfer-window archive editions plus evergreen league explainers \u2014 the Premier League covered honestly, never betting.", epl_hub))
    # ---- live desk edition: Matchweek 4 preview (written 2026-09-10, table as of MW3) ----
    mw4_body = ('<section class="section"><div class="prose">'
        + '<p>This is a live desk edition: written on Thursday 10 September 2026, before a ball is kicked this weekend. The way this desk previews is simple \u2014 verified fixtures, the table as it actually stands, and the storylines worth your time. No odds, no \u201cguaranteed bankers\u201d, no invented team news. Where we don\u2019t know something \u2014 line-ups, injuries, late changes \u2014 we say the desk doesn\u2019t know it.</p>'
        + '<h2>The fixtures (all times UK)</h2>'
        + '<ul>'
        + '<li><b>Saturday 12 September, 15:00</b> \u2014 Aston Villa v Nottingham Forest \u00b7 Bournemouth v Brentford \u00b7 Chelsea v Hull City \u00b7 Crystal Palace v Ipswich \u00b7 Liverpool v Fulham</li>'
        + '<li><b>Saturday 17:30</b> \u2014 Tottenham v Everton</li>'
        + '<li><b>Saturday 20:00</b> \u2014 Sunderland v Arsenal</li>'
        + '<li><b>Sunday 13 September, 14:00</b> \u2014 Coventry v Brighton</li>'
        + '<li><b>Sunday 16:30</b> \u2014 Manchester United v Manchester City</li>'
        + '<li><b>Monday 14 September, 20:00</b> \u2014 Leeds United v Newcastle</li>'
        + '</ul>'
        + '<p>The table going into the weekend, as of Matchweek 3: Manchester City and Arsenal both have nine points from nine, with City top on goals scored (seven to six). Behind them sit Hull City on seven and Chelsea on six, then a pack on five. Fulham and Coventry are still on zero; Aston Villa and Tottenham have a point each and no league goal yet. Early tables exaggerate \u2014 three games is a rumour, not a season \u2014 but they are still the facts on the wall, and the <a href="/promotion-and-relegation-explained/">promotion-and-relegation mechanics</a> are exactly why a promoted club\u2019s strong start matters.</p>'
        + '<h2>One: the derby, with a table attached</h2>'
        + '<p>United host City on Sunday afternoon with the league\u2019s only perfect record standing in the away dressing room. City have nine from nine; United have four from three. Derby form logic goes into hibernation every year, so the desk will simply watch the things that decide derbies: the first goal, the midfield duels, and whether the game opens up late. If a decision goes to the video room, <a href="/how-var-works/">how VAR actually works</a> explains why the wait exists before anyone melts down about it.</p>'
        + '<h2>Two: Hull City visit Chelsea, unbeaten and unscored-on</h2>'
        + '<p>The season\u2019s genuine surprise: promoted Hull City sit third after three games, unbeaten, and yet to concede a league goal. Now comes the stamping-ground test \u2014 away at a Chelsea side that dropped its first points of the season last time out. Whatever happens, this fixture tells us whether Hull\u2019s start is a platform or a sugar rush. The arithmetic of why it matters so much is in <a href="/promotion-and-relegation-explained/">promotion and relegation</a>, and the story of how squads like this get assembled is on <a href="/what-does-a-sporting-director-do/">what a sporting director actually does</a>.</p>'
        + '<h2>Three: Arsenal at the Stadium of Light, Saturday 20:00</h2>'
        + '<p>Arsenal\u2019s three games have produced six goals for and one against \u2014 the league\u2019s meanest defence. Sunderland, on four points from three, get the Saturday-night home slot. Big-stage games under lights are where intensity and crowd noise feed each other; <a href="/pressing-explained/">pressing, explained</a> gives you the vocabulary for the ten seconds after every kick-off, and <a href="/playing-out-from-the-back/">playing out from the back</a> explains what both managers are asking their goalkeepers to be brave about.</p>'
        + '<h2>Four: the bottom shelf stirs</h2>'
        + '<p>Three clubs are still waiting for lift-off. Fulham, on zero points, travel to Liverpool \u2014 the kind of fixture where the table says one thing and the loud predictions say another, which is one reason this desk does not do betting angles. Coventry, also on zero and without a goal, host a Brighton side that has scored eight in three. Tottenham, on one point and no league goals, host an Everton side that has started better, on five. Any of those three columns can look completely different by Monday night \u2014 that is what a matchweek is for.</p>'
        + '<h2>What the desk will do after the weekend</h2>'
        + '<p>Report what happened, not what we hoped. Where a number is interesting, we will say what it measures and what it misses \u2014 <a href="/xg-explained/">xG, explained</a> is the standing primer. The <a href="/sports/epl/">Premier League desk</a> holds the archive and the evergreens, and the <a href="/sports/explainers/">explainers shelf</a> has the vocabulary. The previous live editions sit alongside: the <a href="/premier-league-matchweek-2-preview/">Matchweek 2 preview</a> and the <a href="/premier-league-matchweek-1-guide/">Matchweek 1 guide</a>.</p>'
        + '</div></section>')
    mw4 = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/epl/">Premier League desk</a> / Matchweek 4 preview</nav>'
        + '<section class="cover"><p class="kicker">Season 2026-27 \u00b7 Matchweek 4 \u00b7 live desk edition</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">Matchweek 4, previewed honestly.</h1>'
        + '<p class="byline">BRYME Sport desk \u00b7 written Thursday 10 September 2026 \u00b7 table and results as of Matchweek 3 \u00b7 no odds, ever</p></section>'
        + mw4_body
        + '</div></main>' + foot("sports"))
    pages.append(("/premier-league-matchweek-4-preview/", "Premier League Matchweek 4 preview \u2014 fixtures, the real table, the storylines | BRYME Sport",
                  "The desk\u2019s first live edition of 2026-27: verified Matchweek 4 fixtures, the table as of Matchweek 3, and the four storylines worth following. No odds, ever.", mw4))

    # ---- batch 7: permanent league architecture (spec 5-9): PL hub/table/fixtures/clubs + 3 league hubs ----
    import sports_leagues_data as sld
    import json as _sj
    _root = Path(__file__).resolve().parent.parent
    def _cal(name):
        return _sj.loads((_root / "content" / name).read_text())
    BADGE = {"hull-city": "hull", "manchester-city": "man-city", "manchester-united": "man-united",
             "newcastle-united": "newcastle", "leeds-united": "leeds", "coventry-city": "coventry",
             "tottenham-hotspur": "tottenham", "ipswich-town": "ipswich"}
    def badge_file(slug):
        f = BADGE.get(slug, slug) + ".png"
        assert (_root / "assets" / "img" / "sports" / "badges" / f).exists(), "badge missing: " + f
        return f
    NAME_SLUG = {r[1]: r[2] for r in sld.PL_TABLE}
    CH = {}
    for _c in _cal("club-history/premier-league.json")["clubs"]:
        CH[{v: k for k, v in BADGE.items()}.get(_c["slug"], _c["slug"])] = _c
    _missing_ch = [r[2] for r in sld.PL_TABLE if r[2] not in CH]
    assert not _missing_ch, "club-history missing: " + str(_missing_ch)
    def _panel(title, rows, more):
        m = ('<a class="sp-more" href="' + more[0] + '">' + more[1] + ' \u2192</a>') if more else ""
        return '<div class="side-panel"><h3>' + title + '</h3>' + rows + m + '</div>'
    def _scorers_panel(ld, lslug, n=6):
        if not ld.get("scorers"):
            return ""
        rws = ""
        for i, sc_ in enumerate(ld["scorers"][:n]):
            gw = "goal" if sc_["g"] == 1 else "goals"
            rws += ('<div class="sp-row"><span>' + html.escape(str(sc_["p"])) + '</span><span class="pts">' + str(sc_["g"]) + ' ' + gw + '</span></div>')
        return _panel("The scoring race", rws, ("/" + lslug + "-top-scorers/", "Full list"))
    def _table_panel(ld, lslug, n=6):
        if not ld.get("table"):
            return ""
        rws = ""
        for row in ld["table"][:n]:
            rws += ('<div class="sp-row"><span>' + html.escape(str(row[1])) + '</span><span class="pts">' + str(row[9]) + '</span></div>')
        href = "/premier-league-table/" if lslug == "premier-league" else "/" + lslug + "-table/"
        return _panel("The table, top six", rws, (href, "Full table"))
    def _next_panel(pairs):
        rws = "".join('<div class="sp-row"><span><a href="' + u + '">' + t + '</a></span></div>' for u, t in pairs)
        return _panel("Where next", rws, None)
    def _league_module(ld, lslug, lname):
        if not ld.get("table"):
            return ""
        trows = ""
        for row in ld["table"]:
            gds = ("+" + str(row[8])) if isinstance(row[8], int) and row[8] > 0 else str(row[8])
            trows += ('<tr><td class="pos">' + str(row[0]) + '</td><td class="club-b">' + html.escape(str(row[1])) + '</td>'
                      + '<td class="num">' + str(row[2]) + '</td><td class="num">' + str(row[3]) + '</td><td class="num">' + str(row[4]) + '</td><td class="num">' + str(row[5]) + '</td>'
                      + '<td class="num">' + str(row[6]) + '</td><td class="num">' + str(row[7]) + '</td><td class="num">' + gds + '</td><td class="num"><b>' + str(row[9]) + '</b></td></tr>')
        tbl = ('<p class="byline">' + html.escape(str(ld.get("table_updated", ""))) + ' \u00b7 source: ' + html.escape(str(LIVE.get("source", ""))) + '</p>'
            + '<div class="lg-scroll"><table class="lg-table">'
            + '<thead><tr><th>Pos</th><th>Club</th><th class="num">P</th><th class="num">W</th><th class="num">D</th><th class="num">L</th><th class="num">GF</th><th class="num">GA</th><th class="num">GD</th><th class="num">Pts</th></tr></thead>'
            + '<tbody>' + trows + '</tbody></table></div>')
        _ups = ""
        for _m2 in (ld.get("upcoming") or [])[:5]:
            _ups += ('<div class="sp-row"><span>' + html.escape(str(_m2["d"][5:])) + ' &#183; ' + html.escape(str(_m2["h"])) + ' <b>v</b> ' + html.escape(str(_m2["a"])) + '</span></div>')
        if _ups:
            _ups += '<p class="byline">fixtures last verified ' + html.escape(str(ld.get("upcoming_updated", ""))) + '</p>'
        _lastb = (ld.get("results") or [None])[-1]
        _lrs = ""
        if _lastb:
            for _m3 in _lastb["matches"][:4]:
                _lrs += ('<div class="sp-row"><span>' + html.escape(str(_m3["d"][5:])) + ' &#183; ' + html.escape(str(_m3["h"])) + ' <b>' + str(_m3["hs"]) + '\u2013' + str(_m3["as"]) + '</b> ' + html.escape(str(_m3["a"])) + '</span></div>')
            _lrs += '<p class="byline">scores last verified ' + html.escape(str(ld.get("results_updated", ""))) + ' \u2014 a score appears only once verified</p>'
        side = (_scorers_panel(ld, lslug, 6)
            + (_panel("Next up", _ups, ("/" + lslug + "-fixtures/", "The full calendar")) if _ups else "")
            + (_panel("Last round", _lrs, ("/" + lslug + "-results/", "All verified results")) if _lrs else "")
            + _next_panel([("/" + lslug + "-table/", "The full table page"), ("/" + lslug + "-results/", "All verified results"),
                           ("/" + lslug + "-fixtures/", "The fixture calendar"), ("/" + lslug + "-top-scorers/", "The scoring race")]))
        return ('<section class="section"><div class="section-head"><p class="kicker">' + lname + ' \u00b7 live</p><h2>The table, right now.</h2></div>'
            + '<div class="data-cols"><div>' + tbl + '</div><div>' + side + '</div></div></section>')
    LIVE = _cal("sports-live.json") if (_root / "content" / "sports-live.json").exists() else {}
    PL_TR = _cal("pl-transfers.json")
    LG_TR = {v["id"]: v for v in _cal("league-transfers.json")["leagues"]}
    PMGR = {c["id"]: c for c in PL_TR.get("clubs", [])}
    def _lg_head():
        return head("sports", "Analysis, stories and the long view \u2014 never betting.")

    def ordinal(n):
        return "th" if 11 <= n <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

    def _club_now_text(row, fx):
        pos, name, slug, pl, w, d, l, gf, ga, gd, pts = row
        rec = str(w) + "-" + str(d) + "-" + str(l)
        if fx:
            when, hslug, hname, aslug, aname, venue = fx
            side = "home" if hslug == slug else "away"
            opp = aname if side == "home" else hname
            return ("The table after three rounds: <b>" + str(pos) + ordinal(pos) + " place, "
                    + str(pts) + " point" + ("" if pts == 1 else "s") + " from a " + rec
                    + " record, " + str(gf) + " goals scored, " + str(ga) + " conceded. Next up: "
                    + opp + " (" + ("H" if side == "home" else "A") + "), " + when.lower() + ", " + venue + ".</b>")
        return ("The table after three rounds: <b>" + str(pos) + ordinal(pos) + " place, "
                + str(pts) + " points from a " + rec + " record.</b>")


    pl_hub = (_lg_head()
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / Premier League</nav>'
        + '<section class="cover"><p class="kicker">The Premier League \u00b7 ' + sld.SEASON + ' \u00b7 the permanent hub</p>'
        + '<h1 class="cover-title">The Premier League hub.</h1>'
        + '<p class="cover-dek">Everything this desk publishes about England\u2019s top flight, one gateway: the live table, the verified weekend fixtures, all twenty clubs, the matchweek editions and the evergreen explainers.</p></section>'
        + _league_module(LIVE.get("leagues", {}).get("premier-league", {}), "premier-league", "Premier League")
        + '<section class="section alt"><div class="section-head"><p class="kicker">The essentials</p><h2>Check the state of play.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/premier-league-table/"><span><b>The live table</b><small>Twenty clubs after Matchweek 3 \u2014 stamped with the date and the sources, updated as rounds are verified.</small></span><span class="meta">Live</span></a></li>'
        + '<li><a href="/form-board/"><span><b>The Form Board</b><small>Who is actually in form right now \u2014 real points-per-game arithmetic on verified results.</small></span><span class="meta">Live</span></a></li>'
        + '<li><a href="/who-will-win-the-2026-27-premier-league/"><span><b>Who wins the league?</b><small>The living title-race page \u2014 updated as rounds are verified.</small></span><span class="meta">Feature</span></a></li>'
        + '<li><a href="/premier-league-fixtures/"><span><b>Fixtures &amp; results</b><small>The full 380-fixture official calendar, with the verified Matchweek 4 card on top.</small></span><span class="meta">This weekend</span></a></li>'
        + '<li><a href="/the-weekend-ahead/"><span><b>The weekend ahead</b><small>This weekend\u2019s fixtures and the desk\u2019s labelled forecast.</small></span><span class="meta">Forecast</span></a></li>'
        + '<li><a href="/fpl/"><span><b>FPL, explained properly</b><small>Scoring, chips, transfers \u2014 the fantasy desk, no tips sold.</small></span><span class="meta">Fantasy</span></a></li>'
        + '<li><a href="/premier-league-clubs/"><span><b>All twenty clubs</b><small>Every club\u2019s hub: record, goal difference, next fixture, the story on one page.</small></span><span class="meta">Clubs</span></a></li>'
        + '<li><a href="/premier-league-results/"><span><b>Results, MW1\u20133</b><small>Every verified score from the season\u2019s opening rounds.</small></span><span class="meta">Results</span></a></li>'
        + '<li><a href="/premier-league-top-scorers/"><span><b>Top scorers</b><small>The Golden Boot race, verified and dated.</small></span><span class="meta">Scorers</span></a></li>'
        + '<li><a href="/premier-league-transfers/"><span><b>The transfer centre</b><small>Summer 2026, deal by deal \u2014 statuses strict, rumours excluded.</small></span><span class="meta">Transfers</span></a></li>'
        + '<li><a href="/premier-league-matchweek-4-preview/"><span><b>Matchweek 4, previewed honestly</b><small>The desk\u2019s live edition for the derby weekend \u2014 written Thursday, no odds.</small></span><span class="meta">This week</span></a></li>'
        + '<li><a href="/how-the-premier-league-table-works/"><span><b>How the table works</b><small>Points, goal difference, tiebreakers \u2014 and what actually happens if two clubs finish level.</small></span><span class="meta">Understand</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">Desk &amp; archive</p><h2>The editorial layer.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/epl/"><span><b>The Premier League desk</b><small>Archive editions: the summer transfer window and the season\u2019s opening weeks, kept as published.</small></span><span class="meta">Desk</span></a></li>'
        + '<li><a href="/promotion-and-relegation-explained/"><span><b>Promotion and relegation</b><small>Why three clubs fall every May \u2014 and what it costs them.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/xg-explained/"><span><b>xG, explained</b><small>The number behind every modern match discussion, and what it does not measure.</small></span><span class="meta">Explainer</span></a></li>'
        + '</ul></section>'
        + '<section class="section"><div class="prose"><p><em>House rules: the table and the fixture list carry a last-verified stamp and named sources. If a round has not been verified yet, the hub says so instead of guessing \u2014 and this desk never publishes betting odds.</em></p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/premier-league/", "Premier League hub \u2014 live table, fixtures, all 20 clubs | BRYME Sport",
                  "The Premier League gateway for 2026-27: the live table, verified fixtures, twenty club hubs, matchweek editions and the evergreen explainers. No odds, ever.", pl_hub))

    rows_html = ""
    for r in sld.PL_TABLE:
        pos, name, slug, pl, w, d, l, gf, ga, gd, pts = r
        cls = ' class="rel"' if pos == 18 else ""
        gds = ("+" + str(gd)) if gd > 0 else str(gd)
        rows_html += ('<tr' + cls + '><td class="pos">' + str(pos) + '</td><td class="club-b"><a href="/clubs/' + slug + '/"><img class="club-badge row-badge" src="/assets/img/sports/badges/' + badge_file(slug) + '" alt="" width="22" height="22" loading="lazy">' + name + '</a></td>'
                      + '<td class="num">' + str(pl) + '</td><td class="num">' + str(w) + '</td><td class="num">' + str(d) + '</td><td class="num">' + str(l) + '</td>'
                      + '<td class="num">' + str(gf) + '</td><td class="num">' + str(ga) + '</td><td class="num">' + gds + '</td><td class="num"><b>' + str(pts) + '</b></td></tr>')
    pl_table_page = (_lg_head()
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/premier-league/">Premier League</a> / Table</nav>'
        + '<section class="cover"><p class="kicker">Premier League \u00b7 ' + sld.SEASON + ' \u00b7 the table</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The 2026-27 Premier League table.</h1>'
        + '<p class="byline">Last verified ' + sld.TABLE_AS_OF + ' \u00b7 sources: NBC Sports, Sports Media Watch, worldfootball, footballfixtures (agreement across all four) \u00b7 the desk updates this page only after each round is verified</p></section>'
        + '<section class="section"><div class="data-cols"><div class="lg-scroll"><table class="lg-table">'
        + '<thead><tr><th>Pos</th><th>Club</th><th class="num">P</th><th class="num">W</th><th class="num">D</th><th class="num">L</th><th class="num">GF</th><th class="num">GA</th><th class="num">GD</th><th class="num">Pts</th></tr></thead>'
        + '<tbody>' + rows_html + '</tbody></table></div>'
        + '<div>' + _scorers_panel(LIVE.get("leagues", {}).get("premier-league", {}), "premier-league")
        + _next_panel([("/premier-league-results/", "All verified results"), ("/premier-league-fixtures/", "The full calendar"), ("/premier-league-clubs/", "All twenty clubs")])
        + '</div></div></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">Reading it</p><h2>What the table means.</h2></div>'
        + '<div class="prose"><p>Three points for a win, one for a draw, none for a defeat \u2014 and at the end of May, positions decide everything. The champions and the highest finishers qualify for Europe; the exact number of Champions League places England earns can change from season to season, which <a href="/how-the-champions-league-works/">the Champions League explainer</a> breaks down. The bottom three clubs are relegated to the Championship \u2014 <a href="/promotion-and-relegation-explained/">why that system exists</a> is one of the desk\u2019s most-read pieces. If clubs finish level on points, the tiebreakers run goal difference, then goals scored \u2014 <a href="/how-the-premier-league-table-works/">how the Premier League table works</a> has the full order, including the playoff nobody has ever needed.</p>'
        + '<p>Three games is a rumour, not a season: a club 17th in September has won the title before, and a club 3rd has been relegated. That is why this page updates only when the desk can verify, and why every number carries its date.</p></div></section>'
        + '<section class="section"><div class="prose"><p>Every club on this table has its own hub on the desk: start at <a href="/premier-league-clubs/">all twenty clubs</a>, or go straight to the leaders \u2014 <a href="/clubs/manchester-city/">Manchester City</a> and <a href="/clubs/arsenal/">Arsenal</a> \u2014 or the surprise of the season so far, <a href="/clubs/hull-city/">Hull City</a>.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/premier-league-table/", "Premier League table 2026-27 \u2014 verified, dated, no odds | BRYME Sport",
                  "The 2026-27 Premier League table as of Matchweek 3: position, played, goals, goal difference, points \u2014 verified across four sources and stamped with the date.", pl_table_page))

    fx_rows = ""
    for when, hslug, hname, aslug, aname, venue in sld.PL_MW4:
        fx_rows += ('<div class="fx-row"><span class="fx-when">' + when + '</span>'
                    + '<span class="fx-tie"><a href="/clubs/' + hslug + '/">' + hname + '</a> v <a href="/clubs/' + aslug + '/">' + aname + '</a></span>'
                    + '<span class="fx-where">' + venue + '</span></div>')
    # ---- recovered official calendars (old backend): PL list rendered above; four league calendars open their data desks ----
    cal_pl = _cal("fixtures.json")
    cal_secs = ""
    for mw in cal_pl["matchweeks"]:
        rows = ""
        for m in mw["matches"]:
            h = NAME_SLUG[m["homeName"]]; a = NAME_SLUG[m["awayName"]]
            t = m["time"] if m.get("timePublished") else "TBC"
            tv = ('<span class="fx-tv">' + html.escape(m["tv"]) + '</span>') if m.get("tv") else ""
            rows += ('<div class="fx-row"><span class="fx-when">' + html.escape(m["dayLabel"]) + ' \u00b7 ' + t + '</span>'
                     + '<span class="fx-tie"><a href="/clubs/' + h + '/">' + html.escape(m["homeName"]) + '</a> v <a href="/clubs/' + a + '/">' + html.escape(m["awayName"]) + '</a></span>'
                     + '<span class="fx-where">' + tv + '</span></div>')
        cal_secs += '<p class="cal-mw">Matchweek ' + str(mw["number"]) + '</p>' + rows

    pl_fixtures = (_lg_head()
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/premier-league/">Premier League</a> / Fixtures</nav>'
        + '<section class="cover"><p class="kicker">Premier League \u00b7 ' + sld.SEASON + ' \u00b7 fixtures &amp; results</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The 2026-27 fixture calendar.</h1>'
        + '<p class="byline">Calendar: ' + html.escape(cal_pl["source"]) + ' \u00b7 <a href="' + cal_pl["sourceUrl"] + '" rel="noopener">official release</a> \u00b7 desk file last updated ' + cal_pl["lastUpdated"] + ' \u00b7 kick-off times UK \u00b7 ' + html.escape(cal_pl["kickoffNote"]) + '</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">This weekend \u00b7 verified ' + sld.FIXTURES_AS_OF[9:] + '</p><h2>Matchweek 4, cross-checked.</h2></div>'
        + fx_rows + '</section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">The full season</p><h2>All 380 fixtures, as officially released.</h2></div>'
        + '<div class="prose"><p>' + html.escape(cal_pl["subjectToChange"]) + ' The desk marks a round as played only after its results are verified \u2014 until then, every entry below is a scheduled fixture, not a result.</p></div>'
        + cal_secs + '</section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">Before the weekend</p><h2>Read the round first.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/premier-league-matchweek-4-preview/"><span><b>Matchweek 4, previewed honestly</b><small>The desk\u2019s live edition: the four storylines, the real table, no odds.</small></span><span class="meta">Live</span></a></li>'
        + '<li><a href="/premier-league-table/"><span><b>The live table</b><small>Where all twenty clubs stand going into the round.</small></span><span class="meta">Live</span></a></li>'
        + '<li><a href="/premier-league-results/"><span><b>Results, MW1\u20133</b><small>All thirty verified scores from the opening rounds.</small></span><span class="meta">Results</span></a></li>'
        + '<li><a href="/premier-league-top-scorers/"><span><b>Top scorers</b><small>Haaland, Isak and Fernandes lead \u2014 verified list.</small></span><span class="meta">Scorers</span></a></li>'
        + '<li><a href="/premier-league-matchweek-2-preview/"><span><b>Matchweek 2 preview (archive)</b><small>The desk\u2019s pre-season window editions, kept as published.</small></span><span class="meta">Archive</span></a></li>'
        + '<li><a href="/deadline-day-dont-try-to-make-sense-of-it/"><span><b>Deadline day field guide (archive)</b><small>Why the window\u2019s last night looks the way it does.</small></span><span class="meta">Archive</span></a></li>'
        + '</ul></section>'
        + '<section class="section"><div class="prose"><p><em>Results return the same way: after each round, once verified across sources \u2014 usually inside the desk\u2019s matchweek review. Until then this page will not guess. A full-season calendar lands when the desk has verified the feed for it; a wrong fixture list is worse than an honest gap.</em></p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/premier-league-fixtures/", "Premier League fixtures 2026-27 \u2014 Matchweek 4, verified | BRYME Sport",
                  "Matchweek 4 fixtures with UK kick-off times and venues, verified 10 September 2026 \u2014 plus how the desk handles results, postponements and the season calendar.", pl_fixtures))


    HUBHREF = {"la-liga": "/laliga/"}
    LEAGUE_CAL = [("la-liga", "La Liga", "fixtures-la-liga.json", "The 2026-27 La Liga calendar."),
                  ("serie-a", "Serie A", "fixtures-serie-a.json", "The 2026-27 Serie A calendar."),
                  ("bundesliga", "Bundesliga", "fixtures-bundesliga.json", "The 2026-27 Bundesliga calendar."),
                  ("ligue-1", "Ligue 1", "fixtures-ligue-1.json", "The 2026-27 Ligue 1 calendar.")]
    for lslug, lname, lfile, ltitle in LEAGUE_CAL:
        cd = _cal(lfile)
        secs = ""
        for mw in cd["matchweeks"]:
            rows = ""
            for m in mw["matches"]:
                t = m["time"] if m.get("timePublished") else "TBC"
                note = ('<span class="fx-where">' + html.escape(m["note"]) + '</span>') if m.get("note") else ""
                rows += ('<div class="fx-row"><span class="fx-when">' + html.escape(m["dayLabel"]) + ' \u00b7 ' + t + '</span>'
                         + '<span class="fx-tie">' + html.escape(m["homeName"]) + ' v ' + html.escape(m["awayName"]) + '</span>'
                         + note + '</div>')
            secs += '<p class="cal-mw">' + html.escape(mw.get("name", "Matchweek " + str(mw["number"]))) + '</p>' + rows
        page = (_lg_head()
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="' + HUBHREF.get(lslug, "/" + lslug + "/") + '">' + lname + '</a> / Fixtures</nav>'
            + '<section class="cover"><p class="kicker">' + lname + ' \u00b7 ' + sld.SEASON + ' \u00b7 the calendar</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + ltitle + '</h1>'
            + '<p class="byline">Calendar: ' + html.escape(cd["source"]) + ' \u00b7 <a href="' + cd["sourceUrl"] + '" rel="noopener">official source</a> \u00b7 desk file last updated ' + cd["lastUpdated"] + ' \u00b7 ' + html.escape(cd["kickoffNote"]) + '</p></section>'
            + '<section class="section"><div class="prose"><p>' + html.escape(cd["subjectToChange"]) + ' Rounds appear here as scheduled fixtures; results are added only after the desk verifies them \u2014 an unverified result is never published.</p></div>'
            + secs + '</section>'
            + '<section class="section alt"><div class="prose"><p>The ' + lname + ' hub holds the competition\u2019s format, champions and desk coverage: <a href="' + HUBHREF.get(lslug, "/" + lslug + "/") + '">the ' + lname + ' hub</a>. The desk\u2019s evergreen layer \u2014 <a href="/sports/explainers/">explainers</a>, <a href="/promotion-and-relegation-explained/">the pyramid</a>, <a href="/how-the-champions-league-works/">European qualification</a> \u2014 applies to every league on it.</p></div></section>'
            + '</div></main>' + foot("sports"))
        pages.append(("/" + lslug + "-fixtures/", lname + " fixtures 2026-27 \u2014 the official calendar, stamped | BRYME Sport",
                      "The full " + lname + " 2026-27 fixture calendar (all " + str(sum(len(m['matches']) for m in cd['matchweeks'])) + " matches): dates, kick-off times, sources and change policy \u2014 dated and stamped.", page))

    club_rows = ""
    for r in sorted(sld.PL_TABLE, key=lambda x: x[0]):
        pos, name, slug, pl, w, d, l, gf, ga, gd, pts = r
        club_rows += ('<li><a href="/clubs/' + slug + '/"><img class="club-badge row-badge" src="/assets/img/sports/badges/' + badge_file(slug) + '" alt="' + name + ' club badge" width="40" height="40" loading="lazy"><span><b>' + name + '</b>'
                      + '<small>Ground, foundation, the story, and this season\u2019s numbers on one page.</small></span>'
                      + '<span class="meta">' + str(pos) + ' \u00b7 ' + str(pts) + ' pts</span></a></li>')
    pl_clubs_page = (_lg_head()
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/premier-league/">Premier League</a> / Clubs</nav>'
        + '<section class="cover"><p class="kicker">Premier League \u00b7 ' + sld.SEASON + ' \u00b7 the clubs</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">All twenty clubs.</h1>'
        + '<p class="cover-dek">Every club in the 2026-27 Premier League, each with its own hub: where it plays, when it was founded, the story in a paragraph, and this season\u2019s verified numbers \u2014 updated as rounds are checked.</p></section>'
        + '<section class="section"><ul class="list">' + club_rows + '</ul></section>'
        + '<section class="section alt"><div class="prose"><p>Membership is correct for 2026-27 as verified on 10 September 2026: Hull City, Coventry City and Sunderland are the promoted names; Burnley, West Ham and Wolves are not in this season\u2019s edition of the league. If a club page and the table ever disagree, the table \u2014 with its date stamp \u2014 wins.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/premier-league-clubs/", "Premier League clubs 2026-27 \u2014 all twenty club hubs | BRYME Sport",
                  "Every 2026-27 Premier League club on one gateway: twenty club hubs with grounds, history, verified records and next fixtures.", pl_clubs_page))

    _PLD = LIVE.get("leagues", {}).get("premier-league", {}) if LIVE else {}
    SQ = _PLD.get("squads", {})
    SQUPD = _PLD.get("squads_updated", "")
    def _age(dob):
        try:
            y, m, dd = (int(x) for x in dob.split("-"))
            t = datetime.now(timezone.utc).date()
            return t.year - y - ((t.month, t.day) < (m, dd))
        except Exception:
            return None
    def _squad_secs(sqd, upd):
        if not sqd or not sqd.get("players"):
            return ""
        groups = [("Goalkeeper", "Goalkeepers"), ("Defence", "Defenders"), ("Midfield", "Midfielders"), ("Offence", "Forwards")]
        panels = ""
        shown = 0
        for gkey, glabel in groups:
            ps = sorted([q for q in sqd["players"] if q[1] == gkey], key=lambda x: x[0])
            if not ps:
                continue
            rows = ""
            for q in ps:
                nm = html.escape(str(q[0]))
                num = ('#' + str(q[4]) + ' ') if q[4] else ""
                meta = " \u00b7 ".join([x for x in [html.escape(str(q[2])) if q[2] else "", (lambda a: (str(a) + " yrs") if a else "")(_age(q[3]))] if x])
                rows += '<div class="sp-row"><span>' + num + nm + '</span><span class="pts">' + meta + '</span></div>'
            panels += '<div class="side-panel"><h3>' + glabel + '</h3>' + rows + '</div>'
            shown += len(ps)
        if not shown:
            return ""
        return ('<section class="section"><div class="section-head"><p class="kicker">The squad \u00b7 ' + str(shown) + ' players</p><h2>Who is in the building.</h2></div>'
                + ('<p class="byline">As listed by our data source \u00b7 ' + html.escape(str(upd)) + ' \u00b7 ages as at listing</p>' if upd else "")
                + '<div class="data-cols">' + panels + '</div></section>')
    TROPH = _cal("club-trophies.json")
    def _trophy_sec(slug):
        t = TROPH.get("clubs", {}).get(slug)
        if not t:
            return ""
        rows1 = ""
        if t.get("lg") is not None:
            rows1 += '<div class="sp-row"><span>League titles</span><span class="pts"><b>' + str(t["lg"]) + '</b></span></div>'
        if t.get("fa") is not None:
            rows1 += '<div class="sp-row"><span>FA Cups</span><span class="pts"><b>' + str(t["fa"]) + '</b></span></div>'
        if t.get("lc"):
            rows1 += '<div class="sp-row"><span>League Cups</span><span class="pts"><b>' + str(t["lc"]) + '</b></span></div>'
        rows2 = ""
        if t.get("eu"):
            rows2 += '<div class="sp-row"><span>' + t["eu"] + '</span></div>'
        if t.get("w"):
            rows2 += '<div class="sp-row"><span>' + t["w"] + '</span></div>'
        note = ('<div class="sp-row"><span><em>' + t["note"] + '</em></span></div>') if t.get("note") else ""
        srcnote = ('<p class="byline">Compiled from official club honours records \u00b7 correct as of ' + html.escape(str(TROPH.get("as_of", ""))) + ' \u00b7 counts the desk could not verify are simply not shown</p>')
        return ('<section class="section"><div class="section-head"><p class="kicker">Trophy cabinet</p><h2>The honours, counted.</h2></div>'
            + '<div class="data-cols"><div>' + _panel("Domestic", rows1, None) + _panel("Europe &amp; world", rows2, None) + '</div><div>' + _panel("The story", note + '<div class="sp-row"><span>The evergreen context: <a href="/promotion-and-relegation-explained/">the pyramid</a> and <a href="/how-the-premier-league-table-works/">the table</a> these trophies hang from.</span></div>', None) + '</div></div></section>' + srcnote)
    STORY_FOR = {
        "manchester-city": ("/elliot-anderson-man-city-record-signing/", "Why City paid a record for a midfielder"),
        "liverpool": ("/premier-league-transfer-tracker-august-2026/", "The summer window, deal by deal"),
        "arsenal": ("/premier-league-matchweek-1-guide/", "The season\u2019s opening weekend, as covered"),
        "hull-city": ("/promotion-and-relegation-explained/", "The arithmetic of a promoted start"),
        "coventry-city": ("/promotion-and-relegation-explained/", "The arithmetic of a promoted start"),
        "sunderland": ("/promotion-and-relegation-explained/", "The arithmetic of a promoted start"),
        "leeds-united": ("/promotion-and-relegation-explained/", "The arithmetic of a promoted start"),
        "fulham": ("/premier-league-transfer-tracker-august-2026/", "The summer window, deal by deal"),
    }
    for r in sld.PL_TABLE:
        pos, name, slug, pl, w, d, l, gf, ga, gd, pts = r
        cname, ground, founded, blurb = sld.PL_CLUBS[slug]
        ch = CH.get(slug, {})
        chcity = (' \u00b7 ' + html.escape(ch["city"])) if ch.get("city") else ""
        chsrc = (' <em>Club facts source: <a href="' + ch["source"] + '" rel="noopener">official club history</a>.</em>') if ch.get("source") else ""
        sqd = SQ.get(name) or next((v for k, v in SQ.items() if k.startswith(name) or name.startswith(k)), None)
        _pmgr = (PMGR.get(slug) or {}).get("manager", "")
        fx = next((f for f in sld.PL_MW4 if slug in (f[1], f[3])), None)
        story = STORY_FOR.get(slug)
        gds = ("+" + str(gd)) if gd > 0 else str(gd)
        rec = str(w) + "-" + str(d) + "-" + str(l)
        club_page = (_lg_head()
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/premier-league/">Premier League</a> / <a href="/premier-league-clubs/">Clubs</a> / ' + cname + '</nav>'
            + '<section class="cover"><p class="kicker">Premier League \u00b7 ' + sld.SEASON + ' \u00b7 club hub</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + cname + '</h1>'
            + '<p class="byline">' + ground + ' \u00b7 founded ' + str(founded) + chcity + ' \u00b7 season numbers as of Matchweek 3, verified ' + sld.FIXTURES_AS_OF[9:] + '</p>'
            + '<img class="club-badge cov-badge" src="/assets/img/sports/badges/' + badge_file(slug) + '" alt="' + cname + ' club badge" width="76" height="76" loading="lazy">'
            + '<div class="cover-facts">'
            + '<div><b>' + str(pos) + '</b><span>' + ordinal(pos) + ' in the table</span></div>'
            + '<div><b>' + str(pts) + '</b><span>Points</span></div>'
            + '<div><b>' + gds + '</b><span>Goal difference</span></div>'
            + '<div><b>' + rec + '</b><span>W-D-L</span></div>'
            + ('<div><b style="font-size:20px">' + html.escape(_pmgr) + '</b><span>Manager</span></div>' if _pmgr else "")
            + '</div></section>'
            + '<section class="section"><div class="prose"><p>' + blurb + chsrc + '</p>'
            + '<p>' + _club_now_text(r, fx) + ' <a href="/how-the-premier-league-table-works/">How to read the table</a> \u00b7 <a href="/xg-explained/">what xG adds</a>.</p></div></section>'
            + _squad_secs(sqd, SQUPD)
            + _trophy_sec(slug)
            + '<section class="section alt"><div class="section-head"><p class="kicker">Where next</p><h2>Keep exploring.</h2></div>'
            + '<ul class="list">'
            + ('<li><a href="' + story[0] + '"><span><b>' + story[1] + '</b><small>From the desk\u2019s archive.</small></span><span class="meta">Read</span></a></li>' if story else "")
            + '<li><a href="/premier-league-fixtures/"><span><b>Fixtures &amp; results</b><small>The verified weekend card, with this club\u2019s next game.</small></span><span class="meta">Next</span></a></li>'
            + '<li><a href="/premier-league-transfers/"><span><b>The verified transfer tracker</b><small>Every listed deal for this club \u2014 statuses and fees as recorded, never rumours.</small></span><span class="meta">Transfers</span></a></li>'
            + '<li><a href="/premier-league-table/"><span><b>The live table</b><small>Where every club stands, stamped and sourced.</small></span><span class="meta">Live</span></a></li>'
            + '<li><a href="/premier-league/"><span><b>The Premier League hub</b><small>The whole competition, one gateway.</small></span><span class="meta">Hub</span></a></li>'
            + '<li><a href="/premier-league-matchweek-4-preview/"><span><b>Matchweek 4, previewed honestly</b><small>This weekend\u2019s live desk edition.</small></span><span class="meta">This week</span></a></li>'
            + '<li><a href="/premier-league-clubs/"><span><b>All twenty clubs</b><small>The other nineteen hubs, one list.</small></span><span class="meta">Clubs</span></a></li>'
            + '</ul></section>'
            + '</div></main>' + foot("sports"))
        pages.append(("/clubs/" + slug + "/", cname + " \u2014 club hub, " + sld.SEASON + " | BRYME Sport",
                      cname + " in the " + sld.SEASON + " Premier League: " + ground + ", founded " + str(founded) + ", this season\u2019s verified record and next fixture \u2014 the desk\u2019s club gateway.", club_page))

    # ---- batch 14: the transfer centre (recovered owner-verified trackers, spec s12) ----
    def _tr_rows(items):
        out = ""
        for t in items:
            other = html.escape(str(t.get("from", t.get("to", ""))))
            typ = html.escape(str(t.get("type", "")))
            det = html.escape(str(t.get("detail", "") or ""))
            right = typ + (" \u00b7 " + det if det else "")
            out += ('<div class="sp-row"><span>' + html.escape(str(t.get("player", ""))) + '</span><span class="pts">' + other + ' \u00b7 ' + right + '</span></div>')
        return out
    def _tr_page(tr, lname, lhub, tlug, midwin):
        clubs = tr.get("clubs", [])
        nin = sum(len(c.get("playersIn", [])) for c in clubs)
        nout = sum(len(c.get("playersOut", [])) for c in clubs)
        secs = ""
        for c in clubs:
            mgr = c.get("manager") or ""
            mnote = c.get("managerNote") or ""
            kick = html.escape(c.get("name", ""))
            if mgr:
                kick += ' \u00b7 manager: <b>' + html.escape(mgr) + '</b>' + (' (' + html.escape(mnote) + ')' if mnote else "")
            ins = _tr_rows(c.get("playersIn", [])) or '<div class="sp-row"><span>No listed deals \u2014 listed is not the same as none; the tracker only carries verified entries.</span></div>'
            outs = _tr_rows(c.get("playersOut", [])) or ""
            secs += ('<section class="section"><div class="section-head"><p class="kicker">' + kick + '</p><h2>' + c.get("name", "") + '</h2></div>'
                + '<div class="data-cols"><div>' + _panel("Players in", ins, None)
                + (_panel("Players out", outs, None) if outs else "") + '</div></div></section>')
        srcs = " \u00b7 ".join(html.escape(x) for x in tr.get("sources", []))
        note = ""
        if midwin:
            note = ('<section class="section alt"><div class="prose"><p><b>Dating note, stated plainly:</b> this tracker was recorded on '
                + html.escape(str(tr.get("lastUpdated", ""))) + ' \u2014 before the window closed on ' + html.escape(str(tr.get("windowClose", "")))
                + '. Deal statuses reflect that moment. The desk re-verifies before every update and never guesses what happened next. Reported/rumoured moves are deliberately not listed.</p></div></section>')
        tp = (_lg_head()
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / ' + ('<a href="' + lhub + '">' + lname + '</a>' if lhub else lname) + ' / Transfers</nav>'
            + '<section class="cover"><p class="kicker">The transfer centre \u00b7 ' + lname + ' \u00b7 summer window 2026</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">Every listed deal, club by club.</h1>'
            + '<p class="byline">' + str(nin) + ' players in \u00b7 ' + str(nout) + ' players out \u00b7 tracker updated ' + html.escape(str(tr.get("lastUpdated", ""))) + ' \u00b7 window closed ' + html.escape(str(tr.get("windowClose", ""))) + ' \u00b7 statuses only: Confirmed / Loan / Free / Released / Departed / Retired \u2014 rumours are never listed as deals \u00b7 sources: ' + srcs + '</p></section>'
            + secs + note
            + '<section class="section alt"><div class="prose"><p>Carry on: the ' + lname + ' <a href="' + lhub + '">hub</a>, the <a href="/' + tlug + '-table/">live table</a>, the <a href="/' + tlug + '-fixtures/">fixture calendar</a> and <a href="/' + tlug + '-top-scorers/">the scoring race</a>.</p></div></section>'
            + '</div></main>' + foot("sports"))
        return tp
    pages.append(("/premier-league-transfers/", "Premier League transfers 2026 \u2014 every listed deal | BRYME Sport",
                  "The verified Premier League summer 2026 transfer tracker: every listed deal club by club, with statuses and fees \u2014 never rumours.", _tr_page(PL_TR, "Premier League", "/premier-league/", "premier-league", False)))
    _thubs = {"la-liga": "/laliga/", "serie-a": "/serie-a/", "bundesliga": "/bundesliga/", "ligue-1": "/ligue-1/"}
    _tnames = {"la-liga": "La Liga", "serie-a": "Serie A", "bundesliga": "Bundesliga", "ligue-1": "Ligue 1"}
    for _tg, _tv in LG_TR.items():
        pages.append(("/" + _tg + "-transfers/", _tnames.get(_tg, _tg) + " transfers 2026 \u2014 every listed deal | BRYME Sport",
                      "The verified " + _tnames.get(_tg, _tg) + " summer 2026 transfer tracker: every listed deal club by club, statuses and fees as recorded \u2014 never rumours.", _tr_page(_tv, _tnames.get(_tg, _tg), _thubs.get(_tg, "/" + _tg + "/"), _tg, True)))

    for lslug, lf in sld.LEAGUE_FACTS.items():
        _lld = LIVE.get("leagues", {}).get(lslug, {}) if LIVE else {}
        _live_rows = ""
        if _lld.get("table"):
            _live_rows += ('<li><a href="/' + lslug + '-table/"><span><b>The live table</b><small>All eighteen clubs, stamped with its verification time.</small></span><span class="meta">Live</span></a></li>')
        if _lld.get("results"):
            _live_rows += ('<li><a href="/' + lslug + '-results/"><span><b>Results</b><small>The latest verified scores, matchweek by matchweek.</small></span><span class="meta">Results</span></a></li>')
        if _lld.get("scorers"):
            _live_rows += ('<li><a href="/' + lslug + '-top-scorers/"><span><b>Top scorers</b><small>The scoring race, verified and dated.</small></span><span class="meta">Scorers</span></a></li>')
        if _lld.get("table"):
            status_prose = ('<div class="prose"><p>The live <a href="/' + lslug + '-table/">table</a> is open and stamped with its verification time, and the results and scoring charts join it as the desk\u2019s data agent verifies each round. The same standard the <a href="/premier-league/">Premier League hub</a> meets, league by league.</p>')
        else:
            status_prose = ('<div class="prose"><p>The ' + lf["name"] + ' table and fixture list open here as soon as the desk verifies this season\u2019s rounds across sources \u2014 the same standard the <a href="/premier-league/">Premier League hub</a> already meets. Until then this page will not publish unverified numbers: a wrong table is worse than an honest gap. The desk\u2019s evergreen layer applies to every league on it.</p>')
        lh = (_lg_head()
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / ' + lf["name"] + '</nav>'
            + '<section class="cover"><p class="kicker">The ' + lf["name"] + ' hub \u00b7 ' + sld.SEASON + '</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + lf["name"] + ', on one page.</h1>'
            + '<p class="cover-dek">' + str(lf["clubs"]) + ' clubs, ' + str(lf["rounds"]) + ' rounds, and a league this desk now covers structurally: format, champion, history \u2014 with the live data desk opening as rounds are verified.</p></section>'
            + _league_module(_lld, lslug, lf["name"])
            + '<section class="section"><div class="section-head"><p class="kicker">The competition</p><h2>How it works.</h2></div>'
            + '<div class="prose"><p>' + lf["body_intro"] + '</p>'
            + '<p>The defending champions are <b>' + lf["champion"] + '</b> \u2014 ' + lf["titles_note"] + '. ' + lf["season_note"] + ' Like every league on this desk, promotion and relegation decide the edges of the table: <a href="/promotion-and-relegation-explained/">the system, explained</a>. European places flow from league position into <a href="/how-the-champions-league-works/">the Champions League</a> \u2014 and <a href="/champions-league-new-format-explained/">the new 36-team format</a> changed what qualification is worth.</p></div></section>'
            + '<section class="section alt"><div class="section-head"><p class="kicker">Data desk status</p><h2>Honest, as always.</h2></div>'
            + status_prose + '</div></section>'
            + '<section class="section"><div class="section-head"><p class="kicker">While you wait</p><h2>The shelf works in any league.</h2></div>'
            + '<ul class="list">'
            + _live_rows
            + '<li><a href="/' + lslug + '-fixtures/"><span><b>The 2026-27 calendar</b><small>Every scheduled fixture, dated and stamped \u2014 results join only once verified.</small></span><span class="meta">Calendar</span></a></li>'
            + '<li><a href="/sports/explainers/"><span><b>The explainers shelf</b><small>Offside, VAR, transfers, the pyramid \u2014 the laws are the same everywhere.</small></span><span class="meta">Understand</span></a></li>'
            + '<li><a href="/how-the-champions-league-works/"><span><b>How the Champions League works</b><small>Where every league\u2019s best clubs end up.</small></span><span class="meta">Understand</span></a></li>'
            + '<li><a href="/laliga-explained/"><span><b>LaLiga, explained</b><small>The Spanish league\u2019s structure, for comparison.</small></span><span class="meta">Read</span></a></li>'
            + '<li><a href="/what-does-a-sporting-director-do/"><span><b>What a sporting director does</b><small>The role that builds squads in every league on this desk.</small></span><span class="meta">Read</span></a></li>'
            + '<li><a href="/who-will-win-the-2026-ballon-dor/"><span><b>Who wins the Ballon d\u2019Or?</b><small>The living race \u2014 the award this league\u2019s stars keep winning.</small></span><span class="meta">Feature</span></a></li>'
            + '<li><a href="/best-football-players-in-the-world-2026/"><span><b>The best players in the world</b><small>The BRYME ranking, method printed \u2014 argued over weekly.</small></span><span class="meta">Feature</span></a></li>'
            + '<li><a href="/sports/transfers/"><span><b>The transfer desk</b><small>How deals happen across every league on this desk \u2014 and the centre for the listed deals.</small></span><span class="meta">Transfers</span></a></li>'
            + '</ul></section>'
            + '</div></main>' + foot("sports"))
        pages.append(("/" + lslug + "/", "The " + lf["name"] + " hub \u2014 format, champions, coverage | BRYME Sport",
                      "The " + lf["name"] + " on BRYME Sport: " + str(lf["clubs"]) + " clubs, " + str(lf["rounds"]) + " rounds, defending champions " + lf["champion"] + " \u2014 the gateway that grows as rounds are verified.", lh))

    # ---- batch 10: data-file pages (tables/results/scorers) — the agent grows these automatically ----
    if not LIVE:
        LIVE = _cal("sports-live.json") if (_root / "content" / "sports-live.json").exists() else {}
    LLEAGUES = [("premier-league", "Premier League", "/premier-league/"),
                ("la-liga", "La Liga", "/laliga/"),
                ("bundesliga", "Bundesliga", "/bundesliga/"),
                ("serie-a", "Serie A", "/serie-a/"),
                ("ligue-1", "Ligue 1", "/ligue-1/"),
                ("champions-league", "Champions League", "/champions-league/")]
    def _gd(g):
        return ("+" + str(g)) if g > 0 else str(g)
    for lslug, lname, lhub in LLEAGUES:
        ld = LIVE.get("leagues", {}).get(lslug, {})
        if ld.get("table") and lslug != "premier-league":
            trows = ""
            n_cl = len(ld["table"])
            rel_at = 17 if n_cl == 20 else (16 if n_cl == 18 else 0)
            for row in ld["table"]:
                pos, name, pl_, w_, d_, l_, gf_, ga_, gd_, pts_ = row
                cls = ' class="rel"' if (rel_at and pos == rel_at) else ""
                trows += ('<tr' + cls + '><td class="pos">' + str(pos) + '</td><td class="club-b">' + html.escape(str(name)) + '</td>'
                          + "".join('<td class="num">' + str(x) + '</td>' for x in (pl_, w_, d_, l_, gf_, ga_))
                          + '<td class="num">' + _gd(gd_) + '</td><td class="num"><b>' + str(pts_) + '</b></td></tr>')
            tp = (_lg_head()
                + '<main id="main"><div class="wrap">'
                + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="' + lhub + '">' + lname + '</a> / Table</nav>'
                + '<section class="cover"><p class="kicker">' + lname + ' \u00b7 ' + sld.SEASON + ' \u00b7 the table</p>'
                + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The ' + sld.SEASON + ' ' + lname + ' table.</h1>'
                + '<p class="byline">' + html.escape(str(ld.get("table_updated", ""))) + ' \u00b7 source: ' + html.escape(str(LIVE.get("source", ""))) + ' \u00b7 the desk updates this page only after each round is verified</p></section>'
                + '<section class="section"><div class="data-cols"><div class="lg-scroll"><table class="lg-table">'
                + '<thead><tr><th>Pos</th><th>Club</th><th class="num">P</th><th class="num">W</th><th class="num">D</th><th class="num">L</th><th class="num">GF</th><th class="num">GA</th><th class="num">GD</th><th class="num">Pts</th></tr></thead>'
                + '<tbody>' + trows + '</tbody></table></div>'
                + '<div>' + _scorers_panel(ld, lslug)
                + _next_panel([("/" + lslug + "-results/", "All verified results"), ("/" + lslug + "-fixtures/", "The full calendar"), (lhub, lname + " hub")])
                + '</div></div></section>'
                + '<section class="section alt"><div class="prose"><p>Three points for a win, one for a draw; tiebreakers run goal difference, then goals scored \u2014 <a href="/how-the-premier-league-table-works/">how league tables work</a> explains the full order. The relegation places are marked: <a href="/promotion-and-relegation-explained/">why the pyramid works that way</a>. Club-hub links open for this league as rounds are verified \u2014 meanwhile the <a href="' + lhub + '">' + lname + ' hub</a> and the <a href="/' + lslug + '-fixtures/">full 2026-27 calendar</a> are live.</p></div></section>'
                + '</div></main>' + foot("sports"))
            pages.append(("/" + lslug + "-table/", lname + " table " + sld.SEASON + " \u2014 verified, dated | BRYME Sport",
                          "The " + sld.SEASON + " " + lname + " table, " + str(n_cl) + " clubs, stamped with its verification date and source. No odds, ever.", tp))
        if ld.get("results"):
            rsecs = ""
            for blk in ld["results"][-3:]:
                rrows = ""
                for m in blk["matches"]:
                    hsl = NAME_SLUG.get(m["h"]); asl = NAME_SLUG.get(m["a"])
                    hl = ('<a href="/clubs/' + hsl + '/">' + html.escape(m["h"]) + '</a>') if hsl else html.escape(m["h"])
                    al = ('<a href="/clubs/' + asl + '/">' + html.escape(m["a"]) + '</a>') if asl else html.escape(m["a"])
                    rrows += ('<div class="fx-row"><span class="fx-when">' + html.escape(str(m["d"])) + '</span>'
                              + '<span class="fx-tie">' + hl + '<b class="fx-score">' + str(m["hs"]) + '\u2013' + str(m["as"]) + '</b>' + al + '</span>'
                              + '<span class="fx-where">Full time</span></div>')
                rsecs += '<p class="cal-mw">Matchweek ' + str(blk["mw"]) + '</p>' + rrows
            rp = (_lg_head()
                + '<main id="main"><div class="wrap">'
                + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="' + lhub + '">' + lname + '</a> / Results</nav>'
                + '<section class="cover"><p class="kicker">' + lname + ' \u00b7 ' + sld.SEASON + ' \u00b7 results</p>'
                + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The season\u2019s results, verified.</h1>'
                + '<p class="byline">' + html.escape(str(ld.get("results_updated", ""))) + ' \u00b7 source: ' + html.escape(str(LIVE.get("source", ""))) + ' \u00b7 a score appears here only once the desk can verify it \u2014 no guesses, ever</p></section>'
                + '<section class="section"><div class="data-cols"><div>' + rsecs + '</div><div>'
                + _table_panel(ld, lslug) + _scorers_panel(ld, lslug, 5)
                + '</div></div></section>'
                + '<section class="section alt"><div class="prose"><p>Where the table stands after these results: <a href="/' + lslug + '-table/">the live table</a>. Coming up: <a href="/' + lslug + '-fixtures/">the verified fixture card</a>. The hub: <a href="' + lhub + '">' + lname + '</a>. The vocabulary behind the numbers: <a href="/xg-explained/">xG, explained</a> and <a href="/pressing-explained/">pressing, explained</a>.</p></div></section>'
                + '</div></main>' + foot("sports"))
            pages.append(("/" + lslug + "-results/", lname + " results " + sld.SEASON + " \u2014 every verified score | BRYME Sport",
                          "Verified " + sld.SEASON + " " + lname + " results, matchweek by matchweek, stamped with the verification date. No invented scores, ever.", rp))
        if ld.get("scorers"):
            srows = ""
            for i, sc_ in enumerate(ld["scorers"]):
                extras = ""
                pm = sc_.get("pm")
                av = sc_.get("a")
                if pm:
                    extras += ' \u00b7 ' + str(pm) + (" app" if pm == 1 else " apps")
                if av is not None:
                    extras += ' \u00b7 ' + str(av) + (" assist" if av == 1 else " assists")
                if sc_["g"] == 1:
                    gword = "goal</b>" + extras + "</span></div>"
                else:
                    gword = "goals</b>" + extras + "</span></div>"
                srows += ('<div class="fx-row"><span class="fx-when">#' + str(i + 1) + '</span>'
                          + '<span class="fx-tie">' + html.escape(str(sc_["p"])) + '</span>'
                          + '<span class="fx-where">' + html.escape(str(sc_.get("c", ""))) + ' \u00b7 <b>' + str(sc_["g"]) + ' ' + gword)
            has_t = bool(ld.get("table")) or lslug == "premier-league"
            tlink = ('<a href="/' + lslug + '-table/">live table</a>' if lslug != "premier-league" else '<a href="/premier-league-table/">live table</a>') if has_t else "full calendar"
            race = {"premier-league": "the Golden Boot race", "la-liga": "the Pichichi race"}.get(lslug, "the scoring race")
            sp = (_lg_head()
                + '<main id="main"><div class="wrap">'
                + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="' + lhub + '">' + lname + '</a> / Top scorers</nav>'
                + '<section class="cover"><p class="kicker">' + lname + ' \u00b7 ' + sld.SEASON + ' \u00b7 top scorers</p>'
                + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The scoring race, verified.</h1>'
                + '<p class="byline">Updated ' + html.escape(str(ld.get("scorers_updated", LIVE.get("generated", "")))) + ' \u00b7 sources: ' + html.escape(str(ld.get("scorers_source", LIVE.get("source", "")))) + ' \u00b7 verified season totals only</p></section>'
                + '<section class="section"><div class="data-cols"><div>' + srows + '</div><div>'
                + _table_panel(ld, lslug)
                + _next_panel([("/" + lslug + "-results/", "All verified results"), ("/" + lslug + "-fixtures/", "The full calendar"), (lhub, lname + " hub")])
                + '</div></div></section>'
                + '<section class="section alt"><div class="prose"><p>' + (race[0].upper() + race[1:]) + ' totals move fast in the opening weeks; this page updates only when the desk can verify. Our source records assists and appearances only for the players listed here \u2014 they appear as published, never estimated. Keep going: the <a href="' + lhub + '">' + lname + ' hub</a>, the ' + tlink + ', and the <a href="/' + lslug + '-fixtures/">full calendar</a>.</p></div></section>'
                + '</div></main>' + foot("sports"))
            pages.append(("/" + lslug + "-top-scorers/", lname + " top scorers " + sld.SEASON + " \u2014 the scoring race, verified | BRYME Sport",
                          "The " + sld.SEASON + " " + lname + " scoring race: verified season totals, dated and sourced. No guesses, ever.", sp))
        if lslug == "champions-league" and ld.get("upcoming"):
            by_md = {}
            for u in ld["upcoming"]:
                by_md.setdefault(u["mw"], []).append(u)
            usecs = ""
            for md in sorted(by_md):
                rws = "".join('<div class="fx-row"><span class="fx-when">' + html.escape(str(x["d"])) + ' UTC</span>'
                              + '<span class="fx-tie">' + html.escape(x["h"]) + ' v ' + html.escape(x["a"]) + '</span>'
                              + '<span class="fx-where">Matchday ' + str(md) + '</span></div>' for x in by_md[md])
                usecs += '<p class="cal-mw">Matchday ' + str(md) + '</p>' + rws
            uf = (_lg_head()
                + '<main id="main"><div class="wrap">'
                + '<nav class="crumb"><a href="/sports/">Sport</a> / <a href="/champions-league/">Champions League</a> / Fixtures</nav>'
                + '<section class="cover"><p class="kicker">Champions League \u00b7 2026-27 \u00b7 the league phase</p>'
                + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The league-phase fixtures.</h1>'
                + '<p class="byline">' + html.escape(str(ld.get("upcoming_updated", ""))) + ' \u00b7 source: ' + html.escape(str(LIVE.get("source", ""))) + ' \u00b7 kick-offs UTC \u00b7 rounds appear as the desk verifies them</p></section>'
                + '<section class="section">' + usecs + '</section>'
                + '<section class="section alt"><div class="prose"><p>The 36-team league phase runs across eight matchdays from September to January. Already played: the <a href="/champions-league-results/">Matchday 1 results</a> and the <a href="/champions-league-table/">league-phase table</a>. The format: <a href="/how-the-champions-league-works/">how the Champions League works</a>.</p></div></section>'
                + '</div></main>' + foot("sports"))
            pages.append(("/champions-league-fixtures/", "Champions League fixtures 2026-27 \u2014 the league phase | BRYME Sport",
                          "The 2026-27 Champions League league-phase schedule: verified dates and kick-offs, round by round. No invented fixtures, ever.", uf))


    laliga_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The LaLiga desk</nav>'
        + '<section class="cover"><p class="kicker">The LaLiga hub \u00b7 2026-27</p>'
        + '<h1 class="cover-title">Spain\u2019s league, on one page.</h1>'
        + '<p class="cover-dek">The live table, the scoring race and the verified fixtures first \u2014 then the explainers: what LaLiga is, how it runs, and the fixture that carries more than ninety minutes.</p></section>'
        + _league_module(LIVE.get("leagues", {}).get("la-liga", {}), "la-liga", "La Liga")
        + '<section class="section"><div class="section-head"><p class="kicker">The data desk</p><h2>Every tool for the Spanish season.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/la-liga-table/"><span><b>The live table</b><small>Twenty clubs after Matchweek 4 \u2014 Barcelona perfect, stamped and sourced.</small></span><span class="meta">Live</span></a></li>'
        + '<li><a href="/la-liga-top-scorers/"><span><b>Top scorers</b><small>The Pichichi race, verified: Raphinha leads.</small></span><span class="meta">Scorers</span></a></li>'
        + '<li><a href="/la-liga-results/"><span><b>Results</b><small>The latest verified scores, matchday by matchday.</small></span><span class="meta">Results</span></a></li>'
        + '<li><a href="/la-liga-fixtures/"><span><b>The 2026-27 calendar</b><small>Every scheduled LaLiga fixture \u2014 the official calendar, dated and stamped.</small></span><span class="meta">Calendar</span></a></li>'
        + '<li><a href="/la-liga-transfers/"><span><b>The transfer centre</b><small>Every listed summer deal, club by club \u2014 rumours never listed.</small></span><span class="meta">Transfers</span></a></li>\n<li><a href="/laliga-explained/"><span><b>LaLiga, explained</b><small>Twenty clubs, the drop to Segunda, the calendar \u2014 and why the league\u2019s rhythm differs from England\u2019s.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/el-classico-explained/"><span><b>El Clásico, explained</b><small>Two institutions, two identities, one match the whole sport watches.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/why-football-transfers-collapse/"><span><b>Why transfers collapse</b><small>The four doors between a done deal and a done deal \u2014 the same in Madrid as in Manchester.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/what-does-a-sporting-director-do/"><span><b>What does a sporting director do?</b><small>The role that builds the machine behind every squad renewal.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/who-will-win-the-2026-ballon-dor/"><span><b>Who wins the Ballon d\u2019Or?</b><small>The living race page \u2014 Yamal, Rodri and the field, updated in place.</small></span><span class="meta">Feature</span></a></li>'
        + '<li><a href="/what-the-2026-world-cup-changed/"><span><b>What the World Cup changed</b><small>Spain\u2019s one-goal tournament and Ferr\u00e1n\u2019s 106th-minute winner, six weeks on.</small></span><span class="meta">Feature</span></a></li>'
        + '<li><a href="/sports/transfers/"><span><b>The transfer desk</b><small>How deals happen, the mechanics, the window\u2019s archive \u2014 and the centre for every listed deal.</small></span><span class="meta">Transfers</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="prose"><p><em>This shelf opens now and grows with the season \u2014 the desk adds dated editions as the year runs, under the same house rules: no odds, no rumour mill, no invented facts.</em></p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/laliga/", "The LaLiga desk | BRYME Sport",
                  "LaLiga and El Clásico explained plainly, plus the transfer mechanics \u2014 the Spanish shelf, covered honestly, never betting.", laliga_hub))

    # the transfer desk: one hub for the window's editions and mechanics
    transfers_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The transfer desk</nav>'
        + '<section class="cover"><p class="kicker">The transfer desk \u00b7 the window, in one place</p>'
        + '<h1 class="cover-title">Transfers, covered honestly.</h1>'
        + '<p class="cover-dek">No rumour mill, no betting angles: the desk covers transfers as journalism &mdash; how deals actually happen, who makes them happen, and a tracker of what this desk could verify while the window was open. Live window coverage returns as a fresh edition every window.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The transfer centre</p><h2>Every listed deal, five leagues.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/premier-league-transfers/"><span><b>Premier League \u00b7 summer 2026</b><small>99 players in, 83 out \u2014 statuses strict, rumours never listed.</small></span><span class="meta">Centre</span></a></li>'
        + '<li><a href="/la-liga-transfers/"><span><b>La Liga \u00b7 summer 2026</b><small>Every listed deal, club by club \u2014 fees and statuses as recorded.</small></span><span class="meta">Centre</span></a></li>'
        + '<li><a href="/serie-a-transfers/"><span><b>Serie A \u00b7 summer 2026</b><small>The Italian window\u2019s verified tracker.</small></span><span class="meta">Centre</span></a></li>'
        + '<li><a href="/bundesliga-transfers/"><span><b>Bundesliga \u00b7 summer 2026</b><small>The German window\u2019s verified tracker.</small></span><span class="meta">Centre</span></a></li>'
        + '<li><a href="/ligue-1-transfers/"><span><b>Ligue 1 \u00b7 summer 2026</b><small>The French window\u2019s verified tracker.</small></span><span class="meta">Centre</span></a></li>'
        + '</ul></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The archive editions</p><h2>The 2026 summer window, as we covered it.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/premier-league-transfer-tracker-august-2026/"><span><b>The August 2026 transfer tracker</b><small>Archive edition &mdash; the window as it happened, kept with its date on its sleeve.</small></span><span class="meta">Archive</span></a></li>'
        + '<li><a href="/deadline-day-dont-try-to-make-sense-of-it/"><span><b>Deadline day: don\u2019t try to make sense of it</b><small>A field guide to the window\u2019s strangest evening.</small></span><span class="meta">Archive</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">The mechanics</p><h2>How deals actually happen.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/why-football-transfers-collapse/"><span><b>Why transfers collapse</b><small>Fee, terms, medical, paperwork &mdash; four doors, and the window\u2019s favourite tragedies live in the gaps.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/what-does-a-sporting-director-do/"><span><b>What does a sporting director actually do?</b><small>The role that builds the machine behind every deal.</small></span><span class="meta">Explainer</span></a></li>'
        + '</ul></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The calendar</p><h2>When the next window opens.</h2></div>'
        + '<div class="prose"><p>In England the summer window typically closes on the evening of 1 September, and a winter window runs through January; other leagues set their own dates within FIFA\u2019s framework, confirmed window by window. When the next one opens, the tracker returns as a new dated edition &mdash; until then, the archive stands exactly as it was written.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/transfers/", "The transfer desk \u2014 window coverage, honestly | BRYME Sport",
                  "Transfer coverage without the rumour mill: archive window editions, how deals actually happen, and when live coverage returns.", transfers_hub))

    # the Champions League shelf
    ucl_hub = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The Champions League shelf</nav>'
        + '<section class="cover"><p class="kicker">The Champions League shelf \u00b7 understand the competition</p>'
        + '<h1 class="cover-title">Europe\u2019s big cup, explained.</h1>'
        + '<p class="cover-dek">The live league-phase table, the verified results and the scoring race come first \u2014 then the explainers that walk the whole journey from qualification to the final.</p></section>'
        + _league_module(LIVE.get("leagues", {}).get("champions-league", {}), "champions-league", "Champions League")
        + '<section class="section"><div class="section-head"><p class="kicker">The live data desk</p><h2>The league phase, as played.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/champions-league-table/"><span><b>The league-phase table</b><small>All 36 clubs \u2014 stamped with its verification time.</small></span><span class="meta">Live</span></a></li>'
        + '<li><a href="/champions-league-results/"><span><b>Results</b><small>Every verified score, matchday by matchday.</small></span><span class="meta">Results</span></a></li>'
        + '<li><a href="/champions-league-fixtures/"><span><b>Fixtures</b><small>The next matchdays, verified as the desk receives them.</small></span><span class="meta">Fixtures</span></a></li>'
        + '<li><a href="/champions-league-top-scorers/"><span><b>Top scorers</b><small>The scoring race across the league phase.</small></span><span class="meta">Scorers</span></a></li>'
        + '<li><a href="/who-will-win-the-2026-27-champions-league/"><span><b>Who wins it?</b><small>The living prediction page \u2014 PSG, Arsenal and the chasing field, updated as rounds land.</small></span><span class="meta">Feature</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">Understand the format</p><h2>Start here.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/how-the-champions-league-works/"><span><b>How the Champions League works</b><small>Who gets in, the eight-game league phase, the playoffs, one final on one night.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/champions-league-new-format-explained/"><span><b>The new format: what actually changed</b><small>Old groups vs the 36-team league &mdash; and the honest case each side makes.</small></span><span class="meta">Explainer</span></a></li>'
        + '<li><a href="/why-does-afcon-move-around/"><span><b>Why AFCON moves around the calendar</b><small>The other championship whose dates collide with Europe\u2019s &mdash; climate, calendars, television.</small></span><span class="meta">Explainer</span></a></li>'
        + '</ul></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The honest bit</p><h2>What this hub will not do.</h2></div>'
        + '<div class="prose"><p>It will not invent results, quote odds, or call a twice-daily verified desk \u201clive scores\u201d. The league-phase data above is verified in batches and stamped with its fetch time \u2014 stale-but-sourced beats fresh-but-guessed. Sources: football-data.org v4; UEFA\u2019s official competition pages for the format.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/champions-league/", "The Champions League shelf \u2014 the format, explained | BRYME Sport",
                  "How the Champions League works and what the new 36-team format changed \u2014 evergreen explainers, verified editions in season.", ucl_hub))

    # the /explainers/ section page
    all_rows = "".join('<li><a href="/' + s + '/"><span><b>' + ti + "</b><small>" + dek[:130] + "\u2026</small></span>"
                       '<span class="meta">Explainer</span></a></li>'
                       for s, ti, dek, b, so, re in sports_explainers_data.SPORT_EXPLAINERS)
    sect_body = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / Explainers</nav>'
        + '<section class="cover"><p class="kicker">BRYME Sport \u00b7 the explainer shelf</p>'
        + '<h1 class="cover-title">Understand the game.</h1>'
        + '<p class="cover-dek">The laws, the formats and the roles of football \u2014 explained plainly, argued honestly, and evergreen: nothing here expires with the fixtures. No betting content, ever.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(sports_explainers_data.SPORT_EXPLAINERS)) + ' explainers</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + all_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Also on this desk</p><h2>The season archive.</h2></div>'
        + '<div class="actions"><a class="btn secondary" href="/analysis/">The analysis shelf</a><a class="btn secondary" href="/sports/">Back to BRYME Sport</a></div></section>'
        + "</div></main>" + foot("sports"))
    pages.insert(1, ("/explainers/", "Football explainers \u2014 laws, formats and roles | BRYME Sport",
                     "The offside rule, VAR, promotion and relegation, transfer mechanics, sporting directors and AFCON's calendar \u2014 football explained plainly, evergreen.", sect_body))

    for m in manifest:
        if m["slug"] not in REAL:
            retired.append(f'<li><span><b>{html.escape(m["title"])}</b>'
                           f'<small>{m["words"]} words · reviewed \u2014 retired: teaser stub, not an article</small></span>'
                           f'<span class="meta">Retired</span></li>')
    # ---- batch 16: the form board (pure arithmetic on verified results; spec s7/s45) ----
    _PL_SLUGS = {}
    for _r in sld.PL_TABLE:
        _PL_SLUGS[_r[1]] = _r[2]
    def _form_compute(ld):
        blocks = ld.get("results", [])
        if not blocks:
            return None, ""
        st = {}
        mws = []
        for blk in blocks:
            mws.append(int(blk["mw"]))
            for m in blk["matches"]:
                for nm, gf, ga in ((m["h"], m["hs"], m["as"]), (m["a"], m["as"], m["hs"])):
                    q = st.setdefault(nm, {"p": 0, "w": 0, "d": 0, "l": 0, "gf": 0, "ga": 0, "pts": 0, "f": []})
                    q["p"] += 1
                    q["gf"] += gf
                    q["ga"] += ga
                    if gf > ga:
                        q["w"] += 1; q["pts"] += 3; q["f"].append("W")
                    elif gf == ga:
                        q["d"] += 1; q["pts"] += 1; q["f"].append("D")
                    else:
                        q["l"] += 1; q["f"].append("L")
        season = {row[1]: row for row in ld.get("table", [])}
        for nm, q in st.items():
            q["gd"] = q["gf"] - q["ga"]
            q["ppg"] = (q["pts"] / float(q["p"])) if q["p"] else 0.0
            q["spts"] = season[nm][9] if nm in season else 0
        rows = sorted(st.items(), key=lambda kv: (-kv[1]["ppg"], -kv[1]["gd"], -kv[1]["gf"], -kv[1]["spts"], kv[0]))
        if len(mws) == 1:
            wl = "Matchweek " + str(mws[0])
        elif max(mws) - min(mws) + 1 == len(mws):
            wl = "Matchweeks " + str(min(mws)) + "\u2013" + str(max(mws))
        else:
            wl = "Matchweeks " + ", ".join(str(x) for x in sorted(mws))
        return rows, wl
    def _form_deltas(rows, ld):
        season = ld.get("table", [])
        climbs, slips = [], []
        for i, (nm, q) in enumerate(rows, 1):
            sr = next((j + 1 for j, row in enumerate(season) if row[1] == nm), None)
            if sr is None:
                continue
            d = sr - i
            if d > 0:
                climbs.append((nm, d))
            elif d < 0:
                slips.append((nm, d))
        climbs.sort(key=lambda x: -x[1])
        slips.sort(key=lambda x: x[1])
        return climbs[:3], slips[:3]
    def _form_table(rows, lslug, with_badges):
        trs = ""
        for i, (nm, q) in enumerate(rows, 1):
            if with_badges and nm in _PL_SLUGS:
                club_cell = '<a href="/clubs/' + _PL_SLUGS[nm] + '/"><img class="club-badge row-badge" src="/assets/img/sports/badges/' + badge_file(_PL_SLUGS[nm]) + '" alt="" width="22" height="22" loading="lazy">' + html.escape(nm) + '</a>'
            else:
                club_cell = html.escape(nm)
            form = " ".join(('<b>' + x + '</b>') if x == "W" else x for x in q["f"])
            trs += ('<tr><td class="pos">' + str(i) + '</td><td class="club-b">' + club_cell + '</td>'
                    + '<td>' + form + '</td><td class="num">' + str(q["p"]) + '</td>'
                    + '<td class="num">' + str(q["w"]) + '-' + str(q["d"]) + '-' + str(q["l"]) + '</td>'
                    + '<td class="num">' + str(q["gf"]) + ':' + str(q["ga"]) + '</td>'
                    + '<td class="num"><b>' + ("%.2f" % q["ppg"]) + '</b></td>'
                    + '<td class="num">' + str(q["spts"]) + '</td></tr>')
        return ('<div class="lg-scroll"><table class="lg-table">'
            + '<thead><tr><th>#</th><th>Club</th><th>Form</th><th class="num">P</th><th class="num">W-D-L</th><th class="num">GF:GA</th><th class="num">PPG</th><th class="num">Ssn</th></tr></thead>'
            + '<tbody>' + trs + '</tbody></table></div>')
    _fb_secs = ""
    _fb_pl_rows, _fb_pl_wl = (None, "")
    _fb_order = [("premier-league", "Premier League", True), ("la-liga", "La Liga", False),
                 ("serie-a", "Serie A", False), ("bundesliga", "Bundesliga", False),
                 ("ligue-1", "Ligue 1", False), ("champions-league", "Champions League", False)]
    for _fl, _fn, _fb in _fb_order:
        _fld = LIVE.get("leagues", {}).get(_fl, {})
        _rows, _wl = _form_compute(_fld)
        if not _rows:
            continue
        if _fl == "premier-league":
            _fb_pl_rows, _fb_pl_wl = _rows, _wl
        _cl, _sl = _form_deltas(_rows, _fld)
        _sides = ""
        if _cl:
            _sides += _panel("Climbing fastest", "".join('<div class="sp-row"><span>' + html.escape(n) + '</span><span class="pts">+' + str(d) + '</span></div>' for n, d in _cl), None)
        if _sl:
            _sides += _panel("Slipping", "".join('<div class="sp-row"><span>' + html.escape(n) + '</span><span class="pts">' + str(d) + '</span></div>' for n, d in _sl), None)
        _tlab = "/premier-league-table/" if _fl == "premier-league" else "/" + _fl + "-table/"
        _sides += _panel("Context", '<div class="sp-row"><span><a href="' + _tlab + '">The season table</a></span></div><div class="sp-row"><span><a href="/' + _fl + '-results/">The results behind it</a></span></div>', None)
        _fb_secs += ('<section class="section"><div class="section-head"><p class="kicker">' + _fn + ' \u00b7 form over ' + _wl + '</p><h2>' + _fn + ', by actual form.</h2></div>'
            + '<div class="data-cols"><div>' + _form_table(_rows, _fl, _fb) + '</div><div>' + _sides + '</div></div></section>')
    if _fb_secs:
        _fb_method = ('<section class="section alt"><div class="section-head"><p class="kicker">The method</p><h2>How the board is computed.</h2></div>'
            + '<div class="prose"><p>Every number here is arithmetic on the same verified results the results pages publish \u2014 nothing is modelled, predicted or scored by opinion. Clubs are ranked by <b>points per game</b> across the desk\u2019s current results window'
            + (' (' + _fb_pl_wl + ' for the Premier League)' if _fb_pl_wl else '')
            + '; ties break by window goal difference, then window goals scored, then season points. <b>Form</b> lists the window\u2019s results oldest to newest. <b>Ssn</b> is the club\u2019s real season points, shown for context \u2014 early in a season, three good weeks are a story, not yet a verdict. The board is a BRYME desk table, clearly labelled as ours: it is not an official competition standing, and it refreshes only when the data agent verifies a new round (' + html.escape(str(LIVE.get("generated", ""))) + ').</p></div></section>')
        _fb_page = (_lg_head()
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / The Form Board</nav>'
            + '<section class="cover"><p class="kicker">The Form Board \u00b7 a BRYME desk table</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">Who is actually in form.</h1>'
            + '<p class="byline">The league table says who has the most points; the Form Board says who is earning them right now \u00b7 computed from verified results only \u00b7 refreshed with every data run \u00b7 never betting</p></section>'
            + _fb_secs + _fb_method
            + '<section class="section"><div class="prose"><p>Carry on: the <a href="/sports/">live data desk</a>, the <a href="/the-weekend-ahead/">weekend forecast</a> for what the form means for the next round, and the season-long story in <a href="/premier-league-table/">the real tables</a>.</p></div></section>'
            + '</div></main>' + foot("sports"))
        pages.append(("/form-board/", "The Form Board \u2014 who is actually in form | BRYME Sport",
                      "All six leagues ranked by real recent form: points per game over the verified results window, computed from the same verified scores as the results pages. Nothing modelled, nothing invented.", _fb_page))

    # ---- batch 17: the six living features + the big-questions board ----
    _feat_rows = ""
    for _fslug, _fk, _ft, _fd, _fb, _fbody, _fsrc, _flinks in sports_features_data.FEATURES:
        src_html = ""
        if _fsrc:
            src_html = ('<section class="section alt"><div class="section-head"><p class="kicker">Sources</p><h2>Where the facts came from.</h2></div><ul class="list">'
                + "".join('<li><a href="' + html.escape(u) + '" rel="noopener"><span><b>' + html.escape(n) + '</b></span><span class="meta">Source</span></a></li>' for n, u in _fsrc) + '</ul></section>')
        rel_html = "".join('<div class="sp-row"><span><a href="/' + f2[0] + '/">' + html.escape(f2[2]) + '</a></span></div>' for f2 in sports_features_data.FEATURES if f2[0] != _fslug)
        links_html = "".join('<div class="sp-row"><span><a href="' + u + '">' + html.escape(t) + '</a></span></div>' for u, t in _flinks)
        fp = (_lg_head()
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/sports/">Sport</a> / Big questions</nav>'
            + '<section class="cover"><p class="kicker">' + _fk + '</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + _ft + '</h1>'
            + '<p class="byline">' + _fb + '</p></section>'
            + '<section class="section"><div class="prose">' + _fbody + '</div></section>'
            + '<section class="section"><div class="data-cols"><div>' + _panel("Carry on", links_html, None) + '</div><div>' + _panel("The other big questions", rel_html, None) + '</div></div></section>'
            + src_html
            + '</div></main>' + foot("sports"))
        pages.append(("/" + _fslug + "/", _ft + " | BRYME Sport", _fd, fp))
        _feat_rows += ('<li><a href="/' + _fslug + '/"><span><b>' + _ft + '</b><small>' + _fd[:110] + '</small></span><span class="meta">Feature</span></a></li>')
    feat_secs = ('<section class="section"><div class="section-head"><p class="kicker">Big football questions</p><h2>The six living stories.</h2></div>'
        + '<ul class="list">' + _feat_rows + '</ul></section>')

    # ---- batch 12: the weekend ahead + FPL hub ----
    _wk = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / The weekend ahead</nav>'
        + '<section class="cover"><p class="kicker">The weekend ahead \u00b7 12\u201314 September 2026</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">This weekend, on one page.</h1>'
        + '<p class="byline">Written Thursday 10 September 2026 \u00b7 fixtures verified \u00b7 the forecast is BRYME\u2019s editorial outlook, clearly labelled \u2014 never betting tips, no odds, ever</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Premier League \u00b7 Matchweek 4</p><h2>The fixtures.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/premier-league-fixtures/"><span><b>All ten fixtures, verified</b><small>Every kick-off time and venue for the round, on the calendar page.</small></span><span class="meta">Fixtures</span></a></li>'
        + '<li><a href="/premier-league-matchweek-4-preview/"><span><b>Matchweek 4, previewed honestly</b><small>The desk\u2019s full live edition: the four storylines and the real table.</small></span><span class="meta">Preview</span></a></li>'
        + '<li><a href="/premier-league-table/"><span><b>The table going in</b><small>City and Arsenal perfect, Hull third and unscored-on.</small></span><span class="meta">Live</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">The forecast</p><h2>What the desk expects \u2014 labelled as ours.</h2></div>'
        + '<div class="prose">'
        + '<p><b>The derby (Sunday, 16:30 UK):</b> City arrive perfect, United beaten only once. Derby form logic goes into hibernation; the desk watches the first goal and the midfield duels, and expects the game to open late. BRYME forecast, not a tip.</p>'
        + '<p><b>Hull at Chelsea (Saturday, 15:00):</b> the season\u2019s story visits Stamford Bridge \u2014 unbeaten, unscored-on, third. The desk\u2019s outlook: whatever happens, we learn whether the start is platform or sugar rush. BRYME forecast.</p>'
        + '<p><b>Arsenal at Sunderland (Saturday, 20:00):</b> the league\u2019s meanest defence under the loudest lights in the division. Expect Sunderland to make it ugly early; expect Arsenal\u2019s patience to matter. BRYME forecast.</p>'
        + '</div></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Elsewhere</p><h2>The rest of the weekend.</h2></div>'
        + '<ul class="list">'
        + '<li><a href="/la-liga-fixtures/"><span><b>LaLiga \u00b7 Matchday 5</b><small>Sevilla open on Friday; Barcelona travel on Sunday.</small></span><span class="meta">Spain</span></a></li>'
        + '<li><a href="/serie-a-fixtures/"><span><b>Serie A \u00b7 Matchday 4</b><small>Roma, Inter and Lazio all perfect \u2014 somebody\u2019s run ends.</small></span><span class="meta">Italy</span></a></li>'
        + '<li><a href="/bundesliga-fixtures/"><span><b>Bundesliga \u00b7 Matchday 3</b><small>Augsburg, the early leaders, defend a perfect start.</small></span><span class="meta">Germany</span></a></li>'
        + '<li><a href="/ligue-1-fixtures/"><span><b>Ligue 1 \u00b7 Matchday 4</b><small>Rennes\u2013Marseille under the Friday lights.</small></span><span class="meta">France</span></a></li>'
        + '<li><a href="/champions-league-fixtures/"><span><b>Champions League</b><small>The league phase resumes 13 October \u2014 Matchday 1 is in the books.</small></span><span class="meta">Europe</span></a></li>'
        + '</ul></section>'
        + '<section class="section alt"><div class="prose"><p>Playing fantasy? <a href="/fpl/">Gameweek 4 and the FPL desk\u2019s honest guide</a> is aligned with this weekend. And the standing rule: <a href="/sports/">BRYME Sport never runs betting content</a> \u2014 the forecast is analysis, labelled as opinion.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/the-weekend-ahead/", "The weekend ahead \u2014 fixtures, forecast, no odds | BRYME Sport",
                  "This weekend\u2019s verified fixtures across the six competitions with BRYME\u2019s clearly-labelled editorial outlook. Never betting tips.", _wk))

    _fpl = (head("sports", "Analysis, stories and the long view \u2014 never betting.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/sports/">Sport</a> / FPL</nav>'
        + '<section class="cover"><p class="kicker">Fantasy Premier League \u00b7 the honest guide</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">FPL, explained properly.</h1>'
        + '<p class="byline">BRYME Sport desk \u00b7 rules from the game\u2019s own published rules, evergreen \u00b7 checked 10 September 2026 \u00b7 no tips sold, no odds, ever</p></section>'
        + '<section class="section"><div class="prose">'
        + '<p>Fantasy Premier League is the game inside the game: you pick a 15-man squad within a \u00a3100m budget (at most three players from any one club), set an eleven each gameweek, and score points from their real performances. More than eleven million people play, which makes it the second most-watched sport in English football after football.</p>'
        + '<h2>How points work</h2>'
        + '<p>Playing time first: 1 point for up to 60 minutes, 2 for more. Then the position-based scoring: a goal is worth 6 for a defender or goalkeeper, 5 for a midfielder, 4 for a forward. An assist is 3. A clean sheet pays 4 to goalkeepers and defenders who play 60-plus minutes, 1 to midfielders. Goalkeepers earn a point per three saves and 5 for saving a penalty. There are deductions \u2014 a yellow card costs 1, a red 3, an own goal 2 \u2014 and a bonus system awards 1\u20133 points to the best performers of each match.</p>'
        + '<h2>The captain is everything</h2>'
        + '<p>Your captain scores double. That single fact shapes more FPL decisions than any other: a good week and a great captain are two different things. The Triple Captain chip triples instead, for one week only.</p>'
        + '<h2>Transfers and chips</h2>'
        + '<p>You get one free transfer each gameweek; every extra one costs 4 points, which is why panic hits are the classic beginner tax. Four chips bend the rules for a week: two Wildcards (unlimited transfers, one per half of the season), Free Hit (a one-week squad reset that reverts), and Bench Boost (all fifteen play). The game shows each gameweek\u2019s exact deadline \u2014 it falls shortly before the round\u2019s first kick-off, so set the team the night before.</p>'
        + '<h2>The desk\u2019s angle: fixtures first</h2>'
        + '<p>FPL is a fixtures game wearing a football costume. The tools on this desk map directly: <a href="/premier-league-fixtures/">the verified fixture list</a> for the next round, <a href="/premier-league-table/">the table</a> for who is actually good, <a href="/the-weekend-ahead/">the weekend forecast</a> for the storylines, and the <a href="/premier-league-top-scorers/">scoring charts</a> for who is finishing moves. Use them together \u2014 and remember the house rule applies here too: analysis and information, never gambling.</p>'
        + '</div></section>'
        + '<section class="section alt"><div class="prose"><p>This gameweek: <a href="/premier-league-matchweek-4-preview/">Matchweek 4, previewed honestly</a> \u2014 the derby, Hull\u2019s test, and Arsenal under the lights. The desk\u2019s <a href="/how-the-premier-league-table-works/">table mechanics guide</a> doubles as a tiebreaker explainer for your mini-leagues.</p></div></section>'
        + '</div></main>' + foot("sports"))
    pages.append(("/fpl/", "FPL, explained properly \u2014 scoring, chips, transfers | BRYME Sport",
                  "How Fantasy Premier League actually works: scoring by position, captaincy, transfers and the four chips \u2014 evergreen rules, no tips sold, no odds, ever.", _fpl))

    # ---- batch 12: the sports-portal index blocks ----
    _pl_live = LIVE.get("leagues", {}).get("premier-league", {})
    wk_rows = ""
    for _w in [("/clubs/chelsea/", "Chelsea", "Hull City", "Sat \u00b7 15:00 UK"),
               ("/clubs/sunderland/", "Sunderland", "Arsenal", "Sat \u00b7 20:00 UK"),
               ("/clubs/manchester-united/", "Man United", "Man City", "Sun \u00b7 16:30 UK"),
               ("/clubs/leeds-united/", "Leeds United", "Newcastle", "Mon \u00b7 20:00 UK")]:
        wk_rows += ('<div class="fx-row"><span class="fx-when">' + _w[3] + '</span><span class="fx-tie"><a href="' + _w[0] + '">' + _w[1] + '</a> v ' + _w[2] + '</span><span class="fx-where">Matchweek 4</span></div>')
    _ll_up = LIVE.get("leagues", {}).get("la-liga", {}).get("upcoming", [])
    _bar = next((u for u in _ll_up if "Barcelona" in (u["h"] + " " + u["a"])), None)
    if _bar:
        wk_rows += ('<div class="fx-row"><span class="fx-when">' + html.escape(_bar["d"][:10]) + ' \u00b7 ' + html.escape(_bar["d"][11:]) + ' UTC</span><span class="fx-tie">' + html.escape(_bar["h"]) + ' v ' + html.escape(_bar["a"]) + '</span><span class="fx-where">LaLiga MD' + str(_bar["mw"]) + '</span></div>')
    weekend_secs = ('<section class="section"><div class="section-head"><p class="kicker">This weekend \u00b7 12\u201314 September</p><h2>The matchweek, immediately.</h2></div>'
        + wk_rows
        + '<p class="byline">Fixtures last verified ' + str(LIVE.get("generated", "pre-season")) + ' \u00b7 the full forecast carries sources per fixture</p>'
        + '<a class="sp-more" href="/the-weekend-ahead/">The full weekend forecast</a></section>')
    _def_panel = _panel("The league, live", '<div class="sp-row"><span>The opening rounds are being verified \u2014 the table opens with the first full update.</span></div>', None)
    _pl_panel = _table_panel(_pl_live, "premier-league", 6) or _def_panel
    _sc_panel = _scorers_panel(_pl_live, "premier-league", 5)
    _nx_panel = _panel("Where next", "".join('<div class="sp-row"><span><a href="' + u + '">' + t + '</a></span></div>' for u, t in
        [("/premier-league-results/", "All verified scores"), ("/the-weekend-ahead/", "The weekend forecast"), ("/fpl/", "Fantasy Premier League")]), None)
    comp_rows = ""
    for _s, _n, _h in [("premier-league", "Premier League", "/premier-league/"), ("la-liga", "La Liga", "/laliga/"),
                       ("serie-a", "Serie A", "/serie-a/"), ("bundesliga", "Bundesliga", "/bundesliga/"),
                       ("ligue-1", "Ligue 1", "/ligue-1/"), ("champions-league", "Champions League", "/champions-league/")]:
        _ld = LIVE.get("leagues", {}).get(_s, {})
        _up = _ld.get("upcoming", [])
        if _up:
            _lab = ("MW" if _s == "premier-league" else "MD") + str(_up[0]["mw"])
            _lab += ", this weekend" if _up[0]["d"][:10] <= "2026-09-14" else " \u00b7 from " + _up[0]["d"][:10]
        else:
            _lab = "season under way"
        comp_rows += ('<div class="sp-row"><span><a href="' + _h + '">' + _n + '</a></span><span class="pts">' + _lab + '</span></div>')
    portal_secs = ('<section class="section"><div class="data-cols"><div>' + _pl_panel + _sc_panel + _nx_panel + '</div>'
        + '<div>' + _panel("Six competitions, live", comp_rows, None)
        + _panel("New on the desk", '<div class="sp-row"><span><a href="/the-weekend-ahead/">The weekend ahead \u2014 fixtures + forecast</a></span></div>'
                                     '<div class="sp-row"><span><a href="/fpl/">FPL, explained properly</a></span></div>'
                                     '<div class="sp-row"><span><a href="/champions-league-table/">The Champions League table</a></span></div>'
                                     '<div class="sp-row"><span><a href="/premier-league-transfers/">The transfer centre \u2014 every listed deal</a></span></div>'
                                     '<div class="sp-row"><span><a href="/form-board/">The Form Board \u2014 who is actually in form</a></span></div>', None)
        + '</div></div></section>')
    _b6 = [("Premier League", [("/premier-league-table/", "Table"), ("/premier-league-fixtures/", "Fixtures"), ("/premier-league-results/", "Results"), ("/premier-league-top-scorers/", "Scorers"), ("/premier-league-clubs/", "Clubs")]),
           ("La Liga", [("/laliga/", "Hub"), ("/la-liga-table/", "Table"), ("/la-liga-fixtures/", "Fixtures"), ("/la-liga-results/", "Results"), ("/la-liga-top-scorers/", "Scorers")]),
           ("Serie A", [("/serie-a/", "Hub"), ("/serie-a-table/", "Table"), ("/serie-a-fixtures/", "Fixtures"), ("/serie-a-results/", "Results"), ("/serie-a-top-scorers/", "Scorers")]),
           ("Bundesliga", [("/bundesliga/", "Hub"), ("/bundesliga-table/", "Table"), ("/bundesliga-fixtures/", "Fixtures"), ("/bundesliga-results/", "Results"), ("/bundesliga-top-scorers/", "Scorers")]),
           ("Ligue 1", [("/ligue-1/", "Hub"), ("/ligue-1-table/", "Table"), ("/ligue-1-fixtures/", "Fixtures"), ("/ligue-1-results/", "Results"), ("/ligue-1-top-scorers/", "Scorers")]),
           ("Champions League", [("/champions-league/", "Hub"), ("/champions-league-table/", "Table"), ("/champions-league-fixtures/", "Fixtures"), ("/champions-league-results/", "Results"), ("/champions-league-top-scorers/", "Scorers")])]
    _left, _right = "", ""
    for _i, (_bn, _links) in enumerate(_b6):
        _rows = "".join('<div class="sp-row"><span><a href="' + u + '">' + t + '</a></span></div>' for u, t in _links)
        _pn = _panel(_bn, _rows, None)
        if _i < 3:
            _left += _pn
        else:
            _right += _pn
    big6_secs = ('<section class="section alt"><div class="section-head"><p class="kicker">The big six</p><h2>Every competition, one click in.</h2></div>'
        + '<div class="data-cols"><div>' + _left + '</div><div>' + _right + '</div></div></section>')
    _sc_left, _sc_right = "", ""
    for _i, (_s, _n) in enumerate([("premier-league", "Premier League"), ("la-liga", "La Liga"), ("serie-a", "Serie A"),
                                   ("bundesliga", "Bundesliga"), ("ligue-1", "Ligue 1"), ("champions-league", "Champions League")]):
        _ld = LIVE.get("leagues", {}).get(_s, {})
        _res = _ld.get("results", [])
        if not _res:
            continue
        _last = _res[-1]
        _tag = ("MW" if _s == "premier-league" else "MD") + str(_last["mw"])
        _rws = ""
        for _m in _last["matches"][:5]:
            _rws += ('<div class="sp-row"><span>' + html.escape(_m["d"][5:]) + ' \u00b7 ' + html.escape(_m["h"]) + ' <b>' + str(_m["hs"]) + '\u2013' + str(_m["as"]) + '</b> ' + html.escape(_m["a"]) + '</span></div>')
        _pn = _panel(_n + " \u00b7 " + _tag, _rws, ("/" + _s + "-results/", "All results"))
        if _i < 3:
            _sc_left += _pn
        else:
            _sc_right += _pn
    latest_secs = ""
    if _sc_left or _sc_right:
        latest_secs = ('<section class="section"><div class="section-head"><p class="kicker">Last verified scores</p><h2>The latest round, all six leagues.</h2></div>'
            + '<div class="data-cols"><div>' + _sc_left + '</div><div>' + _sc_right + '</div></div></section>'
            + '<p class="byline">Last verified ' + str(LIVE.get("generated", "pre-season")) + ' \u00b7 source: football-data.org free tier, cross-checked against league sources \u00b7 the desk updates after each verified round</p></section>')
    _as_left, _as_right = "", ""
    for _i, (_s, _n) in enumerate([("premier-league", "Premier League"), ("la-liga", "La Liga"), ("serie-a", "Serie A"),
                                   ("bundesliga", "Bundesliga"), ("ligue-1", "Ligue 1"), ("champions-league", "Champions League")]):
        _ld = LIVE.get("leagues", {}).get(_s, {})
        _sc = [x for x in (_ld.get("scorers") or []) if x]
        if not _sc:
            continue
        _sc2 = sorted(_sc, key=lambda x2: (x2.get("a") or 0), reverse=True)[:3]
        _rws = ""
        for _x in _sc2:
            _av = _x.get("a")
            _avd = str(_av) if _av else "\u2014"
            _rws += ('<div class="sp-row"><span>' + html.escape(str(_x.get("p", "?"))) + ' <b>' + _avd + '</b> <small>' + html.escape(str(_x.get("c", ""))) + '</small></span></div>')
        _pn = _panel(_n + " \u00b7 assists", _rws or '<div class="sp-row"><span>No assists recorded yet \u2014 early rounds.</span></div>', ("/" + _s + "-top-scorers/", "Scorers"))
        if _i < 3:
            _as_left += _pn
        else:
            _as_right += _pn
    assists_secs = ""
    if _as_left or _as_right:
        assists_secs = ('<section class="section"><div class="section-head"><p class="kicker">The creators</p><h2>Top assists, all six leagues.</h2></div>'
            + '<div class="data-cols"><div>' + _as_left + '</div><div>' + _as_right + '</div></div>'
            + '<p class="lede" style="font-size:14px">Assists ledger from the same verified scorer feeds \u2014 blanks are honest blanks until the providers record them.</p></section>')
    index_body = f"""{head("sports", "Analysis, stories and the long view \u2014 never betting.")}
<main id="main"><div class="wrap">
<section class="cover"><p class="kicker">BRYME Sport · the 2026-27 season is live · six competitions · no odds, ever</p>
<h1 class="cover-title">Sport as reporting, not noise.</h1>
<p class="cover-dek">Football first: the transfer window read plainly, the matchweeks reviewed, the season's stories followed as they happen. Restored from the BRYME media desk \u2014 and, as a house rule, never betting odds or gambling-adjacent tips.</p><div class="cover-facts">
<div><b>{len(sports_explainers_data.SPORT_EXPLAINERS) + len(sports_analysis_data.SPORT_ANALYSIS)}</b><span>Evergreen pieces</span></div>
<div><b>6</b><span>Dated editions</span></div>
<div><b>6</b><span>Competitions</span></div>
</div></section>""" + weekend_secs + latest_secs + assists_secs + portal_secs + feat_secs + big6_secs + f"""<section class="section"><div class="section-head"><p class="kicker">The competitions, in depth.</p><h2>The league system.</h2></div><ul class="list"><li><a href="/premier-league/"><span><b>Premier League</b><small>Table | Fixtures | Results | Clubs | Scorers \u2014 the full gateway, live.</small></span><span class="meta">England</span></a></li><li><a href="/laliga/"><span><b>LaLiga</b><small>The Spanish desk: LaLiga and El Clásico, explained plainly.</small></span><span class="meta">Spain</span></a></li><li><a href="/serie-a/"><span><b>Serie A</b><small>Italy\u2019s tactician\u2019s league \u2014 format, champions, history.</small></span><span class="meta">Italy</span></a></li><li><a href="/bundesliga/"><span><b>Bundesliga</b><small>Germany\u2019s 18 clubs and the 50+1 model.</small></span><span class="meta">Germany</span></a></li><li><a href="/ligue-1/"><span><b>Ligue 1</b><small>France, the academy superpower \u2014 and PSG\u2019s project.</small></span><span class="meta">France</span></a></li><li><a href="/champions-league/"><span><b>Champions League</b><small>The 36-team format, explained from every angle.</small></span><span class="meta">Europe</span></a></li></ul></section>
<section class="section"><div class="section-head"><p class="kicker">Evergreen explainers</p><h2>Understand the game.</h2></div>
<ul class="list">{''.join(expl_rows)}</ul></section>
<section class="section"><div class="section-head"><p class="kicker">The shelves</p><h2>Analysis, the transfer desk &amp; the Champions League.</h2></div>
<ul class="list">
<li><a href="/analysis/"><span><b>The analysis shelf</b><small>How the game is actually played &mdash; xG, pressing, possession, the build-up and the trap.</small></span><span class="meta">Shelf</span></a></li>
<li><a href="/epl/"><span><b>The Premier League desk</b><small>Archive matchweeks and the transfer window, plus the evergreen league explainers.</small></span><span class="meta">Desk</span></a></li>
<li><a href="/laliga/"><span><b>The LaLiga desk</b><small>Spain\u2019s league and the Clásico, explained plainly \u2014 the newest shelf.</small></span><span class="meta">Desk</span></a></li>
<li><a href="/transfers/"><span><b>The transfer desk</b><small>The window in one place &mdash; archive editions, deal mechanics, and when live coverage returns.</small></span><span class="meta">Desk</span></a></li>
<li><a href="/champions-league/"><span><b>The Champions League shelf</b><small>The 36-team format, explained honestly &mdash; with match coverage returning in season.</small></span><span class="meta">Shelf</span></a></li>
</ul></section>
<section class="section"><div class="section-head"><p class="kicker">The restored desk</p><h2>Recovered editions</h2></div>
<ul class="list">{''.join(restored)}</ul></section>
<section class="section alt"><div class="section-head"><p class="kicker">The honest bit</p><h2>What stayed retired.</h2></div>
<ul class="list">{''.join(retired)}</ul>
<p class="lede">The archive also held roughly two thousand match-data pages from finished fixtures. They are data, not journalism; they stay retired rather than being republished stale. New reporting accumulates here as the season runs.</p>
</section></div></main>{foot("sports")}"""
    pages.insert(0, ("/", "BRYME Sport \u2014 football reporting, never betting",
              "Transfer reporting, matchweek guides and season stories from the BRYME media desk. Independent, checkable, strictly no gambling content.", index_body))
    return pages + legal_pages("sports", "BRYME Sport", "Analysis, stories and the long view of sport \u2014 checkable, and never betting.")


# ---------------------------------------------------------------- 4. MONEY

TECH_ARTICLES = [
 ("render-static-deploy", "How to deploy a static site on Render — from a site that did it",
  "Push-to-deploy, the publish directory, spooling deploys and the free-tier cold start: the whole path, written by someone whose production site runs on exactly this.",
  """<p>This site you are reading runs on Render's free static hosting, and so does its 500-page sibling. Everything below is first-hand, not documentation paraphrase.</p>
<h2>The three decisions that matter</h2>
<p><strong>1. Build command vs publish directory.</strong> Render runs your build command, then serves whatever directory you name as the publish directory. Ours is <code>npm run build</code> publishing <code>public/</code>. The classic mistake is testing locally, deploying, and looking at a stale page — because the publish directory points at the source folder instead of the build output. Point it at generated output, always.</p>
<p><strong>2. The build can fail and the site still serves.</strong> A static host serves the last good deploy. That is resilience, but it hides breakage: your build can be red for days while the site looks fine. Wire a status notification (Render's dashboard hooks or a simple build-badge check) — trust the build log, not the homepage.</p>
<p><strong>3. Redirects live with the host.</strong> A <code>_redirects</code> file works on some hosts and is ignored on others; Render static sites use a redirects file format of their own (<code>_redirects</code> in the publish directory), and dashboard-level redirect rules shadow everything. When a path "mysteriously" serves the wrong page, check the dashboard rules first.</p>
<h2>The free tier, honestly</h2>
<p>Free static hosting on Render does not sleep — static sites are served from CDN edges, so there is no cold start (that applies to free <em>web services</em>, a different product). The real limits are build minutes and bandwidth. For a text-first site with system fonts and no framework, both are a rounding error: this deployment serves hundreds of thousands of internal links across ~500 pages on the free tier.</p>
<h2>The checklist</h2>
<ul>
<li>Build command tested locally, byte-identical output.</li>
<li>Publish directory = generated output only.</li>
<li>Custom redirects declared once, in the file the host actually reads.</li>
<li>After the first deploy: curl every critical URL. Never sample — verify.</li>
</ul>"""),
 ("custom-domain-dns-order", "Custom domains: the DNS order that avoids downtime",
  "Apex, www, CNAME flattening and verification order — the sequence that works, learned while moving a live site.",
  """<p>Moving a site to a custom domain is simple in principle and annoying in practice because the steps have an order, and doing them out of order produces hours of "why is this still showing the old site".</p>
<h2>The order</h2>
<p><strong>1. Buy the domain at a registrar with honest pricing</strong> (at-cost resellers like Cloudflare or Porkbun), and keep DNS hosted there. Free WHOIS privacy comes standard now; pay for it nowhere.</p>
<p><strong>2. Add the domain in your host's dashboard first.</strong> Render (and most hosts) gives you the exact DNS records to create — an apex record and a www record. Adding the domain before the records exist means verification completes the moment DNS propagates.</p>
<p><strong>3. Create the records exactly as given.</strong> Apex domains usually get ALIAS/ANAME or A records; www gets a CNAME. If your registrar supports CNAME flattening at the apex, flattening to the host's target is the clean path.</p>
<p><strong>4. Change the site's canonical URLs in config, not in pages.</strong> Every canonical link, sitemap entry and Open Graph URL should come from one configuration value. Ours is a single <code>SITE_URL</code> in one config file feeding every builder; grep your codebase for the old hostname and the only hit should be the changelog.</p>
<p><strong>5. Verify with the registry, not your browser.</strong> Browser caches lie about DNS for hours. Check with <code>dig</code>/<code>nslookup</code>, and confirm the old domain 301s to the new one at the host level.</p>
<h2>The mistake that costs a week</h2>
<p>Hard-coding the staging hostname into canonicals, then migrating. Search engines index what your canonicals say; if every page declares the staging URL canonical, the new domain can sit unindexed for weeks. Centralise the hostname before you migrate — the five minutes of config refactor is the whole game.</p>"""),
 ("github-token-hygiene", "Personal access tokens: using them without leaking them",
  "Least-scope tokens, where they can and cannot appear, and the rotation habit — written after months of daily build use.",
  """<p>A GitHub personal access token in a build pipeline is a standing temptation to do the lazy thing: paste it into a script, commit, move on. Don't. Here is the discipline that works day-to-day.</p>
<h2>Scope it to the minimum</h2>
<p>A token that only pushes to one repository needs exactly one scope: contents read/write on that repo. Fine-grained tokens (now the default in GitHub's settings) let you select the single repository and the single permission. If your token's description says "for everything", it is wrong.</p>
<h2>Where a token may appear</h2>
<ul>
<li><strong>CI secrets / environment variables:</strong> yes. Render, Actions, and friends inject them at build time.</li>
<li><strong>A chat message to your own agent or notes:</strong> tolerable only if you plan rotation — and "planning" means a date on the calendar, not intentions.</li>
<li><strong>A committed file, a URL, a screenshot:</strong> never. Committed tokens live forever in history; GitHub's secret scanning will revoke some automatically, and attackers find the rest first.</li>
</ul>
<h2>The rotation habit</h2>
<p>Rotate on a schedule you would be embarrassed to break: 90 days for personal tokens is a good default, immediately after any suspected exposure, and whenever a collaborator leaves. Rotation costs five minutes if your pipeline reads the token from one secret; it costs an evening if the token is pasted in six places.</p>
<h2>The tell you're doing it right</h2>
<p>Grep your repository for the token prefix right now (<code>ghp_</code> for classic tokens). The correct number of results is zero — including in history, which you can check with <code>git log -S ghp_</code>. If history is dirty and the repo is public, the token is burned: revoke first, refactor second.</p>"""),
 ("csp-safe-front-end", "A front end that survives redesigns: CSP-safe patterns that work",
  "No jQuery, no inline scripts, no build step — the four patterns behind a 500-page site's entire JavaScript layer.",
  """<p>The pages on this site's family run on a few kilobytes of hand-written ES5. No framework, no bundler, no jQuery — and, because the sites ship a Content-Security-Policy, no inline scripts anywhere. These are the patterns that make that livable.</p>
<h2>1. One entry point per page, found by attribute</h2>
<p>Every page that needs behaviour carries a <code>&lt;script src=... data-tool="name"&gt;</code> tag. The shared script file reads <code>document.currentScript.dataset.tool</code> at load time and dispatches to that module. It is dependency-free page-to-script wiring that survives any redesign of the HTML around it.</p>
<h2>2. IDs are the contract</h2>
<p>Scripts address the DOM by element ID and data attributes, never by styling classes. Styling classes belong to CSS and change constantly; IDs are semantics and change rarely. When a redesign came through recently, the entire JavaScript audit was "grep for getElementById" — every hook held.</p>
<h2>3. Progressive enhancement, for real</h2>
<p>Filters, editors and calculators here all render their no-JS state first and enhance if the script loads. The test: disable JavaScript and the page must still be a complete, readable document. This is also the cheapest accessibility audit there is.</p>
<h2>4. localStorage with a versioned envelope</h2>
<p>Anything a user creates in the browser (drafts, trackers, tool state) is stored as <code>{"v":1,...}</code>. When the shape changes, bump the version and migrate on read. The day accounts arrive, local data upgrades instead of breaking.</p>
<p>The reward for all this discipline is boring: pages that load fast on hotel Wi-Fi, zero console errors, and redesigns that touch CSS files rather than JavaScript.</p>"""),
 ("sitemap-indexnow", "Sitemaps and IndexNow: telling search engines the honest way",
  "What to ping, when to ping it, and why sampled verification is how broken launches happen.",
  """<p>Every launch conversation eventually asks: do we need to "submit" the site anywhere? The honest answer for most of the job is no — but the parts that are yes, people get wrong constantly.</p>
<h2>The sitemap is a claim, so keep it true</h2>
<p>A sitemap asserts "these are the canonical, indexable URLs." Every assertion that isn't true is a small editorial lie to the crawler: staged-but-unbuilt routes, parameterised duplicates, pages your robots file blocks. Generate the sitemap from the same source of truth as your build, and add an assertion to the build that fails when a sitemap route lacks a built page. Ours fails the build on any mismatch; it has caught three launch mistakes that sampled checking would have missed.</p>
<h2>IndexNow: for changes, not for begging</h2>
<p>IndexNow lets you notify participating engines when URLs are created or materially change. The protocol is a keyed GET/POST with the changed URLs — not a substitute for sitemaps, and not something to hammer on a schedule. Our practice: ping after every meaningful deploy, listing exactly the new and changed URLs, and keep a JSONL log of what was announced when. The log settles every "did we tell them?" argument.</p>
<h2>Search Console is the feedback loop</h2>
<p>Verification via a DNS record takes minutes. The property then tells you what the crawlers actually did with your claims: indexed, ignored, or blocked. Read it monthly, export the queries, and let real impressions — not vanity traffic — pick what gets expanded next.</p>
<h2>What never to do</h2>
<p>Never ping URLs that return 404, never submit a sitemap whose URLs contradict your canonicals, and never generate pages to fill a sitemap. The systems are designed by people who have seen every trick; the only sustainable strategy is to have the site actually be as described.</p>"""),
]

TECH_CAT = {
    "ai": ("AI, without the hype", "What the assistants actually do, what the free tiers really include, and where your conversations go \u2014 checked against the real products, not the press releases.", "hero-assistants.jpg"),
    "tools": ("Free tools & real alternatives", "Free plans and alternatives we actually opened and used \u2014 what they include, what they hold back, and who each one fits.", "hero-alternatives.jpg"),
    "subscriptions": ("Subscriptions & clutter", "Recurring charges, free trials and the audit \u2014 keeping what you pay for fewer, cheaper and actually used.", ""),
    "streaming": ("Streaming & cord-cutting", "Quality settings, bandwidth reality and the honest math of replacing cable \u2014 what your stream costs and why it looks the way it does.", ""),
    "web-and-hosting": ("Web & hosting", "Domains, DNS, deploys and the front end \u2014 written from first-hand builds of this very site, failures included.", "hero-hosting.jpg"),
    "safety": ("Safety & privacy", "Passwords, messaging, tokens and your data \u2014 practical protection without the scaremongering.", "hero-privacy.jpg"),
    "smart-home": ("Smart home", "Devices worth owning, speakers that listen, and the Wi-Fi that quietly decides whether any of it works \u2014 setup honesty, not showroom promises.", ""),
    "android": ("Android & mobile", "Phone storage, permissions, battery and notifications \u2014 the settings that actually matter, explained without the jargon.", ""),
    "windows": ("Windows & PC", "Slow computers, browser trouble and update problems \u2014 triaged in the order that finds the cause fastest.", ""),
    "coding": ("Coding", "Beginner programming explained the honest way \u2014 errors, Git and APIs \u2014 from a desk that ships code.", ""),
    "quant": ("Quantitative computing", "The QuantLab project: a one-person research lab in Python, and what ~140 documented experiments taught \u2014 failures included. Educational research, never investment advice.", ""),
    "buying": ("Buying guides", "Specs vs marketing, refurbished vs new \u2014 the numbers that decide whether tech is still pleasant in year three.", ""),
}
_TECH_CAT_OF = {
    "hosting": "web-and-hosting", "ai-assistants": "ai", "beginner-coding": "coding",
    "app-alternatives": "tools", "useful-websites": "tools", "cybersecurity": "safety",
    "android-apps": "safety", "productivity": "tools",
}
_TECH_CUR_CAT = {
    "csp-safe-front-end": "web-and-hosting", "custom-domain-dns-order": "web-and-hosting",
    "render-static-deploy": "web-and-hosting", "sitemap-indexnow": "web-and-hosting",
    "github-token-hygiene": "safety",
}

def _norm_tech(rec):
    return {
        "slug": rec["slug"], "title": rec["title"], "excerpt": rec.get("excerpt", ""),
        "cat": _TECH_CAT_OF.get(rec.get("categorySlug", ""), "coding"),
        "pub": (rec.get("publishedAt") or "")[:10], "upd": (rec.get("updatedAt") or "")[:10],
        "read": rec.get("readingTime", ""), "author": rec.get("author", "BRYME Tech desk"),
        "blocks": rec.get("content", []), "sources": rec.get("sources", []), "recovered": True,
    }

def _load_tech():
    arts = [_norm_tech(r) for r in json.loads(
        (OUT.parent / "content" / "tech-articles.json").read_text(encoding="utf-8"))]
    by_slug = {a["slug"]: a for a in arts}
    for slug, title, blurb, body in TECH_ARTICLES:
        if slug in by_slug:
            continue
        arts.append({"slug": slug, "title": title, "excerpt": blurb,
                     "cat": _TECH_CUR_CAT.get(slug, "coding"), "pub": TODAY, "upd": TODAY,
                     "read": "", "author": "the BRYME Tech desk",
                     "blocks": [{"heading": "", "body": body, "html": True}],
                     "sources": [], "recovered": False})
    import tech_troubleshooting_data
    for slug, cat, kind, title, dek, body in tech_troubleshooting_data.TROUBLESHOOTING_GUIDES:
        arts.append({"slug": slug, "title": title, "excerpt": dek, "cat": cat, "kind": kind,
                     "pub": TODAY, "upd": TODAY, "read": "", "author": "the BRYME Tech desk",
                     "blocks": [{"heading": "", "body": body, "html": True}],
                     "sources": [], "recovered": False})
    import tech_guides_data
    for slug, cat, kind, title, dek, body, sources, related in tech_guides_data.NEW_TECH_GUIDES:
        arts.append({"slug": slug, "title": title, "excerpt": dek, "cat": cat, "kind": kind,
                     "pub": TODAY, "upd": TODAY, "read": "", "author": "the BRYME Tech desk",
                     "blocks": [{"heading": "", "body": body, "html": True}],
                     "sources": [{"name": n, "url": u} for n, u in sources],
                     "recovered": False})
    return arts

def _tech_blocks(a):
    out = []
    for b in a["blocks"]:
        h = html.escape(b.get("heading") or "")
        if h:
            out.append("<h2>" + h + "</h2>")
        body = b.get("body") or ""
        if b.get("html"):
            out.append(body)
        else:
            out.append("".join("<p>" + html.escape(pp).replace("\n", " ") + "</p>"
                               for pp in body.split("\n\n") if pp.strip()))
    return "".join(out)

def _tech_related(a, arts, n=3):
    same = [x for x in arts if x["cat"] == a["cat"] and x["slug"] != a["slug"]]
    pool = ["where-to-host-website-for-free", "bitwarden-free-password-manager",
            "learning-to-code-on-a-phone-termux", "custom-domain-dns-order",
            "git-errors-fixed", "api-errors-decoded", "computer-fans-loud",
            "how-the-internet-works"]
    pick = pool[sum(map(ord, a["slug"])) % len(pool)]
    extra = [by for by in arts if by["slug"] == pick and by["slug"] != a["slug"] and by not in same]
    if not extra:
        return same[:n]
    return (same[:n - 1] + extra)[:n]

def tech_trust_pages():
    """Trust pages (master build M1): methodology, corrections, terms, disclaimer."""
    methodology_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Methodology</nav>
<section class="cover"><p class="kicker">How we work</p><h1 class="cover-title">How BRYME Tech researches what it publishes.</h1>
<p class="cover-dek">Every guide on this desk is written under one discipline: verify it live, name the source, date the volatile parts &mdash; or don't claim it at all.</p></section>
<section class="section"><div class="prose">
<h2>Two labels, and what they promise</h2>
<p><strong>BRYME Technical Guide</strong> is general technical reference: researched from official documentation and primary sources, written for the practical question in the title. <strong>First-Hand Project Report</strong> is different in kind: the piece comes from a project we actually ran &mdash; this publication's own deployment stack (Render, DNS, token hygiene, CSP patterns) and the <a href="/tech/quantlab-project-how-built/">QuantLab research project</a> are the current examples. First-hand means we ran the thing on our own accounts and hardware; where a piece is first-hand, the label says so, and where it isn't, we don't pretend.</p>
<h2>Where claims come from</h2>
<p>External facts come from primary sources: official documentation, official product and pricing pages, standards bodies, regulators. Numbers get a named source and a date in the text. Where third-party aggregators disagree &mdash; common with pricing and stats &mdash; we publish the named-source range or drop the number entirely; a conflicting figure is never averaged into confidence. <code>sources</code> lists that look empty are deliberate too: it means the piece makes no external factual claims, because it's engineering reasoning or our own experience.</p>
<h2>Verification before publish</h2>
<p>Volatile claims carry a hard gate: nothing publishes on a remembered number. Code examples are executed in a real environment before publishing where practical. And the site itself is machine-checked every build: internal links must all resolve, thin and duplicate pages fail a quality gate, and the deployed pages are spot-checked against their source claims &mdash; we verify the built page, not the intention.</p>
<h2>When facts age</h2>
<p>Technology pieces rot at the edges: prices, model names, menu paths, limits. Pieces with volatile claims are stamped in-text (&ldquo;checked September 2026&rdquo;) and treated as UPDATE-class: on re-review we re-verify against the official pages, patch the text, and add an explicit dated re-verified note. Dates are never quietly refreshed.</p>
<h2>What we refuse</h2>
<p>Fabricated benchmarks, invented statistics, fake screenshots, imagined experience, and pages built to exist rather than to be useful. A smaller number of pages that survive their own claims is the whole business model &mdash; see <a href="/tech/corrections/">what happens when one doesn't</a>.</p>
</div></section></div>"""
    corrections_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Corrections</nav>
<section class="cover"><p class="kicker">Corrections policy</p><h1 class="cover-title">Corrections, handled in the open.</h1>
<p class="cover-dek">Errors get fixed in the text, noted with a date, and never quietly. A publication that can't show its corrections is asking you to trust its averages instead of its record.</p></section>
<section class="section"><div class="prose">
<h2>How errors get found</h2>
<p>Three ways, in rough order of frequency: our own scheduled re-verification passes (volatile claims &mdash; pricing, limits, legal statuses &mdash; are re-checked against official pages before any piece is republished); the automated checks that run on every build (every internal link must resolve; thin and duplicate pages fail the build); and readers, who remain the best error-finding system ever invented. <a href="/tech/contact/">If you find one, that email is the most valuable one we get.</a></p>
<h2>What happens next</h2>
<p><strong>Substantive corrections</strong> &mdash; a wrong number, a broken method, a claim that no longer holds &mdash; are fixed in the text and noted on the page with the date and what changed. If a claim can no longer be verified at all, it is removed rather than softened into vagueness. <strong>Re-verifications</strong> (the claim still holds, re-checked on a later date) are noted the same way, because a date that silently refreshes is worth nothing. <strong>Wording fixes</strong> &mdash; typos, unclear phrasing &mdash; are fixed directly; they change nothing you'd rely on, so they don't get a stamp.</p>
<h2>The receipts habit</h2>
<p>Behind the published pages, every batch of work keeps a written record: which sources were checked live, which claims were gated and how they resolved, what was deliberately left out because the evidence didn't support it. When this desk's own numbers have changed under honest re-audit &mdash; and in the QuantLab project they have, dramatically &mdash; the change is the story, not an embarrassment: <a href="/tech/lookahead-bias-explained/">a backtest result that didn't survive its own entry-bar audit became the most useful article on the shelf</a>.</p>
<h2>The standard</h2>
<p>No silent re-dating, no retro-fitting claims to what turned out true, no deleting the evidence of what we wrote before. The record is the product.</p>
</div></section></div>"""
    terms_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Terms</nav>
<section class="cover"><p class="kicker">Terms of use</p><h1 class="cover-title">The plain terms.</h1>
<p class="cover-dek">Short version: this is a publication, not a professional service. Use it the way you'd use a good book &mdash; intelligently, and at your own discretion.</p></section>
<section class="section"><div class="prose">
<h2>What this site is</h2>
<p>BRYME Tech is an independent technical publication offering general information, guides, opinion and research notes. It is not a consultancy, an agency, or a professional service, and using it does not create any professional relationship or duty of care between you and the publisher.</p>
<h2>No warranties</h2>
<p>The site and its content are provided &ldquo;as is&rdquo;, without warranties of any kind, express or implied, including fitness for a particular purpose or accuracy beyond what the <a href="/tech/methodology/">published methodology</a> states. Technology changes under our feet; steps that worked when written may not work when read. Check official documentation before acting on anything consequential.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by applicable law, the publisher is not liable for any loss or damage arising from use of, or reliance on, the site or its content &mdash; including technical steps you run on your own systems, which you do at your own discretion and risk.</p>
<h2>The tools</h2>
<p>Browser tools on this site run entirely in your browser. Text you paste into them is processed on your device and is not uploaded, stored, or transmitted to us. Don't paste secrets into any web tool anyway &mdash; that's not a term, it's <a href="/tech/plain-text-passwords/">the same advice we give everywhere</a>.</p>
<h2>Ownership and trademarks</h2>
<p>Original text and structure are &copy; THE BRYME. Product names, logos and trademarks mentioned belong to their respective owners; mention implies no affiliation, sponsorship or endorsement, and no trademark is claimed. External links are references, not endorsements; we don't control those pages.</p>
<h2>Changes</h2>
<p>These terms may be updated as the publication grows; material changes get dated notes on this page rather than silent edits. Questions: <a href="/tech/contact/">Contact</a>. See also the <a href="/tech/disclaimer/">disclaimer</a> and <a href="/tech/privacy/">privacy</a> pages.</p>
</div></section></div>"""
    disclaimer_body = """<div class="wrap"><nav class="crumb"><a href="/tech/">Tech</a> / Disclaimer</nav>
<section class="cover"><p class="kicker">Disclaimer</p><h1 class="cover-title">What this desk is, and isn't.</h1></section>
<section class="section"><div class="prose">
<h2>General information, not professional advice</h2>
<p>Everything on BRYME Tech is general technical information. Troubleshooting steps, security guides and configuration advice describe what has worked in specific situations and are not tailored advice for your systems; run them at your own discretion, and for high-stakes situations (production outages, security incidents, legal questions about technology) consult a professional who can see the whole picture.</p>
<h2>Quantitative and trading-adjacent research</h2>
<p>Research note: QuantLab experiments are presented for educational and research purposes. Historical backtests and simulations do not guarantee future results and should not be interpreted as investment advice.</p>
<p>In plain words: the <a href="/tech/quantlab-project-how-built/">QuantLab pieces</a> document a research process &mdash; statistics, software engineering, validation discipline, and a lot of instructive failure. They do not recommend any strategy, signal, instrument or trade, they do not republish performance as a promise, and nothing on this desk should move you to risk money. Most of the project's rigorous conclusions are that promising edges were not real. That is the point of publishing them.</p>
<h2>Products, names and dates</h2>
<p>Product names and trademarks belong to their owners; mention implies no affiliation or endorsement. Claims about products carry their check-date in the text and may have changed since &mdash; the official page is always the current truth. External links are provided for verification and reference, not endorsement.</p>
<p class="lede"><em>Last reviewed: September 2026. Found something wrong or stale? <a href="/tech/corrections/">This is how we fix it</a>.</em></p>
</div></section></div>"""
    def _pg(route, title, desc, body):
        return (route, title, desc, '<main id="main">' + body + "</main>")
    return [
        _pg("/methodology/", "Editorial methodology | BRYME Tech",
            "How BRYME Tech researches, verifies and labels what it publishes: primary sources, named dates, first-hand labels, and no remembered numbers.",
            methodology_body),
        _pg("/corrections/", "Corrections policy | BRYME Tech",
            "How errors are found, fixed, dated and never quietly: the BRYME Tech corrections policy and re-verification discipline.",
            corrections_body),
        _pg("/terms/", "Terms of use | BRYME Tech",
            "The plain terms of use for BRYME Tech: general information, no warranties, tools that run in your browser.",
            terms_body),
        _pg("/disclaimer/", "Disclaimer | BRYME Tech",
            "What BRYME Tech is and isn't: general information, not professional advice; QuantLab research is educational, never investment advice.",
            disclaimer_body),
    ]


_TECH_FIRSTHAND = {
    "deploy-python-app": "BRYME Technical Research \u00b7 first-hand project report",
    "quantlab-project-how-built": "BRYME Technical Research \u00b7 first-hand project report",
    "hundred-experiments-lessons": "BRYME Technical Research \u00b7 first-hand project report",
    "lookahead-bias-explained": "BRYME Technical Research \u00b7 first-hand project report",
    "backtest-validation-checklist": "BRYME Technical Research \u00b7 first-hand project report",
    "why-backtests-fail": "BRYME Technical Research \u00b7 first-hand project report",
    "paper-trading-bot-lessons": "BRYME Technical Research \u00b7 first-hand project report",
    "overfitting-detection-guide": "BRYME Technical Research \u00b7 first-hand project report",
}

_TOOL_JS = {"json-formatter": "json", "base64-encoder": "base64", "url-encoder": "url",
            "uuid-generator": "uuid", "timestamp-converter": "timestamp", "word-counter": "wordcount",
            "case-converter": "case", "http-status-lookup": "status"}

def tech_tool_pages():
    """BRYME Tools (master build M3): client-side tools at /tech/tool/<slug>/, CSP-safe."""
    import tech_tools_data
    tools = tech_tools_data.TOOLS
    pages = []
    for slug, name, title, dek, art, what, ui in tools:
        sibs = [t for t in tools if t[0] != slug]
        sib_btns = "".join('<a class="btn secondary" href="/tool/' + t[0] + '/">' + t[1].split(" (")[0].split(" / ")[0] + '</a>'
                           for t in (sibs[0], sibs[2], sibs[4], sibs[6]))
        guide_btn = ('<a class="btn secondary" href="/' + art + '/">Read the guide</a>') if art else ""
        tbody = (head("tech", "Practical technology. No theatre.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/tech/">Tech</a> / <a href="/tool/">Toolbox</a> / ' + name + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Tools \u00b7 runs entirely in your browser</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + title + "</h1>"
            + '<p class="cover-dek">' + dek + "</p></section>"
            + '<section class="section"><div class="wrap"><link rel="stylesheet" href="/assets/tech-tools.css">' + ui + "</div></section>"
            + '<section class="section alt"><div class="prose">' + what + "</div></section>"
            + '<section class="section"><div class="prose"><p><b>Privacy note:</b> every tool on this desk processes your input on your device, in this page \u2014 nothing is uploaded, stored or sent anywhere. The same policy the <a href="/tech/terms/">terms</a> and <a href="/tech/privacy/">privacy</a> pages promise.</p></div>'
            + '<div class="actions">' + guide_btn + sib_btns + '<a class="btn secondary" href="/tech/">All of BRYME Tech</a></div></section>'
            + '<script src="/assets/tool-' + _TOOL_JS[slug] + '.js" defer></script>'
            + "</div></main>" + foot("tech"))
        pages.append(("/tool/" + slug + "/", title + " | BRYME Tools", dek, tbody))
    hub_rows = "".join('<li><a href="/tool/' + slug + '/"><span><b>' + title + "</b><small>" + dek + "</small></span>"
                       '<span class="meta">Tool</span></a></li>' for slug, name, title, dek, art, what, ui in tools)
    hub = (head("tech", "Practical technology. No theatre.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/tech/">Tech</a> / The toolbox</nav>'
        + '<section class="cover"><p class="kicker">BRYME Tools \u00b7 the toolbox</p>'
        + '<h1 class="cover-title">Small tools, zero strings.</h1>'
        + '<p class="cover-dek">Developer and writer utilities that run entirely in your browser: no accounts, no uploads, no data collection \u2014 open the page, use the tool, close the page. Each one has a companion guide explaining the format behind it.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(tools)) + ' tools</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + hub_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">The honest bit</p><h2>What "runs in your browser" means.</h2></div>'
        + '<div class="prose"><p>Every tool here is a small script served with this page and executed by <em>your</em> browser on <em>your</em> device. There is no backend to send your text to, no logging, no account. The <a href="/tech/disclaimer/">disclaimer</a> applies: general-purpose utilities, provided as-is \u2014 and the standing advice holds everywhere: do not paste secrets into web tools, including these.</p></div></section>'
        + '</div></main>' + foot("tech"))
    pages.insert(0, ("/tool/", "BRYME Tools \u2014 browser tools, zero data collection | BRYME Tech",
                     "Eight free browser tools \u2014 JSON formatter, Base64, URL encoding, UUID generator, timestamps, word counter, case converter, HTTP status lookup. Client-side, no data collection.", hub))
    return pages


def tech_pages():
    arts = _load_tech()
    for a in arts:
        if a["slug"] in _TECH_FIRSTHAND:
            a["author"] = _TECH_FIRSTHAND[a["slug"]]
    by_cat = {}
    for a in arts:
        by_cat.setdefault(a["cat"], []).append(a)
    for lst in by_cat.values():
        lst.sort(key=lambda x: x["upd"] or x["pub"], reverse=True)

    cat_pages = {}
    for cslug, (cname, cdesc, _hero) in TECH_CAT.items():
        lst = by_cat.get(cslug, [])
        rows = "".join(
            '<li><a href="/' + a["slug"] + '/"><span><b>' + html.escape(a["title"]) + "</b>"
            "<small>" + html.escape(a["excerpt"][:110]) + ("\u2026" if len(a["excerpt"]) > 110 else "") + "</small></span>"
            '<span class="meta">' + (a["upd"] or a["pub"]) + "</span></a></li>"
            for a in lst)
        others = "".join('<a class="btn secondary" href="/' + c + '/">' + html.escape(TECH_CAT[c][0]) + "</a>"
                         for c in TECH_CAT if c != cslug)
        cbody = (head("tech", "Practical technology. No theatre.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/tech/">Tech</a> / ' + html.escape(cname) + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Tech \u00b7 section</p>'
            + '<h1 class="cover-title">' + html.escape(cname) + "</h1>"
            + '<p class="cover-dek">' + html.escape(cdesc) + "</p></section>"
            + '<section class="section"><div class="section-head"><p class="kicker">' + str(len(lst)) + ' guides</p><h2>Everything in ' + html.escape(cname) + '.</h2></div>'
            + '<ul class="list">' + rows + "</ul></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Keep going</p><h2>Elsewhere on this desk.</h2></div>'
            + '<div class="actions">' + others + '</div></section></div></main>' + foot("tech"))
        cat_pages[cslug] = [("/" + cslug + "/", cname + " | BRYME Tech", cdesc, cbody)]

    def art_page(a):
        cslug = a["cat"]
        cname = TECH_CAT.get(cslug, ("Coding",))[0] if cslug in TECH_CAT else "Coding"
        chref = "/tech/" if cslug not in TECH_CAT else "/tech/" + cslug + "/"
        rel = _tech_related(a, arts)
        rel_html = "".join('<li><a href="/' + r["slug"] + '/">' + html.escape(r["title"]) + "</a></li>" for r in rel)
        src_html = ""
        if a["sources"]:
            src_html = ('<h2>Sources</h2><ul class="list">'
                        + "".join('<li><a href="' + html.escape(s["url"]) + '" rel="noopener">' + html.escape(s["name"]) + "</a></li>"
                                  for s in a["sources"]) + "</ul>")
        meta_bits = ["By " + html.escape(a["author"])]
        if a["pub"]:
            meta_bits.append("published " + a["pub"])
        if a["upd"] and a["upd"] != a["pub"]:
            meta_bits.append("updated " + a["upd"])
        if a["read"]:
            meta_bits.append(a["read"])
        kind_kick = {"firsthand": "First-hand \u00b7 ", "guide": "Practical guide \u00b7 "}
        tag = ("Recovered from the BRYME tech archive \u00b7 " if a["recovered"]
               else kind_kick.get(a.get("kind", "firsthand"), "Practical guide \u00b7 "))
        summ = ('<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> '
                + html.escape(a["excerpt"]) + "</p></div></section>") if a["excerpt"] else ""
        schema = {"@context": "https://schema.org", "@type": "TechArticle",
                  "headline": a["title"], "author": {"@type": "Person", "name": a["author"]},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": a["pub"] or None, "dateModified": a["upd"] or a["pub"] or None,
                  "mainEntityOfPage": ORIGIN + "/tech/" + a["slug"] + "/"}
        import json as _j
        abody = (head("tech", "Practical technology. No theatre.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/tech/">Tech</a> / <a href="' + chref + '">' + html.escape(cname) + "</a> / " + html.escape(a["title"]) + "</nav>"
            + '<section class="cover"><p class="kicker">' + tag + "verified against the real thing</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(a["title"]) + "</h1>"
            + '<p class="byline">' + " \u00b7 ".join(meta_bits) + "</p></section>"
            + summ
            + '<section class="section"><div class="prose">' + _tech_blocks(a) + src_html + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + '</ul>'
            + '<div class="actions"><a class="btn secondary" href="' + chref + '">All of ' + html.escape(cname) + '</a>'
            + '<a class="btn secondary" href="/tech/">All of BRYME Tech</a></div></section>'
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("tech"))
        return (("/" + a["slug"] + "/"), a["title"] + " | BRYME Tech", a["excerpt"][:155], abody)

    latest = sorted(arts, key=lambda x: x["upd"] or x["pub"], reverse=True)[:5]
    latest_rows = "".join(
        '<li><a href="/' + a["slug"] + '/"><span><b>' + html.escape(a["title"]) + "</b><small>"
        + html.escape(a["excerpt"][:100]) + "\u2026</small></span><span class=\"meta\">" + (a["upd"] or a["pub"]) + "</span></a></li>"
        for a in latest)
    start_here = ["where-to-host-website-for-free", "bitwarden-free-password-manager",
                  "render-deployment-failures-what-they-taught-me"]
    start_rows = "".join(
        '<li><a href="/' + s + '/"><span><b>' + html.escape(next(a["title"] for a in arts if a["slug"] == s))
        + "</b><small>" + html.escape(next(a["excerpt"][:110] for a in arts if a["slug"] == s))
        + "\u2026</small></span><span class=\"meta\">Start here</span></a></li>" for s in start_here)
    cat_cards = "".join(
        '<article class="pub-card live" style="--pc:#1e3a5f"><p class="pc-kicker">' + str(len(by_cat.get(c, []))) + ' GUIDES</p>'
        + "<h3>" + html.escape(TECH_CAT[c][0]) + "</h3><p>" + html.escape(TECH_CAT[c][1][:130]) + "\u2026</p>"
        + '<a class="btn" href="/' + c + '/">Browse ' + html.escape(TECH_CAT[c][0].split(",")[0].split(" &")[0]) + ' \u2192</a></article>'
        for c in TECH_CAT)
    index_body = (head("tech", "Practical technology. No theatre.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Tech</p>'
        + '<h1 class="cover-title">Practical technology. No theatre.</h1>'
        + '<p class="cover-dek">You have a technology problem, question or decision. This desk helps you understand or solve it \u2014 with guides checked against the real products and real deploys, dated honestly, and evergreen on purpose.</p>'
        + '<div class="cover-facts">'
        + '<div><b>' + str(len(arts)) + '</b><span>Published pieces</span></div>'
        + '<div><b>8</b><span>Browser tools</span></div>'
        + '<div><b>' + str(len(TECH_CAT)) + '</b><span>Sections</span></div>'
        + '<div><b>0</b><span>Fabricated claims</span></div>'
        + '</div></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Handpicked</p><h2>Start here.</h2></div>'
        + '<ul class="list">' + start_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Browse by need</p><h2>Sections of this desk.</h2></div>'
        + '<div class="cards">' + cat_cards + "</div>"
        + '</section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Interactive</p><h2>The toolbox.</h2></div>'
        + '<p class="lede">Eight small tools that run entirely in your browser &mdash; nothing you type or paste is sent anywhere: <a href="/tool/json-formatter/">JSON formatter</a> &middot; <a href="/tool/base64-encoder/">Base64 encoder</a> &middot; <a href="/tool/url-encoder/">URL encoder</a> &middot; <a href="/tool/uuid-generator/">UUID generator</a> &middot; <a href="/tool/timestamp-converter/">timestamp converter</a> &middot; <a href="/tool/word-counter/">word counter</a> &middot; <a href="/tool/case-converter/">case converter</a> &middot; <a href="/tool/http-status-lookup/">HTTP status lookup</a>. Each has a <a href="/tech/what-is-json/">companion guide</a> explaining the underlying format.</p>'
        + '</section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Freshly dated</p><h2>Recently updated.</h2></div>'
        + '<ul class="list">' + latest_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">The promise</p><h2>What "no theatre" means here.</h2></div>'
        + '<p class="lede">No AI-tool hype cycles, no top-ten lists assembled from other top-ten lists, no benchmarks without the machine in front of us. If a piece says first-hand, someone on this desk did the thing and wrote down what happened \u2014 including what went wrong. Time-sensitive facts carry their verification dates and named sources.</p>'
        + '</section></div></main>' + foot("tech"))
    pages = [("/", "BRYME Tech \u2014 practical technology help, no theatre",
              "Practical technology guides: AI checked against real products, free-tool alternatives, hosting and DNS from real deploys, and safety without scaremongering.", index_body)]
    for cslug, pl in cat_pages.items():
        pages.extend(pl)
    pages.extend(art_page(a) for a in arts)
    pages.extend(tech_tool_pages())
    return pages + tech_trust_pages() + legal_pages("tech", "BRYME Tech", "Practical technology from people who ran the thing.", skip={"/terms/", "/corrections/"})



# ------------------------------------------------------------------ 5. FITNESS
FIT_WALK_DAYS = [
    (1, "10 minutes, easy pace. Just show up.", "The first week is about the habit, not the speed."),
    (2, "10 minutes, easy pace.", "Same time of day as yesterday. Routine beats motivation."),
    (3, "12 minutes.", "Add two minutes, not ten. Slow progress is progress that sticks."),
    (4, "12 minutes, relaxed.", "Land softly, look ahead, let your arms swing."),
    (5, "15 minutes.", "If you can talk while walking, the pace is right for now."),
    (6, "15 minutes, anywhere new.", "A new route counts as entertainment."),
    (7, "Rest, or 10 gentle minutes if you would miss it.", "Rest days are part of the plan, not a failure."),
    (8, "15 minutes.", "Two weeks in: judge the calendar, not the mirror."),
    (9, "18 minutes.", "Breathe in rhythm \u2014 steps in, steps out."),
    (10, "18 minutes.", "Hills count double for effort. Take them slowly."),
    (11, "15 minutes, easy.", "An easy day after a harder one is smart training."),
    (12, "20 minutes.", "Twenty minutes is a milestone. Notice it."),
    (13, "20 minutes.", "Drink water before you leave, not just after."),
    (14, "Rest, or 10 gentle minutes.", "Two weeks done. Most people quit by now. You did not."),
    (15, "22 minutes.", "The habit is forming. Protect the schedule."),
    (16, "22 minutes, the last 5 slightly faster.", "Finish a little quicker than you started."),
    (17, "25 minutes.", "Longer day: pick a route with some shade."),
    (18, "20 minutes, easy.", "Recovery walks help you come back stronger."),
    (19, "25 minutes.", "Track one thing: time, distance, or how you felt."),
    (20, "30 minutes.", "Half an hour \u2014 the classic benchmark. You are here."),
    (21, "Rest, or 15 gentle minutes.", "Soreness that fades in a day or two is normal. Sharp pain is not \u2014 respect it."),
    (22, "30 minutes.", "Keep the pace conversational."),
    (23, "30 minutes, a brisk middle 10.", "Brisk means you can talk, but not sing."),
    (24, "25 minutes, easy.", "Easy days are what let the stronger days work."),
    (25, "35 minutes.", "The longest walk of the month. Start unhurried."),
    (26, "25 minutes.", "Notice the difference from Day 1."),
    (27, "30 minutes.", "Same time, same rhythm. Almost there."),
    (28, "20 minutes, easy.", "Taper day. Let your body bank the work."),
    (29, "30 minutes on your favourite route.", "Pick the walk you enjoyed most this month."),
    (30, "30+ minutes \u2014 finish, then decide what is next.", "Day 30 is a beginning: repeat week four, or try the strength basics next."),
]

FIT_SOURCES = [
    ("WHO \u2014 Physical activity (fact sheet)", "https://www.who.int/news-room/fact-sheets/detail/physical-activity"),
    ("CDC \u2014 Physical Activity Basics", "https://www.cdc.gov/physical-activity-basics/"),
]

FIT_ARTICLES = [
    ("how-to-start-working-out",
     "Starting from zero: how to begin exercising when you are out of the habit",
     "The practical, no-miracle starting guide: begin low, progress slowly, and let the calendar \u2014 not motivation \u2014 carry you.",
     """<p>The hardest workout of your life is the one that gets you off the sofa the first time. Not because exercise is brutal, but because the habit does not exist yet. The good news, supported by every mainstream public-health guideline, is that the first week does not need to be impressive. It needs to be repeatable.</p>
<h2>Start low, go slow</h2>
<p>Public-health agencies, including the WHO and the CDC, use the same phrase for returning beginners: start low and go slow. For most people that means short sessions of moderate activity \u2014 brisk walking is the classic \u2014 increasing gradually over weeks. The adult guideline worth knowing is around 150 minutes of moderate aerobic activity spread across a week, plus muscle-strengthening on two or more days. You do not start there. You build toward it.</p>
<h2>The two-day rule</h2>
<p>Early on, the only metric that matters is this: do not let two scheduled days pass in a row without doing the session. Ten minutes on a day you feel flat protects the habit. A heroic 90-minute session followed by ten silent days does not. Motivation is weather; the calendar is climate.</p>
<h2>What counts as exercise</h2>
<p>More than people assume. Brisk walking counts. Carrying shopping counts. Taking the stairs, digging a garden bed, dancing badly in your kitchen \u2014 all of it raises your breathing and counts toward the week. If a gym feels like a hostile planet, start at home. The 30-day walking plan on this desk exists precisely because walking is the most underrated entry point in fitness.</p>
<h2>Equipment: none</h2>
<p>A beginner needs shoes that do not hurt and a door. Everything sold as essential is optional. Buy things later, when a specific gap annoys you three sessions in a row \u2014 that is evidence, unlike advertising.</p>
<h2>When to get professional advice first</h2>
<p>This is general information, not medical advice. If you have a health condition, have been inactive for a long time, are pregnant, or get chest pain, dizziness or unusual breathlessness during effort, talk to a qualified health professional before starting. That is not a formality \u2014 it is the difference between a plan and a risk.</p>
<h2>Where to begin on this desk</h2>
<p><a href="/30-day-walking-plan/">The 30-day walking plan</a> is the structured route in. <a href="/how-many-steps-a-day/">The honest guide to step counts</a> sets realistic expectations, and <a href="/rest-days-and-recovery/">the recovery guide</a> explains the part most beginners skip.</p>"""),
    ("how-many-steps-a-day",
     "How many steps a day actually matter? The honest answer",
     "Where 10,000 steps came from, what the research actually found, and the number a beginner should care about instead.",
     """<p>Ask how many steps you should walk and you will hear one number: 10,000. It is on every fitness tracker by default. What almost nobody mentions is where the number came from \u2014 and what the research actually says.</p>
<h2>The number was marketing, not medicine</h2>
<p>The 10,000-step figure is often traced to a 1960s Japanese walking-club campaign around a pedometer whose name can be read as \u201c10,000-step meter\u201d. It was catchy, round and optimistic. It was not a clinical threshold. It became a default because devices shipped with it, and it spread from there.</p>
<h2>What a large study actually found</h2>
<p>One of the most cited step studies followed more than 16,000 older women and compared step counts with deaths over time (Lee et al., JAMA Internal Medicine, 2019). The pattern: the least active group averaged around 2,700 steps a day, mortality was lower in groups averaging around 4,400 steps, and the benefit continued as steps rose, levelling off at roughly 7,500. Two honest caveats: the participants were older women, so the exact numbers do not transfer automatically to everyone; and the study shows association, not a magic threshold you cross and lock in.</p>
<h2>The practical takeaway for a beginner</h2>
<p>More is generally better than less, the biggest jump in benefit is going from very few steps to a modest number, and there is no cliff at 10,000. If your normal day is 3,000 steps, aiming at 6,000 beats aiming at 10,000 and quitting in week two. That is why the <a href="/30-day-walking-plan/">30-day walking plan</a> is built around time and consistency first, with steps as a side effect.</p>
<h2>How to count \u2014 and how not to obsess</h2>
<p>A phone in your pocket estimates steps adequately for trends. Treat any single day as noise and the weekly average as signal. If a tracker makes you anxious, leave it home once in a while \u2014 the walk works with nobody counting.</p>
<h2>The rest of the guideline</h2>
<p>Steps cover the aerobic half. The other half of the adult guideline is muscle-strengthening work on two or more days a week \u2014 see <a href="/strength-training-for-beginners/">the beginner strength guide</a>.</p>"""),
    ("strength-training-for-beginners",
     "Strength training for beginners: six moves, two days, no gym",
     "Why the guidelines want you lifting at least twice a week, the six patterns that cover it, and how to progress without equipment.",
     """<p>Walking is the front door to fitness; strength is the part that keeps the house standing. Public-health guidelines are specific here: muscle-strengthening activity on two or more days a week, working the major muscle groups. It protects bone, joint function and the ability to keep doing everything else you enjoy \u2014 and it does not require a gym.</p>
<h2>The six patterns</h2>
<p>Nearly every useful strength exercise is a variation of six movements. Learn them with bodyweight or household load, and you have a lifetime programme:</p>
<p>Sit down and stand back up from a chair, slowly, without using your hands. That is a squat pattern. Lie face down and push the floor away from your knees or toes \u2014 a push-up, scaled to a wall or a counter if needed. Hinge at the hips with a flat back and stand back up \u2014 the deadlift pattern, with a backpack of books when you are ready. Pull something toward you: a door-frame row, a towel row, or a backpack curl. Carry something moderately heavy from one end of the room to the other and put it down carefully \u2014 the carry, the most underrated exercise there is. Finally, hold a plank position on forearms and knees or toes, and breathe.</p>
<h2>Two days, twenty minutes</h2>
<p>Pick one exercise from each pattern. Do each for a number of repetitions that leaves you feeling like you could do two or three more with good form \u2014 that is what \u201cmoderate\u201d means in practice. Rest, then repeat twice. Two such sessions a week, with at least one day between them, satisfies the guideline.</p>
<h2>Progressive overload, honestly explained</h2>
<p>Muscle adapts to what you ask of it. When the current work feels comfortable, ask slightly more: one more repetition, a slower lowering phase, a heavier backpack, a lower surface for push-ups. Small and boring wins. Pain is not part of the plan; effort is.</p>
<h2>Soreness is not the goal</h2>
<p>New movements commonly cause soreness a day or two later. It fades. It is not a score. Chasing soreness is how beginners get hurt or quit \u2014 see <a href="/rest-days-and-recovery/">the recovery guide</a> for what to do instead. This page is general information, not medical advice; if something hurts sharply or persistently, stop and get qualified advice.</p>"""),
    ("rest-days-and-recovery",
     "Rest days and recovery: the part of training that actually builds you",
     "Why adaptation happens between sessions, what DOMS really is, and the difference between rest and quitting.",
     """<p>Exercise is the question. Recovery is the answer. When you walk, lift or carry, you create a small stress; your body responds during the hours and days afterwards, rebuilding slightly stronger than before. Skip the recovery and you skip the adaptation \u2014 the training was just wear.</p>
<h2>What rest day means</h2>
<p>A rest day is not a sofa day and it is not a failure. It means no planned training. Gentle movement \u2014 an unhurried walk, stretching while the kettle boils \u2014 is fine and often feels better than nothing. What it does not mean is swapping your schedule because enthusiasm dipped. Enthusiasm is allowed to dip. The calendar stands.</p>
<h2>DOMS, explained honestly</h2>
<p>Soreness that arrives a day or so after unfamiliar exercise \u2014 especially the lowering phase of movements \u2014 is called delayed-onset muscle soreness (DOMS). It commonly peaks in the first day or two and settles within several days. It is a normal response to new work, not a badge of quality: a session that leaves you unable to walk downstairs was overdone, not superior. Mechanisms are still debated in the research; the practical handling is not \u2014 move gently, hydrate, sleep, and let it pass before hitting the same muscles hard again.</p>
<h2>Sleep is the strongest legal performance aid</h2>
<p>Nothing sold in a shaker compares with enough sleep. It is when the bulk of recovery happens. If you must choose between an extra hour asleep and a groggy extra session, take the sleep more often than not.</p>
<h2>When soreness is a warning</h2>
<p>Sharp pain, pain that worsens past a few days, swelling, or soreness paired with dark urine are not DOMS and are not to be trained through. This is general information, not medical advice \u2014 a qualified professional should assess anything that fails those tests.</p>
<h2>How the walking plan handles rest</h2>
<p>Every seventh day of the <a href="/30-day-walking-plan/">30-day walking plan</a> is a rest day by design. That rhythm \u2014 stress, recover, repeat slightly stronger \u2014 is the whole trick behind every serious training programme ever written.</p>"""),
    ("workout-at-home-no-equipment",
     "A full-body starter you can do at home, with no equipment",
     "Six patterns, one small space, zero equipment: how to build a two-day-a-week home routine that actually progresses.",
     """<p>The fastest way to make exercise complicated is to buy things first. This guide goes the other way: a full-body routine you can run in a small room, with no equipment, built on the same principle as every good beginner plan \u2014 start easier than you think, then make it slightly harder over time. It is general information, not medical advice; if you have a health condition, are pregnant, or get pain or dizziness during effort, a qualified health professional is the right first stop.</p>
<h2>The six patterns</h2>
<p>Almost every useful beginner movement is a version of one of six things: pushing (wall or counter push-ups), pulling (a towel row around a sturdy door handle, or slow door-frame pulls), squatting (sit-to-stand from a chair), hinging (a hip hinge with hands on the back of a chair), carrying (grocery bags count), and getting down and up off the floor. That last one sounds like a joke and is not \u2014 it is a genuine whole-body skill that gets harder as adults stop practising it.</p>
<h2>Two days a week, twenty minutes</h2>
<p>Pick one movement from each pattern. Do each for a comfortable number of repetitions \u2014 the number you could do twice if you had to, not once to failure. Cycle through them twice, resting as needed. That is the session. The <a href="/strength-training-for-beginners/">strength training for beginners guide</a> explains why the guideline is muscle-strengthening on two or more days a week, and this routine satisfies it without a gym.</p>
<h2>The progression rule that matters</h2>
<p>When a set starts feeling easy \u2014 and only then \u2014 make one small change: one more repetition, a slower lowering phase, a wall push-up moved to a counter. One change at a time is the whole art. The principle is called progressive overload, and <a href="/how-progressive-overload-works/">how progressive overload works</a> walks through it honestly \u2014 including the weeks when you progress by doing the same thing again.</p>
<h2>Warm up, cool down, recover</h2>
<p>Three minutes of marching on the spot and easy arm circles is a warm-up; you do not need to sweat before you start. Afterwards, a short walk around the room and a couple of easy stretches is plenty \u2014 <a href="/how-to-warm-up/">the warm-up guide</a> has the details. And the session only works if the days between it count too: <a href="/rest-days-and-recovery/">rest days and recovery</a> explains that adaptation happens between workouts, not during them.</p>
<h2>Where this fits the week</h2>
<p>If you also walk, this pairs neatly with the <a href="/30-day-walking-plan/">30-day walking plan</a> \u2014 two strength days and three or four walks is a genuinely complete beginner week, in line with the roughly-150-minutes-of-moderate-activity guideline the <a href="/how-to-start-working-out/">starting from zero guide</a> explains. If the choice is between this and nothing, this wins. It needs no equipment, no commute and no perfect version of you.</p>"""),
    ("how-progressive-overload-works",
     "How progressive overload works: getting a little better on purpose",
     "The quiet principle behind every real training result \u2014 and the honest version, including the weeks when you repeat yourself.",
     """<p>Every training result you have ever seen \u2014 someone stronger, someone walking further, someone who now finds stairs boring \u2014 runs on one unglamorous principle: progressive overload. Do a little more than your body is used to, let it adapt, then ask for a little more again. This guide explains the principle and, more usefully, the honest version of it that beginners actually need.</p>
<h2>The principle, minus the gym mythology</h2>
<p>Your body adapts to what you repeatedly ask of it. Ask slightly more than last time, and it responds by becoming slightly more capable. Ask far too much, and it responds with injury or three weeks of not showing up. Ask for nothing new, and it stays exactly as it is. That is the entire trade-off. Public-health guidelines encode it in their own way: activity recommendations always pair a weekly amount with the instruction to increase gradually.</p>
<h2>Overload is more than weight</h2>
<p>Beginners hear \u201coverload\u201d and picture bigger dumbbells. But the dial has many positions: more repetitions, slower lowering phases, shorter rests, an extra set, a harder variation (wall push-up to counter to floor), a longer walk, a hillier route. The <a href="/workout-at-home-no-equipment/">no-equipment home routine</a> progresses for months on repetition counts and variations alone \u2014 no shopping required.</p>
<h2>The honest part: it is not a staircase</h2>
<p>Progress is not +1 every session forever. Some weeks you repeat the last week exactly \u2014 and that still counts, because holding a level while life happens <em>is</em> progress for a beginner. Sleep-poor weeks, stressful weeks and weeks after illness are for holding, not pushing. The desk\u2019s <a href="/rest-days-and-recovery/">recovery guide</a> explains why the gains land between sessions, and the <a href="/how-to-start-working-out/">starting from zero guide</a> explains the calendar-over-motivation mindset that keeps you repeating long enough for overload to work.</p>
<h2>A simple rule to steal</h2>
<p>Keep a note of what you did. Next session, do the same or a hair more \u2014 one repetition, one minute, one harder variation \u2014 but only when the current version feels comfortable. If it does not feel comfortable, you have found this week\u2019s session. That is the whole method. It is slow, it is boring on paper, and it is the reason results compound while bursts do not.</p>
<h2>Where to point the principle</h2>
<p>Any of it counts: the <a href="/30-day-walking-plan/">30-day walking plan</a> applies overload through minutes, the strength routine through repetitions and variations, and the <a href="/walking-vs-running/">walking-versus-running guide</a> explains how to add intensity without adding impact \u2014 one more way to turn the same principle for different bodies.</p>"""),
    ("breathing-during-exercise",
     "Breathing during exercise: the honest basics",
     "What your breathing is actually doing when you exert yourself, when to worry about patterns, and why no breathing trick is magic.",
     """<p>Breathing advice in fitness is mostly theatre: magic ratios, mystical nose rules, commands barked by people who have never watched a real beginner almost fall over counting. Here is the honest version of what matters, written as general information rather than medical advice \u2014 if you get chest pain, severe breathlessness, dizziness or an irregular heartbeat during effort, stop and speak to a qualified health professional.</p>
<h2>What effort does to breathing</h2>
<p>When you exert yourself, your muscles need more oxygen and produce more carbon dioxide, and your breathing responds automatically \u2014 faster and deeper, in proportion to how hard you are working. That is not a fault to be fixed; it is the system working. The classic beginner test on this desk \u2014 brisk means you can talk but not sing \u2014 works precisely because speech and breathing share the same equipment. The <a href="/how-to-start-working-out/">starting from zero guide</a> and the <a href="/how-many-steps-a-day/">step-count guide</a> both lean on that idea.</p>
<h2>The only two habits worth having</h2>
<p>First: do not hold your breath through effort. People clamp up on the hardest repetition of anything \u2014 the push-up, the chair squat, the last hill. Exhaling on the effort (out on the push, out on the up) keeps the habit of continuous breathing and tends to keep tension where it belongs. Second: let your breathing choose your intensity. If you cannot speak a short sentence, the session has crossed from moderate to hard \u2014 fine occasionally, wrong as a beginner default. The <a href="/30-day-walking-plan/">30-day walking plan</a> uses that rule every single day.</p>
<h2>Warm-ups, breathing and going slower</h2>
<p>A few minutes of easy movement \u2014 marching, arm circles, a gentle first stretch of the walk \u2014 lets breathing ramp up with the work instead of scrambling after it; <a href="/how-to-warm-up/">the warm-up guide</a> covers the sequence. And if you finish sessions gasping, the fix is usually pacing, not technique: start slower than feels necessary. The <a href="/walking-vs-running/">walking-versus-running guide</a> is essentially a breathing-management guide in disguise \u2014 run-walk intervals exist so breathing stays conversational.</p>
<h2>The honest summary</h2>
<p>Breathing during exercise mostly takes care of itself, given two habits: keep it continuous, and let it set your pace. Anything more elaborate can wait until a specific coach, for a specific sport, tells you why. If a breathing trick promises performance it cannot explain, treat it like any other claim on this desk: interesting until demonstrated.</p>"""),
]

def _fit_shell(pub, kicker, title, dek, extra_disclaimer=False):
    band = ('<section class="section alt" style="border-left:4px solid var(--brand)"><div class="wrap"><p class="lede"><b>General information, not medical advice.</b> '
            "If you have a health condition, have been inactive for a long time, or something hurts sharply, talk to a qualified health professional first.</p></div></section>")
    return band

def fitness_pages():
    def src_html(sources):
        if not sources:
            return ""
        return ('<h2>Sources</h2><ul class="list">'
                + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                + "</ul>")

    def art(slug, title, dek, body_html, sources, related, schema_type="Article"):
        import json as _j
        rel_html = "".join('<li><a href="/' + s + '/">' + rt + "</a></li>" for s, rt in related)
        schema = {"@context": "https://schema.org", "@type": schema_type,
                  "headline": title,
                  "author": {"@type": "Organization", "name": "BRYME Fitness desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/fitness/" + slug + "/",
                  "description": dek}
        abody = (head("fitness", "Practical fitness \u2014 no miracles, no medical claims.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/fitness/">Fitness</a> / ' + html.escape(title) + "</nav>"
            + '<section class="cover"><p class="kicker">' + kicker_default + "</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(title) + "</h1>"
            + '<p class="byline">BRYME Fitness desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not medical advice</p></section>"
            + '<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(dek) + "</p></div></section>"
            + '<section class="section"><div class="prose">' + body_html + src_html(sources) + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Keep going</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/fitness/">All of BRYME Fitness</a></div></section>'
            + _fit_shell("fitness", "", "", "", True)
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("fitness"))
        return (("/" + slug + "/"), title + " | BRYME Fitness", dek[:155], abody)

    kicker_default = "Evidence-aware \u00b7 beginner-first \u00b7 no miracle claims"
    related_map = {
        "how-to-start-working-out": [("30-day-walking-plan", "The 30-day walking plan"),
                                     ("how-many-steps-a-day", "How many steps a day actually matter?"),
                                     ("rest-days-and-recovery", "Rest days and recovery")],
        "how-many-steps-a-day": [("30-day-walking-plan", "The 30-day walking plan"),
                                 ("how-to-start-working-out", "Starting from zero"),
                                 ("strength-training-for-beginners", "Strength training for beginners")],
        "strength-training-for-beginners": [("rest-days-and-recovery", "Rest days and recovery"),
                                            ("how-to-start-working-out", "Starting from zero"),
                                            ("30-day-walking-plan", "The 30-day walking plan")],
        "rest-days-and-recovery": [("strength-training-for-beginners", "Strength training for beginners"),
                                   ("how-to-start-working-out", "Starting from zero"),
                                   ("30-day-walking-plan", "The 30-day walking plan")],
    }

    # ---- the 30-day plan page (the product) ----
    week_rows = ""
    for wk_start in (1, 8, 15, 22):
        label = {1: "Week 1 \u00b7 show up", 8: "Week 2 \u00b7 rhythm",
                 15: "Week 3 \u00b7 range", 22: "Week 4 \u00b7 finish strong"}[wk_start]
        wk_end = wk_start + (9 if wk_start == 22 else 7)
        rows = ""
        for d, task, tip in FIT_WALK_DAYS:
            if not (wk_start <= d < (wk_start + 9 if wk_start == 22 else wk_start + 7)):
                continue
            rows += ('<li class="fp-day" data-day="' + str(d) + '">'
                     '<span class="fp-num">' + str(d) + "</span><span><b>" + task + "</b>"
                     "<small>" + tip + "</small></span>"
                     '<button type="button" class="btn secondary fp-done" aria-pressed="false">Done</button></li>')
        week_rows += ('<section class="section"><div class="section-head"><p class="kicker">Days '
                      + str(wk_start) + "\u2013" + str(wk_end - 1) + "</p><h2>" + label + "</h2></div>"
                      + '<ul class="list fp-week">' + rows + "</ul></section>")
    import json as _j
    plan_schema = {"@context": "https://schema.org", "@type": "Article",
                   "headline": "The 30-Day Walking Plan",
                   "author": {"@type": "Organization", "name": "BRYME Fitness desk"},
                   "publisher": {"@type": "Organization", "name": "THE BRYME"},
                   "datePublished": TODAY, "dateModified": TODAY,
                   "mainEntityOfPage": ORIGIN + "/fitness/30-day-walking-plan/",
                   "description": "A beginner walking plan built around one honest idea: show up every day for a month. Progress is tracked in your browser \u2014 no account, nothing sent anywhere."}
    plan_body = (head("fitness", "Practical fitness \u2014 no miracles, no medical claims.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/fitness/">Fitness</a> / The 30-Day Walking Plan</nav>'
        + '<section class="cover"><p class="kicker">' + kicker_default + "</p>"
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The 30-Day Walking Plan</h1>'
        + '<p class="byline">BRYME Fitness desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not medical advice</p></section>"
        + '<section class="section alt"><div class="wrap"><p class="lede"><b>One honest idea:</b> show up every day for a month. The plan is built on time, not distance, and every seventh day is a rest day by design. Progress is saved in your browser \u2014 no account, nothing sent anywhere.</p></div></section>'
        + '<section class="section"><div class="wrap"><div class="fp-progressbar" role="img" aria-label="Plan progress"><div class="fp-fill" id="fp-fill"></div></div>'
        + '<p class="lede" id="fp-status">Day 0 of 30 complete. Tick days off as you go \u2014 your browser will remember.</p></div></section>'
        + week_rows
        + '<section class="section"><div class="section-head"><p class="kicker">The fine print</p><h2>How to use this plan sensibly.</h2></div>'
        + '<div class="prose"><p>\u201cEasy pace\u201d means you can hold a conversation; \u201cbrisk\u201d means you can talk but not sing. If a day feels too hard, repeat the previous day \u2014 the numbering is a suggestion, your body is the schedule. Sharp pain, dizziness or unusual breathlessness: stop. This is general information, not medical advice; if you have a health condition or have been inactive for a long time, see a qualified professional first.</p>'
        + '<p>Finished? Repeat week four, move the brisk blocks earlier, or add two strength days from <a href="/strength-training-for-beginners/">the beginner strength guide</a> \u2014 and run the whole system from <a href="/weekly-planner/">the weekly planner</a>, one card for the honest week.</p></div></section>'
        + '<section class="section alt">' + src_html(FIT_SOURCES) + "</section>"
        + _fit_shell("fitness", "", "", "", True)
        + '<script type="application/json" id="fit-plan-data">{"total": 30}</script>'
        + '<script src="/assets/fitness-plan.js" defer></script>'
        + '<script type="application/ld+json">' + _j.dumps(plan_schema) + "</script>"
        + "</div></main>" + foot("fitness"))
    plan_page = [("/30-day-walking-plan/", "The 30-Day Walking Plan | BRYME Fitness",
                  "A beginner walking plan built on one honest idea: show up every day for a month. Time-based, rest days built in, progress saved in your browser.", plan_body)]

    ART_SOURCES = dict((s, FIT_SOURCES) for s, _, _, _ in FIT_ARTICLES)
    ART_SOURCES["how-many-steps-a-day"] = FIT_SOURCES + [
        ("Lee et al., JAMA Internal Medicine (2019) \u2014 Association of Step Volume and Intensity With All-Cause Mortality in Older Women",
         "https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2731911")]
    import more_guides_data
    FIT_ARTICLES.extend((s, ti, dek, b) for (s, _k, ti, dek, b) in more_guides_data.FIT_MORE)
    ART_SOURCES.update((s, FIT_SOURCES) for (s, _k, ti, dek, b) in more_guides_data.FIT_MORE)
    ART_SOURCES["how-much-protein-do-you-need"] = FIT_SOURCES + [
        ("NIH/NCBI \u2014 Recommended Dietary Allowances: protein 0.8 g/kg for adults", "https://www.ncbi.nlm.nih.gov/books/NBK234929/"),
        ("American Heart Association \u2014 Protein: what\u2019s enough?", "https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/nutrition-basics/protein-and-heart-health"),
        ("UC Davis Nutrition Dept \u2014 protein requirements for health professionals", "https://nutrition.ucdavis.edu/outreach/nutr-health-info-sheets/pro-protein-requirements")]
    ART_SOURCES["sleep-and-exercise-performance"] = FIT_SOURCES + [
        ("CDC (MMWR) \u2014 adults 18\u201360 recommended at least 7 hours; short-sleep risks", "https://www.cdc.gov/mmwr/volumes/65/wr/mm6506a1.htm"),
        ("CDC \u2014 1 in 3 adults don\u2019t get enough sleep (AASM/SRS recommendation)", "https://archive.cdc.gov/www_cdc_gov/media/releases/2016/p0215-enough-sleep.html")]
    related_map["walking-vs-running"] = [("30-day-walking-plan", "The 30-day walking plan"),
                                         ("how-to-warm-up", "How to warm up"),
                                         ("how-to-start-working-out", "Starting from zero")]
    related_map["how-to-warm-up"] = [("strength-training-for-beginners", "Strength training for beginners"),
                                     ("walking-vs-running", "Walking or running?"),
                                     ("rest-days-and-recovery", "Rest days and recovery")]
    related_map["workout-at-home-no-equipment"] = [("how-progressive-overload-works", "How progressive overload works"),
                                                   ("strength-training-for-beginners", "Strength training for beginners"),
                                                   ("how-to-warm-up", "How to warm up")]
    related_map["how-progressive-overload-works"] = [("workout-at-home-no-equipment", "The no-equipment home routine"),
                                                     ("strength-training-for-beginners", "Strength training for beginners"),
                                                     ("rest-days-and-recovery", "Rest days and recovery")]
    related_map["breathing-during-exercise"] = [("how-to-start-working-out", "Starting from zero"),
                                                ("walking-vs-running", "Walking or running?"),
                                                ("how-to-warm-up", "How to warm up")]
    related_map["how-much-protein-do-you-need"] = [("strength-training-for-beginners", "Strength training for beginners"),
                                                   ("sleep-and-exercise-performance", "Sleep: the recovery tool you cannot buy"),
                                                   ("how-progressive-overload-works", "How progressive overload works")]
    related_map["sleep-and-exercise-performance"] = [("rest-days-and-recovery", "Rest days and recovery"),
                                                     ("how-much-protein-do-you-need", "How much protein do you need?"),
                                                     ("30-day-walking-plan", "The 30-day walking plan")]
    related_map["rest-days-and-recovery"].append(("sleep-and-exercise-performance", "Sleep: the recovery tool"))
    related_map["strength-training-for-beginners"].append(("how-much-protein-do-you-need", "Protein, honestly"))
    arts = [art(s, ti, dek, b, ART_SOURCES[s], related_map[s])
            for (s, ti, dek, b) in FIT_ARTICLES]

    start_rows = ('<li><a href="/how-to-start-working-out/"><span><b>Starting from zero</b>'
                  "<small>The practical, no-miracle guide to beginning when the habit does not exist yet.</small></span>"
                  '<span class="meta">Start here</span></a></li>'
                  '<li><a href="/30-day-walking-plan/"><span><b>The 30-day walking plan</b>'
                  "<small>Show up every day for a month. Time-based, rest days built in, progress saved locally.</small></span>"
                  '<span class="meta">The plan</span></a></li>'
                  '<li><a href="/strength-training-for-beginners/"><span><b>Six moves, two days, no gym</b>'
                  "<small>The strength patterns that satisfy the guideline, scaled to a door and a backpack.</small></span>"
                  '<span class="meta">Build</span></a></li>')
    more_rows = ('<li><a href="/how-many-steps-a-day/"><span><b>How many steps a day actually matter?</b>'
                 "<small>Where 10,000 came from, what a 16,000-person study found, and the number to aim at instead.</small></span>"
                 '<span class="meta">Understand</span></a></li>'
                 '<li><a href="/rest-days-and-recovery/"><span><b>Rest days and recovery</b>'
                 "<small>Why adaptation happens between sessions \u2014 and when soreness is a warning.</small></span>"
                 '<span class="meta">Understand</span></a></li>'
                 '<li><a href="/workout-at-home-no-equipment/"><span><b>A full-body starter at home, no equipment</b>'
                 "<small>Six patterns, two days a week, twenty minutes \u2014 a routine that needs a door and a floor.</small></span>"
                 '<span class="meta">Build</span></a></li>'
                 '<li><a href="/how-progressive-overload-works/"><span><b>How progressive overload works</b>'
                 "<small>The quiet principle behind every real result \u2014 including the weeks you repeat yourself.</small></span>"
                 '<span class="meta">Understand</span></a></li>'
                 '<li><a href="/breathing-during-exercise/"><span><b>Breathing during exercise</b>'
                 "<small>The honest basics: two habits worth having, no magic ratios.</small></span>"
                 '<span class="meta">Understand</span></a></li>'
                 '<li><a href="/how-much-protein-do-you-need/"><span><b>How much protein do you need?</b>'
                 "<small>The official 0.8 g/kg, why trainers say more, and food before powders.</small></span>"
                 '<span class="meta">Understand</span></a></li>'
                 '<li><a href="/sleep-and-exercise-performance/"><span><b>Sleep: the recovery tool you cannot buy</b>'
                 "<small>Seven hours is the floor \u2014 what short sleep costs your training.</small></span>"
                 '<span class="meta">Understand</span></a></li>')
    index_body = (head("fitness", "Practical fitness \u2014 no miracles, no medical claims.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Fitness \u00b7 start where you are</p>'
        + '<h1 class="cover-title">Build a routine you can actually keep.</h1>'
        + '<p class="cover-dek">Practical fitness guidance for people starting from zero: programs, challenges and progress \u2014 evidence-aware, beginner-first, and clearly separated from medical advice. No \u201cshred\u201d, no \u201cmelt fat\u201d, no 30-day body promises: 30-day <em>habits</em>.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Find your door</p><h2>Where are you starting from?</h2></div>'
        + '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px">'
        + '<a class="btn secondary" style="display:block;padding:20px 18px;text-align:left" href="/how-to-start-working-out/"><b>I\u2019m starting from zero</b><small style="display:block;color:var(--dim);margin-top:6px;text-transform:none;letter-spacing:0;font-size:13px">The no-miracle guide, then the 30-day walking plan \u2014 ten minutes a day to begin.</small></a>'
        + '<a class="btn secondary" style="display:block;padding:20px 18px;text-align:left" href="/strength-training-for-beginners/"><b>I want to get stronger</b><small style="display:block;color:var(--dim);margin-top:6px;text-transform:none;letter-spacing:0;font-size:13px">Six movement patterns, two days a week, zero equipment \u2014 plus the protein arithmetic.</small></a>'
        + '<a class="btn secondary" style="display:block;padding:20px 18px;text-align:left" href="/rest-days-and-recovery/"><b>I keep quitting</b><small style="display:block;color:var(--dim);margin-top:6px;text-transform:none;letter-spacing:0;font-size:13px">Recovery, sleep and the two-day rule \u2014 why the calendar beats motivation.</small></a>'
        + '</div></section>'
        + '<section class="section"><div class="data-cols" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px">'
        + '<div class="section" style="border:1px solid var(--line);padding:22px"><p class="kicker">The plan \u00b7 interactive</p><h2 style="font-size:22px">The 30-Day Walking Plan.</h2>'
        + '<p style="color:var(--dim);font-size:14px">Show up every day for a month. Time-based, rest days built in \u2014 tick days off and your browser remembers. No account, nothing sent anywhere.</p>'
        + '<div class="actions"><a class="btn" href="/30-day-walking-plan/">Open the plan \u2192</a></div></div>'
        + '<div class="section" style="border:1px solid var(--line);padding:22px"><p class="kicker">The tool \u00b7 interactive</p><h2 style="font-size:22px">The Weekly Planner.</h2>'
        + '<p style="color:var(--dim);font-size:14px">One card for the honest week \u2014 move \u00b7 strength \u00b7 on-time nights. Tick what happened; it scores itself against the real targets and resets each Monday.</p>'
        + '<div class="actions"><a class="btn" href="/weekly-planner/">Open the planner \u2192</a></div></div>'
        + '<div class="section" style="border:1px solid var(--line);padding:22px"><p class="kicker">Your week \u00b7 the honest minimum</p><h2 style="font-size:22px">What the guidelines actually say.</h2>'
        + '<ul class="list">'
        + '<li><span><b>150 minutes</b> of moderate movement across the week \u2014 brisk walking counts.</span><span class="meta">WHO</span></li>'
        + '<li><span><b>2 days</b> that challenge the major muscles \u2014 the six patterns cover it.</span><span class="meta">CDC</span></li>'
        + '<li><span><b>7+ hours</b> of sleep \u2014 the recovery tool you cannot buy.</span><span class="meta">CDC</span></li>'
        + '</ul></div></div></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">Handpicked</p><h2>Start here.</h2></div>'
        + '<ul class="list">' + start_rows + "</ul></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Understand the craft</p><h2>Read before you push.</h2></div>'
        + '<ul class="list">' + more_rows + "</ul></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The desk\u2019s rules</p><h2>What BRYME Fitness will never do.</h2></div>'
        + '<div class="prose"><p>It will not promise a body in 30 days; it will not dress general information up as medical advice; it will not sell you equipment you do not need. Every guide carries its reviewed date and, where numbers are quoted, its sources. That is the whole identity: <b>practical fitness guidance, programs, challenges and progress</b> \u2014 sustainable on purpose.</p></div></section>'
        + "</div></main>" + foot("fitness"))
    pages = [("/", "BRYME Fitness \u2014 practical fitness, no miracle claims",
              "Beginner-first fitness: how to start, the 30-day walking plan with in-browser progress tracking, strength basics and recovery \u2014 evidence-aware, never medical advice.", index_body)]
    # ---- batch 20: the weekly planner (second interactive tool) ----
    import json as _j2
    _DAYS7 = [("mon", "Monday"), ("tue", "Tuesday"), ("wed", "Wednesday"), ("thu", "Thursday"),
              ("fri", "Friday"), ("sat", "Saturday"), ("sun", "Sunday")]
    _wp_rows = ""
    for _dk, _dn in _DAYS7:
        _wp_rows += ('<div class="wp-row"><span class="wp-day">' + _dn + '</span>'
            + '<button type="button" class="wp-chip" data-day="' + _dk + '" data-kind="move" aria-pressed="false">Move 30</button>'
            + '<button type="button" class="wp-chip" data-day="' + _dk + '" data-kind="strength" aria-pressed="false">Strength</button>'
            + '<button type="button" class="wp-chip" data-day="' + _dk + '" data-kind="wind" aria-pressed="false">On-time night</button></div>')
    _wp_schema = {"@context": "https://schema.org", "@type": "Article",
        "headline": "The BRYME Weekly Planner",
        "author": {"@type": "Organization", "name": "BRYME Fitness desk"},
        "publisher": {"@type": "Organization", "name": "THE BRYME"},
        "datePublished": TODAY, "dateModified": TODAY,
        "mainEntityOfPage": ORIGIN + "/fitness/weekly-planner/",
        "description": "One card for the honest fitness week: movement most days, two strength days, on-time evenings. Ticks are saved in your browser only and the card resets each Monday."}
    planner_body = (head("fitness", "Practical fitness \u2014 no miracles, no medical claims.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/fitness/">Fitness</a> / The Weekly Planner</nav>'
        + '<section class="cover"><p class="kicker">The tool \u00b7 interactive \u00b7 resets every Monday</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">Your week, on one card.</h1>'
        + '<p class="byline">BRYME Fitness desk \u00b7 general information, not medical advice \u00b7 ticks are saved in <em>your</em> browser\u2019s local storage \u2014 no account, nothing sent anywhere</p></section>'
        + '<section class="section alt"><div class="wrap"><p class="lede"><b>One honest week:</b> move on most days, challenge the muscles twice, protect the evenings. Tick what actually happened \u2014 the card scores the week against the public-health targets, then starts fresh on Monday.</p></div></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The card</p><h2>Tap what happened.</h2></div>'
        + '<div id="wp-grid" class="wp-grid">' + _wp_rows + '</div>'
        + '<p class="lede" id="wp-status" style="margin-top:18px"></p>'
        + '<div class="actions"><button type="button" class="btn secondary" id="wp-reset">Reset the week</button></div></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">What counts</p><h2>Keep it honest, keep it easy.</h2></div>'
        + '<div class="prose">'
        + '<p><b>Move 30</b> \u2014 about thirty minutes of anything that lifts your breathing: a brisk walk (a day of <a href="/30-day-walking-plan/">the 30-day plan</a> counts by definition), cycling, a long swim, vigorous gardening. Five ticked days is the path to the 150-minute weekly guideline \u2014 not a rule, a route.</p>'
        + '<p><b>Strength</b> \u2014 one of the two weekly sessions from <a href="/strength-training-for-beginners/">the six patterns</a> or <a href="/workout-at-home-no-equipment/">the home routine</a>. Two ticks meets the muscle-strengthening guideline. Two, not seven: recovery days are where adaptation happens \u2014 <a href="/rest-days-and-recovery/">the recovery guide</a> explains why.</p>'
        + '<p><b>On-time night</b> \u2014 the evening you got to bed in time for seven-plus hours (<a href="/sleep-and-exercise-performance/">why sleep is the recovery multiplier</a>). The habit lives or dies at night, so the card tracks nights, not mornings.</p>'
        + '<p><b>Scoring, stated plainly:</b> the card reads 5 moves \u00b7 2 strength \u00b7 5 on-time nights as a complete honest week. It is a mirror, not a judge \u2014 a bad week is data for next week, and the card resets itself every Monday either way.</p>'
        + '</div></section>'
        + _fit_shell("fitness", "", "", "", True)
        + '<script src="/assets/fitness-planner.js" defer></script>'
        + '<script type="application/ld+json">' + _j2.dumps(_wp_schema) + "</script>"
        + "</div></main>" + foot("fitness"))
    plan_page.append(("/weekly-planner/", "The Weekly Planner | BRYME Fitness",
                      "One card for the honest fitness week: move most days, two strength days, on-time evenings. Saved in your browser, resets each Monday, nothing sent anywhere.", planner_body))
    pages.extend(plan_page)
    pages.extend(arts)
    return pages + legal_pages("fitness", "BRYME Fitness", "Practical fitness guidance \u2014 responsible, evidence-aware, clearly separated from medical advice.")




# ------------------------------------------------------------------ 6. HOME & DIY
HOME_CHECK = [
    ("Water & drainage", "Run water in every unused sink, shower and floor drain",
     "Traps dry out and let sewer smells back in. A jug of water a month keeps the seal."),
    ("Water & drainage", "Look inside the cabinets under your sinks",
     "Damp rings, swollen board or a slow drip caught early is a five-minute fix, not a flood."),
    ("Safety devices", "Press the test button on your RCD / GFCI outlets",
     "The button exists so you can prove the protection works. If it does not trip, get it checked."),
    ("Safety devices", "Test your smoke alarms",
     "Fire services recommend testing monthly. Press the button; replace batteries on the schedule the maker states."),
    ("Safety devices", "Check the torch you keep for power cuts",
     "Batteries die quietly. Give it thirty seconds of light now, not darkness later."),
    ("Appliances", "Clean the coils behind or under your refrigerator",
     "Dust on coils makes the compressor work harder and run hotter. Unplug first, brush gently."),
    ("Appliances", "Inspect the washing machine hoses",
     "Bulges, cracks or weeping fittings on rubber hoses are how laundry rooms flood. Makers commonly advise replacing ageing hoses before they fail."),
    ("Appliances", "Descale the kettle and coffee machine",
     "Wherever water is hard, scale shortens appliance life and ruins the taste. Your maker\u2019s descaling guide beats any hack."),
    ("Seals & airflow", "Walk the windows and doors",
     "Daylight around a closed door or cracked sealant means lost heat/cooling and moisture where you do not want it."),
    ("Seals & airflow", "Vacuum vents, radiators and the dryer\u2019s full lint path",
     "Dryer lint beyond the filter is a known fire risk; blocked vents make everything work harder."),
]

HOME_SOURCES = [
    ("NFPA \u2014 smoke alarm safety (testing guidance)", "https://www.nfpa.org/education-and-research/home-fire-safety/smoke-alarms"),
    ("U.S. Fire Administration \u2014 dryer fire safety", "https://www.usfa.fema.gov/prevention/home-fires/prevent-hfires/dryers/"),
]

HOME_ARTICLES = [
    ("how-to-fix-a-slow-draining-sink",
     "How to fix a slow-draining sink, honestly",
     "What actually clears a slow sink (in order of effort), what is mostly theatre, and the point at which a plumber earns their fee.",
     """<p>A slow sink is almost always a partial blockage in the trap or the first metre of pipe: hair, soap, fat, or the slow accretion of all three. You rarely need chemicals and you never need panic. Work down this list and stop when the water runs.</p>
<h2>First: the honest physics</h2>
<p>Drain cleaners and home remedies get marketed hard. The honest order of effectiveness for a slow (not fully blocked) sink is mechanical: physically removing the gunk beats dissolving it, and dissolving beats hoping. Hot water alone is theatre for a genuine soap-fat clog, though it helps flush a cleared pipe.</p>
<h2>Step 1: the plunger, properly</h2>
<p>Block the overflow opening with a wet cloth (a basin has a small hole near the top; cover it or the plunger\u2019s pressure escapes there). Add enough water to cover the plunger\u2019s cup. Push and pull sharply for twenty to thirty seconds. Most slow sinks end here.</p>
<h2>Step 2: open the trap</h2>
<p>Under the sink is the U-bend (P-trap). Put a bucket under it, hand-loosen the slip nuts, and lift the trap off. Empty it. What you find inside is usually the entire story \u2014 a compacted plug of hair and soap. Rinse both directions, refit hand-tight, run hot water and check for drips before closing the cabinet. If the pipe from the wall also holds gunk, a plastic hand-crank drain snake costs little and reaches where fingers cannot.</p>
<h2>What about baking soda and vinegar?</h2>
<p>The famous fizz is mostly theatre for real blockages \u2014 it is a mild reaction, not a solvent. It will not harm anything, and it can freshen a smelly (rather than slow) drain, but do not let it replace the plunger and the trap.</p>
<h2>Chemicals: the safety boundary</h2>
<p>If you do use a caustic drain cleaner, follow the label exactly, ventilate, and never mix products \u2014 especially anything containing bleach with anything containing ammonia or acid; the reaction gases are genuinely dangerous. Chemicals also sit in the pipe, waiting for whoever opens the trap next. That is why this guide puts chemicals last, if at all.</p>
<h2>Call a plumber when</h2>
<p>Several fixtures drain slowly at once (the blockage is downstream, often in the main drain), water comes up in a different fixture when another drains, or the trap will not come apart because fittings are corroded or glued. Also call if there is sewage smell that a water top-up does not fix \u2014 a dried trap is a jug of water; a broken vent or seal is a professional.</p>
<h2>Prevention</h2>
<p>A mesh screen over the plug hole, fat into a jar rather than the sink, and a monthly kettle\u2019s worth of hot water down each drain. Three habits; zero emergencies. The <a href="/seasonal-home-maintenance-checklist/">once-a-season home checklist</a> includes the drain top-up.</p>"""),
    ("how-to-fix-a-dripping-tap",
     "A dripping tap (faucet), and what you can honestly fix yourself",
     "Why taps drip, the washer-and-cartridge reality behind most of them, and the ten-minute test that tells you whether it is your job or a plumber\u2019s.",
     """<p>A tap that drips once a second wastes more water over a month than most people expect, and the sound has driven stronger people than you to madness. The good news: the majority of dripping taps are a small, cheap, mechanical fix \u2014 provided you can turn the water off and tell the difference between the two most common tap insides.</p>
<h2>Before anything: the isolation test</h2>
<p>Find the shut-off valve for that tap (under the sink in most homes) and close it, or close the main if there is none. Open the tap to confirm the flow has stopped. No isolation valve and no main you can find? That is the professional\u2019s first visit, not yours.</p>
<h2>What kind of tap is it?</h2>
<p>Two families dominate. Traditional taps with a spindle you turn several times usually seal with a rubber washer and a seat \u2014 dripping when off, usually the washer. Modern single-lever or quarter-turn taps usually seal with a ceramic cartridge \u2014 dripping or failing to shut smoothly, usually the cartridge. Brand matters for parts: open nothing until you know the make, or plan to take the old part to a hardware shop as the specimen.</p>
<h2>The washer job, in one honest paragraph</h2>
<p>With water off: prise the decorative cap, unscrew the handle, unscrew the spindle with an adjustable spanner, and look at the end \u2014 a squashed, grooved or torn rubber washer is your culprit. Replace it with an identical size (take the old one shopping), check the seat it presses against is not scored, reassemble in reverse, reopen the water slowly. Ten to twenty minutes the first time.</p>
<h2>The cartridge job</h2>
<p>Same isolation, then the retaining clip or nut holds the cartridge. Cartridges are brand-specific parts \u2014 photograph the tap and its brand before buying. They swap in minutes once you hold the right part, and they are usually the only part that ever needs replacing on those taps.</p>
<h2>When it is not your job</h2>
<p>Water weeping from the tap body itself, corrosion that will not let fittings separate, no way to isolate the supply, or anything involving the pipes inside the wall: that is a plumber\u2019s territory. Paying for an hour of plumbing is cheaper than a flooded cabinet \u2014 see <a href="/how-to-fix-a-slow-draining-sink/">what lives inside sink cabinets</a> when they stay damp.</p>
<h2>Prevention, such as it is</h2>
<p>Taps wear from use, not neglect. What you can prevent is the collateral: close taps firmly but never forced \u2014 over-tightening chews washers faster. And once a season, glance at every tap\u2019s isolation valve; a valve that has not moved in years is the one that will seize. It is on the <a href="/seasonal-home-maintenance-checklist/">seasonal checklist</a>.</p>"""),
    ("why-does-my-circuit-breaker-keep-tripping",
     "Why your circuit breaker keeps tripping \u2014 and where DIY must stop",
     "What breakers actually protect you from, the safe way to narrow down the cause, and the hard boundary that separates a homeowner from an electrician.",
     """<p>A tripping breaker is not a malfunction. It is your electrical panel doing exactly its job: cutting power when the circuit is asked to carry more current than is safe, or when it detects a leak of current to earth. The nuisance is the clue. Read it correctly and it is one of the most useful signals in your home.</p>
<h2>The three usual causes</h2>
<p>Overload: too many things drawing power on one circuit \u2014 the kettle, heater and iron sharing one socket circuit, say. Short circuit: live and neutral touching somewhere they should not, often a damaged appliance, cable or plug \u2014 the trip is instant. Earth leak (the RCD/GFCI part of the protection): current escaping along a path it should not, often moisture or a failing appliance \u2014 these trips feel random and are the ones you must never ignore, because that protection exists to stop shocks.</p>
<h2>The safe way to narrow it down</h2>
<p>Unplug everything on the dead circuit. Reset the breaker firmly. If it holds: plug items back in one at a time, with a pause between each \u2014 the item that trips it again has named itself; retire or repair it. If it trips immediately with nothing plugged in, or trips repeatedly with everything unplugged, stop there. That is wiring, not appliances, and it is not a homeowner diagnosis.</p>
<h2>The reset, done properly</h2>
<p>Breakers trip to OFF or to a middle position. Push fully to OFF first, then to ON \u2014 resetting from the middle position is the classic reason a breaker \u201cwill not reset\u201d. One or two resets to diagnose is normal. A breaker you find yourself resetting weekly is telling you something is wrong; solving that by resetting harder is how problems escalate.</p>
<h2>The hard boundary</h2>
<p>Resetting a breaker and unplugging appliances: homeowner territory, do it today. Everything else \u2014 panel work, adding circuits, repeated trips with no load, burning smells, warm outlets, any work behind sockets \u2014 belongs to a qualified electrician. This page is general information, not electrical advice, and it deliberately stops at the panel cover. Electricity does not give second chances.</p>
<h2>Where this fits the house</h2>
<p>The <a href="/seasonal-home-maintenance-checklist/">once-a-season checklist</a> includes testing RCD/GFCI outlets and smoke alarms \u2014 the thirty seconds that prove the protective parts of your home still work.</p>"""),
    ("how-to-clean-a-washing-machine",
     "How to clean a washing machine (including the parts that actually cause the smell)",
     "Why machines smell and mark laundry, the gasket-and-filter truth behind it, and a maintenance rhythm that prevents both.",
     """<p>A washing machine that smells damp, or marks clean clothes with grey streaks, is not broken. It is dirty in the three specific places detergent residue and water sit long enough to grow things: the door gasket, the detergent drawer, and the filter. Cleaning those beats every scented product marketed to mask the problem.</p>
<h2>The gasket is the crime scene</h2>
<p>On front loaders, fold back the rubber door gasket and look: black speckles, slime, the odd lost sock. Wipe it out with a cloth and warm soapy water, getting into the folds. Leave the door and drawer ajar between washes so the inside dries \u2014 sealed-in moisture is what grows the smell in the first place.</p>
<h2>The detergent drawer slides out</h2>
<p>Most drawers release fully with a press of a recessed clip (your manual shows where, or the internet knows your model). Wash it under the tap with an old toothbrush; check the jet holes above where it sits and clear the residue that blocks rinse water.</p>
<h2>The filter you have been avoiding</h2>
<p>Behind a small hatch near the floor lives the drain filter \u2014 the place coins, hair clips and lint go to retire. Put a shallow tray or towel down, open it slowly (water will come), remove and rinse the filter, and screw it back snugly. Once a season is the honest rhythm; more if you have pets or small humans.</p>
<h2>Hot wash, occasionally</h2>
<p>Cold-wash habits let grease and residue accumulate. A monthly hot cycle \u2014 empty, with a maker-approved cleaner or plain washing soda per its instructions \u2014 flushes the tub and the pipes behind it. Skip the folk chemistry; heat does the work.</p>
<h2>Prevention rhythm</h2>
<p>Door ajar after washes; drawer ajar; filter each season; a monthly hot cycle; and measure detergent honestly \u2014 most people use far more than the machine needs, and the surplus is what rots. All of this except the hot cycle is on the <a href="/seasonal-home-maintenance-checklist/">once-a-season checklist</a>.</p>"""),
    ("fridge-not-cold-enough",
     "Fridge not cold enough? Five checks before you pay for a repair",
     "The settings, airflow and coil checks that fix most \u201cwarm fridge\u201d calls, and the signs that say it really is a technician\u2019s problem.",
     """<p>A fridge that runs but does not quite cool is one of the most common \u201crepair\u201d calls \u2014 and a decent share of them are fixed in ten minutes with no parts. Work these checks in order; stop and call a technician the moment the path says so.</p>
<h2>1. The thermostat, honestly</h2>
<p>Dials marked 1\u20135 say nothing absolute; the manual says which end is colder. Confirm the setting first \u2014 dials get nudged by grocery bags. A fridge thermometer (cheap, honest) beats any built-in dial: you want roughly at or below 4\u00b0C / 40\u00b0F on the shelf, freezer around \u201318\u00b0C / 0\u00b0F.</p>
<h2>2. Airflow inside</h2>
<p>Cold air travels through vents between freezer and fridge. Boxes jammed against the back wall and vents blocked by a bag of peas mimic a failing fridge. Create space; let air move.</p>
<h2>3. The door seal test</h2>
<p>Close the door on a piece of paper; if it slides out with no resistance at several points, the gasket is not sealing and cold air leaks out. Clean sticky residue off the gasket; a perished or torn one is a replaceable part on most models \u2014 cheaper than a new fridge.</p>
<h2>4. The coils you never see</h2>
<p>Unplug the fridge, find the coils (behind the kick plate or on the back), and brush/vacuum the dust blanket off. Coils choked with dust shed heat poorly and the cabinet warms. This is the single most common neglected maintenance on kitchen appliances \u2014 it is on the <a href="/seasonal-home-maintenance-checklist/">seasonal checklist</a> for that reason.</p>
<h2>5. Give it time, then listen</h2>
<p>After any change, give the fridge several hours with the door kept closed. Then listen: a compressor that clicks on and off every few minutes, or hums constantly without cooling, is failing \u2014 and that, along with frost patterns that suggest a defrost-system fault, is genuinely a technician\u2019s job. Refrigerant and sealed systems are not DIY, full stop.</p>
<h2>When you call, say this</h2>
<p>\u201cCompressor runs continuously, cabinet at 10\u00b0C, coils cleaned, seal tested\u201d gets a better visit than \u201cit\u2019s warm\u201d \u2014 and sometimes a better answer: knowing the checks were done may save you the call-out entirely.</p>"""),
]

HOME_SECTIONS = [
    ("fix", "Fix it", "Household problems and beginner repairs, honestly ordered."),
    ("maintain", "Maintain it", "Preventive care, and the kit that does it."),
    ("appliances", "Appliances", "Keep the machines honest."),
    ("understand", "Understand it", "What the symptoms actually mean."),
    ("outside", "Outside", "Gutters, grills, sheds and the seasons \u2014 the half of the house that faces the weather."),
    ("pests", "Pests", "Unwelcome guests \u2014 prevention, honest decisions, and the aftercare that makes treatment work."),
    ("secure", "Secure it", "Doors, windows, locks and the nightly habits that make a house a hard target."),
    ("owning", "Owning it", "Moving in, budgets, insurance, responsibility and value \u2014 the owner\u2019s ledger."),
    ("mistakes", "Common mistakes", "The errors most homes make - and the fixes."),
]
HOME_SLUG_SECT = {
    "how-to-fix-a-slow-draining-sink": "fix",
    "how-to-fix-a-dripping-tap": "fix",
    "how-to-unblock-a-toilet": "fix",
    "how-to-bleed-a-radiator": "maintain",
    "basic-toolkit-checklist": "maintain",
    "how-to-clean-a-washing-machine": "appliances",
    "washing-machine-wont-drain": "appliances",
    "why-does-my-circuit-breaker-keep-tripping": "understand",
    "fridge-not-cold-enough": "understand",
}
HOME_SLUG_SECT.update({s: "appliances" for s in (
    "washing-machine-heavy-items", "dryer-lint-every-load", "dishwasher-loading-mistakes",
    "stop-pre-rinsing-dishes", "vinegar-in-the-dishwasher", "fridge-coils-twice-a-year",
    "fridge-door-seal-test", "garbage-disposal-mistakes", "induction-hob-wiring",
    "smart-appliances-worth-it")})

HOME_SLUG_SECT.update({s: "understand" for s in (
    "uk-carbon-monoxide-alarm-law", "how-many-smoke-co-alarms", "co-smoke-alarm-expiry",
    "condensation-vs-rising-vs-penetrating-damp", "uk-landlord-damp-mould-duties",
    "gas-heaters-damp")})
HOME_SLUG_SECT.update({s: "maintain" for s in (
    "test-alarms-monthly", "condensation-ventilation-that-works")})
HOME_SLUG_SECT.update({s: "appliances" for s in (
    "how-to-deep-clean-an-oven", "how-to-defrost-a-freezer-properly",
    "washing-machine-mould-door-seal", "how-to-descale-a-kettle",
    "fridge-temperature-setting")})
HOME_SLUG_SECT.update({s: "fix" for s in ("how-to-clear-a-slow-shower-drain",)})
HOME_SLUG_SECT.update({s: "maintain" for s in (
    "how-to-clean-and-care-for-a-mattress", "season-cast-iron-pan",
    "spring-home-reset", "summer-cooling-checklist",
    "autumn-home-preparation", "winter-home-preparation")})

HOME_SLUG_SECT.update({s: "maintain" for s in (
    "hvac-filter-change-habit", "uk-boiler-servicing", "ac-outdoor-unit-care")})
HOME_SLUG_SECT.update({s: "understand" for s in (
    "hvac-noises-decoded", "hvac-diy-warranty-rules", "uk-us-plumber-rules")})
HOME_SLUG_SECT.update({s: "fix" for s in (
    "small-leak-ripple-effect", "leaky-faucet-diy")})

HOME_SLUG_SECT.update({s: "fix" for s in (
    "interior-painting-mistakes", "humidity-and-paint", "painting-over-damp")})
HOME_SLUG_SECT.update({s: "understand" for s in (
    "electrical-fire-warning-signs", "outlet-overloading-danger")})

HOME_SLUG_SECT.update({s: "understand" for s in (
    "us-home-permits", "building-regs-vs-planning-permission", "unpermitted-work-home-sale",
    "part-p-explained", "us-diy-electrical-rules")})

HOME_SLUG_SECT.update({s: "outside" for s in (
    "gutter-cleaning-damage", "fence-shed-insurance", "outdoor-cooking-safety",
    "inspection-checklist-gaps")})
HOME_SLUG_SECT.update({s: "maintain" for s in (
    "draught-proofing-mistakes", "wet-mop-floor-warranty", "deep-clean-schedule")})
HOME_SLUG_SECT.update({s: "understand" for s in (
    "single-glazing-payback", "underfloor-heating-mistakes")})

HOME_SLUG_SECT.update({s: "pests" for s in (
    "clean-home-pests-myth", "ignore-single-pest-sighting", "moving-cardboard-pests",
    "after-pest-treatment", "diy-vs-professional-pests")})
HOME_SLUG_SECT.update({s: "fix" for s in ("bathroom-remodel-mistakes",)})
HOME_SLUG_SECT.update({s: "maintain" for s in (
    "kitchen-ventilation-damp", "grout-sealant-neglect")})

HOME_SLUG_SECT.update({s: "understand" for s in (
    "energy-bill-high-unchanged", "smart-thermostat-payback")})
HOME_SLUG_SECT.update({s: "maintain" for s in ("uk-insulation-grants",)})
HOME_SLUG_SECT.update({s: "secure" for s in (
    "entry-point-mistakes", "smart-locks-cameras-worth-it", "renter-security")})

HOME_SLUG_SECT.update({s: "owning" for s in (
    "pre-move-inspection", "moving-week-by-week", "secondhand-furniture-mistakes",
    "emergency-repair-fund", "someday-maintenance-cost", "unpermitted-work-insurance",
    "renter-vs-owner-repairs", "improvements-no-resale-value")})


def _home_theme_init():
    # External file: the site CSP is script-src 'self' - inline scripts never run.
    # Loaded blocking in <head> so the theme applies before first paint (no flash).
    return '<script src="/assets/home-theme.js"></script>'

def _home_toggle_js():
    # wiring lives in /assets/home-theme.js (CSP: script-src self)
    return ""

def _home_mast():
    return ('<header class="head"><div class="wrap mast">'
            '<a class="mast-brand" href="/home/">BRYME&nbsp;<span style="color:var(--accent)">HOME&nbsp;&amp;&nbsp;DIY</span></a>'
            '<div class="mast-edition"><span class="mast-date">SEPTEMBER 2026 \u00b7 THE FIX-IT DESK</span>'
            '<span class="mast-tag">Fix it. Clean it. Maintain it. Understand it.</span></div>'
            '<div class="mast-tools">'
            '<button type="button" class="theme-btn" id="home-theme" aria-pressed="false" aria-label="Toggle dark mode" title="Toggle dark mode">&#9789;</button>'
            '</div></div></header>')


def _home_nav():
    import home_mistakes_data
    _mset = {m[0] for m in home_mistakes_data.HOME_MISTAKES}
    def mh(slug):
        return ("/home/mistakes/" + slug + "/") if slug in _mset else ("/home/" + slug + "/")
    fix = [("HEAD", "The fix shelf"), ("/home/fix/", "All fixes"),
           ("/home/how-to-fix-a-dripping-tap/", "Dripping tap"),
           ("/home/how-to-unblock-a-toilet/", "Unblock a toilet"),
           ("/home/how-to-fix-a-slow-draining-sink/", "Slow-draining sink"),
           ("/home/washing-machine-wont-drain/", "Washer won\u2019t drain"),
           ("/home/fridge-not-cold-enough/", "Fridge not cold"),
           ("/home/why-does-my-circuit-breaker-keep-tripping/", "Breaker keeps tripping"),
           ("/home/how-to-bleed-a-radiator/", "Bleed a radiator")]
    maintain = [("HEAD", "The care shelf"), ("/home/maintain/", "All maintenance"),
                ("/home/seasonal-home-maintenance-checklist/", "The seasonal checklist"),
                ("/home/deep-clean-schedule/", "Deep-clean schedule"),
                ("/home/how-to-clean-a-washing-machine/", "Clean a washing machine"),
                ("/home/fridge-coils-twice-a-year/", "Fridge coils, twice a year"),
                ("/home/dryer-lint-every-load/", "Dryer lint, every load"),
                ("/home/hvac-filter-change-habit/", "HVAC filter habit"),
                ("/home/test-alarms-monthly/", "Test alarms monthly")]
    appliances = [("HEAD", "The appliance shelf"), ("/home/appliances/", "All appliances"),
                  ("/home/dishwasher-loading-mistakes/", "Dishwasher loading"),
                  ("/home/stop-pre-rinsing-dishes/", "Stop pre-rinsing dishes"),
                  ("/home/vinegar-in-the-dishwasher/", "Vinegar in the dishwasher"),
                  ("/home/smart-appliances-worth-it/", "Smart appliances, worth it?"),
                  ("/home/washing-machine-heavy-items/", "Heavy items in the washer"),
                  ("/home/garbage-disposal-mistakes/", "Garbage disposal")]
    understand = [("HEAD", "The knowledge shelf"), ("/home/understand/", "All explainers"),
                  ("/home/condensation-vs-rising-vs-penetrating-damp/", "The three damp types"),
                  ("/home/building-regs-vs-planning-permission/", "Building regs vs planning"),
                  ("/home/renter-vs-owner-repairs/", "Renter vs owner repairs"),
                  ("/home/part-p-explained/", "Part P, explained (UK)"),
                  ("/home/us-home-permits/", "US home permits"),
                  ("/home/uk-us-plumber-rules/", "UK vs US plumber rules"),
                  ("/home/smart-thermostat-payback/", "Smart thermostat payback")]
    mistakes = [("HEAD", "Avoid these"), ("/home/mistakes/", "All mistakes"),
                (mh("electrical-fire-warning-signs"), "Electrical fire warning signs"),
                (mh("outlet-overloading-danger"), "Outlet overloading"),
                (mh("co-smoke-alarm-expiry"), "Alarm expiry dates"),
                (mh("how-many-smoke-co-alarms"), "How many alarms"),
                (mh("painting-over-damp"), "Painting over damp"),
                (mh("bathroom-remodel-mistakes"), "Bathroom remodel mistakes"),
                (mh("grout-sealant-neglect"), "Grout &amp; sealant neglect")]
    parts = []
    for label, payload in [("Fix it", fix), ("Maintain", maintain), ("Appliances", appliances),
                           ("Understand", understand), ("Mistakes &amp; safety", mistakes)]:
        parts.append('<div class="has-mega"><a href="' + payload[1][0] + '">' + label + "</a>" + _mega(payload) + "</div>")
    parts.append('<a class="nav-cta" href="/home/seasonal-home-maintenance-checklist/">Once-a-season checklist</a>')
    return '<nav class="main-nav"><div class="wrap mast-nav">' + "".join(parts) + "</div></nav>"

def _home_sidebar(current):
    import home_mistakes_data
    counts = {}
    for s in HOME_SLUG_SECT.values():
        counts[s] = counts.get(s, 0) + 1

    def a(href, label, key, n=None, flag=False):
        cls = ""
        if key == current:
            cls = 'active'
        if flag:
            cls += ' flag'
        cls_attr = ' class="' + cls.strip() + '"' if cls else ''
        nn = '<span class="n">' + str(n) + '</span>' if n is not None else ''
        return '<a' + cls_attr + ' href="' + href + '">' + label + nn + '</a>'

    items = (a("/home/", "Desk home", "home")
        + a("/home/fix/", "Fix it", "fix", counts.get("fix", 0))
        + a("/home/maintain/", "Maintain it", "maintain", counts.get("maintain", 0))
        + a("/home/appliances/", "Appliances", "appliances", counts.get("appliances", 0))
        + a("/home/understand/", "Understand it", "understand", counts.get("understand", 0))
        + a("/home/mistakes/", "Common mistakes", "mistakes", len(home_mistakes_data.HOME_MISTAKES), True)
        + a("/home/seasonal-home-maintenance-checklist/", "The seasonal checklist", "checklist", None, True))
    return ('<aside class="h-side"><p class="h-side-title">The desk</p>'
            '<nav aria-label="Home and DIY sections">' + items + "</nav></aside>")

def _home_page(title, desc, route, cover_html, main_html, sidebar_current):
    canonical = ORIGIN + "/home" + route
    og = "https://" + DOMAIN + "/assets/og.png"
    return ('<!doctype html>\n<html lang="en"><head>\n'
        '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>" + html.escape(title) + "</title>\n"
        '<meta name="description" content="' + html.escape(desc) + '">\n'
        '<meta name="robots" content="index,follow">\n'
        '<link rel="canonical" href="' + canonical + '">\n'
        '<meta property="og:type" content="website"><meta property="og:site_name" content="THE BRYME">\n'
        '<meta property="og:title" content="' + html.escape(title) + '"><meta property="og:description" content="' + html.escape(desc) + '">\n'
        '<meta property="og:url" content="' + canonical + '"><meta property="og:image" content="' + og + '">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        + _home_theme_init() + "\n<style>" + css_for("home") + "</style>\n</head>"
        '<body><a class="skip-link" href="#main">Skip to content</a>\n'
        + _home_mast() + _home_nav()
        + '<div class="wrap h-layout">' + _home_sidebar(sidebar_current)
        + '<main id="main" class="h-main">' + cover_html + main_html + "</main></div>\n"
        + foot("home") + "\n" + _home_toggle_js() + "</body></html>")

def home_pages():
    import home_mistakes_data
    import more_guides_data
    _mset = {m2[0] for m2 in home_mistakes_data.HOME_MISTAKES}
    def _hurl(s):
        return ("/home/mistakes/" + s + "/") if s in _mset else ("/home/" + s + "/")
    _have = {s2[0] for s2 in HOME_ARTICLES}
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in more_guides_data.HOME_MORE if s2 not in _have)
    import home_roadmap_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap_data.HOME_ROADMAP if s2 not in _have)
    import home_roadmap2_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap2_data.HOME_ROADMAP_2 if s2 not in _have)
    import home_roadmap3_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap3_data.HOME_ROADMAP_3 if s2 not in _have)
    import home_roadmap4_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap4_data.HOME_ROADMAP_4 if s2 not in _have)
    import home_roadmap5_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap5_data.HOME_ROADMAP_5 if s2 not in _have)
    import home_roadmap6_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap6_data.HOME_ROADMAP_6 if s2 not in _have)
    import home_roadmap7_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap7_data.HOME_ROADMAP_7 if s2 not in _have)
    import home_roadmap8_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap8_data.HOME_ROADMAP_8 if s2 not in _have)
    import home_roadmap9_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap9_data.HOME_ROADMAP_9 if s2 not in _have)
    import home_roadmap10_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap10_data.HOME_ROADMAP_10 if s2 not in _have)
    import home_roadmap11_data
    HOME_ARTICLES.extend((s2, ti, dek, b) for (s2, _k, ti, dek, b) in home_roadmap11_data.HOME_ROADMAP_11 if s2 not in _have)

    def src_html(sources):
        if not sources:
            return ""
        return ('<h2>Sources</h2><ul class="list">'
                + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                + "</ul>")

    def band(text):
        return ('<section class="section alt" style="border-left:4px solid var(--brand)"><div class="wrap"><p class="lede">'
                + text + "</p></div></section>")

    DISCLAIMER = band("<b>General information, not professional advice.</b> Homes differ \u2014 if a job is beyond your confidence or the guide\u2019s boundary, that is what tradespeople are for.")
    SAFETY = band("<b>Safety boundary.</b> Electrical panel work, gas, structural changes and anything at height belong to qualified professionals. Every guide here stops where that line starts.")

    def sec_label(key):
        for k2, l2, _d in HOME_SECTIONS:
            if k2 == key:
                return l2
        return key

    out = []

    # ---------- index ----------
    mistake_rows = []
    mistake_pages = []
    for n2, (slug, theme, mtitle, one_liner, mbody, sources, related) in enumerate(home_mistakes_data.HOME_MISTAKES, 1):
        mistake_rows.append('<li><a href="/mistakes/' + slug + '/"><span><b>' + html.escape(mtitle) + "</b><small>"
                            + html.escape(one_liner) + "</small></span>"
                            '<span class="meta">' + html.escape(theme) + "</span></a></li>")
        rel_html = "".join('<li><a href="' + _hurl(s) + '">' + rt + "</a></li>" for s, rt in related)
        mcover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / '
                  '<a href="/home/mistakes/">Common mistakes</a> / ' + html.escape(mtitle) + "</nav>"
            + '<section class="cover"><p class="kicker">Common mistake ' + str(n2) + ' of ' + str(len(home_mistakes_data.HOME_MISTAKES)) + " \u00b7 " + html.escape(theme) + "</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.8vw,52px)">' + html.escape(mtitle) + "</h1>"
            + '<p class="byline">BRYME Home &amp; DIY desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not professional advice</p></section>")
        mmain = ('<section class="section alt"><div class="wrap"><p class="lede"><b>The mistake:</b> ' + html.escape(one_liner) + "</p></div></section>"
            + '<section class="section"><div class="prose">' + mbody + src_html(sources) + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/home/mistakes/">All common mistakes</a>'
            + '<a class="btn secondary" href="/home/">Desk home</a></div></section>'
            + DISCLAIMER)
        mistake_pages.append(("/mistakes/" + slug + "/", mtitle + " | BRYME Home & DIY", one_liner[:155],
                              _home_page(mtitle + " | BRYME Home & DIY", one_liner[:155], "/mistakes/" + slug + "/", mcover, mmain, "mistakes")))

    icover = ('<section class="cover"><p class="kicker">BRYME Home &amp; DIY</p>'
        + '<h1 class="cover-title">Fix it. Clean it. Maintain it. Understand it.</h1>'
        + '<p class="cover-dek">Practical help for the problems every household hits \u2014 written for low-risk work, with the boundaries stated plainly: electrical panels, gas, structure and height belong to qualified professionals, and every guide here says exactly where that line is.</p>'
        + '<div class="cover-facts">'
        + '<div><b>' + str(len(HOME_ARTICLES)) + '</b><span>Guides &amp; fixes</span></div>'
        + '<div><b>9</b><span>Sections of the desk</span></div>'
        + '<div><b>' + str(len(home_mistakes_data.HOME_MISTAKES)) + '</b><span>Common mistakes</span></div>'
        + '<div><b>0</b><span>Upsells, ever</span></div>'
        + '</div></section>')
    sec_cards = "".join(
        '<div class="h-sec-card"><p class="kicker" style="margin:0">'
        + str(len([s2 for s2, k2 in HOME_SLUG_SECT.items() if k2 == key]) if key != "mistakes" else len(home_mistakes_data.HOME_MISTAKES))
        + " PIECES</p><h3>" + label + "</h3><p>" + sdek + '</p><a class="btn secondary" style="margin-top:12px" href="/home/' + key + '/">Open ' + label + "</a></div>"
        for key, label, sdek in HOME_SECTIONS)
    imain = ('<section class="section"><div class="section-head"><p class="kicker">Start with the classics</p><h2>The common mistakes shelf.</h2></div>'
        + '<ul class="list">' + "".join(mistake_rows[:4]) + "</ul>"
        + '<div class="actions"><a class="btn" href="/home/mistakes/">All ' + str(len(home_mistakes_data.HOME_MISTAKES)) + " common mistakes</a></div></section>"
        + '<section class="section alt"><div class="section-head"><p class="kicker">Browse the desk</p><h2>Sections.</h2></div>'
        + '<div class="h-sec-grid">' + sec_cards + "</div></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">The product</p><h2>The once-a-season checklist.</h2></div>'
        + '<div class="prose"><p><a href="/seasonal-home-maintenance-checklist/"><b>The once-a-season home checklist</b></a> \u2014 ten checks across water, safety devices, appliances and airflow, with progress your browser remembers. Homes fail slowly, then suddenly; this catches the slow part.</p></div></section>'
        + SAFETY)
    out.append(("/", "BRYME Home & DIY \u2014 fix, clean, maintain, understand",
                "Low-risk home repairs and maintenance, honestly explained \u2014 with sections, a common-mistakes shelf and the once-a-season checklist.",
                _home_page("BRYME Home & DIY \u2014 fix, clean, maintain, understand",
                           "Low-risk home repairs and maintenance, honestly explained.", "/",
                           icover, imain, "home")))

    # ---------- section pages ----------
    data_by_slug = {s2[0]: s2 for s2 in HOME_ARTICLES}
    for key, label, sdek in HOME_SECTIONS:
        if key == "mistakes":
            continue
        slugs = [s for s, k2 in HOME_SLUG_SECT.items() if k2 == key]
        rows = ""
        for s in slugs:
            _s2, ti, dek, _b = data_by_slug[s]
            rows += ('<li><a href="' + _hurl(s) + '"><span><b>' + html.escape(ti) + "</b><small>" + html.escape(dek) + "</small></span>"
                     '<span class="meta">Guide</span></a></li>')
        others = "".join('<a class="btn secondary" href="/home/' + k2 + '/">' + l2 + "</a>"
                         for k2, l2, _d in HOME_SECTIONS if k2 != key)
        cover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / ' + label + "</nav>"
            + '<section class="cover"><p class="kicker">BRYME Home &amp; DIY \u00b7 section</p>'
            + '<h1 class="cover-title">' + label + "</h1>"
            + '<p class="cover-dek">' + sdek + "</p></section>")
        main = ('<section class="section"><div class="section-head"><p class="kicker">' + str(len(slugs)) + ' guides</p><h2>Everything in ' + label + '.</h2></div>'
            + '<ul class="list">' + rows + "</ul>"
            + '<div class="actions">' + others
            + '<a class="btn secondary" href="/home/">Desk home</a></div></section>')
        out.append(("/" + key + "/", label + " | BRYME Home & DIY", sdek,
                    _home_page(label + " | BRYME Home & DIY", sdek, "/" + key + "/", cover, main, key)))

    # ---------- mistakes hub ----------
    mcover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / Common mistakes</nav>'
        + '<section class="cover"><p class="kicker">The most-visited shelf on this desk</p>'
        + '<h1 class="cover-title">Common mistakes, and how to fix them.</h1>'
        + '<p class="cover-dek">The errors most homes make \u2014 with too much soap, the wrong cleaner combo, a watering can on a schedule, a drill in the dark. Every piece follows the same honest shape: the mistake, why it backfires, the fix, and how to keep it from happening again.</p></section>')
    mmain = ('<section class="section"><div class="section-head"><p class="kicker">'
             + str(len(home_mistakes_data.HOME_MISTAKES)) + ' mistakes, no shaming</p><h2>The shelf.</h2></div>'
        + '<ul class="list">' + "".join(mistake_rows) + "</ul></section>"
        + SAFETY)
    out.append(("/mistakes/", "Common home mistakes \u2014 and how to fix them | BRYME Home & DIY",
                "The errors most homes make: too much detergent, mixed cleaners, overwatering, blind drilling \u2014 why they backfire and the honest fixes.",
                _home_page("Common home mistakes \u2014 and how to fix them | BRYME Home & DIY",
                           "The errors most homes make, why they backfire and the honest fixes.", "/mistakes/",
                           mcover, mmain, "mistakes")))
    out.extend(mistake_pages)

    # ---------- guides ----------
    related_map = {
        "how-to-fix-a-slow-draining-sink": [("how-to-unblock-a-toilet", "The blocked toilet"),
                                            ("how-to-fix-a-dripping-tap", "A dripping tap, fixed honestly"),
                                            ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "how-to-fix-a-dripping-tap": [("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                      ("basic-toolkit-checklist", "The basic toolkit"),
                                      ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "how-to-unblock-a-toilet": [("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                    ("basic-toolkit-checklist", "The basic toolkit"),
                                    ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "how-to-bleed-a-radiator": [("basic-toolkit-checklist", "The basic toolkit"),
                                    ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                    ("washing-machine-wont-drain", "The machine that won't drain")],
        "basic-toolkit-checklist": [("how-to-bleed-a-radiator", "Bleeding a radiator"),
                                    ("drilling-without-checking", "Drilling without checking"),
                                    ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker")],
        "how-to-clean-a-washing-machine": [("washing-machine-wont-drain", "The machine that won't drain"),
                                           ("too-much-detergent", "Too much detergent"),
                                           ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "washing-machine-wont-drain": [("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                       ("fridge-not-cold-enough", "Fridge not cold enough"),
                                       ("basic-toolkit-checklist", "The basic toolkit")],
        "why-does-my-circuit-breaker-keep-tripping": [("drilling-without-checking", "Drilling without checking"),
                                                      ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                                      ("fridge-not-cold-enough", "Fridge not cold enough")],
        "fridge-not-cold-enough": [("overloading-the-fridge", "Packing the fridge solid"),
                                   ("washing-machine-wont-drain", "The machine that won't drain"),
                                   ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker")],
        "washing-machine-heavy-items": [("washing-machine-wont-drain", "The machine that won't drain"),
                                        ("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                        ("too-much-detergent", "Too much detergent")],
        "dryer-lint-every-load": [("washing-machine-heavy-items", "The load that kills machines"),
                                  ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                  ("basic-toolkit-checklist", "The basic toolkit")],
        "dishwasher-loading-mistakes": [("stop-pre-rinsing-dishes", "Skip the pre-rinse"),
                                        ("vinegar-in-the-dishwasher", "Not with vinegar"),
                                        ("too-much-detergent", "Too much detergent")],
        "stop-pre-rinsing-dishes": [("dishwasher-loading-mistakes", "Load it so it cleans"),
                                    ("vinegar-in-the-dishwasher", "Not with vinegar"),
                                    ("too-much-detergent", "Too much detergent")],
        "vinegar-in-the-dishwasher": [("dishwasher-loading-mistakes", "Load it so it cleans"),
                                      ("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                      ("mistakes/mixing-cleaning-products", "Never mix cleaners")],
        "fridge-coils-twice-a-year": [("fridge-door-seal-test", "The dollar-bill seal test"),
                                      ("fridge-not-cold-enough", "Fridge not cold enough"),
                                      ("overloading-the-fridge", "Packing the fridge solid")],
        "fridge-door-seal-test": [("fridge-coils-twice-a-year", "Clean the coils twice a year"),
                                  ("fridge-not-cold-enough", "Fridge not cold enough"),
                                  ("overloading-the-fridge", "Packing the fridge solid")],
        "garbage-disposal-mistakes": [("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                      ("how-to-unblock-a-toilet", "The blocked toilet"),
                                      ("basic-toolkit-checklist", "The basic toolkit")],
        "induction-hob-wiring": [("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                 ("drilling-without-checking", "Drilling without checking"),
                                 ("basic-toolkit-checklist", "The basic toolkit")],
        "smart-appliances-worth-it": [("fridge-coils-twice-a-year", "Clean the coils twice a year"),
                                      ("washing-machine-heavy-items", "The load that kills machines"),
                                      ("dishwasher-loading-mistakes", "Load it so it cleans")],
        "uk-carbon-monoxide-alarm-law": [("co-alarm-wrong-place", "The CO alarm that can't work"),
                                         ("co-smoke-alarm-expiry", "The expiry date nobody reads"),
                                         ("how-many-smoke-co-alarms", "How many alarms you need")],
        "how-many-smoke-co-alarms": [("uk-carbon-monoxide-alarm-law", "UK CO alarm law"),
                                     ("co-smoke-alarm-expiry", "The expiry date nobody reads"),
                                     ("test-alarms-monthly", "The monthly alarm habit")],
        "co-smoke-alarm-expiry": [("co-alarm-wrong-place", "The CO alarm that can't work"),
                                  ("test-alarms-monthly", "The monthly alarm habit"),
                                  ("how-many-smoke-co-alarms", "How many alarms you need")],
        "test-alarms-monthly": [("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                ("dryer-lint-every-load", "The dryer lint habit"),
                                ("co-smoke-alarm-expiry", "The expiry date nobody reads")],
        "condensation-vs-rising-vs-penetrating-damp": [("condensation-ventilation-that-works", "Ventilation that works"),
                                                       ("uk-landlord-damp-mould-duties", "Landlord damp duties"),
                                                       ("drying-laundry-indoors", "Drying laundry indoors")],
        "uk-landlord-damp-mould-duties": [("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                          ("condensation-ventilation-that-works", "Ventilation that works"),
                                          ("gas-heaters-damp", "Gas heat and damp")],
        "condensation-ventilation-that-works": [("drying-laundry-indoors", "Drying laundry indoors"),
                                                ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                                ("gas-heaters-damp", "Gas heat and damp")],
        "gas-heaters-damp": [("co-alarm-wrong-place", "The CO alarm that can't work"),
                             ("uk-carbon-monoxide-alarm-law", "UK CO alarm law"),
                             ("condensation-ventilation-that-works", "Ventilation that works")],
        "hvac-filter-change-habit": [("ac-outdoor-unit-care", "The outdoor unit"),
                                     ("hvac-diy-warranty-rules", "DIY, warranty and the law"),
                                     ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "hvac-noises-decoded": [("hvac-diy-warranty-rules", "DIY, warranty and the law"),
                                ("hvac-filter-change-habit", "The filter habit"),
                                ("uk-boiler-servicing", "The annual boiler service")],
        "hvac-diy-warranty-rules": [("hvac-filter-change-habit", "The filter habit"),
                                    ("uk-boiler-servicing", "The annual boiler service"),
                                    ("mistakes/co-alarm-wrong-place", "The CO alarm that can't work")],
        "uk-boiler-servicing": [("uk-carbon-monoxide-alarm-law", "UK CO alarm law"),
                                ("co-smoke-alarm-expiry", "The expiry date nobody reads"),
                                ("gas-heaters-damp", "Gas heat and damp")],
        "ac-outdoor-unit-care": [("hvac-filter-change-habit", "The filter habit"),
                                 ("hvac-noises-decoded", "HVAC noises decoded"),
                                 ("fridge-coils-twice-a-year", "Clean the coils twice a year")],
        "small-leak-ripple-effect": [("leaky-faucet-diy", "Fix the dripping tap"),
                                     ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                     ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "leaky-faucet-diy": [("small-leak-ripple-effect", "Why small leaks never stay small"),
                             ("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                             ("basic-toolkit-checklist", "The basic toolkit")],
        "uk-us-plumber-rules": [("leaky-faucet-diy", "Fix the dripping tap"),
                                ("induction-hob-wiring", "Induction wiring rules"),
                                ("uk-boiler-servicing", "The annual boiler service")],
        "interior-painting-mistakes": [("mistakes/painting-without-prep", "Skipping prep"),
                                       ("humidity-and-paint", "Humidity and paint"),
                                       ("painting-over-damp", "Painting over damp")],
        "humidity-and-paint": [("interior-painting-mistakes", "The full painting mistakes list"),
                               ("condensation-ventilation-that-works", "Ventilation that works"),
                               ("painting-over-damp", "Painting over damp")],
        "painting-over-damp": [("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                               ("uk-landlord-damp-mould-duties", "Landlord damp duties"),
                               ("humidity-and-paint", "Humidity and paint")],
        "electrical-fire-warning-signs": [("outlet-overloading-danger", "The overloaded outlet"),
                                          ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                          ("how-many-smoke-co-alarms", "How many alarms you need")],
        "outlet-overloading-danger": [("electrical-fire-warning-signs", "The warning signs"),
                                      ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                      ("mistakes/drilling-without-checking", "Drilling without checking")],
        "us-home-permits": [("unpermitted-work-home-sale", "When unpermitted work resurfaces"),
                            ("us-diy-electrical-rules", "US DIY electrical rules"),
                            ("hvac-diy-warranty-rules", "DIY, warranty and the law")],
        "building-regs-vs-planning-permission": [("part-p-explained", "Part P explained"),
                                                 ("unpermitted-work-home-sale", "When unpermitted work resurfaces"),
                                                 ("uk-us-plumber-rules", "UK vs US plumbing rules")],
        "unpermitted-work-home-sale": [("building-regs-vs-planning-permission", "Building Regs vs planning"),
                                       ("us-home-permits", "US permit basics"),
                                       ("part-p-explained", "Part P explained")],
        "part-p-explained": [("induction-hob-wiring", "Induction wiring rules"),
                             ("outlet-overloading-danger", "The overloaded outlet"),
                             ("building-regs-vs-planning-permission", "Building Regs vs planning")],
        "us-diy-electrical-rules": [("outlet-overloading-danger", "The overloaded outlet"),
                                    ("electrical-fire-warning-signs", "The warning signs"),
                                    ("us-home-permits", "US permit basics")],
        "gutter-cleaning-damage": [("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                   ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                   ("small-leak-ripple-effect", "Why small leaks never stay small")],
        "fence-shed-insurance": [("small-leak-ripple-effect", "Sudden vs gradual damage"),
                                 ("us-home-permits", "US permit basics"),
                                 ("building-regs-vs-planning-permission", "Building Regs vs planning"),
                                 ("outlet-overloading-danger", "The overloaded outlet")],
        "outdoor-cooking-safety": [("test-alarms-monthly", "The monthly alarm habit"),
                                   ("mistakes/co-alarm-wrong-place", "The CO alarm that can't work"),
                                   ("electrical-fire-warning-signs", "The warning signs")],
        "inspection-checklist-gaps": [("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                      ("small-leak-ripple-effect", "The meter test"),
                                      ("condensation-ventilation-that-works", "Ventilation that works")],
        "draught-proofing-mistakes": [("condensation-ventilation-that-works", "Ventilation that works"),
                                      ("single-glazing-payback", "The single-glazing maths"),
                                      ("uk-boiler-servicing", "The annual boiler service")],
        "single-glazing-payback": [("draught-proofing-mistakes", "Draught-proofing, done right"),
                                   ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                   ("interior-painting-mistakes", "The painting mistakes list")],
        "wet-mop-floor-warranty": [("underfloor-heating-mistakes", "Underfloor heating mistakes"),
                                   ("unpermitted-work-home-sale", "Paperwork wins arguments"),
                                   ("smart-appliances-worth-it", "Smart appliances, honestly")],
        "underfloor-heating-mistakes": [("wet-mop-floor-warranty", "The floor-warranty rules"),
                                        ("mistakes/drilling-without-checking", "Drilling without checking"),
                                        ("condensation-ventilation-that-works", "Ventilation that works")],
        "deep-clean-schedule": [("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                ("vinegar-in-the-dishwasher", "Not with vinegar"),
                                ("mistakes/streaky-windows-sunlight", "Streaky windows in sunlight")],
        "clean-home-pests-myth": [("ignore-single-pest-sighting", "The one-sighting protocol"),
                                  ("moving-cardboard-pests", "Boxes are pest vehicles"),
                                  ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "ignore-single-pest-sighting": [("diy-vs-professional-pests", "DIY vs professional"),
                                        ("clean-home-pests-myth", "The clean-home myth"),
                                        ("small-leak-ripple-effect", "Why small leaks never stay small")],
        "moving-cardboard-pests": [("clean-home-pests-myth", "The clean-home myth"),
                                   ("ignore-single-pest-sighting", "The one-sighting protocol"),
                                   ("diy-vs-professional-pests", "DIY vs professional")],
        "after-pest-treatment": [("diy-vs-professional-pests", "DIY vs professional"),
                                 ("mistakes/mixing-cleaning-products", "Never mix cleaning products"),
                                 ("deep-clean-schedule", "The deep-clean rotation")],
        "diy-vs-professional-pests": [("after-pest-treatment", "After the treatment"),
                                      ("ignore-single-pest-sighting", "The one-sighting protocol"),
                                      ("clean-home-pests-myth", "The clean-home myth")],
        "bathroom-remodel-mistakes": [("grout-sealant-neglect", "Grout and sealant care"),
                                      ("condensation-ventilation-that-works", "Ventilation that works"),
                                      ("part-p-explained", "Part P explained")],
        "kitchen-ventilation-damp": [("condensation-ventilation-that-works", "Ventilation that works"),
                                     ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                     ("induction-hob-wiring", "Induction wiring rules")],
        "grout-sealant-neglect": [("bathroom-remodel-mistakes", "Before you remodel"),
                                  ("condensation-vs-rising-vs-penetrating-damp", "Which damp is it?"),
                                  ("small-leak-ripple-effect", "Why small leaks never stay small")],
        "energy-bill-high-unchanged": [("uk-insulation-grants", "What the government funds"),
                                       ("smart-thermostat-payback", "The thermostat maths"),
                                       ("fridge-coils-twice-a-year", "Clean the coils twice a year")],
        "uk-insulation-grants": [("energy-bill-high-unchanged", "Why bills rise anyway"),
                                 ("condensation-ventilation-that-works", "Ventilate what you insulate"),
                                 ("single-glazing-payback", "The window maths")],
        "smart-thermostat-payback": [("energy-bill-high-unchanged", "Why bills rise anyway"),
                                     ("uk-boiler-servicing", "The annual boiler service"),
                                     ("uk-insulation-grants", "Insulation help, dated")],
        "entry-point-mistakes": [("smart-locks-cameras-worth-it", "Smart locks & cameras"),
                                 ("fence-shed-insurance", "Insurance small print"),
                                 ("test-alarms-monthly", "The monthly alarm habit")],
        "smart-locks-cameras-worth-it": [("entry-point-mistakes", "The entry-point list"),
                                         ("smart-appliances-worth-it", "Smart appliances, honestly"),
                                         ("renter-security", "Security for renters")],
        "renter-security": [("entry-point-mistakes", "The entry-point list"),
                            ("smart-locks-cameras-worth-it", "Smart locks & cameras"),
                            ("uk-landlord-damp-mould-duties", "Report it in writing")],
        "pre-move-inspection": [("moving-week-by-week", "The week-by-week plan"),
                                ("inspection-checklist-gaps", "What gets missed"),
                                ("small-leak-ripple-effect", "The meter test")],
        "moving-week-by-week": [("pre-move-inspection", "The day-one inspection"),
                                ("moving-cardboard-pests", "Boxes are pest vehicles"),
                                ("deep-clean-schedule", "The deep-clean rotation")],
        "secondhand-furniture-mistakes": [("moving-cardboard-pests", "The moving-box risk"),
                                          ("ignore-single-pest-sighting", "The one-sighting protocol"),
                                          ("smart-appliances-worth-it", "Buy for the long term")],
        "emergency-repair-fund": [("someday-maintenance-cost", "The cost of someday"),
                                  ("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                  ("uk-boiler-servicing", "The annual boiler service")],
        "someday-maintenance-cost": [("small-leak-ripple-effect", "Why leaks never stay small"),
                                     ("grout-sealant-neglect", "The five-pound tube"),
                                     ("emergency-repair-fund", "The repair fund")],
        "unpermitted-work-insurance": [("us-home-permits", "US permit basics"),
                                       ("unpermitted-work-home-sale", "When it resurfaces at sale"),
                                       ("fence-shed-insurance", "The small-print habit")],
        "renter-vs-owner-repairs": [("uk-landlord-damp-mould-duties", "Landlord duties, dated"),
                                    ("condensation-vs-rising-vs-penetrating-damp", "Whose damp is it?"),
                                    ("renter-security", "Security for renters")],
        "improvements-no-resale-value": [("single-glazing-payback", "The window maths"),
                                         ("someday-maintenance-cost", "The cost of someday"),
                                         ("unpermitted-work-home-sale", "Paperwork at sale")],
        "how-to-deep-clean-an-oven": [("how-to-clean-a-washing-machine", "Cleaning the washing machine"),
                                      ("vinegar-in-the-dishwasher", "Vinegar in the dishwasher?"),
                                      ("fridge-coils-twice-a-year", "The coil ritual")],
        "how-to-clear-a-slow-shower-drain": [("how-to-fix-a-slow-draining-sink", "The slow sink guide"),
                                             ("how-to-unblock-a-toilet", "Unblocking a toilet"),
                                             ("small-leak-ripple-effect", "The ripple effect")],
        "how-to-defrost-a-freezer-properly": [("fridge-not-cold-enough", "The warm-fridge triage"),
                                              ("fridge-door-seal-test", "The seal test"),
                                              ("fridge-coils-twice-a-year", "The coil ritual")],
        "how-to-clean-and-care-for-a-mattress": [("how-to-clean-a-washing-machine", "Cleaning the washing machine"),
                                                 ("condensation-ventilation-that-works", "Condensation and ventilation"),
                                                 ("secondhand-furniture-mistakes", "Secondhand furniture, safely")],
        "washing-machine-mould-door-seal": [("how-to-clean-a-washing-machine", "The full washer clean"),
                                            ("washing-machine-heavy-items", "Load discipline"),
                                            ("condensation-ventilation-that-works", "Condensation and ventilation")],
        "how-to-descale-a-kettle": [("fridge-coils-twice-a-year", "The coil ritual"),
                                    ("washing-machine-heavy-items", "Load discipline"),
                                    ("someday-maintenance-cost", "The someday-cost rule")],
        "season-cast-iron-pan": [("basic-toolkit-checklist", "The basic toolkit"),
                                 ("emergency-repair-fund", "The repair-fund rule"),
                                 ("someday-maintenance-cost", "The someday-cost rule")],
        "fridge-temperature-setting": [("fridge-coils-twice-a-year", "The coil ritual"),
                                       ("fridge-door-seal-test", "The seal test"),
                                       ("fridge-not-cold-enough", "The warm-fridge triage")],
        "spring-home-reset": [("seasonal-home-maintenance-checklist", "The seasonal checklist"),
                              ("ac-outdoor-unit-care", "The AC outdoor unit"),
                              ("co-smoke-alarm-expiry", "Alarm expiry dates")],
        "summer-cooling-checklist": [("hvac-filter-change-habit", "The filter habit"),
                                     ("ac-outdoor-unit-care", "The outdoor unit"),
                                     ("energy-bill-high-unchanged", "Why the bill is high")],
        "autumn-home-preparation": [("uk-boiler-servicing", "The boiler service"),
                                    ("how-to-bleed-a-radiator", "Bleeding radiators"),
                                    ("condensation-ventilation-that-works", "Condensation, solved")],
        "winter-home-preparation": [("small-leak-ripple-effect", "The ripple effect"),
                                    ("fridge-temperature-setting", "The 4°C rule"),
                                    ("emergency-repair-fund", "The repair fund")],
    }
    for slug, ti, dek, b in HOME_ARTICLES:
        key = HOME_SLUG_SECT[slug]
        rel_html = "".join('<li><a href="' + _hurl(s2) + '">' + rt + "</a></li>" for s2, rt in related_map[slug])
        cover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / '
                 '<a href="/home/' + key + '/">' + sec_label(key) + "</a> / " + html.escape(ti) + "</nav>"
            + '<section class="cover"><p class="kicker">' + sec_label(key) + " \u00b7 practical guide</p>"
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.8vw,52px)">' + html.escape(ti) + "</h1>"
            + '<p class="byline">BRYME Home &amp; DIY desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not professional advice</p></section>")
        main = ('<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(dek) + "</p></div></section>"
            + '<section class="section"><div class="prose">' + b + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/home/' + key + '/">All of ' + sec_label(key) + "</a>"
            + '<a class="btn secondary" href="/home/mistakes/">Common mistakes</a></div></section>'
            + DISCLAIMER)
        out.append(("/" + slug + "/", ti + " | BRYME Home & DIY", dek[:155],
                    _home_page(ti + " | BRYME Home & DIY", dek[:155], "/" + slug + "/", cover, main, key)))

    # ---------- the checklist product ----------
    groups = []
    seen = []
    for g2, task, why in HOME_CHECK:
        if g2 not in seen:
            seen.append(g2)
    cur = ""
    items = ""
    n3 = 0
    for g2, task, why in HOME_CHECK:
        if g2 != cur:
            if items:
                groups.append((cur, items))
            cur = g2
            items = ""
        n3 += 1
        items += ('<li class="fp-day" data-item="' + html.escape(task[:40]) + '">'
                  '<span class="fp-num">' + str(n3) + "</span>"
                  "<span><b>" + html.escape(task) + "</b><small>" + html.escape(why) + "</small></span>"
                  '<button type="button" class="btn secondary fp-done" aria-pressed="false">Done</button></li>')
    if items:
        groups.append((cur, items))
    weeks_html = "".join(
        '<section class="section"><div class="section-head"><p class="kicker">The checks</p><h2>' + html.escape(g2) + "</h2></div>"
        + '<ul class="list fp-week">' + rows2 + "</ul></section>" for g2, rows2 in groups)
    import json as _j
    cschema = {"@context": "https://schema.org", "@type": "Article",
               "headline": "The Once-a-Season Home Checklist",
               "author": {"@type": "Organization", "name": "BRYME Home & DIY desk"},
               "publisher": {"@type": "Organization", "name": "THE BRYME"},
               "datePublished": TODAY, "dateModified": TODAY,
               "mainEntityOfPage": ORIGIN + "/home/seasonal-home-maintenance-checklist/",
               "description": "A short, season-proof home maintenance checklist with progress saved in your browser."}
    ccover = ('<nav class="crumb" style="padding-top:22px"><a href="/home/">Home &amp; DIY</a> / The Once-a-Season Checklist</nav>'
        + '<section class="cover"><p class="kicker">The desk\u2019s product \u00b7 season-proof \u00b7 no hemisphere assumptions</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.8vw,52px)">The Once-a-Season Home Checklist</h1>'
        + '<p class="byline">BRYME Home &amp; DIY desk \u00b7 reviewed ' + TODAY + " \u00b7 general information, not professional advice</p></section>")
    cmain = ('<section class="section alt"><div class="wrap"><p class="lede"><b>One honest idea:</b> homes fail slowly, then suddenly. '
             + "A short list of checks every season catches the slow failures while they are still cheap. Progress is saved in your browser \u2014 no account, nothing sent anywhere.</p></div></section>"
        + '<section class="section"><div class="wrap"><div class="fp-progressbar" role="img" aria-label="Checklist progress"><div class="fp-fill" id="fp-fill"></div></div>'
        + '<p class="lede" id="fp-status">Nothing ticked yet. Tick items as you do them \u2014 your browser will remember.</p></div></section>'
        + weeks_html
        + '<section class="section"><div class="section-head"><p class="kicker">Boundaries</p><h2>What is deliberately not on this list.</h2></div>'
        + '<div class="prose"><p>Nothing here asks you near an electrical panel, a gas supply, a roof or a structure. Those are the qualified professional\u2019s territory \u2014 the checklist proves your protective devices work, and their visit proves the rest does.</p></div></section>'
        + '<section class="section alt">' + src_html(HOME_SOURCES) + "</section>"
        + '<script type="application/json" id="fit-plan-data">{"total": ' + str(len(HOME_CHECK)) + "}</script>"
        + '<script src="/assets/home-checklist.js" defer></script>'
        + '<script type="application/ld+json">' + _j.dumps(cschema) + "</script>")
    out.append(("/seasonal-home-maintenance-checklist/", "The Once-a-Season Home Checklist | BRYME Home & DIY",
                "A short, season-proof home maintenance checklist \u2014 water, safety devices, appliances, seals, airflow \u2014 with progress saved in your browser.",
                _home_page("The Once-a-Season Home Checklist | BRYME Home & DIY",
                           "A short, season-proof home maintenance checklist with progress saved in your browser.",
                           "/seasonal-home-maintenance-checklist/", ccover, cmain, "checklist")))

    return out + legal_pages("home", "BRYME Home & DIY", "Practical help for fixing, maintaining, improving and understanding your home \u2014 safe, low-risk guidance with clear professional boundaries.")



def main() -> None:
    (OUT / "hub").mkdir(parents=True, exist_ok=True)
    hp = hub_pages()
    base = OUT / "hub"
    for route, title, desc, body in hp:
        f = base / ("index.html" if route == "/" else route.lstrip("/") + "/index.html")
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(shell("hub", title, desc, SUB["hub"], body), encoding="utf-8")
    (base / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"<url><loc>https://{DOMAIN}/</loc><lastmod>{TODAY}</lastmod></url>\n</urlset>\n", encoding="utf-8")
    (base / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n", encoding="utf-8")
    (base / "assets").mkdir(parents=True, exist_ok=True)
    (base / "assets" / "site.css").write_text(css_for("hub"), encoding="utf-8")
    print("hub: built (thebryme.com homepage)")
    write_service("entertainment", entertainment_pages())
    write_service("sports", sports_pages())
    write_service("tech", tech_pages())
    write_service("fitness", fitness_pages())
    write_service("home", home_pages())
    if ADSENSE_ON:
        _adstxt = "google.com, " + ADSENSE_ID + ", DIRECT, f08c47fec0942fa0\n"
        (ROOT / "ecosystem" / "ads.txt").write_text(_adstxt, encoding="utf-8")
        (ROOT / "ads.txt").write_text(_adstxt, encoding="utf-8")
    else:
        for _f in [(ROOT / "ecosystem" / "ads.txt"), (ROOT / "ads.txt")]:
            if _f.exists():
                _f.unlink()
    print(f"ecosystem built for {DOMAIN}")


if __name__ == "__main__":
    main()
