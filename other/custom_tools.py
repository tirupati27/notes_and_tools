from pathlib import Path
from pprint import pprint
from fastapi import HTTPException, status
import requests

def verify_dict(data: dict, model: dict, path="root")-> bool:
    """
    Recursively verify that 'data' matches the structure defined by 'model'.
    """
    error = None  # store the first error message

    # Root type check
    if not isinstance(data, dict):
        error = f"Error at {path}: Expected dict, got {type(data).__name__}"
    else:
        for key, expected in model.items():
            current_path = f"{path}.{key}"

            # Missing key
            if key not in data:
                error = f"Error: Missing key '{current_path}'"
                break

            value = data[key]

            # Nested dictionary
            if isinstance(expected, dict):
                if not isinstance(value, dict):
                    error = f"Error at {current_path}: Expected dict, got {type(value).__name__}"
                    break
                # Recursive check for nested dicts (note argument order!)
                if not verify_dict(value, expected, current_path):
                    return False
                continue  # move to next key if nested dict is fine

            # Tuple of allowed types
            elif isinstance(expected, tuple):
                if not any(isinstance(value, t) for t in expected):
                    expected_names = [t.__name__ for t in expected]
                    error = f"Error at {current_path}: Expected any of {expected_names}, got {type(value).__name__}"
                    break

            # Single expected type
            else:
                if not isinstance(value, expected):
                    error = f"Error at {current_path}: Expected {expected.__name__}, got {type(value).__name__}"
                    break
    if error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )
    return True


def verify_subpath(
    base_path: str | Path,
    subpath: str | Path,
    exists: bool = False,
    is_file: bool = False,
    is_dir: bool = False,
) -> Path:

    if is_file or is_dir:
        exists = True
    
    base_path = Path(base_path).resolve()
    abs_subpath = (base_path / subpath.lstrip("/")).resolve()

    if not abs_subpath.is_relative_to(base_path):
        error_detail=f"Invalid path: '{subpath}', path must be a childpath of hosted directory."
    elif exists and not abs_subpath.exists():
        error_detail=f"Invalid path: '{subpath}', path does not exits."
    elif is_file and not abs_subpath.is_file():
        error_detail=f"Invalid file: '{subpath}', file does not exits."
    elif is_dir and not abs_subpath.is_dir():
        error_detail=f"Invalid folder: '{subpath}', folder does not exits."
    else:
        error_detail=""
    
    if error_detail:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_detail
        )
    return abs_subpath

def print_routes(app):
    file_path = "api_test.py"
    url_block = "URLS = {\n"
    counter = 1
    for route in app.routes:
        if hasattr(route, "methods") and hasattr(route, "path"):
            for method in route.methods:
                if method in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
                    url_block += f'    {counter}: "{method} http://127.0.0.1:9000{route.path}",\n'
                    counter += 1
    url_block += "}\n"
    print("You have following routes in the app:\n")
    print(url_block)

def print_mimetype(filename):
    import mimetypes
    mime_type, _ = mimetypes.guess_type(filename)
    mime_type = mime_type or "application/octet-stream"
    '''
    application/octet-stream literally means:
    “This is a stream of bytes — I don’t know (or don’t care) what kind of file it is.”
    It’s the fallback MIME type for any file whose type you can’t detect automatically.
    '''
    print(f"\n{mime_type}\n")

def api_test(kwargs: dict):
    kwargs = {key.replace("✅",""):value for key, value in kwargs.items()}
    method = kwargs["url"].split()[0].lower()
    kwargs["url"] = kwargs["url"].split()[1]
    if kwargs["files"]:
        kwargs['headers']["Content-Type"] = None
    
    response = getattr(requests, method)(**kwargs)

    if kwargs["files"]:
        for _, (_, f, _) in kwargs["files"]:
            f.close()
    msg = "✅ Response:" if response.ok else "❌ Error:"
    try:
        print(f"{msg} {response.status_code}")
        pprint(response.json())
    except Exception:
        print(f"{msg} {response.status_code}\n{response.text}")
