#!/usr/bin/env python3
"""A10: Google Consent Mode v2 (default denied) + minimal house consent banner.
Idempotent via static marker <!--gfc-->; scoped to site trees only (never node_modules).
Noindex pages skip (regex targets the real robots meta only).
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
NOINDEX = re.compile(r'<meta[^>]+name="robots"[^>]+content="noindex')
MARK = "<!--gfc-->"

HEAD = '''<!--gfc--><script async src="https://fundingchoicesmessages.google.com/i/pub-1881426210393009?ers=1"></script>
<script>
window.googlefc = window.googlefc || {};
googlefc.callbackQueue = googlefc.callbackQueue || [];
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {ad_storage:'denied', ad_user_data:'denied', ad_personalization:'denied', analytics_storage:'denied', wait_for_update: 500});
(function(){
  try {
    var KEY='bryme-consent-v1', c = localStorage.getItem(KEY);
    if (c === 'granted') {
      gtag('consent','update',{ad_storage:'granted', ad_user_data:'granted', ad_personalization:'granted', analytics_storage:'granted'});
      return;
    }
    if (c === 'denied') return;
    var bar = document.createElement('div');
    bar.id = 'bryme-consent-bar';
    bar.style.cssText = 'position:fixed;bottom:0;left:0;right:0;z-index:99;background:#1a2b4a;color:#f4f1ea;font:15px/1.5 Georgia,serif;padding:14px 18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap;box-shadow:0 -4px 18px rgba(0,0,0,.35)';
    bar.innerHTML = '<span style="flex:1;min-width:220px">We use cookies for ads and to understand what you read. You can accept or decline before you continue.</span>'
      + '<button id="cc-ok" style="background:#e4572e;color:#fff;border:0;padding:9px 16px;border-radius:6px;font:600 14px/1 system-ui;cursor:pointer">Accept</button>'
      + '<button id="cc-no" style="background:transparent;color:#f4f1ea;border:1px solid #f4f1ea;padding:8px 14px;border-radius:6px;font:500 14px/1 system-ui;cursor:pointer">Decline</button>';
    var done = function(v){
      localStorage.setItem(KEY, v);
      if (v === 'granted') gtag('consent','update',{ad_storage:'granted', ad_user_data:'granted', ad_personalization:'granted', analytics_storage:'granted'});
      bar.remove();
    };
    document.addEventListener('DOMContentLoaded', function(){
      document.body.appendChild(bar);
      document.getElementById('cc-ok').addEventListener('click', function(){done('granted')});
      document.getElementById('cc-no').addEventListener('click', function(){done('denied')});
    });
  } catch(e) {}
})();
</script>'''

applied = skipped = 0
for base in (ROOT, PUB):
    for f in sorted(base.rglob("index.html")):
        rel = f.relative_to(base).as_posix()
        if rel.startswith(("node_modules/", ".next/", "dist/", "build/")):
            continue
        t = f.read_text(encoding="utf-8")
        if MARK in t or NOINDEX.search(t) or "</head>" not in t:
            skipped += 1
            continue
        t = t.replace("</head>", HEAD + "\n</head>", 1)
        f.write_text(t, encoding="utf-8")
        applied += 1
print(f"consent: {applied} wired, {skipped} skipped")
