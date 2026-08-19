import pandas as pd
import numpy as np

# Load Matrix A
df = pd.read_csv("matrix_A_6var_n6_renormalized.csv", index_col=0)
print("Raw matrix A:")
print(df)
print()

# Confirm row sums are ~100
print("Row sums:")
print(df.sum(axis=1))

