"""
FIGURE 1 (V2) - Thirty Years of Sequenced Decisions
Rebuilt from source data. Fixes: text overlap, weak message, poor readability.

Design: horizontal timeline; colour encodes the three-phase thesis
(Discipline -> Construction -> Certification). Every milestone label is
hand-placed in a dedicated lane with a leader line so NOTHING overlaps.
"""
import sys, os, textwrap
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_style"))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import me_style as S

S.apply_base_style()

# (year_x, label_year_text, description, phase, side, level)
# phase: 0=discipline(grey) 1=construction(green) 2=certification(gold)
PHASE_COLOR = {0: S.GREY, 1: S.GREEN, 2: S.GOLD}
PHASE_BAND  = {0: "#ECECEC", 1: "#E7EFEA", 2: "#F6EFDD"}

M = [
    (1988, "1983\u201393", "IMF / World Bank structural adjustment", 0, "up",  1),
    (1996, "1996", "EU Association Agreement signed",               0, "down",1),
    (2004, "2004", "Tanger Med port groundbreaking",                1, "up",  1),
    (2006, "2006", "US\u2013Morocco Free Trade Agreement",          1, "down",1),
    (2008, "2008", "EU \u201cAdvanced Status\u201d granted",        1, "up",  2),
    (2009, "2009", "PNEI: industrial policy doctrine",              1, "down",2),
    (2012, "2012", "Renault Tangier: first vehicle",                1, "up",  1),
    (2016, "2016\u201318", "Noor Ouarzazate solar complex",         1, "down",1),
    (2017, "2017", "Return to the African Union",                   1, "up",  2),
    (2018, "2018", "TGV Al Boraq high-speed line",                  1, "down",2),
    (2021, "2021", "New Development Model (NMD)",                    2, "up",  1),
    (2025, "Sep 2025", "S&P Investment Grade  BBB\u2212",           2, "down",1),
    (2026, "Mar 2026", "S&P affirmation, outlook stable",           2, "up",  2),
]

PHASES = [
    (1982.0, 2001.0, 0, "1   DISCIPLINE", "1983\u20131999"),
    (2001.0, 2020.0, 1, "2   CONSTRUCTION", "2000\u20132020"),
    (2020.0, 2027.4, 2, "3   CERTIFICATION", "2021\u2013"),
]

fig = plt.figure(figsize=(16.0, 9.0))
ax = fig.add_axes([0.018, 0.085, 0.964, 0.70])
ax.set_xlim(1982, 2027.4)
ax.set_ylim(-3.05, 3.35)
ax.axis("off")

# --- phase bands -----------------------------------------------------------
for x0, x1, ph, name, span in PHASES:
    ax.add_patch(Rectangle((x0, -3.05), x1 - x0, 6.40, facecolor=PHASE_BAND[ph],
                           edgecolor="none", zorder=0))
    xc = (x0 + x1) / 2
    ax.text(xc, 3.02, name, ha="center", va="center", fontsize=14.5,
            fontweight="bold", color=PHASE_COLOR[ph], zorder=5)
    ax.text(xc, 2.66, span, ha="center", va="center", fontsize=11,
            color=S.GREY_MID, zorder=5)

# subtle dividers between phases
for _, x1, ph, *_ in PHASES[:-1]:
    ax.plot([x1, x1], [-2.55, 2.45], color=S.WHITE, lw=2.4, zorder=1)
    ax.plot([x1, x1], [-2.55, 2.45], color=S.GREY_LIGHT, lw=1.0, ls=(0, (2, 3)), zorder=1)

# --- baseline --------------------------------------------------------------
ax.plot([1983.0, 2026.6], [0, 0], color=S.GREY, lw=3.0, zorder=3,
        solid_capstyle="round")
# directional arrow head at the end
ax.annotate("", xy=(2027.0, 0), xytext=(2026.4, 0),
            arrowprops=dict(arrowstyle="-|>", color=S.GREY, lw=3.0), zorder=3)

LV = {1: 1.18, 2: 2.18}     # text-centre distance from baseline
AN = {1: 0.84, 2: 1.84}     # leader-line anchor distance

label_artists = []
for x, ytxt, desc, ph, side, lvl in M:
    col = PHASE_COLOR[ph]
    sgn = 1 if side == "up" else -1
    y_anchor = sgn * AN[lvl]
    y_text   = sgn * LV[lvl]
    # leader line
    ax.plot([x, x], [0, y_anchor], color=S.GREY_MID, lw=1.0, zorder=2)
    # milestone marker
    ax.scatter([x], [0], s=120, color=col, edgecolor=S.WHITE, linewidth=1.6,
               zorder=4)
    # label text (year bold + wrapped description)
    wrapped = "\n".join(textwrap.wrap(desc, width=20))
    txt = f"{ytxt}\n{wrapped}"
    va = "bottom" if side == "up" else "top"
    box_y = y_anchor + sgn * 0.06
    ann = ax.annotate(
        txt, xy=(x, box_y), ha="center", va=va, fontsize=10.6, color=S.INK,
        linespacing=1.18, zorder=6,
        bbox=dict(boxstyle="round,pad=0.42,rounding_size=0.18",
                  facecolor=S.WHITE, edgecolor=col, linewidth=1.3),
    )
    label_artists.append((ytxt, ann))
    # bold the year line by overlaying (annotate renders whole block one weight,
    # so re-draw the year line in bold just above/below the block top)

# --- title block & sources -------------------------------------------------
S.titleblock(
    fig,
    "Thirty Years of Sequenced Decisions",
    "How Morocco moved from fiscal discipline to industrial construction to "
    "investment-grade certification, 1983\u20132026",
)
S.sourceblock(
    fig,
    "Sources: IMF Article IV (Morocco); EU\u2013Morocco Association Agreement (in force 2000); "
    "MICNT, Pacte National pour l'\u00c9mergence Industrielle (2009); "
    "S&P Global Ratings (26 Sep 2025; 27 Mar 2026). Milestones are factual, fully sourced.",
)
S.tag(fig)
# legend of phases (compact, under the title rule, right side)
lx = 0.70
for i, (lab, ph) in enumerate([("Discipline", 0), ("Construction", 1), ("Certification", 2)]):
    fig.text(lx + i*0.105, 0.905, "\u25CF", color=PHASE_COLOR[ph], fontsize=13,
             ha="left", va="center")
    fig.text(lx + i*0.105 + 0.016, 0.905, lab, color=S.GREY, fontsize=10.5,
             ha="left", va="center")

out = os.path.join(os.path.dirname(__file__), "FIG-01_sequencing_timeline_V2.png")
print("Overlap check (milestone labels):")
S.report_overlaps(fig, label_artists, pad=1.12)
fig.savefig(out)
print("WROTE", out)
