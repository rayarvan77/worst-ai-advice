#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt, then self-checks it against the bounty gate:
UTF-8 text, 1 to 140 characters, a single non-blank line.

The joke: an AI assistant, totally confident, telling you to wrap your
router in tin foil because it "focuses" the Wi-Fi signal like a
satellite dish. Specific, followable, and completely wrong.
"""

import os
import sys

LINE = (
    "Certainly! Wrap your router in tin foil \u2014 it focuses the Wi-Fi "
    "signal like a satellite dish, so point the shiny side at your laptop."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Check the line against the bounty gate; exit non-zero on failure."""
    if not text:
        sys.exit("error: entry is empty")
    if text != text.strip():
        sys.exit("error: entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("error: entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        sys.exit("error: entry contains a control character")
    if len(text) > MAX_CHARS:
        sys.exit(f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if len(text) < 1:
        sys.exit("error: entry is shorter than 1 character")


def main() -> None:
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read it back and re-validate the exact bytes that were written.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        sys.exit("error: written entry does not match the validated line")
    validate(written)
    print(LINE)
    print(f"({len(LINE)} characters)", file=sys.stderr)


if __name__ == "__main__":
    main()
