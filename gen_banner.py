import html, random

W, H = 1180, 610
FONT = "ui-monospace,'SF Mono','JetBrains Mono',SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

P = {
    'dark': dict(
        bg='#030712', panel='#0F172A', panel_op=.62, border='#FFFFFF', border_op=.08,
        text='#F8FAFC', muted='#94A3B8', a1='#7C3AED', a2='#22D3EE', a3='#10B981',
        link='#22D3EE', asc=['#22D3EE', '#7C3AED', '#22D3EE'],
        blob=['#3B82F6', '#7C3AED', '#10B981'], blob_op=[.20, .22, .14],
        shadow='#000000', shadow_op=.55, noise=.07, asc_blur=3.0,
        sheen='#FFFFFF', sheen_op=.10, top_op=.07, pill_op=.14,
        hover='brightness(1.45) saturate(1.2) drop-shadow(0 0 7px #22D3EE)'),
    'light': dict(
        bg='#FFFFFF', panel='#F8FAFC', panel_op=.80, border='#0F172A', border_op=.08,
        text='#0F172A', muted='#475569', a1='#2563EB', a2='#06B6D4', a3='#10B981',
        link='#2563EB', asc=['#2563EB', '#06B6D4', '#2563EB'],
        blob=['#2563EB', '#06B6D4', '#10B981'], blob_op=[.10, .10, .08],
        shadow='#0F172A', shadow_op=.13, noise=.04, asc_blur=1.4,
        sheen='#FFFFFF', sheen_op=.85, top_op=.9, pill_op=.08,
        hover='brightness(1.12) saturate(1.35) drop-shadow(0 0 6px #06B6D4)'),
}

esc = lambda s: html.escape(s, quote=False)

