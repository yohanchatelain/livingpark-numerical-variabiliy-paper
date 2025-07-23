#!/usr/bin/env python3
"""
Generate a jet colorbar from 0 to 0.5 with 0.1 steps and save as PDF.
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 3))

# Define the colorbar range and ticks
vmin, vmax = 0, 0.5
ticks = np.arange(vmin, vmax + 0.1, 0.1)

# Create a colorbar using jet colormap
cmap = plt.cm.jet
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

# Create the colorbar
cbar = plt.colorbar(
    plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation="horizontal"
)

# Set the ticks and labels
cbar.set_ticks(ticks)
cbar.set_ticklabels([f"{tick:.1f}" for tick in ticks])

# Remove the main axis
ax.remove()

# Set title
# cbar.set_label('NAVR Values', fontsize=12, fontweight='bold')

# Adjust layout
plt.tight_layout()

# Save as PDF
plt.savefig("jet_colorbar.pdf", bbox_inches="tight", dpi=300)
print("Jet colorbar saved as 'jet_colorbar.pdf'")

# Optionally display
# plt.show()
