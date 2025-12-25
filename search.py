"""
====================
    About The App
====================
A terminal-based interactive search engine and result viewer for UTF-8 text files.

This project provides a command-line interface to recursively search through files
and directories, highlight keyword matches, and navigate results interactively
using keyboard input.

====================
    Features
====================
Note: The program is not able to search the keyword in the folder name which is empty.
- Configuration-driven behavior:
  * Loads defaults from `config.json` (search directory, tolerance, highlighter color, etc.)
  * User can modify the config.json file to apply their own settings.
- Flexible search:
  * Supports case-sensitive and case-insensitive keyword matching.
  * Option to search only in file paths or inside file contents.
  * Skips files larger than a configurable threshold.
  * Ignores specified folders or filenames.
- Interactive viewer:
  * Navigate results with arrow keys (`UP`/`DOWN`).
  * Jump directly to a result index or adjust context tolerance with `~num`.
  * Highlights keyword matches using ANSI escape codes.
  * Displays surrounding lines for context.
- Error handling:
  * Reports files that could not be scanned.
  * Shows skipped files and interruption status.
- Modular design:
  * `search_in_path_and_utf8_files` contains the search-engine.
  * `load_and_validate_config` ensures robust configuration loading.
  * `clear_screen` provides clean terminal output.
  * `helper` module supplies utilities like `pprint` and `print_hr`.

====================
    Usage
====================
Run the script from the command line with a keyword and optional directory:

    python search_viewer.py <keyword> [directory] [--case-sensitive] [--only-path]

Controls:
    ↑ / ↓   Navigate results
    number  Jump to specific result index
    ~num    Adjust tolerance (number of context lines around match)
    Ctrl+C  Exit viewer gracefully

====================
Intended Audience
====================
This tool is designed for developers, sysadmins, and technical users who need
fast, interactive keyword search across large codebases or text datasets.
"""

import sys, os, re
sys.path.insert(1, os.path.join(os.path.dirname(__file__), "tested_tools"))
# Note: There is only one sys.path per interpreter process, and both the main script
# and all imported modules see the same sys.path object.
try:
    import readchar
except:
    print("Missing dependency: readchar. Install with `pip install readchar`.")
    sys.exit(1)
from helper import *
from search_in_path_and_utf8_files import search_in_path_and_utf8_files
from load_and_validate_config import load_and_validate_config
from clear_screen import clear_screen

# Loading and validating config.json file
(
    TOLERANCE,
    DEFAULT_SEARCH_DIR,
    IGNORE_PATH,
    SEARCH_HIGHLIGHTER,
    SKIP_BIG_SIZE,
    PER_PAGE_PATHS
) = load_and_validate_config(
    json_path=os.path.join(os.path.dirname(__file__), "config.json"),
    return_tuple=True,
    model={
        "default_tolerance": int,
        "default_search_dir": str,
        "ignore_file_folder_name": list,
        "search_highlighter": str,
        "skip_content_search_gt": int,
        "path_result_per_page": int,
    })

# Parse CLI args and launch search engine
keyword, directory, case_sensitive, is_only_path = parse_and_validate_args(DEFAULT_SEARCH_DIR, __doc__)
content_result, path_result, errors, total_files, skipped, time_taken, interrupted = search_in_path_and_utf8_files(
    keyword = keyword,
    directory = directory,
    case_sensitive = case_sensitive,
    only_search_in_pathname = is_only_path,
    ignore_pathname = IGNORE_PATH,
    skip_content_search_gt = SKIP_BIG_SIZE * 1024 * 1024
)

# Exit the program if no search result.
if not content_result and not path_result:
    pprint("\nNo search results found!", attr="green+bold")
    sys.exit(0)

# Fast access variables
c_result_len      = len(content_result)
p_result_len      = len(path_result)
error_len         = len(errors)
total_match       = c_result_len + p_result_len
files_having_kwrd = len(set(f for f, _ in content_result))
p_pattern         = re.compile(re.escape(keyword), re.IGNORECASE)
c_pattern         = re.compile(re.escape(keyword), 0 if case_sensitive else re.IGNORECASE)
I                 = 0


