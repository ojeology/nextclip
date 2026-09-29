#!/usr/bin/env python3
"""B2: Pinterest kit — 6 boards x 30 pins (180) from existing desk content.

For each board (one per Pinterest-fit desk) pick the 30 strongest indexable
pages (deterministic: question/how-to titles first, then word count desc,
route asc) and render a vertical 1000x1500 pin card in the house "Editorial"
palette (warm paper / navy ink / brass accent, DejaVu serif). Each pin gets a
keyword description extractive from the page's own lede. Outputs:

  pinterest/manifest.csv      board, title, description, destination, image
  pinterest/boards/<board>/   pin JPEGs (quality 85, keeps the repo lean)
  pinterest/HOWTO.md          owner posting guide (account = D3 owner decision)

Deterministic (sha1 sidecar per pin): repeat builds do not churn the tree.
Skips itself gracefully when Pillow is unavailable. Kit lives at the repo
root, NOT in public/ — these are marketing assets, not site URLs.
"""
from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "public"
OUT = ROOT / "pinterest"
W, H = 1000, 1500

BG = (246, 242, 232)      # warm paper
INK = (29, 37, 49)        # navy ink
BRASS = (143, 106, 30)    # brass accent
RUST = (228, 87, 46)      # house rust

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("pinterest: Pillow unavailable — keeping committed kit")
    sys.exit(0)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

BOARDS = {
    "paid-writing-freelance": (
        "Paid Writing & Freelance Careers",
        "writers",
        "Pitching, rates, paying publications and the freelance writing craft — researched guides from THE BRYME Writers desk.",
    ),
    "home-diy-that-works": (
        "Home & DIY That Actually Works",
        "home",
        "Repairs, maintenance and household fixes explained properly — researched guides from THE BRYME Home desk.",
    ),
    "money-plain-english": (
        "Money Guides in Plain English",
        "money",
        "Pensions, ISAs, tax and everyday money decisions without the jargon — researched guides from THE BRYME Money desk.",
    ),
    "tech-buying-and-fixes": (
        "Tech Buying & Fixes",
        "tech",
        "Spec floors, refurb checks and settings that fix real problems — researched guides from THE BRYME Tech desk.",
    ),
    "fitness-no-myths": (
        "Fitness, No Myths",
        "fitness",
        "Training, recovery and equipment guides without the hype — researched guides from THE BRYME Fitness desk.",
    ),
    "what-to-watch-tonight": (
        "What to Watch Tonight",
        "entertainment",
        "Watch orders, streaming guides and film explainers — researched guides from THE BRYME screen desk.",
    ),
}

H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
P_TAG = re.compile(r"<p[^>]*>(.*?)</p>", re.S)
NOINDEX = re.compile(r'<meta[^>]+name="robots"[^>]+content="noindex')


