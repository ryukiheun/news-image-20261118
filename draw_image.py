#!/usr/bin/env python3
"""Draw the news-image-20261118 infographic: one 1024x1024 PNG summing up
Wednesday 18 November 2026 in six story blocks. Deterministic, no network,
Pillow only. Run: python3 draw_image.py  ->  writes entry.png beside it."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (244, 239, 230)          # warm paper
NAVY = (20, 38, 63)           # masthead
GOLD = (232, 197, 71)         # date + rules
CARD = (255, 255, 255)
INK = (24, 32, 44)            # headline text
BODY = (46, 56, 64)           # summary text, darkened for 300px legibility
MUTED = (120, 126, 138)       # footer text
BORDER = (216, 210, 196)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def chip(draw, x, y, label, color):
    """Small coloured tag with white bold text; returns its width."""
    fnt = font(BOLD, 16)
    tw = draw.textlength(label, font=fnt)
    pad, h = 12, 26
    draw.rounded_rectangle([x, y, x + tw + 2 * pad, y + h], radius=6,
                           fill=color)
    draw.text((x + pad, y + 5), label, font=fnt, fill=(255, 255, 255))
    return tw + 2 * pad


def icon_sanctions(d, x, y, s):
    """Red ban circle with a diagonal bar."""
    red = (176, 58, 46)
    d.ellipse([x + 4, y + 4, x + s - 4, y + s - 4], outline=red, width=6)
    d.line([x + 12, y + s - 12, x + s - 12, y + 12], fill=red, width=6)


def icon_globe(d, x, y, s):
    """Blue globe: circle, meridians, equator."""
    blue = (26, 107, 138)
    d.ellipse([x + 4, y + 4, x + s - 4, y + s - 4], outline=blue, width=5)
    d.ellipse([x + s // 2 - 10, y + 4, x + s // 2 + 10, y + s - 4],
              outline=blue, width=3)
    d.line([x + 4, y + s // 2, x + s - 4, y + s // 2], fill=blue, width=3)
    d.arc([x + 10, y + 12, x + s - 10, y + s - 12], start=200, end=340,
          fill=blue, width=3)


def icon_chart(d, x, y, s):
    """Green rising bars with a trend arrow above them."""
    green = (46, 125, 50)
    bars = [(8, 24), (24, 18), (40, 12)]
    for bx, bh in bars:
        d.rectangle([x + bx, y + s - 8 - bh, x + bx + 12, y + s - 8],
                    fill=green)
    d.line([x + 6, y + s - 24, x + s - 6, y + 10], fill=green, width=5)
    d.polygon([(x + s - 6, y + 10), (x + s - 18, y + 8), (x + s - 8, y + 20)],
              fill=green)


def icon_ballot(d, x, y, s):
    """Navy ballot box with a paper slip and check mark."""
    navy = (108, 52, 131)
    d.rectangle([x + 8, y + 26, x + s - 8, y + s - 6], outline=navy, width=5)
    d.line([x + s // 2 - 8, y + 18, x + s // 2 + 8, y + 18], fill=navy,
           width=5)
    d.polygon([(x + 18, y + 8), (x + 34, y + 8), (x + 30, y + 20),
               (x + 22, y + 20)], fill=navy)
    d.line([x + 16, y + 44, x + 26, y + 52, x + 42, y + 32], fill=navy,
           width=5)


def icon_bank(d, x, y, s):
    """Brown bank: pediment, three columns, base."""
    brown = (147, 81, 22)
    d.polygon([(x + 4, y + 22), (x + s // 2, y + 6), (x + s - 4, y + 22)],
              fill=brown)
    for cx in (14, 26, 38):
        d.rectangle([x + cx, y + 28, x + cx + 6, y + s - 16], fill=brown)
    d.rectangle([x + 6, y + s - 14, x + s - 6, y + s - 8], fill=brown)


def icon_cyclone(d, x, y, s):
    """Teal spiral: three concentric arcs suggesting a storm."""
    teal = (17, 122, 101)
    d.arc([x + 6, y + 6, x + s - 6, y + s - 6], start=20, end=300,
          fill=teal, width=6)
    d.arc([x + 16, y + 16, x + s - 16, y + s - 16], start=140, end=60,
          fill=teal, width=6)
    d.arc([x + 26, y + 26, x + s - 26, y + s - 26], start=260, end=180,
          fill=teal, width=6)


STORIES = [
    ("MIDDLE EAST", (176, 58, 46), icon_sanctions,
     "West Bank settlers face sanctions",
     "Canberra sanctions 3 people and 4 groups over West Bank "
     "settlement growth and settler violence."),
    ("ASIA-PACIFIC", (26, 107, 138), icon_globe,
     "APEC leaders gather in Shenzhen",
     "Xi chairs the 33rd APEC meeting as Trump, Putin and Lee "
     "Jae-myung arrive; Xi, Trump, Putin meet Thursday 19 Nov."),
    ("TECHNOLOGY", (46, 125, 50), icon_chart,
     "Anthropic's giant IPO prices today",
     "US Claude maker sets a $70\u2013$78 price range, valuing "
     "it up to $1.4 trillion fully diluted; trading starts Thursday as ANT."),
    ("AUSTRALIA", (108, 52, 131), icon_ballot,
     "Early voting opens in Victoria",
     "210 polling centres open across the state ahead of the "
     "28 November election; no reason needed."),
    ("ECONOMY", (147, 81, 22), icon_bank,
     "US Fed minutes land today",
     "The record of October's meeting, when rates were held at "
     "3.75\u20134.00% in a 10\u20132 vote, lands as traders price a rise."),
    ("WEATHER", (17, 122, 101), icon_cyclone,
     "Cyclone Akvan bears down on India",
     "Heavy rain reaches Andhra Pradesh as the severe storm heads "
     "for landfall on Friday, with gusts up to 145 km/h."),
]


def draw_card(d, x, y, w, h, tag, color, icon, headline, summary):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                        outline=BORDER, width=2)
    d.rounded_rectangle([x, y, x + w, y + 8], radius=4, fill=color)
    d.rectangle([x, y + 4, x + w, y + 8], fill=color)
    chip(d, x + 18, y + 20, tag, color)
    icon(d, x + w - 82, y + 14, 64)
    head_fnt = font(BOLD, 29)
    lines = wrap(d, headline, head_fnt, w - 36)
    hy = y + 86
    for ln in lines[:2]:
        d.text((x + 18, hy), ln, font=head_fnt, fill=INK)
        hy += 35
    sum_fnt = font(REG, 22)
    slines = wrap(d, summary, sum_fnt, w - 36)
    # One-line headlines leave ~40px empty at the bottom; push the
    # summary down a little so the card fills more evenly.
    sy = hy + 8 + (14 if len(lines) == 1 else 0)
    for ln in slines[:3]:
        d.text((x + 18, sy), ln, font=sum_fnt, fill=BODY)
        sy += 29


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Masthead.
    d.rectangle([0, 0, W, 150], fill=NAVY)
    d.rectangle([0, 150, W, 156], fill=GOLD)
    title_fnt = font(BOLD, 52)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=title_fnt)
    d.text(((W - tw) / 2, 26), title, font=title_fnt, fill=(255, 255, 255))
    date_fnt = font(BOLD, 36)
    date = "Wednesday, 18 November 2026"
    dw = d.textlength(date, font=date_fnt)
    d.text(((W - dw) / 2, 92), date, font=date_fnt, fill=GOLD)

    # Story grid: 2 columns x 3 rows.
    margin, gutter = 24, 20
    cw = (W - 2 * margin - gutter) // 2
    ch = 258
    top = 172
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = margin + col * (cw + gutter)
        y = top + row * (ch + gutter)
        draw_card(d, x, y, cw, ch, *story)

    # Footer.
    foot_fnt = font(REG, 16)
    foot = "Sources: Reuters \u00b7 Yonhap \u00b7 CNBC \u00b7 Federal Reserve \u00b7 IMD \u00b7 VEC"
    fw = d.textlength(foot, font=foot_fnt)
    d.text(((W - fw) / 2, 994), foot, font=foot_fnt, fill=MUTED)

    img.save("entry.png", format="PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
