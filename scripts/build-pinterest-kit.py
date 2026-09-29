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
Skips itself gracefully when Pillow is unavailable. The source kit lives at the repo root; the deployed static mirror is public/pinterest/.
"""
from __future__ import annotations

import csv
import hashlib
import html
import re
import shutil
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
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t))).strip()


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
        s = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", pm.group(1)))).strip()
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


def fit_ellipsis(draw, text, fnt, max_w):
    text = text.rstrip()
    suffix = "…"
    while text and draw.textlength(text + suffix, font=fnt) > max_w:
        text = text.rsplit(" ", 1)[0] if " " in text else text[:-1]
    return text.rstrip(" ,.;:-") + suffix if text else suffix


def pin_preview(text: str, limit: int = 130) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    head = text[:limit - 1].rsplit(" ", 1)[0].rstrip(" ,.;:-")
    return (head or text[:limit - 1].rstrip()) + "…"


def render_pin(title, desk_label, dest, out_path, salt, subtitle=""):
    sidecar = out_path.with_suffix(".sha1")
    sig = hashlib.sha1(f"pin-v3|{title}|{desk_label}|{salt}|{subtitle}".encode()).hexdigest()
    if sidecar.exists() and sidecar.read_text().strip() == sig and out_path.exists():
        return False
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # frame
    d.rectangle([40, 40, W - 40, H - 40], outline=BRASS, width=3)
    # kicker
    d.text((90, 120), desk_label.upper(), font=font(34), fill=BRASS)
    d.line([(90, 185), (W - 90, 185)], fill=BRASS, width=2)
    # Headline: cap lines and shorten visibly instead of letting it hit the footer.
    f_head = font(64)
    lines = wrap(d, title, f_head, W - 180)
    while len(lines) > 8 and f_head.size > 48:
        f_head = font(f_head.size - 2)
        lines = wrap(d, title, f_head, W - 180)
    if len(lines) > 8:
        lines = lines[:8]
        lines[-1] = fit_ellipsis(d, lines[-1], f_head, W - 180)
    y = 260
    line_h = max(66, int(f_head.size * 1.34))
    for ln in lines:
        d.text((90, y), ln, font=f_head, fill=INK)
        y += line_h
    # Subtitle: keep complete words and visibly mark any shortening.
    if subtitle:
        f_sub = font(34, bold=False)
        y += 32
        sub_lines = wrap(d, pin_preview(subtitle), f_sub, W - 180)
        if len(sub_lines) > 4:
            sub_lines = sub_lines[:4]
            sub_lines[-1] = fit_ellipsis(d, sub_lines[-1], f_sub, W - 180)
        for ln in sub_lines:
            d.text((90, y), ln, font=f_sub, fill=BRASS)
            y += 50
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
            if render_pin(title, board_name, dest, out, route, lede):
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
1. Complete the owner-held Business account and click Verify after the website claim.
2. Create six boards using the exact names in `manifest.csv`.
3. For each Pin, use the matching image, title, description and destination URL.
   Paste the destination URL into Pinterest's link field as well as keeping it in
   the description. If an alt-text field is shown, use the page's meta description.
4. Start with 3 fresh Pins per week; do not upload all 180 at once. The first
   12-post, four-week sequence is in `launch-schedule-4-weeks.csv`.
5. Review impressions, saves and outbound clicks weekly; adjust later batches
   from observed performance, not guesses.

Vertical 2:3 is Pinterest's recommended format. Do not add unverified claims,
clickbait overlays or paid conversion tracking without a separate owner decision.
"""
    (OUT / "HOWTO.md").write_text(howto, encoding="utf-8")
    # Keep the already-shipped static download mirror identical to the source kit.
    public_kit = PUB / "pinterest"
    if public_kit.exists():
        shutil.rmtree(public_kit)
    public_kit.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUT / "manifest.csv", public_kit / "manifest.csv")
    shutil.copy2(OUT / "HOWTO.md", public_kit / "HOWTO.md")
    schedule = OUT / "launch-schedule-4-weeks.csv"
    if schedule.is_file():
        shutil.copy2(schedule, public_kit / schedule.name)
    shutil.copytree(OUT / "boards", public_kit / "boards")
    print(f"pinterest: {made} new pins, {len(rows)} rows in manifest; public mirror synced")


if __name__ == "__main__":
    main()
