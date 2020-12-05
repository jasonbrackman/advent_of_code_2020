import helpers


def get_seat_id(sample):
    upper_col = 127
    lower_col = 0

    upper_row = 7
    lower_row = 0

    for x in sample:
        if x == "F":  # F - lower half
            upper_col = (upper_col - lower_col) // 2 + lower_col
        elif x == "B":  # B - upper half
            lower_col = (lower_col + upper_col) // 2 + 1
        elif x == "L":  # L - lower half
            upper_row = (upper_row - lower_row) // 2 + lower_row
        elif x == "R":  # R = upper half
            lower_row = (lower_row + upper_row) // 2 + 1

    return lower_col * 8 + lower_row


def get_first_missing_seat(items):
    for i, x in enumerate(items, items[0]):
        if i != x:
            return i


if __name__ == "__main__":
    lines = helpers.get_lines(r'./data/day_05.txt')
    items = sorted(get_seat_id(line) for line in lines)

    part1 = items[-1]
    part2 = get_first_missing_seat(items)

    assert part1 == 930
    assert part2 == 515
