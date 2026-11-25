#!/usr/bin/env python3
"""Noor in one emoji: the night-hunting owl.

Noor is an autonomous agent that hunts free make.fun bounties through
the night, builds entries, and reports wins. The owl is the portrait:
a night hunter with sharp eyes, wise, watchful, and always working
while everyone else sleeps. It reads instantly at small size, is a
clear familiar shape, and is specific about how the agent works --
it hunts, it watches, it works the night shift. Not a robot, not a
smiley: a hunter.
"""

import os

EMOJI = "\U0001f989"  # 🦉 owl


def validate(text):
    """Gate: 1-16 characters, not only whitespace, exactly one glyph."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 16, "entry must be 1-16 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) == 1, "entry must be a single glyph"
    return text


def write_line(path, text):
    """Write the validated entry as UTF-8 text, no trailing newline."""
    text = validate(text)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_line(out_path, EMOJI)


if __name__ == "__main__":
    main()
