#!/usr/bin/env python3
"""Generate og:image social cards (1200x630 PNG) for BRYME pages.

Design: "Editorial v3" — aligned to the top writer platforms (Medium /
Substack): white paper, one green accent, serif headline, hairline frame,
domain footer. Deterministic: a card is regenerated only when its design
version or source title changes (sha1 sidecar), so repeated builds do not
churn the git tree. Skips itself gracefully if Pillow is unavailable —
the committed cards keep serving.

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
BG = (255, 255, 255)        # paper white
INK = (26, 26, 26)          # near-black
ACCENT = (26, 137, 23)      # La Palma green (Medium brand green)
MUTED = (107, 107, 107)     # neutral gray
HAIRLINE = (228, 228, 225)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

DESIGN_VERSION = "v3"  # bump to force regeneration of every card


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
    h = hashlib.sha1(f"{DESIGN_VERSION}|{title}|{eyebrow}".encode()).hexdigest()
    marker = path.with_suffix(".hash")
    if path.exists() and marker.exists() and marker.read_text() == h:
        return
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # accent bar across the top + hairline frame (Substack-style inset border)
    d.rectangle([0, 0, W, 12], fill=ACCENT)
    d.rectangle([28, 40, W - 29, H - 41], outline=HAIRLINE, width=2)
    # wordmark
    d.rectangle([72, 76, 108, 112], fill=ACCENT)
    d.text((126, 82), "BRYME", font=ImageFont.truetype(FONT_BOLD, 38), fill=INK)
    # eyebrow — section label in the accent green
    d.text((72, 178), eyebrow.upper(), font=ImageFont.truetype(FONT_BOLD, 25), fill=ACCENT)
    # title — serif, auto-fit: largest size that fits in 3 lines in the safe area
    y = 228
    for size in (76, 64, 54, 46):
        ti_f = ImageFont.truetype(FONT_SERIF_BOLD, size)
        lines = wrap(d, title, ti_f, W - 148, 3 if size > 46 else 4)
        if len(lines) <= 3 or size == 46:
            lh = int(size * 1.18)
            for line in lines:
                d.text((72, y), line, font=ti_f, fill=INK)
                y += lh
            break
    # footer — domain left, tagline right, hairline above
    d.line([72, H - 116, W - 72, H - 116], fill=HAIRLINE, width=2)
    d.text((72, H - 94), "bryme.onrender.com",
           font=ImageFont.truetype(FONT_BOLD, 27), fill=INK)
    tag = "For writers, about writing."
    tag_f = ImageFont.truetype(FONT_REG, 25)
    tw = d.textlength(tag, font=tag_f)
    d.text((W - 72 - tw, H - 93), tag, font=tag_f, fill=MUTED)
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
    # before it now, and again after, so copy explicitly for safety)
    pub = ROOT / "public" / "assets" / "og"
    pub.mkdir(parents=True, exist_ok=True)
    import shutil
    for f in OUT.glob("*.png"):
        shutil.copy2(f, pub / f.name)
    print(f"og: {n} cards current in assets/og/")


if __name__ == "__main__":
    main()
