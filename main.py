"""A one-joke stamper for the make.fun demo-joke bounty.

This module carries exactly one punchline about sharing a desk with an
AI coding agent. Before anything is written, the line is measured
against the house gate: at least one and at most 280 Unicode characters,
and more than blank space. The line is then stamped as UTF-8 into
entry.txt inside the output directory, with no trailing newline, so the
file holds precisely the joke. Identical input means identical bytes on
every run.
"""

import os
import sys
from pathlib import Path

ONE_LINER = (
    "My AI coding agent commits 'fix stuff', pushes to main at 2 a.m., "
    "and skips the tests \u2014 turns out I didn't hire a pair programmer, "
    "I adopted a raccoon with a keyboard."
)

FLOOR_CHARS = 1
CEILING_CHARS = 280
TARGET_NAME = "entry.txt"
FALLBACK_DIR = "/output"


def _complaint(line: str) -> str | None:
    """Name the gate rule a line breaks, or None when the line passes."""
    if not line.strip():
        return "joke is blank or whitespace only"
    size = len(line)
    if size < FLOOR_CHARS:
        return f"joke too short: {size} characters"
    if size > CEILING_CHARS:
        return f"joke too long: {size} characters (limit {CEILING_CHARS})"
    return None


def _where_to_write() -> Path:
    picked = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR
    return Path(picked) / TARGET_NAME


def stamp_joke() -> int:
    flaw = _complaint(ONE_LINER)
    if flaw is not None:
        print(f"refusing to write entry: {flaw}", file=sys.stderr)
        return 1
    destination = _where_to_write()
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = ONE_LINER.encode("utf-8")
    destination.write_bytes(payload)
    if destination.read_bytes() != payload:
        print(f"written file does not match joke: {destination}", file=sys.stderr)
        return 1
    print(f"wrote {len(ONE_LINER)} characters to {destination}")
    return 0


raise SystemExit(stamp_joke())
