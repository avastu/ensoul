#!/usr/bin/env python3
"""ensoul render recipes — generate aligned artifacts by RUNNING, not eyeballing.

A model running ensoul should call these instead of hand-emitting fragile glyphs
or hand-counting a box's padding. Output is correct by construction and identical
across models. Import the functions, or run this file for a live demo:

    python3 render.py

Doctrine baked in:
  * width is measured in RENDER CELLS, not code points (see cells()).
  * ambiguous-width characters are flagged (see audit()); a closed box that
    contains them may drift across fonts — prefer open_frame() or a safe glyph.
"""
from __future__ import annotations
import math
import unicodedata as _u

# --- the measure: render cells, not code points -----------------------------

def char_cells(ch: str, ambiguous: int = 1) -> int:
    """Width of one character in terminal cells. `ambiguous` is how this
    terminal renders East-Asian 'A' glyphs (1 in most Western fonts, 2 in
    CJK-configured ones). Combining marks are 0; W/F are 2."""
    if _u.combining(ch):
        return 0
    eaw = _u.east_asian_width(ch)
    if eaw in ("W", "F"):
        return 2
    if eaw == "A":
        return ambiguous
    return 1

def cells(s: str, ambiguous: int = 1) -> int:
    return sum(char_cells(c, ambiguous) for c in s)

def audit(s: str) -> list[str]:
    """Ambiguous-width characters in s — the ones that can shove a right
    border off across fonts. Empty list == safe to close a box."""
    seen, out = set(), []
    for c in s:
        if c not in seen and _u.east_asian_width(c) == "A":
            seen.add(c); out.append(c)
    return out

# --- sparklines: a real series, in one line ---------------------------------

_BLOCKS = "▁▂▃▄▅▆▇█"  # 8 levels, reliably 1 cell

def spark_block(data, lo=None, hi=None) -> str:
    lo = min(data) if lo is None else lo
    hi = max(data) if hi is None else hi
    rng = (hi - lo) or 1
    return "".join(_BLOCKS[min(7, max(0, round((v - lo) / rng * 7)))] for v in data)

def spark_braille(data, lo=None, hi=None) -> str:
    """2 data points per cell, 4 vertical dots — double the horizontal density
    of a block sparkline. Reliably 1 cell wide."""
    lo = min(data) if lo is None else lo
    hi = max(data) if hi is None else hi
    rng = (hi - lo) or 1
    L = (0x40, 0x04, 0x02, 0x01)   # left column dots, bottom -> top
    R = (0x80, 0x20, 0x10, 0x08)   # right column dots, bottom -> top
    def col(v, bits):
        h = min(4, max(0, round((v - lo) / rng * 4)))
        c = 0
        for i in range(h):
            c |= bits[i]
        return c
    out = []
    for i in range(0, len(data), 2):
        c = col(data[i], L)
        if i + 1 < len(data):
            c |= col(data[i + 1], R)
        out.append(chr(0x2800 + c))
    return "".join(out)

# --- magnitude as ink -------------------------------------------------------

def hbar(frac: float, width: int = 24, fill: str = "█", track: str = "░") -> str:
    """A proportional bar: weight you can see, not just a number. (Note ░/▒/▓
    invert by light/dark theme; █ and the track are safe to read either way.)"""
    frac = max(0.0, min(1.0, frac))
    n = round(frac * width)
    return fill * n + track * (width - n)

# --- surface attunement -----------------------------------------------------

_DEFAULT_WIDTHS = {
    "plain": 72,
    "balanced": 68,
    "wild": 78,
}

def surface_width(dial: str = "balanced", surface_cols: int | None = None, breathing_room: int = 8) -> int:
    """Target artifact width for the current reading surface.

    If the surface is knowable (for example `tput cols` in a terminal), use it
    with breathing room. If not, fall back to conservative portable defaults.
    """
    if surface_cols:
        return max(32, surface_cols - breathing_room)
    return _DEFAULT_WIDTHS.get(dial, _DEFAULT_WIDTHS["balanced"])

