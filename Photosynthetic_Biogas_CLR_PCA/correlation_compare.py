import pandas as pd
import numpy as np

raw = pd.read_csv("matrix_A_6var_n6_renormalized.csv", index_col=0)
clr = pd.read_csv("clr_matrix_A.csv", index_col=0)

print("=== RAW percentage correlation matrix ===")
raw_corr = raw.corr()
print(raw_corr.round(3))
print()

print("=== CLR-transformed correlation matrix ===")
clr_corr = clr.corr()
print(clr_corr.round(3))
print()

print("=== Protein vs Carbohydrate specifically ===")
print(f"Raw correlation:  {raw_corr.loc['Protein','Carb']:.3f}")
print(f"CLR correlation:  {clr_corr.loc['Protein','Carb']:.3f}")
print()

print("=== Protein vs EPS specifically ===")
print(f"Raw correlation:  {raw_corr.loc['Protein','EPS']:.3f}")
print(f"CLR correlation:  {clr_corr.loc['Protein','EPS']:.3f}")
print()

print("=== Carb vs EPS specifically ===")
print(f"Raw correlation:  {raw_corr.loc['Carb','EPS']:.3f}")
print(f"CLR correlation:  {clr_corr.loc['Carb','EPS']:.3f}")

raw_corr.to_csv("raw_correlation_matrix.csv")
clr_corr.to_csv("clr_correlation_matrix.csv")
