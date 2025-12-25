"""
Use this script as:
    source <(python3 bashrc_api.py)
inside the ~/.bashrc file.
"""
import sys, json
from pathlib import Path

script_dir = Path(__file__).parent.resolve()
sys.path.insert(1, str(script_dir.parent))

from build_ansi_escape_code import build_ansi_escape_code

def ps1_api(name: str, name_attr: str, cwd_attr: str)-> str:
    default_attr = "white+bg: black"
    name_attr = build_ansi_escape_code(name_attr) or build_ansi_escape_code(default_attr)
    cwd_attr = build_ansi_escape_code(cwd_attr) or build_ansi_escape_code(default_attr)
    return (
        "if [[ $UID -eq 0 ]]; "
        rf'''then export PS1="\[\033[{name_attr}m\]{name}:\[\033[0m\] \[\033[{cwd_attr}m\]\w\[\033[0m\] \[\033[{name_attr}m\]#\[\033[0m\] "; '''
        rf'''else export PS1="\[\033[{name_attr}m\]{name}:\[\033[0m\] \[\033[{cwd_attr}m\]\w\[\033[0m\] \[\033[{name_attr}m\]\$\[\033[0m\] "; '''
        "fi; "
    )

def ls_color_api(ls_color_config: dict)-> str:
    result=[]
    for key, value in ls_color_config.items():
        k = key.split(":")[0].strip().lower()
        v = build_ansi_escape_code(value) or "0"
        result.append(f"{k}={v}")
    return f"""export LS_COLORS='{":".join(result)}'; """

def aliases_api(alias_data: dict)-> str:
    alias_lines = []
    for key, value in alias_data.items():
        line = f'''alias {key}="{value}"; '''
        alias_lines.append(line)
        
    return "".join(alias_lines)

def main():
    # Loading config json file
    try:
        with open(script_dir/"bashrc_api_config.json") as f:
            config = json.load(f)
    except Exception as e:
        print("Error while loading config file\n", e, file=sys.stderr)
        sys.exit(1)
    
    ps1_code = ps1_api(**config["PS1"])
    ls_color_code = ls_color_api(config["LS_COLORS"])
    aliases_code = aliases_api(config["aliases"])

    print(ps1_code + aliases_code + ls_color_code)


if __name__=="__main__":
    main()