def flow_row(
    label: str,
    path: str,
    qualifier: str | None = None,
    width: int | None = None,
    indent: int = 2,
    edge_margin: int = 8,
) -> str:
    """Render a flow row while keeping secondary detail away from the right edge.

    Primary path stays horizontal. If the qualifier would crowd the surface, it
    folds downward under the path instead of forcing a long line.
    """
    width = surface_width() if width is None else width
    pad = " " * indent
    base = f"{pad}{label}      {path}"
    if not qualifier:
        return base
    inline = f"{base} [{qualifier}]"
    if cells(inline) <= width - edge_margin:
        return inline
    child_indent = " " * (indent + cells(label) + 6)
    return "\n".join([base, f"{child_indent}{qualifier}"])

# --- frames -----------------------------------------------------------------

def open_frame(title: str, rows, indent: int = 2) -> str:
    """Forgiving form: a top rule + left-aligned rows, NO closing right border.
    Cannot drift — ship this when any row carries an ambiguous glyph."""
    pad = " " * indent
    body = [pad + r for r in rows]
    rule_w = max((cells(r) for r in body), default=0) + 1
    return "\n".join([pad + title, pad + "─" * rule_w, *body])

def measured_box(title: str, lines, indent: int = 2):
    """Closed ┌─┐ box, padded by render cells so the right border holds.
    Returns (text, warnings). If a line contains ambiguous-width chars the box
    MAY drift across fonts — the warning tells you to fix the glyph or use
    open_frame() instead."""
    warns = []
    for ln in [title, *lines]:
        bad = audit(ln)
        if bad:
            warns.append(f"ambiguous glyph(s) {''.join(bad)!r} in: {ln.strip()[:48]!r}")
    field = max([cells(title) + 2] + [cells(ln) for ln in lines]) + 2
    pad = " " * indent
    top = pad + "┌─" + title + " " + "─" * (field - cells(title) - 2) + "┐"
    bot = pad + "└" + "─" * field + "┘"
    body = [pad + "│" + ln + " " * (field - cells(ln)) + "│" for ln in lines]
    return "\n".join([top, *body, bot]), warns

# --- procedural beauty: a felt shape from real data -------------------------
# For the `wild` dial: one dominant GENERATED image, dense and exact where
# hand-typed art drifts or goes timid. These use block shading (`░ ▒ ▓ █`),
# which inverts by theme — tuned here for DARK terminals (more ink = heavier /
# deeper), so say so when you ship one. The facts belong in a caption beneath,
# not inside the image; a figurative image has no right border, so it can't drift.
# All are deterministic: same input → same picture (no randomness, no clock).

_SHADE = " ░▒▓█"

def _resample(series, width):
    """Linearly resample a (possibly short) series to `width` samples."""
    s = list(series)
    if len(s) == 1:
        return s * width
    out = []
    for x in range(width):
        t = x * (len(s) - 1) / (width - 1)
        i = int(t); f = t - i
        out.append(s[-1] if i >= len(s) - 1 else s[i] * (1 - f) + s[i + 1] * f)
    return out

def terrain(series, width=56, height=9, lo=None, hi=None):
    """Value-as-elevation landscape: a real series rendered as a filled, shaded
    profile — a wild image that is ALSO a truthful area chart (the surface IS the
    data). Deeper fill reads darker. Tuned for dark terminals."""
    samp = _resample(series, width)
    lo = min(samp) if lo is None else lo
    hi = max(samp) if hi is None else hi
    rng = (hi - lo) or 1.0
    elev = [1 + round((v - lo) / rng * (height - 1)) for v in samp]  # 1..height
    rows = []
    for r in range(height):                       # r=0 top … r=height-1 bottom
        line = "".join(
            " " if (depth := elev[x] - (height - r)) < 0 else _SHADE[min(4, 1 + depth)]
            for x in range(width)
        )
        rows.append(line.rstrip())
    return "\n".join(rows)

def wave(width=56, height=9, envelope="decay", amp=None, freqs=(0.55, 0.23)):
    """A shaded waveform band. envelope='decay' (turbulence → calm),
    'crescendo' (builds left → right), or 'steady'. Centered vertically;
    shaded by nearness to the line."""
    cy = (height - 1) / 2
    amp = (height / 2 - 0.5) if amp is None else amp
    rows = []
    for r in range(height):
        line = []
        for x in range(width):
            if envelope == "decay":
                a = amp * math.exp(-x / (width / 3.5))
            elif envelope == "crescendo":
                a = amp * (x / max(1, width - 1))
            else:
                a = amp
            w = a * sum(math.sin(x * f + i * 1.7) for i, f in enumerate(freqs)) / len(freqs)
            t = max(0.0, 1 - abs((r - cy) - w) / 2.4)
            line.append(_SHADE[min(4, int(t * len(_SHADE)))])
        rows.append("".join(line).rstrip())
    return "\n".join(rows)

