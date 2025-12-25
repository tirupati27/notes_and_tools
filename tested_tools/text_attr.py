#!/usr/bin/env python3
"""
====================================
    Terminal Text Styling Utility
====================================

Note: The `pprint()` function is exactly same as builtin `print()` only one difference is
the `pprint()` has `attr` argument

1. IMPORT AND USE
-----------------
    from text_attr import pprint

    pprint("Hello", "World" attr="bold+red")
    pprint("Warning!", attr="underline+bg:yellow + italic")
    pprint("Info with background", attr="blue+bg:yellow")
    pprint("Random Color Text", attr="rand_color")
    pprint("Custom RGB", attr="bg:128;64;32+italic")

2. RUN FROM TERMINAL
-----------------

    python text_attr.py --attr "underline+bg:yellow + italic" "Warning!"
    python text_attr.py "more" "than" --attr "bold+red" "one" "text"
    python text_attr.py "Info with background" --attr "blue+bg:yellow"
    python text_attr.py "Random Color Text" --attr "rand_color"
    python text_attr.py "Custom RGB" --attr "bg:128;64;32+italic"

3. VALUE OF `attr` ARGUMENT
-----------------------
Text styles:
    bold       - Bold text
    italic     - Italic text
    underline  - Underlined text
    strikethrough - strike text
    blink      - blink text (not supported by some terminal)
    inverse    - inverse (not supported by some terminal)

Foreground colors:
    <color-name>   - Any color defined in your JSON database
    <r;g;b>        - RGB color code e.g. 255;0;200
    rand_color     - Pick a random color from the JSON database

Background colors:
    bg:<color-name>    - Background with a specific color
    bg:<r;g;b>         - RGB color code e.g. 255;0;200
    bg:rand_color      - Random background color
"""

import os, sys
from build_ansi_escape_code import build_ansi_escape_code

def pprint(*args, attr: str | None = None,
           sep: str = ' ', end: str = '\n',
           file=None, flush: bool = False) -> None:
    """Print with ANSI styles/colors, optimized for performance."""
    if file is None:
        file = sys.stdout

    text = sep.join(map(str, args))
    # Disable all color output when env has `NO_COLOR=1` (useful for scripts or CI pipelines)
    if not attr or os.getenv("NO_COLOR"):
        print(text, end=end, file=file, flush=flush)
        return

    ansi_code = build_ansi_escape_code(attr)
    if ansi_code:
        text = f"\033[{ansi_code}m{text}\033[0m"
    print(text, end=end, file=file, flush=flush)


if __name__ == "__main__":
    import argparse
    import sys

    p = argparse.ArgumentParser(description="Terminal Text Styling Utility")
    p.add_argument(
        "--attr",
        default=None,
        help="Text attributes like `bg:128;64;32+italic`, `blue+bg:yellow`, `bold+red`, `rand_color+bold`, etc."
    )
    p.add_argument(
        "--sep",
        default="-",
        help="Value of `sep` argument in `print()` function"
    )
    p.add_argument(
        "--end",
        default="\n",
        help="Value of `end` argument in `print()` function"
    )
    p.add_argument(
        "--usage",
        action="store_true",
        help="Show usage information"
    )
    args, remaining = p.parse_known_args()

    if args.usage:
        print(__doc__)
        sys.exit(0)
    if not remaining:
        p.error("at least one text argument is required")
        sys.exit(1)
    
    pprint(*remaining, attr=args.attr, sep=args.sep, end=args.end)
