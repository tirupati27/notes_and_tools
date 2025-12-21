import os

def iter_files(root_dir: str):
    """
Efficient way to iterate over all the files inside a directory including child folders.
It returns a generator of os.DirEntry object. or simply you can say list of 'os.DirEntry' object,
but it never loads all the items in the memory.
"""
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