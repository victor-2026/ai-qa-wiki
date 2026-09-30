#!/usr/bin/env python3
"""LinkedIn banner 1584x396 for VerdictGate. Variants A (doctrine), B (99%-hook),
C (outline cards), D (article-8 solid fills)."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1584, 396
BG = (13, 17, 23)
GRID = (22, 27, 34)
WHITE = (230, 237, 243)
MUTED = (139, 148, 158)
AMBER = (240, 180, 41)
GREEN = (63, 185, 80)
RED = (248, 81, 73)
DARKRED = (60, 18, 20)
# article-8 solid fills (sampled from 8-cover-architecture.png, repunched)
A8_BLUE = (31, 111, 235)
A8_GREEN = (46, 160, 67)
A8_PURPLE = (137, 87, 229)
A8_SUB = (220, 228, 236)

def fonts():
    d = "/System/Library/Fonts"
    cand = {
        "heavy": [f"{d}/SFNSMonoHeavy.ttf", f"{d}/SFNSMono-Bold.otf"],
        "bold": [f"{d}/SFNSMonoBold.ttf"],
        "reg": [f"{d}/SFNSMono.ttf"],
        "med": [f"{d}/SFNSMono-Medium.otf"],
    }
    out = {}
    for k, paths in cand.items():
        for p in paths:
            if os.path.exists(p):
                out[k] = p
                break
        else:
            out[k] = f"{d}/SFNSMono.ttf"
    return out

F = fonts()

def f(name, size):
    return ImageFont.truetype(F[name], size)

def base():
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)
    for x in range(0, W, 48):
        dr.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 48):
        dr.line([(0, y), (W, y)], fill=GRID, width=1)
    return img, dr

def text_c(dr, xy, s, font, fill):
    dr.text(xy, s, font=font, fill=fill)

def variant_a(path):
    img, dr = base()
    # left block
    text_c(dr, (90, 70), "VerdictGate", f("heavy", 96), WHITE)
    text_c(dr, (94, 185), "Signals inform. Gates decide.", f("bold", 38), GREEN)
    text_c(dr, (94, 245), "mutation evidence  >  risk-tier policy", f("reg", 28), MUTED)
    text_c(dr, (94, 290), "seeded breaks  ·  per-tier gates  ·  published verdicts", f("reg", 28), MUTED)
    # right block: tier chips
    tiers = [("B0", "critical", "0 survivors", RED, True),
             ("B1", "high", "0 survivors", MUTED, False),
             ("B2", "medium", "up to 5%", MUTED, False),
             ("B3", "low", "trend", MUTED, False)]
    x0, y = 1010, 62
    for tag, sev, gate, col, hot in tiers:
        y1 = y + 66
        if hot:
            dr.rounded_rectangle([x0, y, x0 + 484, y1], radius=10, fill=DARKRED, outline=col, width=2)
        else:
            dr.rounded_rectangle([x0, y, x0 + 484, y1], radius=10, outline=(48, 54, 63), width=2)
        text_c(dr, (x0 + 22, y + 12), tag, f("bold", 30), col if hot else WHITE)
        text_c(dr, (x0 + 120, y + 16), sev, f("reg", 26), MUTED)
        tw = dr.textlength(gate, font=f("reg", 26))
        text_c(dr, (x0 + 484 - 22 - tw, y + 16), gate, f("reg", 26), col if hot else MUTED)
        y = y1 + 14
    img.save(path)

def variant_b(path):
    img, dr = base()
    text_c(dr, (90, 60), "99% killed.", f("heavy", 76), (110, 160, 120))
    text_c(dr, (90, 150), "1 survived.", f("heavy", 76), RED)
    dr.rounded_rectangle([90, 255, 560, 325], radius=10, fill=DARKRED, outline=RED, width=2)
    text_c(dr, (118, 270), "GATE: FAIL  —  B0 payment", f("bold", 30), WHITE)
    # right block
    text_c(dr, (830, 110), "Same score.", f("heavy", 48), WHITE)
    text_c(dr, (830, 172), "Different risk.", f("heavy", 48), AMBER)
    text_c(dr, (830, 252), "per-risk-tier verdicts", f("reg", 28), MUTED)
    text_c(dr, (830, 290), "over mutation evidence", f("reg", 28), MUTED)
    text_c(dr, (830, 328), "VerdictGate  -  independent practice", f("reg", 28), MUTED)
    img.save(path)

BLUE = (88, 166, 255)
VIOLET = (163, 113, 247)
CARD = (22, 27, 34)

def sans(bold, size):
    for idx in ([1, 4] if bold else [0, 2, 5]):
        try:
            return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=idx)
        except Exception:
            continue
    return ImageFont.load_default()

def variant_c(path):
    """House style: flat #0d1117, layered cards (blue/violet/green), amber connectors,
    white titles, colored subs, author signature. No structural red."""
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)
    # title block, left-top
    dr.text((90, 44), "VerdictGate", font=sans(True, 72), fill=WHITE)
    dr.text((382, 132), "Signals inform. Gates decide.", font=sans(False, 32), fill=GREEN)
    # three cards - shifted right, clear of bottom-left avatar (~350px)
    cards = [
        ("SEED", "mutants in", BLUE),
        ("JUDGE", "B0 zero  ·  B2 band", VIOLET),
        ("POLICY", "evidence out", GREEN),
    ]
    x, y, cw, ch = 380, 208, 330, 118
    for i, (t, sub, col) in enumerate(cards):
        x0 = x + i * (cw + 60)
        w = 4 if i == 1 else 2
        dr.rounded_rectangle([x0, y, x0 + cw, y + ch], radius=12, fill=CARD, outline=col, width=w)
        tw = dr.textlength(t, font=sans(True, 40))
        dr.text((x0 + (cw - tw) / 2, y + 18), t, font=sans(True, 40), fill=WHITE)
        sw = dr.textlength(sub, font=sans(False, 24))
        dr.text((x0 + (cw - sw) / 2, y + 70), sub, font=sans(False, 24), fill=col)
        if i < 2:
            ax = x0 + cw + 8
            dr.line([(ax, y + ch / 2), (ax + 44, y + ch / 2)], fill=AMBER, width=6)
            dr.polygon([(ax + 44, y + ch / 2 - 10), (ax + 44, y + ch / 2 + 10), (ax + 58, y + ch / 2)], fill=AMBER)
    # footer signature
    sig = "Victor Ematin  ·  AI Quality Engineering Lead"
    sw = dr.textlength(sig, font=sans(False, 22))
    dr.text((W - 90 - sw, H - 44), sig, font=sans(False, 22), fill=MUTED)
    img.save(path)


SLIDE_X = 420  # content starts right of avatar overlay
FOOT = "Victor Ematin  ·  AI Quality Engineering Lead"

def foot(dr):
    sw = dr.textlength(FOOT, font=sans(False, 22))
    dr.text((W - 90 - sw, H - 44), FOOT, font=sans(False, 22), fill=MUTED)

def mixed(dr, x, y, segs, font):
    for s, col in segs:
        dr.text((x, y), s, font=font, fill=col)
        x += dr.textlength(s, font=font)
    return x

def badge(dr, text, font, bg, fg):
    tw = dr.textlength(text, font=font)
    x0, y0 = W - 90 - tw - 44, 36
    dr.rounded_rectangle([x0, y0, x0 + tw + 44, y0 + 56], radius=10, fill=bg)
    dr.text((x0 + 22, y0 + 10), text, font=font, fill=fg)

def slide2(path):
    """Problem: silent green. Amber badge, two-tone headline."""
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)
    badge(dr, "SILENT GREEN", sans(True, 28), AMBER, BG)
    h = sans(True, 52)
    mixed(dr, SLIDE_X, 120, [("A tool that ", WHITE), ("fails red", RED),
          (" costs you an hour.", WHITE)], h)
    mixed(dr, SLIDE_X, 196, [("A tool that ", WHITE), ("lies green", GREEN),
          (" costs you the release.", WHITE)], h)
    dr.text((SLIDE_X, 290), "Article 26 · Quality Operating Model", font=sans(False, 24), fill=MUTED)
    foot(dr)
    img.save(path)

def slide3(path):
    """Method: 5 mutation scenarios, article-8 solid fills."""
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)
    dr.text((SLIDE_X, 30), "THE METHOD — 5 SCENARIOS", font=sans(True, 26), fill=MUTED)
    nodes = [
        ("BASELINE", "green > green", A8_BLUE),
        ("DRIFT", "heal > green", A8_GREEN),
        ("WEAK DECOY", "flag > green", A8_PURPLE),
        ("STRONG DECOY", "flag > green", A8_PURPLE),
        ("REGRESSION", "catch > green", A8_GREEN),
    ]
    bw, gap, y, bh = 196, 22, 100, 140
    for i, (t, sub, col) in enumerate(nodes):
        x0 = SLIDE_X + i * (bw + gap)
        dr.rounded_rectangle([x0, y, x0 + bw, y + bh], radius=12, fill=col)
        tw = dr.textlength(t, font=sans(True, 22))
        dr.text((x0 + (bw - tw) / 2, y + 30), t, font=sans(True, 22), fill=WHITE)
        sw = dr.textlength(sub, font=sans(False, 21))
        dr.text((x0 + (bw - sw) / 2, y + 78), sub, font=sans(False, 21), fill=A8_SUB)
    dr.text((SLIDE_X, 278), "When every row is green, green means nothing.",
            font=sans(True, 32), fill=WHITE)
    foot(dr)
    img.save(path)

def slide4(path):
    """Proof: terminal evidence card."""
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)
    dr.rounded_rectangle([SLIDE_X, 56, W - 90, 320], radius=14, fill=CARD,
                         outline=(48, 54, 63), width=2)
    m = f("reg", 30)
    x, y = SLIDE_X + 36, 92
    mixed(dr, x, y, [("$ ", AMBER), ("python3 verdictgate.py results.csv", WHITE)], m)
    mixed(dr, x, y + 56, [("B0 100% (3/3 caught) · 0 survived  ", WHITE), ("PASS", GREEN)], m)
    mixed(dr, x, y + 112, [("B2 band 1/60  ", WHITE), ("gate: HOLD", AMBER)], m)
    dr.text((x, y + 168), "v0.2.2 · static · zero dependencies", font=f("reg", 22), fill=MUTED)
    foot(dr)
    img.save(path)

def slide5(path):
    """CTA: break it on purpose + open source."""
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)
    h = sans(True, 56)
    dr.text((SLIDE_X, 84), "When did you last break", font=h, fill=WHITE)
    dr.text((SLIDE_X, 154), "your testing tool on purpose?", font=h, fill=WHITE)
    dr.text((SLIDE_X, 252), "VerdictGate  ·  Open Source", font=sans(True, 34), fill=A8_GREEN)
    foot(dr)
    img.save(path)

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "/Users/victor/Projects/ai-qa-wiki/outputs"
    variant_a(f"{out}/linkedin-banner-verdictgate-A.png")
    variant_b(f"{out}/linkedin-banner-verdictgate-B.png")
    variant_c(f"{out}/linkedin-banner-verdictgate-C.png")
    print("saved A + B + C")


def variant_d(path):
    """Article-8 style: dark bg, three SOLID saturated blocks (blue/green/purple),
    white bold titles, light subs, white arrows, no amber."""
    img = Image.new("RGB", (W, H), BG)
    dr = ImageDraw.Draw(img)
    # title block, left-top (above avatar overlay - safe zone)
    dr.text((90, 30), "VerdictGate", font=sans(True, 64), fill=WHITE)
    # tagline aligned with blocks (right of avatar overlay)
    dr.text((382, 108), "Signals inform. Gates decide.", font=sans(False, 28), fill=MUTED)
    # three solid blocks - shifted right, clear of bottom-left avatar (~350px)
    blocks = [
        ("SEED", "mutants in", A8_BLUE),
        ("JUDGE", "B0 zero  ·  B2 band", A8_GREEN),
        ("POLICY", "evidence out", A8_PURPLE),
    ]
    x, y, bw, bh = 380, 168, 330, 160
    for i, (t, sub, col) in enumerate(blocks):
        x0 = x + i * (bw + 60)
        dr.rounded_rectangle([x0, y, x0 + bw, y + bh], radius=14, fill=col)
        tw = dr.textlength(t, font=sans(True, 40))
        dr.text((x0 + (bw - tw) / 2, y + 26), t, font=sans(True, 40), fill=WHITE)
        sw = dr.textlength(sub, font=sans(False, 24))
        dr.text((x0 + (bw - sw) / 2, y + 92), sub, font=sans(False, 24), fill=A8_SUB)
        if i < 2:
            ax = x0 + bw + 10
            cy = y + bh / 2
            dr.line([(ax, cy), (ax + 40, cy)], fill=WHITE, width=7)
            dr.polygon([(ax + 40, cy - 11), (ax + 40, cy + 11), (ax + 56, cy)], fill=WHITE)
    # footer signature
    sig = "Victor Ematin  ·  AI Quality Engineering Lead"
    sw = dr.textlength(sig, font=sans(False, 22))
    dr.text((W - 90 - sw, H - 44), sig, font=sans(False, 22), fill=MUTED)
    img.save(path)