def orb(radius=7, rays=12):
    """A luminous radial body: a bright core fading to an edge, with rays. Pure
    beauty (no data) — for when the felt point is presence, not a series."""
    W, H = int(radius * 4) + 1, int(radius * 2) + 1
    cx, cy = W / 2, H / 2
    ramp = " .·:░▒▓█"
    rows = []
    for y in range(H):
        line = []
        for x in range(W):
            d = math.hypot((x - cx) * 0.5, y - cy)
            if d < radius:
                line.append(ramp[min(len(ramp) - 1, int((1 - d / radius) * len(ramp)))])
            else:
                ch = " "
                if rays:
                    ang = math.atan2(y - cy, (x - cx) * 0.5)
                    for k in range(rays):
                        a = k * 2 * math.pi / rays
                        if abs(((ang - a + math.pi) % (2 * math.pi)) - math.pi) < 0.07 and radius < d < radius * 1.4:
                            ch = "·" if d > radius * 1.2 else ":"
                line.append(ch)
        rows.append("".join(line).rstrip())
    return "\n".join(rows)

def field(fn, width=56, height=12, ramp=_SHADE):
    """Shade an arbitrary scalar field. fn(nx, ny) -> 0..1 over normalized
    coordinates nx, ny in [0, 1]. The flexible primitive — ripples, gradients,
    blobs, anything you can write as a function."""
    rows = []
    for y in range(height):
        ny = y / (height - 1) if height > 1 else 0.0
        line = []
        for x in range(width):
            nx = x / (width - 1) if width > 1 else 0.0
            v = max(0.0, min(1.0, fn(nx, ny)))
            line.append(ramp[min(len(ramp) - 1, int(v * len(ramp)))])
        rows.append("".join(line).rstrip())
    return "\n".join(rows)

# --- calligram: a word-field shaded by MEANING, not cells -------------------
# A concrete-poem / calligram: the WORDS are the paint. A single act, repeated,
# forms a figure — and its vocabulary climbs a semantic gradient by position, so
# WHERE a word sits encodes HOW intense it is (seeing → look → gaze → KNOW). The
# peak word can ring a VOID (an eye's pupil, a mandala's hollow), which is the
# move's whole power: the most intense word surrounds an absence. Unlike
# terrain/wave/field (which shade cells), this shades meaning. A figurative image
# with no right border — it cannot drift; all-ASCII words are robust either theme.

def calligram(gradient, fn, width=74, height=31):
    """Fill a figure with a repeated word-field on a semantic gradient.
    `gradient` is low→high intensity words (e.g. ["seeing",…,"KNOW"]).
    `fn(nx, ny)` -> intensity in [0,1] (which word) or None (blank / void) —
    the SAME normalized-coordinate contract as field(). Deterministic."""
    def inten_at(x, y):
        nx = x / (width - 1) if width > 1 else 0.0
        ny = y / (height - 1) if height > 1 else 0.0
        return fn(nx, ny)
    rows = []
    for y in range(height):
        elig = [inten_at(x, y) is not None for x in range(width)]
        line = [" "] * width
        x = 0
        while x < width:
            if not elig[x]:
                x += 1; continue
            run_end = x
            while run_end < width and elig[run_end]:
                run_end += 1
            pos = x
            while pos < run_end:
                v = inten_at(pos, y) or 0.0
                idx = min(len(gradient) - 1, max(0, int(v * len(gradient))))
                w = gradient[idx]
                if pos + len(w) <= run_end:
                    for i, ch in enumerate(w):
                        line[pos + i] = ch
                    pos += len(w) + 1
                else:
                    pos += 1
            x = run_end
        rows.append("".join(line).rstrip())
    while rows and rows[0] == "":          # crop blank top/bottom rows
        rows.pop(0)
    while rows and rows[-1] == "":
        rows.pop()
    return "\n".join(rows)

