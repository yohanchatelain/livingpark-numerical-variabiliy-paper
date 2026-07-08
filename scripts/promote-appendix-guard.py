#!/usr/bin/env python3
"""Promote the appendix out of its \\ifthenelse guard, in place.

paper.tex includes the appendix as the brace-group argument of
``\\ifthenelse{\\equal{\\includeappendix}{true}}{ \\include{appendix} }{}``.
latexdiff treats a command-argument brace group as one opaque block, so it can
never produce word-level markup for the appendix. This script rewrites the
guard to a bare ``\\include{appendix}`` so that, once flattened, the appendix
sits at the top level of the document and is diffed like the main text.

It must run *before* flattening, while the guarded text is still the short
``\\include{appendix}`` (the regex would not survive the appendix being inlined).
The diff PDF is always built with the appendix on, so dropping the condition is
safe. The regex targets only the appendix guard: the other \\includeappendix
conditional in the preamble wraps \\newcommand definitions, not \\include, and
is left untouched.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

GUARD_PATTERN = re.compile(
    r"\\ifthenelse\{\\equal\{\\includeappendix\}\{true\}\}\{\s*"
    r"\\include\{appendix\}\s*"
    r"\}\{\}"
)
GUARD_REPLACEMENT = "\\include{appendix}"


def promote(text: str) -> str:
    return GUARD_PATTERN.sub(lambda _match: GUARD_REPLACEMENT, text)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: promote-appendix-guard.py PAPER_TEX", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    path.write_text(promote(path.read_text(encoding="utf-8")), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