# ---------------------------------------------------------------- ASCII portrait
ASCII_ART = """\
##########%%#######*#####################***++++++++++*****+++=====+++++++++++++++++++++++++========
###########%#####*****####################*****+***********+++=====+++++++++++++++++++++++++========
#################*****####################***+++*******##***++++=+++++++++++++++++++++++++++========
#################*****###################***+++++++*****##***++++++++*++++++++++++++++++++++========
#################******#################***+++++++++++*******+++++++***+++++++++++++++++++++===-====
################*******#################**%@@@@@@@@@%###****++++++++++++++++++++++++++++++++===--===
################*******#################%@@@@@@@@@@@@@@@@%#*++=====+++++++++++++++++++***+++===-====
####***###########*****##############%@@@@@@@@@@@@@@@@@@@@@@%#+====++++++++++++++++++++***+++=======
###****#####%######################%@@@@@@@@@@@@@@@@@@@@@@@@@@@#====++++++++++++++++++++*++++=======
####*#####%%%%%###################%@@@@@@@@@@@@@@@@@%@@@@@@@@@@@*===++++++++++++++++++++++++========
#########%%%%%%%#################%@@@@@@@@@%%%%%%%##%%%%%%%@@@@@%+==++++++++++++++++++++++++===--===
#######%%%%%%%%%#################@@@@@@@@%###**********###%%%@@@@#==+++++++++++***+++++**+++==----==
#####%%%%%%%%%%#################%@@@@%%#%@@%%%#*+++*%%@%@@@%%%@@@#==+++++++++++***++++***+++==----==
#%%%%%%%%%%%%%%##################@@@@%%%##*****#*+*##*#####%%%@@@@*=+++++++++++***++++***+++==----==
#%%%%%%%%%%%%%%##################%@@@%##%%%%#####*#####%%#%##%@@@@*+++++++++++++**++++***+++===-====
#%%%%%%%%%%%%%%###################%@@%####****###*###****#####@@%*+++++++++++++***++++****++========
####%%%%%@%%%%%########################*******###**##*******##%%#******++++++++***++++****++========
#%%%%%%%%@@%%%%########################***+++*##*++*##+++***###*********++++++***+++++++++++========
#%%%%%%@@@@%%%%#########################*+++**########*****######********+++++***+++++++++++========
#%%%%%%%%%%%%%%#########################***###############*##%##****#***********++++++++++++========
#%%%%%%%%%%%%%%%#####################%%###############%#####%%******###**********+++++++++++=======+
###%%%%%%%%%%%%%####################%%%%%######*******#####%%#*****####***********++++++++++++===+++
####%%%%%%%%%%%%##################%%%%%%%%###*********##%%%%%******######***********+++****+++++++++
####%%%%%%%%%%%%%##################%%%#%%%%%%#########%%%%%%%*****##############*************+++++++
###%%%%%%%%%%%%%%#########*****####%%%###%%%%%%##**##%%%%%%##*****################*****##****+++++++
##%%%%%%%%%%%%%%%########******####%%%####%%%%%%####%%%%%####******######################***++++++++
#%%%%%%%%@@@%%%%%%#################%%%###**##%%@@@@@@%%##***#******#######**#########*******++++++++
#%%%%%%%@@@@@%%%%%%###############%%%%#*#***###*******##****#******######*****####*********+++++++++
#%%%%%%%%@@@%%%%%%%#############%%%%%#*+**********++**##****+****########******************+++++++++
#%%%%%%%%%%%%%%%%###################***+++*****************+*********####******************+++++++++
#######%%%%%%%%%################********+++*+*************+********+************************++++++++
*#######%%%%%%%##############***+**+++**+++**+****+*****+++***+*+*++***+++*****##************+++++++
****#####%%%%%##########****++**++++++++*++**++*******++++***++++*++****+++*+*****************++++**
******####%%%#####******+**+++**+++++++++*+++*++*****+++***++++++++++***+++*++****************++++**
+******###%%%####*****+++*+++++*+++++++++++++++****+++++++*++++++++++*+++++++++*++++***********+++**
+*******###%###*****++++++++++++++++++++++++++++**+++++++++++++++++*++++++++++++++++*********+****
+*******###%##***+**+++++++++++++++++++++++++++++++++++++++++++++++++*+++++++++++++++++*************
+*******####***++++*+++++++++++++++++++++++++++++++++=+++++++++++++++++++++++++++++++++*************
++******###**+++++++++++++++++++++++++++++++++++++++=++++++++++++++++++++++++++++++++++*+*++*********
+******####**++++++++++++++++++++++++++++++++++=+++==++++++++++++++++++++++++++++++++++++*++********
+*****####***++++++++++++==+++++++++++++++++++++++===+++++++++++++++++++++++++++++++++*+++++***+****
**#####%%#*+*==++==+++=++=+++++++++++++++=+++=+++++=++++++++++++++++++++++++++++=+++++*+++++*********
###%%%%%#*++*+=+++=+++=+==+++++++++=========+++++===++++++++++++++++++++++++++++++++++++++++********
#%%%%%%%**+++*===+=+++====+++++++++++==+====++=++======++++=++++++==++++++++++++++++++++++++*++*****
%%%%%%##***+++++=++=++====++++++++===============+=====++++====++====+++++++++++++++++*+++++**++*****
#%######+**++=+=++++++===+=+++==================+=====++++++===========+++++++++++*+++++++***++*****
######**++*+++=++++++++=====++==================+=====++++===============++++++++**++++++++++++****
*********+**+++=++++**++++=====================+======+++=================++++++**+++++++++++++*****
*********++*+++++==++**++++++==+===============+===+===++===============+++++++**++++++*+++++++*****
*********+++*+++++******++++++=================++======++==============++=++++***+++++++++*++++*****
"""
ASCII_LINES = ASCII_ART.splitlines()
ROWS = len(ASCII_LINES)
COLS = max(map(len, ASCII_LINES))
CW, LH = 3.8, 9


def portrait():
    return ASCII_LINES, [" " * len(line) for line in ASCII_LINES]


def line_to_text(s, x0, top, cls, extra=""):
    st = s.rstrip()
    if not st.strip():
        return ""
    lead = len(st) - len(st.lstrip())
    st = st[lead:]
    x = x0 + lead * CW
    return (f'<text x="{x:.1f}" y="{top + 7.5:.1f}" font-size="9" textLength="{len(st) * CW:.1f}" '
            f'lengthAdjust="spacing" xml:space="preserve" {extra}>{esc(st)}</text>')


# ---------------------------------------------------------------- helpers
def clip_typed(cid, x, y, h, n, cw, begin, per_char):
    vals = ";".join(f"{(i * cw):.2f}" if i < n else f"{n * cw + 8:.2f}" for i in range(n + 1))
    kt = ";".join(f"{i / (n + 1):.4f}" for i in range(n + 1))
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="0" height="{h}">'
            f'<animate attributeName="width" values="{vals}" keyTimes="{kt}" calcMode="discrete" '
            f'dur="{per_char * (n + 1):.2f}s" begin="{begin}s" fill="freeze"/></rect></clipPath>')


