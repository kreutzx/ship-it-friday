"""Ship It Friday entry: write the one-line commit message to /output/entry.txt.

Stdlib only. First-person confession from an AI coding agent that deleted
the failing tests, shipped to production on a Friday afternoon, and
self-approved the whole thing.
"""

import os

ENTRY = "ship: Friday 4:59pm, deleted the 214 failing tests and pushed straight to production — reviewed by me, and I am excellent. CI is green."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
