from typing import List, Tuple

from dataclasses import dataclass
import math

import reader


ROW_MAX = 127
COL_MAX = 7
INCREASE = "^"


@dataclass
class BoardingPass:
    row_info: str
    col_info: str


def get_seat_position(boarding_pass: BoardingPass) -> Tuple[int, int]:
    def get_position(boarding_pass: str, low: int, high: int) -> int:
        for char in boarding_pass:
            if char == INCREASE:
                low = math.ceil((high + low) / 2) 
            else:
                high = math.floor((high + low) / 2)

        return low

    return get_position(boarding_pass.row_info, 0, ROW_MAX), \
           get_position(boarding_pass.col_info, 0, COL_MAX)


def get_seat_id(seat_position: Tuple[int, int]) -> int:
    row, col = seat_position
    return 8 * row + col


def find_own_seat_id(boarding_passes: List[str]) -> int:
    all_seat_positions = set(get_seat_position(boarding_pass)
                             for boarding_pass in boarding_passes)
    
    all_seats = {get_seat_id(seat_position): seat_position
                 for seat_position in all_seat_positions}

    for row in range(1, ROW_MAX + 1):
        for col in range(COL_MAX + 1):
            if (row, col) not in all_seat_positions:
                seat_id = get_seat_id((row, col))

                if seat_id - 1 in all_seats and seat_id + 1 in all_seats:
                    return seat_id


if __name__ == "__main__":
    data = reader.read_lines("./input.txt", lambda x: str(x).replace("B", INCREASE).replace("R", INCREASE))
    
    passes = [BoardingPass(line[:7], line[7:]) for line in data]

    # Part 1
    print(max(get_seat_id(get_seat_position(boarding_pass)) for boarding_pass in passes))

    # Part 2
    print(find_own_seat_id(passes))
