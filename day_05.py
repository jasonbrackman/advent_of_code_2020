from typing import List

import helpers


#
# class Window:
#     def __init__(self, lower, upper):
#         self.lower: int = lower
#         self.upper: int = upper
#
#     def keep_lower_half(self):
#         self.upper = (self.upper - self.lower) // 2 + self.lower
#
#     def keep_upper_half(self):
#         self.lower = (self.upper + self.lower) // 2 + 1
#
#
# def get_seat_from_id(seat_id: str) -> int:
#     magic_number = 8  # puzzle provided
#     col: Window = Window(0, 127)
#     row: Window = Window(0, 7)
#
#     for c in seat_id[:7]:
#         if c == "F":
#             col.keep_lower_half()
#         elif c == "B":
#             col.keep_upper_half()
#
#     for c in seat_id[-3:]:
#         if c == "L":
#             row.keep_lower_half()
#         elif c == "R":
#             row.keep_upper_half()
#
#     assert col.lower == col.upper and row.lower == row.upper
#     return col.lower * magic_number + row.lower


def parse(code: str):
    num = "".join([{"F": "0", "L": "0", "B": "1", "R": "1"}[c] for c in code])
    row = int(num[:7], 2)
    col = int(num[-3:], 2)

    return row * 8 + col


def get_first_missing_seat_id(seat_ids: List) -> int:
    for i, x in enumerate(seat_ids, seat_ids[0]):
        if i != x:
            return i


def run():
    global line, seat_numbers
    lines = helpers.get_lines(r"./data/day_05.txt")
    seat_numbers = sorted(parse(line) for line in lines)
    part1 = seat_numbers[-1]
    part2 = get_first_missing_seat_id(seat_numbers)
    assert part1 == 930, f"Expected 930; received {part1}"
    assert part2 == 515, f"Expected 515; received {part2}"


if __name__ == "__main__":
    run()
