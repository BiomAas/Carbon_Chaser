import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

clr = pd.read_csv("clr_matrix_A.csv", index_col=0)
centered = clr - clr.mean(axis=0)
U, S, Vt = np.linalg.svd(centered.values, full_matrices=False)
explained_var = (S ** 2) / np.sum(S ** 2) * 100
cumulative = np.cumsum(explained_var)

CHOC = "#3B1F0F"
SIENNA = "#A0522D"
IVORY = "#FFFFF0"

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_facecolor(IVORY)
fig.patch.set_facecolor("white")

pcs = [f"PC{i+1}" for i in range(len(S))]
bars = ax.bar(pcs, explained_var, color=SIENNA, edgecolor=CHOC, linewidth=1.2, zorder=3)
ax.plot(pcs, cumulative, color=CHOC, marker="o", markersize=6,
        markerfacecolor=IVORY, markeredgecolor=CHOC, linewidth=2, zorder=4, label="Cumulative %")

for bar, val in zip(bars, explained_var):
    ax.text(bar.get_x() + bar.get_width()/2, val + 1.5, f"{val:.1f}%",
            ha="center", fontsize=9, color=CHOC, fontweight="bold")

ax.set_ylabel("Explained variance (%)", fontsize=11, color=CHOC)
ax.set_title("Scree plot: CLR-transformed PCA (n=6)", fontsize=13, fontweight="bold", color=CHOC)
ax.set_ylim(0, 110)
ax.tick_params(colors=CHOC)
ax.spines[['top','right']].set_visible(False)
ax.spines[['left','bottom']].set_color(CHOC)
ax.legend(frameon=False, labelcolor=CHOC, loc="center right")
ax.grid(axis="y", color=SIENNA, alpha=0.15, zorder=0)

plt.tight_layout()
plt.savefig("scree_plot.png", dpi=200, bbox_inches="tight", facecolor="white")
print("Saved scree_plot.png")
