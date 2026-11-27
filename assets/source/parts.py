"""Typing strip, section headers, identity terminal, career transit map,
skill matrix, project cards, comms buttons and the skyway footer."""
import random

from lib import (AMBER, BG, BG2, CYAN, DIM, INK, LIME, MAGENTA, ORANGE, SOFT,
                 VIOLET, T, W, car_symbol, doc, hex_points, wrap)

rnd = random.Random(7)


def pct(t, total):
    return f"{t / total * 100:.3f}".rstrip("0").rstrip(".")


# ======================================================================= typing
def typing():
    """A terminal window: tabbed title bar, powerline prompt, typed lines and
    a carousel indicator that tracks which line is showing. Every icon is a
    vector path, because the embedded font subsets carry no symbol glyphs."""
    WD, HT, TB = 1200, 112, 38          # canvas, title-bar height
    CY = TB + (HT - TB) / 2             # body centre line
    phrases = [
        "designing UI/UX that makes learning click",
        "turning maths lessons into playable worlds",
        "crafting 3D storybooks with games inside",
        "designing it, then building it in code",
        "design × technology × storytelling",
    ]
    NIGHT = "#07061A"
    HAIR = "#262257"
    DARK = "#16062B"

    # ---------------------------------------------------------- title bar
    tab_x, tab_txt = 92, "aniket — zsh"
    tab_w = 14 + 13 + 9 + W("m", tab_txt, 12) + 16 + 7 + 12
    tab_d = (f"M{tab_x},{TB}V15Q{tab_x},7 {tab_x + 8},7H{tab_x + tab_w - 8}"
             f"Q{tab_x + tab_w},7 {tab_x + tab_w},15V{TB}Z")
    ti = tab_x + 14
    tcy = TB / 2 + 3
    title = [
        f'<rect width="{WD}" height="{TB}" fill="{NIGHT}"/>',
        f'<path d="M1,{TB}H{tab_x}M{tab_x + tab_w:.1f},{TB}H{WD - 1}" stroke="{HAIR}"/>',
        f'<circle cx="26" cy="{TB / 2}" r="5.5" fill="{MAGENTA}"/>'
        f'<circle cx="45" cy="{TB / 2}" r="5.5" fill="{AMBER}"/>'
        f'<circle cx="64" cy="{TB / 2}" r="5.5" fill="{LIME}"/>',
        f'<path d="{tab_d}" fill="url(#tbg)"/>',
        f'<rect x="{tab_x + 8}" y="7" width="{tab_w - 16:.1f}" height="2" rx="1" fill="url(#tst)"/>',
        # terminal glyph: window, chevron, underscore
        f'<rect x="{ti}" y="{tcy - 6}" width="13" height="11" rx="2.2" stroke="{CYAN}" stroke-width="1.3"/>'
        f'<path d="M{ti + 3},{tcy - 2.6}l2.4,2.1-2.4,2.1M{ti + 7},{tcy + 2.1}h3" stroke="{CYAN}" '
        f'stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>',
        T(ti + 22, tcy + 4, tab_txt, "m", 12, INK),
        f'<path d="M{tab_x + tab_w - 19:.1f},{tcy - 3.5}l7,7m0-7l-7,7" stroke="{DIM}" '
        f'stroke-width="1.3" stroke-linecap="round" opacity=".7"/>',
    ]
    x = tab_x + tab_w + 22
    for name, col in (("design.fig", VIOLET), ("build.tsx", CYAN), ("story.md", AMBER)):
        title.append(f'<circle cx="{x + 3:.1f}" cy="{tcy}" r="3" fill="{col}"/>')
        title.append(T(x + 13, tcy + 4, name, "m", 12, DIM))
        x += 13 + W("m", name, 12) + 22
        title.append(f'<path d="M{x - 11:.1f},{tcy - 7}v14" stroke="{HAIR}"/>')
    title.append(f'<circle cx="1128" cy="{TB / 2}" r="4" fill="{LIME}" class="lv"/>')
    title.append(T(1140, TB / 2 + 4, "LIVE", "m", 11, LIME, ls=2.5))

    # ---------------------------------------------------- powerline prompt
    SH, TIP = 30, 13
    y0, y1 = CY - SH / 2, CY + SH / 2

    def icon(kind, ix, c):
        if kind == "user":
            return (f'<circle cx="{ix + 6}" cy="{CY - 3.4}" r="3.3" fill="{c}"/>'
                    f'<path d="M{ix},{CY + 6.5}c0-4 2.7-5.8 6-5.8s6 1.8 6 5.8z" fill="{c}"/>')
        if kind == "folder":
            return f'<path d="M{ix},{CY - 5.5}h4.6l1.8,2h6.6v9h-13z" fill="{c}"/>'
        return (f'<g stroke="{c}" stroke-width="1.5" fill="none">'
                f'<circle cx="{ix + 3}" cy="{CY - 5.5}" r="1.9"/><circle cx="{ix + 3}" cy="{CY + 5.5}" r="1.9"/>'
                f'<circle cx="{ix + 10.5}" cy="{CY - 3.5}" r="1.9"/><path d="M{ix + 3},{CY - 3.6}v7.2"/>'
                f'<path d="M{ix + 10.5},{CY - 1.6}c0,3.6-7.5,2-7.5,5.2"/></g>')

    segs = [("aniket", "sb", 16, "url(#pl1)", DARK, "user", 5.6),
            ("~/portfolio", "m", 14, "#6A45EE", INK, "folder", 4.8),
            ("main", "m", 14, "#103656", CYAN, "branch", 4.8)]
    x, laid = 24, []
    for i, (txt, f, sz, fill, ink, kind, dy) in enumerate(segs):
        pad = 12 if i == 0 else TIP + 10
        extra = 18 if kind == "branch" else 0
        w = pad + 13 + 9 + W(f, txt, sz) + extra + 10
        laid.append((x, x + w, pad, txt, f, sz, fill, ink, kind, dy))
        x += w
    xe = x + TIP
    prompt = []
    for i, (a, b, pad, txt, f, sz, fill, ink, kind, dy) in reversed(list(enumerate(laid))):
        if i == 0:
            r = 7
            d = (f"M{a + r},{y0}H{b:.1f}L{b + TIP:.1f},{CY}L{b:.1f},{y1}H{a + r}"
                 f"Q{a},{y1} {a},{y1 - r}V{y0 + r}Q{a},{y0} {a + r},{y0}Z")
        else:
            d = f"M{a:.1f},{y0}H{b:.1f}L{b + TIP:.1f},{CY}L{b:.1f},{y1}H{a:.1f}Z"
        g = [f'<path d="{d}" fill="{fill}" stroke="{NIGHT}" stroke-width="2" stroke-linejoin="round"/>',
             icon(kind, a + pad, ink), T(a + pad + 22, CY + dy, txt, f, sz, ink)]
        if kind == "branch":
            cx_ = a + pad + 22 + W(f, txt, sz) + 8
            g.append(f'<path d="M{cx_:.1f},{CY + 0.5}l3,3.2 6-6.6" stroke="{LIME}" stroke-width="1.8" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')
        prompt.append("".join(g))

    # ------------------------------------------------------ typed phrases
    size = 21
    xp = xe + 18
    widths = [W("m", p, size) for p in phrases]
    maxw = max(widths)
    D = 4.6
    TT = D * len(phrases)
    css = [".cr{animation:cr 1s steps(1) infinite}@keyframes cr{0%,50%{opacity:1}51%,100%{opacity:0}}",
           ".lv{animation:lv 1.4s ease-in-out infinite alternate}@keyframes lv{from{opacity:.3}to{opacity:1}}",
           ".sw{animation:sw 9s linear infinite}@keyframes sw{0%{transform:translateX(0)}45%,100%{transform:translateX(1720px)}}"]
    groups, marks = [], []
    n_x = 1096
    for i, (p, w) in enumerate(zip(phrases, widths)):
        n = len(p)
        s = i * D
        t_type = min(2.3, n * 0.055)
        p0, p1 = pct(s, TT), pct(s + t_type, TT)
        p2, p3 = pct(s + D - 0.95, TT), pct(s + D - 0.35, TT)
        pe = s + D
        if i == 0:
            vis = f"0%,{pct(pe - 0.01, TT)}%{{opacity:1}}{pct(pe, TT)}%,100%{{opacity:0}}"
        elif i == len(phrases) - 1:
            vis = f"0%,{pct(s - 0.01, TT)}%{{opacity:0}}{p0}%,99.99%{{opacity:1}}100%{{opacity:0}}"
        else:
            vis = (f"0%,{pct(s - 0.01, TT)}%{{opacity:0}}{p0}%,{pct(pe - 0.01, TT)}%{{opacity:1}}"
                   f"{pct(pe, TT)}%,100%{{opacity:0}}")
        start = "0%" if i == 0 else f"0%,{p0}%"
        css.append(f"@keyframes v{i}{{{vis}}}.v{i}{{animation:v{i} {TT}s linear infinite}}")
        css.append(f"@keyframes c{i}{{{start}{{transform:translateX(0);animation-timing-function:steps({n},end)}}"
                   f"{p1}%,{p2}%{{transform:translateX({w:.2f}px);animation-timing-function:steps({n},end)}}"
                   f"{p3}%,100%{{transform:translateX(0)}}}}.c{i}{{animation:c{i} {TT}s linear infinite}}")
        groups.append(f'<g class="v{i}">{T(xp, CY + 7.5, p, "m", size, INK)}'
                      f'<g class="c{i}"><rect x="{xp - 1:.1f}" y="{CY - 22}" width="{maxw + 70:.1f}" height="44" fill="url(#tbg)"/>'
                      f'<rect x="{xp + 1:.1f}" y="{CY - 12}" width="11" height="23" rx="1.5" fill="{CYAN}" '
                      f'class="cr" filter="url(#glo)"/></g></g>')
        dx = 1170 - (len(phrases) - 1 - i) * 13
        marks.append(f'<g class="v{i}">{T(n_x - W("m", "/ 05", 12) - 6, CY + 4.5, f"{i + 1:02d}", "m", 12, INK, anchor="end")}'
                     f'<rect x="{dx - 7}" y="{CY - 3}" width="14" height="6" rx="3" fill="{CYAN}"/></g>')
    # Reduced motion: BASE_CSS stops every animation, so pin line one fully typed
    # and hide the rest instead of leaving five stacked cursors and no words.
    css.append("@media (prefers-reduced-motion:reduce){"
               + ",".join(f".v{i}" for i in range(1, len(phrases)))
               + f"{{opacity:0}}.c0{{transform:translateX({widths[0]:.2f}px)}}.cr{{opacity:1}}}}")
    dots = "".join(f'<circle cx="{1170 - k * 13}" cy="{CY}" r="2.6" fill="#343A74"/>'
                   for k in range(len(phrases)))

    defs = f"""<linearGradient id="tbg" x1="0" y1="0" x2="0" y2="{HT}" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#110E36"/><stop offset="1" stop-color="#090721"/></linearGradient>
<linearGradient id="tst" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{MAGENTA}"/></linearGradient>
<linearGradient id="pl1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF5BE0"/><stop offset="1" stop-color="#E01DBD"/></linearGradient>
<linearGradient id="glr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9EF7FF" stop-opacity="0"/><stop offset=".5" stop-color="#9EF7FF" stop-opacity=".06"/><stop offset="1" stop-color="#9EF7FF" stop-opacity="0"/></linearGradient>
<filter id="glo" x="-150%" y="-60%" width="400%" height="220%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="win"><rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="16"/></clipPath>"""
    body = f"""
<g clip-path="url(#win)">
<rect width="{WD}" height="{HT}" fill="url(#tbg)"/>
{''.join(title)}
{''.join(prompt)}
{''.join(groups)}
{dots}{''.join(marks)}
{T(n_x, CY + 4.5, "/ 05", "m", 12, DIM, anchor="end")}
<g class="sw"><rect x="-260" y="{TB}" width="220" height="{HT - TB}" fill="url(#glr)" transform="skewX(-18)"/></g>
</g>
<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="16" stroke="url(#tst)" stroke-opacity=".75" stroke-width="1.5"/>
"""
    return doc(WD, HT, "Typing terminal",
               "A terminal window with a powerline prompt (aniket · ~/portfolio · main) typing, one line at a time: "
               + " · ".join(phrases), ["m", "sb"], "".join(css), body, defs)


