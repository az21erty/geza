"""
THE MOROCCO EQUATION - Visual Package V2
Shared visual-identity module (Bloomberg / IMF / World Bank house style).

Design rules enforced here:
  Background : white
  Primary    : dark green   #1B4332
  Secondary  : dark grey    #3D3D3D
  Accent     : muted gold   #B8860B
  Typography : clean sans-serif (DejaVu Sans), generous spacing
  No chartjunk, no overlapping/truncated labels, publication quality (300 dpi).

Every figure script imports `apply_base_style()` and the palette constants so
the eight revised figures share one identity.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------
GREEN       = "#1B4332"   # primary  - dark green
GREEN_MID   = "#2D6A4F"   # supporting green tint
GREEN_LIGHT = "#74A892"   # light green tint
GREY        = "#3D3D3D"   # secondary - dark grey
GREY_MID    = "#777777"   # supporting grey tint
GREY_LIGHT  = "#C7C7C7"   # light grey tint / gridlines
GOLD        = "#B8860B"   # accent - muted gold
GOLD_LIGHT  = "#E0C878"   # light gold tint
WHITE       = "#FFFFFF"
INK         = "#222222"   # near-black for primary text
PAPER       = "#FFFFFF"

# Ordered categorical palette (for multi-series charts)
SERIES = [GREEN, GOLD, GREY, GREEN_LIGHT, GREY_MID, GOLD_LIGHT]

# Risk / heat ramp (low -> high) used by the risk matrix
HEAT = ["#2D6A4F", "#5C8A3A", "#B8860B", "#C26A2B", "#9B2226"]


def _pick_font():
    """Prefer a clean sans with full glyph coverage available in the sandbox."""
    available = {f.name for f in font_manager.fontManager.ttflist}
    # DejaVu Sans first: guaranteed coverage of dashes, minus sign, bullets, etc.
    for name in ("Helvetica", "Arial", "Liberation Sans", "DejaVu Sans", "Noto Sans"):
        if name in available:
            return name
    return "DejaVu Sans"


FONT = _pick_font()


def apply_base_style():
    """Apply the shared rcParams. Call once at the top of every figure script."""
    mpl.rcParams.update({
        "figure.dpi": 110,
        "savefig.dpi": 300,
        "figure.facecolor": PAPER,
        "axes.facecolor": PAPER,
        "savefig.facecolor": PAPER,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.30,

        "font.family": "sans-serif",
        "font.sans-serif": [FONT, "DejaVu Sans"],
        "font.size": 12.5,
        "text.color": INK,

        "axes.edgecolor": GREY,
        "axes.linewidth": 1.0,
        "axes.titlecolor": GREEN,
        "axes.labelcolor": GREY,
        "axes.titlesize": 15,
        "axes.labelsize": 12.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.axisbelow": True,

        "xtick.color": GREY,
        "ytick.color": GREY,
        "xtick.labelsize": 11.5,
        "ytick.labelsize": 11.5,

        "grid.color": GREY_LIGHT,
        "grid.linewidth": 0.7,
        "grid.alpha": 0.55,

        "legend.frameon": False,
        "legend.fontsize": 11.5,

        "lines.linewidth": 2.6,
        "lines.solid_capstyle": "round",
    })


def titleblock(fig, title, subtitle=None, x=0.012, top=0.965):
    """
    Standard left-aligned editorial title block.
    Bold dark-green title + dark-grey subtitle, with a gold rule beneath.
    Returns the y-coordinate just under the block.
    """
    fig.text(x, top, title, ha="left", va="top",
             fontsize=18, fontweight="bold", color=GREEN)
    y = top - 0.052
    if subtitle:
        fig.text(x, y, subtitle, ha="left", va="top",
                 fontsize=12.5, color=GREY)
        y -= 0.040
    # gold rule
    line = plt.Line2D([x, x + 0.30], [y, y], color=GOLD, linewidth=2.6,
                      transform=fig.transFigure, solid_capstyle="butt")
    fig.add_artist(line)
    return y - 0.02


def sourceblock(fig, text, x=0.012, y=0.022):
    """Standard footnote / source line."""
    fig.text(x, y, text, ha="left", va="bottom",
             fontsize=9.0, color=GREY_MID, style="italic")


def tag(fig, text="THE MOROCCO EQUATION  |  Visual Package V2", x=0.988, y=0.022):
    """Discreet right-aligned series tag."""
    fig.text(x, y, text, ha="right", va="bottom",
             fontsize=8.5, color=GREY_LIGHT)



def report_overlaps(fig, items, pad=1.0):
    """
    items: list of (name, artist) where artist supports get_window_extent().
    Prints any pairwise bounding-box overlaps (in display px). Returns overlap count.
    Used as an automated 'no overlapping labels' gate since the renderer is headless.
    """
    fig.canvas.draw()
    rnd = fig.canvas.get_renderer()
    boxes = []
    for name, art in items:
        try:
            bb = art.get_window_extent(renderer=rnd)
            boxes.append((name, bb.expanded(pad, pad)))
        except Exception as e:  # noqa
            print(f"  [overlap-check] could not measure {name}: {e}")
    n = 0
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            ni, bi = boxes[i]
            nj, bj = boxes[j]
            if bi.overlaps(bj):
                n += 1
                print(f"  [OVERLAP] '{ni}'  <->  '{nj}'")
    print(f"  [overlap-check] {len(boxes)} labels measured, {n} overlaps.")
    return n
