#!/usr/bin/env python3
r"""
Create submission archives with everything needed to build the PDFs.

Usage:
    python3 scripts/make_archive.py [--output-dir .]

Produces two zip files for separate npj uploads:
    submission-main.zip          — main text (paper.tex flattened without appendix)
    submission-supplementary.zip — supplementary material (appendix.tex standalone)

Steps:
    1. Flatten project-local \input and \include commands into one .tex file.
    2. Pack the flat .tex, .bib, .bst, and all referenced figures into a zip.
"""

import argparse
import re
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
PAPER_FILE = PROJECT_DIR / "paper.tex"
APPENDIX_FILE = PROJECT_DIR / "appendix.tex"
BIB_FILE = PROJECT_DIR / "paper.bib"
BST_FILE = PROJECT_DIR / "naturemag.bst"
INCLUDE_APPENDIX_DEFAULT = r"\providecommand{\includeappendix}{true}"
EXCLUDE_APPENDIX_DEFAULT = r"\providecommand{\includeappendix}{false}"
INPUT_RE = re.compile(
    r"^(?P<indent>\s*)\\(?P<command>input|include)\{(?P<target>[^}]+)\}(?P<tail>.*)$"
)


def tex_path(base_dir: Path, target: str) -> Path:
    path = Path(target.strip())
    if path.suffix != ".tex":
        path = path.with_suffix(".tex")
    if not path.is_absolute():
        path = base_dir / path
    return path.resolve()


def flatten_tex(
    source: Path, include_appendix: bool, stack: tuple[Path, ...] = ()
) -> str:
    """Return source with project-local \\input and \\include commands expanded."""
    source = source.resolve()
    if source in stack:
        chain = " -> ".join(path.name for path in (*stack, source))
        raise RuntimeError(f"recursive TeX include detected: {chain}")

    output = []
    for line in source.read_text().splitlines(keepends=True):
        match = INPUT_RE.match(line)
        if not match:
            output.append(line)
            continue

        child = tex_path(source.parent, match.group("target"))
        if child == APPENDIX_FILE.resolve() and not include_appendix:
            continue
        if not child.exists():
            raise FileNotFoundError(f"{source}: included TeX file not found: {child}")

        output.append(
            f"% Begin expanded {match.group('command')}{{{match.group('target')}}}\n"
        )
        output.append(flatten_tex(child, include_appendix, (*stack, source)))
        output.append(
            f"% End expanded {match.group('command')}{{{match.group('target')}}}\n"
        )

    return "".join(output)


def main_text_tex() -> str:
    content = flatten_tex(PAPER_FILE, include_appendix=False)
    return content.replace(INCLUDE_APPENDIX_DEFAULT, EXCLUDE_APPENDIX_DEFAULT)


def supplementary_tex() -> str:
    paper = PAPER_FILE.read_text()
    preamble, _, _ = paper.partition(r"\begin{document}")
    if not preamble:
        raise RuntimeError(f"could not find LaTeX preamble in {PAPER_FILE}")

    preamble = preamble.replace(INCLUDE_APPENDIX_DEFAULT, EXCLUDE_APPENDIX_DEFAULT)
    appendix = flatten_tex(APPENDIX_FILE, include_appendix=True)
    return (
        preamble
        + "\\begin{document}\n\n"
        + appendix
        + "\n\\bibliographystyle{naturemag}\n"
        + "\\bibliography{paper}\n\n"
        + "\\end{document}\n"
    )


def get_figures(content: str) -> list[Path]:
    """Return all unique paths referenced by \\includegraphics in the tex content."""
    pattern = r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}"
    seen = set()
    paths = []
    for match in re.finditer(pattern, content):
        p = Path(match.group(1))
        if p not in seen:
            seen.add(p)
            paths.append(p)
    return paths


def build_archive(tex_content: str, output: Path, label: str):
    files: list[tuple[Path, str]] = []  # (absolute path, archive path)

    def add(path: Path, arcname: str | None = None):
        if path.exists():
            files.append((path, arcname or path.name))
        else:
            print(f"  WARNING: not found, skipping: {path}")

    add(BIB_FILE)
    add(BST_FILE)

    figures = get_figures(tex_content)
    for fig in figures:
        if fig.is_absolute() or ".." in fig.parts:
            print(f"  WARNING: unsafe figure path, skipping: {fig}")
            continue
        add(PROJECT_DIR / fig, str(fig))

    makefile = (
        "all: paper.pdf\n\n"
        "paper.pdf: paper.tex paper.bib naturemag.bst\n"
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
        zf.writestr("paper.tex", tex_content)
        print("  + paper.tex")
        zf.writestr("Makefile", makefile)
        print("  + Makefile")
        for abs_path, arcname in files:
            zf.write(abs_path, arcname)
            print(f"  + {arcname}")

    total = len(tex_content.encode()) + len(makefile.encode())
    total += sum(abs_path.stat().st_size for abs_path, _ in files)
    print(f"Done. {len(files) + 2} files, {total / 1024:.1f} KB uncompressed.")
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
        tex_content=main_text_tex(),
        output=output_dir / "submission-main.zip",
        label="main text",
    )

    build_archive(
        tex_content=supplementary_tex(),
        output=output_dir / "submission-supplementary.zip",
        label="supplementary",
    )


if __name__ == "__main__":
    main()
