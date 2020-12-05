import helpers
from typing import List


class Window:
    def __init__(self, lower, upper):
        self.lower: int = lower
        self.upper: int = upper

    def keep_lower_half(self):
        self.upper = (self.upper - self.lower) // 2 + self.lower

    def keep_upper_half(self):
        self.lower = (self.upper + self.lower) // 2 + 1


def get_seat_from_id(seat_id: str) -> int:
    magic_number = 8  # puzzle provided
    col: Window = Window(0, 127)
    row: Window = Window(0, 7)

    for _id in seat_id:
        if _id == "F":
            col.keep_lower_half()
        elif _id == "B":
            col.keep_upper_half()
        elif _id == "L":
            row.keep_lower_half()
        elif _id == "R":
            row.keep_upper_half()

    assert col.lower == col.upper and row.lower == row.upper
    return col.lower * magic_number + row.lower


def get_first_missing_seat_id(seat_ids: List) -> int:
    for i, x in enumerate(seat_ids, seat_ids[0]):
        if i != x:
            return i


if __name__ == "__main__":
    lines = helpers.get_lines(r'./data/day_05.txt')

    seat_numbers = sorted(get_seat_from_id(line) for line in lines)

    part1 = seat_numbers[-1]
    part2 = get_first_missing_seat_id(seat_numbers)

    assert part1 == 930, f"Expected 930; received {part1}"
    assert part2 == 515, f"Expected 515; received {part2}"
