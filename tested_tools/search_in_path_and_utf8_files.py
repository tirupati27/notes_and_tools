import os
import time
from pathlib import Path
from iter_files import iter_files


def search_in_path_and_utf8_files(
    keyword: str,
    directory: str | Path = ".",
    case_sensitive: bool = False,
    only_search_in_pathname: bool = False,
    ignore_pathname: list | None = None,
    skip_content_search_gt: float | int = 100 * 1024 * 1024,
) -> tuple:
    """
    Search for a given keyword in path names and UTF-8 encoded text files
    (like txt, json, html, etc.) under a given directory.

    Returns:
        tuple: (
            result_in_files: list of (filepath, line_no),
            result_in_path_names: list of paths,
            errors: list of (filepath, exception),
            total_files: int,
            skipped: int,
            elapsed_time: float (seconds),
            interrupted: bool
        )
    """
    start_time = time.perf_counter()

    # Normalize inputs
    directory = Path(directory)
    keyword = keyword if case_sensitive else keyword.lower()
    ignore_pathname = set(ignore_pathname or [])

    print(f"Searching `{keyword}` in dir `{directory}` ...")

    result_in_files: list[tuple[str, int]] = []
    result_in_path_names: list[str] = []
    errors: list[tuple[str, Exception]] = []
    interrupted = False
    total_files = 0
    skipped = 0
    last_print = time.monotonic()

    for entry in iter_files(directory):
        total_files += 1
        filepath = entry.path

        # Progress panel every 0.2s
        now = time.monotonic()
        if now - last_print > 0.2:
            print(
                f"\rTotal-files: {total_files} "
                f"| Matches: {len(result_in_files) + len(result_in_path_names)} "
                f"| Skipped: {skipped} ",
                end="",
                flush=True,
            )
            last_print = now

        # search keyword in pathname (case insensitive)
        if keyword.lower() in filepath.lower():
            result_in_path_names.append(filepath)
            if only_search_in_pathname:
                continue

        # Skip conditions
        if ignore_pathname and set(filepath.split(os.sep)) & ignore_pathname:
            skipped += 1
            continue
        if entry.stat().st_size > skip_content_search_gt:
            skipped += 1
            continue

        # File content search
        try:
            with open(filepath, encoding="utf-8", errors="replace") as f:
                for line_no, line in enumerate(f, start=1):
                    line = line if case_sensitive else line.lower()
                    if keyword in line:
                        result_in_files.append((filepath, line_no))

        except KeyboardInterrupt:
            interrupted = True
            break
        except Exception as e:
            errors.append((filepath, e))

    # Final panel
    print(
        f"\rTotal-files: {total_files} "
        f"| Matches: {len(result_in_files) + len(result_in_path_names)} "
        f"| Skipped: {skipped} "
    )

    return (
        result_in_files,
        result_in_path_names,
        errors,
        total_files,
        skipped,
        round(time.perf_counter() - start_time, 2),
        interrupted,
    )