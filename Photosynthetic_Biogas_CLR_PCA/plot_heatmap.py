import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# --- Custom palette: dark chocolate (negative) -> burnt sienna (mid) -> ivory (positive) ---
colors = ["#3B1F0F", "#A0522D", "#FFFFF0"]  # dark chocolate, burnt sienna, ivory
cmap = LinearSegmentedColormap.from_list("choc_sienna_ivory", colors, N=256)

raw_corr = pd.read_csv("raw_correlation_matrix.csv", index_col=0)
clr_corr = pd.read_csv("clr_correlation_matrix.csv", index_col=0)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

for ax, data, title in zip(axes, [raw_corr, clr_corr], ["Raw % correlation", "CLR-transformed correlation"]):
    im = ax.imshow(data.values, cmap=cmap, vmin=-1, vmax=1)
    ax.set_xticks(range(len(data.columns)))
    ax.set_yticks(range(len(data.index)))
    ax.set_xticklabels(data.columns, rotation=45, ha="right", fontsize=9)
    ax.set_yticklabels(data.index, fontsize=9)
    ax.set_title(title, fontsize=12, fontweight="bold", color="#3B1F0F")
    # annotate values
    for i in range(len(data.index)):
        for j in range(len(data.columns)):
            val = data.values[i, j]
            text_color = "#3B1F0F" if val > 0.3 else "#FFFFF0"
            ax.text(j, i, f"{val:.2f}", ha="center", va="center",
                     fontsize=8, color=text_color)

cbar = fig.colorbar(im, ax=axes, orientation="vertical", fraction=0.03, pad=0.03)
cbar.set_label("Correlation", fontsize=10)

fig.suptitle("Metabolite correlation structure: raw % vs CLR-corrected", fontsize=13, fontweight="bold")
plt.savefig("correlation_heatmaps.png", dpi=200, bbox_inches="tight", facecolor="white")
print("Saved correlation_heatmaps.png")
