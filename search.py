import sys, os
sys.path.insert(1, os.path.realpath(os.path.join(__file__, "..", "tested_tools")))
# Note: There is only one sys.path per interpreter process, and both the main script
# and all imported modules see the same sys.path object.

try:
    import readchar
except:
    print("Missing dependency: readchar. Install with `pip install readchar`.")
    sys.exit(1)
import re
from helper import *
from search_in_path_and_utf8_files import search_in_path_and_utf8_files
from load_and_validate_config import load_and_validate_config
from clear_screen import clear_screen

# Loading and validating config.json file
(
    DEFAULT_TOLERANCE,
    DEFAULT_SEARCH_DIR,
    IGNORE_PATH,
    SEARCH_HIGHLIGHTER,
    SKIP_BIG_SIZE,
    PER_PAGE_PATHS
) = load_and_validate_config(
    json_path="config.json",
    return_tuple=True,
    model={
        "default_tolerance": int,
        "default_search_dir": str,
        "ignore_file_folder_name": list,
        "search_highlighter": str,
        "skip_inside_search_bigger_than": int,
        "path_result_per_page": int,
    })

# Parse CLI args and launch search engine
keyword, directory, case_sensitive, is_only_path = parse_and_validate_args(DEFAULT_SEARCH_DIR)
content_result, path_result, errors, total_files, skipped, time_taken, interrupted = search_in_path_and_utf8_files(
    keyword = keyword,
    directory = directory,
    case_sensitive = case_sensitive,
    only_search_in_pathname = is_only_path,
    ignore_pathname = IGNORE_PATH,
    skip_inside_search_bigger_than = SKIP_BIG_SIZE*1024*1024
)

# Exit the program if no search result.
if not content_result and not path_result:
    pprint("\nNo search results found!", attr="green+bold")
    sys.exit()

# Fast access variables
c_result_len      = len(content_result)
p_result_len      = len(path_result)
error_len         = len(errors)
total_match       = c_result_len + p_result_len
files_having_kwrd = len(set(f for f, _ in content_result))
p_pattern         = re.compile(re.escape(keyword), re.IGNORECASE)
c_pattern         = re.compile(re.escape(keyword), 0 if case_sensitive else re.IGNORECASE)


def show(idx: int = 0, tolerance: int = DEFAULT_TOLERANCE) -> int:
    clear_screen()

    # Normalize index
    if idx < 0:
        idx = 0
    elif idx >= total_match:
        idx = total_match - 1

    # 1. First page: errors + status panel
    if idx in range(PER_PAGE_PATHS):
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
            f"| Errors: {error_len} "
            f"| Skipped: {skipped} "
        )
        print(f"TimeTaken: {time_taken}s")
        print(f"Keyword: `{keyword}`")
        print(f"Files having keyword: {files_having_kwrd}")

    # 2. Path results
    if idx < p_result_len:
        start = (idx // PER_PAGE_PATHS) * PER_PAGE_PATHS
        end = min(start + PER_PAGE_PATHS, p_result_len)
        idx = end - 1
        print_hr()
        pprint(f"{end}/{total_match}", attr="bold+green+underline")
        pprint("Results in path-names", attr="bold")
        print_hr()

        for i in range(start, end):
            highlighted_path = p_pattern.sub(
                lambda m: f"\033[48;2;{SEARCH_HIGHLIGHTER}m{m.group(0)}\033[0m",
                path_result[i]
            )
            print(f"{i+1}. {highlighted_path}")

    # 3. Content results
    else:
        filepath, line_no = content_result[idx - p_result_len]
        print_hr()
        pprint(f"{idx + 1}/{total_match}", attr="bold+green+underline")
        print(f"FilePath: `{filepath}`")
        print(f"Line: {line_no}")
        print_hr()

        with open(filepath, encoding="utf-8", errors="replace") as f:
            print_range = range(max(0, line_no - tolerance - 1), line_no + tolerance)

            for ln, line in enumerate(f, start=1):
                if ln in print_range:
                    # Replace keyword matches with highlighted version
                    highlighted = c_pattern.sub(
                        lambda m: f"\033[48;2;{SEARCH_HIGHLIGHTER}m{m.group(0)}\033[0m",
                        line
                    )
                    print(highlighted, end="")
    return idx


idx = show()
# Main Loop
while True:
    try:
        key = readchar.readkey()
        if key == readchar.key.UP:
            idx = (idx - 1) % total_match
            idx = show(idx)
        elif key == readchar.key.DOWN:
            idx = (idx + 1) % total_match
            idx = show(idx)
        else:
            try:
                pprint(f"Jump to result (1-{total_match}) | ~num (e.g. ~8): ", attr="green", end="")
                user_input = input().strip()
                if user_input.startswith("~"):
                    idx = show(idx, int(user_input[1:].strip()))
                else:
                    idx = show(int(user_input)-1)
            except (ValueError, EOFError):
                # invalid number or user pressed ctrl/d — ignore
                pass
    except KeyboardInterrupt:
        print()
        pprint("Exiting search-result viewer.", attr="magenta+bold")
        sys.exit()