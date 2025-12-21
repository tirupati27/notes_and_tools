def verify_dict(data: dict, model: dict, path: str = "root") -> str:
    """
    Recursively verify that 'data' matches the structure defined by 'model'.
    Returns: empty string when no error, otherwise error message
    """
    if not isinstance(data, dict):
        return f"Error at {path}: Expected dict, got {type(data).__name__}"
    for key, expected in model.items():
        current_path = f"{path}.{key}"
        # Missing key
        if key not in data:
            return f"Error: Missing key '{current_path}'"
        value = data[key]
        # Nested dictionary
        if isinstance(expected, dict):
            if not isinstance(value, dict):
                return f"Error at {current_path}: Expected dict, got {type(value).__name__}"
            error = verify_dict(value, expected, current_path)
            if error:
                return error
        else:
            # Normalize expected into tuple for uniformity
            expected_types = expected if isinstance(expected, tuple) else (expected,)
            if not isinstance(value, expected_types):
                expected_names = ", ".join(t.__name__ for t in expected_types)
                return (
                    f"Error at {current_path}: "
                    f"Expected {expected_names}, got {type(value).__name__}"
                )
    return ""