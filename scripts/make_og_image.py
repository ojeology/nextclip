"""Generate the house social card (1200x630) - batch 31, 11 Sep 2026."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#101a2b")
d = ImageDraw.Draw(img)
# subtle top rule
d.rectangle([0, 0, W, 6], fill="#c8a24a")

def font(size, bold=False):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""),):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

f_kick = font(30, True)
f_title = font(96, True)
f_sub = font(34)
f_desk = font(26, True)

d.text((80, 90), "A FAMILY OF INDEPENDENT PUBLICATIONS", font=f_kick, fill="#c8a24a")
d.text((76, 150), "THE BRYME", font=f_title, fill="#f5f1e8")
d.text((80, 290), "Six publications. One house standard.", font=f_sub, fill="#d8d4c8")

cols = [("WRITERS", "#1d4e89"), ("SPORT", "#0f7b4f"), ("ENTERTAINMENT", "#6d1832"),
        ("TECH", "#3d2f71"), ("FITNESS", "#a34a00"), ("HOME & DIY", "#644536")]
x, y = 80, 420
for name, color in cols:
    w = d.textlength(name, font=f_desk)
    if x + w + 30 > W - 60:
        x, y = 80, y + 70
    d.rounded_rectangle([x, y, x + w + 36, y + 52], radius=10, fill=color)
    d.text((x + 18, y + 12), name, font=f_desk, fill="#f5f1e8")
    x += w + 62

d.text((80, H - 60), "bryme.onrender.com", font=font(24), fill="#8a94a6")
img.save("public/assets/og.png", optimize=True)
print("og.png written:", os.path.getsize("public/assets/og.png"), "bytes")
