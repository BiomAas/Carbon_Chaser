import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

scores = pd.read_csv("pca_scores.csv", index_col=0)
loadings = pd.read_csv("pca_loadings.csv", index_col=0)

CHOC = "#3B1F0F"
SIENNA = "#A0522D"
IVORY = "#FFFFF0"

fig, ax = plt.subplots(figsize=(9, 7))
ax.set_facecolor(IVORY)
fig.patch.set_facecolor("white")

x = scores["PC1"]
y = scores["PC2"]

# Scale loading arrows to roughly match the score point spread
scale = (x.abs().max()) / loadings["PC1"].abs().max() * 0.75

arrow_x = loadings["PC1"] * scale
arrow_y = loadings["PC2"] * scale

# --- Explicitly set axis limits to include BOTH scores and arrow tips ---
all_x = list(x) + list(arrow_x) + [0]
all_y = list(y) + list(arrow_y) + [0]
pad_x = (max(all_x) - min(all_x)) * 0.20
pad_y = (max(all_y) - min(all_y)) * 0.20
ax.set_xlim(min(all_x) - pad_x, max(all_x) + pad_x)
ax.set_ylim(min(all_y) - pad_y, max(all_y) + pad_y)

# --- Score points ---
ax.scatter(x, y, s=140, color=SIENNA, edgecolor=CHOC, linewidth=1.5, zorder=4)

# Manual label offsets to avoid overlap on the tightly-clustered controls
label_offsets = {
    "BBM_control_pH10": (10, 10),
    "BBM_control_pH9.0": (10, -14),
    "BBM_control_pH9.5": (10, -32),
    "R1_BBM_pH9.0_Alk1.5": (-10, 12),
    "R6_BBM_pH9.5_Alk2.5": (10, 10),
    "DD_optimum_pH9.5": (10, -16),
}
for label, xi, yi in zip(scores.index, x, y):
    off = label_offsets.get(label, (8, 6))
    ax.annotate(label, (xi, yi), textcoords="offset points", xytext=off,
                fontsize=8.5, color=CHOC, fontweight="bold")

# --- Loading vectors ---
for var in loadings.index:
    lx, ly = arrow_x[var], arrow_y[var]
    ax.annotate("", xy=(lx, ly), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=CHOC, linewidth=2, alpha=0.85),
                clip_on=False)
    ax.text(lx * 1.15, ly * 1.15, var, fontsize=10, color=CHOC,
            fontweight="bold", ha="center", va="center")

ax.axhline(0, color=SIENNA, linewidth=0.8, alpha=0.4, zorder=1)
ax.axvline(0, color=SIENNA, linewidth=0.8, alpha=0.4, zorder=1)

ax.set_xlabel("PC1 (94.7% variance)", fontsize=11, color=CHOC)
ax.set_ylabel("PC2 (4.4% variance)", fontsize=11, color=CHOC)
ax.set_title("CLR-PCA biplot: conditions & metabolite loadings", fontsize=13, fontweight="bold", color=CHOC)
ax.tick_params(colors=CHOC)
ax.spines[['top','right']].set_visible(False)
ax.spines[['left','bottom']].set_color(CHOC)
ax.grid(color=SIENNA, alpha=0.12, zorder=0)

plt.tight_layout()
plt.savefig("pca_biplot.png", dpi=200, bbox_inches="tight", facecolor="white")
print("Saved pca_biplot.png")






