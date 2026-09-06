#!/usr/bin/env python3
"""Freshness harness: does each record's stated rate still appear on its own
guidelines page?

WHAT THIS IS AND IS NOT. This is an automated string-match against the live
page. It is a cheap way to find records that MIGHT have drifted. It is NOT a
verification, and passing it does not earn a record a new lastVerified date -
only a human reading the guidelines does that. BRYME's whole proposition is
that "verified" means someone read it.

Two known limitations, both hit on the first run (2026-09-06):
  - it extracts figures from pay.conditions, which often quotes third-party
    numbers BRYME explicitly DECLINED to adopt, producing false drift
  - it only checks officialUrl, but the real figure sometimes lives in a
    sources[] entry - Listverse publishes its $100 in a PDF author guide,
    not on the submit page

Treat every DRIFT as "go and look", never as "this changed".
"""
import json, re, sys, urllib.request, urllib.error, ssl, html as _html
from concurrent.futures import ThreadPoolExecutor

ROOT = "/home/user/nextclip/"
recs = json.load(open(ROOT + "content/opportunities.json"))["opportunities"]
stale = [r for r in recs if r["lastVerified"] < "2026-09-01"]

CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
UA = {"User-Agent": "Mozilla/5.0 (compatible; BRYME-verify/1.0)"}

def strip(h):
    h = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", _html.unescape(h))

def money_tokens(rec):
    """The distinctive numeric claims BRYME recorded, to look for on the page."""
    d = (rec["pay"].get("display") or "") + " " + (rec["pay"].get("conditions") or "")
    out = set()
    for m in re.findall(r"[\d][\d,]*\.?\d*", d):
        v = m.replace(",", "")
        if len(v) >= 2 and v not in ("2026", "2025", "2027"):
            out.add(v)
    return sorted(out)[:6]

def check(rec):
    url = rec.get("officialUrl") or ""
    if not url:
        return (rec["slug"], "NO-URL", "", [])
    try:
        req = urllib.request.Request(url, headers=UA)
        raw = urllib.request.urlopen(req, timeout=25, context=CTX).read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return (rec["slug"], f"HTTP-{e.code}", url, [])
    except Exception as e:
        return (rec["slug"], type(e).__name__, url, [])
    txt = strip(raw)
    toks = money_tokens(rec)
    if not toks:
        return (rec["slug"], "NO-FIGURE", url, [])
    hit = [t for t in toks if t in txt.replace(",", "")]
    status = "OK" if hit else "DRIFT"
    return (rec["slug"], status, url, hit)

print(f"re-verifying {len(stale)} records last checked before September\n")
with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(check, stale))

buckets = {}
for slug, st, url, hit in results:
    buckets.setdefault(st.split("-")[0] if st.startswith("HTTP") else st, []).append((slug, st, url))
for k in sorted(buckets):
    print(f"{k}: {len(buckets[k])}")
print()
for slug, st, url, hit in sorted(results, key=lambda x: x[1]):
    if st != "OK":
        print(f"  {st:<12} {slug:<30} {url[:60]}")
