import shutil, argparse, sys, os
from text_attr import pprint

def print_hr(char='-'):
    pprint(f"{char*30}", attr="green+bold")

def exit_viewer():
    pprint("\nExiting search-result viewer.", attr="magenta+bold")
    sys.exit()

def clear_cache_and_exit():
    # os.path.dirname() Removes the last component (file or folder name) from a path
    cache_folders = [
        os.path.join(os.path.dirname(__file__), "__pycache__"),
        os.path.join(os.path.dirname(__file__), "tested_tools", "__pycache__")
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



def parse_and_validate_args(default_search_dir: str, project_doc: str) -> tuple:
    p = argparse.ArgumentParser(
        description='''Search for a given keyword in 'path names' and 'human readable files' or 'utf-8 encoded files'
    (like txt, json, html, etc) under a given directory.''')
    p.add_argument("searching_keyword", nargs="?", help="Keyword to search (non-empty)")
    p.add_argument("--directory", "-d", default=default_search_dir, help="Directory to search (default: current dir)")
    p.add_argument("--case-sensitive", "-c", action="store_true", help="Enable case-sensitive search")
    p.add_argument("--only-path", "-p", action="store_true", help="Enable only search in pathname")
    p.add_argument("--clear", action="store_true", help="Delete all cache files like '__pycache__'")
    p.add_argument("--usage", "-u", action="store_true", help="Show the program documentation")
    args = p.parse_args()

    if args.usage:
        print(project_doc)
        sys.exit()
    if args.clear:
        clear_cache_and_exit()

    # Args Validation
    keyword = args.searching_keyword
    if not keyword.strip():
        p.error("searching_keyword argument is required!")
    
    directory = args.directory
    try:
        os.scandir(directory)
    except Exception as e:
        pprint(f"Error: Regarding search dir `{directory}`", attr="red")
        print(e)
        sys.exit()

    return (
        keyword,
        directory,
        args.case_sensitive,
        args.only_path
    )