# ====================================================================== headers
SECTIONS = [
    ("01", "IDENTITY SCAN", "// about the human behind the hologram", CYAN, "identity"),
    ("02", "CAREER ROUTE", "// experience and education on one transit map", MAGENTA, "career"),
    ("03", "SKILL MATRIX", "// modules installed in this unit", VIOLET, "skills"),
    ("04", "PROJECT CITY", "// featured builds · tap a card to launch it", AMBER, "projects"),
    ("05", "ARCADE DISTRICT", "// 3D storybooks and mini learning games", LIME, "arcade"),
    ("06", "TELEMETRY", "// live signal from my github", CYAN, "telemetry"),
    ("07", "COMMS LINK", "// open a channel · let's build the future", MAGENTA, "comms"),
]


def header(num, title, sub, acc):
    WD, HT = 1200, 96
    tsize, tls = 30, 4
    tw = W("o7", title, tsize, tls)
    lx0, lx1 = 112 + tw + 30, 1010
    ticks = "".join(f"M{x},46V50" for x in range(int(lx0) + 14, lx1 - 4, 22))
    bars = []
    for i in range(7):
        d = 0.55 + rnd.random() * 0.7
        bars.append(f'<rect x="{1046 + i * 16}" y="44" width="9" height="28" rx="2" fill="{acc}" class="eq" '
                    f'style="animation-duration:{d:.2f}s;animation-delay:-{rnd.random():.2f}s"/>')
    css = (".eq{transform-box:fill-box;transform-origin:50% 100%;animation:eq .8s ease-in-out infinite alternate}"
           "@keyframes eq{from{transform:scaleY(.22)}to{transform:scaleY(1)}}"
           f".pk{{animation:pk 3.4s linear infinite}}@keyframes pk{{0%{{transform:translateX(0);opacity:0}}"
           f"8%{{opacity:1}}92%{{opacity:1}}100%{{transform:translateX({lx1 - lx0:.0f}px);opacity:0}}}}"
           ".sw{animation:sw 6s ease-in-out infinite}@keyframes sw{0%{transform:translateX(-300px)}60%,100%{transform:translateX(1500px)}}"
           ".hb{animation:hb 2.2s ease-in-out infinite alternate}@keyframes hb{from{opacity:.35}to{opacity:1}}")
    defs = f"""<linearGradient id="hbg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#110C38"/><stop offset=".6" stop-color="#0B0A26"/><stop offset="1" stop-color="#0A0A22"/></linearGradient>
<linearGradient id="swg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity=".09"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{acc}" stop-opacity=".9"/><stop offset="1" stop-color="{acc}" stop-opacity=".1"/></linearGradient>
<clipPath id="hc"><rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="16"/></clipPath>"""
    body = f"""
<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="16" fill="url(#hbg)"/>
<g clip-path="url(#hc)"><g class="sw"><rect x="0" y="-10" width="170" height="120" fill="url(#swg)" transform="skewX(-22)"/></g></g>
<path d="M18,22 V74" stroke="{acc}" stroke-width="3" stroke-linecap="round"/>
<polygon points="{hex_points(66, 48, 29)}" fill="#120A35" stroke="{acc}" stroke-width="2"/>
<polygon points="{hex_points(66, 48, 22)}" stroke="{acc}" stroke-opacity=".35" stroke-width="1" class="hb"/>
{T(66, 55.5, num, "o7", 19, acc, anchor="middle")}
{T(112, 54, title, "o7", tsize, "none", ls=tls, extra=f'stroke="{acc}" stroke-opacity=".28" stroke-width="6" stroke-linejoin="round"')}
{T(112, 54, title, "o7", tsize, INK, ls=tls)}
{T(114, 79, sub, "m", 14, DIM, ls=1)}
<path d="M{lx0:.0f},43 H{lx1}" stroke="url(#ln)" stroke-width="1.5"/>
<path d="{ticks}" stroke="{acc}" stroke-opacity=".35"/>
<circle cx="{lx0:.0f}" cy="43" r="3.2" fill="{acc}" class="pk"/>
{T(1046, 34, "SIGNAL", "m", 10, DIM, ls=2)}
{''.join(bars)}
<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="16" stroke="{acc}" stroke-opacity=".5" stroke-width="1.5"/>
"""
    return doc(WD, HT, f"{num} · {title.title()}", sub.lstrip("/ "), ["o7", "m"], css, body, defs)


