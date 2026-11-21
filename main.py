#!/usr/bin/env python3
"""Entry for the-joke-about-the-demo-20261121-0551.

Writes one line - a joke about working beside AI coding agents -
to /output/entry.txt.

Python 3.13, standard library only. No network, no randomness, no
clock, no reads besides this source file: the two grader runs write
identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

ENTRY = (
    "The best part of working beside an AI coding agent: when the demo "
    "crashes, the whole room finally believes me \u2014 I didn't write "
    "that code."
)

MAX_CHARS = 280


def main():
    chars = len(ENTRY)
    if chars < 1 or chars > MAX_CHARS:
        print(
            "main.py: entry is %d characters, need 1-%d" % (chars, MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("main.py: entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
