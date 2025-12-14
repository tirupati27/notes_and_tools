#!/usr/bin/env python3
"""
@@@@@@@@Live UI@@@@@@@@
Searching `keyword` ...
Scanned: 2530 | Matches: 2 | Errors: 0
@@@@@@@@UI when index is 0@@@@@@@@
------------------------------
Errors while scanning files-
------------------------------
1. `filePath`
e
2. `filePath`
e
------------------------------
Interrupted by user.
Scanned: 2530 | Matches: 2 | Errors: 0
TimeTaken: 3.43s
Keyword: `keyword`
Files having keyword: 2
@@@@@@@@Search result viewer UI@@@@@@@@
------------------------------
1/2
FilePath: `filepath`
Line: 9
------------------------------
content here...
"""

from text_attr import print as pprint
import argparse
import os
import sys
import re
import mmap
import time
import shutil
import gc
from pathlib import Path
try:
    import readchar
except Exception:
    print("Missing dependency: readchar. Install with `pip install readchar`.")
    sys.exit(1)

# Extensions that are very likely binary / useless for text search
SKIP_EXT = {
    ".jpg", ".jpeg", ".png", ".gif", ".bmp",
    ".mp4", ".mkv", ".avi", ".mov",
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".exe", ".dll", ".so", ".bin", ".iso",
    ".pdf", ".woff", ".woff2", ".ttf", ".otf"
}
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def print_hr(char='-'):
    pprint(f"{char*30}", attr="green+bold")
def count_files(path: str) -> int:
    count = 0
    stack = [path]
    while stack:
        current = stack.pop()
        try:
            with os.scandir(current) as it:
                for entry in it:
                    if entry.is_file():
                        count += 1
                    elif entry.is_dir(follow_symlinks=False):
                        stack.append(entry.path)
        except PermissionError:
            continue
    return count
def iter_files(root_dir: str):
    stack = [root_dir]
    while stack:
        current = stack.pop()
        try:
            with os.scandir(current) as it:
                for entry in it:
                    if entry.is_dir(follow_symlinks=False):
                        stack.append(entry.path)
                    elif entry.is_file(follow_symlinks=False):
                        yield entry
        except PermissionError:
            continue

def search_result_viewer(
    count: int, total: int,
    filepath: str, line_no: int,
    tolerance: int, keyword: str,
    case_sensitive: bool
):
    print_hr()
    pprint(f"{count}/{total}", attr="bold+green+underline")
    print(f"FilePath: `{filepath}`")
    print(f"Line: {line_no}")
    print_hr()
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
            lines = fh.readlines()
    except Exception as e:
        pprint(f"Unable to read file `{filepath}`:", attr="red+bold")
        print(e)
        return
    start = max(0, line_no - tolerance - 1)
    end = min(len(lines), line_no + tolerance)
    for i in range(start, end):
        line = lines[i]
        try:
            pattern = re.escape(keyword)
            flags = 0 if case_sensitive else re.IGNORECASE
            # Replace each matched group with the same text wrapped in ANSI background
            line = re.sub(
                pattern,
                lambda m: f"\033[48;2;250;250;100m{m.group(0)}\033[0m",
                line,
                flags=flags
            )
        except: pass
        print(line, end="")

def print_zero_index_UI(
    errors: list, interrupted: bool,
    total_files: int, matches: int,
    time_taken: float, keyword: str,
    files_having_keyword: int
):
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
        pprint("Interrupted by user.", attr="red")
    print(f"\rScanned: {total_files} | Matches: {matches} | Errors: {len(errors)}")
    print(f"TimeTaken: {time_taken}s")
    print(f"Keyword: `{keyword}`")
    print(f"Files having keyword: {files_having_keyword}")

def fast_search(keyword: str, directory: str, case_sensitive: bool) -> tuple:
    results = []
    errors = []
    interrupted = False
    keyword_b = keyword.encode("utf-8")
    total_files = 0
    max_file = count_files(directory)
    last_print = time.monotonic()
    print(f"Searching `{keyword}`...")
    for entry in iter_files(directory):
        total_files += 1
        # ---- Progress output (throttled, inline, no thread) ----
        now = time.monotonic()
        if now - last_print > 0.2:
            #print(f"\rScanned: {total_files} | Matches: {len(results)} | Errors: {len(errors)}", end="", flush=True)
            print(f"\rScanned: {total_files} {(total_files*100)//max_file}% | Matches: {len(results)} | Errors: {len(errors)}", end="", flush=True)
            last_print = now
        try:
            # ---- Fast skip checks (before open) ----
            name = entry.name.lower()
            _, ext = os.path.splitext(name)
            if ext in SKIP_EXT or entry.stat().st_size == 0:
                continue    # skip the specific ext's file and empty files
            # ---- mmap search ----
            with open(entry.path, "rb") as fh:
                with mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    if case_sensitive:
                        pos = mm.find(keyword_b)
                    else:
                        # Case-insensitive without copying entire file
                        pos = mm.find(keyword_b.lower())
                        if pos == -1:
                            continue
                    if pos == -1:
                        continue  # fast path: no match → no line counting
                    # ---- Line number calculation (only if match exists) ----
                    last = 0
                    line_no = 1
                    while pos != -1:
                        line_no += mm[last:pos].count(b"\n")
                        last = pos
                        results.append((entry.path, line_no))
                        if case_sensitive:
                            pos = mm.find(keyword_b, pos + 1)
                        else:
                            pos = mm.find(keyword_b.lower(), pos + 1)
        except KeyboardInterrupt:
            interrupted = True
            break
        except Exception as e:
            errors.append((entry.path, e))
    return results, errors, total_files, interrupted

