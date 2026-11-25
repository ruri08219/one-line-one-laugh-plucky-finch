#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one funny line of at most 200 characters to /output/entry.txt.
The line is:

    My microwave beeped at 3am to announce the popcorn was ready.
    The popcorn was ready at 9pm. It just wanted company.

One concrete scene (microwave, 3am, popcorn), one reversal (the popcorn
was done hours ago), one landing line (it just wanted company).
"""
import os
import sys

ENTRY = "My microwave beeped at 3am to announce the popcorn was ready. The popcorn was ready at 9pm. It just wanted company."
MAX_CHARS = 200


def resolve_output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "/output/entry.txt"


def main():
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text)),
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line (no newline characters)", file=sys.stderr)
        return 1
    if "\t" in text:
        print("entry must not contain tab characters", file=sys.stderr)
        return 1
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.replace(tmp_path, path)
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