# ===================================================================== identity
def identity():
    WD, HT = 1200, 400
    # ---- holo ID card (left)
    cx, cy = 210, 148
    card = f"""
<path d="M54,30 H390 V346 L366,370 H30 V54 Z" fill="url(#cardG)" stroke="{CYAN}" stroke-opacity=".55" stroke-width="1.5"/>
<path d="M30,54 L54,30" stroke="{CYAN}" stroke-width="2"/>
{T(52, 58, "CITIZEN ID // NEON GRID", "m", 11, CYAN, ls=2, extra='opacity=".8"')}
<circle cx="{cx}" cy="{cy}" r="86" stroke="{CYAN}" stroke-opacity=".5" stroke-width="1.2" stroke-dasharray="3 7" class="spin"/>
<circle cx="{cx}" cy="{cy}" r="78" stroke="{MAGENTA}" stroke-opacity=".35" stroke-width="1" stroke-dasharray="40 14" class="spinR"/>
<polygon points="{hex_points(cx, cy, 66, 0)}" fill="url(#hexG)" stroke="url(#hexS)" stroke-width="2.2"/>
<g clip-path="url(#hexClip)">
  <path d="M{cx - 66},{cy} H{cx + 66} M{cx},{cy - 66} V{cy + 66}" stroke="{CYAN}" stroke-opacity=".08"/>
  <rect x="{cx - 70}" y="{cy - 70}" width="140" height="10" fill="url(#scanV)" class="scanY"/>
</g>
{T(cx, cy + 20, "AC", "o9", 58, "none", ls=2, anchor="middle", extra=f'stroke="{CYAN}" stroke-opacity=".3" stroke-width="7" stroke-linejoin="round"')}
{T(cx, cy + 20, "AC", "o9", 58, "url(#acG)", ls=2, anchor="middle")}
{T(cx, 266, "ANIKET CHAUHAN", "o7", 19, INK, ls=2, anchor="middle")}
{T(cx, 290, "UI/UX DESIGNER · DEVELOPER", "m", 12, CYAN, ls=2, anchor="middle")}
"""
    stats = [("2+", "YRS DESIGN"), ("17", "LIVE BUILDS"), ("25", "DESIGN STUDIES")]
    sx = [90, 210, 330]
    for (big, small), x in zip(stats, sx):
        card += T(x, 330, big, "o7", 20, MAGENTA, anchor="middle")
        card += T(x, 348, small, "m", 9.5, DIM, ls=1.5, anchor="middle")
    card += '<path d="M150,316 V350 M270,316 V350" stroke="#2A2F6A"/>'

    # ---- terminal (right)
    tx0, ty0, tx1, ty1 = 420, 30, 1170, 370
    size, lh = 15, 25
    lines = [
        ("cmd", "whoami"),
        ("out", "Aniket Chauhan — UI/UX Designer & Developer"),
        ("cmd", "cat job.txt"),
        ("out", "AI Content Designer @ ConveGenius.AI, Noida"),
        ("cmd", "ls ~/worlds"),
        ("out", "ui-ux/  front-end/  learning-games/  3d-storybooks/  ai-content/"),
        ("cmd", "cat motto.txt"),
        ("out", "\"I build digital experiences where design, technology"),
        ("out", " and storytelling become one.\""),
        ("cmd", "status --now"),
        ("live", "Designing + coding playable maths worlds for classrooms"),
    ]
    lx = tx0 + 28
    y = ty0 + 66
    TT = 26.0
    t = 0.6
    css = [".cr{animation:cr 1s steps(1) infinite}@keyframes cr{0%,50%{opacity:1}51%,100%{opacity:0}}",
           ".spin{transform-box:fill-box;transform-origin:center;animation:spin 24s linear infinite}"
           ".spinR{transform-box:fill-box;transform-origin:center;animation:spin 16s linear infinite reverse}"
           "@keyframes spin{to{transform:rotate(360deg)}}",
           ".scanY{animation:scanY 3.2s linear infinite}@keyframes scanY{from{transform:translateY(0)}to{transform:translateY(140px)}}",
           ".lv{animation:lv 1.2s ease-in-out infinite alternate}@keyframes lv{from{opacity:.35}to{opacity:1}}",
           f".tg{{animation:tg {TT}s linear infinite}}@keyframes tg{{0%,95%{{opacity:1}}97.5%,100%{{opacity:0}}}}"]
    rows, covers = [], []
    for i, (kind, txt) in enumerate(lines):
        if kind == "cmd":
            full = "$ " + txt
            rows.append(T(lx, y, "$", "m", size, "#FF7AE6") + T(lx + W("m", "$ ", size), y, txt, "m", size, INK))
            n = len(full)
            dur = n * 0.07
            tf = f"steps({n},end)"
        elif kind == "out":
            full = "  " + txt
            rows.append(T(lx, y, full, "m", size, "#9EF7FF"))
            dur = 0.45
            tf = "linear"
        else:
            full = "  ● " + txt
            dot_x = lx + W("m", "  ", size) + 5
            rows.append(f'<circle cx="{dot_x:.1f}" cy="{y - 5}" r="4.5" fill="{LIME}" class="lv"/>'
                        + T(lx + W("m", "    ", size), y, txt, "m", size, LIME))
            caret_x = lx + W("m", "    " + txt, size) + 5
            rows.append(f'<rect x="{caret_x:.1f}" y="{y - 13}" width="9" height="16" fill="{LIME}" class="cr"/>')
            dur = 0.5
            tf = "linear"
        width = (W("m", full, size) if kind != "live" else W("m", "    " + txt, size) + 18) + 10
        a, b = pct(t, TT), pct(t + dur, TT)
        css.append(f"@keyframes k{i}{{0%,{a}%{{transform:translateX(0);animation-timing-function:{tf}}}"
                   f"{b}%,100%{{transform:translateX({width:.1f}px)}}}}.k{i}{{animation:k{i} {TT}s linear infinite}}")
        covers.append(f'<rect x="{lx - 2}" y="{y - 18}" width="{tx1 - lx + 40}" height="{lh}" fill="#070A1C" class="k{i}"/>')
        t += dur + (0.35 if kind == "cmd" else 0.25)
        y += lh
    term = f"""
<rect x="{tx0}" y="{ty0}" width="{tx1 - tx0}" height="{ty1 - ty0}" rx="12" fill="#070A1C" stroke="#2A2F6A" stroke-width="1.5"/>
<path d="M{tx0 + 12},{ty0} H{tx1 - 12} A12,12 0 0 1 {tx1},{ty0 + 12} V{ty0 + 34} H{tx0} V{ty0 + 12} A12,12 0 0 1 {tx0 + 12},{ty0} Z" fill="#0E1230"/>
<circle cx="{tx0 + 22}" cy="{ty0 + 17}" r="5" fill="{MAGENTA}"/><circle cx="{tx0 + 40}" cy="{ty0 + 17}" r="5" fill="{AMBER}"/><circle cx="{tx0 + 58}" cy="{ty0 + 17}" r="5" fill="{CYAN}"/>
{T((tx0 + tx1) / 2, ty0 + 22, "aniket@portfolio: ~/profile", "m", 13, DIM, ls=1, anchor="middle")}
<g clip-path="url(#termClip)"><g class="tg">{''.join(rows)}{''.join(covers)}</g></g>
<rect x="{tx0}" y="{ty0}" width="{tx1 - tx0}" height="{ty1 - ty0}" rx="12" stroke="url(#termS)" stroke-width="1.5"/>
"""
    defs = f"""
<linearGradient id="cardG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#120D3A"/><stop offset="1" stop-color="#090720"/></linearGradient>
<radialGradient id="hexG" cx=".5" cy=".4" r=".7"><stop offset="0" stop-color="#2A1A6E"/><stop offset="1" stop-color="#0B0828"/></radialGradient>
<linearGradient id="hexS" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{MAGENTA}"/></linearGradient>
<linearGradient id="acG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#B9F6FF"/></linearGradient>
<linearGradient id="scanV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}" stop-opacity=".45"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient>
<linearGradient id="termS" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity=".7"/><stop offset=".5" stop-color="{VIOLET}" stop-opacity=".4"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity=".7"/></linearGradient>
<clipPath id="hexClip"><polygon points="{hex_points(cx, cy, 64, 0)}"/></clipPath>
<clipPath id="termClip"><rect x="{tx0 + 2}" y="{ty0 + 36}" width="{tx1 - tx0 - 4}" height="{ty1 - ty0 - 38}"/></clipPath>
"""
    body = f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" fill="{BG}"/>' \
           f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" fill="url(#gridP)"/>{card}{term}' \
           f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" stroke="#232A5C" stroke-width="1.5"/>'
    defs += ('<pattern id="gridP" width="40" height="40" patternUnits="userSpaceOnUse">'
             '<path d="M40,0 H0 V40" stroke="#1A1F4A" stroke-opacity=".7"/></pattern>')
    return doc(WD, HT, "Identity scan — Aniket Chauhan",
               "Holographic ID card (AC monogram, UI/UX Designer and Developer; 2+ years in design, 17 live builds, "
               "25 design studies) beside a terminal: whoami → Aniket Chauhan, UI/UX Designer & Developer; "
               "job → AI Content Designer @ ConveGenius.AI, Noida; motto → I build digital "
               "experiences where design, technology and storytelling become one; status → designing and coding "
               "playable maths worlds for classrooms.",
               ["o9", "o7", "m"], "".join(css), body, defs)


