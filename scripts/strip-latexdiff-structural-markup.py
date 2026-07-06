#!/usr/bin/env python3
"""Remove noisy latexdiff markup from structural LaTeX-only chunks."""

from __future__ import annotations

import sys
from pathlib import Path


DIFF_COMMANDS = ("\\DIFaddFL", "\\DIFdelFL", "\\DIFadd", "\\DIFdel")
REFERENCE_COMMANDS = (
    "\\ref",
    "\\eqref",
    "\\Cref",
    "\\cref",
    "\\autoref",
    "\\suppnoteref",
    "\\suppfigref",
    "\\supptabref",
    "\\suppequref",
    "\\mainsecref",
    "\\maintabref",
    "\\mainequref",
)
WHITESPACE_COMMANDS = ("\\ ", "\\@", "~")


def command_at(text: str, index: int) -> str | None:
    for command in DIFF_COMMANDS:
        if not text.startswith(command, index):
            continue

        next_index = index + len(command)
        if next_index < len(text) and (text[next_index].isalpha() or text[next_index] == "@"):
            continue
        return command

    return None


def brace_argument_end(text: str, open_brace: int) -> int | None:
    depth = 0
    index = open_brace

    while index < len(text):
        char = text[index]

        if char == "\\":
            index += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index

        index += 1

    return None


def is_structural_chunk(chunk: str) -> bool:
    stripped = chunk.lstrip()

    if stripped.startswith("$") or stripped.startswith("($"):
        return True

    if any(stripped.startswith(command) for command in REFERENCE_COMMANDS):
        return True

    return stripped.strip() in WHITESPACE_COMMANDS


def strip_markup(text: str) -> str:
    output: list[str] = []
    index = 0

    while index < len(text):
        command = command_at(text, index)
        if command is None:
            output.append(text[index])
            index += 1
            continue

        argument_start = index + len(command)
        if argument_start >= len(text) or text[argument_start] != "{":
            output.append(text[index])
            index += 1
            continue

        argument_end = brace_argument_end(text, argument_start)
        if argument_end is None:
            output.append(text[index])
            index += 1
            continue

        chunk = text[argument_start + 1 : argument_end]
        if not is_structural_chunk(chunk):
            output.append(text[index : argument_end + 1])
        elif command in ("\\DIFadd", "\\DIFaddFL"):
            output.append(chunk)

        index = argument_end + 1

    return "".join(output)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: strip-latexdiff-structural-markup.py DIFF_TEX", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    path.write_text(strip_markup(path.read_text(encoding="utf-8")), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
