import display
import helpers

INPUT_PATH = r"./data/day_11.txt"
FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"


def get_adjacent_seats(lines, seat_pos):
    collection = []
    x, y = seat_pos
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if (i, j) != (x, y):
                if 0 <= i < len(lines) and 0 <= j < len(lines[0]):
                    collection.append(lines[i][j])

    return collection


def get_visible_seats(lines, seat_pos):
    collection = ["-"] * 8
    x, y = seat_pos

    count = 0
    idx = 1

    while True or count > len(lines):
        count += 1
        ii = 0
        for i in (x - idx, x, x + idx):
            for j in (y - idx, y, y + idx):
                if (i, j) != (x, y):
                    if 0 <= i < len(lines) and 0 <= j < len(lines[0]):
                        if collection[ii] not in ("L", "#"):
                            collection[ii] = lines[i][j]
                    ii += 1
        # print(idx, collection)
        if collection.count(".") == 0 or idx > len(lines):
            break
        else:
            idx += 1

    return collection


def _tests():
    RAW1 = """.......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....""".split()

    RAW2 = """#.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##""".split()

    assert get_visible_seats(RAW1, (4, 3)).count("#") == 8
    assert get_visible_seats(RAW2, (1, 9)).count("#") == 5
    assert get_visible_seats(RAW2, (8, 0)).count("#") == 4


_tests()


def create_board(lines, part2=False):
    seat_search = 5 if part2 else 4
    same = True
    new_lines = []
    for i in range(len(lines)):
        s = ""
        for j in range(len(lines[0])):
            seat_pos = lines[i][j]
            if part2:
                r = get_visible_seats(lines, (i, j))
            else:
                r = get_adjacent_seats(lines, (i, j))

            if seat_pos == EMPTY_SEAT and r.count(OCCUPIED_SEAT) == 0:
                s += OCCUPIED_SEAT
                same = False
            elif seat_pos == OCCUPIED_SEAT and r.count(OCCUPIED_SEAT) >= seat_search:
                s += EMPTY_SEAT
                same = False
            else:
                s += seat_pos
        new_lines.append(s)

    return new_lines, same


def part01(part2=False, generate_visualization=False):
    lines = helpers.get_lines(INPUT_PATH)
    index = 0
    while True:
        if generate_visualization:
            display.generic_out(
                lines, {".": "white", "L": "red", "#": "green"}, "day_11", index
            )

        index += 1
        new_lines, same = create_board(lines, part2=part2)

        if same:
            count = 0
            for line in lines:
                count += line.count(OCCUPIED_SEAT)
            return count
        lines = new_lines


if __name__ == "__main__":
    generate_visualization = True

    p1 = part01()
    assert p1 == 2354

    p2 = part01(part2=True, generate_visualization=generate_visualization)
    assert p2 == 2072

    if generate_visualization:
        imgs = display.load_images_starting_with("day_11_")
        imgs[0].save(
            r"./images/day_11.gif",
            save_all=True,
            append_images=imgs[1:],
            duration=5,
            loop=0,
        )
