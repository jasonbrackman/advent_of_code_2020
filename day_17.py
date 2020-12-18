import copy
import itertools

import display
import helpers

ACTIVE = "#"
INACTIVE = "."


def get_new_id(board, z, r, c, p2=False):
    current = "."
    try:
        current = board[z][r][c]
    except IndexError:
        pass

    func_ = get_neighbours2 if p2 else get_neighbours
    active_count = func_(board, z, r, c)

    if current == INACTIVE:
        return ACTIVE if active_count == 3 else INACTIVE
    elif current == ACTIVE:
        return ACTIVE if active_count in (2, 3) else INACTIVE


def get_neighbours(board, z, r, c):
    neighbours = []
    for z1 in range(-1, 2):
        for r1 in range(-1, 2):
            for c1 in range(-1, 2):
                if not z1 == r1 == c1 == 0:
                    try:
                        if r + r1 < 0 or c + c1 < 0:
                            raise IndexError
                        neighbours.append(board[z + z1][r + r1][c + c1] == ACTIVE)
                    except (KeyError, IndexError):
                        pass
    return sum(neighbours)


def get_neighbours2(board, zw, r, c):
    neighbours = []
    for z1 in range(-1, 2):
        for w1 in range(-1, 2):
            for r1 in range(-1, 2):
                for c1 in range(-1, 2):
                    if not z1 == w1 == r1 == c1 == 0:
                        try:
                            if r + r1 < 0 or c + c1 < 0:
                                raise IndexError
                            neighbours.append(
                                board[(zw[0] + z1, zw[1] + w1)][r + r1][c + c1]
                                == ACTIVE
                            )
                        except (KeyError, IndexError):
                            pass

    return sum(neighbours)


def create_new_board(data, grow):
    row_ = ["."] * grow
    board = [row_[:] for _ in range(grow)]
    board.append(row_[:])

    for row, col in data:
        board[row][col] = ACTIVE

    board.insert(0, [INACTIVE] * grow)
    board.append([INACTIVE] * grow)
    for b in board:
        b.insert(0, INACTIVE)
        b.append(INACTIVE)

    return board


def get_total(z):
    total = 0
    for key in sorted(z.keys()):
        total += list(itertools.chain.from_iterable(z[key])).count(ACTIVE)
    return total


def pprint_board(z):

    total = 0
    for key in sorted(z.keys()):
        total += list(itertools.chain.from_iterable(z[key])).count(ACTIVE)
        print(f"z={key}")
        for i in z[key]:
            print("".join(i))
        print("-" * 29)
    print(f"Total: {total}")


def part01(lines):

    # Create initial depth with input data
    z = dict()
    z[0] = [list(line) for line in lines]
    grow = len(z[0][0])
    for _ in range(6):
        # pprint_board(z)
        slices = []

        z[min(z.keys()) - 1] = [[INACTIVE] * grow] * grow
        z[max(z.keys()) + 1] = [[INACTIVE] * grow] * grow

        for d, v in z.items():
            new = []
            for r in range(len(v) + 1):
                for c in range(len(v[0]) + 1):
                    new_id = get_new_id(z, d, r, c)
                    if new_id == ACTIVE:
                        new.append((r, c))
            new_board = create_new_board(new, grow)
            slices.append((d, new_board))

        # this has to be updated after the fact since we don't want to alter the current board
        # before other slices have been checked.
        grow += 2
        for key, new_board in slices:
            z[key] = copy.deepcopy(new_board)

        # pprint_board(z)
    return z


def part02(lines):
    # Create initial depth with input data
    zw = dict()
    zw[(0, 0)] = [list(line) for line in lines]
    grow = len(zw[(0, 0)][0])
    for _ in range(6):
        slices = []

        zdepth = [r[0] for r in zw.keys()]
        wdepth = [r[1] for r in zw.keys()]

        min_depth = min(zdepth)
        max_depth = max(zdepth)
        min_hyper = min(wdepth)
        max_hyper = max(wdepth)

        for x in range(-1, 2):
            for y in range(-1, 2):
                for z_ in zdepth:
                    key1a = (z_ + x, min_hyper + y)
                    key1b = (z_ + x, max_hyper + y)
                    if key1a not in zw:
                        zw[key1a] = [[INACTIVE] * grow] * grow
                    if key1b not in zw:
                        zw[key1b] = [[INACTIVE] * grow] * grow

                for w_ in wdepth:
                    key2a = (min_depth + x, w_ + y)
                    key2b = (max_depth + x, w_ + y)
                    if key2a not in zw:
                        zw[key2a] = [[INACTIVE] * grow] * grow
                    if key2b not in zw:
                        zw[key2b] = [[INACTIVE] * grow] * grow

        for dw, v in zw.items():
            new = []
            for r in range(len(v) + 1):
                for c in range(len(v[0]) + 1):
                    new_id = get_new_id(zw, dw, r, c, p2=True)
                    if new_id == ACTIVE:
                        new.append((r, c))
            new_board = create_new_board(new, grow)
            slices.append((dw, new_board))

        # this has to be updated after the fact since we don't want to alter the current board
        # before other slices have been checked.
        grow += 2
        for key, new_board in slices:
            zw[key] = copy.deepcopy(new_board)

        # pprint_board(zw)
    return zw


def visualize(table):
    for i, key in enumerate(sorted(table.keys())):
        z, w = key
        display.generic_out(
            table[key], {INACTIVE: "black", ACTIVE: "random"}, "day_17", i
        )
    imgs = display.load_images_starting_with("day_17")
    imgs[0].save(
        r"./images/day_17.gif",
        save_all=True,
        append_images=imgs[1:],
        optimize=True,
        duration=100,
        loop=0,
    )


def run():
    lines = helpers.get_lines(r"./data/day_17.txt")
    p1 = part01(lines)
    p2 = part02(lines)
    assert get_total(p1) == 232
    assert get_total(p2) == 1620
    # visualize(p2)


if __name__ == "__main__":
    run()
