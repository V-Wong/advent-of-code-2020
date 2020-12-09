from typing import List

from collections import Counter, defaultdict

import reader


def count_any_answered(group: List[str]) -> int:
    return len(Counter("".join(group)))


def count_all_answered(group: List[str]) -> int:
    answer_count = defaultdict(lambda: 0)

    for person in group:
        person_answers = set()
        for answer in person:
            if answer not in person_answers:
                answer_count[answer] += 1
                person_answers.add(answer)

    return sum(1 for answer, count in answer_count.items() if count == len(group))


if __name__ == "__main__":
    groups = reader.read_blocks("./input.txt")
    print(sum(count_any_answered(group) for group in groups))
    print(sum(count_all_answered(group) for group in groups))