# Figure presets: each returns an fn(nx, ny) for calligram(). Three topologies —
# almond+void, annulus+void, solid — so the peak word can ring a void or crown an
# apex. Write your own fn for any silhouette (e.g. a rightward arrow whose tip is
# the peak: shaft `u<=0.28 and abs(v)<=0.20`, head `abs(v)<=0.8*(1-u)/0.72`,
# intensity `(u+1)/2`).

def fig_eye(pupil=0.30, squash=1.7):
    """Almond eye with a void pupil; peak word rings the pupil. squash>1 widens."""
    def fn(nx, ny):
        u = (nx - 0.5) * 2; v = (ny - 0.5) * 2 * squash
        d = math.hypot(u, v)
        if d < pupil or d > 1.0:
            return None
        return (1.0 - d) / (1.0 - pupil)
    return fn

def fig_ring(inner=0.46, outer=1.0):
    """Annulus / mandala with a hollow center; peak word rings the inner rim."""
    def fn(nx, ny):
        u = (nx - 0.5) * 2; v = (ny - 0.5) * 2
        d = math.hypot(u, v)
        if d < inner or d > outer:
            return None
        return (outer - d) / (outer - inner)
    return fn

def fig_spire(base=0.95):
    """Solid triangle, apex at top; peak word crowns the apex."""
    def fn(nx, ny):
        u = (nx - 0.5) * 2
        if ny < 0.04 or abs(u) > ny * base:
            return None
        return 1.0 - ny
    return fn


def exponential_backoff_spiral():
    """A fixed golden recipe for exponential backoff.

    The widening spiral is the mechanism: attempt 1 starts near the center, each
    retry waits farther out, and the final arrow exits only after the gaps widen.
    It is intentionally an open figurative image, so block glyphs and arrows have
    no right edge to drift.
    """
    return "\n".join([
        "  EXPONENTIAL BACKOFF",
        "",
        "               ▓▓▓▓▓▓▓▓▓▓▓",
        "           ▓▓ 4          ▓▓▓▓",
        "         ███                ▓▓▓",
        "       ███                    ▓▓▓",
        "      ██            ░░░         ▓",
        "     ██         ░░◂░░ ░░░░       ▓",
        "     █         ▒░   .... ░░      ▓",
        "    ██         ▒   ..  .. ░      ▓",
        "    █          ▒   :    1 :      ▓",
        "    █          3   :: 2 :::     ▓▓",
        "    █          ▒▒              ▓▓",
        "    ██          ▒▒▒         ▒▒▒",
        "     █            ▒▒▒▒▒▒▒▒▒▒▒",
        "     ██",
        "      ██",
        "       ███",
        "         ███",
        "           ███",
        "              ████                >",
        "                  ██████>█████████",
        "",
        "  fail 1      retry 2      retry 3      retry 4",
        "     │           │            │            │",
        "     └─ wait 1s ─┴─ wait 2s ──┴─ wait 4s ──┴─> success or give up",
        "        the gaps widen; that widening is the backoff",
    ])


if __name__ == "__main__":
    weekend = [2, 5, 22, 8, 30, 12, 25, 40, 18, 35, 50, 28, 45, 60, 22, 0]
    print("block   ", spark_block(weekend))
    print("braille ", spark_braille(weekend))
    print("hbar    ", hbar(0.23), "23%")
    print()
    print(open_frame("OPEN FRAME · cannot drift", [
        " ✓  held   rolled back · ~0 failures",
        " ~  open   refund the 41? · ~$1,800",
    ]))
    print()
    txt, warns = measured_box("CLOSED / measured", [
        "  all-ASCII content holds the right border  ",
    ])
    print(txt)
    print("warnings:", warns or "none")
    txt, warns = measured_box("CLOSED / with dot", ["  this line has a · middle dot  "])
    print("\n(demo of the guard)\nwarnings:", warns)
    print()
    print(exponential_backoff_spiral())
    print()
    print("CALLIGRAM · an eye made of attention, knowing nothing at its center")
    print(calligram(["seeing", "see", "look", "read", "gaze", "watch", "SEE", "KNOW"],
                    fig_eye()))
