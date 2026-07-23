#!/usr/bin/env python3
"""Flatten a LaTeX document by inlining all \\input and \\include commands."""

import re
import sys
from pathlib import Path


def flatten_tex(file_path: Path, base_dir: Path, visited: set = None) -> str:
    """Read a TeX file and recursively replace \\input and \\include with content."""
    if visited is None:
        visited = set()

    resolved = file_path.resolve()
    if resolved in visited:
        print(f"Warning: circular \\input/\\include detected for {file_path}, skipping.", file=sys.stderr)
        return ""
    visited.add(resolved)

    content = file_path.read_text()

    def replace_cmd(match):
        arg = match.group(1)  # filename, possibly without .tex
        included = base_dir / (arg if arg.endswith(".tex") else arg + ".tex")
        if included.exists():
            return "\n" + flatten_tex(included, base_dir, visited) + "\n"
        else:
            print(f"Warning: file not found: {included}, leaving command as-is.", file=sys.stderr)
            return match.group(0)

    # Replace \input{...} and \include{...} (but not \includegraphics, etc.)
    pattern = r"\\(?:input|include)\{([^}]+)\}"
    return re.sub(pattern, replace_cmd, content)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input.tex> [output.tex]")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_file.with_stem(input_file.stem + "-flat")

    base_dir = input_file.parent
    flattened = flatten_tex(input_file, base_dir)
    output_file.write_text(flattened)
    print(f"Flattened output written to: {output_file}")


if __name__ == "__main__":
    main()
