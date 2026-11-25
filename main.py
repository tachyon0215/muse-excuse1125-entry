#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The Excuse My Agent Gave Me": The excuse is caused by the machine's own condition twice over - a rate limit, then the self-defeating choice to burn its last tokens on a longer apology - delivered as a straight-faced apology whose punch lands in the final clause.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'Apologies for the delay: I hit my rate limit, then spent my remaining tokens writing you a longer apology about it.'
TEXT = LINE + "\n"
MAX_CHARS = 200
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
