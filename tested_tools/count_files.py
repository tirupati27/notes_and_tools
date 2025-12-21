import os

def count_files(path: str) -> int:
    """
Efficient way to count all the files inside a directory including child folders.
"""
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