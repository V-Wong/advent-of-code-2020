from typing import List

import math

import reader


def count_trees(tree_map: List[str], right: int, down: int) -> int:
    count = 0

    for i in range(len(tree_map) // down):
        y = i * down
        x = (right * i) % (len(tree_map[0]) - 1)

        count += tree_map[y][x] == "#"

    return count


if __name__ == "__main__":
    data = reader.read_lines("./input.txt")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    tree_counts = [count_trees(data, right, down) for right, down in slopes]
    print(math.prod(tree_counts))