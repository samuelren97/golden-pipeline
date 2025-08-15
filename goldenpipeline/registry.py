from typing import Any, Callable, TypeVar

T = TypeVar("T", bound=Callable[..., Any])

STEP_REGISTRY: dict[str, Callable[..., Any]] = {}


def register_step(name: str) -> Callable[[T], T]:
    """
Decorator that registers a function in STEP_REGISTRY under the given name.
"""

    def decorator(func: T) -> T:
        try:
            _ = STEP_REGISTRY[name]
            raise ValueError(f"step with name: {name} already exists")
        except KeyError:
            STEP_REGISTRY[name] = func

        return func

    return decorator
