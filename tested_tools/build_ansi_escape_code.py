import random
from validate_rgb import validate_rgb
"""
Some examples of using text attributes:
    "red"
    "red+underline"
    "bg: red + rand_color"
    "bold + italic + 255;0;100"
    "strikethrough + bg: rand_color"
    "255;100;40 + bg: 80;100;255 + italic"
    etc...
This is how you can use any combination of text attributes
"""

# --- You can add more colors here to use ---
_COLORS = {
    "black": "0;0;0",      "white": "255;255;255", "red": "255;0;0",
    "green": "0;255;0",    "blue": "0;0;255",      "yellow": "255;255;0",
    "cyan": "0;255;255",   "magenta": "255;0;255", "gray": "128;128;128",
    "orange": "255;165;0", "purple": "128;0;128",  "pink": "255;192;203",
    "brown": "165;42;42"
}

_C_VALUES = tuple(_COLORS.values())
_STYLES = {
    "bold": "1",
    "italic": "3",
    "underline": "4",
    "blink": "5",
    "inverse": "7",
    "strikethrough": "9",
}

def build_ansi_escape_code(attr: str) -> str:
    """
Build ANSI escape codes string for given attributes.
Returns:
        - Numeric part of ANSI code (\\033['__THIS-PART__'m): if user passed a meaningful attr.
        - empty string: if user passed meaningless attr."""
    codes = set()
    for a in (x for x in attr.replace(" ", "").lower().split("+")):
        if a in _STYLES:
            codes.add(_STYLES[a])
        elif a == "rand_color":
            codes.add(f"38;2;{random.choice(_C_VALUES)}")
        elif a == "bg:rand_color":
            codes.add(f"48;2;{random.choice(_C_VALUES)}")
        # seeking for 'bg:255;20;50' or 'bg:red'
        elif a.startswith("bg:"):
            c = a[3:]
            if c in _COLORS:
                codes.add(f"48;2;{_COLORS[c]}")
            else:
                c = validate_rgb(c)
                if c:
                    codes.add(f"48;2;{c}")
        # seeking for '255;20;50' or 'green'
        else:
            if a in _COLORS:
                codes.add(f"38;2;{_COLORS[a]}")
            else:
                a = validate_rgb(a)
                if a:
                    codes.add(f"38;2;{a}")

    if codes:
        return ";".join(codes)
    return ""