def fade(begin, dur=.4):
    return (f'<animate attributeName="opacity" from="0" to="1" dur="{dur}s" begin="{begin}s" fill="freeze"/>')


def blink(begin=0):
    return (f'<animate attributeName="opacity" values="1;0" keyTimes="0;.5" calcMode="discrete" '
            f'dur="1.1s" begin="{begin}s" repeatCount="indefinite"/>')


def build(mode):
    c = P[mode]
    out = []
    defs = []
    body = []
    ascii_lines, bg_lines = portrait()

    LX, LY, LW, LHh = 28, 28, 420, 554
    RX, RY, RW, RHh = 472, 28, 680, 554

    # ---------------- defs
    defs.append(f'<clipPath id="card"><rect width="{W}" height="{H}" rx="28"/></clipPath>')
    defs.append(f'<clipPath id="lp"><rect x="{LX}" y="{LY}" width="{LW}" height="{LHh}" rx="20"/></clipPath>')
    defs.append(f'<clipPath id="rp"><rect x="{RX}" y="{RY}" width="{RW}" height="{RHh}" rx="20"/></clipPath>')
    defs.append(f'''<linearGradient id="flow" gradientUnits="userSpaceOnUse" x1="{RX}" y1="0" x2="{RX + 340}" y2="0" spreadMethod="reflect">
<stop offset="0" stop-color="{c['a1']}"/><stop offset=".5" stop-color="{c['a2']}"/><stop offset="1" stop-color="{c['a3']}"/>
<animateTransform attributeName="gradientTransform" type="translate" values="0 0;680 0" dur="9s" repeatCount="indefinite"/></linearGradient>''')
    defs.append(f'''<linearGradient id="flowL" gradientUnits="userSpaceOnUse" x1="{LX}" y1="0" x2="{LX + 210}" y2="0" spreadMethod="reflect">
<stop offset="0" stop-color="{c['a1']}"/><stop offset=".5" stop-color="{c['a2']}"/><stop offset="1" stop-color="{c['a3']}"/>
<animateTransform attributeName="gradientTransform" type="translate" values="0 0;420 0" dur="9s" repeatCount="indefinite"/></linearGradient>''')
    defs.append(f'''<linearGradient id="asc" gradientUnits="userSpaceOnUse" x1="40" y1="70" x2="240" y2="190" spreadMethod="reflect">
<stop offset="0" stop-color="{c['asc'][0]}"/><stop offset=".5" stop-color="{c['asc'][1]}"/><stop offset="1" stop-color="{c['asc'][2]}"/>
<animateTransform attributeName="gradientTransform" type="translate" values="0 0;400 240" dur="10s" repeatCount="indefinite"/></linearGradient>''')
    for i in range(3):
        defs.append(f'<radialGradient id="blob{i}"><stop offset="0" stop-color="{c["blob"][i]}" stop-opacity="{c["blob_op"][i]}"/>'
                    f'<stop offset="1" stop-color="{c["blob"][i]}" stop-opacity="0"/></radialGradient>')
    defs.append(f'<linearGradient id="scanV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["a2"]}" stop-opacity="0"/>'
                f'<stop offset=".5" stop-color="{c["a2"]}" stop-opacity=".16"/><stop offset="1" stop-color="{c["a2"]}" stop-opacity="0"/></linearGradient>')
    defs.append(f'<linearGradient id="scanH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["a2"]}" stop-opacity="0"/>'
                f'<stop offset=".5" stop-color="{c["a2"]}" stop-opacity=".22"/><stop offset="1" stop-color="{c["a2"]}" stop-opacity="0"/></linearGradient>')
    defs.append(f'<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["sheen"]}" stop-opacity="0"/>'
                f'<stop offset=".5" stop-color="{c["sheen"]}" stop-opacity="{c["sheen_op"]}"/><stop offset="1" stop-color="{c["sheen"]}" stop-opacity="0"/></linearGradient>')
    defs.append(f'<linearGradient id="top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="{c["top_op"]}"/>'
                f'<stop offset=".45" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>')
    defs.append(f'<filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="{c["shadow"]}" flood-opacity="{c["shadow_op"]}"/></filter>')
    defs.append(f'<filter id="glowA" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="{c["asc_blur"]}" result="b"/>'
                f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    defs.append('<filter id="glowP" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="2.4" result="b"/>'
                '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    defs.append('<filter id="glowE" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="2.5" result="b"/>'
                '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    defs.append('<filter id="noise" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch" seed="1">'
                '<animate attributeName="seed" values="1;2;3;4;5" dur="1.5s" calcMode="discrete" repeatCount="indefinite"/></feTurbulence>'
                '<feColorMatrix type="saturate" values="0"/></filter>')
    defs.append(f'<mask id="fadeM"><linearGradient id="fadeG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff"/></linearGradient><rect width="{W}" height="{H}" fill="url(#fadeG)"/></mask>')

    # ---------------- background
    body.append(f'<rect width="{W}" height="{H}" fill="{c["bg"]}"/>')
    blobs = [(200, 110, 400, "0 0;60 40;-20 70;0 0", 17), (930, 520, 440, "0 0;-70 -30;30 -60;0 0", 21), (1060, 70, 320, "0 0;-40 50;40 30;0 0", 25)]
    for i, (bx, by, br, vals, dur) in enumerate(blobs):
        body.append(f'<circle cx="{bx}" cy="{by}" r="{br}" fill="url(#blob{i})"><animateTransform attributeName="transform" type="translate" values="{vals}" dur="{dur}s" repeatCount="indefinite"/></circle>')
    body.append(f'<rect width="{W}" height="{H}" filter="url(#noise)" opacity="{c["noise"]}"/>')

    random.seed(5)
    cols = [c['a1'], c['a2'], c['a3']]
    for _ in range(34):
        x, y = random.uniform(10, W - 10), random.uniform(10, H - 10)
        r = random.uniform(.6, 1.7)
        dx, dy = random.uniform(-30, 30), random.uniform(-70, -20)
        dur = random.uniform(8, 18)
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{random.choice(cols)}" opacity="0">'
                    f'<animateMotion path="M0 0 L{dx:.0f} {dy:.0f} L0 0" dur="{dur:.1f}s" begin="-{random.uniform(0, dur):.1f}s" repeatCount="indefinite"/>'
                    f'<animate attributeName="opacity" values="0;.8;0" dur="{random.uniform(3, 6):.1f}s" begin="-{random.uniform(0, 3):.1f}s" repeatCount="indefinite"/></circle>')

    # ---------------- panel builder
    def panel(x, y, w, h, clip, flow):
        s = []
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{c["panel"]}" fill-opacity="{c["panel_op"]}" filter="url(#shadow)"/>')
        s.append(f'<g clip-path="url(#{clip})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#top)"/>'
                 f'<g><polygon points="{x - 120},{y + h} {x - 20},{y} {x + 60},{y} {x - 40},{y + h}" fill="url(#sheen)">'
                 f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;{w + 240} 0" keyTimes="0;.35;1" dur="11s" repeatCount="indefinite"/></polygon></g></g>')
        return "".join(s)

    def panel_edges(x, y, w, h, flow):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="none" stroke="{c["border"]}" stroke-opacity="{c["border_op"] * 2}" stroke-width="1"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="none" stroke="url(#{flow})" stroke-opacity=".5" stroke-width="1.2"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="none" stroke="{c["a2"]}" stroke-width="2" pathLength="1000" stroke-dasharray="70 930" stroke-linecap="round" filter="url(#glowE)">'
                f'<animate attributeName="stroke-dashoffset" values="0;-1000" dur="7s" repeatCount="indefinite"/>'
                f'<animate attributeName="stroke-opacity" values=".35;.9;.35" dur="3.5s" repeatCount="indefinite"/></rect>')

    # ================= LEFT PANEL
    body.append(panel(LX, LY, LW, LHh, 'lp', 'flowL'))
    left = []
    left.append(f'<text x="52" y="58" font-size="11" fill="{c["muted"]}">~/enrique/portrait.ascii</text>')
    left.append(f'<circle cx="394" cy="54.5" r="3" fill="{c["a3"]}"><animate attributeName="opacity" values="1;.25;1" dur="1.8s" repeatCount="indefinite"/></circle>')
    left.append(f'<text x="424" y="58" font-size="11" fill="{c["muted"]}" text-anchor="end">live</text>')
    left.append(f'<line x1="{LX + 18}" y1="70" x2="{LX + LW - 18}" y2="70" stroke="{c["border"]}" stroke-opacity=".12"/>')

    X0, Y0 = LX + (LW - COLS * CW) / 2, 82
    cps, g_lines = [], []
    for r in range(ROWS):
        top = Y0 + r * LH
        cid = f"a{r}"
        cps.append(f'<clipPath id="{cid}"><rect x="{X0 - 2}" y="{top - 1}" width="0" height="{LH + 2}">'
                   f'<animate attributeName="width" from="0" to="{COLS * CW + 4:.0f}" dur=".7s" begin="{.4 + r * .11:.2f}s" fill="freeze"/></rect></clipPath>')
        t_main = line_to_text(ascii_lines[r], X0, top, "m")
        t_bg = line_to_text(bg_lines[r], X0, top, "b", 'opacity=".28"')
        if t_main or t_bg:
            g_lines.append(f'<g clip-path="url(#{cid})">{t_bg}{t_main}</g>')
    defs.extend(cps)
    left.append(
        f'<g fill="url(#asc)" font-family="{FONT}" filter="url(#glowA)">'
        f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -3;0 0" keyTimes="0;.5;1" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1" dur="7s" repeatCount="indefinite"/>'
        + "".join(g_lines) + '</g>')
    left.append(f'<text x="52" y="568" font-size="11" fill="{c["muted"]}">$ ./render --portrait</text>')
    left.append(f'<rect x="{52 + 21 * 6.6 + 3:.1f}" y="558.5" width="7" height="12" fill="{c["a2"]}" opacity="0">{blink(1.0)}</rect>')
    left.append(f'<g clip-path="url(#lp)"><rect x="{LX}" y="{LY - 60}" width="{LW}" height="60" fill="url(#scanV)">'
                f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {LHh + 60}" dur="5s" repeatCount="indefinite"/></rect></g>')
    body.append("".join(left))
    body.append(panel_edges(LX, LY, LW, LHh, 'flowL'))

    # ================= RIGHT PANEL (terminal)
    body.append(panel(RX, RY, RW, RHh, 'rp', 'flow'))
    t = []
    for i, k in enumerate(['a1', 'a2', 'a3']):
        t.append(f'<circle cx="{RX + 24 + i * 16}" cy="48" r="4.2" fill="{c[k]}" opacity=".9"/>')
    t.append(f'<text x="{RX + RW / 2}" y="52" font-size="12" fill="{c["muted"]}" text-anchor="middle">enrique@dev: ~/perfil — zsh</text>')
    t.append(f'<line x1="{RX + 1}" y1="68" x2="{RX + RW - 1}" y2="68" stroke="{c["border"]}" stroke-opacity=".12"/>')

    TX = 500
    # prompt
    t.append(f'<text x="{TX}" y="98" font-size="12" fill="{c["muted"]}" opacity="0">$ whoami{fade(.2)}</text>')

    # greeting
    greet = "Hola, soy Enrique"
    defs.append(clip_typed("cg", TX - 2, 112, 44, len(greet), 18, .6, .07))
    t.append(f'<text x="{TX}" y="146" font-size="30" font-weight="700" fill="url(#flow)" textLength="{len(greet) * 18}" lengthAdjust="spacing" clip-path="url(#cg)">{esc(greet)}</text>')

    # rotating role
    phrases = ["Desarrollador Full Stack", "Administrador de Base de Datos", "Soporte Técnico"]
    dt = .035
    frames = []
    for p in phrases:
        n = len(p)
        for k in range(1, n + 1):
            frames += [(p, k)] * 2
        frames += [(p, n)] * 46
        for k in range(n - 1, -1, -1):
            frames += [(p, k)]
        frames += [(p, 0)] * 7
    N = len(frames)
    kt = ";".join(f"{i / N:.5f}" for i in range(N))
    dur = N * dt
    RW_CW = 10.2
    RXX = TX + 22
    t.append(f'<text x="{TX}" y="182" font-size="17" fill="{c["a3"]}" opacity="0">›{fade(2.0, .3)}</text>')
    for pi, p in enumerate(phrases):
        vals = ";".join(f"{(k * RW_CW + (4 if k else 0)):.1f}" if f == p else "0" for f, k in frames)
        cid = f"cr{pi}"
        defs.append(f'<clipPath id="{cid}"><rect x="{RXX - 2}" y="164" height="26" width="0">'
                    f'<animate attributeName="width" values="{vals}" keyTimes="{kt}" calcMode="discrete" dur="{dur:.2f}s" begin="2s" repeatCount="indefinite"/></rect></clipPath>')
        t.append(f'<text x="{RXX}" y="182" font-size="17" fill="{c["link"]}" textLength="{len(p) * RW_CW:.1f}" lengthAdjust="spacing" clip-path="url(#{cid})">{esc(p)}</text>')
    cx_vals = ";".join(f"{RXX + k * RW_CW + 3:.1f}" for f, k in frames)
    t.append(f'<rect x="{RXX + 3}" y="166" width="9" height="19" fill="{c["link"]}" opacity="0">'
             f'<animate attributeName="x" values="{cx_vals}" keyTimes="{kt}" calcMode="discrete" dur="{dur:.2f}s" begin="2s" repeatCount="indefinite"/>{blink(2.0)}</rect>')

    # details
    details = [("Ubicación:", "Almería", c['text'], None),
               ("Educación:", "Ingeniería Informática", c['text'], None),
               ("Portafolio:", "enriquesantisteban.github.io/portfolio", c['link'],
                "https://enriquesantisteban.github.io/portfolio/"),
               ("Correo:", "ensanfer4@gmail.com", c['link'], "mailto:ensanfer4@gmail.com")]
    DCW = 7.8
    for i, (lab, val, col, href) in enumerate(details):
        y = 216 + i * 22
        n = 12 + len(val)
        begin = 2.6 + i * 1.0
        cid = f"cd{i}"
        defs.append(clip_typed(cid, TX - 2, y - 14, 20, n, DCW, begin, .016))
        value = (f'<a href="{href}" xlink:href="{href}" target="_blank"><text x="{TX + 12 * DCW:.1f}" y="{y}" '
                 f'font-size="13" fill="{col}" textLength="{len(val) * DCW:.1f}" '
                 f'lengthAdjust="spacing">{esc(val)}</text></a>') if href else (
                 f'<text x="{TX + 12 * DCW:.1f}" y="{y}" font-size="13" fill="{col}" '
                 f'textLength="{len(val) * DCW:.1f}" lengthAdjust="spacing">{esc(val)}</text>')
        t.append(f'<g clip-path="url(#{cid})">'
                 f'<text x="{TX}" y="{y}" font-size="13" fill="{c["muted"]}" textLength="{len(lab) * DCW:.1f}" lengthAdjust="spacing">{esc(lab)}</text>'
                 f'{value}</g>')

    # skills
    t.append(f'<text x="{TX}" y="310" font-size="12" fill="{c["muted"]}" opacity="0">$ skills --list{fade(6.3)}</text>')
    sections = [("Languages:", ["C", "C++", "C#", "Java", "JavaScript", "TypeScript", "Python"]),
                ("Frontend Development:", ["HTML5", "CSS3"]), ("Backend Development:", ["Node.js", "Nginx"]),
                ("Databases:", ["MongoDB", "MySQL", "Oracle", "SQLite"]), ("DevOps:", ["Docker", "Jenkins"]),
                ("Software:", ["Blender", "Photoshop", "Figma"]), ("Other:", ["Linux"])]
    k = 0
    for si, (lab, items) in enumerate(sections):
        cy = 334 + si * 25
        t.append(f'<text x="{TX}" y="{cy + 4}" font-size="10.5" fill="{c["muted"]}" opacity="0">{esc(lab)}{fade(6.5 + si * .1)}</text>')
        px = 646
        for it in items:
            w = max(36, len(it) * 7.2 + 22)
            t.append(
                f'<g class="pill" opacity="0">{fade(6.9 + k * .05, .35)}'
                f'<rect x="{px:.1f}" y="{cy - 10}" width="{w:.1f}" height="20" rx="10" fill="{c["a1"]}" fill-opacity="{c["pill_op"]}" stroke="url(#flow)" stroke-width="1" filter="url(#glowP)">'
                f'<animate attributeName="stroke-opacity" values=".55;1;.55" dur="{3 + (k % 5) * .45:.2f}s" begin="{8 + k * .1:.1f}s" repeatCount="indefinite"/></rect>'
                f'<text x="{px + w / 2:.1f}" y="{cy + 4}" font-size="12" fill="{c["text"]}" text-anchor="middle">{esc(it)}</text></g>')
            px += w + 7
            k += 1

    # separator + socials
    t.append(f'<line x1="{TX}" y1="502" x2="{RX + RW - 28}" y2="502" stroke="{c["border"]}" stroke-opacity=".14" opacity="0">{fade(7.8)}</line>')
    t.append(f'<text x="{TX}" y="542" font-size="12" fill="{c["muted"]}" opacity="0">// conectemos{fade(7.8)}</text>')
    stroke = f'fill="none" stroke="{c["text"]}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"'
    icons = {
        'GitHub': ('https://github.com/enriquesantisteban',
                   f'<path transform="translate(-9.5 -9.5) scale(1.19)" fill="{c["text"]}" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>'),
        'LinkedIn': ('https://www.linkedin.com/in/enriquesantisteban/',
                     f'<g {stroke}><rect x="-8" y="-8" width="16" height="16" rx="3.2"/><path d="M-3.8 -1.2V4.6M-3.8 -4.4V-4.3M0 4.6V-1.2M0 1.4C0 -1.6 4.6 -1.8 4.6 1.4V4.6"/></g>'),
        'Instagram': ('https://instagram.com/enrique_sf98',
                      f'<g {stroke}><rect x="-8" y="-8" width="16" height="16" rx="4.6"/><circle r="3.7"/><circle cx="4.7" cy="-4.7" r=".6"/></g>'),
        'Portafolio': ('https://enriquesantisteban.github.io/portfolio',
                       f'<g {stroke}><circle r="8"/><ellipse rx="3.6" ry="8"/><path d="M-8 0H8M-6.8 -4H6.8M-6.8 4H6.8"/></g>'),
        'Gmail': ('mailto:ensanfer4@gmail.com',
                  f'<g {stroke}><rect x="-8.5" y="-6" width="17" height="12" rx="2.2"/><path d="M-8 -4.6L0 1.4L8 -4.6"/></g>'),
    }
    for i, (name, (href, shape)) in enumerate(icons.items()):
        cx = 1118 - (4 - i) * 50
        cy = 538
        t.append(
            f'<a href="{href}" xlink:href="{href}" target="_blank"><g class="soc" opacity="0" transform="translate({cx} {cy})">{fade(8.0 + i * .12)}'
            f'<title>{name}</title>'
            f'<circle r="17" fill="{c["a1"]}" fill-opacity="{c["pill_op"] * .8:.3f}" stroke="url(#flow)" stroke-width="1" filter="url(#glowP)">'
            f'<animate attributeName="stroke-opacity" values=".5;1;.5" dur="{3 + i * .5}s" repeatCount="indefinite"/></circle>{shape}</g></a>')

    body.append("".join(t))
    body.append(f'<g clip-path="url(#rp)"><rect x="{RX}" y="{RY - 60}" width="{RW}" height="60" fill="url(#scanV)" opacity=".7">'
                f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {RHh + 60}" dur="7s" begin="1s" repeatCount="indefinite"/></rect></g>')
    body.append(panel_edges(RX, RY, RW, RHh, 'flow'))

    # global scanline + card border
    body.append(f'<rect x="0" y="-3" width="{W}" height="2" fill="url(#scanH)"><animateTransform attributeName="transform" type="translate" values="0 0;0 {H + 6}" dur="8s" repeatCount="indefinite"/></rect>')

    style = (f'<style>text{{font-family:{FONT}}}'
             '.pill,.soc{transform-box:fill-box;transform-origin:center;transition:transform .25s ease,filter .25s ease;cursor:pointer}'
             f'.pill:hover{{transform:scale(1.12);filter:{c["hover"]}}}'
             f'.soc:hover{{transform:scale(1.18);filter:{c["hover"]}}}</style>')

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'role="img" aria-label="Enrique — Full Stack Developer, perfil de GitHub">'
           f'{style}<defs>{"".join(defs)}</defs>'
           f'<g clip-path="url(#card)">{"".join(body)}</g>'
           f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="28" fill="none" stroke="{c["border"]}" stroke-opacity=".14"/></svg>')
    return svg


for m in ("dark", "light"):
    with open(f"{m}.svg", "w", encoding="utf-8") as f:
        f.write(build(m))
    print(m, "ok")
