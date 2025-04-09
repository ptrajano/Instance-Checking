from typing import Callable, Any
from functools import wraps

def check_instance(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Check the variables type of a given function
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        for (arg_name, arg_type), arg_value in zip(func.__annotations__.items(), args):
            if hasattr(arg_type, '__name__') and not isinstance(arg_value, arg_type):
                raise ValueError(f"In Function: {func.__name__}. Argument '{arg_name}' is not of type {arg_type.__name__}")
        return func(*args, **kwargs)
    return wrapper


