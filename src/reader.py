from typing import List


def reader(file_path: str) -> List[int]:
    return [int(x) for x in list(open(file_path))]