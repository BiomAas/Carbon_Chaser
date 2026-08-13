import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('county_feedstock_categories.csv', index_col='County')

# Pearson correlation across the 8 categories (how they move together across counties)
corr = df.corr(method='pearson')

fig, ax = plt.subplots(figsize=(8, 7))
im = ax.imshow(corr, cmap='Greens', vmin=-1, vmax=1)

ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha='right')
ax.set_yticklabels(corr.columns)

# annotate each cell with its value
for i in range(len(corr)):
    for j in range(len(corr)):
        val = corr.iloc[i, j]
        color = 'white' if val > 0.6 else 'black'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', color=color, fontsize=9)

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Pearson correlation')

ax.set_title('Correlation between feedstock categories\n(across 26 counties)', fontsize=12.5)
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=200)
print("Saved: correlation_matrix.png")