# ======================================================================= career
def career():
    WD, HT = 1200, 470
    LY, EY = 152, 374
    stations = [
        dict(x=200, date="JUN 2024 — APR 2025", role="GRAPHIC DESIGNER", org="CCIE HUB · DELHI",
             desc=["Social posts, stories & promos,", "content scheduling + tracking"]),
        dict(x=580, date="MAY 2025 — NOV 2025", role="GRAPHIC DESIGNER", org="CONVEGENIUS.AI · NOIDA",
             desc=["Social creatives, UI/UX designs", "and campaign graphics"]),
        dict(x=960, date="NOV 2025 — PRESENT", role="AI CONTENT DESIGNER", org="CONVEGENIUS.AI · NOIDA",
             desc=["UI/UX design + front-end builds", "for engaging learning experiences"], now=True),
    ]
    out = []
    # lines
    out.append(f'<path d="M60,{LY} H1040" stroke="{CYAN}" stroke-opacity=".18" stroke-width="12" stroke-linecap="round"/>')
    out.append(f'<path d="M60,{LY} H1040" stroke="{CYAN}" stroke-width="4" stroke-linecap="round"/>')
    out.append(f'<path d="M1052,{LY} H1140" stroke="{CYAN}" stroke-width="3" stroke-dasharray="6 8" class="flow"/>')
    out.append(f'<path d="M1140,{LY - 8} L1152,{LY} L1140,{LY + 8} Z" fill="{CYAN}"/>')
    out.append(T(1150, LY - 18, "NEXT STOP: THE FUTURE", "m", 11, CYAN, ls=1.5, anchor="end", extra='opacity=".85"'))
    out.append(f'<path d="M60,{EY} H1140" stroke="{MAGENTA}" stroke-opacity=".16" stroke-width="10" stroke-linecap="round"/>')
    out.append(f'<path d="M60,{EY} H1140" stroke="{MAGENTA}" stroke-width="3" stroke-linecap="round"/>')
    # interchange connector from station 1 to the knowledge line
    out.append(f'<path d="M200,{LY + 20} V{EY - 6}" stroke="#3B3F7A" stroke-width="2" stroke-dasharray="3 6"/>')
    out.append(f'<circle cx="200" cy="{EY}" r="6" fill="#0B0B2A" stroke="{MAGENTA}" stroke-width="2"/>')
    out.append(T(212, EY + 24, "INTERCHANGE", "m", 10, DIM, ls=2))
    for st in stations:
        x = st["x"]
        acc = LIME if st.get("now") else CYAN
        dw = W("m", st["date"], 13, 1.5) + 26
        out.append(f'<rect x="{x - dw / 2:.1f}" y="{LY - 62}" width="{dw:.1f}" height="26" rx="13" fill="#0F1236" '
                   f'stroke="{acc}" stroke-opacity=".7"/>')
        out.append(T(x, LY - 44.5, st["date"], "m", 13, acc, ls=1.5, anchor="middle"))
        if st.get("now"):
            out.append(T(x, LY - 76, "YOU ARE HERE", "m", 11, LIME, ls=2, anchor="middle", cls="blink"))
            out.append(f'<circle cx="{x}" cy="{LY}" r="26" stroke="{LIME}" stroke-width="1.2" stroke-dasharray="4 5" class="spin"/>')
        out.append(f'<circle cx="{x}" cy="{LY}" r="16" stroke="{acc}" stroke-width="2" class="ping"/>')
        out.append(f'<circle cx="{x}" cy="{LY}" r="15" fill="#0B0B2A" stroke="{acc}" stroke-width="3"/>')
        out.append(f'<circle cx="{x}" cy="{LY}" r="6" fill="{acc}"/>')
        out.append(T(x, LY + 50, st["role"], "o7", 18, INK, ls=2, anchor="middle"))
        out.append(T(x, LY + 75, st["org"], "sb", 17, acc, ls=1.5, anchor="middle"))
        for k, dl in enumerate(st["desc"]):
            out.append(T(x, LY + 102 + k * 22, dl, "s", 16.5, SOFT, anchor="middle"))
    # knowledge station
    ex = 600
    out.append(f'<circle cx="{ex}" cy="{EY}" r="16" stroke="{MAGENTA}" stroke-width="2" class="ping"/>')
    out.append(f'<circle cx="{ex}" cy="{EY}" r="14" fill="#0B0B2A" stroke="{MAGENTA}" stroke-width="3"/>')
    out.append(f'<path d="M{ex - 7},{EY - 1} L{ex},{EY - 5} L{ex + 7},{EY - 1} L{ex},{EY + 3} Z M{ex - 4},{EY + 1} V{EY + 5} '
               f'Q{ex},{EY + 8} {ex + 4},{EY + 5} V{EY + 1}" fill="{MAGENTA}"/>')
    edw = W("m", "AUG 2023 — SEP 2026", 13, 1.5) + 26
    out.append(f'<rect x="{ex - edw / 2:.1f}" y="{EY - 60}" width="{edw:.1f}" height="26" rx="13" fill="#1A0E30" '
               f'stroke="{MAGENTA}" stroke-opacity=".7"/>')
    out.append(T(ex, EY - 42.5, "AUG 2023 — SEP 2026", "m", 13, "#FF9CEB", ls=1.5, anchor="middle"))
    out.append(T(ex, EY + 44, "BA • ENGLISH LANGUAGE & LITERATURE", "o7", 16, INK, ls=1.5, anchor="middle"))
    out.append(T(ex, EY + 68, "DELHI UNIVERSITY", "sb", 17, "#FF9CEB", ls=2, anchor="middle"))
    # legend + status
    out.append(f'<path d="M40,36 H70" stroke="{CYAN}" stroke-width="4" stroke-linecap="round"/>')
    out.append(T(80, 40.5, "CAREER LINE", "m", 12, DIM, ls=2))
    out.append(f'<path d="M210,36 H240" stroke="{MAGENTA}" stroke-width="3" stroke-linecap="round"/>')
    out.append(T(250, 40.5, "KNOWLEDGE LINE", "m", 12, DIM, ls=2))
    out.append(f'<circle cx="{1160 - W("m", "LINE STATUS: RUNNING", 12, 1.5) - 14:.1f}" cy="36" r="4" fill="{LIME}" class="blink"/>')
    out.append(T(1160, 40.5, "LINE STATUS: RUNNING", "m", 12, DIM, ls=1.5, anchor="end"))
    # pods
    pod = (f'<g class="podA"><g transform="translate(60 {LY})"><rect x="-60" y="-2.5" width="44" height="5" fill="url(#podT)"/>'
           f'<rect x="-18" y="-7" width="34" height="14" rx="7" fill="#E6FDFF" stroke="{CYAN}" stroke-width="1.5"/>'
           f'<rect x="-10" y="-3" width="18" height="4" rx="2" fill="{CYAN}"/></g></g>')
    pod2 = (f'<g class="podB"><g transform="translate(60 {EY})"><rect x="-50" y="-2" width="36" height="4" fill="url(#podT2)"/>'
            f'<rect x="-14" y="-6" width="28" height="12" rx="6" fill="#FFE3F8" stroke="{MAGENTA}" stroke-width="1.4"/></g></g>')
    css = (".ping{transform-box:fill-box;transform-origin:center;animation:ping 2.4s ease-out infinite}"
           "@keyframes ping{from{transform:scale(1);opacity:.9}to{transform:scale(2.3);opacity:0}}"
           ".spin{transform-box:fill-box;transform-origin:center;animation:spin 10s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}"
           ".blink{animation:blink 1.2s steps(1) infinite}@keyframes blink{0%,55%{opacity:1}56%,100%{opacity:.2}}"
           ".flow{animation:flow 1s linear infinite}@keyframes flow{to{stroke-dashoffset:-14}}"
           ".podA{animation:podA 12s ease-in-out infinite}"
           "@keyframes podA{0%{transform:translateX(0)}12%,22%{transform:translateX(140px)}45%,55%{transform:translateX(520px)}"
           "78%,96%{transform:translateX(900px)}100%{transform:translateX(980px);opacity:0}}"
           ".podB{animation:podB 16s linear infinite}@keyframes podB{from{transform:translateX(-80px)}to{transform:translateX(1180px)}}")
    defs = f"""<pattern id="gridP" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40,0 H0 V40" stroke="#1A1F4A" stroke-opacity=".7"/></pattern>
<linearGradient id="podT" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset="1" stop-color="{CYAN}" stop-opacity=".8"/></linearGradient>
<linearGradient id="podT2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{MAGENTA}" stop-opacity="0"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity=".8"/></linearGradient>"""
    body = (f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" fill="{BG}"/>'
            f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" fill="url(#gridP)"/>'
            + "\n".join(out) + pod + pod2 +
            f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" stroke="#232A5C" stroke-width="1.5"/>')
    return doc(WD, HT, "Career route — transit map",
               "Career line: Graphic Designer at CCIE Hub, Delhi (Jun 2024 – Apr 2025); Graphic Designer at "
               "ConveGenius.AI, Noida (May 2025 – Nov 2025); AI Content Designer (UI/UX) at ConveGenius.AI, Noida "
               "(Nov 2025 – present). Knowledge line: BA English Language & Literature, Delhi University "
               "(Aug 2023 – Sep 2026).",
               ["o7", "m", "s", "sb"], css, body, defs)


# ======================================================================= skills
def icon(kind, acc):
    if kind == "pen":
        return (f'<path d="M0,-15 L10,3 L0,15 L-10,3 Z" stroke="{acc}" stroke-width="2" stroke-linejoin="round"/>'
                f'<circle cx="0" cy="2" r="3" fill="{acc}"/><path d="M0,-15 V-1" stroke="{acc}" stroke-width="1.5"/>')
    if kind == "spark":
        return (f'<path d="M0,-15 Q2.5,-2.5 15,0 Q2.5,2.5 0,15 Q-2.5,2.5 -15,0 Q-2.5,-2.5 0,-15 Z" stroke="{acc}" '
                f'stroke-width="2" stroke-linejoin="round"/><circle cx="10" cy="-10" r="2" fill="{acc}"/>')
    if kind == "code":
        return (f'<path d="M-6,-10 L-15,0 L-6,10 M6,-10 L15,0 L6,10 M3,-13 L-3,13" stroke="{acc}" stroke-width="2.4" '
                f'stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<rect x="-16" y="-9" width="32" height="18" rx="9" stroke="{acc}" stroke-width="2"/>'
            f'<path d="M-9,0 H-3 M-6,-3 V3" stroke="{acc}" stroke-width="2" stroke-linecap="round"/>'
            f'<circle cx="6" cy="-1.5" r="2" fill="{acc}"/><circle cx="10" cy="2.5" r="2" fill="{acc}"/>')


def skills():
    WD, HT = 1200, 496
    mods = [
        ("MOD-01", "DESIGN", CYAN, "pen",
         ["UI/UX Design", "Graphic Design", "Design Thinking", "Visual Storytelling", "Brand Communication"]),
        ("MOD-02", "CODE", VIOLET, "code",
         ["Web Development", "HTML · CSS · JavaScript", "TypeScript & React", "HTML Game Creation", "Real-time 3D on the Web"]),
        ("MOD-03", "AI CONTENT", MAGENTA, "spark",
         ["AI Content Design", "AI-assisted Visuals", "Social Media Creatives", "Campaign Graphics", "Content Creation"]),
        ("MOD-04", "AI & GAMES", AMBER, "pad",
         ["AI Game Development", "Game Development", "Learning Game Design", "Voice-over & Localisation"]),
    ]
    out = []
    mw, gap, x0, y0, mh = 270, 20, 30, 34, 322
    css = [".seg{animation:seg 2.8s steps(1) infinite}@keyframes seg{0%{opacity:.18}10%,100%{opacity:1}}",
           ".hb{animation:hb 2.4s ease-in-out infinite alternate}@keyframes hb{from{opacity:.4}to{opacity:1}}",
           ".sw{animation:sw 7s ease-in-out infinite}@keyframes sw{0%{transform:translateX(-300px)}55%,100%{transform:translateX(1500px)}}"]
    for i, (code, title, acc, ic, items) in enumerate(mods):
        x = x0 + i * (mw + gap)
        y = y0
        c = 18
        out.append(f'<path d="M{x + c},{y} H{x + mw} V{y + mh - c} L{x + mw - c},{y + mh} H{x} V{y + c} Z" '
                   f'fill="url(#modG)" stroke="{acc}" stroke-opacity=".6" stroke-width="1.5"/>')
        out.append(f'<path d="M{x},{y + c} L{x + c},{y}" stroke="{acc}" stroke-width="2.2"/>')
        out.append(f'<polygon points="{hex_points(x + 44, y + 50, 25)}" fill="#120A35" stroke="{acc}" stroke-width="1.8"/>')
        out.append(f'<g transform="translate({x + 44} {y + 50})" class="hb">{icon(ic, acc)}</g>')
        out.append(T(x + 80, y + 40, code, "m", 11, acc, ls=2))
        out.append(T(x + 80, y + 64, title, "o7", 19, INK, ls=2))
        out.append(f'<path d="M{x + 20},{y + 92} H{x + mw - 20}" stroke="url(#div{i})" stroke-width="1.5"/>')
        for k, it in enumerate(items):
            yy = y + 126 + k * 33
            out.append(f'<path d="M{x + 24},{yy - 10} l7,4.5 l-7,4.5 Z" fill="{acc}"/>')
            out.append(T(x + 40, yy, it, "s", 18, "#D6DEFF"))
        # power meter
        for s in range(10):
            sx = x + 22 + s * 17
            out.append(f'<rect x="{sx}" y="{y + mh - 38}" width="13" height="8" rx="1.5" fill="{acc}" class="seg" '
                       f'style="animation-delay:{s * 0.12 + i * 0.3:.2f}s"/>')
        out.append(T(x + mw - 22, y + mh - 30, "ONLINE", "m", 11, acc, ls=2, anchor="end"))
    # toolchain chips
    tools = ["THREE.JS", "REACT THREE FIBER", "GSAP", "FRAMER MOTION", "LENIS", "CANVAS", "SVG", "CSS 3D",
             "WEB AUDIO", "PWA", "PLAYWRIGHT", "VITEST", "FASTIFY", "FFMPEG", "CLAUDE CODE", "CLAUDE API", "CHATGPT"]
    cols = [CYAN, MAGENTA, VIOLET, AMBER, LIME]
    ty = y0 + mh + 32
    out.append(T(x0, ty + 18, "TOOLCHAIN", "o7", 15, INK, ls=3))
    out.append(T(x0, ty + 40, "// also in the kit", "m", 11, DIM, ls=1))
    cx, cy = 200, ty
    for j, tl in enumerate(tools):
        w = W("m", tl, 12.5, 1.5) + 26
        if cx + w > WD - 30:
            cx, cy = 200, cy + 40
        col = cols[j % len(cols)]
        out.append(f'<rect x="{cx:.1f}" y="{cy}" width="{w:.1f}" height="28" rx="14" fill="#0F1236" stroke="{col}" stroke-opacity=".55"/>')
        out.append(T(cx + 13, cy + 18.5, tl, "m", 12.5, "#D6DEFF", ls=1.5))
        cx += w + 10
    defs = (f'<pattern id="gridP" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40,0 H0 V40" stroke="#1A1F4A" stroke-opacity=".7"/></pattern>'
            f'<linearGradient id="modG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#140E40"/><stop offset="1" stop-color="#0A0824"/></linearGradient>'
            f'<linearGradient id="swg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity=".06"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="pc"><rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20"/></clipPath>')
    for i, m in enumerate(mods):
        defs += (f'<linearGradient id="div{i}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{m[2]}"/>'
                 f'<stop offset="1" stop-color="{m[2]}" stop-opacity="0"/></linearGradient>')
    body = (f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" fill="{BG}"/>'
            f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" fill="url(#gridP)"/>'
            + "\n".join(out) +
            f'<g clip-path="url(#pc)"><g class="sw"><rect x="0" y="-20" width="220" height="540" fill="url(#swg)" transform="skewX(-18)"/></g></g>'
            f'<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" stroke="#232A5C" stroke-width="1.5"/>')
    alt = "; ".join(f"{m[1].title()}: {', '.join(m[4])}" for m in mods) + ". Toolchain: " + ", ".join(tools) + "."
    return doc(WD, HT, "Skill matrix", alt, ["o7", "m", "s"], "".join(css), body, defs)


# ======================================================================== cards
import base64 as _b64
import os as _os

ART_DIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "art")


def art_uri(name):
    """Embed a prepared game-art file (assets/source/art/*.webp) as a data URI.
    GitHub renders the SVG inside an <img> sandbox that fetches nothing external."""
    with open(_os.path.join(ART_DIR, name), "rb") as fh:
        return "data:image/webp;base64," + _b64.b64encode(fh.read()).decode("ascii")


# banner: real art from the game (assets/source/art, 800x400 = 2:1)
# sprites: (art file, x, y, width, height, float class) -- pop-outs that break the frame
CARDS = [
    dict(slug="crown-quest", title="ZIPPY'S CROWN QUEST", sector="SECTOR 01 // MATH QUEST", acc=AMBER,
         banner="crown-quest-banner.webp",
         desc="Class 8 linear equations as a 25-minute voiced adventure: Zippy the monkey swaps crowns for gold bars on a balance. Tip it and Grumble wakes up.",
         chips=["JAVASCRIPT", "WEB AUDIO", "PWA"], live=True, url="https://crown-quest-ten.vercel.app"),
    dict(slug="cannon-quest", title="CANNON QUEST", sector="SECTOR 02 // ALGEBRA ARCADE", acc=ORANGE,
         banner="cannon-quest-banner.webp",
         sprites=[("cannon-quest-orb1.webp", 456, 262, 64, 65, "fa"), ("cannon-quest-orb2.webp", 530, 234, 50, 50, "fb")],
         desc="Load operation orbs into the cannon, fire, and free x from its cage. A drag-to-load 2D algebra game with a guided tutorial and full localisation.",
         chips=["JAVASCRIPT", "GSAP", "I18N"], live=True, url="https://cannon-quest.vercel.app"),
    dict(slug="uttarakhand-riders", title="UTTARAKHAND RIDERS", sector="SECTOR 03 // 3D RACING", acc=CYAN,
         banner="uttarakhand-riders-banner.webp",
         sprites=[("uttarakhand-riders-sprite.webp", 384, 202, 186, 121, "fa")], streaks=True,
         desc="A 3D superbike race through the hills: from Ramnagar past Corbett and the Kosi river up to Ranikhet. Three riders, phone controls and voice chat.",
         chips=["THREE.JS", "NODE.JS", "PWA"], live=True, url="https://bike-game-gamma.vercel.app"),
    dict(slug="the-best-deal", title="THE BEST DEAL", sector="SECTOR 04 // PROFIT & DISCOUNT", acc=MAGENTA,
         banner="the-best-deal-banner.webp",
         sprites=[("the-best-deal-sprite.webp", 430, 234, 150, 93, "fa")],
         desc="A voiced story game about discounts: Amit buys a book, picks sneakers, then hunts the mall for the best deals for Rohan's party. Playable in six languages.",
         chips=["JAVASCRIPT", "I18N", "VOICE-OVER"], live=True, url="https://profit-and-discount-game.vercel.app"),
    dict(slug="distance-formula", title="DISTANCE FORMULA", sector="SECTOR 05 // GEOMETRY", acc=LIME,
         banner="distance-formula-banner.webp",
         desc="A whole maths lesson as one game, led by Swifty the voiced bird: plot the points, find the gaps, close the right triangle and let Pythagoras finish it.",
         chips=["JAVASCRIPT", "SVG", "WEB AUDIO"], live=True, url="https://distance-formula.vercel.app"),
    dict(slug="power-up-bots", title="POWER UP, BOTS!", sector="SECTOR 06 // 3D STORYBOOK", acc=VIOLET,
         banner="power-up-bots-banner.webp", art_note="Banner: the book's real cover.",
         sprites=[("power-up-bots-bot2.webp", 398, 238, 80, 82, "fb"), ("power-up-bots-bot1.webp", 468, 212, 118, 108, "fa")],
         desc="A maths picture book that opens like a real hardcover. After the story, rotate a laser and cut energy blocks into two equal halves to charge the bots.",
         chips=["CSS 3D", "JAVASCRIPT", "VOICE-OVER"], live=True, url="https://powerupp-bots.vercel.app"),
    dict(slug="fish-rescue", title="THE GREAT FISH RESCUE", sector="SECTOR 07 // 3D STORYBOOK", acc=AMBER,
         banner="fish-rescue-banner.webp", art_note="Banner: the book's real cover.",
         sprites=[("fish-rescue-fish2.webp", 404, 262, 84, 57, "fb"), ("fish-rescue-fish1.webp", 474, 236, 110, 66, "fa")],
         desc="A storybook set in the desert: find four hidden ponds, then steer each fish into the stream of its colour and count them, in two games bound into the book.",
         chips=["CSS 3D", "JAVASCRIPT", "WEB AUDIO"], live=True, url="https://fishrescue.vercel.app"),
    dict(slug="byte-saves-the-day", title="BYTE SAVES THE DAY", sector="SECTOR 08 // 3D STORYBOOK", acc=CYAN,
         banner="byte-saves-the-day-banner.webp", art_note="Banner: the book's real cover.",
         sprites=[("byte-saves-the-day-bunny.webp", 466, 206, 112, 118, "fa")],
         desc="A hardcover storybook with real thickness: Byte's Energy Hunt and Right & Left open inside its pages, then turn the page themselves when you finish.",
         chips=["CSS 3D", "JAVASCRIPT", "WEB AUDIO"], live=True, url="https://byte-save.vercel.app"),
]


def card(c):
    WD, HT = 600, 480
    a = c["acc"]
    BX, BY, BW_, BH_ = 12, 12, 576, 288
    frame = "M24,2 H598 V456 L574,478 H2 V26 Z"
    out = [f'<path d="{frame}" fill="url(#cg)"/>']
    # ---- banner: the game's own art, with scanlines, shades and a passing glare
    ban = []
    ban.append(f'<image href="{art_uri(c["banner"])}" x="{BX}" y="{BY}" width="{BW_}" height="{BH_}" preserveAspectRatio="xMidYMid slice"/>')
    ban.append(f'<rect x="{BX}" y="{BY}" width="{BW_}" height="{BH_}" fill="url(#scan)"/>')
    ban.append(f'<rect x="{BX}" y="{BY}" width="{BW_}" height="80" fill="url(#topShade)"/>')
    ban.append(f'<rect x="{BX}" y="{BY + BH_ - 96}" width="{BW_}" height="96" fill="url(#botFade)"/>')
    ban.append('<g class="glare"><rect x="0" y="0" width="110" height="330" fill="url(#glareG)" transform="skewX(-18)"/></g>')
    out.append(f'<g clip-path="url(#bclip)">{"".join(ban)}</g>')
    out.append(f'<path d="M{BX + 12},{BY + BH_ - 30} V{BY + BH_ - 12} H{BX + 30} M{BX + BW_ - 30},{BY + BH_ - 12} '
               f'H{BX + BW_ - 12} V{BY + BH_ - 30}" stroke="{a}" stroke-width="2" opacity=".9"/>')
    out.append(f'<path d="M{BX + 44},{BY + BH_} H{BX + BW_ - 44}" stroke="url(#hair)" stroke-width="1.4"/>')
    # ---- pop-out sprites: real game pieces that break out of the frame
    for f, x, y, w, h, cls in c.get("sprites", []):
        out.append(f'<ellipse cx="{x + w / 2:.1f}" cy="{y + h - 3:.1f}" rx="{w * .42:.1f}" ry="7" fill="url(#pop)"/>')
        if c.get("streaks"):
            for k, (dy, ln) in enumerate([(.38, 46), (.55, 64), (.72, 38)]):
                sy = y + h * dy
                out.append(f'<path d="M{x + w - 6:.1f},{sy:.1f} h{ln}" stroke="{a}" stroke-width="2.4" stroke-linecap="round" '
                           f'class="stk" style="animation-delay:-{k * .23:.2f}s"/>')
        out.append(f'<g class="{cls}"><image href="{art_uri(f)}" x="{x}" y="{y}" width="{w}" height="{h}"/></g>')
    # ---- chips over the art
    lab, col = ("LIVE", LIME) if c["live"] else ("SOURCE", AMBER)
    st = W("m", lab, 11, 2) + 34
    out.append(f'<rect x="{574 - st:.1f}" y="24" width="{st:.1f}" height="26" rx="13" fill="#07061A" fill-opacity=".82" stroke="{col}" stroke-opacity=".85"/>')
    out.append(f'<circle cx="{574 - st + 14:.1f}" cy="37" r="4" fill="{col}" class="pulse"/>')
    out.append(T(574 - st + 24, 41.5, lab, "m", 11, col, ls=2))
    # ---- body
    out.append(T(30, 328, c["sector"], "m", 12, a, ls=2))
    y = 357
    for ln in wrap(c["title"], "o7", 25, 540, 1.5):
        out.append(T(30, y, ln, "o7", 25, INK, ls=1.5))
        y += 32
    y -= 8
    for ln in wrap(c["desc"], "s", 16.5, 540)[:3]:
        out.append(T(30, y, ln, "s", 16.5, SOFT))
        y += 21
    assert y - 21 <= 423, (c["slug"], y)
    cx = 30
    for ch in c["chips"]:
        w = W("m", ch, 11, 1.2) + 20
        out.append(f'<rect x="{cx:.1f}" y="430" width="{w:.1f}" height="24" rx="12" fill="#0F1236" stroke="{a}" stroke-opacity=".6"/>')
        out.append(T(cx + 10, 446, ch, "m", 11, "#D6DEFF", ls=1.2))
        cx += w + 8
    cta = "LAUNCH" if c["live"] else "VIEW CODE"
    out.append(T(554, 447, cta, "m", 12, a, ls=2.5, anchor="end"))
    if c["live"]:
        out.append(f'<path d="M560,437 l9,5.5 l-9,5.5 Z" fill="{a}" class="nudge"/>')
    else:
        out.append(f'<path d="M563,437 l-4,5.5 l4,5.5 M568,437 l4,5.5 l-4,5.5" stroke="{a}" stroke-width="1.6" class="nudge"/>')
    out.append(f'<path d="{frame}" stroke="{a}" stroke-opacity=".75" stroke-width="1.6"/>')
    out.append(f'<path d="M2,26 L24,2 M574,478 L598,456" stroke="{a}" stroke-width="3"/>')
    css = (".fa{animation:fa 3.6s ease-in-out infinite alternate}@keyframes fa{from{transform:translateY(-5px)}to{transform:translateY(3px)}}"
           ".stk{animation:stk .7s linear infinite}@keyframes stk{from{transform:translateX(-6px);opacity:1}to{transform:translateX(16px);opacity:0}}"
           ".fb{animation:fb 2.9s ease-in-out infinite alternate}@keyframes fb{from{transform:translateY(4px)}to{transform:translateY(-6px)}}"
           ".glare{animation:glare 7s ease-in-out infinite}@keyframes glare{0%{transform:translateX(-170px)}55%,100%{transform:translateX(760px)}}"
           ".pulse{animation:pulse 1.3s ease-in-out infinite alternate}@keyframes pulse{from{opacity:.3}to{opacity:1}}"
           ".nudge{animation:nudge 1.6s ease-in-out infinite}@keyframes nudge{0%,100%{transform:translateX(0)}50%{transform:translateX(4px)}}")
    defs = f"""
<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#110C38"/><stop offset="1" stop-color="#08071E"/></linearGradient>
<pattern id="gridC" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24,0 H0 V24" stroke="#1A1F4A" stroke-opacity=".55"/></pattern>
<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#000000" fill-opacity=".14"/></pattern>
<clipPath id="bclip"><path d="M{BX + 22},{BY} H{BX + BW_} V{BY + BH_} H{BX} V{BY + 22} Z"/></clipPath>
<linearGradient id="topShade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05031A" stop-opacity=".45"/><stop offset="1" stop-color="#05031A" stop-opacity="0"/></linearGradient>
<linearGradient id="botFade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0C0A2A" stop-opacity="0"/><stop offset=".7" stop-color="#0C0A2A" stop-opacity=".75"/><stop offset="1" stop-color="#0C0A2A"/></linearGradient>
<linearGradient id="glareG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity=".16"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<linearGradient id="hair" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{a}" stop-opacity="0"/><stop offset=".5" stop-color="{a}"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></linearGradient>
<radialGradient id="pop"><stop offset="0" stop-color="{a}" stop-opacity=".55"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient>
"""
    title = c["title"].title().replace("'S", "'s")
    status = "Live demo" if c["live"] else "Source code"
    art = c.get("art_note", "Banner: the game's real title screen.")
    return doc(WD, HT, f"{title} — project card", f'{c["desc"]} Built with {", ".join(c["chips"]).title()}. {status}. {art}',
               ["o7", "m", "s"], css, "\n".join(out), defs)


# ====================================================================== buttons
# (slug, label, plain-language line, accent, light tint of the accent, icon)
BUTTONS = [
    ("btn-linkedin", "LinkedIn", "Let's connect", CYAN, "#9EF7FF", "in"),
    ("btn-portfolio", "Portfolio", "See my 3D work", MAGENTA, "#FFB3F0", "planet"),
    ("btn-email", "Email", "Say hello", AMBER, "#FFE3A6", "mail"),
]


def button(slug, label, sub, acc, tint, ic):
    """A calm, solid button: filled icon tile, big readable label, and an
    offset accent block behind the card instead of glows and scan sweeps."""
    WD, HT = 300, 76
    ink = "#0B0A24"
    if ic == "in":
        glyph = T(0, 8.5, "in", "sb", 26, ink, anchor="middle")
    elif ic == "planet":
        # back half of the ring, planet (with a gap cut in the tile colour), then the front half on top
        front = "M-15.5,0 A15.5,5 0 0 0 15.5,0"
        glyph = (f'<g transform="rotate(-20)"><ellipse rx="15.5" ry="5" stroke="{ink}" stroke-width="2.2"/>'
                 f'<circle r="8" fill="{ink}" stroke="{acc}" stroke-width="2.5"/>'
                 f'<path d="{front}" stroke="{acc}" stroke-width="6"/>'
                 f'<path d="{front}" stroke="{ink}" stroke-width="2.2" stroke-linecap="round"/></g>'
                 f'<circle cx="11" cy="-10" r="2.2" fill="{ink}"/>')
    else:
        glyph = (f'<rect x="-12" y="-8.5" width="24" height="17" rx="3" stroke="{ink}" stroke-width="2.4"/>'
                 f'<path d="M-11,-6.5 L0,2 L11,-6.5" stroke="{ink}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
    body = f"""
<rect x="7.5" y="8.5" width="290" height="65" rx="14" fill="{acc}" fill-opacity=".9"/>
<rect x="1.5" y="1.5" width="290" height="65" rx="14" fill="#100E34" stroke="{acc}" stroke-width="2"/>
<rect x="15" y="13" width="42" height="42" rx="11" fill="{acc}"/>
<g transform="translate(36 34)">{glyph}</g>
{T(72, 32, label, "sb", 26, INK)}
{T(72, 53, sub, "s", 17, tint)}
<circle cx="260" cy="34" r="16" fill="{acc}" fill-opacity=".14"/>
<path d="M253,34 H266 M261,28.5 L266.5,34 L261,39.5" stroke="{acc}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" class="nd"/>
"""
    css = ".nd{animation:nd 1.6s ease-in-out infinite}@keyframes nd{0%,100%{transform:translateX(0)}50%{transform:translateX(3px)}}"
    keys = ["sb", "s"]
    return doc(WD, HT, f"{label} button", f"{label} — {sub}", keys, css, body)


# ======================================================================= footer
def footer():
    WD, HT = 1200, 250
    r2 = random.Random(77)
    stars = "".join(f'<circle cx="{r2.uniform(10, 1190):.0f}" cy="{r2.uniform(8, 120):.0f}" r="{r2.choice([.6, .8, 1.1])}" '
                    f'fill="#FFFFFF" opacity="{r2.uniform(.25, .8):.2f}"/>' for _ in range(60))
    # skyline silhouette
    parts, x = [], -6
    while x < WD + 6:
        w = r2.randint(18, 44)
        h = r2.randint(26, 96)
        top = 196 - h
        if r2.random() < .2:
            parts.append(f"M{x},196V{top}H{x + w}V196Z M{x + w / 2 - 1.2:.1f},{top}V{top - r2.randint(10, 26)}H{x + w / 2 + 1.2:.1f}V{top}Z")
        else:
            parts.append(f"M{x},196V{top}H{x + w}V196Z")
        x += w + r2.randint(-4, 3)
    d = "".join(parts)
    tile = "".join(f'<rect x="{cx_ * 9 + 3}" y="{cy * 11 + 3}" width="3" height="4" fill="{r2.choice([AMBER, "#9EF7FF", "#FFB3F0"])}" opacity=".75"/>'
                   for cy in range(4) for cx_ in range(5) if r2.random() < .28)
    lanes = [(184, .55, 1, 7.5, (0, 3.7)), (226, .9, -1, 6, (1.2, 4.2))]
    cars, css = [], []
    for li, (y, s, dirn, dur, delays) in enumerate(lanes):
        for dl in delays:
            sc = f"scale({s})" if dirn > 0 else f"scale({-s} {s})"
            cars.append(f'<g class="fl{li}" style="animation-delay:-{dl}s"><g transform="translate(0 {y}) {sc}"><use href="#{"fcA" if li == 0 else "fcB"}"/></g></g>')
        frm, to = (-200, WD + 200) if dirn > 0 else (WD + 200, -200)
        css.append(f"@keyframes fl{li}{{from{{transform:translateX({frm}px)}}to{{transform:translateX({to}px)}}}}.fl{li}{{animation:fl{li} {dur}s linear infinite}}")
    streaks = "".join(
        f'<rect x="0" y="{y}" width="{ln}" height="1.6" rx=".8" fill="url(#stk{i % 2})" class="st" '
        f'style="animation-duration:{du:.1f}s;animation-delay:-{dl:.1f}s"/>'
        for i, (y, ln, du, dl) in enumerate([(206, 140, 1.8, 0), (212, 90, 1.4, .7), (240, 200, 2.2, 1.1), (246, 120, 1.6, .3)]))
    css.append(".st{animation:st 2s linear infinite}@keyframes st{from{transform:translateX(-260px)}to{transform:translateX(1460px)}}"
               ".gl{animation:gl 3s ease-in-out infinite alternate}@keyframes gl{from{opacity:.75}to{opacity:1}}")
    body = f"""
<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" fill="url(#fbg)"/>
<g clip-path="url(#fc)">
{stars}
<ellipse cx="600" cy="196" rx="640" ry="70" fill="url(#fglow)"/>
<path d="{d}" fill="#1A0D44"/><path d="{d}" fill="url(#fwin)"/>
<rect x="0" y="196" width="{WD}" height="10" fill="#1E1250"/>
<path d="M0,196.5 H{WD}" stroke="{CYAN}" stroke-width="1.4"/>
<path d="M0,205.5 H{WD}" stroke="{MAGENTA}" stroke-opacity=".7" stroke-width="1"/>
{''.join(f'<rect x="{px}" y="206" width="8" height="44" fill="#140A36"/>' for px in range(70, WD, 160))}
{streaks}
{''.join(cars)}
</g>
{T(600, 62, "END OF TRANSMISSION", "o7", 26, "none", ls=7, anchor="middle", extra=f'stroke="{CYAN}" stroke-opacity=".3" stroke-width="7" stroke-linejoin="round"')}
{T(600, 62, "END OF TRANSMISSION", "o7", 26, INK, ls=7, anchor="middle", cls="gl")}
{T(600, 92, "DESIGNED × DEVELOPED WITH CURIOSITY  ·  NEON GRID", "m", 13, "#FF9CEB", ls=2.5, anchor="middle")}
<rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20" stroke="url(#ffr)" stroke-width="1.6"/>
"""
    defs = f"""<linearGradient id="fbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05010E"/><stop offset=".6" stop-color="#1A0640"/><stop offset="1" stop-color="#070214"/></linearGradient>
<radialGradient id="fglow"><stop offset="0" stop-color="{MAGENTA}" stop-opacity=".35"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/></radialGradient>
<pattern id="fwin" width="45" height="44" patternUnits="userSpaceOnUse">{tile}</pattern>
<linearGradient id="stk0" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset="1" stop-color="{CYAN}"/></linearGradient>
<linearGradient id="stk1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{MAGENTA}" stop-opacity="0"/><stop offset="1" stop-color="{MAGENTA}"/></linearGradient>
<linearGradient id="ffr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity=".7"/><stop offset=".5" stop-color="{VIOLET}" stop-opacity=".5"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity=".7"/></linearGradient>
<clipPath id="fc"><rect x="1" y="1" width="{WD - 2}" height="{HT - 2}" rx="20"/></clipPath>
""" + car_symbol("fcA", neon=CYAN, tail=MAGENTA) + car_symbol("fcB", body_a="#FFE3F8", body_b="#B060B8", neon=MAGENTA, tail="#FF3B6B")
    return doc(WD, HT, "End of transmission",
               "Footer: a neon skyway at night with hover cars and light trails beneath the words "
               "End of Transmission — designed × developed with curiosity.",
               ["o7", "m"], "".join(css), body, defs)
