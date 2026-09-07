#!/usr/bin/env python3
"""Generate og:image social cards (1200x630 PNG) for BRYME pages.

Deterministic: a card is regenerated only when its source title changes
(sha1 sidecar), so repeated builds do not churn the git tree. Skips itself
gracefully if Pillow is unavailable — the committed cards keep serving.

Outputs to assets/og/ (and mirrors to public/assets/og/):
  <guide-slug>.png   one per content/hub/guides/*.md
  essay-<slug>.png   one per content/essays/*.md (README excluded)
  default.png        fallback for home/section pages

Run:  python3 scripts/build-og-images.py
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "og"

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("og: Pillow unavailable — keeping committed cards")
    sys.exit(0)

W, H = 1200, 630
BG = (250, 246, 238)       # --bg cream
INK = (32, 28, 23)         # --ink
ACCENT = (182, 84, 44)     # --accent terracotta
MUTED = (109, 100, 90)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def fonts() -> tuple:
    return (ImageFont.truetype(FONT_BOLD, 46),      # wordmark
            ImageFont.truetype(FONT_BOLD, 66),      # title
            ImageFont.truetype(FONT_REG, 30),       # tagline
            ImageFont.truetype(FONT_BOLD, 26))      # eyebrow


def wrap(draw, text: str, font, max_w: int, max_lines: int = 4) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
            if len(lines) == max_lines:
                break
    lines.append(cur)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(0, len(lines[-1]) - 1)].rstrip() + "…"
    return lines


def card(path: Path, title: str, eyebrow: str) -> None:
    h = hashlib.sha1(f"{title}|{eyebrow}".encode()).hexdigest()
    marker = path.with_suffix(".hash")
    if path.exists() and marker.exists() and marker.read_text() == h:
        return
    wm_f, _, tag_f, eb_f = fonts()
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=2)
    # wordmark
    d.rectangle([64, 64, 100, 100], fill=ACCENT)
    d.text((116, 66), "BRYME", font=wm_f, fill=INK)
    # eyebrow
    d.text((64, 168), eyebrow.upper(), font=eb_f, fill=ACCENT)
    # title — auto-fit: largest size that fits in 3 lines inside the safe area
    y = 216
    for size in (66, 56, 48, 42):
        ti_f = ImageFont.truetype(FONT_BOLD, size)
        lines = wrap(d, title, ti_f, W - 128, 3 if size > 42 else 4)
        if len(lines) <= 3 or size == 42:
            lh = int(size * 1.2)
            for line in lines:
                d.text((64, y), line, font=ti_f, fill=INK)
                y += lh
            break
    # footer
    d.line([64, H - 108, W - 64, H - 108], fill=INK, width=2)
    d.text((64, H - 92), "For writers, about writing — guides, tools and verified opportunities.",
           font=tag_f, fill=MUTED)
    img.save(path, "PNG", optimize=True)
    marker.write_text(h)


def title_of(md_path: Path) -> tuple[str, str]:
    head = md_path.read_text(encoding="utf-8")[:800]
    m = re.search(r"^title:\s*(.+?)$", head, re.M)
    t = m.group(1).strip().strip('"').strip("'") if m else md_path.stem
    s = re.search(r"^section:\s*(.+?)$", head, re.M)
    sec = s.group(1).strip() if s else "essay"
    return t, sec


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for md in sorted((ROOT / "content" / "hub" / "guides").glob("*.md")):
        title, sec = title_of(md)
        card(OUT / f"{md.stem}.png", title, sec.replace("-", " "))
        n += 1
    for md in sorted((ROOT / "content" / "essays").glob("*.md")):
        if md.stem == "README":
            continue
        title, _ = title_of(md)
        card(OUT / f"essay-{md.stem}.png", title, "investigation")
        n += 1
    card(OUT / "default.png", "BRYME — for writers, about writing",
         "guides · tools · verified opportunities")
    n += 1
    # mirror into public/ (build-public-dir stages most dirs; og is generated
    # after it, so copy explicitly)
    pub = ROOT / "public" / "assets" / "og"
    pub.mkdir(parents=True, exist_ok=True)
    import shutil
    for f in OUT.glob("*.png"):
        shutil.copy2(f, pub / f.name)
    print(f"og: {n} cards current in assets/og/")


if __name__ == "__main__":
    main()
