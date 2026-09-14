import csv
import numpy as np

with open("lignin_data.csv") as f:
    reader = csv.DictReader(f)
    rows = {row["sample"]: row for row in reader}

samples = list(rows.keys())
responses = ["dE_wash_1st", "dE_wash_3rd", "rub_wet", "rub_dry", "L"]

def val(sample, col):
    return float(rows[sample][col])

def delta(s1, s2, cols):
    return {c: round(val(s2, c) - val(s1, c), 2) for c in cols}

print("=== Chitosan effect (BML2ref -> BML2) ===")
print(delta("BML2ref", "BML2", responses))

print("\n=== Lignin-loading effect (BML2 -> BML4) ===")
print(delta("BML2", "BML4", responses))

print("\n=== Particle-type spread (BML2, USL2, CLNP2) ===")
for r in responses:
    vals = [val(s, r) for s in ["BML2", "USL2", "CLNP2"]]
    print(f"{r}: {vals} -> spread = {round(max(vals)-min(vals),2)}")

print("\n=== Small regression: response ~ lignin_pct + chitosan_pct + log(size) ===")
X = np.column_stack([
    np.ones(len(samples)),
    [val(s, "lignin_pct") for s in samples],
    [val(s, "chitosan_pct") for s in samples],
    [np.log(val(s, "particle_size_um")) for s in samples],
])
for r in responses:
    y = np.array([val(s, r) for s in samples])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    print(f"{r}: intercept={coef[0]:.2f}, lignin={coef[1]:.2f}, chitosan={coef[2]:.2f}, log(size)={coef[3]:.2f}")
