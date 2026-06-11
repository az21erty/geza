"""
FIGURE 18 (V2) - REPLACEMENT
Recommendation: REPLACE (see REVISION_NOTES.md). The V1 figure carried low analytical
value. The superior alternative below visualises the report's central battery argument:
value in an LFP battery chain concentrates MIDSTREAM (active materials + cells), yet
Morocco's strength is UPSTREAM (phosphate) - the "midstream value gap" it must close
before the LFP window narrows.

Top: value-capture curve across the chain. Bottom: Morocco's position at each stage
(strength + concrete assets).
"""
import sys, os, textwrap
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_style"))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
import me_style as S

S.apply_base_style()

stages = ["Mining /\nraw material", "Refining &\nintermediates",
          "Cathode & anode\nactive materials", "Cell\nmanufacturing",
          "Pack &\nEV assembly"]
value  = [1.0, 2.8, 4.7, 5.0, 3.2]            # value captured per unit (schematic)
# Morocco position: 0=Established strength, 1=Entering (new FDI), 2=Early/nascent
pos    = [0, 1, 1, 2, 0]
POSCOL = {0: S.GREEN, 1: S.GOLD, 2: S.GREY_MID}
POSLAB = {0: "Established strength", 1: "Entering (new FDI)", 2: "Early / nascent"}
assets = [
    "OCP controls ~70% of\nworld phosphate reserves",
    "OCP: 30,000 t of LFP\nintermediates by 2027;\nMera 1 GWh by 2026",
    "BTR cathode + anode;\nShinzoom anode\n(Tanger Tech)",
    "Gotion gigafactory,\nKenitra (20 \u2192 100 GWh) \u2014\njust starting",
    "Renault & Stellantis\nvehicle-assembly base",
]
x = np.arange(len(stages))

fig = plt.figure(figsize=(14.2, 8.8))

# ---- top: value-capture curve --------------------------------------------
axT = fig.add_axes([0.075, 0.515, 0.885, 0.30])
axT.set_xlim(-0.45, 4.45)
axT.set_ylim(0, 6.0)
# midstream value band
axT.axvspan(1.55, 3.45, color=S.GOLD, alpha=0.10, zorder=0)
axT.text(2.5, 5.7, "MIDSTREAM: WHERE VALUE CONCENTRATES", ha="center", va="top",
         fontsize=10.5, fontweight="bold", color="#9A7400")
axT.fill_between(x, value, color=S.GREEN, alpha=0.10, zorder=1)
axT.plot(x, value, color=S.GREEN, lw=2.8, zorder=2)
for xi, v, p in zip(x, value, pos):
    axT.scatter(xi, v, s=240, color=POSCOL[p], edgecolor=S.WHITE, linewidth=2.0,
                zorder=4)
axT.set_ylabel("Value captured\nper unit (schematic)", fontsize=11)
axT.set_yticks([])
axT.set_xticks([])
for sp in ("left", "bottom"):
    axT.spines[sp].set_visible(True)
axT.grid(False)
# arrow pointing from Morocco's strong upstream node to the value peak
axT.annotate("Morocco is strong here\u2026", xy=(0, 1.0), xytext=(0.05, 3.0),
             fontsize=10, color=S.GREEN, ha="left", va="center", fontweight="bold")
axT.annotate("\u2026but value (and the gap) is here",
             xy=(3.0, 5.0), xytext=(3.15, 2.2),
             fontsize=10, color="#9A7400", ha="left", va="center", fontweight="bold",
             arrowprops=dict(arrowstyle="-|>", color=S.GOLD, lw=1.6,
                             connectionstyle="arc3,rad=0.25"))

# ---- bottom: Morocco position cards --------------------------------------
axB = fig.add_axes([0.075, 0.10, 0.885, 0.37])
axB.set_xlim(-0.45, 4.45)
axB.set_ylim(0, 1)
axB.axis("off")
cw = 0.92
for xi, name, p, note in zip(x, stages, pos, assets):
    # connector from curve marker down into card
    axB.add_patch(FancyBboxPatch((xi - cw/2, 0.06), cw, 0.88,
                  boxstyle="round,pad=0.01,rounding_size=0.03",
                  facecolor="#FAFAF7", edgecolor=S.GREY_LIGHT, linewidth=1.0, zorder=2))
    axB.add_patch(plt.Rectangle((xi - cw/2, 0.86), cw, 0.08, facecolor=POSCOL[p],
                  edgecolor="none", zorder=3))
    axB.text(xi, 0.90, name.replace("\n", " "), ha="center", va="center",
             fontsize=10.0, fontweight="bold", color=S.WHITE, zorder=4)
    # status chip
    axB.scatter(xi - cw/2 + 0.08, 0.74, s=90, color=POSCOL[p], zorder=4)
    axB.text(xi - cw/2 + 0.135, 0.74, POSLAB[p], ha="left", va="center",
             fontsize=8.8, color=POSCOL[p], fontweight="bold", zorder=4)
    # asset note
    axB.text(xi, 0.56, note, ha="center", va="top", fontsize=9.4, color=S.INK,
             linespacing=1.3, zorder=4)

# legend (positions)
handles = [Line2D([0], [0], marker="o", color="none", markerfacecolor=POSCOL[k],
                  markersize=11, label=POSLAB[k]) for k in (0, 1, 2)]
axT.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.0, 1.02),
           fontsize=10, ncol=1)

S.titleblock(
    fig,
    "Morocco's Battery Value-Chain Gap",
    "Value concentrates midstream (active materials & cells) \u2014 where Morocco is only now entering",
)
S.sourceblock(
    fig,
    "Sources: manuscript Part VI (battery value chain); OCP/InnovX (Mera Batteries 1 GWh by 2026; "
    "30,000 t LFP intermediates by 2027); BTR & Shinzoom (Tanger Tech); Gotion High-Tech (Kenitra "
    "gigafactory, Reuters Jun 2024); USGS (phosphate reserves). Global LFP market ~USD 90.3 bn by "
    "2034 (16.9% CAGR). Value-capture curve is schematic (relative).",
)
S.tag(fig)

out = os.path.join(os.path.dirname(__file__), "FIG-18_battery_value_chain_position_V2.png")
fig.savefig(out)
print("WROTE", out)
