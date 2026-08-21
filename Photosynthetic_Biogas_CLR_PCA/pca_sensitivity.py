import pandas as pd
import numpy as np

clr = pd.read_csv("clr_matrix_A.csv", index_col=0)

def run_pca(data):
    centered = data - data.mean(axis=0)
    U, S, Vt = np.linalg.svd(centered.values, full_matrices=False)
    explained_var = (S ** 2) / np.sum(S ** 2)
    loadings = pd.DataFrame(Vt.T, index=data.columns,
                             columns=[f"PC{i+1}" for i in range(len(S))])
    return explained_var, loadings

print("=== FULL DATA (n=6) baseline ===")
ev_full, load_full = run_pca(clr)
print(f"PC1 explained: {ev_full[0]*100:.1f}%")
print("PC1 loadings:")
print(load_full["PC1"].round(3))
print()

# Leave-one-out: drop each condition once, rerun PCA, compare PC1 loadings
print("=== LEAVE-ONE-OUT CHECKS ===\n")
for cond in clr.index:
    subset = clr.drop(index=cond)
    ev, load = run_pca(subset)
    print(f"--- Without: {cond} (n={len(subset)}) ---")
    print(f"PC1 explained: {ev[0]*100:.1f}%")
    print("PC1 loadings:")
    print(load["PC1"].round(3))
    print()