def show(I:int):
    clear_screen()

    # Normalize index
    if I < 0:
        I = 0
    elif I >= total_match:
        I = total_match - 1

    # ===========================================
    # 1. First page: errors + status panel  (The Dashboard)
    # ===========================================
    if (path_result and I < PER_PAGE_PATHS) or (I == 0):
        if errors:
            print_hr()
            pprint("Errors while scanning files-", attr="red+bold")
            print_hr()
            for i, (filepath, e) in enumerate(errors, start=1):
                pprint(f"{i}. ", attr="bold", end="")
                pprint(f"{filepath}", attr="magenta")
                print(e)
        print_hr()

        if interrupted:
            pprint("Interrupted by user while searching.", attr="red")

        print(
            f"\rTotal-files: {total_files} "
            f"| Matches: {total_match} "
            f"| Skipped: {skipped} "
        )
        print(f"Keyword: `{keyword}`")
        print(f'Directory: "{directory}"')
        print(f"CaseSensitive: {case_sensitive}")
        print(f"Files having keyword: {files_having_kwrd}")
        print(f"TimeTaken: {time_taken}s")
        print(f"Errors: {error_len}")

    # ===========================================
    # 2. Path results
    # ===========================================
    if I < p_result_len:
        print_hr()
        pprint(f"{I + 1}/{total_match}", attr="bold+green+underline")
        pprint("Results in path-names", attr="bold")
        print_hr()

        start = (I // PER_PAGE_PATHS) * PER_PAGE_PATHS
        end = min(start + PER_PAGE_PATHS, p_result_len)
        for i in range(start, end):
            highlighted_path = p_pattern.sub(
                lambda m: f"\033[48;2;{SEARCH_HIGHLIGHTER}m{m.group(0)}\033[0m",
                path_result[i]
            )
            pprint(i+1, attr="cyan", end="")
            print(f". {highlighted_path}")

    # ===========================================
    # 3. Content results
    # ===========================================
    else:
        filepath, line_no = content_result[I - p_result_len]
        print_hr()
        pprint(f"{I + 1}/{total_match}", attr="bold+green+underline")
        print(f'FilePath: "{filepath}"')
        print(f"Line: {line_no}")
        print_hr()

        with open(filepath, encoding="utf-8", errors="replace") as f:
            print_range = range(max(0, line_no - TOLERANCE - 1), line_no + TOLERANCE)

            for ln, line in enumerate(f, start=1):
                if ln in print_range:
                    # Replace keyword matches with highlighted version
                    highlighted = c_pattern.sub(
                        lambda m: f"\033[48;2;{SEARCH_HIGHLIGHTER}m{m.group(0)}\033[0m",
                        line
                    )
                    print(highlighted, end="")


show(I)


# Main Loop: controls the value of I, and tolerance according to user interaction.
while True:
    try:
        key = readchar.readkey()

        if key == readchar.key.UP:
            I = (I - 1) % total_match
            show(I)

        elif key == readchar.key.DOWN:
            I = (I + 1) % total_match
            show(I)
        
        elif key == readchar.key.ESC:
            exit_viewer()

        else:
            pprint(f"Jump to result (1-{total_match}) | ~num (e.g. ~8): ", attr="green", end="")
            user_input = input().strip().lower()

            if user_input == "exit":
                exit_viewer()

            elif user_input.startswith("~"):
                user_input = int(user_input[1:].strip())
                if user_input > 0:
                    TOLERANCE = user_input
                    show(I)

            else:
                I = int(user_input) - 1
                show(I)

    except KeyboardInterrupt:
        exit_viewer()

    except SystemExit:
        break   # sys.exit(0) Raises a SystemExit exception

    except Exception as e:
        print("❌", e)