def parse_and_validate_args():
    p = argparse.ArgumentParser(description="Ultra-fast searching tool")
    p.add_argument("searching_keyword", help="Keyword to search (non-empty)")
    p.add_argument("--directory", "-d", default=".", help="Directory to search (default: current dir)")
    p.add_argument("--lines", "-n", type=int, default=7, help="Number of context lines before/after match")
    p.add_argument("--case-sensitive", "-c", action="store_true", help="Enable case-sensitive search")
    p.add_argument("--clear", action="store_true", help="Delete all cache files like '__pycache__'")
    args = p.parse_args()
    keyword = args.searching_keyword
    directory = Path(args.directory)
    if args.clear:
        cache_dir = (Path(__file__) / "../__pycache__").resolve()
        if not cache_dir.exists():
            print("cache already cleared!")
            sys.exit()
        try:
            shutil.rmtree(cache_dir)
            print("All cache cleared!")
        except Exception as e:
            print(f"Error while deleting directory: `{cache_dir}`")
            print(e)
        sys.exit()
    if not keyword.strip():
        pprint("Error: ", attr="red", end="")
        print("searching_keyword cannot be empty.")
        sys.exit(2)
    if not directory.exists():
        pprint("Error: ", attr="red", end="")
        print(f"directory `{directory}` does not exist.")
        sys.exit(2)
    return (
        keyword,
        str(directory),
        args.lines,
        args.case_sensitive,
    )

def main():
    keyword, directory, tolerance, case_sensitive = parse_and_validate_args()
    start = time.perf_counter()
    results, errors, total_files, interrupted = fast_search(keyword, directory, case_sensitive)
    elapsed = time.perf_counter() - start

    if not results:
        print()
        pprint("No search results found!", attr="green+bold")
        sys.exit()

    total_matches = len(results)
    ui_payload = {
        "errors": errors,
        "interrupted": interrupted,
        "total_files": total_files,
        "matches": total_matches,
        "time_taken": round(elapsed, 2),
        "keyword": keyword,
        "files_having_keyword": len(set(f for f, _ in results)),
    }
    viewer_payload = {
        "count": None,
        "total": total_matches,
        "filepath": None,
        "line_no": None,
        "tolerance": tolerance,
        "keyword": keyword,
        "case_sensitive": case_sensitive,
    }
    def show(idx: int):
        clear_screen()
        if idx == 0:
            print_zero_index_UI(**ui_payload)
        viewer_payload["count"] = idx+1
        viewer_payload["filepath"] = results[idx][0]
        viewer_payload["line_no"] = results[idx][1]
        search_result_viewer(**viewer_payload)

    idx = 0
    show(idx)

    # ------Free Memory campaign start--------
    # Locals
    del keyword
    del directory
    del tolerance
    del case_sensitive
    del start
    del errors
    del total_files
    del interrupted
    del elapsed
    # globals
    del_obj = [
        "pathlib",
        "Path",
        "argparse",
        "mmap",
        "time",
        "shutil",
        "SKIP_EXT",
        "count_files",
        "iter_files",
        "fast_search",
        "parse_and_validate_args",
    ]
    for i in del_obj:
        try:
            del globals()[i]
        except KeyError: pass
    del del_obj
    gc.collect()
    # ------Free Memory campaign end--------
    while True:
        try:
            key = readchar.readkey()
            if key == readchar.key.UP:
                idx = (idx - 1) % total_matches
                show(idx)
            elif key == readchar.key.DOWN:
                idx = (idx + 1) % total_matches
                show(idx)
            else:
                try:
                    pprint(f"Jump to result (1-{total_matches}): ", attr="green", end="")
                    show(int(input().strip())-1)
                except (ValueError, EOFError):
                    # invalid number or user pressed ctrl/d — ignore
                    pass
        except KeyboardInterrupt:
            print()
            pprint("Exiting search-result viewer.", attr="magenta+bold")
            sys.exit()

if __name__ == "__main__":
    main()