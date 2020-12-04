from typing import List, Dict

import re

from reader import reader


FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def parse_passport(raw_passport: str) -> Dict[str,str]:
    passport = {}

    for field in FIELDS:
        if match := re.match(f".*{field}:([\S]+)", raw_passport):
            passport[field] = match.group(1)

    return passport


def is_valid_passport1(passport: Dict[str, str]) -> bool:
    return all(field in passport for field in FIELDS)


def is_valid_passport2(passport: Dict[str, str]) -> bool:
    rules = {
        "byr": lambda year: 1920 <= int(year) <= 2002,
        "iyr": lambda year: 2010 <= int(year) <= 2020,
        "eyr": lambda year: 2020 <= int(year) <= 2030,
        "hgt": lambda height: (height[-2:] == "cm" and 150 <= int(height[:-2]) <= 193) \
                              or (height[-2:] == "in" and 59 <= int(height[:-2]) <= 76),
        "hcl": lambda colour: len(colour) == 7 and colour[0] == '#' and colour[1:].isalnum(),
        "ecl": lambda colour: colour in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda id: len(id) == 9 and id.isnumeric(),
    }

    return all(key in passport and rules[key](passport[key]) for key in FIELDS)


if __name__ == "__main__":
    data = reader("./input.txt", lambda x: str(x).replace("\n", " ") if x != "\n" else x)
    raw_passports = "".join(data).split("\n") # ugly hack

    passports = [parse_passport(raw_passport) for raw_passport in raw_passports]
    
    print(sum(1 for passport in passports if is_valid_passport1(passport)))
    print(sum(1 for passport in passports if is_valid_passport2(passport)))
