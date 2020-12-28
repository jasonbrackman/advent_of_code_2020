import helpers

from collections import defaultdict

r"""
   /\
  |  |
   \/
 (-1, -1)(-1, 1)
(0, -2)    (0, 2)
 (1, -1) (1, 1)
"""

WHITE = 1
BLACK = 0


def parse(lines):
    collection = []
    for line in lines:
        fin = list()
        gen = iter(line)

        try:
            current = next(gen)
            while current:
                if current in ("e", "w"):
                    fin.append(current)
                elif current in ("s", "n"):
                    fin.append(current + next(gen))
                current = next(gen)
        except StopIteration:
            collection.append(fin)
    return collection


def get_visited_positions(instructions):
    positions = defaultdict(int)

    for instruction in instructions:
        current_pos = helpers.HexPos(0, 0, 0)
        for move in instruction:
            current_pos += helpers.DIRS[move]
        positions[current_pos] = (
            positions[current_pos] + 1 if positions[current_pos] > 0 else 2
        )

    return positions


def get_neighbours(hexpos):
    return [hexpos + v for k, v in helpers.DIRS.items()]


def get_min_max_extents(hex_positions):
    xs, ys, zs = set(), set(), set()

    for key in hex_positions.keys():
        xs.add(key.x)
        ys.add(key.y)
        zs.add(key.z)

    return [min(xs), min(ys), min(zs)], [max(xs), max(ys), max(zs)]


def run():
    lines = helpers.get_lines(r"./data/day_24.txt")
    instructions = parse(lines)
    results = get_visited_positions(instructions)
    part01 = sum([v % 2 == 0 for k, v in results.items()])
    assert part01 == 354

    # black = sum((v % 2 == 0 for k, v in results.items()))

    for day in range(1, 101):
        min_extents, max_extents = get_min_max_extents(results)

        changes = list()
        for i in range(min_extents[0] - 2, max_extents[0] + 2):
            for j in range(min_extents[1] - 2, max_extents[1] + 2):
                for k in range(min_extents[2] - 2, max_extents[2] + 2):

                    t = helpers.HexPos(i, j, k)
                    k_neighbours = sum(
                        [(results.get(n, 1) % 2 == BLACK) for n in get_neighbours(t)]
                    )

                    colour = results[t] % 2 if t in results else WHITE
                    if colour == BLACK and (k_neighbours == 0 or k_neighbours > 2):
                        changes.append(t)
                    elif colour == WHITE and k_neighbours == 2:
                        changes.append(t)

        for c in changes:
            results[c] = results[c] + 1 if results[c] > 0 else 2

    black = sum((v % 2 == BLACK for k, v in results.items()))
    assert black == 3608


if __name__ == "__main__":
    run()
