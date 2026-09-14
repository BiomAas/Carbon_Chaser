import matplotlib.pyplot as plt
import numpy as np

responses = ["dE_wash_1st", "dE_wash_3rd", "L"]

# from your printed output
chitosan_effect  = [4.4, 10.8, 4.6]   # abs value of BML2ref -> BML2
lignin_effect    = [0.7, 2.7, 8.4]    # abs value of BML2 -> BML4
particle_spread  = [0.5, 1.2, 4.5]    # spread across BML2/USL2/CLNP2

x = np.arange(len(responses))
width = 0.25

fig, ax = plt.subplots(figsize=(7,5))
fig.patch.set_facecolor("#1a1a1a")
ax.set_facecolor("#1a1a1a")

ax.bar(x - width, chitosan_effect, width, label="Chitosan on/off", color="#8B0000")        # dark/blood red
ax.bar(x,          lignin_effect,   width, label="Lignin 2%→4%",    color="#800020")        # burgundy
ax.bar(x + width,  particle_spread, width, label="Particle type spread", color="#DC143C")   # crimson

ax.set_xticks(x)
ax.set_xticklabels(["Wash ΔE* (1st)", "Wash ΔE* (3rd)", "L* (lightness)"])
ax.set_ylabel("Effect size")
ax.set_title("Which factor moves which property?")

ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")
for spine in ax.spines.values():
    spine.set_color("white")

legend = ax.legend()
legend.get_frame().set_facecolor("#1a1a1a")
for text in legend.get_texts():
    text.set_color("white")

plt.tight_layout()
plt.savefig("effect_sizes.png", dpi=150)
print("Saved effect_sizes.png")
