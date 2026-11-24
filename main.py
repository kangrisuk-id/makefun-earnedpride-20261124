#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to entry.txt: a quiet,
earned moment of pride for someone in a scene. Pure standard library;
no third-party packages, so it runs in the official grader image.

Output directory, first writable one wins:
  1. $MAKEFUN_OUTPUT_DIR (set by the grader)
  2. /output
  3. the directory beside this script
  4. /tmp
"""

import os
import sys

LINE = (
    "The grandmother who never learned to read signs her name in the "
    "wedding guest book, slowly, in letters she practiced all winter."
)


def candidate_dirs():
    seen = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        seen.append(env_dir)
    seen.append("/output")
    seen.append(os.path.dirname(os.path.abspath(__file__)))
    seen.append("/tmp")
    unique = []
    for path in seen:
        if path and path not in unique:
            unique.append(path)
    return unique


def main() -> int:
    assert 1 <= len(LINE) <= 240, "entry line must be 1-240 characters"
    errors = []
    for out_dir in candidate_dirs():
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(LINE)
            return 0
        except OSError as exc:  # try the next candidate directory
            errors.append(f"{out_dir}: {exc}")
    for err in errors:
        print(f"could not write entry.txt in {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
