import sys
import gc

def deep_size(obj, seen=None) -> int:
    """This function accept a python object and returns the total memory consumed by it (in bytes).
"""
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)

    size = sys.getsizeof(obj)

    for ref in gc.get_referents(obj):
        size += deep_size(ref, seen)

    return size
