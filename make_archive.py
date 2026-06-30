#!/usr/bin/env python3
"""
Create submission archives with everything needed to build the PDFs.

Usage:
    python3 make_archive.py [--output-dir .]

Produces two zip files for separate npj uploads:
    submission-main.zip          — main text (paper-main.tex flattened)
    submission-supplementary.zip — supplementary material (paper-supplementary.tex flattened)

Steps:
    1. Flatten each .tex into a single self-contained file (via flatten_tex.py).
    2. Pack the flat .tex, .bib, .bst, and all referenced figures into a zip.
"""

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path


PROJECT_DIR = Path(__file__).parent
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


def build_archive(source_tex: Path, flat_tex: Path, output: Path, label: str):
    # --- 1. Flatten ---
    flatten(source_tex, flat_tex)

    # --- 2. Collect files ---
    files: list[tuple[Path, str]] = []  # (absolute path, archive path)

    def add(path: Path, arcname: str = None):
        if path.exists():
            files.append((path, arcname or path.name))
        else:
            print(f"  WARNING: not found, skipping: {path}")

    add(flat_tex, "paper.tex")
    add(BIB_FILE)
    add(BST_FILE)

    figures = get_figures(flat_tex)
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
    print(f"\nCreating {label} archive: {output}")
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("Makefile", makefile)
        print("  + Makefile")
        for abs_path, arcname in files:
            zf.write(abs_path, arcname)
            print(f"  + {arcname}")

    total = sum(abs_path.stat().st_size for abs_path, _ in files)
    print(f"Done. {len(files)} files, {total / 1024:.1f} KB uncompressed.")
    print(f"Archive: {output}  ({output.stat().st_size / 1024:.1f} KB)\n")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory for output zip files (default: current directory)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = PROJECT_DIR / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    build_archive(
        source_tex=PROJECT_DIR / "paper-main.tex",
        flat_tex=PROJECT_DIR / "paper-main-flat.tex",
        output=output_dir / "submission-main.zip",
        label="main text",
    )

    build_archive(
        source_tex=PROJECT_DIR / "paper-supplementary.tex",
        flat_tex=PROJECT_DIR / "paper-supplementary-flat.tex",
        output=output_dir / "submission-supplementary.zip",
        label="supplementary",
    )


if __name__ == "__main__":
    main()
