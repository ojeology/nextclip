#!/usr/bin/env python3
"""
Expand the BRYME author trust page (/writers/author/ibrahim-sodiq/).

Audit 2026-09-29 finding: the founder page carried 322 words of main text --
the thinnest trust page on the site, and the page an AdSense reviewer opens
when checking who is accountable for the content.

Everything added here is checkable against this repo or the live site: the
verification method the opportunity records actually use, the fact that scope
counts are published rather than asserted, and the limits of the site's
authority. No credentials, awards, clients, employers or experience are
invented -- the brief forbids fabricated authority, and a thin honest page
beats a padded dishonest one.

Links are emitted in the form each tier needs:
  - scripts/build-writing-first.py : unrouted ("/writing/") + {BASE} placeholder
  - writers/ and public/writers/   : routed ("/writers/writing/")

Idempotent: a file already carrying the expanded section is skipped.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MARKER = "<h2>Beyond the writing desk</h2>"
SENTINEL = "<h2>What BRYME is not</h2>"

# The block to replace: the old closing h2 plus its two paragraphs, stopping
# just before the container close. Anchored on the h2 so it survives the URL
# rewrites the routing step applies to the published copies.
BLOCK_RE = re.compile(
    re.escape(MARKER) + r".*?(?=</div></section></div>)", re.S)

BODY = """<h2>How a BRYME page actually gets made</h2>
<p>The order matters, and it is always the same. A question is chosen because readers ask it, not because a keyword tool likes it. The primary source is then found &mdash; the publication's own submission guidelines, a government page, the manufacturer's own documentation &mdash; and what it says is recorded exactly, including the parts that are inconvenient. Only then is anything written. Anything the source cannot support is left out, and if two sources disagree the page says so rather than picking the tidier answer.</p>
<p>For the opportunity database this produces a fixed set of fields per record: pay, word count, eligibility, submission method, rights, artificial-intelligence policy, who verified it, and the date it was last checked. Rates are never estimated. If a publication does not state its rate, the record says that instead of guessing.</p>
<h2>What has been verified, and how you can check it</h2>
<p>Every claim about scope on this site is countable, so the counts are kept where you can see them rather than in a slogan. The #{OPP} writing opportunities page carries the live number of publications checked by hand, each one linked to its own guidelines. The #{ABOUT} house page lists all seven publications and how many pieces each one holds. Where a page states a date, that date is the last time a human opened the source and confirmed the page still matched it &mdash; it is not a build timestamp.</p>
<h2>What BRYME is not</h2>
<p>It is worth being plain about the limits. BRYME is not a law firm, an accountancy practice or a medical provider, and nothing on this site is professional advice for your specific situation &mdash; the #{DISC} disclaimer says the same thing in full. It is not a recruiter and it does not hold vacancies: where a role is listed, it belongs to the employer or platform that posted it, and the page says so.</p>
<p>BRYME does not sell placement in the opportunity database, and no publication can pay to appear in it or to be ranked above another. Where a page is research rather than firsthand experience, it is labelled as research. Nothing on the site claims an experience that did not happen.</p>
<h2>Beyond the writing desk</h2>
<p>BRYME has grown into a family of specialist publications under one house standard &mdash; see the #{ABOUT} house page for the full list, from #{TECH} BRYME Tech to #{MONEY} BRYME Money. The editing still happens in one place, and the same rules apply on every desk: dated pages, named sources, a public corrections log, and no advertising dressed up as editorial.</p>
<h2>Holding this site to account</h2>
<p>If a page here is wrong, the fastest route is the #{CONTACT} contact page. Corrections are made on the page itself rather than quietly removed, and the change is logged so the record shows what was wrong and when it was fixed &mdash; see #{CORR} how corrections work. Rights questions, takedown requests and factual challenges reach the same place, and they are read by the person who wrote the page.</p>"""

# {BASE} is the generator's own constant; routed pages need the /writers/ prefix.
UNROUTED = {
    "#{OPP}": '<a href="/writing/">', "#{ABOUT}": '<a href="{BASE}/about/">',
    "#{DISC}": '<a href="/disclaimer/">', "#{TECH}": '<a href="{BASE}/tech/">',
    "#{MONEY}": '<a href="https://thebryme.com/money/">',
    "#{CONTACT}": '<a href="/contact/">', "#{CORR}": '<a href="/corrections/">',
}
ROUTED = {
    "#{OPP}": '<a href="/writers/writing/">', "#{ABOUT}": '<a href="/writers/about/">',
    "#{DISC}": '<a href="/writers/disclaimer/">', "#{TECH}": '<a href="https://thebryme.com/tech/">',
    "#{MONEY}": '<a href="https://thebryme.com/money/">',
    "#{CONTACT}": '<a href="/writers/contact/">', "#{CORR}": '<a href="/writers/corrections/">',
}

TARGETS = [
    (ROOT / "scripts" / "build-writing-first.py", UNROUTED),
    (ROOT / "writers" / "author" / "ibrahim-sodiq" / "index.html", ROUTED),
    (ROOT / "public" / "writers" / "author" / "ibrahim-sodiq" / "index.html", ROUTED),
]


def render(links: dict[str, str]) -> str:
    out = BODY
    for k, v in links.items():
        out = out.replace(k, v)
    return out


def main() -> None:
    done = 0
    for path, links in TARGETS:
        if not path.is_file():
            print(f"  skip (absent): {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if SENTINEL in text:
            print(f"  already expanded: {path.relative_to(ROOT)}")
            continue
        if MARKER not in text:
            print(f"  WARN anchor not found: {path.relative_to(ROOT)}")
            continue
        new_text, n = BLOCK_RE.subn(lambda _m: render(links), text, count=1)
        if n != 1:
            print(f"  WARN ambiguous match in {path.relative_to(ROOT)}")
            continue
        path.write_text(new_text, encoding="utf-8")
        done += 1
        print(f"  expanded: {path.relative_to(ROOT)}")
    print(f"expand-author-page: {done} file(s) rewritten")


if __name__ == "__main__":
    main()
