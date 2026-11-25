"""Describe Your Ex in One Word — make.fun entry.

The verdict: "Unsubscribe".

An ex is a newsletter you never signed up for in the first place:
endless updates you did not ask for, and the only sane response
is the little link at the bottom. One click, no reply-all, gone
from the inbox forever. The joke lands with the word itself —
everyone has hit unsubscribe, and everyone wishes it worked
on people too.
"""

import os

ENTRY = "Unsubscribe"


def main() -> None:
    """Write the single-word verdict to entry.txt as UTF-8."""
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
