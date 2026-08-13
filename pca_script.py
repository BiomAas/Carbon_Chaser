import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('county_feedstock_categories.csv', index_col='County')
print("Loaded data:", df.shape[0], "counties x", df.shape[1], "categories\n")

shares = df.div(df.sum(axis=1), axis=0) * 100
X = StandardScaler().fit_transform(shares)

pca = PCA()
pcs = pca.fit_transform(X)

print("=== Explained variance per PC (%) ===")
for i, v in enumerate(pca.explained_variance_ratio_[:5], start=1):
    print(f"PC{i}: {v*100:.2f}%")
print(f"Cumulative (PC1-3): {np.sum(pca.explained_variance_ratio_[:3])*100:.2f}%\n")

loadings = pd.DataFrame(pca.components_[:2].T, index=shares.columns, columns=['PC1', 'PC2'])
print("=== Loadings (sorted by PC1 strength) ===")
print(loadings.reindex(loadings.PC1.abs().sort_values(ascending=False).index).round(3))
print()

n_clusters = 4
clusters = KMeans(n_clusters=n_clusters, random_state=42, n_init=10).fit_predict(pcs[:, :3])

results = pd.DataFrame({
    'County': shares.index,
    'PC1': pcs[:, 0],
    'PC2': pcs[:, 1],
    'Cluster': clusters,
    'Total_tDM': df.sum(axis=1).values
}).sort_values('Cluster')

print("=== County clusters ===")
print(results.to_string(index=False))
results.to_csv('pca_results.csv', index=False)
print("\nSaved: pca_results.csv")

plt.figure(figsize=(9, 7))
plt.scatter(pcs[:, 0], pcs[:, 1], c=clusters, cmap='tab10', s=80, edgecolor='white')
for i, county in enumerate(shares.index):
    plt.annotate(county, (pcs[i, 0], pcs[i, 1]), fontsize=8, xytext=(4, 4), textcoords='offset points')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
plt.title('County feedstock composition — PCA')
plt.axhline(0, color='#dddddd', lw=0.8)
plt.axvline(0, color='#dddddd', lw=0.8)
plt.tight_layout()
plt.savefig('pca_output.png', dpi=200)
print("Saved: pca_output.png")
