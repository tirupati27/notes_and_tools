"""
This script generates and prints the user specified value for 
the bash variable 'LS_COLORS' which is responsible for coloring the listings.

This script also can be used as `export LS_COLORS=$(python3 provide_ls_colors.py)` in bash.
"""
import sys
from build_ansi_escape_code import build_ansi_escape_code
if __name__ != "__main__":
    print(f"❌Error: This script must run with `python3 {sys.argv[0]}`", file=sys.stderr)
    sys.exit(1)

normal_text = ""
RESET = "0"

user_choice = {
    # ===================
    # Reset / Fallback
    # ===================
    """rs: reset all colors
    (This will reset any applied color or text attributes to default)""": RESET,
    """no: normal file (fallback)
    (A regular file without any special type or permissions)""": normal_text,
    # ===================
    # Directory
    # ===================
    """di: directory
    (A standard directory without special permissions)""": "blue+bold",
    """tw: world-writable directory with sticky bit (safe, e.g. /tmp)
    (Everyone can write, but only file owners can delete/rename their own files)""": "blue+italic",
    """ow: world-writable directory without sticky bit (unsafe)
    (Everyone can write and delete/rename any files, unsafe for shared directories)""": "blue+underline",
    """st: directory with sticky bit only
    (Write access is shared, but deletion and renaming are restricted to file owners)""": "blue+bold+italic",
    # ===================
    # Links
    # ===================
    """ln: symbolic link
    (A file that points to another file or directory)""": "cyan",
    """or: broken symbolic link
    (A symlink pointing to a non-existent target)""": "red+underline",
    """mi: missing file (dangling symlink target)
    (The target of a symlink does not exist)""": "red+italic",
    # ===================
    # Regular files
    # ===================
    """fi: regular file
    (A standard file without executable or special permissions)""": "white",
    """ex: executable file
    (A file that can be executed as a program or script)""": "green+bold",
    """mh: multi-hardlink file
    (A file that has multiple hard links pointing to it)""": "yellow",
    # ===================
    # Special files (IPC)
    # ===================
    """pi: named pipe (FIFO)
    (A file for inter-process communication using FIFO semantics)""": "magenta",
    """so: socket
    (A special file for network or inter-process communication)""": "magenta+bold",
    """do: door (Solaris IPC object)
    (A Solaris-specific IPC object for communication)""": "magenta+underline",
    # ===================
    # Devices
    # ===================
    """bd: block device
    (A device file that provides buffered access to hardware devices)""": "yellow+bold",
    """cd: character device
    (A device file that provides unbuffered, character-by-character access)""": "yellow+italic",
    # ===================
    # Permission-sensitive files
    # ===================
    """su: setuid executable
    (Executable that runs with the privileges of the file owner)""": "red+bold",
    """sg: setgid executable
    (Executable that runs with the privileges of the file's group)""": "red+italic",
    """ca: file with capabilities
    (A file with specific Linux capabilities set for privilege management)""": "red+underline",
    # ===================
    # File extensions
    # ===================
    # Archives
    "*.tar: "  : "blue",
    "*.gz: "   : "blue",
    "*.zip: "  : "blue",
    "*.7z: "   : "blue",
    "*.rar: "  : "blue",
    # Images
    "*.jpg: "  : "magenta",
    "*.jpeg: " : "magenta",
    "*.png: "  : "magenta",
    "*.gif: "  : "magenta",
    # Audio
    "*.mp3: "  : "cyan",
    "*.m4a: "  : "cyan",
    "*.opus: "  : "cyan",
    "*.aac: "  : "cyan",
    # Video
    "*.mp4: "  : "cyan+bold",
    "*.mkv: "  : "cyan+bold",
    # Data / config files
    "*.json: " : "yellow",
    "*.yaml: " : "yellow",
    "*.yml: "  : "yellow",
    "*.toml: " : "yellow",
    # Other
    "*.pdf: "  : "red",
    "*.txt: "  : "white",
    "*.md: "   : "white+italic",
}


result=[]
for key, value in user_choice.items():
    k = key.split(":")[0].strip().lower()
    v = build_ansi_escape_code(value).removeprefix("\033[").removesuffix("m") or RESET
    result.append(f"{k}={v}")

print("'" + ":".join(result) + "'")
