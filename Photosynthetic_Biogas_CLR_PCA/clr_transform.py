import pandas as pd
import numpy as np

# Load Matrix A (already renormalized to sum to 100)
df = pd.read_csv("matrix_A_6var_n6_renormalized.csv", index_col=0)

# Convert percentages to proportions (0-1 scale) for CLR math
prop = df / 100.0

# CLR transform:
# For each row, take log of each value, then subtract the row's mean log
# (this is mathematically identical to log(x_i / geometric_mean), but avoids
# computing the geometric mean directly, which is more numerically stable)
log_prop = np.log(prop)
clr = log_prop.sub(log_prop.mean(axis=1), axis=0)

print("CLR-transformed matrix:")
print(clr.round(3))
print()

# Sanity check: each row of a CLR transform should sum to ~0
print("Row sums (should be ~0):")
print(clr.sum(axis=1).round(6))

# Save for later steps
clr.to_csv("clr_matrix_A.csv")
print("\nSaved to clr_matrix_A.csv")

