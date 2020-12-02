from typing import List, Callable


def reader(file_path: str, func: Callable) -> List[int]:
    return [func(x) for x in list(open(file_path))]