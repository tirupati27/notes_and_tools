def pretty_size(bytes_: int)-> str:
    """Takes size in bytes and returns human readable string. like, 1024 -> '1.000 KB'
"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_ < 1024:
            return f"{bytes_:.3f} {unit}"
        bytes_ /= 1024