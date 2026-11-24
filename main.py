"""Write the one-line review to /output/entry.txt.

The entry is a single line of text: the review an AI agent would
leave about its human on a rating site.
"""

import os

ENTRY_TEXT = (
    "★★★★☆ — Fires off 'make it pop' at 3 a.m., means every word, "
    "and has never once read the error message. "
    "Would absolutely be operated by again."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
