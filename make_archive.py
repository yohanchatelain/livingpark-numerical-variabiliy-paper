#!/usr/bin/env python3
"""
Create a submission archive with everything needed to build the PDF.

Usage:
    python3 make_archive.py [--output submission.zip]

Steps:
    1. Flatten paper.tex into a single .tex file (via flatten_tex.py).
    2. Pack the flat .tex, .bib, .bst, and all referenced figures into a zip.
"""

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path


PROJECT_DIR = Path(__file__).parent
FLAT_TEX = PROJECT_DIR / "paper-flat.tex"
BIB_FILE = PROJECT_DIR / "paper.bib"
BST_FILE = PROJECT_DIR / "naturemag.bst"


def flatten(source: Path, output: Path):
    flatten_script = PROJECT_DIR / "flatten_tex.py"
    print(f"Flattening {source.name} -> {output.name} ...")
    subprocess.run(
        [sys.executable, str(flatten_script), str(source), str(output)], check=True
    )


def get_figures(tex: Path) -> list[Path]:
    """Return all unique paths referenced by \\includegraphics in the tex file."""
    content = tex.read_text()
    pattern = r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}"
    seen = set()
    paths = []
    for match in re.finditer(pattern, content):
        p = Path(match.group(1))
        if p not in seen:
            seen.add(p)
            paths.append(p)
    return paths


def build_archive(output: Path):
    # --- 1. Flatten ---
    flatten(PROJECT_DIR / "paper.tex", FLAT_TEX)

    # --- 2. Collect files ---
    files: list[tuple[Path, str]] = []  # (absolute path, archive path)

    def add(path: Path, arcname: str = None):
        if path.exists():
            files.append((path, arcname or path.name))
        else:
            print(f"  WARNING: not found, skipping: {path}")

    add(FLAT_TEX, "paper.tex")
    add(BIB_FILE)
    add(BST_FILE)

    figures = get_figures(FLAT_TEX)
    for fig in figures:
        add(PROJECT_DIR / fig, str(fig))

    makefile = (
        "all: paper.pdf\n\n"
        "paper.pdf: paper.tex paper.bib\n"
        "\tpdflatex paper\n"
        "\tbibtex paper\n"
        "\tpdflatex paper\n"
        "\tpdflatex paper\n\n"
        "clean:\n"
        "\trm -f *.aux *.bbl *.blg *.log *.out paper.pdf\n"
    )

    # --- 3. Write zip ---
    print(f"\nCreating archive: {output}")
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("Makefile", makefile)
        print("  + Makefile")
        for abs_path, arcname in files:
            zf.write(abs_path, arcname)
            print(f"  + {arcname}")

    total = sum(abs_path.stat().st_size for abs_path, _ in files)
    print(f"\nDone. {len(files)} files, {total / 1024:.1f} KB uncompressed.")
    print(f"Archive: {output}  ({output.stat().st_size / 1024:.1f} KB)")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--output",
        default="submission.zip",
        help="Output archive name (default: submission.zip)",
    )
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = PROJECT_DIR / output

    build_archive(output)


if __name__ == "__main__":
    main()
