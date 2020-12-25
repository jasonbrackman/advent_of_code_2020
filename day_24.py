import helpers

from collections import defaultdict

"""
   /\
  |  |
   \/
 (-1, -1)(-1, 1)
(0, -1)    (0, 1)
 (1, -1) (1, 1)
"""


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


DIRS = {
    "e":  helpers.Pos(0, 1),
    "se": helpers.Pos(1, 1),
    "sw": helpers.Pos(1, -1),
    "w":  helpers.Pos(0, -1),
    "nw": helpers.Pos(-1, -1),
    "ne": helpers.Pos(-1, 1),
}


def get_visited_positions(instructions):
    positions = defaultdict(int)

    for instruction in instructions:
        current_pos = helpers.HexPos(0, 0, 0)
        for move in instruction:
            current_pos += helpers.DIRS[move]
        positions[current_pos] += 1

    for k, v in positions.items():
        print(k, v)

    return positions


def get_neighbours(hexpos):
    return [hexpos + v for k, v in helpers.DIRS.items()]



if __name__ == "__main__":
    lines = helpers.get_lines(r'./data/day_24.txt')
    instructions = parse(lines)
    results = get_visited_positions(instructions)
    part01 = sum([v % 2 != 0 for k, v in results.items()])
    assert part01 == 354

    xs = set()
    ys = set()
    zs = set()
    for key in results.keys():
        xs.add(key.x)
        ys.add(key.y)
        zs.add(key.z)
    min_extents = [min(xs), min(ys), min(zs)]
    max_extents = [max(xs), max(ys), max(zs)]
    print(min_extents)
    print(max_extents)


    neighbour_states = dict()
    for key in results.keys():
        neighbour_states[key] = get_neighbours(key)

    # print(get_neighbours(list(results.keys())[0]))
    # for idx in range(10):
