# this script is used to print all the functions and variables declared in any python scripts.
# the below file list contains the targeted scripts.
file_list = ["custom_tools.py","main.py","api_test.py"]
import importlib.util
import inspect
import os
def load_module_from_path(path):
    """Dynamically import a module from a file path."""
    module_name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
def inspect_scripts(script_paths):
    """Print functions and variables for each script in the list."""
    for path in script_paths:
        print(f"\n===== {os.path.basename(path)} =====")
        module = load_module_from_path(path)
        items = list(module.__dict__.items())   # snapshot to avoid RuntimeError
        for name, value in items:
            if name.startswith("__"):
                continue  # skip internal stuff
            if inspect.isfunction(value):
                print(f"Function: {name}")
            elif not inspect.ismodule(value) and not inspect.isclass(value):
                print(f"Variable: {name} = {value}")
try:
    inspect_scripts(file_list)
except:
    print("This is NOT a valid script, check the 'file_list'")