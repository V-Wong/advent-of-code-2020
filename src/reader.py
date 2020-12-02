from typing import List, Callable, Any, TypeVar

T = TypeVar("T")


def reader(file_path: str, func: Callable[..., T]) -> List[T]:
    return [func(x) for x in list(open(file_path))]