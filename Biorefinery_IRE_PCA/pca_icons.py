import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image, ImageDraw, ImageFont

res = pd.read_csv('pca_results.csv')

cluster_style = {
    0: ('🌲', 'Marginal / Energy-Forestry'),
    1: ('🌿', 'Grass-Dominant Pastoral'),
    2: ('🐄', 'Livestock-Intensive'),
    3: ('🌾', 'Arable / Tillage Belt'),
}

# only label counties you'll actually name in the call
labeled_counties = {'Cork', 'Dublin', 'Kildare', 'Wexford', 'Donegal',
                     'Kilkenny', 'Galway', 'Cavan', 'Meath', 'Louth'}

def emoji_to_image(emoji, size=160):
    font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", size)
    img = Image.new("RGBA", (size + 40, size + 40), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), emoji, font=font, embedded_color=True)
    return img

fig, ax = plt.subplots(figsize=(11, 8))

for cluster_num, (icon, label) in cluster_style.items():
    sub = res[res.Cluster == cluster_num]
    ax.scatter(sub.PC1, sub.PC2, s=0)
    img = emoji_to_image(icon)
    for _, row in sub.iterrows():
        ab = AnnotationBbox(OffsetImage(img, zoom=0.11), (row.PC1, row.PC2), frameon=False)
        ax.add_artist(ab)
        if row.County in labeled_counties:
            ax.annotate(row.County, (row.PC1, row.PC2), fontsize=8, xytext=(0, -15),
                        textcoords='offset points', ha='center', color='#222222',
                        fontweight='bold', zorder=4)

ax.axhline(0, color='#dddddd', lw=0.8, zorder=1)
ax.axvline(0, color='#dddddd', lw=0.8, zorder=1)
ax.set_xlabel('PC1 (40.7% variance)', fontsize=11)
ax.set_ylabel('PC2 (21.7% variance)', fontsize=11)
ax.set_title('County Feedstock Archetypes', fontsize=13)
ax.set_xlim(-2.2, 9)

legend_x = 6.8
legend_y_start = 2.8
for i, (cluster_num, (icon, label)) in enumerate(cluster_style.items()):
    small_img = emoji_to_image(icon, size=60)
    ab = AnnotationBbox(OffsetImage(small_img, zoom=0.22),
                         (legend_x, legend_y_start - i * 0.5), frameon=False)
    ax.add_artist(ab)
    ax.text(legend_x + 0.3, legend_y_start - i * 0.5, label, fontsize=8, va='center')

plt.tight_layout()
plt.savefig('pca_output_icons.png', dpi=200)
print("Saved: pca_output_icons.png")
