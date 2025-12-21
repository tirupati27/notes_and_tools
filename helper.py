import shutil, argparse, sys
from pathlib import Path
from text_attr import pprint

def print_hr(char='-'):
    pprint(f"{char*30}", attr="green+bold")

def clear_cache_and_exit():
    cache_folders = [
        (Path(__file__) / "../__pycache__").resolve(),
        (Path(__file__) / "../tested_tools/__pycache__").resolve()
    ]
    for i in cache_folders:
        try:
            shutil.rmtree(i)
            pprint("Deleted: ", attr="cyan", end="")
            print(i)
        except FileNotFoundError:
            pprint("AlreadyDeleted: ", attr="cyan", end="")
            print(i)
        except Exception as e:
            pprint("Error while Deleting: ", attr="red", end="")
            print(i)
            print(e)
    pprint("Done !", attr="Green+bold")
    sys.exit()



def parse_and_validate_args(default_search_dir: str) -> tuple:
    p = argparse.ArgumentParser(
        description='''Search for a given keyword in 'path names' and 'human readable files' or 'utf-8 encoded files'
    (like txt, json, html, etc) under a given directory.''')
    p.add_argument("searching_keyword", default="", help="Keyword to search (non-empty)")
    p.add_argument("--directory", "-d", default=default_search_dir, help="Directory to search (default: current dir)")
    p.add_argument("--case-sensitive", "-c", action="store_true", help="Enable case-sensitive search")
    p.add_argument("--only-path", "-p", action="store_true", help="Enable only search in path")
    p.add_argument("--clear", action="store_true", help="Delete all cache files like '__pycache__'")
    args = p.parse_args()
    keyword = args.searching_keyword
    directory = Path(args.directory)
    if args.clear:
        clear_cache_and_exit()
    if not keyword.strip():
        p.error("searching_keyword argument is required!")
    if not directory.exists():
        pprint("Error: ", attr="red", end="")
        print(f"directory `{directory}` does not exist.")
        sys.exit()

    return (
        keyword,
        str(directory),
        args.case_sensitive,
        args.only_path
    )
