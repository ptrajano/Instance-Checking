# Runtime Type Checking Decorator

## Overview
This module implements a Python decorator that performs **runtime type checking** of function arguments against their type annotations. The decorator acts as a wrapper that validates argument types before function execution.

## Core Functionality

### `check_instance` Decorator
def check_instance(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    A wrapper decorator that validates function argument types against their
    type annotations at runtime.
    
    Raises:
        ValueError: When an argument doesn't match its declared type
    """

## How It Works
### Type Checking:

Examines the function's type annotations (__annotations__)

Compares each argument's actual type with its declared type

Raises ValueError if type mismatch is found

### Example Usage:

@check_instance
def foo(a: str, b: int) -> None:
    pass

foo("hello", 42)  # Valid
foo(123, 42)      # Raises ValueError: Argument 'a' is not of type str
## Current Capabilities
Validates basic type hints (str, int, float, etc.)

Preserves original function metadata using functools.wraps

Works with positional arguments

Provides clear error messages

## Limitations (Experiment Phase)
❌ Doesn't handle keyword arguments validation

❌ Limited support for complex types (List, Dict, etc.)

❌ No validation for return types

❌ Doesn't work with imported types from typing module

## Add support for:

typing module types (List, Dict, Union, etc.)

Return type validation

Keyword arguments checking

Custom type validators

## Performance optimizations:

Cache type checks

Optional strict mode

Example Roadmap
@check_instance
def process_data(
    items: List[str],
    config: Dict[str, Union[int, float]],
    timeout: Optional[float] = None
) -> bool:
    ...
Requirements
Python 3.6+ (for type hints support)

No external dependencies

Author
Pedro Trajano Ferreira  
pedro.trajano.ferreira@gmail.com  
09/04/25