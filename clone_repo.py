import subprocess

REPOS = [
    "tirupati27/Olevel-javascript-project",
    "tirupati27/ddu_gradesheet",
    "tirupati27/mycmd",
    "tirupati27/climate_change",
    "tirupati27/python-s-documentations",
    "tirupati27/notes_and_tools",
    "tirupati27/a-basic-calculator",
    "tirupati27/termux_file_server"
]

for repo in REPOS:
    url = f"https://github.com/{repo}.git"
    print(f"Cloning {url} ...")

    result = subprocess.run(
        ["git", "clone", url],
        cwd=".temp",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode == 0:
        print(f"✅ Successfully cloned: {repo}\n")
    else:
        print(f"❌ Failed to clone: {repo}")
        print(result.stderr, "\n")
