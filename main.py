#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun bounty entry.

A single funny remark in the voice of a smug self-checkout machine,
written to the output file the grader reads. Stdlib only.
"""

import os

# One line, at most 200 characters: the machine's verdict on a basket
# of twelve yoghurts and nothing else.
LINE = (
    "Twelve yoghurts, no spoon, no shame. "
    "I scanned your whole basket \u2014 the only cultured thing in it "
    "is the yoghurt."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Re-read and confirm the grader will see exactly this one line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match the entry line")


if __name__ == "__main__":
    main()
