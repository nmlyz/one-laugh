#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

The line is a single self-contained joke: a librarian, a fire alarm, and
a misunderstanding about what is sleeping and what is thinking.
Standard library only. Running it twice produces byte-identical output.
The output path follows OUTPUT_DIR when set, otherwise /output/entry.txt.
"""

import os

LINE = ("The librarian was fired for shushing the fire alarm; she said "
        "the books were sleeping and the smoke was just thinking out loud.")


def main():
    if not 1 <= len(LINE) <= 140:
        raise SystemExit("line must be 1-140 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
