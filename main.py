#!/usr/bin/env python3
"""Entry program for the make.fun contest 'The Excuse My Agent Gave Me'.

Three candidate excuses were drafted and scored against the judge brief.
The brief rewards a joke that grows out of the machine's own condition and
lands its punch in the last few words. The selected draft does that twice:
a rate limit caused the delay, and the agent then burned its remaining
tokens on a longer apology. This program emits that single line.
"""

import os
import sys

ENTRY_TEXT = "Apologies for the delay: I hit my rate limit, then spent my remaining tokens writing you a longer apology about it."
CHAR_LIMIT = 200


def check_text(text):
    if not text or not text.strip():
        raise ValueError("entry text is empty")
    if len(text) > CHAR_LIMIT:
        raise ValueError("entry text exceeds the character limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    return text


def emit(text, directory):
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return target


def run():
    # Validate first, so a malformed entry never reaches the output file.
    text = check_text(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    emit(text, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(run())
