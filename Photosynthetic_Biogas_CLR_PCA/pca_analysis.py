import pandas as pd
import numpy as np

clr = pd.read_csv("clr_matrix_A.csv", index_col=0)

# Center (do NOT scale to unit variance - standard for compositional/Aitchison PCA)
centered = clr - clr.mean(axis=0)

# PCA via SVD
U, S, Vt = np.linalg.svd(centered.values, full_matrices=False)

# Explained variance
explained_var = (S ** 2) / np.sum(S ** 2)

# Scores (condition positions in PC space) and loadings (variable directions)
scores = pd.DataFrame(
    U * S,
    index=clr.index,
    columns=[f"PC{i+1}" for i in range(len(S))]
)
loadings = pd.DataFrame(
    Vt.T,
    index=clr.columns,
    columns=[f"PC{i+1}" for i in range(len(S))]
)

print("=== Explained variance ratio by component ===")
for i, v in enumerate(explained_var):
    print(f"PC{i+1}: {v*100:.1f}%")
print(f"\nPC1 + PC2 combined: {(explained_var[0]+explained_var[1])*100:.1f}%")

print("\n=== Scores (condition positions) ===")
print(scores.round(3))

print("\n=== Loadings (variable contributions) ===")
print(loadings.round(3))

scores.to_csv("pca_scores.csv")
loadings.to_csv("pca_loadings.csv")
print("\nSaved pca_scores.csv and pca_loadings.csv")
