#!/usr/bin/env python3
"""Draw entry.png for news-image-20261122: one image summing up the world news
of Sunday 22 November 2026. Original flat illustration drawn with PIL shapes
only - no photographs, no copied artwork. Output: 1024x1024 PNG, < 1 MiB."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 242, 231)      # newsprint
INK = (18, 20, 26)        # near-black
NAVY = (18, 40, 75)
RED = (178, 34, 34)
ORANGE = (214, 110, 24)
TEAL = (14, 110, 110)
GOLD = (196, 148, 28)
PAPER = (255, 253, 246)
GREY = (90, 92, 98)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


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


def text_block(draw, x, y, text, fnt, color, max_w, leading=6):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += fnt.size + leading
    return y


def kicker(draw, x, y, label, color):
    f = font(SANS_B, 17)
    draw.text((x, y), label.upper(), font=f, fill=color)
    return y + 24


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 112], fill=NAVY)
d.text((512, 14), "THE WORLD IN ONE DAY", font=font(SERIF_B, 54),
       fill=(255, 253, 246), anchor="ma")
d.text((512, 76), "SUNDAY, 22 NOVEMBER 2026  •  THE DAY'S WORLD NEWS IN ONE IMAGE",
       font=font(SANS_B, 21), fill=(212, 196, 120), anchor="ma")

# ---------------- lead story: COP31 ----------------
d.rounded_rectangle([16, 124, 1008, 296], radius=10, fill=PAPER,
                    outline=(200, 190, 160), width=2)
d.rectangle([16, 124, 1008, 160], fill=RED)
d.text((32, 131), "LEAD STORY — CLIMATE", font=font(SANS_B, 20), fill=(255, 255, 255))
d.text((32, 168), "COP31 COLLAPSES", font=font(SERIF_B, 46), fill=INK)
text_block(d, 32, 224,
           "Climate talks in Antalya end with no deal. The EU rejects a final "
           "text that never mentions fossil fuels — the longest COP ever ends in failure.",
           font(SANS, 22), INK, 660, leading=5)
# icon: globe with a red slash
cx, cy, r = 880, 228, 52
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(52, 120, 180), outline=NAVY, width=3)
d.polygon([(cx - 38, cy - 8), (cx - 6, cy - 26), (cx + 12, cy - 2), (cx - 10, cy + 14)],
          fill=(74, 160, 90))
d.polygon([(cx + 6, cy + 18), (cx + 34, cy + 6), (cx + 40, cy + 28), (cx + 14, cy + 38)],
          fill=(74, 160, 90))
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
d.line([cx - r + 6, cy + r - 6, cx + r - 6, cy - r + 6], fill=RED, width=9)

# ---------------- story panels ----------------
PANELS = [
    # (x0, y0, x1, y1, kicker, accent, title, body, icon)
    (16, 308, 500, 520, "MIDDLE EAST", RED, "IRAN STRIKES IN THE GULF",
     "Iran hits a US base site in Bahrain and tankers near the Strait of "
     "Hormuz. Two people hurt.", "gulf"),
    (524, 308, 1008, 520, "UKRAINE", NAVY, "WAR HITS HOME",
     "A Russian strike partly collapses a block of flats in Dymer, near Kyiv, "
     "killing 2. A Russian ship is hit by a suspected drone off Libya.", "kyiv"),
    (16, 532, 500, 744, "INDONESIA", ORANGE, "FACTORY FIRE",
     "A blaze at a candy factory in Cikande, Banten, kills 3 workers. Dozens "
     "are still missing as rescuers search the ruins.", "fire"),
    (524, 532, 1008, 744, "SPACE", TEAL, "A PROBE REACHES MERCURY",
     "Europe and Japan's BepiColombo spacecraft enters orbit around Mercury "
     "after an eight-year journey through space.", "mercury"),
]
BODY = font(SANS, 20)
TITLE = font(SERIF_B, 27)


def icon_gulf(x, y, s):
    d.rectangle([x, y + s * 0.62, x + s, y + s], fill=(52, 120, 180))
    d.polygon([(x + s * 0.08, y + s * 0.62), (x + s * 0.45, y + s * 0.62),
               (x + s * 0.38, y + s * 0.42), (x + s * 0.15, y + s * 0.42)],
              fill=(40, 44, 54))
    d.rectangle([x + s * 0.52, y + s * 0.5, x + s * 0.92, y + s * 0.62], fill=(90, 92, 98))
    d.line([x + s * 0.15, y + s * 0.35, x + s * 0.75, y + s * 0.05], fill=RED, width=6)
    d.polygon([(x + s * 0.75, y + s * 0.05), (x + s * 0.88, y + s * 0.12),
               (x + s * 0.7, y + s * 0.16)], fill=RED)
    for k in range(3):
        d.arc([x + k * 14, y + s * 0.72, x + s * 0.35 + k * 14, y + s * 0.92],
              200, 340, fill=(255, 255, 255), width=4)


def icon_kyiv(x, y, s):
    d.rectangle([x + s * 0.12, y + s * 0.35, x + s * 0.55, y + s], fill=(120, 122, 130))
    d.polygon([(x + s * 0.12, y + s * 0.35), (x + s * 0.22, y + s * 0.22),
               (x + s * 0.33, y + s * 0.35), (x + s * 0.44, y + s * 0.24),
               (x + s * 0.55, y + s * 0.35)], fill=(120, 122, 130))
    for r_ in range(3):
        for c_ in range(2):
            d.rectangle([x + s * (0.18 + c_ * 0.16), y + s * (0.48 + r_ * 0.16),
                         x + s * (0.28 + c_ * 0.16), y + s * (0.58 + r_ * 0.16)],
                        fill=(255, 220, 120))
    star = [(0.72, 0.05), (0.78, 0.22), (0.95, 0.18), (0.82, 0.32), (0.9, 0.48),
            (0.72, 0.42), (0.62, 0.55), (0.6, 0.36), (0.44, 0.32), (0.58, 0.2)]
    d.polygon([(x + s * a, y + s * b) for a, b in star], fill=ORANGE)
    d.ellipse([x + s * 0.6, y + s * 0.62, x + s * 0.98, y + s * 0.95], fill=(150, 150, 155))
    d.ellipse([x + s * 0.68, y + s * 0.7, x + s * 0.9, y + s * 0.88], fill=(180, 180, 185))


def icon_fire(x, y, s):
    d.rectangle([x + s * 0.08, y + s * 0.62, x + s * 0.92, y + s], fill=(70, 70, 78))
    d.rectangle([x + s * 0.14, y + s * 0.3, x + s * 0.3, y + s * 0.62], fill=(70, 70, 78))
    d.ellipse([x + s * 0.14, y + s * 0.2, x + s * 0.3, y + s * 0.34], fill=(120, 120, 125))
    flame = [(0.5, 0.02), (0.62, 0.28), (0.78, 0.22), (0.72, 0.5), (0.88, 0.45),
             (0.68, 0.72), (0.32, 0.72), (0.16, 0.48), (0.3, 0.45), (0.28, 0.24),
             (0.42, 0.3)]
    d.polygon([(x + s * a, y + s * b) for a, b in flame], fill=ORANGE)
    d.polygon([(0.5 * s + x, 0.3 * s + y), (0.58 * s + x, 0.5 * s + y),
               (0.42 * s + x, 0.5 * s + y)], fill=(255, 220, 120))


def icon_mercury(x, y, s):
    d.ellipse([x + s * 0.08, y + s * 0.08, x + s * 0.92, y + s * 0.92],
              fill=(176, 148, 110), outline=(120, 95, 70), width=3)
    for (a, b, r_) in [(0.3, 0.3, 0.09), (0.62, 0.55, 0.12), (0.45, 0.72, 0.07),
                       (0.68, 0.28, 0.06)]:
        d.ellipse([x + s * (a - r_), y + s * (b - r_), x + s * (a + r_), y + s * (b + r_)],
                  fill=(140, 112, 80))
    d.arc([x - s * 0.15, y - s * 0.05, x + s * 1.15, y + s * 0.75], 200, 340,
          fill=TEAL, width=4)
    d.rectangle([x + s * 0.78, y - s * 0.02, x + s * 0.95, y + s * 0.12], fill=NAVY)


ICONS = {"gulf": icon_gulf, "kyiv": icon_kyiv, "fire": icon_fire, "mercury": icon_mercury}

for (x0, y0, x1, y1, kick, accent, title, body, icon) in PANELS:
    d.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=PAPER,
                        outline=(200, 190, 160), width=2)
    d.rectangle([x0, y0, x1, y0 + 6], fill=accent)
    tx = x0 + 18
    ty = y0 + 16
    ty = kicker(d, tx, ty, kick, accent)
    text_w = (x1 - x0) - 36 - 132  # leave a 132px icon column on the right
    for ln in wrap(d, title, TITLE, text_w):
        d.text((tx, ty), ln, font=TITLE, fill=INK)
        ty += 33
    ty += 4
    text_block(d, tx, ty, body, font(SANS, 19), (40, 42, 48), text_w, leading=5)
    ICONS[icon](x1 - 140, y0 + (y1 - y0 - 108) // 2, 108)

# ---------------- bottom strip: US politics ----------------
d.rounded_rectangle([16, 756, 1008, 900], radius=10, fill=NAVY)
d.text((40, 772), "UNITED STATES", font=font(SANS_B, 17), fill=(212, 196, 120))
d.text((40, 796), "DEMOCRATS' BIGGEST HOUSE WIN", font=font(SERIF_B, 30),
       fill=(255, 253, 246))
d.text((40, 832), "SINCE 1992", font=font(SERIF_B, 30), fill=(255, 253, 246))
d.text((40, 872), "Democrats secure at least 258 House seats — their largest majority in 34 years.",
       font=font(SANS, 19), fill=(220, 222, 228))
d.text((968, 782), "258", font=font(SERIF_B, 76), fill=(212, 196, 120), anchor="ra")
d.text((968, 868), "SEATS", font=font(SANS_B, 18), fill=(212, 196, 120), anchor="ra")

# ---------------- footer ----------------
d.text((512, 922), "Sources: AP • Reuters • BBC • Le Monde • Al Jazeera — reported 22 November 2026.",
       font=font(SANS, 17), fill=GREY, anchor="ma")
d.text((512, 948), "Original illustration drawn for this entry — no photographs used.",
       font=font(SANS, 17), fill=GREY, anchor="ma")
d.text((512, 980), "THE WORLD IN ONE DAY • 22 NOVEMBER 2026",
       font=font(SANS_B, 16), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
