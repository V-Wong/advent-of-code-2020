from typing import NewType, NamedTuple, Tuple, List, Callable

import re
from dataclasses import dataclass
from collections import Counter

import reader


@dataclass
class PasswordPolicy:
    start: int
    end: int
    character: str
    password: str


def count_valid_passwords(lines: List[PasswordPolicy],
                          validator: Callable[[PasswordPolicy], bool]):
    return sum(1 for line in lines if validator(line))


def validator1(policy: PasswordPolicy):
    return policy.start <= Counter(policy.password)[policy.character] <= policy.end


def validator2(policy: PasswordPolicy):
    password, character = policy.password, policy.character
    start, end = policy.start, policy.end

    return (password[start - 1] == character) ^ (password[end - 1] == character)


def parse(policy: str) -> PasswordPolicy:
    match = re.match(r'(\d+)-(\d+) (\w): (\w+)', policy)

    return PasswordPolicy(int(match.group(1)), int(match.group(2)), 
                          match.group(3), match.group(4))


if __name__ == "__main__":
    password_policies = reader.read_lines("./input.txt", parse)
    print(count_valid_passwords(password_policies, validator2))
