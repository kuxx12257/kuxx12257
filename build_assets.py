#!/usr/bin/env python3
"""Generates the original SVG artwork for the Moon Knight themed profile.

Palette
  void      #05060A   deep black
  bone      #E8E3D9   bone white
  gold      #D4AF37   ceremonial gold
  moonlight #9FB3C8   cold blue-grey
"""
import random
import textwrap

VOID = "#05060A"
BONE = "#E8E3D9"
GOLD = "#D4AF37"
MOONLIGHT = "#9FB3C8"

random.seed(1127)

# --------------------------------------------------------------------------
# shared defs
# --------------------------------------------------------------------------

DEFS = f"""
    <linearGradient id="bg" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0%"   stop-color="#0B0D14"/>
      <stop offset="45%"  stop-color="#06070C"/>
      <stop offset="100%" stop-color="#020204"/>
    </linearGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#E9F1FA" stop-opacity="0.34"/>
      <stop offset="38%"  stop-color="{MOONLIGHT}" stop-opacity="0.13"/>
      <stop offset="100%" stop-color="{MOONLIGHT}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="moonFill" x1="0.1" y1="0" x2="0.9" y2="1">
      <stop offset="0%"   stop-color="#FFFFFF"/>
      <stop offset="42%"  stop-color="{BONE}"/>
      <stop offset="100%" stop-color="#A7A092"/>
    </linearGradient>
    <!-- userSpaceOnUse: a horizontal line has a zero-height bounding box, so an
         objectBoundingBox gradient on it collapses and renders nothing. -->
    <linearGradient id="gold" gradientUnits="userSpaceOnUse" x1="62" y1="0" x2="702" y2="0">
      <stop offset="0%"   stop-color="#6E5410" stop-opacity="0"/>
      <stop offset="18%"  stop-color="#9B7A1C"/>
      <stop offset="50%"  stop-color="#F3E3A0"/>
      <stop offset="82%"  stop-color="#9B7A1C"/>
      <stop offset="100%" stop-color="#6E5410" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="goldSolid" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#B98F1E"/>
      <stop offset="50%"  stop-color="#F3E3A0"/>
      <stop offset="100%" stop-color="#B98F1E"/>
    </linearGradient>
"""

SERIF = "Georgia,'Iowan Old Style','Times New Roman',serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"


def starfield(w, h, n, avoid=None):
    """Scatter faint stars, keeping clear of the moon disc."""
    out = []
    placed = 0
    while placed < n:
        x = random.uniform(6, w - 6)
        y = random.uniform(6, h - 6)
        if avoid:
            cx, cy, r = avoid
            if (x - cx) ** 2 + (y - cy) ** 2 < (r + 26) ** 2:
                continue
        r = random.choice([0.6, 0.7, 0.9, 1.0, 1.3, 1.6])
        delay = round(random.uniform(0, 5.5), 2)
        dur = round(random.uniform(3.2, 6.4), 2)
        base = round(random.uniform(0.10, 0.34), 2)
        out.append(
            f'<circle class="star" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#DCE6F2" '
            f'style="--b:{base};animation-delay:{delay}s;animation-duration:{dur}s"/>'
        )
        placed += 1
    return "\n      ".join(out)


# --------------------------------------------------------------------------
# 1. banner
# --------------------------------------------------------------------------