def strip(t: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def first_sentence(t: str) -> str:
    s = strip(t)
    for sep in (". ", "? ", "! "):
        if sep in s:
            return s.split(sep)[0].strip() + "."
    return s[:200]


def first_lede(t: str) -> str:
    """First substantial body paragraph inside <main> (skip byline/kicker crumbs)."""
    body = t[t.find("<main"):] if "<main" in t else t
    for pm in P_TAG.finditer(body):
        tag = pm.group(0)[:80]
        if re.search(r'class="[^"]*(byline|kicker|crumb|meta|tagline)', tag):
            continue
        s = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", pm.group(1))).strip()
        if len(s.split()) >= 8:
            return s
    return ""


def font(size: int, bold: bool = True):
    name = "DejaVuSerif-Bold.ttf" if bold else "DejaVuSerif.ttf"
    path = FONT_DIR / name
    return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def pick_pages(desk: str, n: int = 30):
    cands = []
    for f in (PUB / desk).rglob("index.html"):
        t = f.read_text(encoding="utf-8")
        if NOINDEX.search(t):
            continue
        m = H1.search(t)
        if not m:
            continue
        title = strip(m.group(1)).rstrip('.')
        lede = first_sentence(first_lede(t))
        if len(lede.split()) < 8:
            continue
        route = "/" + f.parent.relative_to(PUB).as_posix() + "/"
        words = len(re.sub(r"<[^>]+>", " ", t).split())
        howto = 0 if re.match(
            r"(?i)^(how|what|why|when|where|which|does|can|is|should|best|top|\d+)", title
        ) else 1
        cands.append((howto, -words, route, title, lede))
    cands.sort()
    return cands[:n]


def render_pin(title, desk_label, dest, out_path, salt, subtitle=""):
    sidecar = out_path.with_suffix(".sha1")
    sig = hashlib.sha1(f"pin-v2|{title}|{desk_label}|{salt}|{subtitle[:60]}".encode()).hexdigest()
    if sidecar.exists() and sidecar.read_text().strip() == sig and out_path.exists():
        return False
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # frame
    d.rectangle([40, 40, W - 40, H - 40], outline=BRASS, width=3)
    # kicker
    d.text((90, 120), desk_label.upper(), font=font(34), fill=BRASS)
    d.line([(90, 185), (W - 90, 185)], fill=BRASS, width=2)
    # headline
    f_head = font(64)
    lines = wrap(d, title, f_head, W - 180)
    y = 260
    for ln in lines[:8]:
        d.text((90, y), ln, font=f_head, fill=INK)
        y += 86
    # subtitle: extractive lede line
    if subtitle:
        f_sub = font(34, bold=False)
        y += 40
        for ln in wrap(d, subtitle, f_sub, W - 180)[:6]:
            d.text((90, y), ln, font=f_sub, fill=BRASS)
            y += 52
    # footer
    d.line([(90, H - 220), (W - 90, H - 220)], fill=BRASS, width=2)
    d.text((90, H - 180), "thebryme.com", font=font(40), fill=RUST)
    d.text((90, H - 120), "Research before publishing.", font=font(28, bold=False), fill=INK)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "JPEG", quality=85)
    sidecar.write_text(sig)
    return True


def main():
    rows = []
    made = 0
    for board_slug, (board_name, desk, blurb) in BOARDS.items():
        pages = pick_pages(desk)
        for route, title, lede in ((p[2], p[3], p[4]) for p in pages):
            fname = route.strip("/").replace("/", "__") + ".jpg"
            out = OUT / "boards" / board_slug / fname
            dest = "https://thebryme.com" + route
            desc = f"{lede} Read the full guide: {dest} (THE BRYME {desk} desk)."
            if render_pin(title, board_name, dest, out, route, lede[:140]):
                made += 1
            rows.append([board_name, title, desc[:490], dest, f"boards/{board_slug}/{fname}"])
    # prune orphan images/sidecars from earlier selections
    keep = {row[4] for row in rows}
    for f in (OUT / "boards").rglob("*"):
        if f.suffix in (".jpg", ".sha1") and f.relative_to(OUT).as_posix() not in keep \
                and f.with_suffix(".jpg").relative_to(OUT).as_posix() not in keep:
            f.unlink()
    OUT.mkdir(exist_ok=True)
    with open(OUT / "manifest.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["board", "pin_title", "pin_description", "destination_url", "image"])
        w.writerows(rows)
    howto = """# BRYME Pinterest kit — how to post

Six boards, 30 pins each (180 total). Images are vertical 1000x1500 (2:3) JPEGs
in the house style. `manifest.csv` has, per pin: board, title, description
(keyword-rich, extractive from the page), destination URL, image path.

## Posting (owner account = roadmap decision D3)
1. Create the Pinterest account (or a business account under an existing one).
2. Create 6 boards using the exact board names in `manifest.csv`.
3. Pin in manifest order (strongest pages first per board). Native pin flow:
   choose the image, paste the title + description + destination URL.
4. Suggested cadence: 2-3 pins/day per account keeps distribution natural;
   the full kit lands in ~4-6 weeks.

Notes: descriptions already contain the destination URL in text form (safe if
the scheduler strips links); each pin's clickable link is the destination_url.
Vertical 2:3 is Pinterest's recommended format — the site's horizontal OG
cards (`assets/og/`) are fallbacks only if you prefer pixel-exact site imagery.
"""
    (OUT / "HOWTO.md").write_text(howto, encoding="utf-8")
    print(f"pinterest: {made} new pins, {len(rows)} rows in manifest")


if __name__ == "__main__":
    main()
