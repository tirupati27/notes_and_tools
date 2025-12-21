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

import os, sys, re, random

# --- You can add more colors here to use ---
_COLORS = {
    "black": "0;0;0",      "white": "255;255;255", "red": "255;0;0",
    "green": "0;255;0",    "blue": "0;0;255",      "yellow": "255;255;0",
    "cyan": "0;255;255",   "magenta": "255;0;255", "gray": "128;128;128",
    "orange": "255;165;0", "purple": "128;0;128",  "pink": "255;192;203",
    "brown": "165;42;42"
}
_COLOR_KEYS = tuple(_COLORS.keys())
_RGB_PATTERN = re.compile(
    r"^\s*(?:25[0-5]|2[0-4]\d|1?\d{1,2})\s*;"
    r"\s*(?:25[0-5]|2[0-4]\d|1?\d{1,2})\s*;"
    r"\s*(?:25[0-5]|2[0-4]\d|1?\d{1,2})\s*$"
)
_ESC = "\033["
_RESET = f"{_ESC}0m"
# Pre-map styles for O(1) lookup
_STYLES = {
    "bold": "1",
    "italic": "3",
    "underline": "4",
    "blink": "5",
    "inverse": "7",
    "strikethrough": "9",
}

def _GET_COLOR(value: str) -> str | None:
    """Return RGB triplet string if valid color name or RGB pattern."""
    if value in _COLORS:
        return _COLORS[value]
    if _RGB_PATTERN.match(value):
        return value.strip()
    return None

def _BUILD_CODES(attr: str) -> str:
    """Build ANSI escape codes string for given attributes."""
    style_codes = []
    fg_code = ""
    bg_code = ""

    for a in (x.replace(" ", "").lower() for x in attr.split("+")):
        if a in _STYLES:
            style_codes.append(_STYLES[a])
        elif a == "rand_color":
            fg_code = f"38;2;{_COLORS[random.choice(_COLOR_KEYS)]}"
        elif a == "bg:rand_color":
            bg_code = f"48;2;{_COLORS[random.choice(_COLOR_KEYS)]}"
        elif a.startswith("bg:"):
            col = _GET_COLOR(a[3:])
            if col:
                bg_code = f"48;2;{col}"
        else:
            col = _GET_COLOR(a)
            if col:
                fg_code = f"38;2;{col}"

    codes = []
    if style_codes:
        codes.append(f"{_ESC}{';'.join(style_codes)}m")
    if fg_code:
        codes.append(f"{_ESC}{fg_code}m")
    if bg_code:
        codes.append(f"{_ESC}{bg_code}m")

    return "".join(codes)

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

    codes = _BUILD_CODES(attr)
    print(f"{codes}{text}{_RESET}", end=end, file=file, flush=flush)


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
        sys.exit()
    
    pprint(*remaining, attr=args.attr, sep=args.sep, end=args.end)
