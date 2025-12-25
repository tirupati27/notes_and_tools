def ansi_demo():
    styles = {
        'Reset': '0',
        'Bold': '1',
        'Italic': '3',
        'Underline': '4',
        'Inverse': '7',
        'Strikethrough': '9'
    }

    colors = {
        'Black': '30',
        'Red': '31',
        'Green': '32',
        'Yellow': '33',
        'Blue': '34',
        'Magenta': '35',
        'Cyan': '36',
        'White': '37'
    }

    print("=== ANSI Escape Code Demo ===\n")

    for style_name, style_code in styles.items():
        for color_name, color_code in colors.items():
            sequence = f"\033[{style_code};{color_code}m"
            print(f"{sequence}{style_name} {color_name}\033[0m")

    print("\n=== 256-Color Demo (Foreground only) ===")
    for i in range(0, 256):
        print(f"\033[38;5;{i}m{i:3}\033[0m", end=' ')
        if (i + 1) % 16 == 0:
            print()

if __name__ == "__main__":
    ansi_demo()