"""
FIGURE 17 (V2) - Morocco's Battery-Materials Investments: BTR & Shinzoom
Replaces outdated/inaccurate V1 figures with verified primary-source data.

Left: investment magnitude (USD million). Right: verified stat cards
(products, capacity, EV-equivalent, location, status). All figures sourced.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_style"))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import me_style as S

S.apply_base_style()

fig = plt.figure(figsize=(14.0, 8.4))

# ---- left: investment bars ------------------------------------------------
axL = fig.add_axes([0.065, 0.30, 0.46, 0.44])
axL.set_xlim(0, 860)
axL.set_ylim(-0.6, 1.6)
y_btr, y_shz = 1.05, 0.05
bh = 0.46

# BTR: 750 (validated)
axL.barh(y_btr, 750, height=bh, color=S.GREEN, zorder=3)
axL.text(750 + 14, y_btr, "USD 750 M", va="center", ha="left",
         fontsize=13, fontweight="bold", color=S.GREEN)
# Shinzoom: 460 solid + 460->500 hatched ("up to ~500M")
axL.barh(y_shz, 460, height=bh, color=S.GOLD, zorder=3)
axL.barh(y_shz, 40, left=460, height=bh, color=S.GOLD_LIGHT, edgecolor=S.GOLD,
         hatch="////", linewidth=1.2, zorder=3)
axL.text(500 + 14, y_shz, "USD 460 M  (up to ~500 M)", va="center", ha="left",
         fontsize=13, fontweight="bold", color="#9A7400")

axL.set_yticks([y_btr, y_shz])
axL.set_yticklabels(["BTR New Material\nGroup", "Shinzoom\n(Hunan Zhongke)"],
                    fontsize=12.5, fontweight="bold")
axL.set_xlabel("Announced investment, USD million")
axL.set_xticks([0, 200, 400, 600, 800])
axL.grid(axis="y", visible=False)
axL.tick_params(length=0)
axL.spines["left"].set_visible(False)

# ---- right: verified stat cards ------------------------------------------
axR = fig.add_axes([0.55, 0.085, 0.43, 0.70])
axR.set_xlim(0, 1)
axR.set_ylim(0, 1)
axR.axis("off")

def card(y0, h, accent, title, rows):
    axR.add_patch(FancyBboxPatch((0.02, y0), 0.96, h,
                  boxstyle="round,pad=0.008,rounding_size=0.015",
                  facecolor="#FAFAF7", edgecolor=S.GREY_LIGHT, linewidth=1.0,
                  zorder=2))
    axR.add_patch(plt.Rectangle((0.02, y0), 0.012, h, facecolor=accent,
                  edgecolor="none", zorder=3))
    axR.text(0.07, y0 + h - 0.05, title, fontsize=13.0, fontweight="bold",
             color=accent, va="top", ha="left")
    yy = y0 + h - 0.135
    for r in rows:
        axR.text(0.085, yy, "\u2022", fontsize=12, color=accent, va="top", ha="left")
        axR.text(0.115, yy, r, fontsize=10.5, color=S.INK, va="top", ha="left",
                 linespacing=1.22)
        yy -= 0.066 * (1 + r.count("\n"))

card(0.535, 0.45, S.GREEN, "BTR New Material Group  \u2014  ~USD 750 M", [
    "Integrated plant: cathode 50,000 t/yr + anode 60,000 t/yr",
    "Capacity sufficient to supply ~500,000 EVs per year",
    "Cit\u00e9 Mohammed VI Tanger Tech (15 ha, two phases)",
    "First cathode output Sep 2026; targets ~USD 1 bn revenue",
])
card(0.045, 0.45, S.GOLD, "Shinzoom (Hunan Zhongke)  \u2014  up to ~USD 500 M", [
    "Anode (negative-electrode) production facility",
    "20-hectare site; ~2,000 jobs",
    "Cit\u00e9 Mohammed VI Tanger Tech",
    "Announced May 2024 (USD 460 M); expansion to a\n100,000 t/yr anode base later proposed",
])

# correction + context band
fig.text(0.065, 0.205,
         "Update vs V1:  prior figure cited BTR ~USD 690 M (cathode only). Verified scope is "
         "~USD 750 M for an integrated cathode + anode plant.",
         fontsize=9.6, color=S.GREY, style="italic", ha="left", va="center",
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#FBF6EA", edgecolor=S.GOLD, lw=1.0))
fig.text(0.065, 0.145,
         "Context:  both sit within a wider Tanger Tech / Kenitra battery cluster \u2014 e.g. Gotion "
         "High-Tech's USD 1.3 bn EV gigafactory in Kenitra (scaling 20 \u2192 100 GWh).",
         fontsize=9.6, color=S.GREY, ha="left", va="center")

S.titleblock(
    fig,
    "Morocco's Battery-Materials Bet",
    "Two anchor Chinese investments in cathode & anode manufacturing, Tanger Tech",
)
S.sourceblock(
    fig,
    "Sources: BTR \u2014 AGBI (May 2025, USD 750 M; capacity for ~half a million cars); Reuters "
    "(Mar 2024, cathode 50,000 t); electrive (Aug 2024, anode 60,000 t); Morocco World News "
    "(May 2026, ~MAD 6 bn). Shinzoom \u2014 Reuters (May 2024, USD 460 M anode, 20 ha). "
    "Cluster \u2014 Reuters (Jun 2024, Gotion USD 1.3 bn).",
)
S.tag(fig)

out = os.path.join(os.path.dirname(__file__), "FIG-17_battery_investments_V2.png")
fig.savefig(out)
print("WROTE", out)
