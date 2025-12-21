import inspect

# Example dependencies
def get_name():
    return "Alice"

def get_age():
    return 30

# Our dynamic argument builder
def call_with_injection(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = {}

        for name, param in sig.parameters.items():
            if callable(param.default):
                bound_args[name] = param.default()
            else:
                bound_args[name] = param.default
        return func(**bound_args)
    return wrapper

@call_with_injection
def greet(name: str = get_name(), age: int = get_age()):
    print(f"Hello {name}, you are {age} years old.")

greet()