def banner():
    W, H = 1200, 340
    mx, my, mr = 1002, 158, 92          # moon disc
    stars = starfield(W, H, 74, avoid=(mx, my, mr))

    # ceremonial tick marks flanking the rule
    ticks = "".join(
        f'<rect x="{62 + i * 15}" y="266" width="2" height="{6 if i % 3 else 11}" '
        f'fill="{GOLD}" opacity="{0.15 + (0.30 if i % 3 == 0 else 0):.2f}"/>'
        for i in range(26)
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Kushagra Yadav — multi-agent AI systems and applied research">
  <title>Kushagra Yadav — multi-agent AI systems, built and then stress-tested</title>
  <defs>{DEFS}
    <mask id="crescent">
      <rect width="{W}" height="{H}" fill="#000"/>
      <circle cx="{mx}" cy="{my}" r="{mr}" fill="#fff"/>
      <circle cx="{mx + 44}" cy="{my - 30}" r="{mr - 8}" fill="#000"/>
    </mask>
    <mask id="fadeEdges">
      <linearGradient id="fe" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%"   stop-color="#000"/>
        <stop offset="12%"  stop-color="#fff"/>
        <stop offset="88%"  stop-color="#fff"/>
        <stop offset="100%" stop-color="#000"/>
      </linearGradient>
      <rect width="{W}" height="{H}" fill="url(#fe)"/>
    </mask>
  </defs>

  <style>
    .star {{ opacity: var(--b); animation-name: tw; animation-iteration-count: infinite; animation-timing-function: ease-in-out; }}
    @keyframes tw {{ 0%,100% {{ opacity: var(--b); }} 50% {{ opacity: 0.95; }} }}

    .halo   {{ animation: breathe 9s ease-in-out infinite; transform-origin: {mx}px {my}px; }}
    @keyframes breathe {{ 0%,100% {{ opacity:.62; transform:scale(1); }} 50% {{ opacity:1; transform:scale(1.06); }} }}

    .rule   {{ stroke-dasharray: 640; stroke-dashoffset: 640; animation: draw 11s ease-in-out infinite; }}
    @keyframes draw {{ 0% {{ stroke-dashoffset:640; }} 26%,74% {{ stroke-dashoffset:0; }} 100% {{ stroke-dashoffset:640; }} }}

    .orbit  {{ animation: spin 26s linear infinite; transform-origin: {mx}px {my}px; }}
    @keyframes spin {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}

    .rise   {{ animation: rise 1.6s cubic-bezier(.2,.7,.3,1) both; }}
    @keyframes rise {{ from {{ opacity:0; transform: translateY(10px); }} to {{ opacity:1; transform: none; }} }}
    .d1 {{ animation-delay:.15s }} .d2 {{ animation-delay:.45s }} .d3 {{ animation-delay:.75s }}
  </style>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <g mask="url(#fadeEdges)">
      {stars}
  </g>

  <!-- moon -->
  <circle class="halo" cx="{mx}" cy="{my}" r="180" fill="url(#halo)"/>
  <circle cx="{mx}" cy="{my}" r="{mr}" fill="url(#moonFill)" mask="url(#crescent)"/>
  <g class="orbit">
    <circle cx="{mx}" cy="{my - 148}" r="2.6" fill="{GOLD}" opacity=".85"/>
    <circle cx="{mx}" cy="{my + 148}" r="1.6" fill="{MOONLIGHT}" opacity=".55"/>
  </g>
  <circle cx="{mx}" cy="{my}" r="150" fill="none" stroke="{GOLD}" stroke-width="0.8" opacity=".16"/>
  <circle cx="{mx}" cy="{my}" r="150" fill="none" stroke="{GOLD}" stroke-width="1.6" opacity=".30"
          stroke-dasharray="2 22" stroke-linecap="round"/>

  <!-- wordmark -->
  <g class="rise d1">
    <text x="62" y="132" font-family="{SERIF}" font-size="62" letter-spacing="11"
          fill="{BONE}">KUSHAGRA</text>
    <text x="62" y="200" font-family="{SERIF}" font-size="62" letter-spacing="11"
          fill="url(#goldSolid)">YADAV</text>
  </g>

  <g class="rise d2">
    <line class="rule" x1="62" y1="232" x2="702" y2="232" stroke="url(#gold)" stroke-width="1.5"/>
  </g>

  <g class="rise d3">
    <text x="62" y="258" font-family="{MONO}" font-size="15.5" letter-spacing="3.4"
          fill="{MOONLIGHT}">MULTI-AGENT AI SYSTEMS &#183; APPLIED RESEARCH &#183; EVALUATION</text>
    {ticks}
    <text x="62" y="304" font-family="{MONO}" font-size="12.5" letter-spacing="2.2"
          fill="{GOLD}" opacity=".62">B.TECH CSE (AI &amp; DATA ENGINEERING) &#183; VIT &#183; INDORE, INDIA</text>
  </g>

  <!-- vertical accent between the wordmark and the moon -->
  <g class="rise d3">
    <line x1="784" y1="68" x2="784" y2="288" stroke="{GOLD}" stroke-width="1" opacity=".22"/>
    <circle cx="784" cy="68"  r="2.2" fill="{GOLD}" opacity=".5"/>
    <circle cx="784" cy="288" r="2.2" fill="{GOLD}" opacity=".5"/>
    <text transform="translate(770,288) rotate(-90)" font-family="{MONO}" font-size="11.5"
          letter-spacing="4.6" fill="{MOONLIGHT}" opacity=".55">GITHUB.COM/KUXX12257</text>
  </g>
</svg>
"""


# --------------------------------------------------------------------------
# 2. typewriter tagline
# --------------------------------------------------------------------------

LINES = [
    "> anyone can produce an answer.",
    "> the hard part is knowing whether to believe it.",
    "> so i build the system, then i build its accuser.",
]


def tagline():
    W, H = 1000, 108
    CH = 11.05          # advance width at 18.4px in the mono stack
    FS = 18.4
    cycle = 21.0        # seconds
    slot = cycle / len(LINES)

    groups = []
    for i, line in enumerate(LINES):
        w = len(line) * CH + 4
        t0 = i * slot                       # start typing
        t1 = t0 + 1.9                       # finished typing
        t2 = t0 + slot - 0.75               # start clearing
        t3 = t0 + slot - 0.30               # cleared
        kt = [0.0, t0 / cycle, t1 / cycle, t2 / cycle, t3 / cycle, 1.0]
        # keyTimes must be non-decreasing and start at 0 / end at 1
        kt = [min(1.0, max(0.0, k)) for k in kt]
        kts = ";".join(f"{k:.4f}" for k in kt)
        vals = f"0;0;{w:.1f};{w:.1f};0;0"

        groups.append(f"""
    <clipPath id="clip{i}">
      <rect x="26" y="26" width="0" height="56">
        <animate attributeName="width" values="{vals}" keyTimes="{kts}"
                 dur="{cycle}s" repeatCount="indefinite"/>
      </rect>
    </clipPath>
    <g clip-path="url(#clip{i})">
      <text x="28" y="64" font-family="{MONO}" font-size="{FS}" letter-spacing="0"
            fill="{'#E8E3D9' if i != 2 else GOLD}">{line.replace('&', '&amp;').replace('<', '&lt;')}</text>
    </g>
    <rect y="46" width="2.2" height="24" fill="{GOLD}" opacity=".9">
      <animate attributeName="x" values="28;28;{28 + w:.1f};{28 + w:.1f};28;28"
               keyTimes="{kts}" dur="{cycle}s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0;.9;.9;0;0"
               keyTimes="{kts}" dur="{cycle}s" repeatCount="indefinite"/>
    </rect>""")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{LINES[1][2:]}">
  <title>{LINES[1][2:]}</title>
  <rect width="{W}" height="{H}" fill="none"/>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="4" fill="#07080D" stroke="#1D2029" stroke-width="1"/>
  <rect x="1" y="1" width="3" height="{H-2}" fill="{GOLD}" opacity=".55"/>
  <circle cx="{W-30}" cy="26" r="3.4" fill="{GOLD}" opacity=".5"/>
  <circle cx="{W-44}" cy="26" r="3.4" fill="{MOONLIGHT}" opacity=".3"/>
  <circle cx="{W-58}" cy="26" r="3.4" fill="{BONE}" opacity=".18"/>
  {''.join(groups)}
</svg>
"""


# --------------------------------------------------------------------------
# 3. divider
# --------------------------------------------------------------------------

def divider():
    W, H = 1000, 44
    cx, cy = W / 2, H / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="section divider">
  <defs>
    <linearGradient id="dl" gradientUnits="userSpaceOnUse" x1="20" y1="0" x2="{cx-44}" y2="0">
      <stop offset="0%"  stop-color="{GOLD}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity=".75"/>
    </linearGradient>
    <linearGradient id="dr" gradientUnits="userSpaceOnUse" x1="{cx+44}" y1="0" x2="{W-20}" y2="0">
      <stop offset="0%"   stop-color="{GOLD}" stop-opacity=".75"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .pulse {{ animation: p 6s ease-in-out infinite; transform-origin: {cx}px {cy}px; }}
    @keyframes p {{ 0%,100% {{ opacity:.55 }} 50% {{ opacity:1 }} }}
  </style>
  <line x1="20"  y1="{cy}" x2="{cx-44}" y2="{cy}" stroke="url(#dl)" stroke-width="1.2"/>
  <line x1="{cx+44}" y1="{cy}" x2="{W-20}" y2="{cy}" stroke="url(#dr)" stroke-width="1.2"/>
  <g class="pulse">
    <path d="M{cx} {cy-16} L{cx+16} {cy} L{cx} {cy+16} L{cx-16} {cy} Z"
          fill="none" stroke="{GOLD}" stroke-width="1.1" opacity=".7"/>
    <path d="M{cx+6.5} {cy+0.4} a7.6 7.6 0 1 1 -7.4 -7.6 a5.9 5.9 0 1 0 7.4 7.6 z" fill="{GOLD}"/>
  </g>
  <circle cx="{cx-34}" cy="{cy}" r="1.6" fill="{GOLD}" opacity=".55"/>
  <circle cx="{cx+34}" cy="{cy}" r="1.6" fill="{GOLD}" opacity=".55"/>
</svg>
"""


# --------------------------------------------------------------------------
# 4. play badge
# --------------------------------------------------------------------------

def play_badge():
    W, H = 524, 74
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Play the Moon Knight theme">
  <title>Play the Moon Knight theme — opens the player</title>
  <defs>
    <linearGradient id="btn" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="#12141C"/>
      <stop offset="55%"  stop-color="#0A0B12"/>
      <stop offset="100%" stop-color="#15100A"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#5E4A12"/>
      <stop offset="45%"  stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#5E4A12"/>
    </linearGradient>
  </defs>
  <style>
    .ring1 {{ animation: r 3.4s ease-out infinite; transform-origin: 52px 37px; }}
    .ring2 {{ animation: r 3.4s ease-out infinite 1.7s; transform-origin: 52px 37px; }}
    @keyframes r {{ 0% {{ opacity:.75; transform:scale(.55) }} 100% {{ opacity:0; transform:scale(1.9) }} }}
    /* fill-box keeps scaleY anchored to each bar's own base, not the SVG's */
    .bar {{ animation: eq 1.1s ease-in-out infinite; transform-box: fill-box; transform-origin: bottom; }}
    @keyframes eq {{ 0%,100% {{ transform:scaleY(.3) }} 50% {{ transform:scaleY(1) }} }}
  </style>

  <rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="37" fill="url(#btn)"
        stroke="url(#edge)" stroke-width="1.6"/>

  <circle class="ring1" cx="52" cy="37" r="20" fill="none" stroke="{GOLD}" stroke-width="1.4"/>
  <circle class="ring2" cx="52" cy="37" r="20" fill="none" stroke="{GOLD}" stroke-width="1.4"/>
  <circle cx="52" cy="37" r="20" fill="none" stroke="{GOLD}" stroke-width="1" opacity=".55"/>
  <path d="M56.5 37.6 a10 10 0 1 1 -9.8 -10 a7.7 7.7 0 1 0 9.8 10 z" fill="{BONE}"/>

  <text x="92" y="33" font-family="{MONO}" font-size="14.5" letter-spacing="2.6" fill="{BONE}">PLAY THE MOON KNIGHT THEME</text>
  <text x="92" y="53" font-family="{MONO}" font-size="10.5" letter-spacing="1.9" fill="{GOLD}" opacity=".72">HESHAM NAZIH &#183; OFFICIAL SOUNDTRACK</text>

  <g transform="translate({W-52},48)">
    <rect class="bar" x="0"  y="-16" width="3" height="16" fill="{GOLD}" opacity=".8" style="animation-delay:0s"/>
    <rect class="bar" x="6"  y="-16" width="3" height="16" fill="{GOLD}" opacity=".8" style="animation-delay:.18s"/>
    <rect class="bar" x="12" y="-16" width="3" height="16" fill="{GOLD}" opacity=".8" style="animation-delay:.36s"/>
    <rect class="bar" x="18" y="-16" width="3" height="16" fill="{GOLD}" opacity=".8" style="animation-delay:.54s"/>
  </g>
</svg>
"""


for name, fn in [
    ("banner", banner),
    ("tagline", tagline),
    ("divider", divider),
    ("play-badge", play_badge),
]:
    path = f"assets/{name}.svg"
    with open(path, "w") as fh:
        fh.write(fn())
    print(f"wrote {path}")
