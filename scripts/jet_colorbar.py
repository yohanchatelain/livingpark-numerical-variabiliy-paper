#!/usr/bin/env python3
"""
Generate a jet colorbar with configurable vmin/vmax/step and save as PDF.

Usage:
    ./generate_colorbar.py --vmax 1.0
    ./generate_colorbar.py --vmin 0 --vmax 0.5 --step 0.1 --out jet.pdf
"""

import argparse
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Generate a jet colorbar PDF.")
    parser.add_argument("--vmin", type=float, default=0.0, help="Minimum value (default: 0.0)")
    parser.add_argument("--vmax", type=float, default=0.5, help="Maximum value (default: 0.5)")
    parser.add_argument("--step", type=float, default=0.1, help="Tick step size (default: 0.1)")
    parser.add_argument("--out", type=str, default="jet_colorbar.pdf", help="Output PDF filename")
    args = parser.parse_args()

    vmin, vmax, step = args.vmin, args.vmax, args.step

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 3))

    # Define ticks
    ticks = np.arange(vmin, vmax + step * 0.99999, step)

    # Define colormap
    cmap = plt.cm.jet
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

    # Create colorbar
    cbar = plt.colorbar(
        plt.cm.ScalarMappable(norm=norm, cmap=cmap), 
        ax=ax, 
        orientation="horizontal"
    )

    # Configure ticks
    cbar.set_ticks(ticks)
    cbar.set_ticklabels([f"{t:.1f}" for t in ticks])

    # Remove plot axis (you only want the colorbar)
    ax.remove()

    # Layout
    plt.tight_layout()

    # Save
    plt.savefig(args.out, bbox_inches="tight", dpi=300)
    print(f"Jet colorbar saved as '{args.out}'")

    # Optional display
    # plt.show()


if __name__ == "__main__":
    main()
