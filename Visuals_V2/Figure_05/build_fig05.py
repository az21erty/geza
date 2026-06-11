"""
FIGURE 5 (V2) - Industrial Exports: Automotive & Aerospace
Re-audited dataset. Core integrity fix: the V1 series placed an aerospace value
of MAD 21.9 bn at 2022. Office des Changes / Reuters confirm that figure is the
2023 value (MAD 21.8 bn); 2024 = MAD 26.4 bn. Corrected here.

Chart: grouped bars over fully/mostly validated years 2020-2024, single MAD-bn
axis for comparability. One reconstructed estimate (2022 aerospace) is hatched
and flagged. Earlier reconstructed years are audited in the dataset/validation
notes but not charted, to avoid mixing confidence levels.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_style"))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import me_style as S

S.apply_base_style()

years = ["2020", "2022", "2023", "2024"]
auto  = [72.7, 111.3, 141.8, 157.0]          # all validated
aero  = [12.9, 18.9, 21.8, 26.4]             # 18.9 (2022) = reconstructed estimate
aero_est = [False, True, False, False]

x = np.arange(len(years))
w = 0.40

fig = plt.figure(figsize=(13.2, 8.2))
ax = fig.add_axes([0.085, 0.135, 0.65, 0.63])

b1 = ax.bar(x - w/2, auto, w, color=S.GREEN, label="Automotive", zorder=3)
# aerospace bars: validated solid gold; reconstructed estimate hatched + lighter
for i, (xi, v, est) in enumerate(zip(x, aero, aero_est)):
    if est:
        ax.bar(xi + w/2, v, w, color=S.GOLD_LIGHT, edgecolor=S.GOLD, linewidth=1.4,
               hatch="////", zorder=3)
    else:
        ax.bar(xi + w/2, v, w, color=S.GOLD, zorder=3)

# data labels
for xi, v in zip(x - w/2, auto):
    ax.text(xi, v + 2.6, f"{v:.1f}", ha="center", va="bottom",
            fontsize=11.5, fontweight="bold", color=S.GREEN)
for xi, v, est in zip(x + w/2, aero, aero_est):
    ax.text(xi, v + 2.6, f"{v:.1f}" + ("*" if est else ""), ha="center", va="bottom",
            fontsize=11.5, fontweight="bold", color=S.GOLD)

ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylabel("Exports, MAD billion")
ax.set_ylim(0, 178)
ax.set_xlim(-0.6, len(years) - 0.4)
ax.grid(axis="x", visible=False)
ax.spines["left"].set_color(S.GREY)
ax.tick_params(length=0)

# correction callout pointing at the 2023 aerospace bar
ax.annotate(
    "Correction: V1 placed MAD 21.9 bn\nat 2022. This is the 2023 value\n"
    "(MAD 21.8 bn, Office des Changes).",
    xy=(2 + w/2, 21.8), xytext=(1.15, 70),
    fontsize=9.6, color=S.GREY, ha="left", va="center", linespacing=1.25,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="#FBF6EA", edgecolor=S.GOLD, lw=1.1),
    arrowprops=dict(arrowstyle="-|>", color=S.GOLD, lw=1.4,
                    connectionstyle="arc3,rad=-0.2"),
)

# legend
handles = [
    Patch(facecolor=S.GREEN, label="Automotive (Office des Changes)"),
    Patch(facecolor=S.GOLD, label="Aerospace (Office des Changes)"),
    Patch(facecolor=S.GOLD_LIGHT, edgecolor=S.GOLD, hatch="////",
          label="Aerospace, reconstructed estimate (*)"),
]
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.005, 1.0),
          fontsize=10.5)

# --- right-hand context panel ---------------------------------------------
px = 0.775
fig.text(px, 0.715, "WHAT THE NUMBERS SAY", fontsize=10.5, fontweight="bold",
         color=S.GREEN)
fig.add_artist(plt.Line2D([px, px + 0.185], [0.700, 0.700], color=S.GOLD,
               lw=2.0, transform=fig.transFigure))
notes = [
    ("Automotive 2024", "MAD 157.0 bn  (\u2248 USD 17 bn)\nrecord; +41% since 2022"),
    ("Aerospace 2024", "MAD 26.4 bn  (\u2248 USD 2.8 bn)\n+21% over 2023"),
    ("Latest reads", "Auto 9M-2025: MAD 112.2 bn (\u22122.7% y/y)\nAero 2025: MAD 29 bn (full year)"),
    ("Ascent", "Automotive is now Morocco's\nleading export sector; aerospace\nis the fastest climber."),
]
yy = 0.66
for head, body in notes:
    fig.text(px, yy, head, fontsize=10.2, fontweight="bold", color=S.GREY)
    fig.text(px, yy - 0.028, body, fontsize=9.6, color=S.INK, linespacing=1.3)
    yy -= 0.115

S.titleblock(
    fig,
    "Industrial Exports Take Off",
    "Automotive and aerospace export value, MAD billion, 2020\u20132024",
)
S.sourceblock(
    fig,
    "Sources: Office des Changes (annual); automotive 2024 record MAD 157 bn confirmed by "
    "press reporting; aerospace 2023 MAD 21.8 bn / 2024 MAD 26.4 bn (Reuters citing Office des "
    "Changes). (*) 2022 aerospace is a reconstructed estimate (see DATA_VALIDATION.md).",
)
S.tag(fig)

out = os.path.join(os.path.dirname(__file__), "FIG-05_auto_aerospace_exports_V2.png")
fig.savefig(out)
print("WROTE", out)
