"""
FIGURE 16C (V2) - OCP's Value-Chain Ascent
Problem in V1: trajectory direction was ambiguous - a reader could not tell whether
value added increases upward or downward.

Fix: an explicitly ASCENDING staircase. Each downstream stage is a taller step
(left = raw, right = processed; up = more value). Redundant, unmissable cues:
a rising arrow ribbon, "RAW MATERIAL" at the low corner, "MORE VALUE ADDED" at the
high corner, and arrowed axis titles. Schematic value-per-tonne ladder anchored by
one validated quantitative fact (2024 revenue mix).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_style"))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import me_style as S

S.apply_base_style()

# stage: (name, descriptor, height, color, emerging)
STAGES = [
    ("Phosphate rock", "Raw extraction\n70% of world reserves", 1.0, S.GREEN_LIGHT, False),
    ("Phosphoric acid", "First chemical\ntransformation", 2.0, S.GREEN_MID, False),
    ("Phosphate fertilizers", "DAP / MAP / TSP\nbulk export", 3.0, "#235C43", False),
    ("Specialty fertilizers", "Soil-specific blends\nAfrican markets", 4.0, S.GREEN, False),
    ("Battery-grade LFP\nprecursors", "Emerging: phosphate\nfor EV batteries", 5.0, S.GOLD, True),
]

fig = plt.figure(figsize=(13.4, 8.6))
ax = fig.add_axes([0.085, 0.10, 0.88, 0.66])
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(0, 6.2)
ax.axis("off")

bw = 0.9
label_artists = []
for i, (name, desc, h, col, emerging) in enumerate(STAGES):
    x = i + 0.5
    # the step (bar)
    ax.add_patch(FancyBboxPatch((x - bw/2, 0), bw, h,
                 boxstyle="round,pad=0.0,rounding_size=0.04",
                 facecolor=col, edgecolor=S.WHITE, linewidth=1.5, zorder=3))
    # stage number chip near the top of the bar
    ax.text(x, h - 0.32, str(i + 1), ha="center", va="center",
            fontsize=15, fontweight="bold", color=S.WHITE, zorder=5)
    # label card above the bar
    title = ("EMERGING\n" if emerging else "") + name
    card = ax.annotate(
        f"{name}\n{desc}", xy=(x, h + 0.18), ha="center", va="bottom",
        fontsize=10.3, color=S.INK, linespacing=1.22, zorder=6,
        bbox=dict(boxstyle="round,pad=0.4", facecolor=S.WHITE,
                  edgecolor=(S.GOLD if emerging else col), linewidth=1.4),
    )
    label_artists.append((name, card))
    if emerging:
        ax.text(x, h + 0.02, "EMERGING", ha="center", va="bottom", fontsize=8.2,
                fontweight="bold", color=S.GOLD, zorder=7)

# rising arrow ribbon along the staircase (low-left -> high-right)
arrow = FancyArrowPatch((-0.18, 0.55), (5.18, 5.55),
                        arrowstyle="-|>", mutation_scale=34,
                        linewidth=7, color=S.GOLD, alpha=0.28, zorder=1)
ax.add_patch(arrow)

# directional anchors (kill ambiguity)
ax.text(-0.30, 0.30, "RAW\nMATERIAL", ha="left", va="bottom", fontsize=10.5,
        fontweight="bold", color=S.GREY, linespacing=1.1)
ax.text(5.42, 5.65, "MORE\nVALUE ADDED", ha="right", va="top", fontsize=11.5,
        fontweight="bold", color=S.GOLD, linespacing=1.1, zorder=8)

# axis arrows / titles
ax.annotate("", xy=(5.45, -0.12), xytext=(-0.45, -0.12),
            arrowprops=dict(arrowstyle="-|>", color=S.GREY, lw=2.0),
            annotation_clip=False)
ax.text(2.5, -0.42, "Degree of downstream processing", ha="center", va="top",
        fontsize=11.5, color=S.GREY, fontweight="bold")
ax.annotate("", xy=(-0.45, 6.0), xytext=(-0.45, 0.2),
            arrowprops=dict(arrowstyle="-|>", color=S.GREY, lw=2.0),
            annotation_clip=False)
ax.text(-0.62, 3.1, "Value added per tonne", ha="center", va="center",
        rotation=90, fontsize=11.5, color=S.GREY, fontweight="bold")

# validated quantitative anchor (the one hard number)
anchor = ax.annotate(
    "2024 anchor:  OCP revenue MAD 96.99 bn (USD 9.76 bn);\n"
    "69% from fertilizers & downstream \u2014 not raw rock.\n"
    "(1970s: OCP exported raw phosphate rock.)",
    xy=(0.5, 1.0), xytext=(1.35, 1.35),
    fontsize=9.8, color=S.INK, ha="left", va="center", linespacing=1.3, zorder=9,
    bbox=dict(boxstyle="round,pad=0.55", facecolor="#F3F7F4", edgecolor=S.GREEN, lw=1.2),
)

S.titleblock(
    fig,
    "OCP Climbs Its Own Value Chain",
    "Each downstream stage captures more value per tonne of phosphate \u2014 "
    "rock \u2192 acid \u2192 fertilizer \u2192 specialty \u2192 battery materials",
)
S.sourceblock(
    fig,
    "Sources: OCP Group financial disclosures (2024 revenue MAD 96.99 bn, 69% fertilizers; "
    "9M-2025 revenue USD 9.04 bn, +30% y/y); manuscript Part VI. Step heights are a schematic "
    "value-per-tonne ladder (relative, illustrative); exact per-tonne margins are proprietary.",
)
S.tag(fig)

print("Overlap check (stage cards):")
S.report_overlaps(fig, label_artists, pad=1.05)
out = os.path.join(os.path.dirname(__file__), "FIG-16C_ocp_value_chain_ascent_V2.png")
fig.savefig(out)
print("WROTE", out)
