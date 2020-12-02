from typing import List, Tuple, Union

from math import prod

from reader import reader


def two_sum(nums: List[int], target: int) -> Union[Tuple[int, int], None]:
    ht = {}

    for i, v in enumerate(nums):
        if v in ht:
            return i, ht[v]
        else:
            ht[target - v] = i

    return None


def three_sum(nums: List[int], target: int) -> Union[Tuple[int, int, int], None]:
    ht = {target - v: i for i, v in enumerate(nums)}

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            pair_sum = nums[i] + nums[j]
            if pair_sum in ht and ht[pair_sum] not in (i, j):
                return i, j, ht[pair_sum]

    return None


if __name__ == "__main__":
    nums = reader("./input.txt", int)

    if (answer := three_sum(nums, 2020)) is not None:
        print(prod([nums[x] for x in answer]))