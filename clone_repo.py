import os, sys
sys.path.insert(1, os.path.join(os.path.dirname(__file__), "tested_tools"))

import subprocess
import requests
import shutil
from pathlib import Path
from text_attr import pprint


USER_NAME = "tirupati27"

# Add here all the repos in the "user/repo-name" format, which you want to clone
CUSTOM_REPOS = [
    f"{USER_NAME}/notes_and_tools",
    # add more repos here
]


def repo_list_provider()-> list:
    print(f"Getting repo list of '{USER_NAME}' from github API...")
    try:
        url = f"https://api.github.com/users/{USER_NAME}/repos?per_page=100&page=1"
        json_data = requests.get(url).json()
        repos_list = [repo["full_name"] for repo in json_data] + CUSTOM_REPOS
        print(f"Successfully got the list of all the repos from '{USER_NAME}'")
    except Exception as e:
        pprint(f"\nFailed to get repos of '{USER_NAME}' from github API", attr="red+bold")
        print(e)
        sys.exit(1)

    repos_list.remove(f"{USER_NAME}/notes_and_tools")
    return list(set(repos_list))

# 1. Ensure the script not used as module
if __name__ != "__main__":
    print(f'Run with "python3 {sys.argv[0]}"')
    sys.exit(1)

# 2. Setup directory
clone_dir = Path(__file__).resolve().parent / "github_repo"
clone_dir.mkdir(exist_ok=True)

list_of_repos = repo_list_provider()
total_repos = len(list_of_repos)
failed = []

# 3. Prompt for permission
pprint(f"Total {total_repos} repos found. Proceed with cloning [y/n]: ", attr="cyan", end="")
if input().strip().lower() != "y":
    print("Cloning Aborted!")
    sys.exit(0)

# 4. start cloning
for i, repo in enumerate(list_of_repos, start=1):

    url = f"https://github.com/{repo}.git"
    repo_name = repo.split("/")[1]
    pprint(f"{i}/{total_repos} ", attr="green+bold", end="")
    pprint(f"Cloning `{repo}` ...", attr="blue+italic")
    shutil.rmtree(clone_dir/repo_name, ignore_errors=True)

    try:
        subprocess.run(
            ["git", "clone", url],
            cwd=clone_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        print(f"Successfully cloned: `{repo}`\n")
        
    except subprocess.CalledProcessError as e:
        failed.append(repo)
        pprint(f"Failed to clone: `{repo}`", attr="red+bold")
        print(e.stderr)

# 5. Conclusion
if failed:
    pprint(f"\nFollowing {len(failed)} repos failed to clone.", attr="cyan+bold")
    for i, repo in enumerate(failed, start=1):
        print(f"{i}. {repo}")
else:
    pprint("\nAll the repos cloned successfully !", attr="green+bold")