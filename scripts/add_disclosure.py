#!/usr/bin/env python3
"""Insert a standing disclosure block on YMYL pages (Make Money + Tech).

Deliberately NOT a generic "this post contains affiliate links" notice: a grep of
every outbound link on the site found no affiliate/referral parameters anywhere,
so claiming otherwise would be a false disclosure — the same policy-vs-reality
mismatch that had to be fixed on the privacy policy in item #1.

What is actually true, and therefore what we disclose:
  * BRYME earns from display advertising (Monetag), not from the platforms covered.
  * Nobody pays for coverage or placement.
  * Earnings figures are examples, not forecasts.
  * Rates, fees and eligibility change; readers must verify at the source.
Plus a stronger red variant for genuinely high-risk financial content.
"""
import re, glob, os, sys

ROOT = '/home/user/nextclip'
os.chdir(ROOT)

MARK = 'data-bm-disclosure'

GENERAL = (
 '<aside class="bm-disc" %s="general" role="note" aria-label="Disclosure">'
 '<b>Disclosure</b>'
 '<p>BRYME makes money from display advertising, not from the companies, platforms or '
 'publications written about on this page. No one pays us for coverage, placement or a '
 'favourable review, and we use no affiliate or referral links \u2014 if that ever changes, '
 'this notice changes with it.</p>'
 '<p>Any amounts shown are examples of what others have reported, not a prediction of what '
 'you will earn. Rates, fees, payment methods and eligibility rules change often and vary by '
 'country. Always confirm the current terms on the provider\u2019s own site before you rely on '
 'anything here. See our <a href="/editorial-policy/">editorial policy</a> and '
 '<a href="/disclaimer/">disclaimer</a>.</p>'
 '</aside>') % MARK

RISK = (
 '<aside class="bm-disc is-risk" %s="risk" role="note" aria-label="Risk warning and disclosure">'
 '<b>Risk warning \u2014 read before acting</b>'
 '<p>This page is not financial advice, and nothing on BRYME is. Trading and investment products '
 'carry a real risk of losing your entire deposit. Most retail traders lose money. Never stake '
 'funds you cannot afford to lose, and be sceptical of anyone \u2014 including any app, group or '
 '\u201Cmentor\u201D \u2014 promising guaranteed or fixed returns.</p>'
 '<p>BRYME earns from display advertising only. We are not paid by any broker or trading platform, '
 'we use no affiliate or referral links, and we do not promote trading apps. If you need advice '
 'about your money, speak to a licensed professional. See our '
 '<a href="/editorial-policy/">editorial policy</a> and <a href="/disclaimer/">disclaimer</a>.</p>'
 '</aside>') % MARK

LISTING = (
 '<aside class="bm-disc" %s="listing" role="note" aria-label="Disclosure">'
 '<b>Disclosure</b>'
 '<p>BRYME is not affiliated with this publication and is not paid to list it. We earn from display '
 'advertising only, and use no affiliate or referral links. Pay rates, rights terms, response times '
 'and open/closed status change without notice \u2014 always confirm against the publication\u2019s own '
 'guidelines before submitting. See our <a href="/editorial-policy/">editorial policy</a>.</p>'
 '</aside>') % MARK


def classify(path, html):
    if re.search(r'binary|trading|forex|crypto|invest', path, re.I):
        return RISK, 'risk'
    if '/writing/' in path:
        return LISTING, 'listing'
    return GENERAL, 'general'


def insert(html, block):
    """Place the block at the end of the main content, before related/nav chrome."""
    for anchor in ('</article>', '<section class="oc-editor"', '</main>'):
        i = html.find(anchor)
        if i != -1:
            if anchor == '</article>':
                i += len(anchor)          # just after the article body
            return html[:i] + block + html[i:]
    return None


def main():
    targets = sorted(glob.glob('make-money/**/index.html', recursive=True))
    changed = skipped = failed = 0
    counts = {}
    for f in targets:
        html = open(f, encoding='utf-8').read()
        if MARK in html:
            skipped += 1
            continue
        block, kind = classify(f, html)
        out = insert(html, block)
        if out is None:
            print('  !! no insertion point:', f)
            failed += 1
            continue
        open(f, 'w', encoding='utf-8').write(out)
        counts[kind] = counts.get(kind, 0) + 1
        changed += 1
    print('disclosure added to %d pages (skipped %d, failed %d)' % (changed, skipped, failed))
    print('by type:', counts)


if __name__ == '__main__':
    main()
