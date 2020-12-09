from typing import List, Callable, Any, TypeVar

T = TypeVar("T")


def read_lines(file_path: str, parse: Callable[..., T]=str) -> List[T]:
    return [parse(x) for x in open(file_path)]


def read_blocks(file_path: str, parse: Callable[..., T]=str) -> List[List[T]]:
    data = list(open(file_path))
    blocks = "".join(data).split("\n\n") # ugly hack
    return [[parse(x) for x in block.split("\n")] for block in blocks]
