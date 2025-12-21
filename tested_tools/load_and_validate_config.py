import json
import sys
from verify_dict import verify_dict


def load_and_validate_config(json_path: str, model: dict, return_tuple: bool = False) -> tuple | dict | None:
    """Load and validate a configuration JSON file."""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        error = verify_dict(data, model=model)
        if error:
            raise ValueError(f"Validation failed: {error}")
        if return_tuple:
            if not data:
                return None
            if len(data) == 1:
                return next(iter(data.values()))
            return tuple((data[i] for i in model))
        return data
    except Exception as e:
        print(f"\033[31mError while loading and validating json file `{json_path}`:\033[0m")
        print(e)
        print()
        print("Expected Model:")
        print(model)
        sys.exit(1)